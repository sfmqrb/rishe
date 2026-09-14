# Verification process log — verify-page-462


## [2026-09-14T02:27:36.895Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 462 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-462.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-462.json. Write /home/sfmqrb/git/rishe/data/verification/page-462.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 462` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:38.040Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:39.007Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:39.026Z] TOOL RESULT

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


## [2026-09-14T02:27:39.569Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-462.txt"
}
```


### [2026-09-14T02:27:39.599Z] TOOL RESULT

```
1	=== PDF page 462 (book page 432) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sneigwh : snow, to snow  (refs POK:974)
4	#1 (parent #0) [Avestan] refs=POK:974; KLN:1466 | snaěž, snaěj, snaěža : to snow
5	  #2 (parent #1) [Persian] refs=HRN:292 | sněhr «سنهر» : snow (obsolete)
6	#3 (parent #0) [Sogdian] refs=SOD:376 | šněš : to snow
7	#4 (parent #0) [Germanic] refs=POK:974 | snaiwaz : snow
8	  #5 (parent #4) [English] refs=AHD | snow
9	--- entry 1 ---
10	ROOT Sner -> redirect to Ner 2
11	--- entry 2 ---
12	ROOT Snerq -> redirect to Ner 2
13	--- entry 3 ---
14	ROOT Sneu -> redirect to Sâi 2
15	--- entry 4 ---
16	ROOT Sněu -> redirect to Sâi 2
17	--- entry 5 ---
18	ROOT [Indo-European] Sneudh, Neudh : mist, cloud  (refs POK:978)
19	#1 (parent #0) [Avestan] refs=POK:978 | snaoda : cloud
20	#2 (parent #0) [Latin] refs=KLN:1059; AHD | nůběs : cloud
21	  #3 (parent #2) [French] refs=KLN:1059 | nue : cloud ; nuance : shade, a slightly different meaning of a word
22	    #4 (parent #3) [English] refs=AHD; KLN:1059 | nuance
23	--- entry 6 ---
24	ROOT Snôğ -> redirect to Nôğ
25	--- entry 7 ---
26	ROOT Snů -> redirect to Sâi 2
27	
```


## [2026-09-14T02:27:42.793Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-462.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Print source JSON for page 462"
}
```


### [2026-09-14T02:27:44.062Z] TOOL RESULT

```
{
 "pdf_page": 462,
 "book_page": 432,
 "entries": [
  {
   "root": {
    "name": "Sneigwh",
    "lang": "Indo-European",
    "refs": "POK:974",
    "gloss": "snow, to snow"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:974; KLN:1466",
     "words": [
      {
       "translit": "snaěž, snaěj, snaěža",
       "gloss": "to snow",
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
     "refs": "HRN:292",
     "words": [
      {
       "translit": "sněhr",
       "gloss": "snow (obsolete)",
       "script": "سنهر"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Sogdian",
     "refs": "SOD:376",
     "words": [
      {
       "translit": "šněš",
       "gloss": "to snow",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 0,
     "lang": "Germanic",
     "refs": "POK:974",
     "words": [
      {
       "translit": "snaiwaz",
       "gloss": "snow",
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
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "snow",
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
    "name": "Sner",
    "redirect": "Ner 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Snerq",
    "redirect": "Ner 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Sneu",
    "redirect": "Sâi 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Sněu",
    "redirect": "Sâi 2"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Sneudh, Neudh",
    "lang": "Indo-European",
    "refs": "POK:978",
    "gloss": "mist, cloud"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:978",
     "words": [
      {
       "translit": "snaoda",
       "gloss": "cloud",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 0,
     "lang": "Latin",
     "refs": "KLN:1059; AHD",
     "words": [
      {
       "translit": "nůběs",
       "gloss": "cloud",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "French",
     "refs": "KLN:1059",
     "words": [
      {
       "translit": "nue",
       "gloss": "cloud",
       "script": null
      },
      {
       "translit": "nuance",
       "gloss": "shade, a slightly different meaning of a word",
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
     "refs": "AHD; KLN:1059",
     "words": [
      {
       "translit": "nuance",
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
    "name": "Snôğ",
    "redirect": "Nôğ"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Snů",
    "redirect": "Sâi 2"
   },
   "nodes": []
  }
 ]
}
```


## [2026-09-14T02:27:45.197Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','SOD','AHD','WLD','BRT','IEC','SYN','HUB','MON','BQT','PHD','NYB','SKT','FSD','WEB','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False) if v else 'MISSING')\n\"",
 "description": "Read refs_online for keys used"
}
```


### [2026-09-14T02:27:46.337Z] TOOL RESULT

```
<persisted-output>
Output too large (32.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b3ymi71bp.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-14T02:27:50.924Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','HRN','SOD','AHD','WLD','BRT','IEC','SYN','HUB','SKT','FSD','WEB','MON','BQT']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print(k, v.get('title','')[:80], '|lf=',v.get('local_file'), '|off=',str(v.get('page_offset'))[:200])\n    print('   files:', v.get('local_files'))\n\""
}
```


### [2026-09-14T02:27:52.117Z] TOOL RESULT

```
KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vol |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |off= KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between l
   files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
HRN P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893 |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |off= leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>
   files: None
SOD Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Teh |lf= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] |off= printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   files: None
AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New C |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |off= 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (s
   files: None
WLD A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen,  |lf= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |off= Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_B
   files: None
BRT C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979 |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |off= Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the 
   files: None
IEC S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87 |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |off= TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://a
   files: None
SYN C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Lan |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |off= leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   files: None
HUB H. Hübschmann, Persische Studien, Strassburg 1895 |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt |off= leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   files: None
SKT W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford ( |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt |off= leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   files: None
FSD Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 p |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt |off= vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably 
   files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt']
WEB Webster's New Twentieth Century Dictionary of the English Language, Unabridged,  |lf= /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt |off= not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<iden
   files: None
MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, |lf= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |off= None
   files: None
BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; N |lf= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |off= vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 n
   files: None
```


## [2026-09-14T02:27:56.117Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"lemma: sneig\\|lemma: sneudh\\|lemma: sneu\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:27:56.173Z] TOOL RESULT

```
78890:Root / lemma: sneig- 
78895:Root / lemma: sneig^h- 
78901:Root/ lemma: sneig^h-: 'to snow; snow' derived from a zero grade {*suu-etos, *suerid) : 
79087:Root / lemma: sneu b^- {*sneu- b^-) 
79113:Root / lemma: sneud(h)-1 
79131:Root / lemma: sneu6y-2 
79155:Root / lemma: sneu- 
79194:Root / lemma: sneu-. 5/7 J- and sneu-
```


## [2026-09-14T02:27:57.560Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=205 && NR<=215 {print \"=== leaf \" NR-1 \" ===\"; print}' POK_03.txt | grep -n -i \"sneig\\|snaiwaz\\|snaež\\|snow\" | head -30"
}
```


### [2026-09-14T02:27:58.627Z] TOOL RESULT

```
182:sneig-  ,kriechen':  s.  unter  sneg-  ds.
183:sneig'Ah-  ,schneien,  (sich)  zusammen  ballen',  snig^h-,  snoig]iho-s  , Schnee*.
```


## [2026-09-14T02:28:00.212Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78890,79000p' POK_full.txt"
}
```


### [2026-09-14T02:28:00.269Z] TOOL RESULT

```
Root / lemma: sneig- 
Meaning: ' crawl, creep ' 
See also: see below sneg-ds. 
Page(s): 974 

Root / lemma: sneig^h- 

Meaning: to snow; snow, *rain 

Note: 

Root/ lemma: sneig^h-: 'to snow; snow' derived from a zero grade {*suu-etos, *suerid) : 

Old Indie sunSti^ squeezed, pressed ' = Avestan hunaoitioi Root/ lemma: seu-1, se^a-. 

SU-: 'juice; liquid, rain'. 



Material: Prakrit. sineha-{= Old Indie sneha-) "snow'; Avestan snaeza-'to snow', pamir. 
sugni zdn/j'snow', {*snaiga-)\ gr. vicpa Akk. "snow', horn. aYavvi(po(; " much snowed on, 
snow-capt ', vsicpsi (vicpsi) " it is snowing ', vi(pa(; " snowflake ' (vicpsTOc; " snowstorm, 
snowfall '), Latin nix, /7/V/s "snow', nivit^ it is snowing ' (probably /); nasal-pras. ninguit 
{ninxit} ds.; 

Irish snigid^ it drips, is raining ', snigeu. "drip, flux ', snechtfaje ' snow' (to /-forms 
compare vicpsToq); cymr. nyrsnow', nyf/o^to snow'; 

Old High German Old English snTwan^io snow' (stem V., participle gi-snigan, compare 
still Modern High German Bavarian participle geschniwen; otherwise Modern High German 
schw. v.). Old Icelandic snyr^ it is snowing ' (participle snifinn " snowy '); Gothic snaiws 
"snow' = Old English snaw. Old High German s/7eo(Gen. snewes); 

Lithuanian sniegas, Latvian sn/'egs {vo\Ne\ from the undertaken verb) "snow', sna/ga/a' 
snowflake ', sniega^ it is snowing ', Inf. snigti. Old Prussian snayg/s^ snow', Old Church 
Slavic snegb "snow'. 

• Sumerian ^^^4, "frost; cold shudder, chills', seg8/9: "snow; ice' (cf., s^gga)- 
References: WP. II 695, WH. II 169 f., Trautmann 272 f., Vasmer2, 680, R. L. Turner 
BSOAS 18, 449 f.; compare Old Indie sn/hyat/' become damp, sticky ', sneha- m. " 
stickiness, oil, fat '. 
Page(s): 974 

Root / lemma: sneit- 
Meaning: to cut 

Material: Gothic sne/Pan, Old Icelandic snfda'cut, clip, reap'. Old English snTdan^cxA, clip, 
hew, hit'. Old Saxon snllhan. Old High German snTdan^cui, clip'; Old Icelandic sneid^ 
sliced piece'. Middle High German sneite^ through den wood, forest gelegter Durchhau' ; 
Old High German s/7//"the cut'. Middle High German s/7/o'e "cutting edge', intensive. 
*snittdn\n Middle High German snitzen^0QX\ie'; Old Icelandic s/7e/s "small 
(abgeschnittener) twig, branch'. Old English snaes, s/755"spit, pike. Speller', Middle High 
German sneise "row, cord, whereupon etwas gereiht wird' ( *snoid-ta); 

kir. 5/7/rclot, chunk', Czech s/7e/"bough' {*snoito-s); compare perhaps Middle Irish 
s/7e/o' "small, short', whether from Old Irish *sneithl 

References: WP. II 695 f. 
Page(s): 974 



Root / lemma: (s)nerb- 
Meaning: to cut 

Material: Gr. voppsT svTapisTrai, voppa KaArj Hes. (as Modern High German 'schneidig'?); 

also Gothic at-snarpjan 'aniassen'7; Old Icelandic snarpr^ sharp, hart, uneven', snerpa' 

sharpen ', Dutch snerpen'b\te (from Wunden), ache', westfal. sn/rpsch ^ sharp (of wind)'; 

Old High German s/7eAi'&/7 'together pull, drag'; without s-: nisi, norpa' freeze '. 

References: WP. II 701; 

See also: whether to the above sner-b- {sner-2)7 

Page(s): 977 

Root /lemma: (s)ner-l, (s)nur- 
Meaning: to murmur, grumble 

Material: Gr. evupsv Eipiasv; svupnaeK; 9pr|vr|a£iq; ovupi^EOi 65up£Tai Hes.; Middle High 
German snarren^ burr, babble, chatter', snerren^ babble, chatter', s/7^/re/7 'sough, rustle, 
buzz, whirr', snurraere, snurrinc^ merrymaker, fool'. Modern High German schnarren, 
schnurren, Schnurre, engl. snarr growl ', Middle English snorin, nengl. snore 
'schnarchen'. Middle English sneren, nengl. sneer^ contemptibly laugh'; Middle English 
/7^/77e/7'hersagen', Swedish dial, noma, /7y/77a 'zuflij stern'. Old Icelandic norn 
'Schicksalsgottin', Middle High German narren, nerren^ growl ', Old High German narro 
'fool\ 

Lithuanian niurniu, n/urnef/" dror\e, grumble, growl '; Latvian nura'e'\r\ weinerlicher 
person', nurat'dror\e, grumble, spinnen as eine cat '. 

Auf -{//Middle English s/7i//Y//7 'schnarchen'. Middle High German 5/75/2- 'Schnarre, 
Wachtelkonig'; Latvian /7i/?D'e/ 'murmur, drone, grumble, growl '. 

Auf-p: Norwegian Swedish s/7e/'/ra'prusten, schnarchen', Swedish snurka' groan ', 
Middle Low German snorken, s/75/'/re/7 'schnarchen, pant, sniff, snort'. Middle High 
German snarchends.. Modern High German schnarchen, Norwegian nurka^creak, growl ', 
Dutch nurken 'dror\e, grumble, norgein'; Lithuanian snarglys^ nasal mucus ', Latvian 
snurgalasds. ('*rattling, clashing, groaning '); snirguoV sob; fauchen as die Ganse'; 
Latvian nrrgu6ties^\\b\\r\\sc\\ laugh', hu?gt'd\e Zahne show'; also probably Lithuanian 
/757y/K// "somewhat slowly tun' (meaning similarly as in Swiss norggen ' o\r\r\e Erfolg 
arbeiten'). 



Auf -A:" Old Icelandic sngrgia {*snarguldn) " groan ', Modern High German norgeln, 
nergeln^ inarticulate sprechen, with verdrieftlichem naselnden Tone tadein'; Lithuanian 
niurksau, -oti^ dismal or brijtend dasitzen', Latvian hurk'et, hurkstet, nurkset^ drone,
```


## [2026-09-14T02:28:05.071Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79113,79200p' POK_full.txt"
}
```


### [2026-09-14T02:28:05.133Z] TOOL RESULT

```
Root / lemma: sneud(h)-1 

Meaning: drowsy, to drowse 

Note: perhaps to sneu6^-2. 

Material: Gr. vugto^u) 'sleep; bin sleepy, careless, neglectful', vOoiaKoq, -Ktoq ' sleepy '; 

Lithuanian snaudziu, snausti, Latvian snauzu' drowse ', Lithuanian snaudalius' drowsy 

person', snaudulys " slumber ', Latvian snaudule 'Schlafratze', Lithuanian snustu, snudau, 

s/7i/5//"einschlummern', snuda, snudis^Sdc^s^er, Traumer'. 

References: WP. II 697. 

Page(s): 978 

Root / lemma: sneu6y-2 

Meaning: mist 

Material: Avestan snaoSa-^ clouds', siJdbaluci /7oo'"leichtes clouds, fog, Regenwoike'; gr. 

vuGov acpwvov. gkotsivov, y\jQ(bbzc, aK0T£ivaJ5£(; Hes.; Latin /7JMs "cloud', in addition 

obnubo, -ere^ veil, cover ' (durchs Perf. obnubTa\so formal from nubo, nupsFmarry' sharp 

geschieden), under between probably as denominatives verb: "(sich) bewolken' = "(sich) 



cover', at first of sky, heaven, then generally; cymr. nucfcflog' (to GN Nuddsee above S. 
768); 

possibly originally as " dampness ' = *sneu6!^-Vr\e extension from sneu- besides snau- 
and sna- (see there) 'flow'; as 'benebelt, dim, dusky, cloudy = sleepy ' perhaps to 
sneud(h)- 1. 

References: WP. II 697, WH. II 183 f. 
Page(s): 978 

Root / lemma: sneu- 

See also: see above under sna-. 

Page(s): 977 

Root /lemma: (sjneb'^-ri-, (sjnob'^-n'- 

Meaning: narrow 

Note: only armen. and german. 

Material: Armenian nurti' narrow, tight, slim, slender, thin ' {*sndo^-ri-, = Old Icelandic 

*sn0f/); 

Old Icelandic sn^fr{Gen. -rs) 'narrow; quick, fast', aschw. snsever^ tight, slim, slender, 
thin, narrow'. Old Icelandic sn^fugr^rash, hasty, agile', with gradation Old Icelandic sn0fr 
'quick, fast, agile', reduced grade sngfurligr^rash, hasty'; s- loose Nebenformen aschw. 
neeverav\6 nover. Old Icelandic n0fr{neutr. n0frt) 'rash, hasty, agile' (in addition also 
Middle High German, Modern High German Alemannian nuofer'a\ed, awake, smart, fresh, 
sober'. Modern High German Bavarian nuober). 

References: WP. II 698. 
Page(s): 973-974 

Root/ lemma: {snep-), snop- snap- 
Meaning: to gather in sheafs, sheaf, bundle 

Material: Latin (etrusk.?) napurae ^StrohseWe'; Old High German snuaba WWa' , snuobili^ 
small chain '; Old Church Slavic snopt 'Ssapn. fasciculus, £ni5£a|J0(;, ligatura', russ. 
snop-b etc. ' fascicle, sheaf '; 

References: WP. II 698, WH. II 142, Trautmann 272, Vasmer2, 682. 
See also: probably extension to (s)ne- 'zusammendrehen'. 
Page(s): 974-975 



Root / lemma: sneu-. 5/7 J- and sneu- 

Meaning: to turn, to bind, attach; band; sinew 

Material: Old Indie snavan- (n.) and snavan- 'band, strap, sinew'; reshuffling eines r/n- 

neuter: a-snavira- 'ohne Sehnen' {snuta- 'from the sinew'), Avestan snavara^s\v\e\N'
```


## [2026-09-14T02:28:18.666Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT snaez/snaoda ===\" && grep -n -i \"snaež\\|snae[zžsj]\\|snaoδ\\|snaoδa\\|snao[dδ]\" BRT.txt | head -40"
}
```


### [2026-09-14T02:28:18.732Z] TOOL RESULT

```
=== BRT snaez/snaoda ===
9546:yaihe  vanuM  °fs  Yt/0, 60;  —  "pfm  srao- Iahe .  .yasamaide  'pftn  rasnaes . .  'p^m^*  . , Yt.  //,  21  f.;  —  paoiryä  dasa  xiapanJ  .  . listryB  .  .  'pf/n  rai'^wayeiti  .  .  nars  'pa (IS.)  panco-dasanhS  ".  .  formam  induit ,  , viri  forma  .  ."  Yt  Ä  13;  16,  iS;  — mae^imca  värimta  yä  ts  (näml.  Haomakt) 'piin  vaxlayats  V. /O-3;  —  vupimca  'ß (als  AS.)^'  ahurahe  mazdä  yazamaide  Y. 77.4;  — yat  dim  mazaos  (sd.)  °/J  türahe V.  13.  39;  —  pueril  zayante  tanuAshrpa 'pa  Yyt.i;  —  biDX'jqm  tnöi  firasaostrd ..dalddiit  "pJm  (AS.)'y.5/.  17;  —  upa.- iaht  ar?dvi .  .  kainlnB  'pa  srtraya  Yt 5.  64;  H.  2.  9;  —  yq/"  ■  ■  car.liii/iqm  'pa sralstqm  dildansa  H.  2.  10;  9,  YL5.  34, j/'.  11;  —  yeAAä  'pS  hurae'-aya  Yt  y. i9o(?);  —   'fimca   F.^jht?)^'.  a)    sva.
10901:•  j.  xSnaodräi  Inf.  'zufrieden  zu  stellen': s.  unter  'xsnaoira-.
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
13168:weisendem ASn.  des  Pron.  dem,  und  Dat. comm.:  tat  mSi  daidl  akura  Ayal..rapin (sd.)/ai'jY.5;.i8.  5)mitdemDat-iajya- wA«(sd,)  sanhai  'herabsetzen,  verleumden bei  — '  (Dat.):  yS  nanm  asaimmm  anyd.~ varynai  vä  ..  kasyaahe  tanhäi  da'iSiti  V. 75.2.  III)  Med.  'etwas  an  sich  nehmen, sich  erwerben,  erhalten,  empfangen':  :^a- >röya  (sd.)  na  :x^a>rfm  daidlia  (3SOM.) Y.  43.2;  —  äwil  paiii  zl  haxitirim  (sd.) daior(iS.}  vakilhm  v?r»^rayn3ma  .  .  Vt. 10.  80;  —  zugleich  mit  dem  reflex. Dat  des  Pron.  pers.:  täis  yas  syaoiaiiais as'fm  xsmaibya  daduyi  (sPPM.fi'^  \.  46. 15.  a)  mit  Gen,(-Abl.)  'von  ..  her': mfinm  .  .  yS  *rasnaes'^''  daine  (jSPfM.) moi^anfm  yakmäi  rai'nu/  .  ,  Yt  10, 79.  IV)  'etwas  (Akk.)  tun,  betätigen', Akt:  yj  va  möi  n3  g}ni  (sd.)  %'a  .  . däyät  (Konj.)  atthsus  ya  IB  vSista  va- hiita  Y.  46. 10;  —  masya  acistä  dants Y.^2. 4;  — ya'^a  tu  i*ahuramazda  mSng- haüa  vaocasca  ääsia  var>sca ya  vohü  aha., Y.jp.  4;  —  ya%ra  varmlng  {sA.)  vas.r dayag(Koni.)  Y.31. 11;  —  »m  aei  ibaii'ä paiiyantu  (Sp.  149  u.)  .  .  yö  I  dala  Y.  6j, 8;  8.  i)    mit   Dat   comm.;    a)    '(Ge-
```


## [2026-09-14T02:28:19.645Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 313 (p292) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==314' HRN.txt"
}
```


### [2026-09-14T02:28:20.935Z] TOOL RESULT

```
=== HRN leaf 313 (p292) ===
--- 292 —
aw. siiävar- *Seline*; ai. sndvan- 'Band, Sehne'; arm.
neard *Nerv, Sehne' (Hübschmann, No. 217); oss. d.
nawr, t. nvar Ader' (No. 195).
181. sfiehr^) 'Schnee (vd. 6 (74) u. ö., Men., AV.).
aw. [/^snaej-, snaeJenti 'es schneit'; ksl. mögü; lit.
sn'egas 'Schnee', stiigti schneien'; gr. vicpei; lat. nix\
nivis ; got. snaiws, ahd. smuit es schneit', nhd. Schnee,
Vergl. Hörn, Indog. Forsch. II, Anzeiger 2.
182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
AV.).'
aw. spazga- (yt. 3, 8, 11, 15), Bedeutung unsicher.
V
np. dpezgi (so FJ, sonst meist sipergt) 'Leid' er-
scheint in folgendem Verse von Henzelebäd (?) 'Isä
(Metrum: A'efTf):
hei sipezgl kesiden^E zt r^tb
ger hude yär-t mihr%än bä men
Die falsche Schreibung mit r (die im FR z. B. aus-
drücklich als richtig bezeichnet wird) beweist aber die
Ungebräuchlichkeit des Wortes.
188. s^hU bezw. spek 'Schössling', nur y. 10 (12).
aw. frajspareya- 'Schössling'.
e für r- Vokal wie in np. bese (oben No. 256), -des
(oben No. 598). k kann für / stehen, wie öfter im
PehlevT.
184. srältan 'schützen', sräy(i)sn, nur im AW.-Komm.
aw. l/"tVr(?-, d-räy^inti 'schützen'; ai. {/'trä-, trdyate
'schützen, behüten'.
185. Hvav *Wort', nur im AW.-Komm.
aw. sravah' 'Wort'; ai. grävas- 'Ruhm'; ksl. sloro
'Wort'.
186. Star 'Stern', häufig (neben stürak).
aw. Star- 'Stern'; ai. stdr-.
Vergl. np. sitare (oben No. 711).
187. Start 'erschreckt'.
aw. stareta-. Von vd. 19 (6) ist das Wort in die
Literatur eingedrungen und wird hier in der gleichen
*J Odor i^nexr unter dem Einfiuss von iji'x J^is ?
```


## [2026-09-14T02:28:37.097Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD leaf 442 (p376) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==443' SOD_pages.txt | head -80"
}
```


### [2026-09-14T02:28:38.145Z] TOOL RESULT

```
=== SOD leaf 442 (p376) ===
                                                                                                                 §NT
