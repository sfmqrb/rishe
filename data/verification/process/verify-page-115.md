# Verification process log — verify-page-115


## [2026-09-05T17:48:56.897Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 115 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-115.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-115.json. Write /home/sfmqrb/git/rishe/data/verification/page-115.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 115` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:48:58.478Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:48:59.195Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:48:59.211Z] TOOL RESULT

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


## [2026-09-05T17:48:59.287Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-115.txt"
}
```


### [2026-09-05T17:48:59.300Z] TOOL RESULT

```
1	=== PDF page 115 (book page 85) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dekm : ten  (refs POK:191)  PART 2
4	#1 (parent #0) [Indo-European] refs=AHD | Dkm-tom, Kmtom : hundred
5	  #2 (parent #1) [Avestan] refs=POK:191, 192 | sata, satam : hundred ; dve-sate, duye-saite : two hundred ☞Dwo
6	    #3 (parent #2) [Sogdian] refs=SOD:147 | dwyst : two hundred
7	    #4 (parent #2) [Persian] refs=BQT | sad «صد» : hundred ; devîst «دویست» : two hundred
8	  #5 (parent #1) [Greek] refs=AHD | hektaton : hundred
9	    #6 (parent #5) [French] refs=None | hectare : a unit of area ☞As
10	      #7 (parent #6) [Persian] refs=MON:5159 | hectâr «هکتار» : hectare | extra: هکتولیتر ، هکتومتر
11	      #8 (parent #6) [English] refs=AHD:609 | hectare
12	    #9 (parent #5) [English] refs=None | hecto- : hundred
13	  #10 (parent #1) [Germanic] refs=AHD | hundan : hundred
14	    #11 (parent #10) [English] refs=None | hundred
15	  #12 (parent #1) [Latin] refs=AHD | centum, centenarium : hundred ; per-centum : by hundred
16	    #13 (parent #12) [French] refs=None | 
17	      #14 (parent #13) [Persian] refs=MON:1810 | sântîmetr «سانتیمتر» ; pŭrsântâž «پورسانتاژ»
18	      #15 (parent #13) [English] refs=AHD | centimeter
19	    #16 (parent #12) [English] refs=None | cent, century, percent, centenary, centennial
20	  #17 (parent #1) [Greek] refs=VDQ:352 | kentmnarion : of a hundred
21	    #18 (parent #17) [Aramaic] refs=VDQ:352 | 
22	      #19 (parent #18) [Arabic] refs=MON:2734 | qentâr : a unit (100 dinars) for measuring large amounts of jewelry.
23	        #20 (parent #19) [Persian] refs=MON:2734 | qentâr «قنطار (قناطیر)» : a measure or container of valuables
24	--- entry 1 ---
25	ROOT Deks -> redirect to Dek
26	
```


## [2026-09-05T17:49:03.185Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-115.json",
 "description": "Read source JSON for page 115"
}
```


### [2026-09-05T17:49:03.231Z] TOOL RESULT

```
{
  "pdf_page": 115,
  "book_page": 85,
  "entries": [
    {
      "root": {
        "name": "Dekm",
        "lang": "Indo-European",
        "refs": "POK:191",
        "gloss": "ten"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "AHD",
          "words": [
            {"translit": "Dkm-tom, Kmtom", "gloss": "hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:191, 192",
          "words": [
            {"translit": "sata, satam", "gloss": "hundred", "script": null},
            {"translit": "dve-sate, duye-saite", "gloss": "two hundred", "script": null, "see": ["Dwo"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Sogdian",
          "refs": "SOD:147",
          "words": [
            {"translit": "dwyst", "gloss": "two hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "sad", "gloss": "hundred", "script": "صد"},
            {"translit": "devîst", "gloss": "two hundred", "script": "دویست"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hektaton", "gloss": "hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "hectare", "gloss": "a unit of area", "script": null, "see": ["As"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:5159",
          "words": [
            {"translit": "hectâr", "gloss": "hectare", "script": "هکتار"}
          ],
          "script_extra": "هکتولیتر ، هکتومتر",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:609",
          "words": [
            {"translit": "hectare", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hecto-", "gloss": "hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hundan", "gloss": "hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hundred", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "centum, centenarium", "gloss": "hundred", "script": null},
            {"translit": "per-centum", "gloss": "by hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:1810",
          "words": [
            {"translit": "sântîmetr", "gloss": null, "script": "سانتیمتر"},
            {"translit": "pŭrsântâž", "gloss": null, "script": "پورسانتاژ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "centimeter", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cent, century, percent, centenary, centennial", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 1,
          "lang": "Greek",
          "refs": "VDQ:352",
          "words": [
            {"translit": "kentmnarion", "gloss": "of a hundred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Aramaic",
          "refs": "VDQ:352",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Arabic",
          "refs": "MON:2734",
          "words": [
            {"translit": "qentâr", "gloss": "a unit (100 dinars) for measuring large amounts of jewelry.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Persian",
          "refs": "MON:2734",
          "words": [
            {"translit": "qentâr", "gloss": "a measure or container of valuables", "script": "قنطار (قناطیر)"}
          ],
          "note": null,
          "quote": {
            "text": "از زرد و سرخ مرد بنفریبد - نار است صرّهٔ وی و قنطارش",
            "poet": "Nâser-Khosrow"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Deks",
        "redirect": "Dek"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T17:49:03.400Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:49:03.436Z] TOOL RESULT

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


## [2026-09-05T17:49:08.801Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/*.json | head -50 && echo \"---\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['VDQ','SOD','MON','BQT','POK','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-05T17:49:08.832Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p data/verification/page-114.json 2>/dev/null || ls data/verification/ | head -40"
}
```


### [2026-09-05T17:49:10.463Z] TOOL RESULT

```
data/verification/page-100.json
data/verification/page-101.json
data/verification/page-102.json
data/verification/page-103.json
data/verification/page-104.json
data/verification/page-105.json
data/verification/page-106.json
data/verification/page-107.json
data/verification/page-108.json
data/verification/page-109.json
data/verification/page-110.json
data/verification/page-111.json
data/verification/page-112.json
data/verification/page-126.json
data/verification/page-311.json
data/verification/page-31.json
data/verification/page-32.json
data/verification/page-33.json
data/verification/page-345.json
data/verification/page-34.json
data/verification/page-35.json
data/verification/page-36.json
data/verification/page-37.json
data/verification/page-38.json
data/verification/page-39.json
data/verification/page-40.json
data/verification/page-41.json
data/verification/page-42.json
data/verification/page-43.json
data/verification/page-44.json
data/verification/page-45.json
data/verification/page-46.json
data/verification/page-47.json
data/verification/page-48.json
data/verification/page-49.json
data/verification/page-50.json
data/verification/page-51.json
data/verification/page-52.json
data/verification/page-53.json
data/verification/page-54.json
data/verification/page-55.json
data/verification/page-56.json
data/verification/page-57.json
data/verification/page-58.json
data/verification/page-59.json
data/verification/page-60.json
data/verification/page-61.json
data/verification/page-62.json
data/verification/page-63.json
data/verification/page-64.json
---
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


### [2026-09-05T17:49:10.519Z] TOOL RESULT

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
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
```


## [2026-09-05T17:49:13.609Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-05T17:49:13.643Z] TOOL RESULT

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


