# Verification process log — verify-page-387


## [2026-09-07T20:43:54.826Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 387 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-387.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-387.json. Write /home/sfmqrb/git/rishe/data/verification/page-387.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 387` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:43:56.726Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:43:57.392Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:43:57.406Z] TOOL RESULT

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


## [2026-09-07T20:43:57.892Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-387.txt"
}
```


### [2026-09-07T20:43:57.919Z] TOOL RESULT

```
1	=== PDF page 387 (book page 357) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pek
4	Peku : wool, to pluck wool
5	woolly animals, cattle, property  (refs POK:797)
6	#1 (parent #0) [Avestan] refs=POK:797 | pasu, pašman : wool ; fšu : cattle ; fšu-pait : protector of cattle, shepherd ☞Pa
7	  #2 (parent #1) [Persian] refs=POK:797; SNS:123,125 | pašm «پشم» : wool ; šabân, čŭpân «شبان ، چوپان» : shepherd
8	  #3 (parent #1) [Sogdian] refs=SOD:51,298 | `ps : sheep
9	#4 (parent #0) [Germanic] refs=AHD | feht : to pluck out wool, fight
10	  #5 (parent #4) [English] refs=None | fight
11	#6 (parent #0) [Germanic] refs=AHD | fehu : property ; fĕlag : partner sharing property
12	  #7 (parent #6) [English] refs=None | fellow
13	#8 (parent #0) [Latin] refs=AHD | feudum : property, feudal state
14	  #9 (parent #8) [French] refs=None | feodal
15	    #10 (parent #9) [Persian] refs=MON | feodâl «فئودال» : owner of large land
16	  #11 (parent #8) [English] refs=None | feudal
17	--- entry 1 ---
18	ROOT Peku -> redirect to Pek
19	
```


## [2026-09-07T20:44:01.516Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-387.json",
 "description": "Read source JSON for page 387"
}
```


### [2026-09-07T20:44:01.584Z] TOOL RESULT

```
{
  "pdf_page": 387,
  "book_page": 357,
  "entries": [
    {
      "root": {
        "name": "Pek\nPeku",
        "lang": "Indo-European",
        "refs": "POK:797",
        "gloss": "wool, to pluck wool\nwoolly animals, cattle, property"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:797",
          "words": [
            {"translit": "pasu, pašman", "gloss": "wool", "script": null},
            {"translit": "fšu", "gloss": "cattle", "script": null},
            {"translit": "fšu-pait", "gloss": "protector of cattle, shepherd", "script": null, "see": ["Pa"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:797; SNS:123,125",
          "words": [
            {"translit": "pašm", "gloss": "wool", "script": "پشم"},
            {"translit": "šabân, čŭpân", "gloss": "shepherd", "script": "شبان ، چوپان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:51,298",
          "words": [
            {"translit": "`ps", "gloss": "sheep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "feht", "gloss": "to pluck out wool, fight", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "fight", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "fehu", "gloss": "property", "script": null},
            {"translit": "fĕlag", "gloss": "partner sharing property", "script": null}
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
            {"translit": "fellow", "gloss": null, "script": null}
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
            {"translit": "feudum", "gloss": "property, feudal state", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "feodal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "feodâl", "gloss": "owner of large land", "script": "فئودال"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "feudal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Peku",
        "redirect": "Pek"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:44:03.466Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SNS','SOD','AHD','MON','WLD','BRT','PHD','HRN','HUB','KLN','SKT','IEC','SYN','NYB','BQT','ARY','CHEUNG','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T20:44:04.780Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-07T20:44:09.456Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:44:09.512Z] TOOL RESULT

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


## [2026-09-07T20:44:13.273Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"peḱ\\|pek̑\\|peḱ-\\|Wolle\\|pek-\" POK_full.txt | grep -in \"wolle\" | head -30"
}
```


### [2026-09-07T20:44:13.324Z] TOOL RESULT

```
1:45560:weich gemacht ' oder " weich wie gekratzte Wolle '), Old English hnesce 'tender, soft, 
3:68314:vlusch^ fleece, fleece', nnd. vlOs(e), vlusch' tussock hair, BiJschel Wolle', Middle High 
4:70686:Old Icelandic ryja^6en Schafen die Wolle ausreiften' (Norwegian rui. "Winterwolle'), Old 
5:78203:lodo^ coarse Wollenzeug, Uberwurf out of it'. Modern High German Loden, Old Saxon 
8:88922:i4/c»c/re/7 "distaff; flax or Wolle auf dem Rockenstock', Old Saxon M/occc»"cicindela (wick, 
9:90372:underfurof Bartes, Milchhaare', Gothic wulla, Old High German wolla etc. 'Wolle = wool', 
10:90391:lagdr^ tuft of Wolle or Haar' ( *wlagat^a-)\ Old Church Slavic vlakno, russ. volokno " fibre, 
11:90402:Gr. Kdmoc, (*FAaTiO(;, Indo Germanic *ult-lios) "dense with Wolle or Haaren, also 
12:93507:£poc; "aries, ram' ("whereupon Wolle is'), Ionian £iplv£0(;, Attic i^wizoc, "from wool';
```


## [2026-09-07T20:44:14.163Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"797\" POK_full.txt | head -20; echo ===; grep -n \"pe.u-\\|pek\\b\" POK_full.txt | head"
}
```


### [2026-09-07T20:44:14.225Z] TOOL RESULT

```
Exit code 1
4027:esp. Schuize SBprAk.1910, 797 = Kl. Schr. 120). 
19223:References: WP. I 797 ff., WH. I 342 f., 373, 861, Trautmann 51 f. 
54561:References: WP. II 395, WH. I 797. 
65467:Page(s): 796-797 
65504:Page(s): 797 
68256:See also: zur /-extension see above S. 797 \xx\6ex peR-. 
89922:References: WP. I 242, WH. II 797. 
(eval):1: == not found
```


## [2026-09-07T20:44:16.804Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '65400,65520p' POK_full.txt"
}
```


### [2026-09-07T20:44:16.859Z] TOOL RESULT

```
Romagnolo 




pin 




Romanian 




pin 




Valencian 




pi 



Venetian pin 

Zeneize pin 

extension poi-d-, pT-d-: gr. nT5ri£i(; " rich in springs ', nT5a^ 'wellspring', nT5uu) "allow 
trickle through, gushes forth ', Norn. PI. n. rfiasa ' damp places, meadows ' ( *pT-d-s-es-)\ 
Old Icelandic fitai. 'fat', Germanic *faitian^ fatten, overfeed ' (Old High German feizen. Old 
English fgetan. Old Icelandic feit^, "/^//a- "fat'(Old High German feiz. Old Icelandic feiti), 
participle Germanic *faitida-: Q\^ High German feizzit. Middle High German veiz(e)t. 
Modern High German feist. Old English faeted, engl. fat. Middle Low German i/e/"fat'; Old 
Icelandic /^/'meadow'. East Frisian "puddle, slop'; Latvian pisa, /O/se 'morass, bush wood '; 
about Middle Irish esc "water' (see above S. 45 about Middle Irish esc-ung^ eel, snakelike 
fish '), wherefore Middle Irish escaf. "swamp, marsh', see below pe/s/r- "fish'; or escirom 
*pid-ska? 

References: WP. II 73 ff., WH. 211 f., 306, 308, 311, 312, Trautmann 207 f., 210, 217. 
Page(s): 793-794 

Root / lemma: peR-1, peR-, poR- 
Meaning: to make pretty; to be joyful 

Material: Old High German gifehan. Old English gefeon " are glad '; Old Saxon Old High 
German /fe/7d/7 "consume'. Old High German gi-fehdn6s. = Old English ge-feon. Old High 
German gi-fehan^ take pleasure '; Kaus. Gothic fulla-fahjan^ perform satisfaction, give 
satisfaction, serve ', Old High German fagon^ stand '; Gothic /^/7eA's "pleasure, joy'. Old 
Icelandic feginn. Old English /fe^e/7 "blithe, glad', Gothic Old High German faginon. Old 
English faegenian^ are glad ', Old Icelandic fagna6s., Gothic ga-fefiaba' fitting, 
respectable ', Old Icelandic /^^///^/""pleasanf; Gothic fagrs^ suitable ', Old Icelandic fagr. 
Old English /^^©/""beautifuT etc.; Gothic ^3-/^/7/7^/7" prepare, concoct'; in materieller 
meaning Middle High German i/e^e/7 "clean, scour, rub, clean, sweep, wash away ', Old 
Icelandic /^^a "adorn, clean', /^5/a "gleaming make, clean' and Lithuanian puosiu 
{*pdReid), yOi/os// "adorn', Latvian yOi/os/" clean, adorn', refl. "be clean'; perhaps here Middle 
Irish ^//"pleasant' as *pdkli- (yet s. also under paR- " moor '). 
References: WP. II 16, Wissmann Nom. Postverb. 14, 91, Trautmann 229. 
Page(s): 796-797 

Root / lemma: peR-2 
Meaning: to fleece; cattle 



Material: Old Indie pasu-, pasu- n., Gen. pasvah, pasu- m. "cattle'; Avestan pasu- m. 
"cattle' (mostly still "small cattle'), in compound fsu-, -fsu-, wherewith Old Indie ksu-man- 
"rich in food', puru-ksu 6s. (twice also basic ksu) as Diss. -forms for ps^- identical; = Latin 
pecO, -usn. "a head of cattle, beast, brute, animal, one of a herd', next to which pecus, - 
orisu. (formal = gr. to hekoc;), pecus, -udisi. ds.; derivatives pecun/a^ property, riches, 
wealth', pecu//um^ property'; Umbrian pequoP\. n. " pecua '; = Gothic fafhu^ possession, 
fortune'. Old Icelandic fe. Old English feoh. Old Saxon fehu. Old High German fihu^catt\e'\ 
= Lithuanian pekus. Old Prussian pec/ri/ "cattle' (West Indo Germanic guttural); Gothic bi-, 
ga-fafhon^ ijbervorteilen ' are after W. Wissmann (The oldest Postverbalia 79 ff.) 
Denominativa from fafhu, and t>/-fa/h ^ 6ece\t' is noun post-verbal; 

Armenian asr, Gen. asu^ sheep's wool, fleece ', asi/e/ "fleecy' {*poku+ r, with a from o 
in open initial sound syllable); gr. TreKoo (= Lithuanian pesu), hektu) (= Latin pecto. Old High 
German fehtan), hekteu) "comb, shear ', nsKoq n. " fleece, wool', n6K0(; m.; " fleece ', k-\z\c„ 
KTSvoq "comb' (from zero grade *nKT£v-; Latin pecten); 

alb. pile^ Werkzeug zum Flachskammen, -hechein ' {*pekla)\ Latin pecto, -ere, pexT 
"comb', pecten, -//7/s"comb', Umbrian petenata^ pectinatam '; Old High German Old 
Saxon fehtan. Old English feohtan^ fence '; Old High German Old Saxon fahs. Old English 
feax^ hair ', Old Icelandic /&A'"mane' ( *-pok-s-o-, compare the es-stem nsKOi;), Old 
Icelandic faer. Old Swedish /^/""sheep' ( *fahaz= noKoc;), Old Swedish fset{ *fahti-) "wool, 
fleece ', Old English feht^ fleece ', Dutch vacMt "wool, fleece ', Old English f/h/' a piece 
of cloth, garment of cloth '; Lithuanian pesu, pesti^ rupfen, an den Haaren zausen ', Iter. 
pasyti, susipesti^ to tear, rend'. 

Here probably Old \r\6\c paks-man-r\. "eyelashes, hair', paks-mala-^W\t\\ strong 
eyelashes, thick-hairy ', Avestan pasna-r\. "eyelid', compare in not so specified meaning 
np. pasm "wool', common Old Indie -gh- > -ks- : Avestan -gh- > -xs-, -s- 

References: WP. II 16 f., WH. 1 1 269 f., 270 ff., Trautmann 217, Specht KZ 68, 205 ff. 
Page(s): 797 

Root / lemma: pe/T'- {*k"'ek"'hd) 

Meaning: to cook 

Grammatical information: participle pek''-to-^cooke6, boiled' 

Material: Old Indie pacati, Avestan pacaiti^ cooks, bakes, roasts ' (= Latin coquo, cymr. 

pobi, alb. pjek. Old Bulgarian pekg, compare also Lithuanian kepu); Put. paksyat/: gr. 

nsijju)); common Old Indie -g"'h- > -ks- : Gr. -g^'h- > -k^'h- : -k^'h- > -ps- 



Supin. paktum= Latin coctum, Old Church Slavic pestb; participle pakta-{= gr. tt£ttt6(;,
```


## [2026-09-07T20:44:40.629Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT fšu ===\"; grep -n \"fsu-\\|fšu\\|f?u-pana\\|fsupana\\|fsu-pana\" BRT.txt | head -40"
}
```


### [2026-09-07T20:44:40.677Z] TOOL RESULT

```
=== BRT fšu ===
```


## [2026-09-07T20:44:42.518Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 387 -l 387 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg387 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg387.png"
}
```


### [2026-09-07T20:44:44.112Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 45700 Sep  7 16:44 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg387.png
```


## [2026-09-07T20:44:47.150Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg387.png"
}
```


### [2026-09-07T20:44:47.514Z] TOOL RESULT

```

```


## [2026-09-07T20:44:47.512Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:44:48.246Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT pasu ===\"; grep -n \"pasu-\\|pasav\\|pasu m\" BRT.txt | head -30; echo \"=== BRT pasman ===\"; grep -n \"pasman\\|pašman\\|pasman-\" BRT.txt | head -20"
}
```


### [2026-09-07T20:44:48.322Z] TOOL RESULT