375

      sambad (smbyd, smpd)                                    9294 smnwk'nc    M                             j^yJi
      Saturday
                                                                   smanukanc
                                                                   devilish  ©f. adj.; ob. -y ^tSrmnwkw'nch
      C2 glossy STi 67.12, 68.19; Hen. JRAS 1945, 149.3
                                                                   BBB 639; smnkw>nc, Hen. BSOAS 12, 311.66;
9284 smbyd      M =* smbd
                                                                     GMS 423, 1065
9285 smywn        C                 (^jj^dj^idj*^
                                                             9295 smnwq'nyCy) M                              J~tjA
      samyon (sm'wn) =»smywn snk                                  smanukane ^smnq^yy
      SimoniPertrus)                                               devilish
      STii 4 p596.; Sund. AoFi 1974, 9R 6, C2 gloss.
                                                                   GMS 1065, 1244, 1245; BBB 639; -JPnyy, BBB b
                                                                     83
        p226
9286 smywn snk C                                    wjJ*i,
                                                             9296 smny>kh B                                    cjUj
     samyon sang =»smywn, sng                                     samanyak
     Petrus                                                        monkhood
      STii 4.p596; C2 gloss. p226                                  O* 22: Frag. Len. 93.22
9287 smn       B, S                              ^j tJ^      9297 smpd    C =» smbd
      sanjpn   (srmn) ©Skt. sramana     ©ob. -y; abl. -V
                                                             9298 smr>}t- =» ^mVt-
        pi. -f>; ob. pi. -ty(>)                              9299 sn                              (Jj*^^j*)d&J
      monk
      VJ 120; SCE 505, 507; TSP; BSTBL, Padm. 66,                 san (-sn) ©3pl. encl. pers. pron. =*s-, sw1, syl
                                                                  they, them, those
        Dhu. 131; Frag. Len. pl09; Hen. Magi. 138, 30;
                                                                  EGSii 118; GMS 1387, 1397; VJ pl20; BSTBL
        STii 8.6, smnt\ TSP 8.196; Dhy. 3; smnty\ Frag.
                                                                    pl34; ^nt, STii 596, 2.19; SCE p71; C2 gloss.
        Len. 93.15; SCE 3, 201; TSP 5.19, 23 passim.
                                                                    p233; MDii p212; KG pl90
9288 smnWk    B                                ^L,*^         9300 sn- B, C, S                                 dxjj
     samanane
                                                                  san ©Khot. san, Pasht. sandel =»snt-, s}yn}ynch
      (of a)monk                                                  (to)tremble, (/c>)shake
      TSP 6.23; SCE 203; GMS 1040
                                                                  VJ 999 n p96; BSTii 887.30: C2, 51V30; z>y snyy,
9289 smn'nch B                                                      Prolexis. 343
                                       (^jd^j
     samanane ©Skt. sramanik(ka) ©f. pi. -th                 9301 -sn =* sn
     nun
                                                             9302 sn»k(h) S                              y.j^J
      VJ 120; TSP; SCE 18a, BSTBL, Padm. 66; Frag.
                                                                  snak (sn}kk, sn>q) ©pi. -r
        Len. 93.31; STii 8.6; GMS 1043; smrintcK O2 31            small

9290 smn'ncyh B                     ^.v^'j <V*'j (* -k_*v)        TSP 2.193, 894: MDii p212; MDiii pl29; sriqU
     samanancya                                                     GMS 991
      (of a)nun                                              9303 sn'q M =* sn»k(h)
      TSP 624
                                                             9304 sn'kk B, S =* sn»k(h)
9291 smnq}nyy      C                        ^Lwybl^lLui
                                                             9305 sn'xntyc M              (/ju^Li/;^j^)JU^.U
      smankane =»smnwq}ny(y)
      satanic, devilish                                           (a)snaxantic ^sn'ky^tyc
                                                                  fifth month of the year
      BSTii 849.4; C2, 12R4: GMS 1065
                                                                  GMS 1275; Hen. JRAS 1944, 149.6
9292 smnkw'nc       M =» smnwk^c
                                                             9306 sny B =» snx
9293 smnw M, C               (^.^OolM^^bl                    9307 snt C                                        J^J
     smanu ©<ytdrmnw <*a0ramanu <*ahra-manu\
                                                                  sand =»sn, s>ntt
       A v. Angra-mainyu ^tdrmnw                                  them
     Ahriman, demon
                                                                  STii 2.19; GMS 1386
      GMS 1190; BBB 639 b87; KG 2333; STi 11.6;
        STii 3.18; C2, gloss. p226; MSP b 194; Lentz.        9308 Snt s                                 G*k-"J-
       STii 577; W-Lii 515                                        sar5 ©Idg. =»sr5
```


## [2026-09-14T02:28:38.459Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD snow ===\" && grep -n -i \"snow\\|snyhl\\|sn[eē]x\\|wafr\" PHD*.txt | head -20; echo \"=== NYB ===\"; ls | grep -i nyb"
}
```


### [2026-09-14T02:28:38.532Z] TOOL RESULT

```
=== PHD snow ===
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:3714:snow snéxr, snézag, wafr.
PHD.txt:5145:wafr
PHD.txt:5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
PHD_pages.txt:4560:snexr [snyhl] snow.
PHD_pages.txt:4561:snezag [snyeh ] snow.
PHD_pages.txt:4563:snOy [snwd] (rain-, snow-)cloud.
PHD_pages.txt:5136:wafr [wpll M wpr, N barf] snow.
PHD_pages.txt:7603:sister xwah(ar).                              StlOW snexr, snezag, wafr.
PHD_pages.txt:9955:wafr
PHD_pages.txt:9961:Wafrcllag                 ,~~ cat,      wisp                            Q.)3) \
PHD_pages.txt:10879:saHir, snexr            ~l'O         cehclN                                    -U
PHD_mackenzie.txt:4560:snexr [snyhl] snow.
PHD_mackenzie.txt:4561:snezag [snyeh ] snow.
PHD_mackenzie.txt:4563:snOy [snwd] (rain-, snow-)cloud.
PHD_mackenzie.txt:5136:wafr [wpll M wpr, N barf] snow.
PHD_mackenzie.txt:7603:sister xwah(ar).                              StlOW snexr, snezag, wafr.
PHD_mackenzie.txt:9955:wafr
PHD_mackenzie.txt:9961:Wafrcllag                 ,~~ cat,      wisp                            Q.)3) \
=== NYB ===
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
```


## [2026-09-14T02:28:55.827Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep snow ===\" && grep -n -i \"snow\" SOD_pages.txt | head -20; echo \"=== SOD snys ===\"; grep -n \"šnyš\\|snyš\\|šnēš\\|snys\\|Sny[sš]\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T02:28:55.897Z] TOOL RESULT

```
=== SOD grep snow ===
3144: /casm/      csm-         eye          Av. casman-               /wafr/      w/r-        snow
30592:         (ro)snow                                                         83R6
32363:                                                                   Himalaya (snowy)
32369:9914 wp,a                                                          snow
32495:                                                                             snow
39449:silent   9352                                10043, 10265, 10266, 10789             snow    9931, 9980
39450:silk 3177, 3178, 8240                     sixth day of the month      1482          GcOsnow   9312
39451:silk cloth  8854                          sixth month of the year      4549,        snowy   9930
=== SOD snys ===
15108:      f(a)snas ©<*fra-xsnasa           ©impf. fysnys                           f(a)tpez ? ©<*fra-&wa(n)zjaya-
30589:9312 snys- M                               ujuTo^ t jju jUJ^            Lion, Leo
```


## [2026-09-14T02:28:57.244Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB snexr ===\" && grep -n -i \"sn[eē][hx]r\\|snyhl\\|sn[eē]ž\\|snaēž\" NYB*.txt | head -20"
}
```


### [2026-09-14T02:28:57.310Z] TOOL RESULT

```
=== NYB snexr ===
```


## [2026-09-14T02:29:00.449Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30580,30600p' SOD_pages.txt; echo \"--- which leaf ---\"; awk 'BEGIN{RS=\"\\f\"} /9312 snys-/{print \"leaf(1-based)=\"NR}' SOD_pages.txt"
}
```


### [2026-09-14T02:29:01.881Z] TOOL RESULT

```
                                                                        wine cup srafz
                                                                                  ?    ? ©MP lsfrz-y Heb. sprzyyri
                                               ^■Lt* i4**-iZ'
         sanx (sny) ©<IE fcank ©pi. -r =»prsnx(y)
                                                                        Sogdica. 31, lib, 33.11b
         branch
                                                                  9323 srwy M, C                              (c^)jU o^
         Frag. Len. pl09; Snxyt, GMS n 2, 1142
                                                                        sruy ? =4sryw
9312 snys- M                               ujuTo^ t jju jUJ^            Lion, Leo
     snes ©Av. snaeza
                                                                        GMS 410 (zodiac sign); BSTii 879.13: C2, 87V13,
         (ro)snow                                                         83R6
         GMS 450, 452; 3sg. pres. foyftw, GMS 807; S Wf
                                                                  9324 ssky B =» sysk-y(y)
           C2 n pl3l, 20
                                                                  9325 sV C                                              c~l*
9313 spsh      B
         sp(i)s ©<Av. spis% Yaghn. sipus
         louse                                                         eight ^'st05
                                                                        (a)sta 826.28: C2, 94R28
--- which leaf ---
leaf(1-based)=444
```


## [2026-09-14T02:29:18.919Z] TOOL CALL #17: Bash

```json
{
 "command": "pdftoppm -f 462 -l 462 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462.png"
}
```


## [2026-09-14T02:29:20.631Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN leaf ~745 (p1466 snow) ===\"; grep -n \"snaiwaz\\|snaiws\" KLN_1966.txt | head; echo \"=== KLN nubes/nuance ===\"; grep -n -i \"nuance\" KLN_1966.txt | head"
}
```


### [2026-09-14T02:29:21.006Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60489 Sep 13 22:29 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462.png
```


### [2026-09-14T02:29:21.084Z] TOOL RESULT

```
=== KLN leaf ~745 (p1466 snow) ===
35743:Derivatives :  snout,  tr.  and  intr.  v.,  snout-ed,  adj., snout-er, n.,  snout-ish,  adj.,  snout-y,  adj. snow,  n.  —  ME.  snaw,  snow,  fr.  OE.  sndw,  which is  rel.  to  OS.,  OHG.  sneo,  OFris.,  MLG.,  MHG. sne,  MDu.  snee,  Du.  sneeuw,  G.  Schnee,  ON. snjor,  snjar,  sndr,  Dan.  sne,  Swed.  sno,  Goth. snaiws,  ‘snow’,  OE.,  OHG.  sniwan,  MDu.  snu- wen,  snouwen,  Du.  sneeuwen,  MHG.  snlen,  G. schneien,  ‘to  snow’,  fr.  I.-E.  base  *snoigwhos, ‘snow’,  resp.  *sneigw-,  ‘to  snow’,  whence  also Lith.  sniegas,  Lett,  sniegs,  OPruss.  snaygis, OSlav.  snegu,  Gk.  vicpa,  ‘snow’,  Homeric  Gk. vupETo;,  ‘falling  snow,  snowstorm’,  dydv-vupoi;, ‘much  snowed  on’,  L.  nix,  gen.  ni vis,  OIr. snechti  (pi.),  Mir.  snechta,  W.  nyf,  ‘snow’, OIr.  snige,  ‘drop,  rain’,  Avestic  snaezaiti, Gk.  vctcpci,  vtcpEi,  L,  nivit,  Lith.  sniega  (inf. sniegti),  OIr.  snigid,  ‘it  snows’,  W.  nyfio,  ‘to snow’,  and,  with  presential  n :  L.  ninguit,  Lith. snihga  (inf.  snigti),  ‘it  snows’.  Cp.  neve,  nival, Nivose,  nivosity.
=== KLN nubes/nuance ===
8958:continuance,  n.  —  OF.,  fr.  continuant.  See  next word  and  -ce.
11091:suetude,  ‘disuse,  discontinuance  of  a  habit’,  fr. desuetus,  pp.  of  desuescere,  ‘to  give  up  the  use of,  to  disaccustom’,  fr.  de-  and  suescere,  ‘to become  used  or  accustomed’.  See  custom  and cp.  words  there  referred  to. desulfurize,  tr.  v.,  to  remove  sulfur  from.  — Formed  fr.  de-  (in  the  privative  sense  of  this prefix)  and  sulfurize.
11639:discontinuance,  n.  —  AF.,  fr.  OF.  (=  F.)  dis- continuer.  See  discontinue  and  -ance. discontinuation,  n.  —  F.,  fr.  discontinuer.  See  next word  and  -ation.
21687:tinuance,  perseverance’,  fr.  I.-E.  base  *lip-,  ‘to remain,  persevere,  continue,  live’.  See  leave,  v., and  cp.  live,  liver,  alive.
25704:nu,  n.,  name  of  the  13th  letter  of  the  Greek  alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.  See  nun,  the  letter, nuance,  n.,  a  slight  difference.  —  F.,  ‘shade,  hue; a  slight  difference’,  fr.  MF.,  fr.  nuer,  ‘to  shade’, fr.  nue ,  ‘cloud’,  fr.  L.  nubes  (see  nubilous  and -ance);  so  called  with  reference  to  the  different colors  of  the  clouds.
25710:nubilous,  adj.,  cloudy,  foggy,  obscure.  —  Late  L. nubilosus,  fr.  L.  nubes,  ‘cloud’,  which  prob. stands  for  *snoudhis  and  is  cogn.  with  Avestic snaoda-,  ‘clouds’,  W.  nudd,  ‘fog’,  Gk.  vufWv (Hesychius),  ‘dark,  dusky’.  Cp.  nuance,  nubia, nubiform.  For  the  ending  see  suff.  -ous. nuccllus,  n.,  the  central  mass  of  the  body  of  an ovule  (hot.)  —  ModL.,  fr.  L.  micella,  dimin.  of nux,  gen.  nucis,  ‘nut’.  See  nucleus  and  cp.  words there  referred  to.
```


## [2026-09-14T02:29:26.717Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['snaiws,  ‘snow’','nuance,  n.,  a  slight  difference','nubilous,  adj.,  cloudy']:\n    i=t.find(pat)\n    print(pat[:30], 'leaf0=',t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-14T02:29:27.871Z] TOOL RESULT

```
snaiws,  ‘snow’ leaf0= 778
nuance,  n.,  a  slight  diffe leaf0= 567
nubilous,  adj.,  cloudy leaf0= 567
```


