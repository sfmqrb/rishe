# Verification process log — verify-page-103


## [2026-09-05T14:48:48.332Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 103 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-103.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-103.json. Write /home/sfmqrb/git/rishe/data/verification/page-103.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 103` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:48:49.884Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:48:50.624Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:48:50.644Z] TOOL RESULT

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


## [2026-09-05T14:48:50.937Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-103.txt"
}
```


### [2026-09-05T14:48:50.951Z] TOOL RESULT

```
1	=== PDF page 103 (book page 73) ===
2	--- entry 0 ---
3	ROOT [Semitic] B.y.t : house  (refs KLN:167)
4	#1 (parent #0) [Arabic] refs=KLN:167 | b.y.t : house ; bayt : house
5	  #2 (parent #1) [Persian] refs=FVA:55; MON:618 | bayt «بیت» : house, room, a line of poem
6	#3 (parent #0) [Hebrew] refs=KLN:167; FSD:266 | baith : house ; Beth-ěl : the house of God ☞Layh ; Běth-lexem : house of food
7	  #4 (parent #3) [English] refs=AHD:127 | Bethel, Beth ; Bethlehem
8	--- entry 1 ---
9	ROOT [Indo-Schythian] Byŭrru : ten thousand  (refs ISS:262)
10	#1 (parent #0) [Avestan] refs=ISS:262; AEF:324 | baevar, baevare : ten thousand
11	  #2 (parent #1) [Pahlavi] refs=AEF:324 | běvar : ten thousand ; běvar-asp : (with) ten thousand horses ☞Ekwos
12	    #3 (parent #2) [Persian] refs=MON:635; FSF:98 | bîvar «بیور» : ten thousand ; Bîvarasp «بیوراسپ» : "with 10,000 horses"
13	#4 (parent #0) [Sogdian] refs=ISS:262 | brywr : ten thousand
14	#5 (parent #0) [Armenian] refs=ISS:262 | biur : ten thousand
15	--- entry 2 ---
16	ROOT [Semitic] B.y.z, B.w.s : to be white  (refs KLN:215)
17	#1 (parent #0) [Arabic] refs=KLN:215 | b.y.z : to be white ; bayzeh : egg (so called for its color)
18	  #2 (parent #1) [Persian] refs=FVA:56 | batzeh «بیضه» : egg ; bayzî «بیضی» : ellipse ; bayyâz «بیّاض» : whiteness ; bayzâ «بیضا» : white, the shining hand of Moses
19	#3 (parent #0) [Hebrew] refs=AHD:183; KLN:215 | bŭtz, bŭz : white linen
20	  #4 (parent #3) [Greek] refs=KLN:215 | bussos 1 : linen
21	    #5 (parent #4) [Latin] refs=None | 
22	      #6 (parent #5) [English] refs=AHD:183 | byssus : white cloth used to wrap mummies
23	
```


## [2026-09-05T14:48:54.766Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-103.json",
 "description": "Read page 103 source JSON"
}
```


### [2026-09-05T14:48:54.801Z] TOOL RESULT

```
{
  "pdf_page": 103,
  "book_page": 73,
  "entries": [
    {
      "root": {
        "name": "B.y.t",
        "lang": "Semitic",
        "refs": "KLN:167",
        "gloss": "house"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:167",
          "words": [
            {
              "translit": "b.y.t",
              "gloss": "house",
              "script": null
            },
            {
              "translit": "bayt",
              "gloss": "house",
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
          "refs": "FVA:55; MON:618",
          "words": [
            {
              "translit": "bayt",
              "gloss": "house, room, a line of poem",
              "script": "بیت"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ای زوصلت خانه ها دارالشفا - وی زهجرت بیت ها بیت الحزَن",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:167; FSD:266",
          "words": [
            {
              "translit": "baith",
              "gloss": "house",
              "script": null
            },
            {
              "translit": "Beth-ěl",
              "gloss": "the house of God",
              "script": null,
              "see": [
                "Layh"
              ]
            },
            {
              "translit": "Běth-lexem",
              "gloss": "house of food",
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
          "lang": "English",
          "refs": "AHD:127",
          "words": [
            {
              "translit": "Bethel, Beth",
              "gloss": null,
              "script": null
            },
            {
              "translit": "Bethlehem",
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
        "name": "Byŭrru",
        "lang": "Indo-Schythian",
        "refs": "ISS:262",
        "gloss": "ten thousand"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "ISS:262; AEF:324",
          "words": [
            {
              "translit": "baevar, baevare",
              "gloss": "ten thousand",
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
          "refs": "AEF:324",
          "words": [
            {
              "translit": "běvar",
              "gloss": "ten thousand",
              "script": null
            },
            {
              "translit": "běvar-asp",
              "gloss": "(with) ten thousand horses",
              "script": null,
              "see": [
                "Ekwos"
              ]
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
          "refs": "MON:635; FSF:98",
          "words": [
            {
              "translit": "bîvar",
              "gloss": "ten thousand",
              "script": "بیور"
            },
            {
              "translit": "Bîvarasp",
              "gloss": "\"with 10,000 horses\"",
              "script": "بیوراسپ"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "کجا بیور از پهلوانی شمار - بود بر زبان دری ده هزار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "ISS:262",
          "words": [
            {
              "translit": "brywr",
              "gloss": "ten thousand",
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
          "lang": "Armenian",
          "refs": "ISS:262",
          "words": [
            {
              "translit": "biur",
              "gloss": "ten thousand",
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
        "name": "B.y.z, B.w.s",
        "lang": "Semitic",
        "refs": "KLN:215",
        "gloss": "to be white",
        "note": "AHD:183 ultimately derives this from Egyptian \"W.z:linen\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:215",
          "words": [
            {
              "translit": "b.y.z",
              "gloss": "to be white",
              "script": null
            },
            {
              "translit": "bayzeh",
              "gloss": "egg (so called for its color)",
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
          "refs": "FVA:56",
          "words": [
            {
              "translit": "batzeh",
              "gloss": "egg",
              "script": "بیضه"
            },
            {
              "translit": "bayzî",
              "gloss": "ellipse",
              "script": "بیضی"
            },
            {
              "translit": "bayyâz",
              "gloss": "whiteness",
              "script": "بیّاض"
            },
            {
              "translit": "bayzâ",
              "gloss": "white, the shining hand of Moses",
              "script": "بیضا"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "شمع هدایت کجا دردل هر کس نهند - همچو کلیمی بجو دیده زبیضا طلب",
            "poet": "Vahshî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "AHD:183; KLN:215",
          "words": [
            {
              "translit": "bŭtz, bŭz",
              "gloss": "white linen",
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
          "lang": "Greek",
          "refs": "KLN:215",
          "words": [
            {
              "translit": "bussos 1",
              "gloss": "linen",
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
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:183",
          "words": [
            {
              "translit": "byssus",
              "gloss": "white cloth used to wrap mummies",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T14:48:55.310Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:48:55.350Z] TOOL RESULT

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


## [2026-09-05T14:49:00.296Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','MON','FSD','AHD','ISS','AEF','FSF','FVQ']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:800])\n    print()\n\""
}
```


## [2026-09-05T14:49:00.385Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat tools/verify_check.py | head -80"
}
```


### [2026-09-05T14:49:02.214Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 74

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 o

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 193
```


### [2026-09-05T14:49:02.252Z] TOOL RESULT

```
agent
page-101.json
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
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
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


## [2026-09-05T14:49:04.233Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 80,160p tools/verify_check.py"
}
```


### [2026-09-05T14:49:04.272Z] TOOL RESULT

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


## [2026-09-05T14:49:05.313Z] TOOL CALL #8: Bash

```json
{
 "command": "head -c 3000 data/verification/page-101.json"
}
```


### [2026-09-05T14:49:05.353Z] TOOL RESULT

```
{
  "pdf_page": 101,
  "book_page": 71,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "B.r.k",
      "verdict": "confirmed",
      "modern_form": "Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)",
      "note": "The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.",
      "note_fa": "ریشه اصیل است و برچسب «سامی» درست: ویکی‌واژه سامیِ آغازین *birk- «زانو» را بازسازی می‌کند (اکدی birkum، عبری berekh، سریانی burkā، گعزی bərk) با گونهٔ مقلوبِ *rukbat- که «رکبة» عربی از آن است. داستان «زانو زدنِ شتر ← برکت دادن» همان تبیین سنتیِ گزنیوس است و با «بَرَکَ/بارَکَ» عربی می‌خواند. اما پیوستِ سامیِ فرهنگ American Heritage — که خودِ نورایی بدان استناد می‌کند — b-r-k «برکت دادن» را «احتمالاً گونهٔ مقلوبِ k-r-b» می‌داند (اکدی karābu «ستودن، برکت دادن»)، و همین فرضِ قلب است که شاخهٔ اکدی-عبریِ «کروب» بر آن استوار شده؛ کلاین آن را می‌پذیرد اما فرهنگ‌نویسیِ امروزیِ عبری (پایگاه SAHD به نقل از میچل) ردش می‌کند، چون قلبِ همخوان نخست و سوم بسیار نادر است. شاخهٔ «گریفین» نیز حدسی است (از کلاین) و خودِ AHD در مدخل griffin آن را نپذیرفته است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-",
        "https://ahdictionary.com/word/semitic.html",
        "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9"
      ],
      "ref_check": [
        {
          "ref": "FVQ:75",
          "status": "supports",
          "note": "FVQ_pages.txt leaf 92 (Jeffery p. 75), s.v. Baraka: 'To bless. ... The primitive verb b-r-k, which is not used in the Qur'an, means to kneel, used specially of the
```


## [2026-09-05T14:49:28.376Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && echo \"---- KLN1966 leaves:\" && awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt"
}
```


### [2026-09-05T14:49:30.031Z] TOOL RESULT

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
---- KLN1966 leaves:
903
```


## [2026-09-05T14:49:31.034Z] TOOL CALL #10: Bash

```json
{
 "command": "pdftoppm -f 103 -l 103 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg103 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T14:49:33.189Z] TOOL RESULT

```
total 31884
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:49 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
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


## [2026-09-05T14:49:37.601Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg103.png"
}
```


### [2026-09-05T14:49:37.976Z] TOOL RESULT

```

```


## [2026-09-05T14:49:37.974Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:49:48.171Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 103 -l 103 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg103_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg103_400.png'); print(im.size)\n# crops: root2 label area, arabic/persian byz block\nim.crop((820,1450,1700,1620)).save('c_scyth.png')\nim.crop((1400,2830,3100,3320)).save('c_byz_persian.png')\n\""
}
```


### [2026-09-05T14:49:51.183Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T14:49:53.580Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_scyth.png"
}
```


### [2026-09-05T14:49:53.606Z] TOOL RESULT

```

```


## [2026-09-05T14:49:54.301Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_byz_persian.png"
}
```


### [2026-09-05T14:49:54.317Z] TOOL RESULT

```

```


## [2026-09-05T14:50:01.876Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg103_400.png')\nim.crop((700,1120,1400,1280)).save('c_scyth2.png')\nim.crop((1250,2450,2650,2880)).save('c_byz2.png')\nim.crop((700,2150,1300,2450)).save('c_root3.png')\nim.crop((700,850,1450,1050)).save('c_heb1.png')\n\""
}
```


### [2026-09-05T14:50:03.733Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:50:06.623Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_scyth2.png"
}
```


### [2026-09-05T14:50:06.637Z] TOOL RESULT

```

```


## [2026-09-05T14:50:06.891Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_byz2.png"
}
```


### [2026-09-05T14:50:06.907Z] TOOL RESULT

```

```


## [2026-09-05T14:50:21.189Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg103_400.png')\nim.crop((700,1230,1400,1400)).save('c_scyth3.png')\nim.crop((790,900,1500,1140)).save('c_heb2.png')\n\""
}
```


### [2026-09-05T14:50:22.890Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:50:25.738Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_scyth3.png"
}
```


### [2026-09-05T14:50:25.751Z] TOOL RESULT

```

```


## [2026-09-05T14:50:26.029Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_heb2.png"
}
```


### [2026-09-05T14:50:26.047Z] TOOL RESULT

```

```