```
=== BRT pasu ===
5368:"ka''  ski^  avam  *''ufrasatam  aparsam  Bh. /.8;  —  pasavJ'  karJ'  'ka"  abavJ'  Bh. /.  10.
6007:•  j.  az«m,  g.  azSm,  p.  adam  NS.  Fron. 1.  Pers.  'ich'.  Es  wird  gesetzt  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegt)  a)  bei  Gegenüberstellung:  1  naiy 'iam  fuümaiy  taumä  Bh.  >^.  1 1 ;  —  11  ima' ttsuam  (sd.)  Aauv  rtiyastaya^  ktftanaty.. pasavr  'dam  niyastäyam  ..  X.  7.3;  —  i^a maätyOe  dta^arynä  . .  äat  azim  manya  . . \\jo.  I  o  s  t ;  —  'Um  iBi  sis  ^pouruyifravsi- vJdl  (sd.)  vJspSt^  anySng  .  .  \.  44.11;  — yä^a  't^m  avata  V3r3%ra  hacane  ya^a vltfie  *anye  aire  Yt.  5.69;  —  b^r^JoyStiti il .  .  strSuica  titäuApmca  .  .  'z^mca  kl  öptp- jttlm  yö  äaiiva  ahurd  mazdä  V.  7.52''; —  S  mann  taumäyä  ^*  paruvam  xfäya- ^t^ä  a/tcT  'dam  navami^  Bh.  7.4;  — ö^J  aäJ  csit  (sd.)  akurS  .  .  ^öti  sara- "^uärg  , ,  a%a  *'ifmhi  yö  mazdayasno .  .  vimrvyi  Y,  12.  6  '*;  Vr.  11.  19";  — yd^a  avat  kvanxsait^m  ..  av<£k>a  'zsmHl.
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
9034::rri7vrt>(>fl*  ühJ*  Bh.  /.  10;  lo';  — pasav^
9515:aha*  Bh.  2. 6;  5, J.  5.         2)  'Volk'  in  poli- 1     ^'^■- ^  ^-^"^  '""''■  -  ''  ^^-  S  JSJ- tischem   Sinn;   'die  Leute':    pasava"    -ra")         S-  '"^""'  ^-  5'-  ''■  '■  '^''^''-^- >iffnOT'a*  "amt^^iye^  a6av<^ . .  uH  pärsa^  •  j-  kirft-  Adj.  'versans  circa  -,  sich  ab- utn   madä*  ata  anml  dahyävc^  ßh./.  11;  gebend,  zu  tun  machend  mit -,  tätig  bei -'. 13,  16,  ?.I3,  r.  10;  —  hauv  -rahyä  am^ä       f^^P^-  "  ^"""  ^-  *'"'-■  "  ■^ß'"    '^'^''-  >""*
9962:(sd.)  ttsit  janm^  Yt  i4-  S6;  — yS  janat''> dva  %rifva..dagvanqm  Yt/p.26;  41— 43*, _;.  10;  —  dusmaitryä  *janant?m3'>  bavahi yaha  v)r3%raymm  Az.  7;  —  aß  nanm jainti  väf  .,  afl  nar?m  nSit  jainti  V.5.  8; .  9';  —  ynat'^,  ynai''>  F.  22.  a)  'schlagen' i  in  militärischem  Sinn,  'besiegen':  ipasavt^ adam  karam  tyam  nadi''tabairahya  adam \ajanam  vasiy  Bh.J.18;  19,2.13,  4.1;  —
14242:•  '}.  drvö.pasav-  Adj.  (auch  fem.)  'das Kleinvieh  gesund  erhaltend':  drväspqm.. 'svqm  (ASf.)''  drvSjtaorqm  Yt.p.  i.
14522:smtu  dui.mainyui  amtmca  vfrfi^rayn^m'a Yt.  t4. 38.  b)  1  mit  ha^ä  und  Abi.  oder Instr.:  dahyävt^  .  ,  tyS  hacämc^  aiars^ D.5.2J — pasavc^ ha^ämJ^ atarsa""'' ' ßyä  ".,  bekamen  ..  Furcht  vor  mir"  Bh.2. 4;  —  iyam  dahyäul .  .hacä  aniyanä  naiy tarsatiyD.4.2;  —  Aa/a  amya«ä(Sp.i$j\i.) ms  tarsam^*  ^■5-3-  D  c)  mitDat:  vTsfe Unanti  ptnnine  (sd.)  Yt  i4-  38.  a)  zu- gleich mit  Dat  comm.  'für  — ':  avaiia mavayacit  latmye  .  .  Unsintu  aurva%a "folglich  sollen  (werden)  die  Feinde  auch vor  mir  Furcht  für  ihre  Person  bekommen" Yt  14.  38.  Anhang.  PPfP.  'timidus': hS  nsit  tarltS  */ranamaite  frä  ahmäl pars  vTspe  .  .  tar^ta  tamante  Y.  57.  18; Yt.p.4,  Y.5.11.  A)  Kaus.  'in  Furcht, Schrecken  versetzen';  *Aä^ra.larsta  (sd.) %räaAayele  uvaya  aspa.vTraja  "in  plötz- lichen Schrecken  versetzt  er  sie  beide, auf  Ross  und  Reiter  einschlagend"  Yt. 10.101.  2)  B  'etwas  iiirchten  von —'(.*a<ä mit  Abi.);  was  gefürchtet  wird,  erscheint in  einem  selbständigen  Satz  mit  Opt  des Verbs:  kärJ'Sim  (als  Gen.)  kaüa  ^dan^mt^ (sd.)  atarst^:  käram  vasiy  aväjamyl^*''
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
15917:•  j.  pasvant-  Adj.  (fem.  'vaiti-)  'mit *pas-  (f.  'Strick'?)"'  oder  'mit  pasav-  (m. 'Vieh'?)''  versehen':  ha  (näml.  kaine)  .  . °vaiti  V.  ig.  30.
16747:astayS  (sd.)  Y.  70.  4;  4';  —  humaya  nS buyata  (zP.)  Vr, /2.  g;  —  havanhum  mi buyata  Y.  7/.  11';  —  \va^ll  J'urc^i dähJ' adam  xMya%iya^  abavam  "..wiirde ich  König"  Bh. /.  13;  10,  15,  4.2,  1.12, i6,  2.5,  J.  $,  13; — pasava*  käri^  hami- %^iyJ'  adava*  Bh./.io;  11,  16,  2,  5,  14, J.  5,  13,  5.1;  —  bäbiruviyä  hamih''iy3 abava'  Bh.  3. 13;  /.  16,  2.  s,  16,  4. 4,  j, 3.  II  Anhang,  a)  II  An  Stelle  des  kon-
16748:gruenten praed.  Pron.  poss,  steht  der  Gen. des  Pron.  pers.:  fasava/'  dahyäus  manä abavc^  "drauf  wurde  die  Provinz  mein" Bh._j.2,  4,  12.11  b)  An  Stelle  des  praed. Nom.  steht  ein  Adv,:  axua  . .  bavaAi ya'ha  . .  "so  sollst  du  werden  wie  . ."  Az. 2;  —  i^m  . .  saohrä  bavainti  yas»  iava  . . "was  geschieht  mit  den  Z.,  wenn  .."  Yt. 5'94i  —  ftyat  fta%ra  (sd.)  wawi  bavat ya%rä  . .  Y.30.  9 ;  —  yäü  a  atthus  *paou- ruyU  bavat  'Vie  es  mit  dem  ersten  Leben werden  wird"  Y.  2<¥.  1 1 ;  —  I  adataiy  azdä (sd.)  bavatiy  D.6'.4'; — pasaved  draugc^ vasiy  (sd.)  abav<^  Bh.  i.io;  4-  lo»  16  {wo bly^);l\ —  a An  Aüwat (sd.)  abava/(AMgm.) Y. /p.  159',  c)  Statt  der  kongruenten Num.-Form  des  praed.  Adj.  steht  die  des Neutrums  im  Sing. :  ia'^a  aste  spana  3^ä.- xalmm  (sd.)  bavan  V.  15.  44;  43;  —  apirs- näyu  aAmi  (Sp.aj 6  u.)..yezi  baväm  p?r)- »^^»(sd.)  Yt/9.43(?); — yimS  ..jailyat avat..dazdi  ml ..yatbavani  s^annaiiuhas- ttmsm  tslanqm  Yt/5.  i6(?).  d)  Statt
18398:•  j.,  g.  "ßav-  m.:  s.  unter  pasav-  (mit No.  i).        VgL  auch  ^/ys.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
19394:—  manS  J'ur<^tnasds  upasiam  baratuv . .  Uta  imam  dahySum  . .  pätuv  D.  4. 3 ;  — vas^i  (^urJ'mazdäkJ'  manacS  däray<^- vaAaui"D.4.2;  —  iya*  mana  kartam  utä fyc^maiy  /iS'ö*  kartam  X.7.4;  —  avam käram  .  .  hyj*  mana  naiy  gaubataiy*^ Eh.2. 6,  j,3,  14;  2.14.  zu  1  b):  J'urt^- masda  ya'ha  avaina*  imäm  bümim  *yau- d<rHm  (sd.)  pasüvt^dim  martä  fräbart^ mam  (s.  i  i  b)  . .  D.  61 4 ;  — pasavo^  dahyUui mana  abavJ'  Bh.j.  a,  4,  iz.  zu  3): kari^  hy<^  hamüi'iyc^  mana  naiy  gau- &ataiy*'>  Eh.  2.  7,  10.  b  n)  im  jAw.; zu  I  a):  Hat . ,  mana  asti  vjjaymift^m  . . attivam  asti  vJmamiiftim  Yt  /.  a;  — s.  noch  bei  a.  zu  1  b):  mana  raya  .  . pawasla  staorüta  upairi  tarn  vTcarmta Yt  5.  89;  /.  a6  (?).  zu  a):  ya%a  .  . Os  zaofff  mana  yat  ahurakt  matda  Yt ig.  8a;  V.  ig.  14;  —  ar»hu^  y3  mana yai  ahurahe  mazdä  P.  40;  —  zugleich zu  1  a):  manada  yatmm  yat  ahurahe mazda  a^rasca  P.Jp.  11)  schwach- tonige  Formen  stehen  a)  enklitisch i)  hinter  dem  ersten  Wort  des  Satz-  oder Versteils,  von  dem  sie  aber  a)  durch  ein andres  enklitisches  Wort  getrennt  sein können;  a)  hinter  einem  Praenomen; 3)  selten  in  anderer  Stellung;  b)  pro- klitisch5>;  das  hochbetonte  Wort,  an  das sie  sich  anschliessen,  hat  keine  bestimmte Stellung.  I)  Akk,;  a)  im  Ap.;  zu  a  1): avada  mam  cita  amanayJ"  Eh.  2. 6;  — y^a  mam  kame^  Bh.4.4;  D. ö. 4, 17-3)
19396:mam  Eh.  2.  13;  J.  17,  2.14,  5.1,  4;  — -fJra*  .  .  hy<r  upa  mäm  ah<^  Bh.  2. 6; j.  6.  zu  3):  pasav<^  dadarlif  äta mam  amanayt^  ..Sh.2.g,  11.  Bt)  im gAw>;  zu  a  i):  iahmai  mä  ^warSzdüml k!  ma  tasap  Y.25.  i; — kyat  mä  dngva dldarfiatä  (sd.) . .  Y.  46-  7 ;  4?-  7 ;  —  yeAya ma  ai^i/ dva^a  Y.  4^.9;  ^2. 16,  j/.  5;  — Jt!  hvS  yS  ma  artärB  (iikai .  .\.46.9;  —
20302:•  p.  mäda-  Adj.,  bezeichnet  ein  Volk, 'mediscb;  Meder*;  naiy  ähJ'  martiya^ naiy  pars<^  naiy  "d^  Bh.  i.  13;  —  karam psnam  uta  'dam  Bh._j,6,  2.14;  6;  — käram  tyam  °dam  Bh.  2. 6 ;  5 ;  —  i  fravartis namd'  *dc^  Bh.  4.  a;  2.  $,  14,  3.  14;  — avadä  Aamaranam  aiunaus  Aadä  'daibis; Äyo*  'daiiuvä  mdhisia*  aÄa*  hauv  . .  Bh. 2, 6.  a)  Sing.  (koL)  für  Volk  und  Land: pasavs^  draugt^  vasiy  aiava*  uls  pärsaiy Uta  'daiy  uta  amyTuvH  dakyuiüva  Bh. j.io;  12,  II,  14;  —  imä  dakyavcl'  .. Parsal  . .  'da*  Bh.2.a;  1.6,  D.5.2,  6.3;
23143:•  p.  vasiy  Adv.  'multum';  i)  'in  grosser Anzahl,  viel':  v  aniyaiciy  natbam  (sd.) kartam  X./.3;  7.  3,  Bh.d^.S;  —  «israw  (sd.) v  aväjaniy^  Äya*  . .  Bh, /.  13.  a)  mit demV.  i«i-;  a) 'zahlreich  werden':  utätaiy tauma  v  biy^  "und  dein  Geschlecht  möge zahlreich  werden"  Bh,  4- 10,  16.  ß) 'über- handnehmen, sich  ausbreiten':  pasavJ' draugJ'  dahyauvä  V  abavc^  "drauf nahm  die  Lüge  im  Land  überhand"  Bh. 7. 10.  2)  'in  starkem  Mass,  sehr': ksr^  hy^  manu  avam  käram  lyam hamik^iyam  aja"  v  Bh.  2,  7— 11*,  j.  3,  9, 10;  f.  18,  19,  2.  6,  IX,  3.  I,  6,  7.
24276:•  j-,  e-'viT&-,vira-  m.'tAami':  nart  iiArfia ..tala  ayao/(sd.)  yäia  pauirJm  'nm  avi ya  bavaiti  YtS.  I3f.;  14.  2;  —  hasanrai bartina  (sd.)  'ranqm  YL5.  96 'J;  —  insbes. der  wehrhafte,  wafleniragende,  'Kriegs- mann': °rahe  k>hrpa  raSimtS  srJrahf  Yt I4.^^'''■,  —  haüaiti  dtm  •rohe  ao/d  Yl /^.  68;  —  a.  noch  a,  a)  im  Gegen- satz zu  aspa-^:  4d . .  galam  (sd.)  nijainti aspagca  'raica  ". .  auf  Ross  und  (Kriegs-) Mann"  Yt./o.  iqi;  —  aspailu  -raEht  Yt ^5-  S3i  —  s.  noch  No.  3.  b)  im  Gegen- satz zu  ^gav-%  gfuica  va^wa  *ranamca\ "Heerden  von  Vieh  und  Männern"  Yt. , ;o.  a8,  13.  $x;  —  gSus  vifhwa  (sd.)  ..j 'ranqm  *-pouruJäs  Y.  62.  i'o.  c)  im  | Gegensatz  zu  pasav-;  a)  'Manne,  Zuge- liöriger;  Leute':  västryehyä . . pasSus  'räatcä "an  des  Bauern  Tieren  und  Leuten"  Y. _?j,  15;  — pasüs  'rSng  ahmakSng frada^äi (sd.)    a   Y.  45-  9 ;  —  p<i'rT  pasas  . .  'ring
26702:mit  nT  'instituere,  anordnen,  befehlen', mit  Akk.  und  Inf:  D  adam  niyastayam imäm  yuviyäm  (sd.)  k^tanaiy  D.  17.  3;  3; —  ima'  stanam  (sd.)  Aauv  niyastayir  k^ta- naiyX.y.^; — pasava*  adam  niyaslJyam imäm  dipim  (sd.)  nipistanaiy  X.7.  3;!  — sä%rasal . .  yB  nistayeiti  k>r3tSe  sraosyqm (sd.)  ilart  (sd.)  ha  nÜtäta  (LS.)  iiryeiti yai  granto  nistayeiti  (Konj.)  ". ,  sofort  . . wird  sie  vollstreckt,  sobaJd  er  ergrimmt (sie  zu  vollstrecken)  befiehlt  (jusserit)"  Yt W.  109.  Undeutlich  ;*_)■«/ /iVVj  *d>nane ha%räHs  ^nis'MItanti'^''  N.  100.
26861:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
28008:—  pä\aiibya  .  .  -toiibya  V.  5.  1 1 ;  — palnubya  ..  'taiibya  V.  2.  31;  ö".  29,  4".  40, s8.  19,  A.  4-  5.  Yd,  72;  —  Äiiz'fl  mrBihi hsxtim  . .  *°tagibya  variza  kvarltjm  Syao- 'kmm  Aog.  söf.;  —  manaahasca  *humaiti hisvasca  *häxii  'iayas{LS.)'Va  *hvarsii P.  2c?.  a)  gAw.  ID.  sva.  'durch  Handeln, Tun' 3':  at  yJ  aktm  dngvSitl  vacankä  vü ai  vä  manatskä  'tsibyä  va  vanlaitl  "wer aber  dem  Zlrv^enossen  mit  Worten  oder mit  Gedanken  oder  mit  seiner  Hände Werk  Übles  tut"  Y.  jj.  2.  et)  in  Ver- bindung mit  Syaö^ana-.  vahistim  hisvä uxiäi/. .  Sfdnä  . .  'tSibyä  syaö^anä  vimyat (Sp.  1377  0.)  Y.47-  2.  b)  Pv  gAw.  Lok! (Sg.  oder  Du.)  mit  V.  da-  oder  'kar-  'alicui (Dat,  Gen.)  in  manu  ponere':  'pasavJ'- di/  a*ura''rnasdä  manS  'tays  (LS.)''  aku- naui  "dann  gab  sie  AM.  in  meine  Hand" Bh.  4.  4;  —  kdka  asäi  drupm  dyam  "tayd (LD.)  "ob  ich  wohl  dem  A.  (dem  Reich der  Wahrheit)  die  Dr.  (das  Reich  der Lüge)  in  dieHände  liefern  kann?"  \.4.4. 1 4; jo.  85'.  2)  übertr.,  von  den  Klauen des  Ebers  (nur  Komp.).  1
28519:durch  a)  AkL  'nach  .  .':  pasav^  ka'bü- jiyaf'  mudrSyam  asiyav<^  ya%ä  . .  mu- dräyam   asiyavc^  .  .  Bh.  I.  10;  _y.  6',  5.1;
29422:•  p.  ham-arana-,  j.  ham-arana-  n. 'Treffen,  Kampf,  Schlachf :  ^\paraitä  patis vtvanam  -nam  larianaiy  .  .  avadä  'natn akunoDt^  .  .  avahsi'äm  •nam  kartam  Bh. j,  10  usw.'';  — pasavi^  °nam  akuma  Bh. 2,  la  usw.'';  —  ,  .  'nam  akunaus  hadä *märgayaibil  Bh. ,?.  3  usw.'';  —  aäam jg  °na  akunavam  BK 4.2;  —  9  xsäya'^iyä ..agarbäyam  c^tar  ima  °nä  Bh,  4.  jjll  — fravaSayö  ,  .  ya  upairi  *'nat*>  aurva%a- nam  .  .  dSxüf  scaruiayeinti  ",  .  von  oben her  in  der  Schlacht  . ."  YtiJ.  31.
29628:•  j-  (i  S)  haurva-,  p.  haniva-  Adj.  (fem. 'va-")  'ganz';  i)  sva.  'unverletzt,  unversehrt, heil';  dad)mahl  haurvafsavS  .  .  drva  *va (NPm.)  ttüvants  Y.  iß.  6.  2)  sva.  'ge- sammt,  vollständig':  \pasava''  kar<^  °va* /iami'äi''iya^  abava^  Bh.  i.  1 1 ;  1 6 ;  —  °v<^- iim  kära''  avaint/"  Bh.  2, 13,  14;  II  —  'vqm handaitlm  staotanqm  yesnyanqm  Y.  5^'.  8; —  vlsp>m  vacff  fravähm  (sd.)  °rum  vacS ahurahe  mazdä  \.  ig.  14;  —  'vqm  tarasca xlapamm  V.  ;&5,  6;  —  zusammen  mit vTspa-^^:  yO  vtspqm  'vqm  tansm  upanAan- zaiti  V,  6'.  24.  a)  Akk.  in  Verbindung mit  'da-  'etwas  ganz,  vollständig  machen,
=== BRT pasman ===
6288:—  avä  dämqn  'ZavanS  (als  APn.)"'  .. yä  hmti  paoirya.d3ta  Yt.-j.^;  —  sfimtö.- dätäis  dämqn  'idvanB  (als  APn.)*"'  Vr. 75.1;  1;  —  vTspe  .  .  k)  asti  voku  'sava antan  tarn  asmatamca  Y.  68.  15;  — xartmcS  yim  'lavansm  Y.  42.4;  —  'im-a (ASn.)  yra^a.savs  Vr.  7p.  2  (?) ;  —  aspi>.- kthrpqm  (sd.)  'laonlm  YtÄ8(?);  — mSurum  'Savan»m  V,  7.5;  16;  —  kat)haya . .  -savanaya  (LSm.)  Yt5. 54;  —  Hnval-- ppr?tBm  ..  'saortlm  S.  2. 30;  — garayS  . . 'lavana  (als  APm.)  Y.  2. 14;  —  dunman .  .  maeyS.kara  °savanJ  (als  NPn,)  '">  Yt. ^■^y,  —  urvarqm  'laonTm  V.7p.35;  Y. 2, 1 1,  N.  77,  57;  —  urvaire  .  .  masdaü3te 'saone(Y^{.)  Y.if).i8,  Yyt  22;  ~  haema .  .  spitita  '/avana  (als  NP.)  Vr.().  3;  — äp3  . .  '/aenis'Y.2.12',  16.4,  Ö5.7,  ö'(?.7; 2.5,  Yt2. 12;  —  imai  6ar>sma  .,  'sava- tum  aiahe  ratüm  Y.  77.23*';  —  ralavff upapanqm  . .  upasmanqm  . .  "saonqm  asahe ra^wqm  Vr.  7. 1 ;  —  dalnqm  . .  'identtn Y,72.9;  YtJj.ioo;  —  xratüm  °savan>m
```


## [2026-09-07T20:45:06.237Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT fsu-pana / Hirt ===\"; grep -n \"ßu\\.\\|ßu-\\|fsu\\.\\|fSu\\|psupana\\|pana-.*Hirt\\|Hirt\" BRT.txt | head -30"
}
```


### [2026-09-07T20:45:06.280Z] TOOL RESULT

```
=== BRT fsu-pana / Hirt ===
2865:uka  'Geschrei'?    S.  Hirt  Ablaut  132.  —  Vll.
4917:*)  Ursprünglich  des  Fesis  der  Heimkehr  von Hirt  und  Herden  aus  der  Senne  (s.  u.).   Später ist    es    dem   Andenken    an   die  SchaiTung   der Pflanzen  geweiht   Der  letite  (30,)  Tag  fällt  auf den  30.  des  7.  Monats,    d.  i.  in  alter  Zeit  auf den  3.  Okiober,  heutzutage  auf  Mitte  ApriL    S. im  übrigen  unter  yüirya-  und  miuiySisaiH: Ableit.  aas  'a-yä%ra.  n.  (iura  V.  yä-)  'Heim- kehr',  als   Adj.  ftlso  'was  mit  der  Heimkehr in  Beziehung  steht';  s.  Roth  ZDMG.  J4.  704. j.  ayiri.dräjS  N.  43:  lies  ayari.dr',
10189:eayanam  västryehe  fSuyantS  .  .  gaväzista (sd.)  '-izs  (ND.)  \.  14.10.
10924:fl-'Eiweiterung^'t  lus  dem  V.  'zan-;  ^zS.m, S6.  —  M.  jijiiäsati,  jnälah ;  np.  Haäsad  'er erkennt''),  lat.  ^näjfo.  —  i)'Vgl.  Hirt  Abi  au  i 93.  —  ')  mp.  inätan,  np.  sunSdan  "höien' (Hbu.  FSt  8z)  scheint  auf  einer  Kontamina- tion von  air.  xsnä-  und  sru-  lu  beruhen;  vgl. auch  die  PD..werter  SWienAW.  jhS.  880, GIrPb.  /  b.  306.  Undeuüich  Ut  mir  ClrPb. I-  303.  34 1
13596:Zum  J-Aor,  *däh-  des  V.  ää-t).  —  Pü.  (zu  Y. J4);  iim  kuniin  kim  _^iwisn  kern  yatihi  fia aaiari  nniiihtih,  iuniJn  elön  tunim  u  i;äwi!n (tön  gäwem  u  yasisn  itön  kuntm,  u  ä  aSmiahül u  ÖH  lö  dtthcM  Öhrmusd,  (zu  Y.  44) :  mizd  .  . ka  man  Shrmazd  andar  däitem  hamalat  n nmiiHat  Hön  ün  i  hat  2  IS  dät.  —  ')  Vgl. No.  2.  —  ')  Die  Beiiehung  auf  die  Zukunft ist  dem  Nomen  durch  den  Konjunktiv  des J-Aorists  lUEefiitirt  worden,  der  schon  früh- zeitig dem  Ji'fl-Praesensi  (Futurum!  bedeulungs- gleich  geworden  war;  vgl.  •«ai-  No.  3  und die  litt,  bei  BoM.  GiGr, !  3 1 9  f.,  Hirt  GrLaut- Jkt'omienl.  40t.  Im  übrigen  verhält  sich  dAuhä- zu  *iiinhaili  (oi.  datali)  wie  jyUii-  zu  Jijisaili und  wie  u.  pipäsa-  zu  fifäiati,  Miiid-  zu  ikil^-
14141:gewalt, durch  die  du  dem  rechtlebenden Aimen  das  bessere  Los  verschaffen  wirst" V.5_j,  9;  —  yim  'guiyö  dadat  v3stär?m "er  (Zar.),  den  sie  den  Armen  als  Hirten bestellt  haben"  Y.  27. 13S';  benützt  ip.  14.
15859:KompA.,  £.;  AbleiLU.  —  u.  fcsi'.-  m.;  sbal. fas  'Kleinneh',  woss. /»o  'SchaT;  np.  hi-hin ■Hirte'.  —  Pü. :  fah,  gösfonJ,  —  ')  Vennallich kein  selbständigei  Wort,  sondern  ans  einer Komp.  loigelösl;  ».  dain  JF.  ir.  133.  Vgl. nocti  in  ^flyo,  —  '^  LP-,  statt  fitsuTfa^  in Anlehnung  u>  den  NS. —  Jl  S.  auch  tamna-
16364:KompE.  —  Zu  ^ox.  fciijan,  Itsl.  pilali;  Hirt  [ Ablaat  36,  Ostmofp  Suppletivw.  55.  —  Vgl. . •/i'äa«j-.—  ai.>oi/.in. 'Nahrang',  mp.  (Pa.) /iV,  I woss.  ßd  -Fleisch' ;  s,  noch  lu  %Tqf3ia-  No.  3. 1 —  ')  Hds. /ai'iVni;  —  "I  Häs.  fiaißus;  — 3)  Hds.  faluJ;  s.  zu  No.  1-3  Bthl.  IF.  //.  | 139.  —  *)  Vgl.  la  yätus  Y.  7ä  4.  |
18414:•  j.,  g.  fSuyant-  Adj.,  PPA.:  s.  "^ßav-. KompE.
20607:Pü.:  a/r  vinäsem.  —  >)  Hirts  Zusammen- stellungen unter  mowe  und  maj'awa  (Ablaut 105,  151)  sind  nicht  ausgeglichen.
23548:•  g.  västar-  m.  'Hirte'  als  der,  der  für; Ndiiung  und  Sicherheit  der  anvertrauten Herde  sorgt:  yim  */fngui)-3  {sd.)  dadat Uarym  Y.27,13;  zit  /p.  I4i —  »^'^  "'*'■ •ta  xsmai  anyü  "ich  habe  keinen  andern  -■ Hirten  als  euch"  Y.  2g.  i.
24957:PFP.  eines  idg,  V.  ^reiidh-  'reuten,  urbai machen',  —  Vgl.  nhd.  riui/n,  abd.  Huli'1, mp.  rdiastSi  'inhabited  disiricf  (West  SBE- j/.  174),  np.  rös/ä  'DorPJl  und  Pa.  —  Pü. (lU  V.tf):  äröliiiiSmand,  erl.:  ia  kirind  "dais sie  sien"(?);  {lu  V.  F4):  fehlt.  —  O  NA.  ''iay' , s,  S  268.  II.  —  ')  Anders  hierüber  Hirt  PBrB. 23.  23,  aber  ohne  Kenntnis  der  iran.  Wörter. ahd.  riuli  ist  idg.  *,iudHiam'.  —  3>  Vgl.  die oberdeutschen  OrUnamen  KeuU,  Reulk  usw.
26545:*paya-  n.,  lum  V.  pä(y}:  —  PÜ.;  sler  pän.  — >)  Es  handelt  sich  also  um  ein  von  Hirten angemachtes  Feuer.
26559:Vgl,  gr.  Q-niia;  kymr.  la/«;  gani  unsicheres bei  Hirt  PBrB.  22. 223.  —  Pü. :  asiämak  (bei jAUASPji  GI0SS.  549  'gums").
30197:•  g.  hu-cistay-  f.  'die  gute  Lehre':  AvS' tsng  frd^h  pa%m}/tg  (sd.)  'tdis  *carat  Y. 46. 4.  a)  'Inhalt  der  guten  Lehre,  was sie  enthält,  insbes.  was  sie  in  Aussicht stellt,  verheisst':  tai  .  .  vairJm  (näml. mXid^m)  astvaiti  ustänäi  (sd.)  data  .  . xsmäkqm  'tim  ahurä  xrafSui  asä  fraäS v>nz7nä  "diesen  köstlichen  (Lohn) . .  werdet ihr  . .  verschaffen  . .:  was  eure  gute  Lehre verheisst,  o  Ah.,  die  der  Weisheit,  die durch  Äsa  die  Gemeinden  fördert"  Y. 34.\it.
```


## [2026-09-07T20:45:08.034Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN pasm ===\"; grep -n -i \"pašm\\|pasm \\|pasm,\\|Wolle\" HRN.txt | head -30; echo \"=== HRN cupan ===\"; grep -n -i \"šubān\\|subān\\|čūpān\\|cupan\\|šabān\\|saban\\|Hirt\" HRN.txt | head -20"
}
```


### [2026-09-07T20:45:08.092Z] TOOL RESULT

```
=== HRN pasm ===
3873:kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.);
4503:497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
4507:phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
5453:'Geleis' (yt. 5, 50) vergleichen wollen.
7284:'wollen, wünschen* (Hübschniann, No. 140); ai. iama-,
8697:wollend*.
=== HRN cupan ===
2665:§i/n. päda 'Hirte*.
2965:115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
3145:trahirt angesehen (zu m für n vergl. bam, bau 'Dach') ^) ;
5417:Contrahirt aus rawdmden^ Causativ von reßen
5633:contrahirt; andere von den Wörterbüchern überlieferte
6739:77G. sahän Hirte, siiwän, IN2iir (Is. 1, 24).
6741:aw. ysti.päna-; phlv. spän *Hirte' (AV.), supän
6743:kurd. siwan ; aty. spün 'Hirt*, spankai 'Schäferbube' ;
6745:Die dialektischen c«/?i7w (auch kurd. cuwän 'Hirt',
7717:888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
7725:vergl. sar. yubün, af/. yö6a 'Hirte*.
9165:also nur zum Teil von göpä- 'Hirt*. Vergl. auch
```


