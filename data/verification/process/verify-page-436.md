# Verification process log — verify-page-436


## [2026-09-14T01:24:58.139Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 436 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-436.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-436.json. Write /home/sfmqrb/git/rishe/data/verification/page-436.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 436` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:24:59.196Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:24:59.974Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:24:59.990Z] TOOL RESULT

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


## [2026-09-14T01:25:00.473Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-436.txt"
}
```


### [2026-09-14T01:25:00.493Z] TOOL RESULT

```
1	=== PDF page 436 (book page 406) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sed : to sit, to place; also to place a step, to go  (refs POK:884,887; KLN:1075)  PART 2
4	#1 (parent #0) [Germanic] refs=AHD | 
5	  #2 (parent #1) [English] refs=None | sit, set, settle, nest, seat, saddle
6	#3 (parent #0) [Greek] refs=AHD | 
7	  #4 (parent #3) [English] refs=None | chair
8	#5 (parent #0) [Latin] refs=AHD | 
9	  #6 (parent #5) [English] refs=None | sedan, soil, session, hostage, president
10	--- entry 1 ---
11	ROOT [Akkadian] Šedŭ : devil, mad person  (refs AKD:69)
12	#1 (parent #0) [Aramaic] refs=BQT:1320 | šĕdâ, šâtân : demon
13	  #2 (parent #1) [Persian] refs=BQT:1320 | šeydâ «شیدا» : crazy, frenzied (with love)
14	  #3 (parent #1) [Arabic] refs=BQT:1320 | šeytân : devil
15	    #4 (parent #3) [Persian] refs=MON | šeytân «شیطان» : devil
16	  #5 (parent #1) [Hebrew] refs=KLN:1385 | sâtân : adversary
17	    #6 (parent #5) [English] refs=None | Satan
18	--- entry 2 ---
19	ROOT [Indo-European] Segh : to hold, overrule  (refs POK:888)
20	#1 (parent #0) [Avestan] refs=POK:888 | haz : to gain ; hazah : victory
21	#2 (parent #0) [Greek] refs=POK:888; AHD | sxĕma : a holding, form, shape ; sxolĕ : a holding back, stop, rest
22	  #3 (parent #2) [Latin] refs=None | 
23	    #4 (parent #3) [English] refs=AHD | scheme, sketch ; school, scholar
24	--- entry 3 ---
25	ROOT Sĕi 1 -> redirect to Sĕ 1
26	--- entry 4 ---
27	ROOT Sĕi 2 -> redirect to Sĕ 2
28	--- entry 5 ---
29	ROOT Sĕi 3 -> redirect to Sâi 2
30	
```


## [2026-09-14T01:25:01.722Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-14T01:25:03.032Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-436.json",
 "description": "Read page 436 source JSON"
}
```


### [2026-09-14T01:25:03.071Z] TOOL RESULT

```
{
  "pdf_page": 436,
  "book_page": 406,
  "entries": [
    {
      "root": {
        "name": "Sed",
        "lang": "Indo-European",
        "refs": "POK:884,887; KLN:1075",
        "gloss": "to sit, to place; also to place a step, to go"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sit, set, settle, nest, seat, saddle", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "chair", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sedan, soil, session, hostage, president", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Šedŭ",
        "lang": "Akkadian",
        "refs": "AKD:69",
        "gloss": "devil, mad person"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "BQT:1320",
          "words": [
            {"translit": "šĕdâ, šâtân", "gloss": "demon", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1320",
          "words": [
            {"translit": "šeydâ", "gloss": "crazy, frenzied (with love)", "script": "شیدا"}
          ],
          "note": null,
          "quote": {
            "text": "جز من اگرت عاشق شیداست بگو - ور میل دلت به جانب ماست بگو",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "BQT:1320",
          "words": [
            {"translit": "šeytân", "gloss": "devil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "šeytân", "gloss": "devil", "script": "شیطان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN:1385",
          "words": [
            {"translit": "sâtân", "gloss": "adversary", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Satan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Segh",
        "lang": "Indo-European",
        "refs": "POK:888",
        "gloss": "to hold, overrule"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:888",
          "words": [
            {"translit": "haz", "gloss": "to gain", "script": null},
            {"translit": "hazah", "gloss": "victory", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:888; AHD",
          "words": [
            {"translit": "sxĕma", "gloss": "a holding, form, shape", "script": null},
            {"translit": "sxolĕ", "gloss": "a holding back, stop, rest", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "scheme, sketch", "gloss": null, "script": null},
            {"translit": "school, scholar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Sĕi 1", "redirect": "Sĕ 1"},
      "nodes": []
    },
    {
      "root": {"name": "Sĕi 2", "redirect": "Sĕ 2"},
      "nodes": []
    },
    {
      "root": {"name": "Sĕi 3", "redirect": "Sâi 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:25:05.431Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AKD','BQT','MON','AHD','WLD','BRT','HRN','HUB','PHD','NYB','IEC','SYN','SKT','FSD','WEB','ARY','AFM','PLA','FVQ','CHEUNG']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T01:25:06.591Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
CHEUNG MISSING
```


## [2026-09-14T01:25:11.310Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AKD','BQT','AHD','WLD','BRT','IEC','SYN','SKT']:\n    v=d[k]; print(k, '|local:', v.get('local_file'), '|offset:', v.get('page_offset'))\n\""
}
```


## [2026-09-14T01:25:11.983Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:25:12.429Z] TOOL RESULT

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
---
POK |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AKD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt |offset: leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BQT |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
AHD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
WLD |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
BRT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
IEC |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


### [2026-09-14T01:25:12.473Z] TOOL RESULT

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


## [2026-09-14T01:25:20.673Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\n# POK page 884,887 -> which part? POK_02: leaf = p - 344 ; POK_03: leaf = p - 762..766\npython3 - <<'EOF'\nimport re\nfor f in ['POK_03.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print(f,len(pages))\n    for leaf in [884-766,884-762,888-766,888-762]:\n        pass\nEOF\ngrep -n \"seĝh\" POK_03.txt | head -20"
}
```


### [2026-09-14T01:25:21.642Z] TOOL RESULT

```
POK_03.txt 430
```


## [2026-09-14T01:25:21.887Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sed-\" POK_03.txt | head -30; echo ===; grep -n \"σχῆμα\\|σχολή\\|sxhma\" POK_03.txt | head"
}
```


### [2026-09-14T01:25:21.949Z] TOOL RESULT

```
Exit code 1
243:wo  ein  Ast  vom  Stamme  aasgegangen  ist');  wohl(?)  -ozdo-s  ,(am  StammeV ansitzend',  s.  Präfix  's-,   o-  und  sed-  ,sitzen'.
1575:sed-  , sitzen',  ursprüngl.  nur  aoristisch,  punktuell  ,sich  setzen'  (ai.),  später  ak
1577:sed-to- , gesessen',  Subst.  ,Sitz';  sed-ter-  ,der  Sitzer',  sed-ti-  ,das  Sitzenvl
1578:sed-lo-m,  sed-lä,  sed-ro-m,  sed-rä,  sedos-  n.,  sodio-m  .Sitz'.  ^
1585:lat.  sedeö,  -ere,  sedi  ^sitzen'  (Präs.  auf  Grund  des  ursprüngl.  außer- präs.  St.  sede-;  Perf.  aus  *se-zd-ai),  umbr.  sersitu  ,sedetö',  zefef  ,sedens', aiidersesust  ,intersiderit',  lat.  sedö,  -are  , beruhigen'  (vielleicht  =  mnd.  säten ^beruhigen*.  Wissmann  Nom.  postv.  112,  1);  air.  sa{i)did  (*se(i)did),  , sitzt', Fut.  seiss  (*sed-s-ti)j  adsuidi , schiebt  auf,  verzögert,  hält  auf  (Kaus.  *sodeiet] sonst  durch  Denom.  suidigud  , setzen'  verdrängt);  cjmr.  seddu  ,sitzen';
1587:lit.  *sMmi  und  s^dziu,  sedime  {*sed-),  Inf.  sedeti  , sitzen',  Partiz.  Perf. ■  sed^s  {wie  apr.  sidons  , sitzend',  aksl.  sed^),  aksl.  sezdg,  sädäti  ,sitzen' ;  dane- ben S  in  aöech.  sedeti  (:  lat.  sedsre);  lit.  sidu,  sesti,  lett.  sest  (^sestei)  ,sich setzen',  aksl.  sesti  ds.  (Präs.  sedg,  s.  unten),  Kaus.  saditi  (*södeiö)  , setzen, pflanzen',  lit.  sodinü  sodmti  , setzen,  pflanzen',  apr.  mit  (*Ö)  saddinna  , stellt'; aksl.  s^d(^  , setze  i?iich'  (Inf.  sisti)  beruht  auf  sekundärer  Nasalierung  von *sSdg  (=  lit.  sedu)-  auch  apr.  syndens,  sinda{n)ts  ,sitzend'  zeigt  Nasalie- rung; s.  Kuiper  Nasalpräs.  192  f.,  wo  ai.  äsandi  , Sessel'  zu  äste  , sitzt' (oben  S.  342  f.)  gestellt  wird;
1591:*sed-to-  in  ai.  sattd-  , gesessen',  av.  pasuS-hasta-  m.  , Hürde  (*Nieder- lassung)  für  Kleinvieh',  lat.  ob-sessus  usw.,  aisl.  ags.  sess  m.  ,Sitz',  vgl. auch  lit.  Partiz.  sestas  und  lit.  söstas  m.  , Sessel',  apr.  sosto  f.  ,Bank'; *sed-ti  in  ai.  satti-  ,das  Sitzen^,  ni'§atti-  ,das  Sitzen,  Sitz',  av.  ni-sasti- ,Begattung',  lat.  sessiö  ,Sitzung^,  aus  *sessis'^  ai.  sdttar-  m.  der  ,Sitzer^, lat.  ad-^  oh-,  pos-sessor]
1594:Nomen  actionis  sed-  in:  ai.  Akk.  sddam,  Dat.  sac^e,  mit  e-  Erweiterung in  lat.  sedes  f.  ,Sitz'  (sedibus  =  lit.  Inf.  sM-ti:  1  PI.  s^di-me),  umbr.  set^si.
1596:,in  söde';  Nomen  agentis  als  2.  Kompos.-Glied:  ai.  apsu-sdd-  ,der  in  ^en  ' Wassern  wohnt^  av.  maidyöi-säödm  (Akk.)  ,d.er  in  der  Mitte  wohnt';  \^^: prae-ses  , Vorsitzender',  de-ses  ,träge'  =  air.  dM  ds.  (i-Flexion  sekundär),'" zu  deess  ^Trägheit'  (*de-sed-tä)]  mit  lat.  suhsidium  ^Unterstützung'  vgl.  air[ ^ fothae  m.  n.  , Grundlage^  aus  *upo-sodiom,  zu  air.  swid^e;  fei
1600:lok.  iXXä-  ^a&edqa  Hes.  ==  lat.  sella  (*sed-la)  ,Stuhl  Sessel',  gall.  sedlon ,Sitz',  got.  suis,  ags.  seil  n.,  ahd.  sezzal  m.  ,Sitz,  Sessel'  {*sed-lo-)j  nsorb. «edZo  ,Sitz';  aber  aksl.  sedlo  , Sattel'  ist  *sed^lo,  vgl.  aksl.  o^sed^lati  ,satteln*, arm.  eti  ,Platz,  Stelle'  (dazu  auch   teil  ,Ort,  Stelle');
1601:as.  sethal  m.  , Sitzen,  Sitz',  Dat.  sedle  ,(zum)  Sonnenuntergang',  ahd. sethaly  sedal  n.  m.  ,Sitz,  Wohnsitz,  Stätte'  (idg.  *setlo'  aus  *sedtlo)'j  davon  - ahd.  sidilo  ,agricola',  mhd.  sidilen  ,siedeln';  germ.  ^saduh-  in:  aisl.  sgdull^ ags.  sadol,  ahd.  saiul^  satal  , Sattel'  ist  ostidg.  Lw.(?);  vgl.  oben  slav. *sed^lo  aus  *sedu-lo-  n.;  daneben  (im  ar.  geneuertes?)  *sed-tlom  in  av.  hastra- n.  , Versammlung'  =  ai.  satträ-  n.  , Feier,  Fest'.
1615:O'Zdos  , (ansitzender)  Zweig,  Ast*^,  s.  dort;  auch  gr.  b'^og  , Gefährte, Diener'  aus  *o-zdos  ,*Beisitzer* ;  oder  eher  zu  B.  *sed-?
1617:B.  *sed-  in  der  Bed.  ,gehen',  aus  Verbindung  mit  Präfixen  entstanden.
(eval):1: == not found
```


## [2026-09-14T01:25:27.674Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nimport re\n# find leaf containing 'sed-  , sitzen'\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'sitzen\\', ursprüngl' in p or \"sed-  , sitzen'\" in p:\n        print('LEAF',i)\n    if 'B.  *sed-  in  der  Bed.' in p:\n        print('LEAF_B',i)\n    if 'seĝh-' in p or 'segh-' in p:\n        print('SEGH LEAF',i, p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:25:28.716Z] TOOL RESULT

```
LEAF 119
LEAF_B 122
```


## [2026-09-14T01:25:32.209Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(116,128):\n    print('=== leaf',i, repr(t[i][:120]))\nEOF"
}
```


### [2026-09-14T01:25:33.321Z] TOOL RESULT

```
=== leaf 116 '  dörre*;  unsicher  gr.  aijx(^ög  m.  ,Dürre,  Trockenheit, Schmutz*,  falls  aus  *sau-k-smo-  von  einer  Wurzelvari'
=== leaf 117 'g,  ausgegangen  von  *G-cpBL,  a-(pi(p^ die  als  aq)-€i,  G(p-L{v)  aufgefaßt  wurden;\nlat.  sihi,  se,  päl.  sefei, '
=== leaf 118 'art,  Charakter*,  aksl.  sobtstvo  , Eigenart,  Wesen^,  und  mit su-   aksl.    svoboda   .Freiheit*   (ursprgl.    , '
=== leaf 119 "ie    Grundlage  voji   germ.   *selba-   ,selbst'  (-bho-  wie  oben *s(u)ehho-),  got.  silba^  anord.  sjdlfr,  ags. "
=== leaf 120 " =  mnd.  säten ^beruhigen*.  Wissmann  Nom.  postv.  112,  1);  air.  sa{i)did  (*se(i)did),  , sitzt', Fut.  seiss  (*"
=== leaf 121 'Flexion  sekundär),\'" zu  deess  ^Trägheit\'  (*de-sed-tä)]  mit  lat.  suhsidium  ^Unterstützung\'  vgl.  air[ ^ fothae  '
=== leaf 122 "ir.  net  ,Nest^,  cvmr.  nyth  ^Nest,  Wohnung*, coru.  neidj  bret.  nez,  neiz  ds.,  ahd.  ags.  nest  n.  ,Nest';  "
=== leaf 123 "le';  lett.   segt  ^decken';  apr.  sagis  , Schnalle,  Hufnagel';  aksl.  ^gf^^ ,ergreifen',   s^zwh   ,KlafterS  pri-"
=== leaf 124 "  PN  Segi8ü(*-ö),  Sego-märos,  GN  Segomö{n),  f.  Segetä,  ON  Sego-dünon,\n*\n889\nß^go'hriga,  Segontion,  mir.  seg  "
=== leaf 125 " f.  ^Anlauf,  Anstur Wurf,  Geschoß^;\nb.  ,säen':  ai.  sira-  n.  ,SaatpflugS  sitä  ,Furche'  (*die  Besäte);  lat.  "
=== leaf 126 'gelassen;  beigesetzt^;  sileö, .Ire  ,ruhen,  aufhören  (z.  B.  vom  Winde),  schweigen^  =  got.  anasilan  ,(vom ■\\V'
=== leaf 127 "örtl. ,zauberisch',    ablaut.    siabair    ,Phantom,    Gespenst',    slahraid    ,verzaubert,\n892  ^\nverwandelt'  {*s"
```


## [2026-09-14T01:25:39.483Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[122][-2500:])\nprint('#########LEAF123')\nprint(t[123][:4000])\nEOF"
}
```


### [2026-09-14T01:25:40.583Z] TOOL RESULT

```
ich^,  av.  nishidaiti,  ap.  niyasädayam, arm.  nstim,  s.  o. ;
O'Zdos  , (ansitzender)  Zweig,  Ast*^,  s.  dort;  auch  gr.  b'^og  , Gefährte, Diener'  aus  *o-zdos  ,*Beisitzer* ;  oder  eher  zu  B.  *sed-?
pi-s(e)d-  , daraufsitzen  =  drücken*:  ai.  pldayati  (*pi-zd-eiö)  , drückt, unterdrückt;  quält^  (Perf.  pipldi-^  pldä  ^Druck,  Schmerz'),  gr.  Ttiet^o) , drücke^  (*7rL-ae6iüi).
B.  *sed-  in  der  Bed.  ,gehen',  aus  Verbindung  mit  Präfixen  entstanden.
Ai.  ä-sad-  , hintreten,  hingehen,  gelangen*,  vt-sad-  ,sich  zur  Seite  be- geben, verschwinden',  sly.  pazdayeiti  ^verscheucht  (macht  weggehen*),  av. apa-had'  ,sich  wegsetzen,  ausweichen*,  äsnaoiti  {*ö-zd-neu-ti)  ,geht  heran' (s.  886  äsna-)]  gr.  bdog  ,Weg',  ödiTTjg  , Wanderer',  oösvo)  , wandere';  aksl. chodz  ,Gang',  choditi  , gehen',  ablaut.  hdh  ^gegangen';  slav.  ch-  aus  idg.  s- wohl  zunächst  hinter  pri-  und  u-  entstanden.
Hierher  vielleicht  als  Kompositum  mit  einem  zum  Pron.  ko-,  kio-  (oben S.  609)  gehörigen  Adv.  *k{e-:  av.  syazd-  ,zurücktreten  vor,  aufgeben', sUdyamnä  , zurückweichende',  sizdyö  ,aufgebend*,  stzdra-  , scheu'  und  lat. cedo  (*ke-zd-o)  ,schreite  einher;  weiche,  gebe  nach^,  sowie  necesse  , not- wendig', falls  (?)  aus  *ne-kezd-ti-s  ,es  ist  kein  Ausweichen'.
WP.  II  483  ff.,  WH.  II  507 ff.,  511,  Ej\P  917  ff.,  Trautmann  248,  258  ff.,  273.
1.  seg-  ,säen';  nur  lat.  und  kelt.
Lat.  seges,  -etis  f.  ,Saat',  Seia  , Göttin  des  Säens'  (*segia)]  acymr.  sege- ticion  ,prolis',  mcymr.  se,  he  ,Same^,  he-Uj  ncymr.  hau  ,säen',  hauaf ,ich  säe'.
WP.  II  480,  WH.  II  509 f.;  vgl.  2.  se(iy  ,säen'.
2.  seg-,  nasaliert  seng-  ,heften,  sich  anhängen,  berühren'.
Ai.  sdjati  ,anhängen'  (mit  a- , anheften',  vgl.  Perf.  sasaüja),  Kausat.  saüjaya- ti , anheften',  Partiz.  saktd-  ,anhaftend,  angeheftet',  sakti-  f.  ,das  Zusammen- hängen', sandga-  ds.,  apers.  frä-hajam  ,ich  liess  aufhängen'  (arisch  *sanjan- ti  =  slav.  sezeU),  av.  vohuna-zga-  (spä)  ,der  sich  ans  Blut  heftende  Bluthund';
mir.  sen  (*segno-)  ,Fangnetz',  cymr.  hoenyn  i^sogno-),  umgelautet  hwynyn ds.;  gallo-lat.  sagum  {^sogom  oder  *Segom)  ,Soldatenmantel';  mnd.  mhd. Senkel  ,Schnürriemen',  nhd.  ßchnürsenkel,  Schuhriemen';  lit.  segti  ,heften', Iter.    sagyti,   ablaut.    sägas   , Schleife   zum   Befestigen',   sagä  f.   ,Klammer,
888
f  ^
Schnal
#########LEAF123
le';  lett.   segt  ^decken';  apr.  sagis  , Schnalle,  Hufnagel';  aksl.  ^gf^^ ,ergreifen',   s^zwh   ,KlafterS  pri-s^Sti   ,berühren'   und   .schwören',  P''*'-»»*! ^Eid*;  ohne  Nasal:  Iter.  sagati  ,ra^SLv',  po-sagati,  po-sagngti  ,nubere'  (^^ den  Hochzeitsbrauch  bezogen).
WP.  n  448  f.,  480 f.,  482  f.,  WH.  II  464,  Trautmann  252,  Kuiper  Nasal- präs.  195.
segb-,  segbi-,  seghu-  .festhalten,  halten;   einen  im  Kampf  überwältige^ Sieg';  seghos-  n.  ,Sieg',  seghu-ro-  .siegreich'.
Ai.  sdhate  .bewältigt,  vermag,  erträgt',  sdhas-  n.   .Gewalt,   Sieg'  ==  4, hazah-  n.  ,Gewalt(tat),  Raub',  ai.  saksa-,  saksdna-  .Bändiger,  Sieger',  sah .gewaltig,  siegreich'  (:  gr.  ixvQÖg,  dxvQÖg,  vgl.  auch  germ.  *sigus-),  av.  h .sich  bemächtigen,  erwerben'  (Präs.  *zgh-ö,  z.  B.  1.  pl.  Opt.  zaemä  =  ^ axoTi,isv,    redupl.    *se-zgh-o-,    assimiliert    av.    zaza-,    z.    B.    3.    PL    zaz9n Part.  Perf.  Akt.  za-z-va  Nom.   Sg.,  za-z-us-u  Lok.   PL;   dehnstufig  außer Perf.  akt.  ai.  säsdha  auch  Med.  sasähi,  Partiz.  säJivds-,P rä.s.  sdhati^  Imp. sak?va  ,sei  siegreich';
Gr.  excü  {slxoy,  *daxov,  eaxrjy^cc,  £^to  und  axrjou))  , halte,  besitze,  habe'; hora.  "EycTWQ,  lesb.  €'/.ro)Q  , Zurückhalter',  agig  , Verhalten,  Befinden'.  Ixit- AÖg  .gewohnt,  leidend'.  ixvQog,  ablautend  öxvQÖg  .haltbar,  sicher,  befestigt^ (:  ai.  sahuri-,  das  ursprgl.  o-St.  war),  ixhlrj  .Pflugsterz'  (=  cymr.  haeddel f.  ds.  <  *seghedhlä),  ä^rjx^g  {*d'dia-8xr]g)  .ohne  Einhalt  etwas  tuend';  vom -es-St.  eV-s^gg'  sicpvi^g  Hes.,  svs^ia  , Wohlbefinden',  e^fjg  ,der  Reihe  nach'  * (Gen.  eines  Adj.  *€^6g),  i^slrjg  ds.;
o-stufig:  e^'Oxog  , hervorragend',  Adv.  e^oxov,  £?oxof  .weitaus',  danach hom.  5xof  , weitaus',  oxog  , Halter,  Bewahrer',  dxfiw  .halte,  stütze';  halte aus,   (er) trage',   öxsvg  , Riemen,  der  den  Helm  festhält,   Spange,  Riegel';
mit  ö:  eicjxict)  ,tische  auf,  bewirte  reichlich'  (Dehnung  nach  dem  Vor- bild der  Komposita);  dv-,  Sc-,  xar-,  ovv-o-kcoxv  (i^  Anschluß  an  Perf.- Bildungen,  wie  Sttiotit}  produktiv  gewordene  Dehnung);
schwundstufig:  Yaxo)  {*si-zgh-ö)  ,halte  an,  habe',  tV^ag  f.  , Anker',  ax^tr (s.  0.),  axed^-hiv,  -elv,  -sfxev  ,halten',  ä-axsTog  , unaufhaltsam;  unerträglich (Leid)',  axsaig  f.  , Haltung,  Zustand',  axhXiog  , unermüdlich,  hartnäckig' (,*aushaltend'),  a^is&gög  ,knapp,  genau'  (,*eng  anliegend'),  oxsdöv  ,nahe, beinahe'  (,*sich  eng  woran  haltend'),  axegög  .ununterbrochen',  iitiax^ed^ Adv.  ds.,  axfjf^a  , Haltung,  Gestalt.  Form'.  oxoXrj  , Einhalten,  Ruhe,  Muße; (wissenschaftliche)  Beschäftigung  in  Mußestunden'  (ein  damit  ablautendes *Hax(xXog  ,wer  sich  nicht  halten  kann'  vermutet  man  als  Grundlage  von daxocXdu),  daxdllca  ,bin  unwillig,  ungehalten,  zornig');  iax^gy  -vog  ,Stärke' (*/t-(7xu-s)  zu  ai.  vi-sah-  ,in  der  Gewalt  haben';
kelt.
```


## [2026-09-14T01:25:53.030Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AKD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(74,80):\n    print('=== leaf',i)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-14T01:25:54.094Z] TOOL RESULT

```
112
=== leaf 74
ae  dies  usw.,  Jfowtag,  3)  fifiiga  'Aqiws,  Martis dies  usw.,  fi'anz.  marä\,  engl,  thtiesdaj,  deutsch  (dial.)  Äestag,  und  viell. doch  auch  Dienstag,  4)  ?/^/pa  'Egf/ov,  Mercurii  dies  usw.,  franz.  mercreAi, engl.  wednesAaj,  5)  nfxiqa  Ai.ög,  Jovis  dies  usw.,  engl,  thiirsdaj,  Donners- tag, 6)  ijf^^ga  'Aq)QoSlT>]g,  Veneris  dies  usw.,  i^mtag,  7)  i'jfii'^a  Kqövov, Satiirni  dies  usw.,  engl.  saturAaj,  niederdeutsch  safe>-dach,  gehen  durch mehrfache  Übersetzungen,  wenn  auch  nicht  unmittelbar,  so  doch  mittelbar insofern  auf  eine  Benennung  der  Tage  nach  den  babyl.  Göttern  1)  Samas, 2)  Sin,  3)  Nergal,  4)  Nabu,  5)  Mardtik,  6)  Btar,  1)  Kaimänu,  zurück, als  der  7tägigen,  auf  hellenistischem  Boden  entstandenen  Woche  eben  die 7  urspr.  babylonischen  Planetengötter  zugrunde  liegen.
Die  akk.  Monatsnamen  1)  Nisannu,  2)  Ajjaru,  3)  Simänu,  4)  Düzu (urspr.  Tamüzu),  5)  Abu,  6)  Ulülu,  auch  Elidu,  7)  Tasrltu,  8)  Arah-samna,
1)  Eig.;  in  ihr  (unter  dem  Horizont  gelegenes)  Haus  eintreten.
2)  Eig. :  aus  ihrem  (unter  dem  Horizont  gelegenen)  Hause  herausgehen.
      65       —
9)  Kislimu,  10)  Tebetu,  11)  Sabätu,  12)  Addaru  :  >>  späthebr.  u.  arani. 1)  Nlsän,  2)  ^Ijjär,  3)  Smän,  4)  Tammüs,  5)  Ab,  6)  'iM,  7)  mn, 8)  Marhes'Wän,  9)  /sTwZm,  10)  Teftci!,  11)  &&äf,  12)  'Ädär,  die  dann  z.T. auch  ins  Syr.-Arab.  und  neuerdings  auch  ins  Türkische  übergegangen sind.  Dazu  auch  noch  der  aram.  (syr.-arab.  und  tiirk.)  Monatsname  Kämm <C  akk.  Kinünu,  Kamlnu  (s.  schon  oben  S.  32  f.).
Zu  akk.  sabattu  und  nubattu  für  bestimmte  Monatstage  s.  unten  S.  67.
akk.  isten  eins  (wohl  <C  sum.  aS-tan)  :  >  wohl,  trotz  des  ',  spät- hebr. 'aSti  in  "asie  'ämr  elf.  akk.  sinipu,  sinipätu  zwei  Drittel  : >  altaram.  snb  u.  'snb  dass.;  auch  hebr.  pt-sdnajim  viell.  davon  beein- flußt, akk.  hism'^  sechzig  (eig.  ein  Sechstel,  nänil.  der  Vollzahl  360)  : ^  wohl  mand.  Söm  Bez.  für  den  12.  Teil  einer  Stunde.  Deutsch  Schock hat  dagegen  mit  akk.  stiSsu  keinen  etymologischen  Zusammenhang,  während sachlich  die  Kechnung  nach  Sechzigern  allerdings  im  letzten  Grunde  auf das  babylonische  Sexagesimalsysteni  zui'ückgehen  wird.
17.   Religion,  Kultus  und  Mythus.
akk.  palähu  sich  fürchten  vor,   dann  spez.   (die  Götter)   fürchten, verehren,  ihnen  dienen 
=== leaf 75
inen    :    davon   vieU.   beeinflußt    hebr.    raä   panim  in    Verb,    mit Jahwe.     Vgl.  auch  oben  S.  10  zu  akk.  dagälu  pän.  Zu  pers.-arab.
den,  dm  Keligion  s.  oben  S.  24  unter  akk.  denu.
akk.  Pa.  sullü  anflehen,  (^u  den  Göttern)  beten  :  (in  dieser  Bed.) ^  aram.  Pa.  salll  beten,  sdlötä^  Gebet  O  arab.  sallä  u.  salät,  äth.  sallaja u.  salöt).  akk.  Pa.  sullü  anflehen,  beten  :  dazu  mehrfach  der  1. 1.
sälä  der  hebr.  Pss.  gestellt;  aber  sehr  zweifelhaft.
akk.  loräbu-  segnen,  beten  :  ^  viell.  doch,  ti'otz  anderer  Möglich- keiten, südarab.  krb  segnen,  shrb  weihen,  mkri  (auch  noch  heute  mikräb) Heiligtum,   Tempel  (>  wohl  äth.  mekwräb  Heiligtum).  akk.  aräru
verfluchen  :  >>  viell.  hebr.  \lrar  dass.
akk.  naqu'^  (ein  Trankopfer)  spenden,  allg.  opfern,  dann  spez.  auch
1)  Griech.  als  ahaaoq  wiedergegeben,  wie  entsprechend  die  600,  akk.  neru,  als j-^fo?,  und  die  3600,  akk.  Sar,  als  aä^oq.
2)  Urverwandt  mit  hebr.  herek,  aram.  harrek,  ai'ab.  u.  äth.  häraka.
3)  Damit  urverwandt  hebr.,  aram.,  arab.  nqj  rein  sein.
9
      66  
