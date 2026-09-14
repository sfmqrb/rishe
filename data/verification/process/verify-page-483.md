# Verification process log — verify-page-483


## [2026-09-14T03:08:18.520Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 483 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-483.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-483.json. Write /home/sfmqrb/git/rishe/data/verification/page-483.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 483` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:19.455Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:20.300Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:20.315Z] TOOL RESULT

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


## [2026-09-14T03:08:20.802Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-483.txt"
}
```


### [2026-09-14T03:08:20.830Z] TOOL RESULT

```
1	=== PDF page 483 (book page 453) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Stomen : mouth  (refs POK:1035)
4	#1 (parent #0) [Avestan] refs=POK:1035; KLN:1518 | staman : mouth (of a dog)
5	  #2 (parent #1) [Persian] refs=HRN:267 | astam «اَستَم» : mouth (obsolete)
6	#3 (parent #0) [Greek] refs=POK:1035 | stoma, stomaxos : mouth, throat
7	  #4 (parent #3) [Latin] refs=KLN:1518 | stomachus : taste, stomach
8	    #5 (parent #4) [English] refs=AHD | stomach
9	--- entry 1 ---
10	ROOT Stor -> redirect to Ster 1
11	--- entry 2 ---
12	ROOT Str -> redirect to Ster 1
13	
```


## [2026-09-14T03:08:23.900Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-483.json",
 "description": "Read source JSON for page 483"
}
```


### [2026-09-14T03:08:23.950Z] TOOL RESULT

```
{
  "pdf_page": 483,
  "book_page": 453,
  "entries": [
    {
      "root": {
        "name": "Stomen",
        "lang": "Indo-European",
        "refs": "POK:1035",
        "gloss": "mouth"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1035; KLN:1518",
          "words": [
            {"translit": "staman", "gloss": "mouth (of a dog)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:267",
          "words": [
            {"translit": "astam", "gloss": "mouth (obsolete)", "script": "اَستَم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:1035",
          "words": [
            {"translit": "stoma, stomaxos", "gloss": "mouth, throat", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "KLN:1518",
          "words": [
            {"translit": "stomachus", "gloss": "taste, stomach", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stomach", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stor",
        "redirect": "Ster 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Str",
        "redirect": "Ster 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:08:25.862Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','HRN','HUB','WLD','IEC','SYN','BRT','PHD','NYB','SKT','FSD','WEB','MON','BQT','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T03:08:26.942Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
```


## [2026-09-14T03:08:31.227Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -60; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','AHD','BRT','IEC','SYN','SKT','WLD']:\n    v=d[k]; print(k, v.get('local_file'), '|offset:', v.get('page_offset'))\n\""
}
```


### [2026-09-14T03:08:32.322Z] TOOL RESULT

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
KNT_full.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
---
POK /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HRN /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AHD /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
BRT /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
IEC /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WLD ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
```