## [2026-09-05T17:49:36.151Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 191/192 (deḱm̥) ===\"\ngrep -n \"deḱm\\|dekm\\|deḱu\\|zehn\" POK_01.txt | head -30\necho \"=== POK ḱm̥tom ===\"\ngrep -n \"ḱm̥tóm\\|km̥tóm\\|ḱm̥tom\\|kmtom\\|hundert\" POK_01.txt | head -30"
}
```


### [2026-09-05T17:49:36.219Z] TOOL RESULT

```
=== POK 191/192 (deḱm̥) ===
2749:dektn,  dekm-t,  deku-  ,zehn',  Ordinale  dekeino-s,  dekmto-s.
2750:Ai.  ddsa^  av.  dasa;  arm.  tasn  (nach  Meillet  Esquisse  42  aus  *djc-j. wie  russ.  (tri)dcath  ,S0'  aus  (tri-)dbseti),  gr.  öixa,  lat.  decem  {denl  ,je  zehn^ aus  *dek-noi]  PN  Decius  =  osk.  Dekis,  Gen.  Dekkieis),  osk.  deketasiüi, Nom.  PI.  degetasiüs  ,curatores  decimarum^  (*deken-täsio-),  umbr.  desen-{duf) ,duo-decim^,  air.  deich,  cymr.  deg,  corn.  bret.  dek,  got.  taihun  {-n  wie  in sihun,  niun),  an.  tiu,  ags.  tien,  tyn,  as.  tehan,  ahd.  zehan  {a  wohl  aus  den Kompositis,  Brugmann  II  2,  18),  toch.  A  säk,  B  &ak-^  finn.  deksan  ,10^ ist  nach  Jokl  Pr.  ling.  Baudouin  de  Courtenay  104  aus  dem  Idg.  entlehnt).
2751:Auf  das  Zahlsubstantiv  dekm-t(i),  eigentl.  , Dekade^,  gehen  zurück:
2752:ai.  dasat-,  dasati-  f.  , Dekade',  alb.  djete,  gr.  ösxdg^  -adog  (zum  a  s.. Schwyzer  Gr.  Gr.  I  498,  597),  got.  tdihun-tehund  , hundert'  (eigentlich jZehn  Dekaden'),  anord.  tiund  f.  ds.,  apreuß.  dessimpts  ,zehn',  lit.  de- Hmt,  alt  deHmtis,  lett.  alt  desimt,  metath.  desmit,  alt  desmits  (vgl.  desmits^ m.  f.  , Zehner');  aksl.  desetb  (kons.  Stamm  auf  -t,  Meillet  Slave  comm.^  "^^8);
2753:deku-  wohl  in  lat.  decuria  , Zehntschaft'  (daraus  entlehnt  nhd.  Decher  m. ;Zehn  Stück';  spätlat.  *teguria  wii-d  durch  Schweiz.  Ziger  ,zehn  Pfund  Milch^ vorausgesetzt;  wohl  mit  mhd.  ziger  , Quark'  identisch)  =  umbr.  dequrier^ tekuries  ,decuriis,  Fest  der  Dekurien';  vgl.  osk.-umbr.  dekvia-  in  osk.  (via} Bekkviarim  ,(viam)  Decurialem',  umbr.  tekvias  ,decuvias';  dazu  wohl  germ..
2757:Ordinale  dekei^os  und  dekm-to-s:
3310:germ.  *tioi-na-  in  ahd.  zidnal,  zwenel  ,gemellus',  zwiniling  m.,  mhd. zwinüln  u.  , Zwilling',  *twai-na-  in  as.  twBne  ,zwei',  ahd.  zivene  ds.  (mit  e statt  ei  nach  *zwe  =  got.  twai,  das  es  ersetzt  hat),  ahd.  zwein-zug,  as. iwen-tig,  ags.  twen-tig  ,20'  (,Doppelzehn');  germ.  Hwiz-na-  in  anord.  tvennr, ivinnr  ,zweifach',  PL  tvenner  ,zwei  zusammengehörige'  (tvinna  ,verdoppeln'), ahd.  zwirnen,  -ön  ,zweifach  zusammendrehen',  mhd.  ziüirn^  mnd.  tioern ,doppelt  zusammengedrehter  Faden'  wohl  =  ags.  twlrij  holl.  twijn  , Zwirn, Leinen'  (ags.  getwinne  ,bini',  getwinnas  , Zwillinge'  ist  dann  auf  *twi-nja- zurückzuführen).  Daneben  auf  Grund  eines  *ticllia-j  idg.  '^dtiei-ko-,  got. ticeihnai  ,zwei',  ags.  Dat.  tweonum^  betweonum^  engl,  betiveen  ,z wischen';
=== POK ḱm̥tom ===
2752:ai.  dasat-,  dasati-  f.  , Dekade',  alb.  djete,  gr.  ösxdg^  -adog  (zum  a  s.. Schwyzer  Gr.  Gr.  I  498,  597),  got.  tdihun-tehund  , hundert'  (eigentlich jZehn  Dekaden'),  anord.  tiund  f.  ds.,  apreuß.  dessimpts  ,zehn',  lit.  de- Hmt,  alt  deHmtis,  lett.  alt  desimt,  metath.  desmit,  alt  desmits  (vgl.  desmits^ m.  f.  , Zehner');  aksl.  desetb  (kons.  Stamm  auf  -t,  Meillet  Slave  comm.^  "^^8);
2764:Hierher  kmtöm  ,hundert'  aus  *(d)lj:ß2^c5i22  ,(Zehner)dekade':
2766:gr.  £xaroV,   ark.  IxotcJv  (aus   dissimil.  *sem  kmtom.  ,ein   Hundert'? Schwyzer  Gr.  Gr.  I  592  f.),   ein  kürzeres   *xarov  in  *i;£TQd-y.aTOv  usw.  (ia ^eTQav.dtLoi  TstQay.ÖGLOi,  400',  ,400heitliche');
2767:lat.  centum   (dazu   ducentum,  ducentl  ,200',  vgl.  ai.  dvi-Satam  aus  *<^tfi kmtöm j  trecentl  ßOO%  quadringentl  ,400',  usw.;   centesimus  ,der  hundertste' nach  vicesimus,  trlcesimus   aus  *wei-,  *trl-kmt-t;nio-s)',
2769:got.  as.  ags.  hund,  ahd.  ÄitTicZ  ,100'  (in  Kompositis  von  200  ab),  aber an.  hund-rad  (zu  got.  rapian  ,zählen')  , Großhundert'  (,120'),  daraus  ags. hundred]  mhd.  nhd.  hundert  aus  as.  hunderod]
2773:Dazu  eine  r-Ableitung  in  lat.  centuria  f.  ,Hundertschaft'  (wie  decuria), au.  hundari,  ahd.  huntari  n.  , Hundertschaft,  Gau',  abg.  s^tor^ca  ds.,  lit. simteriöpas  ,hundertartig',  simt&j^-gis  ,hundertjährig'.
```


## [2026-09-05T17:49:37.567Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD dekm ===\"\ngrep -n -i \"dekm\\|kmtom\\|dekmtom\" AHD_watkins1985.txt | head -30\necho \"=== AHD hundam/hundred ===\"\ngrep -n -i \"hundam\\|hundan\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T17:49:37.759Z] TOOL RESULT

```
<persisted-output>
Output too large (37.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b7bx080tg.txt

Preview (first 2KB):
=== AHD dekm ===
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old En
...
</persisted-output>
```


## [2026-09-05T17:49:42.826Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^dekm\\|dekm\\.\\|dekm  *Ten\\|Ten\\.\" AHD_watkins1985.txt | head -20\necho \"--- context ---\"\ngrep -n \"dekm\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T17:49:42.882Z] TOOL RESULT

```
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
1169:wikmti. Twenty. Compound of wi-, in half, hence two, and *(d)kmt-i (nominative dual), decade, reduced zero-grade form of dekm. 1. Latin viginti, twenty: VICE- NARY, VIGESIMAL. 2. Greek eikosi, twenty: ICOSAHE- DRON. 3. Sanskrit vimsatih, twenty: PACHISI. [Pok. ui-kmt-i 1177.)
--- context ---
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
415:in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
555:gvou-. Ox, bull, cow. Nominative singular form *gvéu-s. 1. Germanic *kéuz (> *kiiz) in Old English ci, cy, cye, cow: COW], (KINE); COWSLIP. 2. Latin bds (stem bov-), ox, bull, cow: BEEF, BOVINE, BUGLE!; OvIBos. 3. Greek bous, ox, bull, cow: BOUSTROPHEDON, BUCEPHALUS, BUCOLIC, BULIMIA, BUPRESTID, BUTTER, (BUTYRIC). 4. Sanskrit go-, gauh, cow: GAYAL. 5. Suffixed form *gv6u-ro- in Sanskrit gaurah, wild ox: GAUR. 6. Zero-grade form *guw-d- in Greek hekatombé, “sacrifice of a hundred oxen” (hekaton, hundred; see dekm): HECATOMB. [Pok. gtou- 482.]
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
795:od-'. To smell. 1. Suffixed form *od-os- in Latin odor, smell: opor. 2. Suffixed form *od-é- in Latin olére, to smell (with J for d representing a Sabine borrowing): OLFACTORY, REDOLENT. 3. Suffixed form *od-yo- in Greek ozein, to smell: OZONE. 4. Suffixed form *od-md- in Greek osmé, smell: OSMATIC, OSMIUM; ANOSMIA. [Pok. 1. od- 72.] od-2. To hate. Latin édi, I hate, and odium, hatred: ANNOY, ENNUI, (NOISOME), ODIUM. [Pok. 2. od- 773.] 6g-. Fruit, berry. 1. Zero-grade form *ag- in Germanic *ak-ran- in Old English zcern, acorn: ACORN. 2. Latin iva (preform uncertain), grape: UVEA, UVULA; PYRUVIC ACID. [Pok. 6g- 773.] oid-. To swell. 1. Possibly Old English date, oat: oat. 2. Greek oidein, to swell: EDEMA. [Pok. oid- 774.] oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin dllus, any (see ne). [In Pok. e- 281.] oito-. An oath. Probably derived from ei-1. Germanic *aithaz in: a. Old English dth, oath: OATH; b. Old High German eid, oath, in German Eidgenosse, confederate: Hucuenor. [In Pok. 1. ei- 293.] okt6(u). Eight. 1. Germanic *ahté in: a. Old English eahta, eight: EIGHT; b. Old Norse ditjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octé, eight: OcTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek okt6, eight: OcTAD; ocTopus. [Pok. okt6 775.]
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
1087:teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
```


## [2026-09-05T17:49:44.939Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# count formfeeds up to line n\nfor target in (2749,2764,2766,2769):\n    idx=sum(len(l) for l in lines[:target-1])+target-1\n    leaf=t[:idx].count('\\f')\n    print(target,'leaf',leaf,'-> printed p',leaf-8)\nEOF"
}
```


### [2026-09-05T17:49:46.642Z] TOOL RESULT

```
2749 leaf 201 -> printed p 193
2764 leaf 202 -> printed p 194
2766 leaf 202 -> printed p 194
2769 leaf 202 -> printed p 194
```


## [2026-09-05T17:49:54.388Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2758,2780p' POK_01.txt"
}
```


### [2026-09-05T17:49:54.439Z] TOOL RESULT

```
dekeinO'S  in  ai.  da§amdhy  av.  dasdraa-,  osset.  däsäm]  lat.  decimus,  davo!
decumänus  ,zum  Zehnten  gehörig',  später   ,ansehnlich',  osk.  Dekm-anmii{
*Decumaniis^j  vgl.  auch  EN  DecumiuSj  daraus  entl.  etr.  tecumnalj  rilcy
latinisiert  Decumenus]  gall.  decametoSj  air.  dechmad,  mcjmr.  decvetj  coi
degves.
dekzn-to-s  in   gr.  cJexaTOg  (s.  auch  Schwjzer   Gr.  Gr.  I  595);   got.  i( liunda,  anord.  tmnda,  ahd.  zehanto,  zehendo,  ags.  teogeda-^  apreuß.  cZessim^ lit.   deHihtas,   lett.   desmitais,   älter   desimtais]   aksl.   deset^]    toch.  A  ^to B  skantej  ikaüce  (einzelsprachlich  arm.  tasn-erord,  alb.  i-dhjete);
Hierher  kmtöm  ,hundert'  aus  *(d)lj:ß2^c5i22  ,(Zehner)dekade':
ai.  satdm,  av.  satdm  (daraus  finn.  sa^a,  krimgot.  sadd)]
gr.  £xaroV,   ark.  IxotcJv  (aus   dissimil.  *sem  kmtom.  ,ein   Hundert'? Schwyzer  Gr.  Gr.  I  592  f.),   ein  kürzeres   *xarov  in  *i;£TQd-y.aTOv  usw.  (ia ^eTQav.dtLoi  TstQay.ÖGLOi,  400',  ,400heitliche');
lat.  centum   (dazu   ducentum,  ducentl  ,200',  vgl.  ai.  dvi-Satam  aus  *<^tfi kmtöm j  trecentl  ßOO%  quadringentl  ,400',  usw.;   centesimus  ,der  hundertste' nach  vicesimus,  trlcesimus   aus  *wei-,  *trl-kmt-t;nio-s)',
air.  ce<,  cymr.  can^,  bret.  kant,  com.  cans;
got.  as.  ags.  hund,  ahd.  ÄitTicZ  ,100'  (in  Kompositis  von  200  ab),  aber an.  hund-rad  (zu  got.  rapian  ,zählen')  , Großhundert'  (,120'),  daraus  ags. hundred]  mhd.  nhd.  hundert  aus  as.  hunderod]
lit.  HihtaSj  lett.  nmts]
aksl.  usw.  s^to  ist  kaum  iran.  Lw.  (Meillet  Slave  comm.^  63);
toch.  A  känt,  B  kante.
Dazu  eine  r-Ableitung  in  lat.  centuria  f.  ,Hundertschaft'  (wie  decuria), au.  hundari,  ahd.  huntari  n.  , Hundertschaft,  Gau',  abg.  s^tor^ca  ds.,  lit. simteriöpas  ,hundertartig',  simt&j^-gis  ,hundertjährig'.
WP.  I  785  f.,  WH.  I  200  f.,  327  ff.,  859,  Feist  150,  471  f.,  Trautmann -53,  305.
193
jß/.  ^zielen,  berechnen,  nachstellen^,  auch  ,listig  schädigen^  und  ^zählen, ^  erzählen^;    dolo-  , Abzielen,  (böse)  Absicht^
Vielleicht  arm.  tat  ,Linie,  Reihe^,  toiem  ,reihe  aneinander^;
.rr.  SöXog  ,List,  Köder^,  doXöcj  , überliste',  döXwv  ,kleiner  Dolch  der Meuchelmörder'  (über  öölwv  ,Segelstange'  s.  unter  3.  del-)]
aus  dem  Gr.  sind  entlehnt  lat.  dolus  ,List,  Täuschung',  dolö  ,Stock- (leo-en,  Stilett',  osk.  Akk.  dolom,  Abi.  dolud  ,dolus';
anord.  tal  n.  ,Rechnung,  Anzahl,  Rede'  (ags.  tcel  n.  ,Berechnung,  Reihe', gital  ,Zahl');  davon  an.  telja  ,(er)zählen',  ags.  tellan,  ahd.  zellen  (Fem.  anord. tala  ,Rede,  Zahl,  Rechnung'),  ags.  talu  ,Erzählung,  Reihe',  ahd.  zala Zahl,  Bericht'  (davon  an.  tala  ,reden',  ags.  talian  ,rechnen,  bedenken, erzählen',  ahd.  ^a^ön  , berechnen,  zählen,  zahlen');  ^-Erweiterung  in  engl. talk  ,reden';  vom  5-Stamm  *talaz-  n.  :  got.  talzian  ,belehren',  un-tals  ,un- '  gelehrig,  ungehorsam',  dazu  ags.  getcel  ,rasch,  schnell',  as.  gital  ahd.  gizal schnell';  mit  der  in  dolus  vorliegenden  Bedeutungsfärbung  dehnstufig ftnord.  täl  f.  ,Betrug,  Arglist',  ags.  t^l  f.  ,Tadel,  Verleumdung,  Spott',  ahd. säla  ,Nachstellung,  Gefahr',  zälön  ,wegreißen,  rauben';  schwundstufig  ags. tyllan  ,verlocken'  (*dln-).
```


## [2026-09-05T17:49:55.050Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT satəm / sata ===\"\ngrep -n \"sat\\?əm\\|satǝm\\|hundert\" BRT.txt | head -30"
}
```


### [2026-09-05T17:49:55.112Z] TOOL RESULT

```
=== BRT satəm / sata ===
2035:Für  völlig  wertlos  möchte  ich  allerdings  keines  der  genannten  Stücke  bezeichnen, nicht  einmal  das  jüngste  unter  ihnen,  das  aus  der  Mitte  des  19.(1)  Jahrhunderts stammt''.  Für  eine  Anzahl  lässt  es  sich  mit  Bestimmtheit  behaupten,  dass  ihre Verfasser  noch  Kenntnis  von  alten  Texten  gehabt  haben  müssen  —  sei  es  durch mündliche  Überlieferung,  sei  es  durch  Handschriften  — ,  die  heule  verschollen  sind. Und  für  die  übrigen  ist  eine  solche  Annahme  wenigstens  nicht  ganz  ausgeschlossen. Aus  diesem  Grunde  habe  ich  mich  auch  nicht  für  berechtigt  angesehen,  irgend einem  der  mir  bekannten  awestischen  Stücke  die  Aufnahme  ins  Wörterbuch  zu verweigern,  selbst  jenem  jüngsten  nicht,  so  nah  es  auch  gelegen  hätte.
10069:kommen,  (zeitlich)  voll  werden':  äat  yimäi xiairai  *'^risat5.%3ma  *ijnjaspnta's>  "aad dem  Reich  des  Y.  wurden  dreihundert Winter  voll"  V.  2. 8;  —  aü«  vlsp:>m  .7 ahmat  yat  hs  hanjasaili  (cäiirmum  yari) "(und)  so  bis  dahin,  dass  ihm  ein  Viertel- jahr voU  wird"  N,  42;  43.  4)  'angehen, sich  wenden  an  — '  (Akk.),  Med.;  t^m r^ra  hanjasante  * ma>ir3m.sp?nt3m.balsaz3m (sd.)  V.7.44.
10636:KompA.  —  El.?J)  —  Pü.  (zu  1);  xral  slarl*), Sü.  1  buddhija4a^,  buddhinaslah,  (zu  Y.  34.  g): ksudrajantui,  erl,:  duflasv.ipadai  pärvaliyah; (lu  l)  xta/sir  (Transskr.).  "  ')  daäiäücä  . . mafyäiirä  sind  attributiv  gedacht.  —  'i  Wie solche  hundertweis  zu  erschlagen  als  verdienst- liches Werk  gilt;  s.  auch  j-rn/j/riJf a«-.  —  31  Die Zerlegung  in  V™/-(s.  i/r>/-)-t*s/ra-  (zum  ai. V.  arfmi)  ist  wenigstens  denkbar;  ^40,1//. — *)  Vgl.  dazu  DsT.  ZA.  r.  208:  "il  ne  serail pas  imposstble  que  ceUe  etymologie  füt  exacte et  quo  ihrajsira  soit  pour  khral\ii)stara,  d'oü "khtalkslaia,  *k/ira/slara".
10980:•  j.  x5va§.satö.-zyain-"  m.,  Pltir.  'sechs- hundert Winter':  aa$yimäi  xsakrai  *°zima (NP.)  *kmjas>nta  V.2.12.
11148:—  'tanrö  (Af.)  p>rmä  vf<>ärayvU  Yt.  z^. 44;  N.  6j,  /02;  —  '"iiwan  ayaranqmea Vd.//.  a)  -^tpJrff  als  a)Nfs':^ä/^J ^rafJ  .  .  "'^wärB . ,  pania  xsafha  saüänie V.  j6.8;  8.  ß)  An.S':  •%iiiärSsata  Stn.- saokanqm  "vierhundert  .."  V.  Ä 84;  6.21'.
14255:Zunächst  Volk sname ;  eis.  Bed.:  'hundert  Rin- der besitzend',  Komp.  1  *%ala-{%.sata-)  -\-igav-; ai.  iala,^av-  Adj,;  BtHU  IF.  13.  130  No.
14658:•  j.  ftri-sata-  Zw.  'dreihundert"':  bamrami vasträ  .  .  'satanam  bawranam  Yt.5.  139.
14666:•  j.  ^risatö.zyain-  m.,  Plur,  'dreihundert Winter':  aai  yimäi  xiährai  **vma  (NP.) *Afnjasmia  V.  2. 8.
14685:•  j.  ^►riS  Adv.  'dreimal':  dt/ /rasnälay^n malsmana  .  .  'ri/  . .  ca^rus  .  .  x/vai  V. 7.7s;  75'i  14^  JÄ43';  —  ■//'*  vayiibii *hakwit  vlpaititii  N.4;(?);  —  ntmast tl  .  .  'T/a/  (Sp.  593  m.)'>  parö  anyaU dämqn  Ny./.  i;  Y.  i^.  6;  —  -»V'  iatäU ha%a.H^anqm  "mit  dreimal  hundert  ,  ." V.4.  5.  a)  mit  Gen.  tcmp.3':  -iiät  .  . hamahe  ayqn  Vyt  41 ;  —  'ii' *yJn  (sd.) N.  i/.  a)  attrib.  beim  Nom.  act.:  ■■// frasnäiti  tanunam . .  'tl  frasrütti  gä^anam
14885:—  paoiryS  gairiS  AqtnJtisiat  .  .  'ti  äya z^mä  YX.ig.i;  /O.  98,  /J.97,  Y.9.IS.  V, 7,  54;  —  nasunqm  yä  'ti  aya  zimä  irJri- ^ar»  V.5. 4;  — '11  karJ*  pärst^  hyJ'  vtha- (id.)patiy3'^  . .  Bh.  J.  4;  2.  5  (ergänzt);  — tiyri/  ,  ,  afanvaia  'ti  niral  (Sp.  184  o.) Yt^.  38;  —  dasina  'ti  ahoanha  "auf  der rechten  Seile"  N.  65.  4)  mit  Abi.,  nur räumlich;  a)  auf  die  Frage  woher?:  mihr>m .  .  yS  vlspfm  aAsm  . ,  ädiiäiti  haraihyat 'ti  bar3tanhai  Ytio.  51.  b)  auf  die Frage  wo?:  dunmqn  hqmJiiitinli  *iisMndvat °ti  garsit  YtS.32;  —  yim  yazata  ahurS mazda  raoxinat  'ti  gara  nmana£  Yt /0. 1 2  3 ; 5.25,45.  s)  mit  Gen.,  nur  raumlich; a)  auf  die  Frage  woher?:  naKa  dunmqn (sd.)  uzjasaiti  Aaraihyd  'ti  iamayä  Yt 10.  50.  b)  auf  die  Frage  wo?r  ^dasimm J  va  gaonavatö  (sd.)  ^banstrvS  va  'ti vayhanaAe  N.  65;  —  zqm  .  .  yetiAa  'ti  . . apa  taünti  Yt  jj.  9  f. ;  i  o ;  — y^iihe  nmämm ..vüätfm  banzi'te  paiti  bar^aAi (Sp.Ba^ u.)  AaraiiyS  'tt  banxayä  Y. 57.21;  19;  — ys .  .  Aaomq  utdasta  .  .  kara^yS  'ti  bar»- '  xayä  Ytio.  90.  c)  auf  die  Frage  wo- hin?: aurvantim  %wä  .  .  bcrjS  nida'iat .  . Aarai^yS  'ti  banzaya  Y.SO.  10.  6)  mit Dat(?)"'',  räumlich  auf  die  Frage  wo?: tarn  yazata  auf  .  .  daAakS  bawrsii  'ti daiiihaove  Yt.  5.  29.  3)  zum  Ausdruck des  Gleichkoromens,  Aufwiegens;  mit  Akk. 'gleichwertig  mit  — ',  bei  Ellipse  des  Verbums {'ah-):  ha  ml  baya  .  .  satam  'ti  anyaisqm ra^wqm  gä^anqm  "dieses  Stück  .  .  wiegt hundert  andre,,  auf  Y./^.S"';  15.  A)bes. zur  Angabe  dessen,  was  als  Preis  oder  Lohn geboten  oder  verlangt  wird,  'gegen,  um, für';  i)  mit  Akk.:  uzbasaui  'ti  ammxtttn (sd.) /rarazaite  miirS  Yt  10. 1 24.  a)  mit Lok.:  yehyS  .  .  vaAistptn  yesng  'ti  vaidä (sd.)   mazda  Y,  57.  2a;   27.15,  Vr.  16I3;
14960:dem  Aweslft  nicht  hervor.  Die  Frage,  ob  der Tote,  wenn  er  lum  Daxma  gebracht  wird,  einen P.  anhaben  solle  oder  nicht,  bildete  in  Anfang de*  l8.  JaliThunderts  den  Kernpunkt  religiöser Zwistigk eilen.  Jetit  soll  die  durch  Vd.  ver- tretene Sitte  nur  noch  in  Guiarat  vorkommen; vgl.  DsT.  ZA.  I.  XU,  Bahadur  B.  B.  Patel CamiMem.  VoL  175.  —  **)  Nach  V. /J.  2  PüErl. ist  ei  von  beliebigen)  Stoff  und  ivrei  Finger breit.
15095:•  j.  paiti-ätäna-,  "stana-**  n.  i)  'Stand- ort, \V'ohnstätte':  h5  imqm  dalnam  .  ./ra- pinaoiti  sattm  *°i'tananqm{G?.)''' hazannm faiti.daranqm  "der  bringt  diese  Religion zum  Gedeihen,  hundert  (neue)  Wohnstätten, tausend  (neue)  Aufentlialtsorte  (sinds  die er  ihr  schafft)"  V.^.3i)>.  2)  '(Gestell sva.)  Bein',  vom  Fuss  bis  zur  Hüfte:  'stäna F.Jg;  —  maihySi  'slUne  xräidisme  maiöyöi nars  vandusme  "bis  zur  Mitte  des  Beins (der  Beinhöhe)  in  hartem,  bis  zur  (Leibes)- mitte  eines  Mannes  in  weichem  Erdboden" V,Ä8;  *H.86.
15815:•  j.  *parsa-''  m.  'Getreideähre,  Ähre': mqnay^n  ahe  yaä^a  nä  sai?mca  hazar?r»mca ,  .  'l'anqm'^  *nijat3irt  hyat  ".  .  als  ob  ein Mann  auf  hundert  und  tausend  . .  Ähren einschlüge"  Yt. /j.  71''.
16685:'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
17346:ra/WOT    hundert  ..   doppelt  so  oft  . .     V.  iid;..a,6ai.f  ;.;.-,.-m..n.'Je5pensrTetEl;chen
18656:•  j.  nava.satö.-zyam-  m.  Flur,  'neun- hundert Winter' :  äat yimili  xsa%r3i  *'!Pma (NP.)  ''hnjassttta  V.2. 16.
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
21440:yas3  ('wie  sva.  womit')  hwä  yazata vTstäsps  Yt77.  61;  61,  5.90,  91,  /5- 54, V.  75.  17,  Vyt.20,  3/;  — ka%a  zaota  xsäta apB ..yazäile  Y.ö^.g;  —  tim  yazät surunvata  yasna  sraol»m  . .  zaokrabyB  (DP. statt  IP.)  Y.57.  3;  Yt.>  18,  70.  31 ;  —  yö aHm  yjzäite  zaohräbyB  Yt/7.  2;  2,  8.\, 10.6,  Y.68.10;  —  yatal^a  mqm  zara- ^uära  ..  zaokrräbyS  Yt  /.  9 ;  mangelhaft  zitirt F.4g; — hvanx^aitim ..yazamaide  haomays gava  barismana  .  ,  zaohrabyasca  arsux- öaäbyasca  vayzibyS  (DP.  statt  IP.)  Ny.  7. 1 6 ; —  yazayania  %wqm  mazdayasna  pasubya staoraHbya  vayalibya  pataraialibya  (sd.)  Yt 10. 1  \(j;—ultaiaiiya  (LS.  statt \%.)ca  vTspnn asavamm  .  .yazamaide  Vr.  18, 2.  b)  Akk.; tarn  yazata  kaolyaahü . .  sat)m  aspanqm  . . hazaisr)m  gavqm  "ihr  opferte  ff. . .  hundert Rosse, .."  Yt. 5.  21;  p.  ag;  —  tarn  yaztnta .  .  hunavB  .  .  sat>m  aspanqm  Yt  5.  57; 72.  c)  paiti  mit  Gen.(?);  yqm  yazata zara'huitrS  humatahe  paiti  mananhS  Yt 16.  6.  2)  mit  Angabe  des  wozu?  durch
25788:I  j.  'saena-  m.  EN.  eines  GIäiibigen*>: 'nahe  ahüm.jtütB  asaons . .  yH  paoiryS  saiB.- aghryS  fraxstata  paiti  aya  ama  "des  S., Sohns  des  A.  . .,  der  zuerst  mit  hundert SchUlem  auftrat  . ."  YLy.97;  —  HyrSis ■nahe  "des  Z.,  Sohns  des  S."  Yt.ij.  126. *)  Der  vom  loo.  bis  zum  200.  Jahr  der  lora- %»?/rischen  Religion  gelebt  haben  soll;  s.  DkB. '97  iS-  2.17).  West  SEE.  37.  230,  262,  47.  83.
25911:•  j.  sata-  (,  p.  %ata-)  neutr.  Zw.  'hundert'; Aisttnti  .  .  yazatäighö  °t)mca  hasaririmca Yt  6.  I ;  —  nsit  'hm  jatnti  .  .  öim  jainti Yt/4-37'  *)  ii^it  Gen.:  anya  dva  va nara  . .  pan^a  vä  pancäsatim  vä  •t?» *Aqm.n3irinqm  (näml  naram)  V. 5.  27;  — 't^m  atr>.saokanqTn  V.ÄS;;  ig.22,  VyLJ_jj
25912:—  'tun  iayalanqm  YtiO,  2;  —  -Dm paitiitanam  hatargrim  . .  baivari  V.j.31; Yt5.2i.'5.3,  ;j.7i,  H.j.s,  sVar„8,  Yt, ig.d;  —  %rii 'tat! käta.H%anqm  "mit  drei mal  hundert . ."  V.4.  5;  Wytig.  a)  mit attrib.  Einerzahlen":  ca'^warasca . . garays cahwarpsat3m(sd.)ia  dvaica  °ite  (ND.) dvaica  hazanre  Ytjp.  7;  —  %räyS  *°la (NP.)  F.  2j;  —  yä  ..  vazinH  xsvas  *°tais'' (ab  Nom.)  haxarfnnila  Yt  5.  95;  — navaca  yaskS  navaitlsca  navaca  °ta  navaia hatatira  rtavasJs(,sd.ya  baevqn  V.  22,  z;  Yt. ^.?-  S9-  ^)  ™''  Gen.:  duye  °ite  kakyä- Ht  .  .  xrafstranqm  V.  16.  12;  4.  2i';  — tisrS  'ta  upätananqm  V.  4. 1 1 ;  1 1 ;  — ia%w3rS  'tu  äirpjaokanqm  V.<?.  84;  ff.  21';
25915:•  j.  8ata*}Tia-  n.,  Plur.  'hundert  Schläge': pamasaynSi  'fnäÜca . .  aAqx/taynäi/(sii.)ca V.7.  53.         DS.  als  Inf.  sbes.
25917:•  j.  sata-jnäi  Inf.  'hundert  zu  schla- gen': J*  hasat»rizynais?a  .  .  ahaxltaynnU-
25921:•  j.  sata-ßtäna-  Adj.  'mit  hundert  Buckeln besetzt':  vaenm  . .  'tum  satsJänm  Yt. 10. 96.
25922:•  j.  sata-yär-  n.  'Zeitraum  von  hun- dert Jahren':  upa  %wa  hixsaisa  .  .  'ysn ". .  auf  hundert  Jahre  . ."  Vyt.  4j.     Wert-
25925:•  j.  sata'vant- Adj.  (km. 'vaiii-)  'hundert enthaltend,  hundertfach':  'vaitinqm  Aatav- ravaitinqm  balvar»  baevaranqm  V.5.19 Gl.;  —  'vata  iatS.inta  (sd.)  ufavaia  titi.- vita  Yt.  2. 14;  wertlos.
25927:•  j.  aaS-yav-  Adj.  'hundert&chen  Halt habend';  'yus  (näml.  asH  mihrS)  antan pitari  (sd.)  pükrymca  Yt.io,  117.
25930:•  j.satö.aefhya- Adj.'derhundertSchiller hat':  salnahe  (sd.)  .  ,  yS  paoiryS  'ryi fraxitata  Yt.  y.97.
25939:•  j.  satö.tsmö.-sata-  n.  'das  hundertste Hundert':    saiäü  'ta    Vyt  IQ.     Wertlose
```


## [2026-09-05T17:50:06.236Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=25880 && NR<=25945' BRT.txt | grep -nE \"^[0-9]{3,4}$|^\\s*1[0-9]{3}\\s*$\" \necho \"--- raw short lines ---\"\nawk 'NR>=25860 && NR<=25945 {if (length($0)<12) print NR\": \"$0}' BRT.txt"
}
```


## [2026-09-05T17:50:07.664Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD dwyst / two hundred ===\"\ngrep -n \"dwyst\\|ðwyst\\|two hundred\" SOD_pages.txt | head -20\necho \"=== SOD page 147 tag ===\"\ngrep -n \"\\[pdf page 147\\]\\|\\[pdf page 148\\]\" SOD_pages.txt | head"
}
```


### [2026-09-05T17:50:07.874Z] TOOL RESULT

```
--- raw short lines ---
25861: dby  Google
25862: 1553
25863: 'sak-
25907: dby  Google
25936: dby  Google
25937: '557
25940: Bildung.
```


### [2026-09-05T17:50:07.950Z] TOOL RESULT