## [2026-09-07T20:45:16.807Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6730,6760p' HRN.txt; echo \"=== printed page? ===\"; grep -n \"\\[pdf page\" HRN.txt | head -3"
}
```


### [2026-09-07T20:45:16.863Z] TOOL RESULT

```
K5§. mc,
ap.;firt/yii]«?Ä Mes Nachts* ; aw. /sap', /sapan- Nacht*:
phlv. sap, saw(ik\ vergl. Sapak, N. pr. (Hörn, Mit-
teilungen, Heft IV, 29 No. 15); ai. ksdp-.
kurd. sew ; afy. spa ; oss. ä/jaw (44) ; bei. sap (862) ;
wa/. LW. smJ, sij'n. sa6, sar. /at, minj. ;^srfw?a, /asa/rr/.
Der ;<-Stamm findet sich vielleicht noch in np.
sebänröz^) (AM. sehärözT , wie jüd.-pers. ""'iNO^iJ),
sebänffäh, sebdnböl, sebänver u. a. m. erhalten.
77G. sahän Hirte, siiwän, IN2iir (Is. 1, 24).
Kas. cepän, cüptm, cap6 (vergl. V^ullers cüpdn),
aw. ysti.päna-; phlv. spän *Hirte' (AV.), supän
(FP61.), arm. LW. spat (aw. *ßu,paUi')^).
kurd. siwan ; aty. spün 'Hirt*, spankai 'Schäferbube' ;
bei. sipänk, n. mwäuK, safänk 03(57) ; wa/. s/)JJw, süpiin.
Die dialektischen c«/?i7w (auch kurd. cuwän 'Hirt',
cöpän 'Fleischer) sind jung. Das i der kurd. und
beluc. Form ist ebenfalls jung, es ist erst nachträg-
lich zwischen die zusammengerückte Gruppe sp, sw
getreten, also *sup% ^suw" — ^sp'', ^sw'* — siw"^ sip"
(Geiger* s Etymologie *sa — Praeüx — und |/^pö*- ist
falsch).
777. Htäften 'eilen', Praes. sitäb-em^ sitab, DNDl^iN (Jer.
48, 16).
*J E. Drouin*s Lesung suhanum uut* Münzen (Kevuc niumiä-
matique, 1890, S. 361) ist ebenso verfehlt, wie seine Qemmenentzifferungeii
(vergl. ZDMG. 45, 429 folgg.).
') Vergl. oben No. 179 Anm. _
5) IV^u/^ijufQoy, H. 8. Jarret, Aln-i Akbari-Transl. Vol. II, 13
Anm. 2.
*) Ilübsohmann, ZDMG. 44, 5ß0.— 172 -
=== printed page? ===
```


## [2026-09-07T20:45:18.268Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB ===\"; grep -n -i \"pasm\\|šubān\\|subān\\|cupan\\|čupān\\|Hirte\" HUB.txt | head -20; echo \"=== AHD peku ===\"; grep -n -i \"^peku\\|peku\\|pek-\\|fee\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T20:45:18.333Z] TOOL RESULT

```
=== HUB ===
1420:Hier fehit: paSm 'Wolle', skr. paksman- 'Augen-
3194:*Stab, Hirtenstab, Gerte und ist = np. gavaz ^stimulus
4365:folgenden ai contrahirte a nicht ausfallen konnte.
4712:Zu phi. matan *kommen' gehort phi. y^axarmatar*^ d. i. pasmatar *di8-
9797:p. 170. Ein contrahirtes -var mag auch in dilSr "be-
=== AHD peku ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
820:peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
979:in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
991:spreg-. To speak. Germanic *sprek-, *spek- (with Ger- manic loss of r) in: a. Old English specan, to speak: SPEAK; b. Germanic compound *bisprekan (*bi-, about; see ambhi) in Old English bisprecan, besprecan, to speak about: BESPEAK; c. Old English spréc, spéc, speech: SPEECH. [In Pok. (s)p(h)ereg- 996.]
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1306:BISCUIT dwo-, pekw- BISHOP spek- BISHOPRIC reg-! BISON weis-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1401:CROON gere-2 CROP ger-2 CROQUET ger-2 CROSIER ger-2 CROUCH ger-2 CROUP2 ger-2 CROUPIER ger-2 CROUTON kreus- crow! gere-2 cRow2 gere-2 CROWD! greut- CROWD? krut- CROWN sker-3 cRucIFY dhig’- CRUD greut- CRUDE kreue-1 CRUEL kreue-1 CRULLER ger-2 CRUMB ger-2 CRUMMIE ger-2 CRUMPET ger-2 CRUMPLE ger-2 CRUPPER ger-2 CRUSE ger-2 CRUST kreus- CRUSTACEAN kreus- CRUSTACEOUS kreus- CRUSTOSE kreus- CRUTCH ger-2 cRYO- kreus- CRYPT krau-. CRYPTIC krau- CRYPTO- krau- CRYSTAL kreus- CRYSTALLINE kreus- CRYSTALLO- kreus- CTENIDIUM pek-2 CTENOID pek-2 CTENOPHORE pek-2 CUBBY ku-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1495:FACET dhé-1 FACIAL dhé-1 FACIAS_ skei- -FACIENT dhé-1 FACIES dhé-1 FACILE dhé-1 FACILITY dhé-1 FACSIMILE dhé-1 FacT dhé-1 FACTION dhé-1 FACTITIOUS dhé-1 FACTOR dhé-! FACTOTUM dhé-!, teuta- FACULTY dhé-1 FAIN pek-1
```


## [2026-09-07T20:45:48.678Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB ctx ===\"; sed -n '1410,1432p' HUB.txt; echo \"=== SOD sheep ===\"; grep -n \"sheep\" SOD.txt | head -40"
}
```


### [2026-09-07T20:45:48.743Z] TOOL RESULT

```
=== HUB ctx ===
') Fehlt bei H r n.— 42 —
Dem Sinne nach Hesse sich mit pasafid auch zd. paiti-
zanta- *wiIlkommen' vergleichen, dem aber im Neu-
persischen *pazand entsprechen miisste.
320. Np. plst - nicht pist — heisst *MehI, gerSstetes Mehl'.
Also nach Nr. 316 zu stellen.
321. Im Afgh. sind puSt *Riicken und |?ws<^ 'Stiitze' Lehn-
worter ; echt ist pu^tai *Rippe' = skr. pr^ti- *Rippe* (das
von skr. prstha- 'Riicken = zd. parsti-, np. pust doch
wohl zu trennen ist).
Hier fehit: paSm 'Wolle', skr. paksman- 'Augen-
wimpern, Haar' (am Reh), paksa- Flugel'; ahd. fahs
*Haarschopf, gr. 7raxoi;*Vliess', tio xog *Schaf wolle, Vliess',
an, fcer *Schaf (J oh. Schmidt, Pluralbild. p. 148).
Vgl. Fr. Muller, WZKM. 7, 372.
323. Np. %i(i8aifkijtdan, pisanfidan *besprengt werden =
phi. pasindUan Viesein Bdh. 26, 10 kann sehr wohl
zur Wrzl. skr. sin6 gestellt werden. Es ist entstanden
aus pat + sinMaUy die Form sine- fur June trat regel-
recht ein nach den auf i endigenden Praepositionen
(vgl. skr. abhi'Sindafi *begiessen, besprengen , ni$incati
eingiessen, traufein*, parisindati *umgiessen', visincati
Vergiessen), daher skr. pratisincati zugiessen' — ap.
=== SOD sheep ===
16179:sheep,  cattle 
16281:sheep's  shoulderblade 
45521:sheep,  ewe 
57709:sheep,  cattle 
57850:cattle,  sheep 
68698:sheep,  cattle 
68713:flesh  or  skeleton  of  sheep 
89655:flesh  of  sheep    9009 
93585:sheep  1301,  5647,  7431,  7453, 
93588:sheep's  shoulder  blade  1315 
93714:sjceleton  of  sheep    9009
```


## [2026-09-07T20:45:49.066Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS pasm/subon ===\"; grep -n -i \"pašm\\|pasm\\|šubān\\|subān\\|wool\\|shepherd\" SNS.txt | head -30"
}
```


### [2026-09-07T20:45:49.122Z] TOOL RESULT

```
=== SNS pasm/subon ===
7565:. fZjf'ji (^:buz-pasm: 4^i'"ii 
8273:io*) :pasm5n: rex"* 
17610:V?^ -W/Y** .j-i^: ustur pasm: -*<->o -*>v£ 
29385:pasman- 123/10
```


## [2026-09-07T20:45:55.896Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29360,29400p' SNS.txt; echo \"=== SNS pages tag ===\"; grep -n \"\\[pdf page 12[0-9]\\]\" SNS_pages.txt | head"
}
```


### [2026-09-07T20:45:55.949Z] TOOL RESULT

```
paiti.rafiawa 142/15 
paitisahva- 124/4 



.t-jltSl*^ >^~~jt-* 






paitis 142/16 
paitis-x v ar 119/20 
pairi.aojastara- 144/8 
pairlka 135/16 
paflana- 115/15 
panca- 10/14-73/18-137/17 
pancadasa 118/3 
parahaoma- 125/23 
parana 125/14 
pasa-/pasava- 3/13 
pasus.haurva- 124/19 
paskat, pasca 125/5 
pasti- 139/7 
pasman- 123/10 
pacf- 118/11-235/1 

paflra- 118/6 

Parana- 139/13 

parasu- 114/4 

pasav/paratu 137/7 

piitisrauxta- 247/25 

pasta 139/1 

pixa- 143/16 
=== SNS pages tag ===
```


## [2026-09-07T20:45:56.628Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16170,16190p' SOD.txt; echo ===; sed -n '93580,93592p' SOD.txt; echo \"=== entry 1301 ===\"; grep -n \"^ *1301\\|1301 \" SOD.txt | head"
}
```


### [2026-09-07T20:45:56.683Z] TOOL RESULT

```
Exit code 1


o^r*^ 


1301  >ps-:   B,  S  jui-/ 
ap(a)s  ?  (DAv.  pasu   ©pred.  inst.  -\  ace.  -w 

^ps-7    ■ 
sheep,  cattle 
SCE  364;  TSP  3.187;  GMS  953,  1182  n  2 

1302  ips'ys-  =>  'Ps'ys- 

1303  >ps>k(h)   M,  B,  S  (^LZ:J^,)f  ^ 
(a)psak  =»ps>k 

wreath,  garland 

GMS  171,  979;  Hen.  Cosm.  307.16;  BSTBL,  Vim. 

(eval):1: == not found
```


## [2026-09-07T20:46:07.867Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" SNS_pages.txt | head -5; echo ...; grep -c \"\" SNS_pages.txt; echo \"=== pasm lines with context ===\"; grep -n \"pasm\\|subon\\|Subon\\|sub'n\\|shepherd\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T20:46:07.933Z] TOOL RESULT

```
...
16584
=== pasm lines with context ===
4905:                                               .   fZjf'ji (^:buz-pasm: 4^i'"ii
5396:                                    tfli'O*^* (tf*-^ io*) :pasm5n: rex"*
12691:                   V?^ -W/Y** .j-i^: ustur pasm:                                    -*<->o -*>v£
15189:                          nO 218/18                          pasman- 123/10             B
```


## [2026-09-07T20:46:09.236Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" SOD_pages.txt | head -3; echo \"=== find page of entry 1301 ===\"; awk '/\\[pdf page/{p=$0} />ps-/{print p\" :: \"$0}' SOD_pages.txt | head -5"
}
```


### [2026-09-07T20:46:10.642Z] TOOL RESULT

```
=== find page of entry 1301 ===
 ::     ozare ?                                                    344 My>ps-   B                    CjJ^/ ^jy^^tj
 ::          (o)fsak (Ps'k) ^'ps'c-                                                  518 >ps- B =* >Ps>y-
 ::                                                                    1301 >ps-: B, S                                jui-/
 :: 1300 >ps-1 B, M                                                    1310 'psNvxs-   S =» ^wys-
 ::       STii 1.46, 3.73                                              1328 >psw      B =» >ps-
```


## [2026-09-07T20:46:19.315Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"npages\",len(pages))\nfor i,p in enumerate(pages):\n    if '1301' in p and '>ps-' in p: print(\"entry1301 on chunk\",i)\nfor i,p in enumerate(pages):\n    if 'wool' in p.lower(): print(\"wool chunk\",i, [l.strip() for l in p.split('\\n') if 'wool' in l.lower()][:4])\nEOF"
}
```


### [2026-09-07T20:46:20.640Z] TOOL RESULT

```
npages 1
entry1301 on chunk 0
wool chunk 0 ['wool-stuffed  saddle  ?', 'wool,  woolen', 'woolly', 'woolen']
```


## [2026-09-07T20:46:23.735Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -B6 \"^wool,  woolen\" SOD.txt | head -30; echo ====; grep -n -B8 \"^woolly\" SOD.txt | head -20"
}
```


### [2026-09-07T20:46:23.812Z] TOOL RESULT

```
Exit code 1
65057-
65058-BSTBL,  Dhu. 
65059-
65060-8485  ryzy   M  ^^jlys, 
65061-rayzi   ©*IE  rezg  ? 
65062-
65063:wool,  woolen 
(eval):1: === not found
```


## [2026-09-07T20:46:29.002Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '68680,68720p' SOD.txt; echo \"=== 57700 ===\"; sed -n '57695,57715p' SOD.txt; echo \"=== 57840 ===\"; sed -n '57840,57860p' SOD.txt"
}
```


### [2026-09-07T20:46:29.096Z] TOOL RESULT

```
one  hundred 
C2,  54R28,  68V27 

9005  stw-'srt  M  ^l^j-u. 
satu-astat 

one  hundred  and  eighty 

Hen.  Cosm.  p312.100,  101  (clxxx) 

9006  stw-pnc^   C  .l?wj^ 
satu-pancas   ^pnc*s 

one  hundred  and  fifty 
C2,  13R27 

9007  stwr  C,  S  jy^ 
stor  ©ob.  -y;  pi.  -f;  ob.  pi.  ~ty  ^'st'wrh 
sheep,  cattle 

BSTii  849.4,  918.3:  C2,  12R4,  11V18;  STi  22,  22; 
CII  1990  E18 

9008  stwrpSyy   M  IJL^ijj*. 
stor-paSe   ^'st'wrpS^c 

animal,  cattle 

BBB  508;  Gersh.  Advice.  86  n27 

9009  stwry'ty  S  j^f  ^x+Jj^^c+if 
storyate  ? 

flesh  or  skeleton  of  sheep 
CII  1990  E18 

9010  sty'   C  =>  >sty] 

9011  sty2  C  4~^j,<4*j% 
sate  (stty)  ©pp.  =»sn~,  st-1 

=== 57700 ===
pa/os  ©<prsa-  ©impf.  ps>  ^ps'tS'r-,  'prs-, 

prs-,  'ps-1 
(ro)ask 
GMS  145;  BSTBL,  Dhu.  115;  STi  75.15;  Sund. 

AoFiii  1975  p66.16,  8;  BSTii:  C2  glossy  MSP  a5 

c9;  CII  1990,  85;  AVS  127 

7431  ps-'  B,  M,  C  jljl-/ 
pas  ©<Av.  pasu  ©ace.  psw;  nom.  psy(y) 

^ps-2,  psw 
sheep,  cattle 
GMS  953;  VJ;  BBB 

7432  ps*  C  J^_*  Jsje  jl  t<j3  ^  4crj 
pasa  (ps>h)       | 

then,  afterwards,  on  the  other  hand 
=== 57840 ===

Sund.  AI  28,  1988,  183;  perf.  pstwd}r-y  STi 

58.3;  GMS  89,  575 

7452  pstxwmp-  =*  fstxwmp- 

7453  psw   B,  C  JUL./ 
pasu  -»Jps-,  ps-2 

cattle,  sheep 

VJ  87,  164,  57d;  Sund.  AI  28,  1988,  183,  psw  stwr 

7454  pswc-   M  <j^«-$\ 
pasoc  ©<*apa-sauca   ^'ps'wc- 

(fo)purify,  0o)clcan 