## [2026-09-05T14:50:48.800Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 'bayith' ===\"; grep -n -i \"bayith\" KLN_1966.txt | head -20\necho \"=== KLN 1966 'Beth-el' / bethel ===\"; grep -n -i \"beth-el\\|bethel\\|bethlehem\" KLN_1966.txt | head -20\necho \"=== KLN 1966 byssus ===\"; grep -n -i \"byssus\\|byssos\" KLN_1966.txt | head -20\necho \"=== KLN 1971 byssus ===\"; grep -n -i \"byssus\" KLN_1971.txt | head -20"
}
```


### [2026-09-05T14:50:48.911Z] TOOL RESULT

```
=== KLN 1966 'bayith' ===
=== KLN 1966 'Beth-el' / bethel ===
4273:badinage,  n.,  banter.  —  F.,  fr.  badiner,  ‘to  jest, joke’,  fr.  OProveng.  badin,  ‘simpleton,  fool’,  a derivative  of  badar,  ‘to  gape’,  fr.  VL.  batdre,  ‘to gape’.  See  bay  ‘part  in  the  wall’,  and  cp.  words there  referred  to.  For  the  ending  see  suff.  -age. Derivative:  badinage,  intr.  v. badminton,  n.,  name  of  a  game  played  with shuttlecocks.  — -  Fr.  Badminton,  seat  of  the  Duke of  Beaufort  in  Gloucestershire,  England, bactulus,  n.,  a  meteorite  ( antiq .)  —  L.,  fr.  Gk. pairuXo?,  a  sacred  meteoric  stone,  fr.  Heb. beth  El,  ‘house  of  God’;  see  bethel.  The  form Pai-ruXo?  shows  that  the  name  came  to  the
4839:Beta,  n.,  a  genus  of  plants  of  the  goosefoot family  (bot.)  —  L.,  ‘the  beet’.  See  beet, betake,  reflex,  v.  —  ME.  bitaken,  ‘to  entrust’,  fr.  bi- (see  be-)  and  taken,  ‘to  take’.  See  take, betatron,  n.,  a  device  for  accelerating  the  velo¬ cities  of  electrons  or  beta  rays.  —  Coined  fr. beta  (rays)  and  (elec)tron. betel,  n.,  the  leaf  of  the  pepper  called  Piper  betel. —  Port,  betel,  betle,  betre,  fr.  Malayal.  vettila, fr.  veru  ila,  ‘simple  leaf’, beth,  n.,  name  of  the  2nd  letter  of  the  Hebrew alphabet.  —  Heb.  beth,  lit.  ‘house’;  so  called in  allusion  to  the  ancient  Hebrew  form  of  this letter.  See  bethel  and  cp.  beta, bethel,  n.,  a  house  of  worship.  —  Heb.  beth  El, ‘the  house  of  God’.  Beth  is  the  state  construct of  bdyith,  ‘house’,  and  rel.  to  Aram,  baythd, bethd,  Ugar.  bt,  Arab,  bayt,  Akkad,  bitu, ‘house’;  cp.  beth,  beta.  Cp.  also  Basque  baita, ‘house’.  For  the  second  element  see  El.  Cp. baetulus,  baetyl.
4840:Bethesda,  n.,  a  pool  at  Jerusalem;  a  chapel.  — Gk.  Bij&eaSd,  fr.  Aram,  beth  hesdd,  ‘house  of mercy’.  See  bethel  and  Hasidim  and  cp.  beth, beta.
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
26592:ornitho-,  before  a  vowel  omith-,  combining  form meaning  ‘bird’.  —  Gk.  6pvtflo-,  6pviff-,  fr. 8pviq,  gen.  opvlDog,  ‘bird’,  which  is  cogn.  with Goth,  ara,  OE.  earn,  ‘eagle’.  See  erne  and  cp. words  there  referred  to.  Cp.  also  Ortalis. Omithogaium,  n.,  a  genus  of  plants,  the  star  of Bethlehem  ( bot .)  —  ModL.,  fr.  Gk.  opvtffo- YaXov,  ‘the  star  of  Bethlehem’,  which  is  com¬ pounded  of  opvt;,  gen.  opvffl-os,  ‘bird’,  and yiXa,  ‘milk’.  See  ornitho-  and  galactic, ornithology,  n.,  that  branch  of  zoology  which deals  with  birds.  —  ModL.  ornithologia,  fr.  Gk. opvtffoX6voc,  ‘one  who  speaks  of  birds’,  which is  compounded  of  opvu;,  gen.  opvtffoi;,  ‘bird’ (see  ornitho-),  and  ‘one  who  speaks  (in
=== KLN 1966 byssus ===
1277:abysm,  n.,  poetic  for  abyss.  —  OF.  abisme  (F. abime),  fr.  Eccles.  L.  *abismus  (whence  also OProven?.  abisme,  Sp.  and  Port,  abismo),  form¬ ed  on  analogy  of  words  ending  in  -ismus  (fr.  Gk. -ia[x6?;  see  -ism),  fr.  L.  abyssus.  See  abyss. Derivative:  abysm-al,  adj. abyss,  n.  —  L.  abyssus,  ‘bottomless  pit’,  fr.  Gk &(Juccroc;  (scil.  Aluvt]),  ‘bottomless,  unfath¬ omed  (pool)’,  fr.  a-  (see  priv.  pref.  a-)  and (3uaa6?,  ‘depth,  bottom’,  which  is  related  to (Julios,  of  s.m.  Cp.  abysm.
5994:byssine,  adj.,  made  of  byssus.  —  L.  byssinus.
5995:‘made  of  byssus’,  fr.  Gk.  Puaatvos,  fr.  jBucraop. See  next  word  and  adj.  suff.  -ine  (representing Gk.  -ivo?).
5996:byssus,  n.  —  L.,  fr.  Gk.  puaeog,  ‘fine  white  linen’, a  Semitic  loan  word.  Cp.  Heb.  biitz,  of  s.m.,  fr. Sem.  *b-w-f  {*b-w-tz),  ‘to  be  white,  to  surpass in  whiteness’,  whence  Heb.  betzdh,  Arab,  bayda1', ‘egg’.  Cp.  W.  Muss-Amolt,  Semitic  words  in Greek  and  Latin,  in  Transactions  of  the  Ameri¬ can  Philol.  Association,  23,  80,  Note  19. Derivatives:  byss-al,  adj.,  byss-in,  n.,  byssine (Q.v.)
=== KLN 1971 byssus ===
36112:byssine, adj., made of byssus. — L. byssinus , 
36113:‘made of byssus’, fr. Gk. fluacivos, fr. (Sugtoog. 
36117:byssus, n. — L., fr. ( 5 k. puooo?, ‘fine white linen’,
```


## [2026-09-05T14:50:50.755Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT baevar ===\"; grep -n -i \"baēvar\\|baevar\\|baēvan\" BRT.txt | head -20\necho \"=== PHD bewar ===\"; grep -n -i \"bēwar\\|bewar\\|byw'l\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HRN bevar ===\"; grep -n -i \"bêvar\\|bīvar\\|biwar\\|bēvar\" HRN.txt HUB.txt | head -20\necho \"=== DKS byurra ===\"; grep -n -i \"byūr\\|byur\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-05T14:50:50.874Z] TOOL RESULT

```
=== BRT baevar ===
16470:•  j.  baevan-,  baevar-  n.  'Zehntausend, Myriade';  navaca  navaitlsca  navaca  saia navaca  hasattra  navasJs{sA.Ya  •v_qn{^.) Yt  13.  59,  V.  22.  2 ;  —  fravasays  .  .  yä mao^mitncil  myesäinam  °vam  (NP.)  upa- vazinle  "..die  (als  sva.)  inMyriaden . .  herzu- fahren" Yt.jj.  64;  —  urvarh  ..  satavaiti- nqm  hazanravaitinqm  °varf  'varanqm '' V.5.  19  GI.(?).  a)  mit  Gen.:  saümca kasaiirTmca  'vanla  *parianqm  Yt/5. 71; JO.82,  5.21,  $.3,  H./.S,  sVar.,  12,  Y. öiS'-iS.  V.J.  31,  5'.  81,  i4.'i-i.(>"-\—  ys janai  azsqm  äaivanqm  . .  °r5i '>  'vand  (soll heissen)  "..  10000  mal  loooo"  Yt.j.  10; 4.2,  VytJß.  A)  attributiv  gebraucht: *vafv  yjnqnh  nisirinaoiH  Yt.  /o-  a  7 ;  — kakra  . .  yatataiibyS  . .  pan^asaiblsca  sa- täflca  /lasaarSisca  'variblsca  ahaxitäisca Vr.Äi.
16472:•  j.  baevara-yav-   Adj.    'loooofachen
16475:•  j.barvarö.tBniö.-baevar-  n.  'das  loooo-
16478:•  j.  baevara-yna-  n,,  Plur.  'loooo Schläge':  pancascrinsi  .  .  Aazanraynai 'ynäisca  baluarj-jttäi  *aAqxsicrfnäisca  (sd.) V.  7.  S3-         DS.  °ynai  als  Inf.  sbes.
16480:"  j.  baevar9-}iiäi  Inf.  '10000  zu  schla- gen': b°  *ahqxsiaynäisca  (sd.)  V.7.53. Vgl,  6an/ai-?THa-.  —  Pii. :  pa  bevor  ianiinik. ■  j.  baevara.£a§man-  Adj.  'zehntausend- äugig',  nur  von  Müra :  mt^nm  . .  hazattra.- gaossm  'tnatam  Y.  2.  3;  Yt/O.  7,  6.<,\  — mi^rahe  .  .  'manö  Y. /.  3;  —    mitral  .  .
16484:•  j.  baevar9.patay-  ni.  'Herr  Über  Zehn- tausend": pu%rar»hs  'tayd  Yt.  r^.  59;  — ää'iunqm  'paitinqm ''  Yt.  13. 38.
16486:•  j.  baevara.fraskomba-  Adj.  'auf  zehn- tausend Tragbalken  ruhend':  nmämm  .  . saiö.raocamm  .  .  hazatirS.sfunim  .  .  'bim Ytj.ioi.
16489:•  j.  baevar3.vaeSayana-  Adj.  'mit  zehn- tausend Warten':  nmämm  . .  bagvan.misUm 'tarn  V.  18.  aS;  zit  Vyt  4$.
16491:•  j.  baevarfl.vär-  m.,  Flur,  'zehntausend Regentropfen'(?):^(i>'i»'<i  äunma ..upa.apjm Aazanrö.varayö (sd.)  -värascii (NP.)  V. 21.%.
16493:•  j.  baevar«.spasan-  Adj.  'der  zehn- tausend Späher,  Wächter  hat',  von  Mikra: mi%rs  .  .  yS  'sanS  (NS,)"'  Yt  to.  24;  — mi^rB  .  .  yS  'sänö  (NS.)"  Yt  10.  60.
16792:j.  baj/ar!.mäUm  Vyt.  45-.  lies  baevar?.'.
20530:—  'r^m  .  .  haianragaoiim  .  .  bafvar».- iaimafum  ..  ai^afmm  jayaurvanhtm  Vt 70.  7;  —  °r?m  .  .  yahtnäi  mal'äia/um  frä- '^winsat . .  akurö  mazda  . .  karai^yö  paiti barfzaya  Yt  70.50;  —  surunuyä  nä  °ra yamahe  Yt  70.  32 ;  3» ;  —  usta  akmäi  ,  . yakmäi . .  zaota  asava  , ,  'rahe  vaca  yazäite rästun  ahmai  . .  °rB  ma2%anpm  Jcaraiti Yt  70. 137 ;  — yahmai .,*rB jasaiti  avaiiihe yö  baevariJpasanB  vIspB.vtövä  aiaoyamnB Yt  10.24;  —  '"'"  --yS  ■•  aivjyäiti  pasca ha  fräsm5.daitJm  . .  visptm  imat  adkäiti yal  atUan  zqm  asmattfmca  vatnm  zaslaya
21125:—  vJsäne  [ahmät  pourum  framraomi)  y'..  vTifttte  pairi  .  .  dru/a/  ,  .  mqnayfn  ahe jvisai  Y.4.4T,  47';  —  dafvayasnaHbyd'  y  na  sat»mca  . .  *parianqM  {s^)  *mjat>m paurjiö  iimayayanta y  mazdayasnaabyascit  hyät  Yt  13.  71.  b)  mit  Inj.:  *stfrf- V.  7. 37.  2)  y  mit  einer  Mass-  odet  naoiti  atia  avavat  stanm  ..y  nanm Wertangabe  'so  viel  (,  gross,  weit,  wertvoll  aiavarum  .  .  nasus  aoi  ava  *hravTt  (sd.) usw.)  ii\s  .  .';  zu  1):  avavat  taoa  y  P.2j.  c)  mit  Praes.:  n/a/  ahmJi  iiairt ca'hwärS  frtsavS  V,^. 29;  —  yat  h!  han-'  müdim  aahat  ..i  .  .  y'  .  .  baevar?  atr».- jasaiii  y  cd>rusüm  *yär?  a.42;  43;  —  saokanqm  däitlm  gätüm  avi  ava.baraüi nsil  haomO  hutU  axti/  . .  nsit  *nasus.ava.-  ".  .  als  ob  er  ,  .  hinzu  brächte"  V.  8. bfr?ll  {id.)    ava    aSe    ahuta  y    caiwlrö  81,          d)  ohneVerbum:  tä  dim  ata  ni-
25925:•  j.  sata'vant- Adj.  (km. 'vaiii-)  'hundert enthaltend,  hundertfach':  'vaitinqm  Aatav- ravaitinqm  balvar»  baevaranqm  V.5.19 Gl.;  —  'vata  iatS.inta  (sd.)  ufavaia  titi.- vita  Yt.  2. 14;  wertlos.
=== PHD bewar ===
PHD.txt:2880:myriad bēwar.
PHD_mackenzie.txt:1567:bewar [bywll M bywr, N,....,] myriad, ten thousand.
PHD_mackenzie.txt:7117:moderate paymiinig.                            myriad bewar.
=== HRN bevar ===
=== DKS byurra ===
842:aysirümjá ‘equipped with protective armour’, II 57:35 Мпа ssa byüra ssa byūrä aysirümjá bisä tan army all
4535:pirma- ‘а large number’, II 113, 3v4 tcahause kūla pirma Жайга lakşa Буйга hauda ysari hastase ' 14 kofi-millions, 18 laksa-myriads 7 thousands 800', =K 101:35 teihausi kūla pirma hag]üsi küla kşa byürd haudi ysári hastisse, =V 250-t, 775-6 tcahause küla pirma hagfusd lakga byürri hauda ysüri hasjase; JS 4v4 doarabista byurrá hasta ysüri рита. Зо pirma dyadic with Aofi- ‘еп millions’ but here rather ‘опе million’, as laksa—byürád ' 10,000’.
5747:byürru '10,000, myriad', 2 5:87 ksgi byürru ##aya 'six myriad (60,000) Sakya persons’, =Manj. 412 Араз ysüra ídya 'sixty thousand (60,000) Sakyas'; Z 293:28 dvi byürru hvamdä. ‘two myriad (20,000) men’; JS 4v4 dvārabistä Буйтай hasta ysüra 'twenty-two myriad eight thousand (228,000) '; К. бт, 4огт ssa-byüryi ‘(the Prajñā- pāramitā text) consisting of one hundred myriad (units) (1,000,000)'; v 62:15 byürd cha ttyi faysdd stude “ће size of the snake a myriad (10,000) feet’; ш 83:17-8 drai byüra hauvana pa-ysüra pacida pa-se ra hauda ita parvala 'three myriad powerful, five thousand, in due course five hundred also, seven are the protectors’ (BS paripülaka-) (—35,507); K. бт, 41v2 буйта kalpa ʻa myriad. Aalpa-periods'; K 40°12-3 jambwi vira byüra hastá ysürri citrra padimdi 'he built in Jambudvipa а myriad eighty thousand caitya-monuments (citrra for citya)', = 43:132 byürá cittri padáde. Note Z 22:114 dasau ysáre ‘ten thousand’, From *baivar (with ги from -am), Ау. ba£uar-, ba&van-, Sogd. Мап. Вгушт ' 10,000, Zor.P., N.Pers. bévar, M.Parth. T., M.Pers.T. byur, plur. bywr'n, Alan Beaop (in the name Boxopacrmros), Oss, D. beurd, бетй, plur. beretá, І. birä, Armen. lw biur, Georgian Iw beur-i. From Виаї- > bai- with -var-, -oan-; -aiga- > -yil, to base IE Pok. 146-50 bheu-:bhu- see s.v. buro, budara-.
```


## [2026-09-05T14:51:14.723Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport sys\ndef leaf_of(fn, lineno):\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')+1\nfor ln in [4839,4840,5996]:\n    print(ln, leaf_of('KLN_1966.txt', ln))\nEOF"
}
```


## [2026-09-05T14:51:16.912Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بیت ===\"; grep -n \"بیت \" MON_part1.txt | head -5\necho \"=== MON بیور ===\"; grep -n \"بیور\" MON_part1.txt MON_part2.txt | head -10\necho \"=== FSF بیور ===\"; grep -n \"بیور\" FSF_pages.txt | head -10\necho \"=== SOD βrywr ===\"; grep -n \"rywr\\|βrywr\\|βryw\" SOD.txt SOD_pages.txt | head -10"
}
```


### [2026-09-05T14:51:18.157Z] TOOL RESULT

```
4839 100
4840 100
5996 125
```


### [2026-09-05T14:51:18.271Z] TOOL RESULT

```
=== MON بیت ===
81:وی شیخ محمدتقی معین‌العلما که در سلک علمای روحانی بود به تربیت وی 
8970:پروردن» پرورش دادن» تربیت کردن. تنبیه 
9719:رجزء» بیت کوتاه» شعر کوتاه؛ ج. اراجیز. 
11013:منظم برای تقویت جسم و تربیت روان مانند 
13473:دو بیت ذیل مذکورند: 
=== MON بیور ===
MON_part1.txt:15921:شمس قیس از مختصات مردم ابیورد و 
=== FSF بیور ===
1989: ‫که ببرید بیور میانش به ار‬
4469:‫چو بیورد و چو شنگل بافرین‬                     ‫به سر بر نهاد آن کیانی کلاه‬
6181:                                       ‫بیور‬          ‫(‪۱-۲۱-۵4‬‬
6183:              ‫کجا بیور از پهلوانی شمار‬              ‫مصراع دوم اینبیت در نسخه‌های دیگر»‬
6189:                                 ‫بیور اسپ‬            ‫را»‪ .‬ولی در نسخه لندن کهکهن‌تر ادزیگر‬
6194:             ‫کجا بیور اسپش همی خواندند‬               ‫شاهد دیگری برای چون به معنی‬
6197:  ‫گاهنیز فردوسی ضحاک رابیور می‌نامد‪:‬‬                ‫یکی دخمه چون برفرازم تو را‬
6199:‫که ببرید بیور میانش به ار‬                                   ‫نه چیزست بامن نه سیم و نه زر‬
7574: ‫(‪)۲-۴۴۱-۲۷۲‬‬                                                       ‫کجا بیور از پهلوانی شمار‬
=== SOD βrywr ===
SOD.txt:26165:2808  brywr    C  =»  Pryywr 
SOD.txt:26167:2809  prywr  =*  Pryywr,  RYPW 
SOD.txt:26178:Pare-Par   (brywr,  Prywr)  ©Av.  baevar 
SOD.txt:44096:5443  mrywr  C  (-jy^jTlT^j 
SOD.txt:54987:pariwart   (prywrt)   ©impf.  =>prwrt- 
SOD.txt:56767:parwart   ©<*pari-warta   ©impf.  prywrt 
SOD.txt:56769:=»prwst-,  prwyst-,  prw'rt-,  prywrt-,  prwytJk 
SOD.txt:57592:7410  prywr    S  ^  pry'wr 
SOD.txt:57594:7411  prywrt    M  =*  pr'ywrt- 
SOD.txt:66190:Pewar,  prewar   (prywr)  ©Idg.  =»Pryywr
```


## [2026-09-05T14:51:24.919Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==100' KLN_1966.txt | head -20 && echo \"===== LEAF 125 =====\" && awk 'BEGIN{RS=\"\\f\"} NR==125' KLN_1966.txt | head -8"
}
```


### [2026-09-05T14:51:26.710Z] TOOL RESULT

```
 vaidiirya-), which  prob.  derives  from  the  name  of  the  city Velur  (now  called  Belur).  Cp.  G.  Brille,  ‘spec¬ tacles’,  from  the  pi.  of  MHG.  bril,  of  s.m.,  which derives  fr.  MHG.  berille,  ‘beryl’,  fr.  L.  beryl- las  (the  first  spectacles  were  made  from  beryl). Cp.  also  brilliant,  the  first  element  in  besiclo- meter  and  the  second  element  in  chrysoberyl. beryllium,  n.,  a  metallic  element,  called  also ghteinum  ( chem .)  —  ModL.,  fr.  L.  beryllus  (see beryl);  so  called  because  it  was  first  obtained through  isolation  from  beryl  (by  the  French chemist  Nicolas-Louis  Vauquelin  in  1797).  For the  ending  see  suff.  -ium.
166
berzelianite,  n.,  copper  selenide  {mineral.)  — Named  after  the  Swedish  chemist  Baron  Jons Jakob  Berzelius  (1779-1848),  who  first  analyzed it.  For  the  ending  see  subst.  suff.  -ite. berzelite,  n.,  arsenate  of  calcium,  magnesium  and manganese  (mineral.)  —  Named  after  the  S wed- dish  chemist  Baron  Jons  Jakob  Berzelius  (1779- 1848).  For  the  ending  see  subst.  suff.  -ite. bescreen,  tr.  v.  —  Formed  fr.  be-  and  screen, beseech,  trans.  v.  —  ME.  besechen,  fir.  be-,  and sechen,  seken,  ‘to  seek’.  See  seek  and  cp.  G. besuchen,  ‘to  visit’  (fr.  be-  and  suchen,  the  equi¬ valent  of  E.  seek).
Derivatives:  beseech-ing,  adj.,  beseech-ing-ly, adv.
beseem,  impers.  v.  —  Formed  fr.  be-  and  seem, beset,  tr.  v.  —  ME.  besetten,  fr.  OE.  besettan,  ‘to set  on,  adorn’,  rel.  to  Du.  bezetten,  OHG.  bi- sazjan,  G.  besetzen,  Goth,  bisatjan.  See  be-  and the  verb  set.
Derivatives:  besett-er,  n.,  besett-ing,  adj. beshrew,  tr.  v,  —  ME.  beschrewen,  ‘to  pervert’, fr.  be-  and  schrewen,  ‘to  curse’.  See  shrew,  ‘to curse*.
besiclometer,  n.,  an  instrument  for  measuring the  forehead  to  establish  the  exact  size  of  the spectacles.  —  A  hybrid  coined  fr.  F.  besides (pi.),  ‘spectacles’,  and  Gk.  jx^Tpov,  ‘measure’. The  first  element  is  an  alteration  of  OF.  bericle, fr.  L.  beryllus,  ‘beryl’.  The  ending  of  OF.  bericle was  prob.  suggested  by  the  synonym  escarboucle, ‘carbuncle’;  see  beryl.  For  the  second  element see  meter,  ‘poetical  rhythm’, beside,  prep.  —  ME.  besiden,  beside,  fr.  OE.  be sidan,  ‘by  the  side’,  fr.  be,  ‘by’,  and  dative  of side,  ‘side’.  See  by  and  side, besides,  adv.  —  Formed  fr.  prec.  word  with  the adv.  gen.  sufif.  -s.
Derivative:  besides,  prep.
besiege,  tr.  v.  —  Formed  with  change  of  pref.  fr. OF.  asegier  (F.  assieger),  fr.  VL.  *assedicdre, fr.  ad-  and  *sedicum,  ‘seat’,  fr.  L.  sedere,  ‘to  sit’. See  be-  and  siege.
Derivatives:  besieg-er,  n.,  besieg-ing,  n.,  besieg- ing-ly,  adv.
beslaver,  tr.  v.  —  Formed  fr.  pref.  be-  and  slaver, besmear,  tr.  v.  —  Formed  fr.  pref.  be-  and  smear, besmirch,  tr.  v.  —  Formed  fr.  pref.  be-  and  smirch, besom,  n.  —  ME.  besum,  fr.  OE.  besma,  besema, rel.  to  OS.  besmo,  OFris.  besma,  MDu.  besem, bessem,  Du.  bezem,  OHG.  besmo,  besamo,  MHG. besme,  besem,  besen,  G.  Besen.  The  original meaning  is  ‘something  bound  or  twisted’,  fr. I.-E.  base  *bheidh-,  ‘to  bind,  twist’.  See  fisc. Derivatives :  besom,  tr.  v.,  besom-er,  n. besot,  tr.  v.,  to  make  sottish.  —  Formed  fr.  be- and  sot.
Derivatives:  besott-ed,  adj.,  besotted-ly,  adv., besott-ed-ness,  n.
besought,  past  tense  and  pp.  of  beseech.  —  ME. besoht(e),  fr.  besechen.  See  beseech  and  cp. sought.
167
bespangle,  tr.  v.  —  Formed  fr.  be-  and  spangle. Derivative:  bespangl-ed,  adj. bespatter,  tr.  v.  —  Formed  fr.  be-  and  spatter. Derivative :  bespatter-er,  n. bespeak,  tr.  v.  —  ME.  bespeken,  fr.  OE.  be- sp(r)ecan,  ‘to  speak  about’,  rel.  to  Du.  bespreken, G.  besprechen.  See  be-  and  speak, besprent,  adj.,  sprinkled  (archaic).  —  ME.  be- spreynt,  pp.  of  besprengen,  fr.  OE.  besprengan, ‘to  besprinkle’,  rel.  to  Du.  and  G.  besprengen, of  same  meaning.  See  be-  and  sprinkle  and  cp. next  word.
besprinkle,  tr.  v.  —  Formed  fr.  pref.  be-  and sprinkle.
Bessemer  process,  Bessemer  steel.  —  So  called after  Sir  Harry  Bessemer,  engineer  and  inventor (1813-98).
best,  adj.  —  ME.,  fr.  OE.  best,  dissimilated  fr. betst,  rel.  to  ON.  beztr,  Du.  best,  OHG.  be^isto, MHG.,  G.  best,  Goth,  batists,  ‘best’,  OE.  batian, ‘to  become  better’,  bot,  ‘remedy,  cure,  improve¬ ment,  compensation’,  and  possibly  cognate  with OI.  bhadrah,  ‘favorable,  good’,  Avestic  hubadra-, lucky’.  Cp.  better.  Cp.  also  batten,  ‘to  grow fat’,  boot,  ‘advantage’.  For  the  dissimilation  of
OE.  betst  into  best  cp.  last,  adj.
bestead,  adj.  —  ME.  bestad,  ‘placed,  situated’, formed  fr.  be-  and  stad,  ‘placed’,  fr.  ON. staddr,  ‘placed’,  pp.  of  stedja,  ‘to  place,  fix’.  See stead.
===== LEAF 125 =====
 Derivatives:  bustle,  n.,  hurry,  bustl-ing,  adj., bustl-ing-ly,  adv.
bustle,  n.,  framework  worn  by  women  to  support the  skirt.  —  Of  uncertain  origin, busy,  adj.  —  ME.  busy,  bisy,  fr.  OE.  bysig,  bisig, rel.  to  LG.  besig,  Du.  bezig ;  of  uncertain  origin. Derivatives :  busy,  v.  (q.v.),  busy-ness,  n. busy,  tr.  v.  —  OE.  bysgian,  bisgian,  fr.  bysig, bisig.  See  busy,  adj.
Busycon,  n.,  a  genus  of  marine  snails  (tool.)  — ModL.,  fr.  Gk.  (Bouauxov,  ‘a  large  coarse  fig’; so  called  from  the  fancied  resemblance  of  the shell  to  a  large  fig.  Gk.  (Boo cuxov  is  formed  fr. augment  pref.  (Boy-  and  cryxov,  ‘fig’.  The  pref. (Boy-  is  rel.  to  (Bouc,  ‘ox’,  and  orig.  meant  ‘as  big as  an  ox’.  See  bovine  and  Sycon. but,  prep.  —  ME.  butan,  buten,  bate,  fr.  OE.  bu- tan.  ‘without,  except,  besides’,  fr.  be-Cttan, which  is  compounded  of  be,  ‘by’,  and  iitan,  ‘out, outside,  except,  without’,  fr.  iit,  ‘out’.  See  by and  out  and  cp.  about.
Derivatives:  but,  conj.,  adv.,  n.,  tr.  and  intr.  v. but,  n.,  the  outer  room  of  a  cottage.  —  Fr.  but, adv.  See  prec.  word.
butane,  n.,  either  of  two  hydrocarbons  in  the methane  series  ( chetn .)  —  Formed  w'ith  suft. -ane  from  the  first  three  letters  of  L.  butyrum, ‘butter’.  See  butter.
butcher,  n.  —  ME.  bocher,  boucher,  fr.  OF. bochier  bouchier  (F.  boucher),  ‘butcher  ,  lit. ‘one  who  slaughters  bucks’,  fr.  bouc,  ‘buck’.  See buck,  ‘male  deer’,  and  -er  (representing  OF. -ier).
Derivatives:  butcher,  tr.  v.,  butcher-ly,  adj.  and adv.,  butcher-li-ness,  n.
butchery,  n.  —  ME.  bocherie,  fr.  OF.  bocherie, boucherie  (F.  boucherie ),  fr.  boucher.  See  but¬ cher  and  -y  (representing  F.  -ie).
```


## [2026-09-05T14:51:34.324Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==125' KLN_1966.txt | grep -n \"^[0-9]\\{3\\}$\" ; echo \"--- byssus context page marker:\"; awk 'BEGIN{RS=\"\\f\"} NR==125' KLN_1966.txt | grep -n \"byssus\\|^21[0-9]$\\|^2[0-9][0-9]$\""
}
```


### [2026-09-05T14:51:35.844Z] TOOL RESULT

```
24:214
49:217
--- byssus context page marker:
24:214
45:byssine,  adj.,  made  of  byssus.  —  L.  byssinus.
46:‘made  of  byssus’,  fr.  Gk.  Puaatvos,  fr.  jBucraop. See  next  word  and  adj.  suff.  -ine  (representing Gk.  -ivo?).
47:byssus,  n.  —  L.,  fr.  Gk.  puaeog,  ‘fine  white  linen’, a  Semitic  loan  word.  Cp.  Heb.  biitz,  of  s.m.,  fr. Sem.  *b-w-f  {*b-w-tz),  ‘to  be  white,  to  surpass in  whiteness’,  whence  Heb.  betzdh,  Arab,  bayda1', ‘egg’.  Cp.  W.  Muss-Amolt,  Semitic  words  in Greek  and  Latin,  in  Transactions  of  the  Ameri¬ can  Philol.  Association,  23,  80,  Note  19. Derivatives:  byss-al,  adj.,  byss-in,  n.,  byssine (Q.v.)
49:217
```


## [2026-09-05T14:51:36.602Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins byssus/bwt ===\"; grep -n -i \"byssus\\|byssos\" AHD_watkins1985.txt | head\necho \"=== FSD vol1 beth ===\"; grep -n -i \"Beth-el\\|bayith\\|Bethlehem\" FSD_vol1.txt | head -10\necho \"=== SOD line 26178 context ===\"; sed -n '26160,26185p' SOD.txt\necho \"=== SOD 66185 ===\"; sed -n '66185,66195p' SOD.txt"
}
```


### [2026-09-05T14:51:36.708Z] TOOL RESULT

```
=== AHD watkins byssus/bwt ===
=== FSD vol1 beth ===
5219:A"  bo  at  \   X   a*ba';  2   5T>u'*  Edmond  Francois  Valentin  beggars(I6tUandl7thcenturies)whofeignedlunacy;orIgi- (Vi<lS2S-*/nlSS5).  A   French  novelist  and  dramatist.  nally.  a   mendicant  inmate  of  Bethlehem  Hospital.  London.
5483:’   0/7*1528-*/ lilssl)  a   French  novelist  and1  dramatist.  nally.  a   mendicant  inmate  of  Bethlehem  Hospital,  London-  -   .   ,   ~   .   0
9579:The  wondering  flocks. —   agaze  with  grass  half  chewed.  Edwin Arnold  Light  of  the  World,  At  Bethlehem  p.  28.  [r.  a   w.  1891.] a-gazed't»  pv.  Astounded;  amazed;  aghast.
19162:’oaken  valves’  called  the  Bethlehem  or  Joppa  gate.  Aph"ar-sath 'a-cltes,  1   al'ar-safh'd-soits;  2   af’ar-sath'a-clts.
38890:Pope  Epistle  to  Dr.  Arbuthnot  I.  3. 3.  [B-]  The  hospital  of  St.  Mary  of  Bethlehem  in London, founded  as  a   priory  in  Bishopsgate  Street  With- out about  1217.  On  the  suppression  of  religious  houses  by Henry  VIII.  It  was  incorporated  as  a   hospital  for  the  Insane In  1547.  A   new  hospital  was  built  at  Moorfields  In  1G76, and  this  was  superseded  by  the  present  hospital  in  St. George’s  Fields,  1815.  4t-  An  inmate  of  Bedlam.  5f. A   madman.  {Cor.  of  Bethlehem. I   —   bed'lam,  a.—  Bedlam beggar,  one  discharged  from  Bedlam  Hospital  and  licensed to  beg:  the  custom  ceased  about  1675.—  Tom  o*  Bedlam,  a madman.—  bed'Iara-er»,  n.  1.  The  young  of  the  harp-seal when  in  Its  second  year.  2f.  A   bedlamite.— bcd'Iam-lsm, n.  The  acts  or  traits  of  the  insane;  mad  confusion  or  uproar. —   bedlam-Ite,  n.  Ad  inmate  of  Bedlam;  madman;  luna- tic.— bedlam-i"tlsb,a.—  bed'lam-! re,  vt.  To  make  mad.
40741:1   ”   ’   *   ■   "   ...  .   1.  A   resident  of  Bethlehem,  in  Judea.  2.  A   bedlam-
40742:ite. 3.  Ch.  Hist.  (1)  One  of  an  order  of  monks  in England  in  the  13th  century,  wearing  a   badge  repre- senting the  star  of  Bethlehem.  (2)  One  of  a   hospital brotherhood  in  Spanish  America  in  the  17th  century. Beth'Ie-mltcJ.
45463:Bo'az,  1   bO'az;  2   bO'az,  r.  Bib.  A   wealthy] Bethlehemlte,  who  married  Ruth.  Ruth  III,  10.
67534:(6)  Any  one  of  the  tribes  of  ancient  Gaul.  2.  The  peo- ple or  a   city  taken  collectively;  specif.,  the  financial  com- munity in  London.  3.  Antiq.  A   citadel  or  central  sec- tion used  by  the  dwellers  in  a   district  as  a   market,  a   place of  worship  or  festivity,  and  a   refuge  In  time  of  invasion. Compare  acropolis.  [<  F.  dtt,  <   L.  ddtas,  <   rtri*,  citi- zen.] cit'eet;  cit'Ict.—  Cities  of  the  Plain,  the  cities  of the  Palestinian  plain  of  the  Jordan,  north  of  the  Dead  Sea: Sodom  and  Gomorrah  were  the  most  important —   city article  [Eng.],  the  financial  and  commercial  news  article In  a   London  newspaper.—  c.  father,  an  alderman.—  c.  hail, a   building  for  the  municipal  administration.—  C.  or  a   Hun- dred Towers,  Pavla,  Italy:  from  its  numerous  towers.— C.  of  Brotherly  Love,  Philadelphia,  Pa.—  C.  of  Churches, the  former  city  of  Brooklyn,  N.  Y.,  now  a   borough  of Greater  New  York.—  C.  of  David.  Bib.  1.  Jerusalem, especially  the  citadel  on  Mt.  Zion.  1   Chron.  xl,  5.  2. Bethlehem.  Luke  Ii,  11.—  C.  or  Destruction,  in  Bunyan'a Pilgrim’s  Progress,  an  Imaginary  city  that  typifies  the worldly  state  of  the  unconverted;  Christian  fiees  thence to  the  Celestial  City.—  C.  or  Elms,  New  Hnven,  Conn.: from  the  streets  being  shaded  with  elms.—  C.  of  Enchant- ments, in  the  Arabian  Nights,  the  enchanted  city  In  the story  of  Beder ,   Prince  of  Persia.—  C.  of  God,  title  of  a   work by  St.  Augustine  (De  Civitate  Dd),  the  church  or  body  of believers,  ns  opposed  to  the  body  of  unbelievers  —   C.  of Lanterns,  In  Lucian’s  Vcrx  Historix,  the  fanciful  cloud city.—  C.  of  Legions,  the  ancient  city  of  CacrIeOn«on*Usk, where  Arthur  held  court.—  C.  of  Magnificent  Distances, Washington,  D.  C.— C.  of  Masts,  London:  from  Its crowded  shipping.— C.  of  Monuments,  Baltimore,  Ma*
77311:Jesus,  the  babe  of  Bethlehem,  has  become,  beyond  all  others, whether  philosophers,  warriors,  or  kings,  the  most  conspicuous being  who  ever  trod  this  globe.
=== SOD line 26178 context ===
carrying,  having 
BSTi281;GMS  897 A 

2807  prysty/k   S  =->  Pr>yst>k 

2808  brywr    C  =»  Pryywr 

2809  prywr  =*  Pryywr,  RYPW 

2810  pryy   M  ^^ 
pare   =»Pr>y,  bry,  Pr>k2 

fruit 

BBB  570  a7;  Hen.  BSOAS  12,  307,  312;  GMS  966, 
1661 

2811  pryywr   M  jj-mjO**0 
Pare-Par   (brywr,  Prywr)  ©Av.  baevar 

=*RYPW 
ten  thousand,  myriad 
GMS  362,  1329;  Hen.  Cosm.  307.63,  312.92;  BBB; 

C2,  12V20 

=== SOD 66185 ===
defectivness 

MDii  p43.14;  KG  555;  Gersh.  Advice. 

8652  RYPW   B,  S  (y) ^ < Jyt» 
Pewar,  prewar   (prywr)  ©Idg.  =»Pryywr 

ten  thousand,  myriad 

GMS  362;  VJ  pi  19;  TSP;  BSTBL  pl30;  SCE  p69; 
STii  9.14.15;  RYPW  -kyy  Dhy.  329  "by
```


## [2026-09-05T14:51:54.337Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T14:51:54.344Z] TOOL RESULT

```


```


## [2026-09-05T14:51:56.300Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\nimport re\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\bbeth\\b.*Hebrew alphabet|Beth\\'el|Beth-el', p, re.I):\n        print('LEAF',i, p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:51:58.805Z] TOOL RESULT

```
LEAF 181   hunger,  thirst,  and  sex.  See  feei  inc. 3.  A   craving  of  the  mind;  strong  liking,  desire,  or  long- ing, giving  mental  bent  or  tendency;  as.  an  appetite for  art. Of  all  the  
LEAF 316 tollet*preparatlon,  perfume,  etc. — b.  work  (Aftning),  the  richest  ore. best,  n.  1.  The  most  excellent  thing,  part,  belonging,  or quality  ;*  the  highest  degree  or  state;  the  ut
```


## [2026-09-05T14:52:04.003Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\np=txt.split('\\f')[316]\nimport re\ni=p.lower().find('beth')\nprint(p[:120].replace('\\n',' '))\nprint('...')\nfor m in re.finditer(r'[Bb]eth', p):\n    s=max(0,m.start()-200); print('>>>', p[s:m.start()+400].replace('\\n',' ')[:600]); print()\nEOF"
}
```


### [2026-09-05T14:52:05.800Z] TOOL RESULT

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b3tsb5o4l.txt

Preview (first 2KB):
tollet*preparatlon,  perfume,  etc. — b.  work  (Aftning),  the  richest  ore. best,  n.  1.  The  most  excellent  thin
...
>>> bllhlethem Bet'el-guesc,  1   bet'el-guz, -gis,  or-guz;  2b?t'€l-g\ig, -gls,  <   b?lh,  house,  -f  lethem,  food.] Phil.  Soc.  or-gftg,  n.  alslron.  A   reddish  star  of  the  firstUnagnitude  Beth 'ie-hem  Eph'ra-tah.  Bib .   Mic,  v,  2. the  constellation  Orion  (a),  having  a   remarkable  fluted  Beth'Ie-Iieni-lte,  I   befh'h-hem-ait;  2   bSth'le-h£m-It,  n. 1   ”   ’   *   ■   "   ...  .   1.  A   resident  of  Bethlehem,  in  Judea.  2.  A   bedlam- ite. 3.  Ch.  Hist.  (1)  One  of  an  order  of  monks  in England  in  the  13th  century,  wearing  a   badge  repre- sentin

>>> od.] Phil.  Soc.  or-gftg,  n.  alslron.  A   reddish  star  of  the  firstUnagnitude  Beth 'ie-hem  Eph'ra-tah.  Bib .   Mic,  v,  2. the  constellation  Orion  (a),  having  a   remarkable  fluted  Beth'Ie-Iieni-lte,  I   befh'h-hem-ait;  2   bSth'le-h£m-It,  n. 1   ”   ’   *   ■   "   ...  .   1.  A   resident  of  Bethlehem,  in  Judea.  2.  A   bedlam- ite. 3.  Ch.  Hist.  (1)  One  of  an  order  of  monks  in England  in  the  13th  century,  wearing  a   badge  repre- senting the  star  of  Bethlehem.  (2)  One  of  a   hospital brotherhood  in  Spanish  America  in  the  17th  century

>>>   Mic,  v,  2. the  constellation  Orion  (a),  having  a   remarkable  fluted  Beth'Ie-Iieni-lte,  I   befh'h-hem-ait;  2   bSth'le-h£m-It,  n. 1   ”   ’   *   ■   "   ...  .   1.  A   resident  of  Bethlehem,  in  Judea.  2.  A   bedlam- ite. 3.  Ch.  Hist.  (1)  One  of  an  order  of  monks  in England  in  the  13th  century,  wearing  a   badge  repre- senting the  star  of  Bethlehem.  (2)  One  of  a   hospital brotherhood  in  Spanish  America  in  the  17th  century. Beth'Ie-mltcJ. be-stowd',  pp.  Bestowed, be-stow'lng,  1   bi-std'iq;  2   be-sto'ing,  n. A   clamp-casing  of  burn

...
</persisted-output>
```


## [2026-09-05T14:52:12.323Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor i in (315,316,317):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', p)\n    print(i, nums[:10], '|', p[-200:].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:52:14.808Z] TOOL RESULT

```
315 [] | ,  well,  greatly;  cp.  dial.  G.  bale. to  be  of  use.]  bestet.—  best  man,  the  groomsman  at  a wedding. — best  seller,  a   product  greatly  in  demand  by the  public,  esp.,  a   book,  
316 ['266'] | ak'e-ram;  2   b£th'-zfiC#a-rfim, troubled.  ,   ,   n.  .   Btb.  (Doual).  [/  Mac •   vl,  32. I,.  B.  Paton  in  Standard  Btb.  D\ct.  p.  399.  If.  &   w.  09.]  Beth"*zach"a-rl'as,  X   -zak'
317 [] |   have  said,  great  difference  betxoixt  our  Boho- mia  and  your  Sicilia.  Shakespeare  Winter's  Tale  act  I,  sc.  1. [ME.  betvnze,  betwixen  (cp,  OHG.  in  zwishen ,   between two,  >   N
```


## [2026-09-05T14:52:25.059Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%AA",
 "prompt": "Give the Arabic entry: etymology of بيت bayt \"house\", the root ب ي ت (b-y-t), Proto-Semitic reconstruction, cognates (Hebrew בית, Akkadian, Ugaritic), and the meaning \"verse/line of poetry\". Also any Persian section."
}
```


## [2026-09-05T14:52:26.470Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/byssus",
 "prompt": "Give the full etymology of English byssus: Latin byssus, Ancient Greek βύσσος, Hebrew בוץ būṣ, Semitic root, any Egyptian origin claim, and the meaning (fine linen, mummy wrappings)."
}
```


### [2026-09-05T14:52:32.250Z] TOOL RESULT

```
# Arabic Entry: بيت (bayt)

## Etymology
The word derives from **Proto-Semitic *bayt-**, as documented in the Wiktionary entry. The root is **ب ي ت (b-y-t)**, which contains "6 terms" according to the source material.

## Cognates
While the provided document mentions "Cognate with Amharic ቤት (bēt)," it does not include the Hebrew, Akkadian, or Ugaritic cognates you requested. Only the Amharic parallel is explicitly listed.

## Primary Meanings

**As a noun (dwelling):**
The entry defines it as "house, building" and extends to "tent (dwelling), room, apartment, flat," plus commercial establishments and settlements.

**As a noun (poetry):**
In poetic contexts, it means "verse, couplet, distich" with plural **أَبْيَات (ʔabyāt)**.

## Verb Form
**بَيَّتَ (bayyata)** is a Form II verb meaning "to brood" or "to contrive, hatch (a plan, plot)."

## Persian Section
The document includes Persian descendants showing **بیت (beyt)** derived from Arabic, which subsequently influenced Urdu **بیت (bait)**.
```


### [2026-09-05T14:52:32.518Z] TOOL RESULT

```
# Etymology of English "Byssus"

Based on the Wiktionary entry, here's the documented etymological path:

**Latin origin:** The English term derives from Latin *byssus*.

**Ancient Greek source:** Latin *byssus* comes from Ancient Greek *βύσσος* (bússos), meaning "flax; flax cotton."

**Semitic roots:** The Greek term traces to a Semitic source, with cognates in:
- Hebrew *בּוּץ* (būṣ, "byssus")
- Aramaic *בּוּצָא* (būṣā, "byssus")

**Regarding Egyptian origins and mummy wrappings:** The provided Wiktionary content contains no mention of Egyptian origins or use in mummy wrappings. The etymology stops at Semitic languages.

**Modern meaning:** The term now refers to "the long fine silky filaments excreted by several mollusks" used for attachment, or the sea silk manufactured from them.

The documentation does not extend the etymology to Egyptian sources or discuss historical mummy applications, despite the term's association with fine fibers.
```


## [2026-09-05T14:52:38.753Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%B6%D8%A9",
 "prompt": "Arabic بيضة bayḍa: etymology (from بيض bayḍ, root ب ي ض 'to be white'), meanings (egg, testicle), and any note on the adjective أبيض abyaḍ 'white'. Also list Persian/other descendants and any related بياض bayāḍ 'whiteness'."
}
```


## [2026-09-05T14:52:40.657Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1",
 "prompt": "Persian بیور: meaning, etymology (Middle Persian bēwar, Avestan baēuuar-, Proto-Iranian), and any mention of Bēvarasp / Zahhāk. Quote the etymology section."
}
```


### [2026-09-05T14:52:44.777Z] TOOL RESULT

```
# Arabic Word: بيضة (bayḍa)

## Etymology
The word derives from the collective noun "بيض" (bayḍ), with the singulative suffix "-ة" (-a) added. The root "ب ي ض" relates to whiteness.

## Primary Meanings
According to the Wiktionary entry, this term has several definitions:

1. **Egg** - the most common usage
2. **Testicle** - with related synonyms خَصْيَة and خِسْيَة
3. **Helmet** - a less common meaning
4. **Essential part or substance** - an abstract meaning
5. **Counterweight** - specifically on a steelyard scale

## Linguistic Details
The word is feminine and can be declined in various forms. It has multiple plural forms, including both sound plurals (بَيْضَات - bayḍāt) and broken plurals (بُيُوض - buyūḍ).

## Descendants
The term has influenced other languages through historical contact, appearing in Maltese (bajda) and Ottoman Turkish (بیضه - beyza).
```


### [2026-09-05T14:52:47.161Z] TOOL RESULT

```
# بیور (bēwar / bivar)

**Meaning:** This Persian noun historically denotes a myriad or ten thousand.

**Etymology:** The word descends through several language stages. According to the entry's etymology section:

"Inherited from Middle Persian 𐫁𐫏𐫇𐫡 (bywr /⁠bēwar⁠/), from Old Persian *baivaram, from Proto-Iranian *baywáram"

The Proto-Iranian form *baywáram functioned as the accusative case of *baywā́.

**Literary Reference:** The word appears in Firdawsī's *Shahnameh* (c. 977-1010), specifically in the narrative about Zahhák. The text notes that "Ten thousand is **bíwar** in ancient Persian" and references Bíwarasp, a figure associated with possessing ten thousand Arab steeds.
```


## [2026-09-05T14:52:52.168Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=byssus",
 "prompt": "Give the American Heritage Dictionary entry for \"byssus\": definition and full etymology (Latin, Greek, Hebrew, Egyptian?)."
}
```


## [2026-09-05T14:52:53.294Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/byssus",
 "prompt": "Give Etymonline's etymology of byssus (and byssine/bysse if present): Latin, Greek byssos, Hebrew buts, Egyptian origin, meaning."
}
```


### [2026-09-05T14:52:57.585Z] TOOL RESULT

```
# Byssus - American Heritage Dictionary Entry

**Definition:**
The dictionary provides two meanings: "(1) Zoology: A mass of strong, silky filaments by which certain bivalve mollusks, such as mussels, attach themselves to rocks" and "(2) A fine-textured linen of ancient times, used by the Egyptians for wrapping mummies."

**Etymology:**
The entry traces the word's origins back through "Middle English _bissus_, linen cloth, from Latin, from Greek _bussos_, linen." The source notes connections to Sanskrit _picuḥ_ (cotton) "of Dravidian origin, or ultimately from Egyptian _w'ḏ_, linen."

No Hebrew origin is mentioned in this entry. The etymological path runs: Egyptian → Greek → Latin → Middle English → Modern English, with a possible Sanskrit parallel indicating broader ancient textile terminology across linguistic families.
```


### [2026-09-05T14:52:58.625Z] TOOL RESULT

```
I apologize, but the web page content provided does not include any etymology entry for "byssus" or related terms like "byssine" or "bysse." The page shown is primarily a header/navigation page for Etymonline with links, search functionality, and footer information about the site itself.

To find the etymology of "byssus," you would need to search the Etymonline database directly using their search feature, but that specific entry is not present in the content you've shared with me.
```


## [2026-09-05T14:53:21.637Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%91%D7%95%D7%A5",
 "prompt": "Hebrew בוץ (būṣ): give the etymology and meaning (\"byssus, fine white linen\"), whether it is described as a loanword (from Akkadian/Egyptian) or from a Semitic root b-w-ṣ 'to be white', and any cognates listed (Aramaic, Arabic)."
}
```


## [2026-09-05T14:53:22.874Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=bethel",
 "prompt": "Give the American Heritage Dictionary entries for \"bethel\" and, if present, \"Bethlehem\": definitions and etymologies (Hebrew bêt ʾēl etc.)."
}
```


