# Verification process log — verify-page-77


## [2026-09-05T05:54:03.452Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 77 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-77.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-77.json. Write /home/sfmqrb/git/rishe/data/verification/page-77.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 77` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:54:05.652Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:54:06.370Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:54:06.389Z] TOOL RESULT

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


## [2026-09-05T05:54:06.664Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-77.txt"
}
```


### [2026-09-05T05:54:06.684Z] TOOL RESULT

```
1	=== PDF page 77 (book page 47) ===
2	--- entry 0 ---
3	ROOT [Old Persian] Batiaxě : a bowl (of wine)  (refs HRN:36)
4	#1 (parent #0) [Pahlavi] refs=AEF:207 | bâtak : wine
5	  #2 (parent #1) [Persian] refs=AEF:207 | bâdeh «باده» : wine ; bâdîyeh «باديه ( باطيه )» : bowl (of wine) ; pâtîleh «پاتيله ( پاتيل )» : pot | NOTE: VFO:18 claims these words are related to English "pot". Also see "Pô 2".
6	--- entry 1 ---
7	ROOT [Avestan] Bazda : bad, sin  (refs SOD:18)
8	#1 (parent #0) [Sogdian] refs=SLW:101; SOD:18 | `bz, `bj, `bž, `byz : sin, bad
9	  #2 (parent #1) [Persian] refs=BQT:1485 | faž «فژ ( پژ ۲ )» : dirt, dirty ; fažâk «فژاک ( فژاکن ، فژاگین )» : dirty, impure ; fažâğand «فژاغند ( فژغند ، فژگند )» : dirty
10	--- entry 2 ---
11	ROOT Bělŭr -> redirect to Velŭr
12	--- entry 3 ---
13	ROOT [Avestan] Berenža : brass  (refs HRN:48)
14	#1 (parent #0) [Persian] refs=HRN:48 | berenj 1 «برنج ١» : brass
15	  #2 (parent #1) [Latin] refs=PRT:60; KLN:203 | bronzium : brass
16	    #3 (parent #2) [Italian] refs=None | bronzo
17	      #4 (parent #3) [French] refs=None | 
18	        #5 (parent #4) [Persian] refs=MON | bronz «برنز» : bronze
19	      #6 (parent #3) [English] refs=AHD | bronze
20	--- entry 4 ---
21	ROOT Besmâ -> redirect to Busmâ
22	
```


## [2026-09-05T05:54:09.973Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-77.json",
 "description": "Read page 77 source JSON"
}
```


### [2026-09-05T05:54:10.012Z] TOOL RESULT

```
{
  "pdf_page": 77,
  "book_page": 47,
  "entries": [
    {
      "root": {
        "name": "Batiaxě",
        "lang": "Old Persian",
        "refs": "HRN:36",
        "gloss": "a bowl (of wine)",
        "note": "The source of the Old Persian form is not clear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "AEF:207",
          "words": [
            {"translit": "bâtak", "gloss": "wine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AEF:207",
          "words": [
            {"translit": "bâdeh", "gloss": "wine", "script": "باده"},
            {"translit": "bâdîyeh", "gloss": "bowl (of wine)", "script": "باديه ( باطيه )"},
            {"translit": "pâtîleh", "gloss": "pot", "script": "پاتيله ( پاتيل )"}
          ],
          "script_extra": null,
          "note": "VFO:18 claims these words are related to English \"pot\". Also see \"Pô 2\".",
          "quote": {
            "text": "برخیز هان ای جاریه، می درفکن در باطیه - آراسته کن مجلسی، از بلخ تا ارمینیه",
            "poet": "Manŭchehrî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Bazda",
        "lang": "Avestan",
        "refs": "SOD:18",
        "gloss": "bad, sin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SLW:101; SOD:18",
          "words": [
            {"translit": "`bz, `bj, `bž, `byz", "gloss": "sin, bad", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1485",
          "words": [
            {"translit": "faž", "gloss": "dirt, dirty", "script": "فژ ( پژ ۲ )"},
            {"translit": "fažâk", "gloss": "dirty, impure", "script": "فژاک ( فژاکن ، فژاگین )"},
            {"translit": "fažâğand", "gloss": "dirty", "script": "فژاغند ( فژغند ، فژگند )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همانا که چون تو فژاک آمدم - وگر چون تو ابله فغاک آمدم",
            "poet": "Asadî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Bělŭr",
        "redirect": "Velŭr"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Berenža",
        "lang": "Avestan",
        "refs": "HRN:48",
        "gloss": "brass"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "HRN:48",
          "words": [
            {"translit": "berenj 1", "gloss": "brass", "script": "برنج ١"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Latin",
          "refs": "PRT:60; KLN:203",
          "words": [
            {"translit": "bronzium", "gloss": "brass", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "bronzo", "gloss": null, "script": null}
          ],
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
          "refs": "MON",
          "words": [
            {"translit": "bronz", "gloss": "bronze", "script": "برنز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "bronze", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Besmâ",
        "redirect": "Busmâ"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:54:12.224Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','AEF','SOD','SLW','BQT','PRT','KLN','MON','AHD','VFO','POK','WLD','HUB','PHD','NYB','BRT','ARY','CHEUNG','SKT','WEB','FSD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T05:54:13.983Z] TOOL RESULT

```
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_2021
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
VFO null
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-05T05:54:17.522Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local refs and matrix"
}
```


### [2026-09-05T05:54:17.568Z] TOOL RESULT

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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
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
```


## [2026-09-05T05:54:23.711Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"batiak\\|βατιάκη\\|batiax\\|Baxiax\" HRN.txt HUB.txt KLN_1966.txt BQT_v1_pages.txt 2>/dev/null | head -40",
 "description": "Grep batiake in refs"
}
```


### [2026-09-05T05:54:23.789Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:54:25.021Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"bâdeh\\|bade\\b\\|bādha\\|batak\" HRN.txt | head -40",
 "description": "Grep bade in Horn"
}
```


### [2026-09-05T05:54:25.075Z] TOOL RESULT

```
138:wie bade/räh (No. 154), pädOs (No. 265»»*«), petyare (No. 284),
1752:155. hädye *Weingefäss', vergl. bade 'Wein .
1754:Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.).
2734:sich im Bade die Fersen reibt', de Lagarde, Ges.
11694:bade 155.
```


## [2026-09-05T05:54:28.269Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1735,1775p' HRN.txt",
 "description": "Print Horn context"
}
```


### [2026-09-05T05:54:28.316Z] TOOL RESULT

```
153. hädreng 'Citrone*.
mäz. vdreng.
phlv. vatrang (PPGl., Bund.), vatreng (Bund.), vatreg
(verschrieben (?), vd. 2 (77) GL).
*) Die verschiedene Art der Orientirung erklärt Bartholomae,
ZDMG. 42, 154. Zu apcf^s (Nom. sing.) vergl. KZ. 29, 501.
*) Ein aw. üö^«- *Kraft' (Justi) giebt es nicht, vergl. Geldner ,
KZ. 30, 524, Bartholomae, Indog. Forsch. I, 191 Anm.
3*— 86 —
arm. patrinc (de Lagarde, No. 1848: patriny)
gehört kaum hierher.
154. bädefräh 'Vergeltung, Strafe'.
aw. mat]paitifrasa' ; phlv. pätfräs, päz. pädafrah.
FirdüsT verwendet aus metrischen Gründen die
Formen badafräh (Sahn. III 1712 Vers 3784, 1806,
Vers 430) oder bädefre (Sahn. I, 105 Vers 798).
Übrigens muss päd- emendirt werden').
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


## [2026-09-05T05:54:42.211Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD bādag ==\"; grep -n -i \"bādag\\|badag\\|bʾtk\\|bātag\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB ==\"; grep -n -i \"bātak\\|bādag\\|bʾtk\" NYB_vol2_glossary.txt | head -20; echo \"== HUB ==\"; grep -n -i \"bāde\\|bade '\" HUB.txt | head -20",
 "description": "Grep Pahlavi badag"
}
```


### [2026-09-05T05:54:42.287Z] TOOL RESULT

```
== PHD bādag ==
PHD.txt:2875:must (n.) bādag.
PHD.txt:4315:window rózan, roz(b)anag. wine badag, may. wine-press karxēš.
PHD_mackenzie.txt:7994:wine badag, may.                        f.l)orthy arzan(ig), arzomand, sahig,
PHD_mackenzie.txt:11201:bcsaz                     ~\                  badag                        \,~\
== NYB ==
== HUB ==
```


## [2026-09-05T05:54:44.449Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT باده ==\"; grep -n \"باده\" BQT_v1_pages.txt | head -20; echo \"== BQT باطیه ==\"; grep -n \"باطیه\\|باديه\\|بادیه\" BQT_v1_pages.txt | head -20; echo \"== BQT پاتیل ==\"; grep -n \"پاتیل\" BQT_v1_pages.txt BQT_v2_pages.txt | head",
 "description": "Grep Borhan for bade"
}
```


### [2026-09-05T05:54:44.543Z] TOOL RESULT

```
== BQT باده ==
1117:نباده ص‌دوق در حفه ای محشه درون یارسی رفعه‌ای
2965:دو لب او ز باده عنابی دو رخ او ز غلزه کلناری
4160:بادام » باده » باران » باریدن *"بازار » بازو » باغبان » بسامداد »بخشش »
5211:تركگ داده‌اند» چه نزد ابشان هرچه از مفرد زباده است در شمار جمم باشد
5938:آب باده ر نگ - بکرتات ,کناب
8846:با زباده بهم را نیز گوبند؟۹.
12410:باشد که در مقابل باده است - و بزبان کیلان
12658:اورا باری بیرآن‌وسه فرستاد ورستم بباده سدان
14938:ععنی زباده شدن .
15082:ائت و محلل بادها و نفشها ؛ و بفتح اول و کسر
16378:بدیرا کویند ۴ - و بمعنی خشت بادهم هت
16411:روز میباشد برعکس بادسب. وضرر این باد زباده
16477:ه باده _ بفتح» وم : شراب » در بهلوی 9۵12 « اونوال۳۹۲ ب؟ , معرب آن , باذق «قس؟.بلدهرزه
16480:بادهر ده - بازای‌هوز بروزن‌اء‌پردد؛
17031:چیزیرا زباده از اجه هست وانماید .
18202:گرفتن باشد که زباده برقدرت اوست .
19772:۴ هز. 0254 «بوستی. بادهش.۸۸».
19857:اگر زنان آنرا یپزند و بخورند شیر ایشان‌زباده
20480:بالاذه » نتم اول بوز نکباده » بدکار
22221:یجاذه - با ثالی‌مجهول بروزن بی‌باده»
== BQT باطیه ==
16490:بادیه‌غول «کنابهاز دیسای‌فانی‌باشد.
== BQT پاتیل ==
BQT_v1_pages.txt:8301:داله دائه شود آنگاه در پاتیلی کنند و عسل در
```


## [2026-09-05T05:54:50.659Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=16460 && NR<=16495' BQT_v1_pages.txt; echo \"=== page tag ===\"; awk 'NR<=16477 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' BQT_v1_pages.txt",
 "description": "Borhan bade entry context"
}
```


## [2026-09-05T05:54:51.738Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^badag\\|badag \\[\" PHD.txt PHD_mackenzie.txt | head; echo ---; grep -n -w \"badag\" PHD.txt | head",
 "description": "MacKenzie badag entry"
}
```


### [2026-09-05T05:54:52.293Z] TOOL RESULT

```
بگذاوند فی‌الحال بچسبد - وعوام مه سقیدی‌را
سودمند باشد .
بادودم - نم داد اول و فتح دا
دوم (۱) و سکون میم » غرور و تکبر و عجب
و تجبر و خودستابی و خودنمابی باشد . <
بات هر ات باد شمار راکوند .وآن
٩‏ - م رکب از: باد + کند ( جندص خایه) . ۴ رک : بادیجان و پانشگان.
۴ - در فرهنکگ دساتیر (س۷۲۳4) بهمن معنی آمده ۱
» بادفجای _ باندگان , بلدنگان » ور طبری ۷3۳۵84۳0 < واژه نامه ۸۱۸ » »کلکی
6010 , فربز دی 0لا(۷۵(۵610 ۰ برنی و طنزی 92060[0 < 4 . ۱ص ۲۸۲ »۰
تهرانی 9۵061۳08 . باني است یکاله دارای کلهای بنفش و برگهای «راز
و تخم کوچك زرد رنگ و یوم دراز اندام با بضی با گرد بنفش وسفید و غیره .
مسوءٌ آن خوراله انان است [ رد ِ فرحنگه روستابی ۲۳۱ وگل کلاب ۳۸
محرب آن بادتجان و از تازی وارد زبان اسپانیابی شد: 06۳608612 . در زبان
کانالانی (سمال شرفی اسپانیا) عورت: 2106۳88012 و از آ:جا واردفرانه شد؛
6 وسیس درامتالیابی واردگردید: ۳6۱۵061800 دضر» < نداب۳:
۳ ۱۹ فرامرزی ّ بادنجان
ه باده _ بفتح» وم : شراب » در بهلوی 9۵12 « اونوال۳۹۲ ب؟ , معرب آن , باذق «قس؟.بلدهرزه
از طرق مشرق است بجاب فرب . بر خلاف
باد دیود .
بادهر ده - بازای‌هوز بروزن‌اء‌پردد؛
اضونی را گونن که دزدان برساحب‌کالا بدمند:
خواب کران برو مستولی شود .
بادی - بروزن شاوی » یمنی‌همشهردايم
باشی - وآنچه منسوب‌بباد باشداز فلکیات‌همو:
برج جوزا و دلو و یزان ۷ .
بادیچ - بسکون جیم . چیزی باشد
مانند ساق چافشور (۱) که آلرا از پارچة رنگن
قلمی آجیده کنند و بیشتر شاطران و پیاده روان
بای کشند .
بادیه‌غول «کنابهاز دیسای‌فانی‌باشد.
فاد ه بر ون کار » چند مش دازد :
برداشت ؟ . » - نامی است از تامهای خدای
تعالی ۴ و بسعنی بزدگی ورفت و شأن‌وشوکت
باشد . ۳ رخصت و اجازت راکویند صوماٌ
و رخصت واجازت و راه دخول ملافات درآعدن
=== page tag ===
:
```


### [2026-09-05T05:54:52.351Z] TOOL RESULT

```
---
4315:window rózan, roz(b)anag. wine badag, may. wine-press karxēš.
```


## [2026-09-05T05:55:01.561Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bād\\|bâd\" PHD.txt | sed -n 1,40p; echo \"=== UNV ===\"; grep -n -i \"batak\\|bātak\\|wine\" UNV.txt | head -20",
 "description": "PHD bad entries and UNV batak"
}
```


### [2026-09-05T05:55:01.624Z] TOOL RESULT

```
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
233:bādaģ [?{А! | N a] wine, must.
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
784:anarchy abādixšāyīh.
1459:cultivated ābādān; — land warzbüm.
2875:must (n.) bādag.
3180:populous ābād.
3196:powerless abādixšā(y), abādyāwand, agār; become — agārīhistan; render — agārēnīdan.
3197:powerlessness abādixšāyīh.
3262:prosperity ābād(ān)īh, bahrómandih, drod, frāxīh, padéxih.
4000:thriving ābād(ān).
=== UNV ===
41:1.  Die  erste  Kunde  des  von  mir  behandelten  Texts  verdanken  wir E.W.West,  der  ihn  aus  der  Handschrift  J  1  (jetzt  MK)  kennen  lernte. Er  hat  GIrPli.  2.  118  eine  kurze  Inhaltsangabe  verötfentlicht :  ‘The  tale of  Khüsrö  i  Kavätän  and  his  Page  contains  about  1770  words. The  page  is  a  princely  youth  of  great  intelligence,  who  relates  to  the king  that  he  was  the  only  son  of  his  mother,  and  while  yet  a  child he  lost  his  father;  that  he  had  received  a  liberal  education  in  all  kinds of  knowledge,  religion,  literature,  horsemanship;  music,  games,  and wished  the  king  to  test  his  learning.  In  reply  to  the  king  he  details the  pleasantest  foods,  the  handsomest  birds,  the  nicest  meats,  the  fresh- est  jellies,  the  best  broths,  the  most  delicious  fruits,  the  wholesomest grains,  the  best  wines,  the  most  pleasing  tunes,  the  best  seven  ingre- dients  of  soup,  the  sweetest-scented  flowers,  the  best  of  women,  and  the best  steeds.  The  king  also  sends  him  to  capture  two  lions  who  had carried  off  a  mare ;  on  his  way  he  receives  an  evasive  reproof  from  a woman,  and,  returning  with  the  lions,  he  is  made  governor  of  the  district. This  tale  contains  many  Iranian  nouns  not  found  elsewhere  in  Pahlavi."
```


## [2026-09-05T05:55:02.631Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v1_pages.txt; grep -c \"pdf page\" BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | head -3",
 "description": "Check BQT page tags"
}
```


### [2026-09-05T05:55:02.700Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
0
```


## [2026-09-05T05:55:28.827Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT bazda ==\"; grep -n -i \"bazda\\|bažda\" BRT.txt | head -20; echo \"== BRT berenz/brnj ==\"; grep -n -i \"brnja\\|bərənj\\|berenj\" BRT.txt | head -20; echo \"== HRN berenj ==\"; grep -n -i \"berenj\\|birinj\\|Messing\" HRN.txt | head -20",
 "description": "Grep Bartholomae and Horn"
}
```


### [2026-09-05T05:55:28.911Z] TOOL RESULT

```
== BRT bazda ==
16697:KompE.  (fl*%  av).  —  PHP.  wm  V,  ian-,  — Vgl.  bazda-.  —  Pfi.:  vimär.
16708:HB.  254.  — 3)  VgL  ai.oidi/fl-' Rauschtrank' und  •  j.  »band- V. 'kranken'.  Praes  30  (Kaus.) •Rausch'.  -  :.)  S.  dazu  West  Av.-Gloss,  220.  \  bandaya-.  —  PPfP.  bazda-  (sbes.).
17049:•  j.  bazda-  Adj.  'erkrankt,  krank,  siech'; nüii  pasuSca  (statt  IS.)  •da  nsit  irilta  (sA) . .  abanta  airista  N.56.
25495:•  j.  iriäta-  Adj.  'beschädigt;  mit  einem Schaden  behaftet';  tail  "pasulca  (statt pasvd)  bazda  nuit  'ta  (rrSii)  anazdya  ratufris abanfa  airista  *azdya  paifistaahara  (sd.) ratufris  "nicht  wird  man  r.  mit  einem Stück  Kleinvieh,  das  krank  oder  mit einem  Schaden  behaftet  oder  mager  ist; r.  wird  man  mit  einem,  das  nicht  krank, ohne  Schaden,  wohlgenährt,  auserlesen  fett ist"  N.^ö'.
== BRT berenz/brnj ==
== HRN berenj ==
2209:Wort; vergl. arm. brinj; kurd. birinj; oss. brinj
2218:birinj, bei. LW. brinj (34) ^).
```


## [2026-09-05T05:55:30.410Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SOD ==\"; grep -n -i \"sin, bad\\|'sin'\\|βz\\|ʾβž\" SOD.txt | head -30; echo \"== SOD_pages 18 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==18' SOD_pages.txt | head -50",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-05T05:55:32.023Z] TOOL RESULT

```
== SOD ==
== SOD_pages 18 ==
 ij JLij^jj^jsU jua o HTt j> j ,(STi) >f <^j juSl
 _u, .(STii) Jub^T^ <y^^ ** ^^ j'j ^ •'-r*A < jLw juf ^T -uj ^ajlja                 ^JJb ^jZtj^S     iJJu aljO    jJ _ JLjIoJUUj      0>-a*    U^» j y-:-* ' j' <*UpwJb

 BSTi ,Ntt j* :^             >l^   Ij jJ^ j£j dy* u^U <>^J ^ J#> jl

 u^jj? c5^j^v BSTii W&T ^ j < jJo* j~=r>r ^*> j jl ^AiJa                            ^     c?>u o^1 ^i ^Js.                & j ji* t>>*^ j*j j* ^^< ^ Lf-1^ cf*

ojlfJ* <L*JLS' c&jji »tjT * j-XU v^US" jl ^"ULaS) ^^.j.,..* Ojv> j!                 J *_^^A <J^J 'JLi <**rji ^j>* (J ^L^^J c^JV^1 U>> j£±* ol-r«JMrf 4^

                                                                                    J Lf-^^* iJy^ J' cf,a'JLfc7 -JLb^X <*^--H Ij j-^i-1 Ujv^1 < J-J U^jJjjj

jjw» j^j'j-^ j^jl» ^Tr*" -(Eti4i) j^T ju; Ij Oj^U jU<^-y                   </ul»    (o jjvj>^j--) dj&-JJ <i j jU*I ^^--jj oU                    i^-o <, jlijjv ^yi'^

f ^i>y ^jul* j^ j jl ^jj^aL* I J^a j <Jlix* ^,^2^ cjj I Ij BSTii                    j JL-JI j Ifl-ljJ <{S~i 6ji J^'jl j^ <uj^* jJ jl-,^--! -a^ Jii^

jlji (STSC ) ^jJr^ . » ,_£ JL^ cyU<ii jJC — J j;<jJ(Iu» ii_ja- ^ 4-fL* j            p-iU- Ls<JUr-*j<» >^A» JU. ji j-rj- j <<— Jl^i j ^iUJT <j ^^--Jjjj

^*JLi j^wJ          <T Ij ^j^y          j^ULjj-w,      ^^C-J .(WV)           ji-    >> ^j>r-           «^ >^             j <~rs    (Frag- Len.) ^^              -u Ijjf\j

^oU«jlj i^j-^-i^jl ^<^p^ji ^i^li^K" <;Li> Oj^* ^jw           t xc^-l BSTi-         ji ^w jj j Manichaica Selecta ji m« jj .BSOAS ji ^A^
JU >> Ojv-^i jJ (jjj            7-<> (JtIa^-J ^jj jl ^j-jsxS^ j Uc^IjjL
                                                                                                *     "Ju>>jiljfBulletion of the Asia Institute
                                                  ,(C2) j/ ^^          naa
Jj>* OL*J-^J j '-■■♦ A4j * JiJ j jJ_y» Jcu*_j7 «JLS*^.7.;.< ^jpe--** o>>           {Jj-a* T* J>U- 4*io3 jA .Aj» f\i tftJLi- <-^-y ^7 jO jl <f tut^JU^
j (VW&) AoFii j (ttVf) AoFi ^ OUjJUjj .cj/ J^j ^j^,                                .Cwt ftAi ^ jUjU j^S JUx_-v-— - 1 u-JLmj j-J Uy- I^-a^ jl ^j^Ioaj o c— <l

^l^> juju>- 0j>> V j (JiiT lj •juIjp-U ol& jl Lrd*j OM)             AoFiii         Ac^fl ^j-cy          j> ,j j!)U* ^A^       JU jj tfj^£* Ij (»j>ii> oUJa* ^1

lActa      Iranica jj ^j<Aia5 <JU^- jl ^^Lj jojl»- ,y> ju->- ^j .j^                                                                        .j^T ^          >> Iranica
                           .j^T K^-J ^UT -u jj Ij <HAA JU <Y^ ^«jU-i               <i *£ 'j l? JL*-' JJ-r-' ^^      ^H^— rri O^j-^j j >jj ^^ * Jl^ >>

                                                                                   iaj^<> ^-7 jt Jjj— <*iai ^y-'jJUo L dlj.*^ <^jj «JLi <ii_jj ^ JUL- ioj>-

                                                                                   L Uij^-. j.1 .i^T ^i^»           cf -U- ^^        i/jk JJ-r- <*il* ^ -> tJj^

                                                                                   j;U<-^-^ j;<P y**?** ji Uj-jjvCU-O j-Xp j <~*rji <ZJ^jXJj>~
                                                                                                                                                                              ■^j
^ jj WYT        JU ji <«JLi tJiiM.^ j^ju-* o^j<j jjv^l7 <^ o~-l ^j^^i-             jib, jl ^JUw iS^Jj** -J^--j w^>* ^ <C^ULJ               Ifjj -lis- <(CII) ^7^/
                                                                                   jU-ijjjJLjl j oLSa^j*                  <j>j-*> j.m-^^ l? ^j^-^ c**-k-H jp
j <ai iJtiS" ^       «j>r ^ ^j**!* Lf^'^U j* i^^i-lLiOl^X ^l*^ jU^
                                                                                                                                            .Xjb    ^   ji Ij ^U*jvw


^UmJ)^^ j jL; I j-^- ^•JLXAJ o^Jlji ijblJl j j Jjj ^UU          ^*— ^ jj jL*



j fj&- >> »*ji'yi; -ll-r-- *-^i >* *^ '/*-* *.p *»li-»t .jjta jl^* <xJ-r^—         <(jlijjy JU-t    t^Jfjj    ji ijjjjln:,'* j'j^J (jT<*^j>-^ »X          ^^JUwUT        >>

                                                                                   jl ^LaOoIX*-       j t ■ i ■ iC »LI    jl ^ LaJU-^Ij   < J-r^jl ^J-i—     ^Iao^ Ijj
```


## [2026-09-05T05:55:41.605Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD.txt SOD_pages.txt && sed -n '1,20p' SOD.txt && echo \"=== search bz ===\" && grep -n \"^ *1[0-9] \\|^18 \\| 18 ʾ\" SOD.txt | head -20",
 "description": "Inspect SOD structure"
}
```


### [2026-09-05T05:55:41.691Z] TOOL RESULT

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

=== search bz ===
2585:11 
7710:10  »pr  B  ^)J  <WV 
7719:11  »pr-   B,  M,S  WT<j^ 
7727:12  -»pr  B,M  ^v, 
7734:13  "pr'ys'k   B  ^<J-<jjjT 
7742:14  "pr'y  **  -»pr 
7744:15  "prYs'k  =>  'prxsy(y) 
7746:16  "prYs'kmync  S  ^Ji^s*  < j*&^M^ 
7753:17  "prYs'y  4  "Pr^s'k 
7755:18  >Jprxsy   M  ^^  <o^  < jjj7 
7764:19  "prxsymync  M  ^jjjT 
9050:10 
9229:11 
9392:12 
9558:13 
9731:14 
9908:15 
10085:16 
10448:18 
10596:19
```


