# Verification process log — verify-page-349


## [2026-09-07T18:17:41.178Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 349 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-349.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-349.json. Write /home/sfmqrb/git/rishe/data/verification/page-349.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 349` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:43.500Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:17:44.208Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:44.231Z] TOOL RESULT

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


## [2026-09-07T18:17:44.627Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-349.txt"
}
```


### [2026-09-07T18:17:44.649Z] TOOL RESULT

```
1	=== PDF page 349 (book page 319) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nana, Nena : a child word for mother a nurse  (refs POK:754)
4	#1 (parent #0) [Sanskrit] refs=POK:754; KLN:1062 | nana : mother
5	  #2 (parent #1) [Persian] refs=KLN:1062; POK:754; HRN:234 | naneh «ننه» : a slang word for mother or nurse
6	#3 (parent #0) [English] refs=AHD | nana, nanny
7	#4 (parent #0) [Late Latin] refs=AHD | nun
8	  #5 (parent #4) [English] refs=KLN:1062 | nun, nunnery
9	#6 (parent #0) [Greek] refs=POK:754; AHD | nana : aunt ; nannus : little old man, a dwarf
10	  #7 (parent #6) [Latin] refs=AHD:872 | nanŭs : dwarf, short
11	    #8 (parent #7) [English] refs=AHD:872; KLN:1027 | nano- : a prefix meaning a small amount, one billionth of a specified unit. ; nanosecond, nanometer
12	--- entry 1 ---
13	ROOT Naptu -> redirect to Nabatu
14	--- entry 2 ---
15	ROOT [Sanskrit] Naranga : orange tree  (refs HJB:642)
16	#1 (parent #0) [Persian] refs=HJB:642; BQT:2095 | nâreng «نارنگ» : a citrus fruit ; nârengî «نارنگی» : tangerine ; anâr «انار ?» : pomegranate (see SKT:360) | NOTE: IEC:1645 derives "anâr" from Indo-European roots "Nôr, Anôr: juicy"
17	  #2 (parent #1) [Arabic] refs=None | nâranj
18	    #3 (parent #2) [Persian] refs=MON | nârenj «نارنج» : a citrus fruit | extra: نارنجی ، نارنجک
19	    #4 (parent #2) [Spanish] refs=None | naranja
20	      #5 (parent #4) [Italian] refs=None | arancia
21	        #6 (parent #5) [French] refs=None | 
22	          #7 (parent #6) [English] refs=SKT:360 | orange
23	--- entry 3 ---
24	ROOT Narda -> redirect to Nedo
25	
```


## [2026-09-07T18:17:48.621Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-349.json",
 "description": "Read source JSON page 349"
}
```


### [2026-09-07T18:17:48.663Z] TOOL RESULT

```
{
  "pdf_page": 349,
  "book_page": 319,
  "entries": [
    {
      "root": {
        "name": "Nana, Nena",
        "lang": "Indo-European",
        "refs": "POK:754",
        "gloss": "a child word for mother a nurse"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:754; KLN:1062",
          "words": [
            {"translit": "nana", "gloss": "mother", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:1062; POK:754; HRN:234",
          "words": [
            {"translit": "naneh", "gloss": "a slang word for mother or nurse", "script": "ننه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "nana, nanny", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Late Latin",
          "refs": "AHD",
          "words": [
            {"translit": "nun", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:1062",
          "words": [
            {"translit": "nun, nunnery", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:754; AHD",
          "words": [
            {"translit": "nana", "gloss": "aunt", "script": null},
            {"translit": "nannus", "gloss": "little old man, a dwarf", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": "AHD:872",
          "words": [
            {"translit": "nanŭs", "gloss": "dwarf, short", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:872; KLN:1027",
          "words": [
            {"translit": "nano-", "gloss": "a prefix meaning a small amount, one billionth of a specified unit.", "script": null},
            {"translit": "nanosecond, nanometer", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Naptu", "redirect": "Nabatu"},
      "nodes": []
    },
    {
      "root": {
        "name": "Naranga",
        "lang": "Sanskrit",
        "refs": "HJB:642",
        "gloss": "orange tree"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "HJB:642; BQT:2095",
          "words": [
            {"translit": "nâreng", "gloss": "a citrus fruit", "script": "نارنگ"},
            {"translit": "nârengî", "gloss": "tangerine", "script": "نارنگی"},
            {"translit": "anâr", "gloss": "pomegranate (see SKT:360)", "script": "انار ?"}
          ],
          "note": "IEC:1645 derives \"anâr\" from Indo-European roots \"Nôr, Anôr: juicy\"",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "nâranj", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "nârenj", "gloss": "a citrus fruit", "script": "نارنج"}
          ],
          "script_extra": "نارنجی ، نارنجک",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Spanish",
          "refs": null,
          "words": [
            {"translit": "naranja", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "arancia", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "SKT:360",
          "words": [
            {"translit": "orange", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Narda", "redirect": "Nedo"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T18:17:51.406Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','AHD','HJB','BQT','MON','IEC','SKT','WLD','SYN','FSD','WEB','ARY','PHD','NYB','HUB','BRT','KNT','AFM','PLA','LKT','DEV','PHN','FVQ']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online for needed abbreviations"
}
```


### [2026-09-07T18:17:52.940Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-07T18:17:59.285Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','AHD','HJB','SKT','IEC','LKT','DEV','PHN','ARY','SYN','WLD','FSD','WEB','MON','BQT']:\n    v=d.get(k)\n    print('=====',k)\n    print(json.dumps({kk:vv for kk,vv in v.items() if kk in ('local_file','page_offset','lookup_hint','scans','kind','url')},ensure_ascii=False,indent=1))\n\"",
 "description": "Full ref details"
}
```


## [2026-09-07T18:17:59.472Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T18:18:00.965Z] TOOL RESULT

```
===== POK
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"
}
===== KLN
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
}
===== HRN
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."
}
===== AHD
{
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."
}
===== HJB
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/hobsonjobsonagl02croogoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt",
 "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers."
}
===== SKT
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."
}
===== IEC
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."
}
===== LKT
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."
}
===== DEV
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairety00devi",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt",
 "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start."
}
===== PHN
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairetym01pihagoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt",
 "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc."
}
===== ARY
{
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ]
}
===== SYN
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."
}
===== WLD
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
 ],
 "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).",
 "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."
}
===== FSD
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."
}
===== WEB
{
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies."
}
===== MON
{
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null
}
===== BQT
{
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
 ]
}
```


### [2026-09-07T18:18:01.033Z] TOOL RESULT

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


## [2026-09-07T18:18:05.327Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: nana\" POK_full.txt\ngrep -n -i \"nana\\b\" POK_full.txt | head -40\necho \"=== pages 754 area\"\ngrep -n \"Page(s): 754\" POK_full.txt | head",
 "description": "Grep Pokorny for nana"
}
```


### [2026-09-07T18:18:05.414Z] TOOL RESULT

```
61773:Root / lemma: nana, nena etc. 
9481:Material: Old Indie bababa-karotiirom the crackle of the fire; gr. papal, nana! " upon my 
13978:Old Icelandic burn. ' pantry, zenana (part of a house for women in India)', Old English 
16610:7a/7/&/7a (Tacit.), if from *tafnana, Marstrander NTS. 1, 159. 
21639:dhunana-, dhOni-t "the shaking', dhOnayati^ moves to and fro, shakes ', dhavftramu. " 
26704:into', inna, innana, probably from *eni-n-, s. Brugmann IF. 33, 304 f.); (under the influence 
35341:expert '; compare Old \r\6\c Jnana-m {*gnd-no-m) 'knowledge, cognition '. 
47357:ludere, ludern {SchmeWer |2 1542) "Alpine alder, Betula nana L.'. 
61773:Root / lemma: nana, nena etc. 
61781:Alb. Geg nona, nana " mother ' 
71561:compare anana-n. 'mouth, face'), through influence of aisi also ' eternal '; '(doubtful 
84570:"smudges'; Tocharian B swanana m/'sa ' pork'; 
=== pages 754 area
61771:Page(s): 754 
61797:Page(s): 754 
61881:Page(s): 754 
61895:Page(s): 754 
61907:Page(s): 754
```


## [2026-09-07T18:18:07.635Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61765,61800p' POK_full.txt",
 "description": "Read Pokorny nana entry"
}
```


### [2026-09-07T18:18:07.689Z] TOOL RESULT

```
Material: Gr. vcxkoc, n., voKri f. "woolen fell, fur, fleece', apvaKi(; f. (for *apvo-vaKi(;) " fleece 
', vaKu(5)piov 5£ppa Hes.; Old English naesc^saW. leather as e.g. buckskin ' {*nak-s-ko-, - 
ka\ compare the -e5-stem vqkoc;); Old Prussian nognan {irom *noknan) n. "leather' {*nak- 
no-)\ in addition after E. Lewy Old Indie naka-^ vault of the sky, firmament, heavens, skies 

References: WP. II 316. 
Page(s): 754 

Root / lemma: nana, nena etc. 

Meaning: mother, etc.. (child word) 

Material: Old Indie /7a/7a "mother, old woman ', */7a/75/7a reshaped (after svasa: svasr-) to 

nanandar^oia husband's sister', np. /75/75 "mother'; 

Alb. Geg nona, nana " mother ' 

gr. vavva, vivvr) " aunt ', vsvvoc;, vavvaq "uncle'; alb. /75/7e "mother, wet nurse '; Latin 

nonnusm., nonnaf. late " word used by young monks when addressing elders, a nun ', 

also " nurserymaid '; cymr. nain{*nanJ) "grandmother'; russ. njanja^ children keeper, 

nurse, caretaker of a baby or young children, nanny ' (dial, also "older sister '), Bulgarian 

/7e/7/" older person, elder', Serbo-Croatian nena, /7a/7a "mother', Serbian /7a/7 "father'; 

compare also Modern High German Nenne, Kinderwort for "milk'. 

References: WP. II 317, WH. II 175. 

Page(s): 754 

Root/ lemma: nant- {* he-nant-) 
Meaning: to dare, risk
```


## [2026-09-07T18:18:17.988Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"nannos\\|vavvo\\|nanus\\|dwarf\" POK_full.txt | head -30\necho \"=== WLD Bd2 around p.317\"\nawk 'BEGIN{RS=\"\\f\"} NR==322' incoming/WLD/WLD_Bd2_pages.txt | head -80",
 "description": "Pokorny nanos + Walde-Pokorny II 317"
}
```


### [2026-09-07T18:18:19.293Z] TOOL RESULT

```
1627:derived cymr. afanc^ beaver, water demon, dwarf ', to Middle Irish abac {*abankos) " 
1629:beaver, dwarf', Swiss -French avan 'pasture' {*abanko-); Latvian FIN Abava. 
22848:" dwarfish, crippled ' (see there). 
23096:reckoned under other names of physical ailments and perhaps stands for " dwarfish, 
23098:crippled ', with Old Norse dvergr. Old English dweorg, engl. dwarf. Middle Low German 
23102:dwerch, nnd. dwarf, Old High German twerc, Middle High German twerc, -ges, Modern 
24037:Material: Latin ebulus, -Ti. and -umu. " dwarf-elder (danewort, a fetid European species of 
24047:ablaut, (with /r-suffix) gall, and gallorom. oo'ocos "dwarf elder'; 
24049:Old High German affub, attah. Old Saxon ao'^/r "dwarf elder' (borrowed from Celtic); 
26598:ordinals: *neueno- in Latin nanus, introduced after the 7 and 10 m instead of n Umbrian 
31048:Bavarian knos^ a youth, lad ', Swiss c/7/705/ "thick man, husband', nrhein. knoser dwarf, 
45974:m. 'shrub, bush', Czech krs^ dwarf tree ', krs-ati, -nouti^ abate ', poln. dial, karslak^ low, 
46819:"fairy demon, ghost, dwarfish ghost'. Old Prussian cancY 'devil', Lithuanian kaukara^\\\\\ , 
46821:Latvian kukurs, kukums^ hunch, swelling, blister', kuki's^ dwarf; wren, songbird ', kuksa' 
48679:toad, dwarf'; of the ruptured skin (becoming rough) (" goose bumps ') also Lithuanian 
53410:demon, ghost, dwarf ' (W. Schuize Kl. Schr. 399 f.); 
67455:high, dwarf', nuycbv, -6vo(; m. "ulna, ell', nuy-paxo(;, nuKTr|<; "Faustkampfer'; Latin pugil 
75609:Lithuanian skramblys^ smaW dickleibiger person, dwarf'. Old Prussian (with p) sen- 
76442:Middle Irish cymr. etc. co/r'verkijmmert, dwarfish ' {*korso-)\ 
78547:sm/rdet/ ^st\nk', Latvian sm/rdef6s., Lithuanian 5/77//'o'e/e "dwarf elder', s/775/'o'//7//"stinkend 
=== WLD Bd2 around p.317
                                    nag^ih" (nabh-?)     — iiard(h)o-                                   317

n<BSc ,,\veiches Leder wie z. B. Hirschleder'' {^naq-s-qo-, -qa ; vgl.              den -es-St.
vdxog);       apr.     nognan    n, „Leder'*        {n^q-no-).     Liden Stud. 66 f. (mit Lit.
iiber den Yergleich von vdxog mit got. snaga „Kleid, Mantel'^, dessen 5 -
zur Zuruckhaltung notigt), IP.  18, 410 f.
  Niclit iiberzeugend iiber nognan Petersson IF. 23, 393, dessen Wz. 7iogi-
„schaben‘^ keine Gewahr hat (s. u. nog^o- „Baum“).


nag^h- „nuchtern‘' (nabh-?).
     Gr.   v}](p(jo,   dor. vdcpco „bin niichtern^^;          arm. nmiti „niichtern^‘ (Pedersen
KZ. 39, 349; hieher stellen Strachan BB. 20, 22, Pick II ^ 189, Pedersen
KG. I 109 auch ir. nar ,,bescheiden‘^, nare „Scham“ als "^nSg^li-ro-, in der
Bed. sehr abliegend und von Loth Mel. Ha vet 240 wegen des eher damit
zu vergleichenden cymr. 7iar ,,Zwerg'' ferngehalten).      Auch spat-ahd.
miohUirn ^niichtern^^ (Frohde BB. 3, 14) bleibt fern (Klosterentlehnung aus
lat.   nocturnus,            nociurnnm „noch im Morgengrauen abgehaltener
                         speziell
Pruhgottesdienst‘,       Kluge und Weigand-Hirt s. v., unter teilw. lautl. Ein-
                            s.

fluB von ahd. ndita f. „Morgendammerung“; nicht eine neben lat. noctnrnus.
gr. vvxrsQivog,   engl. niliterne „nachtlich“ stehende urverwandte Yrddhi-
bildung "^noMrno-, gegen Pick III ^ 290, Falk-Torp u. n0gtern).
   Abweichend verbindet Bahder IP. 14, 260 vricpco als idg. ^nobh- mit mhd.
nuofer „nuchtern, munter, frisch“, doch ist dessen Bed. erst aus „frisch,
rasch“ spezialisiert, s. u. snehh(ri-^     lautlich zu beanstanden ist Pedersen
KG. I 109 Deutung von miofcr aus "^nag^Jiri- unter Anreihung an die obige
Sippe.


naiia,     nena Lallwort.
                                  ^nanUna umgebildet (nach svasd svasr-)
     Ai. nand ..Mutter, Miitterchen”,                                                           :


zu nanandar „des Mannes Schwester“, np. nana „Mutter“    gr. vdwaj vhva,        ;


vlvva „Base, Xante'', vevvog, vdvvog „Oheim"; alb. (G. Meyer BB. 8, 191,
Alb. Wb. 297) nans „Mutter, Amme''; lat. (sehr zw., s. Yf. LEWb.^ s. v.)
nonnus^ nonnc spat jjMonch, Nonne'', auch „Pflegerin eines Kindes'' cymr.                           ;


72am (^awl) „Gro6mutter"; russ. 72janJa„Kinderwarterin“ (mdartl. auch,,altere
Schwester"), bulg neni „der Altered, skr. nena, nana, ka^'. nana, nena, nenia
 Mutter", sorb, nan „Yater". Ygl. auch nhd. Nemie Kinderwort fiir „Milch".
,,


  Yanicek LEWb.^ 139, Fickl^94, 499,11 ^189, Brugmann II ^ 1, 127, 335,602.

nant-      .,\vagen, sich erkiihnen".
   Ahd. Prat, ginand ,,Mut wozu haben"; got. ana-nanpjan „wagen", aisL
nenna „ubers Herz bringen", ahd. ginenden^ as. natJiian^ ags. nepan ,,wagen",
aisl. nenninn .,tatig, strebsam" f,,'^wagefroh"), mhd. geyiende{c) „eifrig", ahd.

nand (auch in Namen vrie Ferdinand)^ ags. nop ,.Mut" air. nett „Kampf"      ;



(^nenti- oder "^nanti-).   Pick 111^ 292, Palk-Torp 11 neyine (wo gegen den
                                                                        .



Yergleich mit gr. iv-avTiog),            —
                                  Originell, aber sehr gewagt sucht Schroder
Abl. 9 in nanU redupliziertes [api-an-t- zu dt. ahnden und Wz. an- „atraen“.


nard(h)o- (oder "^nerdhc- nrdho-^i) Pflanze mit schaftartigem Stengel?
                                     :




     kx.nadd-. nald-, ndld- m. ,,Sehilfrohr'*, mind, aus *narJa-                    = np. ncd „Kohr-
stengel,      Rohre'^ afgh. nagth        f.   ,,   Stengel"   (aus skr. ’^narda-      stammt durch
```


## [2026-09-07T18:18:33.555Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins nana/nan\"\ngrep -n \"^nana\\|^nan-\\|nanny\\|dwarf\" AHD_watkins1985.txt | head -20\necho \"=== KLN 1966 nun,\"\ngrep -n \"^nun,\\|^nunnery\\|^nanny\\|^nana\\|^nano-\\|^nanism\\|^nanoid\" KLN_1966.txt | head -20",
 "description": "AHD Watkins + Klein greps"
}
```


### [2026-09-07T18:18:33.655Z] TOOL RESULT

```
=== AHD watkins nana/nan
769:nana. Child’s word for a nurse or female adult other than its mother. 1. Greek nanna, aunt, whence nannas, uncle, whence nan(njos, “little old man,” dwarf: NANO-. 2. Late and Medieval Latin nonna, aunt, old woman, nun: NUN}. 3. English (directly from baby talk) NANA, NANNY. [Pok. nana 754.]
=== KLN 1966 nun,
24935:nanism,  n.,  dwarfishness.  —  F.  nanisme,  formed with  suff.  -isme  fr.  L.  nanus,  fr.  Gk.  vavo q,  vxv- vo ?,  ‘dwarf’,  which  is  of  uncertain  etymology. It  is  perh.  a  child’s  lip  word  and  rel.  to  vavvas, vcwo q,  ‘uncle’,  vavvx,  ‘aunt’.  See  nun  and -ism.
24937:nano-,  before  a  vowel  nan-,  combining  form meaning ‘dwarf,  dwarfish'.  —  Gk.vxvo-,  vav-, fr.  vavo;,  ‘dwarf’.  See  nanism.
24939:nanny  goat,  a  she-goat  ( colloq .)  —  Formed  fr. prec.  word  and  goat.
25780:nun,  n.,  1)  a  woman  devoted  to  religious  life,  esp. one  living  in  a  convent  under  vows  of  chastity, poverty  and  obedience;  2)  any  of  various  birds. —  ME.  nunne,  nun,  fr.  OE.  nunne,  fr.  Late  L. norma,  ‘an  old  woman,  a  nun’,  fern,  of  nonnus, ‘an  old  man,  a  monk’,  orig.  a  child’s  lip  word. Cp.  OI.  nana,  ModPers.  nana,  ‘mother’,  Gk. vavva,  vcvva,  ‘aunt’,  Alb.  none,  ‘mother,  nurse', Bulg.  neni,  ‘the  older  one’,  Serbo-Croatian  nana, nena,  ‘mother’,  W.  nain,  ‘grandmother’,  which all  were  orig.  child's  lip  words.  Olt.  nonno, ‘grandfather’,  nonna,  ‘grandmother’,  are  loan words  fr.  Late  L.  nonnus,  resp.  nonna.  Cp. nunnery.  Cp.  also  nanism.
25781:nun,  n.,  the  14th  letter  of  the  Heb.  alphabet.  — Heb.  nun,  lit.  ‘fish’;  so  called  in  allusion  to  the ancient  Hebrew  form  of  this  letter.  Cp.  nu. nuncheon,  n.,  a  light  refreshment  taken  at  noon (i obsol .)  —  ME.  noneschench,  lit.  ‘a  noon-drink’, fr.  none,  ‘noon’,  and  schenche,  ‘a  pouring  out,  a draft".  For  the  first  element  see  noon.  The  second element  derives  fr.  OE.  scencan,  ‘to  give  to drink',  which  is  rel.  to  OS.  skenkian,  OFris. skenka,  OHG.  skenken,  ‘to  give  to  drink’, MHG.,  G.,  Du.  schenken,  ‘to  give’.  The  original meaning  of  these  verbs  was  ‘to  hold  in  a slanting  position’.  They  derive  from  the  Teut. adj.  *skanka-,  ‘slanting,  oblique’,  fr.  I.-E.  base *sqet}g-,  of  s.m.  See  shank  and  cp.  skink,  ‘to serve’.  Cp.  also  luncheon.
25788:nunnery,  n.,  1)  a  community  of  nuns;  2)  a  con¬ vent.  —  ME.  nunnerie,  fr.  OF.  nonnerie,  fr. nonne,  ‘nun’,  fr.  L.  nonna.  See  nun  and  -ery. nuphar,  n.,  the  waterlily.  —  See  nenuphar, nuptial,  adj.,  pertaining  to  a  wedding.  —  L.  nup- tialis,  ‘of  a  marriage  or  wedding’,  fr.  nuptiae, ‘marriage,  wedding’,  fr.  nuptus,  pp.  of  nubo, niibere,  ‘to  marry,  wed’,  which  prob.  stands  for *sneubho  and  is  cogn.  with  OSlav.  snubiti,  ‘to love,  woo’,  Czech  snoubiti,  ‘to  seek  in  marriage, woo’,  Czech  za-snoubiti,  Slovak  zasmibit’,  ‘to betroth’,  Gk.  vupupY),  ‘bride’.  For  the  ending see  suff.  -al.  Cp.  nubile,  connubial,  nymph, nuptials,  n.  pi.  —  Fr.  prec.  word, nuque,  n.,  the  back  of  the  neck,  nape.  —  F., ‘back  of  the  neck,  nape’.  The  original  meaning
33324:nun,  adj.,  queer.  —  Orig.  a  cant  word  meaning ‘good,  fine’,  prob.  a  corruption  of  Gypsy  rom, ‘man,  husband;  gypsy  man’.  See  rom  and  cp. the  first  element  in  rumbustious.
```


## [2026-09-07T18:18:47.570Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# find line numbers of interest -> leaf\nlines=txt.split('\\n')\ntargets=[24935,24937,24939,25780,25788]\nfor t in targets:\n    pos=sum(len(l)+1 for l in lines[:t-1])\n    leaf=txt[:pos].count('\\f')\n    print(t, 'leaf',leaf, 'approx printed p', (leaf-12)*2, 'or', (leaf-12)*2+1)\nEOF\necho \"=== AHD watkins leaf for line 769\"\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(l)+1 for l in lines[:768])\nleaf=txt[:pos].count('\\f')\nprint('leaf',leaf,'printed p',leaf-29)\nEOF",
 "description": "Compute printed pages for Klein and AHD hits"
}
```


### [2026-09-07T18:18:48.970Z] TOOL RESULT

```
24935 leaf 550 approx printed p 1076 or 1077
24937 leaf 550 approx printed p 1076 or 1077
24939 leaf 550 approx printed p 1076 or 1077
25780 leaf 568 approx printed p 1112 or 1113
25788 leaf 569 approx printed p 1114 or 1115
=== AHD watkins leaf for line 769
leaf 73 printed p 44
```


## [2026-09-07T18:19:02.925Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==569' KLN_1966.txt | head -5\necho \"---- leaf 551\"\nawk 'BEGIN{RS=\"\\f\"} NR==551' KLN_1966.txt | head -5\necho \"---- 1971 file check nun\"\ngrep -n \"Late  L.  norma\\|Late L. nonna\\|orig.  a  child’s  lip  word\" KLN_1971.txt | head",
 "description": "Check Klein page numerals"
}
```


### [2026-09-07T18:19:04.160Z] TOOL RESULT

```
 numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  n.,  and  adj.  suff.  -al.
Derivative:  numeral,  n.
numerary,  adj.,  pertaining  to  a  number  or  num¬ bers.  —  ML.  numerdrius,  fr.  L.  numerus.  See number  n.,  and  adj.  suff.  -ary. numerate,  v.,  to  count;  to  enumerate.  —  L.  nu- meratus,  pp.  of  numerdre.  See  number,  v.  and  n., and  verbal  suff.  -ate.
numeration,  n.  —  ME.  numeracion,  fr.  L.  nume- ratio,  gen.  of  -dnis,  ‘a  counting’,  fr.  numeratus, pp.  of  numerdre.  See  number,  v.  and  n.,  and -ation.
numerator,  n.,  that  term  of  a  fraction  which  shows how  many  parts  of  a  unit  are  taken.  — VL.  nume¬ rator,  lit.  ‘counter,  numberer’,  fr.  numeratus,  pp. of  numerdre.  See  number,  v.  and  n.,  and  -tor. numerical,  adj.  —  Formed  with  suff.  -ical  fr.  L. numerus.  Cp.  F.  numirique  and  see  number,  n. Derivative:  numerical-ly,  adv. numerology,  n.,  the  study  of  the  occult  meaning of  numbers.  —  A  hybrid  coined  fr.  L.  numerus, ‘number’,  and  Gk.  -Xoyia,  fr.  -X6yoq,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  -logy.  The  correct form  would  be  arithmology,  fr.  Gk.  api&p.o;, ‘number’,  and  -Xoyia.
---- leaf 551
 B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outside  Indo- European  cp.  Lapp,  namma,  Finn,  nime-.  Hung. nev,  ‘name’.  Cp.  agnomen,  allonym,  anonymous, antonomasia,  antonym,  cognomen,  cryptonym, denominate,  eponym,  Evonymus,  homonym, ignominy,  Jerome,  metonymy,  metronymic,  mis¬ nomer,  nom,  nomen,  nomenclator,  nomenclature, nominal,  nominate,  nominative,  noun,  nuncupa¬ tive,  onomastic,  onomato-,  paronomasia,  paro- nymous,  patronymic,  polyonymous,  praenomen, pseudonym,  renown,  synonym,  toponym,  trino- minal.
Derivatives:  name,  v.  (q.v.),  name-less,  adj., name-ly,  adv.
name,  tr.  v.  —  ME.  namen,  fr.  OE.  namian,  fr. nama,  ‘name’.  See  name,  n.
Derivatives:  name-able,  nam-able,  adjs.,  name- abil-ity,  n.,  nam-abil-ity,  n.,  nam-er,  n.
namesake,  n.,  a  person  having  the  same  name  as an  other.  —  Contraction  of  name's  sake.  Name¬ sake  lit.  denotes  ‘a  person  named  for  the  sake  of another’s  name'.
---- 1971 file check nun
```


## [2026-09-07T18:19:14.641Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nimport re\ndef leafof(t):\n    pos=sum(len(l)+1 for l in lines[:t-1])\n    return txt[:pos].count('\\f')\nfor pat in ['^cherub,','^orange,','^nun,']:\n    for i,l in enumerate(lines,1):\n        if re.match(pat,l):\n            print(pat,i,'leaf',leafof(i))\n            break\nEOF",
 "description": "Klein leaf calibration with cherub"
}
```


### [2026-09-07T18:19:16.002Z] TOOL RESULT

```
^cherub, 7347 leaf 155
^orange, 26460 leaf 583
^nun, 25780 leaf 568
```


## [2026-09-07T18:19:27.563Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -ho \"Klein[^\\\"]\\{0,160\\}\" page-3*.json | grep -i \"p\\.\\|leaf\" | head -30",
 "description": "Look at prior KLN notes"
}
```


### [2026-09-07T18:19:27.621Z] TOOL RESULT

```
Klein cites it in exactly this position ('cp. Akkad. ladunu, Arab. ladan, Heb. lot'). That an Arabian word for the resin existed very early is beyond doubt: Herodotu
Klein's labdanum article says exactly what the arrow says — 'Pers. ladan is an Arabic loan word' (KLN_1966.txt line 20927) — but it stands on leaf 459 of the 1966 tw
Klein 1966 p.874 s.v. 'leave, tr. and intr. v.' (KLN_1966.txt offset 5370317, immediately before the page mark 875): 'ME. leven, fr. OE. lǣfan ... rel. to OE. lāf ..
Klein p.887 s.v. 'life, n.' (running head 'lifer lilac 888' follows): 'ME. lif, fr. OE. līf, rel. to ON. líf “life, body” ... prop. “continuance, perseverance”, fr. 
Klein p.899 (the entries 'live, intr. and tr. v.' and 'liver, n., secreting organ' both stand just after the page mark 899): 'live ... fr. OE. libban, lifian ... fr.
Klein 1966 s.v. lizard (p.899 f.) and leg (p. c.877)
Klein 1966 s.v. leg (KLN_1966.txt offset 5382653, p. c.877)
Klein 1966 s.vv. locust (p.902) and lizard (p.899 f.)
Klein (KLN_1966.txt leaf 231, s.v. deliver): 'OF. delivrer ... fr. VL. dēlīberāre, fr. de- and līberāre, to set free, fr. līber, free'; Klein s.v. Latvia (leaf 467):
Klein (p. 59) gives the same link: English Amazon '— L., fr. Gk. Ἀμαζών'.
Klein, 'Amazon, n., name of the largest river in the world in volume — Sp. Amazonas, from prec. word', i.e. the reference the chart gives (KLN:59) states precisely t
Klein p. 924: 'maid, n. — Shortened fr. maiden'; 'maiden, n. — ME. meiden, fr. OE. mægden, dimin. of mægeð, mægð, \
Klein's and only Klein's: 'fr. Arab. marqashithā, fr. Pers. marqashishā' (p. 937). Everything else reverses it. Wiktionary: Arabic مَرْقَشِيتَا 'from Aramaic marqəšī
Klein p. 937 gives exactly this step ('fr. Sp. marcaxita (ModSp. marcasita), fr. Arab. marqashithā'), Devic p. 157 lists 'Esp. marquesita, autrefois marcaxita', and 
Klein (p. 937), whom the chart follows, has ML marchasita 'fr. Sp. marcaxita', whereas Wiktionary derives Medieval Latin marchasita straight from Arabic مَرْقَشِيتَا
Klein p. 937: 'F. marcassite, fr. ML. marchasita'; Devic p. 157 heads his article 'Marcassite. Pyrite de fer' and lists the same Latin and Romance forms; Lokotsch 13
Klein p. 937 routes it 'F. marcassite, fr. ML. marchasita' as the chart does; Wiktionary has 'From Medieval Latin marchasita et al., from Arabic مَرْقَشِيتَا (marqaš
Klein 1966 s.v. Elohim (KLN_1966.txt line 12865, leaf 278): 'Elohim, n., one of the names of God in the Bible. — Heb. Elōhīm, pl. of Elōah, \
Klein s.v. Elohim (p.505): '…Arab. ilāh, with the article Allāhu (see Allah)' — i.e. Allāh = al- + ilāh, Nourai's arrow exactly. Klein's own Allah entry (p.51) repea
Klein p.51 and the AHD both simply give 'Arab. Allāh, contraction of al-ilāh'.
Klein's two-pages-per-leaf scan): 'Allah, n., Mohammedan name of the Supreme Being. — Arab. Allāhu, contraction of al-ilāhu, fr. al-, \
Klein s.v. benzoin (KLN_1966.txt line 4766, leaf 98): 'benzoin, n., a balsamic resin. — F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first sylla
Klein: 'F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first syllable having been mistaken for the def. article), fr. Arab. lubān jāwī'; Hobson-Jo
Klein p.164, Devic p.63, Lokotsch 1332 and Hobson-Jobson p.86 (see consulted).
Klein gives both: 'benzoin… F. benjoin, fr. Sp. benjui… fr. Arab. lubān jāwī' and 'benzene… Fr. Benzin, a name coined by the German chemist Eilhardt Mitscherlich (17
Klein 1966 vol. I p.2 (KLN_1966.txt form-feed leaf 13, the leaf that carries printed pp.2-3) runs 'abase … abash … abasia … abate … abatis … abattoir … abb … abba … 
Klein DOES support the claim, but at another page: s.v. amnic (KLN_1966.txt line 2497, leaf 45 ≈ printed p.67): 'L. amnicus, fr. amnis, \
Klein p.137 ('so called from Lajward, a place in Turkestan, mentioned in Marco Polo's Travels'), Skeat s.v. Azure ('the mines of Lajwurd, where the lapis lazuli was 
Klein 1966 p.137 (KLN_1966.txt line 4204 = leaf 84; the running head of the preceding leaf reads 'axo- / azyme / 136 / 137', so the azure entry stands on the spread 
Klein p.137 and Skeat s.v. Azure derive the stone-name from the place: 'so called from Lajward, a place in Turkestan, mentioned in Marco Polo's Travels' (Polo, Bk I,
```


## [2026-09-07T18:19:41.905Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(544,590):\n    lv=leaves[i]\n    nums=re.findall(r'\\b(1[01]\\d\\d)\\b',lv)\n    print(i, nums[:6], lv.strip()[:60].replace('\\n',' '))\nEOF",
 "description": "Find page numerals in Klein leaves 544-590"
}
```


### [2026-09-07T18:19:43.278Z] TOOL RESULT

```
544 ['1015', '1016', '1017'] like  a  mummy,  to  dry  up,  shrivel.  — F.  momifier,  co
545 [] urrain’,  which  also  derive  fr. VL.  *morire.  Cp.  murri
546 ['1021'] appoint,  something;  to  have  room; to  be  able;  to  be 
547 ['1100', '1022'] ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  bec
548 [] d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj. 
549 [] l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  
550 ['1028'] B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  
551 [] of  coconut  shells, narial,  adj.,  pertaining  to  the  na
552 ['1033'] us,  ‘birth,  des¬ cent,  origin,  race,  sort,  kind,  clas
553 ['1034', '1035'] d  of  navis,  ‘ship’,  and agere,  ‘to  set  in  motion,  d
554 ['1036'] n.,  that  part  of  the  body  which  joins  the head  to  
555 ['1039'] MF.  (=  F.)  negatif  (fern. negative),  fr.  OF.  negatif,
556 ['1040'] for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Got
557 [] .  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it, 
558 [] �blessed’.  See  nostal¬ gia. Nestorian,  adj.,  1)  pertain
559 ['1046'] corpuscles  that is  neither  oxyphile  nor  basophile');  a
560 [] s  (in  a  certain  manner); one  who  deals  (with  a  cert
561 [] �. Nilotic,  adj.,  pertaining  to  the  Nile,  the  Nile  r
562 [] niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-
563 [] See  nodule  and  -ous. nodus,  n.,  knot;  difficulty,  com
564 ['1054', '1066'] before  the  ides’,  and  cp. words  there  referred  to. no
565 ['1056', '1057'] orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n. Norn, 
566 ['1058', '1059'] Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also 
567 ['1080', '1060', '1061'] alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  o
568 ['1062', '1063'] numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  
569 ['1064'] ), contraction  of  *noven-dinom,  ‘nine  days’,  fr. novem,
570 ['1066'] sexual  desire  in  women (med.)  —  Medical  L.,  compounde
571 ['1067', '1068'] o  put  before’.  It derives  fr.  L.  objectus,  pp.  of  o
572 ['1070', '1071'] elligible’,  orig.  ‘cover¬ ed’,  formed  fr.  ob-  and  l.-
573 ['1072'] ontradiction  in  itself.The  name  should be  foramen  obtu
574 [] eaning  lit. ‘something  sharp-edged’,  and  rel.  to  ocris
575 [] OHG.  ort,  ‘point  (esp.  of  a  weapon  or  a tool),  angl
576 [] e  ecology, oecumenic,  oecumenical,  adjs.  —  See  ecumeni
577 [] The  sense  development  is due  to  a  confusion  of  the  
578 ['1081'] the  ending  see  suff. -aceous. Olethreutidae,  n.  pi.,  a
579 ['1031', '1082', '1083'] ding, portentous,  ominous',  fr.  omen,  gen.  ominis.  See
580 ['1084', '1085'] pretation  of  dreams. oneiromancy ooze oneiromancy,  adj., 
581 ['1086'] aining  eggs  (zool.)  — ModL.  ootheca,  compounded  of  oo
582 ['1088', '1089'] ;  anything  soothing;  tr. opinable 1088 1089 v.,  to  trea
583 [] ts.  —  F.  opticien,  fr.  ML.  optica.  See next  word  an
584 ['1093'] ng  to  an  orator’,  fr.  orator.  See  orator, oratory,  n
585 ['1094', '1095'] coin,  prop,  subst.  use  of  the  adj. aureus,  ‘of  gold,
586 ['1096'] s  American  birds  of  the  family Icteridae.  —  F.  oriol
587 [] �orris  root’,  which  is  identical  with  Gk. Epecoe,  gen
588 [] vowel  osche-,  combining  form meaning  the  ‘scrotum’.  — 
589 ['1103'] a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff
```


## [2026-09-07T18:19:52.291Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 255 (printed 234)\"\nawk 'BEGIN{RS=\"\\f\"} NR==256' HRN.txt | head -60",
 "description": "Horn p.234"
}
```


### [2026-09-07T18:19:53.879Z] TOOL RESULT

```
=== HRN leaf 255 (printed 234)
- 234 —
nicht 'äumand. Gewöhnlich wird allerdings phlv. ö
im Wortinnern nur durch den einfachen «<- Strich
ausgedrückt, z. B. awös, anösak, vergl. auch arj-
ömandlh in Spiegel' s Glossar, S. 366.
1044. iiene *Mutter', nicht schriftgemäss, aber dialektisch
sehr gebräuchlich.
ai. nand' 'Mutter : alb. nane etc. (G. Meyer, 297).
bei. vergl. nänö, nana *Grossvater' , nam *Gross-
mutter' (LW. No. 183) ; §iyn. sangl. nan, wb,/, nan
*Mutter.
Vergl. Delbrück, Verwandtschaftsnamen, 73.
V
1045. wf>, nev (Sahn. I, 130 Vers 19) neu*.
g. nove\ Kä§. K. nav in navhdr ^frühzeitige Frucht'.
aw. nava- neu'; phlv. navak bezw. nök (päz, nö);
ai. ndva^; arm. nor (H. No. 222).
kurd. nu *neu'; af/. aau, navai; oss. d. näväg^ t.
noog (194); bei. nök^ n. nöx (auch *Mond') (272); si/n.
ndu^ sar. nüj,
1046. neva^terij tiuvä/ten *singen; schmeicheln', Praes.
neva^-entj neväzis,
ni -+ l/"£?öfc-, im Indischen reden, sprechen;
schmähen'.
1047. newäde ^Enkel*, newäse, newa (vergl. newäzade),
neblre, nehtr (Öähn. I, 119 Vers 995^)).
ap. napat' 'Enkel'; aw. napat-; ai. ndpat^.
kurd. nevT, nevü^ nehvö 'Enkel*; afy. LW. nwasai;
bei. LW. nawasay (255) ; wa/. napüs^ sar. nabüs, §iyn.
naböSj nebös.
Gegen Leumann's Etymologie von indog. nepöt-,
neptf' als *Waise* (Festgruss an 0. von Böhtlingk,
S. 77) spricht sich z. B. Delbrück, Verwandtschaf tsn.
125 folg. aus; dafür von Bradke, GGA. 1890, S. 909.
1048. nuväzdeh 'neunzehn*.
aw. navadasa- neunzehnter; phlv. naväcdahum^);
ai. ndvadasa 'neunzehn .
^) Vullers s. v. Kaku hat aus dem FS sinnlos benesre,
2) VerKl. Seite 128 Note 6.
```


## [2026-09-07T18:20:05.233Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ORANGE\\|^NARANGI\\|NARANGI\\|Naranga\\|nāranga\\|naranga\" HJB.txt | head -20\necho \"=== SKT orange\"\ngrep -n \"^ORANGE\" SKT.txt\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nimport re\nfor i,l in enumerate(lines,1):\n    if l.startswith('ORANGE'):\n        pos=sum(len(x)+1 for x in lines[:i-1]); print('leaf',txt[:pos].count('\\f'),'printed',txt[:pos].count('\\f')-20)\n        print('\\n'.join(lines[i-1:i+6]))\n        break\nEOF",
 "description": "Hobson-Jobson + Skeat orange"
}
```