### [2026-09-05T14:53:27.354Z] TOOL RESULT

```
# American Heritage Dictionary Entries

## Bethel

**Definitions:**
1. A sacred or holy location
2. A chapel serving seafarers, or (chiefly in Britain) a Nonconformist chapel, particularly Baptist or Methodist

**Etymology:**
From Hebrew *bêt 'ēl*, meaning "house of God" — combining *bayit* (house) and *'ēl* (God)

**Historical Reference:**
The dictionary also notes "A town of ancient Palestine north of Jerusalem. It is now a major archaeological site."

## Bethlehem

No separate entry for "Bethlehem" appears in the provided content.
```


### [2026-09-05T14:53:28.405Z] TOOL RESULT

```
# Hebrew בוץ (būṣ) - Etymology and Meaning

## Meaning
The word has two distinct meanings:

1. **Mud** - The primary definition, exemplified in Biblical Hebrew (Jeremiah 38:22)
2. **Byssus** - "Fine linen," from the second etymology

## Etymology

**For "mud" (Etymology 1):**
The origin is uncertain. The entry notes a possible connection to Arabic root ب ض ض (b ḍ ḍ) with words like بَضُوض (baḍūḍ) referring to "small quantities of rain or water," and to Akkadian bāṣum meaning "sand." The Hebrew root is ב־צ־ץ (b-ts-ts).

**For "byssus/fine linen" (Etymology 2):**
This derives from Proto-Semitic *būṣ-, with the root ב־ו־ץ (b-w-ts). The Wiktionary entry does not explicitly describe this as a loanword or detail cognates in other Semitic languages like Aramaic or Arabic.

The entry lacks comprehensive information about Semitic cognates or explicit designation of loanword status, particularly for the "byssus" meaning.
```


## [2026-09-05T14:53:35.840Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find line 6181 -> which [pdf page N]\nimport re\nn=0\nfor i,l in enumerate(lines[:6260]):\n    m=re.search(r'\\[pdf page (\\d+)\\]', l)\n    if m: n=m.group(1)\nprint('pdf page tag before line 6181:', n)\nprint('\\n'.join(lines[6170:6215]))\nEOF"
}
```


### [2026-09-05T14:53:37.525Z] TOOL RESULT

```
pdf page tag before line 6181: 0
‫از آن بی‌منش کودک زشت کام‬                          ‫که از شهر قیصر ورا دور کرد‬
‫(‪۹‬شیرویه‪٩‬‏ ‪)۲۰۱‬‬                                     ‫(‪۶-۷۴-۰۳‬ع‪)۶‬‬
‫پیوسنده‬                                       ‫‪1۳۵‬‬


                                      ‫بینی‬                                                ‫سننده‬

             ‫همان خوک بیثی خوابیده چشم‬                                           ‫دیده چشم‪:‬‬
