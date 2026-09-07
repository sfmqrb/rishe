# Verification process log — verify-page-326


## [2026-09-07T15:49:29.590Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 326 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-326.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-326.json. Write /home/sfmqrb/git/rishe/data/verification/page-326.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 326` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:31.935Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:32.689Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:32.703Z] TOOL RESULT

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


## [2026-09-07T15:49:33.171Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-326.txt"
}
```


### [2026-09-07T15:49:33.194Z] TOOL RESULT

```
1	=== PDF page 326 (book page 296) ===
2	--- entry 0 ---
3	ROOT Megh -> redirect to Meg
4	--- entry 1 ---
5	ROOT [Indo-European] Mei 1 : soft, mild  (refs POK:711)
6	#1 (parent #0) [Avestan] refs=POK:712; MON:4494 | mayazda : a special meal of Zoroastrians, guests guests invited to a meal
7	  #2 (parent #1) [Pahlavi] refs=BQT:2076; VDQ:370 | mayazd, mâz : feast
8	    #3 (parent #2) [Persian] refs=BQT:2076; MON:4494 | mayazd «مَیَزد» : feast, guests ; mîzbân «میزبان» : host ☞Pa
9	    #4 (parent #2) [Arabic] refs=AFM:148; VDQ:370 | mâ`da : food, food table
10	      #5 (parent #4) [Persian] refs=MON:3674 | mâedeh «مائده» : food | extra: مایده
11	#6 (parent #0) [Latin] refs=AHD:1528 | mitis : soft
12	  #7 (parent #6) [English] refs=None | mitigate : soften, moderate
13	--- entry 2 ---
14	ROOT [Indo-European] Mei 2 : to fix, build, fence  (refs POK:709)
15	#1 (parent #0) [Old Persian] refs=BQT:2073; KNT:202 | maixa : nail ; mayŭxa : door knob
16	  #2 (parent #1) [Persian] refs=POK:709 | mîx «میخ» : nail ; mîxak «میخک» : carnation
17	#3 (parent #0) [Latin] refs=AHD | mŭnîre : to fortify
18	  #4 (parent #3) [English] refs=None | ammunition
19	
```


## [2026-09-07T15:49:35.912Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-326.json",
 "description": "Read source JSON page 326"
}
```


### [2026-09-07T15:49:35.951Z] TOOL RESULT