```
=== SOD dwyst / two hundred ===
5624:     every time                                                           Swest ? =»dwyst
5625:     MDii pl65n3;GMS 1120                                                 two hundred
14341:3713 SwylOO           B => dwyst                                    3724 5yMn     B                 <ii(£w>j / ^ k^x\ i Jjt
14353:3716 dwyst       C                                         o~»>)          GMS 1014
14356:       two hundred                                                        5i/o|3 ©<*dwi-    ©in compd.    =»8Ptyk, Sw>
14361:3717 dwystysywystmyq
14364:       two hundred and twenty-third              r>-^                    TSP 2.1120, 17.14; SCE 442; GMS 430
39781:two hundred        661, 3716             unhurtfulness    8154                    Ursa Major     541
39782:two hundred and twenty-third             union    472,1165,10446                  us 892, 5331, 5713
=== SOD page 147 tag ===
```


## [2026-09-05T17:50:14.154Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14340,14370p' SOD_pages.txt\necho \"=== page tags sample ===\"\ngrep -n \"pdf page\" SOD_pages.txt | head -5\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l) for l in lines[:14352])+14352\nprint('leaf(formfeeds before line 14353):', t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-05T17:50:15.876Z] TOOL RESULT

```
3712 5\vxth       S =* 8wx8r, 8wyt(,)                                     C2, 83V2npl63
3713 SwylOO           B => dwyst                                    3724 5yMn     B                 <ii(£w>j / ^ k^x\ i Jjt
3714 dwyd        C                                           jjjb         8yan (8y>n) ©dhyana; Skt samadhi        ©ob. -f)Jy;
          ©ob. -y; pr. name           \                                     ace. -w
        David                                                             meditation
        C2; STii 6$, 10, 12                                               BSTBL; Sogdica. 60.3
3715 dwynt        C
                                                                    3725 5y>n -» 5y»n
        Siwand ? =>dywyd
                                                                    3726 5y>ncyk     B                      ^Jjs tJJc ju >>
        with it
        BSTi 247                                              OIL         5yancik =»6y*n
                                                                          {related rcOmeditation
3716 dwyst       C                                         o~»>)          GMS 1014
       5owist, 6wcst       (5wyl00) ©<Av. duye-saite                3727 5yp- B                                              ^
         ^Swyst
       two hundred                                                        5i/o|3 ©<*dwi-    ©in compd.    =»8Ptyk, Sw>
                                                                         two
       STii 1.82; SCE 561; BSTBL, Padm. 45; GMS 1316;                    GMS 1320
         SW,C2n p51
                                                                    3728 ayp'zp'k    B                      J^tj^j^^j^
3717 dwystysywystmyq
                                                                         8ip(a)z)3ak    (SypzP'k)
     8wiste se-wist-mik                                                  two-tongued, hypocrite
       two hundred and twenty-third              r>-^                    TSP 2.1120, 17.14; SCE 442; GMS 430
     C2, 1R9 n p50.51                                               3729 6yp6tt     B                                 k*^
3718 6x S                                                                5eP5at ? ©Skt. Devadatta
       8ax ? ©<daha         ©prop. n. SxzHk                v<>           an enemy of the Buddha
       male, man                                                         BSTBL, Dhu. 106
       S W, Rock. Insc. Indus Valley 1989, 135; CII,                3730 8ypnw      B, M                              jv>
         1992, p51
=== page tags sample ===
leaf(formfeeds before line 14353): 212
```


## [2026-09-05T17:50:24.146Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sad ===\"\ngrep -n \"sad \\[\\|sad ‹\\|ṣad\\|^sad\\b\" PHD.txt | head -20\necho \"--- PHD hundred ---\"\ngrep -n \"hundred\" PHD.txt | head -20"
}
```


### [2026-09-05T17:50:24.210Z] TOOL RESULT

```
=== PHD sad ===
562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
619:wassad [wst! | N bussad] coral.
3494:sad andāg(g)ēn, andóhgén, zarīg- ómand; v. sorrowful.
--- PHD hundred ---
562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
2338:hundred sad.
```


## [2026-09-05T17:50:24.863Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sad/hundert ===\"\ngrep -n \"hundert\" HRN.txt | head -20\necho \"=== HUB sad ===\"\ngrep -n \"hundert\" HUB.txt | head -20"
}
```


### [2026-09-05T17:50:24.934Z] TOOL RESULT

```
=== HRN sad/hundert ===
2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
5256:586. duvlst {*duvest) 'zweihundert' {du sed).
5258:hundert'.
6347:aber sed, S. 8 Zeile 4) 'hundert'.
6348:aw. safa- 'hundert*; phlv. sat; ai. gatd-,
9474:bildungen hlzdeh, hijdeh^): statt hestsed dreihundert
=== HUB sad ===
3720:1095. Lies hest^ed achthundert*.
4085:hunderte friiher gesprochen wurden^), was besonders fiir
4115:Jahrhunderten an. Dass ausserdem jede Umschreibung
4368:semn. vtst etc., zd. visaiti; duvest zweihundert*, paz. duest
4629:(danach sanzdah sechzehn* etc.), pansad *fiinfhundert' zu
6358:BB. 4, 35) und mag etwa zwei Jahrhunderte friiher be-
6656:sind, wie in hist 'zwanzig aus "^vtsatj duvest zweihundert'
7472:'angenehm' (oben p. 41), dsiidan ruhen*, duvSst *zweihundert'
8448:sat in bTst 'zwanzig* = zd. visaiti und diivest zweihundert*
```


## [2026-09-05T17:50:30.460Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- HRN 6340-6355 ---\"; sed -n '6338,6356p' HRN.txt\necho \"--- HRN 5250-5262 ---\"; sed -n '5250,5262p' HRN.txt\necho \"--- HUB 8440-8455 ---\"; sed -n '8440,8455p' HUB.txt"
}
```


### [2026-09-05T17:50:30.543Z] TOOL RESULT

```
--- HRN 6340-6355 ---
bei. sak 'hart, stark, fest' (383); yidg. sukt.
V
72 t. sw/un, SU/m (Sahn. I, 29 V. 117 neben -ww, ebendas.
V. 109) 'Wort, Rede*.
Käs. K. siixan[6ni,
aw. sax'Ore (Y. 29, 4), säx^em (y. 53, 5) ('Plan, Rat,
Rede' (Bartholomae, Ar. Forsch. III, 36, 37); phlv.
sa/wi 'Wort, Rede'.
725. sed (heute geschrieben sed; AM. sed, S. 7 Zeile 15,
aber sed, S. 8 Zeile 4) 'hundert'.
aw. safa- 'hundert*; phlv. sat; ai. gatd-,
kurd. sed; af/. sal, sil; oss. sädä (218); wa;^. sar.
LW. sad.
720. ser 'Kopf; vergl. serapa 'Ehrengewand' ^).
aw. Sarah' 'Kopf; phlv. sar^ asar 'endlos' (aw.
anayra-); ai. ciras- 'Kopf; arm. sar 'Höhe, Gipfel,
Abhang' (H. No. 247).
'J Übertritt in die e-lleihe Ca. bei Feist, No. 531).
^) oiiottnts (llesycb), de Lagarde, Ooa. Abb. 208 (?); vergl.
--- HRN 5250-5262 ---
dösdn- 'Vorderarm, Arm'.
585. dev>lden 'laufen, eilen , devän, devämden,
ai. l/^dhaV'j dhdvati 'rennen, rinnen, strömen; phlv.
davTtan (auch "2M geschrieben); gr. dsu).
"WSL/, vidäv-am 'laufen, rennen', sar. davän-am
'galoppiren'.
586. duvlst {*duvest) 'zweihundert' {du sed).
aw. dv^ säte ; päz. dvest (Aogem.) ; ai. dve gate 'zwei-
hundert'.
Der ehemalige Majhülvokal hat sich in der Aus-
sprache, die ursprünglich duvest gewesen sein muss,
*) Dar m steter, Et. ir. I, 319.— 131 —
nicht mehr erhalten ^). duvlst ist die einzige im Np.
--- HUB 8440-8455 ---
= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
skr. srsta-, Wrzl. serg^ ; hast ^) 'acht* = zd. asta, idg. okHOu ;
biristan 'braten' mit st aus skt von Wrzl. iran. brj und
bri^g = idg. bhrzg, oben p. 27.
b) = st: dost Treund' == ap. daustar-; §ast 'sechzig'
= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
46, 139) = ap. mad^ista- ; bargustuvan 'Pferdepanzer H. 205,
oben p. 27. Durch spateren Vokalausfall entstand st aus
sat in bTst 'zwanzig* = zd. visaiti und diivest zweihundert*
= zd. duy^ saite.
Im Phi. steht st hauiBiger fiir urspr. st im Auslaut,
Ygl. angust H. 125 (np. angust), must 'Fau.t' Gl. and Ind.
^J Dazu haStdah 'achtzehn* = hazdah (Fird. I, 46, 216, vgl. die
Anm.) und hajdah (Vullers, Gram. p. 185), hizdah, hijdah Sal,
Shuk. p. 39,— 237 —
218 (np. must), besonders in Superlativen : paz. mahest
```


## [2026-09-05T17:50:40.573Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ qintar ===\"\ngrep -n -i \"qintar\\|qinṭār\\|kintar\\|Ḳinṭār\\|qanṭara\" FVQ.txt FVQ_pages.txt | head -20"
}
```


### [2026-09-05T17:50:40.646Z] TOOL RESULT

```
=== FVQ qintar ===
FVQ.txt:15208:Qintar a measure. 
FVQ_pages.txt:8794:Qintar a measure.
```


## [2026-09-05T17:50:42.327Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA (Fraenkel) qintar ===\"\ngrep -n -i \"qintar\\|kintar\\|Kintâr\\|centenarium\" AFA.txt | head -20\necho \"=== KLN centenarium/quintal ===\"\ngrep -n -i \"quintal\\|centenarium\\|kentenarion\\|kentenarion\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-05T17:50:42.434Z] TOOL RESULT

```
=== AFA (Fraenkel) qintar ===
=== KLN centenarium/quintal ===
KLN_1966.txt:6964:cental,  n.,  a  unit  of  weight,  hundredweight.  — Formed  fr.  L.  centum,  ‘a  hundred’,  with  adj. suflf.  -al,  on  analogy  of  quintal. centaur,  n.,  i)  one  of  a  mythical  race  in  ancient Thessaly,  conceived  as  monsters,  half  man,  half horse  ( Greek  mythol.);  2)  (cap.)  =  Centaurus ( astron .)  —  L.  Centaurus,  fr.  Gk.  Kevxaupoc, which  is  of  uncertain  origin,
KLN_1966.txt:20538:Kanarese,n.,  1)  a  member  of  the  people  inhabiting the  districts  of  North  and  South  Kanara  in India ;  2)  the  language  spoken  by  this  people.  — Formed  fr.  Kanara  with  suff.  -ese. kangaroo,  n.  —  Australian  native  name, kantar,  n.,  an  Egyptian  weight  corresponding to  the  hundredweight.  —  Arab,  qintdr,  fr.  Aram. qintdr,  qintard,  short  for  qinfmard ,  ‘hundred pounds’,  fr.  Late  Gk.  xsvT7]vapi.o?,  representing L.  centenarius ,  ‘consisting  of  a  hundred ;  weighing a  hundred  pounds’.  (See  S.  Fraenkel,  Die  ara- maischen  Fremdworter  im  Arabischen,  Leiden 1886,  p.203).  See  centenarian  and  cp.  centner. Cp.  also  quintal  and  kilderkin.
KLN_1966.txt:20676:kilerg,  a  physical  unit  of  work,  equal  to  1000 ergs.  —  See  kilo-  and  erg. kilderkin,  n„  1)  a  cask;  2)  an  old  English  liquid measure.  —  ME.,  dissimilated  fr.  MDu.  kin- derkin  (also  kindeken),  a  dimin.  formed  with suff.  -kin,  fr.  OF.  quintal,  ‘quintal,  hundred¬ weight’.  See  quintal.
KLN_1966.txt:31435:quintal,  n.,  a  weight.  —  F.,  fr.  ML.  quintale,  fr.
KLN_1971.txt:42476:suff. -al, on analogy of quintal. 
KLN_1971.txt:130424:Cp. also quintal and kilderkin. 
KLN_1971.txt:131231:suff. -kin, fr. OF. quintal, ‘quintal, hundred- 
KLN_1971.txt:131232:weight’. See quintal. 
KLN_1971.txt:198553:quintal, n., a weight. — F., fr. ML. quintdle , fr.
```


## [2026-09-05T17:51:00.213Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15200,15215p' FVQ.txt\necho \"=== search qnt / centenarium in FVQ ===\"\ngrep -n -i \"centenarium\\|centenarius\\|kentenar\\|qintâr\\|Qintâr\\|qin.ar\" FVQ.txt | head -20\necho \"=== قنطار in FVQ ===\"\ngrep -n \"قنطار\" FVQ.txt FVQ_pages.txt | head"
}
```


### [2026-09-05T17:51:00.296Z] TOOL RESULT

```
the source of the Arabic word. 3 It must have been an early borrowing 
for we find it not infrequently in the old poetry. 

**\\ - 

jlklj (Qintdr). 

iii, 12, 68 ; iv, 24. 
Qintar a measure. 

It was recognized by the philologers as of foreign origin, and though 
some, like Slbawaih, held to an Arabic origin, Abu 'Ubaida (LA, vi, 



is a good Tndo-European word, as is evident from the Skt. 
=== search qnt / centenarium in FVQ ===
15208:Qintar a measure. 
15234:centenarium, and passed into Aram, as irD3p, Syr. JjLi^iO. 8 
=== قنطار in FVQ ===
```


## [2026-09-05T17:51:02.854Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15205,15250p' FVQ.txt\necho \"=== page tag ===\"\ngrep -n \"Qintar a measure\" FVQ_pages.txt\nawk 'NR>=8760 && NR<=8800' FVQ_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | head"
}
```


### [2026-09-05T17:51:05.344Z] TOOL RESULT

```
jlklj (Qintdr). 

iii, 12, 68 ; iv, 24. 
Qintar a measure. 

It was recognized by the philologers as of foreign origin, and though 
some, like Slbawaih, held to an Arabic origin, Abu 'Ubaida (LA, vi, 



is a good Tndo-European word, as is evident from the Skt. 
Norse Jtalmr ; Slav, slama ; cf. Boissacq, 397. 

2 See Fraenkel, Fremdw, 45. 

3 Vollers, ZDMO, li, 311, thinks that the Arabic came from the Lat. camifiia, 
but this is hardly likelv. 



244 FOREIGN VOCABULARY OF THE QUR AN 

432) expressly states that the Arabs did not know the meaning of the 
word. 1 Some said it was a Berber word (as-Suyuti, Itq, 323), others 
that it was Syriac (as-Suddl in Mukkassas, xii, 266), but the majority 
were in favour of its being Greek (ath-ThaSalibl, Fiqh, 318 ; as- 
Suyuti, Muzhir, i, 134). 

Undoubtedly it is the Gk. Ktvrrjvdpiov, which represents the Lat. 
centenarium, and passed into Aram, as irD3p, Syr. JjLi^iO. 8 
It was from the Aram., as Fraenkel, Vocab, 13 ; Fremdw, 203, shows, 
that the word came into Arabic, and in all probability from the 
shortened Syr. form Ji 



(Qiyama). 
Occurs some seventy times, cf. ii, 79. 
Resurrection. 
It occurs only in the expression <Ajill *^, which is a technical 

eschatological term for the Last Day. 

The Muslim authorities naturally relate it to the root J& to stand 

or rise, but it has been pointed out many times, that as an eschato- 
=== page tag ===
8794:Qintar a measure.
```


## [2026-09-05T17:51:16.165Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb && ls site/pages/115.jpg 2>/dev/null; pdftoppm -f 115 -l 115 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg115 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T17:51:17.277Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT صد ===\"\ngrep -n \"^صد\\|صد (\" BQT_v2_pages.txt | head -10\necho \"=== BQT دویست ===\"\ngrep -n \"دویست\" BQT_v2_pages.txt BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T17:51:18.539Z] TOOL RESULT

```
total 34108
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:51 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


### [2026-09-05T17:51:18.611Z] TOOL RESULT

```
=== BQT صد ===
34227:                ‫‪ _ ۴‬از ‪ :‬سد (صد) ‪٣‬‏ یای ‪-۳‬ه (شبت) ؛ دارای صد (عدد کثیر) یا ‪.‬‬
=== BQT دویست ===
BQT_v1_pages.txt:373:مدت طولانی که بیش ازهزار ودویست سال است : آثار کتبی که از زبان
BQT_v1_pages.txt:610:(دو>» دو » «دویسته » دویست ۰ «بمژه> بنج » «نسپور 4 چپار ؛ «دسه»
BQT_v1_pages.txt:3910:اين نسخه در سال یکپز ار ودویست وچپل در بلده‌کاشان آغاز شده
BQT_v2_pages.txt:22784:  ‫از حروف ابجد ‪ ,‬وآنرا ر ‪ ۵۲‬وراه ‪ ۰۵۲‬نامند و درحساب جمل دویست گر ند‪ .‬این حرف به «ل»‬
```


## [2026-09-05T17:51:23.960Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg115.png"
}
```


### [2026-09-05T17:51:24.431Z] TOOL RESULT

```

```


## [2026-09-05T17:51:24.428Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:51:39.527Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 115 -l 115 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg115_600\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg115_600.png'); print(im.size)\nw,h=im.size\n# greek hektaton box approx y 550/2200*h .. ; use ratios from 1700x2200 view\ndef crop(x0,y0,x1,y1,name):\n    im.crop((int(x0/1700*w),int(y0/2200*h),int(x1/1700*w),int(y1/2200*h))).save(name)\ncrop(440,440,660,530,'c_hektaton.png')\ncrop(440,1230,760,1310,'c_kent.png')\n\"\nls -la c_hektaton.png c_kent.png"
}
```


### [2026-09-05T17:51:44.727Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3345 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb 3026 Sep  5 13:51 c_kent.png
```


## [2026-09-05T17:51:51.232Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg115_600.png'); w,h=im.size\ndef crop(x0,y0,x1,y1,name):\n    c=im.crop((int(x0/1700*w),int(y0/2200*h),int(x1/1700*w),int(y1/2200*h)))\n    c=c.resize((c.width*2,c.height*2))\n    c.save(name); print(name,c.size)\ncrop(440,590,660,690,'c_hektaton.png')\ncrop(440,1240,760,1320,'c_kent.png')\n\""
}
```


### [2026-09-05T17:51:53.472Z] TOOL RESULT

```
c_hektaton.png (1320, 600)
c_kent.png (1920, 480)
```


## [2026-09-05T17:51:55.767Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_hektaton.png"
}
```


### [2026-09-05T17:51:55.790Z] TOOL RESULT

```

```


## [2026-09-05T17:51:59.330Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_kent.png"
}
```


### [2026-09-05T17:51:59.350Z] TOOL RESULT

```