### [2026-09-07T18:20:06.591Z] TOOL RESULT

```
15974:ORANGE.
15976:ORANGE.
15986:ORANGE.
=== SKT orange
```


## [2026-09-07T18:20:09.889Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:15973])\nprint('leaf',txt[:pos].count('\\f'))\nprint('\\n'.join(lines[15960:16060]))\nEOF",
 "description": "Hobson-Jobson ORANGE entry"
}
```


### [2026-09-07T18:20:11.695Z] TOOL RESULT

```
leaf 687
2  s
quantity  as  is  expended,   and  how  much
may  be  eaten  every  day !
•  •  •  «  «
"  0.  .  .  .  that  which  I  call  of  Cambaia come  for  the  most  part  from  one  territory which  is  called  Malvi  {Molwd),  ...  I  knew  a secretary  of  Nizamoxa  (see  inZAMALUCO), a  native  of  Coracon,  who  every  day  eat  three t6lku  (see  TOLA),  or  a  weight  of  10^  cru- zadoe  .  .  .  though  he  was  a  well  educated man,  and  a  great  scribe  and  notary,  he  was always  dozing  or  sleeping;  yet  if  you  put him  to  business  he  would  speak  like  a  man of  letters  and  discretion ;  from  this  you  may see  what  habit  will  do"—Oarcia,  158v  to 155v.
.  1568.—"  I  went  then  to  Cambaya  .  .  . and  there  I  bought  60  parcels  of  Opium, which  cost  me  two  thousand  and  a  hundreth duckets,  every  ducket  at  foure  shillings  two pence." — Master  C.  Frederike,  in  Hakl,  ii. 371.  The  original  runs  thus,  showing  the looseness  of  the  translation :  " .  .  .  comprai sessanta  vuin  d'Anfion,  che  mi  cost6  2100 ducati  serafini  (see  XEBAFINE),  che  a nostro  conto  possono  valere  5  lire  I'vno." — In  Jtamusio,  iii.  396v.
1598.— "Amfion,  so  called  by  the  Portin- g^les,  is  by  Arabiaps,  Mores,  and  Indians called  AflLon,  in  latine  Opio  or  Opium.  .  .  . The  Indians  use  much  to  eat  Amjion,  .  .  . Hee  that  useth  to  eate  it,  must  eate  it  day  lie, otherwise  he  dieth  and  consumeth  himselfe .  .  .  likewise  hee  that  hath  never  eaten  it, and  will  venture  at  the  first  to  eate  as  much as  those  that  dayly  use  it,  it  will  sUrely  kill him.  .  .  ."— XtVucAotew,  124  ;  [Hak.  Soc. ii.  112].
fc.  1610.— "  Opium,  or  as  they  (in  the Maldives)  call  it,  Apidtm"  —  Pyrard  de Laval,  Hak.  Soc.  i.  19«5.
[1614. — "The  waster  washer  who  to  get Amman  hires  them  (the  cloths)  out  a month."— -Fotfter,  Letters,  ii.  127.
[1615.—" .  . .  Coarse  chintz,  and  ophyan." —Ibid.  iv.  107].
1638. — "  Turcae  opium  experiuntur,  etiam in  bona  quantitate,  innoxiam  et  confer- tativum  ;  adeo  ut  etiam  ante  praelia  ad fortitudinem  illud  sumant ;  nobis  vero,  nisi in  parvft  quantitate,  et  cum  boms  cor- rectivis  lethale  est." — Bacon,  H,  Vitae  et Mortis  (ed.  Montague)  x.  188.
1644.  —  "The  principal  cause  that  this monarch,  or  rather  say,  this  tyrant,  is  so powerful,  is  that  he  holds  in  his  territories, and  especially  in  the  kingdom  of  Cambaya, those  three  plants  of  which  are  made  the ATifla.Tn,  and  the  anil  (see  ANILE),  and that  which  gives  the  Algodam**  (Ck>tton).~~ Bocarro,  MS.
1694.— "This  people,  that  with  amphioen or  opium,  mixed  with  tobacco,  drink  them- selves not  merely  drunk  but  mad,  are wont  to  fall  furiously  upon  any  one  whom they  meet,  with  a  naked  krit  or  danger  in the  hand,  and  to  stab  him,  though  it  be  but a  child,  in  their  mad  passion,  with  the  cry of  Amock  (see  A  MuCE),  that  is  'strike dead, 'or 'fallen  him.'  .  .  .  "—Valentijn,  iy» (Qhina,  &o.)  124.
ORANGE.
642
ORANGE.
1726.— "It  wiU  hardly  be  believed  .  .  . that  Java  alone  consumes  monthly  850 packs  of  opium,  each  being  of  136  eatit  (see CATTY),  though  the  E.  I.  Company  make 145  catis  out  of  it.  .  .  ."— Fafentyw,  iv.  61.
1727.—"  The  Chiefs  of  Caleout,  for  many years  had  vended  between  500  and  1000 chests  of  Bengal  Ophiuni  yearly  np  in  the inland  Coontries,  where  it  is  very  much used."— il.  Hamilton,  i.  815;  fed.  1744,  i. 817  •«?.].
1770.—"  Patna  ...  is  the  most  celebrated place  in  the  world  for  the  cultivation  of opiimi.  Besides  what  is  carried  into  the imand  parts,  there  are  annually  8  or  4000 chests  exported,  each  weighing  800  lbs.  .  .  . An  excessive  fondness  for  opium  prevails in  all  the  coimtries  to  the  east  of  India. The  Chinese  emperors  have  sni>pre88ed  it in  their  dominions,  by  condemning  to  the flames  every  vessel  that  imports  this  species of  poison."- /Zayna^  (tr.  1777),  i.  424.
OBANGE,  s.  A  good  example  of plausible  but  entirely  incorrect  ety- mology is  that  of  orange  from  Lat. aurantivmi.  The  latter  word  is  in  fact an  ingenious  medieval  fabrication. The  word  doubtless  came  from  the Arab,  naranj,  which  is  again  a  form of  Pers.  ndrang,  or  ndrangl,  the  latter being  still  a  common  term  for  the orange  in  Hindustan.  The  Persian indeed  may  be  traced  to  Skt.  ndgaranga, and  ndrangoj  but  of  these  words  no satisfactory  etymolo^cal  explanation has  been  given,  and  they  have  perhaps been  Sanscritized  from  some  southern term.  Sir  W.  Jones,  in  his  article  on the  Spikenard  of  the  Ancients,  quotes from  Dr.  Anderson  of  Madras,  "a  very curious  philological  remark,  that  in the  Tamul  dictionary,  most  words beginning  with  nar  have  some  relation to  fragrance ;  as  naruJeeradu,  to  yield an  odour  ;  ndrtum  pillei,  lemon-grass  ; ndrtdy  citron ;  ndrta  manum  (read mdrum),  the  wild  orange-tree ;  ndrum paneiy  the  Indian  jasmine ;  ndrum cUleri,  a  strong  smelling  flower ;  and ndrtt^  which  is  put  for  nard  in  the Tamul  version  of  our  scriptures."  (See As.  Res.  vol.  ii.  414).  We  have  not been  able  to  verify  many  of  these Tamil  terms.  But  it  is  true  that  in both  Tamil  and  Malayalam  nani  is '  fragrant.'  See,  also,  on  the  subject  of this  article,  A.  E.  Pott,  in  Lassen's ZefUschrift  f.  d.  Kunde  des  Morgmlandes, vii.*114  seqq.
The  native  country  of  the  orange is  believed  to  be  somewhere  on  the northern    border  of    India.     A  wild
orange,  the  supposed  parent  of  the cultivated  species,  botn  sweet  and bitter,  occurs  in  Garhwal  and  Sikkim^ as  well  as  in  the  ESjsia  (see  0088YA> country,  the  valleys  of  which  last are  still  abundantlv  productive  of excellent  oranges.  jfSee  WaU,  Earn. Diet.  ii.  336  seqq.]  It  is  believed  that the  orange  first  known  and  cultivated in  Europe  was  the  bitter  or  Seville orange  (see  Banbury  and  FUidtiger. 111-112).
From  the  Arabic,  Byzantine  Greek got  v€pdyTi:iop,  the  Spaniards  naranja^ old  Italian  narancia,  the  Portuguese laranjOy  from  which  last,  or  some similar  form,  by  the  easy  detachment of  the  I  (taken  probably,  as  in  many other  instances,  for  an  articleX  we  have the  ItaL  arancioy  L.  Latin  auranUum^ French  orange,  the  modification  of these  two  being  shaped  by  aurum  and or.  Indeed,  the  quotation  from  Jacques de  Vitrv  possibly  indicates  that  some form  like  al-ara/ngi  may  have  been current  in  Syria.  Perhaps,  however, his  phrase  ao  indigents  ntmcupantur may  refer  only  to  the  Frank  or  quasi- Frank  settlers,  in  which  case  we  should have  amon^  them  the  birthplace  of our  word  m  its  present  form.  The reference  to  this  passage  we  derived in  the  first  place  from  HehA,  who ^ves  a  most  interesting  history  of  the mtroduction  of  the  various  species  of citrus  into  Europe.  But  we  can hardly  think  he  is  rifht  in  supposing that  the  Portuguese  first  brought  the sweet  orange  (Uitrus  aurantium  dulce) into  Europe  from  China,  c.  1548.  No doubt  there  may  have  been  a  re- introduction  of  some  fine  varieties  at that  time.*  But  as  early  as  the  lie- ginning  of  the  14th  century  we  find Abulfeda  extoUinff  the  fruit  of  Cintra. His  words,  as  rendered  by  M.  Reinaud, run  :  "  Au  nombre  des  dependances  de Lisbonne  est  la  ville  de  Schintara ;  a Schintara  on  recueille  des  pommes admirables  pour  la  grosseur  et  le  gout* (244 1).  That  these  pommes  were  the famous  Cintra  oranges  can  hardly  be
*  There  seems  to  have  been  great  osciUatlou  of traffic  iu  this  matter.  About  1878,  one  of  the present  writers,  then  resident  at  Falermo,  sent, in  compliance  with  a  request  ftx>m  Lahore,  a  col- lection of  plants  of  many  (about  forty)  varietiw of  cUrut  cultivated  In  Sicily,  for  introduction  into the  Pui\ialx  This  despatch  was  much  aided  by the  kindness  of  Prof.  Todaro,  in  chanm  of  th« Royal  Botanic  Oarden  at  Palermo.
t  In  Reiske's  version  "poma  stupendae  molis et  excellentissima."— .BuscAtii^**  MagaHn^  iv.  na
ORANGE.
643
OBANG-OTANG.
doubted.  For  Baber  (Autobiog.  328) describes  an  orange  under  the  name of  Sanqta/rah,  which  is,  indeed,  a  recog- nised Persian  and  Hind,  word  for  a species  of  the  fruit.  And  this  early propagation  of  the  sweet  orange  in Portugal  would  account  not  only  for such  wide  diffusion  of  the  name  of Oiniray  but  for  the  persistence  with which  the  alternative  name  of  PortugaU has  adhered  to  the  fruit  in  question. The  familiar  name  of  the  large  sweet orange  in  Sicily  and  Italy  is  portogallo, and  nothinjg  else ;  in  Qreece  ToproyaXia, in  Albanian  vrotokaUy  among  the Kurds  |K>r^^^  whilst  even  colloquial Arabic  has  hurtukdn.  The  testimony of  Mas'udT  as  to  the  introduction  of the  Orange  into  Syria  before  his  time (c.  A.D.  930),  even  if  that  were  (as  it would  seem)  the  Seville  orange, renders  it  quite  possible  that  better qualities  should  have  reached  Lisbon or  been  developed  there  during  the Saracenic  occupation.  It  was  indeed suggested  in  our  hearing  by  the  late Sir  Henrv  M.  Elliot  that  sangtarah might  be  interpreted  as  sang-tar,  *  green stones '  ^or  in  fact  *  moist  pips ')  ;  but we  hardly  think  he  would  have  started this  had  the  passage  in  Abulfeda  been brought  to  his  notice.  [In  the  Ain (ed.  Gladwin,  1800,  ii.  20)  we  read: **  Sircar  Silhet.  .  .  .  Here  grows  a delicious  fruit  called  Soontara,  in colour  like  an  orange,  but  of  an oblong  form."  This  passage  reads  in Col.  Jarrett's  translation  (ii.  124) : "There  is  a  fruit  called  Simtarah in  colour  like  an  orange  but  large and  verv  sweet."  Col.  Jarrett  dis- putes the  derivation  of  Sangtarah from  Ointra,  and  he  is  followed  by Mr.  H.  Beveridge,  who  remarks  that Humayun  calls  the  fruit  Sanatra. Mr.  Beveridge  is  inclined  to  think that  Santra  is  the  Indian  hill  name  of the  fruit,  of  which  Sangtarah  is  a  cor- ruption, and  refers  to  a  village  at  the foot  of  the  Bhutan  Hills  callea  Santra- bdrty  because  it  had  orange  groves.]
A.D.  c.  930.— "The  same  may  be  said  of the  orange- tree  {Sfu^r-ul-nSLTUij)  and  of  the roond  citron,  which  were  brought  from India  after  the  year  (a.h.)  300,  and  first mwn  in  'Oman.  Thence  they  were  trans- planted to  Basra,  to  Irak,  and  to  Syria .  .  .  but  they  lost  the  sweet  and  pene- trating odour  and  beauty  that  they  bad  in India,  havinff  no  longer  the  benefits  of  the climate,  soil,  and  water  peculiar  to  that coantr7.''~ifa{r'il(ii,  ii.  488-9.
c.  1220k — "In  panns  autem  arboribus quaedam  creacunt  alia  poma  citrina,  minons quantitatis  frigida  et  acidi  seu  pontici {bitter)  saporis,  quae  poma  omunB  ao  indi- flrenis  nuncupantur." — Jacobiu  vitriaeut,  in Bongari,  These  were  apparently  our  Seville oranges.
c.  1290.— "In  the  18th  of  Edward  the first  a  large  Spanish  Ship  came  to  Ports- mouth ;  out  of  the  cargo  of  which  the  Queen bought  one  frail  (see  FBAZALA)  of  Seville fiffs,  one  frail  of  raisins  or  grapes,  one  bale of  dates,  two  hundred  and  thirty  pome- granates, fifteen  citrons,  and  seven  oranges {Poma  de  ortiig9).**—Manneri  and  Hauaehofd Expen»ea  of  England  in  the  I3th  and  15th Centuries,  Koxb.  Club,  1841,  p.  xlviii.  The Editor  deigns  only  to  say  that  *  the  MS.  is in  the  Tower.*  [Prof.  Skeat  writes  j9  ser. Notes  and  Queries,  v.  821) :  "The  only  known allusion  to  oranges,  previously  to  1400,  in any  piece  of  English  literature  (I  omit  house- hold documents)  is  in  the  *  A  lliterative  Poems, ' edited  by  Dr.  Morris,  ii.  1044.  The  next reference,  soon  after  1400,  is  in  Lydgate's 'Minor  Poems,'  ed.  Halliwell,  p.  15.  In 1440  we  find  oronge  in  the  *  Promptorium Parvulorum,'  and  in  1470  we  find  orenges in  the  'Paston  Letters,*  ed.  Gairdner,  ii.  394."]
1481.— "Item  to  the  galeman  (galley  man) brought  the  lampreis  and  oranges . . .  iiijc^." —■Household  Book  of  John  D.  of  Norfolk, Roxb.  Club,  1844,  p.  38.
c.  1626.— "They  have  besides  (in  India) the  nftranj  [or  Seville  orange,  Tr.J  and  the various  fruits  of  the  orange  species.  ...  It always  struck  me  that  the  word  nAranJ  was accented  in  the  Arab  fashion ;  and  I  found that  it  really  was  so;  the  men  of  Bajour and  Siw&d  ctM  ndranj  n/lrank  "  (or  perhaps rather  nAiang).  —  Baber,  328.  In  this passage  Baber  means  apparently  to  say  that the  right  name  was  ndrang,  which  had  been changed  by  the  usual  influence  of  Arabic pronunciation  into  7idrar\j.
1883.— "Sometimes  the  foreign  products thus  cast  up  (on  Shetland )  at  their  doors  were a  new  revdation  to  the  islanders,  as  when  a cargo  of  oranges  was  washed  ashore  on  the coast  of  Deltin^,  the  natives  boiled  them  as a  new  kind  of  potatoes."  — <Sa<y.  Jteviett, July  14,  p.  57. •
OBANG-OTANG,  OBANG- OUTAN,  &c.  s.  The  great  man-like ape  of  Sumatra  and  Borneo ;  Simia Satyrus,  L.  This  name  was  first  used by  Bontius  (see  below).  It  is  Malay, drdng-utdn,  *homo  sylvaticus.'  Tne proper  name  of  the  animal  in  Borneo is  mias,  Crawfurd  says  that  it  is never  called  orang-utan  by  *the natives.'  But  that  excellent  writer  is often  too  positive— especially  in  his negatives !  Even  if  it  be  not  (as is  probable)  anywhere  a  recognised specific  name,  it  is  hardly  possible  that tne  name  should    not   be  sometimes
ORANG'OTANG,
644       ORANKAY,  ARANGKAIO.
applied  popularly.  We  remember  a tame  lioolack  belonging  to  a  gentle- man in  £.  Bengal,  wnicn  was  £abitu- ally  known  to  the  natives  as  jOffigll ddmly  literally  =  omnflr-uton.  [There seems  reason  to  believe  that  Crawfurd wafi  right  after  all.  Mr.  Scott  {Malayan Wards  in  Englisk,  p.  87)  writes  :  "  But this  particular  application  of  drang titan  to  the  ape  does  not  apiDear  to  be, or  ever  to  have  been,  familiar  to  the Malays  generally ;  Crawfurd  (1852)  and Swettennam  (1889)  omit  it,  Pijnappel says  it  is  *  Low  Malay,'  and  Klintert (1893)  denies  the  use  entirely.  This uncertainty  is  explained  by  the  limited area  in  wmch  the  animal  exists  within even  native  observation.  Mr.  Wallace could  find  no  natives  in  Sumatra  who 'liad  ever  heard  of  such  an  animal,' and  no  'Dutch  officials  who  knew anything  about  it.'  Then  the  name came  to  European  knowledge  more than  260  years  ago ;  in  which  time probably  more  than  one  Malay  name has  faded  out  of  general  use  or  wholly disappeared,  and  many  other  things have  happened."  Mr.  Skeat  writes : "  I  believe  Crawfurd  is  absolutely  right in  saying  that  it  is  never  called  Orang- utan by  the  natives.  It  is  much  more likely  to  have  been  a  sailor's  mistake or  joke  than  an  error  on  the  part  of the  Malays  who  know  better.  Through- out the  Peninsula  drana-utan  is  the name  applied  to  the  wild  tribes,  and though  tne  rnawas  or  Ttiias  is  known to  the  Malays  only  by  tradition,  yet in  tradition  the  two  are  never  con- fused, and  in  those  islands  where  the 'nuiwas  does  exist  he  is  never  called Oram^g-utan^  the  word  Orang  b^ing  re- served exclusively  to  describe  the human  species."]
1681.  — "  Loqui  vero  eos  easqae  posse layani  aiunt,  sed  non  velle,  ne  ad  labores cogantur ;  ridicule  meheroules.  Nomen  el induont  Onrang  Oatan^,  quod  'hominem silvae'  significat,  eosque  uasci  affirmant  e libidine  mulienim  Indarum.  quae  se  Simiis et  Cercopithecis  detestanda  libidine  uniunt." ^Bontii,  Hut.  Nai.  v.  cap.  32,  p.  85.
1668. — ^'Erat  autem  hie  8at3rrus  quad- rupes:  sed  ab  human&  specie  quam  prae se  fert,  vocatur  Indis  Onrang-outaii^ :  sive homo  silvestris."— ZieehM  de  MonttrU^  338.
[1701.  —  "  Orang  -  oatang  dve  Homo Sylvestris:  or  the  Anatomy  of  a  Pygmie compared  with  that  of  a  Monkey,  an  Ape, and  a  Man.  .  .  ." — Title  of  work  by  B,  Tyson (.Scott).]
1727. — "As  there  are  many  species  of wild  Animals  in  the  Woods  (of  Jaya)  there  is one  in  narticular  called  the  OnraiL-Oiiteiur-'' —A,  HamiUon,  u.  131 ;  [ed.  1744,  ii.  136^
1783.— "Were  we  to  be  driyen  out  of India  this  day,  nothing  would  remain  to tell  that  it  ha!d  been  possessed,  during  the inglorious  period  of  our  dominion,  by  any thing  better  than  the  onrang-outaaff  or  the tiger."— ^uriv,  Sp,  on,  Fox't  £.  India  Billy Works,  ed.  1852,  m.  468.
1802.— "Man,  therefore,  in  a  state  of nature,  was,  if  not  the  oorang-oataiig  of the  forests  and  moimtains  of  Asia  and Africa  at  the  present  day,  at  least  an animal  of  the  same  family,  and  very  nearly resembling  it" — RiUoti,  Etny  on  Ahstiin^nee from  Animal  Food,  pp.  13-14.
1811. — "  I  haye  one  slave  more,  who  was
f'lvon  me  in  a  present  by  the  Sultan  of Ontiana.  .  .  .  This  gentleman  is  Lord Monboddo's  genuine  Onui|:-<nitaiig,  which in  the  Malay  language  signifies  literally  itUd man,  .  .  .  Some  people  think  seriously  that the  oran-OUtang  was  the  original  patriarch and  progenitor  of  the  whole  Malay  raoe." —Lmd  Minio,  Diary  in  India,  268-9.
1868.— "One  of  my  chief  objects  .  .  . was  to  see  the  Oraiig-utan  ...  in  his native  haimts." — Wallace^  Malay  Archip.  39.
In  the  following  passage  the  term  is applied  to  a  tribe  of  men  :
1884.—"  The  Jaooons  belong  to  one  of  the wild  aboriginal  tribes  .  .  .  they  are  often styled  Oruig  Utan,  or  men  of  the  forest" — Cavenagkf  Rem.  qfan  Indian  Official^  293.
0BANKA7,   ARANGEAIO,  &c.
s.  Malay  Orang  kdya.  In  the  .Archi- pelago, a  person  of  distinction,  a  chief or  noble,  corresponding  to  the  Indian omrah;  literally  *a  rich  man,'  analo- gous therefore  to  the  use  of  rtche-homme by  Joinville  and  other  old  French authors.  [Mr.  Skeat  notes  that  the terminal  o  in  araogkaio  represents  a dialectical  form  used  in  Sumatra  and Java.  The  Malay  leader  of  the  Fa- hang  rising  in  1891-2,  who  was  sup- posed to  bear  a  charmed  life,  was called  by  the  title  of  Orang  Kdya Pahlawan  (see  PULWAUN).]
c.  1612.— "The  Malay  officers  of  state are  classified  as  1.  Bandahara;  2.  Ferdana Mantri;  3.  Pungkuiu  Bandari  ;  4.  the  chief Hulnbalana  or  champion  (see  OOLOO- BALLONG);  5.  the  Paramanirit;  6.  Orang Kavas ;  7.  CfuUriyas  (Kshatrivas) ;  8.  Seda Sidahs;  9.  BetUaroM  or  heralds;  10.  Hulu- halanas." — Sijara  Malayu,  in  J.  Ind.  ArdL
1618.— "The  nobler  Oiancajai  spend their  time  in  pastimes  and  recreatiODs,  in music  and  in  cook  fi^htuur,  a  royal  sport. ..." —Oodinho  de  Krtdm  f.  Slf.
ORGAN.
645
ORMUS,  ORMUZ,
1618.— *  *  An  Onn  Caya  oame  aboord,  and told  me  that  a  Citrra  Gurra  (see  CARACOA) of  the  Flemmings  had  aearohed  three  or fonre  Praws  or  Canoas  oonuning  aboord  vs with  Cloues,  and  had  taken  them  from them,  threatening  death  to  them  for  the next  offence."— iSam,  in  P%ax:has^  i.  848.
[  ,,  '* .  .  .  gave  him  the  title  of  Onn- caja  Pate,  which  is  white  or  clear  hearted lord."— i)a»t«r#,  LeUen,  i.  270.]
1615. — '*  Another  conference  with  all  the Airaakayot  of  Lugho  and  Cambello  in  the hills  among  the  bushes :  their  reverence  for the  King  and  the  honourable  Company." — Sainsbvayy  i.  420.
W[    „     "  Presented  by  Mr.  Ozwicke  to  the rankiaw."— ^01^,  LeUen^  iii.  96.
[  „  *'.  .  .  a  nobleman  called  Axon  Caie Hettam."— 7&ui.  iii.  128.]
1620. — "  Premierement  sur  vn  fort  gprand £lephant  il  y  auoit  vne  chaire  couuerte, dans  laquelle  s'est  assis  yn  des  principaux OrangcayM  on  Sei^eurs." — Beaulieu,  in 7%eveiiot*$  Collectiotiy  i.  49.
1711.— "Two  Pieces  of  Callico  or  Silk  to the  Shahander  (see  BHABUNDEB),  and  head Ozonkoy  or  Minister  of  State."— xx>Cityer,  86.
1727. — "As  he  was  entering  at  the  Door, the  Oraakay  past  a  long  Lance  through  his Heart,  and  so  made  an  end  of  the  Beast." — A.  MamUton,  ii.  97  ;  [ed.  1744,  ii.  96].
„  "  However,  the  reigning  King  not ezpectinff  that  his  Customs  would  meet with  such  Opposition,  sent  an  Oran^kajra aboard  of  my  Ship,  with  the  Linguist,  to know  why  we  made  War  on  him." — Ibid. 106;  [ed.  1744].
1784. — "Three  or  four  days  before  my departure,  Posally  signified  to  me  the  King meant  to  ccmfer  on  me  the  honour  of  being made  Knight  of  the  (3olden  Sword,  Onmg Kayo  deny  piddang  ma*  "  {orang  taya  ddri jMang  mat), — Forrest,  V.  to  Merguif  64.
1811. — "From  amongst  the  onui^T  kayas the  Sultan  appoints  the  officers  of  state, who  as  members  of  Coundl  are  called mwniri  (see  UUNTBEE,  MANDARIN)."— Marsdenj  H,  of  Sumatra,  350.
[ORGAN,  s.  An  Oriental  form  of nutrailleiise.  Steingass  {Did.  38)  has Pers.  arghcm,  arghoUy  from  tlie  Greek Spyapw,  *an  organ.'
1790. — "  A  weapon  called  an  organ,  which is  composed  of  about  thirty -six  gunbarrels no  joined  as  to  fire  at  once." — Letter  from De  Boiffne's  Camp  at  Mairtha,  dated  Sept. 18,  in  H.  ContpUm,  A  particular  Account  of  the Ewropean  Muitary  Aavtnturrrs  of  Hindustan. fromVIhi  to  1803,  p.  61.]
OBISSA,  n.p.  [Skt.  OdnUktra, *  the  land  of  the  Odras'  (see  OOBIYA). The  word  is  said  to  be  the  Prakrit form  of  lUtarOy  'north,'  as  applied  to the  N.  part  of  KaUnga.]  The  name of  the  ancient  kingdom  and  modem
province  which  lies  between    Bengal and  the  Coromandel  Coast.
1616.— **  Kingdom  of  Orisa.  Further  on towards  the  interior  there  is  another  king* dom  which  is  conterminous  with  that  of Narsynga,  and  on  another  side  with  Ben- gala,  and  on  another  with  the  great  King- dom of  Dely.  .  .  ." — Barbota,  in  Lisbon  ea. 806.
c.  1568.— "Orisa  fu  gik  yn  Regno  molto bello  e  securo  .  .  .  sina  che  regnb  il  suo  R^ legitime,  c^uaX  era  Gentile."— Cef.  Federiei, JULmusio,  iii.  392.
[c.  1616.— "Vdoia,  the  Chief  e  Citty  oaUed lekanat  (Jnggnmant)."— ^S^ir  T,  Roe,  Hak. Soc.  u.  538.]
0BME8INE,  s.  A  kind  of  silk texture,  which  we  are  unable  to  define. The  name  suggests  derivation  from Ormus.  [The  Draper^s  Diet,  defines ''Annozeeii,  a  stout  silk,  almost  in- variably  black.  It  is  used  for  hat- bands and  scarfs  at  funerals  by  those not  family  mourners.  Sometimes  sold for  making  clergymen's  gowns."  The N.E.D.  S.V.  Armozeen,  leaves  the  ety- mology doubtful.  The  Stanf.  Diet, gives  Ormimxie,  '^a  fabric  exported from  OrmiLZ."]
c.  1566.—".  .  .  a  little  Island  called Tana,  a  place  very  populous  with  Portugala, Moores  and  Gentiles:  these  have  nothing but  Rice  ;  they  are  makers  of  Axmesie  and weavers  of  girdles  of  wooU  and  bumbast.'* —Caei.  Fre£aricke,  in  Hdkl.  ii.  344.
1726.  —  "  VeWet,  Damasks,  Axmosyn, Sattyn."— FaAwi/i>,  v.  183.
OBMUS,  OBMUZ,  n.p.  Properljr Hurmuz  or  Hurmuz^  a  famous  mari- time city  and  minor  kingdom  near  the mouth  of  the  Persian  Gulf.  The original  place  of  the  city  was  on  the northern  shore  of  the  Gulf,  some  30 miles  east  of  the  site  of  Rindar  Abbas or  Gombroon  (q.v.) ;  but  about  a.d. 1300,  apparently  to  e8caT)e  from  Tartar raids,  it  was  transferrea  to  the  small island  of  Gerun  or  Jerun,  which  may be  identified  with  the  Organa  of Nearchus,  about  12  m.  westward,  and five  miles  from  the  shore,  and  this was  the  seat  of  the  kingdom  when first  visited  and  attacked  by  the Portuguese  under  Alboquerque  in 1606.  It  was  taken  by  them  about 1B15,  and  occupied  permanently (though  the  nominal  reign  of  the native  kings  was  maintained),  until wrested  from  them  by  Shah  'Abbas, with    the    assistance    of    an    English
ORMUS,  ORMUZ,
646
OROMBARROS.
squadron  from  Surat,  in  1622.  The place  was  destroyed  by  the  Persians, and  the  island  has  since  remained desolate,  and  all  but  uninhabited, though  the  Portuguese  citadel  and water-tanks  remain.  The  islands  of Hormuz,  Eishm,  &c.,  as  well  as  Ban- dar 'Abbas  and  other  ports  on  the coast  of  Kerman,  had  been  held  by the  Sultans  of  Oman  as  fiefs  of  Persia, for  upwards  of  a  century,  when  in 1854  the  latter  State  asserted  its dominion,  and  occupied  those  places in  force  (see  Badger's  Imams  of  Omdn, &c.,  p.  xciv.).
B.O.  c.  325.—"  They  weighed  next  day  at dawn,  and  after  a  course  of  100  stadia anchored  at  the  mouth  of  the  river  Anamis, in  a  country  called  Hannoieia."— ^rruz^i, Vauaae  of  Nearchta.  ch.  zxziii.,  tr.  by M'Orindle,  p.  202. -  c.  A.D.  160. — (on  the  coast  of  Cannania}
'Apfioi^w  dxpov/'
PtoL  VI.  viii.  5. o.  540. — At  this  time  one  Gkibriel  is  men- tioned as  (Nestorian)    Bishop  of   Hormux (see  Attemanij  iii.  147-8).
c.  655. — "Nobis  .  .  .  visum  est  nihil- ominus  velut  ad  sepulchra  mortuorum, quales  voa  esse  video,  geminos  hosoe  Dei Saoerdotes  ad  vos  allegare ;  Theodorum videlicet  Episcopum  Hormmdadschir  et Oeorgium  Episcoi>um  Susatrae."  — Syriac Letter  of  the  Patriarch  Jen^abuSy  ibid.  133.
1298. — "When  you  have  ridden  these  two ^ays  you  come  to  the  Ocean  Sea,  and  on  the shore  you  find  a  City  with  a  harbour,  which  is called  Honnos."— Ji/arco  Polo,  Bk.  i.  ch.  xix.
o.  1830.—" ...  I  came  to  the  Ocean  Sea. And  the  first  city  on  it  that  I  reached  is called  Ormea,  a  city  strongly  fenced  and abounding  in  costly  wares.  The  city  is  on an  island  some  five  miles  distant  from  the main ;  and  on  it  there  growv  no  tree,  and there  is  no  fresh  water.  '—/Vior  Odaric,  in CcUkay,  &c.,  56.
c.  1331.—"  I  departed  from  'Oman  for  the country  of  HonnQS.  The  city  of  Hormus stands  on  the  shore  of  the  sea.  The  name is  also  called  Moghist&n.  The  new  city  of Rormxa  rises  in  face  of  the  first  in  the middle  of  the  sea,  separated  from  it  only by  a  channel  3  parasangs  in  width.  We arrived  at  New  aormnx,  which  forms  an island  of  which  the  capital  is  called  Jaraun. ...  It  is  a  mart  for  Hind  and  Sind."— Ibn  Baiuta,  ii.  230.
1442.— "OrmilB  (qu.  BurmiUf),  which  is now  called  Djerun,  is  a  port  situated  in  the middle  of  the  sea,  and  which  has  not  its «qual  on  the  face  of  the  globe." — Abdttr- razzdkf  in  India  in  X  V.  Cent,  p.  5.
o.  1470.— "Honniu  is  4  miles  across  the Vater.  and  stands  on  an  Island." — AUum. A^Mtin,  ibid,  p.  8.
1508. — "Habitant  autem  ex eonun  (Fiao- oorum)  gente  homines  fere  viginti  in  urbe Cananoro:  ad  quoe  profeoti,  post<^uam  es HoxmlBda  urbe  ad  eam  Indoram  avitatem Cananorum  venimus,  signifioavimuB  illis  noa esse  Christianoa,  noetnmqne  oonditioiMai et  gradum  indicavimus;  et  ab  illis  magno cum  gaudio  susoepti  sumus.  .  .  .  EonuuMm autem  Francorum  regio  Portagallus  vocKtor, una  ex  Francorum  regionibos ;  eorumque  Ktx. Emanuel  appellatur;  Enunanuelem  oramaa ut  ilium  custodiat." — Letter  from  Nedorian^ Bishopt  on  Mission  to  India,  in  Auewtam^ iii.  591.
1505. — "In  la  bocha  di  qneeto  mare  (di Persia)  h  vn  altra  insula  chiamata  Afpnmum^ done  sono  perle  infinite :  (e)  caualh  che  per tutte  quelle  parti  sono  in  gran  precio.  — Letter  of  K,  Emanuel,  p.  14.
1672.— "  Mas  v6  a  ilia  Gterum,  oomo  disoobre
O  que  fasem  do  tempo  oe  intervallos ;
Que  da  cidade  Axmuia,  que  alii  esfceve
Mia  o  nome  despois,  e  gloria  teve.**
aiM^x.108.
By  Burton :
```


## [2026-09-07T18:20:31.150Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT orange\"\ngrep -n -i \"orange\" SKT.txt | head -10\necho \"=== IEC nor/anor\"\ngrep -n \"^nor-\\|^n[oō]r\\|^anor\\|^ānor\\|juicy\" IEC.txt | head -20\necho \"=== IEC page 1645 region: find leaf\"\ngrep -n \"Page(s)\" /dev/null",
 "description": "Skeat orange, Mann nor/anor"
}
```


### [2026-09-07T18:20:32.492Z] TOOL RESULT

```
=== SKT orange
7926:Orange,  Granite  :  see  Oroln.
12832:became  *r^t^  by  a  popular  cty- V  fraa  ffr,  Kotd.  Cf.  Span,  tuxranja, |^£e.  ••  llal.  aramcio^  an  orange.  — itinmj,  nSrinj.  mdrgn^,  an  orange. to  PcT».  n<jV,  a  pomegranate. ion.  Orator ;  see  Oral. (F.  —  L  )  I'.  oede.^L.  er^em,  ace. »,  ■  circle,  kpfaexe.
21824:Zest.    I F.  -  L.  -  Gk.)      Fonoerly  a  «Wp of  orange  or  lemon-peel,  used  for  fla' drinks ;  hence,  something  that  gives or  simply  a  reli»h.  — F.  ust,  'tneih whereby  the  kenicll  of  a  walnut  is Cot.;   hence,  a  slice  of  lemoupecL  ^ schisttu,   schistos,  Itt.   cleft,  divide'
23620:Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
=== IEC nor/anor
9767:norant, lewd’, fr. a type *leuitós). (A variant '
11713:nor, lesť; cf. also non, noenu(m) (fno, not, fr. *ne-ue-ne E *ne-ge-num); Alb. cf. nuk (not, if fr. *neu-qu, but cf. ne-que); Ir. nó “either, or, else; W neu, ne ‘or; Srb. nu, id.; Li. neva “as if, so to speak’; Latv. nav, neva, nava (“is not, formed on the same pat- tern as Li. nërà, nêr, id. fr. *ne, I: Gk. ne-, ára)
11851:nor- (1) “penetration; inside; interior; depth’. Cf. nið, enor-, ner- (2), nerteros. WP IT, 333 OCS norü, m. “den, hole, cave, nest’; nora, norja, f. id.; R norà, f. ‘burrow’; Ukr. norà, f. “hole; source, spring’; Li. náras *diver-bird', cf. naroms, adv. “under water; narüs, adj. “Table to sink”
11852:nor- (2) “join, joint Per. narà ‘partition wall (?); Sw. nara, f. 'car- penter's nail; Li. narys, gs: -io, m. “joint, link, member’; Latv. naris ‘fetter on horse's leg; fetlock'; nàrs (with syntactical length), m. 'vice, clamp'
11853:nor- (3) (?) “narrow, close’. Gmc. fr. *nor- quos in view of Finn. LW, but see noruos (2) below Oss. cf. nárág ‘narrow’; OS naru, OE nearu “narrow, close, strict; OE nearu, gs. we, s. ‘danger’; Finn. (LW) narka, adj. ‘narrow’; Li. (?) narávas, m. (archaic) ‘power; force; tyrant; (mod.) ‘obstinacy’
11855:noruos, å (1) ‘incision, groove, burrow, cut, mark, impression; character, habit'. Cf. en-, rouið, rouos, rüió OHG narwa, f. ‘scar; MHG narwe, nar, w. & sf, id.; LG nor, wf. id.; G Narbe, f. d EMSw. narf, Sw. narv, m. 'pockmark, pitted skin’; OCS nravü, m. ‘manner; OCz. nrav ‘custom’; Slovene nráv ‘nature’; R nòrov ‘habit, man- nerism'; Ukr. norov ‘temper’; cf. also Cz. po- nrava ‘larva’; Li. nařvas, narvà, m. f. “cell of honeycomb; cage’; cf. also (?) narávas, m. (*obstinacy'. See nor- (3) above). (For Hes. norbá ‘incision’: Go. at-snarpjan: Du. sner- pen; ON snerpa, see snorb- Supt)
11857:noruos, à (2) (?) “narrow; strait'. See nor- (3)
11866:noruos, à — nii, nün, nünai
=== IEC page 1645 region: find leaf
```


## [2026-09-07T18:20:43.688Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ndef leafof(n):\n    pos=sum(len(x)+1 for x in lines[:n-1]); return txt[:pos].count('\\f')\nfor n in [11851,11852,11853]:\n    print(n,'leaf',leafof(n),'approx p',(leafof(n)-15)*2)\nEOF\necho \"=== search juicy / anar\"\ngrep -n \"juicy\\|anár\\|anār\\|anar '\\|pomegranate\" IEC.txt | head -20",
 "description": "Mann leaf calc and juicy search"
}
```


### [2026-09-07T18:20:45.079Z] TOOL RESULT

```
11851 leaf 475 approx p 920
11852 leaf 475 approx p 920
11853 leaf 475 approx p 920
=== search juicy / anar
7535:kokon ‘knob, boll, seed, berry’. Extn. variant of kokos, q. v. Oss. kákon ‘sloe’; LW in Arm. kokan, id.; Gk. kókkon (‘pomegranate seed’. LW in Lat. *coc- conem, cf. Sard. coccone ‘bran-bread’; Fr. cocon ‘cocoon’); Ir. cocán ‘calyx, bud, poppy, topknot'; OE haga, gs hagan, wm. ( ‘haw’, and com. Gmc.)
7620:konos, is, ios, iə (2) ‘tip, point, end Cf. kon- Lat. cuneus (*wedge, peg’: cu- as in cum, cuius, etc.?); R kon, m., OCS pokoni, f. *be- ginning’; is-koni ‘from the start; OCz. po-kon ‘end’; Li. cf. káne ‘slot for tiebeam' (?). Cf. also (?) Pol. konar (‘branch’, pl. ‘antlers’) (isophonic w. Per. kanar 'side, brink")
```


## [2026-09-07T18:20:51.190Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"anor\\|anōr\\|anôr\\|anör\" IEC.txt | head -20\necho \"=== total leaves\"\npython3 -c \"\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read(); print('leaves',txt.count(chr(12))+1)\"\necho \"=== leaf 837\"\nawk 'BEGIN{RS=\"\\f\"} NR==838' IEC.txt | head -40",
 "description": "IEC supplement search"
}
```


### [2026-09-07T18:20:52.514Z] TOOL RESULT

```
598:anos (2), à ‘ancestor’. WP I, 55 OHG ano, cf. also enel “grandfather; grand- child"; Sw. anor, pl Ukr. on-uka ‘grandchild’; Li. cf. an-yta husband's mother
=== total leaves
leaves 858
=== leaf 837
nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. id.; Cor. gwern, pl. gwernow, f. id.; ON vorn, f. beside vernd, f. ‘defence’; Sw. värn, n. id.; Finn. (LW) varras, s. ‘spit, pole, shaft
uern- (1), see uermn- (2)
uern- (2) (uernà, is, ios) ‘withy, shoot, suck- er; alder. WP I, 292 Gk. érnos, n. ‘young plant, sucker, shoot’; Alb. verr, m. “alder, white poplar’; Gaul. verna, f. ‘alder; LW in Fr. verne, vergne, id.; Ir. fearn, gs: -a, m. ‘alder’; Br. gwern, pl. gwer- nennu, m. id.; W gwern, coll. id.; Cor. gwern, id.
ueró, ueros, see uer- (1)
(uerógh-, see Supt: U)
uéros, à (1) ‘goodwill, grace, charm, favour, fortune' Skt. varah, m. “treasure”; -varah, cpds.; Av. vàro, m. ‘will, goodwill, gift, grace’; Hom. Gk. ēra, acc. sg. id.; Lat. cf. (?) se-vérus ‘harsh, exacting’; Go. cf. un-wéerei, f. ‘reluctance’; OHG cf. ala-wari, mite-wari, adj. ‘amicable, favourable’; ON vert, adj. ‘snug, peaceful. (Isophonic: Latv. veris ‘deciduous forest; vera, adv. “into notice, prominently’: OE wär, adj.)
uéros, ios (2) “true, right, proper. WP I, 268 Lat. verus, id.; MIr. fir, Ir. fior, id.; Br. W gwir, Cor. gwyr, id.; OBr. guir, id.; OHG war, wāri, id. beside wara, f. (truth, loyalty’: Sl. véra); MHG were, adj. ‘true, loyal’; OCS (and com. Sl.) věra, f. (faith: OHG wara)
uéros (3) ‘watchful; watch" OE waer, adj. *watchful'; Latv. cf. vera, adv. ‘into notice’; cf. MHG o-gde ge-war, adj. *aware'; f. “awareness”
1521
(uerpó, see Supt: U and cf. urpo (2), urpol-; uerpos, à, see uorp- (2))
uers- (1) ‘droplet, sprinkling, shower, dew, rain’. WP I, 269. Cf. uersó (1) Skt. varsáh, -Á, Am. mfn. “rain, shower’; Av. cf. varo&-, v. ‘sprinkle’; Per. baris “rain”; Hitt. warsas (queried), id.; Gk. hérse, hérsé, f. (1) ‘dew’; Olr. cf. feraim, v. ‘pour, rain? beside Mir, fear-thuinn, Ir. fearthain, vbl. n. f. ‘raining’ (vocalism obscure in Olr. fross, f. “shower, downpour’, fr. *urost-?); Li. cf. versmas, m. ‘eruption’; versme, f. ‘spring, source’
uers- (2) ‘young of animal’. Cf. uerks- and uersën-. WP I, 269. (Skt. urs-) Skt. cf. (z-gde) vrsah, m. ‘young male, esp. bullock’; Gk. hérse, hérse, f. (2) “young ani- mal, lamb”; cf. also (?) Hes. errás, usu. érraos, m. (cram, wild boar’. A synthetic cpd.?); Lat. verres, gs: verris, m. ‘boar’; Li. cf. versis, gs: -io, m. ‘calf’; Latv. versis & véersens, m. “ox; Finn. LW varsa (ffoal, fr. Iranian — Joki)
uers- (3) 'growth, hard skin' Lat. cf. verr-üca, f. ‘wart; hillock’; OE wearr, m. *callouse'; OFris. cf. (?) wersene ‘wrinkle’
uersen- ‘male animal". Cf. uers- (2), uerks-. WP I, 269 Av. varo$no, adj. ‘male’; Ionic Gk. érsen, gs: -enos, adj. id.; Latv. vérséns, m. “ox; steer’
uersi- (?). Cf. WP I, 267 Skt. cf. vargi-sthah ‘highest’; Per. bi$, adj. “much, more’; Olr. ferr, Ir. fearr, adj. “better”. (ISophonic: Go. waírsiza, OHG wirsiro, ON verri ‘worse’; G wirs, wirsch “bad, raging’; Du. cf. wars 'averse") (!)
uersð (-ið, -aio) (1) ‘shed, sprinkle, pour, gush, rain’. Cf. uers- (1). WP I, 269 Skt. várgati, 3s. ‘shower, bedew’; pp: vrstah; cf. vrstíh, f. ran: Av. varo&-, v. ‘sprinkle; in- seminate'; Gk. eráo, v. (pour, spew forth’; cf. hérse, f. ‘dew’; herseeis, adj. ((bedewed'. Cf. also árdo, v. ‘sprinkle, water’, if from *ursdo); It. Fr. versare, verser, v. (pour. Not in Lat. in this sense); Ir. (?) feraim, fearaim, v. (“pour”, but consonantism obscure)
uersó, ið (2) “drag, trail’. WP I, 292 Hitt. cf. warsiya(mi), v. (queried: “plough); Gk. Gro Locr. wérro, v. ‘dr
```


## [2026-09-07T18:21:02.743Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('n leaves',len(leaves))\nimport re\nfor i in range(840,858):\n    lv=leaves[i]\n    nums=re.findall(r'\\b(1[456]\\d\\d)\\b',lv)\n    print(i,nums[:5],'|',lv.strip()[:80].replace('\\n',' '))\nEOF",
 "description": "IEC tail leaves"
}
```


### [2026-09-07T18:21:03.970Z] TOOL RESULT

```
n leaves 858
840 ['1526', '1527'] | , wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 
841 ['1528', '1529'] | id. cf. Li. ve-du, id. ues- (2) “breath, air, breeze, cool, fragrance’. WP I, 22
842 ['1530'] | Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma, 
843 ['1531', '1532'] | r-old, annual; yearling'. Cf. uetos. WP I, 251 Skt. vatsáh, m. ‘calf, young anim
844 ['1533', '1534'] | ‘crossbar, bail’ beside LLat. vibra, id.; W gwif, pl. -ion, m. "lever, bar; LG w
845 ['1535'] | v. “become visible’. Cf. type *uidoi! in Gk. idoú! ‘behold’ and OCz. vedé! id.; 
846 ['1536', '1537'] | ow in middie of elephants forehead’; Li. vidüs, m. ‘middle; room, cham- ` ber”; 
847 ['1538', '1539'] | ��: Latv. videnis *torso, rump' and Li. Latv. vidus, m. *middle) uig-, uigl- (1)
848 ['1540', '1541'] | f. *filigree-gold'; MHG wiere, f. id.; OE wir, m. ‘wire; filigree; creeper’; Du.
849 ['1542'] | cf. am- usin, s. (spouse, fr. *som-uiKin-, cf. Lat. uxor, if fr. *uoiK-sor-); Al
850 ['1543', '1544'] | WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. cf. vin-dex, gs: -di
851 ['1545', '1546'] | “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A 
852 ['1547', '1548'] | rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isophonic: Mir fial ‘modes
853 ['1549', '1550'] | - sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.; vitíb, f. ‘pleasure
854 ['1551'] | Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (Hitt. wewakhi, v. see
855 ['1552', '1553'] | Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet'; OBr. gulip & guilp,
856 ['1554'] | bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated) (ulio (1) ‘wind,
857 [] | (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wyl
```


## [2026-09-07T18:21:18.133Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 pages: نارنگ\"\ngrep -n \"نارنگ\\|نارنج\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== pdf page tags near\"\npython3 - <<'EOF'\nimport re\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'نارنگ' in p or 'نارنج' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print(i, m.group(1) if m else '?', 'printed', (int(m.group(1))+1917) if m else '?')\nEOF",
 "description": "Search Borhan vol4 for narang"
}
```


### [2026-09-07T18:21:19.445Z] TOOL RESULT

```
=== BQT v4 pages: نارنگ
7080:۲ < باریج (هم.) » قی : نارنگی :
7081:همیشه تا بنجارت زمرو شهجان کس بسوی آمل وساری نیاورد نارنگه .
7105:ناردگه (.م.) است[وقی: نارنگی]. واصل این‌لغت هندی‌است. ولی‌ازراه رش
7124:باشد - و میوه ای هم هست از نارنج کوچکتر | بمعنی‌ناروان است که درخت ممروف۷ - وکلنار
7142:۱ از: نارنگه (ه.م.) ی (سبت) (رك: هزمزدنامه س۸۷)؛ 16110108108 0:۳9
7143:از انواع مر‌کبات است. « کل گلاب ص ۲۱۵ ». میوة نارنگی همان لارنج شیرین با پرتقال است
8293:۳ - شاخ نارنج و بر که نازه فرنج اخلبندی شانده پر هر کنج .
12354:رشه. ۷ - معرب « بیرنگه » (ه.م.) ؛ رك : دزی ج ۲ ص ۹۳۱: لیرنچات ۳ نارنجیات ‏
=== pdf page tags near
177 178 printed 2095
178 179 printed 2096
206 207 printed 2124
306 307 printed 2224
```


## [2026-09-07T18:21:23.586Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==178' incoming/BQT/BQT_v4_pages.txt | head -60\necho \"########## page 2096\"\nawk 'BEGIN{RS=\"\\f\"} NR==179' incoming/BQT/BQT_v4_pages.txt | head -40",
 "description": "Print Borhan p.2095-2096"
}
```


### [2026-09-07T18:21:24.935Z] TOOL RESULT

```
[pdf page 178]
وه مس بارنکه
رمادپالبال خوانند. 38 بعریی رمان مصری خوانند وخاسیت آن نزديك
نارمشك - بم مم و سکون شبن | بنبل است ۱ - وکورء آهنگری را نیز کوبند
نقطه‌دار وکاف » نارهندیر1کویند وآن عغمی‌است | بابار آنش وانگشت .#8
سرخ رانگه و انك سبزی در میان دارد و آنرا نار نگ ۴ » با کاف فارسی . بر وژن
۱- +« بارمشك و هو الناغیشکه. ویسمی ایا المظ » و بای ایا مشکه الرمان ۰ و
هو حفيشة هندية » « عقار ۲۵۰ . نارر«شك فازسي است بمعنی مشك انار ( قی : معك‌الرمان
(م) م.م. )۳ ۲۵۲۲۵۵ 316998 < عقار ۲۵۰ ف > ورك : دزی ج ۲ اس ۷:۹۳۱ ۰
۲ < باریج (هم.) » قی : نارنگی :
همیشه تا بنجارت زمرو شهجان کس بسوی آمل وساری نیاورد نارنگه .
نلهین فاربایی « فرهنکه نظام >.
نارگیل - بکرکاف . پهلوی 802711 ۰« اونوالا ص ۲۲۷ > معرب آن نارجبل
تفس » وتارجیله * دزی ج یس۹۳۱ > . در نامه پهلوی خر و کواتان بند *0آمده: «ابا گیل
که با شکر :
خورند ۰ به فا یر
(زبان) در چ ۹۳۲ شک ۹۳ رک
« آبارگیل > ۵ ۵ ۹۰ ۳
ماش وب هب 1 1
خوانند و + کت ۳۲06 11 3 ۳
(زبان) پارسيك خی دیس رون
رح وه رم
(کوژهندی) * وه ۰-۰
خوانند.» ر4: پم ارگ ۰ اس
خسرو فبادان میوة نارکیل و مقطع آن درخت نا رکیل
وربا وی ترجمةٌ نگارنده (مجلةٌ آموزش وپرورش سال 4 ۱ص۵۹؟۲). - درسانکر بت 8۵116618
42 ونظای رآن. 0.585 ,1۳281602 - 5100 , .1.8۷16 ورك : هرمزدنامه صس ۹۹-۲۶۸
دا رگیل < ۵۷۵/۵۲۵ 00608 ( 201 - 6000 انگه ) ۰ لوفر. اس > درختی ازانواع تخلها
85 که کلهای نر ومادة آن برروی يك درخت است و میوء درشتآن پوشیده از قسمتی
سخت وچوبی و آلبومن‌آن دارای طبقه‌ای سفید رلگه است که*/۰ ۹۵ آن روغتی دار د که درحدود
۹ درجه مایع میشود . این درخت بیشتر در جزایر مرجانی اقیالوس هند میروید . «ک لکلاب
۰.۹۲۹۱
5 نار نج - بفتح نون (ودرلیجهٌ مر کزی‌بکر) ۰ کردی ع 32712 ۰ 38۲888 « ژابا
س .۱ کیلکی ۵8780 نار (8078800 11۳08)) معرب ۸
ناردگه (.م.) است[وقی: نارنگی]. واصل این‌لغت هندی‌است. ولی‌ازراه رش
زبانهای ایرانی وارد زبانهای آروپایی شدم سورت 0۳8886 درآمدم ؛ ی :۳ ۸
و آن از انواع مرکبات است » ورت درختی با میوه‌های کرد ( که هه
شطح آن فرورفتگیهایی دیده میشود). زرد رنگه وترش مزه . نت 5
عاخه تارج

########## page 2096
[pdf page 179]
طردگی خمدها

و ممتی ظرنج است و آن میوه‌ای باشد معروف. | اندام و پرب رکه ومایه‌دار - وکلنار قظرسی راهم

وطرفج معرب غرنگه بود . کویند هر که پیوسته | میگوبند 8 -

دانٌ آنرا بخوردکزبدن عقرب وامثال آن او را نارور ‎٩‏ < بفتح رایع پروزن دادگرء

آزار سعد . زی را گوبند که پتان او مانند آبار شدء
نار تگی ۱ « با کاف فارسی . بر وژن | باشد -

و معنی تلرنجی است که رنگه مشهور و معروف ثادن - بفتح رابع بر وزن باد زن +

باشد - و میوه ای هم هست از نارنج کوچکتر | بمعنی‌ناروان است که درخت ممروف۷ - وکلنار

وشیرین تر - و بمعنی بی‌رنگی(۱) هم هست که | پارسی باشد - و نام بیشه‌ای همست در دارالمرز

عم رنگه باشد . تزديك به بيشةٌ تپمیشه‌مشهور به‌بيشةٌ نارون ۸ -
نارو < بروزن جارو» پرنده‌ایست خوش ودرخت آلار را هم کنته‌اند ‎٩‏ و باین معتی چم

آوازمانند پلیل؟ - وجل ورشته‌ای را نیز گوبند دابع م آمده است .

که از اعنای مردم برمیاید و آترا بعربی عرق نارو ند *۱- بر وزن خاربند , بمعنی

مدتی ‎)٩(‏ خوانند ۴ . اول نارون است که درخت خوش اندام باشد .
ناروان ؟ - پروزن کاروان . رون را نادوه « بنم تالكت و سکوت واو وها :

کویند و آن درختی است معروف بغابت خوش | بمعنی ارواست و آن پرادهای باشد خوش آواز

() چش : بیرنگی (۱) () چش : بدنی .

۱ از: نارنگه (ه.م.) ی (سبت) (رك: هزمزدنامه س۸۷)؛ 16110108108 0:۳9
از انواع مر‌کبات است. « کل گلاب ص ۲۱۵ ». میوة نارنگی همان لارنج شیرین با پرتقال است
ول ی کوچکتی و خوشبوتر ازآست ودرصرف طبیعت و پرورش آدمی مزء دیگر یافته است . رك :
هرمزدنامه ی ۸۷ - ۴ * ناروه (ه.م.) :
کل سرخ و پر تیهو . کل زرد و پر لارو بشمر عشق‌این هردوه کنند اين‌هر دوتن دعوی.

* منوچهری دامغانی ص ۹۶۹ *-
```


## [2026-09-07T18:21:45.724Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 انار\"\ngrep -n \"^انار\\| انار \" BQT_v1_pages.txt | head -10\necho \"=== BQT v1 ننه\"\ngrep -n \"ننه\" BQT_v1_pages.txt | head\necho \"=== ARY انار / نارنگ / ننه\"\ngrep -n \"انار\\|نارنگ\\|ننه\" incoming/ARY/ARY_pages.txt | head -30",
 "description": "Borhan anar, nane; Aryanpur"
}
```


### [2026-09-07T18:21:45.801Z] TOOL RESULT

```
=== BQT v1 انار
6098:و قسمی از انار نیز می‌باشد - و نام نوعی ازحلوا
11067:لشطی بن‌بویان است - وبلفت رومی انار صحرابی
11069:درخت انار صحرایی را کفتداند ؛ و بضی گونند
13817:انار قر ها - ۳۳ رای شرشته. ۸
13822:ازچوب انار بود بقدرت الهی سبزشد ودرخت آنار
13831:انار مثك ت بکسر عم وسکون شین
14114:نوحی از گل انار است , و گویشد درخت آن یر
18595:و اکر هوم نباشد درخت کر و الا درخت انار ء
20830:اناری است که مرا ز کل شمری دمگرنداردءوآن
26512:انار و است" از حروف تهبجي
=== BQT v1 ننه
998:عبداننه بن‌ طاهر : من‌سمی رعی» و من لزمالمنام رأی الاحلام . هذاالمعنی سرقه
1725:عربی معروف است» این‌لفت هندی است اما نه مانند لفات کیی (بوزننه) وشکر وشمن و چندن
3824:آغاز آن : « بسم اننه| لر حمن الر حبم >
5237:گوننهه وا گر دراضاف باشد متاست وا گر درشگل باشدمشاکت‌بوا کر
5377:۱ خم امثال آن میکننه هگر آنکه .... مقدم ساز ند همچو خدا رحمن است ورحیم است
5449:و عیب میداننه (۷
6272:را در آن خوابانند و ادویهٌ جوشاننه در آن
7251:کتنند و آراننه وا کرد - و امر به آراستن
8288:خواننه - و گل آفتاب پرست را نیز گوبند ٩‏ .
8649:کننهه .
=== ARY انار / نارنگ / ننه
3628:انار
6094:بلرچی (اتاه‌تاننههق: 65شا70 بعشا70 اسپانیایی (82۸7197): رید ابا
6164:78187112 پسگشت‌ها آننه رت دی
6315:فرانسه (88۸/0/4): انار نونی (لتی) (47714(7ا): 115
10647:تخاری ۸ (۸ ۷(لق م7 70): ۸0 انگلیسی کهن (تاقنا80 صزم: ‏ انار
10999:۲ واژه‌ی انگلیسی 011187 نیز از همین واجربشه است (از لاقین به فراننه کهن و سپس به انگلیسی).
11091:پپلری (اماننهه): 580820 ,51317820۷ 1 ,۲801
12057:۱ پهلری (۲7مابقده): ۸ انگلیسی (/۸)5۸70/57(از فراننه)
12593:بونانی 080): 005 ولزی (5(7ا#): انار ۱
14314:انگلیسی (6(/0/580): انار ۱۷ 8 (98ت01)) +7
```


## [2026-09-07T18:21:52.884Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY line 3628 ctx\"\nsed -n '3615,3645p' incoming/ARY/ARY_pages.txt\necho \"=== pdf page for that\"\npython3 - <<'EOF'\nimport re\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:3627])\nbefore=txt[:pos]\nm=None\nfor mm in re.finditer(r'\\[pdf page (\\d+)\\]',before): m=mm\nprint('pdf page',m.group(1) if m else '?')\nEOF\necho \"=== BQT v4 ننه\"\ngrep -n \"ننه\" incoming/BQT/BQT_v4_pages.txt | head",
 "description": "ARY anar entry, Borhan v4 nane"
}
```


### [2026-09-07T18:21:54.167Z] TOOL RESULT

```
=== ARY line 3628 ctx
[pdf page 124]
3ج
برّموزء برّمور» برّمزء برّمر» برّموء بوز (به چم "زنبور) / ۱۲۵
یادداشت:
واژه‌های انگلیسی 81.00۸1 ,81088086 (و همریشه‌های ژرمنی آنها) نیز از همین واجریشه‌ی هند و اروپایی
آمده‌اند.
8۸7۸ ,8۸3۸2 ,8۸7۱/78 ,8۸336172
پپلوی (1مالهم: (۸۲۲۵185) 852 لیتوانی (۸(1۸/4ل 4 7/.): 8 و817]8
ساسکریت (54۸/۶8۵/7): 818۸۸/۸3۸ آتونی (لتی) (7۵/۷ا): 7
8۸/81۸۸ پروسی کهن (4۷ا59نا۲# ا0): ۰ 817785
لاتین (/710مل): 08 ایرلندی کهن (#اکلقا 0ا0): انا
ایسلند یکهن (ل۵/( 0ات5 صام. 8 گالی (0ل8لانا0۸): 2305
آلمانی کهن ((05۸۸/۸ ۲04 صاه): ولزی (7اک7): اد
انار
آلمانی (0874۸0): دازا پسگشت‌ها گت دش
انگلیسی کهن (تل5لل5(/0 طان): ردنا 6 ۶0020
انگلیسی (8(/01387): ادن 5 (888) جمترچید
دانمارکی (/0۸//3): 2 142 :م05
سرئدی (7ل8(75275): 3 4 (885) :28( مار
نروژی (/(2/0717201۵): 3 192 ۸0
هلندی (7ل007): 11 4 (852) :0/05
اسلاری کهن (10ما؟ تال صز): 3 (888) 37
ی 810175۸ برهان قاطع : ۳و ۳۱۶
ای چکه (62808:. ۷5۸ لغت‌نامه دهخدا: ۳۳۹
اسلراکی ماه ۷0۲5۸
یادداشت,
۱ واژه‌ی آانگیین" فارسی از آانگه" به چم "شیر ۰ و عسل" است(برهان قاطع :: ۱۷۴). واجریشه‌ی ۰81881 از هند و
اروپایی -8737* به چم "زنبور" است. واژه‌های "انگدان" و "انجبار" و "انگوژه" نشان می‌دهد که "انگه" به چم "یره
و شهد" است. لذا "انگیین" يا "انگویین " یعنی یره پا شهد" زنبور,
[pdf page 125]
لا زژ)۹گگگک ۳
=== pdf page for that
pdf page 124
=== BQT v4 ننه
12773:۱ یم ننه ( در نداول امروزین ) » قی: نیمه - ۲ - فرهنگها نیم چرخ را
13360:سدننها واق
13649:تضیننه اوای
14215:ورزکار اهفننهه
21325:(ننهاء يك بيك)» وخی ۰1۰1۷ شغنی 1۷ ۰ ال ۰ فلا : الا » سریکلی ۰101۷ 3۷ (یکتاه
```


## [2026-09-07T18:22:04.635Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-07T18:22:04.675Z] TOOL RESULT

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


## [2026-09-07T18:22:11.329Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%86%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%A8%E0%A4%BE\" \\\n \"https://en.wiktionary.org/wiki/nonna\" \\\n \"https://en.wiktionary.org/wiki/nun\" \\\n \"https://www.etymonline.com/word/nun\" \\\n \"https://www.etymonline.com/word/nano-\" \\\n ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 349, root Nana/Nena: verify nursery-word family (Pers. naneh, Skt. nana, Latin nonna/nun, Gk nanos/nano-)\" ;\ndone",
 "description": "Archive Wiktionary/Etymonline pages for Nana root"
}
```


### [2026-09-07T18:22:20.996Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f3fe4bd56b550dc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/740bfaf6b088ff4f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0cce09dd129a832.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b5ab21cc8eaf1b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7f031171196ae9c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a28d32f085ab6618.txt
```


## [2026-09-07T18:22:24.378Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## ننه\"\ngrep -n -A25 \"Persian\" f3fe4bd56b550dc8.txt | head -60\necho \"########## नाना\"\ngrep -n -A20 \"Etymology\" 740bfaf6b088ff4f.txt | head -60",
 "description": "Read Persian naneh and Sanskrit nana Wiktionary"
}
```


### [2026-09-07T18:22:24.438Z] TOOL RESULT

```
########## ننه
76: Persian 
77-
78: Toggle Persian subsection 
79-
80- 3.1 
81- Alternative forms 
82-
83- 3.2 
84- Etymology 
85-
86- 3.3 
87- Pronunciation 
88-
89- 3.4 
90- Noun 
91-
92- 3.4.1 
93- Derived terms 
94-
95- 3.4.2 
96- See also 
97-
98- Toggle the table of contents 
99-
100- ننه 
101-
102- 5 languages 
103-
--
241: Persian
242- [ edit ] 
243-
244: Persian Wikipedia has an article on: ننه 
245-
246- Wikipedia fa 
247-
248- Alternative forms
249- [ edit ] 
250-
251- نه‌نه ( with ZWNJ ) , نه نه ( with space ) 
252-
253- نن ( nan ) ( dialectal , Kazerun ) 
254-
255- نانا ( nānā ) , نانی ( nāni ) , ننی ( nani ) 
256-
257- Etymology
258- [ edit ] 
259-
260- Originally from baby talk.
261-
262- Pronunciation
263- [ edit ] 
264-
265: ( Classical Persian ) IPA ( key ) : /na.ˈna/ 
266-
267- ( Dari, formal ) IPA ( key ) : [nä.ná] 
268-
269- ( Dari, formal ) IPA ( key ) : [nä.ná] 
270- ( Kabuli ) IPA ( key ) : [nä.ná] 
271-
########## नाना
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
72-
73- 1.3.2 
74- Related terms 
75-
76- 1.4 
77- References 
78-
79- 2 
80- Sanskrit 
81-
82- Toggle Sanskrit subsection 
--
88: Etymology 
89-
90- 2.3 
91- Pronunciation 
92-
93- 2.4 
94- Adverb 
95-
96- 2.4.1 
97- Descendants 
98-
99- 2.5 
100- References 
101-
102- Toggle the table of contents 
103-
104- नाना 
105-
106- 15 languages 
107-
108- বাংলা 
--
300: Etymology
301- [ edit ] 
302-
303- Inherited from Prakrit णण्ण ( ṇaṇṇa ) + Middle Indo-Aryan -𑀓- ( -ka- ) , from older *नान्न ( nānna ) , from onomatopoeic nursery words.
304-
305- Pronunciation
306- [ edit ] 
307-
308- ( Standard Hindi ) IPA ( key ) : /nɑː.nɑː/ , [näː.näː] 
309-
310- Noun
311- [ edit ] 
312-
313- नाना • ( nānā )  m ( female equivalent नानी , Urdu spelling نانا ) 
314-
315- maternal grandfather
```


## [2026-09-07T18:22:29.316Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '271,300p' f3fe4bd56b550dc8.txt\necho \"########## Sanskrit section of नाना\"\nsed -n '330,420p' 740bfaf6b088ff4f.txt",
 "description": "Read remainder"
}
```


### [2026-09-07T18:22:29.375Z] TOOL RESULT

```
 ( Hazaragi ) IPA ( key ) : [nä.ná] 

 ( Iran, formal ) IPA ( key ) : [næ.né] 

 ( Tajik, formal ) IPA ( key ) : [nä.ná] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 nana

 Dari reading ? 

 nana

 Iranian reading ? 

 nane

 Tajik reading ? 

 nana

 Noun
 [ edit ] 

########## Sanskrit section of नाना
 nānā 

 नाना 
 nānā 

 oblique

 नाना 
 nānā 

 नानाओं 
 nānāõ 

 vocative

 नाना 
 nānā 

 नानाओ 
 nānāo 

 Related terms
 [ edit ] 

 दादा ( dādā ) 

 References
 [ edit ] 

 Turner, Ralph Lilley ( 1969–1985 ), “ *nānna ”, in A Comparative Dictionary of the Indo-Aryan Languages , London: Oxford University Press, page 405 

 Dāsa, Śyāmasundara ( 1965–1975 ), “ नाना ”, in Hindī Śabdasāgara [ lit. “Sea of Hindi words” ] (in Hindi), Kashi [ Varanasi ] : Nagari Pracarini Sabha, page 2581 

 Caturvedi, Mahendra; Bhola Nath Tiwari ( 1970 ), “ नाना ”, in A practical Hindi-English dictionary , Delhi: National Publishing House, page 360 

 McGregor, Ronald Stuart ( 1993 ), “ नाना ”, in The Oxford Hindi-English Dictionary , London: Oxford University Press, page 552 

 Bahri, Hardev ( 1989 ), “ नाना ”, in Siksarthi Hindi-Angrejhi Sabdakosa [ Learners' Hindi-English Dictionary ], Delhi: Rajpal & Sons, page 343 . 

 Sanskrit
 [ edit ] 

 Alternative scripts
 [ edit ] 

 Alternative scripts
 নানা ( Assamese script ) 
 ᬦᬵᬦᬵ ( Balinese script ) 
 নানা ( Bengali script ) 
 𑰡𑰯𑰡𑰯 ( Bhaiksuki script ) 
 𑀦𑀸𑀦𑀸 ( Brahmi script ) 
 နာနာ ( Burmese script ) 
 નાના ( Gujarati script ) 
 ਨਾਨਾ ( Gurmukhi script ) 
 𑌨𑌾𑌨𑌾 ( Grantha script ) 
 ꦤꦴꦤꦴ ( Javanese script ) 
 𑂢𑂰𑂢𑂰 ( Kaithi script ) 
 ನಾನಾ ( Kannada script ) 
 នានា ( Khmer script ) 
 ນານາ ( Lao script ) 
 നാനാ ( Malayalam script ) 
 ᠨᠠ᠎᠊ᠠᠨᠠᢇ ( Manchu script ) 
 𑘡𑘰𑘡𑘰 ( Modi script ) 
 ᠨᠠᢗᠨᠠ᠋᠎ᠠ ( Mongolian script ) 
 𑧁𑧑𑧁𑧑 ( Nandinagari script ) 
 𑐣𑐵𑐣𑐵 ( Newa script ) 
 ନାନା ( Odia script ) 
 ꢥꢵꢥꢵ ( Saurashtra script ) 
 𑆤𑆳𑆤𑆳 ( Sharada script ) 
 𑖡𑖯𑖡𑖯 ( Siddham script ) 
 නානා ( Sinhalese script ) 
 𑩯𑩛𑩯𑩛 ( Soyombo script ) 
 𑚝𑚭𑚝𑚭 ( Takri script ) 
 நாநா ( Tamil script ) 
 నానా ( Telugu script ) 
 นานา ( Thai script ) 
 ནཱ་ནཱ ( Tibetan script ) 
 𑒢𑒰𑒢𑒰 ( Tirhuta script ) 
 𑨝𑨊𑨝𑨊 ( Zanabazar Square script ) 

 Etymology
 [ edit ] 

 Perhaps an aphetic amredita of अना ( anā́ ) (nā́nā ⇐*anā́nā), with the meaning 'in this way and that way, hereby and thereby'. Compare parallel formations इहेह ( iheha ) and इतरेतर ( itaretara ) .

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /nɑ́ː.nɑː/ 

 ( Classical Sanskrit ) IPA ( key ) : /n̪ɑː.n̪ɑː/
```


## [2026-09-07T18:22:40.035Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%CE%BD%E1%BE%B6%CE%BD%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/nanus\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/orange\" \\\n \"https://www.etymonline.com/word/orange\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/naranja\" \\\n \"https://en.wiktionary.org/wiki/arancia\" \\\n ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 349: roots Nana/Nena and Naranga (orange chain, anar)\" ;\ndone",
 "description": "Archive more Wiktionary/Etymonline pages"
}
```


### [2026-09-07T18:22:50.696Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3f470f204b95203d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b67b75c4d5736e69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b25a58f2272c273.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf05b3ee93cf1775.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54c95e12325f4cb9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b87a97274c0d98d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1a934e23fb05c29.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/383e59de6e0e800a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fa8d4e28387bfeb.txt
```


## [2026-09-07T18:22:54.411Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## νᾶνος\"\ngrep -n -B3 -A14 \"^ Etymology$\" 3f470f204b95203d.txt | sed -n '1,80p'\necho \"########## nanus (Latin)\"\ngrep -n -B3 -A14 \"^ Etymology$\" b67b75c4d5736e69.txt | sed -n '1,80p'",
 "description": "Greek nanos / Latin nanus etymologies"
}
```


### [2026-09-07T18:22:55.766Z] TOOL RESULT

```
########## νᾶνος
161-
162- νᾰ́ννος ( nắnnos ) 
163-
164: Etymology
165- [ edit ] 
166-
167- Possibly onomatopoeic , though the logic behind the formation, as well as putative source if borrowed, is unclear. [ 1 ] Compare perhaps English neener ( playground insult ) , Vulgar Latin *ninnus ( “ child ” ) .
168-
169- Pronunciation
170- [ edit ] 
171-
172- IPA ( key ) : /nâː.nos/ → /ˈna.nos/ → /ˈna.nos/ 
173-
174- ( 5 th BCE Attic ) IPA ( key ) : /nâː.nos/ 
175-
176- ( 1 st CE Egyptian ) IPA ( key ) : /ˈna.nos/ 
177-
178- ( 4 th CE Koine ) IPA ( key ) : /ˈna.nos/ 
########## nanus (Latin)
185- Latin
186- [ edit ] 
187-
188: Etymology
189- [ edit ] 
190-
191- Borrowed from Ancient Greek νᾶνος ( nânos , “ dwarf ” ) .
192-
193- Pronunciation
194- [ edit ] 
195-
196- ( Classical Latin ) IPA ( key ) : [ˈnaː.nʊs] 
197-
198- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈnaː.nus] 
199-
200- Noun
201- [ edit ] 
202-
--
305- Northern Sami
306- [ edit ] 
307-
308: Etymology
309- [ edit ] 
310-
311- From Proto-Samic *nënōs .
312-
313- Pronunciation
314- [ edit ] 
315-
316- ( Kautokeino ) IPA ( key ) : /ˈnanuːs/ 
317-
318- Adjective
319- [ edit ] 
320-
321- nanus ( comparative nannosit , superlative nannoseamọs ) 
322-
```


## [2026-09-07T18:23:06.024Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## Sanskrit नारङ्ग\"\ngrep -n -A10 \"^ Etymology\" 6b25a58f2272c273.txt | head -60\necho \"########## Arabic نارنج\"\ngrep -n -A10 \"^ Etymology\" cf05b3ee93cf1775.txt | head -60",
 "description": "Sanskrit naranga + Arabic naranj"
}
```


### [2026-09-07T18:23:06.086Z] TOOL RESULT

```
########## Sanskrit नारङ्ग
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
--
198: Etymology
199- [ edit ] 
200-
201: Etymology tree
202-
203- Proto-Austroasiatic *ŋaːm der. ? 
204- Proto-Dravidian *nāram 
205-
206- Proto-Dravidian *kāy 
207-
208- Sanskrit नारङ्ग 
209-
210- Borrowed from Dravidian ; [ 1 ] compare Tamil நார்த்தங்காய் ( nārttaṅkāy , “ citron ” ) (itself a compound of நரந்தம் ( narantam , “ fragrance ” ) and காய் ( kāy , “ fruit ” ) ), as well as Tamil நாரங்காய் ( nāraṅkāy ) , Telugu నారంగము ( nāraṅgamu ) , Malayalam നാരങ്ങ ( nāraṅṅa ) , Kannada ನಾರಂಗಿ ( nāraṅgi ) . Attested from ca. the 4th century ( Sushruta Samhita ).
211-
########## Arabic نارنج
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
72-
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
--
105: Etymology 
106-
107- 3.2 
108- Noun 
109-
110- 3.2.1 
111- Derived terms 
112-
113- 3.2.2 
114- Descendants 
115-
--
125: Etymology 
126-
127- 4.2 
128- Pronunciation 
129-
130- 4.3 
131- Noun 
132-
133- 4.3.1 
134- Derived terms 
135-
--
216: Etymology
217- [ edit ] 
218-
219: Etymology tree
220-
221- Proto-Austroasiatic *ŋaːm der. ? 
222- Proto-Dravidian *nāram 
223-
224- Proto-Dravidian *kāy 
225-
226- Sanskrit नारङ्ग ( nāraṅga ) bor. 
227- Classical Persian نَارَنْگ ( nārang ) bor.
```


## [2026-09-07T18:23:09.136Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '226,300p' cf05b3ee93cf1775.txt\necho \"=================== descendants section\"\ngrep -n -A40 \"Descendants\" cf05b3ee93cf1775.txt | sed -n '1,90p'",
 "description": "Arabic naranj details"
}
```


### [2026-09-07T18:23:09.193Z] TOOL RESULT

```
 Sanskrit नारङ्ग ( nāraṅga ) bor. 
 Classical Persian نَارَنْگ ( nārang ) bor. 
 Arabic نارنج 

 Borrowed from Classical Persian نَارَنْگ ( nārang ) , from Sanskrit नारङ्ग ( nāraṅga , “ orange tree ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /naː.rand͡ʒ/ 

 Noun
 [ edit ] 

 نَارَنْج • ( nāranj )  m 

 bitter orange ( Citrus aurantium )

 Declension
 [ edit ] 

 Declension of noun نَارَنْج ( nāranj )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نَارَنْج 
 nāranj 

 النَّارَنْج 
 an-nāranj 

 نَارَنْج 
 nāranj 

 nominative

 نَارَنْجٌ 
 nāranjun 

 النَّارَنْجُ 
 an-nāranju 

 نَارَنْجُ 
 nāranju 

 accusative

 نَارَنْجًا 
 nāranjan 

 النَّارَنْجَ 
 an-nāranja 

 نَارَنْجَ 
 nāranja 

 genitive

 نَارَنْجٍ 
 nāranjin 

 النَّارَنْجِ 
 an-nāranji 

 نَارَنْجِ 
=================== descendants section
74: Descendants 
75-
76- 1.4 
77- Further reading 
78-
79- 2 
80- Central Kurdish 
81-
82- Toggle Central Kurdish subsection 
83-
84- 2.1 
85- Etymology 
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
99- 3 
100- Ottoman Turkish 
101-
102- Toggle Ottoman Turkish subsection 
103-
104- 3.1 
105- Etymology 
106-
107- 3.2 
108- Noun 
109-
110- 3.2.1 
111- Derived terms 
112-
113- 3.2.2 
114: Descendants 
115-
116- 3.3 
117- Further reading 
118-
119- 4 
120- Persian 
121-
122- Toggle Persian subsection 
123-
124- 4.1 
125- Etymology 
126-
127- 4.2 
128- Pronunciation 
129-
130- 4.3 
131- Noun 
132-
133- 4.3.1 
134- Derived terms 
135-
136- 4.3.2 
137: Descendants 
138-
139- Toggle the table of contents 
140-
141- نارنج 
142-
143- 13 languages 
144-
145- فارسی 
146- Français 
147- Hrvatski 
148- Magyar 
149- ქართული 
150- Kurdî 
151- Lietuvių 
152- Malagasy 
153- Polski 
154- پښتو 
155- Русский 
156- Sängö 
157- 中文 
158-
159- Entry 
160-
161- Discussion 
162-
163- English
```


## [2026-09-07T18:23:12.595Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/^ Descendants$/{c++} c>=1' cf05b3ee93cf1775.txt | sed -n '1,60p'\necho \"=============== Persian section نارنج\"\nawk '/^ Persian$/{f=1} f' cf05b3ee93cf1775.txt | sed -n '1,60p'",
 "description": "Arabic naranj descendants and Persian narenj"
}
```


### [2026-09-07T18:23:13.832Z] TOOL RESULT

```
 Descendants
 [ edit ] 

 → Classical Persian: نَارَنْج ( nāranj ) ( see there for further descendants )

 → Ottoman Turkish: نارنج ( narenc, narenç ) ( see there for further descendants )

 → ⇒ Byzantine Greek: νεράντζιον ( nerántzion ) ( see there for further descendants )

 → Old Spanish: naranja ( see there for further descendants )

 → Old Galician-Portuguese: laranja ( see there for further descendants )

 → Italian: arancia → Old Occitan: auranja ( see there for further descendants )
 ⇒ Italian: pomarancia ( see there for further descendants )

 Further reading
 [ edit ] 

 نارنج on the Arabic Wikipedia. Wikipedia ar 

 Central Kurdish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Arabic نَارَنْج ( bitter orange ) , ultimately from Sanskrit नारङ्ग ( nāraṅga , “ orange tree ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /naːɾənd͡ʒ/ 

 Noun
 [ edit ] 

 Northern Kurdish

 narinc 

 نارنج ( narinc ) 

 bitter orange , Citrus × aurantium 

 Derived terms
 [ edit ] 

 نارنجۆک ( narincok ) 
 نارنجی ( narincî ) 

 References
 [ edit ] 

 Hejar ( 1990 ), “ نارنج ”, in Henbane borîne ‎ [1] , Tehran: Soroush, page 852 

 Wahby, T. ; Edmonds, C. J. ( 1966 ), “ narinc ”, in A Kurdish-English Dictionary , London: Oxford University Press, page 96 

 Ottoman Turkish
 [ edit ] 
=============== Persian section نارنج
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: نارنج 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Borrowed from Arabic نَارَنْج ( nāranj ) , from Classical Persian نارنگ ( nārang ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /naː.ˈrand͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [nɑː.ɾánd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [nɑː.ɾánd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [nɑː.ɾánd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [nɔː.ɾánd͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [nɒː.ɹénd͡ʒ̥] , [nɒː.ɹǽnd͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [nɔ.ɾánd͡ʒ] 

 Rhymes: -and͡ʒ 

 Readings

 Classical reading ? 

 nāranj

 Dari reading ? 

 nāranj

 Iranian reading ? 

 nârenj, nâranj

 Tajik reading ? 

 noranj

 Noun
 [ edit ] 

 نارنج • ( nāranj, nārinj / nâranj, nârenj ) ( Tajik spelling норанҷ , or норинҷ ) 

 Seville orange , bitter orange , Citrus aurantium 

 Derived terms
 [ edit ] 

 نارنجک ( nârenjak )
```


## [2026-09-07T18:23:21.165Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## etymonline orange\"\ngrep -n -i -A6 \"orange (n\" 7b87a97274c0d98d.txt | head -60\necho \"########## wikt orange english etym\"\nawk '/^ English$/{f=1} f' 54c95e12325f4cb9.txt | grep -n -A12 \"^ Etymology\" | head -40",
 "description": "Etymonline + Wiktionary orange"
}
```


### [2026-09-07T18:23:22.601Z] TOOL RESULT

```
########## etymonline orange
56: orange (n.) 
57-
58- late 14c., in reference to the fruit of the orange tree (late 13c. as a surname), from Old French orange , orenge (12c., Modern French orange ), from Medieval Latin pomum de orenge , from Italian arancia , originally narancia (Venetian naranza ), an alteration of Arabic naranj , from Persian narang , from Sanskrit naranga-s "orange tree," a word of uncertain origin.
59-
60- Not used as a color word in English until 1510s ( orange color ), "a reddish-yellow color like that of a ripe orange." Colors similar to modern orange in Middle English might be called citrine or saffron . Loss of initial n- probably is due to confusion with the definite article (as in une narange, una narancia ), but also perhaps was by influence of French or "gold." The name of the town of Orange in France (see Orangemen ) perhaps was deformed by the name of the fruit. Orange juice is attested from 1723.
61-
62- The tree's original range probably was northern India. The Persian orange, grown widely in southern Europe after its introduction in Italy 11c., was bitter; sweet oranges were brought to Europe 15c. from India by Portuguese traders and quickly displaced the bitter variety, but only Modern Greek still seems to distinguish the bitter ( nerantzi ) from the sweet ( portokali "Portuguese") orange.
########## wikt orange english etym
50: Etymology
51- [ edit ] 
52-
53: Etymology tree
54-
55- ▲ 
56-
57- Italian melarancia calq. 
58-
59- Old French Orenge influ. 
60-
61- ▲ 
62-
63- Old Occitan auranja influ. 
64-
65- Old French pomme d'orenge 
--
1499: Etymology
1500- [ edit ] 
1501-
1502- From French orange , ultimately from Dravidian . Compare Tamil நாரங்காய் ( nāraṅkāy ) .
1503-
1504- Pronunciation
1505- [ edit ] 
1506-
1507- IPA ( key ) : [oˈʁɑŋɕə] 
1508-
1509- Noun
1510- [ edit ] 
1511-
--
1627: Etymology
1628- [ edit ] 
1629-
1630- Inherited from Middle French orange , from Old French orenge , short form of late pomme d'orenge or pomme d'orange , which was calqued after Old Italian melarancia ( mela + arancia ). The o came into the word under influence of the place name Orange .
1631-See English orange .
1632-
1633- Pronunciation
1634- [ edit ] 
1635-
```


## [2026-09-07T18:23:36.459Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:12831])\nleaf=txt[:pos].count('\\f')\nprint('leaf',leaf,'printed approx',leaf-20)\nleaves=txt.split('\\f')\nprint(leaves[leaf][:1500])\nEOF",
 "description": "Skeat orange leaf"
}
```