```
{
  "pdf_page": 326,
  "book_page": 296,
  "entries": [
    {
      "root": {
        "name": "Megh",
        "redirect": "Meg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mei 1",
        "lang": "Indo-European",
        "refs": "POK:711",
        "gloss": "soft, mild"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:712; MON:4494",
          "words": [
            {"translit": "mayazda", "gloss": "a special meal of Zoroastrians, guests guests invited to a meal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:2076; VDQ:370",
          "words": [
            {"translit": "mayazd, mâz", "gloss": "feast", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2076; MON:4494",
          "words": [
            {"translit": "mayazd", "gloss": "feast, guests", "script": "مَیَزد"},
            {"translit": "mîzbân", "gloss": "host", "script": "میزبان", "see": ["Pa"]}
          ],
          "note": null,
          "quote": {
            "text": "ای به مَیَزد اندرون هزار فریدون - ای به نبرد اندرون هزار تهمتن",
            "poet": "Farrokhî"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "AFM:148; VDQ:370",
          "words": [
            {"translit": "mâ`da", "gloss": "food, food table", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3674",
          "words": [
            {"translit": "mâedeh", "gloss": "food", "script": "مائده"}
          ],
          "script_extra": "مایده",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1528",
          "words": [
            {"translit": "mitis", "gloss": "soft", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mitigate", "gloss": "soften, moderate", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mei 2",
        "lang": "Indo-European",
        "refs": "POK:709",
        "gloss": "to fix, build, fence"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:2073; KNT:202",
          "words": [
            {"translit": "maixa", "gloss": "nail", "script": null},
            {"translit": "mayŭxa", "gloss": "door knob", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:709",
          "words": [
            {"translit": "mîx", "gloss": "nail", "script": "میخ"},
            {"translit": "mîxak", "gloss": "carnation", "script": "میخک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "mŭnîre", "gloss": "to fortify", "script": null}
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
            {"translit": "ammunition", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T15:49:36.996Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-07T15:49:37.055Z] TOOL RESULT

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
```


## [2026-09-07T15:49:43.812Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KNT','BQT','MON','AFM','VDQ','PHD','NYB','BRT','HRN','HUB','KLN','LEW','LAT','WLD','IEC','SYN','ARY','PLA','FVQ','SKT','CHEUNG']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Inspect refs_online metadata"
}
```


## [2026-09-07T15:49:44.377Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-317.json",
 "description": "Look at example output file"
}
```


### [2026-09-07T15:49:45.298Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghboo
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== CHEUNG null
```


### [2026-09-07T15:49:45.449Z] TOOL RESULT

```
{
  "pdf_page": 317,
  "book_page": 287,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Mad",
      "verdict": "confirmed",
      "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
      "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
      "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
      "sources": [
        "https://en.wiktionary.org/wiki/mattus",
        "https://en.wiktionary.org/wiki/meat"
      ],
      "ref_check": [
        {"ref": "POK:694", "status": "supports", "note": "POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart."}
      ],
      "consulted": [
        {"src": "WLD", "where": "Bd. II 230-232 s.v. 'mad-'", "stance": "supports", "note": "incoming/WLD/WLD_Bd2_pages.txt line 15104: 'weitere iran. Worte für Dickmilch u. dgl., so np. mast \"saure Milch\", masī[dan]' — the article Pokorny cites as WP. II 231 f., same members."},
        {"src": "AHD", "where": "Watkins 1985 p. 38 (AHD_watkins1985.txt line 708) s.v. mad-", "stance": "supports", "note": "'mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, \"it gladdens, it bubbles,\" hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate … MATE. 3. Suffixed form *mad-sto- … Old English mest, fodder: MAST. [Pok. mad- 694.]'"},
        {"src": "IEC", "where": "Mann, leaves 553-556: 'mad- (1) feed; food', 'mad- (3) get wet; be wet', 'madtós (maditós, mastos)'", "stance": "partial", "note": "IEC.txt lines 10227, 10237, 10239: Mann splits the family into three lemmas — 'mad- (1) \"feed; food\". WP II, 232 …', 'mad- (3) … \"get wet; be wet\". WP II, 230  Skt. mádāmi, pp. mattáh \"get drunk\"; Lat. madeó …', and 'madtós … \"fed, fattened; food, fattening\" … Skt. cf. mástu, n. \"sour cream, whey\" … Per. māst \"sour milk\"' — the same words, but no single root box."},
        {"src": "SYN", "where": "Buck ch. 3.65 'Fish', p. 184 (SYN.txt line 4927)", "stance": "partial", "note": "'Skt. matsya-, Av. masya-, fr. an IE *mad- \"be wet\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' — Buck knows the root but puts a question mark on the fish member."},
        {"src": "CHEUNG", "where": "pp. 253-254, s.v. *mad¹ and *mad", "stance": "partial", "note": "CHEUNG.txt line 16801: '*mad¹ \"to become intoxicated, joyous\" … «PIE *med- … = LIV: 423 f. | Pok.: 694 f.'; line 16828: '*mad \"to curdle, coagulate\" … Skt. mástu- (n.) \"sour cream\" (< *mad-stu-) … The root is apparently IIr. … PIE — = LIV: – | Pok.: 694 f.' Cheung keeps Pokorny's page but treats the two senses as two roots."}
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "masya 1 : fish; mada : having too much liquid, drunk; mad : a water bird, mina",
          "verdict": "plausible",
          "derivation": "Two of the three items are real Avestan words. (a) masiia- 'fish' (Y. 2.8, Vd. 2.8 etc.) is well attested, and Pokorny 694 derives it, with Skt. matsya-, from an -es-stem *mades- 'the wet one' — this is precisely Nourai's arrow; but Buck (p. 184) already marks it with a question mark, and current handbooks (Martínez García & de Vaan, Introduction to Avestan, p. 32; en.wiktionary s.v. Reconstruction:Proto-Indo-Iranian/mátsyas) call PII *mátsyas 'unknown; possibly borrowed from the BMAC substrate', citing the lack of any relation to *peysk- or *dʰǵʰu-, with the *meh₂d- connection only as an 'alternative theory'. (b) maδa- m. 'intoxicating drink, intoxicated ecstasy' (Bartholomae AiW 1112 'Rauschbegeisterung durch Haoma-Genuss', beside the verb maδ- 'to become intoxicated', Y. 10.8, N. 30) is exactly Pokorny's 'av. maδa- Rauschtrank' — Nourai's gloss 'having too much liquid, drunk' is a loose paraphrase but the derivation is right. (c) 'mad : a water bird, mina' is not an Avestan word at all: Bartholomae records only the verb maδ-, and the water-bird word Nourai wants is Sanskrit madgu-, which Pokorny equates with New Persian māγ ('ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ'). The printed page (see refs/ocr/BOOK/317.png) has exactly what the JSON has, so this is Nourai's own slip — he moved the Sanskrit/Persian bird word up into the Avestan box to give māγ a parent.",
          "derivation_fa": "از سه واژهٔ این گره دو تا اوستایی راستین‌اند. یک: masiia- «ماهی» گواهی‌شده است و پوکورنی (ص ۶۹۴) آن را همراه سنسکریت matsya- از ستاکِ ‎*mades-‎ «آنِ تر» می‌گیرد، یعنی همان پیکان نورایی؛ اما باک (ص ۱۸۴) همان‌جا علامت پرسش گذاشته و پژوهش امروزی (مارتینس گارسیا و دِ فان، ص ۳۲؛ ویکی‌واژه ذیل *mátsyas) خاستگاه این واژه را ناشناخته و شاید وام‌واژه‌ای از زیرلایهٔ باکتریا-مرو (BMAC) می‌داند و پیوند با *meh₂d- را تنها «نظری دیگر» می‌شمارد. دو: maδa- «نوشابهٔ مست‌کننده، سرمستی» (بارتولومه، فرهنگ ایرانی باستان ستون ۱۱۱۲) دقیقاً همان «maδa- = Rauschtrank» پوکورنی است و اگرچه معنایی که نورایی داده («دارای مایع بسیار، مست») دقیق نیست، اشتقاق درست است. سه: «mad» به معنی «پرندهٔ آبی، مینا» هیچ گواهی اوستایی ندارد؛ بارتولومه فقط فعل maδ- را ثبت کرده و واژهٔ پرندهٔ آبی در واقع سنسکریت madgu- است که پوکورنی آن را برابرِ «ماغ» فارسی می‌گذارد. تصویر صفحهٔ چاپی (refs/ocr/BOOK/317.png) نشان می‌دهد متن استخراج‌شده امانتدار است؛ پس این لغزش از خودِ نورایی است که واژهٔ سنسکریت/فارسی را به جعبهٔ اوستایی برده تا برای «ماغ» پدری بسازد.",
          "sources": [
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/m%C3%A1tsyas",
            "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C"
          ],
          "ref_check": [
            {"ref": "POK:694", "status": "supports", "note": "POK_02.txt line 5647: 'ai. madgu- \"ein bestimmter Wasservogel, ein Fisch\" = np. māγ \"ein Wasservogel\", ai. mātsya- m., av. masya \"Fisch\" (\"der nasse\"; Ableitung von einem -es-St. *mades-)' and 'av. maδa- \"Rauschtrank, Rauschbegeisterung\"' — all three of Nourai's items, but the bird is Sanskrit/Persian, not Avestan."},
            {"ref": "SYN:184", "status": "supports", "note": "SYN.txt line 4919 ff.: page 184 is Buck's ch. '3.65 FISH', whose table lists 'Skt. matsya- / Av. masya-' and whose note 5 (line 4927) reads 'Skt. matsya-, Av. masya-, fr. an IE *mad- \"be wet\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' Nourai's page is right; the question mark is his to answer."}
          ],
          "consulted": [
            {"src": "BRT", "where": "AiW col. 1112 s.v. maδa- (BRT.txt line 19595); no bird lemma 'mad-'", "stance": "partial", "note": "'g. *mada-, j. maδa- m. 1) \"Rauschbegeisterung\" durch Haoma-Genuss … Ableit. — Zum V. maδ-. — ai. mada- m., np. mai.' Bartholomae has maδa- and the verb maδ-, and masiia- 'Fisch', but no Avestan water-bird word — confirming that Nourai's third item is misplaced."},
            {"src": "CHEUNG", "where": "p. 253 s.v. *mad¹", "stance": "supports", "note": "'*AVESTAN: Y Av. maδ- \"to become intoxicated, joyous\" — Liste: 42 … *SANSKRIT: mad \"to become exhilarated, intoxicated\" (RV+) = EWAia II: 299' — the Avestan verb and its Indic cognate as Nourai draws them."},
            {"src": "HUB", "where": "Persische Studien § 94, p. 101 (HUB.txt line 7170)", "stance": "supports", "note": "'§ 94. Ap. d vor y, m, n ist geschwunden: māγ \"ein Wasservogel\", skr. madgu-, ap. *maδgu-?' — Hübschmann derives the bird from an Old Persian, not Avestan, form."},
            {"src": "IEC", "where": "Mann, s.v. 'mesgus, os \"diving bird\"' (IEC.txt line 10687)", "stance": "contradicts", "note": "'mesgus, os \"diving bird\". Cf. mesgó (2). (mezg-)  Skt. madguḥ, m. id.; Lat. mergus, m., LLat. mergulus \"cormorant\"' — Mann assigns the water-bird word to *mezg- 'to dive' (Lat. mergus), not to *mad-."}
          ]
        },
        {
          "id": 2,
          "lang": "Persian",
          "words": "mâhî «ماهی» : fish; mast «مست ۱» : drunk; mâğ «ماغ» : a black water bird, mina",
          "verdict": "plausible",
          "derivation": "All three Persian words are real and the two central ones are textbook cases. ماهی māhī 'fish' < Middle Persian māhīg [m'hyk] (MacKenzie, CPD p. 54 'mahig … fish; astr. Pisces') < Proto-Iranian *mácyah < PII *mátsyas, cognate with Av. masiia-, Skt. mátsya-; the MP -g of māhīg is regularly lost in New Persian (cf. MP xānag > NP xāna). مست mast 'drunk' < MP mast [mst] 'bemused, intoxicated' (MacKenzie p. 54; Manichaean MP/Parthian mst, Cheung *mad¹), from Old Iranian *mad-ta-, the participle of maδ- — the Old Iranian cluster -dt- gives -st- (cf. *basta- > baste), exactly parallel to Skt. matta- and to Lat. mattus < *maditus in node #10. ماغ māγ 'a black water bird' is attested from the 10th c. (Loghat-e Fors, printed p. 235 of the Eqbal ed., quotes Daqīqī 'مرغی باشد سیاه فام و بیشتر در آب نشیند'), and Pokorny 694, Horn no. 961 and Hübschmann § 94 all equate it with Skt. madgu-, Hübschmann positing an Old Persian *maδgu- with loss of δ before g/m; that is Nourai's arrow, but Mann (IEC, s.v. mesgus) instead puts Skt. madgú- with Lat. mergus under *mezg- 'to dive', so the last word is only plausible. The Rudakī line in the chart is the verse Borhān-e Qāteʿ quotes for ماغ (Mo'in's edition attributes it to Daqīqī, not Rudakī).",
          "derivation_fa": "هر سه واژهٔ این جعبه فارسی راستین‌اند و دو تای نخست از نمونه‌های درسی‌اند. «ماهی» از فارسی میانهٔ māhīg (مکنزی، فرهنگ کوچک پهلوی ص ۵۴: mahig «ماهی») و آن از ایرانی باستان *mácyah و هندوایرانی *mátsyas، هم‌ریشه با اوستایی masiia- و سنسکریت mátsya-؛ ‎-g‎ پایانی فارسی میانه در فارسی نو به‌قاعده افتاده است (مانند xānag > خانه). «مست» از فارسی میانهٔ mast (مکنزی؛ مانوی و پارتی mst)، از ایرانی باستان *mad-ta-، صفت مفعولی ستاک maδ-؛ خوشهٔ ‎-dt-‎ ایرانی باستان به ‎-st-‎ بدل می‌شود (مانند *basta- > بسته)، درست همانند matta- سنسکریت و mattus لاتینی (گرهٔ ۱۰). «ماغ» از سدهٔ چهارم گواهی دارد (لغت فرس، ص ۲۳۵ چاپ اقبال، از دقیقی: «مرغی باشد سیاه فام و بیشتر در آب نشیند») و پوکورنی (۶۹۴)، هرن (شمارهٔ ۹۶۱) و هوبشمان (بند ۹۴) هر سه آن را برابر madgu- سنسکریت می‌دانند و هوبشمان صورت پارسی باستان *maδgu- را با افتادن ذ فرض می‌کند؛ ولی مان واژهٔ سنسکریت را با mergus لاتینی زیر ریشهٔ *mezg- «شنا رفتن، فرو رفتن» می‌گذارد، پس این یکی تنها پذیرفتنی‌است نه قطعی. بیتِ نمودار همان بیتی است که برهان قاطع ذیل «ماغ» آورده و در چاپ معین به دقیقی نسبت داده شده، نه رودکی.",
          "sources": [
            "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C",
            "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA"
```


## [2026-09-07T15:50:22.561Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 70[89]\" POK_full.txt | head -20; echo ====; grep -n \"Page(s): 71[0-3]\" POK_full.txt | head -20",
 "description": "Find Pokorny pages 708-713"
}
```


### [2026-09-07T15:50:22.638Z] TOOL RESULT

```
Exit code 1
58096:Page(s): 708-709 
58296:Page(s): 709 
(eval):1: === not found
```


## [2026-09-07T15:50:24.504Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"mayuxa\\|mayūxa\\|maiuxa\\|myazda\\|miyedha\\|miyédha\" POK_full.txt POK_02.txt BRT.txt KNT.txt PHD.txt NYB_vol2_glossary.txt HRN.txt HUB.txt IEC.txt AHD_watkins1985.txt 2>/dev/null | head -40",
 "description": "Grep mayuxa/myazda across refs"
}
```


### [2026-09-07T15:50:24.581Z] TOOL RESULT

```
HUB.txt:5334:zd. myazda^; niyCt *Grossvater' = ap. zd. nyaka-; razm-yOz
HUB.txt:7018:skr. mtdha'\ miyazd 'Gelage* = zd. myazda-, skr. miyedha-;
HUB.txt:7972:miyazd *Gelage' (Parsenwort) = zd. myazda-, Np. mayz
HRN.txt:8770:aw. myazda- ^Opfermahl'; phlv. myazd, myäzil;
HRN.txt:15146:myazda' 1007.
NYB_vol2_glossary.txt:4914:magu-: magū manā: man martiya-: mart Margu-: Marv ni-māy-: nimūtan mayūxa-: mēx mudräya-: muzräyik
POK_02.txt:5935:m.  , Opferspeise',    av.    myazda-   m.  ,OpfermahP;    als  *mei-dho-    ai.   medha. m.  jFettbrühe',  midhas-  n.  , Opfer*;
POK_full.txt:60704:Indie miyedha-m. " saerifieial food ', Avestan myazda-m. "saerifieial meal'; as *mei-6'"o- 
BRT.txt:2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.5.51;  —  i-.a  Vam  ;  V.  5,  i  o  usw. ;  42,  J.18",  (/.3,  26,  9.49, (APm.)  aJsnt^m(s±)..paiti.bar,ltN.ioj;'—  *Vd.i8-20i;  —  't^m  (als  ASn.)  .\  yat °tayä  urvarayä  älan»irfs'V.8.i$;N.6j,'Vd.\spiln~'  .  .  X.ij.sS.  2)  auf  ein  Relati-
BRT.txt:3058:•  j.  *a-gar»mo.varah- ''  Adj.  'der  keine (Zulassung  zur)  Hilzeprobe  hat,  vom  Hitze- ordal  ausgeschlossen  isf:  myazdavä  ratus atnyaadavamm  ratunaim  "ratflum  daste antan  mazdayasiiilts  ". .  macht  (erklärt) der  Ji.  . .  den  Laien  . .  (für)  untähig,  eine Hitzeprobe  abzulegen  .  ."  A.j.9"
BRT.txt:3272:•  j.  a-dätay-  f.  'Nichtgeben,  Nichtdar- bringen,  Verweigerung':  «J  gJu/  ml  vas- trahe  hatö  "oditlm  vaocöit  "man  soll  nicht das  Nichtgeben  eines  wirklich  vorhandenen Fleischstücks  oder  Kleids  behaupten"  V. 4.46'*; — paoiryeheca  nH  myazdake  'oätii {]Si.) yat  mai'iydi.sar^myeAe"\inA6.zi:iz,Aa:&s man  den  ersten  My.,  den  des  jW. -Festes, nicht  darbringt"  A.  j.?;  8-12  (,  SWienAW. (17,839);  —  kat  «3  *dazi'ayasnäi  vä  .  . giul  'iaitya'"  ästryeiti  "begeht  man  da- durch Sünde,  dass  man  einem  Z>. . .  kein Fleisch  gibt?"  N.  i(?; —  •oaiti  */rilraihya-
BRT.txt:4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
BRT.txt:4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
BRT.txt:4902:unfähig  sich  am  Gottesdienst  zu  beteiligen' : ■ .  myazdava  ratu!  amyazdavamm  rahi- ' naim  "»Im  daste  antari  mazdayasnäil\ ". .  macht  (erklärt)  der  R.,  der  My.  dar- gebracht hat,  den  Laien,  der  keinen  My.  I dargebracht  hat,  (für)  unfähig  sich  am  I Gottesdienst  zu  beteiligen  unter  den  M."
BRT.txt:4916:•  j,  ayäOrima-  m.  Name  der  Gottheit der  vierten  Jahreszeit  und  des  an  deren Ende  gefeierten  fünftägigen  Fests**  (mit dem  letzten,  30.  als  Haupttag) ;  °m»m/ra- ourvaihrimim  (sd.)  * varlnihar!t)mla  (sd.) asavatwm  alahe  ratüm  Vr.  2.  2;  Y,3.9;  — °make  'itrimaAe'a  'staheSa  Vr. /.  s;  A.j. j;  —  'mSi  'hrimsi  'siaica  Y./,9J  — tüiryeheca  nä  myazdakt  ddäiti  (sd.)  . .  yat 'maAeA.3.10;  —  "äirisatim  "mähe  ftW^rahe anayranqm  "30  [Tage  sinds  bis  zum (Hauptjtag]  des  A.  [ira  Monat]  des  M, [am  Tag)  des  ewigen  Lichts"  A._j,  10,
BRT.txt:5014:•  ').  a-vadö.urvatay-  Adj.  'der  einen  Ver- trag durch  das  (blosse)  Wort  abzuschliessen nicht  quaÜfizirt  ist' "';  myazdava  ratus amyaxdavatum  ratunafm  'vaitlm  aaste antarf  masdayasnäii  ".  .  macht  (erklärt) der  Ä. . .  den  . .  Laien  für  unfähig,  durch das  (blosse)  Wort  einen  Vertrag  abzu- schliessen" A.J.8.
BRT.txt:6076:—  'sähe  paiti  mq^rfm  'sähe  paiti  fra-  manarihäY.4ß.  10;  —  '/ahya  yäsa  (sd.) sasiim  V.  4.  43  (s.  a);  —  'fa  i-iyaca  Vyt  a^m  Y.54.  i;  —ySais'sMt  nipSrfhi  (sd.) 75;  —  yS  'sili  hr>jyqsl>mS  (sd.)  R  /;  —  manasut  vohn  V.28.  11.  3)  im  jAwr.: airyamarum  isfm . ,  matistim  'saht  srava-  hs  aiwyiixsayatB  hadü  'Saia  vasträca  .  . tthqm  Y.54'3;  —  'iahe  myazdanqm  Vr.  Y.  3<?.  4;  —  yöi.äim  hanhana  (sd.)  'säca ^■3;  —  y^i  til/'rat  (sd.)  aurö  mainyus  frSriticaH.8.i; —  •/«lä""  nmtaahana.. dahlm 'sähe rauh fus  Yt.13.TT,  —  haoma..  yaorum  (sd.)  äste  V,4.45;  —  ahunm haÜTm^a  'sa/ie  xi'r  (sd.)  ahi  Y.  10.  4^  — \mazdqm   yS    'sähe    apanöJ?mS  yS    'sähe
BRT.txt:9730:—  "Alf  vJsph  ä  xsa>rsi  *yä  ..  ^raasiä'  vTmij(sd.)  katarascit  *parayat  N.  5;5";  — (sd.)  Y.^4.^.  A)  Plur,  und  Sing,  mit  al^S  ''ianam'''' *iris'ifiü»am  ra^s'^{sd.)  N, 2 ; vispa-  Adj.  von  der  Gesammtheit  derl  —  agta paräyaiti (sd.) yaia '^afys^'^A^iii stoflflichen  Lebewesen  'Welt,  Menschheit"  N. 2;  —  myazdava..amyasdavan9tn..yiU)m (vgl.  anhav-  Sp.  io7f,);  y<^a  °^3kva  {%d.)  "'kanqm  frap>r>naoiti  A.j.  11"*;  V. i'fljö^.Äjiiir?/ra(^a>-äne"dassichunabhängig|  19,29,  F,4f-; — /radahüi  'Ibanam  kava- unter  den  Wesen  einhergehe"  Y.9.  17;  —  M^häi  asavastanam  Y.  6S.  4(?);  —  yai aAümca  (sd.)  ratümca  '^anam  Vi.  I0.i}3,'.^avani  aiwi.vanyä  taiiryavantim  ..  ahmt 13. g2;  91;  —  ratu>wim  °%anqm  Yt  /o. ,  (sd-,  Sp,  4)  '"ke  (LS.)"'  ptlanahu  Yt  5. 92;  —  aat  .  .  mraom  .  .  az^m  yö  akurs\  109;  73, 113;  —  ka%S  ayärS  .  .  fprasayäi masda  .  .  yima  .  .  mS  Oi  fniciaya  .  .  mi'  (sd.)  lÄril  ai^T  '^wäAa  '^ahß  tariusiÖl  Y. °'ia  varihaya  ..  mg  vXsäi 'i:anqm  %rätSca'.43-T',  — yS  nS  ainrianqm  (sd.)  irJri- Aarpläca  .  .  V.  2.  4;  5^;  —  aiim  daA3A?m ;  xsäite  °%anam  (als  Obj.)''  .  .  tanunqm  Y. .  .  a^im  *'hsvays  (DP.)  '*  drvant3m  Y.  (J.  ö'j.  7 ;  —  ahmäi  ntmauhs  ävaidayamaidt 8;  —  cim  .  .  qsitm  tsattt  .  .  "'"itä/tz-ö'^  I  '^Sscä  tamiaslä  Y.  jÄ  2;  —  vJspa  °'i:Ssca mahrkaum  Aog.  48;  —  us  *täcil  v.'krka  tanvasca  asdibista  uStänqsca  kihrpasca  . ,
BRT.txt:10884:•  j.  xStva-  Adj.  (fem.  °tvl-)  'der  sechste': akmSi  'tvö  äjasat ..  vjr^iraynS'Yt.i4.iT, 1.7,  15.2,  V.4.2,  N.  102;  —  'tarn  astaiiqm syaoimanqm  V.4.28;  1.8,  5.29,  30,  p.';, 28,  Y.p.2i,N.i'2,  F.j  (wo  '/um);  —  'tia- ht'a  ..  myazdake  A.^.  12;  —  tüirya  'hart- var»  ,  .  puxZa  tainäus  .  .  °tvT  fradaxsana V. /.^.g;  Vd.  72'>.  a)  ASn.  'tum  als Adv.  'beim  sechsten  Mal':  V.4.19,  23, S.Tl-
BRT.txt:12353:V.  5-  30.  31.  9-  7.  28,  3'.  rji  33'>  N-  ", Äs,  *F.  f ;  —  'rlmgäma  frabarat . .  urria H.2.15,  33;V.4.3s,j5.7;  1.6;— />««>■ j^«&  .  .  'ryeht^a  .  .  myazdake  A.J.  10; F.g;  —  V^^V.  7.  53  PüZ.;  —  -rj"* fNPn.)  %am)art  (sd.)  V.  74.  9;  Yt.  /.  7, VA/2;  —  'ry3(^)  uitavailyh  va..hät!lii hanääta  N.  702;  102;  —  'yanqm  Vd. 75.  a)  ASn.  'rXm  und  DS.  'ryai  als Adv.;  a)  'zum  vietten  Mal':  •ryjj'' H/<»aa:  (sd.)  -rj-si»)  ai/ajÄi  V./ö'.  16;  — /äjÄ  TrM'J  *gams.hninm  "nachdem  er den  vierten  Schritt  getan  hat"  V.  s8. 55-  ß)  "beim  vierten  Ma!';  ka  he  asH a^al  .  .  'rfm  %rUatfm  upäsananqm  V. 4. »9;  23,  37. 3I1 5- S>  *■  77-  Tf)  Viertens': kva  °rJm  aiiihi x?mS ^aisUm'V.^.^;  10,23. KompE.  {äxCiÜr').  —  Ordinale  lu  ca%war-; S  311.  —  ai.  turtya-,  lurya-  Adj.  —  Pü.  T  ea- härmn.  —  <)  In  sdjekt.  Gebrauch,  beimNom.act
BRT.txt:14723:'in  '"vivi^äätS  (si)?  yö  alta  (sd.)  pairi ari^ra  frazSnaiH  F.  5;  5;    —   tat  *!ahe tat  ^vjkayehe  "das  (gilt)  für  den  Richter, das  fUr  den  Zeugen"  F.a/b;  —  myaidavh ratui  amyazdavantm    ratunaim    ähüirTm 'i?tn    frapfnnaoiti    (sd.)     A.  J.  12;     — urvaxiayB  (sd.)  ..'s5..  däte.räzS  Y.ß.  10. KompE.  —  VgL  "ifaÄa-  mit  No.  I,  wo  wei- teres, —   Fü.  {la  Y.  p,  4g,  F.);  äälawar,   (lu Y.  p)  erl. :  iu!  viÜr  u  Jältrtiarih  kort;  (lU  A.); däiastämh,   {lu  Y.  33,  afij:   wie   für  fanityö.- jkaiia',   sd. ;    SQ.  {lu  Y.  p):    nyäyädhipah,    (lu y.  4^:    nyäyi,   (zu  A.):   ayäyah,   (lu  Y.  m): färvanyiyaväa.
BRT.txt:15325:xlfrä  dnwS. :  myasdavh  ratui amyazda- vatt?m  ratunalm  yäUm  (sd.)  gaihanam frapirinaoiti  A.3.  ii^*;  10;  —  myazdava .  .  amyasdavamm  . .  ähsirim  tka^pm  /ra- pirmaoiH  ",  .  verurteilt  . .  den  I^en  zum Verlust  des  ah.  Richters"  .^._j.  12*';  — Pass.:  aaf  i^armö  frapiryäd^^ "^  V.  5.  9 PüZ.
BRT.txt:15775:—  °rTm  gäma  frabaral  .  .  bitim  .  .  H. 2.15;  V.r.  2,  4.50",  75.  2,  YLip.3S;  — 'ryqm  gurftqm  gprjtaffa  .  .  bityqm  .  .  Yt ij.  57  f.;  Vyt  54'<  —  "O"^  '^'^^'^  xsapanö  . . bityh  .  .  Yt  Ä  13-16;  —  'ry<!Ae^<f  »ä myazdaAe  mUttt  .  .  bityeheca  .  .  A.^}.  ;£; P.p,  V.  2. 19  PüZ.;  ~  -ryat  >ri/vai  x^afhe .  .  bityäi  .  .  V.  7Ä  18-20;  —  'rya  'yeAAl ml  asät  Aacä'  bifyä  .  .  N.  J02(?); —  'ryai nidanzaym  (sd.)  aptrmSyahm  .  .  aiwica apanm  (sd.)  . .  V.  i$.  48;  —  sraoltm  . ,
BRT.txt:17265:Y.p.  19,  N.  .V2,  F.i  (wo  -fim);  —  nöij •lim  dusjasfis  (sd.)  ahäm  (Sp.109  o.)  m?rq- syat  Y.  4:5.  i;  —  paoirim  aHaisqm  syao- "^manqm  v»r>zimtam  nsit  'tlm  "(wenn)  die erste  dieser  Taten  begangen  (wird),  nicht die  zweite"  V.  4.  50"!; —  \hauv  *'tly^- maf'i'i  udapatain  (sd.)  pärsaiy  Bh.^,  5;  — yai  °tlm  ^annS  apan^mata  "als  die  zweite (sva.  der  zweite  Teil  der)  Herrlichkeit  ent- wich" Yt.jp.  36;  V,j.4,  4.  41,  i^.^,  H.  2, 15;  —  paoiryqm  xlapan>fn  .  .  'tyqm  .  . >riiyam  Yyi.  54;  H.2.  3,  21,  YL/7.S8; —  'iya  (AP£)  äasa  xsapanS  Yt  Ä  1 6 ;  — paoiryeheca  .  .  "tyeheca  .  .  myazdahe  A.  _j. 7  f.;  *P.p*';  —  '^ai  ^risväi  xsaßu  V.  18. 20;  —  '/ytiy)  akunanqm  vairyanqm  N. 102;  102.  a)  ASn.  duvittyam,  bitim  und DS.  bityai  als  Adv. ;  a)  'zum  zweiten  Mal' : yal  paoirfm  .  .  'lim  .  .  'Sirillm  .  .  kgrsnisi V.7-37;  5-5.  8.i^;~'tyäi^'>  upam^sA') 'lyäi^*  fiiiasta  V,  i(7.  15; — \patiy  'llyam bäbiruviyä  hami^'iyä  abavi^  "wiederum zum  zweiten  Male  wurden  die  .  ."  Bh._y. 13;  2.8,11.  ß)  'beim  zweiten  Mal': ks  hl  asti  ri^at ..  "tlm  dasa  upäeana  V. 4.18;  22,  27,  31,  34,  37,  ^'.77;  — aSa *°fyäi''>  a'ha  *irityai(Bd.)li.42.  ■()'zwei~ tens';  ks 'lim  imqm  zant  mazi^ta  x^naoma xsimvayeiti  V.ß.13;  2,8.
BRT.txt:19014:•  j.  naramyazdana-  m.  EN.  eines  Gläu- bigen: 'nahe  äii<wyaoi  asaonH  Yt  13.  iio.
BRT.txt:19015:Eig.  Bed.?  —  Anscheinend  Ableit.  aus  *njtj- myazda^,
BRT.txt:19658:•  j.  mai8yöi.zar9maya-')  m,  Name  der Gottheit  der  ersten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*> (mit  dem  letzten,  45.  als  Haupttag):  'maem Payanhim  (sd.)  alavansm  alahe  ratäm  Vr. 2.3;  Y.2.9,  A.^,  3;  —  'mayehe  payaahö Vr.  1.  3;  A.3.  a;  —  'mayäi  Y.  J.  9;  — pagiryeheca  na  myazdahe  a&siti  (sd)  .  .yai •mayehe  A.^.  7;  — pan^^a  ^a%war)iafom •mayehe  alaAe  vaAistahe  da%usö  "45  [Tage sin<^  bis  zum  (Haupt)tag]  des  M.  [im Monat]  AV.  [am  Tag]  des  Schöpfers" A.^.?.
BRT.txt:20622:•  j.,  g.  myazda-  m.  Bezeichnung  der  zum Opfer  bestimmten,  als  Opfer  dargebrachten festen  (nichtflüssigen)  Genussmittel,  'feste Opferspende,  Opferspeise,  Speiseopfer'  '* : masdayasna  . .  °d>m  daihyärys  gaomsnUm ma^umani»m  V,  6*.  22;  —  asaya  daoamt sfariäijm  'asm  Aaurvata  anwntäta  X.a.x; J.  I ;  —  imq  haemqsca  'dqsca  zao%rasia barfsmaca  V.  */.  i ;  —  imq  haomq  . .  ima 'da  Vr.  II.  2\  —  cfaraia  narö  altttn  'dfm *yBi.äim  kanhana  (sd.)  Y.  tV.  a;  —  yaüa aSaisqm .  ■  myazdavanqm  (sd.)  aitaahqm  yat 'danqm  anahaxtS  (sd.)  parabaraiH  N.  6^; —  kahmäi  kaca  ^myazdavanqm  °de{1) rag'hwaiti  N.61,  62(?);  ^~ paotryekela  nä 'dahe  flSa(/i(sd,)  A.^.  7;  8—12;  —  data hs 'da  ratuffii  "gespendet  ist  von  ihm  der den.Ä.  genehme  My"  A.j.6;  —  dätaca.. aSim  ratUmca  'dimca  ytm  matöysizan- maim  pasSus  *g>fy&u/ "und  Spendet  lur(?) diesen  Jt.  und  als  seine  Opferspeise,  fUr den  M^  das  Junge  eines  . ."  A._j.  3 '';  — mS»h3mca  maiitanimca  'd)mca  fräyasa- maide  Ytrf.  i;  —  ^attam  'de  (als  AP.)  3' ''aiwi.vaä.aydti  ra'^waica  'dal'a  ra'^wai'ca N.ft(?);  Vr.4-  a(?};  —  nivaloayemi  .  . staotanqm  yesnyanqm  .  .  'danqm  Vr,  i.  3;
BRT.txt:20625:•  j.  myazday-  m,  sva.  myazda-:  'döU *ayq  N.  «yj;  *y2  '\
BRT.txt:20627:•  j.  myazda'van*  Adj.  'der  My.  hat, darbringt':  jiaji-a  altaisam  mazdayasnanqm 'vanqm  aitanAqm  yat  myazdanqm  ana- haxts  (sd.)  parabaraiti  "und  wer  von  den Mazdasynem,  die  My.  dargebracht  haben, etwas  von  den  My, . .  wegnimmt"  N.  63;  — kahmät  Aaca  *'vanqm  N.Ö2",  ö"/'>,
BRT.txt:20629:•  j.   myazda'vant-  Adj.   'der  My.   hat,
BRT.txt:20630:darbringt':    myazdahe    aoäiti  (sd.)    .  .   'va ratus    amyasdavafum    ratunalm    ayasnim (sd.)  daste  A.,J.7;  8-12, Pü. !  myazdötnand.
BRT.txt:20631:•  j.  myezdin-  Adj.  (fem.  'dinl-)  'mit Myazda  versehen':  yS  .  .  kaemahe  hulahe daläiti  usjfiitinqm  vä  'dinqm  (GPf)  '>  V. 18.  12.  a)  sva,  'der  Myazda  darbringt': fravalayS ..yä  mat^m^mät  'dinqm  (GPm.) . .  upavazmU  Yt  13.  64,
BRT.txt:21203:—  aitatahqm  urvaranqm  y  IUn.H^ranqm Y.  Ä  7  5 ;  —  aSaesqm  y  daxmanqm  V.  7. 51;  Yt_5.  9, 13; —  aäanhqm  y  myazda- nqm  N.  ^2.  Anhang.  Auftallig  ist  die Wortfolge  (zu  c):  daiiikanqmcli  aidyünam hyat  urunayazamaidfY.3g,3*'>.  2)oluie erkennbare  Bedeutung;  A)imgAw.;a)vor clt  in  ya-  hyalclt  'quicunque'  (Sp.  593  u., 1230  u.):  yä  mazdd^a  (sd.)  hyatüt}^  vt- du!iY.30.\.  b)  vor  cä:  däröi  ahvä astvatascä  hyaicä^l  mananhS  ayapta(sd.) "vitarum  et  (vitae)  corporeae  et  (vitae) animi  fclicitatcs"  Y.  2Ä3;  —  varp^aitl  .. ratui  syaoianS  razistä  (sd.)  drigvataüä hyaicä^'^  *asaom  yehyaca  hsm>myasaill (sd.)  . .  Y.33. 1.  c)  zur  Einleitung  einer Aufforderung:  hy^  höi  hudsmSm  (sd.)  dyäi vax)lrahya  Y.2g.B.  b)  im  jA^p.;  zur Einleitung  der  Antwort:  kva paoirJm  aiiihä zsniB  asailtimi  ..  y^  arpzürahe  grivaya V.J.  7;  —  zur  Einleitung  des  Refrains: paiti  /ahikayai . .  kthrpjm  näämnäi  asaone . .  vadar»  jatäi  y'^^  hl  k»hrppm  . .  vadar> jaiii  Y.5.  33;—  sonst:  bval  vispB  ankul astvä  *azar>s5 ..  daryypm  _y'"  yave  vispai F._3  h;  —  daiiihSul  dairihupaUlm  bisatyai vähm  .  .  anjB  y'i'>  paoirlm  nmana/ie nmänäpaitlm  näirikqm  bHasyät  ka'hioa daSnu  arsjB  V.  7.  41  f.;  —  vTtasti.dra/s y'fi huSkanqm  (sd.)  .  .  aiiihS  s»mB  mdat^yqn V.  7.  29;  29f.3,  33  f.*;  —  das?mB  y  ahmi spanB  alvandasö  spanaauha  .  ,  lutvadasa y    ahmi   data   visqstPmB   ahmi  y    ahmi
BRT.txt:21460:—  ahmükimca  mazdayasnanqm  früya- Simnanqm  Y.6Ä  i2,Vr./2.5.  zaa.:yai aivs  zaota  (sd.)  fräyazüiti  myazdahe  ayq N.Si.  Undeutlich:  yaf  masyika  frä- yazante  v»n%ra^nS  .  .  Yt  J^  48;  —  ya zaota  aiwica  va^ayante  fraca  yazänie Yt  10.  120.  Wertlos:  frayaza  vä nizbaya  vü  ahuräi  mazdai  Vd.  20;  —  yat ^draonS  .  .  fräyazyüi  Vd.  10;  g  (fraya- zfinti).
BRT.txt:21540:•  j.  'yäta-  n.  'der  Jemandem  zugewiesene Anteil;  Besitz':  myazdavh  raiui  amyasda- vatam  raiunaim  *tfm  gal'hanqm  frapirf- naotti  ". .  verurteilt  den . .  Laien  zum  Ver- lust seines  Anteils  an  Hab  und  Gut"  A. ^.11;  —  bao6asca  urvStitmla  'Um  gaz'ia- natu  paiti.jaihydnti  dahm  astvainti  aahvB **, .  befragen  sie  nach  dem  Anteil  an  Hab und  Gut,  der  (dem  Verstorbenen)  . .  ver- lieben war"  V.jp.  29";  F.^f
BRT.txt:24749:Vd.  2',  17;  —  cvant^tn  dräjg  sairi  ma/ya' in  —  (Akk.),  sich  hineinstecken':  tiltryJS iriste  z)mS  nthsite  .  .  sfmö  bavainli  V.  .  .  kthrptm  ral'i:Wayeiti  ".  .  nimmt  eine 7.4s;  — yS  narS  asaanH  trlri'iusö  Z7ml  sichtbare  Gestalt  an"  Yt,  Ä  13;  —  yeähe kihrpa  nikainti  V.  _j.  40  PüZ.;  —  yal  bä  . .  kfhrpasca  ya  raF^wayeiti  srfra  anusa- paili  fraSsi>m  sairi  tiikante  spänasla  nqm  ".  .  und  die  Gestalten,  die  er  an- irista  naraica  irista  V._j.8;  la,  36,  Ä  '  nimmt,  sind  die  schönen  (Gestalten)  der  .." 14;  —  ailala  arte  nasukas'd  nisAioafta(sä.)\Yt.  jj.St.  4)  trans,  'etwas  vermengen, avavat  haca  iristaiibyS  yaia  "irigäim  ,  vermischen  mit  —'{Instr,):  äat  *rai:'ä)wiska- V.  &  ri ;  —  iha  iristanqm  urvqnö yaza'\rahe  (sd.)  ya^  &aom?m  gava  * rafiwayät''^ iiiaide  ya  asaonqm  frarasayB\,26.  7;  i6.\baxsayaatea  ü.jö.  Undeutlich:  aiv(&a 7,  FrW.io.39;  —  sät>m  da%aiti  urvämm'^  asitäkrat  hävanänt  *rasiiwayeiti^''  N.Ä); asaonS  *iriri%änahe  P.24'';  J53';  — \ —  kahmäi  kala  * myazdavanam  myasde yat  irista  paiti  usihistqn  Vt,  7(j.  11;  — .raghwaiti  N.(ii,(J2*''. US  irista  paiti  araiiH  *vijvähu  paiti  ta-\  mit  upa  'eindringen  in  — '  (Akk.):  nasus nuiu  astvä  gayS  *däryeite  (sd.)  FrW.  4.  2 ;  ,  ,  yä  Äaca  irista  upa  jvant»n  upa.rai- s.  noch  *iri^yant-.  "hwaiti  "die  N.,  die  von  dem  Toten  aus  in
BRT.txt:25010:dem,  der  bei  religiösen  Veranstaltungen !  (s.  Sp.  1498  0.)  sävanhalm  visJmca  paiti das  Amt  des  Priesters  und  Leiters  und  \  'tsm  'lavS  vispe  matisia  paiti  °tüm  (AP.) damit  zugleich  des  Richters  innehat^' i,  "um  die  Zeit  H,  wenn  S.  und  F.  die paolryeheca  nä  myazdahe  aaaiti  (sd.)  .  .  |  Ratav%i^^\,  haben,  wenn  alle  gröbsten yat  wailySisarimayeAe  myazdava  'tu}- Ratav  die  Äa/rt?'schaft  haben"  Y.  2.  18C?); amyazdavamm  ratunafm  ayasnim  (sd,) ,  —  vlspaiibyd  afiiys  "tubys  yBi  hmti  asahe aaste  antar»  mazdayasnais  A^^."];  8—12*;  ratavS  (s.  Sp.  1501  o-)  '^rayasca  ^risqsca
BRT.txt:25066:•  j.  ratu-naya-  m.  'Laie'  (im  Gegensatz zu  'ratav):  ratus  'nasin  a^a  'nays  ratüm A.J.  13;  —    myazdavi  ratus  amyazdc n?m     'naim    ayasttim   (sd.J    daste    antara mazdayasnäis  K.3.T,  8-12.
BRT.txt:25530:•  j.  urunya-  m,  'Gefäss';  i)  für  den Myazda,  'Schale,  Schüssel':  yailam  taya- nqm  aiaurune  . .  °ya  rai^wis.6ajina  , . V./4.8.  2)  Du.  die  beiden  Gefässe, 'Eimer'  od.  dgl.,  in  denen  den  Rossen Wasser  und  Futter  gereicht  wicd(?):  äpe urvaire  yazamaide  aourvatqm  •/w(AD.)" asavantm     asahe     ratum    yazamaide    G.
```


## [2026-09-07T15:50:33.704Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 71[0-3]\" POK_full.txt | head; echo \"-----\"; sed -n '58060,58110p' POK_full.txt; echo \"----- 709 article -----\"; sed -n '58250,58300p' POK_full.txt",
 "description": "Print Pokorny 708-709 articles"
}
```


### [2026-09-07T15:50:33.784Z] TOOL RESULT

```
58147:Page(s): 712-713 
58437:Page(s): 711 
58458:Page(s): 711 
60727:Page(s): 711-712 
-----
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
----- 709 article -----
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
Stecken zum Netzestricken '; probably also Old Bulgarian mesto, Serbo-Croatian mjesto, 
Czech /77/s/o "place' from * moiPto-ox *me[i]Pto-. 

References: WP. II 239 f., WH. II 30 f., Trautmann 165 f.; 
See also: compare meih-4. 
Page(s): 709 

Root / lemma: meih-2 

Meaning: to change, exchange
```


## [2026-09-07T15:50:42.302Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '58395,58465p' POK_full.txt",
 "description": "Print Pokorny page 711 articles"
}
```


### [2026-09-07T15:50:42.352Z] TOOL RESULT

```
Meaning: to lessen, small 

Material: Old Indie minati, minoti^ diminishes, damages, hinders ', mTyate, mJyate' 

diminishes ', participle Perf. mlta-\ manyu-mT-^ the diminishing, destructive rancor'; 

gr. pivuGco ' reduce, lessen ', Adj. *mivu-(; in |jivu-cbpiO(; " short-lived, transitory ', |jivuv6a 
" ein kleines Weilchen, nur kurze Zeits ' (Akk. *|jivuv, extension after 5r|-6a); jjeIcjov, [jeTov ' 
less, fewer, inferior, smaller ', after irAEiajv for *[j£ivu)v that still in apisivwv 'better' = "* not 
less ' has received ( *meih-no-), 

Latin ni-mis^ beyond measure, too much, overmuch, excessively, too ' {*ne-mi-is), 
nimiusM] ( *ne-mi-os) " beyond measure, excessive, too great, too much '; Latin minor, n. 
and Adv. minus^ little, small, petty, puny, inconsiderable ', minimus^ least, smallest, very 
small, minute, trifling, insignificant ' {*minu-mos), minister^ subordinate, servant, that 
serves, ministering ' (after magister, Oscan minstrels " little, small, petty, puny, 
inconsiderable '), minerrimus{ : minus af^er vet-errimus: -us), minuo' to make small, 
lessen, diminish, divide into small pieces ', Oscan menvum' to make small, lessen, 
diminish, divide into small pieces ' (probably with neglectful efor /); 



corn, minow^ reduce, lessen ', Middle Breton mynhuigenn, nbret. minvik^ bread without 
the crusts of bread '; 

ndd. minn, /77//7/7e "small, little, lean' is from the comparative back formation; Kompar. 
Gothic minniza. Old Icelandic minni. Old High German minniro^ fewer, less ', Superl. 
Gothic minnistr. Old High German minnist. Old Icelandic minnstr^ the smallest, least ' {-nn- 
from -nu-, Indo Germanic *m/nu- \N\t\r\ new real increase formation through -/zon-, -ista-). 
Adv. Gothic mins{*minniz). Old Icelandic minnr. Old High German Old English min^ fewer, 
less'; 

Old Bulgarian mbnfjb (f. mbhbsi) " smaller, less, fewer, younger ' {*mbnvjb-jb)\ 

here also Lithuanian maila^ sundries, little thing, small fish ', Latvian /77a/7e 'small fish', 
Slavic */77e/b-/rb in altserb. miokT shallow, having little depth ', Czech /77e//ry" small, 
shallow, having little depth ', melitT crumb, spall, crumble ', and Old Icelandic mjor, mjar, 
maer^ narrow, tight, slim, slender, thin' from *maiwa-, *maiwi-\ Tocharian B /77a/We "small, 
young '. 

References: WP. II 242, WH. II 92 f., Trautmann 165, 184. 
Page(s): 711 

Root / lemma: meih-6, meihu-, min(u)-, mim(ei)- 

Meaning: expr. root 

Material: Old Indie mimati" bleats, roars, shouts ', mimayat, amJmeV roared, bleated ', 

mayu-v(\. ' the bleating, roaring '; presumably maya-x^. 'steed', mayuram. "peacock'; m/n- 

mina- " speaking indistinctly through the nose '; 

gr. \x\\x\Zjoi " neigh ', |jipixM6(; " the neighing ', pi|ja^aaa xpsM^Tiaaaa (pwvriaaaa Hes., 
Mivup6(; 'whimpering', pivupO|jai, pivupi^u) ' whimper, whine '; from Latin minur(r)id' to 
twitter, to chirp, to coo ' (gr. loanword?) reshaped mintrid, -Tre ' squeak '; Old Bulgarian 
mbmati, mbmati^ stammer '. 

Maybe alb. memec^ mute ' a Slavic loanword. 

References: WP. II 243, WH. II 93; 
See also: s. also mu-. 
Page(s): 711 

Root / lemma: meih-no- 



Meaning: wish, intention
```


## [2026-09-07T15:50:42.805Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60660,60735p' POK_full.txt",
 "description": "Print Pokorny article with miyedha"
}
```


### [2026-09-07T15:50:42.860Z] TOOL RESULT

```
Meaning: to bind, attach 

Material: Old High German Old Saxon masca. Old English max, maescr' stitch ', Old 

Icelandic mQskvi^s:, 

Lithuanian mezgu, megsti^ tie, bind, knot, knit ', mazgas, Latvian mazgs^Vx\o{\ 
Lithuanian mazgytiWer. " knit ', makstyt/l\ax, wattle, braid', Latvian mezget, mizgef 
dislocate, luxate, crick ', mezgJV grow around, entwine itself around ' (russ. mazgart " 
spider'? s. Berneker II 28). 

References: WP. II 301, Trautmann 172. 
Page(s): 746 

Root / lemma: megh- 

Meaning: well-disposed, friendly 

Material: Gr. n£pi-r||J£KT£U) 'be unwilling ' (from *a-|j£KTOc; " unwilling '?); Gothic megs, 

Swedish mag^ son in law, husband of the daughter ' (compare French belle-mere). Old 

Icelandic /77ag/'" kinsman, relative through marriage'. Old English m^g. Old Saxon Old 

High German /77ag "kinsman, relative', etc.; Lithuanian megstu and megml, megtr like, be 

fond of ', megintr assay, try ', Latvian megV be good for, be suitable for '. 



References: WP. II 256, WH. II 5; Hj. Frisk Eranos 50, 1 1 f. 
Page(s): 707 



Root / lemma: mei-7: moi-. mT- 

Meaning: mild, soft 

Note: often with A, /?-, r-, /-extended 

Material: Old Indie mayas-u. " relief, pleasure, joy, lust', in addition *m(ilies(i!^(e)\u Old 

Indie miyedha-m. " saerifieial food ', Avestan myazda-m. "saerifieial meal'; as *mei-6'"o- 

Old Indie medha-rc\. " Fettbrijhe ', medhas-v\. 'saerifiee, oblation'; 

with A: eymr. /t?^/" blushful', df-fu/'bo\6' {*mdi-lo-)\ Old Prussian miJIs, Lithuanian mfelas 
and /77y/5s"dear, pleasant', meilet 'love', /77e//^5"affeetionate, loving', myliu, my/ef/"\ove\ 
pa-milstu, pa-m/'/t/" gro\N\ng fond of; Latvian m[/s {o\der ^-stem) and m/7s {irom *mielas) 
"dear', mHeflove', mieluot^ host '; Old Chureh Slavie /77//b "pitiful', russ. m/7yj^6ear', ete.; 

Alb. m/re^ dear, niee, kind ' a Slavie loanword (eommon alb. -I- > -r-) 

with n-. eymr. /77i^y/7 "friendly', aeorn. mu/n, /770//7 "dainty', bret. moan'th\n, tiny' {*mei- 
no-)\ Old Irish mm^ smooth, gentle' {*mT-no-)\ 

with r-. alb. m/re^goo6, beautiful'; Old Chureh Slavie m/rh^peace'; ablaut, aserb. m/jer 
{*mo/ro-), apoln. m/er^peace' (Old Lithuanian mieras, Latvian m/ers6s. are Slavie 
loanword); 

with t-. Latin /77/?/s"mild, soft' {*meit-)\ Old Irish moith, moeth {*mdit-) ds., also (?) PI. 
/77e(/)//7"fat, fertile'; eymr. mwydo {*meit-) " soften ', mwydion^ soft parts, external genitalia 
'; Latvian at-misV beeome soft ', at-mieteC soften '. 

References: WP. II 244, WH. II 96 f., Trautmann 174, 175. 
Page(s): 711-712 



Root / lemma: me-1 

Meaning: prohibitive partiele 

Grammatical information: prohibitiv
```


## [2026-09-07T15:50:59.185Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD mitis/mei ===\"; grep -n -i \"mitis\\|mitigate\\|ammunition\\|munire\\|moenia\" AHD_watkins1985.txt | head -20; echo \"=== AHD mei- roots ===\"; grep -n \"^mei-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for mitis, munire"
}
```


### [2026-09-07T15:50:59.243Z] TOOL RESULT

```
=== AHD mitis/mei ===
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1877:MITER mei-4 MITHRAS mei-4 MITIGATE mé6i-
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
=== AHD mei- roots ===
733:mei-'
```


## [2026-09-07T15:51:00.621Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT mayuxa ===\"; grep -n -i \"mayux\\|maixa\\|mayūx\" KNT.txt | head; echo \"=== PHD mex/myazd ===\"; grep -n -i \"mex\\|myazd\\|mezd\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "Grep Kent and MacKenzie"
}
```


### [2026-09-07T15:51:00.689Z] TOOL RESULT

```
=== KNT mayuxa ===
=== PHD mex/myazd ===
PHD.txt:4885:mādayār mādišt mādagīh mādagīg 1*mādag mādagwar mādar Abt, mex ābgēnag! mēhan mēzd may, meh Sahrestan! ‘mahist men- moymard! menidan mënög
PHD_mackenzie.txt:1010:Amextan, amez- ['myhtn', )myc- I M )myxtn, )myz-, N ,..,] mix.
PHD_mackenzie.txt:2613:gumextan, gumez- [gwmyhtn', gwmyc- I M gwmyxtn, gwmyz-] mix.
PHD_mackenzie.txt:3550:mex                             56                           mulAn
PHD_mackenzie.txt:3551: mex [myh I P myx, N -] peg, nail.
PHD_mackenzie.txt:3554:mezd [mYe)zd I N mez] offering, meal.
PHD_mackenzie.txt:6794:heroism gurdih.                                host mezdban.
PHD_mackenzie.txt:7075:meal bazm, cast, mezd, sur; evening        midget widestig.
PHD_mackenzie.txt:7110:mix abyoxtan, amextan, gumextan,               musk musk.
PHD_mackenzie.txt:7160:night raid sabixon.                    offering mezd, parag, us(t)Ofrit, zohr.
PHD_mackenzie.txt:7229:page (boy) redak, rahig.               peg mex.
PHD_mackenzie.txt:7277:pickled meat xamiz.                        Polaris Mex i gah.
PHD_mackenzie.txt:9164:muhrag                   \~(6        mezd, mizd                    ~
PHD_mackenzie.txt:9165:mang, moy                    "'r6    mezdban                \~fl)~
```


## [2026-09-07T15:51:12.901Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT knob/mayu ===\"; grep -n -i \"knob\\|mayu\\|mex \\|peg\" KNT.txt | head -20; echo \"=== KNT page 202 approx (leaf 202+15=217) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==218' KNT.txt | head -60",
 "description": "Check Kent for mayūxa"
}
```


### [2026-09-07T15:51:14.415Z] TOOL RESULT

```
=== KNT knob/mayu ===
1262:a golden helmet’. тауйга- *door-knob', Skt. mayükha- ‘peg’. havd- ‘friend’ m Haad-mani§ ‘Achaemenes’, Skt.
3312:DPc = Darius, PegsEPOLIS с: Trilingual, one Jine only, repeated 18 times on the window cornice of the same room of Darius's palace. Tm. Lex. 35-6 (1908); Wb. KIA xvi, 80-1 (1911); Hz. ApI 22-3 No. 9; Sen, OPI 89-90 (1941).
3317:DPi = Danis, PEnsEPOUIS 1: Trilingual, one line each, on doorknob of artificial lapis lazuli. Hz. Ap] 28 No. 10 and Plate 7 (1938); EFSchmidt, The Treasury of Persepolis 62-3 (1939); Sen, OPI 252 (1941).
3369:XPi = Xerxes, Perserouis 1: on a doorknob (or similar object) of artificial lapis lazuli, from the haremybuilding; OP and Elamite, each in 1
4102:DPi = Darus, PERSEPOLIS т. mayüxa : kasakaina : Dárayavahaus : XShya : уїйїуй : karta TRANSLATION OF DPi: Door-knob of precious stone, made in the house of Darius the King.
5774:тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, perhaps to Skt. mi- (pres. minétz) ‘fix (as in the earth) ($100, 5148.11); ef. Hz. Ар] 258-9. mayüxa пзш. DPi; XPi.
=== KNT page 202 approx (leaf 202+15=217) ===
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps,
```


## [2026-09-07T15:51:24.621Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'mayüxa- sb' in p or 'mayûxa- sb' in p or \"тауйта- sb\" in p:\n        print('leaf(0-based)',i)\n        print(p[:400])\n        print('...')\n        print(p[-400:])\nEOF",
 "description": "Locate Kent leaf for mayuxa"
}
```


### [2026-09-07T15:51:25.888Z] TOOL RESULT

```
leaf(0-based) 226
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm.
...
 VI). Малаа nsm. DB 3.12; 4.24.  Mürgavaibis ipm. DB 3.16.