```


## [2026-09-05T17:52:23.482Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON هکتار ===\"; grep -c \"هکتار\" MON_part1.txt MON_part2.txt 2>/dev/null\ngrep -n \"هکتار\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== MON قنطار ===\"; grep -n \"قنطار\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== MON سانتیمتر / سانتی متر ===\"; grep -n \"سانتیمتر\\|سانتی متر\\|پورسانتاژ\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T17:52:23.607Z] TOOL RESULT

```
=== MON هکتار ===
MON_part2.txt:1
MON_part1.txt:2
MON_part2.txt:90677:هکتار: ۰6۱02۲ (.) واحد برایر مقیاس سطح 
MON_part1.txt:2541:متر مربع (یکث دکامتر مربع): هکتار - صد 
MON_part1.txt:80581:هکتار زمین کافی باشد. - در اصفهان یکث 
=== MON قنطار ===
MON_part2.txt:15151:قنطار: (ند. -۰۸۱276۵[معر. یو (.) پوست 
MON_part2.txt:15156:۷ ۴) ج. قناطیر. . ضح.- در وزن قنطار 
MON_part1.txt:55857:که از طلا و نقره بر کنند؛ خرطال قنطار. 
=== MON سانتیمتر / سانتی متر ===
MON_part2.txt:120:۰ تا ۲۰ سانتیمتر و سهنایش ۴ تا۸ 
MON_part2.txt:121:سانتیمتر است. پهنکك ب رک در سطح فوقانی 
MON_part2.txt:821:می‌گر دد. طول هر غده در انسان ۳ سانتیمتر 
MON_part2.txt:822:و ارتفاعش ۲ سانتیمتر و ضخامتش یکك 
MON_part2.txt:823:سانتیمتر است و وزن هر یکث مایین وشن 02
```


## [2026-09-05T17:52:25.731Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index centum/dekm ===\"; grep -n -i \"DEKM\\|KMTOM\\|CENTUM\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY صد ===\"; grep -n \"صد (\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== IEC kmtom ===\"; grep -n -i \"km̥tom\\|kmtom\\|kṃtom\" IEC.txt | head -10\necho \"=== SYN hundred ===\"; grep -n -i \"13.14\\|Hundred\" SYN.txt | head -10"
}
```


### [2026-09-05T17:52:25.832Z] TOOL RESULT

```
=== ARY latin index centum/dekm ===
207:SHEL 5 92 (She oly CoV gury}) CENTUM pr SUELS 9 (BU 592k gata
465:Yes coad cant ‘hekaton centum cento
806:(CENTUM) tg sl0ob 5 apr YET oS cl op! Ob5 32 Gx! Gegks2 le Ge
11224:stTo CENTUM (LATIN) pa
=== ARY صد ===
=== IEC kmtom ===
18958:triioKomt-, -Kmt- ‘thirty’. Cf. treies (triio), tri-—, and Kmtom Skt. trim$át; Arm. eresun; Gk. triákonta; Lat. triginta; Mir tricha, Ir. triocha; Br. tregont; OW cf. trimuceint, id.
=== SYN hundred ===
120:A constantly increasing number of journal articles, dissertations, and other monographs have dealt with particular groups of synonyms in special fields —a few of them in a non-Indo-European family like Semitic or Finno-Ugri- an, most of them in Indo-European or some branch of it, like the Romance or the Germanic languages. Such monographs furnish some of the stones for building a more comprehensive structure. But they are scattered, they cover only a small number of even the commonest notions, and some are writ- ten on such a grand scale (running to hundreds of pages; e.g. on words for ‘child’, ‘boy’, ‘girl’ in the Romance languages 426 pages, in Old English 271 pages) as to be unwieldy for use without the most severe trimming. A “Dic- tionary of Ideas” (a title that would suggest to laymen the point of such study) in a truly comprehensive sense (history of words for all ideas in all known languages) is, of course, an idle dream. Even for the Indo-European - field anything like a complete semantic dictionary is beyond probable reali- zation at present.
2563:ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such infantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
5246:: form a distinctive is pac ea De Aid tacan a en of their extensive second- es uses. They have been exhaustively discussed for certain fields!, especially the Romance, where it has been noted that, with the inclusion of the dialects, there are some four hundred words an- swering to about eighty in Latin.
13037:tért ‘hundred each’, because of the al- leged ‘hundred-fold yield’ (Pliny, NH 18.16, 40 nascitur (secale) qualicumque
16310:2. Lat. potest (> Romance forms), fr. potis est and pote est, phrase with potis, neut. pote ‘able, possible’ : Skt. pati- ‘master, husband’, Grk. zéo.s ‘husband’, Goth. fabs in brip-faps ‘bridegroom’, hunda-faps ‘master of a hundred, cen- turion’, Lith. patis ‘husband’, ete. Walde-P. 2.77f. Ernout-M. 796.
17323:ON krjipa, Dan. krybe, Sw. krypa, OE créopan, ME crepe, creep, NE creep, Du. kriupen, fr. IE *greu-b- (: Lith. grubineti ‘stumble’); OHG chriochan, MHG, NHG kriechen, fr. IE *greu-g- (: Ir. grug ‘wrinkle’); extensions of LE *ger- in Lett. griezt ‘turn’ (10.13-14), Lith. greati ‘turn around, bore’, etc. Walde- P. 1.597f. Falk-Torp 585.
18314:Av. vaga- : varat- ‘turn’ (10.13-14). Barth. 1418.
18755:avépa is rendered by NIr ni Shuil fear agam, W. nid oes gennyf wr, and Br. nem eus pried ebet ‘there is not a hus- band to me’; so also Lett. man vira nav, Russ. u menja net muza ‘there-is-not a husband to me’. Skt. as- or bha- with the gen. may be ‘have’ or ‘own’, cf. tasya gatam jaya babhuvur ‘he had a hundred Wives’, or manor ha vd rsabha asa ‘Manu had a bull’ (cf. Delbriick, Altind, Syn- tax 162), and similarly, Av. agava dana .... yd hanti spantahe mainysué ‘those creatures....which the holy spirit possesses’ (Yt. 6.2), also with omission of ah-: vahista i84& sradvi zarabustrahé ‘Zarathustra has the best good known���, lit. ‘optimum bonum auditum (est) Zarathustri’ (cf. Reichelt, Aw. Gramm. 253; Barth. 269).
20382:5. Lith. nuosiméai, pl. of nuosimtis ‘percentage’ fr. nuo ‘from’ and Simias ‘hundred’, neolog. modelled on Pol., Russ. procent (below).
20393:Pol., Russ. procent ‘percenta of interest’, hence also simply ‘interest? prob. fr. NHG prozent = It. per ceniy’ etc. ‘by the hundred, percent? With sub. stitution of pro, as if Lat. pro centwm,
```


## [2026-09-05T17:52:33.170Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON قنطار entry ===\"; sed -n '15148,15162p' MON_part2.txt\necho \"=== MON هکتار entry ===\"; sed -n '90672,90690p' MON_part2.txt"
}
```


### [2026-09-05T17:52:33.242Z] TOOL RESULT

```
=== MON قنطار entry ===


قنداق 
قنطار: (ند. -۰۸۱276۵[معر. یو (.) پوست 
گاوی که درون آن را پر زر کرده باشند. 
واحد وزن معادل یک هزار و دویست اوقیه» 
يا ساوی یکصد و بیست رطل (رساله 
مقداریه. فرهنگ ايران زمین ۱۰: ۴-۱ ص 
۷ ۴) ج. قناطیر. . ضح.- در وزن قنطار 
0 : بعضی آن را ۴۰۰۰ دینار 
یا ۱۰۰ من و ۱۰۰ رطل و ۱۰۰ مثقال و 
۰ درهم گفته‌اند. برخی ۱۲۰۰ اوقیه با 
۰ رطل» برخی ۳۰ اوقیه از زر با 
۰ دینار يا ۸۰/۰۰۰ درهم یا ۱۰۰ 
رطل زر و سیم. 
=== MON هکتار entry ===

هفهف: ]20:2 (اصت ۰) آواز سک 

هق وهق: 7۰-۰6 (اصت ق.) (عم) آوای 
کر بة شد ید » صدای گر یستن سحت. 
هکتار: ۰6۱02۲ (.) واحد برایر مقیاس سطح 
صد ,آر» - یک هکتومتر مربع - و ۱۰ 
مر فرب : 

هک‌تو متر: ۱-۲ (امر.) واحدی برای 
سنجش طول - ۱۰۰ متر 

هکسچه: )۱0۲۵ (اصتد.) جستن گلوه 
فواق. ضح.- (پز.) سکسکه. 

هعکف: 6 (ص.) سیهوده» بیفایده؛ 
مزخرف (بیشتر در مورد اجسام و موجودات 
غیر ذی‌روح بکار برند).
```


## [2026-09-05T17:52:35.268Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN numerals hundred sec ===\"; grep -n \"13\\.1[0-9]\" SYN.txt | head -20\necho \"=== SYN sata ===\"; grep -n \"Av. sata\\|satəm\\|OPers. \\(t\\)ata\\|Skt. śatam\\|çatam\" SYN.txt | head -10"
}
```


### [2026-09-05T17:52:35.345Z] TOOL RESULT

```
=== SYN numerals hundred sec ===
2563:ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such infantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
4192:ra, Le Akad. 1918, no. 10. sok Ir. caera, NIx. caora, deriv- of © caer ‘berry, lump, Glog enence a ss from its characteristic droppings. Thur- neyeen, Z. celts Ph. 13.107.
4484:3. Ir. gabor, NIr. gabhar, W. gafr, Br. gaor, gavr, perh. with unexplained init. variation : Lat. caper, etc. So Thurney- sen, Gram. 189, Z. celt. Ph. 13.108 ff. Otherwise Walde-P. 1.533, 547. es Goth. gaits, ON geit, OE gat, etc., a general Gme. word: Lat. haedus kid ; perh. Lith. Zaidziu, Zaisti ‘play’ as =H Jump, gambol’. Walde-P. 1.527.
8025:Sp. cansado, pple. of cansar ‘tire’ (now trans.; refl. ‘get tired’), this (not : Fr. casser ‘break’ ifr. Lat. quassare ‘shake’, as Diez 91, REW 6939, but) = It. cansare ‘avoid’, fr. Lat. campsdre ‘turn aside from’, fr. Grk. xaépyar aor. Of kaurrw ‘bend’ (9.14). So Korting, Menéndez Pidal, C. C. Rice, Language 13.18 f., 19.154, Leo Spitzer, Language 14.205 f., Wartburg 2.156. Lat. campsdare occurs in Ennius in the nautical sense of doub- ling a headland (frequent in Grk.), then only in late Latin in more general sense of ‘turn aside from’ e.g. ut de via cam- semus Pereprinatio 10.8 and in many Blosses, The semantic development in Spanish was prob. (otherwise Rice) oan > ‘cease’ > ‘get hired INe ra as ie > es atl oie re 4 € association is there, ‘get tired? ae cho Russ. ustavat! 0 Slensich » ustate get tired, cease’ =
8327:etc. Walde-P. 1.732), used mostly of animals, but also of men, and in late times simply ‘eat’. In the NT, while less common than éo@iw, it is usual in the Fourth Gospel and must have there a fully respectable standing, for it is put in the mouth of Jesus (Jn. 13.18, etc.). For other examples in pap., cf. Moulton- Milligan s.v. NG zpw(y)w is the reg. word for ‘eat’ in the present.
20261:Av. éi- ‘atone for’ and so ‘pay’ (e.g. Gikayat Vd. 13.10; cf. Barth. 108 s.v. afga- and 464) : Grk. zivw ‘atone for’, etc. (above, 1).
20274:38. Ir. airem, comairem ‘number, reck- oning, account? (cf. Laws, Gloss. 37), NIr. comhaireamh, W. cyfrif, epds. fr, rim-, W. rhif ‘number’ (13.12), vb. Ir. airmin ‘count’ (ad-rim-, Pedersen 2.602).
21129:‘thrive’, etc., prob. : Skt. ghana- ‘com- pact, firm’, Lith. gana ‘enough’, etc. (13.18).
22441:‘Large’ and ‘small’ (12.56) are, of course, understood here in reference to size. For the corresponding notions of quantity, amount, or number, which are partly expressed by the same terms but partly differentiated, see 13.15, 13.17.
22474:2. Lat. parvus (also ‘little’ in quan- tity) : Grk. radpos ‘little’, pl. ‘few’, Lat. pauct, Goth. fawai, etc. ‘few’ (13.17). Walde-P. 2.75. Ernout-M. 737, 742.
23351:13.11 Quantity
23352:13.12 Numper
23353:13.13 WHOLE
23354:13.14 Every; Au (pl.)
23355:13.15 Mucu; Many
23356:13.16 More
23357:13.17 Lirruz (Quantity); Few (Number)
23358:13.18 ENnoucH
23359:13.19 Moxtirupr, Crowp
23360:13.192 Norte on oTHER Wonps ror A CoL- LECTIVE Bopy (of Persons, Ani- mals, or Things)
=== SYN sata ===
```


## [2026-09-05T17:52:50.854Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb && sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-05T17:52:52.815Z] TOOL RESULT

```
Exit code 2
sed: can't read tools/fetch_source.py: No such file or directory
```


## [2026-09-05T17:52:52.835Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kmtom headword ===\"; grep -n \"^kmtom\\|Kmtom\\|kṃtóm\\|km̥tóm\\|‘hundred’\" IEC.txt | head -20\necho \"=== LEW centum ===\"; grep -n \"^centum\\|centum,\" LEW_1910.txt | head -10\necho \"=== LAT centum ===\"; grep -n \"centum\" LAT.txt | head -10"
}
```


### [2026-09-05T17:52:52.924Z] TOOL RESULT

```
=== IEC kmtom headword ===
18958:triioKomt-, -Kmt- ‘thirty’. Cf. treies (triio), tri-—, and Kmtom Skt. trim$át; Arm. eresun; Gk. triákonta; Lat. triginta; Mir tricha, Ir. triocha; Br. tregont; OW cf. trimuceint, id.
=== LEW centum ===
=== LAT centum ===
1395:centum); "X 1'image de; en ce qui touche a, concernant"; sens qui a du
1902:iecem uel centum assilws. - Ancden, usuel. M.L., 346.
11083:centum
11119:centum (indeclinable): cent. Ancien substantif neutre devenu inva-
11120:riable, coame mille. Par suite, le nom qui accompagne centum est traite
11122:Les coaposes multiplicatifs de centum sont des adjectifs dedinables:
11124:Bdb .*, p.470); un reste de neutre apparait peut-etre dans le centum
11125:ac ducentum... milia, Lucii. 1051, o& ducentum est peut-etre le cor -
11131:centie(n)s : cent fois; centendrius: "qui centum (centenas) partes
11134:m. : centum asses (cf. deciissis ).
```


## [2026-09-05T17:52:55.442Z] TOOL CALL #37: Bash

```json
{
 "command": "ls tools/ | head -40"
}
```


### [2026-09-05T17:52:55.484Z] TOOL RESULT

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
```


## [2026-09-05T17:52:56.153Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11119,11145p' LAT.txt"
}
```


### [2026-09-05T17:52:56.208Z] TOOL RESULT

```
centum (indeclinable): cent. Ancien substantif neutre devenu inva-
riable, coame mille. Par suite, le nom qui accompagne centum est traite
coaae avec les noas de noabre precedents,en apposition, non au gdnitif.
Les coaposes multiplicatifs de centum sont des adjectifs dedinables:
ducenti, quingenti, etc.(sur la phonetique de ces formes, voir Sommer,
Bdb .*, p.470); un reste de neutre apparait peut-etre dans le centum
ac ducentum... milia, Lucii. 1051, o& ducentum est peut-etre le cor -
respondant du collectif skr .dvi-fatan. Atteste de tout temps. Panroman,
sauf roumain. M.L.1816.
Ddrivds: centeni, -ae, -a, distributif, d’oii centjsnum: sorte de bld,
"qui rend cent pour un", M.L.1811; centesimus, centibme, d'oli ducen¬
tesimus, etc., d f aprfes uicesinus, etc.; coaae duceni d'aprfes uicenl;
centie(n)s : cent fois; centendrius: "qui centum (centenas) partes
habet"; d'ou A basse Epoque "centenaire", exaxovxaexTjS, et synonyme
de centurio (cf. centena: centenarii dignitas), M.L.i8ioa; centussis
m. : centum asses (cf. deciissis ).
La forae, fldchie dans les neutres skr. fata*, v. sl. silto, et dans
lit. sintas, est devenue invariable en latin comae dans iri. cet (cf.cepa
3 03
gall. eant ), got. hund, gr. e—jcaxov, d'aprbs le modble des eous de nombre
de "cinq" a "dix", l A en juger par le caractbre continu de 1 'aire du
type invariable, le fait doit etre ancien en Occident; 1 'ancien dnel
uigintl et les anciens "pluriels neutres" tels que triginta , etc.,sont
anssi fixes sons la forme de nominatif-accusatif, de meme que les
correspondants grecs.
centuria f.(cf. decuria) : Varr., L.L. 5 , 88 , centuria, qui sub uno cen¬
turione sunt, quorum centenarius iustus numerus, D 4 signe d'abord un
```


## [2026-09-05T17:53:00.712Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T17:53:00.720Z] TOOL RESULT

```


```


## [2026-09-05T17:53:05.593Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1m%CC%A5t%C3%B3m",
 "prompt": "Give the full etymology and descendants for PIE *ḱm̥tóm 'hundred': its derivation from *déḱm̥ (ten), and the descendants in Proto-Iranian/Avestan, Latin, Greek, Germanic."
}
```


## [2026-09-05T17:53:07.089Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%B3%D8%AA",
 "prompt": "Give the Persian etymology of دویست (devist) 'two hundred' — Middle Persian, Old Iranian, Avestan forms cited."
}
```


### [2026-09-05T17:53:11.357Z] TOOL RESULT

```
# Etymology and Descendants of PIE *ḱm̥tóm

## Etymology

According to the Wiktionary entry, this term derives from *déḱm̥ ("ten"). The source states: "Some sort of derivation from *déḱm̥ ("ten") (with Pre-IE *d lost or merged with *h₁)" The word likely represents an ordinal formation, possibly meaning "tenth" as a substantive noun, though the exact derivational path remains conjectural.

## Descendants

The attested descendants listed in the source include:

- **Proto-Indo-Iranian**: *ćatám
- **Proto-Hellenic**: *hekətón (Greek ancestor)
- **Proto-Italic**: *kəntom (Latin ancestor)
- **Proto-Germanic**: *hundą (Germanic ancestor)
- **Proto-Celtic**: *kantom
- **Proto-Balto-Slavic**: *śímta
- **Proto-Tocharian**: *känte

The article does not provide specific Avestan, Latin, or Greek reflexes directly—only their proto-language ancestors. These proto-forms subsequently evolved into historical languages, but detailed individual reflexes fall outside the provided source material.
```


### [2026-09-05T17:53:11.700Z] TOOL RESULT

```
# Persian Etymology of دویست (devist)

According to the Wiktionary entry, دویست is "inherited from Middle Persian /⁠duwēst⁠/, from Avestan 𐬛𐬎𐬎𐬈𐬯𐬀𐬙𐬈 (duuesate)."

The word traces back through the Iranian language family. It is cognate with Sogdian dwyst and has been "displaced by دوصد (do-sad) in eastern dialects of Persian."

This etymological path shows the development of the numeral "two hundred" from ancient Avestan through Middle Persian into modern Iranian Persian.
```


## [2026-09-05T17:53:17.108Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%AF",
 "prompt": "Give the Persian etymology of صد (sad) 'hundred' — Middle Persian, Old/Proto-Iranian, Avestan and PIE forms cited."
}
```


## [2026-09-05T17:53:19.295Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%B7%D8%A7%D8%B1",
 "prompt": "Give the Arabic etymology of قنطار (qinṭār): what language it was borrowed from (Greek? Aramaic/Syriac? Latin?), plural قناطير, and its meaning. Also any Persian section."
}
```


### [2026-09-05T17:53:22.588Z] TOOL RESULT

```
# Persian Etymology of صد (sad) 'Hundred'

Based on the Wiktionary entry, here is the etymological progression:

**Middle Persian:** 𐭰𐭲 (čat, sad)

**Old Persian:** *θatam

**Proto-Iranian:** *catám

**Avestan:** 𐬯𐬀𐬙𐬀 (sata)

**Proto-Indo-Iranian:** *ćatám

**Proto-Indo-European:** *ḱm̥tóm

The entry notes that "the spelling with ص was probably introduced to avoid confusion with شد (šod) in early texts with no or defective punctation." Cognates include Sanskrit शत (śatá), Northern Kurdish sed, Pashto سل (səl), and Finnish sata, demonstrating the word's ancient Indo-European roots.
```


### [2026-09-05T17:53:25.701Z] TOOL RESULT

```
# Etymology and Meaning of قنطار (qinṭār)

## Etymology Chain

The Arabic word قنطار traces back through multiple languages:

1. **Immediate source**: "From Classical Syriac ܩܰܢܛܺܝܪܳܐ (qanṭīrā)"
2. **Ultimate sources**: Byzantine Greek κεντηνάριον and Latin centēnārium ("hundredweight")

The word traveled westward through Greek and Latin before being borrowed into Semitic languages like Syriac and Arabic.

## Meaning

The primary definition is a unit of weight measurement. It refers to "hundredweight, quintal, kantar" used historically across Mediterranean and Middle Eastern regions. The plural form is قناطير (qanāṭīr).

Figuratively, it also means "wealth" or "great possessions," appearing in Quranic contexts describing accumulated riches.

## Persian Section

Persian borrowed the same root directly from Arabic. The Persian entry shows قنطار (qentâr) with identical meanings: kantar and hundredweight/quintal, with plural قناطیر.
```


## [2026-09-05T17:53:30.133Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hectare",
 "prompt": "Give the full etymology of hectare, hecto-, and hectare's French coinage date and elements (hecto- from Greek hekaton + are)."
}
```


## [2026-09-05T17:53:31.545Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hundred",
 "prompt": "Give the full etymology of English \"hundred\": Old English hundred, Proto-Germanic *hunda- / *hundam, PIE *kmtom, and the -red element."
}
```


### [2026-09-05T17:53:35.020Z] TOOL RESULT

```
# Etymology of Hectare

**Hectare (noun)** - 1817, from French *hectare* "a hundred ares," combining:
- **Hecto-**: From the Latinized form of Greek *hekaton* "a hundred"
- **-are**: From Latin *area* "vacant piece of ground"

The term was "coined by decree of the French National Convention in 1795" as a metric measurement equal to 100 ares.

**Greek Origin**: *Hekaton* derives from what may be "dissimilation of *hem-katon*, with *hen*, neuter of *heis* 'one' + *katon* 'hundred.'"

