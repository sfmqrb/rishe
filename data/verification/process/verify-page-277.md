# Verification process log — verify-page-277


## [2026-09-06T21:15:59.456Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 277 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-277.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-277.json. Write /home/sfmqrb/git/rishe/data/verification/page-277.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 277` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:16:00.943Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T21:16:01.656Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:16:01.670Z] TOOL RESULT

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


## [2026-09-06T21:16:01.919Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-277.txt"
}
```


### [2026-09-06T21:16:01.940Z] TOOL RESULT

```
1	=== PDF page 277 (book page 247) ===
2	--- entry 0 ---
3	ROOT [Arabic] K.r.v : a ball, sphere  (refs FVA:350)
4	#1 (parent #0) [Arabic] refs=FVA:350 | koreh : sphere, planet, ball
5	  #2 (parent #1) [Persian] refs=FVA:350 | koreh «کُره» : sphere, planet, ball | extra: کُرات
6	    #3 (parent #2) [Arabic] refs=FSD:1312; PLA:85; AFM:39 | jarrah : a round glass or earthen vessel
7	      #4 (parent #3) [Persian] refs=MON:1226 | jarreh «جَرّه» : jar
8	      #5 (parent #3) [French] refs=PHN:217; AHD:701 | jarre : jar
9	        #6 (parent #5) [English] refs=FSD:1312; TYL:568 | jar : vessel
10	--- entry 1 ---
11	ROOT [Sogdian] K`s : pig  (refs SOD:186; SLW:99)
12	#1 (parent #0) [Persian] refs=BQT:1563; SLW:99 | kâs 2 «کاس ۲» : pig | extra: کاسموی
13	
```


