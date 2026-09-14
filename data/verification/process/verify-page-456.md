# Verification process log — verify-page-456


## [2026-09-14T01:56:27.162Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 456 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-456.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-456.json. Write /home/sfmqrb/git/rishe/data/verification/page-456.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 456` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:28.375Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:29.227Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:29.245Z] TOOL RESULT

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


## [2026-09-14T01:56:29.758Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-456.txt"
}
```


### [2026-09-14T01:56:29.817Z] TOOL RESULT

```
1	=== PDF page 456 (book page 426) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skeud 1 : to throw, shoot  (refs POK:955)
4	#1 (parent #0) [Sanskrit] refs=POK:955; HRN:99 | čodatî : to hurry, propel
5	  #2 (parent #1) [Persian] refs=POK:955; BQT:636 | čost «چُست» : quick, fast
6	#3 (parent #0) [Germanic] refs=AHD | skiutan, skuttjan : to shoot ; skutilaz : dart, shuttle ; skutjôn : corner of sail, a sheet of cloth
7	  #4 (parent #3) [English] refs=None | shoot, shot, shut ; shuttle ; sheet
8	--- entry 1 ---
9	ROOT Skeud 2 -> redirect to Keued
10	
```


## [2026-09-14T01:56:33.113Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-456.json; echo \"=== MATRIX ===\"; cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-14T01:56:33.181Z] TOOL RESULT

```
{
  "pdf_page": 456,
  "book_page": 426,
  "entries": [
    {
      "root": {
        "name": "Skeud 1",
        "lang": "Indo-European",
        "refs": "POK:955",
        "gloss": "to throw, shoot"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:955; HRN:99",
          "words": [
            {
              "translit": "čodatî",
              "gloss": "to hurry, propel",
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
          "refs": "POK:955; BQT:636",
          "words": [
            {
              "translit": "čost",
              "gloss": "quick, fast",
              "script": "چُست"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "skiutan, skuttjan",
              "gloss": "to shoot",
              "script": null
            },
            {
              "translit": "skutilaz",
              "gloss": "dart, shuttle",
              "script": null
            },
            {
              "translit": "skutjôn",
              "gloss": "corner of sail, a sheet of cloth",
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
          "refs": null,
          "words": [
            {
              "translit": "shoot, shot, shut",
              "gloss": null,
              "script": null
            },
            {
              "translit": "shuttle",
              "gloss": null,
              "script": null
            },
            {
              "translit": "sheet",
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
        "name": "Skeud 2",
        "redirect": "Keued"
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


## [2026-09-14T01:56:40.284Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"skeud\\|(s)keud\\|codati\\|cōdati\\|ċodati\\|skiutan\\|skutilaz\" POK_full.txt | head -50\necho \"=== refs_online skeud ===\"\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n\""
}
```


### [2026-09-14T01:56:41.843Z] TOOL RESULT

```
53152:probably from *tri-quedros); possibly also Old Indie codati, codayati^ invigorates, sets in 
76617:Root / lemma: skeud-1 
76637:Root / lemma: (s)keud-2 
76641:Material: Old Indie codati, codayat/^treM an, throngs', np. c^s/"agile, active, fitting'. Old 
76662:German dial, hutzen^ set in motion, hetzen' (as Old Indie codati), also "bump, poke'; 
77407:skeUti^-, skeud-, skeug-, skeuk-. 
77599:mcymr. isgaud, cy-sgawd, cymr. cy-sgod, acorn, scod, neucorn. skez, bret. skeud 
=== refs_online skeud ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


## [2026-09-14T01:56:44.061Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '76610,76700p' POK_full.txt"
}
```


### [2026-09-14T01:56:44.129Z] TOOL RESULT

```
*skugwa-^s\\Y in Middle Low German schu(we), Swedish skugg. Old Church Slavic scuti 
'hetzen' {*skou-); 

References: WP. I 377, II 556, Trautmann 263, Wissmann Nom. postverb. 128, 177 f. and 
SkopBSB. 1954,2. 
Page(s): 955 

Root / lemma: skeud-1 

Meaning: to protest, grumble 

Material: Gr. OKuSpaivu), OKu^opai "rage against, grolle', aKu9p6(; (diss, from *aKu5-9p6c;) " 

grumpy, surly, sullen, unwilling, sad', aKu9pu)n6(; ds., OKuGpa^w "bin unwilling '; 

Lithuanian pra-skundu, -skudau, -skusti\o ache, to exhaust begin ', skunda^ 
accusation ', praskunda^'^a\v\\ nuoskunda^'^W.Y, skundziu, skijsti's\c\\ bemoan '; Latvian 
skund-u, -e/"miftgunstig, envious sein, be angry with'; Lithuanian skaudus^ painful, sullen, 
violent', skausta {skaudeti) "es schmerzt', Latvian skauzu, skaust^ envious sein, injure, 
hurt', skaudetds.; Lithuanian skaudu/ys ^ u\cer' . 

References: WP. II 554; 

See also: compare also keuod- above S. 595 f. 

Page(s): 955 

Root / lemma: (s)keud-2 

Meaning: to throw, shoot 

Material: Old Indie codati, codayat/^treM an, throngs', np. c^s/"agile, active, fitting'. Old 

Indie skundate' hurries ' (Dhatup.); 

gr. Ku5ia(; "Zahnkeim', Hes. (?); alb. heth^ throw, cast, winnow ' (for 77edhf|-onn 
*skoude/ff?); 

This assumption seems uncertain; maybe from Root/ lemma: se(i)-2 . sai-. sT-. se- sa- 
and sei- si- (to throw, send, let fall, sow): derived alb. {*seth), hedh 'throw'. 



Old Icelandic skjdta. Old English sceotan'toss, fling, bump, poke, schieften'. Old High 
German sciozan 'schielien, throw, shooting up bewegen'; Old High German scoz 
"projectile, sprout', scuz^ shot, throw, quickness ', Old Icelandic skjotr. Old English sceot 
"quick, fast', Gothic skautlap, hem'. Old Icelandic skautu. " corner, tail, point, edge, lap, 
protrusion'. Old High German scoz^ corner, tail, Kleiderschoft, Rockschoft', Middle Low 
German schott{-tt-) "(vorgeschobener) bar, bolt, lock ', whereof sc/7^//e/7"abdammen, 
hinder, shield ', Middle High German Modern High German schutzen, 

without aniaut. 5-/ Middle High German hossen, /7c»/ze/7 "quick, fast run'. Modern High 
German dial, hutzen^ set in motion, hetzen' (as Old Indie codati), also "bump, poke'; 

Lithuanian skudrus, skaudrus'agWe'; Latvian skaudrs6s., skudra' ant'; Old Church 
Slavic /5-Ayo(3//"herauswerfen', russ. k/dafb't\r\ro\N', k/dk/j" rash, hasty, willing, ready, 
greedy '. 

References: WP. II 554 f.; 

See also: s. also under skeu-5 and skeub-. 

Page(s): 955-956 

Root / lemma: (s)keu-1 

Meaning: to perform, commit 

Material: Gr. aK£uo(; n. (mostly PI.) "appliance, armament, armor', OKEun "armament, 

armor, clothing, Tracht', OKSua^u) "bereite, richte an; putze from; bewaffne; stifte an'; 

Old Icelandic heyja. Old English hfegan^ commit '; 

Old Church Slavic /0/'e-/ri/////"adorn, embellish, adorn', russ. kutitb^ carouse, sich with 
Klatsch befassen, rage, clamor'. Church Slavic /r^////"machinari', Czech kutiti, kutat/'dme, 
push, philander, flirt ', also (refl.) " gnaw, dig, schijren'; the Slavic words based on a *kou- 
ta perhaps " front '. 

References: WP. II 546, Vasmer 1, 706 (,unclear'). 
Page(s): 950-951 

Root / lemma: (s)keu-2, (s)keu9 : (s)ku- 

Meaning: to cover, wrap 

Material: Old Indie skunati, skunoti, skauti^bedecVX; doubtful ku-kula-^Hu\sev\, armament, 

armor', y05/77s^-/rJ/a-"Lumpenkleid the buddhist. Monche';
```


## [2026-09-14T01:56:56.308Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep ===\"; grep -n -i \"čust\\|cust\\|tschust\\|čust\\|c^ust\" HRN.txt | head -20\necho \"=== HRN page 99 (leaf 120) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==121' HRN.txt | head -60"
}
```


### [2026-09-14T01:56:57.312Z] TOOL RESULT

```
=== HRN grep ===
11:public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we have taken Steps to
=== HRN page 99 (leaf 120) ===
— 99 —
442. öu8t 'flink, tätig, passend'.
ai. l/cörf-, corföf^e 'antreiben ; sich beeilen' (Nöldeke,
mündliche Mitteilung).
Fr. Mtiller's (WZKM. 5, 68) Ableitung des Wortes
aus aw. cista- bezw. cista- ist schon wegen der Vokal-
difl^erenz (doch vergl. np. miizd) wenig wahrscheinlich.
443. eekuS 'Hammer .
aw. cakusqm, yt. 10, 130 'Hammer', Geldner, KZ.
25, 531 Note 210.
Das neupersische Wort ist nicht klar; eine Neben-
form ist öeköd oder deköj, vergl. dialektisch Kasan:
ceküSy rakoz, caküs, ödkös, vergl. kurd. cäqü, cek (H.-Sch.).
Nöldeke schlägt vor (mündliche Mitteilung), auch np.
öäk 'Spalt, Bruch' zu öekus zu stellen.
444. {\)ceni *Essen', cemfden 'trinken'.
ai. l/^(faw-, cämati (skr. camajiti) 'schlürfen',
oss. cimin, ba\dimin 'schlürfen* (320).
445. {2)ceni Sinn .
phlv. clm 'Urgrund, Ursache, Sinn .
Säle mann, Mol. asiat. IX, 233 Note 20.
446. cernber (geschrieben cenber) 'Kreis, Ring (z. B. Vis
und Ramin, S. 89 Vers 1)'.
V
phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
Zu np. cep 'links' (No. 435), gr. yAfiiJxct) 'biege',
adfinvXog (Nöldeke, mündliche Mitteilung).
Fick setzt als Wurzel für ai. capa- und gr. ad^iTiTO)
qep' an. Zu derselben Wurzel wird übrigens auch np.
xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
No. 12 — 'krumm, gebogen, yemtden etc. gehören.
447. eend 'einige*; wie viel?*, cendän, dendm, cendi,
aw. cvant' 'wie viel?'; phlv. cand.
kurd. LW. dend , dm; bei. cunt 'wie viel?' (64);
af;'. cof»[ira, com\ra wie viel?*; wa/. vum^ ciin, sar.
cund.
448. cöh 'Holz*.
phlv. 6öp 'Holz' (Guj. Ab.); kurd. cö, siw (H.-Sch.);
bei. LW. vöp (66); wa/. ^öpk, sar. /Jih,
7*
```


## [2026-09-14T01:57:02.859Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ===\"; grep -n -A14 \"^skeud-\\|skeud-\" AHD_watkins1985.txt | head -60\necho \"=== KLN shoot ===\"; grep -n \"skiutan\\|skeutan\\|sceotan\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T01:57:02.942Z] TOOL RESULT

```
=== AHD ===
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
944-skipam
945-[skipam. Ship. Germanic noun of obscure origin. 1. Old English scip, ship: sHIP. 2. Middle Dutch schip, ship: (SCHIPPERKE), SKIPPER}, 3. Italian schifo, ship, skiff: skiFF. 4. French équiper, to equip: EQUIP. [In Pok. skei- 919.]]
946-skot-. Dark, shade 1. Suffixed form *skot-wo- in Ger- manic *skadwaz in Old English sceadu, shade: SHADE, SHADOW. 2. Suffixed form *skot-o- in Greek skotos, darkness: scoToMa. [Pok. skot- 957.] skreu-. To cut; cutting tool. Extension of sker-'. 1. Basic form *skreu- in: a. Germanic *skraw- in Old English scréawa, shrew (having a pointed snout): SHREW, (SHREWD); b. Germanic *skraud- in Old English scréade, piece, fragment: SCREED, SHRED; C. Germanic *skrid- in (i) Old English scriid, garment (< “piece of cloth”): SHROUD (ii) Old French escro(uje, scroll: SCROLL (iii) Dutch schrood, a slice, shred: scRop. 2. Extended form “skreut- in Latin scriita, trash, frippery: SCRUTINY. 3. Extended variant form ‘*skraut- in Latin scrétum, scrotum (probably identified with scrautum, leather quiver for arrows): SCROTUM. [Pok. 4. (s)ker-, Section ITI. 947.]
947-skribh-. To cut, separate, sift. Extension of sker-1. 1. Latin scribere, to scratch, incise, write: SCRIBBLE, SCRIBE, SCRIPT, SCRIPTORIUM, SCRIPTURE, SERIF, SHRIVE; ASCRIBE, CIRCUMSCRIBE, CONSCRIPT, DESCRIBE, INSCRIBE, MANUSCRIPT, POSTSCRIPT, PRESCRIBE, PRO- SCRIBE, RESCRIPT, SUBSCRIBE, SUPERSCRIBE, TRAN- SCRIBE. 2. Greek skariphos, scratching, sketch, pencil: SCARIFY}, [Pok. 4. sker-, Section II. 945.]
948-skut-. To shake. Germanic *skid- in Middle Low German schéderen, to tremble, be afraid, akin to the source of Middle English shoddren, to tremble: SHUDDER. [Pok. (s)kiit- 957.]
949-(s)kwal-o-. Big fish. 1. Suffixed form *kval-o- in Ger- manic *hwalaz, whale, in: a. Old English hwel, whale: WHALE); b. Old Norse Avalr, whale: NARWAL, RORQUAL. 2. Latin squalus, a sea fish: SQUALENE. [Pok. (s)k¥alo- 958.]
950-(s)lag-. To seize. 1. Suffixed form */ag-yo- in Germanic *lakjan in Old English leccan, to seize, grasp: LATCH. 2. Variant form *slagv- becoming */ab-, with nasalized form *la-m-b- in Greek lambanein (verbal adjective léptos), to take, seize: LEMMA!, -LEPSY; ANALEPTIC, ASTROLABE, CATALEPSY, EPILEPSY, NYMPHOLEPT, OR- GANOLEPTIC, PROLEPSIS, SYLLABLE, SYLLEPSIS. [Pok. (s)lag#- 958.]
951-slak-. To strike. 1.Germanic *slahan in Old English sléan, to strike, kill: sLay. 2. Germanic suffixed form *slag-j6- in Old English slecg, hammer: SLEDGEHAMMER. 3. Germanic suffixed form *slah-tram in Old Norse sidtr, butchery, “striking,” probably akin to the Scandinavian source of Middle English slaughter, killing: SLAUGHTER. 4. Germanic *slag- in: a. Old High German slag (> German Schlag), a blow: scHLOocK; b. Middle Dutch slag, a blow: ONSLAUGHT; C. probably Middle Low Ger- man slagge, metal dross (< “that which falls off in the process of striking”): SLAG. 5. Germanic suffixed length- ened-grade form *slégiz in Old Norse sl@gr, clever, cunning (< “able to strike”): SLEIGHT, SLY. [Pok. slak- 959.]
952-sléb-. To be weak, sleep. Possibly related to slég- through a hypothetical base *slé- (< *sle-). Germanic *slépan, *slépaz in Old English slépan, to sleep, and slép, sleep: SLEEP. [In Pok. 1. leb- 655.]
953-slég-. To be slack, be languid. Possibly related to sléb- through a hypothetical base *slé- (< *slea-). Zero-grade form *(sjlag-, becoming *(s)lag-. 1.Germanic *slak- in Old English sizc, “loose,” indolent, careless: SLACK}. 2. Suffixed form *lag-so- in Latin laxus, loose, slack: LAX; DELAY, RELAX, RELAY. 3. Suffixed nasalized form *la-n-g-u- in Latin languére, to be languid: LANGUISH. 4. Compound */ag-ous-, “with drooping ears” (*ous-, ear; see ous-), in Greek lagés, lagos, hare: LAGOMORPH.
954-smei-
955-5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
956-(s)meit(2)-
957-navian source of Middle English smilen, to smile: SMILE. 3. Suffixed form *smei-ro- in Latin mirus, wonderful (> mirdri, to be amazed): MARVEL, (MI), MIRACLE, MIRAGE, MIRROR; ADMIRE. 4. Prefixed zero-grade form *ko(m)- smi-, smiling with (*ko-, *kom-, together; see kom), in Latin cémis (< *cosmis), courteous: comity. [Pok. 1. (s)mei- 967.]
--
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2226-SEAR?
2227-SEAR? ser-3
2228-SEARCH sker-3 SEASON sé@-1
2229-SEAT sed-1 SEAWARE wei-1 SECANT sek-
2230-sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2231-SEE? sed-1
2232-SEED sé-1
2233-SEEK sag-
2234-SEEL kel-2
2235-SEEM sem-! SEEMLY sem-! SEEP seib-
2236-SEETHE seut- SEGMENT sek- SEGNO  sekw-1 SEGREGATE ger-1, s(w)e- SEGUE sekw-1 SEGUIDILLA sekw-1 SEICENTO dekm, s(w)eks SEIGNIOR sen- SEISIN sag-
2237-SEISM_ twei-
2238-SEIZE sag-
2239-SELECT leg-1, s(w)e- SELF s(w)e-
--
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
2253-105
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2255-SIDE sé-2 SIDEREAL sweid-1 SIEGE sed-1 SIEGFRIED pri-, segh- SIEROZEM dhghem- SIEVE seib-
2256-SIFT seib-
2257-SIGHT sekw-2 SIGN sekw-1 SIGNORY sen-1 SIKH kak-1 SILENT si-lo- SILL swel-3
2258-SILLY sel-2
2259-SILT sal-1 SILURID ors- SILVICOLOUS kWel-1 SIMILAR sem-1 SIMPLE sem-1 SIMPLEX sem-! SIMPLICITY sem-1 SIMULTANEOUS sem-1 SIN] es-
2260-SINCE s6@-2 SINCERE ker-3 SINCIPUT kaput SINECURE cura, sen-2 SINEW sé-4
2261-SING sengh- SINGE senk- SINGLE sem-1 SINGSPIEL sengWh- SINISTRORSE wer-3 SINK seng¥- SINN FEIN s(w)e- SINTER sendhro- SIP seue-2
2262-SIR sen-1
2263-SIRDAR dher-2, ker-1 SIRE sen-!
2264-SIREN twer-2 SIRLOIN lendh-1, uper SIRVENTE servus SISTER swesor- SISTRUM twei- sit sed-1
2265-SITAR ten-, trei- SITH sé@-2 SITUATE tkei- situs tkei-
2266-SITZ BATH sed-1
2267-SITZKRIEG gWere-2, sed-1
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
2269-SLAUGHTER  slak- SLAVER! |leb-1 SLAY slak- SLED sleidh- SLEDGE sleidh- SLEDGEHAMMER slak- SLEEP sléb- SLEET sleu- SLEEVE sleubh- SLEIGH sleidh- SLEIGHT slak- SLEW! sloug- SLICK lei- SLIDE sleidh- SLIGHT lei- SLIM leb-1 SLIME lei- SLING! slengWh- SLINGSHOT slengh- SLINK sleng’h- SLIP! lei-
2270-sLiP3  sleubh- SLIPPERY |lei- SLIVOVITZ  sii- SLOB leb-1
2271-SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
2272-SNICKERSNEE sneit-, steig-
2273-SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2274-SOL?
2275-SOL
2276-SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277-SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2278-sow2 si- SPADE! spé-2 SPADE2 spé-2 SPAN! (s)pen- SPAN2 (s)pen- SPANGLE (s)pen- SPANNER (s)pen- SPAN-NEW newo-, spé-2 SPAR! sper-! SPARERIBS rebh-2, sper-1 SPARGE (s)preg- SPARLING spei- SPARROW sper-? SPARSE (S)preg- SPATHE spé-2 SPATHIC spé-2 SPATULA spé-2 SPAY spé-2 SPEAK spreg- SPEAR sper-! SPECIES spek- SPECIMEN spek-
2279-SPECIOUS spek- SPECTACLE spek- SPECTRUM spek- SPECULATE spek- SPECULUM spek- SPEECH spreg- SPEED spé-1 SPELL! spel-3 SPELL? spel-3 SPELT! spel-! SPERM! sper-4 SPEW spyeu- SPHENE spé-2 SPHENO- spé-2 SPICA spei- SPICA_ spei- SPICULUM spei- SPIDER (s)pen- SPIKE! spei- SPIKE? spei- SPILE spei- SPILL! spel-1 SPILL? spei- SPIN (s)pen- SPINDLE (s)pen- SPINE spei- SPINEL spei- SPINIFEX dhé-1 SPINNEY spei- SPIRACLE spirare SPIRE! spei- SPIRE? sper-2 SPIRIT spirare SPIT! spyeu- SPIT? spei- SPITTLE spyeu- SPITZ spel- SPLANCHNIC spelgh- SPLEEN spelgh- SPLENDID spel-2 SPLICE splei- SPLINT splei- SPLINTER splei- SPLIT splei- SPOIL spel-1 SPOKE! spei- SPONDEE spend- SPONSOR spend- SPONTANEOUS (s)pen- SPONTOON peuk- SPOON spé-2 SPOOR spere- SPORADIC sper-4 SPORE sper-4 SPORO- sper-4 SPORRAN bursa SPORT per-2 SPOUSE spend- SPOUT spyeu- SPRAG (s)preg- SPRAWL sper-4 SPREAD sper-4 SPREE ghend- SPRING spergh-
=== KLN shoot ===
34174:Scorzonera,  n.,  a  genus  of  plants  of  the  chicory family  (bot.)  —  ModL.,  fr.  It.  scorzonera,  lit. ‘viper’s  plant’,  fr.  scorzone,  ‘viper’,  fr.  L.  cur- tidnem,  acc.  of  curtio,  ‘viper’,  which  is  prob.  rel. to  curvus,  ‘curved,  bent,  crooked";  see  curve. The  initial  s-  in  It.  scorzonera,  is  prob.  due  to the  influence  of  scorto,  ‘short’, scot,  n.,  contribution,  tax.  —  ME.,  prob.  fr.  ON. skot,  which  is  rel.  to  OE.  sceot,  ‘shot,  reckoning, contribution’,  fr.  sceotan,  ‘to  shoot,  contribute’, and  to  Du.  schot,  G.  Schofi,  ‘tax,  contribution’. OF.  escot  (whence  F.  tcot),  ‘share’,  is  a  Teut. loan  word.  See  shoot  and  shot,  ‘share,  contribu¬ tion’,  which  is  a  doublet  of  scot.
34935:sheet,  n.,  piece  of  cloth;  piece  of  paper.  —  ME. schete,  shete,  fr.  OE.  sciete,  scyte,  scete,  itself derived  fr.  OE.  sceat,  Tap,  bosom,  surface;  piece of  cloth’,  which  is  rel.  to  ON.  skaut,  ‘seam,  hem of  a  garment’,  Goth,  skauts,  of  s.m.  M  Du.  scoot, Du.  schoot,  ‘bosom,  lap’,  OHG.  SC030,  scoya, MHG.  schos,  G.  Schofi,  of  s.m.,  and  prob.  also to  OE.  sceotan,  ‘to  shoot'.  See  shoot  and  cp. sheet,  ‘rope’.  Cp.  also  scuttle,  ‘hatchway’. Derivatives :  sheet,  tr.  v.,  sheet-ed,  adj.,  sheet-er, n.,  sheet-ing ,  n.
35028:shoot,  tr.  and  intr.  v.  —  ME.  she  ten,  sho  ten,  fr. OE.  sceotan,  rel.  to  OS.  skiotan,  ON.  skjota, Swed.  skjuta,  Dan.  skyde,  OFris.  skiata,  MDu. scieten,  Du.  schieten,  OHG.  skiogan,  MHG. schiejen,  G.  schieJSen,  fr.  I.-E.  base  *(s)qeud-,  ‘to throw,  shoot;  to  run,  haste’,  whence  also  OI. skundate,  ‘hastens,  makes  haste’,  OSlav.  is- kydati,  ‘to  throw  out’,  Lith.  skudrits,  ‘quick, nimble’.  Cp.  scoot,  scot,  ‘contribution’,  scoter, scuttle,  sheet,  shot,  shut,  shuttle,  1st  skeet,  skit, skite,  skitter,  skittish,  and  the  second  element in  wainscot.
35044:shotten,  adj.,  having  shot  its  spawn  and  accord¬ ingly  of  inferior  value.  —  ME.  shotyn,  fr.  sho¬ ten,  shotyn ,  pp.  of  shetcn,  shoten,  fr.  OE.  sceotan (pp.  gescoten),  ‘to  shoot’.  See  shoot, should,  past  tense  of  the  auxil.  v.  shall.  —  ME. scholde,  sholde,  fr.  OE.  scolde,  sceolde,  past tense  of  sceal.  See  shall.
35100:shuttle,  n.  —  ME.  sehytel,  fr.  OE.  scytel,  ‘missile, dart’,  a  gradational  variant  formed  from  the stem  of  sceotan,  ‘to  shoot’;  so  called  from  its being  ‘shot’  across  the  threads  in  weaving.  See shoot  and  dimin.  suff.  -le  and  cp.  prec.  word. Cp.  also  skittle,  which  is  a  doublet  of  shuttle. Derivative:  shuttle,  tr.  and  intr.  v. shwa,  n.  —  A  var.  of  schwa, shy,  adj.,  timid;  bashful.  —  ME.  schey,  shey, ‘shy’,  fr.  OE.  sceoh,  ‘timid’,  rel.  to  MLG. schii(we),  Du.  schuw,  ‘shy’,  MHG.  schiech,  G. scheu,  of  s.m.,  OHG.  sciuhen,  MHG.  schiuhen, ‘to  shy  at,  to  fear’,  G.  scheuchen,  ‘to  scare away’.  The  only  non-Teutonic  cognate  is OSlav.  siuti,  ‘to  hunt,  incite’.  It.  schivare,  ‘to avoid’,  is  a  Teut.  loan  word.  Cp.  eschew. Derivatives :  shy,  intr.  v.,  shy-er,  n.,  shy-ly,  adv., shy-ness,  n.
```


## [2026-09-14T01:57:13.418Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 grep چست ===\"; grep -n \"چست\" BQT_v2_pages.txt | head -30\necho \"=== pdf page tags near ===\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3"
}
```


### [2026-09-14T01:57:13.533Z] TOOL RESULT

```
=== BQT v2 grep چست ===
1568:                 ‫سجتالی ص ‪.*4‬‬        ‫« چستار اول در دور کون چیزی از آفربد کار » «کات‬
3723:                             ‫صبح صادق باشد ‪.‬‬                         ‫چست وچالاك وجلد راکوبند ‪. ۴‬‬
4444:                                                        ‫رك‪ :‬چستن ‪ ۰‬چیین ‪.‬‬       ‫‪۰‬‬      ‫ساب طبری‬
5451:‫چست ‪ = ۷‬بش‌اول‌وسکون‌ثانی وفوقانی‪.‬‬                   ‫چسبیدن * ۔ بباای فارسی بورزن‬
5473:           ‫است ‪.‬‬     ‫ار ارکانش باد درست‬               ‫فراخ و کرنه چست‌است‬        ‫خانه‬
5484:‫چسنگه » بروزن پلنگه » مردم کل‬                     ‫چسته = بفتح اول بروزن دسته» بمعنی‬
7804: ‫چیچست "‪ ۱۰‬بکراول وجیم وسکون‬                                  ‫ثانی» مخفف‬     ‫کلوون‬
7981:                                                          ‫و آن‬‫دستی‬‫چستی آن‌چیزه وچ‬
17054:                                                          ‫به ازنین‌زن چست‬
18169:  ‫فی‌ذ کرها لانها ای تسمی عندنا دربجانات سنها؛‪ .‬وهمو درالتنهیم (س ‪ )4۰4‬آرد‪«:‬دریگان‌چست؟‬
32444:                        ‫سیگر و ف‬                       ‫وابه‌ازمردم بی‌وفارونی‌ته‌بود ‪ -‬وبمعنی‌چست‬
37577:     ‫‪۲‬‬   ‫‪da ¢‬‏‬    ‫هم خوانده شده وما تمیدانیم این کاه چست‬    ‫لکرك کوید ‪« :‬سکدانسون»‬    ‫‪- ۳‬‬
38904: ‫بمعنی‌پاسواراست ککنهابه‌ازيبادة چست‌وچابك‬
=== pdf page tags near ===
```


## [2026-09-14T01:57:18.622Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt | cat -A | head -5\necho \"---- page markers sample ----\"\ngrep -n -m5 -E \"^\\s*(page|صفحه|\\[)\" BQT_v2_pages.txt | head\necho \"---- count formfeeds ----\"; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt'\nt=open(p,encoding='utf-8').read()\nprint('pages',t.count('\\f')+1)\nlines=t.split('\\n')\n# find page index of line 5451\nidx=sum(len(l)+1 for l in lines[:5450])\nprint('formfeed page of line 5451 (1-based):', t[:idx].count('\\f')+1)\nEOF"
}
```


### [2026-09-14T01:57:19.787Z] TOOL RESULT

```
^L                                         M-bM-^@M-+M-bM-^@M-*7M-bM-^@M-,M-bM-^@M-,$
$
                          M-bM-^@M-+M-XM-1M-YM-^FM-bM-^@M-*M-[M-3M-bM-^@M-,M-bM-^@M-,$
    M-bM-^@M-+M-YM-^FM-XM-'M-XM-*M-bM-^@M-,$
      M-bM-^@M-+M-XM-' M-YM-^EM-bM-^@M-,$
---- page markers sample ----
---- count formfeeds ----
pages 684
formfeed page of line 5451 (1-based): 95
```


## [2026-09-14T01:57:22.670Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nb=d['BQT']\nfor k,v in b.items():\n    print(k,'=',str(v)[:1500])\n    print()\n\""
}
```


### [2026-09-14T01:57:23.791Z] TOOL RESULT

```
title = Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)

kind = archive_djvu+local_scan_ocr

url = https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.

lookup_hint = grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

local_file = ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']

page_offset = vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').

covers_etymology = True

notes = Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \f; leaf N = N-th \f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pag

scans = [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]

cites = page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-14T01:57:28.481Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='BQT_v2_pages.txt'\nt=open(p,encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (93,94):\n    print('===== leaf',i,'(printed ~',i+543,') =====')\n    print(pages[i][:3500])\nEOF"
}
```


### [2026-09-14T01:57:29.675Z] TOOL RESULT

```
===== leaf 93 (printed ~ 636 ) =====
                                                                                                                ‫م‪۳‬‬


‫و ازحېرقه‬       ‫دیه‬
                  ‫یمعن‬
                     ‫سیب‬
                       ‫وترک‬
                          ‫پ‪-‬وب‬
                             ‫کوبند ‪۴‬‬                         ‫وکرز و لمتال آن برآبد ‪ -‬وصدا وآواز درای‬
                                                          ‫وفازی را فيز `‬    ‫آص‬
                                                                             ‫وو‬ ‫و زنگه را همگویند ‪-‬‬
                                                            ‫گفته اندکه در مبان کوه و کتبد مبب خوردن‬

‫آن‌باشد که محافظت چراغ ازبادکند‪ -.‬وچراغپابه‬                                           ‫چیزی بر چیزی ببجد ‪.‬‬
‫و بمعنی چاره جوننده ‪٩‬‏ ف‬         ‫‪-‬‬   ‫را نیز کنتماید‪6‬‬
                                                            ‫چر نلک _ جتے لول و انی و رابع‬
               ‫امت ‪۹‬‬      ‫و رونشه مآ مده‬       ‫ودوظه‬
                                                             ‫و سکون ات و کلف » پرنده است بات‬
 ‫چر ولف = بروزن لرزید‪ .‬ماضی‌دوینند‬                                                                        ‫کوج ‪. ۱‬‬
‫چولره جتن اشد سنی دوید و چاره‪ -‬جوبی‬                         ‫چر نگیدن ‪ ۴‬ب بکر اول و تالی ‪.‬‬
                                          ‫کرد ‪. ۷‬‬           ‫آواز و صداکردن کرز و مانند آن بلشد سب‬
‫» بورزن ورزیدن » بمخنی‬               ‫رلون‬
                                        ‫ف‬ ‫ج‬                                                ‫زدن آن برجایی ‪.‬‬
                 ‫چاره جستن ‪ -‬و دومدن باشد ‪.‬‬
                                                            ‫ونم تالی وسکون‬          ‫وحل‬
                                                                                      ‫ات‬‫جروك =‬
 ‫چرو بدن‪ = ۸‬بر وزن گردیدنه ‪ ۰‬نی‬                               ‫‪a‬‏‬             ‫واو وکاف»ء مطلق تانرا کومند خواء‬
                      ‫دویده وچاره جوبی کرده ‪۰‬‬
                                                             ‫وخواء فن‌جووارزن وبرنج وبلوط ومانندآن ‪۴‬‬
‫مم اول و فتح الی > مر ساده‬            ‫چر ه ‪+‬‬                ‫ونانی را نزگفتماند کهدرته انبان گذارند بجهت‬
                      ‫‪#‬‬   ‫‪٩‬‏‬   ‫برامرد را کوند‬        ‫و‬      ‫گونند تانی است کهآ نرابجهت‬            ‫وی‬          ‫توشة راه ؛‬

‫شر مك »‬   ‫اول برورن‬   ‫تح‬        ‫بك‬        ‫جر‬                ‫اشکنه ترمت کنند ورىزه ریزه سازید؛ ویاشمعنی‬

‫‏‪ e‬ازولاتهایدیگر بمدد لشکری‬                                 ‫بسکون‌انی همآمده است که بروزن نفزك باش‬
                                                            ‫رضم اول وئانی ‪ ,‬چن و شکتح ودرحم شحه را‬


  ‫‪ _¥‬فز ‪ :‬چرنگه («‪.‬م‪ + ).‬بدن (یسوسصتری)‪.‬‬                                     ‫‪.‬‬   ‫رك ‪:‬چ ركمك‬       ‫_‬       ‫‪۱‬‬

 ‫است‪ .‬از چور لماك‬      ‫‪ ۷ 0‬آنری ‪ ( 68۲0‬درثر کی عشمانی‪ :‬اتمك ) بمعنی‌دان‬                       ‫‪9‬‬           ‫‪۳‬‬

  ‫‏‪ mk‬جنتایی بممنی درمقابل اش قرار دادن ‪.‬حرتر کی غربی «چورك» حرچیز که‌ رآ‬
                               ‫چور کاماك ‪5‬‬     ‫‪ :‬چور اد ‪6‬‬   ‫‪ :‬درمادء‬   ‫کا‌قدری‬      ‫ظ تورك لغتی‪.‬حسین‬              ‫نهند‪.‬‬

                                                 ‫‪.‬‬       ‫ند‬
                                                          ‫و‪0‬ی)‬
                                                             ‫‪-‬مروز د‪۵‬ز‪6 (۶۵۲‬گ‪-01‬‬
                                                                               ‫‪ ۴‬ا‬
                  ‫‪ - ۹‬اس
===== leaf 94 (printed ~ 637 ) =====
                                           ‫بیان نهم‬
                  ‫در جیم فارسی با زای هوز مشتمل برشش لغت‬
‫جز ده = بفتح‌اول وثالك وسکون‌نانی »‬                ‫=فتح اول وسکون‌انی » میمون‌را‬
                                                                               ‫جز ب‬
‫بمعنی‌چزدره است که جزغاله باشدیعنی دلبه وییه‬                             ‫کون دکه حمدونه است ‪.‬‬
                       ‫‪۰‬‬   ‫ریزه کرد بربان‌شده؟‬     ‫جز ‪۵‬ه بفتح‌اول وسکون‌انی ودال‌ابجد‪,‬‬
‫‪ -‬یکراول وسکون ثانی و غین‬          ‫چزع‬             ‫جالور کیست شبیه بملخ که پیوسته درغله زارها‬
              ‫‪۲‬‬   ‫لقطه دار‪ .‬خارمشت را گوند ‪۴‬‬       ‫ور هوای کرم فرباد طولانی کند و در‬ ‫می‌باشد د‬
                                                    ‫نی جاهاآ نرا بگیرند و بربان کنند وبشخورند‪.‬‬
‫چزك ‪ -‬پکر ارل وسکون ثانی‬
‫واف » پمعنی چزغ است که خار پشت‬  ‫ک‬                  ‫» بارهای‌دنده‬   ‫بروزن محمره‬   ‫جز در ه‬

                        ‫باشد‪ . ۴‬٭‬                         ‫ویبه بربان کرد روغن گرفته کروایندا ‪.‬‬


                                           ‫بان دهم‬
                  ‫در جیم فارسی با سین بی‌نةطه مشتمن بر چپار لت‬

‫چست ‪ = ۷‬بش‌اول‌وسکون‌ثانی وفوقانی‪.‬‬                   ‫چسبیدن * ۔ بباای فارسی بورزن‬
‫| جلد و چالاك و چابك باشد ‪ -‬و هرچیز که يك‬               ‫یشدگر‬
                                                            ‫دی با‬
                                                                ‫‌جسم‬
                                                                   ‫یافتن‬
                                                                       ‫مال ب‬
                                                                           ‫ج"اص‬
                                                                              ‫بیدن‬
                                                                                 ‫رقص‬
‫که انفصال آن مشکل بود ‪ -‬و چیزیرا محکم | و باندام درجابی شیند ‪ -‬و محکم ‪ -‬و ازك ‪-‬‬
‫و زیبارا همکفته‌اند ‪ -‬و بمعنی تنکه و چسبان‬         ‫بدست گرفتن ‪ -‬و بمعنی مل کردن حم آمده‬
 ‫هم هت ‪ ۸‬که نقیض فراخ و کشاد باشد ‪-‬‬                                                    ‫است ‪. ۷‬‬

  ‫‪ ۴‬رکه‪ :‬چزغ‪. ‎‬‬         ‫‪ - ٩‬رك‪ :‬چزده‪ ۴ .‬رك‪ :‬چزدره‪ - ۴ . .‬رك ‪ :‬چزك ‪.‬‬
  ‫‪ = ۵‬چیسدن (ه‪.‬م‪ = ).‬چفیدن ( «‪.‬م‪ »).‬از ریشة ابرانی لهاع ‪ , #‬افتانی ع‬
   ‫(چین دکی)‪( 02۳5260 .‬چسبنده) «اسشق‪ .‬هویشمان ‪ « ۱686‬اسفا ‪: ۱‬ص‪۷٤۲‬‏ » ‪.۹۲۱‬‬                   ‫‪0‬‬
  ‫‪ - ۱‬بمعنی مل كردن رك‪« 5۵1. 4981, 454 :‬هوبتمان ‪« : ۱44‬لطا (عریی)‬
   ‫چسفیدن» «صراح» ‪« .‬الضیف (عیبی) » چسبیدن تیرازشانه «‪٩‬‏ مجمل‌اللفه » « المیل » بچسپیدن‬
    ‫«مصادر زوزنی» «المیل والمیلان ‪ ...‬چپیدن» «تاح‌ال‌سادر ببپقی» » متعدی آن » چسپایدن ‪:‬‬
              ‫د از افادات علامه‌دهشد!ا»‪.‬‬   ‫چبانیدن» «مجمل‌اللفه»‬    ‫«الاستمالة(عریی) » سوی خوش‬
   ‫‪ - ۷‬هندی باستان_ ‪1 , 000‬ا‪ 46‬اغا ‪۲ :۱‬ص ‪ ۲۲۳۲۰‬ساب کرت ‪(112006‬راندن»‬
            ‫تحريك‪ .‬عجله کردن) « اسشق ‪ ۲64۲۰‬پهلری ‪1181۵0٥1۷‬‏ (دوبدن) دریکبه‪۳‬ع‪۲‬؟»‪.‬‬
           ‫است ‪.‬‬     ‫ار ارکانش باد درست‬               ‫فراخ و کرنه چست‌است‬        ‫خانه‬
                                                                                    ‫کر‪۱‬‬
                                                                                      ‫‪۸‬‬
       ‫امیر خرو دهلوی ‪.‬‬
                                             ‫‪ #‬چرك ‏ رك ‪ :‬لفات متفرقةٌ پابان کتاں ‪.‬‬
```


## [2026-09-14T01:57:46.031Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG čud/caud ===\"; grep -n -i \"caud\\|\\*čaud\\|cud-\\|čud\" CHEUNG.txt | head -20\necho \"=== HUB čust ===\"; grep -n -i \"ust 'flink\\|čust\\|cust\" HUB.txt | head -20\necho \"=== SKT shuttle/sheet ===\"; grep -n \"^shuttle\\|shuttle,\" SKT.txt | head -5\necho \"=== IEC skeud ===\"; grep -n -i \"skeud\\|kseud\\|codati\" IEC.txt | head -10\necho \"=== WLD Bd2 554 codati ===\"; grep -n -i \"codati\\|skundate\" /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-14T01:57:46.168Z] TOOL RESULT

```
=== CHEUNG čud/caud ===
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
3570:*Caud ‘to urge to, impel’ 
58266:*Caud, *Hranj 
=== HUB čust ===
11:public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we liave taken steps to
266:tute' etc., paz. afw *custom, law', aina^) (dtna) *mode,
978:vus', bandlv&n *custos carceris'.
1145:tlmdr 'aegritudo, cura aegroti, custodia*, afgh. LW.
2188:'custom' Shk. 241, afgh. LW. daatUr custom, usage,
3782:afgh. yun gait, movement, carriage, habit, custom*
=== SKT shuttle/sheet ===
17160:shuttle.  (E.)  So  calW  from  being tSet  across  the  threads  in  weaving.  M.  £ uAif//,  also  a  bott  of  s  door.  Fortned, with  suffix  -//  of  the  igent,  from  A.  S. Mw/',  base  of  pt.  t  pi  of  ue^tan^  to  shoot ■f-  Dan.  jk^tt,  skytui,  a  shuttle.  Der. ikmttlt-tock  ;  from  its  being  shot  backwards and  forwanl«  like  a  thultU^  and  because fdmUhed  with  feathers.
=== IEC skeud ===
15597:skérios — skeud-
15612:skeud- ‘fling, (Variant:
15828:skoud-, see skeud- (skheud-) O-gde in ON skeyti, n. ‘shaft, arrow’; Li. skausmenys, pl. ‘meteorites’
15982:skud- (1) ‘tip, tail, end, rear’. (Var: skhud-). Cf. skeud- , Oss. kūdi, s. “back, rear, tail; kūda, adj. *dock- ed, tailless'; Arm. cf. xuzem, v. ‘search’; xujz, gs: xuzi, i-st. ‘search’; Gk. skuzáo, v. “follow, tail — of animals'; beside Hes. skudízo, v. ‘kick’; Ir. scud, scod, m. (2) ‘skirt — of robe"; EME scut, v. ‘shorten’; s. ‘short garment; tai; ON skutr, m. ‘stern of ship’; OE cf. scota, wm. *camp-follower'?
16104:sKeud- (form of skeud- and skheud-, q.v.) The initial appears in Skt. Códàmi, v. ‘spur on’; cf. Li. Sauju, šauti, v. 'shoot'; MIr. (ambig.) brot-scuad, s. ‘rub- bish?
=== WLD Bd2 554 codati ===
35973:Ai. codati^ coddpati „treibt an, drangt“ (gegen andere Deutungen s. u.); 
35974:np. cust „flink, tatig, passend“, ai. skundate 5 ,eilt“ (Dhatup.) ; lit. skiidriis 
36013:PBrB. 32, 143. — Ai. codati nicht zu ^q^ed- „stachelii‘^ (z. B. Uhlenbeck
```


## [2026-09-14T01:57:51.870Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG 3570 ===\"; sed -n '3565,3620p' CHEUNG.txt\necho \"=== IEC 15612 ===\"; sed -n '15610,15618p' IEC.txt\necho \"=== WLD 35970-36020 ===\"; sed -n '35965,36020p' /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T01:57:51.960Z] TOOL RESULT

```
=== CHEUNG 3570 ===

wander, roam’ 
*REFERENCES: Horn 1893: 271; IIFL I: 391b f.; Safari 1373: 148; Kiefer 2003: 194 


*Caud ‘to urge to, impel’ 

*MIDDLE PERSIAN: (+ *ui-) BMP wewd- /wizöy-/ (or /wizoh-/ ?) ‘to examine, 
investigate’ 

Partic.: perf. pass. BMP wewst /wizost/; Inf.: BMP wewstn /wizöstan/ 

*NWIR: NP cust ‘quick, brisk, active’ || (+ *?) NP pizohidan/pizoh- ‘to investigate’ 
(LW) 

*NEIR: Oss. I. cudyn/cudt, D. codun/cudt ‘to be shaky’ 

*SANSKRIT: cod ‘to impel, to excite, to incite’ (RV+) = EWAia I: 551 

«PIE *(s)keud- ‘to shoot, impel’ = LIV: 560 | Pok.: 955 f., 636 

*IE COGNATES: OE sceotan ‘to sling, to thrust’, NHG schießen, Engl. to shoot, etc., 


(without s-) OCS kydati ‘to throw’ 
«REFERENCES: Abaev, Slovar’ I: 316; Werba 1997: 347; ESIJa П: 248 


*ЧаН! ‘to be calm, glad, rest 

*AVESTAN: 3(ii)à- ‘to be calm, glad, rest" > Liste: 70 

Pres. athem.: IND. 3sg. YAv. Siieiti (Yt 14.48), ? YAv. Säiienti/e (Y 16.7), 3pl. YAv. Siieinti, ? ҮАУ. 
Saiienti/e (Y 16.7), SUBJ. Ipl. YAv. šiiama (Y 58.3); Partic.: perf. pass. OAv. Siiata- (Y 51.8). © ҮАУ. 
Saiienti/e and Saiienti/e are "Gathicized" forms, cf. De Vaan 2003: 148. 

*OLD PERSIAN: S(i)yata- ‘peaceful, happy (on earth)’ <8-i-y-a-t>, $(i)yati- ‘welfare, 
peace (on earth), happiness (after death)’ <8-i-y-a-t-i-°> 

*MIDDLE PERSIAN: MMP $0, BMP $ /sad/ ‘glad, happy’. 0 MMP 3’yh- means ‘to 
be king, rule’ rather than ‘to make happy, glad’, v. DMMPP: l.c. > DMMPP: 315a, 
313a 


38 *&aH2 


*PARTHIAN: $’d ‘glad, happy’ = Ghilain: 99 | 

*KHOTANESE: tsata- ‘rich, happy’ 

*SOGDIAN: SSogd. уху, SSogd. štxw, CSogd. §’twx- ‘happy, joyful’ || (+ *pati-) 
CSogd. pts’dty’ (Е) ‘rest, gratification’, CSogd. pts’dy ‘at rest’ || (+ *ham-) SSogd. 
"nc()y, BSogd. ’nc’(’)y, CSogd. ’nc’y ‘to rest, dwell, cease’ 

(+ *ham-) Widely attested: Pres.: IND. 3sg. BSogd. ’nc’yt, CSogd. ’ncyt, 3р1. BSogd. ’nc’y’nt, SUBJ. 
=== IEC 15612 ===
sket- (2) “project, put forth, display, unfold, extend'. Cf. skotos & next. Mir sceithim, v. (2) ‘put forth’; cf. mod. scéi- thim, v. (bud, put forth, project, eject, jut, put out, vomit. -éi- is for former -ei- to avoid confusion w. sceit, f. 'terror); scea- thaim, v. is a variant; Li. skečiù, inf: skésti, v. ‘spread, unfold'; Latv. cf. Sketinaju, v. *un- wind — thread'. (Uncertainly) cf. Arm. xajr, i-st. and xajri-K, pl. form (produce, crop’, if fr. a type *skotris). Long-gde in Ir. scíoth, pl. -anna, f. ‘wattle fence’; Li. sketis, gs: skēčio, m. ‘umbrella’. (Isophonic in Ir. & MIr. scith, adj. “tired; f. “rest, pause, fatigue")
sketolos (sketel-, sketul-) (?) Oss. cf. kacäl, s. «chip, splinter’; MHG sché- del, sm. ‘skul; Du. schedel, m. id. (and ‘temple of forehead"); Li. sketelis, io, m. "back, bone; ridge'
skeud- ‘fling, (Variant:
shoot, impel.
1161
skheud- in Skt.) Skt. Codami, v. “egg on; hurry’; Alb. hudh, v. ‘fling’; MIr. cf..brot-scuad, s. ‘rubbish’; OHG skiozan, OS skiotan, OE scéotan, sv. 2 'shoot'; sceot, adj. ‘ready, quick’; ON skjóta, sv. 2 as OHG; skjótr, adj. as OE; (m. also “vehicle; horse); Sw. skjuta, sv. 2. ‘thrust, smite’ skeulos, om, is, à ‘cover, shelter’. Cf. skül-. (Skt. variant: skhoul-) Skt. cf. kholah, m. 'rainhat, helmet; Arm. (vowel ambig.) xuy, gs: xyi, ab. s. xyiv, s. ‘hut’; ON skjól, n. ‘shelter, cover’; Sw. skjul, n. ‘dutch barn’; N. E. shiel, shieling 'shepherd's huť; Norw. cf. skjule, v. ‘hide’. WP II, 547 skeup- ‘poke, stab, grope’. (Skt. variant: skhiup- or skhup-). Gmc. ambig. Skt. čhupāmi, v. “touch'; Go. (ambig. *skeubh-?) skiuban, sv. 2. ‘thrust; MHG schieben, sv. 2. id.; OE sceofan, sv. id. (beside sküfan, sv. 2. with instant aspect as lücan, sv. 2 ‘lock’, and a-sprütan, sv. 2. ‘sprout’; Du. schuiven, sv.; spruiten, id.); R SCup, m. “probe, lancet'; po-SCüpat, inf. “feel, grope’. Nominal type in Skt. chupah, m. “touch; hand-to-hand fight". Isophonic in OCS Stupli, adj. “weak, lean, ailing’; Pol. szczupły, Slovak, Stüply, id. skeut- ‘shred, tatter; shredded, torn’. (Vari- ant in Skt?) Skt. cf. a-Chotitab, pp. “torn off (butisophonic pra-$Cotami, v. = 'drip); ON skjóða, f. “skin bag’; Li. skiautis, gs: ies, f. ‘shred, snippet"; Latv. cf. Sautrs, adj. (loose, hanging’, from a variant *sKeut-?). (Isophonic in OCS Stusto, Stutiti, v. ‘perceive’, radical in Av. sku- look") skéuð, ið (sKeu-) “jump, start, go’. Cf. sKeuo as separate entry Skt. cf. (radical only) chyu- ‘go’; Gk. cf. skeüos, n. ‘equipment’; Alb. hov, v. jump’; Ir. cf. sceabha, m. ‘eagerness’; Go. skewjan, v. go’. LW in Fr. esquivier, It. schivare, Alb. shkoj & E eschew, via Romance); ON skæva, v. ‘hurry, clear off; (o-gde in) Du. schooien, v. ‘go away, clear off”; Fris. skoaje, v. ‘arrange’ (factitive: “make go"); OCz. ščuju, SCváti, v. fegg on: Pol. szczuC, v. ‘incite’; Ukr. SCuty (w. instr.), id. skond-, r-gde formula to accommodate some forms of type skend- (skand-); cf. sküd-
skeulos, om, is, à — skortos, à
20
25
=== WLD 35970-36020 ===
kien Abl. 308 (aber lit. skiidrhs „scharf‘^, von der Axt, lett. skaiidrs „scharf**', 
skaudre „8charfe Kante“ wohl kaum als „woran man sich weh tut“ hierher, 
sondern wie lett. skaute „scharfe Kante‘‘ zu sqeti- „schneiden, kratzen“); 
skaudeti usw. nicht zu qeud- „schreien‘', s. d. 

3. (s)qeud- „^yerfeD, schieBen, hetzen** ; intr. ^jdahinschieBen, eilen, hervor- 
schie6en“. 

Ai. codati^ coddpati „treibt an, drangt“ (gegen andere Deutungen s. u.); 
np. cust „flink, tatig, passend“, ai. skundate 5 ,eilt“ (Dhatup.) ; lit. skiidriis 
„flmk^3 alb. (G. Meyer BB. 14, 56, Alb. Wb. 150, Alb. St. Ill 90, Jokl. IF. 
36, 158f.) hed ^werfe; worfle das Getreide^^ (fiir ^Jied aus ^sqoudeio)\ 
abg. is-kydati „herauswerfen“, imma kydati ,j^?MO(pr}jU€iVj gnjpaoiv doep- 
votg pdXkeiv^^ (also nicht nach Hirt Abl. 102 zu '^qetid- „schi*eieu‘^), russ. 
kiddth „werfen‘S sja „eilen“, kidkij „rasch, gesch^vind, gleich bereit, gierig^* 
(usw., 8. Berneker 676, der auch lett. paktidti^ pakudindt ,jantreiben, an- 
sputen^* anreiht); gr. xvdiag' rd dvd)] rd)v odovKov Hes. (vgl. zur Bed. ahd. 
sco^ „Scho6, junger Spro6“); 

aisl. skjota „schleudern, vorstoBen, schieBen“, refl. „lossturmen'', ags. 
sceotan „werfeu, schiefien, schlagen, sto6en‘^, ahd. scio^an ^schiejien^ werfen, 
schnellend bewegen*^ mit zahlreichem germ. Zubehor (z. B. bei Pick III ^ 
467 f.), wie ahd. sco^ „GeschoB, Sch66Iing“ scu^ ^SchuB, ^Yurf, Schnellig- 
keit'^, aisl. skjotr^ ags. sceot „schnell“, got. skaiita d. sg. „(hervorschieBen- 
der) Zipfel oder Saum eines Kleides''', aisl. skaiit n. „Zipfel, Ecke, SchoB, 
Vorsprung“, ahd. sco^ „Zipfel, KleiderschoB, RockschoB^^ (s. auch Falk- 
Torp u. skjed^ skjede)^ mnd. schot{-tt-) „(Yorgeschobener) Riegel, Yerschlu6‘S 
wo von schiitten „abdammen, hindern, schutzen‘‘, mhd. nhd. schiltzen, Ohne 
anl. S’ mhd. hossen^ koUen „schnell laufen“, nhd. mdartl. hidzen „antreiben, 
hetzen“ (wie ai. cddati)^ auch ,,stoBen'" (ob so auch ai. kTiuddti „stoBt hinein, 
spez. penem"^ mit nach Johansson IF. 19, 125ff. vielleicht altem Ubergang 
von sk’ zu ai. M-? Dieselbe praegnante Bed. 5 ,futuere^‘ von dt. Tiotzen 
ist aber nach Luft KZ. 36, 146 anders entstanden). 

Yereinbare Bed., aber andern Dental zeigen ags. scudan^ scyndan^ aisl. 
skynda „eilen“, abg. skytatisq „Yagari‘‘, s. dariiber u. sqftt- „rutteln‘^ 

^Ygl. Zup. 9, 121, 127, 156 (Lit.), Falk-Torp u. skyde (Lit.), Berneker 
676, Boisacq 874 a 1; in zu weitem Zshange Johansson IF. 19, 125fF., Lewy 



(s)qeup', sqeub{h)- 


555 


PBrB. 32, 143. — Ai. codati nicht zu ^q^ed- „stachelii‘^ (z. B. Uhlenbeck 
Al Wb. 93, Ficklll^ 115, Falk-Torp u. hvas), da in der Vokalstellung 
unvereinbar (vgl. Zup. 9, 56, auch Fick 31); Umbildung etwa eines *ca- 
dati durch Reim auf Tisodati „8t66t“ (erwogen von Griintert Reimwortbild. 
23) wird durch up. ctist widerlegt; noch anders yerbindet Wood AlPh, 
27, 59 cMati mit mhd. luu^e „munter, frech'^ (dock s. dariiber u. qeud 
5 jSchreien“) und Cl. Phil. 5, 303 f. auSer mit slav. Tcydati auch mit got. 
gaJvatjan „anreizen‘’, ags. hweftan „wetzen, scharfen, anreizen“, aisl. huafa
```


## [2026-09-14T01:58:01.475Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\nls | head -30\npython3 -c \"\nimport json,glob\nf='page-385.json'\nd=json.load(open(f))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-14T01:58:02.625Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "w
```


## [2026-09-14T01:58:07.871Z] TOOL CALL #15: Bash

```json
{
 "command": "pdftoppm -f 456 -l 456 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456.png"
}
```


### [2026-09-14T01:58:09.696Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 33661 Sep 13 21:58 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456.png
```


## [2026-09-14T01:58:11.677Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456.png"
}
```


### [2026-09-14T01:58:12.315Z] TOOL RESULT

```

```


## [2026-09-14T01:58:12.304Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:58:27.158Z] TOOL CALL #17: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:58:27.206Z] TOOL RESULT

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


## [2026-09-14T01:58:31.958Z] TOOL CALL #18: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-14T01:58:32.009Z] TOOL RESULT

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


## [2026-09-14T01:58:36.662Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%DA%86%D8%B3%D8%AA\" \"https://en.wiktionary.org/wiki/shoot\" \"https://en.wiktionary.org/wiki/sheet\" \"https://en.wiktionary.org/wiki/shuttle\" \"https://www.etymonline.com/word/shoot\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/skeutan%C4%85\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 456, root Skeud 1, verification of čost/čodati and Germanic shoot/sheet/shuttle\" \ndone"
}
```


### [2026-09-14T01:58:42.383Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c750e927dbe98b08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96c1e6ace34fdf83.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74a41a48100b7ec0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59e4deb7d17832d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c643129035ef42f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/200efd7d8d8be27d.txt
```


## [2026-09-14T01:58:45.357Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== چست wikt ===\"; grep -n -A18 \"Persian\\[edit\\]\\|Etymology\" c750e927dbe98b08.txt | head -60\necho; echo \"=== PGmc skeutaną ===\"; head -c 2500 200efd7d8d8be27d.txt"
}
```


### [2026-09-14T01:58:45.457Z] TOOL RESULT

```
=== چست wikt ===
62: Etymology 
63-
64- 1.2 
65- Adjective 
66-
67- 1.2.1 
68- Descendants 
69-
70- 2 
71- Urdu 
72-
73- Toggle Urdu subsection 
74-
75- 2.1 
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Adjective 
83-
84- 2.4 
85- Further reading 
86-
87- Toggle the table of contents 
88-
89- چست 
90-
91- 7 languages 
92-
93- فارسی 
94- Bahasa Indonesia 
--
158: Etymology
159- [ edit ] 
160-
161- From Proto-Iranian *custáh , from Proto-Indo-Iranian *čutˢtás , from Proto-Indo-European *(s)kud-tó-s ( “ propelled ” ) , from *(s)kewd- ( “ to shoot, throw ” ) . Cognate with Sanskrit चोदति ( códati , “ to impel ” ) .
162-
163- Adjective
164- [ edit ] 
165-
166- چست • ( čost ) ( comparative چست‌تَر , superlative چست‌تَرین ) 
167-
168- quick 
169-
170- brisk 
171-
172- active 
173-
174- fleet 
175-
176- agile 
--
188: Etymology
189- [ edit ] 
190-
191- Borrowed from Classical Persian چُسْت ( čust ) .
192-
193- Pronunciation

=== PGmc skeutaną ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/skeutan%C4%85
FETCHED: 2026-09-14T01:58:42Z
STATUS: 200
TITLE: Reconstruction:Proto-Germanic/skeutaną - Wiktionary, the free dictionary

Reconstruction:Proto-Germanic/skeutaną - Wiktionary, the free dictionary 

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
 Proto-Germanic 

 Toggle Proto-Germanic subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Inflection 

 1.3.2 
 Derived terms 

 1.3.3 
 Related terms 

 1.3.4 
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Germanic/ skeutaną 

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

 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Germanic
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *(s)kewd- 

 Proto-Indo-European *-eti 

 Proto-Indo-European *(s)kéwdeti ? 

 Proto-Germanic *skuttōną bf. ? 

 Proto-Germanic *skeutaną 

 Traditionally derived from Proto-Indo-European *(s)kewd- ( “ to advance, propel ” ) , and compared with Albanian hedh ( “ to throw ” ) . [ 1 ] However, Kroonen prefers to take the word as a back-formation from the iterative verb *skuttōną ( “ to shoot ” ) [ 2 ] (whence Old Norse skotra ( “ to shove, push ” ) , Icelandic skota ( “ idem ” ) ), which he derives from a Proto-Indo-European *sket- ( “ to drive forward ” ) , and connects with Lithuanian skàsti ( “ to jump, hop ” ) , Latin scatō ( “ to gush forth, swarm ” ) . [ 3 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈskeu̯.tɑ.nɑ̃/ 

 Rhym
```


## [2026-09-14T01:58:56.689Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== shoot ===\"; grep -n \"Proto-Germanic\\|Old English scēotan\\|skeutan\" 96c1e6ace34fdf83.txt | head -12\necho \"=== sheet ===\"; grep -n \"skautijǭ\\|skautij\\|Proto-Germanic\" 74a41a48100b7ec0.txt | head -12\necho \"=== shuttle ===\"; grep -n \"skutil\\|Proto-Germanic\\|scytel\" 59e4deb7d17832d0.txt | head -12\necho \"=== etymonline shoot ===\"; grep -n -i \"skeud\\|Proto-Germanic\\|shut\\b\" 3c643129035ef42f.txt | head -12"
}
```


### [2026-09-14T01:58:56.802Z] TOOL RESULT

```
=== shoot ===
299: Proto-Germanic *skuttōną bf. ? 
301: Proto-Germanic *skeutaną 
302: Proto-West Germanic *skeutan 
307: Inherited from Middle English scheten , schoten , from Old English scēotan , from Proto-West Germanic *skeutan , from Proto-Germanic *skeutaną , from Proto-Indo-European *(s)kéwd-e-ti , thematic present of *(s)kewd- ( “ to shoot, throw ” ) .
1477: English terms derived from Proto-Germanic 
1483: English terms inherited from Proto-Germanic 
=== sheet ===
236: From Middle English schete ; partly from Old English sċīete ( “ a sheet, a piece of linen cloth ” ) ; partly from Old English sċēata ( “ a corner, angle; the lower corner of a sail, sheet ” ) ; and Old English sċēat ( “ a corner, angle ” ) ; all from Proto-Germanic *skautijǭ , *skautaz ( “ corner, wedge, lap ” ) , from Proto-Indo-European *(s)kewd- ( “ to throw, shoot, pursue, rush ” ) .
973: English terms derived from Proto-Germanic 
=== shuttle ===
237: Middle English shutel , schetil , shotil , shetel , schootyll , shutyll , schytle , scytyl ( “ missile; projectile; spear ” ) , from Old English sċytel , sċutel ( “ dart, arrow ” ) , from Proto-Germanic *skutilaz .
664: English terms inherited from Proto-Germanic 
665: English terms derived from Proto-Germanic 
=== etymonline shoot ===
27: This is reconstructed to be from Proto-Germanic *skeutanan (source also of Old Saxon skiotan , Old Norse skjota "to shoot with (a weapon); shoot, launch, push, shove quickly," Old Frisian skiata , Middle Dutch skieten , Dutch schieten , Old High German skiozan , German schießen ), often said to be from PIE root *skeud- "to shoot, chase, throw," but Boutkan gives it no IE etymology.
71: "to or toward a point or place higher than another," Old English up , uppe , from Proto-Germanic *upp- "up," from PIE root *upo "under," also "up from under," hence also "over." As a preposition, from late Old English as "down onto, above and touching, sitting on, at the summit of;" from c. 1200 as "to a higher place."
75: From the same Proto-Germanic source are Old Frisian, Old Saxon up "up, upward," Old Norse upp ; Danish, Dutch op ; Old High German uf , German auf "up;" Gothic iup "up, upward," uf "on, upon, under;" Old High German oba , German ob "over, above, on, upon."
103: "heavenly body which revolves about the earth monthly," Middle English mone, from Old English mona, from Proto-Germanic *menon- (source also of Old Saxon and Old High German mano, Old Frisian mona, Old Norse mani, Danish maane, Dutch maan, German Mond, Gothic mena "moon"), from P
115: , "feed on buds, eat leaves or twigs from" trees or bushes, from Old French broster "to sprout, bud," from brost "young shoot..., twig, green food fit for cattle or deer," probably from Proto-Germanic *brust- "bud, shoot," from PIE *bhreus- "to swell...
119: contempt" (c. 1600, now obsolete), of Scandinavian origin (compare Old Norse skuta, skute "to taunt"), from skotja "to shoot...notion of a "shooting of words"), which according to Watkins is from a Proto-Germanic *skut- from PIE root *skeud- "to shoot...
127: Old English spir "a sprout or shoot of a plant, spike, blade, tapering stalk of grass," from Proto-Germanic *spiraz (source...also of Old Norse spira "a stalk, slender tree," Dutch spier "shoot, blade of grass," Middle Low German spir "a small point...
135: Old English tima "limited space of time," from Proto-Germanic *timon- "time" (source also of Old Norse timi "time, proper time," Swedish timme "an hour"), from PIE *di-mon-, suffixed form of root *da- "to divide." The abstract sense of "time as an indefinite continuous duration" 
139: "tiny animal, minute arachnid," Old English mite "minute, parasitic insect or arachnid," from Proto-Germanic *miton (source also of Middle Dutch mite, Dutch mijt, Old High German miza, Danish mide) meaning originally perhaps "the cutter," in reference to its bite, from Proto-Germ
```


## [2026-09-14T01:59:05.785Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1/2 چست ===\"; grep -n \"چست\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== ARY latin index CUST/CHUST ===\"; grep -n -i \"cust\\|čust\\|chost\" incoming/ARY/ARY_latin_index_pages.txt | head -15\necho \"=== ARY fa چست ===\"; grep -n \"چست\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T01:59:05.889Z] TOOL RESULT

```
=== MON part1/2 چست ===
MON_part2.txt:8847:بلوچستان به مقدار زیاد می‌روید؛ فندق 
MON_part2.txt:11051:کسی. قباء در برگردانیدن: راست و چست 
MON_part2.txt:11159:قبرای: 072۷« [تر.] (ص.) چابک» چست: 
MON_part2.txt:14277:قلقل: ۱۰۷۰۱/۵۱۱ [ع.) (ص.) مرد چست 
MON_part2.txt:18082:چست و چالا ک (در رفتار؛ برداشتن بار و 
MON_part2.txt:19595:خرماه آنجا که به نخل چستیل ۵. 
MON_part2.txt:21589:بلو چستان به فراوانی می‌روبد. از دانه‌هایش 
MON_part2.txt:39093:رخوء بحال؛ مق. چست. جابکك. تنبل و 
MON_part2.txt:44163:+ یت س. مص جهع. | (.) چستی» حقبقت» 
MON_part2.txt:57126:سرشت؛ طبیعت. نژاد. مرد چست و سبکث 
=== ARY latin index CUST/CHUST ===
=== ARY fa چست ===
6566:۴ | چست (به چم ۰
```


## [2026-09-14T01:59:10.079Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6550,6590p' incoming/ARY/ARY_pages.txt\necho \"=== which pdf page ===\"; awk 'NR<=6566 && /\\[pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T01:59:11.431Z] TOOL RESULT

```
آلمانی (0727//۸4)(سویس) دا لغت‌نامه دهخدا: ۸۳۲
پارسی باستان (0۷فای۲8 01): ۰ ۳178۸11* دا
افغانی (پشتو) (۸۳0/۸۸): آلمانی (7ف/ل057): نود( انا
۸7 ,0۸8۳ انگلیسی کهن (3/ا2۸6 0ا0): 11888۸7۲
سانسکریت (5۸/567): ۲۸71شط ,۲۸۲737 انگلیسی (ل87لا8(/0): اد را ادا :۱
یونانی (0280): ۰ ۴۳086 ,77310شز دانمارکی (0۸//574): دنا
لاتین (471ا): سوئدی (5(7521/577): 1۸
کوب ماهت اف کقن تروژی (49۷ا۵۷070۷50: 1
گرتیکه (2۶4/0م 6" 1۸0 هلندی (00707): 1
ایسلندی کهن (74(7 5۸010۸ 00): لیترانی (4()لهنالل7لم: 0۳۸
1۸ لنونی (لتی) (701۵01ل): 0/7
نورس کهن (۸0785 0ا0): 1۸ ایرلندی کهن (#زکل#ا 2ا0): ۰ ۲۸037
ساکسونی کهن (/(84200 0): 118881۸0 ولزی (ل0851-87): 3 دی
فریزی کهن (۷فا5ل۲ صا0): 1۸ آلبانی (/۸انمقلم. ۱
آلمانی کهن (/(028۵/۸ 2/04 صاه):
[pdf page 223]
۴ | چست (به چم ۰
پسگشت‌ها رد ند 3 (138۸۷8) 00/5
زر 1 سا یا :37
2 (118۸۷8) +8۸17 برهان قاطع + 1 ۶۳۷
یادداشت: : ۱ 31
۱- واژه‌های "چسب" و "چسباندن" و غیره هم از همین ریشه‌اند.
۲ چم اين واژه در زبان‌های ژرمنی کهن "گرفتن" برده ولی در زبان‌های ژرمی نوین چم آن اپا زور بلند کردن*
است.
۳ چم این واژه در زبان‌های لاتین و -لنی؛ اسیر گرفتن.
پهلری (1/ا7ل۳۸): ۷0 7 ,50307۸
کردی (0801/57)): لا اه روسی (7854(7): 1۵7 ,نا 1610۸3
مانسکریت (54(/98/7): ,010 ,۲32۸71 لینرانی (/7۸(ولال7ل):
6 ۲532۸۷۸7 5 85701708178
گرتیکد (007[710): 7اه آعونی (لتی) (4777۸27): نی زاره 0
ایسلندی کهن (۵(7ا0/۸/نش5 صا۵): آلبانی (7لمالمقلم: 1
م87(071۸
آلمانی کهن ((088۸1۸ 0 انز صها0): پسگشت‌ها ان رد ادن دا
7 501072۸ 6 2000
آلمانی (/024۸): ند مرا هن 3 (۴۸81) ۸
انگلیسی کهن (4ل9ا.ا8۸0 010): برهان قاطع : ۶۳۶
بادداشت:
چم این واژه در زبان سانسکریت: راندن» شتاپیدن,
چم این واژه در زبان پهلوی: دویدن؛ شتابیدن,
: چم اين واژه در زبان آلمانی: حفظ و حراست کردن.
[pdf page 224]
=== which pdf page ===
[pdf page 223]
```


## [2026-09-14T01:59:21.453Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (610,611,612):\n    p=pages[i]\n    print('--- leaf',i,'---')\n    print(p[:1200])\nEOF"
}
```


### [2026-09-14T01:59:22.543Z] TOOL RESULT

```
Exit code 1
434
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-14T01:59:24.729Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"qeud\\|(s)qeud\\|codati\" POK_03.txt | head -20"
}
```


### [2026-09-14T01:59:24.787Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:59:27.055Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n -i \"skundate\\|cödati\\|codati\\|skjota\" $f | head -5; done"
}
```


### [2026-09-14T01:59:28.170Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
4686:wahrscheinlich  lat.  tri-quetrus  , dreieckig*  (,dreispitzig' ;  wohl  aus  *tri- quedros)]  möglicherweise  auch  ai.  cödati,  cöddyati  ,treibt  an,  drängt* i^keud-).
== POK_03.txt
2595:schießen*. Ai.   cödati,  cöddyati  ,treibt   an,    drängt*,   np.   cust  ,flink,   tätig,   passend*, ai.  skundate  ,eilt*  (Dhätup.);
2599:ohne  anlaut.  s- :  mhd.  hossen,  hotzen  , schnell  laufen',  nhd.  dial.  hntzttk ,antreiben,  hetzen'  (wie  ai.  cödati),  auch  , stoßen';
```


## [2026-09-14T01:59:31.666Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='POK_03.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:2594])\nleaf=t[:idx].count('\\f')\nprint('leaf',leaf,'-> printed approx',leaf+762,'to',leaf+766)\npages=t.split('\\f')\nprint(pages[leaf][:2200])\nEOF"
}
```


### [2026-09-14T01:59:32.849Z] TOOL RESULT

```
leaf 196 -> printed approx 958 to 962
56,  Trautmann  263,  Wissmann  Nom.  postverb.  128,  177  f. und  Skop  BSB.  1954,  2.
1.  skeud-  ,unwillig,  mürrisch  sein',  im  Balt.  auch  von  körperlichem  Schmerze.
Gr.  Gxvd(.iaiva),  'oy,v^oiJ,ca  , zürne,  grolle*,  ay-v^gög  (diss.  aus  ^a-üvö-S-QÖg) ,mürrisch,  unwillig,  traurig*,  ay.vd-QCx)7T6g  ds.,  OKv-d-QaLo)  ,bin  unwillig';
lit.  pra-skunditj  -skudaii,  -sküsti  ,zu  schmerzen,  zu  ermüden  anfangen', skundä  , Anklage*,  praskundä  , Schmerz*,  nüoskunda  , Mitleid*,  skündziu, ski^sti  , sich,  beklagen*;  lett.  skund-u,  -et  , mißgünstig,  neidisch  sein,  zürnen*; lit.  skaudüs  ,schmerzhaft,  verdrießlich,  heftig*,  skausta  (skaudeti)  ,es schmerzt',  lett.  skäuzu,  skäust  , neidisch  sein,  schädigen*,  skaudet  ds. ;  lit. skaudulys  , Geschwür'.
WP.  II  554;  vgl.  auch  keu9d-  oben  S.  595  f.
2.  (s)keud-  , werfen,  schießen,  hetzen*;   intr.   ,dahinschießen,  eilen,   hervor-
schießen*. Ai.   cödati,  cöddyati  ,treibt   an,    drängt*,   np.   cust  ,flink,   tätig,   passend*, ai.  skundate  ,eilt*  (Dhätup.);
956
gr.  xvdlag  ,ZahnkeimS  Hes.(?);  alb.  heth  ,werfe,  worfle'  (für  Hedk  an, *skoudeiö  ?) ;
aisl.  sJcjöta,  ags.  sceotan  ^schleudern,  stoßen,  schießen',  ahd.  sciozq^ ,schipßen,  werfen,  schnellend  bewegen';  ahd.  scoz  ^Geschoß,  SchößÜn»«  " scuz  , Schuß,  Wurf,  Schnelligkeit',  aisl.  skjöir,  ags.  sceot  ^schnell«,  »ot skaut  , Schoß,  Saum^  aisl.  slcaut  n.  ,Zipfel,  Ecke,  Schoß,  Vorsprung',  ahd  m scöz  , Zipfel,  Kleiderschoß,  Rockschoß',  mnd.  schott  (-U-)  ^(vorgeschobener)  .J Riegel,  Verschluß^  wovon  schütten  , abdämmen,  hindern,  schützen',  mlj^  ,  J nhd.  schützen]
ohne  anlaut.  s- :  mhd.  hossen,  hotzen  , schnell  laufen',  nhd.  dial.  hntzttk ,antreiben,  hetzen'  (wie  ai.  cödati),  auch  , stoßen';
lit.  shudriXs,  skaudrüs  ,flink';  lett.  skaudrs  ds.,  skudra  , Ameise';  aksl. is-kydati  , herauswerfen',  russ.  kiddth  , werfen*,  kidkij  , rasch,  bereit,  gieri»"*^
WP.  II  554 f.;  s.  auch  unter  5.  skeu-  und  skeub-,
(s)keup-,  skeub(h)-  , Büschel,  Schopf,  Quaste';  nur  gerin.  und  slav.
Aisl.  skauf  ,Büschel,  Quaste',
```


## [2026-09-14T01:59:41.653Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== HUB öust ==\"; grep -n \"öust\\|cust\\b\\|6ust\" HUB.txt | head -10\necho \"== PHD cust ==\"; grep -n -i \"^cust\\|cust \\|čust\\|cwst\" PHD.txt PHD_mackenzie.txt | head -10\necho \"== NYB ==\"; grep -n -i \"cust\\|čust\" NYB_vol2_glossary.txt | head -10\necho \"== SYN quick ==\"; grep -n -i \"np. cust\\|cust 'flink\" SYN.txt | head"
}
```


### [2026-09-14T01:59:41.944Z] TOOL RESULT

```
== HUB öust ==
== PHD cust ==
PHD.txt:2655:locust kullag, mayg.
PHD_mackenzie.txt:5503:wizostan, wizoh/y- [wcwstn l , wcwd- I (J bzwb-, N piziJhidan)] examine,
PHD_mackenzie.txt:7017:locust kullag, mayg.                     majestic rayomand.
== NYB ==
331:āivēn ['dwyn'] rites, customs 818; cas.obl. —-E [+1] nāmak 121%, the Sassanian code of courteous manners and conduct, NP dīn-nāmah, often referred to by Mus- lim authors. — < OIr "abi-dayana- from "day- (v. dītan),. whence NW-Prth ab- den, but SW-Prs *aibiden > *aiviyén .> diven. — KZŠPrth 1. 19 "bdyn = Prs l. 24 *dwyn, Gr. v. #00¢; Ps. ’dwyny translating Syr. nāmēsā = the Mosaic Law; MPrth 'bdyn ‘habit, custom’ (Hen- ning, TPhS 1944, 110-112); Arm. lw. aurēn-k* ‘institution, the Law ; the Eucha- rist’; Syr. lw. b-abden ‘similar to’, cf also hämöden; Paz. NP Gin, Skr. v. äcära; Arab. lw. °@in. V. Markwart, UJ VII, 1927, 89-121; Junker, WuS XII, 1919, 150.
1210:dastavar [dstwbl], cas. obl. dastavareh [dstwblyh] 9815 : 1. valid religious doctrine, custom, law 10871; canon of religious doctrines etc. 109°; decision (of a relig- gious authority): pat ~ % oi 101%; <pat> ~ + Hušetar 96; pat hàn à Husetarmäh ~-éh 9814-15, — 2. an expert in religious matters, a theologian, a Dastur, also of the Zoroastrian clergy in general: a theo- logian 1018; x“atai u dahyupat u sardār u ~ + den 1081-2; pl. cas. obl.: ~-dn u dätavarän u hérpatàn u magupatān u den- burtärän 107'3-14, — MPrs dstwr ‘a priest’ (S); Paz. dastūr, Skr. v. ācārya, guru; NP dastür in profane senses (v. Steingass). — dast- from Av. (746) dqh- ‘to teach’, cf (745) dqstvà ‘religious doctrine’; hence MPrth dst ‘able, skilful? (A-H III). Cf Bailey, ZP 160, n. 5; TPhS 1945, 8.
1266:dépahr [dyp’hl] anger; pat ~ dästan (to hold in anger =) to keep in custody, to arrest 2170-24, — MPrth dybhr or tybhr ‘anger’; dybhrg tybhrg, ‘banished’ (MHC); Arm. lw. dipah ‘arrest; guard-room’, % di- pahoj dnel or arkanel ‘to place in arrest, to throw into prison’. V. Henning in MHC s. v. dybhrg.
2705:nihan [nyh’n'] secrecy; a secret place, a hiding-place: pat ~ secretly 5? etc.; hac ~ from an ambush 259; ~ kartan to hide 10?3; õi ~ be dätan to put aside in safe custody 4219; pat ~ dāštan to con- ceal 165-24-25 (hac from); ~ ravisn, -nēh v. these ws. — Cf Av. (1082) ničate-. Paz. niha, NP nihan.
2719:nikah [nk’s] look, glance, observation; custody, care: ~ kartan to look on, to watch 152. 259.24, 2726. 2817; ~~ daštan to notice, to observe, to pay attention to 108%. 12114; apar ~ dāštan to keep in safe custody 4112. — MPrth ng’h ‘look, attention’, n. kyrdn ‘to notice’ (A-H ITT); Paz. nagäh, NP nigäh; < Olr "ni-kada- from kà-, v. ākāh. Another derivative was "niš-ka0a- > Milr *niškāh ‘contempt’, preserved in Arm nškah-em ‘to reject, to condemn’. Cf also Arm nkat linel or nkat-em ‘to see, to consider, to contem- plate’ from MIr *nikät < Olr *nikātā, nom. sg. of the nomen actoris *nikätar- ‘contemplator’. The pt. pass. *nekāta- is found in the name of the 15th nask (q. v.) of the Sas. Avesta: N?kütom [nyk”- twm] = Av. *nikätem ‘that which is observed (in medical matters)’.
2720:nikäh-däreh [-d’lyh] custody, safekeep- ing 82%.
2749:nipēk [npyk'] document, codex, book, pl. ~-ihā 108°. 1097. 1112-917. 1128. — < *ni-paya-ka- ‘that which is kept, or is to be kept, in safe custody’, ‘record’, originally an administrative term; MPrth Prs nbyg; Paz. nevé, nivé. From Av. (886) ni-pãy- (pres. also pay-). — Bthl’s ety- mology: nipčk < "nipčhak < *ni-paida- ka- from a SW form of nipištan (MirM IV, 30, n. 2) is untenable.
3279:raväk [lwb’k'] running, going on, current: ~ kartan to put into circulation, to dis- : seminate. 8015, 1072, — From raftan (g. v.); Paz. ravā, Skr. v. pravartamāna (Mx), pravrtta (SGV); NP ravä ‘current (coin), lawful, admissible’; Arab. lw. ravāj < raväg ‘current (money), vendible (goods); use, custom’.
3320:2ristak [lystk', Istk'] 1. custom, rule, law: v. yuvat-ristak. — 2. adj. firm, reliable, truthful 1101’; sup. ~-tom 59", cf ristake- nitan. — From Av. rād-, v. s. v. patrāstak and ef rdyénitan; MPrth pt. ryst ‘exact, correct’, Ghilain 60; Paz. subst. (SGV) rastaa ‘law, element’ (= Gr ototxetov, thus de Menasce); NP rast ‘firm, steady’, rastah ‘rule, institute, market’; Talm lw. rystq? ‘market-place’, Telegdi 255.
3599:šāk [š*k'] branch 3118; pl. cas. obl. šākān (or šārān) [š*hn'] 40%, — NP sax; an alternation -k: -x, -h is found in several ws: BP sūlāk (q.v.): NP siuldr; BP malak (FrP 8): NP malax ‘locust’; Av. (1114) maóaxa-, Arm. lw. marax id.: NP maig < *maóaka-; BP zanak (q. v.): NP zanax. — Bal šah ‘horn’. (Not identical with Skr säkhä).
== SYN quick ==
```


## [2026-09-14T01:59:54.671Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"shoot,  verb\\|^shoot\\|shoot\\. \" SKT.txt | head -5\ngrep -n \"sheet\\.\\|shut\\.\" SKT.txt | head -6\necho \"=== KLN shut ===\"; grep -n \"^shut\\|shut,  tr\" KLN_1966.txt | head -5\ngrep -n \"scyttan\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T01:59:54.787Z] TOOL RESULT

```
3552:cliff,  a  Bleep  rock,  headland.  (£.)   A.S. €Hf  a  rock,  cliff  +Du.  and  Iccl.  klif,  Cf.  G. and    Dan.    klippe,   Swed.   kllpfa,    a    crag. Orig.   sense    prob.    '  a    climbing-place,*    a steep :   Kc  Climb.  Clip.     ^  It  canMoi  be allied  to  r/^oiv  (1). Clof :  see  Clariole. Cloft  :  sec  Cleave  (i). Cleinatla.  a  plant  (Gk.)     Gk.  MXintarts, tlrush-wood,  creeping- plant  wGk.  K^nftar-, stem  of  KKi}iMy  a  shoot.  twig.«»Gk.  «Ad«»'. to  brcAk  off,  ptuac
14152:—  L.  ptanta,  a  plant ;  propcrifi  • sucker  or  shoot.  From  wm  hmt plaioe  (aboveV
17159:•hut.  (K.)  M.  E.  shutUtf,  tkittm. AS.  tfyttan.  to  shut;  to  fasten  a  door with  a  bolt  (called  a  shuttU).  We  still my  '  to  xAodt  a  bolt*  1  he  A.  S.  u^/Zom U  a  weak  veib;  from  scm/-,  base  of  pt.  t pi.  of  ueJfUH,  to  shoot.  •^  Du.  uhu/tnt, G,  /T'^u/.i/M  (similarly  formed).    See  bel.ow.
17165:Swetl.    sk/uta,   to   shoot.     CI.  Swcd.
3528:ooncUide.  (L.)  L  eondudert,  to  shut up,  close,  end.  — L  f<Mr-(<'i#jn),  together  :  aikI •dMiUrt  =  dauJett,  to  shut.  Der.  condus' UH.  Similarly  es-dude,  in-elude,  prt-dmJe, Si-dud*;  whence  in-duj-tve,  prt-dus-wfty te-duxiou  (from  pp,  -<iusus  ^  cfausus) .
3530:sluice,  a  floodgate.  ^F.-L.)  O,  F- esdujt,  *  a,  sluce,  floudgate ;  *  Cot.  —  Low L  txduia,  a  Dood-gate ;  lit.  shut  oil (water) ;  pp.  of  tjc-tludtre,  to  shut  out.*> L.  ex,  out ;  daudere^  to  shut.
5491:duwieolino.  (L.)    /m  t/tut£entm» 12  leaves  to  the  sheet.  — L.  dk of   duodecimus^    twelfth.  —  U twelve ;  see  doftea  above.
13318:forms,  in  the  same  sense.  (Cf.  G.  sperrtn, to  shut.)  The  verb,  meaning  *  to  fasten with  a  spar  ot  bar/  is  formed  from  the  sb. Bpar  ( 0.  q.  v.  p.  The  word  is  common to  Teutonic  tongues ;  as  in  Du./Vr^,  Sued. Dan.  park,  G.  p/crck,  whence  not  only  F. part,  Ital.  parvo.  Span,  parque,  but  also Irish  and  Gael,  pairc,  W.  pari  and  paru*g (  -  E.  parrot),  Bret.  park.
17154:sheet.  (E,>  M  E.  schtte.  A.  S.  scitt, fcyte,  a  sheet ;  also  scedt^  a  corner,  nook,  fold Oi  B  garment,  comer  of  a  sail,  hence  a  shtit or  rope  fastened  to  a  comer  of  a  sail.  —  A.  S. JTtfJ/,  pp.  of  teeitan^  10  shoot,  hence  to  jut out  The  orig.  sense  of  sktft  was  '  pro- }ecl Ion,*  hence 'comer,' Sec  +  Icel./iau/, corner,  shed  of  a  sail;   Swcd.  tkot  (the
=== KLN shut ===
35098:Derivatives :  shunt,  n.,  shunt-er,  n.,  shunl-ing,  n. shut,  tr.  and  intr.  v.  —  ME.  schitten,  schutten, shutten,  fr.  OE.  scyttan,  ‘to  shut’;  prob.  rel.  to shoot.  For  sense  development  cp.  the  phrase  ‘to shoot  a  bolt’.  Cp  next  word.  Cp.  also  the  second element  in  wainscot.
35100:shuttle,  n.  —  ME.  sehytel,  fr.  OE.  scytel,  ‘missile, dart’,  a  gradational  variant  formed  from  the stem  of  sceotan,  ‘to  shoot’;  so  called  from  its being  ‘shot’  across  the  threads  in  weaving.  See shoot  and  dimin.  suff.  -le  and  cp.  prec.  word. Cp.  also  skittle,  which  is  a  doublet  of  shuttle. Derivative:  shuttle,  tr.  and  intr.  v. shwa,  n.  —  A  var.  of  schwa, shy,  adj.,  timid;  bashful.  —  ME.  schey,  shey, ‘shy’,  fr.  OE.  sceoh,  ‘timid’,  rel.  to  MLG. schii(we),  Du.  schuw,  ‘shy’,  MHG.  schiech,  G. scheu,  of  s.m.,  OHG.  sciuhen,  MHG.  schiuhen, ‘to  shy  at,  to  fear’,  G.  scheuchen,  ‘to  scare away’.  The  only  non-Teutonic  cognate  is OSlav.  siuti,  ‘to  hunt,  incite’.  It.  schivare,  ‘to avoid’,  is  a  Teut.  loan  word.  Cp.  eschew. Derivatives :  shy,  intr.  v.,  shy-er,  n.,  shy-ly,  adv., shy-ness,  n.
35098:Derivatives :  shunt,  n.,  shunt-er,  n.,  shunl-ing,  n. shut,  tr.  and  intr.  v.  —  ME.  schitten,  schutten, shutten,  fr.  OE.  scyttan,  ‘to  shut’;  prob.  rel.  to shoot.  For  sense  development  cp.  the  phrase  ‘to shoot  a  bolt’.  Cp  next  word.  Cp.  also  the  second element  in  wainscot.
```


## [2026-09-14T02:00:09.952Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 456 -l 456 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg456hi\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg456hi.png')\nprint(im.size)\nw,h=im.size\n# germanic box region approx: x 0.21-0.45, y 0.185-0.24 of page (based on 200dpi view)\nbox=(int(w*0.20),int(h*0.180),int(w*0.46),int(h*0.245))\nim.crop(box).resize((int((box[2]-box[0])*1.6),int((box[3]-box[1])*1.6)),Image.LANCZOS).save('pg456-germ.png')\nEOF\nls -la pg456-germ.png"
}
```


### [2026-09-14T02:00:13.005Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 102312 Sep 13 22:00 pg456-germ.png
```


## [2026-09-14T02:00:15.086Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456-germ.png"
}
```


### [2026-09-14T02:00:15.109Z] TOOL RESULT

```

```


## [2026-09-14T02:00:41.776Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-\" --note \"page 456, root Skeud 1 (PIE *(s)kewd-)\" \npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/shut\" --note \"page 456, English node #4, shut < OE scyttan\"\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg456.png data/verification/sources/refs/ocr/BOOK/456.png\nls -la data/verification/sources/refs/ocr/BOOK/456.png"
}
```


### [2026-09-14T02:00:44.408Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5f0ec0ae18620abe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b46b80d1154e410f.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 33661 Sep 13 22:00 data/verification/sources/refs/ocr/BOOK/456.png
```


## [2026-09-14T02:00:47.875Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A4 \"Proto-Indo-European\\[edit\\]\\|Root\\[edit\\]\\|Descendants\" 5f0ec0ae18620abe.txt | sed -n '1,40p'\necho \"=== shut ===\"; grep -n \"scyttan\\|skutjan\\|Proto-Germanic \\*\" b46b80d1154e410f.txt | head -6"
}
```


### [2026-09-14T02:00:47.952Z] TOOL RESULT

```
=== shut ===
237: From Middle English schitten , schetten , from Old English sċyttan ( “ to cause rapid movement, shoot a bolt, shut, bolt ” ) , from Proto-West Germanic *skuttjan , from Proto-Germanic *skutjaną , *skuttijaną ( “ to bar, bolt ” ) , from Proto-Germanic *skuttą , *skuttjō ( “ bar, bolt, shed ” ) , from Proto-Indo-European *(s)kewd- ( “ to drive, fall upon, rush ” ) . The Modern English word was originally a dialect form; the Old English word would have normally merged with shit .
488: Old English: scyttan
```


## [2026-09-14T02:00:52.685Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -8 5f0ec0ae18620abe.txt; wc -c 5f0ec0ae18620abe.txt; grep -n -i \"kewd\" 5f0ec0ae18620abe.txt | head -5"
}
```


### [2026-09-14T02:00:52.788Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-
FETCHED: 2026-09-14T02:00:43Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/(s)kewd- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/(s)kewd- - Wiktionary, the free dictionary 

 Jump to content 
4425 5f0ec0ae18620abe.txt
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-
4:TITLE: Reconstruction:Proto-Indo-European/(s)kewd- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/(s)kewd- - Wiktionary, the free dictionary 
72: Reconstruction:Proto-Indo-European/ (s)kewd- 
134: *(s)kewd- [ 1 ] [ 2 ]
```


## [2026-09-14T02:00:54.954Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '125,175p' 5f0ec0ae18620abe.txt"
}
```


### [2026-09-14T02:00:55.016Z] TOOL RESULT

```
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *(s)kewd- [ 1 ] [ 2 ] 

 to advance , push 

 to drive , propel 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *(s)kewd- (32 c, 0 e) 

 *(s)kéwd-e-ti ~ *(s)kéwd-o-nti ( thematic root present ) [ 2 ] 
 Proto-Indo-Iranian: *čáwdati 
 Proto-Indo-Aryan: *ćáwdati 
 Sanskrit: चोदति ( codati ) ( see there for further descendants )

 > ? Proto-Albanian: [ 2 ] 
 Proto-Albanian: *skeuda [ 3 ] 
 Albanian: hedh ( “ to throw ” ) 

 > ? Proto-Germanic: *skeutaną ( “ to shoot ” ) ( disputed [ 4 ] ) ( see there for further descendants )

 *(s)kud-tó-s ( “ propelled ” ) 
 Proto-Indo-Iranian: *čutˢtás 
 Proto-Iranian: *custáh 
 Persian: چست ( čost , “ quick, active ” ) 

 *(s)kud-eh₂-yé-ti 
 Proto-Balto-Slavic: *kūˀdā́ˀtei 
 Latvian: kûdît , kûdinât ( “ to drive, to urge ” ) ( possibly ) 

 Lithuanian: skiautė , skutai 

 Proto-Slavic: *kydati   impf , *kydnǫti   pf ( see there for further descendants )

 Proto-Germanic: *huttōną ( “ to run ” ) ( see there for further descendants )

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ 2. (s)keud- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 955
```


## [2026-09-14T02:04:43.445Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ndata = {\n \"pdf_page\": 456,\n \"book_page\": 426,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Skeud 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *(s)kewd- 'to throw, shoot, drive, propel' (Pokorny 955-956, '2. (s)keud- werfen, schießen, hetzen'; Watkins/AHD 'skeud-. To shoot, chase, throw.')\",\n   \"note\": \"The root is real, the language label ('Indo-European' = PIE) is right and the gloss 'to throw, shoot' is Pokorny's own ('werfen, schießen, hetzen; intr. dahinschießen, eilen'). Nourai's numbering is the mirror image of Pokorny's: Pokorny p.955 prints '1. skeud- unwillig, mürrisch sein' and '2. (s)keud- werfen, schießen, hetzen', whereas Nourai's 'Skeud 1' is Pokorny's no. 2 and his 'Skeud 2' is Pokorny's no. 1. The redirect 'Skeud 2 -> Keued' is not an invention either: under 1. skeud- Pokorny himself writes 'WP. II 554; vgl. auch keuəd- oben S. 595 f.', so Nourai simply follows Pokorny's cross-reference (that entry is skipped here as a redirect). LIV 560 and Cheung (ESIV) both keep the root as *(s)keud- 'to shoot, impel'. The one substantive caveat concerns the Germanic branch: Kroonen (EDPG) and Boutkan detach Gmc. *skeutaną from this root, so the root itself is secure but its Germanic membership is now debated (see node #3).\",\n   \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *(s)kewd- «افکندن، پرتاب کردن، راندن» است که پوکورنی آن را در صفحهٔ ۹۵۵–۹۵۶ فرهنگ خود با معنای werfen, schießen, hetzen آورده است؛ پس هم برچسب زبانی و هم معنای دادهٔ نورایی درست است. تنها نکته این است که شماره‌گذاری نورایی وارونهٔ شماره‌گذاری پوکورنی است: «Skeud 1» نورایی همان «۲. (s)keud-» پوکورنی است و «Skeud 2» او همان «۱. skeud-» به معنای «ناخرسند و ترشرو بودن»؛ ارجاع «Skeud 2 ← Keued» نیز برگرفته از یادداشت خودِ پوکورنی است که همان‌جا به keuəd- در صفحهٔ ۵۹۵ ارجاع می‌دهد. چونگ و LIV نیز همین ریشه را با همین معنا ثبت کرده‌اند. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ تنها پیوستگی شاخهٔ ژرمنی به این ریشه در پژوهش‌های تازه (کرونن، بوتکان) محل بحث است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:955\",\n     \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p.955 (local POK_03.txt, form-feed leaf 196; the scan shows the page-break numeral '956' inside the entry, so it begins on 955): '2. (s)keud- ,werfen, schießen, hetzen'; intr. ,dahinschießen, eilen, hervorschießen'. Ai. cōdati, cōdáyati ,treibt an, drängt', np. čust ,flink, tätig, passend', ai. skundate ,eilt' (Dhātup.) ... aisl. skjóta, ags. sceotan ... WP. II 554 f.' Exactly Nourai's root gloss, and the page number is exact.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"POK\",\n     \"where\": \"IEW 955-956 (POK_03.txt leaf 196; POK_full.txt line 76637)\",\n     \"stance\": \"supports\",\n     \"note\": \"'Root / lemma: (s)keud-2 | Meaning: to throw, shoot | ... Page(s): 955-956'. Note the immediately preceding lemma 'skeud-1 to protest, grumble ... See also: compare also keuəd- above S. 595 f.', which is the source of Nourai's 'Skeud 2 -> Keued' redirect.\"\n    },\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny II 554-555 (WLD_Bd2_1927_dli_106624_djvu.txt lines 35970-36013)\",\n     \"stance\": \"supports\",\n     \"note\": \"'3. (s)qeud- „werfen, schießen, hetzen“; intr. „dahinschießen, eilen, hervorschießen“. Ai. codati, codāpati „treibt an, drängt“; np. cust „flink, tätig, passend“, ai. skundate „eilt“ (Dhātup.)' — same root, same gloss, same two members Nourai puts in the chart.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, s.v. skeud- (AHD_watkins1985.txt line 943)\",\n     \"stance\": \"supports\",\n     \"note\": \"'skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot ... [Pok. 2. (s)keud- 956.]' — Watkins's gloss is Nourai's 'to throw, shoot'.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, IE Comparative Dictionary, s.v. skeud- (IEC.txt line 15612)\",\n     \"stance\": \"supports\",\n     \"note\": \"'skeud- \\\"fling, shoot, impel.\\\" (Variant: skheud- in Skt.) Skt. Codami, v. \\\"egg on; hurry\\\"; Alb. hudh, v. \\\"fling\\\"; OHG skiozan, OS skiotan, OE scéotan, sv. 2 \\\"shoot\\\" ... WP II' — same root, same two branches.\"\n    },\n    {\n     \"src\": \"CHEUNG\",\n     \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *Čaud (CHEUNG.txt line 3570)\",\n     \"stance\": \"supports\",\n     \"note\": \"'*Čaud \\\"to urge to, impel\\\" ... PIE *(s)keud- \\\"to shoot, impel\\\" = LIV: 560 | Pok.: 955 f., 636' — the current standard Iranian handbook keeps Pokorny's root and page.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"čodatî\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit cṓdati (3sg. pres.), caus. codáyati 'drives on, impels, incites, urges' (root cud-, attested from the Rigveda on) is the thematic root present *(s)kéwd-e-ti of the root, via Proto-Indo-Iranian *čáwdati: PIE initial *k- before the front vowel of the full grade *kewd- was palatalised to Indo-Iranian *č- (the 'first palatalisation'), giving Skt. c- [tʃ], while the s-mobile variant without palatalisation survives beside it in Skt. skundate 'hastens' (Dhātupāṭha), which Pokorny quotes in the same line. Nourai's transliteration 'čodatî' is his usual rendering of cṓdati (č for Sanskrit c, and the circumflexed final vowel for the accented/long mark in Pokorny's 'cōdati'); the word, its language and its gloss 'to hurry, propel' are all correct — Pokorny glosses it 'treibt an, drängt'.\",\n     \"derivation_fa\": \"واژهٔ سنسکریت cṓdati (و ساختِ سببیِ codáyati) به معنای «راندن، برانگیختن، شتاباندن» از ستاک cud- است و از ریگ‌ودا به بعد گواهی شده است. این صورت همان زمان حالِ درون‌مایه‌ایِ ریشه، یعنی *(s)kéwd-e-ti، است که از راه هندوایرانی آغازین *čáwdati به سنسکریت رسیده: k هندواروپایی پیش از واکهٔ پیشینِ درجهٔ کاملِ *kewd- بر اثر «کام‌شدگیِ نخست» به č بدل شده و در سنسکریت c خوانده می‌شود؛ گونهٔ دارای s آغازین بی‌کام‌شدگی نیز در همان زبان با skundate «می‌شتابد» بر جای مانده است. آوانویسی «čodatî» در کتاب همان cṓdati است و واژه، زبان و معنای آن درست ثبت شده؛ ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:955\",\n       \"status\": \"supports\",\n       \"note\": \"POK_03.txt leaf 196 (= IEW 955): 'Ai. cōdati, cōdáyati ,treibt an, drängt', np. čust ,flink, tätig, passend', ai. skundate ,eilt' (Dhātup.)' — the Sanskrit verb stands first in the entry, exactly as Nourai draws it.\"\n      },\n      {\n       \"ref\": \"HRN:99\",\n       \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss der neupers. Etymologie p. 99 (HRN.txt form-feed leaf 120, headed '— 99 —'), no. 442: 'čust \\\"flink, tätig, passend\\\". ai. √cud-, codate \\\"antreiben; sich beeilen\\\" (Nöldeke, mündliche Mitteilung).' The page number is exact and Horn gives precisely the Sanskrit verb Nourai puts in this node.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny II 554 (WLD_Bd2 djvu line 35973)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Ai. codati, codāpati „treibt an, drängt“ (gegen andere Deutungen s. u.)'; p.555 adds 'Ai. codati nicht zu *qʷed- „stacheln“ ... da in der Vokalstellung unvereinbar' — i.e. Walde-Pokorny explicitly defend the attachment of codati to this root against rival derivations.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. skeud- (IEC.txt line 15612) and sKeud- (line 16104)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Skt. Codami, v. \\\"egg on; hurry\\\"' under skeud- 'fling, shoot, impel'; and 'sKeud- ... The initial appears in Skt. Códàmi, v. \\\"spur on\\\"'.\"\n      },\n      {\n       \"src\": \"CHEUNG\",\n       \"where\": \"s.v. *Čaud (CHEUNG.txt line 3570)\",\n       \"stance\": \"supports\",\n       \"note\": \"'*SANSKRIT: cod \\\"to impel, to excite, to incite\\\" (RV+) = EWAia I: 551' — Mayrhofer's EWAia is cited as the authority for the Sanskrit verb.\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 955 (POK_full.txt line 76641)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Material: Old Indic codati, codayati \\\"treibt an, throngs\\\", np. čust \\\"agile, active, fitting\\\". Old Indic skundate \\\"hurries\\\" (Dhatup.)'\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"čost «چُست»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Persian word چُست čust/čost 'quick, brisk, nimble, agile' is real and does belong to this root — Pokorny prints it inside the entry itself ('np. čust \\\"flink, tätig, passend\\\"') and Cheung lists 'NP čust \\\"quick, brisk, active\\\"' under Iranian *Čaud 'to urge to, impel'. What is not right is the arrow as drawn: a New Persian word cannot descend from Sanskrit. čust is an inherited Iranian formation, not a borrowing or continuation of Skt. cōdati: it goes back to the verbal adjective *(s)kud-tó-s 'propelled, driven' (zero grade *kud- + *-tó-), Proto-Indo-Iranian *čutˢtás > Proto-Iranian *čustah, with the regular Indo-Iranian *-tt- > Iranian *-st- and Persian retention of the cluster -st; the Sanskrit present cōdati is therefore its cognate, formed from the full grade of the same root, not its ancestor. The same Iranian root survives in Middle Persian in the compound verb wizōstan / wizōy- 'to examine, investigate' (< *wi-čaud-, MacKenzie p.93), which shows that the root was alive in Pahlavi; Mo'in's footnote in Borhan-e Qāṭeʿ (the page Nourai cites) likewise gives a Pahlavi gloss 'to run, hurry' beside the Sanskrit. Verdict plausible: the root affiliation and the gloss 'quick, fast' are confirmed, only the route (Sanskrit > Persian rather than sister-cognates) is wrong.\",\n     \"derivation_fa\": \"واژهٔ «چُست» به معنای «تند، چابک، زبردست» راستین است و به همین ریشه بازمی‌گردد؛ پوکورنی خودِ آن را در متنِ مدخل آورده (np. čust „flink, tätig, passend“) و چونگ نیز آن را زیر ستاک ایرانی *čaud «راندن، برانگیختن» ثبت کرده است. اما پیکانِ نمودار نادرست است: واژه‌ای فارسی نو نمی‌تواند از سنسکریت مشتق شود. «چست» صورتی ارثی و ایرانی است، از صفتِ فعلیِ *(s)kud-tá- «رانده‌شده» (درجهٔ صفرِ ریشه + پسوندِ *-ta-)، که از راه هندوایرانی آغازین *čutta- به ایرانی آغازین *čustah رسیده؛ خوشهٔ *-tt- هندوایرانی در ایرانی به -st- بدل می‌شود و در فارسی نو نیز همان -ست مانده است. پس cōdati سنسکریت هم‌ریشهٔ «چست» است نه نیای آن. بازماندهٔ همین ستاک در فارسی میانه در فعل wizōstan / wizōy- «بررسی کردن» (از *wi-čaud-، مکنزی ص ۹۳) دیده می‌شود و حاشیهٔ معین بر برهان قاطع (همان صفحه‌ای که نورایی ارجاع داده) نیز در کنار صورت سنسکریت، گونه‌ای پهلوی با معنای «دویدن، شتابیدن» می‌آورد. داوری: با احتیاط پذیرفتنی است — تعلق واژه به ریشه و معنای آن درست است، ولی مسیرِ اشتقاق (سنسکریت ← فارسی) نادرست و باید «هم‌ریشگی» خوانده شود.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%86%D8%B3%D8%AA\",\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewd-\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:955\",\n       \"status\": \"partial\",\n       \"note\": \"POK_03.txt leaf 196 (IEW 955) has 'np. čust ,flink, tätig, passend'' — but it stands in the same breath as 'Ai. cōdati' as a co-ordinate member of the root, not as a derivative of the Sanskrit verb. Pokorny thus supports the root affiliation and the gloss, but not the Sanskrit > Persian arrow.\"\n      },\n      {\n       \"ref\": \"BQT:636\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin p.636 (BQT_v2_pages.txt form-feed leaf 94; the page carries the 'بیان دهم در جیم فارسی با سین بی‌نقطه' heading and the entry 'چست ۷ = بضم اول و سکون ثانی ... جلد و چالاک و چابک باشد'). Moʿin's footnote 7 at the bottom of that page reads: 'هندی باستان ... codati (راندن، تحریک، عجله کردن) ... پهلوی ... (دویدن)' — Old Indic codati 'to drive, incite, hurry', plus a Pahlavi form glossed 'to run'. That is exactly the pairing Nourai draws, and Aryanpur independently cites 'برهان قاطع : ۶۳۶' for چست, which confirms the page number.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BQT\",\n       \"where\": \"vol. 2 p.636 (BQT_v2_pages.txt leaf 94), s.v. چست + Moʿin's footnote 7\",\n       \"stance\": \"supports\",\n       \"note\": \"Headword: 'چست ... جلد و چالاک و چابک باشد'; footnote: 'هندی باستان ... codati ... پهلوی ... (دویدن)'. Grep pattern used: grep -n 'چست' BQT_v2_pages.txt (hit on line 5451).\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi, [pdf page 223] = printed p.224, s.v. چست\",\n       \"stance\": \"supports\",\n       \"note\": \"The entry cites 'برهان قاطع : ۶۳۶' (confirming Nourai's page) and notes 'چم این واژه در زبان سانسکریت: راندن، شتابیدن' and 'چم این واژه در زبان پهلوی: دویدن، شتابیدن' — Sanskrit CODATI / CUD forms are listed in the Latin-script column.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn no. 442, p.99 (HRN.txt leaf 120)\",\n       \"stance\": \"supports\",\n       \"note\": \"'442. čust \\\"flink, tätig, passend\\\". ai. √cud-, codate \\\"antreiben; sich beeilen\\\" (Nöldeke, mündliche Mitteilung). Fr. Müller's (WZKM. 5, 68) Ableitung des Wortes aus aw. čista- bezw. čišta- ist schon wegen der Vokaldifferenz ... wenig wahrscheinlich.' Horn couples the word with the Sanskrit root and rejects the rival Avestan derivation.\"\n      },\n      {\n       \"src\": \"CHEUNG\",\n       \"where\": \"s.v. *Čaud (CHEUNG.txt line 3570)\",\n       \"stance\": \"partial\",\n       \"note\": \"'*NWIR: NP cust \\\"quick, brisk, active\\\" || (+ *?) NP pizohidan/pizoh- \\\"to investigate\\\" (LW)'; '*MIDDLE PERSIAN: (+ *ui-) BMP wcwd- /wizōy-/ \\\"to examine\\\"'; '«PIE *(s)keud- \\\"to shoot, impel\\\"'. Supports the root but treats NP čust as an inherited Iranian form parallel to Skt. cod, not a derivative of it.\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.93 (PHD_mackenzie.txt line 5503)\",\n       \"stance\": \"partial\",\n       \"note\": \"'wizōstan, wizōh/y- [wcwstn, wcwd-] examine' — the Middle Persian continuant of the root; MacKenzie has no Pahlavi *čust headword, so the Persian adjective itself is first attested in New Persian.\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Persische Studien (HUB.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"grep -n 'öust|cust|6ust' HUB.txt returns no entry for the word (only the English word 'custom' in library boilerplate); Hübschmann does not treat čust.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny II 555 (WLD_Bd2 djvu line 36013 f.)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Umbildung etwa eines *cadati durch Reim auf ksodati „stößt“ ... wird durch np. čust widerlegt' — Walde-Pokorny use the Persian word as independent evidence for the root's vocalism, i.e. they take čust as a direct Iranian member of the root.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Germanic\",\n     \"words\": \"skiutan, skuttjan; skutilaz; skutjôn\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Three of the four forms are Watkins's, lightly respelled: *skeutaną 'to shoot' (Nourai's 'skiutan', with Gothic-style <iu> for the diphthong /eu/) > OE scēotan, ON skjóta, OHG sciozan; *skutjaną / West Gmc *skuttjan 'to bar, bolt' (Nourai's 'skuttjan') > OE scyttan; *skutilaz 'dart, missile' (exactly Watkins) > OE scytel. Two problems. (a) 'skuttjan' is glossed 'to shoot' here, but the sources gloss it 'to bar, to bolt' — it is the bolt-shooting verb behind English shut, a causative/iterative to the strong verb, not a second word for 'shoot'. (b) 'skutjôn' is not a form any source knows: the word for 'corner of a sail, piece of cloth' requires the o-grade *skaut-, i.e. PGmc *skautjōn- (Watkins) / *skautijǭ, *skautaz (Wiktionary), the grade actually attested in Goth. skauts 'hem', ON skaut 'corner, lap', OHG scōz, OE scēat/scēata; a zero-grade *skut-jōn could never give OE scēata. I rendered pdf page 456 at 400 dpi and read the Germanic box: the book itself prints 'skutjôn' (and 'skiutan, skuttjan', 'skutilaz'), so the extraction is faithful and the missing -a- is Nourai's misprint, presumably a slip while copying Watkins's *skautjōn-. A separate, substantive caveat: Kroonen (EDPG) takes *skeutaną to be a back-formation from the iterative *skuttōną, which he derives from PIE *sket- 'to drive forward', and Boutkan gives *skeutaną no IE etymology at all, so the attachment of the whole Germanic group to *(s)kewd- is disputed in the newest handbooks even though Pokorny, Walde-Pokorny, Klein and Watkins all assert it.\",\n     \"derivation_fa\": \"سه صورت از چهار صورتِ این خانه همان بازسازی‌های واتکینز است با اندکی دگرگونی در نگارش: *skeutaną «تیر انداختن» (نگارشِ «skiutan» با iu به شیوهٔ گوتی برای دوواکهٔ /eu/) که به scēotan انگلیسی کهن، skjóta نورس کهن و sciozan آلمانی علیای کهن رسیده؛ *skutjaną / ژرمنی باختریِ *skuttjan «چفت زدن، بستن» (همان skuttjan کتاب) که به scyttan انگلیسی کهن انجامیده؛ و *skutilaz «تیر، زوبین» که دقیقاً صورتِ واتکینز است. دو ایراد هست: نخست آنکه skuttjan در کتاب «تیر انداختن» معنا شده، حال آنکه منابع آن را «چفت/کلون انداختن» می‌دانند (ریشهٔ shut انگلیسی). دوم و مهم‌تر آنکه «skutjôn» صورتی است که هیچ منبعی نمی‌شناسد؛ واژهٔ «گوشهٔ بادبان، تکه‌پارچه» درجهٔ o می‌خواهد، یعنی *skautjōn- (واتکینز) یا *skautijǭ / *skautaz (ویکی‌واژه)، همان درجه‌ای که در skauts گوتی، skaut نورس کهن، scōz آلمانی کهن و scēat(a) انگلیسی کهن گواهی شده است. صفحهٔ ۴۵۶ را با تفکیک ۴۰۰ نقطه بازخوانی کردم: خودِ کتاب «skutjôn» چاپ کرده، پس خطای خوانشِ اسکن نیست بلکه خطای چاپی/سهو مؤلف است در رونویسی از واتکینز. افزون بر این، کرونن و بوتکان در پژوهش‌های تازه پیوند کل شاخهٔ ژرمنی را با این ریشه محل تردید می‌دانند، هرچند پوکورنی، والده-پوکورنی، کلاین و واتکینز همگی آن را می‌پذیرند.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"skutjôn\",\n     \"correct_form\": \"*skautjōn- (Watkins/AHD) = PGmc *skautijǭ, *skautaz\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/skeutan%C4%85\",\n      \"https://en.wiktionary.org/wiki/sheet\",\n      \"https://en.wiktionary.org/wiki/shut\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"partial\",\n       \"note\": \"Watkins 1985 s.v. skeud- (AHD_watkins1985.txt line 943): '1. Germanic *skeutan, to shoot ... 2. Germanic *skutaz, shooting, shot ... 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): SHUT. 4. Germanic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautjōn- in: a. Old English scéata, corner of a sail: SHEET2; b. Old English scéte, piece of cloth: SHEET1.' This is plainly Nourai's source, but Watkins writes *skautjōn-, not 'skutjôn', and glosses *skutjan as the 'shut' verb, not 'to shoot'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 955-956 (POK_03.txt leaf 196)\",\n       \"stance\": \"supports\",\n       \"note\": \"'aisl. skjóta, ags. sceotan ,schleudern, stoßen, schießen', ahd. sciozan ... ahd. scoz ,Geschoß', got. skaut ,Schoß, Saum', aisl. skaut n. ,Zipfel, Ecke, Schoß' ... mnd. schott(-tt-) ,(vorgeschobener) Riegel, Verschluß'' — note Pokorny's forms all have skaut-, never *skut-, for the 'corner/hem' word.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny II 554 (WLD_Bd2 djvu lines 35984-35993)\",\n       \"stance\": \"supports\",\n       \"note\": \"'got. skauta d. sg. „(hervorschießender) Zipfel oder Saum eines Kleides“, aisl. skaut n. „Zipfel, Ecke, Schoß, Vorsprung“, ahd. scoz „Zipfel, Kleiderschoß“' — again the au-grade.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein, s.v. shoot (KLN_1966.txt line 35028) and sheet (line 34935)\",\n       \"stance\": \"supports\",\n       \"note\": \"'shoot ... fr. OE. sceotan, rel. to OS. skiotan, ON. skjota ... fr. I.-E. base *(s)qeud-, \\\"to throw, shoot; to run, haste\\\"'; 'sheet ... OE. sceat, \\\"lap, bosom, surface; piece of cloth\\\", which is rel. to ON. skaut ... Goth. skauts'. Klein's Germanic protoform for 'sheet' is again the skaut-/skaut- type.\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. skeud-\",\n       \"stance\": \"partial\",\n       \"note\": \"See ref_check: supports every derivation drawn here, but prints *skautjōn- where the book prints skutjôn.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"shoot, shot, shut; shuttle; sheet\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All five English words go back to the Germanic forms of the parent node. shoot: ME sheten, shoten < OE scēotan (strong class II) < PWGmc *skeutan < PGmc *skeutaną. shot: OE (ġe)sceot, scot 'a shooting, a shot' < PGmc *skutaz, the zero-grade noun to the same verb (the homophonous scot 'tax, contribution' is its doublet, whence 'scot-free'). shut: ME schitten, schutten < OE scyttan 'to shoot a bolt, fasten' < PWGmc *skuttjan, a weak verb built on the zero-grade *skut- of the strong verb — Klein: 'prob. rel. to shoot. For sense development cp. the phrase \\\"to shoot a bolt\\\"'; Modern English shut continues a dialect form, since the regular outcome of OE scyttan would have fallen together with shit. shuttle: ME shutel, schetil < OE scytel 'dart, missile' < PGmc *skutilaz, transferred to the weaver's implement because it is 'shot' across the warp threads (Skeat: 'so called from being shot across the threads in weaving'); it is a doublet of skittle. sheet: two OE words fell together, scīete/scȳte 'piece of linen cloth' (< PGmc *skautijǭ) and scēata 'corner, lower corner of a sail' (< *skautaz), which is why English sheet means both the bed-linen and the rope made fast to the corner of a sail. Nourai gives no reference for this node; the chain is standard and uncontroversial in Klein, Skeat and Watkins alike.\",\n     \"derivation_fa\": \"هر پنج واژهٔ انگلیسیِ این خانه بازماندهٔ همان صورت‌های ژرمنیِ خانهٔ بالایند: shoot از انگلیسی میانهٔ sheten/shoten و انگلیسی کهنِ scēotan (فعل قویِ ردهٔ دوم) از ژرمنی آغازین *skeutaną؛ shot از (ġe)sceot انگلیسی کهن، اسمِ درجهٔ صفرِ همان فعل (*skutaz)؛ shut از scyttan انگلیسی کهن «کلون انداختن، بستن»، فعلی ضعیف ساخته‌شده بر درجهٔ صفرِ *skut- — کلاین می‌گوید پیوندِ معنایی را با عبارتِ «to shoot a bolt» بسنجید؛ صورت امروزی برآمده از گویشی است، زیرا بازتابِ قاعده‌مندِ scyttan با shit یکسان می‌شد. shuttle از scytel انگلیسی کهن «تیر، زوبین» (*skutilaz) است و نامِ ماکوی بافندگی شد چون میان تارها «پرتاب» می‌شود (اسکیت: «چنین نامیده شده از آنکه در بافندگی میان نخ‌ها انداخته می‌شود»). sheet حاصلِ درهم‌آمیختنِ دو واژهٔ انگلیسی کهن است: scīete «تکه‌پارچهٔ کتانی» (از *skautijǭ) و scēata «گوشه، گوشهٔ پایینِ بادبان» (از *skautaz)؛ از همین روست که sheet در انگلیسی هم «ملافه» است و هم «طنابِ بستهٔ گوشهٔ بادبان». نورایی برای این خانه مرجعی نداده، ولی زنجیره نزد کلاین، اسکیت و واتکینز یکسان و بی‌مناقشه است؛ ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/shoot\",\n      \"https://en.wiktionary.org/wiki/sheet\",\n      \"https://en.wiktionary.org/wiki/shuttle\",\n      \"https://en.wiktionary.org/wiki/shut\",\n      \"https://www.etymonline.com/word/shoot\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"none\",\n       \"status\": \"not_checked\",\n       \"note\": \"The chart gives no reference for this node (refs=None); the parent node's AHD citation covers it, and Klein and Skeat were consulted instead — see 'consulted'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.vv. shoot, shut, shuttle, sheet, scot (KLN_1966.txt lines 35028, 35098, 35100, 34935, 34174)\",\n       \"stance\": \"supports\",\n       \"note\": \"'shoot ... fr. OE. sceotan ... fr. I.-E. base *(s)qeud- ... Cp. scoot, scot, scoter, scuttle, sheet, shot, shut, shuttle, skeet, skit ...'; 'shut ... fr. OE. scyttan, \\\"to shut\\\"; prob. rel. to shoot. For sense development cp. the phrase \\\"to shoot a bolt\\\"'; 'shuttle ... fr. OE. scytel, \\\"missile, dart\\\", a gradational variant formed from the stem of sceotan'; 'sheet ... fr. OE. sciete, scyte, scete, itself derived fr. OE. sceat ... prob. also to OE. sceotan, \\\"to shoot\\\"'. Every English word of the node is covered.\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"Skeat s.vv. shut, sheet, shuttle (SKT.txt lines 17159, 17154, 17160)\",\n       \"stance\": \"supports\",\n       \"note\": \"'shut. (E.) M.E. shutten, shitten. A.S. scyttan, to shut; to fasten a door with a bolt ... a weak verb; from scut-, base of pt. t. pl. of sceotan, to shoot'; 'sheet ... A.S. scite, scyte, a sheet; also sceat, a corner ... corner of a sail, hence a sheet or rope fastened to a corner of a sail'; 'shuttle. (E.) So called from being shot across the threads in weaving.'\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. skeud- and index (AHD_watkins1985.txt lines 943, 2252-2254)\",\n       \"stance\": \"supports\",\n       \"note\": \"The index lists SHEET1 skeud-, SHEET2 skeud-, SHOOT skeud-, SHOT1 skeud-, SHUT skeud-, SHUTTLE skeud- — the same five words Nourai puts in this box.\"\n      },\n      {\n       \"src\": \"WEB\",\n       \"where\": \"etymonline s.v. shoot (archived copy)\",\n       \"stance\": \"partial\",\n       \"note\": \"'reconstructed to be from Proto-Germanic *skeutanan ... often said to be from PIE root *skeud- \\\"to shoot, chase, throw,\\\" but Boutkan gives it no IE etymology' — the English chain is not in doubt, only its ultimate PIE attachment (see node #3).\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-456.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", p)\nPYEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-456.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 456"
}
```


### [2026-09-14T02:04:44.778Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-456.json
JSON OK
nodes verified: 4/4
node verdicts: {'confirmed': 2, 'plausible': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 3, 'partial': 2, 'not_checked': 1}
books consulted: {'supports': 14, 'partial': 4, 'silent': 1} | by book: {'WLD': 3, 'CHEUNG': 2, 'POK': 2, 'KLN': 2, 'AHD': 2, 'IEC': 1, 'BQT': 1, 'ARY': 1, 'HRN': 1, 'PHD': 1, 'HUB': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-14T02:05:00.510Z] AGENT

Page 456 (book p. 426) verified — `data/verification/page-456.json`, `verify_check.py 456` shows 0 PROBLEM lines.

Counts: 1 entry (entry 1 "Skeud 2" is a redirect, skipped), 4 nodes.
- Root verdicts: confirmed 1
- Node verdicts: confirmed 2, plausible 1, transcription_suspect 1
- Ref checks: supports 3, partial 2, not_checked 1; 13 book consultations (POK, WLD, AHD, IEC, CHEUNG, KLN, SKT, HRN, BQT, ARY, PHD, HUB, etymonline)

Flagged items:
- `transcription_suspect` — Skeud 1, node #3 Germanic **skutjôn** "corner of sail": the 'sheet' word requires the o-grade *skaut-; Watkins (Nourai's own AHD source) prints *skautjōn-, Wiktionary *skautijǭ/*skautaz. Rendered pdf p.456 at 400 dpi: the **book itself prints "skutjôn"**, so `error_in: book` — Nourai's misprint, extraction is faithful. Same node: `skuttjan` is glossed "to shoot" but is the 'bolt' verb behind *shut*. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/456.png`.
- `plausible` — node #2 Persian چست čost: word, gloss and root affiliation all confirmed (Pokorny prints "np. čust" inside the entry), but the drawn arrow Sanskrit → Persian is wrong: čust is inherited Iranian *(s)kud-tó-s > PIr *čustah, a cognate of Skt. cōdati, not a descendant.

No extraction errors: the JSON matches the printed page exactly (root box, all four nodes, both refs sets).

Useful confirmations: POK:955 is exact (entry "2. (s)keud-" begins on 955); HRN:99 no. 442 gives čust ← ai. √cud-, codate verbatim; BQT:636 is exact — Moʿin's footnote 7 on that page cites Old Indic codati plus a Pahlavi 'to run', and Aryanpur (p. 224) independently cites "برهان قاطع : ۶۳۶". Nourai's "Skeud 1"/"Skeud 2" numbering is the reverse of Pokorny's, and the "Skeud 2 → Keued" redirect reproduces Pokorny's own cross-reference to keuəd- (IEW 595 f.).