Margu- sb. ‘Margiana’, a province of the Persian Empire: Elam. mar-ku-i$, АКК. mar-gu-’, Gk. Mapyos, Мару:аиу (S31, $153.1). See also Márgava-. Margué пэт. DB 2.7; 3.11. Mar- gum asm. DB 4.25. Margaw lsm. ($114) DB 4.25; DBj 5f.
marta- ріс. as ad]. ‘dead’: Av. marata-,-N Pers. murd, Skt. mrid-, Gk. Вротос (for *Sparós, with vowel assimilat
```


## [2026-09-07T15:51:35.443Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(222,230):\n    hits=re.findall(r'\\b(\\d{3})\\s+OLD PERSIAN|LEXICON\\s+(\\d{3})|\\b(\\d{3})\\s+LEXICON', pages[i])\n    print(i, hits[:5], pages[i][:80].replace('\\n',' | '))\nEOF",
 "description": "Find page headers in Kent leaves"
}
```


### [2026-09-07T15:51:36.825Z] TOOL RESULT

```
222 [('', '199', '')] -. — fra&aram asn. XPf 26f, 37. | Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-
223 [('200', '', '')] 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 
224 [] 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54
225 [('202', '', '')] BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2
226 [] 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] 
227 [('', '203', '')] ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1
228 [] so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a provi
229 [] d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101;
```


## [2026-09-07T15:51:48.924Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo \"=== AFM maida ===\"; grep -n \"مائدة\\|المائدة\\|مايدة\" AFM_pages.txt | head -20",
 "description": "List refs dir and grep AFM for maida"
}
```


### [2026-09-07T15:51:48.995Z] TOOL RESULT

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
=== AFM maida ===
2872:خوان اى مائدة
```


## [2026-09-07T15:51:50.390Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ maida ===\"; grep -n -i \"mā'ida\\|maida\\|mâ'ida\\|ma'ida\" FVQ_pages.txt | head -20",
 "description": "Grep Jeffery for maida"
}
```


### [2026-09-07T15:51:50.462Z] TOOL RESULT

```
=== FVQ maida ===
```


## [2026-09-07T15:51:57.543Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM ctx 2872 ===\"; sed -n '2860,2885p' AFM_pages.txt; echo \"=== AFM myzd/mayda ===\"; grep -n \"ميزد\\|مايده\\|ميزَد\\|مَيزد\" AFM_pages.txt | head",
 "description": "AFM context around maida"
}
```


### [2026-09-07T15:51:57.601Z] TOOL RESULT

```
=== AFM ctx 2872 ===
5 الهيئة 3 873 86 وقيل فيه طرّذ
( الطرَازِدان ) - الميزان تعريس 03567
* 9 الرجل عدا عدوًا سُديدًا من الفزع مأخوذ عن ترْساً اي `
ܛܐ
ܸ ܐܨ الليل أظلم ( وطرمش ܕ)ܟܐܨ ܨ ) ܐܝܐܝ فيه ( ܕܐܨ .| َّ )
النللية أو تراكها كل ذلك مأخوذ عن تار شب اي ليل مظلم
(الطارمة ) ܥ من ܚܝܢ ܡܝ ܟ تارم
. (الطِرممدَار) المتتكثر ها لم يفعل وقيل ܝ مركب من تَارْمِيغْ اي الضباب
وق حار اك طعت
( الطازّج) معرب تازه ومعناه الطري ܙܘ :ܪ القري والكردي تازه
* (ܫܐܚܐ ܕܐ وطسًا) نكم مأخوذ من تأسه ومعناه ܐܝܕ والتتخمة
( ܐܝܐ ܢܳܐ ) قصعة كيرة اول عليها الطعام ܨ ل اى عطس ومن
خوان اى مائدة
( الطسترج ) اإلناحية مركت من لق 111 2 005 `
(الطين) 1 - اليد تعريس تتشت 5843 «الطشيت والطسة
3 ܝ 5 0 ܝ والتري تاس 39
305 والكر دئٍ 3 وطشت. وطننتث ܕ ܟܠܐ ܢ= (| (× =
( ܐܨ والطأسك) ܢܓ شيل م 8 ن الخراج على < او شه
ضر يدة مغاوفة الال ضح 4 5 ܨ ܥ 0 بال به 4 البسمن 4
الارائى ܛܣܩܐ
00 دة من الله شيعن علنها الموشق تعريب تاسته
( الطغرا ا 2 على مناشير الساطان ومسكوكاته | يدر شها أسمة
03
ܣ ® ± 00070 95 10875
كلع ومعتاء الا
ܨ )0 5 9 5 لا 39( 350 0 دايا من صوفب ܐܢܐ
=== AFM myzd/mayda ===
```


## [2026-09-07T15:51:58.311Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Table\\b\\|a table\" FVQ_pages.txt | head -20; echo \"=== FVQ arabic maida ===\"; grep -n \"مائدة\" FVQ_pages.txt | head",
 "description": "Grep Jeffery for table entry"
}
```


### [2026-09-07T15:51:58.372Z] TOOL RESULT

```
4243:2 So DDHI in the Has Shamra tablets.
4692:1 And now also in the Ras Shamra tablets.
6468:1 So also the D^t27 of the Ras Shamra tablets.
7319:mr u, to rebel of the Amarna tablets).
8919:as in Phon. and in the Ras Shamra tablets, and from the Heb. came
9180:Table.
9182:is to a table which Jesus brought down for His disciples.
9190:Table, e.g. ThR* : V?IIJfflfliC> while Noldeke's examination
=== FVQ arabic maida ===
```


## [2026-09-07T15:52:04.687Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9160,9215p' FVQ_pages.txt; echo \"=== page tags near ===\"; awk 'NR>=9100 && NR<=9200 && /\\[pdf page/' FVQ_pages.txt",
 "description": "Read Jeffery table entry"
}
```


## [2026-09-07T15:52:05.739Z] TOOL CALL #22: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FVQ'],ensure_ascii=False,indent=1))\n\"",
 "description": "Get AFM/FVQ offsets"
}
```


### [2026-09-07T15:52:06.283Z] TOOL RESULT

```
we may judge that the word was used in this technical sense among
Muhammad's contemporaries.
*> %
(Lut).
Occurs some twenty-seven times, cf. vi, 86.
Lot.
Always the Biblical Lot, whose name some of tho authorities
derive from (cf. Raghib, Mufraddt, 472; ath-Tha'labi, Qisas, 72),
but which Jawhari recognizes as a foreign name. 3
1 Cf. also ash-Shammakh, xvii, 13, in Geycr, Zwei QedicMe, i, 136.
2 Vide also Fraenkel, Vocab, 21 ; Cheikho, Nasraniya, 221.
8 So al-Jawaliql, Mu'arrab, 134 ; al-KhafajI, 175.FOREIGN VOCABULARY OF THE QUR*AN 255
The name is apparently unknown in pre-Islamic literature, though
it must have been known to the circle of Muhammad's audience. 1
From its form one would conclude that it came from the Syr. %^ol
rather than the Heb. Bl /, 2 a conclusion that is strengthened by the
Christian colouring of the Lot story. 3
,>
S^Tl^i (Md'ida).
v, 112, 114.
Table.
A late word found only in a late Madinan verse, where the reference
is to a table which Jesus brought down for His disciples.
The Muslim authorities take it to be a form Icli from
(cf. LA, iv, 420), though the improbability of their explanations is
obvious. It has been demonstrated several times that the passage
v, 112-15 is a confusion of the Gospel story of the feeding of the multitude
with that of the Lord's Supper. 4 Fraenkel, Vocab, 24, 5 pointed out
that in all probability the word is the Eth. ^tiK, which among
the Abyssinian Christians is used almost technically for the Lord's
Table, e.g. ThR* : V?IIJfflfliC> while Noldeke's examination
of the word in Neve Beitrage, 54, has practically put the matter beyond
doubt. 6
Addai Sher, 148, however, has argued in favour of its being taken
as a Persian word. Relying on the fact that aA*U is said by the
Lexicons to mean food as well as table, he wishes to derive it from
Pers. ftf^t, meaning farina triticea. 7 Praetorius also, who in ZDMG,
Ixi, 622 ff., endeavours to prove that Eth. lt\f: and the Amh. *?#
are taken from Arabic, takes a*xf U back to Pers. J^A 8 (earlier pro-
Horovitz, KU, 136.
But see Sycz, Eigennamen, 37.
Vide Kiinatlinger, " Christliehe Herkunft der Kuranischen Lotlegende," in
Roc nik Orjentalistyczny (1931), vii, 281-295.
Noldeke, ZDMG, xii, 700 ; Bell, Origin, 136.
Vide also his Fremdw, 83, and Jacob, Beduinenleben, 235.
Vide also Wellhausen, Reste, 232, n. ; Pautz, Offenbarung, 255, n. ; Vollers,
ZDMG, li, 294 ; Cheikho, Nasraniya, 210.
Vullers, Lex, ii, 1252.
Vullers, Lex, ii, 1254.256 FOREIGN VOCABULARY OF THE QUR*AN
nounced mdz), through forms A~, JL*4, and d A<. Now there is a Phlv.
word 53^5 myazd, 1 meaning a sacred repast of the Parsis, of which
the people partake at certain festivals after the recitation of prayers
and benedictions for the consecration of the bread, fruit, and wine
used therein. It seems, however, very difficult to derive aA) U from
this, and still more difficult from the forms proposed by, Praetorius.
Noldeke rightly objects that the forms miz and mdz which Praetorius
=== page tags near ===
```


### [2026-09-07T15:52:07.793Z] TOOL RESULT

```
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
{
 "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
 "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"
 ],
 "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)",
 "covers_etymology": true,
 "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.",
 "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"
}
```


## [2026-09-07T15:52:20.137Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9215,9250p' FVQ_pages.txt",
 "description": "Read rest of Jeffery maida entry"
}
```


### [2026-09-07T15:52:20.174Z] TOOL RESULT

```
Noldeke rightly objects that the forms miz and mdz which Praetorius
quotes from the Mehri and 'Umam dialects in favour of his theory,
are hardly to the point, for these dialects are full of Persian elements
of late importation. Praetorius has given no real explanation of
the change of z to rf, whereas on the other side may be quoted the
Bilin mid and the Beja mes which are correct formations from a stem
giving 'TfftJt in Eth., and thus argue for its originality in that
stock.
(Md'iin).
cvii, 7.
Help.
This curious word occurs only in an early Meccan Sura, though
v, 7, is possibly Madinan (cf. Noldeke-Schwally, i, 93), and the Com-
mentators could make nothing of it. The usual theory is that it is
a form ^vft from A.*<, though some derived it from j.
Noldeke, Neue Beitrage, 28, shows that it cannot be explained from
Arabic material, 2 and that we must look for its origin to some foreign
source. Geiger, 58, 3 would derive it from Heb. ]11??3 a refuge, which
is possible but not without its difficulties. Rhodokanakis, WZKM,
xxv, p. 67, agrees that it is from Hebrew but coming under the influence
of A) J*A (cf. Aram. &MNQ ; Syr. ]*\&), developed the meaning of
benefit, help.*
1 West, Glossary, 222.
2 Fleischer, Kleinne Schriften, ii, 128 ff., would have it a genuine Arabic word, but
as Noldeke says : " aus dem Arabischen lasst sie sich nicht crklaren, wio denn schon
die Form auf em Fremdwort deutot."
8 So von Kremer, Ideen, 226. The word is used by al-A'sha, and Horovitz, JPN,
221 if., thinks Muhammad may have learned the word from this poet.
4 So Torrey, Foundation, 51.FOREIGN VOCABULARY OF THE QUR*AN 257
cUJlJ. (Malik).
xliii, 77.
Malik is the angel who has charge over Hell. ^ ^
The native authorities derived the name from ^UJU to possess,
rule over. This root may have influenced the form, but the source is
doubtless tjie Biblical Moloch. The Heb. form is "5]7?fo, and it may
possibly have come direct from Heb., 1 but the Syr. r^ (PSm, 1989)
```


## [2026-09-07T15:52:29.216Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in range(150,162):\n    p=pages[i]\n    print('=== leaf',i,'===')\n    print(p[:300].replace('\\n',' | '))\nEOF",
 "description": "Inspect Addi Shir leaves near p.148"
}
```


## [2026-09-07T15:52:30.665Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON* ; echo \"=== grep MON میزبان ===\"; grep -c \"میزبان\" MON_part1.txt MON_part2.txt; echo \"=== grep میخ ===\"; grep -c \"میخک\" MON_part1.txt MON_part2.txt",
 "description": "Check Mo'in files"
}
```


### [2026-09-07T15:52:30.757Z] TOOL RESULT

```
leaves 198
=== leaf 150 ===
_ 4¿ ܙ - | وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 ` | (ص: ܥ ) | 6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال | 2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال | اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب | الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن 
=== leaf 151 ===
ܢ ܀ © | ܝܝܚ | لغتان فيه ٠‏ والظاهر ان الافظة ارامية الاصل ذعي ܐܢܒܘܒܐ باللغة البابليَة | ܕ ܐܝܟ ܨܐܬ و > دنه حدم ܐܬܐ .ܕ % ܨܝ ܨ ܝܨ 811 )ܙ( | ومعئاها الأننوبة والمزمار ܨ ܐ من ܢܒܒ اي صرخ وتخ ٠‏ .وان ܒܝܒܐ | و ܒܘܒܝܐ اى المجرى والة: ناة 885 | ܗ ܐܐ ܨ ]711 (راجع كلمة | ندب في هذا ܐܐܝ “راجع @ فرئكل ص 7١:‏ ) | ܨ عر شجرة 0 و
=== leaf 152 ===
ܒ ܙ( ܘ | -- | + (الكراز) الشرف المتكير واعلبان 35 ` 72410 97 }܆ | المهذار ܐܬܐ | ܣܣ معرب مرك ومنة 0 0 | 01200010004 واللاتيني 05 والفرة سي 15 و الايطاليالي 1121150 | والاتكايزي 115 واطرمالي 11 ܥ و ككردي ܥ والارائي | ܢܪܩܝܣ ܙܝ ܢܪܩܘܣ والارمنى /7///404 0 عر 5 كس وان | دان اي وعاء الأرجس : | التأرجيل ) ܐܧ( الهددي 0 اردق 
=== leaf 153 ===
هه 00 ܐܓ | أن طاف اقطار المسكونة اتتهى الى اذور 9 وأعر 43" 0.33 | حل عالتفى اعلهة الشرقية منة عرش مرضع .2 لس نا به الملوكة ووضع على رأسه | تاج المرضع ܬܐܨ النفيسة وجاس على العرش امنصوب له ܶܪ | طلعث الشمس | فضر بث ܣ التابم 057 امنتلاً ذلك الوضع نورًا وضماء ٠‏ فاستبدع :3 | المدظر فاستسغدوا ܛ || ܐܕܬ ا نورورًا ܥ ا
=== leaf 154 ===
ل ܕܙܘ | شت | الصحاج :« والذي تراه كالطر يق من النمل نفسها ٠»‏ والنمل اذا جاء منها واحد في | 39 0 ܕܟܐ ܨ ܠܐܝܐ والميّة. ܢ الواضح : معربان عن | ÷ ن اي ` الأو | $ 6 نات 98 7( 3:77 ونون يقترن | 391 ܕܐ لهُ بالتركية « اغسطوس كلى ܙܝ ܐܥ كل ».وان كان زهره ابيض قيل | له « اق كل » وان كان اي ` كل 0 | ل داوس 03 قوي © |( الأزهر
=== leaf 155 ===
حا ¿ © ܐ ܘܡܐ | * 5 السكران ܐ :¥97 اي سكر ومن بان (ويقال .50 | وان» أي صاحب | 5 بقل طيّب 3[ 1:3 وهو ايضاً ® بالتركيّة وك | بالكردة و سكع بالاراميّة و سلح» بالسريائّة الدارجة او ܝܐ بوورون | باليونانة 1161111329 بالرومسة 11111119 بالاتكايرنة وع111611 بالفرنسة و 1111176 | بالكرمانية و 111@1112 بالايطا ® و اوباب لار
=== leaf 156 ===
ܚܝܚ © ܘ | كك | 11 ‫ 0[ )3 معرب وده | (3) الكتات الذي 4 فيه تعريب ثامه وبنوا.منة فملا وقالوا غقّ | 3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس | جد ( العا 096 ܦ £ حجم الخردل .0 (08(8421¶÷ 0 2 93 | 106 ) تعريب 3( اللبز. والمب المذكور سني به لاه | ܝܣ | (التوردجة ) الضميمة وما أف من كل شىء ء 5 لورده | (التَاوق ) ا
=== leaf 157 ===
ܢܐ }ܘ ܐ ܝܝ | :3 تر | يصبغ به ومن ܨ وهو اسم »ܓ 21 فل ܗ بنيل لان الورقة | مضموغة | الحنا حين ( حيط المحبظ ) ٠‏ وقال صاحب البيغان القاطع :« النيلوفر ورد معروف يظلهر | في طلوع الشمس فوق الماء ويزهر وفي غرويها يع في 2( وقيل اله عند وقوعه | في الاء يلقي طائر ويسقظ مكانة ويقم 2 مسترياً الى ان يظهر النيساوفر فيطير | ܫܠ
=== leaf 158 ===
سب ¥ © |{ ܗ | 0 قبل ܟܪ ܀ ܫ )1:1 ܥ وهم || ܡ . ٠وقبل‏ عظلاء ٠‏ ܐܩܝ وقيل | ܢܣ وقبل ܗ نار الأجوس الواحد هر ربد ( حيط المحدظ ) ٠‏ والمعنى الاخار ® | لان الفارسي 7 ابد إمام خدم نار المحجوس وسيدهم ܨܢ 0 ܨܝ | + ( احرج ) الأحق تعريب هرك | + (الرْد) !£ الأمغل مكزت يصع نا افارفكة جر وتر متش حادق | كك | + لان 5 1 ببن الشعير ܒ
=== leaf 159 ===
_ )ܘ | ܝܚ | العرض بق رات او ار ل ا | ܣ تعر يب و 5 ܐܪܝ | ( هما بون ) لفظة فارسيّة معناها العزيز والسلطان ܘܬ من هما اي عنقاء ومن | يون وهي اداة النسبة :فقيل ان همايون في الاصل اسم طائر من وقع عليه ,]‫ ; | ول ال على للراتب ولذا أطلق على العزيز والسلطان | ١‏ لمئيّان) فارسيةُ هميان وهو كيس حمل فيه 2 ومنة | ܗܡܢܢܐ | ܐܸܝ
=== leaf 160 ===
ل | ܘ | صمت | ,3 ܚܝ | و3 ( الحاوآت 22 الذى يدق شه الدواء وغاره 2 هاون ܦ 4 ة هاون | بالتركة 313 بالكردنة | د ( | ܙ ) ܐܕܒ ^ 7 32 هيرون 2 بضصرب °ܝ القصب علو | الداخل ̄ܒ 4 زم ر سّليه با لقَطن :رفير 354 | + ا ( 00:0 وقمل اسم اداته 0 56 هس وهو الحراث | ܒܝܒܗ ® (م 026 © جرمعى | 153 | ( الوبر) فارسيتة وبر 905 اصغر 7 »× 0:3737
=== leaf 161 ===
ܡܗ ܀ ¥ ܐ| وه | باب 0 | 1 | والمتفر ٠‏ و يرادفة التي ينان وقالوا فيه يس : | ( المَارَّج والمَارّق ) القلى والسوار تعريب بآرَه | ( الإبأرجة).مسجون.مسهل معرب ااره ومنة اللدر الى 201 | ( الي تدج ). السوات وداه صرمت رانده عمقي عر الا | ( اليَرمنآن) نسيج رفيع من ܐܝܠܨ ܨ فارسيّة ومعناه ܩܠ ܘܬܐ ܚܨ به لاله | ما يهندى ٠‏ واأشه
```


### [2026-09-07T15:52:30.820Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== grep MON میزبان ===
MON_part1.txt:5
MON_part2.txt:4
=== grep میخ ===
MON_part1.txt:0
MON_part2.txt:25
```


## [2026-09-07T15:52:41.328Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (149,150):\n    print('=== leaf',i,'===')\n    print(pages[i])\nEOF",
 "description": "Print AFM leaves 149-150"
}
```


### [2026-09-07T15:52:42.712Z] TOOL RESULT

```
=== leaf 149 ===
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
( لوم ) ببى الشبع فارسي تكلموا 4 0:27 ܨ
(ليَة) فشر بشىء من ܇ الأدرية ܣ من ܐܝ اي الخير 1:0 يبه اي
ܝ
( الميبحتج » العنب المطبوخ مركب من تمي )1١(‏ اي <> ومن إبخته اي مطبوخ
وهو عسبل العنب ١‏ كن الاطباء يغلونة مرة ثانية »= والعسل
4 فشحة مجبهة همده 18 رلم اليل قل كلمن انام 1ه
ܨܐܘ واضبطرابه عند السباق٠وقيل‏ هو من الوَدْن لان الل رون فيه «بحبط
الجيط ‏ ܢܘܛ رأبي ان الميدان ܠܚܢ الاصل وهر مركب من ,مي اي الشراب ومن
:0 وهى : الأدوات ܐܛ تاحق الاسماء ܐ¿ على 5 13 £ اول الام
5 3 5 .يشر بون فيه امن ثم اطلتوم على الفسيعة المدء اسان
واعب الخيل ٠‏ وهر مردان بالتركية والكردبة
(( ܨ » الطعام والحوان عليه الطعام ٠‏ قيل ܐܬܐܬ مشتقّة من ܘ ععنى اعطاه
دعي فاعلة ܬܶܢ مفعولة لان الماك ]ܪܬܐ للنامن اي اعطاهم اياها , «وقيل من ماد كيد
اذا تحرك ( اقرب الموارد ) انها | معربة عن ܚܬܪܘ وهو خبز المسميذ با لفارسة 1
܀ لإن صاحب البيت اذا ܐܘ ضيف ܪܟ له من خْبز ܢܒ ܐܰܢ على الموان وأطلقت
5 * بالفارسة على الموان والذي يخدم ( 55 المانيدة 7450("
)١‏ وشرب الفاريي مي 0 0 4 اي سك واامونالي 40¡ أي
1
ܝ
=== leaf 150 ===
_ 4¿ ܙ -
وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 `
(ص: ܥ )
6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال
2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال
اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب
الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن آب اي ماء ܕܝܙܝ النسمية
ظاهر (راجع ` لكل :4 )
ܣ 10 ® 099 2 من مي اق شراب بم الى"
.܀
ܗܐ
9
١‏ ابابا 6 فول الذي 'يككل به فارسيّة ميل ` = ܟ اله
معرب عن اليونافي «</نم٠‏ فالفارمي ايضاً ܨܕ ܝ عن اليونافى وملة ايضاً
ܡܝܠܐ بالارامسية .وما الم للمسافة فهو تعر يب 00 509 (© ܘܐ
بالارامية
*« (المثاء) عق جوقر الزجاج تريب الفارسي مثا وير به 4 الفرني 0081
والايطا ليالي 56 ܙ 1܀] اذى مرمئ السيةء+ة فأخرذ 9 ن الادائي ° ܠܡܐܢܐ والارائي
4 4 مالحوذ من اليوالي ܬܨ(
( ® نات له ورق سُدِيهِ بورق الكر رم البري تعر بيب 8596
باب النون
± 7
» ( الا نوب) ما بين الكعبين م الل اي ܝ النبات ما بين عقدتنه
ويستعار كن ܥܕܝ وسيب ل لر ܟܝܢ ܚ ܨܝ || ܀ ^ له . ܘ ,ܝܝ ܐܟ ܢܬ
المسداة 90 4 :3 ويطاق ايأ على ܐܳܝܰܐܺܝܢ الاناء واللولى ٠‏ والا تنب 0477
```


## [2026-09-07T15:53:04.509Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/BQT/ && for f in incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt incoming/BQT/BQT_v3_pages.txt; do echo \"== $f\"; grep -c \"\" $f; grep -n \"\\[pdf page\" $f | head -3; done",
 "description": "Inspect BQT vol 3-5 page files"
}
```


## [2026-09-07T15:53:04.554Z] TOOL CALL #28: Bash

```json
{
 "command": "head -40 tools/ref_page.py",
 "description": "Check ref_page tool usage"
}
```


### [2026-09-07T15:53:05.803Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
== incoming/BQT/BQT_v4_pages.txt
22553
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
== incoming/BQT/BQT_v5_pages.txt
10090
1:[pdf page 1]
3:[pdf page 2]
16:[pdf page 3]
== incoming/BQT/BQT_v3_pages.txt
51425
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
```


### [2026-09-07T15:53:05.843Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
```


## [2026-09-07T15:53:08.902Z] TOOL CALL #29: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2076 --image 2>&1 | tail -60",
 "description": "Fetch Borhan page 2076"
}
```


### [2026-09-07T15:53:15.975Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 159; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2076.png
REF: BQT:2076  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 159  OCR-lang: fas

میرآش خف پا
گیرمیگویند.* است که دربان هشت بهشت باشد .
میر آش ۱ -« بکررای قرشت.شخسی مور قفتمین - کنایهاز کوکب زحل
راکویند که پانک آش زد یعنی کی که مروم ۷ است چه او در فلك هفتم میباشد .
را بآش خوردن طلید . میران - بکر اول و فتح رای قرشت,
بام داماد و است ۵ کنایه از |
۱ ۰ ام داماد قیصر روم است - - و ۸ رد آمیر
۵ ه با دال ۱ وزن م
:۰ کر ی دال بح اروت پیش خسرو وامیرحن دهلوی هم هست ۹۱ ۰
بینی » نوعی از خیری بنفش باشد وآن کلی‌است ها 2
معروف - وبافَةٌ حریری را نیز گویند که بیشتر ز « با نالی‌مجپول وسکون زای نقطه
زان آترا پیراهن کنند وپوشند .۶ دار » بمعنی معمان است پعنی‌شخصی که یافت
َ ۶ ۳ پا کی‌رود ۷ - واسباب مهمانیرا هم کنته‌اند۷ -
ههر و 4 * - با اول بتانیرسید دنت | وکرسیرانیزکوین دکه‌بربالای آن طمام خوردد۸
برد کنیدم و یاف ده ۰ ی 0 باشد که - و مغفف تمیز هم‌هست ۸ - و پیشاب و شاش
مصف مور است و از حشرات‌الارش باشد. را نیز کویند ‎٩‏ و بمربی‌بول خوانند - و امرباین
یره - بر وزن خیره » بمعنی خواجه | معنی‌هم هت بعنی بشاش وبول کن *۱- وبمعنی
باشد که کدخدا و رئیسی وصاحب خانه است ۴ ‎ -‏ بول‌کننده نیز آمده است۰۱۱
و بممتی عداوت و کینه عربی است ۴ . میز بان ۱۴- پابای ابجد بروزن مهمان,
میرظهشت بهشت - کنایه ازرضوان | ضیافت کننده باشد پعنی‌شخسی که مردم‌را ضبافت
‎٩‏ -رك : هیر . ۲ "مور (ه.م.) ۴ -قی : بختیاری 121۲ ( شوهر »
مرد) - ۴ - (ع) ۸ میره بکسر اول بردن خوراکی و بار خوراکت » « شرح قاموی».
بمعنی‌اول 8/1171 ظ. مصحف «میرولید؟ اس ت که نام یکی‌ازس سکرده‌های نامی‌بونان
درجنگه «پلانه» بود. اين‌نام درشاهنامه‌آمده «فهرست ولف» و راك: «پیریا . داستانهای‌ابران قدیم
ده ‎٩‏ - تیه ‎٩‏ میر » (ه.م.) ۷ - ظ.. از اوستایی 12787208 ( میزد )
ر3 : میزد » و رك : میزبان . ترکی مأٌخوذ ازفارسی «* میز > و * میزبان » « حسین‌کاظم قدری».
۸ - تمیز دز مخفف « نمییز ؟ عربی است . ‎٩‏ - رك : میختن » کمیز ؛ کردی
عنط ( خاش ) « ژابا یس2۱۱ > ور4 : ژابا س ۳۹۹ » اوستابی -33862 ( شاشیدن ).
*- امر از ۶ میختن » (ه.م.) ۱- اسم فاعل مرخم بجای « میزنده ».
میر - یک اول » مغفف « امیر > (ع) ؛ در عربی نیز « مین » بمعنی آمیر آمده
وی ج ۲ ص ۹۲۸ > ؛ آمیر » پادشاه :
یکی مین بود اندر آن شهر اوی سراقراز و با لشکر وآبروی .
قردوسی طوسی « شاهنامةٌ بخ اج ۷ ۱۹۶۹
در میر و وزیر و سلطان را ی وسیلت مکرد پیرامن .
« کلتان س ۳۹
2 میرز! - بکر اول » از : میر ( مغغف آمیر ) (۸.م.) ۲ زا ( مشفف زاد "* زاده )
۶« اسقا٩:‏ ۲ ص ۸۳ *؛ امیرزاده » این کلمه از زمان تیموریان ظاهرآً رواج پافته . درعهد قاحاربه
هرگاه پیش از نم‌کسان ذ کر میشد پممنی‌آقا بود : میرزا محمد , میرزا جفر ؛ و اکر پس از
با مکان میامد دال برشاهزا د کی ( امیرزا دکی) بود : محمد علی میرزا ۰ آحمد میرزا .
```


## [2026-09-07T15:53:27.663Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2073 --image 2>&1 | tail -55",
 "description": "Fetch Borhan page 2073"
}
```


### [2026-09-07T15:53:34.874Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 156; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2073.png
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
```


## [2026-09-07T15:53:48.776Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" MON_part1.txt | head -3; echo \"--- count pages:\"; grep -c $'\\f' MON_part1.txt; echo \"=== میزبان ===\"; grep -n \"میزبان\" MON_part1.txt MON_part2.txt | head; echo \"=== مائده ===\"; grep -n \"مائده\" MON_part1.txt MON_part2.txt | head",
 "description": "Grep Mo'in local text"
}
```


### [2026-09-07T15:53:50.011Z] TOOL RESULT

```
--- count pages:
0
=== میزبان ===
MON_part1.txt:55797:میزبان است. (افا.) در ترکیب به معنی 
MON_part1.txt:70190:که به وسیلةٌ آنها پوست بدن میزبان خود را 
MON_part1.txt:77797:که مانند رشتمای: دور ساقه نبات میزبان 
MON_part1.txt:77800:به وسیلهٌ مکینه‌هایی مواد غذایی گیاه میزبان 
MON_part1.txt:88136:گیاه میزبان خود اخذ می‌نمایند. برگ‌های 
MON_part2.txt:53364:سخت بوست که میزبان واسط انگل این 
MON_part2.txt:53370:روشن می‌باشند.) نام علمی این میزبان واسطه 
MON_part2.txt:59386:میزبان. 
MON_part2.txt:70193:میزبان: -(2)-۱۱]7 [میز + بان < بان س. 
=== مائده ===
MON_part1.txt:57805:خوردنی» مائده. 
MON_part1.txt:97157:عقب مائده. 
MON_part2.txt:41631:مائده: (6-)020012 [ع. مائدة: ف. مایده| 
MON_part2.txt:41634:مائدهٌ مسیح: روایت کنند که تا مدتی هر روز 
MON_part2.txt:60404:سمار. ( کذ.) مائده‌ای که از آسمان به جهت
```


## [2026-09-07T15:53:55.599Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON مائده ctx ===\"; sed -n '41625,41640p' MON_part2.txt; echo \"=== MON میزبان ctx ===\"; sed -n '70185,70205p' MON_part2.txt",
 "description": "Read Mo'in entries"
}
```


### [2026-09-07T15:53:55.670Z] TOOL RESULT

```
=== MON مائده ctx ===
به حد نصاب کر باشد طاهر و مطهر است 
مگر آنکه رنگ يا بوی یا طعم آن تغییر کند 
و در این صورت به محض برخورد با 
متجنس نجس می‌شود. این نوع آب را 
مضاف گویند. ماء معین: آب روان و پاک 
ماء ورد: گلاب. 
مائده: (6-)020012 [ع. مائدة: ف. مایده| 
(ا.) خوردنی. خوانی که بر آن طعام باشد. 
یه نش کی * نعیم بهشتی: نعیم ااشتهاتی؛ 
مائدهٌ مسیح: روایت کنند که تا مدتی هر روز 
به وسیلةً ابر خوانی بر عیسی(ع) نازل می‌شد 
و در آن ماهیی بود بریان بی‌خار که روغن از 
او می چکید. نزدیکك سر آن نمک و متصل 


است 
=== MON میزبان ctx ===
راست ودن و محادی هم بودن دو طرف 
چبزی مانند دو کفه ترازو. (عم. اصط. 
جاهل‌ها) بر اثر خوردن مشروب يا کشیدن 
شک نشاه لازم را حاصل کردن. میزان 
ترکیبی: (م.) اگر هر یک از ضربها به 
قسمت تقسیم شود مبزان‌های ت رکسی به 
وجود می‌آید» مثل یک سیاه نقطه‌دار که به 
سه چنگ تقسیم می‌شود. 
میزبان: -(2)-۱۱]7 [میز + بان < بان س. 
قآ تیک یک ً 
چند تن را به مهمانی خود دعوت و پدیرایی 
کند؛+ ضافت کننده؛ مق. مهمان» میهمان. 
مبیرد. ۵ (.) (زردشتی) ندر و 
تقدیمی غیر مایم و فدیه» چیزی خوردنی در 
مقابل نذر مایع و آشامیدنی (زور). مجلس 
ق ع ۳ 
میزر: 7۳۵۲ [ع. مگرر | (.) پارچة ساتر 
بدن» پارچه‌ای که به کمر بندند؛ ازار. شالی 
که بر سر نندنده دستار. عمامه. کهن مبزر: 
پر ۰ 
میزک: (7-20)82]< (ا.مسصف. ۱.) شاش»
```


## [2026-09-07T15:54:07.952Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 8760-8780 ===\"; sed -n '8760,8785p' HRN.txt; echo \"=== HUB 7010-7025 ===\"; sed -n '7010,7025p' HUB.txt; echo \"=== HUB 7965,7980 ===\"; sed -n '7965,7982p' HUB.txt",
 "description": "Read Horn and Hübschmann on myazd"
}
```


### [2026-09-07T15:54:08.013Z] TOOL RESULT

```
=== HRN 8760-8780 ===
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
=== HUB 7010-7025 ===
§ 91. Ap. d bleibt im Np. als d
a) im Anlaut, z. B. dad *Gerechtigkeit' = ap. ddta-^
dast 'Hand' = ap. dasta-j zd. zasta-, u. s. w., vgl. H. 518
—599.
b) im Inlaut nach n^ z, zi handam *binde' = zd. ban-
dami ; landa 'Sklave' = ap. bandaka- ; andam *K5rper, Glied'
= zd. handcLma-^ u. s. w. ; duzd *Dieb' = zd. duzd& *Bose-
wicht*; muzd, muzd *Lohn, Preis' = zd. mlzda, ksl. mtzda,
skr. mtdha'\ miyazd 'Gelage* = zd. myazda-, skr. miyedha-;
nazd *nahe = zd. nazda-, skr. comp. nediyas-] sassanid.
Hormizd = ap. a(h)uramazda; azdahd *Drache* = arm.
aMahak, zd. azis dahako, u. s. w. In alien diesen Fallen
stand im Ap. der Verschlusslaut d.
§ 92. Ap. d hatte nach Vokalen die Geltung als
Spirans J und wurde im Paz. und Np. zu h oder y = i.
a) zu A: diham gebe* = zd. dadqmi^^di^. ipt. dadatuv
=== HUB 7965,7980 ===
als r:
a) Iran, zd (= idg. s oder Dental -f d, dh) = ap. np.
zd; iran. zg = ap. zg = np. yz: sassanid. Hormizd =
phi. Ohrmazd, ap. A(h)uramazd(l, arm. Ormizd, alter Ara-
tnazd; arm. Artavazd = zd. Asavazdah-, gr. '^praovdadrjg
(Strabo), ap, ^Artavazdah-; np. nazd 'nahe* = zd. nazda-;
phi. arm. azd *Nachricht, Kunde' =■ ap. azda *Kunde'; np.
miyazd *Gelage' (Parsenwort) = zd. myazda-, Np. mayz
'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
b)tlran. zm (= idg. ^^ g^h + w, auch][dA -f s + w?)
= zd. sm = ap. np. zmi bazm 'Gastmahl', arm. bazmakan
*Gast*, siehe oben p. 29 ; razm *Schlacht, Kampf , arm. razm
und paterazni, phi. razm u patrazm Yatk. i. Zar. 66, zd.
rasman-, Wrzl. reg'^, siehe oben p. 66; hSzum 'Brennholz'
= zd. a^sma-, aus *aidhsmO'?, vgl. gr. ai&w; Gurazm bei
Firdusi (fur *Karazm) = zd. kavarasmo (gen. sg.), Dar-
mesteter, Etud. iran. II, 230.— 224 —
c) Iran. 2;n (= idg. g^, g% + n) ==-- zd. ap. sn, im
```


## [2026-09-07T15:54:19.935Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n '1,40p' /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Check fetch_source tool"
}
```