## [2026-09-14T02:29:28.148Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462.png"
}
```


### [2026-09-14T02:29:28.865Z] TOOL RESULT

```

```


## [2026-09-14T02:29:28.860Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:29:45.373Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 462 -l 462 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg462hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg462hi.png'); print(im.size)\nim.crop((3500,900,4000,1250)).resize((1500,1050)).save('pg462-fa.png')\nim.crop((1150,1400,2400,1700)).resize((2500,600)).save('pg462-sog.png')\n\""
}
```


### [2026-09-14T02:29:50.297Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-14T02:29:52.333Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462-fa.png"
}
```


### [2026-09-14T02:29:52.353Z] TOOL RESULT

```

```


## [2026-09-14T02:29:58.770Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462-sog.png"
}
```


### [2026-09-14T02:29:58.951Z] TOOL RESULT

```

```


## [2026-09-14T02:29:58.934Z] INPUT

[Image: original 2500x600, displayed at 2000x480. Multiply coordinates by 1.25 to map to original image.]


## [2026-09-14T02:30:03.031Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg462hi.png')\nim.crop((1150,1200,2000,1400)).resize((2550,600)).save('pg462-sog2.png')\n\""
}
```


### [2026-09-14T02:30:04.766Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:30:06.945Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462-sog2.png"
}
```


### [2026-09-14T02:30:07.174Z] TOOL RESULT

```

```


## [2026-09-14T02:30:07.170Z] INPUT

[Image: original 2550x600, displayed at 2000x471. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T02:30:17.010Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins sneigwh/sneudh ===\" && grep -n -i \"sneigwh\\|sneudh\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:30:17.065Z] TOOL RESULT

```
=== AHD watkins sneigwh/sneudh ===
976:sneudh-. Mist, cloud. Latin nibés, cloud: NUANCE. [Pok. 2. sneudh- 978.]
1939:NOXIOUS nek-1 NUANCE sneudh- NUB gen-
```


## [2026-09-14T02:30:19.190Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'sneig|snaoδ|snaod|snaez|snaeg|nubes|nūbēs|sneudh',t):\n    print(m.start(), t[max(0,m.start()-80):m.start()+150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:20.310Z] TOOL RESULT

```
2650391  sndudMu                    —                                                s. sneudh- „sclilafrig^‘   nichts       — zu tun haben, gegen Persson Beitr. 328 Anm. 3, s. auch Falk-Torp u. snue m. Nachtrag). Eher sind die ir. Worte 
2650573 p u. snue m. Nachtrag). Eher sind die ir. Worte verwandt, vielleicht auch idg. *sneudh~ „Neber‘ als „Feuchtigkeit'‘ (s. d.); ob hierher nach Froehde BB. 21, 185flF. thrak. vvod ,Nymphe“? (s. u. sntisds),                         5 
2653867                    ;            ;                                               sneig        sneit-                                           695  fascia‘s, corn, snod „vitta'‘ (Entlelinung dieser brit. tSW-Formen aus engl.  snood
2655418 ichen Wzformen). Zum Ablaut mehrfach nicht zutreffend Reichelt KZ. 39, 28, 55.  sneig- „kriechen‘'     ;    s.   u. sneg- ds.   sneig^h- „schneien“, snig^h-, snoig^hos „Schnee“.    Av. snaczenti {ciyqn) „an einem schneienden Tage‘
2655466 ffend Reichelt KZ. 39, 28, 55.  sneig- „kriechen‘'     ;    s.   u. sneg- ds.   sneig^h- „schneien“, snig^h-, snoig^hos „Schnee“.    Av. snaczenti {ciyqn) „an einem schneienden Tage‘‘, snaezdt (Konj.) „wird schneien", gr. viq^a Ac
2655571 ^h-, snoig^hos „Schnee“.    Av. snaczenti {ciyqn) „an einem schneienden Tage‘‘, snaezdt (Konj.) „wird schneien", gr. viq^a Acc. „Schnee‘', horn, dydwicpog „sehr beschneit‘‘,                               ve'Kpei (vtq)ei)„es schnei
2662042  Beitr. 328 Anm. 3) ist ungestiitzt.  snendh- „Nebel; nebelig, diister".    Av. snaoda- „Gew6lk“, siidbaluci nod „leichtes Gewolk, Nebel, Eegen- wolke" (nach Solmsen WfklPh. 1906, 870 zu;) lat. niihes jjWolke^^, cymr. nudd „Neber‘
2679539 iff des „Kasses“ zugrunde, sowohl nach Froehde BB. 21, 185ff. eine Bildung von *sneudh- „flie6en“     —   s,   u. sna- „fliefien“           Gdf. (s)midh-s-a),   sraqj-to-, -ti- „scbarfkantig, scharfe Kante, Ecke, Felszacke‘‘?   Ai
```


## [2026-09-14T02:30:29.536Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD snow ===\"; grep -n -i \"snoigwh\\|SNOW sn\\|snaiwaz\" AHD_watkins1985.txt | head -10; echo; echo \"=== AHD lines 970-985 ===\"; sed -n '965,985p' AHD_watkins1985.txt"
}
```


### [2026-09-14T02:30:29.596Z] TOOL RESULT

```
=== AHD snow ===
972:sneigh-. Snow; to snow. 1. Suffixed o-grade form *snoig’h-o- in Germanic *snaiwaz in Old English sndw, snow: SNOW. 2. Zero-grade form *snigvh- in Latin nix (stem niv-), snow: NEVE, NIVAL, NIVEOUS. [Pok. sneigth- 974.]
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-

