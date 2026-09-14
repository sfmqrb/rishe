# Verification process log — verify-page-480


## [2026-09-14T03:08:10.285Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 480 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-480.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-480.json. Write /home/sfmqrb/git/rishe/data/verification/page-480.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 480` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:11.272Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:12.156Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:12.172Z] TOOL RESULT

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


## [2026-09-14T03:08:12.658Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-480.txt"
}
```


### [2026-09-14T03:08:12.694Z] TOOL RESULT

```
1	=== PDF page 480 (book page 450) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ster 2 : star  (refs POK:1027)
4	#1 (parent #0) [Avestan] refs=POK:1027 | star 2
5	  #2 (parent #1) [Persian] refs=AHD | setâreh «ستاره» : star | NOTE: IEC:260 derives "setâreh" and "axtar" from the same root. See "Apânak".
6	#3 (parent #0) [Germanic] refs=AHD | sterron : star
7	  #4 (parent #3) [English] refs=None | star
8	#5 (parent #0) [Greek] refs=AHD:81 | aster ; aster-lambanein : taking (measuring) stars
9	  #6 (parent #5) [Persian] refs=MON:248; ETM:45 | ostorlâb «استرلاب» : astrolabe | extra: اسطرلاب
10	  #7 (parent #5) [English] refs=AHD | asterisk ; astrolabe ; disaster
11	#8 (parent #0) [Latin] refs=AHD | sterron : star
12	  #9 (parent #8) [English] refs=None | constellation
13	--- entry 1 ---
14	ROOT [Indo-European] Ster 3, Sterp : stiff  (refs POK:1022)
15	#1 (parent #0) [Pahlavi] refs=HRN:86 | turuš : sour (stiff) taste
16	  #2 (parent #1) [Persian] refs=POK:1022; BQT:485 | toroš, torš «تُرش» : sour | extra: تُرشا ، تُرشی
17	#3 (parent #0) [Latin] refs=AHD | torpere : to be stiff
18	  #4 (parent #3) [English] refs=None | torpedo
19	#5 (parent #0) [Germanic] refs=AHD | sterk : to move stiffly ; staren : to look with stiff eyes (stare) ; strŭt : to stand firm ; starkjan : to stiffen ; sterben : to become rigid (die)
20	  #6 (parent #5) [English] refs=None | start ; stare ; strut ; starch ; starve
21	    #7 (parent #6) [Persian] refs=MON:238 | estârt «استارت» : start
22	#8 (parent #0) [Greek] refs=AHD | steros : solid
23	  #9 (parent #8) [English] refs=AHD | stereo ; cholesterol
24	    #10 (parent #9) [Persian] refs=None | esterîyo «اِستریو» : "solid, three dimensional" ; kolestrol «کلسترول» : "hard gall, first found in gallstones"
25	
```


## [2026-09-14T03:08:15.782Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-480.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read page JSON and source matrix"
}
```


### [2026-09-14T03:08:15.839Z] TOOL RESULT

```
{
  "pdf_page": 480,
  "book_page": 450,
  "entries": [
    {
      "root": {
        "name": "Ster 2",
        "lang": "Indo-European",
        "refs": "POK:1027",
        "gloss": "star"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1027",
          "words": [
            {"translit": "star 2", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AHD",
          "words": [
            {"translit": "setâreh", "gloss": "star", "script": "ستاره"}
          ],
          "note": "IEC:260 derives \"setâreh\" and \"axtar\" from the same root. See \"Apânak\".",
          "quote": {
            "text": "چون ستاره با دو بال زر نشان - آمده از دور دست آسمان",
            "poet": "Farrokhzâd"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sterron", "gloss": "star", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "star", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:81",
          "words": [
            {"translit": "aster", "gloss": null, "script": null},
            {"translit": "aster-lambanein", "gloss": "taking (measuring) stars", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:248; ETM:45",
          "words": [
            {"translit": "ostorlâb", "gloss": "astrolabe", "script": "استرلاب"}
          ],
          "script_extra": "اسطرلاب",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "asterisk", "gloss": null, "script": null},
            {"translit": "astrolabe", "gloss": null, "script": null},
            {"translit": "disaster", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sterron", "gloss": "star", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "constellation", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ster 3, Sterp",
        "lang": "Indo-European",
        "refs": "POK:1022",
        "gloss": "stiff"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:86",
          "words": [
            {"translit": "turuš", "gloss": "sour (stiff) taste", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:1022; BQT:485",
          "words": [
            {"translit": "toroš, torš", "gloss": "sour", "script": "تُرش"}
          ],
          "script_extra": "تُرشا ، تُرشی",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "torpere", "gloss": "to be stiff", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "torpedo", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sterk", "gloss": "to move stiffly", "script": null},
            {"translit": "staren", "gloss": "to look with stiff eyes (stare)", "script": null},
            {"translit": "strŭt", "gloss": "to stand firm", "script": null},
            {"translit": "starkjan", "gloss": "to stiffen", "script": null},
            {"translit": "sterben", "gloss": "to become rigid (die)", "script": null}
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
            {"translit": "start", "gloss": null, "script": null},
            {"translit": "stare", "gloss": null, "script": null},
            {"translit": "strut", "gloss": null, "script": null},
            {"translit": "starch", "gloss": null, "script": null},
            {"translit": "starve", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:238",
          "words": [
            {"translit": "estârt", "gloss": "start", "script": "استارت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "steros", "gloss": "solid", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stereo", "gloss": null, "script": null},
            {"translit": "cholesterol", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "esterîyo", "gloss": "\"solid, three dimensional\"", "script": "اِستریو"},
            {"translit": "kolestrol", "gloss": "\"hard gall, first found in gallstones\"", "script": "کلسترول"}
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:08:20.264Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','HRN','BQT','MON','ETM','IEC','KLN','WLD','SYN','SKT','LEW','LAT','BRT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-14T03:08:21.339Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-14T03:08:26.000Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---AHD---'); print(d['AHD'].get('page_offset')); print(d['AHD'].get('lookup_hint'))\nprint('---HRN---'); print(d['HRN'].get('lookup_hint'))\nprint('---BQT---'); print(d['BQT'].get('page_offset')); print(d['BQT'].get('lookup_hint'))\nprint('---MON---'); print(d['MON'].get('page_offset'))\n\""
}
```


### [2026-09-14T03:08:27.057Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---AHD---
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
---HRN---
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---BQT---
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
---MON---
None
```


## [2026-09-14T03:08:29.993Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ster\" POK_full.txt | head -40"
}
```


### [2026-09-14T03:08:30.052Z] TOOL RESULT

```
81998:Root / lemma: sterg-, sterk- 
82496:Root / lemma: ster-3 
82508:Root / lemma: ster-4 
82599:Root / lemma: ster-5, stera- : stre-, steru- : streu- 
82687:Root / lemma: ster-6 
83007:Root / lemma: ster-2
```


## [2026-09-14T03:08:32.108Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82480,82620p;82980,83040p' POK_full.txt"
}
```


### [2026-09-14T03:08:32.175Z] TOOL RESULT

```
Old Icelandic 
stf{/) up/" throat, gullet ', Norwegian sZ/iOyO "narrow aperture '; 



Lithuanian strubas, Latvian 5//'i/(/77)/7s "short abgestutzt', strubikis, 

strupikis, s/mp5s//s "Stumpfschwanz', Latvian s/myO^/zs "kurzer thick 

person; piece wood, clot, chunk'. Old Lithuanian strupas^ decrepit, antiquated man'. 

References: WP. II 627 ff., WH. II 595, 601 f., 606 f., 692, Trautmann 284 f., 325, Vasmer 
3, 98f., 126. 
Page(s): 1022-1027 

Root / lemma: ster-3 

Meaning: to rob, steal 

Material: Gr. GTspsu) (Attic OTspiaKU) only present) "rob', aT£po|jai "bin stolen; looted, miss'; 

Middle Irish serb^ theft ' ( *ster-ua); with /instead of rthrough hybridization with hehlen: 
Gothic stilan. Old Icelandic stela. Old English Old High German stelan^steaW 

References: WP. II 636. 
Page(s):1028 

Root / lemma: ster-4 



Meaning: line, stripe, ray 

Note: also stere-. stre- strei-, streu-, with g, b, d^ (or /) extended; identical with ster- 

"outspread' 

Material: Old High German stra{a) 'arrow, lightning ', Modern High German Strahl, Old 

Saxon stralai. 'arrow'. Middle Low German s/A^/e 'arrow, ray, sting, prick'. Old English 

strseli. ^arro\N, lance ', Norwegian straars'cnaW Fischschwarm', East Frisians/Aa/'stripe', 

Old Saxon sfra/m., Middle High German strsel {*strelia-) 'comb' (from den teeth = 

Strahlen), whereof Old High German stralen. Modern High German strah/en^ comb'; 

Norwegian sfn/, s//775 'stripe, vein, ray', Swedish 5//7/ 'small Wasserstrahl', 5/77/5' trickle ', 

Old Church Slavic s/zie/a 'arrow'; 

Middle High German s//'5/77'Lichtstreifen, ray, stream'. Modern High German dial, sfram 
'stripe'; to strek Old High German strTmo, Modern High German dial, streimen. Middle 
Low German s//w7e 'stripe, Strieme, ray'; to * streu- perhaps: Middle High German mnl. 
strieme. Middle Low German s/Ae/r?© 'stripe, ray' (if from Old High German *striomo). 
Modern High German Striemen^ weals, marks from blows'; 

Old High German streno. Middle High German stren(e)^ Strahne, braid, plait '; to * streu-: 
Lithuanian strun/t/^to build'. Old Church Slavic struna^rope, string '; from the basis *ster-: 
kir. postoronok, poln. postronek, Czech postranek^ cord, rope, string '. 

Latvian (sau/es) 5/5/3 'Sonnenstrahl', s/sas 'bough', stara'rope, stripe'; 

streig-:gr. ^sarpi^ (knid.) 'sechsseitig', whether from ^sa-arpi^; Latin str/ga'Wne, 
Schwade; Zeltreihe; Langsfurche', strigosus 'fragile, flimsy, lean ', stria (probably *strigia) 
'furrow, crease '\stringd, -ere\n the meaning ' strip, wipe, stroke, touch, das sword Ziehen', 
str/g/7/s' rasper' (out of it Modern High German S//7e^e/' currycomb'); 

Old High German str/hhan ^ stroke' , Old English str/ican^ stroke, rub, sich bewegen, go'; 
Gothic str/ks^\\r\e'. Old High German str/kl\r\e, stripe, Strecke Wegs, line Landes', Old 
English s//7ic5 'stripe'; Old Icelandic s//?]^ 'striped Zeug', Norwegian str/k'\\r\e, Windstrich, 
prank'; Middle Low German s//"e/r 'prank, prank'. Middle High German s/zie/ic/? 'prank, blow, 
knock' {*stra/ka-). Old English strac/an^ stroke', engl. s/zio/re'blow, knock'; 

Old Prussian str/g//'t\r\'\st\e'; Old Church Slavic str/gg, str/st/' shave, shear'; russ. -Church 
Slavic stregb 'Koupa' {*stro/go-= Middle High German Streich); with Swedish streke 
{*strikan-) 'Stromstrich' compare proto Slavic, strtz-: russ. strezent, strez, streza 
'Stromstrich'; 



after Trautmann 290, Vasmer 3, 12 f. here as " center, heart'. Old Prussian strigeno' 
brain '. 

Maybe alb. Geg {*struni) trunT brain '; (common alb. st- > /-) 

proto Slavic. *strbZbnb, respectively *strbzenb " center, marrow ', russ. -Church Slavic 
strbzenb " marrow 'etc. 

streib-. Old Irish s/v^it' "stripe' {*streiba)\ Middle Low German s/A^e "stripe'. Middle High 
German strife. Modern High German Streifen, Norwegian stnpads., Swedish str/pa 
"herabhangender topknot '; Middle Low German mnl. s//77?e/7"(ab)stripe'. Middle High 
German streifen {*straipjan) "stroke, glide, slide, umherstreifen, (ab)ziehen, flay'. Low 
German strepen^ strip, wipe ' 

streug-:gr. OTpEuyofjai "werde weakened, schmachte hin' (Old Irish trog^ woeful, 
wretched, miserable '? see below ter-, treugh- \ub'); Old Icelandic strjuka' stroke, whisk, 
smooth; sich rasch bewegen', strykja, strykva ds., s//y/r"line', strykr^ strong wind'. Old 
High German struchon \uere, impingere'. Middle High Germans/mc/7e/7"straucheln', nl. 
strooken^ caress, iJbereinstimmen with'. East Frisian strdk^S\xe\i, stripe'. Middle Low 
German s/Aa/re/? "stripe, caress' (afrom o). Old English stroccian^ stroke' , Norwegian 
strokk^ plane '; Latvian struga/ns ' stnped ', Lithuanian s//7t/^55 "knife' (poln. loanword); Old 
Church Slavic struzg, strbgat/^ scrape, shave, shear', strugb "tool zum Schaben', russ. 
Strug " plane ' etc. 

Alb. strugb plane, bladed tool used to smooth wood ' Slavic loanword. 

streub- Old High German stroufen. Middle High German stroufen {*straupjan) " strip, 
wipe, mug, rob, pliJndern, umherstreifen' = Middle Low German stropends.. Old English 
be-strfepan ds.. Middle High German striefen {*streupan) "stripe'; Middle High German 
strupfen 'sir'\pe, pick off, remove'. 

streud^ - or streut-: 0\d English strud/an ar\d strucfan ^p\ur\derr\', strycfan^mug, rob'. 
Middle Low German stroden. Old High German strutten ds. 

References: WP. II 636 ff., WH. II 603, 604 f., Trautmann 288 f.; Vasmer 3, 27, 30 ff. 
Page(s): 1028-1029 

Root / lemma: ster-5, stera- : stre-, steru- : streu- 

Meaning: to widen, to scatter 

Note: (compare ster- " stare, stiff sein') 



Material: A. Old Indie strnati, s//77d7/ (actually zur basis streu-), later also staratr s\xe\i\. 
(hin), bestreut; wirft hin, wirft low, base', participle strta-, stTrna-, Inf. s/5/fai/eand staritavai, 
stantave; sva-stara-m. 'eigene Streu', pra-stara-xx\. 'Streu, cushion; surface, plain, area, 
plain ' (= russ. prostor^Rawm, Geraumigkeit'); starT-man-v\. 'Ausbreitung, Ausstreuung' 
(ablaut, with gr. arpajpa, LaWustramen); 

Avestan star- (present starati, staranaoti, staranati) 'sternere', participle sfarafa-an6 
starata-, stain's- v\. 'Streu, lair, bed'; urvard-straya-^H\e6er\\auev\irom Pflanzungen'; 

gr. GTopvufji (only present and Impf.; to vocalism compare oijopyvupi), GTopswOpi 
(neologism), arpcbwupi (after arpwaai) 'bestreue, strecke hin; breite from; level, even ', 
Aeolic Perf. saropoTai; participlearpcjOTOc;; arpajpa n. 'Streu, lair, rug, cover', arpwijvri ds.; 
GTpaTOc; (= Old Indie strta-) 'troop, multitude, crowd, Volksmenge' (Cretan aTapT6(; with 
metathesis 'eine Unterabteilung the Phyle'), then ' army ' (in addition arpaTia, arpaTsia, 

2. steip-, sffp-. Latin stipes, -itisxx\. "picket, pole, stem, shaft, pole', stTpo, -are "dense to 
press together, pile up, collect, accumulate, gedrangt vollstopfen', obsfipus " sideways 
willing, inclined'; 

with I stipulai. " stem, straw'; unclear are stips, st/p/s' currency, gift, Spende'; 
s/!^eA7o'/i//77"Soldatenlohnung, tax, tribute, pay, guerdon, reward ' {*stipi-pendiom), stipulor, 
-^/"/""bedinge mirfrom'; Umbrian steplatu, 5//p/5/c»"stipulat5'; 

gr. PN IfiTTOJv to *aTTno(; = Old English stTf, Middle High German (actually md.) stTF stiff 
erect', besides Old Frisian stef{7); Middle Low German s//Ve'/e"pad', Middle High German 
stTvelAs., Old Icelandic 5//775 "dammen' (out of it engl. 5//>fe "choke; suppress, crush'); with 
Germanic yo: Low German stTpel, s//7?e/'"Stutzholz', Frisian sZ/pe "picket, pole', engl. stipe^ 
stalk'; Middle Low German stip, stippe^ dot, speck, Tupf, 5//p'pe/7"punktieren, prick ', 
Middle High German s/e/0'/0e/7"reihenweise sew, prick ', Modern High German steppen; 
Middle Low German s///? "small nail, peg'. Old High German s/e/?"cusp, peak, thorn, peg\ 
unclear are Old Low German 5////o/7"aedificare', Old High German Middle High German 
s///?e/7"feststellen, grijnden, to build, instigate ', Modern High German stiften; 

Lithuanian stimpu stipti^ solidify, congeal, verenden', s///7Ai/s "strong', PI. sf/p/narpa6 
am sled ', Latvian st/pt' stiff become', ablaut. Lithuanian stiepti, Latvian st/'ept 'recken'; Old 
Prussian post/pp/n'\N\r\o\e'. 

References: WP. II 646 f., WH. II 593 ff., Trautmann 287, Vasmer 3, 7; 
See also: to sta/'-S. 1010. 
Page(s): 1015-1016 

Root / lemma: ster-2 
Meaning: star 
Material: 

In a-grade: 

Hittite: ast/ra- c. 'star?' (Tischler 86), haster- c. (204ff) 

Armenian as//. Gen. as/e/"star, stars'; gr. aarrip, -ipoq "star', collective aarpa " young ' 

aoTpov "star, stars' (out of it Latin astrum), wherefore probably with (u)n-)6n-: (a)aT£ponri, 

darpann "lightning, sheet lightning ', aaT£ponr|Tr|(;, aaTsponaToq " Blitzeschleuderer (Zeus) 



In zero grade: 

In e-grade (internal): 

gr. OTtpoy\) " shimmering ', (a)aTpaTTTU) 'flash, sparkle, glitter', 

Latin sfe//a 'star' {* sfer-[o]/a, diminutive); bret. sterenn, corn. sterenn{P\. steyi), cymr. 

se/ie/? 'star' (PI. sei). Middle Irish se^'star' (ZfcPh. 19, 200); in addition lengthened grade 

gall. GN Dhirona, Sirona; Gothic stafrno. Old High German sterno. Old Norse stjarna'star' 

and Old High German Old Saxon sterro. Old English steorra ' star' {*sters- to s-stem 

*steros7), Old Frisian stera' star' (or sterei.). 

Tokharian: A sre (pi. sreh), B scirye (FT *scariye) 'star' (Adams 640)
```


## [2026-09-14T03:08:39.416Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83007,83070p' POK_full.txt; echo ===; grep -n \"Root / lemma:\" POK_full.txt | awk -F: '$1>81300 && $1<83100' | head -30"
}
```


### [2026-09-14T03:08:40.469Z] TOOL RESULT

```
Exit code 1
Root / lemma: ster-2 
Meaning: star 
Material: 

In a-grade: 

Hittite: ast/ra- c. 'star?' (Tischler 86), haster- c. (204ff) 

Armenian as//. Gen. as/e/"star, stars'; gr. aarrip, -ipoq "star', collective aarpa " young ' 

aoTpov "star, stars' (out of it Latin astrum), wherefore probably with (u)n-)6n-: (a)aT£ponri, 

darpann "lightning, sheet lightning ', aaT£ponr|Tr|(;, aaTsponaToq " Blitzeschleuderer (Zeus) 



In zero grade: 

In e-grade (internal): 

gr. OTtpoy\) " shimmering ', (a)aTpaTTTU) 'flash, sparkle, glitter', 

Latin sfe//a 'star' {* sfer-[o]/a, diminutive); bret. sterenn, corn. sterenn{P\. steyi), cymr. 

se/ie/? 'star' (PI. sei). Middle Irish se^'star' (ZfcPh. 19, 200); in addition lengthened grade 

gall. GN Dhirona, Sirona; Gothic stafrno. Old High German sterno. Old Norse stjarna'star' 

and Old High German Old Saxon sterro. Old English steorra ' star' {*sters- to s-stem 

*steros7), Old Frisian stera' star' (or sterei.). 

Tokharian: A sre (pi. sreh), B scirye (FT *scariye) 'star' (Adams 640) 

Note: 

Common alb. Tocharian st- > sc- see alb. stjerre, shqerre ' young cow, heifer'. 

In a-grade (internal): 

Old Indie Instr. PI. strbhih, Nom. PI. tarahm. 'stars', tarai. 'star', Avestan Akk. Sg. staram. 

Gen. staro, PI. Nom. staras-ca, staro, Akk. straus. Gen. stram, Dat. stare by 6 'star'; 

without ani. s- (as Old Indie tarah, tara) Tspsajv Gen. PI., with metr. lengthening Tsipsa, 

TEipeaiv ' constellation '; 

Maybe alb. {* Hster-[o]la, diminutive > abbreviated hyirstar'. 

References: WP. II 635 f., WH. II 587 f., Scherer Gestirnnamen 18 ff.. Frisk Gr. Et. Wb. 

170f. 

Page(s): 1027-1028 

Root / lemma: stilp-, stilb- ? 

Meaning: to shine; to show 

Note: dem Bau Indo Germanic roots widersprechend 

Material: Gr. ariApu) 'gleam, shimmer', OTiApn ' radiance '; aTiAnv6(; 'gleaming' = Irish sell 

(eval):1: == not found
```


## [2026-09-14T03:08:44.168Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=81200 && NR<=82500 && /^Root \\/ lemma:|^Meaning:|^Page\\(s\\):/ {print NR\": \"$0}' POK_full.txt"
}
```


### [2026-09-14T03:08:45.194Z] TOOL RESULT

```
81370: Page(s): 1004-1010 
81374: Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
81376: Meaning: post, pillar, stump; to support, etc.. 
81477: Page(s): 1011-1013 
81479: Root / lemma: stegh-, nasal, stengh- 
81480: Meaning: to stick; pole, stalk, etc.. 
81508: Page(s): 1014-1015 
81510: Root / lemma: (s)teg-1 
81512: Meaning: to cover 
81552: Page(s): 1013-1014 
81554: Root / lemma: (s)teg-2 
81556: Meaning: pole, stick, beam 
81590: Page(s): 1014 
81594: Root / lemma: steigh- 
81596: Meaning: to march, ascend 
81631: Page(s): 1017-1018 
81633: Root / lemma: (s)teig- 
81634: Meaning: to stick; sharp 
81704: Page(s): 1016-1017 
81706: Root / lemma: (s)teig''- 
81708: Meaning: shoulder, arm, hip 
81720: Page(s):1018 
81722: Root / lemma: (s)teig''h- 
81726: Meaning: to await patiently 
81736: Page(s):1018 
81738: Root / lemma: (s)tei- 
81739: Meaning: sharp, spike 
81751: Page(s):1015 
81753: Root / lemma: (s)tel-1 
81755: Meaning: to let flow; to urinate 
81775: Page(s):1018 
81779: Root / lemma: stel-2, stela- 
81781: Meaning: broad, to broaden 
81798: Page(s): 1018-1019 
81800: Root / lemma: stel-3 
81802: Meaning: to put, place 
81917: Page(s): 1019-1020 
81919: Root / lemma: stem- 
81920: Meaning: to push; to stumble, stutter 
81941: Page(s):1021 
81943: Root / lemma: (s)ten-1 
81945: Meaning: to groan, etc.. 
81978: Page(s):1021 
81980: Root / lemma: sten-2 
81982: Meaning: narrow 
81996: Page(s): 1021-1022 
81998: Root / lemma: sterg-, sterk- 
82000: Meaning: to care for, take care of 
82014: Page(s):1032 
82018: Root / lemma: (s)ter-1, (s)tera-. (s)tre- 
82020: Meaning: stiff, immovable; solid, etc.. 
82494: Page(s): 1022-1027 
82496: Root / lemma: ster-3 
82498: Meaning: to rob, steal
```


## [2026-09-14T03:08:53.568Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=82018 && NR<=82494' POK_full.txt | grep -n -i \"torp\\|sterp\\|sterb\\|starve\\|starch\\|strut\\|stare\\|stereo\\|GTSpso\\|orspEO\\|steros\\|strudh\\|Avestan\\|Persian\\|New Persian\\|np\\.\" | head -60"
}
```


### [2026-09-14T03:08:54.609Z] TOOL RESULT

```
44:"starblind'. Old Icelandic stara. Old English starian. Old High German staren " stare, 
45:stare'; with-//'- (from -rn-) Old Icelandic stgrri. "Carex' (actually "die 
91:Old High German stare, starah^ strong, big, large'. Old Icelandic sterkr. Old Swedish 
125:klr. storcaty, storc/ty' ragen, stare ', 
211:without S-: torped, -ere' rigid, insensible, betaubt sein' (= Old Bulgarian u-trbpetior = 
222:"suffer, bear, endure', russ. terpetbds.; proto Slavic. *torp/t/ (Kaus.) in Czech trap/'t/, apoln. 
225:np. turus'sour' (if from *trfsa-) and Modern High German derb{see below). 
237:Old High German sterban'6\e' ("*solidify, congeal '; see below Middle Irish ussarb); Old 
240:sterban. Old Frisian sterva. Old English steorfan6s. (engl. starve' perish, esp. vor 
241:hunger'); Old High German sterbo. Old English steorfa' pestilence, epidemic disease, 
246:Modern High German-Tirol storfn^ stall<, stem of a plant, stump ', westfal. storpein 
277:sterbnutb ' solidify, congeal, absterben', etc. (Trautmann 284 f., Vasmer 3, 1 1 
330:strk/an stem V. " march, step, stride, strut', engl. to stride, Middle Low German striden^6\e 
407:Old Icelandic strutr^cusp, peak', Danish strude, 
408:strutte^ stiff stand, widerstreben', Swedish s/m//5'stolpernd go'. 
410:Old English strutian^ stiff stand'. Low German strutf stiff. Modern High German strotz 
452:Middle High German struben, *striuben^ stare ', Modern High German strauben. Middle
```


## [2026-09-14T03:08:58.115Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=82018 && NR<=82494 {print NR-82017\": \"$0}' POK_full.txt | sed -n '195,260p'"
}
```


### [2026-09-14T03:08:59.215Z] TOOL RESULT

```
195: 3. 
196: Labial extensions: 
197: 
198: (s)terp-. 
199: 
200: 
201: 
202: Latin st/rps'siem eines 
203: Baumes (iJbertr. progeny, origin, source, beginning; an ancestor)'; 
204: 
205: Litliuanian s//]77//"sonnewliat ennporl<onnnnen, lieranwaclisen' (actually "*sich straffen'), 
206: s/e/5o//5"auf seinem Rechte bestehen' ("sich versteifen'), sfurp//s ^ rump of the horse'; 
207: 
208: alb. shterpe' infertile ' (compare also 6. ster-' infertile '); Irish serrach' plenitude' (from 
209: den langen Beinen); 
210: 
211: without S-: torped, -ere' rigid, insensible, betaubt sein' (= Old Bulgarian u-trbpetior = 
212: russ. toropetb); Lithuanian tirpti' solidify, congeal, insensible become', Latvian t/rptds.; 
213: 
214: Serb. -Church Slavic utrbpeti' solidify, congeal ', russ. terpnutb'ds., also vorfear', r.- 
215: Church Slavic terpkf auarripoi; ', r. terpk/j'herb, sour'; russ. toropetb, otoropetb 'bestijrzt 
216: become' (Trautmann Bsl. Wb. 325), kir. /o/'dyoa'unbeweglicher person', slov. trap' 
217: blockhead '; 
218: 
219: Maybe alb. trap' fool ' a Slavic loanword. 
220: 
221: in the meaning " rigid, stiff = persistent sein' based on probably Old Church Slavic trbpeti 
222: "suffer, bear, endure', russ. terpetbds.; proto Slavic. *torp/t/ (Kaus.) in Czech trap/'t/, apoln. 
223: //"OyO/ic "torment, smite', russ. toropftb " set in motion '; as " rigid, dull, vom Standpunkte of 
224: Geschmacks': Old Church Slavic *//^yC>b/rb"acerbus, asper', russ. terpkij' herb, sour', as 
225: np. turus'sour' (if from *trfsa-) and Modern High German derb{see below). 
226: 
227: Toils auf (s)teij)-, partly auf 
228: (s)teib'^-cau go back: 
229: 
230: Old Icelandic t^iarfr. Old English deorf. 
231: Old Saxon thervi. Old High German derbi" unleavened ', Modern High German Bavarian 
232: derb'and, dry, lean '; 
233: 
234: with aniaut. 5-: Old Icelandic stjarfixu. "work, toil', 5^a/^"hartmaulig (from horses)', 
235: s///:/^/7/7"halsstarrig', starfu. "work, Streben, Amt', starfa'sicb abmijhen'; 
236: 
237: Old High German sterban'6\e' ("*solidify, congeal '; see below Middle Irish ussarb); Old 
238: Saxon 
239: 
240: sterban. Old Frisian sterva. Old English steorfan6s. (engl. starve' perish, esp. vor 
241: hunger'); Old High German sterbo. Old English steorfa' pestilence, epidemic disease, 
242: plague '; 
243: 
244: 
245: 
246: Modern High German-Tirol storfn^ stall<, stem of a plant, stump ', westfal. storpein 
247: "strauchein' can auf a root form auf b based on. 
248: 
249: 
250: 
251: strep-: 
252: 
253: Lithuanian yC>5/'-s//'5/0//7//"heimtorkeln', 5//yy0//"trample', stripinys, straipis^ rung, 
254: horizontal step on a ladder '; Late Middle High German straf{-ff-) 'straff, strenge'. West 
255: Flemish straf{*strepo-) 'strong, stern'. East Frisian strabben ^s\c\\ widerspenstig 
256: gebarden'. Middle High German strabbeln^ wriggle '; Swiss s/Aa/O/fe/? 'straff Ziehen' 
257: {*strappdn)\ probably as 'stern behandein' here: Old Frisian sZ/'a^a'bestreiten, scold, 
258: chide', mnl. Middle Low German straffen, from which borrowed Middle High German 
259: strafen, ds. 'punish, curse', strafe^ ScheWe, reprimand, punishment '. 
260:
```


## [2026-09-14T03:09:08.649Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=82018 && NR<=82494 {print NR-82017\": \"$0}' POK_full.txt | sed -n '1,60p'"
}
```


### [2026-09-14T03:09:09.676Z] TOOL RESULT

```
1: Root / lemma: (s)ter-1, (s)tera-. (s)tre- 
2: 
3: Meaning: stiff, immovable; solid, etc.. 
4: 
5: Note: s. also ster- 'unfruchtbar' and ster- " stiff Pflanzenschaft', further treg- "alle Krafte 
6: 
7: anstrengen', strenk- 'straff 
8: 
9: Material: A. Gr. aiz^zoc, (Attic also areppoc; from 
10: 
11: *aT£p£6(;) ' rigid, tight, firm, hard', aT£pi(po(; ds. (also 
12: 
13: " infertile ', s. ster-6^ infertile '), OTspsiJvioq ds.; 
14: 
15: GTsTpa 'Kielbalken', lengthened grade: arripa to 
16: 
17: AiGiva npoGupa Hes., arripi^u) (Fut. -ipS) "tight, firm 
18: 
19: prop, support, stemmen', Med. Pass, "sich prop, support, sich feststemmen', 
20: 
21: arnpiYt -YYO<; pad', wherefore aKripinTw 'stijtze', 
22: 
23: Med. "stiJtze myself, stemme myself, dissimil. from *aTr|piTTT(jo; aTpr|vr|(;, aTpr|v6(; " hard, 
24: 
25: sharp, forceful ', aTpr|vo(; n. 'heftiges desire, power, Ubermut', arpriviav "minxish, wanton 
26: 
27: sein', QTpnvu^u) "cry rauh' (in formant. Bez. to Latin strenuu^l), Latin strenuus\o\\ 
28: 
29: riJstiger 
30: 
31: Tatkraft, betriebsam, wacker'; alb. shterr{*ster-n-) "lay, dry the place, make dry up '; about 
32: 
33: strena'goo6 omen, sign' s. WH. II 601; 
34: 
35: Latin consterno, -are, also eA'5/e/77o"besturzen, from the Fassung 
36: 
37: bringen', sternax' shy, storrisch'; 
38: 
39: cymr. fr/n "toil, fight, struggle' 
40: {*strena7); 
41: 
42: Germanic *stara- " rigid, esp. of eye' in mnl. star 
43: m. "Starrheit of Auges', Old High German stara-blint. Old English stger{e)blind 
44: "starblind'. Old Icelandic stara. Old English starian. Old High German staren " stare, 
45: stare'; with-//'- (from -rn-) Old Icelandic stgrri. "Carex' (actually "die 
46: Steife'), starr{Akk. starran) " stiff, rigid, hard'. Modern High German starr^ rigid', 
47: Middle High German sterre. Modern High German Bavarian sterr^ rigid, stiff, whereof 
48: Middle High German starren, sterren^ rigid be or become'. Modern High German 
49: erstarren, starren, Norwegian stara av\6 sterra {*starrian) "sichstrauben, sich anstrengen'; 
50: *sturra- ( *sturna-) "sich steif aufrichtend, stemmend' in Gothic and-staurran " 
51: uncourageous sein'. Old High German s/d/re/? "steif herausstehen, jut, project, protrude, 
52: stick out ', Old High German storro " stump, clot, chunk'. Modern High German storrig, 
53: storrisch; Old English s//e/77e"ernst, hard, stern'. Old High German 5/0/775/7 "stutzen, 
54: frighten' (*"stiff, rigid vor Schrecken'), 5/i//77/ "stupor', Swedish s/i//77a "stutzen'; 
55: 
56: 
57: 
58: Old Icelandic stirdr^ stiff, unbeugsam, hard, 
59: unfriendly'; 
60:
```


## [2026-09-14T03:09:14.259Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=82018 && NR<=82494 {print NR-82017\": \"$0}' POK_full.txt | sed -n '85,100p;320,345p;400,415p'"
}
```


### [2026-09-14T03:09:15.617Z] TOOL RESULT

```
85: in addition gr. Topyoc; " vulture', actually " stiff = big, large'?), compare Tirol 
86: storke{l)n^\N\Vc\ langen Beinen einherschreiten', thijring. 
87: storchen^as ein stork go', westfal. s/c»/'/re//7"straucheln, 
88: stumble'; 
89: 
90: Adj. *starku- in Old English stearc^ stiff, stern, strong'. 
91: Old High German stare, starah^ strong, big, large'. Old Icelandic sterkr. Old Swedish 
92: starker 
93: "strong', zero grade Old Icelandic styrkr {*sturki-) m. " strength '; 
94: 
95: Middle Low German 
96: strak{-ck-) " stiff, straff, gerade emporgerichtet; storrig'. Middle High German 
97: strac{-ck-) "straff, gestreckt, straight': Old English strec, strsec 
98: {strsekl) " rigid, tight, firm, stern, violent'; Denom. (or umgekehrt strak 
99: 
100: 
320: s//7777e/7o'/"resisting, striving' Gloss.; engl. dial. tostrime= to 
321: stride; Lithuanian strainus^ keen, widerspenstig', pasistramyti 
322: "strive, sich feststemmen'. 
323: 
324: 1. With guttural extension: s. streig- 
325: " stiff '. 
326: 
327: 2. With Dental extensions: 
328: 
329: with Indo Germanic -d'^-: Old English 
330: strk/an stem V. " march, step, stride, strut', engl. to stride, Middle Low German striden^6\e 
331: Beine spreizen, weit ausschreiten' (about Latin strittabe//ae ^Bu\r\\6\rnen' 
332: 
333: 
334: 
335: s. WH. II 605 f.); Old High German stntanstV. ^quarrel, sich bemijhen', schw. 
336: 
337: V. Old Icelandic sZ/TcJa 'quarrel, torment, smite'. Old English s//'/o'/5/7 'quarrel'; Old Icelandic 
338: 
339: S//71? 'fight, plague, care, austereness, severeness ', Old Saxon stnd^ioW, fight, struggle'. 
340: 
341: Old High German 
342: 
343: s/zT? 'fight', e//75//7?/"hartnackig'; Old Icelandic stndr^ stiff, 
344: 
345: hard, stern, strong'; with Indo Germanic -flf-: Old Icelandic S//7/5 'strive, sich 
400: 
401: glands, craw' {*sfreuc/-sfrouc/-, sfrud-ma); after Vasmer 3, 145 
402: 
403: in addition Lithuanian trausti^ crumb, spall, crumble ', Latvian fraus/slraW, breakable', 
404: 
405: trust^ decayed, modern'; 
406: 
407: Old Icelandic strutr^cusp, peak', Danish strude, 
408: strutte^ stiff stand, widerstreben', Swedish s/m//5'stolpernd go'. 
409: 
410: Old English strutian^ stiff stand'. Low German strutf stiff. Modern High German strotz 
411: ds., 
412: 
413: Middle High German Modern High German strotzen. Middle High German striuzen 
414: 'strauben, spreizen', struz 
415:
```


## [2026-09-14T03:09:21.092Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ster-\\|^ster \\|^2\\. ster\\|^ster-1\\|^ster-2\\|^ster-3\\|^ster-4\\|^ster-5\\|^ster-6\\|^sterə\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T03:09:21.151Z] TOOL RESULT

```
243:ster-3, 3. Oldest root from *oster- in Greek astér...
1018:ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
1020:ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
1021:ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
1022:ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
```


## [2026-09-14T03:09:27.268Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1010,1020p' AHD_watkins1985.txt"
}
```