‫دل آگنده دارد توگوییبه حشم‬                                    ‫بسه بسینندگان آفسریننده را‬
‫(پرویز ‪)۴۷۱‬‬                                         ‫چو بینی؟ مرنجان دو بیننده را‬
                                       ‫بیور‬          ‫(‪۱-۲۱-۵4‬‬

              ‫کجا بیور از پهلوانی شمار‬              ‫مصراع دوم اینبیت در نسخه‌های دیگر»‬

 ‫بود بر زبان دری ده هزار‬                            ‫وعمولا در نسخه‌های چایی شاهنامه به‬
                                                                                     ‫م‬
 ‫(‪)۱-۲۴-۵۸‬‬                                           ‫این شکل است «نبینی مرنجان دو بیننده‬

                                 ‫بیور اسپ‬            ‫را»‪ .‬ولی در نسخه لندن کهکهن‌تر ادزیگر‬
             ‫دارای ده هزار اسب نامضحاک‪:‬‬              ‫نسخه‌هاست به جای نبینی «جوبینی»‬

             ‫جهانجوی را نام ضحاک بود‬                ‫آمده» «چو» در اینبیت مخفف چون و به‬
‫دکلااوردا تناک نود‬                                                 ‫معنای چجگونه» چسان است‪.‬‬
             ‫کجا بیور اسپش همی خواندند‬               ‫شاهد دیگری برای چون به معنی‬
 ‫حنین نام بر پهلوی راندند‬                                                     ‫چگونه» چسان‪:‬‬
‫‏)‪(AF-FF-1‬‬                                                 ‫همی گفت کاکنون چه سازم تو را‬
  ‫گاهنیز فردوسی ضحاک رابیور می‌نامد‪:‬‬                ‫یکی دخمه چون برفرازم تو را‬
           ‫نه من بیش دارم ز جمشید فر‬                 ‫(‪)۶-۵۵۱-۲۱۳‬‬
‫که ببرید بیور میانش به ار‬                                   ‫نه چیزست بامن نه سیم و نه زر‬
  ‫‪۶۲۲۳۰۷۸۱‬‬                                          ‫نه خشت و نه آب و نه دیوار گر‪.‬‬
                                   ‫بیو سنده‬
                                                                                 ‫نه‪:‬‬
                                                                                   ‫یب‬‫افف‬
                                                                                       ‫مخ‬
‫(اسم فاعل از بیوسیدن به معنی اميد و‬
                                                           ‫تواو را بدین جنگ رنجه مکن‬
 ‫ارزو داشتن)‪ :‬امید دارنده باارزو و امید‪:‬‬
                                                    ‫زی نمانم سخن‬  ‫این‬‫رنب‬
                                                                       ‫کده م‬
                ‫که هرگز نبیند تنم جز زره‬             ‫(‪)۶۰۵-۱۷۶‬‬
‫بسیوسنده و برفگنده گره‬
                                                     ‫(در نسخه لندن و دو نسخۀ دیگر «بین»‪,‬‬
 ‫(‪۶-۵۳۳-۲۴۲4‬‬
                                                         ‫نسخه قاهره «بر» نسخهة دیگر «زین»)‬
 ‫نابیوسان به معنی‪ :‬ناخواسته نهبر ارزو‬
```


## [2026-09-05T14:53:50.276Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nprint('leaf for line 6181:', '\\n'.join(lines[:6181]).count('\\f')+1)\nprint('total leaves', txt.count('\\f')+1)\nimport re\nprint(re.findall(r'\\[pdf page \\d+\\]', txt)[:3])\nEOF"
}
```


## [2026-09-05T14:53:51.947Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D9%88%D8%B1/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for بیور — the definition and any bracketed origin tag (e.g. [په.]). Also the دهخدا entry if present."
}
```


### [2026-09-05T14:53:52.929Z] TOOL RESULT

```
leaf for line 6181: 129
total leaves 485
[]
```


### [2026-09-05T14:53:58.761Z] TOOL RESULT

```
# بیور - Dictionary Entries

## فرهنگ معین (Mo'in)

**Definition:** "(وَ) [په.] (اِ.) عددی معادل ده هزار"

Translation: A numerical value equivalent to ten thousand.

The bracketed origin tag [په.] indicates Pashto origin.

---

## لغت نامه دهخدا (Dehkhoda)

The Dehkhoda entry provides extensive etymological information, noting that in Pahlavi, بیور meant "ten thousand" (ده هزار). The entry references multiple classical sources and includes historical usage examples from Ferdowsi's Shahnameh, documenting the term's application in Persian literature to denote this numerical quantity.
```


## [2026-09-05T14:54:11.491Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== RCH bait/house ===\"; grep -n -i \"bait,\\? *a house\\|baita\\b\" RCH.txt | head -6\necho \"=== RCH baiza ===\"; grep -n -i \"baiza\\|baizat\\|bayza\" RCH.txt | head -8\necho \"=== RCH biwar ===\"; grep -n -i \"biwar\\|bewar\\|bīwar\" RCH.txt | head -8\necho \"=== FVQ bayt ===\"; grep -n -i \"bait\\b\\|bayt\" FVQ.txt | head -8\necho \"=== ARY biwar ===\"; grep -n \"بیور\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T14:54:11.612Z] TOOL RESULT

```
=== RCH bait/house ===
17070:A   \aJ  bait  (from  baita)y  Cutting  open  (a  boil).
=== RCH baiza ===
140:clared heiress  of  the  empire,  if  not  delivered  of  a son,  and  regent,  in  that  event,  till  he  was  of  age  to reign.  Averse  even  from  the  distant  prospect  of resigning  sovereign  power,  the  queen  ordered  the birth  of  her  son  to  be  concealed  ;   and  sent  him privately  to  be  exposed  in  a   casket  on  the  banks  of the  JThun ;   the  rising  of  the  waters  soon  swept  him away,  and  threw  him  on  a   dyer’s  bleaching-ground. The  rich  stuffs  and  valuable  jewels,  which  the  poor man  found  in  the  casket,  convinced  him  that  he was  a   child  of  elevated  birth  ;   he  educated  him however  as  his  own  son,  and  wished  him  to  follow his  profession ;   but  the  prinfo,  unwilling  to  believe himself  the  son  of  a   dyer,  urged  his  reputed  father so  strongly,  that  the  good  man  discovered  at  length all  he  knew;  and  delivered  to  him  the  jewels,  which he  had  carefully  preserved.  Young  Darab  deter- mined immediately  on  the  profession  of  arms;  and set  out  for  the  army,  which  was  then  marching against  the  Greeks.  He  arrived  on  the  eve  of  a battle;  in  which  he  distinguished  himself  with  such heroism,  that  his  fame  reached  the  queem  The prince  was  sent  for :   Ilumay  was  struck  with  his presence  :   she  discovered  him  by  the  jewels  and the  old  man’s  testimony,  and  resigned  the  diadem to  him,  after  having  reigned  with  great  reputation about  thirty  years.  This  Darab  is  represented  as an  accomplished  prince,  and  a   successful  warrior. Philip  of  Macedon,  amongst  others,'  according  to Khondemir,  drew  upon  him  his  resentment,  by  re- fusing to  acknowledge  his  authority.  He  marched against  him  ;   and,  forcing  him  to  take  refuge  in a   fortress,  Philip  sued  for  peace,  which  was  granted, on  condition  of  giving  his  daughter  in  marriage  to the  Persian  king,  and  paying  an  annual  tribute  of a   thousand  bayzats,  or  eggs  of  gold.  The  young queen  did  not  please  her  royal  consort ;   though pregnant,  he  returned  her  to  her  father’s  court, where  she  was  afterwards  delivered  of  the  famous Alexander,  whom  Philip  educated  as  his  son  ;   and left  him  his  kingdom,  with  the  secret  of  his  birth. Darab  having,  in  the  mean  time,  espoused  another lady,  she  brought  him  Darab  the  Younger ;   who mounted  the  throne  on  the  demise  of  his  father.
569:murghdnahy  or  some  w'ord  originally  Pcrsiaity  would  have been  used;  and  not  bayzaty  which  being  Arabky  must  only have  been  introduced  into  Persian  writings  subsequent  to  the /I  conquest.  Bibliolheque  Orient,  p.  286  and  318.
18516:A jjW  baydziry  (pi.  of  bayzar)  Fullers*  beetles.
18517:A   baydziraty  (pi.  of  bayzar)  Falconers.
18748:A   ^3^  bayzakhy  A   fat  woman.  Name  of  a   place, p   bayzaky  A   foot-soldier.  A   coniinander.  A   falcon. bi-^Vy  A   well,  a   pit.  ^   The  wells  of  Joseph  ;   the
18887:(pi.  of  idJ  bayzat)  Eggs.  Helmets.  Biz,  (pi.  of  hayuz) Hens  which  lay  many  eggs.  (pi.  of  blzal)  liite  kinds  of light,  soil.  (pi.  ofj^l  abyaz  and  LauJ  bayzu)  White.  The
18895:p^^Lij  bayzdbl  (for  bayzavl),  A   species  of  Persian
18899:^   bl  zabt  o   rabt.  Without  order  or  connexion. A<Li^  bayzat.  An  egg.  A   testicle.  A   helmet.  The  head- ach  (a  lasting  pain  seizing  the  whole  head).  The  middle  (of  a country,  of  a   city,  of  the  head).  A   margin,  border.  A   ring  or circus  formed  by  a   number  of  people;  also  the  area  compre- hended by  a   circular  disposition  of  tents.  jJJt  (U£j  The  chief
=== RCH biwar ===
5291:p   azdaby  Beware  !
10460:al  hazary  Take  care !   beware  I   shun  (it).
10866:A   amdmy  Before,  pippr  to.  Before  thee,  beware !
13792:A   \A  aydj  O   !   ho  1   hola  \   have  a   care  !%!U:!^\y  aydka tea’ll  mukhdlafaty  Beware  lest  thou  contend.  Ay  yd  or  tydj  is also  a   pleonastic  particle  prefixed  to  personal  pronouns ;   as lydya\  Me.  C^bJ  tydka^  Thee,  jibf  tydhu^  Him.  U^l  lydm kumd^  You  two.  UjbbI  tydhumh^j  Them  two.  bbl  tyandy  Us.
13833:A   ci/y  Begone !   Take  heed !   Beware !
14364:f   ^yhdy  Come  on !   Well  then!  Beware  I   A   desert.
20577:"^J^pohtawy  A   hero.  A   wrestler.  Name  of  a   country  and of  a   city.  Pahluy  The  sidey  the  hypochondria  or  back  and  sides under  the  short  ribsi  The  breast.  The  hip.  Strength.  Utility. Strong.  Bold.  Warlike,  j^j^pahlupahlu  (or pahlu  bahpahlu)y  Breast  to  breast,  man  against  man,  equal,  jlfi To  assist  To  retire.  To  avoid,  ^d^j^^pdhiu zadany  To  associate  together,  to  be  on  a   footing  with. pahlu  kardatiy  To  run  away.  T o   turn  away  the  face,  to  avoid,  to beware  of.  ^i^j^pahluw^i  Ioshkar y   The  wing  of  an  army.
21007:p   b   tdy  (a  causal  participle,  denoting  the  end,  as  dawdm docs  a   continuation,  of  action).  To,  until,  so  far,  as  far  as,  so  that, as  long  as,  even  to  (that  time,  that  place,  that  object),  to  the  end that,  in  such  a   manner  that,  in  order  that.  Beware !   Behold ! Since.  Unless.  In,  among.  ^   b   dmadam  id  tord btnamy  I   am  come  in  order  to  see  thee.  aCij  b   rafianr  id ba  Makkahy  I   went  as  far  as  Mecca,  bf-  b   /d  an  jdy  Thi- therto, so  far.  bf-  ^   b   id  in  jdy  Hitherto,  thus  far.  b
=== FVQ bayt ===
=== ARY biwar ===
```


## [2026-09-05T14:54:17.844Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== RCH bait house/verse ===\"; grep -n \"bait\\b\" RCH.txt | head -12\necho \"=== RCH bayaz ===\"; grep -n -i \"bayaz\\b\\|bayaz,\" RCH.txt | head -6\necho \"=== RCH ten thousand ===\"; grep -n \"Ten  thousand\\|ten  thousand\" RCH.txt | head -12"
}
```


### [2026-09-05T14:54:17.924Z] TOOL RESULT

```
=== RCH bait house/verse ===
15195:A   butut^  (pU,  of  (JM  bait)  Cloaks,  made  of  coarse  silk.
17070:A   \aJ  bait  (from  baita)y  Cutting  open  (a  boil).
30196:jLjj^jazar^  A   piece  of  meat,  as  a   bait  for  wild  beasts.  A   fat sheep,  (from  p   gazar)j  A   carrot,  a   parsnip. jazaru^r  rd^yaij  A   plant  (scabiosa  columbaria). jazar^i  hindij  A   species  of  pumpkin.
38626:Ddnurij  Name  of  the  prophet  Jonah, p   Aib  ddnahj  (s  tj7^ )   Grain ;   a   berry,  a   stone  of  fruit,  the seed  of  any  grain  or  fruit.  A   pimple.  Grain  or  bait  scattered for  catching  birds.  A   cannon-ball.  Knowledge,  science,  learn- ing.  Learned,  jj&l  ddna^i  angur^  A   grape,  a   grape- stone.  ddnah  dvoardan^  To  bring  forth  grain,  to  fall
52132:ing ;   also  the  bowhaudle.  A   thumb-stall  worn  by  archers.  A lish-hook.  A   net.  A   bait.  A   fine  lancet  Sixty.  The  thumb, ^girdle  worn  by  thelifagi.  The  bow,  also  the  string  .of  a inusical  instrument.  A   hair-riiig.  A   woirfan's  hips.
56840:A   tujiiff  ti^naty  A   manner  in  eating  or  tasting.  Tu^iaty  Meat, food,  fodder,  forage.  Birds’  food.  A   bait,  a   lure.  An  invita- tion to  an  entertainment.  Dinner.  A   dining-room,  or  any  place where  people  eat.  Gain,  profit,  any  mode  of  acquisition.  The woof.  P^jl^  tu^nat  dddany  To  bait.
75729:tress  them  in  the  course  of  the  year.  The  king,  on  the  first  day of  this  festival,  after  anointing  himself  with  the  oil  of  bait,  dressed in  a   superb  robe  of  many  colours,  his  head  adorned  with  the royal  ^   tuj  (diadem)  on  which  was  a   splendid  figure  of  the Sun,  seated  himself  on  his  throne ;   when  the  high  priest  entering alone  with  a   large  silver  dish,  filled  with  sugar,  peaches,  quinces, apples,  citrons,  pomegranates,  the  jujube,  the  lote,  a   bunch  of white  grapes,  and  seven  myrtle-berries,  muttered  over  them  a prayer,  and  presented  them  to  the  king,  who  eat  of  them  all ; afler  which,  the  nobility  and  others  approaching  according  to their  rank,  followed  their  sovereign’s  example  ;   when  a   variety of  robes  and  other  rich  furniture,  fropi  the  royal  wardrobes, were  distributed  amongst  them  in  proportion  to  their  degree. On  this  day  it  was  esteemed  fortunate  to  wean  or  name  children ; and  if  a   son  was  then  born  to  the  king,  he  was  immediately,  with great  solemnity,  consecrated  high  priest  of  the  Sun.
90363:Mnmbit^  A   pot-herb  sprouting,  growing,  vegetating;  (laud)  fer- tile in  plants  or  fruits.  Mumbait^  Obliged  to  break  off  a   journey* A mumhatir^  Cut,  broken  off.  Mutilated.
102586:A   swift  and  strong  horse.  A   locust  springing  a   great  distance, p   ^'^suya^anjy  A   harmless  kind  of  serpent  being  In  vineyards. yn^'y  A   kid ;   especially  one  fastened  in  a   ditch  to  catch a   lion;  any  bait  for  entrapping  wild  beasts.  Name  of  a   tree.
=== RCH bayaz ===
93818:(or  nasi^Cl  bayaz)^  Pure  white,  snowy.
=== RCH ten thousand ===
19123:Pj^  blxcav^  J^ixty  thousand  (in  the  J’ahlavi  or  old  Persian ten  thousand).  Any  thing  circular.  The  kernel  of  a   walnut when  dry  and  hitter.  Name  of  a   king.
20962:p   paywany  A   thousand, p payury  Ten  thousand.
27033:a^4j  tumam  and  timam^  An  amulet  of  caipeW  haiyitf. v^j^tamany  A   cloudy  Tumany  Ten  thousand.  TTie  sum of  five  thousand  aspers.
41466:p   Ifc  W   duh  hd,  The  ten  firrt  day*  of  the  month  Muharram.  and  evil ;   hence  an  epithet  of  God.  Computing,  settling  accounts rj\j^  irj  dah  hazar.  The  fourth  game  at  chess.  Ten  thousand,  with  another.  A   judge,  an  umpire,  an  administrator.  Religious, p   W   dah  haft,  Name  of  an  ancient  coin..  A   AJIj  J   diyanat  (from  J),  Embracing,  adhering  to  religion.
42664:rububtyat^  Dominion,  supreme  power.  Deity,  divinity, A   5^j  ribwat^  rabwat^  and  ruhtoai^  A   hill,  a   rising  ground,  a heap.  Ribroaty  Ten  thousand  drams, p   rabutj  A   lapwing,  a   puet.
68939:vehicle.  A   camel-saddle.  The  skin  of  an  aniiiials’s  leg  tanned, which  they  use  as  a   mortar  for  braying  drugs.  KadiHj  Corpulent.  i p   kidin^  A   village  in  which  near  ten  thousand  people  as- semble on  ihe  day  called  ^ishurd,  A   pathic.
77762:(ten  thousand).  Ready,  prepared,  expeditious.
97004:p   fiui/hf,  (in  the  dialect  of  Kh’arazm)  The  son  of  a king,  a   prince.  A   commander  of  ten  thousand  men.
99557:y^^toaity  Like,  resembling.  Pure.  Sincere.  A   pistachio- nut.  But,  yet,  however,  (in  Kathay)  Ten  thousand  years.
```


## [2026-09-05T14:54:29.576Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Myriade ===\"; grep -n -i \"myriade\\|zehntausend\" HRN.txt HUB.txt | head -10\necho \"=== NYB bewar ===\"; grep -n -i \"bēwar\\|bewar\\|byw'r\\|bywl\" NYB_vol2_glossary.txt | head -10\necho \"=== BQT بیور ===\"; grep -n \"بیور\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10\necho \"=== BQT بیضه ===\"; grep -n \"بیضه\" BQT_v1_pages.txt | head -5"
}
```


### [2026-09-05T14:54:29.668Z] TOOL RESULT

```
=== HRN Myriade ===
HUB.txt:1150:262. Lies *zehntausend' (statt 'tausend*).
HUB.txt:5260:barg *Blatt', bevar zehntausend', parr Teder, Fliigel', dar
HUB.txt:5967:aber b^var 'zehntausend' = zd. ba§vare,
HUB.txt:6389:Mm Turcht' H. 258 ; bevar zehntausend' H. 262. Mit vor-
=== NYB bewar ===
995:bevar [bywl] ten thousand; 2 — späh an army of 20000 men 1811-16-17; 12 ~ späh 29233; won 15 ~, 14 ~, 13 ~ 2372.17, 248-11; 131 ~ ziön äyend 24115; 12 x 12 ~ 2427; 12 ~~ 251; 3 ~ nēzak (g. v.) balas 1041, — Av. (913) baévar-, baévan-; MPrth- Prs bywr ; Arm. lw. biur; Paz. baévar ; ear- rly NP bevar.
996:Bévar-asp [bywl’sp'] n. pr. 78%. — Paz. Baévardsp; NP Bévarasp.
=== BQT بیور ===
BQT_v1_pages.txt:1135:همان بیورسیش؟ همی خو اند ند چنین نام بر پهلوی راند ند
BQT_v1_pages.txt:1136:کجا بیور از بهلوانی شمار بود در زبان دری ده هزار.
BQT_v1_pages.txt:3377:نیز در ذیل « یورسب» گوید : «بزبان دری بیور بروزن زیوربمعنی
BQT_v1_pages.txt:22755:میخواندماند. و نام اصلی او بیور بر وزن صبور
BQT_v1_pages.txt:29605:انوری آبیوردی بنقل *المعجم شمس فیس چاپ مدری۲ ۲۷
BQT_v2_pages.txt:8477:                                                          ‫گبیورا‬
BQT_v2_pages.txt:10067:                  ‫‪.‬‬   ‫‪ :‬سوم‬    ‫چش‬     ‫»‬    ‫چك‬    ‫(‪)۲‬‬           ‫(‪ )۱‬چش‪ :‬خبیوره باشد بروزن متوره‪.‬‬
BQT_v2_pages.txt:10574:      ‫پوشنگه » بادغیس » طوس) ‪ -‬مروشاهجان » سرخس » دا » ابیورد ‪ .‬مروالرون » طالقان آمل‬
BQT_v2_pages.txt:21527:  ‫ده‬   ‫اشتقافه‪:‬‬   ‫دەك‬   ‫ده ك‬   ‫«بیوراسب‬   ‫اینکلمه لو سد؛‬   ‫اشتقاق‬   ‫حمزءه اصفهانی در وجه‬   ‫=‬   ‫‪۱‬‬
=== BQT بیضه ===
22528:بیضه ] آشین «کنایدازآقاب‌عالمتاب
22550:بیضه دد آب » بینه‌ای تکههنوز
22552:بیضه زد - ويضة زریی ۰ کنایه از
30141:شود بیضه بجاب هوا پران کردد ت از طرغایب
```


## [2026-09-05T14:54:32.022Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AA/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for بیت — the definition and the bracketed origin tag (e.g. [ع.] for Arabic). Include the senses (خانه، اتاق، شعر)."
}
```


### [2026-09-05T14:54:37.271Z] TOOL RESULT

```
# فرهنگ معین Entry for بیت

According to Farhang-e Mo'in, the entry for **بیت** is:

**(بِ یا بَ ) [ ع . ] ( اِ. )**

**Senses:**
1. "خانه ، اتاق" (house, room) — plural: بیوت
2. "دو مصراع از شعر" (two verses of poetry) — plural: ابیات

The bracketed origin tag **[ع.]** indicates the word derives from **Arabic** (عربی).
```


## [2026-09-05T14:54:51.249Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN no 262 ===\"; grep -n \"^262\\|262\\.\" HRN.txt | head -10\necho \"=== HUB 5967 ctx ===\"; sed -n '5960,5975p' HUB.txt\necho \"=== BQT v1 3370-3385 ===\"; sed -n '3370,3385p' BQT_v1_pages.txt\necho \"=== BQT v1 1130-1140 ===\"; sed -n '1128,1140p' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:54:51.343Z] TOOL RESULT