=== AHD lines 970-985 ===
sna-. To swim. Contracted from *snaa-. 1. Extended form *sndgh- in Greek nékhein, to swim: NEKTON. 2. Suffixed zero-grade form *(s)na-to- in Latin natdre, to swim: NATANT, NATATION, NATATORIAL, NATATORIUM; SUPER- NATANT. 3. Attributed by some to this root (but more likely obscure) is Greek nésos, island: CHERSONESE. See (s)nau-. [Pok. snd- 971.]
(s)nau-. To flow, let flow, whence suckle. Contracted from *snaau-; extension of sna-. 1. Suffixed basic form *naw-yo- in Greek naein, to flow, whence probably Naias, fountain nymph: NAIAD. 2. Zero-grade form *ni- (< *nua-) in suffixed form *ni-tri- (with feminine agent suffix) in Latin ndtrix, nurse, and nitrire, to suckle, nourish: NOURISH, NURSE, NURTURE, NUTRIENT, NUTRI- MENT, NUTRITION, NUTRITIOUS, NUTRITIVE. [In Pok. sna- 971.]
(s)né-. Also né-. To spin, sew. Contracted from “(s)neo-. 1. Suffixed form *né-tla in Germanic *néthlé in Old English nédl, needle: NEEDLE. 2. Suffixed form *sné-mn in Greek néma, thread: NEMATO-; CHROMONEMA, PROTO- NEMA, SYNAPTINEMAL COMPLEX, TREPONEME. [Pok. (s)né- 973.]
(s)neeu-. Tendon, sinew. Extension of (s)né-. Suffixed form *(s)neow-r-, further suffixed in: a. *neu-r-o- in Greek neuron, sinew: NEURO-, NEURON; APONEUROSIS;
sol-
b. metathesized form *nerwo- in Latin nervus, sinew: NERVE; ENERVATE. [Pok. snéu- 977.]
sneg-. To creep; creeping thing. 1. Suffixed o-grade form *snog-on- in Germanic *snak-6n- in Old English snaca, snake: SNAKE. 2. Variant Germanic root *sneg- in suf- fixed o-grade form *snag-ila- in Old English snzxg(e)l, sneg(ejl, snail: SNAIL. [Pok. ? sneig- 974.]
sneigh-. Snow; to snow. 1. Suffixed o-grade form *snoig’h-o- in Germanic *snaiwaz in Old English sndw, snow: SNOW. 2. Zero-grade form *snigvh- in Latin nix (stem niv-), snow: NEVE, NIVAL, NIVEOUS. [Pok. sneigth- 974.]
sneit-. To cut. 1. Germanic *snithan in Dutch snijden, to cut: SNICKERSNEE. 2. Expressive Germanic *snitt-ja- in Middle High German sniz (> German Schnitz), slice: SCHNITZEL. [Pok. sneit- 974.]
sner-. Expressive root of various verbs for making noises. 1. Germanic *sner- in North Frisian sneere, scornful remark, perhaps akin to the possible source of SNEER. 2. O-grade form *snor- in Germanic *(s)nor- in: a. Middle High German snurren, to hum, whirr: SCHNORRER; b. German snarchen, to snore: SNORKEL; c. Middle Low German snarren, to snarl: SNARL!; d. Middle English snoren, to snort: SNORE; e. Middle English snorten, to snort: SNORT; f. possibly Old Norse Norn, goddess of fate (< “the whisperer”): NoRN. Compare snu-. [Pok. 1. (s)ner- 975.]
(s)ner-. To wind, twist. 1. Suffixed extended zero-grade form *snork- in Germanic *snarh-6n- in: a. Old Norse snara, cord, noose, trap: SNARE}; b. Dutch snaar, string: SNARE?. 2. Proposed by some as a derivative of this root is Germanic *narwa- in Old English nearu, narrow: NARROW. 3. Extended variant form *(s)nark- in Greek narké, cramp, numbness: NARCO-, NARCOSIS, NARCOTIC. [Pok. 2. (s)ner- 975.] sneubh-. To marry. 1. Latin niibere, to marry, take a husband: NUBILE, NUPTIAL; CONNUBIAL. 2. Possibly nasalized zero-grade form *nu-m-bh- in Greek numphé, nymph, bride: NYMPH. [Pok. sneubh- 977.]
sneudh-. Mist, cloud. Latin nibés, cloud: NUANCE. [Pok. 2. sneudh- 978.]
sneud(h)-. To be sleepy. Expressive root. Compare snu-. Zero-grade form *snud-to- giving *nusto- in Greek nusta- zein, to be sleepy: NYSTAGMOUS. [Pok. 1. sneud(h)- 978.] snu-. Imitative beginning of Germanic words connected with the nose. 1. Germanic *snit-, *snut- in: a. Old English gesnot(t), nasal mucus (ge-, collective prefix; see kom): SNOT; b. Middle Dutch snut(e), snout, akin to the probable source of Middle English snute, snout: SNOUT; c. German Schnauze, snout: SCHNAUZER, SCHNOZZLE. 2. Germanic *snuf- in: a. Low German or Dutch snuffe- len, to sniff at: SNUFFLE; b. Middle Dutch snuffen, to snuffle: SNUFF!; c. Old English *snyflan (> Middle English snyvelen), to run at the nose: SNIVEL; d. Middle English sniffen, to sniff: sNirF. 3. Germanic *snup- in Dutch snoepen, to eat on the sly, pry: SNoop. 4. Ger- manic *snip- in Low German and Dutch snippen, to snap at: snip. 5. Germanic *snap- in Middle Low German and Middle Dutch snappen, to snap at: SNAP. 6. Germanic *snub- in Old Norse snubba, “to snub, turn up one’s nose at,” scold, rebuke: SNUB. 7. Germanic *snak- in Middle Dutch snakken, to snap at, akin to the Low German source of Middle English snacchen, to snatch: SNATCH. [In Pok. snd- 971.] so-. This, that (nominative). For other cases see to-. 1. Greek ho (nominative plural Aoi), the: HOI POLLOI. 2. Feminine form “syd in Germanic *sjé in Old English séo, sie, she: SHE. 3. Compound variant form *sei-ke (*-ke, “that”; see ko-) in Latin sic, thus, so, in that manner: sic}. [Pok. so(s), sd, si 978.] sol-. Also sole-. Whole. I. Basic form *sol-. 1. Suffixed form *sol-ido- in Latin solidus, solid: SOLID; CONSOLI- DATE. 2. Suffixed form *sol-wo- in Greek holos, whole: HOLO-; CATHOLIC. 3. Dialectal geminated form *soll-o-
spé-'
in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
sper-4
ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
spere-
spréot, pole (< “sprout, stem”): sPRIT; d. Middle English bouspret, bowsprit: BOwsPRIT. 3. Extended form *spreit- in Germanic *spraidjan in Old English sprédan, to spread: SPREAD. II. Basic form *sper-. 1. Suffixed form *sper-yo- in Greek speirein, to scatter: Diaspora. 2. Suf- fixed form *sper-mn in Greek sperma, sperm, seed (< “that which is scattered”): SPERM}. III. O-grade form *spor-. 1. Suffixed form *spor-d- in Greek spora, a sowing, seed: SPORE, SPORO-. 2. Suffixed form *spor-nd- in Greek sporas (stem sporad-), scattered, dispersed: SPORADIC. [Pok. 2. (s)p(hJer- 993.]
spere-. Ankle. Zero-grade form *spr(o)-. 1. Germanic suffixed form *spur-6n- in Old English spura, spora, spur: SPUR. 2. Nasalized form “spr-n-o- in Germanic *spurnon in Old English spurnan, spornan, to kick, strike against: SPURN. 3. Germanic suffixed form *spur- am in Middle Dutch spor, spoor, track of an animal: Spoor. [Pok. 1. sp(hJer- 992.]
spergh-. To move, hasten, spring. Nasalized root form *sprengh-. 1. Germanic *springan in: a. Old English springan, to spring: SPRING; b. Middle Dutch springen (> Dutch springen and Afrikaans spring), to leap: KLIP- SPRINGER, SPRINGBOK; C. Old High German springan, to jump: GELANDESPRUNG. 2. Germanic causative *sprang- Jan in: a. Old English besprengan, to sprinkle, scatter: BESPRENT; b. Old English *sprencg, snare used to catch game: SPRINGE. [Pok. spergh- 998.]
```


## [2026-09-14T02:30:31.537Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT snaez ===\"; grep -no \"snaez[a-zA-Z]*\\|snaeZ[a-zA-Z]*\\|sna[eE][zZjž][a-zA-Z]*\\|snaoS[a-zA-Z]*\\|snao[dδ][a-zA-Z]*\" BRT.txt | head -30"
}
```


### [2026-09-14T02:30:31.591Z] TOOL RESULT

```
=== BRT snaez ===
20527:snaoSca
27087:snaoS
27090:snaoS
```


## [2026-09-14T02:30:37.333Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pos in [20527,27087,27090]:\n    print('---',pos,'leaf0=',t[:pos].count('\\f'))\n    print(t[pos-600:pos+600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:38.449Z] TOOL RESULT

```
--- 20527 leaf0= 18
5) :  Y.  6. 18. 5    ■3):Y.i9.4. 27  :Z. 6li6):Y.39.s. 28  :  Y.J.  25. 7(i8):Vr.7Ö.2. 8.  1  :  A.  7.  1,  13,  YL  17.  5,  Y. 3  {4Ü  3'  (S)i  4  (9);  5  (10); 8:Y.2/.i5,59.33,Yt.7.22 3.  18.  7*.  8. H(75M:Vr.5...77.20. 6(13);  7  (15);  8  ('7). 9:Y.J.  25. 2    3   :  Y.  7J.  4. 3(0:Y...i8. 9.1. 4  17)  :Y.  7.  23. 2  (5)  :  Y.  9.  4,  7.  10 '3- 5;Y.j.25. 3(9):V.p.6,9,  12 JS{7(5).  i  :Vr.6.i,  G.5.6. 4  (li);Y.s.2,  7,  10 13.  vt. 2  (4)  :  Z. 75.  16. 3  (8)  :  \.s6.  1. S(>7)-Y(-79.33- 4:Y.J.2S. 6(3l):Y.9-3- W   7/    l:Y.7fi.2. 7(22):  Ys- 2,  4. 2(S):Y.7S.I. 8(35);Yt.5.34.  p 14,  75. 3  (ilh  4(19'- 24.  77-  34,  7p-  37- 5  126) -.8.=.  22. 9  (»8):Y.s.3- 6(34l ■  o(29):Y,5.2,  4. 7:42  TVr.  7.1. 11  (34) :  Yl.  79. 40. 8  (45) :  Y.  ÖÄ  3,  Yt.  S.  Sl. 12  M:Y.il.3- 9  (50);  10  (53)- I3(40:Y.p.2  4. 17.  1   (56)  :  Y.  2.  2. 14  t44)cYt.7g.8i. 1-17  :Y.  59.  1-17. 15  (46);  16  (48);  17  (S4> 2-10:Y.2.3-ll. l8(6o):Yl.7*4!J'.lo.5-l3, ii(62):Y.59.i". 70.34J5.22,7*62.7J.33. ia-l7:Y.2.  12-17. Die  awestischen  Texte.    Konkordanz 8:Y.2fi.  1,77.22,  Yt7j.2i S.  3. 30. 9  :  Y.  2. 18. iff.  iZ. 2(3)!Y./9-4. 3  (4)- i{S):Y.  19.3. S(6X 6(9):Y./9
--- 27087 leaf0= 20
17,    18. 2  :  Vr.  24.  4. II  (54  1  V./j-.  u. n(/2).i;  2(8). 24  (27).  o:Vr.7j.o.  7.^.1,2. U(S7  :Y.^/.8,  G.AS. 3  li4):Y.22.  1. I  (l):Vr.20.l,2. .3(6.  iV.45.6. 4li7).5  =  V.22.2,3. 3  ;  Vr.  T4.  4. U  (65  . 6(18):  V.V.»,  Vr.4.a. 4:Y.7Al,l. 15  (67) :  Y.  zj).  7. 7  {2i):Y.2^5. l6  (7lli  17  (74)- >8  (79)'Y.J4.2,  5J.6,5Ä8, 8-M:y.  2.^.1-3. ii(22);y..#.4.  J9.3- X'arlak  apastsk. Ny.  /.  9. 19  (88}-al  :  V.  &  14-16. 13  125)  :Y.*  5. Gl.    1  :  Y.  27.  14. «4  (30)- Z:Y.27..3. 3J;Y.  77. 18. 15  (33):Y..#.6. Nk.  1  iVt.  7.0. 13  (89):  Y.  2.1z,   l6.^,    Vi. 16  134)  :Y.  7.1,2,  4. 2, 22, 23. 2  :  Y.  72.  7-9,  72-  9- 7.  5,  G.  /.  9. 17  (35),   l8:Vr./0.1,2. SrB.I  :  Z. 24(9S)-V.J7.4- 19  {f3-  I)- 2:Y.J7.i,  V.//.3. 25:^.^5.4,  ^tf.ö- 20  (75.2);  Vr.  5.1. ):Yt.J.17,  V.Ä21. 2fr-28  :  Z. 21  ys.7):\:4.6. 4  ;  Y.72.  6. 29-31  :Y.&.i. -13. 12(7^1.  1  :  Y.27.6. 5  ;  S.6S.  19,  ki.8,  Aoc.  112. 72(7^).  1-5  :V.5/.  1-5. 2  (5) :  V.  27.  7. Hb   1  :  V.  77.  3. 6;  Y.2^.a3,7?.8,  YLj.23, 3(8i 4  (9) ;  Y.  27. 7,  Vr.  72. 5. 3-S  :  Z. Ny./.i7,SrB.v,G./.io. Ny.  1.1-9  :N>S.i. T.Z. 5  (i3]:Vr.72.5. 2  ;  Yl.  /.  0. 8:Y.73.6
--- 27090 leaf0= 20
    18. 2  :  Vr.  24.  4. II  (54  1  V./j-.  u. n(/2).i;  2(8). 24  (27).  o:Vr.7j.o.  7.^.1,2. U(S7  :Y.^/.8,  G.AS. 3  li4):Y.22.  1. I  (l):Vr.20.l,2. .3(6.  iV.45.6. 4li7).5  =  V.22.2,3. 3  ;  Vr.  T4.  4. U  (65  . 6(18):  V.V.»,  Vr.4.a. 4:Y.7Al,l. 15  (67) :  Y.  zj).  7. 7  {2i):Y.2^5. l6  (7lli  17  (74)- >8  (79)'Y.J4.2,  5J.6,5Ä8, 8-M:y.  2.^.1-3. ii(22);y..#.4.  J9.3- X'arlak  apastsk. Ny.  /.  9. 19  (88}-al  :  V.  &  14-16. 13  125)  :Y.*  5. Gl.    1  :  Y.  27.  14. «4  (30)- Z:Y.27..3. 3J;Y.  77. 18. 15  (33):Y..#.6. Nk.  1  iVt.  7.0. 13  (89):  Y.  2.1z,   l6.^,    Vi. 16  134)  :Y.  7.1,2,  4. 2, 22, 23. 2  :  Y.  72.  7-9,  72-  9- 7.  5,  G.  /.  9. 17  (35),   l8:Vr./0.1,2. SrB.I  :  Z. 24(9S)-V.J7.4- 19  {f3-  I)- 2:Y.J7.i,  V.//.3. 25:^.^5.4,  ^tf.ö- 20  (75.2);  Vr.  5.1. ):Yt.J.17,  V.Ä21. 2fr-28  :  Z. 21  ys.7):\:4.6. 4  ;  Y.72.  6. 29-31  :Y.&.i. -13. 12(7^1.  1  :  Y.27.6. 5  ;  S.6S.  19,  ki.8,  Aoc.  112. 72(7^).  1-5  :V.5/.  1-5. 2  (5) :  V.  27.  7. Hb   1  :  V.  77.  3. 6;  Y.2^.a3,7?.8,  YLj.23, 3(8i 4  (9) ;  Y.  27. 7,  Vr.  72. 5. 3-S  :  Z. Ny./.i7,SrB.v,G./.io. Ny.  1.1-9  :N>S.i. T.Z. 5  (i3]:Vr.72.5. 2  ;  Yl.  /.  0. 8:Y.73.6;
```


## [2026-09-14T02:30:45.064Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['schnei','Gew.lk','Schnee']:\n    for m in re.finditer(pat,t):\n        print('---',pat,m.start(),'leaf0=',t[:m.start()].count('\\f'))\n        print(t[max(0,m.start()-400):m.start()+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:46.569Z] TOOL RESULT

```
<persisted-output>
Output too large (54.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bt756is8y.txt

Preview (first 2KB):
--- schnei 515236 leaf0= 129
.  H.  3.  20. •  j.  avaS-ät  Adv.  'so',  in  zurückweisen- dem Sinn:  av  ila  sraoli  asta  "so  soll sich  hier  der  Gehorsam  einstellen"  Y. 5«.i. Abl«it.  ans  ava%a  (sd.  3);  »gl.  tAäl.  —  Pfi.: tiS«,  Sü.:  rt'am, •  j.  ava(he  (indekL):  ihe  (sd.)  tha  yahna ahmai  av°   iha  yahna  ahmsi  avSya  iha lyahna  ahmai  Yt  75.63.  Sinnlose  Fluch- worte. *ava.3Twar98a-    m.    'Abschneiden, dby  Google 173 avaSra avant- 174 •  j.  ava-Duhabdamna-,  -Dhabdamna- Adj.,  PPM.:  s.  :e'ap: KompE. j.  avanräsayäl  N.  ^j  s.  ras-. •  j,  ava-ahabdant-  Adj.,  PPA.:  s.  *"a/-. •  j.  a-vaahav-  Adj.  'ungut,  böse':  tT daSväil  ayäis  ^'tihls  (IV.y ..  sar)m  mruyl Y.12.4. Able
--- schnei 1049617 leaf0= 242
amV.gam-, •  p,  upa'darma-  m.  £N.  eines  Mannes: /  martiy^  ah''ind'  nämd'  'makyä pU^^'J' hauv  udapatats  ''uvajaiy  Bh. /.  16. Eig.  etwa   'der  Ordnung   Untertan';    *darma- die  Lesung  richtig  und  das  Wort  persisch  ist; s.  luletzt  Gray  AJPh.  a/.  4,  Fov  KZ.  57. 541,  HOsiNG  KZ.  38.  248. j.  upadari^ku  Y.  lO.    17:  lies  upa  dtriz'. •  j,  upa.9TVarätay-  f.  'Anschneiden  sva. Durchstechen  des  Grabendamms,  Damm- durchstich': yaval  ai^a  ä/s  byärixti  (sd.) 'ti  {VA.)  frabavät  ^.14.1$. Pü.:  a/wr  fia  baidnn;  vgl  Y.  ig.  3;  ob iun-iiui •  j.  upa.^^v^rasa-  m,,  Plur.  'Bresche': alte  mazdayasna  ahe  nmUnahe  'sqn  upa,- %wpr/sayqn  ". .  soll
--- schnei 1071985 leaf0= 247
...
</persisted-output>
```


## [2026-09-14T02:30:53.616Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(845,860):\n    s=leaves[i]\n    # print column numbers appearing\n    import re\n    nums=re.findall(r'\\b1[5-7]\\d\\d\\b',s)\n    print(i, nums[:6], s[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:54.813Z] TOOL RESULT

```
845 ['1546', '1548'] b  ys haemahe  mala  (sd.)  asa  haldiU  'srnana Y,  10.  8.  2)  n.  'Freude,  Wonne,  Selig- keif:  7a/.  .^(Wi-aW«  a
846 ['1550']   ")  Vgl.  V.  /(f.  19.  —  a)  S.  ferner Pü.  lu  ajyamna-,  atisla-  (,  wo  avismiin  zu lesen),  jayäi,  'Jyä-,  
847 [] sammenbang  stehen.  Jlaoma  wird  -  nach der  falschen  Lehre  -  zur  Hilfleistung  veran- lasst dadurch,  dass  man 
848 ['1536', '1553'] �r^f««-)  genannt bei  Zara%uitrai  Rettungswerk  zu  helfen  wird:  Aaia  gayäi  manknat  J  •yantai^'' bereit  sind:  
849 ['1554'] ein',  mit  Dat  der  beteiligten  Person:  ym näiriia  vohunT^  aiwixamat  yat  kl  %rayS xSafna  salante  "wenn  die  
850 ['1556'] a  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  'ta  . .  tisrS  '
851 ['1559'] aisqm  'fänhüY.^j.tT.  a)  'Huf- stilck,  Stück  eines  Pferdehufs':  'fim  vä  ää- lirum  vä  zfm.var>tpm  vä  kqmBt  v
852 ['1560'] �ble  Gerüche empfinde"  H.a.  35;  7.  zu  b):  na^.a manyäe  jaynvi  */ia^a.am  y»nam  sadayetti yavata  .  .  "nicht 
853 [] nutzt Vr.  13. 1 1  'va  aSavabyS  yazamaide;  —  auch Plur.:  yS  ma  dngvä  (Sp.  776  o.)  äzc^  °vä paiturfte  "der 
854 ['1565'] inen  senkrechten  Keil,  sowie  am  Ende der  Zeile  wieder  einen  senkrechten  Keil  er- kennen lassen,  während  all
855 ['1566', '1568'] on  den  Glas- gefässen  einzelne  Scherben  gibt,  (als  ob) er  so  viel  . ."  V.Ä85. Znm    ai.  V.  ifnhi,    vgl. 
856 [] gegen  die  Sghander  der  (deiner) Lehre  zusammen  mit  all  denen,  die  . ." Y.4^.  14. Zum  ai.  V.  iärdhati').  —
857 ['1571'] Vor- habeDs)',   % /S4,    —   Pü.!   lArmasui  loj^anän (Sü.:    vacaiim)   ämärtnltär,    erl,:  fa   vinäs   ii Aarfa
858 [] ^;  —  yaAmi  jä>^  (3PPM.)  . .  jata paun'a{Sf.S$$  m.)  ma/yäiiäaAl'  Vt.io.So; —  neij  zT  m  sä  M  (sd.)  ya  dar
859 [] .baoya-"  Adj.  'aus,  vor  dem Untergang  rettend':  haoimm  baire  'ffm Aaomim  vfrphrä/atum  baire  Yt/rf-SJ. 'itufja
```


## [2026-09-14T02:31:02.809Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(875,905):\n    s=leaves[i]\n    nums=re.findall(r'\\b1[5-9]\\d\\d\\b',s)\n    hits=re.findall(r'\\bsna\\w*',s)\n    print(i, nums[:4], hits[:10])\nEOF"
}
```


### [2026-09-14T02:31:03.890Z] TOOL RESULT

```
875 [] []
876 [] ['snaihiüi']
877 [] []
878 ['1612'] []
879 [] []
880 [] []
881 ['1561', '1618'] []
882 ['1620'] []
883 [] []
884 ['1624'] []
885 ['1626'] []
886 ['1637'] ['snaeg', 'snaisa', 'snaüainiyliica', 'snaHintalia', 'snalzinti', 'snaliiniyä', 'snaoo', 'snalzät', 'snae', 'snaig']
887 [] ['snafrant', 'sna', 'snadäi', 'sna', 'sna', 'snad', 'sna', 'snai', 'sna', 'snaya']
888 ['1631'] ['snaiSe']
889 ['1903'] []
890 ['1634', '1634', '1635', '1636'] []
891 ['1634'] []
892 ['1637', '1638'] []
893 ['1640', '1607'] []
894 ['1642', '1641', '1603', '1603'] []
895 ['1640', '1644'] []
896 ['1646', '1616', '1641'] ['sna', 'snaiSinfyai']
897 ['1647', '1590'] []
898 ['1641', '1650'] []
899 ['1651', '1653', '1652'] ['snaviihm']
900 ['1607', '1654'] []
901 ['1653'] []
902 ['1657', '1658'] []
903 [] []
904 ['1660'] []
```


## [2026-09-14T02:31:06.262Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ns=leaves[886]\ni=s.find('snaeg')\nprint(s[max(0,i-1500):i+2500])\nEOF"
}
```


### [2026-09-14T02:31:07.352Z] TOOL RESULT

```
 Bruders des  Yima:  'urimca  yim5.k>r3nt>in  "den Sp.,  der  den  Y.  (mit  der  Säge)  entzwei- schnitt'"' YL15. 46.
•)  Zusimmer  mii  oder  veranlasst  durch  Aüty Dakäka.  litt,  bei  vonStackelberg  WZKM. li.  245.
Eig.  'der  weisse  SchaOämmer  hat'.  Neben *jj^i"J-  ^=  ni.  urä-  stand  im  Komp.  ai.  *iirä-; vgl.  Bthl.  IF.  11. 137,  Bgm.  KuneVglGr.  144- S.  noch  varaiasana-.  —  ')  iSchr.  •yui'  statt 'ivr'  vgl.  S  26S.  i8.
•  j.  spinja —  ?  — ,  vll.  Bezeichnung  eines Volksstamms  od.  dgL''
KompA.  —  Auch  sfinj'  geschrieben.  —  Vgl. spmgha:  —  >1  JusTls  Annahme,  NB.  508  halte ich  für  wenig  wahrscheinlich.
•  j.  spinja-uruska-  m.  EN.  eines  Un- gläubigen, Feinds  des  Vi^täspa:  uta  azsm nijanäni..  'hm  dalvayasnim  Yt.f?, 31.
Eig.Bed.?  —  *arui:*a.  vll.  =  lat.  Äürm?').— mp.  spinjrul,  in  Pü.  zu  Y.  //.  11,  sowie SWienAW.  6/.  840.  5,  845.  25  mit  sjanjavya- verwechselt.  —  ■)  Anders  JusTl  NB.  508.
•  j.  spi§-'>  n.  'Laus,  Milbe  (od.  dgl.)': Sat . .  xrafstra  hqm.bavainti  yiin  masyäia spis{NS.)  nqma  aojaile yim  tnasyäta  yaom yavS.kva  nnganh}nti  vastra  vasträhva ".  .  die  Xr.  . .,  was  die  Leute  'Laus' nennen,  was  den  Leuten  das  Getreide  in den  Speichern  wegfrisst,  die  Kleider  in den  Kammern"  V.iy.^'K
mp.  spis,  sfus,  np.  supiis.  —  Pü.:  spis.  — ')  Oder  aucb  spis-,  —  *)  Grammatisch  geringe Stelle.
j.  ipnArim  P.  26:  lieg  x!«aa%rim.
•  j.  snaeg- V. 'schneien' (persönl.).  Praes. 2  snaisa:
i)  intr.  'als  Schnee  (zur  Erde)  fallen', nur  PPA.  als  Attribut  'Schnee-':  Sat altatiha  sps  yat  snaüainiyliica  srasSti- tyäi(s^.)ca  V.  6'.  36''.  a) 'Schnee  fallen lassen':  mllti  zl  m!  hlm  . .  vär>ntag{5A..)ca snaHintalia  (3Plur.,  näml.  arläna)  . .  Yt. I  5.  lao;  —  värmti  (sd.)  vä  snalzinti  vä .  bamtti  v3 . .  ayqn  "die  pluviali  sive  nivah ,  sive  ventoso"  V.  8. 4'';  —  xsa/nS  var?fttyä \  snaliiniyä  "in  einer  Nacht,  die  (sva.  in der  es)  . .  schneit"  Yt.itf.  lo^'.  a)  mit Akk.  des  Inhalts  aus  va/ra-  (sd.):  yahmai haca  .  .  snaoo^  (sd.)    va/ra    snalzät    V.
2.2  2. ahd.  sneivit,  lit.  ineja;  mp.  vgl.  utix,  snixr (wozu  Bthi,  ZDMG.  ja  697).  —  Pa.  (zu V.  S):  sittx,  eri.:  vajr,  (zu  V,  Ö):  siiixr, (lU  V.  3]i  undeuUich.  —  0  Wörtlich  'des Wassers,  das  als  Schnee  fSllt,  gefallen  ist'.  — ")  Wörtlich  'an  einem  Tag,  der  regnet..'; Bthl.  1F.  /.  178.  Dbr.  VglS.  3.  24  hat  das nicht  beachtet.  —  J)  S.  No.  2.
•  j.  snae^ana-  Adj,  'geifernd':  'zanü  (nUml. as/i  spa)  yaha  apinttHyu!  V,/J.  48;  — jq%wa  .  ,  vihrka  'na  V.  JJ.  40.
Zum  V.  snaig-;  eig.  'Schnee  fallen  lassend sva.  Schaum,  Geifer  aus  dem  Maul,  Mund flicssen  lassend';?).  —  Pö.:  *siirxre>«/äri).  — 1)  So  wird  wohl  an  beiden  Stellen  zu  lesen sein;  s.  zu  snaeg^
•  j.  snae2ant-'>  Adj.  (fem.  'nü-),  PPA.: S.  snatlg-.
')  Es  ist  nur  'ünr  bezeugt
•  j.   snaoJa-  m.  'Gewölk':  yahmat  haca
PaurvS    "S^   va/ra    snatiät    bartzisiatibyö
gairibyS  "weshalb   zunächst   das  Gewölk
Schneemassen  herschneien  wird  von  den
höchsten  Beiden  her"  V.  2. 12.
Vgl.  sbal.  nid  (S  S3.  2);    s.  GOR.  SBayrAW.
ig.  I.  139;  vgl.  noch  Pü.  —   Pü.:  kt  hal  an
ape  vas  pa  ddndann  va/r  ddn  dan  n  pa  baust
apar  garän ,    sie    zeigt    also    für    snaoiä   und
j'jiif^/(sd.)  die  nämliche  Zeichenreihe;  ist  an
erslerer  Stelle  pa  snoiän  in  lesen?
•  j.snaoÄant-Adj.(fem.''Sj«Ä-)'kreischend, schreiend  (od,  dgl.)':  äat  ti  (aümL /ainis) °hnti/  g>mänä  hasU  nivarszayin  (sd.) dagva  Yt  IQ.  80.
PPA.  einer  (ar.)  Basis  •«««<*>>).  —  Pü,: %.  West  SBE.  4^,  60.  —  t)  Ganz  Unsicheres bei  FiCK  VgIWb.4  3.  316.
•  j.  snaoSö.manah-  Adj.  —  ?  — :  ^^  asti °nä  yS  nSiX  a%a  snachs.vaci  ys  ridij  a&a ^sna^öja0%nä  VytJJ.     Wertlos.
dby  Google
1637
snaoSö.vac
```


## [2026-09-14T02:31:25.569Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in [268,269,270,271,272,290,291]:\n    print('=== leaf',i,'(p',i-21,') ===')\n    print(leaves[i][:700])\nEOF"
}
```


### [2026-09-14T02:31:26.849Z] TOOL RESULT

```
=== leaf 268 (p 247 ) ===
— 247 -
1102***** hetnänä gleichsam; ja wolil, wie es scheint',
hemdnend ^).
phlv. Iminänäk, jüd.-pers. X^NOir (Is. 1, 9j.
kern - mänä bezw. mänend, vergl. No. 967.
IMickert, ZDMG. 10, iry2 :l
/^llO.'l heute all, ganz*.
ap. aw. Iiatnu' all, ganz; phlv. Iiamuk; ai. samd-.
knrd. heniä; bei. hama, hainak, liamnk (151).
1104. heiue, niB- (Verbalpraetix) , bei FirdüsT auch dem
Verbum folgend.
phlv. hamai-, paz. harne.
Uisprünglich *immer ; steht auch vor Inlinitiv und
Participien, eine Construction die jetzt wieder modern
wird *^).
Fr. Müller construirt WZKM. 5, 64 ein ap. hamaiij
— (aw.) 'hamä-li' als Grundform.
1105. heiuymi 'Gürtel*.
aw. *A«/// -r i^l/dh' 'umgürten , vergl. aw. aiwyäonh-
ana- 
=== leaf 269 (p 248 ) ===
— 248 —
80, 318), Tüchtigkeit*; ai. sündra-, skr. sundani^)
'schön*: phlv. hunar, arm. LW. hnar.
LW. kurd. huner; af;'. bei. (95) hunar.
1/1109. henffäm *Zeit', Ungarn (AM. 213 Zeile 4 v. u.).
ap. *han(/ama' *Zeit*, vergl. aw. aiwLgäma^ 'Winter ;
phlv. hangäm (päz. ögäm), arm. LW. angam *Cbel,
Unglück'.
^1110. henöz noch* (reimt auf iös, 5ö5, y ö-e bei Firdös i
und im Burzönäme, Macan, 1533 Vers 3 v. u., 1583
Vers 17, 2260 Vers 6, 2212 Vers 1), henüz (reimt
auf äz, teinüz, Sadi, Gulistän, Sprenger, 93 Zeile
1 V. u.; 10, 7; Sahn. I, 135 Vers 118)2), ^^^ (gä^n.
I, 67 Vers 97).
Darmes teter. Et. ir. II, 114, 115 ist durchaus
verfehlt.
Zusammenhang mit arm. hanapaz *immer (WZKM.
5, 355, Fr. Müll
=== leaf 270 (p 249 ) ===
- 249 —
4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
^^|j^' Pflanze, AM. 268).
'' aw. haowa-; phlv. hötn; ai. soma-.
bei. vergl. hörn (LW., 99).
V1114. Äe^ jemand, jemals*, mit Negation 'niemand, nichts;
ec (äähn. I, S. 4 Vers 59).
W^ Käs. K. Z. ec,
ap. *(tiva ~r ciy (Salemann, Mel. asiat. IX, 241);
phlv. ec bezw. hec (päz. hec, hSöi),
1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',
das man daraus erschlossen hat, ist aber bedenklich^).
aw. aeAlrapaiti' ; phlv. ehrpat (Inschriften), lierput,
herpatastän, herputlh bezw. erpat,
1116. lilrek, {^hereh?) 'Bockchen, Zickchen'.
ap. *yö*V7/ra- 'Jährling (Tomas chek, Cent
=== leaf 271 (p 250 ) ===
— 250 —
1,V.
1118. i, L Izäfe.
aw. f/at; phlv. /", päz. i.
Das Neutrum nimmt auch Caland, Zur Syntax
der Fronomina im Awesta, S. 24 als Grundform des
np. ? der Izäfe an ').
{^118»''^ yfi oder.
Da die Lesung des entsprechenden, jedenfalls aber
mit %" anlautenden Pehlevlwortes ganz unsicher ist,
so lässt sich keine sichere Etymologie aufstellen.
Die neueste Fr. Müller\s (WZKM. IV, :35(i), der
als Grundform ap. "^adcivd annimmt, ist möglich aber
auch nicht beweisbar. ,, . , ,.
\/fll9. {\)yäd ^Erinnerung, Gedächtniss', yädifär.
aw. yäta- 'Gedächtniss (Geldner, Studien I, 10,
Note 2); phlv. ijät (vd. 19 (96)), sonst äyät^).
Anders Fr. Müller, WZKM. 5, 265.
1120. {lyyäd (Suflix), in hunyäd,
ap. 'd
=== leaf 272 (p 251 ) ===
\
— 251 —
aber ohne Erfolg, da er np. yärwer nicht kennt.
Dieses ist etwa wie np. döstdär zn beurteilen ; yüwer
ist aus yürwer entstanden.
Darmesteter's (Et. ir. I, 73) Erklärung des
Suffixes -yär - vergl. beytyür 'glücklich* , hösyär
Verständig', däwyär * Jäger , sehrydr 'Herrscher u.
a. m., sowie den Eigennamen hfendyär etc., auch
talniudisches imriN (de Lagarde, Ges. Abh. 71) —
aus altem -data- auf lautlichem Weife ist natürlich
ganz unmöglich; dieselben gehen vielmehr auf *-(/6lrw-
zurück, wie phlv. satrdarän der Inschriften beweist
(vergl. Bartholomae, Litbl. f. or. Phil. I, 16)^). Bei
Isfendydr u. a., wo direkt eine ältere Form auf -data-
vorhanden ist, ist das np. r nur durch Verschre
=== leaf 290 (p 269 ) ===
— 2f)9 —
42. azg (d. i. azak) 'Ziege (PPÖl.).
ai. ajd' *Bock , ajd- 'Ziege' ; lit. osys, lett. aßs *Ziegen-
bock*, ozMi *Ziege'. Dazu wohl auch arm. aic (H. No. 16),
gr. al^ und aw. iza^na- 'aus (Ziegen)fell- (?) , ledern
(vergl. ai. ajina- 'Fell'; wa/. ijWj sar. Jein *Filz ; ksl.
a^rwo Teir) 0-
43. «j? 'Schlange'.
aw. aSi' (vergl. oben unter No. 76). Im Np. nur
in ezdehä erhalten.
B.
44. hag 'Teil, Anteil' (M^n.), arm. LW. hacj 'Anteil, Erbe'.
aw. baya- 'Teil, Anteil' neben häga (oben No. 169).
45. hay 'öott'.
ap. haga- 'Wott'; aw. haya-x ai. hhäffha-; ksl. hogn
'Gott'.
46. hwftan 'schenken', vergl. np. leystdev (oben No. 186).
47. hayf mit Hülsen versehen (Getreidekörner)', ^h-ba/f
(vd. 7 
=== leaf 291 (p 270 ) ===
- 270 —
(Metrum : Hezej).
bedl7i suhräue ddd du hersr-endes
du pänsed be/te-yt ferhe hvdervH
Hekim Nizäri QuhistänT.
48. batvrak Biber, siehe oben No. 181.
49. bes *Leid, Unheil* (Men.), hesitan, hns{i)sn, beSttar (aw.
dvaesäo 'Peiniger y. 43, 11).
aw. [/dvaes-, tbaes- peinigen', dvaesah-^ tbaesah-
II. s.w.; ai. [/^dves-, dvesti 'abgeneigt sein, hassen etc.*,
dvesas' u. s. w.
50. böjln 'Melone' (das -ä in böjtnä ist aramäischen Ur-
sprungs).
Vergl. unter np. xerbuze (oben No. 474) und de
Lagarde, Semitica I, 52.
51. böitan erlösen, retten, befreien', Praes. böjet; höj(i)sn
(päz. böz°), böjmUan etc.
ap. N. pr. Ka(m)büjti/a- ; aw. \/baoj- ablegen, weg-
tun, retten', bii/ti- ^Befreiung, Rettung
```


## [2026-09-14T02:31:34.348Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(284,290):\n    print('=== leaf',i,'(p',i-21,') ===')\n    print(leaves[i][:500])\nEOF"
}
```


### [2026-09-14T02:31:35.565Z] TOOL RESULT

```
=== leaf 284 (p 263 ) ===
A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos*, a/^ar(i)sn *das Nichtessen , aguftar 'nicht
sprechend' u. v. m.
ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
ai. a-, an-; arm. aw- (H. No. 20).
oss. d. t. «-, ä- (1).
Das Neupersische hat a-, an- aufgegeben (Fälle wie
näb, oben No. 1015, und nägäh, oben No. 1021, sind ver-
einzelt) und ersetzt dieses Praefix durch vorgesetztes
nä' (oben No. 1014) , z. B. phlv. anspä$ 'undankbar
gegenüber np. näsipüs, oder dur
=== leaf 285 (p 264 ) ===
- 264 —
4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
(i)sn.
Scheint ein Causativuni mit der gewöhnlichen phlv.
Endung -imtan (np. dagegen -ämdeN) zu sein. Bar-
tholomae denkt dagegen nach briefl. Mitteilung an
Zusammenhang mit aw. hisidyät etc. (vergl. oben
No. 922).
5. agräl, agre Vortrefflich' (AW.-Komm., Bund.).
aw. ayrya' Vorzüglich ; ai. agriyd",
6. ahöklnltan Verunreinigen, beschmutzen', ähökinttär
(aw. ähitl', vd. 20, 14), ahökm{i)sn (aw. ähiti-) ^).
Nur ähö (Reim: Vis und Rämin,
=== leaf 286 (p 265 ) ===
- 265 -
12. anaiv nicht arisch; boshaft, feindlich*, anainh (Men.).
aw. miairya-,
np. ener schlechter Charakter ist unbelegt (die laut-
gesetzliche Form müsste nEr lauten), die Riväyets
haben arier als ^ungehorsam'.
13. anäklh 'Unheil etc.'
Das sehr häufige Wort ist aufgegeben; das seltene
anäk (AV.) hat sich dagegen im np. näk erhalten
(s. oben No. 1020*»»»).
14. andarvnl Atmosphäre, Luftraum .
aw. *aütarevat/u-; ai. *antarc(lyU',
Im Neupersischen soll endervä {endenväl 'Bedürfniss*
vergl. unte
=== leaf 287 (p 266 ) ===
— 266 —
18. aniifnal ^Kleinvieh*.
aw. anumaya- 'Kleinvieh'. Wohl nur Transcription
des Awestawortes.
19. apavTk 'später, anderer, übrig; der Rest' (päz. aware),
ap. aparam nachher ; aw. apara-, ai. äpara- 'hinterer,
späterer.
20. apastän Vertrauen , sehr häufig auf Gemmen ; arm.
LW. apastan,
skr. upasthäna- 'das Aufwarten, Verehren'.
20***** ajnsfnan nicht sehend, blindlings', nur vd. 13 (145),
aber wegen des Suffixes vielleicht nicht nur um-
schreibend.
aw. apisman- (yt. 10, 105), apisma,;r''ar
=== leaf 288 (p 267 ) ===
— 267 —
27. äsn natürlich, eigen (AW.-Komm., Mön.).
aw. asna- angeboren, natürlich, eigen* (Geld n er,
KZ. 24, 131/2).
28. aspastän 'Pferdestall'; arm. LW. aspastan.
aw. aspöMäna- Pferdestall'; skr. agvasthamt'.
Vergl. auch phlv. tistrastän 'Kameelstall*, göstän
'Kuhstair.
29. dHpräs 'Pferdeweg, Rennbahn .
Im PehlevT häufig, vergl. arm. LW. aspares, as-
parBz (?).
30. äsrük 'Priester, dsrühlh, päz. äsrm.
aw. dtiraoan-; ai. dtharvan-.
V
Np. vergl. (itörbän der Wörterbücher (im Sähnäme
I, 24 Vers 
=== leaf 289 (p 268 ) ===
— 268 —
schon durch die Lesung asta- hinfällig ; aber auch die
Bedeutung ^Gesandter, Bote' kam seinem asta- nicht zu.
Bartholomae's schöne Gleichsetzung von aw. asti-
mit ai. dtithi- (BB. 15, 10) hat, beiläufig bemerkt,
Jackson, Ayesta Grammar § 794 angenommen.
85. aMr 'Dolch, Schlachtmesser (des Priesters), Pferde-
stacher.
aw. asträ' ^) ; ai. asträ- Stachel zum Antreiben des
Viehs*.
36. äturastnr *Asche' (z. B. vd. 5 (148) für aw. atrya-).
Über das np. dialektische hül^ hol, /id (Vullers)
'Asc
```


## [2026-09-14T02:31:44.446Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB snehr/snaez ===\"; grep -n -i \"snehr\\|snexr\\|snaez\\|snaeg-\" HUB.txt | head; echo \"=== BQT/MON سنهر ===\"; grep -n \"سنهر\" BQT_v1_pages.txt BQT_v2_pages.txt MON_part1.txt MON_part2.txt 2>/dev/null | head; echo \"=== CHEUNG snaiz ===\"; ls | grep -i cheu"
}
```


### [2026-09-14T02:31:44.544Z] TOOL RESULT

```
=== HUB snehr/snaez ===
=== BQT/MON سنهر ===
BQT_v2_pages.txt:20343:   ‫سنهراردن ‪ -‬آنکا هکه سی‌سال ازعمراو گذشته بود ‪ -‬غل همد داد و روح القدی بات کبوتری‬
=== CHEUNG snaiz ===
CHEUNG.txt
```


## [2026-09-14T02:31:46.176Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC sneigwh/sneudh ===\"; grep -n \"sneig\\|sneudh\\|snoig\" IEC.txt | head -10; echo \"=== SYN snow ===\"; grep -n \"1\\.78\\|snaiws\\|sniegas\" SYN.txt | head -10"
}
```


### [2026-09-14T02:31:46.276Z] TOOL RESULT

```
=== IEC sneigwh/sneudh ===
16549:sneigó, ið 'creep, crawl; reach out; steal forth' OE snican, sv. 1. ‘creep, crawl’; ON sníkja, v. ‘hanker after’; (mod. “beg, scrounge’); cf. sníkjur, fpl. 'scrounging'; Late sniedzu, sniegt, v. ‘reach out, range; suffice’
16550:sneiguh- ‘snow’. Cf. snoiguh-, sniguh-. WP IL, 695 OHG, OE sniwan, v. id.; MHG sniē, sf. d: OLi. sniegti, 3s. id.; Latv. snieg, id.
16560:(sneudh-?, snoidh-? ‘cloud, mist’, etc. See Supt: S)
16566:sneu- — snoiguhos
16579:sniguh- (sninguh-) ‘snow’. Cf. sneiguh-, snoiguh-. WP II, 695 Skt. cf. snih, f. *moisture'; snihyati, 3s. “gets oily, moist; Gk. cf. nípha, acc. f. ‘snow’; niphei, 3s. ‘snows’; OLat. ninguit, nivit, Lat. ningit, 3s. id. beside nix, gs: nívis, f. ‘snow’; Olr. snige, Ir. snighe, m. ‘drip, shower’; sni- gim, snighim, v. id. beside Ir. sneachta, m. ‘snow’; OHG and OE sniwan, v. id., MHG snie, sf. ‘snow, -storm’; ON snjófa, v. id.; snifinn, adj. ‘snowed under’; Li. cf. sniñga, 3s. ‘snows’ beside OLi. (e-gde) sniegti, 3s. id. and Li. snygurioti, inf. ‘flurry — as snow’; Latv. cf. snigt, 3sg: snieg ‘to snow; it snows’
16582:(snoidh-, possible reconstruction as alterna- tive to type sneudh-. See Supt: S)
16583:snoiguhos ‘snow’ (Skt: *grease"). Cf. sniguh- Skt. snehah, m. ‘grease’; Av. cf. snaezetiti, 3pl! “it snows’; Go. snaiws, m. OHG sneo, snio; OE snàw, m. ‘snow’; OCS & com. SI.
=== SYN snow ===
1652:ME, NE sky, orig. ‘cloud’ (both senses in ME), fr. Norse, ON sky, Dan. sky ‘cloud’, Sw. sky ‘cloud’ and ‘sky’ (1.78).
1844:4. It. lo scuro, oscurita, Fr. obscurité, fr. Lat. obscurus ‘dark’: OF scuwa ‘shade’, scéo ‘cloud’, etc. (1.63, 1.78), Skt. sku- ‘cover’. Walde-P. 2.546 fi. Ernout-M. 694.
2005:Grk.  xidy (vida poet.) Goth. snaiws Lith. snie, NG xtdve ON 8n@r (snjor, snjar) Lett. shee Lat. nix Dan.  sne ChSl.  snégit It. neve Sw. snd SCr.  snijeg Fy. neige OE snaw Boh. snth Sp. nieve ME snow Pol. — fnieg Rum. zdpadé NE snow Russ. sneg Ir. snechte Du. Sneeuw Skt. hima- Nir. sneachta OHG  snéo Ay. vafra- W. etra (nyf) MHG nz ;
2016:Grk. vi¢a ace. sg. (poet.), with vb. yelder; Lat. nix, nivis, with vb. ningutt, It. neve, OF r. noif, Fr. neige (fr. neiger, *niviare. RIEW 5934), Sp. nieve, Rum. mea (dial.); Ir. snechte (but snigid ‘it rains’), NIr. sneachta, W. nyf (obs.); Goth. snaiws, OE sndw, etc. general Gmce.; Lith. sniegas, ChSl. snégi, etc., general Balto-Slavic; Av. snaég- only in vb., pres. snaéza- (but Pahl. sb. snéhr ‘snow’, Horn 292); here prob., but with
2044:1.78 WEATHER
3566:1. IE *daiwer-, root connection dub. Walde-P. 1.767. Ernout-M. 541. Walde- H, 1.787 f.
4142:1, Ir. dam, NIy. damh : Skt. damya- ‘to be tamed’, ‘young bull’, Grk. danédns ‘young ox, steer’, dauadts ‘young cow, heifer’, Skt. dam-, Grk. dauynur, Goth, gatamjan, etc. ‘tame’. Walde-P. 1.789,
4193:Ir. cit, cetnatt ‘sheep’ or lamb’ : Arm. ona ‘wether’, o&tar ‘sheep’, NIcel. hyeda sheep, sheepshead’. Walde-P. 1.384. Pedersen 1.120. Johannesson, KZ CE fed: Br. danvad: Ir. dam ‘ox’, Grk, dazadns ‘young 0x’, Skt. damya- ‘to be tamed, young bull’, Skt. dam, Grk. Sauvnue ‘tame’, etc., orig. ‘tamed animal’ specialized in different ways. Walde-P. 1.789. Pedersen 1.132.
4545:6. Lith. arklys, deriv. of arklas ‘plow’, this fr. the root of arti ‘plow’ : Grk. apéw, Lat. ardre ‘plow’, etc., hence orig. ‘plow horse’. Walde-P. 1.78.
4832:Note on ‘bitch’. Of the preceding words, Grk. xtwy, Lat. canis, and some- times others were used of the male and female dog, without distinction except as shown by the gender of the agreeing word. But for the female ‘bitch’ there are usually special terms. Some of these are simply new fem. forms of words for ‘dog’, as NG oxida, VLat. *cania (> It. cagna, MIr. caigne, Fr. chienne), Sp. perra, Br. kiez, Sw. hynda, NHG hiindin, Skt. ¢uni-, also SCr. kuéka (fr. kuéak, a less common word for ‘dog’, based on a calling cry. Berneker 636f.). Many more are quite unrelated. Rum. catea, fr. Lat. catella ‘female puppy’ (REW 1763). ON bikkja, Norw. bikje, Sw. dial. bicka, OF bicce, ME bicche, NE bitch, etym. dub., perh. : Skt. bhaga- ‘cunnus’ (Walde-P. 2.148. Falk-Torp 72). OE life, Du. teef, MLG teve (> Dan. teve) etym. dub. (Falk-Torp. 1313. Franck— v. W. 690). OHG zoha, MHG zohe, NHG dial. zope, zauche, perh. as orig. ‘bearer’ : OHG ziohan ‘draw, nourish’ (Walde-P. 1.781. Falk-Torp. 1297). Lith. kale: Ir. cuilén ‘puppy’, ete. (3.612). Among others, either of imi- tative orig. or obscure, are Fr. lice (now obs. or dial.), Br. gart, ON tik, Norw., Sw. dial. tk, Lett. kun’a, Boh. cubka, Pol., Russ. suka (see above, 1).
```


## [2026-09-14T02:31:55.635Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(f,pat):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.find(pat)\n    return (t[:i].count('\\f') if i>=0 else None)\nprint('SYN snaez leaf',leafof('SYN.txt',\"Av. snaég- only in vb.\"))\nprint('SYN 1.78 leaf',leafof('SYN.txt',\"1.78 WEATHER\"))\nprint('IEC sneiguh leaf',leafof('IEC.txt',\"sneiguh- ‘snow’\"))\nprint('IEC snoiguhos leaf',leafof('IEC.txt',\"snoiguhos ‘snow’\"))\nprint('IEC sneudh leaf',leafof('IEC.txt',\"(sneudh-?, snoidh-?\"))\nEOF"
}
```


### [2026-09-14T02:31:56.903Z] TOOL RESULT

```
SYN snaez leaf 97
SYN 1.78 leaf 98
IEC sneiguh leaf 681
IEC snoiguhos leaf 682
IEC sneudh leaf 681
```


## [2026-09-14T02:32:02.572Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T02:32:02.578Z] TOOL RESULT

```


```


## [2026-09-14T02:32:05.384Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneygʷʰ-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Iranian, Avestan, Germanic, Latin, Greek). Also any notes on the root shape."
}
```


## [2026-09-14T02:32:06.476Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/snaiwaz",
 "prompt": "Give the reconstruction, meaning, etymology (PIE source) and descendants including Old English snaw > English snow."
}
```


### [2026-09-14T02:32:12.088Z] TOOL RESULT

```
# Proto-Indo-European *sneygʷʰ- Root

**Reconstruction:** *sneygʷʰ-

**Meaning:** "to snow"

**Root Shape:** This is a CReRC-shaped root (consonant-resonant-consonant pattern).

## Descendants

The page lists descendants across several language families:

- **Iranian/Indo-Aryan:** Sanskrit स्निह् (snih), though its meaning shifted to "to stick, remain; sticky fluid"
- **Latin:** ningit/ninguit (via Proto-Italic *sningʷet)
- **Celtic:** Proto-Celtic *snigʷyeti and descendants
- **Balto-Slavic:** Lithuanian, Latvian, Latgalian forms (snigt/snigti)
- **Tocharian B:** śiñcatstse* (adjectival derivative meaning "snowy")

**Note on root semantics:** "The original meaning of the root was 'to stick, remain', with semantic shift to 'snow'" was proposed by Karl Hoffmann in 1965, but this interpretation is disputed. Most daughter languages point to "to snow" as the primary meaning, with Sanskrit's "sticky" sense likely being secondary or slang-derived.
```


### [2026-09-14T02:32:12.128Z] TOOL RESULT

```
# Proto-Germanic *snaiwaz

**Reconstruction:** *snaiwaz (masculine a-stem noun)

**Meaning:** "snow"

**Etymology:** The term derives from earlier *snaygʷaz, ultimately from Proto-Indo-European "*snóygʷʰos" (snow).

**Key Descendants:**

- **Old English:** snāw → **English:** snow
- **Old Norse:** snjór → **Icelandic:** snjór; **Swedish:** snö; **Danish:** sne
- **Old High German:** snēo → **German:** Schnee
- **Old Dutch:** snēo → **Dutch:** sneeuw
- **Gothic:** snaiws

The word spread throughout Germanic languages with consistent phonetic development, producing modern terms like German "Schnee," Dutch "sneeuw," and Scandinavian variants. The reflexes demonstrate the regular sound changes from Proto-Germanic through each language family's evolution.
```


## [2026-09-14T02:32:14.766Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nuance",
 "prompt": "Full etymology of nuance: French, nuer, nue, Vulgar Latin *nuba, Latin nubes, PIE root. Dates."
}
```


## [2026-09-14T02:32:16.246Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nubes",
 "prompt": "Latin nubes: etymology, PIE reconstruction, cognates (Avestan snaoda, Welsh nudd), and any note from de Vaan."
}
```


### [2026-09-14T02:32:19.576Z] TOOL RESULT

```
# Etymology of Nuance

The word **nuance** entered English in 1781 from French *nuance*, meaning "slight difference, shade of color." The French term derives from *nuer* ("to shade"), which comes from *nue* ("cloud").

## Historical Language Path

Tracing backward, *nue* originates from Vulgar Latin *nuba*, which developed from Latin *nubes* meaning "a cloud, mist, vapor." This ultimately connects to the Proto-Indo-European root *sneudh-*, signifying "fog."

## Semantic Evolution

According to etymological sources, the French secondary sense referenced "the different colors of the clouds." By 1852, English adopted the meaning relating to "a slight variation in shade" of colors or tones. Musical applications appeared by 1841.

The verb form emerged later in 1886, meaning "to give nuances to," while the adjective **nuanced** appeared in 1896, describing something with "delicate gradations in tone."
```


### [2026-09-14T02:32:21.919Z] TOOL RESULT

```
# Latin *nubes*: Etymology and Cognates

**Etymology**: The word derives from Proto-Italic *\*nouðetis*, which comes from Proto-Indo-European *\*(s)newdʰ-e-ti-s*, rooted in *\*(s)newdʰ-* meaning "to cover."

**Cognates**: The entry lists several related words:
- Welsh *nudd* ("haze")
- Avestan *snaoδa* ("clouds")
- Baluchi *nod* ("raincloud")

**De Vaan's Note**: According to Michiel de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008), the word has this Proto-Indo-European foundation, though "despite similar pronunciation and semantics, not related to *nebula*" ("mist, fog").

The entry documents seven primary meanings for *nubes*: cloud, swarm, phantom, cloudiness, concealment, storm-cloud (figuratively), and bad luck/misfortune.
```


## [2026-09-14T02:32:27.459Z] TOOL CALL #45: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg462.png data/verification/sources/refs/ocr/BOOK/462.png && ls -la data/verification/sources/refs/ocr/BOOK/462.png"
}
```


### [2026-09-14T02:32:27.536Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60489 Sep 13 22:32 data/verification/sources/refs/ocr/BOOK/462.png
```


## [2026-09-14T02:32:31.058Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneygʷʰ-' --note 'page 462, root Sneigwh: PIE root form and descendants' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/snaiwaz' --note 'page 462, node Germanic snaiwaz > OE snaw > English snow'; python3 tools/fetch_source.py 'https://www.etymonline.com/word/nuance' --note 'page 462, root Sneudh: French nuance < nuer < nue < L nubes'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/nubes' --note 'page 462, node Latin nubes < PIE *(s)neudh-, cognate Av. snaoda'"
}
```


### [2026-09-14T02:32:33.707Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b128ca2bf6f446e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/912ca2d687217ba9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbf4e76f110a43d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51fde19d48b0381c.txt
```


## [2026-09-14T02:32:40.394Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG snaiz ===\"; grep -n -i \"snaiz\\|snaēž\\|snaez\\|snaiž\" CHEUNG.txt | head -10; echo \"=== SKT snow/nuance ===\"; grep -n \"SNOW\\|Snow, sb\\|nuance\" SKT.txt | head -10"
}
```


### [2026-09-14T02:32:40.467Z] TOOL RESULT

```
=== CHEUNG snaiz ===
22820:is unwilling though to consider snaeZ- as a ja-pres. stem (p. 130) on account of the 
22824:Pres. them.: IND. med. 3pl. YAv. snaeZintae? (Yt 5.120), SUBJ. 3sg. YAv. snaézat (V 2.22); Partic.: pres. 
=== SKT snow/nuance ===
19708:Tlor,  a  rank,  row.  (F.  —  Teut.l  For- merly  /ire,  a  better  spelling ;  Florio  ex- plains Ilal.  tiro  bv  *  a  ryn  of  ordinance.'  -> r .  tirt,  '  a  draught,  pull,  .  ,  ahso  a  tire ;  a stroke,  hit.  reach,  gate,  course,  or  con- tinuance of  a  course;'  Cot  [Cf.  Span. tira,  a  set  of  mnles ;  ItaL  tiro,  '  a  shoot, !>hot,  tire,  reach,  .  .  a  stones  caste,  a fyrt  of  ordinance  ;'  Florio  (1598).]  — F, ttrer,  to  draw,  drag,  pull.  &c.  The orig.  sense  was  to  tear  or  pull  violently ; from  the  verb  appearing  Oi*  Goth,  tairan, E.  tear;  see  Tear  (0.  ^1  f>"d  no  evi- dence for  connecting  it  with  O.  F.  tiere,  .i low,  rajik,  though  there  may  have  been some  confusion;  the  A.S.  tt^r,  occurring but  once,  is  an  obscure  and  doubtful  woid* and  has  nothmg  to  do  with  it,  that  I  can  see. retire.  (F.-Tcut.)  O.  F.  rttirer,  'to retire,  withdraw;'  Cot.  —  F.  rr,  back; tirer,  to  poll ;  see  Tier  (above).
```


## [2026-09-14T02:32:42.178Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22800,22835p' CHEUNG.txt"
}
```


### [2026-09-14T02:32:42.236Z] TOOL RESULT

```
*SANSKRIT: ѕпа ‘to bathe, to wash’ (RV+) = EWAia П: 769 