### [2026-09-14T03:09:27.321Z] TOOL RESULT

```
steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
steip-
STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre, to compress, stuff, pack: STEEVE!, STEVEDORE; CONSTIPATE. [Pok. stéib(h)- 1015.] stel-. To put, stand; with derivatives referring to a standing object or place. I. Basic form *stel-. 1. Suffixed form *stel-ni- in Germanic “*stilli- in Old English stile, quiet, fixed: sTILL’. 2. Suffixed form “stel-yo- in Greek stellein, to put in order, prepare, send, make compact (with o-grade and zero-grade forms sfol- and stal-): APOSTLE, DIASTOLE, EPISTLE, PERISTALSIS, SYSTALTIC. II. O-grade form *stol-. 1. Suffixed form *sfol-no- in Germanic *stalla- in: a. Old English steall, standing place, stable: STALL; FORESTALL; b. Old French estal, place: INSTALLMENT!; Cc. Old French estalon, stallion: STALLION; d. Old Italian stallo, stall: PEDESTAL; e. Me- dieval Latin stallum, stall: INSTALL; f. Germanic denomi- native *stalljan in Old High German stellen, to set, place: GESTALT. 2. Suffixed form stol-6n- in Latin stolé, branch, shoot: STOLON. 3. Suffixed form *stol-ido- in Latin stoli- dus, “firm-standing,” stupid: sTOLID. 4. Suffixed form *stol-d- in Greek stolé, garment, array, equipment: STOLE}, III. Zero-grade form “*stj-. 1. Suffixed form *stl-to- in Latin stultus, foolish (< “unmovable, unedu- cated”): STULTIFY. 2. Suffixed zero-grade form “st/-no- in Germanic *stullén- in Old High German stollo, post, support (> German Stolle, Stollen, stollen): sTOLLEN. 3. Suffixed zero-grade form *stal-nd- in Greek stélé, pillar: STELE. IV. Extended form “stelg- in Germanic *stalk- in Norwegian dialectal stalk, stalk, akin to the source of Middle English stalk(e), stalk: sTALK’. V. Ex- tended form *steld- in: a. Germanic *stiltjon- in Low German and Flemish sfilte, stick, akin to the source of Middle English stilte, crutch, stilt: sTILT; b. zero-grade form “*stld- in Germanic *stult-, “walking on stilts,” strutting, in Old French estout, stout: stout. [Pok. 3. stel- 1019.] stele-. To extend. Zero-grade form “*sélo-. 1. Suffixed form *stlo-to- in Latin /atus, broad, wide: LATITUDE; DILATE. 2. Attributed by some to this root (but more likely of obscure origin) is Latin /aémina, place, layer: LAMELLA, OMELET. [Pok. 2. stel- 1018.] sten-. Narrow. Suffixed form *sten-wo- in Greek stenos, narrow: STENO-, STENOSIS. [Pok. 2. sten- 1021.] (s)tene-. To thunder. 1. Zero-grade form *stno- in Ger- manic *thunaraz in: a. Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY; b. Middle Dutch doner, donder (> Dutch donder), thun- der: BLUNDERBUSS, DUNDERHEAD; C. Old Norse Thorr (older form Thunarr), “thunder,” thunder god: THOR. 2. O-grade form *tona- in Latin tondre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.] ster-'. Stiff. I. O-grade form *stor-. 1. Suffixed form *stor-é- in Germanic *staren in Old English sfarian, to stare: STARE. 2. Suffixed form *stor-g- in: a. Germanic *starkaz in Old English stearc, hard, severe: STARK; b. Germanic denominative *starkjan in Old English *stercan (> Middle English starchen), to stiffen: STARCH. II. Full-grade form *ster-. 1. Germanic *sternjaz in Old English stierne, styrne, firm: STERN}. 2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL. 3. Lengthened-grade form *s¢ér- in Greek stérizein, to support: STERIGMA. III. Zero-grade form *str-. 1. Extended form *strg- in Germanic *sturkaz in
66
(s)teu-
Old English storc, stork (probably from the stiff move- ments of the bird): STORK. 2. Germanic *striit- in Old English striitian, to stand out stiffly: struT. IV. Extend- ed form *sterd-. 1.Germanic *stertaz in Old English steort, tail: REDSTART. 2. Germanic “*stert- in: a. Old English *styrtan, to leap up (< “move briskly, move stiffly”): start; b. Old English steartlian, to kick, strug- gle: STARTLE. V. Extended form *sterbh- in Germanic *sterban in Old English steorfan, to die (< “become rigid”): STARVE. VI. Extended form *(s)ierp- in suffixed (stative) zero-grade form *trp-é- in Latin torpére, to be
stiff: TORPEDO, TORPID, TORPOR. [Pok. 1. (s)ter- 1022.]
ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
Strahl, ray): BREMSSTRAHLUNG. II. O-grade extended form *strou-. 1. Suffixed form *strou-eyo- in Germanic *strawjan in: a. Old English stré(o)wian, to strew: STREW; b. Old High German strouwen, strowwen, to sprinkle, strew: STREUSEL. 2. Suffixed form *strow-o in Germanic *strawam, “that which is scattered,” in Old English stréaw, straw: sTRAW. III. Basic forms *ster-, *stero-. 1. Nasalized form *ster-n-a in Latin sternere (past participle strdtus from zero-grade *stro-to-), to stretch, extend: STRATUS, STREET; CONSTERNATE, SUB- STRATUM. 2. Suffixed form *ster-no- in Greek sternon, breast, breastbone: STERNUM. IV. Zero-grade form *str-, stra-. 1. Suffixed form “str-to- in Greek stratos, multi- tude, army, expedition: STRATAGEM; STRATOCRACY. 2. Suffixed form *stro-to- becoming Celtic s(t/rato- in Scottish Gaelic srath, a wide river valley: STRATH. 3. Suf- fixed extended form *stro-mn in Greek stréma, mattress, bed: STROMA; STROMATOLITE. [Pok. 5. ster- 1029.]
ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
```