### [2026-09-07T18:23:37.791Z] TOOL RESULT

```
leaf 341 printed approx 321
  of  an  original  by  meul — O.  F.  f^pit,  abundance;  ftlvH L.  f#^d.  plenty  (aboveV         ^|
office,  duly.    (F.-L.)      F.  ^ offidum.  duty  pKc-^oiaAM^a^Ma. contr.  from  optficiHm.^X^  ^i'»> of  opa,  wealth  ;  fiutrt.  to  do;| Der.  effi('fr,  F.  ojffUttr,  Low  ~ offie-i-CHS,  F.  cfficitux,  L.  o^
optimism,  the  doctrine the  best.  (L.>     From  L.  oftim' best;  with  suffix   -ism  (Gk. 0P'ti-PHus  is  a  supcrl,  form  fn (i.  c.  choice) ;  cf.  optart,  to
option,  choice.   vF.  — L.) L.  optiomm,  ace.  of  «//!«,  ch( to  L.  opfart,  to  wish  (above).
opment,  wealthy     (F.  — 1-> i!nf/.  — L.  opuUntui,  wc&lthy.  — L. of  «|/Vj,  uealth.     Cf.  Skt.  a^oi,  \ Optic,  relating  to  the  tight.    ( F.  optiqu€.  —  Gk,  orriffiii,  bell sight ;  ci.   t*T^Pt  a  spy.     Fi ow-  (for  0*-)  seen  in  Ionic  Sw~ seen,  Sip-ofiat,  I  shall  see;  cf.  t^ the  eye.     See  Sr«.     ( ^AK.)
autopsy,  [fCTSonal  ins]>ccti« iik.  a^mifia,  a  seeing  with  our's  c
—  Gk.  aur-*li,  self;  and  ^(t,  sight catoptric,  relating  tooplicaj  r
(Gk.)  Gk.  KaTorrpixdr,  rcflcxi* ic&Towr^ov,  a  mirror. —  Gk.  aarH inward ;  CirT-o/iat,  I  see.
dioptrics,  the  science  of  the  i of  li^,'ht.  (Ck.)  Gk.  rd  fitorr^ tries. —  Gk.  ^owrpiK6s,  relating  lo Tpa,  an  optical  instrument  for  takinf &c.  —  Gk.  9tA.  through  ;  ^i
ophthalmia,  inflomniatiou] Gk.  i^aA,>iia.  — Gk.  ti^tfoA^. for  uwTuK^ui  •  ;  cf.  Doric
—  Gk.  SwT-oi/a
```