«PIE *(s)neH>- ‘to wash, swim’ = LIV: 572 f. | Pok.: 971 f. 

*IE COGNATES: Lat. nare ‘to swim’, Lat. natare ‘to swim, to drip’, Olrish snaid, -snä 
‘swims’, Toch. B näsk- ‘to bathe’, Olrish snam ‘the swimming’ 


*sna0H 349 


*REFERENCES: IIFL I: 288a; IFL II: 276a, 551a, 264b Ё; Andreev — Реёќегеуа: 321b f.; EVS: 108b; 
Abaev, Slovar’ II: 152, 150; Abaev, Slovar' I: 111 f.; DKS: 351a, 466b; Werba 1997: 328 f.; Abaev, Slo- 
var’ IV: 239 f.; Paul 1998: 291b; Steblin-Kamenskij 1999: 404; Cheung 2002: 157; Korn 2005: 178, 348 


*snaij ‘to snow’ 

*AVESTAN: Y Av. ѕпаё2- ‘to snow’. 0 On *ji> Av. Z see Martínez 1999: 127 ff., who 
is unwilling though to consider snaeZ- as a ja-pres. stem (p. 130) on account of the 
full grade -aé-. Perhaps, the Av. sna&Z- is a blend of a them. stem *sna&ja- and 
Ja-stem *sniZa- (= Skt. snihya-) ? = Liste: 65 