The word entered English in 1817, representing a systematized unit of superficial (area) measurement developed during France's metric reform period.
```


### [2026-09-05T17:53:38.191Z] TOOL RESULT

```
# Etymology of English "Hundred"

**Old English Origin:**
The word "hundred" derives from Old English *hundred*, meaning "the number of 100, a counting of 100."

**Proto-Germanic Stage:**
It comes from Proto-Germanic *hunda-ratha-*, where the first element *hundam* means "hundred" and the second element *rath* means "reckoning, number."

**Indo-European Root:**
The *hundam* component traces to PIE *km-tom* "hundred," which itself is a reduced form of *dkm-tom-*. This root appears across Indo-European languages: Sanskrit *satam*, Greek *hekaton*, Latin *centum*, and Lithuanian *šimtas*.

**The "-red" Element:**
The second component *rath* derives from PIE *re-* meaning "to reason, count." Related forms include Gothic *raþjo* ("reckoning, account, number") and the verb *garaþjan* ("to count"). The OED notes that "the common word for the number in Old English was simple *hund*," with the compound form emphasizing the counting aspect of the number.

This etymological structure reflects how Germanic languages built the number through both the cardinal value and an explicit reference to the counting mechanism.
```


## [2026-09-05T17:53:45.718Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/percent",
 "prompt": "Give etymology of percent, cent, century, centenary, centennial, centimeter — from Latin centum / per centum."
}
```


## [2026-09-05T17:53:47.257Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON پورسانتاژ ===\"; grep -n \"پورسانتاژ\\|سانتیمتر:\\|سانتی متر:\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON سانت ===\"; grep -n \"سانتیمتر\" MON_part1.txt | head -5"
}
```


### [2026-09-05T17:53:47.344Z] TOOL RESULT

```
=== MON پورسانتاژ ===
=== MON سانت ===
786:بود ۲۰۰ سانتیمتر تر مکپ آب و ۲۰ گرم 
5369:سانتیمتر» صعتر» سعتر» بودینه صحرایی 
11149:۵سانتیمتری در جوی‌های آب دیده 
12605:۰ تا ۰۰ سانتیمتر است. 
18614:۰ سانتیمتر می‌رسد ب رگ‌هایش به شکل
```


### [2026-09-05T17:53:51.427Z] TOOL RESULT

```
# Etymology of Percent and Related Words

**Percent** comes from Modern Latin *per centum*, meaning "by the hundred." The term dates to the 1560s and combines two elements: *per* (through, by means of) and *centum* (hundred).

**Cent** derives from Latin *centum* "hundred" (late 14c.). Its meaning shifted in the 17th century to denote a "hundredth part" under the influence of *percent*. It was officially chosen in 1786 as the name for the U.S. currency unit representing one hundredth of a dollar.

**Century, Centenary, and Centennial** all trace back to the same Latin root *centum*, which connects to a broader Indo-European family of words for the number 100 found across multiple language groups.

**Centimeter** similarly uses the Latin *centum* combined with the metric prefix for measurement, literally meaning one hundredth of a meter.