## [2026-09-05T05:55:51.342Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'bz\\|'bj\\|'bz'\\|>bz\\|»bz\\|\\\"bz\\|'byz\\|»bj\" SOD.txt | head -40",
 "description": "Grep Sogdian bz forms"
}
```


### [2026-09-05T05:55:51.401Z] TOOL RESULT

```
27011:P^zaxak  ?  =»bz}xwq,  'pyz'ywk^ 
27798:P(3)zaxutya   ->bz}xwty},  'Pj'xwty^ 
43263:5340  mn6-'  B  jj»bjK;
```


## [2026-09-05T05:55:52.105Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sin\\b\" SOD.txt | head -40",
 "description": "Grep sin in SOD"
}
```


### [2026-09-05T05:55:52.161Z] TOOL RESULT

```
4334:Tarlm  basin,  mentioned  In  Chinese  annals  from  around 
5785:/oktani/      ykrt>ny(h)     sin  Olr.  *krtani 
11286:evil  deed,  sin 
11884:afsin   ©<*xsaewan 
12742:sin,  evil  deed 
12853:sin,  evil  deed 
12956:sin,  evil  deed 
25092:sin,  corruption 
25385:&Gersh.);  Oss.  raxsin   =»Pr}xs-,  b'rxs-,  brxs-, 
36009:sin,  fault,  error 
36061:sin,  shortcoming,  fault 
40445:sin,  evil  deed 
44129:marsisin 
45275:mortal  sin 
51700:from  sin) 
65005:r(u)xusn   ©Yaghn.  raxsin   ©nom.  ob.  -y;  ace. 
68144:sin 
69611:sisin 
70389:9251  sin-   C  jjii-^^  ^  jl 
73061:sin,  sinful 
87420:avoiding  from  sin     6539 
91873:mortal  sin     5611 
93667:sin     582,  812,  827,  841,  2639,  4296, 
110344:avoiding  from  sin 
110346:avoiding  sin
```


## [2026-09-05T05:55:56.218Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '93660,93672p' SOD.txt; echo \"=== 11280 ===\"; sed -n '11275,11300p' SOD.txt; echo \"=== 12735 ===\"; sed -n '12730,12760p' SOD.txt; echo \"=== 12845 ===\"; sed -n '12845,12870p' SOD.txt",
 "description": "Print SOD sin entries"
}
```


### [2026-09-05T05:55:56.325Z] TOOL RESULT

```
5770,  5772,  5773 
similar    2265,  2266,  2267,  5193, 

5199,  5208,  5322,  5354,  5440,  5629 
similarity     5209 
similar  to    4385 
Simon    9126,9285 
sin     582,  812,  827,  841,  2639,  4296, 

4306,  4950,  8922,  9637 
since     3144,  3145 
sincere     1438,  1439,  1440,  2246, 

=== 11280 ===

581  'pyz'ywksth    B  o^jo  ^ 
(o)Pizaxukst   ©elat.  -wy  ^'P^ykwstr, 

w^yz^wksth 
miserable 
VJ  825;  Gersh.  JRAS  1942,  92 

582  »pyz'krtyh    B  .Lfu,jr 
(o)pizak(r)tya/i   OPyzktyh)   ^'Pzykrtyh 

evil  deed,  sin 
TSP;SCE;STii  10.43.46 

583  'JJyz'nkVk    B  X±<J&*jt 
(o)pizangare   OPyz'nkr'k)   -^'Pyz'nk^'y,  'Pjng'ry 
evildoer 

VJ  49c,  476;  TSP  7.40,  120,  188;  'flyJnkVw,  VJ 
31d 

584  »pyz,nkVy    B 
(3)pizangare   ^Pyz'nk'r'k 

evildoer 
VJ  652,  1187 
=== 12735 ===

810  >krt»k  **  'krt'y 

811  >krtWry   S,  B  jf* 
(o)krtan-karc   ^'qt^yk'ry 

sinner,  evildoer 
Magi.  138.32;  TSP 

812  >krt>ny(h)    B,  S  &f  <x  X 
(o)krtani,  oktanya   ^kt'nyy 

sin,  evil  deed 

VJ;  TSP;  SCE;  BSTBL;  Frag.  Len.;  S  W,  AO  1981, 
16 

813  'krt'nyk'r'k   B,  S  J^j<jfx 
(o)krtani-kare   ^qttoyk'ry 

sinner 

VJ;  Frag.  Len.  93.9;  Hen.  Magi.  138.38,  ob.  pi. 

-k*ryty\  GMS  1125;  'krt'nyk'r'y,  VJ  758,  994 

814  Wnyk'rch   S  jfj, 
(o)krtam-karc   ©f.  adj,   ^qt'nyq'rc,  qt'nyq'ry 
sinner 

BBB  101  e22;  Hen.  Magi.  138.35;  GMS  1125 
=== 12845 ===


*J^./<jy 


827  'krty'kh   S  fluf  .xj-* 
(a)krtyak 

sin,  evil  deed 
Sund.  MHC  p27.10 

828  >krty>kryyh   M 
(o)krtya-kare 
performer 
Hen.  Sogdica.  55.14  p57 

829  'krtyh   B,  S  =»  }krty> 

830  'krtyy   M  =>  >krty,  >krt>y 

831  >ks-   B 
(o)kasc,  (o)kos(e)?   Oks}y)  ©Av.  kdrdsa-,  Khwar 

yks   =*ks-     - 
small,  thin 
GMS  1201;  Benv.  VJ  n  p94,  39d;  Inst.  >ks\  SCE
```


## [2026-09-05T05:56:05.254Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 2639 4296 4306 4950; do echo \"=== $n ===\"; grep -n \"^$n  \\|^$n \" SOD.txt | head -3; done",
 "description": "Locate SOD entries"
}
```


## [2026-09-05T05:56:06.249Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"fazag\\|fažāg\\|fazak\\|fažāk\\|fajakand\\|pazd\\|bazd\" HENNING_selected_papers.txt | head -30",
 "description": "Henning Sogdian loanwords grep"
}
```


### [2026-09-05T05:56:07.078Z] TOOL RESULT

```
=== 2639 ===
25089:2639  pn's   B  ^Li^uf 
=== 4296 ===
36006:4296  yw»n    B,  M  j^^f 
=== 4306 ===
36057:4306  y\v*n   B,  M,  C  (J>>  >-^  j>)*\£  t^r^  'J&J> 
=== 4950 ===
40442:4950  qt'ny   C  .Lf  <ju>*
```


### [2026-09-05T05:56:07.135Z] TOOL RESULT

```
7822:(B) y28'n- (line 4), transla mysterious Pahlavi word he’n (‘2’), regarded by some as an ideogram, which in employed to render the Avestan dazma- in the Pahlavi o ‘The relation of y28'n-, which may reflect Manich, Middle Porsian dn, to Pal. he'n is the same as that of Av. pazdu- to Pahl. pasdk dued to Pahl, and Man, MPers. du, secondary, 0
```


## [2026-09-05T05:56:19.405Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11180,11290p' SOD.txt",
 "description": "SOD entries around 570-582"
}
```


### [2026-09-05T05:56:19.463Z] TOOL RESULT

```
Sund,  p40;  MSP  b!2 

568  'pyVt-   S  jaL  * jijjTc-i-u 
(o)Pyart   ©pt.  st.  ^Py'rt- 

(ro)obtain 

STii  p580;  Hen.  Miltelir.  p63;  AVS  104 

569  >py>s-  =>  'Py'ys-,  py'ys- 

570  'py's'ntcy   B  oiij>- 
(o)pyesanc-   ©f.  adj.   ^Py'ys'ntk 

boiling 
SCE  235 

571  »py»tr  =>  »py»tr 

572  'py'tCw)   S  c?->JT^<^ 
aPyat  .*  . 
reminding 

Anc.  Lett.  4.8;  Sund.  A  green  leaf,  AI  1988  pl8l, 

byhqhc 

573  'py'ys-    B  0-^>r 
(o)Pycs  ?   0PyJs-)  ©Av.  abi-aeh  Yaghn.  cs 

^Py'^ntcy,  Py*ys*ntk,  Py'ys- 
OcOboil 
GMS  90;  >pfYs  1  TSP  19.6  n  p232 

574  »bynt-   C 

aPont/d   =>Jbst-,  >bnt(t) 

(to)bc  attached 

Sund.  AoFiii  1975,  62;  C2,  31V24,  40V10  n  p75 

575  >byr-  **  Jnpr- 

576  *bysty  C  l°#j*< 
aposte   ©pp.   =»}bst-,  }bynt- 

joined,  related 

STi;  Sund.  AoF  1975,  62 

577  }pywn-  =*  Py}wn- 

578  *pywny   M  (e-LuTLr^crL,)^U 
(o)Piwane-,  (o)Pyonc   ©<*abi-waina—,  Parth. 

frywn   ©pi.  -f   =»bywny 
prophet 
GMS  434 

579  >pyz-    B,  S  (o^>^  j^^oij** 
(o)Pez   (bz-,  >Pyzy)   ©ace.  ->v;  nom.  ob.  ~U)y,  -\ 


jr"X$ 


m 


bad,  evil 


■lPj-  }Pz-,  Pyj-.  Pyz- 


23 


'pz'yCh) 


jli  X  t  j£&j 


GMS  179;  TSP  9.122  (nom.  -v) ;  SCE  272  (ace. 
-w);  VJ  318  (ace.  f.  ->);  VJ  102  (abl.  ->) 

580  'pyz'Ywk01    B  l^^o;.^ 
(o)Pi/ezaxuk   -^Pz'ywk,  bz'xwq 

miserable 

VJ  831,  958,  1382;  GMS  391,  976  n  1 

581  'pyz'ywksth    B  o^jo  ^ 
(o)Pizaxukst   ©elat.  -wy  ^'P^ykwstr, 

w^yz^wksth 
miserable 
VJ  825;  Gersh.  JRAS  1942,  92 

582  »pyz'krtyh    B  .Lfu,jr 
(o)pizak(r)tya/i   OPyzktyh)   ^'Pzykrtyh 

evil  deed,  sin 
TSP;SCE;STii  10.43.46 

583  'JJyz'nkVk    B  X±<J&*jt 
(o)pizangare   OPyz'nkr'k)   -^'Pyz'nk^'y,  'Pjng'ry
```


## [2026-09-05T05:56:29.988Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^[0-9]\\{2,4\\}  .pz\\|^[0-9]\\{2,4\\}  .pj\\|^[0-9]\\{2,4\\}  .p[yz]\" SOD.txt | head -40",
 "description": "Find bz-family main entries"
}
```


### [2026-09-05T05:56:31.673Z] TOOL RESULT

```
7816:28  »pyc  =>  »P>ycy 
7818:29  »pyr  =»  »P>yr- 
8973:226  Mpyk   M 
8978:227  »pync  r'ph  =>  9p}ync  r'Ph 
8980:228  "pznp'k   B 
8986:229  "pznph    B,  S  =>  »pznp>k 
10522:464  *pj-   M  (_jS;jLi-j)oUf  <jjj<uuij<ju 
10538:466  'pjng'ry   M  j£*j.tj&kf 
10545:467  *pjwnyh   M  ^jjji 
10551:468  »pjyn   M  ^J\ 
10557:469  'pjynyh  =*  'pjwnyh 
10559:470  'pjyr'ync    M  j^f^UI^UI 
11154:564  »py»tr   B  j^> 
11177:567  'py'pt-   S  j3\t*z~*<d>J'^'j> 
11183:568  'pyVt-   S  jaL  * jijjTc-i-u 
11190:569  >py>s-  =>  'Py'ys-,  py'ys- 
11192:570  'py's'ntcy   B  oiij>- 
11198:571  »py»tr  =>  »py»tr 
11200:572  'py'tCw)   S  c?->JT^<^ 
11208:573  'py'ys-    B  0-^>r 
11232:577  }pywn-  =*  Py}wn- 
11234:578  *pywny   M  (e-LuTLr^crL,)^U 
11241:579  >pyz-    B,  S  (o^>^  j^^oij** 
11269:580  'pyz'Ywk01    B  l^^o;.^ 
11276:581  'pyz'ywksth    B  o^jo  ^ 
11283:582  »pyz'krtyh    B  .Lfu,jr 
11296:584  »pyz,nkVy    B 
11302:585  'pyz'nkr'k  =>  'Pyz'nk^k 
11304:586  »pyzp'rch   S 
11315:588  'pyzpr'n  =*  'pyzypr'n 
11317:589  'pyzktyh    B  =*  >pyz>krtyh 
11319:590  >py2y  =»  >pyZ_ 
11321:591  >pyz>pr>n   B  ^^ 
11354:594  »pz»w-  .  B  =»  'pz'w- 
11362:596  'pz'ywk  S 
11367:597  'pz'nx^y   S 
11373:598  >pz»w-    B 
11382:599  >pz}w  «*  'pz'w- 
11384:600  »pz»wn   S 
11389:601  »pz'xtyh   S
```


## [2026-09-05T05:56:36.144Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10500,10560p' SOD.txt",
 "description": "SOD entry 464 bj-"
}
```


### [2026-09-05T05:56:36.199Z] TOOL RESULT

```
461  >p«>yp<>}   B  j^y 
of5ep(a)   ©<*fra-daip-   =»ftyp- 

radiance,  brilliance 

BSTBL,  Dhu.  101,  103;  STSC  57 

462  >p6>ys   B  ^u^.^c-Jj 
ofSes   (f8ys)  ©<*fra-daisa-   ^fS'ys,  p8'ys- 
appearance,  vision,  region 

BSTBL,  Dhy.  354,  371.159(N);  GMS  3l5A;  AVS 
125 

463  >pY>n   B  uU3 
sfyan   ©ob.  pi.  -ty  ^Py'h1 

lament 

VJ  533  n  p97 


464  *pj-   M  (_jS;jLi-j)oUf  <jjj<uuij<ju 
aJ3z,  Piz,  Paz,  Pez   (byz-,  bz-)   ©<Av.  bazda 

©ob.  -y  =»>pyz-,  }pz-,  Pj-,  pyj-,  pyz-,  Pz~ 
bad,  evil,  pain 
GMS  179,  510;  Hen.  LW  101;  S  W,  AO  1981, 

13n8 

465  'Pfxwty'h   M  j*** 
aP(o)zaxutya   ^Pj'xwty'h,  PzJYwty}kh 
unhappiness,  misery 

GMS  391,  1070;  BBB  b61;  Gersh.  Sogd.  Cpds. 
1945,  140 

466  'pjng'ry   M  j£*j.tj&kf 
oP(o)zangare  ©ob.  pi.  -tyy  ^Pyzmk^k, 

bzng*ry 
evildoer,  sinful 
GMS  1126;  BBB  520 

467  *pjwnyh   M  ^jjji 
aPzo/enya  CPjynyh)  =^Pjyn 

increase 
GMS  1026A 

468  »pjyn   M  ^J\ 
aPzcn 

increase 
GMS  187,  1026 

469  'pjynyh  =*  'pjwnyh 

470  'pjyr'ync    M  j^f^UI^UI 
oPzircnc   ©f.  adj.  ^Pjyrnyh
```


## [2026-09-05T05:56:42.811Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=10200 && NR<=10700 && /^ *[0-9]{1,3} *$/ {print NR\": \"$0}' SOD.txt",
 "description": "Find page number markers near entry 464"
}
```


### [2026-09-05T05:56:45.322Z] TOOL RESULT

```
10261: 427 
10264: 129 
10273: 433 
10448: 18 
10512: 125 
10596: 19
```


## [2026-09-05T05:56:51.336Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"loan-words in new persian\\|loan words in new persian\" HENNING_selected_papers.txt | head; echo ===; grep -n -i \"agand\\|āgand\\|fazak\\|fazsk\\|paz \" HENNING_selected_papers.txt | head -20",
 "description": "Find Henning SLW article"
}
```


### [2026-09-05T05:56:51.395Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T05:56:53.892Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"loan-words in new persian\" HENNING_selected_papers.txt | head; echo \"-----\"; grep -n -i \"agand\" HENNING_selected_papers.txt | head -20",
 "description": "Find Henning SLW article"
}
```


### [2026-09-05T05:56:53.960Z] TOOL RESULT

```
-----
20837:fach weggelassen oder so verindert, daB es harmlos aussieht; nichts liegt dem Ubersetzer ferner, als etwa die Lokalfarbe xm wahren. Die Druj, die Diimonen, welche Ahriman gegen die Menschen schickt, eracheinen als ndie natirlichen Eigenschaften und Begierden', das ,,Gesetz der Dit- monen' wird der ,,Befehl des Teufels", die Dimonin Basdep wird Tief- achlaf, der zoroastrische Priester ist einfach ein Fagih, und die Frage well jon int die beste" ist taktvoller Weise beiseite gelassen. Dem ganzen Stiick sieht man nicht mehr ohne weiteres seinen fremden Urwprung an, und der Leser kann kaum umbin, zu finden, da® Buzurj- mihr und seine Zoroastrier eigentlich ganz gute Muslims waren, Man kann wohl sagen, daB solche Obersetzungen eine Art kultureller Propaganda darstellen.
21655:One would contend that the purely historical evidence, summed up in the preceding paragraphs, deserved more credit than the legendary story of Mani’s life. Hagiography is not history; it is biassed and involves elements of religious propaganda. We hear of Mani’s age only on three occasions: when he was twelve, when he was twenty-four, and when he died at the age of sixty. Is it eredible that the prophet’s life thus proceeded in even jumps of twelve years precisely? Five and twelve, we must remember, were sacred numbers for Mani; everything in his system was grouped in pentads or dodecads. Did Life accommodate itself to Mani’s system to the extent of granting him a span equal to the product of his favourite numbers? Such figures are no more than approximate values at best.
23348:sgrave). Yet although on the face of it no Muslimie censor could have found fault with it, we should remember that this is a Manichaean poem and realize that the apparent meaning conceals a hidden sense. ‘Then the speaker becomes the viva anima griw sindag, the ‘Living Soul”, that is ever suffering through malice and neglect, cast aside and trampled on, a stranger in this evil world. So understood, the poem may be regarded as a witness to the adaptability of Manichacan propaganda, to its readiness to assume ever fresh disguises in order to meet the demands of the times. Just asin earlier centuries Christians and Buddhists had compl
```


## [2026-09-05T05:56:59.349Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sogdian loan\" HENNING_selected_papers.txt | head; echo \"---files---\"; grep -rn -i \"fažāgand\\|fazagand\\|فژاگند\" . --include=*.txt 2>/dev/null | head -20",
 "description": "Search Sogdian loanwords and fažāgand"
}
```


### [2026-09-05T05:56:59.407Z] TOOL RESULT

```
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
---files---
(eval):1: no matches found: --include=*.txt
```