## [2026-09-07T18:23:45.986Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('nleaves',len(leaves))\nfor i in range(335,350):\n    nums=re.findall(r'\\b(3[0-9]\\d)\\b',leaves[i])\n    print(i,nums[:6],'|',leaves[i].strip()[:60].replace('\\n',' '))\nEOF",
 "description": "Skeat leaf numerals"
}
```


### [2026-09-07T18:23:47.237Z] TOOL RESULT

```
nleaves 657
335 [] | v/er-nu/turariui^ cxcvssive  in  number. Numismatic ;  see  
336 [] | �■     -'i-T,   pi     AS.   rf//i, !   to  Ice).  fj/iV/,  
337 [] | 8-sidrd  fi| (Gk.)  From  Axrd,  for  ^ctw,  eight;! a  base
338 [] | cll  (alxivc). '  ince  percci^-ed  by  its  smell ,     'le
339 [] | -  0.  F. «r//  (F.  huili).  —  L   oleum.  «  Gk.  ^Aojov,
340 ['316'] | tame  n^trne.o Ck.  6fi'!y-tt  same;  Cvofta,  name.  See  S
341 [] | of  an  original  by  meul — O.  F.  f^pit,  abundance;  ftl
342 [] | nat«.  (L.)  L.  co-  (for  ntm\ together;  ortiinatus^  arr
343 [] | correct  anting.  (F. -Gk.)     M.  E.  erte^raphit.^J  prit
344 [] | omiptioa of  M.  E.  outemeU  (Rich.  Coer  dc  l.ion, J931)
345 [] | n,  awtn, contracted  to  own  by  loss  of  /.    A.S.  ig^
346 [] | tmmfmtmm^  sii.  -  U  tompoiiut,  pp.  of 4 tpmpaasa,  to  
347 [] | ety  entitled  Congrtgatie  dt  p» fide,  constituted  at  R
348 [] | mpuniti.^ L.  Acc.  impunitattm,  ace  of  imputtifaj, impun
349 ['335'] | �//fW.  also/w/j/i'**, a  coat,  jacket  (Oudemaos).  We  fi
```


## [2026-09-07T18:24:07.331Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (378,379,380,381,382):\n    print('---',i,leaves[i].strip()[:300].replace('\\n',' '))\nEOF",
 "description": "Skeat leaf 378-382"
}
```


### [2026-09-07T18:24:08.579Z] TOOL RESULT

```
--- 378 L.) ;  older  form /!> ;  A.  S /w".  —  L. jai  fix,  pitch,  •f-  Gk.  maca  \J[qi '  "man.  ptkkit.  pitch. 10  pitch  the  scajn  of  a  &hip. ,)      opoji.  P*gt*,  a   vaini&h   of to  pitch.     Here  tmpt^ar r,  to  pilch  (with  prefix  tm- 7—h.  fit-,    item    of  pix,   pitch. ME.   wo
--- 379 itAq^,  a  flat  sur- face; s«  Plain. plan.  (F.-L.)     F.plan,  'the  grouxid- filat  of  a  building;'  Cot.  —  V. pian,  flat ; atcr  form  of  O.  ¥.  pfatn.  —  h.  planum,  ace. of  planus,  flat.  Properly,  a  drawing  (for a  building)  on  a  flat  surface. plane  (i),  a  level  surfac
--- 380 if*-  (for  i»),
--- 381 tt*,  to  iikould.  form  in  clay  or m\aaau<f  «  w\nr-y«iv  •,  ony.  lo ^to  rAart/T,  flat. "  -Gkl  L.  //«/iou.-Gk. formoQlding.~Gk.  vXa^ircu', flat  space.  (K.  -  Gk.)     F. 0.  K.  /Ai/f/.  a  small  plate ; a  plate.  -  F.  pla/,  flat.  -  Gk. see  PlAte  (above). ft  flat  (urfacc, 
--- 382 d.  ;F.-L.)  M.  E.  pit<ien,~0.  F. plat  Jeff  to  plead,  argue.  —  O.  F. /il«</,  a plea ;  see  plea  above. pleasure.  (F.-L.)  An  £.  spelling  of ¥,  piaisir,  pleasure  (Ukc  E.  leisure  for  F. loisir).  This  F.  sb.  is  merely  the  infin. mood  uiicd  substantively.  *L.  placere;
```


## [2026-09-07T18:24:13.973Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls data/extracted 2>/dev/null | head\ngrep -rn \"SKT\" --include=*.json --include=*.md data/verification/sources/refs_online.json | head -3\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SKT'],ensure_ascii=False,indent=1))\"",
 "description": "Check SKT bibliography claim"
}
```


### [2026-09-07T18:24:15.178Z] TOOL RESULT

```
batch
NEXT_CHUNK
RETRY.txt
test
(eval):3: no matches found: --include=*.json
{
 "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
 "edition_found": "1911 'new and corrected impression' (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.",
 "cites": "page number of Skeat, Concise Etymological Dictionary"
}
```


## [2026-09-07T18:24:22.798Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 60 curl -s \"https://archive.org/metadata/bub_gb_4ZkRAAAAIAAJ\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'),d.get('dir'))\nfor f in d.get('files',[]):\n    if f['name'].endswith('djvu.txt') or f['name'].endswith('_djvu.xml') or f['name'].endswith('.pdf'): print(f['name'], f.get('size'))\n\"",
 "description": "Check 1882 Skeat archive item"
}
```


### [2026-09-07T18:24:25.470Z] TOOL RESULT

```
ia600509.us.archive.org /23/items/bub_gb_4ZkRAAAAIAAJ
bub_gb_4ZkRAAAAIAAJ.pdf 72768524
bub_gb_4ZkRAAAAIAAJ_djvu.txt 3120575
bub_gb_4ZkRAAAAIAAJ_djvu.xml 38211942
```


## [2026-09-07T18:24:30.470Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ntimeout 180 curl -s -o skeat1882.txt \"https://ia600509.us.archive.org/23/items/bub_gb_4ZkRAAAAIAAJ/bub_gb_4ZkRAAAAIAAJ_djvu.txt\" && python3 - <<'EOF'\nimport re\ntxt=open('skeat1882.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('nleaves',len(leaves))\nfor i,lv in enumerate(leaves):\n    if re.search(r'ORANGE',lv):\n        print('leaf',i, lv.strip()[:400].replace('\\n',' '))\nEOF",
 "description": "Download Skeat 1882 concise and find ORANGE"
}
```


### [2026-09-07T18:24:33.199Z] TOOL RESULT

```
nleaves 1
```


## [2026-09-07T18:24:36.410Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\ntxt=open('skeat1882.txt',encoding='utf-8',errors='replace').read()\nprint(len(txt))\ni=txt.find('ORANGE')\nprint(txt[i-3000:i+1500] if i>0 else 'not found')\nEOF",
 "description": "Find ORANGE in Skeat 1882"
}
```


### [2026-09-07T18:24:37.764Z] TOOL RESULT

```
3089919
not found
```


## [2026-09-07T18:24:41.244Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\ntxt=open('skeat1882.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'[Oo]range',txt):\n    print(m.start(), repr(txt[m.start()-200:m.start()+300]))\n    print('---')\nEOF",
 "description": "Search orange in Skeat 1882"
}
```


### [2026-09-07T18:24:42.495Z] TOOL RESULT

```
440671 "of  lyre  or  lute. \n\nguitar.  (F.  -  L.  -  Gk.)  F.  guitare.  - \nL.  cithara ;  as  above. \n\nCitizen ;  see  Civil. \n\nCitron.  (F.-L.-Gk.)  F.  a'tron.- \nLow  L.  acc.  citronem.  —  L.  citrus,  orange- \ntree. —Gk.  ttirpov,  a  citron;  mrpta,  citron- \ntree. \n\nCity;  see  Civil. \n\nCivet.  (F.  -  Arab.)  F.  civette,  civet ; \nalso  the  civet-cat ;  borrowed  from  medieval \nGk.  faWno*  (Brachet).  -  Arab,  zabdd, \ncivet. \n\nCivil.  (L.)  L.  ciuilis,  belonging  to \ncitizens.  —  L.  c"
---
1606567 "are,  to  speak  (above). \n\nOrang-outang,  a  large  ape.  (Malay.) \nMalay  6rang  titan,  lit.  '  wild  man.'  —  Malay \n6rang,  a  man  ;  titan,  htitan,  woods,  wilds  of \n•a  country,  wild. \n\nOrange.  (F.  -  Ital.  -  Pers.)  O.  F. \norenge  (F.  orange).  Put  for  narenge*,  but \nthe  initial  n  was  lost  (in  Italian),  and  then \narenge  became  orenge  by  a  popular  ety- \nmology from  or,  gold.  Cf.  Span,  naranja, \nan  orange.  —  Ital.  arancio,  an  orange.  — \nPers.  nara"
---
1606623 ".  (Malay.) \nMalay  6rang  titan,  lit.  '  wild  man.'  —  Malay \n6rang,  a  man  ;  titan,  htitan,  woods,  wilds  of \n•a  country,  wild. \n\nOrange.  (F.  -  Ital.  -  Pers.)  O.  F. \norenge  (F.  orange).  Put  for  narenge*,  but \nthe  initial  n  was  lost  (in  Italian),  and  then \narenge  became  orenge  by  a  popular  ety- \nmology from  or,  gold.  Cf.  Span,  naranja, \nan  orange.  —  Ital.  arancio,  an  orange.  — \nPers.  naranj,  ndrinj,  ndrang,  an  orange. \nAllied  to  Pers.  n"
---
1606811 'renge  (F.  orange).  Put  for  narenge*,  but \nthe  initial  n  was  lost  (in  Italian),  and  then \narenge  became  orenge  by  a  popular  ety- \nmology from  or,  gold.  Cf.  Span,  naranja, \nan  orange.  —  Ital.  arancio,  an  orange.  — \nPers.  naranj,  ndrinj,  ndrang,  an  orange. \nAllied  to  Pers.  ndr,  a  pomegranate. \n\nOration,  Orator ;  see  Oral. \n\nOrb.  (F.  — L.)  F.  orbe.  —  h.  orbem,  acc. \nof  orbis,  a  circle,  sphere. \n\nexorbitant,  extravagant.  (F.-L.)  F. \nexorbita'
---
1606844 'arenge*,  but \nthe  initial  n  was  lost  (in  Italian),  and  then \narenge  became  orenge  by  a  popular  ety- \nmology from  or,  gold.  Cf.  Span,  naranja, \nan  orange.  —  Ital.  arancio,  an  orange.  — \nPers.  naranj,  ndrinj,  ndrang,  an  orange. \nAllied  to  Pers.  ndr,  a  pomegranate. \n\nOration,  Orator ;  see  Oral. \n\nOrb.  (F.  — L.)  F.  orbe.  —  h.  orbem,  acc. \nof  orbis,  a  circle,  sphere. \n\nexorbitant,  extravagant.  (F.-L.)  F. \nexorbitant.  —  L.  exorbitant-,  stem  o'
---
1606894 'alian),  and  then \narenge  became  orenge  by  a  popular  ety- \nmology from  or,  gold.  Cf.  Span,  naranja, \nan  orange.  —  Ital.  arancio,  an  orange.  — \nPers.  naranj,  ndrinj,  ndrang,  an  orange. \nAllied  to  Pers.  ndr,  a  pomegranate. \n\nOration,  Orator ;  see  Oral. \n\nOrb.  (F.  — L.)  F.  orbe.  —  h.  orbem,  acc. \nof  orbis,  a  circle,  sphere. \n\nexorbitant,  extravagant.  (F.-L.)  F. \nexorbitant.  —  L.  exorbitant-,  stem  of  pres. \npt  of  exorbitare,  to  fly  out  of  a'
---
2927341 "rum,  acc.  of \nzephyr  us,  the  west  wind.  —  Gk. \nthe  west  wind.    Allied  to  (u<f>ost \ngloom,  the  dark  quarter,  west. \n\nZero ;  see  Cipher. \n\nZest.  (F\\-L.-Gk.)  Formerly  a  chip \nof  orange  or  lemon-peel,  used  for  flavouring \ndrinks ;  hence,  something  that  gives  a  relish, \nor  simply  a  relish.  —  F.  test,  4  the  thick  skin \nwhereby  the  kernell  of  a  walnut  is  divided,' \nCot.;  hence,  a  slice  of  lemon-pccl.  —  L \nschist  us,  schistos,  lit.  cleft,  "
---
3065452 ' (1). \n\nFrench  from  Low  Latin  from  Persian : \nzedoary. \n\nItalian  from  Persian :  scimetar  (cime- \nter)?. \n\nFrench  from  Italian  from  Persian :  car- \ncase  (carcass),  jargonelle,  mummy,  orange, \nrebeck,  taffeta  (taffety),  turquoise  (turkoise). \n\nFrench  from  Spanish  from  Persian: \njulep,  saraband. \n\nEX \n\n\nDigitized  by  Google \n\n\n6io \n\n\nVI.   DISTRIBUTION  OF  WORDS,  ETC. \n\n\npagoda,  ve- \n\n\nPortuguese  from \nranda  (verandah)  ?. \n\nFrench  from  Portuguese  from  Persian  '
---
```


## [2026-09-07T18:24:52.499Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\ntxt=open('skeat1882.txt',encoding='utf-8',errors='replace').read()\nseg=txt[1600000:1612000]\nfor m in re.finditer(r'\\n\\s*(\\d{3})\\s*\\n',seg):\n    print(1600000+m.start(), m.group(1))\nEOF",
 "description": "Find page numbers near Orange in Skeat 1882"
}
```


### [2026-09-07T18:24:53.737Z] TOOL RESULT

```
1604982 317
```


## [2026-09-07T18:24:58.464Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\ntxt=open('skeat1882.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'ORAL|ORANGE|OPULENT|ORB|Digitized  by  Google',txt[1600000:1615000]):\n    print(1600000+m.start(), m.group(0))\nprint('---- context around 1604982')\nprint(repr(txt[1604700:1605400]))\nprint('---- context after orange, look for headers')\nprint(repr(txt[1606900:1608600]))\nEOF",
 "description": "Locate page markers"
}
```


### [2026-09-07T18:24:59.857Z] TOOL RESULT

```
1604935 Digitized  by  Google
---- context around 1604982
'ee  Ere. \n\nOr  (3\\  gold ;  see  Aureate. \n\nOracle ;  see  Oral. \n\nOral,  spoken.  (L.)  Coined  from  L.  or-, \nstem  of  os,  the  mouth. +Skt.  isya,  mouth, \ndnana,  mouth.  (^AN.) \n\nadore.  (L.)    L.  adorare,  to  pray  to.— \n\n\nDigitized  by  Google \n\n\nORANG-OUTANG. \n\n\nORE. \n\n\n317 \n\n\nL.  ad,  to ;  orare,  to  pray,  from  or-,  stem  of \nos,  the  mouth. \n\ninexorable.  (F.-L.)     Y.  inexorable. \n\n—  L.  inexorabilis,  that  cannot  be  moved  by \nintreaty.  —  L.  in-,  not ;  ex-orare,  to  gain  by \nintrcaty. \n\noracle.  (F.-L.")  F.  oracle. -L.oracu- \nlum,  a  divine  announcement ;  double \ndimin.  formed  from  ora-re,  to  pray  (above). \n\noration.  (F.-L.)  F.  oration.  —  '
---- context after orange, look for headers
'. \nAllied  to  Pers.  ndr,  a  pomegranate. \n\nOration,  Orator ;  see  Oral. \n\nOrb.  (F.  — L.)  F.  orbe.  —  h.  orbem,  acc. \nof  orbis,  a  circle,  sphere. \n\nexorbitant,  extravagant.  (F.-L.)  F. \nexorbitant.  —  L.  exorbitant-,  stem  of  pres. \npt  of  exorbitare,  to  fly  out  of  a  track.  —  L. \nex,  out ;  orbita,  a  track  (below). \n\norbit.  (L.)  L.  orbita,  a  track,  circuit ; \nformed  with  suffix  -fa  from  orbi-,  crude \nform  of  orbis,  an  orb,  circle. \n\nOrchard ;  see  Wort. \n\nOrchestra.  (L.-Gk.)   L.  orchestra.  - \n\n\nGk.  6pxfi<rrpa,  an  orchestra ;  which,  in  the \nAttic  theatre,  was  a  space  on  which  the \nchorus  danced.  — Gk.  vpxiopat,  I  dance. \n\nOrchis,  a  plant.  (L.—  Gk.)   L.  orchis.— \nGk.  <"/>\\\'f>  a  testicle,  a  plant  with  roots  of \ntesticular  shape.    Der.  orchid,  a  false \nform,  since  the  gen.  case  of  Cpx*  is \nbpx^on. \n\nOrdain ;  see  Order. \n\nOrdeal ;  sec  Deal. \n\nOrder.  (F.-L.)  F.  ordre,  O.  F.  ordine. \n\n—  L.  ordinem,  acc.  of  ordo,  order.  Per- \nhaps allied  to  Origin.    Der.  dis-order. \n\nco-ordinate.  (L.)  L.  co-  (for  cum), \ntogether;  ordinatus,  arranged,  pp.  of \nordinare;  see  ordain  (below). \n\nextraordinary  (L.)  L.  extra-ordi- \nnanus,  beyond  what  is  ordinary,  rare. \n\ninordinate.  (L.)  L.  in-,  not;  ordi- \nnatus, ordered,  controlled,  pp.  of  ordinare ; \nsee  ordain  (below). \n\nordain,  to  set  in  order.  (F.  —  L.)  M.  E. \nordeinen.  —  O.  F.  ordener  (later  ordonner). \n\n—  L.  ordinare,  to  set  in  order.  —  L.  ordin-, \ncrude  form  of  ordo,  order.  Der.  pre- \nordain. \n\nordinal,  shewing  the  order.  (L.)  L. \nordinalis,  adj.,  in  order.'
```


## [2026-09-07T18:25:14.592Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ntimeout 60 curl -s \"https://archive.org/metadata/in.ernet.dli.2015.158267\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin); print(d.get('server'),d.get('dir'))\nmd=d.get('metadata',{}); print(md.get('title'),'|',md.get('year'),'|',md.get('creator'))\nfor f in d.get('files',[]):\n    if f['name'].endswith('djvu.txt'): print(f['name'],f.get('size'))\n\"",
 "description": "Check DLI Skeat copy"
}
```


### [2026-09-07T18:25:16.213Z] TOOL RESULT