## [2026-09-14T03:08:35.650Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"stomen\\|stōmen\\|staman\" POK_03.txt | head -20\necho \"=== POK_02 ===\"\ngrep -n -i \"stomen\\|staman\" POK_02.txt | head -10"
}
```


### [2026-09-14T03:08:35.728Z] TOOL RESULT

```
3843:kv.  staman-  n.  ,Maul  (vom  Hund)^;  gr.  GT6y,a  n.  ,Mund^,  orö^axog K-^^o-Formans)  , Kehle,  Mündung  (der  Blase,  des  Uterus);  Magenmund, Hagen';  dehnstufi^  arMf-ivlog  ,mundfertig,  geschwätzig;  artig  plaudernd', [•ttofiuUw  ,plaudere',  arwfxvXia  ^Geschwätzigkeit'  (daß  ved.  stämü-  etwa jiKnend,  stöhnend'  bedeute  und  verwandt  sei,  ist  unsicher);  mit  sekund��-
=== POK_02 ===
```


## [2026-09-14T03:08:36.877Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN stomach ===\"\ngrep -n -i \"stomach\" KLN_1966.txt | head -20\necho \"=== HRN astam ===\"\ngrep -n -i \"astam\\|staman\" HRN.txt | head -20"
}
```


### [2026-09-14T03:08:36.963Z] TOOL RESULT

```
=== KLN stomach ===
1201:*k°*nasu,ti,  n.,  the  fourth  stomach  of  a  ruminant (anat.)  —  ModL.,  fr.  ab-  and  L.  omasum, ‘bullock’s  tripe’.  See  omasum.
1909:agastric,  adj.  having  no  stomach  (zool.)  —  Form¬ ed  fr.  priv.  pref.  a-,  and  Gk.  vxo-nrp,  ‘stomach’. See  gastric.
2668:anastomosis,  n.,  intercommunication  of  vessels  in the  animal  body  or  of  parts  in  any  branching system  (anat.)  —  Gk.  dvanTouwai-:,  ‘outlet, opening’,  fr.  dvaa-ropiouv,  ‘to  furnish  with  a mouth’,  fr.  dvd  (see  ana-)  and  ordpa,  ‘mouth’. See  stoma,  stomach.
4878:bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon
6525:cardiac,  adj.  (anal.),  1)  pertaining  to  the  heart; 2)  pertaining  to  the  upper  part  of  the  stomach.
7647:stomach  into  the  small  intestine,  (physiol.)  — Late  L.  chymus,  fr.  Gk.  yuiiop,  ‘juice’,  which  is rel.  to  yfiXoq,  ‘juice’.  See  chyle  and  cp.  words there  referred  to.  Cp.  also  enchyma  and  words there  referred  to.
11389:digest,  tr.  v.,  1)  to  arrange  systematically;  2)  to prepare  (food  in  the  stomach)  for  assimilation; intr.  v.,  to  be  digested.  —  L.  digestus,  pp.  of  di- gerere,  ‘to  carry  apart,  distribute,  divide,  spread about’,  fr.  di-,  ‘apart’,  and  gerere,  ‘to  carry’. See  gerent.
12449:duodenitis,  n.,  inflammation  of  the  duodenum (med.)  —  A  Medical  L.  hybrid  coined  fr.  duo¬ denum  and  -itis,  a  suff.  of  Greek  origin, duodeno-,  combining  form,  meaning  ‘referring  to the  duodenum’.  —  See  next  word, duodenum,  n.,  the  first  part  of  the  small  intestine leading  from  the  stomach  to  the  jejunum  (ana¬ tomy).  —  ML.  duodenum,  coined  by  Gerard  of Cremona  (died  in  1187),  the  translator  of  the Canon  Avicennae,  fr.  L.  duodeni,  ‘twelve  each’, fr.  duo,  ‘two’,  and  deni,  ‘ten  each’*  which  is  rel.  to
13384:epigastric,  adj.,  on  or  above  the  stomach  (anat.) —  Formed  with  suff.  -ic  fr.  Gk.  ini^dnnpioq, ‘above  the  belly’,  fr.  6tc1  (see  epi-)  and  yaaTrjp, ‘belly’.  See  gastro-  and  cp.  hypogastric,  meso- gastric.
14862:flatulence,  flatulency,  n.  —  F.  flatulence,  fr. flatulent.  See  next  word  and  -ce,  resp.  -cy. flatulent,  adj.,  windy;  vain.  —  F.,  fr.  L.  flatu- lentus,  fr.  flatus.  See  next  word  and  -ent. Derivatives:  flatulent-ly,  adv.,  flatulent-ness,  n. flatus,  n.,  a  puff  of  wind;  accumulation  of  gas in  the  stomach  or  bowels.  —  L.  flatus  (scil. ventris),  ‘blowing  (of  the  stomach)’,  fr.  flatus, pp.  of  flare,  ‘to  blow’,  which  is  cogn.  with  OE. blawan,  ‘to  blow’.  See  blow,  ‘to  puff’,  and  cp. afflatus,  conflate,  deflate,  flabellum,  flageolet, ‘wind  instrument’,  inflate,  perflation,  reflate, sufflate.  Cp.  also  soffione,  souffle.  Cp.  also  flavor, flaunt,  intr.  v.,  to  make  an  ostentatious  display; tr.  v.,  to  display  ostentatiously.  —  Prob.  a  blend of  flout  and  vaunt.
15093:folkmote,  folk  moot,  n.,  general  assembly  of  a town  or  shire  in  Anglo-Saxon  England.  — Modem  rendering  of  OE.  falcmdt,  folcgemot, lit.  ‘people’s  meeting’.  See  folk  and  moot, follicle,  n.,  1)  a  small  sac,  cavity  or  gland  ( anat .); 2)  a  seed  vessel  (bot.)  —  F.  follicule,  ‘a  little bag’,  fr.  L.  folliculus,  of  s.m.,  dimin.  of  folds, ‘a  leather  sack;  a  pair  of  bellows,  moneybag, wind  cushion,  stomach’.  L.  faUis  stands  for *bhol-nis  or  *bhj-nis  and  is  a  derivative  of  base *bhel-,  ‘to  swell’.  See  bull,  ‘male  of  the  ox’,  and cp.  belly  and  words  there  referred  to.  For  the ending  see  suff.  -cle.
15746:gambeson,  n.,  a  medieval  military  garment  of defense.  —  OF.  gambaison,  gambeson,  fr.  gam- bais,  wambais ,  fr.  Frankish  *wamba ,  ‘stomach, belly’.  Cp.  OHG.,  Goth,  wamha  and  see  womb, gambier,  n.,  the  extract  of  the  shrub  Uncaria gambir.  —  Malay  gambir. gambit,  n.,  opening  move  in  chess  in  which  the first  player  risks  a  pawn  to  gain  an  advantage later.  —  F.,  fr.  Sp.  gambito,  fr.  Arab,  janbt, ‘lateral’,  fr.  janb,  ‘side’  (whence  jdnaba,  ‘he  put aside’),  which  is  rel.  to  Aram. -Syr.  gabh,  gabbd, ‘side’,  Heb.  ganabh,  Aram. -Syr.  gendbh,  ‘he stole’,  lit.  ‘he  put  aside’,  Heb.  ganndbh,  ‘thief’. Cp.  gonnof.
15836:gastero-,  before  a  vowel  gaster-,  combining  form meaning  ‘stomach’  or  ‘belly’.  —  Gk.  yaaxcpo-, yaaxsp-,  identical  in  meaning  with  yaaxpo-, yaaxp-.  See  gastro-.
15839:gastrectomy,  n.,  the  surgical  removal  of  part  of the  stomach.  —  Compounded  of  gastr-  and Gk.  -exTopda,  ‘a  cutting  out  of’,  fr.  exxouf,,  ‘a cutting  out’.  See  -ectomy. gastric,  adj.,  pertaining  to  the  stomach.  — Formed  with  suff.  -ic,  fr.  Gk.  yaaxqp,  gen. yaaxpop,  ‘stomach’.  See  gastro-  and  cp.  di¬ gastric,  epigastric,  hypogastric,  mesogastric. gastritis,  n.,  inflammation  of  the  stomach  (med.)
15841:gastro-,  before  a  vowel  gastr-,  combining  form meaning  ‘stomach’  or  ‘belly’.  —  Gk.  yaaxpo-, yaaxp-,  fr.  yaaxqp,  gen.  yaaxp6;,‘stomach,  belly, womb’,  which  is  dissimilated  fr.  *ypxaxY]p  anp lit.  means  ‘eater,  devoured,  fr.  ypav,  ‘to  gnaw, eat’,  whence  also  ypaaxi;,  ‘green  fodder’,  yaa- xpi;  (dissimilated  fr.  ‘ypxaxptp),  ‘pot-bellied; glutton’;  prob.  cogn.  with  OI.  grasati,  ‘eats, devours’.  See  cress  and  cp.  gangrene, gastrocnemius,  n.,  the  largest  muscle  of  the  calf of  the  leg  (anal.)  —  Medical  L.,  fr.  Gk.  yaa- xpoxvqpda,  ‘the  calf  of  the  leg’,  which  is  com¬ pounded  of  yaaxqp,  gen.  yaaxpo;,  ‘belly’,  and xvfjpLT],  ‘part  between  knee  and  ankle,  leg, shank’.  For  the  first  element  see  gastro-,  for the  second  see  cnemial.
15843:gastrology,  n.,  1)  the  sciences  of  the  structure, functions  and  diseases  of  the  stomach;  2)  gas¬ tronomy.  —  Gk.  yaaxpoXoyia,  title  of  the Greek  Almanach  des  Gourmands,  a  poem  writ¬ ten  by  Archestratus,  a  contemporary  of  Aris¬ totle;  compounded  of  yaaxqp,  gen.  yocaxpip, ‘stomach’,  and  -Xoyia,  fr.  -Xoyo;,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  gastro-  and  -logy. Derivatives:  gastrolog-er,  n.,  gastrolog-ist,  n. gastronome,  n.  —  F.,  back  formation  fr.  gastro¬ nomic.  See  gastronomy.
15845:gastronomy,  n.,  the  act  or  science  of  caring  for the  stomach,  i.e.  cookery.  —  F.  gastronomie, fr.  Gk.  yaaxpovopda,  another  name  for  yaa-
15846:xpoXoyia  (see  gastrology);  formed  fr.  yaaxqp, gen.  yaaxp6;,  ‘stomach’,  on  analogy  of  aaxpo- vopda,  ‘astronomy’  (fr.  aaxqp,  ‘star’).  See  gastro- and  -nomy.
15847:Derivatives :  gastronom-ic,gastronom-ic-al,  adjs., gastronom-ic-al-ly,  adv.,  gastronom-ist,  n. gastroscope,  n.,  an  instrument  for  examining  the interior  of  the  stomach.  —  Compounded  of gastro-  and  Gk.  -axo7nov,  fr.  oxoraiv,  ‘to  look at,  examine’.  See  -scope.
15848:gastroscopy,  n.,  examination  of  the  interior  of the  stomach.  • —  Compounded  of  gastro-  and Gk.  -oxoTua,  fr.  oxotteTv,  ‘to  look  at,  examine'. See  -scopy.
=== HRN astam ===
1590:ap. ^avastaman- 'zuverlässig*, vergl. skr. ava-r
10155:aw. staman- 'MauV.
15638:astam 31.
```


## [2026-09-14T03:08:42.227Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3830,3850p' POK_03.txt\necho \"=== which leaf ===\"\npython3 - <<'EOF'\ndata=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nimport re\nidx=data.find('staman-  n.  ,Maul')\nleaf=data[:idx].count('\\f')\nprint('leaf(0-based)',leaf,'=> printed approx', leaf+762, 'to', leaf+766)\nEOF"
}
```


### [2026-09-14T03:08:43.425Z] TOOL RESULT

```
aus    *steub{hymä,    *stouh{h)-mä:    cymr.    ystum    f.    ,Biegung,  "Wen; Gestalt',    bret.    stumm    ds.   (ins  Ir.   entlehnt  mir.   stuaimm  f.  ,Fähii auch  ,Flußbiegung' ;  dastum  ,das  Einsammeln'  (Loth  RC.  48,  354ff,) ags.  stüpian-^  ^^:
ahd.  stobarön  ,obstupere';
aisl.  stüfr  , Stumpf,  mnd.  stuf  Adj.   , stumpf,   stüven  ==  aisl.  si stumpfen,  abhauen' ;  aisl.  stofn  , Baumstumpf,  Grundlage' ;   ags.  ttoj aisl.  stuhhr,  stuhhi  m.  , Stumpf,  Baumstumpf,  ags.  styhh  n.  ,Baui
mit  germ.  -p-:  aisl.  stüpa  ,emporragen*,  ags.  stüpian,  mnl.  stui bücken*;  ablaut.  ags.  steap  ,hoch,  ragend'  (engl,   steep  , steil*),  mhd. ,hochragender  Felsen'  (Hohestaufen),  mhd.  stief  ,steil';  aisl.  stäup  tu Becher';  ags.  steap,  ahd.  mhd.  stouf  ,Becher*;  ags.  stoppa  , Kübel, aus   , abgestutzt  =  beraubt*  erklärt  sich   aisl.  stjüp-  , Stief-*  {stjüi söhn*),  ags.  steop-,  ahd.  stiof-,  stiuf-,  nhd.  Stief-,  ags.  äbe-stlepan  ,ber ä-stleped  ,verwaist',  ahd.  ar-,  bi-stiufan  ,der  Eltern  oder   der  Kin( rauben* ;
lett.  Staupe  ,Pferdefußtapfen* ;  stupe,  stups  ,Bes'enstumpf ;  (abgebi Rute'.
WP.  II  615  ff.,  WH.  II  608  ff.,  Trautmann  331,  Vasmer  3,  109,
1035
\.     few  ;l3'Ut  preisen*;  nur  indo-iran.  u.  griech.
^      ^i.  stäuti,  stdvate  usw.  ,lobt,  preist^,  Partiz.  stutd-  ,gepriesenS  stuti-  f. j^b^  preis',   stötdr-   , Lobsänger'    usw.,   av.    staoiti  ,lobt,   preist,   besingt; betet',   Partiz.    stüta-,    stüiti-,  staotar-   usw.,   erweitert  ai.   stöhhati  ^preist, Ijüchzt';  gr.  otsvtccl  ,(*rühmt  sich)  verspricht  prahlend'.    - ^yp.  II  620.
[^üQ'  jSich  verdichten,  sich  ballen',  vielleicht  stau-,  stou-istü   mit  stäi-: stt-'.sti-ä-  ,sich  verdichten,  stocken'  als   Erweiterung  eines  *stä-  auf- faßbar, ^i.   ghrta-stävah   Akk.    PL   , Schmalz^   Tropfen';    'pfthu-stu-    ,mit    einem breiten  Zopfe^  stü-k-ä,  stuka-  m.  , Zotte,  Flocke',  stöhd-  m.  , Tropfen',  mit ^er  Bed.-Entw.  ,Klümpchen,  rundliches  Ding*,  wahrscheinlich  lett.  stükis Wickelkind'  und  ai.  stuka-  m.  ,Kind,  Tierjunges';  ai.  stä-p-a-,   stupd-  m. Haarschopf',  gr.  *(JT^n7]j  atvrtrtrj  ,Werg'  (daraus  lat.   stüpa,   stuppa  ds.) ; rr.  oxtcpoi  , ziehe  zusammen,   mache   dicht,   hart,   schmecke  herb',  gtvi.i(.icc «usammenziehendes  Mittel',  azvxpLg  ,das   Zusammenziehen,  Beizen',  OTVTt- fttög  ,zusammenziehend',  GTvcpög,  arvcpQÖg,  GTVq)v6g  ,herb,  zusammenziehend', fpv^vög  ,fest,  kompakt';  vielleicht  gr.  gtv^,   OTvyög  im   PL   ,durchdringen- fier  Frost,    Eiseskälte',    arvyog   n.    ,(*Schauder)    Abscheu,    Haß',   Gtvyeo) ^jbasse,  verabscheue,  fürchte^,  doch  vgl.  oben  S.  1033 ;
ksl.  stud^   studh   , Kälte',    styngti    , erkalten'    und   stydeti   ,sich   schämen' .♦erstarren') ;  russ.  istygnuth,  stugnuth  .gefrieren'. WP.  II  620,  Vasmer  3,  33  ff.
Stilb-?  ,glänzen;  schauen'?  dem  Bau  idg.  Wurzeln  widersprechend. Gr.  oxiXßu)  ^glänze,  schimmere',  OTiXßr}  , Glanz';  axLlTCvog  , glänzend'  = [Ir.  seil   jAuge',   sellaim   ,sehe   an',    cymr.    syllu,   corn.   sylly,  bret.  sellout inschauen'. WP.  II  646.
len-  ,Mund'.
kv.  staman-  n.  ,Maul  (vom  Hund)^;  gr.  GT6y,a  n.  ,Mund^,  orö^axog K-^^o-Formans)  , Kehle,  Mündung  (der  Blase,  des  Uterus);  Magenmund, Hagen';  dehnstufi^  arMf-ivlog  ,mundfertig,  geschwätzig;  artig  plaudernd', [•ttofiuUw  ,plaudere',  arwfxvXia  ^Geschwätzigkeit'  (daß  ved.  stämü-  etwa jiKnend,  stöhnend'  bedeute  und  verwandt  sei,  ist  unsicher);  mit  sekund��-
»m  a:  cymr.  sa/n, Kinnlade';  sefnig  ,Kehle',  acorn.  stefenic  , Gaumen', [•l)ret.  staffn,  nbret.  staofi  ds.
WP.  II  648.
1036  •
storos,  Stornos  (strnos?)  ,Star  und  Vögel  ähnlichen  Lauteindruckt« Lat.  sturnus,  -i  m.  ^Star',  aus  *strnos  oder  *stornos,  in  letzterem  J'tU. ags.  stearn  ,Seeschwalbe*,  apr.  starnite  ,Möwe'  (Ms.  stamite) ;  vgl.  ^^^^j^     ** strnad,  russ.  strendtka  , Goldammer*?  ^^
ahd.  star{a),  nhd.  Star,  aisl.  stari,  ags.  stc^r,  Demin.  stcerling  ^^ WP.  II  649,  WH.  II  610,  Frisk  173,  Vasmer  3,  26.
1.  streig-  ^stehenbleiben,  steckenbleiben,  innehaltend
Lat.  strigöj  -äre  , stehenbleiben,  innehalten  (besonders  von  Zugtii^r*«. wozu  wohl  auch  obstrigillö,  -äre  ,hemmend  entgegenstehen,  liinderiick  k, Wege  sein';  norw.  strika  (*strikön  =  strigäre)  ^einhalten,  stoppen*,  t<HW ^hinderlich',  strika  st.  V.  ^den  Lauf  hemmen,  stoppen* ;  lit.  straigjü  Ji* einstoßen',  stringü,  strigti , steckenbleiben',  lett.  striegt  und  strigt  ^einsj^^ (eig.  ,steckenbleiben'),  straignis  ,Morast';  slav.  *str^g-ti  in  poln.  «oilrfe ustrz(ic.  *-4
=== which leaf ===
leaf(0-based) 277 => printed approx 1039 to 1043
```


## [2026-09-14T03:08:43.779Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10145,10165p' HRN.txt\necho \"=== leaf ===\"\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\nidx=data.find(\"aw. staman- 'MauV\")\nleaf=data[:idx].count('\\f')\nprint('leaf',leaf,'printed p.',leaf-21)\nEOF"
}
```


### [2026-09-14T03:08:45.054Z] TOOL RESULT

```
30. äsrük 'Priester, dsrühlh, päz. äsrm.
aw. dtiraoan-; ai. dtharvan-.
V
Np. vergl. (itörbän der Wörterbücher (im Sähnäme
I, 24 Vers 18 entsprechen von Jemsed's vier Ständen
die katüziyän, Calc, (imäziyan, Par., das Rückert,
ZDMG. VIII, 256, in atüviyan ändern wollte. Doch
lassen sich die augenscheinlich sehr corrumpirten
Namen der Stände überhaupt nicht leicht deuten).
31. astanfi ^Maul*.
aw. staman- 'MauV.
Arm. stom ist aus gr. avo^ia entlehnt.
32. aS 'Auge (AW.-Komm. für aw. asi-; Bund. 'Quell)'.
aw. asi' 'Auge'; ai. äksi-'j arm. akn 'Auge*, acU
'Augen (H. No. 4, 26).
33. aH{i)nSttan 'begiessen' (AW.-Komm.).
Wohl aw. <X + 1/ haec-, hiüöaiti 'begiessen ; ai. 61 +
[/'sed'^ sincdti.
Wenn np. peäenjüien (oben No. 323) nicht wäre, so
würde ich ah(i)ncifan zu lesen vorschlagen. Übrigens
könnte pesenjiden auch nur ein aus peh(i)njiden ver-
=== leaf ===
leaf 288 printed p. 267
```


## [2026-09-14T03:09:08.061Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafpage(f,pat,off=None):\n    data=open(f,encoding='utf-8',errors='replace').read()\n    pages=data.split('\\f')\n    for i,p in enumerate(pages):\n        if re.search(pat,p,re.I):\n            print('---',f,'leaf',i)\n            print(p[:60].replace('\\n',' | '))\n    print()\n# KLN stomach headword\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'stomach,\\s*n\\.', p):\n        print('KLN leaf',i)\n        m=re.search(r'stoma,.{0,3000}', p, re.S)\n        j=p.find('stomach,')\n        print(p[max(0,j-1500):j+1500])\n        break\nEOF"
}
```


### [2026-09-14T03:09:09.175Z] TOOL RESULT

```
KLN leaf 805
See  stolon, stolen,  pp.  of  steal.  —  ME.  stolen,  fr.  OE.  ge- stolen,  pp.  of  stelan.  See  steal.
stolid
&LUUI  IU
1518  ‘  1  i5iy
stolid,  adj.,  dull.  —  L.  stolidus,  ‘dull,  obtuse, stolid’,  prop,  ‘unmovable’,  rel.  to  stultus,  ‘fool¬ ish’,  fr.  I.-E.  base  *st(h)el-,  ‘to  cause  to  stand, to  place’.  See  stall  and  cp.  stultify.  Cp.  also  still, adj.,  stolon.
stolidity,  n.,  dullness.  —  L.  stoliditds,  ‘dullness, obtuseness’,  fr.  stolidus.  See  prec.  word  and  -ity.
stolon,  n.,  a  shoot,  sucker.  —  L.  stold,  gen.  -dnis, cogn.  with  Arm.  stein ,  ‘trunk  (of  a  tree) ;  branch’, Gk.  axEXeyoc,  ‘trunk,  stem,  log’,  axsXea,  ‘haft, shaft’,  axrjXr],  ‘block  of  stone’,  Lett,  stulms, ‘trunk  (of  a  tree),  arm,  leg’,  fr.  I.-E.  base  *st(h)el-, ‘to  cause  to  stand,  to  place’.  See  stall  and  cp. stolid.
stolonate,  adj.,  having  a  stolon.  —  Formed  with adj.  suff.  -ate  fr.  L.  stold,  gen.  -dnis.  See  prec. word.
stoloniferous,  adj.,  producing  stolons.  —  See stolon  and  -ferous.
stoma,  n.,  a  minute  mouthlike  orifice.  —  Gk. ax6pa,  gen.  axopaxo?,  ‘mouth’,  whence  axo- paxo;,  ‘throat,  gullet,  stomach’.  See  stomach.
stomacace,  n.,  canker  of  the  mouth  ( med .)  — ModL.,  fr.  Gk.  axopaxax7],  ‘scurvy  of  the gums’,  lit.  ‘disease  of  the  mouth’,  fr.  ax6pa, ‘mouth’,  and  xaxv],  ‘wickedness,  vice’,  which  is rel.  to  xaxo?,  ‘bad,  evil’.  See  prec.  word  and caco-.
stomach,  n.  —  ME.  stomak ,  fr.  OF.  (=  F.)  esto- mac,  fr.  L.  stomachus,  ‘gullet,  esophagus,  stom¬ ach,  liking,  taste’,  fr.  Gk.  ox opayop,  ‘throat, gullet,  esophagus,  stomach’,  fr.  ax6pa,  ‘mouth’, which  is  cogn.  with  Avestic  staman-,  ‘mouth  (of a  dog)',  Hitt,  shtamar ,  ‘mouth’,  MBret.  stajfn, ‘mouth;  jawbone’,  Co.  stefenic,  ‘palate’.  Cp. stoma.
Derivatives:  stomach,  tr.  v.,  stomachal  (q.v.), stomach-ed,  adj.,  stomach-er,  n.,  stomach-ful, adj.,  stomachic  (q.v.),  stomach-less,  adj., stomach-y,  adj.
stomachal,  adj.,  pertaining  to  the  stomach.  —  See prec.  word  and  adj.  suff.  -al.
stomachic,  stomachical,  adj.,  1)  pertaining  to  the stomach ;  2)  digestive.  —  L.  stomachicus,  fr.  Gk. oxopa/ixoc,  ‘pertaining  to  the  stomach’,  fr. axopa/o;.  See  stomach  and  adj.  suff.  -ic,  resp. also  -al.
stomat-,  form  of  stomato-  before  a  vowel.
stomatitis,  n.,  inflammation  of  the  mucous  mem¬ brane  of  the  mouth  (med.)  —  Medical  L.,  form¬ ed  with  suff.  -itis  fr.  Gk.  axopa,  gen.  axopaxoc, ‘mouth’.  See  stoma.
stomato-,  before  a  vowel  stomat-,  combining  form meaning  ‘mouth’,  as  in  stomatology.  —  Gk. axopaxo-,  axopax-,  fr.  axopa,  gen.  axopa- xoc,  ‘mouth’.  See  stoma.
stomatology,  n.,  the  study  of  the  diseases  of  the mouth.  —  Compounded  of  stomato-  and  Gk. -Xoyta,  fr.  -Xoyop,  ‘one  who  speaks  (in  a  certain manner) ;  one  who  deals  (with  a  certa
```


## [2026-09-14T03:09:17.947Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ===\"; grep -n -i -B3 -A8 \"stomen\" AHD_watkins1985.txt | head -40\necho \"=== IEC (Mann) ===\"; grep -n -i \"stomen\\|stoma-\\|staman\" IEC.txt | head -15\necho \"=== SYN (Buck) mouth ===\"; grep -n -i \"stomen\\|staman\\|στόμα\\|stoma \" SYN.txt | head -15"
}
```


### [2026-09-14T03:09:18.071Z] TOOL RESULT

```
=== AHD watkins ===
1024-(s)teu-. To push, stick, knock, beat; with derivatives referring to projecting objects, fragments, and certain related expressive notions and qualities. I. Extended forms *steup-, steub-. 1. Germanic *staup- in Old English stéap, lofty, deep, projecting: STEEP!. 2. Germanic *staupilaz in Old English stypel, st@pel, steeple: STEEPLE. 3. Germanic *steup-, “bereft” (< “pushed out”), in Old English stéop-, step-: STEP-. 4. Germanic *stip- in Old English stipian, to stoop: stoop}. 5. Germanic expres- sive form *stubb- in Old English stubb, stybb, stump: STUB. 6. Germanic *stuf-, “fragment,” small coin, in
1025-steu(8)-
1026-Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
1027:ste-men-. Denoting various body parts and orifices. Greek stoma, mouth: STOMA, STOMACH, STOMATO-, (STO- MATOUS), -STOMY; ANASTOMOSIS, ANCYLOSTOMIASIS, PROSTOMIUM, SCYPHISTOMA. [Pok. stomen- 1035.] storo-. Starling. Germanic *staraz in Old English ster, starling: STARLING}. [Pok. storos 1036.]
1028-streb(h)-. To wind, turn. 1. Greek strephein, to wind, turn, twist (> strophion, headband): STREPTO-, STROP, STROPHE, STROPHOID, STROPHULUS; ANASTROPHE, APOS- TROPHE!, BOUSTROPHEDON, CATASTROPHE, DIASTRO- PHISM. 2. Unaspirated o-grade form *strob- in Greek strobos, a whirling, whirlwind (> strobilos, ball, pine cone): STROBILE; STROBOSCOPE. 3. Unaspirated zero-grade form *strb- in Greek strabos, a squinting: STRABISMUS; STRABOTOMY. [Pok. strebh- 1025.]
1029-strei-. To hiss, buzz. Imitative root. 1. Extended form *strid- in Latin stridére, to make a harsh sound: sTRI- DENT. 2. Extended variant form *trig- in Greek trismos, trigmus, a scream: TRISMUS. [Pok. 3. streig- 1036.] streig-. To stroke, rub, press. I. Basic form *streig-. 1. Germanic *strikan in Old English strican, to stroke: STRIKE. 2. Germanic diminutive *strik-ila- in Old Eng- lish stricel, implement for leveling grain: STRICKLE. 3. Germanic *strikén- in Old English strica, stroke, line: STREAK. II. O-grade form “stroig- in Germanic *straik- in Middle English stroke, stroke: STROKE. III. Zero-grade form *strig-. 1. Suffixed form *strig-d- in Latin striga, row of grain, furrow drawn lengthwise over the field: STRIGOSE. 2. Suffixed form *strig-yd- in Latin stria, furrow, channel: sTRIA. 3. Nasalized form *stri-n-g- in Latin stringere, to draw tight, press together: STRAIN}, STRAIT, STRICT, STRIGIL, STRINGENDO, STRINGENT; ASTRINGE, CONSTRAIN, DISTRAIN, PRESTIGE, RESTRICT. [Pok. 1. streig- 1036; 4. ster- 1028.] strenk-. Tight, narrow. Possible root. 1. O-grade form *stronk- in: a. Germanic “strangi- in Old English streng, string: STRING; b. Germanic *strangaz in Old English strang, strong, powerful, strict: STRONG; c. Germanic *strangithé in Old English strengthu, strength, strict- ness: STRENGTH. 2. Variant *strang- in: a. Greek strang- alé, halter: STRANGLE, (STRANGLES), (STRANGULATE);
1030-s(w)e-
1031-b. Greek stranx, drop (< “that which is squeezed out”): STRANGURY. [Pok. strenk-, streng- 1036.]
1032-strep-. To make a noise. Imitative root. Latin strepere, to make noise: OBSTREPEROUS. [Pok. (s)trep- 1037.]
1033-su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gia-es-, “living in good condition” (see g"ei-). [Pok. su- 1037.]
1034-sii-. Pig. Contracted from *sua-; probably a derivative of seue-'. 1. Suffixed form *sua-ino- in Germanic *swinam in Old English swin, swine: SWINE. 2. Celtic expressive form *sukko-, swine, snout of a swine, plowshare, in: a. British *hukk- in Old English hogg, hog: HoG; b. per- haps Old French soc, plowshare: SOCKET. 3. Germanic *sii- in Old English sugu, sow: sow?. 4. Latin sis, pig: soit’. 5. Greek hus, swine: HYENA; HYOSCINE. [Pok. su-s 1038.]
1035-stro-. Sour, salty, bitter. Germanic “siraz in: a. Old English sir, sour: SouR; b. Old High German sir, sour: SAUERBRATEN SAUERKRAUT; C. Old French sur, sour: SORRELI, [Pok. siir-o 1039.]
=== IEC (Mann) ===
17289:stomn- “mouth, open jaws, maw’. WP II, 648 Av. staman, m. ‘mouth’; Gk. stóma, n. id. and ‘opening’; Ir. stomán, m. ‘maw, paunch’; Br. staon, f. (1) ‘roof of mouth’; W cf. (va- riant) safn, f. pl. -au (jaw, fr. *stəmn-); Cor. sawn, pl. -yow, f. ‘gorge’
17525:sthāmn- (sthàmón-, -en-) “stand, stop, prop, fixture, firmness', etc. WP IL, 606 Skt. stháman, n. ‘station, seat, place, power’; Tokh. A stàm, B stam, s. ‘tree’, cf. B $mofifía ‘place’; Hitt. cf. stananas (queried: 'altar"); Gk. stéma, n. ‘stamen; warp’; stémōn, n. ‘warp’; Lat. stamen, m. “loaded distaff; stamen”; (in pl.) ‘stamina’; Umb. stahmei, ds. ‘stop’; Go. stom-, s. ‘material, basis; OHG gi-stuomi, adj. ‘restful’; W sawf, m., Br. saw, m. ‘stop, stand’ beside (LW ?) stoeven, Steen, f. ‘warp, woof; Srb. staman, f: stamna, adj. "old beside stamen, a, o, adj. “firm, sure’; Li. stomuó, gs: stomefis, m. ‘stature, build”. Cf. sthàn-
=== SYN (Buck) mouth ===
5926:2. Grk. orbpa: Av. staman- ‘dog’s mouth’, W. safn ‘mouth, jaws’ (of ani- mals), MBr. staffn, Br. staon ‘palate’, root connection? Walde-P. 2.648. Ped- ersen 1.78.
```


## [2026-09-14T03:09:19.642Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT staman ===\"; grep -n -i \"staman\" BRT.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"astam\\|staman\" HUB.txt | head -20\necho \"=== PHD ===\"; grep -n -i \"stam\\b\\|staman\" PHD*.txt 2>/dev/null | head; ls | grep -i \"PHD\\|NYB\""
}
```


### [2026-09-14T03:09:19.751Z] TOOL RESULT

```
=== BRT staman ===
7090:•)  Vgl.  die  Definitionen  F.  25  b :  iij;ri/l  l^ti/t] äir  ba!.-cl  ka  Satan  i  aiinäs  rai  siieA  a/Hir  i^Vcl und  bei  DsT.  ZA.  2.  54:  gj-Ailam  kila  iasyäfiy upari  gAStamanasJ-  iailram  gfAnati.
7852:mit  Kf 'einschnüren,  einzwängen':  ha  hi maiofm  nyäsala  "sie  schnürt  sich  ihre TaiUe"  Ytj.137'*.  a)  'hineinzwängen in  — '  (Akk.):  täst>m  däuru  .  .  stamanim he  aoat  nyszaym  ".  .  ein  zugeschnittenes Stück  Holz..;  in  sein  Maul  sollen  sie  es dann  hineinzwängen"  V, /J.30.
26557:•  j.  staman-  m.  'Maul',  nur  von  dem des  Hunds:  'manim  .^^(näml.  des  Hunds) . .  nySzaym  (Sp.  362  o.)  V.  ij.  30;  —  yat . . alte  ganma  (sd.)  :^an%a  •maram  vü Aizvam  v3  apa.daiat  (näml.  dem  Hund)
28628:j  N.  42;  —  spa  .  .  stamantm  kl  mai  nyä- saym  .  .  dasimm  hl  gaeiTtn  .  .  Aöyum  kl \gaosfm  upa^Wfrfsayitt  .  .  doTimtn  Al 'paßyqm  .  .  kaoyqm  hl  paiiyqm  upa.- ksr^ntay^n  .  .  dum^mcil  Al  (zu  a)  upa.- '^lionsaym  V.  13. 30  ff,;  8.  40,  5. 1 7  ff.  (oft), 49,  H.2.  18,  36;  —  Aavatianö  (sd.)  äaityS gatuÜ  .  .  Aaffyaj  *Al^^  *nalmat  Omatars R  7p;  *7P'^  Yl/o.  ioo',  126,  Ä  38,  V. 79.  2;  —  nairika  .  .  airime  (sd.)  gätüm ^?  (fem,;  zu  ß)  nisAihalta  V.i6.&;g.^^ (mask,);  —  ahmi  nairi . .  b^m/ayän/i  fsd.) /l . ,  mänh^m^a  hvarfca  aamca  Al{za  a) bfr^Jaim  V, 7.  52;  —  sünahe  .  .  asti  sl haHn  ya%a  a^aurune  V,  13.  44;  44'; —  yS  ga'hanqm  *anu.tnaiti  (sd.)  *afm.- mainyete . .  anyS  vä  hl  (zu  a)  daAmB  srvth ga%ä  dalaiti  N.  25;  —  azdibji. .  *usäan3m h  i (Plnr.)  alat  k^rmaot  Y.  6. 50; — *Aixsa»e . .  drvatqm  .  .  anyqm   i4?(PIur.)  avarptqta
=== HUB ===
611:apastam (Phi. Min. p. 11, Z. 5; 37, 4 v. u.) = alterem
616:ort' zu iibersetzen und mit Horn auf ^avastaman- (vgl.
3719:{hastam = zd. histami).
9084:veredrayna-; paz. awastam confidence, reliance' = phi.
=== PHD ===
PHD.txt:2991:oppression awištāb, handraxtagih, pazd, stahm, stahm(ag)ih, stam- bagih.
PHD.txt:3359:refuge abestam/n, panah; take ~ with pad рапаһ griftan.
PHD.txt:3898:support abestam/n, pušt, puštībānīh.
PHD_pages.txt:784: abestam ['pst'm] = abestan.
PHD_pages.txt:1314:awestam ['wst)m I M )wyst)m] province, district.
PHD_pages.txt:6448:district awestam, kust(ag), paygos,     dumb agowag, gung.
PHD_pages.txt:7362:pro'nince awestam, nahang, paygos,             rain (n.) waran.
PHD_pages.txt:7816:touch (v.) pahikaftan, pahrmah-,         trust abestam/n.
PHD_pages.txt:11350:abestam                                            afsay-
PHD_pages.txt:11899:a\Vestam                   .<tc.vt-'       xwamnwiziir                )....~,~~
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
```


## [2026-09-14T03:09:35.134Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r\"staman-\\s+m\\.\\s+'Maul'\", p):\n        print('BRT leaf',i)\n        cols=re.findall(r'\\b1[5-9]\\d\\d\\b',p)\n        print('col-numbers on leaf:',cols[:10])\n        j=p.find(\"staman-\")\n        print(p[max(0,j-300):j+500])\nEOF\necho \"=== NYB stam ===\"; grep -n -i \"stam\\b\" NYB_vol2_glossary.txt | head -10\necho \"=== BQT استم ===\"; grep -n \"استم\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-14T03:09:36.892Z] TOOL RESULT

```
BRT leaf 868
col-numbers on leaf: []
uV.): kac  an  slaxmakih.
•  j.  stawra-  Adj.  (fem.  -ra-)  'stark,  fest": mihrvin  .  .  yS  .  .  'ri  aikya  k?rmaoiti Yt.  10.  28.
Zum  V.  slamb-.  —  np.  silabr.
•  j.  "stanvS ''  v3  puili  paihi  davaisfie  vä" V.  7.  43  PÜZ-"-
0  So  Wo.    SP,  und  die  NA  des  FahlVend.:
•  j.  staman-  m.  'Maul',  nur  von  dem des  Hunds:  'manim  .^^(näml.  des  Hunds) . .  nySzaym  (Sp.  362  o.)  V.  ij.  30;  —  yat . . alte  ganma  (sd.)  :^an%a  •maram  vü Aizvam  v3  apa.daiat  (näml.  dem  Hund)
v./i.4-
Vgl,  gr.  Q-niia;  kymr.  la/«;  gani  unsicheres bei  Hirt  PBrB.  22. 223.  —  Pü. :  asiämak  (bei jAUASPji  GI0SS.  549  'gums").
•  j.,  g.  *stay-  £,  m.'>  'Wesen';  1)  'Sein, Dasein':  ßm  (näml.  katium)  mli  data dangahyä  ^yaol. .  vairyä  stSisyS  %waAmt x/a^r
=== NYB stam ===
542:apa-stam [’pst’m] reliance 725. 8215, — Paz. awastgm; for *apa-stān < *upa- stäna-; Arm lw. apastan ‘refuge, resort’. apastéh [’p’styh] support 8222. — < Olr *upa-ā-stā-, ci Av. (396) upa-stā- ‘assis- tance, help’. Paz. substitutes dasti. apa-sütak [’pswtk'] probably: treated with magic art, of a sword 2516, 2813, —
2124:but we are here in a part of Iran where Greeks reigned for about 200 years after Alexander (v. Tarn, The Greeks in Bactria & India, 1951). There is every reason to believe that their kings and magnates erected monumental buildings over their tombs, with which the Yvy1 of the de- ceased was in some way connected. The Greek Yvx1 could, however, only be ren- dered in Iranian by jän, as the ruvān belonged to a quite different sphere. Prob- ably these seven jdnakdns were built in the seven cities which Alexander founded in Bactriana and Sogdiana (Justin XII, 5, 8). The later attribution of such ancient monuments to the primordial heroes of East Iranian antiquity is a phenomenon too well known to need comment, cf Taxt + Jamsid, Nags 1 Rustam and the like. — Strictly speaking the reading HY?-d’n' = jän-dän 're- captacle of the jan’ would be admissible (cf uvnuciov Ļvxījg of the cinerary urn Sophocles, Electra 1126-1127), but this interpretation is perhaps too hazardous. — jānakān has a parallel in MPrs rw’ng’n, MPrth ’rw’ng’n ‘belonging to, serving the ruvan’, of pious works.
2285:ké-c hac amahraspandän Nerösang — u kē-c hac martömän Yam both sorts of good parentage, partly from the Amah- raspands (through) N. and partly from mankind (through) Y. 3917-18, — 4. conj. as, because 119 (kč-c). 122° (ké-m). 441? (kē či); so that 39!" (?). Later copyists use "MT = ka and MNW = ke promiseu- ously. — OIr gen. kahya from (422 sqq.) ka-. kém [kym] small, little, slight, = kam: 8619.20.22, 9016, — < *kambyah- comp. of kamna (v. kam), but used in the sense of the pos.; Av. (440) sup. adv. kambistam ‘least’; MPrs gmb (A-H II); Paz. kim, kem; MPrth kmbyg ‘short’, abstr. qmby ft, gmbystn ‘to empty’ (List 84).
3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
3537:statan [YNSBWN-tn'] stān-, to take, in all senses; imp. YNSBWN = stan 28?’. 70%; —-i (ending written in Paz.!) = stam 60%; the forms with the endings -X, and -x, function a) as imp. sg. = stané 911 (-x,). 44? (-x2); b) as pres. 3d p. sg. 2515. 2815, 29? (-x,); c) as pret. pass. 3d p. sg. 2813, 121? (-x,). 42°. 4821, 498.22, 5015, 6019 (.x,); inf. YNSBWN-tn' 77°. 7917, 8919, — FrP 21 both YNSBWN- and YNSBWN., Ir. equivalents ysttn' - yst*nyt' — yst'nym = istatan — istānēt — istaném, some MSS *sttn' — ’st’n- ete. = astatan — astän-; Paz. stadan stan- (Mx), stän- (Aog.); MPrthPrs pt. ‘std, pres. *s?n-, v. Verbum 189, Ghilain 71; NP sitadan sitdn-.
3635:*Sif(a)rg [Splg] of doubtful meaning, per- haps: swift arrow, ~ % Rotastahm swift Rustam-arrows, arrows swift as those shot by R. 20%, — The form is to
4528:its capital was Ghazna; it was the native country of Rustam. Cat. 88; Bailey, BSOS VI, 1931, 590; Gnoli, Ricerche storiche sul Sīstān antico, Roma 1967, v. Index.
4683:DNa = Dareios, Nagš i Rustam inscription a, according to Kent’s edition (q. v.).
6427:awastam: apastäm
7372:Rustam: Rötastahm
=== BQT استم ===
3061:- درکلیله ودمنه بارها «رای» استممال شده وآن ازلغت سانسکریت ۲2 بمعنی راجه
3591:هما نامیغو استم نوشت ومیدانستم نوشت » اما بسیب انبوهی بیان های ژو لیدة
3905:و نسخه‌های‌مغلوطراهم نمیخو استم بالاخره نا گز یر نسخه‌ای‌عار یت‌و « بر بط ناتمام
6175:باّب که خوبی ولیکی وقابلیت و کمال‌واستمداد
7832:فرهنگ جهانگیریت از ابهام و ابهام و قلیل الاستممال بودن کلم آسان فکن نشأت کرده است
9287:استماره چشم را نیز آهو مبگویند - و شاهد
10499:«روزشماری ۵٩-۵۷‏ » . ايشکه درمتن ارد بکسر اول بادشده برای استممال آن دراشمار فردوسی
11915:استم - بکس‌اوز رح ات و سکون
15540:مفپوم آنکاسته شده واین‌لفت م رکب‌بدمنی مملکت ابران استممال شده. راد: شمارٌ هفت وهفت
15887:بز رکمرا 880 202 گویند . درلانینی ۳3۳8 و درنازی‌هم باباستممل است «تفی» -
18070:بلندی هرچیز و استملا هم هست - و بار درخت
19558:زه رگونه‌ای نعام آراستم بگفتم درآن هر چه خودخواستم
19844:کند و استمداد نماید - و ضصک و اراد هکند ۸ .
20232:داشته . شکل 1381020 یشتر استممال ميشده است *دالرتالمعارف اسلام». اين شهر را منصور
30507:ازچیز» استمال شود.
31401:دومشخص مفرد (مفرد مکلطب). فردوسی هم 40 وهم 8۵ استممال کرده . پارسی باستان ۱1۷860
31630:عمتی دیواته ووحشی اراده کرده‌اند چنانکه‌در لهج کردی و کیلکی بهمن معنی استمسال هیشود.
```


## [2026-09-14T03:09:45.373Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11905,11930p' BQT_v1_pages.txt\necho \"=== find pdf page tag ===\"\nawk 'NR<=11930 && /\\[pdf page/ {p=$0} END{print p}' BQT_v1_pages.txt\necho \"=== BRT cols on leaves 860-875 ===\"\npython3 - <<'EOF'\nimport re\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in range(862,874):\n    nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$',pages[i])\n    nums2=re.findall(r'\\b1[5-7][0-9]{2}\\b',pages[i])\n    print(i, nums, nums2[:6])\nEOF"
}
```


### [2026-09-14T03:09:46.720Z] TOOL RESULT

```
دلیری وجانبازی کردن باشد .
استطلس- بکسر اول وفتح تاث وضم
لام و سکون ثانی و طا وسین می نفطه » یلفت
بوئانی نوعی از حومیابی باشد و آن مانند زفت
است و بوی قیی از آن می‌آید و در شکستکی
و کوفتگیاعضا عمل‌مومیابیمیکندرآنرا مومیابی
تتانی رسیده ولام یال 9 ار بوده
نورانی درلشگر افراسیاب .*3
استل « بکر اول وفتح ناك‌وسکون.
ثانی و لام ؛ تالاب و آبگیر و ب رکه وأمنخر
استم - بکس‌اوز رح ات و سکون
ثالی ومیم » ستم وجور وظلم را گوند
استن - بنم اول و الث و کون انی
استنبه - با نون بر وزن اشکنبه » » هر
چبز زشت را کوبند مطلقاً وسورتی باشد بفایت
کربه‌منظ رکه طبم ازدیدنش‌رمان‌وهراسان کردد-
وسنگینی را لیز کوبن که درخواب برمردم افتد
۵ ,در متن ناء زاید است
ستر ( از مصدر استردن
۴ رکه : استخر .وت ۱ تیم
استوی بش اول والث بر وزت بر
کوی » مهر پشت را کویند .
استه * ه ختح اول بروزن خسته , دالةٌ.
خرما و شفتالو و زردآ لو ء امثال آبرا کوبند -
واستضوانآ دمی‌وحبوانات. دبگررایز گفتهان -
وضم اول کفل وسرین را کوبند -و بکر اول
=== find pdf page tag ===

=== BRT cols on leaves 860-875 ===
862 ['1579'] ['1579', '1580']
863 [] []
864 [] []
865 ['1586'] ['1585', '1586']
866 [] []
867 [] ['1589', '1590']
868 [] []
869 ['1594'] ['1594']
870 ['1596'] ['1596']
871 [] []
872 ['1599'] ['1599']
873 [] []
```


## [2026-09-14T03:09:59.702Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in (284,285,286,287,288):\n    print('=== leaf',i,'printed p.',i-21,'===')\n    print(pages[i][:300])\nEOF"
}
```


### [2026-09-14T03:10:00.769Z] TOOL RESULT

```
=== leaf 284 printed p. 263 ===
A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos*, a/^ar(i)sn *das Nichtessen , aguftar 'nicht
sprechend' u. v. m.
ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
ai. a-, an-; arm. aw- (H. No. 20).
oss. d. t. «-, ä- (1).
Das Neupersische hat a-, an- aufgegeben (Fäll
=== leaf 285 printed p. 264 ===
- 264 —
4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
(i)sn.
Scheint ein Causativuni mit der gewöhnlichen phlv.
Endung -imtan (np. dagegen -ämdeN) zu sein. Bar-
tholomae denkt dagegen nach briefl. Mitteilung an
Zusammenhang mit aw. hisidyät etc. (vergl. oben
No. 922).
5. agräl, agre Vortreff
=== leaf 286 printed p. 265 ===
- 265 -
12. anaiv nicht arisch; boshaft, feindlich*, anainh (Men.).
aw. miairya-,
np. ener schlechter Charakter ist unbelegt (die laut-
gesetzliche Form müsste nEr lauten), die Riväyets
haben arier als ^ungehorsam'.
13. anäklh 'Unheil etc.'
Das sehr häufige Wort ist aufgegeben; das seltene
anäk (AV.
=== leaf 287 printed p. 266 ===
— 266 —
18. aniifnal ^Kleinvieh*.
aw. anumaya- 'Kleinvieh'. Wohl nur Transcription
des Awestawortes.
19. apavTk 'später, anderer, übrig; der Rest' (päz. aware),
ap. aparam nachher ; aw. apara-, ai. äpara- 'hinterer,
späterer.
20. apastän Vertrauen , sehr häufig auf Gemmen ; arm.
LW. apastan,
skr. up
=== leaf 288 printed p. 267 ===
— 267 —
27. äsn natürlich, eigen (AW.-Komm., Mön.).
aw. asna- angeboren, natürlich, eigen* (Geld n er,
KZ. 24, 131/2).
28. aspastän 'Pferdestall'; arm. LW. aspastan.
aw. aspöMäna- Pferdestall'; skr. agvasthamt'.
Vergl. auch phlv. tistrastän 'Kameelstall*, göstän
'Kuhstair.
29. dHpräs 'Pferdeweg, Ren
```


## [2026-09-14T03:10:08.753Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in (281,282,283):\n    print('=== leaf',i,'printed p.',i-21,'===')\n    print(pages[i][:900])\nEOF"
}
```


### [2026-09-14T03:10:09.846Z] TOOL RESULT

```
=== leaf 281 printed p. 260 ===

=== leaf 282 printed p. 261 ===
VERLORENES SPRACHGÜT.
=== leaf 283 printed p. 262 ===
```


## [2026-09-14T03:10:19.052Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT stomach ===\"; grep -n -A3 \"^stomach\\|stomach\\.\" SKT.txt | grep -i -m5 -A3 \"stomach\"\necho; echo \"=== FSD vol4 stomach ===\"; grep -n \"stomachus\" FSD_vol4.txt | head -5\necho; echo \"=== MON استام ===\"; grep -n \"اَستَم\\|استام\" MON_part1.txt MON_part2.txt | head -10\necho; echo \"=== ARY ===\"; ls | grep -i ARY"
}
```


### [2026-09-14T03:10:19.178Z] TOOL RESULT

```
=== SKT stomach ===
11267:Maw,  stomach.  (E.)  M.E.  imiiM.  A.S. maga.'^  Du.  nuxag,  Icel.  magi,  Swed.  magt, Dan.  mave,  G.  magtn.  ^Perhaps  from VMAGH.)
11268-Mawkieh ;  see  Moth.
11269-MAzUlar.  Maxillary ;  see  Maoorate.
11270-MazilXli  ^ff*^Tnum  ;  see  Magnitude.
--
11530:midriff,  the  diaphragm  separating  the heart  from  the  stomach.  Sic.  (E.>  M.  E. midrif.  A,  S.  midrt/{\oT  midAh/).^  A.  S. mid,  middle  ;  Art/,  the  belly.  4-  O.  Fries. midrtfx  from  miV,  middle,  rt/;  rif  the belly.
11531-midship,  short  for  amid-ship\  hcoca
11532-midst,  the  middle.  (E.)  Im  middest, Si:>en«r.  F.  Q.  vi.  3.  35  ;  formed,  with  added t,  from  M.  £.  in  middes,  equivalent  to amiddis ;  see  amid  (above).
11533-midwife.  (F..)  M  K  midwif;  rarelv mtdrwif»  from  a  false  etymology  which connected  it  with  M.E.  witdt  or  m€(d,  re* ward.  ~  A.  S.  mid,  prep.,  together  with; wlf  a  woman.  Thus  the  liL  sense  '  a woman  who  is  with  another,*  a  helper. CC  A.  S.  mid-wyrcan,  10  work  with.  So also  Span,  co-mai/rt,  lit.  *  co-mother,'  a midwife.  Cf.  Da.  mtdiAtlpen^  to  assist (from  medt,  with,  Aelp^n,  to  help);  G.  *»/• helftr,  a  helper  with,  assistant.

=== FSD vol4 stomach ===
23102:G   P   R   Jameb  Arrah  Neil  p   53  (r  a   a   ) 2   [Rare]  To  nauseate,  disgust  Sf  To  remember With  anger  if.  To  inspire  with  courage,  embolden lly.  t   Po  become  angry  I   <   L   storna^or,  be  angrj', <   stomachus,  see  stomach,  n   \ stom'ach,  In  1.  An  anterior  dilatation  or  senes  of  dila- stuiu  ac**,  J   tations  of  the  alimentary  canal,  serving  as one  of  the  principal organs  of  digestion,  a digestive  cavity In  man  the  stomach Is  pyriform,  and  lies obliquely  In  the  up- per part  of  the  abdo- men mostly  toward  the left,  between  the  esoph- agus and  duodenum The  mucous  lining  is thickly  beset  with  tu- bular glands  of  two kinds  the  most  Im- portant being  the  pep- tic glands,  which  elab- orate  the  gastric Juice  Beyond  the mucous  lining  Isalayer of  loose  connective  tis- sue covered  bj  a   mus-  Human  Stomach  with  the  Adjacent, cular  coat  of  longltudl-  Viscera,  viewed  from  the  front nal,  transverse,  and  l   Aorta  2   Esophagus  3   Dia- obllque  fibers  over  phragm  4   Inferior  %ena  cava  5 which  there  is  an  outer  Portal  vem  6   Stomach  7   Spleen, serous  membrane  In  8   Suprarenal  capsule  9   Gall  bladder- many  mammals  tho  Duodenum  11  Pancreas  12  Je- Btomach  is  more  com-  Kidneys
23105:3.  Desire  of  food,  appetite,  hence,  an>  desire,  fondness; inclination,  hlung  af.  Anger,  sullonness,  resentment, stubbornness  5t»  Pride,  haughtiness  Cf  Compas- sion 7t»  Spirit  Sf.  The  mouth,  gullet  1<F mac,  <   L   stomachus,  <   Gr  stoniachos,  <   stoma,  mouth  J

=== MON استام ===
MON_part2.txt:69187:شت شود استامپ. مهر انگشت: (فره.) اثر 
MON_part1.txt:11303:استام: ماع (.) آتش کاو آهنین؛ محش» 
MON_part1.txt:11309:استام: صقاعه [ « اوستام ِ ستام] (.) زین و 
MON_part1.txt:11312:استامو لی: 001-1ههای [- استانبولی] 
MON_part1.txt:11313:(ص‌نسب.) منسوب به استامبول (- استانبول). 
MON_part1.txt:11314:کالایی که در استامول سازند و صادر کنند. 
MON_part1.txt:11315:اهل استامبول» از مردم استامبول. زبان ترکی 
MON_part1.txt:11316:که در استامبول بدان سخن می‌گویند. ترکی 
MON_part1.txt:11317:استامبولی: زبان ترکی که در استامبول و تمام 
MON_part1.txt:11321:استامپ: اه (۰.) تصویری که پس از 

=== ARY ===
NYB_vol2_glossary.txt
```


## [2026-09-14T03:10:25.362Z] TOOL CALL #18: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo ===; grep -n \"استم\" data/verification/sources/refs/MON_part1.txt | head"
}
```


### [2026-09-14T03:10:25.420Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-14T03:10:29.747Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CF%83%CF%84%CF%8C%CE%BC%CE%B1' --note 'page 483, root Stomen, Greek stoma etymology' \npython3 tools/fetch_source.py 'https://www.etymonline.com/word/stomach' --note 'page 483, English stomach chain'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/stomachus' --note 'page 483, Latin stomachus from Greek stomachos'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steh%E2%82%82-' --note 'page 483, PIE root check'"
}
```


### [2026-09-14T03:10:32.750Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b059f0aba1bb7827.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e313d865a75894ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2550cda19e4f496.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dd2e100b6c8ace7.txt
```


## [2026-09-14T03:10:34.381Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## stoma\"; grep -n -i -A25 \"Etymology\" b059f0aba1bb7827.txt | head -60"
}
```


### [2026-09-14T03:10:34.444Z] TOOL RESULT

```
########## stoma
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Declension 
75-
76- 1.4.2 
77- Derived terms 
78-
79- 1.4.3 
80- Related terms 
81-
82- 1.4.4 
83- Descendants 
84-
85- 1.5 
86- References 
87-
88- 1.6 
89- Further reading 
90-
--
97: Etymology 
98-
99- 2.2 
100- Pronunciation 
101-
102- 2.3 
103- Noun 
104-
105- 2.3.1 
106- Declension 
107-
108- 2.4 
109- Further reading 
110-
111- Toggle the table of contents 
112-
113- στόμα 
114-
115- 33 languages 
116-
117- Azərbaycanca 
118- Čeština 
119- Dansk 
120- Deutsch 
121- Ελληνικά 
122- Español 
--
238: Etymology
239- [ edit ] 
240-
241- From Proto-Indo-European *stéh₃mn̥ ( “ mouth; muzzle ” ) . Cognate with Avestan 𐬯𐬙𐬀𐬨𐬀𐬥 ( staman , “ mouth [of a dog] ” ) , Welsh safn ( “ mouth; jaws ” ) , Hittite 𒅖𒋫𒈪𒈾𒀸 ( iš-ta-mi-na-aš /⁠ištāman-⁠/ , “ ear ” ) , as well as, despite Beekes's objections, Proto-Germanic *stebnō ( “ voice; sound ” ) . [ 1 ] 
242-
243- Compare typologically Russian у́стье ( ústʹje ) , у́стьице ( ústʹice ) (akin to уста́ ( ustá ) ).
```


## [2026-09-14T03:10:46.551Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### etymonline stomach\"; grep -n -i \"stomach (n\" -A12 e313d865a75894ab.txt | head -40\necho; echo \"##### latin stomachus\"; grep -n -i -A8 \"^ Etymology$\" f2550cda19e4f496.txt | head -40"
}
```


### [2026-09-14T03:10:47.584Z] TOOL RESULT

```
##### etymonline stomach
23: stomach (n.) 
24-
25- late 14c. variant of earlier stomake (early 14c.), "the human stomach, internal pouch of the body into which food is digested," from Old French stomaque , estomac "stomach," from Latin stomachus "throat, gullet; stomach," also "taste, inclination, liking; distaste, dislike;" also "pride, indignation," which were thought to have their origin in that organ (source also of Spanish estómago , Italian stomaco ), from Greek stomakhos "throat, gullet, esophagus," literally "mouth, opening," from stoma "mouth" (see stoma ). The native word is maw (Old English maga glosses stomachus ).
26-
27- Applied anciently to the openings of various internal organs, especially that of the stomach, then by the later Greek physicians to the stomach itself.
28-
29- Some 16c. anatomists tried to correct the sense of the word back to "esophagus" and introduce ventricle for what we call the stomach. The meaning "belly, midriff, surface of the body over the stomach" is from c. 1400.
30-
31- In Middle English also stomack, stomac, stommak, stomoke; the spelling of the ending of the word was conformed to Latin regularly from 16c., but the pronunciation remains as in Middle English. A 19c. attempt to make it look as it sounds yielded stummik (1888), stummock .
32-
33- Related: Stomachal (1580s); stomachical (c. 1600); stomachic (1650s). Stomachous (1540s), stomachate (1540s, from Latin stomachatus ) seem to have been used only in figurative senses.
34-
35- The classical figurative senses also were in Middle English, such as "relish, inclination, desire; courage, spirit; inmost thoughts, consciousness; temper, disposition" (mid-15c.) or early Modern English, when the stomach was regarded as the seat of thought and emotion as well as hunger. It also sometimes was regarded in Middle Ages as the seat of sexual desire.
--
40: "tolerate, put up with," 1570s, from stomach (n.), probably in reference to digestion. The earlier sense of the verb was rather opposite, "be offended at, resent" (1520s, now obsolete), echoing Latin stomachari "to be resentful, be irritated, be angry," from stomachus (n.) in its secondary sense of "pride, indignation" (see the noun). For this sense also compare Old English  belgan  (v.) "to become angry," literally "to belly," probably from the notion of "swelling."
41-
42- A literal sense of "take into the stomach and digest" is attested from 1822, more or less facetious (Praed, the satirist); OED calls it nonce-use." Related: Stomached ; stomaching .
43- also from 1570s 
44-
45- Entries linking to stomach 
46-
47- maw (n.) 
48-
49- Middle English maue , from Old English maga "stomach" (of men and animals, including fish and birds; in Modern English only of animals unless insultingly of humans), from Proto-Germanic *magan- "bag, stomach" (source also of Old Frisian maga , Old Norse magi , Danish mave , Middle Dutch maghe , Dutch maag , Old High German mago , German Magen "stomach"), from PIE *mak- "leather bag" (source also of Welsh megin "bellows," Lithuanian makas , Old Church Slavonic mošina "bag, pouch"). Meaning "throat, gullet" is from late 14c. Metaphoric of voracity from late 14c.
50-
51- stoma (n.) 
52-

##### latin stomachus
160: Etymology
161- [ edit ] 
162-
163- From Ancient Greek στόμαχος ( stómakhos ) .
164-
165- Pronunciation
166- [ edit ] 
167-
168- ( Classical Latin ) IPA ( key ) : [ˈstɔ.ma.kʰʊs]
```


## [2026-09-14T03:10:56.300Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/st%C3%A9h%E2%82%83mn%CC%A5' --note 'page 483, PIE *stéh₃mn̥ mouth - root box check'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%F0%90%AC%99%F0%90%AC%99%F0%90%AC%A8%F0%90%AC%A5%F0%90%AC%A7' --note 'page 483, Avestan staman attempt' 2>/dev/null | tail -1"
}
```


### [2026-09-14T03:10:59.468Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e67f7f6a1e228ead.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01a493ac8c87f69b.txt
```


## [2026-09-14T03:11:02.732Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### recon\"; sed -n '1,40p;200,300p' e67f7f6a1e228ead.txt | grep -n -i \"mouth\\|Descendants\\|Avestan\\|Greek\\|Hittite\\|Proto-Ira\" | head -30\necho \"---- raw tail\"; grep -n -i \"stéh₃mn\\|Avestan\\|Hittite\\|Root\\|mouth\" e67f7f6a1e228ead.txt | sed -n '1,40p'"
}
```


### [2026-09-14T03:11:02.834Z] TOOL RESULT

```
### recon
121: According to Kloekhorst, the Luwian term requires a pre-form of the shape *stHm-en- , and the Greek evidence confirms that the laryngeal was *h₃ . [ 1 ] Kroonen, however, argues that the Germanic evidence for e-grade vocalism renders the reconstruction *stéh₃mn̥ ~ *sth₃méns impossible. [ 5 ] The short-vowel in Avestan 𐬯𐬙𐬀𐬨𐬀𐬥 ( staman ) is unexpected; a pre-form *stéh₃mn̥ should have yielded **𐬯𐬙𐬁𐬨𐬀𐬥 ( **stāman ) . However, according to Lubotsky, vowels in Avestan are often unreliable, and unetymological short vowels sometimes appear before clitics. Given that in both attestations of 𐬯𐬙𐬀𐬨𐬀𐬥 ( staman ) the term appears before clitics, it is possible that the short vowel is secondary. [ 6 ] 
123: As an alternative to the reconstruction *stéh₃mn̥ , Melchert posits a reconstruction *stómh₁-mn̥ , which could have undergone laryngeal loss via the Saussure-Hirt effect, yielding *stómmn̥ , which itself would have undergone degemination, producing *stómn̥ . According to this theory, the Hittite term actually derives from *stomh₁-mén- , itself an internal derivative of *stómh₁-mn̥ . This theory does require the reconstruction of an otherwise rare type of acrostatic *mn̥ -stem, though—as justification for this reconstruction—Melchert compares πῶμα ( pôma ) . [ 2 ] 
125: Descendants
129: Hittite: 𒅖𒋫𒈪𒈾𒀸 ( iš-ta-mi-na-aš , “ ear ” ) 
138: Ancient Greek: στόμα   n ( stóma , “ mouth, face ” ) 
141: Proto-Iranian: 
---- raw tail
4:TITLE: Reconstruction:Proto-Indo-European/stéh₃mn̥ - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/stéh₃mn̥ - Wiktionary, the free dictionary 
87: Reconstruction:Proto-Indo-European/ stéh₃mn̥ 
141: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
149: Seemingly from an otherwise unattested root *steh₃- suffix with *-mn̥ . [ 1 ] Another possible derivative of the underlying root is present in στωμύλος ( stōmúlos , “ wordy, loquacious ” ) , though—according to the etymology advanced by Vine—it would actually implying a root *stem- , which is incompatible with the reconstruction proffered by Kloekhorst. [ 2 ] 
154: *stéh₃mn̥   n [ 1 ] [ 3 ] 
156: mouth 
179: *stéh₃mn̥ 
199: *stéh₃mn̥ 
209: *stéh₃mn̥ 
219: *stéh₃mn̥ 
280: According to Kloekhorst, the Luwian term requires a pre-form of the shape *stHm-en- , and the Greek evidence confirms that the laryngeal was *h₃ . [ 1 ] Kroonen, however, argues that the Germanic evidence for e-grade vocalism renders the reconstruction *stéh₃mn̥ ~ *sth₃méns impossible. [ 5 ] The short-vowel in Avestan 𐬯𐬙𐬀𐬨𐬀𐬥 ( staman ) is unexpected; a pre-form *stéh₃mn̥ should have yielded **𐬯𐬙𐬁𐬨𐬀𐬥 ( **stāman ) . However, according to Lubotsky, vowels in Avestan are often unreliable, and unetymological short vowels sometimes appear before clitics. Given that in both attestations of 𐬯𐬙𐬀𐬨𐬀𐬥 ( staman ) the term appears before clitics, it is possible that the short vowel is secondary. [ 6 ] 
282: As an alternative to the reconstruction *stéh₃mn̥ , Melchert posits a reconstruction *stómh₁-mn̥ , which could have undergone laryngeal loss via the Saussure-Hirt effect, yielding *stómmn̥ , which itself would have undergone degemination, producing *stómn̥ . According to this theory, the Hittite term actually derives from *stomh₁-mén- , itself an internal derivative of *stómh₁-mn̥ . This theory does require the reconstruction of an otherwise rare type of acrostatic *mn̥ -stem, though—as justification for this reconstruction—Melchert compares πῶμα ( pôma ) . [ 2 ] 
288: Hittite: 𒅖𒋫𒈪𒈾𒀸 ( iš-ta-mi-na-aš , “ ear ” ) 
297: Ancient Greek: στόμα   n ( stóma , “ mouth, face ” ) 
301: Avestan: 𐬯𐬙𐬀𐬨𐬀𐬥   m ( staman , “ maw ” ) 
306: ↑ 1.0 1.1 1.2 Kloekhorst, Alwin ( 2008 ), “ištāman- / ištamin-”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , pages 411-412 : “ *stéh₃-mn / *sth₃-mén-s ” 
325: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/stéh₃mn̥&oldid=91961011 "
332: ine-pro:Mouth 
369: Reconstruction:Proto-Indo-European/ stéh₃mn̥
```


## [2026-09-14T03:11:06.569Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '285,305p' e67f7f6a1e228ead.txt"
}
```


### [2026-09-14T03:11:06.620Z] TOOL RESULT

```
 [ edit ] 

 Proto-Anatolian: 
 Hittite: 𒅖𒋫𒈪𒈾𒀸 ( iš-ta-mi-na-aš , “ ear ” ) 

 Luwian: [script needed] ( tum-ma-a-an , “ ear ” , nom-acc.pl ) 

 Proto-Celtic: *stamnā   f ( perhaps via *sth₃m-n- ) [ 7 ] 

 ⇒ Proto-Germanic: *stebnō   f ( “ voice, sound ” ) ( via *stem-n-eh₂ ) 

 Proto-Hellenic: 
 Ancient Greek: στόμα   n ( stóma , “ mouth, face ” ) 

 Proto-Indo-Iranian: 
 Proto-Iranian: 
 Avestan: 𐬯𐬙𐬀𐬨𐬀𐬥   m ( staman , “ maw ” ) 

 References
 [ edit ]
```


## [2026-09-14T03:11:11.867Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\ndata=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nprint(len(pages))\nfor i in (652,653,654):\n    p=pages[i]\n    print('=== leaf',i,'printed',i-5,'===')\n    print(p[:200].replace('\\n',' '))\n    if 'staman' in p or 'stomen' in p or 'stōmen' in p:\n        j=max(p.find('stomen'),p.find('staman'))\n        print('HIT:', p[max(0,j-600):j+900])\nEOF"
}
```


### [2026-09-14T03:11:12.891Z] TOOL RESULT

```
725
=== leaf 652 printed 647 ===
                                                                                    ;     648                                                 stomen-   noch die andere Bed. „Terdiehteii“ unmittelbar f