## [2026-09-05T05:57:02.175Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -rn \"فژاگند\\|فژاک\\|فژ \" --include=\"*.txt\" . 2>/dev/null | head -20",
 "description": "Grep Persian faz forms"
}
```


### [2026-09-05T05:57:02.273Z] TOOL RESULT

```
MON_part2.txt:7273:فزه: (2۸)۵] [قس. فژ فوا کن به‌اگن] 
MON_part2.txt:7283:فژاک: ۱21-0 (ص‌مر.) چرکین؛ چرکن» 
BQT_v1.txt:25017:افژ ول با زای قلرسی بروزن مقبول. 
FRS_pages.txt:3769: ‫چونغلیجی که بنه بر کند [کذا‪ |] :‬کیست چون تو فژاکن‌و فزغند‬
FRS_pages.txt:11201:‫تاکی‌همی‌در آبی‌وکردم همی‌دوی حقّاکه کمتری‌وفژ آکن‌تریز پك‪]۱‬‬
SBK.txt:21171:حرفژ 
MON_part1.txt:31416:یز 22 [فژ ] (.) چ رک ریم پلیدی. کهنه» 
MON_part1.txt:31425:پذاگن: 0- ۳21-5 [یز + ۳ - فژاکن] 
MON_part1.txt:31427:فژاکن» بژوین» دنس. زشت» نازیبا. 
FRS.txt:3589:چونغلیجی که بنه بر کند [ کذا: ]| کیست چون تو فژاکن‌و فزغند 
FRS.txt:10340:تاکی‌همی‌در آبی‌و کردم همی‌دوی حقّا که کمتری‌وفژ آ کن‌تریز پك۱] 
FRS.txt:16082:پلید و پلشت باشد و فژاکن [رودکی گوید : 
incoming/BQT/BQT_v3_pages.txt:20208:۱ -قس: ‎SG AM oo‏ فژاکن» فزه,‌فراك» ‎SNe‏
incoming/BQT/BQT_v3_pages.txt:20217:در فارسی هم وارد شده . دربرهان قاطع ‎OLE‏ ذبل‌آمده : راك , فژاکن » ‎GTN‏ فژغند.
incoming/BQT/BQT_v3_pages.txt:20268:‎Slam ۴‏ (هم.) ‎(GS Ham‏ س فژاکن . ورك : فز.فژه:فزه. ۴ - یزهنینگه
incoming/BQT/BQT_v3_pages.txt:20270:‏گوید (رك:صفحهّقبلح۸): فژاکن (رك : ‎usuely seal‏ معرارجمالی: ‎(fazhakan‏ قس:سغدی
BQT_alt_v1.txt:22620:افژ و با زای فارسی بروزن مقبول, 
BQT_alt_v1.txt:22624:افژ و لنده بر وزن افروزنده 4 سر 
BQT_alt_v1.txt:47487:فژ و له ح بروزن دربند » چویی باشد 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:31416:یز 22 [فژ ] (.) چ رک ریم پلیدی. کهنه»
```


## [2026-09-05T05:57:07.058Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=20180 && NR<=20290' incoming/BQT/BQT_v3_pages.txt; echo \"=== nearest page tags ===\"; awk 'NR>=19800 && NR<=20400 && /pdf page/ {print NR\": \"$0}' incoming/BQT/BQT_v3_pages.txt",
 "description": "Read Borhan v3 faz entry"
}
```


### [2026-09-05T05:57:08.943Z] TOOL RESULT

```
‎Go 0/8‏ اول ‎gly‏ و سکون ‎she‏
‏پلید و زشت را گوبند ۱ - و بمعنی غالب شدن
هم آمده است ۷ .

‏هشتم

‏در حرف فا با ژای فارسی مشتمل بر هیچده ‎Ca)‏

‎cae 9‏ اولوسکون ثالی (6۷» ‎ee‏
‏چرك باتد که عربان وس وید ۸ - و ض‌اول

‎. ale -: ‏چش‎ )۱(

‏۱ = 0 جپانگیری > ظ. مسحف ‎Oy‏

‏۴ رل : افزار .
‎So‏

‏بمعنی یال اسب باشد و در عربی عرف بضم ‎we‏
‏ی‌نقطه خوانند .

‎(x)‏ چك ,چش : مین.

‏۴ ازه افرودن > حه فزودن .

‎AHP‏ (ه.م.).وفس: ‎SV‏ فزاکین, ‎ASV‏ فره» فژه.
ظ . مصحف « فروده » ‎Com)‏ = فرود = فرودین .
۱ -قس: ‎SG AM oo‏ فژاکن» فزه,‌فراك» ‎SNe‏

‏۷ - مصحف‌فره» (هم).

‎Sty ) ‏درشاهنامه آمده (رك : فهرست ولف‎ UG ‏-پژاهم.). «فز » 22 که‎ A

‎Fizhih‏ ( شمی فخری ص۱۷۹ ؛ با ‎ait fitih op‏ آمده وبحتمل خطا باشدوسحیح آن1326
با ‎fizhe‏ باشد) درست ازسقدی - ۲92 ۲92-۰ ,- ۱82 , سقدی مبحی 0۷2,028
مانوی - 8" ‎Byj . Bj.‏ « بد » کناه ‎Live‏ یار رابجی‌است ودارای مشتقات بسیار . بعضآنها
در فارسی هم وارد شده . دربرهان قاطع ‎OLE‏ ذبل‌آمده : راك , فژاکن » ‎GTN‏ فژغند.
فزفنده ‎Se‏ ف ٌکنده . غاب آنها محتمل است که ناثی از تخیل ‎cad‏ وان
بائد . 102 ‎Henning, BSOS , X-1,p.101-‏ .
[pdf page 279]
AS

‎IS‏ = بتتحاول بروزن هلاكبمعنی
‎coh‏ و"چرکن و چركآلود و پلید باشد .

‏فا کن بر وزن مساکن ۴ » بمعتی
‎I‏ است که چرکن وچرلآ لود و پلئت وپلید
باشد ۴

‏قژا لین - ‎GEL‏ فاسی ۴ بر وزن
شیاطین, بمعنی‌فژا کن است که چر کن‌وچرل] لود
ویپلید وپلشت باشد .

‎ge? eZ‏ وزن شب چره » چوبی
باشد که در پس در خاله اندازند تا در کشوده
باشد .

‏(۱) خم۱ : اکیر .

‏روا

‎ce = TIS‏ اول و ثالی وسکونزای
فارسی » ‎ol‏ است که درد =

‏شکم را سود دارد
‎ATT,‏ تکی و اکر(۱) ترکی خوانند.

‏فژغرده = بفتح اول و غین نقطه دار
بروزن سکرده + ‎gine‏ خیسیده ونم کشیدموتر
کرده وآغشته باشد ۷ .

‏فژغنك - بر وزن فرزند | چیزی پلید
وچرکن ‎Maa Sl)‏ - و ‎gine‏ عشقه هم آمده
است وآنکیاهی باشد که بر درخت پیچد ‎٩‏ .

‏فزغنده ”= بر وزن ارزنده » بمعنی
‎oa‏ وچر کن وچركآلود باشد .

‏۱ - از ‎ay) STH:‏ سبت و اصاف ) « دارستتر ‎coke.‏ ۱ ص ۷۷۵ )
و راد : فژه فزال.فزاکن.فژااگین,فزه‌فره. ‎NGG:‏ , پلشت ‎cope‏ اسدی (طوسی) کوید :

‎Sle‏ چون‌تو فزاك آعدم

‏و کرچون نو ابله ‎Md‏ آعدم.»

‏«لفت فرس ۲۳۰۷ .

‎Slam ۴‏ (هم.) ‎(GS Ham‏ س فژاکن . ورك : فز.فژه:فزه. ۴ - یزهنینگه

‏گوید (رك:صفحهّقبلح۸): فژاکن (رك : ‎usuely seal‏ معرارجمالی: ‎(fazhakan‏ قس:سغدی
«پت ۰ فرومایه» . ‎Sole‏ فارسی آن > ‎«oy‏ 0226 ( کناء ) است. ‎My‏
‎Fazh-agin = ۴ . Bailey, BSOS, VII,p.85‏ ت رکیبی قارسی است ۰
‎H+ 4) Henning, BSOS, X.1,p. 102.note 1.‏ فزاك. ‎S19‏ فزکن «فژه‌فزه»
فزاکین » پزاکن :
نژاکن نیم سالخورده نیم ایرجفت ‎slay‏ کرده نیم. بوشکوربلخی« لغت فری ۳۷۷».
‎SLO‏ مصحف « فردره »۳ فردر و رك : قزوره » فرورده » فرود » فرودین .
۲ -ظ . مصحف « فرژ » (هدم.) ک فرز(هم.) - ۲ - چهانگیری این بیت‌مولوی
را شاهد آورده : .
‎dle‏ اسرنور حق ‎ZZ‏ شد
اما این یت در مثنوی چاپ ‎GAG‏ ج ه ص ۳۳۹ لیامده ودرمشلوی چاپ ۱۳۰۷ قمری‌درحاشیه
آمده و بجای فژغرده « فرغوده » ثبت شده . صحیح ‎Ope) Cor pa?‏ اسم مفعول ‎ADI‏ ©
‎Cpa)‏ است . ‎A‏ فزغنده . »ف وکند, ورك : فز . حنینگ گوید : فزغند » لااقل
بمعنی پلید وچر کین » ناثی از ضحیف «فرغند» است .
‎Henning, BSOS, . X.1,p. 102  , ۰ ۱‏
درلفت ‎(aay) ue‏ آمده: « ینی فژغند بینی کندیده بود. عماره (مروزی) گوید :
ممذور است ار با تو سلزد زنت ای غر زان کند ‎Obes‏ نو وزان بینی ‎MED‏
‎dy ۰‏ فژفند ‎ee‏ فژه» فزءفزه.

‏پی زعلمت نور ‎eb‏ قوم لد:

=== nearest page tags ===
19855: [pdf page 274]
19917: [pdf page 275]
19989: [pdf page 276]
20058: [pdf page 277]
20150: [pdf page 278]
20220: [pdf page 279]
20292: [pdf page 280]
20380: [pdf page 281]
```


## [2026-09-05T05:57:22.009Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['PRT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('AEF'),ensure_ascii=False,indent=1))\n\"",
 "description": "Check BQT page mapping"
}
```


### [2026-09-05T05:57:23.632Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
{
 "title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958",
 "edition_found": "1958 (lending-only copies)",
 "kind": "archive_restricted",
 "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending",
 "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)",
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.",
 "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."
}
{
 "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
 "kind": "catalog",
 "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
 "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "none online; proxy via HRN/HUB. || RE-SEARCH 2026-09: still catalogue/purchase only (Open Library record; iketab second-hand; digikala dkp-3058984 for the 2015 ed.). Publisher of the 2015 ed. is مهرافروز."
}
```


## [2026-09-05T05:57:33.963Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))\nprint(type(m))\nif isinstance(m,dict):\n  ks=list(m)[:5];print(ks)\n  for k in ['276','277','278','279','280','281']:\n    print(k, m.get(k))\nelse:\n  print(m[:5])\n\"",
 "description": "Check BQT v3 pagemap"
}
```


### [2026-09-05T05:57:35.460Z] TOOL RESULT

```
<class 'dict'>
['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
276 None
277 None
278 None
279 None
280 None
281 None
```


## [2026-09-05T05:57:39.237Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))\nprint(m['offset_mode'], m['pdf_pages'])\nprint(json.dumps(m['anchors'],ensure_ascii=False)[:600])\nmp=m['map']\nprint(type(mp))\nimport itertools\nif isinstance(mp,dict):\n  for k in ['276','277','278','279','280']: print(k,mp.get(k))\nelse: print(mp[270:285])\n\"",
 "description": "Inspect pagemap details"
}
```


### [2026-09-05T05:57:40.633Z] TOOL RESULT

```
1203 721
34
<class 'dict'>
276 None
277 None
278 None
279 None
280 None
```


## [2026-09-05T05:57:44.382Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))\nmp=m['map']; ks=sorted(mp)[:10]; print(ks); print({k:mp[k] for k in ks})\nprint([ (k,mp[k]) for k in sorted(mp,key=lambda x:int(x) if x.isdigit() else 0) if k.isdigit() and 270<=int(k)<=285])\n\" 2>&1 | head -20",
 "description": "Print pagemap sample"
}
```


### [2026-09-05T05:57:45.861Z] TOOL RESULT

```
['1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1218', '1219']
{'1210': 1, '1211': 2, '1212': 3, '1213': 4, '1214': 5, '1215': 6, '1216': 7, '1217': 8, '1218': 9, '1219': 10}
[]
```


## [2026-09-05T05:57:49.591Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))\nmp=m['map']\ninv={v:k for k,v in mp.items()}\nfor p in range(275,283): print('pdf',p,'-> printed',inv.get(p))\nprint('printed 1485 -> pdf', mp.get('1485'))\n\"",
 "description": "Map pdf pages to printed"
}
```


### [2026-09-05T05:57:51.099Z] TOOL RESULT

```
pdf 275 -> printed 1482
pdf 276 -> printed 1483
pdf 277 -> printed 1484
pdf 278 -> printed 1485
pdf 279 -> printed 1486
pdf 280 -> printed 1487
pdf 281 -> printed 1488
pdf 282 -> printed 1489
printed 1485 -> pdf 278
```


## [2026-09-05T05:57:56.200Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2185,2235p' HRN.txt",
 "description": "Horn berenj entry"
}
```


### [2026-09-05T05:57:56.244Z] TOOL RESULT

```
206. bern 'Egge'.
Nur aufgenommen, weil G. Meyer (albanes. Wörter-
buch, S. 44) np. bern 'Egge als Etymon der entlehnten
*) Phlv. vrejan ist nur fehlerhafte Schreibung; np. biristen ist
durchaus nicht ungebräuchlich, wie Fr. Müller (WZKM. 5, 185) nach
V
Vullcrs meint. Ich citire nur Sahn. I, S. 20, Vers 8.^ - 48 —
slavischen Wortgruppe alb. braus *Egge*, serb. brana,
poln: brona, russ. borona, ngr. ößdpva etc. annimmt.
Das neupersische Wort ist aber ganz unsicher; die
Wörterbücher (ausser dem FS.) überliefern nur die
Form bezen, im Gacophylacium und bei Woliaston
fehlt es.
207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
Njm5 Is. 3, 4, 5, wumaj wernä, purnäk (unbelegt);
vergl. arab. LW. burnäj, barnaj, eine Dattelart (de
Goeje, Bibl. geogr. arab. IV, 189).
aw. aperenäyuka^ * Knabe*; phlv. apurnäyak.
afy. wör 'klein , wörkai, wörukai 'Kind*; bei. LW.
Warna jung, Jüngling (285).
208. (i)&fr«tijf, gurinj (AM.) 'Reis'.
Semn. varinj; (Käs. nur berSnj).
aw. ^verenja-; skr. vergl. vrthi- *ßeis'.
Vielfach entlehntes , gewiss ursprünglich arisches
Wort; vergl. arm. brinj; kurd. birinj; oss. brinj
(Hübschmann, S. 121); bei. brinj (35); wa/.
gurunj etc.
af/. vrize geht auf die Form ohne Nasal zurück,
wie gr. o()v£a, /J^(>«fa, ostt. uruz, urz, AM. eruz),
208^»« {2)birin) 'Kupfer .
Zusammenhang mit aw. berejya^ (in parö.berejya-)
ist durchaus unsicher; vergl. Schrader, Sprach-
vergleichung und Urgeschichte \ 273, 274, kurd. LW.
birinj, bei. LW. brinj (34) ^).
209. bemT 'Gefäss* (unbelegt).
aw. vergl. urunya- 'Schüssel* (vd. 14, 8); de Lagarde,
Beitr. z. altbaktr. Lexig., 71, Geldner, KZ. 25, 567
Anm. 21. Also zu [^var- Verhüllen, umschliessen ?
Unsicher.
210. bervär *Sommerlusthaus*, nn^X, nxnDN (Talmud).
aw. *upairivara- oder wohl besser ^upairivärana- ;
vergl. de Lagarde, Beitr. z. altbaktr. Lex. 54 folg.,
Semitica, I, 38.
»j Vergl. auch 'Prinzmetall*, Pott ZKM. IV, 264.- 49 -
211. berre, bere 'Lamm*.
g. vare; semn. vara; mäz. vare; Kä§. verrd, verä,
veri,
ai. ürana- *Widder, Lamm'; phlv. varak', arm. gam
Xamm' (H. No. 64).
kurd. vark^ garik, bar/, bar/ik (H.-Sch.); af;'. vrai\
oss. d. warik^ urek, t. värjg (78) ; bei. gvarak, n. gvaraU
```


## [2026-09-05T05:58:07.723Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT parö.b ==\"; grep -n -i \"brzya\\|bərəj\\|berejya\\|parö\\.b\\|paro\\.b\" BRT.txt | head -20; echo; echo \"== KLN bronze ==\"; grep -n -i \"bronze\" KLN_1966.txt | head -20",
 "description": "Grep Bartholomae and Klein for bronze"
}
```


### [2026-09-05T05:58:07.892Z] TOOL RESULT

```
== BRT parö.b ==

== KLN bronze ==
1788:aeneous,  adj.,  bronze-colored.  —  L.  aeneus,  ‘bra¬ zen’,  fr.  aes,  gen.  aeris,  ‘brass’,  which  is  cogn. with  OI.  ayah,  Goth,  aiz,  OE.  dr,  ser,  ‘brass’, ora,  ‘metal’.  See  ore  and  cp.  words  there  referred to.  For  E.  -ous,  as  equivalent  to  L.  -us,  see  -ous. Aeolian,  adj.,  pertaining  to  Aeolus,  god  of  the winds;  pertaining  to  the  wind.  —  See  Aeolus and  -ian.
1797:aequor,  n.,  even  surface;  the  sea.  —  L.,  ‘an  even surface,  the  even  surface  of  the  sea’,  fr.  aequus, ‘even,  level,  flat’ ;  see  equal.  L.  aequor  is  a  loan translation  of  Gk.  7r£Xayo;,  ‘the  open  sea,  the unbroken  surface  of  the  sea’,  which  is  cogn. with  L.  plaga,  ‘hunting  net,  curtain’,  and  planus, ‘level,  flat’  (see  pelagian). aerarian,  adj.,  fiscal.  —  Formed  with  suff.  -an  fr. L.  aerarius,  ‘pertaining  to  copper,  pertaining  to money’  fr.  aes,  gen.  aeris,  ‘copper,  bronze, money’,  which  is  cogn.  with  OE.  dr,  ser,  ‘brass’. See  ore  and  cp.  aes.
5712:bronze,  n.  —  F.,  fr.  It.  bronzo,  bronzino,  ult.  fr, Persian  birinj.
5713:Derivatives :  bronze,  tr.  and  intr.  v.  (cp.  F.  bron- zer),  bronze,  adj.,  bronz-ify,  tr.  v.  (rare),  bronz¬
19898:Derivatives:  irk-some,  adj.,  irksome-ness,  n. Irma,  fern.  PN.  —  A  var.  of  Erma,  which  is  a shortened  form  of  Ermentrud  (q.v.)  Cp.  Emma, iron,  n.  —  ME.  iren,  iron,  fr.  OE.  ise(r)n,  iren,  rel. to  OS.  isarn,  ON.  isarn,  jam,  OFris.  iser(ri), MDu.  iser,  Du.  ijzer,  OHG.  isarn,  isan,  MHG. isern,  iser,  isen,  G.  Eisen,  Goth,  eisarn,  isarn. These  words,  as  well  as  the  Gaul.  PN.  Isarno-  and OIr.  iarann,  iarn,  W.  haiarn,  OCo.  hoern,  ‘iron’, are  prob.  Illyrian  loan  words,  and  orig.  denoted the  ‘strong’  metal  (in  contradistinction  to  the softer  bronze).  Cp.  OI.  ifirdh,  “vigorous,  strong’, Gk.  Eep6q,  ‘strong’,  and  see  ire.
26525:ore,  n.  — -  ME.  oor,  or,  fr.  OE.  dr,  Sr,  ‘brass’,  rel. to  ON.  eir,  ‘brass,  copper’,  OHG.  er,  ‘brass’, OHG.,  MHG.  erin,  G.  ehern,  ‘brazen’,  Goth. aiz,  ‘bronze’,  and  cogn.  with  OI.  ayah  (gen. dyasah),  Avestic  ayo  (gen.  ayanhd),  L.  aes,  gen.
28421:pfennig,  n.,  a  small  bronze  coin  of  Germany.  — G.  See  penny.
34018:Schiedam,  n.,  Holland  gin.  —  Prop,  gin  made  at Schiedam,  a  town  in  Holland, schiller,  n.,  a  bronzelike  luster.  —  G.,  fr.  schillern, ‘to  change  colors’,  fr.  MHG.  schiilen,  a  collat¬ eral  form  of  schilhen  (G.  schielen),  ‘to  blink, wink,  squint’,  which  is  rel.  to  OHG.  scelah, MHG.  schel,  G.  scheel,  ‘squint-eyed’,  fr.  I.-E. base  *sqel-,  ‘crooked,  curved’,  whence  also  Gk. axaXvjvo;,  ‘limping,  halting,  uneven’.  See scalene  and  cp.  words  there  referred  to. Derivatives:  schiller-ize,  tr.  v.,  schiller-iz-ation, n.
38076:Talos,  n.,  1)  a  man  of  bronze  made  by  Hephaes¬ tus  and  given  by  Zeus  to  Minos,  king  of  Crete, to  watch  over  the  island ;  2)  nephew  and  pupil of  Daedalus  ( Greek  my t hoi.)  —  Gk.  TaXcog,  of uncertain  origin;  perh.  orig.  a  personification of  the  sun,  which,  according  to  Hesychius,  was called  TiXwg  in  Crete.  See  Albert  Carnoy, Dictionnaire  6tymologique  de  la  mythologie gr6co-romaine,  Louvain,  p.  191  s.v.  *Talos.
40107:triens,  n.,  name  of  a  gold  and  a  bronze  coin  in ancient  Rome.  —  L.  triens,  prop,  ‘the  third  part (of  an  as)’,  fr.  tres,  neut.  tria,  ‘three’.  See  three.
```


## [2026-09-05T05:58:19.796Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py; echo ---; tail -3 data/verification/sources/web/index.jsonl",
 "description": "Check fetch_source tool"
}
```


### [2026-09-05T05:58:19.843Z] TOOL RESULT

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
---
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%85/", "file": "data/verification/sources/web/779f0d3a871711a3.txt", "fetched": "2026-09-05T05:53:19Z", "status": 200, "bytes": 9748, "title": "بم - معنی در دیکشنری آبادیس", "note": "page 76: Mo(in entry for بم, no Arabic tag"}
{"url": "https://abadis.ir/fatofa/%D9%88%D8%AF/", "file": "data/verification/sources/web/b50d87e493daa23e.txt", "fetched": "2026-09-05T05:56:14Z", "status": 200, "bytes": 11405, "title": "ود - معنی در دیکشنری آبادیس", "note": "page 76: Dehkhoda/Moin entry وَد = بد (MON:4993)"}
{"url": "https://abadis.ir/fatofa/%D8%A8%D8%AF/", "file": "data/verification/sources/web/a9c8262b58448d18.txt", "fetched": "2026-09-05T05:56:16Z", "status": 200, "bytes": 16573, "title": "بد - معنی در دیکشنری آبادیس", "note": "page 76: Moin entry بد"}
```


## [2026-09-05T05:58:24.543Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9\" \\\n \"https://www.etymonline.com/word/bronze\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/bronze\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 77 verification\" ; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T05:58:29.811Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c73ee63573ce953a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a302e613963e0e45.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f63663460a9c2d0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bad8b3940952dbd0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7eebd4293cc12d9c.txt
```


## [2026-09-05T05:58:32.233Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== باده =====\"; grep -n -A20 \"Persian\" c73ee63573ce953a.txt | head -60",
 "description": "Read Wiktionary bade"
}
```


### [2026-09-05T05:58:32.276Z] TOOL RESULT

```
===== باده =====
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62- Etymology 
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
76- 1.5 
77- Further reading 
78-
79- Toggle the table of contents 
--
151: Persian
152- [ edit ] 
153-
154- Etymology
155- [ edit ] 
156-
157: From Middle Persian bʾtk' ( bādag , “ wine, must ” ) (cognate to Khotanese [script needed] ( bātaa , “ wine; must ” ) , Talysh boə ( “ date-plum (or grape) syrup; must ” ) ), from Old Persian *bātah , most likely from Akkadian 𒁀𒂅𒌑 ( baṭû , “ tray, platter; mixing container, bowl for liquids; wine jar, pitcher ” ) , from earlier Akkadian 𒁀𒋾𒌝 ( baṭium , “ vessel, basin, place to hold; tray, platter ” ) . Cognate to Arabic بَاطِيَة ( bāṭiya , “ a kind of earthen vessel for storing wine ” ) , Persian بادیه ( bādiya  / bâdiye ) , Classical Syriac ܒܳܛܺܝܬܴܐ ( bāṭīṯā ) , Ancient Greek βατιάκη , βατιάκιον ( batiákē, batiákion ) , Latin batiaca , batioca , batiola . Compare Middle Armenian բադակ ( badak ) , Old Georgian ბადაგი ( badagi ) , Udi бадакӏ ( badaḳ ) , as well as Jewish Babylonian Aramaic באדג ( bādāĝ , “ a type of wine ” ) , Arabic [script needed] ( bāδaǰ/q , “ boiled juice of grape ” ) and بَاذِق ( bāḏiq , “ red wine ” ) , all Iranian borrowings.
158-
159- Pronunciation
160- [ edit ] 
161-
162: ( Classical Persian ) IPA ( key ) : /baː.ˈda/ 
163-
164- ( Dari, formal ) IPA ( key ) : [bɑː.d̪ä] 
165-
166- ( Dari, formal ) IPA ( key ) : [bɑː.d̪ä] 
167- ( Kabuli ) IPA ( key ) : [bɑː.d̪ä] 
168-
169- ( Hazaragi ) IPA ( key ) : [bɔː.d̪ä] 
170-
171- ( Iran, formal ) IPA ( key ) : [bɒː.d̪e] 
172-
173- ( Tajik, formal ) IPA ( key ) : [bɔ.d̪ä] 
174-
175- Rhymes: -a 
176-
177- Readings
178-
179- Classical reading ? 
180-
181- bāda
182-
--
226: Dehkhoda, Ali-Akbar ( 1931– ), “ باده ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
227-
228: ʿAmīd, Ḥasan ( 1985 ), “ باده ”, in Farhang-e Fārsī-e ʿAmīd (in Persian), Tehrān: Amīrkabīr
```


## [2026-09-05T05:58:42.575Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '100,200p' a302e613963e0e45.txt",
 "description": "Read Wiktionary batiya"
}
```


### [2026-09-05T05:58:42.618Z] TOOL RESULT

```
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

 Etymology
 [ edit ] 

 Borrowed from Aramaic , cognate with Classical Syriac ܒܳܛܺܝܬܴܐ ( bāṭīṯā ) and Jewish Babylonian Aramaic בָּטִיתָא ( bāṭīṯā ) , with a possible mediary Old Persian *bātah ( “ wine, must ” ) from Akkadian 𒁀𒂅𒌑 ( baṭû , “ tray, platter; mixing container, bowl for liquids; wine jar, pitcher ” ) , from earlier Akkadian 𒁀𒋾𒌝 ( baṭium , “ vessel, basin, place to hold; tray, platter ” ) shifting semantically by the Neo-Babylonian period, but consistently an item listed with sets of vessels. Ultimately derived from Proto-Semitic *bvṭ- ( “ a space or vessel; to be swollen, filled up, slow; to mix, agitate, or gurgle; to be hollow or emptied out, to lose or spread out contents ” ) . Further cognates with Persian بادیه ( bādiya  / bâdiye , “ deep earthen wine-jug ” ) , Persian باده ( bāda  / bâde , “ wine ” ) , Ancient Greek βατιάκη ( batiákē ) , Latin batiaca , batioca , batiola .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /baː.tˤi.ja/ 

 Noun
 [ edit ] 

 بَاطِيَة • ( bāṭiya )  f ( plural بَوَاطٍ ( bawāṭin , construct state بَوَاطِي ( bawāṭī ) ) ) 

 an earthen vessel used for storing wine 
 Synonym: نَاجُود ( nājūd ) 
 7th century CE , Sunan an-Nasāʾiyy , 51:128 : فَانْطَلَقَ مَعَ جَارِيَتِهَا فَطَفِقَتْ كُلَّمَا دَخَلَ بَابًا أَغْلَقَتْهُ دُونَهُ حَتَّى أَفْضَى إِلَى ٱمْرَأَةٍ وَضِيئَةٍ عِنْدَهَا غُلَامٌ وَبَاطِيَةُ خَمْرٍ. […] قَالَ فَاسْقِينِي مِنْ هَذَا الْخَمْرِ كَأْسًا فَسَقَتْهُ كَأْسًا. fānṭalaqa maʕa jāriyatihā faṭafiqat kullamā daḵala bāban ʔaḡlaqathu dūnahu ḥattā ʔafḍā ʔilā mraʔatin waḍīʔatin ʕindahā ḡulāmun wabāṭiyatu ḵamrin. […] qāla fāsqīnī min haḏā l-ḵamri kaʔsan fasaqathu kaʔsan. So he set out with her slave girl, and every time he entered a door, she locked it behind him, until he reached a spruce woman who had with her a boy and a vessel of wine. […] He said: ”Pour me of this wine a cup”. So she poured him a cup. 

 Declension
 [ edit ] 

 Declension of noun بَاطِيَة ( bāṭiya )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 بَاطِيَة 
 bāṭiya 

 الْبَاطِيَة 
 al-bāṭiya 

 بَاطِيَة 
 bāṭiyat 

 nominative

 بَاطِيَةٌ 
 bāṭiyatun 

 الْبَاطِيَةُ 
 al-bāṭiyatu 

 بَاطِيَةُ 
 bāṭiyatu 

 accusative

 بَاطِيَةً
```


## [2026-09-05T05:58:47.449Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== berenj ===\"; grep -n \"Etymology 1\\|Etymology 2\\|brass\\|copper\\|Middle Persian\\|rice\" bad8b3940952dbd0.txt | head -40",
 "description": "Wiktionary berenj"
}
```


### [2026-09-05T05:58:47.498Z] TOOL RESULT