```
ia800404.us.archive.org /21/items/in.ernet.dli.2015.158267
A Concise Etymological Dictionary Of The English Language | None | Walter W. Skeat
2015.158267.A-Concise-Etymological-Dictionary-Of-The-English-Language_djvu.txt 2985742
```


## [2026-09-07T18:25:20.331Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ntimeout 180 curl -s -o skeatdli.txt \"https://ia800404.us.archive.org/21/items/in.ernet.dli.2015.158267/2015.158267.A-Concise-Etymological-Dictionary-Of-The-English-Language_djvu.txt\" && python3 - <<'EOF'\nimport re\ntxt=open('skeatdli.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('Orange.')\nprint(i)\nprint(repr(txt[i-2500:i+900]))\nEOF",
 "description": "Search DLI Skeat for Orange with page number"
}
```


### [2026-09-07T18:25:22.661Z] TOOL RESULT

```
1595161
" \nnear; '^pedum ((rk. trihov'), a field, plain; L. opiionem, acc. oi optio, choice. Allied \nBrugm. i. § 65. (Explained as ‘ protecting to L. optdre, to wish ; see Optative. \n\nthe plain’ ; the derivation is clearer than Opulent, wealthy. (F.-L.) F. opu- \nthe sense.) ^ lent. — L, opulentus, wealthy. — L. op-, base \n\nOppilatiou, a stopping up. (F.-L.) of opes, wealth. Cf. Skt. apnas. wealth, \n\nM. l^ ‘ an obstruction ; ’ Cot.- Or (i), conj,, offering an alternative. \n\nL acc. oppildtibnem. oppildius, pp. of (E.) Short for other, out her, anther, the \noppildre, to stop up. — L. op (for ob), M. E. forms, which answer to A. S dhwee- \nagainst ; plldre, to ram, from pilum, a pei , dwper. Bat this M. E. took the \njiestle. And L. plluin is for *pins-lom, place of A. S otibe, or. \n\nfrom pinsere, to -pound. Or (2\\ eie. (E.) M. E. unemphatic \n\nOpponent. (L.) L. opponent-, stem of form of er, ere. A. S. ier, ere ; see Ere. \npres part, of opponere, to oppose. — L. ob, (In the phrases or ere, or ever.) \nagainst ; to place. vSee Position. Or (3), gold. (F.-L.) In heraldry. ¥. \nOpportune, timely. (F. — L.) F. op- <7r. — L. aurum, gold. \nportun.-^G. opportnnus, convenient, sea- Orach, a pot-herb. (F. — L. — Gk.) \nsonable, lit. ‘ near the harbour,’ or ‘ easy of N\\so arrache — F arroche, ‘ orache, orage;’ \naccess.’ — L. op- (^7<5),near; portus, access, Cot A Picard form corresponding to F. \nharbour. See Port (2). ^ (Hatzfeld). [Cf Walloon ar*>, \n\nOppose. (F. — L. ««^/Gk.) Y.opposer, orach (Remade); Ital. atrepice'\\ G. \nto withstand. — L. (for ^7^), against ; F. atriplicem, acc. of atriplex, orach. — Gk. \nposer, to place, from Late G.paus&re, used drpdi^i?, drpdipofus, orach, \nto translate G.pdnere, to place. See Pose. Oracle. (F.—L.) F. oracle. •^G, ord- \n^PPOSite. (F. — L.) F. opposite. culum, a divine announcement; formed \n\n359 \n\n\n\nORGAN \n\n\nORAL \n\nfrom drd^re, to pray, from dr- (for ds\\ the of testicular shape. Der. orchid, where \nmouth (below). the suffix -id was suggested by the Gk. \n\noral, spoken. (L.) Coined from L. €?5or, shape; di. cyclo-id, cono-id, \n\n(for the mouth. + Skt. mouth ; Ordain, to set in order. (F.— L.) \nIcel. dss, mouth of a river. M. E. ordemen.-O. F. ordener (later \n\nOrangf-OUtanff, a large ape. (Malay.) donner).^\\u, ordindre, to set in order.— \nyiBXQ.y drang-utan^ii. ‘ wild man ’ — Malay L. ordin-, declensional stem of ordo^ order. \ndrang, a man ; iiCan, hufan^ woods, wilds “Der, pre-ordain. \n\no^ country, wild. Ordeal, a seveie test, judgment by fire. \n\nOrange. (F. - Ital. - Arab. — Pers.) &c. (E.) M. E. ordal. A. S. ord?l, ordal, \n\n0 F. orengc {^.orange). ¥ oi *narenge, a dealing out, judgment, decision. O. \nbut the initial n was lost (m Italian), and Friesic ordel.-h. S. or-^ prefix, out ; ddl, \nthen arenge became oi-en^e by a popular ddl, a dealing ; see Deal, Dole. The \netymology from or, gold. Cf. Span, wnt- prefix oi-^Du. oor-, G. nr-, Goth, us-, \nranya, an orange, ’^Ital.arancia, an orange; out (hence, thorough V •+• Du. oordeel. \nLow Lat. arangia.’^ hxdn, ndi^anj, nd- O. Sax. w/y/i?//, G. judgment; simi- \nrz;/y. — Pers. ndrang, an orange. Allied larly compounded. \n\nioVer^. ndr, a pomegranate. Order. (F.-l..) F. ordre, O. F. or- \n\nOration. (F. — L.) ¥. oration. dine.—^¥. odinetn, acc. of ordo, order. \n\nordtidnem\\ cf. drdtus, pp. of ordre, to Allied to L. ordfri, to begin, orlri, to \npray. — L. dr- (for ds\\ the mouth. .See arise B"
```


## [2026-09-07T18:25:51.258Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://ia800404.us.archive.org/21/items/in.ernet.dli.2015.158267/2015.158267.A-Concise-Etymological-Dictionary-Of-The-English-Language_djvu.txt\" --note \"page 349: Skeat, Concise Etym. Dict. (DLI copy) p.360 s.v. Orange = Nourai's SKT:360\" >/dev/null\ncd data/verification/sources/refs\necho \"=== LEW nonnus / nanus\"\ngrep -n \"nonnus\\|nonna\\|nānus\\|nanus\" LEW_1910.txt | head -10\necho \"=== LAT nonnus/nanus\"\ngrep -n \"nonnus\\|nonna\\|nanus\" LAT.txt | head -10\necho \"=== SYN mother section\"\ngrep -n \"^2.36\\|2\\.36 MOTHER\\|MOTHER\" SYN.txt | head -10\necho \"=== IEC nana\"\ngrep -n \"^nana\\|^nanà\\|nanà\\|nana \" IEC.txt | head -10",
 "description": "Latin dicts, Buck, Mann for nana/nonna/nanus"
}
```


### [2026-09-07T18:25:53.732Z] TOOL RESULT

```
=== LEW nonnus / nanus
=== LAT nonnus/nanus
1100:Derivas artificiels: accipitro,-ds, Laevius; accipetrina (scii.nanus).
3837:posta po6tiques: anguifdr (= ocpi.ou)(OC); -ger; -gena; -nanus, -pes. S'y
7669:eo quod ab umeris ad nanus breuiores sunt quan a coxis plantae. Noter
18142:5,1360, atque opere in duro durarent nenbra nanusque, en face de Vg.,
21654:frapper 1'ennemi, nn nnr, la nonnaie, nne victime, a la porte; frapper
35918:quo nanus lauantur; malluuiae quibus manus sunt lotae; pelluuiae quibus
36263:manuciolum (-lus, v. nanus). Atteste depuis Pl. Les formes romanes re-
38879:nonna, monnula, -ae f. (bas latin): terne de tendresse, de ca~
38880:ractere populaire, a geminee expressive. Cf .nonnus, -a, etc.Dey.ova?
40312:quo postea accessit nanus {magnus cod. * nagnus, nannus) cum Graeco
=== SYN mother section
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2781:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 103 2.35 2.36 2.37 FATHER MOTHER PARENTS
2813:2.36. ‘Mother’. 1. IE *mdter-, prob.
2936:2.47 GRANDMOTHER
3377:2.61 FATHER-IN-LAW 2.62 MOTHER-IN-LAW
3615:128 SELECTED INDO-EUROPEAN SYNONYMS 2.71 2.72 2.73 2.74 STEP. STEPFATHER STEPMOTHER STEPSON DAUGHTER Grk.  (unrputés, rarpuiés) rout FESTOS f mpdyovos, Tpoydyn NG pytpuiés pnTpu Tporyoves, wrpoyore Tpoyorn, mpoydre Lat. _vitricus, patrasler noverca, matraster Gi eed Silidster es Me Sfiliastra | It. patrigno matrigno fightastro igliastra Fr. beau-ptre belle-mére (mardtre) beau-fils belle-fille Sp. padrastro madrastra hijastro hijastra Rum. até vitreg mamé vitregd fiu vitreg fatd vitregé Ir. lessathair lesmathair lesmac lessingen Nir. __leasathair leasmhathair leasmhac leasinghean W. llysdad llysfam llysfab Uysferch a ' lez-tad lez-vamm lez-vab lez-verc’h Obhas es otek Aas 2 Aiea a ee ee ane stjipr stjipdottir | an.  stiffader stifmoder slifson stifdatter Sw. styffar styfmoder styfson styfdoiter es Sie oe pee Se is | slepsone stepdou; te; NE stepfather stepmother stepson jenni Du. sliefvader stiefmoeder sttefzoon stiefdoehter OHG  stiuffater stiufmuotar sliufsun stiuftohter MHG stiefvater sliefmuoter sltiefsun stieftohter me a ies stiefsohn stieftochter ‘ pamote ostinis d Lett. patévs pamdate naaels ees ChSl.  oliéimii, oltéuchtt mastecha pastoriiku pastortika (pa- : : duiSz) See Le ; maceha pastorak pastorka oh.  nevlasint otec, olfim  nevlastnt matka, macecha nevlastni syn, pastorek nevlastnt dcera, : pastorkyné ec tte ard a aie i ; asyno. y Skt. _ (tata- yaviyan-) pee lai Av. pone
=== IEC nana
11526:nanå “mother, nurse, foster-parent'. WP II, 317 Skt. nanà ‘mother’; Per. cf. nānā (“maternal grandfather' sic!); Oss. naná *mother, grand- mother; Gk. (expressive) nánne ‘maternal aunt; Alb. nán&, T nënë ‘mother’; W nain, pl. neiniau, neinoedd ‘grandma’; neina, f sg. id.
```


## [2026-09-07T18:26:02.162Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 2.36\"\nsed -n '2813,2830p' SYN.txt\necho \"=== LAT nonna ctx\"\nsed -n '38875,38890p' LAT.txt\necho \"=== LAT nanus ctx\"\nsed -n '40305,40320p' LAT.txt",
 "description": "Buck MOTHER, Ernout-Meillet nonna/nanus"
}
```


### [2026-09-07T18:26:02.261Z] TOOL RESULT

```
=== SYN 2.36
2.36. ‘Mother’. 1. IE *mdter-, prob.
starting fr. a nursery word of the pa type (above, p. 94) orig. pd, reduced to pa before the accent. Walde-P. 2.4. Here belong the Grk., Lat., Ir., Gme., and Indo-Iranian words, also Arm. hair, and Toch, A pacar, B pacer. In Balto-Slavic it is completely replaced. 2. Nursery words that have become oe usual terms. Type baba (above, p. ) in It. babbo, now a serious rival of padre, nes atta, tata (above, p. 94) in Rum. an ., Br. tad, Goth. atta (So reg., Vs. ihe) te and here not of earthly » Lith. tévas, Lett. tévs, OPruss.
taws, ChSl. otict , 3 , ete. (all the Balto- Slavic forms), Hitt. fae aad
starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
Goth. aipei, prob. new fem. formed fr. some nursery word similar to, though not identical with, atta ‘father’. Feist 28.
Digitized by Arya Samaj Foundation Chennai and eGangotri
104 SELECTED INDO-EUROPEAN SYNONYMS
2.37. Words for ‘parents’ are fr. verbs for ‘beget’ or ‘bear’ (4.71, 72); fr. words for ‘old’; or are pl. or du. forms (the lat- ter, of course, more orig.), or derivs., of words for ‘father’, or rarely ‘mother’.
1. Grk. roxets (so reg. Hom.), or aor. pple. rexdvres : rixrw ‘beget, bear’ (4.71).
Grk., NG yovets : yiyvouat ‘be born’, yevvaw ‘beget, bear’ (4.71).
2. Lat. parentés (also ‘ancestors’, late also ‘relatives’), pres. pple. of par- in parere ‘bear, beget’ (4.72). Hence Rum. parinti ‘parents’, Fr. parents formerly ‘parents’ and ‘relatives’ (> ME paren- tes, NE parents), now ‘relatives’ (as ‘parents’ replaced by pére et mére), as also It. parenti, Sp. parientes. REW 6233.
Lat. patrés (as also Grk. rarépes) was commonly used for ‘forefathers’ and oc- casionally in late times for ‘parents’. Hence Sp. padres.
Lat. genitor ‘begetter, father’ : gig- nere ‘beget’, etc. Hence It. genitori.
3. Ir. tuistidi, NIv. tuismhightheoiri : Ir. do-fuismim ‘beget, bear’ (4.71).
W. rhieni (formerly also ‘ancestors’), epd. rhi-eni : gent ‘be born’, Lat. gig-
nere, etc., formed like Grk. mpéyovor ‘an- cestors’. Pedersen 2.533. Br. tad ha mam, after Fr. pére et mére,
4. Goth. bérusjés, orig. a nom. pl. fem. perf. act. pple. of bairan ‘bear’, For the fem., cf. Skt. mataradu, below. Feist 87 f.
=== LAT nonna ctx
de "nuque, cou". Le mot p,txvUOtxriS designe en grec le "collier" porte
par des guerriers barbares; il doit etre d'origine gauloise; cf. aus -
si jxavvos ou p.ovvo£ atteste par Pollux V 99 et par le scholiaste de
Theocrite XI 41.
nonna, monnula, -ae f. (bas latin): terne de tendresse, de ca~
ractere populaire, a geminee expressive. Cf .nonnus, -a, etc.Dey.ova?
- mono-: prefixe grec (de p,ovo£ "seul") qui a basse epoque a servi
a former des composes hybrides du type monoculus (Firm.) = p,ovocp8a\|j,oc;,
conserve dans quelques dialectes italiens, M.L.5GG3 (Plaute dit uno¬
culus)', nonosolis (Ed. de Diocl^tien) de p,. et solea: soulier a semelle
simple; monoloris (Vopisc.) de |a. et lorum', nonomarlta (inspr*)*
L'epoque republicaine connaissait deja 1 ’adj. monogrammus "fait'uni -
quement de lignes, ebauche, decharne" (Lucii., Cic. ).
mons, montis m. (theme en -i, anc.abi. monti, gen.pl. montium): mont,
montagne. — Usite de tout temps. Panroman, M.L.5GG4; v.angi, munt.
— Deja rapproche de emineS par Isid. Or.14, 0 ,1.
=== LAT nanus ctx
n»r«s
fourni ob-iioxius "enclin A, au j et i" (t. ce aot); pour le sena, cf.
gr. 7to6’-r)ve>eTjC> 8 l—r\vewr] C. Ce aot a aubi 1'influence de noxa.
n&nus, -i a. (nannus), nSna, -ae f.: nain, naine. Eaprunt au gr.
vavoc, vavvoc (le aot lat. e8t pumilis, cf.Geli. 19,13,«). MSnus apparaat
pour la preaibre fois dans Varr., L.L.5,119, o4 il ddaigne nn raae
grotesque, aans doute en fprae de nain: uos aquarium uocant' futim...
quo postea accessit nanus {magnus cod. * nagnus, nannus) cum Graeco
nomine, et cum Latino nomine Graeca figura barbatus ; cf. P.F.185,8,
nanum Graeci toas aquarium dicunt humilem et concauum, quod uulgo
situlum barbatum, unde nani pumiliones dicuntur. -Manus paaaait pour
rulgaire; il ae diaait anasi de8 cheraux et anlets naina, cf. Geli.
1.1. ** Panroaan, aanf rouaain, M.1.58x9« Iri. nan.‘
naphtha(a), -ae f.: naphte Mot dtranger: ita appellatur circa
Babylonem et in Austacenis Parthiae profluens bituminis liquidi modo.
(Plin.3,335), venu par le gr. vaqj0cx(c).
```


## [2026-09-07T18:26:14.823Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM نارنج\"\ngrep -n \"نارنج\\|النارنج\" AFM_pages.txt | head -10\necho \"=== PLA naranj\"\ngrep -n -i \"naran\\|nārang\\|nāranǧ\" incoming/PLA/PLA_pages.txt | head -10\necho \"=== LKT orange/naranj\"\ngrep -n -i \"narang\\|naranǧ\\|Orange\\|arancia\\|naranja\" LKT.txt | head -20",
 "description": "Arabic-loan sources for naranj"
}
```


### [2026-09-07T18:26:14.897Z] TOOL RESULT

```
=== AFM نارنج
=== PLA naranj
14409:at       -       näran g:          "Orange"                  aus    pers.       ai narang            ”      m.         RAW   anar "Granat-
14411:       sp.           naranja,            port.           larange          9% dtsch.           Orange,        ndl.       Orange     10         it.
14413:       arancia,              rum.           naranta,               dtsch.       Aurantium            11
=== LKT orange/naranj
260:'Mensch',  dann  N.  pr.  für  den  Stamm- vater des  Menschengeschlechtes  [vgl. assyr.  admu  'Kind,  bes.  junges  Kind' Del  HWB  25  b],  daraus  bei  den  Ana- tomen des  Mittelalters  hebr.  iappü"h ha-ädäm,  wörtlich  'Apfel  des  Mannes', zur  Bezeichnung  des  Vorsprungs  am Kehlkopf  des  Mannes  [gr.  irpöXoßo;]. Da  er  nur  am  Halse  des  Mannes  zu sehen  ist,  ist  der  Name  treffend  ge- wählt, dann  aber  durch  mißverständ- liche Übersetzung  zu  Pomum  Adami 'Adamsapfel'  geworden  und  die  bekannte Fabel  entstanden,  daß  Adam  den  ihm hingereichten  Apfel  nicht  ganz  habe verschlucken  können.  Ii. morso d'Adamo, frz.  morceau  d' Adam,  pomme  d'Adatn. Engl.  Ada7n's  apple,  schwed.  adanis aepple,  dän.  adams  üble,  ndl.  adanis  appel. Poln.  jabiko  Adamowe,  ßech.  Adamavo jahlko.  Im  Angloind.  ist  Adanis  apple die  Frucht  von  Mimusops  Elengi  L., im  It.  joomo  d'Adamo  [od.  pomo  di  para- diso]  eine  Orangenart,  Citrus  decumana. [Kluge  6.  Hobson-Jobson  4.  HArllebr- An  164.
3580:'Aptelsine'  [vielleicht  aus  •s.sVr .ndgarant^a 'Elefantenneigung',  d.  h.  Lieblingsfrucht der  Elefanten,  vgl.  Lassen,  Indische  Alter- tumskunde I,  247];  hieraus  über  das gleichlautende  ar.  Wort  sp.  naranja, pg.  laranja,  kat.  naronja,  rum.  näranfä, it.  arancia  'Apfelsine',  Adj.  rancio 'orangegelb',  [mit  Anlehnung  an  or  mit Bezug  auf  die  goldgelbe  Farbe]  frz. orange;  dtsch.  Orange,  ndl.  oranje, oranjeappel,  -boom,  engl,  orange,  poln. or«»^i;  aus  mlat.  pomarancia  <^  it.  pomo 'Apfel'  und  arancia  wurde  dtsch.  Pome- ranze. [DE  324.  Eguilaz4(;3.  ML  5822. Hobson-Jobson  642/643.  Kluge  332.  349.
4883:2185.  Ar.  zahr: 'Orangenblüte'  [vom  Vb.  zahura  'leuch- ten, weiß  schimmern'],  plr.  azhär;  hier- aus teils  mit,  teils  ohne  ar.  Art.  sp. azahar  'dass.',  zahor  'glänzende,  weiße Farbe',  pg.  azar  branco  'Art  Anemone', Abltg.  azareiro  'Kirschlorbeerbaum',  it. zaghera,  siz.  zagara  'Orangenblüle'.  [DE 223/234.  Eguilaz  318.  ML  9594.  Gr SVociSic  249.
5853:Ortfse  2152 Odaliske  1586 Oo;h//.9  (^ree;  1889 0/j«Z  2135 Orange  1555 Orang-Utang  1593 Organdi(n)  2137 Oryxantilope  2113 Osmanen  2144 Ottomane  2l44
6118:orange  1555
6646:)  orange  1555
7442:Pacorus  569 pallaca  203 pandura  2015 paradisum  1631 pascha(Ks)  1652 pastinaca  912 pelusia  1647 penidium  583 jp?M^e«  887 pomarancia  1555 pontica  (niix)  355 pyramis  1457
```


## [2026-09-07T18:26:26.929Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT entry 1555 full\"\nsed -n '3574,3584p' LKT.txt\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:3579])\nleaf=txt[:pos].count('\\f'); print('LKT leaf',leaf,'printed',leaf-26)\nEOF\necho \"=== PLA context\"\nsed -n '14400,14420p' incoming/PLA/PLA_pages.txt\npython3 - <<'EOF'\nimport re\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:14408])\nm=None\nfor mm in re.finditer(r'\\[pdf page (\\d+)\\]',txt[:pos]): m=mm\nprint('PLA pdf page',m.group(1) if m else '?')\nEOF",
 "description": "Lokotsch 1555 and Asbaghi naranj"
}
```


### [2026-09-07T18:26:28.292Z] TOOL RESULT

```
=== LKT entry 1555 full
'Gebet'  [Horn  NpEt  S.  233,  Nr.  1040], ebenso  tk.  nemaz  'Gebet'  [das  rituelle Gebet  der  Muslimen];  hieraus  rum.  na- mas  'dass.';  sp.  namaz,  namazi  [Dicc Gast  1406  c].
1553.  Pers.  nänii:
'Mutter'  [Horn  NpEt  .S.  234,  Nr.  1044], ebenso  tk.  nene;  hieraus  rum.  neneacä 'dass.',  nene  und  demin.  wen/for 'Trauter' als  Anrede  an  den  älteren  Bruder  oder Verwandten.
1554.  Chili.  Nau-kiiis::
N.  pr.,  große  Stadt  am  Unterlauf  des Jang-tse-kjang,  wörtlich  'südlicher  Hof, d.  h.  Hauptstadt  des  Südens  [wie  Peking 'Hauptstadt  des  Nordens'];  nach  dieser Stadt  wurde  ein  baumwollener  Stoff  von bräunlich-gelber  Farbe  mit  meist  ka- riertem Muster  benannt,  da  er  hier  ur- sprünglich ausgeführt  wurde  Engl. 7iankin,narikeen,  disch.  Nanking,  Nankin, ndl.  nanking;  frz.  nankin;  poln.  serb. nankin,  6e  'h.  nankyn,  aber  russ.  nanka 'chines.  Leinwand'.  [Hobson  Jobson  6 16. Hirth  ChinFW  209.
1555.  Pers.  iiäräng::
'Aptelsine'  [vielleicht  aus  •s.sVr .ndgarant^a 'Elefantenneigung',  d.  h.  Lieblingsfrucht der  Elefanten,  vgl.  Lassen,  Indische  Alter- tumskunde I,  247];  hieraus  über  das gleichlautende  ar.  Wort  sp.  naranja, pg.  laranja,  kat.  naronja,  rum.  näranfä, it.  arancia  'Apfelsine',  Adj.  rancio 'orangegelb',  [mit  Anlehnung  an  or  mit Bezug  auf  die  goldgelbe  Farbe]  frz. orange;  dtsch.  Orange,  ndl.  oranje, oranjeappel,  -boom,  engl,  orange,  poln. or«»^i;  aus  mlat.  pomarancia  <^  it.  pomo 'Apfel'  und  arancia  wurde  dtsch.  Pome- ranze. [DE  324.  Eguilaz4(;3.  ML  5822. Hobson-Jobson  642/643.  Kluge  332.  349.
1556.  Pers.  iiärgilä: 'Wasserpfeife'  [angeblich  aus  sskr.  nä- rikera  'Kokosnuß'];  hieraus  engl,  nar- gula,  nargileh,  narghile;   frz.  narguiU,
kat.  nargili,  sp.  narguile,  rum.  narghilea 'dass.';  poln.  nargile.  [Eguilaz  463. ML  5823a.    Hobson-Jobson  618.
lf)57.  Pers.  närh: 'Preis,  Wert'  [Horn  NpEl  S.  230.  Nr.  1027], ebenso  tk.  nark  'Preis,   feste  Taxe'; hieraus  rum.  nart  'Taxe,  Steuersatz'.
1558.  Ar.  na's:
LKT leaf 153 printed 127
=== PLA context

Aust         _       närmask:            "eine          wohlriechende                 Blume"               pers.ui,b         em                   < mp.
       .„kı           anar       "Granatapfel"                      +    4 moSk         a     syr.    Ans.        (P. Sub)
                                                                                                                      Suse


Aubs,b       -       närmak:             "Pome           granate          rhus    Vermicifera"               6_     närmask        q.      V.«.


at       -       näran g:          "Orange"                  aus    pers.       ai narang            ”      m.         RAW   anar "Granat-
       apfel"           + mp.               >»        rang    "Farbe",          mand.        narniz        (p.   a!       8
       sp.           naranja,            port.           larange          9% dtsch.           Orange,        ndl.       Orange     10         it.

       arancia,              rum.           naranta,               dtsch.       Aurantium            11


&D;L - näzuk:                "Zart"               s. nizäkat.

asstl - naffa:                   "Gefäß               mit     Parfüm"             pers.asL           näfe        12 mp.          ao,    näf        13,
       syr.           ng          (pP. at)                     19,

PLA pdf page ?
```


## [2026-09-07T18:26:44.198Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 incoming/PLA/PLA_pages.txt | cat -A | head -5\ngrep -c \"\" incoming/PLA/PLA_pages.txt\ngrep -n \"\\[pdf page\" incoming/PLA/PLA_pages.txt | head -3\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:14408])\nprint('leaf',txt[:pos].count('\\f'))\nleaves=txt.split('\\f')\nprint(repr(leaves[txt[:pos].count('\\f')][:200]))\nEOF",
 "description": "Determine PLA page"
}
```


### [2026-09-07T18:26:45.522Z] TOOL RESULT

```
             Asya Asbaghi$
$
$
16027
leaf 271
'nardila                                                                         257                                                               nänha\n\n\nala,L            -    närgila:              "p'
```


## [2026-09-07T18:26:49.816Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV ORANGE\"\ngrep -n \"^ORANGE\\|Orange\\.\" DEV.txt | head\necho \"=== PHN ORANGE\"\ngrep -n \"^ORANGE\\|ORANGE\" PHN.txt | head\necho \"=== KLN orange\"\ngrep -n \"^orange,\" KLN_1966.txt",
 "description": "Devic, Pihan, Klein for orange"
}
```


### [2026-09-07T18:26:49.886Z] TOOL RESULT

```
=== DEV ORANGE
2754:Arancia ,  ital.  voy.  Orange.
2755:Arancio,  ital.  voy.  Orange.
3781:Laranja,  pg.  voy.  Orange. Lascar.
4028:Naranja,  esp.  voy.  Orange.
4029:Xaranz,  milan.  \oy.  Orange.
4030:Naranza,  vénit.  voy.  Orange.
4065:Orange.
4069:Orenge,  voy.  Orange.
=== PHN ORANGE
8207:ORANGE, 8. f. (p.)
=== KLN orange
26460:orange,  n.  —  ME.  orenge,  orange,  fr.  MF.  orenge (F.  orange),  in  pomme  d' orenge,  fr.  It.  arancia (in  Olt.  melarancia,  lit.  ‘orange-apple’),  fr. Arab,  naranj  (whence  also  Sp.  naranja.  Port. laranja,  MGk.  vcpavxOov),  fr.  Pers.  narang,  fr. OI.  ndrangah,  ‘orange  tree’,  which  is  of  uncer¬ tain  origin.  The  change  of  nar-ange  to  or-ange  is prob.  due  to  the  influence  of  the  name  of  the town  Orange,  an  important  transit  station  for the  oranges  bound  for  the  north  of  France. The  usual  explanation  that  the  change  mention¬ ed  is  due  to  a  confusion  with  F.  or,  ‘gold’  (see aurum),  must  be  abandoned  owing  to  the  fact that  originally  and  for  many  centuries  the  fruit was  called  in  French  pomme  d'orange,  which makes  it  probable  that  orange  was  regarded  as  a place  name.  See  Bloch-Wartburg,  DELF.,  p. 425  s.v.  orange.
```


## [2026-09-07T18:26:58.598Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (582,583,584):\n    print(i, re.findall(r'\\b(10\\d\\d)\\b',leaves[i])[:6])\nEOF\necho \"=== DEV Orange entry\"\nsed -n '4065,4069p' DEV.txt\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:4064])\nleaf=txt[:pos].count('\\f'); print('DEV leaf',leaf,'printed ~',leaf-30)\nEOF\necho \"=== PHN Orange entry\"\nsed -n '8207,8225p' PHN.txt",
 "description": "Klein page, Devic and Pihan orange entries"
}
```


### [2026-09-07T18:26:59.921Z] TOOL RESULT

```
582 ['1088', '1089']
583 []
584 ['1093']
=== DEV Orange entry
Orange.
Orang-Outan.
Orcanète.
Orchanel,  voy.  Orcanète.
Orenge,  voy.  Orange.
DEV leaf 291 printed ~ 261
=== PHN Orange entry
ORANGE, 8. f. (p.)
^j\i [nârindj] Fruit à pépins, à pulpe juteuse et rafraîchis-
sante, et dont l'écorce, d'un jaune doré, est d'un usage fré-
c|uent en médecine. C'est à cause de sa couleur que les
Romains l'ont appelé matum aureum [pomme d'or) y et l'on
connaît la fable du dragon préposé à la garde des pommes
du jardin des Hespérides. — L'oranger, originaire du midi296 OTT
de la Chine , fut bientôt cultivé dans l'Inde et dans la Perse ;
de là il se propagea en Europe par la Grèce, Tltalie, le Por-
tugal, l'flspagne et le midi de la France. Sa fleur blanche,
d'une odeur délicieuse, est l'emblème de l'innocence et de la
pureté. — Les oranges les plus estimées viennent de Malte
et du Portugal. — Le mot orange se rattache, dit-on, au la-
tin aurùm {or); mais cette analogie n'est pas assez précise
pour fixer l'orthographe du substantif français : il vaut mieux
en reconnaître la racine dans le persan ^j\à [nârindj]^ que-
Ton retrouve dans le grec moderne vepavrlt^ l'espagnol na-
ranja, le portugais laranja, et l'italien arancio et narancio.
0SMANLI,8. m. (t.)
```


## [2026-09-07T18:27:06.916Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"narandj\\|nârandj\\|naranj\\|nârendj\\|nârindj\" DEV.txt | head -10",
 "description": "Devic orange article"
}
```


### [2026-09-07T18:27:06.963Z] TOOL RESULT

```
1555:Jargon.  Gemme  de  couleur  jaune  tirant  sur  le  rouge, souvent  confondue  avec  VhyacintJie.  Le  minéralogiste  Haûy a  réuni  ces  deux  sortes  de  pierres  sous  le  nom  commun de  zircon.  Ital.  giargone.  Jargon  et  zircon,  dont  personne, à  ma  connaissance,  n'a  encore  établi  l'étvmoloffie,  sont certainement  identiques  à  l'espagnol  azarcon.  D'après  le Dictionnaire  de  l'Académie  espagnole,  azarcon,  en  pein- ture, signifie  orangé  vif  :  ^e\  color  naranjado  muy  encen- dido,  color  aureus;v  ce  qui  s'applique  très-exactement  à l'hyacinthe.  Azarcon  s'est  dit  aussi,  comme  le  portugais zarcâo,  zarquào,  azarcâo,  de  l'ocre  rouge.  Et  tous  ces  mots correspondent  à  un  terme  arabe,  ij^)';)  zarqoûn,  avec  l'ar- ticle az-zarqoûn,  qui  se  disait  du  minium  et  d'autres  sub-
1889:Ora>ge.  Esp.  naranja,  portug.  laranja ,  ital.  arancm. arancio  (dialecte  milanais,  naranz,  vénit.  uarauza'j,  bas grec  vepdvT^iov.  Les  formes  qui  ont  perdu  le  n  initial  l'ont sans  doute  laissé  tomber  par  suite  d'une  fausse  assimila- tion au  n  de  une,  una;  une  narange,  una  narancla,  n'ont pas  eu  de  peine  à  devenir  une  orange,  una  arancia.  Tous ces  mots  viennent  de  l'arabe  g^^U  narandj,  persan  libjb  na- reng,  même  signification.
4028:Naranja,  esp.  voy.  Orange.
```


## [2026-09-07T18:27:18.476Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:1888])\nleaf=txt[:pos].count('\\f'); print('DEV leaf',leaf,'printed ~',leaf-30)\nimport re\nleaves=txt.split('\\f')\nprint(re.findall(r'\\b(1\\d\\d)\\b',leaves[leaf])[:6])\nEOF\necho \"=== HRN narang\"\ngrep -n -i \"narang\\|nāran\\|narenǰ\\|narind\" HRN.txt | head\necho \"=== HUB narang/nane\"\ngrep -n -i \"narang\\|nāran\\|nene\\|nanā\" HUB.txt | head\necho \"=== ARY latin index NANA / NARANG\"\ngrep -n \"NANA\\|NARANG\\|NAR \" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Devic page, Horn/Hübschmann narang, ARY index"
}
```


### [2026-09-07T18:27:19.924Z] TOOL RESULT

```
DEV leaf 214 printed ~ 184
['180']
=== HRN narang
=== HUB narang/nane
9602:an die Uruckerei gelangt. Die seitdem erschienene ein-
=== ARY latin index NANA / NARANG
3503:Sag FISNAR 94S 5th! GNEO 54S J pS SNE 345 xd (SHINEE 1 JT) SNEO
4483:OLD IRISH) oS 54) 3) COCER, COCINAR qfapansin able!
5632:THROW, TURN (ENGLISH) 5S! TORNAR SPANISH) gi!
5636:: ‘TRETI TORNAR (PORTUGUESE) JW x
5799:THUNAR — (OLD SAXON) ‘pf gS
7570:GODDEF, ADDEF —(WELSH) «535 DAMAN, DAMNANAI, ANATHEMA
14436:NAR, NERT (OLD IRISH) aS 541 2' NAR PAHLAVI) 5 3h
14439:NIJER ALBANIAN) glT NAR (BALUCH) ge 3h
14623:NAIN (WELSH) 639 NANA. SANSKRIT) ey Sails
14629:| TAYE top Sad NANNY, NANA (ENGLISH) 1831
```


## [2026-09-07T18:27:24.818Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14615,14640p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== 14430-14445\"\nsed -n '14430,14445p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "ARY index around NANA"
}
```


### [2026-09-07T18:27:24.870Z] TOOL RESULT

```
NEMAY
‘REFERENCES both, NITAN, NIMUDAN, —:(PAHLAV1) «5 shy,
POKORNY, = SS™S*~*~*~*~«S NIMOTAN
MACKENZIE: NIMAIN, NIMAYUN — -(OSSETIC) 3)
(GUIDE) 117, (SHOW) 132 NAYATI, NITA., (SANSKRIT) 2 Sle
ry + be olay NITHA, NETAR
cwtloah
2 pS ha Ada at esl 2 05s col ee
NAIN (WELSH) 639 NANA. SANSKRIT) ey Sails
NANE, NEN (ALBANIAN) giJT NANNA, NINNE, (GREEK) gli
NENNOS
‘REFERENCES ecnthany NONNUS, NONNA LATIN) 3
POKORNY. SS*~*~<CS~*~S*«SS NUANJA RUMANIAN) «ploy,
MALLORY & ADAMS: —_N-HEN, N-AN NENNE (GERMAN) git
| TAYE top Sad NANNY, NANA (ENGLISH) 1831
YYVER-TYVEE hice aalicadd NJANJA RUSSIAN) .g+5,
| NENI :(BULGARAIN) 5 ,\6,
[pdf page 502]
aS VWuIOVv
orf cases
dentlsay
sh (ISO) GAT 345 29 la cal
Bap hb 6 sy OY5 22 05s cal
(OLD HIGH GERMAN) of galT NAVO, NAVA AVESTAN) gle 3)
NIUWE OLD PERSIAN) ikal go
NEU (GERMAN) glaST NEUWENEN, NAUNS
=== 14430-14445
es ay pp Me)-ogg |
[wae ten yr le |
7 NRAVE NAR, NARA, HAVESTAN) glen)
NORIU, NORETI, :(LITHUANIAN) iy} NAIRYA
NORAS, NARTSAS {OLD PERSIAN) istry p+
NERTIEN —:(OLD PRUSSIN) oS 3.4 MARTIYA, NAR
NAR, NERT (OLD IRISH) aS 541 2' NAR PAHLAVI) 5 3h
NER WELSH) 635 NAR, NALE, NAL -(OSSETIC) 4!
NERZA ABRETON) 5.x NER, NER KURDISH) 53,5
NIJER ALBANIAN) glT NAR (BALUCH) ge 3h
NAR, NARINA (AFGHAN) (34) 343)
‘REFERENCES ant heng NAR, NARAH, (SANSKRIT) 2 Site
POKORNY, = SOSOSC*~S~*~«SS NARYA
MACKENZIE: (MALE) 122 AIR, ARN ARMENIAN) gs \
BUCK: 85, 81, 139 NOREI, ANDROS HGREEK) gb y
AMINDAROV: (MALE) 251 NERO, NERIOSUS, (LATIN) g3'Y
```


## [2026-09-07T18:27:31.691Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"NONNUS\\|NENNOS\\|NJANJA\\|NANNA\" incoming/ARY/ARY_pages.txt | head\necho \"--- and 754\"\ngrep -n \"NANA\" incoming/ARY/ARY_pages.txt | head",
 "description": "ARY main text nana family"
}
```