## [2026-09-14T03:09:49.704Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 107 (p.86) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==108' HRN.txt | head -60"
}
```


### [2026-09-14T03:09:50.697Z] TOOL RESULT

```
=== HRN leaf 107 (p.86) ===
-> 86 --
l)(i)rr(l)8tü ('Schwalbe'; oder gehört dies zu perriden?
vergl. gr. nsQiarsQd 'Taube') u. a. m.
383. {\)ter 'ein Vogel'.
Prof. Nöldeke verweist mich auf Ahrens, Buch
der Naturgegenstände, 25, 5 nebst G. Hoff mann 's
Bemerkungen zu der dortigen Übersetzung und ver-
gleicht lat. sturnus, nhd. Staar,
384. tersTden *sich fürchten', tersä 'furchtsam; Christ'.
ap. [/'tras-, tarsatiy 'er fürchtet'; aw. [/^tras-,
teresenti; phlv. tarsitan; ai. i^tras-, träsatl.
kurd. tirsm erschrecken ; afy. tarh[edal; oss. d.
farsim, t. färsin (244); bei. trusag, tursay, n. fursay
(394); sar. inträsam 'ich mache scheu'.
385. turus 'sauer .
kurd. Urs 'sauer ; bei. trusp, triips, n. trus (395);
wa/. tresp, sar. tä/b, yidg. trisp,
386. terfend, ferfende 'Falschheit, Betrug, Nichtigkeit' 0-
aw. i/trap'^ terefyat 'durch Betrug entwenden,
stehlen; phlv. tarftlnltan durch List wegnehmen*
(y. 11 (17)), taraftagl, taraft (ZPGL); ai. (mit anderer
Bedeutung) [/^trap-^ trdpate 'verlegen werden', eigent-
lich 'sich wenden, abwenden ; vergl. gr. Tginco,
np. terb 'List', das Hübschmann (ZDMG. 26, 457)
dazu stellt, ist unbelegt-).
M ÖF, FJ und FR bieten die folgenden Belege:
(Metr. Xefif)
nebüved der keläm-i tu juz edl
nereved her zehän-i tu ierfend
Öcms-I Fa/rl.
(Metr. Heze.]):
cun x^d neküiii ciinäiiki göyl
pend-l tu büved düröy ü ter/end
Näsir Xosrö.
Ein Vers Senai's im FJ ist metrisch nicht in Ordnung.
Auch tcrwend, terwende sollen in der gleichen Bedeutung vor-
kommen, während die Worte in dieser Form gewöhnlich nur ^Erstling
einer Frucht' bezeichnen.
^J Daneben giebt es auch ein up. terkend^ ierkeude mit gleicher
Bedeutung. FJ (fehlerhaft), FR:
```


## [2026-09-14T03:09:59.104Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- PHD ---\"; grep -n -i \"turuš\\|turush\\|truš\\|tuxl\\|^truš\" PHD.txt PHD_mackenzie.txt | head -20; echo \"--- NYB ---\"; grep -n -i \"turuš\\|truš\" NYB_vol2_glossary.txt | head; echo \"--- HUB ---\"; grep -n -i \"turus\\|turuš\\|tirs 'sauer'\\|sauer\" HUB.txt | head -20; echo \"--- CHEUNG ---\"; grep -n -i \"turuš\\|truš\\|sour\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:09:59.211Z] TOOL RESULT

```
--- PHD ---
PHD.txt:4474:dat targumān tarwēn- tarwēnīdan trufš truftag truš
PHD_mackenzie.txt:625:       tohm(ag) [twhm(k') 1M twhm, -g, N tUXlll, -a] ...
--- NYB ---
1116:catrušvitak [ctlwšw'tk'] a fourth, a . quarter, a cubic measure 42%. — Borrowed, and reshaped, from Av. (580) cadrušva-, cf srisvätak.
--- HUB ---
1630:385. Zu turns *sauer etc. vgl. auch afgh. triv, f. tarva
1631:sauer. Es gelingt mir nicht, die verschiedenen
5114:belegt), skr. ksar *fliessen'; turns *sauer' aus t^fsa-? (siehe
6570:leicht auch inlautend in turvs *sauer (aus *trus -= Hrusf
9556:cafsidan 'anpacken, kleben. Ueber turns *sauer =
--- CHEUNG ---
3289:source. Skt. camura- is perhaps rather a so-called "substrate" word, as it 
5198:and formal agreement with the Skt root: borrowing from a Sanskrit source should 
6489:root is perhaps a borrowing from a "substrate" source, comparable to similar verbs 
7301:Olrish ger ‘sharp, sour’, Lith. giZti ‘to become sour [of milk, soup]’, Lith. gaiZti ‘to 
7897:Henning: 387 f. cites NP garzin from the lexicographical source Farhang-i Jahangiri 
8149:Olrish glam ‘cry, curse’, are probably from a substrate source, on which see 
8384:seems to point to borrowing from an Elr. source, cf. Henning, BSOAS 10: 100; 
8814:"substrate" source ? 
13269:*4-rux-S° ) = argay (m.) ‘belch, sour eructation’, argamdy (f.) ‘yawning’, (Wan.) irZa 
15615:opening, hole’, kha- (f.) ‘source, spring’ is usually assumed (cf. EWAia I: 446, fn.). 
16854:*NEIR: Yghn. mayd- ‘to curdle’, Wa. moö-, mod-/mo6t- ‘to turn sour, curdle’, Oss. 
16857:‘buttermilk’ || (+ *ni-) Sh. (Baj.) nimäö-/nimost ‘to prepare cream and sour milk’, 
16858:Sariq. патиӨ-/патиӨ ‘to turn sour’, Khf. nimöö ‘cream coagulated in a trough’, 
16861:*SANSKRIT: Skt. mástu- (n.) ‘sour cream’ (< *mad-stu-) = EWAia П: 336 
18448:Sangl. niduk, Ishk. nuduk ‘buttermilk’, M. niyo, Yi. niya ‘sour milk’ || (+ *pari-) 
19138:*NEIR: Sh. pai, Sangl. poy, Yi. poya, M. poya 'sour milk" (LW ?), Pash. poy (f. 
19893:old borrowings from an Indo-Aryan source (Szemerényi 1957: 628b). 
19974:the same unknown "substrate" source that passed on the strikingly similar item OP 
21460:Wa. rosod-, rosoó-/rosn- ‘to break [intr.]; to get sour [of milk]’ 
22237:*MISC: Par. sit(u) ‘sour’, Arm. (LW) sug ‘lament’
```


## [2026-09-14T03:10:04.436Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"truš\" PHD.txt | head -20; echo ---; sed -n '4470,4480p' PHD.txt"
}
```


### [2026-09-14T03:10:04.512Z] TOOL RESULT

```
4474:dat targumān tarwēn- tarwēnīdan trufš truftag truš
---
-tar
tar, tarr tarazén- tarāzēnīdan tarāzūg piht
targ
tars
dat targumān tarwēn- tarwēnīdan trufš truftag truš
talag, tarrag talagčīn tarmānīh tarmenišnīh tarmenišn
tars-
[181]
ves v p үө шее
rod
ўе
```


## [2026-09-14T03:10:06.401Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"trus\\|truf\\|tlwš\\|sour\" PHD_mackenzie.txt | head -30"
}
```


### [2026-09-14T03:10:06.475Z] TOOL RESULT

```
413:(J-from whatever source) and the earliest New Persian (N-
781:       sipurdan, sipiir-] commit, entrust, consign.
785:abcstan ['pst'n l ] refuge, support, trust.
809:ab-kamag ['pk'mk l I N '""'a] a thick, sour soup.
1661:bun-xan [bwnh)n ] source.
1732:   ItaAmag [elmk l I M elmg, N ""'a] spring, source.
2610:  appoint, commission, entrust.
3493:mAst [m'st IN . . . . ] curds, sour milk.
4698:stOr [stwl] trustee, curator, guardian.
4699: -ih: trusteeship.
5017:tru(f)s [tlw(p)f I (P tryfS), N turf] sour.
5018:truftag [tlwptk ' ] stolen; intercalary (days).
5108:wAbarigiin [w'plyk'n l I M w'bryg'n] true, trustworthy.
5109: --ih: trustworthiness.
5534:2xan [h),,' I P x)n] spring, source.
5730:zahabag [zh)pk I N zahdb] spring, source.
6481:educate frahixtan, parwardan.                entrust abespurdan, gumardan.
6898: intercalary (days) duzidag, truftag;      joy farroxih, sadih, urwahm(an)ih.
7082:  (time, length) hasar, v. Appendix        milk (n.) jiw, pem, sir; sour'" mast.
7639:     ruwan, uStan.                      spring, v. source.
7642: sour tru(f)s.                          sprinkle passinJidan.
7643: source bunxan, casmag, xan(ig),        sprinkling passinJisn.
7680:stolen duzidag, truftag.                   suburb parwiir.
7816:touch (v.) pahikaftan, pahrmah-,         trust abestam/n.
7817:    sohistan.                            trustee srur.
7818:to'lvard(s) andar, 0 •.• ron, padirag.   trusteeship stiirih.
7819:tower burg.                              trustworthiness wabariganih.
7820:track pay.                               trustworthy wabarigan.
8193:                                        trus
```


## [2026-09-14T03:10:16.992Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 710 711 712 713 714 715 716; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' BQT_v1_pages.txt | head -8; done"
}
```


### [2026-09-14T03:10:18.010Z] TOOL RESULT

```
=== leaf 710 ===
هعئی با زای نقطه دار نیز بنظرآهده ات
ترر بان » بروزن همزبان؛ بمه‌:ی زبان
آور وشخصی که کرم کفنکو شود و خن هی
ثر وتازه بگوید - و بمعنی ترجمان هم هست
یمنی شخصی که لفتی را اززبانی بزبان دیگر
قرب کند ۷ .
فر ۵۵ بسکون ثالی بر وزن سرزده »
بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
=== leaf 711 ===
یو اس
آلرسه- بفتح اول, قوت واهمهرا گویند ‏
رصم اول فوس تزح را )۱( 3
تر شدن ه کنابه از اعراضی شدن
و آزرده گردیدن باشد ببب ظرافت کردن
تر شاك ضم اول بر وزن اردك »
نام پرندمایست سبزرنگه - و بر که کياهی است
اه
=== leaf 712 ===
آر قنج» بر وزن شطرنج , راه باريك
ودشوار را گویند ۵ .
آر نك ۱ » بروزن‌فزند » بممنی‌مسال
و بپوده ۷ - ودروغ - و تروبر و عکر وحیله
باشد۸
آر هه بر وزن برف , کشكه سیاه را
کویشد و آنرا بعربی مصل وبترکی قرافروت
خوانشد - و کمكك سفید و پر خشك را نیز
=== leaf 713 ===
وامالآنرا نی زکفته‌اند - و گذاشتن و گذشتن
ونرك دادن وخلاصی از تملفات‌جسمانی وخواهش
نضالی و گشتن ازماسوی‌افه بجذیات حفانی,ونراد
باینمعنی عربی هم هست6 - ونام قصبه ایست از
مضافات آذربایجان ‏ و بنم اول و سکون انی
ممروف‌است که‌نفیض نازمك باشدء ‏ و کویندترکان
از ارلاد بافث بن نوح‌اند و ولابت ثرکتان‌رانیز
بطریق مجاز تراد میگویشا - و کنابه‌ازمطلوب
=== leaf 714 ===
ت رکتازی
کوبته از جنی فرج یکه زدان ترك پوشند.
تر کتادی با تای قرشت بر وذن
مرخ بازی » تلخت آوردن بشتاب و تعجبل و می
خبروتا گاه باشدبرسبیل تاراج وغارت نمودن‌سوبمعنی
حولان کردن عم گفته‌اند ۱
قر لگ چوش » با جیم بر وزن سرخ
پوشی ۰ کوشت تیم پخته را کوندا -
=== leaf 715 ===

=== leaf 716 ===
۵
۷
۷
4
تاش 9
```


## [2026-09-14T03:10:26.480Z] TOOL CALL #21: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:485 --image 2>&1 | head -60"
}
```


### [2026-09-14T03:10:27.548Z] TOOL RESULT

```
no scan of BQT covers printed page 485 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:10:32.572Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==712' BQT_v1_pages.txt; echo \"======= 710\"; awk 'BEGIN{RS=\"\\f\"} NR==711' BQT_v1_pages.txt; echo \"==== grep latin\"; grep -n \"tur\\|truš\\|trš\" BQT_v1_pages.txt | sed -n '1,20p'"
}
```


### [2026-09-14T03:10:33.614Z] TOOL RESULT

```
یو اس
آلرسه- بفتح اول, قوت واهمهرا گویند ‏
رصم اول فوس تزح را )۱( 3
تر شدن ه کنابه از اعراضی شدن
و آزرده گردیدن باشد ببب ظرافت کردن
تر شاك ضم اول بر وزن اردك »
نام پرندمایست سبزرنگه - و بر که کياهی است
اه
ترش یا - کیاهی است‌ترش خموساء
وه رگیاه ترش‌را نوان کفت عموماً .
فر شه- بن اول و تانی و فتح الت" نام
میوهء‌ایست -٩‏ ورستنیی باشد که تضم آندا بعرمی
بزر الحماض و حب آلرشاد خوانند . اکر قدری
از آن‌نخم درخرعه بندند» وزن بربازوی چپ‌ندد
مادام که باخود دارد آیستن نشود. ۶
تر شیناث. بروزن گل چنك. رستنیی
باشد بوستانی که بعربی حماض کویند ؛ و نخم
آنرا بزه الحماش خوانند ؟ .
فرع » بنم اول و ثالی و سکون ین
تقطه دار , اسبی باشد سرخ رنگه که آن را
کهر خوانند ۴ .
قرغاذه - بروزن ادزه. غالبوساحب
حکم وسر کش وک ی که حکمها ازروی غالبیت
ور کی کند - وسر کشی کردتیرا نیز کویند.
قر تغاق - بنتح اول بر وزن چخماق »
بای داشتن شبها د خبر دار بودن را کویند -
ویضم اول عم باینمعنی آمدیاست.
قر هه با دال ابجد بر وزن طبقچه .
گرفته شده وترنجده» وهرعنوی وبندیومفصلی
که سب درد مندی و آزار آن حرکت شوان
کرد . گونند « ترغده شده است » ۰ و بروژن
غمکده هم آمده است که بفتح نالث باشد -
ترش مه بکسر الت بر وزن ورزش ۰
نوعی از زرد آلو و فیسی باشد .
فرغو ‏ بر وزن بد کوء نوعی ازباقتة
ابررشمی سرخ رنگه باشد.
(0) چش: قوی وقرح‌را:
اد ۲۳
از آن کز تو ترسد شری ای حکیم
و گر با چنو صد بر آیی بجنگه .
« کلتان ۲۸ .
باشد. ضد شیرین.
مقابل: شیرسی .
======= 710
هعئی با زای نقطه دار نیز بنظرآهده ات
ترر بان » بروزن همزبان؛ بمه‌:ی زبان
آور وشخصی که کرم کفنکو شود و خن هی
ثر وتازه بگوید - و بمعنی ترجمان هم هست
یمنی شخصی که لفتی را اززبانی بزبان دیگر
قرب کند ۷ .
فر ۵۵ بسکون ثالی بر وزن سرزده »
بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
- وقنح انی بروزن تبرزه هم‌آهدء ۲ ست.
تر فان بروزن ومعتی ترجمان است
یمنی شخصی که لفتی راز زبانی بز بان دیگرسیان
کند ؟- وترزبان را نیز گوبند ۴ و آن شخصی
باشد که سخنهای تروتازه نقل کند.
نرس- بخم اول و سکون انی و سین
بی‌نقطه» بمعنی سخت و محکم باشد- ودر عربی
سیر را کوبند که ترکان قلقان خوانند - و نم
اول ونانی زمین سخت باشد ؛ و باین معنی بفتح
9
اول دضم نانی هم گفته‌اند - وبفئح اول وسکون
انی ممروف است که خوف وبیم باشد ۴ .
قر سا ه بر وزن تنها » ثرسنده و یم
بر نده وء امه کننده‌را گو ند و نصرانی ٩‏ وآش-
مرست را نیز گفتهاند ۷
ترس استودان*- بنتح اود
وسکون ثانی و ثاكث و همز؛ مفتوح وسین دبگر
موقوف و فوفانی بواو زسبده و دال بالف کشده
بنون زده دعا وزند ویازند (۱) خواندن فارسیان
ات یه ووو من اه تمه منک :له که
گونند چونروح از فالب مفارقت نماید سه‌شانه
و او را دز این
سه شبانروز ترس دم بسیار است ٩‏ لهذا دراین
سه روز برسردخمة اونكك خوانند تا روح‌اواز آن
ایمن گردد . ومعنی ترکیبی اين لفت خوف فبی
است چه ترس بمعتی خوف ویم‌باشد, واستودان
دخمه ومقبره را کوند . ۶
0
)۱( چيك: زند وبا ند.
. رك : ترزفان‎ ٩
«اسشق ۰۰۷۸۶ اتکاه
رك : ترسیدن .
راهب‌نیز درعر می بهه ین معنی است
۴ بارسی اسثان و اوستابی ۳25 ‌
۱ - بهلری 2۲521
۳۸ چنانکه
ای کریمی که از خزانة غیب
٩‏ - در ندش فصل۲۸ بند۱۸] مده:
۰ کلستان ۲ *.
۵ رل : اسنودان .
. دیو وبزرش بردر دوزخ
ث رسندفه» خالف.
==== grep latin
```


## [2026-09-14T03:10:45.727Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; echo ---; grep -n \"اسطرلاب\\|استرلاب\" MON_part1.txt MON_part2.txt | head -20; echo \"--- estart ---\"; grep -n \"استارت\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T03:10:45.841Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
---
MON_part2.txt:21987:مرتفع در اسطرلاب که عرو اسطرلاب بدو 
MON_part1.txt:10135:اسطرلاب: علامت‌های هفت اختر بر 
MON_part1.txt:11083:اسطرلاب (التفهیم بیرونی). خيمةً بز رگد» 
MON_part1.txt:66498:نوعی از بات نجومی مانند اسطرلاب. 
MON_part1.txt:89873:است؛ قبله. (اسطرلاب) جسمی است که 
MON_part1.txt:96733:پار» پاور. (اسطرلاب) قسطعه‌ای است 
MON_part1.txt:96734:مستطیل ملصق بر پشت اسطرلاب که آن را 
MON_part1.txt:98850:طبقه‌ای از طبقات اسطرلاب که مشبکك 
--- estart ---
MON_part2.txt:91861:استارت الکتریکی ندارد روشن می‌کنند. 
MON_part1.txt:2731:پیچی شده‌ای که در داخل استوانةٌ استارت 
MON_part1.txt:11255:استارت: 7 () حرکت کردن و به 
MON_part1.txt:11259:دوچرخه‌سواری دو نوع استارت است: 
MON_part1.txt:11260:استارت متح رک و استارت ثاست. 
MON_part1.txt:11265:ضح.- معمو لا آن ر راستارت» گو بند. 
MON_part1.txt:81489:قبل از باز کردن سویچ دستگاه استارت و
```


## [2026-09-14T03:10:48.963Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11245,11270p' MON_part1.txt; echo \"=== astrolabe ===\"; sed -n '10125,10145p' MON_part1.txt; echo \"=== find headword استرلاب ===\"; grep -n \"اسْطُرلاب\\|اسطرلاب\\b\" MON_part1.txt | head; echo === ; grep -n \"استرلاب\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-14T03:10:49.167Z] TOOL RESULT

```
Exit code 1
ورزش] (.) میدان ورزش» زمین ورزش» 
ورزشگاه. 

شتا و تقاهد [ع.] (ا.) ج. ستر) سترها؛ 
پرده‌ها. استار کعبه: پرده‌های کعه. هتکك 
استار: پرده در یدن. 

استار: :2اه [معر. چهار] (ا. عد) عدد 
چهار» چارء اریعه» چهار تا. 

استارت: 7 () حرکت کردن و به 
حرکت در آوردن (ور.) در ورزش‌های دو 
و میدانی» دوچرخه‌سواری» شنا و اسکی 
لحطه حرکت ورزشک‌اران است. در 
دوچرخه‌سواری دو نوع استارت است: 
استارت متح رک و استارت ثاست. 

استار تر؛ ۲ (ا.) (مکن.) دستگاه 
خودکاری است که موتوری رابه سرعت 
عااي ول تن معیی راد جر کت درمی آورد. 
ضح.- معمو لا آن ر راستارت» گو بند. 
استاز: 2اه (.) دورة خدمتی که داوطلبان 
کاری برای فراگرفتن آن کار باید بگذرانند؛ 
کار آموزی. 

استازیر: ۲ تا (ص.) (کم.) کسی که 
=== astrolabe ===
ت 
ارفع: 2۳3 [ع.] (رص تفض. رفعت) بلند تر» 
رفیع تر» برتر» اعلی» برداشته‌تر. ارزنده‌تر» 
قیمتی تر» ارچمند تر. بلند قدر تر» اشرف. 
ارق: (272«۵ [ع.] (ص تفض. رقت) رقبق تر» 
تنگ تر» شفاف‌ترء باریکک تر. 
ارف‌ام: فد [ع.] .( ج. رقم؛ خط ها» 
نو شته‌ها. . (مسد.) علامت‌های وضع شده برای 
0 عددها. در تداول بازاربان مجموع 
چند بخش از کالا را می‌گو بند؛ اجناس. ار قام 
اسطرلاب: علامت‌های هفت اختر بر 
اسطر لاب. ارقام هندی: علامت‌هابی که 


فرهنگ فارسی معین 


ار غنده 
برای نمايش عدد در فارسی بکار می‌بریم و 
منشاء آن را از هند دانند: ۰ ۱ ۲ ۳ ۴ ۵ "٩‏ 
۷ .۱ 
=== find headword استرلاب ===
10135:اسطرلاب: علامت‌های هفت اختر بر 
11083:اسطرلاب (التفهیم بیرونی). خيمةً بز رگد» 
66498:نوعی از بات نجومی مانند اسطرلاب. 
89873:است؛ قبله. (اسطرلاب) جسمی است که 
96733:پار» پاور. (اسطرلاب) قسطعه‌ای است 
96734:مستطیل ملصق بر پشت اسطرلاب که آن را 
98850:طبقه‌ای از طبقات اسطرلاب که مشبکك 
(eval):1: == not found
```


## [2026-09-14T03:10:59.056Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اسطر\" MON_part1.txt | head -20; echo \"=== page markers ===\"; sed -n '11270,11290p' MON_part1.txt; echo \"... look for numeric page marks\"; awk 'NR>11000 && NR<11600 && /^[۰-۹0-9]+$|فرهنگ فارسی معین/ {print NR\": \"$0}' MON_part1.txt | head -20"
}
```


### [2026-09-14T03:11:00.241Z] TOOL RESULT

```
10135:اسطرلاب: علامت‌های هفت اختر بر 
10136:اسطر لاب. ارقام هندی: علامت‌هابی که 
11083:اسطرلاب (التفهیم بیرونی). خيمةً بز رگد» 
12783:اسطر لاب: ([ - اصطر لاب؛ معر ] 
17615:دسستگاه: اندام‌های اسطرلات. آلت 
66498:نوعی از بات نجومی مانند اسطرلاب. 
89873:است؛ قبله. (اسطرلاب) جسمی است که 
96733:پار» پاور. (اسطرلاب) قسطعه‌ای است 
96734:مستطیل ملصق بر پشت اسطرلاب که آن را 
98850:طبقه‌ای از طبقات اسطرلاب که مشبکك 
=== page markers ===
استازیر: ۲ تا (ص.) (کم.) کسی که 
دورة کارآموزی را میگذراند» کار آموز. 
استافیل: 0201 [دانٌ انگور] (.) انگوره 
استاکار: ۰:02-5 (- استادکار] (ص‌فا.) 
(عم.) بر صنعتگران از نجار و کفش‌دوز و یا 
کار گران فنی که در کار خبره و استاد باشند 
اطلاق می‌شود و زیردستان آنان را شاگرد 


استالااکتیت فرهنگ فارسی معین ۱۳۵ 


می‌نامند. 

استالا کتیت: :25اه (.) (زم.) ستون 
آهکی مخروطی شکل معلق در سقف 
غارها که در نتیجه آب چکك سقف غار 
سوجود سی آید. آبی که ار سقف غار 
می‌چکد. قبل از خروج از منافذ سقف غار 
دارای بیکربنات کلسیم محلول است و پس 
از خروج از منافذ سقف غار انیدرید 
... look for numeric page marks
11188: ۱۳۴ فرهنگ فارسی معین استات 
11279: استالااکتیت فرهنگ فارسی معین ۱۳۵ 
11507: فرهنگ فارسی معین 
11560: ۱۳۸ فرهنگ فارسی معین ۱ استخار
```


## [2026-09-14T03:11:08.477Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12780,12800p' MON_part1.txt; echo \"--- nearest page marks ---\"; awk 'NR>12600 && NR<12950 && /فرهنگ فارسی معین/ {print NR\": \"$0}' MON_part1.txt"
}
```


### [2026-09-14T03:11:09.503Z] TOOL RESULT

```
جایگاه ستوران» جای آرامش چارپایان؛ 
۳ 

اسطر لاب: ([ - اصطر لاب؛ معر ] 
(.) (نج.) ابزاری است که برای اندازه گیری 
موقع و ارتفاع ستارگان و دیگر امور فلکی 
بخار می‌رفت. 

اسطقس ۰ (0500705)5 آمعر. محر. عنصر و 
اصل ] (۱.) مایه» ماده» اصل هر چبز» مادة 
سجستین در و هبولی. عنصر های 
چهارگانه: آب و خاک و باد و آتش. 
استخوان‌بندی هر چیز» آنچه مایةٌ قوام و 
دوام چیزها است؛ ج. اسطقسات. 
اسطقسات: 05۱0۳۵5۵-۱ [معر . بو. ع.] .( 
ج. اسطقس. الف - مایه‌ها» مواد (اصلی). ب 
- عنصرهای نخستین هر چیزء عناصر اربعه. 
جَ اجرام سماوی. د علم هند سه. 
اسطوانه: (0-)05۱0۷2۵ [معر. ستون < 
استوانه ] (.) ور دنه تب رک نورد. 
اسطوره: (۵-)05۱۲۸ [ - اسطور - اسطاره» 
--- nearest page marks ---
12644: 7 فرهنگ فارسی معین استیحاش 
12728: اسدال فرهنگ فارسی معین ۱۵۱
```


## [2026-09-14T03:11:20.571Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN astrolabe ===\"; grep -n -i \"astrolabe\" KLN_1966.txt KLN_1971.txt | head -6; echo \"=== KLN star, ===\"; grep -n \"^star, n\\|^star,\\|steorra\" KLN_1966.txt KLN_1971.txt | head -8; echo \"=== KLN torpedo ===\"; grep -n -i \"^torpedo\\|torpēre, 'to be stiff\\|torpere\" KLN_1971.txt | head -8; echo \"=== LKT astrolab ===\"; grep -n -i \"astrolab\" LKT.txt PHN.txt DEV.txt FVQ.txt AFM.txt | head -10"
}
```


### [2026-09-14T03:11:20.709Z] TOOL RESULT

```
=== KLN astrolabe ===
KLN_1971.txt:11196:alidade, n., indicator of an astrolabe. — F., fr. 
KLN_1971.txt:21662:astrolabe, n., an obsolete astronomical instru- 
KLN_1971.txt:136023:astrolabe, catalepsy, epilepsy, narcolepsy, nym- 
KLN_1966.txt:2199:Alice  blue.  —  Named  after  Mrs.  Alice  Roosevelt, wife  of  President  Theodore  Roosevelt, alicula,  n.  a  short  cloak  (Rom.  antiq.)  —  L.  ‘a light  upper  garment’,  a  dimin.  formed  fr.  Thes- sal.  Gk.  akKiY.cc,  acc.  of  aXXi^,  ’upper  gar¬ ment;  purple  cloak’,  with  suff.  -ula  (see  -ule). L.  alicula  is  not  rel.  to  L.  ala,  ‘wing’, alidade,  n.,  indicator  of  an  astrolabe.  —  F.,  fr. Sp.  alidada,  fr.  Arab.  al-i(lddah,  ‘the  revolving radius  of  a  circle’.
KLN_1966.txt:3764:astrography,  n.,  the  mapping  of  the  stars.  —  Lit. ‘description  of  the  stars’,  fr.  astro-  and  Gk. -ypa<3>ia,  fr.  ypd<pEiv,  ‘to  write’.  See  -graphy. Derivative:  astrograph-ic,  adj. astrolabe,  n.,  an  obsolete  astronomical  instru¬ ment.  —  ME.,  fr.  OF.  astrelabe,  fr.  ML.  astro- labium,  fr.  Gk.  daxpoXdjiov  (scil.  opyavov),  lit. ‘startaking  (instrument)’,  fr.  daxpov,  ‘star’,  and the  stem  of  XocppdvEiv,  ‘to  take".  See  astro- and  lemma.
=== KLN star, ===
KLN_1971.txt:113074:star, esp. Venus. — L. Hesperus, fr. Gk. £c- 
KLN_1971.txt:231169:star, n. — ME. sterre , fr. OE. steorra , rel. to OS. 
KLN_1971.txt:231867:steorra , ‘star’. See star and cp. prec. word and 
KLN_1966.txt:36605:Derivatives:  staple,  adj.,  staple,  tr.  v.,  to  grade, classify,  stapl-er,  n.,  stapl-ing,  n. star,  n.  —  ME.  sterre,  fr.  OE.  steorra,  rel.  to  OS. sterro,  ON.  stjarna,  Swed.  stjerna,  Dan.  stierne, OFris.  stera,  MLG.  Sterne,  MDu.  sterre,  Du. ster,  OHG.  sterro,  sterno,  stern,  MHG.  sterre, Sterne,  stern,  G.  Stern,  Goth,  stairno,  and  cogn. with  OI.  star-,  ‘star’,  nom.  pi.  tarah,  ‘stars’, instr.  pi.  stfbhih,  ‘by  means  of  stars’,  Toch.  A sre-rt  (pi.),  ‘stars’,  Hitt,  shittar,  Gk.  d<jxt]p, doxpov,  L.  Stella  (for  *ster-la),  OCo.,  Bret. sreremi,  W.  seren,  ‘star’.  All  these  words  prob. go  back  to  an  I.-E.  primary  form  *astero,  which is  of  uncertain  origin.  It  possibly  derives  from the  name  of  the  evening  star  called  after  the  Sem. goddess  Astarte,  i.e.  Ishtar,  ‘ AshtSreth  (see Aphrodite).  See  Zimmern  in  E.  Schrader,  Die Keilinschriften  und  das  Alte Testament,  3rd  ed., p.  425  and  Jensen  in  Wiener  Zeitschrift  fur  die Kunde  des  Morgenlandes  6,  70.  Cp.  aster, asterisk,  Astraea,  astral,  astrology,  astronomy, constellation,  disaster,  Esther,  stellar. Derivatives:  star,  tr.  and  intr.  v.,  star-less,  adj., star-like,  adj.,  starr-ed,  adj.,  starr-y,  adj.,  starr- i-ness,  n.
KLN_1966.txt:36707:stellar,  adj.,  pertaining  to  stars.  —  L.  stelluris,  fr. Stella  (for  *ster-la),  ‘star’,  which  is  cogn.  with Gk.  atrxfjp,  aoxpov,  ‘star",  Goth,  stairnd,  OE. steorra,  ‘star’.  See  star  and  cp.  prec.  word  and Estella,  estolle.
=== KLN torpedo ===
250128:torpedo, n., 1) a fish allied to the rays ; 2) a destruc- 
250130:ness ; crampfish’, fr. torpere, ‘to be numb, to be 
250140:fr. torpere. See prec. word. 
250150:the stem of L. torpere, ‘to be numb’, and -ficare, 
250156:the stem of torpere. See torpedo, 
=== LKT astrolab ===
DEV.txt:271:Alancabuth.  Terme  d'astronomie.  Partie  de  l'astrolabe. De  l'arabe  ci^^-aX^x)!  al-anhahoût,  dont  le  sens  propre  est l'araignée.  L'alancabutli,  en  effet,  rappelle  assez  bien  l'idée d'une  araignée  posée  sur  sa  toile  (dont  les  fils  sont  figurés par  le  réseau  des  méridiens  s'entre-croisant  avec  les  paral- lèles). Voy.  les  fig.  /ly  et  54,  dans  le  Mémoire  deSédillot sur  les  instrumenls  astronomiques  des  Arabes,
DEV.txt:436:Alidade.  Esp.  alidada,  allndada,  alhadida,  de  l'arabe i^:>l^2jJI  (d-kllda.  r^Les  lexiques,  dit  Engelmann,  ne donnent  à  ce  mot  que  le  sens  de  jwstis  januœ  (vantail  de porte),  mais  dans  un  traité  arabe  sur  la  construction  de l'astrolabe,  je  l'ai  trouvé  avec  sa  signification  technique, car  on  y  lit  que  c'est  une  espèce  de  mastara  «Ja^o*  ou règk^.v  11  suffit,  ajouterai-je,  d'ouvrir  un  traité  d'astro- nomie arabe,  pour  y  rencontrer  ce  terme  »i>Uifi  ^idôda  avec le  sens  exact  d'alidade,  comme  par  exemple  dans  ce  pas-
DEV.txt:616:82.  Alhabos,  le  clou  qui  joint  l'anneau  de  suspension à  l'astrolabe;  en  arabe,  (j*^aJI  al-habs,  d'une  racine  signi- fiant retenir,  emprisonner.
DEV.txt:617:33.  Alphelath,  petit  cercle  placé  au  centre  de  l'astrolabe  ; en  arabe,  (_j^-iîi  al-fals,  proprement  la  petite  pièce  de monnaie  appelée  en  grec  à^oXos,  obole,  mot  dont  le  terme arabe  est  une  altération.  (Pour  le  changement  de  s  en  th, cf.  alplwralh,  de  ij**J^\  al-faras.^
DEV.txt:622:35.  Alméhan,  trou  circulaire  au  centre  de  l'astrolabe; en  arabe,  (^ys^î  al-mahn,  (Voy.  L.  A.  Sédillot,  Supplément au  Traité  des  instruments  astronomiques  des  Arabes,  p.  226.)
LKT.txt:410:'Spinne'.  Wegen  der  Ähnlichkeit  der sich  kreuzenden  Meridiane  und  Parallel- kreise am  Astrolabium  hiefa  ein  Teil desselben  sp.  alhancahit,  frz.  alancabuth. [Devic  DEt  5.    Laramens  Rem  4.
LKT.txt:2157:'BewegUches  Lineal  am  Astrolabium'; hieraus  sp.  alidada  'Diopterlineal',  frz. alidade  'dass.',  auch  'Lineal',  it.  alidada, dtsch.  Alhidade  physikalischer  Fachaus- druck zur  Bezeichnung  eines  wesent- lichen Teiles  optischer  Meßinstrumente. Es  kann  vermutet  werden,  daß  das  bis- her unerklärte  Wort  Theodolith  auf dieses  Grundwort  zurückgeht.  [DE  140. Devic  DEt  22/23.    Lammens  Rem  15.
```


## [2026-09-14T03:11:29.346Z] TOOL CALL #28: Bash

```json
{
 "command": "ls site/pages/480.jpg 2>/dev/null; pdftoppm -f 480 -l 480 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg480 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg480.png"
}
```


### [2026-09-14T03:11:31.066Z] TOOL RESULT

```
site/pages/480.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 69787 Sep 13 23:11 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg480.png
```


## [2026-09-14T03:11:33.323Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg480.png"
}
```


### [2026-09-14T03:11:33.960Z] TOOL RESULT

```

```


## [2026-09-14T03:11:33.941Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:11:49.694Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 480 -l 480 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg480hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg480hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.50),int(h*0.555),int(w*0.80),int(h*0.615))).save('crop480_chol.png')\nim.crop((int(w*0.30),int(h*0.215),int(w*0.80),int(h*0.265))).save('crop480_astro.png')\n\""
}
```


### [2026-09-14T03:11:53.737Z] TOOL RESULT

```
(4250, 5500)
```


## [2026-09-14T03:11:55.357Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop480_chol.png"
}
```


### [2026-09-14T03:11:55.371Z] TOOL RESULT

```

```


## [2026-09-14T03:11:57.716Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg480hi.png'); w,h=im.size\nim.crop((int(w*0.42),int(h*0.655),int(w*0.80),int(h*0.715))).save('crop480_chol2.png')\n\""
}
```


### [2026-09-14T03:11:59.279Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:12:00.868Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop480_chol2.png"
}
```


### [2026-09-14T03:12:00.888Z] TOOL RESULT

```

```


## [2026-09-14T03:12:06.790Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg480hi.png'); w,h=im.size\nim.crop((int(w*0.42),int(h*0.635),int(w*0.80),int(h*0.672))).save('crop480_ster.png')\nim.crop((int(w*0.30),int(h*0.225),int(w*0.80),int(h*0.275))).save('crop480_astro.png')\n\""
}
```


### [2026-09-14T03:12:08.324Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:12:10.286Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop480_ster.png"
}
```


### [2026-09-14T03:12:10.359Z] TOOL RESULT

```

```


## [2026-09-14T03:12:20.081Z] TOOL CALL #36: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg480.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/480.png && echo copied\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT star- ===\"; grep -n \"star-, stār-\\|stārəm\\|^star-\\|stərəbyō\\|1596\" BRT.txt | head -10"
}
```


### [2026-09-14T03:12:21.012Z] TOOL RESULT

```
copied
=== BRT star- ===
26589:1596
```


## [2026-09-14T03:12:22.625Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Stern\" BRT.txt | head -20"
}
```


### [2026-09-14T03:12:22.682Z] TOOL RESULT

```
3338:der  Sterne?"  V.  44. 3;  —  tsm  °vän?m  .  .
3639:KompA.,  E.  —  Kompor.  aus  apanh-  [%  20^'). —  mp.  (Pü.)  apäxtar,  np.  bäilar  (Hbm.  PSl. läo  No.).  —  ■)  Ergänze  nährte.  — t)  Die  Zer- legung in  apa+'ajflara-  (np.  iLxlar)  ist  falsch. Mp.  apäxlar  ist  ])  'Norden',  aus  ir.  *ap', 2)  Tlanet',  aus  *»/'  {iipa-\-axtar°  "was  bei  den Sternbildern  ist').
4094:•  j.  aß-äSra-'*  Adj.  'den  Samen  des Wassers  enthaltend',  von  Sternen*':  Hstrim staivm  °r»n  Yt<?.4;  —  vlspe  starB  'ra S.IM3;  Yt/i'.z9;—  U.ira  gufra  'raukö
4799:ajasa  andvl . .  Yt5.8s;  —  fiiirim  .. yS  aßcCiraiibyS  ätti  raoxinuha  lazfmnS "..der  mit  den..  (Sternen)  im  Lichtglanz dahergefahren  kommt"  Yt.  Ä45.  7)  mit Akk,  des  Ziels:  ä  mJ  aidäm""^  vahiltä  a ^^at^yacJ  (sd.)  mazdil  Y.j^,  7;  —  at  vä vTsp7ng  ayti'"^  "so  komme  ich  zu  euch allen"  Y.  j/.  2.  a)  in  feindlichem  Sinn, a)  vom  Feindesheer:  späopm  . .  dOräi ayanttm  rasmaoyS  . .  daniayasnanqm  Yt. 5. 68.  p)  'sich  machen  an  — ,  hermachen über  — '*J':  pairikqm  yä  aiti  airim  äpm sqm  .  ,  V.  //.  9.  b)  in  freundlichem, a)  'zur  Seite  treten,  stehen':  at yastsm nsit  na  issmrUS  Syät'*^  (Opt)  "wer  dem aber,  wenn  er  (drum)  angegangen  wird, nicht  zur  Seite  steht"  Y.  46. 6.  ß)  'auf Jemands  Seite  treten,  übei^ehen  zu  — ' (Akk,):  _v7  ayat  (Konj.)  asavanim  divam- wm  (sd.)  ..  Y.j/.  20.  ßß)   mit  Abi.
8284:•)  Gemeint   ist  der  Siem  Salavafsa-  (sd.),  der zweite  der  Sterne  (nach  dem  Tiitrya,  sd.). '3*
8485:•  j.  urvarö.cä9Ta-  Adj.  'den  Samen  der Pflanzen  enthaltend',  von  den  Sternen":  upa ave  stärS  yH  '/^ü  Yt /2.31; — vlspe  stsrd °ra  S.  2. 13;  —  starqin  qfia^ranqm  Zimat- airanam  'ranqm  S.J.  13.
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
11783:•  j.   taera-  m.,   a   'Bergspitze,   Gipfel': 'rasca  barö.srayai0{%A.)\t.ig.6.       a)  sonst von  dem  Gipfel  der  Hara,  Haraitr.  upa 'nm  AarayiYtiS.T,  —  'nmcä  harai%ya hmS  Y.  42. 3;    —    upa    'r>m    Aarai'iya iarttS  yat    ml  aiwitö   vrvistnti   starasca masca  hvania  "auf  dem  Gipfel  desffaraitl- gebirgs,  um  den  meine  Sterne,  Mond  und Sonne  kreisen"  YL/2.  ss'^- Et?')  —  Vgl.  j/<wra-,  S  Sj.  a.   KZ.  29.  487. —  mp.  (Pu.)  tirai,  nbiL  fer  'Be^spitze',    afT. tir^  -spitz'.  —   ')  Vgl.  iSt.  Bd.  J.  4:    /Frai  i hatiurz  Ja  ölt  i  man  ^ariil  u  mäh  u  itäraiän kacpai  afäivartit.  — ')  Falsch  Go».  ABajrAW. so.  I.  189.
12269:♦)  7:,  dem  Yt.  8  gewidmet  ist,  gilt  als  Gegner der  Patriki  (Meteore;  s.  zu  kmma-)  und  be- sonders de»  ^/uffÄi  (sd.),  nach  dessen  Besiegong und  Verlreibung  (Yt.  8.  22  ff.)  er  den  erquicken- den Regen  spendet  (Vt  8.  30  ff.,  Bd.  9.  z\  In Su.  zu  Y.  I.  II,  Ny.  /.  S  wird  er  darum  als vj-ftinakiotram,  in  Npü.  zu  Ny.  /.  8  als  man^t i  batan  bezeichnet.  Mi.  4g.  5  heisst  er  der  erste der  Sterne.  Bd.  2.  7,  $.  i  der  Anführer  des  öst- lichen Fiislemhimmels  und  spezieller  Gegner des  Planeten  T!r  (Merkur);  s.  noch  Dd.  oi.  iff und  die  von  Blocket  RHR.  33.  loj  u.  (=  4, Zeile  3  ff.  des  autographirten  Teiles)  mitgeteille Slelle  des  GrBd.   Vgl.  Gor.  OK.  308)  316,  318.»
12274:•  j.  tiätryaeini-  f.,  Plur.  Name  von  Sternen in  der  Nähe  des  Tistrya:  'yatnyS  (AP.) yatamaide  Ny.  1,8;   —    'yalinyasHa  yasa-
12275:•  j.  tiätryo.star-   m.  'der   TiHrya    (ge- nannte) Stern':  yaihs  ainiis  brszaüi  yä^a
14918:•  j.  paiti.9r«tte  Inf.  'in  den  Weg  zu treten,  aufzuhalten':  mamnOs  slärqtn  ,  . vTspanqm  p'  "vermeinend  alle  Sterne  auf- halten zu  können"  YtÄ39''.
15787:•  j.  paoiiyaeini-  f.,  Plur.  Name  eines Sternbilds 'Plejaden':  'yaanyas^a  yazamaide YtÄi2.
16497:•  j.  bae^aza-  1)  Adj.  (fem.  'sr-)  'heilend, heilkräftig,  heiltätig';  a)  von  Mond  imd Sternen:  mawi^m  ..  bay>m  'Km  Yt". 5;  —  vanantim  stär>m  .  .  °wm  Yt  21. 1.  b)  sonst:  als3  , ,  asti  °zanqm  bag- sai:yS.t)mö  yat  *mq%r?m.sp>nt»m.batiasyB V.7.44;  zitYtj.6;  —  mq^ranqm  'am .  .  bal^atyBJimim  Yt  J.  S;  —  vaca  ars- uxoa    van'hrayms    'zis    (APf?)   YtJÄS;
16648:•  j.  baj-ö.däta-  Adj.  'gottgeschaffen':  y.it hx  stäram  'tanam  aiwi.raocayänte  "damit ihn  die  gottgeschaffenen  Sterne  bescheinen" V.  ig.  33.
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
20399:j.  'iD'Srazav-  in.,  Du.  Bezeichnung iner  a frischen  Schöpfung,  vll.  eines Sternbilds:  nizbayemi  'zu  ^pourvs  *:^a%/ltd yüßis/ff  mairtivä  *d3mqn  'ich  rufe  an  die beiden  M.  im  Süden,  die  ewigen,  die  am besten  kämpfen  von  der  Schöpfung  der beiden  Geister"  V.  ig.  42.
20587:•)  Neben  jlsay,  dem  Dahia  der  Gier,  elwit als  Hexe  der  Habsucht  od.  dgl.  zu  fa^isen.  Bd. 5.  2,  28.  44  erscheint  duidin  müs  parlk  (so  28) 'die  diebische  P.  MüP,  die  als  dambömand  'mit einem  Schweif  verseben'(s,  ■Eapairikä-\  beieichnet wird,  in  Verbindung  mit  den  Planeten  als  Feind von  Sonn*,  Mond  und  Sternen.
22629:•)  Er  gilt  Bd.  2.  ?,  5.  I,  Mx.  4g.  12  als  An- führer des  westlichen  (s.  DsT.  ZA.  3.  417)  Fm- sternhimmels  im  Kampf  gegen  den  Planeten Öhrmaid  (Juppiter)  und  als  Hüter  der  Narbutz. passe.  Ob  der  Stern  Wega  gemeint  ist?  S. übrigens  unter  lalavalsa-.
24868:•  ').,  g.  'raocah-,  p.  raucah-  n.  i)  'Leuchte' (bes.  des  Himmels) :  hvare  'c5  Vr.  if).  2, Yt.  6.1;  —  slrSUiäi  mdiiA^mcn  hvanca °ca  "die  Sterne,  den  Mond  und  die  Sonne, die  (himmlischen)  Leuchten"  G,^.  6;  — mt^nm  .  .  yeivhe  vaxl .  .  us  ava  -La ainaeiti  ava  pairi  imqnt  sqm  jasciiü  "M, . .,  des  Stimme  hinauf  bis  zu  jenen  Leuchten dringt,  rings  um  die  Erde  gehl"  Yt,  10. 85;  90,  H. /.  16;    —    c'ay3  Hat  aile  ''iv!'>
```