### [2026-09-07T15:54:19.981Z] TOOL RESULT

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


## [2026-09-07T15:54:26.013Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B2%D8%A8%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%AE\" \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%A6%D8%AF%D8%A9\" \"https://en.wiktionary.org/wiki/mitis\" \"https://www.etymonline.com/word/mitigate\" \"https://www.etymonline.com/word/ammunition\"; do timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 326, roots Mei 1 / Mei 2\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T15:54:31.212Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/33e2a4cffb8a4aae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c714ca1c87e1541.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b251d116a18bf8fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/418d46146444d482.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d848321982a4872.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c562fbf41691aa81.txt
```


## [2026-09-07T15:54:34.634Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 33e2a4cffb8a4aae 3c714ca1c87e1541; do echo \"########## $f\"; grep -n -A25 \"Etymology\" $f.txt | head -60; done",
 "description": "Read wiktionary mizban and mikh"
}
```


### [2026-09-07T15:54:35.901Z] TOOL RESULT

```
########## 33e2a4cffb8a4aae
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Descendants 
72-
73- 1.4 
74- References 
75-
76- 2 
77- Punjabi 
78-
79- Toggle Punjabi subsection 
80-
81- 2.1 
82: Etymology 
83-
84- 2.2 
85- Noun 
86-
87- 3 
88- Urdu 
89-
90- Toggle Urdu subsection 
91-
92- 3.1 
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
98- 3.3 
99- Noun 
100-
101- 3.4 
102- References 
103-
104- Toggle the table of contents 
105-
106- میزبان 
107-
108- 7 languages 
109-
110- বাংলা 
111- فارسی 
112- Bahasa Indonesia 
113- Malagasy 
114- Norsk bokmål 
115- Sängö 
116- سرائیکی 
117-
118- Entry 
--
177: Etymology
178- [ edit ] 
########## 3c714ca1c87e1541
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
75-
76- 2 
77- Persian 
78-
79- Toggle Persian subsection 
80-
81- 2.1 
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.3.1 
91- Related terms 
92-
93- 2.3.2 
94- Descendants 
95-
96- 3 
97- Ushojo 
98-
99- Toggle Ushojo subsection 
100-
101- 3.1 
102: Etymology 
103-
104- 3.2 
105- Noun 
106-
107- Toggle the table of contents 
108-
109- میخ 
110-
111- 9 languages 
112-
113- فارسی 
114- Français 
115- Bahasa Indonesia 
116- Kurdî 
117- Malagasy 
118- Nederlands 
119- Polski 
120- سرائیکی 
121- 中文
```


## [2026-09-07T15:54:39.058Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '170,240p' 33e2a4cffb8a4aae.txt; echo \"########## MIKH\"; sed -n '130,215p' 3c714ca1c87e1541.txt",
 "description": "Read etymology sections"
}
```


### [2026-09-07T15:54:39.116Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: میزبان 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( myzdpʾn' /⁠mēzdbān⁠/ , “ host ” ) . By surface analysis , میز ( miz , “ table ” ) +‎ ـبان ( -bân , “ keeper, guardian ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /meːz.ˈbaːn/ , /miːz.ˈbaːn/ 

 ( Dari, formal ) IPA ( key ) : [meːz.bɑ́ːn] 

 ( Dari, formal ) IPA ( key ) : [meːz.bɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [meːz.bɑ́ːn] 

 ( Hazaragi ) IPA ( key ) : [meːz.bɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [miːz.bɒ́ːn] 

 ( Tajik, formal ) IPA ( key ) : [miz.bɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 mēzbān, mīzbān

 Dari reading ? 

 mēzbān

 Iranian reading ? 

 mizbân

 Tajik reading ? 

 mizbon

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 میزبان • ( mēzbān / mizbân ) ( Tajik spelling мизбон ) 

 host 

 Descendants
 [ edit ] 

 → Bengali: মেজবান ( mezban ) , মেজমান ( mejoman ) , মেজ্বান ( mejjan ) — regional 

 → Hindustani: 
 Hindi: मेज़बान ( mezbān ) , मेजबान ( mejbān ) — nuqtaless 
 Urdu: میزْبان ( mezbān ) 

 → Punjabi: 
 Gurmukhi script: ਮੇਜ਼ਬਾਨ ( mezbān ) , ਮੇਜਬਾਨ ( mejbān ) — nuqtaless 
 Shahmukhi script: میزْبَانْ ( mezbān ) 

 → Pashto: مېزبان ( mēzbān ) 
########## MIKH

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

 See also: مىخ 

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Persian میخ ( mix , “ nail ” ) .

 Noun
 [ edit ] 

 میخ • ( mıh ) 

 nail , a spike -shaped metal fastener used for joining wood or similar materials 
 Synonyms: چیوی ( çivi ) , مسمار ( mismar ) 

 coin die , any of the metal stamps used to strike impressions of designs onto coins 
 Synonym: سكه ( sikke ) 

 Derived terms
 [ edit ] 

 میخ كسمك ( mıh kesmek , “ to make nails ” ) 
 میخ چاقمق ( mıh çakmak , “ to drive in a nail ” ) 
 میخلاتمق ( mıhlatmak , “ to make or let be nailed ” ) 
 میخلامق ( mıhlamak , “ to nail ” ) 
 میخلانمق ( mıhlanmak , “ to be nailed ” ) 
 میخلو ( mıhlı , “ furnished with nails ” ) 

 Descendants
 [ edit ] 

 Turkish: mıh 

 → Armenian: մըխ ( məx ) 

 Further reading
 [ edit ]
```


## [2026-09-07T15:54:43.894Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '215,300p' 3c714ca1c87e1541.txt",
 "description": "Read Persian mikh etymology"
}
```


### [2026-09-07T15:54:43.933Z] TOOL RESULT

```
 Çağbayır, Yaşar ( 2007 ), “ mıh2 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 3195 

 Hindoglu, Artin ( 1838 ), “ میخ ”, in Hazine-i lûgat ou dictionnaire abrégé turc-français ‎ [1] , Vienna: F. Beck, page 472a 

 Kélékian, Diran ( 1911 ), “ میخ ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 1255 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Clavus”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [3] , Vienna, column 190 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ میخ ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [4] , Vienna, columns 5067-5068 

 Nişanyan, Sevan ( 2002– ), “ mıh ”, in Nişanyan Sözlük 

 Redhouse, James W. ( 1890 ), “ میخ ”, in A Turkish and English Lexicon ‎ [5] , Constantinople: A. H. Boyajian, page 2053 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( myh /⁠mēx⁠/ ) , from Old Persian 𐎶𐎹𐎢𐎧 ( MYUX /⁠mayūxa⁠/ ) , from Proto-Indo-Iranian *mayū́kʰas ( “ peg, nail ” ) , ultimately a borrowing from the the BMAC substrate . Cognate with Sanskrit मयूख ( mayūkha , “ peg ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈmeːx/ 

 ( Dari, formal ) IPA ( key ) : [meːx] 

 ( Dari, formal ) IPA ( key ) : [meːx] 
 ( Kabuli ) IPA ( key ) : [meːx] 

 ( Hazaragi ) IPA ( key ) : [meːx] 

 ( Iran, formal ) IPA ( key ) : [miːx] 

 ( Tajik, formal ) IPA ( key ) : [meχ] 

 Rhymes: -eːx 

 Readings

 Classical reading ? 

 mēx

 Dari reading ? 

 mēx

 Iranian reading ? 

 mix

 Tajik reading ? 

 mex

 Audio ( Iran ) : ( file ) 

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 میخ 

 Iranian Persian

 Tajik

 мех 

 میخ • ( mix, mêx ) ( plural میخ‌ها ( mix-hâ, mêx-hâ ) ) 

 nail 

 Related terms
 [ edit ] 

 میخک ( mixak ) 

 میخی ( mixi )
```


## [2026-09-07T15:54:56.586Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"etymology\" -A30 b251d116a18bf8fc.txt | sed -n '1,10p'; echo ====; awk 'NR>100 && NR<330' b251d116a18bf8fc.txt | grep -n -i -B3 -A20 \"borrow\\|Ge.ez\\|Ethiop\\|Aramaic\\|Hebrew\" | head -60",
 "description": "Read wiktionary maida"
}
```


### [2026-09-07T15:54:57.938Z] TOOL RESULT

```
Exit code 1
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
(eval):1: === not found
```


## [2026-09-07T15:55:00.852Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '100,220p' b251d116a18bf8fc.txt",
 "description": "Read maida page body"
}
```


### [2026-09-07T15:55:00.909Z] TOOL RESULT

```
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

 Arabic
 [ edit ] 

 مَائِدَة 

 Etymology
 [ edit ] 

 Borrowed from Ge'ez ማእድ ( maʾədd , “ table ” ) , which is of unknown origin.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /maː.ʔi.da/ 

 Noun
 [ edit ] 

 مَائِدَة • ( māʔida )  f ( plural مَائِدَات ( māʔidāt ) or مَوَائِد ( mawāʔid ) ) 

 dining table 
 609–632 CE , Qur'an , 5:112-114 : 

 ( metonymic ) The food itself
 مَائِدَة العَشَاء ― māʔida al-ʕašāʔ ― dinner 

 Declension
 [ edit ] 

 Declension of noun مَائِدَة ( māʔida )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 مَائِدَة 
 māʔida 

 الْمَائِدَة 
 al-māʔida 

 مَائِدَة 
 māʔidat 

 nominative

 مَائِدَةٌ 
 māʔidatun 

 الْمَائِدَةُ 
 al-māʔidatu 

 مَائِدَةُ 
 māʔidatu 

 accusative

 مَائِدَةً 
 māʔidatan 

 الْمَائِدَةَ 
 al-māʔidata 

 مَائِدَةَ
```


## [2026-09-07T15:55:06.457Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### mitis\"; grep -n -A12 \"^ Etymology$\" 418d46146444d482.txt | sed -n '1,40p'; echo \"### mitigate\"; grep -n -i \"mitigate\" 0d848321982a4872.txt | head -5",
 "description": "Read mitis and mitigate"
}
```


### [2026-09-07T15:55:07.847Z] TOOL RESULT

```
### mitis
191: Etymology
192- [ edit ] 
193-
194- Perhaps from Latin mitis ( “ mild ” ) .
195-
196- Pronunciation
197- [ edit ] 
198-
199- This entry needs pronunciation information. If you are familiar with the IPA or enPR then please add some!
200-
201- Noun
202- [ edit ] 
203-
--
223: Etymology
224- [ edit ] 
225-
226- Of unclear origin, with multiple competing theories.
227-
228- The prevailing etymology connects Old Irish méth ( “ plump, fat ” ) , Welsh mwyd ( “ act of soaking ” ) , Welsh mwydion ( “ soft parts ” ) (from Proto-Celtic *meitos ( “ soft, plump ” ) ); Old Irish mín ( “ soft; gentle, smooth; mild, tender, calm ” ) ( Proto-Celtic *mīnis ); and Old Irish moíth ( “ soft, tender ” ) ( Proto-Celtic *moitos ), together from Proto-Indo-European *meyh₁- ( “ mild, soft ” ) . Other potential Indo-European cognates also point to a meaning like “pleasant”: Sanskrit मयस् ( máyas , “ pleasure, enjoyment, refreshment ” ) , Avestan 𐬨𐬀𐬌𐬌𐬀𐬵 ( maiiah , “ pleasure ” ) , Proto-Slavic *mìlъ ( “ soft, mild, gentle, agreeable, pleasant, sweet, dear ” ) , Lithuanian mielas ( “ nice, sweet, cute ” ) , Latvian mīls ( “ dear, cherished, beloved ” ) , Old Prussian mijls ( “ dear ” ) , [ 1 ] [ 2 ] Albanian mirë ( “ good, well ” ) . De Vaan suggests that the root *meyh₁- is actually *meh₁i- , being originally an extension of *meh₁- ( “ to measure ” ) . [ 3 ] 
229-
230- Alternatively, Oettinger compares Hittite 𒈠𒀀𒄿𒀭𒍣 ( ma-a-i-an-zi , “ to grow (up); to prosper ” ) , reconstructing Proto-Indo-European *meyH- ( “ to ripen ” ) ; Kloekhorst rejects this on both semantic and formal grounds. [ 4 ] 
231-
232- Plötz suggests it to be a zero-grade extension of the prohibitive particle *meh₁i , specifically labeling it a derivative from *mh₁i-tis . [ 5 ] 
233-
234- Pronunciation
235- [ edit ] 
### mitigate
1:URL: https://www.etymonline.com/word/mitigate
4:TITLE: Mitigate - Etymology, Origin & Meaning
6:Mitigate - Etymology, Origin & Meaning 
21: Origin and history of mitigate 
23: mitigate (v.)
```


## [2026-09-07T15:55:15.599Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '20,45p' 0d848321982a4872.txt; echo \"#### AMMUNITION\"; sed -n '20,45p' c562fbf41691aa81.txt",
 "description": "Read etymonline entries"
}
```


### [2026-09-07T15:55:15.649Z] TOOL RESULT

```
 Origin and history of mitigate 

 mitigate (v.) 

 early 15c., "relieve (pain); make mild or more tolerable; reduce in amount or degree," from Latin mitigatus , past participle of mitigare "soften, make tender, ripen, mellow, tame," figuratively, "make mild or gentle, pacify, soothe," ultimately from mitis "gentle, soft" + root of agere "to do, perform" (from PIE root *ag- "to drive, draw out or forth, move"). For mitis de Vaan suggests cognates in Sanskrit mayas- "refreshment, enjoyment," Lithuanian mielas "nice, sweet, dear," Welsh mwydion "soft parts," Old Irish min "soft," from a PIE *mehiti- "soft." Related: Mitigated ; mitigating ; mitigates .
 also from early 15c. 

 Entries linking to mitigate 

 mitigating (adj.) 

 "extenuating," 1610s, present-participle adjective from mitigate .

 immitigable (adj.) 

 1570s, from Latin immitigabilis , from assimilated form of in- "not" (see in- (1)) + mitigabilis , from past-participle stem of mitigare "make mild or gentle" (see mitigate ). Related: Immitigably .

 mitigable 
 mitigant 
 mitigation 
 unmitigated 
 *ag- 
 See All Related Words (7) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
#### AMMUNITION
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light
```


## [2026-09-07T15:55:18.746Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A6 \"ammunition (n.)\" c562fbf41691aa81.txt | head -20",
 "description": "Find ammunition entry text"
}
```


### [2026-09-07T15:55:18.797Z] TOOL RESULT

```
56: ammunition (n.) 
57-
58- 1620s, "military stores and provisions," from French soldiers' faulty separation of French la munition , as if *l'amunition ; from Latin munitionem (nominative munitio ) "a fortifying" (see munition ).
59-
60- The mistake in the word perhaps was by influence of French a(d)monition "warning." The error was corrected in French (Modern French munition ), but retained in English, with the unetymological double -m- spelling to conform to words in Latin. At first it meant all military supplies in general; in modern use it means only material used in the discharge of firearms and ordnance.
61- also from 1620s 
62-
```


## [2026-09-07T15:55:30.253Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 mei- mitis ===\"; grep -n \"mitis\\|moenia\\|mūnīre\\|munire\\|mayūkha\\|mayukha\\|miyedha\\|myazda\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-07T15:55:30.310Z] TOOL RESULT

```
=== WLD Bd2 mei- mitis ===
15702:      moenia „Umwallung, Stadtmauern^ („*Umpfahlung“), mUnio (mocnio),
15788:270 f. Yerb. mit moenia),
15981:m. „Opferspeise“, av. myazda- m. „Opfermal'‘ (unmittelbar von der Wz.
17241:drobend'* (s. Vf. LE\Yb - s. v. minae moenia wiirde nur der Bed. ,,Zinnen‘'
42198:nahme semitischen Ursprungs wendet sich Giintert Ub. ar. Reimwortbil-
```