Schafe  opfern  :  >-  wohl  syr.  nuqqi  opfern,  S}-r.  u.  christl.-pal.  nuqqdjä Libation,  späthebr.  (wohl  <;  aram.)  manaqqit  Opferschale  O  syr.  nwneqJtri), sowie  syr.  neqja  Schaf  (s.  hierzu  bereits  oben  S.  50).  akk.  nakäsu
(den  Kopf)  abhauen,   spez.  (dem  Opfertier)  die  Kehle  durchschneiden  :  > wohl  aram.  ndk<is  schlachten,  opfern,  niJcsata  Schlachtung,  Opfer. akJc.  Pa.  qurruhu  nahebringen,  spez.  v.  Opfer  darbringen  :  davon  wohl beehiflußt  aram.  qarreh,  späthebr.  hiqrib  Opfer  darbringen,  aram.  qurhdna, späthebr.  qorhan  (NT  xogßäi',  xoQßaväi)  Opfergabe.  [akk.  zihii  Opfer,
selten  u.  als  Verbuni  niclit  gebräuchlich;  daher  vieU.  (aber  lautgesetzlich entwickelt)  <<  westsem.  (hebr.  sähnh,  aram.  (hhah ,  arab.  dahaha,  äth. zabha).]  akk.  reScti  das  Erste,  der  beste  Teil  (als  Opfergabe):  davon
viell.  beeinflußt  hebr.  reStt  in  dieser  Bed.
akk.  zaraqu  sprengen  (von  Wasser,  Öl  usw.  im  Kultus)  :  davon viell.  beeinflußt   die  gleiche  kulttechn.  Bed.  von  hebr.  saraq.  akk.
sdlälni  besprengen  (mit  Wasser  usw.)  :  ^  viell.  aram.  zalah  sprengen, und  viell.  darauf  zurückgehend  auch  hebr.  sälah  .(Sünde)  vergeben.
akk.  l:ap<rru  bestreichen  (z.  B.  mit  Erdpech,  laipru  s.  oben  S.  60), abwi
=== leaf 76
gehend  hebr.  Upper  als  kult- techn. Bez.  für  sühnen.
akk.  quddusii  glänzend,  rein,  spez.  kiüttech.  qudduSu  reinigen  :  > viell.,  dann  freüicli  früh,  hebr.  qiddas  heiligen,  weihen,  qados  heUig  (auch phön.),  aram.  qaddei  u.  qaddlAa  dass.  O  wohl  südarab.,  arab.,  äth.  qds  in der  loilt.  Bed.).  Vgl.  auch  noch  unten  S.  68  zu  qadiStu  Hierodule  und oben  S.  38  zu  syr.  qddns/i  Ohrring.  akk.  jnt  pi  wörtl.  Mundöffuung,
eine  babyl.  kultische  Reinigungszeremonie  :  davon  abhängig  wohl  mand. peldä  wörtl.  Öffnung,  als  Bez.  einer  lail tischen  Speisung.
Zu  akk.  himänu  eine  kultisch  verwendete  Art  Kuchen,  s.  oben S. 38.
Zu  aldv.  hafa  sündigen,  s.  bereits  oben  S.  11.
akk.  tajjäru  (eig.  zurücldcehrend ,  sich  wieder  zuwendend)  barm- herzig, gnädig  (von  der  Gottheit)  :  davon  viell.  beeinflußt  hebr.  Süh  \ll od.  h  von  Gott,  mand.  (auch  avoIiI  palm.  i)  tajjübä  barmherzig  (aus  aram. ^  arab.  tawwäb).  akk.  paSähu  sich  besänftigen  (von  der  erzürnten
1)  Falls  liier  nicht  doch  tjru,  d.  i.  das  akt.  tajjarti,  zu  lesen  ist.
      67      
Gottheit)  :  >  viell.  (doch  kommen  hier  noch  allerlei  andere  Möglichkeiten in  Betracht)  hebr.  päsah,  O  aram.  pishä  usw.,  LXX  n.  NT  näaxa.  Passah).
akk.  nnbbil.  numhfi  wehklagen  (Pa.  zu  nnhü  rufen,  St.  «&')  :  ^ maud.  numhdjil  Trauer,  namlii  trauern.  akk.  sa^Kldu  klagen,  trauern:
;>  viell.  hebr.  säpad.  jüd.-aram.,  christl.-pal.  sdpad.^
akk.  Saqqn  Sack  (für  Geti-eide,  Mehl  usw.),  und  Büßergewand  : >  wohl  hebr.  sag,  altaram.  PI.  Sqqii,  später  saqqti  O  äth.  Sag).  Aus  dem Semit.  >  giüech.  adxxog,  lat.  Saccus  usw.,  Sacl:
Zu  akk.  nigfdu,  ningfitu  Spiel,  Musik,  sowie  zu  zamftru  singen und  spielen  s.  bereits  oben  S.  29.
akk.  sahattu,  auch  (sekundär)  sapattu  (Etym.  noch  unklar),  15.  Tag  des Monats,  Tollmondstag  :  >  wohl  sicher  hebr.  sahhät  Sabbath  O  aram. iahbdtct,  ^  äth.  sanhat;  ferner  aüßßaror,  saibatitm  usw.  bis  franz.  samedi und  andererseits  Samstag,  sowie  jüd.-deutsch  Schahhes).  Dazu  viell.  auch ägypt.  snit-t^  15.  Tag  des  Monats.  akk.  nuhattti  Abend,  Yor-
abend,  Festvorfeier  :  in  Anlehnung  daran   viell.  neuhebr.  'äreb  Sabbat, jüd.-aram.  'ärribtcij.napaaxtvi'i  (XT),  Rüsttag,  Freitag.
akk.  IcoMapu,  lia-isaptu  Zauberer,  Zauberin,  l;usSupu  zaubern, Impu  Zauber  :  >  wohl  h
=== leaf 77
schwönu}g)  :  >  späthebr.  'asiäp.  bibl.-aram.  V/iop,  syr.  \lsöpa  Beschwö- rer, akk.  sähiru  Zauberer  :  >  wohl  arab.  sähir  Zauberer,  sihr  Zau- ber, akk.  Pa.  luhhmu  flüstern  (von  Zauberformeln) :  in  Anlehnung  daran wohl  die  techn.  Bed.  beschwören  von  hebr.  liikai,  aram.  hljas,  bhai. akk.  zalärii  nennen,  sprechen,  u.  spez.  schworen  :  >  wohl  syr.  zaJcJcar zaubern,  zakMrä  Totenbeschwörer  (auch  jüd.-ai"am.).  akk.  Icasii binden,  bannen  :  >  viell.  späthebr.  PL  Jcdsritot  ein  Zaubermittel,  bei  Ez.
akk.  hdrü  wörtl.  Seher,  Beschauer,  "Wahrsager,  bjrii  Schau  (des Wahrsagers)  :  >  hebr.  PI.  bärim,  falls  so  Jes.  44,  25;  Jer.  50,  36  statt baddim  zu  lesen;  sowie  viell.  TiobsreYax.  Mbdru  Jes.  47. 13.  Ferner  viell. hebr.  bdrit  (]>  ägypt.  brt)  mit  nell.  urspr.  Bed.  Schau.  akk.  tertu
Vorzeichen,  Omen  :  >>  ^■iell.  hebr.  föm  mit  ^'iell.  urspr.  Bed.  Vorzeichen,
1)  Dagegen  sjr.  sapped  schlagen  (mit  den  Händen)  wohl  ui'verwandt  mit  akk. sapndu.
2)  Dies  würde,  falls  hier  wirklich  ein  alter  .Zusammenhang  vorliegt,  für  akk. iabattu  eine  Entstehung  aus  Sabat-tu  befüi'worten,  aus  dem  dann  ägypt.  smt-t  viell.  früh- zeitig entlehnt  wäre.
9*
      68      
u.  erst  sekundär  mit  horä  unterweisen,  verknüpft.     Aus  hebr.  töra,  hörä
>  aram.  'öräitä  (>>  äth.  ""örit),  desgl.  aus  hebr.  moräh  viell.  erst  ;>  äth. man  Wahrsager.  Vgl.  auch  bereits  oben  S.  48  zu  tertu  Eingeweide,  das im  letzten  Grunde  mit  tertu  Omen,  identisch  sein  wird.  alvk.  nisirtu wörtl.  Verborgenes;  Geheimnis,  Mysterium  :  davon  viell.  beeinflußt  hebr. ngsürtm,  ndsiirot  Jes.  65,  4;  48,  6.
akk.  paMäru  lösen,  erklären,  deuten  (z.  B.  von  Traumen)  :  >  wohl späthebr.  peser,  aram.  pdsar  (^  arab.  fasara).  akk.  xMtäru  lösen  :
>  viell.  hebr.  patar  auslegen,  deuten.
akk.  mahhu  Bez.  f.  einen  Priester  :  >  vieU.  altpers.  magu[S). griech.  fiäyos  Magier;  dagegen  wohl  nicht  hebr.  mag  (s.  oben  S.  6  zu akk.  rdb-mugi).
akk.  qadistu  wörtl.  Reine;  Tempeldirne,  Hierodule  :  >  wohl  hebr. qsdesä.     Vgl.   oben  S.  66  zu  akk.   gudäusu.  akk.  gagü  (<<;  sum.
gagi)  Haus  für  die  Tempeldirnen  :  ^  wohl  syr.  gaggaujä  Hurer.
=== leaf 78

akk.  eJcurru  Tempel  (<<  sum.  e-kur) :  >>  mand.  ehürä  (Götzen)tempel, ägypt.-aram.,  jüd.-aram.  'egOrä  Heiligtum,  Götzenaltar.  Zu  hebr.  usw.
heJcäl  i.  d.  (sekundären)  Bed.  Tempel  s.  oben  S.  8  zu  alvk.  eJcallu  Palast.
aklv.  asirtu,  esirtu  Heiligtum,  Tempel  (St.  wohl  wsr)  :  ]>  wohl  phön. 'srt  Heiligtum,  hebr.  'äserä  kultischer  Pfahl  u.  Bez.  für  eine  Göttin  O akk.  Äsirtu,  Asratu).
akk.  })'^''^o,]clcu  Göttergemach  :  >  syr.  x)dralcM,  mand.  pdriickä Götzenschrein.  Zu  hebr.  müsülc  und  müsOk  s.  oben  S.  32  unter  akk.
mastaku.  akk.  surinnu  Emblem,  Göttersymbol  :  >  viell.  bibl.-
aram.  u.  ägypt.-aram.  'ussarnä  Ausstattung  od.  ä.  eines  Heiligtums.
Zu  hebr.  bämä  s.  oben  S.  43  unter  akk.  hämtu  Höhe.
akk.  himahhu  Grab,  Grabgewölbe  (<<  sum.  ki-mah)  :  >  vieU.  aram. (palm.,  nab.)  gmh,  gwh  Grabnische,  sowie  viell.  armen,  kmax  Leiche,  Skelett.
akk.  Istar  Göttin  Istar  u.  appell.  Göttin  :  >  viell.  frühzeitig,  trotz des  "  und  der  Lautverschiebung,  hebr.  'Astäret,  'AaräQTi^,  phön.  'strt,  nioab. 'str  O  ägypt.  'str,  "Mrt),  aram.  'tr,  südarab.  'ttr;  ferner  späthebr.  ''Äster Esther.  Möglicherweise  auch  früh  aus  akk.  Istar  i.  d.  Bed.  Venusstern  > das  idg.  Wort  für  Stern  (skr.  sfar,  griech.  darij^,  lat.  stella,  Stern). Zu  hebr.  'Asera  s.  oben  unter  akk.  asirtu.  akk.  Beltf  wörtl.  Meine
Herrin,  Belitni  wörtl.  Unsere  Hemn,  Bez.  der  Hauptgöttin  :  ]>•  aram. Beltf,   Beltm,  griech.  Bijlrt?;  im  letzten  Grunde  geht  wohl  aucli   darauf
      69      
zurück  die  Bez.  für  Maria,  ital.  Madonna,  franz.  Notre-Davw,  deutsch Unsre  liebe  Frau.  Zu  mand.  'Amämit  Venus-Istar  s.  oben  S.  61
unter  akk.  aniämü.
Zu  aram.  usw.  Kewän  Saturn  s.  o.  S.  öl  miter  akk.  Kaimänu.
Zu  hebr.  usw.  Tammüz  als  Monatsname  s.  oben  S.  64  f.  Auch  als Göttername  ist  der  bab.  *Tanmsu,  Dii'um,  Düsu  (<]  sum.  Bumii-zi)  im hebr.  Tammus,  aram.  Tämuza  erhalten.  S.  auch  oben  S.  29  unter  akk. imhähu  Flöte  zu  'Äßußag.
akk.  Sin,  der  Mondgott  Sin  :  >>  wohl  südarab.  Mondgott  Sin;  auch im  aram.  (mand.,  liarran.)  ist  der  bab.  Gottesn.  noch  mehrfach  erhalten; vgl.  auch  oben  S.  59  zu  syr.  slnä  Süber.
akk.  EresJcigal  Name  der  ünterweltsgöttin,  als  'Egta^iyal  in  griech. Zauberpapyrus  erhalten.
Zu  akk.  Siris.  eine  Göttin,  s.  oben  S.  40  unter 
=== leaf 79
 :  >  wohl  (aus einer  Kebenf.  karülni)  hebr.  korüb  Cherub.  Fi'aglich,  ob  dazu  auch  ygvtp, griplius,   Greif  gehört.  akk.  seäu  Name  eines  Dämons  :  >  hebr.
sed,  aram.  sedä.  akk.  lamnssu  Name  eines  (guten)  Dämons,  Bez.
für  die  Stierkolosse  :  >> '  viell.  hebr.  sämel  Götzenbild  (aus  Stein) ,  auch phön.  sml  Statue.  alck.  gallü  Name  eines  (bösen)  Dämons  :  >
wahrsch.  griech.  Fillw  Gello.  akk.  asakku  Name  eines  (bösen)  Dä-
mons :  >  viell.  jüd.-aram.  'asM  als  Zauberwort.  akk.  lilü,  lilitu
{<C  sum.  lil)  Name  eines  männl.  u.  weibl.  (bösen)  Dämons  :  >  hebr. liltt  (erst  volksetym.  mit  lajil  Nacht  verknüpft),  Lilitlt.  akk.  labartu
Name  eines  weibl.  (bösen)  Dämons  :  >>  viell.  hebr.  PI.  bbäröt  Thr.  4,10, falls  so  zu  fassen.  alck.  etimmii  (<  sum.  gidim)  Name  eines  (bösen)
Dämons,  spez.  Bez.  für  den  Totengeist  :  >  viell.  hebr.  'ifttm  Jes.  19,3, sowie  vieU.  tarne  Deut.  26,14^.
akk.  usumgallu,  auch  wohl  sungallu'^,  ein  Schlangenname,  auch  in mythischem  Zusammenhange  :  >  wohl  aram.  (Teima-Inschr.)  sngla.
Zu  akk.  Ti'ämat  das  mythische  Meerungeheuer,  s.  oben  S.  44.
18.  Verschiedenes.
akk.  usezib  {Mzubu)  retten  (eig.  übrig  lassen,  Saf.  v.  'gb)  :  >  aram.
1)  Dagegen  jüd.-aram.  ti>majj((.  Totengebeine,  doch  wohl  besser  zu  'äsem,  Htma  usw.
2)  K.  189,  12  (Harper  IX  951).
      70      
sesih,  sauzel  retteu,  befreien.  aldi.  usm  {silsü)  hinausführen  (§af.  v.
ivs)  :  >  aram  wslC)  vollenden,  vernichten.  akk.  usaUil  (suMulu)
vollenden  :  >■  aram.  ialiel.  akk.  hasahu  begehren,   bedürfen  :
>  wohl  aram.  Ipsah.  akk.  dagOlu  blicken  :  >  wahrsch.  syr.
(selten),  neusyr.  cbgal.    Vgl.  oben  S.  12f.  zu  aklc.  diglu.  akk.  samcihu
wachsen,  sprossen  :  ^  wahrsch.  aram.  sdwah.
akk.  asru  Ort,  asar  wo  :  >  wahrsch.  hebr.  Pron.  rel.  "äset: akk.  aSsum  (eig.  =  ana  Sum  im   Namen  von)   wegen,   betreffs  :  davon wohl   beeinflußt  aram.  hd-sum,  'al-Sum  dass.  alck.  ina  lihhi  davon,
darunter  :  davon  wohl  beeinflußt  ägypt.-aram.  hs-gau  darunter.  akk.
immäti  für  und  neben  ina  mctti  wann?  :  darnach  wohl  der  erste  Bestand- teil in  aram.  'immat[j\  'emmat{i)  wann?  akk.  iüimdli  für  und  neben ina  timfili  gestern  :  darnach  wohl  der  erste  Bestandteil  in  hebr.  "etmöl, 'itidmöl  neben  tdmöl,  desgl.  in  ai-am.  'etmnl,  'etinäl{7
```


## [2026-09-14T01:26:09.416Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'\\bSatan\\b', p) and ('adversary' in p or 'Sätän' in p or 'satan' in p):\n        print('LEAF',i)\nEOF"
}
```


### [2026-09-14T01:26:10.949Z] TOOL RESULT

```
leaves 903
LEAF 736
LEAF 759
```


## [2026-09-14T01:26:13.607Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[736]\ni=p.find('Satan')\nprint(p[max(0,i-1500):i+1500])\nEOF"
}
```


### [2026-09-14T01:26:14.829Z] TOOL RESULT

```
the  dissimilation  of  the  first r  to  l.
sash,  n.,  an  ornamental  scarf  or  band.  —  Dis- similated  fr.  Arab,  shash.
sash,  n.,  framework.  —  Alteration  of  F.  chassis, ‘framework’,  incorrectly  pronounced  sashes  and mistaken  for  a  plural.  See  chassis.  For  similar back  formations  cp.  pea  and  words  there  re¬ ferred  to.
sashay,  intr.  v.,  a  term  in  dancing.  —  Corruption of  F.  chassez,  imper.  pi.  of  chasser,  ‘to  chase, hunt’,  fr.  OF.  chacier,  fr.  VL.  *captiare.  See chase,  catch.
sasin,  n.,  the  Indian  antelope.  —  Nepalese, saskatoon,  n.,  a  small  tree,  Ameianchier  alnifolia.
—  Aphetic  for  Cree  misaskwatomin,  which  is compounded  of  misaskwat,  name  of  the  tree, and  min,  ‘berry’.
sassaby,  n.,  a  large  S.  African  antelope.  — Sechuana  tsessebe.
sassafras,  n.,  a  small  laurel-like  tree  of  N.  Ameri¬ ca.  —  Sp.  sasafras,  fr.  saxafrax,  fr.  saxifraga, fr.  L.  saxifraga.  See  saxifrage.
Sassenach,  n.,  a  Saxon;  an  Englishman.  —  Ir.  sa- sanach,  ‘Saxon’.  See  Saxon, sassolite,  n.,  native  boric  acid  (mineral.) — Named after  Sasso  in  Italy.  For  the  ending  see  com¬ bining  form  -Lite.
sassy,  n.,  a  W.  African  tree.  —  W.  African;  said to  derive  from  E.  saucy.
sat,  past  tense  and  pp.  of  sit.  —  ME.  sat,  fr.  OE. sxt,  resp.  ME.  seten,  fr.  OE.  geseten.  See  sit. satable,  adj.,  capable  of  being  sated.  —  Formed fr.  sate  with  suff.  -able.
Satan,  n.  — ■  Heb.  satan,  ‘adversary’,  fr.  satan,  ‘he acted  as  an  adversary  of,  showed  enmity  to ;  he charged,  accused’,  which  is  rel.  to  Aram.  sitan, of  s.m.  Aram.-Syr.  sdtdna,  Arab,  shaytan,  ‘ad¬ versary,  Satan’,  are  loan  words  from  Heb.  satan. Cp.  Gk.  Zdxav,  Zdrava?,  Late  L.  Satan,  Sa- tanas,  which  are  transliterations  of  Heb.  satan. Cp.  also  Shaitan.
Derivatives:  Satan-ism,  n.,  Satan-ist,  n.
Satanic,  adj.  —  Late  Gk.  Zaxavixdg,  fr.  Gk. Zdxav.  See  prec.  word  and  adj.  suff.  -ic. Derivatives:  satanic-al,  adj.,  satanic-al-ly,  adv. Satanology,  n.,  the  study  of  Satan.  —  Coined  fr. Satan  and  Gk.  -Xoyia,  fr.  -X6yos,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals with  a  certain  topic)’.  See  -logy, satara,  n.,  a  woolen  breadcloth.  —  Named  after Satara,  a  town  in  India.
satchel,  n.,  a  small  bag.  —  ME.  sachet,  fr.  OF. sachel,  fr.  L.  saccelius,  dimin.  of  saccus,  ‘sack, bag’.  See  sack,  ‘bag’,  and  -el.
Derivative:  satchel-ed,  adj. sate,  tr.  v.,  to  satisfy,  surfeit.  —  Prob.  a  blend  of obsol.  E.  sade,  fr.  OE.  sadian,  ‘to  satiate’,  and L.  sat,  satis,  ‘enough’.  See  sad  and  cp.  satiate, satis.
sate,  archaic  past  tense  and  past  participle  of  sit.
—  See  sat  and  sit.
sateen,  n.,  a  glossy  cotton  cloth  resembling  satin.
—  Alteration  of  satin,  on  the  analogy  of  velve¬ teen ;  the  ending  -een  is  a  phoneti
```


## [2026-09-14T01:26:29.518Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in [704,705,706,707,736]:\n    nums=re.findall(r'\\b1[0-7]\\d\\d\\b', t[i])\n    print(i, t[i][:80].replace('\\n',' '), '|| nums:', nums[:8])\nprint('=== leaf 549-551')\nfor i in [547,548,549,550,551]:\n    print(i, t[i][:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:26:32.493Z] TOOL RESULT

```
704 imburse-ment,  n. reimport,  tr.  v.,  to  import  again.  —  Formed  fr. re-  a || nums: ['1322', '1323']
705 ’,  fr. rilevare,  'to  raise’,  fr.  L.  relevare.  See  next  word and  cp.  p || nums: ['1324', '1325', '1606', '1326']
706 d  fr.  re- and  model,  v. remonetize,  tr.  v.,  to  restore  as  lawful  curr || nums: []
707 ,  n. repair,  intr.  v.,  to  resort.  —  ME.  repairen,  fr. MF.  repairier,   || nums: ['1329']
736 um,  fr.  sar- pere,  ‘to  cut  off,  lop,  trim’,  fr.  I.-E.  base  *srep-, *s || nums: ['1659', '1734']
=== leaf 549-551
547   ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  because  according to  the  ancient  Russ
548 d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'ord  and  -aceous. myr
549 l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  from  the  stem  of na'
550  B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  
551   of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff
```


## [2026-09-14T01:26:44.951Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [579,580,581,582]:\n    print('=== leaf',i)\n    print(t[i][:600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:26:46.190Z] TOOL RESULT

```
=== leaf 579
ding, portentous,  ominous',  fr.  omen,  gen.  ominis.  See omen  and  -ous. Derivatives:  ominous-ly,  adv.,  ominous-ness,  n. omissible,  adj.  —  Formed  with  suff.  -ible  fr.  L. omissus,  pp.  of  omittere.  See  omit. Derivative:  omissibil-ity,  n. omission,  n.  —  ME.  omissioun,  fr.  Late  L. omissio,  gen.  -onis,  ‘an  omitting’,  fr.  L.  omissus, pp.  of  omittere.  See  omit  and  -ion. omissive,  adj.  —  Formed  with  sulf.  -ive  fr.  L. omissus,  pp.  of  omittere.  See  omit  and  -ive. omit,  tr.  v.  —  ME.  omitten,  fr.  L.  omittere,  ‘to  let go,  give  up,  dism
=== leaf 580
pretation  of  dreams. oneiromancy ooze oneiromancy,  adj.,  divination  through  dreams. Compounded  of  oneiro-  and  Gk.  uavTcta, 'oracle,  divination’.  See  -mancy. oneiromantic,  adj.,  pertaining  to  oneiromancy. See  oneiro-  and  -mantic. oner,  n.,  a  unique  person  or  thing  (slang).  — Formed  fr.  one  with  agential  suff.  -er. onerous,  adj.,  burdensome,  troublesome,  oppres¬ sive.  —  ME.,  fr.  MF.  onereus  (F.  ont- reux ),  ‘onerous,  burdensome’,  fr.  L.  onerdsus,  of s.m.,  fr.  onus,  gen.  oneris ,  ‘burden,  weight’.  See onus. Derivatives:  onerous-ly,  adv.
=== leaf 581
aining  eggs  (zool.)  — ModL.  ootheca,  compounded  of  oo-  and  Gk. 8-fjx7),  ‘case’.  See  theca. ooze,  n.,  1)  an  oozing;  2)  something  that  oozes; 3)  liquor  used  in  tanning  leather.  —  ME.  wose, wos,  fr.  OE.  wos,  ‘sap,  juice’,  rel.  to,  and  in- ooze opiate fluenced  by,  OE.  wdse,  ‘soft  mud,  mire' ;  rel,  also to  OS.  waso,  ‘wet  ground,  mire',  ON.  veisa,  ‘pond of  stagnant  water’,  and  prob.  cogn.  with  OI. vifdm,  ‘poison’,  Gk.  to 5  (for  *Fta6;),  L.  virus (for  *visos),  ‘poison’.  See  virus. Derivative:  ooze ,  intr.  v.,  to  flow  slowly,
=== leaf 582
;  anything  soothing;  tr. opinable 1088 1089 v.,  to  treat  with  an  opiate;  to  narcotize.  —  ML. opiatus,  fr.  L.  opium.  See  opium  and  adj.  suff. -ate. opinable,  adj.,  1)  that  which  is  a  matter  of  opin¬ ion;  2)  capable  of  being  opined.  — •  L.  opinabilis, ‘that  which  rests  on  opinion ;  conjectured',  fr. opinari.  See  next  word  and  -able, opine,  tr.  and  intr.  v.,  to  hold  an  opinion;  to think,  suppose  (now  humorous).  —  MF.  (=  F.) opiner,  fr.  L.  opinari,  ‘to  think,  suppose’,  fr. *opio,  gen.  -onis,  ‘expectation’,  which  is  rel.
```


## [2026-09-14T01:26:59.393Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(565,590):\n    nums=[n for n in re.findall(r'\\b\\d{3,4}\\b', t[i]) if 1000<=int(n)<=1120]\n    print(i, nums, t[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:27:00.548Z] TOOL RESULT

```
565 ['1056', '1057'] orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n. Norn, 
566 ['1058', '1059']   Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (als
567 ['1080', '1060', '1061']  alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  
568 ['1062', '1063']  numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number, 
569 ['1064'] ), contraction  of  *noven-dinom,  ‘nine  days’,  fr. novem,
570 ['1066']   sexual  desire  in  women (med.)  —  Medical  L.,  compoun
571 ['1067', '1068'] o  put  before’.  It derives  fr.  L.  objectus,  pp.  of  o
572 ['1070', '1071'] elligible’,  orig.  ‘cover¬ ed’,  formed  fr.  ob-  and  l.-
573 ['1072'] ontradiction  in  itself.The  name  should be  foramen  obtu
574 [] eaning  lit. ‘something  sharp-edged’,  and  rel.  to  ocris
575 [] OHG.  ort,  ‘point  (esp.  of  a  weapon  or  a tool),  angl
576 [] e  ecology, oecumenic,  oecumenical,  adjs.  —  See  ecumeni
577 []   The  sense  development  is due  to  a  confusion  of  the
578 ['1081']  the  ending  see  suff. -aceous. Olethreutidae,  n.  pi.,  
579 ['1031', '1082', '1083'] ding, portentous,  ominous',  fr.  omen,  gen.  ominis.  See
580 ['1084', '1085'] pretation  of  dreams. oneiromancy ooze oneiromancy,  adj., 
581 ['1086'] aining  eggs  (zool.)  — ModL.  ootheca,  compounded  of  oo
582 ['1088', '1089'] ;  anything  soothing;  tr. opinable 1088 1089 v.,  to  trea
583 [] ts.  —  F.  opticien,  fr.  ML.  optica.  See next  word  an
584 ['1093'] ng  to  an  orator’,  fr.  orator.  See  orator, oratory,  n
585 ['1094', '1095']  coin,  prop,  subst.  use  of  the  adj. aureus,  ‘of  gold
586 ['1096'] s  American  birds  of  the  family Icteridae.  —  F.  oriol
587 [] �orris  root’,  which  is  identical  with  Gk. Epecoe,  gen
588 []   vowel  osche-,  combining  form meaning  the  ‘scrotum’.  
589 ['1103'] a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff
```


## [2026-09-14T01:27:19.323Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(730,742):\n    nums=[n for n in re.findall(r'\\b\\d{4}\\b', t[i]) if 1300<=int(n)<=1450]\n    print(i, nums, t[i][:60].replace('\\n',' '))\nprint('---- around 573')\nfor i in [573,574,575,576]:\n    print(i, t[i][:1200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:27:20.483Z] TOOL RESULT

```
730 [] :  Sahar-an,  Sahar-ian,  Sahar-ic,  adjs. sahib,  n.,  a  t
731 ['1376', '1377'] See  salt  and  -ine  (representing L.  -inus)  and  cp.  L.
732 ['1378']   fr.  OF.  saluta- cion  (F.  salutation),  fr.  L.  saluta
733 ['1380'] s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and 
734 ['1382'] derives  fr.  VL. sanguem.  See  prec.  word.  F.  de,  ‘of,
735 []  ‘soap’,  which  is a  Teut.  loan  word.  See  soap. Deriva
736 [] um,  fr.  sar- pere,  ‘to  cut  off,  lop,  trim’,  fr.  I.-
737 ['1388']   —  ME.  Saterdai,  fr.  OE.  Satsern(es)- dteg,  Sseterd&g
738 ['1390'] .  secgan,  ‘to  say’.  See  say  and  cp.  saga, which  is 
739 ['1391', '1392'] e  head).  See  Kluge- Mitzka, EWDS.,  p.  633  s.v.  Schale
740 [] ades,  shoulders’,  which  is of  uncertain  origin.  It  po
741 ['1394', '1393']  the  Tower  under  Henry  VIII. scazon,  n.,  1)  a  cholia
---- around 573
573 ontradiction  in  itself.The  name  should be  foramen  obturatum,  ‘the  obstructed  hole’.  See Joseph  Hyrtl,  Onomatologia  anatomica,  p.  223. For  etymology  see  obturator  and  foramen, obtuse,  adj.,  1)  not  pointed,  blunt;  2)  dull  —  L. obtusus,  ‘blunted’,  pp.  of  obtundere,  ‘to  beat against,  to  blunt’,  fr.  ob-  and  tundere,  ‘to  beat, strike,  stump’,  which  is  rel.  to  tudes,  gen.  -ditis, ‘hammer’,  and  cogn.  with  OI.  tudati,  tundate, ‘he  thrusts',  fr.  I.-E.  base  *(s)tud-,  ‘to  beat,  strike push,  thrust’.  See  stint  and  cp.  words  there  re¬ ferred  to. Derivatives:  obtuse-ly,  adv.,  obtuse-ness,  n. obverse,  adj.,  turned  toward  the  observer.  —  L. obversus,  pp.  of  obvertere,  ‘to  turn  toward’,  fr. ob-  and  vertere,  ‘to  turn'.  See  version  and  cp. obvert. Derivatives:  obverse,  n.,  obverse-iy,  adv. obvcrsion,  n.,  the  act  of  obverting.  —  Late  L.  ob- versid,  gen.  -onis,  ‘a  turning  toward’,  fr.  L.  ob¬ versus,  pp.  of  obvertere.  See  prec.  word  and  -ion. obvert,  tr.  v.  —  L.  obvertere.  See  obverse, obviate,  tr.  v.,  to  prevent;  to  make  unnecessary. —  L.  obvidtus,  pp.  of  ob
574 eaning  lit. ‘something  sharp-edged’,  and  rel.  to  ocris,  ‘a rugged,  stony  mountain’,  acer,  ‘sharp’.  See  acrid and  words  there  referred  to  and  cp.  esp.  the second  element  in  mediocre. ocreate,  adj.,  having  an  ocrea.  —  Formed  fr. prec.  word  with  adj.  suff.  -ate. octa-,  before  a  vowel  oct-,  combining  form  mean¬ ing  ‘eight’.  —  Gk.  oxtoc -,  oxt-,  fr.  oxtco, ‘eight’,  which  is  cogn.  with  L.  odd,  OI.  ayta, astau,  Goth,  ahtau,  OE.  eahta,  ‘eight’ ;  see  eight. The  a  in  oxra-  is  due  to  the  analogy  of  enra, ‘seven’,  evv£a,  ‘nine’,  Sexx,  ‘ten’.  Cp.  penta- and  hexa-. octachord,  n.,  1)  a  musical  instrument  with  eight strings;  2)  an  octave.  —  Gk.  oxTdcyopSoc;, ‘having  eight  strings’,  compounded  of  oxtoc  - (see  octa-)  and  yopSir),  ‘string’.  See  chord. Derivative:  octachord-al,  adj. octad,  n.,  1)  a  series  of  eight  numbers  (math.); 2)  an  atom  or  radical  with  the  valency  of  eight (chem.)  —  Gk.  oxtcx?,  gen.  AxtcxSoc,  ‘the number  eight’,  fr.  oxtco.  See  octa-  and  -ad  and cp.  ogdoad. octagon,  n.,  a  plain  figure  with  eight  angles  and eight  sides  (geom.) — L.  
575 OHG.  ort,  ‘point  (esp.  of  a  weapon  or  a tool),  angle,  edge,  beginning’,  MHG.  ort,  "point’ (esp.  of  a  weapon  or  a  tool’),  G.  Ort,  ‘place’,  fr. Teut.  base  *uzda •;  cogn.  with  Alb.  ust,  ‘ear  of grain’,  Lith.  us-rtis,  ‘thistle’. Derivatives:  odd-ly,  adv.,  oddity  (q.v.),  uddment (q.v.),  odd-ness,  n.,  odds  (q.v.) oddity,  n.  —  A  hybrid  coined  fr.  odd  and  -ity,  a suff.  derived  fr.  L.  -Has. oddment,  n.,  an  odd  piece,  a  remnant.  —  A  hy¬ brid  coined  fr.  odd  and  -ment,  a  suff.  derived  fr. L.  -mentum. odds,  n.  pi.,  difference  in  favor  of  one  as  against another,  balance  of  advantage;  advantage.  — From  the  adjective  odd. ode,  n.,  1)  orig.  a  poem  intended  to  be  sung;  2)  in modern  use,  a  lyric  poem  of  exalted  style.  — MF.  (=  F.),  fr.  Late  L.  ode,  oda,  fr.  Gk.  toS-rj, contraction  of  aoi.8 tj,  ‘song’,  rel.  to  aetSo),  ‘I sing’,  which  prob.  stands  for  *d(u)-sl-8to  and is  rel.  to  dbr)8<l)v  [for  *a  (u  j-vj-Srov],  ‘nightingale’, otiS 7]  (for  x-oSrj  ) ,  ‘voice,  tone,  sound’,  ctuSia (for  d-uSaoi ),  ‘I  talk,  speak’,  and  cogn.  with  Of. vadati,  ‘speaks,
576 e  ecology, oecumenic,  oecumenical,  adjs.  —  See  ecumenic, ecumenical. oecus,  n.,  a  room  or  hall  in  a  house.  —  L.,  fr.  Gk. olxo c,  ‘house’.  See  economy, oedema,  n.  —  See  edema. Oedipus,  n.,  the  son  of  Laius  and  Jocasta,  king and  queen  of  Thebes,  who  unknowingly  slew his  father  and  married  his  mother;  he  solved  the riddle  of  the  Sphinx  ( Greek  mythol.)  —  L.,  fr. Gk.  OlSi7tou;,  lit.  ‘swell-foot’,  fr.  olSav,  ‘to swell’,  and  iro’ic  (gen.  tco86? ),  ‘foot’.  See  edema and  -pod. oeil-de-boeuf,  n.,  a  round  or  oval  window  ( archit .) —  F.  ail-de-bceuf  lit.  ‘eye  of  an  ox’,  fr.  aril  (fr. L.  oculus),  ‘eye’,  de,  ‘from,  of’  (fr.  L.  de,  ‘from, away  from’),  and  bauf  (fr.  L.  bovem,  acc.  of bos),  ‘ox’.  See  ocular,  de-  and  beef, oeillade,  n.,  an  amorous  glance.  —  F.  eeillade,  fr. ail,  ‘eye’,  fr.  L.  oculus.  See  ocular  and  -ade. oen-,  form  of  oeno-  before  a  vowel. Oenanthe,  n.,  a  genus  of  plants,  the  water  drop- wort  (bot.)  —  L.  oenanthe ,  ‘vine  shoot,  the  vine; dropwort’,  fr.  Gk.  oEvdtvffrj,  of  s.m.,  which  is compounded  of  etvi],  ‘vine’,  and  avffo;
```


## [2026-09-14T01:27:29.833Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'\\*sed-', p):\n        # find nearby page number\n        m=[n for n in re.findall(r'\\b\\d{3,4}\\b', p) if 100<=int(n)<=1780]\n        print(i, m[:4], re.findall(r'.{80}\\*sed-.{120}', p.replace('\\n',' '))[:1])\nEOF"
}
```