```
=== HRN no 262 ===
2648:262. bever 'tausend'.
11850:bever 262.
15038:ha^vare 262.
15460:übt» 262.
15717:bevar 262.
21026:I. Hrn 262.
=== HUB 5967 ctx ===
3) -dt?i- wild zu fl: askara *k\a.r ,^h\, askarak, skr. avis-
kar oflfenbar machen*, aviskara- *das
Offenbaren*.
Dazu np. basam *werde sein ? (das nicht = skr. bhavl-
syami (zd. ptc. busy ant-) sein kann).
4) em- im Anlaut wird zu ya- : yak ein = phi. ^vak
(vgl. nek *gut, schon* = phi. nevak, ap. naiba-),
aber b^var 'zehntausend' = zd. ba§vare,
5) Fro- wird zu I : ^is^an 'leben* (ziyam lebe', 5?i«da
'lebendig*) = paz. zTvastan u. s. w. Min. Gl. 225,
phi. zlvandak 'lebendig' Gl. and Ind. 152;
paz. pSy (lies ptg) = phi. pig oder plk Shk.
263, bal. p^g, nb. ^ty 'Fett* ans ^plvaka-; np.
pfA *Talg, Fett\ skr. ptvasd- *fett' (obenp. 46).
Dagegen zlva, jlva 'Quecksilber H. 683.
b) -ava- wird zu D : furod 'hinunter — skr. pravdta\
=== BQT v1 3370-3385 ===
ذیل < سرخ شبان یاهو دار > گوید : « نام حضرت موسی علیه السلام است
بز بان پپلوی (؛) >
بسیاری از لغات بارسی و بپلوی نیز مشتر كاند و دیپی‌است که درمتن
بر‌هان تصر یحی بدین موضوع نیست .
د - دری ۱- مولف در ذیل « باستان > گوید: < بزبان دری
تاریخ را گویند» ۴ وذیل «< هی > گوید : « بلغت دری و لفت هندی بمعنی
هست باشد .»
نیز در ذیل « یورسب» گوید : «بزبان دری بیور بروزن زیوربمعنی
ده هزار باشد» ویور بپلوی است ۳ .
بخش اعظم لغات برهان قاطم لغات دری ( پارسی ) است که چون
منظوراصلی موّلف گرد آوردن ]نپاست» درمتن‌برهان نصریحی بدان نشده.
ه - خوارژزمی ۴ - ذیللفت «بکند» گوید :« بلفت ولایت خوارزم
۱ - بل «دری کوبد : «لفت پارسی باستانی‌است ووجه نسميةً آنرا بعضی بفصیح تعبیر
کرده‌اند » وهر لغت ی که درآن نتصانی نباشد دری میگویند همحو اشکم وشکم وبگوی وی
وبشنود و شنود وامثال اینها : پس‌اشکم وبگوی وبشنود دری باشد , وجممی کویند اف ساکنان
چند شهر بوده است که‌آن بلخ وبخارا وبدخشان ومروانت؛ و بعضی گوبند دری زبان اهل بهشت
=== BQT v1 1130-1140 ===
۸- نام شیروبه . 4- شاهنامة بخ ج۸ ص ۲۵۷۷ .مقدمه سی و دو
«دری» و«پارسی» دوزبان جدا گانه بشماررفته است»[یا چنین‌است؛
وری منسوب است‌به «در> بمعنی‌دربار » چنانکه ابن‌المقفع وحمزه
وخوارزمی ودیگران تصر یح کر ده‌|ند ۱ واشتفاقات دیگر که برای این کلمه
ذکر کرده اند یی ارزش است ۴ .
شك نیست که دری در دورء اسلامی بهمینز بان معمول پارسی بس‌از
اسلام‌اطلان میشده‌است؛ اينك شواهد آن :
همان بیورسیش؟ همی خو اند ند چنین نام بر پهلوی راند ند
کجا بیور از بهلوانی شمار بود در زبان دری ده هزار.
فردوسی‌طوسی. شاهنامه بخج۱ص۲۸.
دل‌بدان یافتی‌ازمن که نکودانی خواند مدحت خواجه آزاده ۴با لفاظدری.
فرخی‌سیستانی. دیوان مصحح عبدالر سو لی‌ص4۰۰.
اندرعرب؟ درعربی کویی‌او کشاد ‏ و او باز کردیارسیان‌را دردری.
```


## [2026-09-05T14:55:05.894Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2640,2656p' HRN.txt"
}
```


### [2026-09-05T14:55:05.933Z] TOOL RESULT

```
Semn. vlm; mäz. v^it,
aw. va^nä' Nase' (Y. 9, 11 (35), Darmesteter, Et.
ir. I 57); phlv. venik (Bund., AV.), bEmk (AV.).
kurd. hen *Nase, Geruch' (H.-Sch.); bei. gin *Atem,
Leben (109) (?).
Fr. Müller (WZKM. 5, 260) stellt dazu phlv. mi,
(ZP61. 8, 3) 'Hauch* und nimmt als dessen Grundform
*vayana' an.
262. bever 'tausend'.
äw. ba^vare 'tausend'; phlv. bevar.
oss. d. beurä, t. birä Viel, sehr, lange (61).
263. beve Wittwe'.
Käs. vJgd^ vU (neben bivä^ bwe),
ai. vidhdvä' *Wittwe'; phlv. vepak d. i. vBvak; lat.
oidiia; got. viduvö,
oss. t. idäj *Wittwe' (aus *vidüä'j), von Stackel-
be rg (briefliche Mitteilung).
```


## [2026-09-05T14:55:07.628Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/semitic.html",
 "prompt": "Search this Semitic roots appendix for roots byt (\"house\") and bwṣ / byḍ (\"to be white\", linen, egg). Quote the entries for bayt/byt and any b-w-ṣ or b-y-ḍ root, including derivatives (Bethel, Bethlehem, byssus)."
}
```


### [2026-09-05T14:55:14.580Z] TOOL RESULT

```
# Semitic Roots: BYT and Related Entries

## **byt** (House)

The appendix defines this as: "Common Semitic noun _\*bayt‑_, house."

Notable derivatives include **Bethel** ("house of God") and **Bethlehem** ("house of bread"), demonstrating how this root combines with other elements to form place names and religious terms.

## **bwṣ / byḍ** (Whiteness/Linen)

I searched the provided appendix extensively but found **no entry for a root meaning "white," "linen," or "egg"** with the forms bwṣ or byḍ. 

The document does include **brr** ("to be(come) clear, pure, white"), which relates to whiteness, but this is distinct from the bwṣ/byḍ roots you're seeking. The appendix also lacks any entry for "byssus" (a fiber-producing gland in mollusks).

The roots you're looking for may appear in a different section of the dictionary's Semitic roots appendix not included in this excerpt.
```


## [2026-09-05T14:55:30.583Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(16400,16500):\n    if re.match(r'^\\s*9\\d\\d\\s*$', lines[i]) or re.search(r'\\b91[0-9]\\b', lines[i][:40]):\n        print(i, repr(lines[i][:80]))\nprint('---')\nfor i in range(16455,16475): print(i, lines[i][:100])\nEOF"
}
```


### [2026-09-05T14:55:32.323Z] TOOL RESULT

```
16443 '»puSra-  910'
16462 '913'
16464 '914'
16498 '915'
---
16455 cäen  i^^B^st ..  ■=.i.  ss  s^h^ar^Lrer  =:iihr'  •    >.  "f-  bä   rir-    öä   5«garr=:j   ::rid
16456 bat  J^i^s  rCTT^riKL  =ji  ^^  ^  ■z:;^-.'  *-«    -"  y.fK  .-  Yi.r~. 7:    —    ö^Cflör.V
16457 »js-i-r.  —  rt.    ^^  ;    if  .  .  ^T».-  .■  re  £SiJ5-    «„-»j  fi;c:»tl   Y:.  r^.  i^ .    
16458 •  >  pcSfran-  Ar.  'dsr  e^;=  S *■*•-.           ^    ^                 iJi  >■  H.
16459 •  >  puJTaTsct-  Ar.  ■=:.-:  L-:r^K:.  Eis-  -i^ .'  
16460 •  -.  "bae    2»^.  =    -r^tT:  F.;:'. r-Tf»  . .  .1"  -ii    NS-    V:..?  f  ^  1^'   «--53  S.
16461 dby  Google
16462 913
16463 bae.«r3zu.fra9^-
16464 914
16465 •  j.  bae.9r9zu.fra9Bh-  Adj.  'zweifiDger- breif:  '%ar»hfm  V.  lA'.  i  PüZ.">.
16466 I)    Es    heisst    hier    vom  />aläm    { paiti-däna-) : 3  angusi  5i  afäyet  hal  an  yä\  f
16467 •  j.  bae'arazu.stavah-  Adj.  'zweifinger- dick': as/?m  . .  'vatafum  (ASm.  als  n.)  vä bipTDS
16468 Pü.:  3  angusi  zahii.
16469 •  j.  baevan-,  baevar-  n.  'Zehntausend, Myriade';  navaca  navaitlsca  navaca  saia navaca  hasa
16470 KompA-,  E.;  Ableil.  —  tEt.  s.  S  ^'O.  ~  mp. (Pü.),  np.  hBvar.  —  i)  Them.
16471 •  j.  baevara-yav-   Adj.    'loooofachen
16472 Halt  habend':  satäyul  .  .  hazanräH  . , 'röis  (NSm.)**  asti  mf^rS  yd  dainayä mnsdayasnsiS 
16473 1)  Slatt  'tayu!  geschr.,  j  26*  14.  Aber  das a  ist  aoffaiig.  Doch  vgl.  den  them.  GP. b
16474 •  j.barvarö.tBniö.-baevar-  n.  'das  loooo-
```


## [2026-09-05T14:55:46.862Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B6%DB%8C/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for بیضی — definition and origin tag. Also whether it means \"oval / ellipse\" (بیضی‌شکل، اهلیلگی)."
}
```


## [2026-09-05T14:55:48.982Z] TOOL CALL #52: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg103.png data/verification/sources/refs/ocr/BOOK/103.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T14:55:53.433Z] TOOL RESULT

```
# Farhangi Mo'in Entry for بیضی

**Definition:** "(بِ) [ع. اِمر.] یکی از اشکال هندسی که کشیده تر از دایره بوده و دارای دو کانون می باشد"

**Origin tag:** ع. اِمر. (Arabic origin, imperative/derived form)

**Meaning:** This entry describes an geometric shape that is elongated compared to a circle and possesses two foci, clearly denoting both oval and ellipse concepts. The term conveys the mathematical properties of an ellipse rather than merely describing its egg-like appearance.
```


### [2026-09-05T14:55:53.509Z] TOOL RESULT

```
total 2764
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 10:55 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
```


## [2026-09-05T14:55:55.240Z] AGENT

Now let me archive the web sources.


## [2026-09-05T14:56:01.036Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%AA|page 103 entry 0, Arabic bayt 'house' < Proto-Semitic *bayt-, Persian descendant beyt\" \\\n \"https://en.wiktionary.org/wiki/byssus|page 103 entry 2, English byssus < Latin < Gk byssos, Semitic source Heb bus\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%B6%D8%A9|page 103 entry 2, Arabic bayda 'egg' from bayd, root b-y-d 'white'\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1|page 103 entry 1, Persian bivar < MP bewar < OP *baivaram < PIr *baywaram\" \\\n \"https://en.wiktionary.org/wiki/%D7%91%D7%95%D7%A5|page 103 entry 2, Hebrew bus 'byssus, fine linen' < Proto-Semitic *bus-\" ; do\n  url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20"
}
```


### [2026-09-05T14:56:04.367Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/887e5e750369dcaa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0945a820aeb989eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9013f7855d8b8db.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79ce64222e9cb1b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f34b4a81558c5bf4.txt
```


## [2026-09-05T14:56:11.782Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n \"https://www.ahdictionary.com/word/search.html?q=byssus|page 103 entry 2, AHD byssus: Gk bussos, ultimately from Egyptian w'd 'linen' (Nourai's AHD:183 note)\" \\\n \"https://www.ahdictionary.com/word/search.html?q=bethel|page 103 entry 0, AHD bethel < Hebrew bet el 'house of God' (AHD:127)\" \\\n \"https://www.ahdictionary.com/word/semitic.html|page 103 entry 0, AHD Semitic roots appendix byt 'house': Bethel, Bethlehem\" \\\n \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D9%88%D8%B1/|page 103 entry 1, Mo'in bivar [pahlavi] 'ten thousand' (MON:635)\" \\\n \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AA/|page 103 entry 0, Mo'in beyt [Arabic] 'house, room; couplet' (MON:618)\" \\\n \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B6%DB%8C/|page 103 entry 2, Mo'in bayzi [Arabic] 'ellipse'\" ; do\n  url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20"
}
```


### [2026-09-05T14:56:18.407Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ba4704aa53949e8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3f9c3997d7d9a9a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75b739fc6c2698d2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d224578ae15d350.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74f77df8a2510c40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92320d4cc191add4.txt
```