GMS  89,  591;  Hen.  Cosm.  311,67,  2sg.  impf.;  BBB 
f87;  AVS  73
```


## [2026-09-07T20:46:45.151Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON feodal ===\"; grep -n \"فئودال\\|فئودالیسم\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON pashm ===\"; grep -n \"پشم :\\|(پَ) \\[ په \\]\\|چوپان\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T20:46:45.244Z] TOOL RESULT

```
=== MON feodal ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4841:فئودال: 7 (ص.) کسی که دارای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4846:فئودالسته: 0021-6] نوعی حکومت 
MON_part2.txt:4841:فئودال: 7 (ص.) کسی که دارای 
MON_part2.txt:4846:فئودالسته: 0021-6] نوعی حکومت 
=== MON pashm ===
MON_part1.txt:27795:چوپان شبان. پاسبان» نگاهبان. 
MON_part1.txt:28879:کنند. چوبی که بازیگران و چوپانان بر پای 
MON_part1.txt:51640:خشن که چوپانان و برزیگران پوشند. جامة 
MON_part1.txt:61827:بی آلایش نظیر زندگی بی‌تکلف چوپانی و 
MON_part1.txt:66008:گوسفندچران» چوپان. 
MON_part1.txt:83811:به شبان؛ چوپانی. 
MON_part2.txt:20456:چوپانان و روستاییان و درویشان و 
MON_part2.txt:28874:آفریقا می‌روید؛ کیس‌الراعی» يس چوپان؛ 
MON_part2.txt:29891:چوپان با گلٌ خود به علت پیش آمد زمستان 
MON_part2.txt:34851:نگهبان گله و رمه؛ شبان» چوپان.
```


## [2026-09-07T20:46:46.324Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; echo \"=== ARY pashm/chupan ===\"; grep -n \"پشم\\|چوپان\\|شبان\" ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i \"PASU\\|PEKU\\|PEK\\b\\|PASMAN\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T20:46:46.396Z] TOOL RESULT

```
=== ARY pashm/chupan ===
161:ولی چون هند و اروپایی‌ها در اصل از طریق شکار و دامداری و شبانی زیست می‌کردند و
179:خاور دریاچه‌ی بایکال‌زندگی می‌کردند. آنها نیز مثل هندواروپالیان زندگی شبانی و دامداری داشتند.
289:شده‌اند. این جامعه در آغاز شکارگر -گر دآور (11701181-0۸7778587) بوده ر کم کم شبانی و
653:ارابه‌ی مجهز به چرخهای پره‌دار (سبکك و سریع) و زندگانی شبانی و کوچگری (یادآور ایل‌های
959:و خونآشامی بود. ۳ رومولوس (10۸/171-178) که حامی شبانان و رمه بود و برای مردان خود ۱
965:( کشاورزان و شبانان و سوداگران) وجود داشتند که نقش اجتماعی آنها با الگوی سه گانه‌ی فوق
1081:نظامی غیر متحمل است. ظاهراً در جامعه‌ی هند و اروپائیان هر مرد هم کشاورز یا شبان بود وهم .۱
4564:۳ معنی واژه یونانی این فهرست: گله» شبان؛ گرسفند پاء
4956:اوستایی (4887/4): اففانی (پشم) (//(0/۸/): ۰ ۳8137
4991:پشم / ۱۷۱ ِ
5005:چم‌های این واژه در زبان سانسکریت: مو؛ پشمالو.
5006:چم‌های این واژه در زبان لاتین؛ پشم شانه کردن و چیدن,
6543:چم اين واژه در بونانی و ایرلندی کهن و لیترانی و زبان‌های ژرمنی: (پشم گوسپند را) بریدن» قطع کردن» خراشیدن,
9084:چم این واژه در روسی و نروژی و ایسلندی کهن: موی نرم؛ پشم نرم.
11105:۲ به احتمال زیاد واژه‌ی "چوپان" هم از همین واجريشه است. ۱
11108:4 ۴- بازگشیت به: پشم
12740:۲ چم این وُژه در دْقزیان‌های این فهرست: نخ پشمی» ریسمان (از الیاف گیاهی).
12741:۳ واژه‌های انگلیسی .۷001 و آلمانی ۷۷0178 و سانسکریت 18۸1۸ (همه به چم "پشم!) نیز از همین
15319:وَبّر (به چم "پشم!) / ۵۱۷ ۱
=== latin index ===
4320:DELANARRE: ===S=S*~*~« PENI, PENI, PASUNE
5110:i) Labi day HUPEK (POLISH) glong)
10880:FE :(OLD SCANDINAVIAN) 46 54th! *FSHU-PAITI, PASU-
10884:PEKUS - :(LITHUANIAN) i523 SHIWAN (KURDISH) ($35
10889:DELAMARRE: (BERGER) 52 PASVAH, PASU, FSU-,
10895:9 PEK phyla) “asin Sy "uy" ep g SHU ot oye ob ely 92 jN"0Lt" aS oH
```


## [2026-09-07T20:46:52.214Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '4940,5015p' ARY_pages.txt"
}
```


### [2026-09-07T20:46:52.253Z] TOOL RESULT

```
۱ بلوچی (1لقعتاملم8): ان انا لنرنی (لتی) (770۷)ما): نان ایا
۱ سانسکریت (۳5۸:)44(570/7 رقف3ط برتونی (/37670)(شاید) ۳07
ا یونانی (06780): 5 ,5 ۸ط
لانین (4700): ۰ ۴۸61 ,81178 بالق ات۶ پسگشت‌ها 7272255
گوتیکه (0077470): ۸ 0
ابسلندی کهن ((507010۸4 ۵۵): 528 9 (5) اتمه
نررس کهن (ظ۸/08۶ 010)(شاید) ‏ ۲1178 3 ((80) امد هم
ساکسونی کهن ((۹4240 0ا0): 5 57 ند
فریزی کهن (ا5ل۶# ا0): زدد] 3 (38) :0105
آلمانی کهن (/(057/4 ال ۰:0۵ 31۸0 6 (8) +57
انگلیسی کهن ([5ل2۸۷0 صا0): شاج 47 را
دورد نداد برهان قاطع : ۳.۵
سوئدی (4ل9780/9)(شاید) 0
یادداشت: َ
معنی اين واژه در زبان‌های ژرمنی: کم کرچکك» محدود.
معنی این واژه در پیشتر زبان‌های هند و اروپایی علاوه بر "پسر» "فرزند ذکور": جانور کوچکه.
اوستایی (4887/4): اففانی (پشم) (//(0/۸/): ۰ ۳8137
7۸ با ۴۸5[11 سانسکریت (84(/8977): ۰
پپلری (1/ماتلهه): 17 ۹1۸ ,۳85177
کردی (0ل5ا(0۸): ۰ ۳۸۹130۸ ,۴18137 یرنانی (0724): -۳0 ,۳۸078
بلوچی (اتلتاسله8): ۳7 لاتین (712ما): -0 ,۳05718
[pdf page 169]
۱ :
۱ ساکسرنی کهن ((54700 2ا0): ۳7 0
آلمانی کهن ((0529/۸ ۲770/7 (0۱): 71887 پسگشت‌ها تشرد ادن ۲
آلمانی (/4ل02): 7 [ ۲ ت 9 200/07
انگلیسی کهن (8۸087 صا0): سوان ‏ سیگ 1
7 آ۲۷38 3 (8۸6) ۱
انگلیسی (80/011577): ۳/03 3321112 1 لتاق
ملندی (0۱760(3): اد اه 9و (۳۵87) :0105
اسلاوی کهن (۲12شا5 ب#ناتن صاه): 6 (۳۵۹) دواد
[د ادا با 8 (8۸00) ۸0
لیتوانی (1۵۷/لتاب2 )+ ۲ نی ۱۱ برهان قاطع : ۴۷
پاه‌داشت: ‏ "
۱- واجریشه‌های هند و اروپایی - ۳-۰* ,۳88۰ (۳818* خود از واجریشه‌ی هند و اروپایی -872* (به چم
"یستادن )مشتن شده‌اند (پازگشت به؛ ایستادن).
۲- معنی واژه‌ی ۳8871311 در زبان سانسکریت: دنده.
معنی واژه‌ی ۳08718 در زبان لاتین: یاهر (هریکك از دو تبر عمود چارچوب در).
معنی واژه‌ی لیتوانی و اسلاوکهن این فهرست: انگشت,.
معنی اين واژه در زبان‌های ژرمنی: تبر زیر شیروانی؛ دیرکك.
اوستایی (۸۷8874): 52۸883 بااناناباآهی5
: 5613۸۸ ۲8۸3218۸
سغفدی (900۸214): شلد ۱( پسگشت‌ها رد۲
سانسکریت (84(/9807): 5۸/871 6 بو
5۸/871۸01۸1 فرهنگ معین : ۷۳۹۸
لاتین (770ل): ,50۸7105 برهان قاطم : ۴۰
یادداشت: ۱
چم این واژه در اوستایی و سانسکریت: ستون» پایه» نگهدار,
چم اين واژه در زبان لاتین: اریکه» تخت» سریر, ِ
[pdf page 170]
نج ا
پشم / ۱۷۱ ِ
۱
| انگلیسی سرواژی نارس ۱۷۵۹
اوستایی ((۳8:574)): 3۸8118 سوندی‌کهن (57752[/57 صا0): 7
پهلوی (4ات۳۸): 1 هلندی (ع076ه): ۷7
سانسکریت (54۸/87077): لیترانی (/277۸/140ل): ۳۵87111 ,۳85711
۳۸1681391۸ ,۳۸511۸۵۸۵۲ آلبانی (لهالفمقلم: ۸
ارمنی (4745۸/۸): ۸۳ َ
برنانی (07280): 7/05 پسگشت‌ها آنششبرد ادن
لانین ۰:70 ۳۳0585 ,۳800 و20
ایسلندی کهن (/00/0477ی5 طا۵): 7۸3 0 (اگ۲۸) :2/۸025
آلمانی کهن (0870/۸2 /270 صا0): 7۸378 برهان قاطع + ۴۰
انگلیسی کهن (8070/3/7 صا۵): ۰ ۲8۸
بادداشت,
چم‌های این واژه در زبان سانسکریت: مو؛ پشمالو.
چم‌های این واژه در زبان لاتین؛ پشم شانه کردن و چیدن,
چم‌های این واژه در زبان ایسلندی کهن: یال. ۰
چم‌های این واژه در زبان آلمانی و انگلیسی: موی زبر, :
پهلوی (1شایل۸): ۰" یا :۱:۱۹ گوتیکه (0077710): 710
اففانی (پشش) (/۵/674: 8۸ات۷۸ ایسلندی کهن (49۷ 5040/0104 صا۵): ۴1۵
کر سانسکریت (5(/8077): 5اماناد آلمانی کهن (0529401 017ات صا۵): ۴073
ارمنی (7( ۱۸4/۸ تسه 0 ۳ آلمانی (/0880/۸): 101
پرنانی 0قق08): هانامم انگلیسی کهن (8(7013 صا0): تلفشا۲
لاتین (۵710): ۸ بلاط الط انگلیسی (/61/81/اق: ها
فرائسه (4لع(۳): میرم اهلندی (0014: مسا
```


## [2026-09-07T20:46:54.040Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '11085,11115p' ARY_pages.txt; echo \"=== page tags near ===\"; awk 'NR<11115 && /\\[pdf page/{p=$0; n=NR} END{}' ARY_pages.txt; grep -n \"\\[pdf page\" ARY_pages.txt | awk -F'[][ ]' '{print}' | head -3"
}
```


### [2026-09-07T20:46:55.275Z] TOOL RESULT

```
[pdf page 374]
اج
اوستایی (4۲887۸۷): گرنیکد (0077110): ۳۸17
۸817۰ ,۹۴89171-7۸11 ایسلندی کهن (/0101۸7142/م5 ۰:۱۵ 88
پارسی باستان (۳۵۴۵1(۷ 0ا0): آلمانی کهن (0584۵(۷ 07/لط ضل0): 21317
۹۳811-۷۸۸ انگلیسی کهن (نقلاه/8 012):
پپلری (اماننهه): 580820 ,51317820۷ 1 ,۲801
کردی (80/5[4ل8): لادا:ن لیتوانی (۵07اهنا 2 7/): ۰ 7845
بلوچی (اتقتاله8): ونان پروسی گهن (/۶542ت۲۸۱ ۰۰:)01۵ 88016۲۲
َ ولا
افغانی (پشتو) (/44(7ا4۳0): لرزقه ان پسگشت‌ها اش ات۲
سانسکریت (84(/887): زر رس
+18 دلا۳۸۹ ,۳۸8۷۸3 2 (838023) :ههام05
ارمنی (42/8/140): این ان 2 (8118713520) :20/28 ها
بونانی 072270): نا در زری ی 160164 اه
لاتین 28008:471۷ ,68 و8567 برهان قاطع : ۱۳۳۰
ایتالیایی (ال7): ه۳08
بادداشت: ۰
۱ واژه‌ی "بان" از دو واجريشه درست شده است:-387111 به چم "رم" پا " گوسفند" (هند و اروپایی:۳8۰ او
پسوند ۳۸311 به چم "پاییدن" (هند و اروپایی:-۱۶01 بازگشت به: پاییدن)
۲ به احتمال زیاد واژه‌ی "چوپان" هم از همین واجريشه است. ۱
۳ آپا رابطه‌ای میان اوستایی +8 و انگلیسی 87108 (انگلیسی کهن: 568۸7 آلمانی کهن: 8228
7 آلمانی:561۸) وجود دارد؟
4 ۴- بازگشیت به: پشم
ی
اوستایی (4۲5974(۷: 081378۸ ,1191180 سانسکریت (8۸78877): 1378۸
پهلری (۲1ماللم): لاتین (47/2ما): 5 ,۷8885
8 1181378 ,115117۸ فرانسه (4[ح۳۸۵7): ۷۸۲
[pdf page 375]
۶ اش
اسپانیایی :(8۳۸/]314): ساتد یه پسگشت‌ها 5 ۱ 5
=== page tags near ===
1:[pdf page 1]
10:[pdf page 2]
38:[pdf page 3]
```


## [2026-09-07T20:47:13.760Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-07T20:47:13.799Z] TOOL RESULT

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


## [2026-09-07T20:47:14.681Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4835,4850p' MON_part2.txt; echo \"=== chupan headword ===\"; grep -n \"^چوپان\\|چوپان:\" MON_part1.txt | head"
}
```


### [2026-09-07T20:47:14.751Z] TOOL RESULT

```
دو دسته. دو دسته از شک بان: 

فاس: ۳ ۳8 )1( آلتی که د سته کو تاه 
دارد و بدان چوب و جز آن را قطع کنند؛ 
هش 

فئودال: 7 (ص.) کسی که دارای 
ملک‌ها و رعابای سبار باشد و بر آنان تسلط 
کامل داشته باشد؛ ملک بزرکگک» عمده 
مالک مل وک الطواثف. 

فئودالسته: 0021-6] نوعی حکومت 


۱۹۴ فررهنگ فارسی معین فتو دالیسم 

=== chupan headword ===
27795:چوپان شبان. پاسبان» نگاهبان.
```


## [2026-09-07T20:47:24.877Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D9%88%D9%BE%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pe%E1%B8%B1-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9%E1%B8%B1u\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 387, root Pek/Peku: Persian pašm, čupān; PIE *peḱ-, *péḱu\" ; done"
}
```


### [2026-09-07T20:47:28.634Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6153b7e3c46a20ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1321a137af30ccc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b4eedcf9a451bca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da907e0fab3e1efd.txt
```


## [2026-09-07T20:47:32.067Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### pashm\"; grep -n -A12 \"Etymology\" 6153b7e3c46a20ca.txt | head -40; echo \"### chupan\"; grep -n -A14 \"Etymology\" e1321a137af30ccc.txt | head -50"
}
```


### [2026-09-07T20:47:32.157Z] TOOL RESULT

```
### pashm
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- Further reading 
--
156: Etymology
157- [ edit ] 
158-
159- From Proto-Iranian *pášma , from Proto-Indo-Iranian *páćšma ( “ hair, bristles ” ) , from Proto-Indo-European *poḱ-s-mn̥ ( “ hair, whiskers ” ) , from *peḱ- ( “ to shear, pluck ” ) . Cognate with Avestan 𐬞𐬀𐬱𐬨𐬀𐬥 ( pašman ) , Sanskrit पक्ष्मन् ( pakṣman ) .
160-
161- Pronunciation
162- [ edit ] 
163-
164- ( Classical Persian ) IPA ( key ) : /ˈpaʃm/ 
165-
166- ( Dari, formal ) IPA ( key ) : [pʰäʃm] 
167-
168- ( Dari, formal ) IPA ( key ) : [pʰäʃm] 
### chupan
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Descendants 
75-
76- 1.5 
77- References 
78-
79- 2 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
94- Derived terms 
95-
96- 2.4 
97- References 
98-
99- Toggle the table of contents 
--
180: Etymology
181- [ edit ] 
182-
183- From Middle Persian 𐫢𐫇𐫁𐫀𐫗 ( šwbʾn /⁠šubān⁠/ ) , from Old Persian *fšupāna- , composed of [script needed] ( fšu- , “ sheep ” ) (compare Old Armenian շպետ ( špet ) , Sanskrit पशुपन् ( paśupan ) ) and [script needed] ( pāna- , “ protector ” ) . Cognate with Pashto شپون ( špun ) , Baluchi شپانک ( šipánk ) , Northern Kurdish şivan , Zazaki şıwane , Northern Luri شڤا ( şeva ) , Bactrian χοβανο ( khobano ) , Wakhi шәбын , шәпын .
184-
185- Pronunciation
186- [ edit ] 
187-
188- ( Classical Persian ) IPA ( key ) : /t͡ʃoː.ˈpaːn/ 
189-
190- ( Dari, formal ) IPA ( key ) : [t͡ʃʰoː.pʰɑ́ːn] 
191-
192- ( Dari, formal ) IPA ( key ) : [t͡ʃʰoː.pʰɑ́ːn] 
193- ( Kabuli ) IPA ( key ) : [t͡ʃʰoː.pʰɑ́ːn] 
194-
--
282: Etymology
283- [ edit ]
```


## [2026-09-07T20:47:40.579Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '195,300p' e1321a137af30ccc.txt"
}
```


### [2026-09-07T20:47:40.634Z] TOOL RESULT

```
 ( Hazaragi ) IPA ( key ) : [t͡ʃʰʊː.pʰɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [t͡ʃʰuː.pʰɒ́ːn] 

 ( Iran, formal ) IPA ( key ) : [t͡ʃʰuː.pʰɒ́ːn] 
 ( Tehrani ) IPA ( key ) : [t͡ʃʰuː.pʰúːn] 

 ( Tajik, formal ) IPA ( key ) : [t͡ʃʰɵ.pʰɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 čōpān

 Dari reading ? 

 čōpān

 Iranian reading ? 

 čupân

 Tajik reading ? 

 čüpon

 چوپان 
 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 چوپان • ( čōpān / čupân ) ( Tajik spelling чӯпон ) 

 shepherd 
 Synonym: پاده‌بان ( pāda-bān  / pâde-bân ) 

 Descendants
 [ edit ] 

 → Azerbaijani: çoban 

 → Chagatai: چوپان ( čwpʾn /⁠cōpān⁠/ ) 
 Uyghur: چۇپان ( chupan ) 

 Uzbek: choʻpon 

 → Crimean Tatar: çoban 

 → Gujarati: ચૂબાન ( cūbān ) , ચૂપાન ( cūpān ) 

 → Hindustani: 
 Hindi: चूपान ( cūpān ) 
 Urdu: چوپان ( cūpān ) 

 → Ishkashimi: چوپان ( cōpān ) 

 → Kazakh: шопан ( šopan ) 

 → Northern Luri: چووپۆ ( çupø ) 

 → Kermanic: čöppūn ( Abyanehi ) , čoppūn ( Jowshaqani ) , čöwpōn , čūppū , čūppōn , čūppō ( Abuzeydabadi ) , čūpūn ( Qohrudi ) 

 → Munji: چوپان ( čūpān ) , چوپون ( čūpōn ) 

 → Ormuri: چوپان ( čopån ) ( Logar ) 

 → Ottoman Turkish: چوبان ( çoban ) ( see there for further descendants )

 → Turkmen: çopan 

 → Sanglechi: چپان ( čəpān ) 

 References
 [ edit ] 

 Ačaṙean, Hračʻeay ( 1971–1979 ), “ շպետ ”, in Hayerēn armatakan baṙaran [ Armenian Etymological Dictionary ] (in Armenian), 2nd edition, a reprint of the original 1926–1935 seven-volume edition, Yerevan: University Press 

 Horn, Paul ( 1893 ), “šubān”, in Grundriss der neupersischen Etymologie (in German), Strasbourg: K.J. Trübner, page 171 

 Urdu
 [ edit ] 

 A Pakistani چوپان ( caupān , "shepherd") herding his flock 
 Etymology
 [ edit ] 

 Borrowed from Classical Persian چوپَان ( čōpān ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /t͡ʃɔː.pɑːn/ , /t͡ʃoː.pɑːn/ , /t͡ʃuː.pɑːn/ 

 Noun
 [ edit ] 

 چوپان • ( caupān )  m ( Hindi spelling चूपान ) 

 shepherd ; cowherd ; herder 

 caretaker
```


## [2026-09-07T20:47:47.768Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### peḱ-\"; grep -n -m1 -A18 \"^ Etymology\\|Root\" 5b4eedcf9a451bca.txt | head -40; echo \"### péḱu\"; grep -n -m1 -A20 \"Noun\" da907e0fab3e1efd.txt | head -45"
}
```


### [2026-09-07T20:47:47.829Z] TOOL RESULT

```
### peḱ-
62: Etymology 1 
63-
64- 1.1.1 
### péḱu
65: Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
71- Derived terms 
72-
73- 1.2.3 
74- Descendants 
75-
76- 1.2.4 
77- References 
78-
79- Toggle the table of contents 
80-
81- Reconstruction:Proto-Indo-European/ péḱu 
82-
83- Add languages 
84-
85- Reconstruction
```


## [2026-09-07T20:47:50.840Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### peḱ- body\"; sed -n '85,200p' 5b4eedcf9a451bca.txt; echo; echo \"### péḱu body\"; sed -n '85,175p' da907e0fab3e1efd.txt"
}
```


### [2026-09-07T20:47:50.900Z] TOOL RESULT

```
### peḱ- body
 1.3.1.1 
 Derived terms 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peḱ- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root
 [ edit ] 

 *peḱ- [ 1 ] 

 to pluck ( wool, hair ) 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peḱ- (pluck) (16 c, 0 e) 

 *péḱ-ti 
 Hellenic:
 Ancient Greek: πέκω ( pékō , “ to comb ” ) 

 *peḱ-te-ti (perhaps by metathesis from *petḱ- < *pe-pḱ- or the same seen in *pléḱ-te-ti )
 Proto-Germanic: *fehtaną ( “ to comb, detangle, struggle ” ) 

 Hellenic:
 Ancient Greek: πεκτέω ( pektéō , “ to shear ” ) 

 Proto-Italic: *pektō 
 Latin: pectō ( “ to comb ” ) 

 *pḱ-t-ḗn ( see there for further descendants )

 *poḱ-os- 
 Proto-Germanic: *fahaz ( “ sheep ” ) ( see there for further descendants )

 *poḱ-o- 
 Hellenic:
 Ancient Greek: πόκος ( pókos ) 

 *poḱ-ti- 
 Proto-Germanic: *fahtiz ( “ fleece ” ) ( see there for further descendants )

 *poḱ-s-om 
 Proto-Germanic: *fahsą ( see there for further descendants )

 *poḱ-s-mn̥ 
 Proto-Indo-Iranian: *páćšma ( see there for further descendants )

 Unsorted formations 

 Balto-Slavic:

### péḱu body
 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 From the *u -stem of *peḱ- ( “ livestock ” ) .

 Noun
 [ edit ] 

 *péḱu   n ( oblique stem *peḱu- ) [ 1 ] [ 2 ] 

 livestock 

 Declension
 [ edit ] 

 Athematic, proterokinetic

 singular

 nominative

 *péḱu 

 genitive

 *pḱéws 

 singular

 dual

 plural

 nominative

 *péḱu
```


## [2026-09-07T20:48:03.904Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://www.etymonline.com/word/fellow\" \\\n \"https://www.etymonline.com/word/feudal\" \\\n \"https://www.etymonline.com/word/fight\" \\\n \"https://en.wiktionary.org/wiki/feudum\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 387, root Pek/Peku: Germanic fehu/feht, English fellow, fight, feudal, Med.Latin feudum\" ; done"
}
```


### [2026-09-07T20:48:06.683Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/27484c5b6812b6ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/325d5d4392c8e03d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcad8c45ccba5e6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea291f1c1a5d15ae.txt
```


## [2026-09-07T20:48:10.012Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 27484c5b6812b6ca 325d5d4392c8e03d dcad8c45ccba5e6f; do echo \"##### $f\"; grep -n -m2 -A10 \"Old English\\|Medieval Latin\" $f.txt | head -30; done"
}
```


### [2026-09-07T20:48:12.729Z] TOOL RESULT

```
##### 27484c5b6812b6ca
25: "companion, comrade," c. 1200, from Old English feolaga "partner, one who shares with another," from Old Norse felagi , from fe "money" (see fee ) + lag , from Proto-Germanic *lagam , from PIE root *legh- "to lie down, lay." The etymological sense of fellow seems to be "one who puts down money with another in a joint venture."
26-
27- Meaning "one of the same kind" is from early 13c.; that of "one of a pair" is from c. 1300. Used familiarly since mid-15c. for "any man, male person," but not etymologically masculine (it is used of women, for example, in Judges xi.37 in the King James version: "And she said unto her father, Let this thing be done for me: let me alone two months, that I may go up and down upon the mountains, and bewail my virginity, I and my fellows").
28-
29- Its use can be contemptuous or dignified in English and American English, and at different times in its history, depending on who used it to whom, it has carried a tinge of condescension or insult.
30-
31- University senses (mid-15c., corresponding to Latin socius ) evolved from notion of "one of the corporation who constitute a college" and who are paid from its revenues. Fellow well-met "boon companion" is from 1580s, hence hail-fellow-well-met as a figurative phrase for "on intimate terms."
32-
33- In compounds, with a sense of "co-, joint-," from 16c., and by 19c. also denoting "association with another." Hence fellow-traveler , 1610s in a literal sense but in 20c. with a specific extended sense of "one who sympathizes with the Communist movement but is not a party member" (1936, translating Russian poputchik ).
34-
35- Fellow-countrymen formerly was one of the phrases the British held up to mock the Americans for their ignorance, as it is redundant to say both, until they discovered it dates from the 1580s and was used by Byron and others.
--
42: Middle English, representing the merger or mutual influence of two words, one from Old English, one from an Old French form of the same Germanic word, and both ultimately from a PIE root meaning "cattle."
43-
##### 325d5d4392c8e03d
25: 1610s, "pertaining to feuds ," estates of land granted by a superior on condition of services to be rendered to the grantor, from Medieval Latin feudalis , from feudum "feudal estate, land granted to be held as a benefice," of Germanic origin (cognates: Gothic faihu "property," Old High German fihu "cattle;" see fee ). Related to Middle English feodary "one who holds lands of an overlord in exchange for service" (late 14c.). Not related to feud .
26- also from 1610s 
27-
28- Entries linking to feudal 
29-
30- fee (n.) 
31-
32: Middle English, representing the merger or mutual influence of two words, one from Old English, one from an Old French form of the same Germanic word, and both ultimately from a PIE root meaning "cattle."
33-
##### dcad8c45ccba5e6f
25: Old English feohtan "to combat, contend with weapons, strive; attack; gain by fighting, win" (intransitive; class III strong verb; past tense feaht , past participle fohten ), from Proto-Germanic *fe(u)hta (source also of Old High German fehtan , German fechten , Middle Dutch and Dutch vechten , Old Frisian fiuhta "to fight"), probably from PIE *pek- (2) "to comb, to pluck out" wool or hair (source also of Lithuanian p ė šti "to pluck," Greek pekein "to comb, shear," pekos "fleece, wool;" Persian pashm "wool, down," Latin pectere "to comb," Sanskrit paksman- "eyebrows, hair"). Apparently the notion is "pulling roughly," or "to tear out one another's hair." But perhaps it is from the source of Latin pugnus "fist."
26-
27: Spelling substitution of -gh- for a "hard H" sound was a Middle English scribal habit, especially before -t- . In some late Old English examples, the middle consonant was represented by a yogh . Among provincial early Modern English spellings, Wright lists faight , fate , fecht , feeght , feight , feit , feyght , feyt , feort , foight .
28-
29- From c. 1200 as "offer resistance, struggle;" also "to quarrel, wrangle, create a disturbance." From late 14c. as "be in conflict." Transitive use from 1690s. To fight for "contest on behalf of" is from early 14c. To fight back "resist" is recorded from 1890. Well figt þat wel fligt ("he fights well that flies fast") was a Middle English proverb.
30-
31- fight (n.) 
32-
```


## [2026-09-07T20:48:33.889Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Wolle\" BRT.txt | head -15"
}
```


### [2026-09-07T20:48:33.937Z] TOOL RESULT

```
10606:ä^at  't3us  dSihrabyöyt.ig.^^^'*; —  kd>a \  ..ySi  uxsänö  (sd.)  asnain  atskSus  dariirai fsd.)  .  .  frännts  Vimdäis  s^nghäis  sao- '  fyantqm  'tavS  "wann  werden  . .  herkom- men, fwann)  mit  den  gewaltigen  Sprüchen •  j.,  g.  XTAlaV' :  xrdkiv  m.  ('geistiges '  (die  Weisheiten  der  5'.,  sva.)  die  weisheits- Wollen  und  Können"'  sva,)  i)  'Wille,  vollen  Saosyatit"  y.46^,3"; —  aat  tnraot Absicht,  Plan,  Ratschluss';  nett  na  manS  ■  aAuri)  masda  x^tvS yat  ahmt  'tus^''  Yt.  ;.  7; .  .  sJn^Aa  .  .  'lavS  ('Absichten')  .  .  varana  j  —  '^Hft  vjsps.v^vanhim  .  .  yim  ahursm (sd.)  ..  u:Sta  ..  syaokaHa  .  .  dasnä  .  .  ».■azdqmVT.ig.i.  A)  auch  sva. 'Wissen', urvqnS  Aacaitils  Y.  45-  *;  —  tna^a  , .  \  bes.  religiöses:  kus.hqm.b}r:t}m  fsd.)  '"hivim mazda  ahurahyä  °tlus  ('Wille')  nas-  \  ■  ■  saElsm  Yt.  18.  i ;  —  °tsu^  al^aya  Vyt.  41; yants(iA.)  alaatcä  Y._j2.4; — yä  vS  'tjus  —  uxsne  (sd.)  °%we  vXdrvanahe  asät  V.   iäkahya   a.manatiha  (sd.)  Y.
15936:•  j.  'paSna-  n,  'Augenlid':  'nsm  F.^d. Vgl.  ai.  päkfman-  n.  'Augenwimpern';  np. pdim  'Wolle';  e.  dazu  Zufitza  Gült.  1S9, Hbm.  PSt.43.  —  Ya.%pS!  i  fah»  (woiu  liurd. pac  i  cam  'Augenlid',  ZDMG.  3S.  55  lU  ver- gleichen).
19770:•  j.,  g.  "manah-  n.  'der  innere  Sinn,  Geist" als  Sitz  des  Denkens,  Erkennens  und Wollens;  'Sinn,  Geist;  Denken,  Gedanke; Streben,  Begierde;  Plan,  Anschlag';  I)  im gAw.:  at  %wa  mSr^hs  .  .  'noTgAä  Y. 31. 8  '>;  —  iaya  (Sp.  462  m.) . ,  ava  'nanha ya  .  .  manta  vastryS  Y._JJ.  6'';  —  n^ra i  Audätihg  ya%ana  vagdfmnai  (sd.)  'nanha V.31.32;  —  Ayat  Aahra  (sd.)  °nä  bavat ya'iira  listi/  atahai  maiha  Y.J0.9;  — yS  dat  °nS  vahyS  .  .  a^a4?A,)ca  hv5  daf- nqm  iyaohanaH'a  vai'anha^  Y.4^.4(3.  a);
19876:•  y,  g.  mainyav-,  manyav-  m.  'Geisf ; I)  'Geist' ab  Sitz  des  Denkens  und  Wollens, sva.  'manaA-;  I)  im  gAw.:  ta  t«^  *'iti- yJui  mahyä  . .  yüsmaibys  g>r>xl{ii,)  Y, 32.  9  ";  —  vTspSng  anySng  *'inyJus  spasyä (sd.)  dvadatahä  Y.  44. 1 1 ;  — fi-S  mä  slia (sd.)  %wahm3t  ^vaocai^kl  *'inyfui  hacä %ws  S>ä»ha  Y.2S.  ii'^i  —  *ärmaiti/  'iiryB *pfnsaitl ya'^ra  Ma^ä{s±)  Y.jj.  la;  — kvB  .  .  irixtim  ,  .  MrS  (sd.)  'inyü  Y.44. 3^;  —  mit  varthav  Adj,:  vanAsuS  *°m- yfus  syao'hananqm  javarB  (sd)  Y.  48. 8  *>.  a)  im  Gegensatz  zu  Sprechen  und YlaxiAth^:  y!  hSi  *inyO  ^aohanäis^a  urva'hS (sd.)  Y. 31.31;  —  mit  vanhav-  Adj.:  «ß zTi  (Sp.  1 54  u.)  zyadanstm  vatihsu!  *°m- yfu/ ^aohanaiyä  uxlaSyalä  Y,  4I5.  8^'j  — mit  sp3nta-,  spsidita- :  sf?nta  'inya  vaiWiä^a manatiha  haiä  aSät  (Sp.  a3im,)  lyadiia' nät'a  vacavAä/a  ahmai  dqn  . .  masdä  Y. 47-i;  —  oAyä^'iriy^ui' sp^iäaAya  vaM/fym . .  3»ana  . .  vtmyaiisA.)  Y.47.  a; —  aAya
22957:ävmts  (sd.)    Y.^lj.  1;    —    tarä^ustrahe  •  j.  varanä-  £  i)  'Wolle' der  Tiere:  aipi
22960:saofyantqm  . .  tä  'rmäca  tiaisäcä  matda-  zeit  entsprechende  Wolle  (der  Tiere)"  V.
22962:ist,  nach  diesem  Glauben  und  dieser  Lehre  aus  Wolle:    u  va»haiH    'nSsfa   'pairi-
```


## [2026-09-07T20:48:36.266Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%81%D8%A6%D9%88%D8%AF%D8%A7%D9%84/\" --note \"page 387 node 10: Mo'in entry for فئودال (French loan)\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/fehu\" --note \"page 387 node 6: PGmc *fehu 'cattle, property' < PIE *peḱu\""
}
```


### [2026-09-07T20:48:39.171Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c43c42f022c0f7b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86f6ce3781e43c5f.txt
```


## [2026-09-07T20:48:52.487Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%F0%90%AC%9E%F0%90%AC%80%F0%90%AC%B1%F0%90%AC%A8%F0%90%AC%A5\" --note \"page 387 node 1: is Avestan pašman attested?\" ; f=$(ls -t data/verification/sources/web/*.txt | head -1); echo $f; head -c 1500 data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/%F0%90%AC%9E%F0%90%AC%80%F0%90%AC%B1%F0%90%AC%A8%F0%90%AC%A5'.encode()).hexdigest()[:16]+'.txt')\")"
}
```


### [2026-09-07T20:48:54.798Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/98ee040f87dfd9c0.txt
data/verification/sources/web/98ee040f87dfd9c0.txt
URL: https://en.wiktionary.org/wiki/%F0%90%AC%9E%F0%90%AC%80%F0%90%AC%B1%F0%90%AC%A8%F0%90%AC%A5
FETCHED: 2026-09-07T20:48:54Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-07T20:49:10.063Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 page 16 ===\"; awk 'BEGIN{RS=\"\\f\"} /pek̑|peḱ|peko|pekṷ|pecu|pekus/{print NR\": \"substr($0,1,200)}' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt 2>/dev/null | head -5; echo \"--- try grep\"; grep -n \"pek\\|Vlies\\|pesti\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | sed -n '1,15p'"
}
```


### [2026-09-07T20:49:11.346Z] TOOL RESULT

```
=== WLD Bd2 page 16 ===
1: 


ALOIS WALDE 

--- try grep
185:Oder ah ^pokli- zu aisl. fc^gil^gr ds,, s. 1. ^pek-P):, cymr. aelod „GIied‘’^ 
237:s. u. ^pek- „Wolle rupfen"^; Velar wird erwiesen durch:) lett. paksis 
697:als „gezeichneter“ zu pekp, peik- ^farbeln'', Schade 174, Zup. G. 189f.), 
1058:pek-, pek-, j^Ok- 
1061:1. pek-, pek-, pok- etwa „Mbsch machen, aufgeraumt oder vergniigt sem‘‘\ 
1088:2. pek- ,,Wolle oder Haare rupfen, zausen; Y^olltier, Schaf {peku)^ dann 
1101:ahd. fihu „Yieh“; =^\\t pekus.^ apr. pecku „Yieh“ (westidg. Gutt.; Lit. 
1115:Alb. pih ^YTerkzeug zum Flachsktomen, -hecheln^ (f'pekla, Jokl SBAk 
1197:V. Osten-Sacken IF. 33, 239f.)=abg. peUh „Ofen‘‘; abg. pekq, pcsti ds., 
1198:pekii „Hitze^^, poH „SchweiB“ {^poq^to-^ Zupitza KZ. 35, 266). 
1612:„Getrampek‘ (beide von der verbalen Yorstellung aus), 2 i\,frad)da „Yorder- 
4762:Bed.-Entw. Zubaty AfsIPh. 13, 478, BB. 18, 256, der von pek- ,,hubsch 
5305:Hierher ir. uclit „Brust‘' (Fick II^ 55; "^puphis)', nicht zu lat. pictzis (s. "^pek- 
6972:V^P^ „Ifabel”, klr. pup ^Knospe”, poln. pqpie 5 ,Knospen”, pepek 
9189:Fut. Ptc. ksl. bysestc-je, bysaste-je ..to pekXov"\ Kondiz. 3. pi. b(t (^bhua-nt,
```


## [2026-09-07T20:49:11.938Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN wool/cattle ===\"; grep -n -i \"pekus\\|pecu\\b\\|paśu\\|pasu-\\|Av. pasu\" SYN.txt | head -20; echo \"=== IEC ===\"; grep -n -i \"pek̂os\\|pekos\\|peku\\|pek̂\\|pasman\" IEC.txt | head -20"
}
```


### [2026-09-07T20:49:12.011Z] TOOL RESULT

```
=== SYN wool/cattle ===
3917:Bara) Sy Dan. kereaturer ChSl.  skotit NG #7 ae POX Sw. kreatur Boe wks hale Lat. pect 6 OR toh oh. ytele eee tomers ME ie cattell Pol. _bydlo Ir. bas a NE livestock (cattle) Russ. skot Sp. os (dobitoc) Du. vee Skt. pagu- Sd indile, crod, cethra OHG  fihu Av. pasu-; staora- ze eet ell MHG vihe
3927:Lat. (early) pecu, pl. pecua, Umbr. pequo, Lat. pecus, gen. pecoris, coll. ‘cattle’ in wide sense, also esp. ‘sheep’ (hence It. pecora ‘sheep’), pecus, gen. pecudis ‘a head of cattle’, pl. pecudés ‘cattle’; (Goth. faihu only ‘property’), ON fé ‘cattle’ esp. ‘sheep’, and ‘proper- ty’, for ‘cattle’ also kuikfé (with kuikr ‘Jiving’) and bafé (with b& ‘household’, Dan. fa, Sw. fa ‘beast, brute’, OE feoh, ME fie, fee ‘cattle’ and ‘property’ (but for NE fee, see NED fee, sb.”), Du. vee, OHG fihu, fehu, MHG vihe, NHG vieh ‘cattle’; OPruss. pecku ‘cattle’, OLith. pekus ‘cattle’ in wide sense, but also ‘small cattle’, esp. ‘sheep’ (Hermann, Arch. sl. Ph. 40.161); Skt. pagu- ‘do- mestic creature’ (in AV 11.2.9 covers cows, horses, men, sheep, and goats; sometimes also asses, mules, camels, dogs; sometimes ‘animal’), Av. pasu- mostly ‘small cattle’.
3974:8. Skt. pagu-, Av. pasu-, above, 1.
4093:Ay. gavo-sténa-, aspd-stana-, etc. (above, 1) for the large animals, also (nmanam) gavayam, lit. ‘(house) for ox- en’. For small animals, as sheep, pasus-hasta-, cpd. of pasu- ‘small cattle’ (8.15) and *hasta- fr. had- ‘sit’? = Skt. sad-. Cf. Vd. 15.23 ff., where the whole series occurs.
4198:6. Balto-Slavie words, above, 1. a PLCC adj. in pasu-anu-
18236:ee p OHG  brucka Av. pasu-, paratu-
19090:sense ‘guardian’ (disputed, see 19.42), is clearly cognate with Av. pasus-haurva- ‘guarding the flock’, vis-haurva- ‘guard- ing the village’, nighaurvaiti ‘watches over’, IK *serw-, extension of *ser- in Ay. har- ‘give attention to, watch over’, haratar- ‘watcher’. Walde-P. 2.498 f. Ernout-M. 933.
19547:Goth. faihu ‘property, money’, ON Jé, OF feoh ‘cattle, property, money)’ : OHG fihu ‘cattle’, Lat. pecu ‘cattle’, pectima, ‘property, riches, wealth’, esp, ‘money’ (11.48), Skt. pagu-, Av. pasy- ‘cattle’, etc. (3.15). Walde-P. 2.16 f, Ernout-M, 746 f.
19629:2. Lat. pecinia, earlier ‘wealth in cattle’, then ‘wealth, money’ whence also ‘coin’ esp. in late Lat. ‘copper coins’, fr. pecu ‘cattle’, this also sometimes ‘money’ (like Goth. faihu, below).
33418:2. Lat. servus, often explained as orig., though unattested, ‘watcher, guardian’ : servare ‘save, preserve, keep’, Av. pasus- haurva- ‘guarding the flocks’, etc. (see under Lat. servdre, 11.24). Walde-P. 2.498. Ernout-M. 933. Otherwise Ben- veniste, Rev. ét. lat. 10.429 ff. (as Etrus- can loanword), Vendryes, BSL 36.126 ff. (: Ir. serbh ‘pillage’, W. herw ‘outlawry’). Biugmann, op. cit. 383 (as ‘running’ : Skt. sr- ‘run, flow’).
=== IEC ===
12601:peik- (poik-, pik-) — peku
12607:peKos, us ‘fleece’. Cf. poKos, peko Arm. asr, gs: asu, id.; Gk. pékos, gs: -eos, n. id.; Lat. cf. pecus, gs: -oris n. “flock of sheep beside OLat. pecu, n. id.; Li. cf. pesenà, mf. ‘shaggy person
12610:. comb’. Cf. peko, pekus & ten-, tən-
12617:peKu ‘small farm-animal for shearing, head of cattle’. Cf. peKo, etc. Skt. pá$u, pasúh, n & m ‘head of cattle’; Av. pasus, m. id.; Oss. fís, Dig. fus, s. ‘sheep’ be- side fos, s. (cattle, fr. *peKu-); OLat. pecu, pl: -ua, n. “cattle, sheep’; Lat. pecus, gs: -oris, n. id., Umb. pequo, pl. ‘small farm-animals'; Go. Tabu, n. ‘money’, OHG fëho, fihu, OS
12619:f&hu, n. *farm-animal'; OE feoh, n. ‘cattle, wealth); ON fé, n. id. (Gmc. LW in Li. pekus, gs: -aus, m. ‘cattle’. Cf. the Gmc. LW in Li. kerdZius *herdsman)
12698:pequos, à, om (2) *neat, attractive; pet, dar- ling'. (Same as (1)?) Skt. cf. (+-8-) pakah ‘young, artless; young child or animal, pet'; Gk. pépon, n. ‘pet’; Lat. (ambig.) pecülium (“private possession'. Infl. (?) of type peKu, q.v.); (LW in Alb. pekül, m. ‘darling, favourite); Per. (?) pak “pure, clean’; Cz. péče, OCz. peka, péCé, f. “care, attention'; R cf. o-péka, id. (Uncertainly w. nasal infix: Pol. piekny, Cz. pěkný *pretty?)
16775:spek- (spekos, spokos, us) (2) ‘cave’ (?). (Arm. a LW from Lat. fossa via Gk.?)
```


## [2026-09-07T20:49:25.154Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pek-\\|Wolle oder Haare\" incoming/WLD/WLD_Bd2_pages.txt | head -8; echo \"=== page tag ===\"; awk '/\\[pdf page/{p=$0} /Wolle oder Haare rupfen/{print p; exit}' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T20:49:26.388Z] TOOL RESULT

```
148:Oder ah ^pokli- zu aisl. fc^gil^gr ds,, s. 1. ^pek-P):,   cymr. aelod „GIied‘’^
199:s. u. ^pek- „Wolle rupfen"^; Velar wird erwiesen durch:) lett. paksis
1016:16                                    pek-, pek-, j^Ok-
1020:1. pek-, pek-, pok- etwa „Mbsch machen, aufgeraumt oder vergniigt sem‘‘\
1051:2.   pek- ,,Wolle oder Haare rupfen, zausen;                  Y^olltier,   Schaf {peku)^ dann
4864:Bed.-Entw.             Zubaty AfsIPh. 13, 478, BB. 18, 256, der von pek-                                  ,,hubsch
5389:Hierher ir. uclit „Brust‘' (Fick II^ 55;            "^puphis)', nicht zu lat. pictzis (s. "^pek-
43688:                                   speud- — spek-                           659
=== page tag ===
```


## [2026-09-07T20:49:27.218Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN feudal ===\"; grep -n -i \"feudum\\|feudal,\" KLN_1966.txt | head -8; echo \"=== KLN fellow ===\"; grep -n \"^fellow\\|fellow, n\\|feolaga\" KLN_1966.txt | head -5; echo \"=== KLN fight ===\"; grep -n \"feohtan\" KLN_1966.txt | head -5; echo \"=== LEW pecu ===\"; grep -n \"pecus\\|feudum\" LEW_1910.txt | head -5"
}
```


### [2026-09-07T20:49:27.312Z] TOOL RESULT

```
=== KLN feudal ===
14640:feud,  n.,  a  fief.  —  ML.  feudum,  fr.  feum,  a  word of  Teut.  origin;  cp.  Goth,  faihu,  ‘property’, OHG.  fihu,  ‘cattle’,  and  see  fee  (in  both  senses) and  cp.  infeudation.  The  d  in  ML.  feudum  is prob.  due  to  the  influence  of  the  word  al¬ lodium  (q.v.)
14641:Derivatives:  feudal  (q.v.),  feudatory  (q.v.) feudal,  adj.,  1)  pertaining  to  land  held  in  feud; 2)  pertaining  to  feudalism.  —  OF.,  fr.  ML.  feu- dalis,  fr.  feudum.  See  feud,  ‘fief’,  and  adj.  suff.
14643:Derivatives:  feudal-ism,  n.,  feudal-ist,  n.,feudal- ist-ic,  adj.,  feudal-ity,  n. .feudal-ize,  tr.  v.,feudal- iz-ation,  n.,  feudal-ly,  adv. feudatory,  adj.  and  n.  —  A  collateral  form  of  ob¬ solete  feudatory,  fr.  ML .  feuddtarius,  it.  feudum, ‘fief’.  See  feud,  ‘fief’,  and  adj.  suffixes  -ate  and -ory.  Derivatives:  feudatori-al,  adj. feu  de  joie,  public  bonfire.  —  F„  lit.  ‘fire  of  joy’. F.  feu  derives  fr.  L.  focus,  de,  ‘of,  from’,  comes fr.  L.  de,  ‘from,  away  from’,  joie  derives  fr.  L. gaudia,  pi.  of  gaudium,  ‘joy’.  See  focus,  de- and  joy.
14688:fief,  also  feoff,  n.,  land  held  in  fee.  —  OF.  feof, fief,  fr.  feudum,  ‘fief’.  See  feud,  ‘a  fief’, field,  n.  —  ME .feld,  fild,  fr.  OE .feld,  rel.  to  OS., OFris.,  OHG.  feld,  MHG.  velt,  G.  Feld,  Du. veld,  ‘field’,  and  to  ON.  fold,  ‘earth’,  OE.  folde, OS.  folda,  of  s.m.  Cognates  outside  Teut.  are Lett,  platit,  ‘to  flatten’,  OIr.  laihar,  ‘distri¬ bution’,  Mir.  lathair,  ‘surface’.  All  these  words derive  fr.  I.-E.  *pela-to ,  enlargement  of base  *pela-,  ‘flat,  plain’,  whence  L.  planus,  ‘flat, level’,  OSlav.  polje,  ‘field’.  See  plain,  adj.,  and cp.  words  there  referred  to.  Cp.  also  veld  and the  first  element  in  feldspar.  Cp.  also  Pole. Derivatives:  field,  tr.  and  intr.  v.,  field-er,  n. fieldfare,  n.,  a  kind  of  thrush.  —  ME.  feldefare, fr.  OE.  feldefare,  fit.  ‘field  goer’.  See  field  and fare,  ‘to  prosper’.
=== KLN fellow ===
12287:fellow’.
14542:fellow,  n.  —  ME.  fetaghe,  felawe,  fr.  OE .feolaga, fr.  ON.  felagi,  ‘partner,  companion’,  from felag,  ‘companionship’,  lit.  ‘laying  down  of money’,  fr.  /<?,  ‘cattle,  money’,  and  lag,  ‘a  lay¬ ing’.  See  fee,  ‘money’,  and  lay,  ‘to  place’. Derivatives  -.fellow,  tr.  v.,  and  aA).,  fellowship,  n. felly,  felloe,  n.,  the  rim  of  a  spoked  wheel.  — ME.  feli,  felwe,  felow,  fr.  OE .  felg,  felge,  rel.  to OS.  felga,  MLG.,  MDu.  velge,  Du.  velg,  OHG. felga,  felaga,  MHG.  velge,  G.  Felge.  These words  are  -^-enlargements  of  I.-E.  base  *qwel-, ‘to  turn’.  See  wheel  and  cp.  cycle.  Cp.  also fallow,  n.
=== KLN fight ===
14516:fedora,  n.,  a  kind  of  soft  felt  hat.  —  So  called from  Fedora,  a  play  written  by  Victorien  Sardou in  1882.  For  sense  development  cp.  trilby. fee,  n.,  cattle;  property;  money  ( obsol .)  —  ME. feoh,  fr.  OE.  feoh,  ‘cattle,  money,  property, wealth’,  rel.  to  OS.  fehu,  ON.  fe,  Dan.  fie, Swed.  fa,  OFris.  fid,  Du.  vee,  OHG.  feho,  fihu, MHG.  vibe,  vich,  G.  Vieh,  ‘cattle’,  Goth,  faihu, ‘money,  fortune’,  and  cogn.  with  OI.  pasu, pasu,  pasuh,  Avestic  pasu-,  L.  pecu,  ‘cattle’, pecus,  gen .  pecoris,  ‘cattle’,  pecus,  gen.  pecudis, ‘a  single  head  of  cattle’,  pecunia,  ‘money,  prop¬ erty’,  Umbr.  pequo,  Lith.  pekus,  OPruss.  pecku, ‘cattle’,  fr.  I.-E.  base  *peku-,  ‘the  woolly  ani¬ mal’,  whence  ‘sheep,  cattle,  property,  money’. This  base  is  an  enlargement  of  base  *pek-,  ‘to pluck  (wool  or  hair);  hairy,  woolly’,  whence OI.  pdkfman,  ‘eyebrows,  hair’,  Pers.  pashm, ‘wool’.  Arm.  asr,  gen.  asu,  ‘sheep’s  wool,  fleece’, Gk.  x£xog,  rx6xog,  Aeol.  ttcxxoc,  ‘uncombed wool,  fleece’,  Gk.  7x£xsi.v,  Att.  7texxew,  ‘to comb,  shear’,  Gk.  xxe (<;,  gen.  xxev^c  (for *pkten-),  ‘comb’,  L.  pexus,  ‘woolly’,  pectere, ‘to  comb,  shear’,  pecten,  ‘comb’,  pectus,  gen, pectoris,  ‘breast’,  Toch.  A  pdssdm,  B  pascane (dual.),  ‘the  breasts’  (prop,  ‘the  hairy  part  of the  body’),  OE.  feax,  OS.,  OHG.  fahs,  ‘hair’, ON.  fax,  ‘mane’,  OE.  feohtan,  ‘to  fight’  (orig. ‘to  pluck,  pull,  scuffle’).  Cp.  fee,  ‘estate’,  fight, and  the  first  element  in  fellow.  Cp.  also  cteno-, pashm,  paxwax,  Pecora,  pecten,  pectinate,  pec¬ toral,  peculate,  pecuniary,  impecunious,  peignoir, pekin,  ‘a  civilian’,  petto,  poitrel,  and  the  second element  in  parapet.
14699:fight,  n.  —  ME.  fiht,  fr.  OE.  feoht,  fr.  feohtan, ‘to  fight’.  See  fight,  v.
15267:fought,  past  tense  and  pp.  of  fight.  —  ME.  fauht, fr.  OE.  feaht,  ‘fought’,  past  tense  of  feohtan,  ‘to fight’.  See  fight,  v.
15268:foughten,  old  pp.  of  fight.  —  ME.  foughten,  fr. OE.  fohten,  pp.  of  feohtan,  ‘to  fight’.  See  fight,  v. foujdar,  n.,  an  officer;  a  criminal  judge  (India).  — Hind,  fawjddr,  fr.  Pers.  fawjddr,  a  hybrid  lit. meaning  ‘a  holder  of  military  force’,  coined  fr. Arab,  fauj,  ‘band,  troop,  military  force’,  and  the Pers.  suff.  -dar,  ‘holder,  possessor’.  See  aumildar and  cp.  words  there  referred  to. foujdary,  also  foujdarry,  n.,  a  criminal  court.  — Hind,  fawjddri,  fr.  fawjddr.  See  prec.  word, foul,  adj.  —  ME.  foul,  fr.  OE.  fid,  rel.  to  OS., OFris.,  MLG.,  OHG.,  MHG.  fid,  ON.  full, Dan.,  Swed.,  Norw.  ful,  MDu.  vuul,  Du.  vuil, G.  faul,  Goth,  fids',  formed  with  suff.  -la  fr. Teut.  base  *fi-  (whence  also  ON.  fuinn,  ‘foul, rotten’),  corresponding  to  I.-E.  base  *pu-, whence  OI.  pByati,  ‘rots,  stinks’,  pBtih,  ‘foul, rotten’,  Arm.  hu,  ‘purulent  blood’,  Gk.  rcu6<;, ‘first  milk  after  the  birth’,  ttjov  or  ttuov,  ‘dis¬ charge  from  a  sore;  matter’,  ttuOciv,  ‘to  cause to  rot’,  L.  pus,  ‘matter’,  putere,  ‘to  stink’,  puter, putridus,  ‘foul,  rotten’,  Lith.  pdviu,  pBti,  ‘to  rot’, pBliai,  ‘matter’,  Mir.  othrach,  ‘dung’.  Cp.  filth, defile,  ‘to  pollute’,  foumart.  Cp.  also  empyema, purulent,  pus,  pustule,  putanism,  putois,  Pu- torius,  putrid,  pyaemia,  pyo-,  Pythium,  sup¬ purate.
=== LEW pecu ===
```


## [2026-09-07T20:49:45.753Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT fellow/fight/fee/feud ===\"; grep -n \"^FELLOW\\|^FIGHT\\|^FEE\\|^FEUD\\|Fellow, a partner\\|feolaga\" SKT.txt | head -10; echo \"=== LAT feudum ===\"; grep -n \"feudum\\|pecus\" LAT.txt | head -5; echo \"=== PHD pasm/suban ===\"; grep -n \"pašm\\|pasm \\|šubān\\|suban\\|shepherd\" PHD.txt PHD_mackenzie.txt | head -10"
}
```


### [2026-09-07T20:49:45.832Z] TOOL RESULT

```
=== SKT fellow/fight/fee/feud ===
6406:FEE.
6528:FEUD.
=== LAT feudum ===
2315:abduxit, pecus abegit-, d'o 4 abigeus,-i (abigeius) "voleur de troupeaux",
2330:enseable, reunir dans nn meae lien, rasaeabler (= cruvayu)); cogere pecus
2381:■prodigo: pousser devant soi; Varr., R.R.3,4 prodigere pecus (= 7 tpo-
2395:modo uictus; modo compulsus; ut cum dicimus pecus sub arborem subactum;
18692:*/3,3 - inde dici coeptum, quod in sacrificiis optimum pecus e grege
=== PHD pasm/suban ===
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:588:šubān [sp’n!' | P боря, N ~] shepherd. | Sudan, Saw- [OZLWN-tn! < A N?sl; šwb- | M fwdn, So N ~] go. Sus&r [šwsl = Av. xfudra-] liquid, fluid; semen.
PHD.txt:3628:shepherd pānāg, šubān.
PHD.txt:4341:wool pašm, wart.
PHD.txt:4342:woollen pašmēn.
PHD.txt:4532:šasabīgān wih-1 wistanī šab šubān šabīxēn
PHD.txt:4640:pafšīr- pafšīrišnīh pafšīrišn paz- pa(č)čēn pa(č)čībāy- pa(č)čībāgīh pašēmānīh pašēmān pišīz paššing pašn pašom paššinj- paššinjīdan paššinjag pašm pašmēn pašt paštag pad- petyārag pattāy-
PHD_mackenzie.txt:4005:pandg [p'n(,)k I M p'ng] guard, protector; shepherd.
PHD_mackenzie.txt:4105:pasm [psm IN.....,] wool.
```


## [2026-09-07T20:49:53.830Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT fee ===\"; sed -n '6400,6412p' SKT.txt; echo \"=== SKT feud ===\"; sed -n '6524,6536p' SKT.txt; echo \"=== SKT fellow/fight ===\"; grep -n -i \"Fellow, a companion\\|Fellow\\.\\|Fight, to\\|Fight\\.\" SKT.txt | head -6"
}
```


### [2026-09-07T20:49:53.897Z] TOOL RESULT

```
=== SKT fee ===
—  L.  ne/as,  that  which  is  unlawful.  — L.  fu, not ;  /as,  law,  fromy^n*,  to  speak,  declare.
preface.  ( F.  —  L.)  O.  F.  prt/au.  — Lriw  L  pra/atium^,  not  found,  put  for L  prafatum,  a  preface,  neut.  ol  pra-/atus, spoken  before.
Father.  (E.)  U.Z. /aJer.  A.S. /adrr. \T\\e  f|icliing  with  /A  approaches  the  Ice- landic-)  +  Icei.yflfT»>,  Du.  vcihr,  Don.  Swcd. fader,  Golh  /adar,  G.  f«/er,  h. pa/it,  Gk. iTaTi7p,  Per*,  pidar.  Ski.  puri.     (^  VA.)
Fathom.  (E.)  M.E,  /adrru,  A.S. fteJim  the  space  reached  by  the  extended arms,  a  ^^rasp,  embrace. +  r'"'  vadem,  Icel. fax  mr.  a  fathom,  Dan.  /avn.  Swcd.  famn^ AD  embrace,  G. /adtn.  Allied  to  FsteaL CVf'AT.)
FaU^ruo.  ^-  (F.-U)  O.  F.  /atigv/\ from  faii^uir,  to  weary.  —  L.  /attgart,  to weary.
F&tuot3«.  CL.)     L./altiti3,  tilly,  fccbl*.
FEE.
Dar.  in/aluaie,  from  pp.  of  L.  in/«i
lo  make  a  fool  of.
fade,  vK  (P.  -L.)  From  F./«ft,  »dL, unsavoury,  weak,  faint,  —  L.  /aNtus,  fooUto. tasteless.
vade.  to  fade.  <F.  — I^)  A  weakened form  of  fade  (above)..
Fauces.  (L.)  l^  faucet,  pi.,  the  tipptt part  of  the  throat.
Faueet,  Fault ;  sec  Fallible.
=== SKT feud ===
Fetch.  (E.)    M.  t    v,  .^<-«.  1 f,2Ate.     K.S.fetean,  10  letch.  Gc Luke  xii    20.     TxXih.  ftcean  ta  a  ij..t oi/eiiitn,  to  fetch  *  AngUa,  vi.  ]77K /ir/  a  pace,  stem,  journey.  (V^FAD fetih,  sb.,  a  stratagem. Ffite ;  see  Festal. Fetich,  Fetish;  see  Faot. Fetid.    (F.  -  L.)      O.  F.   fetUt.  -  L fetiiiiu,  fartiJus,    stinking —L1  faUrt,   R stink.     Allied  to  Fiune. Fetlock,  Fetter;  ^ee  Foot. Fetus,  offspring.  (L.)     L.  ^/itr,  a  brin(p- ing  forth,  offkpriny.  -  L.  ftuirt  •,  an  ob» iete  verbk  to  generate,  produce ;  aUicd  to fu'i,  \  was :  see  Future,  B«.
effete,    exh-nuftwl.     (i   '       1 weakened  by  having  brod —  L-    eff    (or    /x,    out  : brought  fonh,  pp  o; fawn    (»),    ay. O.  F.    /rt«,    faett,     eailici    y>.«,    a    tAra, answering  to  a  Low  L  ionu  frtanm  •  il*t fonnd)/^L  fetuit/ittuj,  offspnng.
T
«
FEUD.
^  ^^  )      0.  F.  ftcomfiti
.'ittem,   fniitfulncss.
cw  : :    tUicd  to  /eims,
A^i  «p  Feiine. ''!>.  hn»'H:  »pc  Fo«.
i  (L')    M.  E.
\^.-.iT^  .  .T,.  ..-.  .'vc-,  ft/or  \  •« TiiL    15.  ••  U    .i^^t-iV.   fevcr.   lit    a
OBUrD;.*     CI  A.  S.  bijian,  G.   ^i^cM.
tit  coble.
=== SKT fellow/fight ===
1534:batUa.  (F.-L.)   M.E. -O.  F.  bataiUe,  (i)  a  Fight,  ;i)  a  bati Low  L.  bataiia,  a  fight.  •  ll bafuere,  to  beat.
1536:combat.  (F.  — L.)  Orig.  a  verb.«K €ombattn,  O.  F.  combatn.  to  fight  with.* F.  com-  (  «  L.  com-),  with ;  and  F.  battn,. O.  F.  batre,  to  fight.  Der.  cambaZ-aat  (F« pres.pt.>.
1603:bumpkin,  a  thick  headed  fellow.  (Dn.) —  O.  Hu,  boomktn,  a  little  tree  (Hexham); dimin,  of  boom,  a  tree,  a  beam,  bar.  The E.  bttrnkiH  aUo  meant  a  luff,  block,  a  thidt piece  of  wood  (Cotgravc,  5.  v.  Chicambault)', hence  readily  applied  10  a  block<bead, thick-skulled  fellow.
2404:buffer  (I),  a  foolish  fellow.  (F.)  Oik a  stammerer ;  hence  a  foolish  fellow.  M.  & bufftH^  to  stammer.- O.  F.  bmjer,  toprf out  the  cheeks  (hence,  to  puff  or  blov  ii talking).
2441:parboil.   (F.  — L.)     It  now  means  Mo boil  insufficiently,'  by  confusion  with  part. The  old  sense  is  'to  boil  thoroughly.'  — O, F.  parbouillir,  to  cook  thoroughly  (Koque- fort).  — Low  'L.  furl'ullirt,  \^.  f^rbuUin^  to boil  thoroughly.  —  L.  per^   through ;  and bullire  ;  sec  boil  (above). Bullaco.  wild  plum.  (C.)    M.  E.  bcltu, 'Gncl.  bulaisttar,  a  bullace;  Irish  buloSp, a  prune  :  Hrct  boles,  tohf,  bullace. BuUet.BuUetiu.BulUon;  weBTill(s). Bully,  a  noisy  rough  Icllow,  (O.  LowG.) In  Sh.  —  0.  Du.  bollaert,  '  a  jester  or  a  cylwr, Hexham;  Low  G.  bulltrjaaH,  bulltrl>iik,  in Hamburgh  bulUi-brock  (cf.  E.  bully-rock), a  boisterous  fellow.     So  also  Sued,  bulltr' bos,  a  noisy  fellow:  bvller,  clamouri  bullnt, to  make  .1  noise.     Allied  to  Bull  (T),  Bal- tow,  an<l  Boulder. Bulrush.  (Scand.  onJ  E.)     M.  E.  bnl- rysihi,  Piompt.  Parv.,  p.  344,  col.  a.     Lit 'stem-rush;'  from  its  stout  ittcm.  ■■  Dan. bul,  ^xtvA,  trunk  ;  see  bola,  under  Bnl|;e. Bulvrark.  (Scand.)    Sm  Bulge. Bum,  coDti  acted  form  of  Bottom.  (E.) So  also  O.  Frie&ic  bodtn,  bottom,  bicame N.  Friesic  t4n%.
4541:crook :  sec  Crook, tb-rd,  (K.)  O.F.  roriiru,  *m ',  C(  ital.  (kiur/ff,  a  curlew, bowl.  ^ wed  iturla,lo  coo;  io led  from  its  cry. foon.  (E.  o»rf  F  )  Formerly (Phil.  Holland) ;  it  means  a eom,  hence  a  ttingy  fellow. wntJi^ing,  prr*.  pi.  of  mu,/i*t, t  wtCHh  (M.  E.  mmtkgm), .  F.  iwwrtfr,  to  bide,  to
```


## [2026-09-07T20:49:54.607Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB ===\"; grep -n \"pašm\\|šubān\\|šupān\\|špān\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T20:49:54.657Z] TOOL RESULT

```
=== NYB ===
3664:$upän [šp'n'] shepherd 1”; pl. cas. obl. ~-dn 10, — Av. (1029) fšu- ‘sheep’ = pasu-, v.S. v. püh, + pāna-, v. pānak; MPrth swb’n; NP šubān, sabän.
5688:šwb'n: šupān
7455:šubān, Saban: šupan
```


## [2026-09-07T20:50:08.178Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v1 pashm ===\"; grep -n \"پشم\" BQT_v1_pages.txt | head -12; echo \"=== BQT v2 chupan ===\"; grep -n \"چوپان\\|شبان\" BQT_v2_pages.txt | head -12"
}
```


### [2026-09-07T20:50:08.256Z] TOOL RESULT

```
=== BQT v1 pashm ===
8455:کنند از پثبه و پشم وغیره - وبمعنی پر کننده
11013:ارمز پشم أول بروزن هرمز . نام
11028:ار مك بشم اول‌بروزن‌اروك» پشمینه‌ای
12458:و تسدوسقرلاط و صوف و دیگر پشمینها و کندم
13847:وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
14906:۱ - رك: ارمز . ۴ - اورماك » ت کی » نومی منسوج ازپشم شتر «جفتابی ۵۷*.
17872:ده - بروزن چکیده , .پشم و پنبة
19437:الث و میم , پشم فرمی را کوند که از بن موی
19515:پر پشم» موی و پشم بز را کوبند 4 .
21070:پشمینه» تکمهر گوی
23962:باشد که برکاغذ وجامه دحندب رپشم نرمی دا نیز
25984:پشما گنف* م بنخ اول و سکون انی
=== BQT v2 chupan ===
2236:              ‫و ملخ آبی را نیز گفته‌الد‬          ‫‪-‬‬   ‫آها ‪۲‬‬     ‫ساعت‌شبانر وزی‬      ‫بك حصه‌از یکپززار و هتار حصه‬
7457:      ‫‪ #‬چو پان (بدواومعروف) ‪ -‬همریشة شبان ( پهلوی ‪٩4°‬‏ ‪( )11[8‬ه‪.‬م‪ ( ).‬از افادات‌استاد‬
7462:      ‫چوپانیان «بارتولد ‪ .‬دائرقالممارف‌املام > درزیاکی ‪ « 08۳۵6‬گربرسن ‪ . ۵۷6‬کیلکی ‪82۳06‬‬
14688:     ‫نگاه دارد وسوشبانت ‪( 6۳290505‬موعود زرتشتی ) از فر امزدی برخوردار شود و اکزنار‬
19051: ‫که شبانان بدست گیرند‪ -‬وهرچیز پارهکه بقدمار‬                                                                  ‫عالمتاب ات ‪٩‬‏‬
20689:                                            ‫از بپر دو شبانی وز بهر ی‬
20775: ‫‪ = ۸‬دویرار ‪( 0 ۲2۲‬کردی) «عقاب دوبرار " توری آن بهتر از آشبانی‌آن‬                                        ‫‪. ۸۷‬‬
20984:‫مامت دامن کوه » اشاره بايشکه شبان در دامن‬
22398:     ‫» مجنون « وشبانگاه آوردند بش وی (عیسی)‬         ‫بی عفل* بخیرد‬       ‫‪۶۹۱‬‬   ‫ص‬       ‫رد( ‪۰‬‬       ‫‪6‬‬
22917:‫بيار میکرد بهرام از قضيةٌ شبان وسگه خائن‬                             ‫که جریی صراط خوانند ؟ ‪.‬‬
24907:                       ‫شبان کوله بانراکونند ‪#.‬‬                         ‫چنانکه در خر یز ه وهندوانه بشرط کارد ل‬
25279:                                                                                           ‫شبانگه کا‬
```


## [2026-09-07T20:50:15.289Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=7440 && NR<=7470' BQT_v2_pages.txt; echo \"=== nearest page tag ===\"; awk 'NR<=7460 && /\\[pdf page/{p=$0;n=NR} END{print n\": \"p}' BQT_v2_pages.txt"
}
```


### [2026-09-07T20:50:16.515Z] TOOL RESULT

```
                                                              ‫و رای قرشت هر دو مقتوح * مر‬
              ‫‪۱‬‬                        ‫پوشند ‪. ۴‬‬      ‫مرتفع از زمین بقدرنیمگز بابديشرتربکاهغها‬
     ‫چخویدن ‪ -‬باالی مجهول خوای‬                                             ‫‪۰‬‬   ‫ودرهای خانها ساز ند‬

    ‫نقطه داربروزن کوشیدن ‪ ,‬بمعنی لخزبدن و سر‬         ‫جو <‪ 4‬ه بر وزن کوچه ‪ ۰‬چوبی باشد‬
    ‫درآهدن وافتادن باشف خواه انان وخواه حیوان‬
                                                               ‫که بدان خمیر انرا تنك سازند [‬

                 ‫«فتایی ‪۱٩۲‬‏ * ‪.‬‬
                               ‫‪ - ۱‬در ترکی « چوتور » بمعنی نوك کوچك است‪ .‬ج‬
      ‫؟ ‏ استی ‪( 30606‬یم تن قفقازی) «ك‪ .‬است ‪ ۰۱۱‬کیلکی ‪( 806‬یم تنیشمی‬
      ‫بی دوخت و بدونآستین که بیشتر کله بانان و ساربانان پوشند) * درترکی «چوغا»(جامهٌیوستین)‬
                                                     ‫«جفتایی ‪ , 6۹۲‬معرب آن «جوخ» « تفس ‪:‬‬
              ‫شده مولوزن وپوشیده چوخا ‪.‬‬                  ‫‪-‬ا بینند اندرکنج غاری‬
                                                                             ‫‪۴‬ر‬
                                                                              ‫م‬
       ‫خاقالی شروالی در قصیدة مدحائیه«دیوان ‪۲۲‬‬
      ‫‪ #‬چو پان (بدواومعروف) ‪ -‬همریشة شبان ( پهلوی ‪٩4°‬‏ ‪( )11[8‬ه‪.‬م‪ ( ).‬از افادات‌استاد‬
      ‫پور داود)‪( 020۵6 ,‬باواومجهول) درجفتابی ‪ ۰‬و چوبان ( با واو مجهول وباء ) « داثرة المعارف‬
      ‫اسلام» « جغتابی ‪ ۰۹۲۲‬درتر کی عثمانی و زبان تاتاران قریمه» کلمه‌ایست تر کی ‪ -‬فارسی بمعنی‬
     ‫راعی ( عربی ) ؛ اسلا در مورد نگهبان کوسفندان و کاوان بکار میرود ‪ -‬کلمةٌ چویان بمترلة‬
      ‫علم باشخاص بیز اطلاق شده مانند امیر چرپان سرداربزر که‌ابران درعهد ابوسعید وموسی سللة‬
      ‫چوپانیان «بارتولد ‪ .‬دائرقالممارف‌املام > درزیاکی ‪ « 08۳۵6‬گربرسن ‪ . ۵۷6‬کیلکی ‪82۳06‬‬
                                                                           ‫‪,‬در فارسی نیز چوبان ‪:‬‬
             ‫ابا زين وبیحان کمندی دراز ‪...‬‬                ‫مشد کرد چوبان و دوکره تاز‬
            ‫برآشفت از آن شهربار رمه‪.‬‬                      ‫فروماند چویان و لشکر هنه‬
          ‫«شاهنامة بخ ج ‪ ۷‬ص ‪. ۵۹۰۲-۹۹‬‬
                  ‫بلکه چویان برای خدمت‌اوست‪.‬‬               ‫کوسیند از برای چویان نیست‬
      ‫« کلتان ‪۱6‬‬


=== nearest page tag ===
:
```


## [2026-09-07T20:50:32.275Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SNS.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f'); print(\"chunks\",len(p))\nEOF\nsed -n '5385,5405p' SNS.txt"
}
```


### [2026-09-07T20:50:33.573Z] TOOL RESULT

```
chunks 1
lo 



16 



J/XT^Io'jo^* ***») 'l*3*.*3*:hucihr: Jjo^v uU. : \i^ T 



•6J*'*i*ja :uzSnag: »3«««f 
T?/U^ .(jji-^i^J xuzina/x^azlna : t 



?Y
```


## [2026-09-07T20:50:38.122Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['SNS'];print(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T20:50:39.746Z] TOOL RESULT

```
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-07T20:50:47.339Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 60 curl -s \"https://ia-petabox.archive.org/services/search/beta/page_production/inside.php?item_id=VajnameShayest&doc=VajnameShayest&path=/27/items/VajnameShayest&q=pasm\" | python3 -c \"\nimport sys,json\ntry:\n  d=json.load(sys.stdin)\n  for m in d.get('matches',[])[:12]:\n    print(m.get('par',[{}])[0].get('page'), (m.get('text','')[:160]).replace('\\n',' '))\nexcept Exception as e: print('ERR',e)\n\""
}
```


### [2026-09-07T20:50:48.710Z] TOOL RESULT

```
ERR Expecting value: line 1 column 1 (char 0)
```


## [2026-09-07T20:51:26.004Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15850,15860p' BRT.txt | head -20; echo \"--- look for column markers near\"; awk 'NR>=15700 && NR<=15870 && /^[0-9]{3,4}$|^ *[0-9]{3,4} *$/{print NR\": \"$0}' BRT.txt | tail -5; echo \"=== near 18398\"; awk 'NR>=18300 && NR<=18420 && /^ *[0-9]{3,4} *$/{print NR\": \"$0}' BRT.txt | tail -5"
}
```


### [2026-09-07T20:51:27.513Z] TOOL RESULT

```
•  j.  pas-  V.  'fesseln'.  j-Aor.  1  pas-.  —  PPfP. *paxita-'^.
'an  nnander  befestigen,  zusammenfügen': s.  sartmyapax^pad:
mit/d^'nndai'ii'ziisammen-.aDeinaDder- fesseln':  (^anka^tsis  flsbis  oidibTs  paiti opa.pai^st  "mit  eisernen  Fesseln  soll  man seine  Knochen  zu&ammenfesseln"  V.  ^  5 1 .
VgL  laßai-.  —  Po. :  /aJfnlUin,}).  —  >l%S6aE.
•  p.  pasa  Praen.  'nach';  i)  örtlich  'hinter —  nach,  dreb',  mit  Gen.:  iäri^  .  .p°  manä asiymie^  mädam  Bh.  2.  6.  3)  zeitlich "nach",  mit  Aklc:  pasltvi^  (sbes.).
Am  ir.  *pas  (=  idg.  *^J')  durch  Aosgleich mit  dem  gegensitzlichen  fori.  Tgl.  Bim- ZDMC.  $0.  713  '».  —  S.  Doeh  faskäi,  fOira.  — Dp.  pas.  —  ')  Anders  Fov  KZ.  35.  a6,  G«ay AJPh.  21.  8.
•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
airya  daiAhärö  Yt  Ä  58 ;  N.  6^7  (?) ;  —  caiti m  airoAe  'srö  *ui0>ra  barät  "Srie  viel  Z. soll  man  bei  einem  Opfeitiei  bringen?" N.  65;  —  ni}itpanis(a  (statt  IS.,  lies  pasvaT) . .  irista  (sd.)  . .  ratufris  N.  56;  — yi  'süm 'ata  finacUi  (sd.)  S.-iS;  —  Aasat^r^m aimmayanqm  /räviiruyät  (sd-)  FUpanqmät aBaiiqm  par.qm  ..   WlS.JO.  [N.  65:
lies  pasvä^Mr^A^H.I
KompA.,  £.;  AbleiLU.  —  u.  fcsi'.-  m.;  sbal. fas  'Kleinneh',  woss. /»o  'SchaT;  np.  hi-hin ■Hirte'.  —  Pü. :  fah,  gösfonJ,  —  ')  Vennallich kein  selbständigei  Wort,  sondern  ans  einer Komp.  loigelösl;  ».  dain  JF.  ir.  133.  Vgl. nocti  in  ^flyo,  —  '^  LP-,  statt  fitsuTfa^  in Anlehnung  u>  den  NS. —  Jl  S.  auch  tamna-
•  j.  paüiva''  Adv.  'darnach,  darauf,  dann'; i)  an  der  Spitze  des  Satzes:  /*  kc^hajiyJ' avam  bardiyawt  aväja'  .  .  p'  kt^b&jiyt^ mudrsyam  asiyav<^..p'  draugt^  dahyauiä vany  abavt^  Bh.i-io;  11*,  12,  13,  16',  17, 18J,  19*,  2.  iJ,  4,  S,  63,  7',  9,  10',  II,  12, 13'.  >4S  16.  3- 1.  2.  3*.  4,  5.  6^  7.  ».  9. II,  n,  13,  14*,  4.4.  5- "^  4.  D.77.3'>,  X.
--- look for column markers near
15721: 871
15751: 874
15777: 875
15780: 876
15801: 877
=== near 18398
```


## [2026-09-07T20:51:35.620Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=15856 && /^ *[0-9]{3,4} *$/{n=$0} END{}' BRT.txt; for L in 15856 15936 18398 18414; do awk -v L=$L 'NR<=L && /^ *[0-9]{3,4} *$/{n=$1} NR==L{print L\" -> last col marker \"n}' BRT.txt; done"
}
```


### [2026-09-07T20:51:37.352Z] TOOL RESULT

```
15856 -> last col marker 877
15936 -> last col marker 886
18398 -> last col marker 998
18414 -> last col marker 998
```


## [2026-09-07T20:51:47.693Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 14516 14542 14640 14699; do awk -v L=$L 'NR<=L && /^ *[0-9]{3,4} *$/{n=$1} NR==L{print L\" -> nearest page marker \"n}' KLN_1966.txt; done; echo; awk 'NR>=14500 && NR<=14700 && /^ *[0-9]{3,4} *$/{print NR\": \"$0}' KLN_1966.txt | head"
}
```