### [2026-09-14T01:27:31.091Z] TOOL RESULT

```
145 [] [' prob.  for  *ce- zdere,  from  the  demonstr.  particle  ce-  and T.-E.  base  *sed-,  ‘to  go’,  whence  also  Gk.  6869, ‘way’,  OSlav.  chodu,  ‘a  walking,  going’,  choditi, ‘to  walk,  go’,  OI.  d-']
150 ['264', '265', '157', '715'] ["to  e^eaftxi, ‘to  sit’,  fr.  Gk.  base  *s8-,  corresponding  to I.-E.  base  *sed-,  ‘to  sit',  whence  L.  sedere, ‘to  sit’.  See  sedentary  and  cp.  cathedra,  cathe¬ dral.  Cp.  also  chaise,  wh"]
272 ['1241', '107'] ['is  rel.  to  sSog,  ‘seat,  base,  foun¬ dation’,  fr.  stem  *kS-  (=  I.-E.  *sed-),  ‘to  sit’, and  cogn.  with  L.  sedere,  ‘to  sit’.  See  sedentary and  cp.  next  word. edaphology,  n..  the  st']
479 ['890', '891', '1554', '1581'] [' of  L.  timus, ‘slime,  mud,  mire’,  and  sella,  ‘seat’,  which stands  for  *sed-la,  from  the  stem  of  sedere,  ‘to sit’.  For  the  first  element  see  limno-,  for  the second  see  sedentary  a']
557 [] ['ce to  sit  down  in’,  fr.  *ni-,  ‘down’,  and  zero  degree of  I.-E.  base  *sed-,  ‘to  sit"  [cp.  OI.  ni-satsuh, ‘sitting’,  ni-sidati,  ‘sits  down,  settles’,  and  Gk. 6^05  (metathesis  for  *o']
575 ['686', '886', '686'] ['?,  fr.  ypd^Eiv,  ‘to  write’.  The first  element  derives  fr.  I.-E.  base  *sed-,  ‘to  go’, whence  also  OSlav.  chodu,  ‘a  walking,  going’, choditi,  ‘to  walk,  go’.OI.  a-sad-,  ‘to  go, approa']
632 ['1635', '1705', '556'] ["upon,  to  press’,  fr. *pi-,  short  form  of  *epi,  ‘on’  (see  epi-),  and  *sed-, ‘to  sit’,  whence  OI.  sidati,  ‘sits',  Gk.  Eqcadai, L.  sedere,  ‘to  sit’.  See  sedentary, piezometer,  n.,  an"]
729 ['368', '1740', '1373'] [' words  orig.  meant  ‘a  place  to  sit  upon’, and  derive  fr.  I.-E.  base  *sed-,  ‘to  sit’,  whence also  L.  sedere.  Cp.  L.  sella  (for  *sed-Ia),  ‘seat, chair’,  OSlav.  sedlo,  ‘saddle’,  and']
748 ['1583', '1408', '1409'] ["G.  Gesd.fi,  ‘but¬ tocks',  fr.  Teut.  base  *set-,  corresponding  to I.-E.  *sed-,  ‘to  sit’.  See  sit. Derivatives:  seat,  tr.  v.,  seat-ed,  adj.,  seat-er ,  n., seat-ing,  n.,  seat-less,  adj."]
749 ['1410'] [" sedens,  gen.  -ends,  pres.  part,  of  sedere,  ‘to  sit’, fr.  I.-E.  base  *sed-,  ‘to  sit’,  whence  also  OI.  d- sadat,  ‘sat  down’,  sidati,  ‘sits’,  Avestic  had-,  'to sit  down’,  Gk.  (for "]
751 ['1772', '1671', '1713', '1640'] [' —  ME.  selle,  fr.  MF.  (=  F.)  selle,  fr. L.  sella,  which  stands  for  *sed-la,  fr.  sedere,  ‘to sit’.  See  settle,  n.,  and  cp.  saddle, sellenders,  n.  —  A  var.  of  sallenders. Seltzer ']
757 ['1426', '1427', '528', '642'] ['of  s.m.,  OE. sadol,  ‘saddle’.  I.-E.  *sedla-  is  an  enlargement of  base  *sed-,  ‘to  sit’.  See  sit,  sedentary  and  cp. saddle  and  sell,  ‘seat’. settle,  tr.  and  intr.  v.  —  ME.  set  ten']
770 [] ['sitzen,  Goth,  sitan,  fr. Teut.  base  *set-,  corresponding  to  I.-E.  base *sed-,  ‘to  sit’,  whence  OI.  sidati,  ‘he  sits’,  Gk. E^Eaffai  (for  *sedyesthai),  ‘to  sit’,  s8px  (for *sedra),  ‘s']
782 [] [' settles’,  fr.  Teut. base  *set-,  ‘to  sit,  set’,  corresponding  to  I.-E- *sed-,  ‘to  sit’,  whence  OSlav.  sazda,  Lith.  sudd- ziai  (pi.),  OIr.  suide,  W.  huddyl,  Bret,  huzel, ‘soot’.  See ']
814 ['1534'] ['ium,  n.,  a  low  bench.  —  L.,  ‘bench,  seat’, fr.  sub-  and  sella  (for  *sed-ld-),  from  the  base  of sedere,  ’to  sit’.  See  sedentary  and  cp.  seat,  settle. Cp.  also  the  second  element']
```


## [2026-09-14T01:27:43.418Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[575].replace('\\n',' ')\ni=p.find(\"*sed-\")\nprint(p[max(0,i-2000):i+800])\nEOF"
}
```


### [2026-09-14T01:27:44.574Z] TOOL RESULT

```
e. Odeum,  n.,  1)  a  hall  for  musical  performances  in ancient  Greece  and  Rome ;  2)  in  modern  use,  a concert  hall.  —  L.  odeum,  fr.  Gk.  4>8eiov,  ‘a  pub¬ lic  building  at  Athens  designed  for  musical performances’,  fr.  c!>8t],  ‘song.  See  ode. odic,  adj.,  pertaining  to  an  ode.  —  See  ode  and adj.  suff.  -ic  and  cp.  Gk.  q>8i>c6?,  ‘fond  of  sing¬ ing,  musical’. odic,  adj.,  pertaining  to  an  od.  —  Formed  fr.  od with  adj.  suff.  -ic. Odin,  n.,  the  chief  deity  of  Norse  mythology.  — Dan.,  fr.  ON.  Odinn,  rel.  to  OS.  Wodan,  OE. Woden,  OHG.  Wuotan.  See  Woden  and  cp. words  there  referred  to. odious,  adj.,  hateful;  disgusting.  —  ME.,  fr.  MF. odieus  (F.  odieux),  fr.  L.  odiosus,  ‘hateful,  offen¬ sive,  unpleasant’,  fr.  odium.  See  odium. Derivatives:  odious-ly,  adv.,  odious-ness,  n. odium,  n.,  hatred,  opprobrium,  disgust.  —  L. odium,  ‘hatred,  offense,  annoyance,  disgust’,  rel. to  odi,  odisse,  ‘to  hate’,  cogn.  with  Arm.  ateam, ‘I  hate’,  ateli,  ‘hateful,  odious’,  ON.  atall,  OE. atol,  ‘dire,  horrid,  loathsome’,  perh.  also  with Gk.  686aax<7&x'.,  ‘to  be  grieved  at,  be  angry  at’; fr.  I.-E.  base  *od-,  ‘to  hate’,  which  is  perh.  orig. identical  with  *od-,  ‘to  smell’.  See  odor  and  cp. Odysseus.  Cp.  also  noisome,  annoy. Odobenus,  n.,  the  genus  consisting  of  the  walrus¬ es  ( zool .)  —  ModL.,  compounded  of  Gk.  68cov, ‘tooth’,  and  fiouveiv,  ‘to  walk’  (see  odonto-  and base,  n.);  so  called  in  allusion  to  the  use  of  the tusks  in  walking. Odocoileus,  n.,  a  genus  including  various  species of  deer  (zool.)  —  ModL.,  compounded  of  Gk. 68t»v,  ‘tooth’,  and  xoIXo?,  ‘hollow’.  Seeodonto- and  coelo-. odograph,  n.,  an  instrument  recording  the  dis¬ tance  traveled.  —  Compounded  of  Gk.  886?, ‘way’,  and  -yp X90?,  fr.  ypd^Eiv,  ‘to  write’.  The first  element  derives  fr.  I.-E.  base  *sed-,  ‘to  go’, whence  also  OSlav.  chodu,  ‘a  walking,  going’, choditi,  ‘to  walk,  go’.OI.  a-sad-,  ‘to  go, approach’, ut-sad,  ‘to  step  aside,  disappear’,  L.  cedere (for  *ce-zdere),  ‘to  go,  go  away,  yield’.  Cp.  -ode, ‘way’,  and  anode,  cathode,  Diodia,  electrode, episode,  exodus,  hexode,  method,  parodos,  period, stomodeum,  synod.  I.-E.  base  *sed-,  ‘to  go’,  is identical  with  *sed-,  ‘to  sit’,  the  original  sense of  the  base  having  been  ‘to  place  (either  the seat  in  order  to  sit  down,  or  the  foot  on  the ground  in  order  to  go)’.  See  sedentary  and  cp. cede.  For  the  second  element  see  -graph.  The spelling  odograph  is  prob.  due  to  the  influence of  next  word  (q.v.) odometer,  n.,  an  instrument  attached  to
```


## [2026-09-14T01:28:02.525Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -A24 \"^sed-\\|^ *sed-\\b\" AHD_watkins1985.txt | head -60\necho \"=========SEGH\"\ngrep -n -A20 \"segh-\" AHD_watkins1985.txt | head -50"
}
```


### [2026-09-14T01:28:02.598Z] TOOL RESULT

```
<persisted-output>
Output too large (38.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bdptgh54y.txt

Preview (first 2KB):
910:sed-', To sit. 1. Suffixed form *sed-yo- in Germanic *sitjan in: a. Old English sittan, to sit: sit; b. Old High German sizzen, to sit (> German Sitz, act of sitting): sITz BATH, SITZKRIEG, SITZMARK. 2. Suffixed (causative) o-grade form *sod-eyo- in Germanic *satjan, to cause to sit, set, in: a. Old English settan, to place: sET’; b. Old High German sezzan, to set, in irsezzan, to replace: ERSATZ. 3. Suffixed form *sed-lo-, seat, in Germanic *setlaz in Old English setl, seat: SETTLE. 4. O-grade form *sod- in Germanic *sadulaz, seat, saddle, in Old English sadol, saddle: SADDLE. 5. Suffixed lengthened o-grade form *séd-o- in Germanic *sétam in Old English sét, soot (< “that which settles”): soot. 6. Suffixed lengthened-
911-sek-
912-grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, 
...
</persisted-output>
```


## [2026-09-14T01:28:05.355Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '905,935p' AHD_watkins1985.txt"
}
```


### [2026-09-14T01:28:05.403Z] TOOL RESULT

```
sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
s6-1, To sow. Contracted from *sea-. 1. Germanic *séan in Old English séwan, to sow: sow!. 2. Suffixed form *sé-ti-, sowing, in Germanic “sédiz, seed, in: a. Old English s&d, seed: sEED; b. Middle Dutch saet and Middle Low German sdt, seed: couza. 3. Reduplicated zero-grade form “si-s()- in Latin serere, to sow: SEASON; INSERT. 4. Suffixed form *sé-men-, seed, in Latin sémen, seed: SEME, SEMEN, SEMINARY, SEMINATION; DISSEMI- NATE. [In Pok. 2. sé(i)- 889.]
s@-2, Long, late. Contracted from *sea-. Variant *seoi-, zero-grade form *sia-, contracted to *si-. 1. Suffixed form sé-ro- in: a. Latin sérus, late: SEROTINOUS, SOIREE; b. Middle Breton Air, long: MENHIR. 2. Possibly Ger- manic *si- in: a. Germanic *sid6, “long surface or part,” in Old English side, side: stDE; b. Germanic ‘sith, “later,” after, in Old English siththon, siththan, after that, since: SINCE, SITH. [In Pok. 2. sé(i)- 891.]
s@-3, To sift. Contracted from *sea-. Suffixed form *sé-dho- in Greek éthein, to sift: ETHMOID. [Pok. 1. sé(i)- 889.]
sé-4, To bind, tie. Contracted from *sea-. Variant *sesi-, zero-grade form *si-. Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW. [Pok. 3. sé(i)- 891.]
sed-', To sit. 1. Suffixed form *sed-yo- in Germanic *sitjan in: a. Old English sittan, to sit: sit; b. Old High German sizzen, to sit (> German Sitz, act of sitting): sITz BATH, SITZKRIEG, SITZMARK. 2. Suffixed (causative) o-grade form *sod-eyo- in Germanic *satjan, to cause to sit, set, in: a. Old English settan, to place: sET’; b. Old High German sezzan, to set, in irsezzan, to replace: ERSATZ. 3. Suffixed form *sed-lo-, seat, in Germanic *setlaz in Old English setl, seat: SETTLE. 4. O-grade form *sod- in Germanic *sadulaz, seat, saddle, in Old English sadol, saddle: SADDLE. 5. Suffixed lengthened o-grade form *séd-o- in Germanic *sétam in Old English sét, soot (< “that which settles”): soot. 6. Suffixed lengthened-
sek-
grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
sék-
sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
seng’-
tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
seng"h-
*sakk- in Swedish sacka, to sink, akin to the Scandina- vian source of Middle English saggen, to subside: sac. [Pok. sengz- 906.]
seng“h-. To sing, make an incantation. 1. Germanic *singan in: a. Old English singan, to sing: SING; b. Old High German singan (> German singen), to sing: MEIs- TERSINGER, MINNESINGER, SINGSPIEL. 2. Suffixed o-grade form *songvh-o-, singing, song, in Germanic *sangwaz in Old English sang, song, song: SONG. [Pok. sength- 906.]
senk-. To burn. Suffixed (causative) o-grade form *sonk- eyo- in Germanic *sangjan, to cause to burn, in Old English sengan, to singe: SINGE. [Pok. senk- 907.] sent-. To head for, go. 1. Germanic suffixed form *sinth- nan in Old High German sinnan, to go: WITHERSHINS. 2. Suffixed (causative) o-grade form *sont-eyo- in Ger- manic *sandjan, to cause to go, in Old English sendan, to send: SEND!. 3. Suffixed o-grade form *sont-o- in Ger- manic *sandaz, that which is sent, in Old English sand, message, Messenger: GODSEND. 4. Perhaps suffixed form *sent-yo- in Latin sentire, to feel (< “to go mentally”): SCENT, SENSE, (SENSILLUM), SENTENCE, SENTIENT, SEN- TIMENT, SENTINEL; ASSENT, CONSENT, DISSENT, PRESEN- TIMENT, RESENT. [Pok. sent- 908.]
sep-'. To taste, perceive. Suffixed zero-grade form *sap-yo- in Latin sapere, to taste, have taste, be wise: SAGE}, SAPID, SAPIENT, SAPOR, SAVANT, SAVOR, SAVVY. [Pok. sap- 880.]
sep-2, To foster, serve, venerate (the dead). Suffixed form *sep-el-yo- in Latin sepelire, to bury: SEPULCHER, SEPUL- TURE. [Pok. sep- 909.]
septm. Seven. 1. Germanic *sebum in Old English seofon, seven: SEVEN. 2. Latin septem, seven: SEPTEMBER, SEP- TENNIAL, SEPTET, SEPTI-, SEPTUAGINT, SEPTUPLE; SEP- TENTRION. 3. Greek hepta, seven: HEBDOMAD, HEPTA-, HEPTAD. [Pok. septm 909.]
ser-1, To protect. 1. Extended form *serw- in Latin serudre, to keep, preserve: CONSERVE, OBSERVE, PRE- SERVE, RESERVE, (RESERVOIR). 2. Suffixed length- ened-grade form *sér-6s- perhaps in Greek hérés, “protector,” hero: HERO. [Pok. 2. ser- 910.]
ser-?, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA. 3. Extended roots *sr-edh-, *sr-et-, to whirl, bubble, in Germanic *stred- in Old High German stredan, to whirl, swirl, whence ablaut formation in Middle High German séru- del, whirlpool: STRUDEL. [Pok. 1. ser- 909; sr-edh- 1001.]
ser-3, To line up. 1. Latin serere, to arrange, attach, join (in speech), discuss: SERIES, SERTULARIAN; ASSERT, DESERT’, DISSERTATE, EXERT, INSERT. 2. Suffixed form *ser-mon- in Latin sermé (stem sermé6n-), speech, dis- course: SERMON. 3. Suffixed form *ser-d- perhaps in Latin sera, a lock, bolt, bar (? < “that which aligns”): SEAR?, (SERRIED). 4. Suffixed zero-grade form *sr-t- in Latin sors (stem sort-), lot, fortune (probably from the lining up of lots before drawing): SORCERER, SORT; ASSORT, CONSORT, SORTILEGE. [Pok. 4. ser- 911.]
serk-. To make whole. Latin sarcire, to mend, repair: SARTORIUS. [Pok. serk- 912.]
serp-'. Sickle, hook. 1. Latin sarpere, to cut off, prune (> sarmentum, twigs): SARMENTOSE. 2. Greek harpé, sickle (> Old French harper, to seize): HARPOON. [Pok. 5. ser- 911.]
serp-2. To crawl, creep. 1. Latin serpere, to crawl: SER- PENT, SERPIGO. 2. Greek herpein, to crawl, creep: HER- PES, HERPETOLOGY. [Pok. serp- 912.]
[servus. Slave. Latin noun of unknown origin. SERF, SERGEANT, SERVE, SERVICE, SERVILE, SERVITUDE, SIR- VENTE; CONCIERGE, DESERVE.]
seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
seue-2, To take liquid. I. Suffixed zero-grade form
skei-
*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
skel-'
```


## [2026-09-14T01:28:22.943Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"شیدا\" BQT_v3_pages.txt | head -20; echo \"=== pdf page tags near\"; grep -n \"\\[pdf page 11[0-9]\\]\" BQT_v3_pages.txt | head"
}
```


### [2026-09-14T01:28:23.019Z] TOOL RESULT

```
2908:کردیدن. ‎Cis gan‏ شدن و شیدایی بودن
8536:‏شیدا ۴ « بفتح اول بروزن پیداء بمعنی _
8546:‏شیدان - بکر اول بر وزن شیلان .
8568:شیاطین ) « باروچا ۲4۳*. © - بر ماختهُ فرقة آذرکیوان : « شیداب پزشکی بودروشنای
8570:ص ‎٩۷‏ » و مولف دیستان در(درازدهمین نظر در مذهب شیداییان ) از عقاید این فرقه بحث کند.
8588:و فتح دال » بمم‌نی شیداست که هرچیزروشن ۴
26909:‏وشیدایی و دبوانه مزاج وپریشان حال باشد؟ .
26912:کالفته است که آشفته وشیدایی باشد .
27075:‎BEV‏ بلبل سح ‎QUIT‏ و باد مشکبوی مردم سرمست را کالیوه و شیدا کند .
40067:شیدا » بلفت زند وپازند نقره را کگوند و بعریی
=== pdf page tags near
8399:[pdf page 110]
8497:[pdf page 111]
8575:[pdf page 112]
8686:[pdf page 113]
8745:[pdf page 114]
8762:[pdf page 115]
8767:[pdf page 116]
8865:[pdf page 117]
8967:[pdf page 118]
9053:[pdf page 119]
```


## [2026-09-14T01:28:26.032Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '8497,8600p' BQT_v3_pages.txt"
}
```


### [2026-09-14T01:28:26.137Z] TOOL RESULT

```
[pdf page 111]
Sx

کرت ‎SHYT‏ رومی یز ‎lye‏ و بفتح
اول هم کنتماند ؛ وبابای ابجد ایزدرست است .

‎Goan‏ = با تعتالی در آخر و حرکت
میهول ۰ بمعنی شکیوی است که آوازبای باشد
که درب آهسته ‎Sigal,‏ -وصداییکه‌درخواب
آهته از مردم ‎Hwee‏
‏شیتره ۲ فتح اول و فودالی بروژن
میسره » دوابی است که آنرا ‎Bye‏ سرخیوی
ولیذیون خوانند ومعرب آن شیطرج است. گویند
اکر ‎MYT‏ سر یاون ده درا ‎BL‏
‏سلزد ؛ وبجای های هوز (۱)کاف هم بنظی آمده
است و جربی مسواك الراعی خوانند.

‏یج = بکر اول وسکون ثانی ‎ley‏
‏قله . درمنه را کویند و بهترین آن‌تر کی‌است
مشهوو ‎Lape‏ تر کی .

‏شیخ ‎GIS‏ - بکرخای‌تطه‌دار(»)
وقتح بون. شطان لمين را کوشد.

‏شید ۴ © پکر اولوسکون ثالیمجهول
و دال » بممئی لور باشد مطلفاً که آن روشتابی

‏(۱) چك : وبجای‌ها .
۱ رك : شلپری وشکیوی .

‎Ve

‏معنوی است - وعرچیز بیار روشن‌رالیز گویند
و عربی ‎lad‏ خوانند - ‎Soy‏ از نامهای
‎aT‏ است - ‎Leg,‏ آفتاب راهم میگویند -
و لام یس افرامياب لیز بوده که او را پشنگه
خواندد - و پفتح‌اول زرق و سالوسی وساختگی
باشد .

‏شیدا ۴ « بفتح اول بروزن پیداء بمعنی _
‎alps‏ ولاسقل باشد .

‏شید اب ‎AK, » ٩‏ اول‌بروزن تیز آب»
تام حکیمی بوده و اوخاك را اله میداندچتانکه
دیگران ‎wl‏ را

‏شید اسپهید ۱ - ‎gow‏ روان بخش
است که ‎og yar‏ روح الفدی خوانند.

‏شیدان - بکر اول بر وزن شیلان .
خوان طء‌ام ‎candy‏ را گوبند .

‏شید ] هرمن ۲ - بکر اول ترجه
نورالشیطان است چه‌شید بمعنی لورباشد و آهرمن
شیطان را کوبند -و ‎OVS MOLT‏ زشت وتخیلات
‎dhl‏ بود .

‏(0) چك : بکر ‎ole‏

‎. ‏شاء تره‎ df

‏۴ - اوستا - 5518648 (درخشان).پهلوی ]526 ‎gael?‏ ۸۰۱ درارمتی 891064(سرخ
‎Coord‏ [در اسب ] ‎shé oo Spe) 5080-۷2۳5 sles‏ (روبام), ‎shi‏ (کرند [اسب])
? هوبدمان ۸۰۱ «من‌کامه آعت که در «خورشید» و «جمشید» آمده .

‏۴ - از آرامی واردشده ‎lilt‏ ۱ : ۲ ص ‎٩٩‏ درزبان اکدی ‎ShEdU‏ (نام عفریتی) » در

‏عبری ‎shed‏ درآرامی ‎shed‏ (دیر) .