All these terms share the fundamental Latin concept of "hundred," making them semantically interconnected through their common etymological ancestor.
```


## [2026-09-05T17:54:00.274Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index around line 465 (hekaton centum cento) ===\"; sed -n '460,470p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY line 207 ===\"; sed -n '203,212p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY 11224 ===\"; sed -n '11218,11232p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-05T17:54:00.343Z] TOOL RESULT

```
=== ARY latin index around line 465 (hekaton centum cento) ===
ta se | chwech hex Sex sei
Yseacht | saith hepta septem sette
A ocht | wyth okto octo otto -
4 naoi | naw ennea novem nove; a
\+ Deich | deg deka decem +] leet
Yes coad cant ‘hekaton centum cento
[pdf page 19]
805 ly} sata cla, | Te
\ en | one jeden odin ek
Y to | two dwie dva dvi
Y tre | three try tri tri
=== ARY line 207 ===
Gs g5he Sp GgIKY OB La
A82F RUS Ay claty yl gies Go sly Scab sly AAUALIL) uy JI
Sagi yo
‘Bla! 54) SATEM totlon Ug 2a bags ty a 92 4 2hys} gata ly
SHEL 5 92 (She oly CoV gury}) CENTUM pr SUELS 9 (BU 592k gata
tp Cll} yo scuul Kab Sh ow (FRICATIVE) ib erergesly ls cab tgilen
(HUNDRED ,, 631 Y SCENT 0515 52 Sta) coal Ni > 3b Veer tter cosy
FN Se 2513 NY s) Sp 9 logue Seal ahaa) ge Ob 5 es 53 oil dle jy
ts atl td ele pF Sp Noe cle y Oy yo 4 aby) yan EFS pady
{Jur sate 92 bey oil (CENTER OF GRAVITY) (6164 J2 iS Sipe pols
=== ARY 11224 ===
HUNDRED ENGLISH) yJSi "SAL, SIL, SEL {AFGHAND (4) gbi!
| HUNDRA DANISH) ls KANT ——_(TOKHARIAN A) A 6
| HUNDRA (SWEDISH) 8 yo KANTE :(TOKHARIAN B) B 5 5
| HUNDRE (NORWEGIAN) 633 SATA (RHOTANESE) 52>
HONDERD DUTCH) gale SATAM, SHATA (SANSKRIT) <2 Sie
(OLD CHURCH SLAVIC) 48 5 3%+\ HEKATON, EKATO — (GREEK) (lin
stTo CENTUM (LATIN) pa
STU, SETKA : (POLISH) soa) CENT (FRENCH) sail 5
sTo (RUSSIAN) g3 CIENTO SPANISH) gil!
sToO CZECH) See CENTO AUITALIAN) gids!
sTO (BULGARIAN) (5) SUTA (RUMANIAN) glvy 5
sto (SLOVAK) 5 let CEM. :(PORTUGUESE) J
SHIMTAS (LITHUANIAN) gly} HUNDA (GOTHIC) 3
SIMTS LATVIAN) (5) 3) OLD SCANDINAVIAN) 48 5th!
CET (OLD IRISH) 4S 53.2! HUNDRADH
```


## [2026-09-05T17:54:02.062Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB sad/sat ===\"; grep -n \"sat 'hundred'\\|sad.*hundred\\|100\" NYB_vol2_glossary.txt | head -10\necho \"=== NYB sat ===\"; grep -n \"^sat\\b\\|\\bsat \\[\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T17:54:02.133Z] TOOL RESULT

```
=== NYB sad/sat ===
333:äivenak [’dwynk'] kind, sort, species, genus 478, 3917, 7611, 8028, 9417-20, 1083.10; nature 100!4; — manner: pat han =, pat én ~ in this, in such a manner; being in such a state; thus: 1129-21, 3416, 8519; the thing (event, situation) being so, connected with ditan 21. 322, 917.27, ]]6.14, 123. 1215; with āšnūtan 814, — cë ~ A813, pat ce ~ 1620.21, 788 how?; pat ciš-ic ~ ma 708, pat hec ~ ... ne 792-3 in no way, by no means; pat han ~ ka griyét so that he is weeping 11"; — pat ~ i guaršet like the sun 441?; pat Susr ~ some- thing like a sperm 95!7; pat ēzanišn ~ by (means of) killing 103%; har 2 — in both respects 110%, — MPrs ’ywyng (S, A-H JI), yng (List 80); Paz. dina, ŠGV àinaa, Skr. v. prakära, SGV also vidhà, riti. [MPrth ”dyng, List 79, NP Ginah ‘mirror’ seems to go back to *ä- dayana-]. — Note: — NP ädinah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it (v. above s.v. ātvēn); it probably goes back to MIr *atēnak < Olr *ati-ayana- (OP ati-ay- ‘to go along’), ci MPrs 'dyn ‘entrance’ (S, A-H II), with secondary lengthening of the initial a-: *ādēnay ‘congregation’. — V. also ham-ātvēnak.
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
440:„a thousand times as much as... 10072; ~-susr cand having as much sperm [a bahuvrihi-compound] as 41?! (cf MPrs ’wyn’m ‘of such, or that, name, fame, Sogd. 214-22). - MPrs "nd; Paz. NP and. Probably a secondary formation from cand, q. v.
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
677:āsānēh tranquillity, peace 341+. 70??, 90%; comfort, well-being 907. 941-11, 10029.
706:ast ['st' the bones 50!. 10012; +ast- dahišnan corporeal creatures 5571. — Av. (211 sq.) ast-; MPrs ?st, stg. V. astómand.
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1021:brat [bbt'; "H<Y>] brother, sg. cas. rect. 2471, 10018; after a name as its app.: Zarér i tō ~ 20-24 passim; 221^; after a prep.: hac pus tài brat 221%; — as pl. cas. rect.: vas ~ PH] ... bavend 22"; — sg. cas. obl. brātar [bl”tl] in compounds (v. below); in the sense of a pl. after nume- rals: har 2 brdtar 9%, hàn 4 brätar 9!? (both dir. obj.); — pl. cas. obl. brätarän 826, 21°. 241-5; han i 2 vat-baxt brātarān 9? (dir. obj.). - Av. OP (971 sq.) bratar-, nom. sg. brati; MPrthPrs br'd, cas. obl. br’dr, pl. br’dr’n; Paz. brad; NP birädar.
1040:bun-dahišn [bwndhän'] the laying of foundations — the primordial creation 100%; cas. obl. ~-éh: pat ~-éh 7911. 80? (Paz. bundahašn). — V. dātan.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
=== NYB sat ===
3410:sat-0š [stwš] the state of one just deceased ; theological term expressing the state of the deceased from the moment his life (jan) expires, the soul (ruvän) remaining at the head of the corpse, until the morning of the fourth day when the ruvän leaves this world and, after having been exam- ined, passes across the Cinvat bridge to the other world, “the three-nights-inter- val” (between the existence in this world and the entrance into the beyond) 6411, described 726-7615. — The literal mean- ing of this term was lost early, as shown by the very varying Paz. trans- literations: saduš, sadiš, sadis(a), sediš, sadaš etc. (Mx; Tavadia, Šnš 12). An- klesaria gives in his ed. of Mx (not yet published) sēdēš, which Tavadia (himself reading the Phl form satus) seems to reject. At all events sēdēš is an attempt to harmonize the Paz. reading with the Skr. v. trirdtra, -rin, rendering the termino-
```


## [2026-09-05T17:54:12.441Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY page tag near 11224 ===\"; awk 'NR<=11224' incoming/ARY/ARY_latin_index_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2\necho \"=== ARY page tag near 207 ===\"; awk 'NR<=207' incoming/ARY/ARY_latin_index_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2\necho \"=== PHD page markers near 562 ===\"; awk 'NR>=555 && NR<=565 {print NR\": \"substr($0,1,80)}' PHD.txt"
}
```


### [2026-09-05T17:54:14.262Z] TOOL RESULT

```
=== ARY page tag near 11224 ===
[pdf page 384]
[pdf page 385]
=== ARY page tag near 207 ===
[pdf page 8]
[pdf page 9]
=== PHD page markers near 562 ===
555: rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, 
556: ranjwar 71 rëš
557: ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ip
558: résag 72 rózig
559: rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wou
560: rūz-šabān 73 sān
561: rdz-Saban [YWM, lwc sp’n' | N šabān(a)rēz] day and night. rózwürag [/zvcw
562: sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo 
563: sang 74 sén murw
564: sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-
565: se-pay 75 spas
```


## [2026-09-05T17:54:24.296Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D9%88%D8%B1%D8%B3%D8%A7%D9%86%D8%AA%D8%A7%DA%98/",
 "prompt": "What does the Persian word پورسانتاژ mean and what origin/language tag is given (French pourcentage)? Quote the dictionary entries, especially فرهنگ معین."
}
```


## [2026-09-05T17:54:26.178Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb && mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg115.png data/verification/sources/refs/ocr/BOOK/115.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T17:54:29.772Z] TOOL RESULT

```
# پورسانتاژ (Percentage)

**Origin**: French (pourcentage)

**Meaning**: The word refers to a proportional measurement system based on units of one hundred, or percentage calculations.

## Dictionary Entry - فرهنگ معین:

"[ فر . ] (اِ. ) = پورسان : ۱ - درصد. ۲ - حق دلالی ، حق العمل"

This translates to: percentage (1) and commission/brokerage fees (2).

**Other definitions** include: "a measurement scale with a unit typically being one hundred" and "the proportion of something relative to one hundred units."
```


### [2026-09-05T17:54:32.088Z] TOOL RESULT

```
total 80
drwxrwxr-x 2 sfmqrb sfmqrb  4096 Sep  5 13:54 .
drwxrwxr-x 3 sfmqrb sfmqrb  4096 Sep  5 13:54 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 70699 Sep  5 13:54 115.png
```


## [2026-09-05T17:54:39.193Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱm̥tóm\" \\\n \"https://en.wiktionary.org/wiki/دویست\" \\\n \"https://en.wiktionary.org/wiki/صد\" \\\n \"https://en.wiktionary.org/wiki/قنطار\" \\\n \"https://www.etymonline.com/word/hectare\" \\\n \"https://www.etymonline.com/word/hundred\" \\\n \"https://www.etymonline.com/word/percent\" \\\n \"https://abadis.ir/fatofa/پورسانتاژ/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 115, root Dekm part 2 (hundred/kmtom): root, Avestan sata/duye-saite, Persian sad/devist, Arabic-Persian qentar, hectare, hundred, percent, pursantaz\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T17:54:45.857Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0da309370f18377b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb14480aefcfea5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0fb5c8b5c1c9180.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54bdc1f793f3e694.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34d6d06ff77b92fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa3fac60aea0e6a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/02c8d7a5429cdceb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c78e2e603e20a3ee.txt
```


## [2026-09-05T17:54:52.821Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN hectare/hecto ===\"; grep -n \"hectare\\|hecto-,\" KLN_1966.txt | head -5\necho \"=== KLN hundred ===\"; grep -n \"^hundred,\\|hundred,  n\" KLN_1966.txt | head -5\necho \"=== KLN centimeter ===\"; grep -n \"centimeter\\|centimetre\" KLN_1966.txt | head -3\necho \"=== SKT hundred ===\"; grep -n \"hundred, a\\|HUNDRED\" SKT.txt | head -5"
}
```


### [2026-09-05T17:54:52.922Z] TOOL RESULT

```
=== KLN hectare/hecto ===
3373:L.  area,  ‘vacant  piece  of  ground’.  See  next  word and  cp.  the  second  element  in  hectare, area,  n.  —  L.,  ‘vacant  piece  of  ground,  building, plot’,  rel.  to  arere,  ‘to  become  dry’,  hence  area orig.  meant  ‘a  place  burned  down,  a  dry,  bare  pla¬ ce’  ;  see  ardent  and  cp.  areola,  debonair.  For  sense development  cp.  G.  Esse,  ‘chimney,  forge , which  also  derives  fr.  I.-E.  base  *&s-,  ‘to  burn’. Areca,n.,  a  genus  of  palms  of  Asia  and  the  Malay Archipelago  ( hot .)  —  ModL.,  fr.  Port,  areca,  fr. Malayalam  ddakka ,  fr.  Tamil  adaikdy,  lit. ‘having  close  clusters  of  nuts’,  fr.  ddai,  close arrangement  of  the  cluster’,  and  kay,  ‘nut’.  See OED.  and  Yule-Burnell,  Hobson-Jobson,  p.35. Arecaceae,  n.  pi.,  a  family  of  plants,  the  palm family  (bot.)  —  ModL.,  formed  fr.  prec.  word with  suff.  -aceae.
17398:heckle,  tr.  v.,  1)  to  hackle;  2)  to  embarrass  the speaker  with  questions.  —  ME.  hekelen,  fr. hekele,  ‘an  instrument  for  cleansing  and  carding flax  or  hemp’.  See  hatchcl  and  cp.  hackle. Derivatives:  heck-ler,  n.,  heckl-ing,  n. hect-,  form  of  hecto-  before  a  vowel, hectare,  n.,  a  surface  measure  containing  100 ares.  —  F.,  lit.  ‘a  hundred  ares’,  a  hybrid  coined in  1 795  by  a  decree  of  the  French  National  Con¬ vention  fr.  Gk.  £xax6v,  ‘a  hundred’,  and  L. area,  ‘a  vacant  piece  of  ground’.  See  hecto-  and are,  ‘a  square  unit’.
17401:hecto-,  before  a  vowel  hect-,  combining  form meaning  ‘a  hundred’.  —  F.  hecto-,  hect-,  arbi¬ trarily  shortened  fr.  Gk.  £xax6v,  ‘a  hundred’ (see  hecatomb);  introduced  by  the  French  Natio¬ nal  Convention.
=== KLN hundred ===
18249:hundred,  n.  —  ME.  hundred,  honderd,  fr.  Late OE.  hundred,  prob.  fr.  ON.  hundrad  (whence also  Dan.  hundrede,  Swed.  hundrade,  hundra), lit.  ‘the  number  of  hundred’,  fr.  Teut.*hunda-, ‘hundred’  (seen  also  in  OE.,  OS.,  Goth,  hund, OHG.  hunt),  and  *-rad,  ‘reckoning,  number’, (seen  in  Goth,  rapjo,  "a  reckoning,  account, number’,  ga-rapjan,  ‘to  count’,  sec  reason);  cp. OS.  hunderod  (whence  MLG.,  MHG.,  G.  hun- dert,  MDu.  hondert,  honderd  (Du.  honderd). Teut.  *hunda-,  'hundred',  corresponds  to  I.-E. *kmto-,  which  appears  in  OI.  satam,  Avestic satfm  [OSlav.  suto  (Russ,  sto),  is  prob.  an Iranian  loan  word],  Toch.  A  kant,  B  kante, kante,  Gk.  i-y.% tov,  L.  centum,  Lith.  simtas, Lett,  simts,  Olr.  cet,  W.  cant,  Bret,  kant,  Co. kans,  ‘hundred’.  I.-E.  *kmto-,  ‘hundred’,  orig. meant  'ten  tens’,  fr.  *kmt-,  'ten',  which  also appears  in  the  Latin  ending  -ginti,  -gintd (in  viginti,  ‘twenty’,  triginta,  ‘thirty’,  quadra- ginta,  ‘forty’,  etc.),  in  the  Greek  ending  -xovtoc (in  Tpi«xovT<x,  ‘thirty’,  Tcaoap&xovTa,  ‘forty’,
=== KLN centimeter ===
2787:Derivatives:  angri-ly,  adv.,  angri-ness,  n. angstrom  unit,  angstrom,  n.,  unit  of  length  equal to  one  hundred-millionth  of  a  centimeter;  used to  measure  the  wavelengths  of  light.  —  Named after  the  Swedish  physicist  Anders  Jonas  Ang¬ strom  (1814-1874).
4420:Barabbas,  masc.  PN.  —  L.,  fr.  Gk.  BapappSp,  fr. Aram,  bar  abba,  ‘son  of  the  father,  son  of  the master',  fr.  bar,  ‘son’,  which  is  rel.  to  Heb.  ben, ‘son’,  and  fr.  Aram,  abbd,  ‘the  father’,  emphatic state  of  abh,  which  is  rel.  to  Heb.  abh,  ‘father’. For  the  first  element  sec  ben,  ‘son’,  and  cp.  bar mitzvah  and  words  there  referred  to.  For  the second  element  see  Aboth  and  cp.  Abba,  abbot, barad,  n.,  the  unit  of  pressure  in  the  centimeter- gram-second  system  (physics).  —  Fr.  Gk.  Papop, ‘weight’.  See  baro-.
6973:centiliter,  centilitre,  n.  —  F.  centilitre,  compound¬ ed  of  centi-  and  litre.  See  centi-  and  liter, centillion,  n.  —  Formed  fr.  centi-  on  the  analogy of  million  (q.v.)  See  also  billion, centime,  n.  —  F.,  formed  fr.  cent,  ‘a  hundred’,  on the  analogy  of  decime,  ‘one  tenth  (of  a  franc)’, fr.  L.  decima  (pars),  ‘tenth  (part)’,  fr.  decern, ‘ten’.  See  cent,  ‘a  hundred’,  and  decimal, centimeter,  centimetre,  n.  —  F.  centimetre,  com¬ pounded  of  centi-  and  metre.  See  centi-  and -meter.
=== SKT hundred ===
```


## [2026-09-05T17:55:09.298Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-05T18:01:50.741Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk115.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KMTOM = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱm̥tóm\"\nW_DEVIST = \"https://en.wiktionary.org/wiki/دویست\"\nW_SAD = \"https://en.wiktionary.org/wiki/صد\"\nW_QENTAR = \"https://en.wiktionary.org/wiki/قنطار\"\nE_HECTARE = \"https://www.etymonline.com/word/hectare\"\nE_HUNDRED = \"https://www.etymonline.com/word/hundred\"\nE_PERCENT = \"https://www.etymonline.com/word/percent\"\nA_PURSANT = \"https://abadis.ir/fatofa/پورسانتاژ/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Indo-European\", \"words\": \"Dkm-tom, Kmtom : hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"PIE *dḱm̥tóm > *ḱm̥tóm 'hundred', the zero-grade neuter derivative of *deḱm̥ 'ten' (literally '(ten) decad'), with loss of the initial *d- by simplification of the cluster *dḱ- in most branches. Watkins/AHD prints exactly Nourai's two forms: 'Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom'. Pokorny 192 heads the paragraph 'Hierher ḱm̥tóm ‘hundert’ aus *(d)ḱm̥tóm ‘(Zehner)dekade’'. The reduced *ḱm̥tóm is the ancestor of Skt. śatám, Av. satəm, Gk. hekatón, Lat. centum, Goth. hund, Lith. šimtas.\",\n \"derivation_fa\": \"«صد» در همهٔ زبان‌های هندواروپایی از *dḱm̥tóm بازساخته می‌شود که صورت صفرمرتبهٔ (zero-grade) خنثای *deḱm̥ «ده» است، یعنی در اصل «دهگان، دهه». خوشهٔ آغازین *dḱ- در بیشتر شاخه‌ها ساده شده و *ḱm̥tóm به دست آمده است. واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) دقیقاً همین دو صورت را می‌آورد و پوکورنی (ص ۱۹۲) می‌نویسد ḱm̥tóm «صد» از *(d)ḱm̥tóm «دههٔ (ده‌تایی)». ادعای نورایی در این گره درست است.\",\n \"sources\": [W_KMTOM, E_HUNDRED],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dekm (AHD_watkins1985.txt line 362): 'V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom.' — Nourai's box reproduces both forms and the gloss verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192 (POK_01.txt line 2764)\", \"stance\": \"supports\", \"note\": \"'Hierher ḱm̥tóm ,hundert' aus *(d)ḱm̥tóm ,(Zehner)dekade’' followed by ai. śatám, av. satəm, gr. hekatón, lat. centum, got. hund.\"},\n   {\"src\": \"WLD\", \"where\": \"WP. I 785 f. (cited by Pokorny at the foot of the same article)\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line reads 'WP. I 785 f., WH. I 200 f., 327 ff.' for the whole deḱm̥/ḱm̥tóm article.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 745 s.v. hundred (KLN_1966.txt line 18249)\", \"stance\": \"supports\", \"note\": \"'Teut. *hunda-, ‘hundred’, corresponds to I.-E. *kmto- … I.-E. *kmto-, ‘hundred’, orig. meant ‘ten tens’, fr. *kmt-, ‘ten’.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.1 (numerals), consulted for ordering\", \"stance\": \"silent\", \"note\": \"grep 'Av. sata|çatam' in SYN.txt returns nothing usable; Buck's numeral tables are not in the OCR at that point.\"}\n ]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Avestan\", \"words\": \"sata, satam : hundred; dve-sate, duye-saite : two hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. sata- n. 'hundred' (nom.-acc. sg. satəm) is the regular Iranian reflex of PIE *ḱm̥tóm: the palatal *ḱ became Indo-Iranian *ć and then Iranian s (the classic 'satem' change — the branch is in fact named after this very word), and *m̥ > a. Bartholomae, AWb. col. 1557, lists 'j. sata- (, p. ẋata-) neutr. Zw. ‘hundert’'. The dual phrase 'two hundred' is attested as duye saite (Vd. 16.12 'duye °ite kahyāčit … xrafstranąm'), the dual saite of sata- with duye 'two'; Horn (no. 586) cites the same phrase as aw. dvē sāte. Nourai's four forms are thus the stem, the nom.-acc. sg., and the two variant citations of the dual phrase found in Horn and Hübschmann respectively.\",\n \"derivation_fa\": \"اوستایی sata- (خنثی) «صد»، صورت مفرد فاعلی‑مفعولی satəm، بازتاب قاعده‌مند *ḱm̥tóm هندواروپایی است: *ḱ کامی به ć هندوایرانی و سپس به s ایرانی بدل شده (همان دگرگونی «ساتِم» که نام این شاخه از همین واژه گرفته شده) و *m̥ هجایی به a. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۵۵۷) می‌آورد: «j. sata- (p. ẋata-) خنثی، عدد: صد». برای «دویست» صورت مثنّای duye saite در وندیداد ۱۶٫۱۲ آمده و هرن (شمارهٔ ۵۸۶) همان را dvē sāte می‌نویسد؛ هر دو صورتی که نورایی آورده در منابع موجود است. ادعای نورایی درست است.\",\n \"sources\": [W_SAD, W_DEVIST],\n \"ref_check\": [\n   {\"ref\": \"POK:191, 192\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2765 (p. 192): 'ai. śatám, av. satəm (daraus finn. sata, krimgot. sada)'; and line 2767 'vgl. ai. dvi-śatam aus *duwi ḱm̥tóm' — Pokorny's p.191-192 article covers both the root and the Avestan hundred.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1557 (BRT.txt line 25911)\", \"stance\": \"supports\", \"note\": \"'j. sata- (, p. ẋata-) neutr. Zw. ‘hundert’'; the dual at line 25912 'duye °ite kahyāčit .. xrafstranąm V.16.12' = duye saite 'two hundred'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 586, p. 131 (HRN.txt line 5256)\", \"stance\": \"supports\", \"note\": \"'duvīst (*duvest) ‘zweihundert’ (du sed). aw. dvē sāte; pāz. dvest (Aogem.); ai. dvē śate ‘zweihundert’.'\"},\n   {\"src\": \"HUB\", \"where\": \"p. 237 (HUB.txt line 8448)\", \"stance\": \"supports\", \"note\": \"'Durch späteren Vokalausfall entstand st aus sat in bīst ‘zwanzig’ = zd. visaiti und duvest ‘zweihundert’ = zd. duyē saite.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm\", \"stance\": \"supports\", \"note\": \"'5. Avestan satam, hundred: SATEM.'\"}\n ]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"dwyst : two hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian δwyst (Christian script), read δōwist / δwēst 'two hundred', continues the same Old Iranian dual phrase *duwaya-śatai as Avestan duye saite: the intervocalic *s of the second member is preserved, the unstressed vowel between the two members is lost, and the outcome is a single univerbated word. Gharib's Sogdian Dictionary (entry 3716) prints the etymology in exactly these terms, and the Buddhist-script spelling δwy100 (entry 3713, the numeral written with the figure) shows the word was still felt as 'two × hundred'. New Persian دویست continues an identical formation independently.\",\n \"derivation_fa\": \"سغدی δwyst (به خط سریانی/مسیحی) که δōwist / δwēst خوانده می‌شود، دنبالهٔ همان ترکیب مثنّای ایرانی باستان *duwaya-śatai است که در اوستایی duye saite شده: واکهٔ میانی افتاده و دو جزء یک واژه شده‌اند. غریب در «فرهنگ سغدی» (مدخل ۳۷۱۶، ص ۱۴۶–۱۴۷) ریشه را صریحاً «< اوستایی duye-saite» می‌دهد. صورت بودایی δwy۱۰۰ (مدخل ۳۷۱۳) نشان می‌دهد واژه هنوز «دو×صد» احساس می‌شده است. «دویست» فارسی نو نیز همین ساخت را مستقلاً ادامه داده است. ادعای نورایی درست است.\",\n \"sources\": [W_DEVIST],\n \"ref_check\": [\n   {\"ref\": \"SOD:147\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 3716 (SOD_pages.txt line 14353, form-feed leaf 212 ≈ printed p. 146/147): 'δwyst C — δōwist, δwēst (δwy100) ©<Av. duye-saite ⇒δwyst — two hundred. STii 1.82; SCE 561; BSTBL, Padm. 45; GMS 1316'. Exactly Nourai's arrow Avestan duye-saite → Sogdian dwyst.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 3713 and 3716 (SOD_pages.txt lines 14341, 14353)\", \"stance\": \"supports\", \"note\": \"3713 'δwy100 B => δwyst' (numeral spelling) and 3716 as quoted; index at line 39781 'two hundred 661, 3716'.\"},\n   {\"src\": \"HUB\", \"where\": \"p. 237\", \"stance\": \"supports\", \"note\": \"gives the parallel Persian development duvest = zd. duyē saite, i.e. the same Old Iranian phrase behind both Sogdian and Persian.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese\", \"stance\": \"silent\", \"note\": \"grep for 'dwyst' in ISS_alt_DKS.txt gives no hit; Khotanese has sata- but no relevant compound.\"}\n ]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"sad «صد» : hundred; devîst «دویست» : two hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP صد sad < MP sad (written with the ideographic figure 100 in Book Pahlavi; MacKenzie p. 73 'sad [100 | M sd, N ~] hundred'), from OIr. *śatam = Av. satəm, OP *θatam, PIE *ḱm̥tóm; Iranian s- was later written with ص (rather than س) in Persian orthography, probably to avoid confusion with شد šod in unpointed manuscripts, so the Arabic-looking spelling is not a sign of an Arabic loan. NP دویست devīst < MP duwēst < Av. duye saite; Hübschmann (p. 237) explains the final -st as st from -sat after the loss of the medial vowel, exactly as in بیست bīst 'twenty' < *vīsati; Horn (no. 586) notes that the older pronunciation must have been duvest with majhūl ē, later raised to ī, which is why the word is spelled دویست but pronounced devīst.\",\n \"derivation_fa\": \"«صد» از فارسی میانهٔ sad (که در پهلوی کتابی با هُزوارش/رقم ۱۰۰ نوشته می‌شد؛ مکنزی، فرهنگ کوچک پهلوی، ص ۷۳)، از ایرانی باستان *śatam = اوستایی satəm، پارسی باستان *θatam، و هندواروپایی *ḱm̥tóm. نوشتن آن با «ص» به جای «س» املای قراردادی فارسی است — احتمالاً برای پرهیز از خلط با «شد» در متون بی‌نقطه — و نشانهٔ معرّب بودن نیست. «دویست» از فارسی میانهٔ duwēst و آن از اوستایی duye saite است؛ هوبشمان (ص ۲۳۷) می‌گوید st پایانی از sat- پس از افتادن واکهٔ میانی پدید آمده، درست مانند «بیست» از *vīsati. هرن (شمارهٔ ۵۸۶) می‌افزاید که تلفظ کهن‌تر duvest با «ای مجهول» بوده که در فارسی نو به ī کشیده بدل شده است. ادعای نورایی درست است.\",\n \"sources\": [W_SAD, W_DEVIST],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page for BQT here. صد and دویست fall in Borhan vol. 3 (ش–ل), which exists on disk only as un-OCR'd page scans (BQT_v3_pages.txt has no usable text for these headwords; grep 'دویست' in BQT_v1/v2_pages.txt returns only running-text occurrences, e.g. BQT_v2_pages.txt line 22784). Without a cited page the claim could not be pinned to a specific Borhan entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 73 s.v. sad (PHD.txt line 562)\", \"stance\": \"supports\", \"note\": \"'sad [100 | M sd, N ~] hundred' — MacKenzie confirms MP sad, Manichaean MP sd, NP identical.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 725 (HRN.txt lines 6347-6349) and no. 586 (line 5256)\", \"stance\": \"supports\", \"note\": \"'sed … ‘hundert’. aw. sata- ‘hundert’; phlv. sat; ai. śatá-; kurd. sed; afγ. sal, sil; oss. sädä; waχ. sar.' and 'duvīst (*duvest) ‘zweihundert’ (du sed). aw. dvē sāte.'\"},\n   {\"src\": \"HUB\", \"where\": \"p. 237 (HUB.txt line 8448)\", \"stance\": \"supports\", \"note\": \"'duvest ‘zweihundert’ = zd. duyē saite'.\"},\n   {\"src\": \"ARY\", \"where\": \"printed p. 386 (ARY_latin_index_pages.txt, [pdf page 385], line 11224)\", \"stance\": \"supports\", \"note\": \"Aryanpur's cognate table under HUNDRED lists 'SATA (KHOTANESE), SATAM, SHATA (SANSKRIT), HEKATON, EKATO (GREEK), CENTUM (LATIN), HUNDA (GOTHIC)' — the same family, with the Persian word at its head.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab/abadis entry for صد\", \"stance\": \"silent\", \"note\": \"the MON OCR on disk (MON_part1/part2) has no clean صد headword entry; grep 'هکتار|قنطار' finds those but not صد.\"}\n ]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Greek\", \"words\": \"hektaton : hundred\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Greek word for 'hundred' is ἑκατόν hekatón, not *hektaton. The printed page (pdf 115, book p. 85) really does read 'hektaton : hundred', so the extraction is faithful and the error is Nourai's own misprint — a transposed -t-. Substantively the node is right: ἑκατόν continues *ḱm̥tóm with the prothetic/dissimilated first syllable he- (Watkins and Pokorny both explain it as a dissimilation of *sem-ḱm̥tóm 'one hundred', with *sem- 'one' giving Gk. he-), the labiovelar-free palatal *ḱ giving Gk. k, and *m̥ > a. It is this word, in the shortened form hecto-, that the French National Convention used in 1795 to build hectare, so the arrow to French is correct.\",\n \"derivation_fa\": \"واژهٔ یونانی «صد» ἑκατόν hekatón است، نه hektaton. تصویر صفحهٔ چاپی (صفحهٔ ۱۱۵ پی‌دی‌اف، صفحهٔ ۸۵ کتاب) نشان می‌دهد که خود کتاب «hektaton» چاپ کرده است؛ پس خطای خوانش اسکن نیست، بلکه غلط چاپی نورایی است (جابه‌جایی حرف t). محتوای گره درست است: ἑκατόν دنبالهٔ *ḱm̥tóm است با هجای آغازین he- که پوکورنی و واتکینز آن را حاصل ناهمگونی *sem-ḱm̥tóm «یک صد» می‌دانند (*sem- «یک» در یونانی he- می‌شود)، *ḱ کامی به k و *m̥ هجایی به a بدل شده است. همین واژه در صورت کوتاه‌شدهٔ hecto- در ۱۷۹۵ مبنای ساخت hectare در کنوانسیون ملی فرانسه شد؛ پس پیکان آن به فرانسوی درست است. حکم: خطای چاپی کتاب.\",\n \"error_in\": \"book\",\n \"book_prints\": \"hektaton\",\n \"correct_form\": \"hekaton (ἑκατόν)\",\n \"sources\": [W_KMTOM, E_HECTARE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. dekm: '4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-1): HECATOMB, HECTO-.' The cited reference gives hekaton, so it supports the derivation but contradicts the spelling printed in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192 (POK_01.txt line 2766)\", \"stance\": \"partial\", \"note\": \"'gr. ἑκατόν, ark. hekatón (aus dissimil. *sem ḱm̥tom ,ein Hundert’? Schwyzer Gr. Gr. I 592 f.)' — the form is hekatón.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 713 s.v. hecto- (KLN_1966.txt line 17401)\", \"stance\": \"partial\", \"note\": \"'hecto-, before a vowel hect-, combining form meaning ‘a hundred’. — F. hecto-, hect-, arbitrarily shortened fr. Gk. ἑκατόν, ‘a hundred’.'\"},\n   {\"src\": \"ARY\", \"where\": \"printed p. 386\", \"stance\": \"partial\", \"note\": \"Aryanpur's cognate list prints 'HEKATON, EKATO (GREEK)' — again hekaton, never hektaton.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. centum (LAT.txt line ~11137)\", \"stance\": \"partial\", \"note\": \"'got. hund, gr. ἑκατόν' listed as the parallel invariable neuters.\"}\n ]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"hectare : a unit of area\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French hectare is a deliberate metric coinage of 1795, made by decree of the French National Convention: hect(o)- (an arbitrary shortening of Gk. ἑκατόν 'hundred', chosen as the Greek-based multiplier prefix, against the Latin-based sub-multiples deci-, centi-, milli-) + are (from Lat. area 'vacant piece of ground', the base unit of 100 m²). It is therefore a Greek-Latin hybrid meaning 'a hundred ares' = 10,000 m². Nourai's ☞As pointer sends the reader to his root 'As' for the second element, which is correct.\",\n \"derivation_fa\": \"«hectare» فرانسوی واژه‌ای برساختهٔ نظام متری است که در ۱۷۹۵ به فرمان کنوانسیون ملی فرانسه ساخته شد: پیشوند hect(o)- که کوتاه‌شدهٔ قراردادی ἑκατόν یونانی «صد» است (پیشوندهای بزرگ‌کننده را از یونانی و کوچک‌کننده‌ها را از لاتین گرفتند) به‌علاوهٔ are از area لاتین «زمین بایر»، واحد پایه برابر ۱۰۰ مترمربع. پس هکتار یعنی «صد آر» = ۱۰٬۰۰۰ مترمربع و واژه‌ای دورگهٔ یونانی‑لاتین است. ارجاع نورایی به ریشهٔ «As» برای جزء دوم درست است. ادعای نورایی درست است.\",\n \"sources\": [E_HECTARE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 713 s.v. hectare (KLN_1966.txt line 17398)\", \"stance\": \"supports\", \"note\": \"'hectare, n., a surface measure containing 100 ares. — F., lit. ‘a hundred ares’, a hybrid coined in 1795 by a decree of the French National Convention fr. Gk. ἑκατόν, ‘a hundred’, and L. area, ‘a vacant piece of ground’.'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 128 s.v. area (KLN_1966.txt line 3373)\", \"stance\": \"supports\", \"note\": \"'L. area, ‘vacant piece of ground’. See next word and cp. the second element in hectare.'\"}\n ]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"hectâr «هکتار» : hectare (extra: هکتولیتر ، هکتومتر)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian هکتار hektār is a 20th-century loan straight from French hectare, taken over with the metric system; the French final -e is dropped and the stressed -a- rendered as long ā, giving hek-tār. Mo'in's Farhang-e Fārsi glosses it 'واحد … مقیاس سطح، صد آر = یک هکتومتر مربع' and prints the French source spelling 'hectare' beside the headword. The same French series gave Persian هکتومتر (Mo'in: 'hectomètre … واحدی برای سنجش طول = ۱۰۰ متر') and هکتولیتر, which are the two extra words in Nourai's box; all three entered Persian through French technical and school vocabulary, not through English.\",\n \"derivation_fa\": \"«هکتار» وام‌واژه‌ای است که در سدهٔ بیستم همراه با نظام متری مستقیماً از فرانسوی hectare گرفته شده؛ ـه پایانی فرانسوی افتاده و a تکیه‌بر به «ا» کشیده بدل شده است. معین در «فرهنگ فارسی» ذیل «هکتار» صورت فرانسوی hectare را می‌آورد و آن را «واحد … مقیاس سطح، صد آر = یک هکتومتر مربع» معنی می‌کند. دو واژهٔ افزودهٔ نورایی، «هکتومتر» و «هکتولیتر»، از همان سلسلهٔ فرانسوی‌اند؛ معین «هکتومتر» را نیز با ضبط hectomètre و معنی «واحدی برای سنجش طول = ۱۰۰ متر» آورده است. راه ورود، فرانسوی است نه انگلیسی. ادعای نورایی درست است.\",\n \"sources\": [E_HECTARE],\n \"ref_check\": [\n   {\"ref\": \"MON:5159\", \"status\": \"supports\", \"note\": \"Mo'in's entry found in the local OCR (MON_part2.txt line 90677): 'هکتار: hectare (اِ.) واحد برابر مقیاس سطح صد آر - یک هکتومتر مربع'; the neighbouring entry (line 90678) is 'هکتومتر: hectomètre (اِمر.) واحدی برای سنجش طول = ۱۰۰ متر'. The page number 5159 could not be verified because the OCR carries no page tags, but the entry and the French source tag are exactly as Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 90677-90679 (headwords هکتار, هکتومتر)\", \"stance\": \"supports\", \"note\": \"as quoted above; Mo'in prints the Latin-script French etymon next to each headword.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 713 s.v. hectare\", \"stance\": \"supports\", \"note\": \"confirms that the ultimate donor of every European form is F. hectare, coined 1795.\"}\n ]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"hectare\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English hectare is attested from 1817, borrowed unchanged from French hectare; the spelling and the metric value (100 ares = 10,000 m²) were taken over with the French unit itself as the metric system spread after the Napoleonic period. English never built the word from Greek independently — the -are element is French, and the pronunciation with final -air/-ar preserves the French shape.\",\n \"derivation_fa\": \"«hectare» انگلیسی از سال ۱۸۱۷ به‌کار رفته و بی‌هیچ تغییری از فرانسوی hectare وام گرفته شده است؛ املا و مقدار واحد (صد آر = ۱۰٬۰۰۰ مترمربع) همراه با خودِ واحد فرانسوی و در پی گسترش نظام متری پس از دورهٔ ناپلئون وارد انگلیسی شد. انگلیسی این واژه را مستقیماً از یونانی نساخته است؛ جزء -are فرانسوی است. ادعای نورایی درست است.\",\n \"sources\": [E_HECTARE],\n \"ref_check\": [\n   {\"ref\": \"AHD:609\", \"status\": \"not_checked\", \"note\": \"AHD:609 is a page of the main New College Edition dictionary (1975/76), not of the Indo-European appendix; only the Watkins appendix (AHD_watkins1985.txt) is on disk, and the New College scans on archive.org are lending-only. The substance is confirmed by Klein and Etymonline instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 713 s.v. hectare (KLN_1966.txt line 17398)\", \"stance\": \"supports\", \"note\": \"Klein gives the English headword and derives it '— F., lit. ‘a hundred ares’, a hybrid coined in 1795 by a decree of the French National Convention'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep 'hectare' in SKT.txt returns nothing; Skeat does not treat modern metric coinages.\"}\n ]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"hecto- : hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English hecto- (before a vowel hect-) is the metric multiplier prefix '×100', taken over from French hecto-, which the National Convention formed by arbitrarily clipping Gk. ἑκατόν 'hundred' to a two-syllable prefix on the model of deca-, kilo-. It is therefore not a native Greek combining form (Greek itself used hekato-, as in hekatombē 'sacrifice of a hundred oxen') but a French metric invention out of Greek material — Nourai's arrow from the Greek box is right as a statement of the source material.\",\n \"derivation_fa\": \"پیشوند hecto- (پیش از واکه hect-) در انگلیسی، پیشوند ضرب‌کنندهٔ متری «×۱۰۰» است و از فرانسوی hecto- گرفته شده؛ کنوانسیون ملی فرانسه آن را با کوتاه‌کردن قراردادی ἑκατόν یونانی به یک پیشوند دوهجایی، به قیاس deca- و kilo-، ساخت. پس این پیشوند صورت اصیل یونانی نیست (یونانی خود hekato- به کار می‌برد، مانند hekatombē «قربانی صد گاو») بلکه ساختی فرانسوی از مادهٔ یونانی است. پیکان نورایی از جعبهٔ یونانی، به‌عنوان بیان خاستگاه مادّه، درست است.\",\n \"sources\": [E_HECTARE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 713 s.v. hecto- (KLN_1966.txt line 17401)\", \"stance\": \"supports\", \"note\": \"'hecto-, before a vowel hect-, combining form meaning ‘a hundred’. — F. hecto-, hect-, arbitrarily shortened fr. Gk. ἑκατόν, ‘a hundred’ (see hecatomb); introduced by the French National Convention.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm\", \"stance\": \"supports\", \"note\": \"'4. Greek hekaton, a hundred …: HECATOMB, HECTO-.' — HECTO- is listed among the English words derived from Gk. hekaton.\"}\n ]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Germanic\", \"words\": \"hundan : hundred\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Proto-Germanic word for 'hundred' is a neuter *hundą (older notation *hundam / *hunda-), from PIE *ḱm̥tóm by Grimm's Law (*ḱ > *h) and the regular *m̥ > un; it survives as Goth. hund, OS/OE hund, OHG hunt. Nourai's cited source, Watkins/AHD, prints 'Germanic *hundam'; Klein prints 'Teut. *hunda-'; Wiktionary reconstructs *hundą, where the ogonek stands for the nasalized vowel that older handbooks wrote -an or -am. The book's 'hundan' is therefore a defensible older transcription of the nasal ending rather than a real error, but it matches none of the three standard notations exactly, so the node is plausible rather than confirmed.\",\n \"derivation_fa\": \"صورت ژرمنی آغازین «صد» یک اسم خنثای *hundą است (در ضبط‌های کهن‌تر *hundam یا *hunda-) که از *ḱm̥tóm هندواروپایی با قانون گریم (*ḱ > *h) و تحول قاعده‌مند *m̥ > un پدید آمده؛ بازماندهٔ آن گوتی hund، ساکسونی و انگلیسی باستان hund و آلمانی علیای باستان hunt است. مأخذ خودِ نورایی، یعنی واتکینز، *hundam می‌نویسد؛ کلاین *hunda-؛ ویکی‌واژه *hundą که در آن نشانهٔ زیرین همان واکهٔ خیشومی است که کتاب‌های قدیمی -an یا -am می‌نوشتند. پس «hundan» کتاب ضبط کهنه‌ای از پایانهٔ خیشومی است، نه غلط آشکار، ولی با هیچ‌یک از سه ضبط استاندارد دقیقاً یکی نیست. حکم: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_KMTOM, E_HUNDRED],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. dekm: '1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED.' The derivation is Nourai's, but the cited reference spells the form *hundam, not *hundan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192 (POK_01.txt line 2769)\", \"stance\": \"supports\", \"note\": \"'got. as. ags. hund, ahd. hunt ,100’ (in Kompositis von 200 ab)' — Pokorny cites only the attested forms, no starred Germanic.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 745 s.v. hundred (KLN_1966.txt line 18249)\", \"stance\": \"partial\", \"note\": \"'fr. Teut. *hunda-, ‘hundred’ (seen also in OE., OS., Goth. hund, OHG. hunt)' — stem form *hunda-, not *hundan.\"},\n   {\"src\": \"WLD\", \"where\": \"WP. I 785 f.\", \"stance\": \"supports\", \"note\": \"cited by Pokorny for the whole ḱm̥tóm paragraph including the Germanic reflexes.\"}\n ]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"OE hund 'hundred' was in late Old English extended to hundred, a compound of hund + *rad 'reckoning, number' (Goth. rapjō 'a reckoning, account', ga-rapjan 'to count'; PIE *ré-/ar- 'to reason, count'), probably on the model of ON hundrað. The compound displaced simple hund entirely in Middle English (ME hundred, honderd), so that Modern English hundred literally means 'a count of hundred'. Nourai's arrow Germanic → English is right, but the box hides the second element, which is not from this root at all.\",\n \"derivation_fa\": \"«hund» انگلیسی باستان به معنی «صد» بود؛ در اواخر دورهٔ انگلیسی باستان به hundred گسترش یافت که ترکیبی است از hund + ‏*rad «شمار، شمارش» (گوتی rapjō «حساب»، ga-rapjan «شمردن»؛ از ریشهٔ هندواروپایی *ar-/rē- «شمردن»)، احتمالاً به قیاس نروژی باستان hundrað. این ترکیب در انگلیسی میانه (hundred, honderd) جای hund ساده را کاملاً گرفت، چنان‌که hundred امروزی تحت‌اللفظی یعنی «شمارِ صد». پیکان نورایی از ژرمنی به انگلیسی درست است، ولی جعبه جزء دومِ واژه را نشان نمی‌دهد که اصلاً از این ریشه نیست.\",\n \"sources\": [E_HUNDRED],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent Germanic box carries AHD, which does cover the English word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 745 s.v. hundred (KLN_1966.txt line 18249)\", \"stance\": \"supports\", \"note\": \"'ME. hundred, honderd, fr. Late OE. hundred, prob. fr. ON. hundrað … lit. ‘the number of hundred’, fr. Teut. *hunda-, ‘hundred’ … and *-rad, ‘reckoning, number’ (seen in Goth. rapjo).'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm and s.v. ar-\", \"stance\": \"supports\", \"note\": \"'Old English hundred, hundred (-red, from Germanic *radam, number; see ar-)'; and s.v. ar- 'Zero-grade form *ra- in Germanic *radam, number (see dekm)'.\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192\", \"stance\": \"supports\", \"note\": \"'an. hund-rað (zu got. rapjan ,zählen’) ,Großhundert’ (,120’), daraus ags. hundred; mhd. nhd. hundert aus as. hunderod'.\"}\n ]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Latin\", \"words\": \"centum, centenarium : hundred; per-centum : by hundred\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Lat. centum 'hundred' is the regular Italic reflex of *ḱm̥tóm (Proto-Italic *kəntom): the palatal *ḱ merged with plain velar k (the 'centum' merger that named the western branch), and *m̥ gave en before a stop. It is an indeclinable neuter, like mille. From it Latin built the adjective centēnārius 'consisting of a hundred, weighing a hundred pounds' (Ernout-Meillet: 'centēnārius: qui centum (centenas) partes habet'), used substantivally as centēnārium, the hundredweight — this is the form that later travelled east into Greek and Arabic in node 17. per centum 'by the hundred' is not a Classical Latin compound but a Modern Latin phrase abstracted from Italian commercial per cento; Nourai's hyphenation makes it look like an ancient univerbation, which it is not.\",\n \"derivation_fa\": \"«centum» لاتین بازتاب قاعده‌مند *ḱm̥tóm در ایتالیایی آغازین (*kəntom) است: *ḱ کامی با k ساده یکی شده (همان ادغام «کنتوم» که نام شاخهٔ غربی از آن گرفته شده) و *m̥ هجایی پیش از انسدادی به en بدل شده است. این واژه مانند mille اسمی خنثی و غیرمنصرف است. از آن صفت centēnārius «صدتایی، به وزن صد رطل» ساخته شد (ارنو–مه‌یه: «centēnārius: qui centum (centenas) partes habet») که در کاربرد اسمی centēnārium یعنی «قنطار» شد — همان صورتی که در گرهٔ ۱۷ به یونانی و سپس عربی راه یافت. اما «per centum» ترکیبی لاتینی کهن نیست، بلکه عبارتی لاتینِ نو است که از per cento تجاری ایتالیایی انتزاع شده؛ خط پیوند نورایی آن را کهن‌تر از آنچه هست می‌نمایاند.\",\n \"sources\": [E_PERCENT, W_KMTOM],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dekm: '3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CENTESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CENTURY; CENTENNIAL, PER CENT, …' — both centum and its centenar-/per cent derivatives are exactly as Nourai draws them.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. centum (LAT.txt lines 11119-11134)\", \"stance\": \"supports\", \"note\": \"'centum (indeclinable): cent. Ancien substantif neutre devenu invariable, comme mille … Dérivés: … centēnārius: ‘qui centum (centenas) partes habet’; d'où à basse époque ‘centenaire’, ἑκατονταετής, et synonyme de centurio.'\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192 (POK_01.txt line 2767)\", \"stance\": \"supports\", \"note\": \"'lat. centum (dazu ducentum, ducentī ,200’, vgl. ai. dvi-śatam aus *duwi ḱm̥tóm …)'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 745 s.v. hundred\", \"stance\": \"supports\", \"note\": \"lists 'L. centum' among the direct reflexes of I.-E. *kmto-.\"}\n ]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A pass-through box with no word printed in it (the printed page shows an empty French box), standing for the French metric and commercial vocabulary built on Latin centum: centi- (the metric sub-multiple prefix, Convention of 1795), centimètre (1801), cent 'hundred', pour cent and pourcentage. It is from this French layer, not from Latin directly and not from English, that the Persian and English children below are taken.\",\n \"derivation_fa\": \"این جعبه واژه‌ای ندارد (در صفحهٔ چاپی نیز جعبهٔ فرانسوی خالی است) و تنها حلقهٔ واسطه است: مجموعهٔ واژگان متری و بازرگانی فرانسوی که بر پایهٔ centum لاتین ساخته شده‌اند — پیشوند centi- (کنوانسیون ۱۷۹۵)، centimètre (۱۸۰۱)، cent «صد»، pour cent و pourcentage. فرزندان فارسی و انگلیسیِ زیر آن از همین لایهٔ فرانسوی گرفته شده‌اند، نه مستقیماً از لاتین و نه از انگلیسی.\",\n \"sources\": [E_PERCENT],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this empty pass-through node; it carries no word to check.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 249 s.v. centimeter, centime (KLN_1966.txt line 6973)\", \"stance\": \"supports\", \"note\": \"'centimeter, centimetre, n. — F. centimètre, compounded of centi- and mètre' and 'centime, n. — F., formed fr. cent, ‘a hundred’' — confirms the French layer between Latin and the modern words.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. centum\", \"stance\": \"supports\", \"note\": \"'Attesté de tout temps. Panroman, sauf roumain. M.L. 1816' — Latin centum survives in all Romance including French cent.\"}\n ]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\", \"words\": \"sântîmetr «سانتیمتر»; pūrsântâž «پورسانتاژ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are French loans of the Pahlavi-to-Qajar modernisation period, taken through French-language schooling and administration. سانتی‌متر sāntimetr < F. centimètre (coined 1801 from centi- + mètre), the French nasal-free -en- of centi- rendered in Persian as -ān- and the final -re as -r. پورسانتاژ pursāntāž < F. pourcentage 'percentage', with the French nasal vowel of -cen- again written سان and the final -age rendered -āž with the characteristic Persian ژ for French /ʒ/; Mo'in tags it [فر.] (French) and glosses it 'درصد' and 'حق دلالی، حق‌العمل', the second sense (commission) being a Persian specialisation not present in French. Neither word passed through Arabic.\",\n \"derivation_fa\": \"هر دو وام‌واژهٔ فرانسوی دورهٔ نوسازی قاجار و پس از آن‌اند و از راه مدرسه و دیوان فرانسوی‌زبان وارد شده‌اند. «سانتی‌متر» از centimètre فرانسوی (ساختهٔ ۱۸۰۱ از centi- و mètre)؛ واکهٔ خیشومی -en- در فارسی «ان» نوشته شده و -re پایانی به «ر» بدل شده است. «پورسانتاژ» از pourcentage فرانسوی؛ باز هم خیشومی -cen- «سان» شده و پسوند -age با «ـاژ» ضبط شده، همان ابدال همیشگی /ʒ/ فرانسوی به «ژ» در فارسی. معین آن را با برچسب [فر.] می‌آورد و «۱- درصد ۲- حق دلالی، حق‌العمل» معنی می‌کند؛ معنی دوم تخصیص معنایی فارسی است و در فرانسوی نیست. هیچ‌یک از راه عربی نیامده است. ادعای نورایی درست است.\",\n \"sources\": [A_PURSANT, E_PERCENT],\n \"ref_check\": [\n   {\"ref\": \"MON:1810\", \"status\": \"supports\", \"note\": \"Mo'in's entry, read through abadis.ir (which reproduces فرهنگ معین): 'پورسانتاژ [فر.] (اِ.) = پورسان: ۱- درصد. ۲- حق دلالی، حق‌العمل' — the [فر.] tag is Mo'in's own mark for a French loan, exactly Nourai's arrow. The page number 1810 could not be checked (the MON OCR on disk carries no page tags and the online text is unpaginated).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir reproduction of فرهنگ معین s.v. پورسانتاژ\", \"stance\": \"supports\", \"note\": \"'[ فر . ] (اِ. ) = پورسان : ۱ - درصد. ۲ - حق دلالی ، حق العمل'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 249 s.v. centimeter (KLN_1966.txt line 6973)\", \"stance\": \"supports\", \"note\": \"'centimeter, centimetre, n. — F. centimètre, compounded of centi- and mètre' — establishes the French etymon of the Persian word.\"}\n ]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"centimeter\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English centimeter/centimetre is a borrowing of French centimètre (first used 1801), itself compounded of the metric sub-multiple prefix centi- (from Lat. centum, chosen by the National Convention for the Latin-based fractions) and mètre. English took the whole word, not the parts, which is why the British spelling keeps the French -re.\",\n \"derivation_fa\": \"«centimeter/centimetre» انگلیسی وام‌گیری کامل از centimètre فرانسوی (نخستین کاربرد ۱۸۰۱) است که خود از پیشوند کسری متری centi- (از centum لاتین؛ کنوانسیون ملی فرانسه کسرها را از لاتین گرفت) و mètre ساخته شده. انگلیسی کل واژه را وام گرفته، نه اجزا را؛ به همین سبب املای بریتانیایی -re فرانسوی را نگه داشته است. ادعای نورایی درست است.\",\n \"sources\": [E_PERCENT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dekm lists CENTI- among the English words derived from Latin centum: '3. Latin centum, hundred: CENT, … CENTESIMAL, CENTI-, CENTIME …'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 249 s.v. centimeter (KLN_1966.txt line 6973)\", \"stance\": \"supports\", \"note\": \"'centimeter, centimetre, n. — F. centimètre, compounded of centi- and mètre. See centi- and -meter.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. centum\", \"stance\": \"supports\", \"note\": \"confirms centum as the base of the centēsim-/centi- derivatives.\"}\n ]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"cent, century, percent, centenary, centennial\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are Latin-based: cent (late 14c.) from Lat. centum, its modern sense 'hundredth part' developing in the 17th c. under the influence of percent and fixed in 1786 as the name of the U.S. coin; century from Lat. centuria 'a group of a hundred' (Pokorny notes centuria as the r-derivative of centum, formed like decuria); centenary from centēnārius, centennial an 18th-c. English formation on centum + annus after biennial; percent from Modern Latin per centum 'by the hundred', 1560s, a bookkeepers' phrase modelled on Italian per cento. Nourai's box lists exactly the English family that Watkins gives under Latin centum.\",\n \"derivation_fa\": \"هر پنج واژه از راه لاتین‌اند: cent (اواخر سدهٔ ۱۴م) از centum لاتین که معنی «یک‌صدم» را در سدهٔ ۱۷م زیر تأثیر percent گرفت و در ۱۷۸۶ نام سکهٔ آمریکایی شد؛ century از centuria لاتین «دستهٔ صدتایی» (پوکورنی centuria را مشتق ـr از centum می‌داند، به قیاس decuria)؛ centenary از centēnārius؛ centennial ساختی انگلیسی از سدهٔ ۱۸م بر پایهٔ centum + annus به قیاس biennial؛ و percent از عبارت لاتینِ نو per centum «به ازای صد» (دههٔ ۱۵۶۰)، اصطلاح دفترداران به قیاس per cento ایتالیایی. فهرست نورایی دقیقاً همان خانوادهٔ انگلیسی است که واتکینز ذیل centum لاتین می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [E_PERCENT],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; its Latin parent carries AHD, which lists this same English family.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm\", \"stance\": \"supports\", \"note\": \"'3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CENTESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CENTURY; CENTENNIAL, PER CENT …' — all five of Nourai's words appear.\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 192 (POK_01.txt line 2773)\", \"stance\": \"supports\", \"note\": \"'Dazu eine r-Ableitung in lat. centuria f. ,Hundertschaft’ (wie decuria)' — the source of century.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, s.v. percentage (SYN.txt lines 20382, 20393)\", \"stance\": \"supports\", \"note\": \"'Pol., Russ. procent … prob. fr. NHG prozent = It. per cento etc. ‘by the hundred, percent’ with substitution of pro, as if Lat. pro centum' — confirms per centum is a modern commercial formation.\"}\n ]})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Greek\", \"words\": \"kentmnarion : of a hundred\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The word is Byzantine Greek κεντηνάριον kentēnárion 'hundredweight, a weight/sum of a hundred (pounds, pounds of gold)'; the printed page (pdf 115, book p. 85) reads 'kentmnarion', so the extraction is faithful and the odd -mn- is Nourai's own misprint for -ēn- (an m set for an ē/ē-macron). Two things follow. (a) The correct form is kentēnarion. (b) The arrow is drawn from the Indo-European box, but the Greek word is not an inherited Greek reflex at all — it is a Late Greek borrowing of Latin centēnārium (the substantivised centēnārius 'consisting of a hundred'), introduced with Roman fiscal and weight administration; Greek k- for Latin c-, -ē- for Latin -ē-, and the neuter -arion for -ārium are the regular loan correspondences. Jeffery, Klein and Wiktionary all state this explicitly. The node therefore belongs under the Latin box (#12 centenarium), not directly under IE *Kmtom.\",\n \"derivation_fa\": \"واژهٔ مورد نظر یونانی بیزانسی κεντηνάριον kentēnárion «قنطار، وزن یا مبلغ صدتایی (صد رطل، صد لیترهٔ زر)» است. صفحهٔ چاپی (ص ۱۱۵ پی‌دی‌اف، ص ۸۵ کتاب) «kentmnarion» دارد؛ پس خطای خوانش اسکن نیست و -mn- غلط چاپی خودِ نورایی به جای -ēn- است (حرف m به جای ē). دو نکته در پی می‌آید: نخست، صورت درست kentēnarion است. دوم، این واژه بازماندهٔ ارثی یونانی از *ḱm̥tóm نیست، بلکه وام‌واژه‌ای است که یونانی متأخر از centēnārium لاتین (صورت اسمی‌شدهٔ centēnārius «صدتایی») همراه با نظام مالیاتی و اوزان رومی گرفته است؛ k یونانی در برابر c لاتین، ē در برابر ē، و پسوند خنثای -arion در برابر -ārium همگی معادل‌های قاعده‌مند وام‌گیری‌اند. جفری، کلاین و ویکی‌واژه هر سه این را صریح می‌گویند. بنابراین جای درست این گره زیر جعبهٔ لاتین (#۱۲ centenarium) است، نه مستقیماً زیر *Kmtom هندواروپایی.\",\n \"error_in\": \"book\",\n \"book_prints\": \"kentmnarion\",\n \"correct_form\": \"kentēnarion (κεντηνάριον)\",\n \"sources\": [W_QENTAR],\n \"ref_check\": [\n   {\"ref\": \"VDQ:352\", \"status\": \"partial\", \"note\": \"VDQ is Badre'i's Persian translation of Jeffery's FVQ and is only on noorlib, whose viewer is JavaScript-rendered and unreadable by WebFetch; the substance was checked in the original, FVQ pp. 243-44 (FVQ.txt lines 15208-15236): 'Undoubtedly it is the Gk. Κεντηνάριον, which represents the Lat. centenarium, and passed into Aram. as קנטרא, Syr. …'. The reference therefore supports the word and the chain but gives the Greek as a loan FROM Latin, not as a direct IE reflex, and spells it kentēnarion.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 243-244 (FVQ.txt line 15234)\", \"stance\": \"partial\", \"note\": \"as quoted: Gk. κεντηνάριον 'represents the Lat. centenarium'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 838 s.v. kantar (KLN_1966.txt line 20538)\", \"stance\": \"partial\", \"note\": \"'fr. Late Gk. κεντηνάριος, representing L. centenarius, ‘consisting of a hundred; weighing a hundred pounds’.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. centum (LAT.txt line 11131)\", \"stance\": \"supports\", \"note\": \"'centēnārius: ‘qui centum (centenas) partes habet’; d'où à basse époque ‘centenaire’ … et synonyme de centurio (cf. centena: centenarii dignitas), M.L. 1810a' — the Latin base of the Greek loan.\"}\n ]})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Aramaic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box (the printed page shows no word) standing for Aramaic קנטרא qenṭārā / Classical Syriac ܩܢܛܝܪܐ qanṭīrā 'hundredweight', the Aramaic adaptation of Gk. κεντηνάριον: Greek k- is rendered by q-, the -t- by emphatic ṭ, and the Greek neuter ending is replaced by the Aramaic emphatic-state -ā. Jeffery cites both the longer Aramaic form and the shortened Syriac one, and it is the shortened Syriac form that Arabic took. Nourai's decision to leave the box wordless loses the actual form but the language and the position in the chain are right.\",\n \"derivation_fa\": \"جعبه‌ای خالی و واسطه است (در صفحهٔ چاپی هم واژه‌ای ندارد) و نمایندهٔ آرامی קנטרא qenṭārā و سریانی کلاسیک ܩܢܛܝܪܐ qanṭīrā «قنطار» است، یعنی صورت آرامی‌شدهٔ κεντηνάριον یونانی: k یونانی به ق، t به طای مُطبَق، و پایانهٔ خنثای یونانی به «ـا»ی حالت مؤکّد آرامی بدل شده است. جفری هم صورت بلند آرامی و هم صورت کوتاه‌شدهٔ سریانی را می‌آورد و می‌گوید عربی از صورت کوتاه سریانی گرفته است. خالی‌گذاشتن جعبه صورت واژه را از خواننده دریغ می‌کند، ولی نام زبان و جای آن در زنجیره درست است.\",\n \"sources\": [W_QENTAR],\n \"ref_check\": [\n   {\"ref\": \"VDQ:352\", \"status\": \"partial\", \"note\": \"checked through the original FVQ pp. 243-44 (VDQ is its Persian translation, same entry order): 'passed into Aram. as קנטרא, Syr. ܩܢܛܝܪܐ. It was from the Aram., as Fraenkel, Vocab, 13; Fremdw, 203, shows, that the word came into Arabic, and in all probability from the shortened Syr. form.' Supports the Greek→Aramaic→Arabic route; the noorlib scan of VDQ itself could not be opened.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 243-244 (FVQ.txt lines 15234-15236)\", \"stance\": \"supports\", \"note\": \"as quoted; Jeffery names Fraenkel, Fremdwörter 203 as the authority.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 838 s.v. kantar (KLN_1966.txt line 20538)\", \"stance\": \"supports\", \"note\": \"'Arab. qintār, fr. Aram. qintār, qintārā, short for qintīnārā, ‘hundred pounds’ … (See S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886, p. 203).'\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel 1886 p. 203 (AFA.txt)\", \"stance\": \"silent\", \"note\": \"grep 'qintar|kintar|centenarium' in AFA.txt returns nothing — the OCR of the Arabic-script headwords on that page is not searchable in transliteration; the passage is however quoted at second hand by both Jeffery and Klein.\"}\n ]})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Arabic\", \"words\": \"qentâr : a unit (100 dinars) for measuring large amounts of jewelry.\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic قنطار qinṭār, plural قناطير qanāṭīr, is a pre-Islamic borrowing from Classical Syriac qanṭīrā (itself from Byzantine Greek κεντηνάριον / Lat. centēnārium). It is a Qur'anic word (3:14 qanāṭīr muqanṭara 'heaped-up hundredweights (of gold and silver)', 3:75, 4:20), and the Arab philologists themselves recognised it as foreign: Abū ʿUbayda stated that the Arabs did not know its meaning, some called it Berber, some Syriac, and the majority held it Greek — which is correct. Its value was never fixed: the lexica give 1200 ūqiya, or 120 raṭl, or 100 raṭl of gold and silver, so Nourai's '100 dinars' is only one of the many figures the tradition reports.\",\n \"derivation_fa\": \"«قنطار» عربی با جمع «قناطیر» وام‌واژه‌ای پیش از اسلام از سریانی کلاسیک qanṭīrā است که خود از یونانی بیزانسی κεντηνάριον و لاتین centēnārium آمده. واژه‌ای قرآنی است (آل‌عمران ۱۴: «القناطیر المقنطرة من الذهب و الفضة»؛ نیز ۳:۷۵ و ۴:۲۰) و خودِ لغویان عرب آن را دخیل می‌دانستند: ابوعبیده گفته است عرب معنای آن را نمی‌دانست؛ برخی آن را بربری و برخی سریانی خواندند و اکثریت یونانی دانستند که همان درست است. مقدارش هرگز ثابت نبود: فرهنگ‌ها ۱۲۰۰ اوقیه، یا ۱۲۰ رطل، یا ۱۰۰ رطل زر و سیم آورده‌اند؛ پس «۱۰۰ دینار»ِ نورایی تنها یکی از چند رقمی است که سنت لغوی گزارش کرده است. ادعای نورایی درست است.\",\n \"sources\": [W_QENTAR],\n \"ref_check\": [\n   {\"ref\": \"MON:2734\", \"status\": \"supports\", \"note\": \"Mo'in's entry (MON_part2.txt line 15151) opens 'قنطار: (قِ) [معر. یو. …]' — the tag معرّب یونانی 'Arabicised from Greek' is Mo'in's own, exactly Nourai's Greek→Arabic claim; the entry goes on 'واحد وزن معادل یک هزار و دویست اوقیه، یا مساوی یکصد و بیست رطل … ج. قناطیر' and lists the variant values including '۴۰۰۰ دینار … ۱۰۰ من و ۱۰۰ رطل و ۱۰۰ مثقال'. The page number 2734 could not be verified (the MON OCR carries no page tags).\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 243-244 (FVQ.txt lines 15205-15236)\", \"stance\": \"supports\", \"note\": \"'It was recognized by the philologers as of foreign origin … the majority were in favour of its being Greek (ath-Thaʿālibī, Fiqh, 318; as-Suyūṭī, Muzhir, i, 134). Undoubtedly it is the Gk. Κεντηνάριον…'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 838 s.v. kantar (KLN_1966.txt line 20538)\", \"stance\": \"supports\", \"note\": \"'Arab. qintār, fr. Aram. qintār, qintārā … fr. Late Gk. κεντηνάριος, representing L. centenarius.'\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 15151-15161\", \"stance\": \"supports\", \"note\": \"as quoted, with the [معر. یو] (Arabicised Greek) tag.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, Alfāẓ fārisiyya muʿarraba\", \"stance\": \"silent\", \"note\": \"grep 'قنطار' in AFM.txt/AFM_pages.txt returns no entry — as expected, since Addi Shir collects Persian, not Greek, loans in Arabic.\"}\n ]})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Persian\", \"words\": \"qentâr «قنطار (قناطیر)» : a measure or container of valuables\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian قنطار qenṭār is a straight loan from Arabic qinṭār, taken with the Arabic broken plural قناطیر qanāṭīr (which Nourai correctly prints in the box), and carrying the Qur'anic overtone of 'heaped wealth'. Nāṣer-e Khosrow's line quoted in the entry — 'از زرد و سرخ مرد بنفریبد / نار است صرّهٔ وی و قنطارش' ('let a man not be deceived by the yellow and the red: his purse and his hundredweight are fire') — is a direct allusion to Q. 3:14 and shows the word fully naturalised in 5th/11th-century Persian verse. Since the ultimate source is Greek/Latin and not Persian, this is not an Arabic-mediated round trip: it is a one-way Greek > Syriac > Arabic > Persian loan.\",\n \"derivation_fa\": \"«قنطار» فارسی وام‌واژه‌ای مستقیم از «قنطار» عربی است که همراه با جمع مکسّر عربی «قناطیر» وام گرفته شده (نورایی هم همان را در جعبه آورده) و بار معنایی قرآنی «مال انباشته» را با خود دارد. بیتی که در مدخل نقل شده، از ناصرخسرو — «از زرد و سرخ مرد بنفریبد / نار است صرّهٔ وی و قنطارش» — اشاره‌ای است آشکار به آیهٔ ۱۴ آل‌عمران و نشان می‌دهد واژه در شعر فارسی سدهٔ پنجم هجری کاملاً جاافتاده بوده است. چون خاستگاه نهایی یونانی‑لاتینی است و نه ایرانی، این‌جا با «رفت‌وبرگشت» فارسی←عربی←فارسی روبه‌رو نیستیم، بلکه با وام‌گیری یک‌سویهٔ یونانی ← سریانی ← عربی ← فارسی. ادعای نورایی درست است.\",\n \"sources\": [W_QENTAR],\n \"ref_check\": [\n   {\"ref\": \"MON:2734\", \"status\": \"supports\", \"note\": \"same Mo'in entry as node 19 (MON_part2.txt lines 15151-15161): headword قنطار with '[معر. یو]', the plural 'ج. قناطیر', and the sense 'پوست گاوی که درون آن را پر زر کرده باشند' — literally 'a hide filled with gold', i.e. Nourai's 'a measure or container of valuables', which is evidently taken straight from Mo'in.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 15151-15161\", \"stance\": \"supports\", \"note\": \"'قنطار: (قِ) [معر. یو] پوست گاوی که درون آن را پر زر کرده باشند. واحد وزن معادل یک هزار و دویست اوقیه … ج. قناطیر.'\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 243-244\", \"stance\": \"supports\", \"note\": \"establishes that the Arabic word from which Persian borrowed is itself Greek via Aramaic, so the Persian word is not a returning Iranian word.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vol. 3 (ق)\", \"stance\": \"silent\", \"note\": \"the ق volume is on disk only as un-OCR'd scans; no searchable قنطار entry was found in BQT_v1/v2_pages.txt.\"}\n ]})\n\nout = {\n \"pdf_page\": 115,\n \"book_page\": 85,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [{\n   \"entry\": 0,\n   \"root\": \"Dekm\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *deḱm̥ 'ten' (Pokorny 191 deḱm̥, deḱm̥t, deḱu-)\",\n   \"note\": \"Part 2 of the Dekm chart, covering only the 'hundred' derivative *(d)ḱm̥tóm. The root box is correct: Pokorny p. 191 heads the article 'deḱm̥, deḱm̥-t, deḱu- ,zehn’' and Watkins/AHD prints 'dekm. Ten. … [Pok. dekm 191]', so root, language label, gloss and page citation all match. Two cross-cutting observations on the chart as drawn. (1) The two Greek boxes both carry misprinted forms in the printed book (hektaton for hekaton, kentmnarion for kentēnarion); the JSON reproduces the page faithfully in both cases, so these are the author's errors, not extraction errors. (2) The lower Greek box (#17 kentēnarion) is hung directly off the Indo-European *Kmtom box, but it is a Late Greek loan from Latin centēnārium, which Nourai himself prints one box higher (#12); Jeffery, Klein and Wiktionary all route it Latin > Greek > Aramaic/Syriac > Arabic. The Iranian side of the chart (Avestan sata-/duye saite > Sogdian dwyst, Persian صد/دویست) is fully confirmed by Bartholomae, Gharib, MacKenzie, Horn and Hübschmann, and is the strongest part of the page.\",\n   \"note_fa\": \"این صفحه بخش دوم نمودار ریشهٔ Dekm است و تنها مشتق «صد»، یعنی *(d)ḱm̥tóm، را می‌پوشاند. جعبهٔ ریشه درست است: پوکورنی در ص ۱۹۱ مدخل را «deḱm̥، deḱm̥-t، deḱu- «ده»» می‌آورد و واتکینز نیز «dekm. Ten … [Pok. dekm 191]»؛ پس نام ریشه، برچسب زبان، معنی و ارجاع صفحه هر چهار درست‌اند. دو نکتهٔ کلی: یکم، هر دو جعبهٔ یونانی در خودِ کتاب غلط چاپی دارند (hektaton به جای hekaton و kentmnarion به جای kentēnarion)؛ داده‌های استخراج‌شده در هر دو مورد به صفحهٔ چاپی وفادارند، پس خطا از نویسنده است نه از خوانش اسکن. دوم، جعبهٔ یونانی پایینی (kentēnarion) مستقیماً زیر *Kmtom هندواروپایی آویخته شده، حال آن‌که وام‌واژه‌ای است از centēnārium لاتین — همان که نورایی خود یک جعبه بالاتر آورده؛ جفری، کلاین و ویکی‌واژه هر سه مسیر را لاتین ← یونانی ← آرامی/سریانی ← عربی می‌دانند. در مقابل، سمت ایرانی نمودار (اوستایی sata- و duye saite ← سغدی dwyst و فارسی «صد»/«دویست») با بارتولومه، غریب، مکنزی، هرن و هوبشمان کاملاً تأیید می‌شود و استوارترین بخش این صفحه است.\",\n   \"sources\": [W_KMTOM, W_SAD, E_HUNDRED],\n   \"ref_check\": [\n     {\"ref\": \"POK:191\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2749 (Pokorny p. 191): 'deḱm̥, deḱm̥-t, deḱu- ,zehn’, Ordinale deḱm̥eino-s, deḱm̥to-s. Ai. dáśa, av. dasa; … gr. δέκα, lat. decem …'; the same article runs on to p. 192 with ḱm̥tóm 'hundert'. Watkins independently tags the root '[Pok. dekm 191]'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm (AHD_watkins1985.txt line 362)\", \"stance\": \"supports\", \"note\": \"'dekm. Ten. I. Basic form *dekm … V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom … [Pok. dekm 191.]'\"},\n     {\"src\": \"WLD\", \"where\": \"WP. I 785 f. (Pokorny's own reference at the end of the article)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny I 785 f. is cited by Pokorny as the source of the whole deḱm̥/ḱm̥tóm treatment.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, s.v. triiokomt- (IEC.txt line 18958)\", \"stance\": \"supports\", \"note\": \"'triioKomt-, -Kmt- ‘thirty’. Cf. treies (triio), tri-, and Kmtom' — Mann too operates with a headword Kmtom, i.e. Nourai's second form is a standard reconstruction.\"},\n     {\"src\": \"ARY\", \"where\": \"printed p. 10 ([pdf page 9], ARY_latin_index_pages.txt line 207) and p. 386\", \"stance\": \"supports\", \"note\": \"Aryanpur's introduction uses this very word for the SATEM/CENTUM split ('SATEM … CENTUM …') and his cognate table under HUNDRED lists SATA, SATAM, HEKATON, CENTUM, HUNDA side by side.\"}\n   ],\n   \"nodes\": nodes\n }]\n}\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-115.json','w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk115.py"
}
```


### [2026-09-05T18:01:53.158Z] TOOL RESULT

```
ok 20
```


## [2026-09-05T18:01:56.559Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-115.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 115"
}
```


### [2026-09-05T18:01:58.398Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 17, 'transcription_suspect': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 7, 'partial': 4}
books consulted: {'supports': 45, 'silent': 7, 'partial': 7} | by book: {'KLN': 16, 'POK': 6, 'MON': 5, 'LAT': 5, 'AHD': 4, 'FVQ': 4, 'HUB': 3, 'WLD': 2, 'SYN': 2, 'HRN': 2, 'ARY': 2, 'BRT': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'PHD': 1, 'SKT': 1, 'AFA': 1, 'AFM': 1, 'BQT': 1}
```