Pres. them.: IND. med. 3pl. YAv. snaeZintae? (Yt 5.120), SUBJ. 3sg. YAv. snaézat (V 2.22); Partic.: pres. 
YAv. snaéZint- (Yt 16.9, V 6.36, V 8.4) 


*SOGDIAN: MSogd. snys ‘to snow’ 
Pres.: PREC. 150. MSogd. Snystw ‘may I snow’ 


*NEIR: Sh. (Baj.) Zinij (m.), Rosh. Zinij, Bart. ZiniZ ‘snow’ (with sib. assimilation) 
*SANSKRIT: sneh ‘to stick, remain [? RV, Kath.]; to (overwhelm with) snow [? RV]’ 
|| Pkt. sineha (m.), sinha (Ё) ‘snow, fog’. Ф The Skt. meaning ‘to stick, remain’ can 
hardly reflect the IE original meaning, as proposed in Hoffmann 1965: 24 and
```


## [2026-09-14T02:32:49.660Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22835,22860p' CHEUNG.txt"
}
```


### [2026-09-14T02:32:49.727Z] TOOL RESULT

```
hardly reflect the IE original meaning, as proposed in Hoffmann 1965: 24 and 
assigned accordingly in LIV: l.c. All IE cognates point to ‘to snow’. The Skt. 
meaning ‘to stick, remain’ of sneh should therefore be considered secondarily: Hoff- 
mann’s alternative explanation that this meaning may have coexisted with ‘to snow’ 
is not convincing. The Skt. ‘snow’ forms have probably acquired the (slang ?) mean- 
ing(s) ‘to stick, remain; sticky fluid, sim.’ perhaps from whiteish bodily fluids which 
are compared to snow, notably snot and spit ? Another argument for the older mean- 
ing ‘to snow’ is perhaps found in RV 9.97.54 sneháyati (caus. pres. 3sg.), which 
Jamison 1983: 91 translates as ‘overwhelms with snow, destroys’. = EWAia П: 772 
«PIE *sneig""- ‘to snow’ = LIV: 573 | Pok.: 974 

*IE COGNATES: Gr. veiget ‘it is snowing’, Gr. viga (Asg. f.) ‘falling snow’, Lat. 
ninguit, Lith. sniéga ‘it is snowing’, Lat. nix (f£), OCS snégs, Latv. sniegs, Goth. 
snaiws, Engl. (to) snow, etc. 

*REFERENCES: EVS: 110b; Werba 1997: 261 


*sna0H ‘to strike’ 
*AVESTAN: Y Av. sna0- ‘to strike’ = Liste: 65 
Pres. them.: IND. 3pl. (partic. pres. f. ?) YAv. sna0onti (FrW 8.2), INJ. 3sg. YAv. snadat (V 7.52C) 


*MIDDLE PERSIAN: BMP sn’h /snah/ ‘blow, strike, violence’ 

*SANSKRIT: snath' ‘to push (down), strike (down), pierce’ (КУ) > EWAia II: 659
```


## [2026-09-14T02:32:58.566Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['SKT.txt','FSD_vol3.txt','WEB_vol1.txt']:\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,e); continue\n    for pat in ['Snow,','snow,  sb','Nuance','nuance,']:\n        for m in list(re.finditer(pat,t))[:2]:\n            print('###',f,pat,'leaf',t[:m.start()].count('\\f'))\n            print(t[m.start()-100:m.start()+400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:33:00.054Z] TOOL RESULT

```
### FSD_vol3.txt nuance, leaf 361
iamond pen'den-cyt 1 pen'den-si. 2 pfln'dfin-cy. n 1. The state of pending or being undecided, continuance, as, during pendency of a suit 2. The state of hanging down or being pendent Pen-den'nis, 1 pen-den'is. ? ptn-d^n'ts, a In Thackeray's novel The HUtary of Pendennts. hU Fortunes and Misfor^ tunes, the surname of live hero, Arthur, and of his uncle, a major The story treats of the life of Arthur, a vain and aelQsli ty|M9, who In early youth Is spoiled by an liidulgont mother and an adopted s
### WEB_vol1.txt nuance, leaf 278
hould be of the same nationality as the ey of his flock. Other measures were suggested for the continuance, among t various races represented in the United States, of the use of their mother tongues, and for the preservation of their national tradi- tions. ca-hiér’ (or kä-yā’), n. [Fr. cahier, OFr. caier, qua qi It. quaderno; LL. quaternus, four each. 1. a book of loose leaves held together; notebook. 2. a report of the proceedings of any body, as a legislature. cå-hiñ’cá root, the root of a shr
### WEB_vol1.txt nuance, leaf 311
ts divided a play into the protasis, epitasis, catastasis, and catastrophe—the introduction, con- tinuance, heightening, and development or conclusion. 2. a disastrous overthrow or ruin. 3. any great and sudden calamity, disaster, or misfortune. 4. any event that disturbs or overthrows the existing order of things. 5. in geology, a cataclysm. cat-a-stroph’ic, a. pertaining to a catastrophe; disastrous; calamitous, ca-tas/tro-phism, n. the theory that geologi- cal changes are the result of sudden
```


## [2026-09-14T02:33:29.643Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"sneig'Ah-\",\"snendh-\",\"sneu6y-2\",\"snaoda-\",\"Neber\"]:\n    i=t.find(pat)\n    print(pat, 'leaf0=', t[:i].count('\\f') if i>=0 else None)\n# find the sneudh entry in POK_03\nimport re\nfor m in re.finditer(r'snaoSa|snaoda|snao',t):\n    print(m.start(), t[:m.start()].count('\\f'), t[m.start()-120:m.start()+200].replace('\\n',' '))\n    break\nEOF"
}
```


### [2026-09-14T02:33:30.766Z] TOOL RESULT

```
sneig'Ah- leaf0= 214
snendh- leaf0= None
sneu6y-2 leaf0= None
snaoda- leaf0= 219
Neber leaf0= None
327209 122 n, verschwinden',  sly.  pazdayeiti  ^verscheucht  (macht  weggehen*),  av. apa-had'  ,sich  wegsetzen,  ausweichen*,  äsnaoiti  {*ö-zd-neu-ti)  ,geht  heran' (s.  886  äsna-)]  gr.  bdog  ,Weg',  ödiTTjg  , Wanderer',  oösvo)  , wandere';  aksl. chodz  ,Gang',  choditi  , gehen',  ablaut.  hdh  ^gegangen';  slav.  ch-
```


## [2026-09-14T02:33:39.100Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nfor i in (214,219):\n    s=L[i]\n    import re\n    print('=== leaf',i,'nums:',re.findall(r'\\b9[5-9]\\d\\b',s)[:8])\nfor i in (214,):\n    print(L[i][:60])\n    j=L[214].find(\"sneig'Ah-\")\n    print(L[214][j-300:j+500])\nj=L[219].find(\"snaoda-\")\nprint('--- 219 ---'); print(L[219][j-500:j+500])\nEOF"
}
```


### [2026-09-14T02:33:40.255Z] TOOL RESULT

```
=== leaf 214 nums: ['974']
=== leaf 219 nums: ['979']
 vfj  ,spinnt'  (*avi^isL',  evvr]  ,nebat',  ivvvriTog  ,gu
l,  flink',  reduktion^. stufig  sngfurligr  , rasch';  s-lose  Nebenformen  aschw.  ri^ver  und  never^  aisl nefr  (neutr.  7wfrt)  ,rasch,  flink*  (dazu  auch  mhd.,  nhd.  alem.  nuofer  ,mmiter frisch,  nüchtern*,  nhd.  bair.  nuober).
WP.  II  698.
sneig-  ,kriechen':  s.  unter  sneg-  ds.
sneig'Ah-  ,schneien,  (sich)  zusammen  ballen',  snig^h-,  snoig]iho-s  , Schnee*.
Präkrit.  sineha-  (=  ai.  sneha-)  , Schnee^;  av.  anae^a-  
--- 219 ---
```