## [2026-09-07T15:55:31.873Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB mezd ===\"; grep -n -i \"mezd\\|myazd\\|mex\\b\" NYB_vol2_glossary.txt | head -15; echo \"=== IEC ===\"; grep -n \"mitis\\|mūnio\\|munio\\|mayukha\" IEC.txt | head -15",
 "description": "Grep Nyberg and Mann"
}
```


### [2026-09-07T15:55:31.947Z] TOOL RESULT

```
=== NYB mezd ===
2545:mex [myh], "meči [*myd] pole 2026, 421° (*myd). — NP mēx; connection with OP mayüza- ‘doorknob’ (Kent), Skr mayū- kha- probable. The spelling was a crux in BP, as myh wholly coincides with MY? = dp. The spelling in 421° is con- firmed, e.g., by DkM 6279, and by *Mei-var (g.v.). At first sight it would seem to be a desperate attempt to get rid of the ambiguity by mutilating the last letter (I transliterated it in the Index *myh) — true, only to fall into Charybdis, for now the spelling coincided
2551:(Sitz.ber. d. Kön. bay. Ak. d. Wiss. 1890, 2. Bd, 43-84). Hübschmann read the three ws. myhk' [ZY] *plzyn 221 in one: mšk*plzyn, and identified it (AG 192) with Arm maškapačen (P‘aust. Buz. p.78; there in pl.), also maškavarzan (ibd. p. 240), or maš(k)aperčan (Sebčos, not accessible to me), translating them 'the tent of the Great King'. However, these ws., which are manifestly identical but re- present a foreign term imperfactly re- produced, signify ‘accounts’ (mask 'lea- ther’ being the material used for such documents); Nor Bargirk* explains it by the terms hisäb, daftardär, daftarxäneh, and the passages quoted above refer to the regimental treasurer or treasury forming part of the field army. The w. mask (of Ass. origin) never signifies ‘tent’, only ‘skin, leather’. The semantic con- nection between méxak ‘headquarter’ and mex ‘pole’ is obvious.
2554:name Qais born by the kings of Kinda, v. Nyberg, Unvala Vol. 111-112. — For mēx-var, v.g. v. mex.
2802:dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hurmuzd, Ormuz(d).
6641:Hörmezd: Ohurmazd
=== IEC ===
2737:dheguho (dhoguh-) ‘burn, fire’. Cf. dhe- guhlos, dheguhro-, dheguhto- and guheguh-. WP I, 849 Skt. dahàmi; Av. daZai-; Tokh. A tsak-; AB tsák- (also ‘bite, sting"); Alb. djeg, aor. dogja (fr. *dheguhiou, cf. Li. degiaü) beside n-dez (*kindle', fr. *dhoguheio, a factitive); MIr. dóim, Ir. dóighim and dóghaim (cf. OLi. degmi); Br. devi, pp. devet; Cor. dywy; W cf. cyn-neu ‘kindle’; cyn-ne ‘burning’ beside OW deifaw 'roast; Li. degü, OLi. degmi, inf. dégti; Latv. degu, dedzu, inf. degt. Lat. foveo, tr ‘warm’; fomes, -mitis (for the second element "wood cf. termes, trà-mes) seems to represent o-gde factitive
6245:-is, adjectival formant denoting (1) colour; (2) animate content (1) Skt. harih ‘yellow’; Av. zairis, id.; Hitt. har- kis (^white', as against Gk. argós “bright”, where i-type adjj. are rare); Lat. viridis; OHG gruoni; OE erëne ‘green’ (2) Skt. šučih ‘pure’; Hitt. mekkis ‘big’: Lat. fortis, acris, rudis, mitis, tristis, lenis, sterilis, facilis, etc.; Go. hrains, sels, süts, brüks, anda- sets “pure, kind, sweet, useful, revolting’; OCS vísi "all, Zen “female? (other forms in -ï are adverbial, cf. svobodi, is-plünf, razlict, sugubi, roct, all undeclined. Cf. OCz. je mi len, im- pers. ‘I am (too) lazy . . ^: Lat. lēnis); Li. pats ‘the same’. Sole example of i-st. in Li. Absent fr. Latv. Gk. eünis “bereft'; ídris “skilled”
10499:meit- (1) (moit-) ‘soft, gentle’. (Lat. ambig. but prob. moit-, q.v.). WP II, 238 & 247 Illyrian (in names) cf. Teut-meitis, m., Mei- time, f.; Lat. mitis (gentle, soft, overripe'. Cf. moit-); Br. mwéz, mwés (*moist'. Phonol. ambig. but prob. > Fr. moite *moist); W mwyd, m. ‘steeping’; mwydo, inf. ‘steep’; Ir. cf. méath, méith ‘fat; OIr. also méithe, f. “fat- ness’
10849:mitos, is, us (radical: mit-) (3) “substance. Cf. WP II, 247 Oss. mit, met ‘snow’; Gk. mítus, f. 'bee-glue' beside misu, n. ‘copper sulphate; truffles’; Lat. cf. mes -mitis in pal-mes ((vine-shoot', cf. palpare); ter-mes (folive-branch; wood. worm’, cf. terere); fo-mes (Cfirewood', cf. fo- vëre); Ili-mes (boundary-mark; cross-path', cf. linere); and trà-mes ‘forest path, firebreak'; (in limes there is influence of limis, adj. *askew^); Li. mitas ‘food, board" beside mita- las *food, fodder (For Latv. mitu, mist, v. ‘live’, see mitos (1))
11050:moitos, is (2) “soft, tender, mild, tame'. Cf. meit-. Cf. WP II, 244 and (4) Lat. mitis (^mellow, mild, calm, soft, kind’. Vowel ambig. cf. meit-); MIr. maóith, Mir. & mod. maoth “soft, tender, feeble, sickly’; MHG cf. meidem, meiden, sm. ‘gelding’; mei- denen, v. ‘castrate’; ON meiða, v. ‘spoil, dam- age, maim’; Li. maità, Latv. maita ‘carrion’; Finn. LW miete “weak”
```


## [2026-09-07T15:55:46.776Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (15702,15981):\n    # find nearest preceding page tag\n    for i in range(ln-1,max(0,ln-400),-1):\n        if '[pdf page' in t[i]:\n            print('line',ln,'-> tag at',i+1,t[i].strip()); break\n    print('   >>', '\\n   >> '.join(x.strip() for x in t[ln-4:ln+4]))\nEOF",
 "description": "Get WLD page context"
}
```


### [2026-09-07T15:55:48.213Z] TOOL RESULT

```
   >> 
   >> maide „Stange“    mdidit ^bestecken, bepfahlen"' (mit -d(hy wie ir. mMe)^
   >> maili „Zauiistecken‘'; mir. mlde „Nacken‘‘ {^mei-d-io-^ Pick II ^ 205);
   >> moenia „Umwallung, Stadtmauern^ („*Umpfahlung“), mUnio (mocnio),
   >> lat.
   >> 
   >> „aufdammen (einenWeg; ursprgl, vom Priigelweg), aufmauern, ver-
   >> -‘Ire
   >> setzt Hirt  Abl. 100 *meiW‘, Reichelt KZ. 39, 10 «ig«- (: me- s. u.) an
   >> (letzteres fiir ai. mdyas, das wobl nicbt *ni9ios ist, schwierig).
   >> Ai. mdyas n. „Labsal, Preude, Lust“, dazu *m{i)ies dh{e)- in ai. niiyedha-
   >> m. „Opferspeise“, av. myazda- m. „Opfermal'‘ (unmittelbar von der Wz.
   >> als niei-dho- wobl ai. medha- m. „Fettbruhe, kraftiger Trank“, medJias- n.
   >> „Opfer“, 8. auch zu mad- „na6“, Wiedemann BB. 28, 42         iiber ai. mitrd-          ;
   >> 
   >>
```


## [2026-09-07T15:55:54.181Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 incoming/WLD/WLD_Bd2_pages.txt; grep -c $'\\f' incoming/WLD/WLD_Bd2_pages.txt; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\n# find leaf index containing our lines\nlines=t.split('\\n')\nfor target in (15702,15981):\n    txt='\\n'.join(lines[:target])\n    print(target,'leaf(0-based)',txt.count('\\f'))\nEOF",
 "description": "Find WLD leaf numbers"
}
```


### [2026-09-07T15:55:55.642Z] TOOL RESULT

```
                ALOIS WALDE


VERGLEICHENDES WORTERBDCH
                            DER
720
15702 leaf(0-based) 244
15981 leaf(0-based) 248
```


## [2026-09-07T15:56:04.999Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (243,244,247,248):\n    L=leaves[i]\n    nums=re.findall(r'\\b(2[34]\\d)\\b', L[:200]+L[-200:])\n    print('leaf',i,'nums',nums, '|', L[:120].replace('\\n',' / '))\nEOF",
 "description": "Check WLD printed page numbers"
}
```


### [2026-09-07T15:56:06.411Z] TOOL RESULT

```
leaf 243 nums ['239', '237'] |                                          mei-                                   239 /  / xvaioy neben y.vr]v, s. Bechtel Lex
leaf 244 nums ['240'] | 240                                           mei- /  /  /  / maide „Stange“    mdidit ^bestecken, bepfahlen"' (mit -d(hy wie ir
leaf 247 nums [] |                                                                                                                      ; /  / 
leaf 248 nums ['244'] | 244                                            mei           meit /  / 8. inei-,    ml        weich, sanft, geliiide; erquic
```


## [2026-09-07T15:56:16.025Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[248][:1200])\nEOF",
 "description": "Print WLD p.244 opening"
}
```


## [2026-09-07T15:56:17.014Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN mitigate\"; grep -n \"mitigate\\b\" KLN_1966.txt | head -5; echo \"### KLN ammunition\"; grep -n \"ammunition\" KLN_1966.txt | head -5; echo \"### SKT\"; grep -n \"mitigate\\|ammunition\" SKT.txt | head -5",
 "description": "Grep Klein and Skeat"
}
```


### [2026-09-07T15:56:17.437Z] TOOL RESULT

```
244                                            mei           meit

8. inei-,    ml        weich, sanft, geliiide; erquicklich, liebreich“; als Basis
      setzt Hirt  Abl. 100 *meiW‘, Reichelt KZ. 39, 10 «ig«- (: me- s. u.) an
      (letzteres fiir ai. mdyas, das wobl nicbt *ni9ios ist, schwierig).
   Ai. mdyas n. „Labsal, Preude, Lust“, dazu *m{i)ies dh{e)- in ai. niiyedha-
m. „Opferspeise“, av. myazda- m. „Opfermal'‘ (unmittelbar von der Wz.
als niei-dho- wobl ai. medha- m. „Fettbruhe, kraftiger Trank“, medJias- n.
„Opfer“, 8. auch zu mad- „na6“, Wiedemann BB. 28, 42         iiber ai. mitrd-          ;


„Preund“ s. u. mei ^„binden“).
   Mit ^-Pormantien lat. ntUis „mild, gelind“; air. moith, moeth „tener“,
CO moithaigidir „emolliat“ (Stokes KSB. 5, 114), cymr. mivydo „erweichen,
mwydion „Weichteile“ (wenn die ir. Worte aus dem Brit, entlehnt sind,
ware im Kelt, nur die Ablautshife           nicbt auch *mvit- vh. Pedersen                            ;


KGr. I 184),           lett.          Johansson IP. 2, 41, Zupitza BB. 25.
                               atme'et .;erweichen“     ;


99 (wo Abgrenzung gegen andere Wzln. der Porm meit).
  Mit H-, 1-, r-Pormantien: air. mJn „sanft
```


### [2026-09-07T15:56:17.500Z] TOOL RESULT

```
### KLN mitigate
1925:agent,  adj.  —  L.  agens,  gen.  agentis,  pres.  part, of  agere,  ‘to  set  in  motion,  drive,  lead,  conduct, guide,  govern ;  to  do,  act’,  whence  agmen,  ‘army, troop,  band,  multitude’,  lit.  that  which  is  lead’, fr.  I.-E.  base  *ag-,  ‘to  drive,  lead,  act,  do’,  whence also  Gk.  dyeiv,  ‘to  lead,  guide,  drive,  carry off’,  dytveiv,  ‘to  lead,  bring’,  aycov,  ‘assembly, contest  in  the  games’,  xycovtx,  ‘struggle  for  vic¬ tory,  anguish,  agony’,  Aycoyd?,  ‘leader’,  aywyfj, ‘a  carrying  away,  a  leading’,  OI.  ajati,  ‘drives’, ajirah,  ‘moving,  active’,  Avestic  aza'ti,  ‘drives’, Toch.  A  dk-,  B  &k-,  ‘to  travel,  lead’,  Arm.  acem, ‘1  lead,  bring",  ON.  aka,  ‘to  drive’.  Cp.  agent, n.  Cp.  also  abigeat,  acorn,  acre,  act,  action,  acti¬ vate,  actor,  actress,  actuate,  Agelaius,  agenda, agile,  agitate,  agminate,  -agogue,  agonist,  ago¬ nize,  agony,  agrarian,  agrestic,  agriculture,  agrio-, agro-,  agronomy,  Agrostis,  Agyieus,  aisle,  ala, ambages,  ambagious,  ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘acting  force’,  fr. ML.  agens,  in  the  sense  of  ‘acting  person’,  fr. It.  agente;  both  these  words  derive  fr.  L.  agens, gen.  agentis,  pres.  part,  of  agere.  See  agent,  adj. agential,  adj.  —  Formed  fr.  agency  with  suff. -ial.
3717:See  prec.  word  and  verbal  suff.  -ate. assort,  tr.  and  intr.  v.  —  OF.  assorter,  ‘to  assort, match’,  fr.  a,  ‘to’  (see  a),  and  sorte,  ‘sort,  kind, species’.  See  sort,  v.  and  n.  The  change  of  con¬ jugation  in  F.  assortir,  of  s.m.,  is  due  to  the  in¬ fluence  of  the  verb  sortir,  ‘to  go  out’. Derivatives:  assort-ative,  adj.,  assort-ed,  adj., assort-er,  n.,  assort-ive,  adj.,  assort-ment,  n. assuage,  tr.  v.,  to  mitigate;  to  soothe.  —  ME. asuagen,  fr.  OF.  asuager,  assouager,  assouagier, fr.  a,  ‘to’  (see  a),  and  L.  suavis,  ‘sweet’.  See sweet  and  cp.  suave.
18808:immitigable,  adj.  —  Late  L.  immitigabilis,  ‘not mitigable’,  fr.  in-,  ‘not’,  and  L.  mitigare,  ‘to make  soft,  mitigate’.  See  mitigate  and  -able, immobile,  adj.  —  F.,  fr.  L.  immobilis,  ‘immov¬ able’,  fr.  in-,  ‘not’,  and  mobilis,  ‘movable’.  See mobile.
21464:part,  of  lenire,  ‘to  soften,  alleviate,  mitigate, allay,  soothe,  calm’,  fr.  lenis,  ‘soft,  smooth, mild,  gentle,  calm’,  which  prob.  derives  fr.  I.-E. base  *le(i)-,  ‘to  leave  behind,  leave,  yield’, whence  also  Lith.  lenas,  ‘quiet,  tranquil;  tame; slow’,  Lett.  Iqns,  ‘slow,  lazy’,  OSlav.  lenu,  ‘lazy’. Fr.base  *le(i)d-,  a  -^-enlargement  of  base  *le(i)-, derive  L.  lassus  (for  *lad-to-s),  ‘faint,  weary, languid’,  OE.  Iset,  ‘sluggish,  slow’,  IStan,  ‘to leave  behind’. See  let,  ‘to  leave’,  and  cp.  lassitude, late.  For  the  ending  see  suff.  -ent.
21465:Derivative :  lenient-ly,  adv. lenify,  tr.  v.,  to  soften,  mitigate.  —  Compounded of  L.  lenis  (see  lenient)  and  suff.  -fy. lenitive,  adj.,  softening,  mitigating.  —  ML.  leni- tivus,  fr.  L.  lenitus,  pp.  of  lenire,  ‘to  soften’.  See lenient  and  -ive.
### KLN ammunition
2494:ammotherapy,  n.,  treatment  by  means  of  sand baths.  —  Compounded  of  ammo-  and  -therapy, ammunition,  n.  —  F.  amunition,  a  dialectal  form for  munition  (see  munition).  Amunition  arose through  a  misdivision  of  la  munition  ivAoTamu- nition.
3518:arsenal,  n.,  a  place  for  manufacturing  and  storing ammunition  and  weapons.  —  It.  arsenale  (Olt. arzanale),  ‘dock’,  borrowed — prob.  through  the medium  of  MGk.  d.pm]'tdkt)C, — fr.  Arab,  dar- a?-sind'ah  (whence  also  Sp.  darsena  and  It.  dar- sena,  ‘dock’),  lit.  ‘house  of  construction’,  fr.  ddr, ‘house’,  as-,  assimilated  form  of  al-,  ‘the’,  and Sind'ah,  ‘construction,  art’,  fr.  Sana' a,  ‘he  made’. For  the  ending  of  arsenal  see  adj.  suff.  -al. arsenic,  n.,  a  chemical  element.  —  OF.  (=  F.) arsenic,  fr.  L.  arsenicum,  arrhenicum,  fr.  Gk. dptrsvixov,  appevvxov,  ‘yellow  orpiment',  fr. MPers.  *zarnik,  ‘gold,  golden ;  orpiment’(whence ModPers.-Arab.  zarnikh,  ‘orpiment’),  through the  medium  of  a  Semitic  language;  cp.  Mish- naic  Heb.  zarnikh,  Syr.  zarnikhd,  ‘orpiment’. Cp.  Avestic  zaranya,  Pers.  zar,  ‘gold’,  and  the first  element  in  zermahbub,  and  see  yellow  and words  there  referred  to.  Cp.  also  jargon,  ‘a variety  of  zircon’.  Gk.  apctevtxov,  appsvtx&v, ‘orpiment’,  was  influenced  in  form  by  apcrevtxop, appevixic,  ‘male’,  fr.  ape rc;v,  ap pr,v,  ‘male’.  For the  sense  development  of  MPers.  *zarnik,  cp.  L. auripigmentum,  fr.  aurum,  ‘gold’  (see  orpiment). Derivatives:  arsenic,  arsenic-al,  adjs. arsenious,  adj.,  containing  arsenic.  —  See  ar¬ senic  and  -oils.
### SKT
12032:ammunition,  store  for  defence.  {F.^ L.)  From  O.  F.  amuniticn,  a  soIiUers' comiptioD,  due  to  putting  J'amuni/ion  for
```


## [2026-09-07T15:56:24.996Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN mitigate entry\"; grep -n \"mitigate,  tr\\|mitigate, tr\\|munition,  n\\|munition, n\" KLN_1966.txt | head; echo \"### KLN mitis\"; grep -n \"L.  mitis\\|mitis,\" KLN_1966.txt | head -5",
 "description": "Grep Klein entries"
}
```


### [2026-09-07T15:56:25.071Z] TOOL RESULT

```
### KLN mitigate entry
2494:ammotherapy,  n.,  treatment  by  means  of  sand baths.  —  Compounded  of  ammo-  and  -therapy, ammunition,  n.  —  F.  amunition,  a  dialectal  form for  munition  (see  munition).  Amunition  arose through  a  misdivision  of  la  munition  ivAoTamu- nition.
24059:Mithras,  n.,  the  Persian  god  of  light.  —  L.,  fr. Gk.  M 10-pa?,  fr.  Avestic  Mipra-,  which  is  rel. to  OI.  Mitrah.  See  Mitra  and  cp.  next  word, mithridate,  n.,  an  antidote  against  poison.  — ML.  mithriddtum,  fr.  Late  L.  mithridatium, prop.  neut.  of  Mithridatius,  ‘pertaining  to  Mith- ridates’,  fr.  L.  Xfithridates,  fr.  Gk.  MifiptSarv)?; so  called  in  allusion  to  Mithridates,  King  of Pontus,  who  made  himself  poison-proof. Derivatives :  mithridat-ism,  n.,  mithridat-ize,  tr.  v. mitigate,  tr.  v.,  to  alleviate.  —  ME.  mitigaten,  fr. L.  mitigatus,  pp.  of  mitigare,  ‘to  make  soft  or tender,  to  soothe,  mitigate’,  compounded  of mit  is,  ‘soft,  mild,  gentle’,  and  agere,  ‘to  set  in motion,  drive,  lead;  to  do,  act’.  The  first  ele¬ ment  prob.  stands  for  *mi-tis  and  derives  fr, I.-E.  base  *mei-,  *mi-,  ‘soft, mild,  tender,  gentle; peaceful,  lovely',  whence  also  OIr.  moith,  Mir. moeth,  Ir.  maoth,  ‘soft’.  Cp.  also — with  -/-forma¬ tive  element — OSlav.  milu,  ‘charitable’,  Russ. milyj,  Pol.  mily,  Czech  and  Slovak  mily,  Lith. mielas,  mylas,  ‘beloved,  dear’,  Lith.  myliu, myleti,  ‘to  love’,  Lett,  mil's,  OPruss.  mijls,  ‘be¬ loved,  dear’,  Russ,  milovat’,  ‘to  show  mercy’, Pol.  milovac,  Czech  milovati,  Slovak  milovat', etc.,  ‘to  love’,  Russ,  mllost',  ‘mercy’,  Czech milost,  Slovak  milost',  ‘love,  mercy’.  Cp. — with  -r-formalive  element — Alb.  mire,  ‘good’, OSlav.  miru,  Pol.  mir,  Czech  mir,  Slovak  mier, ‘peace’,  Russ,  mir,  ‘peace,  world,  community’; with  -/(-formative  element :  Ir.  min,  ‘soft,  smooth, fine’,  W.  main,  ‘slender,  slim’,  mwyn,  ‘soft, kind’,  OCo.  muin,  moin,  ‘soft,  tender’.  OI. mayah,  ‘enjoyment,  pleasure’,  and  Toch.  B maiwe,  ‘little,  subtle',  prob.  also  derive  fr.  I.-E. base  *mei-,  *mi-.  Cp.  mir  and  the  second  ele¬ ment  in  Casimir.  For  the  second  element  in  L. mitigare  see  agent,  adj.,  and  cp.  words  there referred  to.
24676:munition,  n.,  1)  pi.,  military  stores,  provisions;  2) military  material  stored.  —  MF.  (=  F.)  muni¬ tion,  fr.  L.  munitidnem,  acc.  of  miinitid,  ‘fortifi¬ cation,  defense’,  fr.  munitus,  pp.  of  munire.  See muniment  and  -ion  and  cp.  premunition. Derivatives:  munition,  tr.  v.,  munition-eer ,  n., munition-er,  n.
30101:premunition,  n.,  1)  premonition  (archaic);  2) protection  beforehand  (archaic);  3)  immunity to  a  disease  due  to  a  persistent  latent  infection (med.)  —  L.  praemunitid,  gen.  -onis,  ‘a  fortifying beforehand’,  fr.  praemunitus,  pp.  of  praemunire, ‘to  fortify  beforehand’,  fr.  prae  (see  pre-)  and munire,  ‘to  fortify,  protect’.  See  munition  and cp.  praemunire.
### KLN mitis
9439:countless,  adj.  —  Formed  fr.  count,  ‘number’, with  suff.  -less;  first  used  by  Shakespeare, countrified,  adj.  —  Pp.  of  obsol.  countrify,  ar¬ bitrarily  formed  fr.  country  and  suff.  -fy. country,  n.  —  ME.  contree,  fr.  OF.  cuntree,  con- tree  (F.  contree),  fr.  Late  L.  contrata,  ‘land  lying opposite’,  fr.  L.  contra,  ‘against,  opposite’.  See contra-  and  cp.  words  there  referred  to.  Cp.  also It.,  OProveng.  Catal.,  Sp.  and  Port,  contrada, which  also  derive  fr.  Late  L.  contrata. county,  n.  —  OF.  cunte,  conte,  contee  (F.  comte), fr.  L.  comitatus,  "escort,  retinue’,  lit.  ‘a  com¬ pany’,  fr.  comitatus,  pp.  of  comitari,  ‘to  accom¬ pany’,  fr.  comes,  gen.  comitis,  ‘companion’.  See count,  ‘title  of  nobility',  and  cp.  contadino  and posse  comitatus.
13331:Derivative:  ependym-al,  adj. ependymitis,  n.,  inflammation  of  the  ependyma (med.)  —  Medical  L.,  formed  fr.  prec.  word with  suff.  -itis.
13379:epididymitis,  n.,  inflammation  of  the  epididymis (mcd.)  Medical  L.,  formed  fr.  epididymis  with suff.  -itis.
21765:chol.)  —  L.  Ilmen,  gen.  liminis,  ‘threshold’,  prob. rel.  to  limes,  gen.  limitis,  ‘boundary,  limit’.  See limit  and  -men  and  cp.  lintel,  eliminate,  prelimi¬ nary,  postliminy,  sublime,  subliminal.
21773:Derivative:  limitar-ian,  n.,  one  who  limits, limitation,  n.  —  ME.  limitacioun,  fr.  L.  limit atio, gen.  -dnis,  ‘a  fixing’,  fr.  limitatus,  pp.  of  limitare. See  limit,  v.  and  n.,  and  -ation. limitative,  adj.  —  F.  limitatif  (fern,  limitative),  fr. ML.  limitativus,  ‘limiting’,  fr.  L.  limitatus,  pp. of  limitare.  See  limit,  v.  and  n.,  and  -ive. limitless,  adj.  —  Formed  fr.  limit,  n.,  and  suff. -less;  first  used  by  the  English  poet,  statesman and  soldier  Sir  Philip  Sidney  (1554-86)  in  1581. Derivatives:  limitless-ly,  adv.,  limitless-ness,  n. limitrophe,  adj.,  bordering,  adjacent.  —  F.  limi¬ trophe,  fr.  Late  L.  limitrophus,  ‘set  apart  for  the support  of  troups’,  a  hybrid  coined  fr.  L.  limes, gen.  limitis,  ‘boundary,  limit’,  and  Gk.  rpotpoq, ‘feeder’,  fr.  xpetpeiv,  ‘to  feed,  nourish’.  See  limit, n.,  and  tropbic.Late  L.  limitrophus  is  shortened fr.  *limitotrophus  (see  haplology).
```


## [2026-09-07T15:56:27.527Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PLA maida\"; grep -n \"مائدة\\|Māʾida\\|maida\" incoming/PLA/PLA_pages.txt | head; echo \"### AFA fraenkel\"; grep -n \"mā'ida\\|maida\\|ma'ida\\|Tisch\" AFA.txt | head -10; echo \"### LKT\"; grep -n -i \"maida\\|mā'ida\" LKT.txt | head -5; echo \"### SOD myyk\"; grep -n -i \"myyk\\|nail\\|میخ\" SOD.txt | head -8",
 "description": "Grep Semitic and Sogdian refs"
}
```


### [2026-09-07T15:56:27.614Z] TOOL RESULT

```
### PLA maida
### AFA fraenkel
3270:Tisch aus dem Aramäischen.
3289:ges Be]qi 133, 15; Tgl. auch Belcri 472, 8) »ein Tisch
3304:SiXSLt aus äthiop. mä«d »Tisch** (Dillmann 197). MitiCLL
3309:Das »Tischtuch*' Jujüf (ursprünglich wohl mandtl ge-
3317:früher habe ein grooaer Tisch KniPi) and ein kleiner KTPini) (beachte die Femi-
8913:Einen deutlich aramäischen Namen fdhrt der Tischler
8928:zu Tergleichen]. Von den Instrumenten des Tischlers ist
### LKT
3165:'Platz',  Ik.  ebenso  mejdan ;  hieraus  rum. maidan,  meidan  'dass.,  freie  Zeit,  Ge- legenheit'; bulg.  megdan,  serb.  mejdan, poln.klruss.  wiajf/aw,  russ.  maidan  'Platz', Vb.  maidanit'  'gaunern'.  —  [Sp.  alameda 'Platz,  Promenade'  gehört  nicht  hierher, DE  370;  vielmehr  <  ulamo  'Pappel']. [Löbel  EITAP  60.  Gorjajew  XXXIX. Mikl  SlEtVvb  186.  _
8719:mn!  64 macar  1456 macara  1371 mar-«!'  1370 madem  1341 magaza  1362 magazin  1362 mahal  806 mahala(giü)  1350 mahmicr(ie)  1359 waza  1367 maidan  1364 maimu^ä  1365 malotea  1380 mamelegiü  1487 mmneluc  1384 manä  1398 mandanea  1390 mangal  1392 marabut  1410 marafet  1418
### SOD myyk
26244:long-nailed 
45294:5615  myyk    B 
45296:spike,  nail 
46233:nail 
77206:nail,  needle 
77232:nailed 
79160:(/£?)nail,  (/o)strike,  (ro)knock  in 
79182:set  up,  nailed
```


## [2026-09-07T15:56:37.950Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AFA ctx\"; sed -n '3295,3315p' AFA.txt; echo \"### SOD ctx\"; sed -n '45288,45300p' SOD.txt",
 "description": "Read Fraenkel and Gharib contexts"
}
```


### [2026-09-07T15:56:38.009Z] TOOL RESULT

```
### AFA ctx
Nöldeke MaruL Gramm p. 114. Es scheint da nirgends eine
Ableitung zu haben. Das aspirierte aratnsiische Jl ^^ ist
im Arabischen genau durch väi wiedergegeben, wahrend
umgekehrt unaspiriertes H ^ im Arabischen c^ bleibt; Tgl.
JSjucS »Schüssel" gilt schon manchen Arabern (Mn^arr.
124) als fremd. Das ist in der That nicht unwahr-
sclieinlich ; aber pers. gjJS' ist erst Entlehnung aus dem
Arabischen. Aus dem Persischen stammt bekanntlich ^L^ 9
und eine rein zufällige Entlehnung durch Mohammed ist
SiXSLt aus äthiop. mä«d »Tisch** (Dillmann 197). MitiCLL
ist es auch nicht ganz klar, ob es wirklich, wie Gauharl
meint, nur Metapher für die Speise ist, die der Reuende
(Wurzel ^LJ) mit sich nimmt , oder nicht lieber persischen
Ursprungs ist.
Das »Tischtuch*' Jujüf (ursprünglich wohl mandtl ge-
sprochen) in einem Ausspruche Muhammeds Ibn Dor. JTä-
al'ütUf. 223, 8; Agani XVIU. 164, 7; Betai 193, 6;
1) Die wnteren bei JikAt L L angegebenen Bedentunginiimneen J ^ : > U nnd
Juu^u nnd mlleieht nur mi»reretandliebe Anflanangen der LexicognplMB •
die bei einem Fremdworte nicht aaffallen dürfen, to daM man nieht nStbig
hat, an ein Uineinapielen dea aramüaeh tonst nieht Tertretenen ptitsrm xn
### SOD ctx
5614  myy  C 
mey 

cloud,  gloom 
BSTii  906.1;  C2,  40V 1 

5615  myyk    B 
mexe  ©OP  mayuxa 
spike,  nail 
SCE  237 

