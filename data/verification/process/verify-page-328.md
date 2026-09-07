# Verification process log — verify-page-328


## [2026-09-07T16:07:31.629Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 328 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-328.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-328.json. Write /home/sfmqrb/git/rishe/data/verification/page-328.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 328` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:07:33.991Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T16:07:34.699Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:07:34.716Z] TOOL RESULT

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


## [2026-09-07T16:07:35.116Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-328.txt"
}
```


### [2026-09-07T16:07:35.141Z] TOOL RESULT

```
1	=== PDF page 328 (book page 298) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Meig, Meik / Meigh 1 / Meigh 2 : Meig, Meik: to mix. Meigh 1: to sprinkle, urinate. Meigh 2: to blink, cover, darken.  (refs POK:712-714; AHD)
4	#1 (parent #0) [Avestan] refs=POK:714; BQT:1835 | minašti : to mix, mixed ; vi-maik, vi-minašti : to mix ☞Wi
5	  #2 (parent #1) [Persian] refs=HRN:12 | âmîxtan «آمیختن» : to mix ; gomîxtan «گمیختن» : to mix up | extra: آمیزش
6	#3 (parent #0) [Avestan] refs=POK:713; BQT:62; SYN:273 | maĕz : urine
7	  #4 (parent #3) [Sogdian] refs=SOD:227 | myz`y : urine
8	  #5 (parent #3) [Persian] refs=BQT:1835,2073; MON:4493 | mîz «میز» : urine ; mîxtan «میختن» : to urinate | extra: میزراه ، گمیز
9	#6 (parent #0) [Avestan] refs=POK:712; BQT:2079 | maeğa : cloud
10	  #7 (parent #6) [Pahlavi] refs=ISS:285 | mîğ : cloud
11	    #8 (parent #7) [Persian] refs=HRN:226; ISS:285 | mîğ «میغ» : cloud ; meh 1 «مه ۱» : fog
12	#9 (parent #0) [Persian] refs=POK:712; HRN:219; BQT:2006 | možeh, možgân «مژه ، مژگان» : eyelashes
13	#10 (parent #0) [Latin] refs=AHD | miscĕre : to mix
14	  #11 (parent #10) [English] refs=None | mix, miscellaneous
15	#12 (parent #0) [Germanic] refs=AHD | mih-stu : fine rain, mist
16	  #13 (parent #12) [English] refs=None | mist
17	--- entry 1 ---
18	ROOT Meigh 1 -> redirect to Meig
19	--- entry 2 ---
20	ROOT Meigh 2 -> redirect to Meig
21	--- entry 3 ---
22	ROOT Meigw -> redirect to Mei 3
23	--- entry 4 ---
24	ROOT Meih -> redirect to Mei 3
25	--- entry 5 ---
26	ROOT Meik -> redirect to Meig
27	
```


## [2026-09-07T16:07:38.369Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-328.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-07T16:07:38.426Z] TOOL RESULT

```
{
  "pdf_page": 328,
  "book_page": 298,
  "entries": [
    {
      "root": {
        "name": "Meig, Meik / Meigh 1 / Meigh 2",
        "lang": "Indo-European",
        "refs": "POK:712-714; AHD",
        "gloss": "Meig, Meik: to mix. Meigh 1: to sprinkle, urinate. Meigh 2: to blink, cover, darken."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:714; BQT:1835",
          "words": [
            {
              "translit": "minašti",
              "gloss": "to mix, mixed",
              "script": null
            },
            {
              "translit": "vi-maik, vi-minašti",
              "gloss": "to mix",
              "script": null,
              "see": [
                "Wi"
              ]
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
          "refs": "HRN:12",
          "words": [
            {
              "translit": "âmîxtan",
              "gloss": "to mix",
              "script": "آمیختن"
            },
            {
              "translit": "gomîxtan",
              "gloss": "to mix up",
              "script": "گمیختن"
            }
          ],
          "script_extra": "آمیزش",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:713; BQT:62; SYN:273",
          "words": [
            {
              "translit": "maĕz",
              "gloss": "urine",
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
          "lang": "Sogdian",
          "refs": "SOD:227",
          "words": [
            {
              "translit": "myz`y",
              "gloss": "urine",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1835,2073; MON:4493",
          "words": [
            {
              "translit": "mîz",
              "gloss": "urine",
              "script": "میز"
            },
            {
              "translit": "mîxtan",
              "gloss": "to urinate",
              "script": "میختن"
            }
          ],
          "script_extra": "میزراه ، گمیز",
          "note": null,
          "quote": {
            "text": "باچنین دل چه جای باران است - ابر بر تو گمیز هم نکند",
            "poet": null
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:712; BQT:2079",
          "words": [
            {
              "translit": "maeğa",
              "gloss": "cloud",
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
          "lang": "Pahlavi",
          "refs": "ISS:285",
          "words": [
            {
              "translit": "mîğ",
              "gloss": "cloud",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "HRN:226; ISS:285",
          "words": [
            {
              "translit": "mîğ",
              "gloss": "cloud",
              "script": "میغ"
            },
            {
              "translit": "meh 1",
              "gloss": "fog",
              "script": "مه ۱"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همی گفت کای پادشاهی دریغ - که ماهت نهان شد به تاریک میغ",
            "poet": "Asadî"
          }
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:712; HRN:219; BQT:2006",
          "words": [
            {
              "translit": "možeh, možgân",
              "gloss": "eyelashes",
              "script": "مژه ، مژگان"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "miscĕre",
              "gloss": "to mix",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "mix, miscellaneous",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "mih-stu",
              "gloss": "fine rain, mist",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "mist",
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
        "name": "Meigh 1",
        "redirect": "Meig"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Meigh 2",
        "redirect": "Meig"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Meigw",
        "redirect": "Mei 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Meih",
        "redirect": "Mei 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Meik",
        "redirect": "Meig"
      },
      "nodes": []
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


## [2026-09-07T16:07:59.692Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','HRN','SOD','MON','ISS','SYN','BRT','PHD','NYB','HUB','CHEUNG','KLN','SKT','LEW','LAT','IEC','WLD','ARY']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-07T16:08:01.201Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== CHEUNG null
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-07T16:08:05.437Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"meig̑h\\|meiĝh\\|meigh-\\|meik̂\\|meiĝ-\\|meik-\" POK_full.txt | head -50"
}
```


### [2026-09-07T16:08:05.488Z] TOOL RESULT

```
58135:derived the truncated Root/ lemma: meigh-, also rneik-: "to glimmer, twinkle; mist'. 
58164:water ' ( *meigh-id)\ 
78716:Root / lemma: smei-3, smeid- smeig- smeik-
```


## [2026-09-07T16:08:07.468Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '58050,58230p' POK_full.txt"
}
```


### [2026-09-07T16:08:07.519Z] TOOL RESULT

```
Alb. math^b\g,: mcymr. ma/th'\ong, big' large' common alb. - mcymr. -k > -th. 

Latin magnus'b\g, large' {*meg-nd-s), Kompar. mag-is^ more, in a higher degree, more 
completely ', maior^ greater' {*meg-Jds), Superl. maximus {*meg-Semo-s)\ in addition 
maiestas^ greatness, grandeur, dignity, majesty ' {*meg-Jes-tat-), compare alb. madheshtf 
( *megis-t-iJS) ds. (about Oscan mais, maimas, Umbrian mestrusee below me- "big, large'), 
Maia " Daughter of Atlas and Pleione, and the mother of Mercury by Jupiter '; deus Maius 
"Juppiter' (Tusculum), whereof the month Maius {as Oscan Maesius^ May ' derives from 
the missing God's name, s. Schuize Eigenn. 469 ff.), Oscan PN Ma/'/ufDat Sg. (compare 
also Celtic magio-); Latin (Celtic, also alb.) -a- is Indo Germanic e, about Latin maialis^ a 
gelded boar, a barrow hog ' s. WH. II 13; 

Latin mactus' worshipped, honored ', /77ac/e" (sacrificial call) hail!', macto, -are^ to 
magnify, extol, honor, glorify, elevate, to offer, sacrifice, immolate, devote, to kill, slaughter, 
put to death, to overthrow, ruin, destroy, to afflict, trouble, punish '; magmentum' that 
which magnifies ' can be a formation of magnus aiter augmentum. 

Old Irish mochtae^b\g, large' (o!). Middle Irish maignech 6s. {*maginiakos, compare gall. 
Maginus; compare the />formsfrom Latin magnus). Middle Irish mag-, ma/ge^b\g, large', 
Pc»//77yC> A^5/ge"Pompeius Magnus', gall. Magio-rTx, Are-magios (formal = Latin Maius); 
Middle Irish mai {*magios) " noble person, prince, lord', gall. Magio-s\n gods- and PN, 
abrit. PN Mag/o-cune {cymr. Maei-gwn), Cuno-magius e\.c.\ gall. Maga/u Dat Sg. god's 
name, MagaiosPH, Middle Irish mag-iorg ^c\ub, mace, joint' {*mago-iorga large cudgel, 
club'), /77as5 "stately' ( */77a/r5C»5 compare Latin maximus), Kompar. Old Irish maissiu, cymr. 
corn, meiiinlat', Middle Breton biii/n' fullness; abundance ' {*magesTno-)\ mcymr. maon 
{*magones) " the big ', maitiilong, big, large' {*mag-tio-), probably also Old Irish do-for- 
maig^ to increase, augment, enlarge, spread, extend ', -magar^ to increase, augment, 
enlarge, spread, extend ', acymr. di-guor-mechis^ has increased ' (acymr. c/7from *-g-s-); 
to divide from cymr. magu^ bring up ' ( *mak-)\ 



whether Old Irish magu. " plain, the open countryside', mcymr. /77a- "place', gall. 
Arganto-magus {whereoi Irish /775^e/7 'place', cymr. maen, corn, men, bret. mean^ stone 
'), cymr. maes {*magesto-) "field', to Old Indie mahT^eartW? 

Gothic /77/Ms"big, large'. Old High German mihhil. Old Saxon mikil. Old English micel. 
Old Icelandic m/ke// ds., Old English mycel, Proto German 'Vr7/Maz probably with -/o suffix 
after /e////5. Old High German luzzi^. Old Icelandic mjgk^ye'cy' (engl. much) at first from 
*/r7e/ri/- after /e/i/"much, a lot of; 

Tocharian A mak, B /775/ra"big, large an number, much, a lot of; Hittite me-ik-ki-is 
{mekki§) "big, large'. 

References: WP. II 257 ff., WH. II 4 f., 10 ff., Szemerenyi Word 8, 48. 
Page(s): 708-709 

Root / lemma: meihgh-, also meihk- 
Meaning: to glimmer, twinkle; mist 
Material: 1 . meihgh-. 

A. with the meaning "flicker, blink, move quickly to and fro, vibrate, quiver, shake, 
tremble, beat, palpitate '. 

Middle Low German m/cken' observe ', Old West Frisian m/tza^\r\ee6'; 

Lithuanian mingu, migti^ fall asleep ' (with uz-)\ Latvian miegu, m/gf6s. (with a/z-, ie-)\ 
Old Prussian enm/gguns ' 6ozed off, ismige^ passed away '; Latvian miegV close the 
eyes ', Old Prussian maiggun kVk., Lithuanian miegas, Latvian m/egs's\eep', in addition 
Lithuanian m/egu {o\d miegmi), miegotiaud Old Prussian /77e/ic/e "sleep'; 

Slavic *m/gb\n Bulgarian russ. /77/ig" instant, eye blink'; Slavic *mbgngt/"\n russ. -Church 
Slavic megnut/" to move the eyelids up and down, to wink, blink ', serb. namagnut/^wave, 
beckon', and m/gat/"b\\nk'; Iterat.-Kaus. Old Church Slavic sb-mez/t/^ close the eyes ', 
with aor.-pass. meaning Slavic *mbzat/, sloven, mezati^ keep the eyes closed ', russ. mzat 
" drowse '; serb. -Church Slavic miglivb " blinking '; 

B. with the meaning " d iyilJS£^2j^£|P-^lJ yi§J^^ilirf|g|Q 1 ^ *^ ^ * ■ ^? iliii£ '■ 

Old Indie megha-m. "cloud', m/h^ fog, watery precipitation ', Avestan maeya- ^c\oud'; 
Armenian meg log'; gr. 6|jixAn (Attic opixAn) "cloud, fog', hom. aMixOaAosaaav "foggy, 
epithet of Lemnos' (with vowel suggestion); 



Dutch /77/g^e/e/7 "staubregnen'; Old Icelandic /77/5//'"trubes weather' etc. {*mixstu-); 

Lithuanian migla^ioQ\ Latvian miglaAs. (= opiixAr)); Old Bulgarian mhg/a log', russ. 
/77^/a "snow flurry, cold fog', Czech mhalog', russ. mz/l^ rain lightly, fog, cloud ' etc. 

Note: 

gr. Gr. apoppoi; "dark' derived from alb. mje(r)gule^ fog, darkness ' [common gr. p < gw, p 
< kw\; alb. proves that from Root / lemma: mer-2, *extended mer-ek-\ "to shimmer, shine' 
derived the truncated Root/ lemma: meigh-, also rneik-: "to glimmer, twinkle; mist'. 

2. meihk-. Npers. miza, muza {Pa\r\\av\ *micak), ba\uc\ m/cac' eyelash '; 

Latin m/co, -are' to move quickly to and fro, vibrate, quiver, shake, tremble, beat, 
palpitate ' {*mikajd)\ dT-mico' to struggle, strive, contend, to be in conflict, be in peril, run a 
risk, risk, hazard '; cymr. /r7yig/'"luminous', di-r-mygu' despise ' (as de-spicio); Old Irish de- 
meccim{cc= g) " despise ' is brit. loanword; Old Bulgarian /77i>C6/b "vision, ghost, shimmer 
'; Upper Serbian mikac'b\\v\k, glitter, flash', etc. 

References: WP. II 246 f., WH. II 86, Trautmann 174, 184; 
See also: s. also under meis-. 
Page(s): 712-713 

Root / lemma: meihgh- 

Meaning: to urinate 

Material: Old Indie mehati' urinates ', participle mTdha-{= Latin mictus), mTdha-v\. "ordure', 

meha-xr\. "urine'; Avestan maezaitT urinates, dungs, manures ', maesman- 'unne'; 

Armenian mizem' urinate ', /77ez"urine'; 

gr. 6[j£ix£iv, Aor. wjjsi^a (= Latin mix?), new oplxsu) "urinate, to make water ', d\x\%a\ 
oupnaai Hes. (d-, 6- are probably vowel suggestion); compare [JOixoq m., MOixac;. -a5o(;f. " 
adulterer, adulteress '?? 

Latin meid, -ere, mixi, mictum (secondary mingo, minxi, minctum) "urinate, to make 
water ' ( *meigh-id)\ 

Old Icelandic mTga, Old English mTgan, Middle Low German /77/^e/7 "urinate, to make 
water'. Old English m/cgam., m/cget m /goda ' unne' , Gothic mafhstus. Old Saxon Old 
High German /77/s/"crap, muck'. Old English /77ec»A'" ordure, manure'. Modern Frisian 



mjuks, Old English miexeni. ' dung heap ', Old Saxon mehsn. "urine', Middle Low 
German mes, Old Frisian mese ds.; probably here transform the name the only through 
the crap, muck, droppings of the bird Mister mistletoe ': Old High German mistil. Old 
English mistel. Old Icelandic mistil-teinn^ sprig of mistletoe '; (with refreshed Tenuis of 
formants:) Middle High German meisch^ mash ', Middle Low German meisch, mesch^ 
unfermented malt juice, mash ', Old English masc-, max-wyrt^ mash spice ', engl. mash^ 
mash, crush, squeeze hard, squash '; 

Lithuanian /77^zi/ (neologism for *minzu), ni/sf/ ^unnate, to make water', Latvian mieznu 
and mTzu, participle mizu. Inf. /77/z/ 'urinate, to make water ' (but Lithuanian meziu, mezti^ 
work on the fertilizer ' is rather meziu = Latvian mezu, meto, mezt, it lies a lengthened 
grade root noun the basic *me[i]gh-)\ 

Serbo-Croatian miz-am, -5//"urinate, to make water' (zfrom the present *miz-jg)\ 
sloven. m9zf, mszeti' produce (liquids)', mezina' swampy land '; Slavic *mezga 
( *mo/gzgha irom * moigh-ska) " tree juice ' in Serbo-Croatian mezga, Czech mfzha, mfza 
etc.; 

Tocharian B /77/so 'urine'. 

References: WP. II 245 f., WH. II 60 f., Kuiper Nasalpras. 159, Trautmann 185, Berneker II 

54. 

Page(s):713 

Root / lemma: meih-g"- 

Meaning: to exchange 

Material: Gr. apsipw " change ', Med. ' reciprocate, repay, reward, retribute, shift, wander', 

a|JOi(36(; ' changing ', apoipn "variation'; Note: common lllyrian g"- > b-. 

Latin migro, -are^ to remove, depart, flit, migrate, to go away, depart, pass over, 
change, turn, to leave, abandon, transgress, violate ', Denom. of *mig"-ros. 

References: WP. II 245, WH. II 86 f. 

See also: extension from /77e/-"swap, vary, exchange'. 

Page(s):713 

Root/ lemma: me/h-R- {and meih-g-7) 

Meaning: to mix, stir 

Grammatical information: also mei- : mi-gR-, m/'-n-gR- Prasensstamme also with -so- -sRo-; 



Material: Old Indie meksayati, mimikse^ stirs, mixes ', misra-^ mixes ', misrayatr mixes '; 
Avestan minasti^ mixes ', misvan-^ containing the composite '; myasaite^ sie mischen 
^1 '; common Old Indie -gh- > -ks- > -s- : Avestan -ks- > -s- -s- 

gr. piYvu|ji (more properly psivvuiJi), psi^u), spsi^a, £m(£)ikto, spilYnv "mix, mingle', (jIgyu) 
ds., (jiya, [^'\yba Adv. ' mixed ', [}\yaq, -a5oc; "mixture' (with unclear y); Miayu) "mix, mingle' 
from *|jiy-aKU), or to mezg-\ common Old Indie -gh- > -ks- : Gr. - lllyrian -gh- > -d-, -z-
```


## [2026-09-07T16:08:14.875Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '58230,58290p' POK_full.txt"
}
```


### [2026-09-07T16:08:14.929Z] TOOL RESULT

```
Latin misceo, -ere^ mix, mingle, intermingle, blend ' (extension from mi[k]-skd)\ 

Old Irish mesc^ drunk, intoxicated ', Middle Irish also " baffle '; mesc(a)id^ mixes, 
immerses in a liquid, baffles '; cymr. mysgu^rniy!; 

Old High German miskan. Old English m/sc/an'm\x' (rather Latin loanword); 

Lithuanian miesiu, miesti {*meikid) "mix', Iterat. maisau, maisyti, Latvian maisu, maisTt 
ds.; also " plow for the second time '; compare Old Prussian maysotan' mixed ', i.e. 
"varicolored'; Intransit. sum/su and sum/stu, -misti^ get tangled, make a mess, get 
confused ', Latvian sam/sf6s.; Latvian /77/5e/"mix, make mad'; Lithuanian ma/sfasm. " 
agitation' m/sras' mixed ', Latvian m/strs6s.; 

Maybe alb. Geg meshoj^press, push', /77esoy "learn, teach (mix in one's mind?), *make 
mad ' 

Old Bulgarian mesg, mes/t/etc. "mix', has lost its iterate meaning. 

Here probably Old Indie a-mfksa "curd of milk', osset. misin " buttermilk ', Middle Irish 
medg, cymr. maidd, ncorn. meith, abret. meid, gall. -Latin */77es^a (French megue) "wheys' 
( *misga). Old Icelandic mysa "wheys' ( *mihswdn-). common Old Indie -gh- > -ks- : lllyrian - 
Celt, -gh- > -d-, -th- 

References: WP. II 244 f., WH. II 95 f., Trautmann 175; Kuiper Nasalpras. 50, 123. 
Page(s): 714 

Root / lemma: meih-1 

Meaning: to strengthen; pole 

Material: Old Indie minotT fastens, founds, builds ', mitf-i. " erection, fundation ', mita- 

"fastens', metar-^ der Aufrichter', mayukha-xx\. "peg, plug, ray', npers. /77ex"peg, plug, 

nail' {*maixa-), sogd. myyk^s.. Old Indie sumeka-^ well founded, tight, firm'; 



Latin PI. moenia^ defensive walls, ramparts, bulwarks, city walls ', munid{ardc\. 
moenio), -Tre^ to wall, defend with a wall, fortify, defend, protect, secure, strengthen '; 
mums, old mo/ros'\Na\\'; 

alb. mur' wall ' a Latin loanword. 

Old Irish -tuidmen {*to-dT-mi-na-t} "fastens', verbal noun tuidme; 

Germanic */775//7/7a- "boundary post, frontier post ', Old English msere, gemsere'\\m\t, 
boundary, region, area'. Old Icelandic /5/70''a-/77^/7" limit, boundary, border land ', etc. 

meih-d(h)-\v\. Middle Irish me{/)derc\. " nape ' {*meih-d-io-)\ Latvian miet^ enclose with 
posts ', maTdtV decorate, ornament, adorn '. 

With /extended me[i]ht-. meiht-. m/t-\n: 

Old Indie methf- m., methTi. (Prakrit medhf-, medhT, medhl) " pillar, jamb ', mft- f. " 
column, jamb ' (perhaps also in Avestan barazi-mita-, if " high column '), Armenian moit'^ 
pillar'; Latin meta^ a cone, pyramid, a conical column at the end of the circus, turning- 
post, goal, a goal, winning-post, mark, an end, period, extremity, boundary, limit '; Middle 
Irish methas^ border land, frontier land ' ( *mitostu-)\ Old Icelandic me/dr'tree, balk, beam, 
shaft, pole'; Lithuanian mietas, Latvian /77/e/5 "picket, pole'; zero grade Lithuanian mita^
```


## [2026-09-07T16:08:21.114Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"mihstu\\|mih-stu\\|miscellaneous\\|meik-\\|meigh-\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-07T16:08:21.166Z] TOOL RESULT

```
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1385:coMAl keme- COMB gembh- COMBAT battuere COMBINE dwo- COMBUSTION eus- COME gWa- COMEDO ed- COMEDY wed-2 COMESTIBLE ed- COMFIT dhé-1 COMFORT bhergh-2 COMITIA  ei-1 COMITY smei- COMMA skep- COMMAND man-2 COMMANDO man-2 COMMEMORATE (s)mer-1 COMMENCE ei-1 COMMEND man-? COMMENSURATE mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1820:Mars Mawort- MARSH mori- MARSHAL marko- MART merk-2 MARTIAL Mawort- MarTIAN Mawort- MARVEL smei- MASCULINE mas MASH meik-
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
1845:MEGALO- meg- MEGALOCARDIA kerd-1 MEGALOPOLIS_ pele-3 MEIOSIS mel-2 MEISTERSINGER sengh- MELANCHOLY ghel-2, mel-2 MELANGE meik- MELANO- mel-2 MELD! meldh- MELILOT melit- MELINITE mélon MELIORATE mel-4 MELIORISM mel-4 MELISMA mel-3 MELLIFEROUS melit- MELLIFLUOUS bhieu-, melit- MELODRAMA mel-3 MELODY mel-3, wed-2
1855:MESO- medhyo- MESOGLEA gel-1 MESONEPHROS negWh-ro- MESOTHELIUM dhée(i)- MESS (s)meit(@)- MESSAGE (s)meit(@)- MESTIZO meik-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1879:MITOCHONDRION ghrendh-, mei-4 MITOSIS mei-4 MITTEN medhyo- MITTIMUS (s)meit(a)- MIX meik- MIXTURE meik- MIZZEN medhyo- MIZZLE meigh- MNEMONIC men-! MNEMOSYNE men-1 MOAN mei-no- MOB meue- MOBILE meue- MODAL med- MODE med- MODEL med- MODERATE med- MODERN med- MODEST med- MODICUM med- MODIFY dhé-1, med- MODIOLUS med- MODULATE med- MODULE med- MODULUS med- MOGUL! miik- MOIETY medhyo- MOIL mel-1
2050:PANICLE pan- PANMICTIC melk- PANMIXIS meik- PANNIER pa- PANOCHA pa- PANOPTIC okw- PANORAMA wer-4 PANSY (s)pen-
2071:PEG bak- PEGMATITE pag- PEJORATION ped-1 PELAGE pilo- PELAGIC plak-1 PELARGONIUM pel-2 PELECYPOD ped-1 PELISSE pel-4 PELLAGRA ag-, pel-4 PELLICLE pel-4 PELL-MELL meik- PELLUCID leuk- PELOPS okw-, pel-2 PELORIA kwer-1 PELT! pel-4 PELTATE pel-4 PELTRY pel-4 PELVIS pel-7 PEN! pet-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
```


## [2026-09-07T16:08:31.367Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- BRT maez ---\"; grep -n \"maēz\\|maez\\|maêz\\|maeza\\|mazaiti\" BRT.txt | head -30; echo \"--- BRT maega ---\"; grep -n \"maēγ\\|maeya\\|maega\\|maêγ\" BRT.txt | head -30"
}
```


### [2026-09-07T16:08:31.430Z] TOOL RESULT

```
--- BRT maez ---
9839:•  j.  gao-maeza-  m.  'Rindsharn',  als  rituelles Reinigungs-   und    als   Heilmittel'*:    'am
19503:j.  'tnaez-  V.  'harnen'.   Fraes.  3  maeza-.
19506:ai.  mlkaii,  np,  metaä.  —  Pü.:  mitiOH  (GltPh. /.  301,  Sp.  VendPü.  so«,  3..1etzte(  Wort)  — ■)  Hds.  yoftff,  aber  Pti.:  mnä». g.  »maez-  V.  'hegen'.  Praes.  3  mua-. 'hegen,  sorglich  pflegen  (das  Rind)': yais  gqm  karapa  usixJ(sd.)eS  ai&mai  data
19509:"^maezant-
19514:•  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i).
--- BRT maega ---
14500:•  j.  ftray-  Zw.,  fem.  tisr-  'drei',  Plur.: nSit  atvd  nSii  dva  nsit  %rayB  (Nm,)  nSit\ fräyanhs  T.44',  —  aivahe  pasvS  .  .  dvä ..  iryam'^  .  .  caturqm  N.  65;  —  aSva lirUva  ,.  dva  %riiha  . ,  %ribyS  %risvaiiöyö V.  2.  ii£;  —  aevahe  ..  *as)maeyahe  .. dvayä  .  .  %rayqm  ,  ,  caiiWärS  V.  iS.ii; F./,  P.2^,  V.  1$.  49,  iS.  17';  —  %rays zavainti  gäusca  aspasca  haomOscaY.ll.i; 20,3,  21.  i,  Az.  5J,  Vyt_5;  —  aitbyö  ratu- byS yöi  hinti  %rayasca'^  %risqsca  "..33.." Y. /.  10;  —  "ibräyd  (als  Am.)  anya  maya nihw?r»sBii  V.p.  9;  ti^,  5. 10,  Vd.  12;  — är(/(Ain.)  mätahs  ußa.baolayan  .  .  xAias mänhs  V.  7.  i4f.i  N.  66,  67,  '88.  57^;  — ^ris  mayam^^  ava.kanaym  V.  Ä37,  16. 12;  j.  51;  —  %rJ  (An.)  *malima.safnqn asamäj  P. g;  — -  %rlvä  azsiti  (sd)  sraois.-
19439:•  j,  "maeya-  m.  'Grube,  Kuhle"':  yai  nsii spa..'-]e  vä  iäili  vä . . paS>yäite  V.y.37,
```


## [2026-09-07T16:08:37.248Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Wolke\" BRT.txt | head -30; echo \"=== maesman ===\"; grep -n \"maesman\\|maêsman\\|Harn'\" BRT.txt | head -20"
}
```


### [2026-09-07T16:08:37.308Z] TOOL RESULT

```
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
4000:•  j.  awra-  n.  i)  'Regenwolke,  Wolke': yaha  'nm  vätsJsism  Y,(?.32;  —  'ra upapä  Yt  74.41;  —  'm  F.7.  2)  "Regeii, Regenschauer':  ma?ya  .  .  yähva  urväi/is (sd.)  'r&  Yt.Ä40.
4001:KompE.   —    ai.  aikrä-   n.  'Wolke';    np,  abt •Wolke',  afy.  erif  'Wolke',  baJ.  haur  'Regen'.
10040:ser: US  vS  apqm  aaavS  apaitijrsta  jashnti Yt.  (?.  29.  c)  'aufsteigen',  von  Wolken: namia  dunman  (sd.)  uzjasaili  harat^yS Paiti    bartzayh    Yt.  iQ.  50.  a)    'in    die
13680:•  j.  dunman-  n.  ''Nebel,  Nebelwolke, Wolke':  yayata  'ma  ,  .  frä.ap3m  nyäpftn upa.3p^m  (sd.)  V.21.2;  F.^g;  —  apim.. MdSrra  vat>m  'mqnia  ¥.5.15;  —  naioa 'man  utjasaiti  haratky3  paiti  banzayä "und  nicht  steigen  Nebel  empor  von . ."  Yt. 10. 50;  —  Hat  tat  'man  hqm.hishnti  . .  äat tat  '"tan  frasäupayeiti  (sd.)  magyS-kara Yt  S.  31 1
13682:•  j,  dunmö.frut-  Adj.  'in"  den  Wolken fliegend':  vats  (NP.)  vänti  'tB  (NP.)  xä paiti  Yt/J.i4-
13683:*/rut-  Adj.,  zum  V.  /rav:  —  ai.  'prul-  Adj.  — >)  Oder  auch  'mit'  oder  'mittelst',  wenn  die Wolken  als  Flügel  des  Windes  gedacht  wur- den.   DsT.s  *poussant  tes  nuees'  ist  unrichtig.
13993:•  g.  dv^nman-  n.  'Wolke':  k!  vätäi dvqnmaibyascä  yaog3t  äsS  "wer  verband mit  Wind  und  Wolken  die  Schnelle?"  Y.
17774:mit  US  1)  'aufziehen,  aufsteigen',  von Wolken :  äat  magya  usfravante  . .  yahva  . . "alsdann  steigen  die  Wolken  auf  . ."  Yt, 8. 40.  2)    Kaus.  'hinaus-,   fortschwem-
19433:•  ].  'maej'a-  n.  'Wolke':  andvlm  ..yaiAe ca%wärS  arläna  hqmdälat  aAurS  masdS vat?mca  värimla  -jgmla  fyaahum^a  Yt 5.120;  ÄSS,  Y.io.3;  —  Bat  *ya^*  ui.- fravänti  kuyäirya  äpö  öanntii'  ySkva  . . p?r3%u  aipi  vjJasSitlS  avS  urvaitls  (sd) "dann  steigen  die  Wolken  auf,  die  die  . . Wasser  enthalten,  (die  Wolken)  in  denen . .,
19440:Et.?  —  Pü.:  wa'>-  —  '>  Oder  dgl.  — »)  Wohl  nur  Transsltr.  'Wolke'  (Horm  NpEl. 236)  kann  doch  nicht  gemeint  sein.  Zu  V.  T3 \iX  PQ.  nicht  in  Ordnung;  m  d  z  n  an  n.
22600:feuchten  Wolken  von  oben  her  die  grossen
22981:Zum  V.  Ivat:  —  ai.  ürmäy-  f.,  sbal.  ^tiarm; PDs.  T/arm  'Wolke,  Nebel'.  —  Vgl,  a^a-i.- varalay:
23483:Ir.  wohl  'sfä/fcSä-  (IF.  p.  261),  Bildung  mit Int-Red.  —  ")  Ohne  Wert  Gdn.  KZ.  ij.  551 1 'Wolkenbruch',    Dst.   ZA.  2.  5491    *rinconti-
25655:•  j.  'urvant-  Adj.  (fem.  'vSiti-)  'flicssend, strömend',  auch  mit  Akk.  des  Inhalts'*: maiya  .  .  yahva  'väitii  (NPf.  statt  n.) awra  p)r3hu  aipi  vJjasäiti?  avS  "vaitTs (NPf.)  hapta  kar^qn  "die  Wolken  . .,  in denen  die  strömenden  Regenschauer  ent- halten sind,  die  Wasser  strömend  sich  gar weithin  verbreiten  über  die  sieben  K.  hin" Yl  Ä  40 ;  —  andvt  süra  . .  frä  . .  sispata *'vaiti''>  iaBu.staayeAi  (sd.)  Yt5.  7.
29197:•  j,,  g.  ha'ÖTä  i)  Adv.  "an  einem  Ort, zu  gleicher  Zeit;  zusammen,  zugleich': ap»m  tazähi  tatn  yö  ahurS  mazdä  zra- yanha^  hata  vouru,kasät  °ra  vstimca  dun- mqnca  "entlässt  du  . .  das  Wasser  aus  dem Meer  V.,  zugleich  den  Wind  und  die Wolken"  V.  5.  15;  Vyt  42(?);  —  tä  'ra fra/rSvayühi  avi  zrayü  .  .  V.5.  16;  10; —  mit  vfspa-  'alle  zusammen"':  na^a vUpe  'ra  daiva  mahrka%ai  upadarznvainii
=== maesman ===
19489:•  j.  maesma-  m.  'Harn',  als  rituelles j  Reinigungs-  und  als  Heilmittel  verwendet*';
19493:■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a
19497:•  j.  *maesinaAima-''  n.  'Schluck  Harn': "  rJ  .  .  ^'mqn  '>  aiamai  (sd.)  P.  g.
20581:ai.  mu/ra-  n.  'Harn'.  —  Pü. :  nmkrdjin,  muht- däi  (geschr.  mn  l  r*).  —  ')  Mit  u  F.  11.
27125:—  yd  .  .  rapthwifom  .  .  JrSyasäite  Jra- snälaiibya  xastaäbya  frasnataltbya hüvanalibya  A.  4-  Si  V.  <?  40,  i<y.  19;  — zasta  hl  paoirlm  frasnatayM  V.  8.  40, 16.  T,  —  vasirä  frasna^aytn  massmana gSus  V.  7.  13;  14';  —  taita  . .  hak^nt /rasnahaym  maümana  giul  .  .  halant apS  ß-asnäiayM  V.  7.  74;  —  aSaia  .  . "krii  may^m  (sd.)  avaAanaym  dva  maja /rasnälaym  maesmana  gius  *Hm  apS  V, j6. 13;  —  Med.  in  reflex.  Sinn:  fra  tasta snayaauha  V,  18. 19;  —  tanUm  frasnaya- yanta  \X.io.  laz*;  —  malsma  .  .  yaiibyS (statt  Instr.)  . ,  nasuMala  frasnyänte  van-
29557:AbleiL  aus  hi-apak-  r.,  S  'OO  a.  a.  —  Pii. : Itanssltr.,  mit  der  Erl.:  niisak  'Harn';  vgL  lu
```


## [2026-09-07T16:08:42.158Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19425,19520p' BRT.txt"
}
```


### [2026-09-07T16:08:42.215Z] TOOL RESULT

```
Ableit.  —  ni.  mam,  mal;  mä,  mt;  np.  man, •m  (aas  ir.  *inai);  vgl.  noch  S  '46,  423.  — Pö.:  man;  s.  noch  No.  I,  3,  6,  II.  —  0  Die Scheidung  zwischen  maityä  und  maiiSfä  im  Ge- brauch ist  uiffÜÜS.  Pü.(m*ist):  maniiän;  s.  lu mauant;  —  >>  öfters  ist  dei  Nachdruck,  der  auf
'mae}«-
V  gäanjn.  —  7)  Hinter  dep Vokativ  mazdä  fallt  eine  Pause;  s.  Bthu  AF. 3.  25.  —  «)  Vgl.  Y.  48.  a,  wo  parä  hyat  mä; s,  'mä  3.  —  9)  In  gAw.  Lautform;  Vgl.  Y.  J3. *  c.  —  '")  Der  vorhergehende  und  der  folgende Sati  enthalt  mqm  als  Akkusativ.  —  »>  Das in  L4,  Kl  fehlt;  F&.  freilich:  man.
•  g.  "ma-  Adj.  (fem.  mä-)  'mein,  memig"; a)  attrib.:  »»?  (KSm.)  urva  ^s7ä  azya (sd.)  Y.2g.t,;44.B;  —  kj  mS  nä  '^rätä vistS  Y.  50. 1 ;  —  makmai  hyätä  *avaAhl ^■50.  7;  —  tä  «tSj  *mainySul  maAys  .  . g3rm{sA.)  Y.^S.9;  —  AizvB  rai^lm  (sd.) stsi  makya  Y.50. 6;  —  vahistä  mahyh is'IBii  Y.46.1S;  50.9,  44-io;  —  mahmi manSi  (sd.)  Y.  J2.  i ;  —  inai^ä  (sd.)  mayä (ISf.)  Y.j^.9.  b)  pracdik.:  »«i(NPn.) kamnafhä  (sd.)  Y.  4Ö.  2.  [Y.  ^.  1 2 :  lies ali>mahyä^
Ableit  aus  ■ma..  —  gr.  vgl.  iftii.  —  Fü-: (i^  man,  am,  (lu  Y.  _y ) :  pa  falmäit.
•  g,  maekant-  Adj.  (fem.  'iainil-)  'hervor- ^ckemd,  quellend':  aps ..  "kainttscä  *ksba- vaintlscä  fravasaahs  "die  hervorquellen- den und  (dann)  sich  zusammenfindenden (und    dann)    fortfliessenden    Wasser"    Y.
*)  Die  spätere  Theologie  sieht  in  maekainli- und  andern  Wörtern  von  Y.  38. 3  ond  5  siebzehn Namen  bestimmter  Flüssigkeiten ;  vgl.  Bd.  11.  1 : pa  din  haß  lo  sarlak  i  äp  ('17  Arten  Wasser'J giifi  und  deren  Aufzählung  nach  dem  GrBd.  bei DST.  ZA.  /.  265,267.  Bezeichnender  Weite  er- kennt sie  solche  Namen  auch  in  dem  GS.  ahu- rahyä  (Samenllüssigkeit)  und  in  ubcibyä  aiulryä cagimä  (ausgelassene  Butter).  Diese  Deutung ist  wohl  durch  Y.  38.  4;  üilJ  yä  vi  vamikii (näml.n/ö]  ahutS  maxdi*nämqm  (/«^veranlasst fiie  ist  wertlos.
PPA,  einer  Basis  ir.  *maii-  'hervorquellen'; vgl.  np.  niaiTt/an,  mazidan  'saugen,  schmecken', sbaLmi<-Vsaueen'(usw.,  beiHBM.  PSL  137)'). —  Pü.:  transskt.  und  erl.  :/a  umar  eslel{aiso Fflanzensaft).  —  >)  Wegen  der  Bedeutungs- diflerenz  verweise  ich  auf  ahd.  iwrüait  'her- vorquellen'und  j;EiAi'sapor'DEW.,woznGsTllOFF rBtB.  8.  279  auch   ahd.  sim,g^  '»äugen'  «teilt.
•  ].  'maej'a-  n.  'Wolke':  andvlm  ..yaiAe ca%wärS  arläna  hqmdälat  aAurS  masdS vat?mca  värimla  -jgmla  fyaahum^a  Yt 5.120;  ÄSS,  Y.io.3;  —  Bat  *ya^*  ui.- fravänti  kuyäirya  äpö  öanntii'  ySkva  . . p?r3%u  aipi  vjJasSitlS  avS  urvaitls  (sd) "dann  steigen  die  Wolken  auf,  die  die  . . Wasser  enthalten,  (die  Wolken)  in  denen . .,
dby  Google
II05  *mae)«-
die  sich  .  .  verbreiten  . ."  Yt.  S.  40;  — asyattha  (sd.)  'yaHiya  Y.57. 28,
KompA.  —  ai.  migkä-  m.,  np.  mtf.  —  Pü. : undeullich '),  Sü. :  megha^.  —  >)  NI^.;  dailLuf beziehen  sich  die  folgenden  femininen  For- men iarfntiJ,  yähva  usw. ;  S  4'3  aE,  —  ')  Vgl. ',
HoRN  NpEl.  284;  ZDMG,  56.  117.
•  j,  "maeya-  m.  'Grube,  Kuhle"':  yai  nsii spa..'-]e  vä  iäili  vä . . paS>yäite  V.y.37,
Et.?  —  Pü.:  wa'>-  —  '>  Oder  dgl.  — »)  Wohl  nur  Transsltr.  'Wolke'  (Horm  NpEl. 236)  kann  doch  nicht  gemeint  sein.  Zu  V.  T3 \iX  PQ.  nicht  in  Ordnung;  m  d  z  n  an  n.
•  j.  maeyö.kara-  Adj.  'wolkenbildead': äat  tat  dunmatt  fra^äupayäti  (sd.)  'ra (NPn.)>t.Ä33'.
•  j.  mact-  V. 'weilen'.  Praes.  11  mfönJ-, 34  mitaya-.
i)  'weilen,  wohnen':  va^hu^  sraols mitayatu  asisvatsuki  tha  mi^natu'^  Y.io.i; — yahmi  zl  kacit  tanunani  dräpHim  (sd.) . . mag^aine  mi^näj  Y.  16. 10.  2)  'bleiben': ya^a  granis  .  .  mtimaUi  miäsra  Yt  10. 39.  3)  'dauerad  vorhanden  sein':  tia mi^thit  .  .  ai?iAai  gunäayäi  (sd.)  V._j.  32,
VgL  iEL  unter  mai%ana:  —  Pü. :  mändan.  —
■)  Them.
•  j.  tnaid-  V.,  nur  mit  harn  'nieder-,  zu Boden  werfen,  unterdrücken'.  —  PPfP. °mtita-,  Inf.  "mistSe,  •mistayae^a.
avas3.xsa%rS  kyatdrvä  gatJ hamistö'^ nisbirsts  haca  spmtahe  mainySu^  dämabyd ".  .  gewichen,  unterdrückt,  weggebracht von  .  ."  Y.  Ä  6 ''.
Vgl.  ags.  imitan,  nhd,  schmdsstn;  %  S/3>.  — S.  auch  hamaislar:  —  Pü. :  karacstärik.  —  •)  m für  'm+m%  %304  11.40.  —  ')  Vgl.  Y.Ä/.  2, 5.  —  3)  Die  Zusammengehörigkeit  der  Aw.. WÖTter  mit  an.  tneüta,  lelt  mailat  usw.  (s.  Zv- FiTZA  BB.  25.  98)  ist  auch  möglich,  doch  passC deren  Bedeutung  nicht  so  gut.
•  g.  maeÖ'-  V.  'mittere'.  Fraes.  a  mafh-: OT/ä-,  II  mihnä-.
mit  Abi.  '(emittere  ex  — ,  hinauslreiben  aus —  sva.)  berauben':  yastSm  x/ahräl  mazäa mSikat  jyalSus  v3  "wer  ihn,  o,  M.,  der Herrschail  beraubt  oder  des  Lebens"  Y. 46.  A.
mit  a  (etwa)  '(an  sich)  kommen  lassen': ayarS  amihnäiti  juye  tanul  frayaire  ayan bavaiti  (sd.)  AubairS  "den  Tag  muss  man  im Leben  an  sich  kommen  lassen: . ."  Aog.55.
mit  paiti  '(zurückschicken  sva.)  den Laufpass  geben,  absagen':  avä  Alm  paiii.-
maeS'ana-
IIOÖ
m^naifi  vispfm  du^mattmca  . .  "jener  dort sagt  ab  allem,  was  Übel  gedacht  ist  und  . ." V.J.  20.
mit  Aam  dnwS.:  ys  x£ fy&tJui  Asm^yar^ vai7.it5iSc<l  "der  sie  des  Lebens  und  der Freiheit  beraube"  Y.  5_j.  9.
mit  ham  und  aibt  'zulassen,  den  Zu- tritt gestatten'  (in  das  Reich)'':  ai  is  voAa ASm  aibj.msisf  manaNAä"''  aäbyS  raföräi mazdä  sastl{%^)  Y.46.12.
Ar.  'mailA-;  Tgl.  lut.  mitten  (mit  idg.  /;  S. daiu  S  52-  2,  Bgm.  Grdr.»  /.  632).  —  Pü-  (zu Y.  46) :  hamesläteHisn  hind,  erl. :  kac  vinäs  apil apäyiiid  dästaa  u  ianiin  hind,  {m  Aog.):  mtnet •er  denkt'«,  (lu  V.5):  mUtiilaa  (Transskr.), (zu  Y.  S3\.  kf  ösän  ianit  vasä»  kan,tstärl,ül, erL:  ht  Jan  hat  vinäs  apäil  därit,  (mV.  ^5): öfö«  pa  valmman  mänend  pa  frärSmh.  —  >)  « für  •m-fm-  %304  IL  40.  —  »)  Vgl.  V.jo.  8(anler la/Cfl-).  —  3)  Sa.!  Hnlayati.  Aber  Pü.  zu  V.J.  20 lässt  doch  m  ddn  dt  ^muMcf  vermuten.
•  g,  maeOa-  Adj.  (fem.  -äa-)  'schwankend, wandelbar":  kyat  Aa%ra  (sd.)  manh  bavat
^ya%rä  Hstil  avAat  "Sa  Y._jo.  9.
Zum  ai.  V.  mtthele  'sie  schwanken  hin  und her'(?)»),  got  inmaidj'an  'immatare' (usw.).  — VgL  M«äö.,  mSiö;  Gdn.  BB.  15.  257.  — Pü.:  andar  mikan.  —  0  RV.  /.  113-  3i  im Gegens.  lu  laslhaiufy.  SSVa^/a  freilich /o/rw- fararn  Aimilah.
•  ].  maeS-ana-  n.  'Aufenthaltsort  für Menschen  (und  Götter),  Wohnung,  Haus': UnAam  asanAqmca  sBt'^ranqmca  gaoyaoitt- nqm'ca  'nanqmca  Y. /.  16;  ' —  ya%a  ass °mmca    atwisitSe   i/aää«i  (sd.)    Yt.y.67;
—  aAe  i'rje(sd.)  uta  'mm  Y.  10.  7  Gl.;  — rältim  aAmäi  naire..  mi^rS  "ntm  Scaraiti "stracks  kommt  zu  dem  M.  ms  Hans" Yt.10,137;  —  tum  'nahe pata..adruzqm Yt.iO.8o; — yazamaide  ^Toam  'mm  yam ärmaitim  . .  yazamaide  %wqm  'nahe  paiti .  .  aAura  mazda  ,  .  drvS.vlrahe  .  .  yaAmi zT  käBt  tanunqm  dräplttm  (sd.)  harne '%aine  mi^nai  "wir  verehren  dich,  o  Arm. (Erde),  als  unsre  Wohnung,  wir  beten  zu
I  dir,  o  AAM.,  um  eine  Wohnung  .  .  mit gesunden  Männern . .,  auf  dass . ."  Y.r^.  10;
—  aefqnt{sd.)at . .  'nahe  x"ai  pairigiurva- yeiti  V.  4. 1 ;  '•'iPüZ.'';  —  avantariqm  (sd.) 'nanamca  Vd.  2;  —  maaAimca  'nmi^a myaidtmca yazamaide  Yt.<?.  1°^;  —  m^r?m ..yetihe  z^m.fra^ö  'n?m  viZälim  YtlO.44; go,  79,  81;  —  avi  garJl  nmätmn  'tmn aAuraAe  mazdä  'mm'  .  .  Y.iff.^i;  zit Sl.  r_j.  8.
Ableit    —    Zum  V.  maet-i    wegen   des  ^  t.
dby  Google
107
tnaeSan]^-
1108
S  Ä  —   i^  MÄto»;    »jL  kiL  athla  'Ort'.  —
PK.:  mihan,   erl.  (in  V.  4):  dnifut  gas;    (lo
V.  i-ff);   Jwä«,  mäniln,    (in  V.  /p):  mönl),  —
■>  Hds.  mai%imnahi%   i.  Var.  lu  V.  ^  l.  —
»)  ScbweiUch  richtig  überlicfett   —    9  Aber
mihan  im  ZtUt  des  SL
•  j.  mae^anyä-  t  "Wohnuiig,  Behausung':
asäsca  ,  .  yäsca  Y.  2. 1 6,  Ä  1 5 ;  —  xrBmä
saitays  fraänte  (sd.)  anaÜtä  'ya  (NP.)  Yt
•  g.  maeVä-  £1)  'Schwanken,  Unsicher- keit': d/w/.^u/'^rmaii^miiin)«  *pprfsaiti yäira  'ää"  "von  einem  zum  andern gehend  bespricht  sich  Arm.  mit  dessen Geist,  der  noch  schwankend  ist"  Y.j/. 1 2  ".  2)  'Schwenkung,  Wandel' :  at  tat «01  daxitfm  data  ahyä  at»hsus  vitfa  "üä "so  werde  mir  das  als  Zeichen  gegeben: der  vollständige  Wandel  (der  Dinge)  schon in  diesem  Leben"  "^.34. 6;  —  a{  toi  tnazdn tfm  mainyüm  .  ,  '^a  (IS.)  mayj  vahistä bar^ü  manaaha  "Deinen  Geist,  o  M., . .  soll  bei  dem  durch  mich  bewirkten Wandel^  (der  Dinge)  VahiltaManah  herbei- bringen" Y.^.9«.
Vgl  miü%a:  —  Pn.  (dRn.):  mehan,  mänänf, mämnim.  —  ')Wört].'wo(,beiwcm)Scliwanken (iit)',  näaiL  ästBii;  i.  Y.  ja  9.  —  "1  Vgl  Y. 46.\i.  —  St  Wörtl.  •mttlelsl  meines  W&DdeU'; du  pTon.  pou.  in  prägninlem  Sinn.  —  4)  Gdn. bat  bisher  drei  TSUig  verschiedene  Über- seuangen  der  Strophe  geliefeit,  Stod-  i.  31, KZ.  28.  40S,  BB.  IS-  250,  257- j.  maiXimmUu  V,  4.  PüZ.  1 :  lies  mai%anaAe.
•  ].  maefhnannn  Inf.'>  'sich  zu  paaieu', vom  Hund:  y^  z/asm  mazdayasndjvS.- daxlt>m  (sd.)  m'  "wenn  die  AI.  wollen,  dass ein  läufischer  (Hund)  sich  paare"  V.  15.  46.
V(;I.  m&-aiana-.  —  aL  vgl.  mithan'ikaroli  usw.  — Pü.:  mdd  (wohl  slaCt  m  da  =^  mih) -rm/aK, erL:  ginor  tarlan.  —  i)  Auffällige  BilduDg. Ob  mit  Jp  t,  &ff  z  iHai%anJtn  lu  lesen,  Inf. wie  im  Germanischen?
•  j.  maenabtan-  m.  Name  eines  Bergs oderGebirgs:  akmat  kaca  garayB fragxsyan .  .  aaaxasca  'xas^a  (NS.)''  Yt  ig.  4.
Eig,  "wo  die  Quelle  des  -Vo/nailusses  liegt'; s.  lu  arzaxan-  und  ai.  mcnä-  f.  Name  eines Flusses').  —  OS  405.  —  »)  Die  oft  wieder- bolle  ZasammenstelluniT  mit  ai.  mlnaiä- i^o\!) f.,  luletzt  bei  Gge.  OK.  131,  ist  falsch.
•  g.  ■•'inaenay-  £  'Strafe,  Bestrafung' :  p?r9sa avat  ya  •«mj'J.  .  "darnach  frag  ich,  was die  Strafe  ist  (fiir  den),  der  .  ."  Y.j/. 15.  a)  mit  Gen.  dessen,  woftir,  und Akk.  dessen,  an  dem  die  Strafe  vollzogen
wird:  kä  ßm  ahyä  'nü  attha^  *pacuntyt "welche  Strafe  wird  den  dalür  zm^chst treffen?"  Y.44.19.
ai.  menäy-  t 'Rache';  vgl. GdN. Festgr.  Boeht- lingk  31.  —  Pö.:  voiätän  fäöfräs,  in  Y.  44 erL:  viitäiiärii  fiääfrä],
•  j.  maesma-  m.  'Harn',  als  rituelles j  Reinigungs-  und  als  Heilmittel  verwendet*';
im  Flur.:  Aam  aSe  *Ma  (AP.)  baraym tyaÜhfB  aUe  nasuiala  frastr^änU  vamäsla tanümca  Y.8. 1 1 ;  —  aäe  'ma  (AP.)  maaa- yanta  yaäbyS  , .  V.Ä  13;  —  cayS  .  .  aSe •ma  (AP.)  aaim  .  .  yaHbyS  .  .  V.  Ä  11; F.^g.
*)  Insbesondere  gilt  das  vom  Rindshara  (a. ^armofta-)!);  TgL  dazu  DsT.  ZA.  3.  266,  Schka- DEK  RealL  103 1.
Zam  V.  'nnÄ-,  J  V^  '-4-  —  ^ß'-  "laämait: —  K.:gümä.  {in  V.  Ä  13) :  rnÜai'),  (lU  F.): m««  (in  Aw.-Bach5t.>  —  »  VgL  V.  *.  12  t  — ')  Oder  tIL  mHaJt  aas  ar.  'maqiAa-  ?
■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a
—  aitä  vasträ  JrasMaoi^fn  •managfui'V. 7. 13;  14,  74,  16. 12;  —  gSus'mana  OtryS.- paiüiristtm  (sd.)  V.J.  51.
KompA.  —  Zam  V.  "marä-,  —  Pü. :  gimh.  —
I)  Vgl  in  moimia:
•  j.  *maesinaAima-''  n.  'Schluck  Harn': "  rJ  .  .  ^'mqn  '>  aiamai  (sd.)  P.  g.
Zum  V.  iam:    —    Vgl.  sama-.  —  K.:  apisa-
maki')  (miisma  ist  nicht  übersetzt). —  <)  Hds.
(nach   DsT.)    maisma   iamait;   aber   BLOcaST
Lei.  156  hat  iitmqit.  —  »)  Das  wäre  etwa  ir.
'ufail-samaJi'.
j.  'tnaez-  V.  'harnen'.   Fraes.  3  maeza-.
'harnen,  Hain  lassen',  von  Menschen und  Tieren;  yat  is  faiti  fralsttm  maf- isnli  pasvasca  staoräca  V.J.  6;  —  -ia«- hqm  na  gäisanqm  .  .  aratujriit  ya *maizS*^  vä  *frä  va  saimns{sA.)  srSva- yeiti  N.J7.  a)  mit  Inhaltsakk.:  par(^t dvaHbya  yOi  aahtn  i^altvada&asca  a^ai- tvadai^Ts^a  aae  malsma  malsayanta  (Opt) yaiibyS  .  .  Jroinyante  V.  8. 1 3.
mxfrä  'nach  vorne  pissen  vor  — ,  hinans- pissen  über-' (Akk.)  ;^ai  nä  faurva  Jrabda (sd.)  frahdöJräjO  framauaiii  V.  18.  40.
ai.  mlkaii,  np,  metaä.  —  Pü.:  mitiOH  (GltPh. /.  301,  Sp.  VendPü.  so«,  3..1etzte(  Wort)  — ■)  Hds.  yoftff,  aber  Pti.:  mnä». g.  »maez-  V.  'hegen'.  Praes.  3  mua-. 'hegen,  sorglich  pflegen  (das  Rind)': yais  gqm  karapa  usixJ(sd.)eS  ai&mai  data
dby  Google
:io9
"^maezant-
, .  nSit  htm  mltSn  a/5  västrwt  frädaiähi "wie  sie  . .  das  Rind  der  Raserei  preis- geben, statt  dass  sie  es  hegeo*',  um  durch Asa    die   Landwirtschaft  zu   fördern"   Y.
Aus  »x.'smaif-;  %.  tahd.  smiUkm  'schöntun'.
—  Pü.:  paia  ntiid,  Sa.  i  frasädcfu.  —  0  Wört- lichi  "nicht  faber)  hegen  sie  es,   um  .  .",  —
—  1)  JusTls  Obeisetiung  PrJ.<Kf.247  verstehe ich  nicht
•  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i).
•  j.  maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7.
KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL
•  j.  maeäina- Adj.  "vom  Schaf  herrührend, daiiir  bestimmt,  ovillus':  'Hmm  yavaah?nt Aog.  82;
ÄbleiL  aus  nia^io:  —  Pü. :  meiii,  mätak  i  mii
•  j.  maoSanö.kara-  Adj.  (fem.  °kairl-) 'Lust,  Wollust  bereitend':  jahikayii  .  . •kairyäi  Y,p.3a,
Vgl.  ahiinuita:  —  ai.  moiiana-  n.;  vgt,  moda- m.  'Lust'.    —   Pü.!    mülai   (Stt.:   mandatvam) tartär,  erl.:  Hc  iapäh  kuncl;  vgl.  unlermräfa-. j.  BiaairJ':  s.  maurvay:
```


## [2026-09-07T16:08:55.106Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN mig ===\"; grep -n \"mîġ\\|mîg\\|mig \\|meġ\\|mêġ\\|Wolke\" HRN.txt | head -40"
}
```


### [2026-09-07T16:08:55.158Z] TOOL RESULT

```
=== HRN mig ===
1007:63. ebr *Wolke .
1009:ap. 'AßpolKo/LiTjg Herod. ; aw. awra- 'Wolke* ; phlv. awr
1011:arm. amp, amb 'Wolke (H. No. 14); kurd. avr, awr,
1773:(H. -Seh.); af/. varyaj 'Wolke*, varyaz, var-edal
8778:1009. mey *Wolke .
8779:aw. maf.ya- *Wolke'; phlv. mey ^ vd. 15 (18); ai.
8781:oss. d. meyä, t. 7nty *Nebel, Wolke' (185).
10753:Wohl kaum in der Bedeutung 'Wolke'.
```


## [2026-09-07T16:09:02.440Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\n# compute leaf index per line\nleaf=0\nres={}\nfor i,l in enumerate(lines,1):\n    res[i]=leaf\n    leaf+=l.count('\\f')\n    # form feed may be within line\nfor ln in [1007,1009,8778,8779,8781]:\n    print(ln, 'leaf',res[ln],'printed~',res[ln]-21)\nEOF"
}
```


### [2026-09-07T16:09:03.787Z] TOOL RESULT

```
1007 leaf 37 printed~ 16
1009 leaf 37 printed~ 16
8778 leaf 247 printed~ 226
8779 leaf 247 printed~ 226
8781 leaf 247 printed~ 226
```


## [2026-09-07T16:09:09.138Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# leaf index i = i-th page (0-based). printed = leaf-21\nfor printed in (12,219,226):\n    leaf=printed+21\n    print('='*20,'printed',printed,'leaf',leaf)\n    print(pages[leaf][:2600])\nEOF"
}
```


### [2026-09-07T16:09:10.469Z] TOOL RESULT

```
==================== printed 12 leaf 33
12 -
49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen.
Im Awesta und Altindischen wird die Bedeutung
gnädig sein, verzeihen' durch das Wurzeldeterminativ
d aus der [/^merg- ^abwischen' gewonnen, vergl. aw.
merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
87, während Brugmann, Indog. Forsch. I, 171 auch
an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt).
50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis,
phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ;
lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum
können bringen" (Kurschat), moJdnus (refl.) 'ich lerne'.
Die Zusammenstellung stammt von Spiegel (Tradit.
Lit., 360) ; sie ist indess lautgesetzlich unmöglich, da
lit. (d. i. ö) arischem ä entspricht. Skr. ä + [/"muC'
heisst nur ^bekleiden*.
51. ätney(ten 'mischen , Praes. ämez-em, ämezis^ ümeze, ämey,
vergl. enduh-amey (Vis und Rämin, Seite 83 Vers 16).
phlv. ame/tan, ämeßt (Bund.) mischen*; aw. vergl.
hememyäsaite *sie mischen sich zusammen', minas *du
vereinst' (Bartholomae, Ar. Forsch. III, 61 Anm.;
II 170); skr. a-\- l^miks- f mischen*), vergl. ^miisä-
'Quark', neben ai. migrä- Vermischt*; vergl. gr. ulyw^u^
/List^ai etc.^).
52. an jener*.
Die heutige Aussprache ün findet sich schon in der
bukhärischen Psalmenübersetzung (Et he, Litbl. f. or.
Phil. I, 191).
päz. a7i bez. hän (Aussprache für die Ideogramme
■^T und auch nöD), phlv. in an-gün, an-c.
Zu aw. a«-a, an-agäo, an-äis; skr. an-aycC, Der
Übergang von der aw. skr. Bedeutung 'dieser zu jener'
ist derselbe, wie in ksl. onü^ lit. ans, lat. ollus {*onlus) ;
^) Np. äme/ten hat mit np. meßten (No. 1006) nichts zu thun, wie
Fr. Müller, WZKM. 5, 351 will.
==================== printed 219 leaf 240
— 219 —
975**** nie%*y zum Viehfutter dienendes Gras', meryzar *()rt,
wo mery wächst', arab. LW. inarj *Wiese\
aw. mareyOr *Wiese' (Hübschmann, ZDMG. 46, 244
No. 75); arm. LW. warg 'Wiese', syr. LW. n:i*1D 'Wiese'.
kurd. mirkj merya 'Prairie'.
V
976. meryzenf merzyen, merzyän 'Kirchhof (Beleg bei SF).
merg Tod' -r phlv. özan *Da;Kma', np. (Riväyet)
meryözen (Darm es teter. Et. ir. II, 132).
Ganz unsicher, da die PehlevTform (NB. )XTN oder
JNin) unklar ist; die Verknüpfung mit ap. apadäna-
ist vollständig verfehlt.
977. merg *Tod'.
aw. mahrkor 'Tod*; phlv. marg\cirjan^ marißh 'Tod';
arm. vergl. waÄ, warA 'Tod' (H. No. 185).
kurd. merk 'Tod'; bei. mark; oss. d. t. marg *Gift'
(178 e).
Der Bedeutungswechsel im Ossetischen könnte als
ein Analogen vielleicht auch die Ableitung von np. mar
Schlange' aus l^mar^ sterben* bezw. deren Causativs
*tödten' rechtfertigen.
978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
schaft'.
aw. mUda- 'Lohn'; phlv. m(i)zd (paz. mozd), mtizd
(AV.); ai. midhd- 'Kampf, Wettkampf; got. mizdö
'Lohn'.
oss. d. mizd, t. m^izd 'Bezahlung, Vergeltung, Lohn,
•Belohnung' (188).
Das u im Neupersischen ist auffällig.
979. me^^yiden saugen, schmecken', meze 'Wohlgeschmack',
meklden.
g. meöcLdmün\ Käs. Q. hdmij, K. bemüj, 7j, oermez;
Q. mitSn, K. vermSt {*mi/ten),
phlv. micUan (Bund.), midak 'Wohlgeschmack (Men.);
kurd, mltin^imlßim 'saugen'; bei. micagj n. misay 'saugen'
(235).
Von einer l^meq/c- 'saugen*.
980. miSe, muze 'Augenwimper, HJD (Jer. 9, 18).
g. müjeng; Käs. mejd, mujd^ mezL
==================== printed 226 leaf 247
— 226 —
passt der Bedeutung und des t halber schlecht ') ; ob
besser zu ai. siimeka- zu stellen (Bartholomae,
ZDM6. 44, 553), ist auch zweifelhaft. Sehr unsicher
sind die Lautverhältnisse von af/. woyai bezw. wökii
*Pflock'. Nöldeke (mündliche Mitteilung) will np.
m^X direkt an ai. sumeka- anschliessen, dann müssten
die Worte der anderen iranischen Sprachen sämmt-
lich Lehnworte sein.
1006. tneyiten (diese Infinitivforni ist nicht belegt) *harnen\
Praes. mez-etn, mezlden.
aw. l^maez-, maezenti *harnen' ; phlv. m^zltan, mezet,
m{i)stan, vd. 18 (98) Gl., niez{i)smk {KV ,); ai. [^weh-,
mehati; arm. mizem *harnen', mez *Urin* (H. No. 198).
kurd. mTztin, mistin *harnen', mizum; af/. mifal;
oss. d. m^zun^ t. mizju (184); bei. mizay, mBzay(2'i%).
Np. giimz (d. i. *gumcz) der Wörterbücher, auch
kimtz, kumlz *Urin', ginnzlden harnen' (aw. gaomaeza-y
phlv. gcmez, arm. LW. gomez-)) sind sämmtlich
unbelegt.
1007. meyezd *Gelage\
aw. myazda- ^Opfermahl'; phlv. myazd, myäzil;
ai. miyidha-.
1008. meS 'Schaaf, Widder.
aw. maesct' *Schaaf, Schaafbock'; phlv. mes; ai.
mesd',
kurd. mt^ miya; af/. m^y 'Mutterschaaf, LW. mes
'Büffel'; bei. mes (240); wa;t'- w^*> sar. mdo^ mdul,
siyn. may, mdyij.
1009. mey *Wolke .
aw. maf.ya- *Wolke'; phlv. mey ^ vd. 15 (18); ai.
meghä-; arm. m^g 'Nebel* (H. No. 197).
oss. d. meyä, t. 7nty *Nebel, Wolke' (185).
Dass mey mit l^meig^h- 'harnen' (1006) zusammen
gehört, scheint sicher zu sein, vergl. zuletzt Bechtel,
Hauptprobleme S. 373.
') Das l Hesse sich allerdings als Ablaut erklären.
') Seifenkraut; Ochsenurin.
```


## [2026-09-07T16:09:34.173Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ===\"; grep -n \"gumextan\\|gumēxtan\\|āmēxtan\\|amextan\\|mēxtan\\|mēz\\|mēg \\|mēγ\\|mist\" PHD.txt | head -40; echo \"--- PHD_mackenzie ---\"; grep -n \"gum[eē]xtan\\|[aā]m[eē]xtan\\|m[eē]z-\\|m[eē]g \" PHD_mackenzie.txt | head -30"
}
```


### [2026-09-07T16:09:34.235Z] TOOL RESULT

```
=== PHD ===
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
127:mayānjīg ... add arbiter. for | !"?mez- read ! *mēz-, v. 'mēzišn, mistan.
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
476:méy [туу | Р myg, N ~] cloud, mist.
491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
767:all hamag, hāmist, hamoyén, har(w), harwin, harwisp, hambāstag.
921:banana mēz.
1021:blinking mēzišn.
1571:desire (v.) abāyistan, kāmistan, xwāstan,
1678:don paymēxtan, pēšīdan.
1695:dress paymēzan; v. garment.
1747:element āmēzišn, rastag, záhag.
2323:host mēzdbān.
2588:least kahist, kamist, nidom; at — pad kamistih.
2635:limbo hammistagàn.
2827:mist méy, mizné.
2828:mistress kadagbānūg.
2831:mixing, mixture āmēzišn, gumēzišn, gumēzag(īh), gumēg.
3064:peaceful isin, hammist, rāmišnīg.
3796:stagnant hammist.
3875:suck mēzīdan.
3941:teach čāštan, frahixtan, hammēxtan, wizistan.
3942:teacher  hammēzgār; (priest) hérbed.
3943:teaching āfrāh, čāšišn, hammēzišn.
4101:twinkling mēzišn.
4175:urinate góméz-, mistan.
4176:urination čamišn, mēzišn, pēšārwār.
4177:urine mēšag, pēšyār; bull's — gūmēz, dastšēy.
4260:want (v.) abáyistan, kāmistan, xwās- tan.
4842:Čē-ēwēnag! саһ -masāy mehtar mehtarih mehén- mehénidan mehēnišn mast mistan
4877:ménogwénih! mēnēgīh mēnēgīgīh mēnēgīg mēwag moymard mowbed menišnīg menišn mēzd, mizd mēzdbān miznē mēy mayg mērag namagt Jabar! sah-! sahistan! sahián! mij 13mēx- mēzīdan mijūg
--- PHD_mackenzie ---
575:for    mistan, 3 mez- read ... 2 mez- .. ,
922:               a-gumeg r>gwmyk I M )gwmyg] unmixed, pure.
1010:Amextan, amez- ['myhtn', )myc- I M )myxtn, )myz-, N ,..,] mix.
2543: g~mez- [gwmye- I N gimez-] urinate.
2612:gumeg [gwmyk' I M gwmyg] mixture.
2613:gumextan, gumez- [gwmyhtn', gwmyc- I M gwmyxtn, gwmyz-] mix.
3553:1-3mez-, v. mezidan, mezi~n, mistan.
3556:mezidan, Imez- [myc-ytn l ] suck.
3572:mistan, 'mez- [mstn l , myc- IN mezidan] urinate.
7110:mix abyoxtan, amextan, gumextan,               musk musk.
7865:undertaking pardazisn..                  urinate gomez-, mistan.
10682:guftan                       "~Vt'           gumeg                             \~,...
```


## [2026-09-07T16:09:44.387Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nfor f in ['PHD.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    leaf=0; res={}\n    for i,l in enumerate(lines,1):\n        res[i]=leaf; leaf+=l.count('\\f')\n    for ln in [476,491]:\n        print(f,ln,'leaf',res[ln],'printed',res[ln]-21)\nEOF\necho \"=== NYB ===\"; grep -n \"gumextan\\|gum[eē]z\\|m[eē]z\\|m[eē]y \\|m[eē]γ\\|mij\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T16:09:45.833Z] TOOL RESULT

```
PHD.txt 476 leaf 79 printed 58
PHD.txt 491 leaf 80 printed 59
=== NYB ===
526:apar-zén [’plzyn'] the King's headquar- ters in the field 221. — < ?apar + zen (g. v.) ‘that which (is over =) superin- tends the arms’ = ‘Supreme command’; cf mezak.
1738:apäk 971, andar 423, 6 42?5, andar 6 93"*. 10419-20, 116°; hakanén ~ to intermingle, to become blended 431; andar € giyäk gumēztēnd they will crowd together in one place 9615. 9812-13; apāc ~ with a pred. to mix so as to become again 10416-17, apāc 6 . apäc ~ id. 10417-18, — < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gumyxtn, pres. intrans. gwmyas-, v.n. gwmyzysn (S), gwmyg ‘mixture’ (A-H II) confirming -k as the final cons. of the root; Paz. gumertan gumēž/z/-, gumežjzjašn. — V. ämecisn, ümek. gund [gnd] troop 8-18, — MPrth gwnd, Arm. lw. gund, Arab. lw. jund; cf Bailey, TPhS 1955, 73 sq.
2802:dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hurmuzd, Ormuz(d).
6620:guméxtan, gumez/z- : gumextan
6641:Hörmezd: Ohurmazd
```


## [2026-09-07T16:09:52.236Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; res={}\nfor i,l in enumerate(lines,1):\n    res[i]=leaf; leaf+=l.count('\\f')\nfor ln in [1738]:\n    print(ln,'leaf',res[ln],'printed',res[ln]-8)\nEOF\ngrep -n \"āmēcišn\\|ämecisn\\|ämek\\|āmēk\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-07T16:09:53.544Z] TOOL RESULT

```
1738 leaf 98 printed 90
398:āmēcišn [’mycän'] mixture; the elements that constitute the human body (Arab. mizdj): 4 ~ 12019. — MPrs ’myzysn (A-H I, Sogd. 164°-17), from MPrthPrs 'myaln ?(?)myxs- ‘to mix’: Verbum 178, Ghilain 81. Cf guméxtan, gumécisn.
399:āmēk [myk] mixture; zük-— mixed with the dust, dusty 11213. — MPrth ’’myg, ct MPrs gwmyg (A-H. II, from gumevtan, q. v., which proves that the root was *maik- and not maig-, as Henning and Ghilain (v. above) have it: an original *āmēg would have resulted in *āmēļ(t), *āmēh in SW, ef s. v. teh.
400:āmēcišn ['mwešn'] teaching, instruction 804-17, 8823, — Paz. āmēžašni.
401:āmēk [’mwk'] teaching, doctrine 108". 1092, 11019, — MPrth ’mwg; MPrs hmwg (A-H II); from
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
1738:apäk 971, andar 423, 6 42?5, andar 6 93"*. 10419-20, 116°; hakanén ~ to intermingle, to become blended 431; andar € giyäk gumēztēnd they will crowd together in one place 9615. 9812-13; apāc ~ with a pred. to mix so as to become again 10416-17, apāc 6 . apäc ~ id. 10417-18, — < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gumyxtn, pres. intrans. gwmyas-, v.n. gwmyzysn (S), gwmyg ‘mixture’ (A-H II) confirming -k as the final cons. of the root; Paz. gumertan gumēž/z/-, gumežjzjašn. — V. ämecisn, ümek. gund [gnd] troop 8-18, — MPrth gwnd, Arm. lw. gund, Arab. lw. jund; cf Bailey, TPhS 1955, 73 sq.
5500:?myg: āmēk
5768:’myzysn: āmēcišn
6347:āmēžašni: āmēcišn
```


## [2026-09-07T16:09:57.849Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"myz\\|urine\" SOD_pages.txt | head -30"
}
```


### [2026-09-07T16:09:57.898Z] TOOL RESULT

```
9963:      axaz, anxaz ©impf. mxz           ^Yz-, myz-, >xst-                 STSCiii; BSTii 905.9; C2, 57V9
10880:     Pam-Pay- ©Parth. Wmyzd                                      load
18867:                                                                 5318 myz B                                     jl^^J^*
19967: 5673 *myz- B
19973: 5674 myz>y S, B                                      V
19975:      urine                                                5685 mz'yxch S                              ^cJ'jj
19979: 5675 myzd S                       *                             big,
20955:     nmyzysn ©<Parth.
31490:     dandarak                                                          tambourine ?
31495:9617 tny- C                                o*J'ij>}**~ ^j <o>j.         tambourine
39594:   10718                                       tambourine 9628, 9629                  ten thousand       2811, 8652
39779:                                                                                  urine    56741461
```


## [2026-09-07T16:10:01.440Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19955,19995p' SOD_pages.txt; echo \"---- page tag ----\"; awk 'NR>=18800 && NR<=20000 && /pdf page/' SOD_pages.txt | tail -5; echo \"--- around 5318 ---\"; sed -n '18855,18875p' SOD_pages.txt"
}
```


### [2026-09-07T16:10:02.723Z] TOOL RESULT

```
     5656 mysy =» mys-, myr
                                                                5669 myw B, M
     5657 mysy Pyyy =* mysyy Pyyyh
                                                                     myu   ©Khot. muyU Chin, miau
     5658 mysyy =» 'mySr-y                                           tiger                                            *rt
     5659 mysyy Pyyyh M                   >jur^lj~+                  SCE 301, 358; TSP 2.635, 681, 713, 811, 3.137, 6.8,
          misi-Payi (mysy pyyy) -»mys-, mySr*                          8.166; BBB
 5670 myy M =» my1                                          5682 mzVrk' B                                       J,y
                                                                 mazezk ? (mz^xk)
 5671 myy6cyq M =» my8cyq
 5672 myyS8 M =» myS1                               >J^J         big, great
                                                                 SCE  62, 257; GMS 396
 5673 *myz- B
      me/iz ?                                               5683 mz'yn B                          ^iL^^U
      (/<?)let go                                                mazen ©Av. *hama-zaena-; MP zen =*mzyyn
                                                             >y armour, armoured
      TSP 2.299; Hen. Texts. 718
                                                                 VJ 921; GMS 397
 5674 myz>y S, B                                      V
      meze ©Av. maez\ MP /mz                                5684 mz'yx   B =* mz'yYOO
      urine                                                5685 mz'yxch S                              ^cJ'jj
                                                                mazexc/k (mz'yxk) ©f. -ch\ m. -k; adj.
      Hen. BSOAS 1946, 718, TSP 2.299, myn>y ; S W,               ^mz^YCh)
        BSOAS 1991, 490
 5675 myzd S                       *                             big,
                                                                 Anc. old
                                                                       Lett. 2.40, 2.53; GMS 396, 976
      mizd ? ©Av. mizda
      salary, reward                                       5686 mz'yxk =** mz'yxch
                                                           5687 mz'yxy'k S                                      J ,y
      Anc. Lett. 248, 49; Bailey. Prolexis. 280
                                                                 mazexyak ^mzyxy*
5676 mz» M, S                                       ♦>
     miza ?, muza ©f. nom. sg. mi/uz-i ob. ~y                    greatness
                                                                 KG 328
       *=*nymz-, nmzy*
                                                           5688 mzdw^q C                  *>y t J~*jI <OjULj
     eyelash
     Hen. Sogdica. 4, 1 f. n 1; S W, BSOAS 1991, 492,           muzducak ©^mwzd'cq ^mwzd-fcq
       muzayi                                                   Gospel
                                                                STii 1.96; GMS 1019
---- page tag ----
--- around 5318 ---
       Buddha's title                                                 whole, all
       TSP 2.45, 366, Hen. Texts. 715                                 TSP; BBB; Hen. Cosm. 312, 81; MD; STi 32, 22;
5307 myY'c B                                                            Sund. AoFi 1971, 241.3; C2; KG; mYwnt(h),
                                                     ^\j^
     maharaj ©Skt. maharajan ©pi. -/                                    MDii B-19, 7; B-5, 10, 11; mYwnw, MSP b 107,
     Maharajah                                                          117
       TSP 5.100, 8.50, 51, 49; BSTBL, Padm. 50                  5317 mywpt S                                           ju^*
5308 myNvn B, S                 jjjLa<^«ua                            mayu-pat =*mwypt(w), my8P-
     mayon ©*hama-gaona ©ace. -w =*mywn,                              Zoroastrian priest
       nVywny
                                                                      MDii pi 84, 18; MDiii p96
       all, complete, like
                                                                 5318 myz B                                     jl^^J^*
       GMS 379; VJ; TSP; BSTBL; STii 8.11, mx>wn
                                                                      mayz ©ace. -w, -y; ob. -y
        mY'wnw, TSP 2, 876, 9.142
                                                                      marrow
5309 mY5>k B, S
                                              ^                       VJ 987, 1180, I486; TSP 2.115, 118, 476, 3.274,
     ma/iy8e, msy5e (mySy) ©<*migda-ka-, Parth.
                                                                        276, 289; SCE 271
```


## [2026-09-07T16:10:10.568Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.search(r'pdf page (\\d+)',l)\n    if m: cur=int(m.group(1))\n    if i in (19967,19975,19990,18867):\n        print(i,'pdf page tag',cur,'printed~',cur-66 if cur else None)\nEOF"
}
```


### [2026-09-07T16:10:11.992Z] TOOL RESULT

```
18867 pdf page tag None printed~ None
19967 pdf page tag None printed~ None
19975 pdf page tag None printed~ None
19990 pdf page tag None printed~ None
```


## [2026-09-07T16:10:16.402Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" SOD_pages.txt | head -3; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; res={}\nfor i,l in enumerate(lines,1):\n    res[i]=leaf; leaf+=l.count('\\f')\nfor ln in [19967,19975,18867]:\n    print(ln,'leaf',res[ln],'printed~',res[ln]-66)\nEOF"
}
```


### [2026-09-07T16:10:17.758Z] TOOL RESULT

```
19967 leaf 293 printed~ 227
19975 leaf 293 printed~ 227
18867 leaf 277 printed~ 211
```


## [2026-09-07T16:10:27.183Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; for f in BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"== $f ==\"; wc -l $f; grep -o \"pdf page [0-9]*\" $f | head -2; grep -o \"pdf page [0-9]*\" $f | tail -2; done"
}
```


### [2026-09-07T16:10:28.491Z] TOOL RESULT

```
== BQT_v3_pages.txt ==
51425 BQT_v3_pages.txt
pdf page 1
pdf page 2
pdf page 720
pdf page 721
== BQT_v4_pages.txt ==
22553 BQT_v4_pages.txt
pdf page 1
pdf page 2
pdf page 552
pdf page 553
== BQT_v5_pages.txt ==
10090 BQT_v5_pages.txt
pdf page 1
pdf page 2
pdf page 292
pdf page 293
```


## [2026-09-07T16:10:30.949Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py BQT:1835 2>&1 | head -60"
}
```


### [2026-09-07T16:10:37.294Z] TOOL RESULT

```
REF: BQT:1835  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 632  OCR-lang: fas

-۱۸۳۵- کن ابلیس
سین بی نقطه و فوقانی » جوهریت فرومایه | است که‌کنایه لزیی‌شان باشد - وکنایه ا ز کی
و ارزان و رنگه آن کبود بسرخی مابل میباشد | است که‌کاری را چنان کند که دبگری پی‌بمطلب .
و معدن آن بمدینه طیبه ازديك است . کوبند | ومقصد آنکی نبرد .
درپیاله وظروف کست‌هرچند شراب خورندمتی مه « بکر اول وفتح ثالی» نام‌رستنیی
نیاورد و | گرقدری ازآن در قدح شراب اندازند | باشد مانشد رازبانه و آن راکوسفند وشترودواب
همین خاصیت دهد و اکر در زیر بالین گذارند خورند و بمربی فزاخ ۴ کوبند - ویضم اول.
وبخوابند خوابهای خوش بینند . نوعی از ماهی باشد و معرب آن جمه است بم
گم شددلب‌در یا -کنایه ازعخصی | جیم ۴ و عربان بهمین لفظ میخوانند #۰
ات که شتاوری و آب ورزی نداند و در آب گمیز ۴ - بکر اول واانی بتختانی
غرق شود ۱ . کشیده و بزای نقطه‌دار زده » پیغاب را کوبند
گم کردهپی - بسمنی پی کم کرده | که شا باشد و بعربی بول خوانند 8 .
بیان شانز دهم
درکاف فارسی با نون مشتمل بر نود لغت و کنات
گن < بکسر اول و سکون ثانی» بمعنی که ضیه است ۷ .
صفت باشد هرگاه آنر| با کلمه‌ای تر کیب‌سازند گن‌ابلیس - بنم اول . بستی خايةٌ
همچو شرمگن وگرکن وامثال آن ‎٩‏ » وافاده | شیطان چه کن بمعنی خسیه باشد ۸ - و دانه‌ای
معنی‌ساحب هم میکندیمنی‌صاحب‌شرموصاح ب گر هم هست بیار سخت و اسیاه رنگه به بزرکی
که جرب‌دار باشد - و بضم اول مخفف‌کند بود ‏ جوزبواء چونآنرا حرکت دهند وبجنبانند مغز
۱- کوهری کزصدف کون ومکان بیرون‌بود طلب از کم‌شد کان لب دربامیکرد.
« حافظط شیرازی ص ۹۹ .
۴ - صاحب تحفقةالمژمنین میگوید که لفظ قزاح بقاف و زای معجمه اسم مغربی لباتی
است خوشبو و شبیه برازیانه ‏ و از آن کوچکتر . شعبةٌ او بیشتر و مشتبك » و تخمش مانند
ایون « چك ص ۹۵۰ ح ؟ . ۴ - (عر) « جم بالضم » نوعی ازصدفی > « منتهی‌الارب».
۴ - بهلوی 81012860. رل : کمیختن . درفارسی «کمیز > با کاف ضبط کرده‌اند و اصح
با گاف است .
8 - با چنین دل چه جای باراست کابر بر توکمیز هم نکند .
سنائی غزنوی ص ۷۸۶ ۰
‎٩‏ - مغفف «کن > . ۷ - رك : کند . در اراك ( سلطان آباد ) 801 (خصیه)
مثلا «کن کوسفند » یعنی دنبلان کوسفند هکی نژاد» - ۸ -رك :کن .
گمیختن - بنم اولوفتح پنجم » ا زکمیخ (* کمیز [هم.] تن(پسوندمصدری):
پپلوی 81718673120 ( مخلوط کردن ) ۰ ابرانی باستان - 3۷1-13811 » سانمکربت- 7011690
* نیب رکه ص ‎۸٩‏ ؛ جزء اول پیشوند است بمعنی‌بد » ضد؛ وجزء دوم بمعتی آمبختن » لغةیعنی
بدآمیشتن ؛ مخلوط کردن » قاتی کردن - پیشام ربختن .
```


## [2026-09-07T16:10:55.300Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for p in 62 2006 2073 2079; do echo \"###### BQT:$p\"; python3 tools/ref_page.py BQT:$p 2>&1 | head -45; done"
}
```


### [2026-09-07T16:11:06.634Z] TOOL RESULT

```
###### BQT:62
no scan of BQT covers printed page 62 (see 'scans' in refs_online.json)
###### BQT:2006
(no exact page map; using offset -1917 -> pdf page 89; check the printed number and re-run with --pdf-page if off)
REF: BQT:2006  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 89  OCR-lang: fas

وه ۱ سوه
هژه ۱ - بکس اول و فتح ثانی,ممروف | بازی است که آلرا خیزبگیر: خوانند . و بسنی
است که موی پلك چشم باشد وآنرا مژگان هم | کوبند بازی مزاد است که در بیان میم با زای
میگویند جْ اول . قطه‌دار مذ کور شد .
مژیده ؟ » بر وزن ندیده . نوفی از
بیان چهار دهم
در میم با سین بی نقطه مشتمل بر بیست و شش لغت و کنایت
مس - بفتح اولوسکون نانی؛ پای‌بندی | ودست سودن باشد برچیزی9 - وبمعنی‌دیوانگی
را گویند که کسی را ازآن خلاس ونجات مشکل | هم بنظرآمده است 8 - ویضم اول . مانمی باشد
ودشوار باشد » و بسنی کوبند بندی باشد که بر | که کسی بابب آن مانع بجایی نتواند رفتن »
پای مجرمان و گناهکاران نهند؟ - و بممنی‌مهتر | و این بمعنی اول نزديك است ‎٩‏ - و بکسراول,
و بز رکه هم هت ۴ .- و درعریی دست مالیدن ‏ م«مروف است و آن جوهری باشد از فلزاتٌ که
۱ عطعام. 20286 کردی 22128020 , اطعنه . آهتازام ( مژکان )۰
بلوچی 8210260 , 17189128810 ( مزکان ) ۰ بلوچی ع 1120281288 . قس : هندی باستان
]11 (چشمك چعم ) . ساندکریت - 811319122 ر4: اسشق- هوبشمان ۹۸۰؛ بروجردی
58 شهیدی » . بعش مماسران آنرا از : م [ مضموم ] ( مغفف «مو») لژ(
یژه ‏ چه <یچه ) [ پولدصفیر 1 داسته‌اند ولی بر اساسی نیت . ورك:مر کان. در فارسی
هژه بغفیف و تشدید ۶ ژ * هر دو آمد. . فرخی در دوبیت متوالی گوید :
بوقت صلح دل من خلد بتیر مژه بوقت جنگه دل دشمنان بتیر خدلگه
بتیر مژه از آهن فروچکاند خون چنانکه میر بپولاد سنگه ازدل سنگه
* فرخی سیستانی ص ۲۱۸ ۰
۴ - ر4: مزاد , مزبده. ۴ - جهانگیری ورشیدی وسروری وفرهنگه ابراهیمی
این ببت فردوسی طوسی را شاهد آورده‌اند :
هنر نزد ایرالیاست و بی بدارند ( درآرند ) شین ژبان را بمس .
موْلف فرهنگه نظام گوید : «کوبا مأٌخن تمام همان شمر فردوسی است که بر فرض‌آنکه لفظمی
درآن آمده باغدبمعمنی دست مالیدن هم درمت‌امست » ولی مصراع دوم درلسخ بدو سورت ذبل‌لیز
آمده : ندارند شیرژبان را بکی ( بسنی اهمیت نمیدهند ) - ندارند شیر ژبان را به مس ( ومی
بممنی بزرگه است . رك : ح 4 ) . رشیدی « بامی > را ازین کلمه مر کب داند , وصحیح آن
* پامی > (۸.م.) امت. ‏ ۴ - پهلوی 133889 (بز رکه , مه) * مه(ه.م.). خوانساری 130558۳
( مپتر ) . رك دح ۰۳ 8 - رك : منتهی‌الارب » اقرب‌الموارد ... .
۹ - در موبدالفضلاء آمده : « مس بالشم پای‌بند بعنی رنجی (ظ . زنجیری )که کی
از آن تواند رفت وقیل بالفتح . * رك : ح۳ ورك : مس‌بند .

###### BQT:2073
(no exact page map; using offset -1917 -> pdf page 156; check the printed number and re-run with --pdf-page if off)
REF: BQT:2073  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 156  OCR-lang: fas

۰۳ میخ قدم
و نام شهری است مابین عراق وآذربایجان. وبمعنی سکهٌ زرهم آمده‌است یعثی آهن ی که در
ی پسه ۱ ۹ بشما بسنی دواب ی ۳۳

است -ودوغایین! ای زگویند که چندان | وبدان سکه برژر زشد -
که بقوامآید؛ وبعنی گوبند شرابی است که‌آنرا 5 فا ی +
با داروی چند بجوشانند و صاف کنند و معرب ک ی ۰ است 1
آن می بختج (۱) باشد و بعربی عقید الب | ۶ ۶ یا ۱
خوانند . ۱ میحشن " < با
انی مجپول بروزن ر,ختن سک
هی هرست ؟ - کناب از دایم الغمی پسی شافیدن و بول کردن باشد . ۳
بعنی شخ ی که پیوسته شراب خورد . میخ در 2 < بکسرئالك ودال بی‌نقطه»
همین ۴ < با نانی مجهول وتای قرشت | سکه راکوبند وآن‌آهنی باشد که نقش زر وپول
بر وزن پیشین » کلنگه ومیل آهنی باشد که | برآن‌کنده باشند .
سنگه ترادان بدان سنگه تراشند و بشکافند میخح دبنادی < بسسنی میخ درم است
و بکنند . که سکه باشد .
ی « بروزن سیخ » معروف است ۴ - میخ ققد۴ - بسکون نالك و فتح قاق

(۱) خم ۱ : می پختج .

۱- از : می (عراب) ۳ پخته ( اسم مفمول از پختن ) معرب‌آن میبختج ( بفتح اول و
سوم وپنجم ( با میبختج ) بفتح اول وضم سوم وفتح پنجم) « جمهوری هوماء‌العنب الذی طبخ حتی
ذهب صفه فی‌الطبخ ... وان طبخ حتی ببقی ربمه سمی میبختج .» « مقار ۸۶ 21011۳ 73001
«عقارع ۸«ف» . ورك : دزی‌ج؟ص ۰۳:۹۹ ولیزمعرب‌آن میفختج. ۴ - از: می (شراب) +
پرمت(پرستنده). ۴ - ۶ هیتن,» تبری با کلنگی بو د که بدان کوه وزمین کنند .آغاجی کوید :

بشندی چنان اوفند بر برم که میتین فرهاد بر بیستون .>
« لغت فری ص ۰.۳۸۲

۴ -فی: پارسی‌باستان -0892178 ۳۳ آریابی- ۰878216108 ساسکریت 12206102
( میخ چوبی ) * هویشمان ۵ لفات متعار در لهجه‌ها : کردی 112 » افغانی ۹
080 ( میخ » میخ چوبی ) » استی 17367 ۰ 13211 ( لیر ) » بلوچی 1310 . وشی ۰12670
سربکلی 7132 . رك : اسشق ۰۱۰۶۵ گیلکی 13626 ؛ رك : تتبعات شرقی بافتخار پاوری » ض
4 : میخ بقلم ۳6۳۲۵۴۵ 0320761 ؛ میلةٌ فلزی با چوبی که يك سرآن باريك و تیز وسر
دیگر آن یپن است و با کلاهکی دارده وآنرا برای اتصال قطاءات فلزی وچوبی با آوبختن قابها
بدیوار بکار برند .

8 - رك : میختن . ‎٩‏ - از : میخ (* میز) + تن ( پسوند مصدری ) . تلفظ
قدیم 1388128 ۰ اوستا -131267 ۰ ۳8626811 ( شاشیدن ) ۰ پهلوی ۵۸62112 ۰ ۳8281
0( » هندی باستان - ([گ۳۳. 76۳0811 » ارمنی 1117677 (شاشیدن) » 12862 (عاش):
کردی 7017118 ۰ 1715110 ( شاشیدن ) » 7012030 , اففانی [018 ۰ استی 3262070 ۰
هل . بلرجی و1252 . و362۵ 3 استق ۲۱۶۶۹ ر4 : میم .
###### BQT:2079
(no exact page map; using offset -1917 -> pdf page 162; check the printed number and re-run with --pdf-page if off)
REF: BQT:2079  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 162  OCR-lang: fas

سطً ج خه ما بکد
آنگوری لملی باشد . میگزد * - با اول بتحتانی رسیده
میش مرغ - بکسراول وسکون با | وکاف فارسی مفتوح بزای نقطه‌دار و دال باق
ثالك , پرسماست آبی و کبود رنکه که آنرا زده» بمعنی‌ميزد باشد(۱) که مجلس وبزم شراب
2 ایو وی بود ر ار و میت و عشرتگاه ومهمانی باشد - و مهمانغانهٌ
خرچال کوبند ۱ آکایر وسلاطین را نیز کوبند ؛ و بفتح اول وکات
میغ ؟ - با نانی مجهول پروزن تیخ ۰ | فارسی هم کفته‌اند -
بشاربرا کوبند تیره و ملاصق زمین - و بمعنی | هیگسار ۲ «ایمنی شراب خوار ۷ چه
ایر.هم آمده است که عربان سحاب خوانند ۴ . کاردن بمعنی خوردن شراب باشد لاغیر .
میگ ؟ - بغتم اول و اسکون: ثانی میک ۸ - بنتح اول و کاف فارسی
و کاف فارسی » ملخ را کوبند که بعربی جراد | وسکون انی وکاف تازی » بمعتی‌میگه باشد که
خوانند . ملخ است - وتصغیر میگه‌هم هت یمنی ملخك.
() چش : است .
۱ - ر4 : خرچال . ۴ - اوستا ۳3868۳2 (ابر) » یپلوی 13680 » هندی
باستان - 7۳1868364 » آرمنی 3268 (مه) ۰ استی 1338812 , 72181 (مه . ابر). اینکه «میم»
با ربشهٌ 128188 ( ادرار کردن ) همربشه باشد , قطمی پنظن میرسد « اسشق ۰۱*۹
۴ - « میغ » ابربود » فردوسی ( طوسی ) کفت :
همانا که باران نبارد ز میخ فزون زانکه بارید پرسرش تیخ.»
« لغت فری *۲۶ ۰
۴ - 38[8< ميگك («.م.) . اکنون در سواحل خلیج فاری نوعی از ملخ را «میگو»
کوبند . وآن متعلق بزبان پارسی‌اخص - یعمنی‌لهجهٌ جنوب غربی- است ودراصل ۰07722402۳2
08 بوده است . رك : ص هیجده ازمقدمةٌ کتاب حاض . هوبشمان کوید : میگه فارضی
پارسی باستان -07۳202 ( ۰ اوستا 33۵412 ) قی: 0218 کلم ارمنی 77227226
مستماراست, ولغت اشکانی- پارسی»13261287 متعلق است متقیماً یكلمهٌ اوستایی 224122752
«هوبشمان ۶۱۶۱۰ ۰ پپلوی 32218 ؛ بلوچی 328428 ۰ 1320802810 . رك : اسشق ۰۱۰۲۶
8 - مصحف « میزد » (ه.م.) رك : سراج اللغات بنقل « فرهنگه نظام ج ۵ ص ها ۰
‎٩‏ - از : می + کار (کارنده ) . ۷ - ونیز دهنده شراب » ساقی .
۸ «<میگه (ه.م.) * میگو :
احمد! پیش سلیمان می برد پای ملخ رکه پیش امه تین میگك میکند.
: احید اطمیه ۶ رشیدی » .
7 میشیه - ر4 : مشته (۱)
بقیه از حاشیهٌ صفحهٌ ۲۰۷۸
ودرلغت فری چاپ‌هرن « میشته» آمده » وبیت مزبور دررشیدی بدون ذ کر نام شاعرچنین آهده :
دیدم بت ماه روی رعنايك را سرمت به پیش میشته بنشته.
ظ . این نام مصحف « مشنا > ( بکس اول ) است که کنابی است بهودان را» وآن در عربی‌دخیل
است « اقرب الموارد » * 31902 ۰ رك : 7655 0۶ 17910۲ , 8.3۸16۲
۰ 2016 ,57 . 2 رطتقذه‌نای 112 ورك : دائرةالممارف مذاهب باهتمام همتینکه: 2هطفن۸4.
```


## [2026-09-07T16:11:32.409Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | grep -i bqt; python3 - <<'EOF'\nimport re\nf='BQT_v1_pages.txt'\nt=open(f,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find page containing printed marker for 62\nfor i,p in enumerate(pages):\n    if re.search(r'-\\s*۶۲\\s*-|۶۲',p[:300]):\n        print('cand leaf',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T16:11:34.144Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
777
cand leaf 1 ۱ ۵ ۱! ۱ | 7 موم ۳ لام | م ۱ 0 و طق صفرررنیاعدریرماروی | ۰ ۱ "۳ | ۳ | م و اس مر هر وه او | 7 رین خلت ریز یتایب بره ات | لف‌بال ۶۲ .یرک | ا اند کل داي رشب , رمع | فان تا تا | رن 9 3 | کرحم تن | اد شش مرا | مو رم | مر | وک رهب اه 
cand leaf 3 شیر زوا عرسا رده ارسال ۱۳۱۷ ۰۳۳1« 9 لو امد ۰ | / ی و ۷ مر | دسج ناویح ( منیا مینست | با ل ۰۰۱۰۶۲ . تسا یرتکاب رش و طابر | نواعت داست )ای ما لاسال ۹ ۱۳۳۸« ش ,مج مامت | وورو ر] نذا ۱۳۳۰ ۵۷ ماب سرد . | و۸ و ۰ ۰ ت‌ ف
cand leaf 158 عقدمه ۰ ۱ صد و نساه | 219- ۸ ۳۸66۵ 0۲۰ ۳۵6۵0۲ 1 0۸01 ۳6۶5/2۵ . 2۵ | 129۹44۰ | 2۸ ۰ ۱2:20 مقطاع۳۸ ۵هه ۳:2۵ 1 ۷۵5۶ -220 | ۰ 19۹44 | 2۵ ۲۲۲۱۱۵۱۵۵۱62۱ ۸۵ ,(ودممه) مدممنامهه‌یبه6 -221 | ۱ ۰ . .۳۵۸5080 0۲ | -صدطاعع۸ ۲۵ ص
cand leaf 159 صد وپنجاه و يك ما غذ | (اشتینگاس - ) .1930 عموما ومنووهءمه۱ ۵صمنعی «زتهوون)»ز۳] | 0 ۹ ...۵۳ (.5 .[ .1) هلوموم:1 -232 | 6۰ ۱۷20۶245 05۳6۶۲2۰ 7.2120 | ٩2256 06 5۳۵2۷256 ۰. ۰‏ ,2.۷ تتوممطه() عنله۲۵۳ -233 | ۰ 930 ۲
cand leaf 700 تخت فیروزه . ۷4 سس | تحت فیروده کنابه از آسمان | است- ونخت کیخسرو را نیز گوبند . | تخت نشنان خالك ۰ کنابه از | بادشاهان است - و ارواح را هم گفته اند س | واهل سلوك - وساکنان زمین را یز کومد . | لحنه . بم اول وفتح
```


## [2026-09-07T16:11:40.290Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T16:11:41.655Z] TOOL RESULT

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
```


## [2026-09-07T16:11:48.954Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(268,278):\n    print('==== leaf',i,'====')\n    print(pages[i][:1200])\nEOF"
}
```


### [2026-09-07T16:11:50.288Z] TOOL RESULT

```
==== leaf 268 ====
آ و فك س بروزن باربند » تلم کوهیست
درهمدان که بالوند شپرت دارد ؟ . «
له » بنتح ثالث‌بروزن لاله ؛ سنبل -
الطیب را کویند و آن داروبی‌است که در دواها
بعربی «عقاب» میگوشد ٩‏ -
آ یز - بروزن‌فالیز» جفته ولگدانداختن
- وخیز کردن و برجستن ستور باشد ۷ .
روم درون‌قلمه بجهت محافت قلمه نعیین(۱)
کننهه .
]لو ۷ سبروزن‌خالو موماست ممروف؟ -
ومخفف آلود نیزباشدکه از آلودکي حست ۴
و داش و کور؛ خشت پزی را نز کویند . *
[ لوده داهی ه مرمدامقید - وفاسق
و فلجر و کتاهکار و عاصی را کویند .
۲ لوس « بروزن ناموی ؛ ناه کردن
بگوشةٌ چشم باشد از روی خشم و نز .
را وقتح دال بی‌نقطه . میومایست زرد رلک شببه نون و فتح دال بی نقطه . اسب و استر جهنده
پزرد لو ودخوی لکد انداز راگویند . ۶
۱ - پهلوی 8100 « بونکر ۵۱ » ۰ شهمیرزادی ألقثا , کیلکی 5218 ( کوجه)
ر0( , طبری لاه (آلوچه) « واژه تایه ۳۱۰ > . ۴ یکی از انواع دسته بادامی ها
که تم علمی آن 1000650162 کناتلنا۳ است «گل کلاب وا ۳
؟ - درکلیات مر کب مانند : کل‌آلو , خواب آلو » یشمالو :
جبله اعل بیت خشم آلو شدند که همه درشیر بز طامم بدند. مثئوی «لفت نامه».
۴ - ر4 : الوند . ۵ رد : آفك .
1 - حمزه اصفهانی در کتاپ الئنببه علی حدوث التصحیف (نسخهٌ خطی ) ومیدانی در کتاب‌السامی
فی‌الاسامی عغابرا به « آله » ترجمه کرده اند وهمچنین ابورسان بیرونی در التفهیم. حکیم‌موژمن
در تحفه کوید : « عقاب بخ
==== leaf 269 ====
]هاچ » بای بروزن تاراج , خاکی
باش د که تشانتیررا برآن صبکنند چه آماجگاه
جاییرا کوبند که نثانه در آنجا بهند - وبسعنی
تشانةٌ یرهم هست ۱ - و آلتی را نیز گوبند از
آه نکه برزیگران زمین رابدان شیا رکنند ۴ -
و تخت یادشاحانرا کفته‌اند - و يك حسه ازیست
و چهار حصاٌ فرسنگه باشد چه هر فرسنگی سه
عیل است و هر میلی مسافت دو ندا و هر ندائی
بغدر چهار آماج » پس‌فرسنگی‌بیست وچهارآماج
باشد ۴ .
آمار
1هادن » بتح دال و سکون دون .
بمعلی ساختن - و ساخته شدن - و پر و مملو
کردانیدن - ومهیا کردن وستعد نمودن باشد .
] ماه ه پننی‌ساخته و پرداخته ومهبا
کرده باشد ۴ .
۲مار _ ه بروزنآزارهمرشی اس تکه‌آنرا
استقا گوبند - و بمعنی تهابت طلب و تفحص
ونجسی باشد - وبمعنی حساب هم‌هست چهآعاره
گیر محاسب وحساي کیزنده را کول ویدشی
استفصا و تبم‌هم بنظی آعده است٩‏ هه
۱ - باين معتی در دزفولی 6 کاشفری (1 : ۵۳) آماچ را درلغات نکی‌بمعنی
هدف وثشانه آورده وبدیهی‌است که دخیل است ر‌ در کتاب «اللیات‌النوائه والاستشهادات‌الستائه»
ننامده :
چونیر انداختی برروی دشمن
بر کند. نبرتو زآ نان خالد درآماچگاه
جنر رکن کاندر آ ماجش شتی. ممدیدلت‌نلمه».
بر ز کر ب رکنده‌پنداری باماج وکلند
سوزنی* لت نامد».
۴ آماج توازبلخ بود تابپنج آب پرتاب توازبلخ‌بود تابف‌طین. فرخی«لفت‌نامه».
۴ - «امیر (محمدین محمود غزنوی) . . .آواز داد . . . که او را تنپا برند؛ حلجب
کگفت 
==== leaf 270 ====
آماره مات
] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #
وییعنی آعار است کهمرض استقا - ونهایت تفحص
.و تس - و ساب - و تشبم باشد ,
]ماس ؟ ‏ بسکون مين ی قطه »
بمعنی ورم باشد که برآمدگی است در انا خواء
با درد باشد خواه بی‌درد .
]ماه ۴ ه پروزن تا گاه . بمعنی آحلي
است که ورم و برآمدگی اعضا باشد .
آهای - بسکون بای حطی . بمعنی‌یر
کته ره اراخته د ومافته و صحه زوسیا
کننده باشد ؟ - و اعر باین معنی هم‌هستیعنی
پرکن و بیارای و مهیا و مستمد نمای ۴ .
| محته. بضم نالت بروزن تايخته , مخفف | شهر مازندران ٩٩‏ است .
کویند ۷ . #
وغین نقطه دار » بممنی نفع و فایده است ۸
و زیده و خلاصهٌ هر چیز را نیز کفته اند ٩‏
و بفتح اك‌هم درست است .
۱ مرک از : آمار۳-ه (یسوند) . رك : آمار . ۴ - آهای و آهاه ومای ؛
طری ۵610189 » « واژه نامه ۱۲۹ », کلکی 2۳0۵6 . ؟ ‏ مخنف آمانده :
نوی کوه رآهای چارآخشیج مسلل کن گوهران درمزیج . نظامی «لفت‌نامه».
کر لزع مونح: ۵ - رگ: آموختن . ۱ - ره : آمدن .
۷ - بارها درشدی بجلس خاصس ‏ گه نوا زن بدی وه رقاس
کا هگنتی شوخی آهدمای که نمودی بعشوه شعده‌ای. امرخ رو*لفت‌نامه».
۵ - بیکی دلو سی رکردد هرغ صد درم مرمرا شود آمرغ. سنائی «لغت‌نامه».
٩‏ - این معانی ظاهراً ازحدسهای مختلفی است که در بیت سنائی زدماند. < لغت‌ناحه *.
۴ - آمل ‏ در پهلوی ۸۱0۵ کرسی طبرستان . این‌تام مأخون است ازنلم فبیلهٌ غیر
ابرانی 
==== leaf 271 ====
آمله ۲ - ینم ثاكك و قح رابغ » دوائی
است کثیرالتفع وممرب آن «آملج» باشد . گویند
دو درم را از آن کوفه تا دوساعت درآب شیرین
بجوشانند و بمد ازآن ساف کنند و سه‌چپارلویت
درچشم چکانند ۰ سفید یرآ که ۳ بود سود
دارد .
]هن - پنتح الك و نون ۰ نود خومن
هیزم شکافنه(۱) را گوبند سوپشته ویشتوار؛ هیزم
ببتهرا ن رگفته‌اند - و بکسرالث یام مادرحصرت
رمالت یناه علیه السلام است .
آمو . نم تالث و سکون واو , مضفف
آمون‌است وآن رودخانه‌ای باشدمشهور وممروف.
واقم در میان ابران وتوران- وبسنی گوبند دهی
است که این رود خانه موسوم بآن ده است ۳
(۱) چش: شکته . . (۲) چك: ژند ویلژند.
وژمینی خم‌هست میان جیحون وفرأت .
] موت - با فوفانی بروزن لاعوت .
آشیان جانوران شکاربرا کوبند حمیویاز وشاهین
]هو یا - بکر فوفانی و تضانی بالف
کشیده , بلفت زد و پازن() کنیزك و پرستا
وخدمتکار (۳) باشد ۴ .
۲ موختگان ادل » اب ر ارب
صلوات اف علیهم اجمعین (4) را کوبند . *#
| مود پروزن تابود » بعنی بر آحیخت
1 بر آراست - و ماخت کرد .
آمودن بروزن آسودن . بمعنی
ارات .- 1 "آراسته خدن و آم‌ختن -
(4)چك : - اجمعین .
منانات دراطامعلار۳ < تیتی دما ؟ ‏ آعو جحون ؛ در
. لهج پارتی وپپلوی (2722(]) ۲12100 وهمچنین درلهجةٌ یکی خلج‌ونیز فرکمنی. رله : مقاله
6 .۱ .3 در پاپ کتاب ,601870۳8۲ مهم‌مودتده ,۱۷۵۵866 . ۲٩‏ . 8۲۱
40 .و4 ۲۵.3 ۰ ۷۵۲۰۱۵ و عع‌نت:5 عتاهني۸ ۵۶ اعصیداه
==== leaf 272 ====
آموده ۰ 7۳۳
و آ یخته‌شدن - وساختن و ساخته گردانبدن٩‏ ۹
و پر کردن و مملو ساختن باشد .
آموده ۴ « پروزن آسوده » لمل و
مروارید و امثال آن را گوبند. که در رشته کشیده
شده باشد - ویمعنی‌پر کرده ومملوساخته‌هم‌هست-
و آراسته و بسراسته را یز کوبند. وترجمه‌لفظی
است که در عربی«مندرج خواند» .#
۱ ]موز گار ۴ ‌ باکاف فارسی. آموزنده
و آموزاننده را کویند که معلم و استاد باشد .
| هو سئی - بسکون‌ین بی‌نقطم و کس
نون و تحتانی ساکن » دو زن با بیشتر که يك
شوهر داشته باشند عربك مردیگررا «آموستی»
بائد ۴ ,
آمولن * - بنتح لام و سکون نون .
بونانی نگاسته را گونند که از آن بالوده و
آ هار پز ند .
آمون ‌ ب‌وذن حامون ؛ زودست که
ب رکنار خوارزم گنرد ؛ و میان تر کستان و
خراسان واقم است ۱ - و بمعنی پر و مملو و
لالب و لبریز هم هست .
موی ۰۲ بسکون بای حطی , دام
شهریست بر کذلر جیحون و جیحون منسوب‌باآن
شهراست - و بمعنی پر کردن و عملو ساختن -
و امر باین ععنی - و فاعل هم آعده است ۸ .
۲ مو یه - بنتح تحنانی ؛ بمعنی آمون
است و آن رووخانه ای باشد مشهور ۷ .
۱ هه .» بروزن نامه ۰ یمعی دوات
نوسندکی باشد ٩‏ - و توده و پشتٌ هیزمرا نیز
کنته اند ۷۰. «
آمیز ۷۱ بروزن کاریز» بمعنیآميزش
و مباشرت و جماع باشد - و امیختن دو چیز
با زباده بهم را نیز گوبند؟۹.
.* کرانمایه سیاهی داشت فرمود  باستقبال شهزاده بآمود. قضرالدین ابوالعملی < لفت‌نامه‎ - ٩
۳ 
==== leaf 273 ====
۰میژ ۲ « بازای‌فارسی» بروژن ومعنی
آمیزاست که آمیختن دوچیز بازیاده بهم‌باشد . *
آهیژه " « بروزن پاکیزه » بمعنی
آميخته است ‏ ومباشرت وجاع رایز گوبند -
ویمعنی مزاح وطسعت هيآ مده‌است ۴ - ویسنعنی
خردم پیر و کهل و رش دو موبه یز هت .
هردم زش دوموبه و پیر و کپل باشد - وبمعنی
آمیخته هم هست - و مردم شاعو وموزون را نیز
گونند .
| هیزه هو » بامیم بروزن پاکیزه روه
مردم رش جو کندم و دو موبه را گویندوسربی
«کهل» خوانند ۵ 1
] هی - بسکون غین نقطه دار » بمعنی
(۷) چب ۲ . چش : نوالعقول .
۱ - رکه : آمیز.
کر دکرده ببی سخن ریزه
۴ رکه : آمیژه .
۵ - اکرشاه حرهفت کشوربود
آن
حقیت‌بودکه درمقابل مجاز است ۷ - وآعیختن
و آمیزش در چیز باشد باهم ۷ - و مباشرت
و مجامعت را نیز گوبند ۸ .
] میقه ود بفتح غین نفطه دار .
بمعنی آهيخته و آميزش - و مجامعت ومباشرت
ماشد .
آ هیقی - بک غین نقطه دار وسکون
تحتالی » بمعنی حقیقی باشد که در مقابل
مجازست*۹ .39
آن بر وزن جان . بمعنی وفت و
حنگام ٩۱‏ واشاره بچیزی دور باشد ازغیرذوی-
المقول (۱) حمجو این که اشاره بچیزی ترديك
است -٩۴‏ ونمك وچاشنی وحالتی و کیفیتی رانیز
گوبن که در حسن میباشد و بتقربر درنمی آبد
اسدی «لفت‌نامه».
نوش آحیغ 4 کوهرآعیغ وغیره. «لفب نامه».
۸ - چوآعیغ برنا شدآراسته
دساتر ۲۳۱ .
#- درطمات مر کب : زهرامی: ۰
۶۰ رکه : آمیغ و فرهنگه
ر یگاهان». « السسجم ۱۷۵ ۰ .
1 < دانشنامه ٩۹٩‏
==== leaf 274 ====
ات ۱
وآنراجز بتوق وان بافت "٩‏ - وبمعنی عقل -
و پسمتی ثتراب هم.باظر آمده است ۴ ء
آ فت » بسکون نون وتای قرشت؛بسملی
آت بفتح نون باشد یمنی تزا آن ۰ هنچنانکه
کوبند «آت بی‌است» بعنی تراآن بس است -
گفته‌اند . 2
ا نج - عتح الث و سکون جیم , نم
دارویست که آتراعربر هزعرور» کویند؟ . #
آ فلون - بسنی آنجا - وآنچنان؟
و آنگاه و آترغان بائد همچو ابدون که‌ببمنی
اینجا - و اینچنین - و اين زمان است
۲ سب الث بروزن واسنه . بخ
1
۲ يك عه بفتح ثاك‌وسکون کاف‌صفیر,
(۱) چش . چب ۲ : آنکندن.
صورت مصحف دآلج» ناشد . «الفت‌نامه» .
+ تاریخ مستان بو, ۸۷ *.
تسس ( اش
آنس تکه آشاره به بمید وچیزی دود باشد همچو
ایك که اشاره قرب و چیزی. تزدحكث است -
۲ نگندن (۱)- سگان له بستی
آکندن (۲) است که پرساختن وانباشتن باشد .
آ فیسه - بکر اك و سکون نحتانی و
بد شواری واشود - و بنمنی خون بسته و مداد
بته وامثال آن هم آمده است وآنرا آنیسته‌نیز
کوند بازبادتی فوقانی ٩‏ .
] لین « بروزن پایین ؛ چويي باشد که
ماست را بدان برهم زنند تامکه از دوغ جدا
شود - و نیز بمعنی ظرفی باشد سفالین مانند
چمچه که مایت‌را درآن ریزند وجنبانند تاروغن
از وی جدا کردد .
< حافط ور »
۴ - کمان مبکنم این
خواهی ابدون گرای وخواحیآندون .
۱ ناصو خسر )۴ 2 لب نامه 5
: 2 نك‌نام اسرائیل بر بعقوب تهاد ند .»
از آنجا بنزديك مأدر دوان
آقره رکه : آ کارا .
فردوسی «لفت‌ناهه».
. این ن
==== leaf 275 ====
که هکلم سوراخ کردن نمل اسب و استر ومانند
آن از سل بیفند .
آواد - بسکون زای‌قطه دار.عمروف
است کد مدا و ندا و بانگه بلند باشد - وبمعنی
شهره شدن و سم کشتن عم آمده است .
آو اد گشتن بممنی شهره شدن
و مشهور کردیدن باشد .
]واه ۷ - بنتح زای هوز . بمعنی
شهرت باشد - و گفتار و حرف زدن بلند را نیز
گوشد - و چند نقمه‌هی‌هست ازموسیقی کهآ نرا
شش آوازه کویند و آن : سلمك و شهناز ومابه
و نوروز و کردانیا و کوشت باشد .
]و اذه گشتن - بسنیم آوازکفتن
است که بممنی شهرت گرفتن ر سمر گردیدن
ا وخ « بفتح ثاك و سکون خای قطه
دار. بمعنی آواخ است که آه واضوس - وفشمت
آو بروزن واو . آب را کوبند چه
در فارسی واو ببا و برعکس تبدیل می‌باید ۷ .
و « با تاك بالف کشیده . مخفف
آواز باشد لهذا هزار دستان را هزار آوا تسیز
گومشد .
] و اخه بسکون خای‌نقطه دار » بمعنی
آوخ قت که ماو بای نی فقوت نی مق اف
وضمت و اصیب را نیز گوبند .
آواد » بر وزن ناچار . مخذف آواره
است که از خان و مان دور افتاده باشد - وبمعنی
آزار و مشم هم آمده است - و حسب و حساب
را یز گوبند ۴ - وبمعنی خراب هم آمده است
که شض آباد باشد . ۶
[ و اده ‏ ختح رای فرشت. نابود شده
و کم کردیده و پراکنده و پریثان گشته و می‌نلم
و نشان و از وطن دور افتاده و سرکردان شده
را گوبند و ترجمة حساب نیز هست ۴ ؛ چه
حساپ کننده و محاسب را آواره گیر گوشد ‏
وبنمنی خراب هم هست که درمقابل آباد است -
==== leaf 276 ====
عمتی هم هست معنی بیاور - و بمنی صاحب و
خداوند نز گفته‌اند وقت ی که بالفظی م کب شود
همچو جنکه‌آور و دلاور و زورآور و مانند
آن - ویمشی کربه و زشت و بد قیافه هم بنظر
آمده است ۱ - و مخی‌ژشت و بدرا نیز گویند.
| ور چ4 - بنتح‌جیم» بمعنی‌آوارجه ۴
است که دفتر حسابهای پراگنده (۱) باشد .
آودذده بر وزن ناورد ۰ عمروف ات
که تقیض برد باشد ۴ - وبمعنی جنگ و یبکار
و کلوزار هم هت و بعربی«هیجا» خوانند .
ای بیع( ۹
آوردیلن ۴ - بننی حبله کردن
وجنگه اوری نمودن باشد .
]ود فك - ختح را رسکون نون ودال,
(6۷ ها :۷ج با که
کته
اند - و بیعنی مکی و فرب و حیله هم بنظر
آمده ات ۵
آوده- تح رایع و سکون ها ۰
اودی ح بر وزن باوری . صاحب
یقین و تحفق را" گونند . چه اور دمعتی تحقیق
و شین است ۹ ۰
| و شن س بکسر شین‌قطه داروسکون
نون » کاكوتي را کوبند ۷ و آن کیاهیست
که بعربی«سمتربری» خوانند ۵ .
آون *- بروزن اون ؛ مخخفآونگت
است که آویشنه و آویزان شده باشد .
او ند - بروزن ایند . رسمانی را
گوبند که خوشه های انگور از آن باویزند
کامروز همچوجهل هنرزشت و آوراست
عصری « لفت‌نامه »
الاوارحه ۰ من کب اصحاب الدواوین
۱
آوردن .
آروند و آورند .
۵ رکه :
ندارد بکسکینه وداوری . اپوشکور-
- رکه : آویشن .
سمتراست . «لغت نامه * .
آوشن
==== leaf 277 ====
9
و لنگی و جامه و غیره بر زبرآن اندازند - و
حجت و دلیل و برهاترا بیز کویند ۱ -و بمعنی
سابر ظروف و اوانی باشد همچو کاسه و کوزمو
امثال آن وبعربی «وعا» گوبند ۴ - و تخت‌وهسند
راهم گفته اند ۴ - و بمعنی شطرنج باشد و آن
بازیی است مشپور - و بمعنی اول و نضت هم
هست و باین معنی بکسر ثالث هم گفته اند .
و فدی ه بروزن رامندی , ظرف یکه
شواب درآن کنند .
و فگه ۴ - بسکون تون وکاف فارسی »
بمعتی رسمانی باشد که رخت بر آن انداژنه
و خوشه ای انگور نیز از آن آویزند- و حر
چیز آوشته را نیز گویتد.
آو نگان ۲ بروزن افرمان, آوشتن
و اوشته شده و آووان را گونتد..
٩‏ چنین کنت با پهلوان زال زر
رکه : آبه .
نامه» .
]وه - بنتح اك وطهور حا؛ بمعی ۰
ووای‌وافوس باشد ۵ وباخقای‌ها» نلم شهرست
ترديك بساوه ۱ - و کوره و داش خشت پزیرا
هم کفته اند - و بر آورتده صدا و ندا ماشك ب
و زنجیره را نیز گوبند که نقاشان و دوزندکان
ا وج 2۲ باجم. بروزن و معنی آویز
است که از آویختن‌باشد ۸ - چه در فارسی جیم
ابجد بزای هوز و برعکس تبدبل می‌بابد 4 .9
]ویر گان - با زاو کاف فارسی بر
وزن فالیز بان , خواص - و دلبران و مسشوقان
را گویند .
) و یز گن ‏ بسکون زای حوز و کس
کاف فارسی و نون ساکن . کدای مبرم وابرام
فتتنهترا گونتا .
۴۳ ک ۷ آوشتن واوئد ,
سود لاغر که ۳۹1 رزق رت
مثنوی «لفت نامه .
۸ چنانکه مردآویج «لفت
فردوسی.
نصب کردن « لت نامه » .
بفه از صفعةه ٩٩‏
```


## [2026-09-07T16:12:22.419Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor printed in (273,):\n    leaf=printed+24\n    print('printed',printed,'leaf',leaf)\n    print(pages[leaf][:3000])\nEOF"
}
```


### [2026-09-07T16:12:23.654Z] TOOL RESULT

```
printed 273 leaf 297
 MHG gemaht, NEG gemacht (: OHG maht ‘power,
‘and-H. 1.671). Sr aation, form.’ ON skgpin (pl.,
vith article, of skap ‘state, condition’), 1 (ge)sceap ‘private parts’ of either sex 3 dial. shape ‘female parts’, NED s.v.
16), Falk-Torp 976. ‘Organ for urinating’. Skt. medhra-
pants OF
Digitized by Arya Samaj Foundation Chennai and eGangotri
ILY FUNCTIONS AND CONDITIONS 259
(AV +), fr. mih- (4.65), Lith. mizius, Lett. mislis (Leskien, Ablaut 279).
Miscellaneous and doubtful. Lat. mato, Ir. moth (Walde-P. 2.312. Ernout-M. 649) ; Lat. mentula (> It. minchia), etym. dub. (Walde-H. 2.72. REW 5513) : It. cazzo (: cazza ‘crucible’?); Rum. puld (Tiktin 1277 f.); Ir. biach (Walde-P. 1.667) ; Ir. bot, NIr. bod : W. both ‘nave of a wheel, boss of a shield’, perh. ChSI. gvozdt ‘nail’ (Pokorny, Z. celt. Ph. 16.405. Walde-H. 1.574); OE teors, ME, NE terse, tarse (NED tarse sb.'), OHG, MHG zers (perh. : OE teran ‘tear,’ etc. Walde-P. 1.802); Lith. bybzs; Pol. kutas (‘tassle’, Berneker 653) : Skt. cigna- (Walde-P. 1.402); Skt. kaprt(h)- (Walde- P. 1.348, 2.49).
4.51 BREATHE; BREATH
Grk,  zvéw; aveDpa, rv07 Goth. anan Lith. kvépuoti; kvapas
NG  avarrviw; avacaivw ; ON anda; ond, andi Lett. dvaSuot, elpét; dvaSa, avon, évaca Dan. aande; ande elpe
Lat.  spirdre; anima, spiri- Sw. andas; ande ChSl. dychati; dychanije, lus OE orpian, cbian; orop, duchit
It. respirare, fiatare; Zbm SCr.  disati, dihati; dah fialo, respiro ME trethe; bre(e)th Boh.  dychati; dech
Fr. __respirer; haleine, NE breathe; breath Pol. dychaé; dech souffle Du. ademen; adem Russ. dySat’; dychante
Sp. _respirar, resolla-; OHG  datumén; dium Skt.  an-, quas-; ana-, aliento, huelgo MHG dtemen; diem cvasa-, Gtman-
Rum. rdsufla; rdsuflare NHG  atimen; atem, hauch Av. (dnti-, pardnti-)
Ir, doberim anal; anal andluighim; anal anadlu; anadl
Br. alanat; alan
A few of the words listed apply only | Ir. andluighim, W. anadlu, Br. alanat;
i" the exhalation of breath, as NHG ae in contrast to atem, or are mostly Cee This was originally true of - ae e Ely all, of the others, as ; € usual associati 1
tle ais ee Clations with
oun an but d verb
at, anima: az ne (vith mena anal, W. anadl, Br.
Goth. anan (only uz-anan éexvetyv Mk. 15.37, 39), ON anda, Dan. aande, Sw. andas (refl.), with nouns ON ond, andi, Dan. aande, Sw. ande; OE orpian (fr. orop ‘breath’, this fr. *uz-anp-); Skt. an- but mostly cpd. pra-an-, with nouns ana-, prana-, Av. Gnti, pardnti- ‘inhala- tion’, ‘exhalation’ (fr. *anti- ‘breath’ with @ and pard-) : Grk. évepos ‘wind’, ChSI. vonja ‘odor’, achat ‘odorari’, etc. Here also Fr. haleine, fr. late Lat. aléna; Sp. aliento fr. alentar ‘breathe, en-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
otis © igen
Digitized by Arya Samaj Foundation Chennai and eGangotri
260 SELECTED INDO-EUROPEAN SYNONYMS
courage’ (fr. *alénitare) derivs. (with metathesis) of Lat. anh
```


## [2026-09-07T16:12:30.293Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"4.65 URINE\\|4.65\" SYN.txt | head; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (309,310,311,312):\n    p=pages[leaf]\n    import re\n    print('=== leaf',leaf, [x for x in re.findall(r'\\b2\\d\\d\\b',p[:200])][:5])\n    if 'URINE' in p.upper():\n        i=p.upper().find('URINE')\n        print(p[max(0,i-200):i+2500])\nEOF"
}
```


### [2026-09-07T16:12:31.647Z] TOOL RESULT

```
5326:ee Ir. cennt ‘scales’) : opds.)> ce aaa and ON skinn, Walde-P. 2.563. seithe : Lat. secare Walde-P. 2.475. 3, OF hgd, OHG hit, etc., the general Gme. word for ‘skin’ ae hide DOW properly only os animals) : Grk. oxdros ide, leather’, Lie: cutis skin’, Lith. kiautas ‘hull, husk’, OPnuss. keuto ‘skin’, Ir. codal ‘hide’; Grk. xev@w, OE hgdan ‘cover, hide’, ete., fr. IE *(s)keu- with various extensions. Walde- Pp. 2,546ff. Ernout-M. 249. Falk- Torp 4265.
5663:e’ (as Mt. 6.16, Mk. 14.65,
6691:(AV +), fr. mih- (4.65), Lith. mizius, Lett. mislis (Leskien, Ablaut 279).
6906:2.384. Ernout-M. 519f. REW 4865,
7029:4.65 URINATE; URINE
7090:8. Goth. mathstus (korpia), OF meoz, ME mix, Du. mest, OS, OHG, MHG, NHG mist: ON miga, OE migan, ete. ‘mingere’ (4.65), hence orig. ‘liquid ex- crement’, Walde-P. 2.245f. Feist 340,
7131:Av. miléra- : Skt. mitra- ‘urine’, ete, (4.65).
7133:Av. hizra- (‘liquid excrement’) : haek-, Skt. sic- ‘pour’, Serb.—ChS]. Sicat; ‘mingere’, etc. (4.65). Barth. 1812.
24305:14.53 14.61 14.62 14.63 14.64 14.65 14.66 14.67 14.68 14.71 14.72 14.78 14.74 14.75 14.76 14.77 14.78
25630:14.65 WEDNESDAy
=== leaf 309 []
=== leaf 310 []
=== leaf 311 ['220']
. also Lat. spirare ‘breathe’, ChSIl. piskati ‘whistle’). Walde-P. 2.11. Falk-Torp 220 f.
4.65 URINATE; URINE
: qo ae Goth. Lith. my2i; myzalai (pl.), eee ON. mia ilapumas NG me vps} Kéroupo Dan. pisse; urin Lett.  mizt; mizalt (pl.) ringere, metere; Sw. pissa; urin ChSI. steati; stl Lat. 7 eee OE migan; migopa, SCr.  mokriti, pisati; i isciare; orina migpa mokraéa i Pee rsser: ager ME pisse; pisse, urine : Boh. — scdti, motiti; moé Sp. orinar, mear; orina NE urinate, piss; urine, Pol. —szezaé, moczyé; mocz, Rum, urina, pisa; urina PSII as Ce Ir. minaim; faal, min Du. pissen; urine Russ. scat’, motit'sja; mota Nir. miinaim; fual OHG - seichan; haran, seich Skt. mth-, miitraya-; W. piso, troetht; pis, MHG _ harmen, seichen; mira-, metra- troeth harn, seiche Av. miz-; maésma-, Br.  staota, troaza; staot, NHG _harnen, pissen; harn maesman- troaz
Several of the more respectable verbs, like NE urinate, etc., are derived from Lat. dina ‘urine’. Among the more euphemistic but still common terms, Many (though not entered in the list) are parallel to NE make water, as Fr. faire de Veau, Rum. ldsa udul, Dan. lade vandet, NG kav (dial, Xbvw) 7d vepd pov. ae ong those listed there is a widely
stributed inherited group reflecting an
TE root with thi j S meaning. A
sp ane g nother of imitative notions as ‘wet, In several cases : ae meaning ‘filth’, ‘lye’, of citer cting the common notions
me, acidity’
codd.; cf. Solmsen, IF 31.468), with duecxua ‘urine’; Lat. mingere, meiere, late meidre, midre (> Sp. mear); ON miga, OF migan; Lith. myzti (1 sg. mezu, OLith. minzu), Lett. mizt, with sbs. Lith. myzalat (pl.), Lett. mizali (pl.) ‘urine’; SCr. (obs.) mizatz; Skt. mth-, Av. miz- (with maésma- ‘urine’); Arm. mizem; Toch. B miso.
2. Grk. obpéw, NG (lit. obp&) xaroupa, with sbs. odpov, NG xaroupo ‘urine’; Lat. trina ‘urine’ (source of the most wide- spread Eur. words): Skt. varsa- ‘rain’, var-, vdri- ‘water’, etc. (1.31, 1.75). Walde-P. 1.268 f. Ernout-M. 1137.
3. It. pisciare, Fr. pisser (> ME pisse, NE piss, reg. biblical words, also as sbs.; Dan. pisse, Sw. pissa, Du., NHG pissen), Rum. pisa (SCr. pisati fr. Rum. or It.), all fr. a VLat. *pissiare (or the like), of imitative orig. REW 6544. Puscariu 1324. Falk-Torp 830.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
susasem
Digitized by Arya Samaj Foundation Chennai and eGangotri
274 SELECTED INDO-EUROPEAN SYNONYMS
4. Ir. miinaim, miunigim, NIr. mi- naim, with Ir. min ‘urine’ : Skt. mitra- id. (whence denom. miitraya-, but usual- ly mitram kr- lit. ‘make urine’), Av. miora- ‘filth, dung’, MLG modder, NE mud, etc.
=== leaf 312 []
hing) : MBr. gow- zroncquet ‘bathe’, Ir. fo-thrucud id., Lith. trinkti ‘wash’.
W. piso, with sb. pis, fr. ME pisse, NE piss. Parry-Williams 141.
Br. staota, deriv. of staot, MBr. staut ‘urine’ (esp. of animals, but also of men), loanword fr. Gmce., Dan. stalle, Sw. stalla, MLG, NHG stallen (OFr. estaler), NE stale, all ‘urinate’ (of horses, NHG stallen dial. also of men), these perh. (with special application to horses in-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
fluenced by the words for ‘stall, Stable’) . Grk. craddoow ‘drip’. Walde-P, 2.649 Henry 252. Loth, Rom. 19,593, 5. OHG seichan, MHG seichen (NHG dial. id.), LG séken (sbs. OHG seih MUHG seich), fr. IE *seig-, beside *sei. in ChSl. sicati, Boh. scdti, Pol. szcedg Russ. scat’ : OF séon, OHG sthan, NHG sethen ‘strain, filter’, Skt. sic- ‘pour out, shed’, Lat. stat: obpe? ert Bpédous (gl.). Walde-P. 2.466f. Weigand-H. 2.835, Briickner 545. MHG harmen, hermen, NHG harnen, fr. sbs. NHG harn, MHG harm, harn, OHG haran, ‘urine’ cf. MHG vb. hur- men ‘manure’, prob. : Lith. garmas ‘lye from ashes’, Lett. sarms, OPruss. sirmes ‘lye’. Walde-P. 1.463. 6. Lith. myZzlz etc., above, 1. Lith. Slapumas ‘wetness’ (: glapias ‘wet’, 15.83) and, esp. pl., slapwmai, ‘urine’. 7. ChSl. sicati, ete. : OHG seichan, etc. (above, 5). SCr. mokriti, Boh. moéiti, etc., with sbs. SCr. mokraéa, Boh. moé, etc. : ChSl. mokri ‘wet’ (15.83). 8. Skt. mth-, Av. miz-, etc., above, 1. Skt. miatraya-, mitra-: Ir. min, ‘urine’, etc., above, 4.
igitized by Arya Samaj Foundation Chennai and eGangotri
tai BODY; BODILY FUNCTIONS AND CONDITIONS 275
pARTS OF 4.66 VOID EXCREMENT; EXCREMENT, DUNG taae ee Goth. . ; maihstus, Lith.  Sikti; $udas, méSlas k KaKKaO, xe} Noe smarna Lett. dirst; stids, mésls
Grk. xbmP0S) ihe i z ON skita, drita; drit, skitr, ChSl. - 5 gnojt, govno,
NG xefo; apie Cie myki, skarn lajtno xompava Se merda, Dan. _ skide; skidt, mg SCr. _.srati; govno, gnoj, ba- ; Jat.  oa0dres Hg Zmentum Sw. skita; skit, dynga, lega : fimus, exer sae track Boh.  srdti; hovno, lejno, 1. oacare; eae es OE scitan; meox, cwead, hnij
Ir. chier; merae, scearn, dung, tord Pol. sraé; gowno, tajno, fiente - ME schite, drite; schit, gn6j
Sp. cagar; oe ; dung, mix, lord Russ.  srat’; govno, kal,
estiérco | NE shit; shit, dung, turd, pomet, etc.
Rum citea; edca he manure Skt. had-; cakrt-, purisa-,
Ir. case 2 Du. __ schijten, drijten; mest, visthd-, giitha- Nir.  cacaim; cac hoes drek, dreet Av. ri-; mi0ra-, giida-
W. _cachu, caca; cach, ican; mist, qual irya-, $a , ca, tom OHG Ariens mist, quat, sairya-, §2man- pony yep ES unga Br. kac’hout; kac’h, mon MHG > schizen; schize, mist, drec, quat, tunge NHG - scheissen; sc
```


## [2026-09-07T16:12:44.028Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN mist ===\"; grep -n \"^mist\\b\\|mist, n\\.\\|mist,\\s*n\" KLN_1966.txt | head -10; echo \"=== KLN mix ===\"; grep -n \"miscellaneous\\|misceo\\|miscere\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T16:12:44.131Z] TOOL RESULT

```
=== KLN mist ===
1470:acosmism,  n.,  the  denial  of  the  independent  real¬ ity  of  the  world  as  distinct  from  God.  —  Coined by  Fichte  and  Hegel  fr.  Gk.  priv.  pref.  a-, xoop.0?,  ‘the  world’  (see  cosmos),  and  suff.  -ism. acosmist,  n.,  one  who  believes  in  acosmism.
2091:Derivatives :  alarm ,  tr.  v.,  alarm-able,  alarm-ed, adjs.,  alarm-ed-ly,  adv.,  alartn-ing,  adj.,  alarm- ing-ly,  adv.,  alarmist  (q.v.) alarmist,  n.,  i)  one  who  starts  alarming  rumors; 2)  one  easily  frightened.  —  A  hybrid  coined  fr. F.  alarme  (see  prec.  word)  and  -ist,  a  sufT.  of Greek  origin.
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
2825:animist,  n.,  one  who  believes  in  animism.  —  See animism  and  -ist.
4051:autonomic,  adj.  —  See  autonomous  and  -ic. autonomist,  n.  —  Formed  with  suff.  -ist  fr.  Gk.
7333:chemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  actions  or  chemicals.  —  See  chemic. chemosis,  n.,  swelling  of  the  conjunctiva  (med.)  — Medical  L.,  fr.  Gk.  yfioiaic,  ‘affection  of  the eye  in  which  the  cornea  swells  like  a  cockle¬ shell’,  fr.  yj],u. r],  ‘a  yawning,  gaping:  cockleshell’, which  is  rel.  to  yatvsiv,  ‘to  yawn,  gape’;  fr. I.-E.  base  *ghei-,  *ghi-,  ‘to  gape,  yawn’.  See chaos  and  -osis  and  cp.  chela,  ‘claw’, chemotherapy,  n.,  —  Coined  by  the  Jewish  bac¬ teriologist  and  chemist  Paul  Ehrlich  (1854-1915) fr.  chemo-  and  therapy.
8689:conformation,  n.  —  L.  cdnformdtio,  gen.  -onis, ‘asymmetrical  forming’,  fr.  conformatus,  pp.  of conformare.  See  prec.  word  and  -ion. conformist,  n.,  1)  one  who  conforms;  2)  one  who conforms  to  the  Established  Church  ( English hist.)  —  Formed  fr.  conform  with  suff.  -ist. conformity,  n.  —  F.  conformite,  fr.  Late  L.  con- formis,  ‘similar,  like’,  which  is  rel.  to  L.  con- formare.  See  conform  and  -ity. confound,  tr.  v.  —  OF.  confondre,  confundre  (F. confondre),  fr.  L.  confundere  (pp.  confusus),  ‘to pour  together’,  fr.  con-  and  fundere,  ‘to  pour’. See  found,  ‘to  cast’,  and  words  there  referred to  and  cp.  esp.  fuse,  ‘to  melt’,  confuse. Derivatives:  confound-ed,  adj.,  confound-ed-ly, adv.,  confound-er,  n.,  confound-ing,  adj.,  con- found-ing-ly,  adv.
11384:digamist,  n.,  one  who  marries  for  the  second  time (in  contradistinction  to  bigamist,  which  denotes a  man  who  has  two  wives  or  a  woman  who  has two  husbands  at  the  same  time).  —  See  digamy and  -ist.
13799:euphemist,  n.  —  See  prec.  word  and  -ist. Derivatives:  euphemist-ic,  euphemist-ic-al,  adjs., euphemist-ic-al-ly,  adv.
21421:legitimist,  n.,  a  supporter  of  legitimate  authority.
=== KLN mix ===
1675:Derivatives:  admitt-able,  adj.,  admitt-ance,  n., admitt-ed,  adj.,  admitt-ed-ly ,  adv.,  admitt-ee,  n. admix,  tr.  v.  —  Back  formation  fr.  earlier  ad- mixt,  which  derives  fr.  L.  admixte,  ‘mixed with’,  but  was  mistaken  for  the  pp.  of  an  Eng¬ lish  verb  (i.e.  admixt  was  supposed  to  have  been formed  from  the  verb  admix  and  the  pp.  suff. -/).  L.  admixte  is  pp.  of  admiscere,  ‘to  add  to by  mingling,  mix  with’,  and  is  formed  fr.  ad- and  miscere ,  ‘to  mix’.  See  mixed  and  cp.  com¬ mix,  intermix.
1676:admixtion,  n.  —  L.  admixtio ,  gen.  -onis,  a  min¬ gling’,  fr.  admixte,  pp.  of  admiscere.  See  prec. word  and  -ion.
1677:admixture,  n.  —  Formed  with  suff.  -ure,  fr.  L. admixte,  pp.  of  admiscere.  See  admix, admonish,  tr.  v.  —  ME.  amonesten,  fr.  OF.  amo- nester,  fr.  VL.  admonestare,  fr.  L.  admonere,  ‘to remind,  suggest,  advise,  admonish’,  fr.  ad-  and monere,  ‘to  warn’.  See  monition  and  cp.  next word.  The  insertion  of  the  letter  d  in  OF.  ad- monester  and  E.  admonish  is  due  to  the  influence of  L.  admonere.  The  use  of  the  suff.  -ish  is  due to  the  influence  of  the  numerous  English  verbs ending  in  -ish,  in  which  this  suffix  corresponds to  OF.  and  F.  -iss  and  goes  back  to  the  Latin inchoative  suff.  -iscere.  Cp.  astonish,  distinguish, extinguish.
1750:•dversaria,  n.  pi.,  miscellaneous  notes.  —  L.  ad¬ versaria  (scil.  scripta),  lit.  ‘writings  turned  to¬ ward  one’,  neut.  pi.  of  adversarius.  See  ad¬ versary.
8384:commix,  tr.  and  intr.  v.  —  Back  formation  fr. earlier  commixt ,  which  derives  fr.  L.  commixtus, ‘mixed  together’,  but  was  mistaken  for  the  pp. of  an  English  verb  (i.e.  commixt  was  supposed to  have  been  formed  from  the  verb  commix  and the  pp.  suff.  -t).  L.  commixtus  is  pp.  of  commi¬ scere,  ‘to  mix  together’,  which  is  formed  fr.  com- and  miscere,  'to  mix’.  See  mixed  and  cp.  admix, intermix.
8385:commixtion,  n.  —  Late  L.  commixtio,  gen.  -onis, fr.  L.  commixtus,  pp.  of  commiscere.  See  prec. word  and  -ion.
8386:commixture,  n.  —  L.  commixtura,  fr.  commixtus, pp.  of  commiscere.  See  commix  and  -ture. commode, n.,  1)  a  chest  of  drawers;  2)  a  movable washstand.  —  F.,  fr.  commode,  ‘convenient, serviceable,  comfortable’,  fr.  L.  commodus,  ‘fit, suitable,  convenient’,  lit.  ‘measured  with’,  fr. com-  and  modus,  ‘measure,  manner,  mode’.  See mode  and  cp.  accommodate,  discommode, commodious,  adj.,  spacious,  roomy.  —  F.  com- modieux  (fern,  commodieuse),  fr.  Late  L.  com- modidsus,  fr.  L.  commodus.  See  prec.  word  and -ous.
14809:Derivative:  fixat-ive,  adj. fixation,  n.  —  ML.  fixatio,  gen.  -onis,  fr.  L. fixdtus,  pp.  of  fixare,  freq.  of  figere  (pp.  fixus), ‘to  fix,  fasten’.  See  fix  and  -ation. fixity,  n.  —  Formed  with  suff.  -ity  fr.  L.  fixus, ‘fixed’.  Cp.  F.  fixite  and  see  fix. fixture,  n.  —  Fr.  earlier  fixure,  which  is  formed with  suff.  -ure  fr.  L.  fixus,  ‘fixed’  (see  fix);  in¬ fluenced  in  form  by  the  false  analogy  of  mixture (rel.  to  mix),  in  which,  however,  the  /  is  organic (it  represents  L.  t  in  mixtus,  ‘mixed’,  pp.  of miscere,  ‘to  mix’).
19674:an  English  verb  (i.e.  intermixt  was  supposed  to have  been  formed  from  the  verb  intermix  and the  pp.  suff.  -t).  L.  intermixtus  is  pp.  of  inter- miscere,  ‘to  intermix’,  lit.  ‘to  mix  among’,  fr. inter-,  and  miscere,  ‘to  mix’.  See  mixed  and  cp. mix,  admix,  commix.
23049:maskery,  masquery,  n.  —  F.  masquerie,  fr.  mas¬ quer,  ‘to  mask’,  fr.  masque.  See  mask  and  -ery. maskelynite,  n.,  a  feldspar  mineral  (mineral.)  — Named  after  the  English  mineralogist  Nevil Slory -Maskelyne  (1823-1911).  For  the  ending see  subst.  suff.  -ite. maskinonge,  n.  —  See  muskellunge. maslin,  n.,  a  kind  of  brass  (obsol.)  —  ME.,  fr. OE.  meestling,  m  testing,  mseslin,  rel.  to  MDu., M  HG.  messinc,  missinc,  Du.  messing,  G.  Mes¬ sing,  ‘brass’.  These  Teut.  words,  as  well  as Czech  mosaz,  Slovak  mosadz,  Pol.  mosiqdz, ‘brass’,  ult.  derive  fr.  Gk.  Moaouvoixoi;  yeOutiq, ‘brass  made  by  the  Mossynoikoi’,  a  people  liv¬ ing  south  of  the  Euxine,  lit.  ‘those  dwelling  in (zoaouvec  (i.e.  wooden  houses)’.  Brass  is  said to  have  been  first  manufactured  by  the  Mossy¬ noikoi,  whence  the  name  Moaouvotxo?  yotXxoq. maslin,  n.,  a  mixture  of  different  kinds  of  grain. —  ME.  mastlyoun,  mestlyon,  fr.  OF.  mesteillon, mestillon,  fr.  mestueil,  mesteil  (F.  mdteil),  fr. VL.  *mistilium,  which  was  formed  from  the adjective  *mistilis,  fr.  *mistus,  a  collateral  form of  L.  mixtus,  pp.  of  miscere,  ’to  mix’.  See  mix. masochism,  n.,  a  form  of  sexual  perversion  in which  one  finds  pleasure  in  being  hurt  ( med.); the  opposite  of  sadism.  —  Named  after  the Austrian  novelist  Leopold  Sacher  Masoch (1836-95),  who  describes  it  in  one  of  his  works. For  the  ending  see  suff.  -ism. masochist,  n.  —  See  prec.  word  and  -ist.
```


## [2026-09-07T16:12:47.891Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"mixed,  adj\\|mist,  n\\|mistletoe\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T16:12:47.979Z] TOOL RESULT

```
1470:acosmism,  n.,  the  denial  of  the  independent  real¬ ity  of  the  world  as  distinct  from  God.  —  Coined by  Fichte  and  Hegel  fr.  Gk.  priv.  pref.  a-, xoop.0?,  ‘the  world’  (see  cosmos),  and  suff.  -ism. acosmist,  n.,  one  who  believes  in  acosmism.
2091:Derivatives :  alarm ,  tr.  v.,  alarm-able,  alarm-ed, adjs.,  alarm-ed-ly,  adv.,  alartn-ing,  adj.,  alarm- ing-ly,  adv.,  alarmist  (q.v.) alarmist,  n.,  i)  one  who  starts  alarming  rumors; 2)  one  easily  frightened.  —  A  hybrid  coined  fr. F.  alarme  (see  prec.  word)  and  -ist,  a  sufT.  of Greek  origin.
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
2825:animist,  n.,  one  who  believes  in  animism.  —  See animism  and  -ist.
4051:autonomic,  adj.  —  See  autonomous  and  -ic. autonomist,  n.  —  Formed  with  suff.  -ist  fr.  Gk.
7333:chemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  actions  or  chemicals.  —  See  chemic. chemosis,  n.,  swelling  of  the  conjunctiva  (med.)  — Medical  L.,  fr.  Gk.  yfioiaic,  ‘affection  of  the eye  in  which  the  cornea  swells  like  a  cockle¬ shell’,  fr.  yj],u. r],  ‘a  yawning,  gaping:  cockleshell’, which  is  rel.  to  yatvsiv,  ‘to  yawn,  gape’;  fr. I.-E.  base  *ghei-,  *ghi-,  ‘to  gape,  yawn’.  See chaos  and  -osis  and  cp.  chela,  ‘claw’, chemotherapy,  n.,  —  Coined  by  the  Jewish  bac¬ teriologist  and  chemist  Paul  Ehrlich  (1854-1915) fr.  chemo-  and  therapy.
8689:conformation,  n.  —  L.  cdnformdtio,  gen.  -onis, ‘asymmetrical  forming’,  fr.  conformatus,  pp.  of conformare.  See  prec.  word  and  -ion. conformist,  n.,  1)  one  who  conforms;  2)  one  who conforms  to  the  Established  Church  ( English hist.)  —  Formed  fr.  conform  with  suff.  -ist. conformity,  n.  —  F.  conformite,  fr.  Late  L.  con- formis,  ‘similar,  like’,  which  is  rel.  to  L.  con- formare.  See  conform  and  -ity. confound,  tr.  v.  —  OF.  confondre,  confundre  (F. confondre),  fr.  L.  confundere  (pp.  confusus),  ‘to pour  together’,  fr.  con-  and  fundere,  ‘to  pour’. See  found,  ‘to  cast’,  and  words  there  referred to  and  cp.  esp.  fuse,  ‘to  melt’,  confuse. Derivatives:  confound-ed,  adj.,  confound-ed-ly, adv.,  confound-er,  n.,  confound-ing,  adj.,  con- found-ing-ly,  adv.
11384:digamist,  n.,  one  who  marries  for  the  second  time (in  contradistinction  to  bigamist,  which  denotes a  man  who  has  two  wives  or  a  woman  who  has two  husbands  at  the  same  time).  —  See  digamy and  -ist.
12326:—  F.  druide,  fr.  L.  pi.  druides  (Caesar),  druidae (Cicero),  fr.  OCelt.  druid,  which  stands  for *dru-wid,  and  is  compounded  of  *daru-,  *dru-, ‘oak’,  and  *wid-,  ‘know’,  hence  lit.  meaning ‘they  who  know  the  oak’ ;  so  called  in  allusion to  their  practices  with  the  mistletoe.  Cp.  Pliny, 16,  249.  For  the  first  element  see  tree  and  cp. dryas,  Drusilla,  for  the  second  see  vision. Derivatives:  the  hybrids  druid-ess,  n.,  druid-ic, druid-ic-al,  adjs.,  druid-ism,  n.,  druid-ry,  n.
13799:euphemist,  n.  —  See  prec.  word  and  -ist. Derivatives:  euphemist-ic,  euphemist-ic-al,  adjs., euphemist-ic-al-ly,  adv.
```


## [2026-09-07T16:12:56.403Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"OE\\. mist\\|OE.  mist\\|mist, n\\., water\\|micturition\" KLN_1971.txt | head -10; echo \"---\"; grep -n -m5 \"mist\" KLN_1971.txt | head -3; echo \"=== try grep 'to urinate' ===\"; grep -n \"to  urinate\\|to urinate\" KLN_1971.txt | head -10"
}
```


### [2026-09-07T16:12:56.493Z] TOOL RESULT

```
4362:-wire cp. esurient, micturition, parturient, vomi- 
81268:micturition. 
145988:mezgd, Pol. miazga , ‘sap’. See micturition and 
151110:micturition, n., 1) a morbid desire to urinate; 2) 
152719:mist, n. — ME., fr. OE. mist , ‘darkness, gloom’, 
152741:mistletoe, n. — OE. misteltan , compounded of 
152967:L. meiere , mingere , ‘to urinate’. See micturition 
---
219:discovered several thousand mistakes in the standard etymological dictionaries, I decided 
313:What the elements are to chemistry, what the sounds are to music, are words to language. 
352:dipped him into the river Styx to render him invulnerable ; first used by the Dutch anatomist Verheyden 
=== try grep 'to urinate' ===
145987:L. meiere , mingere, ‘to urinate’, Russ. 
151106:micturate, intr. v., to urinate, — .Formed irreg- 
151110:micturition, n., 1) a morbid desire to urinate; 2) 
151113:stem of micturire ‘to desire to urinate’, desider- 
151114:ativeof mingere, pp. stem mict-(um), ‘to urinate’, 
151118:Gk. 6[i.si.x etv J &jztX e *- v > <to urinate’, {xoix 6$, -‘adul- 
151123:migen, ‘to urinate', OE. micga , migoda, ‘urine’, 
152965:ON. miga, MLG. migen , ‘to urinate’, OE. micga, 
152967:L. meiere , mingere , ‘to urinate’. See micturition 
230780:See stale, ‘to urinate’, and cp. stalagmite. For
```


## [2026-09-07T16:12:59.946Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '151106,151132p;152715,152750p' KLN_1971.txt; echo \"=== mix/miscellaneous ===\"; grep -n \"miscellaneous, adj\\|miscellaneous,  adj\\|^mix, tr\\|mix, tr\" KLN_1971.txt | head"
}
```


### [2026-09-07T16:13:00.056Z] TOOL RESULT

```
micturate, intr. v., to urinate, — .Formed irreg- 
ularly fr. L. micturire. See next word and 
verbal suff. -ate. 

micturition, n., 1) a morbid desire to urinate; 2) 
excessive urination; 3) the act of urinating. — 
Formed with suff. -ion fr. L. micturit-(um ), pp. 
stem of micturire ‘to desire to urinate’, desider- 
ativeof mingere, pp. stem mict-(um), ‘to urinate’, 
which is rel. to meiere (for *meighiere), of s.m., 
and cogn. with OI. mehati , ‘urinates’, pp. midhdh , 
Avestic maezaiti , ‘urinates, manures, dungs’, 
Gk. 6[i.si.x etv J &jztX e *- v > <to urinate’, {xoix 6$, -‘adul- 
terer’, Arm. mez, ‘urine’, mizem, ‘I urinaje’, 
(prob. denominated fr. mez), Toch. B miso, 
‘urine’, earlier Lith. miniu , Lith. m$2u, Lett. 
mizu, ‘I urinate’, OE. migan , ON. miga, MLG. 
migen, ‘to urinate', OE. micga , migoda, ‘urine’, 
Goth, malhstus, OE. meox, ‘dung, filth’. See 
mash, n., andcp. mistletoe, mixen. For the desid- 
erative suff. -urire in L. micturire cp. Abiturient 
and words there referred to. 
mid, adj. — ME., fr. OE. midd, rel. to ON. midr , 
OS. middi, OFris. midde, OHG. mini, Goth. 
midjis , ‘mid’, and cogn. with OI. madhyah, Gk. 
jjticjoq, L. medius , ‘middle’. See media, ‘voiced 
stop consonant’, and words there referred to 

lettre missive , lit. ‘a letter sent’. See missive, adj. 
missy, n., a young girl {colloq.) — Formed from 
the noun miss with suff. -y. 
mist, n. — ME., fr. OE. mist , ‘darkness, gloom’, 
rel. to ON. mistr, Swed., MDu., Du. mist , ‘mist’, 
fr. I.-E. base *meigh whence also 01. meghdh , 
‘cloud’, mih -, ‘mist, vapor’, Avestic maeya 
‘cloud’, Arm. meg, ‘mist’, Gk. opuxto], ‘cloud, 
mist’, Alb. mjeguie , OSlav. migla, Lith. migla, 
Lett, migla, ‘mist’. Cp. mizzle, ‘to drizzle’. 
Derivatives: mist, intr. and tr. v., misty (q.v.) 
mistake, tr. and intr. v. — ME. mistaken , fr. ON. 
mistaka, lit. ‘take in error’, formed fr. mis- and 
taka, ‘to take’. See take. 

Derivative: mistake, n. 
mister, n. — Weakened form of master, 
mistery, n. — A var. of mystery, ‘trade’, 
mistic, n., a kind of small coasting vessel. — Sp. 
mistico, prob. fr. Arab, musdttah, ‘an armed 
ship’, lit. ‘something spread out, something 
even or level ; surface’, prop, passive part, of the 
2nd conjugation of sataha, ‘he spread abroad, 
spread out’, which is rel. to Heb. shatdh, Aram. 
sh e fah, Aethiop. sataha , of s.m. 
mistletoe, n. — OE. misteltan , compounded of 
mistel, ‘mistletoe’, and tan , ‘twig, branch’. The 
first element is rel. to Du., MHG., G., Dan., 
Swed. mistel, OS., OHG. mistil, ON. mistilteinn, 
‘mistletoe’, and prob. also to OHG. mist , ‘dung’ 
(the plant being propagated by bird dung). See 
mash and cp. mixen. Cp. also missel thrush. OE. 
tan, ‘twig’, is rel. to OS., OFris. ten , ON. teinn, 
Du. teen, OHG. zein, Goth, tains , ‘twig’, OE. 
tznel (whence obsol. E. teanal), OS. tend, ‘bas- 
=== mix/miscellaneous ===
7725:admix, tr. v. — Back formation fr. earlier ad- 
52025:commix, tr. and intr. v. — Back formation fr. 
125426:intermix, tr. and intr. v. — Back formation fr. 
152470:miscellaneous, adj., mixed, consisting of various
```


## [2026-09-07T16:13:10.956Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '152470,152480p' KLN_1971.txt; echo \"...\"; grep -n \"^mix\" KLN_1971.txt | head; echo \"=== mixed ===\"; grep -n \"mixed, adj\" KLN_1971.txt | head"
}
```


### [2026-09-07T16:13:11.057Z] TOOL RESULT

```
miscellaneous, adj., mixed, consisting of various 
kinds. — L. miscelldneus , ‘mixed, miscellane- 
ous’, fr. miscellus , ‘mixed’, fr. miscere , ‘to mix’. 
See mix. For E. -ous, as equivalent to L. -us, 
see -ous. 

Derivatives: miscellaneously , adv., miscellane - 
ous-ness, n. 

miscellany, n., 1) a medley ; 2) a collection of writ- 
ings on various subjects. — F. miscellanies 
...
7726:mixt, which derives fr. L. admixtus, ‘mixed 
7733:mix, intermix. 
11613:mixture; ‘the rule of mixtures’. — L. alligatio , 
34137:mix together, embroil, confuse’, which is prob. 
52712:mix’, fr. OF. componre, compondre, fr. L. corn- 
59216:mix, mingle, blend, temper’, &x£paaxo<;, &cpa- 
78078:mixing, blending’. See crater and cp. crasis. 
125434:mix, admix, commix. 
143212:mix; to make’. The sense development of the 
149278:mixed’, orig. prob. ‘bright, clear’, cogn. with 
=== mixed ===
152946:mixed, adj. — For mixt, fr. F. mixte. See mix.
```


## [2026-09-07T16:13:15.580Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '152946,152990p' KLN_1971.txt"
}
```


### [2026-09-07T16:13:15.648Z] TOOL RESULT

```
mixed, adj. — For mixt, fr. F. mixte. See mix. 
mixen, n., dunghill {archaic or dial.) — ME., 
fr. OE., ‘dung, dunghill’, rel to OE. meox, 
‘dung, filth’, OS. mehs, mist, OHG., MHG., G. 




MIXO- 



470 



(q.v.) 

mist, Goth, maihstus, ‘dung, filth’, OE. migan, 
ON. miga, MLG. migen , ‘to urinate’, OE. micga, 
migoda , ‘urine’, and cogn. with Gk. 6fJt.et.xeLV, 
L. meiere , mingere , ‘to urinate’. See micturition 
and cp. mash, mistletoe. 

mixo-, combining form meaning ‘mixed’. — Gk. 
pt£o-, fr. mixing, mingling, inter- 

course’, from the stem of |XLyvuvai, pioyeWj 
‘to mix’. See mix. 

Mixodectes, n., an extinct genus of insectivores 
( paleontol .) — ModL., compounded of mixo- 
and Gk. Stqxt ?]<;> ‘biter’, which is rel. to Saxveiv, 
‘to bite’, fr. I.-E. base *denk -, ‘to bite’, whence 
also OI. dasati (for *dnketi), ‘bites’, OE. tang , 
tange , ‘tongs’. See tongs and cp. words there 
referred to. 

Mixosaurus, n., a genus of extinct reptiles ( pale- 
ontol ,) — ModL., compounded of mixo- and 
Gk. craupoc, ‘lizard’. See sauro-. 
mixture, n. — ME., fr. OF. misture (F. mixture ), 
fr. L. mixtura, ‘a mixing', fr. mixtus , pp. of 
miscere, ‘to mix’. See mix and -ture.
```


## [2026-09-07T16:13:20.061Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"I.-E. base \\*meik\\|\\*meik-\\|\\*meig-\" KLN_1971.txt | head; echo \"=== SKT mix/mist ===\"; grep -n \"^mix\\|mist, vapour\\|mist (1)\\|mist,\" SKT.txt | head"
}
```


### [2026-09-07T16:13:20.143Z] TOOL RESULT

```
152926:*mik-sko ), ‘I mix’, fr. I.-E. base *meik - (var. 
=== SKT mix/mist ===
520:chomiBt,  Christ.  (Ck.)  Shortened form*  of  akhtnttsff  (xlckymist,  formed  by dropping  the  Arab,  article  al,
2332:Perhaps  related  to  G.  brudeJn,  br^dtM,  to bubble  (whence  to  give  off  steam,  coofose) ; a.  brodel,  broifem,  vapour,  allied  to  E. Breath  (Schclcr).  Cf.  F.  btvuUhrJ,  a mist,  fog.  %  We  also  find  >N.brxKh^  tumult, broiheii.  a  tempest ;  Gael.  brei,^hUadh,  titf- moil.  broigiuk,  noise  (pcrhft[>.s  unrelated). Broker.  <E.)  SceBrooku)- Bronchial.  (Gk.)  Gk.  Bfiyx****  neol. pi.,  the  ramifications  of  the  windpipe.— Gk.  ^p6yxot,  ihe  windpipe  ;  cf.  fipnyx*^-  ' gill.  Allied  to  Gk.  a^x'"*'  ^^  ^<^^-  ^*'* brvrKk't'tis;  (rom  0p6yxof. Bronze.  (F.-ltal.-Teat)  SeeBrown. Brooch.  (F.-L.)  Named  from  the  pin which  fastens  iL  M.  E.  brockr,  a  pin,  yejL brooch.  —  F.  brocht,  a  spit,  point.  —Low  L bnvfa,  a  pointed  stick.  — L.^/vrinttj,  ashaip tooth,  pomt  Cf.  Gael.  bn>ff,  to  goad.^r^, on  awl ;  \V.  procio^  to  stab.
3355:Chemise.  (K.-L-C?)  ¥.  chemist, •-Laic  L.  ramiVt'a,  a^iirt,  ihin  dress.  I'rob. Celtic;  cf.  U.  Iii&h  taimma,  shiiU
11717:transmit.     (L.)     L.    trans^    mcross ; mitUrt,  to  send.    Der,  trans  miss  ten  (from pp.  missus). uiselon.  Missive ;  see  Bliasilo. Mist.  (£.)     A.  S,  mist,  gloom,  darkness. •4-  IceL  mistr,  Du.  Swed.  mist,  mi&^t ;   G. mist,  dung  (the  same  word'} ;    Golh.  math- Jtuj,  dung.     Formed,  with  suffixed  'St,  from the  base  MIC  (Aryan  MICH),  as  seen  in  , Luhoan.  mtgla,   Koss.  m^^,   Gk.  i>ftix^^>  \ niBt.   Ski.    mih'ira,   a  doud,    me,^ha,    a dowL    Cf  Skt,  miJk,  to  spriolde.  lo  uriiM ; '
11724:•f  G.  mistelJrosiel.  mistle-thruUL I     mistletoe.   (E.)     A  final  ji  lui I  lost     A.S.  miittUdn.  -  A.  S.  mistily I  used  alone  in  the  sense  of  mistletoe  ? a  twig.     Mistet  is  from  A.  S.  mist, \  which  in  O.  Do.  had  the  sense  of  '  x or  bird  lime,  and  in  G.  has  the  toa dung.     Thus  the  sense  is  *  birdlime-* The  A.  S.  tdn,  twig,  is  the  same  u ,  teitiM,  Du.  /««,Goth.  tainr,  Dan.  U/M.S* teity  twig,  spindle.  +  IceL  mitttiuinn^  « tletoe.
11725:I      mizale.  to  rain  in  fine  drops.  fE.)    '' I  merly  misle,  put  for  mtst-U*,  fieqoeoUT I  form  of  mist,  to  form  vapour  toaK^ ,  For  the  loss  of/,  cf.  pronunciation  oivW glisten,  listen,  &C- Uistake.  toerr.  (Scand.*)    led  mot lo  take  by  error,  make  a  slip.  —  IccL^ wrongly  ;  taJta,  lo  lake.     Sec  Kl*-  tO  ' Take. Mister;  see  Msffnitude. Mistletoe ;  see  Mist. Mistress ;  see  Ma«iiitade. Mite  (1),  an  insect  vE.)    H.  C  ■< .AS.  mite,  a  mite. •4- Low  G.  anif,  CXB< mlid,  a  mite.   The  word  means  '  cvCltr/ 1 biter;  fiom  Teut  base  MIT.  to  cut,  • Coth.  maitam,  Tcel.  meita,  to  cot
13820:Pessimist,  one  who  complains  that  sfl is  for  the  worst  C^-)  Coined  fr^  ,L ptsrim-us,  worst ;  supcrL  connected  wiA peter,  woi^ ;  sec  Impair
18736:Btllffy.  close,  stifling.  (F.  -  L.)  From O.  F.  tsloufftr^  to  choke  (F.  itimff<r\.  The same  ts  O.  F  esioffer,  to  stuff  or  cram  up. -  O.  F.  tsUffe,  stuff  (above).  ^  &..  Schclcr, disputing  the  su^^^iion  of  Diez,  who  need- lessly goes  to  the  Gk.  rv^or,  smoke,  mist, in  unJcr  to  explain  tstoffe.
```


## [2026-09-07T16:13:28.567Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW misceo ===\"; grep -n \"misceo\\|mi-sceo\" LEW_1910.txt | head -5; echo \"=== LAT misceo ===\"; grep -n \"misceo\" LAT.txt | head -5; echo \"=== IEC meik ===\"; grep -n \"meik-\\|misceo\\|miks\" IEC.txt | head -10"
}
```


### [2026-09-07T16:13:28.645Z] TOOL RESULT

```
=== LEW misceo ===
=== LAT misceo ===
38136:misceo.
38273:poetiques et tardifs); mirio,-onis: admirateur (Tert.); miraculum:misceo
38295:misceo, -es, -ui, mixtum, -ere: meler, melanger. Ancien (Enn.,
38315:A misceo se rattache sans doute 1 1 adj. miscix (conjectural, le ms.
38325:Composes: ad-, com-, im~, inter-, per-misceo", immixtus "non melange"
=== IEC meik ===
10511:méK- (meKs-, meKst-, méKsl-) ‘dung, filth’. Cf. miks- (1) with velar cons. Arm. mesim ‘grow mouldy’; mec, gs meçi, i-st ( ‘mould, rot: Go. maihstus ‘dung’); Go.
10794:miks- (misk-) (1) ‘slime’. WP II, 245. Cf. miKs-, etc. Skt. cf. a-miksà, f. ‘curds’; Arm. cf. mxem 'im- merse’; mxim ‘plunge’; Br. mécht michi, m. (*mucus'. Ambig. cf. muks-); Gk. mískoi, pl. ‘rubbish, garbage’; OS mehs, n. ‘dung, filth’; OE meox, n. id.; cf. G Mist, m. (fr. *mikstos); Du. mest, id. (OCS mïšelň, m. = ‘baseness; Rum. LW misel, ‘base, vile’; m. ‘cad’)
10795:miks- (2) ‘squeak’ W mich, m. id.; Li. cf. miksiù, éti, v. ‘hiccup’
10796:miks-, variants miks- & misK-, see following entries. WP II, 244
10797:miKslos, miKsros ‘mixed, stirred, confused. See next Skt. mi$ráh, id.; Arm. cf. mxlem, v. ((spoil, fr. *mikslio); Lat. cf. miscellus *mixed'; Cz. cf. o-msely (2) ‘tattered, grubby’; Li. mislüs, miš- rùs & miras *mixed'; simplex in Ir. measc, id. & W mysg ‘midst
10798:miKso, ið (miKsko, mimiKs-, beside miks-, misk-, etc.) “mix, confuse, stir'. WP II, 244 Skt. cf. mímiksgàmi, v. id.; Gk. cf. mísgo, fut: míxoó, id. (consonantism unexplained); Lat. misceo, ere, id.; Olr. mescaim, Ir. meascaim, id.; OBritish -misc-, v. id.; Br. meski, meska, id.; W mysgu, id.; OHG miskan, OE miscian, id.; Li. myštu, misti, intr. (‘get mixed, con- fused', fr. *miKsK-); Latv. cf. misa, f. ‘mash’;
10801:miksos, à, is ‘mixed; mixture’. WP II, 244. Cf. miKslos, etc. Mir. mess ‘mixture’; measc mixed, confused’; m. ‘midst; W mysg, m. id.; Li. cf. misinýs, m. ‘mixture’
10802:mikstos (mikstos) ‘mixed’. Cf. mikso Gk. miktós, id.; Lat. mixtus, 1d.; Ir. measctha, id.; Br. cf. meskid, id.; MHG cf. ge-mischede, sn. ‘mixture’; Li. mistas “mixed, confused”
10844:(misk- see miks-; misK-, see miKs-)
11028:moiks- (o-gde form of type miks-, q.v.). WP II, 245 Skt. meksayami, tr. ‘stir; Gk. cf. aor. (e-gde) é-meixa ‘I mixed; MHG meisch, adj. 'in- fused; meisch, sm., G Meische, f. ‘mash’; Ger. cf. meischen, v. Cinfuse': E dial. to mash, id.); OCS měšọ, mésiti & mésati, v. ‘mix’; Li. mai&aü, ýti, id.; Late maisu, it, id.; (e-gde in) Li. miefiü, ti, v. id. and in OCz. mí&&ti, id.; (z-gde in) Ir. meascaim, W mysgu, id. and in OS mehs, n. ‘dung’. Grade uncertain in Arm. mec, gs meçi, meciv, i-st. trot, mould’; mesim, v. ‘grow mouldy’. A variant of type *moiK- occurs in OE mah ‘wanton, shame- less, but see moigh-. Extn. in Li. maisalas, m. “medley”
```


## [2026-09-07T16:13:34.169Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '38295,38330p' LAT.txt"
}
```


### [2026-09-07T16:13:34.218Z] TOOL RESULT

```
misceo, -es, -ui, mixtum, -ere: meler, melanger. Ancien (Enn.,
Pl.), usuel. Les formes romanes supposent *miscSre, cf.M.L.s6o4; v.h.a.
miscen.
Derives en misc- et en mixt-: 1'-niscuus,-miscus,-a,-um, attestes
dans promiscuus "melange", promiscam". ~ dicebant pro promiscue,
P.F.«50,26, ancien accusatif f^minin employe adverbialement, cf.
Pii, As.366, operam promiscam dare, et Ru.nOaj promisce . Il est a
noter qu'un certain nombre de ces adj. en -uus ne figurent que dans
les composes; cf,assiduus, contiguus, etc. On trouve aussi dans
les gloses un verbe miscuo, avec un adj. miscudtus",
miscellus,-a,-um (arch. et postclass., M.L.56o3a miscellum ); miscellio,
-onis : -es appellantur qui non certae sunt sententiae, sed uariorum
mixtorum iudiciorum sunt, P.F.no, 0 ;
miscellaneus (lat.imper.) : employe surtout au n.pl. miscellanea "pot
pourri" (peut-etre mot de 1'argot des gladiateurs, cf.Juv.11,20).
Miscellus est sans doute le diminutif de misculus qui est attest 4
indirectement par le verbe misculare auquel remontent certaines
formes romanes, M.L.5606, et germaniques (v. h. a. misce 16 n), a cot 4
d'autres qui sujiposent miscitdre, M.L.5605. Sur un miscellus qui
serait issu de minuscellus, v.M.Leumann, Glotta 11,190.
A misceo se rattache sans doute 1 1 adj. miscix (conjectural, le ms.
a mixcix) de Petrone 45,6, de sens obscur: "mele-tout, brouillon,
gacheur"? La formation serait comparable A celle de felix, pernix .
«* mixtus,-us m.: melange, et dans la 1. rustique "melange de semences",
cf. Coi.6,37,7 , sens technique qu'on retrouve dans les d£riv 4 s romans
de mixtum, mixtid, mixtilia "m^teil", cf, mixtura, cf. M.L.56 1 9“S<>22.
mixtio,- 5 nis f. (lat. imper.): m 41 ange; mixtS,-as (Mul.Chir.);
mixtarius (?), cf. Non.546,20 mixtarium, quo miscemus, = xptxxrip;
mixticius (lat. eccl.), traduisant gr. cn>|4UXT0C, cf.fr .mdtis, M.L.5618;
mixtura, M.L.5622; iri. maistreadh, Cf.aussi M.L.5617 *mlxticare.
Composes: ad-, com-, im~, inter-, per-misceo", immixtus "non melange"
(Aus., = cc^uxtoc;); impermixtus (rare, non class.); remisceo, M.L.7i96a.
Racine *meik'~ avec doublet *meig’~ : skr. migrdh et lit.mtjfrus
"mel£"; fournissait sans doute un pr^sent radical ath 4 matique, remplac^
en lituanien par mesip, meSti "meler"; le slave n'a que le causatif733
ml t±s
```


## [2026-09-07T16:13:40.084Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"mei\\ĝ\\|meiĝh\\|meik\\|maiz\\|maēz\\|maeza\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T16:13:40.131Z] TOOL RESULT

```
ugrep: error: error at position 8
(?m)mei\ĝ\|meiĝh\|meik\|maiz\|maēz\|maeza
        \___invalid escape
```


## [2026-09-07T16:13:43.533Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n -e \"meiĝh\" -e \"meik\" -e \"maēz\" -e \"maeza\" -e \"mih-stu\" -e \"maihstus\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T16:13:43.587Z] TOOL RESULT

```
16033:y auf die \on Anfang an zu meik- gehorigen Bildungen                                 iibergegriffen habe;^
16096:„Harn‘';            av. maezaiti           „harnt,    diingfc^,    maVsnia-,    maesmaii- „Harn“;          arm.
16109:migany mnd. mlgen ,,harnen'^ ags. micgay Nticge, migod „IIarn'', got. maihstus.
16143:Dagegen        die unter meik- ,,mischen‘‘ genannten Worter fiir „Molkem
20453:„na6“,   s.   d. ;    desgleichen     gall.-lat.   ‘^mesga,   ir.    medg „Molken“            (s.    u.    meik-
45524:in norw. smika „streichen, streicheln, glatten^*, smeikja „streicheln, lieb-
45595:glatten", aisl. smeikr ,,glatt, schuchtern", s. Wood Men. 22, 236.
```


## [2026-09-07T16:13:46.476Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '16000,16150p' WLD_Bd2_pages.txt"
}
```


### [2026-09-07T16:13:46.528Z] TOOL RESULT

```
„dunn, winzig“ (kelt. Abl. l-.ei, Pedersen KGr. I 51, 181: von Pick II*
204 nicbt besser zu mei- „klein“ gestellt).
  Alb. mire „gut, sch6n“ (G. Meyer Alb. Wb. 279); lit. 7nelas, „lieb“,
meile     „Liebe“, meih'is „liebreieh“,                tnijliu,       myUti      „lieben“,       myh'is „lieb“,
susimil-stu,           -ti     „sich erbarmen“,
                                         mils (Endzelin KZ. 42, 378) ”lieb“,^
                                                     lett.
mU'sch ds., apr. mils ds., lett. mtlet „lieben“, melut „bewirten“: abg. mih
„erbarmen8wert, mitleidenswert“, russ. mih „lieb, lieblich, angenehm“
(usw.,      s.       Berneker II      57f.,   auch     iiber       ksl.    milo „Mitgift“); lett. mvrs
„Priede“, abg. mir^ „Priede“ und „yMafiog“                                (zurBed. s. Meillet Et. 404              ’
Berneker II 60 f.).
   Auf me[i\-l- mit idg. geschwundenem i und damit sekundar ablautendes
mo-l- bezieht Persson Wzerw. 233, Reichelt KZ. 39, 10; gr. (jon.) rd
                                                                     yeiha
„erheiterndes; erfreuliche Gaben: Brautschatz, Schmucksachen“, lesb.
                                                                       yeX-
hyog, kret. yyXlyiog, jon. yeiXiyog, -tyiog, att. (mit Wandel von -Ui-
                                                                         zu
-Ui-, Wackernagel IP. 25, 328) /uihyog „freundlich, liebreich“
                                                                   (*yeX-r-
aus ^mel-n-') und lit. maldne „Gnade“: etwas unsichere Konstruktion.

nieik- „mischen", Prasensstamme auch mit -so-, -slco.
  Ai. meksdtjati (minuksc ,.ruhrt um“, meksana- n.
                                                      .,Euhrstab==,                                         7niip-d-
„vermischt-‘, mir-rdyati „mischt“, av. (Bartholomae IP.
                                                        10,                                  II,      Airan. Wb.
1186f.) rnisvan- „die gemischten enthaltend“;
   gr.                      (riehtiger ueiyvvyr,            ei.i{e)iy.To, eylyyv) „mische“,
yiayco    ds.,        yiya,     ytyda Adv. „gemischt“, yiydg-dSog „Gemisch“ (um das
ausl. -y- zu rechtfertigen,               nimmt Wackernagel KZ. 33, 39, Bally Msl.                               12,
327 ein zu m'^zg- „tauchen“ gehoriges Praes. ^yi-yzyco                              = ylayoj an, dessen
y auf die \on Anfang an zu meik- gehorigen Bildungen                                 iibergegriffen habe;^
unsicher)        ;



   lat.   misceo,           -ere   „mischen“ (Erw. von mi\k]-sko, Brugmann IP                              3.   262-
                               fmixjVos zunachst zu          ai.   7neksaynfi gehore,            z.   B.   Sommer
Mdb       610,        1st    nicbt sicher; es konnte ein mi'sceo
                                                                 gebildetes *»i(St‘i7os nach
der Synkope Lmstellung von                    -set-    zu     -cst-   erfahren haben)        ;
                                                                                                  air.     commes-
catar „miscentur“, Inf. 7nescad (aus
                                                                      in die d-Flexion iibergefuhrt).
                                                     meigu        meigh-                                    245

cyinr. mysgu ,inisclieii“; ahd. misTcan^ ags. miscian „iiiischen'‘ (eher lat.
                          5


Lw. als urverwandt: s Brugmann II^ 3, 35 J, Kluge Weigand-Hirl; s. v.;
dt. 3Iaische usw., die, weun verwandt gegen Entlehnung sprechen konnten,
besser zu abg. m^zga^ s. u. meiyhs „harneii^');
  Lit. maiszafc^ -yti „mischen, inengen% lett. mat sit „inischen, mengen;
zum 2. Mai pfliigen^^ apr, may sot an „gemengt (d. i. bunt)^*, lit. malszalas
j,Gemeugsel“ matsztas „Aufrahr“                          (bait, sz    wie    slav.   s*   in abg. m^siti   kann
            -As-, ksh sein),           mesziu^ meszti ds.                   Osten-Sacken IF.
                                                                   (Belege bei       v. d.

33,         233),    sitmisztu^           snmtszti „sich durcheinandermengen, in Yerwirrung
geraten‘‘ (Praet. snmiszaii   aus dem sAo-Praesens ? Brugmann II ^ 3, 352)
lett.miset „misclien, irremachen'^, alit. mischlnmas j^Yermischung*', lit.
miszriu Adv. ,durcheinander“ (vgl. ai. micrd-)^ lett. mistrs „gemi8cbt“;
                              5


abg.mesrf, mesitl „mischen‘‘, nmcsiti chleh^       (usw., s. Berneker Il52f.).
   Ygl. Curtius 334, Fick I ^ 103, 510, 11^216, III^ 321 £, Pedersen IF.
5, 68,  KG. I 76, Brugmann I^ 568, II ^ 3, 141, 262, 267. 35 If., 356,
Berneker aaO.
   Hieher wohl (Pedersen KG. I 88) ai. a-mihsa „Quark von Milcb“, osset.
(Liden   Stud. 41 Anm. 1) misin „Buttermilch“, mir. medg^ cymr. maidd^
ncorn. meiilt, abret. meid^ gall.-lat. "^mesga (frz. megue) „Molken“ (Gdf.
'^mlsga\ Yf. KZ. 34, 502, Meyer-Liibke Rom. Wb. 204), aisl. mysa „Molken“
{^m'disivon- B>ugge Svenska Landsmalen 4, 2 S. 235, Sverdrup IF. 35, 157);
                     ^


Yerwandtschaft mit slav. 7nezga (s. o.) ist nicbt vrahrscheinlicher (noch
anders stellt Charpentier KZ. 46, 39 die kelt. Worter als Ablautform zu
mozgJio- ,,Mark'').

nieigu- „wechseln, tauschen; eine Ortsveranderung vornebmen^\
   Gr.        djuEtfia)           „wechsle“,    med. ,,erwidere,           vergelte.      wandere'*,   djuoij^o^
.,wecbselnd“,            dfLioiprj        ,,^Yechseb^
  Lat. migro^ -are „wandern“, Denom. eines "^mkjV^-ros, Walter KZ. 11.
430 Fick BB. 6, 213, Wb. I^ 510.
        j
                                   Erw. von mei” „wechseln‘‘ (Persson
Wzerw. 15, 28,                     156)
   Ksl. miglivz bedeutet nicht „beweglicli‘‘, sondern ,,blinzelnd‘‘                              (Berneker II
56)         und bleibt fern.
meigh- „liarnen“ (Praes. meigho und mingho),
  Ai. //^c/ia/2 „barnt“, ptc. nudha- (= lat. mictus), nhdlia- n. ,,Kot‘‘, nielia- m.
„Harn‘';            av. maezaiti           „harnt,    diingfc^,    maVsnia-,    maesmaii- „Harn“;          arm.
(Hubschmann Arm. St. I 43, Arm. Gr. I 474) mizcm „harne“, mez „Harn‘';
gr. ojiier/tiv ,,harnen'^, oyer/ua „Harn“ (so sind die iiberlieferten Formen
oyr/eivy dylyya nach Solmsen IF. 31, 467 zu interpretieren) dyi^ai' ovofjoat
Hes. (d-, d- sind wohl Yokalvorschlag, kaum Praep., etwa „anpissen*‘; einen
idg. Wzansatz '^omeigh-, Hirt Abl. 121, vermbgen die gr. Formen nieht zu
tragen), yor/ogy yoiydg, -adog „Ehebrecher(in)“ (die                                 Beschrankung des Ge-
brauchs auf den Fall des Eingriffs in die Rechte des Gatten, die Wackernagel
Hellenistica, Gottingen 1907, 7 Anm. 2 hervorhebt, wird aus irgendeinem
Trivialgebrauch, allenfalls z. B. vom Yergleich mit dem Hunde, stammen):
   lat. mingo, -ere^ mhixi, miclnm und atinctum ,,harnen'^, meioy -ere ds.

(^nteigh-lo\ s. Solmsen KZ. 39, 21S m. Lit,, IF. 31, 467); 2i\s\. mlga, ags.
migany mnd. mlgen ,,harnen'^ ags. micgay Nticge, migod „IIarn'', got. maihstus.
246                                             meigh-, meiq-


ahd. mist                        meox ,Kot, Diinger'^, ags. engl, mixen „Mist-
                           ags, miox,                5


haufe'^ as. mehs n.              mnd. mes, afries. mese ds. (anders Kern IF. 4,
lllf.);      wahrscheinlich hieher die Bez. der nur durch den Mist der Vogel
verpflanzten Mistel,                  mistil,    Sig^.misiel,        aisl.               (Fick IIl^ 320,
Falk-Torp u. Mistel);
  lit. rnlzii (Keubildung fur                              m{szH „harnen% m[zalal. {jnyzalaT) PI,
„Harn“, mlfnis „einer, der piBt“,                  lett,     mejmi und                   Prat, mifii. Inf.
mift „harnen'^ (aber lit. meziit^ mezti „den Diinger bearbeiten*' ist nach
Leskien Abl. 279 vielmehr meziu                  =
                                     lett. mejchii,   mvft; liegt ein dehn-
stufiges Wznomen *ine[i]?jh zugrunde?);
     skr. rniz-uin^       -afi   „harnen“   (i    aus dexn Praes. "^mis-jq yerallgemeinert,
Solmsen KZ. 39, 218 Anm.);
      sloven, mdzi^ m9seti „hervordringen                    (von Flussigkeiten)“, nidzina „Moor-
grund'‘.
  Hieher (Berneker II 54) auch slav. mezga {^moigzghu aus "^nio/gh-sqay
,,Baumsaft“ C^„hervortr6pfelnd“) in skr. mezga, cech, mkha, nnza usw und                            ,


(mit aufgefrischter Tenuis des Formans) mhd. meiscJi „Maische^^, mnd, meisch,
mesch „ungegorener Malzsaft, Maische"' ags. mcesc-^ max-ivyrt „Maischwurze‘‘,
engl. mash „zerquetschen‘'' (untereinander verb, v. J. Schmidt KZ. 25, 129>
Koreen Ltl. 139, Weigand-Hirt u. 3Iaisclie),
  Letztere Gruppe nicht nach Koreen aaO., Falk-Torp u. mask, Sverdrup
IF. 35, 152 zu meilz- „mischen'*'; blo6 das germ. Wort zu mischen zu stellen,
geht kaum an, zumal begrifflich ein Ubergang von „Baum8aft zum Garen'^^
zu „gahrende  oder zu gahrende anderer Saft‘^ durchaus einwandfrei ist.
Dagegen        die unter meik- ,,mischen‘‘ genannten Worter fiir „Molkem
                 sind
Quark*‘ kaum hieher zu beziehen
  S. Curtins 194 f. und bes. Kern IF. 4, 106f. (hier Scheidung von meigh-
„flimmern; dunkel, Wolke‘'), Solmsen aaO.


 meigh-, auch meiq- „flimmern, blinzeln; dunkel (vor den Augen flimmernd);
```


## [2026-09-07T16:13:53.552Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '16150,16230p' WLD_Bd2_pages.txt"
}
```


### [2026-09-07T16:13:53.607Z] TOOL RESULT

```
 meigh-, auch meiq- „flimmern, blinzeln; dunkel (vor den Augen flimmernd);
     Nebel, Wolke“: vgl. denselben Bedeutungsumfang bei {mer-)^ mer{9 )q-^


      A. mit der Bed. „flimmern, blinzeln, micare“:
      Wzt mcigJi-:          lit.   -mingu^ -augii          (z.   B. mit id-) ,,einschlafen'', citmigas
.,NachschIaf“, m'egmi (3. sg. mekti)        und megu^ -oti „schlafen“, megas „Schlaf‘v
                 .,Schlafbank‘', lett. megs „Schlaf', miga „Lager eines Tieres“, apr-
mciigtin a. sg. „Schlaf*,           enmiggtms „eingeschlafen“,                  iSinige „entschlief’:
      abg.   )h'bg72qt%   Uthzaii „blinzeln“,            russ. mldih^ mzH'b       „schlummern“, migdi^y
,,   blinzeln,         abg. pomidza-jq, -ti „mit den Augen winken^', skr.
                  winken“,
rntg-am, -aii „blinzeln“, cech. mihati „blinzeln, winken"-, -se „8ich schnell
hin und her bewegen“ (wie lat.              russ. mig „Augenblick‘% skr. nug^
 cech. mih ,,Augenblick,             Wink“        s.     ksl. 7n^glil^       „blinzelnd“ (nicht „beweg-
lich‘*, s.Leskien IF. 19, 204) abg.                         po-mez’di (pci) „die Augen schlie6en“
 (usw., s. Berneker II 56 f.);
   rand, micketi {-kk- = gkn-^ vgl. slav. mhgnq) „das Auge worauf rich ten
                                                                              ^
 beach ten“ (*,,hinblinzeln“), mnl. mickcn „ds. beabsichtigen“, awfries. mifzo-
 ,.beachten“.
                                   meit-, meit(h)-   — meit hj-                            247


   Wzf. meiq-: osorb. mihac .jblinzeln, blinken'^, mih j,Augenblick“; lat. mico,
-are „schimmern: sich zuckend oder zitternd bin und her bewegen, zappeln
(z.   B. digitis);     baluci micac^    npers. rniia     (pehl.   ^micah) „Augenwimper‘^
(Liden ]P. 19, 333 f.,  wo auch gegen andere Deutungen Yon       mkare).

      B. mit der Bed. „dunkel vor den Augen werden, Nebel, Wolke^^
      Ai. meghd- m. „Wolke‘',        mih „]S[ebel, Dunst, wasseriger       Niederschlag'*,
av. maeya- „WoIke'"; arm. meg (Hiibschmann Arm.-Gr. I 474) „Neber'; gr.
ofjLiyXrj (atfc. Sgtykrj)  „Wolke, IfebePS bom. djuix^aXoEOoav „nebelig, Bei-
wort von Lemnos^ (Vokalvorschlag wie bei den gr. Yertretern von meigh-
„harnen“; an ein Praef. d- als „B^’ii®belung‘‘ ist wohl nicht zu denken):
    ndl. miggden „staubregnen‘‘ (aisl. mistr j,trubes Wetter^ usw. vielleicht
zur verw. Wz. mei-s-^ oder als                hieher);
    lit. migid, 7nygJd „^7ebek‘, lett, migla^ ds. (— djuLt'/Xr}    ob auch ndl. mig-
                                                                      ;


gelen auf ders. Gdf. beruht, mit Kons.-Dehnung vor              ist unsicherer) abg.   ;



rmgld                 russ. mga „Staubregen, Schneegestober, kalter feuchter
Nebek', eecb. mha „Nebel“, russ.           „staubregnen, nebeln“ usw.
  Alb, mjegtiJe „I7ebel“ steht aber fiir und nehen mjerguh, s. u. mer-, mer{d)g-.
  Ygl. Kern IF. 4, 106f. (unter richtiger Trennung von meigh- „harnen“,
sowie unter Zsfassung der Gnippen               A
                                           und B, wie auch Berneker II 56 f.),
Uhlenbeck PBrB. 26, 303 f. (aber ai. mccaka- „dunkelblau, dunkelfarbig“
und dt. Moive von einem versch. moig^o- „graublau^‘)? Biden IF. 19, 333 f.,
van Wijk IF. 28, 124f., Wood KZ. 45, 70. Ygl. noch meis- „flimmern“.

1. lueit- „fett,       masten“??     meit(h)- ,.Aufenthalts(ort)'', woraus     bait,       auch
            .jLebensunterhalt, Nahrung^’.
      Ir.    medh „fett^‘
                      lit. ininiii,
                            ;       mitau^ nusfi „sich nahren“, niitas „Lebens-
unterhalt^', maU'mti ,,nahren“, maistas .^Nahrung'', auch lit. maitd „Aas“
(das nicht besser nach Wiedemann BB. 28, 42 zu lett. aimetet „erweichen“,
Wz. mel- .,mild‘';, apr. maita „nahrt'', )naitatimsm „sich nahren*‘. Zupitza
BB. 25, 99, Trautmann Apr. 374.
   Beziehung zu ai. mayas „Labsal“ usw. (s. niei- „mild‘'j ist von Wiede-
mann aaO. nicht wahrscheinlich gemacht worden.
   Der Yergleich der bait. YTorter mit dem irischen wird aber schwer ge-
fahrdet durch die von erstern kaum losreiBbaren lett. mitmat „unterhalten,
Aufenrhalt geben‘^, miiu^             mist „wohnen, sich aufhalten, seine Kah-
rung wo haben'*; denn dafi bier „Aufenthalt“ nicht (etwa uber ,,Putter-
stelle, Futterstation^) aus „Kahrung'' entwickelt, sondern der umgekehrte
 Bedeutungswandel anzunehmen ist, lehren av. mat^ana- n. „Aufenthalts-
 ort fiir Menschen und Gutter, Wohnung, Haus“, mi'&naiti „weilt, wohnt,
 bleibt^* mnd abg. m '"sfo „Ort'% wenn es trotz der mit lit. aumias in Wider-
 spruch stehenden Intonation von skr. mjesto, cech. misto hierhergehoren
 sollte; doch s. Berneker II 51 f.j.


 2,    ineit(h)- ,,wechseln, tauschen^^
                   mthati „wechselt ab, zankt. gesellt sich zu“, loiihas Adv.
       Ai. ^nethat'K
```


## [2026-09-07T16:14:07.656Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T16:14:07.664Z] TOOL RESULT

```


```


## [2026-09-07T16:14:11.755Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Indo-Iranian, Avestan, Latin, Germanic, Persian) verbatim as far as possible."
}
```


## [2026-09-07T16:14:12.889Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meyǵʰ-",
 "prompt": "Give the reconstruction, meaning, notes on whether 'to urinate' and 'mist/cloud' are the same root, and the descendants (Avestan, Sanskrit, Latin, Greek, Germanic, Iranian)."
}
```


### [2026-09-07T16:14:18.487Z] TOOL RESULT

```
# Proto-Indo-European *meyḱ- Root

**Reconstruction:** *meyḱ-* or *meyǵ-*

**Meaning:** "to mix"

**Key Descendants:**

**Indo-Iranian:**
- Sanskrit: मेक्षयति (mekṣáyati, "to mix")
- Proto-Iranian: *máyxšati*

**Avestan:**
- Younger Avestan: 𐬨𐬌𐬱𐬙𐬌 (mišti, "confusedly")

**Persian:**
- آمیختن (âmixtan, "to mix")
- آمیغ (âmeġ, "mixture")

**Other Notable Descendants:**
- Ancient Greek: μίγνυμι (mī́gnūmĭ)
- Lithuanian: miēši ("dilute, mix, ferment, sweeten")
- Ossetian: месин (mesin, "buttermilk")

The entry notes this root possibly derives from *mey-* meaning "to change" and tracks numerous inflectional formations across Indo-European language families.
```


### [2026-09-07T16:14:20.202Z] TOOL RESULT

```
# Proto-Indo-European Root *h₃meyǵʰ-

## Reconstruction & Meaning
The root **\*h₃meyǵʰ-** means "to urinate." It's a reconstructed Proto-Indo-European term attested through comparative linguistic evidence rather than direct historical records.

## Related Root Query
The page notes "A connection to *h₃meygʰ- (mist, cloud, condensation)" is conceivable, though morphological details remain uncertain. These appear to be distinct roots with different semantic fields—one relating to bodily functions, the other to atmospheric phenomena.

## Key Descendants

**Avestan & Sanskrit:** The root yields Proto-Indo-Iranian *Hmáyjah, appearing in Avestan as maēza and Sanskrit मेह (méha, "urine").

**Latin:** Descendants include mēiō and mingō, derived through different morphological formations (ye-present and nasal-infix variants).

**Greek:** A doubtful connection exists to Ancient Greek μοιχός (moikhós, "adulterer"), though this association remains uncertain.

**Germanic:** Proto-Germanic *miggо̄ną and related forms yield Dutch miggelen, possibly connected to the "drizzle" sense rather than urination.

**Iranian:** Middle Persian myc (mēz-) and Persian میزیدن (mêzidan) continue the root, as do Northern Kurdish forms like mîz and mîstin.
```


## [2026-09-07T16:14:25.702Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-",
 "prompt": "Give the reconstruction, meaning, and the descendants (Avestan, Sanskrit, Iranian/Persian, Greek, Germanic including Old English mist, Balto-Slavic)."
}
```


## [2026-09-07T16:14:26.998Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%BA",
 "prompt": "Persian میغ: give the full etymology (Middle Persian, Avestan, Proto-Iranian, PIE), meaning, and any cited sources."
}
```


### [2026-09-07T16:14:31.211Z] TOOL RESULT

```
# Proto-Indo-European Root: *h₃meygʰ-

## Reconstruction
**\*h₃meygʰ-**

## Meanings
1. "fog, mist, cloud"
2. "to drizzle"

## Key Descendants

**Proto-Indo-Iranian:** "*Hmaygʰás" (with further descendants listed)

**Proto-Indo-Iranian:** "*Hmíčš ~ *Hmiǰʰás"

**Proto-Germanic:** "*mihstaz" and "*mihsą" (relating to dung)

**Balto-Slavic:** Lithuanian "miegoti" (sleep) and "miegas" (sleep); Proto-Slavic "*měžiti" (close one's eyes) and "*migati" (blink)

**Old Armenian:** "մէգ" (mēg)

**Germanic:** The page notes a potential connection to Old English "mist" through Proto-West Germanic "*migglen" and related forms.

The entry indicates these terms are "hypothesized to have existed based on comparative evidence" rather than directly attested historical records.
```


### [2026-09-07T16:14:33.002Z] TOOL RESULT

```
# Etymology of Persian میغ (mēġ)

**Meanings:** Cloud (archaic/poetic) and fog/mist

**Etymology Chain:**

The word traces back through multiple language stages:

- **Middle Persian:** From *myγ* (mēγ, "cloud, mist")
- **Parthian:** The Middle Persian form derived from this language
- **Proto-Iranian:** *Hmaygáh*, with comparisons to Manichaean Parthian *myg* and Avestan *maēγa-* ("cloud")
- **Proto-Indo-Iranian:** *Hmaygʰás*, comparable to Sanskrit *मेघ* (megha, "cloud")
- **Proto-Indo-European:** *h₃meygʰ-* ("cloud, mist, fog")

**Cognates:** The word relates to Persian *مه* (meh), Northern Kurdish *mij*, and Hindi *मेघ* (megh).

**Sources:** The Wiktionary entry cites these etymological connections with reconstructed proto-language forms, though no external scholarly sources are explicitly referenced in the provided content. The entry notes the Urdu term was "borrowed from Classical Persian" and represents a "doublet" of the Urdu form *مینہ* (mẽh).
```


## [2026-09-07T16:14:38.522Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DA%98%D9%87",
 "prompt": "Persian مژه (može): full etymology chain (Middle Persian, Proto-Iranian, PIE root), meaning, cognates, and any sources cited. Also mention مژگان if present."
}
```


## [2026-09-07T16:14:40.189Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%DB%8C%D8%AE%D8%AA%D9%86",
 "prompt": "Persian آمیختن: full etymology (Middle Persian, Proto-Iranian, PIE), meaning, and cognates. Also anything about گمیختن."
}
```


### [2026-09-07T16:14:44.683Z] TOOL RESULT

```
# Etymology of Persian مژه (može)

**Meaning:** Eyelash

**Etymology Chain:**
The word traces back through several proto-languages:
- **Proto-Indo-European:** *meyg⁽ʷ⁾ʰ- ("to blink, cover (the eyes)")
- **Proto-Indo-Iranian:** *mayš- ("to blink, wink")
- **Proto-Iranian:** *maiĵ- ("to blink, wink")
- **Persian:** مژه (može)

An alternative etymology proposes derivation from "موی" (muy, "hair") + a diminutive suffix.

**Cognates:**
The entry identifies related words across Indo-European languages:
- Sanskrit: मिष् (miṣ, "to wink")
- Lithuanian: miẽgas ("sleep")
- Proto-Slavic: *měžiti ("to close one's eyes")

**Related Languages:**
Cognate forms appear in Sogdian (miža, muža) and Mazanderani (میجیک, mijik).

**Descendants:**
The term influenced multiple Turkic languages, including Azerbaijani müjə and Uzbek derivatives (mijja, mujgon).
```


### [2026-09-07T16:14:46.928Z] TOOL RESULT

```
# آمیختن (Āmēxtan) - Persian Verb

## Etymology
The word derives from **Middle Persian** *ʾmyhtn* (āmēxtan), ultimately tracing back to **Proto-Indo-European** *\*meyḱ-*, the same root that produced the English word "mix."

## Meaning
This transitive verb means "to mix" or "to mingle." An intransitive usage also exists, meaning "to be intermixed." The synonym in Persian is **مخلوط کردن** (maxlut kardan).

## Key Linguistic Details

**Pronunciation varies by dialect:**
- Classical Persian: /ʔaː.meːx.ˈtan/
- Iranian Persian: \[ʔɒː.miːx.t̪ʰǽn\]
- Tajik: \[ʔɔ.meχ.t̪ʰán\]

**Present stem:** آمیز (āmēz/âmiz)  
**Past stem:** آمیخت (âmixt)

## Historical Usage
The word appears in classical Persian poetry, such as in Mahsatī's work (c. 1100), where it describes the violet mingling perfumes with earth.

**Note:** The page does not contain information about گمیختن (gamixtan), which appears to be a related but separate Persian verb.
```


## [2026-09-07T16:14:53.064Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mist",
 "prompt": "Give the full etymology of \"mist\" including Proto-Germanic form and PIE root."
}
```


## [2026-09-07T16:14:53.801Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mix",
 "prompt": "Give the full etymology of \"mix\" including Latin miscere and the PIE root; also mention miscellaneous if present."
}
```


### [2026-09-07T16:14:59.444Z] TOOL RESULT

```
# Etymology of "Mist"

The word "mist" originates from Old English *mist*, with roots extending back through Germanic and Indo-European languages.

**Proto-Germanic:** The term derives from Proto-Germanic *\*mikhstaz*, which also appears in Middle Low German *mist*, Dutch *mist*, Icelandic *mistur*, and Norwegian and Swedish *mist*.

**PIE Root:** The Proto-Germanic form "perhaps" traces to the Proto-Indo-European root *\*meigh-*, meaning "to urinate." Related forms appear across Indo-European languages, including Greek *omikhle* ("fog"), Old Church Slavonic *migla* ("fog"), and Sanskrit *mih-* ("fog, mist") and *megha* ("cloud").

**Semantic Development:** Originally describing "a cloud resting upon the ground, fog," the term expanded to include "precipitation consisting of fine droplets." By the 15th century, it acquired figurative senses relating to dimness and obscurity, both literal and metaphorical. The meaning "haze of dust in the air producing obscurity" emerged by 1785.

The uncertain PIE connection reflects linguistic debate—some scholars propose these cognates represent a "separate IE root meaning 'fog'" rather than deriving from the "to urinate" root.
```


### [2026-09-07T16:15:00.394Z] TOOL RESULT

```
# Etymology of "Mix"

The word "mix" traces back through several linguistic layers. The verb form emerged in the 1530s as "a back-formation from Middle English _myxte_" (early 15c.), which came from Anglo-French and ultimately Latin.

## Latin and PIE Roots

The Latin foundation is _miscere_, meaning "to mix, mingle, blend; fraternize with; throw into confusion." This derives from the Proto-Indo-European root **\*meik-**, which simply means "to mix."

## Historical Development

Interestingly, the word was relatively rare before Elizabethan times, possibly because it risked confusion with unrelated Middle English words like _mixen_ (dung-hill) and _mixed_ (foul, filthy), which stemmed from a different PIE root (\*meigh- "to urinate").

The noun form appeared later, around 1580s, as "act or result of mixing," eventually broadening to mean "a mixture" by 1882 and "ingredients mixed together and sold ready for cooking" by 1938.

## Note on "Miscellaneous"

The provided source does not include information about "miscellaneous," so I cannot comment on its etymological connection based on the material given.
```


## [2026-09-07T16:15:08.984Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[220+21][:1800])\nEOF\necho \"=== CHEUNG maiz / maik ===\"; grep -n -e \"\\*maiz\" -e \"\\*maik\" -e \"\\*mai\" CHEUNG.txt | head -20"
}
```


### [2026-09-07T16:15:11.458Z] TOOL RESULT

```
— 220 —
kurd. miMnk, mizl, mujüal (H.-Sch.) ^Augenwimpern';
bei. micäc, n. misäs ^Augenwimpern*, daneben LW.
mizayän (236).
ai. nimis' 'Blinzeln, Zwinkern des Auges*, skr. nMsa-,
das Bartholomae ZDMG. 44, 553 vergleicht, stimmt
lautlich nicht zu np. kurd. i, g. /, bei. c (für letzteres
erscheint im nb. regulär s, vergl. Geiger, Dialekt-
spaltung, 83).
981. ^nest 'betrunken* 0-
aw. vergl. mada- 'Kausch trank* ; phlv. mast (PV.);
ai. mattd- 'trunken', vergl. |/"fwad-, mddati 'froh sein,
sich berauschen'.
Allgemein entlehnt; oss. d. mast, t. mäsf 'Galle,
Zorn' (181) ist wegen des Bedeutungswechsels un-
sicher.
982. ^nust 'Faust*.
mäz. mis (*nitist).
aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
(18) Gl.) 2), mtistih (AV.), must (PPGl.); ai. musti-,
kurd. mist, miste/c; af/. mmt^ müt; bei. LW. mtist
(172) ; wa;k'. mösty sar. mut
983. tniiSten 'reiben*.
aw. [/^marz-j marezaiti *fegen'; phlv. mmt^ mmt
(vd. 4 (7) (26) für aw. marsta-); ai. l/'mar/-, mdrsfi
'abwischen'.
kurd. mistin 'fegen'; af/. mu/al; bei. musag, n. musay
'reiben*, kratzen, streichen, salben, mahlen' (244).
Eine Doublette zu np. maltden (No. 962).
984. muy, möy 'Magier, Feueranbeter*^), möbed,
ap. magu-; aw. -moyu- in moyu.fbis-? (vergl. Geldner,
*) Irgendjemand hat, wie mir Herr Prof. Nöldeke sagt, irgendwo
(die SteUe war augenblicklich nicht aufzufinden) das als arabisch geltende
medhüs 'sinnlos* für ein persisches Wort (|/ mad' + hös 'Verstand, 8inn*J
erklärt. Ich denke aber, dann könnte es nur mesthös lauten.
') Ganz falsch war natürlich meine Bemerkung ZDMG. 48, 36
Note 34.
') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
und besonders zum 'Kneipwirt, Zecher* geworden (H ä f i ? häufig), vergl.
auch muybece^ muyän u. a. m.
=== CHEUNG maiz / maik ===
10979:‘daughter-in-law’ (< *snusa-), "mh ‘ewe’ (< *maisi-). = Samadi: 110 
11562:*NEIR: ? Oss. I. min-as, D. mijn-as& ‘feast, reception’ (*mai@na- ‘(guest)dwelling’), 
11951:*gausa-), mi, meh ‘ewe’ (< *mais?), on which see for instance, Cabolov 1997: 51. 
12229:which this root has been abstracted may be interpreted differently: cf. *maij” ‘to 
17010:*maié (mac) ? 257 
17042:© Sokolova 1973: 23, postulates the existence of an Iranian root *mai/mi ‘to be’ (the 
17056:*maié (*ma£) ? ‘to suck’ 
17070:258 *maiH 
17093:*maiH ‘to harm, damage, fade, decrease (?)’ 
17128:*maij! ‘to blink, wink’ 
17133:*maißHl 259 
17150:Ó The Ir. formation *maig'á- ‘(dark) cloud’ (< *‘which covers (the eyes)’), Skt. 
17162:*maif^ (Hmaij) ‘to move (to places)’ 
17176:9 An Ir. root *maij ‘to move to (places)’, which corresponds to Skt. niméghamana-, 
17188:*mai0H! ‘to dwell’ 
17192:Pres. пӣ-: IND. 35р. YAv. mi0naiti (Yt 10.39 ff., V3.20), ? YAv. paiti miOnaiti (< *mai0H ?, У 3.20); 
17202:260 *mai0H2 
17208:( *mai0na- ‘(host-) dwelling’), ? Pash. mést ‘settled, residing’ 
17221:*mai0H? ‘to change (position), deviate, tauschen, täuschen (?)* 
17254:*maidH’ ‘to throw, discard, mittere’
```


## [2026-09-07T16:15:14.976Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17128,17185p' CHEUNG.txt; echo \"=== maiz urinate ===\"; grep -n -e \"to urinate\" -e \"urine\" CHEUNG.txt | head -20"
}
```


### [2026-09-07T16:15:15.058Z] TOOL RESULT

```
*maij! ‘to blink, wink’ 
*MIDDLE PERSIAN: ВМР mycsn /mézisn/ ‘blinking, winking’, myc(k) /mij(ag)/ 
‘eyelid, eyelash’ 


*maißHl 259 


*KHOTANESE: (+ *ni-) OKh. nämäs- ‘to wink’ > SGS: 55 

*SOGDIAN: (+ *ni-) BSogd. nymz- ‘to blink’, ? CSogd. nmzy’ ‘wink, blink’ 

Partic.: pres. nymz’y ‘blinking’ (Vim. 201) 

*NWIR: NP muže, meZe ‘eyelash’ 

*NEIR: (+ *ni-) Yi. nomíZ ‘winking’, nemig-/nemosk' (Zarubin), Ishk. nu-mul- ‘to 
shut one’s eye’ (Zarubin) 

*SANSKRIT: ? mes ‘to open the eyes’ (RV+), mil ‘to close the eyes’ (contaminated ?) 
c» EWAia П: 379 

Ó The Ir. formation *maig'á- ‘(dark) cloud’ (< *‘which covers (the eyes)’), Skt. 
meghá-, Y Av. maéya-, etc., may also contain this root, on which see Cheung, Fs 
Klingenschmitt. 

«PIE *mei-g/""- ‘to blink, cover (the eyes)’ = LIV: 427 | Pok.: 712 f., 714 

*IE COGNATES: OCS po-méZiti (oct) ‘to close (the eyes)’, Lith. miegü (miegöti) ‘I 
sleep’, Lith. miégas ‘sleep’ 

*REFERENCES: IIFL II: 232b, 404b; DKS: 184a f.; Werba 1997: 361 f. 


*maif^ (Hmaij) ‘to move (to places)’ 

*CHORESMIAN: ’m’xy- (caus.) ‘to move, shake (something)! = Samadi: 110 

*NWIR: ? Gil. (Rsht.) va-moeytoen/va-meej- ‘to seek’ 

*NEIR: Yzgh. mex"-/max"t ‘to move, shake’, max“ an- (caus.), Yi. müZ-/muyd- ‘to 
move [intr.], to be swung’ || (+ *ni-) Yzgh. namoxs-/namoxt ‘to go out’, Yzgh. 
namoacé-/namast (caus.) ‘to take out, drive away’ 

*MISC: ? Par. muz-, muš- ‘to go’ (LW ?) 

*SANSKRIT: Skt. niméghamana- ‘moving down’ (RV) = EWAia П: 381 

9 An Ir. root *maij ‘to move to (places)’, which corresponds to Skt. niméghamana-, 
may be postulated on the basis of the evidence above. On the possible IE etymology, 
see further Cheung, Fs Klingenschmitt. 

«PIE *meig"- ‘to move, go (to places)” > LIV: – | Pok.: 

*IE COGNATES: Lat. migrare ‘to move (from place to place), change residence or 
position? 

*REFERENCES: Christensen, Contributions I: 61; IFL I: 274b; UEL П: 230a; Cheung, Fs Klingenschmitt 
=== maiz urinate ===
3663:*NWIR: NP 335 ‘urine, pee’, Qohr. sasid/sas- ‘to urinate’ || (+ *a-) Tt. (Esh.) 4si/ 
8853:*NWIR: ? NP saridan/sar- ‘to flow as rivers, with a great noise; to pour, trickle, urine’ 
9047:(ritually with water or cow’s urine)’ || (+ *para-) ‘to pour, flow out, away’ || (+ *fra-) 
9935:drip; flow (of urine)’, hl’wy- (caus.) ‘to let it drip, drop’ = Samadi: 173, 168, 47, 
12224:© According to Mayrhofer, EWAia, Le IE *Hsmeié - ‘to urinate’ (> Ir. *Hmaiz) 
12244:*Hmaiz ‘to urinate’ 
12247:*AVESTAN: Y Av. maez- ‘to urinate’ || (+ *fra-) ‘to pee forward, forth’ — Liste: 45 
12252:*MIDDLE PERSIAN: ВМР myc- /mez-/ ‘to urinate’ || (+ *ni-) MMP nmyzysn ‘incite- 
12260:*KHOTANESE: miysai ‘urine’ 
12262:*CHORESMIAN: myz- ‘to urinate, piss’ = Samadi: 113 f. 
12265:dimistan/dimiz- ‘to urinate’, Ard. mis/mes-, Gz. méz-/més, miss (tr.), Khuns. miz-/ 
12267:Sorkh. demestan/demiz- ‘to defecate’, Zaz. mizi (f.) ‘urine’ || (+ *ui-) NP gimizidan/ 
12268:gimiz- ‘to make water’, NP gimiz, (LW ?) Awrom. guméz (m.) ‘urine’ 
12270:*NEIR: Oss. I. mizyn/myzt, D. mezun/mizt ‘to flow; to urinate’, Pash. mitol/mez-, Sh. 
12272:Yi. miz-/mizd- ‘to urinate’, Oss. I. mizg&, D. mezgz ‘urethra’, Sariq. meyz, Wa. 
12273:mizg ‘urine’. Ф The meanings assigned by Abaev, l.c. ("течь, протекать, fluere") to 
12275:Dictionary cites, next to ‘to urinate’ ("мочиться"), the second meaning ‘to seep 
12278:*MISC: Par. miz, Orm. mizi ‘urine’ 
12280:*SANSKRIT: meh ‘to urinate’ (RV+) © EWAia II: 381 
12282:«PIE *H;meig"- ‘to urinate’ => LIV: 301 f. | Pok.: 713
```


## [2026-09-07T16:15:30.412Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12230,12290p' CHEUNG.txt; echo \"=== Cheung mix ===\"; grep -n -e \"to mix\" CHEUNG.txt | head -20"
}
```


### [2026-09-07T16:15:30.471Z] TOOL RESULT

```
move’. The Iranian forms might reflect the denominative usage of the well-attested 
PIE ‘cloud’ form: *H;mig"- ‘cloud’ ? Alternatively, the forms might point to the 
existence of an old PIE verbal root *Hsmeig"- ‘to pour out, nebulize’ (?), cf. Ger- 
shevitch 1974: 89 ff. No further support in IE for such a root can be cited though. 
«PIE *H3mig - ‘cloud’ => LIV: — | Pok.: 712 

*IE COGNATES: Gr. оріҳАт (Ё) ‘nebula’, etc. 

*REFERENCES: MacKenzie 1966: 102; Shahbakhsh: s.v. miss- 


*Hmard 179 


*Hmaiz ‘to urinate’ 


*AVESTAN: Y Av. maez- ‘to urinate’ || (+ *fra-) ‘to pee forward, forth’ — Liste: 45 
Pres. them.: IND. 3sg. YAv. framaézaiti (V 18.40), 3pl. YAv. maézonti (V 3.6), OPT. med. 3pl. YAv. 
maezaiianta (V 8.13); Partic.: pres. YAv. maezant- (N 37) 


*MIDDLE PERSIAN: ВМР myc- /mez-/ ‘to urinate’ || (+ *ni-) MMP nmyzysn ‘incite- 


ment, provocation, urging’ > DMMPP: 244a 
Pres.: IND. 3sg. BMP mycyt /mézéd/; Partic.: perf. pass. BMP myst /mist/ 


*PARTHIAN: (+ *ni-) nmyzysn ‘incitement, provocation, urging? > DMMPP: 244a 
*KHOTANESE: miysai ‘urine’ 

*CHORESMIAN: myz- ‘to urinate, piss’ = Samadi: 113 f. 

*NWIR: NP méxtan/méz-, Bal. mest, mezit/meZ-, méz-, Kurd. mistin/miz-, Gil. 
dimistan/dimiz- ‘to urinate’, Ard. mis/mes-, Gz. méz-/més, miss (tr.), Khuns. miz-/ 
mizä, mis(s)-, Lasg. demeston/demiz-, Nn. més/méz-, Semn. demestiyon/damiz-, 
Sorkh. demestan/demiz- ‘to defecate’, Zaz. mizi (f.) ‘urine’ || (+ *ui-) NP gimizidan/ 
gimiz- ‘to make water’, NP gimiz, (LW ?) Awrom. guméz (m.) ‘urine’ 

*NEIR: Oss. I. mizyn/myzt, D. mezun/mizt ‘to flow; to urinate’, Pash. mitol/mez-, Sh. 
mez-/mixt, Rosh. miz-/mixt, Sariq. meyz-/maxt, Yzgh. miz-/maxt, M. méz-/mizd, 
Yi. miz-/mizd- ‘to urinate’, Oss. I. mizg&, D. mezgz ‘urethra’, Sariq. meyz, Wa. 
mizg ‘urine’. Ф The meanings assigned by Abaev, l.c. ("течь, протекать, fluere") to 
Oss. I. mizyn, etc., are perhaps a bit inaccurate. The standard Ossetic-Russian 
Dictionary cites, next to ‘to urinate’ ("мочиться"), the second meaning ‘to seep 
through, percolate’ ("просачиваться"). 

*MISC: Par. miz, Orm. mizi ‘urine’ 

*SANSKRIT: meh ‘to urinate’ (RV+) © EWAia II: 381 

«PIE *H;meig"- ‘to urinate’ => LIV: 301 f. | Pok.: 713 

*IE COGNATES: Gr. ópeíxo, Lat. meiö/mingö ‘I urinate’, OE migan, Lith. myZti, 
SCr. miZati ‘to urinate’ 

*REFERENCES: KPF I: 140b f.; EVP: 48; IIFL I: 274b, 401b; IIFL II: 230a; MacKenzie 1966: 95; Abaev, 
Slovar’ II: 126 f., 125; EVS: 46b; WIM I: 71; WIM II/1: 80; DKS: 332; Werba 1997: 217; Paul 1998: 


=== Cheung mix ===
8038:agistan/agar- ‘to impregnate; to mix; to soil’ (« Elr., perhaps Sogd. ?) 
8040:*NEIR: ? Pash. yen, yon (m.), Yi. уй ‘penis’ || (+ *a-) ? Pash. āyažəl ‘to mix, knead’ 
13978:ways: ‘to encompass’ (Humbach 1991 II: 242), ‘to join (in marriage’, i.e. from *џақН) ‘to mix, mingle’, 
17280:* maiz! ‘to mix, mingle’ 
17282:*MIDDLE PERSIAN: (+ *а-) MMP ’(’)myz-, BMP ’myc- /améz-/ ‘to mix’, MMP 
17283:’C)myxs- (inch.) ‘to be mixed’ || (+ *ui-) BMP gwmyc- /guméz-/ ‘to mix, mingle’, 
17293:*PARTHIAN: (+ *4-) ’myj- ‘to mix’, "myxs- (inch.) ‘to be mixed with’ || (+ *ш-) 
17300:*NWIR: (+ *а-) NP amextan/amez- ‘to mix’, Kurd. (Sor.) am&Zän ‘addition; ligature’ 
17310:*SANSKRIT: meks ‘to mix, to mingle’ (RV+) = EWAia II: 373 
17312:«PIE *meik(-s)-, *meig(-s)- ‘to mix, to mingle’ = LIV: 429 | Pok.: 714 
19442:*SANSKRIT: parc ‘to mix; [sec.] to fill, saturate’ (RV) = EWAia II: 96 
20346:*rai02 ‘to mix, mingle, pervade’ 
20349:below)’ || (+ *pati-) ‘to affect’ || (+ *ham-) ‘to mix together’ = Liste: 58 
20372:*SOGDIAN: (+ *aua- or *ш-) MSogd. wryö- ‘to mix’, CSogd. wyry@’mnt ‘mixing. 
20373:union’ || (+ *a-) BSogd. ’’r’yé ‘to mix’ || (+ *pati-) BSogd. ptr’yö-, CSogd. ptrys- ‘to 
22092:*sarH? “to mix, unite with’ 
22094:*AVESTAN: OAv. sar- ‘to mix, unite with’ — Liste: 61 
22104:*SOGDIAN: (+ *ш-) ? CSogd. wsyr- ‘to mix (?), [Syrian] mzg'. © Cf. Sims-Williams 
22120:«PIE *KerH>- ‘to mix’ © LIV: 328 | Pok.: 582 
23251:*MIDDLE PERSIAN: BMP slš- /sris-/ ‘to mix, knead’
```


## [2026-09-07T16:15:33.637Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17276,17320p' CHEUNG.txt"
}
```


### [2026-09-07T16:15:33.689Z] TOOL RESULT

```
*IE COGNATES: Lat. mittere ‘to throw, release’, Toch. B mit- ‘to go; set out’ 
*REFERENCES: Adams 1999: 461 


* maiz! ‘to mix, mingle’ 

*MIDDLE PERSIAN: (+ *а-) MMP ’(’)myz-, BMP ’myc- /améz-/ ‘to mix’, MMP 
’C)myxs- (inch.) ‘to be mixed’ || (+ *ui-) BMP gwmyc- /guméz-/ ‘to mix, mingle’, 
MMP gwmyxs- (inch.) ‘to be mixed, mingled’ = DMMPP: 41b f. 

(+ *а-) Pres.: IND. 3sg. BMP ’mycyt /amézéd/, 3р1. MMP *’myzynd, IMPV. 250. MMP ’myc /amez/; 
Partic.: perf. pass. MMP ’myxtg, MMP ’(’)myxt, Inf: BMP "myhtn /amextan/; Inch./Pass.: pres. IND. 
3sg. MMP *’myxsyd, 3р1. MMP ’myxsynd, MMP ’’myxsynd || (+ *ui-) Pres.: IND. 3sg. BMP gwmycyt 
/gumézéd/, 3pl. BMP gwmycynd /gumözönd/; Partic.: perf. pass. MMP gwmyxtg, (pl) MMP 
gwmyxtg’’n, MMP “gwmyxtg’n; Inf: BMP gwmyhtn /guméxtan/; Inch.: pres. SUBJ. 3pl. MMP 
gwmyxs’nd 

*PARTHIAN: (+ *4-) ’myj- ‘to mix’, "myxs- (inch.) ‘to be mixed with’ || (+ *ш-) 
wmyxs- (inch.) ‘to be mixed’ = Ghilain: 81, 80 | DMMPP: 41b 

(+ *а-) Pres.: IND. 3sg. "myjyd; Partic.: perf. pass. "myxt, ’myxtg; Inch.: pres. IND. 3sg. ’myxsyd, 3pl. 
"myxsynd; Inf.: *’myxtn || (+ *ui-) Inch.: pres. IND. 35р. wmyxsyd; Partic.: perf. pass. wmyxt, wmyxtg 
*SOGDIAN: (+ *ш-) SSogd. wmxsk PN 

*NWIR: (+ *а-) NP amextan/amez- ‘to mix’, Kurd. (Sor.) am&Zän ‘addition; ligature’ 
*NEIR: (+ *uz-) ? Oss. I. yzmis, D. (@)zme(n)sz ‘sand’ (semantically difficult) 
*MISC: Most Iranian forms apparently derive from the (IE) root variant *meig-. NP 
mihan (mehan ?) ‘fresh butter; sheep's milk’, Oss. I. misyn, D. mesin, Yghn. mesin 
‘buttermilk’, which are assumed to contain this root, are probably unrelated. NP 
mihan might contain the root жтаіӨН? ‘to throw, discard’, to which, considering the 
very close meaning, we have to add the Ossetic and Yghn. forms. The latter form 
probably show contamination with the ‘sheep’ *maisa- formation(s), cf. Av. maesi- 
(f.) ‘ewe’, maesina- ‘sheep-, ovine’. 

*SANSKRIT: meks ‘to mix, to mingle’ (RV+) = EWAia II: 373 

«PIE *meik(-s)-, *meig(-s)- ‘to mix, to mingle’ = LIV: 429 | Pok.: 714 

*IE COGNATES: Gr. (e) yvop, nioyo, Lat. misceo, Olrish mescaim, Lith. miesiü 
(miésti) ‘I mix’, etc. 

*REFERENCES: Abaev, Slovar’ II: 123 Ё; Abaev, Slovar’ IV: 281 Ё; Werba 1997: 393; Cabolov 2001: 77 


*maiz” ? ‘to take care, foster ?’
```


## [2026-09-07T16:15:43.510Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -e \"minas\" -e \"misvan\" -e \"myasait\" -e \"mik-\" BRT.txt | head -20"
}
```


### [2026-09-07T16:15:43.559Z] TOOL RESULT

```
6875:2g.  6,  33.6,  II,  51.  15,  53.  i):  y}  sivim 'rS  mazda  Jiä..  Y.j:^.ii;2Ä'.5;  —  spmtim at  %'wil  mazdä  m}nghl{sA.)  "rä  Y.  43.  5; 2g.  T,  5'.  16;  —  sp>ntS.t?mo  ..  mazdä  °rö Y.45.S;  —  mazda  sai^ärJi^A^  mairisiö.. kvS  vleirsisd.)  'r3'>  V.25.4;  —  hätä-maräm (sd.)  'rä  . .  mazdä  Y.  32.  6 ;  —  yaslqm tu  °rä  irixl»m  mazdä  vagdiitö  ahl  Y._y2. 7;  —  ai  S  (sd.)  vaocat  -rö  mazda  vtdva vq/äf  (sd.)  Y.  25.  6;  —  aiiiyS  mazda  'rS .  .  paiti.mraot  Y.^2.  2;  —  tvSm  mazdä °rä  frS  mä  sTsä  .  .  *vaocaiihi  Y.  28.  11; 4S-  ^  >  —  anhsttl  (sd.)  akya  paourvJm *yqm  mSi  vJdva  (sd.)  mazda  vaocat  'rö '^'■45-V>  —  tat  %w<i  pinsä  (sd.)  »nl mSi  vaocä  'rä  .  ,  azJm  täÜ  "iwä  fraxsnt (sd.)  avämX  masdä  .  .  vupanam  dätJnm \.44~T,  1-4,8-11,  14-18,'^/.  14,  J4- 15;  —  °rä  yaübys  mazdä  "hwöi  vasyäl damä  Y.44.11;  —  sdr  «7  mazdä  'rä vanhsus  /radaxitä  (sd.)  majianhB  Y.jj. 1 7 ;  34-  13;  —  yehya  . .  vakisUm  . .  valdä mazdä  'rff  Y.  51.2a;  31.3;  —  yJ  viHnaot dä%imcä  (sd.)  aää'^?mca  dangrä  mantu aM  mazdä  'rö  Y.  46. 17;  2S.  10;  —  ustä aAmäi  yahmäi  ultä  (sd.)  kakmäicii  *vasS xiayqs  mazda  däyät'rö\. 43.1  •,32.16;  — yS  afimJnT(sd.)  matda  srävT  °rö  Y.  45. 10"*;  —  tä^ä  x/a^rä  mazdä  dqmis  °rS Y.  45.  7 ;  —  voAb  xia%r»m  manaahä mazdä  dadät  'rS  Y.5J.  ai;  31.  zi,  34.  i, 47.  I ;  —  at  mazdä  taibyS  xi'a%r?m  voAli mananhä  *vSivTdaitl  aübyo  sastl{sA.)  °ril.. Y._jo.  8;  46'.  12;  —  at  hsi  mazda  ahüm (sd.)  dadät  'rB  V.^tf'ij;  —  y}  vahyo vat^Asuf  dazdi  ,  .  'rö  xsa'hrä  mazdä  at ahmäi  akäjl  asyS  Y.5/.  6;  —  Aat»Aus(sd.) ; .  .  mazdä  dadät  'rö  . .  yai'öi  vTspäi  ä  Y. 53- Ai  I.  5'-'7>  54- i;  —  aslscä  syao>a-^ nanqm  ..  mazdä  'rahyä  Y.2Ä4;  —  'rahyä urväzsmä  matda  Y._J2.  i; —  'rä  .,  hyal\ *avistä  *hudäbys  mTidfm{&A.)  mazdä  yehyä  ' tu  da'^nm  ^.34- 13;  14, 5 J.  15;  —  mazda  \ x/dira  *vanzT (sd.)  «ä  dyäj  'rö pasüs,,^ frada^äi  ä  Y.45.  9;  —  at  ahyäi  (n'äml.  1 gavöi)  asä  mazdä  urvara  vaxlai  'rö  Y. 4S.  6;  —  C7«  äzötöis  'rö  mq^r>m  lasai . . ' mazda  Y.2(J.  7;  —  ?«;s/  paüö  ya?ia' mazda  'rff  *saittl  ^.33.5;  46.16;  — y^ngstü  mazdä  kad»möi  minas  'rä  Y.  46. , 14; — gätamcä  'räi..t3raohm(^A^  mazdäi ^ Y. 2&5;  —  töi  rwr<7/(sd.)  rädmil  -rahyä- zaosl  mazdä  ^.33.2;   —    yai'ä  xsnaol)H\
10300:hvialia  V.O.33,  /tf.8;  —  hiku  pqsitu  (sd.) °tu  (IS.)  tihayaaa  Y.16.2;  —  nsit  Alm  'tvd (GS.)  vindm  pasvasca  . .  "es  fanden  nicht mehr  Platz  .."  V.2.8;  9.  a)  mit  misvan- Adj,  (sd.,  auch  fdSt.):  misvärum  'tarn  S. 2.^0;  — misvänahe  'tvaie(GS.)^>  S./.30; usw.  2)  sva.  'festbestimmter,  vorge- schriebener, richtiger  Ort  (usw.)';  iva aHahe  nars  'tu^  anhat  ya£  irisis.kasahe ^■,?-^5i  —  y^S  "^'''^  zaota  (sd.)  /r3ya- zititi ..zaotars  "lai-a^  (IS.) .. syae^nöJätfya .  .  paiti.jatfkdit  hävanänö  -taiii'  .  .  N.  Si;
20538:misvan-  11 86
20550:•  j.  misvan-  Adj.  'die  Gemischten  ent-
20613:Vgl.  mp.  hamislak  'gemischt',  np.  ämestan (wozu  Hbm,  PSt.  8).  —  Vgl.  misvan-.  —  Pü. (zu  Y.  46):  vartmS,  (zu  Y.  33):  kila  i  Si  i kam  mal  Citel  an  i  dräy  keia  i  öi  an  i  apilak, dazn  die  Erl.:  hamhlakän.—  ')  S.  zSt  Bthl.
29129:•  g.  ha-.dam-  :  'dm-  m.  'das  selbe  Haus, die  nämliche  Wohnung';  iwävqi..  ■•d>möi (LS.)''  alä  voAucä  sj/qs  maiiaa/ia  "einer wie  du,  der  mit  VAf.  im  selben  Hause wohnt"  V  ■ij,  9'';  —  yJngsta  .  .  'd^mdi'^ minas"  (Sp.  11 90  m.)  Y.46.  14,
```


## [2026-09-07T16:15:46.699Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20538,20620p' BRT.txt"
}
```


### [2026-09-07T16:15:46.773Z] TOOL RESULT

```
misvan-  11 86
gnwmti  '/ar»As{W.)  "M.,  des  lange  Arme die  ergreifen,  welche  . ."  Vtjo.  104.
')  Je  nachdem  das  Wort  aus  miiö.aajaaiä, 2U  'jai-  Adj.,  dnw.  mi%i.ao/;  oder  aus  mi%rao- jaahö,  haplolog.  für  mii,ra-%rao]' ,  zu  'jah-  Adj., dnw.  mRrö.drug;  verderbt  ist.
•  j.  miÖTÖ-drug-  Adj.  'den  Mf^ra  be- lügend, betrügend',  auch  sva.  'den  Vertrag brechend'"':  msrsncaiU  vTspqm  dai^kaom mairyS  'druxs  Yt/o.  a;  19;  —  VtspsAu paiti  barszähu  .  .  spass  änAaire  mikraAe ''  drujim  *AispS.S3mna  Yt.  10. 45;  — pdhS. . yim  wnii  'ärup (SP.)  Yt.  10.4$;  i8,  80;  — aspacilySi  *drujam  vazyqstra  (sd.)  bavaintt Yt.  JO.  20;  —  mihrS  .  .  tiaram  'drujqm apqlgavS  dar)zayeiH  Yt/0.48;  —  mi^rtm .  .yö  nöit  kaAmäi  'drujqm  maiyänqm  aojö da\siti  n5il  zävar»  Yt/O.öz;  62,  23,  26, 37%  38.  73,  133.  J-^- 63;  —  hamistayalca ..  mihrB.zyqmca  *'drujimca  Y.  ö';.  3;*Yt .10.82.
ai,  mUradruh-  Adj.  —  mp.  (Pii.)  taihr  dmi.  — »  Vgl.  SWienAW.  6/-  848.  2,  wo  mihr  drui so  erliulert  wird;  iaul  siiaslan  näm  i  da  (1) zidd  i  mihr  izad  asl^  kaul  biSiAanadi  ähnlich anch  849.  4.
•  j.  iniSrö.zyä-  Adj.  'den  Mi%ra  schädi- gend sva.  deu Vertrag  verletzend':  'zyqm^a *mi>rB.drujimla  Y.  61. 4,  Yt.  10. 82.
Vgl.  zyänäi.  —  pü.;  mihr  ia«. g.  minal  Y.  46.   14:   s.  myas:
•  j,  minav-  f.  'Halsgeschmeide,  -schmuck": 'num  barat  .  .  arfdvi  .  .  upa  tqm  .  . mattao%rim  "ein  Halsgeschmeide  trug  A. ..  am  ..  Hals"  Yt.5. 117.  a)  Du.'* dn.:  /rä  gaola-vara  sispimna  . .  'nuca  (AD.) zarany5.pisi  "..  und  ein  goldgeschmiiclctes Halsgeschmeide"  YL  ij.  10.
KonipE(?).  —  Et.fi).  „  VgL  •manay-,  aber wie  zusammenhängend?  5.  IF.  j,  172.  — O  Weil  aus  zwei  Sti^cken,  für  Vorder-  und Hinterhals,  bestehend;  vgl.  Dbr.  VglS. /.  136. —  =1  SCHEFTELOWnz  ZDMG.  JÄ  167  nimmt m'  als  LW.  aus  dem  Assyrischen.  Nach Bezold,  briefl.  Mitleil.  vom  oS.oä.03,  lässt  sich die  Bedeutung  'Kopfputz'  für  mi-i-nu,  das  nur in  einem  Synonymen  Verzeichnis  belegt  ist, nicht  erweisen.  Im  Übrigen  bes^t  manae%ri- 'Hals',  nicht 'Kopp,  wie  Scheftelowitz  über- setzt.
•  j.  mtmara-  Adj. 'eingedenk,  memor*:  'rB F.  II.
Red.  Bildung.  ~  Zum  V.  'mar-.  —  Pu.-.  Aa- miiat  ösmuttär.
j.  miry',  Verbalf. :  s.  'mar-.
•  j.  misvan-  Adj.  'die  Gemischten  ent-
38
dby  Google
ii87  mi^k-
haltend',  mit^.Jtav-  m.  'Oit  der  Gemischten', Name  des  Zwischenreichs**:  °vänjm  gatüm s^artät^m  5.2. 30;  —  'vänahe^i  gäivake il'ähätahe  S.  /.  30,  V.  jg.  36,  Yt  /.  1  PüZ.
*)  In  dos  Zwischenrcich,  \n.-p.yä%  i  hamist\ai!'^n "Ort  der  Gemischten'  kommen  die,  deren  Cot- ond  Übellaten  bei  der  Abwägung  sich  die  Wage hallen.  Es  befindet  sich  nach  Mi.  7.  iS  mi- lchen der  Erde  and  dem  Siemenprad;  s.  aucb At.  (J.  5  ff.  —  VgL  lor  Sache  unter  »yaj-  und nanä.  femer  Bthl.  ZDMG.  35.  157,  IF.  3.  51, /.  2z6,  10.  II.  wo  «eitere  Litt.;  daiu  noch Mills  G.  487,  Jn.  The  Bibl.  Woild  1896,  155, Jlsti  PrJ,  ,¥f.  238,  SöDERBLOM La lie  fuinre  i»6, BöKLEN  Eschatologie  z6,  56.  Pü.  beiiebt  den Ansdrack  imümlicb  aaf  dos  Schatzhaus  [^on/] dei  überzähligen  guten  Werke;  s.  unten  and Bthi_  AF.  j.  50.
AbleiL  aus  *min/a-  Adj,  'gemischt',  lum  V. myas-;  vgL  ai.  miira-  und  IF,  lO.  11.  —  Pü. : kamcsak  lül  gäh;  s.  NpuErl. :  fl^'ar  h  ri  iarja nabid  at  gcij  •  hamlia  lud  i  ürmizd  livaz  i an   iäi   dikand   (bei   Sp.  Komm.  /.  449).    —
•  j.  misik-  Adj,  (auch  fem.)  —  ?  — '':  asim rSsaintlm  dar^yS.vän^marum  'sacim  Avd.- aiwisilam   'säam    äfrasanhaitim  Y.52.  i.
Sehr  zweifelhaftes  Wort.  —  I'ü. :  pa  hamtsak apiklk.  —  1)  Nach  Pü.  (und  DsT.  ZA.  /  340 : 'perpftuelle  compagne')  ein  Komp.  mit  'hat- als  2.  Glied.     S.  tu  miiti.
•  j.  miäti''  Adv.  i)  '{in  Mischung  sva.) durcheinander':  °ti  zT  mi Alm  ..vatTtttaica snal^intal{^A.)ca  Yt.5.120.  2)  '(inVer-' einigung  sva.)  miteinander':  yat  mht>h>m raoxsne  tapayäti  'li  urvaranqm  zairigaa- nanam  .  .  stmäia  *uzuxlyeiiiti  YL  7. 4.       i
IS.  au*  *müta}'-  f.  'Mischung'  >l,  lam  V.  myas-,
—  VgL  lat.  fHisüi,  misiim.  —  Vü,:  mliaki\ Npü-:  Äamiia,  Sü. :  sadahm, —  ')  Mit  i  Yt.  5-
—  »)  Falsch  Roth  ZDMG.  34-  703,  Pischel VSL  7.  S7.  —  J)  Wohl  Aamflai  zu  lesen  ;   s.
•  j.,  g.  mizda-''  n.  i)  TLohn'  als  das  ver- abredete oder  zugesicherte  oder  gebührende Äquivalent  einer  Leistung  (usw.) :  kaiä  . . tal  'dim  Aan^nl{sd.)  äasä  aspa  arinavattjs (sd.)  ..hyat  m5i ..  aj/hai/r {sd.)  \.44-i&;
—  ahmai  'dim  hanmtl  parShüm  (sd.) mariJ.vistäis  Ißd)  mal  vJspät!  gäva  a«r  Y.  | 46.1g;  —  yas/ai  'dim  Aan?ntl{sA.)  nöit däitl\.44.i')\  —  hanalla  ta  tum  tat  'd?m  ^ yat  zaota  kanayamnd  ätsha  Y.55.30;  F.  11;
—  'dake  a/r^raUi  (ad.)  Vyt.jo.  a)  bes.  I von  dem  Lohn,  der  den  Gläubigen  ver- 1 sprechen  ist:  haurvata  ammtäia  ySi  stü °d)m  asaonam  pard.asti  jas^nlam  "H.  und  , A.,  die  den  Lohn  der  Gerechten  bilden,  1
—  mndräya-  1188
'  wenn  sie  ins  künftige  Leben  kommen" Ylj.  25;  V.p.44;  —  cvat  aßimäi  naire 'dim  aakat  pas'a  astasca  baooattkasca vi.urvistim  "wie  grosser  Lohn  wird  dem Maime  werden  .  ."  V.  Ä  8 1 ;  A.  ^  4,  6;  — —  Ayai  'dim  *mavai'i:3M  (sd.)  /radadä^ä dam^byB  Y. 40.  \;  —  hyat  dairiä  vaMstl yli/^(sd.)  'dt  y.4g.g;  —  ..  iyat  *cfi,i/ts *'hudaby5  'dim  mazdä  yehyä  tu  dähnm I ".  .  zu  dem  Lohn,  der  den  Verständigen versehen  ward,  den  du,o  J/.,  festgesetzt  hastT V,^4.  13; —  hyat  'dim  zarä^ustrS  maga- vabyö  {&A.)  cdisf  para  Y.  5/.  15.  a)  mit Gen.  obj.:  yä  damä  vairJm  hanäi  'dim asahyä  yäsä  (sd.)  aslm  Y.  54. 1 ;  —  aicä vs  'dim  aahat  ahyä  magahyä  .  .ya'irä  . . "und  es  wird  euch  der  Lohn  dieses  Bundes werden . .  dort  wo  . ."  Y,  3^.  7 ;  —  disyät Ai  anAe  avat  'dim  parS.asnai  anuAe ya'ka  . .  "es  soll  ihm  dafUr  ein  so  grosser Lohn  Tür  das  künftige  Leben  zugesichert werden,  als  ob  . ."  A._j.  7,  aa)  zugleich
auch  von  der  den  Ungläubigen  angedrohten Strafe:  s.  Ableit.  2)  'Gewinn,  Vorteil"': miird  . .  yS  nH£  iaAmai  mihr{f.drw/qm  . . :^annS  datiaiti  nött  'dim  Yt  70.62;  Vr. 20. 1 ;  —  zazi  (sd.)  buye  vanhäuca  'de vanAauca  sravaAe  A.i.ii.
KompE.;  Ahleit.  —  El.?]).  —  ai-  i«md-  n. 'Kampfpreis',  np.  mutd  'Lohn'.  -*  Pu. ;  mäd, Sü.;  fras'idah.  —  ■)  In  g.  »,  in  j.  1  ansser  la Y-  59-  —  ')  Vgl-  Yt.  10.  61 :  x'annä  . .  mUdiiK mit  Yt.  10.  lo8:  raeira  ^arrnascä. —  3)  Gegen- über   Johansson    IF.  2.  33   s.   Bgu.    Gidr.>
•  g.  mizda'vant-  Adj.  'mit  dem  (gebühren- den) Lohn  (in  beiderlei  Sinn,  Lohn  tind Strafe)  versehen':  hyat  da  syaokana  'von (APn.)  yäiä  uxiä  akSm  akäi  vanuAlm asim  vanhaov?  "wie  du  den  Taten  ihren Lohn  bestimmtest''  und  den  Worten,  das böse  Los  dem  Bösen,  das  gute  dem  Guten"
Vgl.  milda-  1  aa.    —    Pu.;    kal  däl  ö  kmösH iarän  mizd  u  itia  pa  sax^aii.    —    ')  Wörtl.i . .  die  Taten  lohnversehen  machtest. j.  ar)m  müxli  P.  25:  lies  anm-uxli.
•  j,  inüi«^-  f.  Name  einer  Daevr.  ptn/te "Si  pifitte  kapastis  V.  11. 9.
Pü.!  fehlt.
•  p.  mudräya-  Adj.,  bezeichnet  ein  Volk 'ägyptisch;  Ägypter';  Plur.  und  Sing. (kollekt)  als  Bezeichnung  fUr  Volk  und Land:  imä  dahyävc^  tyä  adam  *adatiiy..
dby  Google
muÖra
'^myastra.barana-
II 90
dahyäv^  tya  manä  patiyaisa" . .  arabäyJ' 'yj"  (NS.)  Bh.j.6;  2.2;  —  kaüa  pärs^ 'yam  agarbäyam  D.  //.  3;  —  pasäva" ka'^büjiye^  'yam  asiyava*  Bh.i.  10;  10;  — pirävtr  nämaf  rauia"  /ya*  °yaiy  danuvatiy D./7.3.
•  j.,  g.  mü'ÖTa-''  n.  'Exkremente,  faeces': '■%r3m  F.  11;  —  aitaKhani  astamca  .  . spämamca  (sd.)  '^ram^' {GV.)  'v.6.j; 29.  a)  sva.  'Unrat,  Unflat':  iadn  apn 'hrym  akyä  *madakya  (sd.)  ^.48. 10.
ai.  mu/ra-  n.  'Harn'.  —  Pü. :  nmkrdjin,  muht- däi  (geschr.  mn  l  r*).  —  ')  Mit  u  F.  11.
•  j.  müra-  Adj.  'stumpf-,  blödsinnig':  mil avä  zag%rä  patti.vlse  yh  .  .frataukannti . . 'räsla  (NP.)  YL  5. 93.
ai.  mürd-  Adj.  —  Vgl.  müraka-.
•  j.  mSraka-  m.  Bezeichnung  i'n^ischer Geschöpfe;  nsit  ahmi  nmäne  *zänaite ä%rava  naä,a  ra^aisti  na^a  västryD fsuyqs  aat  .  .  zayänte  dahaiäla  °kä^a pauru^ariha  varSnä^a  Y.  //.  6  ".
Et.  und  eig,  Bed.?».  —  Pü,:  mülak  kartär; s.  unter  mrüra:  —  ')  Den  drei  aAwrischen Ständen  werden  drei  Klassen  lAjÄ/ischer  Wesen ßcgenüberge stellt.  —  »)  Ob  Ableit.  aus  müra-1
•  j.  mü^-  f.  Name  einer  Pairika*'':  x^viia äzüiti  yazamaide  .  .  äzöis  .  .  hamöistri avaiAha  «ff/  {als  GS.) "'  avaiAha.  pairi- kaysi  paitistqtayaica  .  .  Y.  16.  8.
•)  Neben  jlsay,  dem  Dahia  der  Gier,  elwit als  Hexe  der  Habsucht  od.  dgl.  zu  fa^isen.  Bd. 5.  2,  28.  44  erscheint  duidin  müs  parlk  (so  28) 'die  diebische  P.  MüP,  die  als  dambömand  'mit einem  Schweif  verseben'(s,  ■Eapairikä-\  beieichnet wird,  in  Verbindung  mit  den  Planeten  als  Feind von  Sonn*,  Mond  und  Sternen.
Eig.  Bed.?   Ob'Mausf;  ai.  ™a/- f.,  np,  wi«/;
vgl,  DsT,  ZA.  /.  144.  —  Pü.  r  iransskr.  {viü's
parik;     s.    *>);     Sü.!     muinSmnT    räkfosT,     —
')  Flexionslos;  vgl.  zn  xiiq%ai/i: }.  mu}la.mas0  F.  3g:  lies  muUi.m-.
•  j.  mustamaSa-  m.  'Myrte*:    'Id  F.  11. Ir.  *tnustainj-ta-1  Schwerlich  richtig  beieugf
-    Pü.!
-/  (d.  i.
ü.d).
)  Vgl.  z
j.  Namen  der  Myrte  HehN'SchraDer Kulturpil.fi,  ScHKADEE  Keallex.  56S.
•  j.  musti.masah-  i)  n.  'Grösse  einer Faust':  *°sl^  F.^jg''.  2)  Adj.  (auch fem.)  'faustgross':  'sat3h>m  (ASf.)  xrStn (sd.)  Yt./<^.33.
*masltty-    f.   'Faust';    tti.  mufläy-  f.,   np.  musi 'Faust'.  —  Pü. ;  musI  masäk.  —  ')  Hds.  miisla.-
•  j.  muza-  Adj.  (fem.  'sä-),  bezeichnet  ein
Volk:  parS.dasmahe  .  .  *'iaÄe'*  muzayä daiAhSus  "des  P. . .,  des  J/asers  aus  dem Muierland"  Vt/^J.  125.
'}  Hds.  niu:a;  vgl.  /attya-  und  raaidya:
•  j.  myaeii  F.  11:  —  ?  — .
Pü.:  mösisn.
•  j.  myav-  V.,  nur  mit  ava  'beseitigen'. Praes.  3  mtva-.
'beseitigen,  wegnehmen':  pascaSa  vaHn ySi  dafva  va!m  ava.mivämaki  kisvasca pivas{^A.Va  V.iS.  55.
Pü.:  a/r  vinäsem.  —  >)  Hirts  Zusammen- stellungen unter  mowe  und  maj'awa  (Ablaut 105,  151)  sind  nicht  ausgeglichen.
•  g.  myas-  V.  'mischen'.  Praes.  4  myäsa-,
'zusammenmischen, -bringen,  vereinigen':
yingslä  mazdä  hadtmöi  minai  (aSPrA.) akurä  "die  du  im  selben  Haus  (mit  dir) vereinigen  sollst"  ¥.46114'*.
mit  kam  Med.  'sich  (zu  gleichen  Teilen) mischen':  dr>gvatalcä  ..  *asaonl  ..yehyalä ksm»myasaUi{-^Y\A.Y^  tni^akyä  yacä  hSi 3r»svä  ".  .  und  gegen  den,  bei  dem  sich (zu  gleichen  Teilen)  mischen  was  falsch und  was  bei  ihm  recht  ist"  '^-33- 1*';  V. 7.52  PüZ.  mit  harn  yä  saiii  zitirt
•)  D.  i.  bei  dem  'sich  Gut-  und  Übeltaten  die Wage  hallen,  einander  ausgleichen  (Mx.  72.14 : kfi  karpak  u  vinäs  hakanin  räil  asi)  und  der darum  weder  in  den  Himmel  noch  in  die  Hölle kommt,  sondern  in  das  Zwischenreich  der  Ge- mischten {hamislakän);  s.  BthL.  ZDMG.^J.  IS7, AF.  3.  61   und  zu  misvaa-.
Vgl.  mp.  hamislak  'gemischt',  np.  ämestan (wozu  Hbm,  PSt.  8).  —  Vgl.  misvan-.  —  Pü. (zu  Y.  46):  vartmS,  (zu  Y.  33):  kila  i  Si  i kam  mal  Citel  an  i  dräy  keia  i  öi  an  i  apilak, dazn  die  Erl.:  hamhlakän.—  ')  S.  zSt  Bthl.
AF.  3- 1 70,  Gdn.  BB.  14. 4.  —  '*  S  '20. 1  c,
yX3.    4.
•  g.  ''^myasträ.barana-"  Adj.  'societatem praebens  (cum—)':  mazdh7ä  ahuräaAe  s *mByasträ.baranä  (NPm.)'>  asäcä  hya^ ha%ra  (sd.)  .  .  "MAA.  und  ihr  andern Götter,  heran  (kommt)!  eure  Bundesge- nossenschaft gewährend ,  und  Asa,  auf dass  .  ."  Y..?o.  93'.
ai.  vgl.  '»/■'diu-  Adj.;  s.  GtiN.  KZ.  2/.  249, Bthl.  AF.  2.130. —  Vgl.  kamiifatay-,  p.EN. 'AiiäTpr,l.  —  Pü. :  öhtmazdm  an  i  hatnäk  han- jamanikih  barim  asttj/ahiitia,  erl. :  kusän  haute- !ak  kanjaman  apar  tan  i  pasin  tuniiti.  — ')  NA.  getrennt;  s,  No.  2.  —  ")  ä  mSya'  (NA. ä.möya')  statt  ä  mya'  wie  in  hävdya  (S  268. 13);  s.  auch  ä  vdyn%rä  Y.  34.  10.  —  J)  W* hierin  die  Anspielung  auf  die  Bd.  30. 10  ge- 38-
ob,Google
mrav-  I  i
119a
```


## [2026-09-07T16:16:05.545Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -e \"vT\\.mik\" -e \"vimik\" -e \"vi\\.mik\" -e \"vT\\.my\" BRT.txt | head; echo \"---- ISS/DKS meg cloud, mij eyelash ----\"; grep -n -e \"mīysai\" -e \"miysai\" -e \"cloud\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-07T16:16:05.606Z] TOOL RESULT

```
---- ISS/DKS meg cloud, mij eyelash ----
794:ánaba 'moistened (?)' їп 84-53 па-йпаһйт dui priyi татнагӣ gviha rüm tcerai ‘it (a paimdaka-poultice) must be made without moistening with two frZya-measures of butter (cow oil)”; Ш 92:237 u na-ánaha anarva mütaká ісетӣ ‘апа it (the paindaka-) must be made with un- moistened unbroken máfaka-plant'. Possibly compound (with na- for an-) to base naf- (nap-, nabh-) 'be moist’, Av. aiwi-nap- 'pour upon’, nepta- 'moistened', Zor.P. nam, namb ‘moist’, nambet, nambitan (gloss to Av. haek- t pour out’), naft, N.Pers. nam ‘moist’. To IE Pok. 315-16 enebh- ‘moist’, O.Ind. ndbhas- ‘mist, sky', Av. nabah-, ‘sky’, Greek уёрос, vegéAn ‘cloud’, O.Slav. nebes- ‘sky’, O.Sax. nebal, O.Engl. nifol ‘mist’. Hence a-nah- ‘о pour upon’, as Ау. атил-пар-,
905:avida ‘he sees, he is seen', Manj. 245 (as the sky (акаїа-) by clouds) ttu mafia(da) aysmva patca besa bada vasue arma kümyau jsa üphida saitta va(sa)ya avida abvatta ‘so the mind then at all times pure, stainless, seems by thoughts disturbed, sees the sense-objects abundant', = Manj. 246 vasaye av(i)da abv(a)tta; Manj. 246 vasve ya üya vira satv(d)na üvida icire ‘опе sees persons’ faces upon a clear mirror’ (see teari- 'face"); Manj. 347-8 ttu mañada aysmva prrara (by nature) batsa bada vasve arima nümyau jsa üphida saitta тақауа avida pharüka (for nümyau ‘by names’ with clear má, read kamyan ‘у thoughts"; Manj. 376 khu иса bahyana avida ch(ayye ' as in water one sees the shadows of trees'; Manj. 385 nai nai va айла aysmva nai và krrideiyà jsa pahaista ‘е mind does not see it nor is it freed from klefa-afflictions'. From à with viu- ‘see’, both avida from *à-vindá ‘he sees! and a-vinde ' he is seen’ (like hoinde ‘it
1059:i$imiü ‘covering’ with epithet kaimejä, п 60:23 mīji-jūna {айй Каітејӣ ifimd а) 'red-coloured ground, kaimeja- cloth covering, one’, Possibly from  *ati-fadama- ‘covering’ (ati- > ai- > i-, cf. pati-, to base sad- (Khotan Saka íad-) 'to cover', Av. saSayantit-ca ‘апа coverings (garments) ' ; Oss. D. asadun, asást ' to cover ', I. asadyn, asást, and DI, ахй? ' cloud’; sad- in Pašto siyalai *sadyaka- ‘rennet’, psal ‘belt, necklace', psalol ' to wear, put on’. psūnai ‘ambush (*upa-südana-)'. IE Pok. 919 sked- O.Ind. chadayati ‘to cover’, chattra- ' umbrella", chada-, chadis- 'covering', O.Engl. Лайети, plural, ‘trousers’, For Khotan Saka £ for older s, see Лайтта, särşļaa-, Sipje ‘jujube’.
1256:ora- 'sky', loc. sing. orzia, oña, V 141, 18r4 Aamdrauysi огйа ‘moving in the sky’, parallel to Z 22:296 hamdrauyst hámáte ágáto, К. 64, Sov1 hadrrauysya tsüma aía, = BS viháyasácabhyudgamya, Pali vehasam abbhuggantva; Z, 23'158 oria ggaljmndi päyore 'in the sky the clouds thunder’; ni 29, 41a4-bi khu jd oña stara dyàri ўил brrüiüri hamrrastà “аз in the sky the stars appear, they shine at night all the time’, = Manj. 361-2 khu ja asa stara dyara siva brrūñāra hamrras(f)a. From *abra-, Ау. awra-, Zor.P, agr, N.Pers. abr 'cloud', but Oss. DI. aro 'sky', duray ‘cloud’. Pašto waryadz, fem., 'cloud' < *abryaci-, Огт. yëuər, Рагйё air < *abrya-. IE Pok. 315-6 nebh-, embh-, mbh-, O.Ind. abhrd ‘clouds, sky', Lar. imber, Armen. amb ‘cloud’, See pryaura-.
1660:khara- 'dark(?)', K 109:314 tta tta bada ya Rharaña 'so it was first in darkness(?)'. From xara- base of khīraa- ‘depressed’, N.Pers. хїгай ' gloomy, dark, dim’; possibly in the deer name khara-. Kroraina khara-barna- ‘dark- coloured’ or ‘ass-coloured’?, see Asiatica, Festschrift Fr. Weller 18. Oss. D. xärä 'dark', xärämeyä 'dark cloud’ may have either older x- or h-.
1819:Egalj- 'to roar’, Z 4/107 atasi ggaljáte pyaura іп the sky (BS аййїа-) the cloud thunders'; Z 2-19 ggaljindi kho pyaure ‘they roar like the clouds'; Z 3:125 nauniku ggaljīindi kho gyastüiia svara 'softly they sound like the celestial voices’ (BS svara-); Z 23'158 oriüa gsaljindi páyore ‘in the sky the clouds thunder"; Z 24:502 ggaljmdi ttä naga “ће nüga-serpents hiss’. Parallel Pali megho thanayami Itivuttaka 66 yathapi megho thanayitvà gajja- yitvà. From base *garg- or *garz- with -ya- (for -rz-y- > -lj-, see spuljei ' spleen"), to TE ger- ' make noise', Iranian gar- for various sounds; Khotan бака grañ- ‘roar’ of a tigress, JS 17v2 pres. participle grañamca; Sogd. Chr. yryntg, yryn- ' to roar’, Yidya yənil ' to roar, bleat’, Ваібё garand, Seistüni grand 'thunder'  Zor.P. yarrünak ‘thunder’, yarrānišn, Pázand grīnā, rendering Parsi-San- skrit äkranda-, Zor.P. gryn'k (GrBd 'TD2 138:5); Pasto уатӣ 'thundering', bayāra ‘scream’, Зарәі ‘to weep', Paráéi Jar- ‘to say’, N.Pers. yurridan 'to roar’. IE Pok. 383-5 ger- 'to make noise’, with increment gerg-, O.Ind. garjati, Armen. kark-, karka£' ‘noise’, O.Engl. cracían, cearcian ' to echo’, I£ Khotan Saka garz-y-, the IE base is дег-й-; O.Ind. garj- is ambiguous.
2223:causi 'envelope(?)', ш 8o16 baysga causi ttauda-brrathá drvanaka-gūnä ‘thick covering (of clouds) with hot winds, dark(?)-coloured'. Intervocalic -s- may replace —-ss= (as in hvàssa-, hvàsa-, huata ' herb") from -xf-, and -au- occurs in dyoysa-, dyaugta- ' agitate' for -du-, but -- would normally give -2- replaced by subscript hook (see kuyüysa-). In caugi one might rather see older *cafia- to base kap- 'to hold, envelope’ (see #hausa- from *&affz- 'shae"). See also causha-,
2637:ttima- ‘seed’, and ‘cause’, v 389, 19v4 bata ku jue ttima pärendä ' where one scatters (sows) little seed’, BS G 37, 1427 bijam alpam yatha vapya; ibid. 19v4—-5 ku hará ttīma пе jiye ‘where the seed fails not at all’, BS G 37, r4br uptüd bījān mahāphalam; Sid. тодут vitsüvisi ttim "the seed of (BS) vatsa-', BS vatsa- 'holarrhena antidysen- terica', Tib. dug-mo-ñun, with 1 191, 11215 vatsaka-bijd, BS vatsa; Sid. 132v3 tti, Tib. sa-bon ‘seed’; ut 29, 4324. ttimafiüm pracai diysdai harvaidà pryaurd prabhüvana ‘it holds the cause of seeds, they grow by power of the cloud’; ibid. 43b2 bisiüd ttīmañä diysedä; Мап). 242 ttema cu таўййтї ttima 'because the vijiizna-thought is its seed’, =Z, 5'84 ttäna cu viñāni nä bijá ' because the thought is their seed’; For the meaning ‘cause’, SuvO. уд cu ttima и cu pracai ' what cause and what reason’, BS ko hetuh kalt pratyayo; SuvO. svs dot ttmnaiid, u dva pracya ' what two causes and what two reasons’, BS dvau het dvau ca pratyayau; hence read SuvO. 36v4 tta ce (ttimd)na, BS tat kasya hetoh ‘for what reason?’ (BS Aetu-); dyadic Manj. 86 ttīma hetta hama slave ‘what is the cause, reason?'. From tauk-:tuk- 'to produce seed’, if -au- through -i- to -i-, to Av. taoxman-, O.Pers. tau(hyman-, Armen. lw tol, Sogd, Bud. tn R in mrtym'k ‘mankind’, Zor.P. ібхт, tām, N.Pers. tuxm, Suyni tóym, іпут, Yidya tuyum, Waxi tayum, taym, t£ym, Sanglëëí tieym (-2- from -au-), Pašto toma, tomna 'seed'. But pattīmä 'result', with pattaj- : pattiya-.
2849:anijsa(sta tti) karmapaha dasau cuam. buàiiai ime, hauda- (rd?) defana karmana biü(nd) ' what ten evil courses (BS karmapatha) have accumulated for me, but are not expounded, those which I ought to understand, give the teaching of all the Аагта-асіопз'. From (s)kand- ‘to heap’, Oss. D. cdndá, І. cánd * heap, mass’, dord'yty cándtá ‘masses of clouds’, cánd-amad ‘bank (of a river)’ to IE skand-, O.Ind. skandati 'leap', Lat. scandó ‘rise’, See also Icesta-, tcaista-, paltcana-; and hashaistai ' he leapt’.
2926:tvarai 'many', Manj. 425-6 ranyā jàla aidrranilà kauja ysirrna pharai hsattra náyai khu pyaurai dajai pala tvarai ‘nets with jewels, índranila-stones (sapphires), with küncana-gold, abundant; he may set up like clouds umbrellas, standards, banners, many’ (BS dhvaja, Раіака-). See ttuvare.
3107:dāta- ' placed, established; law’, v 112, 3415 ttätäñe dat pyüvamatigye pvātiñe üce jsa ‘with the cool water of the hearing of this dharma-doctrine', BS anena dharma- sravana-salilodakena; у 108, 30v7 dátàna, BS dharmena; v 118, 67r3 dātänai ksird anata tcerä ' by the dharma-law his land must be guarded’, BS dharmena pálayed rástram; later Bed 48r3 uysdisimi baysam dà ' I preach the Buddhas’ dharma”, inst. sing. Bed 47v4 dana parāhna 'by dharma, by #а-сойе'; adjectives, v 123, 19v3 dátaityau aysmya dirysde with. ..of the dharma holds in mind’; K 58, 29:2 dāvañvā samühünvà ‘іп trances of the dharma’ (BS samüdhàna-); datya-, Z 64 dàti сайти ' wheel of dharma’; биуР, 61v4 dàvi cakrrd; Bed srv4 dayi cakrrina, ibid. 46r4 dayi cakrrä; fem., K 53: 10-8-9 daya prrara ' dharma nature; K 136:864 dayya byamja ' section of the dharma’; 865 daye byamji jsa; plural, v 108, gov7 datya, inst. V 118, 67:2 dütyau; gen. V 115, 64v4 datyanu; with negative, v 115, бду adütyanu, BS adhürmika-; datinaa-, 11 24, 2314 dàtinai ttaradard for BS dharma-kāya-; ш 27, 3522 datijà tcaimañä ' in the dharma eye', BS dharma-cahsus- ; v 182, 4372 dātīmja nauya ' in the dharma boat’ ; davinaa-, пі 114, буз davinai ttaramdarád; fem. v 55, 2v4 dátigyein icemaiid; K бт, доут daviji; Manj. 316 davije; plural, Y 45, 9924. data bulysd ' dharma Buddhas’; K 105:231-2 daw(ija py(aw)a, BS dharma-megha- ‘dharma cloud’; п 105:100-1 ttyai йіп davasta сағат jsa 'by that dharma lamp’ (translation AM, n.s., 11, 1965, 105). Compound, SuvO. 36r3 data-huañaa-' dharma preacher', ВӘ dharma- bhünaka-. Participle to base da- ‘to put, place, establish’; Av., O.Pers. dà-, düta-, Zor.P. nihàtan, nih-, M.Parth.T. d'm-d'd ‘creature’ (no verb), М.Регѕ.Т. nh-, nyl'dg, Pahlavi Psalter луд’; Sogd. Bud. 8"në'r'k “lord of creatures', ë'nh ' creature; for dáta-, Av. dáta-, dáitya-, Zor.P. dat, datastán, dátufar, dütik, N.Pers. dad, davar ‘judge’; Armen. lw dat ‘judgement’, datastan, api-rat 'unjust'; Sogd. Ə'Phh "law', adjective. S'f'yk, S'tkr'k ‘judge’, Chr. d'tb'r-; Bud. 'p8'ty, рату, Chr. pd'ty 'un- just', pd'i-qry; M.Parth. T. d'dór, M.Pers.T. d'yur; Pahlavi Psalter d'tzebin; Pašto dóe ‘custom’ from *dà8 from *848. IE Pok. 235-9 dhé-:dha-, O.Ind. даан, dhitd-, hitd-, Greek tinm, Өетёс̧, Lat. -ditus (ad-, соп-), Lit. déti, demi; O.Slav. déti. See also pada 'she placed’; padāna- 'receptacle'; and myàáttara- ‘inferior’ from *ni-data- or *niyàta-.
3198:dumä 'smoke', N 158:5-6 ttiña hamdrd vya vara mista dumä sarbi и (т) nväsä ка ‘between that there a great smoke arises and a great noise sounds’; Sid. тодуз dūma, Tib. dud-pa; Sid. 147r2 hīha, dāmmä 'house smoke" (='soot'), Tib. dud-pa; Sid. 122r1 Аш daumä, Tib. khyim-gyi du-ba; Ur 93:259 dumi; compound, ш $4742 duma-hausia güra 'smoke-dried grapes’. See padoa-, padiüte, duya. Base dau-:diü- ‘ќо fumigate', Av. dvan-, dunman- ‘cloud’, Zor.P. düt, N;Pers, düd, Ва!бё dit, dit, Pašto dund, іп, Рагйёї di, Yidya lui, Sangl. 215, Waxi Št, Suyni Bud, Yazg. 804 (but Sogd. Bud. pzt-, Oss. D. jüxdág, Yayn. фаза), IE Pok. 261-7 dheu- 'of smoke, dust’, O.Ind. dhüma-, Lat. fumus, Lit. plur. dmat, O.Slav. dymii,
3304:drüme 'flood(;)', К 49-y2 día bayspi busümji pyaure ysarrnīja drüme fairkye ramnīnai Баға 'sky's thick per- fumed clouds, excellent golden streams, jewelled rain’, Base dar-, dram- ' to run? see s.v. dram-, ТЕ Pok. 204-6, of European river names (ibid. 205), as Dramme < *dromia.
3355:drvanaka-güná 'dark-coloured', ш 80-16 baysga caugi Паша brratha drvanaka-günd ' thick covering (of clouds), dark storms, dark-coloured'. Base drau-;dru- ‘be dark’ to IE Pok. 251-2 dher- 'be dark’ with increment -eu- dhreu- see also dravasam ‘dark, red (of fire)', drava- with suffix -dsa-. For ‘thick clouds’ see K 49, 4/2 baysgi busamjt pyaure ' thick scented clouds’,
3492:nastauda- ‘burnt’, 2 5:49 pyaura...uysdemáte апаи nastaudo ce püsüre jsa nátauda ‘the cloud...cools the burnt earth which is heated by the sunshine', from *nii-tafta-, see ttav-, ttauda-.
3721:nuvalys- 'issue', SuvP. 61r1-2 tti vā Rrrisame beda silām nvaysira wvüra 'at the time of the (drum-) beating these noble verses issued’ (BS iloka-, udára-), BS tena üko- lyamünüyü ime flokaé ca niscarüh; Z т]'ї8 ggaryau nuvalysde kho ju bārmañi samu от mountains it issues just as fram a reservoir’; Z 20°57 Lturrrna (r supra- script to -r) nuvaysde 'issues from the mouth’; 2 3:125 bálevo nuvaysäre 'lightnings issue’; Z 3:21 pyaure nvaysüre pharu 'many clouds issue’; 2 4:56 bisse nuva- ysüre vikalpe ‘all the concepts issue’; variant, v 380, ir2 b(i)é(d) nuvajsare (js certain). From ni-parz-, ni- barz- or ni-varz-; to Armen. lw parzem ‘to filter, purify, expand, put forth’, Hence IE Pok. 3012 pel- ' drive', see s.v. pasa 'emissary' « pel-k-, Armen. lw parsem 'send out’; Lat. pello, pulsus, pultare; OHG -falz in anafalz, O.Engl. anfilte ‘anvil’, O.Engl. felt (cloth). Here nuvalys- < *ni-peló(h)- and nuvajs- < *ni-pel-g(/1)-, beside pasa- < *pelk-. For -fh-:-gh- see s.v. drays-, darys-, and drjs- from IE dheráh-, dhergh-.
3993:patisu 'covering (?)', Z 2:176 samu kho ātāśi vasusti váno pyaurāņu райи “ав the sky (BS akáfa-) clears without the covering of clouds’. The uncertainty lies in the possibility that patif- could mean 'to come’ (O.Ind. Epic jalada- agama- ‘coming of clouds") rather than be the older form of putj- ‘to cover’, see КТ 6, 158 and 440; below pvti-.
4214:paltcana ‘heaps’ (less likely 'fragments", Z 24:422 pürnanu hálstánu pharu paltcana ando. . . ggadare ‘many heaps of arrows, of spears lie on the ground’, From base skand-, see tcaista-' heaped’, Oss. D. cándá, Y. cánd' heap’, cünd-amad ‘bank of river’, ávräyty cändtä ‘masses of clouds”, If ‘fragment’, see base skarid-, s.v. Лаісап-.
4503:páyaura- ‘cloud’, see pryaurá.
4765:pyaura ‘cloud’, see фгуаитй-.
```


## [2026-09-07T16:16:17.773Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== DKS miysai ===\"; grep -n -e \"miysai\" -e \"mijsa\" -e \"'urine'\" ISS_alt_DKS.txt | head -10; echo \"=== HUB ===\"; grep -n -e \"miza\" -e \"muza\" -e \"meġ\" -e \"Wolke\" -e \"Augenwimper\" HUB.txt | head -20"
}
```


### [2026-09-07T16:16:17.840Z] TOOL RESULT

```
=== DKS miysai ===
1245:5бгз odd ‘ир to’, BS upádaya (cited s.v. ssanda); K 65, S4r2 prraundve astana auda cü küra-draistd ' beginning with killing up to what are false views'. With following buru, V 99, rs odi dstai mijsaya buru panu uysnaurá väte
1497:kumijsata- ‘sesame’, v 333, 2773 kumjsatu kerä "sows sesame seeds’, BS С 31, 2423-4 tilam vapayet; Sid. дут kumjsa; Sid. gr3 kujsa jsa; Sid. 100v4 Айтта, Adjective v 333:27v2 kwunjsatinau. hambisu ‘heap of sesame’, BS С 37, 24b1 tila-phalakünt; V 335, 3371 kuinjsattje dane ' sesame grains’ BS G 37, 2966 tila-phalakah; v 69-70, 8v2—3 gvihu rrügu o kujsatinau, BS G 37, 12а5 ghrtena và tailena và; Sid. 139r2 kugjsavina aruma rrūna ‘sesame medicinal oils’; compound п 35, 818 hamjsata-kerá и ganama-kerā ' sowers of sesame and sowers of wheat’. From &uncita-, O.Ind. kuncita-, Zor.P. hnéyt!, N.Pers. kunfid, -td, -ud; Sogd.
2221:caurši ‘goat's fat(?)', 111 89-160 tcard, cau-rsi, tharka mijsa (three fatty things) ‘fat, goat's far, walnut kernel’. Pos- sibly from cau ‘goat’ (see caukala-), and "ў from svi with intruse -r-, from *suiya- ' fatty stuff’ to base sau-:si- ' to swell’, like IE Pok. 793-4 pei-:pi- ' swell, be fat’, O.Ind. pdyate ‘swells’, ptnd-, pivan- ‘fat’. See also co-ivi. Base IE Pok. 592-4 Ёеи-:ЁЙй- ‘swell’.
4004:pattauda- ' heated, roasted’, participle to pattav-, Z 13:152 itīma pattaudà ‘roasted seed’, cliché Šikşã-samuccaya şır ла rohati vijanàm agni-dagdhānām ankuro harito yathā ‘does not grow, like the green shoot of fire- roasted seed’; HI go'i82 pattāmdë hāmai 'roasted barley’, ш 91-211 pattaudä hamat, pattaudä ādä ' roasted barley, roasted flour’; ш 87:111 pattaudä gana mijsaká ‘roasted kernels of яйпаа- plant’, Sid. 100v4 pattoda miüjsüka; parallel to їп go'rg8 padīya gāņām miījsäkā (padiya 'burnt'. From *pati-tafta- to pattav-, base *pati-tap-.
4068:jpaniys(au) 'urine', BS mütra-. From base naiz- ‘flow’,
4111:paysüya ‘dish, griddle (?)', loc. sing., ш 18:20 paysaya bisa nümji tcerü ‘bread (baked) on a griddle must be made’, from base pas- ‘Бе flat, plain’, Oss. D. fázd, I. faz (see s.v. paysa-) with suffix -à as májsü, mijsa ' marrow, kernel’, loc. sing. mījsāya. See also s.v. sáta-.
4551:(dyadic) ‘white’, BS pāndurāni. Hence pdsa from *pisdkü-, for -а note mijsa ‘marrow’, #anda 'earth, ground’, IE Pok. 794-5 феїй-.
4917:phiysgüna- ‘urinary bladder’, Sid. 121v2 phiysgam, BS vasti-, Tib. ¿hu-so; loc. sing. Sid. 122v4 phiysgāña; 1 143, 52r5 phaiysgāña; nt 88:148. pheysgäñä. Adjective, 1 157, 69r2 pháysagaña acha (or loc. sing.?) From *mizpa- düna-, Sogd. Bud. Bzm-9'ny. For the initial, note also miysai, biysina. Cognates s.v. miysar.
5309:biysma 'urine', Sid. rozvs brysma, Tib. gcn; Sid. 12814. buystfie biysme jsa, BS basta-mütre, Tib. ra-géin dan; adjec-
5310:tive, 24v3 O.Suv Biysmansa paniys(au) (dyadic), BS mütra-. See cognates s.v. miysat, and note three initials miysai, biysma, phiysgüna- ‘bladder’. For b-, note also Sogd. Bud. Й#эт-8'пу ‘bladder’, BS vastr-. IE. Pok. 713 meih-.
=== HUB ===
209:'Temperament*, Matlkan i catrang § 13) , amiza 'commixtus, coitus,
4172:ebenso im Neup. vor Doppelkonsonanten: ahr 'Wolke*,
4808:miia = mum *Augenwimper aus *fnicak, vgl. bal.
6397:a) = np. b in : abr * Wolke' = paz. awar Shk. 233, zd,
8088:*Cypresse* ; mum, pi. muzgan Augenwimper , bal. micac, also
8829:= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
9250:*Wolke* = zd. awra- u. s. w.
9559:umgestellt: abr 'Wolke* = zd. awra-; sahr 'Stadt' =
```


## [2026-09-07T16:16:28.456Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; res={}\nfor i,l in enumerate(lines,1):\n    res[i]=leaf; leaf+=l.count('\\f')\nfor ln in [4808,8088,8829,209]:\n    print(ln,'leaf',res[ln],'printed',res[ln]-10)\nEOF\necho \"--- context 8080-8092 ---\"; sed -n '8084,8092p' HUB.txt; echo \"--- 8825-8833 ---\"; sed -n '8825,8833p' HUB.txt; echo \"--- 4804-4812 ---\"; sed -n '4804,4812p' HUB.txt"
}
```


### [2026-09-07T16:16:30.016Z] TOOL RESULT

```
4808 leaf 147 printed 137
8088 leaf 236 printed 226
8829 leaf 257 printed 247
209 leaf 19 printed 9
--- context 8080-8092 ---
tajar *heizbares Winterhaus', arab. tazar 'Sommerhaus* =
ap. tacara-, arm. tadar 'Tempel, Palast, Haus'; varj 'Grosse,
Wiirde' = zd. varecah-; hujXr — - xujlr = hum' schon' =
zd. hucidra^; noj , noz , noz pinus' = arm. noc, noci
*Cypresse* ; mum, pi. muzgan Augenwimper , bal. micac, also
*) Bei B loch ma nil JASB. XXXVII, 1, 52: mavlz.- 227 —
fhl, *micak; dd0, ddza*Lsick\ arm. dod (medic. Schriften) in
doci xez = Xack-gummi'; pazan = pdzan, kavtz = kavHz
s. oben, raja^ raza oben p. 66 ^). Np. ocaj *Kreuz' aus alterem
--- 8825-8833 ---
§ 139. Ap. g nach Vokalen und r = y bleibt im
Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
(oben p. 98) = zd. mareya- ; may profunditas*, mayak
Grube* H. 985 ■= zd. maya- Xoch*; muy^ may *Magier
= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
aroq 'Rulpsen', gr. iotvyo^iai; dyardan 'deglutire'? H. 36;
t^y 'Spitze, Schwert', zd. bitaeya- 'zweischneidig* ; juy, yOy
* Joch*, skr. yiiga- ; dtirdy 'Luge = ap. drauga- (= drauya-) ;
day 'Brandmal, Fleck, Wunde, Brenneisen, zd. daya-; doy
--- 4804-4812 ---
in: ildan *sammeln, pfliicken', pr. dtnam; guzldan 'aus-
suchen': pr. gtisflnam von Wrzl. 6i u. s. w.
§ 19. Aus i wird u bei Labialen oder durch Assimi-
lation an vorangehendes oder folgendes u:
miia = mum *Augenwimper aus *fnicak, vgl. bal.
micdc; muzd, muzd *Lohn', paz. mazd Min. Gl. 136, phi.
m(i)zd und muzd Gl. and Ind. 213 und 217, afgh. LW. mazd
oder muzd Vages, hire' = zd. mizda-^ ap. ^mizda-, gr.
fjLi6&6g] supuS, supus neben sipiS u. s. w. 'Laus == zd. spis;
```


## [2026-09-07T16:16:36.247Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -e \"مژه\" -e \"میغ\" -e \"آمیختن\" -e \"میزیدن\" ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i -e \"MEIK\" -e \"MEIGH\" -e \"MUZHE\" -e \"MIGH\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T16:16:36.314Z] TOOL RESULT

```
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
1991:آمیختن»- آمیز آمیغ آمیزه ۷۱
14017:۲ | مژه مژگان
14354:۴ / مه میغ (به چم "ابر" "سحاب")
=== latin index ===
1972:MENGEN DUTCH) ga MISGEIN, MIGHA}: —-(GREEH)..sty
1973:(OLD CHURCH SLAVIC) 45 533% MEIKSO, MEIGNYNAL ‘
13825:MIGHT ENGLISH) g-lSil GREEK) gy
14096:MAGLA (SERBIAN) 9 pe MIGH, MIGHA OSSETIC) «ge 3\
```


## [2026-09-07T16:16:41.839Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\nmarks={}\nfor i,l in enumerate(lines,1):\n    m=re.search(r'pdf page (\\d+)',l)\n    if m: cur=int(m.group(1))\n    marks[i]=cur\nfor ln in (1991,14017,14354):\n    print(ln,'pdf page',marks[ln],'printed',(marks[ln] or 0)+1)\nEOF\necho \"=== ctx 1985-2000 ===\"; sed -n '1985,2000p' ARY_pages.txt; echo \"=== ctx 14010,14025 ===\"; sed -n '14010,14028p' ARY_pages.txt; echo \"=== ctx 14348,14365 ===\"; sed -n '14348,14366p' ARY_pages.txt"
}
```


### [2026-09-07T16:16:43.168Z] TOOL RESULT

```
1991 pdf page 70 printed 71
14017 pdf page 471 printed 472
14354 pdf page 483 printed 484
=== ctx 1985-2000 ===
تخاری 8(:8 ((فن702): 6۸۸ ,الا رومانی 21/4 #): (شاید) ۷1
ساسکریت رازه اد سا پرتغالی "(۳0877010832): (شاید) :۹ ۱7 :۰.۹8۱
اا۸#ق2 باقع باتفللفه نامرد گرتیک:0071/10): متام
ارمنی (۸4/8(/14۸): انا انش نررش کهْنْ (۸0888 0): 04
[pdf page 70]
تج
آمیختن»- آمیز آمیغ آمیزه ۷۱
آلمانی کهن (/(057044 4014 0ظا0):
08/۸ پسگشت‌ها ۶۸۵78۵755
آلمانی 0879400): 10/0 5 20/0220
انگلیسی کهن (#لقلا8/0 ۰:۱۵ 006۸3۲ 2( +820
انگلینی ‏ (8701977) :۰۰ : لد ره 9 (۷8313) :5 اطما5ط
دانمارک ی" (0(/73/7): دای 7 (۲0185) ,53 ۸1۸05/250
سوئدی ‏ (3(052/54): 10۸ 69396 علاط
نروژی (0۷005014/0: دا را و نا ونان :0/105
ملدی (7لع07): ان 2 (۲۱3/۵) 5۰
=== ctx 14010,14025 ===
ایسلندی کهن (010۸۷74۷/ی5 صا0): پسگشت‌ها ع رت دنت
10۸ 0 200500
آلمانی کهن (05824۸۸ ۲۲04 صا۵): 3 (۳۸0 0۸30 :۸۸۲2/22
,3180 بال۸410075 ,111377۸3 1222 ناه ۱

اد رون ۱۱ لغت‌نامه دهخدا: ۳۷۴۶
[pdf page 471]
۲ | مژه مژگان
بادداشت. ۱
۱- چم این واژه در سانسکریت و پلفاری: خرد» غاقل,
چم این واژه در گوتیکه: هدف» سر منزل مقصرد. 4 ۹
چم این واژه در آلمانی کهن و ولزی: اشتیاق» خواستن. بشید
چم این واژه در لیتوانی و لتونی: دلیر» دلااور,
چم این واژه در آلبانی؛ پیروزی. :
۲- در اوستایی 11۸210 به چم خردمند" و "عافل " هم بوده است.
| چمانگلیس سروازای فارس ‏ #کش88
پهلری (47ال۸): 1(
12۸6 ,۸41273 ,2۳073۸ ایرندی کهن (تلقل۸/ .ا0):
کردی (0-72157): 1 هن
=== ctx 14348,14365 ===
لائین 77 1۸01878 ,۱۸۵۲۷۵ ولزی (5]7ل5/): ان ۱یا
فرائسه (270/7ق/8: ی ان برتونی (8786700۷): 8878
اسپانیایی (52۸137): زد ونان آلبانی رامزبیمهتم: ۰ 1۸2111 بل ۸«
ابتالیایی (74۵۸۷): زین اند با هیت (17777775): دنه 4 دای
پرتغائی (۳0717010835): ای بان ابا
[pdf page 483]
۴ / مه میغ (به چم "ابر" "سحاب")
پسگشت‌ها هرت دی 7 (063۸310) :ال 08/۸
8 000 کلا عم :0/25
8۸/7 0 1339 ۵ طلاطا
3 (۸1613) ,639 (1۸8183) برهان قاطع + ۵۸ این
بادداشت. 5
زه واژه‌های هندی آمهاراج " و "مهاتما" و "ماهوت"(81۸110171) نیز از همین ریشه‌اند.
اوستایی (۸۷287/0): ۸۸۳۸ لهستانی (۳0/54): ۸10۸
پهلوی (1/اتله): 5 ۸/801 روسی (۷ا55/): 7 ,ش3106
اوستی (05557/6): ۱۸ ,1/۳6۶ صربی (/85814): ها6ق3<
سانسکریت (54(/907): ۷1863۸ ,۸115 برهمی (80778141۸1): ۸
ارمنی (/4//21۵): ,680 لیترانی (/(۵ا هل( 77): 16۸
پونانی (08888): 0۱۱ لترنی (لتی) (701۸4ما): ۵۸
```


## [2026-09-07T16:16:52.970Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -e \"میز \" -e \"میزیدن\" -e \"گمیز\" -e \"شاشیدن\" ARY_pages.txt | head -10; echo \"=== root headers near 483 ===\"; sed -n '14366,14395p' ARY_pages.txt"
}
```


### [2026-09-07T16:16:53.033Z] TOOL RESULT

```
167:صغیر و فلات ایران و هندوستان را زیر مهمیز خود درآوردند.
660:(48-49 ,۱1۸110۷). قوم ایرانی دیگرا » الان‌ها (۸775آ۸) فرانسه و اسپانیا را زیر مهمیز کشیده و
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
1147:حاوی سرودهای نیایشآمیز بنام «پشت‌هاء (۷۸81778) و وردهایی برای طرد دیوها پنام «ویدیوداده ...۰
1991:آمیختن»- آمیز آمیغ آمیزه ۷۱
=== root headers near 483 ===
پونانی (08888): 0۱۱ لترنی (لتی) (701۸4ما): ۵۸
ایسلندی‌کهن (010۸1۸(7(ی5 صاه).
۸18918 پسگشت‌ها اشهردد رد۲
فریزی کهن (4۸۷ا5ل۶۶ صضا۵): 141605105 8 ۶000
انگلیسی کهن (4ل40/3ظ صا0): انا 8 (۸131) ی
انگلیسی (6۸0/314): 17 6 (0فا[ )830‏ م+قعقانمع0 "
سرئدی (81750/57): 17 4 (81181) ,107 (213:))70170 اهر
نر وژی (۸/0701۷): 157 6546 2
هلندی (7لع007): ۷۸16651۸0 ,۸1191 1 (187/) 0015
اسلاوی کهن (4۷/2ا5 ل#نائن صاه): 0 (115) +7
1/101۸ برهان قاطع + نخقم اد یمس تما
بمانگلیسی سرواژی تال را لا
پهلری (/4۲ال(۸): بکقف31۲۴ ,۸۸۲۲ ۸ 2/1703
[pdf page 484]
۱ می (به چم "شراب") / ۴۸۵
اوستی (0587/0)؛ 3 اه
کردی (0153)): پسگشت‌ها رده رد تاد
,۷100 ,#نآ3انل2 710 2005900
بلوچی (اللتاا8۸): 1 (ل85۸) دراد شا
7 11020 برهان قاطع :۰ ارمیما
سانسکریت (8540/577)+ ه08 فرهنگ معین + ۳۳۶۲
آرمنی (7ل4ا(۸۸48) ۸۸۸۸
اوستابی (4۲857:400): ,ش۸1۸0 ,لا ۸1۸73 آلمانی کهن ((057(44 ۵4[ 02):
۸۵1 ۷87۲
پپلری (//بمائزم): ۰ لا3۸ ,31۸03 ,2۸3 آلمانی (054۸2): 8 هون 1۱
اوستی (05538712): 0 ,3110 انگلیسی کهن (نژکلا8(/0 طا۰۰:)۵ 218010
کردی (0157): ۸ ,۸15 انگلیسی (6۸/057): 25۵0
افغانی (پشنو) (470۸/1): 1 دانمارکی (0۸04154): 702
سغدی (/800/0140): 01 سوئدی (57520/57): زور 1
سانسکریت (54(807): 31۸2۸ ,۸1۸20151 نر وژی (۰)/0#00140 زار ۱
```


## [2026-09-07T16:17:00.139Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la MON_part*.txt | head; grep -c \"\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"میز\" MON_part2.txt | head -5"
}
```


### [2026-09-07T16:17:00.220Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part2.txt:94500
MON_part1.txt:99339
872:سفره و میز غذاخوری. 
878:بدان طعام خورند. میز غذاخوری: میزی که 
1567:قشلاق با تمیز خطر از دور وامی دارد (دکتر 
1816:کول زدن» خدعه کردن. کدورت. آمیزش 
1845:بهم آمیختگی حق و باطل. آمیزش چیزی
```


## [2026-09-07T16:17:04.483Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^میز\\|میز \\[\\|میز ‪\\|میز(\" MON_part2.txt | head -10; echo \"--- search bracket pahlavi ---\"; grep -n \"mēz\\|میزیدن\" MON_part2.txt | head -10; echo \"--- 860-890 ---\"; sed -n '862,890p' MON_part2.txt"
}
```


### [2026-09-07T16:17:04.575Z] TOOL RESULT

```
22346:میزان واسطه‌اش خ وک است و به وسبلة 
26460:میزان خود به مشتری فروشد. 
31633:میزان الحراره بکا ر برده‌اند (رکك. لف.) 
33504:میز میگذارند. رنگ گل‌های آن زرد 
45116:میزء نیمکت و غیره؛ اثاثه. 
59386:میزبان. 
62551:میزان باشد. ( کشاف‌اصطلاحات) ضح.- 
70154:میزی که روی آن لوازم تحریر نهند و چیز 
70160:میزاب: 7-2] ۱2۱ [ مت ات» معر. فتنز انتا] 
70164:میزان: 011720 [ع. ۰ (.) ترازو. مقیاس. 
--- search bracket pahlavi ---
--- 860-890 ---
گیاه؛ ج. ان (غم. گسوی بافته» دوّابه؛ 
ج. . غداثر (غدایر). 

غذاء: ۰ 72۵[ع. . ف.] (.) آنجه خورده شود 
و قوام بدن بدان ست» خوردنی و نوشیدنی) 
ج. اغذیه. غذای سنگین: خوراکی که ثقیل 
باشد؛ غدای دیر هضم. 

غذا جیدن: 7-0« [ع. ف.] (سصم.) 
چیدن انواع غذا بطور منظم و مرتب در 
سفره و میز غذاخوری. 

غذاخوری: 02« (ع. ف.] (حامص.) 
عمل غدا خوردن» طعام خوردن. اطاق 
(سالن) غذاخوری: اطاقی (سالنی) که در آن 
غذا صرف کنند. قاشق غذاخوری: قاشقی که 
بدان طعام خورند. میز غذاخوری: میزی که 
روی 0 غدا جیئنك. 

غذا کشیدن: 7 [غع. ف.) (مص م.) 
غذا را از دیگ در ظرف‌ها ریختن» طعام 
کشیدن. 

غر: ۲(ص.) زن فاحشه؛ قحه. بد دل. مرد 
غر: ۸« [مخف. غرد] (.) خانهٌ چوبین و نثین؛ 
به این معنی در ترکیب آید: بادغر. 

غر: :[- قر] (ا.) جنباندن جزو یا تمام بدن 
از روی ناز. غر و غریبیله: (عم.) ناز و ادا و
```


## [2026-09-07T16:17:10.739Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '70135,70170p' MON_part2.txt; echo \"=== مژه ===\"; grep -n \"مژه:\\|مژگان\" MON_part2.txt | head -5"
}
```


### [2026-09-07T16:17:10.814Z] TOOL RESULT

```
است؛. 

میر ۵. (۵-) ۱۱11۵ [ع. میرة] (.) بار خورا کل 
خواربار. 

میر: (۱۱]2)082 (۰۱) ول شاش. 

میر: (۱2)62 (ص. ۱.) مهمان. (.) اسباب؛ 
ها 

میر: 2 (مغ. میز ] (.) کرسیی که دارای 
چهار پایةٌ بلند است و بر روی آن لوازم 
تحریر نهند و چیز نویسند» یا ظرف‌های غدا 
چینند و جز آن. ضح.- این کلمه ظ. مغولی 
الااصل است و از اینجا وارد ترکی و هندی 
شده ولی از سوی دیگر در بر تغالی 3 به 
همین معنی (میز) آمده است. میز تحریر: 
میزی که روی آن لوازم تحریر نهند و چیز 
نویسند. میز گرد: میز مدورء (سیا.) شورایی 
که از شخصت‌های رسمی متعدد تشک 
شوی تاساره ش لهای سنحت ک قر 
نهارخوری: میزی که بر روی آن ظروف و 
آلات غذاخوری نهند و غذا خورند. 
میزاب: 7-2] ۱2۱ [ مت ات» معر. فتنز انتا] 
1( آب راهه» آب گذر. ناودان؛ ج. با فا 
موازیب» میاز یب (غم.) 

میزان: 011720 [ع. ۰ (.) ترازو. مقیاس. 
اندازه» مقداره هلا ج: . موازین. . هفتمین برج 
از بروج دوازده کانة سال شمسی معادل آبان 
ماه. (مس.) جملهةٌ موسیقی. به اجزای کوچک 
مساوی تقسیم می‌شود که آنها را میزان نامند 
و آنها به وسیلاٌ خط کوچکی از یکدیگر 
جدا قن کرو رکه مبزان بر دو نوع است: میزان 
=== مژه ===
37013:معدنی. گوهر مژگان: (کد.) اشکك. گوهر 
51412:وسلةٌ آن ابرو و مژگان را آرایش دهند. 
55261:مژگان: هن رصق ع(ه) ۱02۵ (۰۱) ج. مز و ؛ 
55265:کنار آزاد پلکث چشم؛ ج. مژگان. ضح.- در 
72212:(کد.) سخن بکر. ناسفته گوهر مژگانی: ( کد.)
```


## [2026-09-07T16:17:17.075Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '55255,55275p' MON_part2.txt"
}
```


### [2026-09-07T16:17:17.121Z] TOOL RESULT

```
شنوندةً خبری خوش به خبرآورنده دهد؛ 
انعام» بخشش. خبر خوش» مزده. بشارت. 
مزده. (۵-)۱0202 (ا.) خبر خوش: شارت 
نوید. (عم.) مژدگانی انعام خبر خوش. 
شادی» خوشحالی. 

مژگان: هن رصق ع(ه) ۱02۵ (۰۱) ج. مز و ؛ 
مو های ریبزی که ک از آزاد بلک‌های 
فوقانی و تحتانی چشم می‌رویند! مژه‌ها. 
مژه. 0 ,)02۸ (۱.) هر یک از موهای 
کنار آزاد پلکث چشم؛ ج. مژگان. ضح.- در 
شعر بصورت مشدد اید. 

مس: ۵ |[ - مه | (ص.) بر کف مه . 

مس: (0۸5)5 (ع.] (مص م.) ذننت اسالبادن» 
سودن. (امسص.) دست مالی» سباش. 
هانگ 

مس: 5 ([معر. مس | (.) (شیم.) فلزری 
التیته قرمرز تک که زور ۳ درجه دوت
```


## [2026-09-07T16:17:27.165Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%85%DB%8C%D8%AE%D8%AA%D9%86",
 "prompt": "Persian گمیختن: etymology (Middle Persian gumēxtan, prefix, Proto-Iranian), meaning. If the page does not exist, say so."
}
```


## [2026-09-07T16:17:28.816Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B2%DB%8C%D8%AF%D9%86",
 "prompt": "Persian میزیدن: etymology (Middle Persian, Avestan, PIE), meaning; also any note on میز 'urine' and گمیز."
}
```


### [2026-09-07T16:17:29.014Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:17:30.476Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T16:17:34.155Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/maij-",
 "prompt": "Proto-Iranian *maij- : meaning and descendants. If not found say so."
}
```


## [2026-09-07T16:17:35.023Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/miscellaneous",
 "prompt": "Etymology of miscellaneous: Latin miscellaneus, miscere, PIE root, dates."
}
```


### [2026-09-07T16:17:35.755Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:17:39.148Z] TOOL RESULT

```
# Etymology of Miscellaneous

The word "miscellaneous" comes from Latin roots meaning "mixed." According to the Online Etymology Dictionary, the term emerged "consisting of a mixture, diversified" in the 1630s, derived from Latin *miscellaneus* ("mixed, miscellaneous"), which itself comes from *miscere* ("to mix").

The ultimate origin traces back to the Proto-Indo-European root *\*meik-*, meaning "to mix." This ancient root is also the source of related English words like mixture, medley, and promiscuous—all sharing that fundamental sense of combining or blending different elements together.
```


## [2026-09-07T16:17:46.078Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meyǵʰ-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\" \\\n \"https://en.wiktionary.org/wiki/میغ\" \\\n \"https://en.wiktionary.org/wiki/مژه\" \\\n \"https://en.wiktionary.org/wiki/آمیختن\" \\\n \"https://www.etymonline.com/word/mist\" \\\n \"https://www.etymonline.com/word/mix\" \\\n \"https://www.etymonline.com/word/miscellaneous\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 328, root Meig/Meik/Meigh 1/Meigh 2: PIE roots mix / urinate / blink-cloud, Persian amixtan gumixtan miz mixtan mig meh moze, Latin miscere, Germanic mihstu mist\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T16:17:50.703Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fafaf9401117db96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7416350792e0f29.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/adaedff8fad7ca9d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c54e01311cc31b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72d9cc61743c80fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e92d127d61193b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1478e682f43e9113.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32da72b22660ea04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0fe56eeee70920e.txt
```


## [2026-09-07T16:18:03.639Z] TOOL CALL #73: Bash

```json
{
 "command": "ls site/pages/328.jpg 2>/dev/null || pdftoppm -f 328 -l 328 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg328 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T16:18:04.873Z] TOOL RESULT

```
site/pages/328.jpg
total 2672
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 12:17 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    449 Sep  7 12:17 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb   7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb  33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb  46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb  51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb  37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb  58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb 146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb 128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb      4 Sep  7 12:17 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb  35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T16:18:07.749Z] TOOL CALL #74: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/328.jpg"
}
```


### [2026-09-07T16:18:07.774Z] TOOL RESULT

```

```


## [2026-09-07T16:18:42.801Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:26:25.626Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-328.json <<'JSONEOF'\n{\n  \"pdf_page\": 328,\n  \"book_page\": 298,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Meig, Meik / Meigh 1 / Meigh 2\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"three separate PIE roots: *meyḱ- (~*meyǵ-) 'to mix' (Pok. 714); *h₃meyǵʰ- 'to urinate' (Pok. 713); *h₃meygʰ- ~ *meyǵ(ʷ)ʰ- 'to blink, cover the eyes; mist, cloud' (Pok. 712-713)\",\n      \"note\": \"The three glosses Nourai gives are each correct and correspond exactly to the pages he cites: Pokorny 714 'meiḱ- (and meiǵ-?) to mix, stir' (Av. minasti, Lat. misceo); Pokorny 713 'meiǵh- to urinate' (Av. maēzaiti, maēsman-); Pokorny 712-713 'meiǵh-, also meik- to glimmer, twinkle; mist' (Av. maēγa- 'cloud', Npers. miza/muza 'eyelash', Lat. mico). What is questionable is the single ROOT BOX: presenting Meig/Meik, Meigh 1 and Meigh 2 as one root implies a unity that Walde-Pokorny explicitly reject — WLD II 246 credits Kern (IF 4, 106f.) with the 'richtige Trennung von meigh- \\\"harnen\\\"' from meigh- 'flimmern; Nebel, Wolke', and *meyḱ- 'mix' is a wholly different root (ends in a palatal *ḱ, not *ǵʰ). Wiktionary keeps *meyḱ-, *h₃meyǵʰ- and *h₃meygʰ- apart, saying only that 'a connection to *h₃meygʰ- is conceivable' for the 'urinate' root. On the other side, Mo'in (BQT 2079 n.2) writes that the cognacy of میغ with the root maēz- 'to urinate' «قطعی بنظر میرسد», Watkins/AHD file MIST under meigh- 'to urinate', and Cheung (2007: 259) suggests the 'cloud' formation *maiga- belongs with *maiǰ 'to blink, cover (the eyes)'. So Nourai's lumping reproduces one live minority position for Meigh 1 ~ Meigh 2 but cannot be defended for Meik 'to mix'. Verdict: plausible with the mix root separated out.\",\n      \"note_fa\": \"نورایی سه ریشهٔ جداگانهٔ هندواروپایی آغازین را در یک کادر گنجانده است: ‏*meyḱ- «آمیختن» (پوکورنی ۷۱۴)، ‏*h₃meyǵʰ- «ادرار کردن» (پوکورنی ۷۱۳) و ‏*h₃meygʰ- / *meyǵ(ʷ)ʰ- «پلک زدن، پوشاندن (چشم)؛ مه، ابر» (پوکورنی ۷۱۲–۷۱۳). خودِ سه معنایی که او نوشته با همان صفحات پوکورنی کاملاً می‌خواند و نادرست نیست؛ اشکال در یکی‌شمردن آنهاست. والده-پوکورنی (جلد دوم ص ۲۴۶) به‌صراحت جداسازی «ادرار کردن» از «مه/ابر» را درست می‌داند و ریشهٔ «آمیختن» با کامی *ḱ پایان می‌یابد، پس جدا است. در برابر، معین در حاشیهٔ برهان قاطع (ص ۲۰۷۹) هم‌ریشگی «میغ» با maēz- «ادرار کردن» را «قطعی» می‌داند و واتکینز نیز mist انگلیسی را زیر ریشهٔ «ادرار کردن» می‌آورد. پس ادعای نورایی برای پیوند Meigh 1 و Meigh 2 با احتیاط پذیرفتنی است، ولی گنجاندن Meik «آمیختن» در همان ریشه پذیرفتنی نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meyǵʰ-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:712-714\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root/lemma: meiǵh-, also meik- | Meaning: to glimmer, twinkle; mist … Page(s): 712-713'; 'Root/lemma: meiǵh- | Meaning: to urinate … Page(s): 713'; 'Root/lemma: meiḱ- (and meiǵ-?) | Meaning: to mix, stir … Page(s): 714'. The three-page span is exactly right, and Nourai's three glosses paraphrase Pokorny's three Bedeutung lines.\"},\n        {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt has 'meigh-. To urinate' (with Gmc *mih-stu- > MIST, MISTLETOE, and Lat. micturire) and 'meik-. To mix' (Lat. miscēre > MISCELLANEOUS, MIX) — i.e. two of Nourai's three, both with the same glosses. Watkins has NO separate root for 'blink, cover, darken': he files no reflex of Pok. 712 under a distinct entry, so Nourai's 'Meigh 2' is not in AHD.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 244-247\", \"stance\": \"partial\", \"note\": \"Three consecutive lemmas: 'meik- \\\"mischen\\\"' (244f., av. misvan-, lat. misceo), 'meigh- \\\"harnen\\\" (Praes. meigho und mingho)' (245f., av. maezaiti, maēsma-, got. maihstus, ahd. mist), 'meigh-, auch meiq- \\\"flimmern, blinzeln; dunkel …; Nebel, Wolke\\\"' (246f., av. maēγa-, npers. miza). Closes the 'harnen' article with 'S. … bes. Kern IF. 4, 106f. (hier Scheidung von meigh- \\\"flimmern; dunkel, Wolke\\\")' — i.e. the books Nourai cites separate what his root box joins.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. mēḱ-, miKso, miks-\", \"stance\": \"partial\", \"note\": \"Mann keeps them apart too: 'mēK- (meKs-, meKst-, méKsl-) \\\"dung, filth\\\" … Go. maihstus \\\"dung\\\"' vs 'miKso, iō … \\\"mix, confuse, stir\\\". WP II, 244 … Lat. misceo, ere'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.65 (pp. 273-274) and 4.66 (pp. 274-275)\", \"stance\": \"supports\", \"note\": \"'4.65 URINATE; URINE … Av. miz-; maēsma-, maēsman-' and '4.66 … Goth. maihstus, OE meox, ME mix, Du. mest, OS, OHG, MHG, NHG mist: ON miga, OE migan, etc. \\\"mingere\\\" (4.65), hence orig. \\\"liquid excrement\\\"'.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. misceo\", \"stance\": \"supports\", \"note\": \"'Racine *meik- avec doublet *meig-' — confirms Nourai's double heading 'Meig, Meik' for the mix root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"minašti; vi-maik, vi-minašti\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Avestan verb for 'to mix' is myas- / mis-, Proto-Iranian *maiǰ (Cheung 2007: 261) < PIE *meyḱ(-s)-/*meyǵ(-s)- (LIV 429, Pok. 714), cognate with Skt. mekṣ- 'to mix', mimikṣ-, miśra- 'mixed', Lat. misceō, Gk. μίγνυμι. Nourai's 'minašti' is Pokorny's citation form ('Avestan minasti \\\"mixes\\\"', IEW 714); the actually attested Avestan form is the 2sg. subjunctive minaš (Y 46.14, Bartholomae AiW 1189 s.v. myas- 'mischen', translating 'die du im selben Haus (mit dir) vereinigen sollst'), beside ham-myāsaite 'they mix together' (Y 33.1) and the derivatives mišti 'in Mischung, durcheinander' and misvan- 'die Gemischten enthaltend'. So the -šti of 'minašti' is a normalised 3sg. of the nasal present *mi-na-k-ti, not a citation from a text. The second word, 'vi-maik / vi-minašti', is NOT an attested Avestan form at all: it is the reconstructed Old Iranian preverb compound *vi-maik-/*ui-maiǰ- that underlies MP gumēxtan (Nyberg, Manual II 90: 'gumēxtan … < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gwmyxtn'), and Mo'in repeats exactly this in his footnote to گمیختن (BQT 1835: «پهلوی gumēxtan (مخلوط کردن)، ایرانی باستان *vi-maik-‌ … نیبرگ ص ۸۹»). Verdict plausible: the derivation is right, but the language label on the second word should be Old Iranian (reconstructed), not Avestan; and Cheung prefers *ui-maiǰ (root variant *meiǵ-) to Nyberg's *maik-.\",\n          \"derivation_fa\": \"ستاک اوستایی «آمیختن» myas-/mis- است، از ایرانی باستان *maiǰ و در نهایت از هندواروپایی آغازین ‏*meyḱ(-s)-/*meyǵ(-s)-، هم‌ریشه با سنسکریت mekṣ- و miśra- «آمیخته»، لاتین misceō و یونانی mígnymi. صورت minašti که نورایی آورده، صورتِ سرواژهٔ پوکورنی (ص ۷۱۴) است؛ آنچه در متن اوستا آمده minaš (یسنا ۴۶.۱۴) و hem-myāsaite (یسنا ۳۳.۱) است — بارتولومه در فرهنگ ایرانی باستان (ستون ۱۱۸۹) همین را زیر myas- «مخلوط کردن» آورده است. اما «vi-maik / vi-minašti» به‌هیچ‌روی صورت اوستایی نیست؛ این صورتِ بازسازی‌شدهٔ ایرانی باستان *vi-maik- است که نیبرگ (کتابچهٔ پهلوی، بخش دوم، ص ۹۰) و به‌پیروی از او معین در حاشیهٔ برهان قاطع (ص ۱۸۳۵) برای «گمیختن» پهلوی gumēxtan داده‌اند. پس ریشه‌شناسی نورایی درست است ولی برچسبِ زبانِ واژهٔ دوم باید «ایرانی باستان (بازسازی)» باشد نه «اوستایی»؛ چونگ نیز به‌جای *maik- گونهٔ *maiǰ (< *meiǵ-) را ترجیح می‌دهد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-\",\n            \"https://en.wiktionary.org/wiki/آمیختن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:714\", \"status\": \"supports\", \"note\": \"POK_full.txt, Root/lemma meiḱ- 'to mix, stir', Page(s): 714: 'Old Indic mekṣayati, mimikṣe \\\"stirs, mixes\\\", miśra- \\\"mixes\\\" …; Avestan minasti \\\"mixes\\\", misvan- \\\"containing the composite\\\"; myasaite \\\"sie mischen sich\\\"'. Nourai's 'minašti' is this line verbatim.\"},\n            {\"ref\": \"BQT:1835\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1835 (v3 pdf p.632), footnote to گمیختن: «گمیختن … از گمیخ (= گمیز) + تن (پسوند مصدری): پهلوی gumēxtan (مخلوط کردن)، ایرانی باستان *vi-maik- … نیبرگ ص ۸۹» — Nourai's 'vi-maik' comes straight from this footnote.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1188-1190, s.v. myas-\", \"stance\": \"partial\", \"note\": \"'g. myas- V. \\\"mischen\\\". Praes. 4 myāsa- … yə̄ṇg-stā mazdā hadəmōi minaš ahurā \\\"die du im selben Haus (mit dir) vereinigen sollst\\\" Y.46.14'; also 'mišti Adv. \\\"(in Mischung sva.) durcheinander\\\"' and 'misvan- Adj. \\\"die Gemischten enthaltend\\\" … Ableit. aus *mišva- Adj. \\\"gemischt\\\", zum V. myas-'. Bartholomae has no lemma minašti and no Avestan vī-mik-: the attested form is minaš.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *maiǰ¹ 'to mix, mingle' (p. 261)\", \"stance\": \"partial\", \"note\": \"'*maiǰ¹ \\\"to mix, mingle\\\" … (+ *ā-) BMP ʾmyc- /āmēz-/ \\\"to mix\\\" … (+ *ui-) BMP gwmyc- /gumēz-/ \\\"to mix, mingle\\\" … PIE *meik(-s)-, *meig(-s)- \\\"to mix, to mingle\\\" ⇒ LIV: 429 | Pok.: 714' and 'Most Iranian forms apparently derive from the (IE) root variant *meig-'. Confirms the *ui- compound but prefers *maiǰ to Nyberg's *maik-.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, p. 90 s.v. gumēxtan; p. 13 s.v. āmēk\", \"stance\": \"supports\", \"note\": \"p.90: 'gumēxtan … < *vi-maik-, vi-maic-; MPrth wmyxtn; MPrs gwmyxtn, pres. intrans. gwmyas-, v.n. gwmyzysn (S), gwmyg \\\"mixture\\\" (A-H II) confirming -k as the final cons. of the root'; s.v. āmēk he argues 'gumēxtan … proves that the root was *maik- and not maig-'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 51, p. 12\", \"stance\": \"supports\", \"note\": \"'aw. vergl. hem-myāsaite \\\"sie mischen sich zusammen\\\", minaš \\\"du vereinst\\\" (Bartholomae, Ar. Forsch. III, 61 Anm.; II 170); skr. ā + √mikṣ- (\\\"mischen\\\")'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âmîxtan «آمیختن»; gomîxtan «گمیختن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both verbs are prefixed formations on the same Iranian root *maiǰ/*maik- 'to mix'. (1) آمیختن āmīxtan < MP āmēxtan, pres. āmēz- (MacKenzie CPD 8: 'āmēxtan, āmēz- [ʾmyhtn, ʾmyc-] mix; ~išn: mixture; element'), Manichaean MP ʾ(ʾ)myz-, Parthian ʾmyj-, from Old Iranian *ā-maiǰ- (preverb *ā- 'to, together'); the past stem in -xt goes back to *-mai(k)-ta-, the present in -z to *-maiǰ-a-, exactly the -xt/-z pair of dōxtan/dōz-. The derived noun آمیزش āmīzeš (Nourai's script extra) is the New Persian verbal noun on the present stem, continuing MP āmēzišn 'mixture'. (2) گمیختن gomīxtan 'to mix (up)' < MP gumēxtan, pres. gumēz- (MacKenzie CPD 37: 'gumēxtan, gumēz- [gwmyhtn, gwmyc-] mix; gumēzag mixture; gumēg mixture'), Parthian wmyxs-, from Old Iranian *vi-maiǰ- with the preverb *vi- 'apart, asunder' which regularly gives MP/NP gu- (cf. *vi-mārda- > gumārdan, *vi-nāsa- > gunāh). Mo'in's footnote to گمیختن (BQT 1835) analyses the prefix as pejorative («جزء اول پیشوند است بمعنی بد، ضد») and glosses the whole «لغةً بدآمیختن، مخلوط کردن، قاتی کردن». Horn (no. 51, p. 12) adds an explicit warning in a footnote that NP āmēxtan has nothing to do with NP mēxtan 'to urinate' (no. 1006) — precisely the separation Nourai's chart draws by hanging āmīxtan/gomīxtan off the Meik node and mīz/mīxtan off the Meigh 1 node. Note that گمیختن 'to mix' and گمیز 'urine' (Nourai's extra under node 5) are homophonous but etymologically distinct; the chart keeps them on the right branches.\",\n          \"derivation_fa\": \"هر دو فعل، ساخت‌های پیشوندی از یک ستاک ایرانی *maiǰ/*maik- «آمیختن»‌اند. «آمیختن» از فارسی میانهٔ āmēxtan (ستاک حال āmēz-) است — مکنزی، فرهنگ کوچک پهلوی ص ۸: «āmēxtan, āmēz- mix» — و آن از ایرانی باستان *ā-maiǰ- با پیشوند *ā-. ستاک گذشتهٔ ‎-xt از *-mai(k)-ta- و ستاک حالِ ‎-z از *-maiǰ-a- می‌آید، همان جفتِ «دوختن/دوز». اسم مصدر «آمیزش» بر ستاک حال ساخته شده و ادامهٔ āmēzišn پهلوی است. «گمیختن» از پهلوی gumēxtan (ستاک حال gumēz-) است، از ایرانی باستان *vi-maiǰ- که پیشوند *vi- در فارسی میانه و نو به گُـ بدل شده (چنانکه در «گماردن» و «گناه»). معین در حاشیهٔ برهان قاطع (ص ۱۸۳۵) جزء اول را پیشوندی به معنای «بد، ضد» می‌داند و همه را «بدآمیختن، مخلوط کردن، قاتی کردن» می‌گذارد. هرن (شمارهٔ ۵۱، ص ۱۲) در پانویس هشدار می‌دهد که «آمیختن» هیچ پیوندی با «میختن» (شمارهٔ ۱۰۰۶، شاشیدن) ندارد — و نمودار نورایی درست همین جدایی را رعایت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آمیختن\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:12\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 33 = printed p.12, no. 51: 'āmēxten \\\"mischen\\\", Praes. āmēz-em … phlv. āmēxtan, āmēxt (Bund.) \\\"mischen\\\"; aw. vergl. hem-myāsaite … skr. ā + √mikṣ-'; footnote: 'Np. āmēxten hat mit np. mēxten (No. 1006) nichts zu thun, wie Fr. Müller, WZKM. 5, 351 will.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD pp. 8 and 37\", \"stance\": \"supports\", \"note\": \"'āmēxtan, āmēz- [ʾmyhtn, ʾmyc- | M ʾmyxtn, ʾmyz-, N ~] mix. ~išn: mixture; element'; 'gumēxtan, gumēz- [gwmyhtn, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; gumēzag mixture; ~īh: the Mixture, (the duration of) this material world'. Also the reverse index: 'mixing, mixture āmēzišn, gumēzišn, gumēzag(īh), gumēg'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *maiǰ¹ (p. 261)\", \"stance\": \"supports\", \"note\": \"'(+ *ā-) NP āmēxtan/āmēz- \\\"to mix\\\", Kurd. (Sor.) āmēžān'; '(+ *ui-) BMP gwmyc- /gumēz-/ \\\"to mix, mingle\\\", MMP gwmyxs- (inch.)'; Parthian '(+ *ui-) wmyxs- (inch.) \\\"to be mixed\\\"'.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 1835 (v3 pdf 632), footnote to گمیختن\", \"stance\": \"supports\", \"note\": \"«گمیختن … پهلوی gumēxtan (مخلوط کردن)، ایرانی باستان *vi-maik- … جزء دوم بمعنی آمیختن، لغةً یعنی بدآمیختن، مخلوط کردن، قاتی کردن».\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 71 (pdf 70), s.v. آمیختن\", \"stance\": \"supports\", \"note\": \"Headword «آمیختن» with derivatives «آمیز، آمیغ، آمیزه» and the IE cognate list (Gk., Lat., OCS MĪSITI, Lith., Germanic MISCEIN/MENGEN) under the *meik- root — an independent modern Persian cross-check.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 13 s.v. āmēcišn, āmēk\", \"stance\": \"supports\", \"note\": \"'āmēcišn [ʾmycšn] mixture; the elements that constitute the human body (Arab. mizāj) … MPrs ʾmyzyšn … from MPrth/MPrs ʾmyxtn / ʾmyxs- \\\"to mix\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"maĕz\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Young Avestan maēz- is a verb, 'to urinate', not a noun 'urine': Bartholomae AiW 1108 'j. ¹maēz- V. \\\"harnen\\\". Praes. 3 maēza-', with attested forms maēzəṇti (V 3.6), framaēzaiti 'to urinate forth' (V 18.40), maēzaiianta (V 8.13). The Avestan NOUNS for 'urine' are maēsma- m. and maēsman- n. (AiW 1108-1109, 'Harn, als rituelles Reinigungs- und als Heilmittel verwendet' — the gōmaēza- of the Vidēvdād purification rites). So the chart's gloss 'urine' belongs to maēsma(n)-, while maēz- means 'to urinate'; the root and the branch are otherwise entirely correct. The chain is PIE *h₃meyǵʰ- (LIV 301f., Pok. 713) > PIr. *Hmaiz > YAv. maēz-, cognate with Skt. mehati 'urinates', méha- 'urine', Arm. mizem / mēz, Gk. ὀμείχειν, Lat. meiō/mingō, OE mīgan, Lith. mỹžti, Toch. B miso. Verdict plausible only because of the part-of-speech/gloss slip.\",\n          \"derivation_fa\": \"maēz- در اوستای نو ستاکِ فعلی است به معنای «شاشیدن، ادرار کردن»، نه اسم «ادرار»: بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۰۸) می‌نویسد «j. ¹maēz- V. harnen. Praes. 3 maēza-» و صورت‌های maēzəṇti و framaēzaiti را از ویدیوداد گواه می‌آورد. اسمِ «ادرار» در اوستا maēsma- و maēsman- است (همان gōmaēza- «میزِ گاو» در آیین‌های پاک‌سازی). پس معنایی که نورایی زیر maēz نوشته («urine») در واقع از آنِ maēsma(n)- است، هرچند خودِ ریشه و شاخه بی‌گمان درست است. زنجیره چنین است: هندواروپایی آغازین ‏*h₃meyǵʰ- ← ایرانی آغازین *Hmaiz ← اوستایی maēz-، هم‌ریشه با سنسکریت mehati، ارمنی mizem/mēz، یونانی omeíkhein، لاتین meiō/mingō و انگلیسی کهن mīgan. حکم: با احتیاط پذیرفتنی است (خطا تنها در نقشِ دستوری و معنای واژه است).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meyǵʰ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:713\", \"status\": \"supports\", \"note\": \"POK_full.txt, Root/lemma meiǵh- 'to urinate', Page(s): 713: 'Old Indic mehati \\\"urinates\\\" … meha- m. \\\"urine\\\"; Avestan maēzaiti \\\"urinates, dungs, manures\\\", maēsman- \\\"urine\\\"; Armenian mizem …; Latin meiō, -ere, mixi, mictum'. Note Pokorny too gives maēzaiti as a verb and maēsman- as the noun.\"},\n            {\"ref\": \"BQT:62\", \"status\": \"not_found\", \"note\": \"BQT vol.1 printed p.62 (= BQT_v1_pages.txt leaf 272, pinned by the catch-line «بقیه از صفحهٔ ۶۶» on leaf 277) is the آموده / آموزگار / آمون / آموی / آمه / آمیز page — i.e. the MIX branch, with «آمیز … بمعنی آمیختن دو چیز با زیاده بهم». There is nothing about urine on that page; the citation looks displaced (it fits node 1/2, not this node). No scan of BQT covers a second p.62.\"},\n            {\"ref\": \"SYN:273\", \"status\": \"supports\", \"note\": \"SYN.txt: section '4.65 URINATE; URINE' begins on printed p.273 and lists 'Av. miz-; maēsma-, maēsman-' in the table column, with the commentary 'Skt. mih-, Av. miz- (with maēsma- \\\"urine\\\")'. Buck likewise treats maēz-/miz- as the verb and maēsma(n)- as the noun.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1108 s.v. ¹maēz-; cols. 1107-1108 s.v. maēsma-, maēsman-\", \"stance\": \"partial\", \"note\": \"'j. ¹maēz- V. \\\"harnen\\\". Praes. 3 maēza- … yat̰ iš paiti frastərət̰əm maēzəṇti pasvasca staorāca V.3.6 … mit fra \\\"nach vorne pissen vor —\\\" … ai. mīhati, np. mēzad. — Pū.: mēzītan'; and 'j. maēsma- m. \\\"Harn\\\", als rituelles Reinigungs- und als Heilmittel verwendet', 'j. maēsman- n. \\\"Harn\\\"'. Supports the derivation, contradicts the gloss 'urine' for maēz-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hmaiz 'to urinate' (p. 179ff.)\", \"stance\": \"supports\", \"note\": \"'*Hmaiz \\\"to urinate\\\" — *AVESTAN: Y Av. maez- \\\"to urinate\\\" || (+ *fra-) \\\"to pee forward, forth\\\" … Pres. them.: IND. 3sg. YAv. framaēzaiti (V 18.40), 3pl. YAv. maēzəṇti (V 3.6) … «PIE *H₃meiǵʰ- \\\"to urinate\\\" ⇒ LIV: 301 f. | Pok.: 713'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. micturition\", \"stance\": \"supports\", \"note\": \"'L. micturire … rel. to meiere (for *meighiere) … and cogn. with OI. mehati \\\"urinates\\\", pp. mīḍháh, Avestic maezaiti \\\"urinates, manures, dungs\\\", Gk. ὀμείχειν … Arm. mez \\\"urine\\\", mizem \\\"I urinate\\\" … Toch. B miso \\\"urine\\\" … Goth. maihstus, OE. meox \\\"dung, filth\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 245\", \"stance\": \"supports\", \"note\": \"'meigh- \\\"harnen\\\" (Praes. meigho und mingho). Ai. mehati \\\"harnt\\\" … av. maezaiti \\\"harnt, düngt\\\", maēsma-, maēsman- \\\"Harn\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"myz`y\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian myzʾy /mēzē/ 'urine' (Sutra and Buddhist Sogdian) is the regular Sogdian noun on the same Iranian root *Hmaiz- as Avestan maēz-; Gharib's Sogdian Dictionary entry 5674 (p. 227) explicitly derives it from Avestan maēz- and compares MP mēz. Formally it is a *-ya-/-ā- stem *maiza-ka- > mēzē with the usual Sogdian loss of final syllables and -ē < *-aya-; Henning (BSOAS 1946: 718) first read the word, and Sims-Williams (BSOAS 1991: 490) confirmed the reading against the Christian Sogdian material. The arrow Avestan maēz- → Sogdian myzʾy is therefore not 'descent' in the narrow sense (Sogdian does not come from Avestan) but the usual chart shorthand for 'both continue the same Old Iranian root'; taken that way it is correct.\",\n          \"derivation_fa\": \"واژهٔ سغدی myzʾy /mēzē/ «ادرار» صورتِ سغدیِ همان ستاک ایرانی *Hmaiz- است که اوستایی maēz- از آن آمده. قریب در فرهنگ سغدی (مدخل ۵۶۷۴، ص ۲۲۷) خودِ او این واژه را به اوستایی maēz- بازمی‌گرداند و با mēz فارسی میانه می‌سنجد: «meze ©Av. maez; MP /mz — urine». از نظر ساخت، ‎-ē پایانی از *-aya- سغدی است. خوانش واژه نخست از هنینگ (۱۹۴۶) و سپس تأیید سیمز-ویلیامز (۱۹۹۱) است. پیکانِ «اوستایی ← سغدی» در نمودار را باید به معنای «هم‌ریشه از یک ستاک ایرانی باستان» خواند، نه گرفتنِ سغدی از اوستایی؛ با این تعبیر ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:227\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 293 = printed p. 227 (printed ≈ leaf − 66), entry '5674 myzʾy S, B | meze ©Av. maez; MP /mz | urine | Hen. BSOAS 1946, 718, TSP 2.299, myn'y; S W, BSOAS 1991, 490'. Nourai's SOD:227 is therefore a page, not an entry number, and it is the right page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hmaiz (p. 179ff.)\", \"stance\": \"partial\", \"note\": \"Cheung lists Choresmian myz- 'to urinate, piss', Khotanese mīysai 'urine', MP mēz-, but does not itemise the Sogdian noun; his Sogdian entries for this family are the *ni-maiǰ 'blink' ones (BSogd. nymz-). Silent on myzʾy specifically, so no contradiction.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. biysma, phiysgūna-\", \"stance\": \"supports\", \"note\": \"'biysma \\\"urine\\\" … See cognates s.v. miysai, and note three initials miysai, biysma, phiysgūna- \\\"bladder\\\" … IE. Pok. 713 meiǵh-' — the Khotanese member of the same set, referred to Pokorny 713 exactly as here.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.65 p. 273\", \"stance\": \"supports\", \"note\": \"Buck's Iranian column for 4.65 is 'Av. miz-; maēsma-, maēsman-'; the whole East-Iranian set (Oss. mizyn, Sogd., Khot.) belongs here.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"mîz «میز»; mîxtan «میختن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP میختن mīxtan / میزیدن mēzīdan 'to urinate' and the noun میز mēz 'urine' continue MP mistan, pres. mēz- (MacKenzie CPD 56: 'mistan, mēz- [mstn, myc- | N mēzīdan] urinate; ~išn(īh): urination'), from Old Iranian *maiz-, Av. maēz-, PIE *h₃meyǵʰ-. Mo'in's footnote to میختن (BQT 2073 n.9) gives the chain in full: «از میخ (= میز) + تن (پسوند مصدری). تلفظ قدیم mēxtan. اوستا maēz-, maēzaiti (شاشیدن)، پهلوی mēzītan, mēzēt، هندی باستان meh-/mehati، ارمنی mizem (شاشیدن), mēz (شاش)» — i.e. past stem mēxt- < *maiz-ta- with the regular Middle/New Persian z + t > xt, present stem mēz- < *maiza-. Horn no. 1006 (p. 226) adds MP m(i)stan and the dialect forms (Kurd. mīztin/mistin, Bal. mīzay, Oss. mizyn). Of the two script extras: میزراه mīz-rāh 'urethra' is a NP compound mēz + rāh 'way' (cf. Oss. mizgæ 'urethra'); گمیز gomīz 'urine' is MP gōmēz [gwmyc] 'bull's urine' (MacKenzie CPD 37, the ritual purifier of the Vidēvdād), i.e. Av. gao-maēza- 'cow-urine' with gav- 'cow' — so Horn no. 1006 ('aw. gaomaēza-, phlv. gōmēz, arm. LW. gomēz'), while Cheung analyses NP gumiz/gumizīdan as (+ *ui-) *ui-maiz-; either way it is on the right branch here, and is NOT the homophone گمیختن 'to mix' of node 2. The verse quoted under the node («با چنین دل چه جای باران است / کابر بر تو گمیز هم نکند») is Sanā'ī of Ghazna, and Nourai took it, with the attribution, from Mo'in's footnote 5 on BQT 1835 (which cites «سنائی غزنوی ص ۷۸۶»).\",\n          \"derivation_fa\": \"«میختن»/«میزیدن» و اسمِ «میز» (= شاش) ادامهٔ فارسی میانهٔ mistan با ستاک حالِ mēz- است (مکنزی، فرهنگ کوچک پهلوی ص ۵۶: «mistan, mēz- urinate»)، از ایرانی باستان *maiz-، اوستایی maēz-، و در نهایت هندواروپایی آغازین ‏*h₃meyǵʰ-. معین در حاشیهٔ برهان قاطع (ص ۲۰۷۳، پانویس ۹) همین زنجیره را می‌دهد: «از میخ (= میز) + تن … تلفظ قدیم mēxtan. اوستا maēz-, maēzaiti (شاشیدن)، پهلوی mēzītan، هندی باستان mehati، ارمنی mizem». ستاک گذشتهٔ mēxt- از *maiz-ta- با ابدال آوایی z+t ← xt پدید آمده و ستاک حال mēz- از *maiza-. از دو واژهٔ افزودهٔ نمودار، «میزراه» ترکیب فارسیِ میز + راه است (قس اوستی mizgæ «مجرای ادرار») و «گمیز» همان gōmēz پهلوی «میزِ گاو» است، از اوستایی gao-maēza- (هرن شمارهٔ ۱۰۰۶؛ چونگ آن را *ui-maiz- می‌خواند). این «گمیز» را نباید با «گمیختن» گرهٔ پیشین (آمیختن) یکی گرفت. بیتِ زیر گره از سنائی غزنوی است و نورایی آن را با همان انتساب از پانویس معین در ص ۱۸۳۵ برهان گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meyǵʰ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1835\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1835, headword گمیز with footnote 4: «پهلوی gōmēz. رك: گمیختن. در فارسی «گمیز» با کاف ضبط کرده‌اند و اصح با گاف است»; footnote 5 is the very verse in Nourai's node: «با چنین دل چه جای باران است / کابر بر تو گمیز هم نکند. سنائی غزنوی ص ۷۸۶».\"},\n            {\"ref\": \"BQT:2073\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2073 (v4 pdf 156), footnote 9 to میختن: «از: میخ (= میز) + تن (پسوند مصدری). تلفظ قدیم mēxtan. اوستا maēz-, maēzaiti (شاشیدن)، پهلوی mēzītan, mēzēt، هندی باستان meh-, mehati، ارمنی mizem (شاشیدن), mēz (شاش)؛ کردی mīztin, mīstin، … بلوچی …».\"},\n            {\"ref\": \"MON:4493\", \"status\": \"partial\", \"note\": \"The 6-vol Amir Kabir pagination Nourai cites could not be checked (the local Mo'in is the 2-vol Adena reprint, different pagination). In that reprint (MON_part2.txt) the entry stands: «میز (mēz) (ا.) بول، شاش» — headword and gloss confirmed, and Mo'in distinguishes it from the homonym «میز» (table), which he calls probably Mongol in origin. No etymological note in the reprint, so 'partial'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD pp. 56 and 37\", \"stance\": \"supports\", \"note\": \"'mistan, ³mēz- [mstn, myc- | N mēzīdan] urinate. ~išn(īh): urination'; reverse index 'urinate gōmēz-, mistan'; 'urine mēšag, pēšyār; bull's — gūmēz, dastšōy'; 'gūmēz [gwmyc | N gūmēz] bull's urine (as ritual purifier). gūmēz- [gwmyc- | N gūmēz-] urinate'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1006, p. 226\", \"stance\": \"supports\", \"note\": \"'mēzīten (diese Infinitivform ist nicht belegt) \\\"harnen\\\", Praes. mēz-em, mezīden. aw. √maēz-, maēzəṇti \\\"harnen\\\"; phlv. mēzītan, mēzēt, m(i)stan …; ai. √meh-, mehati; arm. mizem \\\"harnen\\\", mez \\\"Urin\\\". kurd. mīztin, mistin; oss. d. mizun; bal. mizay, mēzay. Np. gumēz … \\\"Urin\\\", gumēzīden \\\"harnen\\\" (aw. gaomaēza-, phlv. gōmēz, arm. LW. gomēz-)'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hmaiz (p. 179ff.)\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP mēxtan/mēz-, Bal. mest, mezit/mež-, Kurd. mistin/miz-, Gil. dimistan/dimiz- \\\"to urinate\\\" … || (+ *ui-) NP gumizīdan/gumiz- \\\"to make water\\\", NP gumiz, (LW ?) Awrom. gumēz (m.) \\\"urine\\\"'.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol reprint), s.v. میز\", \"stance\": \"supports\", \"note\": \"«میز (mēz) (ا.) بول، شاش» — the noun and gloss Nourai gives; a separate entry «میز» (کرسی/table) is marked as probably of Mongol origin, so the homonyms are kept apart.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"maeğa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan maēγa- n. 'cloud' is well attested in the Yašts and the Yasna (Yt 5.120 'the cloud that holds the waters'; Yt 8.40 'then the clouds rise up'; Y 57.28; the derivative maēγō.kara- 'cloud-making', Yt 8.33). Bartholomae AiW 1104-1105 lists it as '¹maēγa- n. \\\"Wolke\\\"' and equates it with Skt. meghá- m. and NP mēγ, citing Horn NpEt. and ZDMG 56.117. The word goes back to PIr. *Hmaigah- < PIIr. *Hmaygʰás < PIE *h₃meygʰ- 'cloud, mist, fog' (Pok. 712 'meiǵh-, also meik-: to glimmer, twinkle; mist', section B 'dunkel vor den Augen werden, Nebel, Wolke'), with cognates Skt. meghá- 'cloud', míh- 'mist', Arm. mēg 'mist', Gk. ὀμίχλη 'cloud, mist', Lith. miglà, OCS mъgla. Bartholomae's second lemma ²maēγa- m. 'Grube, Kuhle' (V 7.37) is a different, etymologically obscure word ('Et.?') — the chart correctly takes the 'cloud' one.\",\n          \"derivation_fa\": \"maēγa- در اوستای نو اسمِ خنثی به معنای «ابر» است و در یشت‌ها و یسنا بارها آمده (یشت ۵.۱۲۰ «ابری که آب‌ها را در خود دارد»؛ یشت ۸.۴۰ «آنگاه ابرها برمی‌آیند»؛ همچنین maēγō.kara- «ابرساز» در یشت ۸.۳۳). بارتولومه (فرهنگ ایرانی باستان، ستون‌های ۱۱۰۴–۱۱۰۵) آن را «¹maēγa- n. Wolke» می‌آورد و با megháـ سنسکریت و mēγ فارسی نو یکی می‌داند و به هرن ارجاع می‌دهد. این واژه از ایرانی آغازین *Hmaigah- و در نهایت از هندواروپایی آغازین ‏*h₃meygʰ- «ابر، مه» است (پوکورنی ص ۷۱۲، بخش ب «تیرگی پیش چشم، مه، ابر»)، هم‌ریشه با míh و meghá سنسکریت، mēg ارمنی، omíkhlē یونانی و miglà لیتوانیایی. باید توجه داشت که ²maēγa- دومِ بارتولومه («گودال») واژه‌ای دیگر و بی‌ریشه‌شناسی روشن است؛ نمودار درست همان «ابر» را گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\",\n            \"https://en.wiktionary.org/wiki/میغ\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:712\", \"status\": \"supports\", \"note\": \"POK_full.txt, Root/lemma 'meiǵh-, also meik-', Meaning 'to glimmer, twinkle; mist', section 'B. with the meaning \\\"darkness before the eyes, fog, cloud\\\"': 'Old Indic megha- m. \\\"cloud\\\", mih \\\"fog, watery precipitation\\\", Avestan maēγa- \\\"cloud\\\"; Armenian meg \\\"fog\\\"; gr. ὀμίχλη …'. Page(s): 712-713.\"},\n            {\"ref\": \"BQT:2079\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2079 (v4 pdf 162), headword میغ 'ابر' with footnote 2: «اوستا maēγa- (ابر)، پهلوی mēγ، هندی باستان meghá-، ارمنی mēg (مه)، اوستی meγä, miγ (مه، ابر). اینکه «میغ» با ریشهٔ maēz- (ادرار کردن) هم‌ریشه باشد، قطعی بنظر میرسد».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1104-1105 s.v. ¹maēγa-\", \"stance\": \"supports\", \"note\": \"'j. ¹maēγa- n. \\\"Wolke\\\": … Yt 5.120; 8.33, Y.10.3; — āat̰ yaθa us-fravāṇti … \\\"dann steigen die Wolken auf, die die … Wasser enthalten\\\" Yt 8.40 … KompA. — ai. meghá- m., np. mēγ. — Pū.: undeutlich, Sū.: megha-. … HORN NpEt. 284; ZDMG. 56. 117.' Immediately after it: 'j. ²maēγa- m. \\\"Grube, Kuhle\\\" … Et.?' — a different word.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 246-247\", \"stance\": \"supports\", \"note\": \"'meigh-, auch meiq- \\\"flimmern, blinzeln; dunkel (vor den Augen flimmernd); Nebel, Wolke\\\" … B. mit der Bed. \\\"dunkel vor den Augen werden, Nebel, Wolke\\\": Ai. meghá- m. \\\"Wolke\\\", mih \\\"Nebel, Dunst, wasseriger Niederschlag\\\", av. maēγa- \\\"Wolke\\\"; arm. meg \\\"Nebel\\\"; gr. ὀμίχλη \\\"Wolke, Nebel\\\"'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *maiǰ¹ 'to blink, wink' (p. 259)\", \"stance\": \"supports\", \"note\": \"'The Ir. formation *maigá- \\\"(dark) cloud\\\" (< *\\\"which covers (the eyes)\\\"), Skt. meghá-, Y Av. maēγa-, etc., may also contain this root, on which see Cheung, Fs Klingenschmitt.' — supports the form and, incidentally, Nourai's grouping of the 'cloud' node with 'Meigh 2: to blink, cover, darken'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"Watkins has no root entry for Pok. 712 'to glimmer/mist' and no reflex of Av. maēγa-; grep for 'meigh-' finds only 'meigh-. To urinate'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"mîğ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian mēγ [myγ] 'cloud, mist' is the regular continuation of Old Iranian *maigah- (Av. maēγa-): the intervocalic/final Old Iranian *-g- appears in Middle and New Persian as the fricative γ (Hübschmann, Persische Studien §139, p. 247: 'Ap. g nach Vokalen und r = γ bleibt im Np. als γ: … mēγ \\\"Wolke\\\" = zd. maēγa-', beside murγ, marγ, druγ), and the Avestan thematic ending *-a- is lost. MacKenzie CPD 55 records it as 'mēγ [myγ | P myg, N ~] cloud, mist', and the Manichaean Parthian equivalent is myg (whence, per Wiktionary, the NP form may in part be Parthian-mediated). MacKenzie also has *miznē 'mist, dew' from the same family. The Pahlavi Vidēvdād gloss to V 15(18) uses mēγ for Avestan maēγa-, which is Horn's evidence at no. 1009.\",\n          \"derivation_fa\": \"mēγ فارسی میانه «ابر، مه» ادامهٔ منظمِ *maigah- ایرانی باستان (اوستایی maēγa-) است: g ایرانی باستان پس از واکه در فارسی میانه و نو به سایشیِ غ بدل می‌شود — هوبشمان در «پژوهش‌های فارسی» بند ۱۳۹ (ص ۲۴۷) همین را می‌گوید: «mēγ \\\"ابر\\\" = زند maēγa-»، در کنار مرغ، مرغ (چمن)، دروغ — و پایانهٔ ‎-a- اوستایی می‌افتد. مکنزی (فرهنگ کوچک پهلوی ص ۵۵) آن را «mēγ [myγ] cloud, mist» ثبت کرده و برابر پارتی مانوی myg است. زندِ پهلویِ ویدیوداد نیز maēγa- اوستایی را به mēγ برگردانده و همین گواهِ هرن در شمارهٔ ۱۰۰۹ است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/میغ\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:285\", \"status\": \"not_checked\", \"note\": \"ISS = Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis), Cambridge 1967 — not available online (Google Books preview only, HathiTrust search-only). The substitute on disk, Bailey's Dictionary of Khotan Saka, has no entry for MP mēγ (Khotanese 'cloud' is pryaurā-/pyaura-, DKS s.v.), so p. 285 of ISS could not be verified either directly or by proxy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p. 55 (leaf 79)\", \"stance\": \"supports\", \"note\": \"'mēγ [myγ | P myg, N ~] cloud, mist.' Reverse index p. 218: 'mist mēγ, miznē'; also '*miznē [m(y)znydy] mist, dew'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1009, p. 226\", \"stance\": \"supports\", \"note\": \"'mēγ \\\"Wolke\\\". aw. maēγa- \\\"Wolke\\\"; phlv. mēγ, vd. 15 (18); ai. meghá-; arm. mēg \\\"Nebel\\\" (H. No. 197). oss. d. meγä, t. miγ \\\"Nebel, Wolke\\\" (185).' — the Pahlavi form with its Vidēvdād reference.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary covers only the texts of Part I; grep for mēγ/myγ finds no entry (the word does not occur in his selection), so no evidence either way.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §139, p. 247\", \"stance\": \"supports\", \"note\": \"'Ap. g nach Vokalen und r = γ bleibt im Np. als γ: murγ \\\"Vogel\\\" = zd. mərəγa-; marγ \\\"Wiese\\\" …; muγ, maγ \\\"Magier\\\" = ap. magu-; mēγ \\\"Wolke\\\" = zd. maēγa-' — the sound law that carries maēγa- to mēγ.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"mîğ «میغ»; meh 1 «مه ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"(1) میغ mēγ/mīγ 'cloud' (archaic and poetic; the Ferdowsī verse quoted in Borhān, «همانا که باران نبارد ز میغ …», and the Asadī verse Nourai prints) is MP mēγ continued unchanged into New Persian, with the later Iranian-Persian raising of ē > ī that gives the modern pronunciation mīγ. Mo'in's footnote (BQT 2079 n.2) gives the whole chain: «اوستا maēγa- (ابر)، پهلوی mēγ، هندی باستان meghá-، ارمنی mēg، اوستی meγä/miγ». (2) مه meh 'fog, mist' is the same word after the loss of the final fricative: NP -γ is regularly dropped in this position (cf. Wiktionary, which lists مه as a cognate/doublet of میغ), so *mēγ > meh with the -h a mere orthographic prop for the final vowel; Persian dictionaries accordingly keep مه 'fog' apart from the homographs مه 'moon' (< māh) and مه 'greater' (< MP mas/meh). Aryanpur's Persian IE-root dictionary heads the whole family «مه، میغ (به چم ابر، سحاب)» — treating exactly these two Persian words as one entry, as Nourai does.\",\n          \"derivation_fa\": \"«میغ» همان mēγ فارسی میانه است که بی‌تغییر به فارسی نو رسیده و تنها با کشیدگیِ متأخر ē ← ī به تلفظ امروزی mīγ درآمده؛ در شعر کهن فراوان است (بیت فردوسی در برهان: «همانا که باران نبارد ز میغ …» و بیت اسدی که نورایی آورده). معین در حاشیهٔ برهان (ص ۲۰۷۹) زنجیره را کامل می‌دهد: «اوستا maēγa-، پهلوی mēγ، هندی باستان meghá-، ارمنی mēg، اوستی meγä/miγ». «مه ۱» به معنای «مه، غبار» نیز همان واژه است پس از افتادن غِ پایانی؛ ویکی‌واژه «مه» را دوگانهٔ «میغ» می‌شمارد. این «مه» را نباید با «مه» (ماه) و «مه» (بزرگ‌تر، از مسِ پهلوی) یکی گرفت. آریان‌پور نیز در فرهنگ ریشه‌های هندواروپایی، مدخل را «مه، میغ (به چم ابر، سحاب)» گذاشته است — درست همان جفتی که نورایی در یک گره آورده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/میغ\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:226\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 247 = printed p.226, no. 1009: 'mēγ \\\"Wolke\\\". aw. maēγa- \\\"Wolke\\\"; phlv. mēγ, vd. 15 (18); ai. meghá-; arm. mēg \\\"Nebel\\\"'. Horn adds: 'Dass mēγ mit √meiǵh- \\\"harnen\\\" (1006) zusammen gehört, scheint sicher zu sein, vergl. zuletzt Bechtel, Hauptprobleme S. 373' — Horn himself endorses the very lumping of Meigh 1 with Meigh 2 that the root box implies.\"},\n            {\"ref\": \"ISS:285\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies VI not available (see node 7); the substitute DKS has no NP mēγ/meh entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"p. 2079 (v4 pdf 162), s.v. میغ + footnotes 2-3\", \"stance\": \"supports\", \"note\": \"Headword «میغ … بشار [ابخار] را گویند تیره و ملاصق زمین - و بمعنی ابر هم آمده است که عربان سحاب خوانند»; footnote 2 «اوستا maēγa- (ابر)، پهلوی mēγ …»; footnote 3 quotes Ferdowsī from Loghat-e Fors: «همانا که باران نبارد ز میغ / فزون زانکه بارید برسرش تیغ».\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §139, p. 247\", \"stance\": \"supports\", \"note\": \"'mēγ \\\"Wolke\\\" = zd. maēγa-' in the list of NP γ < Old Persian/Avestan g.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur pp. 483-484 (pdf 483), s.v. مه / میغ\", \"stance\": \"supports\", \"note\": \"Headword «مه میغ (به چم \\\"ابر\\\" \\\"سحاب\\\")» with Avestan MAEΓA, Pahlavi MEΓ, Ossetic MEΓÄ/MIΓ, Sanskrit MEGHA/MIH, Armenian MEG, Greek OMIXLI, Lithuanian MIGLA, Old Church Slavonic MĪGLA, Old English MIST, English MIST/MIZZLE, and a citation to برهان قاطع — an independent modern Persian source giving Nourai's exact pair مه/میغ.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p. 55\", \"stance\": \"supports\", \"note\": \"'mēγ [myγ | P myg, N ~] cloud, mist' — the 'N ~' means the New Persian form is identical, i.e. میغ.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"možeh, možgân «مژه ، مژگان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"مژه može (older miža/muža) 'eyelash', pl. مژگان možgān, goes back to MP mij(ag) [myc(k)] 'eyelid, eyelash' (MacKenzie CPD 56), i.e. *mičaka- with the common diminutive/nominal suffix -aka- > NP -a; Hübschmann Persische Studien §19 (p. 137) states the form outright — 'miža = muža \\\"Augenwimper\\\" aus *mičak, vgl. bal. mičāč' — and repeats it at pp. 226-227 with the plural: 'muža, pl. možgān \\\"Augenwimper\\\", bal. mičāč'. The plural مژگان preserves the older stem-final consonant (možg- < *mičak- + -ān), exactly as ستارگان/بندگان preserve MP -ak. The root is PIE *meyǵ(ʷ)ʰ- 'to blink, cover (the eyes)' (Nourai's 'Meigh 2'), PIr. *maiǰ 'to blink, wink' (Cheung 2007: 258-259), whence also BMP mēzišn 'blinking, winking', Sogdian mizā/muzā 'eyelash', Skt. miṣ- 'to wink', Lith. miẽgas 'sleep', OCS *měžiti 'to close the eyes', Lat. micāre. Mo'in (BQT 2006 n.1) gives Pahlavi mičak, Kurdish mižūlānk, Balochi mičāč and refers to Hübschmann p. 980[= §/p. ref], and explicitly rejects the folk analysis as مو 'hair' + diminutive: «بعضی معاصران آنرا از مو … دانسته‌اند ولی بر اساسی نیست» — the same alternative Wiktionary still records as a minority view.\",\n          \"derivation_fa\": \"«مژه» (صورت کهن‌تر miža/muža) و جمعِ آن «مژگان» از mij(ag) فارسی میانه [myc(k)] «پلک، مژه» می‌آید (مکنزی ص ۵۶)، یعنی از *mičaka- با پسوند ‎-aka- که در فارسی نو به ‎-ه بدل شده؛ هوبشمان در «پژوهش‌های فارسی» بند ۱۹ (ص ۱۳۷) صریحاً می‌نویسد: «miža = muža، مژه، از *mičak، قس بلوچی mičāč» و در ص ۲۲۶–۲۲۷ با جمع نیز می‌آورد. «مژگان» همخوانِ پایانیِ ستاک کهن را نگه داشته (možg- < *mičak- + ‎-ān)، همان‌گونه که «ستارگان» و «بندگان» ‎-ak پهلوی را نگه داشته‌اند. ریشه هندواروپایی آغازین ‏*meyǵ(ʷ)ʰ- «پلک زدن، پوشاندن چشم» است — همان «Meigh 2» نورایی — و در ایرانی آغازین *maiǰ «پلک زدن» (چونگ ص ۲۵۸–۲۵۹)، که mēzišn پهلوی «پلک زدن»، mizā/muzā سغدی «مژه»، miṣ- سنسکریت و micāre لاتین نیز از آن‌اند. معین در حاشیهٔ برهان (ص ۲۰۰۶، پانویس ۱) پهلوی mičak، کردی، افغانی و بلوچی mičāč را می‌آورد و ریشه‌شناسی عامیانهٔ «مو + پسوند» را رد می‌کند: «بعضی معاصران آنرا از مو … دانسته‌اند ولی بر اساسی نیست». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/مژه\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:712\", \"status\": \"supports\", \"note\": \"POK_full.txt, Root/lemma 'meiǵh-, also meik-', Page(s) 712-713, section '2. meik-': 'Npers. miza, muza (Pahlavi *mičak), baluči mičāč \\\"eyelash\\\"; Latin mico, -are \\\"to move quickly to and fro, vibrate, quiver …\\\"'. Nourai's možeh sits exactly here.\"},\n            {\"ref\": \"HRN:219\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 240 = printed p.219, no. 980: 'miže, muže \\\"Augenwimper\\\", HJD (Jer. 9, 18). g. mūjeng; Käs. mejä, mujd, mezi' — continued on p.220: 'kurd. mižīnk, mizī, mužūal \\\"Augenwimpern\\\"; bal. mičāč … ai. nimiṣ \\\"Blinzeln, Zwinkern des Auges\\\"'.\"},\n            {\"ref\": \"BQT:2006\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2006 (v4 pdf 89), headword «مژه … معروف است که موی پلک چشم باشد و آنرا مژگان هم میگویند», footnote 1: «پهلوی mičak، کردی mižūlānk … بلوچی mičāč … قس: هندی باستان [nimiṣ] (چشمک زدن)، سانسکریت … هوبشمان ۹۸۰ … بعضی معاصران آنرا از م[و] … دانسته‌اند ولی بر اساسی نیست»; then the two Farroxī verses with مژه.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §19 p. 137 and pp. 226-227\", \"stance\": \"supports\", \"note\": \"p.137: 'miža = muža \\\"Augenwimper\\\" aus *mičak, vgl. bal. mičāč'; p.226f.: 'muža, pl. možgān \\\"Augenwimper\\\", bal. mičāč, also phl. *mičak'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *maiǰ¹ 'to blink, wink' (pp. 258-259)\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: BMP mycšn /mēzišn/ \\\"blinking, winking\\\", myc(k) /mij(ag)/ \\\"eyelid, eyelash\\\" … *NWIR: NP muže, meže \\\"eyelash\\\" … «PIE *mei-ǵ/ǵʷʰ- \\\"to blink, cover (the eyes)\\\" ⇒ LIV: 427 | Pok.: 712 f., 714'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p. 56\", \"stance\": \"supports\", \"note\": \"'mij(ag) [myc(k) | N muž(a)] eyelid; eyelash'; also '*mēzišn [mycšn] blinking, twinkling' (reverse index p.211 'blinking mēzišn', p.226 'twinkling mēzišn').\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib p. 227, entry 5676\", \"stance\": \"supports\", \"note\": \"'5676 mzʾ M, S | mizā ?, muzā ©f. nom. sg. mi/uz-ī ob. ~y | eyelash | Hen. Sogdica. 4, 1 f. n 1; S W, BSOAS 1991, 492, muzayi' — the Sogdian cognate of مژه, on the very page Nourai cites for node 4.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 472 (pdf 471), s.v. مژه / مژگان\", \"stance\": \"supports\", \"note\": \"Headword «مژه مژگان» with Pahlavi MIJ, Kurdish and Old Irish cognates and a reference to لغت‌نامه دهخدا ۳۷۴۶ — independent confirmation of MP mij.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 247\", \"stance\": \"supports\", \"note\": \"'Wzf. meiq-: … lat. mico, -are \\\"schimmern; sich zuckend oder zitternd hin und her bewegen\\\"; baluči mičāč, npers. miža (pehl. *mičah) \\\"Augenwimper\\\" (Liden IF. 19, 333 f.)'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"miscĕre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin misceō, -ēre, -uī, mixtum 'to mix, mingle, blend' is old (Ennius, Plautus) and is built on a *-sk̑e/o- present: *mi-k-skō > misceō, i.e. the zero grade *mi- of *meyḱ- plus the inchoative/iterative suffix -sk-, exactly as in poscō < *pṛk-skō. Ernout-Meillet (s.v. misceō) state 'Racine *meik- avec doublet *meig-: skr. miśráh et lit. mišrus \\\"mêlé\\\"'; Watkins/AHD file it as 'Suffixed zero-grade form *mik-sk- in Latin miscēre (past participle mixtus), to mix'. The past participle mixtus (older mistus) with its -t- is the source of most of the Romance and English derivatives. Cognates: Skt. mekṣáyati, Gk. μίγνυμι/μίσγω, Av. myas-/minaš, OIr. mescaid, Lith. miešiù, OCS měsiti.\",\n          \"derivation_fa\": \"لاتین misceō, -ēre «آمیختن» واژه‌ای کهن است (اِنیوس، پلاؤتوس) و بر ستاک حالِ ‎*-sk̑e/o- ساخته شده: *mi-k-skō ← misceō؛ یعنی درجهٔ صفرِ ریشهٔ ‏*meyḱ- به‌همراه پسوند ‎-sk-، همان‌گونه که poscō از *pṛk-skō. اِرنو-میه در ذیل misceō می‌نویسد: «ریشه *meik- با گونهٔ دوگانهٔ *meig-: سنسکریت miśráh و لیتوانیایی mišrus «آمیخته»». واتکینز نیز آن را «صورت درجه‌صفرِ پسوندی *mik-sk- در لاتین miscēre» می‌داند. صفت مفعولی mixtus (کهن‌تر mistus) سرچشمهٔ بیشترِ مشتق‌های رومانسی و انگلیسی است. هم‌ریشه‌ها: mekṣáyati سنسکریت، mígnymi/mísgō یونانی، myas- اوستایی و měsiti اسلاوی کهن. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mix\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meyḱ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. 'meik-. To mix': '2. Suffixed zero-grade form *mik-sk- in Latin miscēre (past participle mixtus), to mix: MEDDLE, (MEDLEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. [Pok. meik- 714.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. misceo\", \"stance\": \"supports\", \"note\": \"'misceo, -es, -ui, mixtum, -ere: mêler, mélanger. Ancien (Enn., Pl.), usuel … Racine *meik- avec doublet *meig-: skr. miśráh et lit. mišrus \\\"mêlé\\\"; fournissait sans doute un présent radical athématique …'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 714\", \"stance\": \"supports\", \"note\": \"'Latin misceo, -ere \\\"mix, mingle, intermingle, blend\\\" (extension from mi[k]-skō)' under Root/lemma meiḱ- 'to mix, stir'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. miKsō, iō\", \"stance\": \"supports\", \"note\": \"'miKsō, iō (miKskō, mimiKs-, beside miks-, misk-, etc.) \\\"mix, confuse, stir\\\". WP II, 244. Skt. cf. mímikṣāmi …; Gk. cf. mísgō …; Lat. misceo, ere, id.; OIr. mescaim …; OHG miskan, OE miscian'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 244-245\", \"stance\": \"supports\", \"note\": \"'lat. misceo, -ere \\\"mischen\\\" (Erw. von mi[k]-sko, Brugmann II 3, 262) … air. commescatar \\\"miscentur\\\" … cymr. mysgu \\\"mischen\\\"; ahd. miskan, ags. miscian \\\"mischen\\\" (eher lat. Lw. als urverwandt)'.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"mix, miscellaneous\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words go back to Latin miscēre, but by different routes. mix (verb, 1530s) is a back-formation from Middle English myxte / mixt (early 15c.) 'mixed', which came through Anglo-French from Latin mixtus, pp. of miscēre; Klein notes that the -t of mixture 'is organic (it represents L. t in mixtus)'. Etymonline adds that the verb was rare before the Elizabethan period, probably because it collided with the unrelated Middle English mixen 'dung-hill' and mixed 'foul, filthy' — which belong to the OTHER root on this page, *h₃meyǵʰ- 'to urinate' (Klein s.v. mixen: 'ME., fr. OE., \\\"dung, dunghill\\\", rel. to OE. meox … Goth. maihstus'). miscellaneous (1630s) is a learned borrowing straight from Latin miscellāneus 'mixed', from miscellus 'mixed', from miscēre (Klein s.v.). The chart's arrow Latin miscēre → English mix, miscellaneous is therefore right, with Anglo-French/Old French as an unstated intermediate for mix.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی به لاتین miscēre بازمی‌گردند، ولی از دو راه. mix (فعل، دههٔ ۱۵۳۰) گشتهٔ پس‌سازِ (back-formation) صورتِ انگلیسی میانهٔ myxte/mixt «آمیخته» است که از راه انگلونرمان از mixtus لاتین (اسم مفعولِ miscēre) وام گرفته شده؛ کلاین یادآور می‌شود که تِ mixture «اصیل است و همان t لاتینیِ mixtus را نشان می‌دهد». اتیمانلاین می‌افزاید که این فعل پیش از دورهٔ الیزابت کم‌کاربرد بود، احتمالاً از بیمِ آمیختگی با mixen «تلّ سرگین» و mixed «پلید» در انگلیسی میانه — که خودشان از ریشهٔ دیگرِ همین صفحه، ‏*h₃meyǵʰ- «ادرار کردن»، می‌آیند. miscellaneous (دههٔ ۱۶۳۰) وام‌واژه‌ای کتابی است یک‌راست از miscellāneus لاتین «آمیخته». پس پیکانِ نمودار درست است، تنها میانجیِ انگلونرمان/فرانسهٔ کهن برای mix ناگفته مانده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mix\",\n            \"https://www.etymonline.com/word/miscellaneous\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None). Checked against Klein, Skeat and Etymonline instead — see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. miscellaneous, mixed, mixture, mixen\", \"stance\": \"supports\", \"note\": \"'miscellaneous, adj., mixed, consisting of various kinds. — L. miscellāneus, \\\"mixed, miscellaneous\\\", fr. miscellus, \\\"mixed\\\", fr. miscēre, \\\"to mix\\\"'; 'mixed, adj. — For mixt, fr. F. mixte. See mix'; 'mixture, n. — ME., fr. OF. misture (F. mixture), fr. L. mixtura … fr. mixtus, pp. of miscere'; and, for the collision, 'mixen, n., dunghill … rel. to OE. meox \\\"dung, filth\\\" … Goth. maihstus'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mix (Miscellaneous under Mix/mingle)\", \"stance\": \"supports\", \"note\": \"Skeat derives mix from the Latin mixtus/miscere family; his separate entry 'Mist. (E.) A.S. mist … G. mist, dung (the same word)' shows the same two-root situation Klein describes.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. mix/miscellaneous\", \"stance\": \"silent\", \"note\": \"Not consulted in detail; the chain Latin > Anglo-French > English is uncontroversial and covered by Klein and Etymonline (per the instruction that one good source suffices for a well-known Latin-to-English chain).\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Germanic\",\n          \"words\": \"mih-stu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *mih-stu- is the *-stu-/-sta- derivative of the verb *mīgan 'to urinate' (< PIE *h₃meyǵʰ-), i.e. *migʰ-stu- 'urine, liquid excrement', with the regular Germanic development *gʰ + s > h + s. Its two branches of meaning are visible side by side: 'dung, filth' in Gothic maihstus, OS mehs, OHG/MHG/G mist, OE meox, mixen, and 'fine rain, mist' in OE mist, ON mistr, Du./Swed. mist. Watkins/AHD (Nourai's cited reference) states Nourai's node verbatim: 'meigh-. To urinate. 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST …' Skeat says the same: 'Mist … G. mist, dung (the same word); Goth. maihstus, dung. Formed, with suffixed -st, from the base MIC (Aryan MIGH)'. Buck 4.66 likewise: 'Goth. maihstus, OE meox, ME mix, Du. mest, OS, OHG, MHG, NHG mist: ON miga, OE migan \\\"mingere\\\" (4.65), hence orig. \\\"liquid excrement\\\"'. The reservation to record is that Klein, Pokorny (712) and Aryanpur put OE mist not here but under the 'mist, cloud' root (*h₃meygʰ-), keeping it apart from OHG mist 'dung'; Etymonline calls the connection 'perhaps' and notes some scholars posit 'a separate IE root meaning \\\"fog\\\"'. Since the root box on this page contains both Meigh 1 and Meigh 2, Nourai's chart is compatible with either analysis.\",\n          \"derivation_fa\": \"*mih-stu- ژرمنی آغازین ساختِ پسوندیِ ‎*-stu- بر ستاک فعلیِ *mīgan «ادرار کردن» (از هندواروپایی ‏*h₃meyǵʰ-) است، یعنی *migʰ-stu- «ادرار، پس‌آبِ آبکی»، با دگرگونی آواییِ منظمِ ژرمنیِ gʰ + s ← h + s. دو شاخهٔ معنایی آن در کنار هم دیده می‌شود: «سرگین، پلیدی» در گوتیک maihstus، ساکسونی کهن mehs، آلمانی کهن و آلمانیِ امروز mist و انگلیسی کهن meox/mixen؛ و «باران ریز، مه» در انگلیسی کهن mist، نورس کهن mistr و هلندی/سوئدی mist. واتکینز (همان مرجعی که نورایی داده) دقیقاً همین گره را می‌نویسد: «meigh-. ادرار کردن. ۱. صورت پسوندیِ ژرمنی *mih-stu-، ادرار، و از آنجا mist، باران ریز». اسکیت هم می‌گوید mist انگلیسی و mist آلمانی «همان یک واژه‌اند»، با پسوند ‎-st از پایهٔ MIGH. اما باید یادآور شد که کلاین، پوکورنی (ص ۷۱۲) و آریان‌پور mist انگلیسی کهن را نه اینجا بلکه زیر ریشهٔ «مه/ابر» (*h₃meygʰ-) می‌آورند و آن را از mist آلمانی «سرگین» جدا می‌کنند؛ اتیمانلاین نیز این پیوند را «شاید» می‌خواند. چون کادر ریشهٔ این صفحه هر دو Meigh 1 و Meigh 2 را دربر دارد، نمودار نورایی با هر دو تحلیل سازگار است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mist\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃meygʰ-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. 'meigh-. To urinate': '1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle … c. Germanic diminutive form *mihst-ila-, mistletoe … in Old English mistel: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in Latin micturire … [Pok. meigh- 713.]' — Nourai's node reproduces the form and both glosses ('fine rain, mist').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mist\", \"stance\": \"supports\", \"note\": \"'Mist. (E.) A.S. mist, gloom, darkness. + Icel. mistr, Du. Swed. mist; G. mist, dung (the same word); Goth. maihstus, dung. Formed, with suffixed -st, from the base MIC (Aryan MIGH), as seen in Lithuan. migla, Russ. mgla, Gk. ὀμίχλη, mist. Skt. mihira, a cloud, megha, a cloud. Cf. Skt. mih, to sprinkle, to urinate.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.66, p. 274f.\", \"stance\": \"supports\", \"note\": \"'Goth. maihstus (κοπρία), OE meox, ME mix, Du. mest, OS, OHG, MHG, NHG mist: ON miga, OE migan, etc. \\\"mingere\\\" (4.65), hence orig. \\\"liquid excrement\\\". Walde-P. 2.245f. Feist 340.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. mist\", \"stance\": \"contradicts\", \"note\": \"'mist, n. — ME., fr. OE. mist, \\\"darkness, gloom\\\", rel. to ON. mistr, Swed., MDu., Du. mist, \\\"mist\\\", fr. I.-E. base *meigh- whence also OI. meghah, \\\"cloud\\\", mih-, \\\"mist, vapor\\\", Avestic maēγa \\\"cloud\\\", Arm. meg, \\\"mist\\\", Gk. ὀμίχλη …' — Klein puts OE mist under the 'cloud/mist' root, not under the 'urinate' one, and treats OHG mist 'dung' separately (s.v. mixen).\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 245-247\", \"stance\": \"partial\", \"note\": \"Under 'meigh- \\\"harnen\\\"' (245f.): 'got. maihstus, ahd. mist, ags. miox, meox \\\"Kot, Dünger\\\"'; but under 'meigh-/meiq- \\\"Nebel, Wolke\\\"' (247): 'aisl. mistr \\\"trübes Wetter\\\" usw. vielleicht zur verw. Wz. mei-s-, oder als … hierher' — i.e. WLD hesitates over which root the 'mist' words belong to.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"mist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE mist 'darkness, gloom; mist' > ME mist > Modern English mist, from Proto-Germanic *mihstaz/*mih-stu- (Etymonline: 'from Proto-Germanic *mikhstaz, also in MLG mist, Du. mist, Icel. mistur, Norw./Swed. mist'). The Old English sense 'dimness before the eyes, gloom' is the oldest attested one; the meteorological sense 'cloud resting upon the ground, fog' broadens in Middle English to 'precipitation of fine droplets', with the figurative senses of dimness and obscurity from the 15th c. and 'haze of dust in the air' by 1785. Whether the ultimate root is *h₃meyǵʰ- 'to urinate' (Watkins, Skeat, Buck) or the separate *h₃meygʰ- 'mist, cloud' (Klein, Pokorny 712) is the open question recorded under node 12; either way English mist descends from the Germanic *mihst- noun drawn on this chart, and the arrow Germanic → English is correct.\",\n          \"derivation_fa\": \"mist انگلیسی از mist انگلیسی کهن «تیرگی، تاریکی؛ مه» و آن از *mihstaz ژرمنی آغازین است (اتیمانلاین: «از ژرمنی آغازین *mikhstaz، همچنین در آلمانی سفلای میانه mist، هلندی mist، ایسلندی mistur»). کهن‌ترین معنای گواه‌دار در انگلیسی کهن «تاری پیش چشم» است؛ معنای هواشناسیِ «ابرِ نشسته بر زمین، مه» در انگلیسی میانه گسترش می‌یابد و از سدهٔ پانزدهم معناهای مجازیِ تیرگی و ابهام و از ۱۷۸۵ «غبار معلق» پیدا می‌شود. اینکه ریشهٔ نهایی ‏*h₃meyǵʰ- «ادرار کردن» است (واتکینز، اسکیت، باک) یا ریشهٔ جداگانهٔ ‏*h₃meygʰ- «مه، ابر» (کلاین، پوکورنی ص ۷۱۲)، پرسشی است که در گرهٔ پیشین یاد شد؛ در هر دو حال mist انگلیسی از همان اسمِ ژرمنیِ *mihst- که در نمودار آمده گرفته شده و پیکانِ «ژرمنی ← انگلیسی» درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mist\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None). Checked against AHD/Watkins, Klein, Skeat and Etymonline instead — see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. meigh-\", \"stance\": \"supports\", \"note\": \"'Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST'; index p. 1875 'MIST meigh-'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. mist\", \"stance\": \"partial\", \"note\": \"Confirms OE mist > ME > NE mist and the Germanic cognates (ON mistr, Swed./MDu./Du. mist), but assigns the base to *meigh- 'cloud/mist' (with OI meghah, Av. maēγa, Gk. ὀμίχλη) rather than to the 'urinate' root.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mist, mistletoe, mizzle\", \"stance\": \"supports\", \"note\": \"'Mist. (E.) A.S. mist, gloom, darkness … Formed, with suffixed -st, from the base MIC (Aryan MIGH)'; 'mizzle, to rain in fine drops … formerly misle, put for mist-le, frequentative form of mist'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 484 (pdf 483), s.v. مه/میغ\", \"stance\": \"partial\", \"note\": \"Lists Old English MIST and English MIST/MIZZLE among the descendants of the 'cloud, mist' root together with Avestan MAEΓA and Persian میغ — i.e. with Klein rather than with Watkins.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-328.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T16:26:27.334Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T16:26:30.698Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 tools/verify_check.py 328"
}
```


### [2026-09-07T16:26:31.995Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'plausible': 2, 'confirmed': 11}
root verdicts: {'plausible': 1}
ref checks: {'supports': 16, 'not_found': 1, 'partial': 1, 'not_checked': 4}
books consulted: {'partial': 7, 'supports': 42, 'silent': 3, 'contradicts': 1} | by book: {'CHEUNG': 7, 'PHD': 5, 'WLD': 5, 'ARY': 4, 'KLN': 4, 'BRT': 3, 'NYB': 3, 'HRN': 3, 'HUB': 3, 'SKT': 3, 'BQT': 2, 'SYN': 2, 'AHD': 2, 'ISS_alt_DKS': 1, 'MON': 1, 'SOD': 1, 'LAT': 1, 'POK': 1, 'IEC': 1, 'WEB': 1}
```


## [2026-09-07T16:26:55.351Z] AGENT

Verification of PDF page 328 (book page 298) complete. `data/verification/page-328.json` written; `verify_check.py 328` reports **13/13 nodes, 0 PROBLEM lines**.

**Counts** — nodes: 11 confirmed, 2 plausible. Root: 1 plausible. Ref checks: 16 supports, 1 partial, 1 not_found, 4 not_checked. 42 supporting / 7 partial / 3 silent / 1 contradicting entries across 20 local books + 9 archived web pages.

**Root (Meig, Meik / Meigh 1 / Meigh 2) — plausible.** All three glosses match Pokorny 712–714 exactly, but the single root box conflates three roots: *meyḱ- "mix" (Pok. 714) is unrelated to *h₃meyǵʰ- "urinate" (713) and *h₃meygʰ- "blink/cloud" (712). WLD II 246 credits Kern with the "richtige Trennung"; on the other hand Horn no. 1009, Mo'in (BQT 2079: «قطعی بنظر میرسد») and Cheung 259 do join Meigh 1 with Meigh 2.

**Plausible nodes (no disputed, no transcription_suspect):**
- #1 Avestan "minašti; vi-maik, vi-minašti" — *vi-maik-* is a **reconstructed Old Iranian** form (Nyberg II 90, repeated by Mo'in BQT 1835), not attested Avestan; the attested Avestan is `minaš` (Y 46.14, Bartholomae s.v. myas-), "minašti" being Pokorny's normalised citation form.
- #3 Avestan "maēz : urine" — maēz- is the **verb** "to urinate"; the Avestan noun "urine" is maēsma-/maēsman-. Gloss/part-of-speech slip only; root and branch correct.

**Reference problem to note:** `BQT:62` on node #3 is misplaced — Borhān vol. 1 p. 62 (leaf 272, pinned by the catch-line «بقیه از صفحهٔ ۶۶») is the آموده/آمون/آمیز page, i.e. the *mix* branch, with nothing on urine. It fits nodes 1–2, not 3. `ISS:285` (nodes 7, 8) is unverifiable — Bailey's Indo-Scythian Studies VI is not online and the DKS substitute has no MP mēγ.

**Extraction error for the owner to fix:** node #5's quote (`باچنین دل چه جای باران است…`) has `"poet": null`, but the printed page prints the attribution **Sanâî** in the left margin (Mo'in's source footnote, BQT 1835 n.5, gives «سنائی غزنوی ص ۷۸۶»). Everything else in the JSON matches the printed chart faithfully.

**Notable finding:** the chart correctly separates the homophones گمیختن "to mix" (< *vi-maiǰ-, node 2) from گمیز "urine" (< gō-mēz / *ui-maiz-, node 5) — exactly the split Horn insists on in his footnote to no. 51. For node #12, Watkins/AHD supports Nourai's *mih-stu- → mist verbatim, while Klein (and Aryanpur) put OE *mist* under the "cloud" root instead; recorded as the one `contradicts` stance.