‎H.Zimmern , Akkadische Fremdworter.Leipzig 1917 ۰‏
رگ ‎lees‏ ۱ س ۳۸ج ؛ یدتم! ۷ ص ۲۸ هز , 511602 ( شبطان, ‎(go‏ عربی‌شرطان (جمع
شیاطین ) « باروچا ۲4۳*. © - بر ماختهُ فرقة آذرکیوان : « شیداب پزشکی بودروشنای
از ‎opt‏ و منظور بطر ازاعیان و سنادید. در اواخر دولت ایام ‎Shae‏ (!) » ( دبتان المذاعي
ص ‎٩۷‏ » و مولف دیستان در(درازدهمین نظر در مذهب شیداییان ) از عقاید این فرقه بحث کند.

‏۱ -ظ . برساختة فرقهٌ آنر کبوان .
‎odes #‏ - از : شیب ۳ ‎Ga;‏ (پسوادمصدری) (متعدی آن :شیرایدن)؛ ءخلوط شدن 1
‎cay)‏ هدن - ارزیدن- جنبیدن .
[pdf page 112]
ARNIS

شید ر نگ ۱ » با رای قرشت بروزن
‎Keg‏ , امپپلوانی ‎oon‏ درتهایت فضل‌رداش

و او طبع را واجب لوجود میداند چه هیچ چیز
خالی ‎gd‏ ایست.

شید و ش ‏ بانانی+جهول بروزن‌ببهوش؛
تام پر کودرز است وگیو برادر او بود .

‎Obed‏ » بکر اول وسکون ثالیءجوول
و فتح دال » بمم‌نی شیداست که هرچیزروشن ۴
‎ty -‏ آفتاب ۴ - و نام پسر افراسیاب باشد .
کوبند چون او بغابت حسن وجمال داشت‌پ-رش
‎sat,‏ ملقب کردانید ۴
که خواهرزادة ار بود روزی با او کفتی‌میگرفت
چناای برزمین زد که ‎Sole‏ شد - و نام یکی از
شا کردان سنماراست که‌,جهت بهرام کورخورنکه
‎prey‏ ماخت ۴ ؛ و ‎gan‏ کویند نام حکیمی

‏و کیخروین سیاوخش

‏بود که بجهت بپرام هقت عمارت فرمود ساختند
```


## [2026-09-14T01:28:37.730Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1320 --image 2>&1 | tail -30"
}
```


### [2026-09-14T01:28:38.786Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 115; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1320.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1320.txt]
[Borhan-e Qate', ed. Mo'in, vol. 3, printed page ۱۳۲۰ = PDF page 111 of BQT_v3_picofile.pdf
 (the tool's default offset gives pdf 115 = printed ۱۳۲۳; correct offset here is printed = pdf + 1209).
 Read from the page image by eye — Persian OCR unusable.]

Headword (right column, bottom):
شید ۳ - بکسر اول و سکون ثانی مجهول و دال ، بمعنی نور باشد مطلقاً که آن روشنایی ...

Mo'in's etymological footnote ۳ (bottom of the page):
۳ - اوستا xshaeta (درخشان)، پهلوی shēt «استق ۸۰۱»، در ارمنی ashxēt (سرخ قهوه‌ای)
[در اسب]، پهلوی shēt-vars (سرخ‌مو)، کردی shē (روباه)، shi (کرد [اسب])
«هوبشمان ۸۰۱» همین کلمه است که در «خورشید» و «جمشید» آمده.

Other headwords on the same page: شیبوی ، شیتره ، شیخ ، شیخ نجدی ، شیدا ، شیداب ،
شید اسپهبد ، شیدان ، شیدآهرمن. Footnote ۴ (on شیدا) derives it from Aramaic/Akkadian
shedu (نام عفریتی)، عبری shed، آرامی shēdâ (دیو) — citing H. Zimmern,
Akkadische Fremdwörter, Leipzig 1917, s. 69 — i.e. a different word from شید «نور».
```


## [2026-09-14T01:28:46.198Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T01:28:46.245Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T01:28:52.919Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sed-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%AF%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%B7%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D7%A9%D7%98%D7%9F\" \\\n \"https://en.wiktionary.org/wiki/%D7%A9%D7%93\" \\\n \"https://www.etymonline.com/word/Satan\" \\\n \"https://www.etymonline.com/word/sedan\" \\\n \"https://www.etymonline.com/word/sketch\" \\\n \"https://www.etymonline.com/word/hostage\" \\\n \"https://www.etymonline.com/word/soil\" \\\n \"https://www.etymonline.com/word/school\" ; do\n  timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 436 verification (Sed, Shedu, Segh)\" &\ndone; wait"
}
```


### [2026-09-14T01:28:56.035Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/965b0a4c9aecd452.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/853a0eca839092a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e972fb55daf4590a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/052471d49e0f1905.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/650319822b7540fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a422d2986aa4d85a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6680f562588d210b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e30f11893953f05b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/26d9a722233354b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/870601d8cac544b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba26319439c7b60d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ad69bd8182aeb77.txt
```


## [2026-09-14T01:29:00.379Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport json,io\nidx={}\nfor line in open('index.jsonl',encoding='utf-8'):\n    d=json.loads(line); idx[d['file']]=d['url']\nfor f,label in [('e972fb55daf4590a.txt','شیدا'),('052471d49e0f1905.txt','شيطان'),('650319822b7540fa.txt','שטן'),('a422d2986aa4d85a.txt','שד')]:\n    t=open(f,encoding='utf-8').read()\n    print('#####',label,idx.get(f), len(t))\n    i=t.find('Etymology')\n    print(t[max(0,i-300):i+2500])\nEOF"
}
```


### [2026-09-14T01:29:01.527Z] TOOL RESULT

```
##### شیدا None 8315
URL: https://www.etymonline.com/word/sedan
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: Sedan - Etymology, Origin & Meaning

Sedan - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of sedan 

 sedan (n.) 

 1630s, "a covered chair on poles, serving as a vehicle for one person," a word of uncertain origin, possibly from a southern Italian dialect derivative of Italian sede "chair" (compare Italian seggietta , 1590s; the thing itself was said to have originated in Naples), which is from Latin sedes , a noun related to sedere "to sit" (from PIE root *sed- (1) "to sit").

 Since the date of Johnson's conjecture, however, the word has been often derived from the name of the town of Sedan in France, where it was said to have been made or first used, but historical evidence for this connection is lacking and OED frowns on it.

 The thing was introduced in England by Sir Sanders Duncombe in 1634 and first called a covered chair . "In Paris the sedan-chair man was usually an Auvergnat, in London an Irishman" [" Encyclopaedia Britannica ," 1929]. 

 Brit. 'Sfoot where's my wife then?

 Sam. If your wife be the gentlewoman o' the house sir, shee's now gone forth in one o' the new Hand-litters : what call yee it, a Sedan.

 [Richard Brome, "The Sparagus Garden: A Comedie," 1635]

 [T]heir use was greatly extended in the eighteenth century, when they were the common means of transportation for ladies and gentlemen in the cities of England and France. They were often elaborately decorated, with paintings by artists of note, panels of 
 vernis Martin , and the like, and lined with elegant silks. Similar chairs, carried on the shoulders of two or more bearers, have long been in use in China. [Century Dictionary]

 Meaning "closed automobile seating four or more" is recorded by 1911, American English, in automotive journals. Middle English had sede (n.) "a chair, seat" (early 14c.), from Latin sedes .
 also from 1630s 

 Entries linking to sedan 

 *sed- (1) 

 Proto-Indo-European root meaning "to sit."

 It might form all or part of: assess ; assiduous ; assiento ; assize ; banshee ; beset ; cathedra ; cathedral ; chair ; cosset ; dissident ; dodecahedron ; Eisteddfod ; ephedra ; ephedrine ; ersatz ; icosahedron ; inset ; insidious ; nest ; niche ; nick (n.) "notch, groove, slit;" nidicolous ; nidification ; nidus ; obsess ; octahedron ; piezo- ; piezoelectric ; polyhedron ; posses
##### شيطان None 9608
URL: https://www.etymonline.com/word/hostage
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: Hostage - Etymology, Origin & Meaning

Hostage - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of hostage 

 hostage (n.) 

 late 13c., from Old French ostage , hostage "kindness, hospitality; residence, dwelling; rent, tribute; compensation; guarantee, pledge, bail; person given as security or hostage" (11c., Modern French ôtage ), which is of uncertain origin. Either from hoste "guest" (see host (n.1)) via notion of "a lodger held by a landlord as security" [Watkins, Barnhart]; or else from Late Latin obsidanus "condition of being held as security," from obses "hostage," from ob- "before" + base of sedere "to sit," with spelling influenced by Latin hostis . [OED, Century Dictionary]. Modern political/terrorism sense is from 1970.
 also from late 13c. 

 Entries linking to hostage 

 host (n.1) 

 "person who receives guests," especially for pay, late 13c., from Old French oste , hoste "guest, host, hostess, landlord" (12c., Modern French hôte ), from Latin hospitem (nominative hospes ) "guest, stranger, sojourner, visitor (hence also 'foreigner')," also "host; one bound by ties of hospitality."

 This appears to be from PIE *ghos-pot- , a compound meaning "guest-master" (compare Old Church Slavonic gospodi "lord, master," literally "lord of strangers"), from the roots *ghos-ti- "stranger, guest, host" and *poti- "powerful; lord." The etymological notion is of someone "with whom one has reciprocal duties of hospitality" [Watkins]. The biological sense of "animal or plant having a parasite" is from 1857.

 H 

 eighth letter of the alphabet; it comes from Phoenician, via Greek and Latin. In Phoenician it originally had a rough guttural sound like German Reich or Scottish loch . In Greek at first it had the value of Modern English -h- , and with this value it passed into the Latin alphabet via Greek colonies in Italy. Subsequently in Greek it came to be used for a long "e" sound; the "h" sound being indicated by a fragment of the letter, which later was reduced to the aspiration mark.

 In Germanic it was used for the voiceless breath sound when at the beginning of words, and in the middle or at the end of words for the rough guttural sound, which later came to be written -gh .

 The sound became totally silent in Vulgar Latin and in the languages that emerged from it; thus the le
##### שטן None 7997
URL: https://www.etymonline.com/word/sketch
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: Sketch - Etymology, Origin & Meaning

Sketch - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of sketch 

 sketch (n.) 

 1660s, scetch , "rough drawing intended to serve as the basis for a finished picture," from Dutch schets or Low German skizze , both apparently being 17c. artists' borrowings from Italian schizzo "sketch, drawing."

 This is commonly said to be from Latin *schedius (OED compares schedia "raft," schedium "an extemporaneous poem"), which is from or related to Greek skhedios "temporary, extemporaneous, done or made off-hand," related to skhema "form, shape, appearance" (see scheme (n.)). But according to Barnhart Italian schizzo is a special use of schizzo "a splash, squirt," from schizzare "to splash or squirt," a word of uncertain origin. German Skizze , French esquisse , Spanish esquicio are said to be likewise from Italian schizzo .

 The extended sense of "brief account" is from 1660s. The meaning "short and slightly constructed play or performance, usually comic" is from 1789; in music, "short composition of a single movement," 1840. Sketch-book "book with blank leaves of drawing paper" is recorded from 1820; it also was used of printed books composed of literary sketches.

 In old slang, a hot sketch (simple sketch for short) was "amusing, ridiculous person" (1909). It turns up first in descriptions of stage entertainment, and a theatrical help-wanted ad from 1906 seeks "a good hot sketch team" for "all circus and vaudeville lines."

 Miss Cora Martini, the Cuban dancer, might be termed a hot sketch. When Girard announced her, the crowd asked her age. Girard said he didn't know as he never liked to ask ladies personal questions. The house told him it was just as well, seeing she wouldn't tell him anyhow. ["Amateur Night at the Gotham," Brooklyn Weekly Chat, Nov. 30, 1907]
 also from 1660s 

 sketch (v.) 

 1690s (Dryden), "present briefly the essential facts of, omitting detail," from sketch (n.). The pictorial peaning "draw, portray in outline and partial shading" is from 1725. The intransitive sense of "make a sketch" is by 1874. Related: Sketched ; sketcher ; sketching .
 also from 1690s 

 Entries linking to sketch 

 scheme (n.) 

 1550s, "figure of speech" (a sense now obsolete), from Medieval Latin schema "a shape, a figure, a form, appearance; figu
##### שד None 9897
URL: https://www.etymonline.com/word/school
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: School - Etymology, Origin & Meaning

School - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of school 

 school (n.1) 

 [place of instruction] Middle English scole , from Old English scol , "institution for instruction," from Latin schola "meeting place for teachers and students, place of instruction;" also "learned conversation, debate; lecture; disciples of a teacher, body of followers, sect," also in the older Greek sense of "intermission of work, leisure for learning."

 This is from Greek skholē "spare time, leisure, rest, ease; idleness; that in which leisure is employed; learned discussion;" also "a place for lectures, school;" originally "a holding back, a keeping clear," from skhein "to get" (from PIE root *segh- "to hold") + -olē by analogy with bolē "a throw," stolē "outfit," etc.

 The basic sense of the Greek word is "leisure," which passed to "otiose discussion" (in Athens or Rome, the favorite or proper use of free time), then it came to be used for the place for such discussion.

 The Latin word was widely borrowed (in addition to Old French escole , French école , Spanish escuela , Italian scuola; Old High German scuola , German Schule , Swedish skola , Gaelic sgiol , Welsh ysgol , Russian shkola ).

 The meaning "students attending a school" in English is attested from c. 1300; the sense of "school building" is by 1590s. Sense of "people united by a general similarity of principles and methods" is from 1610s; hence school of thought (by 1848). As an adjective by mid-18c., "pertaining to or relating to a school or to education."

 School of hard knocks "rough experience in life" is by 1870; to tell tales out of school "betray damaging secrets" is from 1540s. School-bus is from 1908. School days is from 1590s. School board "local committee of education" is by 1836; school district "division of a town or city for the management of schools" is by 1809.

 school (n.2) 

 [large number of fish] late 14c., scole , from Middle Dutch schole (Dutch school ) "group of fish or other animals" (porpoises, whales), which is cognate with Old English scolu "band, troop, crowd of fish," both from West Germanic *skulo- (source also of Old Saxon scola "troop, multitude," West Frisian skoal ), perhaps with a literal sense of "division," and from PIE root *skel- (1) "to cut." Comp
```


## [2026-09-14T01:29:05.873Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport json\nrows=[json.loads(l) for l in open('index.jsonl',encoding='utf-8')]\nfor d in rows[-12:]:\n    print(d['file'], d['status'], d['url'])\nEOF"
}
```


### [2026-09-14T01:29:07.003Z] TOOL RESULT

```
data/verification/sources/web/853a0eca839092a1.txt 200 https://www.etymonline.com/word/Satan
data/verification/sources/web/e972fb55daf4590a.txt 200 https://www.etymonline.com/word/sedan
data/verification/sources/web/052471d49e0f1905.txt 200 https://www.etymonline.com/word/hostage
data/verification/sources/web/650319822b7540fa.txt 200 https://www.etymonline.com/word/sketch
data/verification/sources/web/a422d2986aa4d85a.txt 200 https://www.etymonline.com/word/school
data/verification/sources/web/6680f562588d210b.txt 200 https://en.wiktionary.org/wiki/%D7%A9%D7%93
data/verification/sources/web/e30f11893953f05b.txt 200 https://en.wiktionary.org/wiki/%D7%A9%D7%98%D7%9F
data/verification/sources/web/26d9a722233354b9.txt 200 https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%AF%D8%A7
data/verification/sources/web/870601d8cac544b4.txt 200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sed-
data/verification/sources/web/ba26319439c7b60d.txt 200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-
data/verification/sources/web/8ad69bd8182aeb77.txt 200 https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%B7%D8%A7%D9%86
data/verification/sources/web/8943c6c271c2d839.txt 200 https://www.etymonline.com/word/riot
```


## [2026-09-14T01:29:09.775Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 6680f562588d210b e30f11893953f05b 26d9a722233354b9 8ad69bd8182aeb77; do\necho \"##### $f\"; sed -n '1,6p' $f.txt; grep -n -A14 -m3 \"Etymology\" $f.txt | head -70; echo; done"
}
```


### [2026-09-14T01:29:10.807Z] TOOL RESULT

```
##### 6680f562588d210b
URL: https://en.wiktionary.org/wiki/%D7%A9%D7%93
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: שד - Wiktionary, the free dictionary

שד - Wiktionary, the free dictionary 
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
71- See also 
72-
73- 1.1.3 
74- References 
75-
76- 1.1.4 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Pronunciation 
84-
85- 1.2.2 
86- Noun 
87-
88- 1.2.2.1 
89- Derived terms 
90-
91- 1.2.3 
92- References 
93-
94- 1.2.4 
--
98: Etymology 3 
99-
100- 1.3.1 
101- Noun 
102-
103- 1.4 
104- Anagrams 
105-
106- 2 
107- Yiddish 
108-
109- Toggle Yiddish subsection 
110-
111- 2.1 
112- Alternative forms 

##### e30f11893953f05b
URL: https://en.wiktionary.org/wiki/%D7%A9%D7%98%D7%9F
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: שטן - Wiktionary, the free dictionary

שטן - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
--
158: Etymology
159- [ edit ] 
160-
161- Perhaps from a root relating to opposition or accusation. Compare Arabic شَيْطَان ( šayṭān ) , Aramaic סָטָנָא , Ge'ez ሰይጣን ( säyṭan ) , and Classical Syriac ܣܛܢܐ ( sāṭānā ) .
162-
163- Pronunciation
164- [ edit ] 
165-
166- ( reconstructed Biblical ) IPA ( key ) : /ɬaːˈtˤaːn/ 
167-
168- ( Tiberian ) IPA ( key ) : /sɔːˈtˤɔːɔn/ 
169-
170- ( Modern Israeli ) IPA ( key ) : /saˈtan/ 
171- Audio : ( file ) 
172-

##### 26d9a722233354b9
URL: https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%AF%D8%A7
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: شیدا - Wiktionary, the free dictionary

شیدا - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- Noun 
75-
76- 1.4.1 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Adjective 
101-
102- 2.4 
103- Noun 
104-
105- 2.4.1 
106- Derived terms 
107-
108- 2.5 
--
183: Etymology
184- [ edit ] 
185-
186- Borrowed from Aramaic שידא ( šēḏā ) or Classical Syriac ܫܐܕܐ ( šēḏā , “ demon ” ) , from Akkadian 𒀭𒆘 ( šēdum , “ a protective deity ” ) .
187-
188- For the semantic sense of "mad, crazy; enamored, infatuated", compare دیوانه ( dēwāna, dīwāna , “ mad, fan, patron ” ) . Both stemming from etymological meanings of "demonic" and "crazy", but being poetically used for "love" and "infatuation", especially in Sufi mysticism . 
189-
190- Also for the semantic shift, compare Arabic مجنون ( majnūn , “ mad, insane; enamored ” ) , which is from جن ( jinn , “ demon ” ) .
191-
192- Pronunciation
193- [ edit ] 
194-
195- ( Classical Persian ) IPA ( key ) : /ʃaj.ˈdaː/ 
196-
197- ( Dari, formal ) IPA ( key ) : [ʃäj.d̪ɑː] 

##### 8ad69bd8182aeb77
URL: https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%B7%D8%A7%D9%86
FETCHED: 2026-09-14T01:28:56Z
STATUS: 200
TITLE: شيطان - Wiktionary, the free dictionary

شيطان - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Related terms 
75-
76- 1.3.3 
--
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Proper noun 
103-
104- 3.3.1 
105- Declension 
106-
107- 3.4 
108- Further reading 
109-
110- Toggle the table of contents 
--
196: Etymology
197- [ edit ] 
198-
199- Often interpreted as coming from the root ش ي ط ( š y ṭ ) meaning “to burn , scorch ” and the ـَان ( -ān ) suffix forming adjectives. Given the historical precedence of Hebrew texts wherein the word is of relevance, it is likely that the Arabic word is a reinterpretation of Hebrew שָׂטָן ( śāṭān ) , from a root relating to opposition or accusation .
200-
201- Cognate with Classical Syriac ܣܛܢܐ ( sāṭānā ) , Hebrew שָׂטָן ( śāṭān ) , Ge'ez ሠይጣን ( śäyṭan ) , ሰይጣን ( säyṭan ) .
202-
203- Pronunciation
204- [ edit ] 
205-
206- IPA ( key ) : /ʃaj.tˤaːn/ 
207-
208- Audio ( Modern Standard Arabic ) : ( file ) 
209-
210- Noun
```


## [2026-09-14T01:29:30.595Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; ls | head; echo ---; cat 1320.vision.txt 2>/dev/null"
}
```


### [2026-09-14T01:29:30.667Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1074.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
---
[Borhan-e Qate', ed. Mo'in, vol. 3, printed page ۱۳۲۰ = PDF page 111 of BQT_v3_picofile.pdf
 (the tool's default offset gives pdf 115 = printed ۱۳۲۳; correct offset here is printed = pdf + 1209).
 Read from the page image by eye — Persian OCR unusable.]

Headword (right column, bottom):
شید ۳ - بکسر اول و سکون ثانی مجهول و دال ، بمعنی نور باشد مطلقاً که آن روشنایی ...

Mo'in's etymological footnote ۳ (bottom of the page):
۳ - اوستا xshaeta (درخشان)، پهلوی shēt «استق ۸۰۱»، در ارمنی ashxēt (سرخ قهوه‌ای)
[در اسب]، پهلوی shēt-vars (سرخ‌مو)، کردی shē (روباه)، shi (کرد [اسب])
«هوبشمان ۸۰۱» همین کلمه است که در «خورشید» و «جمشید» آمده.

Other headwords on the same page: شیبوی ، شیتره ، شیخ ، شیخ نجدی ، شیدا ، شیداب ،
شید اسپهبد ، شیدان ، شیدآهرمن. Footnote ۴ (on شیدا) derives it from Aramaic/Akkadian
shedu (نام عفریتی)، عبری shed، آرامی shēdâ (دیو) — citing H. Zimmern,
Akkadische Fremdwörter, Leipzig 1917, s. 69 — i.e. a different word from شید «نور».
```


## [2026-09-14T01:29:35.563Z] TOOL CALL #32: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1320.png"
}
```


### [2026-09-14T01:29:36.218Z] TOOL RESULT

```

```


## [2026-09-14T01:29:36.205Z] INPUT

[Image: original 1375x2122, displayed at 1296x2000. Multiply coordinates by 1.06 to map to original image.]


## [2026-09-14T01:29:56.283Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ shaitan\"; grep -n -i \"shaitan\\|Šaiṭān\\|Saitan\\|shayt\" FVQ_pages.txt | head -20\necho \"=== AFA satan\"; grep -n -i \"sat[aā]n\\|šēdā\\|Satan\" AFA.txt | head -20\necho \"=== KLN Shaitan\"; grep -n -i \"Shaitan\" KLN_1966.txt | head"
}
```


### [2026-09-14T01:29:56.379Z] TOOL RESULT

```
=== FVQ shaitan
397:Madyan, Saba', and many of the commonest religious terms Shaitan,
6892:Moreover, we find Shaitan used as a personal name in ancientFOREIGN VOCABULARY OF THE QUR'AN 189
6917:Krenkow, iii, 37), there is mention of a certain Shaitan b. al-Hakam.
6928:theological connotations of Shaitan as leader of the hosts of evil, is
=== AFA satan
9336:der Satan dem hl« Nonnos in den Acta 8. Pelagiae (ed«
=== KLN Shaitan
33779:Satan,  n.  — ■  Heb.  satan,  ‘adversary’,  fr.  satan,  ‘he acted  as  an  adversary  of,  showed  enmity  to ;  he charged,  accused’,  which  is  rel.  to  Aram.  sitan, of  s.m.  Aram.-Syr.  sdtdna,  Arab,  shaytan,  ‘ad¬ versary,  Satan’,  are  loan  words  from  Heb.  satan. Cp.  Gk.  Zdxav,  Zdrava?,  Late  L.  Satan,  Sa- tanas,  which  are  transliterations  of  Heb.  satan. Cp.  also  Shaitan.
34855:shaitan,  n.,  an  evil  spirit;  the  devil.  ■ —  Arab.
```