## [2026-09-14T02:33:46.018Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nfor i in range(213,220):\n    s=L[i]\n    print('leaf',i,'nums',re.findall(r'\\b97[0-9]\\b',s)[:4],'| sneud hits:',[m.start() for m in re.finditer(r'sneu[dö6]',s)][:5])\ns=L[216]\nfor m in re.finditer(r'sneu[dö6]',s):\n    print(s[max(0,m.start()-150):m.start()+600].replace('\\n',' ')); break\nEOF"
}
```


### [2026-09-14T02:33:47.130Z] TOOL RESULT

```
leaf 213 nums ['973'] | sneud hits: []
leaf 214 nums ['974'] | sneud hits: []
leaf 215 nums ['975'] | sneud hits: []
leaf 216 nums ['976'] | sneud hits: []
leaf 217 nums ['977'] | sneud hits: []
leaf 218 nums ['978'] | sneud hits: [2645, 2703]
leaf 219 nums ['979'] | sneud hits: [183, 770, 924]
```


## [2026-09-14T02:33:50.093Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nprint(L[218][2500:3400].replace('\\n',' '))\nprint('=== 219 ===')\nprint(L[219][:1200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:33:51.000Z] TOOL RESULT

```
h  Heirat  uad^ Weiterung  zu  sneu-  ,Fäden  zusammendrehen,  knüpfen*. WP.  II  697,  WH.  II  183  f.,  Trautmann  273,  Vasmer  2,  683. 1,  sneud{b)-  »schläfrig,  schlummern*;  vielleicht  zu  2.  sneudh-, Gr.  vvaTccl^ü)  , schlafe;  bin  schläfrig,  nachlässig',  vvoTaXog,  -Xiog rig';  lit.  sndudziUy  sndusti,  lett.  snaüzu  , schlummere',  lit.  snaudälius  z{ riger    Men
=== 219 ===
sch',    snaudulys   , Schlummer',    lett.    snaudule   ,  Schlaf  ratze*  ®^ snüstUj  snüdauj  snüsti  ,einschlummern',  snudäj  snüdis  ,Schläfer,  Träutatf*  - WP.  II  697. 2.  sneudh-  , Nebel;  neblig,  düster';  snoudho-  ,NebeF. Av.  snaoda-  , Gewölk',  südbaluci  nöd  ,leichtes  Gewölk,  Nebel,  Regj wölke*;  gr.  vv&öv  ^qtwvov.  oy.oxslv6v,  wd^wdsg'  a^iOTeivoJösg  Kes.]  lat ,Wolke',  dazu  ohnübö,  -ere  ,verhüllen'  (durchs  Perf.  obnühl  auch  fa von  nübö,  nupsl  ,heiraten*  scharf  geschieden),  u.  zw.  wohl  als  denomliii. tives  Verbum :  ,(sich)  bewölken'  =  ,(sich)  bedecken*,  zunächst  vom  HimmiL dann  allgemein;  cymr.  nudd  ,Nebel'  (zum  GN  Nudd  s.  oben  S.  768) ;Xi möglicherweise  ursprüngl.  als  ,Feuchtigkeit'  =  *sneudh-  der  Erwelt#i rung  von  sneu-  neben  snäu-  und  snä-  (s.  dort)  »fließen* ;  als  ^benebelt,  däma^ rig  =  schläfrig*  vielleicht  zu  1.  sneud(hy. WP.  II  697,  WH.  II  183  f. snusös  f.  o-Stamm  , Schwiegertochter*. Ai.  snusd  ds.  (nach  den  Fem.  auf  a-  umgebildet);  arm.  nw,  Gen.  nu^ ds.,  gr.  j/v(5g  ds.;  lat.  nurus,  -üs  ds.  (nach  socrus  umgebildet);  ahd.  mW, snoraj  ags.  snoru,  ais
```


## [2026-09-14T02:33:56.492Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T02:33:56.542Z] TOOL RESULT

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


## [2026-09-14T02:38:12.906Z] TOOL CALL #56: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-462.json",
 "content": "{\n  \"pdf_page\": 462,\n  \"book_page\": 432,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sneigwh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sneygʷʰ- 'to snow', noun *snóygʷʰ-o-s 'snow'\",\n      \"note\": \"Pokorny p. 974 heads the entry 'sneigʷh- ‚schneien, (sich) zusammen ballen’, snigʷh-, snoigʷho-s ‚Schnee’'; Watkins/AHD 1985 has 'sneigʷh-. Snow; to snow', i.e. exactly Nourai's gloss, with the same Pokorny page. The language label 'Indo-European' and the citation form Sneigwh (= sneigʷh-) are both right. Cheung 2007 s.v. *snaij and Wiktionary write the root *sneygʷʰ- in the newer laryngeal-free notation; nothing substantive differs. The only quibble on the whole chart is the initial š- of the Sogdian form (node #3), which is Nourai's own misprint.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sneygʷʰ- «برف باریدن» و نام‌واژهٔ آن *snóygʷʰ-os «برف» است. پوکورنی در صفحهٔ ۹۷۴ همین ریشه را با همین معنا آورده و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) نیز آن را «snow; to snow» معنا کرده است؛ پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. تنها ایرادِ این نمودار، ش‌آغازِ صورت سغدی (گرهٔ ۳) است که خطای چاپی خودِ کتاب است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneyg%CA%B7%CA%B0-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:974\",\n          \"status\": \"supports\",\n          \"note\": \"POK_03.txt leaf 214 (printed p. 974, the page number 974 is on that leaf): 'sneig'ʷh- ‚schneien, (sich) zusammen ballen’, snigʷh-, snoigʷho-s ‚Schnee’. Präkrit. sineha- (= ai. sneha-) ‚Schnee’; av. snaeža- …'. POK_full.txt 'Root / lemma: sneig^h- … Page(s): 974' repeats it. Exactly Nourai's root and gloss.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 695\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd2_pages.txt: 'sneig^h- ‚schneien“, snig^h-, snoig^hos ‚Schnee“. Av. snaeženti (ciyąn) ‚an einem schneienden Tage“, snaežat (Konj.) ‚wird schneien“, gr. νίφα …' — the Walde–Pokorny source of POK 974.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sneigʷh-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 972: 'sneigʷh-. Snow; to snow. 1. Suffixed o-grade form *snoigʷh-o- in Germanic *snaiwaz in Old English snāw, snow: SNOW. 2. Zero-grade form *snigʷh- in Latin nix … [Pok. sneigʷh- 974.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. sneiguh- / snoiguhos (leaf 681-682 ≈ pp. 1332-1334)\",\n          \"stance\": \"supports\",\n          \"note\": \"IEC.txt: 'sneiguh- ‘snow’. Cf. snoiguh-, sniguh-. WP II, 695' and 'snoiguhos ‘snow’ … Av. cf. snaezeiti … Go. snaiws, OHG sneo, snio; OE snāw, m. ‘snow’'.\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"p. 349 s.v. *snaij\",\n          \"stance\": \"supports\",\n          \"note\": \"CHEUNG.txt: '*snaij ‘to snow’ … «PIE *sneigʷ(h)- ‘to snow’ = LIV: 573 | Pok.: 974'. Cheung also rejects Hoffmann's ‘to stick’ as the original sense: 'All IE cognates point to “to snow”.'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 1.81 'snow', leaf 97 ≈ p. 73\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt: 'Goth. snaiws, OE snāw, etc. general Gmc.; Lith. sniegas, ChSl. sněgŭ … Av. snaēž- only in vb., pres. snaēža- (but Pahl. sb. snēhr ‘snow’, Horn 292)'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"snaěž, snaěj, snaěža\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan has only verbal forms of this root: Bartholomae's AirWb (col. ~1636) heads it 'j. snaēž- V. ‘schneien’ (persönl.), Praes. 2 snaēša', and cites snaēžiṇti (V. 8.4 'värəṇti vā snaēžinti vā'), snaēžāt (Konj., V. 2.22 'snaoδō vafra snaēžāt' = 'the cloud will snow snow-masses'), and the participle snaēžaintī- (Yt. 16.10). Nourai's three shapes are one and the same item in different notations: snaěž = the root snaēž-, snaěža = the thematic present stem snaēža-, and snaěj is simply an older Latin-letter transliteration (j for ž) of the same root, of the type Klein prints as 'Avestic snaezaiti'. Phonetically Av. snaēž- continues PIE *sneygʷʰ- with the regular Indo-Iranian palatalisation of the labiovelar *gʷʰ before the front-vowel diphthong *ey to *ǰʰ > Iranian ž (Cheung 2007: 349 discusses whether the stem is *snaiǰa- or a blend with a *ja-present *sniža-, cf. Skt. snihya-), and *ey > Av. aē. Hence Av. snaēž- 'to snow' beside Skt. snih-, Gk. neíphei, Lat. ninguit.\",\n          \"derivation_fa\": \"در اوستایی تنها صورت‌های فعلی این ریشه به‌جا مانده است: بارتولومه در «فرهنگ ایرانی باستان» (ستون ≈۱۶۳۶) مدخل را snaēž- «برف باریدن» آورده و صورت‌های snaēžinti (وندیداد ۸:۴)، snaēžāt (وندیداد ۲:۲۲) و صفت فاعلی snaēžaintī- (یشت ۱۶:۱۰) را گواه می‌گیرد. سه صورتی که نورایی نوشته در حقیقت یک واژه‌اند: snaěž ستاکِ ریشه، snaěža ستاک حال، و snaěj تنها آوانگاری کهن‌ترِ همان (j به‌جای ž) است؛ کلاین نیز به همین شیوه snaezaiti می‌نویسد. از نظر آوایی، gʷʰ هندواروپایی پیش از ey به ǰʰ هندوایرانی و سپس به ž ایرانی بدل شده و ey به aē اوستایی تبدیل شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sneyg%CA%B7%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:974\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 214 (p. 974): 'av. snaeža- ‚schneien’'; POK_full.txt s.v. sneig^h-: 'Avestan snaeza- ‘to snow’'. Exactly the node's word and gloss.\"\n            },\n            {\n              \"ref\": \"KLN:1466\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 778 (two printed pages per leaf, = pp. 1465/1466) s.v. 'snow, n.': '… fr. I.-E. base *snoigwhos, ‘snow’, resp. *sneigw-, ‘to snow’, whence also … Avestic snaezaiti … ‘it snows’'. Klein's 'snaezaiti' is Nourai's 'snaěj'-type spelling.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AirWb col. ~1636, leaf 886 of BRT.txt\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. snaēž- V. ‘schneien’ (persönl.). Praes. 2 snaēša … värəṇti vā snaēžinti vā … yahmai haca snaoδō vafra snaēžāt V. 2.22' and, crucially for node #2, the closing note 'ahd. sneiwit, lit. sniẽga; mp. vgl. snēx, snēxr'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 349 s.v. *snaij\",\n              \"stance\": \"supports\",\n              \"note\": \"'*snaij ‘to snow’. AVESTAN: Y Av. snaēž- ‘to snow’ … Pres. them.: IND. med. 3pl. YAv. snaēžinte (Yt 5.120), SUBJ. 3sg. YAv. snaēžāt (V 2.22); Partic.: pres. YAv. snaēžint- (Yt 16.9, V 6.36, V 8.4).'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 695\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. snaeženti (ciyąn) ‚an einem schneienden Tage“, snaežat (Konj.) ‚wird schneien“'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sněhr «سنهر»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is real and the etymology is right, but the language label is loose: snēhr is a Book-Pahlavi (Middle Persian) noun, not a New Persian one, and it is precisely for that reason that Nourai has to add '(obsolete)'. Horn, whom Nourai cites, prints it not in the New Persian body of the Grundriss (nos. 1-1106) but in the alphabetical Pahlavi appendix that begins on p. 263: HRN p. 292, appendix no. 181 'sñehr ‘Schnee’ (vd. 6 (74) u. ö., Men., AV.). aw. √snaēž-, snaēženti ‘es schneit’ …', with a footnote 'Oder sñexr …?'. MacKenzie's CPD reads the spelling ‹snyhl› as snēxr (beside snēžag 'snow' ‹snyck›), and Bartholomae already wrote 'mp. vgl. snēx, snēxr'; so the modern reading is snēxr, with -xr not -hr, and Nourai's Persian-script rendering «سنهر» follows Horn's older -h- reading. As to the arrow: MP snēxr is not a loan from Avestan but the Middle Persian reflex of the same Old Iranian stem *snaiž-/*snaixra- that Avestan attests only as a verb (Av. snaēž-); Nourai's Avestan→Persian arrow is his usual shorthand for 'the Persian word continues the Old Iranian form attested in Avestan'. The Pahlavi word did not survive into New Persian, where 'snow' is barf (< MP wafr, Av. vafra-).\",\n          \"derivation_fa\": \"واژه واقعی است و ریشه‌شناسی آن درست، اما برچسب زبانی دقیق نیست: snēxr/snēhr واژه‌ای فارسی میانه (پهلوی کتابی) است نه فارسی نو؛ به همین سبب نورایی ناچار شده «obsolete» بیفزاید. هرن آن را نه در بدنهٔ فارسی نوِ «Grundriss» بلکه در پیوستِ واژه‌های پهلوی (از صفحهٔ ۲۶۳) آورده است: صفحهٔ ۲۹۲، شمارهٔ ۱۸۱: «sñehr «برف» (وندیداد ۶(۷۴)، مینوی خرد، ارداویراف)؛ اوستایی √snaēž-». مکنزی در فرهنگ پهلوی خود نوشتار ‹snyhl› را snēxr می‌خواند (در کنار snēžag «برف») و بارتولومه نیز «mp. snēx, snēxr» نوشته است؛ پس خوانشِ امروزی snēxr با «خ» است و ضبط «سنهر» پیرو خوانش کهن‌ترِ هرن است. دربارهٔ پیکانِ نمودار: snēxr وام‌واژه‌ای از اوستایی نیست، بلکه بازماندهٔ همان ستاک ایرانی باستان *snaiž-/*snaixra- است که در اوستایی تنها به‌صورت فعل (snaēž-) دیده می‌شود. این واژه به فارسی نو نرسید و جای آن را «برف» (از فارسی میانهٔ wafr، اوستایی vafra-) گرفت. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:292\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt leaf 313 (printed p. 292, header '— 292 —'), Pahlavi-appendix no. 181: 'sñehr¹) ‘Schnee’ (vd. 6 (74) u. ö., Men., AV.). aw. √snaēž-, snaēženti ‘es schneit’; ksl. sněgŭ; lit. sniegas ‘Schnee’, snigti ‘schneien’; gr. νίφει; lat. nix, nivis; got. snaiws, ahd. sniuit ‘es schneit’, nhd. Schnee.' Footnote: 'Oder sñexr unter dem Einfluss von …?'. The page says exactly what the arrow says — but it is in Horn's Pahlavi glossary (which begins on p. 263, e.g. no. 42 'azg (d.i. azak) ‘Ziege’ (PPGl.)'), so the word is Middle Persian, not New Persian.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie CPD p. 76 s.v. snēxr\",\n              \"stance\": \"partial\",\n              \"note\": \"PHD_pages.txt: 'snēxr [snyhl] snow.' immediately followed by 'snēžag [snyck] snow.' and 'snōy [snwd] (rain-, snow-)cloud.' MacKenzie gives no New Persian continuation (contrast 'wafr [wpl | M wpr, N barf] snow'), confirming the word died with Middle Persian; and he reads -xr, not -hr.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AirWb col. ~1636 s.v. snaēž-\",\n              \"stance\": \"supports\",\n              \"note\": \"'ahd. sneiwit, lit. sniẽga; mp. vgl. snēx, snēxr (wozu Bthl. ZDMG. 50, 697)' — Bartholomae himself ties the Middle Persian noun to the Avestan verb, which is Nourai's arrow.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 1.81 'snow', leaf 97 ≈ p. 73\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. snaēž- only in vb., pres. snaēža- (but Pahl. sb. snēhr ‘snow’, Horn 292)' — Buck labels it Pahlavi and cites the same Horn page.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"grep 'سنهر' in BQT_v1_pages.txt / BQT_v2_pages.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry «سنهر»; the only hit is the unrelated string «سنهراردن» in a running text on BQT_v2_pages.txt line 20343. Borhān-e Qāṭeʿ does not know the word, as expected for a Pahlavi-only noun.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"grep 'سنهر' in MON_part1.txt / MON_part2.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"No hit; Moʿin's Farhang-e Fārsi has no headword «سنهر».\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"grep 'snehr|snexr|snaez' in HUB.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Hübschmann's Persische Studien does not treat the word (no hits).\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"šněš\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Sogdian verb is real and its derivation from this root is certain, but the citation form should begin with s-, not š-. Nourai's own source, Gharib's Sogdian Dictionary, gives it at exactly the cited page: no. 9312 'snyš- M | snēš ©Av. snaēža | (to) snow'. Cheung 2007: 349 s.v. *snaij likewise gives 'MSogd. snyš ‘to snow’' (the only š-initial shape is the precative snyštw 'may I snow', where the š is the stem's final consonant carried into the spelling, not an initial). Phonetically, Sogdian snēš- ‹snyš› continues Old Iranian *snaiža- with (a) the regular Sogdian raising of the Old Iranian diphthong *ai to ē, and (b) the regular Sogdian devoicing of final/preconsonantal *ž to š. The printed page 432 does show 'šněš' (see data/verification/sources/refs/ocr/BOOK/462.png), so the extraction is faithful and the stray š- is Nourai's own misprint.\",\n          \"derivation_fa\": \"فعل سغدی واقعی است و اشتقاق آن از این ریشه قطعی، اما صورت مدخلی باید با s- آغاز شود نه š-. خودِ منبعی که نورایی ارجاع داده — «فرهنگ سغدی» بدرالزمان قریب — در همان صفحه (شمارهٔ ۹۳۱۲) چنین دارد: «snyš- (M) snēš ©اوستایی snaēža — برف باریدن». چونگ (۲۰۰۷، ص ۳۴۹) نیز «MSogd. snyš» می‌نویسد. از نظر آوایی، snēš- سغدی بازماندهٔ *snaiža- ایرانی باستان است: دوگانه‌واکهٔ ai به ē سغدی بدل شده و ž پایانی به š بی‌واک شده است. صفحهٔ چاپی ۴۳۲ کتاب به‌روشنی «šněš» دارد (تصویر در data/verification/sources/refs/ocr/BOOK/462.png)، پس خطا از خوانش اسکن نیست بلکه خطای چاپی خودِ کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"šněš\",\n          \"correct_form\": \"snēš- (Sogd. ‹snyš›)\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:376\",\n              \"status\": \"partial\",\n              \"note\": \"SOD_pages.txt leaf 443-444 (printed p. 376; the preceding leaf carries the header '375'), entry 9312: 'snyš- M | snēš ©Av. snaēža | (to) snow | GMS 450, 452; 3sg. pres. …'. The page fully supports the derivation from the Avestan/Iranian root but spells the stem snēš-, not šnēš-; hence 'partial'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 349 s.v. *snaij\",\n              \"stance\": \"partial\",\n              \"note\": \"'*SOGDIAN: MSogd. snyš ‘to snow’. Pres.: PREC. 1sg. MSogd. šnyštw ‘may I snow’.' Same derivation, same s-initial citation form.\"\n            },\n            {\n              \"src\": \"SOD\",\n              \"where\": \"SOD_pages.txt, index 'snow 9312'\",\n              \"stance\": \"partial\",\n              \"note\": \"Gharib's English index lists 'snow 9312' pointing back to the s-initial headword; there is no šn- entry in the dictionary.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 974\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny cites 'pamir. sugni zin ‘snow’ (*snaiga-)' among the Iranian reflexes but no Sogdian form.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"snaiwaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *snaiwaz m. 'snow' is the standard reconstruction and is precisely the o-grade noun *snóygʷʰ-o-s of the root: PIE *snoygʷʰos > pre-Gmc *snaigʷʰaz > (Grimm's law: *gʷʰ > *gw/w) Gmc *snaigwaz > *snaiwaz. Watkins/AHD spells out the chain: 'Suffixed o-grade form *snoigʷh-o- in Germanic *snaiwaz in Old English snāw, snow'. The form is directly attested in Gothic snaiws (Wulfila, 4th c.), and gives ON snjór, OHG snēo (gen. snēwes) > German Schnee, OS/OFris. snē, Du. sneeuw.\",\n          \"derivation_fa\": \"ژرمنی آغازین *snaiwaz «برف» بازسازی معیار است و درست همان نام‌واژهٔ درجهٔ o ی ریشه، یعنی *snóygʷʰ-os، است: *snoygʷʰos هندواروپایی > *snaigʷʰaz پیشاژرمنی > بر پایهٔ قانون گریم *gʷʰ به *gw/w بدل شده و *snaiwaz به دست آمده است. واتکینز همین زنجیره را می‌آورد: «صورت درجهٔ o ی پسوندی *snoigʷh-o- در ژرمنی *snaiwaz». این صورت در گوتیِ اولفیلا (سدهٔ چهارم میلادی) به‌گونهٔ snaiws گواهی شده و بازتاب‌های آن ON snjór، آلمانی علیای کهن snēo (> Schnee آلمانی)، و هلندی sneeuw است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/snaiwaz\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:974\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt s.v. sneig^h- (Page(s): 974): 'Gothic snaiws ‘snow’ = Old English snaw, Old High German sneo (Gen. snewes)', and the root line itself gives the noun as 'snoigʷho-s ‚Schnee’' — the etymon Nourai labels Germanic snaiwaz.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. sneigʷh-\",\n              \"stance\": \"supports\",\n              \"note\": \"'1. Suffixed o-grade form *snoigʷh-o- in Germanic *snaiwaz in Old English snāw, snow: SNOW.' — the reconstruction *snaiwaz verbatim.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 1466 s.v. snow (KLN_1966.txt leaf 778)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… rel. to OS., OHG. sneo … Goth. snaiws, ‘snow’ … fr. I.-E. base *snoigwhos, ‘snow’'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. snoiguhos (leaf 682 ≈ p. 1334)\",\n              \"stance\": \"supports\",\n              \"note\": \"'snoiguhos ‘snow’ … Go. snaiws, m. OHG sneo, snio; OE snàw, m. ‘snow’; OCS & com. Sl.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"snow\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gmc *snaiwaz > Old English snāw (Beowulf, Anglo-Saxon Chronicle) > Middle English snaw/snow > Modern English snow. The change is the ordinary Middle English rounding and raising of OE long ā to ǭ in the north-of-Humber-excepted dialects (OE snāw > ME snow, like OE bān > bone, OE stān > stone), with the final -w preserved as the second element of the resulting diphthong. No borrowing is involved anywhere in the line.\",\n          \"derivation_fa\": \"*snaiwaz ژرمنی > snāw انگلیسی کهن (گواهی‌شده در بئوولف و «سالنامهٔ انگلوساکسون») > snaw/snow انگلیسی میانه > snow انگلیسی امروز. دگرگونی آوایی همان گردشدن و برافراشته‌شدنِ āی کشیدهٔ انگلیسی کهن در انگلیسی میانه است (مانند bān > bone و stān > stone)، و w پایانی همچون جزء دومِ دوگانه‌واکه باقی مانده است. هیچ وام‌گیری‌ای در این زنجیره در کار نیست؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/snaiwaz\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. sneigʷh-: '… in Germanic *snaiwaz in Old English snāw, snow: SNOW'; the AHD index line 'SNOW sneigʷh-' confirms the headword assignment.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 1466 s.v. snow (KLN_1966.txt leaf 778)\",\n              \"stance\": \"supports\",\n              \"note\": \"'snow, n. — ME. snaw, snow, fr. OE. snāw, which is rel. to OS., OHG. sneo … Goth. snaiws, ‘snow’ … fr. I.-E. base *snoigwhos.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 1.81 'snow', leaf 97 ≈ p. 73\",\n              \"stance\": \"supports\",\n              \"note\": \"Buck's table: 'OE snāw | ME snow | NE snow', with 'Goth. snaiws, OE snāw, etc. general Gmc.'\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Sneudh, Neudh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)neudʰ- 'mist, cloud', noun *snoudʰo-\",\n      \"note\": \"Pokorny p. 978 (the entry runs onto leaf 219 = p. 979 in POK_03.txt) heads '2. sneudh- ‚Nebel; neblig, düster“; snoudho- ‚Nebel“', and Watkins/AHD has 'sneudh-. Mist, cloud. Latin nūbēs, cloud: NUANCE. [Pok. 2. sneudh- 978.]' — Nourai's gloss 'mist, cloud' is the two dictionaries' glosses combined, and his double citation form 'Sneudh, Neudh' correctly records that the s-mobile is absent in the Italic and Brittonic reflexes (Lat. nūbēs, W. nudd) while present in Iranian (Av. snaoδa-). Pokorny keeps this root separate from '1. sneud(h)- ‚schläfrig“' but allows a possible link ('als ‚benebelt, dämmerig = schläfrig“ vielleicht zu 1. sneud(h)-'); modern work (de Vaan 2008) keeps them apart, as Nourai does. Note for the owner: on the printed page an empty, wordless box is drawn to the right of the Avestan node with an arrow into it; it carries no language label and no word, and both the chart text and the extracted JSON rightly ignore it.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۹۷۸ مدخل «2. sneudh- «مه؛ مه‌آلود، تیره»؛ snoudho- «مه»» را آورده و واتکینز نیز «sneudh-. Mist, cloud. لاتینی nūbēs «ابر»: NUANCE [Pok. 978]». پس معنای «mist, cloud» در نمودار درست است و صورت دوگانهٔ «Sneudh, Neudh» به‌درستی نشان می‌دهد که sِ آغازینِ متحرک (s-mobile) در بازتاب‌های ایتالیک و برایتونیک (لاتینی nūbēs، ولزی nudd) افتاده ولی در ایرانی (اوستایی snaoδa-) مانده است. پوکورنی این ریشه را از «1. sneud(h)- «خواب‌آلود»» جدا می‌داند و دِ وان (۲۰۰۸) نیز همین جدایی را می‌پذیرد، چنان‌که نورایی کرده است. ادعای نورایی درست است. (یادداشت: در صفحهٔ چاپی، کنارِ گرهٔ اوستایی جعبه‌ای تهی و بی‌واژه کشیده شده که نه برچسب زبانی دارد و نه واژه‌ای؛ متن نمودار و دادهٔ استخراج‌شده به‌درستی آن را نادیده گرفته‌اند.)\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/nubes\",\n        \"https://www.etymonline.com/word/nuance\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:978\",\n          \"status\": \"supports\",\n          \"note\": \"POK_03.txt leaf 219 (the '2. sneudh-' entry begins on p. 978 and continues here): '2. sneudh- ‚Nebel; neblig, düster“; snoudho- ‚Nebel“. Av. snaoda- ‚Gewölk“, südbaluci nōd ‚leichtes Gewölk, Nebel, Regenwolke“; gr. νυθόν … lat. [nubes] ‚Wolke“ … cymr. nudd ‚Nebel“'. POK_full.txt: 'Root / lemma: sneuδʰ-2, Meaning: mist … Page(s): 978'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 697\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd2_pages.txt: 'sneudh- ‚Nebel; nebelig, düster“. Av. snaoda- ‚Gewölk“, südbaluci nod ‚leichtes Gewölk, Nebel, Regenwolke“ (nach Solmsen WklPh. 1906, 870 zu) lat. nūbēs ‚Wolke“, cymr. nudd ‚Nebel“' — the source of POK 978.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. sneudh-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 976: 'sneudh-. Mist, cloud. Latin nūbēs, cloud: NUANCE. [Pok. 2. sneudh- 978.]' — both of Nourai's gloss words and the whole Latin→nuance line in one entry.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, leaf 681 ≈ p. 1332\",\n          \"stance\": \"partial\",\n          \"note\": \"IEC.txt: '(sneudh-?, snoidh-? ‘cloud, mist’, etc. See Supt: S)' — Mann records the root and gloss but flags the reconstruction as uncertain and offers *snoidh- as an alternative shape.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"snaoda\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan snaoδa- m. 'cloud(s)' is attested once, in the Vidēvdād passage that also carries the verb of the previous chart: V. 2.22 'yahmāt haca … snaoδō vafra snaēžāt barəzištaēibyō gairibyō' — Bartholomae (AirWb col. ~1636) renders 'weshalb zunächst das Gewölk Schneemassen herschneien wird von den höchsten Bergen her'. The form is the o-grade noun *snoudʰo- of the root (PIE *snoudʰ-o- > Ir. *snauda- > Av. snaoδa-, with the regular Avestan raising of *au to ao and the regular Old Iranian spirantisation of intervocalic *d to δ); its West Iranian relatives are Balochi nōd 'light cloud, rain-cloud' (cited by Pokorny and Walde-Pokorny) and MP snōy ‹snwd› '(rain-, snow-)cloud' in MacKenzie.\",\n          \"derivation_fa\": \"اوستایی نو snaoδa- «ابر، توده‌ابر» تنها یک بار گواهی شده است، در همان بند وندیداد ۲:۲۲ که فعل نمودار پیشین نیز در آن آمده: «snaoδō vafra snaēžāt barəzištaēibyō gairibyō»، که بارتولومه چنین ترجمه می‌کند: «توده‌ابر از بلندترین کوه‌ها برف خواهد بارید». این واژه نام‌واژهٔ درجهٔ o ی ریشه، یعنی *snoudʰo-، است: *snauda- ایرانی باستان > snaoδa- اوستایی، با تبدیل معمولِ au به ao و نرم‌شدن (سایشی‌شدنِ) dِ میان‌واکه‌ای به δ. هم‌ریشه‌های ایرانی غربی آن بلوچی nōd «ابر سبک، ابر باران‌زا» و فارسی میانهٔ snōy ‹snwd› «ابرِ باران و برف» (مکنزی) است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nubes\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:978\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 219 (entry beginning p. 978): 'Av. snaoda- ‚Gewölk“, südbaluci nōd ‚leichtes Gewölk, Nebel, Regenwolke“'; POK_full.txt s.v. sneuδʰ-2: 'Avestan snaoδa- ‘clouds’'. Exactly the node's word and gloss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AirWb col. ~1636, leaf 886 of BRT.txt\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. snaoδa- m. ‘Gewölk’: yahmāt haca Paurvą snaoδa vafra snaēžāt barəzištaēibyō gairibyō … V. 2.12 [= 2.22]. Vgl. sbal. nōd'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie CPD p. 76 s.v. snōy\",\n              \"stance\": \"supports\",\n              \"note\": \"'snōy [snwd] (rain-, snow-)cloud' — the Middle Persian continuant of the same *snauda-, which corroborates the Avestan reading.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 697\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. snaoda- ‚Gewölk“, südbaluci nod ‚leichtes Gewölk, Nebel, Regenwolke“'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"nůběs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin nūbēs, -is f. 'cloud, mist, vapour' (the JSON's 'nůběs' is the extraction's house rendering of nūbēs; the printed page shows the same). It is the s-less (Neudh) branch of the root: PIE *(s)neudʰ-, zero/e-grade *(s)noudʰ- > Proto-Italic *nouðet-is > Lat. nūbēs, with the regular Latin monophthongisation of *ou to ū (as in dūcō < *doukō) and *dʰ > Lat. b after u/before r-l (the *dʰ > f- only word-initially; medially it yields -b-, exactly as in Lat. ruber < *h₁rudʰ-ro-). Klein p. 1059: 'L. nubes, ‘cloud’, which prob. stands for *snoudhis and is cogn. with Avestic snaoda-, ‘clouds’, W. nudd, ‘fog’'. De Vaan 2008 accepts the same etymon (PIt. *nouðetis < PIE *(s)newdʰ-e-ti-s) while warning that nūbēs is not related to the look-alike nebula.\",\n          \"derivation_fa\": \"لاتینی nūbēs «ابر، مه، بخار» (صورت «nůběs» در داده، همان شیوهٔ نگارشِ کتاب برای nūbēs است). این واژه به شاخهٔ بدونِ sِ ریشه (همان «Neudh» در نمودار) تعلق دارد: *(s)noudʰ- هندواروپایی > *nouðetis ایتالیک آغازین > nūbēs لاتینی، با تک‌واکه‌شدنِ قاعده‌مندِ ou به ū (مانند dūcō از *doukō) و بدل‌شدنِ *dʰ میانی به b (چنان‌که در ruber از *h₁rudʰ-ro-). کلاین در صفحهٔ ۱۰۵۹ می‌نویسد: «لاتینی nubes که احتمالاً از *snoudhis است و هم‌ریشه با اوستایی snaoda- «ابرها» و ولزی nudd «مه»». دِ وان (۲۰۰۸) نیز همین ریشه را می‌پذیرد اما هشدار می‌دهد که nūbēs با nebula «مه» — با آنکه شبیه می‌نماید — خویشاوند نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nubes\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1059\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 567 (two printed pages per leaf, = pp. 1059/1060) s.v. nubilous: 'Late L. nubilosus, fr. L. nubes, ‘cloud’, which prob. stands for *snoudhis and is cogn. with Avestic snaoda-, ‘clouds’, W. nudd, ‘fog’, Gk. νυθόν (Hesychius), ‘dark, dusky’.' — Nourai's root, Avestan cognate and Latin word in one sentence.\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'sneudh-. Mist, cloud. Latin nūbēs, cloud: NUANCE. [Pok. 2. sneudh- 978.]'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 978 (text on leaf 219 of POK_03.txt)\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. [nūbēs] ‚Wolke“, dazu obnūbō, -ere ‚verhüllen“ … als denominatives Verbum: ‚(sich) bewölken“ = ‚(sich) bedecken“'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 697\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. nūbēs ‚Wolke“' listed directly beside Av. snaoda- under sneudh-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"nue; nuance\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both French words are correctly placed. (a) nue f. 'cloud' does not continue classical nūbēs directly but its Vulgar Latin collective/feminine remake *nūba (cf. Ital. nuvola, Sp. nube), whence Old French nue (11th c.), still poetic in modern French. (b) nuance is a Middle French derivative of the verb nuer 'to shade, to match colours', itself denominative from nue: the metaphor is the graded colours of clouds — Klein p. 1059 says so explicitly ('so called with reference to the different colors of the clouds'). The suffix is -ance (< Lat. -antia). So the chart's placing of nuance under nue, and of both under Latin nūbēs, is exactly the standard account.\",\n          \"derivation_fa\": \"هر دو واژهٔ فرانسوی درست جای گرفته‌اند. یکم، nue «ابر» بازماندهٔ مستقیمِ nūbēs کلاسیک نیست بلکه از صورت لاتینی عامیانهٔ *nūba (قس ایتالیایی nuvola، اسپانیایی nube) می‌آید که در فرانسوی کهن (سدهٔ یازدهم) nue شده و امروز واژه‌ای ادبی است. دوم، nuance ساختهٔ فرانسوی میانه از فعل nuer «سایه‌روشن زدن، رنگ‌ها را هماهنگ کردن» است که خود از nue گرفته شده؛ استعارهٔ آن درجه‌بندیِ رنگ ابرهاست — کلاین در صفحهٔ ۱۰۵۹ همین را می‌گوید: «چنین نامیده شده به سببِ رنگ‌های گوناگون ابرها». پسوند آن -ance (از لاتینی -antia) است. پس جای‌گذاری nuance زیر nue و هر دو زیر nūbēs لاتینی، همان روایت معیار است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nuance\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1059\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 567 (= p. 1059) s.v. nuance: 'F., ‘shade, hue; a slight difference’, fr. MF., fr. nuer, ‘to shade’, fr. nue, ‘cloud’, fr. L. nubes (see nubilous and -ance); so called with reference to the different colors of the clouds.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline.com/word/nuance (web, archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'from French nuance ‘slight difference, shade of colour’ (17c.), from nuer ‘to shade’, from nue ‘cloud’, from Gallo-Roman *nuba, from Latin nubes ‘a cloud, mist, vapor’, from PIE *sneudh- ‘fog’.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. sneudh-\",\n              \"stance\": \"partial\",\n              \"note\": \"Watkins jumps straight from 'Latin nūbēs, cloud' to 'NUANCE' without spelling out the French stage; it supports the chain but does not name nue/nuer.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"nuance\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English borrowed nuance from French unchanged, in 1781, first of shades of colour; Etymonline dates the extension 'slight variation in shade' of tone or meaning to 1852 and the musical use to 1841, with the verb (1886) and nuanced (1896) later. The spelling and the French nasal-vowel pronunciation were both kept, marking it as a late, learned borrowing rather than a Norman-era one — which is why the chart gives it a separate box under French.\",\n          \"derivation_fa\": \"انگلیسی واژهٔ nuance را در سال ۱۷۸۱ بی‌هیچ دگرگونی از فرانسوی وام گرفت، نخست دربارهٔ سایه‌های رنگ؛ بنا بر Etymonline معنای «تفاوت اندک در لحن یا معنا» از ۱۸۵۲ و کاربرد موسیقایی آن از ۱۸۴۱ است، و فعلِ آن (۱۸۸۶) و صفت nuanced (۱۸۹۶) دیرتر پدید آمدند. نگه‌داشتنِ املا و تلفظِ خیشومیِ فرانسوی نشان می‌دهد که این وام‌واژه‌ای دیرهنگام و کتابی است، نه وامی از دورهٔ نورمان‌ها؛ به همین سبب نمودار آن را در جعبه‌ای جداگانه زیر فرانسوی نهاده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nuance\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1059\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 567 (= p. 1059): 'nuance, n., a slight difference. — F., ‘shade, hue; a slight difference’, fr. MF., fr. nuer …' — Klein's headword is the English word, derived from French.\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'sneudh-. Mist, cloud. Latin nūbēs, cloud: NUANCE.'; the AHD word index line reads 'NUANCE sneudh-'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline.com/word/nuance (web, archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'nuance (n.) 1781, ‘slight difference or shade of color’ … 1852 as ‘a slight variation in shade’; 1841 in music.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 1059 s.v. nuance and nubilous\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's cross-reference 'Cp. nuance, nubia, nubiform' under nubilous ties the English word back to L. nubes and thence to Avestic snaoda-.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T02:38:12.985Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-462.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:38:15.124Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-462.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 462"
}
```