5616  myyny  M 
mcync
```


## [2026-09-07T15:56:40.072Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY میخ\"; grep -n \"میخ\" incoming/ARY/ARY_pages.txt | head -10; echo \"### ARY میزبان/میز\"; grep -n \"میزبان\\|مِیز\\b\" incoming/ARY/ARY_pages.txt | head -6; echo \"### ARY latin index\"; grep -n -i \"MIX\\|MEX\\|MIZBAN\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-07T15:56:40.147Z] TOOL RESULT

```
### ARY میخ
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
612:میخی (/۲112331۳03) و به زبان‌های هتیت‌کهن (حدود ۲۰۰۰ تا ۱۵۰۰ پیش از میلاد) و هتیت.
798:که به تدریج با مهاجمان آمیخته شدند. در نتیجه‌ی این آمپزش» ملت انگلیس و زبان انگلیس ی کهن به
1128:وانگان میخی نگاشته شده‌اند. این نوشتارها اطلاع کمی درباره‌ی پارسی کهن و واژگان آن ارائه
1152:سلوکی (به خط میخی) و در تعدادی خشت‌های سفالی یافت می‌شود. در برخی متون مردمان
1286:امروزین نسبتاً آسان است ولی هر چه عقب برویم تعبین معنی دشوارتر و آمیخته با ابهام بیشتری
1991:آمیختن»- آمیز آمیغ آمیزه ۷۱
14155:ملس, ملیس (به چم "ترش و شیرین"» "میخوش؛) /_۲۷۷ أ
### ARY میزبان/میز
### ARY latin index
1968:MISCAN AMICAMEXTAN —:(PAHLA¥1) (5 hy,
1971:MIX ENGLISH) 3&3) AMIC ARMENIAN): gs)!
1983:BARNHART: (MIX) 668 MISHRAS, LITHUANIAN) gg
1986:MACKENZIE: 8, (MIX) 124 (OLD PRUSSIAN) 7S +9 9
1988:ONIONS: (MIX) 582 MESCAIM. HOLD IRISH) oS 5-23 2!
1989:SKEAT: (MIX) 381 MEASG (GAULISH) JE
10689:‘REFERENCES cathy cIMEX (LATIN) ops
14011:MYRION WELSH) jy WORMIKAS, MURMEX.(GREEK) iy
14114:MIXUR HOSSETIC) «iu \
14185:MARE, — (OLD ENGLISH) 4S" gui! MEX (PAHLAVI) «5 gly,
```


## [2026-09-07T15:56:48.885Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=14150 && NR<=14200' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== nearest page tag ===\"; awk 'NR<=14185 && /\\[pdf page/ {p=$0; n=NR} END{print n, p}' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Inspect ARY index near MEX"
}
```


### [2026-09-07T15:56:50.246Z] TOOL RESULT

```
4p cel eT VINUM 2 cis I ghsat sols S12 lt al edo G4 Zee 285i jhe
scent ¢ glee tga ala cal Jel
|
(ITALIAN) gid'ol MAITHA, MAIDHYA:(AVESTAN) pies!
MEDIO, (NEL) MEZZO MIVAN, MAYAN (PAHLAVI) 5.4,
(D0) MEIO — (PORTUGUESE) 9 x MIDAG, MEDAG, —-:(OSSETIC) .\ q
MIDJIS GOTHIC) S35 MEFIIO
(OLD SCANDINAVIAN) Ssh! MAYAN (KIRIN) (KURDISH) 62,5"
MEDHAL, MIDER NIYAMAGH, {(BALUCHD) gx 3h
MIDDIL — (OLD SAXON) oy gS NIVIMIG, NIYAM
MIDDEL — (OLD FRISIAN) eS 623 MANGJ, MIYANJ, :(AFGHANI) (5-4) git
HOLD HIGH GERMAN) oS gist MANDZ
MITTIL, MITTI MADHYA SANSKRIT) 2g Suile
MITTEL (GERMAN) glaT MBJ, MICHAG, (ARMENIAN) .5,!
MIDDEL :(OLD ENGLISH) eS oa) MICHIN, MECHDEGH
MIDDLE, MID- (ENGLISH) 5S MESOS, METHYOS, (GREEK) ly
MIDDLE, MIDT- (DANISH) jails MESO- .
MEDEL, MID- (SWEDISH) sty» MEDIUS LATIN) ys
MIDDEL, MIDT-  «(NORWGIAN) 553) (AU) MILIEU, MI- :FRENCH) «i\)
MIDDEL, MIDDEN- (DUTCH) scl» MEDIO (SPANISH) git!
i
[pdf page 486]
Tia
REFERENCES bok, (OLD CHURCH SLAVIC) nS 3%l
POKORNY = SSS*~*~*~*~«Sd MEZHDU
BARNHART: (MIDDLE) 659 MIEDZY POLISH) ling)
DELAMARRE: (AU MILIEU) 227 MEZHA RUSSIAN) ge 5
MACKENZIE: (BETWEEN) 104, MEZI (CZECH) Soy
(MIDDLE) 124 MEZHDA (BULGARIAN) ¢5 4,
BUCK: 863] | MEDZI SLOVAK) .f'\,Lel
ONIONS (MIDDLE) 575 IMMEDON, — (OLD IRISH) oS 54x!
SKEAT: (MIDDLE) 374 MIDE, MID-
RAMAT: 46 MEDIO- AGALISH) JE
rey bi dby
-MARI *MAIXA (OLD PERSIAN) tol go sh
MARE, — (OLD ENGLISH) 4S" gui! MEX (PAHLAVI) «5 gly,
GEMARE MIX, MEX H(OSSETIC) gs)
-TUIDMEN, = (OLD IRISH) «5 540) \ MIX (KURDISH) 52 5°
TUIDME MEH BALUCHI) gy she
\ MEX, MEXCU  :(4FGHAND (24) gli
: REFERENCES beth MYGHK * (SOGHDIAN) gt
POKORNY, SSSS™S~*~«SOD MAYOKHA = <(ANSKRIT) cy Se
MACKENZIE: (NAIL) 124 MOENIA, MOENIUM — (LATIN) fet ,
ner soo oby 4OLD $EANDINAVIAN) pS.s.thng
Jeelaal
. Sorel 2o2V O85 22 05s cal
[pdf page 487]
MITRA (NAME OF A GOD), KINDNESS, AFFECTION, 31 503) 0 gulS a f
AMITY, FRIENDS! HIRX LOVE . ;
ye or a |
MITHRA NAVESTAN) «glgh ;
=== nearest page tag ===
14171 [pdf page 486]
```


## [2026-09-07T15:57:06.368Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LEW mitis\"; grep -n \"mītis\\|mitis,\" LEW_1910.txt | head -6; echo \"### LEW munio\"; grep -n \"moenia\\|mūnio\" LEW_1910.txt | head -6; echo \"### LAT mitis\"; grep -n \"mitis\\|MITIS\" LAT.txt | head -6; echo \"### LAT munio\"; grep -n \"moenia\\|munio\" LAT.txt | head -6",
 "description": "Grep Walde and Ernout-Meillet"
}
```


### [2026-09-07T15:57:06.448Z] TOOL RESULT

```
### LEW mitis
### LEW munio
### LAT mitis
157:occupent des extrimitis du domaine indo-europien: ici, 1'on
13243:*comitissa, comes stabuli 3078a. Iri. coem.
32318:Emprunte egalement en gallois Hara, liari "mitis, mansuetus"; et
38366:mitis, -e: doux, douce. Se dit de la saveur, et en partieulier
38368:de "mur", "tendre", cf. Pl., Hi . 14234, mitis sum equidem fustibus (en
38378:immitis,-e, oppose 4 dulcis par Plin.13,36; immitis uua, Hor.C.3,5,10;
### LAT munio
958:ville des pommes", cf .Vg., Aen.7,740, ...maliferae... moenia Abellae.
1504:gronpe de minae est pina probable qne le rattachement k moenia.
5680:e.g. Sali., Ca.53,35, intra moenia atque in sinu urbis; ou "et pour-
6034:De meme Servius glose 1 'expression augusta moenia de Vg., Ae.7,133,
17275:condere urbem, moenia, carmen "r^unir les 4 l£aents d'une ville, d'un
38601:moene, -is n.; moenia, -ium (singulier trbs rare; un ex. dans
```


## [2026-09-07T15:57:08.569Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN mex\"; grep -n \"^ *10[0-9][0-9]\\. m\" HRN.txt | head -20; echo \"### HRN mIx\"; grep -n \"mex \\|m^ex\\|mix 'Nagel'\\|Nagel\" HRN.txt | head -10; echo \"### SKT mitigate\"; grep -n -i \"mitigate\" SKT.txt | head -5",
 "description": "Grep Horn for mex/Nagel"
}
```


### [2026-09-07T15:57:08.643Z] TOOL RESULT

```
### HRN mex
8696:1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
8703:1001. muhr 'Siegel; Siegelring,
8724:1003. mei 'Wein, jüd.-pers., ^^O.
8736:1004. miyün 'Mitte; mitten, mittlerer, miyäne,
8743:1005. mex Pflock, Nagel'.
8769:1007. meyezd *Gelage\
8772:1008. meS 'Schaaf, Widder.
8778:1009. mey *Wolke .
### HRN mIx
8743:1005. mex Pflock, Nagel'.
8745:LW\ kurd. mix; af/. we/, meyöü 'Nagel, Pflock';
8833:1016. nä%un *Nagel (am Finger oder an der Zehe)' 2).
8834:ai. nakhä- 'Nagel, Kralle'; phlv. nä/un (Bund.),
8835:kurd. neinuJc ^Nagel'; afy. nük; bei. näkun^ vahuft,
21221:d. mex lOOö.
### SKT mitigate
11726:mite  (z),  a  verv  &maU  portion.    (P M.  E,   mite.  -  O.   Du.   mijt,  mUt,  ■ small  coin,  a  mite.     Lit  '  cut  small  ;* Teuc.  base  MIT,  to  cut  (above). Mitigate.   (L.)     From  pp.  of  L. gart,  to  make  gentle.  ••  L*  mitis^  £( 'igare,  for  agerr^  to  make. Mitre,  a  head-dress,  esp.  for  a (F.-L.-Gk.)    O.F.  mi'/«-L.tw** cap.  —  Gk.  ^tirpa,  a  belt,  girdle. 61lct.  turban.
```


## [2026-09-07T15:57:15.396Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LAT mitis\"; sed -n '38366,38385p' LAT.txt; echo \"### LAT moenia\"; sed -n '38601,38625p' LAT.txt",
 "description": "Read Ernout-Meillet entries"
}
```


### [2026-09-07T15:57:15.459Z] TOOL RESULT

```
### LAT mitis
mitis, -e: doux, douce. Se dit de la saveur, et en partieulier
des fruits, sunt nobis mitia poma, Vg. B.1,81. Il s'y joint une id 4 e
de "mur", "tendre", cf. Pl., Hi . 14234, mitis sum equidem fustibus (en
j eu de mots avec mittis de mitto), cf. Non. 343, usqq.; de 14 le sens
de mitius "blet" dans les dialeetes italiens, cf,M,L.56i4 (avec un
doublet dialectal *me tius), S' applique aussi au moral; souvent joint
a placdtus, placidus (Vg. Ae. 8 , 80 ), tranquillus, lenis, etc. - Ancien,
classique.
D 4 riv 4 s et composes: mltescd,-is; mltig 5 ,-as et ses derives (cf.
pour la formation leuis/leuigo), dS-mltig 5 ; 2 -mltesc 5 , -mltig 5 (tar-
difs); immitigabilis (Cael.Aur.); mitificus, -fic 5 ; mitiusculus (Cael.
Aur.); nlti 5 ,-ls (Apic.).
immitis,-e, oppose 4 dulcis par Plin.13,36; immitis uua, Hor.C.3,5,10;
au sens moral "cruel, farouche". Ancien (Pl.), mais 4 vite par Cic.
et Ces.; repris a 1 'epoq.imp.
On rapproche gall. muydion "parties molles", iri.m oith "mou, tendre"
et d'autre part iri. m in "fin" (v.Pedersen, E. Gr. d.k. Spr ., I p.181 et
184).!« groupe de lit.milas, v.sl.m ilu "cher" differe pour le sens.mitiscus
7 84
mitiscus: est ubi homo tenet pedes, cum. sedet in equo, CGL V 681 ,
### LAT moenia
moene, -is n.; moenia, -ium (singulier trbs rare; un ex. dans
Naevius, B.P.Go, apud emporium in campo hostium pro moene (l.moeni?),
cite par Festus, 138,33, qui 1 'attribue faussement a Ennius; on emploie
le pluriel, pour lequel on rencontre les formes moeniorum, moeniis,
sans doute sous 1'influence de murus , ancien moiros, moerus, apparentemola
7a0 -
a la fois par la forme et par le sena. La diphtongue a’est conservde
dans moenia, tont au moins dans 1’ecriture, tandis que dans les derives
elle a abouti regulierement a u: muni 5 , cf. poena, punio', Poenus,
pUnicus. Le maintien de -oe~ dans moenia 3'explique par le caractbre
technique du mot, plutot que par la presence des deux i qui flanquent
l'n (opinion de Fr.Mulier, R.Et.lat., I y7 ). Le sena en est bien defini
par Festus, 138,25, moenia: muri et cetera muniendae urbis gratia
facta; ut Accius in Hellenibus (385): 11 Signa extemplo canere, ac tela
ob moenia offerre imperat" . Terme technique de sens plus large que
murus, comme on le voit par le vera de Vg., Ae.a, 334: diuidimus muros
et moenia pandimus urbis. D'ou le sens de "construction" (e.g. Ae.6,54y
moenia lata uidet triplici circumdata muro), et de "ville fortifiee"
( = oppidum).
L'homonymie avec munus (ancien moinos, moenus) amene 1 ’etymologie
de Varr., L.L.5,141, quod muniendi causa portabatur, munus, quod se-
piebant oppidum eo moenere, moerus. - Ancien, classique, mais rare
a 1 '^poque imperiale en dehors de la langue po^tique. Non roman.
Denominatif: munio,-Is,-lui ( - ii), - itum, -ire: fortifier, munir
( sens physique et moral), qui a fourni a son tour de nombreux derives
```


## [2026-09-07T15:57:17.375Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8743,8768p' HRN.txt; echo \"=== find HRN page for 1005/1007 ===\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,L in enumerate(leaves):\n    if '1005. mex' in L or '1007. meyezd' in L:\n        print('leaf(0-based)',i,'-> printed p.',i-21)\nEOF",
 "description": "Read Horn 1005 and page"
}
```


### [2026-09-07T15:57:18.861Z] TOOL RESULT

```
1005. mex Pflock, Nagel'.
ai. vergl. mayukha- 'Pflock' (?).
LW\ kurd. mix; af/. we/, meyöü 'Nagel, Pflock';
oss. d. mex, t. mix 'Pfahl (187); bei. meh (239);
wa/. mix, sar. max,
bei. mik aufgerichtet' (239), das Geiger ansehliesst.
Uorn. Orundriss <J. neup. Fltyniolo^ic. ],j— 226 —
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
=== find HRN page for 1005/1007 ===
leaf(0-based) 246 -> printed p. 225
leaf(0-based) 247 -> printed p. 226
```


## [2026-09-07T15:57:35.203Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC moiros/mei fix\"; grep -n \"moiros\\|mei- (1)\\|meiô\\|minomi\\|mitis, e\\|moinis\" IEC.txt | head -12; echo \"### SYN nail/peg\"; grep -n -i \"Skt. mayukha\\|mayūkha\\|NAIL\\b\" SYN.txt | head -8; echo \"### SYN wall\"; grep -n \"moenia\" SYN.txt | head -5",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-07T15:57:35.289Z] TOOL RESULT

```
### IEC moiros/mei fix
11042:moiros (?) (Evidence ambig.) OLat. & Lat. moerus, mūrus, gs -1, m. ‘wall’; pro-moerium ‘boundary wal’; W mur, adj. “fixed, firm’. (For OE mëre “boundary, baulk’, cf. mér-)
### SYN nail/peg
5173:wurm ‘dragon’), all orig. ‘worm’. See 3.84. ON snakr, Dan. snog, Sw. snok, OF snaca, ME, NE snake (displacing ser- pent in pop. use) : OHG snahan ‘crawl’, OE snegl ‘snail’, etc. Walde-P. 1.697 ff. Falk-Torp 1098.
6272:nail’, As noted above
6307:orig. ‘claw’, coll. formation to Lith. nagas, Lett. nags ‘nail (on finger or toe), claw’ (4.39). Walde-P. 1.180 f.
6323:4.39 NAIL Goth. «.-- Lith. mnagas Lett. nags out ON _ nagl J oe ie Dan. negli ChSl.  nogittt N unguts Sw. nagel SCr.  nokat Bs unghia OE negl Boh. nehet " — ongle ME We oe pene “ ufia NE nat E Rum. unghie Du. nagel Skt. nakha- ingen OHG  nagal Av. sri, srvd- Nir. tong MHG  nagel ' lal NHG  nagel ivin
6692:Miscellaneous and doubtful. Lat. mato, Ir. moth (Walde-P. 2.312. Ernout-M. 649) ; Lat. mentula (> It. minchia), etym. dub. (Walde-H. 2.72. REW 5513) : It. cazzo (: cazza ‘crucible’?); Rum. puld (Tiktin 1277 f.); Ir. biach (Walde-P. 1.667) ; Ir. bot, NIr. bod : W. both ‘nave of a wheel, boss of a shield’, perh. ChSI. gvozdt ‘nail’ (Pokorny, Z. celt. Ph. 16.405. Walde-H. 1.574); OE teors, ME, NE terse, tarse (NED tarse sb.'), OHG, MHG zers (perh. : OE teran ‘tear,’ etc. Walde-P. 1.802); Lith. bybzs; Pol. kutas (‘tassle’, Berneker 653) : Skt. cigna- (Walde-P. 1.402); Skt. kaprt(h)- (Walde- P. 1.348, 2.49).
8899:Meyer, Neugr. Stud. 2.99, 3.61, but with no mention of xéradis) is unsatisfactory, 2. Lat. coc(h)ledre, coc(h)ledrium, a small spoon with one end pointed, used for eating snails and eggs (Mart. 14,121 sum cochleis habilis, sed non minus ovis. Numquid scis potius cur cochleare vocor), deriv. of coc(h)lea ‘snail’, this fr. Grk. xoxNas. Hence It. cucchiaio, Fr. cuiller, cuilliére, Sp. cuchara, also OE cuc(e)ler. Walde-H. 1.241, TErnout-M. 201. Walde-H. 1.241. REW 2012.
11779:1. IE *klau-, klawi-, denoting the wooden peg which was the primitive ‘key’, cognate with words meaning ‘peg’ or ‘nail’ as Lat. clavus, Ir. clo, and with verbs meaning ‘hook’ as Lith. kliutt, or ‘shut’ as Lat. claudere. Walde-P. I,
11907:‘stake, palisade’ : Goth. walus ‘staff’, Grk. #dos ‘nail’, etc. Walde-P. 1.301. NED s.v. wall, sb.}.
### SYN wall
11882:Grk. _—_retxos} rotxos, retxlov Goth. -waddjus Lith. miras; stena NG TotxXos ON mirr; veggr Lett. miiris; siena Lat. mitrus, moenia (pl.); Dan. mur; vag Chl. zidit, sléna paries Sw. mur; vdgg SCr. id, stijena It. muro; parele OE weall; wag Boh. zed’; sténa Fr. mur, muraille ME wall (waw) Pol. mur; Sciana Sp. muro; pared NE wall Russ. stena Rum. id; pdrete Du. muur; wand Skt. dehi-, prakdara-; ky- Ir. mur; fraig OHG mira; want dya~ NIr. muir; falla (fraigh) MHG mir(e); want Av. uzdaézi- W. mur, gwal, magwyr; NHG mauer; wand pared Br. moger
11889:2. Lat. mirus (early moerus) and moenia (pl.) : Skt. mé- ‘fix, build’, etc. Walde-P. 2.239f. Ernout-M. 624 ley 645 (without etym.).
32949:ON landa-mé@ri, OE (ge)mére, ME (and NE dial.) mere, MDu. mére, orig. the (boundary) ‘stake’, fr. Gmc. *mairia- : Lat. mirus, old moiros ‘wall’, moenia ‘walls’, Skt. mi- ‘fix, build’, ete. Walde- P, 2.239 f. Franck, KZ 37.120 ff. NED S.v. mere, sb.?.
```


## [2026-09-07T15:58:32.241Z] TOOL CALL #61: Bash

```json
{
 "command": "ls site/pages/326.jpg 2>/dev/null; pdftoppm -f 326 -l 326 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg326 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg326.png",
 "description": "Render PDF page 326"
}
```


### [2026-09-07T15:58:34.014Z] TOOL RESULT

```
site/pages/326.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 55902 Sep  7 11:58 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg326.png
```


## [2026-09-07T15:58:37.064Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg326.png"
}
```


### [2026-09-07T15:58:37.393Z] TOOL RESULT

```

```


## [2026-09-07T15:58:37.391Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T15:58:59.545Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg326.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/326.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T15:58:59.612Z] TOOL RESULT

```
total 14400
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 11:58 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T15:59:00.288Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-07T15:59:00.328Z] TOOL RESULT

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


## [2026-09-07T15:59:03.502Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-07T15:59:03.540Z] TOOL RESULT

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