## [2026-09-14T01:29:59.529Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6880,6935p' FVQ_pages.txt; echo \"=== pdf tags\"; awk 'NR<6900 && /\\[pdf page/ {l=$0; n=NR} END{}' FVQ_pages.txt; grep -n \"\\[pdf page\" FVQ_pages.txt | awk -F: '$1<6895' | tail -3"
}
```


### [2026-09-14T01:30:01.050Z] TOOL RESULT

```
babbler, j\+A*Amangled,&rid A\<A~* courageous, quoted by Brockelmann,
Grundriss, i, 344, but these are all rare adjectival forms and hardly
parallel the Qur'anic jUaxZi.
Now we learn from the Lexicons that Shaifan has the meaning of
snake O^ A) A*>- (LA, xvii, 104, 105), and we find this meaning
in the old poets, e.g. in a Rejez poet
'' A foul-tongued woman who swears when I swear, like the crested
serpent from Al-Hamat,"
and in a verse of Tarafa,
A M
" They (the reins) play on the back of the Hacjramaut camel, like a
snake's writhings in the desert where the Khirwa' grows."
Moreover, we find Shaitan used as a personal name in ancientFOREIGN VOCABULARY OF THE QUR'AN 189
Arabia. 1 The Aghdrii, xv, 53, mentions
among the ancestors of 'Alqama, and Ibn Duraid mentions a ^
jlkjjjl (240, 1. 4) and a ilijlLl Jr jlktt (243, 1. 3). 2 As a tribal
name we find a sub-tribe of the Band Kinda called
in Aghdrii, xx, 97, and in Yaqut, Mu'jam, iii, 356, we have mention
of a branch of the Banu Tamim of the same name. This use is probably
totemistic in origin, for we find several totem clans among the ancient
Arabs, such as the 4*>- ^1 who in the early years of Islam were the
ruling caste of the Tayyi (Aghdrii, xvi, 50, 1. 7), the ^1 jl (Hamdani,
91, 1. 16), the jjil^ j^[ a sub-tribe of Aus (Ibn Duraid, 260, 2), etc. 3
The serpent was apparently an old Semitic totem, 4 and as a tribal
name associated with one of the many branches of the Snake totem.
van Vloten and Goldziher take jlkx-2 to be an old Arabic word. 5
That the Arabs believed serpents to have some connection with
supernatural powers, was pointed out by Noldeke in the Zeitschrift
fur Volker psychologic, i, 412 if., and van Vloten has shown that they
were connected with demons and evil, 6 so that the use of the name
i for the Evil One could be taken as a development from this.
The use of jUa>i in the Qur'an in the sense of mischievous spirits,
where it is practically equivalent to Jinn, can be paralleled from the
1 Vide Goldziher, ZDMG, xlv, 685, and Abhandlungen, i, 106 ; van Vloten in
Feestbundel aan de Goeje, 37 if. ; Horovitz, KU, 120.
2 So we find a fcj* ^ 0^*^ of the tribe of Jual m ( TA ^ iv 29 ) antl in Usd al "
Qhaba, i, 343, we find a man jliaxJI # Sjy, while in the Diwan of Tufaii (ed.
Krenkow, iii, 37), there is mention of a certain Shaitan b. al-Hakam.
3 Vide the discussion in Robertson Smith, Kinship, 229 ff.
4 Vide Robertson Smith in Journal of Philology, ix, 99 ff. ; G. B. Gray, Hebrew
Proper Names, p. 91, and Uaudissin, Studien zur semitischen Religionsgeschichte, i,
pp. 257-292.
6 Goldziher, Abhandlungen, i, 10 ; van Vloten, Feestebundel aan de Ooeje, 38 ff.
Also Sprenger, Leben, ii, 242, n. 2. Wellhausen, however, Reste, 157, n., thinks that
this has been substituted for some earlier name and is not itself an old Arabic name.
6 Vide his essay " Damonen, Geister und Zauber bei den alten Arabern " in
WZKM, vii, particularly pp. 174-8, and see Goldziher, Abhandlungen, i, 6 ff.190 FOREIGN VOCABULARY OF THE QUR ? AN
old poetry, and would fit this early serpent connection, but the
theological connotations of Shaitan as leader of the hosts of evil, is
obviously derived from Muhammad's Jewish or Christian environments.
In the Rabbinic writings ]B{# is used in this sense, as are the Gk.
^arav and the Syr. Ji^fib. 1 From the Syr. come the Arm.
and also the Phlv. ideogram -tf^ (PPQl, 209), the
Shiddn of the Paikuli fragment, 3 iii, 2, but it is from the Eth.
which occurs beside ftjmt for 6 StdftoXos, that many scholars
have sought to derive the Ar. jUaX-i. 4 Whether this is so it is now
=== pdf tags
```


## [2026-09-14T01:30:09.489Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6935,6960p' FVQ_pages.txt\necho \"=== KLN shaitan full\"\nsed -n '34855,34860p' KLN_1966.txt"
}
```


### [2026-09-14T01:30:09.580Z] TOOL RESULT

```
have sought to derive the Ar. jUaX-i. 4 Whether this is so it is now
perhaps impossible to determine, but we may take it as certain that
the word was in use long before Muhammad's day, 5 and he in his use
of it was undoubtedly influenced by Christian, probably Abyssinian
Christian, usage. (Fischer, Glossar, 165, thinks that the word is from
but influenced by the genuine Arabic juax meaning demon.)
<*~~ (Shl'a).
vi, 65, 160 ; xv, 10 ; xix, 70 ; xxviii, 3, 14 ; xxx, 31 ; xxxiv, 54 ;
xxxvii, 81 ; liv, 51.
Sect or party.
Both plurals jLj!* and P u-i I are used in the Qur'an.
^ -
The verb Pli in the sense of to be published abroad, occurs in
xxiv, 18, and it is usual for the Muslim authorities to derive 4*x* from
this (cf. Raghib, Mufraddt, 272). Schwally, Idiotican., 61, however,
points out that in the meaning of sect the word has developed under
is the form on the incantation bowls, cf. Montgomery, Aramaic
Incantation Texts, Glossary, 296.
2 Hubschmann, Arm. Gramm., i, 316.
8 Herzfeld, Paikuli, Glossary, p. 243. Of the same origin is also the Soghdian
s't'nh (Henning, Manichdisches Beitbuch, 1937, p. 142).
N6ldeke, Neue Beitrage, 47 ; Pautz, Offenbarung, 48 ; Ahrens, Muhammed, 92 ;
Rudolph, AbMngigkeit, 34; Margoliouth, ERE, x, 540. Praetorius, ZDMQ, Ixi,
619-620, thinks the Eth. is derived from the Arabic, but see Noldeke, op. cit.,
against him.
8 Wellhausen, Reste, 157, and see Horovitz, KU, 121.FOREIGN VOCABULARY OF THE QUR'AN 191
=== KLN shaitan full
shaitan,  n.,  an  evil  spirit;  the  devil.  ■ —  Arab.
shaytan,  a  loan  word  fr.  Heb.  satan.  See  Satan, shake,  tr.  and  intr.  v.  ■ —  ME.  schaken,  shaken,  fr. OE.  scacan,  ‘to  shake,  to  move  quickly,  flee, depart’,  rel.  to  ON.  and  Swed.  skaka,  Dan. skage,  ‘to  shift,  turn,  veer’,  fr.  I.-E.  base  *skag- ‘to  move  quickly’,  whence  also  OI.  khdjati, ‘churns’,  prop,  ‘moves  to  and  fro’.  Cp.  shack  in its  various  senses.
Derivatives:  shake,  n.,  shak-able,  adj.,  shaker (q.v.),  shak-ing,  adj.,  and  n.,  shak-ing-ly,  adv. shaker,  n.  —  ME.  schakare,  fr.  schaken.  See  prec. word  and  agential  suff.  -er. shako,  n.,  cylindrical  soldier’s  hat,  with  a  plume. —  F.,  fr.  Hung,  csdkd,  lit.  ‘peaked  (hat)’,  fr.  G. Zacke,  ‘sharp  point,  edge,  peak’.  See  tack, shale,  n.,  scale  of  fish,  etc.  —  ME.  schate,  schal, fr.  OE.  scalu,  scealu,  ‘shell,  dish,  husk,  scale  of balance’.  See  scale,  ‘weighing  instrument’,  and scale  of  fish,  and  cp.  words  there  referred  to.  Cp. also  next  word.
Derivatives:  shale,  v.,  shal-ed,  adj. shale,  n.,  a  fissile  rock  formation  ( petrogr .)  —  G.
Schate,  ‘shell,  scale,  husk’.  See  prec.  word, shall,  auxil.  v.  —  ME.  schal,  shat,  fr.  OE.  sceal, past  used  as  pres. ;  rel.  to  OS.  sculan,  ON.  skola, skula,  Dan.  skulle,  Swed.  skola,  Norw.  skula, MDu.  sullen,  Du.  zullen,  OHG.  solan,  MHG. suln,  soln,  G.  sollen,  Goth,  skulan,  ‘to  owe,  be under  obligation’,  OS.  sculd,  OE.  scyld,  ‘guilt’, OHG.  sculd,  scult,  MHG.  schulde,  schult,  G. Schuld,  ‘guilt;  debt’.  Cognates  outside  Teutonic are:  Lith.  skola,  ‘debt’,  skeleti,  ‘to  owe’,  skilti, ‘to  contract  debts’,  OPruss.  skallisnan,  ‘duty’, and — without  the  initial  x — Lith.  kaltas, ‘obliged’,  kalte,  ‘obligation’.
Derivative:  shall,  n.
```


## [2026-09-14T01:30:13.235Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hazah\\|haz-\\|hazañh\\|hazaŋh\" BRT.txt | head -20"
}
```


### [2026-09-14T01:30:13.291Z] TOOL RESULT

```
22494:•  j.  vaDhaz-dih-'>,  va^haz-°  *>  Adj.  'der das  Bessere  gibt,  der  schenkt,  was  besser ist   (als  gut/:    vJspe  yazatanhö  ySi    'da
27540:—  hamqm  . .  *xsäudrim  (sd.)  °rqm  (AS£) bamts  hamqm  ^papikwqm  N.  64;  64';  — *'paettalnya(sd.yit  °raya  (ISf.)  "auch  mit einem  Honigtrank  Opfer"  N.  57;  —  mit payB  fsufa  (sd.)  're  (LSn.)  nHi  gSu?  °re büDSmainc  paitiMirt  V.7,77;  —  vispa- nqmca  aita^qm  pasvqm  asmaniv3  (sd.) 'ra  (ISn.)  .  .'/rabaröi/ yf.i8.jo;  —  yS ape  'rqm  frabaraite  N.48;  Yt(j.3,  V.^. 14  PüZ.;  —  aiwyS  °ra  frabarHS yaoidäta dakmB.pairisih  Y.ö'j.io;  ö'Ä  14,  Vr.  rr.  3, V.I2.  a,  79. 34,  N.*65,  ^i',  ■•"T/;  — yaica ml  layäsca  hazahisla  . .  °rä  frabarät  P. 22;  —  °rä  hl  uzbaraym  YtÄsS;  — altasf  tl  ^atar»  'rä  N.  ^5 ;  —  yS  vS  äpJ . . yazäite  .  .  dahmi}.pairi.aKhar^täby5  ^rabyö Y.68.10;  10',  3,  j(?.i,  57.3,Vr.ö".  i,Yt. '■9.  J-18.  5-8,  9.  ^'-^5,  10-6,  lö,  31,  13. 94,  /7.2',  G,  J.  7,  N.  77,  Vd.5,  Any,  2^;
28050:Zum  Praes.  5  des  V.  'san-  3).  —  O  So  F  i  m Yt.  19.  14,  TJ.  24;  sonst  'Oc  (so  NA.),  wobei aber  die  Epenthese  ungerechtfertigt  wäre.  — ä)  Falsch  S  '5S.  ad.  —  1)  Anscheinend!  In der  Tat  aus  *!Öifr  (b.  ai.  jäläy-)  unter  dem Einfluss  des  reduplizirten  Praesens  zaam' entstanden;  s.  5p.  703  o.  No.  3.  Joham^son IF.  14,  a9;  verfährt  zu  mechanisch;  auch  ist seine  Erklärung  auf  lazäiu  nicht  anwendbar. j,  lazaili,  g.  saanlTi  s.  haz-.
29678:haz-
29682:•  j.,  %.  haz- V.  'sich  bemächtigen'.  Praes.  3 sa-%  s  2fli-'';  Pert  i  zaz-^K
29761:•  j.  hazaDh'an-  :  'tarn-,  hazah'van-  dl  j  die  Genossen  der  Priestermnft)  betrügend': 'Räuber':  _y?  tayus  yS  'zatfAa''>  Y.  ^5.8;  A"'^'^^'^  "^^^  drvatB  arStSil^a  gai^if.'
29779:•  ).,   g.    hazah*  n.  1)  'Gewalt,  Macht':  j
29788:•  j.  hazah'van- Adj.:  s.  unter  Aa<«ff-ia«-.  I  ^ff^Presse:  ya%a  *va  (nämL  Aavuita,
```


## [2026-09-14T01:30:17.600Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29676,29700p' BRT.txt; echo '---'; sed -n '29779,29800p' BRT.txt\necho \"=== find col number\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\noff=0\nfor i,p in enumerate(t):\n    if 'haz-' in p and \"'sich  bemächtigen'\" in p:\n        print('leaf',i, re.findall(r'\\b1[0-9]{3}\\b', p)[:6])\nEOF"
}
```


### [2026-09-14T01:30:18.741Z] TOOL RESULT

```
dby  Google
I79S
haz-
hazanra-
1796
voD  iveien  (die  Gä^as)  aufsagt,  ist  nicht r.,  wer  sie  für  eine  Veisammlung  von  dreien au&agt,  ist  r.    Wie  gross  muss  eine  Ver- sammlung  mindestens  sein,    damit   man die  Ji.  befriedigt?    Eine  Versammlung  von dreien."  N.jj. KompE.  —  Zum  V.  'Ani;  eig.  'Siuung'.    — u.  tiUb-d.  n.  'Feier,  Feit';   s.  daia  IFAni.  Ä 15.    —    Pü.:  haHJaman.    —     ')  Der  folgende Text   iit    Dicht   in  OTdnone.    Auch    die   Pü. nicht.     Abweichend  überielit  DsT.  ZA.  3.  99. S.   noch   No.   3  ff.    —    1)   Liei   aratu/f.    — J)  Erginze  rahtfr'.  —  *)  Liei  %Tii.hattnm ;  td.  '
•  j.,  %.  haz- V.  'sich  bemächtigen'.  Praes.  3 sa-%  s  2fli-'';  Pert  i  zaz-^K
i)  'sich  bemächtigen,  in  seinen  Besitz bringen,  gewinnen';  a)  mit  Akk.;  tri- %mttm  xia'hnm  zazaiti  (3SKPA.)''  Yt. 5.  i3o(?).  b)    mit    Lok.:    hanaema(3
*awia{i  POP  A.  Va . .  ^wahml  rafinakl  dary- gäyau  "verdienen  möchten  wir  uns  und  ge- winnen deine  tangdauemde  Unterstützung" Y.  4r.  4;  —  ysi  zciantl''>  vanAäu  sravaAi "die  sich  einen  guten  Leumund  erwerben" Y.^.  10;  —  xa*ji>  (NS.)  6uyi'>  va^hüvca müde  vanhauca  sravahe  urunaiia  darrte havanhe  "damit  ich  mir  den  guten  Vor- teil erwerbe  und  . ."  A.  /.  1 1 ;  —  fUSit iahmi  sazva  (NS.)  yö  nBil  urune  xasva "nichts  hat  gewoimen,  wer  (es)  nicht  für seine  Seele  gewonnen  hatf'  FrD.^*>;  — nSit  cahmi  *zatus^  (NS.)  yS  nSii  *urune *tä3ui^>    FrD.^".  2)    absolut    'im
Kampf  gewinnen,  den  Sieg  davontragen': ya^a  U  vtspe  aurvania  xazvävÄa  (liF.) paiti.jasqn  ydka  (Sp.  1 243  o.) . .  vistäspahe YL  5.  13a»);  —  «ae»/a  (LP.)  vupaisu vanhusu  tazusu  vlspaUu  aiff.eihralsu P.  27.
Ü.  sähate ,  sähvan ;  gr.  a%if,  'tX"'  —  ^"-  ■ gri/ian ,  gri/tär  Ulan  -  eiL :  ö  j'ii  iartan  -, (ru  Y.  41):  sinävttndetälan  -  Sü. :  sädkaTtayi- tuM,  —  >)  S  51-  2.  lOi  L  1  mit  No.  a,  311, 313.  9,  Jjolb;  Bgm.  Grdr.»/.  558,  BN.Stud. /.  397.  —  >)  Thom.  —  3)  Man  könnte  natür- lich auch  einen  Stamm  vaa-  anietien,  s.  va- vana:  Zu  Y.  6i.  6  sind  die  WStter  in  NA. ^schlich  verbunden.  —  *)  Vgl.  iSt,  Mx.  /.  a8. —  M  So  nach  der  Var,  —  *)  Hds.  Jaiu}.  — ?)  Scheint  nur  eine  Variante  des  vorherg. Satzes  zu  sein.  Pü.  hat  freilich  für  xaxva grift,  für  M3w/  dagegen,  das  DsT.  ZA,  ^.  IJI für  einen  Aorist  sa-m-i  halt,  sirit.  —  ä)  VgL Y.  57.  12  unter  gam-  mit  paiS.
*  %■  (•  jO  ha-zao6a-  Adj.  'gleichen  Willens, gleichgewillt  mit  — '  (Instr.):  vahistfm  '^wä vahiitä   ySm    aiä    vahtstä    'Am    ahunm
".  .  dich,  o  bester,  den  mit  dem  besten A.  gleichgewillten  Ah."  Y.  21?.  8 ;  —  ahuri . .  ala  'SB  masdä  "AAM.,  der  mit  A.  gleich- gewillte"  V.2p.  7;  —  tat  vS  nS  'iäoha (VP.)  vUpänkB  daidyäi  savB  "diesen  euren Nutzen  sollt  ihr  uns  gewähren,  ihr  gleich- gewillten (Götter)  alle"  Y.5/.  20.
KompE.  —    aL  laj'ifa-  Adj.  —    Pü. :  fia  ikam
äBÜitilh.
•  j,  yim  vä  ainim  *Ad6B^al%a  (sd.) "hazaoäyä  paanha"  layqn  N.  /.
Pü. ;  undeutlich.  Vll. :  pa  dSHSn  -  pa  kämak  - i  ^eJ  u  S/räi  -  dastatoarih  -  1  öiän  i  haat- trätarän  i  apärllan  d.  i-  "auf  seinen  eignen Wunsch  (WUlen)  und  mit  Genehmigung  (Be> votlmächtigung)  der  andern  Genossen".  Da- nach vll.  kva  toBsa  uta  iänha'1  zu  lesen').  — ')  Ai.  Jäia-  m.,  vgl.  jämä-,  wofür  Npft. ämüxtuH  hat,  ebenso  wie  für  öfräs,  die  Ubier- setzung von  "paiaha  c=  sin/vi,  in  Mx.  — >)  Anders  HoKN  KZ.  34.  5S3.
•  j.  hazanra-  neutr.  Zw.  'tausend':  hist^nti .  .  yazalänhs  iattmla  'rtmca  YL  Ö,  i ;  — yä  .  .  paica  vazinti  xsvai  tatäü  •rtm'a Yt  5.  95.  a)  mit  Gen.:  ydi^a  'nrn narqm  "Htm  nartm  arwyaxiaySit  Yt  /.  1 9 ; Ä  55,  io.  69,  128-131*,  Y.65.  4';— _yaäa na  satimca  "tfmca  baivanca  *parsanqm ''ni/abmlsd.)  Ayät \t  13.  JI -,3.31,  63,  120, Ä4S-5-3.  10,  JO.82,  A.J.7-11*,  V.J.31, 37',  /A'.  70-73»,  74'',  2/.  7,  22.3-4,*,  Y. 6S.1S,  N.42',  H./.s,sVar.,  10;  —  'rai (ab  Gen.)  bar>sna  vlranqm  YL  5.  96; £49;  —  'r»m  (statt  Instr.)  ha<ia.cikanqm (sd.)  V.4-ioi  —  y^ /"""i  fl^q^t  daei-a- nqm  'rai  'rB  pairi  Yt_j.  10  •';  4.  2  ",  Vyt ig'K  a)  mit attrib. Einerzahlen:  ioiitfa- rasca  a^a  garayB  . .  ca'^aiargsatfm{sd.)/a
.dvaiea  satte  dvaica  =«  (ND.)  Yt/p.  7; '  —  nava^a  yaskS  navailisca  navaca  sata j  navaca  'ra  navas!s{sd.)ia  baivqn  V.  22.  3; !  Ytij-sg.  i)mAGK^\duyfrevpap€tnam j  V.  7tf.  73;  73%  Vd.  6  (-rohe).  b)  adjekt i  gebraucht:  ha'^ra  . .  yasata^byO  . .  panäx- \saiblica  laiaisca  'räiS^a  batvanbls^a  Vr. ,8.\;  —  'nm  vq%wh  bavatti  YLj<S'.5";5*'; I  —  'nmyanm  Vytf"; — 'raw^alsNom.) I  sünXs  strX.nSmanS  'räis  sunit  nairyS.- .itämanB  V.  y,  51;  14.1';  —  *rw«  (als I  Gen.)  narqm  .  .  taoxma  ,  .  xiva^  lata  . . tisrB  sata  (sd.)  V.  2. 30.
KompA.,  E.;  Ableit.  —  ai.  sahätra'  n.,  np. kiuär.  —  Pü. :  tOOO.  —  ')  Wo  'um  statt  duye •rt  lu  lesen.  Die  Abschreiber  haben  den Wechsel  von  V.  18.  73  auf  74  übertrafen.  — 1}  Werllose  Stellen.
dby  Google
1797
bazaDra.gao^a-
hazaeba-
1798
---
•  ).,   g.    hazah*  n.  1)  'Gewalt,  Macht':  j
daroä  . ,  alä  'zs  smavai  "schenk  . .  durch  ! As'a  starke  Gewalt"  Y.33. 1 3 ;  — gartma  (sd.) , ^rS  hyat  .,  vartAsui  'tS  jtmal  matiat»As\ ". .  die  Macht  des  guten  Sinns  '>  . ."  Y.  .  j.  hahya-  Adj.  'der  es  mit  dem  Getreide, 4-3- ^-  3)  'Gewalt,  Gewalttat':  5a/ /i   der  Getreideerate  zu  tun  hat,  fnimentaiius',
snaehntis  .  .  •*!!  nivansaym  (sd.)    daaiaU(,a*paiHsJiaAya-{sA.):*paitilAaAlm 'htm Yt  ig.  8o;  —  amä  a^mff  'zasca  . .  äAi/aya  I  Vr.2.  a ;  —  *paUis.AaAyeAe  'Ayehe  Vr.  /.  1. (Sp.  1800  U.)    Y.  3p.  I*\  3)    'gewalt-  ,      Ableit.  aiu  "kakya-  n.  (mit  Verschiebung  dei
same    Wegnahme,    Raub':    ut  gSui  siuyl<      Wortakients).  —  PiL:  transskr.,  dain  dieEiL: tayäatra  -taaAai^ä  Y.  12. 2;  —  -zS  F.  25b. !     ^^  ^"''"'^  ^'^  "^'^  '>''•
AbleiL  —  Zum  V.  Aa«..  —  u.  sähai-  n.  —  \»   j.,  g.  ha(y)-  V.   'binden,    schliessen'.
PiL:   staxmak,   (lu  V.  3?)  erl.;   kum  ofF  apä-    praes    %   Aava-''>-   —  Perf    I   /iwäv     —
-    .)  D.i.    die   Macht,    wie   sie    dem   Gut-   PPn"-  '"*"-•  I°f-   °'*^'>«.   *'^3^rat. gesinnten  versprochen  ist    Pü.:  ia  ö  man  än\       l)  binden,fesseln':j'^4l'ffi(nämL<l!aAaffi) i  fa  vahaman  ilaxmak  äyii,    erL :  iS^-äns.  —    stätam  hitam  Aaitim  utvaiat  Aala  AinBtayS «)  Nach  Pa.  i^elmehr  lu  3.-   «  Sol    s^  zu    (sd.)  Yt /J.  100;  —  Ä»»'.     '    a) 'verbinden, hazaiihan-  und  Su. :  yfl  ha!hal  harati.     Falsch  ,..'       .',  .         i-fj  ._i
äzärit  (nach  Npü,)  MiLu  G.  20.  -  4)  S.  lu : «"«    einander     in    Verbmdun^    setzen': haznahtn-.
I  °Aita-,        a)  von  den  beiden  Teilen  der
•  j.  hazah'van- Adj.:  s.  unter  Aa<«ff-ia«-.  I  ^ff^Presse:  ya%a  *va  (nämL  Aavuita,
j.  htttdyäl:  s.  'had: j.  Aala,  Aase:  1,  Aaxay-.
•  j.  haSi-  f.  Name  einer  Datvl:  naiBm
janat  *Ii  janal  Yt  ^  a ;  —  bajat  nartm alavamm  Aala  nasüm  kaia  °H  Yt  4-  3- Wertlos.
NpÜ.!  xah». j.  Aaji'  (KompA.):  i.  kaxay-  mit  Mo.  3. •  p.  haSitiya-'>  Adj.  (fem.  °yä')  'aufsässig,
]  sd.)  *däityS  Atta  N.  loy.  3)  'anspannen, anschirren',  an  den  Wagen:  Ailö  F.je; —  Aita';  —  s.  auch  Atta-  bes.
mit  ä  i)  'einzwängen,  be-,  imterdrUcken': J''  tnä  aistmS  Aatasiä  [fvmff]  ä'^Aisäyj dmlca  tfviscä  (sd.)  "Raserei  bedrückt  mich und  Gewalttat  [.Grausamkeit]  und.."  Y.sp. I ;  —  s.  noch  In£  aAsthsi.  a)  'impedire, inhibere',  mit  Akk.  und  Inf. :  f^al  ^ainaii/U
iauvm^i,  ya'i  alm.'m.s.3.  l"dass  ,ch  den  /JrTO=oosstn  Emhalt  tue
Et!    Vgl  BTHt  AT.  ^.  28.  BB%<.  »so,  ..  1 »   '>>"»   GewaltUtigkiiM  gegen
db,Google
mit /aiA' 'sich  eatschliessen,  beschliessen':  1 s.  Inf.  *paitisährJi.  I
M.iyä(i'},ii}äj-a.«iäi:ap.gH!äyad'tT  öffnet' '),i  9  g,  hätä-maränav-,  i.  häta.niar«nay- (lu  Y.  29^  a/ä.;  (.u  N.).V«hh;  s.  noch  .J 1  ^"^J"  ">"*  mcmor  der  im  Gedächtnis den  Inf.,  zu  Ma-  (und  Komp.)  und  No.  3.  —  '  hat,  was  emer  (als  Lohn)  verdient  hat': >)  Das  Aw.  hat  die  Simplexform  Aaya-,  das  pourB  amh  SnaxHä  yäü'  srSvakyäU  (sd.) Aind.    die   Kompfom    sya-   Terallgemeinert; ,  j,„f  tau   ahä    -ränl  (VS.)    akurä   vahisti
'J'"''!,^-  n-^°-i'^?''"'^Ä"P*-^'^"'U^«''»  ^nana^hä  ".  .,  der  du  Jedermanns yad.  —  'I  Zur  Doppelsetiung  des  Praev.  am  I    ^      ,.  r-    ,     J      -     1        J'-'"-""'"™»
=== find col number
leaf 974 ['1796']
```


## [2026-09-14T01:30:30.972Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if \"hazah*  n.  1)  'Gewalt,  Macht'\" in p:\n        print('leaf',i); print(p[:160])\nEOF"
}
```


### [2026-09-14T01:30:32.077Z] TOOL RESULT

```
leaf 976
 Stars  V.&.So;  So  PüZ.