## [2026-09-14T03:12:27.064Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"star-  m\\|star-   m\\|j.  star-\\|star-  m\\.\" BRT.txt | head; echo ===; grep -n \"^• *j\\. *st[aä]r\" BRT.txt | head"
}
```


### [2026-09-14T03:12:27.129Z] TOOL RESULT

```
Exit code 1
3984:•  j.  aiwyästar-  m.  'der  das  Bansman bündelt':  upa  tu  n6  'la  bansma . .  Yyt  2J.
5801:•  j.  astar-  m.  'Schleudercr,  Schütze',  mit Akk.  verbunden:  °ta  ilum  F.  7.
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
12275:•  j.  tiätryo.star-   m.  'der   TiHrya    (ge- nannte) Stern':  yaihs  ainiis  brszaüi  yä^a
12993:j,  darstar-  m.  'der  erblickf.
13713:•  j.  dürae-darstar-  m.  'der  in  die  Feme ^ebt':  °ta  nama  ahmt  YLi.  12.
15155:•  g.  paity'i-star-  m-  'der  wiederholt,  durch Wiederholung  einschärft':  %wqm  atalSqm (näml.  vacaiikqm)  'tanmcä  fradoxstlrtmia dad^maidi  "dich  (Zar.)  bestellen  wir  als deren  Einschäifer  und  Lehrer"  Y.yj.  9'>.
17805:•  j.  fra-varstar-  m.  'Bekenner  (des Glaubens)':  döai  anyaliqm  asaonqm  (nämL Jravaiis)  . .  yazäi  "ta  Yt  i.  30.
18486:•  j.  naenaestar-  m.  'der  eifrig  strebt nach  — ,  sich  bemüht  um  —'  (Gen.)'*:  kuma- tanqm  hüxtanam  kvar^lanqm  ..tnahl  aibi.- antärö  'tsrö  ya^ariä  voAunam  mahl  "wir
23548:•  g.  västar-  m.  'Hirte'  als  der,  der  für; Ndiiung  und  Sicherheit  der  anvertrauten Herde  sorgt:  yim  */fngui)-3  {sd.)  dadat Uarym  Y.27,13;  zit  /p.  I4i —  »^'^  "'*'■ •ta  xsmai  anyü  "ich  habe  keinen  andern  -■ Hirten  als  euch"  Y.  2g.  i.
(eval):1: == not found
```


## [2026-09-14T03:12:30.826Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'Stern'\" BRT.txt | head -10"
}
```


### [2026-09-14T03:12:30.883Z] TOOL RESULT

```
26639:•  j.,  g.  ^star-  m.  'Stern':  tainm  (sd.) httraihya  . .  yat . .  aiwits  urvisntti  staras- (NP.)'V'ä  mäsca  kvartla  Yt.  J2.  25;  V. '  2.  40;  —  slrfus{A2.)ca  mänhfmca  hvarna raocä  yazamaide  G.^.  6;  Y.  2.  11,  yi.<), Vtio.  145,  *V.  7.  52  (äs  Nom.)'>;  —  kuka . . yaosda'iäni . . ku%a  *strSus'* . . mänh>m . . hvart  V.  11.  \;  1  (als  Nom.),  10  (statt Abi.);  ~  kasnä  :^'Sng  *s/rfm(,GP.)äca  däl adväfam  (sd.)  Y.  44-  3 ;  —  ankam  (näml. fravasinqm)  raya  . .  hvan  . .  mh  . .  stärS ava  pdka  yänti  Yt.  i_j.  16;  FrBy.;  — fra- va^ayB  .  .  yä  strqm  mStthS  kür5  anayra- nqm  rao^anhqm  pa%S  dalsay»n~^\..i3.$T; V.l.  16;  —  Ääu  ma..  ave  stärö  V.9.41; Yt.  Ä  i;  —  tistrJm  ..yim  ratBm  ..vlspaisqm stärqm  Yt.  S.  44;  —  nittmalit  avaüqm stärqm  ya'ka  nars  malmyehe  va-^'hangm "selbst  die  kleinsten  jener  Sterne  (sind  so gross)  wie  der  Kopf  eines  mittelgrossen Manns"  'S. 4^;  —  ha(a  avaibyü  st>r^yS Ytj.  85;  —  slärqmia  sptntB.mainya'vanqm
```


## [2026-09-14T03:12:40.495Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==146' IEC.txt | head -40; echo \"=== grep axtar ===\"; grep -n \"axtar\\|akhtar\" IEC.txt | head -10"
}
```


### [2026-09-14T03:12:41.469Z] TOOL RESULT

```
) lémbos, s. ‘skiff; Gk. elakhás; G Lung ‘dash, lunge’; OCS lígúkúu; Li. leñňñgvas, lengvüs; Latv. liegs
elnguhros, ios (variant of above) Gk. elaphrós; OHG lungar; OE tunger, lungre (adj. & adv.)
elntà, os, is ‘tree; timber’. Cf. WP I, 152 & 437. Variant: lenta, is Hitt. alanc(a) (a kind of wood); Gk. láte ‘pine’; Alb. lândë, lëndë “tree, timber, mate- rial, substance’; Br. lann juniper’; ON lind “lime-tree? beside lundr ‘copse, tree’; Pol. cf. tet ‘stick’; Cz. la? (“lath”, infl. by G Latte); Li. lentà “board”; Latv. ? lieta “thing, matter’. O-gde in G Lande ‘stake, pale’; Ge-länder ‘banister’; MHG lander, f. ‘palings’; Swiss Lande ‘shaft of cart
el"uos (elouos), variant of alouos, q.v. Cf. olouos. Laryngalism may account for fluctua- tion: e:a. Cf. es?or, me$-, al?snis, etc. Hitt. cf. halluwas ‘deep’; OHG ëlo, gs élawes *yellow', etc.
elnā (elnà), see Inā, olenio “ell, elbow’. WP
-élis, ios — emos
10
20
25
30
35
40
45
240
I, 156
-em, an adverbial extn. Skt. cf. (diva) naktam ‘by (day and) night’; Lat. noct-im, aut-em, salt-em, etc.; Gk. ai-én “for ever
eme, mé, mene, mné acc. prn. ‘me’. WP II, 236 Skt. OPer. màm, -mà; Av. ma; Per. man; Oss. màn, mà; Gk. emé, me; Alb. mue, mua; Lat. me; Ir. mé, emph: mi-se; W mi; Br. mé, em; OE me; OCS mene; OCz. mé, mne; Li. cf. mane; Latv. cf. mani, man. Cpds. with *-8e: Gk. emé + ge; Venet. cf. me-go; Go. cf. mi-k; Hitt. cf. ammuk. Cf. with *-$h-: Skt. amahyam; Arm. indz; Lat. mi-hi (dat.)
emeios (emoios, emos) *my; mine'. WP II, 236 Arm. im, gs imo; Gk. emós, e (beside the gen. sg. emeio, emeü, emoü, moü); Alb. i im, f. e ime & e eme; Lat. meus, a; Ir. mo; W my, fy (beside predic. ym, and adj. mau); Br. ma, va; OCS moj, a; OPr. mais
emnos, ios (emn-) (?) “fine, minute” Skt. anuh ‘tiny, subtle, delicate’; Gk. heanós, id. (variant: *esmnos ?); Cz. jemny, id. (If the radical is *em-, m- ‘take’, cf. R iz-ja&Cij, ‘dainty’, fr. iz + ím. Thus Preobr. ESRJa)
emo Omg, mö) ‘take, get. Cf. iem-, iom-. WP I, 124 Arm. cf. imanam, aor. imacaj “understand”; (Tokh. cf. ? ime ‘thought: Lat. imago & imitor VWind. LEDT); Lat. emo, ére beside ad-imo (: em! ‘take’; eme! *buy'); cf. auris ima ‘flap of the ear; Umb. emps, for *emptos, pp. ‘taken’; MIr. do-emim ‘protect’; air-imim ‘receive’; fo-emaim, id. (fr. *do-, *pri-, *upo-?); OCS imo, jeti “hold, seize’; emljo, imati ‘take’; OCz. jmám ‘have’; Li. imu, imti, aor. emiau (: Lat. emi) ‘take’; Latv. cf. n-emu, -emt, id. (The apparent reduction in the initial vowel is traditionally regarded as ‘shva se- cundum’, here represented as "Í-. Cf. que- tuores, sked-)
emoi, see moi; emoios, see emeios
emos ‘holder’. Cf. emó & am- (2), amn-. Cf. WP I, 124 Lat. cf. auris ima ‘flap of the ear’; Cz. -jem, cpds.; OCS cf. néámü (*mute', for *ne-emo-)
241
empis, io “insect; swarm’. WP I, 125 Gk. empís; OHG imbi ‘swarm of bees; MHG imbe, OE imbe, id.; LG imm, wf. ‘bee’; Cz. cf. jepice (^mayfly', fr. *empitio); Pol. cf. jetka, id. (fr. a type *emptika); ? cf. Finn. (LW?) ampia- (^wasp- in cpds.)
emtio- (emtio, mtio-) ‘taking’. Cf. em- (m-) Lat. emptio; OCS jetije; Slovene ječa ‘prison’: Li. iicios, f. pl. ‘struggle’; imæius “bribable”
en, eni ‘in’. Cf. endo. WP I, 125 Arm. i, en-; Tokh. in-, y-; Lyc. ünü; Myc. & Gk. ení, eín, en; Lat. in; Osc. Umb. -en; Olr. en, in beside ind; OBr. en, in, i; Sequ- anian in; Br. en, é beside enn; W Cor. yn; Go. OHG OE in: ON í; OCS vü (beside R jà- in jà-beda ‘slander’; (zero-gde in) Li. i, i, ing ('into', fr. *n); in-, px. in in-imant ‘including’; im-buvys “lodger?; Latv. ie-, px. (fr. *n)
-en (ablative suffix) Arm. cf. dnen (durs) "out of doors’; Osc. Umb. -en (w. abl. “from? as in imad-en ‘
=== grep axtar ===
3841:oster- (osteren-, ster-) ‘star’. WP II, 635. (A Semitic LW according to E. Schrader. Cf. Akkad. istar, Can. Syr. Astarte, AStoroth, a goddess of fertility. Cf. also Basque izar ‘star and Kabyle ithri, id.) Skt. cf. str-bhih ‘by the stars; Romani Cheren ‘star’; Av. stare, acc. stárom beside axtaro, id., Per. sitare, axtar; Tokh. eren, B on, sCirin, beside cCirye; Hitt. asteras, sittar; Gk. astér, gs. asté- ros beside ástron; (LW in Lat. astrum); Lat.
```


## [2026-09-14T03:12:47.094Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>3700 && NR<3900 && /^[0-9]{3}$/ {print NR\": \"$0}' IEC.txt | head -20; echo ---; sed -n '3841p' IEC.txt | cut -c1-1500"
}
```


### [2026-09-14T03:12:48.132Z] TOOL RESULT

```
3713: 252
3725: 253
3743: 254
3752: 255
3769: 256
3780: 251
3800: 258
3813: 259
3830: 260
3842: 261
3857: 262
3868: 263
3878: 264
3889: 265
---
oster- (osteren-, ster-) ‘star’. WP II, 635. (A Semitic LW according to E. Schrader. Cf. Akkad. istar, Can. Syr. Astarte, AStoroth, a goddess of fertility. Cf. also Basque izar ‘star and Kabyle ithri, id.) Skt. cf. str-bhih ‘by the stars; Romani Cheren ‘star’; Av. stare, acc. stárom beside axtaro, id., Per. sitare, axtar; Tokh. eren, B on, sCirin, beside cCirye; Hitt. asteras, sittar; Gk. astér, gs. asté- ros beside ástron; (LW in Lat. astrum); Lat.
```


## [2026-09-14T03:12:57.889Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1\\.53 STAR\\|STAR$\\|1.53\" SYN.txt | head -10"
}
```


### [2026-09-14T03:12:58.969Z] TOOL RESULT

```
691:1.53 1.54
1669:1.53 MOON Grk.  cedjvn Goth. ména Lith. ménuo, ménulis NG  devyapt (cedrv7 lit.) ON mani (poet.), tungl Lett. ménesis Lat. lina Dan. maane ChSl. luna, mésgct It. luna Sw. mane SCr.  mjesic Fr. lune OE mona Boh. _mésic Sp. -luna ME mone Pol.  ksigzyc Rum. lund NE moon Russ. luna Ir. ésce (luan) Du. maan Skt. (mGs-), candra-, ¢a- Nir. gealach, ré (éascd) OHG wmédno ¢cin-, etc. W. Ueuad, lloer MHG mane Av. mah- Br. loar NHG mond
1691:1.54 STAR
1706:1. IE *ster-, orig. disputed. The old deriv. fr. IE *ster- ‘spread out’, as first in pl. ‘the scattered ones’ = ‘stars’, may seem colorless, but no more so than, e.g. that of several words for ‘moon’ fr. ight, brightness’ (1.53). Walde-P. 2.635 f. (with refs.). Or (to me less like- ly) old IE (!) loanword fr. Akkad. tstar ‘Venus’. Ipsen, IF 41.179 ff. Feist 448 (with refs.; add Wackernagel-Debrun- ner, KZ 67.161 fr.).
1838:1. IE *tem-, *temes-, etc. in sbs. for ‘darkness’ and adjs. for ‘dark’. Walde- P. 1.720 ff. Ernout-M. 1027f. REW 8648, 4484. Weigand-H. 1.535. Briick- ner 65.
2571:3. mama, amma, etc. Walde-P. 1.53, 2.221. For ‘mother’, Grk. nauun (also ‘srandmother’), Lat. mamma _ (also ‘grandmother’ and ‘nurse’), It. mamma, Fr. mama, NE mamma, etc., familiar in nearly all the European languages, in some as reg. word for ‘mother’. Cf. also Lett. mdsa ‘sister’, Lith. mosa ‘hus- band’s sister’, OHG muoma ‘aunt’, later ‘niece’ or ‘cousin’ (NHG muhme).
2667:NHG gatte, whence fem. gattin, fr. MUG gate ‘companion’, here also Du. gade now used mostly for ‘wife’ : MLG gaden ‘be suitable’, OE gegada ‘com- panion’, td gedere ‘together’, Goth. ga- dilligs ‘cousin’, etc. Walde-P. 1.531 ff. Weigand-H. 1.628. Franck-v. W. 172.
2957:ON amma ‘grandmother’, pet name of the amma type (above, p. 94). Walde-P. 1.53.
3112:5. Lat. amita ‘father’s sister’, deriv. of pet name of the amma type (above, p. 94). Hence, with extension at the expense of matertera, OF r. ante (> ME, NE aunt), Fr. tante (> Du., NHG., Dan. tante) with t variously explained, and with dim. suffix Rum. matusd. Walde-P. 1.53. REW 4024, Wartburg 1.89.
3277:4. Goth. gadilligs : OE gedeling ‘com- panion’, t0 gedere ‘together’, MHG gate ‘companion’ (NHG gatte ‘husband’), etc. Walde-P. 1.531 ff. Feist 178 f.
```


## [2026-09-14T03:13:01.294Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1691,1715p' SYN.txt"
}
```


### [2026-09-14T03:13:01.357Z] TOOL RESULT

```
1.54 STAR
a dorip, Razor Goth. stairné Lith.  Zvaigidé Lat. stella, aie ON _ sijarna Lett.  zvaigzne
It. stella’ Paes Dan. _ sijerne ChSl. © zvézda
Fr. toile Sw. —stjdirna SCr.  zvijesda
Sp. estrella OE sleorra Boh. hvézda
Rum.  stea ME sterre Pol. gwiazda
Ir, retglu, rind NE star Russ. zvezda
Nir, realt : Du. ster Skt. star-, ta: @-
W. en OHG - sterro, sterno Ay. star-
Br. steredenn vee slérne
stern
| | | | | | | | / 4
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
56 SELECTED INDO-EUROPEAN SYNONYMS
1. IE *ster-, orig. disputed. The old deriv. fr. IE *ster- ‘spread out’, as first in pl. ‘the scattered ones’ = ‘stars’, may seem colorless, but no more so than, e.g. that of several words for ‘moon’ fr. ight, brightness’ (1.53). Walde-P. 2.635 f. (with refs.). Or (to me less like- ly) old IE (!) loanword fr. Akkad. tstar ‘Venus’. Ipsen, IF 41.179 ff. Feist 448 (with refs.; add Wackernagel-Debrun- ner, KZ 67.161 fr.).
Grk. aornp, aorpov, NG dorépr fr. dim. form; Lat. stélla (fr. *stér-lz; otherwise Ernout-M.) and astrum (fr. Grk. aorpov), It. stella, Fr. étoile, Rum. stea, fr. stélla, but Sp. estrella by mixture with astrum; W. seren, Br. sterenn, steredenn; Goth. stairnd, OE steorra, etc., all the Gme. forms; Skt. star- (Vedic) and tara-, Av. star-; Arm. ast?; Hitt. astiras; Toch. A $ren, nom. pl. (SSS 3, ftn.; Lane, Lan- guage 21.28).
2. Ir. rétglu, MIr. réila, NIv. réalt, epds. of rét ‘thing’ (prob.) and glan ‘pure, bright’ (cf. dat. pl. rétglannaib). Otherwise Pedersen 1.485 (cpd. of rét ‘star’, but where is this quotable?), 2.47.
Tr. rind (neut.) ‘star’, same word as rind (masc.) ‘point, top’, perh. : Grk, metpw ‘pierce’, etc. Pedersen 1.37.
3. Lith. Zvaigzdé, ChSI. zvézda, etc. (all the Balto-Slavic forms; also OPruss. swaigstan rendering NHG schein), clear- ly belong together, though the Baltic forms point to an initial palatal, the Slavic to an initial velar (explained by Meillet as dissimilation). Briickner 165 assumes forms with voiced consonants parallel to IE *kweit- ‘bright’ in ChSl svétu ‘light’, etc. (Walde-P. 1.470). But the words have all the appearance of imitative orig., like Lith. Zvigti ‘squeal’, Ch8l. zvizdati, Pol. gwizdaé ‘whistle’, etc. (Berneker 365), in which the consonant relations are precisely the same. A shift of application from sound to light is entirely possible. Cf. NE flash, of imitative orig. and once used only of the rushing or splashing of the sea, now only with reference to fire or light (NED s.v.).
4. Other Skt. words besides star-, tara-, are mostly such as are applied to any heavenly body, as bha- fr. bha- ‘shine’, jyotis- fr. jyut- ‘shine’, naksatra- of obscure orig.
1.55 LIGHTNING
Grk. dorparq Goth. lauhmuni Lith. Zaibas
NG ss dorpar ON elding Lett.  zibens
Lat. fulgur, fulgor Dan. lyn ChSl. mliintjt, bliscanije It. lampo, baleno, folgore Sw. blizt SCr. munja, blijesak Fr. éclair + OE léget(u), liget(u) Boh.  blesk
```


## [2026-09-14T03:13:08.596Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"steorra\\|stairno\\|stella\" WLD_Bd2_pages.txt | head -10; echo \"=== pdf page tags near ===\"; grep -n \"turus\\|turuš\\|torpere\\|torpeo\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T03:13:08.731Z] TOOL RESULT

```
42171:Boisacq 948) lat. stella „Stern'‘ (^sttr~{e)la, Deminutiv) bret. sterenn, corn,
42176:Name          einer         Gottheit);   got.   stairno,       ahd. sterno,         anord. stjarna        „Stern‘‘
42177:und ahd. as. sierra, ags. steorra „Stern‘' (aus ^ster-ero^ ? s. zuletzt Brugmann
=== pdf page tags near ===
14412:aber auch der E-eife", matutinus „morgendlich", maturus „quod neque ci-
41898:     Ohne S-: torpeo^ -ere „steif, starr, gefiihllos, betaubt sein" (= abg. n-trz-
41980:Yf. LEWb.^ u. torpeo,
```


## [2026-09-14T03:13:11.429Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'NR>41850 && NR<42200 && /\\[pdf page/ {print NR\": \"$0}' WLD_Bd2_pages.txt | head; echo \"---\"; sed -n '41890,41915p' WLD_Bd2_pages.txt; echo \"=== star ===\"; sed -n '42160,42185p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T03:13:12.500Z] TOOL RESULT

```
---
*, jSich     strafifen^'),   sterptis   „auf seinem Rechte bestehn‘^ („sich versteifen'*'),
stmplis „Hinterteil des Pferdes", stiirpUs ,,Biirzel eines Vogels''.
  Alb. sterps „unfnichtbar" (s. zur Bed. auch ster- „unfruchtbar“ G. Meyer                ;


Wb. 416 f.); ir. serrach „Fullen“ (Pedersen KG. 94; wohl nicht eig. „heran-
wachsend" oder „noch unfruchtbar", sondern von den unverhaltnismaBig
langen, stelzenahnlichen Beinen).
     Ohne S-: torpeo^ -ere „steif, starr, gefiihllos, betaubt sein" (= abg. n-trz-
pUi         oder   = russ. toropBh:     abzulehnende Vergleiche Vf. LEWb.^
                                          s.   iiber
s.   V.;    falsch auch Collitz Praet. 42)
                                        lit. tirpstu, tirpti .,erstarren oder ein-
schlafen, gefiihllos werden, von einem gewissen Krampf (oder Blutleere)
der Glieder", lett. €%rpt „vertauben, erstarren";
   abg. ^itr^pHi ,,erstarren", russ. terpnnt’b „ds., auch vor Furcht", r.-ksl.
terplii} ,,avorr]o6g'\ r. terpkij          „herb, sauer; russ. toropeih, otoropUh „besturzt
^'erden, aus der Fassung kommen'*' (usw., s. Mikl. EWb. 355, 359, Persson 438,
954) Trautmann Bsl. Wb. 325, klr. toropa („steifer =) unbeholfener Mensch",
slov. trap ,,DummkopP; auf der Bed. „starr, steif                      =
                                                       ausdauernd sein" be-
ruht wohl abg. b^peti „leiden", russ. terpeih ds., slov. trpjes „Geduld" (usw.,
s. Mikl. EWb, 355; Persson Beitr. 43Sj: hieher, nicht nach Strekelj AfslPh.

28, 502 f. zu trep-           „wenden“ oder nach Yf. LEWb.^                u.       trepidus zu   trep-
„trippeln", auch slav. "^torpiti (kaus.) in c. trdpiti, apoln. tropic „qualen", russ.
=== star ===
widerraten die andern Sprachen, trotz Meillet Bull. soc. lingu. 59, LXV, der
auch fiir lat. stHla einer Gdf. ^sUl-na zuneigt; s. noch Brugmann Grdr. II
^1,339); gr. dar^p,         doxqoyv^ darpam „Stern“, doxgov ,, Stern, Gestirn^
(daraus lat. asfntm), wozu wohl als Zss. mit cojt-, ojt-, s. J. Schmidt KZ.
32, 335 Anm. 1.), doregom'], oxegoni], doxgam/j „Blitz, Wetterleuchten“, oxe-
goip /uyvvg „der Rauch, in dem Funken sternengleich flimmern”, doxgdjixco,
oxgdjiza)       „blitzen,        funkeln^',     doxegojitjx^g,            doxEgoTiaiog     jjBlitzeschleuderer
(Zeus)“    noch Boisacq 92); ohne anl. s- (wie ai. farak, tara) xsgecov g. pL,
              (s.

mit metr. Dfehnung xeigea, xelgeoiv „Gestime'' (Curt. 206, Schulze, Quep. 205,
Boisacq 948) lat. stella „Stern'‘ (^sttr~{e)la, Deminutiv) bret. sterenn, corn,
                        ;                                                              ;


sterenn (pL steyr), cymr. seren „Stern“ (aber kaum gall. Dirona^ Sirona
Name          einer         Gottheit);   got.   stairno,       ahd. sterno,         anord. stjarna        „Stern‘‘
und ahd. as. sierra, ags. steorra „Stern‘' (aus ^ster-ero^ ? s. zuletzt Brugmann
IF. 33, 303; das Formans dann etwa nach "^iifero- „die Oberen^^?), afries.
stera „Stern“.
   Ygl. im allgemeinen Cuttius^ 206, Fick I ^ 146, 334, 570, 11^313.                                          Seit
Kuhn KZ. 4, 4 denkt man z. T. an Yerwandtschaft mit ster- „ausbreiten“
als „die am Himmel ausgebreiteten, ausgestreuten'^ oder (nach Wood aaO.)
als    „Funken“             (vgl. engl. spark   „Funke“ lat. spargers) unter Benifung auf
                                                                   :
```


## [2026-09-14T03:13:19.505Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"SETAREH\\|SETARE\\|SITAREH\\|TORSH\\|TOROSH\" ARY_latin_index_pages.txt | head -10; echo \"=== fa ===\"; grep -n \"ستاره\" ARY_pages.txt | head -8; echo \"=== torsh fa ===\"; grep -n \"ترش\" ARY_pages.txt | head -8"
}
```


### [2026-09-14T03:13:19.598Z] TOOL RESULT

```
=== fa ===
1306:ضمناً چون این واژه‌ها از راه بازسازی به وجود آمده‌اند. طبق رسم معمول جلو آنها یک ستاره (:)
10138:۴ | ستاره
=== torsh fa ===
50:جنوبی و مرکزی و همچنین در استرالیاگبترش داده است. ضمناً در گذشته زبان مردم آذرپایجان و
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
113:ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این
118:هند و باختر اروپاگسترش داشته باشد. ۲- بررسی‌های اغیر نشان می‌دهد که زبان‌های هند و اروپایی
158:(8۸ظ۸ 283/7391818 ۸1۸1/1724) اگر حوزه‌ی گسترش یکه زبان زیاد شود» گویش‌های
200:گسترش سریح قبایل ترکك نشان می‌دهد که سرعت تهاجم و تصاحب می‌تواند :
253:نقشه‌ی گسترش هند و اروپائیان از خاستگاه (بخش سیاه) به سوی باختر وخاور و جنوب از حدود 5۴۰۰۱
292:بوده‌اند و تحرکك و تفوقی که سوارکاری و ترابری به آنها داده عامل بزرگی در گسترش آنها بوده
```


## [2026-09-14T03:13:21.913Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '10125,10160p' ARY_pages.txt; echo \"=== page tag ===\"; awk 'NR>10050 && NR<10160 && /\\[pdf page/ {print NR\": \"$0}' ARY_pages.txt"
}
```


### [2026-09-14T03:13:22.927Z] TOOL RESULT

```
بونانی 0788/0): 571۸۸ 9 ۶005908
لاتین (47100): 521۸2۸ ,5۳38 6 (5217882) نمی ده ی نا
فرانسه (ل۳87): 5۳ 5 (5711838) :002/5
اسپانبابی (52۸۷/8): ۸ 7 (8717838) دوه
ایتالیابی (۷ل۵ارلم7): 55۸ برهان قاطع + ۱.۹
رومانی (81014۸(0): 1 ان
بادداشت: 8 :
۱ بازگشت به: سپید.
‌ نت ۲ واژه‌های رومانس (برگرفته از لاتین) در این فهرست در آغاز چم "گوی" و "فلک" را داشتند و بعداً چم آنها
"کره‌ی سماوی نا جنرافباقی یز شد.
اوستایی (4۷587424): هد کردی (780/57): 51
پهلوی (۳۸]47): 0 ,8۳۳ بلرچی (اتلنال۸): 7 ,187۳
[pdf page 343]
۴ | ستاره

افغانی (پشتو) (/(۸۴0//۸): راون هلندی (0076): 7

سانسکریت (54(/577): اسلاوی کهن (۲7ا؟ /86نا7ا) 010):

,0715۷۳3۸ 537 ,8۷7۸ ۱ 0 : و اد

ارمنی (0ها(474415): 5۳17۸ روسی ((15314ا#): ی 9

گونیک (ع/0077): ۲7۲۷۳118 ,۷۷115175 لیتوانی (4(14(۷لا72/ل): ی

ایسلندی کهن (/(3۸01۸۸۳۸ صا۵): 71 517۷130715

17۷7811 لترنی (لتی) ((ماتمم: 171

ساکسونی کهن ((440 صا0): 17

فریزی کهن (/(۲-54 صا0): از پسگشت‌ها اد راد اد یا

آلمانی کهن ((05801۸ ۲7/0 ا0): 11۷۷12 9 ۶006

آلمانی (08۸17): 5 23 (۷3178) ی
=== page tag ===
10053: [pdf page 340]
10084: [pdf page 341]
10109: [pdf page 342]
10137: [pdf page 343]
```


## [2026-09-14T03:13:28.191Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '10109,10126p' ARY_pages.txt"
}
```


### [2026-09-14T03:13:28.238Z] TOOL RESULT

```
[pdf page 342]
۹
سپهر | ۳۴۳
ا
انگلیسی کهن (نْعلا8۸/0 ۰:02 بآ8ت8 8 97307۸
اسلاوی کهن (7۴بما؟ لام طا0):
زا لد این پسگشت‌ها ازش هت دای
لهستانی (نلقداهه): 5 0 ۶0/0520
, چکه (لع285ح): 5۸737 8 (8۸3) :02۵
۱ اسلوا کی (8101/7): ۵ 8 (03013) اد
لیتوانی (142 هلان[ 7ل): ک 2 6 (101) ۸2
۱ لدرنی (لتی) (/(/47۲): 50578 ,501081 لغت‌نامه دهخدا : ۷ و ۲۰۷۴
پروسی کهن ۶۸۹5۵۸7 ۵ا0).
پارسی پاستان (228۵1۵49 0ا0): 9۳118۸ پرتغالی (۳077010852): 3
پهلری (۳۸۶۲۲): ۰ 1188178 ,571118
سانسکریت (54(/8577): )2 پسگشت‌ها شک دا
بونانی 0788/0): 571۸۸ 9 ۶005908
لاتین (47100): 521۸2۸ ,5۳38 6 (5217882) نمی ده ی نا
```


## [2026-09-14T03:13:33.585Z] TOOL CALL #49: Bash

```json
{
 "command": "head -40 tools/fetch_source.py"
}
```


### [2026-09-14T03:13:33.638Z] TOOL RESULT

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


## [2026-09-14T03:13:39.735Z] TOOL CALL #50: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82st%E1%B8%97r\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%B7%D8%B1%D9%84%D8%A7%D8%A8\" \\\n \"https://www.etymonline.com/word/astrolabe\" \\\n \"https://www.etymonline.com/word/star\" \\\n \"https://www.etymonline.com/word/torpedo\" \\\n \"https://www.etymonline.com/word/starve\" \\\n \"https://www.etymonline.com/word/start\" \\\n \"https://www.etymonline.com/word/starch\" \\\n \"https://www.etymonline.com/word/cholesterol\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 480, roots Ster 2 / Ster 3\" ; done 2>&1 | tail -20"
}
```


### [2026-09-14T03:13:48.657Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8e299ca1fff83e80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53c8253c4d7dd056.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9648cfcf780fe2c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f1678e023adfd69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2bbabfed71711ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0acb0fd4fab041e9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3675237d329b3ff8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7abaea7022c9353.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/781941fc9a5bf776.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95ed5510245f7ff7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bee868b21be47a11.txt
```


## [2026-09-14T03:13:50.772Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### setare\"; grep -n -A12 -i \"^Persian\" 8e299ca1fff83e80.txt | head -40"
}
```


### [2026-09-14T03:13:50.836Z] TOOL RESULT

```
### setare
```


## [2026-09-14T03:13:53.048Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 8e299ca1fff83e80.txt 9648cfcf780fe2c4.txt 4f1678e023adfd69.txt 53c8253c4d7dd056.txt; echo ====; grep -n -i \"etymolog\" -A8 8e299ca1fff83e80.txt | head -40"
}
```


### [2026-09-14T03:13:53.139Z] TOOL RESULT

```
Exit code 1
 9912 8e299ca1fff83e80.txt
 8593 9648cfcf780fe2c4.txt
12230 4f1678e023adfd69.txt
 4969 53c8253c4d7dd056.txt
35704 total
(eval):1: === not found
```


## [2026-09-14T03:13:54.622Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,80p' 8e299ca1fff83e80.txt"
}
```


### [2026-09-14T03:13:54.684Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D8%B1%D9%87
FETCHED: 2026-09-14T03:13:42Z
STATUS: 200
TITLE: ستاره - Wiktionary, the free dictionary

ستاره - Wiktionary, the free dictionary 

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
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection 

 1.1 
 Etymology 1 

 1.1.1 
 Noun 

 1.1.1.1 
 Derived terms 

 1.2 
 Etymology 2 

 1.2.1 
 Noun 

 1.3 
 Further reading 

 2 
 Persian
```


## [2026-09-14T03:13:56.224Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '80,220p' 8e299ca1fff83e80.txt"
}
```


### [2026-09-14T03:13:56.269Z] TOOL RESULT

```
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
 Usage notes 

 2.4.2 
 Derived terms 

 2.4.3 
 Descendants 

 2.5 
 Proper noun 

 2.6 
 See also 

 Toggle the table of contents 

 ستاره 

 26 languages 

 Azərbaycanca 
 Català 
 Eesti 
 فارسی 
 Français 
 हिन्दी 
 Magyar 
 한국어 
 Kurdî 
 Latina 
 ລາວ 
 Lietuvių 
 Malagasy 
 Nederlands 
 Norsk bokmål 
 Polski 
 Português 
 Română 
 Русский 
 Slovenščina 
 Gagana Samoa 
 Shqip 
 Тоҷикӣ 
 Türkçe 
 Tiếng Việt 
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

 See also: ستارہ 

 Ottoman Turkish
 [ edit ] 

 Etymology 1
 [ edit ] 

 Borrowed from Classical Persian ستاره ( sitâra , “ star; fate ” ) .

 Noun
 [ edit ] 

 ستاره • ( sitare ) ( plural ستارگان ) 

 ( astronomy ) star , a luminous celestial body made up of plasma 
 Synonyms: اختر ( ahter ) , نجم ( necm ) , یلدز ( yıldız ) 

 ( figuratively ) one's star , fortune , fate , chance , destiny 
 Synonym: اختر ( ahter ) 

 an open tent, a pavilion

 Derived terms
 [ edit ]
```


## [2026-09-14T03:13:57.916Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '220,300p' 8e299ca1fff83e80.txt"
}
```


### [2026-09-14T03:13:57.979Z] TOOL RESULT

```
 [ edit ] 

 ستاره سوخته ( sitare suhte , “ unfortunate ” ) 
 ستاره‌دان ( sitaredan , “ astrologer ” ) 
 ستاره‌سز ( sitaresiz , “ unfortunate, unlucky ” ) 
 ستاره‌لو ( sitareli , “ starry; lucky, fortunate ” ) 

 Etymology 2
 [ edit ] 

 Borrowed from Classical Persian ستاره . Compound of سه ( “ three ” ) +‎ تاره ( “ stringed ” ) .

 Noun
 [ edit ] 

 ستاره • ( sitare ) 

 a three-stringed lute

 three-dice backgammon

 Further reading
 [ edit ] 

 Çağbayır, Yaşar ( 2007 ), “ sitare2 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 4265 

 Kélékian, Diran ( 1911 ), “ ستاره ”, in Dictionnaire turc-français ‎ [1] (in French), Constantinople: Mihran, page 665 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Stella”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [2] , Vienna, column 1595 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ ستاره ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [3] , Vienna, column 2547 

 Redhouse, James W. ( 1890 ), “ ستاره ”, in A Turkish and English Lexicon ‎ [4] , Constantinople: A. H. Boyajian, page 1039 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: ستاره 

 Wikipedia fa 

 ستارگان ( sitāragān  / setâregân ) 

 Alternative forms
 [ edit ] 

 ستار ( satâr, setâr ) , استاره ( estâre ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂eHs- 

 Proto-Indo-European *-tḗr 

 Proto-Indo-European *h₂stḗr 
 Proto-Indo-Iranian *Hstā́ 
 Proto-Iranian *Hstā́ 
 Old Persian 𐎠𐎿𐎫𐎼 ( a-s-t-r /⁠star-⁠/ ) 
 Middle Persian [script needed] ( stʾlk' /⁠stārag⁠/ ) 
 Persian ستاره 

 Inherited from Middle Persian [script needed] ( stʾlk' /⁠stārag⁠/ ) , from Old Persian 𐎠𐎿𐎫𐎼 ( a-s-t-r /⁠star-⁠/ ) , from Proto-Iranian *Hstā́ , from Proto-Indo-Iranian *Hstā́ , from Proto-Indo-European *h₂stḗr , from *h₂eHs- + *-tḗr . Cognate with English star .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /si.taː.ˈra/ 

 ( Dari, formal ) IPA ( key ) : [sɪ.t̪ʰɑː.ɾá] 

 ( Dari, formal ) IPA ( key ) : [sɪ.t̪ʰɑː.ɾá] 
 ( Kabuli ) IPA ( key ) : [sɪ.t̪ʰɑː.ɾá] 

 ( Hazaragi ) IPA ( key ) : [si.t̪ʰɔː.ɾá] 

 ( Iran, formal ) IPA ( key ) : [se.t̪ʰɒː.ɹé] 

 ( Tajik, formal ) IPA ( key ) : [si.t̪ʰɔ.ɾá]
```


## [2026-09-14T03:14:10.238Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Middle Persian\\|Proto-Iranian\\|Etymology\\|sour\" 9648cfcf780fe2c4.txt | sed -n '1,60p'"
}
```


### [2026-09-14T03:14:10.293Z] TOOL RESULT

```
70: Etymology 
95: Etymology 
109: Etymology 
248: Etymology
251: From Proto-Iranian *tr̥fšah . Compare Persian ترش ( torš ) .
267: sour 
284: Arabic spelling of turş ( “ sour ” ) 
289: Etymology
299: sour 
313: Etymology
316: Ultimately inherited from Proto-Iranian *tr̥fšah .
361: sour , tart ( tasting acidic ) 
422: ( Masarm , Deh Sarv , Kuzarg ) sour 
430: Central Kurdish terms inherited from Proto-Iranian 
431: Central Kurdish terms derived from Proto-Iranian 
442: Persian terms derived from Proto-Iranian 
443: Persian terms inherited from Proto-Iranian
```


## [2026-09-14T03:14:12.161Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '305,370p' 9648cfcf780fe2c4.txt"
}
```


### [2026-09-14T03:14:12.215Z] TOOL RESULT

```
 References
 [ edit ] 

 Pashtoon, Zeeya A. ( 2009 ), “ ترش ”, in Pashto–English Dictionary , Hyattsville: Dunwoody Press, page 184 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Ultimately inherited from Proto-Iranian *tr̥fšah .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /tu.ˈruʃ/ , /ˈturʃ/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.ɾʊʃ] , [t̪ʰʊɹʃ] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.ɾʊʃ] , [t̪ʰʊɹʃ] 
 ( Kabuli ) IPA ( key ) : [t̪ʰʊ.ɾʊʃ] , [t̪ʰʊɹʃ] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰu.ɾuʃ] , [t̪ʰuɹʃ] 

 ( Iran, formal ) IPA ( key ) : [t̪ʰo.ɹoʃ] , [t̪ʰoɹʃ] 

 ( Tajik, formal ) IPA ( key ) : [t̪ʰu.ɾuʃ] , [t̪ʰuɹʃ] 

 Rhymes: -uʃ , -urʃ 

 Readings

 Classical reading ? 

 turuš, turš

 Dari reading ? 

 turuš, turš

 Iranian reading ? 

 toroš, torš

 Tajik reading ? 

 turuš, turš

 Audio ( Iran ) : ( file ) 

 Adjective
 [ edit ] 

 ترش • ( turuš  / toroš or turš  / torš ) 

 sour , tart ( tasting acidic ) 

 morose , stern 

 fermented 

 Derived terms
 [ edit ] 

 nouns