### [2026-09-07T18:27:31.742Z] TOOL RESULT

```
--- and 754
```


## [2026-09-07T18:27:43.838Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor target in (14623,14436):\n    pos=sum(len(x)+1 for x in lines[:target-1])\n    m=None\n    for mm in re.finditer(r'\\[pdf page (\\d+)\\]',txt[:pos]): m=mm\n    print(target,'pdf page',m.group(1) if m else '?','-> printed',int(m.group(1))+1 if m else '?')\nEOF",
 "description": "ARY pdf pages for nana and nar"
}
```


### [2026-09-07T18:27:45.561Z] TOOL RESULT

```
14623 pdf page 501 -> printed 502
14436 pdf page 495 -> printed 496
```


## [2026-09-07T18:27:51.084Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%D8%AC/\" \\\n \"https://abadis.ir/fatofa/%D9%86%D9%86%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A7%D8%B1/\" \\\n \"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%DA%AF/\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 349: Mo'in/Dehkhoda entries for narenj, naneh, anar, narang (Nourai refs MON, BQT:2095)\"; done",
 "description": "Fetch Mo'in/Dehkhoda entries"
}
```


### [2026-09-07T18:28:00.531Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fb7349303ddeb15a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4c5e9894021de8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49b4f9bc7449ed85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55f601744b4ff46e.txt
```


## [2026-09-07T18:28:04.048Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in fb7349303ddeb15a d4c5e9894021de8c 49b4f9bc7449ed85 55f601744b4ff46e; do\necho \"########## $f\"; grep -n \"معین\\|فرهنگ معین\" -A6 $f.txt | head -30; done",
 "description": "Extract Mo'in sections"
}
```


### [2026-09-07T18:28:05.384Z] TOOL RESULT

```
########## fb7349303ddeb15a
26: نارنج. [ رَ / رِ ] ( اِ ) بفتح «ر» ( و در لهجه مرکزی به کسر ). کردی ، نارنج ، نارنگ . گیلکی ، نارنج. نارنج معرب «نارنگ » است. اصل این لغت هندی است ولی از راه زبانهای ایرانی وارد زبانهای اروپائی شده به صورت اُرانژ و آرنج واُرَنجه و... درآمده و آن از انواع مرکبات است به صورت درختی با میوه های گرد ( که در سطح آن فرورفتگی هائی دیده می شود ) زردرنگ و ترش مزه. ( برهان قاطع چ معین حاشیه ص 2095 ). معرب نارنگ. ( آنندراج ) ( فرهنگ نظام ) ( شمس اللغات ) ( زمخشری ). میوه ای است گرمسیری از اقسام مرکبات ترش و گردشکل است نارس آن سبز و رسیده اش زرد می شود، در جنوب و شمال ایران جاهائی که در زمستان یخ زیاد بندد به عمل می آید. ( فرهنگ نظام ). بادرنگ. ( مهذب الاسماء ). معرب از نارنگ فارسی است ریشه و پوست درخت و پوست نارنج و شکوفه و تخم او در دوم گرم و خشک و ترشی او در آخر دوم سرد و خشک و با لزوجتی که موافق سینه و نزلات و سرفه حار است و در برگ و پوست او تفریح عظیم و جمیع اجزای او در همه امور بهتر از ترنج و ضماد پوست زرد او با سرکه جهت دردسر مجرب است و شرب یک درهم و نیم آن که خشک کرده باشند با آب گرم جهت پیچش و اخراج کرم شکم و قی و غثیان از مجربات و ضماد پخته مهرای نارنج بتمامه جهت جرب و حکه و جوششهای سر و نرم کردن موی جلد و بدن بی عدیل و بوئیدن او و برگ آن رافع طاعون و فساد هوا و آب خیسانیده پوست و شکوفه او جهت عسر ولادت مجرب و حمول آن مدر حیض و شرب او رافع سم عقرب و هوام و ترشی او با شکر مسهل صفرا و مدر آن و رافع خمار و امراض حاره عصب غیرصحیح و اکثار او مضعف جگر ومصلحش عسل و شکر و دو درهم از تخم مقشر او تریاق گزیدن جانوران و به دستور شرب ریشه های باریک درخت او با شراب همین اثر دارد و در سایر منافع مانند ترنج و لیمو است و ضرر نارنج به اعصاب کمتر است و روغن نارنج که پوست او را با شکوفه و روغن کنجد سه هفته در آفتاب گذاشته باشند در جمیع افعال قوی تر از روغن ناردین و دو مثقال آن پادزهر سموم بارده حیوانی است و بوئیدن شکوفه او مقوی دماغ و محلل زکام و عرق او که مسمی به عرق بهار است در دوم گرم و خشک و جهت ضعف دماغ و تفریح و تقویت اشتها و باه و سدّه مصفاة و نزلات و درد سینه و قولنج ریحی و پیچش و خفقان و غشی و مداومت او هفت روز و روزی دو وقیه با شکر و ربع درهم مرجان جهت رفع سپرز از مجربات و با آب کرفس جهت اخراج سنگ مثانه و گرده و شراب او ناشتا جهت قطع اسهال رطوبی نافع و حمول او با پشم جهت اصلاح رحم و با شیر مادیان جهت اعانت بر حمل از مجربات دانسته اند و اکثار بوئیدن او مورث بی خوابی و هوا، مضر عرق بهار است و مصلح او گلاب و قوتش در ظرف مس تا هفت سال باقی است و در شیشه تا یکسال. ( تحفه حکیم مؤمن ). و حبه حار یابس نافع نهش الهوام. ( از بحر الجواهر ). تخم نارنج را چون بکوبند روزی یک مثقال با نبات چند روز کفلمه کننددر گزیدگی غریب گز شفاء تمام بخشد و این را من خود تجربه کرده ام. ( یادداشت به خط مرحوم دهخدا ). و نیز رجوع شود به ضریر انطاکی ص 336 و گیاه شناسی گل گلاب ص 215و تاج المصادر بیهقی : و از وی [ بلخ ] ترنج و نارنج و نیشکر و نیلوفر خیزد. ( حدود العالم ). بیشتر بخوانید ... 
27-
28- فرهنگ فارسی
29-
30- ( اسم ) نیرنگ جمع : نارنجات . 
31-
32: فرهنگ معین
33-
34- (رِ ) (اِ. ) درختی است پایا از تیرة مرکبات با میوة آب دار، درشت و کروی .
35- (رَ ) [ معر. ] (اِ. ) نیرنگ . ج . نارنجات . 
36-
37- فرهنگ عمید
38-
--
81:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
82-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
83-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
84-
85- Narnj 
86-
87- اسم قشنگ دخترانه ی کُردی
--
105: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
106-
107- لینک ها 
108-
109- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
110-
111- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
########## d4c5e9894021de8c
20: ننه. [ ن َ ن َ / ن َ ن ِ ] ( اِ )در تداول ، مادر. ( ناظم الاطباء ) ( فرهنگ فارسی معین ).والده. || مادربزرگ. جده. ( فرهنگ فارسی معین ). || خدمتکار زن مخصوصاً اگر پیر باشد. ( فرهنگ عامیانه جمال زاده از فرهنگ فارسی معین ).
21-- ننه جان ؛ مادرجان. کلمه ای که مادر هنگام مهربانی به فرزند خود می گوید. ( ناظم الاطباء ).
22:- ننه خانی شله پز، ننه خانم شله پز ؛ شخص چلمن و بی عرضه و بی قابلیت : این جور که تو خیاطی می کنی ننه خانی شله پز هم می تواند بکند. ( فرهنگ عامیانه جمال زاده از فرهنگ فارسی معین ).
23:- ننه من غریبم درآوردن ؛ آه و ناله کردن. ( فرهنگ فارسی معین ). خود را ناتوان و بینواو ضعیف وانمود کردن برای جلب ترحم دیگران.
24:- ننه صمد ؛ ننه خانی شله پز. ( فرهنگ عامیانه جمال زاده از فرهنگ فارسی معین ).
25:- ننه قمر ؛ ننه خانی شله پز. ( فرهنگ عامیانه جمال زاده از فرهنگ فارسی معین ).
26:- ننه مرده ؛ مادرمرده. ( فرهنگ عامیانه جمال زاده از فرهنگ فارسی معین ).
27- ننه. [ ن َ ن ِ ] ( اِخ ) دهی است از دهستان بالک از بخش مریوان شهرستان سنندج که 100 تن سکنه دارد. آبش از چشمه و قنات ، محصولش غلات و لبنیات و توتون ، شغل اهالیش زراعت و گله داری است. ( از فرهنگ جغرافیایی ایران ج 5 ). 
28-
29- فرهنگ فارسی
30-
31- نه نه، مادر
32-( اسم ) ۱ - مادروالده .۲- مادر بزرگ جده . ۳ - خدمتکار زن مخصوصا اگر پیرباشد. یاننه جان . مادر جان مادر عزیز . یا ننه خانی شله پز.( صفت ) شخص چلمن و بی عرضه و بی قابلیت: این جور که تو خیاطی میکنی ننه خانی شله پز هم میتواند بکند. یا ننه من غریبم.لغت:مادر. من از وطن دور افتاده و بی کسم.یا ننه من غریبم در آوردن. آه و نالهکردن : خوب کمتر ننه من غریبم دربیار...
--
35: فرهنگ معین
36-
37- (نَ نِ ) (اِ. ) (عا. ) مادر، مادربزرگ . 
38-
39- فرهنگ عمید
40-
41- مادر. 
--
233:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
234-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
235-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
236-
237- منابع • https://fa.m.wikipedia.org/wiki/زبان_سانسکریت 
238- موضوع واژه �ننه� و ادعاهای مرتبط با آن درباره ریشه شناسی اش خیلی جالب و بحث برانگیزه، به ویژه وقتی پای زبان های مختلف، به ویژه ترکی و فارسی، به میان می آید. 
239- - - - 
--
########## 49b4f9bc7449ed85
28: ( آنار ) آنار. ( اِ ) رجوع به انار شود. انار. [ اَ ] ( اِ ) درختچه ایست از تیره موردیها که گاهی آنرا تیره ای مستقل محسوب دارند و بنام انارها نامند، پوست آن خاکستری و برگهایش بیضوی و گلهایش بالنسبه بزرگ و قرمزرنگ است. ( فرهنگ فارسی معین ). میوه آن درشت و دارای پوست سرخ و کلفت است. دانه های آن شفاف و آبدار و بیشتر سرخ رنگ است و دور آنرا پوسته نازکی با موادی غذایی فراگرفته است. ( از یادداشت مؤلف ) ( از گیاه شناسی حسین گل گلاب ص 232 ). رمان. ( برهان قاطع، ذیل رومنا ) ( ناظم الاطباء ). و بلغت زند، رومنا. ( برهان قاطع ) ( ناظم الاطباء ) . نار. درخت انار درجلگه های کرانه دریای مازندران بحال وحشی فراوان است ، در نزدیکی مراوه تپه نیز دیده میشود و آنرا همه جا انار میخوانند. انار درختی است کوچک که در خاکهای شنی خوب میروید. چوب آن دارای مازوج فراوان است و دررنگرزی مصرف میشود. ریشه آن نیز دارای آلکالوئیدی است که سمیت دارد و بمقدار کم برای از میان بردن کرم تنیا در پزشکی مصرف میشود. ( از جنگل شناسی کریم ساعی ج 1 ص 244 ). انار دارای اقسامی است ، شیرین و بیدانه آنرا که املیسی نامند لطیفتر از سایر اقسام و سرد باعتدال و در اول تر و با قوه قابضه و قلیل الغذا و مولد خلط صالح و نفاخ است و از این جهت باعث نعوظ محرورین است و مدر بول و مفتح و جالی و ملین طبع و مورث تشنگی است و خوردن آن بعد از طعام سبب انحدار آن و جهت تصفیه روح کبدی و تقویت جگر و استسقاء لحمی و زقی و سوءالقنیه و یرقان و سپرز و خفقان و الم سینه و سرفه حار و صاف کردن آواز و فربه کردن بدن و نفوذ فرمودن غذا و رفع جرب و حکه و نیکو کردن رنگ رخسار نافع و اکثار آن مفسد غذا و مرخی معده و مصلحش انار ترش و در باردالمزاج زنجبیل پرورده است. ( از تحفه حکیم مؤمن ، ذیل رمان ). و رجوع بهمان متن و رمان شود.
29-درخت کوچک معروفی است که از عصاره [ میوه ] آن شراب ترتیب میدادند و درخت مذکور بنوعی بزرگ شود که انسان میتواند در سایه آن مأوی گزیند. و لباس وافود رئیس کهنه با انارها مزین میگشت و بدین جهت انارهای بسیاری در اماکن مختلف هیکل میکاشته اند. ( از قاموس کتاب مقدس ) : و اگر شکم سخت نبود آنگاه سیب و انار و آبی خام بکوبد و... ( هدایة المتعلمین چ دانشگاه مشهد ص 376 ). و ما ببلخ بودیم بچند دفعت مجمزان رسیدند از قصدار سه و چهار و پنج و نامهای یوسف آوردند و ترنج و انار و نیشکر. ( تاریخ بیهقی چ ادیب ص 251 ). بیشتر بخوانید ... 
30-
31- فرهنگ فارسی
32-
33- نار: میوهای است درشت ودارای پوست سرخ وکلفت، دانه هایش آبدارومفرح، برای تصفیه خون نافع است
34-درختچهای از تیر. موردیها که گاهی آنرا تیره ای مستقل محسوب دارند و بنام انارها نامند . پوست آن خاکستری و برگهایش بیضوی و گلهایش باالنسبه بزرگ و قرمز رنگ است رمان ارز
--
37: فرهنگ معین
38-
39- ( اَ ) [ په . ] ( اِ. ) = نار: درختچه ای از تیرة موردی ها دارای برگ های بیضوی و گل های قرمزرنگ . میوه اش درشت و دارای پوست سرخ و کلفت و دانه های آبدار و خوشمزه می باشد. 
40-
41- فرهنگ عمید
42-
43- ۱. میوه ای خوراکی با پوستی سفید یا سرخ، دانه های قرمز یا سفید آبدار، با مزۀ ترش یا شیرین که از آب آن رب تهیه می شود و در پختن برخی خوراک ها کاربرد دارد.
--
166:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
167-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
168-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
169-
170- منابع • https://archive.org/details/1_20221023_20221023_1515 
171- یکی از مراکز تولید انار شهرستان کوهدشت استان لرستان است.
172-
--
186:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
187-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
188-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
189-
190- منابع • https://archive.org/details/1_20221023_20221023_1515 
191- میوه نار در ترکستان ( اورخان و آلتای، اورخان که همان مغولستان و آلتای هم که شمال غرب چین است ) وحود نداشته و ندارد ولی این میوه از دیر باز در ایران بوده، و ترکان که از مغول و چین بودند در ایران با ان روبرو شدند و این واژه به زبان انان وارد شد.
########## 55f601744b4ff46e
58:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
59-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
60-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
61-
62- نگاه کنید به واژه رنگ
63-نارنگ رو به اشتباه گاها نا رنگ نوشته اند اما نار رنگ می باشد همونطور که در 
64-میشه تا که شود شاخ گل چو چوگان پست
--
81: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
82-
83- لینک ها 
84-
85- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
86-
87- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-07T18:28:23.013Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/^ Persian$/{f=1} f' a1a934e23fb05c29.txt | grep -n -A12 \"^ Etymology\" | head -30\necho \"###### naranja\"\nawk '/^ Spanish$/{f=1} f' 383e59de6e0e800a.txt | grep -n -A8 \"^ Etymology\" | head -20\necho \"###### arancia\"\nawk '/^ Italian$/{f=1} f' 3fa8d4e28387bfeb.txt | grep -n -A10 \"^ Etymology\" | head -24",
 "description": "Wiktionary anar, naranja, arancia"
}
```


### [2026-09-07T18:28:24.292Z] TOOL RESULT

```
13: Etymology
14- [ edit ] 
15-
16- Inherited from Middle Persian 𐭠𐭭𐭠𐭥 ( ʾnʾl /⁠anār⁠/ ) . Arguably, ultimately related to the pomegranate terms under Arabic رُمَّان ( rummān ) .
17-
18- Pronunciation
19- [ edit ] 
20-
21- ( Classical Persian ) IPA ( key ) : /ʔa.ˈnaːr/ 
22-
23- ( Dari, formal ) IPA ( key ) : [ʔä.nɑ́ːɾ] 
24-
25- ( Dari, formal ) IPA ( key ) : [ʔä.nɑ́ːɾ] 
--
116: Etymology
117- [ edit ] 
118-
119- Borrowed from Classical Persian اَنَار ( anār ) .
120-
121- Pronunciation
122- [ edit ] 
123-
124- IPA ( key ) : /əˈnäːɾ/ 
125-
126- Noun
127- [ edit ] 
128-
--
181: Etymology
182- [ edit ] 
###### naranja
38: Etymology
39- [ edit ] 
40-
41: Etymology tree
42-
43- Proto-Austroasiatic *ŋaːm der. ? 
44- Proto-Dravidian *nāram 
45-
46- Proto-Dravidian *kāy 
47-
48- Sanskrit नारङ्ग ( nāraṅga ) bor. 
49- Classical Persian نَارَنْگ ( nārang ) bor. 
--
179: Etymology
180- [ edit ] 
181-
182: Etymology tree
183-
184- Proto-Austroasiatic *ŋaːm der. ? 
185- Proto-Dravidian *nāram 
###### arancia
4: Etymology
5- [ edit ] 
6-
7- Feminine form of arancio ( “ orange (tree) ” ) , from Arabic نَارَنْج ( nāranj ) , [ 1 ] from Persian نارنگ ( nârang ) , from Sanskrit नारङ्ग ( nāraṅga ) . [ 2 ] 
8-
9- Pronunciation
10- [ edit ] 
11-
12- IPA ( key ) : /aˈran.t͡ʃa/ 
13-
14- Audio (un'arancia) : ( file )
```


## [2026-09-07T18:28:28.839Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/^ Spanish$/{f=1} f' 383e59de6e0e800a.txt | sed -n '38,75p'",
 "description": "Spanish naranja etymology detail"
}
```


### [2026-09-07T18:28:30.124Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Austroasiatic *ŋaːm der. ? 
 Proto-Dravidian *nāram 

 Proto-Dravidian *kāy 

 Sanskrit नारङ्ग ( nāraṅga ) bor. 
 Classical Persian نَارَنْگ ( nārang ) bor. 
 Arabic نَارَنْج ( nāranj ) bor. 
 Old Spanish naranja 
 Spanish naranja 

 Inherited from Old Spanish naranja , from Arabic نَارَنْج ( nāranj ) , from Persian نارنگ ( nârang ) , from Sanskrit नारङ्ग ( nāraṅga , “ orange tree ” ) . Compare Portuguese laranja ; Catalan taronja is unrelated, being instead cognate to Spanish toronja ( “ grapefruit ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /naˈɾanxa/ [naˈɾãŋ.xa] 

 Audio ( Colombia ) : ( file ) 

 Rhymes: -anxa 

 Syllabification: na‧ran‧ja 

 Adjective
 [ edit ] 

 naranja   m or f ( masculine and feminine plural naranja or naranjas ) 

 orange ( having orange color ) 

 ( politics , Spain ) Pertaining to Ciudadanos , a Spanish political party
```


## [2026-09-07T18:28:45.882Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN nanny/nana\"\ngrep -n \"nanny,\\|^nana\\|nanny  goat\" KLN_1966.txt | head\necho \"=== SKT nun\"\ngrep -n -i \"^Nun\\.\\|Nun\\. \" SKT.txt | head\ngrep -n \"nonna\\|nunnery\" SKT.txt | head\necho \"=== FSD vol3 nano-\"\ngrep -n \"^nano-\\|^nanism\" FSD_vol3.txt | head\necho \"=== WEB vol1 nano\"\ngrep -n \"^nano-\\|^nanism\\|^nanny\" WEB_vol1.txt | head",
 "description": "Klein nanny, Skeat nun, FSD/WEB nano-"
}
```


### [2026-09-07T18:28:45.988Z] TOOL RESULT

```
=== KLN nanny/nana
24939:nanny  goat,  a  she-goat  ( colloq .)  —  Formed  fr. prec.  word  and  goat.
=== SKT nun
4955:llo,  ■  dcspmte  nun.  (Span.*< AsptxaiU.^XA.  dcsptfottu^  pp. f  (*l.ore>.
8972:Hunt,  to  chase  wild  animals  (E.)  M.  £ hunUn.  A.  S.  huntian,  to  capture.  Allied 10  Goth,  hunths,  ciptivily,  whidi  is  from huntharts,  pp.  oi  hitUhaa,  to  seize,  capture vpt.  t.  fianth).  Thus  the  Teut.  base  is HANTH.  to  seize.  Cf.  Skt.  ^diaya,  to fell,  to  drive,  causal  of  ta^^  to  fall. CVKAD.)
12513:Nun.  (L.)  M.  E.  and  A.S.  mwne.^ Low  L.  nunna,  nonria.  a  nun  ;  orig.  a  title of  respect;  oldcsit  sense,  '  mother.*  It  an- swers to  L.  ttouuus,  father,  also  a  monk, •f  <^Jk,  rfjKvr;,  aunt ;  Skt.  nand^  mother,  a famili.-vr  word  used  by  children.  Formed like  ma-ma,  da-Ha  {daddy)^  and  the  like. Der.  MUMtter-yj  from  U,  V.  rtfitittert'e,  which from  O.  F.  twnne  =  L.om  L.  ncnna*
21173:Walnut.  lE.)  Lit.  "afoieipn  nut.*  A.S, ■wea/Af  foreign  ;  Anu/^  a  nut-+Uu.  wainoot, Icel.  valhnot,  Dan.  valnod.  Swed.  vatnbt^ G.  wailnun.  p.  The  A.  S.  lueatA  innkei !  he  pi  wealiu,  foreigners,  which  is  the mod.  £.  Waiei  (now  applied  to  the  country itself)  ;  cognate  with  O.  H.  G.  walah^ a  foreigner,  whence  G.  IVdircA,  foreign. Italian.
22822:inun.   mullci,  musckt  mnse,  mast,  male,
=== FSD vol3 nano-
=== WEB vol1 nano
```


## [2026-09-07T18:29:00.164Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\ntxt=open('skeatdli.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('Nun.')\nwhile i>0 and 'nunna' not in txt[i:i+300]:\n    i=txt.find('Nun.',i+1)\nprint(repr(txt[i-200:i+700]))\n# find nearest page numbers\nseg=txt[max(0,i-6000):i+3000]\nprint([ (m.group(1)) for m in re.finditer(r'\\n\\s*(\\d{3})\\s*\\n',seg)])\nEOF",
 "description": "Skeat DLI Nun page"
}
```


### [2026-09-07T18:29:01.491Z] TOOL RESULT

```
' Coined from L numismat-, stem \nof numisma, current com. — Cik. vofiiOfM, \na custom, also current coin. — Gk. \nto adopt, use as coin. — Gk. v 6 /xos, usage. \n\n— Gk. ve^iiVy to distribute. (-y^NEM.) \n\nNun. (L.) M.E. and A.S. nunne.^m \n\nLate L. nunna, nonna, a nun ; orig. a title \nof respect ; oldest sense, ‘ mother.’ It \nanswers to L, nonnus, father, also a monk \n(Ducange). + ^k. ydwrj, aunt; Skt. nand, \nmother, a familiar word used by children. \nFormed like ma-ma, da-da {daddy), and \nthe like. Der. nunn-er-y, from O F. non- \nncrie, which is fiom C). F. nonne, Late L. \nnonna. \n\nNuncboon, a luncheon. (Hybrid; L. \nand E.) The ending is confused with that \nof luncheon. M. E. nonechenche (for none- \n^chenche), Riley, Memorials of London, \np. 265 ; lit. a ‘ noon-drink,’ to accompany \nthe nonemete or ‘ noon-meat.’ — M.E none, \nnoon ; schenche, a pouring out of drink. — \nA. S non, noon (of L. or'
['351', '352']
```


## [2026-09-07T18:29:08.709Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/nanny\" --note \"page 349, node 3 English nana/nanny (root Nana)\" >/dev/null\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/nanny\" --note \"page 349, node 3 English nanny\" >/dev/null\ncd data/verification/sources/web\nf=$(python3 -c \"import hashlib;print(hashlib.sha1('https://www.etymonline.com/word/nanny'.encode()).hexdigest()[:16])\")\ngrep -n -A4 \"nanny (n\" $f.txt | head -20\nf2=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/nanny'.encode()).hexdigest()[:16])\")\nawk '/^ English$/{x=1} x' $f2.txt | grep -n -A8 \"^ Etymology\" | head -20",
 "description": "Etymonline/Wiktionary nanny"
}
```


### [2026-09-07T18:29:10.814Z] TOOL RESULT

```
23: nanny (n.) 
24-
25- "children's nurse," 1795, from the widespread child's word for "female adult other than mother" (compare Greek nanna "aunt," and see nana ). The word also is a nickname form of the fem. proper name Ann , which probably is the sense in nanny-goat "female goat" (1706, compare billy-goat ). Nanny-house "brothel" is slang from c. 1700. Nanny state , in reference to overintrusive government policies is attested by 1987, the term is associated with British political leader Margaret Thatcher, who criticized the tendency. Nannyism in reference to actions or policies considered unduly protective is by 1959; also compare the verb.
26- also from 1795 
27-
--
30: "to be unduly protective," 1954, from nanny (n.). Related: Nannied ; nannying .
31- also from 1954 
32-
33- Entries linking to nanny 
34-
8: Etymology
9- [ edit ] 
10-
11- From nan ( “ grandmother; nursemaid ” ) +‎ -y . The root is from nana ( “ grandma; nanny ” ) , which is from nanna ( “ grandmother ” ) , which is possibly derived from Proto-Celtic *nana ( “ grandmother ” ) . See also Proto-Brythonic *nanī , Welsh nain ( “ grandmother ” ) , Galician nana ( “ mama ” ) , Spanish nana ( “ granny; nanny; mommy; housekeeper ” ) , Sicilian nanna ( “ grandma ” ) , Italian nonna ( “ granny ” ) , Late Latin nonna ( “ nun; tutoress; old woman ” ) , Norman nonne ( “ nun ” ) , Old French nonain ( “ nun ” ) . All probably ultimately from a Proto-Indo-European root imitative of a child babbling, similar to Ancient Greek νάννα ( nánna ) .
12-
13- (1795) It has often been assumed that the English term was originally a widespread child's word for "female adult other than mother" (compare Greek νάννα ( nánna , “ aunt ” ) , nanna ).
14-
15- On the other hand, according to recent research of the Dutch historical linguists Hans Beelen and Nicoline van der Sijs (published in Onze Taal , September 2018), on which see also etymologiebank.nl , in Dutch), the term nanny (and the British colloquial nan for "grandmother") may actually be eponymous , viz. being originally an affective form (i.e. a hypocoristic ) of the popular female name Anne . The Dutch statesman and scientist Constantijn Huygens Jr. made the following observation during one of his many sojourns in England (noted in his Journaal , dated 13 December 1692): "Yesterday I received 10lb of chocolate again, from niece Becker, and she had Nanny , her maid, bringing me the money that she had owed me" ( Gisteren kreegh 10 ℔ choccolate wederom van nicht Becker, en had Nanny, haer meidt, geweest om mij 't geldt, dat van haer hebben most, te brengen ). Beelen and van der Sijs therefore assumed that "since many female domestic servants were named " Nan " or "Nanny", the name became a sobriquet for the profession of "maid, childminder" in the 18 th century". ("Omdat veel vrouwelijke huisbedienden in het Engels de voornaam Nan of Nanny hadden, verschoof de betekenis in de achttiende eeuw naar die van een beroepsaanduiding: ‘meid, kindermeisje’")
16-
```


## [2026-09-07T18:29:18.265Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls site/pages/349.jpg 2>/dev/null; pdftoppm -f 349 -l 349 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg349 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg349.png",
 "description": "Render PDF page 349"
}
```


### [2026-09-07T18:29:19.916Z] TOOL RESULT

```
site/pages/349.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 59757 Sep  7 14:29 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg349.png
```


## [2026-09-07T18:29:22.508Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg349.png"
}
```


### [2026-09-07T18:29:22.846Z] TOOL RESULT

```

```


## [2026-09-07T18:29:22.843Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T18:29:37.317Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg349.png data/verification/sources/refs/ocr/BOOK/349.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head\necho \"=== try IEC fulltext search\"\ntimeout 60 curl -s \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" | python3 -c \"\nimport json,sys;d=json.load(sys.stdin);print(d.get('server'),d.get('dir'));\nprint([f['name'] for f in d.get('files',[]) if f['name'].endswith('djvu.txt') or f['name'].endswith('.pdf')])\"",
 "description": "Save page PNG, check Mann item"
}
```


### [2026-09-07T18:29:39.078Z] TOOL RESULT

```
total 16200
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 14:29 .
drwxrwxr-x 13 sfmqrb sfmqrb   4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
=== try IEC fulltext search
ia902900.us.archive.org /17/items/mann-an-indo-european-comparative-dictionary-1984-1987
['Mann - An Indo-European Comparative Dictionary (1984-1987).pdf', 'Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.txt']
```


## [2026-09-07T18:29:43.663Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 90 curl -sG \"https://ia902900.us.archive.org/fulltext/inside.php\" \\\n --data-urlencode \"item_id=mann-an-indo-european-comparative-dictionary-1984-1987\" \\\n --data-urlencode \"doc=Mann - An Indo-European Comparative Dictionary (1984-1987)\" \\\n --data-urlencode \"path=/17/items/mann-an-indo-european-comparative-dictionary-1984-1987\" \\\n --data-urlencode \"q=juicy\" | head -c 3000",
 "description": "Fulltext search Mann for juicy"
}
```


### [2026-09-07T18:29:46.990Z] TOOL RESULT

```
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "juicy", "indexed": true, "matches": []}
```


## [2026-09-07T18:29:54.203Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor q in \"anor\" \"1645\" \"Supplement\"; do\necho \"== $q\"\ntimeout 90 curl -sG \"https://ia902900.us.archive.org/fulltext/inside.php\" \\\n --data-urlencode \"item_id=mann-an-indo-european-comparative-dictionary-1984-1987\" \\\n --data-urlencode \"doc=Mann - An Indo-European Comparative Dictionary (1984-1987)\" \\\n --data-urlencode \"path=/17/items/mann-an-indo-european-comparative-dictionary-1984-1987\" \\\n --data-urlencode \"q=$q\" | head -c 600; echo; done",
 "description": "Probe Mann scan extent"
}
```


### [2026-09-07T18:30:01.619Z] TOOL RESULT

```
== anor
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "anor", "indexed": true, "matches": [{"text": "anos (2), \u00e0 \u2018ancestor\u2019. WP I, 55 OHG ano, cf. also enel \u201cgrandfather; grand- child\"; Sw. <IA_FTS_MATCH>anor</IA_FTS_MATCH>, pl Ukr. on-uka \u2018grandchild\u2019; Li. cf. an-yta husband's mother", "par": [{"l": 829, "t": 2062, "r": 991, "b": 2116, "page": 29, "boxes": [{"l": 829, "t": 2062, "r": 991, "b": 2116, "page": 29}], "page_width": 3901, "page_height": 5698}]}]}
== 1645
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "1645", "indexed": true, "matches": [{"text": "<IA_FTS_MATCH>1645</IA_FTS_MATCH>", "par": [{"l": 281, "t": 216, "r": 419, "b": 275, "page": 838, "boxes": [{"l": 281, "t": 216, "r": 419, "b": 275, "page": 838}], "page_width": 3901, "page_height": 5698}]}]}
== Supplement
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "Supplement", "indexed": true, "matches": [{"text": "11. 1987. 1573-1684 (uolobhis-uupsios + <IA_FTS_MATCH>Supplement</IA_FTS_MATCH> + Corrigenda)", "par": [{"l": 1027, "t": 2307, "r": 1489, "b": 2390, "page": 5, "boxes": [{"l": 1027, "t": 2307, "r": 1489, "b": 2390, "page": 5}], "page_width": 3901, "page_height": 5698}]}, {"text": "VAN Wu. N.: Etymologisch Wb. der nederlandse Taal, 1912. With <IA_FTS_MATCH>Supplement</IA_FTS_MATCH> by C. B. van Haeringen, 1936. Reprint Staatsdrukkerij- en Uitgeverijbedrijf, den Haag 1949",
```


## [2026-09-07T18:30:17.728Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (836,837,838,839):\n    print('=== leaf',i)\n    print(leaves[i][:400])\nEOF",
 "description": "Inspect IEC leaves 836-839"
}
```


### [2026-09-07T18:30:18.967Z] TOOL RESULT

```
=== leaf 836
‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. werken, id.; OE weorcan, id. beside (z-gde) wyrcan, id.; ON verka, v. ‘work’; Alb. virdhem, v. ‘gain a skill, win sympathy’, mp. fr. *uergemoi or sim.. Nomi- nal types: Pahl. varz, s. “practice, work? (Per. id. fr. Pahl.); cf. also Per. barz-gar, s. 'farm-labou- rer’; Arm. (e- or o-gde), o-st. "work act, fact’; Myc. we(
=== leaf 837
nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. id.; Cor. gwern, pl. gwernow, f. id.; ON vorn, f. beside vernd, f. ‘defence’; Sw. värn, n. id.; Finn. (LW) varras, s. ‘spit, pole, shaft
uern- (1), see uermn- (2)
uern- (2) (uernà, is, ios) ‘withy, shoot, suck- er; alder. WP I, 292 Gk. érnos, n. ‘young plant, sucker, shoot’; Alb. verr, m. “alder, white poplar’; Gaul. ve
=== leaf 838
ag’; Lat. verro, ére, OLat. vorro ('drag, trail; sweep, brush”,
uerpo — uertos
15
20
25
30
35
40
45
1522
but a type *uris- is possible for verro in the sense of 'sweep^); Latv. cf. (?) verSuü, vērst, v. ‘direct’; vērsties, refl. ‘go, wend’; cf. ver- stuve, f. ‘plowtail’. See next
uerstis (urst-) ‘turn’. Cf. uert-, uort-, urt- and extns. Av. varstis, f., varstvom, n. ‘deed’; OW gwers, f. ‘while’; R
=== leaf 839
a dike’; G Werd, m. “island, coastal strip’; Ukr. vereta, f. ‘blanket. (Go. wairdus, G Wirt, m. “host, entertainer’, fr. *uer-tüs?, but *ues- "be, dwell" for Lat. verna, mf. “household slave). See next
uerut- (2) (?) ‘crowd, group, team’ Skt. cf. varütham, n. (2) 'swarm, crowd; Tokh. A wartsi, B wertsya, -tsyo, f. ‘crowd, retinue’; OE werod, n. (1) ‘team, band, troop’
ueru- (1) “din, confusion, st
```


## [2026-09-07T18:30:35.270Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(x)+1 for x in lines[:11525])\nleaf=txt[:pos].count('\\f')\nleaves=txt.split('\\f')\nprint('leaf',leaf)\nprint(re.findall(r'\\b(\\d{3,4})\\b',leaves[leaf])[:12])\nprint(leaves[leaf][:200])\nEOF",
 "description": "IEC page for nana"
}
```


### [2026-09-07T18:30:36.615Z] TOOL RESULT

```
leaf 462
['826', '317', '701', '827', '693', '318', '318']
kos, náke, mf. “goatskin, fleece'; Br. naka, inf. ‘cover, hide, dissemble’
nāk- (naks-) (3) ‘come, arrive, reach, suf- fice’ Lat. cf. nanciscor, nactus, v. “find, get, reach’; OHG gi-nuogi, -nuog, adv
```


## [2026-09-07T18:30:47.960Z] TOOL CALL #75: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T18:30:47.997Z] TOOL RESULT

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


## [2026-09-07T18:31:31.813Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"###### nonna latin\"\nawk '/^ Latin$/{f=1} f' c0cce09dd129a832.txt | grep -A8 \"^ Etymology\" | head -20\necho \"###### etymonline nun\"\ngrep -A4 \"nun (n\" 7f031171196ae9c4.txt | head -20\necho \"###### etymonline nano-\"\ngrep -A4 \"nano-\" a28d32f085ab6618.txt | head -20",
 "description": "Read nonna, nun, nano- sources"
}
```


### [2026-09-07T18:31:33.025Z] TOOL RESULT

```
###### nonna latin
 Etymology
 [ edit ] 

 Feminine of nonnus .

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [ˈnɔn.na] 
--
 Etymology
 [ edit ] 

 Inherited from Late Latin nonna .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈnɔnnə/ 