Ableit.  aus  '-pia-').  —  Pü.:  /ij  looo lanisniA.  — ■>  Oder  aach  un-Part.  tai  gaa-;  It'.  lo.  195,
•  j.  hazanra-jnäi  In
```


## [2026-09-14T01:30:38.298Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC sed\"; grep -n \"sedō\\|sedo\\b\\|seghō\\|segho\\b\\|séd-\\|sed-\" IEC.txt | head -20\necho \"=== WLD Bd2 sed\"; grep -n \"sed-\" incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== WLD Bd2 segh\"; grep -n \"seĝh\\|segh-\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T01:30:38.421Z] TOOL RESULT

```
=== IEC sed
2334:dm-pedom (-pods) “site, land, footing, base” Gk. dá-pedon “ground, floor; Br. danvez *building-material; OHG, MHG zumft ‘guild; rule, status, discipline OE toft ‘site; ON tupt, topt ‘homestead’; Dan. toft *'smalihold- ing’; Norw. tomt ‘site’. Cf. Gk. héme-, hume- dapós ‘native’ and Myc. edapo-, Gk. é-daphos, (f. fr. *sed-dmbhos, and ki-dáphe “lie- aground’ > 'fox). (Gk. oü-das fr. *oio-dms *Jevel-ground" (?))
2508:drütos (1) “wooden, of oak, of hardwood; solid, firm, strong’. WP I, 804 Per. durüd ‘timber, plank’; Arm. cf. artuc Cjuniper, fr. *drutio-); Gk. drútë ‘wooden bowl, wooden coffin’; Alb. i drutë ‘wooden’; Lat. cf. in-druticare Clusurate fr. Gaul.); Mir druit (€compression', but cf. drudh-); Gaul. drutos (sturdy, brisk’, substr. in Fr. dru); Li. drūtas “thick, solid, strong’. Cf. also dru- in Gk. dru-pepés ‘ripened on the tree’; drü-ppà ‘olive’. (The source of Gk. hi- drütós “set, established" is uncertain, perh. fr. *sed-, *síséd-)
2601:dus-, dusi-, px. 'ill-, mis-, hard-, un- (z- gde to duis- and deus-). Cf. dusá, dusoros Skt. dus-, dur-, etc: Av. du&-, duZ-, dus-, etc. OPer. du$-; Arm. suffix arku (in dzajn- arku ‘weeping’, etc.) beside erkn, erkk ‘toil’; Gk. dus-, cf. also o-dúnē, dúē ‘grief, misery’; Ir. do-, Gaul. du-; OBr. do-; MW dy- (in dy- hedd ‘ill-health, sad state’, fr. *dus-séd-); Go. tuz-; OHG zur-; G zer- (also fr. dis-, q. V.); OE ON tor-; e-gde in OE teosu Cham", fr. *deusu-). See next
11903:ndó “into, in'. Cf. endo, en-, do. Variant: ond(o). Some evidence ambig. Cf. nti Arm. (ambig.) ond Cum For other senses cf. ndh-, nti (onti)); Hitt. (ambig.) anda, id.; Mes- sap. anda, id.; EMAIb. éndé, mod. né, prp. "nto, in’; Ir. ann- 'in-; W cf. ann-edd, f. (*dwelling', fr. *ndo-sed-)
12152:-omos, theme of present passive participle (also as an adjective -omos, -omà) E. Arm. cf. utum em “am eating’; gorcum em (am working’. Cf. -omeno-); Skt. cf. jrvama- yah ‘animate, living’; archaic Slavonic 'Sarma- tiar cf. prosedamum, n. (‘sterility in animals’. Pliny. Earliest record of a Slavonic word?: OCS *prosëdomü as pres. pass. pt. to proséd- noti se ‘being broken’); OCS vidomá “visible”; védomü ‘known’; ne-ctajemü “unexpected: Li. cf. menamas ‘supposed’; supamas 'surround- ed'; gyvénamas “inhabited': ne-judamas ‘im- movable’; Latv. grieZams ‘being cut; turn- able’; kustams ‘mobile’; protams *understand- able’; slaucama govs ‘milch cow’, etc. A simi- lar aspect (but with extn. *-imo-, *imà) is present in Lat. sacrimum ‘new wine being of- fered to Bacchus’; victima ‘animal to be sacri- ficed'
12921:pisdó (piséd-, pisod-) “bear down on, trample'. Cf. pi- (epi), sed-. WP I 122 & II, 486. See next Skt. pidayami, v. ‘squeeze, press’; Gk. piézo, piazo, v. id. beside psiázo, v. (dance, fr. *Ks- pi-sodio); Ir. (?) iadhaim, v. ‘enclose, brace’; W (?) eddu, v. ‘press on, go: OCz. pezd, gs: pzda, m., pizda, f. 'arse
13290:podios, iom, io of a foot, of a base, of a pace; foot, base, pace', etc. Cf. ped-, pod- (pods) and extns. WP II, 23. Adjectival variant: podiko- Skt. (vowel ambig.) pádyam ‘syllable’; pádya, f. “pace; path"; Oss. faz, Dig. fazà ('buttocks'. Vocalism as Lat. podex, but this is ambig. « *posd-?); Arm. oC, i-st. and o-st. (2) *haulm"; cf. atean, gs: ateni, i-st. ‘tribunal’; Gk. pódion, n. ‘small foot, foot-bandage'; (LW in) Lat. podium, n. ‘balcony, theatre-box'; Ir. oidhe, m. 'traveller'; OCor. odion, late Cor. ojyon, m. ‘0X’; Br. eZenn, s. id.; Icel. fet, n. ‘pace, step, foot’; OCS. poZzdi, m. “floor, pavement, foundation’; Li. padis, gs: padZio, m. ‘base’. For *podik- (podok-) cf. Skt. padikah “pede- strian’; Arm. h-atak, i, av, s. (bottom, base’, fr. *en-podok-); Gk. cf. a-pódikos “without standing, outcast’; Gaul. odicos, odecus, odo- cos *dwarf-elder'. (Lat. podex ‘arse’ is ambig. Despite the phonological equivalence of Oss. faz, fazà, id. the background may be *po-sd-, see po-, sed-). Cf. LG fette, f. 3oist
13586:pró-sed-, cf. pro-, séd- Skt. pra-sadabh, m. “high seat; palace’; -sadi- kah, adj. ‘friendly’; Gk. (hapax) pro-edikós, adj. “landed, ground-; OCS pro-sédati, v. ‘penetrate’
13729:(‘vulva’, but pith, m. id. is fr. a type *pisdom, à, q.v. and cf. pi-, epi- and sd-, sed-); Lat. cf. sal-püga beside sol" soli (5jump-tail' hence ‘poison ant); Big. pia, (^wench', fr. *pugio). (Isophone: Skt. puja, f. honour)
14359:qusoitos (1) “bright, red? Av. xSaeto “bright; Per. Said (2), id. beside sed-, cpds. (“bay” of a horse); (LW in) Arm. ašxęt, adj. (“bay” of horse); Arm. xajt, i-st. *dapple, speckled’; Oss. áxsid, Dig. àxsed (cred Of sky)
15037:-sd-, syncopated form of type séd-, q.v. Cf. nisdos, and Skt. pitham, n. (footstool, base”, fr. *pisd-); pidáyami, v (“press upon’: Gk. piézo); (but Gk. hízo *make sit: Lat. sido, ére 'settle down' represent a type *síséd-, q.v.); OCS cf. jazdo, jazditi ‘ride’, fr. *ja-, -sd-, cf. iaio, & cf. OCS
15042:séd-, radical element of following entries: ‘sit’. Cf. -sd-
15044:sédàio “seat; be seated'. WP II, 483 Skt. sadayami, tr. ‘seat’; Lat. sedo, are, f. ‘allay’; OHG, MHG sazen, tr. ‘set, settle, oc- cupy'; OE s&tian, v. *waylay'; OCS sédajo, ati, v. intr. “sit, settle’; Li. cf. (for *séd-) sedóm, sédomis, adv. 'seated'
15045:sed-dhlários, io Lat. sellaria 'sitting-place, parlour’; OCS (and com. Sl.) sedlarí fsaddler'. WP II, 485
15046:sed-dhlom ‘seat, settle’. Cf. sedlo- Gk. cf. edéthlon, n. (foundation, pavement’, fr. *sed-edhlo-); OE seld, n. “hall, seat, throne’; MLG selde, sólde, n. id.; OE selda, wm. ‘retainer’; OCS selo, n. ‘field, tent’; cf. also sédelo, sédalo, n. (/seat': Gk. edéthlon); Cz. sídlo “seat; country house’; cf. u-sedly, adj. ‘settled’
15049:se- — séd-mi (sédàó, sedio, sedeio)
15058:sedis, sediom, io (sed-) ‘seat’. WP II, 483-4 Skt. sádas, n. “seat, abode'; sadáh, m. “sitting, riding’; Av. haóis, n. ‘seat’; Ober hadis, id.; Arm. cf. stor, i-st. (bottom, fr. *sedeuis) (?); OLat. sedda (sic) ‘saddle’; Lat. sedes, gs: -is, gp: sedum & sedium, f. “seat, place, base’; -sidium, in cpds.; MIr. sid, mn. ‘peace’; Ir. síodh, s. ‘burial mound, cairn’; MHG sase, sf. ‘seat, place, siege, dwelling, manner’; OE sæt, f. ‘ambush’; sæte, f. (id. & 'house"); OFris. sete, f. ‘pledge’; seta, wm. “home; Du. (*sed-) zeet, f. ‘seat’; Icel. sáta, f. ‘haycock’; Sw. sáte, m. id.; säte, wm. "seat: ON sætt, pl. sætir ‘reconciliation’; sæti, n. ‘seat; hayrick'; sát, f. ‘ambush’; sæta, f. ‘grass widow’; Sw. sát, adj. “Intimate, affectionate’; n. *wood-joint; OCS pri-séda, f. fambush'; Li. sedis, gs: sēdžio, m. ‘sitting, session”; pa-° 'attender'; Latv. sede, f. ‘sitting’; seZa, f. ‘seat’; (LW in) Finn. saatto
15059:sedlos, om (sedul-) ‘seat, resting-place'. WP II, 485 Hes. hellá, f. id.; Lat. (ambig.) sella, f. id. (but cf. sed-dhlom); cf. subsellium, n. “bench, pew’; Gaul. cf. caneco-sedlon; MHG sezsel, sm. "seat OE setl, n. ‘seat, settle, throne, assembly’; ON sjotull, m. ‘settler’; OCS (and com. Sl.) sedlo, n. ((saddle'. But cf. sed- dhlom); Latv. sedli, mpl. ‘saddle’ beside se- dulka, f. ‘saddle-cushion’. (NB Eng. & Gmc. saddle represents an o-gde form of type *sod- dhlo-). Here also prob. Arm. ety, gs: etey, ab. s. eteyb, s. “place?
15060:séd-mi (sédó, sedio, sedeio) ‘sit’. WP IT, 483 Athematic types: Skt. aor. subj. 3s. satsi: MIr. seiss, 3s. *will sit; OLi. sédmi, 3s: sésti. Other- wise Skt. sádami, v. (sit; Ober Av. sad-; Hom. hézomai; Lat. sedeo, ere; W heddu, inf. ‘pacify’; Cor. hedhy, inf. ‘cease’; Br. cf. az-eza, inf. (^seat, sit", fr. *ad-sed-); Go. sitan, sv. 5; OHG sizzen (fr. stan < *sedjo); OE sittan; ON sitja, sv. 5. ‘sit beside sæta: OE sætlan, v. *waylay'; Vedic sadáyami, v. “make sit; afflict’; cf. Lat. sedo, are, v. ‘allay’; OCS cf. sedo, sésti, v. ‘sit; séZdo, sédéti, v. "be seated' (and com. Sl1.); Li. sédZiu, sēdēti, v. *sit, be seated"; Latv. sezu and sedu, inf: sedet,
15065:sedos, -es- ‘seat, settlement, place’. (Vari- ants: sedos, seda) Skt. sádas, n. id. beside sadah, m. (*-e- or *-o-: ‘saddle of back"); Av. haóis, n. ‘seat’; Ober hadis, id.; Gk. hédos, gs: -eos, n. id.; OIr. & Ir. sead, gs: seide, f. ‘nest’; W hedd, m. ‘peace’ beside annedd, pl. au, f. (dwelling, < *n- sed-); OHG së3, n. id.; ON set, n. ‘dais’; seta, f. ‘sitting, seat’ beside sjọt, npl. ‘abode’; Du. zeet, f. ‘seat’. Long-gde in Skt. sadáh ‘posture’; Per. ni-hadan, v. ‘place’; ni-hād, s. ‘nature, quality’; ON sát, f. ‘mbush’; sæti, n. ‘seat’; sætt, pl. sætir, f. (reconciliation', semantics of W hedd ‘peace’); Li. séda, f. ‘sunset
=== WLD Bd2 sed
484:und Wz. sed- bei Kluge® s. v. aus; noch andere Deutungen von fest verz.
19742:                                  lit.        sed-mi,
22230:  Ygl. idg.            '^ni-’Zdos                unter sed- „sitzen“.      Als „heruTiterinachen‘‘
30689:"^sed- „sitzen'' gehdrige sedi- „Entkraftung, Yerkoramenheit“ yergleicht);
30691:Zuteilung dieser kelt. \Ydrter fiir „Friede‘' zur \Yz. ^sed- „sitzen“ durch
32052:                                                   sed-                                                       483
32072:sed- „sitzeD“, z. T, mit einer Basis sede\i\                     :   sedl-.
32155:se{i)d-^ wozu sed- Ablautsneuhildung sein miiBte. Ygl. Osthoff Pf. 414f.,
32199:                                                          sed-                                                 4S5
32228:setJialj    sedal n. m. „Sitz, Wohnsitz, Ruhesitz, Statte'^ (idg. ^seilo- aus ^sed-
=== WLD Bd2 segh
31906:                                                           segh-                                           481
31924:segh- j,festbalten, halten; einen im Kampf unterlegenen fest gepackt halten,
32047:    (ahnlich wie segh- „festhalten“).
32049:azgata- j>uiibezwinglich‘‘ (s. u. segh-). Abg. sqgnqti „den Arm ausstrecken^,
```


## [2026-09-14T01:30:43.296Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31924,31960p' incoming/WLD/WLD_Bd2_pages.txt; echo \"==== sed 32072\"; sed -n '32072,32090p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T01:30:43.382Z] TOOL RESULT

```
segh- j,festbalten, halten; einen im Kampf unterlegenen fest gepackt halten,
        iiberwaltigen, Sieg“.
  Ai. sdhate „bewaltigt, vermag, ertragt^^, sdJias- n. „Gewalt, Sieg‘‘=aY.
hazah- n. „Gewalttat, Raub“ (vgl. unten germ, sigis-)^ ai. saJcsa-^ saksana-
„Bandiger, Sieger‘s, sdhu-ri- „gewaltig, iiberlegen, siegreich^^ (: gr. ex^Qog^
oyvQog^ vgl. auch germ. * signs-) av. haz- „sich bemacbtigen, erwerben^^
                                                       ^


(Praes. *zgh-Oj z. B. 1. pi. opt. mBna                          =
                                             gY, oxoTjuev^ red. *se-zgh-o^ assi-
miliert av.           z. B. 3. pi. zaz9nt\ Part. Pf. Akt. za-z-va nom. sg., za-

z-ns-u loc. pi. ; s. Barth olomae Airan, Wb. 1795 m. Lit.); dehnstufig aufier
Pf. alt. ai. sasaha auch med. sasahe^ ptc. salivas-^ Praes. sdhati,^ Imp.
saksva „sei siegreich^ (s. Brugmann IP. 13, 280, KYG. 542 Anm. 1, Grdr,
II ^ 3, 434, 447; ein gr, *a>;^c6c = ai- sahvas- mit nachtraglicher Redupl.
ware nach ihm in cjfico ovv-oxcoxdre II. 2, 217 „zusaramengewachsene
Schultern^^ verbaut, wenn nicht eher ovvoywxojE zu lesen ist als Pf. eines
von ovvoyog „zusammenhaltend^^ abgeleiteten "^ovvoyooy^ *ovv-6yco-xa „bin
zusammengewachsen“, Wackernagel GGK 1902, 737 f., Bechtel Lex. 305).
  Ai. saglmoti „ist gewachsen, nimmt auf sich, vermag zu ertragen-^ av.
azgata- (scheinbar = gr. doyexog) ,.unbezwinglich^^ (Whitney Wzln. 182, Zu-
pitza KZ. 37, 401, Bartholomae Airan. Wb. 228; von einer ahnlichen Wz.
seg^h-,   s.   d.
  Gr. eyoy {elyov^ £oyov,, eoyrjxa^ k'^co und oy^joco) „halten, besitzen, haben;
(mit Adv.) sich so und so befinden^, horn. "JSxxcoq, lesb. extcoq ,,Zuruck-
halter“, E^ig „Yerhalten, Befinden^, ixzixog (s. dazu Boisacq s. v. und unter
*aig- ,,verstimmt“), iyvgog, ablautend (s. J, Schmidt KZ. 32, 353) dyvgog
„haltbar,        sicher,   befestigt“       (:     ai.     sahuri-^        das ursprgl. o-St. war),
,,Pflugsterz“ (=:cymr. haeddel                   f.    ds.,   Gdf ^seyhedhla^ Pick 11^ 296, Henry
Lex. bret. 159, Pedersen I 39, 97), ddiEyrjg, d^yjy/jg „ohne Einhalt etwas
tuend^ (s. dazu Boisacq s. v., Bechtel Lex. t4f), vom -es-St Ev-E^og^ ev-
(pvgg  Hes., sve^la ,.gute Beschaffenheit, Wohlbefinden^*, i^fjg^ icp-E^rjg^
westgr. E^dv „der Reihe nach“ (Gen. Acc. eines Adj. *£i6g. Lit. bei Boi-
sacq    s. V., wozu bes. Bechtel Lex. 128), i^Eh]g ds.;
  horn,     oya „weitaus“ (: dyv-gog — rdyairayv-g)^ i'ioyog ^hervorragend^,
==== sed 32072
sed- „sitzeD“, z. T, mit einer Basis sede\i\                     :   sedl-.

   Ai. sad- {sdtsi, dsadat, Pf. sasada^ scdima^ sedivas-, vgl. av. hazdya-t opt.);
   av. ap. had- (mit Praeverbien) „sich setzen“ {nisaiohasti fiir "^nisasti^  Bar-
tholomae Airan. Wb. 1753f.; nish^daHi s. u.); kaus. (dehnstufig)            sada-                      ai.

yati ^setzt“, av. ni^adnyeiti „lal3t niedersitzen, setzt nieder^, ap. niyasada-
yam „ich setzte^ (vgl. das ^-Nomen sadi- m. „Reiter“)          aksl. saditi s. u.);       —
    arm. nstini (imper. ni-st) „sitze, setze mich^ (vielleicht ^o-Praes. ^ni-zdip
oder sMip-)\ hecanim „sitze auf, reite^^ (Torp bei Bugge KZ. 32, 47, Peder-
sen KZ. 38, 206, nach welchem c aus d            aor, s)     +                ;



     gr. eZopai ^sitze, setze mich“ (Aor. eJoa Horn, loom Pind.); me^co s. u.;
     lat. sedeo, -ere, sedi „sitzen“ (Praes  auf Grund des ursprgl. auBerpraes.
 St. sedc-; Pf. aus idg. "^sedai oder ^se-zd-ni), umbr. sersitii „sedeto“, serse^
zt'ft'f „sedens“, andersesust ,,intersiderit“, lat. sMo^ -are ^beruhigen*^^
```


## [2026-09-14T01:30:51.209Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT sedan\"; grep -n -m2 -A3 \"^ *SEDAN\\|Sedan,\" SKT.txt | head -20\necho \"=== SKT chair\"; grep -n -m2 -A4 \"CHAIR\" SKT.txt | head -20\necho \"=== SKT nest\"; grep -n -m2 -A3 \"NEST,\" SKT.txt | head -12\necho \"=== SKT scheme\"; grep -n -m2 -A4 \"SCHEME\" SKT.txt | head -20\necho \"=== SKT sketch\"; grep -n -m2 -A4 \"SKETCH\" SKT.txt | head -20"
}
```


### [2026-09-14T01:30:51.419Z] TOOL RESULT

```
=== SKT sedan
=== SKT chair
=== SKT nest
=== SKT scheme
=== SKT sketch
```


## [2026-09-14T01:30:54.669Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT size\"; wc -c SKT.txt; grep -n -i -m3 \"sedan\" SKT.txt; echo ---; grep -n -i -m3 \"sketch\" SKT.txt; echo ---; grep -n -i -m3 \"scheme\" SKT.txt; echo ---; grep -n -i -m3 \"chair\" SKT.txt"
}
```


### [2026-09-14T01:30:54.806Z] TOOL RESULT

```
=== SKT size
2656202 SKT.txt
16781:Sedan-chair.  CF.)  Naraed  from5>i/aff, a  inwn  in  France.  Cf.  F.  udoH^  cloth  made at  Sedan  (Litcre).
---
6582:profile.  Otal.  -  L.)  lul.  profiic,  a sketch  of  a  picture,  outline  (Florio).  — L fro,  before,  in  front  \  Jt/um,  a  thread  (Ital. /ih,  thread,  line).  ^  The  mod.  F./ro/U is  al^K)  from  l)al. /n^V^r.
7908:diagram.  (L.  —  Gk.)  L.  diagrami a  scale,  gamut  (hence,  sketch,  plan). « I 8iri7/Ki^/«o,  a  fignre,  plan,  gamnt.  ••  I ita*f(>a^tar,  to  mark  out  by  lines,  deicri »Gk.  dwi,  through  ;  fp^^^tv,  to  write.
10468:delineate.  (L.)  From  pp.  of  L. dtlineare,  to  sketch  in  outline.  —  L.  (/<, down  ;  Itmart,  to  mark  out,  from /iVwd^a  line.
---
16614:Scheme.  (L.  — Gk.)  Fonnerly  schema, »L.  schema. —OV.  9xhtta,  form,  appear* ance,  also  used  as  a  term  in  rhetoric.  * Gk.  ffx^-tf«;,  fut.  of  'x-*'"!  *o  hold,  have (base  o«x-).  CC  Skt  sak,  to  bear.  <V SAGH.)
17381:Sketch.  (Du.  -  Iial.  -  L.  -  Gk.)  Dn. jcAets,  a  draught,  sketch.  »Iti1.  tcAisw,  a first  rough  draught.  »U  uheJium,  a  thing made  hastily;  from  schtiiiuj.  adj ,  hastily made.  —  Cilc.  (rx<Jliof,  sudden;  allied  to ffx'JWv,  ncnr;  from  the  base  <»X'"»  *o  bold. Allied  to  Scheme.
---
3120:Cathedral.  U-  -  Gk.)  L.  cath<drah's eaUsia  =  a.  cathedral  church,  or  one  which has  a  bishop's  throne.  — Low  L.  cathedra, a  throne  — Gk.  iva&cO/xi,  a  seat  —  Gk.  «a^, for  jrarii,  down;  and  \hpa,  a  seat,  chair, from  li»iUkx  (  >-^S-/o^cu),  I  at ;  sec  Sit.
3121:choir.  (F.  -  L.  -  Gk.)  M.  E.  ckaitt, chsure.^O.  F.  chaiere,  cluiett.  —  Low  L. cathedra^  a  throne,  raised  seat*  chair ;  see al.ove.
3289:Chair,  Chaise  ;  see  Cathedral.
```


## [2026-09-14T01:31:04.836Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"### $f\"; grep -c \"شیطان\" $f 2>/dev/null; grep -n -m4 \"شیطان\" $f 2>/dev/null | head -4; done"
}
```


### [2026-09-14T01:31:06.062Z] TOOL RESULT

```
### MON_part1.txt
16
8107:حلم (.)» خواب‌ها» خواب‌های شیطانی؛ 
15990:الیر: 21۳2۲ (عم.) زرنگ» شیطان. متقلب» 
16562:شیطانی است. 
18983:خبیت» عقل پلید] (.) (اخ.) شیطان. هر یک 
### MON_part2.txt
11
14046:خدا و شیطان و هر دسته از راهی در تسخیر 
20595:دست نوشته باشد. کتاب شیطان (شیطانی): 
26171:(کد.) قوس قزح. کمان شیطان: (کد.) قوس 
28681:شیطان است: هنگامی که وقت اجرای کاری 
### incoming/MON/MON_2vol_Adena_v1_djvu.txt
16
8107:حلم (.)» خواب‌ها» خواب‌های شیطانی؛ 
15990:الیر: 21۳2۲ (عم.) زرنگ» شیطان. متقلب» 
16562:شیطانی است. 
18983:خبیت» عقل پلید] (.) (اخ.) شیطان. هر یک 
### incoming/MON/MON_2vol_Adena_v2_djvu.txt
11
14046:خدا و شیطان و هر دسته از راهی در تسخیر 
20595:دست نوشته باشد. کتاب شیطان (شیطانی): 
26171:(کد.) قوس قزح. کمان شیطان: (کد.) قوس 
28681:شیطان است: هنگامی که وقت اجرای کاری
```


## [2026-09-14T01:31:12.582Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 90 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%B7%D8%A7%D9%86/\" --note \"page 436 entry 1 node 4: Mo'in entry for شیطان\" 2>&1 | tail -2\ntimeout 90 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%AF%D8%A7/\" --note \"page 436 entry 1 node 2: Mo'in entry for شیدا\" 2>&1 | tail -2"
}
```


### [2026-09-14T01:31:17.843Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8f04adeaa00786cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bd15e58532fd82b.txt
```


## [2026-09-14T01:31:20.960Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### شیطان\"; grep -n -m1 -A25 \"معین\" 8f04adeaa00786cf.txt | head -40\necho; echo \"### شیدا\"; grep -n -m1 -A25 \"معین\" 4bd15e58532fd82b.txt | head -40"
}
```


### [2026-09-14T01:31:21.041Z] TOOL RESULT

```
### شیطان
22: شیطان. [ ش َ ] ( ع اِ ) هر سرکش و نافرمان از مردم و پری و ستور و جز آن. ج ، شَیاطین. ( از منتهی الارب ) ( آنندراج ) ( ناظم الاطباء ). نافرمان. متمرد. ( از فرهنگ فارسی معین ) ( از اقرب الموارد ). || دیو. ( دهار ) ( مهذب الاسماء ) ( مجمل اللغة ) ( آنندراج ) ( منتهی الارب ) ( ترجمان القرآن ص 2 ). || دیو استنبه. ( ناظم الاطباء ). || دیو مردم. ( دهار ) ( مهذب الاسماء ). || بدخوی سخت دل. ( از منتهی الارب ) ( از اقرب الموارد ). || نوعی از نبات. ج ، شیاطین. ( مهذب الاسماء ). نوعی از زقوم. ( تحفه حکیم مؤمن ). || مار. ( از منتهی الارب ) ( ناظم الاطباء ). || ( از ع ، ص ) در صفت بچه شریر بی آرام شوخ. تُخْس. بازیگوش. ( یادداشت مؤلف ).

### شیدا
26: شیدا. [ ش َ / ش ِ ] ( ص ) در زبان اکدی «شدو» . نام عفریتی است. در عبری «شد» و در آرامی «شدا» به معنی دیو است. دیوبت. دبت شد. ( از یشتها ج 1 ص 38 ) ( از حاشیه برهان چ معین ). دیوانه و لایعقل. ( برهان ) ( رشیدی ) ( غیاث ) ( انجمن آرا ) ( آنندراج ). دیوانه. مجنون. ( یادداشت مؤلف ). دیوانه. ( لغت فرس اسدی ). بی عقل و بی هوش. ( ناظم الاطباء ). || آشفته. ( انجمن آرا ) ( آنندراج ) ( فرهنگ رشیدی ) ( غیاث ). سرگردان. ( لغات شاهنامه ). آشفته و سرگردان. ( لغت فرس اسدی ). آشفته و سرگردان. ( اوبهی ). هائم. حیران. ( زمخشری ). آشفته از عشق. ( ناظم الاطباء ). سخت عاشق. واله. سخت شیفته. ( یادداشت مؤلف ). شیفته : 
27-دل برد چون بدانست کم کرد ناشکیبا
28-بگریخت تا چنینم دیوانه کرد و شیدا. دقیقی.
29-بمردی ز خورشید پیداتر است 
30-به پیکار از شیر شیداتر است. فردوسی.
31-برآمد پیلگون ابری ز روی نیلگون دریا
32-چو رای عاشقان گردان چو طبع بیدلان شیدا. فرخی.
33-نکرد این دوستی بر دایه پیدا
34-وگرچه گشته بود از مهرشیدا. اسدی.
35-عالم قدیم نیست سوی دانا
36-مشنو محال ِ دهری شیدا را. ناصرخسرو.
37-نه سخن گفتن نباشد هرچه آنرا نشنوی 
38-این چنین در دل تصور مردم شیداکند. ناصرخسرو.
39-وآنکه گوید خواست ما را نیست میگوید خرد
40-کاین همانا قول مرد مست یا شیداستی. ناصرخسرو.
41-گرچه تو ز پیغمبری و چون تو
42-با عقل و سخن بیهشی و شیدا. ناصرخسرو.
43-درست وراست صفات تو گویم و نه شگفت 
44-درست و راست شنیدن ز مردم شیدا. مسعودسعد.
45-یکی بگرید بربیهده چو مردم مست 
46-یکی بخندد خیره چو مردم شیدا. مسعودسعد.
47-ز پستی لاله شد خندان چو روی دلبر گلرخ 
48-ز بالا ابر شد گریان بسان عاشق شیدا. مسعودسعد.
49-چون مست شیدا در شب یلدا بر در و دیوار می افتادم. ( مقامات حمیدی ).
50-کعبه قطب است و بنی آدم بنات النعش وار
51-گرد قطب آسیمه سر شیداو حیران آمده. خاقانی.
```


## [2026-09-14T01:31:36.711Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sheda\"; grep -n -i \"šēdā\\|sêdâ\\|schêdâ\\|shēdā\\|Dämon\" HRN.txt | head -8\necho \"=== HUB\"; grep -n -i \"šēdā\\|sêdâ\\|Dämon\\|Satan\" HUB.txt | head -8\necho \"=== PHD sedan\"; grep -n -i \"šēdā\\|sedan\\|dew \\|dyw\" PHD_mackenzie.txt | head -8\necho \"=== ARY shayda\"; grep -n \"شیدا\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY sheytan\"; grep -n \"شیطان\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T01:31:36.841Z] TOOL RESULT

```
=== HRN sheda
2433:aw. Biisyqsta' 'Dämon des Schlafes'-); phlv. büsäsp (in
3858:jatuk; ai. yätü- 'Spuk, Hexerei; Spukdämon'.
5347:598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
5349:aw. daeva- 'Dämon'; phlv. dev; ai. devd- 'Gott'.
5372:^) Ursprünglich natürlich 'teuflisch , dämonisch*, vergl. Sahn. 1,
10539:aw. gava- 'Hand' (nur von 'Dämonen'), asengö,gäum ;
10632:Iranischen bekanntlich nur von Dämonen gebraucht.
=== HUB
=== PHD sedan
665:abadyawand [)p)tyd)wnd I J )b)dywn(d)] powerless, weak.
1171:Ardwahist prtwhlt l I M 'rdywhy!t, (N urdibihift)] Right, the second
1980:dew [SD Y A < A fyd\ pI. fydy) I N -] demon, devil.
1982:dewanag [dyw'nk I N --a] demonic, mad.
1984:dewar [dyw'll M dyw'r, N -] wall.
1985:dewl-esnih [SDYAysnyh I (M dyw'snyh)] idolatry, devil-worship.
1987:dewok [dywwk l I N dewuk] leech.
3091:  ",,-dew [-SDYA] anti-demonic.
=== ARY shayda
=== ARY sheytan
12519:چم این واژه در پروسی کهن: خلاص از شر شیطان,
```


## [2026-09-14T01:31:45.852Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1978,1990p' PHD_mackenzie.txt; echo \"=== pdftoppm\"; pdftoppm -f 436 -l 436 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436.png"
}
```


### [2026-09-14T01:31:46.945Z] TOOL RESULT

```
Exit code 1
desidan, des- [dys-ytn I M dys-yd] build.
                          '
dew [SD Y A < A fyd\ pI. fydy) I N -] demon, devil.
dewan [d(p)yw'n l I N -] archive, collected writings.
dewanag [dyw'nk I N --a] demonic, mad.
                      '
dewar [dyw'll M dyw'r, N -] wall.
dewl-esnih [SDYAysnyh I (M dyw'snyh)] idolatry, devil-worship.
 --ezagih [SDYAyckyh] = ---esnih.
dewok [dywwk l I N dewuk] leech.
dibir [dpy(w)r I M dbyr, N --] scribe.
                  '
 --ih: writing, scribeship.
=== pdftoppm
I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-14T01:31:50.158Z] TOOL CALL #48: Bash

```json
{
 "command": "pdftoppm -f 436 -l 436 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436.png"
}
```


### [2026-09-14T01:31:51.802Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66400 Sep 13 21:31 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436.png
```


## [2026-09-14T01:31:53.660Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg436.png"
}
```


### [2026-09-14T01:31:54.250Z] TOOL RESULT

```

```


## [2026-09-14T01:31:54.246Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:32:04.992Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### PIE sed- recon\"; grep -n -m1 -A18 \"Root\" 870601d8cac544b4.txt | head -30\necho; echo \"### PIE segh- recon\"; sed -n '/Proto-Indo-European/,/Descendants/p' ba26319439c7b60d.txt | head -40"
}
```


### [2026-09-14T01:32:06.350Z] TOOL RESULT

```
### PIE sed- recon
62: Root 
63-
64- 1.1.1 
65- Derived terms 
66-
67- 1.1.2 
68- Descendants 
69-
70- 1.2 
71- References 
72-
73- 1.3 
74- Further reading 
75-
76- Toggle the table of contents 
77-
78- Reconstruction:Proto-Indo-European/ sed- 
79-
80- Add languages 

### PIE segh- recon
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-
FETCHED: 2026-09-14T01:28:54Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/seǵʰ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/seǵʰ- - Wiktionary, the free dictionary 

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


## [2026-09-14T01:32:10.810Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### segh root line\"; grep -n -m1 -B2 -A12 \"^ \\*seǵʰ-\\|seǵʰ- (imperfective\\|to hold, to overpower\" ba26319439c7b60d.txt | head -30\necho; echo \"### sed root line\"; grep -n -m1 -B2 -A12 \"sed- (imperfective\\|to sit down\" 870601d8cac544b4.txt | head -30\necho \"### Avestan in segh page\"; grep -n -i \"avestan\\|hazah\\|𐬵𐬀𐬰\" ba26319439c7b60d.txt | head -10"
}
```


### [2026-09-14T01:32:10.964Z] TOOL RESULT

```
### segh root line
132- [ edit ] 
133-
134: *seǵʰ- [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] 
135-
136- to overpower 
137-
138- to take hold of
139-
140- Derived terms
141- [ edit ] 
142-
143- Terms derived from the Proto-Indo-European root *seǵʰ- (76 c, 0 e) 
144-
145- *séǵʰ-e-ti ( thematic root present ) 
146-

### sed root line
### Avestan in segh page
```


## [2026-09-14T01:32:13.489Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '125,200p' 870601d8cac544b4.txt; echo \"=====SEGH desc\"; sed -n '145,200p' ba26319439c7b60d.txt"
}
```


### [2026-09-14T01:32:13.555Z] TOOL RESULT

```
 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *sed- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to sit 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *sed- (108 c, 0 e) 

 *séd-t ~ *sd-ént ( athematic root aorist ) 

 *sí-sd-e-ti ( thematic i-reduplicated present ) 

 *séd-e-ti ( thematic root present ) 
 Proto-Celtic: *sedeti ( see there for further descendants )

 *sed-s- ( sigmatic aorist ) [ 4 ] 
 ⇒ Old Armenian: հեծանիմ ( hecanim ) 
 Armenian: հեծնել ( hecnel ) 

 *séd-ye-ti ( ye-present ) 

 *sod-éye-ti ( “ to set ” , causative ) 

 *sed-éh₁-ye-ti ( eh₁-stative ) 
 Proto-Balto-Slavic: *sēdḗˀtei ( see there for further descendants )

 Proto-Italic: *sedēō < earlier *sedējō ( see there for further descendants )

 *sed-éh₂-ye-ti ( eh₂-factitive ) 
 Proto-Balto-Slavic: *sēdā́ˀtei 
 Proto-Slavic: *sědati 
 Czech: sedat 

 Polish: siadać 

 Serbo-Croatian: sedati , sjedati 

 Proto-Italic: *sēdāō 
 Latin: sēdō ( see there for further descendants )

 *se-sód-e ~ *se-sd-ḗr ( reduplicated perfect ) [ 2 ] 
 Proto-Germanic: *sat , *sētun ( 3sg. and 3pl. past of *sitjaną ) 

 Proto-Indo-Iranian: *sasā́da 
 Proto-Indo-Aryan: *sasā́da 
 Sanskrit: ससाद ( sasā́da ) 

 Proto-Iranian: 
 Avestan: 𐬵𐬀𐬰𐬛𐬌𐬌𐬁𐬝 ( hazdiiāt̰ , 3sg.opt. ) 

 Proto-Italic: *sezdai 
 Latin: sēdī 

 * ḱye -sd-é-ti (< perhaps originally meaning sit/set here )
 Proto-Italic: *kezdō 
 Latin: cēdō ( see there for further descendants )

 *sēd-s, *sed-es ( root noun ) [ 5 ] 
 ⇒ ? Proto-Italic: *sēdis 
 Latin: sēdēs ( see there for further descendants )
=====SEGH desc
 *séǵʰ-e-ti ( thematic root present ) 

 *séǵʰ-se-ti ( (h₁)se-desiderative ) [ 5 ] 
 Proto-Hellenic: *héksō [ 5 ] 
 Ancient Greek: ἕξω ( héxō ) 

 *sḗǵʰ-s-t ~ *séǵʰ-s-n̥t ( s-aorist ) [ 1 ] 
 Proto-Indo-Iranian: *Hásāȷ́žʰat 
 Proto-Indo-Aryan: *Hásāḍẓʰat 
 Sanskrit: असाक्षि ( ásākṣi , 1sg.med. ) , सक्षत् ( sákṣat , “ to overpower ” , 3sg.subj.act. ) 

 *se-sóǵʰ-e ~ *se-sǵʰ-ḗr ( reduplicated stative ) [ 1 ] 
 > ? Proto-Tocharian: *sākā ( “ remain (behind); to restrain ” ) [ 6 ] 
 Tocharian A: sākam 

 Tocharian B: sākāu 

 Proto-Indo-Iranian: *sasā́ȷ́ʰa 
 Proto-Indo-Aryan: *sasā́źʰa 
 Sanskrit: ससाह ( sasā́ha ) , ससाहे ( sasā́he , “ to defeat, be victorious ” , 3sg.med. ) 

 *sǵʰ-e-ti ( thematic root aorist ) [ 5 ] 
 Proto-Hellenic: *ḗskʰe 
 Ancient Greek: ἔσχον ( éskhon , “ bring to a halt, hold on ” ) 

 *si-séǵʰ-ti ~ *si-sǵʰ-énti ( i-reduplicated present ) [ 1 ] [ 2 ] [ 5 ] 
 Proto-Hellenic: *hískʰō [ 5 ] [ 6 ] 
 Ancient Greek: ἴσχω ( ískhō , “ bring to a halt, hold on ” ) 
 ⇒ Ancient Greek: ἰσχύς ( iskhús ) ( see there for further descendants )

 *sí-sǵʰ-se-ti ( i-reduplicated (h₁)se-desiderative ) [ 1 ] [ 5 ] 
 Proto-Indo-Iranian: *sízȷ́žatay 
 Proto-Indo-Aryan: *síẓḍẓatay 
 Sanskrit: सीक्षते ( sīkṣate ) 

 *soǵʰ-éye-ti ( eye-causative ) [ 1 ] 
 Proto-Hellenic: *hókʰeyō 
 Ancient Greek: ὀχέω ( okhéō , “ to have, hold ” ) 

 Proto-Indo-Iranian: *sāȷ́ʰáyati 
 Proto-Indo-Aryan: *sāźʰáyati 
 Sanskrit: साहयति ( sāháyati ) 

 *séǵʰ-os 

 *seǵʰ-ó-s 

 *seǵʰ-tó-s 
 Proto-Indo-Iranian: *saždʰás 
 Proto-Indo-Aryan: *saẓḍʰás 
 Sanskrit: साढ ( sāḍhá ) 

 ⇒ Sanskrit: अषाढ ( ásāḍha ) 

 *séǵʰ-tōr ~ *sǵʰ-tr-és 
 Proto-Hellenic: *héktōr
```


## [2026-09-14T01:32:21.993Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m3 \"seghō\\|segho\\b\\|seghos\\|seĝh\" IEC.txt | head -5\necho \"=== SYN school/sit\"; grep -n -m2 \"σχολή\\|skhole\\|schola\" SYN.txt | head -5\necho \"=== Etymonline Satan\"; sed -n '/Origin and history of Satan/,/Entries linking/p' ../web/853a0eca839092a1.txt | head -30"
}
```


### [2026-09-14T01:32:23.061Z] TOOL RESULT

```
15084:(seghos, à, io, cf. seg-, seng- and se£h-, sengh- Skt. sághan, m. ‘vulture’; Arm. heg, Lat, *syl- lable’; Li. (ambig.) segë f. ‘brooch’. (Seman- tics obscure))
15087:seghis, see seghos Ir. sigh, f. ‘peace’; OE cf. sig, sige, n. & m. ‘victory’; MHG sic, gs. siges, also sige, wm. id.: Ir. seagh, m. 'strength; esteem; value; skill
15091:seĝhlos (2) ‘hold, grip’. (Variant: segh-) Arm. cf. heydznum, heydzanim, tr., intr. ‘choke, drown’; OE sigle, n. ‘collar, necklace’; ON sigli, n. id.; Br. W hual, m. ‘fetter’; (but Li. ségalas “pin” represents a type seg- or segh-)
=== SYN school/sit
189:It is hoped that, with all its inevitable limitations, the omissions intention- al or otherwise, and the errors of detail which may be pointed out by scholars in the special fields, the book may be found useful and worth while as a tentative and skeleton dictionary of synonyms.
9112:Italian scholars render Grk. mAakobs, Lat. libum by focaccia, which in actual use denotes a very special kind of cake, orig. a sort of ‘ash-cake’, like Fr. fouace, fr. *focdcea (cf. focacius Isid. 20.2.15), deriv. of focus ‘hearth’. REW 292. The Sprach- und Sach-Atlas Italiens und der Siidschweiz, Karte 1007 (vol. 5) also gives focaccia (schiacciata) as the heading = NHG Kuchen, Fr. gdteau. The schiacciata is a flat, brittle cake, fr. schiacciare ‘break, crack’.
=== Etymonline Satan
 Origin and history of Satan 

 Satan (n.) 

 proper name of the supreme evil spirit and great adversary of humanity in Christianity, Old English Satan , from Late Latin Satan (in Vulgate in the Old Testament only), from Greek Satanas , from Hebrew satan "adversary, one who plots against another," from satan "to show enmity to, oppose, plot against," from root s-t-n "one who opposes, obstructs, or acts as an adversary."

 In the Septuagint usually translated into Greek as diabolos "slanderer," literally "one who throws (something) across" the path of another (see devil (n.)), though epiboulos "plotter" is once used.

 In biblical sources the Hebrew term the 
 satan describes an adversarial role. It is not the name of a particular character. Although Hebrew storytellers as early as the sixth century B.C.E. occasionally introduced a supernatural character whom they called the 
 satan , what they meant was any one of the angels sent by God for the specific purpose of blocking or obstructing human activity. [Elaine Pagels, "The Origin of Satan," 1995]

 In Middle English also Satanas , Sathanas .

 Entries linking to Satan
```


## [2026-09-14T01:32:47.287Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -c . index.jsonl; grep -n \"etymonline.com/word/soil\" index.jsonl | tail -2"
}
```


### [2026-09-14T01:32:47.374Z] TOOL RESULT

```
4782
4632:{"url": "https://www.etymonline.com/word/soil", "file": "data/verification/sources/web/965b0a4c9aecd452.txt", "fetched": "2026-09-14T01:28:54Z", "status": 200, "bytes": 7767, "title": "Soil - Etymology, Origin & Meaning", "note": "page 436 verification (Sed, Shedu, Segh)"}
```


## [2026-09-14T01:32:50.339Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '/Origin and history of soil/,/Entries linking/p' 965b0a4c9aecd452.txt | head -20"
}
```