## [2026-09-06T21:16:04.966Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-277.json",
 "description": "Read source JSON for page 277"
}
```


### [2026-09-06T21:16:05.003Z] TOOL RESULT

```
{
  "pdf_page": 277,
  "book_page": 247,
  "entries": [
    {
      "root": {
        "name": "K.r.v",
        "lang": "Arabic",
        "refs": "FVA:350",
        "gloss": "a ball, sphere"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:350",
          "words": [
            {"translit": "koreh", "gloss": "sphere, planet, ball", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:350",
          "words": [
            {"translit": "koreh", "gloss": "sphere, planet, ball", "script": "کُره"}
          ],
          "script_extra": "کُرات",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FSD:1312; PLA:85; AFM:39",
          "words": [
            {"translit": "jarrah", "gloss": "a round glass or earthen vessel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:1226",
          "words": [
            {"translit": "jarreh", "gloss": "jar", "script": "جَرّه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "French",
          "refs": "PHN:217; AHD:701",
          "words": [
            {"translit": "jarre", "gloss": "jar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "FSD:1312; TYL:568",
          "words": [
            {"translit": "jar", "gloss": "vessel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "K`s",
        "lang": "Sogdian",
        "refs": "SOD:186; SLW:99",
        "gloss": "pig"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1563; SLW:99",
          "words": [
            {"translit": "kâs 2", "gloss": "pig", "script": "کاس ۲"}
          ],
          "script_extra": "کاسموی",
          "note": null,
          "quote": {
            "text": "اندر کَفَش آن تیغ درخشندهٔ شب داج - گفتی تو که یَشک از زفر کاس برآمد",
            "poet": "Ezzeddîn Tabasî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-06T21:16:07.225Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','FSD','PLA','AFM','MON','PHN','AHD','TYL','SOD','SLW','BQT','HRN','HUB','KLN','ARY','WEB','SKT','LKT','DEV','DOZ','LAM','POK']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-06T21:16:09.062Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
TYL {"title": "W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII), Oxford 1933", "edition_found": null, "kind": "hathitrust_fullview", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4089843 (S.P.E. Tracts nos. 31-40 bound volume incl. Tract XXXVIII, rightsCode pdus = full view in the US; record 000519279) ; mdp.39015005310308 (nos. 36-58) search-only", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_202108)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt", "page_offset": "Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles ke
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
```


## [2026-09-06T21:16:23.419Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -100; echo ---; ls incoming 2>/dev/null | head -50",
 "description": "List local reference files"
}
```


## [2026-09-06T21:16:23.437Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:16:23.477Z] TOOL RESULT

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


### [2026-09-06T21:16:23.483Z] TOOL RESULT

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
---
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-06T21:16:31.622Z] TOOL CALL #7: Bash

```json
{
 "command": "pdftoppm -f 277 -l 277 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg277 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 277"
}
```


## [2026-09-06T21:16:32.923Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep k's pig ===\"; grep -n -i \"pig\" SOD_pages.txt | head -40",
 "description": "Grep Gharib Sogdian dictionary for pig"
}
```


### [2026-09-06T21:16:33.753Z] TOOL RESULT

```
total 19120
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:16 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     374 Sep  6 17:16 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
```


### [2026-09-06T21:16:33.796Z] TOOL RESULT

```
=== SOD grep k's pig ===
17036:                                                                         pork, pig
17369:                                                                dove, pigeon
17973:              kun    (qwn-, kr-, qr-) ®<*krnu; OP kunau                        pigeon,
34029:        p277; Frag. Len. 27.4; Hen. JRAS 1944,                     wispiGre, wispase (wyspy8r}y, wysp5ry)
39090:0<?)pass away        4024                perfection  1655, 1659, 2388, 2390,       pig 46664794, 5031
39091:                                                                                   pigeon
```


## [2026-09-06T21:16:37.837Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17020,17050p' SOD_pages.txt",
 "description": "Context around pork/pig in SOD"
}
```


### [2026-09-06T21:16:37.882Z] TOOL RESULT

```
         TSP 5.75; Frag. Len. 71, 8                                       ©post
                                                                          suffix position with inf.
    4645 k'm'nty -* k'm'ntk                                               GMS 932f; BSTBL, Dhu. 81, Dhy. 56 etc. p96
    4646 k'mS'r- S *=» k>m-
                                                                    4663 .-k'ry -» -k'r'k
    4647 q'md'r- C ■* k>m-
                                                                    4664 -q>ry -* -kVk
    4648 q'mp C =» qmp                                              4665 k'rykV S                               jj<^</X
    4649 k'n B, M                                jL»&JJj f *^>-
                                                                         karekar
           kan =»kJm\ -q>                                                worker
           future particle
                                                                          MDii, A-9R3, p96.3; Gersh. Advice. 85
           GMS 646-50
                                                                    4666 k*s B, M, S          (^^(T^iT          :J-^S)Sy~
    4650 k'n'kh      B °* k'z'kh                                         kas (q's) ©Khwar. k*s ©ob. -y(y)
                                                                         pork, pig
    4651 q'ny* M                        (UT;J^)^l^bU
         kanya                                                           TSP 3.138, 9.44, 13.17; SCE 88, 122, 141, 360;
         stupidity                                                         Anc. Lett. 3.24, BBB f8, 766; GMS 822, 1683;
         BBB 716                                                           Hen. LW 99; Frye 2
    4652 k'p B                                        <*io3 t AX7
         kap?                                                       4667 q's C =» k's
                                                                    4668 k's M                                         j£&
         piece                                                           kas ©Parth. k}$
         TSP 3.180; Hen. Texts. 728; k>p\ TSP 3.196                      Kashghar
    4653 k'r S -» »ztk>r                                                 Sogdica. 8.10
    4654 -kVk            («jf» i^J» J.>U.)«»ju^» ^a, ju^            4669 k's'k B, M, S                             ^jjtf
         kare (-k'ry, -q'ry, -k}rk, -qry) ©<*kdraka                      kase (k'sk)
           ©f. -q>ra suff. =*-kr>k                                       (//ww)Kashghar
         making, doing                                                   Sogdica. 8.10c, n p!0; GMS 1048; MDii; TSP
```


## [2026-09-06T21:16:38.853Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"4666\\|4794\\|5031\" SOD_pages.txt | head -30",
 "description": "Find SOD entries by number"
}
```


### [2026-09-06T21:16:38.901Z] TOOL RESULT

```
17034:                                                                    4666 k*s B, M, S          (^^(T^iT          :J-^S)Sy~
17365:     digging                                              4794 kp'wt'ych B                                   j^S
17969:                                                                         5031 qwpwtyc C                                         j^f
38074:dispute 74, 334, 9aG, 993, 1 194,      dove     4794, 4805, 5031               duration    1577
39090:0<?)pass away        4024                perfection  1655, 1659, 2388, 2390,       pig 46664794, 5031
39167:pork 4666                                presented    2599                        protection    1175, 1176, 3417, 6542,
```


## [2026-09-06T21:16:46.468Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=17034 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<17034' | tail -3; echo \"=== after ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1>17034' | head -2",
 "description": "Locate SOD printed page for entry 4666"
}
```


### [2026-09-06T21:16:48.212Z] TOOL RESULT

```
=== after ===
```


## [2026-09-06T21:16:48.283Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kās\\|k’s\\|kas\\b\" HENNING_selected_papers.txt | grep -i \"pig\\|swine\\|schwein\" | head; echo \"=== search 'Sogdian Loan-Words' ===\"; grep -n \"Loan-Words in New Persian\\|Sogdian Loan\" HENNING_selected_papers.txt | head",
 "description": "Search Henning selected papers"
}
```


### [2026-09-06T21:16:48.348Z] TOOL RESULT

```
=== search 'Sogdian Loan-Words' ===
```


## [2026-09-06T21:16:52.689Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD_pages.txt SOD.txt HENNING_selected_papers.txt; echo \"=== SOD head ===\"; head -5 SOD_pages.txt; echo \"=== formfeeds SOD_pages ===\"; python3 -c \"\ns=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff',s.count(chr(12)))\ni=s.find('4666 k*s')\nprint('idx',i, 'leaf', s.count(chr(12),0,i))\n\"; echo \"=== HENNING head ===\"; head -30 HENNING_selected_papers.txt",
 "description": "Inspect SOD and Henning files"
}
```


### [2026-09-06T21:16:54.617Z] TOOL RESULT

```
  45615 SOD_pages.txt
 111423 SOD.txt
  25027 HENNING_selected_papers.txt
 182065 total
=== SOD head ===
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


=== formfeeds SOD_pages ===
ff 644
idx 1336757 leaf 251
=== HENNING head ===
 
 
 
 
ACTA IRANICA
DEUXIEME SERIE
VOLUME VI
 
                                      
SOUS LE HAUT PATRONAGE DE S.M.I. LE SHAHINSHAH ARYAMEHR
ACTA IRANICA
ENCYCLOPEDIE PERMANENTE DES ETUDES IRANIENNES FONDEE A L'OCCASION DU 2500" ANNIVERSAIRE DE LA FONDATION DE L'EMPIRE PERSE PAR CYRUS LE GRAND
 
DEUXIEME SERIE
HOMMAGES ET OPERA MINORA
Acta Iranica 15
BIBLIOTHEQUE PAHLAVI E, J. BRILL TEHERAN-LIEGE LEIDEN
HOMMAGES ET OPERA MINORA
W.B. HENNING SELECTED PAPERS
Tt
EJ. BRILL BIBLIOTHEQUE PAHLAVI LEIDEN TEHERAN-LIEGE
 
 
COMITE INTERNATIONAL
Prof. Sir Harold Bauey (Grande-Bretagne); Prof. George CaMERon (EU): §, Exe, Prof. Enrico CeRULLI (Italie); tS. Exc. Dr Tara CHAND (Inde); Prof. Henri Conny (France); Prof. Jacques DUcnesne-Guniemin (Belgique): Prof. Namio Eoas (Japon); Prof. Dr, Wilhelm
S. Edman Enzi (Turquie); Prof. Richard ErmicHausen (E-U,); Acad BG. Garunov (URSS):
Garcia Gomez (Espagne); Pr Walther Hinz (Allemagne); Prof. Yat Dr. Franz Konia (Autriche): Pr
S. Nvaexc (Suéde); Pir Husams
```


## [2026-09-06T21:17:03.461Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"loan-words\\|loanwords\\|Lehnwör\" HENNING_selected_papers.txt | head -20; echo \"=== toc ===\"; grep -n -i \"BSOAS\\|Bulletin of the School\" HENNING_selected_papers.txt | head -20",
 "description": "Look for Henning's Sogdian loanwords article"
}
```


### [2026-09-06T21:17:03.519Z] TOOL RESULT

```
1094:rixo 'kdn’ (but Syr. loan-words in Tranian usually have -d).—(11) " Astrologers," of. Nyberg, i, p.7, and Buddh. snp(r VJ, 22, 27, 69, 9, 12%, sq., SCE., 264, I should like to take this opportunity to explain a Sogdian word from a closely related sphere namely mySBy, pl. myBBt’ (NB. a “Ii toRosnberg, I
3649:'y or yy in Jewish type of Aram by Mani, Rel. of the Man, pp. 111199.) Ha loan-words-'y replaces Aram. ay, ane.g. in remy, Of, also Man, MPeorn. mgin'yi’n * Menenians'” = mdindy-ip.An with a Persian suffix (os in Publ, HRWAMDYK) ; in Pal. both forms ocear: myln'y Pall, Vil, 1, and myindyl'n, Gr, 207%
11133:Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
11770:milar Sogdian loan-words in Pe nd-wif, ete,
12201:and classical spelling is p'askwn|i alone.—The following two are loanwords
12482:Pazend, e.g, SGV., xvi, 25, 38 loanwords in Aramaic that ap Tn the homilies of Aphraat
13264:). ‘There are forms with & and s, Persian d6r(-), but Bakhtiari str (Lorimer, p. 69), Gabri of Yexd sir (Lorimer, JRAS., 1916, 437), Baluchi sir, Brabui sbr, and last but not least Pahlavi sir. ‘The word is unknown to Oh to be restricted (loanwords from Persian excepted) to the area of Persia and Baluchistan. Could it belong to a substrate language and be connected with Dravidian ‘ewoar (Gondi savor, GondiM. hovar “salt, Tatil, Malayalam wear * salt quoted by T. Burrow, BSOAS., XI, 352) has the common Iranian na/imadka (Sogdica, 8, and Add.; na/imadka cannot ed) ; a8 nmydk it occurs in M 377 R 5. In additio nd for “salty” in Parthian, sol = wal! Th
20591:loanwords in Armenian, which entered Armenian from the of Azerbaijan, prove the existence of these changes. Now the first, hr from fr, is satisfactorily
21147:As confusing as the treatment of 8r and fr is that of postvocalic =f It remains in a few words, pethaps throughout loanwords, pw «cat», pupiyk «hoopoe» (Pers. pipas), ’Swk «target» (cf. Arm. néavak?), but normally becomes -s, €. ‘ws «attention» Ows «intelligent» (Ba- + ‘ws), etc.; ef. also sry «lion» for initial
23150:changed, but did so without system and allowed adequate representa tions of current speech to stand beside antiquated forms. The Middle Persian disguise is sometimes so perfect that only an occasional Arabic word betrays the true character of the language. The word for “and”, pronounced 1, is still written ‘wd (23!), the Idafe-particle f appears as ‘yg (St) or 'y, the abstract ending -Fia -yh or singular of presents ends in -yd but was pronounced in ~dd (or perhaps ~éd), words in final -e and -d are still spelt in -g and ~'g, and this on ‘occasion even affects Arabic loan-words, e.g. jomlg—alax. Influence of Sogdian orthography may be detected in x’n'g “house” (for the expected x’ng), kten’nd “they do” (beside heennd), stos'ndg “burning”, and the like. Quite modern forms abound, e.g. 2-, in st, a'ym ‘from beside "c (and 'z) “from”, j’y or j’ “place"* (MPers, beside 'b'g, K’—ke for MPers. ka, ku, and hé, etc In metrical passages the spelling takes little notice of the form of the words required by the verse: the metre is not meant for the eye
=== toc ===
75:Compte rendu de E. Hexzreto, Archaeologische Mitteilungen «us Iran (BSOAS, 1940. pp. 501-507) 1 Compte rendu de A. Guitatn, Essai sur la langue parthe (BSOAS, 1940, pp. 508-509) 7%
76:Mani’s Last Journey (BSOAS, 1942, pp. 941-953), 81 An Astronomical Chapter of the Bundahishn (JRAS, 1942 pp. 229-248) 95
79:ants (BSOAS, 1943, pp. 52-74) Ms
81:The murder of the Magi (JRAS, 1944, pp. 133-144) 139 The Disintegration of the A vestic Studies (TPS, 1942, pp. 40-56) 151 Sogdian Tales (BSOAS 945, pp. 465-487) 169 Brihman (TPS, 1944, pp. 108-118) 193 The Manichaean Fasts (JRAS, 1945, pp. 146-164) 205 Waruéiin-Sih (Journal of the Greater India Society, 1945, X1/2,
84:The Sogdian Texts of Paris (BSOAS, 1946, pp. 713-740)
86:Two Manichaean Magical Texts, with an Excursus on the Parthian ending -éndéh (BSOAS, 1947, pp. 39-66) 273
87:A Sogdian Fragment of the Manichacan Cosmogony (BSOAS
91:1948, pp. 306-318) 301 The Date of the Sogdian Ancient Letters (BSOAS, 1948,
92:pp. 601-615 MS The Aramaic Inscription of Asoka found in Lampaka (BSOAS.
94:pp. 158-162) 341 ‘Okt5(u) (TPS, 1948, p. 69) 347 A Pahlavi Poem (BSOAS, 1950, pp. 641-648; p. 809) 349
99:A Farewell to the Khagan of the Aq-Aqatirin (BSOAS, 1952, pp. 501-522)
105:The Middle Persian word for “beer” (BSOAS, 1955, pp. 603- 604)
111:Surkh Kotal (BSOAS, 1956, pp. 366-367)
113:The inscriptions of Tang-i Azao (BSOAS, 1957, pp. 335-342)
114:A spurious folktale (BSOAS, 1958, pp. 315-318)
115:New Pahlavi inscriptions on silver vessels (BSOAS, 1959, pp. 132-134)
128:The Bactrian inscription (BSOAS, 1960, pp. 47-55)
130:nian silver bow! from Georgia (BSOAS, 1961, pp. 353.
146:A Bactrian seal-inscription (BSOAS, 1962, p. 335)
152:A Sogdian god (BSOAS, 1965, pp. 242-254)
```


## [2026-09-06T21:17:04.656Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -rn \"کاسموی\\|كاسموى\" . 2>/dev/null | head -20",
 "description": "Grep kāsmūy across refs"
}
```


### [2026-09-06T21:17:04.773Z] TOOL RESULT

```
FRS_pages.txt:21514:                                  ‫کاسموی‬
FRS_pages.txt:21517:‫چو کاسموی کیاهان اوبرهنه زبرك چوشاخ بید»درختان‌او تهی‌از بار]‬
FRS_pages.txt:21535:  ‫‪- ۳‬لن ‪:‬کاسموی موی گر از بودکه کفشگران بدان‬
FRS_pages.txt:21536:     ‫‪- 4‬ن ‪:‬رنگ‬      ‫چیز دوزند » چ ‪:‬کاسموی سبیلگراز باشدکهکفشگر ان دارند‬
MON_part2.txt:18220:کاسموی: ۷2-۷ [- کاسموء کاس 
FRS.txt:19313:کاسموی 
FRS.txt:19317:چو کاسموی کیاهان اوبرهنه زبرك چوشاخ بید» درختان‌او تهی‌از بار ] 
FRS.txt:19328:۰ درنسخه اساس و حاشهٌ ن .۰ ۳ -لن :کاسموی موی گر از بودکه کفشگران بدان 
FRS.txt:19331:چیز دوزند » چ :کاسموی سبیل گر از باشد که کفشگر ان دارند 4 -ن :رنگ 
incoming/BQT/BQT_v3_pages.txt:25904:‎EBS ‏است . درفارسیکاسموی ( موی زير ) آعده [ ره :کاسموی [ : بنظر میرسد‎ 1*5 cane
incoming/BQT/BQT_v3_pages.txt:25905:‏«کاس» بالانفراد هرز در فارسی استعمال نشده باشد . لفت توبان ناگزیر از «کاسموی» کلمه‌لی‎
incoming/BQT/BQT_v3_pages.txt:25912:. ‏عزالدین طبی . « جپانگیری»رك: کاسموی‎
incoming/BQT/BQT_v3_pages.txt:25939:پشت کلان ‎alg‏ باشد . کفته‌اندموی‌سیات‌روباماست؛و آنرا کاسموی
incoming/BQT/BQT_v3_pages.txt:25960:‏مصفر «کاس © ۵ قي : کاسانه . 1 -«کاسموی» موی خوه‎ - ۴
incoming/BQT/BQT_v3_pages.txt:25962:‏چوکاسموی گیاهان او برهنه زب رکه چو شاخ بید درختان او تهي از بار.»‎
incoming/MON/MON_2vol_Adena_v2_djvu.txt:18220:کاسموی: ۷2-۷ [- کاسموء کاس 
ocr/BQT/1564.txt:11:پشت کاان تیرانداز باشد . کفته‌اندموی‌سبات روباماست؛وآ نرا کاسموی
ocr/BQT/1564.txt:26:۴ - مصفر «کاسی >. 8 -_قی : کاسانه . ۹ ۶ کاسموی, موی خوكد
ocr/BQT/1564.txt:28:چو کاسموی گیاهان او برهنه زی رک چو شاخ بید درختان او تهی از بار.»
```


## [2026-09-06T21:17:12.809Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11125,11145p' HENNING_selected_papers.txt",
 "description": "Check Henning article start at line 11133"
}
```


### [2026-09-06T21:17:12.851Z] TOOL RESULT

```
thi article and Kily adding the index
 
 
                                                                                                   
TWO CI
 
NTRAL ASIAN WORDS
 
Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
| pursuits, Such words, passed on
 
 
changes; but th rignifica- tions. So the me the leas we should arrogate to ourselves in the matter of
y possess very precise and limit e latitude we may claim in regard to form,
   
 
A. Dawasx Niya th twice a word prigha (Nos, 316, 318) which Liders, Teztilien ten Turkistan (Abh.P.A.W., 1936), p. 30, combined with Skt. priga in the Mahdeyutpatti, & Hi" thin flowe with figures”, In Doe. No. 318 (line 6) Liders corrected the text given by B speta-prigha“ whi which we shall be able to confirm with fresh n that prigha meant “‘unicoloured figured silk (= damask)” ean be fully sub-
In the Kharogthi documents found
```


## [2026-09-06T21:17:13.657Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kas\\b\\|kās\\|«kas»\\|swine\\|Schwein\\|\\bpig\\b\" HENNING_selected_papers.txt | sed -n '1,60p'",
 "description": "Grep Henning for kas/pig"
}
```


### [2026-09-06T21:17:13.709Z] TOOL RESULT

```
4012:‘The king rose from the table,? and putting one arm round the Queen of the Sakas ¢ and the other round Kerdér * the son of Ardawan, he came towards the Lord, His first words to the Lord were: You are not weloome.* ‘The Lord replied: what wrong have I done! The king said ; I have sworn not to let you come to this country.’ And in anger he spoke thus to the Lord: Eh, what
4075:plr’s inscription.* That the king who appears in the fragment M 3 was Bahram 1° (and not Shapur, as assumed by F.W. K. Maller and others) is proved by the unfriendly tenor of the whole conversation, The Sakdn-Banbisn, “Queen of the Sakas,” who also participated in the conversation, was the wife of the then ruling Sakén-Sah, or prince-governor of the south:
5335:(Pig. 9, fst page) (7H)}'y nf... 00 aly ky pa y(t} 7B) yHtyd 00 n'y ky pd sewn r's(tXt
5495:(Pig. #) ... father ... nuptial (2)... until the completion of hin... in fighting ... (60) .., and in the nest(?) Ohya and Ahya .., he suid to his brother: “get up and ,.. we will take what our father has ordered us to. ‘The pledge we have given ... battle.” And the giants ... together... (67) [Not the] ... of the ion, but the ... om his... [Not the)... of the rainbow bout the bow ... firm. Not the sharpness of the blade, [but] (70) the strength of the ox (t).® Not the .... eagle, but his wings.!! Not the ... gold, but the
6050:(23) 'w ‘ym ambwdyg ‘dwr 00 "ws wa8 (2 ) tnb'r o0 'w b'yn “dwr od ) yd oo by cw'gwn dw be'de'n (28) ky fre{'w] wynd'd oo "wd pig mrd 00 (29) (‘yw pt byd] ‘ng’f'd "wd mwrd (30) [/hynd] 00 w’gwn ’why’ Iwy'tyn ng'f'd 00 ‘wd ‘pyd "bynd 00 ewgwnte(33)
11218:as a zndp'iyk = song-hymn ; its last lines are spytyy prymg myrcBn Garment of white damask, Brrvy mpyk "t By book in the hands Sryy 2'r wftyy kwrd'k Three thousand woven jackets, uynk'h 00 ive thousand ziinkas,
11268:4 ‘wed bueyyst'n 0 "vad pig an "rod
12662:akyatras: yakas Tn employing such of charms, the M Mahiimiyasi
13227:C8; for Kad be propeses with a fine displ int first Cutch, then Kashnir, then Kid, deciding himself in favour of the last. He takes it for granted that the Inst Grock word was dpéy. With this T cannot agree. We should read xal Zag Kas Debucweije xal Tow Spe — Parthian wd yp 5 Kat Suyd wil Os (- astan) (wimand), The boundary of Kid wan the
13687:raft kas eto, “api-d sast etc. api-din dit api-é avéidn af to, = et un tel. se renit i,t maitre... ot it le leur donna it leur downas la bénédiction en disont ..  e iit deur obuvar . ... With regan
13760:wader against the misreading kas by adding Zag az yazan “one jen"; but his name should be familiar to all students of the
17750:the Sien-pi and the T'u-yi-hun (a branch of the Sien-pi) The dominion of the Sien-pi (about 4.p. 155-402) was confined to Mongolia and never extended to the ares of Chinese Turkestan, which, however, was subjected to raids b ‘T'w-yi-hun, who on one o Khotan ; whether the Persians, by the end of the Srd century, bad ever heard of either may well be doubted. Nevertheless, as we know now that Sassanian rule, u “to the limits of Kas = Kashghar was constantly transmitted fre
17901:event under Khosrau i (4.b. 581-678); yet all its undisputed references * are 50 vague that they may well be proleptic. Of far greater, indeed decisive, {importance isthe list of Hunnic nations in the appendix to the Syriae Chronicle ascribed to Zachariah of Mitylene *; the relevant part of this appendix, which i.e. at the beginning of the Turkish e before it had any effect on the neighbourbood of the Caspian Sea, is based on reports of returned prisoners of war in contact with Albanian missionaries who had laboured to the north of the Caucasus 20 to 30 years earlier.* One of the names in this list is KSR = Xasor (or Xasir)* evidently an early form of t Marquart,” not without justification, identified the name (which he transeribed Kas()r) with "Ancr{ipot, no doubt on account of the company by which ASR is surrounded: Lapéyoupot, "Ovéyoupor, "Irivapos, ete. The truth of the matter is that here, where the historical context leads us to expect the "Andérfipot, we find them under a new name, Xasar (Xasir); the list thus provides tho sought-for link between the two national names.
18308:Even though we readily concede that the Greek translator of the inscription saw in Sykn some insignificant little district on the Black Sea coast, we are far from submitting to his judgement. To interpret this Persian inscription, an official document of the first rank, from the Greek version that accompani in a capital mistake. In claiming that Sykn is la Mingréie, que le nom désigne comme wn pays de Scythes (Saka) th gifted young scholar runs into difhiculties ; for neither the Mingrelians nor the Machelones have ever been, or could ever have been, described as * Sakas’, which name, needless to sty
19936:know’, bitkas ‘look’ [imp.], 4 * you should go) two differ materially from the forms I received, in which the first person of the singular ends in ~im and the first person of the plural in nt in Takista nda.
21212:A brief list of some interest may conclude this survey, which, it is hoped, will afford some guidance to those who may wish to study the Khwarezmian material contained in the Mugaddimatu -l- Adab. «Paradise» is yrdm'n, «hell» tm- (as in Sogd.), “shnd'rmd «earth», Byk, ‘Byyk «doll» (from «god; cf. Pers. fig), “rd «feast» (AY. ratu-; Beruni has ryd). K's «pig» (Sogd.), p’@ «arrow» (Asica 11), pdryk «slate» (Sogd. pyd'r, S. T., i), mand- negative prefix as in Sogd. (nindm’nynd «dissimilar», mndeyr «blunt», mnd’ktrm'n «disobe- dient»); robs «fox», ‘bd 1) «silk», 2) «woot» (Sogdica 19), p'rd- sell», tiyckyk «axe» (Sogd. tiyeq), wyryk «saw» with worth «he with a saw» P 21, iii, 3; 61 wyr’, S. T., : w'nnyk «royal faloon» (Av, and Sogd,), mrk «monkey» (Sogd. mkr’), drmeyk «scorpion » (from drmad- ef. Sogd. nyrdf"k from drdab- and, from drdam-, Pasthto laram, Pers. dilamak), yrbk «neck» (Sogd. yrS'kh). byrBk «cloud» (Sogd. pr'yf’k), *ks «lean» (Sogd.). Knbynk «linen» (Sogd. kynp’, cf. BSOAS. xi 724), wyn ass» (also Sogd., Pers. gar). K'm «mouth» (Oss. kom), ‘m'ny- «guide, show» with intrans. m'm'nsyd «he was guided» (Oss. amonin), n'rk «narrow (Oss. nareg, Psht. narai), ‘le «top of the spindle» (Oss. dlxui excludes etym. Asica 36), pdyk «large axe» (from p(a)rt-, ef. Asica 13), rsy «barley» (Saka rrusd- etc.). Spdyr «mule» (Pers astar, but Sogd. yrir-), mr'w «date» (Parth. ‘mr'w), ywndyk «sin » (Parth. gwyndg), Bir «cup», ‘Byw-, trans. ‘fy’
21387:Now, however, Professor Henning, relying on a Turkish Manichaean colophon in which the year 522 after the death of Mani is counted a8 a “pig-year"’* has become persuaded that the year of the death was 274 and the day Monday, March 2 (corresponding with the fourth of the Babylonian Addaru); the aforesaid scholar supports this view chiefly by stressing that all other conclusions are built on conjectures, inferences, and calculations,
21551:To come now to the equation, in the Turkish colophon, of the year “522 after Mani’s death” with 2 "‘pig-year", which Henning regards as the sole and principal authority in the question of Mani’s death-date, and which would require attributing the death to the year 274: even if one cannot consider it totally unworthy of attention, it cannot, in my view, have decisive force in the face of the numerous contrary arguments. Firstly, the document is late, It is not at all unlikely that the authors of the Turkish manuscripts made mistakes in identifying non~Turkish years with Turkish ones, especially if they were accustomed to using Sogdian or Persian years and dates (or others, except Chinese ones). An example of this sort of mistake can be seen in a Manichaean Uigur calendar-fragment,! where the Yeadegerdi year 358 is described as a “mouse-year””, while in fact it was a “cow-year", with its last days in a “tiger-year” (perhaps the year 357 Yezd. had been intended). I referred to this circumstance in my Notes to Henning’s article on the Sogdian calendar-fragments.* In one of the last-named frag- ments, as I pointed out in the same Notes, the Christian year 985 is appar- ently identified with the year 388 after the death of Sad-Ormizd (if [xi] the figure 388 is s0 to be interpreted), whereas it should have been 384 or 385, 80 that a mistake of as much as three years has crept in; however, that the
23461:‘ah-t ke bar-ney-dyam az Juz gth-i! Sumar ~~~ air-i taxt furd x"abanand “mari kafir (u) barg-i mid kunand *rdy-i man ni@ar anbaz - -~ ~~ -ne juft-iJ® man kunand ~~~ siy-i man ne-dihand - bargalte ~~ —~~ az garf-i]* man pa-dard man air-i xik fard ne kas ~~ —» Awarde pul! suy-t "to! suy-1 rih-dide mard ~~~ i pa-xarpulte-i] zar-nihide® *xart yak bar yi do bir ~——kunand bas
24844:‘Schon lange hatte man sich um die in gewissen chinesisch-buddhisti schen Texten firden GroBkinig Kaniike bezeugte Bezeichnung Chan-tan Kia-ni-ch‘a bemit, bis os endlich H. W. Barry gelang", in einer skt.- hot. Bilingue dio Vorform cadra-kayaiskd (cadrra-Kiyaiska) aufcufin den, Er restaurierte die sanskritische Form als candra-kanigka und be- trachtete es im Hinblick suf ein schon fraher von F, W. Tomas ans Licht gezogenes Wortspiel mit 2la-ba ,,Mond"* im tibetischen Mahdrdja- Kanika-lekha als wabrecheinlich, daB candra im Sinne von ,Mond zu nehmen sei, Im Verfolg seiner Forschungen kam jedoch Bamxy von die- ser Meinung ab und erwog runichst akt. capda ,,gowalttitig'®t, spiter cinen iranischen Titel *éandan'. Jetzt aber, da die Namensform als *Maho-Kanetko ,Mond-K."" in KaniSkas Muttersprache vorliegt, wird
24859:© Dio Frage, warum Kaniikas Eltern ih una vielleicht selteam scheinende gaben, fuhrt aber die Grenzen des Widlbaren hinaus. Sic mégen ihn ala des Mondgottes' veratanden haben, aber wie kann man dergle
```


## [2026-09-06T21:17:22.850Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT_v3 around 25900 ===\"; sed -n '25890,25970p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Read BQT v3 kās context"
}
```


### [2026-09-06T21:17:22.911Z] TOOL RESULT

```
=== BQT_v3 around 25900 ===
باشد که عربان کذب میکویند.- وماضی کاستن
‎Se‏ بعنی کا هید وکم شد.

‏کاست ‎IT‏ ه با کان بالف کشیدموبرای
قرشت زده؛ دروغ کو برا گویند چه‌کاست‌بمعنی

‏۴ - کاجیره ‎Ape)‏
‏۴ هم او ریخت در طای حکمت زلال

‏هم او کوفت بر کاس دولت دوال .
امیرخرو دهلوی. « فرهنگه نظام ©

‏۴ - اسدی کوید ( لفت فری ص ۱۹۹ ): «کاس » خوك بود » و ‎KAS‏ همان‌کلمةءعمول

‎EBS ‏است . درفارسیکاسموی ( موی زير ) آعده [ ره :کاسموی [ : بنظر میرسد‎ 1*5 cane
‏«کاس» بالانفراد هرز در فارسی استعمال نشده باشد . لفت توبان ناگزیر از «کاسموی» کلمه‌لی‎
. ‏بمعنی « خوك » استخراح کردهاند وبی درنگ کاس را بمعنی خولك درفرهشگهای خود آورده‌اند‎
: ‏عبدالقادر ۱۹۸۳ » ور‎ : Dy) ‏و حتی مشکوك است که فردوسیکاس را بمعتی خولك گفته باشد‎
‏دائست که فردوسی فاعدة ازلغات مستعار ازابرانی شرقی احتراز میجوبد. اگر‎ wk ) ‏فهرست ولف‎
(Hentting, Sogdian 1088- . ‏داذه‌شده است‎ ous ‏چه بیاری‌ازآ نپا توسط عبدالقادر بدو‎
: ‏درین بت کای بمعنی مذ کور آمده‎ Jy ۷0۲05 ..., ۲.99 .)
. ‏درخشنده شب داج کفتی توکه بشك از زفر کاس برآمد‎ Got ‏اندر کفش‎
. ‏عزالدین طبی . « جپانگیری»رك: کاسموی‎
. ‏شراب خوردن با جام با شراب .» «منتهی الارب»‎ ple ‏کأس بالفتم‎ « (4) - ٩
‏ودارای"‎ (gle) ‏نهرسیحون و ورای شاش‎ shy ‏دراول بلاد تر کستان‎ Koy ‏شهری‎ - ۱
. » ‏استوار است و برباب‌آن وادی اضبیکث است . «معجم‌البلدان‎ clas
. ‏قن : کاسکینه‎ - ۴
‏چند؟‎ alle ‏مچندپوبی بگرد‎ A
‏زانکه از بهر قوت شپوت‎

‏چند کوبی طریق پوبایی ؟
همچو ‎GLO‏ می‌تناسایی .
عممق ‎sie‏ « لفت فرس 0۰۵ >

‎. ‏-رك : کاستن‎ ٩
[pdf page 357]
~\ert— ‏کاسته‎

دروغ هم آمده است #۰ کاسمو 1 = با میم ‎sly‏ کشیده‌بروزن
کاسقه ۱ » بروزن راسته » بمعنی نازبو » موی ‎Ay‏ نررا گوشد چه کاس پمعنی

شده وکاهیده(۱) ‎ath‏ . خوك نر هم آمده ‎Vet‏ - ورشته‌باریکی را نیز
‎wer‏ بضم ثالث وسکون‌جیم.خارپشت کفته اند که کنش ‎OLS‏ و موزه دوزان بر سر

aS ‏تیرانداز راگویند ۴ . سوزن کشند 139 بمان گنده‌ای را که بدان‎ OMT

کاسچو ‎FY)‏ = برکرن ‎SU‏ و جیم موزه‌دوزندبآآن ‎(aig.‏ کند؛ ‎ef aes‏
بواو کشیده ویکاف زده ۰ بمعنی‌کاسج است که‌خار سبلت خو ‎al Tye‏ بی‌هلب‌خوانند(۳)؛وبعضی

پشت کلان ‎alg‏ باشد . کفته‌اندموی‌سیات‌روباماست؛و آنرا کاسموی
کاساث ۴ - بتح نالت و سکون ‎Se‏ ,| با زیدنی تحتانی درآخی نیز میگویند

مصفر کاسه باشد. کاسن پروژن دامن . نام قربه‌است از
کاصطینه * - ‎oy,‏ آبکینه , مرفی | قرای سمرقند ۵ .

باشد سبز ‎Gy‏ بسرخی ‎bh‏ و آنرا سبزكك یز کاسفبی » بنتخ ناك‌ونون بتحتان‌رسیده.

کویند . تاجی بر سر دارد ‎atl‏ هدهد و پعرپی | مردمیرا کوبند که ‎ELA‏ متسوبند که

شفراق خوانند . قربه‌است از قرای سمرقند ‎A‏ - ویسکون‌نالث

(۱) خم۱ : + شده . (۷) خم۱ : ضب
(۳) چش : - موی سلت ... خوانشد .

: ‏اس مفعول ازه کانتن» ۲ ؟ - کاسسو‎ - ٩
‏همه اعضاش همجون پشت کاسج.‎ wk ‏بروی صف شده از زخم‎
> ‏روت نظام‎ vis oly ۱
: ‏ره : کاسج‎
‏پیجد دل من همجو ماری که‌هجرانش براو چون کاسجوكاست‎ OT ‏از‎
‎vt ‏نظام‎ Lan b> ‏مولوی‎
‏مصفر «کاس © ۵ قي : کاسانه . 1 -«کاسموی» موی خوه‎ - ۴
: ‏بو دکه کفشگران بررشته بندند . فرخی (سیستانی) کوبد‎
‏چوکاسموی گیاهان او برهنه زب رکه چو شاخ بید درختان او تهي از بار.»‎
=f 6۱۹ ‏فری‎ cal?

رك : کاس. آنچه درهندوستان رواج دارد آنست که موهای خولك را دسته ساخته کفشگران‌برای
جلای سقرلات و مخمل وچرم پیش خود نگاهدارند و همچنین زرگران برای جلای ‎Wh,‏ ونقرء .
« فرهنگه نظام ‎Ve‏ :کاس ‎A‏ -کاسن بفتح سین » ازفرای نخشب بماوراءالتهر
است «معج البلدان» و مولف با «کاسان» ‎Com)‏ خلط کرده است .

۰ کاستن ( بفتح چهارم) = کاهیدن.پهلوی ۵112۳ ۰ ۰20101120 بقولدارمتتر
```


## [2026-09-06T21:17:24.502Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON kasmuy ===\"; sed -n '18210,18230p' MON_part2.txt; echo \"=== FRS ===\"; sed -n '19305,19335p' FRS.txt",
 "description": "Read Mo'in and Loghat-e Fors kāsmūy"
}
```


### [2026-09-06T21:17:24.562Z] TOOL RESULT

```
=== MON kasmuy ===
ماهوت جون شالکی. 
کاسر: 2:۰ (ع.] (افا.) شکننده» قاطع. (پز. 
قد.) دردی است که صاحیش بندارد که 
عضو دردنا ک مر شکنن: عقاب کاسر: عقابی 
که وقت فرو آمدن پرها را فراهم آورد. 
کاسیک: ۷2:۰ (۱.) خودء کلاهخود» مغفر. 
کاشکت: 2۵۷ (۱.) کلاه مر دانه لبه‌دار. هر 
یک از انواع کلاه‌های لبه‌دار که سربازان بر 
سر گذار ند. 
کاسل: ۷2:۵ [ع.] (افا.) سست و کاهل. 
کاسموی: ۷2-۷ [- کاسموء کاس 
خوک + موی] (امر.) موی خوک که 
کفشگران و موزه‌دوزان بر سر سوزن کشند 
و رسمان گنده‌ای را که بدان کفش و موره 
دوزند بدان ببوند کنند. (مج.) موی زبر و 
خشن. 
کاسنی: 2۶ [- کاشنی ] (1.) (گیا.) گیاهی 
است عافی و پایا از تیرا مرکبان که در 
حقبقت سردسته این تیره است. ار تفاعش ین 
۰ ۵ ساأند تیمتر تا ۱ متر است و آن بر اثر 
کشت‌های متوالی تا ۲ متر نیز می‌رسد. ریش 
=== FRS ===
جلیبت بود و بارکی آفردوسی کوید : 
ز کین تند کشت و برآمد زجای ببالای جنکی در آورد پای 1 


باری" 
باريك بود [ عنصری گوید : 
رای دانا سر سخن ساری است نيك بشنو که‌اين سخن باری‌است ] 
۵ ۶ ۳ 
کاسموی 


موی خوك بود که کفشکران بر رشته بندند [ فرخی کوید : 
چو کاسموی کیاهان اوبرهنه زبرك چوشاخ بید» درختان‌او تهی‌از بار ] 
شاه بوی" 
عبر 1 باشد [رو کی گوید : 
بی قیمت است گر ازآن دو لبان اوی 
کاسدشد ازدوزلفش‌بازار شاه بوی ] 
‌ِ 
دار بوی 
عود بود [رود کی گوید : 
تا صبر را نباشد شیرنی شکر تابید بوی ندهد برسان دار بوی۷ 
کشفی گوید : 
۳ ۳ ۳ 5 7 
۰ درنسخه اساس و حاشهٌ ن .۰ ۳ -لن :کاسموی موی گر از بودکه کفشگران بدان 


چیز دوزند » چ :کاسموی سبیل گر از باشد که کفشگر ان دارند 4 -ن :رنگ 
۵ درنسخه اساس : سیاه روی ۰ 1ج ۰ عبر . ۷ - اط در چ 


9۳۰
```


## [2026-09-06T21:17:50.125Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM جرة ===\"; grep -n \"جرة\\|الجرة\\|جرّة\" AFM_pages.txt | head -20; echo \"=== PLA جرة ===\"; grep -n \"ǧarra\\|garra\\|jarra\\|جرة\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Addi Shir and Asbaghi for jarra"
}
```


### [2026-09-06T21:17:50.210Z] TOOL RESULT

```
=== AFM جرة ===
226:الأرض) ܢܢ فارس _يستى « طاق وطءك » 5 له ` ® ܐܢ̈ܕܐ وشجرة 3
567:* , 95 سُجرة تاكلها الناس والماشية تذ كرك ريح < وطعمه اذا
1530:دار شيشغان ٠‏ قال في البرهان القاطع : :دار ششغان شجرة 0( لا 06 17
1632:وهي العطية والاجرة المعطاة قبل العمل
3182:ܕܠܐ على الشجرة 03 حيدار في بلاد الماد ٠‏ وهذا الدود ܚ ܕ¦ܛܚܡܚ ܐ[
3478:زهو صمع شجرة توجد في اطراف سرانديب في بلاد الهند وهو انواع احستها | رياحي
3485:1ك كتج ).ضمغ شجرة متها مال عراد ين الل 300
3816:ܨ عر شجرة 0 و يم عاد ܐܒ وتفاحي مكلك انع
=== PLA جرة ===
```


## [2026-09-06T21:17:51.918Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol2 jar ===\"; grep -n \"^jar\\b\\|jar, n\\|Ar\\. jarrah\\|jarrah\" FSD_vol2.txt | head -20; echo \"=== PHN jarre ===\"; grep -n -i \"jarre\" PHN.txt | head -20; echo \"=== DEV jarre ===\"; grep -n -i \"jarre\" DEV.txt | head -10; echo \"=== LKT jarre ===\"; grep -n -i \"jarra\\|jarre\" LKT.txt | head -10",
 "description": "Grep English/French sources for jar"
}
```


### [2026-09-06T21:17:52.017Z] TOOL RESULT

```
=== FSD vol2 jar ===
57388:jar",  n.  a   poroeiam  vessel  usea  lor  preparing  inrusions.—  i. method  (Brewing) ,   a   system  of  mashing,  in  which  the  mash (malt  and  water)  Israised  to  the  final  desired  temperature  by the  admixture  of  water  having  a   correspondingly  high  tem- n.  iT  The  act  of  infringing,  2.  Any  breaking  in  upon  -   perature.  1.  process;.— A   fire-proof  Infuslon-]ar. or  violation  of  a   right,  privilege,  regulation,  law,  con-  zhon-Ifrn,  n.
63357:a-nl^  1   jap'a-noiz;  2   Jap'a-nIz,  ®f.  J-nized;  -niz.’-  jarra.<  Ar.  jarra,  <   Per.  jarrah,  jar.]  jarret- i.J  T.0  change  into  contormity  with  Japane.se  senti-  —   Leyden  jar,  a   form  of  condenser  for  static  electric- at  or  customs:  make  Japanese.  Ja-pan'I-clzef;  Jap'»  ity,  consisting  of  a   glass  jar  or  a   cj'linder  closed  at  one  end, ilset.—  Jap"a-nl-za'ror-sa']tlon,  re.  coated  Inside  and  out  with  tin-foil  nearly  to  the  top,  the  In-
63402:jar'gon,  i   jar'gan;  2   jSr'gon,  t.  I.  f.  To  warble;  expreas  ia'wv  \   jl'si*  2   m'sv  «   fDJal  Fne  ?   o^rSi  the  Hebrew /q.s7ipcA;  al.so  mentioned  in  Revelation,  as
63522:jar'qmoonk",  l   j   .ir -ffipk  ;   2   jar -foopk  ,   re.  [Hind-J  Hyp-  sima) ;   a   wild  coffee.  4.  A   GlUnese  shrub  (C/crodcredrore/ra-  probably  a   mixture  of  Aryas,  White  Huns,  and  aboriginal
63527:jar  rail,  i   jar  a;  2   jar  a,  re.  [Austral.J  A   large  soumtrostern  genus  of  erect  or  climbing  shrubs  of  the  family  Ofeace*,  with  takas  are  of  interest  as  the  source  of  23sop’a  Fables,  and  of
63545:jar'veJ,  w.  [Prov.  Eng.]  Same  as  jarble.  .   pubbce.  After  seem
=== PHN jarre ===
2642:aaIsL \baiiyai\^ en persan A^^lf [6d^te&], grande jarre à vin,
6220:JARRE, s. f. (a.)
6233:[là kotdl marrât taslim aUjarrat] La jarre n'est pas toujours saine
10640:Jarre, s. f. (a.) 917
=== DEV jarre ===
1553:Jahde.  Tumeur  qui  se  développe  à  la  partie  externe du  jarret  du  cheval.  liai,  giardn.  Dans  un  ouvrage  d'hip- piatrique  écrit  en  latin  au  moyen  âge,  je  trouve  les  deux ïovmes  giarda ,  jarda  :  «Quasi  mollis  sufflatio  ad  magnitu- dinem  ovi  aut  amplius. . .  nascitur  in  garrelis  ^  w  C'est l'arabe  i».:^^  âjaradh,  même  signification  i^Tumor  omnis  na- tiis  tu  sufjfragine  junienti  aut  inferiore  pedis  nervo,  dit  Me- ninski).
3561:Giara,  ital.  voy.  Jarre. Giarda,  ital.  vov.  Jarde. (îiarro,  ital.  voy.  Jarre.
3664:lâppos,  voy.  Jarre. Iblis,  voy.  Eblis.
3692:Jarra,  hisp.  voy.  Jarre.
3693:Jarre.
3694:Jarro,  esp.  voy.  Jarre.
4490:Zarra ,  pg.  voy.  Jarre.
4735:ïts^  voy.  Jarre.
=== LKT jarre ===
1698:'Wassergefäß,  Krug';  hieraus  it.  giara 'Krug  mit  zwei  Henkeln',  siz.  giarra 'Olkrug',  prov. /arra,  üz.jarre,  sp.jarra, pg.  zarra,  jarra  'Krug'.  BAISF  in  Zf romPh.  V,242  führt  sp.  charro  'mit  ge- schmacklosen Zieraten  überladen;  Lüm- mel' auf  dieses  Grundwort  zurück.  [DE 290.    Eguilaz  431.    ML  3944.
3130:'Balken,  Hebel';  hieraus  pg.  almanjarra 'Balken  einer  Mühle  oder  Wasserkraft- maschine, an  den  man  das  Tier  bindet, das  drehen  soll',  siz.  minciarrn  'Arm der  Ölpresse  und  anderer  von  Pferden betriebener  Maschinen'.  [DE  156.  Gon- stancio  Dicc  55  c.    GrSVociSic  241.
3310:1439.  Ar.  masraba: 'Trinkgefäß'  [vom  Vb.  sariha  'trinken'],, erst  moderne  Aussprache  für  misraba 'dass.,  kleiner  Krug';  hieraus  mit  ar. Art.  sp.  almojarra  'kleiner  Krug';  über tk.  masrapa  wurde  rum.  nästräpa 'Trinkglas',  nästräpioara;  bulg.  mas- trapa,  serb.  mastraf a  'Becher'.  [DE  179. Eguilaz  238.  M  kl  SIEtWb  184  b.
7969:alguidar  717 alhadla  770 alhaima  782 alhaja(s)  11h alhondega  616 aljama  651 aljaroz  2198 aljava  626 aljaveira  641 a;joA>-e  694 aljuhe  636 alkekengi  1016 a«e//  868 almacen  1362 almazem  1362 almadia  1343 almadraque(xa)  1446 abnadrava  1344 almafariz  1467 almäfega  1413 almafra  1463 almagra  1349 almagre  1349 almanach  1389 almanjarra  1346 almarge(m)  1415 almarracha  1466  a almatrixa  1446 almeja  1347 ahnenara  1463  a almicantarat  1506 almirante  69  a almires  1467 almiscar  1515  a almiscre  1515  a almocadem  1504 almöcavar  1372 almocella  1511a almocreve  1507 alnioeda  1511 almofaga  1465 almofada  1464 almofala  1464 almofariz  1467 almofate  1502 almofrez  1502 almogävar  1496 almoqueire  1507 almotacel  1503 almoxarife  1519 almoxatre  1581 almucella  1520 almude  1490 alparca  243 alpargata  243 alqueire  1174  a alqueria  1096 alquicel  1186 alquicer  1186 alquiis  1174 alquifol  1227 alquilar  1181
8267:jarra  688
8674:jarra  688
9972:almojarife  1519 almojarra  1439 almojatre  1581 alnirineda  1511 almoraduj  1411 ahnotacen  1503 almozal(l)a  1511  a almucio  1520 almud  1490 almuecin  1485 almuidano  1485 aloque(ro)  803 aloqueria  803 alpargata  243 alpicoz  576 alquequenge  1016 alqueria  1096 alquez  1174 alquifol  1227 aquilar  1181 alquile(r)  1181 alquhnia  1157 alquitara  1130 alqmtrdn  1128 altramuz  2115 alubia  1333 «Zmc^cZ  2142 aluquete  2153 aZfaci/  2160 amacena  476 amalgama  1378 amapola  762  d amargaza  829 amarillo  70 mnbar  78 amoscarse  1436 amuco  71 amtileto  866 amusco  1515  a anacal(o)  1545 anadel  1566 «w«/?/  1537 anafre  130 anatron  1567 anazea  1583 andamio  520 annafe  130 ante(ado)  1305 antimonio  918 anzarote  86 afiacal  1545 anacea  1583 anaciar  1583 anafil  1537 öw«7  1568 «/Itr  1568 arac  92 arambel  811 arancel  1428 arfceZW  dial.  204 arhollön  204 arcaditz  988
```


## [2026-09-06T21:18:06.108Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT ctx ===\"; sed -n '1690,1705p' LKT.txt; echo \"=== AFA jarra ===\"; grep -n \"Krug\\|ǧarra\\|garra\" AFA.txt | head -20",
 "description": "LKT entry 688 and Fraenkel"
}
```


### [2026-09-06T21:18:06.162Z] TOOL RESULT

```
=== LKT ctx ===
685.  Ar.  garnait:
'Zibetkatze'  [CHERBONNEAU  in  JAs 1849,  I,  541];  hieraus  frz.  genette,  sp. pg.  gineta  'Zibet-  oder  Risamkatze,  Vi- verra  genetta  L.'.  —  [*(.fa)gmetta  ist schon  von  DIEZ  als  Grundwort  zurück- gewiesen worden.]  [DE  276.  Eguilaz 413.    Devic  DEt  127.    ML  3949.
686.  Berb.  garulu:
'Distel';  hieraus  mit  berb.  Präfix  ta- sp.  tagarnina  'eine  Art  Distel;  sehr schlechte  Zigarre,  Stinkadores'  [DiccCast 1804  b].  —  [Besteht  ein  Zusammenhang mit  gr.  äxapva  'Distel',  woraus  frz. acarne,  sp.  acarna'^]
687.  Ar.  garra:
Vb.  'ziehen,  durch  Ziehen  mitschleppen', schon  von  Ibn  Battuta  IV,  247  als  Fach- ausdruck der  Schiffahrt  benutzt:  'Schlep-
pen, remorquer';  hieraus  sp.  navejar oder  llevar  a  jorro,  pg.  levar  a  zorros 'schleppen',  sp.  jorro  'Schlepptau' ;  ndl. sjorren,  opsjorren  [wozu  noch  sjorklamp, sjorring,  sjortouw].  Pg.  päo  de  jorro, jorräo  'Karren  ohne  Räder  zum  Ab- flachen der  Erde  oder  zum  Schleppen schwerer  Lasten'  [Constancio  Dicc  640]. [DE  291/292.
688.  Ar.  garra:
'Wassergefäß,  Krug';  hieraus  it.  giara 'Krug  mit  zwei  Henkeln',  siz.  giarra 'Olkrug',  prov. /arra,  üz.jarre,  sp.jarra, pg.  zarra,  jarra  'Krug'.  BAISF  in  Zf romPh.  V,242  führt  sp.  charro  'mit  ge- schmacklosen Zieraten  überladen;  Lüm- mel' auf  dieses  Grundwort  zurück.  [DE 290.    Eguilaz  431.    ML  3944.
689.  Ar.  garräfa: 'Weitbauchige  Flasche'  [vom  Vb.  garafa 'schöpfen';  das  Subst.  ist  nicht  klassisch- ar.,  sondern  scheint  nur  vulgär  imMagrib, s.  hier  Nr.  674,  gebräuchlich  zu  sein] ; hieraus  sp.  pg.  garrafa,  frz.  caraffe, carafe,  it.  caraffa,  siz.  carrabba  'Wasser- flasche, Flasche  für  Wein  od.  ähnl.'; dtsch.  Karaffe,  Karaffine,  ndl.  karaf, engl,  caraffe;  russ.  grafin,  poln.  karafka, ßech.  karafina,  bulg.  karafa.  —  [Ab- leitung aus  ar.  kar'a  'Kürbis,  Kürbis- flasche' geht  für  kat.  carbassa,  sp.  cala- baza,  pg.  cabaga  'Flasche'  ebensowenig wie  die  Gruppe  caraffe  aus  angeblichem ar.  karä'a  ML  4676  u.  6900].  —  [DE 274.  Dozy  Oost  48/50.  Hobson-Jobson 160.    Gorjajew  78.
690.  Ar.  garräli:
'Wundarzt,  Chirurg';  hieraus  rum.  gerac 'dass.'.
691.  Pers.  gärsäb:
'Stoffdecke,  Tischtuch'  [aus  pers.  cädir, s.  hier  Nr.  380,  und  sab  'Nacht'  Horn NpEt  S.  171,  Nr.  775];  tk.  carsaf^  'Lein- tuch, Art  Staubmantel,  in  den  sich  die tk.  Damen  beim  Ausgehen  hüllen'; hieraus  rum.  cearceaf,  cearsaf  'dass.'.
692.  Ar.  gäsija:
'Satteldecke'  [vom  Vb.  gasä,  Part,  praes. act.  fem.,  also  eigentlich  'die  Bedeckende']; hieraus  mit  ar.  Art.  sp.  algagias  'Aus- rüstung eines  reitenden  Soldaten'  [so nach  Engelmann;  dagegen  will  Dozy Jiawa'ig,  plr.  von  Jßga,  s.  hier  Nr.  775, also  'die  Kleider',  als  Grundwort  auf- stellen. Lautlich  bietet  die  erste  Ety- mologie weniger  Schwierigkeiten  ;  seman- tisch ist  der  Übergang  von  'Satteldecke' zur  'Gesamtausrüslung  des  Reiters'  eine Regriffserweiterung,  wie  sie  sehr  häufig ist].    Vgl.  hier  Nr.  755.    [DE  117.
=== AFA jarra ===
2663:neinen möchte , zu sein. Diesen , nicht eiuen Krug zahlen
2741:kocht, in einen Krug gethan und von da tropfenweise
2825:(belegt bei (uiuh. s. v. ^jo\) »Seherbe eines Kruges" oder
2885:vorzuschlagen. Auch das jemeuische üJU »Krug'* scheint
2922:[Zwei echt arabische Namen für den Krug sind J^^l^ und
2929:ren, iis^ »Krug" gehört zur Wurzel I^. »ziehen", wie
2930:|?&^, »Krug, Becher", zu ^33. Auf dieses Wort geht
2950:und Aramäisch bei \^ einem kleinen Kruge, das ebenso-
3073:]Ji^c^ >Krug" als Bedeutung angegeben wird, während
3084:halber Krug, in den man Pflanzen (D*3^> » übersetzt aus
5911:mit einer Schnauze versehenen Kruge für den Wein (so
7223:dern ist eine allgemeine Bezeichnung für »Krug". Wo es
7230:glaube, auch hier wieder die Grundbedeutung »Krug" (wie
7236:Kruge«. W-as aber die Bedeutungen »Gerechtigkeit, Grad-
```


## [2026-09-06T21:18:08.898Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 jar ===\"; grep -n \"jar, n\\.\\|^jar,\\|Arab. jarrah\\|jarrah\" KLN_1966.txt | head -20; echo \"=== SKT jar ===\"; grep -n -i \"jarrah\\|jarra\" SKT.txt | head -10; echo \"=== WEB jar ===\"; grep -n \"jarrah\" WEB_vol1.txt | head -5; echo \"=== HJB ===\"; grep -n \"jarrah\\|Jarr\" HJB.txt | head -10",
 "description": "Grep Klein, Skeat, Webster, Hobson-Jobson for jar"
}
```


### [2026-09-06T21:18:08.989Z] TOOL RESULT

```
=== KLN 1966 jar ===
20173:jar,  intr.  and  tr.  v„  to  make  a  harsh,  creaking noise.  —  Prob.  of  imitative  origin.  Cp.  ajar, ‘out  of  harmony’,  nightjar.
20175:jar,  n.,  a  vessel  of  earthenware,  glass  or  stone.  — F.  jar  re,  fr.  OProven?.  jarra,  fr.  Arab.  jarra11, ‘a  large  earthen  vessel’  (whence  also  Sp.  jarra. It.  giarra).
20181:jarosite,  n.,  a  potassium  iron  sulfate  (mineral.)  — Named  after  Barranco  Jaroso,  Almeria,  Spain. For  the  ending  see  subst.  sufF.  -ite. jarrah,  n.,  a  eucalypt  of  Australia  (Eucalyptus marginata).  —  From  Australian  native  name, jarvey,  n.,  a  cabdriver.  —  From  Jarvey  or  Jervis, name  of  a  Dublin  driver  who  lived  in  the  18th century.
=== SKT jar ===
=== WEB jar ===
=== HJB ===
268:i5jL.  Aln-i-Akbaxi,  The,  by  Abul  Fazl 'Allami,  tr.  from  the  orig.  Persian  by H.  Blochmann,  M.A.  Calcutta.  1873. VoL  i. ;  [vols.  ii.  and  iii.  translated  by CoL  H.  S.  Jarrett ;  Calcutta,  1891-94].
2152:c.  1590.— "To  the  S.E.  of  Bengal  is  a large  oountrv  called  Arkniig  to  which  the Bunder  of  Chittagong  properly  belongs." — Oladtrin*t  Ayeen^  ed.  1800,  h.  4.  [Ed.  JarreU. u.  119]  in  ong.  (i.  888)  ArUumff.
2247:o.  1680. — "The  dominions  of  the  Rajah of  Aaiiatn  join  to  Kamroop ;  he  is  a  very powerful  prince,  lives  in  great  state,  and when  he  cues,  his  principal  attendant^  both male  and  female,  are  voluntarily  buried  alive with  his  corpse."— 6'tediiniir*«  Ayeem  (ed. 1800)  ii.  8 ;  [Jarrett,  trans,  ii.  118].
2329:[c.  1590.— "In  the  citv  of  Sambal  is  a temple  called  Hari  Mandal  (the  temple  of Vishnu)  belonging  to  a  Brahman,  from among  whose  descendants  the  tenth  avatar will  appear  at  this  spot." — Aln,  tr.  Jarrett,
3131:[c.  1590.— "The  baya  is  like  a  wild  spar- row but  yellow.  It  is  extremely  intelligent, obedient  and  docile.  It  will  take  small  coins from  the  hand  and  bring  them  to  its  master, and  will  come  to  a  call  ^m  a  long  distance. Its  nests  are  so  ingeniously  constructed  as^to defy  the  rivalry  of  clever  artificers."-— A  In (trans.  Jarrett),  iii.  122.]
3235:BEEQAH,  s.  H.  bighd.  The  most common  Hindu  measure  of  land-area, and  varying  much  in  different  parte of  India,  whilst  in  every  part  that has  a  l^ghd  there  is  also  certain  to  be a  pucba  beegah  and  a  kuteha  beeffoh  (vide CUTCHA  and  PUCKAX  the  latter  being some  fraction  of  the  former.  The be«^  formerly  adopted  in  the  Revenue Survey  of  the  N. W.  Pl*ovinces,  and  in the  Canal  Department  there,  was  one of  3026  sq.  yards  or  i  of  an  acre. This  was  apparently  founded  on Akliar's  beegah,  which  contained  3600 »q.  Hahi  gaz,  of  about  33  inches  each. [For  which  see  Ain,  trans.  Jarretty  ii. 62.].  But  it  is  now  in  official  returns superseded  by  the  English  acre.
3289:[c.  1500.— "Sarkar  of  Behar:  containing 46  Mahals.  .  r—Au  (tr.  JarreU),  ii.  153.] F
3593:[c.  1590.— "This  tract  is  inhabited  by  an important  Baloch  tribe  called  Ealmam." — Axn,  trans.  Jarret,  ii.  837.]
4069:BBINJABBY,  s.  Also  BINJAB- BEE,  BUNJABBEE,  and  so  on.  But the  first  form  has  become  classical  from its  constant  occurrence  in  the  Indian Despatches  of  Sir  A.  Wellesley.  The word  is  properly  H.  bawdrdy  and Wilson  derives  it  from  Skt.  hamj, trade,'  kdra^  '  doer.'  It  is  possible  that the  form  bnnjdrd  may  have  been  sug- gested by  a  supposed  connection  witn the  Pers.  hiring,  *rice.'  (It  is  alleged in  the  Did,  of  Words  used  in  the  E, Indies^  2nd  ed.,  1806,  to  be  derived  from brinjy  *rice,'  and  aro,  'bring'!)  The Brinjanries  of  the  Deccan  are  dealers  in grain  and  salt,  who  move  about,  in numerous  parties  with  cattle,  carrying their  goods  to  different  markets,  and  who in  the  days  of  the  Deccan  wars  were  the great  resource  of  the  commissariat,  as they  followed  the  armies  with  supplies for  sale.  They  talk  a  kind  of  Manratta or  Hindi  patois.  Most  classes  of  Banjaras in  the  west  appear  to  have  a  tradition <)f  having  first  come  to  the  Deccan  with Moghul  camps  as  commissariat  carriers. In  a  pamphlet  called  Some  Account  of the  Bunjarrah  Class^  by  N.  R.  Cumber- lege,  District  Sup.  of  Police^  Bcueinj Berar  (Bombay,  1882  ;  [N(yrih  Indian N,  <fc  Q,  iv.  "163  Mqq.ji  the  author attempts  to  distin^ish  between  brinj- arees  as  *  grain-carriers,'  and  bunjarrahs, from  bunjdr,  *  waste  land'  ^meaning banjar  or  bdnjar).  But  this  seems fanciful.  In  the  N.-W.  Provinces  the name  is  also  in  use,  and  is  applied  to a  numerous  tribe  spread  along  the skirt  of  the  Himalaya  from  Hardwar to  Qorakhpur,  some  of  whom  are settled,  whilst  the  rest  move  about with  their  cattle,  sometimes  transport- ing goods  for  hire,  and  sometimes carrying  grain,  salt,  lime,  forest  pro- duce, or  other  merchandise  for  sale. rSee  Orooke,  Tribes  and  Castes,  i.  149  seqq.] vax^&r&S,  as  they  are  called  about Bombay,  used  to  come  down  from Bajputana  and    Central    India,    with
4089:1800.— "The  BinJarriM  I  look  upon  in the  light  of  servants  of  the  public,  of  whose grain  I  have  a  right  to  regulate  the  sale .  .  .  always  taking  care  that  they  have  a proportionate  advantage." — A,  Well^letff  in Life  of  Sir  T.  Munro,  i.  264.
```


## [2026-09-06T21:18:24.331Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA ctx 2915-2940 ===\"; sed -n '2915,2940p' AFA.txt; echo; echo \"=== PHN leaf of line 6220 ===\"; python3 -c \"\ns=open('PHN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport sys\ntxt='\\n'.join(s[:6219])\nprint('leaf idx', txt.count(chr(12)))\n\"; sed -n '6215,6250p' PHN.txt",
 "description": "Fraenkel context and Pihan jarre"
}
```


## [2026-09-06T21:18:25.265Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/TYL; echo \"=== MON جره ===\"; grep -n \"^جره:\\|جره:\" MON_part1.txt MON_part2.txt | head -20; echo \"=== MON کره ===\"; grep -n \"^کره:\\|کره:\" MON_part1.txt MON_part2.txt | head -20",
 "description": "TYL files and Mo'in entries"
}
```


### [2026-09-06T21:18:26.206Z] TOOL RESULT

```
=== AFA ctx 2915-2940 ===
muthlich ist auch jede semitische Etymologie überhaupt
hinilUlig und das Wort persischen Ursprungs. Der .Sabb.
156^ vorkommende Niime Snnpp bedeutet vielleicht dasselbe
und wahrscheinlich ist auch ^lySLs Jäküt IV. 18 damit
zu combinieren. [}-^V^ bei Gast. 7S9 scheint kein echt ara-
mäisches Wort, sondern wird wohl ein arab. Plur. jjl^*
syrisch transcribiert sein.]
[Zwei echt arabische Namen für den Krug sind J^^l^ und
5*^^. Zu dem ersteren scheint mit aram. |i.-.s^ ]»Trau-
benranke" zu gehören, das mit 712cyX wahrscheinlich
• •
nichts zu thun hat. Beide sind von :»lang herabhängen*'
benannt, wie zu *7l JS die nVvT va>LJIi> gehören ; wahr-
scheinlich wird auch äthiop. sagal i Zauber" dazu gehö-
ren, iis^ »Krug" gehört zur Wurzel I^. »ziehen", wie
|?&^, »Krug, Becher", zu ^33. Auf dieses Wort geht
bekanntlich fr. giarre »SchiflFskrug, ital. giarra zurück.]
Ein altes Fremdwort ist jy.Jo (higäz. Dial.) nach Gauh. zur
Wurzel JLcXi, für die die Araber den Grundbegriff »reini-
gen" erfunden haben (vgl. Nöldeke Lit Centralbl. 1879.
p. 361), »weil man sich darin reinigt". Es ist xaio;;
wohl durch Vermittelung von syr. Uor^ ; in das Jüd. aram.
1) II. :U2. J 3 , äJ Jj.73
ist die griechische Form dieses bekanntlich ursprünj^lich
semitischen Wortes niclit eingedrungen. Eine, wie es
scheint, das griechische xxioy direct wiedergebende Form

=== PHN leaf of line 6220 ===
leaf idx 248
vinces. Les officiers des janissaires portaient e titre de tchxr^
badjts, c'est-à-dire yawetir* de soupe. Voyez Tghorbadji. — II y
a loin, sans doute, de la transcription française à l'original
turc, qui se prononce yénîtchéry, comine on vient de le voir;
mais l'usage veut que l'on écrive janissaire,
JARRE, s. f. (a.)
ijj^ [djarrat] grande cruche de terre cuite, à large ventre, ordi-
nairement vernissée , et qui sert en Orient à conserver de l'eau
ou tout autre liquide. En Provence, on fabrique une grande
quantité de ces sortes de vases pour y mettre de l'huile. C'est
aussi le nom d'une espèce de fontaine en terre cuite, très-
communément employée dans les ménages. — On trouve ce
mot écrit giare dans quelques dictionnaires français, et giara
en italien; mais l'usage a fait adopter yarre, qui se rapproche218 JAS
davantage du correspondant arabe, dont la seconde consonne
est surmontée d\in teclidtd ou signe de redoublement. — Les
Arabes font souvent usage du proverbe suivant, en jouant sur
les mots ij^ [marrai] et i^ [e^Virra^] : 'ijÂ j^^mJ »j^ J^^ ^
[là kotdl marrât taslim aUjarrat] La jarre n'est pas toujours saine
et sauve. En français , nous disons : «^ Tant va la crucbe à Feau
qu'à la fin elle se casse. »
JASMIN, s. m. (a.)
(^jvc^l! [yoamln] Nom d'un arbuste sarmenteux , à fleui's mono-
pétales et d'une odeur très-suave. 11 en existe un assez grand
nombre d'espèces, parmi lesquelles on distingue le jasmin blanc
commun, employé dans la composition de poudres, huiles, es-
sences et parfums; puis le jasmin à grandes feuUles ou jasmin
d'Espagne, dont les fleurs sont rougeâtres en dehors. — Le
mot français jasmin, qui s'emploie aussi bien en parlant de la •
fleur que de l'arbuste , représente avec exactitude l'orthographe
de son correspondant arabe, dont les variantes (^«wl^ [ycumtVi] ,
^jy€>éê\it [yâsmoûn]^ et |«wl» [yo^'m] en poésie, sont également
usitées chez les Persans et les Turcs. — On peut comparer
avec l'arabe le grec Idtriifi , l'espagnoiyozntm^ le portugais y^^nitm
pour la fleur eijasmineiro pour l'arbuste, l'italien gelsomino,
enfin l'anglais yo^mtW et yeMamtne.
```


### [2026-09-06T21:18:26.280Z] TOOL RESULT

```
TYL_Taylor1934_BenJonson_pages.txt
TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf
=== MON جره ===
MON_part2.txt:88280:هماجره: (ممعلهه (ع. . هاجرة] (افا) 
MON_part1.txt:17452:انجره: (مدددلمد (ا.) ( کی .) گر نه دو پایه. 
=== MON کره ===
MON_part1.txt:15814:اکره: [ع.] (ص تفض..) منفور تر) 
MON_part1.txt:20804:با کره: (6-) 2672 [ع. با کرة] (ص.) دختری 
MON_part1.txt:24552:یکره: (۵-)90(۲2 [ع. بکرة] (.) بامداد بگاه» 
MON_part1.txt:39400:تلکره: )۱2266۲2 [ع. تدذکرة] (امسص.) 
MON_part1.txt:50958:چکره: (م)«تاث [- چکله] (۱.) قطرهٌ آب» 
MON_part1.txt:65001:داکره: (0-) -276۲ [ع. ذا کرة | (افا.) مونث 
MON_part1.txt:78600:سکره: (6-)0۲2: [- اسکوره ِ اسکره ِ 
MON_part2.txt:15460:۳ ص ۱۹۵؛ فرع. سج.) قوت مفکره: (فد. 
MON_part2.txt:22152:کرکره: (۵-)۵۲۲۵۲۸ (۱.) قسمی برد چوبی 
MON_part2.txt:22617:کره: «ها() چ رکد» وسخ. پوست دست و 
MON_part2.txt:22631:کره: (1۵۳)۵ [- کرو - کری] (.) خاناة 
MON_part2.txt:22635:کره: (9)9:ه [- معر. کرج] (ا.) زنگار 
MON_part2.txt:22639:کره: (6-)121۲2 [ع. کرة] (.) بار» دقعه 
MON_part2.txt:22645:کره: (معما (ع. کرة] (.) گوی (اعم از 
MON_part2.txt:22657:کره: 10۳ [ع.] (مسص م.) نایسند داشتن» 
MON_part2.txt:52034:مذاکره: (16۲6-) ۱2102211۵۲2 [ع. مداکرة] 
MON_part2.txt:56275:مستکره: ۱( [ع.) (امف.) زشت 
MON_part2.txt:56277:مستکره: ۱۱05۳۵ [ع.] (افا.) زشت و 
MON_part2.txt:63872:مکره: دا [ع.] (افا.) اکراه نماینده» 
MON_part2.txt:65882:مناکره: (ع۲ع)مفقنهه [ع. منا کرة5]
```


## [2026-09-06T21:18:45.647Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T21:18:45.684Z] TOOL RESULT

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


## [2026-09-06T21:18:47.212Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"جرّه\\|جَرّه\" MON_part1.txt MON_part2.txt | head -20; echo \"=== v1 djvu ===\"; grep -n \"جره:\\|جرّه:\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -20",
 "description": "Grep Mo'in for jarreh"
}
```


### [2026-09-06T21:18:47.296Z] TOOL RESULT

```
=== v1 djvu ===
17452:انجره: (مدددلمد (ا.) ( کی .) گر نه دو پایه.
```


## [2026-09-06T21:18:59.243Z] TOOL CALL #28: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/jar\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D8%B1%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%A9\" \\\n \"https://www.etymonline.com/word/jar\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 277 verification: Arabic K.r.v/kura -> jarra -> jar chain\" ; done",
 "description": "Archive web sources for jar chain"
}
```


### [2026-09-06T21:19:05.074Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d9e8bf70354addc0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b23666a3b8fabbbd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9baa7324c2e7d46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1fef3b99bab2cb6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f827e9692d827780.txt
```


## [2026-09-06T21:19:08.070Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### jar wikt\"; grep -n -A12 \"^Etymology 1\" d9e8bf70354addc0.txt | head -40; echo \"###### etymonline jar\"; grep -n -i -B2 -A8 \"jar (n\" e1fef3b99bab2cb6.txt | head -60",
 "description": "Read jar etymologies"
}
```


### [2026-09-06T21:19:08.136Z] TOOL RESULT

```
###### jar wikt
###### etymonline jar
26- also from 1520s 
27-
28: jar (n.) 
29-
30- "simple earthen or glass cylindrical vessel," early 15c., possibly from rare Old French jarre "liquid measure smaller than a barrel," or more likely from Medieval Latin jarra (13c.) or Spanish or Catalan jarra (13c.), all ultimately from Arabic jarrah "earthen water vessel, ewer" (whence also Provençal jarra , Italian giarra ), a general word in the 13c. Mediterranean sea-trade, which is from Persian jarrah "a jar, earthen water-vessel." Originally in English a large container used for importing olive oil.
31-
32- In Britain in the 15th to 17th centuries, oil-lamps were overall not often used, because the oil was too expensive. Usage increased in the 17th century despite the expense. Olive oil was the most-often-used type of oil in the oil-lamps until the 18th century. The indications are good that no country or region exported more oil to Britain than southern Spain did in the 15th-17th centuries, with southern Italy coming second. ["English Words of Arabic Ancestry"]
33- also from early 15c. 
34-
35- Entries linking to jar 
36-
```


## [2026-09-06T21:19:15.739Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### جرة\"; sed -n '1,120p' b23666a3b8fabbbd.txt | grep -n -i -A6 \"Etymology\\|Arabic\" | head -60",
 "description": "Read Arabic jarra wiktionary"
}
```


### [2026-09-06T21:19:15.795Z] TOOL RESULT

```
###### جرة
57: Arabic 
58-
59: Toggle Arabic subsection 
60-
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Declension 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Noun 
84-
85- 1.2.1.1 
86- Declension 
--
89: Etymology 3 
90-
91- 1.3.1 
92- Noun 
93-
94- 1.3.1.1 
95- Declension 
--
98: South Levantine Arabic 
99-
100: Toggle South Levantine Arabic subsection 
101-
102- 2.1 
103: Etymology 
104-
105- 2.2 
106- Pronunciation 
107-
108- 2.3 
109- Noun
```


## [2026-09-06T21:19:16.469Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### كرة\"; grep -n -i -A8 \"Etymology\" e9baa7324c2e7d46.txt | head -60; echo \"###### کره persian\"; grep -n -i -A6 \"Etymology\" f827e9692d827780.txt | head -60",
 "description": "Read kura wiktionary pages"
}
```


### [2026-09-06T21:19:16.542Z] TOOL RESULT

```
###### كرة
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
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
--
171: Etymology 1
172- [ edit ] 
173-
174- Likely through Aramaic , from Akkadian 𒄥 ( /⁠kurru⁠/ ) , ultimately from Sumerian 𒄥 ( GUR , “ a bundle, rolled up barley ” ) 
175-
176- Pronunciation
177- [ edit ] 
178-
179- IPA ( key ) : /ku.ra/ 
--
374: Etymology 2
375- [ edit ] 
376-
377- Root 
378-
379- ك ر ر ( k r r ) 
380-
381- 8 terms 
382-
###### کره persian
73: Etymology 1 
74-
75- 2.1.1 
76- Pronunciation 
77-
78- 2.1.2 
79- Noun 
--
88: Etymology 2 
89-
90- 2.2.1 
91- Pronunciation 
92-
93- 2.2.2 
94- Noun 
--
100: Etymology 3 
101-
102- 2.3.1 
103- Pronunciation 
104-
105- 2.3.2 
106- Noun 
--
118: Etymology 4 
119-
120- 2.4.1 
121- Pronunciation 
122-
123- 2.4.2 
124- Noun 
--
130: Etymology 5 
131-
132- 2.5.1 
133- Pronunciation 
134-
135- 2.5.2 
136- Proper noun 
--
351: Etymology 1
352- [ edit ] 
353-
354- From Middle Persian *karag . Related to Middle Armenian կարագ ( karag ) and Arabic كَرَج ( karaj ) .
355-
356- Pronunciation
357- [ edit ] 
--
432: Etymology 2
433- [ edit ] 
434-
435- Borrowed from Arabic كُرَة ( kura ) .
436-
437- Pronunciation
438- [ edit ] 
--
492: Etymology 3
493- [ edit ] 
494-
495- From Middle Persian [script needed] ( kwlk' /⁠kurrag⁠/ , “ colt ” ) , from Old Iranian *kurna-ka- , a derivative of the Proto-Iranian root which gave Bakhtiari کر ( kowr ) , Northern Kurdish kur ( “ boy, son ” ) . Cognate with Northern Kurdish kurrik , Zazaki kurrî , kirrêk , kirri , kurik , kurrik , Talysh kırə , and akin to Middle Armenian քուռակ ( kʻuṙak ) , Armenian քուռակ ( kʻuṙak ) , քուռիկ ( kʻuṙik ) , Aghwan 𐕣𐕒𐕡𐕙𐕒𐕡𐕄 ( kuruḳ ) , Georgian ქორაკი ( koraḳi ) , ქორა ( kora ) , კურაკი ( ḳuraḳi ) , კურატი ( ḳuraṭi ) , კურიჰკაჲ ( ḳurihḳay ) , კურიკაჲ ( ḳuriḳay ) , კურია ( ḳuria ) , ქვირანაჸი ( kviranaʾi ) , ქვირა ( kvira ) , კურო ( ḳuro ) , Arabic كُرَّج ( kurraj ) , Iranian borrowings.
```


## [2026-09-06T21:19:23.798Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '160,420p' e9baa7324c2e7d46.txt",
 "description": "Read full Arabic كرة wiktionary section"
}
```


### [2026-09-06T21:19:23.842Z] TOOL RESULT

```
 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: گره , کره , گڑھ , كره , گرہ , and ك ر ه 

 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Likely through Aramaic , from Akkadian 𒄥 ( /⁠kurru⁠/ ) , ultimately from Sumerian 𒄥 ( GUR , “ a bundle, rolled up barley ” ) 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ku.ra/ 

 Noun
 [ edit ] 

 كُرَة • ( kura )  f ( dual كُرَتَان ( kuratān ) , plural كُرَات ( kurāt ) or كُرًى ( kuran , construct state كُرَى ( kurā ) ) or كُرُون ( kurūn ) ) 

 ball 
 الكرة مستديرة وملونة. ― The ball is round and colorful. 

 sphere , globe 

 Declension
 [ edit ] 

 Declension of noun كُرَة ( kura )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 كُرَة 
 kura 

 الْكُرَة 
 al-kura 

 كُرَة 
 kurat 

 nominative

 كُرَةٌ 
 kuratun 

 الْكُرَةُ 
 al-kuratu 

 كُرَةُ 
 kuratu 

 accusative

 كُرَةً 
 kuratan 

 الْكُرَةَ 
 al-kurata 

 كُرَةَ 
 kurata 

 genitive

 كُرَةٍ 
 kuratin 

 الْكُرَةِ 
 al-kurati 

 كُرَةِ 
 kurati 

 dual

 indefinite

 definite

 construct

 informal

 كُرَتَيْن 
 kuratayn 

 الْكُرَتَيْن 
 al-kuratayn 

 كُرَتَيْ 
 kuratay 

 nominative

 كُرَتَانِ 
 kuratāni 

 الْكُرَتَانِ 
 al-kuratāni 

 كُرَتَا 
 kuratā 

 accusative

 كُرَتَيْنِ 
 kuratayni 

 الْكُرَتَيْنِ 
 al-kuratayni 

 كُرَتَيْ 
 kuratay 

 genitive

 كُرَتَيْنِ 
 kuratayni 

 الْكُرَتَيْنِ 
 al-kuratayni 

 كُرَتَيْ 
 kuratay 

 plural

 sound feminine plural‎; 
 broken plural in ـًى ( -an ) ‎; 
 sound masculine plural

 indefinite

 definite

 construct

 informal

 كُرَات ‎; كُرَى ‎; كُرِين 
 kurāt ‎; kurā ‎; kurīn 

 الْكُرَات ‎; الْكُرَى ‎; الْكُرِين 
 al-kurāt ‎; al-kurā ‎; al-kurīn 

 كُرَات ‎; كُرَى ‎; كُرِي 
 kurāt ‎; kurā ‎; kurī 

 nominative

 كُرَاتٌ ‎; كُرًى ‎; كُرُونَ 
 kurātun ‎; kuran ‎; kurūna 

 الْكُرَاتُ ‎; الْكُرَى ‎; الْكُرُونَ 
 al-kurātu ‎; al-kurā ‎; al-kurūna 

 كُرَاتُ ‎; كُرَى ‎; كُرُو 
 kurātu ‎; kurā ‎; kurū 

 accusative

 كُرَاتٍ ‎; كُرًى ‎; كُرِينَ 
 kurātin ‎; kuran ‎; kurīna 

 الْكُرَاتِ ‎; الْكُرَى ‎; الْكُرِينَ 
 al-kurāti ‎; al-kurā ‎; al-kurīna 

 كُرَاتِ ‎; كُرَى ‎; كُرِي 
 kurāti ‎; kurā ‎; kurī 

 genitive

 كُرَاتٍ ‎; كُرًى ‎; كُرِينَ 
 kurātin ‎; kuran ‎; kurīna 

 الْكُرَاتِ ‎; الْكُرَى ‎; الْكُرِينَ 
 al-kurāti ‎; al-kurā ‎; al-kurīna 

 كُرَاتِ ‎; كُرَى ‎; كُرِي 
 kurāti ‎; kurā ‎; kurī 

 Derived terms
 [ edit ] 

 كُرَة اَلْقَدَم ( kurat al-qadam , “ football ” ) 

 كُرَة اَلسَّلَّة ( kurat as-salla , “ basketball ” ) 

 كُرَة اَلْقَاعِدَة ( kurat al-qāʕida , “ baseball ” ) 

 Descendants
 [ edit ] 

 → Azerbaijani: kürə 

 → Ottoman Turkish: كره ( küre ) Turkish: küre 

 Etymology 2
 [ edit ] 

 Root 

 ك ر ر ( k r r ) 

 8 terms 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /kar.ra/ 

 Noun
 [ edit ] 

 كَرَّة • ( karra )  f ( dual كَرَّتَان ( karratān ) , plural كَرَّات ( karrāt ) ) 

 recurrence , repetition , return , time 
 609–632 CE , Qur'an , 39:58 : لَوْ أَنَّ لِي كَرَّةً فَأَكُونَ مِنَ الْمُحْسِنِينَ law ʔanna lī karratan faʔakūna mina l-muḥsinīna If I had another time so I could be amongst those who do good! 

 attack , instance noun of كَرّ ( karr ) 

 Declension
 [ edit ] 

 Declension of noun كَرَّة ( karra )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 كَرَّة 
 karra 

 الْكَرَّة 
 al-karra
```


## [2026-09-06T21:19:42.678Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM page tags ===\"; grep -n \"\\[pdf page\" AFM_pages.txt | head -5; echo; python3 - <<'EOF'\nimport re\ns=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages[:3]):\n    print('---',i,p[:200].replace('\\n',' | '))\nEOF",
 "description": "Inspect AFM page structure"
}
```


### [2026-09-06T21:19:44.955Z] TOOL RESULT

```
=== AFM page tags ===

npages 198
--- 0 
--- 1 8 | 0 | ܥܝ | ܶܡ 7 | ܫ ܢ 0 ܣܚ | .ܡܨ >  )‏ اعم ܨ | 3 ܛ 5 62 ܨ ܗ | ܡ 5 | 1 ` < 3[ | 1 , 3 5 ܢ | ل ܨ( : : | `( × 2 7 : ̄ܡ | ܝ 2 -. و | / ܪ ܇ ܐ ܢ | . ܥ يبد < ܲܗ | ܘܨ ܝ ܓ | بي بهم 0 1 1 | ܗܨ . ܢ 1 ` | ܙ ^ ܢܢ | 9 ܪ 1 .° 2 | 3 0 : | 1 : ܫ" | ܫ ܠ 1 ܨܢ 7
--- 2 الالفاظ 9 ܐܘܝ ܐܬܗ بين | ܨ | 1 62 شرا | رس 03 سعرد اتكلرالى | 70 | ܒ | ܦ المطبعة الكاثوليكة للاباء السوعبين | في بيروت سنة ^ ܀ ܬܙ
```


## [2026-09-06T21:19:45.099Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ns=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nm=[mm.start() for mm in re.finditer(r'\\[pdf page (\\d+)\\]',s)]\nprint('tags',len(m))\n# find page 85 by leaf offset note: '301 lea...' unknown; print tag list sample\nprint(re.findall(r'\\[pdf page (\\d+)\\]',s)[:5], re.findall(r'\\[pdf page (\\d+)\\]',s)[-5:])\nEOF",
 "description": "Inspect PLA page structure"
}
```


### [2026-09-06T21:19:46.759Z] TOOL RESULT

```
tags 0
[] []
```


## [2026-09-06T21:19:52.051Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AFM','PLA','TYL','AHD','FVA','SOD','SLW','BQT','MON']:\n    e=d[k]\n    print('==',k)\n    for f in ['page_offset','lookup_hint','local_file','scans','notes','cites']:\n        if e.get(f): print('  ',f,':',str(e[f])[:500])\n\"",
 "description": "Read page offsets for key refs"
}
```


### [2026-09-06T21:19:53.626Z] TOOL RESULT

```
== AFM
   page_offset : 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   lookup_hint : Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   notes : Arabic OCR fair; Syriac/Latin etyma partially garbled.
   cites : page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)
== PLA
   page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}]
   notes : Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).
   cites : page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word
== TYL
   lookup_hint : Not on IA (searched 'arabic words in english', 'society for pure english tract 38'); Google Books record has no view. Taylor's related 'Etymological List of Arabic Words in English' (1933) id QmBbAAAAIAAJ is snippet only.
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt']
   notes : RE-SEARCH 2026-09: the tract itself is full view on HathiTrust (US) — download in a browser (host is IP-blocked). Only a related article (Taylor, 'Arabic Words in Ben Jonson', Leeds Studies in English 3, 1934) was downloadable here; it is NOT the tract. Not on archive.org/Google Books.
== AHD
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   notes : AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.
   cites : page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
== FVA
   lookup_hint : Searched archive.org, ketabnak, noorlib, web: no digital copy found.
   notes : RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only.
== SOD
   page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get serv
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   notes : OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.
   cites : entry number / page in Gharib's Sogdian dictionary
== SLW
   page_offset : Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles keep the ORIGINAL journal page numbers in the margins, so grep 'Sogdian Loan' then the original page number (93-106). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Original: JSTOR https://www.jstor.org/stable/608123 (BSOAS 10.1) - search jstor for 'Sogdian Loan-Words in New Persian'. In the local text grep -n -i 'sogdian loan' to find the article, entries are numbered Persian words with Sogdian etyma.
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt
   notes : Also Bailey/Henning BSOAS volumes are not on IA.
== BQT
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
   notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noo
   cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
== MON
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
   notes : covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full
   cites : page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
```


## [2026-09-06T21:20:01.937Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA leaf 100 (printed p.85) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==100' incoming/PLA/PLA_pages.txt | head -60",
 "description": "Print Asbaghi p.85"
}
```


## [2026-09-06T21:20:02.648Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 46 47 48; do echo \"=== AFM leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' AFM_pages.txt | head -40; done",
 "description": "Print Addi Shir around p.39"
}
```


### [2026-09-06T21:20:03.529Z] TOOL RESULT

```
=== PLA leaf 100 (printed p.85) ===
 armdäni                                                                          85                                               $aribäna

                                                PA
           aus       dem       mp.         p        kirm    "Drache"             am.           staro-karsma         ı +   ol,    däne      mp.
           davänik,                ar..yi, dänig                    stammt       aus     dem mir,        dänak     2, syr. tert,


Or»         -       Sarmüg:              "Überschuhe"                    aus    dem    pers.      gu.     sarmüze     4   "was    über   den
           normalen                Schuhen               getragen          wurde,        aus    dem    mp.
                                                                                                         )» sar       "Kopf;      auf,   über"
           +       mp.    3%        mözag            "Schuhe"             5,

   .                                                                                          £         u
De?            -    Baranfas:                  "stark"          aus       dem    pers.      Zu  giränpost                 6, mp.         rd
           garän          "schwer"                  + MP ersio pußt              "Rücken!         cc      aw.     paräta-


a              - baranfa$:                     "stark"          =    Yaranfas          Ss. Karanfas.

     [3
o>-            $urra:          "Gefäß               aus    Glas"          8 aus       dem   pers. „s kore.


y?-            Karü:          Pl.        v. st adur s.                    abur


                    $arühaq:               "Bündel,             Truppe"          aus     dem pers. „,‚/grüh 9 << mp.» gröh                       10,
ey?”                      .                1
           syr. Laos 11,

—ıs- Barib: Pl. v.cyL,» Zurbbän s. Zurbbän.

7                  Barip:           "Dsharib,              ein       Flächenmaß"            aus    dem    pers.     2, arib       12    m.
[—_                                  13                    ?„..       14
                vb griw                       ‚syr.        ein.


&l,,2- Jaribäna:                                "eine bestimmte                   Art Steuer"            adj. v. Zarib 15,


1.        Nyberg          Bd.        IIs.            v.
2.        ebda.
3.        Brockelmann                    s.     v.
4.        Muhit          s.    v.,         albasa          s.       v.
5.        Mackenzie                Ss.     v.
6.        Addai          Scher           s.     v.
7. Mackenzie                       s.      v.
8.        Addai          Scher           s.     v.
9.        LD.       s.    v.
10.        Mackenzie                 Ss.       v.
11.        Brockelmann                     s.       v.
12.        FM.       s.       v.
13.        Mackenzie                 Ss.       v.
14.        Brockelmann                     s.       v.
15.        FM.       s.       v.
```


### [2026-09-06T21:20:05.285Z] TOOL RESULT

```
=== AFM leaf 46 ===
اشر ا
الوجود في ܐܬܬܬ وجلدها ܐܢܐܟ منقّط والنقاشون يتاضون ܐܛܝܐ عن الثلم ( الإرهان
ܗ ظ
* (الجاهة ) الصخرة العظيمة المستديرة تعريب كله
+( الخن) 3060 تقولا كاماد اي شخصة تعريب تجو ܕܬܐ ܐܶܢ
( الجَيْجم ) معرب جمجم وهو ضرب من الأحذية يله فتراء بلاد فارس
( 3 الذي يمل :3 امام الملك حين يلس ثيابة مركب من جام اي
مرآة ومن دار اي حامل
* :5 5 ` معرب تجمّار أي شحم النخلة وهو مادّة بيضاء لسَة
لذيذة الطعم كالطليب التجتد تكون في رأس النخلة ويقال لها بالتركبة حزما
ني
امون ») معرث كارمدئ ومنة الا ران ليككة عد 4 ١‏ ` ܥ
والكردي ُأميش ' ١‏
ܫܫ نوع مرخ الحجارة 5 5 نم قرب يقال لما الطفراء على منسافة
ثلاثة ايام من المدينة واحوده 15( الى 338 ܨ .3 مع بياض وزرقة 0
ܚܝ ܐ في البرهان القاطع : : واسمة ܐ ܐ ܨ .وهو اذا :| وضع
ܐܵܪܵܐ( أوورك ܝ 25 الاحتلام وان الخمز اذا شر بت
بقدح مصنوع «نة لا تسكر ابدًا وكذا اذا وضع فيها 3 1
نوع من اللعل »
( الجَمَسَفْرم ) ܒ قوتة
,ܢ شبيهة بقوة الشّيح عل ا 0
ܨܐ # ܨ جم ܐܚܝ ٠‏ .ܣ £ البرهان القاطع ܒ ܟ هو |( > |©
الساطالي زهره دقيق الى الغابة يتف على النبات والشجر نظير حمل المساكين 10
له بالعر بسة الريحان السلمالي 18039 فسلكن وسلوالى فسلكن »
* (الجَبّشُ) الصوت 53 03 وهو 504 العاشق والمعشوق بعضعرا
لبعض بنوع خني ٠‏ وتقول بالعريّة : سمعت من جانبها تجنشا
53 ± منشتق من اشن" ومضاه قله 7 وايتهزن
ܟ ”2
=== AFM leaf 47 ===
ܝܚܘ 5 ܝܚ
( الَامَكيّة والجَوْمَك) رواتب خدام الدولة. 1 9 مودق مق
1 ` وهو آداة النسة
( )0 هنوات كالاؤاو من فضَّة وفي ܐܠܩܰܒ݂ܳܐ هو عن مم الفحة
6 على شكل ܐܕܕ مأخوذ ما عن الفارسي حجان ومعناهُ المرج والمخضرة
والحندنة ويطلق 50 على كن شي ٠‏ 17 ܚ ( راجع 08003
اوعء ن < 24 20
19ل ܓ ) 2 إن مسكر فقيل بيذ العنب 1
ل ل العترةا ܒ ا ܡ 3 0 29775
® وهو الشراب العثيق وهو 2 2 جم اي ظاهر ماه ومن : هور اي ضوء
7 × الياء ع فعمي للنسمة ٠‏ ܀ -- وعندي 5 :41 نفسة ععنى اللماعة ܨ الناس
ومعظم كل سيء ܕܨ ܠ[ 3 × ܐܐܟܘ اليم ومعناه اللياعة
* (الجمثورة 3 المجموع تعريب © الهري
الصنوع من التراب
1 ( ܐܚܝ 0 الضخم والطويل وااعالي تعريب 35 الذي ° ٠١‏ والجنادف
ܢ 3 ܙ :ܐ ܕ أب والتنفج ان وي وغيرها» كلها لغمات فيه
وكلها ܚܨܢ الضخم والسمسين سمين ܐܥܛܢ ٠‏ عن جنبه معرب ايضأ (الغنبقة ) اي 31
الستّئة الخاق ٠‏ والمنفس واللفنس لفتان فيها
ܝܘ كاه ومعناه الاثم وقالوا فيه جنحة اي 6 اليه اما ٠‏ <
ايضأ معربة ( التَاية) يعنى الذف وان 1 راق ما 92105 ع ܐܝܐ ܝ في
الاصل )11 3 من الشجر ثم قلت الى إحداث الشر ثم الى الشر ثم 30
حرم ( حيط الحيط )
5 ܝܐ والجند ܢܡܡ ) خصية حيوان البحر له قشر ܘ بادلى
مس وهو كلل النفخ ويطرد الرياح ٠وقيل‏ هو خصي حيوان بري يقال له كل الاء ٠‏
050 ܝ 096 :4 3 ܨ ܡ وهو كلب المساء
ܨ ܩܐ انسل 1 ܝܢܐ ܐܢ 3 تصتع من جاده فراء فاخرة 9
3:1
=== AFM leaf 48 ===
ري لد
3 ذات 9 × 90[ 5 1503
دار اي حافظ
( حدر ناندع 1" مر القلم على ما درس منة ܝܠܝܟ ْ ٠ماخوذ‏ من حندره ومعناها
ܝܬܐܕ الماش
(الجتاغ » فشر بضرب من ܓ قلت فارسيّتَهُ مجناغ ثوب مرضع
منقّش يِلتَى على السرج لازينة ١٠و‏ من المحتمل الَّهُ معرب عن 39
القدح والقصعة
( الجَنك) من آلات الطرب تعريب جنك
(الغنان) تعريب جنار وهو الدلل ٠‏ والصنار لغة فيه ٠‏ ومنة الكردى
رحنار
ܨ 0 1 نيدن لفظا ومعنى
+( 6 رد رحا قتا رمن الكل : نامك 1055 0 150
الخجل :3 ܚܨ
ولي 3 الناقد العارفه ميج احمذ 0:0 0 3
ا وى وحار تا ؛ الت في ܥܐ ويطكق على النساك وعلى الناقد والعارف
والدلّال
0:0000 1 معرب ܫܩ اي قطعة من الل وهو يطلق
بافارسية على حصان قوي عظي |
(الجَهبلة » المرأة القبيحة تمري ب ܐܢ اي الأحق الثقيل
( الجهاركاه ) اللحن الرابع من ܐܝܠܐ الموسيقى ܐܚܠܬ جهاركاه واصل معناه
الباب الرابع
( الجهارة ) . حسن |( والن تعر يب جهره ومعئاه ما الانسان وطاعتة ووجهة
وسحتة رومنة الحهزة بالار كة وانكرد ية ٠‏ واطن أن حير كد أ زمه ا `
ܢܟܐ
* ( الجهوّري» المرتفع العالي معرب عن جاهوار ومعناه ذو القدر وامازلة
(الجَوتمر) الأصل وكل 39 3 39 73 اغة فيه
```


## [2026-09-06T21:20:24.462Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"المستديرة\" AFM_pages.txt | head; echo \"=== pdfinfo ===\"; pdfinfo AFM.pdf 2>/dev/null | head -5",
 "description": "Grep Addi Shir for round-rock entry"
}
```


### [2026-09-06T21:20:26.332Z] TOOL RESULT

```
1118:* (الجاهة ) الصخرة العظيمة المستديرة تعريب كله
=== pdfinfo ===
Title:           كتاب الالفاظ الفارسية المعربة
Author:          السيد ادى شير (Author)
Creator:         Internet Archive
Producer:        Recoded by LuraDocument PDF v2.68
CreationDate:    Mon Aug  6 19:46:06 2018 EDT
```


## [2026-09-06T21:20:32.828Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && pdftoppm -f 46 -l 46 -r 220 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm46 && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm46.png'); print(im.size)\nim.crop((0,0,im.size[0],int(im.size[1]*0.35))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm46_top.png')\n\"",
 "description": "Render Addi Shir page image"
}
```


### [2026-09-06T21:20:41.262Z] TOOL RESULT

```
(2136, 3594)
```


## [2026-09-06T21:20:43.236Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm46_top.png"
}
```


### [2026-09-06T21:20:43.660Z] TOOL RESULT

```

```


## [2026-09-06T21:20:43.658Z] INPUT

[Image: original 2136x1257, displayed at 2000x1177. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-06T21:20:50.393Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 40 41 42; do echo \"=== AFM leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' AFM_pages.txt | head -35; done",
 "description": "Print AFM leaves 40-42"
}
```


### [2026-09-06T21:20:52.173Z] TOOL RESULT

```
=== AFM leaf 40 ===
راع
+ ( )ܥ ) عريب ند وهو زهر الرمآن والورد < 0 ايضا على
| ® “ذفني 8 0 6 0 عب القية
0 1 0 فارسلتة جو ܢ( وهو مركت من جوى
اي سيل دمن بار دهي من الأدوات | 3 تدل على الكثرة
+ ( أ مجار) بات ܦܟ سديه بورق الرطبة عليه زغب لطيف كالغبار وله
أغصان دقيقة مائة الى الحيرة وزهر احمر واصل خشبي غائر في الارض تعر يب
انكر
* ( اد ) الغليظ والبخيل «اللثيم 89 الخليظ الشخين . وعة
مغرب ايضاً ١١ل‏ س2 بمنى ܝ ܒ > المافي انس واخفس اليس
غات فبه رك الس ܐ 07 99 عن اليونالي. 4 ومنه 5 ܣܨ
فالس @ 3 5 ا للعة الريامة !ܐܬܟ 9 ܨ والأسارسي
جسين ماخوذ من ܐܝܟ يالى .ܕܘܐ الخص فعرب عن :3 ¢ الاراعى
ܓܨܐ ܦܟ 100 ܘܒ فيه ܡܝ قصّص ܫܩܢ (طالع 1
ص : \-- ›  \‏ وهو 0 حص € ¬ 79
` الجل القصيد < ب كهتر وهو ܐ م 6 أي صخيد ومن ثر وي
أداة التفضيل ٠‏ وكثر الابدال والتصحيف في هذه الكلمة حق صار فيها لغات عديدة.
ܐܝ ذلك قوم شها 1 )ܨ : .ܙ ܕܠ ܨ وا للعظ_ار
ܙ ܐܝܐܝ واللعير والمعبرى || يخ (طالع الشرق * 7
(الخثر) ܢܬܐ والش.سية ܚܠܨܐ ܡ ومنها ܫܬܪ بالسريانّة
* ܣ الملاء ܡ ترب يديس مب ابعر | `
له ܘ قطاع الطريق
# ( حثا ححثو ) .ܗ حا ܩܡ 5( 0 وهو £ المونانة 01/0١‏
* (المحنبار 1 ܐܐ( الجل = والعظيم !+ ܙ العظي
ܐܝ ` ܢܝ 7 ܬ ܬ ܨ ل ويطلق 2 خصوصي على ܐܝܚ ܐ
واصان وهو 20 13 اي جمل ومن ܨ بكار اي جِنّة
* ( الحم » الضيّق الخلق 6 ال
=== AFM leaf 41 ===
سس ܟܝܢ _
50) 3 م الطريق ووسطه تعر يب جأده واصل 7:1414 ]ܕܩܐܢ
الى القر نه .ܕܕ ܆4 @ ܫܝ بالكردنة لاما 3 95 ÷ ن الردمي
8 والصراط عن 5615218 ومنه ܐܣܛܪܛ
0 ( ܐܐ ) فارسي محض وهو اصل نماث و نت مع ܐܠܨ 59 2808
)ܕܨ فاسي 0 واخمر
( )ܥܪ ) ܟܫܐ ¦ ` :»> 60 3 ܚ 11 اب
( اللودّر) َلك 73 32970
1 ܨ( الثيء الفليظ 85( واصل 5 الثقيل الردي .
ومنه ايضياً ܘܝܨ
ܟ 33 الذى لامة 3
01 الخداع 377 3 .بز ومعئاة ܐܰܢ والشجاع وا مكار . وقالوا
٠ 0973 5‏ 30 لغة فيه
0 (اطرنانة) المرأة الصحًابة < السرزئة الخاق ܐܦܬ من كران بن واصل
معناها الثقية الاصل ` 35 3
الراك ܨܝ والطين الذي 2 به والصحيفة ܐܨ ܝ جرجشت والفاسي
ماخوذ من السرباني ܓܪ̈ܓܫܬܐ ̈ܨ ܝܨ ܝ فيه راجع كتاب فرذتكل ص :
07
63 000 طرفت ترتى عَنها 5 من لدرخ
ومعناها الفا !© وتطاق على جميع ܠܠܝ القى تدور 0 والمكرة < ومنها
حرخ بالتركة والكردنة
(الحرداب) معظم ابعر تعريب ܐܢ الذي 1
13:1§ 1 000 09 وال ܕܝ ,ܐܪܝܐ ) الدذى ي يضع 2 على
شي : : يككون على الحوان لثلا 415 غيره فاذا نع رع القوم من الطعا م يا كله ٠و(‏ جردم
ܓ ܕ ܝ 6 ذلك ماخوذ من ܝ بان تعلاة 5 الرغيف ْ 00
لكر ده :1 ( اردق واطردقة 39 331 ܬ اي الرغيف
13332 20
=== AFM leaf 42 ===
ܚܝ ܀ 4 ندا
(١ 4‏ 9 5 5 95 5:7950 0705 10590
ال ا يا ܐ حديد وأكار من المقمعة ٠‏ ܀ وعئه 0
+ 7 ܦܝ 0 ܇ ܕܕ ! فيه 113 اي قثل وقطم
: ( ܨ( نوع من 157 يدنع من < ٠.وعند‏ الاطاء ¦ نوع من
الأدوة تعريب 9 واصل معناه الحضام ܕܐܐ ܓܘܪܫܝܐ
ع ܫ ܐܟ ܕ س ,ܐ ܚ ܙ !)ܪ̈ܐ ,1 13050
ܩ ܐ ܫ 3 وا ربع ܣ
ܙ ܩ )ܐܨ ܙ وار ياض واردَحَل واسراهم واخرائ»ة 3 0 ܨ
والقسحب والفرادس والغرضاح والّْأ ردخ ,ܐܨ ܢ ܙܐ مح والشّر مح ܕܐܐܐ
والشرناض والشرواض والشرواص والشرداح والشرابث والسر داح والسرداحة
ܐܠ سق ) وغيرها : كل ذلك يمنى العظلم 00 الضخم الثقيل إن كان من الرجال
وإ ن كان من اللموانات ا 2 ܝ الغريب عن 5 2
واحدة فارسية 56 ومعناه القوي الظهر 95 وعظيمة ان انساناً وان
ا :
+ (الرعبيل ) الغليظ تمر = 5 ` < القامة
( 05079 صبغ احمر عن الاصمعي ٠‏ وقال ابن الاعرالي الطريال ` من
لور مر وغيره وقيل جريال ܐܶܟ ܐܕܐ شيل ܝ ܀ الغلئل انما
روسة 19 فرنكل ( ܟ : \ ܘ) 1 خمفة من ܐܟܐܠ 0 اي المرجان ٠‏
قلبت أن الكلمة تعاب ع الفارسي زربون وهو 2 من زر 5 ذه اوهن زر
3 ܡ ` - ومن يون اي لون ٠‏ وزر يون بالفارسيّة يطلق على اللون الأأصفر
دعلى مشقسائق النعمان وعلى الرجل < .ويا بؤيد قولنا ان جريون ` ]` 5 في
الجريال المعرب ٠‏ ويون الفارسي تصحيف كون وقالوا 0 ` لونة لون النار
9 الخار .ܓ ومنة ايضاً الكردي وم
١‏ الْرْمُوق ) ما ܢܟ فوق الخف ܚܐܢܫܐܘ من الطين معرب سر مُوذه وهو مركب
2 7 08:10
* ( 9 0 ` .معرب 98 حب `
```


## [2026-09-06T21:21:04.167Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && pdftoppm -f 41 -l 41 -r 220 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41 && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.08),w,int(h*0.55))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41_a.png')\nim.crop((0,int(h*0.5),w,int(h*0.95))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41_b.png')\n\"",
 "description": "Render AFM leaf 41 (printed p.39)"
}
```


### [2026-09-06T21:21:10.621Z] TOOL RESULT

```
(2136, 3594)
```


## [2026-09-06T21:21:12.854Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41_a.png"
}
```


### [2026-09-06T21:21:13.360Z] TOOL RESULT

```

```


## [2026-09-06T21:21:13.358Z] INPUT

[Image: original 2136x1689, displayed at 2000x1581. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-06T21:21:19.292Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm41_b.png"
}
```


### [2026-09-06T21:21:19.764Z] TOOL RESULT

```

```


## [2026-09-06T21:21:19.762Z] INPUT

[Image: original 2136x1617, displayed at 2000x1514. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-06T21:21:48.373Z] TOOL CALL #45: Bash

```json
{
 "command": "for u in \\\n \"https://www.ahdictionary.com/word/search.html?q=jar\" \\\n \"https://abadis.ir/fatofa/%D8%AC%D8%B1%D9%87/\" \\\n \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B3/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 277: jar / jarreh / kās lookups\" ; done",
 "description": "Fetch AHD and abadis pages"
}
```


## [2026-09-06T21:21:50.171Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ISS/Bailey pig ===\"; grep -n -i \"'pig'\\|\\\"pig\\\"\\|swine\" ISS_alt_DKS.txt | head -10; echo \"=== CHEUNG kas ===\"; grep -n -i \"pig\\b\" CHEUNG.txt | head -10; echo \"=== HRN kas ===\"; grep -n -i \"Schwein\" HRN.txt HUB.txt | head -10",
 "description": "Grep Bailey/Cheung/Horn for pig"
}
```


### [2026-09-06T21:21:53.779Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/67b1fbe66f591f93.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/243b0916c3bf34ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b2ed3910ccecf89.txt
```


### [2026-09-06T21:21:53.851Z] TOOL RESULT

```
=== ISS/Bailey pig ===
4428:pá$a 'swine's', genitive to рӣѕа-, Sid. 16v4 páía gusta ‘flesh of pig’, BS mamsam oarahan, Tib. phag-fa; Sid. 9r2 рай gūsta, BS varaha-, Tib. bhag-ía—v 318-58 pveśä gušta, See рӣѕа-.
4439:pása- ‘рів, Һор’, v 62:12 päsä salya ‘іп the hog year’; пш 15:54 püsi salya (without subscript hook) ‘hog year’ (in animal cycle no. 12 after їое dog); HI трт påsi ‘9-11 p-m.’ (BSOS 8, 1937, 928 animal cycle pasa-, Sogd. Ёз, NW Prakrit Kroraina sug'ara, BS sikara, Tokhara B suwo); gen. sing. Sid. gr2 рай gūsta 'pig's flesh’, BS väräha-, Tib. phag-éa, =V 318:58 ровй gusta; їп gr-221 фай ісага. From *pülsa- to *parsa- or *prsa-, with intrusive -o- pvaíd, ровй. Ау. perosó in Nirangastün 114v9-1o yaba huš parosü, see K. Hoffmann, Münchener Studien 22, 1967, 20#. IE Pok. 841 porfo-s, Finn. lw porsas, Mordwin puris, Lat. porcus, O.Engl. fearh, Lit. pařšas, O.Slav. prasę. See for IE, E. Benveniste, BSL 45, 1949, 74-
4835:pya— pviys- 257 pig’, Sid. gra pasi gusta 'pig's Hesh', =v 318, 58 рше gusta. With intrusive -v- after labial p-. See pasa- from *palsa-, Lat. porcus.
4866:pvesü ' pig's', gen. sing., Sid. v 318:58 pues gusta 'pig's flesh’, —Sid. gr2 рӣ5 gūsta. See påsa-.
5748:byuyäre 'they catch alight’, Z 4:59 ssundānu pürrá byüyare “е ravens’ wings catch fire’, From aui- 'to burn’, rare in Iranian, see Zaza vei-, Brühüi lw Лийпр 'to burn’; Armen. lw atrouían 'fire-temple', from atra and aušana- 'burning-place', IE Pok. 347-8 eus-, O.Ind. dsatš, usjd-, иўпа- ‘Пос’, Greek eco, ejorpa ' pit to singe slaughtered swine’, Lat. rō, ustus, O.Norse usli ‘glowing ashes’, O.Engl. ysl; O.Norse ysa ‘fire’, eim-yrja, O.Engl. &m-yrie ‘embers’, Lit. usnis ‘thistle’, бее ñautcai ‘pungent (?)’, and /tausja-.
=== CHEUNG kas ===
28710:*IE COGNATES: Lat. -cerda ‘excrements (of mice, pig, cow and sheep)’, (with mobile 
=== HRN kas ===
HUB.txt:7638:xUk Schwein' = phi. xUk 61. and Ind. 53 = zd. hu-; xujlr
HUB.txt:8512:*Stachelschwein — zd. sukurena- (Neuausgabe, var. suku-
HUB.txt:8589:(nom.); dig gestern' (neben di), bal. zlk; xug 'Schwein
HRN.txt:4609:510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
HRN.txt:4612:skr. siikard- 'Eber, Schwein*.
HRN.txt:6481:744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
HRN.txt:6488:schwein' (345).
```


## [2026-09-06T21:22:00.639Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### abadis جره\"; grep -n -i -A4 \"معین\\|فرهنگ فارسی\" 243b0916c3bf34ac.txt | head -50",
 "description": "Read abadis jarreh"
}
```


### [2026-09-06T21:22:00.691Z] TOOL RESULT

```
##### abadis جره
37: فرهنگ فارسی
38-
39- خمچه، سبو، کوزه بزرگ دسته دار، جرارجمع، جانوراعم ازپرنده یاچرنده، بازنر، چابک، دلیری
40-( اسم ) ۱- جنس نر جانوران بطور عام . ۲- باز نر باز سفید ( اعم از نر یا ماده )
41-نهر ... نهر جره از ماصرم برخیزد و نخست مسجان را آب دهد و برود و جره و نواحی آنرا آب دهد و بعضی از روستای غندجان پس با نهر بشاپور آمیخته شود و در دریا افتد . 
--
43: فرهنگ معین
44-
45- (جُ رِّ ) (اِ. ) ۱ - جنس نر جانوران از هر نوع . ۲ - باز نر.
46- (جَ رِّ ) [ ع . ] (اِ. ) ۱ - دام برای شکار آهو و غیره . ۲ - خرمهره . ۳ - سبو.
47- (جُ رِ ) (ص مر. ) نوجوان . 
--
160: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
161-
162- لینک ها 
163-
164- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد.
```


## [2026-09-06T21:22:07.854Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### abadis کاس\"; sed -n '25,70p' 8b2ed3910ccecf89.txt",
 "description": "Read abadis kās"
}
```


### [2026-09-06T21:22:07.898Z] TOOL RESULT

```
##### abadis کاس
هم او ریخت در طاس حکمت زلال 
هم او کوفت بر کاس دولت دوال. امیرخسرو دهلوی.
|| خوک. ( لغت فرس اسدی ). بمعنی خوک نر هم آمده است که جفت خوک باشد . ( برهان ). || در عربی کاسه و پیاله را گویند. ( برهان ). کأس. رجوع به کأس شود. || ( ص ) در اصطلاح بنایان فرورفته ، مقابل قوزدار. قوزی. || تیره و به رنگ زاغ. ازرق ، کبود: عینک کاس ، شیشه کاس. || نامی از نامهای مردم گیلان ، کاس آقا، کاس گل ، غالباً به افراد کبودچشم گفته میشود. 

 فرهنگ فارسی

 ( اسم ) جعب. خانه خانه که حروف سربی را در آن ریزند گارسه 

 فرهنگ معین

 ( کأس ) (کَ ) [ ع . ] (اِ. ) کاسه ، پیاله . ج . کرؤس . (اِ. ) کوس ، طبل بزرگ .
 [ سغ . ] (اِ. ) خوک نر. 

 فرهنگ عمید

 خوک.
۱. پیالۀ شراب.
۲. کاسه.
۳. [مجاز] شراب.
نقارۀ بزرگ، کوس. 

 گویش مازنی

 /kaas/ زرد رنگ پریده – زاغ - ناقص و کج و معوج ۳آلت تناسلی زن & رنگ سفید مایل به خاکستری - کاسه & ناقص – دارای کاستی - به دامی گفته شود که در قسمت پستان دچار نقص باشد

 واژه نامه بختیاریکا

 فقیر و طمع کار؛ آس و پاس؛ ندار؛ گدا؛ آس و کاس

 دانشنامه اسلامی

 [ویکی الکتاب] معنی کَأْسٍ : ظرف مخصوص نوشیدنیها-قدح-جام(ظرف مخصوص نوشیدنیها البته در صورتی که نوشیدنی در آن باشد )
ریشه کلمه: 
 کئس (۶ بار)

«کَأْس» (بر وزن رأس) نزد اهل لغت، به ظرفی گفته می شود که پر و لبریز باشد، و اگر خالی باشد، معمولاً به آن «قدح» می گویند. «راغب» در «مفردات» می گوید: اَلْکَأْسُ الاِنَاءُ بِمَا فِیْهِ مِنَ الشَّرابِ: «کأس به معنای ظرفی است که پر از نوشیدنی باشد». و گاه به خود جام یا محتوای آن نیز اطلاق می شود.
راغب می‏گوید: کأس ظرف است با شراب «اَلْاِناءُ بِما فیهِ مِنَ الشَّرابِ» و در ظرف تنها و شراب تنها نیز به کار رود طبرسی نیز ذیل آیه . ظرف توأم با شراب گفته و از اخفش نقل کرده: مراد از هر کأس در قرآن خمر است (خمر بهشتی). در صحاح از ابن اعرابی نقل شده: ظرف را کأس نگویند مگر اینکه در آن شراب باشد. این لفظ شش بار در قرآن مجید آمده است و مراد از آن کاسه‏های پر از شراب بهشتی است . نیکوکاران از کاسه‏ای یا شرابی می‏خورند که آمیخته آن کافور بخصوصی است. wikialkb: کَأْس 

 دانشنامه آزاد فارسی

 کاس (اخترشناسی)
رجوع شود به:باطیه wikijoo: کاس 

 جدول کلمات

 ظرف, جام, کاسه
```


## [2026-09-06T21:22:08.910Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg277.png"
}
```


### [2026-09-06T21:22:09.246Z] TOOL RESULT

```

```


## [2026-09-06T21:22:09.244Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:22:21.029Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -B3 -A6 \"jar\" 67b1fbe66f591f93.txt | head -60",
 "description": "Read AHD jar entry"
}
```


### [2026-09-06T21:22:21.076Z] TOOL RESULT

```
1:URL: https://www.ahdictionary.com/word/search.html?q=jar
2-FETCHED: 2026-09-06T21:21:50Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: jar
5-
6:American Heritage Dictionary Entry: jar 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
11- guide to the dictionary 
12-
--
38- INTERESTED IN DICTIONARIES?
39- Check out the Dictionary Society of North America at http://www.dictionarysociety.com 
40-
41: jar  1 (jär) 
42- Share: 
43-
44- Tweet 
45-
46- n. 1. A cylindrical glass or earthenware vessel with a wide mouth and usually no handles.
47: 2. The amount that a jar can hold.
48- 3. Chiefly British A glass of beer.
49-
50: tr.v. jarred , jar·ring , jars To put into a jar.
51-
52: [Middle English jarre , a liquid measure, from Old French (from Provençal jarra ) and from Medieval Latin jarra , both from Arabic jarra , earthen jar, from jarra , to draw, pull; see grr in the Appendix of Semitic roots .]
53: jar  ful ′ n. 
54-
55- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
56-
57: jar  2 (jär) 
58- Share: 
59-
60- Tweet 
61-
62: v. jarred , jar·ring , jars 
63: v. intr. 1. a. To cause shaking or vibrations: The ride over the old road was jarring. 
64: b. To shake or vibrate from an impact or impacts: "The gallery jarred with a quick, heavy tramp" (Robert Louis Stevenson). 
65-
66: 2. To be disturbing or irritating; grate: The incessant talking jarred on my nerves. 
67: 3. To be out of harmony; clash or conflict: The curtains jar with the rest of the room. 
68-
69: v. tr. 1. To cause to shake or vibrate from impact: The ride on the donkey jarred my bones. 
70: 2. To startle or unsettle; shock: The alarm jarred him out of sleep. 
71-
72- n. A jolt; a shock.
73-
74- [Perhaps of imitative origin.]
75: jar  ring·ly adv. 
76-
77- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
78-
79- Indo-European & Semitic Roots Appendices
80- Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
81- Indo-European Roots
```


## [2026-09-06T21:22:21.689Z] TOOL CALL #51: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1563 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 1563"
}
```


### [2026-09-06T21:22:28.810Z] TOOL RESULT

```
REF: BQT:1563  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 356  OCR-lang: fas

-۱۹۳-< کاست کار
تا صید ازآن رمیده بطرف دام ودانه آید باخود که نقاره بز رکه است ۴ - و بمعنی خوذ رهم
در عقب آن پنهان شده دام را بکشند - وسایبان | آمده است که جفت خوك ماده باشد ۴ - و در
را نی ز گویند . عربی کاسه و پیاله راگوبند ۵ .
کاژه ۱ * بفّج‌زای فارسی » خانه‌ومنزل کاسان * بروزن آمان , نام دهی باشد
و مقام را کوبند عموماً - وکمینگاه صیاد را | از نواحی سمرفند که بر شمال اخسیکت وافع
خصوصاً : است ‎٩۹‏ .
کاژ بره۲- با زای فارمی » بر وزن کاسانه ۷ * بر وزن جانانه ۰ مرفکی
و هعنی کاجیره است و آن دانه ای باشد سفید | باشد سبزرنگه بسرخی مابل ودرولایت خوزستان
که روغن از آن گیرند و آنرا بمربی احریض | بسیار است ۸ .
خوانند ؛ و بمض ی کوبند احریض کل کازیرهاست کاست ‎٩‏ بروزن راست» بمعئی دروغ
که‌بم‌بی آنر| عصفر ومصفر خوانند؛ وبعنی کل | باشدکه عربان کذب میگونند.- وماضی کاستن
آنراکاژیره‌میگویند که مصفر باشده وهضی‌نبات | هم‌هت بعنی‌کاهید وکم شد.
آن را چه گلکاریژه و تخم کاژیره مشهوراست. کاست کاد - باکاف بالف کشیدم‌ویرای
کاس بروزن طای » بهءن ی کوی‌باشد | قرشت زده» دروخ گو برا کوبند چه‌کاست بمعنی
۹ < کاز < کازه (و.م.) ۰ ۲ < کاجیره (و.م.).
۴ - هم او ریخت در طای حکمت زلال هم اوکوفت بر کاس دولت دوال .
امیرخرو دهلوی. « فرهنگه نظام >.
۴ - اسدی کوید ( لغت فری ص ۱۹۹ ): «کاس » خوك بود؟ و ۷25 همان‌کلمهمعمول
سغدی ۲75 است . درفارسی‌کاسموی ( موی زر ) آمده [ رك :کاسموی ۱ . بنظر میرسد که‌کلمه
«کاس» بالانفراد هر کز در فارسی استعمال نشده باشد . لغت نوبان ناگزیر از «کاسموی» کلمه‌ای
بمعنی « خوك > استخراج کرده‌اند وبی درنگه کاس را بمعنی خوك درفرهتگهای خود آورده‌اند »
و حتی معشکوك اس ت که فردوسی‌کاس را بمعنی خوك گفته باشد ( رك : عبدالقادر ۱۹۸۳ » ورك :
فهرست ولف ) باید دانست که فردوسی قاعدة ازلغات مستمار ازایرانی شرقی احتراز میجوید. گر
چه بیاری‌ازآنها توسط عءبدالقادر بدو نسبت دازه‌شده امت . 1080 5084128 ,ق۲1605180)
(. 0.99 , ... ۷۵۲۵8 ولی درين بیت کاس بمعنی مذ کور آهده :
اندر کفش آن تیغ درخشنده شب داج کفتی توکه بعك از زفر کای برآهد .
عرالدین طبسی . « جهانگیری»رك: کاسموی .
- (م) « کاس بالفتح جام شراب خوردن با جام با شراب .» «منتهی الارب» .
‎٩‏ - شهری بز رکه دراول پلاد ترکستان ورای نهرسیحون و ورای شاش (چاج) ودارای"
فلمه‌ای استوار است و برناب‌آن وادی اخسیکث امت . «ممجم‌الپلدان » .
۷ -قن : کاسکنه.
۸ -چندپویی بگرد عالم» چند؟ چند کویی طربق پوبایی ؟
زانکه از بهر قوت شهوت همچو کاسانه می‌نیاسایی .
عمعق بخباری ۸« لت فرس 6*۵ *.
‎٩‏ -رك : کاستن ۰
```


## [2026-09-06T21:22:54.277Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1939\\b\" HENNING_selected_papers.txt | head -10; echo \"=== TOC first ===\"; sed -n '70,80p' HENNING_selected_papers.txt",
 "description": "Check Henning volume coverage"
}
```


### [2026-09-06T21:22:54.338Z] TOOL RESULT

```
438:to read thus instead of (Use, the name of the royal clan of the Qurlug ace. to Gardezi (see Minorsky, op. cit., p. 288).—(10)  Kashgharian,” see BSOS,, ix, p. 567. Of. also Bailey, JRAS., 1939 p- 89.—(11) “Khotanese,” ywSnyk is xwa8anik or xd5anik, with an unexpected 8, Saka hratana, later hyamna, etc., Niya doc. kholana, Baréuq Saka Aradana, headna (g = d), etc. According to a much joussed passage of the T'an,
460:‘Thomas-Konow, Tico Medieval Documents, pp. 146 sq.) ?—(19) Hardly tobe read tnywt, In any case, the name of the Tangut (Si-hia) would be spelt t'nkwt = Orkhon inscr. taut, ef. also Saka tamgdt-, Bailey, JRAS,, 1939, p. 89.—Apparently we have to read ¢'yrot = Saka agua, Stael-Holstein scroll, lines 9, 42, which Professor Thomas identified with Tib. Sta-gu (see above, nr. 18), Professor Bailey informs ‘me that in unpublished Saka texts he has found evidence which seems to suggest that ttdgitta refers to Tibet and is an alternative spelling of tdmbatta, BSOS., ix, p. 542. We are looking forward with great interest to the full publication of this important discovery. We should have two forms of the name of Tibet in Sogdian, t’yiet and ¢wp'tet- (Karabalgasun, line 19; thus also to be read in the insor. of Ladakh, where the top of the second w is damaged; Miller: twp'wyt, Benveniste, BSOS., ix, p. 504: ttep’nyt or trep'yyl)—(20) The Merkit, who, at the beginning of the thirteenth century, were livingto the south and east of the Ike Baikal, to the north-east of the Naiman, the northern neighbours of the Uiyurs of Turfan. ‘The head of the Merkit was among the tribal chiefs whom Je-li Ta-si, the founder of the Qura-Xitai (Si Linu) dynasty, convoked at Bishbali (Liaw-i, transl, Bretschneider, Researches, i, p. 213). 1 do not: know anything about their earlier habitations and history. They have conjecturally been connected with the Moux pi ( Fragment VI, 9), ef. Marquart, Branéahr, p. 54; Minorsky, op. cit., p. 448.—(21) ‘The Mikri, who lived in the mountains of the eastern T'ien-gan, mostly around Hami. The Chinese ambassador who in a.p. 1220 travelled to Chingiz-Khan, met the “Mo-li-hi"* and the “Mo-K’o- with the Qirqiz, Neiman, and other tribes in the T'ien-gan region, doubtless the Merkit and the Mikri(t), as recognized by Bretschneider, op. cit., i, p. 28. Still in Ming times the “ Me-k‘o-li"” inhabited the mountains to the north-east of Hami, Bretschneider, ibid., ii, p. 178. Professor Minorsky kindly referred me to Rashid al Din, vii, 90, 166, ed. Bérézine: the Mikrin/Bikrin, different from the Merkit/Mekrit, lived in the mountains of the Uiyur country and were called gayaét
3132:Essar SUR LA LAXGUE Parris. Son systéme verbal. D'apris les textes manichéens du Turkestan Oriental: By A. Guttars Bibliothéque du Muséon, vol. 9. Louvain, 1939. 18 The study of the
8655:Tt seems to me that this information can be supplemented and (in part) corrected with the help of Sogdian Manichman calendar tables published here for the first time. ‘They had been referred to before by F. W. K. Miller (in Sb.P.4.W., 1907, 465) and by myself (in Orientalia, vii, 1939, 87-95) for the purpose of establishing the correct forms of the names of the Sogdian days and months.
10166:O11, By'n yon'y = Raurara (Skt. and Chin. reference to raurava in BSOS., IX (1939), 511 89 interpretation of mkyze (ibid., p. 499) can be understood only with the indered why M. Benv
17024:bears an ornament on its head (2); it is not correctly centred for lack of space (the lower panel interfered). Compare the throne of Ardavin on the stele of Khwasak (which is carried by winged griffins according to Ghirshman), and the statue published by H. Seyrig, Syria, xx (1939) 182 59
17188:spite of the difference in headgear (the small conical helmet would not afford sufficient protection in war.)! The typically Parthian dagger is clearly visible on the rider’s right thigh, of the lange statue found at Shami and A. Godard’s remarks, Athar-é lrdn, ii, 297 8q. (see also H, Seyrig, Syria, xx (1939), 177-81). The large object behind the rider's leg was recognized by Stein as a quiver; it is very broad and probably was bowease and quiver combined* (¢f. Noldeke, Tabari, 249); it is divided lengthwise into three compartments (cf. the equally broad quiver of Ardavin at Firizibid, which is bisected vertically). Portions of the rich surface ornamentation on the quiver and on the middle of the cuirass can stil be seen. ‘The rider wears a leather cuirass over a coat of scale armour with brassarts of annulate plate armour (cf.the Parthian warriors at Firdizabad), The horse, too, is protected by plate (scale) armour; its suit has a projection before the chest, w gives it the appearance of a funnel (or oven) and may be responsible for the origin of the term clibanarius (differently Noldeke, Tabari, 164, 1. §); the projection was open in front to allow some movement to the forelegs; the whole suit bore no resemblance to the Sassanian bargustu- edn represented at Taq-i Bustin. OF the three soldiers sketched in the top left-hand corner of the panel, one is shown throwing a stone (correctly seen by de Bode), the second shooting an arrow, the third falling down backwards; their style of dress differs from that of the other figures in Tang-i Sarvak, The bowman and the stone-thrower carry long swords, attached to shoulder belts in Roman fashion, Behind the stone-thrower’s legs, a little above the butt of the lance, one sees an implement, which de Bode regarded as a hammer, while Stein took it for a ring and chain; perhaps it is a battle-axe, a tabarain, with a ring for attachment to the belt.
18091:inscription who will have to be deposed. There are the persons, chiefly at the nd of the inscription, whom Herafeld regarded as * Saka kgatropas’ from the Indo-Iranian borderlands, Outstanding among them is the Lord of Avanti (the | country around Ujjain). I discussed him and a few of his colleagues in an article on the inscription of Shapuri at the Ka‘be-yi Zanduit which I contributed to the Volume in Memory of A. V. W. Jackson. That article, which was sent to Bombay in March, 1939, at a time when of the inscription of Shapur the | defective Pahlavi version alone was known to exist, has never been published *; it may not come amiss to quote the relevant paragraph here in full (with annotations, in the form in which it was written thirteen years ago
20898:Three years later, before we could complete the work, the «discovery » of the very same Qunyah was announced by S.L. Volin and A.A Freyman in two articles (Zapiski Instituta Vostokovedeniya Akad. Nauk, vii, 1939, 79-91, 306-319), of which the former repeats Professor Togan’s lecture and the latter reproduces what I had said, These two articles are unhampered by consideration of our clear priority; in Freyman’s article the only acknowledgement made is in a sentence of classical brevity at the end: «the study of the Khwarezmian language proceeds also abroad» (p, 319, with reference to ZDMG., 90, but without mention of our names). One gains the impression that in the opinion of these two authors the task of analysing the Khwarezmian language was so easy that its accomplishment deserved no credit; it is true that it is easy after it has been accomplished by someone else.
20915:Ever since 1939 A.A. Freyman has published a series of articles on the various features of the Khwarezmian language, without, however, fulfilling his promise of making the text of the Qunyah accessible in a proper edition. Only in his latest paper, contained in Sovetskoe Vostokovedenie, vi, 1949, pp. 63-88, has he made a beginning with the systematic publication of the Khwarezmian sentences, although still withholding the Arabic context and, for the greater part, the Arabic and Persian glosses explaining the Khwarezmian words !
=== TOC first ===
Sogdica, James G. Forlong Fund, Vol. XX1, London, 1940 (67 p. with Errata and addenda) 1
“Sulphur” in Sogdian (BSOS, 1940, p. 398) @
  
   
 
Compte rendu de E. Hexzreto, Archaeologische Mitteilungen «us Iran (BSOAS, 1940. pp. 501-507) 1 Compte rendu de A. Guitatn, Essai sur la langue parthe (BSOAS, 1940, pp. 508-509) 7%
Mani’s Last Journey (BSOAS, 1942, pp. 941-953), 81 An Astronomical Chapter of the Bundahishn (JRAS, 1942 pp. 229-248) 95
The Book of the €
 
ants (BSOAS, 1943, pp. 52-74) Ms
```


## [2026-09-06T21:22:55.607Z] TOOL CALL #53: Bash

```json
{
 "command": "curl -s \"https://archive.org/advancedsearch.php?q=henning+selected+papers&fl%5B%5D=identifier&fl%5B%5D=title&rows=20&output=json\" 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); [print(x.get('identifier'),'|',x.get('title')) for x in d['response']['docs']]\" 2>&1 | head -25",
 "description": "Search archive.org for Henning Selected Papers I"
}
```


### [2026-09-06T21:22:57.958Z] TOOL RESULT

```
1913-june-11-atlanta-constitution-14-pages-georgia | 1913 June 11 Atlanta Constitution 14 Pages Georgia
1913-june-11-atlanta-journal-20-pages-georgia | 1913 June 11 Atlanta Journal 20 Pages Georgia
1913-06-11-dictograph-records-crooked-says-gentry | Wednesday, 11th June 1913 Dictograph Records Crooked, Says Gentry(page 1,2, column 7,1)
springer_10.1007-978-3-642-38082-2 | The Future Internet [electronic resource] : Future Internet Assembly 2013: Validated Results and New Horizons
NASA_NTRS_Archive_20110016803 | NASA Technical Reports Server (NTRS) 20110016803: Selected Papers on Protoplanetary Disks
1913-06-11-gentry-now-says-dictograph-record-was-tampered-with | Wednesday, 11th June 1913 Gentry Now Says Dictograph Record Was Tampered With
TheFutureInternet | The Future Internet [electronic resource] : Future Internet Assembly 2013: Validated Results and New Horizons
w.-b.-henning-selected-papers_202108 | W. B. Henning Selected Papers
1913-06-11-plot-exposed-says-felder-but-lanford-doubts-affidavit-the-atlanta-georgian | 1913 06 11 Plot Exposed Says Felder But Lanford Doubts Affidavit The Atlanta Georgian
1913-june-12-atlanta-constitution-14-pages-georgia | 1913 June 12 Atlanta Constitution 14 Pages Georgia
w.-b.-henning-selected-papers | W. B. Henning Selected Papers
wiredwirelessint0000wwic | Wired/wireless internet communications : 8th international conference, WWIC 2010, Luleå, Sweden, June 1-3, 2010 : proceedings
1913-06-11-gentry-now-says-dictograph-record-was-tampered-with_202606 | Wednesday, 11th June 1913 Gentry Now Says Dictograph Record Was Tampered With
cia-readingroom-document-cia-rdp90g01353r001300110002-8 | CIA Reading Room cia-rdp90g01353r001300110002-8: LETTER TO PAUL SEABURY FROM ROBERT M. GATES
computationallog0000clim_o9g2 | Computational logic in multi-agent systems : 7th international workshop, CLIMA VII, Hakodate, Japan, May 8-9, 2006 : revised selected and invited papers
renderingtechniq0000gort | Rendering Techniques 2001 : Proceedings of the Eurographics Workshop in London, United Kingdom, June 25-27, 2001
```


## [2026-09-06T21:23:05.844Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp && meta=$(curl -s \"https://archive.org/metadata/w.-b.-henning-selected-papers_202108\"); echo \"$meta\" | python3 -c \"\nimport sys,json\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d.get('files',[]):\n    if f['name'].endswith(('.pdf','_djvu.txt')): print(f['name'], f.get('size'))\n\" 2>&1 | head -20",
 "description": "Check Henning IA item files"
}
```


### [2026-09-06T21:23:09.466Z] TOOL RESULT

```
ia803204.us.archive.org /14/items/w.-b.-henning-selected-papers_202108
W. B. Henning selected papers.pdf 67218669
W. B. Henning selected papers_djvu.txt 1640467
W. B. Henning selected papers_text.pdf 13956257
```


## [2026-09-06T21:23:12.810Z] TOOL CALL #55: Bash

```json
{
 "command": "curl -sG 'https://ia803204.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=w.-b.-henning-selected-papers_202108' --data-urlencode 'doc=W. B. Henning selected papers' --data-urlencode 'path=/14/items/w.-b.-henning-selected-papers_202108' --data-urlencode 'q=Sogdian Loan-Words' 2>/dev/null | head -c 2000",
 "description": "Full-text search Henning item"
}
```


### [2026-09-06T21:23:18.922Z] TOOL RESULT

```
{"ia": "w.-b.-henning-selected-papers_202108", "q": "Sogdian Loan-Words", "indexed": true, "matches": [{"text": "\u201cSulphur\u201d in <IA_FTS_MATCH>Sogdian</IA_FTS_MATCH> (BSOS, 1940, p. 398) @", "par": [{"l": 171, "t": 274, "r": 216, "b": 283, "page": 8, "boxes": [{"l": 171, "t": 274, "r": 216, "b": 283, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "The murder of the Magi (JRAS, 1944, pp. 133-144) 139 The Disintegration of the A vestic Studies (TPS, 1942, pp. 40-56) 151 <IA_FTS_MATCH>Sogdian</IA_FTS_MATCH> Tales (BSOAS 945, pp. 465-487) 169 Brihman (TPS, 1944, pp. 108-118) 193 The Manichaean Fasts (JRAS, 1945, pp. 146-164) 205 Waru\u00e9iin-Sih (Journal of the Greater India Society, 1945, X1/2,", "par": [{"l": 86, "t": 468, "r": 131, "b": 481, "page": 8, "boxes": [{"l": 86, "t": 468, "r": 131, "b": 481, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "The <IA_FTS_MATCH>Sogdian</IA_FTS_MATCH> Texts of Paris (BSOAS, 1946, pp. 713-740)", "par": [{"l": 111, "t": 557, "r": 156, "b": 569, "page": 8, "boxes": [{"l": 111, "t": 557, "r": 156, "b": 569, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "Two Central Asian <IA_FTS_MATCH>Words</IA_FTS_MATCH> (TPS, 1945, pp. 150-162)", "par": [{"l": 204, "t": 575, "r": 239, "b": 585, "page": 8, "boxes": [{"l": 204, "t": 575, "r": 239, "b": 585, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "A <IA_FTS_MATCH>Sogdian</IA_FTS_MATCH> Fragment of the Manichacan Cosmogony (BSOAS", "par": [{"l": 100, "t": 628, "r": 145, "b": 640, "page": 8, "boxes": [{"l": 100, "t": 628, "r": 145, "b": 640, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "1948, pp. 306-318) 301 The Date of the <IA_FTS_MATCH>Sogdian</IA_FTS_MATCH> Ancient Letters (BSOAS, 1948,", "par": [{"l": 202, "t": 663, "r": 246, "b": 676, "page": 8, "boxes": [{"l": 202, "t": 663, "r": 246, "b": 676, "page": 8}], "page_width": 646, "page_height": 1008}]}, {"text": "A <IA_FTS_MATCH>Sogdian</IA_FT
```


## [2026-09-06T21:23:30.887Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ kura ===\"; grep -n -i \"kura\\|كرة\" FVQ.txt | head -5; echo \"=== TAD جرة/كرة ===\"; grep -n \"الجرة\\|كرة\" TAD_pages.txt | head -10; echo \"=== ARB ===\"; grep -n \"جرة\\|كرة\" ARB_mo3rb.txt | head -10; echo \"=== DOZ jarre ===\"; grep -n -i \"jarre\\|kruik\" DOZ.txt | head -5; echo \"=== LAM jarre ===\"; grep -n -i \"^JARRE\\|jarre\" LAM.txt | head -5; echo \"=== SKT jar ===\"; grep -n \"^Jar\\b\\|Jar,\" SKT.txt | head -5",
 "description": "More cross-checks in Arabic and French sources"
}
```


### [2026-09-06T21:23:30.989Z] TOOL RESULT

```
=== FVQ kura ===
3396:3 Kiinstlinger, " Die Herkunft des Wortes Iblia im Kuran," in Rocznik Orjen- 
12935:4 See Kunstlinger, " Tur und Gabal im Kuran," in Rocznik Orjentalistyczny, v 
15931:Vide Kiinatlinger, " Christliehe Herkunft der Kuranischen Lotlegende," in 
=== TAD جرة/كرة ===
32: ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬
80:‫فاى أن هذهالطريقةلابعتزيقاةلالكلام معبانكرة وممهما‬   ‫يربخفل‬‫أمونضاع الع‬
231: ‫معمخورائط ب يوئاني ‪ 52114‬وهو اسملجار حامل الكرة الارضية‬        ‫طلس‬
1416:‫سكرة ‪ -‬عامي أرامي سوك ماع»ناه _مثلاق أعيما يغلق باهلباب ويقفل‬
1741:                 ‫طابة ‏ عاميترك طوب » معناه كرةمرادفه كجّة‬
2143:      ‫وهو وع سن الهوخ كرة شه حب‬               ‫بوناني ‪8‬‬       ‫قراسيأ وقراصا‬
3114:‫هذكرة فى تركيب الاو_اس اكور بائية‬                 ‫‪4‬‬         ‫المساديون ومم الذين ذغوا هن النقر‬
3116:         ‫قمة حمرّه البلوان اوبعة احزاء‬        ‫‪١‬و‏‬     ‫تركيا وى المذكرة المقدءةالىزمؤتمر لوزان‬
=== ARB ===
1246:م : مم والشذرات م : بهم وذكره الذهى" فى وفيات التذكرة م : 88" ٠‏ 
1515:(.ه- #ه) وهو صاحب كاب الأفساب . له ترجمة حافلة فى تذكرة الحفاظ 
1635:قال ابن النجار فيا نقله عنه الحافظ الذهى فى تذكرة الحفاظ غ :مم فى ترجمة 
3572:ولا م أن 50 من الزيا أده 5 المحذوفة ٠‏ وإن حذنت الآحرة ا لت «أويجرة» ٠‏ 
3857:وقال فى شرحها : « والامنجرة الملا'ى تفيض ود كها » والمتعنجر والمسحتفر : السيل الكثير » ٠‏ 
5019:ومريب » ٠‏ وفى القاموس « الأنبج كأحجد وتكسر باه : ثمرة شجرة هندية » معرب أنب» ٠‏ وف المادة 
5611:أبن رسولا الفسانى صاحب الهن » وتذكرة داود ٠‏ وقوله « تحر » مم « تاج » ٠‏ « وقأرة المسك » 
5802:والببرمان دونه نشىء قالجرة ٠ ٠‏ (4) كة « البرازيق » لم نذى فى ى وهو خطأ ٠‏ وق الاسان 
6627:كرة: دراه البسل وانا نو الأمر انع «الاغيرب من الفدل بالجترين أ بها + ونان ابو عرو 
6822:بمد اطجرة » وكان حينئذ مر القوافل من الموصل إلى نصيبين عايها » فأما الآن س فى عصر ياقوت 
=== DOZ jarre ===
1522:theu* hands." Deze „ kruik in den vorm van een Etrus-
=== LAM jarre ===
264:par g (doux) : genette, gerboise; / : jambette, jarre, javarî,
4655:Jarre, (i) Grande cruche; de ïjr garra, même sens.
4657:une mesure pour les liquides usitée au Levant. « La jarre
6157:que de la conquête de l'Algérie. Dans les Alpujarres
7009:Trévoux.— <( Des jarres, dont l'ouverture paraît recouverte d'un parchemin,
=== SKT jar ===
6580:ftligrree.  Span.  -  U)  Formerly //«'- grvnt;  XVII  cent.  —  Span./Zi^rana,  fili- gree-work, fine  wrought  work.  — Span. ^/d, a  thread  or  tow,  JiJar,  to  spin ;  gutno,  grain or  texture ;  so  called  because  the  chief texture  of  it  was  wrought  in  silver  wiie. From  X^filnm,  thread;  ^ranum^  grain.
9429:Jar  (1),  to  nuUce  a  harsh  notsc  ^ It  stands  for  an  older  form  (Hmt,  m found  in  the  derivative  chatJun,  to  CM (.Prompt  Parv.)  Again,  rfiar  «  U% Teut.  base  KAR,  conei base  GAR,  as  seen  in  L crook  i  sec  Garrulooa
9431:Jar  (3\   an  earthen  pot.    (F. O,  F.  Jart,  '  a  Jarre  ; '  Col. a  jar;  cf.  Pers.  Jurrah^  »   linli jar.
20884:lontcnd  fur  gaperiorily,  (F.  — tfieUt  a  contracted  form  of  /«• ,  contend  for  wperiority.  (Cf. }frt*<tt  story  for  history^  flee.)  — r  {flH  ifu), '  to  vie ; '  Cot.  The if  O.  F.  envter  was  to  Invite |ct  from  tHviir,  to  envy],  esp. Initti;  in  the  icnse  'to  o\kh  a kking  a  certain  sum  ; '  precisely ViJar,  Iial.  invitare,  to  invite, Vopose  a  &lake.  —  1^  inuitart^ '  wnich  nV  it  thus  seen  to  be  a See  Invite.  ^  The  scn&e  was m  to  draw  on  or  invite  a  game, get,  bet  against,  contend,  iitnve ir  hand, to  Vision.
```


## [2026-09-06T21:23:40.510Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T21:23:40.548Z] TOOL RESULT

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


## [2026-09-06T21:24:00.889Z] AGENT

Now let me write the verification file.


## [2026-09-06T21:24:25.771Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/39.vision.txt <<'EOF'\n[Addi Shir, al-Alfaz al-farisiyya al-mu'arraba, Beirut 1908 — printed p. 39 = AFM.pdf leaf 41\n (offset: leaf = printed page + 2; verified against leaf 46 whose running number reads ٤٤).\n Read from the page image (pdftoppm -f 41 -r 220) because the OCR of AFM_pages.txt is\n unreliable for this page. Entries on p. 39, in order:]\n\n* ( الجَادَّة ) مُعظم الطريق ووسطهُ تعريب جاده واصل معناهُ المكان المُوصل الى القرية. ومنهُ جاده\n  بالتركيَّة وجَعْـد بالكرديَّة. وامّا السمت فمعرب عن الرومي semita والصراط عن strata\n* ( الجَدْوَار ) فارسيّ محض وهو اصل نباتٍ ينبت مع البيش ومنفردًا عنه\n  ( الجَادِي ) فارسيّ بحت وهو الزعفران والخمر\n  ( الجُوذَاب ) طعام يُتَّخذ من سكَّر ورز وجوز ولحم تعريب كُوذَاب\n  ( الجَوْذَر ) ولد البقرة الوحشيَّة معرب گُودَر\n* ( الجَرَنْبَذ ) الشيء الغليظ مشتق من گِران بَد واصل معناهُ الثقيل الردي\n* ( الجَرَنْبَذَة ) الذي لامِّهِ زوج\n  ( الجُرْبُز ) الخدَّاع الخبيث تعريب گُربُز ومعناهُ الذكيّ والشجاع والمكَّار\n* ( الجِرِبَّانَة ) المرأة الصخَّابة البذيئة السيّئة الخلق مشتقَّة من گِران بِن\n  ( الجِرْجِس ) الشمع والطين الذي يُختَم به والصحيفة تعريب جرجشت والفارسي ماخوذ من\n    السرياني … (راجع كتاب فرنكل ص ٢٥٢)\n  ( الجُرُوخ ) من ادوات الحرب تُرمى عنها السهام والحجارة مشتقَّة من چرخ ومعناها الفلك …\n  ( الجِرْدَاب ) معظم البحر تعريب گِرداب الذي بمعناهُ\n  ( الجَرْدَبَان والجُرْدُبان والجَرْدَبِيّ والمُجَردِب والجَرْدَبيل ) … كل ذلك ماخوذ من گِرده بان\n    ومعناهُ حافظ الرغيف. ومن گِرْدَه معرّب ايضًا ( الجُرْدَق والجُرْدَقة والجُرْذَقة والجُرْذَق ) اي الرغيف\n* ( الجَرَّة ) اناء من خزف تعريب كُرَه            <<< the line Nourai cites (AFM:39)\n\n[So Addi Shir does say: al-jarra \"an earthenware vessel\" is an Arabicization of Persian\n kura/kora. This is the source Asbaghi (PLA p. 85) cites in turn (\"ǧurra 'Gefäß aus Glas'\n aus dem pers. kore\", footnote 8 = \"Addai Scher s.v.\").]\nEOF\necho saved",
 "description": "Save Addi Shir p.39 vision reading"
}
```


### [2026-09-06T21:24:27.488Z] TOOL RESULT

```
saved
```


## [2026-09-06T21:28:45.679Z] TOOL CALL #59: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-277.json",
 "content": "{\n  \"pdf_page\": 277,\n  \"book_page\": 247,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"K.r.v\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ك ر و (k-r-w), noun كُرَة kura(t) 'ball, sphere, globe'\",\n      \"note\": \"Nourai's 'K.r.v' is the Arabic triliteral ك ر و with v standing for wāw; the noun كُرَة kura (pl. كُرَات kurāt, كُرًى kuran, كُرُون kurūn) is a genuine Classical Arabic word for 'ball, sphere', so the root box (language label and gloss) is right. Wiktionary raises a further, pre-Arabic layer for it (a possible Aramaic transmission of Akkadian kurru, ultimately Sumerian GUR), which lies behind Nourai's box and does not affect it. The chart's problem is not the root but the arrow from Persian koreh to Arabic jarra (node #3): Nourai's own references (Addi Shir AFM:39, echoed by Asbaghi PLA:85) do assert it, but Fraenkel, Klein, Lokotsch, Lammens and Pihan all treat Arabic جرّة as native Arabic from the root ج ر ر.\",\n      \"note_fa\": \"ریشهٔ عربی ك ر و و نام کُرَة (جمع کُرات، کُرًى، کُرُون) به معنی «گوی، کره» واژه‌ای اصیل و کهن در عربی کلاسیک است؛ بنابراین برچسب زبان و معنای جعبهٔ ریشه در نمودار نورایی درست است. ویکی‌واژه لایه‌ای کهن‌تر (اکدی kurru از راه آرامی، و در نهایت سومری GUR) را نیز محتمل می‌داند که خارج از ادعای نورایی است. اشکال اصلی این نمودار در گرهٔ ۳ است: پیوند «کُرهٔ فارسی ← جَرّهٔ عربی». ادّی شیر (ص ۳۹) و به پیروی او اصغی (ص ۸۵) همین را گفته‌اند، امّا فرنکل، کلاین، لوکوچ، لامنس و پیهان جَرّه را واژه‌ای سره‌عربی از ریشهٔ ج ر ر «کشیدن» می‌دانند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%A9\",\n        \"https://www.ahdictionary.com/word/search.html?q=jar\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVA:350\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989) — refs_online.json records that no digital copy exists on archive.org, ketabnak, noorlib or the open web (re-searched 2026-09); catalogue record only.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"Wiktionary\", \"where\": \"s.v. كرة, Etymology 1\", \"stance\": \"partial\", \"note\": \"'كُرَة (kura) f ... ball; sphere, globe', but the etymology given is 'Likely through Aramaic, from Akkadian 𒄥 (kurru), ultimately from Sumerian 𒄥 (GUR, \\\"a bundle, rolled up barley\\\")' — i.e. the word is real with exactly Nourai's gloss, but its ultimate origin may not be a native Arabic ك ر و root.\"},\n        {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. jar¹, Semitic roots appendix\", \"stance\": \"partial\", \"note\": \"AHD's Semitic-root apparatus assigns Arabic jarra to the root grr ('from jarra, to draw, pull; see grr in the Appendix of Semitic roots'); it has no entry making kura the source of anything on this chart.\"},\n        {\"src\": \"FVQ\", \"where\": \"grepped FVQ.txt for kura / كرة\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no entry for كرة (the word is not Qur'anic), so it neither supports nor contradicts a foreign origin.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"koreh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic كُرَة kura(t) 'ball, sphere, globe' is the standard deverbal noun of the weak-lām root ك ر و: underlying *kurawat- > kurat- with loss of the intervocalic wāw, whence the irregular plurals كُرًى kuran and كُرُون kurūn beside the sound plural كُرَات kurāt, all of which betray the original III-w stem. It is Classical (used of the polo ball, al-kura wa-l-ṣawlajān, in early ʿAbbasid prose) and became the technical term of the astronomers for the celestial sphere (al-kura al-falakiyya) and later for 'planet'. Nourai's node simply spells out the root box, so it stands; the only reservation is Wiktionary's suggestion that the word itself may be an old Mesopotamian culture-word carried into Arabic through Aramaic.\",\n          \"derivation_fa\": \"کُرَة در عربی اسمی است از ریشهٔ ناقصِ واوی ك ر و: صورت اصلی ‎*kurawat‎ بوده که با افتادن واو میان دو واکه به kurat بدل شده؛ جمع‌های نامنظم کُرًى و کُرُون در کنار کُرات همین ستاک واوی را نشان می‌دهند. واژه در عربی کلاسیک (در ترکیب «الکرة والصولجان» = گوی و چوگان) به کار رفته و سپس در نجوم به معنی «کرهٔ فلکی» و «سیّاره» اصطلاح شده است. ادعای نورایی در این گره درست است؛ تنها احتیاط آن است که ویکی‌واژه خودِ این واژه را وام‌واژه‌ای بین‌النهرینی (اکدی kurru از راه آرامی) می‌داند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:350\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi is not digitized anywhere on the permitted platforms (refs_online.json, re-searched 2026-09).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. كرة, Arabic, Etymology 1\", \"stance\": \"supports\", \"note\": \"'كُرَة • (kura) f (dual كُرَتَان, plural كُرَات or كُرًى ... or كُرُون) — ball; sphere, globe' — Nourai's form and gloss exactly; descendants listed are Ottoman Turkish küre and Azerbaijani kürə.\"},\n            {\"src\": \"TAD\", \"where\": \"grepped TAD_pages.txt (al-Unaysi, Tafsir al-alfaz al-dakhila) for كرة\", \"stance\": \"silent\", \"note\": \"the only hits are unrelated (طابة 'ball' explained from Turkish طوب, line 1741: 'عامي ترك طوب، معناه كرة'); al-Unaysi does not list كرة among the borrowed words, i.e. he treats it as Arabic.\"},\n            {\"src\": \"ARB\", \"where\": \"grepped ARB_mo3rb.txt (al-Jawaliqi, al-Mu'arrab) for كرة\", \"stance\": \"silent\", \"note\": \"no headword كرة in al-Jawaliqi's list of arabized words; the medieval Arabic tradition therefore did not regard it as a loan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"koreh «کُره»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian کُره kore 'sphere, globe, planet' is a straight loan from Arabic كُرَة kura, taken over with the scientific vocabulary of astronomy and geometry from the 4th/10th century onward (کرهٔ زمین, کرهٔ آسمان); the chart's script_extra کُرات is the Arabic sound feminine plural kurāt used unchanged in Persian, itself proof of the Arabic source, since a native Persian noun would pluralize in -hā/-ān. The word is homonymous in Persian with two inherited words spelt the same — کُرّه korre 'colt' (< MP kurrag, Old Iranian *kurna-ka-) and کَره kare 'butter' (< MP *karag) — which is why the dictionaries number the entries.\",\n          \"derivation_fa\": \"«کُره» در فارسی نو وام‌واژه‌ای مستقیم از عربی كُرَة است که همراه با واژگان علمی نجوم و هندسه از سدهٔ چهارم هجری به فارسی راه یافته است (کرهٔ زمین، کرهٔ آسمان). جمعِ «کُرات» که در نمودار آمده همان جمع مؤنث سالم عربی kurāt است و خود گواه عربی‌بودن واژه است، زیرا اسم فارسی سره با ـها/ـان جمع بسته می‌شد. این واژه با دو واژهٔ ایرانی هم‌نویسه اشتباه نشود: «کُرّه» (بچّهٔ اسب، از فارسی میانهٔ kurrag) و «کَره» (روغن، از فارسی میانهٔ ‎*karag‎). معین نیز آن را با نشان [ع.] عربی دانسته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:350\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary of Arabic loans in Persian; but the claim it is cited for (Persian کره < Arabic كرة) is the standard one and is confirmed independently below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. کره, Persian, Etymology 2\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic كُرَة (kura).' — exactly Nourai's arrow. (Etymology 1 there is کَره 'butter' < MP *karag, Etymology 3 کُرّه 'colt' < MP kwlk' /kurrag/ — different words.)\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کره, via abadis.ir\", \"stance\": \"supports\", \"note\": \"'کره: [ع. کرة] (اِ.) گوی (اعم از ...)' (MON_part2.txt line 22645) — Mo'in tags the word [ع.] = Arabic and glosses it 'gūy, ball', beside the separate entries کره [= کرو، کری] and کره [معر. کرج].\"},\n            {\"src\": \"ARY\", \"where\": \"grepped ARY_pages.txt / ARY_latin_index_pages.txt for کره 'sphere'\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry for this کره, as expected for an Arabic loan.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"jarrah\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"This is the weak link of the chart. Arabic جَرَّة jarra 'earthenware jar' is treated by every Semitist as a native Arabic noun of the geminate root ج ر ر 'to drag, draw': Fraenkel (AFA, in the chapter on vessel-names) lists it explicitly among the 'zwei echt arabische Namen für den Krug' and derives it 'zur Wurzel جرّ \\\"ziehen\\\"' (a vessel is named from being dragged/drawn, as Syriac qūqā 'jug' is from its root), and AHD's Semitic appendix likewise sends jarra to the root grr. Nourai's derivation from Persian کُره kora is not his invention: Addi Shir (AFM p. 39) ends his ج section with '(الجَرَّة) اناء من خزف تعريب كُرَه' — 'al-jarra, an earthenware vessel, arabized from Persian kura' — and Asbaghi (PLA p. 85) repeats it on Addi Shir's authority ('ǧurra \\\"Gefäß aus Glas\\\" aus dem pers. kore', footnote 8 = 'Addai Scher s. v.'). But phonetically Arabic has no rule turning Persian k- into j- (Persian k is normally kept, as in kūza > kūz, or rendered by q/g), and the gemination -rr- of jarra is unexplained from kora; semantically 'sphere' → 'earthen pot' is a leap. Addi Shir is well known for over-assigning Arabic words to Persian, and the argument is in any case circular, since Persian کُره is itself a loan from Arabic كُرَة (node #2). Modern scholarship therefore rejects the arrow: jarra is Arabic, and the resemblance to kora is accidental.\",\n          \"derivation_fa\": \"این سست‌ترین حلقهٔ نمودار است. جَرَّة در عربی نام کوزهٔ سفالین است و سامی‌شناسان آن را واژه‌ای سره‌عربی از ریشهٔ مضاعف ج ر ر «کشیدن» می‌دانند؛ فرنکل صریحاً آن را یکی از «دو نام سره‌عربی برای کوزه» می‌شمارد و به ریشهٔ جرّ بازمی‌گرداند، و پیوست ریشه‌های سامی فرهنگ American Heritage نیز همان را می‌گوید. البته نورایی این را از خود نساخته است: ادّی شیر در ص ۳۹ می‌نویسد «(الجَرَّة) اناء من خزف تعریب کُرَه» و اصغی (ص ۸۵) همان را به نقل از او تکرار می‌کند. امّا از نظر آوایی هیچ قاعده‌ای «ک» فارسی را در معرّب‌سازی به «ج» بدل نمی‌کند (مقایسه کنید کوزه > کوز)، مشدّدشدن ر در جَرّه بی‌توجیه می‌مانَد، و از «گوی» به «کوزهٔ گلی» جهش معنایی بزرگی لازم است. افزون بر این، استدلال دوری است، زیرا «کُرهٔ» فارسی خود وام‌واژه‌ای از كُرَة عربی است (گرهٔ ۲). ادّی شیر به فارسی‌انگاشتنِ بی‌رویهٔ واژه‌های عربی شهره است؛ پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/jar\",\n            \"https://www.ahdictionary.com/word/search.html?q=jar\",\n            \"https://en.wiktionary.org/wiki/jar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FSD:1312\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls, s.v. jar (FSD_vol2.txt line 63357): '... jarra. < Ar. jarra, < Per. jarrah, jar.]' — F&W does end the chain in Persian, though it says nothing about kura/kora; F&W is one of the older dictionaries that took the Persian step from Addi Shir's tradition via the Century Dictionary.\"},\n            {\"ref\": \"PLA:85\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 85 (PLA_pages.txt leaf 100; printed page = leaf − 15): 'ǧurra: \\\"Gefäß aus Glas\\\"⁸ aus dem pers. کره kore.' Footnote 8 = 'Addai Scher s. v.' — Asbaghi records the claim but only on Addi Shir's authority, adding no independent evidence.\"},\n            {\"ref\": \"AFM:39\", \"status\": \"supports\", \"note\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba, p. 39 (last line; AFM.pdf leaf 41, read from the page image and saved to data/verification/sources/refs/ocr/AFM/39.vision.txt): '* ( الجَرَّة ) اناء من خزف تعريب كُرَه' — 'al-jarra, an earthenware vessel, arabized from kura'. Exactly Nourai's arrow. Page identified by the printed numeral ٣٩ on the image.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, in the excursus on vessel-names (AFA.txt lines 2922-2931)\", \"stance\": \"contradicts\", \"note\": \"'[Zwei echt arabische Namen für den Krug sind ... und ...] ... جرة \\\"Krug\\\" gehört zur Wurzel جرّ \\\"ziehen\\\", wie ܩܘܩܐ \\\"Krug, Becher\\\", zu ... Auf dieses Wort geht bekanntlich fr. giarre \\\"Schiffskrug\\\", ital. giarra zurück.' — Fraenkel classes جرة as genuinely Arabic, from the root ج ر ر, and makes it the source of the Romance forms.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, s.v. jar (n.) (KLN_1966.txt line 20175)\", \"stance\": \"contradicts\", \"note\": \"'jar, n., a vessel of earthenware, glass or stone. — F. jarre, fr. OProvenç. jarra, fr. Arab. jarrah, \\\"a large earthen vessel\\\" (whence also Sp. jarra, It. giarra).' Klein stops at Arabic; no Persian, no kura.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 688 (LKT.txt line 1698)\", \"stance\": \"contradicts\", \"note\": \"'688. Ar. garra: \\\"Wassergefäß, Krug\\\"; hieraus it. giara, siz. giarra, prov. jarra, frz. jarre, sp. jarra, pg. zarra, jarra \\\"Krug\\\".' Lokotsch heads the entry 'Ar.', i.e. Arabic-origin, unlike his many 'Pers.' headings (e.g. no. 691 'Pers. čāršab').\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. jar¹\", \"stance\": \"contradicts\", \"note\": \"'... both from Arabic jarra, earthen jar, from jarra, to draw, pull; see grr in the Appendix of Semitic roots.' AHD derives it inside Semitic, from the root g-r-r.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/jar\", \"stance\": \"partial\", \"note\": \"'... all ultimately from Arabic jarrah \\\"earthen water vessel, ewer\\\" ... which is from Persian jarrah \\\"a jar, earthen water-vessel.\\\"' Etymonline keeps the old Persian step (as F&W and Skeat's 'cf. Pers. jurrah' do), but its Persian etymon is jarrah, not kura/kora, so it does not support Nourai's particular arrow either.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"jarreh «جَرّه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian جَرّه jarre 'jar, pitcher' is an ordinary Arabic loan of the ʿAbbasid period: Arabic jarra(t) with tāʾ marbūṭa was taken into Persian as -a/-e (jarra > jarre), the geminate -rr- being preserved in writing with tašdīd. Mo'in marks the word [ع.] = Arabic and glosses it 'سبو' (pitcher). It is thus a return-loan only if node #3 were right; on the mainstream view (jarra is native Arabic) it is a plain one-way borrowing into Persian, and the fact that Persian has to borrow the word at all is a further argument against the Persian origin of jarra.\",\n          \"derivation_fa\": \"«جَرّه» در فارسی نو وام‌واژه‌ای عادی از عربی جَرَّة است: تای مربوطهٔ عربی در فارسی به ـه بدل شده و تشدید ر در نوشتار حفظ مانده است. معین آن را با نشان [ع.] عربی می‌داند و «سبو» معنی می‌کند. اگر ادعای گرهٔ ۳ درست می‌بود، این واژه بازگشتِ وام (فارسی ← عربی ← فارسی) می‌شد؛ امّا بنا بر دیدگاه رایج که جَرّه سره‌عربی است، وام‌گیری یک‌سویه است، و همین که فارسی ناچار شده این واژه را وام بگیرد خود قرینه‌ای بر عربی‌بودن آن است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AC%D8%B1%D9%87/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1226\", \"status\": \"supports\", \"note\": \"Farhang-e Mo'in s.v. جرّه, read via abadis.ir: '(جَ رِّ) [ ع . ] (اِ. ) ۱ - دام برای شکار آهو و غیره . ۲ - خرمهره . ۳ - سبو.' — sense 3 سبو 'pitcher, jar', with the origin tag [ع.] = Arabic, i.e. exactly the arrow Arabic jarra → Persian jarre. (The print page number 1226 could not be checked: Mo'in's six-volume pagination is not reproduced online and MON_part1/2 OCR has no جرّه headword.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir s.v. جره\", \"stance\": \"supports\", \"note\": \"as quoted above; the homonym '(جُ رِّ) (اِ.) ۱ - جنس نر جانوران ... ۲ - باز نر' (jorre, the male falcon) is a different, Iranian word and is not what the chart means.\"},\n            {\"src\": \"Dehkhoda\", \"where\": \"Loghatnameh s.v. جره via abadis.ir\", \"stance\": \"supports\", \"note\": \"glosses جره as 'خمچه، سبو، کوزه بزرگ دسته‌دار' ('pitcher, jar, large handled jug'), confirming the sense Nourai gives ('jar').\"},\n            {\"src\": \"ARY\", \"where\": \"grepped ARY_pages.txt for جره\", \"stance\": \"silent\", \"note\": \"Aryanpur's Indo-European root dictionary has no entry, consistent with an Arabic loan rather than an inherited word.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"jarre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French jarre 'large earthen jar' is one of the best documented Arabisms of the Mediterranean oil and wine trade: Arabic jarra was picked up in the 13th-century western Mediterranean, appearing as Old Provençal/Catalan jarra, Spanish jarra, Italian giara/giarra and Medieval Latin jarra, and reached French through Provençal (whence the Provençal-looking -arre); the older French spelling giare, still in some dictionaries, shows the Italian route competing with it. Pihan's entry is emphatic that the French form was chosen precisely because it renders the Arabic tašdīd. Nourai draws the arrow straight from Arabic to French, which compresses but does not falsify the route.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی jarre «خمرهٔ سفالین بزرگ» از شناخته‌شده‌ترین وام‌واژه‌های عربیِ بازرگانی مدیترانه است: جَرَّة عربی در سدهٔ سیزدهم میلادی در مدیترانهٔ غربی به کار می‌رفت و به صورت‌های پروانسی/کاتالانی jarra، اسپانیایی jarra، ایتالیایی giara/giarra و لاتین میانهٔ jarra درآمد و از راه پروانسی به فرانسه رسید. صورت کهن‌تر فرانسویِ giare نشان می‌دهد که مسیر ایتالیایی نیز رقیب بوده است. پیهان تصریح می‌کند که صورت jarre را از آن رو برگزیده‌اند که تشدید عربی را بهتر می‌نمایانَد. پیکان مستقیم نورایی (عربی ← فرانسوی) مسیر را فشرده کرده، امّا نادرست نیست.\",\n          \"sources\": [\"https://www.etymonline.com/word/jar\"],\n          \"ref_check\": [\n            {\"ref\": \"PHN:217\", \"status\": \"supports\", \"note\": \"Pihan p. 217 (PHN.txt leaf 248 = printed 217; leaf = printed + 31): 'JARRE, s. f. (a.) جرّة [djarrat] grande cruche de terre cuite, à large ventre ... On trouve ce mot écrit giare dans quelques dictionnaires français, et giara en italien; mais l'usage a fait adopter jarre, qui se rapproche davantage du correspondant arabe, dont la seconde consonne est surmontée d'un techdid.' The '(a.)' tag = arabe: Pihan derives the French word from Arabic, with no Persian step.\"},\n            {\"ref\": \"AHD:701\", \"status\": \"partial\", \"note\": \"the 1975/76 AHD New College Edition (where p. 701 would fall in the J's) is not open online; the current AHD text was read instead at ahdictionary.com s.v. jar¹: '[Middle English jarre, a liquid measure, from Old French (from Provençal jarra) and from Medieval Latin jarra, both from Arabic jarra ...]' — same Arabic origin, but AHD routes English through Old French AND Medieval Latin rather than through French alone.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAM\", \"where\": \"Lammens, Remarques sur les mots français dérivés de l'arabe, s.v. Jarre (LAM.txt line 4655)\", \"stance\": \"supports\", \"note\": \"'Jarre, (i) Grande cruche; de جرّة garra, même sens.' — French from Arabic, same meaning, no intermediary language named.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 688\", \"stance\": \"supports\", \"note\": \"'hieraus it. giara \\\"Krug mit zwei Henkeln\\\", siz. giarra \\\"Ölkrug\\\", prov. jarra, frz. jarre, sp. jarra, pg. zarra, jarra \\\"Krug\\\"' — the Provençal link that mediates the French form is explicit here.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale, index entries 'Jarre', 'Jarra, hisp.', 'Giara, ital.', 'Zarra, pg.' (DEV.txt lines 3561, 3692-3694, 4490)\", \"stance\": \"supports\", \"note\": \"Devic collects Italian giara, Spanish jarra and Portuguese zarra all under his French headword Jarre, i.e. one Arabic etymon spread across the western Mediterranean.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, same passage as node #3\", \"stance\": \"supports\", \"note\": \"'Auf dieses Wort geht bekanntlich fr. giarre \\\"Schiffskrug\\\", ital. giarra zurück' — the French word comes from Arabic جرة.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"jar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English jar is first recorded in the early 15th century, at first as the name of a large container in which olive oil was imported from southern Spain and southern Italy, and only later as the ordinary word for a wide-mouthed vessel. Middle English jarre answers to French jarre and to Medieval Latin/Spanish jarra, all from Arabic jarra; the loss of the final -e and the shortening of the vowel are the regular English treatment. This is 'jar 1'; the verb jar 'to make a harsh noise' (jar 2) is a separate, probably imitative word, as Klein, Skeat and AHD all note.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی jar نخستین بار در آغاز سدهٔ پانزدهم میلادی دیده می‌شود، نخست به عنوان نام ظرف بزرگی که روغن زیتون را از جنوب اسپانیا و ایتالیا در آن وارد می‌کردند و سپس به معنی عام «کوزه، شیشهٔ دهان‌گشاد». صورت انگلیسی میانهٔ jarre برابر jarre فرانسوی و jarra لاتین میانه/اسپانیایی است و همه از جَرَّة عربی می‌آیند؛ افتادن ـه پایانی و کوتاه‌شدن واکه تحوّل عادی انگلیسی است. این jar شمارهٔ ۱ است؛ فعل jar به معنی «صدای ناهنجار کردن» واژه‌ای جداگانه و آوابنیاد است (کلاین، اسکیت، AHD). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/jar\",\n            \"https://www.ahdictionary.com/word/search.html?q=jar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FSD:1312\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls New Standard Dictionary, s.v. jar (FSD_vol2.txt line 63357, in the Japanese–jarret column block): '... jarra. < Ar. jarra, < Per. jarrah, jar.]' — the F&W etymology for the vessel-word runs French/Spanish jarra < Arabic jarra, i.e. the English←French step Nourai draws (the further Persian step is F&W's, and is the disputed one, see node #3).\"},\n            {\"ref\": \"TYL:568\", \"status\": \"not_checked\", \"note\": \"W. Taylor, 'Arabic Words in English' (S.P.E. Tract XXXVIII, Oxford 1933) is full view only on HathiTrust from a US browser and is not on archive.org or Google Books (refs_online.json, re-searched 2026-09); the local TYL folder holds only Taylor's different 1934 article on Arabic words in Ben Jonson, which has no 'jar' entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, s.v. jar (n.) (KLN_1966.txt line 20175)\", \"stance\": \"supports\", \"note\": \"'jar, n., a vessel of earthenware, glass or stone. — F. jarre, fr. OProvenç. jarra, fr. Arab. jarrah' — English from French exactly as drawn.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. Jar (3) (SKT.txt line 9431)\", \"stance\": \"partial\", \"note\": \"'Jar (3), an earthen pot. (F. ...) O. F. jarre, \\\"a Jarre;\\\" Cot. ... a jar; cf. Pers. jurrah, [a little] jar.' Skeat too takes English from Old French, but adds only a cautious 'cf.' to Persian jurrah, not a derivation.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. jar¹\", \"stance\": \"supports\", \"note\": \"'[Middle English jarre, a liquid measure, from Old French (from Provençal jarra) and from Medieval Latin jarra, both from Arabic jarra, earthen jar ...]'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/jar\", \"stance\": \"supports\", \"note\": \"'\\\"simple earthen or glass cylindrical vessel,\\\" early 15c. ... Originally in English a large container used for importing olive oil' — dates and sense-history as given in the derivation.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"K`s\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Sogdian k's (kās) 'pig, pork' (Buddhist, Manichaean and Christian Sogdian)\",\n      \"note\": \"The root box is right in every particular. Gharib's Sogdian dictionary, entry 4666, has 'k's B, M, S — kas (q's) ⓢKhwar. k's ⓢob. -y(y) — pork, pig', with references to the Buddhist texts (TSP 3.138, 9.44, 13.17), the Christian Sogdian ones (SCE 88, 122, 141, 360), the Ancient Letters (3.24) and, tellingly, 'Hen. LW 99' = Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10 (1939), p. 99 — Nourai's own second reference. Henning's Khwarezmian word-list (Selected Papers II) independently records 'k's «pig» (Sogd.)'. Note that the Sogdian word is not the inherited Iranian word for pig (Av. hū-, Khot. pāsa- < *parsa-, NP xūk), so it is itself of unclear Iranian pedigree; that question lies outside Nourai's box.\",\n      \"note_fa\": \"جعبهٔ ریشه در همهٔ جزئیات درست است. غریب در فرهنگ سغدی، مدخل ۴۶۶۶، می‌آورد: «k's (سغدی بودایی، مانوی و مسیحی) = kās، خوارزمی k's، به معنی خوک/گوشت خوک» و از جمله به «Hen. LW 99» یعنی مقالهٔ هنینگ «وام‌واژه‌های سغدی در فارسی نو» (BSOAS ۱۰، ۱۹۳۹، ص ۹۹) ارجاع می‌دهد — همان مأخذ دوم نورایی. هنینگ در فهرست واژه‌های خوارزمی خود نیز «k's «خوک» (سغدی)» را ثبت کرده است. توجه شود که این واژه دنبالهٔ واژهٔ موروثی ایرانی برای خوک نیست (اوستایی hū-، ختنی pāsa- از ‎*parsa-‎، فارسی خوک)، امّا این پرسش بیرون از ادعای نورایی است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"SOD:186\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 4666 (SOD_pages.txt leaf 251; printed page ≈ leaf − 66 = p. 185/186, matching Nourai's 186): '4666 k*s B, M, S — kas (q's) ©Khwar. k*s ©ob. -y(y) — pork, pig — TSP 3.138, 9.44, 13.17; SCE 88, 122, 141, 360; Anc. Lett. 3.24, BBB f8, 766; GMS 822, 1683; Hen. LW 99; Frye 2'. The dictionary's own index confirms it ('pork 4666', 'pig 4666, 4794, 5031').\"},\n        {\"ref\": \"SLW:99\", \"status\": \"not_checked\", \"note\": \"Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) 93-106 is reprinted in Selected Papers I (Acta Iranica 14), which is not on disk and not on archive.org — the local HENNING_selected_papers.txt is Selected Papers II (Acta Iranica 15), whose table of contents starts at 1940, and an archive.org full-text search of that item for 'Sogdian Loan-Words' returns only unrelated 1940+ titles. The page is however quoted for exactly this word by two independent authorities: Mo'in's footnote in Borhan-e Qate' p. 1563 cites '(Henning, Sogdian Loan-Words ..., p. 99)' for kās, and Gharib s.v. k's cites 'Hen. LW 99'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"HENNING\", \"where\": \"Selected Papers II, Khwarezmian word-list (HENNING_selected_papers.txt line 21212)\", \"stance\": \"supports\", \"note\": \"'K's «pig» (Sogd.)' — in Henning's list of Khwarezmian words from the Muqaddimat al-Adab, marked as shared with Sogdian; independent proof of the Sogdian word and its meaning.\"},\n        {\"src\": \"ISS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. pāsa- (ISS_alt_DKS.txt lines 4428-4439)\", \"stance\": \"partial\", \"note\": \"'pāsa- \\\"pig, hog\\\" ... From *pālsa- to *parsa- or *pṛsa- ... Av. parəsō ... IE Pok. 841 porḱo-s, Lat. porcus' — the Eastern Iranian word Bailey documents is the inherited *parsa-, not k's, i.e. Sogdian kās stands apart from the regular Iranian pig-word.\"},\n        {\"src\": \"BRT\", \"where\": \"grepped BRT.txt for an Avestan antecedent of k's\", \"stance\": \"silent\", \"note\": \"Bartholomae has no Avestan form that could underlie Sogdian k's; the Avestan words for pig are hū- and varāza-, so the Sogdian term has no Old Iranian etymon in the standard dictionary.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"kâs 2 «کاس ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian کاس kās 'pig, boar' is a Sogdian loanword taken into the Persian of Transoxiana and Khurasan in the Samanid period, when Sogdian was still spoken in the Zarafshan valley; the Sogdian form k's /kās/ was adopted unchanged, since Persian had no phonological adjustment to make. Mo'in states the borrowing twice: in his footnote to Borhan-e Qate' p. 1563 ('kās is the same as the common Sogdian word k's', citing Henning, Sogdian Loan-Words in New Persian p. 99) and in Farhang-e Mo'in itself, where the entry کاس in this sense carries the origin tag [سغ.] = Sogdian. Two reservations, both raised by Mo'in himself, must be recorded. (1) The word is mainly known from the compound کاسموی kās-mūy 'pig's bristle', the coarse hair cobblers wax on their thread, which Asadi Tusi glosses in Loghat-e Fors ('کاسموی: موی خوک بود که کفشگران بر رشته بندند', with Farrokhi's verse 'چو کاسموی گیاهان او برهنه زبر'); Mo'in suspects that 'کاس' alone was never used independently in Persian and that the lexicographers extracted it from the compound ('بنظر می‌رسد که کلمهٔ «کاس» بالانفراد هرگز در فارسی استعمال نشده باشد. لغت‌نویسان ناگزیر از «کاسموی» کلمه‌ای بمعنی «خوک» استخراج کرده‌اند'), and he doubts that Ferdowsi used it. (2) Against his own doubt he then adduces exactly the verse Nourai prints, by ʿEzz al-Dīn Ṭabasī via the Jahāngīrī dictionary, as a genuine attestation. So the arrow Sogdian k's → Persian kās is confirmed; what remains uncertain is only how firmly the simplex was established in literary Persian.\",\n          \"derivation_fa\": \"«کاس» در فارسی نو وام‌واژه‌ای سغدی است که در دورهٔ سامانی، هنگامی که سغدی هنوز در درّهٔ زرافشان زنده بود، از راه فارسیِ ماوراءالنهر و خراسان وارد شده است؛ صورت سغدی k's /kās/ بی هیچ دگرگونی آوایی پذیرفته شد. معین دو بار این وام‌گیری را تصریح می‌کند: یکی در حاشیهٔ برهان قاطع ص ۱۵۶۳ («و kās همان کلمهٔ معمول سغدی k's است»، با ارجاع به هنینگ، وام‌واژه‌های سغدی در فارسی نو، ص ۹۹) و دیگری در فرهنگ معین که مدخل «کاس» در این معنی را با نشان [سغ.] آورده است. دو احتیاط، هر دو از خودِ معین: نخست آنکه واژه بیشتر در ترکیب «کاسموی» (موی زبر خوک که کفشگران بر رشته می‌بندند؛ اسدی در لغت فرس، با بیت فرخی) شناخته است و معین گمان می‌برد «کاس» به تنهایی هرگز در فارسی به کار نرفته و لغت‌نویسان آن را از همین ترکیب بیرون کشیده‌اند؛ دوم آنکه خودِ او در برابر این تردید همان بیت عزالدین طبسی را که نورایی نقل کرده گواه کاربرد مستقل می‌آورد. پس پیکان «سغدی ← فارسی» درست است و تنها استواری کاربرد واژهٔ ساده در فارسی ادبی جای گفت‌وگو دارد.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B3/\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1563\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 1563 (fetched with tools/ref_page.py BQT:1563 = BQT_v3_picofile.pdf page 356). Main text: 'کاس بروزن طاس ... ۳ - و بمعنی خوک هم آمده است که جفت خوک ماده باشد'. Mo'in's footnote 3/4: 'اسدی گوید (لغت فرس ص ۱۹۹): «کاس» خوک بود؛ و kās همان کلمهٔ معمول سغدی k's است. در فارسی کاسموی (موی زبر) آمده [رک: کاسموی]. بنظر می‌رسد که کلمهٔ «کاس» بالانفراد هرگز در فارسی استعمال نشده باشد ... (Henning, Sogdian Loan-Words ..., p. 99). ولی درین بیت کاس بمعنی مذکور آمده: اندر کفش آن تیغ درخشندهٔ شب داج / گفتی تو که یشک از زفر کاس برآمد. عزالدین طبسی. «جهانگیری» رک: کاسموی.' The cited page carries the etymology, the Sogdian source, the Henning reference AND the very verse and poet attribution the chart prints.\"},\n            {\"ref\": \"SLW:99\", \"status\": \"not_checked\", \"note\": \"as at the root: BSOAS 10.1 (1939) / Selected Papers I is not accessible here; but Mo'in on BQT p. 1563 and Gharib s.v. k's both cite Henning p. 99 for precisely this Sogdian-to-Persian loan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کاس, via abadis.ir\", \"stance\": \"supports\", \"note\": \"the third sense block reads '[ سغ . ] (اِ. ) خوک نر.' — 'Sogdian, noun, male pig'. Mo'in's own dictionary thus tags the word Sogdian, exactly Nourai's arrow. (The preceding blocks are the Arabic کأس 'cup' and کوس 'kettledrum', unrelated homonyms.)\"},\n            {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors, s.v. کاسموی (FRS.txt lines 19313-19331, FRS_pages.txt 21514ff.)\", \"stance\": \"partial\", \"note\": \"'کاسموی: موی خوک بود که کفشگران بر رشته بندند [فرخی گوید: چو کاسموی گیاهان او برهنه زبر که چو شاخ بید، درختان او تهی از بار]' — the oldest attestation is the compound, not the simplex; a variant reading in the manuscripts even has 'کاسموی سبیل گراز باشد'. This is the evidence behind Mo'in's doubt that کاس stood alone.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie, no. 510 (HRN.txt line 4609)\", \"stance\": \"silent\", \"note\": \"Horn's Persian word for 'Schwein' is خوک xūk (with Sanskrit sūkará- adduced); he has no entry کاس, i.e. the word is not part of the inherited New Persian stock he treats — consistent with a late Sogdian loan.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 7638, 8589)\", \"stance\": \"silent\", \"note\": \"'xūk \\\"Schwein\\\" = phl. xūk ... = zd. hu-'; Hübschmann likewise records only xūk/xug and has no کاس, again pointing to a borrowed rather than inherited word.\"},\n            {\"src\": \"Dehkhoda\", \"where\": \"Loghatnameh s.v. کاس via abadis.ir\", \"stance\": \"supports\", \"note\": \"'|| خوک. (لغت فرس اسدی). بمعنی خوک نر هم آمده است که جفت خوک باشد. (برهان).' — Dehkhoda records the sense 'pig' with Asadi and Borhan as authorities, i.e. the same chain of evidence.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T21:28:45.714Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-277.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T21:28:48.538Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-277.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 277",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T21:28:50.675Z] TOOL RESULT

```
JSON OK
nodes verified: 7/7
node verdicts: {'confirmed': 6, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 4, 'supports': 7, 'partial': 1}
books consulted: {'supports': 14, 'silent': 6, 'contradicts': 4, 'partial': 3} | by book: {'MON': 3, 'Wiktionary': 2, 'ARY': 2, 'AFA': 2, 'KLN': 2, 'LKT': 2, 'AHD': 2, 'Etymonline': 2, 'Dehkhoda': 2, 'TAD': 1, 'ARB': 1, 'LAM': 1, 'DEV': 1, 'SKT': 1, 'FRS': 1, 'HRN': 1, 'HUB': 1}
```


## [2026-09-06T21:28:55.809Z] TOOL CALL #61: Bash

```json
{
 "command": "tail -8 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['file'], d['url'][:80])\n\"; echo; git status --short | head -30",
 "description": "Confirm archived sources and git status"
}
```


### [2026-09-06T21:28:57.628Z] TOOL RESULT

```
-1 data/verification/sources/web/80ffe871f7bb589d.txt https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A4%E0%
200 data/verification/sources/web/c3e840e994094f1f.txt https://en.wiktionary.org/wiki/κόρος
200 data/verification/sources/web/e8c6815e1df2bed4.txt https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%
200 data/verification/sources/web/480c721afb52995d.txt https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%B1
200 data/verification/sources/web/05fede3ea55ec731.txt https://abadis.ir/fatofa/%D8%B3%D8%A7%DA%A9%D8%A7%D8%B1%D8%B2/
200 data/verification/sources/web/4d661945493ddd27.txt https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AE%D8%A7%D8%B1%DB%8C/
200 data/verification/sources/web/978fb705c97a4d3e.txt https://en.wiktionary.org/wiki/%CE%BA%CF%81%CE%BF%CE%BA%CF%8C%CE%B4%CE%B5%CE%B9%
200 data/verification/sources/web/aba9ac32b01744d6.txt https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%85

?? data/verification/page-277.json
```


## [2026-09-06T21:29:06.981Z] TOOL CALL #62: Bash

```json
{
 "command": "for f in d9e8bf70354addc0 b23666a3b8fabbbd e9baa7324c2e7d46 e1fef3b99bab2cb6 f827e9692d827780 67b1fbe66f591f93 243b0916c3bf34ac 8b2ed3910ccecf89; do ls -la data/verification/sources/web/$f.txt 2>&1 | sed 's/^/  /'; done; echo \"=== index hits ===\"; grep -c . data/verification/sources/web/index.jsonl; for f in d9e8bf70354addc0 67b1fbe66f591f93 8b2ed3910ccecf89; do grep -c \"$f\" data/verification/sources/web/index.jsonl; done; echo \"=== git log -1 ===\"; git log --oneline -3; git status --short",
 "description": "Verify archived files and repo state"
}
```


### [2026-09-06T21:29:09.213Z] TOOL RESULT

```
  -rw-rw-r-- 1 sfmqrb sfmqrb 47474 Sep  6 17:19 data/verification/sources/web/d9e8bf70354addc0.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 8630 Sep  6 17:19 data/verification/sources/web/b23666a3b8fabbbd.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 8649 Sep  6 17:19 data/verification/sources/web/e9baa7324c2e7d46.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 6992 Sep  6 17:19 data/verification/sources/web/e1fef3b99bab2cb6.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 11866 Sep  6 17:19 data/verification/sources/web/f827e9692d827780.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 5522 Sep  6 17:21 data/verification/sources/web/67b1fbe66f591f93.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 14574 Sep  6 17:21 data/verification/sources/web/243b0916c3bf34ac.txt
  -rw-rw-r-- 1 sfmqrb sfmqrb 13780 Sep  6 17:21 data/verification/sources/web/8b2ed3910ccecf89.txt
=== index hits ===
3002
1
1
1
=== git log -1 ===
d0c4b93 Verify page 273 (Korkâ/šekar, sugar, saccharin, crocodile; Kormo/šarm, harm); fix ساکارُز script
8ba7ad0 Verify page 270 (Kleu 1/šenidan, xosrow, sorud, Slav, slave, loud)
5de8040 Verify page 271 (Klěu 2/kelid, eqlid, close; Klis/sereš, serešt)
?? data/verification/page-277.json
```


## [2026-09-06T21:29:28.800Z] AGENT

Done. Page 277 verified; `verify_check.py 277` reports 0 PROBLEM lines.

**Page 277 (book p. 247) — 2 entries, 7 nodes**

- Root verdicts: confirmed 2 · Node verdicts: confirmed 6, disputed 1
- Ref checks: supports 7, partial 1, not_checked 4 (FVA:350 — Nahvi's dictionary has no digital copy anywhere; TYL:568 — Taylor's S.P.E. Tract XXXVIII is HathiTrust-US only; SLW:99 ×2 — Henning 1939 is in Selected Papers I, which is not on disk or archive.org)
- Books consulted: 17 distinct (supports 14, silent 6, contradicts 4, partial 3)

**disputed (1)**
- `K.r.v` #3 Arabic *jarrah* ← Persian *koreh*: Nourai's own refs do back him — Addi Shir AFM p. 39 last line reads «(الجَرَّة) اناء من خزف تعريب كُرَه», and Asbaghi PLA p. 85 repeats it citing him — but Fraenkel (AFA) lists جرة among the "zwei echt arabische Namen für den Krug" from the root جرّ "ziehen", and Klein, Lokotsch no. 688, Lammens, Pihan and AHD all derive it inside Arabic (root g-r-r). Persian *k-* does not become Arabic *j-*, the gemination is unexplained, and the argument is circular since Persian کره is itself a loan from Arabic كرة.

**No transcription_suspect items, no extraction errors.** The JSON matches the printed page exactly (checked against a 200 dpi render of PDF p. 277), including "K.r.v", «کُره (کُرات)», «جَرّه», «کاس ۲ (کاسموی)» and the Ezzeddîn Tabasî verse.

Notable positives: BQT:1563 (fetched via `ref_page.py`) carries Mo'in's footnote giving the Sogdian source, the Henning p. 99 citation and the very verse Nourai prints; Farhang-e Mo'in tags کاس "خوک نر" as [سغ.]; Gharib SOD entry 4666 (leaf 251 ≈ printed p. 185/186) matches SOD:186.

New audit artifact written: `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/39.vision.txt` (Addi Shir p. 39 read from the page image, since the AFM OCR is unusable there; page offset for AFM is leaf = printed + 2).

Files: `/home/sfmqrb/git/rishe/data/verification/page-277.json` (untracked, ready to commit); 8 web sources archived under `/home/sfmqrb/git/rishe/data/verification/sources/web/` (already swept into a parallel agent's commit).