### [2026-09-14T02:38:16.733Z] TOOL RESULT

```
JSON OK
nodes verified: 9/9
node verdicts: {'confirmed': 7, 'plausible': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'partial': 1}
books consulted: {'supports': 18, 'partial': 4, 'silent': 4} | by book: {'BRT': 3, 'WLD': 3, 'KLN': 3, 'CHEUNG': 2, 'PHD': 2, 'SYN': 2, 'POK': 2, 'AHD': 2, 'WEB': 2, 'BQT': 1, 'MON': 1, 'HUB': 1, 'SOD': 1, 'IEC': 1}
```


## [2026-09-14T02:38:29.188Z] AGENT

Page 462 (book p. 432) verified — `data/verification/page-462.json`, `verify_check.py 462` shows 9/9 nodes, 0 PROBLEM lines.

Counts: roots 2 confirmed. Nodes: 7 confirmed, 1 plausible, 1 transcription_suspect. Ref checks: 11 supports, 1 partial. 5 redirect entries (Sner, Snerq, Sneu, Snĕu, Snôǧ, Snŭ) skipped.

- **transcription_suspect** — Sneigwh, Sogdian `šněš` (#3): Nourai's own source, Gharib SOD no. 9312 (p. 376), reads `snyš- / snēš- ©Av. snaēža`, and Cheung 2007:349 has `MSogd. snyš`. No š-initial citation form exists. `error_in: book` — the printed page 432 does show "šněš" (PNG saved to `data/verification/sources/refs/ocr/BOOK/462.png`), so the extraction is faithful.
- **plausible** — Sneigwh, Persian `sněhr «سنهر»` (#2): the word is real and the root is right, but it is Middle Persian, not New Persian. Horn 292 no. 181 is in his *Pahlavi appendix* (which starts p. 263), Buck 1.81 calls it "Pahl. sb. snēhr … Horn 292", and MacKenzie/Bartholomae read it `snēxr` ‹snyhl› (with -xr, not -hr). It never reached New Persian, where 'snow' is *barf* < MP *wafr*.

No extraction errors found: the JSON matches the printed page everywhere (`nůběs`, `snaěž/snaěj/snaěža`, «سنهر» all verified against the 600-dpi render).

One layout note for the owner, not an error: on the printed page, entry 5 (Sneudh, Neudh) has an **empty, wordless box** drawn to the right of the Avestan node with an arrow into it. It has no language label and no word; the chart text and the extracted JSON both correctly ignore it.