### [2026-09-14T01:32:51.367Z] TOOL RESULT

```
 Origin and history of soil 

 soil (v.) 

 early 13c., "to defile or pollute with sin," from Old French soillier "to splatter with mud, to foul or make dirty," originally "to wallow" (12c., Modern French souillier ), from souil "tub, wild boar's wallow, pigsty," which is from Latin solium "tub for bathing; seat" (from PIE root *sed- (1) "to sit") or else from Latin suculus "little pig," from sus "pig." The literal meaning "to make dirty on the surface, begrime" is attested from c. 1300 in English. Related: Soiled ; soiling .
 also from early 13c. 

 soil (n.1) 

 c. 1300, "land, area, place," from Anglo-French soil "piece of ground, place" (13c.). It is attested from late 14c. as "the earth, the ground," and mid-15c. as "mould, earth, dirt," especially that in which plants grow. The meaning "one's land, place of one's nativity" is from c. 1400.

 The word seems to be a merger or confusion of three words in Old French: 1. sol "bottom, ground, soil" (12c., from Latin solum "soil, ground;" see sole (n.1)); 2. soeul , sueil "threshold, area, place" (from Latin solium "seat," from PIE root *sed- (1) "to sit"); 3. soil , soille "a miry place," from soillier "splatter with mud" (see soil (v.)).
 also from c. 1300 

 soil (n.2) 

 "filth, dirt, refuse matter, sewage, liquid likely to contain excrement," c. 1600, a sense extended from Middle English soile "miry or muddy place, bog," especially as a wallow for a hog or a refuge for a hunted deer (early 15c.), from Old French soille "miry place," from soillier (v.) "to make dirty," and in part a native formation from soil (v.). In form and senses also much influenced by soil (n.1). This is the word in the plumber's soil pipe (by 1833) and archaic night-soil .
 also from c. 1600 

 Entries linking to soil
```