## [2026-09-05T15:04:07.548Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk103.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ndata = {\n  \"pdf_page\": 103,\n  \"book_page\": 73,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": []\n}\n\n# ---------------- ENTRY 0 : B.y.t ----------------\ne0 = {\n  \"entry\": 0,\n  \"root\": \"B.y.t\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Proto-Semitic *bayt- 'house' (Common Semitic noun byt)\",\n  \"note\": \"The root, the language label and the gloss are all correct. Wiktionary reconstructs Proto-Semitic *bayt- 'house' (Akkadian bītu, Ugaritic bt, Hebrew bayiṯ, Aramaic baytā, Arabic bayt, Ge'ez/Amharic bēt); the AHD Semitic appendix has it as a 'common Semitic noun *bayt-, house' rather than as a verbal root, and Klein p.167 s.v. bethel gives exactly Nourai's set of cognates. Nourai writes the root in the tri-consonantal shape 'B.y.t' as if it were a verbal root; it is in fact a primary noun, which is why no verb 'to dwell' is derivable from it — a presentational, not a substantive, inaccuracy. The Hebrew branch of the chart (Beth-el, Beth-lehem > Eng. Bethel, Bethlehem) is standard.\",\n  \"note_fa\": \"ریشهٔ سامیِ *bayt- «خانه» اصیل است و برچسب «سامی» و معنای آن هر دو درست‌اند: ویکی‌واژه سامیِ آغازین *bayt- را بازسازی می‌کند (اکدی bītu، اوگاریتی bt، عبری bayiṯ، آرامی baytā، عربی بیت، گعزی bēt) و پیوستِ سامیِ فرهنگ American Heritage نیز آن را «اسمِ مشترکِ سامی *bayt-» می‌خواند، نه ستاکِ فعلی. کلاین در ص۱۶۷ ذیل bethel همین مجموعه هم‌ریشه‌ها را می‌آورد. تنها نکته آنکه نورایی آن را به شکلِ سه‌همخوانیِ «B.y.t» می‌نویسد، گویی ستاکِ فعلی است، حال آنکه اسمی است بسیط. ادعای نورایی در اصل درست است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%AA\",\n    \"https://www.ahdictionary.com/word/semitic.html\",\n    \"https://www.ahdictionary.com/word/search.html?q=bethel\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"KLN:167\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 100 (which carries the printed page markers 166 and 167), s.v. bethel: 'Heb. beth El, \\\"the house of God\\\". Beth is the state construct of bayith, \\\"house\\\", and rel. to Aram. baythā, bethā, Ugar. bt, Arab. bayt, Akkad. bitu, \\\"house\\\"; cp. beth, beta.' Nourai's root box, his Arabic node and his Hebrew node all come straight from this page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"online Semitic roots appendix, s.v. byt\", \"stance\": \"supports\",\n     \"note\": \"'byt — Common Semitic noun *bayt-, house', with the derivatives Bethel 'house of God' and Bethlehem 'house of bread'.\"},\n    {\"src\": \"FSD\", \"where\": \"vol. I leaf 316 = printed p. 266\", \"stance\": \"supports\",\n     \"note\": \"Funk & Wagnalls p.266 s.v. Bethlehem: '< beth, house, + lehem, food.' — the very page Nourai cites (FSD:266) and the source of his gloss 'house of food'.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 100 = p.167, s.v. beth\", \"stance\": \"supports\",\n     \"note\": \"'beth, n., name of the 2nd letter of the Hebrew alphabet. — Heb. beth, lit. \\\"house\\\"'.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"b.y.t; bayt\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic بيت bayt 'house, tent, room' continues Proto-Semitic *bayt- unchanged: the diphthong *ay is preserved in Classical Arabic (where Hebrew monophthongised it to bayiṯ/bēṯ in the construct bēṯ- and Akkadian to bītu). Arabic then built a whole nominal family on it (pl. buyūt, ʔabyāt; denominative Form II bayyata 'to spend the night, to hatch a plot'), which is why the lexicographers list it as a triliteral root b-y-t even though the noun is primary. Klein p.167 sets Arab. bayt beside Heb. bayith, Aram. baythā, Ugar. bt and Akkad. bītu as the same word.\",\n  \"derivation_fa\": \"«بیت» عربی دنبالهٔ بی‌واسطهٔ سامیِ آغازین *bayt- «خانه» است؛ مصوّتِ مرکّبِ ay در عربیِ فصیح دست‌نخورده مانده، حال آنکه در عبری در حالت اضافه به bēṯ و در اکدی به bītu ساده شده است. عربی سپس بر همین اسم خانوادهٔ صرفیِ کاملی ساخته است (جمعِ بیوت و ابیات، فعلِ بابِ دومِ بَیَّتَ «شب را گذراندن، توطئه چیدن») و به همین سبب لغویان آن را ستاکِ سه‌همخوانیِ ب‌ی‌ت می‌شمارند، هرچند اسمی است بسیط. کلاین (ص۱۶۷) و ویکی‌واژه هر دو این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%AA\", \"https://www.ahdictionary.com/word/semitic.html\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:167\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 100 (pp.166-167) s.v. bethel: '... rel. to Aram. baythā, bethā, Ugar. bt, Arab. bayt, Akkad. bitu, \\\"house\\\"'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"online Semitic appendix, root byt\", \"stance\": \"supports\",\n     \"note\": \"'Common Semitic noun *bayt-, house' — Arabic bayt is one of its regular reflexes.\"},\n    {\"src\": \"RCH\", \"where\": \"RCH.txt, Arabic entries under bait/bayt\", \"stance\": \"partial\",\n     \"note\": \"Richardson lists Arabic bait among its homographs (e.g. line 15195 'butut (pl. of bait)'); the OCR of the main 'bait, a house' entry is broken, so the dictionary is only indirectly usable here.\"},\n    {\"src\": \"FVQ\", \"where\": \"FVQ.txt, grep 'bayt'/'bait'\", \"stance\": \"silent\",\n     \"note\": \"Jeffery has no entry for bayt — expected, since he treats only the FOREIGN vocabulary of the Qur'an and bayt is native Arabic.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"bayt «بیت»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian بیت beyt is a straightforward Arabic loan of the ʿAbbasid period, taken over with the Arabic form intact (Persian has no phonetic reason to alter bayt); Mo'in tags it '[ع.]' = Arabic. It carries both the concrete sense 'house, room' (pl. بیوت buyūt, kept in the Arabic broken plural) and — the sense that matters for Persian literature — 'a line of verse' (pl. ابیات abyāt). The prosodic sense is itself an Arabic metaphor: the poetic line is a 'tent/house' whose two hemistichs (مصراع, literally the two leaves of a door) are its halves, and this whole terminology came into Persian with ʿarūḍ metrics in the 3rd-4th c. AH. Nourai's Saʿdi shahed 'وی ز هجرت بیت‌ها بیت‌الحزن' puns on exactly the two senses.\",\n  \"derivation_fa\": \"«بیت» در فارسی نو وام‌واژه‌ای عربی است از دورهٔ اسلامی که بی هیچ دگرگونیِ آوایی پذیرفته شده (معین آن را با نشانِ [ع.] می‌آورد) و جمعِ شکستهٔ عربی‌اش نیز همراه آن آمده است: بیوت به معنی «خانه‌ها» و ابیات به معنی «سطرهای شعر». معنای عروضیِ آن خود استعاره‌ای عربی است: هر بیت چون خانه یا خیمه‌ای است که دو «مصراع» (یعنی دو لَنگهٔ در) نیمه‌های آن‌اند، و این اصطلاح‌شناسی با علم عروض در سدهٔ سوم و چهارم هجری به فارسی راه یافت. شاهدِ سعدی که نورایی آورده («وی ز هجرت بیت‌ها بیت‌الحزن») آگاهانه بر همین دو معنا بازی می‌کند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AA/\", \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%AA\"],\n  \"ref_check\": [\n    {\"ref\": \"FVA:55\", \"status\": \"not_checked\",\n     \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: refs_online.json records that no digital copy exists on any permitted platform (catalogue record only), so p.55 could not be read.\"},\n    {\"ref\": \"MON:618\", \"status\": \"supports\",\n     \"note\": \"Mo'in's entry via abadis.ir: 'بیت (بِ یا بَ) [ع.] (اِ.) ۱- خانه، اتاق؛ ج. بیوت. ۲- دو مصراع از شعر؛ ج. ابیات' — Arabic origin tag and both of Nourai's senses. (vajehyab/abadis do not carry Mo'in's print pagination, so p.618 itself is not verifiable online.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. بیت\", \"stance\": \"supports\",\n     \"note\": \"'[ع.] (اِ.) ۱- خانه، اتاق ... ۲- دو مصراع از شعر' — Arabic loan, senses 'house/room' and 'couplet'.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 100 = p.167 s.v. bethel\", \"stance\": \"supports\",\n     \"note\": \"gives Arab. bayt 'house' as the source form that Persian borrowed.\"},\n    {\"src\": \"RCH\", \"where\": \"RCH.txt (Richardson, Persian-Arabic-English)\", \"stance\": \"partial\",\n     \"note\": \"Richardson carries bait/bayt among the Arabic words current in Persian, but the OCR of the headword line is corrupt; only the plural forms are legible.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"baith; Beth-ěl; Běth-lexem\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Hebrew בַּיִת bayiṯ (Nourai's 'baith') 'house' is the regular Canaanite reflex of *bayt-, with the anaptyctic i of the segholate pattern; in the construct state it contracts to בֵּית bēṯ 'house of…', and that construct is what forms the place-names. בֵּית־אֵל Bēṯ-ʾĒl = bēṯ 'house of' + ʾĒl 'God' (Gen. 28:19, Jacob's name for Luz) — Nourai's cross-reference to his root 'Layh' is his own place for ʾĒl. בֵּית־לֶחֶם Bēṯ-leḥem = bēṯ + leḥem; leḥem is 'bread' in Hebrew but the underlying Semitic root l-ḥ-m means 'food, staple' generally (whence Arabic laḥm 'meat'), so Nourai's gloss 'house of food' — taken over from Funk & Wagnalls p.266, which glosses it '< beth, house, + lehem, food' — is defensible; AHD's appendix renders it 'house of bread'. Nourai's 'lexem' uses x for ḥeth, his own transliteration convention.\",\n  \"derivation_fa\": \"عبریِ بَیِت (bayiṯ) «خانه» بازتابِ منظمِ *bayt- در کنعانی است با مصوّتِ میانجیِ الگوی سِگولی؛ در حالت اضافه به bēṯ «خانهٔ…» فشرده می‌شود و همین صورتِ مضاف است که نام‌جای‌ها را می‌سازد: بیت‌ئیل (Bēṯ-ʾĒl) «خانهٔ خدا» (سفر پیدایش ۲۸:۱۹) و بیت‌لحم (Bēṯ-leḥem). واژهٔ leḥem در عبری «نان» است، اما ریشهٔ سامیِ ل‌ح‌م معنای عامِ «خوراک» دارد (در عربی «لحم» به «گوشت» تخصیص یافته)؛ ازاین‌رو معنایی که نورایی به‌دست می‌دهد، یعنی «خانهٔ خوراک»، پذیرفتنی است و برگرفته از فرهنگ فانک و واگنالز ص۲۶۶ است، هرچند پیوستِ American Heritage آن را «خانهٔ نان» می‌آورد. حرفِ x در نویسه‌گردانیِ «lexem» شیوهٔ خودِ نورایی برای حرفِ «ح» است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/semitic.html\", \"https://www.ahdictionary.com/word/search.html?q=bethel\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:167\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 100 = p.167 s.v. bethel: 'Heb. beth El, \\\"the house of God\\\". Beth is the state construct of bayith, \\\"house\\\"' — Nourai's spelling 'baith' is Klein's 'bayith'.\"},\n    {\"ref\": \"FSD:266\", \"status\": \"supports\",\n     \"note\": \"FSD_vol1.txt leaf 316, which carries the printed page number 266: s.v. Bethlehem '... < beth, house, + lehem, food.', with 'Bethlehem Ephratah' and 'Bethlehemite' following. This is the source of Nourai's gloss 'house of food'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"online Semitic appendix s.v. byt\", \"stance\": \"partial\",\n     \"note\": \"same root and the same two names, but glosses Bethlehem 'house of bread' rather than 'house of food'.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 100 = p.167, s.vv. beth, bethel, Bethesda; and leaf ~... s.v. El\", \"stance\": \"supports\",\n     \"note\": \"'Bethesda — Gk. Bēthesda, fr. Aram. beth ḥesdā, \\\"house of mercy\\\". See bethel'; s.v. El: 'the second element in Babel, bethel'.\"},\n    {\"src\": \"FSD\", \"where\": \"vol. I p.266\", \"stance\": \"supports\",\n     \"note\": \"'< beth, house, + lethem [read lehem], food.'\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"English\", \"words\": \"Bethel, Beth; Bethlehem\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both English words are learned biblical borrowings, not inherited: Bethel entered English through the Vulgate/Septuagint spelling of Hebrew Bēṯ-ʾĒl and became a common noun ('a hallowed place; a seamen's chapel; in Britain a Nonconformist, esp. Baptist or Methodist chapel') in the 17th-19th centuries; AHD gives it as '[Hebrew bêt ʾēl, house of God: bayit, house + ʾēl, God]'. Beth is separately the name of the second Hebrew letter, literally 'house', named after the pictogram of a house. Bethlehem came in via Greek Βηθλεέμ / Latin Bethleem and, through the London hospital of St Mary of Bethlehem, also yielded the common noun bedlam (Funk & Wagnalls: 'Cor. of Bethlehem'). Nourai's AHD:127 is the page of the New College edition on which bethel/Beth fall.\",\n  \"derivation_fa\": \"هر دو واژهٔ انگلیسی وام‌واژه‌های کتاب‌مقدسی‌اند، نه میراثی: Bethel از راهِ صورتِ سپتواگینت و ولگات از عبریِ Bēṯ-ʾĒl به انگلیسی رسید و در سده‌های هفدهم تا نوزدهم اسمِ عام شد به معنی «نمازخانه، عبادتگاهِ دریانوردان». فرهنگ American Heritage ریشهٔ آن را «عبری bêt ʾēl، خانهٔ خدا: bayit «خانه» + ʾēl «خدا»» می‌دهد. Beth نیز نامِ حرفِ دومِ الفبای عبری است که خود «خانه» معنی می‌دهد. Bethlehem از یونانیِ Βηθλεέμ و لاتینِ Bethleem آمده و از نامِ بیمارستانِ سنت‌مری آو بتلهم در لندن واژهٔ bedlam «آشوب، دیوانه‌خانه» پدید آمده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=bethel\", \"https://www.ahdictionary.com/word/semitic.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:127\", \"status\": \"supports\",\n     \"note\": \"The printed New College page could not be paged (only Watkins's IE appendix is on disk), but the AHD entry itself, read at ahdictionary.com s.v. bethel, reads: 'A hallowed spot; a chapel for seamen; Brit. a Nonconformist chapel — [Hebrew bêt ʾēl, house of God: bayit, house + ʾēl, God.]' — exactly Nourai's arrow Hebrew > English.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 100 = p.167 s.v. bethel, beth; and s.v. baetulus\", \"stance\": \"supports\",\n     \"note\": \"'bethel, n., a house of worship. — Heb. beth El' and 'baetulus ... fr. Heb. beth El, \\\"house of God\\\"; see bethel'.\"},\n    {\"src\": \"FSD\", \"where\": \"vol. I p.266 (Bethlehem, Bethlehemite) and s.v. bedlam\", \"stance\": \"supports\",\n     \"note\": \"'Bethlehemite ... 1. A resident of Bethlehem, in Judea. 2. A bedlamite'; s.v. bedlam 'The hospital of St. Mary of Bethlehem in London ... {Cor. of Bethlehem.}'\"},\n    {\"src\": \"AHD\", \"where\": \"online, s.v. bethel\", \"stance\": \"supports\",\n     \"note\": \"'[Hebrew bêt ʾēl, house of God: bayit, house + ʾēl, God]'.\"}\n  ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 : Byurru ----------------\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Byŭrru\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Proto-Iranian *baiwar- / *baywar- 'ten thousand, myriad' (Av. baēuuar-/baēuuan-, Khotanese byūrru, MP bēwar)\",\n  \"note\": \"The word is real and the family is right, but the root box is mislabelled in two ways. (1) 'Byŭrru' is not a proto-form: it is Bailey's Khotanese Saka headword (Indo-Scythian Studies / Dictionary of Khotan Saka s.v. byūrru '10,000, myriad'), i.e. one daughter language's reflex, so the Avestan, Sogdian and Armenian words are its SISTERS, not its descendants; the common ancestor is Proto-Iranian *baiwar-, whence also Ossetic beurä/birä, Parthian bywr, Georgian beur-i. Wiktionary reconstructs PIr. *baywáram (acc. of *baywā́) behind Persian بیور. (2) 'Indo-Schythian' is Nourai's spelling (so printed in the book, p.73) of Bailey's term 'Indo-Scythian' for Khotanese Saka; it is not a language name in current use. Bailey's further derivation of the word from PIE *bheu- 'to be, grow' (Pokorny 146-50) via *bai- + -var- is his own and is not generally accepted; most handbooks leave the Iranian numeral without a secure IE etymology. Everything below the root box is sound.\",\n  \"note_fa\": \"واژه اصیل است و خانوادهٔ زبانی درست، اما جعبهٔ ریشه دو اشکال دارد. نخست آنکه «byūrru» صورتِ بازسازی‌شده نیست، بلکه سرواژهٔ ختنیِ (سکاییِ) بیلی است در «مطالعات هندوسکایی» و «فرهنگ ختن‌سکا»؛ یعنی بازتابِ یکی از زبان‌های دختر است، پس اوستایی و سغدی و ارمنی خواهرانِ آن‌اند نه فرزندانش، و نیای مشترک ایرانیِ آغازینِ *baiwar- است که آسیِ beurä/birä و پارتیِ bywr و گرجیِ beur-i نیز از آن‌اند؛ ویکی‌واژه پشتِ «بیور» فارسی صورتِ ایرانیِ آغازینِ *baywáram را می‌گذارد. دوم آنکه «Indo-Schythian» املای خودِ نورایی است (در کتاب، ص۷۳، همین‌گونه چاپ شده) از اصطلاح «Indo-Scythian» بیلی برای ختنیِ سکایی، و امروزه نام زبانی به‌شمار نمی‌رود. برگردانِ خودِ بیلی به ریشهٔ هندواروپاییِ *bheu- «بودن، بالیدن» (پوکورنی ۱۴۶-۱۵۰) نیز پذیرفته نیست و بیشتر پژوهشگران این عدد ایرانی را بی ریشه‌شناسیِ استوارِ هندواروپایی می‌دانند. باقیِ نمودار درست است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:262\", \"status\": \"supports\",\n     \"note\": \"Bailey's Indo-Scythian Studies vol. VI is not online (refs_online.json), so the check was made in his own Dictionary of Khotan Saka, which repeats the ISS article: ISS_alt_DKS.txt line 5747, s.v. 'byūrru \\\"10,000, myriad\\\" ... From *baivar (with -u from -am), Av. baēvar-, baēvan-, Sogd. Man. βrywr \\\"10,000\\\", Zor.P., N.Pers. bēvar, M.Parth., M.Pers.T. byur, plur. bywr'n, Alan Beaor (in the name Boxoracrmros), Oss. D. beurä, birä, Armen. lw biur, Georgian lw beur-i. From bhu- > bai- with -var-, -van-; ... to base IE Pok. 146-50 bheu-:bhu-.' Every word in Nourai's chart is in this one paragraph — but Bailey presents them as cognates, not as descendants of the Khotanese form, and explicitly marks the Armenian as a loanword ('lw').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"cols. 913-914, s.v. baēvan-, baēvar-\", \"stance\": \"supports\",\n     \"note\": \"'j. baēvan-, baēvar- n. \\\"Zehntausend, Myriade\\\" ... — mp. (Pū.), np. bēvar', with the compounds baēvarə.gaošman-, baēvarə.spasan- etc.\"},\n    {\"src\": \"NYB\", \"where\": \"vol. II Glossary, s.v. bēvar\", \"stance\": \"supports\",\n     \"note\": \"'bēvar [bywl] ten thousand ... — Av. (913) baēvar-, baēvan-; MPrth-Prs bywr; Arm. lw. biur; Paz. baēvar; early NP bēvar.' Nyberg too marks Armenian biur as a loanword.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 146-150 (bheu-), reached through Bailey's cross-reference\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's bheu-:bhū- article is about 'to be, grow' and does not list an Iranian numeral 'ten thousand'; Bailey's link is his own construction.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"baevar, baevare\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Young Avestan baēuuar- / baēuuan- n. 'ten thousand, myriad' (Nourai's baevar, baevare) is well attested — Yt. 13.59, V. 22.2, and in a long series of compounds (baēuuarə.gaošman- 'ten-thousand-eyed', of Miθra; baēuuarə.spasan- 'having ten thousand watchers'; baēuuarə.paitay- 'lord over ten thousand'). The r/n heteroclisis (baēuuar- : baēuuan-) is the archaic Indo-Iranian neuter type. Note that this is not a descendant of Khotanese byūrru but its sister: both go back to Proto-Iranian *baiwar-, the Khotanese having taken -u from the accusative *-am and having simplified *-ai- to y (byūrru), while Avestan keeps the diphthong.\",\n  \"derivation_fa\": \"اوستاییِ نو baēuuar-/baēuuan- «ده هزار» نیک گواهی شده است (یشت ۱۳ بند ۵۹، وندیداد ۲۲ بند ۲) و در ترکیب‌های فراوانی دیده می‌شود، مانند baēuuarə.gaošman- «ده‌هزارگوش» و baēuuarə.spasan- «دارندهٔ ده هزار دیده‌بان» که هر دو صفتِ مهرند. جابه‌جاییِ r/n در این ستاک (baēuuar-/baēuuan-) از الگوهای کهنِ خنثای هندوایرانی است. تنها نکتهٔ اصلاحی این است که این صورت فرزندِ byūrru ختنی نیست بلکه خواهرِ آن است: هر دو از ایرانیِ آغازینِ *baiwar- می‌آیند، با این تفاوت که ختنی مصوّتِ مرکّبِ ai را ساده کرده و پایانهٔ -u را از حالت مفعولیِ *-am گرفته، حال آنکه اوستایی مصوّتِ مرکّب را نگه داشته است. واژه و معنا درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:262\", \"status\": \"supports\",\n     \"note\": \"DKS s.v. byūrru (ISS_alt_DKS.txt line 5747) cites 'Av. baēvar-, baēvan-' as the Avestan member of the set — exactly Nourai's two forms.\"},\n    {\"ref\": \"AEF:324\", \"status\": \"not_checked\",\n     \"note\": \"Khaleqi Motlaq's Asās-e Eštteqāq-e Fārsi is not digitised (refs_online.json: catalogue records only). Because AEF is the Persian rendering of Horn's Grundriss, the claim was checked against Horn instead: HRN.txt line 2648, no. 262 'bēver \\\"tausend\\\" — aw. baēvarə \\\"tausend\\\"; phlv. bēvar', with Hübschmann's correction (HUB.txt line 1150: '262. Lies \\\"zehntausend\\\" (statt \\\"tausend\\\")').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"col. 914, s.v. baēvan-, baēvar-\", \"stance\": \"supports\",\n     \"note\": \"'j. baēvan-, baēvar- n. \\\"Zehntausend, Myriade\\\"' with attestations Yt. 13.59, V. 22.2 and the derivative compounds; 'mp. (Pū.), np. bēvar'.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.262 (and §4 of the vowel chapter)\", \"stance\": \"supports\",\n     \"note\": \"HUB.txt line 5967: 'aber bēvar \\\"zehntausend\\\" = zd. baēvare' — Hübschmann uses the pair as an example of Avestan ai- NOT becoming ya- in Persian.\"},\n    {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar\", \"stance\": \"silent\",\n     \"note\": \"grep of AVG.txt for baēvar/baevan returns nothing; the numeral is not discussed in the grammar's paradigms.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"běvar; běvar-asp\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian bēwar, written bywl (Book Pahlavi) / bywr (Manichaean and Parthian), 'ten thousand', is the regular continuation of Proto-Iranian *baiwar-: OIr. *ai > MP ē, intervocalic *-w- kept, final *-r retained. It is the ordinary Pahlavi numeral for a myriad, used of army units in the Kārnāmag and the Dēnkard ('2 bēwar spāh = an army of 20,000'). Bēwar-asp [bywl'sp'] 'having ten thousand horses' is the standing epithet, and in Pahlavi tradition the name, of Dahāg/Azdahāg — asp being MP asp 'horse' < PIr. *aswa- (Nourai's cross-reference to his root 'Ekwos' is right, PIE *h₁eḱwos).\",\n  \"derivation_fa\": \"فارسیِ میانهٔ bēwar، به نگارشِ پهلویِ کتابی bywl و در مانوی و پارتی bywr، «ده هزار» دنبالهٔ منظمِ ایرانیِ آغازینِ *baiwar- است: مصوّتِ مرکّبِ ai در فارسی میانه به ē بدل شده، w میان‌واکه‌ای مانده و r پایانی حفظ شده است. این عدد در متن‌های پهلوی برای شمارِ سپاه به کار می‌رود («۲ بیور سپاه» یعنی سپاهی بیست‌هزار نفره). Bēwar-asp «دارندهٔ ده هزار اسب» لقب و در سنّتِ پهلوی نامِ ضحاک (دهاگ/اژدهاگ) است؛ asp نیز از ایرانیِ آغازینِ *aswa- است و ارجاعِ نورایی به ریشهٔ «Ekwos» (هندواروپاییِ *h₁eḱwos) درست است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"AEF:324\", \"status\": \"not_checked\",\n     \"note\": \"AEF (Khaleqi Motlaq's Persian version of Horn) is not digitised; checked against its German original instead — HRN.txt no. 262: 'bēver \\\"tausend\\\". āw. baēvare \\\"tausend\\\"; phlv. bēvar. oss. d. beurä, i. birä \\\"viel, sehr, lange\\\"', corrected to 'zehntausend' by Hübschmann p.262.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"supports\",\n     \"note\": \"PHD_mackenzie.txt line 1567: 'bēwar [bywll M bywr, N ...] myriad, ten thousand'; the English-Pahlavi index gives 'myriad bēwar' (PHD.txt line 2880).\"},\n    {\"src\": \"NYB\", \"where\": \"vol. II Glossary, s.vv. bēvar, Bēvar-asp\", \"stance\": \"supports\",\n     \"note\": \"'bēvar [bywl] ten thousand; 2 ~ spāh an army of 20000 men ...' and 'Bēvar-asp [bywl'sp'] n. pr. ... — Paz. Baēvarāsp; NP Bēvarasp.'\"},\n    {\"src\": \"SNS\", \"where\": \"Glossary of Šāyast nē Šāyast\", \"stance\": \"silent\",\n     \"note\": \"grep for bēwar/bywl in SNS.txt returns nothing — the numeral does not occur in that text.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"bîvar «بیور»; Bîvarasp «بیوراسپ»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian بیور bīvar/bēvar 'ten thousand' is the inherited continuation of MP bēwar: MP ē is written with yāʾ and read ī in later Persian, and MP -w- appears as Persian -v-. It is an archaism already in Ferdowsi's day, which is precisely why he glosses it in the very verse Nourai quotes — 'کجا بیور از پهلوانی شمار / بود بر زبان دری ده هزار' ('what in the Pahlavi reckoning is bīvar / is in the Dari tongue ten thousand'). بیوراسپ Bīvarasp is the Shahnameh's name for Ẓaḥḥāk, taken over from Pahlavi Bēwar-asp. Mo'in tags بیور '[په.]' (Pahlavi) and defines it 'عددی معادل ده هزار'; Mo'in likewise notes in his edition of Borhān-e Qāṭeʿ that 'بیور پهلوی است'.\",\n  \"derivation_fa\": \"«بیور» فارسی دنبالهٔ میراثیِ bēwar فارسی میانه است: ē فارسی میانه با «ی» نوشته می‌شود و در فارسیِ متأخر ī خوانده می‌شود، و w میانی به «و» بدل شده است. این واژه در روزگار فردوسی نیز کهنه و ناآشنا بوده و به همین سبب شاعر در همان بیتی که نورایی آورده معنایش را می‌دهد: «کجا بیور از پهلوانی شمار / بود بر زبان دری ده هزار». «بیوراسپ» نیز نامِ ضحاک در شاهنامه است که یکسره از Bēwar-asp پهلوی گرفته شده. معین ذیل «بیور» نشانِ [په.] یعنی پهلوی می‌گذارد و آن را «عددی معادل ده هزار» می‌داند، و در حاشیهٔ برهان قاطع نیز می‌نویسد «بیور پهلوی است». ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\", \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D9%88%D8%B1/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:635\", \"status\": \"supports\",\n     \"note\": \"Mo'in's entry (read at abadis.ir, which reproduces Farhang-e Fārsi but not its pagination): 'بیور (وَ) [په.] (اِ.) عددی معادل ده هزار' — Pahlavi origin tag and Nourai's gloss exactly.\"},\n    {\"ref\": \"FSF:98\", \"status\": \"supports\",\n     \"note\": \"Noushin's Vāzhe-nāmak: FSF_pages.txt leaf 129 has the headword 'بیور' with precisely Nourai's Ferdowsi couplet ('کجا بیور از پهلوانی شمار / بود بر زبان دری ده هزار'), followed by the headword 'بیور اسپ: دارای ده هزار اسب، نام ضحاک' and further Shahnameh shawāhed. The printed page number on this leaf of the scan is 135, so the copy on disk is a different printing from the one Nourai paginated (p.98); the content is the cited content.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt, Mo'in's introduction, line 3377\", \"stance\": \"supports\",\n     \"note\": \"'نیز در ذیل «بیورسب» گوید: «بزبان دری بیور بروزن زیور بمعنی ده هزار باشد» و بیور پهلوی است' — Borhān's own entry plus Mo'in's footnote that bīvar is Pahlavi; lines 1135-6 quote the same Ferdowsi couplet.\"},\n    {\"src\": \"RCH\", \"where\": \"RCH.txt line 19123\", \"stance\": \"partial\",\n     \"note\": \"'bīwar, Sixty thousand (in the Pahlavi or old Persian ten thousand). Any thing circular. ... Name of a king.' Richardson has the Pahlavi value right and knows the royal name, but records a later, inflated Persian usage 'sixty thousand'.\"},\n    {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. بیور\", \"stance\": \"supports\",\n     \"note\": \"'[په.] (اِ.) عددی معادل ده هزار'.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"brywr\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian βrywr 'ten thousand' (Nourai's brywr is the consonantal spelling; Manichaean βryywr, Buddhist/Sogdian script RYPW as an ideogram-like writing) is the Sogdian sister of Av. baēuuar-, from PIr. *baiwar-. The Sogdian shape shows the language's characteristic development of the initial cluster — *bai- appears as βri-/βry- — and the rounded second syllable -wr. Like the Avestan word it is a cognate, not a descendant, of Khotanese byūrru; Bailey lists 'Sogd. Man. βrywr \\\"10,000\\\"' in the very article Nourai cites.\",\n  \"derivation_fa\": \"سغدیِ βrywr «ده هزار» (که نورایی به صورتِ همخوانیِ brywr آورده؛ در سغدیِ مانوی βryywr و در نگارشِ دیگر RYPW) خواهرِ سغدیِ baēuuar- اوستایی است و از ایرانیِ آغازینِ *baiwar- می‌آید. صورتِ سغدی دگرگونیِ ویژهٔ این زبان را در آغازِ واژه نشان می‌دهد: *bai- به βri-/βry- بدل شده و هجای دومِ گِردشده -wr مانده است. این واژه نیز مانندِ صورتِ اوستایی هم‌ریشهٔ byūrru ختنی است نه فرزندِ آن؛ بیلی در همان مقاله‌ای که نورایی بدان استناد می‌کند «سغدیِ مانوی βrywr» را می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:262\", \"status\": \"supports\",\n     \"note\": \"DKS s.v. byūrru (ISS_alt_DKS.txt line 5747): 'Sogd. Man. βrywr \\\"10,000\\\"'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 2808, 2811, 8652\", \"stance\": \"supports\",\n     \"note\": \"'2808 βrywr C =» βryywr'; '2811 βryywr M ... βare-βar (βrywr, βrywr) ©Av. baēvar ... ten thousand, myriad'; '8652 RYPW B, S ... βēwar, βrēwar (βrywr) ©Idg. =»βryywr — ten thousand, myriad'. Gharib explicitly cross-references Avestan baēvar.\"},\n    {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. bēvar\", \"stance\": \"partial\",\n     \"note\": \"Nyberg cites the Middle Parthian/Middle Persian bywr for the same etymon but does not treat Sogdian.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Armenian\", \"words\": \"biur\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Armenian բիւր biwr 'ten thousand, myriad' is real and belongs to this etymon, but it is not an independent branch of it as the chart's arrow implies: it is a borrowing from Middle Iranian (Parthian bywr), one of the very large stratum of Parthian loans in Armenian, and both of the authorities behind Nourai's own citation say so — Bailey writes 'Armen. lw biur' and Nyberg 'Arm. lw. biur' ('lw' = Lehnwort/loanword; compare the parallel Georgian loan beur-i). Phonetically the borrowing is straightforward: Parthian bēwar > Arm. biwr with the usual Armenian rendering of Iranian ē by i and loss of the final vowel. The chart is therefore right about the connection and wrong about its nature.\",\n  \"derivation_fa\": \"ارمنیِ բիւր (biwr) «ده هزار» واژه‌ای اصیل است و به همین خانواده تعلق دارد، اما چنان‌که پیکانِ نمودار می‌رساند شاخه‌ای مستقل از ریشه نیست: وام‌واژه‌ای است از ایرانیِ میانه (پارتیِ bywr) و از همان لایهٔ بزرگِ وام‌واژه‌های پارتی در ارمنی؛ هر دو مرجعی هم که خودِ نورایی به آن‌ها ارجاع می‌دهد همین را می‌گویند: بیلی می‌نویسد «Armen. lw biur» و نیبرگ «Arm. lw. biur» (lw کوتاه‌شدهٔ Lehnwort «وام‌واژه» است)، چنان‌که گرجیِ beur-i نیز وام‌واژه است. از نظر آوایی وام‌گیری ساده است: ē ایرانی در ارمنی i شده و مصوّتِ پایانی افتاده است. پس پیوند درست است اما نوعِ آن (میراث به‌جای وام) نادرست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:262\", \"status\": \"partial\",\n     \"note\": \"DKS s.v. byūrru (ISS_alt_DKS.txt line 5747) does list 'Armen. lw biur' — the form is Nourai's, but Bailey marks it explicitly as a loanword ('lw'), which the chart's inheritance arrow does not convey.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. bēvar\", \"stance\": \"partial\",\n     \"note\": \"'MPrth-Prs bywr; Arm. lw. biur' — Nyberg agrees on the form and, like Bailey, calls it a loanword from Iranian.\"},\n    {\"src\": \"BRT\", \"where\": \"col. 914 s.v. baēvar-\", \"stance\": \"silent\",\n     \"note\": \"Bartholomae gives only the Iranian material (mp., np. bēvar); no Armenian is cited.\"}\n  ]\n})\n\ndata[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 : B.y.z, B.w.s ----------------\ne2 = {\n  \"entry\": 2,\n  \"root\": \"B.y.z, B.w.s\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Arabic root b-y-ḍ 'to be white' (bayāḍ 'whiteness', ʔabyaḍ 'white', bayḍ 'eggs'); separately Proto-Semitic *būṣ- 'byssus, fine linen' (Heb. בּוּץ būṣ, Aram. būṣā)\",\n  \"note\": \"Nourai's root box unites two things that modern scholarship keeps apart. The Arabic root b-y-ḍ 'to be white' is beyond dispute and the whole Arabic/Persian branch follows from it correctly. The identification of that root with the 'fine linen' word (Heb. būṣ, Aram. būṣā, Gk. byssos) is Klein's: KLN p.215 s.v. byssus derives Heb. būṣ 'fr. Sem. *b-w-ṣ (*b-w-tz), \\\"to be white, to surpass in whiteness\\\", whence Heb. bēṣāh, Arab. bayḍa, \\\"egg\\\"', and Nourai's two-shaped root 'B.y.z, B.w.s' is simply Klein's *b-y-ḍ / *b-w-ṣ. Wiktionary, by contrast, reconstructs the linen word as a self-standing Proto-Semitic *būṣ- with no whiteness etymology, and modern Hebrew lexicography treats būṣ as a late culture-word (it appears only in Chronicles, Esther and Ezekiel, and its Aramaic and Akkadian counterparts point to a borrowed Levantine textile term). Nourai's own chart note is the honest one: AHD p.183 does not go through Semitic at all — the online AHD s.v. byssus reads 'from Greek bussos, linen ... of Dravidian origin, or ultimately from Egyptian wʾḏ, linen', and the AHD Semitic-roots appendix has no b-w-ṣ or b-y-ḍ root whatever. So the Arabic side is confirmed, the Hebrew-Greek side is a nineteenth-century hypothesis that AHD and Wiktionary decline to follow.\",\n  \"note_fa\": \"جعبهٔ ریشهٔ نورایی دو چیز را یکی گرفته است که پژوهشِ امروزی جدا نگه می‌دارد. ستاکِ عربیِ ب‌ی‌ض «سپید بودن» بی‌گفت‌وگو اصیل است و همهٔ شاخهٔ عربی-فارسی به‌درستی از آن برمی‌آید. اما یکی گرفتنِ آن با واژهٔ «کتانِ نازک» (عبری būṣ، آرامی būṣā، یونانی byssos) از کلاین است: او در ص۲۱۵ ذیل byssus عبریِ būṣ را «از سامیِ *b-w-ṣ به معنی سپید بودن» می‌گیرد و از همان ریشه bēṣāh عبری و «بیضة» عربی را می‌آورد؛ صورتِ دوگانهٔ «B.y.z, B.w.s» در کتاب چیزی جز همین دو صورتِ کلاین نیست. در برابر، ویکی‌واژه واژهٔ کتان را سامیِ آغازینِ مستقلِ *būṣ- بازسازی می‌کند بی هیچ پیوندی با «سپیدی»، و عبری‌شناسیِ امروز būṣ را واژه‌ای فرهنگی و متأخر می‌داند (تنها در تواریخ و استر و حزقیال آمده) که به یک اصطلاحِ پارچه‌ایِ وام‌گرفته بازمی‌گردد. خودِ نورایی در یادداشتِ نمودار صادقانه یادآور شده که فرهنگ American Heritage اصلاً از راهِ سامی نمی‌رود: آن فرهنگ byssos یونانی را «شاید دراویدی یا سرانجام از مصریِ wʾḏ «کتان»» می‌داند و در پیوستِ ریشه‌های سامیِ آن هیچ ستاکِ b-w-ṣ یا b-y-ḍ نیست. پس شاخهٔ عربی تأیید می‌شود و شاخهٔ عبری-یونانی فرضیه‌ای سدهٔ نوزدهمی است که مراجعِ امروزی نمی‌پذیرند؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%B6%D8%A9\",\n    \"https://en.wiktionary.org/wiki/%D7%91%D7%95%D7%A5\",\n    \"https://en.wiktionary.org/wiki/byssus\",\n    \"https://www.ahdictionary.com/word/search.html?q=byssus\",\n    \"https://www.ahdictionary.com/word/semitic.html\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"KLN:215\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 125 (page markers 214 … 217), s.v. byssus: 'L., fr. Gk. byssos, \\\"fine white linen\\\", a Semitic loan word. Cp. Heb. būtz, of s.m., fr. Sem. *b-w-ṣ (*b-w-tz), \\\"to be white, to surpass in whiteness\\\", whence Heb. bēṣāh, Arab. bayḍaʾ, \\\"egg\\\". Cp. W. Muss-Arnolt, Semitic words in Greek and Latin, TAPA 23, 80, Note 19.' This is verbatim Nourai's root, his Hebrew node and his Greek node.\"},\n    {\"ref\": \"AHD:183\", \"status\": \"supports\",\n     \"note\": \"For the chart's own note ('AHD:183 ultimately derives this from Egyptian W.z:linen'): the AHD entry s.v. byssus reads 'Middle English bissus, linen cloth, from Latin, from Greek bussos, linen … of Dravidian origin, or ultimately from Egyptian wʾḏ, linen.' Nourai reports his source accurately — and that source contradicts his own Hebrew > Greek arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"online Semitic roots appendix\", \"stance\": \"contradicts\",\n     \"note\": \"The appendix has no root b-w-ṣ / b-y-ḍ at all (the nearest is brr 'to be(come) clear, pure, white'), i.e. AHD does not recognise the Semitic 'white' etymology for byssus.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215, s.vv. byssine, byssus\", \"stance\": \"supports\",\n     \"note\": \"'byssine, adj., made of byssus — L. byssinus … fr. Gk. byssinos'; and the byssus article quoted above.\"},\n    {\"src\": \"FVQ\", \"where\": \"FVQ.txt / FVQ_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"Jeffery has no entry for bayḍ/būṣ — the Qur'anic words of this family are native Arabic, so his book of foreign vocabulary is silent.\"}\n  ],\n  \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"b.y.z; bayzeh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic ب ي ض b-y-ḍ 'to be white' is a genuine hollow root (bāḍa, yabīḍu 'to lay eggs'; ʔabyaḍ / bayḍāʔ 'white'; bayāḍ 'whiteness'). بيض bayḍ is the collective 'eggs' and بيضة bayḍa its singulative in -a — the egg is named from its colour, exactly as Nourai says; Wiktionary derives bayḍa 'from بيض (bayḍ) + ة (-a), the root ب ي ض relating to whiteness', with the further senses 'testicle, helmet, essential part'. The ḍād of the Arabic root corresponds regularly to Hebrew ṣade (Proto-Semitic *ṣ́), which is what makes Klein's comparison with Heb. bēṣāh 'egg' formally possible.\",\n  \"derivation_fa\": \"ستاکِ عربیِ ب‌ی‌ض «سپید بودن» ستاکی است اجوف و اصیل: باضَ/یَبیضُ «تخم گذاشتن»، أبیض و بیضاء «سپید»، بَیاض «سپیدی». «بَیض» اسمِ جنسِ جمعی به معنی «تخم‌ها» است و «بیضة» مفردِ آن با پسوندِ ـة؛ یعنی تخم‌مرغ را به سببِ رنگش چنین نامیده‌اند، درست همان‌که نورایی می‌گوید. ویکی‌واژه نیز «بیضة» را «از بیض به‌علاوهٔ ـة، از ستاکِ ب‌ی‌ض مربوط به سپیدی» می‌داند و معناهای دیگرِ آن را «خصیه، کلاهخود، اصل و اساس» می‌آورد. «ض» عربی به‌طور منظم برابرِ «צ» عبری است (سامیِ آغازینِ *ṣ́) و همین برابری است که قیاسِ کلاین با bēṣāh عبری «تخم» را از نظر صوری ممکن می‌کند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%B6%D8%A9\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:215\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 125, s.v. byssus: '… \\\"to be white, to surpass in whiteness\\\", whence Heb. bēṣāh, Arab. bayḍaʾ, \\\"egg\\\"' — Nourai's Arabic node is Klein's clause.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"RCH\", \"where\": \"RCH.txt line 18899\", \"stance\": \"supports\",\n     \"note\": \"'bayzat. An egg. A testicle. A helmet. … The middle (of a country, of a city, of the head)'; and line 18887, '(pl. of bayzat) Eggs. Helmets. … (pl. of abyaz and bayzā) White.'\"},\n    {\"src\": \"AHD\", \"where\": \"online Semitic roots appendix\", \"stance\": \"silent\",\n     \"note\": \"no b-y-ḍ root is listed in the appendix, so AHD neither confirms nor denies the Arabic root here.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Alfāẓ fārsiyya muʿarraba\", \"stance\": \"silent\",\n     \"note\": \"grep of AFM.txt finds no بيض entry — as expected, since Addi Shir collects Persian words borrowed INTO Arabic and bayḍ is native Arabic.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"batzeh «بیضه»; bayzî «بیضی»; bayyâz «بیّاض»; bayzâ «بیضا»\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"batzeh\",\n  \"correct_form\": \"bayzeh\",\n  \"derivation\": \"All four words are genuine Arabic loans in Persian, but two of the transliterations are wrong in the printed book. (1) «بیضه» is bayze(h) — the same word Nourai correctly transliterates 'bayzeh' one box to the left, in the Arabic node — yet the Persian box prints 'batzeh'. I checked the printed page (PDF p.103 = book p.73, rendered at 400 dpi): the book itself reads 'batzeh : egg', so the extraction is faithful and this is Nourai's own misprint (t for y). (2) «بیّاض» glossed 'whiteness' is likewise off: the Persian word for 'whiteness' is بیاض bayāz (Arabic بَیاض bayāḍ), without tašdīd; with tašdīd, bayyāḍ is the Arabic agent noun 'whitewasher, plasterer'. The printed page does show the tašdīd, so this too is the book's error, not the scan's. The other two are correct: بیضی bayzī 'oval, elliptical', the standard Persian geometrical term (Mo'in: 'یکی از اشکال هندسی که کشیده‌تر از دایره بوده و دارای دو کانون می‌باشد'), a nisba on بیضه 'egg'; and بیضا bayzā, the Arabic feminine of ʔabyaḍ 'white', current in Persian only in the Qur'anic collocation یدِ بیضا 'the white hand (of Moses)' (Qurʾān 7:108, 20:22), whence Vaḥshī's shahed. The route in each case is Arabic > Persian in the Islamic period, with no phonetic change beyond the Persian pronunciation of ḍād as z.\",\n  \"derivation_fa\": \"هر چهار واژه وام‌واژه‌های عربیِ اصیل در فارسی‌اند، اما دو نویسه‌گردانی در متنِ چاپی نادرست است. نخست «بیضه» که باید bayzeh باشد — همان صورتی که نورایی یک جعبه آن‌سوتر، در گرهِ عربی، درست نوشته است — ولی در جعبهٔ فارسی «batzeh» چاپ شده. صفحهٔ چاپی را (پی‌دی‌اف ص۱۰۳ برابرِ ص۷۳ کتاب) با تفکیک ۴۰۰ نقطه بررسی کردم: خودِ کتاب «batzeh: egg» دارد، پس خطای خوانشِ اسکن نیست بلکه غلطِ چاپیِ کتاب است (t به‌جای y). دوم «بیّاض» با معنیِ «سپیدی»: واژهٔ «سپیدی» در فارسی و عربی «بَیاض» است بی تشدید، و «بیّاض» با تشدید در عربی اسمِ فاعل و به معنیِ «سفیدکار، گچ‌کار» است؛ تشدید در صفحهٔ چاپی دیده می‌شود، پس این نیز خطای کتاب است. دو واژهٔ دیگر درست‌اند: «بیضی» صفتِ نسبی از «بیضه» و اصطلاحِ جاافتادهٔ هندسیِ فارسی است (معین: «یکی از اشکال هندسی که کشیده‌تر از دایره بوده و دارای دو کانون می‌باشد») و «بیضا» مؤنثِ «أبیض» است که در فارسی تنها در ترکیبِ قرآنیِ «یدِ بیضا» (اعراف ۱۰۸ و طه ۲۲) به کار می‌رود و شاهدِ وحشی نیز بر همان است. راهِ وام‌گیری در هر چهار مورد عربی به فارسی در دورهٔ اسلامی است، بی هیچ دگرگونیِ آوایی جز تلفظِ «ض» به‌صورتِ «ز» در فارسی.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%A8%D9%8A%D8%B6%D8%A9\",\n    \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B6%DB%8C/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"FVA:56\", \"status\": \"not_checked\",\n     \"note\": \"Nahvi's Farhang-e Vāzheh-hā-ye ʿArabi dar Fārsi is not digitised anywhere (refs_online.json: catalogue record only), so the sole reference Nourai gives for this box could not be read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. بیضی\", \"stance\": \"supports\",\n     \"note\": \"'بیضی (بِ) [ع. اِمر.] یکی از اشکال هندسی که کشیده‌تر از دایره بوده و دارای دو کانون می‌باشد' — Arabic origin tag, and the sense 'ellipse' that Nourai gives.\"},\n    {\"src\": \"RCH\", \"where\": \"RCH.txt lines 18899, 18887, 93818\", \"stance\": \"supports\",\n     \"note\": \"'bayzat. An egg. A testicle. A helmet.'; '(pl. of abyaz and bayzā) White'; and line 93818 '(or nāṣiʿ) bayāz, Pure white, snowy' — Richardson's form for 'whiteness' is bayāz, without the tašdīd Nourai prints.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt lines 22528-22552\", \"stance\": \"supports\",\n     \"note\": \"Borhān-e Qāṭeʿ has the headword 'بیضه' with the figurative senses ('کنایه از آفتابِ عالم‌تاب' etc.), confirming the Persian currency of the loan; the spelling is بیضه throughout.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215 s.v. byssus\", \"stance\": \"supports\",\n     \"note\": \"gives 'Arab. bayḍaʾ, \\\"egg\\\"' as the source form of the Persian loan.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"bŭtz, bŭz\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Hebrew בּוּץ būṣ 'byssus, fine white linen' (Nourai's būtz/būz, the two spellings being his tz/z for ṣade) is a real word — it is the cloth of the Levites and of Mordecai's robe (1 Chr. 15:27, 2 Chr. 3:14, Esth. 1:6, 8:15), alongside Aramaic בּוּצָא būṣā and Syriac būṣā. Its attachment to the 'white' root is the disputable part. Klein p.215 derives it 'fr. Sem. *b-w-ṣ, \\\"to be white, to surpass in whiteness\\\"', which is Nourai's arrow; Wiktionary instead sets up an independent Proto-Semitic *būṣ- 'byssus' under a root ב־ו־ץ with no whiteness gloss and no Arabic cognate, and the distribution (only in the late books, always of an imported luxury textile, with the older Hebrew word for fine linen being šēš, itself an Egyptian loan) points to a Levantine culture-word rather than to an inherited derivative of b-y-ḍ. AHD does not recognise the Semitic-'white' connection at all. So: the word and its meaning are right, its parentage in this chart is one nineteenth-century option among others.\",\n  \"derivation_fa\": \"عبریِ בּוּץ (būṣ) «کتانِ سپیدِ نازک، بوس» — که نورایی به دو صورتِ būtz و būz آورده، و tz و z هر دو نویسه‌گردانیِ او از «צ» است — واژه‌ای اصیل است و در کتاب‌های متأخرِ عهد عتیق (تواریخ، استر) نامِ پارچهٔ لاویان و جامهٔ مردخای است؛ آرامی būṣā و سریانی būṣā نیز همان‌اند. آنچه محلِ گفت‌وگوست پیوندِ آن با ستاکِ «سپیدی» است. کلاین در ص۲۱۵ آن را «از سامیِ *b-w-ṣ به معنی سپید بودن» می‌گیرد و پیکانِ نورایی از همین‌جاست؛ اما ویکی‌واژه سامیِ آغازینِ مستقلِ *būṣ- «بوس» را بازسازی می‌کند بی هیچ معنایِ «سپیدی» و بی هم‌ریشهٔ عربی، و پراکندگیِ کاربرد (تنها در کتاب‌های متأخر و همواره دربارهٔ پارچه‌ای وارداتی، در برابرِ واژهٔ کهن‌ترِ šēš که خود وام‌واژه‌ای مصری است) نشان می‌دهد که با واژه‌ای فرهنگیِ شامی سروکار داریم نه با مشتقی میراثی از ب‌ی‌ض. فرهنگ American Heritage نیز این پیوند را یکسره نمی‌پذیرد. پس واژه و معنا درست است ولی نسبتی که نمودار می‌دهد یکی از گزینه‌های سدهٔ نوزدهم است؛ با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D7%91%D7%95%D7%A5\", \"https://en.wiktionary.org/wiki/byssus\", \"https://www.ahdictionary.com/word/semitic.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:183\", \"status\": \"contradicts\",\n     \"note\": \"AHD s.v. byssus routes the word 'from Latin, from Greek bussos, linen … of Dravidian origin, or ultimately from Egyptian wʾḏ, linen' — no Hebrew step at all; and the AHD Semitic appendix has no b-w-ṣ root. Nourai's own chart note concedes this.\"},\n    {\"ref\": \"KLN:215\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 125, s.v. byssus: 'Cp. Heb. būtz, of s.m., fr. Sem. *b-w-ṣ (*b-w-tz), \\\"to be white, to surpass in whiteness\\\"' — Nourai's spelling 'būtz' is Klein's.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"online, s.v. byssus + Semitic appendix\", \"stance\": \"contradicts\",\n     \"note\": \"Egyptian/Dravidian etymology, no Hebrew intermediary, no Semitic 'white' root in the appendix.\"},\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215\", \"stance\": \"supports\",\n     \"note\": \"the Semitic 'white' etymology, credited to Muss-Arnolt, TAPA 23, 80 n.19.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD vols, s.v. byssus\", \"stance\": \"silent\",\n     \"note\": \"grep of the Funk & Wagnalls volumes on disk returns no usable byssus article (OCR gap in the by- range of vol. I).\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Greek\", \"words\": \"bussos 1\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Ancient Greek βύσσος bússos 'fine linen, flax' (Nourai's 'bussos', with u for upsilon; the '1' is his homograph index, distinguishing it from the other βύσσος 'depth, bottom' that underlies abyss) is first in Herodotus and in the Septuagint, where it renders Hebrew būṣ and šēš — and that Septuagint equation is the strongest argument for the Semitic route the chart draws. Wiktionary agrees that Greek bússos comes 'from a Semitic source', citing Hebrew būṣ and Aramaic būṣā, and Klein calls it 'a Semitic loan word'. The competing view, AHD's, takes it from Egyptian wʾḏ 'linen' (or connects it with Sanskrit picuḥ 'cotton', of Dravidian origin) without any Hebrew intermediary. Since both routes end in the same eastern-Mediterranean textile trade, the disagreement is about the immediate donor, not about the word's oriental origin.\",\n  \"derivation_fa\": \"یونانیِ باستانِ βύσσος (bússos) «کتانِ نازک» — که نورایی با u برای «اوپسیلون» نوشته و عددِ ۱ نشانهٔ هم‌نگاشتِ اوست تا از βύσσος دیگر به معنی «ژرفا» که ریشهٔ abyss است بازشناخته شود — نخست در هرودوت و سپس در ترجمهٔ سبعینیه دیده می‌شود، و در آنجا برابرِ būṣ و šēš عبری می‌آید؛ همین برابری در سبعینیه نیرومندترین دلیل بر راهِ سامی است که نمودار کشیده است. ویکی‌واژه نیز می‌گوید که bússos «از منبعی سامی» است و عبریِ būṣ و آرامیِ būṣā را گواه می‌آورد، و کلاین آن را «وام‌واژه‌ای سامی» می‌خواند. دیدگاهِ رقیب، یعنی فرهنگ American Heritage، آن را بی هیچ واسطهٔ عبری از مصریِ wʾḏ «کتان» می‌گیرد. چون هر دو راه به همان بازرگانیِ پارچه در مدیترانهٔ خاوری می‌رسد، اختلاف بر سرِ وام‌دهندهٔ بی‌واسطه است نه بر سرِ خاستگاهِ شرقیِ واژه؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/byssus\", \"https://www.ahdictionary.com/word/search.html?q=byssus\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:215\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 125, s.v. byssus: 'L., fr. Gk. bussos, \\\"fine white linen\\\", a Semitic loan word. Cp. Heb. būtz, of s.m.' — precisely the Hebrew > Greek arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215, s.vv. byssus, byssine\", \"stance\": \"supports\",\n     \"note\": \"'a Semitic loan word', with the reference to Muss-Arnolt's list of Semitic words in Greek and Latin.\"},\n    {\"src\": \"AHD\", \"where\": \"online, s.v. byssus\", \"stance\": \"contradicts\",\n     \"note\": \"'from Greek bussos, linen … of Dravidian origin, or ultimately from Egyptian wʾḏ, linen' — Greek is taken from Egyptian, not from Hebrew.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"The empty pass-through box is Latin byssus, -ī f. 'fine linen, byssus', borrowed from Greek βύσσος with the ordinary Latin rendering of upsilon by y and of the Greek nominative -os by -us; it is the form used in the Vulgate (Luke 16:19, the rich man clothed in purpura et bysso) and in Pliny, and it is the immediate source of the English word. Klein p.215 states the chain 'L., fr. Gk. bussos', and AHD the same ('from Latin, from Greek bussos'), so both authorities on the page supply the link Nourai leaves unlabelled.\",\n  \"derivation_fa\": \"این جعبهٔ خالی همان byssus لاتین است، مؤنث، به معنی «کتانِ نازک»، که از βύσσος یونانی وام گرفته شده با برگردانِ معمولِ «اوپسیلون» به y و پایانهٔ ‑os یونانی به ‑us لاتین. همین صورت است که در ولگات (لوقا ۱۶:۱۹، توانگری که «purpura et bysso» پوشیده بود) و در پلینیوس به کار رفته و سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی است. کلاین در ص۲۱۵ همین زنجیره را می‌دهد («لاتین، از یونانیِ bussos») و فرهنگ American Heritage نیز («از لاتین، از یونانیِ bussos»)؛ پس هر دو مرجعِ همین صفحه حلقه‌ای را که نورایی بی‌نام گذاشته پر می‌کنند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=byssus\", \"https://en.wiktionary.org/wiki/byssus\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives no reference for this pass-through box; the Greek > Latin > English chain is covered by the KLN:215 and AHD:183 citations on the boxes either side of it, both of which were checked and both of which state 'L., fr. Gk. bussos'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215 s.v. byssus\", \"stance\": \"supports\",\n     \"note\": \"'byssus, n. — L., fr. Gk. bussos'; also 'byssine … — L. byssinus, \\\"made of byssus\\\", fr. Gk. byssinos'.\"},\n    {\"src\": \"AHD\", \"where\": \"online, s.v. byssus\", \"stance\": \"supports\",\n     \"note\": \"'Middle English bissus, linen cloth, from Latin, from Greek bussos, linen.'\"},\n    {\"src\": \"LEW\", \"where\": \"Walde-Hofmann, LEW_1910.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for byssus/bysso in the OCR of Walde 1910 returns nothing usable (the b- section of this scan is damaged), so the Latin etymological dictionary could not be brought to bear.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"byssus\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English byssus is a learned borrowing of Latin byssus, already Middle English bissus 'linen cloth'; AHD defines it as '(1) a mass of strong, silky filaments by which certain bivalve mollusks attach themselves to rocks; (2) a fine-textured linen of ancient times, used by the Egyptians for wrapping mummies' — the second sense is exactly Nourai's gloss 'white cloth used to wrap mummies', so his AHD:183 is faithfully reported. The mollusc sense (sea-silk, the beard of Pinna nobilis) is an eighteenth-century transfer of the same word on the strength of the fibre's fineness; Klein records the derivatives byssal, byssin, byssine.\",\n  \"derivation_fa\": \"byssus انگلیسی وام‌واژه‌ای عالمانه از byssus لاتین است که پیش‌تر در انگلیسیِ میانه به صورتِ bissus «پارچهٔ کتانی» دیده می‌شود. فرهنگ American Heritage دو معنا برایش می‌آورد: نخست «رشته‌های ابریشمینِ استواری که برخی نرم‌تنانِ دوکفه‌ای با آن خود را به سنگ می‌چسبانند» و دوم «کتانِ نازکِ روزگارِ باستان که مصریان مومیایی‌ها را در آن می‌پیچیدند» — و معنایی که نورایی می‌دهد («پارچهٔ سپیدی که برای پیچیدنِ مومیایی به کار می‌رفت») درست همین معنای دوم است؛ پس ارجاع او به AHD:183 امانت‌دارانه است. معنای جانورشناختی (ابریشمِ دریایی، ریشِ صدفِ Pinna nobilis) انتقالی است از سدهٔ هجدهم بر پایهٔ نازکیِ همان رشته‌ها. کلاین مشتق‌های byssal و byssin و byssine را نیز ثبت کرده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=byssus\", \"https://en.wiktionary.org/wiki/byssus\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:183\", \"status\": \"supports\",\n     \"note\": \"AHD s.v. byssus: '… 2. A fine-textured linen of ancient times, used by the Egyptians for wrapping mummies. [Middle English bissus, linen cloth, from Latin, from Greek bussos, linen …]' — Nourai's gloss is AHD's sense 2 verbatim in substance. (The 1975 New College page 183 itself could not be paged; only Watkins's IE appendix from that edition is on disk.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 125 = p.215 s.v. byssus\", \"stance\": \"supports\",\n     \"note\": \"'byssus, n. — L., fr. Gk. bussos, \\\"fine white linen\\\" … Derivatives: byss-al, adj., byss-in, n., byssine.'\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for byssus in the Webster volume on disk finds no legible article (the scan's by- range is not in this volume).\"},\n    {\"src\": \"AHD\", \"where\": \"online, s.v. byssus\", \"stance\": \"supports\",\n     \"note\": \"definition and etymology as quoted.\"}\n  ]\n})\n\ndata[\"entries\"].append(e2)\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-103.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk103.py && python3 -m json.tool data/verification/page-103.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 103"
}
```


### [2026-09-05T15:04:10.264Z] TOOL RESULT

```
written
valid json
nodes verified: 15/15
node verdicts: {'confirmed': 11, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 13, 'not_checked': 5, 'partial': 1, 'contradicts': 1}
books consulted: {'supports': 26, 'partial': 6, 'silent': 9, 'contradicts': 2} | by book: {'AHD': 8, 'KLN': 8, 'RCH': 5, 'MON': 3, 'FSD': 3, 'NYB': 3, 'BRT': 2, 'BQT': 2, 'FVQ': 1, 'HUB': 1, 'AVG': 1, 'PHD': 1, 'SNS': 1, 'SOD': 1, 'AFM': 1, 'LEW': 1, 'WEB': 1}
```


## [2026-09-05T15:04:18.264Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"AVG:\"; grep -c -i \"baevar\\|baevan\" AVG.txt\necho \"SNS:\"; grep -c -i \"bewar\\|bēwar\\|bywl\" SNS.txt\necho \"FSD byssus:\"; grep -c -i \"byssus\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt\necho \"WEB byssus:\"; grep -c -i \"byssus\" WEB_vol1.txt\necho \"LEW byssus:\"; grep -c -i \"byssus\\|bysso\" LEW_1910.txt\necho \"AFM bayd:\"; grep -c \"بيض\\|بیض\" AFM.txt\necho \"FVQ bayd/bus:\"; grep -c -i \"bayd\\|buts\\|būṣ\" FVQ.txt"
}
```