###### etymonline nun
 nun (n.) 

 Old English nunne "woman devoted to religious life under vows of celibacy, poverty, and obedience to a superior," also "vestal, pagan priestess," from Late Latin nonna "nun, tutor," originally (along with masc. nonnus ) a term of address to elderly persons, perhaps from children's speech, reminiscent of nana (compare Sanskrit nona , Persian nana "mother," Greek nanna "aunt," Serbo-Croatian nena "mother," Italian nonna , Welsh nain "grandmother;" see nanny ).

 Entries linking to nun 
###### etymonline nano-
URL: https://www.etymonline.com/word/nano-
FETCHED: 2026-09-07T18:22:20Z
STATUS: 200
TITLE: Nano- - Etymology & Meaning of the Prefix

--
 Origin and history of nano- 

 nano- 

 introduced 1947 (at 14th conference of the Union Internationale de Chimie ) as a prefix for units of one thousand-millionth part (now "one-billionth"), from Greek nanos "a dwarf." According to Watkins, this is originally "little old man," from nannos "uncle," masc. of nanna "aunt" (see nana ), but Beekes calls it "An onomatopoeic word of unknown origin." Earlier nano- was used as a prefix to mean "dwarf, dwarfish," and still it is used in a non-scientific sense of "very small."
 also from 1947 

 Entries linking to nano- 

 nana 

 child's word for "grandmother" or, sometimes, "nurse," 1844 (see nanny ).
--
 "one-billionth of a gram," 1951, from nano- + gram .
```


## [2026-09-07T18:39:17.971Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-349.json <<'JSONEOF'\n{\n  \"pdf_page\": 349,\n  \"book_page\": 319,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nana, Nena\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"IE nursery word (Lallwort) *nana / *nena 'mother, nurse' — Pokorny 754 'nana, nena etc., mother, etc. (child word)'; Walde-Pokorny II 317; Watkins/AHD root 'nana'\",\n      \"note\": \"Pokorny IEW p.754 has the headword exactly as Nourai gives it — 'Root/lemma: nana, nena etc.', 'Meaning: mother, etc. (child word)' — and its material list is the chart's list (Old Indic nanā, NP nānā, Gk. νάννα/νίννη 'aunt', νέννος/νάννος 'uncle', Lat. nonnus/nonna, Welsh nain, Russ. njanja). The language label 'Indo-European' is right only in Pokorny's own weak sense: this is not a reconstructible PIE root with regular reflexes but a nursery/Lallwort type that each language re-creates (Buck, Selected Synonyms 2.35-2.36, treats the whole ma-/pa-/na- series this way, and Klein calls nonnus 'orig. a child's lip word'). Nourai's own gloss ('a child word for mother a nurse') states that correctly. Consequence for the tree: the arrows below are better read as 'parallel formation / cognate nursery word' than as regular descent; where a node depends on real descent (Gk.>Lat.>Eng. nano-, LL>Eng. nun) it holds, where it asserts inheritance between branches (Skt.>Pers.) it does not.\",\n      \"note_fa\": \"پوکورنی در «فرهنگ ریشه‌شناسی هندواروپایی» ص ۷۵۴ سرواژه را دقیقاً به همان صورتی می‌آورد که نورایی نقل کرده است: nana, nena و دیگرگونه‌ها، به معنای «مادر و مانند آن (واژهٔ کودکانه)». پس ریشه و برگردان آن درست است. اما باید توجه داشت که این یک ریشهٔ هندواروپایی آغازین به معنای فنی نیست، بلکه از گونهٔ واژه‌های کودکانه (Lallwort) است که هر زبان جداگانه می‌سازد؛ بنابراین پیکان‌های این نمودار بیشتر «هم‌ریشگی/ساخت موازی» را نشان می‌دهند تا وام‌گیری یا تحول آوایی منظم. ادعای نورایی درست است، با این یادآوری.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/nun\",\n        \"https://www.etymonline.com/word/nanny\",\n        \"https://en.wiktionary.org/wiki/nonna\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:754\", \"status\": \"supports\", \"note\": \"POK_full.txt line 61773: 'Root / lemma: nana, nena etc.' — 'Meaning: mother, etc.. (child word)'; Material: 'Old Indie nana \\\"mother, old woman\\\" ... np. nana \\\"mother\\\"; Alb. Geg nona, nana \\\"mother\\\"; gr. vavva, vivvr] \\\"aunt\\\", vsvvoc, vavvaq \\\"uncle\\\"; Latin nonnus m., nonna f. late \\\"word used by young monks when addressing elders, a nun\\\", also \\\"nurserymaid\\\"; cymr. nain \\\"grandmother\\\"; russ. njanja ...' + 'References: WP. II 317, WH. II 175. Page(s): 754'. Page number and content are exactly Nourai's.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Band II p.317 (WLD_Bd2_pages.txt leaf 322, running head 'nag^ih ... nard(h)o- 317')\", \"stance\": \"partial\", \"note\": \"'naiia, nena Lallwort. Ai. nana \\\"Mutter, Mütterchen\\\" ... np. nana \\\"Mutter\\\"; gr. vdwaj vhva, vlvva \\\"Base, Tante\\\", vevvog, vdvvog \\\"Oheim\\\"; alb. nane \\\"Mutter, Amme\\\"; lat. (sehr zw., s. Vf. LEWb.2 s.v.) nonnus, nonne spät \\\"Mönch, Nonne\\\" ...' — same family, but Walde flags the Latin nonnus/nonna link as 'sehr zweifelhaft' (very doubtful), and calls the whole thing a Lallwort, not a root.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44 (AHD_watkins1985.txt leaf 73)\", \"stance\": \"supports\", \"note\": \"'nana. Child's word for a nurse or female adult other than its mother. 1. Greek nanna, aunt, whence nannas, uncle, whence nan(n)os, \\\"little old man,\\\" dwarf: NANO-. 2. Late and Medieval Latin nonna, aunt, old woman, nun: NUN. 3. English (directly from baby talk) NANA, NANNY. [Pok. nana 754.]' — this single entry is the whole of Nourai's chart, branch for branch.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p.826 f. (IEC.txt line 11526, leaf 462)\", \"stance\": \"supports\", \"note\": \"'nanā \\\"mother, nurse, foster-parent\\\". WP II, 317 Skt. nanà \\\"mother\\\"; Per. cf. nānā (\\\"maternal grandfather\\\" sic!); Oss. nanā \\\"mother, grand-mother\\\"; Gk. (expressive) nánne \\\"maternal aunt\\\"; Alb. nánë ...; W nain \\\"grandma\\\".'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 2.35-2.36 'FATHER / MOTHER', pp.103-104 (SYN.txt line 2813)\", \"stance\": \"silent\", \"note\": \"Buck's 'Mother' section derives the standard words from IE *māter- and lists only the mama type as the nursery-word rival ('Nursery words that have become the usual terms. Type mama ... in It. mamma ... W., Br. mam'); the nana type is not discussed at all, i.e. Buck records no such word as a 'usual term'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"nana\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Vedic nanā́ f. 'mother, little mother', a term of endearment attested in the Rigveda (VIII.91.5, the Apālā hymn) and glossed 'mother, old woman' by Pokorny; it is a reduplicated nursery form, formed like ma-mā, ta-tā, and it is the base from which the kinship term nanāndar- 'husband's sister' was reshaped (Pokorny: '*nansna reshaped, after svasā : svasr-, to nanandar-'). The word is not derived from anything: it is a primary child's word, and that is exactly how Nourai's root box describes it. Skeat quotes it in the same function ('Skt. nanā, mother, a familiar word used by children. Formed like ma-ma, da-da (daddy)').\",\n          \"derivation_fa\": \"سنسکریت nanā «مادر، مادرجان» واژه‌ای است کودکانه و مضاعف (مانند ma-mā و ta-tā) که در ریگ‌ودا (۸.۹۱.۵) به کار رفته است؛ پوکورنی آن را «مادر، پیرزن» معنی می‌کند و یادآور می‌شود که نام خویشاوندی nanāndar- «خواهرشوهر» بر پایهٔ همین واژه و به قیاس svasā : svasr- ساخته شده است. این واژه از هیچ صورت کهن‌تری گرفته نشده، بلکه خودش ساختی نخستین و کودکانه است — درست همان چیزی که نورایی در جعبهٔ ریشه گفته است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%A8%E0%A4%BE\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:754\", \"status\": \"supports\", \"note\": \"POK_full.txt p.754: 'Old Indie nana \\\"mother, old woman\\\", *nansna reshaped (after svasa: svasr-) to nanandar \\\"of a husband's sister\\\"'.\"},\n            {\"ref\": \"KLN:1062\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 25780 = leaf 568, whose running head carries printed pp.1062-1063, s.v. 'nun': 'Cp. OI. nana, ModPers. nana, \\\"mother\\\", Gk. vavva, vcvva, \\\"aunt\\\" ... which all were orig. child's lip words.' Nourai's page number is exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. 'Nun', p.~352 of the same edition Nourai cites (DLI copy in.ernet.dli.2015.158267)\", \"stance\": \"supports\", \"note\": \"'+ Gk. ναννη, aunt; Skt. nanā, mother, a familiar word used by children. Formed like ma-ma, da-da (daddy), and the like.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.826 (IEC.txt line 11526)\", \"stance\": \"supports\", \"note\": \"'nanā \\\"mother, nurse, foster-parent\\\". WP II, 317 Skt. nanà \\\"mother\\\" ...'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 317\", \"stance\": \"supports\", \"note\": \"'Ai. nand \\\"Mutter, Mütterchen\\\", *nanUna umgebildet (nach svasd : svasr-) zu nanandar \\\"des Mannes Schwester\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"naneh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP ننه nane (Iranian reading nane, Dari/Classical nanā) 'mum, granny, old nurse' is real and well attested: Mo'in glosses it '(نَ نِ) (اِ.) (عا.) مادر، مادربزرگ' — colloquial 'mother, grandmother' — and Dehkhoda adds 'خدمتکار زن مخصوصاً اگر پیر باشد' ('a female servant, especially an old one'), i.e. precisely Nourai's 'slang word for mother or nurse'. But the arrow as drawn (Sanskrit nanā → Persian naneh) is not a derivation any source accepts. Horn, the very page Nourai cites, treats it as a colloquial Persian word 'nicht schriftgemäss, aber dialektisch sehr gebräuchlich' and merely COMPARES it ('ai. nanā \\\"Mutter\\\" : alb. nane etc.', Balochi nānō/nani, Shughni-Sanglechi nan), and Wiktionary says flatly 'Originally from baby talk.' Middle Persian has no *nanak that would give it; the -eh is the ordinary NP spelling of final -a in a hypocoristic. So Persian nane and Sanskrit nanā are parallel nursery formations (cognate only in the loose Lallwort sense), not parent and child.\",\n          \"derivation_fa\": \"«ننه» در فارسی گفتاری به معنای «مادر، مادربزرگ» و نیز «کلفت پیر/دایه» است؛ معین آن را «(عا.) مادر، مادربزرگ» و دهخدا «خدمتکار زن مخصوصاً اگر پیر باشد» می‌آورد، که همان تعریف نورایی است. اما پیکان نمودار (سنسکریت nanā → فارسی ننه) پذیرفتنی نیست: هرن در همان صفحهٔ ۲۳۴ (بند ۱۰۴۴) که نورایی به آن ارجاع می‌دهد، «نَنه» را واژه‌ای گفتاری و غیرکتابی می‌داند و تنها آن را با سنسکریت nanā و آلبانیایی nanë و بلوچی nānō/nani و شغنی nan «می‌سنجد»، نه اینکه از آنها بگیرد؛ ویکی‌واژه هم می‌نویسد «در اصل از زبان کودکانه». در فارسی میانه صورتی مانند *nanak سراغ نداریم. پس «ننه» و nanā ساخت‌های موازی کودکانه‌اند و هم‌ریشه به معنای دقیق کلمه نیستند: ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%86%D9%87\",\n            \"https://abadis.ir/fatofa/%D9%86%D9%86%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:234\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 255 (printed p.234, header '- 234 -'), entry no.1044: 'nene \\\"Mutter\\\", nicht schriftgemäss, aber dialektisch sehr gebräuchlich. ai. nanā \\\"Mutter\\\" : alb. nane etc. (G. Meyer, 297). bal. vergl. nānō, nana \\\"Grossvater\\\", nani \\\"Grossmutter\\\" (LW. No.183); šiγn. sangl. nan, wb. nan \\\"Mutter\\\".' The page is exactly right and the word is there, but Horn only compares the Sanskrit — he does not derive the Persian from it.\"},\n            {\"ref\": \"KLN:1062\", \"status\": \"supports\", \"note\": \"Klein p.1062 s.v. nun: 'Cp. OI. nana, ModPers. nana, \\\"mother\\\"' — Klein lists Persian nana in this family (again as a parallel child's word, 'which all were orig. child's lip words').\"},\n            {\"ref\": \"POK:754\", \"status\": \"supports\", \"note\": \"POK_full.txt p.754 lists 'np. nana \\\"mother\\\"' in the material of the lemma nana/nena.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in s.v. ننه (via abadis.ir/fatofa/ننه)\", \"stance\": \"supports\", \"note\": \"'(نَ نِ) (اِ.) (عا.) مادر، مادربزرگ' — colloquial 'mother, grandmother'; Dehkhoda on the same page: 'در تداول، مادر ... || مادربزرگ. جده ... || خدمتکار زن مخصوصاً اگر پیر باشد'.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no.1553, p.127 (LKT.txt leaf 153)\", \"stance\": \"supports\", \"note\": \"'1553. Pers. nänä: \\\"Mutter\\\" [Horn NpEt S.234, Nr.1040 (recte 1044)], ebenso tk. nene; hieraus rum. neneacă \\\"dass.\\\", nene und demin. nenišor \\\"Trauter\\\" ...' — an independent witness both to the Persian word and to Nourai's HRN:234 citation.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep for 'nene', 'nanā', 'nan' \", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien has no entry for this colloquial word (no hit).\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt, grep 'ننه'\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (vol. 4, ن) has no headword ننه — as expected of a purely colloquial word; only OCR noise matches.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.502 (ARY_latin_index_pages.txt line 14623, [pdf page 501])\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry for this family lists 'NAIN (WELSH) / NANA (SANSKRIT) / NANE, NEN (ALBANIAN) / NANNA, NINNE, NENNOS (GREEK) / NONNUS, NONNA (LATIN) / NENNE (GERMAN) / NANNY, NANA (ENGLISH) / NJANJA (RUSSIAN) / NENI (BULGARIAN)', with 'REFERENCES: POKORNY ... MALLORY & ADAMS' — i.e. an independent modern Persian handbook puts the Persian word in exactly Pokorny's set.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"nana, nanny\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English nana 'grandmother, nurse' (first recorded 1844) and nanny 'children's nurse' (1795) are, on Watkins's account, taken straight from English baby talk rather than through any Latin or Greek intermediary — AHD's root entry says so in as many words ('3. English (directly from baby talk) NANA, NANNY'), which is why Nourai hangs them directly off the root box. Etymonline agrees ('from the widespread child's word for \\\"female adult other than mother\\\"'). The reservation is that part of the evidence points elsewhere: nanny-goat (1706) is generally taken from Nanny, the pet form of Ann (cf. billy-goat from Billy), Klein's only entry is 'nanny goat ... formed fr. prec. word and goat', and Beelen & van der Sijs (Onze Taal, Sept. 2018) argue from Constantijn Huygens Jr.'s Journaal (13 Dec. 1692, 'Nanny, haer meidt') that the nursemaid sense itself began as the given name Anne, since so many English maids were called Nan/Nanny. So the baby-talk origin is the majority view but not the only one.\",\n          \"derivation_fa\": \"واژه‌های انگلیسی nana «مادربزرگ، دایه» (نخستین ثبت ۱۸۴۴) و nanny «دایهٔ کودکان» (۱۷۹۵) بنا بر نظر واتکینز یک‌راست از زبان کودکانهٔ انگلیسی برآمده‌اند و از لاتین یا یونانی وام گرفته نشده‌اند؛ در ضمیمهٔ ریشه‌های هندواروپایی فرهنگ AHD صریحاً آمده «انگلیسی (مستقیماً از زبان کودکانه): NANA, NANNY»، و نورایی همین را در نمودار آورده و درست است. اتیمانلاین نیز همین را می‌گوید. با این حال یک احتیاط لازم است: nanny-goat (۱۷۰۶) را معمولاً از Nanny، صورت خودمانی نام Ann، می‌دانند (مانند billy-goat از Billy)، و بیلن و فان‌درسایس (۲۰۱۸) بر پایهٔ روزنوشت کنستانتین هویخنس (۱۶۹۲) استدلال می‌کنند که خودِ معنای «دایه» از همان نام Anne پدید آمده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nanny\",\n            \"https://en.wiktionary.org/wiki/nanny\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 73 (p.44), root 'nana': '3. English (directly from baby talk) NANA, NANNY.' Nourai gives no page for this citation, and the root entry is exactly what the arrow claims.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1027 (KLN_1966.txt line 24939, leaf 550)\", \"stance\": \"partial\", \"note\": \"Klein has no entry for nana/nanny as such, only 'nanny goat, a she-goat (colloq.) — Formed fr. prec. word and goat' (the preceding word being nano-/nanism), i.e. he does not endorse the baby-talk derivation of the nurse-word.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt / DLI copy, grep 'nanny', 'nana'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no entry for nana or nanny.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Late Latin\",\n          \"words\": \"nun\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"nun\",\n          \"correct_form\": \"nonna (fem.) / nonnus (masc.)\",\n          \"derivation\": \"The Late Latin word in this position is nonna f. (masc. nonnus), 'old woman / nun' and 'old man / monk', originally a respectful term of address of nursery origin — Ernout-Meillet: 'nonna, nonnula, -ae f. (bas latin): terme de tendresse, de caractère populaire, à géminée expressive. Cf. nonnus, -a'; Klein: 'Late L. nonna, \\\"an old woman, a nun\\\", fem. of nonnus, \\\"an old man, a monk\\\", orig. a child's lip word'. The box on the printed page (I read the rendered page image, data/verification/sources/refs/ocr/BOOK/349.png) really does read only 'nun', so the extraction is faithful and the slip is Nourai's own: he has put the English gloss where the Late Latin form belongs (compare his AHD source, which prints 'Late and Medieval Latin nonna, aunt, old woman, nun'). Substance aside from the form: the connection of nonnus/nonna with this nursery family is standard (AHD, Klein, Skeat, Etymonline 'perhaps from children's speech'), but Walde-Pokorny II 317 marks it 'sehr zw.' (very doubtful) and Ernout-Meillet derive it from expressive gemination without invoking an IE root, so the arrow is accepted rather than proved.\",\n          \"derivation_fa\": \"واژهٔ لاتینی متأخر در این جایگاه nonna (مادینه) و nonnus (نرینه) است، به معنای «پیرزن/راهبه» و «پیرمرد/راهب»، که در اصل نشانهٔ احترام و برآمده از زبان کودکانه بوده است؛ ارنو و مه‌یه می‌نویسند: «nonna، لاتین پسین، واژه‌ای عامیانه و مهرآمیز با مضاعف‌سازی تأکیدی»، و کلاین آن را «در اصل واژه‌ای کودکانه» می‌خواند. اما در جعبهٔ چاپ‌شدهٔ کتاب (تصویر صفحه را دیدم) تنها «nun» آمده است؛ یعنی خطا از خوانش اسکن نیست، بلکه خطای خودِ کتاب است: نورایی برگردان انگلیسی را به جای صورت لاتینی نشانده (منبع خودش، AHD، «Late and Medieval Latin nonna» دارد). دربارهٔ محتوا: پیوند nonna با این خانوادهٔ واژه‌های کودکانه دیدگاه رایج است، ولی والده-پوکورنی (ج ۲ ص ۳۱۷) آن را «بسیار مشکوک» می‌شمارد. پس: خطای چاپی کتاب در صورت واژه، و محتوای پیکان پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nonna\",\n            \"https://www.etymonline.com/word/nun\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt p.44, root 'nana': '2. Late and Medieval Latin nonna, aunt, old woman, nun: NUN.' — the arrow is right; note that the reference itself prints the Latin form as nonna, which is what the chart's box should have said.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. de la langue latine, s.v. nonna (LAT.txt line 38879)\", \"stance\": \"partial\", \"note\": \"'nonna, nonnula, -ae f. (bas latin): terme de tendresse, de caractère populaire, à géminée expressive. Cf. nonnus, -a, etc.' — a popular affective word with expressive gemination; they do not connect it to any IE root, so the family link is left open.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1062 s.v. nun (KLN_1966.txt line 25780)\", \"stance\": \"supports\", \"note\": \"'fr. Late L. nonna, \\\"an old woman, a nun\\\", fem. of nonnus, \\\"an old man, a monk\\\", orig. a child's lip word. Cp. OI. nana, ModPers. nana, \\\"mother\\\", Gk. vavva ... Alb. none ... W. nain ...'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 317\", \"stance\": \"partial\", \"note\": \"'lat. (sehr zw., s. Vf. LEWb.2 s.v.) nonnus, nonne spät \\\"Mönch, Nonne\\\", auch \\\"Pflegerin eines Kindes\\\"' — 'sehr zweifelhaft', i.e. Walde doubts the very step this node draws.\"},\n            {\"src\": \"LEW\", \"where\": \"LEW_1910.txt, grep 'nonnus', 'nonna'\", \"stance\": \"silent\", \"note\": \"no hit in the Walde 1910 OCR (the word is a Late Latin one and may be absent from that edition).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"nun, nunnery\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Late Latin nonna was borrowed into Old English as nunne 'woman under religious vows' already in the Anglo-Saxon period (the word travels with the monastic institution, hence Etymonline's 'nun, tutor' sense and the OE use also for 'vestal, pagan priestess'); OE nunne > ME nunne, nun > NE nun, with the ordinary loss of the final unstressed syllable. Nunnery is not formed in English on nun but taken over from Old French nonnerie (< OF nonne < Late Latin nonna) and then re-shaped to the English stem: Klein, 'nunnery — ME. nunnerie, fr. OF. nonnerie, fr. nonne, \\\"nun\\\", fr. L. nonna'; Skeat, 'Der. nunn-er-y, from O.F. nonnerie, which is from O.F. nonne, Late L. nonna'. Both steps are exactly as the chart draws them.\",\n          \"derivation_fa\": \"لاتینی متأخر nonna همراه با نهاد رهبانیت وارد انگلیسی کهن شد: nunne «زن دارای پیمان دینی» (در انگلیسی کهن حتی برای «کاهنهٔ بت‌پرست» هم به کار رفته)؛ سپس nunne > انگلیسی میانه nunne/nun > انگلیسی نو nun، با افتادن هجای پایانی بی‌تکیه. اما nunnery در انگلیسی از nun ساخته نشده، بلکه از فرانسهٔ کهن nonnerie (از nonne، از nonna) وام گرفته و سپس بر پایهٔ ستاک انگلیسی بازساخته شده است؛ کلاین (ص ۱۰۶۲) و اسکیت (ذیل Nun) هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nun\",\n            \"https://www.etymonline.com/word/nun\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1062\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 25780, leaf 568 (running head carries printed 1062-1063): 'nun, n., 1) a woman devoted to religious life ... — ME. nunne, nun, fr. OE. nunne, fr. Late L. nonna, \\\"an old woman, a nun\\\", fem. of nonnus ... Cp. nunnery.' and line 25788 'nunnery, n. ... — ME. nunnerie, fr. OF. nonnerie, fr. nonne, \\\"nun\\\", fr. L. nonna.' Nourai's page is exact and covers both words.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. 'Nun' (p.~352 of the edition whose 'Orange' is on p.360; DLI copy in.ernet.dli.2015.158267)\", \"stance\": \"supports\", \"note\": \"'Nun. (L.) M.E. and A.S. nunne. — Late L. nunna, nonna, a nun; orig. a title of respect; oldest sense, \\\"mother.\\\" It answers to L. nonnus, father, also a monk (Ducange). + Gk. ναννη, aunt; Skt. nanā, mother ... Der. nunn-er-y, from O.F. nonnerie, which is from O.F. nonne, Late L. nonna.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44, root 'nana'\", \"stance\": \"supports\", \"note\": \"'2. Late and Medieval Latin nonna, aunt, old woman, nun: NUN.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"nana : aunt; nannus : little old man, a dwarf\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two different Greek words share this box and they do not stand equally well. (a) νάννα / νέννα / νίννη 'aunt' (with masc. νέννος, νάννας 'uncle') is confirmed as a member of the nursery family: Pokorny p.754 lists 'gr. νάννα, νίννη \\\"aunt\\\", νέννος, νάννας \\\"uncle\\\"' under the lemma nana/nena, and Walde-Pokorny II 317 the same ('Base, Tante ... Oheim'). Nourai's spelling 'nana' for νάννα and the gloss 'aunt' are right. (b) νᾶνος / νάννος 'dwarf' (whence the modern prefix) is the doubtful half. Pokorny does NOT list it at 754. Nourai follows Watkins, who chains it inside the family — 'Greek nanna, aunt, whence nannas, uncle, whence nan(n)os \\\"little old man,\\\" dwarf' — and Klein allows it as a possibility only: 'νᾶνος, νάννος \\\"dwarf\\\", which is of uncertain etymology. It is perh. a child's lip word and rel. to νάννας, νέννος \\\"uncle\\\", νάννα \\\"aunt\\\".' Beekes rejects it outright ('an onomatopoeic word of unknown origin', quoted at Etymonline s.v. nano-; Wiktionary: 'Possibly onomatopoeic, though the logic behind the formation, as well as putative source if borrowed, is unclear'). Worst word governs, hence plausible. Note also that 'nannus' is a Latinised spelling of νάννος, and that in Pokorny and Walde-Pokorny νάννος means 'uncle', not 'dwarf' — Nourai's 'little old man, a dwarf' is Watkins's gloss.\",\n          \"derivation_fa\": \"در این جعبه دو واژهٔ یونانی جداگانه نشسته‌اند که ارزش یکسانی ندارند. یکم: νάννα / νέννα / νίννη «خاله، عمه» (و نرینهٔ آن νέννος، νάννας «عمو، دایی») بی‌گمان از همین خانوادهٔ واژه‌های کودکانه است؛ پوکورنی ص ۷۵۴ و والده-پوکورنی ج ۲ ص ۳۱۷ آن را ذیل همین سرواژه می‌آورند. دوم: νᾶνος / νάννος «کوتوله» — که پیشوند امروزی nano- از آن است — جای بحث دارد: پوکورنی آن را در ص ۷۵۴ نمی‌آورد؛ واتکینز (منبع نورایی) آن را در همین خانواده و از νάννας «عمو» می‌گیرد؛ کلاین تنها آن را «شاید» می‌داند و ریشه‌اش را «نامعلوم» می‌شمارد؛ و بیکس آن را واژه‌ای آوایی-نمادین با ریشهٔ ناشناخته می‌داند. چون بدترین حکم بر جعبه حاکم است: ادعای نورایی با احتیاط پذیرفتنی است. افزون بر این، صورت «nannus» املای لاتینی‌شدهٔ νάννος است و در پوکورنی معنای νάννος «عمو» است نه «کوتوله».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BD%E1%BE%B6%CE%BD%CE%BF%CF%82\",\n            \"https://www.etymonline.com/word/nano-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:754\", \"status\": \"partial\", \"note\": \"POK_full.txt p.754 has 'gr. vavva, vivvr] \\\"aunt\\\", vsvvoc, vavvaq \\\"uncle\\\"' — it supports νάννα 'aunt' but contains no νᾶνος 'dwarf' at all, so it covers only the first of the box's two words.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt p.44: '1. Greek nanna, aunt, whence nannas, uncle, whence nan(n)os, \\\"little old man,\\\" dwarf: NANO-.' — both of Nourai's words and both of his glosses come from here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 317\", \"stance\": \"partial\", \"note\": \"'gr. vdwaj vhva, vlvva \\\"Base, Tante\\\", vevvog, vdvvog \\\"Oheim\\\"' — 'aunt/cousin' and 'uncle' only; the dwarf-word is absent here too.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1027 s.v. nanism (KLN_1966.txt line 24935, leaf 550)\", \"stance\": \"partial\", \"note\": \"'L. nanus, fr. Gk. νᾶνος, νάννος, \\\"dwarf\\\", which is of uncertain etymology. It is perh. a child's lip word and rel. to νάννας, νέννος, \\\"uncle\\\", νάννα, \\\"aunt\\\".' — Klein grants Nourai's link only as a possibility.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.826 s.v. nanā (IEC.txt line 11526)\", \"stance\": \"partial\", \"note\": \"'Gk. (expressive) nánne \\\"maternal aunt\\\"' — Mann lists only the aunt-word in this family, not the dwarf-word.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"nanŭs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin nānus m. (also nannus), fem. nāna, 'dwarf', is a straightforward borrowing of Greek νᾶνος / νάννος — Ernout-Meillet: 'nānus, -i m. (nannus), nāna, -ae f.: nain, naine. Emprunt au gr. νανος, ναννος (le mot lat. est pumilis, cf. Gell. 19,13)'. It first appears in Varro, De lingua Latina 5,119, where it denotes a squat vessel ('quo postea accessit nanus ... cum Graeco nomine, et cum Latino nomine Graeca figura barbatus'; cf. Paulus-Festus 185,8 'nanum Graeci vas aquarium dicunt humilem et concavum ... unde nani pumiliones dicuntur'), so the word entered Latin as a colloquial/vulgar term, the classical word for a dwarf being pumilio. Long ā in nānus renders Greek ᾶ. The word survives across Romance (M-L 5819) and was even borrowed into Irish (nan). Nourai's gloss 'dwarf, short' and the direction of the arrow are both right.\",\n          \"derivation_fa\": \"لاتینی nānus (و nannus)، مادینه nāna، «کوتوله»، وام‌واژه‌ای است یک‌راست از یونانی νᾶνος/νάννος؛ ارنو و مه‌یه صریح می‌نویسند «Emprunt au gr. νανος, ναννος» و می‌افزایند که واژهٔ اصیل لاتینی برای این مفهوم pumilis/pumilio بوده است. نخستین کاربرد آن در «دربارهٔ زبان لاتینی» وارّو (۵٫۱۱۹) است، آنجا که ظرفی کوتاه و گودافتاده را nanus می‌نامد، و پاولوس-فستوس (۱۸۵٫۸) نیز همین را گزارش می‌کند؛ پس این واژه در لاتین رنگ عامیانه داشته. آی کشیدهٔ nānus برگردان ᾶ یونانی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/nanus\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:872\", \"status\": \"not_checked\", \"note\": \"AHD:872 is a page of the 1975/76 New College Edition main dictionary (the entry nanus/nano-), which is not openly available (the IA copies americanheritage0000dict, americanheritag00morr etc. are lending-only and their djvu.txt returns 401). The claim is however covered by the same dictionary's IE-root appendix, which IS available: Watkins 1985 p.44, root 'nana', '... whence nan(n)os, \\\"little old man,\\\" dwarf: NANO-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nanus (LAT.txt line 40312)\", \"stance\": \"supports\", \"note\": \"'nānus, -i m. (nannus), nāna, -ae f.: nain, naine. Emprunt au gr. νανος, ναννος ... Nanus apparaît pour la première fois dans Varr., L.L. 5,119 ... cf. P.F. 185,8, nanum Graeci vas aquarium dicunt humilem et concavum ... unde nani pumiliones dicuntur. Nanus passait pour vulgaire ... Panroman, sauf roumain, M.L. 5819. Irl. nan.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1027 s.v. nanism / nano- (KLN_1966.txt lines 24935-24937)\", \"stance\": \"supports\", \"note\": \"'nanism ... F. nanisme, formed with suff. -isme fr. L. nanus, fr. Gk. νᾶνος, νάννος, \\\"dwarf\\\"'.\"},\n            {\"src\": \"LEW\", \"where\": \"LEW_1910.txt, grep 'nanus'\", \"stance\": \"silent\", \"note\": \"no usable hit in the Walde 1910 OCR.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"nano- : a prefix meaning a small amount, one billionth of a specified unit.; nanosecond, nanometer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English nano- continues Latin nanus / Greek νᾶνος. Two layers must be kept apart. The older, purely lexical layer is 'dwarf, dwarfish' (nanism 'dwarfishness' via French nanisme, nanoid, nanocephalic), which Klein describes as 'nano-, before a vowel nan-, combining form meaning \\\"dwarf, dwarfish\\\" — Gk. νανο-, ναν-, fr. νανος, \\\"dwarf\\\"'. The metric layer is a 20th-century decision, not an inherited meaning: nano- was adopted as the prefix for 10⁻⁹ at the 1947 conference of the Union Internationale de Chimie and ratified for SI by the 11th CGPM in 1960 (Etymonline: 'introduced 1947 ... as a prefix for units of one thousand-millionth part ... from Greek nanos \\\"a dwarf\\\"'), giving nanosecond (1959) and nanometer. So Nourai's gloss and both his examples are correct, and the arrow Latin nanŭs → English nano- is the standard route (Latin being the transmitting form for the Greek combining stem in modern scientific coinage).\",\n          \"derivation_fa\": \"پیشوند انگلیسی nano- ادامهٔ لاتینی nanus و یونانی νᾶνος است، اما باید دو لایه را از هم جدا کرد. لایهٔ کهن‌تر و واژگانی به معنای «کوتوله، کوتوله‌وار» است (nanism «کوتولگی» از راه فرانسهٔ nanisme، و nanoid و nanocephalic)؛ کلاین می‌نویسد: «nano-، پیش از واکه nan-، جزء ترکیبی به معنای کوتوله، از یونانی νανος». لایهٔ دوم یک قرارداد سدهٔ بیستمی است و نه معنایی موروثی: nano- در همایش سال ۱۹۴۷ اتحادیهٔ بین‌المللی شیمی برای ۱۰⁻⁹ برگزیده و در یازدهمین کنفرانس عمومی اوزان و مقادیر (۱۹۶۰) در نظام SI پذیرفته شد، و از آن nanosecond (۱۹۵۹) و nanometer ساخته شده است. پس برگردان و هر دو نمونهٔ نورایی درست است و پیکان «لاتینی nanŭs ← انگلیسی nano-» همان مسیر پذیرفته‌شده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/nano-\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 24937, leaf 550 (running head shows printed 1028, so the leaf carries pp.1027-1028): 'nano-, before a vowel nan-, combining form meaning \\\"dwarf, dwarfish\\\". — Gk. νανο-, ναν-, fr. νανος, \\\"dwarf\\\". See nanism.' Nourai's page is exact.\"},\n            {\"ref\": \"AHD:872\", \"status\": \"not_checked\", \"note\": \"the 1975/76 AHD main-dictionary page 872 is not openly available (lending-only IA scans). Its IE-root appendix, which is available, ends the root entry with 'nan(n)os, \\\"little old man,\\\" dwarf: NANO-' (Watkins 1985 p.44), i.e. it makes exactly this arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44, root 'nana'\", \"stance\": \"supports\", \"note\": \"the derivative printed in caps at the end of branch 1 is 'NANO-'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1-vol4, grep '^nano-', '^nanism'\", \"stance\": \"silent\", \"note\": \"no hit; the Funk & Wagnalls plates (1913) predate the metric prefix and the OCR does not yield the nanism entry.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt, grep '^nano-', '^nanism'\", \"stance\": \"silent\", \"note\": \"no hit (only vol. 1 of Webster's 2nd ed. is available and its OCR does not return these headwords).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Naranga\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Sanskrit नारङ्ग nāraṅga m. 'orange tree, orange' (Suśruta-saṃhitā, c. 4th c. CE), itself a loan from Dravidian\",\n      \"note\": \"The headword, the language label and the gloss are all correct: Sanskrit nāraṅga (also nāgaraṅga) is the orange tree, and it is the recognised starting point of the European word. What Nourai leaves open is what the sources also leave open — where the Sanskrit itself comes from. Hobson-Jobson, his own reference, says so explicitly on the cited page: 'The Persian indeed may be traced to Skt. nāgaranga, and nāranga, but of these words no satisfactory etymological explanation has been given, and they have perhaps been Sanscritized from some southern term', and points to Tamil/Malayalam nāṟu 'fragrant'. Modern work has taken that option: Wiktionary derives नारङ्ग from Dravidian (cf. Tamil நார்த்தங்காய் nārttaṅkāy 'citron', from narantam 'fragrance' + kāy 'fruit'), and Lokotsch records the older folk-etymological guess Skt. nāgaraṅga 'elephant's liking' (Lassen). Klein and Etymonline simply call it 'of uncertain origin'. One dissenting Iranist view exists and cuts against the whole root: Asbaghi (Persische Lehnwörter im Arabischen p.257) analyses Persian nārang as native anār 'pomegranate' + rang 'colour', which would make the Persian word the source and not a borrowing from Sanskrit.\",\n      \"note_fa\": \"سرواژه، برچسب زبان و معنای آن هر سه درست است: سنسکریت नारङ्ग nāraṅga (و نیز nāgaraṅga) «درخت نارنج» است و همه‌جا آن را سرچشمهٔ واژهٔ اروپایی می‌دانند. آنچه نورایی ناگفته می‌گذارد، همان است که منابع نیز باز گذاشته‌اند: خودِ واژهٔ سنسکریت از کجاست؟ هابسون-جابسون در همان صفحهٔ ۶۴۲ که نورایی به آن ارجاع می‌دهد می‌نویسد که برای nāgaranga و nāranga «هیچ ریشه‌شناسی رضایت‌بخشی به دست نیامده و شاید از واژه‌ای جنوبی (دراویدی) سنسکریت‌سازی شده باشند» و به nāṟu «خوش‌بو» در تامیل و مالایالام اشاره می‌کند. پژوهش امروزی همین راه را برگزیده است: ویکی‌واژه nāraṅga را وام‌واژه‌ای از دراویدی می‌داند (تامیل nārttaṅkāy «بالنگ» از narantam «بو» + kāy «میوه»). لوکوچ حدس عامیانهٔ کهن‌تر nāgaraṅga «دلخواه فیل» را نقل می‌کند. یک دیدگاه مخالف هم هست: اصباغی (ص ۲۵۷) نارنگِ فارسی را از «انار + رنگ» می‌داند که در آن صورت فارسی سرچشمه می‌شود نه وام‌گیرنده. در کل ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97\",\n        \"https://www.etymonline.com/word/orange\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HJB:642\", \"status\": \"supports\", \"note\": \"HJB.txt leaf 687 carries the running head 'ORANGE. 642 ORANGE.' and the article 'ORANGE, s.' begins there: 'The word doubtless came from the Arab. naranj, which is again a form of Pers. nārang, or nārangī ... The Persian indeed may be traced to Skt. nāgaranga, and nāranga, but of these words no satisfactory etymological explanation has been given, and they have perhaps been Sanscritized from some southern term.' Page and content are exactly Nourai's.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. p.360 s.v. Orange (DLI copy in.ernet.dli.2015.158267)\", \"stance\": \"partial\", \"note\": \"Skeat's chain stops at Persian: 'Orange. (F. - Ital. - Arab. - Pers.) ... — Arab. nāranj, nārinj. — Pers. nārang, an orange. Allied to Pers. nār, a pomegranate.' He does not cite the Sanskrit at all.\"},\n        {\"src\": \"LKT\", \"where\": \"Lokotsch no.1555, p.127 (LKT.txt leaf 153)\", \"stance\": \"partial\", \"note\": \"'1555. Pers. nārāng: \\\"Apfelsine\\\" [vielleicht aus sskr. nāgaraṅga \\\"Elefantenneigung\\\", d.h. Lieblingsfrucht der Elefanten, vgl. Lassen, Indische Altertumskunde I, 247]' — Lokotsch heads the entry with the Persian word and treats the Sanskrit as a mere possibility.\"},\n        {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p.257 s.v. nāranǧ (PLA_pages.txt leaf 271, running head '... 257 ...')\", \"stance\": \"contradicts\", \"note\": \"'nāranǧ: \\\"Orange\\\" aus pers. نارنگ nārang < mp. anar \\\"Granatapfel\\\" + mp. rang \\\"Farbe\\\"' — Asbaghi makes Persian nārang a native compound, not a loan from Sanskrit.\"},\n        {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.642 (continuation p.643)\", \"stance\": \"supports\", \"note\": \"besides the etymology it dates the fruit's westward movement from Mas'ūdī (c. AD 930): 'the orange-tree (shajar-ul-nāranj) ... were brought from India after the year (A.H.) 300, and first sown in Oman. Thence they were transplanted to Basra, to Irak, and to Syria.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"nâreng; nârengî; anâr\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words are right, the third is not. (a) nâreng «نارنگ» — Sanskrit nāraṅga was borrowed into Persian with the ordinary treatment of the Indic cluster -ṅg- as -ng-, giving Cl.Pers. nārang; it is Persian nārang, not the Sanskrit, that Arabic and then Europe took over, and Mo'in's footnote to Borhan-e Qate' p.2095 states exactly this transmission ('اصل این لغت هندی است ولی از راه زبانهای ایرانی وارد زبانهای اروپایی شد', 'the word is Indic in origin but entered the European languages by way of the Iranian languages'). (b) nârengî «نارنگی» — a Persian nisba-type derivative in -ī of nārang, now the tangerine/mandarin; Mo'in's footnote on the facing page 2096 derives it 'از: نارنگ (ه.م.) ... (سنسکریت)' and Hobson-Jobson already reports nārangī 'still a common term for the orange in Hindustan'. Both confirmed. (c) anâr «انار» — this is a different word altogether and does not come from nāraṅga. Persian انار is inherited from Middle Persian ʾnʾl /anār/ 'pomegranate' (Mo'in tags the headword '[په.]', i.e. Pahlavi, and glosses it '= نار'); Wiktionary: 'Inherited from Middle Persian 𐭠𐭭𐭠𐭥 (ʾnʾl /anār/)'. Nourai himself marks it with a question mark and offers two escapes, and neither works: Skeat's 'Allied to Pers. nār, a pomegranate' (SKT:360) is a nineteenth-century guess that no later authority repeats, and the IEC:1645 root 'Nôr, Anôr: juicy' cannot be verified (see ref_check). Note that even Asbaghi, the one modern source that links the two words, reverses the arrow: he makes nārang = anār + rang, so anār would be the parent of nārang, not its child.\",\n          \"derivation_fa\": \"از سه واژهٔ این جعبه دو تا درست است و یکی نه. یکم، «نارنگ»: سنسکریت nāraṅga با تبدیل عادی خوشهٔ -ṅg- هندی به -ng- به فارسی وام گرفته شد و صورت فارسی nārang به دست آمد؛ و همین صورت فارسی است — نه سنسکریت — که به عربی و از آنجا به اروپا رفت. معین در حاشیهٔ برهان قاطع ص ۲۰۹۵ درست همین را می‌نویسد: «اصل این لغت هندی است ولی از راه زبانهای ایرانی وارد زبانهای اروپایی شد». دوم، «نارنگی»: مشتق فارسی با پسوند نسبت -ی از نارنگ، امروز به معنای نارنگی/ماندارین؛ معین در ص ۲۰۹۶ آن را «از: نارنگ ... (سنسکریت)» می‌داند. سوم، «انار»: این واژه‌ای دیگر است و از nāraṅga نمی‌آید. انار از فارسی میانهٔ anār (ʾnʾl) «انار» به ارث رسیده است؛ معین خود سرواژهٔ «انار» را «[په.]» یعنی پهلوی نشانه‌گذاری کرده و «= نار» آورده، و ویکی‌واژه هم آن را برگرفته از فارسی میانه می‌داند. نورایی خودش کنار این واژه علامت پرسش گذاشته و دو راه گریز پیشنهاد کرده که هیچ‌کدام کار نمی‌کند. پس در این بخش پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A7%D8%B1\",\n            \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A7%D8%B1/\",\n            \"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%D8%AC/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2095\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt [pdf page 178] = printed p.2095 (printed = pdf + 1917): the headword نارنگ stands there with Mo'in's footnote '۲ ← نارنگ (ه.م.)، قی: نارنگی' and the نارنج entry on the same page carries his note 'معرب نارنگ (ه.م.) است [قی: نارنگی]. و اصل این‌لغت هندی است. ولی از راه ... زبانهای ایرانی وارد زبانهای اروپایی شد و صورت orange درآمد'. Dehkhoda quotes the same footnote and cites it as '(برهان قاطع چ معین حاشیه ص ۲۰۹۵)', which independently confirms Nourai's page number. Nothing on that page derives انار from نارنگ.\"},\n            {\"ref\": \"HJB:642\", \"status\": \"supports\", \"note\": \"Hobson-Jobson p.642: 'The word doubtless came from the Arab. naranj, which is again a form of Pers. nārang, or nārangī, the latter being still a common term for the orange in Hindustan.' Covers both nâreng and nârengî; says nothing about anâr.\"},\n            {\"ref\": \"IEC:1645\", \"status\": \"not_checked\", \"note\": \"Nourai's NOTE cites Mann p.1645 for IE roots 'Nôr, Anôr: juicy'. Page 1645 lies in Mann's Supplement (the item's own contents line reads 'II. 1987. 1573-1684 (uolobhis-uupsios + Supplement + Corrigenda)'), and the only scan available (archive.org mann-an-indo-european-comparative-dictionary-1984-1987, 858 leaves) stops in the u- section around printed p.1554; its full-text index returns no match at all for 'juicy'. In the main alphabet, which IS available, Mann's nor- entries are nor- (1) 'penetration; inside', nor- (2) 'join, joint', nor- (3) 'narrow, close' (IEC.txt lines 11851-11853, p.~920) — none of them 'juicy' — so the claim cannot be checked from the accessible text.\"},\n            {\"ref\": \"SKT:360\", \"status\": \"partial\", \"note\": \"Skeat p.360 s.v. Orange ends 'Allied to Pers. nār, a pomegranate' — so Nourai's cross-reference is faithful to Skeat, but Skeat suggests only a link with نار/انار, dates from 1901, and is repeated by no later authority; Klein, Etymonline and Wiktionary all keep the two words apart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in s.v. نارنج and s.v. انار (via abadis.ir/fatofa/)\", \"stance\": \"contradicts\", \"note\": \"on انار Mo'in prints '( اَ ) [ په . ] ( اِ. ) = نار: درختچه‌ای از تیرة موردی‌ها ...' — the tag [په.] marks it as a Pahlavi inheritance, not an Indic loan; on نارنج he prints '[ معر. ]', 'Arabicised'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.4 p.2096 (BQT_v4_pages.txt [pdf page 179]), footnote 1 to نارنگی\", \"stance\": \"supports\", \"note\": \"'۱ از: نارنگ (ه.م.) ... (سنسکریت) (رك: هرمزدنامه ص ۸۷) ... میوة نارنگی همان نارنج شیرین یا پرتقال است ولی کوچکتر و خوشبوتر از آن است' — nārangī from nārang, itself Sanskrit.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no.1555, p.127\", \"stance\": \"supports\", \"note\": \"the entry is headed 'Pers. nārāng: \\\"Apfelsine\\\"' and makes the Persian word the immediate source of the Arabic and hence of all the European forms.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.257 s.v. nāranǧ\", \"stance\": \"partial\", \"note\": \"'aus pers. نارنگ nārang < mp. anar \\\"Granatapfel\\\" + mp. rang \\\"Farbe\\\"' — links nārang with anār but in the opposite direction to the chart (anār as component, not descendant).\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'narang', 'nāran'\", \"stance\": \"silent\", \"note\": \"Horn has no entry for nārang/nārenj.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"nâranj\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic نَارَنْج nāranj 'bitter orange, Citrus aurantium' is a borrowing of Classical Persian نارنگ nārang, with the regular Arabic substitution of ج /dʒ/ for Persian گ /g/ (as in برنامه > برنامج, نارگیل > نارجيل). The loan is datable: Mas'ūdī (c. AD 930) reports that the orange tree, shajar al-nāranj, was brought from India after AH 300 and first planted in Oman, whence it went to Basra, Iraq and Syria (Hobson-Jobson p.643), so the word travelled with the tree in the 10th century. Bābur still knew that the -j was the Arabic pronunciation: 'the men of Bajaur and Swād call nāranj nārang' (Bābur-nāma 328, quoted ibid.). Wiktionary: 'Borrowed from Classical Persian نَارَنْگ (nārang), from Sanskrit नारङ्ग (nāraṅga, \\\"orange tree\\\")'. The node has no refs= in the book, but the step is uncontested.\",\n          \"derivation_fa\": \"عربی «نارنج» وام‌واژهٔ فارسی «نارنگ» است، با ابدال همیشگی گِ فارسی به جیم عربی (مانند نارگیل > نارجیل و برنامه > برنامج). زمان وام‌گیری را می‌توان تعیین کرد: مسعودی (حدود ۳۱۸ ق/۹۳۰ م) می‌نویسد که «شجر النارنج» را پس از سال ۳۰۰ هجری از هند آوردند و نخست در عمان کاشتند و از آنجا به بصره و عراق و شام رفت؛ پس واژه در سدهٔ چهارم هجری همراه درخت به عربی رسیده است. بابر نیز آگاه بود که جیم تلفظ عربی است: «مردم بجور و سواد نارنج را نارنگ می‌گویند». این جعبه در کتاب بی‌ارجاع است، اما گامش مورد اختلاف نیست: ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%D9%86%D8%AC\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); checked instead against Wiktionary, Asbaghi p.257, Lokotsch 1555, Klein p.1091, Devic p.184 and Hobson-Jobson p.642 f. — all agree.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.257 s.v. nāranǧ\", \"stance\": \"supports\", \"note\": \"the entry itself is 'nāranǧ: \\\"Orange\\\" aus pers. nārang', i.e. a Persian loanword in Arabic, with the Romance and Germanic descendants listed (sp. naranja, port. larange, it. arancia, dtsch. Orange, ndl. oranje, rum. naranta, lat. Aurantium) and Mandaic narniz.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1091 f. s.v. orange (KLN_1966.txt line 26460, leaf 583)\", \"stance\": \"supports\", \"note\": \"'fr. Arab. naranj (whence also Sp. naranja, Port. laranja, MGk. νεραντζιον), fr. Pers. narang, fr. OI. nārangaḥ, \\\"orange tree\\\", which is of uncertain origin.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no.1555, p.127\", \"stance\": \"supports\", \"note\": \"'hieraus über das gleichlautende ar. Wort sp. naranja, pg. laranja ... it. arancia' — the Arabic word is the pivot through which the Persian reached Europe.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep 'نارنج'\", \"stance\": \"silent\", \"note\": \"Addi Shir's Alfaz al-farisiyya al-mu'arraba returns no hit for نارنج in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"nârenj\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A genuine Arabic-mediated round trip: Persian nārang → Arabic nāranj → back into Persian as نارنج nārenj, which is why Persian now has the doublet nārang / nārenj. Mo'in marks the second one as a loan outright: 'نارنج ... (رَ) [ معر. ] (اِ.)' — معرب, 'Arabicised' — and his footnote in Borhan-e Qate' says 'نارنج معرب «نارنگ» است'. The Arabic ج was kept in the returning form, and Iranian Persian shifted the vowel (nāranj > nārenj) as usual. Today nārenj is the specific Seville/bitter orange (Citrus aurantium), while the borrowed pair نارنگی nārangī covers the tangerine. The two script extras on the printed page are Persian derivatives of the returned form: نارنجی nārenjī 'orange (the colour)' and نارنجک nārenjak, literally 'little orange', the modern word for a hand grenade.\",\n          \"derivation_fa\": \"نمونه‌ای روشن از دوگانهٔ فارسی-عربی-فارسی: «نارنگ» فارسی به عربی رفت و «نارنج» شد و همان صورت معرّب بازگشت، چنان‌که امروز در فارسی هم «نارنگ» داریم و هم «نارنج». معین خودِ سرواژه را «[معر.]» یعنی معرّب نشانه‌گذاری کرده و در حاشیهٔ برهان قاطع نوشته «نارنج معرب نارنگ است». جیم عربی در صورت بازگشته نگه داشته شد و واکهٔ آن در فارسی ایران به کسره گرایید (nāranj > nārenj). امروز «نارنج» همان مرکبات ترش (Citrus aurantium) است و «نارنگی» میوهٔ شیرین کوچک. دو واژهٔ افزودهٔ کنار جعبه هم مشتق‌های همین صورت معرّب‌اند: «نارنجی» (رنگ) و «نارنجک» یعنی «نارنج کوچک»، نام امروزی نارنجک دستی. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%D9%86%D8%AC\",\n            \"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%D8%AC/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. نارنج (read via abadis.ir/fatofa/نارنج/, section فرهنگ معین): '(رِ ) (اِ.) درختی است پایا از تیرة مرکبات با میوة آب‌دار، درشت و کروی' and '(رَ ) [ معر. ] (اِ.) نیرنگ. ج. نارنجات' — the [معر.] tag is precisely the arrow Arabic → Persian. Nourai gives no volume/page, and the 6-volume edition cannot be paged online, but the entry text is unambiguous.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.4 p.2095, Mo'in's footnote to نارنج (BQT_v4_pages.txt [pdf page 178])\", \"stance\": \"supports\", \"note\": \"'معرب ... نارنگ (ه.م.) است [قی: نارنگی]. واصل این‌لغت هندی‌است. ولی‌ازراه ... زبانهای ایرانی وارد زبانهای اروپایی شد ... صورت orange درآمد' — Arabicised from nārang.\"},\n            {\"src\": \"MON\", \"where\": \"Dehkhoda's Loghatnameh s.v. نارنج (same abadis page), which quotes Mo'in's Borhan footnote verbatim\", \"stance\": \"supports\", \"note\": \"'نارنج معرب «نارنگ» است. اصل این لغت هندی است ولی از راه زبانهای ایرانی وارد زبانهای اروپائی شده به صورت اُرانژ ... درآمده ... ( برهان قاطع چ معین حاشیه ص 2095 )'; also '( آنندراج ) ( فرهنگ نظام ) ( شمس اللغات ) ( زمخشری )' all give 'معرب نارنگ'.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.257\", \"stance\": \"supports\", \"note\": \"Asbaghi's whole point in listing nāranǧ is that it is the Arabic shape of the Persian word; the re-borrowed Persian نارنج is the same form back again.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Spanish\",\n          \"words\": \"naranja\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Spanish naranja was taken directly from Andalusi Arabic nāranj during the Muslim period in the Peninsula, with Arabic -nj rendered by the Old Spanish palatal (later /x/, hence modern naranja /naˈɾanxa/); the initial n- is preserved here, in contrast to Italian and French. Wiktionary: 'Inherited from Old Spanish naranja, from Arabic نَارَنْج (nāranj), from Persian نارنگ (nârang), from Sanskrit नारङ्ग'. Devic and Lokotsch list it in the same position, and Klein has 'Arab. naranj (whence also Sp. naranja, Port. laranja, MGk. νεραντζιον)'. The node has no refs= in the book; the step itself is not in doubt. (Portuguese laranja shows the extra n- > l- dissimilation, and Catalan taronja is a different word, related to Spanish toronja 'grapefruit'.)\",\n          \"derivation_fa\": \"اسپانیایی کهن naranja را یک‌راست از عربی اندلسی nāranj گرفته‌اند، در دورهٔ حکومت مسلمانان در شبه‌جزیرهٔ ایبری؛ خوشهٔ -nj عربی به همخوان کامی اسپانیایی کهن بدل شد که بعدها /x/ شد (naranja امروزی). نکتهٔ مهم این است که نونِ آغازین در اسپانیایی حفظ شده، برخلاف ایتالیایی و فرانسه. ویکی‌واژه، دویک، لوکوچ و کلاین همه همین را می‌گویند («عربی nāranj که اسپانیایی naranja و پرتغالی laranja نیز از آن است»). این جعبه در کتاب بی‌ارجاع است ولی گامش مسلم است: ادعای نورایی درست است. (در پرتغالی laranja ابدال n به l رخ داده، و تارونجای کاتالانی واژهٔ دیگری است.)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/naranja\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; verified against Wiktionary, Devic p.184, Lokotsch 1555 and Klein p.1091.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, p.~184 s.v. Orange (DEV.txt line 1889, leaf 214)\", \"stance\": \"supports\", \"note\": \"'Orange. Esp. naranja, portug. laranja, ital. arancia, arancio (dialecte milanais, naranz, vénit. naranza), bas grec νεράντζιον ... Tous ces mots viennent de l'arabe نارنج narandj, persan نارنگ nareng, même signification.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no.1555, p.127\", \"stance\": \"supports\", \"note\": \"'hieraus über das gleichlautende ar. Wort sp. naranja, pg. laranja, kat. naronja, rum. nărănţă, it. arancia'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1091 s.v. orange\", \"stance\": \"supports\", \"note\": \"'fr. Arab. naranj (whence also Sp. naranja, Port. laranja, MGk. νεραντζιον)'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Italian\",\n          \"words\": \"arancia\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Italian form and its shape are right — arancia (fem. of arancio) goes back to an earlier narancia (Venetian naranza, Milanese naranz), the n- having been lost by false division of the article: una narancia was re-analysed as un'arancia (Devic: 'Les formes qui ont perdu le n initial l'ont sans doute laissé tomber par suite d'une fausse assimilation au n de une, una; une narange, una narancia, n'ont pas eu de peine à devenir une orange, una arancia'). This is the step that produced the n-less European word, so its position in the chart is essential and correct. What is not supported is the specific parent drawn here: no source routes Italian through Spanish. Klein has Italian arancia straight 'fr. Arab. naranj', with Spanish only as a sibling ('whence also Sp. naranja'); Etymonline the same ('from Italian arancia, originally narancia ... an alteration of Arabic naranj'); Wiktionary lists 'Italian: arancia' as a direct descendant of Arabic نَارَنْج; Skeat's own summary classifies orange as 'French from Italian from Persian'; and Hobson-Jobson makes the Italian come from Portuguese laranja instead ('the Portuguese laranja, from which last, or some similar form, by the easy detachment of the l ... we have the Ital. arancio'). Since Arabic Sicily and Ibero-Romance were both plausible points of contact the arrow is not absurd, but the intermediate language as drawn is Nourai's own.\",\n          \"derivation_fa\": \"صورت ایتالیایی و سرگذشت آوایی‌اش درست است: arancia (مادینهٔ arancio) از صورت کهن‌ترِ narancia می‌آید (در ونیزی naranza و در میلانی naranz) و نونِ آغازین آن با «تقطیع نادرست» حرف تعریف افتاده است: una narancia به un'arancia بازتحلیل شد. دویک همین را می‌گوید. همین گام است که واژهٔ بی‌نونِ اروپایی را ساخته، پس جای آن در نمودار لازم و درست است. اما پدرِ ترسیم‌شده پذیرفتنی نیست: هیچ منبعی ایتالیایی را از اسپانیایی نمی‌گیرد. کلاین arancia را یک‌راست «از عربی nāranj» می‌داند و اسپانیایی را در کنارش می‌گذارد نه پیش از آن؛ اتیمانلاین و ویکی‌واژه نیز همین‌گونه؛ خودِ اسکیت در فهرست پایانی‌اش orange را «فرانسه از ایتالیایی از فارسی» رده‌بندی می‌کند؛ و هابسون-جابسون ایتالیایی را از پرتغالی laranja می‌گیرد. پس این پیکان با احتیاط پذیرفتنی است و زبان واسطهٔ آن افزودهٔ خودِ نورایی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/arancia\",\n            \"https://www.etymonline.com/word/orange\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; checked against Klein p.1091, Etymonline, Wiktionary, Devic p.184, Lokotsch 1555 and Hobson-Jobson p.643, none of which routes Italian through Spanish.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1091 s.v. orange\", \"stance\": \"partial\", \"note\": \"'fr. It. arancia (in OIt. melarancia, lit. \\\"orange-apple\\\"), fr. Arab. naranj (whence also Sp. naranja ...)' — Italian direct from Arabic, Spanish a parallel.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.643\", \"stance\": \"contradicts\", \"note\": \"'the Spaniards naranja, old Italian narancia, the Portuguese laranja, from which last, or some similar form, by the easy detachment of the l (taken probably, as in many other instances, for an article), we have the Ital. arancio, L. Latin aurantium, French orange' — Yule derives the Italian from Portuguese, not Spanish.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic p.~184 s.v. Orange\", \"stance\": \"partial\", \"note\": \"lists 'ital. arancia, arancio' beside 'esp. naranja' as coordinate reflexes and says 'Tous ces mots viennent de l'arabe narandj'.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no.1555, p.127\", \"stance\": \"partial\", \"note\": \"'sp. naranja, pg. laranja, kat. naronja, rum. nărănţă, it. arancia' — all listed as parallel outcomes of the Arabic word.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box stands for French orange, and the step Italian → French is the well-attested one. Old French had orenge (12th c.) only inside pomme d'orenge, a calque of Old Italian melarancia 'orange-apple', from which the noun was later extracted; the Medieval Latin form pomum de orenge is recorded in between (Etymonline: 'from Old French orange, orenge (12c.), from Medieval Latin pomum de orenge, from Italian arancia, originally narancia'). Two explanations compete for the change of a- to o-: the traditional one, folk-etymological attraction to Old French or 'gold' from the colour of the fruit (Skeat: 'arenge became orenge by a popular etymology from or, gold'; Devic and Pihan the same), and Klein's, which argues from the long life of the phrase pomme d'orange that the fruit was rather associated with the town of Orange, 'an important transit station for the oranges bound for the north of France', and that 'the usual explanation ... must be abandoned' (following Bloch-Wartburg, DELF p.425). Wiktionary's French entry combines both: 'short form of late pomme d'orenge ..., which was calqued after Old Italian melarancia ... The o came into the word under influence of the place name Orange.'\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ واژهٔ فرانسوی orange است و گام «ایتالیایی ← فرانسه» به‌خوبی مستند است. در فرانسهٔ کهن صورت orenge (سدهٔ دوازدهم) تنها در ترکیب pomme d'orenge به کار می‌رفت که گَرته‌برداری از ایتالیایی کهن melarancia «سیب‌نارنج» است، و بعدها اسم از آن ترکیب بیرون کشیده شد؛ در میانه صورت لاتینی میانهٔ pomum de orenge هم ثبت شده است. دربارهٔ تبدیل a- آغازین به o- دو توضیح رقیب هست: توضیح سنتی، ریشه‌شناسی عامیانه و کشش به or «زر» به سبب رنگ میوه (اسکیت، دویک، پیان)؛ و توضیح کلاین که با تکیه بر دیرپایی ترکیب pomme d'orange می‌گوید نام شهر Orange — گذرگاه مهم بارِ نارنج به شمال فرانسه — عامل بوده و «توضیح رایج را باید رها کرد» (به پیروی از بلوخ-وارتبورگ ص ۴۲۵). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/orange\",\n            \"https://en.wiktionary.org/wiki/orange\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; verified against Etymonline, Wiktionary, Klein p.1091, Skeat p.360, Devic p.184 and Pihan pp.295-296.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1091 s.v. orange\", \"stance\": \"supports\", \"note\": \"'ME. orenge, orange, fr. MF. orenge (F. orange), in pomme d'orenge, fr. It. arancia ... The change of nar-ange to or-ange is prob. due to the influence of the name of the town Orange, an important transit station for the oranges bound for the north of France. The usual explanation ... due to a confusion with F. or, \\\"gold\\\" ... must be abandoned ... See Bloch-Wartburg, DELF., p.425 s.v. orange.'\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots ... dérivés de l'arabe, du persan ou du turc, pp.295-296 s.v. ORANGE\", \"stance\": \"supports\", \"note\": \"'Le mot orange se rattache, dit-on, au latin aurum (or); mais cette analogie n'est pas assez précise ... il vaut mieux en reconnaître la racine dans le persan نارنج [nârindj], que l'on retrouve dans le grec moderne νεραντζι, l'espagnol naranja, le portugais laranja, et l'italien arancio et narancio.'\"},\n            {\"src\": \"DEV\", \"where\": \"Devic p.~184 s.v. Orange\", \"stance\": \"supports\", \"note\": \"'une narange, una narancia, n'ont pas eu de peine à devenir une orange, una arancia' — the French form arises by the same false division.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"orange\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English orange is a French loan of the late 14th century (as a surname already late 13th c.): ME orenge/orange from Old/Middle French orenge, first of the fruit and only from the 1510s of the colour (before that Middle English used citrine or saffron for that hue). Skeat, on Nourai's own cited page, gives the whole chain: 'Orange. (F. - Ital. - Arab. - Pers.) O.F. orenge (F. orange). Put for *narenge, but the initial n was lost (in Italian), and then arenge became orenge by a popular etymology from or, gold. Cf. Span. naranja ... — Ital. arancia, an orange; Low Lat. arangia. — Arab. nāranj, nārinj. — Pers. nārang, an orange.' Klein and Etymonline agree on the English end of the chain. Earliest English attestations: the Alliterative Poems (ed. Morris) ii.1044, then Lydgate's Minor Poems (soon after 1400), oronge in the Promptorium Parvulorum (1440) and orenges in the Paston Letters (1470) — the list Skeat himself supplied to Notes and Queries and Hobson-Jobson quotes on p.643.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی orange وام‌واژه‌ای فرانسوی از اواخر سدهٔ چهاردهم است (به‌عنوان نام خانوادگی از اواخر سدهٔ سیزدهم): انگلیسی میانه orenge/orange از فرانسهٔ کهن و میانهٔ orenge؛ نخست نام میوه بوده و تنها از دههٔ ۱۵۱۰ به معنای رنگ به کار رفته است (پیش از آن در انگلیسی میانه برای آن رنگ citrine یا saffron می‌گفتند). اسکیت در همان صفحهٔ ۳۶۰ که نورایی به آن ارجاع می‌دهد، تمام زنجیره را می‌آورد: «فرانسه ← ایتالیایی ← عربی ← فارسی: فرانسهٔ کهن orenge، به جای *narenge، که نونِ آغازینش (در ایتالیایی) افتاده و سپس arenge به سبب ریشه‌شناسی عامیانه از or «زر» به orenge بدل شده ... ایتالیایی arancia ... عربی nāranj ... فارسی nārang». کلاین و اتیمانلاین نیز همین را می‌گویند. کهن‌ترین گواه‌های انگلیسی: «چکامه‌های تکیه‌دار» (۱۰۴۴)، سپس اشعار کوتاه لیدگیت (پس از ۱۴۰۰)، oronge در Promptorium Parvulorum (۱۴۴۰) و orenges در نامه‌های پاستون (۱۴۷۰). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/orange\",\n            \"https://en.wiktionary.org/wiki/orange\",\n            \"https://ia800404.us.archive.org/21/items/in.ernet.dli.2015.158267/2015.158267.A-Concise-Etymological-Dictionary-Of-The-English-Language_djvu.txt\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:360\", \"status\": \"supports\", \"note\": \"Nourai's page is exact, but only in the right copy. In the Skeat scan held locally (SKT.txt = IA aconciseetymolo01skeagoog) the Orange entry sits on leaf 341 (≈ printed p.321), and in the 1882 first edition (IA bub_gb_4ZkRAAAAIAAJ) it is on p.317; in the copy IA in.ernet.dli.2015.158267, however, the running head immediately before the entry reads '359' and the article stands on the next page, i.e. p.360 — Nourai's number: 'Orange. (F. - Ital. - Arab. - Pers.) O.F. orenge (F. orange). Put for *narenge, but the initial n was lost (in Italian), and then arenge became orenge by a popular etymology from or, gold. Cf. Span. naranja, an orange. — Ital. arancia, an orange; Low Lat. arangia. — Arab. nāranj, nārinj. — Pers. nārang, an orange. Allied to Pers. nār, a pomegranate.' Note for the owner: refs_online.json's SKT offset ('leaf = printed + 20', item aconciseetymolo01skeagoog) does not reproduce Nourai's page numbers; in.ernet.dli.2015.158267 does.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1091 s.v. orange (KLN_1966.txt line 26460, leaf 583)\", \"stance\": \"supports\", \"note\": \"'orange, n. — ME. orenge, orange, fr. MF. orenge (F. orange), in pomme d'orenge, fr. It. arancia ..., fr. Arab. naranj ..., fr. Pers. narang, fr. OI. nārangaḥ, \\\"orange tree\\\", which is of uncertain origin.'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.642-643 s.v. ORANGE\", \"stance\": \"supports\", \"note\": \"'A good example of plausible but entirely incorrect etymology is that of orange from Lat. aurantium. The latter word is in fact an ingenious medieval fabrication. The word doubtless came from the Arab. naranj ...', with the early English quotations (Promptorium Parvulorum 1440 'oronge', Paston Letters 1470 'orenges').\"},\n            {\"src\": \"FSD\", \"where\": \"FSD volumes, grep '^orange'\", \"stance\": \"silent\", \"note\": \"no usable hit in the Funk & Wagnalls OCR.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-349.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 349",
 "description": "Write and validate page-349.json"
}
```