```


## [2026-09-14T03:14:20.118Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -B2 -A14 \"Etymology\" 4f1678e023adfd69.txt | sed -n '1,90p'"
}
```


### [2026-09-14T03:14:20.176Z] TOOL RESULT

```
71-
72- 2.2 
73: Etymology 
74-
75- 2.3 
76- Noun 
77-
78- 2.3.1 
79- Declension 
80-
81- 2.3.2 
82- Descendants 
83-
84- 2.4 
85- Further reading 
86-
87- 3 
--
94-
95- 3.2 
96: Etymology 
97-
98- 3.3 
99- Pronunciation 
100-
101- 3.4 
102- Noun 
103-
104- 3.5 
105- References 
106-
107- Toggle the table of contents 
108-
109- اسطرلاب 
110-
--
194- سطرلاب ( suturlab ) 
195-
196: Etymology
197- [ edit ] 
198-
199- Borrowed from Arabic أَسْطُرْلَاب ( ʔasṭurlāb ) , which derives from Ancient Greek ἀστρολάβος ( astrolábos ) .
200-
201- Noun
202- [ edit ] 
203-
204- اسطرلاب • ( usturlab ) ( definite accusative اسطرلابی ( usturlabı ) , plural اسطرلابلر ( usturlablar ) ) 
205-
206- astrolabe , an astronomical and navigational instrument for gauging the altitude of the Sun and stars 
207-
208- Declension
209- [ edit ] 
210-
--
545- سطرلاب ( suturlāb ) , اصطرلاب ( usturlāb, asturlāb, isturlāb ) , صطرلاب ( suturlāb ) , صلاب ( sulāb, sullāb ) , استرلاب ( usturlāb, asturlāb, isturlāb ) , سترلاب ( suturlāb ) 
546-
547: Etymology
548- [ edit ] 
549-
550- Borrowed from Arabic أَسْطُرْلَاب ( ʔasṭurlāb ) , which derives from Ancient Greek ἀστρολάβος ( astrolábos ) .
551-
552- Pronunciation
553- [ edit ] 
554-
555- ( Classical Persian ) IPA ( key ) : /ʔus.tur.ˈlaːb/ , /ʔas.tur.ˈlaːb/ , /ʔis.tur.ˈlaːb/ 
556-
557- ( Dari, formal ) IPA ( key ) : [ʔʊs.t̪ʰʊɾ.lɑːb] 
558-
559- ( Iran, formal ) IPA ( key ) : [ʔos.t̪ʰoɹ.lɒːb̥] , [ʔæs.t̪ʰoɹ.lɒːb̥] 
560-
561- ( Tajik, formal ) IPA ( key ) : [ʔus.t̪ʰuɾ.lɔb]
```