## [2026-09-07T16:00:21.849Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:11:46.957Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_MIZBAN = \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B2%D8%A8%D8%A7%D9%86\"\nW_MIX    = \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%AE\"\nW_MAIDA  = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%A6%D8%AF%D8%A9\"\nW_MITIS  = \"https://en.wiktionary.org/wiki/mitis\"\nE_MITIG  = \"https://www.etymonline.com/word/mitigate\"\nE_AMMO   = \"https://www.etymonline.com/word/ammunition\"\n\ndata = {\n \"pdf_page\": 326,\n \"book_page\": 296,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"Mei 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *mei- / *meyẖ₁- (de Vaan *meh₁i-) 'mild, soft, gentle, pleasant' — Pokorny 'mei-7: moi-, mī-', pp. 711-712\",\n   \"note\": \"Root, language label and gloss are all right, and the page number is right: POK_full.txt (line 60686 ff.) has 'Root / lemma: mei-7: moi-, mī-  Meaning: mild, soft  Note: often with dh-, n-, r-, l-extended … References: WP. II 244, WH. II 96 f.  Page(s): 711-712', i.e. the article begins on the page Nourai cites (711) and runs on to 712, which is why node #1 carries POK:712. Watkins' appendix has the same root as 'mē(i)-. Mild. Contracted from *meəi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.]', and Walde-Pokorny II 244 opens '8. mei-, mī- \\\"weich, sanft, gelınde; erquicklich, liebreich\\\"'. Two structural remarks. (a) Pokorny sets up seven homophonous mei- roots; Nourai's 'Mei 1' and 'Mei 2' are his own numbering, and they correspond to Pokorny's mei-7 (711) and mei-1 (709) respectively, not to Pokorny's 1 and 2 — the reader should not read the numbers as Pokorny's. (b) Nourai's chart reproduces Pokorny's own material list for mei-7 in order: Skt. mayas- → *m(i)ies-dh(e)- → Skt. miyedha- / Av. myazda-, and 'with t-: Latin mītis'; the Arabic māʾida branch is Nourai's own addition and is the only weak link in the entry. Modern reconstruction writes the root *meyh₁- (or, with de Vaan, *meh₁i-, an extension of *meh₁- 'to measure'); the semantics 'soft, mild' are undisputed.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mei- (در نگارش امروزی *meyh₁- یا به رأی دِ فان *meh₁i-) به معنی «نرم، ملایم، دلپسند» ریشه‌ای پذیرفته است: پوکورنی آن را زیر مادهٔ mei-7 در صفحات ۷۱۱–۷۱۲ با همین معنی می‌آورد و والده–پوکورنی (جلد ۲ ص ۲۴۴) و پیوست واتکینز نیز همین را دارند؛ پس برچسب زبانی، معنی و شمارهٔ صفحهٔ نورایی درست است. دو نکته: یکی آنکه پوکورنی هفت ریشهٔ هم‌نگاشت mei- دارد و «Mei 1» و «Mei 2» شماره‌گذاری خود نورایی است (به‌ترتیب mei-7 و mei-1 پوکورنی)؛ دیگر آنکه همهٔ شاخه‌های نمودار جز شاخهٔ عربی (مائدة) عیناً از مقالهٔ پوکورنی گرفته شده‌اند؛ شاخهٔ عربی افزودهٔ خود اوست و همان نقطهٔ سست این مدخل است.\",\n   \"sources\": [W_MITIS],\n   \"ref_check\": [\n    {\"ref\": \"POK:711\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 60686 ff.: 'Root / lemma: mei-7: moi-, mī-  Meaning: mild, soft  Note: often with dh-, n-, r-, l-extended … References: WP. II 244, WH. II 96 f.  Page(s): 711-712'. The article starts on 711 exactly as cited.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 244 (WLD_Bd2_pages.txt leaf 248, printed number '244' in the header)\", \"stance\": \"supports\",\n     \"note\": \"'8. mei-, mī- „weich, sanft, gelınde; erquicklich, liebreich“ … Ai. māyas n. „Labsal, Freude, Lust“, dazu *m(i)ies-dh(e)- in ai. miyedha- m. „Opferspeise“, av. myazda- m. „Opfermal“ … Mit t-Formantien lat. mītis „mild, gelind“' — the article Pokorny cites as WP. II 244, containing both of Nourai's branches.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mē(i)- (AHD_watkins1985.txt line 734; index line 1877 'MITIGATE mē(i)-')\", \"stance\": \"supports\",\n     \"note\": \"'mē(i)-. Mild. Contracted from *meəi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. 'meit- (1) (moit-)' and 'moitos, is (2)' (IEC.txt lines 10499, 11050)\", \"stance\": \"partial\",\n     \"note\": \"'meit- (1) (moit-) “soft, gentle”. WP II, 238 & 247 … Lat. mitis “gentle, soft, overripe”' and 'moitos, is (2) “soft, tender, mild, tame” … Lat. mitis' — Mann keeps the Latin word but files it under the t-extension as a lemma of its own, with no root box 'mei- mild'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. mitigate (KLN_1966.txt line 24059)\", \"stance\": \"supports\",\n     \"note\": \"'The first element prob. stands for *mi-tis and derives fr. I.-E. base *mei-, *mi-, “soft, mild, tender, gentle; peaceful, lovely” … OI. mayah, “enjoyment, pleasure” … prob. also derive fr. I.-E. base *mei-, *mi-.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 784 s.v. mitis (LAT.txt line 38366 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'mitis, -e: doux, douce … On rapproche gall. mwydion “parties molles”, iri. moith “mou, tendre” et d'autre part iri. mīn “fin” … Le groupe de lit. mielas, v.sl. milu “cher” diffère pour le sens.' They accept the Celtic comparison (hence the root) but doubt the Baltic-Slavic members.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"mayazda\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word is genuine but the shape and the gloss in the box are both loose. Avestan has myazda- m. (Bartholomae, AiW col. 1189, BRT.txt line 20622: 'j., g. myazda- m. Bezeichnung der zum Opfer bestimmten, als Opfer dargebrachten festen (nicht flüssigen) Genussmittel, „feste Opferspende, Opferspeise, Speiseopfer“'), attested throughout the Y̱asna, Vispered, Nirangistān and Āfrinagān (Y. 8.2, Vr. 11.2, N. 63, A. 3.6-12), with the derivatives myazda-van- 'who has offered a myazda' and myezdin-. Its formation is exactly what Pokorny 712 gives for this root: *m(i)ies-dh(e)- = the es-stem of *meyh₁- (Skt. máyas- n. 'refreshment, pleasure', Av. maiiah-) + the root *dẖeh₁- 'to place, set down', i.e. 'the setting-out of pleasant things'; the exact Indic match is miyédha- m. 'sacrificial food' (RV), so the arrow root → Avestan is right. Two reservations keep this from 'confirmed'. (a) The attested Avestan form is myazda-, not mayazda-; Nourai has back-projected the New Persian/Parsi vocalisation mayazd onto Avestan (Mo'in's footnote in Borhan p. 2076 also writes the Avestan as myazda). (b) Semantically myazda- is the solid food-offering itself, opposed to the liquid offering zaoq̊ra-/zōhr; the 'guests' element in the gloss belongs only to the much later New Persian mīzbān (node #3) and is anachronistic for Avestan. The printed page (data/verification/sources/refs/ocr/BOOK/326.png) shows the gloss set on three lines as 'a special meal / of Zoroastrians, guests / guests invited to a meal': the word 'guests' really is printed twice — a dittography across the line break in the book itself, faithfully carried into the JSON, not an extraction error.\",\n     \"derivation_fa\": \"واژه اصل دارد اما صورت و معنایش در جعبه دقیق نیست. در اوستا صورت گواهی‌شده myazda- است (بارتولومه، فرهنگ ایرانی باستان، ستون ۱۱۸۹) به معنی «پیشکش و خوراکِ جامدِ قربانی» در برابر پیشکش مایع (zaoq̊ra- / زور)؛ پوکورنی (ص ۷۱۲) ساخت آن را *m(i)ies-dh(e)- می‌داند، یعنی ستاک es-دارِ ریشهٔ *meyh₁- (سنسکریت máyas- «خوشی، پیشکش گوارا») به‌علاوهٔ ریشهٔ *dẖeh₁- «نهادن»؛ برابر دقیق هندی آن miyédha- «خوراک قربانی» است؛ پس پیکان ریشه ← اوستایی درست است. دو ایراد: یکی آنکه نورایی واکه‌گذاری فارسی/پارسیانِ «مَیَزد» را به اوستایی برگردانده و mayazda نوشته است؛ دیگر آنکه معنی «میهمانان» در این مرحله وجود ندارد و تنها در فارسی نو و از راه «میزبان» پیدا شده است. تصویر صفحهٔ چاپی (BOOK/326.png) نشان می‌دهد که تکرار واژهٔ guests در خود کتاب و در مرزِ سطر رخ داده است؛ پس خطای خوانش اسکن نیست، خطای حروف‌چینی کتاب است.\",\n     \"sources\": [W_MIZBAN],\n     \"ref_check\": [\n      {\"ref\": \"POK:712\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 60704 (POK_02.txt line 5935): 'Old Indic mayas- n. “relief, pleasure, joy, lust”, in addition *m(i)ies-dh(e)- Old Indic miyedha- m. “sacrificial food”, Avestan myazda- m. “sacrificial meal”' — on the second page of the mei-7 article, exactly the arrow Nourai draws, and the reason the node cites 712 while the root cites 711.\"},\n      {\"ref\": \"MON:4494\", \"status\": \"partial\",\n       \"note\": \"The page number cannot be checked against the local OCR (Mo'in's pagination is not mapped), but Mo'in's entry exists and reads (MON_part2.txt line ~70195, s.v. میزد) '(زردشتی) نذر و تقدیمی غیر مایع و فدیه، چیزی خوردنی در مقابل نذر مایع و آشامیدنی (زور)' — it supports the Zoroastrian food-offering sense but gives no Avestan form there, so it cannot carry the etymological arrow by itself.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1189 s.v. myazda- (BRT.txt lines 20622-20631)\", \"stance\": \"supports\",\n       \"note\": \"'j., g. myazda- m. … „feste Opferspende, Opferspeise, Speiseopfer“: mazdayasna … myazdəm daiṯ̱y̱ārəta gaoməntəm V. 6.22 … Pü. myazdōmand' — the Avestan lemma is myazda-, with the derived adjectives myazda-van(t)- and myezdin-; there is no form mayazda-.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 1007, p. 226 (HRN.txt line 8769)\", \"stance\": \"supports\",\n       \"note\": \"'1007. meyezd „Gelage“. aw. myazda- „Opfermahl“; phlv. myazd, myāzd; ai. miyidha- [miyedha-].' Horn gives the whole Avestan → Pahlavi → New Persian chain of nodes #1-#3.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien § 91b p. 101 and § (p. 223) (HUB.txt lines 7018, 7972)\", \"stance\": \"supports\",\n       \"note\": \"'miyazd „Gelage“ = zd. myazda-, skr. miyedha-' and 'np. miyazd „Gelage“ (Parsenwort) = zd. myazda-'; Hübschmann adds that the New Persian word is a Parsi technical term, i.e. a learned continuation, and that -zd is the regular Old-Persian-type reflex.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 244 (leaf 248)\", \"stance\": \"supports\",\n       \"note\": \"'dazu *m(i)ies-dh(e)- in ai. miyedha- m. „Opferspeise“, av. myazda- m. „Opfermal“ (unmittelbar von der Wz. …)'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"mayazd, mâz\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The first form is right, the second is a ghost. Middle Persian has myazd / mēzd ⟨myzd⟩ 'offering, (ritual) meal': MacKenzie, CPD p. 56 'mezd [myzd | N mez] offering, meal', and his English-Pahlavi index gives 'offering mezd, parag, us(t)ōfrit, zōhr' and 'meal bazm, čāst, mezd, sūr'; Horn no. 1007 cites the Book Pahlavi spellings 'phlv. myazd, myāzd'. The development is regular: Av. myazda- loses its thematic vowel and the initial cluster my- is read mē-/miya- in Middle Persian (hence the two transliterations myazd and mēzd of one ⟨myzd⟩), the group -zd being preserved as in mizd 'wage', nazd 'near'. 'māz', however, is not an attested Pahlavi word: it comes from Praetorius' attempt (ZDMG 61, 622 ff.) to derive Arabic māʾida from Persian mēz 'table', which he claimed was 'earlier pronounced māz' (Jeffery, FVQ 256, i.e. the very page Nourai cites through its Persian translation VDQ:370), and Nöldeke rejected precisely those forms: 'Nöldeke rightly objects that the forms miz and māz which Praetorius quotes from the Mehri and ʿUmani dialects in favour of his theory are hardly to the point, for these dialects are full of Persian elements of late importation.' So the Pahlavi box should read myazd/mēzd alone.\",\n     \"derivation_fa\": \"صورت نخست درست است و صورت دوم ساختگی. در فارسی میانه واژهٔ ⟨myzd⟩ = myazd / mēzd «پیشکش، خوراک آیینی» گواهی دارد: مکنزی در فرهنگ کوچک پهلوی (ص ۵۶) می‌نویسد mezd [myzd | N mez] «offering, meal» و هرن (شمارهٔ ۱۰۰۷) نیز دو نگاشت myazd و myāzd را می‌آورد. دگرگونی به‌قاعده است: پایانهٔ اوستایی -a می‌افتد و خوشهٔ -zd مانند mizd «مزد» و nazd «نزد» نگه داشته می‌شود. اما māz هیچ گواهی پهلوی ندارد؛ این صورت را پراتوریوس برای اشتقاق عربی «مائدة» از «میز» فرض کرده بود و نولدکه همان صورت‌های miz و māz را رد کرده است (جفری، واژه‌های دخیل در قرآن، ص ۲۵۶ — همان صفحه‌ای که نورایی از راه ترجمهٔ فارسی به آن ارجاع داده). پس درستِ این جعبه تنها myazd/mēzd است.\",\n     \"sources\": [W_MIZBAN],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2076\", \"status\": \"supports\",\n       \"note\": \"Page fetched with tools/ref_page.py BQT:2076 (vol. 4 scan, pdf p. 159; cached at refs/ocr/BQT/2076.png/.txt). Mo'in's footnote 7 to میز reads 'ظ. از اوستایی myazda (میزد) … رک: میزد، و رک: میزبان' — the printed page number matches and the footnote is the Avestan-to-Persian link, with the Pahlavi stage implied by 'myazd'.\"},\n      {\"ref\": \"VDQ:370\", \"status\": \"partial\",\n       \"note\": \"VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib behind a JS viewer, so it was checked in the original: Jeffery, FVQ p. 256 (FVQ_pages.txt line ~9209) 'Now there is a Phlv. word myazd, meaning a sacred repast of the Parsis, of which the people partake at certain festivals after the recitation of prayers …' — the reference does give the Pahlavi word (supporting this box), but on the same page it refuses the Arabic derivation drawn from it (see node #4).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 56 (PHD_mackenzie.txt lines 3550-3554) and the English-Pahlavi index (lines 7075, 7160)\", \"stance\": \"supports\",\n       \"note\": \"'mezd [myzd | N mez] offering, meal'; 'meal bazm, čāst, mezd, sūr'; 'offering mezd, parag, us(t)ōfrit, zōhr'. MacKenzie reads the Book Pahlavi ⟨myzd⟩ as mēzd and gives New Persian mez, not māz.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary) — grep for 'mezd'/'myazd' finds only 'Hōrmezd' (NYB_vol2_glossary.txt line 6641)\", \"stance\": \"silent\",\n       \"note\": \"The glossary covers only the texts of Part I, in which the offering word does not occur; it therefore neither supports nor contradicts. (Nyberg does have mēx, used for entry 2 node #1.)\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 1007, p. 226\", \"stance\": \"supports\",\n       \"note\": \"'phlv. myazd, myāzd' — the two Pahlavi readings; no māz.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. میزد (MON_part2.txt line ~70195)\", \"stance\": \"partial\",\n       \"note\": \"'(زردشتی) نذر و تقدیمی غیر مایع و فدیه، چیزی خوردنی در مقابل نذر مایع و آشامیدنی (زور)' — the sense, but no Pahlavi form.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"mayazd «مَیَزد» : feast, guests ; mîzbân «میزبان» : host\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Persian words are real and the arrow from Pahlavi is standard. (a) مَیَزد mayazd (Horn reads it meyezd, Hübschmann miyazd, and calls it a 'Parsenwort', i.e. a Zoroastrian technical term kept in learned use) continues MP myazd/mēzd directly, with no phonetic change beyond the New Persian reading of ⟨myzd⟩; Mo'in glosses it '(زردشتی) نذر و تقدیمی غیر مایع … در مقابل نذر مایع (زور)', preserving the Avestan myazda-/zaoq̊ra- opposition, and Borhan-e Qāteʿ p. 2076 (Mo'in's footnote 7 to میز) links میز / میزد / میزبان to Avestan myazda. The Farrokhī line in the chart ('ای به مَیَزد اندرون هزار فریدون – ای به نبرد اندرون هزار تهمتن') is the classical shāhed for the extended sense 'banquet'. (b) میزبان mēzbān/mīzbān 'host' goes back to Middle Persian ⟨myzdpʾḇn⟩ mēzdbān, literally 'keeper of the mēzd (feast)' (mēzd + the agent suffix -bān < OIr. -pāna- 'guarding'); MacKenzie's English index gives 'host mezdbān' and Wiktionary cites the same Book Pahlavi spelling. In New Persian the -d- of mēzd was lost in the cluster -zdb- (mēzdbān > mēzbān), and میز mēz 'table' — which Mo'in analyses as میز + بان — is best explained as a back-formation from it (whence, later, Ottoman/Turkish and Indic mezbān; Hūsayn Kāzim Qadrī, quoted in Mo'in's footnote, notes 'Turkish takes میز and میزبان from Persian'). Nourai's '☞ Pa' cross-reference on mīzbān is thus correct.\",\n     \"derivation_fa\": \"هر دو واژه فارسی راستین‌اند و پیکان از فارسی میانه پذیرفته است. «مَیَزد» (خوانش هرن: meyezd؛ هوبشمان: miyazd و آن را «واژهٔ پارسیان» می‌نامد) دنبالهٔ مستقیم myazd فارسی میانه است؛ معین معنی آن را «نذر و تقدیمی غیر مایع در مقابل زور» می‌داند که همان تقابل اوستایی myazda-/zaoq̊ra- است، و در حاشیهٔ برهان قاطع (ص ۲۰۷۶) معین «میز، میزد، میزبان» را به اوستایی myazda باز می‌گرداند؛ بیت فرخی نیز شاهد کلاسیک معنی «بزم» است. «میزبان» از فارسی میانهٔ mēzdbān ⟨myzdpʾḇn⟩ «نگاهبان/برپاکنندهٔ میزد» است (mēzd + پسوند -bān از ایرانی باستان -pāna-)؛ دال در خوشهٔ -zdb- افتاده و mēzbān شده، و «میز» به معنی خوان/میز را بهتر است ساختهٔ پسینی (قیاسی) از همین میزبان دانست؛ از فارسی به ترکی و زبان‌های هند هم رفته است. ارجاع «☞ Pa» نورایی درست است.\",\n     \"sources\": [W_MIZBAN],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2076\", \"status\": \"supports\",\n       \"note\": \"refs/ocr/BQT/2076.txt (fetched with ref_page.py, vol. 4 pdf p. 159): the page carries the entries میز and میزبان ('میزبان ۱۲- … ضیافت کننده باشد یعنی شخصی که مردم را ضیافت …') with Mo'in's footnote 'ظ. از اوستایی myazda (میزد) … رک: میزد، و رک: میزبان' and 'ترکی مأخوذ از فارسی «میز» و «میزبان» «حسین کازم قدری»'. Exactly Nourai's arrow.\"},\n      {\"ref\": \"MON:4494\", \"status\": \"supports\",\n       \"note\": \"Mo'in's page numbers are not mappable in the local OCR, but the entries are there: MON_part2.txt line 70193 'میزبان: [میز + بان < بان …] کسی که چند تن را به مهمانی خود دعوت و پذیرایی کند؛ ضیافت کننده، مق. مهمان' immediately followed by the entry میزد; both of Nourai's Persian words stand on the same Mo'in page, as his single citation implies.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. میزبان and میزد (MON_part2.txt lines 70193-70197)\", \"stance\": \"supports\",\n       \"note\": \"'میزبان: [میز + بان] … ضیافت کننده'; the following entry میزد '(زردشتی) نذر و تقدیمی غیر مایع … (زور)'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD, English-Pahlavi index p. 155 (PHD_mackenzie.txt line 6794)\", \"stance\": \"supports\",\n       \"note\": \"'host mezdban.' — the Middle Persian ancestor of میزبان, from mezd 'offering, meal' (p. 56).\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 1007, p. 226\", \"stance\": \"supports\",\n       \"note\": \"'1007. meyezd „Gelage“' — the New Persian word treated as the direct continuation of Av. myazda- through Pahlavi myazd.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 223 (HUB.txt line 7972)\", \"stance\": \"supports\",\n       \"note\": \"'np. miyazd „Gelage“ (Parsenwort) = zd. myazda-' — with the sound law 'iran. zd = ap. np. zd' explaining the preservation of -zd.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Arabic\",\n     \"words\": \"mâ`da\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Arabic word is real but its origin is not the Pahlavi feast-word, and Nourai's own second reference says so. The Qurʾanic مائدة māʾida (Q 5:112, 114 — the sūra is named after it) means 'table (spread with food)' and, metonymically, 'the food'; Nourai's spelling 'mâ`da' (so printed on p. 296) is a defective rendering of māʾida, the active participle-shaped form the Arab lexicographers derived from māda/yamīdu 'to move, sway' (Lisān al-ʿArab iv, 420). Modern scholarship: Fraenkel, Aramäische Fremdwörter p. 24, called it 'eine rein zufällige Entlehnung durch Mohammed … aus äthiop. māʿed „Tisch“ (Dillmann 197)'; Nöldeke, Neue Beiträge 54, according to Jeffery 'has practically put the matter beyond doubt'; Jeffery himself (FVQ 255-256 = VDQ:370) reports Addi Shir's and Praetorius' Persian proposals and rejects them — 'It seems, however, very difficult to derive māʾida from this [Phlv. myazd], and still more difficult from the forms proposed by Praetorius … Praetorius has given no real explanation of the change of z to d, whereas on the other side may be quoted the Bilin mid and the Beja mes which are correct formations from a stem giving māʿedd in Eth., and thus argue for its originality in that stock' — and Wiktionary today has simply 'Borrowed from Geʿez ሙእድ (maʾadd, “table”), which is of unknown origin'. Two concrete phonetic objections stand against the chart: Middle Persian mēzd/māz would give Arabic *mīz/*māz with zāy (as in Arabic loans mīzāb, mizmar), not مائدة with hamza + dāl, and the Arabic word is a feminine in -a with a hamzated stem, i.e. shaped on an Arabic pattern, which fits a Geʿez maʾadd far better. Addi Shir's page (AFM 148) does argue for a Persian source, but not for Nourai's: he derives مائدة from Persian میده 'fine wheaten bread' ('وقیل من ماد یمید اذا تحرک … انها معربة عن … وهو خبز السمیذ بالفارسیة'), a derivation nobody now accepts.\",\n     \"derivation_fa\": \"واژهٔ عربی واقعی است، ولی خاستگاهِ آن «میزد» پهلوی نیست و خودِ مأخذِ دومِ نورایی هم همین را می‌گوید. «مائدة» قرآنی (مائده ۵ؚ۱۱۲ و ۱۱۴) «خوانِ پرواز خوراک» است و نگاشت «mâ`da» در کتاب نگاشتی نارسا از māʾida است. پژوهش امروزی آن را وام‌واژه‌ای از حبشی (گعز) maʾadd «خوان، میز» می‌داند: فرنکل (ص ۲۴)، نولدکه (Neue Beiträge ۵۴) و جفری (ص ۲۵۵–۲۵۶) و ویکی‌واژه؛ جفری صریحاً می‌نویسد گرفتن مائدة از myazd پهلوی «بسیار دشوار» است و پراتوریوس برای تبدیل z به d هیچ توضیحی نداده است. دو ایراد آوایی روشن است: از mēzd/māz در عربی انتظار *میز/*ماز با زای می‌رود (مانند میزاب و مزمار)، نه مائدة با همزه و دال؛ و ساخت مونثِ مائدة با ریشهٔ مهموز به وام‌گیری از گعز می‌ماند. افزون بر این، ادیّ شیر (ص ۱۴۸) که نورایی به او ارجاع داده، مائدة را معرّبِ «میده» (خبز السمید) می‌داند، نه مَیَزد؛ پس این پیکان را باید ردشده دانست.\",\n     \"sources\": [W_MAIDA],\n     \"ref_check\": [\n      {\"ref\": \"AFM:148\", \"status\": \"partial\",\n       \"note\": \"Addi Shir's مائدة entry stands on the leaf of AFM_pages.txt (0-based leaf 149) that Jeffery cites as 'Addai Sher, 148': '(( مائدة )) الطعام والخوان علیه الطعام … وقیل من ماد یمید اذا تحرک (اقرب الموارد) … انها معربة عن [میده] وهو خبز السمیذ بالفارسیة', with the Fraenkel footnote continuing on the next leaf ('اما فرنکل … ان المائدة تعریب …'). So the page does claim a Persian origin — but from میده 'fine bread', not from mayazd/māz; it does not support the arrow as drawn. (Jeffery, p. 255: 'Addai Sher, 148, however, has argued in favour of its being taken as a Persian word … he wishes to derive it from Pers. mīda, meaning farina triticea.')\"},\n      {\"ref\": \"VDQ:370\", \"status\": \"contradicts\",\n       \"note\": \"Checked in the original of which VDQ is the translation — Jeffery, FVQ pp. 255-256 (FVQ_pages.txt lines 9180-9222): 'A late word found only in a late Madinan verse … Fraenkel, Vocab, 24, pointed out that in all probability the word is the Eth. māʿedd … while Nöldeke's examination of the word in Neue Beiträge, 54, has practically put the matter beyond doubt … It seems, however, very difficult to derive māʾida from this [Phlv. myazd], and still more difficult from the forms proposed by Praetorius.' Nourai's own reference rejects his arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qurʾān, pp. 255-256 s.v. Māʾida (FVQ_pages.txt leaf 272-273)\", \"stance\": \"contradicts\",\n       \"note\": \"See the quotation above; Jeffery settles for Ethiopic and reports both Persian proposals as rejected.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen p. 24 (AFA.txt line 3304)\", \"stance\": \"contradicts\",\n       \"note\": \"'… und eine rein zufällige Entlehnung durch Mohammed ist مائدة aus äthiop. māʿed „Tisch“ (Dillmann 197).'\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen — grep for مائدة in PLA_pages.txt finds nothing\", \"stance\": \"silent\",\n       \"note\": \"Asbaghi's corpus of Persian loanwords in Arabic does not list مائدة at all, i.e. the standard modern handbook of Persian→Arabic loans does not recognise it as one.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs — no entry for māʾida (grep silent; only maidān at no. 1364)\", \"stance\": \"silent\",\n       \"note\": \"No Oriental-loan entry, as expected for a word that stayed inside Arabic and Persian.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"mâedeh «مائده» (also مایده)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian مائده māʾeda 'food; a table spread with food' is a straightforward learned borrowing of Arabic مائدة māʾida, taken over with the Qurʾanic overtone (مائدهٔ مسیح, مائدهٔ آسمانی), the Arabic feminine ـة being written ـه in Persian and the hamza optionally dropped in the popular spelling مایده that the chart prints as a variant. Mo'in labels it exactly so: 'مائده: [ع. مائدة: ف. مایده] (ا.) خوردنی. خوانی که بر آن طعام باشد' — '[Arabic مائدة: Persian مایده]', which is both the loan direction Nourai draws and the source of his bracketed second script form. The one caveat is systemic rather than local: because the Arabic word is itself a Geʿez loan (node #4), this is not the Persian→Arabic→Persian round trip the chart implies, but a one-way Arabic loan into Persian.\",\n     \"derivation_fa\": \"«مائده» در فارسی نو وام‌واژه‌ای کتابی از عربی مائدة است که با بارِ قرآنیِ خود (مائدهٔ مسیح، مائدهٔ آسمانی) به فارسی راه یافته؛ تای تأنیث عربی در فارسی ـه نوشته می‌شود و همزه در نگاشت عامیانه می‌افتد، از این‌رو صورت دوم «مایده». معین همین را دارد: «مائده: [ع. مائدة: ف. مایده] (ا.) خوردنی؛ خوانی که بر آن طعام باشد»، که هم سوی وام‌گیری را تأیید می‌کند و هم منبعِ صورتِ دومِ نورایی است. تنها نکته اینکه چون خودِ واژهٔ عربی از حبشی گرفته شده (گرهٔ ۴)، اینجا با دورهٔ «فارسی → عربی → فارسی» روبرو نیستیم، بلکه وام‌گیری یک‌سویه از عربی است.\",\n     \"sources\": [W_MAIDA],\n     \"ref_check\": [\n      {\"ref\": \"MON:3674\", \"status\": \"supports\",\n       \"note\": \"The page number cannot be mapped in the local OCR, but Mo'in's entry is unambiguous — MON_part2.txt line 41631: 'مائده: [ع. مائدة: ف. مایده] (ا.) خوردنی. خوانی که بر آن طعام باشد … مائدهٔ مسیح: روایت کنند که تا مدتی هر روز به وسیلهٔ ابر خوانی بر عیسی(ع) نازل می‌شد' — both the Arabic origin tag and the مایده variant that the JSON records as script_extra.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. مائده (MON_part2.txt line 41631)\", \"stance\": \"supports\",\n       \"note\": \"'[ع. مائدة: ف. مایده]' — Arabic loan, Persianised spelling مایده.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 255-256\", \"stance\": \"partial\",\n       \"note\": \"Confirms that the Arabic word is the Qurʾanic one (Q v, 112, 114) which Persian then borrowed back in its religious sense, while denying that Arabic got it from Persian in the first place.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā — no مائده entry (grep of ARY_pages.txt silent)\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur only treats Indo-European material, so an Arabic loan is out of scope.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Latin\",\n     \"words\": \"mitis\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin mītis, -e 'mild, soft, mellow (of fruit), gentle (of persons)' is attested from Plautus and Virgil on ('sunt nobis mitia poma', Ecl. 1.81) and is the standard Latin member of this root: Pokorny 712 'Mit t-Formantien lat. mītis „mild, gelind“ … (*meit-)', with Old Irish moith/moeth, Welsh mwydo 'to soften', mwydion 'soft parts'; Watkins reconstructs 'suffixed zero-grade *mi-ti- (< *mis-ti-)', Klein 'prob. stands for *mi-tis … fr. I.-E. base *mei-, *mi-', and de Vaan (via Etymonline and Wiktionary) *mh₁i-ti-, with Skt. máyas- 'refreshment' as the closest semantic parallel — i.e. the same es-/ti-stem play as in the Avestan branch of this chart. Wiktionary's caution ('of unclear origin, with multiple competing theories') concerns only the exact suffixal shape and the rival Hittite/prohibitive-particle proposals of Oettinger and Plötz, not the *meyh₁- 'mild' etymology, which it calls the prevailing one. Nourai's gloss 'soft' and his language label are right; AHD:1528 is a page of the 1975 New College appendix, whose M section falls in exactly that range.\",\n     \"derivation_fa\": \"واژهٔ لاتینی mītis «نرم، ملایم، رسیده (میوه)» از پلاوتوس و ورگیل به بعد گواهی دارد و نمایندهٔ اصلی این ریشه در لاتینی است: پوکورنی (ص ۷۱۲) آن را با پسوند t- و از *meit- می‌گیرد (همراه ایرلندی کهن moith و ولزی mwydion)، واتکینز صورت صفرِ *mi-ti- و دِ فان *mh₁i-ti- می‌سازند و کلاین نیز آن را به همین ریشهٔ *mei-/*mi- «نرم، ملایم» باز می‌گرداند؛ نزدیک‌ترین موازی معنایی سنسکریت máyas- است، یعنی همان ستاکی که در شاخهٔ اوستایی همین نمودار کار کرده است. تردیدی که ویکی‌واژه مطرح می‌کند فقط بر سر شکل پسوند و فرضیه‌های رقیب (اوتینگر، پلوتس) است، نه بر سر خودِ ریشه. پس برچسب و معنای نورایی درست است.\",\n     \"sources\": [W_MITIS, E_MITIG],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1528\", \"status\": \"supports\",\n       \"note\": \"The cited 1975 New College appendix is not on open shelves, but its author's own standalone edition has the entry verbatim — AHD_watkins1985.txt line 734: 'mē(i)-. Mild. Contracted from *meəi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.]' The appendix runs pp. 1505-1550 and its M roots fall around pp. 1527-1530, so the page reference is consistent; the content certainly is.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny 712 (POK_full.txt line 60718)\", \"stance\": \"supports\",\n       \"note\": \"'Mit t-: Latin mītis „mild, soft“ (*meit-); Old Irish moith, moeth (*mōit-) ds. … cymr. mwydo (*meit-) „soften“'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. mitigate (KLN_1966.txt line 24059)\", \"stance\": \"supports\",\n       \"note\": \"'compounded of mitis, “soft, mild, gentle”, and agere … The first element prob. stands for *mi-tis and derives fr. I.-E. base *mei-, *mi-, “soft, mild, tender, gentle”'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 784 s.v. mitis (LAT.txt line 38366)\", \"stance\": \"supports\",\n       \"note\": \"'mitis, -e: doux, douce … Dérivés et composés: mītescō; mītigō … On rapproche gall. mwydion „parties molles“, iri. moith „mou, tendre“' — both the sense and the Celtic cognates of the root.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. meit- (1) / moitos (IEC.txt lines 10499, 11050)\", \"stance\": \"partial\",\n       \"note\": \"'Lat. mitis “gentle, soft, overripe”' filed under a t-extension lemma rather than under a root 'mild'.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"mitigate\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A textbook Latin→English learned borrowing, and the arrow from mitis is exactly right because the Latin verb is a compound of it: L. mītigāre 'to make soft or tender, to soothe' = mītis 'soft' + the reduced form of agere 'to drive, make' (the same -igāre as in levigāre, lītigāre, fumīgāre; Ernout-Meillet note the formation 'cf. pour la formation leuis/leuigo'). English mitigate appears in the early 15th century in the sense 'relieve (pain), make mild', formed on the past participle mītigātus (ME mitigaten), with the earlier noun mitigation borrowed through Old French; Klein and Skeat give the same derivation. Nourai's gloss 'soften, moderate' is accurate, and the node needs no reference of its own.\",\n     \"derivation_fa\": \"وام‌واژه‌ای کتابی از لاتینی به انگلیسی است و پیکان از mitis دقیقاً درست است، زیرا فعل لاتینی mītigāre «نرم کردن، فرونشاندن» خود مرکب از mītis و صورت کاهیدهٔ agere «راندن، کردن» است (همان ساختِ -igāre در levigāre و lītigāre). صورت انگلیسی در سدهٔ پانزدهم میلادی و بر پایهٔ صفت مفعولی mītigātus ساخته شده است (کلاین، اسکیت، اتیمولانلاین)؛ معنای «soften, moderate» در نمودار درست است.\",\n     \"sources\": [E_MITIG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book (refs=None); the chain was verified independently from Klein, Skeat and Etymonline.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. mitigate (KLN_1966.txt line 24059)\", \"stance\": \"supports\",\n       \"note\": \"'mitigate, tr. v., to alleviate. — ME. mitigaten, fr. L. mitigatus, pp. of mitigare, “to make soft or tender, to soothe, mitigate”, compounded of mitis … and agere.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mitigate (SKT.txt line 11726)\", \"stance\": \"supports\",\n       \"note\": \"'Mitigate. (L.) From pp. of L. mitigare, to make gentle. — L. mitis … -igare, for agere, to make.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1877)\", \"stance\": \"supports\",\n       \"note\": \"'MITIGATE mē(i)-' — the English word is filed under this very root.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Mei 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *mei- 'to fix, fasten; post, stake' (Pokorny 'mei-1', p. 709; Watkins 'mei-3. To fix; to build fences or fortifications')\",\n   \"note\": \"Root, label, gloss and page are all correct, and the gloss is almost word-for-word Watkins': POK_full.txt line 58259 ff. has 'Root / lemma: mei-1  Meaning: to strengthen; pole  Material: Old Indic minoti “fastens, founds, builds”, miti- f. “erection, foundation”, mita- “fastened”, metar- „der Aufrichter“, mayukha- m. “peg, plug, ray”, npers. mex “peg, plug, nail” (*maixa-), sogd. myyk ds. … Latin Pl. moenia “defensive walls, city walls”, munio (archaic moenio), -ire “to wall, fortify”; murus, old moiros “wall” … With t-extension me[i]t-: Old Indic methi- “pillar, jamb” … Latin meta … References: WP. II 239 f., WH. II 30 f.  Page(s): 709', and Watkins has 'mei-3. To fix; to build fences or fortifications … *moi-ni- in Latin munire, to fortify, protect, strengthen: MUNITION; (AMMUNITION) … [Pok. 1. mei- 709.]'. So both of Nourai's branches on this chart (Iranian mēx and Latin mūnīre) are drawn straight out of Pokorny's page 709, and his gloss 'to fix, build, fence' is Watkins' 'to fix; to build fences'. The only reservation, which belongs to the Indo-Iranian branch and not to the root box, is that Skt. mayūkha- (and with it OP mayūxa-, NP mīx) is today often taken out of the root and explained as a BMAC-substrate loanword.\",\n   \"note_fa\": \"ریشه، برچسب زبانی، معنی و شمارهٔ صفحه همه درست است. پوکورنی در ص ۷۰۹ مادهٔ mei-1 را با معنی «استوار کردن؛ تیر، میخ» می‌آورد و در همان مقاله هم سنسکریت minoti «استوار می‌کند، می‌سازد» و mayūkha- «میخ» و فارسی نو mēx (< *maixa-) و سغدی myyk را دارد و هم لاتینی moenia و mūnio/mūnīre و mūrus را؛ واتکینز نیز عیناً «to fix; to build fences or fortifications» می‌نویسد که تعبیر نورایی ترجمهٔ همان است. پس هر دو شاخهٔ این نمودار (میخ و mūnīre) راست از صفحهٔ ۷۰۹ پوکورنی برگرفته شده است. تنها احتیاط آنکه امروز برخی mayūkha- سنسکریت (و به تبع آن میخ فارسی) را وام‌واژه‌ای از زیرلایهٔ باکتریا–مرو (BMAC) می‌دانند و از این ریشه جدا می‌کنند.\",\n   \"sources\": [W_MIX],\n   \"ref_check\": [\n    {\"ref\": \"POK:709\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 58259 ff.: 'Root / lemma: mei-1  Meaning: to strengthen; pole … npers. mex “peg, plug, nail” (*maixa-), sogd. myyk … Latin moenia … munio (archaic moenio), -ire “to wall, fortify”; murus, old moiros “wall” … Page(s): 709'. Both branches of the chart and even Nourai's Old Persian form *maixa- come from this page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 239-240 (WLD_Bd2_pages.txt leaves 243-244, headers '239' and '240')\", \"stance\": \"supports\",\n     \"note\": \"The article 'mei-' whose p. 240 has 'moenia „Umwallung, Stadtmauern“ („*Umpfahlung“), mūnio (moenio) … maide „Stange“, māidīt „bestecken, bepfahlen“' — i.e. WP. II 239 f., the reference Pokorny gives for page 709.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mei-3 (AHD_watkins1985.txt line 734)\", \"stance\": \"supports\",\n     \"note\": \"'mei-3. To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in … Latin murus, wall … 2. Suffixed o-grade form *moi-ni- in Latin munire, to fortify, protect, strengthen: MUNITION; (AMMUNITION), PRAEMUNIRE, PREMUNITION. [Pok. 1. mei- 709.]' — Nourai's gloss is this wording, condensed.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 7.28 'Wall' (SYN.txt lines 11882-11889) and 19.35 (line 32949)\", \"stance\": \"supports\",\n     \"note\": \"'2. Lat. mūrus (early moerus) and moenia (pl.) : Skt. mī- “fix, build”, etc. Walde-P. 2.239 f.' — Buck states the root's meaning in the same words Nourai uses.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. moiros (?) (IEC.txt line 11042)\", \"stance\": \"partial\",\n     \"note\": \"'moiros (?) (Evidence ambig.) OLat. & Lat. moerus, mūrus … “wall”; pro-moerium “boundary wall”; W mur, adj. “fixed, firm”' — the Latin family, but Mann files it as an isolated noun lemma and marks the reconstruction doubtful.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Old Persian\",\n     \"words\": \"maixa : nail ; mayūxa : door knob\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The second form is genuine attested Old Persian, the first is a reconstruction wearing an Old Persian label. mayūxa- is read on two trilingual inscriptions on lapis-lazuli door-knobs, DPi and XPi: Kent's lexicon (p. 202) has 'mayūxa- sb. “doorknob”: Skt. mayūkha- “peg”, perhaps to Skt. mi- (pres. minóti) “fix (as in the earth)” … mayūxa nsm. DPi; XPi', and his text of DPi reads 'mayūxa : kasakaina : Dārayavahauš : Xšāyaθiyā : viq̋iyā : karta — Door-knob of precious stone, made in the house of Darius the King'. So the gloss 'door knob' is Kent's own and the page reference is exact. 'maixa', by contrast, is nowhere attested in the inscriptions: it is the Proto-Iranian pre-form of New Persian mēx that Pokorny 709 sets up ('npers. mex “peg, nail” (*maixa-)'), and Aryanpur's Persian etymological dictionary labels it the same way as Nourai does ('*MAIXA (OLD PERSIAN)' in the same entry as 'MEX (PAHLAVI)', ARY_latin_index_pages.txt line 14184). Whether mēx descends from mayūxa- itself (by contraction of -ayū- > -ē-, so Nyberg and Wiktionary) or from a parallel *maixa- (so Pokorny, Aryanpur) is an open question, and Nourai has simply put both forms in one box. The deeper reservation is that the tie to the root is not secure: Kent says only 'perhaps', Horn (no. 1005) marks the comparison with Skt. mayūkha- with a question mark and reports Nöldeke's rival proposal (np. mēx direct to Skt. sumeka-, which would make all other Iranian forms loanwords), and Lubotsky's substrate work, followed by Wiktionary, now derives PII *mayū́kʰas 'peg, nail' from the BMAC substrate, i.e. not from PIE *mei- at all.\",\n     \"derivation_fa\": \"صورت دوم پارسی باستانِ گواهی‌شده است و صورت نخست بازساخته‌ای با برچسب پارسی باستان. mayūxa- در دو سنگ‌نوشتهٔ سه‌زبانهٔ DPi و XPi بر دستگیرهٔ درِ لاجوردین آمده و کنت (ص ۲۰۲) می‌نویسد: «mayūxa- «دستگیرهٔ در»: سنسکریت mayūkha- «میخ»، شاید وابسته به mi- (minóti) «استوار کردن»»؛ پس معنی و شمارهٔ صفحه درست است. اما maixa در کتیبه‌ها گواهی ندارد و صورتی است که پوکورنی (ص ۷۰۹) برای فارسی نو mēx فرض کرده است؛ فرهنگ ریشه‌های آریانپور نیز همانند نورایی آن را «*MAIXA (پارسی باستان)» می‌نامد. اینکه میخ از خود mayūxa- (با ادغام -ayū- > -ē-؛ نیبرگ و ویکی‌واژه) می‌آید یا از صورت موازی *maixa- (پوکورنی، آریانپور) هنوز گفتگو دارد و نورایی هر دو را در یک جعبه نشانده است. ایراد مهم‌تر آن که پیوند با ریشه قطعی نیست: کنت می‌گوید «شاید»، هرن (شمارهٔ ۱۰۰۵) مقایسه با mayūkha- را با علامت پرسش می‌آورد و رأی نولدکه را نقل می‌کند، و پژوهش امروزی (لوبوتسکی و ویکی‌واژه) *mayū́kʰas هندوایرانی را وام‌واژهٔ زیرلایهٔ BMAC می‌داند، نه از ریشهٔ *mei-.\",\n     \"sources\": [W_MIX],\n     \"ref_check\": [\n      {\"ref\": \"KNT:202\", \"status\": \"supports\",\n       \"note\": \"KNT.txt leaf 226 (between the page headers '202' on leaf 225 and 'LEXICON 203' on leaf 227, i.e. printed p. 202): 'mayūxa- sb. “doorknob”: Skt. mayūkha- “peg”, perhaps to Skt. mi- (pres. minóti) “fix (as in the earth)” (§100, §148.II); cf. Hz. Apī 258-9. mayūxa nsm. DPi; XPi.' Kent's DPi text (line 4102) confirms the gloss.\"},\n      {\"ref\": \"BQT:2073\", \"status\": \"supports\",\n       \"note\": \"Fetched with tools/ref_page.py BQT:2073 (vol. 4 scan, pdf p. 156; cached at refs/ocr/BQT/2073.png/.txt). Mo'in's footnote 5 to میخ reads 'فی: پارسی باستان *mayūxa، آریایی *mayūkha، سانسکریت mayūkha (میخ چوبی) «هوبشمان»؛ لغات متعارف در لهجه‌ها: کردی mīx، افغانی mēx … استی، بلوچی …' — the Old Persian mayūxa → Persian mīx arrow, on the very page cited.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon p. 202 and DPi (p. 136)\", \"stance\": \"supports\",\n       \"note\": \"See the quotation; mayūxa- is attested only in DPi and XPi, both door-knob inscriptions.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p. 132 s.v. mex (NYB_vol2_glossary.txt line 2545) and the OP–Pahlavi list (line 4914)\", \"stance\": \"supports\",\n       \"note\": \"'mex [myh] … pole … NP mēx; connection with OP mayūxa- “doorknob” (Kent), Skr mayūkha- probable'; and the correspondence list 'mayūxa-: mēx'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (incoming/ARY/ARY_latin_index_pages.txt lines 14183-14192, entry printed after [pdf page 486])\", \"stance\": \"supports\",\n       \"note\": \"The میخ entry lists '*MAIXA (OLD PERSIAN) … MEX (PAHLAVI) … MIX, MEX (OSSETIC) … MYGHK (SOGHDIAN) … MAYOKHA (SANSKRIT) … MOENIA, MOENIUM (LATIN) … -TUIDMEN (OLD IRISH) … MARE (OLD ENGLISH)' with 'REFERENCES: POKORNY 709; MACKENZIE (NAIL) 124' — an independent modern Persian dictionary that uses the same Old Persian *maixa label as Nourai and the same Pokorny page.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW — no Avestan cognate of mēx is listed (grep silent)\", \"stance\": \"silent\",\n       \"note\": \"The word is not attested in Avestan, which is why the chart's Iranian branch has to start from Old Persian.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"mîx «میخ» : nail ; mîxak «میخک» : carnation\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"میخ mēx/mīx 'nail, peg' descends through Middle Persian mēx ⟨myh⟩ 'peg, nail' (MacKenzie, CPD p. 56; Nyberg II 132, who notes that the Book Pahlavi spelling ⟨myh⟩ was a crux because it coincides with ⟨MY?⟩), the Classical Persian reading being mēx, modern Iranian mīx after the regular raising of ē > ī; the same word is Sogdian myyk (Gharib no. 5615 'myyk B, mexe, cf. OP mayuxa, “spike, nail”'), Ossetic mix/mex, Kurdish mīx, Balochi meh, Pashto mēx — the dialect list Mo'in gives in Borhan p. 2073 n. 5. میخک mīxak is its diminutive in -ak, and the semantic step is the well-known one: the dried clove looks like a small nail (exactly as Latin clāvus 'nail' > French clou de girofle > English clove), so mīxak is first 'clove', and the flower called میخک (carnation, Dianthus) is named after the clove's scent; Nourai gives only the flower sense, which is right but incomplete. The arrow itself is uncontroversial — only the ultimate PIE attachment of the family is disputed (see node #1 and the root note).\",\n     \"derivation_fa\": \"«میخ» از فارسی میانهٔ mēx ⟨myh⟩ «میخ، گوه‌میخ» می‌آید (مکنزی ص ۵۶؛ نیبرگ ج ۲ ص ۱۳۲) و خوانش فارسی دری mēx است که در فارسی امروز ایران بر اثر تبدیل قاعده‌مندِ ē > ī به mīx بدل شده است؛ همین واژه در سغدی myyk (غریب، شمارهٔ ۵۶۱۵)، استی mix/mex، کردی mīx، بلوچی meh و پشتو mēx دیده می‌شود — همان فهرستی که معین در حاشیهٔ برهان قاطع (ص ۲۰۷۳) می‌آورد. «میخک» مصغر آن با پسوند -ک است و تحول معنایی آن شناخته است: غنچهٔ خشکیدهٔ قرنفل به میخی کوچک می‌ماند (درست مانند لاتینی clāvus «میخ» > فرانسه clou > انگلیسی clove) و گلِ میخک را به سبب بوی قرنفلی‌اش چنین نامیده‌اند؛ نورایی تنها معنی «گل» را آورده که درست ولی ناکامل است. خودِ پیکان پذیرفته است؛ تنها انتساب نهایی این خانواده به ریشهٔ هندواروپایی محل اختلاف است (بنگرید به گرهٔ ۱).\",\n     \"sources\": [W_MIX],\n     \"ref_check\": [\n      {\"ref\": \"POK:709\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 58263: 'npers. mex “peg, plug, nail” (*maixa-), sogd. myyk ds.' — Pokorny lists the New Persian word on the cited page, together with Skt. mayūkha- and the Latin members, so the node's single reference is right.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 56 (PHD_mackenzie.txt line 3551)\", \"stance\": \"supports\",\n       \"note\": \"'mex [myh | P myx, N -] peg, nail.' — the Middle Persian (and Manichaean myx) ancestor.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 1005, pp. 225-226 (HRN.txt line 8743)\", \"stance\": \"partial\",\n       \"note\": \"'1005. mex „Pflock, Nagel“. ai. vergl. mayūkha- „Pflock“ (?) … kurd. mix; afġ. mex, meyou „Nagel, Pflock“; oss. d. mex, t. mix „Pfahl“ … Nöldeke (mündliche Mitteilung) will np. mex direkt an ai. sumeka- anschliessen, dann müssten die Worte der anderen iranischen Sprachen sämmtlich Lehnworte sein.' Horn has the word and the dialect cognates but hesitates over the Sanskrit comparison.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qāteʿ p. 2073, Mo'in's footnote 5 (refs/ocr/BQT/2073.txt)\", \"stance\": \"supports\",\n       \"note\": \"'فی: پارسی باستان *mayūxa … سانسکریت mayūkha (میخ چوبی) «هوبشمان»' with the dialect list and, in the body of the page, 'میخ … معروف است' plus the derivative entries میخ درم/میخ دیناری 'coin die'.\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 5615 (SOD.txt line 45294)\", \"stance\": \"supports\",\n       \"note\": \"'5615 myyk B / mexe, cf. OP mayuxa / spike, nail / SCE 237' — the Sogdian cognate Pokorny also cites, confirming an Old Iranian, not a late, word.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II 132 s.v. mex (NYB_vol2_glossary.txt line 2545)\", \"stance\": \"supports\",\n       \"note\": \"'— NP mēx; connection with OP mayūxa- “doorknob” (Kent), Skr mayūkha- probable.'\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Latin\",\n     \"words\": \"mūnīre\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin mūnīre (archaic moenīre) 'to wall in, fortify, protect' is the denominative of moenia 'city walls, fortifications' — Ernout-Meillet s.v. moene, moenia: 'Dénominatif: mūnio, -īs, -īuī, -ītum, -īre: fortifier, munir', with the sound history spelled out there: the oe of moenia was kept in the technical term but developed regularly to ū in the derivatives ('mūniō, cf. poena, pūnio; Poenus, pūnicus'), while beside it stands mūrus, old moiros 'wall'. That puts the word on the o-grade *moi-ni- of the root, exactly as Watkins states ('Suffixed o-grade form *moi-ni- in Latin munire, to fortify, protect, strengthen'), and Pokorny 709 lists 'Latin Pl. moenia … munīo (archaic moenio), -īre “to wall, defend with a wall, fortify”' on the page Nourai cites for the root. Two small points: the citation form is mūnīre with a long ū (the printed page has 'mŭnîre', Nourai's font using a breve where a macron is meant, as also in 'mayŭxa' in the box above), and this Latin node carries the bare reference 'AHD' with no page — the entry is Watkins' mei-3.\",\n     \"derivation_fa\": \"لاتینی mūnīre (کهن moenīre) «دیوار کشیدن، استحکام بخشیدن» فعلِ برساخته از نامِ moenia «دیوارهای شهر، بارو» است؛ ارنو–مییه می‌نویسد: «Dénominatif: mūnio … fortifier, munir» و دگرگونی آوایی را نیز باز می‌گوید: oe در خود moenia به سبب فنی بودن واژه مانده ولی در مشتقات به‌قاعده به ū بدل شده (مانند poena/pūnio). پس این واژه بر پایهٔ درجهٔ o یعنی *moi-ni- از همین ریشه ساخته شده است — همان که واتکینز و پوکورنی (ص ۷۰۹) می‌گویند. دو نکتهٔ کوچک: صورت درست mūnīre با واو بلند است (در کتاب mŭnîre چاپ شده، زیرا نورایی برای کشیدگی نشانهٔ جیم کوتاه می‌گذارد، چنانکه در mayŭxa هم)؛ و این گره ارجاع AHD را بی‌شمارهٔ صفحه دارد که مقصود مادهٔ mei-3 واتکینز است.\",\n     \"sources\": [E_AMMO],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"No page given in the book; the entry is AHD_watkins1985.txt line 734: 'mei-3. To fix; to build fences or fortifications … 2. Suffixed o-grade form *moi-ni- in Latin munire, to fortify, protect, strengthen: MUNITION; (AMMUNITION), PRAEMUNIRE, PREMUNITION. [Pok. 1. mei- 709.]' — which also supplies node #4.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. moene, moenia (LAT.txt lines 38601-38625, printed pp. 740-741)\", \"stance\": \"supports\",\n       \"note\": \"'murus, ancien moiros, moerus, apparenté à la fois par la forme et par le sens … dans les dérivés elle a abouti régulièrement à u: mūniō, cf. poena, pūnio … Dénominatif: munio, -īs … -īre: fortifier, munir'.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny 709 (POK_full.txt line 58265)\", \"stance\": \"supports\",\n       \"note\": \"'Latin Pl. moenia „defensive walls, ramparts, bulwarks, city walls“, munio (archaic moenio), -ire „to wall, defend with a wall, fortify“; murus, old moiros „wall“'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. munition and premunition (KLN_1966.txt lines 24676, 30101)\", \"stance\": \"supports\",\n       \"note\": \"'munition … fr. L. munitionem, acc. of mūnitiō, “fortification, defense”, fr. munitus, pp. of munire'; 'munire, “to fortify, protect”'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 7.28 (SYN.txt line 11889)\", \"stance\": \"supports\",\n       \"note\": \"'Lat. mūrus (early moerus) and moenia (pl.) : Skt. mī- “fix, build”' — the same root attachment for the Latin group.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"ammunition\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Right chain, with one refinement: English took the word not from the verb mūnīre directly but from its noun mūnītiō 'a fortifying', through French, and with a famous mis-division. Etymonline: 'ammunition (n.) 1620s, “military stores and provisions,” from French soldiers' faulty separation of French la munition, as if *l'amunition; from Latin munitionem (nominative munitio) “a fortifying” … The error was corrected in French (Modern French munition), but retained in English, with the unetymological double -m- spelling to conform to words in Latin. At first it meant all military supplies in general; in modern use it means only material used in the discharge of firearms and ordnance.' Klein and Skeat say the same ('F. amunition, a dialectal form for munition … arose through a misdivision of la munition into l'amunition'), and Watkins files AMMUNITION under mei-3, exactly where the chart puts it. The semantic route is 'fortification work' → 'military stores' → 'powder and shot'.\",\n     \"derivation_fa\": \"زنجیره درست است، با یک دقیق‌سازی: انگلیسی این واژه را نه مستقیماً از فعل mūnīre بلکه از نامِ mūnītiō «استحکام‌بخشی» و از راه فرانسه گرفته است، و آن هم با یک برشِ نادرستِ مشهور: سربازان فرانسه la munition را l'amunition شنیدند و از دههٔ ۱۶۲۰ میلادی صورت amunition به انگلیسی راه یافت؛ در فرانسه بعدها درست شد (munition) ولی در انگلیسی ماند و املای دو-میمی هم قیاسی است (کلاین، اسکیت، اتیمولانلاین). تحول معنایی: «کارِ استحکامات» ← «ساز و برگ جنگی» ← «مهمات». واتکینز نیز AMMUNITION را زیر مادهٔ mei-3 می‌آورد، درست همانجا که نمودار گذاشته است.\",\n     \"sources\": [E_AMMO],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference in the book (refs=None); verified from Etymonline, Klein, Skeat and Watkins' index instead.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. ammunition (KLN_1966.txt line 2494)\", \"stance\": \"supports\",\n       \"note\": \"'ammunition, n. — F. amunition, a dialectal form for munition (see munition). Amunition arose through a misdivision of la munition into l'amunition.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. ammunition (SKT.txt line 12032)\", \"stance\": \"supports\",\n       \"note\": \"'ammunition, store for defence. (F. – L.) From O.F. amunition, a soldiers' corruption, due to putting l'amunition for [la munition]'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1239)\", \"stance\": \"supports\",\n       \"note\": \"'AMMUNITION mei-3' — the English word filed under the root of this chart.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-326.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-326.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 326",
 "description": "Write and validate verification file"
}
```


### [2026-09-07T16:11:48.617Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 3, 'contradicts': 1, 'not_checked': 2}
books consulted: {'supports': 31, 'silent': 5, 'partial': 4, 'contradicts': 2} | by book: {'HRN': 4, 'KLN': 4, 'PHD': 3, 'NYB': 3, 'MON': 3, 'BRT': 2, 'HUB': 2, 'FVQ': 2, 'ARY': 2, 'POK': 2, 'LAT': 2, 'SKT': 2, 'AHD': 2, 'WLD': 1, 'AFA': 1, 'PLA': 1, 'LKT': 1, 'IEC': 1, 'KNT': 1, 'BQT': 1, 'SOD': 1, 'SYN': 1}
```