```
=== berenj ===
62: Etymology 1 
74: Etymology 2 
133: Etymology 1 
151: Etymology 2 
252: Etymology 1
333: Etymology 2
336: From Classical Persian برنج ( birinj , “ rice ” ) .
343: ( obsolete ) rice 
344: a. 870 , علي بن سهل ربّن الطبري [ ʿalī ibn Sahl Rabbān aṭ-Ṭabarīy ], فردوس الحكمة في الطب [ firdaws al-ḥikma fī aṭ-ṭibb , Ali ibn Sahl Rabban al-Tabari ]‎ [1] , Bayrūt: دار الكتب العلمية , published 2002 , →ISBN , archived from the original on 5 April 2023 , page 326 last line : […] اسفيدباجه ثم يأخذ سبعة مثاقيل برنج ومثله حمص […] its blancmange. Then one takes seven weights of rice and so much of chickpeas. 
487: rice 
502: rice 
523: rice 
553: Etymology 1
556: Inherited from Middle Persian blnc ( /⁠brinǰ⁠/ ) .
603: rice 
613: کرنجبا ( koranj-bâ , “ rice soup ” ) 
652: Etymology 2
655: From Middle Persian [script needed] ( blnc /⁠brinǰ⁠/ ) , 𐫁𐫡𐫏𐫗𐫗𐫃 ( brynng /⁠bring⁠/ , “ bronze, brass ” ) . According to Encyclopedia Iranica, ultimately of onomatopoeic origin, imitative of ringing brass, similar to Proto-Germanic *hringaz ( “ ringing sound ” ) . [ 1 ] 
657: Cognate with Parthian 𐫛𐫓𐫏𐫗𐫝 ( plync /⁠plinǰ⁠/ ) . Compare Old Armenian պղինձ ( płinj ) , Old Georgian პილენძი ( ṗilenʒi , “ copper ” ) , Aghwan 𐕗𐔼𐔾𐔼𐕎𐕕 ( ṗilinʒ , “ bronze ” ) , Laz პრინჯი ( p̌rinci , “ copper ” ) , Udi пӏилиндж ( ṗilinǯ , “ copper ” ) , Classical Syriac ܦܠܙܐ ( plezzā ) , Middle Iranian borrowings.
664: brass 
739: Persian terms derived from Middle Persian 
741: Persian terms inherited from Middle Persian 
765: Requests for native script for Middle Persian terms 
766: Middle Persian terms with redundant script codes
```


## [2026-09-05T05:58:48.512Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== etymonline bronze ===\"; grep -n -i \"bronz\" f63663460a9c2d0c.txt | head -20",
 "description": "Etymonline bronze"
}
```


### [2026-09-05T05:58:48.559Z] TOOL RESULT

```
=== etymonline bronze ===
1:URL: https://www.etymonline.com/word/bronze
4:TITLE: Bronze - Etymology, Origin & Meaning
6:Bronze - Etymology, Origin & Meaning 
21: Origin and history of bronze 
23: bronze (n.) 
25: 1721, "alloy of copper and (usually) a smaller amount of tin," from French bronze , from Italian bronzo , from Medieval Latin bronzium , which is of uncertain origin. Perhaps cognate (via notion of color) with Venetian bronza "glowing coals," or German brunst "fire." Perhaps influenced by Latin Brundisium the Italian town of Brindisi (Pliny writes of aes Brundusinum ). Perhaps ultimately from Persian birinj "copper."
27: In Middle English, the distinction between bronze (copper-tin alloy) and brass (copper-zinc alloy) was not clear, and both were called bras (see brass (n.)). Used historically for bells, cannons, statuary, and fine mechanical works. Also from French are Dutch brons , German Bronze , etc., and ultimately from the Medieval Latin word are Spanish bronce , Russian bronza , Polish bronc , Albanian brunze , etc.
29: A bronze medal has been given to a third-place finisher at least since 1852. The archaeological Bronze Age (1850) falls between the Stone and Iron ages, and is a reference to the principal material for making weapons and ornaments.
32: bronze (v.) 
34: 1640s, "give the color or appearance of bronze to," from French bronzer (16c.) or else from bronze (n.). Figuratively, of feelings, hearts, etc., "to harden like bronze," 1726. The meaning "to make to be brown or bronze in color" (by exposure to the sun, etc.) is from 1792. Related: Bronzed ; bronzing .
37: Entries linking to bronze 
41: "yellow malleable alloy metal, harder than copper," Old English bræs "brass, bronze," originally any alloy of copper, in England usually with tin (this is now called bronze ), later and in modern use an alloy of roughly two parts copper to one part zinc. A mystery word, with no known cognates beyond English. Perhaps akin to French brasser "to brew," because it is an alloy. It also has been compared to Old Swedish brasa "fire," but no sure connection can be made. Yet another theory connects it with Latin ferrum "iron," itself of obscure origin.
43: Words for "brass" in other languages (such as German Messing , Old English mæsling , French laiton , Italian ottone ) also tend to be difficult to explain. As brass was unknown in early antiquity (it was well-known to Strabo, 1c., but not mentioned by Homer), the use of the English word in Bible translations, etc., likely means "bronze." The Romans were the first to deliberately make it.
46: bronzo , 
47: bronze ) came into use to distinguish this 'ancient brass' from the current alloy. [OED]
55: Ancient Greek had khalkos "ore, copper, bronze;" an old IE word for "ore, copper, bronze" is retained in Sanskrit ayah , Latin aes . Latin aes originally was "copper," but this was extended to its alloy with tin (see bronze ), and as this was far more extensively used than pure copper, the word's primary sense shifted to the alloy and a new word evolved for "copper," from the Latin form of the name of the island of Cyprus, where copper was mined (the alchemists associated copper with Venus).
71: *aus- (2) "gold" (source also of Sanskrit ayah "metal," Avestan ayo, Latin aes "brass," Old English ar "brass, copper, bronze...," Gothic aiz "bronze," Old Lithuanian ausas "gold"), which is probably related to root *aus- (1) "to shine."...
75: The sense of the word before it reached English began as "gold leaf prepared for gilding bronze, brass, etc.," then shifted...to "gilded bronze," then to various prepared metallic substances resembling it....
79: Tin, essential in making bronze, was mined in Celtic regions in what is now Spain and southwestern England, and in the early...Roman era the Gallic Celts were masters of bronze metalworking....
83: "greenish encrustation on old bronze," 1748, from French patine (18c.), from Italian patina....pet-ano-, from root *pete- "to spread"), but it is uncertain why, as patina was found on many ancient objects other than bronze...
```


## [2026-09-05T05:59:01.070Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['VFO','PRT','AHD','MON']:\n    v=d.get(k)\n    print(k,'::',(v or {}).get('title'),'|',(v or {}).get('kind'))\n\"; grep -rn \"VFO\" data/verification/sources/*.md data/verification/sources/refs_online.json | head",
 "description": "Check VFO reference"
}
```