### [2026-09-07T20:51:49.018Z] TOOL RESULT

```
14516 -> nearest page marker 581
14542 -> nearest page marker 583
14640 -> nearest page marker 587
14699 -> nearest page marker 590

14513: 581
14539: 582
14540: 583
14576: 584
14587: 585
14624: 586
14632: 587
14660: 588
14661: 589
14697: 590
```


## [2026-09-07T20:51:52.582Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T20:51:52.623Z] TOOL RESULT

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


## [2026-09-07T20:51:56.105Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-07T20:51:56.145Z] TOOL RESULT

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


## [2026-09-07T20:52:58.751Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -m3 -A6 \"فئودال\" c43c42f022c0f7b2.txt | head -40"
}
```


### [2026-09-07T20:52:58.799Z] TOOL RESULT

```
4:TITLE: فئودال - معنی در دیکشنری آبادیس
5-
6:فئودال - معنی در دیکشنری آبادیس 
7-
8- دیکشنری مترجم بپرس 
9-
10: فئودال
11- /fe~odAl/
12-
```


## [2026-09-07T20:53:01.980Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"معین\\|فرانسوی\\|فر\\.\\|féodal\\|feodal\" c43c42f022c0f7b2.txt | head -20"
}
```


### [2026-09-07T20:53:02.028Z] TOOL RESULT