## [2026-09-07T16:12:05.739Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport io\np='data/verification/page-326.json'\ns=io.open(p,encoding='utf-8').read()\nfixes=[(\"*meyẖ₁-\",\"*meyh₁-\"),(\"zaoq̊ra-\",\"zaoθra-\"),(\"viq̋iyā\",\"viθiyā\"),(\"حسین کازم قدری\",\"حسین کاظم قدری\"),(\"gelınde\",\"gelinde\"),(\"myzdpʾḇn\",\"myzdpʾn\"),(\"ሙእድ (maʾadd\",\"ማእድ (maʾədd\"),(\"myazda-/zaoθra-\",\"myazda- / zaoθra-\")]\nfor a,b in fixes:\n    n=s.count(a); s=s.replace(a,b); print(n,a,'->',b)\nio.open(p,'w',encoding='utf-8').write(s)\nPYEOF\npython3 -m json.tool data/verification/page-326.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 326 | tail -3",
 "description": "Fix transliteration typos"
}
```


### [2026-09-07T16:12:07.154Z] TOOL RESULT

```
0 *meyẖ₁- -> *meyh₁-
4 zaoq̊ra- -> zaoθra-
1 viq̋iyā -> viθiyā
1 حسین کازم قدری -> حسین کاظم قدری
2 gelınde -> gelinde
0 myzdpʾḇn -> myzdpʾn
1 ሙእድ (maʾadd -> ማእድ (maʾədd
2 myazda-/zaoθra- -> myazda- / zaoθra-
JSON OK
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 3, 'contradicts': 1, 'not_checked': 2}
books consulted: {'supports': 31, 'silent': 5, 'partial': 4, 'contradicts': 2} | by book: {'HRN': 4, 'KLN': 4, 'PHD': 3, 'NYB': 3, 'MON': 3, 'BRT': 2, 'HUB': 2, 'FVQ': 2, 'ARY': 2, 'POK': 2, 'LAT': 2, 'SKT': 2, 'AHD': 2, 'WLD': 1, 'AFA': 1, 'PLA': 1, 'LKT': 1, 'IEC': 1, 'KNT': 1, 'BQT': 1, 'SOD': 1, 'SYN': 1}
```


## [2026-09-07T16:12:11.300Z] TOOL CALL #68: Bash

```json
{
 "command": "grep -o '\"\\*meyẖ₁-\\|meyh₁' data/verification/page-326.json | head -3; grep -c \"myzdpʾn\" data/verification/page-326.json; python3 tools/verify_check.py 326 | head -3",
 "description": "Verify fixes and no problems"
}
```


### [2026-09-07T16:12:12.682Z] TOOL RESULT

```
meyh₁
meyh₁
meyh₁
0
nodes verified: 11/11
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
```


## [2026-09-07T16:12:17.591Z] TOOL CALL #69: Bash

```json
{
 "command": "grep -o \"myzd[^ ]*\" data/verification/page-326.json | sort -u",
 "description": "Check MP spelling string"
}
```


### [2026-09-07T16:12:17.633Z] TOOL RESULT

```
myzd
myzd⟩
myzd⟩),
myzd⟩;
myzdpʾḇn⟩
```


## [2026-09-07T16:12:24.749Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport io,re\np='data/verification/page-326.json'\ns=io.open(p,encoding='utf-8').read()\ns2=re.sub(r\"myzdpʾ[^⟩]*n⟩\", \"myzdpʾn'⟩\", s)\nprint(s.count(\"myzdp\"), s2.count(\"myzdpʾn'⟩\"))\nio.open(p,'w',encoding='utf-8').write(s2)\nPYEOF\ngrep -o \"myzdp[^ ]*\" data/verification/page-326.json; python3 -m json.tool data/verification/page-326.json>/dev/null && python3 tools/verify_check.py 326 | head -2",
 "description": "Fix Book Pahlavi spelling"
}
```


### [2026-09-07T16:12:26.120Z] TOOL RESULT

```
2 2
myzdpʾn'⟩
myzdpʾn'⟩
nodes verified: 11/11
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 1}
```


## [2026-09-07T16:12:30.144Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/verify_check.py 326; echo \"exit=$?\"",
 "description": "Final verify_check run"
}
```


### [2026-09-07T16:12:31.563Z] TOOL RESULT

```
nodes verified: 11/11
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 3, 'contradicts': 1, 'not_checked': 2}
books consulted: {'supports': 31, 'silent': 5, 'partial': 4, 'contradicts': 2} | by book: {'HRN': 4, 'KLN': 4, 'PHD': 3, 'NYB': 3, 'MON': 3, 'BRT': 2, 'HUB': 2, 'FVQ': 2, 'ARY': 2, 'POK': 2, 'LAT': 2, 'SKT': 2, 'AHD': 2, 'WLD': 1, 'AFA': 1, 'PLA': 1, 'LKT': 1, 'IEC': 1, 'KNT': 1, 'BQT': 1, 'SOD': 1, 'SYN': 1}
exit=0
```


## [2026-09-07T16:12:50.322Z] AGENT

Page 326 (book p. 296) verified. `verify_check.py 326`: 11/11 nodes, exit 0, no PROBLEM lines.

**Counts** — roots: 2 confirmed (Megh redirect skipped). Nodes: 7 confirmed, 3 plausible, 1 disputed. Ref checks: 10 supports, 3 partial, 1 contradicts, 2 not_checked (nodes with `refs=None`).

**Disputed**
- Mei 1 #4, Arabic *mā'ida* «مائدة» ← Pahlavi *mayazd/māz*: modern consensus is a Geʿez loan (ማእድ *maʾədd* "table"). Nourai's own second reference refutes him — Jeffery FVQ 255–256 (= VDQ:370): "very difficult to derive māʾida from this [Phlv. myazd]"; Fraenkel p. 24 and Nöldeke, *Neue Beiträge* 54 for Ethiopic; Asbaghi's Persian-loans-in-Arabic does not list it. AFM:148 does argue Persian, but from میده "fine wheaten bread", not *mayazd*.

**Plausible (with reasons)**
- Mei 1 #1: root→Avestan arrow is exactly Pokorny 712 (*m(i)ies-dh(e)-*, Skt. *miyédha-* = Av. *myazda-*), but the attested form is *myazda-* not *mayazda-* (NP vocalisation back-projected), and *myazda-* is the solid food-offering, not "guests".
- Mei 1 #2: Pahlavi *myazd/mēzd* confirmed (MacKenzie p. 56, Horn 1007); "māz" is a ghost form — Praetorius' posited older pronunciation of NP *mēz*, rejected by Nöldeke.
- Mei 2 #1: *mayūxa-* is genuine attested OP (Kent p. 202, DPi/XPi door-knobs — page reference exact); "maixa" is a Proto-Iranian reconstruction with an OP label (so also Aryanpur), and Lubotsky/Wiktionary now treat PII *mayū́kʰas* as a BMAC substrate loan rather than from PIE *mei-.

**Extraction errors for the owner: none.** Two oddities are faithful to the printed page (checked against the rendered image, copied to `data/verification/sources/refs/ocr/BOOK/326.png`):
- The Avestan gloss really prints "guests" twice across a line break ("…of Zoroastrians, guests / guests invited to a meal") — the book's dittography.
- "mayŭxa" / "mŭnîre" carry a breve where a macron is meant; that is Nourai's font/typography, not a misread.

Fetched pages cached: `refs/ocr/BQT/2076.*` and `2073.*`; six web sources archived via `fetch_source.py` (Wiktionary میزبان / میخ / مائدة / mitis, Etymonline mitigate / ammunition).