HIT: d, eingeti’etene FuBspur“, oxi^dg,
-ddog „aufgehauftes und zusammengedriicktes Lager von Streu oder Strok
usw.“, oxoi^ri „das Stopfen, zum Stopfen vervvendetes Wollhaar oder Flachs-
seide^, axoi^d^co „haufe an“, oxt^rj „Reif“ (ygl, ttcE^o?,              nd/v^ ds.   :   n^yvvpi)-
tFber   ir.   toeb      s.   u. steigu- „Scbulter‘^
  Ygl. zu diesen Gruppen Curtius 214, J. Schmidt Yoc. I 129 f., Kretsch-
mer KZ. 31, 383, Fick       568, III^ 492, Persson Y^zerw. 116, 178f., Beitr.
712 f., Zupitza Gutt. 45, Prellwitz, Boisacq, Yf. LEWb.^ s. yv., Trautmann
Apr. 429.


stomen-       jjMund^^.
  Ay. staman- n. „Maul (yom Hundj^"; gr. oxopa n. ^Mund"^, oxopaypg (Ygl.
zum -^/zo-Pormans Bgm. IP 1, 486, 513) „Kehle, Miindung (der Blase, des
Uterus);      Magenmund,            endlich       Magen“; dehnstufig oxo^pvkog „muadfertig,
geschwatzig; hubsch oder artig plaudernd^, oxcopvXloj „plaudere, schwatze“,
oxcopvXia „Redseligkeit, Geschwatzigkeit^^ (daB Yed. stamu-li etwa „tonend,
stohnend^ bedeute und verwandt sei, ist unsicher; s. Fick I ^ 146, 332,
570. Uhlenbeck Ai. Wb. 343 f., L. Meyer Hdb. lY 158. Got. usw, munps
„Mund“ ist nieht nach Hirt PBrB. 22, 228 als stmnto- mit gr, oxopax- zu
Yergleichen) cymr. safn „Kinnlade “5 corn, stefenic „Gaumen^^, mbret. staffn.^
                    ;


nbret. staon ds., cymr. ystefaig ds., abret. istomid ds. (brit. a aus o s. zum           ;


Kelt. Fick II^ 312, Pedersen KG. I 78, Jones ^Yelsh Gr. 109, 149).
   Sowohl wegen der Bed. („Stimme^ aus „
=== leaf 653 printed 648 ===
                                                                                                 ^                                            stores, stornos (strnos?)          — (s)trep-             
=== leaf 654 printed 649 ===
650                                       strenk-, streng-    KZ. 36, 274; der Anklang an gr. '&g^vog mahnt trotz des e zur Yorsicht); hi, prefa ^zanken^',       ahl.prapt n. „garrulitas", ags. prceft
```


## [2026-09-14T03:11:21.888Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f,off in (('IEC.txt',None),('SYN.txt',24),('AHD_watkins1985.txt',29),('SKT.txt',20),('FSD_vol4.txt',None)):\n    data=open(f,encoding='utf-8',errors='replace').read()\n    pages=data.split('\\f')\n    for i,p in enumerate(pages):\n        if re.search(r'stomn-|staman|stə-men|ste-men|stomachus,\\s*<', p):\n            print(f,'leaf',i, 'printed~', (i-off) if off else '?')\nEOF\nls /home/sfmqrb/git/rishe/data/verification/sources/refs | grep -iE \"ARY|aryan\"\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['ARY'],ensure_ascii=False))\""
}
```


### [2026-09-14T03:11:23.252Z] TOOL RESULT

```
IEC.txt leaf 712 printed~ ?
IEC.txt leaf 722 printed~ ?
SYN.txt leaf 264 printed~ 240
AHD_watkins1985.txt leaf 97 printed~ 68
AHD_watkins1985.txt leaf 112 printed~ 83
AHD_watkins1985.txt leaf 132 printed~ 103
AHD_watkins1985.txt leaf 135 printed~ 106
AHD_watkins1985.txt leaf 137 printed~ 108
FSD_vol4.txt leaf 219 printed~ ?
FSD_vol4.txt leaf 244 printed~ ?
NYB_vol2_glossary.txt
{"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1", "scans": [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}], "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"}
```


## [2026-09-14T03:11:25.647Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n -i \"STOMEN\\|staman\\|stomach\" ARY_latin_index_pages.txt | head -10\necho \"=== fas ===\"; grep -n \"اَستَم\\|استم \" ARY_pages.txt | head -10"
}
```


### [2026-09-14T03:11:25.721Z] TOOL RESULT

```
=== fas ===
```


## [2026-09-14T03:11:33.296Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in (712,722):\n    p=pages[i]\n    print('leaf',i,'has stomn-' if 'stomn-' in p else 'has sthamn', '| printed approx', (i-15)*2)\n    nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*',p)\n    print('nums',nums[:8])\nEOF"
}
```


### [2026-09-14T03:11:34.536Z] TOOL RESULT

```
leaf 712 has stomn- | printed approx 1394
nums ['1292', '1293']
leaf 722 has sthamn | printed approx 1414
nums ['1310', '1311']
```


## [2026-09-14T03:12:00.857Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T03:12:00.923Z] TOOL RESULT

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


## [2026-09-14T03:12:02.029Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:15:06.317Z] TOOL CALL #30: Bash

```json
{
 "command": "cat > data/verification/page-483.json <<'JSONEOF'\n{\n  \"pdf_page\": 483,\n  \"book_page\": 453,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Stomen\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *stomen- 'mouth' (Pokorny 1035); modern notation *stéh₃mn̥ (Kloekhorst 2008), Watkins *stə-men-\",\n      \"note\": \"Pokorny IEW p.1035 heads the entry exactly 'stomen- ,Mund'' and gives precisely the two branches Nourai draws: 'av. staman- n. ,Maul (vom Hund)'; gr. στόμα n. ,Mund', στόμαχος … ,Kehle, Mündung …; Magenmund, Magen''. Walde-Pokorny II 648 has the same article. The reconstruction survives in current scholarship as *stéh₃mn̥ 'mouth, muzzle' (Kloekhorst, Etym. Dict. of the Hittite Inherited Lexicon 411-412, from the Hittite ištāman- 'ear'); Watkins/AHD writes *stə-men- and glosses it 'denoting various body parts and orifices', citing Pok. stomen- 1035. The o-vocalism of Pokorny's *stomen- is the Greek reflex of *-eh₃-; the language label 'Indo-European' and the gloss 'mouth' are both correct. The one caveat worth recording is that the root is poorly attested (Greek + Avestan + Anatolian + Celtic only) and Buck (Synonyms 4.24) prints 'root connection?'; Kroonen and Melchert dispute the exact shape (*stómh₁-mn̥ is Melchert's alternative), but nobody disputes that Gk. στόμα and Av. staman- belong together.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *stomen- «دهان» است؛ پوکورنی در صفحهٔ ۱۰۳۵ فرهنگ ریشه‌شناسی خود دقیقاً همین مدخل را با همین معنا آورده و تنها دو شاخهٔ اوستایی staman- و یونانی στόμα را برای آن برشمرده است — یعنی همان دو شاخه‌ای که نورایی رسم کرده است. در بازسازی امروزی (کلوکهورست ۲۰۰۸، بر پایهٔ هیتّیِ ištāman- «گوش») این ریشه را *stéh₃mn̥ می‌نویسند و واتکینز در پیوست فرهنگ American Heritage آن را *stə-men- آورده است؛ هر سه صورت یک ریشه‌اند و اختلاف تنها در شیوهٔ نشان دادن حنجرهٔ (laryngeal) هندواروپایی است. باید افزود که این ریشه گواهِ چندانی ندارد (تنها یونانی، اوستایی، آناتولیایی و سِلتی) و باک در «فرهنگ مترادف‌ها» با تردید نوشته «پیوند ریشه‌ای؟»، ولی در پیوندِ στόμα یونانی با staman- اوستایی تردیدی نیست. برچسب زبانی و معنای ریشه در نمودار نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stéh₃mn̥\",\n        \"https://en.wiktionary.org/wiki/στόμα\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1035\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 277 (printed p.1035, the '1035' page marker stands just above and '1036' just below the entry): '…men- ,Mund'. [a]v. staman- n. ,Maul (vom Hund)'; gr. στόμα n. ,Mund', στόμαχος (-χο-Formans) ,Kehle, Mündung (der Blase, des Uterus); Magenmund, Magen' … WP. II 648.' Grep: grep -n -i 'staman' POK_03.txt. Root name, language label and gloss are exactly Nourai's.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 648 (incoming/WLD/WLD_Bd2_pages.txt leaf 652)\", \"stance\": \"supports\", \"note\": \"'stomen- \\\"Mund\\\". Av. staman- n. \\\"Maul (vom Hund)\\\"; gr. στόμα n. \\\"Mund\\\", στόμαχος … \\\"Kehle, Mündung (der Blase, des Uterus); Magenmund, endlich Magen\\\" … cymr. safn \\\"Kinnlade\\\", corn. stefenic \\\"Gaumen\\\", mbret. staffn' — Walde-Pokorny is the source Pokorny 1035 itself refers to.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 68 (AHD_watkins1985.txt leaf 97)\", \"stance\": \"supports\", \"note\": \"'stə-men-. Denoting various body parts and orifices. Greek stoma, mouth: STOMA, STOMACH, STOMATO-, -STOMY; ANASTOMOSIS … [Pok. stomen- 1035.]' — same root, same Pokorny page, Watkins listing only the Greek branch.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, cols./pp. 1292-1293 (IEC.txt leaf 712) s.v. stomn-\", \"stance\": \"supports\", \"note\": \"'stomn- \\\"mouth, open jaws, maw\\\". WP II, 648. Av. staman, m. \\\"mouth\\\"; Gk. stóma, n. id. and \\\"opening\\\"; Ir. stomán, m. \\\"maw, paunch\\\"; Br. staon, f. \\\"roof of mouth\\\"; W cf. (variant) safn, f. …' — Mann reconstructs the zero-grade *stomn-, same root.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck p. 240 (SYN.txt leaf 264), §4.24 MOUTH\", \"stance\": \"partial\", \"note\": \"'2. Grk. στόμα: Av. staman- \\\"dog's mouth\\\", W. safn \\\"mouth, jaws\\\" (of animals), MBr. staffn, Br. staon \\\"palate\\\", root connection? Walde-P. 2.648. Pedersen 1.78.' Buck accepts the equation but queries the deeper root etymology — hence the root is well founded but the Grundform is not fully agreed.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"staman\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. staman- m./n. is a genuine Avestan noun, attested only in the Vidēvdād (V. 13.30, 13.44 and 15.4) and always of a dog's muzzle, whence Bartholomae's gloss 'Maul, nur von dem des Hunds'. It continues the PIE *men-/*mn̥-stem *stéh₃mn̥ (Pokorny's *stomen-) with the regular Indo-Iranian outcome of the interconsonantal laryngeal in the zero-grade stem; the short a of stɑman- instead of the expected **stāman- is the one irregularity, and Lubotsky explains it as a secondary shortening, since both attestations stand before enclitics (so Wiktionary, citing Kloekhorst 2008 and Lubotsky). The Pahlavi Vidēvdād glossators render the word astāmak (Jamaspji Gloss. 549, wrongly 'gums'), which is the form that underlies Horn's Persian entry in node #2. Nourai's chart form 'staman' and gloss 'mouth (of a dog)' are verbatim Pokorny/Klein.\",\n          \"derivation_fa\": \"staman- واژه‌ای اوستایی است که تنها در وندیداد (فرگرد ۱۳ بندهای ۳۰ و ۴۴ و فرگرد ۱۵ بند ۴) به کار رفته و همواره به «پوزهٔ سگ» اشاره دارد؛ بارتولومه در فرهنگ ایرانی باستان (ستون ~۱۵۹۱) می‌نویسد: «staman- نرینه، «پوزه»، تنها دربارهٔ سگ». این واژه بازماندهٔ ستاکِ -mn̥ی هندواروپایی *stéh₃mn̥ (همان *stomen- پوکورنی) است و در ایرانی باستان حنجرهٔ میان‌هجایی از میان رفته است. تنها بی‌قاعدگی، کوتاهیِ واکهٔ a به جای صورت مورد انتظار **stāman- است که لوبوتسکی آن را کوتاه‌شدگیِ ثانوی پیش از واژه‌بست‌ها می‌داند، زیرا هر دو گواه پیش از واژه‌بست آمده‌اند. ترجمهٔ پهلویِ وندیداد این واژه را astāmak آورده است که همان صورتی است که گرهٔ بعدی از آن برمی‌خیزد. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stéh₃mn̥\",\n            \"https://en.wiktionary.org/wiki/στόμα\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1035\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 277 = printed p.1035: '[a]v. staman- n. ,Maul (vom Hund)'' — exactly the chart's form and gloss, placed directly under the root heading.\"},\n            {\"ref\": \"KLN:1518\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 805 (= printed pp.1518-1519), s.v. stomach: Gk. στόμα 'mouth', 'which is cogn. with Avestic staman-, \\\"mouth (of a dog)\\\", Hitt. shtamar, \\\"mouth\\\", MBret. staffn, \\\"mouth; jawbone\\\", Co. stefenic, \\\"palate\\\".' Nourai's English gloss 'mouth (of a dog)' is copied from Klein.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiran. Wb. col. ~1591 (BRT.txt leaf 868)\", \"stance\": \"supports\", \"note\": \"'staman- m. \\\"Maul\\\", nur von dem des Hunds: [sta]manim … nyāsayən (Sp. 362 o.) V. 13.30; — yat … V. 15.4. Vgl. gr. στόμα; kymr. safn; ganz unsicheres bei Hirt PBrB. 22, 223. — Pü.: astāmak (bei JAMASPJI Gloss. 549 \\\"gums\\\").' Bartholomae is the authority for the restriction to dogs and gives the Pahlavi rendering astāmak.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.648\", \"stance\": \"supports\", \"note\": \"'Av. staman- n. \\\"Maul (vom Hund)\\\"' heads the stomen- article, before the Greek.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann pp. 1292-1293 s.v. stomn-\", \"stance\": \"supports\", \"note\": \"'Av. staman, m. \\\"mouth\\\"' listed as the Iranian reflex of *stomn-.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian (KNT.txt) — grep 'staman' finds nothing\", \"stance\": \"silent\", \"note\": \"No Old Persian cognate is attested; the word is Avestan-only in Old Iranian, which is consistent with the chart drawing the arrow to Avestan and not to Old Persian.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"astam «اَستَم»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form itself is real and Nourai's reference is exact: Horn, Grundriss p.267 no. 31 reads 'astam \\\"Maul\\\". aw. staman- \\\"Maul\\\". Arm. stom ist aus gr. στόμα entlehnt.' The phonology is regular — Proto-Iranian *stāman- > (with the prothetic a- that Middle Persian regularly develops before initial st-, cf. Pahl. astar 'mule', astūdan, NP استخوان ostoxān) astām/astam, the Pahlavi Vidēvdād glossaries writing astāmak (so Bartholomae, col. ~1591, from Jamaspji's Glossary 549). Two qualifications keep this from 'confirmed'. (i) Language stage: Horn's p.267 belongs to the section headed VERLORENES SPRACHGUT (Grundriss pp.261ff.), his list of PAHLAVI words that New Persian gave up — the same list explains of no. 13 anākīh 'das sehr häufige Wort ist aufgegeben'. So astam is a Middle Persian (Pahlavi/Pāzand) word, not a New Persian one; Nourai's '[Persian] … (obsolete)' preserves Horn's 'obsolete' but promotes the word a stage too far, and the Persian spelling «اَستَم» is Nourai's own transposition into Arabic script, not a form any Persian dictionary carries (Borhān-e Qāṭeʿ's استم is a by-form of ستم 'oppression', and Moʿin has only استام 'fire-iron' and 'saddle-mount'). (ii) The arrow Avestan → Persian is a genealogical shorthand: MP astām is not borrowed from Avestan but inherited in parallel from Proto-Iranian *stāman-, though here the only route by which the word is actually documented in Persian is the Pahlavi Zand of the Avestan text, so Nourai's arrow is defensible as a transmission route.\",\n          \"derivation_fa\": \"صورتِ این واژه راست است و ارجاع نورایی نیز دقیق: هُرن در «مبانی ریشه‌شناسی فارسی نو»، صفحهٔ ۲۶۷، شمارهٔ ۳۱ می‌نویسد: «astam «پوزه». اوستایی staman- «پوزه»». دگرگونی آوایی نیز قاعده‌مند است: ایرانی باستان *stāman- با افزوده‌شدن واکهٔ آغازینِ کمکی (a-) پیش از خوشهٔ st- — همان پدیده‌ای که در «اَستر» و «استخوان» دیده می‌شود — به astām/astam فارسی میانه رسیده و در واژه‌نامه‌های پهلویِ وندیداد به صورت astāmak آمده است (بارتولومه، ستون ~۱۵۹۱). دو نکته اما مانع از پذیرش کامل است: نخست آنکه صفحهٔ ۲۶۷ هُرن بخشی از فهرستی است با عنوان VERLORENES SPRACHGUT، یعنی «واژگان از دست رفته»، که هُرن در آن واژه‌های پهلوی‌ای را برشمرده که فارسی نو آن‌ها را رها کرده است؛ پس astam واژه‌ای فارسی میانه (پهلوی/پازند) است نه فارسی نو، و املای «اَستَم» ساختهٔ خودِ نورایی است و در برهان قاطع و فرهنگ معین چنین واژه‌ای به معنی «دهان» نیامده (استمِ برهان قاطع گونه‌ای از «ستم» است). دوم آنکه پیکان «اوستایی ← فارسی» در اینجا وام‌گیری نیست بلکه ارثِ موازی از ایرانی باستان است، هرچند چون تنها گواهِ فارسیِ این واژه از زندِ پهلویِ متن اوستایی می‌آید، مسیرِ نورایی پذیرفتنی است. حکم: با احتیاط پذیرفتنی است، با تصحیحِ برچسبِ زبانی به «فارسی میانه».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stéh₃mn̥\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:267\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 288 = printed p.267, entry no. 31: 'astam \\\"Maul\\\". aw. staman- \\\"Maul\\\". Arm. stom ist aus gr. στόμα entlehnt.' (grep -n -i 'staman' HRN.txt → line 10155). Page and content are exactly as cited. Caveat: leaf 282 = p.261 carries the section heading 'VERLORENES SPRACHGUT', i.e. Horn's list of Pahlavi words lost in New Persian — so Horn's astam is a Pahlavi, not a New Persian, word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt) — grep 'astam', 'staman'\", \"stance\": \"silent\", \"note\": \"Only apastam/awastam 'trust, reliance' (lines 611, 616, 9084), a different word (< *upa-stāna-). Hübschmann has no astam 'mouth'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. (PHD_pages.txt) — grep 'stam'\", \"stance\": \"silent\", \"note\": \"Only abestam/awestam ['pst'm], 'reliance' and 'province' (pp. as indexed in PHD_pages.txt). MacKenzie's selection does not include astām 'muzzle', which occurs only in the Zand glossaries — the word is genuinely marginal in Middle Persian.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"Glossary has apa-stam ['pst'm] 'reliance' (< *upa-stāna-) and Rōtastahm, nothing for astām 'mouth'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol.1 (BQT_v1_pages.txt line 11915) s.v. استم\", \"stance\": \"contradicts\", \"note\": \"'استم — بکسر اول … و سکون ثانی و میم، ستم و جور و ظلم را گویند' = a by-form of ستم 'oppression, tyranny'. Borhān knows no Persian استم 'mouth', so the Persian-script form in the chart has no lexicographic backing.\"},\n            {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi (MON_part1.txt lines 11303, 11309)\", \"stance\": \"silent\", \"note\": \"استام is given twice, as 'iron fire-poker' and as '[اوستام، ستام] saddle ornament' — neither is 'mouth'. No entry astam 'mouth'.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae col. ~1591 s.v. staman-\", \"stance\": \"supports\", \"note\": \"'Pü.: astāmak (bei JAMASPJI Gloss. 549 \\\"gums\\\")' — the Pahlavi rendering, i.e. the actual Middle Persian attestation behind Horn's astam.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur Kashani (incoming/ARY/ARY_pages.txt, ARY_latin_index_pages.txt) — grep 'STOMEN', 'staman', 'استم'\", \"stance\": \"silent\", \"note\": \"The modern Persian IE-roots dictionary has neither the root nor the word — confirming it is not part of the living Persian lexicon.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"stoma, stomaxos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek στόμα (stóma), gen. στόματος, n. 'mouth, face; opening, mouth (of a river, of a vessel)' is the direct Greek reflex of PIE *stéh₃mn̥ (Pokorny's *stomen-), the Greek o-vowel being the regular colouring by *h₃ and the *-mn̥ stem being remade as a -ματ- stem. στόμαχος (stómakhos) is NOT an independent descendant of the root but an inner-Greek derivative of στόμα with the suffix -χο- (Brugmann Grundriss II.1, 486, 513, cited by Walde-Pokorny II 648); its sense went 'throat, gullet, oesophagus' → 'the mouth of an organ' (the neck of the bladder or uterus) → 'the mouth of the stomach' → in the later Greek physicians simply 'stomach'. Nourai's node gloss 'mouth, throat' covers both words correctly; the only imprecision is that the chart puts the two on one level under the root rather than deriving στόμαχος from στόμα.\",\n          \"derivation_fa\": \"στόμα یونانی (ستاک στόματ-) به معنی «دهان، چهره، دهانه» بازتابِ مستقیمِ *stéh₃mn̥ هندواروپایی است؛ واکهٔ o در یونانی از رنگ‌گرفتنِ واکه بر اثر حنجرهٔ *h₃ پدید آمده و ستاکِ *-mn̥ در یونانی به ستاکِ -ματ- بازساخته شده است. اما στόμαχος بازماندهٔ جداگانه‌ای از ریشه نیست، بلکه مشتقی درون‌یونانی از خودِ στόμα با پسوندِ -χο- است (والده-پوکورنی، جلد ۲، ص ۶۴۸، به نقل از برویگمان). تحولِ معناییِ آن چنین بوده است: «گلو، مری» ← «دهانهٔ اندام» (دهانهٔ مثانه و زهدان) ← «دهانهٔ معده» ← نزد پزشکانِ یونانیِ متأخر خودِ «معده». معنیِ «دهان، گلو» که نورایی برای این گره آورده درست است؛ تنها بی‌دقتیِ نمودار آن است که هر دو واژه را هم‌سطح زیر ریشه نشانده، حال آنکه στόμαχος از στόμα برآمده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/στόμα\",\n            \"https://www.etymonline.com/word/stomach\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1035\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 277 = p.1035: 'gr. στόμα n. ,Mund', στόμαχος (-χο-Formans) ,Kehle, Mündung (der Blase, des Uterus); Magenmund, Magen''. Pokorny explicitly marks -χο- as a formant, i.e. στόμαχος is built on στόμα.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.648\", \"stance\": \"supports\", \"note\": \"'gr. στόμα n. \\\"Mund\\\", στόμαχος (vgl. zum -χο-Formans Bgm. II² 1, 486, 513) \\\"Kehle, Mündung (der Blase, des Uterus); Magenmund, endlich Magen\\\"; dehnstufig στωμύλος \\\"mundfertig, geschwätzig\\\".'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein pp.1518-1519, s.vv. stoma, stomach\", \"stance\": \"supports\", \"note\": \"'stoma, n., a minute mouthlike orifice. — Gk. στόμα, gen. στόματος, \\\"mouth\\\", whence στόμαχος, \\\"throat, gullet, stomach\\\".' Klein derives στόμαχος from στόμα, as Pokorny does.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.68 s.v. stə-men-\", \"stance\": \"supports\", \"note\": \"'Greek stoma, mouth: STOMA, STOMACH, STOMATO-, -STOMY; ANASTOMOSIS …' — the whole English στόμα family is routed through Greek stoma.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann pp.1292-1293 s.v. stomn-\", \"stance\": \"supports\", \"note\": \"'Gk. stóma, n. id. and \\\"opening\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"stomachus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin stomachus is a straight loan from Greek στόμαχος, taken over with the Greek χ rendered ch and the Greek -ος declined as a Latin second-declension -us; it is already in Cicero and Celsus. In Latin the word means first 'gullet, oesophagus' and then 'stomach', and it developed a set of purely Latin figurative senses — 'taste, liking, inclination' (bonus stomachus 'good digestion, good humour') and, from the organ as the seat of temper, 'distaste, irritation, pride, indignation', whence the verb stomachārī 'to be angry'. Nourai's gloss 'taste, stomach' names exactly these two Latin senses and is copied from Klein, who gives L. stomachus 'gullet, esophagus, stomach, liking, taste'. The arrow Greek → Latin is uncontroversial.\",\n          \"derivation_fa\": \"stomachus لاتین وام‌واژه‌ای مستقیم از στόμαχος یونانی است: خیشومیِ... (بهتر بگوییم) واجِ خِ یونانی (χ) در لاتین ch نوشته شده و پایانهٔ یونانیِ -ος به -us صرفِ دوم لاتین بدل شده است؛ این واژه از دورهٔ سیسرون و کِلسوس به بعد در متون لاتین هست. در لاتین نخست به معنی «مری» و سپس «معده» به کار رفته و سپس معناهای مجازیِ ویژهٔ لاتین یافته است: «ذوق، میل، پسند» (bonus stomachus) و — از آنجا که معده را جایگاهِ خُلق و خو می‌دانستند — «بیزاری، خشم، نخوت»، که فعلِ stomachārī «خشمگین بودن» از همان‌جاست. معنیِ دوگانهٔ «ذوق، معده» که نورایی آورده دقیقاً همین دو معنای لاتین است و از کلاین گرفته شده. این پیکان بی‌مناقشه است و ادعای نورایی درست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/stomachus\",\n            \"https://www.etymonline.com/word/stomach\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1518\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 805 = printed pp.1518-1519, s.v. stomach: 'fr. L. stomachus, \\\"gullet, esophagus, stomach, liking, taste\\\", fr. Gk. στόμαχος, \\\"throat, gullet, esophagus, stomach\\\", fr. στόμα, \\\"mouth\\\"'. Klein's 'liking, taste' is the source of Nourai's gloss 'taste, stomach'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. stomach / stomacher (FSD_vol4.txt line 23105)\", \"stance\": \"supports\", \"note\": \"'… < F. [esto]mac, < L. stomachus, < Gr. stomachos, < stoma, mouth'; and s.v. stomach v. '< L. stomachor, be angry, < stomachus' — confirming the Latin affective senses.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 only (A-?) held locally\", \"stance\": \"silent\", \"note\": \"Vol. 2 (S-Z) is not in the local library, so 'stomach' could not be looked up there.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt) — grep 'stomach'\", \"stance\": \"partial\", \"note\": \"The OCR of the S pages is too damaged to isolate Skeat's stomach entry; he is quoted only at s.v. maw ('Maw, stomach') and midriff. Treated as not usable here; Klein and Funk & Wagnalls cover the chain.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"stomach\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English stomach is attested as ME stomake/stomak from the early 14th century, borrowed not straight from Latin but from Old French estomac / stomaque, itself from Latin stomachus (so Etymonline, Klein and Funk & Wagnalls alike); Spanish estómago and Italian stomaco are the Romance parallels. The Latin-looking spelling with -ch was restored in the 16th century, but the pronunciation stayed the Middle English one (/ˈstʌmək/), which is why the ch is read as k. The English word inherited the Latin figurative senses too — 'relish, inclination, desire; courage, spirit; anger, resentment' (mid-15c. onward), and the verb to stomach 'to tolerate' (1570s) and the older 'to resent' (1520s, echoing L. stomachārī). Nourai's arrow Latin → English is correct in substance; the only compression is that the immediate donor was Old French, Latin being the ultimate source. The native English word displaced by it was maw (OE maga, glossing L. stomachus).\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ stomach از آغاز سدهٔ چهاردهم میلادی به صورت stomake/stomak در انگلیسیِ میانه گواهی شده است، اما نه یکسره از لاتین، بلکه از فرانسهٔ باستان estomac/stomaque که خود از stomachus لاتین است (اتیمآنلاین، کلاین و فانک و وگنالز هر سه چنین می‌گویند)؛ estómago اسپانیایی و stomaco ایتالیایی نیز همتاهای رومَنسِ همین وام‌اند. املای لاتین‌نمای -ch در سدهٔ شانزدهم بازگردانده شد ولی تلفظ همان تلفظِ انگلیسیِ میانه ماند و از همین روست که ch را «ک» می‌خوانند. معناهای مجازیِ لاتین نیز به انگلیسی رسید: «میل، اشتها، دلیری، خشم» و فعلِ to stomach «تاب آوردن» (۱۵۷۰م) و پیش‌تر «رنجیدن» (۱۵۲۰م، برابرِ stomachārī لاتین). پیکانِ «لاتین ← انگلیسی» در نمودار نورایی از نظر محتوا درست است و تنها حلقهٔ فرانسهٔ باستان از آن افتاده است. واژهٔ بومیِ انگلیسی که این وام آن را کنار زد maw (انگلیسی کهن maga) بود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/stomach\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p.68 (AHD_watkins1985.txt leaf 97) s.v. stə-men-: 'Greek stoma, mouth: STOMA, STOMACH, STOMATO-, (STOMATOUS), -STOMY; ANASTOMOSIS, ANCYLOSTOMIASIS, PROSTOMIUM, SCYPHISTOMA. [Pok. stomen- 1035.]' — STOMACH is listed as a derivative of this root, exactly as the chart has it. (Nourai's bare 'AHD' has no page; the 1976 AHD appendix is not open, but the 1985 Watkins edition prints the same entry.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein pp.1518-1519 s.v. stomach\", \"stance\": \"partial\", \"note\": \"'stomach, n. — ME. stomak, fr. OF. (= F.) estomac, fr. L. stomachus …' — same origin, but Klein makes the immediate source Old French, not Latin directly; the chart's Latin→English arrow skips that step.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. stomach (FSD_vol4.txt line 23105)\", \"stance\": \"partial\", \"note\": \"'[ME. sto]mac, < L. stomachus, < Gr. stomachos, < stoma, mouth' with the archaic English sense '7†. The mouth, gullet' — again via French/ME rather than straight from Latin.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century — only vol. 1 (A-?) available locally\", \"stance\": \"silent\", \"note\": \"S-volume not held; could not check.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool data/verification/page-483.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 483"
}
```


### [2026-09-14T03:15:07.486Z] TOOL RESULT

```
JSON OK
nodes verified: 5/5
node verdicts: {'confirmed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6}
books consulted: {'supports': 9, 'silent': 8, 'contradicts': 1, 'partial': 3} | by book: {'BRT': 2, 'WLD': 2, 'IEC': 2, 'KLN': 2, 'FSD': 2, 'WEB': 2, 'KNT': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'MON': 1, 'ARY': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-14T03:15:14.978Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PY'\nimport json,io\np='data/verification/page-483.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace(\"خیشومیِ... (بهتر بگوییم) واجِ خِ یونانی (χ)\",\"واجِ خِ یونانی (χ)\")\ns=s.replace('{\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt) — grep \\'stomach\\'\", \"stance\": \"partial\"','{\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt) — grep \\'stomach\\'\", \"stance\": \"silent\"')\nopen(p,'w',encoding='utf-8').write(s)\njson.load(open(p,encoding='utf-8'))\nprint('ok')\nPY\npython3 tools/verify_check.py 483"
}
```


### [2026-09-14T03:15:16.117Z] TOOL RESULT

```
ok
nodes verified: 5/5
node verdicts: {'confirmed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6}
books consulted: {'supports': 9, 'silent': 9, 'contradicts': 1, 'partial': 2} | by book: {'BRT': 2, 'WLD': 2, 'IEC': 2, 'KLN': 2, 'FSD': 2, 'WEB': 2, 'KNT': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'MON': 1, 'ARY': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-14T03:15:34.152Z] AGENT

Page 483 verified. `verify_check.py 483` reports 0 PROBLEM lines.

**Counts** — 1 entry (2 redirect entries skipped: Stor → Ster 1, Str → Ster 1); root verdicts: 1 confirmed; node verdicts: 4 confirmed, 1 plausible. Ref checks: 6/6 `supports`. Books consulted: 15 entries (POK, WLD, AHD/Watkins, IEC/Mann, SYN/Buck, KLN, BRT, KNT, HRN, HUB, PHD, NYB, BQT, MON, ARY, FSD, WEB, SKT).

**Root Stomen (PIE *stomen- "mouth")** — confirmed. Pokorny IEW p.1035 heads the entry exactly `stomen- ,Mund'` with precisely Nourai's two branches; Walde-Pokorny II 648 identical; Watkins prints *stə-men-; modern notation *stéh₃mn̥ (Kloekhorst 2008). Buck 4.24 queries the deeper root connection but not the Gk/Av equation.

**No `disputed` and no `transcription_suspect` items; no extraction errors** — the JSON matches the chart text faithfully.

One item worth the owner's attention (recorded as `plausible`, not an extraction bug):

- **#2 Persian `astam` «اَستَم» "mouth (obsolete)"** — Horn p.267 no. 31 says exactly `astam 'Maul'. aw. staman- 'Maul'`, so the citation is exact, but p.267 sits inside Horn's section **VERLORENES SPRACHGUT** (from p.261), his list of *Pahlavi* words New Persian gave up. So the word is Middle Persian (Bartholomae col. ~1591 gives the Pahlavi Zand gloss `astāmak`), not New Persian; the Arabic-script «اَستَم» is Nourai's own transposition. Borhān-e Qāṭeʿ's استم is a by-form of ستم "oppression" (the only `contradicts` on the page), Moʿin has only استام "fire-iron / saddle-mount", and MacKenzie, Nyberg, Hübschmann and Aryanpur are all silent. The arrow is also genealogically a parallel inheritance from Proto-Iranian *stāman- rather than a borrowing from Avestan — though the Pahlavi Zand of the Vidēvdād is in fact the only route by which the word is documented in Persian, which keeps Nourai's arrow defensible.

Minor compressions noted in the derivations without downgrading: Greek στόμαχος is an inner-Greek -χο- derivative of στόμα (the chart levels the two), and English *stomach* came via Old French estomac (ME stomak, early 14c.), Latin being the ultimate rather than immediate source.

Six web pages archived via `fetch_source.py` (Wiktionary στόμα, *stéh₃mn̥, stomachus, PIE *steh₂-; Etymonline stomach). Webster vol. 2 (S–Z) is not in the local library, and the S pages of Skeat's OCR are too damaged to read — both recorded as `silent`.