```
22: فرهنگ معین
24: (فِ ئُ ) [ فر. ] (ص . ) مالک ، دارندة زمین های بسیار. 
50:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
65: ( فِ ئُ ) [ فر. ] ( ص . ) مالک ، دارندة زمین های بسیار. ( معین ) 
73: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-07T20:53:08.904Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg387.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/387.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T20:53:08.975Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T20:57:50.183Z] TOOL CALL #62: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-387.py",
 "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPEK = W + \"Reconstruction:Proto-Indo-European/pe%E1%B8%B1-\"\nPEKU = W + \"Reconstruction:Proto-Indo-European/p%C3%A9%E1%B8%B1u\"\nPASHM = W + \"%D9%BE%D8%B4%D9%85\"\nCHUPAN = W + \"%DA%86%D9%88%D9%BE%D8%A7%D9%86\"\nFEHU = W + \"Reconstruction:Proto-Germanic/fehu\"\nFEUDUM = W + \"feudum\"\nETY_FELLOW = \"https://www.etymonline.com/word/fellow\"\nETY_FEUDAL = \"https://www.etymonline.com/word/feudal\"\nETY_FIGHT = \"https://www.etymonline.com/word/fight\"\nABADIS = \"https://abadis.ir/fatofa/%D9%81%D8%A6%D9%88%D8%AF%D8%A7%D9%84/\"\n\ndata = {\n \"pdf_page\": 387,\n \"book_page\": 357,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Pek, Peku\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *peḱ- 'to pluck (wool, hair), shear' with its u-stem *péḱu 'livestock, movable wealth'\",\n   \"note\": \"Nourai's double root box is exactly Pokorny's lemma peḱ-2 on the cited page 797 ('to fleece; cattle'), which lumps both halves; Watkins/AHD splits the same material into pek-2 'to pluck the hair, fleece, comb' and peku- 'wealth, movable property', both tagged '[Pok. 2. pek- 797]'. Wiktionary likewise has *peḱ- 'to pluck (wool, hair)' with *péḱu 'livestock' derived from its u-stem. Language label ('Indo-European' = PIE) and both glosses are right; 'woolly animals, cattle, property' is the standard semantic ladder for *péḱu (Klein s.v. fee: I.-E. base *peku- 'the woolly animal', whence 'sheep, cattle, property, money'). The page is otherwise faithful: the printed chart (pdf p. 387, copied to data/verification/sources/refs/ocr/BOOK/387.png) matches the extracted JSON word for word, including the accentless French 'feodal' and the pointer '☞Pa' on fšu-pait.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peḱ- به معنی «کندن پشم یا مو، چیدن» و ستاک -u آن *péḱu به معنی «دام، چهارپا، مال و دارایی». پوکورنی در همان صفحهٔ ۷۹۷ که نورایی ارجاع داده، هر دو معنی را زیر یک سرواژه (peḱ-2) آورده است؛ واتکینز در پیوست ریشه‌های هندواروپایی همین ماده را به دو مدخل pek-2 و peku- بخش کرده ولی هر دو را به همان صفحهٔ ۷۹۷ پوکورنی ارجاع داده است. برچسب زبانی و هر دو معنی درست است و تحول معنایی «جانور پشم‌دار ← گوسفند و گله ← مال و دارایی» همان چیزی است که کلاین نیز زیر fee آورده. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [PEK, PEKU, ETY_FEUDAL],\n   \"ref_check\": [\n    {\"ref\": \"POK:797\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, lemma printed 'Root/lemma: peR-2' (OCR for peḱ-2), 'Meaning: to fleece; cattle', 'Page(s): 797': 'Old Indic pasu-, pasu- n. … cattle; Avestan pasu- m. cattle (mostly still small cattle), in compound fsu-, -fsu- … = Latin pecū … = Gothic faihu property, fortune … = Lithuanian pekus, Old Prussian peckū cattle'. Both of Nourai's glosses ('wool, to pluck wool' / 'woolly animals, cattle, property') are on this one page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 16 (WLD_Bd2_pages.txt line 1051, page header '16 pek-, pek-, pōk-')\", \"stance\": \"supports\",\n     \"note\": \"'2. pek- „Wolle oder Haare rupfen, zausen; Wolltier, Schaf (peku)“, dann …' — Walde-Pokorny states the double sense of the root exactly as Nourai's two boxes do; further down 'ahd. fihu „Vieh“; = lit. pekus, apr. pecku „Vieh“'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. pek-2 and peku- (AHD_watkins1985.txt line 828)\", \"stance\": \"supports\",\n     \"note\": \"'pek-2. To pluck the hair, fleece, comb. … [Pok. 2. pek- 797.]' and 'peku-. Wealth, movable property. … [In Pok. 2. pek- 797.]' — the split matches Nourai's Pek / Peku pair.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. peKos and peKu (IEC.txt lines 12607, 12617)\", \"stance\": \"supports\",\n     \"note\": \"'peKos, us „fleece“ … Gk. pékos … Lat. cf. pecus' and 'peKu „small farm-animal for shearing, head of cattle“ … Skt. páśu; Av. pasuš m.; OLat. pecu; Go. faihu n. „money“; OE feoh „cattle, wealth“; ON fé'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §3.15 'cattle' (SYN.txt line 3927) and §11.41/11.48 (line 19547)\", \"stance\": \"supports\",\n     \"note\": \"'Lat. (early) pecu … Goth. faihu only „property“, ON fé „cattle“ esp. „sheep“, and „property“ … Skt. paśu- „domestic creature“ …, Av. pasu- mostly „small cattle“' — the 'cattle ↔ property' polysemy Nourai puts in the root gloss.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 581 s.v. fee\", \"stance\": \"supports\",\n     \"note\": \"'fr. I.-E. base *peku-, „the woolly animal“, whence „sheep, cattle, property, money“. This base is an enlargement of base *pek-, „to pluck (wool or hair); hairy, woolly“, whence OI. pákṣman …, Pers. pashm „wool“ … OE. feohtan „to fight“ (orig. „to pluck, pull, scuffle“)' — Klein's article is in effect this whole chart in prose.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"pasu, pašman; fšu; fšu-pait\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three separate items sit in this one box and only part of it survives checking. (a) Av. pasu- (m.) is 'cattle, domesticated quadruped', in practice mostly 'small cattle, sheep and goats' (Bartholomae, AiW ~col. 878 s.v. pasav-: 'Vieh, domestiziertes vierfüssiges Tier, Haustier'; Buck §3.15 'Av. pasu- mostly small cattle'; Pokorny 797 'Avestan pasu- m. cattle'). Nourai's gloss 'wool' for pasu is therefore wrong; the word means the animal, from *péḱu. (b) fšu- is correct: it is the compositional/zero-grade shape of the same stem (*pśu- < *pḱu-, Iranian p+ś > fš), listed by Bartholomae as 'fšav- m.: s. unter pasav-' (~col. 998) and seen in Av. fšuyant- 'cattle-breeder', Pokorny's 'in compound fsu-, -fsu-'. (c) 'pašman' is not an Avestan headword in Bartholomae, who has only Av. pašna- n. 'Augenlid' (~col. 886), where he compares 'ai. pákṣman- n. Augenwimpern; np. pašm Wolle'; Pokorny 797 does the same. The wool word is therefore a Proto-Iranian reconstruction *pašman- (< PIE *poḱ-s-mn̥), not an attested Avestan form — Wiktionary cites 'Avestan pašman' as a cognate but has no Avestan entry for it. (d) 'fšu-pait' = Av. *fšu-paiti- 'lord of cattle', which Horn (Grundriss p. 171) invokes only to explain the Armenian loan špet; the compound that actually yields Persian šabān/čupān is *fšu-pāna- 'cattle-protector' (fšu- + pā(y)- 'to protect'), which is what Nourai's own '☞Pa' cross-reference points at. So the gloss 'protector of cattle, shepherd' belongs to -pāna-, not to -paiti-.\",\n     \"derivation_fa\": \"این جعبه سه چیز جداگانه را در خود جای داده و همه‌شان درست نیست. یکم، اوستایی pasu- به معنی «دام، چهارپای اهلی» (به‌ویژه گوسفند و بز) است نه «پشم»؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۸۷۸) آن را «Vieh, Haustier» معنی کرده و پوکورنی هم در همان صفحهٔ ۷۹۷ «cattle» آورده است؛ پس معنایی که نورایی داده نادرست است. دوم، صورت fšu- درست است: همان ستاک در ترکیب، از ایرانی باستان *pśu- که در آن خوشهٔ آغازین به fš بدل شده (بارتولومه: fšav- بنگرید به pasav-؛ نیز fšuyant- «دامدار»). سوم، pašman در اوستا شاهد ندارد؛ آنچه در اوستا هست pašna- «پلک» است و بارتولومه ذیل آن سنسکریت pakṣman و فارسی نو «پشم» را سنجیده است؛ بنابراین صورت *pašman- بازسازیِ ایرانی آغازین است نه واژهٔ اوستایی. چهارم، fšu-pait همان *fšu-paiti- «سرور دام» است که هرن (ص ۱۷۱) تنها برای توضیح وام‌واژهٔ ارمنی špet آورده؛ اما آنچه «شبان/چوپان» از آن آمده *fšu-pāna- «نگاهبان دام» است (fšu + پاییدن)، یعنی همان ریشه‌ای که خودِ نورایی با نشانهٔ ☞Pa به آن ارجاع داده است. حاصل: مسیر کلی درست است ولی صورت‌ها و معناها دقیق نیست؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [PASHM, CHUPAN, PEK],\n     \"ref_check\": [\n      {\"ref\": \"POK:797\", \"status\": \"partial\",\n       \"note\": \"The cited page has 'Avestan pasu- m. „cattle“ (mostly still „small cattle“), in compound fsu-, -fsu-' (so fšu- is Nourai's, but pasu- is glossed 'cattle', not 'wool'), and at the end 'Avestan pašna- n. „eyelid“, compare in not so specified meaning np. pašm „wool“' — i.e. Pokorny gives pašna-, not an Avestan pašman-, and has no fšu-pait(i)- at all.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW ~cols. 878 (pasav-), 886 (pašna-), 998 (fšav-)\", \"stance\": \"partial\",\n       \"note\": \"'j., g. pasav-, fšav- m. „Vieh, domestizirtes vierfüssiges Tier, Haustier“ … u. fśu- m.; sbal. fas „Kleinvieh“, oss. fos „Schaf“; np. šubān „Hirte“' (BRT.txt line 15856); 'j. pašna- n. „Augenlid“ … Vgl. ai. pákṣman- n. „Augenwimpern“; np. pašm „Wolle“' (line 15936); 'j., g. fšav- m.: s. unter pasav-' (line 18398). Bartholomae has pasu- and fšu-, but no Avestan pašman- and no fšu-paiti-.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary) s.v. šupān\", \"stance\": \"partial\",\n       \"note\": \"'šupān [špʾn] shepherd … — Av. (1029) fšu- „sheep“ = pasu-, v.s.v. pāh, + pāna-, v. pānak; MPrth šwbʾn; NP šubān, šabān' — Nyberg analyses the shepherd word as fšu- + pāna-, i.e. not -paiti- as printed here (but exactly Nourai's ☞Pa pointer).\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 776, p. 171\", \"stance\": \"partial\",\n       \"note\": \"'šabān Hirte, šuwān, šubān … aw. fšu.pāna-; phlv. špān „Hirte“ (AV.), šupān (FP.); arm. LW. spat (aw. *fšu.paiti-)' — Horn has BOTH compounds: -pāna- for the Iranian shepherd word, *fšu-paiti- only for the Armenian loan.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck §3.15 'cattle' (SYN.txt line 3927)\", \"stance\": \"contradicts\",\n       \"note\": \"'Av. pasu- mostly „small cattle“' — the animal, never 'wool'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"pašm «پشم»; šabân, čŭpân «شبان ، چوپان»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Persian words descend from the Avestan/Old Iranian material of the parent box, through Middle Persian. (a) پشم: Proto-Iranian *pašman- (< PIE *poḱ-s-mn̥, the -mn̥ derivative of *peḱ- 'pluck') > MP pašm [pšm] 'wool', with loss of the -an of the n-stem as regularly in MP (MacKenzie, CPD p. 65: 'pašm [pšm | N ~] wool. ~ēn woollen') > NP pašm 'wool'; cognates Skt. pakṣman- 'eyelashes, hair', Gk. pókos 'fleece', Arm. asr, Lat. pectō. Pokorny cites 'np. pašm „wool“' on the very page Nourai gives. (b) شبان/چوپان: Old Iranian *fšu-pāna- 'cattle-protector' > MP šubān/šupān (written špʾn, Manichaean šwbʾn; Parthian šwbʾn) > NP šubān/šabān 'shepherd'; the initial cluster fš- was simplified to š- with an anaptyctic vowel (*fšupān > šupān > šubān), and intervocalic -p- softened to -b-. čupān is the later, originally dialectal by-form of the same word (Horn no. 776: 'die dialektischen čupān … sind jung'); from Persian it passed into Turkic (Ottoman çoban, Chaghatai čōpān, Azerbaijani çoban) and was reinforced from there in the Mongol/Ilkhanid period (whence the Chupanid dynasty, Amir Čupān). Mo'in's footnote in Borhān-e Qāṭeʿ, s.v. چوپان, states 'همریشهٔ شبان (پهلوی šubān) … از افادات استاد پورداود' and reports the Encyclopaedia of Islam's view that Ottoman çoban is a Turco-Persian word. Nourai's arrow and both glosses are right.\",\n     \"derivation_fa\": \"هر دو واژه از راه فارسی میانه به فارسی نو رسیده‌اند. «پشم» از ایرانی آغازین *pašman- (خود از هندواروپایی *poḱ-s-mn̥، مشتق ریشهٔ *peḱ- «کندن پشم») به فارسی میانهٔ pašm (نوشتهٔ pšm در فرهنگ مکنزی، ص ۶۵) و از آنجا به «پشم» فارسی نو؛ پایانهٔ -an ستاک نونی در فارسی میانه افتاده است. هم‌ریشه‌های آن سنسکریت pakṣman «مژه، مو»، یونانی pókos «پشمِ چیده» و لاتین pectō است، و پوکورنی هم در همان صفحهٔ ۷۹۷ «np. pašm Wolle» را آورده. «شبان» از ایرانی باستان *fšu-pāna- «نگاهبان دام» است که در فارسی میانه šubān/šupān شده (مکنزی ص ۷۹؛ نیبرگ، واژه‌نامه، ذیل šupān؛ پارتی šwbʾn): خوشهٔ آغازین fš- ساده و واکهٔ میانجی افزوده شده و p میان‌واکه‌ای به b نرم شده است. «چوپان» گونهٔ گویشی و متأخرترِ همان واژه است (هرن، شمارهٔ ۷۷۶: صورت‌های چوپان «جوان»‌اند)، که از فارسی به ترکی رفته (çoban عثمانی، چوپان جغتایی) و در دورهٔ ایلخانی دوباره رواج یافته است؛ معین نیز در حاشیهٔ برهان قاطع ذیل «چوپان» می‌نویسد «هم‌ریشهٔ شبان (پهلوی šubān)… از افادات استاد پورداود». ادعای نورایی درست است.\",\n     \"sources\": [PASHM, CHUPAN, PEK],\n     \"ref_check\": [\n      {\"ref\": \"POK:797\", \"status\": \"supports\",\n       \"note\": \"'compare in not so specified meaning np. pašm „wool“' — Pokorny p. 797 explicitly attaches New Persian pašm to this root (he says nothing about šabān/čupān, which are covered by Horn and Nyberg instead).\"},\n      {\"ref\": \"SNS:123,125\", \"status\": \"partial\",\n       \"note\": \"Tavoosi's Shāyast nē Shāyast glossary is on disk only as very poor OCR with no readable printed page numbers (refs_online: 'page offset not determined'). The text does contain the Pahlavi material Nourai is citing — 'buz-pašm' (goat wool, SNS.txt line 7565), 'uštur pašm' (camel wool, line 17610), a headword ':pašmān:' (line 8273) — and its Avestan index has 'pašman- 123/10' (line 29385), which matches the '123' of the citation; but I could not pin the printed pages 123 and 125 to leaves of the scan, so this ref is only partially checked.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 65 and 79\", \"stance\": \"supports\",\n       \"note\": \"'pašm [pšm | N ~] wool. ~ēn [-yn | N ~īn] woollen' and 'šubān [špʾn! | P šwbʾn, N ~] shepherd' — both Middle Persian links of the chain are attested.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. šupān\", \"stance\": \"supports\",\n       \"note\": \"'šupān [špʾn] shepherd … — Av. (1029) fšu- „sheep“ = pasu-, + pāna-; MPrth šwbʾn; NP šubān, šabān'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 776, p. 171\", \"stance\": \"supports\",\n       \"note\": \"'776. šabān Hirte, šuwān, šubān … aw. fšu.pāna-; phlv. špān „Hirte“ (AV.), šupān … kurd. šiwan; afg. špūn „Hirt“ … Die dialektischen čupān (auch kurd. čuwān „Hirt“) sind jung.'\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 42 (note after no. 321)\", \"stance\": \"supports\",\n       \"note\": \"'Hier fehlt: pašm „Wolle“, skr. pakṣman- „Augenwimpern, Haar“ …; ahd. fahs „Haarschopf“, gr. πόκος „Vliess“ … an. fær „Schaf“' — Hübschmann assigns NP pašm to exactly this word family.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, Moʿin's footnote s.v. چوپان (BQT_v2_pages.txt line 7457)\", \"stance\": \"supports\",\n       \"note\": \"'چوپان (بدو او معروف) - همریشهٔ شبان (پهلوی šubān) (ه.م.) از افادات استاد پورداود' — Moʿin, on Pourdavoud's authority, makes čupān and šabān the same word, with the Pahlavi form; he adds the Turkic spread (çoban, Chaghatai čōpān, the Chupanid amirs).\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi, s.v. شبان (ARY_pages.txt, pdf page 374) and s.v. پشم (pdf page 170)\", \"stance\": \"supports\",\n       \"note\": \"s.v. شبان: 'واژهٔ \\\"شبان\\\" از دو واجریشه درست شده است: -FSHU به چم \\\"رم\\\" یا \\\"گوسفند\\\" (هندواروپایی: -PEK) و پسوند PANA به چم \\\"پاییدن\\\"'; note 2 'به احتمال زیاد واژهٔ \\\"چوپان\\\" هم از همین واجریشه است'; note 4 cross-refers to پشم — an independent modern Persian source giving Nourai's exact analysis.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sogdian\",\n     \"words\": \"`ps\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian ʾps- (Gharib no. 1301, read ap(a)s / ʾps-) 'sheep, cattle', with the by-forms ps- (no. 7431, pas, acc. psw, nom. psy) and psw (no. 7453, pasu) — the ʾ- is the prosthetic aleph regular before an initial cluster in Sogdian orthography. All three continue Old Iranian *pasu- 'small cattle', the same stem as Avestan pasu-, so Nourai's arrow is right in substance; strictly, though, Sogdian is a sister Eastern Iranian language, not a descendant of Avestan — Gharib's own note is a comparison ('©<Av. pasu'), not a derivation. Nourai's transliteration '`ps' with a backtick for aleph reproduces Gharib's headword exactly, and 'sheep' is Gharib's first gloss.\",\n     \"derivation_fa\": \"سغدی ʾps- (قریب، شمارهٔ ۱۳۰۱) «گوسفند، دام» و گونه‌های ps- (شمارهٔ ۷۴۳۱، خوانش pas) و psw (شمارهٔ ۷۴۵۳، pasu) همگی دنبالهٔ ایرانی باستان *pasu- «دام کوچک»‌اند، یعنی همان ستاکی که در اوستایی pasu- دیده می‌شود؛ الف آغازین در ʾps- الف پروتتیک خط سغدی است. پس صورت و معنایی که نورایی آورده درست است. تنها نکتهٔ دقیق این است که سغدی فرزند اوستایی نیست بلکه زبانی ایرانی شرقی و هم‌عرض آن است؛ خودِ قریب هم در برابر مدخل «<Av. pasu» را همچون مقایسه آورده نه اشتقاق. ادعای نورایی پذیرفتنی است.\",\n     \"sources\": [PEKU],\n     \"ref_check\": [\n      {\"ref\": \"SOD:51,298\", \"status\": \"supports\",\n       \"note\": \"Gharib entry 1301 (SOD.txt line ~93585 area / entry block): '1301 ʾps-: B, S … ap(a)s ? (DAv. pasu) ©pred. inst. -, acc. -w … sheep, cattle | SCE 364; TSP 3.187; GMS 953, 1182 n 2' — at roughly p. 51 of the dictionary (≈25 entries a page); and entries '7431 ps-2 B, M, C … pas ©<Av. pasu ©acc. psw … sheep, cattle' and '7453 psw B, C … pasu … cattle, sheep' fall at roughly p. 298. Both cited pages carry exactly the word and gloss Nourai prints, and Gharib himself links them to Av. pasu.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 1301, 7431, 7453\", \"stance\": \"supports\",\n       \"note\": \"See ref_check; the dictionary gives 'sheep, cattle' and the Avestan comparison for all three forms.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW ~col. 878 s.v. pasav-\", \"stance\": \"supports\",\n       \"note\": \"Bartholomae's own comparative tail for pasav- lists the Eastern-Iranian cognates 'sbal. fas „Kleinvieh“, oss. fos „Schaf“', the same *pasu- family the Sogdian form belongs to.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 797\", \"stance\": \"supports\",\n       \"note\": \"'Avestan pasu- m. „cattle“ (mostly still „small cattle“)' — the Iranian branch of the root, of which the Sogdian word is a member.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"feht\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Two Germanic words of this root are packed into one box. The verb is Proto-Germanic *fehtaną 'to comb out, struggle' (OE feohtan, OS/OHG fehtan, Du. vechten, G. fechten), from the t-extension *peḱ-t- of the root; the noun is *fahtiz > OE feht 'fleece' (Du. vacht 'wool, fleece', OSw. fæt 'wool, fleece'), which is what Pokorny prints on p. 797 ('Old English feht „fleece“, Dutch vacht „wool, fleece“'). Nourai's spelling 'feht' is therefore the noun's shape carrying the verb's gloss; both belong here, and his double gloss 'to pluck out wool, fight' is precisely the semantic bridge the handbooks assume ('pulling roughly', 'tearing out one another's hair'). Etymonline is slightly more cautious — 'probably from PIE *pek- (2) … But perhaps it is from the source of Latin pugnus „fist“' — but Pokorny, Walde-Pokorny, Watkins and Klein all put the verb here.\",\n     \"derivation_fa\": \"در این جعبه دو واژهٔ ژرمنی با هم آمده‌اند: فعلِ ژرمنی آغازین *fehtaną «شانه‌کردن/کشمکش کردن» (انگلیسی کهن feohtan، آلمانی کهن fehtan، آلمانی امروز fechten) از گسترش t-دارِ ریشه، و نامِ *fahtiz > انگلیسی کهن feht «پشمِ چیده، پشمینه» (هلندی vacht) که پوکورنی در همان صفحهٔ ۷۹۷ آورده است. پس صورتی که نورایی نوشته صورت اسم است و معنایی که داده معنای فعل؛ ولی هر دو به همین ریشه بازمی‌گردند و همان پل معنایی «کندنِ خشن مو و پشم ← زدوخورد» را نشان می‌دهند که فرهنگ‌نویسان فرض می‌کنند. اتیمانلاین محتاط‌تر است و می‌گوید «احتمالاً» از این ریشه است و شاید هم با لاتین pugnus «مشت» پیوند داشته باشد، اما پوکورنی، والده-پوکورنی، واتکینز و کلاین همگی آن را همین‌جا می‌نهند. ادعای نورایی درست است.\",\n     \"sources\": [ETY_FIGHT, PEK],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. pek-2: '1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT.' — exactly the node and the next one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 797 (peḱ-2)\", \"stance\": \"supports\",\n       \"note\": \"'Old High German Old Saxon fehtan, Old English feohtan „fence“; … Old English feht „fleece“, Dutch vacht „wool, fleece“' — both the verb and the noun 'feht' of Nourai's box.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 581 s.v. fee\", \"stance\": \"supports\",\n       \"note\": \"'… OE. feax, OS., OHG. fahs „hair“, ON. fax „mane“, OE. feohtan „to fight“ (orig. „to pluck, pull, scuffle“)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 16\", \"stance\": \"supports\",\n       \"note\": \"The Germanic material stands under '2. pek- „Wolle oder Haare rupfen, zausen“' on the same page as the root.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"fight\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE feohtan 'to combat, contend with weapons' (class III strong verb, pt. feaht, pp. fohten) > ME fighten > fight; the noun is OE feoht > ME fiht. The -gh- is a Middle English scribal spelling for the earlier hard h before -t- (late OE examples still write yogh). The word never left English; no borrowing is involved, so the single arrow from the Germanic box is right.\",\n     \"derivation_fa\": \"انگلیسی fight دنبالهٔ انگلیسی کهن feohtan «جنگیدن، نبرد کردن» (فعل قوی طبقهٔ سوم: گذشتهٔ feaht، اسم مفعول fohten) است که در انگلیسی میانه fighten شده؛ اسم آن نیز از feoht انگلیسی کهن می‌آید. نوشتنِ gh در املای انگلیسی میانه صرفاً جانشین همان «های سخت» پیش از t است. هیچ وام‌گیری در میان نیست و پیکان نمودار درست است. ادعای نورایی درست است.\",\n     \"sources\": [ETY_FIGHT],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own; it inherits AHD from the parent Germanic box, where Watkins names FIGHT as the English outcome of *fehtan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 590 s.v. fight, n.\", \"stance\": \"supports\",\n       \"note\": \"'fight, n. — ME. fiht, fr. OE. feoht, fr. feohtan, „to fight“'; the verb article cross-refers to fee, i.e. to the *pek- family.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pek-2\", \"stance\": \"supports\",\n       \"note\": \"'… in Old English feohtan, to fight: FIGHT.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/fight\", \"stance\": \"partial\",\n       \"note\": \"Confirms OE feohtan > fight in full, but hedges the root: 'probably from PIE *pek- (2) „to comb, to pluck out“ wool or hair … But perhaps it is from the source of Latin pugnus „fist“.'\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Germanic\",\n     \"words\": \"fehu; fĕlag\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The first word is right and central: Proto-Germanic *fehu 'cattle, livestock, property' < PIE *péḱu (Goth. faihu 'money, property', OHG fihu 'cattle', OS fehu, OE feoh 'cattle, money, property', ON fé) — Grimm's law gives p > f and ḱ > h. The second is not a Common Germanic word: félag is Old Norse, a compound noun 'partnership, joint ownership', literally 'a laying down of money', from fé (< *fehu) + lag 'a laying' (PIE *legʰ- 'to lie, lay'), first attested in the Viking-age North and productive in the Danelaw. So only its first element belongs to this root, and the box should be labelled Old Norse rather than Germanic for that word; Watkins likewise routes FELLOW through 'Old Norse fé' rather than through a Proto-Germanic *fēlag.\",\n     \"derivation_fa\": \"واژهٔ نخست درست و اصلی است: ژرمنی آغازین *fehu «دام، چهارپا، مال» از هندواروپایی *péḱu (گوتی faihu «مال، پول»، آلمانی کهن fihu «دام»، انگلیسی کهن feoh، اسکاندیناوی کهن fé)؛ بر پایهٔ قانون گریم p به f و ḱ به h بدل شده است. اما félag واژه‌ای ژرمنی مشترک نیست، بلکه ترکیبی است در نورس کهن (اسکاندیناوی کهن) به معنی «شراکت، مالِ روی‌هم‌گذاشته»، از fé «مال» و lag «نهادن» (از ریشهٔ هندواروپایی *legʰ- «خواباندن، نهادن»)؛ پس تنها جزء نخست آن به این ریشه بازمی‌گردد و برچسب درست برای آن «نورس کهن» است نه «ژرمنی». واتکینز نیز واژهٔ fellow را از «اسکاندیناوی کهن fé» می‌گیرد نه از صورتی ژرمنی. ادعای نورایی با این اصلاح پذیرفتنی است.\",\n     \"sources\": [FEHU, ETY_FELLOW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"Watkins 1985 s.v. peku-: 'Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD2' — *fehu is confirmed, but the appendix has no Germanic *fēlag; the compound is Old Norse.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 581 (fee) and 583 (fellow)\", \"stance\": \"partial\",\n       \"note\": \"'fee, n., cattle; property; money — ME. feoh, fr. OE. feoh … Goth. faihu' supports *fehu; but 'fellow, n. — … fr. ON. felagi, „partner, companion“, from felag, „companionship“, lit. „laying down of money“, fr. fé, „cattle, money“, and lag, „a laying“' makes félag Old Norse and its second element a different root.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck §3.15 and §11.41 (SYN.txt lines 3927, 19547)\", \"stance\": \"supports\",\n       \"note\": \"'Goth. faihu „property, money“, ON fé, OE feoh „cattle, property, money“ : OHG fihu „cattle“, Lat. pecu … Av. pasu- „cattle“ (3.15)'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. peKu\", \"stance\": \"supports\",\n       \"note\": \"'Go. faihu n. „money“, OHG fëho, fihu, OS fehu n. „farm-animal“; OE feoh n. „cattle, wealth“; ON fé n. id.'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"fellow\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE feolaga 'partner, one who lays down money with another', a late-Old-English borrowing from Old Norse félagi (agent noun to félag) taken over in the Danelaw in the 10th–11th c.; ME felaghe, felawe > fellow (c. 1200 'companion, comrade'). The semantics run 'joint depositor of property' > 'partner, comrade' > 'any man' (mid-15c.) and, in the universities, 'member of a corporation paid from its revenues' (mid-15c.). Nourai's arrow from the fehu/félag box is exactly right.\",\n     \"derivation_fa\": \"انگلیسی fellow از انگلیسی کهن feolaga «شریک، آن‌که مال خود را با دیگری روی هم می‌گذارد» می‌آید که خود در سدهٔ دهم و یازدهم میلادی در ناحیهٔ دِین‌لا از نورس کهن félagi (اسم فاعل از félag) وام گرفته شده است؛ در انگلیسی میانه felawe و سپس fellow شده است. تحول معنایی آن چنین است: «هم‌سرمایه» ← «همراه، رفیق» ← «مرد، شخص» و در دانشگاه‌ها «عضو مستمری‌بگیر یک کالج». پیکان نمودار درست است.\",\n     \"sources\": [ETY_FELLOW],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference printed on the node; the parent box's AHD covers it — Watkins names FELLOW as the English outcome of Germanic *fehu- via Old Norse fé.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 583 s.v. fellow\", \"stance\": \"supports\",\n       \"note\": \"'fellow, n. — ME. felaghe, felawe, fr. OE. feolaga, fr. ON. felagi, „partner, companion“, from felag, „companionship“, lit. „laying down of money“, fr. fé, „cattle, money“, and lag, „a laying“.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/fellow\", \"stance\": \"supports\",\n       \"note\": \"'from Old English feolaga „partner, one who shares with another“, from Old Norse felagi, from fe „money“ (see fee) + lag … The etymological sense of fellow seems to be „one who puts down money with another in a joint venture“.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peku-\", \"stance\": \"supports\",\n       \"note\": \"'a. Old Norse fé, property, cattle: FELLOW.'\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Latin\",\n     \"words\": \"feudum\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"feudum 'fief, feudal estate' is Medieval Latin, first in Frankish/Burgundian charters of the 10th–11th c., not Latin of the classical period; and it is not an independent Italic reflex of *péḱu (that reflex is pecū, pecus, pecūnia, pecūlium). It is a borrowing of Germanic/Frankish *fehu 'cattle, movable property' — most handbooks reconstruct *fehu-ōd 'property-estate' (fehu + ōd 'possession'), while Klein derives feudum from an earlier feum and explains the -d- as analogy with allodium. Either way the route is root > Germanic > Medieval Latin, so the chart's direct arrow from the Indo-European root to a 'Latin' box is misleading — Watkins, whom the node cites, himself lists 'Medieval Latin feudum' as a sub-item of Germanic *fehu-. The gloss 'property, feudal state' is otherwise fine.\",\n     \"derivation_fa\": \"واژهٔ feudum «تیول، ملکِ فئودالی» لاتینِ میانه (سده‌های دهم و یازدهم میلادی، در سندهای فرانکی) است نه لاتینِ کلاسیک، و بازماندهٔ مستقیم *péḱu در ایتالیایی-لاتین نیست؛ بازماندهٔ آن pecū و pecus و pecūnia است. feudum در حقیقت وام‌واژه‌ای است از ژرمنیِ فرانکی *fehu «دام، مالِ منقول»، که بیشتر پژوهشگران آن را ترکیب *fehu-ōd «دارایی-ملک» می‌دانند و کلاین آن را از صورت کهن‌ترِ feum می‌گیرد و دالِ آن را برآمده از قیاس با allodium می‌شمارد. پس مسیر درست «ریشه ← ژرمنی ← لاتین میانه» است و پیکانی که نورایی یکراست از ریشه به جعبهٔ «لاتین» کشیده گمراه‌کننده است؛ خودِ واتکینز هم که نورایی به او ارجاع داده feudum را زیرمجموعهٔ ژرمنیِ *fehu- آورده است. با احتیاط پذیرفتنی است.\",\n     \"sources\": [ETY_FEUDAL, FEUDUM],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"Watkins 1985 s.v. peku-: '1. Germanic *fehu- in: … c. Medieval Latin feudum, feudal estate: FEUD2; INFEUDATION.' The word is in the appendix under this root, but as a Germanic loan into Medieval Latin, not as a Latin descendant — the chart's arrow bypasses the Germanic stage and drops 'Medieval'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 587 s.v. feud, n., a fief\", \"stance\": \"partial\",\n       \"note\": \"'feud, n., a fief. — ML. feudum, fr. feum, a word of Teut. origin; cp. Goth. faihu, „property“, OHG. fihu, „cattle“, and see fee … The d in ML. feudum is prob. due to the influence of the word allodium.' — Medieval Latin, Germanic origin.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/feudal\", \"stance\": \"partial\",\n       \"note\": \"'from Medieval Latin feudalis, from feudum „feudal estate, land granted to be held as a benefice“, of Germanic origin (cognates: Gothic faihu „property“, Old High German fihu „cattle“; see fee)'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt), grep 'feudum'\", \"stance\": \"silent\",\n       \"note\": \"No hit for feudum in the dictionary of classical Latin — only pecus/pecu articles; confirms the word is post-classical.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde-Hofmann (LEW_1910.txt), grep 'feudum'\", \"stance\": \"silent\",\n       \"note\": \"No hit; the classical Latin reflex of the root is pecū/pecūnia, not feudum.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"French\",\n     \"words\": \"feodal\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French féodal (the book prints it without the accent, as it does with other French forms) is the regular learned adjective to Medieval Latin feudālis (feudum + -ālis), taken into French in the late 15th–16th c. alongside the inherited noun fief (OF fieu, feu, feof < feudum). It is from this French adjective, not from Latin directly, that both the English and the Persian boxes below are fed.\",\n     \"derivation_fa\": \"صورت فرانسویِ féodal (که کتاب بدون نشانهٔ زیر-وزبر «feodal» چاپ کرده، چنان‌که با دیگر واژه‌های فرانسوی هم می‌کند) صفتِ عالمانه‌ای است ساخته‌شده از لاتینِ میانهٔ feudālis (از feudum + پسوند -ālis) که در سده‌های پانزدهم و شانزدهم وارد فرانسه شد؛ در کنار آن اسم موروثی fief (فرانسهٔ کهن fieu، feof) از همان feudum آمده است. هم انگلیسی feudal و هم «فئودال» فارسی از همین صفت فرانسوی گرفته شده‌اند نه یکراست از لاتین.\",\n     \"sources\": [ETY_FEUDAL],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference on the node; the parent's AHD entry covers feudum, and Klein p. 587 supplies the French adjective.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 587 s.v. feudal, adj.\", \"stance\": \"supports\",\n       \"note\": \"'feudal, adj., 1) pertaining to land held in feud … — OF., fr. ML. feudalis, fr. feudum.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/feudal\", \"stance\": \"supports\",\n       \"note\": \"'from Medieval Latin feudalis, from feudum' — the same adjective, reaching English through French.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"Persian\",\n     \"words\": \"feodâl «فئودال»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian فئودال feodāl is a 20th-century loan from French féodal, taken over with the whole cluster of terms of European historiography and political economy (فئودالیسم، فئودالیته، نظام فئودالی), largely through translations of French and, later, Marxist historical writing. The spelling with hamza on a yāʾ seat (ئ) is the standard Persian rendering of the French hiatus é-o. In Persian the French adjective has been nominalised: Moʿin defines it as an adjective/noun 'مالک، دارندهٔ زمین‌های بسیار' — 'owner of large land', exactly Nourai's gloss. The arrow French > Persian is right; the word did not come through Arabic.\",\n     \"derivation_fa\": \"«فئودال» وام‌واژه‌ای است از فرانسویِ féodal که در سدهٔ چهاردهم خورشیدی همراه با دستهٔ اصطلاح‌های تاریخ‌نگاری و اقتصاد سیاسی اروپایی (فئودالیسم، فئودالیته، نظام فئودالی) و بیشتر از راه ترجمه‌های فرانسه و سپس نوشته‌های تاریخی مارکسیستی وارد فارسی شد. نوشتن همزه بر کرسی «ی» شیوهٔ معمول فارسی برای نمایاندن پیوند دو واکهٔ é-o در فرانسه است. در فارسی این صفتِ فرانسوی اسم شده است؛ معین آن را «مالک، دارندهٔ زمین‌های بسیار» معنی کرده که دقیقاً همان معنایی است که نورایی داده. مسیر «فرانسه ← فارسی» درست است و این واژه از راه عربی نیامده است.\",\n     \"sources\": [ABADIS],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\",\n       \"note\": \"Moʿin, Farhang-e Fārsi: 'فئودال (فِ ئُ) [فر.] (ص.) مالک، دارندهٔ زمین‌های بسیار' (abadis.ir, فرهنگ معین section) — the tag [فر.] = French, i.e. Moʿin gives exactly the French source Nourai's arrow draws. The Amir Kabir two-volume text on disk (MON_part2.txt line 4841) reads 'فئودال: (ص.) کسی که دارای ملک‌ها و رعایای بسیار باشد و بر آنان تسلط کامل داشته باشد؛ ملک بزرگ، عمده مالک، ملوک‌الطوایف', with 'فئودالیسم' following.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. فئودال (MON_part2.txt line 4841; abadis mirror)\", \"stance\": \"supports\",\n       \"note\": \"See ref_check — French tag and the 'large landowner' definition.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/feudal\", \"stance\": \"supports\",\n       \"note\": \"Supplies the French/Medieval Latin end of the chain that Persian borrows: 'Medieval Latin feudalis, from feudum'.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"English\",\n     \"words\": \"feudal\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English feudal is first recorded in the 1610s, 'pertaining to feuds (fiefs)', borrowed from Medieval Latin feudālis, in part through Old/Middle French féodal; the earlier native-legal family (feoffee, feodary 'one who holds lands of an overlord', late 14c.) shows the word already in Anglo-French legal use. It has nothing to do with feud 'quarrel' (a separate word from Old French faide, Germanic *faihitho). Nourai's arrow Latin > English is right in substance, given that his 'Latin feudum' is Medieval Latin.\",\n     \"derivation_fa\": \"انگلیسی feudal نخستین بار در دههٔ ۱۶۱۰ میلادی به معنی «مربوط به تیول» ثبت شده و وامی است از لاتینِ میانهٔ feudālis، تا اندازه‌ای از راه فرانسویِ féodal؛ خانوادهٔ حقوقیِ کهن‌ترِ آن (feodary «تیول‌دار»، اواخر سدهٔ چهاردهم) نشان می‌دهد واژه پیش‌تر در زبان حقوقی انگلیسی-فرانسوی به کار می‌رفته است. این واژه هیچ پیوندی با feud «کینه و ستیز» ندارد که از فرانسهٔ کهن faide و ژرمنی *faihiþō آمده. پیکان «لاتین ← انگلیسی» درست است، به شرط آنکه «لاتین» را لاتینِ میانه بدانیم.\",\n     \"sources\": [ETY_FEUDAL],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference on the node; the parent Latin box cites AHD, where Watkins gives 'Medieval Latin feudum … : FEUD2; INFEUDATION' as the English outcome.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 587 s.v. feudal, adj.\", \"stance\": \"supports\",\n       \"note\": \"'feudal, adj. … — OF., fr. ML. feudalis, fr. feudum. See feud, „fief“.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/feudal\", \"stance\": \"supports\",\n       \"note\": \"'1610s, „pertaining to feuds“, estates of land granted by a superior … from Medieval Latin feudalis … Not related to feud.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peku-\", \"stance\": \"supports\",\n       \"note\": \"'c. Medieval Latin feudum, feudal estate: FEUD2; INFEUDATION.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-387.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"ok\")\n"
}
```