## [2026-09-05T18:02:04.230Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 - <<'EOF'\nimport io\np='data/verification/page-115.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('pūrsântâž «پورسانتاژ»','pŭrsântâž «پورسانتاژ»')\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 tools/verify_archive_sources.py 115 2>&1 | tail -20"
}
```


### [2026-09-05T18:02:06.194Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/page-115.json'
python3: can't open file '/home/sfmqrb/tools/verify_archive_sources.py': [Errno 2] No such file or directory
```


## [2026-09-05T18:02:10.038Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='/home/sfmqrb/git/rishe/data/verification/page-115.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('pūrsântâž «پورسانتاژ»','pŭrsântâž «پورسانتاژ»')\nio.open(p,'w',encoding='utf-8').write(s)\nprint('fixed')\nEOF\npython3 /home/sfmqrb/git/rishe/tools/verify_archive_sources.py 115 2>&1 | tail -20\necho \"--- recheck ---\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 115"
}
```


### [2026-09-05T18:02:12.155Z] TOOL RESULT

```
fixed
8 cited URLs, 0 not yet archived
archived 0, failed 0
--- recheck ---
nodes verified: 20/20
node verdicts: {'confirmed': 17, 'transcription_suspect': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 7, 'partial': 4}
books consulted: {'supports': 45, 'silent': 7, 'partial': 7} | by book: {'KLN': 16, 'POK': 6, 'MON': 5, 'LAT': 5, 'AHD': 4, 'FVQ': 4, 'HUB': 3, 'WLD': 2, 'SYN': 2, 'HRN': 2, 'ARY': 2, 'BRT': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'PHD': 1, 'SKT': 1, 'AFA': 1, 'AFM': 1, 'BQT': 1}
```


## [2026-09-05T18:02:29.532Z] AGENT

Page 115 (book p. 85) verified — 0 PROBLEM lines, all 8 cited URLs archived.

**Counts** — 1 entry (Dekm PART 2), root `confirmed`; 20 nodes: 17 confirmed, 1 plausible, 2 transcription_suspect.

**transcription_suspect (both are the book's own misprints; extraction is faithful — page PNG saved to `data/verification/sources/refs/ocr/BOOK/115.png`)**
- #5 Greek `hektaton` "hundred" → should be **hekaton** (ἑκατόν). Watkins/AHD (Nourai's own ref), Pokorny 192, Klein s.v. hecto- and Aryanpur all print *hekaton*.
- #17 Greek `kentmnarion` "of a hundred" → should be **kentēnarion** (κεντηνάριον); the `m` stands where `ē` belongs.

**plausible**
- #10 Germanic `hundan` — AHD, which Nourai cites, prints \*hundam; Klein \*hunda-; Wiktionary \*hundą. Defensible old notation for the nasal ending, but matches no standard spelling.

**Substantive routing issue (recorded in the entry note and node #17, not counted as disputed)**
- #17 is drawn straight off IE \*Kmtom, but Byzantine Gk. κεντηνάριον is a **loan from Latin centēnārium** — the very form Nourai prints one box up (#12). Jeffery FVQ pp. 243–44, Klein s.v. kantar, and Wiktionary all route Latin > Greek > Syriac qanṭīrā > Arabic qinṭār > Persian قنطار. The node belongs under #12.

**No extraction errors** — the JSON matches the printed page everywhere, including the two misprints, the empty French (#13) and Aramaic (#18) boxes, and all Persian script.

**Strongest links:** Gharib SOD entry 3716 gives "δwyst … ©<Av. duye-saite, two hundred" verbatim; Bartholomae col. 1557 `sata-` n. 'hundert' with the dual `duye saite` (Vd. 16.12); Horn no. 586 and Hübschmann p. 237 for دویست; MacKenzie p. 73 for MP sad. Mo'in's own tag on قنطار is `[معر. یو]` (Arabicised Greek), exactly Nourai's claim.

**Unchecked refs:** BQT (#4 — no page cited, and ص/د fall in the un-OCR'd vol. 3), AHD:609 (main dictionary page, lending-only), VDQ:352 (noorlib viewer is JS-only — verified instead against its original, Jeffery FVQ, same entry order), and MON page numbers 5159/1810/2734 (entries found and quoted, but the OCR carries no page tags).