### [2026-09-05T05:59:02.561Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/sources/refs_online.json'
(eval):6: no matches found: data/verification/sources/*.md
```


## [2026-09-05T05:59:03.507Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84\" --note \"page 77: Persian پاتیل pot\" ; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/\" --note \"page 77: Moin/Dehkhoda پاتیل\"",
 "description": "Fetch patil sources"
}
```


### [2026-09-05T05:59:07.102Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0af573ddd8850565.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/057e68e9bb3bcd09.txt
```


## [2026-09-05T05:59:10.450Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint('VFO' in d, 'PRT' in d)\nprint(json.dumps(d.get('VFO'),ensure_ascii=False)[:600])\nprint([k for k in d if k.startswith('V')])\n\"",
 "description": "Check VFO key"
}
```


## [2026-09-05T05:59:11.590Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== wikt patil ===\"; sed -n '140,200p' 0af573ddd8850565.txt; echo \"=== abadis patil ===\"; grep -n -i \"پاتیل\" 057e68e9bb3bcd09.txt | head -20",
 "description": "Read patil sources"
}
```


### [2026-09-05T05:59:12.357Z] TOOL RESULT

```
False True
null
['VOP', 'VDQ', 'VGH', 'VIE', 'VSF']
```


### [2026-09-05T05:59:12.411Z] TOOL RESULT

```
=== wikt patil ===
=== abadis patil ===
4:TITLE: پاتیل - معنی در دیکشنری آبادیس
6:پاتیل - معنی در دیکشنری آبادیس 
10: پاتیل
13: مترادف پاتیل : دیگ، سیاه مست
20: پاتیل. ( اِ ) ظرف بزرگ مسین و جز آن که دهانه ٔآن فراختر از شکم است و در آن چغندر و آشهای بزرگ وفرنی و امثال آن پزند. پاتیله. تیان. طنجیر. لوید. و رجوع به پاتیله و پاتله شود. || ( در حمام ) ظرف بزرگ مسین با دهانه فراخ که زیر خزانه گذارند و از بن آن آتش کنند تا آب خزانه گرم شود. تیان.
21:- پاتیل شدن ؛ در تداول عوام ، خفتن و بی خبری بعلت مستی و سکر. 
25: دیگ مسی دهان فراخ که ته آن گرداست، پاتیله هم گویند
37:* پاتیل شدن: (مصدر لازم ) ‹پاتیلی شدن› [عامیانه، مجاز] مستِ مست شدن و از پا درآمدن. 
45: پاتیل یک ظرف بزرگ فلزی ( قابلمه ) برای پختن غذا یا جوشاندن آب روی یک آتش باز است، این ظرف دهانی باز و اغلب دسته ای قوسی شکل دارد. 
46:پاتیل ها در دنیای پیشرفته به عنوان وسیله آشپزی به شدت از مد افتاده اند. یک استفادهٔ متداول در فرهنگ غربی، استفاده از پاتیل به عنوان وسیلهٔ جادوگر است، کلیشه ای که بوسیلهٔ ادبیات داستانی مختلف مانند نمایشنامه مکبث نوشته شکسپیر محبوب شده است. در ادبیات معمولاً جادوگران معجون هایشان را در پاتیل آماده می کنند. در فولکلور ایرلندی، یک پاتیل مکان نگهداری گنج لپرکان ها را لو می دهد. 
47:در برخی از اشکال ویکا، با ترکیب جنبه های اسطوره شناسی سلتی، پاتیل با الهه کریدوِن مرتبط است. اسطوره شناسی ولز هم، از پاتیل هایی صحبت می کند که برای جنگجویان ارتش مفید بودند. 
48:در شاخه دوم مَبی نوگیون در داستان برانون، دختر لیر، دِ پِیر دادنی ( پاتیل تولد دوباره ) پاتیلی جادویی است که می توان جنگجویان مرده را در آن قرار داد تا زنده شوند، فقط آنها قدرت سخن گفتن نخواهند داشت. [ ۱] گمان می رود که این جنگجویان فاقد روح هستند، آن ها می توانند دوباره به میدان نبرد برگردند تا زمانیکه دوباره کشته شوند. در ویکا و برخی از اشکال دیگر سیستم های اعتقادی نئوپاگان یا پاگان پاتیل هنوز در کارهای جادویی مورد استفاده قرار می گیرد. 
49:اغلب پاتیل از چدن ساخته می شود و برای سوزاندن بخور بر روی یک صفحه زغال چوب، برای ساخت نمک سیاه ( مورد استفاده در مراسم تبعید ) ، برای مخلوط کردن گیاهان، یا برای سوزاندن عریضه ها ( کاغذی با کلمات قدرت یا خواسته های نوشته شده در آنها ) استفاده می شود. پاتیل ها نه تنها نماد الهه، بلکه نماد رحم نیز هستند ( چون چیزی را توی خود نگه می دارند ) و بر روی یک محراب نشان دهندهٔ زمین است، چون ابزار کاربردی است. پاتیل ها اغلب در مغازه های عصر جدید یا «متافیزیکال» فروخته می شوند و ممکن است نمادهای قدرت های مختلفی باشند که بر روی آنها نوشته شده است. 
50:جام مقدس ماهیت بریتن گاهی اوقات پاتیل نامیده می شود، گرچه به طور سنتی جام در مورد فنجان دسته دار بیشتر از ظرف بزرگی که کلمهٔ پاتیل برای بیان آن به کار می رود استفاده می شود. ممکن است این از ترکیبی از جام افسانه ای با اسطوره های پیشین سلتیک از پاتیل های جادویی حاصل شده باشد. 
51: wiki: پاتیل 
53: پاتیل (ریخته گری). پاتیل[ ۱] ظرفی است با پوشش نسوز که فلز گداخته از کوره در آن ریخته و به وسیلهٔ آن به قالب ها منتقل می شود. 
54:در ریخته گری پس از آنکه قالب ها کاملاً مستحکم شد و درجه حرارت پیش گرم هم به اندازه لازم رسید نوبت به مرحله بارریزی است. تخلیهٔ مذاب از کوره یا پاتیل در قالب را بارریزی یا مذاب ریزی می نامند. مرسوم ترین روش بارریزی ریختن ثقلی مذاب توسط پاتیل است. گاه نیروی ثقل برای پرکردن قالب کافی نیست و علاوه بر آن از نیروی گریز از مرکز هم استفاده می شود. 
55: wiki: پاتیل (ریخته گری) 
66: دیگ، پاتیل، کوره، تنور، تون حمام و غیره، بوته آزمایش
68: دیگ، پاتیل، کتری بزرگ
```


## [2026-09-05T05:59:20.041Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON پاتیل ==\"; grep -n \"پاتیل\" MON_part1.txt MON_part2.txt | head -10; echo \"== MON باده ==\"; grep -n \"^باده\\|باده:\" MON_part1.txt | head -10; echo \"== MON بادیه ==\"; grep -n \"بادیه:\" MON_part1.txt | head -10; echo \"== BQT پاتیله ==\"; grep -n \"پاتیله\" BQT_v1_pages.txt BQT_alt_v1.txt | head -10",
 "description": "Grep Moin and Borhan for patil/bade/badiye"
}
```


### [2026-09-05T05:59:20.160Z] TOOL RESULT

```
== MON پاتیل ==
MON_part1.txt:27611:پاتیل: 1 (.) دیگ بزرگ مسیء دیگک 
MON_part1.txt:64465:نوعی دیگ و پاتیل. 
MON_part1.txt:81452:و شکر و زعفران می‌آميزند و در پاتیل آن 
MON_part2.txt:32285:پاتیل جوش آورده و آتش را کم کرده و گز 
== MON باده ==
1634:باده‌پیما؛ ساقی. حکاک» نکٌّین‌ساز. آبیار 
20025:باده: (6-)۰2۵2 () نوشابه‌ای که مستی 
20027:باده‌پیما (ی): (مسرم)رهن-.< (ان.) 
20030:باده گسار؛ ۰.. (افا.) شرابخوار» 
24600:باده. بیاله ِ ار 
35724:باده» قدح شرانخواری. (مج.) شراب» باده. 
36633:باده در سر آورد. (گیا.) درخت تار. 
51341:باده بیماء باده‌دهنده. 
57381:باده‌فر وش. (تص.) بير کامل» مرشد و اصل. 
82833:باده خورد؟ نوش ‌خور. شراب‌خوار» 
== MON بادیه ==
20048:بادیه: (-)۰رن۵ة۱ زع. بادیة] (.) صحراه 
== BQT پاتیله ==
BQT_alt_v1.txt:42023:و ن یکی زد بسنیپااونن است کهبربی بی | پاتیله است وآن مطلق دنکه باشدعموماً ودنگ
```


## [2026-09-05T05:59:25.416Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20020,20060p' MON_part1.txt; echo \"=== patil ===\"; sed -n '27605,27620p' MON_part1.txt",
 "description": "Print Moin entries"
}
```


### [2026-09-05T05:59:25.483Z] TOOL RESULT

```
محور عمودی می‌چرخد و آن را برای تعیین 
جهت و سمت باد در محل مر تفعی نصب 
نمایند. 

باده: (6-)۰2۵2 () نوشابه‌ای که مستی 
آورد» نوشیدنی مسکرء شراب» می. 
باده‌پیما (ی): (مسرم)رهن-.< (ان.) 
شرابخوار» میخوار. 

باده گسار؛ ۰.. (افا.) شرابخوار» 
و زر 

بادی: -۰20 (ص‌نسه.) منسوب به باد: آس 
بادی. (نج.) برج‌های منسوب به باد» جوزاء 
دلو» میزان. (مس.) آلتی موسیقی که با باد 
(فوت) به صدا در آید. 

بادی: 2۵" [ع. بادیْ] (افاء بدء). آغاز 
کننده» شروع کننده. آفر یننده. نو بیرون 
آورنده: )۱( آغاز» شروع. 

بادی: 020 [ع.] (افا. بدو) بیدا شونده» 
آشکار شو نده. 

بادیان: مورزفةه (- بادیانه - وادبان] (ا.) 
(گیا.) گیاهی از تبرث چتریان که دو ساله یا پایا 
است» رازیانه و آن دارای انواع است. 
بادیه: (-)۰رن۵ة۱ زع. بادیة] (.) صحراه 
بیابان؛ ج. نوادی. 

بادل: اعتةه [ع.] (افا. بذل) بذل کننده 
بخشش کننده؛ بحشند ه. 

بار: ۲ آنچه که بر دوش و بشت انسان با 


چارپا حمل شود؛ حمل. (پز.) دگرگونی 


زبان به سبب پری معده. غشی که در سیم و 
=== patil ===
توغ را حرکت دهند زير و اطراف توغ را 
«پاتوغ» گویند. 

پاتولوزی: 0200-021 (امر.) (یز.) مبحت 
علل و اعراض امراض د(کم 

پاتیل: 1 (.) دیگ بزرگ مسیء دیگک 
خران 4 حسمام؛ تسان» دیگک دهن فراخ 
حلوایزی. 

پاجامه: : (0-)02-12002 (امر.) زیر جامه» 
تنبان, شلوار» باشامه. . ضح. - بیژاما در 
انگلیسی از این کلمه ماخ رات 
پاجوش: 0-184 (امر.) ( گیا.) شاخة باریکی 
که در بای بعض درختان از قمبل چنار» 
تبر بزی» تمشکک» آلو گوجه» فندق و غبره
```


## [2026-09-05T05:59:35.621Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON باطیه ==\"; grep -n \"باطیه\" MON_part1.txt MON_part2.txt | head; echo \"== SKT bronze ==\"; grep -n -i \"bronze\" SKT.txt | head -5; echo \"== FSD bronze ==\"; grep -n -i \"^bronze\\|bronze,\" FSD_vol1.txt | head -5; echo \"== WEB bronze ==\"; grep -n -i \"bronze\" WEB_vol1.txt | head -5",
 "description": "Grep more sources for bronze/batiye"
}
```


### [2026-09-05T05:59:35.717Z] TOOL RESULT

```
== MON باطیه ==
MON_part1.txt:20664:باطیه فررهنگ فارسی معیر ۲۳۵ 
MON_part1.txt:20671:باطیه: دون (ع. - باطتةء ف. بادیه) (.) 
MON_part1.txt:88993:آن مستند به ظنون اجتهادیه و استنباطیه باشد. 
MON_part1.txt:91613:بسته و در وقت چلو دم کردن باطیه را ته 
== SKT bronze ==
2332:Perhaps  related  to  G.  brudeJn,  br^dtM,  to bubble  (whence  to  give  off  steam,  coofose) ; a.  brodel,  broifem,  vapour,  allied  to  E. Breath  (Schclcr).  Cf.  F.  btvuUhrJ,  a mist,  fog.  %  We  also  find  >N.brxKh^  tumult, broiheii.  a  tempest ;  Gael.  brei,^hUadh,  titf- moil.  broigiuk,  noise  (pcrhft[>.s  unrelated). Broker.  <E.)  SceBrooku)- Bronchial.  (Gk.)  Gk.  Bfiyx****  neol. pi.,  the  ramifications  of  the  windpipe.— Gk.  ^p6yxot,  ihe  windpipe  ;  cf.  fipnyx*^-  ' gill.  Allied  to  Gk.  a^x'"*'  ^^  ^<^^-  ^*'* brvrKk't'tis;  (rom  0p6yxof. Bronze.  (F.-ltal.-Teat)  SeeBrown. Brooch.  (F.-L.)  Named  from  the  pin which  fastens  iL  M.  E.  brockr,  a  pin,  yejL brooch.  —  F.  brocht,  a  spit,  point.  —Low  L bnvfa,  a  pointed  stick.  — L.^/vrinttj,  ashaip tooth,  pomt  Cf.  Gael.  bn>ff,  to  goad.^r^, on  awl ;  \V.  procio^  to  stab.
23579:French  from   ItaHam  frpm ba^tcllc,    bronze,    cscarpmeat    ^1 sujix),  scaramouch.  scu\\  lir^ftc;
== FSD bronze ==
12369:II.  t.  To  enter  into  combination;  form  an  alloy.  I   < F.  aloyer ,   <   OF.  alter,  <   alligo;  see  alligation'.] al-Ioy',  1   e-lei'  or  al'ei;  2   a-Ioy'  or  Sl'Sy, n.  1.  A   homo- geneous compound  or  mixture  of  two  or  more  metals,  as brass,  formed  by  the  fusion  of  copper  and  zinc,  or bronze,  consisting  of  copper  and  tin:  commonly  pro- duced by  fusing  together  the  constituent  metals.  See
12371:The  following  are  some  of  the  most  important  alloys: fl)  Aluminum  combines  with  copper  to  form  aluminum bronze,  used  In  machinery,  and  with  zinc  to  form  aluminum zinc,  used  in  parts  of  chemical  apparatus  requiring  strength and  lightness.  (2)  Antimony  alloys  with  lead,  potassium, sodium,  and  tin.  With  lead  and  tin  it  forms  typometal, with  tin  muslc^mctal,  and  with  tin  and  other  metals  plate pewter,  Britannia  metal,  and  queen’ s*metal,  the  last-named used  in  jewelry.  (3)  Arsenic  is  used  in  lead  to  produce metal  for  shot.  With  copper  It  yields  white  copper  and  tom- bac, used  for  Imitation  jewelry.  (4)  Bismuth  alloys  chiefly with  lead,  tin,  and  type-metal,  forming  fusible  alloy,  used for  cliches,  and  pewterers'  soft  solder.  (5)  Cadmium  com- bines with  mercury  to  form  an  amalgam  used  to  fill  teeth, with  gold  and  silver  to  form  an  alloy  used  by  jewelers,  and with  tin,  lead,  and  bismuth  to  form  Wood’s  fusible  alloy .   (6) Chromium  alloys  with  Iron  to  form  ferro*chrome,  and  also  with tin  and  copper.  (7)  Copper  combines  with  zinc  to  form  brass, with  tin  to  form  bronze,  gurvmetal,  and  bell-metal,  and  with lead  to  Jorm  pot-metal,  used  for  faucets  and  domestic  uten- sils. Alloys  of  these  four  metals  in  varying  proportions  also exist.  (8)  Gold  alloys  with  copper,  silver,  manganese,  co- balt, nickel,  antimony,  tin,  zinc,  bismuth,  lead,  the  platinum metals,  arsenic,  tellurium,  and  mercury.  With  copper  It forms  a   reddish  gold,  and  with  sliver  a   lighter-colored  alloy called  jewelers’  gold.  Gold  coin  is  an  alloy  of  gold  and  cop- per, generally  with  silver  also.  (9)  Iron  alloys  with  copper, zinc  (forming  Alch’s  metal,  used  for  casting  cannon),  tin, titanium,  manganese  (forming  ferromanganese,  used  in  the Bessemer  steel  process),  tungsten,  nickel  ( meteorite ),  cobalt, gold,  and  platinum.  (10)  Lead  combines  with  antimony and  tin  to  form  type-metal,  with  arsenic  for  shot,  with  tin to  make  pewter  and  solder,  with  bismuth  to  form  fusible  alloy. (11)  Manganese  is  used  with  Iron  to  form  steel,  as  spiegelel- sen.  It  Is  used  in  the  Bessemer  process  to  deoxidize  the metal.  (12)  Mercury  forms  with  tin  an  amalgam  for  sil- vering mirrors,  with  gold  and  tin  one  for  gliding,  with  tin, gold,  and  silver  one  Tised  for  filling  by  dentists,  with  sodium one  used  for  metallurgical  purposes,  and  with  zinc  one used  for  coating  the  rubbers  of  electric  machines.  (13) Nickel  alloys  with  copper  and  zinc  to  form  white  metals used  largely  in  place  of  silver  and  called  albata,  Brit- ish plate,  clectrum,  German  silver,  pal-fang,  tutenag,  white copper,  etc.  (14)  Palladium  yields  with  silver  and  copper tough  alloys  used  .   in  the  making  of  hard  Instruments. (15)  Platinum  alloys  with  gold,  and  with  the  various platinum  metals  with  which  it  Is  found  In  nature.  (16) Phodlum  combines  with  platinum  metals  and  with  steel to  form  a   fusible  alloy.  (17)  Silver  alloys  with  copper,  as  In coin  and  solder,  and  with  tin,  mercury,  and  other  metals. (18)  Tin  combines  with  lead  to  form  pewter  and  ordinary plumbers*  or  tinsmiths'  solder,  with  copper  and  antimony to  form  Babbitt  metal.  (19)  Zinc  alloys  with  copper  to  form brass,  and  also  with  tin  and  lead  as  In  Burton’s  alloy,  used for  plowshares.
25570:—   art  and  part  (Scots  Lute),  complicity  in  Instigating crime  (nr/),  and  part  in  committing  it.—  art  bronze,  a   com- position of  tin  and  copper  used  by  sculptors.—  art  nouveau IF. |.  lit.,  new  art:  applied  to  a   school  of  artists  who  have abandoned  the  old  order  and  conventions,  especially  of decorative  art.—  art’*pump"kln,  n.  Pec  balsam-tear.— art  square,  a   square  rug  of  Ingrain  carpet.— art  union,  a society  formed  for  the  encouragement  of  the  arts,  especially of  design.— black  art,  necromancy:  magic.  See  nt c ro- mance.— faculty  of  arts  (as  distinguished  from  fac- ulty of  late,  faculty  of  medicine,  etc.),  originally,  the  body  of Instructors  who  had  charge  of  the  earlier  studies  of  the course;  now.  those  in  charge  of  the  academical  or  collegiate course  proper.— landscape  art,  the  art  of  improving  the natural  beauty  of  scenery.—  liberal  arts,  the  higher branches  of  learning:  so  called  because  among  the  Romans only  freemen  were  allowed  to  pursue  them.  In  medieval  uni- versities they  Included  the  trivlum  and  the  quadrivium.  See Tritium  and  quadrivium.  In  modern  times  they  embrace the  languages,  history,  science,  philosophy,  etc.—  the  art preservative  of  all  arts,  printing. — the  manly  art,  or the  art  of  seir^defense,  boxing;  In  England,  the  noble art.
36175:bronze  agra  In  the  Brills trtsles  and  generally  throughout  Bartthez',  x   bar'tc':  2   bSrte',  Paul  Joseph  (*Vnl<3A-  “[<  qV.  bratTf  +   ^ron,  SSI  ]   °   y   f
38505:—   absolute  bearing,  see  relative  bearing.—  bear'ing* bln"na-cle,  n.  Naui.  A   binnacle  on  the  poop  for  con- venience when  taking  bearings.—  b.*b!ock,  n.  Same  as bearing,  7   (1).— b.*c!oth,  n.  A   covering  thrown  over  a child  when  carried  to  church  for  baptism,  bear'cloth”*.— b.*door,  n.  [Eng.]  A   ventilating  door  in  a   coal-mine.— b.*dowu,  n.  Compression  of  the  abdominal  viscera  by  con- traction of  the  muscles  of  the  wall,  as  in  parturition.— b.» feeler,  n.  Mech.  A   device  for  indicating  when  a   Journal or  bearing  is  undesirably  warm  by  friction.— bimetal,  n. Mech.  Brass,  bronze,  or  other  metal,  suitable  for  bearings.
== WEB bronze ==
3761:Bronze Age. ade Ae-ge/ri-in, E.ge/ri-An, a. of or pertaining to
3786:of bronze.]
4114:3. in decorative art, any small ornament added or attached, as the dragons on Japa- nese bronzes.
5227:tion. Al-bi-gen’sian (-shun), a. pertaining to the Albigenses. Al-bi-Sen/sian (-shun), n. any member of the Albigenses. al/bin, n. [L. albus, white.] a variety of opaque white apophyllite found in Bohemia. al-bi/ness, 7. a female albino. al-bin/ic, a. of or having albinism. F al’/bi-nism, 7. the state of being an albino; leukopathy; albinoism. xe ate al-bi-nis’tic, a. of or pertaining to albinism. al-bi’/nd, n.; pl. al-bi/nos, [Port. albino, from L. albus, white.) i 1. a person having, through deficiency of coloring matter, abnormally white skin an hair and pink eyes. : 2. any plant or animal having the same abnormal lack of color. ; s al-bi/n6-ism, n. the state of being an albino. al-bi-not/ic, a. albinistic. = Al’/bi-dn, n. [L., from Gaul; understood as if from L. albus, white: the cliffs of southern England are white.] England: used in poetry. al’/bite, n. (L. albus, white, and -ile.] a sodium- bearing, whitish mineral of the feldspar group. It is a constituent of many varieties of granitic rocks. aoe Al-biz/zi-a (-bit/si-), n. [L. from It. Albizzt, a noble family in Tuscany.] a genus of plants of the Mimosez family, allied to the Acacia. al’/bo-lith, al’/bo-lite, 7. [L. albus, white, an Gr. lithos, stone.] artificial stone or cement composed of magnesia and silica. It is used as a fireproofing and for plastic decorations in buildings. AVbo-rak, n. [Ar. al-burag, from baraga, to shine.] the fabled white mule on whic Mo- hammed is said to have journeyed to heaven. al’/bronze, 7. an alloy of copper and aluminum. _al-bu-gin/é-a, n. [L., f., as if from albugineus,
18503:Berlin iron; a fusible kind of soft iron, large- ly used in making delicate or ornamental ar- ticles, as jewelry and fine smooth castings, which are sometimes stained or lacquered in imitation of bronze.
```


## [2026-09-05T05:59:43.170Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20660,20680p' MON_part1.txt; echo \"== FSD bronze entry ==\"; grep -n \"bronze,  n\\|bronz'\" FSD_vol1.txt | head -5",
 "description": "Moin batiye and FSD bronze"
}
```


### [2026-09-05T05:59:43.242Z] TOOL RESULT

```
باطن: ۱3160 [ع.] (۰) بنهان» درون چبری» 


باطیه فررهنگ فارسی معیر ۲۳۵ 


اندرون؛ ج. بواطن. ابطنه. حقیقت» اصل. 
صمیر » دل. (اح.) نامی از نام‌های خدا. در 
باطن: باط 

باطیه: دون (ع. - باطتةء ف. بادیه) (.) 
ظرف سفالینی که در آن شراب نگاه دارند» 
ابریقی که از آن در بیاله‌های کو چک شراب 
ریرند. 

باع: 8 [ع. قس. باز] (.) واحد طول, از 
سر انگشت دست راست تا سرانگشت دست 
چپ آنگاه که دست را افقی به طرفین باز 
باعث: »۱5 [ع.] (افا.) برانگیزنده» بعث 
کننده. یکی از نام‌های خدا. (.) سبب» 
== FSD bronze entry ==
50531:Bronx,  1   brepks;  2   brOpks,  n.  1.  A   river  in  S.  E.  New  York, flowing  through  Bronx  county  to  East  River.  2.  A   county of  S.  E.  New  York;  41  sq.  m.:  borough  of  New  York  city, bronze, )   1   bronz;  2   brSnz.  [bronzed,  broxzd8;  bronz'- bronzp,  J   ing.]  r.  1. 1.  1.  To  give  the  color  or  appearance of  bronze  to  by  a   mechanical  or  chemical  process;  as, the  cast  was  bronzed.  2.  To  give  a   similar  color  to  by natural  means,  as  by  exposure  to  the  sun;  brown;  tan; as,  a   bronzed  Arab.
50534:II.  t.  To  become  like  bronze,  as  in  color;  be  sun- burned.—bronzed  skln<dlsease  (Pathol.'),  Addison’s  dis- ease.— bronz'er,  n.  One  who  or  that  which  bronzes; Bpeclf .,  a   bronzlng-machine,  or  brush  for  applying  bronze- powder.
50535:bronze,  n.  1.  A   reddish-brown  alloy  of  copper  and  tin, sometimes  containing  small  proportions  of  other  metals. Bronze,  which  was  known  at  a   very  early  period,  is  an  im-
50594:bronz'en,  a.  IRare.]  Made   
50595:of  or  like  bronze.—  bronz'I- fy,  cl.  To  make  into  bronze;  "
```


## [2026-09-05T05:59:51.102Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50535,50545p' FSD_vol1.txt; echo \"=== KLN page markers near 5712 ===\"; awk 'NR>=5600 && NR<=5760 && /^ *[0-9]{2,4} *$/ {print NR\": \"$0}' KLN_1966.txt; echo \"---\"; sed -n '5700,5716p' KLN_1966.txt",
 "description": "FSD bronze etymology and Klein page"
}
```


### [2026-09-05T05:59:52.656Z] TOOL RESULT

```
bronze,  n.  1.  A   reddish-brown  alloy  of  copper  and  tin, sometimes  containing  small  proportions  of  other  metals. Bronze,  which  was  known  at  a   very  early  period,  is  an  im-
portant material  used  for  making  weapons,  coins,  domestic  hrnnde'iTP"*  «   a
utensils,  bells,  cannon,  and  statuary,  and  for  many  other  hm  l 'hniA??  i   a   j   j
...rin.im,    Drooa  ct.  i   Drucl  ar;  2   brood  er,  n.  1.  A   covered  and
warmed  receptacle,  usually  with  an  outside  run,  for
purposes.  Several  varieties  of  bronze  derive  their  names
from  a   constituent  alloy;  as,  bismuth  (bronze,  carbon  *b.t  ...  ...  ,   ,   -   -   ,   -
cobalt»b.,  manganese«b.,  nlckebb.,  phosphorus^b.,  protecting  chicks  reared  without  a   hen.  2.  One  who slIIcon*b.,  etc.  broods  over  things  in  thought.  [brooder.
2.  An  artistic  production  in  bronze,  as  a   statue  or  statu-  brood 'ered,  1   brud'erd;  2   brood'erd,  a.  Reared  in  a ette.  3.  One  of  various  metallic  powders  or  pigments  brood'l-ness,  1   brfld'i-nes;  2   brood'i-ngs,  n.  The  state  or more  or  less  resembling  bronze,  used  in  decorative  work;  .   common  of  being,  or  the  inclination  to  be,  broody, as,  gold  bronze,  silver  bronze,  blue  bronze.  4.  The  color  urood  lei>  1   brfld'let;  2   brobd'Ifit,  n.  IRare.l  A   nestling;  a of  bronze.  5.  Impudence;  effrontery;  brass.  [F.,  <   ik'L  ,   fc,
brolnP  braSS'  <   br0"'n'  <   0HG‘  b™'  5j  l   “
0t  dmerent  2hbr65d>P“-  I^lbedtobn.od.or
=== KLN page markers near 5712 ===
---
bromism,  n.,  bromine  poisoning  ( med .)  —  See bromine  and  -ism.
bromite,  n.,  salt  of  bromous  acid  (chem.)  —  See bromine  and  chem.  suff.  -ite. bromize,  tr.  v.,  to  treat  with  bromine  or  a  bro¬ mide.  —  See  bromine  and  -ize.
Derivatives:  bromiz-ation,  n.,  bromiz-er,  n. bromo-  before  a  vowel  brom-,  combining  form meaning  ‘containing  bromine’.  —  Gk.  Ppojpo-, [jpo)u-,  fr.  (ipoipop,  more  exactly  fapo;xoc;,  ‘noi¬ some  smell’,  identical  with  ppopiop,  ‘any  loud noise’,  which  is  rel.  to  |Jpip.Etv,  ‘to  clash,  roar’, Ppov-rf)  (for  *ppop.-Ta),  ‘thunder’,  fr.  *brem-,  a variant  of  I.-E.  base  *bhrem-,  whence  L.  fre- mere,  ‘to  roar,  resound,  murmer,  W.  brefu,  ‘to roar’,  OHG.  breman,  MHG.  bremen,  MHG.,  G. brummen,  'to  growl,  buzz’,  OE.  brimsa,  OHG. bremo,  brimissa,  G.  Breme,  Bremse,  ‘horsefly,
203
gadfly’,  OI.  bhramarah,‘bee\  Cp.  Brontes,  Bron¬ tosaurus.  Cp.  also  fremitus.
Bromus,  n.,  a  genus  of  grasses  (bot.)  —  ModL., fr.  L.  bromos,  fr.  Gk.  ppop.04,  ‘wild  oats’,  which is  prob.  related  to  [3polp.a,  ‘food’,  fhppwiTXEiv.'to eat,  eat  up’,  flops,  ‘food’.  See  broma  and  cp. brome.
bronchia,  n.  pi.,  the  bronchial  tubes  (anat.)  — Late  L.  bronchia,  gen.  -drum,  fr.  Gk.  Ppoyyia, fr.  PpoYX°S>  ‘windpipe’.  See  bronchus, bronchiole,  n.,  a  minute  bronchial  tube  (anat.)  — Medical  L.  bronchiola,  a  diminutive  coined  by E.  Schultz  fr.  L.  bronchia  (pi.),  ‘the  bronchial tubes’;  see  bronchia.  Cp.  Joseph  Hyrtl,  Ono- matologia  anatomica,  p.  557- Derivative:  bronchiol-ar,  adj. bronchiolitis,  n.,  inflammation  of  the  bronchioles (med.)  —  Medical  L.  formed  fr.  bronchiola  with suff.  -itis.  See  prec.  word, bronchitis,  n. ,  inflammation  of  the  bronchial  tubes (med.)  — -  Medical  L.,  coined  by  Charles  Bed- ham  in  1808  fr.  bronchus  and  suff.  -itis;  intro¬ duced  into  medicine  by  P.  Frank  in  his  Inter- pretationes  Clinicae  in  1812. broncho-,  before  a  vowel  bronch-,  combining  form denoting  relation  to  the  bronchi.  —  Gk.  |3poyxo-, Pp °YX.->  fr-  Pp°TX°?>  ‘windpipe’.  See  next  word, bronchus,  n.,  each  of  the  two  forked  branches  of the  windpipe.  —  Medical  L.,  fr.  Gk.  ppoyxo?, ‘windpipe’,  which  is  prob.  rel.  to  (ipoyhoc, ‘throat’,  (aor.),  ‘he  swallowed  up’,
ppayxtov,  ‘gill’,  and  cogn.  with  OIr.  bragae, ‘neck’,  W.  breuant,  ‘throat,  gullet’,  Lith.  gur- klys,  ‘crop,  maw’,  ME.  crawe,  ‘craw’.  See  craw and  cp.  branchia.  The  above  words  prob.  de¬ rive  fr.  I.-E.  base  *gu'rSgh-,  a  -^-enlargement of  base  *gwer-,  ‘to  devour’,  whence  Gk.  Pupa, ‘food’,  Pp&pia,  ‘food’,  L.  vorare.  See  voracious and  cp.  words  there  referred  to.
Derivatives:  bronchi-al,  adj.,  bronchi-al-ly,  adv. bronco,  n.,  a  rough  horse  of  Western  North  Ame¬ rica.  —  Sp.  bronco,  ‘rough’,  fr.  VL.  *bruncus, ‘block,  log,  lump’,  which  seems  to  be  a  blend of  L.  truncus,  ‘trunk  of  a  tree’,  and  broccus, ‘projecting’.  See  trunk  and  broach.
Brontes,  n.,  one  of  the  Cyclopes  (Greek  mythol.) —  L.,  fr.  Gk.  Bp6vTr,p,  fr.  (Jpovrr;,  ‘thunder’. See  bronto-.
bronto-,  before  a  vowel  bront-,  combining  form meaning  ‘thunder’.  —  Gk.  fipovTU-,  ppovr-,  fr. Ppov-rvj  (for  *flpoa--:a),  ‘thunder’,  which  is  rel. to  Ppopoc,  ‘any  loud  noise’,  Ppspeiv,  ‘to  clash, roar’.  See  bromo-  and  cp.  Brontes  and  the  first element  in  Brontosaurus.
Brontosaurus,  n.,  a  genus  of  American  dinosaurs ( paleontol .)  —  ModL.,  coined  fr.  Gk.  ppovrij, ‘thunder’,  and  aaupo?,  ‘lizard’.  See  bronto-  and saurian.
bronze,  n.  —  F.,  fr.  It.  bronzo,  bronzino,  ult.  fr, Persian  birinj.
Derivatives :  bronze,  tr.  and  intr.  v.  (cp.  F.  bron- zer),  bronze,  adj.,  bronz-ify,  tr.  v.  (rare),  bronz¬
ing,  n.,  bronz-ite,  n.  (mineral.),  bronz-y,  adj. brooch,  n.  —  A  var.  of  broach.
Derivative:  brooch,  tr.  v.
brood,  n.  —  ME.  brod,  fr.  OE.  brod,  lit.  ‘that which  is  hatched  out  by  warmth’,  rel.  to  Du. broed,  MHG.  bruot,  G.  Brut,  ‘brood’,  and  to MLG.  brdien,  MDu.  broeyen,  MHG.  briieyen , briien,  G.  briihen,  ‘to  scald’.  See  brew  and  cp. words  there  referred  to.
```


## [2026-09-05T06:00:07.811Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT batiake ==\"; grep -n -i \"batiak\\|batiac\" KNT.txt TLM.txt SPG_keilinschriften1881.txt 2>/dev/null | head; echo \"== LEW/LAT batiola ==\"; grep -n -i \"batiola\\|batioca\\|batiaca\" LEW_1910.txt LAT.txt | head; echo \"== NYB batak ==\"; grep -n -i \"b\\[?ʾ\\]tk\\|bātak\\|badhag\\|bātag\" NYB_vol2_glossary.txt | head; echo \"== NYB wine ==\"; grep -n \"wine\" NYB_vol2_glossary.txt | head -5; echo \"== LEW bronzium ==\"; grep -n -i \"bronz\" LEW_1910.txt LAT.txt | head",
 "description": "Grep Kent, Walde-Hofmann, Nyberg"
}
```


### [2026-09-05T06:00:07.918Z] TOOL RESULT

```
== KNT batiake ==
== LEW/LAT batiola ==
LAT.txt:7032:batioca, -ae f.: coape X vin. Eaprant a une forae dialectale (Ta¬
LAT.txt:7034:d'Arn. On troave aassi batiola, de aene sens (Pl. Colax frg. 1).
== NYB batak ==
== NYB wine ==
107:HML?: HAMRA wine
1313:dórak [dwlk'] a pail, a bucket 53°. — Arab. lw. dauraq ‘a water-pot with handles’; NP daurah ‘a wine-measure’.
1947:2has [KZY] wine: x%aštom hac x“arisnan, ~ ménóyàn yazdān: ~ hān i martdydzarm rovan the most delicious of dishes (or, beverages), to wit: the wine of the heavenly gods — “wine”: that is the mid- spring ghee 7418-14 (ravan = rögn, g. v.). — KZŠPrs l. 25 hs = Prth 1. 20 HMR; ibd. Prth 1. 24 mdydr = madē-dār, Prs 1. 30 [hs]d"ly = has-därY (the restoration almost certain) ‘butler’; hence it follows that mad was the NW w., has the SW
1950:w. for ‘wine’. V. further s.v. mad. — The ideogr. is borrowed from the homo- nym ‘thas. — Neriosengh had no inkling either of thas or *has; in 7413-14 he omitted the first KZY and rendered the second by kač, translating it in Skr šīghram ‘quickly’. — V. Nyberg, Henning Vol. op. 345.
2228:-kart [-krt'] -gart [.glt'] -fold: cahär- kart, haft[7]-gart fourfold, sevenfold in- tertwined 20%, 12027, — Probably quite simply from kartan, and at all events influenced by it; or from gart- ‘to turn, to twist’ (v. gartišn)?
== LEW bronzium ==
LAT.txt:1800:aes (anc. ais), aeris n.: bronze. A. factum "bronze travaille" et a.
LAT.txt:1801:infectum "quod in massis est"; a. graue "bronze au poids", premibre
LAT.txt:1803:"bronze estampe". - Ancien, usuel. - Specialise bientot dans le sens
LAT.txt:1808:petite monnaie (tardif). Aussi le sens de "bronze" a~t~il finalement
LAT.txt:1828:Autres deriv 6 s: aeratus: bronze, aerosus " 7 ioXuxaAxoc", aerarius
LAT.txt:1829:"concernant le bronze, ou la monnaie, le tresor"; et peut-etre aerdnis"i
LAT.txt:1846:le bronze"; cf. 1’expression juridique per aes et libram expendere
LAT.txt:1850:Ce nom indo-europeen du "cuivre" ou du "bronze" est aussi conserve
LAT.txt:4984:aspect, tandis que le nom du "cuiyre" (et du "bronze"), lat. aes , etc.,
LAT.txt:5397:L'as etait d'abord une plaque de bronze rectangulaire et non estam-
```


## [2026-09-05T06:00:12.581Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7025,7042p' LAT.txt",
 "description": "Ernout-Meillet batioca"
}
```


### [2026-09-05T06:00:12.636Z] TOOL RESULT

```
De bataclare d6rive batdcldtid, Gloss.Saloa. BatSre, bataculare, for-
aations expressives, ont 61 iaine oscXtdre qai est trfes pea repr6sent6,
et sons des foraes alterces, dans les langaes roaanes.
batla, -ae f.: noa de poisson dans Plin.(nne raie?), d6riv6 sans
doute de batis,-is eapront aa gr. f&XTkC.
batillua: -r.uatillum. Mais les foraes roaanes reaontent X batillum,
*batlle M.L.993, peut-etre *batulus 997.
batioca, -ae f.: coape X vin. Eaprant a une forae dialectale (Ta¬
rente, Heraclee) correspondant a ion.-att. paTtOOtq. Dn ex. de Pl. et an
d'Arn. On troave aassi batiola, de aene sens (Pl. Colax frg. 1).
battuo, -is, -ere (batto attest6 4 partir de Fronton): battre;
qaelquefois avec le sens de futuo, Cic. Faa. 9,33,4. Hot rare dans les
textes, aais dejX dans Piante, sans doate popalaire. Panroaan; gall.
bathu "battre aonnaie".
De IX: battualia (batta-J adj. n.pl.(cf. Charis. GLK I 33 , 35 : neutra
semper pluralia ... battualia) devena f£ainin; battudtor. Cf. anssi
battuaculun. M.L.994-996; abattere Lex Salica 41 add. 1, M.L.11;
debattuere (sensa obsceno, Petr.), conbattuere M.L.3073. Irl.betlim
```


## [2026-09-05T06:00:24.126Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/77.jpg 2>/dev/null; pdftoppm -f 77 -l 77 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg77\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render PDF page 77"
}
```


### [2026-09-05T06:00:26.316Z] TOOL RESULT

```
site/pages/77.jpg
total 7720
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:00 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
```


## [2026-09-05T06:00:29.482Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg77.png"
}
```


### [2026-09-05T06:00:29.912Z] TOOL RESULT

```

```


## [2026-09-05T06:00:29.910Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:00:47.799Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:00:47.841Z] TOOL RESULT

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


## [2026-09-05T06:00:55.833Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY باده/برنج ==\"; grep -n \"باده\\|برنج\" incoming/ARY/ARY_pages.txt | head -20; echo \"== HUB brinj/badye ==\"; grep -n -i \"brinj\\|birinj\\|batiak\" HUB.txt | head -10",
 "description": "Grep Aryanpur and Hubschmann"
}
```


### [2026-09-05T06:00:55.910Z] TOOL RESULT

```
== ARY باده/برنج ==
== HUB brinj/badye ==
884:208. Die meisten iran. Formen fiir birinj = gurinj 'Reis*
891:ihr stimmt kurd. pirinjok = birinj *bronze' (Justi-
893:') Vullers giebt biranj neben birinj an, aber auoh die Lehn-
894:worter zeugen fiir birinj.— 28 —
922:*) Arm. plinj : np. birinj — arm. hrinj 'Reis' : np. birinjf.
5568:vraj 'schreiten, gehn ; birinj = gurinj (Muwaffaq p. 6,
5774:= n^.birinj (siehe § 50), das bei Moses, Geogr. ed. Soukry
6159:birinj — gurinj *Reis* aus *virinj = *vrinjii' und bei gurazldan
6191:birinj *Kupfer = arm. plinj, s. oben p. 27 — 28. Das von
8271:Yaismav.) = np. birinjf, gurinj^), afgh. vrize, skr. vrihi^
```


## [2026-09-05T06:00:58.628Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '880,930p' HUB.txt; echo \"=== 6185 ===\"; sed -n '6185,6200p' HUB.txt",
 "description": "Hübschmann birinj entry"
}
```


### [2026-09-05T06:00:58.677Z] TOOL RESULT

```
Etymologie rich tig, falls gustuvan aus kuStuvan *Wei-
chen-schiitzer' entstanden ware. Arm. kstapanak stimmt
lautlich gut dazu, aber nicht in der Bedeutung, da es
das ntpids^iav der Septuag. wiedergiebt.
208. Die meisten iran. Formen fiir birinj = gurinj 'Reis*
haben i-Vokal,*) daher ap. *vrinji-^ iranisch *vrinji',
^vriSi-? (afgh. mi^ pi. fem., vri^a 'Keiskorn, vgl.
auch skr. vrthi-) anzusetzen.
2ogbi8. jfp lyipifij *Kupfer fMessing' nach Rosen, Neup.
Sprachfiihrer p. 35) ist nach Vullers die (jungere)
Nebenform zu piring, die Horn nicht erwahnt. Zu
ihr stimmt kurd. pirinjok = birinj *bronze' (Justi-
^) Dazu phi. kuataktar 'ftussere* ZDMG. 43, 37.
') Vullers giebt biranj neben birinj an, aber auoh die Lehn-
worter zeugen fiir birinj.— 28 —
Jaba Wb.) und arm. plinj^) *Kiipfer, Kiipfergeld, Munze,
Erz, Messing (5. Jhd.). Wohl Fremdwort im Iranischen.
209. Np. barnl Vas parvuin (unbelegt^) ist natiirlich nicht
= zd. urunya (phi. myazdddn vgl. Darmesteter,
le Zend-Avesta II, 215).
210. Np. harvdr =^ zd. *upairivara' (nicht *upairivarana-,
siehe Horn p. 197, Anm. 2), vgl. zd. fravdra-^ pairivCLra-
*Schutzwehr (skr. parivara- *Decke*) und arm. patuar,
Siehe oben Nr. 161 und WZKM. 8, 97. Die Neben-
form varvara a throne, open gallery, balcony* JRAS.
1894, 491.
212. Np. burtdan, burridan 'schneiden hat im Praesens
buram, burram^) (letzteres z. B. Fird. I, 443, Z. 5),
das nach den Lautgesetzen auf ein idg. ^bhrndmi
zuriickgehen muss, das selbst wieder aus Hher-ne-di-mi
(Wrzl, bherai, schwach bhrt) entstanden ist. Das
Particip pass, dazu lautete idg. bhrt'to-s = ap. *brita,
das im Neup. zu *birid werden sollte, durch Anlehnung
an das Praesens^) aber zu burtd wurde. Danach der
Infinitiv burldan oder burridan^), Dazu phi. burak
'schneidend* Jasna 56, 12, 4 (zum Praesensstamm),
phi. inf. brltan, burUan = paz. bridan, burldan
Gl. and Ind. 84, Shk. 237, Min. Gl. 43, phi. paz. brln
(-= skr. chinna) Min. cap. 27, 10, Shk. 237. Vgl.
Bartholomae, Studien zur idg. Sprachgeschichte,
II, 107, Anm. 4, und 180—181 ; Joh. Schmidt im Fest-
gruss an R. von Roth p. 186.
*) Arm. plinj : np. birinj — arm. hrinj 'Reis' : np. birinjf.
*J Aber gesiohert durch arab. hamiyya (No Id eke).
3) Dazu das Abstractum hurts *sectio' (Tom Praesensstamm ge-
bildet) sowie bal. inf. hurag^ buray *schneiden\
*) Im Sanskrit ist umgekehrt das Praesens (*bhrnami^ durch
Anlehnung an das Particip (*bhrltas) zu bhrlnami geworden wie
*grndmi zu grtnami (f'estgruss an Roth p. 186).
^) Bartholomae, Stud. II, 107 setzt als Grundforra *bhrmtanai
an, aber der persrsche InfinitiT wurde von der Wurzel gebildet, lautete
=== 6185 ===
Ausnahmen: Bahak, arabisirt aus Pabak = phi.
Papak; hab *Vater aus *pa6 (durch Assimilirung des An-
lauts an den Auslaut) = phi. "^pdp, arm. pap 'Grossvater ;
badafrdh 'Vergeltung* (Parsenwort), zu korrigiren in pada-
frah ; np. ba (neben pa in padrud u. s. w.) = paz. pa (s.
oben p. 21) mit unerklartem Uebergang von p in b. Dazu
birinj *Kupfer = arm. plinj, s. oben p. 27 — 28. Das von
Brockelmann, Lexicon syriacum p. 288 angefiihrte syr.
:ii1£» 'cyprum' ist nach N 6 Id eke unsicher.
Ap. p nach Vokalen = np. v oder b (iiber mp. w);
§ 66. Ap. p = np. 2^ in : avam, vam ^) Schuld = phi.
apam; huvaida 'deutlich*, aus hu + paidd; vdrUn 'inversus,
perversus, infaustus' = paz. awarUn *schlecht', phi. dparun
Gl. and Ind. 9; zdv *Spalt*, (?) s. oben p. 68 und 70; kavtis
ein Mass* = phi. kapTc (s. oben p. 89); pesvd *der voran-
geht' = phi, pesupai Gl. and Ind. 114, paz. pHawai Shk. 263,
```


## [2026-09-05T06:01:09.376Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT ==\"; grep -n -i \"bronze\\|birindsch\\|birinj\" LKT.txt | head -10; echo \"== AHD watkins bronze ==\"; grep -n -i \"bronze\" AHD_watkins1985.txt | head -5; echo \"== POK Messing/birinj ==\"; grep -n -i \"birinj\\|Messing\" POK_full.txt | head -5",
 "description": "Grep Lokotsch, Watkins, Pokorny"
}
```


### [2026-09-05T06:01:09.452Z] TOOL RESULT

```
== LKT ==
3786:hronzo,  frz.  sp.  hronce,  frz.  bronze;  ndl. brons,  engl,  bronze,  dtsch.  Bronze, Prinzmetall  [mit  vcjlksetymologischer Umgestallung,  POTT  in  ZKM  IV,  264]; russ.  hronza,  klruss.  bronza,  öecli.  poln. bronz,  serb.  bronac;  bulg.  pernio,  serb. pirinac  'Messing'.  —  [Die  anderen  Ab- leitungen sind  weniger  wahrscheinlich:
3788:2.  Mlat.  obryzum  sc.  aurum  =  gr.  XP'J" afov  ößpuCov  'Gold,  das  die  Feuerprobe bestanden  hat';  also  Bronze  nach  der goldenen  Farbe.  3.  Mgr.  ßpovxriaiov  < lat.  aes  brumlisium,  da  nach  Plin.  Hist. nat.  XXXIII,  9,  45;  XXXIV,  17,  40  in Brundisiuni,  heute  Brindisi,  bronzene Spiegel  hergestellt  wurden;  Etymologie von  Berthelot,  Sur  le  nom  du  bronze chez  les  alchimistes  grecs  in  Revue archeologique  1888,  S.  294.  Übrigens ist  der  Ortsname  Brundisium,  gr.  Bpcv- Tr)aiov,  nach  Strahns  Geographie  das niessapische  Woit  für  'Hirschkopf'.  In der  Tat  springt  die  Ähnlichkeit  der  Ge- stalt des  Hafens  mit  dem  Geweih  eines Hirsches  in  die  Augen ;  dazu  weist  Meyer, Essays  und  Studien  II,  311  auf  das albanesische  Wort  brin  'Geweih,  Horn' hin.]  [DozyOost26.  Kluge  70.  ML  1113. Bern  SlEtWb  87.
4704:Auch  tue,  tung  'Bronze';  hieraus  bulg. tue  'dass.',  serb.  tue  'dass.,  Messing, Glockenspeise';  runi.  tucm  'Gußmetall; Vase  aus  solchem  Metall',  [Sain  60, Mikl  SlEtWb  364  b.
5765:besehein  j.  2210 Beteigetize  St.  695 Betel  2149 betucht  j.  267 Betuchter  j.  267 Betuecliter  j.  267 Bezoar  1605 Bisam  293 ii/Mse  1647 Boback  181 ß��c/i^r  j.  180 Bombasin  16 17 Bonze  331 Borax  356 Boretsch  13 Borretsch  13 £os  j.  184  a Bronze  1657 Burnus  365 Burrich  13 5?<sa  376 Buxkin  324
6024:bronze  1657
6380:bouracan  250 i  bournotcs  365 1  bourrache  13 j  boutargue  274 i  bouza  376 j  brodequin  1856 !  bronce  1657 I  bronze  1657 I  brouhaha  256
== AHD watkins bronze ==
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
== POK Messing/birinj ==
```


## [2026-09-05T06:01:13.561Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3770,3790p' LKT.txt",
 "description": "Lokotsch bronze entry"
}
```


### [2026-09-05T06:01:13.604Z] TOOL RESULT

```
'Großes  Haus'  [vgl.  kopt.  pero  'Haus' und  W.  Spiegelberg,  Die  Schrift  und Sprache  der  alten  Ägypter.  1907.  S.  26], Name  des  altägyptischen  Königs,  gr. q)apaüj;  hieraus  it.  faraone,  frz.  pharaon; engl,  pharaoh,  dtsch.  Pharao,  auch  Name eines  Kartenspieles,  verkürzt  Pharo  ge- nannt, da  der  Herzkönig  auch  Pharao hieß.
1651.  Mal.  peräha:
Auch  prähü  [Pijn  156;  doch  vgl.  auch malayäl.  päru  'Boot']  'Boot';  hieraus angloind.  parao,  engl,  prow,  prau,  proa, bes.  Malay  prow  'kleines  Schiff  jeder Art',  bes.  gerne  von  Seeräubern  benutzt, da  sie  damit  schnell  in  die  Flüsse  hinauf- fahren können,  um  sich  der  Verfolgung zu  entziehen;  dtsch.  Praue;  sp.  proa, pg.  2>c"'cu,  sp.  pg.  it.  parao,  frz.  prao, pro.  [MMM  45.  Devic  DEt  186.  Eguilaz 468.  Hobson-Jobson  733.  JAOS  XVIII, 93/97.
1652.  Hebr.  pesah: 'Osteropfer,  Osterfest',  gr.  udaxa,  lat. pascha,ki}.paschalis  'österlich';  hieraus it.  pasqiia,  pasqiiale,  sard.  pasca,  prov. pasca,  pasqua,  frz.  päque,  plr.  päqties 'christliche  Ostern',  kat.  pasqua,  sp. pascua,  pg.  pascoa,  rum.  paqti;  russ. pasha,  paska;  engl.  ndl.  pasch,  dtsch. Passa.    [Eguilaz  469.    ML  6264.
1653.  Tk.  pic:
'Bastard,  Junge'  [Kelekian  Kämüs  330a]; hieraus  bulg.  pic  'dass.',  rum.  pictü 'Knirps,  Balg'.
1654.  Tk.  pide:
Auch  pite  'Brot  in  flacher,  Janger  Band- form' [>  ngr.  uriTtt];  hieraus  ruvci.  pita 'Brot',  pitar  'Bäcker',  pitärie;  bulg.  serb. pita  'Kuchen',  bul?.  pitice  'Krapfen'. [Löbel  EITAP  77.    Mikl  SlEtWb  248a.
1655.  Mal.  piknl:
'Eine  über  der  Schulter  getragene  Last' [Pijn  168],  'Gewicht',  dessen  Höhe  in den  verschiedenen  mal.  Ländern  variiert, z.  B.  in  Sumatra  60  kg;  hieraus  frz. pikoul,  engl,  pihul,  picul,  dtsch.  Pikid. [MMM  43.
1656.  Tk.  pilaw:
'Mit  Fett  abgekochter  Reis';  hieraus  in derselben  Bedeutung  rum.  pilaf,  frz.  pi- laf,  pilau;  engl,  pilau,  pillau,  pilaw, pillaw;  russ.  jyilaw,  plow.
1657.  Pers.  piring:
Auch  hiring  'Kupfer'  [Horn  NpEt  S.  48, Nr.  208 bis];  hieraus  mlat.  bronzium,  it.
133
[Pers.  pis-ahäng.
hronzo,  frz.  sp.  hronce,  frz.  bronze;  ndl. brons,  engl,  bronze,  dtsch.  Bronze, Prinzmetall  [mit  vcjlksetymologischer Umgestallung,  POTT  in  ZKM  IV,  264]; russ.  hronza,  klruss.  bronza,  öecli.  poln. bronz,  serb.  bronac;  bulg.  pernio,  serb. pirinac  'Messing'.  —  [Die  anderen  Ab- leitungen sind  weniger  wahrscheinlich:
1.  Ahd.  *brunizzo  'bräunliches  Metall' -<  dtsch.  bruno  'braun',  mlat.  brunitius.
2.  Mlat.  obryzum  sc.  aurum  =  gr.  XP'J" afov  ößpuCov  'Gold,  das  die  Feuerprobe bestanden  hat';  also  Bronze  nach  der goldenen  Farbe.  3.  Mgr.  ßpovxriaiov  < lat.  aes  brumlisium,  da  nach  Plin.  Hist. nat.  XXXIII,  9,  45;  XXXIV,  17,  40  in Brundisiuni,  heute  Brindisi,  bronzene Spiegel  hergestellt  wurden;  Etymologie von  Berthelot,  Sur  le  nom  du  bronze chez  les  alchimistes  grecs  in  Revue archeologique  1888,  S.  294.  Übrigens ist  der  Ortsname  Brundisium,  gr.  Bpcv- Tr)aiov,  nach  Strahns  Geographie  das niessapische  Woit  für  'Hirschkopf'.  In der  Tat  springt  die  Ähnlichkeit  der  Ge- stalt des  Hafens  mit  dem  Geweih  eines Hirsches  in  die  Augen ;  dazu  weist  Meyer, Essays  und  Studien  II,  311  auf  das albanesische  Wort  brin  'Geweih,  Horn' hin.]  [DozyOost26.  Kluge  70.  ML  1113. Bern  SlEtWb  87.
1658.  Pers.  pis-äliäng:
'Führer,  Zuhälter'  [aus  pers.  pes  'zuerst' Horn  NpEt  S.  79,  Nr.  356  und  ähäng. Präsensstamm  zu  ahängldän  'ziehen' ebenda  S.  14,  Nr.  58],  tk.  umgestaltet zu  pezeivenk  'dass.'  [Kelekian  Kämüs 321  b];  hieraus  rum.  pezeoenchm  'Kupp- ler', pezevenche  'Kupplerin',  pecevenclic 'Kuppelei'.
```


## [2026-09-05T06:01:23.127Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"برنز\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"== برنج MON ==\"; grep -n \"برنج:\" MON_part1.txt | head -5",
 "description": "Grep Moin for bronz"
}
```


### [2026-09-05T06:01:23.212Z] TOOL RESULT

```
MON_part1.txt:73670:است. رنگ پرهای بدنش برنزی مایل به 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:73670:است. رنگ پرهای بدنش برنزی مایل به 
== برنج MON ==
87925:شیربرنج: لجه:»0-.5 (امر.) خوراکیی که با
```


## [2026-09-05T06:01:31.448Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A3 \"Borrowed from\\|From French\" 7eebd4293cc12d9c.txt | head -20; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%86%D8%B2/\" --note \"page 77: Persian برنز bronze, Moin/Dehkhoda\"",
 "description": "Wiktionary bronze + fetch Persian bronz"
}
```


### [2026-09-05T06:01:33.243Z] TOOL RESULT

```
Exit code 2
350: From French bronze (1511); from Italian bronzo (13th c.), of uncertain origin ( q.v. ). First use appears c.  1721 in the writings of Matthew Prior (for which, see citation below).
351-
352- Pronunciation
353- [ edit ] 
--
1175: Borrowed from Italian bronzo .
1176-
1177- Pronunciation
1178- [ edit ] 
--
1254: Borrowed from Danish bronze ; see English bronze etymology .
1255-
1256- Noun
1257- [ edit ] 
--
1288: Borrowed from French bronze , from Italian bronzo , [ 1 ] [ 2 ] either from Byzantine Greek βροντησίον ( brontēsíon ) , presumably from Βρεντήσιον ( Brentḗsion , “ Brindisi ” ) , known for the manufacture of bronze; or ultimately from Persian برنج ( berenj, beranj , “ brass ” ) ~ پرنگ ( pereng , “ copper ” ) .
1289-
1290- Pronunciation
1291- [ edit ] 
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/web/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-05T06:01:37.018Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%86%D8%B2/\" --note \"page 77: Persian برنز bronze (Moin/Dehkhoda)\" && python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%81%DA%98\" --note \"page 77: Persian فژ dirty\"",
 "description": "Fetch bronz and faz sources"
}
```


### [2026-09-05T06:01:40.664Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/ea212d86c574a93e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cbbccb28279c822.txt
```


## [2026-09-05T06:01:43.608Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== bronz ==\"; grep -n \"برنز\" ea212d86c574a93e.txt | head -8; echo \"== faz wikt ==\"; head -20 4cbbccb28279c822.txt; wc -c 4cbbccb28279c822.txt",
 "description": "Check fetched pages"
}
```


### [2026-09-05T06:01:43.664Z] TOOL RESULT

```
== bronz ==
4:TITLE: برنز - معنی در دیکشنری آبادیس
6:برنز - معنی در دیکشنری آبادیس 
10: برنز
13: مترادف برنز : آلیاژ مس و قلع، مفرغ
21: برنز. [ بْرُ / ب ُ رُ ] ( فرانسوی ، اِ ) آلیاژی که از آمیختن مس و قلع بدست می آید. مفرغ. ( فرهنگ فارسی معین ). و رجوع به مفرغ شود. 
37: برنز یا مِفرَغ ( به انگلیسی: Bronze ) آلیاژی است که عمدتاً از مس تشکیل شده و معمولاً با حدود ۱۲ تا ۱۲٫۵ درصد قلع و با افزودن فلزات دیگر ( مانند آلومینیوم، منگنز، نیکل یا روی ) و گاهی نافلزها مانند فسفر، یا شبه فلزهایی مانند آرسنیک یا سیلیسیم همراه است. این افزودنی ها طیف وسیعی از آلیاژها را تولید می کنند که ممکن است سخت تر از مس به تنهایی باشند یا دارای ویژگی های مفید دیگری مانند استحکام، شکل پذیری یا قابلیت ماشین کاری باشند. 
38:دورهٔ باستان شناسی که در آن برنز، سخت ترین فلز مورد استفادهٔ گسترده بود، با عنوان عصر برنز شناخته می شود. آغاز عصر برنز در غرب اوراسیا و هند به طور معمول به اواسط هزارهٔ چهارم پیش از میلاد و در اوایل هزارهٔ دوم پیش از میلاد در چین مربوط می شود. [ ۱] استفاده از برنز در جاهای دیگر نیز به تدریج، گسترش یافت. عصر برنز با عصر آهن دنبال شد که از حدود سال ۱۳۰۰ پیش از میلاد آغاز شد و در حدود سال ۵۰۰ پیش از میلاد به بیشتر اوراسیا رسید. 
39:از آن جا که آثار هنری تاریخی بیشتر از برنج ( مس و روی ) و برنز با ترکیب بندی های مختلف ساخته می شدند، موزه های مدرن و توصیف های علمی آثار هنری قدیمی تر به طور فزاینده ای از اصطلاح کلی «آلیاژ مس» استفاده می کنند. [ ۲] 
== faz wikt ==
URL: https://en.wiktionary.org/wiki/%D9%81%DA%98
FETCHED: 2026-09-05T06:01:40Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found138 4cbbccb28279c822.txt
```


## [2026-09-05T06:03:27.229Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"rejya\\|brzya\\|paro\\.b\\|par6\\.b\\|parö\" BRT.txt | head -20; echo \"== CHEUNG bazd ==\"; grep -n -i \"bazd\\|band.*sicken\" CHEUNG.txt | head -10",
 "description": "Grep Bartholomae parö.bərəjya and Cheung"
}
```


### [2026-09-05T06:03:27.304Z] TOOL RESULT

```
2459:sSmaidf  Y.  jG.  I ;  —  ahmya  zaoi^re  imat  us  haca  aiihyS  nmänaiibyS  ..N. ^.-^^L-j^- barfsma  äyae  yäti  Y.  2-i;  aE,  Vr.2. iff.;  parö  ibisyanbyö..  a^^am  ibaisattuhatqmXx.
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2950:•  j.  aonya-  n,  Bezeichnung  einer  Feuerungs- oder Heizvorrichtung :  'yat  haca  parö.- iarfjyäi {sd.)  V,Ä86;  —  'yat  haSa  taxair- yät(sd.)  V.Ä93.
3213:mit  pairi  'aufsagen,  hersagen'  (die  Gä- 'kä%):  *yöi  glü^i  ..srävayanti yezi  arastnm (sd.)  pairi.aoxta  pairi.äaa  vä  . .  pasla  vä parö  Vä  pairi.äm  aratufryö  ".  .  wenn einer  .  .  (die  GiJääworte)  zu  spät  oder  zu früh  aufsagt,  die  sind  ar."  N._J2.
3598:•  j.  aparö.apäxtara-  Adj.  'der  hintere nördliche':  viW  °ra  Janat  Yt 3. 16;  16" (Einschiebung  in  K  36,  MI  a).
4239:•  j.  "anaomo  mananhe  kya  vTsäi  kaia kia  parö"  FrD.  (i.
4256:•  j.  ana  parö  adv.-artigcVerb.  'vordem'(?); &!/  ana  parö  dus.hr?la  (sd.)  aat  ana par3  ma'^^rö  spmtd  S.2i.^(^).
4524:•  '}.  an-usant'  Adj.  (fem,  •saitt-)  'der (etwas)  nicht  (tun)  will,  widerwillig,  ohne CS  zu  wollen':  ndit  mam  vTspe  yazatat>hs •Sf/ttfm  fraerscinta  "nicht  mich  gegen meinenWillen.."Yt  i7. 19;  19;  —  v?r3zyjt usaitica  *°ja(//Vfl(NSf.)''"..  mag  sie  wollen oder  nicht"  N.  6\  —  virszylt  usaiti  (sd.) neu  *'saili'^  N.ö;  — yat  ■j^(NS.)  vi/yei- tii'aisA.)..  M.S.  a6.  a)  "jiJNSm.  alsAdv.J» 'widerwillig':  'sS..  avat  kvar»  ätäpaite{i^) •tJ  h-tu  ma  °s5  ave  stärB  V.9.41;  — frä ahmät  parö  vlspe  daiva  'SS  tarsta  mmanle Y.  57. 18.  o)  sva,  'mit  Gewalt':  vaim>m (sd.)  's5  pai'iy3ife^.4.i,^;  53.
5093:•  j.  ava  paröit  *d«rflna_m''  Inf.  'entzwei zu  spalten,  entzwei  zu  sprengen':  ava  mS azii  . . parsii  pairt^nam  arthvqm  ava.d°'' saäayelti  (sd.)  V.  18. 19^'.
5323:Fü. :  aparön  g&aiiin, j.  art&wytS.varlli  P.  28:  lies  riA-aiy'.
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
7254:frabanm  .  .  ä'  yimai  xia'irai  "iirisats, zima  *Amjas?nta  il'  he  tm  za  bvat  psnne .  .  ä°  yim3i  paüi.vaäiaim  . .  ä'  yimS  fra- sBsaJ  .  .  ä°  yimS  tmam  zam  vlsSvaya^  V. 2.2— 11;  —  äat{s.2)  aoxla  ahurö  mazdä yimäi  .  .  avi  ahSm  .  .  *z3m5  Janhtntu  .  . 3°'  t>m  var?m  kgnnava  . .  ä°  mqsta  yimS . .  3°  aoxta  aAurS  mazdä  . ,  S°  yimS  ava'^a kinnaot . .  ä°  yimö  var)m  k^rmaot .  .ä° . . V.2.22-33;  —  3at  (s.  8)  .  .  mjrr/ff  y5 paröJari  .  .  airö  väbm  surunaoitt  3°  .  . fradvaraiti  büsyqsta  FrW./o.4if.;  —  tat y^arjnd  apatacat  .  .  ä°   us.patal  franrase
7289:•  j,  hakat  daSva  "äparö  sente*''^  FrG.
8341:•  }.  uparö.kairya-  Adj.  'des  Tätigkeit überlegen  ist,  überlegen  wirkend":  vayus" ys  'ryB  Yti5.4;  ai,  3;  —  vaim  "rlm Y-  25.  5,  Yt  tS-  5;  —  vayaoS  'ryehe  Y. 22.24,  V. /p.13;  —  tiltrJm  .  .  'rim  Yt A4;  —  kavalm  :^armS  .  .  'rim  Yt.  19.9; 45;  —  /w(  z/Tspanam  sravatfhqm  °rim frada'hqm  yim  airyamamm  isttn  FrW.  4. 1 ;
8345:•  j.  uparö.vimanö.bya-  n.  'Ubergrosse  (?) Zweifelsucht':  rayam  %rizantüm  . .  ahe Paityanm  fräk^rmta^  attrS  tnainyui  .  . aftmca  -Alm  V.  r,  15.
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
8900:•  j.  kaeta-  m.  —  ?  — ,  wohl  Bezeichnung feindlicher  Wesen:  tistrim  ,  .  yim  pailis' mar.mte  .  .  masy,l'a  parö  darAi'qttS  (sd.) "/n.vj  pars  druzinlö  ".  .  und  die  A".,  die zuvor  böslich  gehandelt  haben"  YL>V.  5.
9389:•  j.  karsnaz-  m.  Name  einer  iranischen  masUtahe  V>.  10;  JÄ  44PUZ.  b)  'der Yz.TsM%\  yasmaoyö  parö  'nazS  {'^'2.)  hvira  geringfügigste':  yö  n��  matiltim  yasmm baon  sn-isfa  Yt.  13.  38.                                    yasäite  'titn  ^yasnat  frsyatät  (sd.)  Yt/.  24;
12469:sragis)  nlHt  tarsts  *JränSmaiU  .  .  parö •vaxibyS  frä  ahmät  pars  VJspe  'va . .  tarHa rumanie  tarUa  ttmanhs  ^dvannte  Y.  57. 1 8 ;
== CHEUNG bazd ==
1566:bandaiieiti (V 22.5) to "banaiieiti, which is not supported by the ppp. bazda- (N 56),
```


## [2026-09-05T06:03:32.667Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1545,1575p' CHEUNG.txt",
 "description": "Cheung bazda context"
}
```


### [2026-09-05T06:03:32.709Z] TOOL RESULT

```
*NEIR: ? Pash. wat (m.) ‘break, hole; gorge, defile’. Ó NEVP: 93 derives the form 
from *bista-, envisaging a connection with M. viskyo, Yi. visco ‘ravine, steep 
embankment’. 

*SANSKRIT: bhañj ‘to break’ (RV+) = EWAia П: 242 


4 *ban 


«PIE *b"eg- ‘to break’ > LIV: 66 f. | Pok.: 114 f. 

*IE COGNATES: Arm. bekanel ‘to break’, Arm. ebek (aor.) ‘broke’, Arm. bek 
‘shattered’, (?) Olrish -aid-begar ‘is dissolved’ 

*REFERENCES: DKS: 266a; Werba 1997: 210 f.; ESIJa II: 58; Lecoq 2002: 128 


*ban ‘to afflict, be afflicted’ 

*AVESTAN: ban- (caus.) ‘to make ill, afflict’. © КеПепѕ 1984: 143 emends ҮАУ. 
bandaiieiti (V 22.5) to "banaiieiti, which is not supported by the ppp. bazda- (N 56), 
Khot. basdaä- (cf. Sims-Williams 1989: 256). = Liste: 37 

Caus.: pres. INJ. 3pl. OAv. banaiion (Y 30.6); Partic.: perf. pass. YAv. banta- (Yt 13.24, V 22.5) 
*KHOTANESE: (?) ban- ‘to cry out, lament’, banānu (pl.) ‘mockery, [transl. BSkt.] 
abhandana-’. Ф The comparison of Khot. ban- to Skt. bhan? ‘to speak’, cited in SGS: 
l.c., is semantically unsatisfactory (as noticed by Schirmer, LIV: 69 f., fn 7). The 
presumed shift from ‘to speak’ to ‘to cry out, lament’ needs an explanation, having 
hardly any parallels in Пг. (or IE). Alternatively, the meaning of Khot. ban- perhaps 
allows a connection with Av. ban-, cf. DKS: 266b, s.v. bamcai ‘with lament’. The
```


## [2026-09-05T06:03:44.400Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg77.png\" /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/77.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T06:03:44.500Z] TOOL RESULT

```
total 1212
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 02:03 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
```


## [2026-09-05T06:03:51.784Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -9 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['bytes'], d['url'])\n\"",
 "description": "Check fetch statuses"
}
```


### [2026-09-05T06:03:54.583Z] TOOL RESULT

```
200 4659 https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87
200 6540 https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9
200 9089 https://www.etymonline.com/word/bronze
200 14810 https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%AC
200 31325 https://en.wiktionary.org/wiki/bronze
-1 39 https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84
200 8143 https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/
200 6429 https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%86%D8%B2/
-1 39 https://en.wiktionary.org/wiki/%D9%81%DA%98
```


## [2026-09-05T06:09:27.266Z] TOOL CALL #71: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-77.json",
 "content": "{\n  \"pdf_page\": 77,\n  \"book_page\": 47,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Batiaxě\",\n      \"verdict\": \"transcription_suspect\",\n      \"modern_form\": \"Greek βατιάκη / βατιάκιον (batiákē) 'Persian drinking cup' (Athenaeus XI); beside it Old Persian *bātah 'wine' > MP bādag; the family is ultimately Akkadian baṭû 'bowl for liquids, wine jar' (< baṭium 'vessel, basin')\",\n      \"note\": \"Horn's no. 155 (p. 36) is exactly Nourai's source: 'bādye \\\"Weingefäss\\\", vergl. bāde \\\"Wein\\\". ap. βατιάκη (φιάλη Athen. XI, 27) (de Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.).' Nourai's root box therefore reproduces Horn faithfully in substance — including the caveat, which he renders as 'The source of the Old Persian form is not clear' (Horn's 'unsicher'). Two things are nevertheless wrong with the box as printed. (1) The FORM: the word Horn cites is the Greek βατιάκη, i.e. batiākē with kappa; the book prints 'Batiaxě' with an x, which is not the attested form in any source (LSJ, Athenaeus, Ernout-Meillet, Wiktionary all have κ). Checked against the printed page (pdf p. 77, copy at data/verification/sources/refs/ocr/BOOK/77.png): the book itself prints 'Batiaxě', so this is Nourai's own misrendering, not a scan error. (2) The LANGUAGE LABEL: βατιάκη is a Greek word that Athenaeus reports as Persian; it is not an attested Old Persian form. The Old Persian antecedent modern sources reconstruct is *bātah 'wine' (whence MP bādag), and Latin batioca/batiola (Plautus, 2nd c. BCE) shows the cup-word already circulating in the Mediterranean. The ultimate source is Semitic (Akkadian baṭû), so 'the source of the Old Persian form is not clear' is over-cautious by 1999 standards rather than wrong.\",\n      \"note_fa\": \"ریشهٔ این خانواده در کتاب «Batiaxě» و «پارسی باستان» خوانده شده است. آنچه هرن (ص ۳۶، شمارهٔ ۱۵۵) آورده در واقع واژهٔ یونانی βατιάκη (batiākē) «جام شراب پارسی» است که آتنایوس آن را پارسی می‌خواند؛ پس نه «x» درست است و نه دقیقاً «پارسی باستان». صورت ایرانی بازسازی‌شدهٔ امروزی *bātah در پارسی باستان است که در فارسی میانه bādag شده است، و خاستگاه نهایی این واژه اکدی baṭû «کاسه و خم شراب» دانسته می‌شود؛ لاتینی batioca نزد پلاؤتوس (سدهٔ دوم پ.م.) نشان می‌دهد که واژه از دیرباز در مدیترانه رواج داشته. تصویر صفحهٔ چاپی بررسی شد: خطا از خودِ کتاب است، نه از خوانش اسکن. جمله‌ای که نورایی افزوده («خاستگاه صورت پارسی باستان روشن نیست») همان «unsicher» هرن است.\",\n      \"error_in\": \"book\",\n      \"book_prints\": \"Batiaxě\",\n      \"correct_form\": \"Batiākē (Gk. βατιάκη); the Old Iranian antecedent is OP *bātah\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87\",\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:36\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 155 (printed p. 36; HRN.txt line 1752, the OCR reads 'hädye *Weingefäss', vergl. bade 'Wein . ap. ßandarj' üsgaiiitj (ptdXrj Athen. XI, 27 (de Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.)' = 'bādye Weingefäss, vergl. bāde Wein. ap. βατιάκη (φιάλη Athen. XI, 27) …, unsicher; phl. batak'). The page carries the whole box: the Greek/'ap.' cup-word, the Pahlavi batak, the Persian bāde/bādye, and the caveat 'unsicher'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. batioca (LAT.txt line 7032)\", \"stance\": \"supports\", \"note\": \"'batioca, -ae f.: coupe à vin. Emprunt à une forme dialectale (Tarente, Héraclée) correspondant à ion.-att. βατιάκη. Un ex. de Pl. et un d'Arn. On trouve aussi batiola, de même sens (Pl. Colax frg. 1).' Attests the Greek form with κ and dates the cup-word to Plautus.\"},\n        {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"grep 'batiak|batiac' in KNT.txt (and TLM.txt, SPG_keilinschriften1881.txt): no hits — the word is not in the attested Old Persian corpus, which is why 'Old Persian' can only mean 'reported as Persian by a Greek author'.\"},\n        {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"silent\", \"note\": \"no Avestan cognate of the cup-word; grep gave nothing.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"bâtak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Pahlavi word is written ⟨bʾtk'⟩ and read bādag 'wine, must'; Nourai's 'bâtak' is the older graphic transliteration (t for the Book-Pahlavi letter that stands for /d/ after a long vowel), the same form Horn quotes as 'phl. batak (PPGl.)' from the Pahlavi-Pazand glossaries. MacKenzie, Concise Pahlavi Dictionary p. 16 has 'bādag [bʾtk' | N bāda] wine, must', and his English index 'wine bādag, may'. The suffix is the Middle Persian -ag (< OIr. -aka-) added to the base *bāt-, so the chain root → MP bādag is the standard one; Khotanese bātaa 'wine, must' is the sister form.\",\n          \"derivation_fa\": \"صورت پهلوی به خط کتابی ⟨bʾtk'⟩ نوشته می‌شود و bādag «می، شیرهٔ انگور» خوانده می‌شود؛ آنچه نورایی «bâtak» آورده، آوانگاری حرف‌به‌حرف کهن است (t در پهلوی پس از واکهٔ بلند برابر /d/ فارسی نو است) و همان صورتی است که هرن از واژه‌نامه‌های پهلوی نقل می‌کند. مکنزی در «فرهنگ کوچک پهلوی» ص ۱۶ آورده: bādag [bʾtk'] «می، شیره». پسوند ‑ag همان ‑aka- ایرانی باستان است. صورت خواستهٔ ختنی bātaa نیز هم‌ریشه است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"AEF:207\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi is not online (refs_online.json: 'catalogue/purchase only'); it is the Persian translation of Horn, so the equivalent passage is Horn no. 155, checked above, which does read 'phl. batak (PPGl.)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 16 s.v. bādag (PHD.txt line 233); index 'wine' line 4315\", \"stance\": \"supports\", \"note\": \"'bādaģ [?{А! | N a] wine, must' (OCR of 'bādag [bʾtk' | N bāda]'); English index: 'wine badag, may.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep 'bātak|bādag|bʾtk' gave no hit; Nyberg's glossary covers only the texts he edits, and 'wine' there is mad / has (line 1947).\"},\n            {\"src\": \"HRN\", \"where\": \"no. 155, p. 36\", \"stance\": \"supports\", \"note\": \"'phl. batak (PPGl.)' — Horn takes the Pahlavi form from the Pahlavi-Pazand glossaries, exactly Nourai's arrow.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"bâdeh; bâdîyeh; pâtîleh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"باده bāde 'wine' is the regular New Persian continuation of MP bādag: final -ag > -a/-e in New Persian (bandag > banda, bādag > bāde), so this word is confirmed. بادیه bādiye 'wine-bowl' is the same etymon but reached Persian by a detour: the Aramaic/Syriac bāṭīṯā and Arabic باطیة bāṭiya 'earthen wine vessel' (attested 7th c. CE, Sunan an-Nasāʾī) belong to the same Akkadian-based family, and Mo'in's own dictionary marks باطیه as '[ع. ← باطیة، ف. بادیه]', i.e. the Arabic shape of Persian بادیه — the doublet spelling باديه ( باطيه ) that the chart itself prints is the trace of this Arabic round trip. Nourai's arrow (straight from Pahlavi bātak) is therefore a simplification but not an error of family. پاتیله / پاتیل pātile 'large copper pot' is the weak link: Dehkhoda and Mo'in give only the meaning ('ظرف بزرگ مسین… پاتیله. تیان'; Mo'in 'دیگ بزرگ مسی'), with no etymology, and no source consulted connects it with bādag/bādiye; the p-/b- alternation Nourai relies on (as in piring/biring below) is possible but unattested here, so this word is unverified. The chart's own NOTE, that VFO:18 links these to English 'pot', has no support: 'pot' is Late Latin pottus / Old English pott of obscure origin, unrelated to the batiākē family, and VFO is not even in the project's reference key.\",\n          \"derivation_fa\": \"«باده» دنبالهٔ منظم فارسی میانهٔ bādag است؛ پسوند ‑ag فارسی میانه در فارسی نو به ‑ه بدل شده (bandag > بنده، bādag > باده)، پس این واژه بی‌گمان درست است. «بادیه» به معنی «کاسهٔ می» از همین خانواده است اما از راهی دیگر رسیده: صورت آرامی/سریانی bāṭīṯā و عربی «باطیة» (گواه سدهٔ نخست هجری در سنن نسائی) هم‌ریشه‌اند و معین خودْ ذیل «باطیه» می‌نویسد «[ع. ← باطیة، ف. بادیه]»؛ یعنی همان دوگانهٔ «بادیه (باطیه)» که در نمودار آمده، نشانِ همین رفت‌وبرگشت از راه عربی است. اما «پاتیله/پاتیل» بندِ سست این گره است: دهخدا و معین تنها معنا («ظرف بزرگ مسین»، «دیگ بزرگ مسی») می‌دهند و هیچ ریشه‌شناسی نمی‌آورند و هیچ منبعی آن را به bādag نمی‌پیوندد؛ ابدال پ/ب که نورایی بر آن تکیه دارد ممکن است ولی در اینجا گواهی ندارد. یادداشتِ نمودار دربارهٔ پیوند این واژه‌ها با pot انگلیسی نیز پذیرفتنی نیست: pot از لاتینی متأخر pottus است و ربطی به این خانواده ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AEF:207\", \"status\": \"not_checked\", \"note\": \"not online (see node 1); the German original Horn no. 155 (p. 36) carries the bāde/bādye pair — 'bādye Weingefäss, vergl. bāde Wein' — but has no پاتیله.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1, s.v. باده (BQT_v1_pages.txt line 16477)\", \"stance\": \"supports\", \"note\": \"'باده _ بفتح [اول] … : شراب ، در پهلوی … (اونوال ۳۹۲) ، معرب آن باذق' — Mo'in's footnote gives the Pahlavi antecedent and the Arabicized form باذق, i.e. the same chain Nourai draws.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. باده (MON_part1.txt line 20025) and s.v. باطیه (line 20671)\", \"stance\": \"partial\", \"note\": \"'باده: bāda (اِ.) نوشابه‌ای که مستی آورد' — no etymology; but s.v. باطیه: '[ع. ← باطیة، ف. بادیه] ظرف سفالینی که در آن شراب نگاه دارند' explicitly makes Arabic باطیة the counterpart of Persian بادیه. Mo'in's only بادیه headword (line 20048) is the unrelated Arabic بادیة 'desert'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 16 s.v. bādag\", \"stance\": \"supports\", \"note\": \"'bādag [bʾtk' | N bāda] wine, must' — MacKenzie himself gives New Persian bāda as the descendant.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha\", \"stance\": \"silent\", \"note\": \"grep 'باده' in incoming/ARY/ARY_pages.txt: no hit (the book covers IE roots; a Semitic loan is out of its scope).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Bazda\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Avestan bazda- 'afflicted, diseased' (past participle of ban- 'to afflict, make ill'), taken by Gharib as the source of Sogdian ʾβž 'bad, evil'\",\n      \"note\": \"The form and the language label are right: Avestan bazda- is real, attested in the Nērangestān (N 56), and Bartholomae s.v. glosses it 'erkrankt, krank, siech' — the past participle of ban- 'to fall/make ill' (Cheung, root *ban 'to afflict, be afflicted', with Khotanese basdaa-). What is not Avestan is the GLOSS: 'bad, sin' is the Sogdian meaning, projected back onto the Avestan etymon. Nourai is however faithfully following his cited source: Gharib's Sogdian dictionary, entry 464 (printed p. 18), writes the etymology of ʾβj- as '© < Av. bazda'. So the root box is a correct transcript of a real scholarly proposal whose semantic step ('afflicted, sick' → 'bad, foul, sinful') is Gharib's, not something modern handbooks state independently; Cheung lists no Sogdian reflex under *ban. Hence 'plausible' rather than 'confirmed'.\",\n      \"note_fa\": \"صورت و برچسب زبانی درست است: bazda- اوستایی واقعاً هست (نیرنگستان ۵۶) و بارتولومه آن را «erkrankt, krank, siech» (بیمار، رنجور) معنی می‌کند؛ اسم مفعولِ ban- «بیمار کردن، رنجاندن» است و چونگ نیز آن را زیر ریشهٔ *ban «رنجاندن» با ختنی basdaa- می‌آورد. آنچه اوستایی نیست، معناست: «بد، گناه» معنای سغدی است که به صورت اوستایی بازتابانده شده. با این همه نورایی امانت‌دار منبع خویش است: قریب در «فرهنگ سغدی»، مدخل ۴۶۴ (ص ۱۸ چاپی)، ریشه‌شناسی ʾβj- را چنین می‌نویسد: «< Av. bazda». پس این جعبهٔ ریشه نقلِ درستِ یک پیشنهاد علمی است که گام معناییِ آن («بیمار» ← «بد، پلید، گناه‌آلود») از آنِ قریب است و در فرهنگ‌های امروزی به‌صورت مستقل تأیید نشده؛ از این رو «با احتیاط پذیرفتنی».\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"SOD:18\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 464 'ʾβj- M … ©<Av. bazda … bad, evil, pain' (SOD.txt line 10522). The page numerals in the OCR put entry 464 between the markers '18' (line 10448) and '19' (line 10596), so entry 464 stands on printed p. 18 — Nourai's SOD:18 is a page citation and it is exact.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. bazda- (BRT.txt line 17049; cross-ref. at line 16708)\", \"stance\": \"partial\", \"note\": \"'j. bazda- Adj. \\\"erkrankt, krank, siech\\\"; … pasuš.ca … bazda nōit irišta … N.56'; and under band- 'PPfP. bazda- (s. bes.)'. The word exists but is glossed 'diseased', not 'bad, sin'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, root *ban 'to afflict, be afflicted' (CHEUNG.txt line 1557 ff.)\", \"stance\": \"partial\", \"note\": \"'*ban \\\"to afflict, be afflicted\\\". AVESTAN: ban- (caus.) \\\"to make ill, afflict\\\" … not supported by the ppp. bazda- (N 56), Khot. basdaā-'. Confirms the Avestan form and its 'afflict' sense; lists no Sogdian ʾβž under this root.\"},\n        {\"src\": \"SOD\", \"where\": \"Gharib entries 464, 579-584\", \"stance\": \"supports\", \"note\": \"the whole ʾβž- family (ʾβyz- 'bad, evil', ʾβyzʾkrtyh 'evil deed, sin', ʾβyzʾngārē 'evildoer') sits together, so the semantic range Nourai gives the root is exactly the Sogdian one.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`bz, `bj, `bž, `byz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four shapes are genuine Sogdian spellings of one word, differing only by script and scribal habit: Gharib's entry 464 heads it ʾβj- (Manichaean script) and reads it (ə)βž, βiž, βaž, βež, listing βyz-, βz- as variants and cross-referring to ʾβyz-, ʾβz-, βj-, βyj-, βz-; entry 579 ʾβyz- (Buddhist and Christian Sogdian) glosses it 'bad, evil'. The initial ʾ- is the prothetic aleph that Sogdian writes before an initial fricative cluster, and β is the bilabial fricative from Old Iranian *b-; the second consonant is /ž/, spelled z, j, ž or yz depending on the script. Derivatives in the same dictionary (ʾβyzʾkrtyh 'evil deed, sin', ʾβyzʾngārē 'evildoer', ʾβžāxūk 'miserable') show the range 'bad, evil, sin' that Nourai's gloss gives. Gharib's own references are 'GMS 179, 510; Hen. LW 101' — Gershevitch's Grammar of Manichean Sogdian and Henning's 'Sogdian Loan-words in New Persian' p. 101, which is Nourai's SLW:101.\",\n          \"derivation_fa\": \"هر چهار صورت، نگارش‌های گوناگون یک واژهٔ سغدی‌اند و تفاوتشان تنها به خط و عادت کاتبان است: قریب در مدخل ۴۶۴ سرواژه را ʾβj- (خط مانوی) می‌آورد و (ə)βž، βiž، βaž، βež می‌خواند و βyz-، βz- را نیز گونه می‌شمارد؛ مدخل ۵۷۹ همان را در سغدی بودایی و مسیحی ʾβyz- «بد، شرّ» ثبت کرده است. الفِ آغازین، الفِ پیشین (prothetic) سغدی است و β همان واکهٔ سایشی دولبی برآمده از *b ایرانی باستان؛ همخوان دوم /ژ/ است که بسته به خط z، j، ž یا yz نوشته می‌شود. مشتقات همین ریشه در فرهنگ قریب (ʾβyzʾkrtyh «گناه»، ʾβyzʾngārē «بدکار»، ʾβžāxūk «بیچاره») همان گسترهٔ معنایی «بد، گناه» را نشان می‌دهد. ارجاع خود قریب «GMS 179, 510; Hen. LW 101» است، یعنی همان SLW:101 نورایی.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:18\", \"status\": \"supports\", \"note\": \"SOD.txt line 10522, entry 464: 'ʾβj- M | aJ3z, Piz, Paz, Pez (byz-, bz-) ©<Av. bazda ©ob. -y =>ʾβyz-, ʾβz-, βj-, βyj-, βyz-, βz- | bad, evil, pain | GMS 179, 510; Hen. LW 101' (OCR renders β as P/p). Printed p. 18, between the page markers 18 and 19.\"},\n            {\"ref\": \"SLW:101\", \"status\": \"not_checked\", \"note\": \"Henning, 'Sogdian Loan-words in New Persian', BSOS X/1 (1939) p. 101 is not in the local scan of Henning's Selected Papers (grep 'Sogdian loan' in HENNING_selected_papers.txt returns only an unrelated passage on a Turkish loan). Corroborated indirectly twice over: Gharib cites 'Hen. LW 101' for this very entry, and Mo'in's footnote in Borhan-e Qate' p. 1485 cites 'Henning, BSOS X-1, p. 101-102' for the Persian reflexes.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entries 464, 579-584, 594-601 (SOD.txt lines 10522, 11241 ff., 11354 ff.)\", \"stance\": \"supports\", \"note\": \"579 'ʾβyz- B,S … bad, evil'; 582 'ʾβyzʾkrtyh … evil deed, sin'; 583 'ʾβyzʾngārē … evildoer' — the exact glosses Nourai gives.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"root *ban\", \"stance\": \"silent\", \"note\": \"no Sogdian reflex listed under *ban, so the Avestan ancestry of the Sogdian word rests on Gharib alone; the Sogdian word itself is not in doubt.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. bazda-\", \"stance\": \"partial\", \"note\": \"supplies the Avestan etymon but with the sense 'diseased'; the shift to 'bad, evil' is a Sogdian development.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"faž; fažâk; fažâğand\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"This is one of the best-documented Sogdian loans in early New Persian, and Nourai's citation lands exactly on the page that proves it. Mo'in's footnote to Borhan-e Qate' p. 1485 (vol. 3, pdf p. 278) says of فژ: 'درست از سغدی ʾβž, ʾβž-, ʾβz, سغدی مسیحی βž, βz, مانوی βž, βj, βyj «بد»، گناه … ریشه‌ای است پربار و دارای مشتقات بسیار، بعضی آنها در فارسی هم وارد شده. در برهان قاطع عناوین ذیل آمده: فژاک، فژاکن، فژاکین، فژغند، فژغنده … Henning, BSOS X-1, p. 101-102'. Phonetically the Sogdian bilabial fricative β- was heard by Persian speakers as f- (hence فژ, with the by-form پژ that Borhan also lists, showing the usual f/p wavering in loans), and Sogdian ž is kept. فژاک is the same base with the Persian adjectival -āk (Borhan's فژاکن is analysed by Mo'in, after Bailey BSOS VII 85, as the Persian compound fažh-agin), so it is a Persian formation on a Sogdian stem rather than a separate borrowing — still 'from Sogdian' in Nourai's sense. فژاغند/فژغند is the shakiest of the three: Mo'in's footnote on the next page reports Henning (BSOS X/1, p. 102 n. 1) as holding that فژغند, at least in the sense 'filthy, dirty', arises from a textual corruption (تصحیف) of فرغند, so its membership in the Sogdian family is disputed even by the authority Nourai's chain rests on. Hence the node as a whole is plausible: faž and fažāk confirmed, fažāğand doubtful.\",\n          \"derivation_fa\": \"این یکی از شناخته‌شده‌ترین وام‌واژه‌های سغدی در فارسی دری است و ارجاع نورایی درست بر همان صفحه‌ای می‌نشیند که گواه آن است. معین در حاشیهٔ برهان قاطع ص ۱۴۸۵ ذیل «فژ» می‌نویسد: «درست از سغدی ʾβž… سغدی مسیحی βž، βz، مانوی βž، βj، βyj «بد»، گناه… ریشه‌ای است پربار و دارای مشتقات بسیار، بعضی آنها در فارسی هم وارد شده… Henning, BSOS X-1, p.101-102». از نظر آوایی، واکهٔ سایشی دولبیِ سغدی (β) در گوش فارسی‌زبانان «ف» شنیده شده (از این‌رو «فژ»، با گونهٔ «پژ» که برهان نیز آورده و نمایندهٔ نوسان معمول ف/پ در وام‌واژه‌هاست) و «ژ» سغدی برجای مانده است. «فژاک» همان ستاک با پسوند فارسی ‑اک است؛ معین «فژاکن» را به پیروی از بیلی ترکیبی فارسی (fazh-agin) می‌داند، یعنی ساختی فارسی بر پایهٔ ستاکی سغدی. اما «فژاغند/فژغند» سست‌ترین بند است: معین در حاشیهٔ صفحهٔ پس از آن از حنینگ نقل می‌کند که «فژغند، لااقل به معنی پلید و چرکین، ناشی از تصحیف فرغند است». پس در مجموع: «فژ» و «فژاک» تأییدشده و «فژاغند» مشکوک.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1485\", \"status\": \"supports\", \"note\": \"Exact hit. Printed p. 1485 = vol. 3 pdf p. 278 (BQT_v3_pagemap.json maps printed 1485 → pdf 278); the OCR block tagged [pdf page 278] in incoming/BQT/BQT_v3_pages.txt (lines 20150-20220) carries the headword فژ 'چرک' and the footnote quoted in the derivation, with the Sogdian forms and the Henning citation. The next page (1486) carries فژاک، فژاکن، فژاکین، فژغند، فژغنده with their own footnotes.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 3, printed pp. 1485-1486, Mo'in's footnotes 8 and 4\", \"stance\": \"supports\", \"note\": \"'…«فژ» … درست از سغدی ʾβž … مانوی βž، βj، βyj «بد»، گناه … Henning, BSOS X-1, p.101-102'; and on p. 1486 'حنینگ گوید: فژغند، لااقل بمعنی پلید و چرکین، ناشی از تصحیف «فرغند» است' plus 'Bailey, BSOS VII, p.85 … fazh-agin ترکیبی فارسی است'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. فژ (MON_part1.txt line 31416) and فژاک (MON_part2.txt line 7283)\", \"stance\": \"supports\", \"note\": \"'فژ (اِ.) چرک، ریم، پلیدی'; 'فژاک (ص.مر.) چرکین، چرکن'; and 'فژاکن … [فژ + ‑اکن]' — the same base and the same derivational analysis.\"},\n            {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt lines 3769, 11201; FRS.txt line 16082)\", \"stance\": \"supports\", \"note\": \"'پلید و پلشت باشد و فژاکن [رودکی گوید…]' and 'کیست چون تو فژاکن و فژغند' — 11th-c. attestation of both فژاکن and فژغند in the sense 'filthy', i.e. the words are genuinely early New Persian, as a Sogdian loan of the Samanid period should be.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib entry 464\", \"stance\": \"supports\", \"note\": \"gives the Sogdian source forms and cites Henning's loan-word paper p. 101 for exactly this transfer.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Berenža\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"New Persian برنج berenj / پرنگ pereng 'brass, copper', from Middle Persian brinǰ (Manichaean MP brynng), Parthian plinǰ — a Middle Iranian culture-word of disputed, probably non-Indo-European origin; there is no Avestan *bərənža- 'brass'\",\n      \"note\": \"The root box does not survive checking. (a) No Avestan word 'berenža 'brass'' is attested. What Horn actually writes on the page Nourai cites (HRN:48, no. 208bis) is: '(2)birinj \\\"Kupfer\\\". Zusammenhang mit aw. bərəǰya- (in parō.bərəǰya-) ist durchaus unsicher' — 'the connection with Avestan bərəǰya- (in parō.bərəǰya-) is thoroughly uncertain'. bərəǰya- is not a word for brass; it occurs only inside the obscure Avestan compound parō.bərəǰya-. Nourai has promoted Horn's explicitly rejected guess to a root box, dropped the caveat, and given it the gloss of the Persian word. (b) Hübschmann, Persische Studien §209bis (pp. 27-28), reviewing the same material, concludes 'Wohl Fremdwort im Iranischen' — probably a loanword within Iranian. (c) Modern handbooks (Wiktionary s.v. برنج, following Encyclopaedia Iranica) derive NP berenj from MP brinǰ / Man. MP brynng 'bronze, brass', with Parthian plinǰ, Old Armenian płinj, Old Georgian ṗilenʒi, Syriac plezzā as the Middle Iranian spread, and call the ultimate origin onomatopoeic ('imitative of ringing brass') — not Avestan. (d) The spelling itself: Horn's form is bərəǰya- with ǰ, not ž. Also note that Horn's neighbouring no. 208 is birinj 'rice' (< *vrinji-), an entirely different word; Nourai correctly keeps them apart by writing 'berenj 1'.\",\n      \"note_fa\": \"این جعبهٔ ریشه پذیرفتنی نیست. نخست آنکه واژهٔ اوستایی «بِرِنژَه» به معنی «برنج/مفرغ» گواهی ندارد. آنچه هرن در همان ص ۴۸ (شمارهٔ ۲۰۸ مکرر) نوشته این است: «(۲)birinj «مس». پیوند آن با اوستایی bərəǰya- (در parō.bərəǰya-) به‌کلی نامطمئن است» — یعنی خودِ منبعِ استنادشده این پیوند را رد می‌کند و bərəǰya- هم واژه‌ای به معنی برنج نیست، بلکه تنها در ترکیب مبهم parō.bərəǰya- می‌آید. دوم، هوبشمان در «مطالعات فارسی» (بند ۲۰۹ مکرر، ص ۲۷–۲۸) پس از بررسی همین شواهد نتیجه می‌گیرد: «احتمالاً وام‌واژه‌ای در ایرانی است». سوم، پژوهش امروزی (ویکی‌واژه به پیروی از دانشنامهٔ ایرانیکا) «برنج» را از فارسی میانهٔ brinǰ / مانوی brynng می‌گیرد، با هم‌ریشه‌های پارتی plinǰ، ارمنی کهن płinj، گرجی کهن ṗilenʒi و سریانی plezzā، و خاستگاه نهایی را نام‌آوا (تقلید آوای زنگِ فلز) می‌داند، نه اوستایی. افزون بر این، صورت هرن bərəǰya- با «ج» است نه «ژ». پس: پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%AC\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:48\", \"status\": \"contradicts\", \"note\": \"Horn no. 208bis, printed p. 48 (HRN.txt lines 2214-2219): '(2)birinj \\\"Kupfer\\\". Zusammenhang mit aw. berejya- (in parö.berejya-) ist durchaus unsicher; vergl. Schrader, Sprachvergleichung und Urgeschichte 273, 274, kurd. LW. birinj, bel. LW. brinj (34)'. The cited page states the opposite of the arrow: Horn calls the Avestan connection thoroughly uncertain and treats the Kurdish and Balochi forms as loans from Persian.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §209bis, pp. 27-28 (HUB.txt lines 888-895)\", \"stance\": \"contradicts\", \"note\": \"'Np. birinj \\\"Kupfer, Messing\\\" … ist nach Vullers die (jüngere) Nebenform zu piring … Zu ihr stimmt kurd. pirinjok = birinj \\\"bronze\\\" und arm. płinj \\\"Kupfer, Kupfergeld, Münze, Erz, Messing\\\" (5. Jhd.). Wohl Fremdwort im Iranischen.' Repeated at HUB p. 69 (line 6191): 'birinj \\\"Kupfer\\\" = arm. płinj, s. oben p. 27-28'.\"},\n        {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"not_found\", \"note\": \"grep for 'berejya', 'brzya', 'parö.b' in BRT.txt found no usable entry (the OCR of Avestan diacritics is very poor, so this is not proof of absence); in any case no Avestan word glossed 'brass' turned up.\"},\n        {\"src\": \"POK\", \"where\": \"Pokorny IEW\", \"stance\": \"silent\", \"note\": \"grep 'birinj|Messing' in POK_full.txt: no hits — the word has no Indo-European root entry, consistent with its being a culture-word.\"},\n        {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1657 (LKT.txt lines 3767-3790)\", \"stance\": \"supports\", \"note\": \"'1657. Pers. piring: Auch biring \\\"Kupfer\\\" [Horn NpEt S. 48, Nr. 208bis]; hieraus mlat. bronzium, it. bronzo, frz. sp. bronce, frz. bronze; ndl. brons, engl. bronze, dtsch. Bronze…' — supports the Persian→European half of Nourai's chart (see the nodes), while saying nothing for an Avestan origin.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"berenj 1\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word itself is beyond doubt: برنج berenj 'brass' (kept apart in the chart from berenj 2 'rice' by the numeral) is inherited from Middle Persian brinǰ, spelled blnc in Book Pahlavi and brynng /bring/ in Manichaean Middle Persian with the meaning 'bronze, brass'; its Parthian counterpart is plinǰ, and the by-form پرنگ pereng with p- is what Vullers and Hübschmann record. The same Middle Iranian word was borrowed all round the Caucasus (Old Armenian płinj, Old Georgian ṗilenʒi 'copper', Udi ṗilinǯ, Syriac plezzā), which is why it is usually taken for a wandering metal-name rather than an inherited Iranian noun; Encyclopaedia Iranica suggests an onomatopoeic origin, imitative of ringing metal. What is only 'plausible' is the ARROW: the chart makes berenj descend from an Avestan 'Berenža', and the source Nourai cites for it (Horn p. 48) explicitly calls that connection 'durchaus unsicher', while Hübschmann calls the word a loan within Iranian. So: real word, right meaning, unproven ancestry.\",\n          \"derivation_fa\": \"خودِ واژه تردیدناپذیر است: «برنج ۱» (که نورایی با شمارهٔ ۱ آن را از «برنج ۲» به معنی غله جدا کرده) از فارسی میانهٔ brinǰ به ارث رسیده؛ در پهلوی کتابی blnc و در فارسی میانهٔ مانوی brynng /bring/ «مفرغ، برنج» نوشته می‌شود و همتای پارتی آن plinǰ است؛ گونهٔ «پرنگ» با «پ» را ولرس و هوبشمان ثبت کرده‌اند. همین واژهٔ ایرانی میانه در سراسر قفقاز وام گرفته شده (ارمنی کهن płinj، گرجی کهن ṗilenʒi «مس»، اودی ṗilinǯ، سریانی plezzā)، و از همین‌رو آن را نامِ سرگردانِ فلز می‌دانند نه اسمی ایرانی‌الاصل؛ دانشنامهٔ ایرانیکا خاستگاه آن را نام‌آوا (تقلید آوای زنگ فلز) می‌داند. آنچه تنها «با احتیاط پذیرفتنی» است، خودِ پیکان است: نمودار «برنج» را از «Berenža»ی اوستایی می‌گیرد، حال آنکه هرن در همان ص ۴۸ این پیوند را «به‌کلی نامطمئن» می‌خواند و هوبشمان واژه را وام‌واژه‌ای درون‌ایرانی می‌شمارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:48\", \"status\": \"partial\", \"note\": \"Horn no. 208bis, p. 48, has the word with the gloss 'Kupfer' (copper) rather than 'brass', and rejects the Avestan link: 'Zusammenhang mit aw. bərəǰya- … ist durchaus unsicher'. It therefore supports the existence and the Iranian standing of berenj, but not the arrow drawn from the root box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §209bis, pp. 27-28\", \"stance\": \"partial\", \"note\": \"'Np. birinj \\\"Kupfer, Messing\\\" … arm. płinj … (5. Jhd.). Wohl Fremdwort im Iranischen.' Word confirmed, Iranian ancestry denied.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1657\", \"stance\": \"supports\", \"note\": \"'Pers. piring: Auch biring \\\"Kupfer\\\" [Horn NpEt S. 48, Nr. 208bis]' — the Persian word is the starting point of the whole European chain.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi\", \"stance\": \"silent\", \"note\": \"grep 'برنج:' in MON_part1.txt found only the compound شیربرنج; the two-volume OCR on disk has no usable برنج headword.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"bronzium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form is right but the label needs qualifying: bronzium is MEDIEVAL Latin, not classical Latin — it is the Latin shape behind Italian bronzo, first visible in medieval metallurgical usage, and Etymonline states plainly 'from Italian bronzo, from Medieval Latin bronzium, which is of uncertain origin'. That a Persian metal-name lies behind it is one live theory and the one Nourai adopts; it is exactly what Lokotsch no. 1657 argues ('Pers. piring … hieraus mlat. bronzium, it. bronzo …'), and Klein, on the page Nourai cites, agrees in substance ('bronze, n. — F., fr. It. bronzo, bronzino, ult. fr. Persian birinj'), though Klein goes straight from Italian to Persian without a Latin waystation. Against it stand two rivals that the same handbooks list: Byzantine Greek βροντήσιον from Brundisium/Brindisi (Pliny's aes Brundusinum, mirrors of Brindisi — Berthelot 1888), and a Germanic source, Old High German brūn 'brown' via Medieval Latin brunitius. Skeat and Funk & Wagnalls take the Germanic line outright. Lokotsch calls the rivals 'weniger wahrscheinlich'; Etymonline and Wiktionary leave the question open. So 'plausible', not 'confirmed'.\",\n          \"derivation_fa\": \"صورت درست است اما برچسب زبانی نیازمند قید: bronzium لاتینیِ میانه (قرون‌وسطایی) است نه لاتینی کلاسیک؛ همان صورتی که پشتِ ایتالیایی bronzo ایستاده است. اتیمانلاین می‌نویسد: «از ایتالیایی bronzo، از لاتینی میانهٔ bronzium که خاستگاهش نامعلوم است». اینکه نامی ایرانی برای فلز پشت آن باشد یکی از فرضیه‌های زنده است و همان است که نورایی برگزیده؛ لوکوچ (شمارهٔ ۱۶۵۷) دقیقاً همین را می‌گوید: «فارسی piring/biring «مس» … از آن لاتینی میانهٔ bronzium، ایتالیایی bronzo …»؛ کلاین نیز در همان صفحهٔ ۲۰۳ که نورایی ارجاع داده در اصلِ مطلب هم‌داستان است، هرچند بی‌واسطهٔ لاتینی: «bronze از فرانسه، از ایتالیایی bronzo، در نهایت از فارسی birinj». در برابر آن دو فرضیهٔ رقیب هست: یونانیِ بیزانسی βροντήσιον از Brundisium (بریندیزی، به گواه پلینیوس) و خاستگاه ژرمنی از brūn «قهوه‌ای». لوکوچ این دو را «کم‌احتمال‌تر» می‌داند و اسکیت و فانک‌واگنالز درست همان ژرمنی را می‌پذیرند. پس: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronze\",\n            \"https://en.wiktionary.org/wiki/bronze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:203\", \"status\": \"partial\", \"note\": \"Klein, Comprehensive Etymological Dictionary, p. 203 (the page numeral '203' stands a few lines above the entry in KLN_1966.txt, line 5712): 'bronze, n. — F., fr. It. bronzo, bronzino, ult. fr. Persian birinj.' Klein supports the Persian origin and the French/Italian route but posits no Latin bronzium.\"},\n            {\"ref\": \"PRT:60\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is lending-only on archive.org and has no local copy (refs_online.json: 'RE-SEARCH 2026-09: 8 lending copies, none open').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, no. 1657\", \"stance\": \"supports\", \"note\": \"'Pers. piring: Auch biring \\\"Kupfer\\\" [Horn NpEt S. 48, Nr. 208bis]; hieraus mlat. bronzium, it. bronzo, frz. sp. bronce, frz. bronze; ndl. brons, engl. bronze, dtsch. Bronze … [Die anderen Ableitungen sind weniger wahrscheinlich: 1. Ahd. *brunizzo … 2. Mlat. obryzum … 3. Mgr. βροντήσιον < lat. aes brundisium …]'. This is the single closest match to Nourai's whole chart, Medieval Latin bronzium included.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. Bronze (SKT.txt line 2332)\", \"stance\": \"contradicts\", \"note\": \"'Bronze. (F.-Ital.-Teut.) See Brown.' Skeat routes it to Germanic *brūn 'brown', not to Persian.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary s.v. bronze (FSD_vol1.txt line 50535 ff.)\", \"stance\": \"contradicts\", \"note\": \"the etymology bracket ends '[F., < It. bronzo, brass, < brown, < OHG. brūn]' — the Germanic derivation again.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"grep 'bronz' in LAT.txt returns only French glosses of aes; bronzium is post-classical and outside the dictionary's scope, which is itself evidence that the label 'Latin' should read 'Medieval Latin'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Italian\",\n          \"words\": \"bronzo\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Italian bronzo 'bronze' is attested from the 13th century and is the immediate source of every other European form; Wiktionary dates French bronze to 1511 'from Italian bronzo (13th c.)'. The Italian word continues Medieval Latin bronzium with the regular Italian outcome -ium > -o. Whatever the ultimate origin of bronzium, this link in the chain is uncontroversial: Klein, Skeat, Lokotsch, Etymonline and Wiktionary all route the word through Italian.\",\n          \"derivation_fa\": \"«bronzo» ایتالیایی از سدهٔ سیزدهم میلادی گواهی شده و سرچشمهٔ بی‌واسطهٔ همهٔ صورت‌های اروپایی دیگر است؛ ویکی‌واژه صورت فرانسوی bronze را به سال ۱۵۱۱ و برگرفته از ایتالیایی bronzo می‌داند. واژهٔ ایتالیایی دنبالهٔ لاتینی میانهٔ bronzium است با تحول منظم ‑ium به ‑o. خاستگاه نهایی bronzium هرچه باشد، این حلقه از زنجیره مورد اختلاف نیست: کلاین، اسکیت، لوکوچ، اتیمانلاین و ویکی‌واژه همگی مسیر را از ایتالیایی می‌گذرانند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronze\",\n            \"https://en.wiktionary.org/wiki/bronze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; checked against Klein p. 203, Lokotsch 1657 and Etymonline instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 203 s.v. bronze\", \"stance\": \"supports\", \"note\": \"'bronze, n. — F., fr. It. bronzo, bronzino…'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1657\", \"stance\": \"supports\", \"note\": \"'…hieraus mlat. bronzium, it. bronzo, frz. sp. bronce, frz. bronze…' — Italian in exactly Nourai's position.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Bronze\", \"stance\": \"partial\", \"note\": \"'Bronze. (F.-Ital.-Teut.)' — Skeat too has French from Italian; he differs only on what lies beyond Italian.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through node with no word printed: it stands for French bronze, borrowed from Italian bronzo and first recorded in 1511 (Wiktionary), from which English took the noun in 1721 and Persian took برنز in the 20th century. Etymonline: 'from French bronze, from Italian bronzo'. Nothing in the chart depends on this node beyond the routing, and the routing is standard.\",\n          \"derivation_fa\": \"این گره گذرگاهی است و در کتاب واژه‌ای در آن چاپ نشده؛ منظور واژهٔ فرانسویِ bronze است که از ایتالیایی bronzo وام گرفته شده و نخستین گواه آن ۱۵۱۱ میلادی است (ویکی‌واژه). انگلیسی اسم bronze را در ۱۷۲۱ از فرانسه گرفته و فارسی «برنز» را در سدهٔ بیستم. اتیمانلاین: «از فرانسویِ bronze، از ایتالیایی bronzo». مسیرِ ترسیم‌شده استاندارد است و درست.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronze\",\n            \"https://en.wiktionary.org/wiki/bronze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference printed for this node; checked against Etymonline and Wiktionary, which both give French bronze < Italian bronzo.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 203 s.v. bronze\", \"stance\": \"supports\", \"note\": \"'bronze, n. — F., fr. It. bronzo' — English from French, French from Italian.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1657\", \"stance\": \"supports\", \"note\": \"'…it. bronzo, frz. sp. bronce, frz. bronze; ndl. brons, engl. bronze, dtsch. Bronze…'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"bronz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"برنز beronz is a modern European loan in Persian, taken from French bronze during the 19th-20th century wave of technical borrowings (the French shape, not the English, is shown by the final -z and by the vowel). Mo'in's dictionary labels it outright: 'برنز. [بْرُ / بُ رُ] (فرانسوی، اِ) آلیاژی که از آمیختن مس و قلع بدست می‌آید. مفرغ.' The word is thus a round trip in Nourai's sense — a Middle Iranian metal-name that travelled to Italy, France and back — but only if the Persian origin of bronzium (node 2) is accepted; the loan from French itself is certain. Persian keeps its inherited برنج for 'brass' and uses برنز/مفرغ for the copper-tin alloy.\",\n          \"derivation_fa\": \"«برنز» وام‌واژه‌ای اروپایی و امروزی در فارسی است که در موج وام‌گیری‌های فنی سدهٔ سیزدهم و چهاردهم خورشیدی از فرانسویِ bronze گرفته شده (صورت فرانسوی است نه انگلیسی، چنان‌که پایانهٔ ‑ز و واکهٔ آن نشان می‌دهد). معین صریح می‌نویسد: «برنز. (فرانسوی، اِ) آلیاژی که از آمیختن مس و قلع به دست می‌آید. مفرغ.» پس این واژه ــ اگر ریشهٔ ایرانیِ bronzium پذیرفته شود ــ نمونهٔ رفت‌وبرگشت است: نامِ فلزی ایرانی میانه که به ایتالیا و فرانسه رفت و بازگشت؛ اما خودِ وام‌گیری از فرانسه قطعی است. فارسی برای «برنج» (آلیاژ مس و روی) همان واژهٔ ارثی و برای آلیاژ مس و قلع «برنز/مفرغ» را به کار می‌برد.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%86%D8%B2/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"not_found\", \"note\": \"Nourai cites MON without a volume/page. برنز is absent from the local OCR of Mo'in (MON_part1/part2 and the two-volume Adena scan: only برنزی in a bird description at line 73670); it belongs to Mo'in's vol. 4 of foreign words, which is not on disk. The entry was recovered instead from abadis.ir, which quotes it verbatim with the attribution '(فرهنگ فارسی معین)': 'برنز. (فرانسوی، اِ) آلیاژی که از آمیختن مس و قلع بدست می‌آید. مفرغ.' — so the citation is right, just not checkable in the local copy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. برنز, quoted at abadis.ir\", \"stance\": \"supports\", \"note\": \"'(فرانسوی، اِ)' — Mo'in labels the word French, exactly the arrow French → Persian that the chart draws.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1657\", \"stance\": \"supports\", \"note\": \"lists the modern spread of French/Italian bronze into Dutch, English, German, Russian, Czech, Polish, Serbian; Persian برنز is the same 19th-20th c. wave.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"bronze\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English bronze 'alloy of copper and (usually) tin' is first recorded in 1721 (Etymonline; Wiktionary cites Matthew Prior for the first use), borrowed from French bronze. Before that Middle English made no distinction between the copper-tin and copper-zinc alloys and called both bras, which is why bronze was needed as a new term. The verb (1640s 'to give the colour of bronze to') came in from French bronzer. Nourai's node is correct in form, meaning and route; the AHD citation is to the main dictionary, not to the Indo-European appendix (Watkins has no entry for this word, since it is a wandering culture-word, not an IE inheritance).\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ bronze «آلیاژ مس و (معمولاً) قلع» نخستین بار در ۱۷۲۱ میلادی ثبت شده (اتیمانلاین؛ ویکی‌واژه نخستین کاربرد را از متیو پرایر می‌آورد) و از فرانسویِ bronze وام گرفته شده است. در انگلیسیِ میانه میان آلیاژ مس‑قلع و مس‑روی فرق نمی‌گذاشتند و هر دو را bras می‌نامیدند؛ از همین رو به واژهٔ تازه‌ای نیاز افتاد. فعل bronze «به رنگ برنز درآوردن» (دههٔ ۱۶۴۰) از bronzer فرانسوی آمده است. گره نورایی از نظر صورت، معنا و مسیر درست است؛ ارجاع AHD به خودِ فرهنگ است نه به پیوستِ ریشه‌های هندواروپایی، چون واتکینز برای این واژه مدخلی ندارد (واژه‌ای سرگردان و فرهنگی است، نه میراث هندواروپایی).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronze\",\n            \"https://en.wiktionary.org/wiki/bronze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"Nourai cites AHD bare, i.e. the dictionary body. The local copy is Watkins's Indo-European Roots appendix (AHD_watkins1985.txt), where 'bronze' occurs only in prose remarks under ayes- ('A metal, copper or bronze. Latin aes… [Pok. aios- 15]') — there is no root entry for bronze, as expected for a borrowed culture-word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 203 s.v. bronze\", \"stance\": \"supports\", \"note\": \"'bronze, n. — F., fr. It. bronzo, bronzino, ult. fr. Persian birinj.' English from French, and Klein even endorses the Persian ultimate origin.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Bronze (SKT.txt line 2332)\", \"stance\": \"partial\", \"note\": \"'Bronze. (F.-Ital.-Teut.) See Brown.' — same French/Italian route into English, different ultimate source.\"},\n            {\"src\": \"FSD\", \"where\": \"s.v. bronze (FSD_vol1.txt lines 50531-50535)\", \"stance\": \"partial\", \"note\": \"'bronze, n. 1. A reddish-brown alloy of copper and tin…' with the etymology '[F., < It. bronzo, brass, < brown, < OHG. brūn]' — the English-from-French step confirmed, the origin disputed.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T06:09:27.313Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-77.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T06:09:31.567Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-77.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 77",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T06:09:33.610Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'plausible': 4}
root verdicts: {'transcription_suspect': 1, 'plausible': 1, 'disputed': 1}
ref checks: {'not_checked': 6, 'supports': 2, 'partial': 2, 'not_found': 2}
books consulted: {'supports': 18, 'silent': 5, 'partial': 6, 'contradicts': 2} | by book: {'LKT': 5, 'MON': 4, 'SKT': 3, 'KLN': 3, 'PHD': 2, 'BQT': 2, 'SOD': 2, 'FSD': 2, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'CHEUNG': 1, 'BRT': 1, 'FRS': 1, 'HUB': 1, 'LAT': 1}
```


## [2026-09-05T06:09:54.953Z] AGENT

Page 77 (book p. 47) verified — `data/verification/page-77.json`, `verify_check.py 77` reports 0 PROBLEM lines.

**Counts** — 3 non-redirect entries, 10/10 nodes. Node verdicts: 6 confirmed, 4 plausible. Root verdicts: 1 transcription_suspect, 1 plausible, 1 disputed. Ref checks: 2 supports, 2 partial, 2 not_found, 6 not_checked (AEF, PRT, SLW have no accessible copy). 31 `consulted` entries across 16 books.

**Flagged**
- **ROOT `Batiaxě` (transcription_suspect, error_in: book)** — Horn p. 36 no. 155, Nourai's own source, cites the Greek **βατιάκη** (Athenaeus XI); the book prints "Batiaxě" with *x* for kappa. Verified on the printed page (copied to `data/verification/sources/refs/ocr/BOOK/77.png`) — the extraction is faithful, the misrendering is Nourai's. Also the label: βατιάκη is Greek reported as Persian, not attested Old Persian; the modern antecedent is OP *bātah < Akkadian baṭû.
- **ROOT `Berenža` "brass" (disputed)** — no such Avestan word. HRN:48 (the cited page) says the opposite: "Zusammenhang mit aw. bərəǰya- … ist durchaus unsicher"; Hübschmann §209bis "Wohl Fremdwort im Iranischen"; modern view (Wiktionary/EIr): NP berenj < MP brinǰ / Man. MP brynng, Parth. plinǰ, onomatopoeic. Nourai promoted Horn's explicitly rejected guess to a root box.
- Root `Bazda` (plausible) — Av. bazda- is real but means 'afflicted, diseased' (ppp. of ban-, Bartholomae; Cheung *ban); "bad, sin" is the Sogdian sense. Nourai faithfully follows Gharib, who does write "< Av. bazda".

**Notable positives** — SOD:18 is exact (Gharib entry 464, printed p. 18, on the page-number markers). BQT:1485 is exact (vol. 3 pdf p. 278 per the pagemap): Mo'in's footnote derives فژ from Sogdian ʾβž and cites Henning BSOS X/1 pp. 101–102, i.e. Nourai's SLW:101. Lokotsch no. 1657 independently gives the whole Persian → mlat. bronzium → it. bronzo → fr./engl. bronze chain.

**Weak links inside otherwise sound nodes** (not separately flagged): پاتیله in entry 0 node 2 has no etymological support in any source consulted (Dehkhoda/Mo'in give meaning only) — the node is `plausible` on the strength of باده/بادیه; and فژاغند in entry 1 node 2 is called by Henning (via Mo'in, p. 1486) a تصحیف of فرغند.

**No extraction errors found** — the JSON matches the printed page throughout, including the doubtful "Batiaxě".