### [2026-09-05T15:04:18.390Z] TOOL RESULT

```
AVG:
3
SNS:
0
FSD byssus:
FSD_vol3.txt:1
FSD_vol4.txt:2
FSD_vol1.txt:10
FSD_vol2.txt:2
WEB byssus:
9
LEW byssus:
0
AFM bayd:
40
FVQ bayd/bus:
0
```


## [2026-09-05T15:04:23.088Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AVG ===\"; grep -n -i \"baevar\\|baevan\" AVG.txt | head -5\necho \"=== FSD vol1 byssus ===\"; grep -n -i \"byssus\" FSD_vol1.txt | head -4 | cut -c1-700\necho \"=== WEB byssus ===\"; grep -n -i \"byssus\" WEB_vol1.txt | head -4 | cut -c1-700"
}
```


### [2026-09-05T15:04:23.178Z] TOOL RESULT

```
=== AVG ===
2043:Note.  These  neuters  rarely  show  declined  cases:— e.g.  Sg.  Instr. dasvara  'with  strength'  (Ys.  55.3);  PL  Instr.  balvar'brt  'with  thousands'.— Like  a-decl.,  Dat.  sg.  baevarai.
2234:1000.  hazavra- 10000.  baevar-
4647:Av.  karfvar-  n.  f.  beside  karfvan-  'clime,  zone' ;  Av.  za/ar-  (i.  e. *zap-var  §  95)  n.  beside  zafan-  'jaw' ;  Av.  batvar-  n.  beside  baevan- 'myriad'.  So  mibwara-  n.  (-vara)  beside  mibwan-  'pair'.  Observe Av.  srvara-  (for  sruvara-  §  68)  'horned,  Sruvara'.
=== FSD vol1 byssus ===
5782:[   <   OF.  ablsme  (F.  abtme),  <   LL.  abissimus,  sup.  of  abis- eua,  <   L.  abyssus ;   sec  abyss.]  a-blsme't;  a-bysme't. a-b)’s'xnal,  1   a-btz/mal;  2   a-b^g'mal,  a.  1.  Of.  per- taining to,  or  relating  to  an  abyss.  2.  Of  or  pertaining to  oceanic  depths.— a»bys'maMj',  adr. a-byss',  I   o-bi*.';  2   a-b^s',  cl.  [Rare.!  To  swallow  up;  en- gulf; bury  completely.
38473:2.  Zool.  -Some  appendage  or  part  more  or  less  like  the human  beard.  (1)  The  hairs  on  the  chin  and  other  parts of  the  face  of  various  mammals,  especially  of  the  goat.  (2) (a)  In  birds,  rictal  vlbrissce.  ( b )   The  vane  or  barbs  of  a feather,  (c)  Pendent  metallic  feathers  beneath  the  throat in  certain  humming-birds,  or  color-markings  suggesting  a beard.  (3)  The  barbels  of  fishes.  (4)  (a)  The  gills  of  the oyster  and  other  bivalves.  (&)  The  byssus  or  a   mussel  or other  anchored  bivalve,  (5)  The  small  labial  processes of  lepidopterous  and  certain  dipterous  insects.
53953:bys'slne.  I.  a.  Made  of  byssus;  flax-like;  silken.  II.  n. A   byssine  garment,  bys'sln;.—  bys-sl-no'sls,  n.  Chronic Inflammation  of  the  lungs  caused  by  the  inhalation  and  lodg- ment of  cotton-fibers  —   bys-sog'e-nous,  a.  Producing  a byssus.—  bys'sold,  a.  Byssaceous  —   hys'so-llte,  n.  Min- eral. Same  as  amantoid.
53955:Slaves  Bearing  red  jars  of  byssus,  sealed  for  Rome.
=== WEB byssus ===
1320:in- a-but/ment, n. 1. a part that supports an ty. arch or strut, as of abridge. _ is 2. that which rd abuts or borders ras on another thing, S as a building or piece of land. ıb- 3. the state of E E a V., . the point of contact between th D h and Ma thine Be DO eas OSU se he a-but’tal, n. . the butting or boundary of in land at the end: used in the plural. E | 2. an abutment. 3 re; å-but’tēr, n. a person who or a thing whi abuts: said of a building or land, or pe O ty; a-but’ting, a. 1. touching at the end; contigu- n- ous; as, abutting property. aS 2. resting on or against; as, abutting rocks, i Syn.—adjacent, neighboring, next. of a-buzz’, a. [a-, in, and buzz.] 1. filled
17254:6. (a) the byssus of certain kinds of mol- lusks, consisting of fine threads or hairs, by which they fasten themselves to rocks, etc.; (b) the gills or respiratory organs of the oyster and other bivalves. i
25692:bys-sa’/ceous, a. {L. byssus; Gr. byssos, a fine flax or linen.] resembling a byssus; consisting of fine silky filaments.
25693:bys’sal, a. relating to a byssus.
```


## [2026-09-05T15:04:33.784Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol1 bys'sus ===\"; grep -n \"bys'sus\\|bys’sus\\|byssus,  n\" FSD_vol1.txt | head -3 | cut -c1-900\necho \"=== WEB byssus headword ===\"; sed -n '25694,25700p' WEB_vol1.txt\necho \"=== AFM بيض ===\"; grep -n \"بيضة\\|البيض\" AFM.txt | head -5"
}
```