## [2026-09-14T01:33:02.120Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:42:07.227Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write436.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 436,\n \"book_page\": 406,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n\n # ---------------- entry 0 : Sed (part 2) ----------------\n {\n  \"entry\": 0,\n  \"root\": \"Sed\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *sed- 'to sit' (Pokorny 884) and *sed- 'to go, to step' (Pokorny 887) — one base whose original sense was 'to place (the seat, or the foot)'\",\n  \"note\": \"Root name, language label and the double gloss are all right, and both halves of the gloss are traceable to the two references Nourai gives. Pokorny p.884 heads the entry 'sed- „sitzen’, ursprüngl. nur aoristisch, punktuell „sich setzen’'; p.887 opens section 'B. *sed- in der Bed. „gehen’, aus Verbindung mit Präfixen entstanden'. Klein p.1075 (s.v. odograph) states the very formula Nourai paraphrases: 'I.-E. base *sed-, “to go”, is identical with *sed-, “to sit”, the original sense of the base having been “to place (either the seat in order to sit down, or the foot on the ground in order to go)”'. Watkins/AHD splits the two as sed-1 [Pok. sed- 884] and sed-2 [Pok. sed- 887]; Wiktionary reconstructs *sed- 'to sit' (perfective). This is PART 2 of the chart; the Iranian/Persian offshoots stand on the preceding page.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sed- «نشستن، نهادن» درست است و پوکورنی در صفحهٔ ۸۸۴ همین معنا را آورده و در صفحهٔ ۸۸۷ بخش دومی با معنای «رفتن» آورده است. کلاین نیز در صفحهٔ ۱۰۷۵ همین دو معنا را یکی می‌داند و معنای بنیادین را «نهادن (تن بر جای نشستن یا پا بر زمین)» می‌خواند — یعنی دقیقاً همان چیزی که در نمودار آمده. ادعای نورایی درست است. این برگ «بخش ۲» است و شاخهٔ ایرانی ریشه در برگ پیشین آمده است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:884\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 119 (= printed p.884, confirmed by the running numerals '889' on leaf 124 and '892' on leaf 127): \\\"sed- ‚sitzen', ursprüngl. nur aoristisch, punktuell ‚sich setzen' (ai.) … sed-to- ‚gesessen', Subst. ‚Sitz'; sed-ter- ‚der Sitzer' … sed-lo-m, sed-lā, sed-ro-m … ‚Sitz'.\\\"\"},\n    {\"ref\": \"POK:887\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 122 (= printed p.887): \\\"B. *sed- in der Bed. ‚gehen', aus Verbindung mit Präfixen entstanden. Ai. ā-sad- ‚hintreten, hingehen, gelangen' … gr. ὁδός ‚Weg' … aksl. chodŭ ‚Gang'.\\\" Exactly Nourai's second gloss 'also to place a step, to go'.\"},\n    {\"ref\": \"KLN:1075\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 575 (pp. ~1075–1076, bracketed by '1072' on leaf 573 and '1081' on leaf 578), s.v. odograph: \\\"I.-E. base *sed-, ‘to go’, is identical with *sed-, ‘to sit’, the original sense of the base having been ‘to place (either the seat in order to sit down, or the foot on the ground in order to go)’.\\\" Nourai's root gloss is a condensation of this sentence.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.483 (WLD_Bd2_pages.txt l.32072)\", \"stance\": \"supports\", \"note\": \"\\\"sed- „sitzen“, z. T. mit einer Basis sede[i]- : sedl-. Ai. sad- … av. ap. had- (mit Praeverbien) „sich setzen“ … gr. ἕζομαι … lat. sedeō.\\\"\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sed-1 and sed-2\", \"stance\": \"supports\", \"note\": \"\\\"sed-1, To sit … [Pok. sed- 884.]\\\" and \\\"sed-2. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey … [Pok. sed- 887.]\\\" — the same two Pokorny pages Nourai cites.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann cols. s.v. séd-, séd-mi, sedos, sedlos\", \"stance\": \"supports\", \"note\": \"\\\"séd-, radical element of following entries: ‘sit’\\\"; \\\"séd-mi (sédō, sedio, sedeio) ‘sit’. WP II, 483\\\"; also \\\"sedos, -es- ‘seat, settlement, place’ … Av. haðis, n. ‘seat’\\\".\"}\n  ],\n  \"nodes\": [\n   {\"id\": 1, \"lang\": \"Germanic\", \"words\": \"\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"An empty pass-through box: Proto-Germanic inherited the root as *setjan- 'to sit' (< *sed-ye-), with the causative *satjan- 'to set' (< o-grade *sod-eye-), the noun *setlaz 'seat' (< *sed-lo-) and *sadulaz 'saddle' (< o-grade *sod-). Verner/Grimm regularly give Gmc. *t for PIE *d, so *sed- > *set-.\",\n    \"derivation_fa\": \"این خانهٔ خالی فقط واسطهٔ گذر است: ژرمنی آغازین ریشه را به صورت *setjan- «نشستن» ، *satjan- «نشاندن» و *setlaz «نشستگاه» به ارث برده است؛ بر پایهٔ قانون گریم دال هندواروپایی در ژرمنی به t بدل می‌شود. ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n    \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sed-1 §1–6: 'Suffixed form *sed-yo- in Germanic *sitjan … Suffixed (causative) o-grade form *sod-eyo- in Germanic *satjan, to cause to sit, set … Suffixed form *sed-lo-, seat, in Germanic *setlaz … O-grade form *sod- in Germanic *sadulaz, seat, saddle.'\"}],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.884–885 (POK_03 leaves 119–120)\", \"stance\": \"supports\", \"note\": \"\\\"as. sethal m. ‚Sitzen, Sitz' … ahd. sethal, sedal n. m. ‚Sitz, Wohnsitz, Stätte' (idg. *setlo- aus *sedtlo); germ. *sadul- in: aisl. sǫdull, ags. sadol, ahd. satul, satal ‚Sattel'.\\\"\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.485 (WLD_Bd2_pages.txt l.32228)\", \"stance\": \"supports\", \"note\": \"\\\"setȝal, sedal n. m. „Sitz, Wohnsitz, Ruhesitz, Stätte“ (idg. *seṭlo- aus *sed-…)\\\" — the Germanic branch of the root.\"}\n    ]},\n\n   {\"id\": 2, \"lang\": \"English\", \"words\": \"sit, set, settle, nest, seat, saddle\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"All six are native Germanic inheritances. OE sittan (< Gmc. *sitjan < *sed-ye-) > ME sitten > sit. OE settan 'to place' (causative < *sod-eye-) > set. OE setl 'seat' (< *sed-lo-) > ME setel > settle; the verb settle is OE setlan 'to place, seat'. OE sǣt 'ambush, seat' / ON sæti (< lengthened *sēd-yo-, with the collective prefix *ge-) gave ME sete > seat. OE sadol 'saddle' < Gmc. *sadulaz < o-grade *sod-(dh)lo-; Pokorny suspects it may be an eastern IE loan into Germanic (cf. OCS sedlo), but the root is the same. nest is the compound *ni-sd-o- 'place to sit down' (*ni 'down' + zero grade *sd- of *sed-), OE nest, exactly the 'compound root nizdo-' Watkins cross-refers to under sed-1.\",\n    \"derivation_fa\": \"هر شش واژه میراث مستقیم ژرمنی‌اند: انگلیسی کهن sittan «نشستن»، settan «نشاندن» (ستاک سببی با مصوت گo)، setl «نشیمنگاه» ، sǣt/نروژی کهن sæti «جای نشستن» و sadol «زین». واژهٔ nest نیز مرکّب *ni-sd-o- «جای فرونشستن» است: پیشوند *ni «فرود» به علاوهٔ گونهٔ صفر ریشه (*sd-)؛ همین ساخت در سنسکریت nīḍá- و لاتین nīdus دیده می‌شود. ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n    \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; the parent Germanic box cites AHD, whose sed-1 entry lists SIT, SET, SETTLE, SADDLE, SEAT and cross-refers 'See also compound root nizdo-' for NEST.\"}],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 557 (nest) and leaves 748–757 (seat, settle, saddle)\", \"stance\": \"supports\", \"note\": \"s.v. nest: \\\"… ‘place to sit down in’, fr. *ni-, ‘down’, and zero degree of I.-E. base *sed-, ‘to sit’\\\"; s.v. seat: \\\"fr. Teut. base *set-, corresponding to I.-E. *sed-, ‘to sit’. See sit\\\"; s.v. settle: \\\"I.-E. *sedla- is an enlargement of base *sed-, ‘to sit’. See sit, sedentary and cp. saddle and sell.\\\"\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Sit / Settle / Saddle\", \"stance\": \"supports\", \"note\": \"Skeat traces the whole Germanic family to the base SAD/SED 'to sit' (same entry group that gives Cathedral → chair, l.3120: \\\"ἕδρα, a seat, chair, from ἕζομαι (= *sed-yomai), I sit; see Sit\\\").\"}\n    ]},\n\n   {\"id\": 3, \"lang\": \"Greek\", \"words\": \"\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Empty pass-through box for the Greek branch: PIE *sed- gives Gk. ἕζομαι (hézomai) 'I sit' (< *sed-yomai), ἕδρα (hédra) 'seat, chair' (< *sed-rā, with initial s- > h- by the regular Greek change), ἕδος 'seat' and the compound καθέδρα (kathédra) 'seat with a back' (κατά 'down' + ἕδρα).\",\n    \"derivation_fa\": \"خانهٔ خالی واسطه: در یونانی s آغازین هندواروپایی قاعده‌مند به h بدل می‌شود؛ از این‌رو *sed- ← ἕζομαι «می‌نشینم» و ἕδρα «نشیمن، صندلی» (از *sed-rā) و مرکّب καθέδρα «کرسی». ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n    \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 sed-1 §12: 'Suffixed form *sed-rā-, seat, in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR) …'\"}],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.885 (POK_03 leaf 120)\", \"stance\": \"supports\", \"note\": \"\\\"lok. ἐλλά · καθέδρα Hes. == lat. sella (*sed-la) ‚Stuhl, Sessel'\\\" — Pokorny's Greek material for *sed-.\"},\n      {\"src\": \"KLN\", \"where\": \"leaf 150 (cathedra/chair) and leaf 272 (edaphos)\", \"stance\": \"supports\", \"note\": \"\\\"… to ἕζεσθαι, ‘to sit’, fr. Gk. base *sed-, corresponding to I.-E. base *sed-, ‘to sit’, whence L. sedēre, ‘to sit’. See sedentary and cp. cathedra, cathedral. Cp. also chaise…\\\"\"}\n    ]},\n\n   {\"id\": 4, \"lang\": \"English\", \"words\": \"chair\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Greek καθέδρα kathédra 'seat with a back' (κατά 'down' + ἕδρα < *sed-rā) was taken into Latin as cathedra, whence Old French (Anglo-French) chaiere / chaere (with the regular French loss of the intervocalic -d- and palatalisation of ca- > cha-), Middle English chaere, chaiere, chayer > chair. The word thus reaches English through Greek and Latin, as the chart draws it.\",\n    \"derivation_fa\": \"یونانی καθέδρα «کرسی پشتی‌دار» به لاتین cathedra وام رفت، سپس در فرانسوی کهن با افتادن دال میان‌واکه‌ای و کامی‌شدن ca- به cha- به صورت chaiere درآمد و از آنجا وارد انگلیسی میانه شد (chaere > chair). ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n    \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent Greek box cites AHD, which lists CHAIR under sed-1 §12 via Greek hedra/cathedra.\"}],\n    \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Cathedral / choir / Chair (SKT.txt ll.3120–3289)\", \"stance\": \"supports\", \"note\": \"\\\"Low L. cathedra, a throne — Gk. καθέδρα, a seat — Gk. καθ, for κατά, down; and ἕδρα, a seat, chair, from ἕζομαι, I sit; see Sit\\\" and l.3289 \\\"Chair, Chaise; see Cathedral.\\\"\"},\n      {\"src\": \"KLN\", \"where\": \"leaf 150 s.v. chair/cathedra\", \"stance\": \"supports\", \"note\": \"Klein sends chair to cathedra and thence to Gk. base *sed- 'to sit'.\"}\n    ]},\n\n   {\"id\": 5, \"lang\": \"Latin\", \"words\": \"\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Empty pass-through box: Latin sedeō, sedēre 'to sit' (present built on the stative stem *sed-ē-, perfect sēdī < *se-zd-ai), sēdēs 'seat', sessiō 'a sitting' (< *sed-ti-), solium 'throne' (< o-grade *sod-yo-) and the prefixed compounds obses 'hostage', praeses 'president' all continue *sed-.\",\n    \"derivation_fa\": \"خانهٔ خالی واسطه: لاتین sedeō/sedēre «نشستن» (ستاک حالتی *sed-ē-)، sēdēs «نشیمن»، sessiō «نشست» (از *sed-ti-)، solium «تخت» (گونهٔ o) و مرکّب‌های پیشونددار obses و praeses همه دنبالهٔ همین ریشه‌اند. ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/sed-\"],\n    \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 sed-1 §7: 'Form *sed-ē- in Latin sedēre … SEANCE, SEDENTARY, … SESSION, … HOSTAGE, … PRESIDE …'; §11: 'Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL.'\"}],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.884 and p.886 (POK_03 leaves 119, 121)\", \"stance\": \"supports\", \"note\": \"\\\"lat. sedeō, -ere, sedi ‘sitzen’ (Präs. auf Grund des ursprüngl. außerpräs. St. sede-; Perf. aus *se-zd-ai)\\\"; \\\"*sed-ti in … lat. sessiō ‘Sitzung’\\\"; \\\"prae-ses ‘Vorsitzender’\\\".\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.483–484\", \"stance\": \"supports\", \"note\": \"\\\"lat. sedeo, -ere, sedi „sitzen“ … umbr. sersitu „sedeto“\\\" — same Italic material.\"}\n    ]},\n\n   {\"id\": 6, \"lang\": \"English\", \"words\": \"sedan, soil, session, hostage, president\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"session (ME sessioun < OF session < L. sessiōnem, from sess-, ppl. stem of sedēre) and president (< L. praesidēns, pres. ppl. of praesidēre 'to sit before, preside') are straightforward and certain. soil 'ground' is, per Etymonline, a merger of three Old French words, one of which is soeul/sueil 'threshold, area' < Latin solium 'seat' (< *sod-yo-), so the *sed- link is real but only for one strand. hostage is contested: Watkins and Barnhart derive it from OF ostage < hoste 'guest' (L. hospes), while OED and the Century Dictionary derive it from Late Latin obsidaticum ← obses 'hostage' ← ob- + sedēre; Watkins nevertheless lists HOSTAGE under sed-1, which is the authority Nourai cites. sedan is the weak link: Etymonline calls it 'a word of uncertain origin, possibly from a southern Italian dialect derivative of Italian sede \\\"chair\\\" … from Latin sedes', while Skeat flatly says 'Named from Sedan, a town in France' — a derivation OED rejects. So four of five words hold; sedan is only possible.\",\n    \"derivation_fa\": \"session و president بی‌گمان از لاتین sessiō و praesidēns، هر دو از sedēre، آمده‌اند. soil در واقع آمیزهٔ سه واژهٔ فرانسوی کهن است که یکی از آنها (sueil) از لاتین solium «تخت» از همین ریشه است. hostage دو ریشه‌شناسی رقیب دارد (از hospes «میزبان» یا از obses «گروگان» که به sedēre می‌رسد)؛ واتکینز — همان مرجعی که نورایی می‌آورد — آن را زیر sed- آورده است. امّا sedan سست‌ترین حلقه است: اتیموآنلاین ریشهٔ آن را نامعلوم می‌داند و اسکیت آن را به نام شهر Sedan در فرانسه بازمی‌گرداند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n    \"sources\": [\"https://www.etymonline.com/word/sedan\", \"https://www.etymonline.com/word/soil\", \"https://www.etymonline.com/word/hostage\"],\n    \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent Latin box cites AHD, which lists SESSION, HOSTAGE and PRESIDE under sed-1 §7 and SOIL under §11, but does NOT list SEDAN anywhere under sed-.\"}],\n    \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Sedan-chair (SKT.txt l.16781)\", \"stance\": \"contradicts\", \"note\": \"\\\"Sedan-chair. (F.) Named from Sedan, a town in France. Cf. F. sedan, cloth made at Sedan (Littré).\\\" — no *sed- connection at all.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sed-1\", \"stance\": \"partial\", \"note\": \"lists SESSION, HOSTAGE, PRESIDE, SOIL under the root but omits SEDAN.\"}\n    ]}\n  ]\n },\n\n # ---------------- entry 1 : Akkadian Sedu ----------------\n {\n  \"entry\": 1,\n  \"root\": \"Šedŭ\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Akkadian šēdu (𒀀𒆘) 'a (protective) spirit, genius; demon'\",\n  \"note\": \"The word is real and Nourai's own reference is exact: Zimmern, Akkadische Fremdwörter p.69 (AKD:69) has 'akk. šēdu Name eines Dämons : > hebr. šēd, aram. šēdā'. The gloss is only half right: in Assyriology šēdu is primarily the benevolent tutelary spirit (the bull-colossus genius paired with lamassu), and it is in West Semitic that it becomes a malign 'demon'; 'mad person' is not an Akkadian sense at all but is read back from Persian šeydā. The serious problem with the chart is structural: Nourai hangs šāṭān / śāṭān / šayṭān under this root. That is a different word from a different Semitic root (ś-ṭ-n 'to oppose, accuse'), unconnected with š-d; Klein p.1385, Etymonline and Wiktionary all derive Satan/šayṭān from Hebrew śāṭān, not from Akkadian šēdu, and they run the borrowing in the opposite direction (Hebrew → Aramaic/Syriac/Arabic). The šēdā → Persian šeydā branch, by contrast, is fully confirmed.\",\n  \"note_fa\": \"ریشه واقعی است: اکدی šēdu نام یک روح/عفریت است و زیمرن در صفحهٔ ۶۹ همین را آورده (همان صفحه‌ای که معین نیز در حاشیهٔ برهان قاطع ص ۱۳۲۰ بدان ارجاع داده است). امّا در آشورشناسی šēdu بیشتر «روح نگهبان» است و معنای «دیو» در سامی غربی پدید آمده؛ «دیوانه» هم معنای فارسی «شیدا» است که نورایی به ریشه بازگردانده است. ایراد اصلی آن است که نورایی «شیطان» را نیز زیر همین ریشه آورده؛ حال آنکه آن از ریشهٔ سامی دیگری (ś-ṭ-n «دشمنی کردن، اتهام زدن») است. شاخهٔ شیدا درست و شاخهٔ شیطان/Satan مردود است.\",\n  \"sources\": [W + \"%D8%B4%DB%8C%D8%AF%D8%A7\", W + \"%D7%A9%D7%93\"],\n  \"ref_check\": [\n    {\"ref\": \"AKD:69\", \"status\": \"supports\", \"note\": \"AKD.txt leaf 79 (= printed p.69, the leaf carries the running numbers 69 and 70): \\\"akk. šeđu Name eines Dämons : > hebr. šed, aram. šedā.\\\" Zimmern says nothing there about šāṭān / šayṭān — that part of the chart is not covered by AKD:69.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol. 3 p.1320, Mo'in's footnote 4 (= PDF p.111 of BQT_v3; image saved as refs/ocr/BQT/1320.png)\", \"stance\": \"supports\", \"note\": \"\\\"۴ - از آرامی واردشده … در زبان اکدی shedu (نام عفریتی)، در عبری shed، در آرامی shêdâ (دیو). H. Zimmern, Akkadische Fremdwörter. Leipzig 1917. s. 69.\\\" Mo'in is Nourai's source and cites the same Zimmern page.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.26 s.v. dew\", \"stance\": \"supports\", \"note\": \"\\\"dew [SDYA < A šydʾ, pl. šydyʾ | N -] demon, devil\\\" — the Aramaic word šēdā was in fact the heterogram used by Pahlavi scribes to write dēw, proof of how current it was in Iranian scribal practice.\"}\n  ],\n  \"nodes\": [\n   {\"id\": 1, \"lang\": \"Aramaic\", \"words\": \"šĕdâ, šâtân\", \"verdict\": \"disputed\",\n    \"derivation\": \"Two unrelated words are put in one box. (a) Aramaic/Syriac שידא / ܐܢܕܐܓ šēḏā 'demon' is genuinely a loan from Akkadian šēdu: Zimmern (p.69) and Wiktionary both derive it that way, and Middle Persian scribes used the Aramaic spelling SDYA as the heterogram for dēw 'demon' — so the arrow ROOT → šēdā is correct. (b) Aramaic/Syriac ساطانا sāṭānā 'adversary, Satan' is NOT from šēdu: it belongs to the Semitic root ś-ṭ-n 'to be hostile, accuse'; Klein p.1385 says outright 'Aram.-Syr. sāṭānā, Arab. shayṭān … are loan words from Heb. śāṭān', i.e. the Aramaic form is itself a borrowing, and from the other direction. šēdā has d, šāṭān has emphatic ṭ plus a final -n — no sound change links them. Because the worse word governs, the node is disputed.\",\n    \"derivation_fa\": \"در یک خانه دو واژهٔ بی‌ربط کنار هم نشسته‌اند. آرامی šēḏā «دیو» واقعاً وام‌واژهٔ اکدی šēdu است و همین صورت آرامی در فارسی میانه هوزوارش (SDYA) برای نوشتن dēw به کار می‌رفته است. امّا سریانی sāṭānā از ریشهٔ سامی ś-ṭ-n «دشمنی کردن» است و به گفتهٔ کلاین (ص ۱۳۸۵) خود وام‌گرفته از عبری است؛ میان d در šēḏā و ṭ در sāṭānā هیچ دگرگونی آوایی رابطه برقرار نمی‌کند. پس نیمی از این خانه درست و نیمی رد می‌شود.\",\n    \"sources\": [W + \"%D8%B4%DB%8C%D8%AF%D8%A7\", W + \"%D7%A9%D7%98%D7%9F\"],\n    \"ref_check\": [{\"ref\": \"BQT:1320\", \"status\": \"partial\", \"note\": \"Mo'in's footnote 4 (image refs/ocr/BQT/1320.png) gives \\\"در آرامی shêdâ (دیو)\\\" from Akkadian shedu — supports the šēdā half. The same footnote then adds \\\"shêdâ (شیطان، دیو)، عربی شیطان (جمع شیاطین)\\\"; that equation is Mo'in's, and it is what Nourai copied, but it is not accepted today.\"}],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1385 s.v. Satan (KLN_1966 leaf 736)\", \"stance\": \"contradicts\", \"note\": \"\\\"Aram.-Syr. sāṭānā, Arab. shayṭān, ‘adversary, Satan’, are loan words from Heb. śāṭān.\\\" The Aramaic form is a borrowing FROM Hebrew, not a source, and has nothing to do with Akkadian šēdu.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt, grep ‘satān’, ‘šēdā’)\", \"stance\": \"silent\", \"note\": \"no entry for šēdā or šayṭān was found in the searchable text (the only hit for 'Satan' is an unrelated passage on the Acta S. Pelagiae, l.9336).\"}\n    ]},\n\n   {\"id\": 2, \"lang\": \"Persian\", \"words\": \"šeydâ «شیدا»\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Persian شیدا šeydā 'mad, distracted, madly in love' is a borrowing of Aramaic/Syriac šēḏā 'demon' with the Aramaic determinate ending -ā taken over unchanged; the Aramaic ē is rendered by Persian ey (Classical /šaj.ˈdaː/). The semantic step is the standard 'demon-possessed' → 'mad' one, exactly parallel to Persian دیوانه dīwāna (from dēw 'demon') and Arabic مجنون majnūn (from jinn); in Sufi poetry it narrows further to 'frenzied with love', which is the sense in the Mowlavi couplet the book quotes. Wiktionary gives the same chain, and Mo'in's footnote in Borhan-e Qate' p.1320 (repeated verbatim by Dehkhoda) is its source.\",\n    \"derivation_fa\": \"«شیدا» وام‌واژه‌ای است از آرامی/سریانی šēḏā «دیو»، با همان پایانهٔ معرفهٔ آرامی -ā؛ ای کشیدهٔ آرامی در فارسی به ey بدل شده است. تحول معنایی آن «دیوزده ← دیوانه ← شیفتهٔ عشق» است، دقیقاً همانند «دیوانه» (از dēw) و عربی «مجنون» (از جنّ). معین در حاشیهٔ برهان قاطع (ص ۱۳۲۰) و دهخدا به نقل از او، و همچنین ویکی‌واژه، همین را می‌گویند. ادعای نورایی درست است.\",\n    \"sources\": [W + \"%D8%B4%DB%8C%D8%AF%D8%A7\", \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%AF%D8%A7/\"],\n    \"ref_check\": [{\"ref\": \"BQT:1320\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p.1320 headword \\\"شیدا ۴ – بفتح اول بروزن پیدا، بمعنی دیوانه ولایعقل باشد\\\", with Mo'in's footnote 4 \\\"از آرامی واردشده … در آرامی shêdâ (دیو)\\\" — precisely the arrow drawn. Page image saved at refs/ocr/BQT/1320.png.\"}],\n    \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in entry شیدا on abadis.ir\", \"stance\": \"supports\", \"note\": \"\\\"شیدا. [ ش َ / ش ِ ] (ص) در زبان اکدی «شدو». نام عفریتی است. در عبری «شد» و در آرامی «شدا» به معنی دیو است … (از حاشیه برهان چ معین)\\\" — with citations from Daqiqi, Ferdowsi, Farrokhi, Naser Khosrow.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (grep ‘šēdā’, ‘schêda’, ‘Dämon’)\", \"stance\": \"silent\", \"note\": \"Horn has no entry for شیدا; his Dämon entries are no. 598 dev 'Dämon, Teufel' (< Av. daēva-) and būsāsp, neither relevant.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.26 s.v. dew\", \"stance\": \"partial\", \"note\": \"\\\"dew [SDYA …] demon, devil\\\"; \\\"dewanag [dywʾynk] demonic, mad\\\" — attests both the Aramaic word in Iranian use and the very semantic shift 'demonic' > 'mad' that šeydā shows.\"}\n    ]},\n\n   {\"id\": 3, \"lang\": \"Arabic\", \"words\": \"šeytân\", \"verdict\": \"disputed\",\n    \"derivation\": \"Arabic شيطان šayṭān cannot come from Aramaic šēdā: the consonants do not match (d vs. emphatic ṭ) and the -ān is unexplained. Modern scholarship offers two accounts, neither of them Nourai's. (i) It is a native Arabic formation from the root ش ي ط š-y-ṭ 'to burn, be consumed' with the adjectival suffix -ān — Jeffery (FVQ pp.188–190) documents the pre-Islamic use of šayṭān as a personal and tribal name and as a word for 'snake', and van Vloten and Goldziher take it for an old Arabic word. (ii) The theological sense, and possibly the form, come from the Jewish-Christian environment: Rabbinic שטן, Greek Σατανᾶς, Syriac sāṭānā, or (Nöldeke, Ahrens, Rudolph) Ge'ez ၕየጠን śayṭān; Klein p.1385 simply calls Arab. shayṭān a loan from Hebrew śāṭān. If one keeps only Nourai's drawn arrow 'Aramaic → Arabic' it is defensible for the form sāṭānā, but the ultimate ancestor is the root ś-ṭ-n, never Akkadian šēdu.\",\n    \"derivation_fa\": \"عربی «شیطان» نمی‌تواند از آرامی šēḏā آمده باشد؛ نه دال/طا با هم می‌خوانند و نه پسوند -ān توجیه می‌شود. پژوهش امروزی دو راه می‌نماید: یا ساختهٔ بومی عربی از ریشهٔ ش‌ی‌ط «سوختن» (جفری در واژگان دخیل قرآن، ص ۱۸۸–۱۹۰، همراه با کاربرد پیشااسلامی آن به معنای «مار» و نام قبیله)؛ یا وام‌گیری از عبری/سریانی/حبشی (نولدکه و کلاین). پس تیر «آرامی ← عربی» فقط برای صورت sāṭānā پذیرفتنی است و بازبردن آن به اکدی šēdu مردود است.\",\n    \"sources\": [W + \"%D8%B4%D9%8A%D8%B7%D8%A7%D9%86\", \"https://www.etymonline.com/word/Satan\"],\n    \"ref_check\": [{\"ref\": \"BQT:1320\", \"status\": \"partial\", \"note\": \"Mo'in's footnote 4 does write \\\"shêdâ (شیطان، دیو)، عربی شیطان (جمع شیاطین)\\\" on the same page, so Nourai reproduces his source faithfully; but the reference is a 1963 Persian footnote, not a Semitist's judgement, and it conflates two roots.\"}],\n    \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an pp.188–190 (FVQ_pages.txt ll.6880–6945)\", \"stance\": \"contradicts\", \"note\": \"\\\"we learn from the Lexicons that Shaiṭān has the meaning of snake … van Vloten and Goldziher take شيطان to be an old Arabic word … the theological connotations of Shaitan as leader of the hosts of evil is obviously derived from Muhammad's Jewish or Christian environments. In the Rabbinic writings שטן is used in this sense, as are the Gk. Σαταν and the Syr. sāṭānā … it is from the Eth. … that many scholars have sought to derive the Ar. شيطان.\\\" No Akkadian šēdu anywhere.\"},\n      {\"src\": \"KLN\", \"where\": \"p.1385 s.v. Satan and s.v. shaitan\", \"stance\": \"contradicts\", \"note\": \"s.v. shaitan: \\\"Arab. shayṭān, a loan word fr. Heb. śāṭān. See Satan.\\\"\"}\n    ]},\n\n   {\"id\": 4, \"lang\": \"Persian\", \"words\": \"šeytân «شیطان»\", \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian شیطان šeyṭān 'devil' is an Arabic loan of the Islamic period, taken over with its Arabic orthography (طـ) and its Arabic broken plural شیاطین šayāṭīn, which is itself used in Persian — the sure sign of a direct Arabic borrowing rather than an inherited word. Persian dictionaries mark it 'ع' (Arabic). The arrow Arabic → Persian is therefore correct whatever one thinks of the Arabic word's own origin.\",\n    \"derivation_fa\": \"«شیطان» در فارسی نو وام‌واژه‌ای عربی از دورهٔ اسلامی است؛ هم رسم‌الخط عربی (ط) را حفظ کرده و هم جمع مکسّر عربی «شیاطین» را با خود آورده است — نشانهٔ قطعی وام‌گیری مستقیم. فرهنگ فارسی معین و دهخدا آن را با نشانهٔ (ع) می‌آورند. این حلقه از زنجیره درست است.\",\n    \"sources\": [\"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%B7%D8%A7%D9%86/\", W + \"%D8%B4%D9%8A%D8%B7%D8%A7%D9%86\"],\n    \"ref_check\": [{\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in's Farhang-e Farsi entry, quoted in the Dehkhoda article on abadis.ir: \\\"شیطان. [ ش َ ] (ع اِ) هر سرکش و نافرمان از مردم و پری و ستور و جز آن. ج، شَیاطین … نافرمان. متمرد. (از فرهنگ فارسی معین)\\\" — marked (ع) = Arabic, exactly as the chart draws it.\"}],\n    \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_pages.txt)\", \"stance\": \"silent\", \"note\": \"شیطان is not listed among Persian loans in Arabic — as expected, since the traffic here runs Arabic → Persian, not the reverse.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vol. 3 p.1320 area\", \"stance\": \"partial\", \"note\": \"the Borhan treats شیطان as the ordinary Arabic word (it appears in the gloss of شید آهرمن \\\"ترجمهٔ نورالشیطان است … آهرمن شیطان را گویند\\\") without claiming Iranian origin.\"}\n    ]},\n\n   {\"id\": 5, \"lang\": \"Hebrew\", \"words\": \"sâtân\", \"verdict\": \"disputed\",\n    \"derivation\": \"The arrow is drawn backwards. Hebrew שָׂטָן śāṭān 'adversary, accuser' is a native formation on the verb שָׂטַן śāṭan 'to be hostile to, accuse', root ś-ṭ-n, and Klein — on the very page Nourai cites, p.1385 — says that it is Hebrew that lent the word out: 'Aram.-Syr. sāṭānā, Arab. shayṭān … are loan words from Heb. śāṭān.' Etymonline and Wiktionary agree. In the Hebrew Bible ha-śāṭān is still a common noun, an office ('the accuser') rather than a name, and it is the Septuagint's rendering by διάβολος / transliteration Σατανᾶς that turns it into a personal name. Hebrew also has a separate שֵׁד šēd 'demon', which IS the Akkadian loan — but that is a different word from śāṭān, and it is not what the chart puts in this box.\",\n    \"derivation_fa\": \"جهت تیر وارونه است. عبری śāṭān «دشمن، مدّعی» ساختهٔ بومی عبری از فعل śāṭan «دشمنی کردن، اتهام زدن» (ریشهٔ ś-ṭ-n) است، و کلاین در همان صفحهٔ ۱۳۸۵ که نورایی بدان ارجاع داده، صریحاً می‌گوید که آرامی‌سریانی و عربی از عبری وام گرفته‌اند، نه برعکس. در عهد عتیق هنوز اسم عام است و ترجمهٔ سبعینیه آن را به نام خاص بدل کرده است. عبری «شد» (šēd) «دیو» هم هست که واقعاً وام‌واژهٔ اکدی است، امّا همان نیست که در این خانه آمده. پژوهش امروزی این حلقه را رد می‌کند.\",\n    \"sources\": [W + \"%D7%A9%D7%98%D7%9F\", \"https://www.etymonline.com/word/Satan\", W + \"%D7%A9%D7%93\"],\n    \"ref_check\": [{\"ref\": \"KLN:1385\", \"status\": \"contradicts\", \"note\": \"The page number is exactly right (KLN_1966 leaf 736, bracketed by the printed numerals 1382 on leaf 734 and 1388 on leaf 737), but the content reverses Nourai's arrow: \\\"Satan, n. — Heb. śāṭān, ‘adversary’, fr. śāṭan, ‘he acted as an adversary of, showed enmity to; he charged, accused’, which is rel. to Aram. siṭan, of s.m. Aram.-Syr. sāṭānā, Arab. shayṭān … are loan words from Heb. śāṭān.\\\"\"}],\n    \"consulted\": [\n      {\"src\": \"AKD\", \"where\": \"Zimmern p.69 (AKD.txt leaf 79)\", \"stance\": \"contradicts\", \"note\": \"Zimmern derives only \\\"hebr. šed, aram. šedā\\\" from akk. šēdu; śāṭān does not appear in his list of Akkadian loanwords at all.\"},\n      {\"src\": \"KLN\", \"where\": \"p.1385 s.v. Satanic / Shaitan\", \"stance\": \"contradicts\", \"note\": \"same entry group; Gk. Σατάν, Σατανᾶς and Late L. Satan, Satanas are called \\\"transliterations of Heb. śāṭān\\\".\"}\n    ]},\n\n   {\"id\": 6, \"lang\": \"English\", \"words\": \"Satan\", \"verdict\": \"confirmed\",\n    \"derivation\": \"The route from Hebrew to English is not in doubt: Hebrew śāṭān → Greek Σατανᾶς / Σατάν (a transliteration in the Septuagint and the New Testament) → Late Latin Satan, Satanas (used in the Vulgate, in the Old Testament only) → Old English Satan, Middle English Satan / Sathanas > Satan. Only the step above this node (Aramaic → Hebrew) is wrong; this arrow itself is right.\",\n    \"derivation_fa\": \"این حلقه بی‌اشکال است: عبری śāṭān ← یونانی Σατανᾶς (آوانویسی در ترجمهٔ سبعینیه و عهد جدید) ← لاتین متأخر Satan/Satanas در وولگات ← انگلیسی کهن Satan. تنها حلقهٔ بالادستی (آرامی ← عبری) نادرست است، نه این یکی.\",\n    \"sources\": [\"https://www.etymonline.com/word/Satan\", W + \"%D7%A9%D7%98%D7%9F\"],\n    \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent Hebrew box cites KLN:1385, which covers this chain: \\\"Cp. Gk. Σατάν, Σατανᾶς, Late L. Satan, Satanas, which are transliterations of Heb. śāṭān.\\\"\"}],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1385 s.v. Satan\", \"stance\": \"supports\", \"note\": \"\\\"Cp. Gk. Σατάν, Σατανᾶς, Late L. Satan, Satanas, which are transliterations of Heb. śāṭān.\\\"\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p.190\", \"stance\": \"supports\", \"note\": \"\\\"In the Rabbinic writings שטן is used in this sense, as are the Gk. Σαταν and the Syr. sāṭānā\\\" — the same Hebrew→Greek transmission.\"}\n    ]}\n  ]\n },\n\n # ---------------- entry 2 : Segh ----------------\n {\n  \"entry\": 2,\n  \"root\": \"Segh\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *seǵʰ- 'to hold (fast), overpower', with the neuter s-stem *seǵʰ-os 'victory, might'\",\n  \"note\": \"Pokorny p.888 — the page Nourai cites — heads the entry exactly: 'segh-, seghi-, seghu- „festhalten, halten; einen im Kampf überwältigen, Sieg‘; seghos- n. „Sieg‘, seghu-ro- „siegreich‘'. Nourai's gloss 'to hold, overrule' is a fair rendering of 'festhalten, halten; … überwältigen'. Watkins gives 'segh-. To hold. [Pok. segh- 888.]' and Wiktionary reconstructs *seǵʰ- 'to overpower, to take hold of'. Every node on this chart is covered by this one Pokorny page.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *seǵʰ- «نگاه داشتن، فروگرفتن، چیره شدن» درست است و پوکورنی در همان صفحهٔ ۸۸۸ که نورایی می‌آورد آن را با همین معنا آورده، همراه با نام خنثای *seǵʰ-os «پیروزی». واتکینز و ویکی‌واژه نیز همین را می‌گویند. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-\"],\n  \"ref_check\": [{\"ref\": \"POK:888\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 123 (= printed p.888, fixed by '889' on leaf 124): \\\"segh-, seghi-, seghu- „festhalten, halten; einen im Kampf überwältigen, Sieg‘; seghos- n. „Sieg‘, seghu-ro- „siegreich‘.\\\"\"}],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.481 (WLD_Bd2_pages.txt l.31924)\", \"stance\": \"supports\", \"note\": \"\\\"segh- „festhalten, halten; einen im Kampf unterlegenen fest gepackt halten, überwältigen, Sieg“.\\\"\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. segh-\", \"stance\": \"supports\", \"note\": \"\\\"segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< ‘a holding or conquest in battle’) … [Pok. segh- 888.]\\\"\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. seghis/seghos, seĝhlos\", \"stance\": \"partial\", \"note\": \"\\\"seghis, see seghos — Ir. sigh, f. ‘peace’; OE cf. sig, sige, n. & m. ‘victory’; MHG sic, gs. siges …\\\" and \\\"seĝhlos (2) ‘hold, grip’\\\" — Mann has the root but scatters it over several entries and does not list the Greek σχ- forms under it.\"}\n  ],\n  \"nodes\": [\n   {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"haz : to gain ; hazah : victory\", \"verdict\": \"plausible\",\n    \"derivation\": \"Both forms are real Avestan and both belong to this root — Indo-Iranian *saǵʰ- regularly gives Avestan haz- (PIE *s > Ir. h before a vowel, *ǵʰ > z). Bartholomae cols. 1795–1796 s.v. haz- 'sich bemächtigen': (1) 'sich bemächtigen, in seinen Besitz bringen, gewinnen', (2) absolutely 'im Kampf gewinnen, den Sieg davontragen' — so 'to gain' is exact. The gloss on hazah- is off, though: Bartholomae cols. 1799–1800 gives hazah- n. as (1) 'Gewalt, Macht', (2) 'Gewalt, Gewalttat', (3) 'gewaltsame Wegnahme, Raub', and both Pokorny p.888 and Walde-Pokorny II 481 render it 'Gewalt(tat), Raub'. It is the Sanskrit cognate sáhas- that means 'Gewalt, Sieg'; Avestan hazah- had gone over to the pejorative 'violence, plunder'. So the derivation is confirmed and only the English gloss 'victory' is imported from Sanskrit.\",\n    \"derivation_fa\": \"هر دو صورت اوستایی اند و از همین ریشه‌اند: در ایرانی باستان s آغازین پیشاز واکه به h و *ǵʰ به z بدل می‌شود؛ پس *saǵʰ- ← haz-. بارتولومه (ستون ۱۷۹۵) haz- را «دست یافتن، به دست آوردن» و در کاربرد مطلق «در نبرد پیروز شدن» معنا کرده — پس to gain درست است. امّا hazah- نزد بارتولومه (ستون ۱۷۹۹) «زور، قدرت، ستم، غارت» است نه «پیروزی»؛ معنای «پیروزی» از هم‌ریشهٔ سنسکریت sáhas- آمده است. بنابراین پیوند درست و فقط معنای دوم دقیق نیست.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-\"],\n    \"ref_check\": [{\"ref\": \"POK:888\", \"status\": \"partial\", \"note\": \"POK p.888 has both words but glosses the noun differently: \\\"ai. sáhas- n. ‚Gewalt, Sieg' == av. hazah- n. ‚Gewalt(tat), Raub'\\\", and \\\"av. h[az-] ‚sich bemächtigen, erwerben'\\\". The verb matches Nourai's 'to gain'; the noun is 'violence, plunder', not 'victory'.\"}],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae cols. 1795–1796 (haz-) and 1799–1800 (hazah-), BRT.txt leaves 974 and 976\", \"stance\": \"partial\", \"note\": \"\\\"haz- V. ‘sich bemächtigen’ … 1) ‘sich bemächtigen, in seinen Besitz bringen, gewinnen’ … 2) absolut ‘im Kampf gewinnen, den Sieg davontragen’\\\"; but \\\"hazah- n. 1) ‘Gewalt, Macht’ … 2) ‘Gewalt, Gewalttat’ … 3) ‘gewaltsame Wegnahme, Raub’\\\" — no 'victory'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.481\", \"stance\": \"partial\", \"note\": \"\\\"Ai. sáhate „bewältigt, vermag, erträgt“, sáhas- n. „Gewalt, Sieg“ = av. hazah- n. „Gewalttat, Raub“ … av. haz- „sich bemächtigen, erwerben“.\\\"\"}\n    ]},\n\n   {\"id\": 2, \"lang\": \"Greek\", \"words\": \"sxĕma : a holding, form, shape ; sxolĕ : a holding back, stop, rest\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Both are zero-grade *sǵʰ- formations to ἔχω ékhō 'I hold' (< *seǵʰ-ō): σχῆμα skhḗma 'a holding, bearing, form, figure' is the -μα action-noun to the aorist stem σχ- (cf. ἔσχον), and σχολή skholḗ 'a holding back, halt, rest, leisure' is built on the same stem with -ολή (on the model of βολή, στολή). Pokorny prints both under segh- with these very glosses, and the semantic development of σχολή 'leisure' > 'learned discussion' > 'place of lectures' is the well-documented Athenian one.\",\n    \"derivation_fa\": \"هر دو واژه از گونهٔ صفر ریشه (*sǵʰ-) ساخته شده‌اند، هم‌ریشه با ἔχω «دارم، نگاه می‌دارم»: σχῆμα «نگاه‌داشت، هیئت، شکل» با پسوند -μα بر ستاک ماضی σχ-، و σχολή «بازایستادن، آسایش، فراغت» بر قیاس βολή و στολή. پوکورنی در صفحهٔ ۸۸۸ هر دو را با همین معناها زیر segh- آورده است. ادعای نورایی درست است.\",\n    \"sources\": [W + \"Reconstruction:Proto-Indo-European/seg%CC%81%CA%B0-\", \"https://www.etymonline.com/word/school\"],\n    \"ref_check\": [\n      {\"ref\": \"POK:888\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 123: \\\"schwundstufig: ἴσχω (*si-zgh-ō) ‚halte an, habe' … σχῆμα ‚Haltung, Gestalt, Form'. σχολή ‚Einhalten, Ruhe, Muße; (wissenschaftliche) Beschäftigung in Mußestunden'.\\\" Word for word Nourai's two glosses.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 segh- §4: \\\"Zero-grade form *sgh- in: a. Greek skhēma, ‘a holding’, form, figure: SCHEME; b. Greek skholē, ‘a holding back’, stop, rest, leisure, employment of leisure in disputation, school.\\\"\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.481–482\", \"stance\": \"supports\", \"note\": \"\\\"Gr. ἔχω (εἶχον, ἔσχον, ἔσχηκα, ἕξω und σχήσω) „halten, besitzen, haben“ … ἕξις „Verhalten, Befinden“\\\" — the same Greek family.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Scheme (SKT.txt l.16614)\", \"stance\": \"supports\", \"note\": \"\\\"Scheme. (L. — Gk.) Formerly schema. – L. schema. – Gk. σχῆμα, form, appearance … Gk. σχήσω, fut. of ἔχω, to hold, have (base σεχ-). Cf. Skt. sah, to bear. (√SAGH.)\\\"\"}\n    ]},\n\n   {\"id\": 3, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n    \"derivation\": \"An empty pass-through box, correctly placed as a child of Greek rather than of the root: Latin has no inherited reflex of *seǵʰ-, it simply took the two Greek nouns over as learned loans — schema, -atis 'figure, shape' (Cicero, Quintilian) and schola 'leisure for learning, lecture-place, school' (with the Greek -ολή rendered -ola), whence also scholaris, scholasticus. Latin schola was then borrowed on into Old English (scol) and all over Europe (OF escole, OHG scuola, Welsh ysgol, Russian shkola).\",\n    \"derivation_fa\": \"خانهٔ خالی واسطه، و به درستی فرزند یونانی است نه فرزند ریشه: لاتین از این ریشه میراث مستقیمی ندارد و هر دو واژه را وام گرفته است: schema «هیئت» و schola «فراغت درس، مدرسه». همین schola سپس به انگلیسی کهن (scol) و سراسر اروپا راه یافت. ادعای نورایی درست است.\",\n    \"sources\": [\"https://www.etymonline.com/word/school\"],\n    \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference; the claim is covered by the AHD citation on the child English box and by Etymonline s.v. school.\"}],\n    \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Scheme and Sketch\", \"stance\": \"supports\", \"note\": \"Skeat routes both words through Latin: \\\"Scheme … (L. — Gk.) … L. schema — Gk. σχῆμα\\\"; \\\"Sketch. (Du. — Ital. — L. — Gk.)\\\".\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. school, scholar\", \"stance\": \"supports\", \"note\": \"Klein derives school from OE scol, fr. L. schola, fr. Gk. σχολή, and scholar from Late L. scholaris.\"}\n    ]},\n\n   {\"id\": 4, \"lang\": \"English\", \"words\": \"scheme, sketch ; school, scholar\", \"verdict\": \"plausible\",\n    \"derivation\": \"scheme is a direct 16th-c. learned borrowing of Latin schema (< σχῆμα), first in the rhetorical sense 'figure of speech'. school is OE scol < L. schola < σχολή, and scholar is OE scolere / ME scoler < Late Latin scholaris 'of a school' — both certain. sketch is the one open question: the chain Dutch schets / Low German skizze ← Italian schizzo (17th-c. artists' jargon) is agreed, but the origin of Italian schizzo is not. The older view (OED, Skeat, Klein) derives it from Latin *schedius / schedium 'a thing made hastily', from Greek σχέδιος 'extempore', which is indeed built to σχεδόν 'near' from the same σχ-/*seǵʰ- stem; Barnhart instead takes schizzo as a special use of schizzo 'a splash, squirt' (schizzare 'to splash'), of unknown origin. Three of four words are confirmed, so the node is plausible rather than confirmed.\",\n    \"derivation_fa\": \"scheme وام‌واژهٔ عالمانهٔ سدهٔ شانزدهم از لاتین schema است؛ school از انگلیسی کهن scol از لاتین schola و scholar از لاتین متأخر scholaris — هر سه قطعی. تنها sketch محل بحث است: مسیر هلندی schets ← ایتالیایی schizzo پذیرفته است، امّا دربارهٔ سرچشمهٔ schizzo دو رأی هست: یا از لاتین schedium از یونانی σχέδιος (هم‌ریشه با σχήμα) یا از schizzare «پاشیدن» که ریشه‌اش ناروشن است. پس ادعای نورایی در کل با احتیاط پذیرفتنی است.\",\n    \"sources\": [\"https://www.etymonline.com/word/sketch\", \"https://www.etymonline.com/word/school\"],\n    \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 segh- §4 lists SCHEME, (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL under the root — but not SKETCH, which Watkins does not place here.\"}],\n    \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Sketch (SKT.txt l.17381)\", \"stance\": \"supports\", \"note\": \"\\\"Sketch. (Du. – Ital. – L. – Gk.) Du. schets, a draught, sketch. – Ital. schizzo, a first rough draught. – L. schedium, a thing made hastily; from schedius, adj., hastily made. – Gk. σχέδιος, sudden; allied to σχεδόν, near; from the base σεχ-, to hold. Allied to Scheme.\\\" — exactly Nourai's grouping.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. scheme, school, scholar\", \"stance\": \"supports\", \"note\": \"Klein takes scheme from L. schema < Gk. σχῆμα (to ἔχειν), school from L. schola < Gk. σχολή, scholar from Late L. scholaris.\"}\n    ]}\n  ]\n }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-436.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write436.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-436.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T01:42:14.782Z] TOOL RESULT

```
ok
JSON OK
```


## [2026-09-14T01:42:18.446Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 tools/verify_check.py 436"
}
```


### [2026-09-14T01:42:19.427Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'plausible': 3, 'disputed': 3}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 7, 'not_checked': 5, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 19, 'contradicts': 6, 'partial': 5, 'silent': 3} | by book: {'KLN': 9, 'SKT': 6, 'WLD': 4, 'POK': 3, 'FVQ': 2, 'AHD': 1, 'AFA': 1, 'MON': 1, 'HRN': 1, 'PHD': 1, 'PLA': 1, 'BQT': 1, 'AKD': 1, 'BRT': 1}
```


## [2026-09-14T01:42:39.976Z] AGENT

Done. `python3 tools/verify_check.py 436` reports **0 PROBLEM lines** (16/16 nodes verified).

**Page 436 (book p. 406) — 3 entries, 16 nodes**

Verdicts: nodes — 10 confirmed, 3 plausible, 3 disputed; roots — 2 confirmed (Sed, Segh), 1 plausible (Akkadian Šedŭ).
Ref checks: 7 supports, 4 partial, 1 contradicts, 5 not_checked (nodes with `refs=None`).

**Disputed**
- *Šedŭ* / Aramaic `šĕdâ, šâtân` (node 1) — two unrelated words in one box. `šēdā` "demon" really is the Akkadian loan (Zimmern AKD:69 verbatim), but `šāṭān` is from Semitic ś-ṭ-n; no sound change links d ~ ṭ+n.
- *Šedŭ* / Arabic `šeytân` (node 3) — Jeffery (FVQ 188–190) and Klein derive it from the root š-y-ṭ or from Hebrew/Syriac/Ge'ez, never from Akkadian *šēdu*.
- *Šedŭ* / Hebrew `sâtân` (node 5) — **arrow reversed**: Klein p.1385, the page Nourai himself cites, says "Aram.-Syr. sāṭānā, Arab. shayṭān … are loan words from Heb. śāṭān".

**Plausible**
- *Sed* / English `sedan, soil, session, hostage, president` — `sedan` is of uncertain origin (Skeat: from the town Sedan) and is absent from Watkins' *sed-*; `hostage` has two competing etymologies.
- *Segh* / Avestan `hazah` — Bartholomae cols. 1799–1800 and Pokorny 888 gloss it 'Gewalt(tat), Raub', not "victory" (that is the Sanskrit cognate *sáhas-*); `haz-` "to gain" is exact.
- *Segh* / English `scheme, sketch; school, scholar` — `sketch` disputed (Skeat/OED via Gk. σχέδιος vs. Barnhart via Ital. *schizzare* "splash").

**Transcription flags / extraction errors: none.** I rendered PDF p.436; the JSON matches the printed chart word for word. One cosmetic note for the owner: in the Segh chart the Avestan box has an arrow into a completely blank box (no language label, no words) that the extraction omits — it carries no content, so nothing is lost.

**Notably good citations:** POK:884/887 and KLN:1075 are both exactly right, and Klein p.1075 s.v. *odograph* is verbatim the source of Nourai's double gloss. BQT:1320 is exact (Mo'in's footnote 4, which itself cites Zimmern p.69 = Nourai's AKD:69); the page image is at `data/verification/sources/refs/ocr/BQT/1320.png`. MacKenzie's Pahlavi heterogram `dew [SDYA]` independently attests Aramaic *šēdā* in Iranian use.