### [2026-09-07T18:39:19.850Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'plausible': 4, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'partial': 3, 'not_checked': 7}
books consulted: {'supports': 28, 'silent': 10, 'partial': 10, 'contradicts': 2} | by book: {'KLN': 9, 'LKT': 5, 'SKT': 3, 'WLD': 3, 'MON': 3, 'BQT': 3, 'PLA': 3, 'DEV': 3, 'IEC': 2, 'LAT': 2, 'LEW': 2, 'AHD': 2, 'FSD': 2, 'HJB': 2, 'HUB': 1, 'ARY': 1, 'WEB': 1, 'HRN': 1, 'AFM': 1, 'PHN': 1}
```


## [2026-09-07T18:39:51.595Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-349.json` written; `verify_check.py 349` reports **15/15 nodes, 0 PROBLEM lines**.

**Verdicts (pdf 349 / book 319)** — roots: 2 confirmed. Nodes: 9 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 13 supports, 3 partial, 7 not_checked. 20 books consulted.

- **transcription_suspect — Nana/Nena, node #4 [Late Latin] "nun"**: the printed page really prints `nun` in the Late Latin box (verified on the rendered page, copied to `data/verification/sources/refs/ocr/BOOK/349.png`), i.e. Nourai put the English gloss where the Latin form belongs. Correct form: `nonna` (f.) / `nonnus` (m.) — his own source (AHD/Watkins p.44) prints "Late and Medieval Latin nonna". `error_in: "book"`; extraction is faithful, **no data fix needed**.
- **disputed — Naranga, node #1, word `anâr` «انار ؟»**: Persian انار is inherited from MP *anār* (Mo'in tags it «[په.]»; Wiktionary: from MP ʾnʾl), unrelated to Skt. *nāraṅga*. Nourai's two props both fail: Skeat p.360's "Allied to Pers. nār" is an 1901 guess no later authority repeats, and IEC:1645 is unverifiable (see below). Asbaghi p.257 is the only source linking them, and he reverses the arrow (*nārang* = *anār* + *rang*). The other two words in the node (nâreng, nârengî) are confirmed.
- **plausible (4)**: #2 Persian *naneh* (Horn p.234 no.1044 only *compares* Skt. nanā; Wiktionary "originally from baby talk" — parallel Lallwort, not descent); #3 Eng. *nana/nanny* (AHD's baby-talk route, but Beelen–van der Sijs 2018 make it a hypocoristic of Anne); #6 Greek (νάννα 'aunt' is in Pokorny 754, νᾶνος 'dwarf' is not — Beekes rejects the link, Klein says "perh."); #5 Italian *arancia* (no source routes it via Spanish — Klein/Etymonline/Wiktionary derive it straight from Arabic, Hobson-Jobson from Portuguese *laranja*).

**Reference-page findings for the owner (not extraction errors):**
- All Nourai page numbers checked out exactly: POK:754, HRN:234, KLN:1062, KLN:1027, HJB:642, BQT:2095 (independently confirmed by Dehkhoda citing «برهان قاطع چ معین حاشیه ص ۲۰۹۵»), SKT:360.
- **`refs_online.json` SKT offset is wrong for Nourai's pagination**: in the local scan (`aconciseetymolo01skeagoog`) *Orange* sits ≈p.321 and in the 1882 ed. at p.317, but in IA copy **`in.ernet.dli.2015.158267` it is on p.360** — Nourai's number. Suggest recording that item as the SKT reference copy.
- **IEC:1645 unverifiable**: Mann p.1645 lies in the Supplement (vol. II, pp.1573–1684); the only scan available stops ≈p.1554 and its full-text index has no match for "juicy". Mann's accessible *nor-* entries (p.~920) mean 'penetration', 'joint', 'narrow' — none 'juicy'.
- `AHD:872` (2×) not checkable — 1975/76 New College Edition is lending-only; substituted the open Watkins 1985 root entry `nana` (p.44), which supports every branch of the chart.
- Bonus corroboration: Lokotsch no.1553 (p.127) cites Horn p.234 for Persian *nānā* 'Mutter', independently validating Nourai's HRN:234.

19 web sources archived via `fetch_source.py`.