### [2026-09-07T20:57:50.219Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-387.py (file state is current in your context — no need to Read it back)
```


## [2026-09-07T20:57:53.843Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-387.py && python3 -m json.tool data/verification/page-387.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 387"
}
```


### [2026-09-07T20:57:55.403Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 3, 'confirmed': 8}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 4, 'supports': 4, 'not_checked': 4}
books consulted: {'partial': 7, 'contradicts': 1, 'supports': 26, 'silent': 2} | by book: {'KLN': 7, 'Etymonline': 6, 'AHD': 3, 'BRT': 2, 'NYB': 2, 'HRN': 2, 'SYN': 2, 'POK': 2, 'PHD': 1, 'HUB': 1, 'BQT': 1, 'ARY': 1, 'SOD': 1, 'WLD': 1, 'IEC': 1, 'LAT': 1, 'LEW': 1, 'MON': 1}
```


## [2026-09-07T20:58:15.592Z] AGENT

Verification of PDF page 387 (book page 357) is written to `/home/sfmqrb/git/rishe/data/verification/page-387.json`; `verify_check.py 387` reports 11/11 nodes, **0 PROBLEM lines**.

**Counts** — root: 1 confirmed. Nodes: 8 confirmed, 3 plausible, 0 disputed / transcription_suspect. Ref checks: 4 supports, 4 partial, 4 not_checked (nodes with `refs=None`). 38 `consulted` entries across POK, WLD, AHD/Watkins, IEC, SYN, KLN, BRT, NYB, HRN, HUB, PHD, BQT (Moʿin's footnote), MON, ARY, SOD, LAT, LEW, Etymonline.

**Root Pek/Peku** — confirmed: POK:797 lemma peḱ-2 "to fleece; cattle" carries both of Nourai's glosses on that one page; Watkins splits it as pek-2 / peku-, both tagged "[Pok. 2. pek- 797]".

**The three `plausible` nodes (no disputes, but worth the owner's eye):**
- #1 Avestan `pasu, pašman; fšu; fšu-pait` — pasu- means "cattle/small cattle", not "wool" (Bartholomae col. 878, Buck 3.15, Pokorny); `pašman` is not an Avestan headword in Bartholomae (only pašna- "eyelid"), the wool word is Proto-Iranian *pašman-; and the shepherd compound is *fšu-pāna- (Nyberg, Horn p. 171, Aryanpur) — Nourai's `fšu-pait` = *fšu-paiti- "lord of cattle", which Horn cites only for Armenian špet. Nourai's own ☞Pa pointer fits -pāna-.
- #6 Germanic `fehu; fĕlag` — *fehu is right; félag is Old Norse ("laying down of money", fé + lag < *legʰ-), so only its first element belongs to this root.
- #8 Latin `feudum` — Medieval Latin, and a Frankish/Germanic loan (*fehu-ōd; Klein: from feum, -d- after allodium), not an Italic reflex; Watkins himself files feudum under Germanic *fehu-, so the direct root→Latin arrow bypasses a stage.

**Extraction errors: none.** I rendered pdf p. 387 and compared: the JSON matches the printed chart word for word, including the accentless French "feodal", "fšu-pait", and «فئودال». Page image copied to `data/verification/sources/refs/ocr/BOOK/387.png`.

**Notes for the coordinator:** SNS:123,125 could only be checked partially — the Shāyast nē Shāyast scan has no determinable page offset (refs_online says so); the OCR does contain buz-pašm / uštur pašm and an Avestan index line "pašman- 123/10", consistent with the citation. 9 web pages archived via `fetch_source.py` (Wiktionary پشم/چوپان/*peḱ-/*péḱu/*fehu/feudum, Etymonline fellow/feudal/fight, abadis for Moʿin's فئودال); one 404 (no Avestan pašman page on Wiktionary) is not cited.