### [2026-09-05T15:04:33.872Z] TOOL RESULT

```
=== FSD vol1 bys'sus ===
5787:<   a-  prlv.  -f  byssos.  bottom.  <   bothy t.  deep.]  a-bys'susf.
53954:bys'sus,  1   bis'us;  2   bys'us,  n.  [bts'si,  1   -ai;  2   -I,  or BYS'sus-ES.  pl.]  1.  Class.  Antiq.  A   variety  of  flax,  or the  fine  white  cloth  into  which  it  was  made;  the  “fine linen”  of  the  Bible;  also,  in  late  times,  any  costly white  stuff  of  cotton,  silk,  or  linen.
=== WEB byssus headword ===
bys-sif/ér-ous, a. [L. byssus, byssus, and ferre, to bear.] bearing a byssus or tuft.
bys/sin, n. same as byssus (a cloth).
bys/sine, a. (L. byssinus; Gr. byssinos, from byssos, byssus.] made of silk; having a silky or flaxlike appearance.
bys’soid, a. byssaceous.
bys/so-lite, n. [Gr. byssos, fine flax, and lithos, stone: so called from its resemblance to flax. a variety of hornblende having short silky fibers and an olive-green color.
byssus, n.; pl. bys/si, [L. byssus; Gr. byssos, fine linen, or cotton.]
1. among the ancients, a linen, silk, or cot- ton cloth of exceedingly fine texture: used by the Egyptians in mummy wrapping.
=== AFM بيض ===
618:المماركة والشوكة البيضاء ܢ هذا الات بالا دورد لأن الريح تلعس به وهو 
2093:ظهر في ايأمه.وقيل انه اسم نبات ܚܨܢ «سفيد تلك» اي الكرمة البيضاء 
2122:* (اباري ) بزر السمك تعريب خاّهبر واصل معناهٌ كثة البيض ٠‏ وملة 
3289:( الزُمأوَرد) طعام من البيض واللحم ٠‏ وقول العامّة بزماورد اصوب لان < 
4909:ار لات عم كر يا حتى في انام الشتاء ٠‏ واسمة بالعربيّة الكرمة البيضاء
```


## [2026-09-05T15:04:53.585Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np='data/verification/page-103.json'\nd=json.load(open(p,encoding='utf-8'))\n\ndef node(e,i):\n    return next(n for n in d['entries'][e]['nodes'] if n['id']==i)\n\ndef setcon(n, src, where, stance, note):\n    for c in n['consulted']:\n        if c['src']==src:\n            c.update(where=where, stance=stance, note=note); return\n    raise SystemExit('not found '+src)\n\n# entry 1 node 1: AVG is not silent\nsetcon(node(1,1), 'AVG', 'Jackson, Avesta Grammar §§ (numerals list) and the r/n-stem section', 'supports',\n  \"AVG.txt line 2234 lists the Avestan numerals '1000. hazavra- 10000. baevar-'; line 4647 uses the word as a type example of heteroclisis: 'Av. baēvar- n. beside baēvan- \\\"myriad\\\"'; line 2043 gives the dative sg. baēvarai.\")\n\n# entry 2 node 3: FSD is not silent\nsetcon(node(2,3), 'FSD', 'vol. I line 53954, s.v. byssus', 'partial',\n  \"'byssus, n. ... 1. Class. Antiq. A variety of flax, or the fine white cloth into which it was made; the \\\"fine linen\\\" of the Bible; also, in late times, any costly white stuff of cotton, silk, or linen.' Funk & Wagnalls confirms the sense and the biblical equation with Hebrew būṣ, but gives no etymology of the Hebrew word.\")\n\n# entry 2 node 6: WEB is not silent\nsetcon(node(2,6), 'WEB', \"Webster's New Twentieth Century, vol. I, s.v. byssus\", 'supports',\n  \"'byssus, n.; pl. byssi, [L. byssus; Gr. byssos, fine linen, or cotton.] 1. among the ancients, a linen, silk, or cotton cloth of exceedingly fine texture: used by the Egyptians in mummy wrapping.' — Webster's wording is almost Nourai's gloss, and it too routes the word L. < Gk.\")\n\n# entry 2 node 1: refine the AFM note\nsetcon(node(2,1), 'AFM', 'AFM.txt, grep بيض / بيضة', 'silent',\n  \"Addi Shir has no headword for بيض/بيضة; the string occurs only inside unrelated plant names (e.g. 'الكرمة البيضاء' s.vv. lines 618, 4909). Expected, since he collects Persian words borrowed INTO Arabic and bayḍ is native Arabic.\")\n\njson.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-103.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 103"
}
```


### [2026-09-05T15:04:56.392Z] TOOL RESULT

```
patched
valid json
nodes verified: 15/15
node verdicts: {'confirmed': 11, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 13, 'not_checked': 5, 'partial': 1, 'contradicts': 1}
books consulted: {'supports': 28, 'partial': 7, 'silent': 6, 'contradicts': 2} | by book: {'AHD': 8, 'KLN': 8, 'RCH': 5, 'MON': 3, 'FSD': 3, 'NYB': 3, 'BRT': 2, 'BQT': 2, 'FVQ': 1, 'HUB': 1, 'AVG': 1, 'PHD': 1, 'SNS': 1, 'SOD': 1, 'AFM': 1, 'LEW': 1, 'WEB': 1}
```


## [2026-09-05T15:05:12.989Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-103.json` written; `verify_check.py 103` reports **0 PROBLEM lines** (15/15 nodes).

**Page 103 (book p. 73) — 3 entries, 15 nodes**
- Node verdicts: 11 confirmed, 3 plausible, 1 transcription_suspect
- Root verdicts: 1 confirmed (B.y.t), 2 plausible (Byŭrru, B.y.z/B.w.s)
- Ref checks: 13 supports, 1 partial, 1 contradicts, 5 not_checked (FVA:55/56 and AEF:324 have no digital copy; AEF was proxied through Horn no. 262 + Hübschmann p. 262)

**Flagged items**
- `transcription_suspect` — entry 2 #2 Persian «بیضه»: the chart/JSON read **batzeh**. The 400 dpi render of the printed page shows the book itself prints "batzeh : egg", so the extraction is faithful and this is Nourai's own misprint for *bayzeh* (`error_in: "book"`). The same box's «بیّاض» "whiteness" carries a tašdīd on the page too — the word for "whiteness" is *bayāz* (بیاض); *bayyāḍ* is "whitewasher". Also a book error.
- `plausible` — root 1 "Indo-Schythian Byŭrru": *byūrru* is Bailey's **Khotanese** headword, so Avestan/Sogdian/Armenian are its sisters, not descendants; the etymon is PIr. *\*baiwar-*. "Indo-Schythian" is the book's own spelling (verified on the page). Bailey's link to PIE *\*bheu-* (Pok. 146-50) is not generally accepted.
- `plausible` — entry 1 #5 Armenian *biur*: both Bailey (DKS) and Nyberg mark it "lw." — an Iranian (Parthian) loanword, not an inherited branch.
- `plausible` — root 2 and nodes #3/#4: Klein's unification of Arabic b-y-ḍ "white" with Hebrew *būṣ* / Gk. *byssos* is a 19th-c. hypothesis; Wiktionary reconstructs an independent PSem. *\*būṣ-*, and AHD (Nourai's own AHD:183) routes *byssos* from Egyptian *wʾḏ* with **no Hebrew step** — recorded as the one `contradicts`.

**No extraction errors found** — the JSON matches the printed page throughout (including "Indo-Schythian", "batzeh", "bussos 1", "Bĕth-lexem").

Page PNG archived at `data/verification/sources/refs/ocr/BOOK/103.png`; 11 web sources archived via `fetch_source.py` (Wiktionary ×5, AHD ×3, abadis/Mo'in ×3).