## [2026-09-14T03:14:28.602Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in AFM.txt TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt FVQ.txt LKT.txt PHN.txt; do echo \"--- $f\"; grep -n \"سطرلاب\\|astrolab\\|Astrolab\" $f | head -4; done; echo \"=== PLA ===\"; grep -n \"سطرلاب\\|strolab\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5"
}
```


### [2026-09-14T03:14:29.790Z] TOOL RESULT

```
--- AFM.txt
--- TAD.txt
--- ARB_mo3rb.txt
--- ARB_abdulraheem.txt
--- FVQ.txt
--- LKT.txt
410:'Spinne'.  Wegen  der  Ähnlichkeit  der sich  kreuzenden  Meridiane  und  Parallel- kreise am  Astrolabium  hiefa  ein  Teil desselben  sp.  alhancahit,  frz.  alancabuth. [Devic  DEt  5.    Laramens  Rem  4.
2157:'BewegUches  Lineal  am  Astrolabium'; hieraus  sp.  alidada  'Diopterlineal',  frz. alidade  'dass.',  auch  'Lineal',  it.  alidada, dtsch.  Alhidade  physikalischer  Fachaus- druck zur  Bezeichnung  eines  wesent- lichen Teiles  optischer  Meßinstrumente. Es  kann  vermutet  werden,  daß  das  bis- her unerklärte  Wort  Theodolith  auf dieses  Grundwort  zurückgeht.  [DE  140. Devic  DEt  22/23.    Lammens  Rem  15.
--- PHN.txt
=== PLA ===
```


## [2026-09-14T03:14:38.269Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c2bbabfed71711ae 0acb0fd4fab041e9 3675237d329b3ff8 c7abaea7022c9353 781941fc9a5bf776 95ed5510245f7ff7 bee868b21be47a11; do echo \"##### $f\"; python3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\ni=t.find('Advertisement')\nprint(t[:120].replace('\\n',' '))\nm=re.search(r'\\n\\s*(\\w[\\w\\-]*)\\s*\\(.{0,4}\\)\\s*\\n', t)\n# just print a middle chunk\nprint(t[1000:3200].replace('\\n',' ')[:1800])\nEOF\ndone"
}
```


### [2026-09-14T03:14:39.516Z] TOOL RESULT

```
##### c2bbabfed71711ae
URL: https://www.etymonline.com/word/astrolabe FETCHED: 2026-09-14T03:13:47Z STATUS: 200 TITLE: Astrolabe - Etymology, O
t labhate , rabhate "seizes;" Old English læccan "to seize, grasp;" Greek lazomai "I take, grasp;" Old Church Slavonic leca "to catch, snare;" Lithuanian lobis "possession, riches"). Related: Lemmatical .   *ster- (2)    Proto-Indo-European root meaning "star." Buck and others doubt the old suggestion that it is a borrowing from Akkadian istar "venus." The source of the common Balto-Slavic word for "star" (Lithuanian žvaigždė , Old Church Slavonic zvezda , Polish gwiazda , Russian zvezda ) is not explained.   It might form all or part of: aster ; asterisk ; asterism ; asteroid ; astral ; astro- ; astrobiology ; astrobleme ; astrognosy ; astroid ; astrolabe ; astrolatry ; astrology ; astromancy ; astronaut ; astronomy ; AstroTurf ; constellation ; disaster ; Estella ; Esther ; instellation ; interstellar ; lodestar ; star ; stardust ; starfish ; starlet ; starlight ; starry ; stellar ; stellate .   It might also be the source of: Sanskrit star- ; Hittite shittar , Greek aster "star," with derivative astron ; Latin stella , Breton sterenn , Welsh seren "star."   Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   More to explore   scale    14c., "series of registering marks; marks laid down to determine distance along a line," (in Chaucer's description of the astrolabe...   sextant    instrument for determining latitude in navigation and surveying, 1620s, from Modern Latin sextans, which is said to have been first used in this sense c. 1600 by Danish astronomer Tycho Brahe, from Latin sextans "a sixth, a sixth part," from sex "six" (see six). So called because   apprehension    late 14c., "perception, comprehension," from Old French apreension "comprehension, something learned" or directly from Latin apprehensionem (
##### 0acb0fd4fab041e9
URL: https://www.etymonline.com/word/star FETCHED: 2026-09-14T03:13:47Z STATUS: 200 TITLE: Star - Etymology, Origin & Me
xon sterro , Old Frisian stera , Dutch ster , Old High German sterro , German Stern , Old Norse stjarna , Swedish stjerna , Danish stierne , Gothic stairno ). This is from PIE root *ster- (2) "star."   Used originally of the apparently fixed celestial bodies, which is the restricted modern sense. But it also was used of planets and comets, as preserved in falling star (late 15c.) "meteor;" morning star "Venus at dawn" (Old English), etc.   The astrological sense of "influence of planets and zodiac on human affairs" is recorded from mid-13c., hence "person's fate as figured in the stars" (c. 1600; star-crossed "ill-fated," literally "born under a malignant star," here meaning "planet," is from "Romeo and Juliet," 1592; star-struck is by 1787). The astrological sense also is in expressions such as My stars! , thank (one's) stars , both 1590s.   The meaning "leading performer" is from 1824, originally of actors and singers; the sense of "outstanding performer in a sport" is by 1916; star turn "principal act or song in a show" is by 1898.   Stars as a ranking of quality for hotels, restaurants, etc. are attested by 1886, originally in Baedecker guides. Sticker stars as rewards for good students are recorded by 1977. A brass star as a police badge is recorded from 1859 (New York City).   The astronomical star-cluster is from 1870. Star-shower "meteor shower" is by 1818. To see stars when one is hit hard on the head is from 1839.   star (v.)    1590s, "mark with a star," from star (n.). By 1718 as "set with stars, adorn with star-like ornaments." By 1827 as "mark with an asterisk."   In reference to actors, singers, etc., "perform the lead part," by 1824, in reference to actors in ensembles who performed only in plays where they had leading roles.   This abominable American h
##### 3675237d329b3ff8
URL: https://www.etymonline.com/word/torpedo FETCHED: 2026-09-14T03:13:47Z STATUS: 200 TITLE: Torpedo - Etymology, Origi
e to a floating mine; the self-propelled version is from c. 1900. Torpedo-boat is by 1810: a small, swift boat from which a torpedo is operated. Torpedo tube , from which it is launched, is by 1893. An expert in their use was a torpedineer (1881).   Of the adjective forms, torpedinal , torpedinous (18c.) were used of the fish, torpedic , torpedoic of the munition.  also from 1520s    torpedo (v.)    "attack with torpedoes, destroy or sink (a ship) by a torpedo," 1874, from torpedo (n.). Also used late 19c. in reference to blowing open oil wells. The figurative sense is attested by 1895. Related: Torpedoed ; torpedoing .  also from 1874    Entries linking to torpedo    *ster- (1)    Proto-Indo-European root meaning "stiff."   It might form all or part of: cholesterol ; redstart ; starch ; stare ; stark ; stark-naked ; start ; startle ; starve ; stere ; stereo- ; stern (adj.); stork ; strut ; torpedo ; torpid ; torpor .   It might also be the source of: Greek stereos "solid," sterizein "to support," sterphnios "stiff, rigid," sterphos "hide, skin;" Sanskrit sthirah "hard, firm," Persian suturg "strong;" Lithuanian storas "thick," strėgti "to become frozen;" Old Church Slavonic trupeti , Lithuanian tirpstu, tirpti "to become rigid;" Old Church Slavonic strublu "strong, hard," staru "old" (hence Russian stary "old"); Old English starian "to stare," stearc "stiff, strong, rigid," steorfan "to die," literally "become stiff," styrne "severe, strict."   Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   More to explore   grinder    Old English grindere "one who grinds (grain);" agent noun from grind (v.). Meaning "molar tooth" is late 14c. (Old English had grindetoð). Meaning "machine for milling" is from 1660s; of person
##### c7abaea7022c9353
URL: https://www.etymonline.com/word/starve FETCHED: 2026-09-14T03:13:47Z STATUS: 200 TITLE: Starve - Etymology, Origin 
iple storfen ), etymologically "become stiff," from Proto-Germanic *sterbanan "be stiff, starve" (source also of Old Frisian sterva , Old Saxon sterban , Dutch sterven , Old High German sterban "to die"). This is reconstructed to be from an extended form of PIE root *ster- (1) "stiff."   The conjugation became weak in English by 16c. The word seems to have been used especially of lingering or wasting deaths, and came to especially mean "die of cold" (14c.); "die from want of nourishment, suffer from hunger" (mid-15c.). The transitive meaning "afflict or kill with hunger" is recorded by 1520s (Middle English starve of hunger in the same sense is from early 12c.; hunger-storven "dead from hunger" is from late 14c.).   The "die of cold" sense is marked "Now chiefly Eng." in Century Dictionary (1902) and "Now only North. " in OED (1989). Wedgwood (1878) notes that "In the Midland Counties to clem is to perish from hunger ; to starve , to suffer from cold."   "Dear me," continued the anxious mother, "what a sad fire we have got, and I dare say you are both starved with cold. Draw your chair nearer, my dear. ..." ["Mansfield Park," 1814]    German cognate sterben "to die" retains the original sense of the word, but the English has come so far from its origins that starve to death (1910) is now common. The verb is not found in Scandinavian, but compare Old Norse stjarfi "tetanus."   Entries linking to starve    die (v.)    mid-12c., dien, deighen , of sentient beings, "to cease to live," possibly from Old Danish døja or Old Norse deyja "to die, pass away," both from Proto-Germanic *dawjan (source also of Old Frisian deja "to kill," Old Saxon doian , Old High German touwen , Gothic diwans "mortal"), from PIE root *dheu- (3) "to pass away, die, become senseless" (source also of 
##### 781941fc9a5bf776
URL: https://www.etymonline.com/word/start FETCHED: 2026-09-14T03:13:48Z STATUS: 200 TITLE: Start - Etymology, Origin & 
suddenly," the sense extended by c. 1300 to include "awaken suddenly or abruptly; flinch or recoil in alarm," and by 1660s to "cause to begin acting or operating."   The meaning "begin to move, leave, or depart; enter upon action" (without implication of suddenness) is from 1821. The connection probably is from sporting senses ("force an animal from its lair," late 14c.). The transitive sense of "set in motion or action" is from 1670s; specifically as "set machinery in action" by 1841.   Related: Started ; starting . To start in "begin" in any sense, is by 1873, American English; to start something "cause trouble" is by 1915, American English colloquial. To start over "begin again" is from 1912. In running, starting-line is so called by 1855; starting-block by 1937.   start (n.)    late 14c., "an involuntary movement of the body, a sudden jump," from start (v.). The meaning "act of beginning to move or act, a setting out in some course or action" is by 1560s; that of "act of setting in motion, signal to begin" is from c. 1600.   Many senses are modern; in sports-writing it is synecdoche for "a game" (by 1944). The meaning "act of beginning to build a house" is from 1946, as in the statistical term housing starts . The meaning "opportunity at the beginning of a career or course of action" is from 1849, from the notion of a lead or advantage in setting out (in a race or contest). It has been paired regularly with finish (n.) from at least 1839.  also from late 14c.    Entries linking to start    jump-start (v.)    also jumpstart , "to start a car engine using battery booster cables," by 1970; see jump (n.) + start (v.). The sense of jump is that in the jump-spark ignition system, attested from 1883 in gas-lighting, from c. 1902 as a common way to start an automobile; henc
##### 95ed5510245f7ff7
URL: https://www.etymonline.com/word/starch FETCHED: 2026-09-14T03:13:48Z STATUS: 200 TITLE: Starch - Etymology, Origin 
pasty substance made from flour and used to stiffen or whiten cloth," mid-15c., sterche , from starch (v.). The figurative sense of "stiffness and formality of manner" is recorded from 1705.  also from mid-15c.    Entries linking to starch    starchy (adj.)    1778, "resembling or abounding in starch," from starch (n.) + -y (2). Figurative sense of "stiff, precise, formal in manner" is by 1828. Related: Starchily ; starchiness .   *ster- (1)    Proto-Indo-European root meaning "stiff."   It might form all or part of: cholesterol ; redstart ; starch ; stare ; stark ; stark-naked ; start ; startle ; starve ; stere ; stereo- ; stern (adj.); stork ; strut ; torpedo ; torpid ; torpor .   It might also be the source of: Greek stereos "solid," sterizein "to support," sterphnios "stiff, rigid," sterphos "hide, skin;" Sanskrit sthirah "hard, firm," Persian suturg "strong;" Lithuanian storas "thick," strėgti "to become frozen;" Old Church Slavonic trupeti , Lithuanian tirpstu, tirpti "to become rigid;" Old Church Slavonic strublu "strong, hard," staru "old" (hence Russian stary "old"); Old English starian "to stare," stearc "stiff, strong, rigid," steorfan "to die," literally "become stiff," styrne "severe, strict."   Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   More to explore   amyl    hydrocarbon radical, 1850 (amyle), from Latin amylum "starch," from Greek amylon "fine meal, starch," noun use of neuter...So called because it was first obtained from the distilled spirits of potato or grain starch (though it also is obtained...English amyl meant "starch, fine flour."...   grouch    He carried a Facial Expression that frightened little Children in Street Cars and took all the Starch out of sentimental...   malt    "g
##### bee868b21be47a11
URL: https://www.etymonline.com/word/cholesterol FETCHED: 2026-09-14T03:13:48Z STATUS: 200 TITLE: Cholesterol - Etymolog
ing to cholesterol    sterol (n.)    "white, crystalline substance discovered in gallstones," 1913, abstracted from cholesterol .   *ghel- (2)    Proto-Indo-European root meaning "to shine;" it forms words for "gold" (the "bright" metal), words denoting colors, especially "yellow" and "green," also "bile, gall," for its color, and a large group of Germanic gl- words having to do with shining and glittering and, perhaps, sliding. Buck says the interchange of words for yellow and green is "perhaps because they were applied to vegetation like grass, cereals, etc., which changed from green to yellow."   It might form all or part of: arsenic ; Chloe ; chloral ; chloride ; chlorinate ; chlorine ; chloro- ; chloroform ; chlorophyll ; chloroplast ; cholecyst ; choler ; cholera ; choleric ; cholesterol ; cholinergic ; Cloris ; gall (n.1) "bile, liver secretion;" gild ; glad ; glance ; glare ; glass ; glaze ; glazier ; gleam ; glee ; glib ; glide ; glimmer ; glimpse ; glint ; glissade ; glisten ; glister ; glitch ; glitter ; glitzy ; gloaming ; gloat ; gloss (n.1) "glistening smoothness, luster;" glow ; glower ; gold ; guilder ; jaundice ; melancholic ; melancholy ; yellow ; zloty .   It might also be the source of: Sanskrit harih "yellow, tawny yellow," hiranyam "gold;" Avestan zari "yellow;" Old Persian daraniya- , Avestan zaranya- "gold;" Greek khlōros "greenish-yellow color," kholos "bile, gall, wrath;" Latin helvus "yellowish, bay," Gallo-Latin gilvus "light bay;" Lithuanian geltonas "yellow;" Old Church Slavonic zlutu , Polish żółty , Russian zeltyj "yellow;" Latin galbus "greenish-yellow," fellis "bile, gall;" Lithuanian žalias "green," želvas "greenish," tulžis "bile;" Old Church Slavonic zelenu , Polish zielony , Russian zelenyj "green;" Old Irish glass , Welsh and Breto
```


## [2026-09-14T03:14:55.730Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN constellation\"; grep -n \"constellation,  n\" KLN_1966.txt | head -2; echo \"### KLN disaster\"; grep -n \"disaster,  n\" KLN_1966.txt | head -2; echo \"### KLN asterisk\"; grep -n \"asterisk,  n\" KLN_1966.txt | head -2; echo \"### KLN stereo\"; grep -n \"stereo-,  combining\\|stereo-, \" KLN_1966.txt | head -3; echo \"### KLN cholesterol\"; grep -n \"cholesterol\" KLN_1966.txt | head -3; echo \"### KLN starch/stare/strut/starve/start\"; grep -n \"starch,  n\\|stare,  intr\\|strut,  intr\\|starve,  intr\\|start,  intr\" KLN_1966.txt | head -6"
}
```


### [2026-09-14T03:14:55.906Z] TOOL RESULT

```
### KLN constellation
8870:constellation,  n.  —  Late  L.  constellatid,  ‘a  col¬ lection  of  stars’,  fr.  constelldtus.  See  prec.  word
### KLN disaster
11587:Derivative:  disassociat-ion,  n. disaster,  n.,  misfortune,  calamity.  —  F.  desastre, fr.  It.  disastro  (but  with  the  substitution  of  the F.  prefix  des-  for  It.  dis-).  It.  disastro  is  a  back
### KLN asterisk
3739:asteria,  n.,  a  gem  reflecting  a  six-rayed  light ( Greek  antiq.)  —  L.,  fr.  Gk.  aaxcpia,  ‘a  pre¬ cious  stone’,  prop.  fern,  of  daxipLo;,  ‘starred, starry’,  used  as  anoun,  fr.  aaxvjp,  ‘star’.  See  Aster, asterisk,  n.,  the  figure  of  a  star  (the  printing mark  *).  —  Late  L.  asteriscus,  fr.  Gk.  daxEptaxo;, dimin.  of  aaxr)p,  ‘star’.  See  Aster, asterism,  n.,  a  system  of  stars,  a  constellation.  — Gk.  daxepiapd;,  fr.  danrjp,  ‘star’.  See  Aster  and -ism.
### KLN stereo
36609:starr,  ‘stiff’,  Star,  ‘cataract  of  the  eye’),  ON. storr,  ‘proud’,  OHG.  storren,  MHG.  storren,  ‘to stand  out,  project’,  Goth,  andstaurran,  ‘to  be obstinate’.  All  these  words  derive  fr.  I.-E.  base *ster-,  ‘strong,  firm,  stiff,  rigid’.  Cp.  starch, stark,  start,  n.,  starve,  stem,  stork,  stour,  adj. consternation,  starosta,  stereo-,  sterigma,  sterile, strenuous,  strut.
36737:Sterculiaccae,  n.  pi.,  a  family  of  plants,  the  choc¬ olate  family  (bot.)  —  ModL.,  formed  from prec.  word  with  suff.  -aceae. stere,  n.,  a  cubic  meter.  —  F.  stere,  fr.  Gkaxe- p£o?,  ‘solid’.  See  stereo-, stere-,  form  of  stereo-  before  a  vowel, stereo,  n.  —  Abbreviation  of  stereotype, stereo-,  before  a  vowel  stere-,  combining  form meaning  ‘solid,  firm’.  —  Gk.  oxepeo-,  fr. oxEpEcu;,  ‘firm,  hard,  solid,  stiff’,  fr.  I.-E.  base *ster-,  ‘stiff,  rigid’.  See  stare  and  cp.  sterile.  Cp. also  the  second  element  in  cholesterol, stereobate,  n.,  a  solid  substructure  without  col¬ umns.  —  Compounded  of  stereo-  and  Gk. [ixxYjC,  ‘that  which  steps  or  treads’,  which  is  rel. to  pdot?,  ‘a  stepping,  that  on  which  one  steps’. See  base,  n.,  and  cp.  stylobate.
36753:steric,  adj.,  spatial.  —  Formed  with  adj.  suff.  -ic fr.  Gk.  oTEpeop,  ‘solid’.  See  stereo-, sterigma,  n.,  stalk,  filament  (bot.)  —  ModL. sterigma,  fr.  Gk.  axr, ptypa,  ‘a  support',  from the  stem  of  axyjpi^av,  ‘to  prop,  support’,  prop, ‘to  make  firm’,  which  is  rel.  to  oxspeo?,  ‘firm, solid;  stiff;  hard’.  See  stereo-  and  -ma. sterile,  adj.,  1)  barren;  2)  free  from  living  germs.
### KLN cholesterol
5050:biosis,  n.,  vitality  (biol.)  —  Gk.  ploiaig,  ‘way  of life’,  fr.  piog,  ‘life’.  See  bio-  and  -osis. biosterin,  n.,  product  from  cod-liver  oil.  —  Coined fr.  Gk.  pto?,  ‘life’  (see  bio-),  cholesterol  and chem.  suff.  -in.
7507:choledocho-,  combining  form  meaning  ‘contain¬ ing  bile’.  —  See  prec.  word, choler,  n.  —  ME.  coler,  colere,  fr.  OF.  colere  (F. colire),  ‘choler,  anger',  fr.  L.  cholera,  fr.  Gk. yoXepa,  'bilious  diarrhea,  cholera’,  fr.  yolrh  also y6Xo c,  ‘gall,  bile’,  which  is  rel.  to  y'k'joc,  ‘greenish- yellow  color’,  yko^eiv,  ‘to  be  green’,  yluicib', ‘greenish-yellow,  pale  green,  green,  fresh’,  and cogn.  with  Avestic  zara-,  ‘gall,  bile’,  L.  fel, OSlav.  zluci,  Russ,  zelc.’,  Lith.  tulzis  (metathesis for  *zultis ),  Lett,  zults,  OE.  gealla,  galla,  ‘gall, bile’,  fr.  I.-E.  base  *ghel-,  *ghel-,  ‘to  shine;  yel¬ low,  yellowish  green,  green’.  See  yellow  and  cp. gall,  ‘bile’.  Cp.  also  next  word,  Chloe,  Chlorella, chlorine,  Chloris,  and  the  second  element  in melancholy,  Chrysochloris,  Echinochloa.  Cp.  also the  second  element  in  bezoar. cholera,  n.  —  L.  cholera,  fr.  Gk.  xoXepa,  ‘bilious diarrhea’,  fr.  yoTcq,  ‘gall,  bile'.  See  prec.  word, choleraic,  adj.,  related  to,  or  resembling,  cholera. —  Formed  from  prec.  word  with  suff.  -ic. choleric,  adj.  —  MF.  (=  F.)  choleriqtie,  fr.  L. cholericus,  fr.  Gk.  yokepixo^,  fr.  ydkipdi,  (see choler  and  -ic) :  first  used  by  Chaucer. Derivatives:  choieric-ly,  adv.,  choieric-ness,  n. cholesterine,  n.,  cholesterol.  —  See  next  word and  chem.  suff.  -ine.
7508:cholesterol,  n . ,  a  fatty  alcohol  ( biochem .)  —  Form¬ ed  fr.  F.  cholesterine,  a  word  coined  by  the French  chemist  Miehel-Eugene  Chevreul  (1786- 1889),  and  -ol,  a  suff.  denoting  an  alcohol.  F. cholesterine  is  formed  fr.  Gk.  yoklj,  ‘gall,  bile’, and  aTEpeoe,  ‘solid’  (see  chole-  and  stereo-),  and is  so  called  because  it  was  originally  found  in gallstones.
### KLN starch/stare/strut/starve/start
36607:starch,  n.  —  ME.  sterche,  starche,  back  forma¬ tion  fr.  sterchen,  ‘to  starch’,  fr.  OE.  stercan,  ‘to stiffen’,  fr.  stearc,  ‘stiff’.  Cp.  G.  Starke,  ‘strength ; starch’,  and  see  stark.
36608:Derivatives:  starch,  adj.  and  tr.  v.,  starch-ed, adj.,  starch-ed-ly,  adv.,  starch-ed-ness,  n.,  starch- y,  adj.,  starch-i-ly,  adv.,  starch-i-ness,  n. stare,  intr.  and  tr.  v.  —  ME.  staren,  fr.  OE.  sta- rian,  ‘to  look  fixedly  at’,  rel.  to  ON.  stara, MLG.,  MDu.  staren,  Du.  staren,  OHG.  staren, MHG.  starn  (whence  G.  starred),  ‘to  look  fixed¬ ly  at’,  and  to  MHG.  starren,  ‘to  be  stiff,  to stiffen’,  whence  G.  starren,  of  s.m.  (whence
36617:start,  intr.  and  tr.  v.  —  ME.  sterten,  ‘to  start’,  rel. to  OE.  sturtian,  styrtan,  ‘to  leap  up’,  OFris. stirta,  ‘to  fall,  tumble’,  MDu.  sterten,  sturten, storten,  Du.  storten,  ‘to  rush,  fall’,  OHG.  stur- zen,  MHG.  sturzen,  also  stiirzen,  G.  stiirzen, ‘to  hurl,  throw,  plunge’;  of  uncertain  origin. Cp.  startle.
36625:starve,  intr.  v.,  to  die  from  hunger;  tr.  v.,  to  cause to  starve.  —  ME.  sterven,  ‘to  die’,  fr.  OE.  steor- fan,  rel.  to  OFris.  sterva,  Du.  sterven,  OS. ster'ban,  OHG.  sterban,  MHG.,  G.  sterben,  ‘to die’,  and  to  ON.  stjarfi ,  ‘tetanus’,  and  cogn.  with Gk.  OT^pcpvtoi;  (Hesychius),  ‘stiff,  rigid’,  axsp- 90?,  ‘hide,  skin’,  OSlav.  strublu,  ‘strong, hard’.  All  these  words  derive  fr.  I.-E.  *sterbh-, a  -Wi-cnlargement  of  base  *ster-,  ‘stiff,  rigid’. See  stare  and  cp.  torpedo,  torpid.
37097:strut,  intr.  v.,  to  walk  pompously.  —  ME.  strou- ten,  ‘to  swell  out,  strut’,  fr.  OE.  strutian,  ‘to stand  stiffly,  be  rigid’,  rel.  to  Dan.  strutte, strude,  Swed.  strutta,  MHG.,  G.  strotzen,  ‘to  be puffed  up,  be  swelled’,  LG.  strutt,  ‘rigid’,  MHG. striuzen,  ‘to  contend,  resist’.  ME.  strout,  MHG. stray,  G.  Straufi,  ‘fight’.  All  these  words  are traceable  to  I.-E.  base  *ster-,  ‘strong,  firm,  stiff, rigid’,  whence  also  OE.  starian,  ‘to  look  fixedly at’.  See  stare  and  cp.  words  there  referred  to. Derivatives:  strut,  n.,  the  act  of  strutting, strutt-er,  n.,  strutt-ing,  n.  and  adj.,  strutt-ing-ly, adv.
```


## [2026-09-14T03:15:04.174Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LEW torpeo\"; grep -n \"torpeo\" LEW_1910.txt | head -4; echo \"### LAT torpeo\"; grep -n \"torpeo\" LAT.txt | head -4; echo \"### LEW stella\"; grep -n \"stella\" LEW_1910.txt | head -3; echo \"### LAT stella\"; grep -n \"^stella\\|stella, \" LAT.txt | head -4"
}
```


### [2026-09-14T03:15:04.286Z] TOOL RESULT

```
### LEW torpeo
### LAT torpeo
64888:torpeo, -es, -ere: itre engourdi (sens physique et moral). An -
### LEW stella
### LAT stella
9217:stellation du Cbien; nom d*un poisson, cbien de mer; d'un crochet
12105:et des conpos 4 s latins: cistula (dejA dans Pl.); cistella, M.L.i950a,
17110:stella, ex quibus a riuo communi aquam quisque in suum fundum ducit,
21457:fenestro; fenestella, noa propre; non d'une porte de Soae, et d'un
```


## [2026-09-14T03:15:06.748Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64885,64900p' LAT.txt; echo \"=== stella entry ===\"; grep -n \"stëlla\\|stella:\" LAT.txt | head -5"
}
```


### [2026-09-14T03:15:06.824Z] TOOL RESULT

```
Derives: torno,-ds: fayonner au tour, tourner (depuis Cic.). Pan-
roman (a remplaci torquet, uerto ), M.L.O794; v.angl. tyrnan', tornatilis,
tornator, tornatura (tous tardifs et techniques).
torpeo, -es, -ere: itre engourdi (sens physique et moral). An -
cien, deja dans Plaute, Am.33,5. — Usuel, classique.
Dirivis: torpor : engourdissement, torpeur; torporo,-as (rare, Turp.,
Lact.); torpidus: engourdi; toT"^)edo:(torpille (cf.M.L.879 6a); tor¬
pesco, -is, -pul-, torpefacio (Non.183,5: torporauit pro torpefecit).
Cf.v.sl.(serbe) u-trupeti "evvapxo«j 0 ai", v.sl.(Suprasliensis)
u-truposta "torpuerunt", russe terpnut' "se raidir", et lit. tirpstU,
tirpti "se raidir, perdre conaaissance, s'engourdir".
torqueo, —es (auquel s'est substitui torquo, torco dans les 1.
romanes, v.M.L.8798, cf .mordere, etc.), torsi, tortum, torquere:
faire tourner, tourner; tordre, en particulier "tordre les membres,
torturer, tourmenter" (sens physique et moral); dans la 1. militaire
"faire tourner une arme avant de la laacer* brandir". Ancien (Cat*)*
=== stella entry ===
5604:astella: v. assis.
```


## [2026-09-14T03:15:11.173Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1628,1636p' HUB.txt; echo ---; sed -n '5110,5118p' HUB.txt; echo ---; sed -n '6566,6574p' HUB.txt"
}
```


### [2026-09-14T03:15:11.247Z] TOOL RESULT

```
Oder Hrsati (vgl. ksql *ziehen' = krs). Die iranische
Wurzel war d^rah^ schwach trs, inchoat. trs,
385. Zu turns *sauer etc. vgl. auch afgh. triv, f. tarva
sauer. Es gelingt mir nicht, die verschiedenen
Dialektformen aus einer iran. Grundform lautgesetz-
lich abziileiten. Liesse sich iran.*^r/sa- (= B,v.Hrpsa')
ansetzen, so k5nnte man mit Fr. Miiller, WZKM.
8, 93 sehr wohl ksl. trufMlm o/iKpa^ vergleichen.
386. Dazu skr. paguti^p *Vieh stehlend' und KZ. 25, 311.
---
von ctturpat = ap. ^dt^pata-? (zd. atarepata-, gT!ATpondTjjc);
np. buzurg gross* = ap. vazrka-, arm. vzurk, vzruk (vgl.
§ 53) ; Surndan continue fundere , surrdn {sarran) 'continue
fluens' {surr- aus Sf«-?), vgl. sdridan 'fluere' (alle kaum
belegt), skr. ksar *fliessen'; turns *sauer' aus t^fsa-? (siehe
p. 186).
Nach Analegie von sumurdan (vgl. skr. smrta-): pr.
sumaram (vgl. skr. smarayati), supurdan: pr. sipciram ist
gebildet azurdan *kranken' (Sal. Shuk. Gram. p. 15, Bloch-
---
(idg. pek^U'); sarm *Scham' = zd. fsarema-^); ap. fr ist im
An- und Inlaut stets = np. fr {far u. s. w.), nur im Aus-
laut = rf {barf *Schnee' = zd. vafra-), siehe Kap. 32.
Ap. / ist also geschwunden im Anlaut vor s, Viel-
leicht auch inlautend in turvs *sauer (aus *trus -= Hrusf
= Hrufs = >/sa-? vgl. H. 385 und oben p. 48).
§ 82. Persisches / wird von den Armeniern, deren
Sprache den /-Laut nicht kennt, in verschiedener Weise
wiedergegeben :
```


## [2026-09-14T03:15:17.746Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ster- \\|^ster-,\\|‘stiff\" IEC.txt | head -20"
}
```


### [2026-09-14T03:15:17.802Z] TOOL RESULT

```
7019:kerdos (2) ‘firm, stout, hard”. Alb. cf. (*-&) n-gordh ‘stiffen’, sh-kordh “loosen up’; OE heort, adj. ‘stout-hearted’ (ambig. cf. Kerd-, Krd-); Icel. cf. hirta, v. *chas- tize’; OCS crëdu, adj. ‘firm’
7510:koip- (quoip- ?) (1) ‘harden, dry off, wither’ OCS cf. cépénü ‘rigid’; Cz. cepny ‘stiff; cepe- nét, R cépenét “die off, stiffen'; Li. kaipstu, kaipti beside kaipiniuoti ‘waste away’
7672:kor- “harsh, hard; torture, torment’ Skt. kárjami ‘torment’; Oss. karz, adj. ‘strict’; Alb. cf. n-gardh, v. ‘stigmatize, brand’; ngardhë, f. ‘stigma’; Arm. korcem, kocem, v. (1) ‘beat; ON harka ‘harshness, hardness’; mod. harki ‘dearth’; harka, v. ‘rack, torment’; Du. cf. harkerig ‘stiff, awkward’. (Isophonic are: ON harka (1) ‘scrape’; Sw. harka ‘rake’; Du. (and G fr. LG) barken, v. id. ON also herkja ‘drag oneself along’; Norw. harke, v. ‘hawk, cough’)
7699:koros (2) ‘arrogance, rudeness, bullying, fighting’. (SI. & Balt. ambig. w. influence of type kar-, q.v.) Gk. kóros ‘arrogance’; OCS korü ‘contumely’; Cz. cf. kory ‘stiff; Li. káras ‘war’; Latv. cf. karš, id.
10358:máruos (moruos, mruos) ‘dead, decayed, broken-down'. Cf. mruos, moros, us & moruos. WP II, 276. (Variant mris, io) Ligurian (in Rumansch) marv, -a, adj. ‘stiff with cold'; Olr. marb, Ir. marbh ‘numb, dead’; W marw, Br. maró, Cor. marow dead: OHG maro, gs *marwes ‘rotten, mellow’ beside mu- ruwi ‘mellow, crumbly’; MHG mürwe, wd: G mürbe, id.; Du. murw ‘tender, soft; LG, Sw. mör ‘crumbly, mellow’; Cz. mp ‘dead’; mrva ‘dung’; cf. Srb. mrva ‘crumb’; OCS mrúv-ica, id.; cf. Srb. (vowel?) marva ‘cattle’. (Variant of type mri-, mruio in OHG ei-muria, OE &- mege ‘embers’, if for *aidh-^, and Latv. miris, adj. "dead. cf. Li. mirimas ‘death’. For Fr. morve ‘snot, glanders' see smeruos, à. The variant vocalism seems to be present where two continuants are followed by Si or *-u-, but the evidence is inconclusive. A dative absolute formula occurs in Li. tévui mirus ‘the father having died’. Cf. ON moru-eldr ‘phosphorescence’, lit. ‘dead fire")
14379:qusül- a possible variant for items listed under ksül-, q.v. Cf. further ON syla, tr. & intr. ‘stiffen (with ice)
14673:roghos (1) “peak, point, tip, horn; project- ing”. Cf. rog- (1) and (3) Oss. (long-gde) rag, s. “back, ridge’; MHG rac, gs: rages, adj. ‘stiff, taut’; cf. also rage- hüffe ‘with projecting hips’; (e-gde in) rëgen, sv. 5 ‘stiffen, jut; (o-gde also in) ragen, v. ‘stand out’; OCS rogü, m. “horn, corner’ (pl: rogove & rodzi); Li. rágas, m. “horn, head- land'; Latvian: rags, m. id. (Here possibly also MHG ramme, sf. “battering-ram? beside ram, gs: rammes, sm. ‘ram’; OE ramm, id. if from *roghmos, à). WP I, 482, II 361 & 367
15918:(skrob- or skrab-) (4). (Gmc. only?) MHG schraf, sm. 'tang'; adj. “bitter cold'; Du. schrap, adj. ‘stiff, unmoved'; MLG cf. schravel, adj. ‘sharp, sheer’; Sw. cf. skräpa, v. “look blank, be nonplussed'
17089:srīĝ- “feel cold, shiver’. WP II, 705. (Variant: ri-) Oss. rizin, Dig. rezun, inf. id.; Per. cf. ariz, s. *hoarfrost; Gk. rhigéo, v. ‘shiver’; Lat. (in- tensive fr- for initial r-) frigeo, ere, v. id. (cf. Supt: srág- “berry? for analogy) beside rígeo, ere, v. id. (and 'stiffen); OW, W cf. rhynn, rh?$n, adj. ‘shivering’; m. ‘shiver’ (for expected *ffrynn, fr. *rigno- beside *srigno-); Cor. rynny, inf. ‘shiver’; Cz. stříž(e), f. “newly formed ice; Slovene srež, m. 'hoarfrost. Nominal types include Gk. rhigos, n. “cold; shudder’; Lat. frigus, gs: ons, n. id. beside rígor, oris, m. ‘stiff cold"; Br. frimm, m. (“hoar- frost', fr. *srigmo-. Fr. frimas is of ambig, origin); cf. also Cz. stříž-aha ‘dry frost; Pol. $rezoga “haze?
17194:ON stinnr, adj. ‘stiff, strong’; Sw. stind, adj. ‘stiff, crammed, bursting’
17198:ster-, e-gde of radical str-, q. v. Cf. also stor- *strew, spread”, etc. WP II, 640 Skt. stare, mp. ‘strew’; pp: strtáb; Av. star-, id.; Per. cf. gu-stardan, inf. id.; gu-star, s. ‘spreader (fr. *aue-^); Lat. cf. sterno, Ere, v. id.; cf. ster-cus & -cor, -quilinium, n. ‘dung’; Srb. stérem, stérati, v. ‘stretch’; cf. OIr. sernaim, v. 'strew'. (In the sense of “side”, a possible formant in Gk. ari-sterós, Lat. sini-ster, OHG, OE winister, win-ster, etc.)
17216:sterp- ‘stiff, hard, barren, withered, dead’. (Variant strp-) Alb. shterpë, adj. ‘barren’; f. ‘barren cow’; Rum. substrate sterp, id.; Rumansh sterp, m., sterpa, f. (briar, dead twig’. Substr. Ligurian); OHG, MHG stërbo, stërbe, wm. ‘plague’; OE steorfa, wm. ‘plague; carrion’; Icel. stjar- fur, adj. ‘stif? beside stirfinn, adj. ‘peevish’; (Gmc. LW in) OCS strüví & strúvo, R steriva ‘carrion’. Cf. WP II, 632. Verbal types in OHG stërban, OE steorfan, sv. 3. ‘die’ and in Li. dial. (z-gde) stirpstù, inf: stifpti, v. ‘grow up, become adult, lit. ‘harden’. The proto- type is uncertain in Arm. t'ormim, v. ‘fade, wither’; t'aram, adj. ‘faded, withered’, perh. from *storp- : *strp-, but cf. ster- above.
17221:steu- (sth-) ‘stiff, solid, stern’. Cf. sthugeros Ir. stuagh, m. (2) 'stalwart'; Fris. stjüch, adj. ‘surly, stubborn'; Du. cf. stiekem, adv. “slily, sneaking’; (z-gde in) G stocken, v. ‘come to a
17239:stibhos (sth-) ‘stiff, hard, tight; crush, cram; mass’. Bee next. WP II, 648 Skt. cf. stibhih, m. ‘tuft, bunch’; Gk. stiphos, gs. -eos, n. ‘compact body of men’; stiphos, m. ‘crowd’; Du. cf. stijven, tr. ‘stiffen, starch’ beside stevig, adj. (solid, firm’: *1:1)
17241:stibhoros, stibhros (sth-) ‘stiff, firm, dense’. Cf. stibhos. WP II, 643 Phryg. stibarós, id.; Gk. stiphrós, id.; Fris. cf. stjurje, stuverje, v. ‘clot, congeal’
17255:stipo, ið (sth-) ‘stiffen’; stip- ‘stiff; stiffness,
17256:rigour, firmness’. Lat. stipo, are, v. ‘cram; enclose’; OE stifian, v. “be stiff; OFris. stivia, id.; LG stīwen, Du. stijven, v. ‘stiffen’; Norw. stive, v. ‘starch’; OCS cf. (?) stíno, steti, v. (congeal, harden’, if fr. *stipno-); Li. cf. stimpu, stipti, v. id. beside stypstu, stypti, intr. ‘stretch oneself’; cf. stiprüs, adj. ‘firm’; Latv. stipa, f. “band, tyre, hoop’. Nominal types in Lat. stips, gs: Stipis, f. ‘coin, profit’; stipes, -itis, m. ‘stake’, beside stipa, f. ‘caulking-tow°: Latv. stipa *band, hoop'; OE. LG stif, Norw. stiv, Du. stijf ‘stiff, rigid’; R stepi, f. ‘steppe’; stepenit'sa, refl. ‘steady oneself; stepennyj, adj. ‘steady’; Li. cf. stipna, f. ‘carrion’; stipinas, m. ‘spoke, strut’. Cf. also Lat. ob-stīpus, adj. ‘stiff at side’ WP II, 647
17297:storg-, cf. stergsos & storgs- EME stark, adj. ‘stiff; MHG starc, gs: starkes, adj. ‘strong; ponderous, evil; sterken, v. ‘strengthen, cheer’; ON sterkr, adj. ‘strong, great; OCS straZí, m. ‘watchman’; straža, f. (^watch', and com. S1.); R storòžiť, v. ‘guard’; Srb. strãžiti, id.; Cz. cf. vý-straha ‘warning’. Cf. storg-
17393:strogos ‘stiff, tight, straight, strict. (See
17473:sthabh- (stabh-) (1) ‘fix, stop, hold, estab- lish’. (Most forms are indistinguishable from those represented under sthab-, q. v.). Cf. WP IL, 624. Verbal forms: Skt. stabhnámi, stabhnómi, pp: stabhitáh, stabdhah, v. “stop, fix, prop’; Oss. cf. stavd, adj. (fat, thick’, fr. *sthabht-); Hitt. staphi, tr. ‘shut’; mp. ‘stop, come to rest’; Ir. cf. sta- bhuighim, v. ‘straddle’; W safaf, 3sg: saif, v. ‘will stand; MHG staben, intr. ‘stiffen’; Du. staven, v. (1) ‘prop’; E to stave off ‘avert’; to stave in, p.t. stove in ‘dent’; ON stafa, v. ‘assign’; stefja, v. ‘prevent’. Nominal types sthabhos, is, å (1) in Tokh. A stop, stow, s. ‘stick’; Gk. staphís, f. (2) ‘delphinium’; Ir. stabh, m. “log; stalwart’; sabh, f. (2) ‘stump, Stick, bolt; W saf, pl. -ion, f. ‘stand, fixity:'; Go. stafs, m. ‘letter; MHG stap, gs: stabes, sm. “post, stick’; LG staff, pl. stäw, m. “staff”; OE staf, pl. stafas, m. id. & "letter; Du. staf, m., staaf, f. “staff, stave’; Sw. cf. stáver, mpl. ‘staves of a barrel; Li. stabas, m. ‘idol’; Latv. stabs, m. 'post, pillar. Ambig. *-b- or *-bh-: OPr. stabis, s. ‘stone’. See next
```


## [2026-09-14T03:15:24.623Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^STAR,\\|STAR, \" SKT.txt | head -3; echo ---; grep -n \"TORPEDO\\|STARVE\\|STARCH\\|STRUT\\|ASTROLABE\\|CONSTELLATION\\|DISASTER\" SKT.txt | head -10"
}
```


### [2026-09-14T03:15:24.793Z] TOOL RESULT

```
18366:Star.  (E.)  M  K  sUrre.  A.S.rfevrru. +  r>u.  sffr;  O.  H.  G.  lUrrv.  Cf.  led. s/Jama,  Dan.  s//^mr,  Swcd.  ttj'rma,  Goth. slainiff',  also  L  sftlia  (for  ster-u/a*),  Gk, AffT^/*,  Com,  sUrtn,  W,  firm^  Ski.  /Jnf. Orig.  acnse  'sprinkler'  of  tight;  (lom V-STAR,  to  sprinkle  (Max  MUllcr).
---
```


## [2026-09-14T03:15:55.536Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,40p' 53c8253c4d7dd056.txt | tail -20; grep -n -i \"star\\|Avestan\\|redirect\" 53c8253c4d7dd056.txt | head -20"
}
```


### [2026-09-14T03:15:55.609Z] TOOL RESULT

```
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

149: star 
260: → ? Proto-Semitic: *ʕaṯtar- ( “ Ishtar, Astarte ” , name of a star goddess ) ( see there for further descendants )
277: ine-pro:Stars
```


## [2026-09-14T03:15:57.728Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,270p' 53c8253c4d7dd056.txt"
}
```


### [2026-09-14T03:15:57.779Z] TOOL RESULT

```
 [ edit ] 

 Apparently from *h₂e(h₁)s- ( “ to burn, glow ” ) +‎ *-tḗr ( agentive nominal suffix ) , so that the result literally meant “glower, shiner”. Compare *h₂éh₁tēr ( “ fire ” ) .

 Noun
 [ edit ] 

 *h₂stḗr   m [ 1 ] [ 2 ] 

 star 

 Inflection
 [ edit ] 

 Athematic, hysterokinetic

 singular

 nominative

 *h₂stḗr 

 genitive

 *h₂strés 

 singular

 dual

 plural

 nominative

 *h₂stḗr 

 *h₂stérh₁(e) 

 *h₂stéres 

 vocative

 *h₂stér 

 *h₂stérh₁(e) 

 *h₂stéres 

 accusative

 *h₂stérm̥ 

 *h₂stérh₁(e) 

 *h₂stérm̥s 

 genitive

 *h₂strés 

 *? 

 *h₂stróHom 

 ablative

 *h₂strés 

 *? 

 *h₂str̥mós , *h₂str̥bʰós 

 dative

 *h₂stréy 

 *? 

 *h₂str̥mós , *h₂str̥bʰós 

 locative

 *h₂stér , *h₂stéri 

 *? 

 *h₂str̥sú 

 instrumental

 *h₂stréh₁ 

 *? 

 *h₂str̥mís , *h₂str̥bʰís 

 Descendants
 [ edit ] 

 Proto-Anatolian: *Hstḗrs Hittite: 𒄩𒀸𒋼𒅕𒍝 ( ḫašterz ) 

 Proto-Armenian: 
 Old Armenian: աստղ ( astł ) Armenian: աստղ ( astġ ) 

 Proto-Celtic: *sterā ( see there for further descendants )

 Proto-Germanic: *sternǭ , *sternô ( see there for further descendants )

 Proto-Hellenic: *astḗr ( see there for further descendants )

 Proto-Indo-Iranian: *Hstā́ ( see there for further descendants )

 ⇒ Proto-Italic: *stērlā ( diminutive ) 
 Latin: stēlla ( see there for further descendants )

 Proto-Tocharian: *ścär-iye- 
 Tocharian A: śre , ( plural ) śren̄ 

 Tocharian B: ścirye 

 → ? Proto-Semitic: *ʕaṯtar- ( “ Ishtar, Astarte ” , name of a star goddess ) ( see there for further descendants )

 References
 [ edit ] 

 ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [1] , 1st edition, Oxford: University Press, →ISBN 

 ^ Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin ( 2008 ), Nomina im indogermanischen Lexikon [ Nouns in the Indo-European Lexicon ]‎ [2] (in German), Heidelberg: Universitätsverlag Winter, pages 348-354 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/h₂stḗr&oldid=92151445 "
```


## [2026-09-14T03:16:02.601Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T03:16:02.676Z] TOOL RESULT

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


## [2026-09-14T03:16:04.602Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-14T03:16:04.652Z] TOOL RESULT

```
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


## [2026-09-14T03:25:37.486Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-480.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SETARE = \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D8%B1%D9%87\"\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82st%E1%B8%97r\"\nW_TORSH = \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%B4\"\nW_ASTOR = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%B7%D8%B1%D9%84%D8%A7%D8%A8\"\nE_ASTROLABE = \"https://www.etymonline.com/word/astrolabe\"\nE_STAR = \"https://www.etymonline.com/word/star\"\nE_TORPEDO = \"https://www.etymonline.com/word/torpedo\"\nE_STARVE = \"https://www.etymonline.com/word/starve\"\nE_START = \"https://www.etymonline.com/word/start\"\nE_STARCH = \"https://www.etymonline.com/word/starch\"\nE_CHOL = \"https://www.etymonline.com/word/cholesterol\"\n\ndoc = {\n \"pdf_page\": 480,\n \"book_page\": 450,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ster 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂stḗr 'star' (older notation *ster-/*aster-)\",\n   \"note\": \"Pokorny's 'ster-2, Meaning: star, Page(s): 1027-1028' is exactly Nourai's root; Watkins/AHD prints it as ster-* 'Star' with the tag '[Pok. 2. ster- 1027.]'. The language label (Indo-European) and the gloss (star) are right; the modern laryngeal notation is *h₂stḗr (Wiktionary, Wodtko-Irslinger-Schneider, NIL 348-354), a hysterokinetic agent noun probably to *h₂e(h₁)s- 'to burn, glow'. Pokorny's own oldest shape 'a-grade *aster-' (Hitt. ḫastērza, Arm. astł, Gk. astḗr) is the laryngeal reflex. The old alternative of a Semitic loan (Akkad. Ištar) is recorded by Klein and Mann but rejected by Buck ('to me less likely') and by Etymonline ('Buck and others doubt the old suggestion'); Nourai rightly keeps the word Indo-European. Nourai's numbering 'Ster 2' happens to coincide with Pokorny's ster-2. One book-level error inside the entry: the Latin box prints 'sterron' (a Germanic form) where Latin has stēlla.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂stḗr «ستاره» که در نگارش قدیم‌تر *ster- یا *aster- نوشته می‌شد؛ پوکورنی در صفحهٔ ۱۰۲۷ همین ریشه را با همین معنی آورده است. شاکلهٔ آغازین با حنجره‌ای (h₂) توجیه‌کنندهٔ صورت‌های دارای a- مانند یونانی astḗr و هیتی ḫastērza است. این احتمال کهن که واژه وام‌واژه‌ای سامی (از اکدی Ištar) باشد امروزه پذیرفته نیست. ادعای نورایی دربارهٔ خود ریشه درست است؛ تنها در جعبهٔ لاتین به جای stēlla صورت ژرمنی sterron چاپ شده که خطای چاپی کتاب است.\",\n   \"sources\": [W_PIE, E_ASTROLABE, E_STAR],\n   \"ref_check\": [\n    {\"ref\": \"POK:1027\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt 'Root / lemma: ster-2 / Meaning: star ... Page(s): 1027-1028' (grep -n 'lemma: ster-2'); the entry lists Hitt. ḫaster-, Arm. astł, Gk. astēr/astron, Lat. stella, Goth. stairno, OHG sterno, OE steorra, Av. acc. stārəm, Skt. str̥bhih — the whole Nourai chart.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 635 f.\", \"stance\": \"supports\",\n     \"note\": \"WLD_Bd2_pages.txt l.42171-42177: 'lat. stella ‚Stern‘ (*stēr-(e)la, Deminutiv) ... got. stairno, ahd. sterno, anord. stjarna ‚Stern‘ und ahd. as. sterra, ags. steorra ‚Stern‘ (aus *ster-ero-?)'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ster-* 'Star'\", \"stance\": \"supports\",\n     \"note\": \"'ster-*, Star. 1. Suffixed form *ster-s- in Germanic *ster-rōn- in Old English steorra, star: STAR. 2. Suffixed form *stēr-lā- in Latin stēlla ... 3. Oldest root form *aster- in Greek astēr ... 4. Iranian stem *stār- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]'\"},\n    {\"src\": \"IEC\", \"where\": \"p. 260 s.v. oster- (osteren-, ster-)\", \"stance\": \"supports\",\n     \"note\": \"Mann p.260: 'oster- (osteren-, ster-) ‘star’. WP II, 635 ... Av. stārē, acc. stārəm beside axtarō, id., Per. sitare, axtar' — the very page Nourai's NOTE cites.\"},\n    {\"src\": \"SYN\", \"where\": \"1.54 STAR, p. 56\", \"stance\": \"supports\",\n     \"note\": \"Buck 1.54: 'IE *ster-, orig. disputed ... Lat. stēlla (fr. *stēr-lā) ... Skt. star- (Vedic) and tāra-, Av. star-'; he calls the Akkadian-loan idea 'to me less likely'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. star, n.\", \"stance\": \"partial\",\n     \"note\": \"Klein: 'ME. sterre, fr. OE. steorra ... cogn. with OI. star- ... Gk. astēr, astron, L. stella (for *ster-la) ... All these words prob. go back to an I.-E. primary form *asterō, which is of uncertain origin. It possibly derives from the name of the evening star called after the Sem. goddess Astarte' — same cognate set, but Klein leaves a Semitic origin open.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"star 2\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan star- m. 'star' is well attested: nom./acc. sg. stārəm, gen. starō, nom. pl. staras-ca, acc. pl. strə́uš, gen. pl. strəm (Yt. 12.25, G. 3.6, Y. 44.3). It continues PIE *h₂stḗr directly, with the regular Indo-Iranian loss of the initial laryngeal-vowel (PIE *h₂stḗr > PII *Hstā́ > Av. star-/stār-) and the Iranian shift of the inherited *r-stem accent, exactly as Sanskrit keeps str̥-bhih 'by the stars' beside tārā-. Nourai's '2' is only his homograph number, distinguishing this star- from the Avestan verb star- 'to strew' (Pokorny's ster-5).\",\n     \"derivation_fa\": \"اوستایی star- / stār- «ستاره» در متن‌های اوستا به صورت‌های stārəm، starō، staras-ca و strə́uš آمده است (بارتولومه، ستون ۱۵۹۶). این ستاک بازماندهٔ مستقیم *h₂stḗr هندواروپایی است که در هندوایرانی به *Hstā́ بدل شده و حنجره از میان رفته است؛ هم‌ریشه با سنسکریت str̥-bhih. عدد ۲ در کتاب فقط برای جداکردن این star- از star- «گستردن» است. ادعای نورایی درست است.\",\n     \"sources\": [W_PIE],\n     \"ref_check\": [{\"ref\": \"POK:1027\", \"status\": \"supports\",\n        \"note\": \"POK ster-2 (p.1027-1028): 'Avestan Akk. Sg. starəm, Gen. starō, Pl. Nom. staras-ca, starō, Akk. strəuš, Gen. strəm, Dat. starə by ō ‘star’'.\"}],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. ~1596 s.v. star-\", \"stance\": \"supports\",\n       \"note\": \"BRT.txt l.26639: '• j., g. ᵃstar- m. ‚Stern‘: ... aiwitō urvisənti staras-ca måsca hvarə (Yt. 12.25)' — Avestan star- 'Stern' with the full paradigm.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ster-*\", \"stance\": \"supports\",\n       \"note\": \"'Iranian stem *stār-' is precisely the Avestan stār-/star- stem Nourai puts here.\"},\n      {\"src\": \"SYN\", \"where\": \"1.54 STAR\", \"stance\": \"supports\", \"note\": \"Buck's table lists 'Av. star-' under 1.54 STAR.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"setâreh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP ستاره setāre (classical sitāra) continues Middle Persian stārag, written stʾylkʹ/stʾlkʹ, itself an -aka-extended Old Iranian *stārakā- beside plain OP a-s-t-r /star-/ and Av. star-. The chain is OIr. *stār- + diminutive/individualising *-aka- > MP stārag > NP sitāra: MP final -g (< *-ka-) is lost in NP and the stem vowel takes the NP -a(h) ending, with the same prothetic i-/e- that western NP gives every st-/sp- onset (cf. sipāh, sitām). Nourai's arrow Avestan > Persian is right in substance (Wiktionary and AHD both derive sitareh from the Old Iranian *stār- stem); the chart merely omits the Middle Persian stage. The chart's NOTE, that IEC:260 derives setâreh and axtar from one root, is literally correct (Mann p.260 lists 'Per. sitare, axtar' under oster-), but axtar is the shakier half: Bartholomae warns that splitting MP apāxtar into apa + axtar is 'falsch', and NP axtar is usually taken from MP axtar 'constellation, planet' whose own prehistory is disputed.\",\n     \"derivation_fa\": \"«ستاره» از فارسی میانهٔ stārag (نگاشتهٔ stʾylkʹ) و آن از ایرانی باستان *stārakā- (ستاک *stār- + پسوند -aka-) است؛ همان ستاکی که در اوستایی star- و در پارسی باستان star- دیده می‌شود. گاف پایانی فارسی میانه در فارسی نو افتاده و «هٔ» پایانی جای آن را گرفته، و الف آغازین همان الف پروتتیک فارسی پیش از خوشهٔ st- است (مانند سپاه، ستم). ادعای نورایی درست است، فقط مرحلهٔ فارسی میانه را نیاورده است؛ دربارهٔ «اختر» که در یادداشت آمده، باید احتیاط کرد زیرا بارتولومه تجزیهٔ apāxtar به apa + axtar را نادرست می‌داند.\",\n     \"sources\": [W_SETARE, E_STAR],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ster-* 'Star', section 4: 'Iranian stem *stār- in Persian sitareh, star: ESTHER.' — exactly Nourai's arrow.\"}],\n     \"consulted\": [\n      {\"src\": \"ARY\", \"where\": \"ستاره, pdf page 343 (printed 344)\", \"stance\": \"supports\",\n       \"note\": \"ARY_pages.txt l.10137 ff. gives ستاره with the cognate列: اوستایی / پهلوی stārag / کردی / بلوچی / سانسکریت / یونانی ASTER / لاتین STELLA.\"},\n      {\"src\": \"IEC\", \"where\": \"p. 260 s.v. oster-\", \"stance\": \"supports\",\n       \"note\": \"'Av. stārē, acc. stārəm ... Per. sitare, axtar' — Mann puts NP sitare straight under the star root.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"ستاره (Persian)\", \"stance\": \"partial\",\n       \"note\": \"'Inherited from Middle Persian stʾylkʹ (stārag), from Old Persian a-s-t-r (star-), from Proto-Iranian *Hstā́, from PIE *h₂stḗr' — same root, but routed through Old Persian/MP rather than Avestan.\"}\n     ]},\n    {\"id\": 3, \"lang\": \"Germanic\", \"words\": \"sterron\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The West Germanic n-stem *sterrōn- (OE steorra, OS/OHG sterro, MDu. sterre, Du. ster) is Watkins' 'suffixed form *ster-s- in Germanic *ster-rōn-'; the geminate -rr- comes from *-rs- (Walde-Pokorny hesitates between *ster-ero- and *sters-), beside the -n-suffixed North/East Germanic *sternō(n) in Goth. stairnō, ON stjarna, OHG sterno, G Stern. Nourai's 'sterron' is therefore a legitimate (if unstarred) citation of the Germanic etymon of English star, not of the Gothic/Nordic type.\",\n     \"derivation_fa\": \"صورت ژرمنی باختری *sterrōn- (انگلیسی کهن steorra، آلمانی باستان sterro) که رر دوتایی آن از *-rs- پدید آمده است؛ در برابر آن گونهٔ نون‌دار *sternō(n) در گوتی stairnō و آلمانی Stern قرار دارد. بنابراین sterron در کتاب صورت درست ژرمنی نیاکان واژهٔ انگلیسی star است و ادعای نورایی درست است.\",\n     \"sources\": [E_STAR],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985: 'Suffixed form *ster-s- in Germanic *ster-rōn- in Old English steorra, star: STAR.'\"}],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 636\", \"stance\": \"supports\",\n       \"note\": \"'got. stairno, ahd. sterno, anord. stjarna ‚Stern‘ und ahd. as. sterra, ags. steorra ‚Stern‘ (aus *ster-ero-? ...), afries. stera'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. star, n.\", \"stance\": \"supports\",\n       \"note\": \"'OE. steorra, rel. to OS. sterro, ON. stjarna ... OHG. sterro, sterno, stern ... Goth. stairnō'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Star\", \"stance\": \"supports\",\n       \"note\": \"Skeat: 'M.E. sterre. A.S. steorra. + Du. ster; O.H.G. sterro. Cf. Icel. stjarna, ... Goth. stairno.'\"}\n     ]},\n    {\"id\": 4, \"lang\": \"English\", \"words\": \"star\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE steorra > ME sterre > NE star, with the normal ME lowering/lengthening of e before r + consonant and the 15c.-16c. shift of ME er to ar (cf. clerk/clark, sterve/starve), so that sterre became star. The word kept the restricted 'fixed celestial body' sense; the astrological 'fate' sense (mid-13c.) and the 'leading performer' sense (1824) are later developments in English only.\",\n     \"derivation_fa\": \"انگلیسی star از انگلیسی کهن steorra و انگلیسی میانه sterre است؛ تبدیل er > ar در سدهٔ پانزدهم و شانزدهم میلادی (همانند sterve > starve) صورت امروزی را پدید آورده است. ادعای نورایی درست است.\",\n     \"sources\": [E_STAR],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; the parent Germanic box cites AHD, which lists STAR under ster-*.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. star, n.\", \"stance\": \"supports\", \"note\": \"'ME. sterre, fr. OE. steorra'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Star\", \"stance\": \"supports\", \"note\": \"'Star. (E.) M.E. sterre. A.S. steorra.'\"}\n     ]},\n    {\"id\": 5, \"lang\": \"Greek\", \"words\": \"aster; aster-lambanein\", \"verdict\": \"plausible\",\n     \"derivation\": \"Greek ἀστήρ astḗr 'star' (gen. astéros), with its derivative ἄστρον ástron, is the Greek reflex of the a-grade *h₂stḗr: initial *h₂- appears as prothetic a-, and Greek keeps the agent-noun suffix -tēr. That half is certain. The second item, 'aster-lambanein', is not a Greek word: the instrument is ἀστρολάβον (ὄργανον) astrolábon/astrolábos, literally 'star-taking (instrument)', built on ástron (compositional form astro-, not aster-) plus the stem of λαμβάνειν lambánein 'to take' (aorist stem lab-, whence -labos). Nourai's elements and gloss are right, his citation form is not.\",\n     \"derivation_fa\": \"یونانی astḗr «ستاره» بازماندهٔ مستقیم *h₂stḗr است و الف آغازین آن بازتاب حنجرهٔ h₂ است؛ صورت دیگر آن ástron است. اما «aster-lambanein» واژهٔ یونانی نیست؛ نام ابزار astrolábon است، مرکب از astro- (از ástron) و ستاک lab- از مصدر lambánein «گرفتن، اندازه گرفتن». پس اجزا و معنایی که نورایی می‌دهد درست است ولی صورت مرکب را به شکل غیرواقعی آورده است؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_ASTROLABE, W_ASTOR],\n     \"ref_check\": [{\"ref\": \"AHD:81\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ster-* (p. 66 of the 1985 standalone ed.; Nourai's p.81 is the 1976 AHD appendix pagination, not open online): '3. Oldest root form *aster- in Greek astēr, star, with its derivative astron ... ASTER, ASTERISK, ASTRO-, DISASTER'.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. astrolabe\", \"stance\": \"partial\",\n       \"note\": \"'ME., fr. OF. astrelabe, fr. ML. astrolabium, fr. Gk. ἀστρολάβον (scil. ὄργανον), lit. ‘startaking (instrument)’, fr. ἄστρον, ‘star’, and the stem of λαμβάνειν, ‘to take’' — astro-, not aster-.\"},\n      {\"src\": \"POK\", \"where\": \"p. 1027 s.v. ster-2\", \"stance\": \"supports\",\n       \"note\": \"'gr. astēr, -eros ‚Stern‘, collective astra ... astron ‚Stern, Gestirn‘ (out of it Latin astrum)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 635\", \"stance\": \"supports\",\n       \"note\": \"'gr. ἀστήρ ... ἄστρον ‚Stern, Gestirn‘ (daraus lat. astrum)'.\"}\n     ]},\n    {\"id\": 6, \"lang\": \"Persian\", \"words\": \"ostorlâb\", \"verdict\": \"plausible\",\n     \"derivation\": \"The ultimate source is indeed Greek astrolábos, but the word did not reach Persian from Greek directly. Greek astrolábon passed, in the 8th-9th c. translation movement (in part through Syriac ʾasṭurlābōn), into Arabic أَسْطُرْلَاب ʾasṭurlāb, with the Arabic treatment of Greek /t/ before a back vowel as emphatic ṭāʾ and a prothetic ʾa- for the initial cluster; from Arabic it was taken into Persian as اسطرلاب osṭorlāb, de-emphaticised in the common variant استرلاب ostorlāb that Nourai prints first. Persian scientific literature (Biruni's al-Tafhīm, quoted by Mo'in) uses the word from the 4th/10th c. on. The popular Persian folk etymology 'ستاره‌یاب' has no standing. Verdict plausible: the root and the Greek source are right, the chart skips the Arabic (and Syriac) mediation and so reverses the usual direction of loan traffic on this page.\",\n     \"derivation_fa\": \"«اسطرلاب» معرّب یونانی astrolábos است ولی نه به‌یکباره: در دوران نهضت ترجمه (سدهٔ دوم و سوم قمری) و غالباً از راه سریانی به عربی أسطرلاب راه یافت و از عربی به فارسی آمد؛ طای مؤنّث حاصل برگرداندن t یونانی پیش از واکهٔ پسین به مخرج مطبق عربی است. صورت استرلاب همان صورت بی‌طای فارسی است. ریشه‌شناسی عامیانهٔ «ستاره‌یاب» پایه‌ای ندارد. نمودار نورایی در اصل درست است ولی میانجی عربی را حذف کرده است؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_ASTOR, E_ASTROLABE],\n     \"ref_check\": [\n      {\"ref\": \"MON:248\", \"status\": \"partial\",\n       \"note\": \"Mo'in has the headword: 'اسطرلاب: [- اصطرلاب؛ معر]‏ (ا.) (نج.) ابزاری است که برای اندازه‌گیری موقع و ارتفاع ستارگان ... به کار می‌رفت' (MON_part1.txt l.12783, 2-vol. Adena repr. p.151-152 = 6-vol. p.~248). He tags it معرّب (Arabicised), which is the Arabic mediation the chart leaves out; the condensed edition does not spell out the Greek etymon.\"},\n      {\"ref\": \"ETM:45\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Risheh-shenasi (Qoqnus 1374) has no digital copy on any permitted platform (refs_online.json ETM: 'RE-SEARCH 2026-09: no digital copy ... catalogue/purchase only').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"اسطرلاب (Persian)\", \"stance\": \"partial\",\n       \"note\": \"'Borrowed from Arabic أَسْطُرْلَاب (ʾasṭurlāb), which derives from Ancient Greek ἀστρολάβος (astrolábos)'; alternative forms listed include استرلاب (usturlāb) — Nourai's first spelling.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. astrolabe\", \"stance\": \"partial\",\n       \"note\": \"Klein traces the European word Gk. > ML. astrolabium > OF astrelabe > ME, and says nothing about the Persian form; silent on the Arabic leg.\"},\n      {\"src\": \"LKT\", \"where\": \"searched for 'Astrolab'\", \"stance\": \"silent\",\n       \"note\": \"Lokotsch has no headword for the instrument (only al-ʿankabūt and al-ʿiḍāda, parts of the astrolabe, ll. 410, 2157); AFM, PLA, FVQ, TAD, ARB, PHN gave no hit for سطرلاب.\"}\n     ]},\n    {\"id\": 7, \"lang\": \"English\", \"words\": \"asterisk; astrolabe; disaster\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are Greek astron/astḗr words that entered English through Latin and French. asterisk: Gk. asteriskos 'little star' (dimin. of astḗr) > Late Latin asteriscus > English (1530s). astrolabe: Gk. astrolábon > Medieval Latin astrolabium > Old French astrelabe > ME astrolabe (Chaucer's Treatise on the Astrolabe, 1391). disaster: Gk. astron > Latin astrum > Italian dis-astro 'ill-starred event' (a back-formation on astro with the pejorative prefix dis-) > French désastre > English (1590s) — the semantics are astrological, 'a calamity blamed on an unfavourable star'.\",\n     \"derivation_fa\": \"هر سه واژه از راه لاتین و فرانسه به انگلیسی رسیده‌اند: asterisk از یونانی asteriskos «ستارک»؛ astrolabe از astrolábon یونانی از راه لاتین میانه astrolabium و فرانسهٔ کهن astrelabe (رسالهٔ چاسر ۱۳۹۱م)؛ و disaster از ایتالیایی disastro «بداختر» (پیشوند dis- + astro از لاتین astrum). ادعای نورایی درست است.\",\n     \"sources\": [E_ASTROLABE],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ster-*: the derivative list under the Greek section contains 'ASTER, ASTERIATED, ASTERISK, ASTERISM, ... ASTEROID, ASTRAPHOBIA, DISASTER' and, via astro-, ASTROLABE.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. asterisk, astrolabe, disaster\", \"stance\": \"supports\",\n       \"note\": \"'asterisk ... Late L. asteriscus, fr. Gk. ἀστερίσκος, dimin. of ἀστήρ'; 'disaster ... F. désastre, fr. It. disastro ... a back[-formation]'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"*ster- (2)\", \"stance\": \"supports\",\n       \"note\": \"'It might form all or part of: aster; asterisk; ... astrolabe; ... constellation; disaster; ... star; stellar.'\"}\n     ]},\n    {\"id\": 8, \"lang\": \"Latin\", \"words\": \"sterron\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"sterron\",\n     \"correct_form\": \"stēlla\",\n     \"derivation\": \"There is no Latin *sterron. The Latin word for 'star' is stēlla, from Proto-Italic *stērlā, a diminutive *stēr-lā of the root noun, with the regular Latin assimilation rl > ll (so Walde-Pokorny II 635, Buck 1.54, Klein s.v. stellar 'L. stella (for *ster-la)'). 'sterron' is the Germanic etymon of English star, which Nourai has correctly in the Germanic box of the same chart and has accidentally repeated in the Latin box. The printed page 450 does read 'sterron : star' in the Latin box (see data/verification/sources/refs/ocr/BOOK/480.png), so the extraction is faithful and the error is the book's. The arrow itself is sound: English constellation does go back to Latin stella.\",\n     \"derivation_fa\": \"در لاتین واژه‌ای به صورت *sterron وجود ندارد؛ واژهٔ لاتین برای «ستاره» stēlla است که از ایتالیک آغازین *stērlā (تصغیر *stēr-lā) و با همگونی rl > ll پدید آمده است. sterron همان صورت ژرمنی است که نورایی در جعبهٔ ژرمنی همین نمودار درست آورده و اینجا سهواً تکرار کرده است. این خطای چاپی خود کتاب است (تصویر صفحهٔ ۴۵۰ را ببینید)، نه خطای خوانش اسکن؛ خود پیوند لاتین ← انگلیسی constellation درست است.\",\n     \"sources\": [W_PIE, E_STAR],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"contradicts\",\n        \"note\": \"Watkins 1985 s.v. ster-*: '2. Suffixed form *stēr-lā- in Latin stēlla, star: STELLAR, STELLATE; CONSTELLATION.' The reference Nourai cites gives stēlla, not sterron.\"}],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 635\", \"stance\": \"contradicts\",\n       \"note\": \"'lat. stella ‚Stern‘ (*stēr-(e)la, Deminutiv)' — WLD puts sterr- only under Germanic.\"},\n      {\"src\": \"SYN\", \"where\": \"1.54 STAR\", \"stance\": \"contradicts\",\n       \"note\": \"Buck's Latin cell reads 'stella, astrum'; his commentary: 'Lat. stēlla (fr. *stēr-lā ...)'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. stellar\", \"stance\": \"contradicts\",\n       \"note\": \"'stellar ... L. stellaris, fr. stella (for *ster-la), ‘star’'.\"}\n     ]},\n    {\"id\": 9, \"lang\": \"English\", \"words\": \"constellation\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin con- 'together' + stēlla 'star' gives the Late Latin verbal adjective constellātus and the noun constellātiō 'a collection of stars' (an astrological coinage, 'the position of the stars at a birth'); this passed into Old French constellacion and so into Middle English (c. 1300) with the astrological sense, the plain astronomical 'group of fixed stars' sense following in the 14th c. The chain hangs on Latin stēlla, i.e. on the corrected form of node #8.\",\n     \"derivation_fa\": \"انگلیسی constellation از لاتین متأخر constellātiō «مجموعهٔ ستارگان» از پیشوند con- «با هم» و stēlla «ستاره» است، از راه فرانسهٔ کهن constellacion در حدود ۱۳۰۰ میلادی وارد انگلیسی میانه شده و نخست معنای احکام‌نجومی داشته است. پیوند درست است، به شرط آنکه صورت لاتین stēlla خوانده شود.\",\n     \"sources\": [E_ASTROLABE],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"no reference on the node; the parent Latin box cites AHD, whose ster-* entry lists CONSTELLATION under Latin stēlla.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. constellation\", \"stance\": \"supports\",\n       \"note\": \"'constellation, n. — Late L. constellātiō, ‘a collection of stars’, fr. constellātus.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"*ster- (2)\", \"stance\": \"supports\",\n       \"note\": \"constellation is listed among the English derivatives of *ster- (2).\"}\n     ]}\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ster 3, Sterp\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *(s)ter- / *(s)terp- 'stiff, rigid, immovable'\",\n   \"note\": \"Pokorny's '(s)ter-1, (s)terə-, (s)trē-, Meaning: stiff, immovable; solid, Page(s): 1022-1027' is exactly this root, and the labial extension '(s)terp-' is a named subsection of that entry (POK_full.txt, relative line 198 of the entry: '3. Labial extensions: (s)terp-'), so Nourai's double heading 'Ster 3, Sterp' and his page 1022 are both right. Watkins prints it as ster-1 'Stiff' with '[Pok. 1. (s)ter- 1022.]'; Mann (IEC) even has an independent lemma 'sterp- ‘stiff, hard, barren, withered, dead’'. Only Nourai's serial number differs from Pokorny's (Pokorny's ster-3 is 'to rob, steal', p.1028) — that number is his own book-internal homograph count, not a citation. Two forms inside the entry are misprinted in the book: Greek 'steros' for stereos, and the Germanic 'sterk' offered as the source of English start.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی *(s)ter- «سخت، ستبر، بی‌حرکت» که پوکورنی در صفحات ۱۰۲۲–۱۰۲۷ آورده و گستردهٔ لبی آن *(s)terp- بخشی از همان ماده است؛ پس عنوان دوگانهٔ کتاب درست است. شمارهٔ «۳» شمارهٔ درون‌کتابی نورایی است نه شمارهٔ پوکورنی. مهم‌ترین حلقهٔ ایرانی این نمودار، «ترش»، در خود پوکورنی ذیل همین ریشه آمده است.\",\n   \"sources\": [E_TORPEDO, E_STARCH],\n   \"ref_check\": [\n    {\"ref\": \"POK:1022\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: (s)ter-1, (s)terə-, (s)trē- / Meaning: stiff, immovable; solid, etc. ... Page(s): 1022-1027'; within it '3. Labial extensions: (s)terp-' and 'ohne s-: torpēo, -ēre ‚rigid, insensible‘'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ster-1 'Stiff' (p. 65-66)\", \"stance\": \"supports\",\n     \"note\": \"'ster-1. Stiff. ... STARE ... STARK ... STARCH ... STERN; ... Greek stereos, solid: STERE, STEREO-; CHOLESTEROL ... STRUT ... START ... STARTLE ... STARVE ... Extended form *(s)terp- ... Latin torpēre, to be stiff: TORPEDO, TORPID, TORPOR. [Pok. 1. (s)ter- 1022.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 627 ff.\", \"stance\": \"supports\",\n     \"note\": \"WLD_Bd2_pages.txt l.41898: 'Ohne s-: torpeo, -ere ‚steif, starr, gefühllos, betäubt sein‘ ... lit. tirpstu, tirpti ‚erstarren‘ ... r. terpkij ‚herb, sauer‘' — the (s)terp- section of the same root.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. sterp- (Mann)\", \"stance\": \"supports\",\n     \"note\": \"IEC.txt l.17216: 'sterp- ‘stiff, hard, barren, withered, dead’ ... OHG, MHG stërbo ... OE steorfa ... Icel. stjarfur, adj. ‘stiff’ ... Cf. WP II, 632.' Mann keeps Nourai's second heading as a lemma of its own.\"},\n    {\"src\": \"Etymonline\", \"where\": \"*ster- (1)\", \"stance\": \"supports\",\n     \"note\": \"'*ster- (1) Proto-Indo-European root meaning “stiff.” It might form all or part of: cholesterol; redstart; starch; stare; stark; start; startle; starve; stere; stereo-; stern (adj.); stork; strut; torpedo; torpid; torpor.'\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"turuš\", \"verdict\": \"plausible\",\n     \"derivation\": \"The word is genuine and the root is right, but the label and the shape do not match: turuš is the CLASSICAL NEW PERSIAN form, which is exactly how Horn prints it at the page Nourai cites (Grundriss no. 385, p. 86: 'turuš ‚sauer‘', with Kurd. tirš, Bal. trusp/trūs, Wakhi trešp). The Middle Persian antecedent is tru(f)š [tlw(p)š], Psalter Pahlavi tryfš, as MacKenzie prints it (Concise Pahlavi Dictionary p.83: 'tru(f)š ... sour', with 'N turš'). Both go back to Proto-Iranian *tr̥fšah- (Hübschmann, Pers. Studien §82 and no. 385: 'turuš ‚sauer‘ aus *tr̥fsa-? ... ap. f ist geschwunden ... vielleicht auch inlautend in turuš'), from *(s)terp-/*trp- of the root: the f of the cluster -fš- was lost, the resulting *truš acquired an anaptyctic u (truš > turuš). So: Nourai's arrow root > Iranian 'sour' is correct and is Pokorny's own; the box should read Pahlavi tru(f)š (or be labelled New Persian).\",\n     \"derivation_fa\": \"صورت turuš آنچه در جعبه آمده فارسی نوی کلاسیک است نه پهلوی؛ هرن در صفحهٔ ۸۶ (شمارهٔ ۳۸۵) همین turuš «ترش» را ذیل فارسی نو آورده است. صورت فارسی میانه به روایت مکنزی tru(f)š (در زبور پهلوی tryfš) است. هر دو از ایرانی آغازین *tr̥fšah- اند؛ هوبشمان می‌گوید f در خوشهٔ -fš- افتاده و سپس میان t و r واکهٔ میانجی u افزوده شده است. پس پیوند ریشه درست است ولی برچسب «پهلوی» برای این صورت نادرست است؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_TORSH],\n     \"ref_check\": [{\"ref\": \"HRN:86\", \"status\": \"partial\",\n        \"note\": \"HRN.txt leaf 107 (= printed p.86): '385. turuš ‚sauer‘. kurd. tirš ‚sauer‘; bal. trusp, trūps, n. trūs (395); waḵ. trešp, sar. təřb, yidg. trišp.' Horn has the word on the cited page with the cited meaning, but as a NEW PERSIAN headword — he gives no Pahlavi form, so the label 'Pahlavi' is not Horn's.\"}],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 83 s.v. tru(f)š\", \"stance\": \"partial\",\n       \"note\": \"PHD_mackenzie.txt l.5017: 'tru(f)š [tlw(p)š | (P tryfš), N turš] sour.' The Middle Persian form is tru(f)š, not turuš.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien no. 385 and §§81-82\", \"stance\": \"supports\",\n       \"note\": \"HUB.txt l.1630 '385. Zu turuš ‚sauer‘ etc. vgl. auch afgh. triũ ... Liesse sich iran. *tr̥fsa- (= av. *tr̥psa-) ansetzen...'; l.5114 'turuš ‚sauer‘ aus t̥r̥fsa-?'; l.6570 'vielleicht auch inlautend in turuš ‚sauer‘ (aus *truš = *trušf = *trufs = ...)'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n       \"note\": \"grep -n -i 'turuš|truš' NYB_vol2_glossary.txt returns only catrušvitak 'a quarter'; Nyberg's glossary does not carry the word.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb\", \"stance\": \"silent\",\n       \"note\": \"grep for truš/turuš gives no root entry — expected, since the word is an adjective, not a verbal root.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"toroš, torš\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP تُرش: classical reading turuš/turš, modern Iranian reading toroš/torš — exactly the two forms Nourai prints, and the alternation is only the modern Iranian raising-lowering of the classical u to o. It continues MP tru(f)š < PIr. *tr̥fšah- < the *(s)terp-/*tr̥p- grade of the root, with the semantic bridge 'stiff, rigid' > 'astringent, tart' > 'sour' that is visible in the cognates Pokorny lines up (r.-ChSl. terpkŭ 'αὐστηρός', Russ. terpkij 'herb, sauer', NHG derb). Pokorny cites the Persian word himself. Derivatives تُرشا / تُرشی (pickles) are NP formations on it.\",\n     \"derivation_fa\": \"«تُرش» در خوانش کلاسیک turuš/turš و در خوانش امروز ایران toroš/torš؛ از فارسی میانهٔ tru(f)š و آن از ایرانی آغازین *tr̥fšah- از گونهٔ *(s)terp- ریشه. تحول معنایی از «سخت، گس» به «ترش» در روسی terpkij و آلمانی derb نیز دیده می‌شود. پوکورنی خود در صفحهٔ ۱۰۲۲ می‌نویسد «np. turuš ‚sauer‘». «ترشی» و «ترشا» مشتقات فارسی نوی آن‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W_TORSH],\n     \"ref_check\": [\n      {\"ref\": \"POK:1022\", \"status\": \"supports\",\n       \"note\": \"POK (s)ter-1, labial-extension section: 'als ‚rigid, dull, vom Standpunkte des Geschmacks‘: aksl. *trŭpŭkŭ ‚acerbus, asper‘, russ. terpkij ‚herb, sauer‘, as np. turuš ‚sauer‘ (if from *tr̥fsa-) und nhd. derb'. Pokorny puts the Persian word on the very page Nourai cites.\"},\n      {\"ref\": \"BQT:485\", \"status\": \"partial\",\n       \"note\": \"BQT_v1_pages.txt leaves 711-712 (≈ printed pp. 483-486, the ترش section between ترسا and ترک) carry ترش with the definition '... باشد. ضد شیرین. مقابل: شیرین' and the derivatives ترشک, ترشاک, ترشه, ترشیناک — so the page reference is right for the headword and the gloss 'sour'; Mo'in's Latin-script etymological footnote on that page is illegible in this OCR (vol. 1 has no page scan in refs_online.json, so ref_page.py cannot render it).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 385, p. 86\", \"stance\": \"supports\",\n       \"note\": \"'385. turuš ‚sauer‘' with the Iranian dialect cognates — Horn treats it as an inherited Iranian adjective, not a loan.\"},\n      {\"src\": \"HUB\", \"where\": \"no. 385 / §82\", \"stance\": \"supports\",\n       \"note\": \"'turuš ‚sauer‘ aus *tr̥fsa-?' — Hübschmann's reconstruction is the modern Proto-Iranian *tr̥fšah-.\"},\n      {\"src\": \"PHD\", \"where\": \"p. 83 s.v. tru(f)š\", \"stance\": \"supports\",\n       \"note\": \"'tru(f)š [tlw(p)š | (P tryfš), N turš] sour' — MacKenzie's 'N turš' is Nourai's Persian box.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"ترش (Persian)\", \"stance\": \"supports\",\n       \"note\": \"'Ultimately inherited from Proto-Iranian *tr̥fšah'; readings given: 'Classical: turuš, turš / Iranian: toroš, torš'.\"}\n     ]},\n    {\"id\": 3, \"lang\": \"Latin\", \"words\": \"torpere\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin torpēre 'to be numb, stiff, insensible' (Plautus onward) is the s-less stative of the labial extension: zero-grade *tr̥p- + the stative suffix *-eh₁- gives *tr̥p-ē-, Latin torp-ē-re (syllabic r̥ > or before a labial). Its cognate set is precisely the Balto-Slavic 'grow stiff' family: OCS u-trŭpěti, Russ. terpnut' 'stiffen', Lith. tirpstu, tirpti 'grow numb'. Derivatives torpor, torpidus and torpēdō are all classical.\",\n     \"derivation_fa\": \"لاتین torpēre «سخت و بی‌حس بودن» از درجهٔ صفر *tr̥p- به‌علاوهٔ پسوند حالتی *-eh₁- ساخته شده است؛ r هجایی پیش از همخوان لبی در لاتین or شده است. هم‌ریشه‌های آن در اسلاوی کهن (u-trŭpěti) و لیتوانی (tirpti) همان معنای «خشک و بی‌حس شدن» را دارند. ادعای نورایی درست است.\",\n     \"sources\": [E_TORPEDO],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ster-1: 'VI. Extended form *(s)terp- in suffixed (stative) zero-grade form *tr̥p-ē- in Latin torpēre, to be stiff: TORPEDO, TORPID, TORPOR.'\"}],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. torpeo\", \"stance\": \"supports\",\n       \"note\": \"LAT.txt l.64888: 'torpeo, -es, -ere: être engourdi (sens physique et moral). Ancien, déjà dans Plaute ... Dérivés: torpor ...; torpidus: engourdi; torpēdō ... Cf. v.sl. u-trupěti, russe terpnut', lit. tirpstu, tirpti.'\"},\n      {\"src\": \"POK\", \"where\": \"p. 1022 ff. s.v. (s)ter-1\", \"stance\": \"supports\",\n       \"note\": \"'ohne s-: torpēo, -ēre ‚rigid, insensible, betäubt sein‘ (= aksl. u-trŭpěti or = russ. toropetĭ)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 627\", \"stance\": \"supports\",\n       \"note\": \"same passage in Walde-Pokorny: 'Ohne s-: torpeo, -ere ‚steif, starr, gefühllos, betäubt sein‘'.\"}\n     ]},\n    {\"id\": 4, \"lang\": \"English\", \"words\": \"torpedo\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin torpēdō 'numbness, stiffness' (from torpēre) was also the Roman name of the electric ray, the fish that numbs whoever touches it. English took it in that zoological sense in the 1520s; Robert Fulton applied it in 1807 to his 'submarine explosive device' (from the paralysing shock), whence the floating mine and, from c.1900, the self-propelled torpedo.\",\n     \"derivation_fa\": \"انگلیسی torpedo از لاتین torpēdō «بی‌حسی، کرختی» (از torpēre) است که نام ماهی «سپرماهی برقی» هم بود؛ در سدهٔ شانزدهم به همین معنا وارد انگلیسی شد و در ۱۸۰۷ فولتن آن را بر سلاح انفجاری زیردریایی نهاد. ادعای نورایی درست است.\",\n     \"sources\": [E_TORPEDO],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"no reference on the node; the parent Latin box cites AHD, which lists TORPEDO under ster-1.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. torpedo\", \"stance\": \"supports\",\n       \"note\": \"KLN_1971.txt l.250128 ff.: 'torpedo, n., 1) a fish allied to the rays; 2) a destructive [device] ... ‚numbness; crampfish‘, fr. torpēre, ‘to be numb’.'\"},\n      {\"src\": \"LAT\", \"where\": \"s.v. torpeo\", \"stance\": \"supports\",\n       \"note\": \"Ernout-Meillet list 'torpēdō (torpille)' among the derivatives of torpeo.\"}\n     ]},\n    {\"id\": 5, \"lang\": \"Germanic\", \"words\": \"sterk; staren; strŭt; starkjan; sterben\", \"verdict\": \"plausible\",\n     \"derivation\": \"Four of the five are exactly Watkins' Germanic forms under ster-1: staren = Gmc *starēn (OE starian 'to stare', OHG starēn), strŭt = Gmc *strūt- (OE strūtian 'to stand out stiffly'), starkjan = Gmc denominative *starkjan (OE *stercan > ME starchen 'to stiffen', beside the adj. *starkaz 'hard, stiff'), sterben = Gmc *sterban (OE steorfan 'to die', lit. 'become rigid', from the bh-extension *sterbh-). The odd one is the first: 'sterk : to move stiffly' is offered here as the parent of English start, but start is from a DENTAL extension, Gmc *stert- (OE *styrtan 'to leap up' < 'move briskly/stiffly'), not from *sterk-. Gmc *sturkaz with the guttural gives OE storc 'stork' instead. So the box is right in substance but one of its five etyma is matched to the wrong English word.\",\n     \"derivation_fa\": \"چهار صورت از پنج صورت این جعبه دقیقاً همان‌هایی است که واتکینز ذیل ster-1 می‌آورد: staren (ژرمنی *starēn)، strūt (*strūt-)، starkjan (*starkjan از صفت *starkaz) و sterban (گستردهٔ bh- یعنی *sterbh-). اما «sterk» که در کتاب نیای انگلیسی start شمرده شده نادرست است؛ start از گستردهٔ دندانی *stert- (انگلیسی کهن styrtan) می‌آید و گستردهٔ کامی *sturkaz به stork «لک‌لک» می‌رسد. پس محتوا درست است ولی یک جفت‌شدن نادرست دارد؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_STARCH, E_STARVE, E_START],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"Watkins 1985 s.v. ster-1 has *starēn (STARE), *starkaz/*starkjan (STARK, STARCH), *strūt- (STRUT) and *sterban (STARVE) exactly as drawn, but puts START under 'IV. Extended form *sterd-. ... Germanic *stert- in ... Old English *styrtan, to leap up' — not under a *sterk-.\"}],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"pp. 1022-1027 s.v. (s)ter-1\", \"stance\": \"supports\",\n       \"note\": \"'Germanic *stara- ‚rigid, esp. of eye‘ in ... ahd. starēn ‚stare‘'; 'Adj. *starku- in ae. stearc ‚stiff, stern, strong‘, ahd. starc'; 'ae. strūtian ‚stiff stand‘'; 'ahd. sterban ‚die‘ (*‚solidify, congeal‘) ... ae. steorfan (engl. starve)'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.vv. stare, stark, starch, starve, strut\", \"stance\": \"supports\",\n       \"note\": \"Klein groups them all: 'All these words derive fr. I.-E. base *ster-, ‘strong, firm, stiff, rigid’. Cp. starch, stark, start, n., starve, stern, stork, ... stereo-, ... strut.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 628-634\", \"stance\": \"supports\",\n       \"note\": \"same Germanic material (starēn, starkaz, strūtian, sterban) under the (s)ter- entry from which Pokorny's text is drawn.\"}\n     ]},\n    {\"id\": 6, \"lang\": \"English\", \"words\": \"start; stare; strut; starch; starve\", \"verdict\": \"plausible\",\n     \"derivation\": \"stare < OE starian 'to look fixedly' (Gmc *starēn); strut < OE strūtian 'to stand out stiffly', ME strouten 'to swell out'; starch, a back-formation from ME sterchen < OE *stercan 'to stiffen', from stearc 'stiff' (cf. G Stärke 'strength; starch'); starve < OE steorfan 'to die', literally 'become stiff', narrowed in ME to 'die of cold' (14c.) and then 'die of hunger' (mid-15c.). These four are secure. start is the doubtful one: Watkins and Etymonline derive it from Gmc *stert- (OE *styrtan 'to leap up' < 'move briskly, move stiffly'), but Klein flatly calls ME sterten, OE sturtian/styrtan 'of uncertain origin', and the OHG cognate sturzen 'to hurl, plunge' is hard to reconcile with a 'stiff' semantics. Node verdict plausible for that reason.\",\n     \"derivation_fa\": \"stare از انگلیسی کهن starian، strut از strūtian «سخت ایستادن»، starch از *stercan «سخت کردن» (از صفت stearc) و starve از steorfan «مردن» (در اصل «خشک و سخت شدن»)؛ این چهار قطعی است. اما start محل اختلاف است: واتکینز و اتیمانلاین آن را از ژرمنی *stert- می‌دانند ولی کلاین می‌نویسد «of uncertain origin». پس این جعبه در مجموع با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_STARCH, E_STARVE, E_START],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"no reference on the node; the parent Germanic box cites AHD, which lists STARE, STARCH, STRUT, STARVE and START (under *sterd-/*stert-) as English reflexes of ster-1.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. starch, stare, start, starve, strut\", \"stance\": \"partial\",\n       \"note\": \"Klein supports four: 'starch ... back formation fr. sterchen, fr. OE. stercan, ‘to stiffen’, fr. stearc'; 'strut ... fr. OE. strutian, ‘to stand stiffly, be rigid’'; 'starve ... fr. OE. steorfan ... fr. I.-E. *sterbh-, a -bh-enlargement of base *ster-'. But 'start, intr. and tr. v. — ME. sterten ... rel. to OE. sturtian, styrtan, ‘to leap up’ ... of uncertain origin.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"*ster- (1) and s.v. start\", \"stance\": \"supports\",\n       \"note\": \"'*ster- (1) ... It might form all or part of: cholesterol; redstart; starch; stare; stark; start; startle; starve ...; strut; torpedo' — start included, but with the hedging 'might'.\"},\n      {\"src\": \"SKT\", \"where\": \"grep for STARVE/STARCH/STRUT\", \"stance\": \"silent\",\n       \"note\": \"no hit for these headwords in the OCR of SKT.txt (only 'Star' at l.18366), so Skeat could not be used here.\"}\n     ]},\n    {\"id\": 7, \"lang\": \"Persian\", \"words\": \"estârt\", \"verdict\": \"confirmed\",\n     \"derivation\": \"استارت estārt is a 20th-c. European loan into Persian — from English start (in sport: the starting signal) and, in the mechanical sense, from the same word through automobile vocabulary, where استارتر estārter 'starter motor' is the base and استارت its clipping. The prothetic e- is the usual Persian repair of an initial st- cluster (as in استادیوم, استکان). Nourai's arrow English > Persian is therefore right, and this is one of the rare modern-loan boxes in the book.\",\n     \"derivation_fa\": \"«استارت» وام‌واژهٔ سدهٔ بیستم از انگلیسی start است؛ در ورزش به معنای لحظهٔ حرکت و در فناوری خودرو کوتاه‌شدهٔ «استارتر». الف آغازین همان الف پروتتیک فارسی پیش از خوشهٔ st- است. معین هر دو مدخل استارت و استارتر را آورده است. ادعای نورایی درست است.\",\n     \"sources\": [E_START],\n     \"ref_check\": [{\"ref\": \"MON:238\", \"status\": \"supports\",\n        \"note\": \"Mo'in has the headword with a Latin-script etymon: 'استارت: [start] (ا.) حرکت کردن و به حرکت در آوردن (ور.) در ورزش‌های دو و میدانی، دوچرخه‌سواری، شنا و اسکی لحظه حرکت ورزشکاران است' followed by 'استارتر ... (مکن.) دستگاه خودکاری است که موتوری را ... به حرکت درمی‌آورد' (MON_part1.txt l.11255 ff.; 2-vol. Adena repr. p.134-135, matching 6-vol. p.~238).\"}],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.vv. استارت, استارتر\", \"stance\": \"supports\",\n       \"note\": \"both entries are tagged with a Latin-script European etymon and a sports/mechanics domain label, i.e. a modern loan, not an inherited word.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. start (v./n.)\", \"stance\": \"supports\",\n       \"note\": \"'The meaning “begin to move, leave, or depart” ... is from 1821 ... specifically as “set machinery in action” by 1841' — the very senses Persian borrowed.\"}\n     ]},\n    {\"id\": 8, \"lang\": \"Greek\", \"words\": \"steros\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"steros\",\n     \"correct_form\": \"stereos (στερεός)\",\n     \"derivation\": \"Greek has no *στερός. The word meaning 'solid, firm, hard' is στερεός stereós (Attic also στερρός sterrós < *στερεός), Watkins' 'suffixed form *ster-ewo- in Greek stereos'; it is the source of stere-, stereo-, and of the -sterol of cholesterol. The printed page 450 does read 'steros : solid' (see data/verification/sources/refs/ocr/BOOK/480.png), so this is the book's misprint (or Nourai's shorthand), not an extraction error — and it matters, because the English derivatives in node #9 presuppose stereo-, not *ster-os. The derivation itself (root 'stiff' > Greek 'solid') is correct and is Pokorny's very first citation under (s)ter-1.\",\n     \"derivation_fa\": \"در یونانی واژه‌ای به صورت *steros وجود ندارد؛ واژهٔ درست stereós (στερεός) «سخت، جامد» است که از *ster-ewo- ساخته شده و در آتیک به صورت sterrós هم آمده است؛ همین واژه است که stereo- و پایانهٔ -sterol در کلسترول از آن است. چاپ کتاب در صفحهٔ ۴۵۰ همین steros را دارد، پس خطای چاپی کتاب است نه خطای خوانش اسکن؛ خود پیوند ریشه درست است.\",\n     \"sources\": [E_TORPEDO],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"Watkins 1985 s.v. ster-1: '2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL.' The reference supports the derivation but spells the Greek word stereos.\"}],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p. 1022 s.v. (s)ter-1\", \"stance\": \"partial\",\n       \"note\": \"the entry opens 'Material: A. Gr. στερεός (Attic also στερρός from *στερεός) ‚rigid, tight, firm, hard‘, στερίφος ds.' — stereos, never steros.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. stereo-\", \"stance\": \"partial\",\n       \"note\": \"'stereo-, before a vowel stere-, combining form meaning ‘solid, firm’. — Gk. στερεο-, fr. στερεός, ‘firm, hard, solid, stiff’, fr. I.-E. base *ster-, ‘stiff, rigid’.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"*ster- (1)\", \"stance\": \"partial\",\n       \"note\": \"'It might also be the source of: Greek stereos “solid,” sterizein “to support,” sterphnios “stiff, rigid”.'\"}\n     ]},\n    {\"id\": 9, \"lang\": \"English\", \"words\": \"stereo; cholesterol\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are 19th-c. learned formations on Greek stereós 'solid'. stereo- is the combining form (stereoscope 1838, stereotype 1798, stereophonic 1927), 'stereo' being a clipping of one of them. cholesterol is French cholestérine, coined by Michel-Eugène Chevreul in 1815 from Gk. χολή kholḗ 'bile, gall' + stereós 'solid', because the substance was first isolated from gallstones; English replaced -ine with the alcohol suffix -ol (1894). Nourai's gloss for the Persian descendant, 'hard gall, first found in gallstones', is literally Klein's explanation.\",\n     \"derivation_fa\": \"هر دو واژه ساختهٔ علمی سدهٔ نوزدهم بر پایهٔ یونانی stereós «جامد»‌اند: stereo- صورت ترکیبی آن است، و cholesterol از فرانسه cholestérine (ساختهٔ شورول در ۱۸۱۵) از یونانی kholḗ «زرداب» + stereós، زیرا نخست‌بار در سنگ کیسهٔ صفرا یافت شد؛ پسوند -ol نشانهٔ الکل است. ادعای نورایی درست است.\",\n     \"sources\": [E_CHOL],\n     \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ster-1: 'Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL.'\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. cholesterol, stereo-\", \"stance\": \"supports\",\n       \"note\": \"KLN_1966.txt l.7508: 'cholesterol ... Formed fr. F. cholestérine, a word coined by the French chemist Michel-Eugène Chevreul (1786-1889), and -ol ... fr. Gk. χολή, ‘gall, bile’, and στερεός, ‘solid’ ... so called because it was originally found in gallstones.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. cholesterol / sterol\", \"stance\": \"supports\",\n       \"note\": \"'sterol (n.) “white, crystalline substance discovered in gallstones,” 1913, abstracted from cholesterol.'\"}\n     ]},\n    {\"id\": 10, \"lang\": \"Persian\", \"words\": \"esterîyo; kolestrol\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Persian words are 20th-c. loans of the international scientific vocabulary, taken through French: اِستریو est(e)riyo from French/English stéréo (with the usual Persian prothetic e- before st-, and -éo rendered -iyo), and کلیسترول / کلسترول kolesterol from French cholestérol, French ch- for Greek χ being read as k-. Nourai's glosses ('solid, three dimensional'; 'hard gall, first found in gallstones') translate the Greek elements correctly. Note that the printed page spells the second word کلیسترول (with ی), while the extracted JSON has کلسترول.\",\n     \"derivation_fa\": \"هر دو واژه از راه فرانسه در سدهٔ بیستم وارد فارسی شده‌اند: «اِستریو» از stéréo با الف پروتتیک پیش از st-، و «کلسترول/کلیسترول» از cholestérol که ch فرانسه (معادل خی یونانی) در فارسی کاف خوانده شده است. معنایی که نورایی می‌دهد درست است. توجه: در چاپ کتاب «کلیسترول» آمده ولی در دادهٔ استخراج‌شده «کلسترول» ثبت شده است.\",\n     \"sources\": [E_CHOL],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"the node carries no reference; checked instead against Klein s.v. cholesterol and Etymonline (below).\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. cholesterol\", \"stance\": \"supports\",\n       \"note\": \"Klein's 'F. cholestérine ... fr. Gk. χολή and στερεός ... so called because it was originally found in gallstones' is the source of Nourai's Persian gloss.\"},\n      {\"src\": \"MON\", \"where\": \"grep for استریو / کلسترول in MON_part1/2\", \"stance\": \"silent\",\n       \"note\": \"neither word appears as a headword in the OCR of the 2-vol. Mo'in on disk (استارت and استارتر are there, these two are not) — they are post-Mo'in technical loans.\"}\n     ]}\n   ]\n  }\n ]\n}\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-480.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-480.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-480.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 480"
}
```


### [2026-09-14T03:25:38.875Z] TOOL RESULT

```
ok
valid json
nodes verified: 19/19
node verdicts: {'confirmed': 12, 'plausible': 5, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 6, 'partial': 5, 'contradicts': 1}
books consulted: {'supports': 35, 'partial': 9, 'silent': 5, 'contradicts': 3} | by book: {'KLN': 13, 'Etymonline': 6, 'WLD': 5, 'POK': 4, 'Wiktionary': 3, 'SKT': 3, 'SYN': 2, 'PHD': 2, 'HUB': 2, 'LAT': 2, 'MON': 2, 'BRT': 1, 'AHD': 1, 'ARY': 1, 'IEC': 1, 'LKT': 1, 'NYB': 1, 'CHEUNG': 1, 'HRN': 1}
```


## [2026-09-14T03:25:44.644Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np=\"data/verification/page-480.json\"\ns=io.open(p,encoding=\"utf-8\").read()\ns=s.replace(\"the cognate列:\",\"the cognate list:\")\nio.open(p,\"w\",encoding=\"utf-8\").write(s)\njson.load(io.open(p,encoding=\"utf-8\"))\nprint(\"列\" in s)\nEOF\npython3 tools/verify_check.py 480 | tail -8"
}
```


### [2026-09-14T03:25:45.737Z] TOOL RESULT

```
False
nodes verified: 19/19
node verdicts: {'confirmed': 12, 'plausible': 5, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 6, 'partial': 5, 'contradicts': 1}
books consulted: {'supports': 35, 'partial': 9, 'silent': 5, 'contradicts': 3} | by book: {'KLN': 13, 'Etymonline': 6, 'WLD': 5, 'POK': 4, 'Wiktionary': 3, 'SKT': 3, 'SYN': 2, 'PHD': 2, 'HUB': 2, 'LAT': 2, 'MON': 2, 'BRT': 1, 'AHD': 1, 'ARY': 1, 'IEC': 1, 'LKT': 1, 'NYB': 1, 'CHEUNG': 1, 'HRN': 1}
```


## [2026-09-14T03:25:58.742Z] AGENT

Page 480 (book p. 450) verified — `verify_check.py 480` reports 19/19 nodes, 0 PROBLEM lines.

**Counts:** roots 2 confirmed · nodes 12 confirmed, 5 plausible, 2 transcription_suspect, 0 disputed/unverified.

**Flagged items**
- `Ster 2` #8 [Latin] **sterron** — transcription_suspect, `error_in: book`. Latin has *stēlla* (< *stēr-lā); "sterron" is the Germanic form repeated from box #3. AHD (the ref Nourai cites), WLD II 635, Buck 1.54 and Klein all give *stella*. Page image confirms the book itself prints it.
- `Ster 3, Sterp` #8 [Greek] **steros** — transcription_suspect, `error_in: book`. Greek is στερεός *stereós* (AHD: "*ster-ewo- in Greek stereos"); *steros doesn't exist. Book prints "steros".

**Notable plausible verdicts**
- #1 [Pahlavi] *turuš* — the form is Horn's **New Persian** headword (HRN no. 385 p. 86); MP is *tru(f)š* (MacKenzie p. 83). Root link itself is Pokorny's own ("np. turuš 'sauer'", p. 1022).
- #6 [Persian] *ostorlâb* — Greek → **Arabic** أسطرلاب → Persian; chart skips the Arabic (Syriac) mediation.
- #5 Greek "aster-lambanein" — not a Greek word; the compound is *astrolábon* (astro- + lab-); elements/gloss right.
- E1 #5/#6 — "sterk : to move stiffly" is matched to English *start*, but *start* is from Gmc *stert- (AHD); Klein calls *start* "of uncertain origin".

**Extraction error for the owner to fix**
- Entry 1, node #10: printed page reads **کلیسترول**; `data/extracted/batch/page-480.json` has **کلسترول** (missing ی). Everything else matches the page.

Page image kept at `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/480.png`; 11 web pages archived via `fetch_source.py`. Output: `/home/sfmqrb/git/rishe/data/verification/page-480.json`.
