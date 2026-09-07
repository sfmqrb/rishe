# Verification process log — verify-page-371


## [2026-09-07T20:16:04.069Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 371 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-371.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-371.json. Write /home/sfmqrb/git/rishe/data/verification/page-371.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 371` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:06.139Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:06.813Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:06.824Z] TOOL RESULT

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


## [2026-09-07T20:16:07.391Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-371.txt"
}
```


### [2026-09-07T20:16:07.414Z] TOOL RESULT

```
1	=== PDF page 371 (book page 341) ===
2	--- entry 0 ---
3	ROOT [Semitic] N.w.r : to shine, light up  (refs KLN:982)
4	#1 (parent #0) [Arabic] refs=KLN:963,982 | nŭr : light ; nâr : fire ; manâreh : candlestick, lighthouse, minaret
5	  #2 (parent #1) [Persian] refs=MON; SAP:1734; FVA:418 | nŭr «نور (انوار ، انور)» : light ; manâr «مَنار (مَناره)» : minaret ; nâr «نار» : fire | extra: نورانی ، نیّره ، مُنیر ، منوّر ، تنویر
6	#3 (parent #0) [English] refs=KLN:982 | minaret
7	#4 (parent #0) [Hebrew] refs=KLN:963 | měnôrâh : candlestick ; ab-ner : my father is light ☞Ab 2
8	  #5 (parent #4) [English] refs=None | menorah, Abner
9	--- entry 1 ---
10	ROOT [Avestan / Old Persian] Nyâka, Nyâkâ : grand parent  (refs SYN:110; KNT:194)
11	#1 (parent #0) [Pahlavi] refs=BQT:2221; UNV:52 | niyâk, niyâkân : grandparents
12	  #2 (parent #1) [Persian] refs=BQT:2221; HRN:238 | nîyâ «نیا ، نیاکان» : ancestor
13	#3 (parent #0) [Avestan / Old Persian] refs=KNT:168 | apa-nyâka : great grandfather, ancestor ☞Apo
14	  #4 (parent #3) [None] refs=None | 
15	--- entry 2 ---
16	ROOT Nyâkâ -> redirect to Nyâka
17	
```


## [2026-09-07T20:16:11.127Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-371.json",
 "description": "Read source JSON"
}
```


### [2026-09-07T20:16:11.171Z] TOOL RESULT

```
{
  "pdf_page": 371,
  "book_page": 341,
  "entries": [
    {
      "root": {
        "name": "N.w.r",
        "lang": "Semitic",
        "refs": "KLN:982",
        "gloss": "to shine, light up"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:963,982",
          "words": [
            {"translit": "nŭr", "gloss": "light", "script": null},
            {"translit": "nâr", "gloss": "fire", "script": null},
            {"translit": "manâreh", "gloss": "candlestick, lighthouse, minaret", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; SAP:1734; FVA:418",
          "words": [
            {"translit": "nŭr", "gloss": "light", "script": "نور (انوار ، انور)"},
            {"translit": "manâr", "gloss": "minaret", "script": "مَنار (مَناره)"},
            {"translit": "nâr", "gloss": "fire", "script": "نار"}
          ],
          "script_extra": "نورانی ، نیّره ، مُنیر ، منوّر ، تنویر",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "English",
          "refs": "KLN:982",
          "words": [
            {"translit": "minaret", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:963",
          "words": [
            {"translit": "měnôrâh", "gloss": "candlestick", "script": null},
            {"translit": "ab-ner", "gloss": "my father is light", "script": null, "see": ["Ab 2"]}
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
            {"translit": "menorah, Abner", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nyâka, Nyâkâ",
        "lang": "Avestan / Old Persian",
        "refs": "SYN:110; KNT:194",
        "gloss": "grand parent"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:2221; UNV:52",
          "words": [
            {"translit": "niyâk, niyâkân", "gloss": "grandparents", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2221; HRN:238",
          "words": [
            {"translit": "nîyâ", "gloss": "ancestor", "script": "نیا ، نیاکان"}
          ],
          "note": null,
          "quote": {
            "text": "چنین بود رسم نیاکان تو - سرافراز و دیندار و پاکان تو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KNT:168",
          "words": [
            {"translit": "apa-nyâka", "gloss": "great grandfather, ancestor", "script": null, "see": ["Apo"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": null,
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nyâkâ",
        "redirect": "Nyâka"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:16:12.908Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','MON','SAP','FVA','SYN','KNT','BQT','UNV','HRN','POK','AHD','WLD','IEC','BRT','PHD','NYB','HUB','ARY','FVQ','AFM','PLA','SKT','WEB','FSD','CHEUNG']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


### [2026-09-07T20:16:14.375Z] TOOL RESULT

```
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
=== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c
=== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
=== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
=== UNV {"title": "J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Text Der König Husrav und sein Knabe', Heidelberg diss. 1917]", "edition_found": "1917 German dissertation edition (text + glossary); 1963 Paris ed. not found", "kind": "archive_djvu", "url": "https://archive.org/details/derpahlavitextde00unva", "identifier": "derpahlavitextde00unva", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt", "page_offset": "leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \\f between leaves (0-based l
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
=== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
=== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
=== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
=== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
=== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
=== CHEUNG MISSING
```


## [2026-09-07T20:16:25.429Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:16:25.473Z] TOOL RESULT

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


## [2026-09-07T20:16:26.020Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -100; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head -40"
}
```


### [2026-09-07T20:16:26.076Z] TOOL RESULT

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
SKT_dli_revised.txt
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
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-07T20:16:30.377Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"minaret\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== menorah\"; grep -n -i \"menorah\\|men.r.h\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-07T20:16:30.457Z] TOOL RESULT

```
KLN_1971.txt:148920:element in Abner. Cp. also minaret and the last 
KLN_1971.txt:151808:minaret, n., a slender tower attached to a 
KLN_1971.txt:156156:cial who, from the minaret of the mosque, calls 
KLN_1966.txt:23475:—  Heb.  mlnorah,  ‘candlestick’,  from  stem  n-w-r, ‘to  give  light,  shine’,  whence  also  ner,  ‘lamp’ ;  rel. to  Aram. -Syr.  nur,  ‘fire’,  Arab,  nara,  ‘shone’, nur,  ‘light’,  nar,  ‘fire’,  Aram,  mfnarta,  ‘candle¬ stick’,  Arab.  manarah,  ‘candlestick;  lighthouse; tower  of  a  mosque’,  Akkad,  nuru,  ‘light’,  nawa- ru,  namaru,  ‘to  give  light,  shine".  Cp.  the  second element  in  Abner.  Cp.  also  minaret  and  the  last element  in  Koh-i-noor.
KLN_1966.txt:23949:Minaean,  adj.  —  Formed  with  suff.  -an  fr.  L. Minaei  (pi.),  a  people  in  South  Arabia,  fr.  Gk. Mtvsiot,  fr.  Arab.  Ma'am,  they  are  mentioned in  the  Bible  under  the  names  of  M  'untm  (I  Chr. 4  :  41,  II  Chr.  26  :  7)  and  Ma'Sn  (Judg.  10  :  12). minaret,  n.,  a  slender  tower  attached^  to  a mosque.  —  Sp.  minarete,  fr.  Turk,  menaret,  fr. Arab.  manarah,  ‘candlestick ;  tower  of  a  mosque, lighthouse’,  fr.  nara,  ‘it  lighted’,  rel.  to  Heb. ner,  ‘lamp’,  mlndrdh,  Aram.  mlnartd,  ‘candle¬ stick’.  See  Menorah.
KLN_1966.txt:23950:Derivative:  minarett-ed,  adj. minatory,  adj.,  threatening.  —  Late  L.  minatdrius.
KLN_1966.txt:24579:muezzin,  n.,  in  Mohammedan  countries,  an  offi¬ cial  who,  from  the  minaret  of  the  mosque,  calls the  people  to  prayer.  —  Arab,  mu'  adhdhiti,  prop, active  part,  of  adhdhana,  II  (=  frequentative  or intensive)  conjugation  of  adhana,  ‘he  proclaim¬ ed’,  fr.  udhn,  ‘ear’,  which  is  rel.  to  Ethiop.  ezn, Heb.  Szen,  Aram,  udhna,  Syr.  edhnd,  Akkad. uznu,  ‘ear’,  Heb.  he'lzln,  ‘he  gave  ear,  heard, listened,  hearkened’.
=== menorah
KLN_1971.txt:4484:Aboth, for the second see Menorah. 
KLN_1971.txt:132078:nur, ‘light’ (see Menorah). 
KLN_1971.txt:148910:Menorah, n., the seven-branched candelabrum in 
KLN_1971.txt:148923:menorrhagia, n., excessive menstruation (med.) 
KLN_1971.txt:151816:stick’. See Menorah. 
KLN_1971.txt:209401:ing forth, excessive flow’, as in menorrhagia 
KLN_1966.txt:1191:lonian  PN.  Abunuri.  For  the  first  element  see Aboth,  for  the  second  see  Menorah. abnormal,  adj.  — ■  A  blend  of  L.  abnormis  and ML.  anormalis,  this  latter  itself  being  a  blend of  L.  anomalus  and  normalis.  See  anomalous  and norm  and  cp.  anormal.
KLN_1966.txt:20824:Koh-i-noor,  n.,  a  famous  diamond,  one  of  the British  crown  jewels.  —  Pers.  koh-i-nur,  lit. ‘mountain  of  light’,  prop,  a  hybrid  coined  fr. Pers.  koh,  ‘mountain’,  which  is  rel.  to  Pers. kohe,  ‘hump’,  OPers.  kaufa-,  ‘mountain’,  Aves- tic  kaofa-,  ‘mountain,  hump’,  and  fr.  Arab. nur,  ‘light’  (see  Menorah). kohl,  n.,  powder  (esp.  of  antimony),  used  by  East¬ ern  women  to  darken  the  eyelids.  —  Arab. kuhl.  See  alcohol.
KLN_1966.txt:23474:Menorah,  n.,  the  seven-branched  candelabrum  in the  Tabernacle  and  in  the  Temple  of  Jerusalem.
KLN_1966.txt:23476:menorrhagia,  a.,  excessive  menstruation  (med.)
KLN_1966.txt:23949:Minaean,  adj.  —  Formed  with  suff.  -an  fr.  L. Minaei  (pi.),  a  people  in  South  Arabia,  fr.  Gk. Mtvsiot,  fr.  Arab.  Ma'am,  they  are  mentioned in  the  Bible  under  the  names  of  M  'untm  (I  Chr. 4  :  41,  II  Chr.  26  :  7)  and  Ma'Sn  (Judg.  10  :  12). minaret,  n.,  a  slender  tower  attached^  to  a mosque.  —  Sp.  minarete,  fr.  Turk,  menaret,  fr. Arab.  manarah,  ‘candlestick ;  tower  of  a  mosque, lighthouse’,  fr.  nara,  ‘it  lighted’,  rel.  to  Heb. ner,  ‘lamp’,  mlndrdh,  Aram.  mlnartd,  ‘candle¬ stick’.  See  Menorah.
KLN_1966.txt:33242:-rrhagia,  combining  form  used  to  denote  ‘a  burst¬ ing  forth,  excessive  flow’,  as  in  menorrhagia ( med .)  —  Medical  L.,  fr.  Gk.  -ppoqxa,  ‘a  burst¬ ing  forth’,  from  the  stem  of  prjYvuvai.,  ‘to  break forth,  burst  forth’.  See  regma.
```


## [2026-09-07T20:16:31.742Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Abner\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== nur/nawara\"; grep -n -i \"n.wer\\|nawara\\|nūr\\|manārah\\|man.rah\" KLN_1966.txt | head -30"
}
```


### [2026-09-07T20:16:31.827Z] TOOL RESULT

```
KLN_1971.txt:4480:Abner, n., masc. PN.; in the Bible, commander 
KLN_1971.txt:4623:Cp. the first element in Abraham, Abner, Absa- 
KLN_1971.txt:148920:element in Abner. Cp. also minaret and the last 
KLN_1966.txt:1190:Abner,  n.,  masc.  PN.;  in  the  Bible,  commander of  Saul.  —  Heb.  Abhnir,  lit.  ‘my  father  is  light’, fr.  abh,  ‘father’,  and  ner,  ‘light’;  cp.  the  Baby¬
KLN_1966.txt:1209:Derivatives:  abortion-al,  adj.,  abortion-ist ,  n. abortive,  adj.,  I)  born  prematurely;  2)  unsuccess¬ ful.  —  L.  abortivus,  ‘pertaining  to  miscarriage’, fr.  abortus,  pp.  of  aboriri.  See  abort,  v.,  and  -ive. Derivatives:  abortive-ly,  adj.,  abortive-ness,  n. Aboth,  also  Abot,n.,  i)the  Mishnah  treatise  also called  Pirke  Aboth  or  The  Ethics  of  the  Fathers  ', 2)  name  of  the  first  benediction  of  the  Shemoneh Esreh  ( Jewish  liturgy).  —  Heb.  Abhdth,  pi.  of abh,  ‘father’,  rel.  to  Aram,  abh  (absolute  state), abbd  (emphatic  state),  Ugar.  ’b,  Arab,  ab, Ethiop.  ab,  ‘father’ ;  of  uncertain  origin,  possibly traceable  to  *ab(a),  a  child’s  word  for  father. Cp.  the  first  element  in  Abraham,  Abner,  Absa¬ lom,  Abigail,  and  the  second  element  in  Joab, Moab,  Barabbas.  Cp.  also  abbot  and  words there  referred  to.  Cp.  also  borage, abound,  intr.  v.  —  ME.  abounden,  fr.  OF,  (=  F.) abonder,  fr.  L.  abundare,  ‘to  overflow;  to  a- bound’,  fr.  ab-  and  unda,  ‘wave’.  See  undate  and cp.  redound,  surround.  Derivatives:  abound-er, n.,  abound-ing,  adj.,  abound-ing-ly,  adv. about,  adv.  —  ME.  abuten,  abouten,  about e,  fr. OE.  abutan,  onbutan,  ‘on  the  outside  of’,  formed fr.  a-,  ‘on’,  and  butan,  ‘outside’,  which  itself  is formed  fr.  be,  ‘by’,  and  iitan,  ‘outside’,  fr.  ut, ‘out’.  See  by  and  out  and  cp.  but.
KLN_1966.txt:23475:—  Heb.  mlnorah,  ‘candlestick’,  from  stem  n-w-r, ‘to  give  light,  shine’,  whence  also  ner,  ‘lamp’ ;  rel. to  Aram. -Syr.  nur,  ‘fire’,  Arab,  nara,  ‘shone’, nur,  ‘light’,  nar,  ‘fire’,  Aram,  mfnarta,  ‘candle¬ stick’,  Arab.  manarah,  ‘candlestick;  lighthouse; tower  of  a  mosque’,  Akkad,  nuru,  ‘light’,  nawa- ru,  namaru,  ‘to  give  light,  shine".  Cp.  the  second element  in  Abner.  Cp.  also  minaret  and  the  last element  in  Koh-i-noor.
=== nur/nawara
2460:amuna,  ‘he  was  faithful’,  d'mana,  ‘he  believed’, amtn,  ‘faithful’.  Cp.  ameen.  Cp.  also  mammon, amenable,  adj.,  answerable;  willing;  submissive. —  Formed  with  suff.  -able  fr.  F.  amener,  ‘to lead,  or  bring  up,  to’,  fr.  a,  ‘to’  (see  a),  and mener,  ‘to  lead’,  fr.  VL.  minare,  ‘to  drive  (ani¬ mals)  by  shouting’,  fr.  L.  minari,  ‘to  threaten’. The  orig.  meaning  of  L.  minari  has  survived  in Rum.  mana,  ‘to  threaten’.  See  menace  and  -able. Derivatives :  amenabil-ity,  n.,  amenable-ness,  n., amenabl-y,  adv.
2887:Anser,  n.,  a  genus  of  birds,  the  goose  ( ornithol .) —  L.  anser,  ‘goose’,  for  *hanser.  See  goose  and cp.  the  second  element  in  merganser, anserine,  adj.,  1)  pertaining  to,  or  resembling,  a goose;  2)  stupid.  —  L.  anserinus,  fr.  anser.  See prec.  word  and  -ine  (representing  L.  -tnus). answer,  n.  —  ME.  andsware,  answere,  fr.  OE. andswaru,  ‘a  reply’,  lit.  ‘a  swearing  against ,  fr. and-,  ‘against’,  and  swerian,  ‘to  swear’ ;  cp.  OS. antswor,  ON.  andsvar  (Dan.,  Swed.  ansvar), OFris.  ondser.  The  first  element  is  cogn.  with Gk.  avrf,  ‘against’,  L.  ante,  ’before’.  See  ante- and  cp.  anti-.  For  the  second  element  see swear.
2888:answer,  tr.  and  intr.  v.  —  ME.  andswerien,  fr.  OE. andswarian,  andswerian,  fr.  andswaru.  See answer,  n.  Derivatives:  answer-able,  adj.,  an- swer-er,  n.,  answer-ing,  adj. ant,  n.  — ME.  amete,  ante,  fr.  OE.  xmete,  zmette, rel.  to  OHG.  amei^a,  MHG.  amei3e,  G.  Ameise, ‘ant’,  lit.  ‘the  animal  that  cuts  (i.e.  bites)  off’, fr.  Teut.  a,  ‘off’,  and  *maitan,  ‘to  cut’  (whence Goth,  maitan,  ON.  meita,  OHG.  mei^an,  ‘to cut’,  ON.  meitill,  OHG.  mei^il,  MHG.  mei^el, G.  Meifiel,  ‘chisel’).  Cp.  emmet.  Cp.  also  mite, ‘a  small  arachnid’, ant-,  form  of  anti-  before  a  vowel.
2898:Antares,  n.,  a  large  red  star,  the  brightest  in  the Constellation  Scorpio.  —  Gk.  ’  Avxapr]<;,  lit.  ‘op¬ posite  (the  planet)  Mars’,  fr.  avxi,  ‘opposite’, and  "Apr]4,  ‘Mars’.  See  anti-  and  Ares, ante-,  pref.  —  Fr.  L,  ante,  ‘before,  in  front  of’, which  is  cogn.  with  OI.  anti,  ‘opposite  ,  Toch. B  ente,  ‘opposed  to’.  Arm.  lnd,  ‘opposite’,  Gk. £vxa,  5vt7)v,  ‘opposite’,  avxt,  ‘over  against, opposite,  before’,  OLith.  anta,  Lith.  ant,  ‘on to’,  Goth,  and,  anda,  ‘along’,  ON.,  OS.,  OE. and-  ‘against’,  OHG.,  MHG.,  G.  ant-,  OHG. inf-,  MHG.,  G.  ent-,  ‘along,  against’,  Hitt,  hand, ‘opposite’,  hantezzish,  ‘the  first’.  Cp.  anti-.  Cp. also  Ananta,  antiae,  enantio-,  the  first  ele¬ ment  in  ancestor,  antique,  antiquity,  and  the second  element  in  Rosinante  and  in  Vedanta. Cp.  also  end,  un-,  pref.  expressing  reversal,  and the  first  element  in  along  and  in  answer, antecede,  tr.  and  intr.  v.  —  L.  antecedere,  ‘to  go before’,  fr.  ante-  and  cedere,  ‘to  go’.  See  cede and  cp.  precede.
2916:anthem,  n.  —  ME.  antefne,  antem,  fr.  OE.  antefn (orig.  identical  in  meaning  with  antiphony),  fr. ML.  antiphona,  fr.  Gk.  avxi^oiva,  neut.  pi.  of avxiqxovo;,  ‘sounding  in  answer  to’,  which  was mistaken  for  fern.  sing.  Sec  antiphon.
2989:Derivative:  antiphlogistic,  n. antiphon,  n.,  a  versicle  sung  responsively.  —  F. antiphone,  fr.  ML.  antiphona,  fr.  Gk.  dvxitpoiva, neut.  pi.  of  dvxicpotvo;,  ‘sounding  in  answer to’,  mistaken  for  fem.  sing.;  fr.  avxi,  ‘over against,  in  response  to’  (see  anti-),  and  (pew;, ‘voice,  sound’ ;  see  phone,  n.  Cp.  anthem,  which is  a  doublet  of  antiphon.
2992:antiphonon,  n.,  an  antiphon.  —  Gk.  avxi^tavov, neut.  of  dvx( qjcovoc,  ‘sounding  in  answer  to’.
3135:-ize  and  answers  in  sense  to  Gk.  dtTtoXoyEioOoa, ‘to  speak  in  defense,  defense  oneself’. Derivative:  apologiz-er,  n. apologue,  n.,  moral  truth.  —  F.,  fr.  L.  apologus, fr.  Gk.  inbXofoq,  ‘story,  tale,  fable,  apologue, account’,  lit.  ‘(that  which  comes)  from  a  speech’, fr.  (xttA  (see  apo-)  and  Xoy 6?,  ‘word,  speech, discourse,  account’.  See  logos, apology,  n.  —  F.  apologie,  fr.  L.  apologia,  fr.  Gk. dmoXoyla,  ‘a  speech  in  defense’,  fr.  a-rroXoyo;, See  prec.  word  and  -y  (representing  Gk.  -ta). apomorphine,  n.,  name  of  a  drug,  C17H17N02 (chem.)  —  Changed  fr.  earlier  apomorphia,  a name  coined  by  the  chemists  Mathieson  and Wright  fr.  apo-  and  morphine.  They  gave  the drug  this  name  because  it  is  obtainable  from morphine.
5451:change  of  Antwerp  built  after  the  pattern  of that  in  Bruges  was  called  Bourse.  Later  this  word became  the  general  name  denoting  exchange. See  Bloch-Wartburg,  DELF.,  p.  81.  Cp.  bur¬ sar,  disbourse.
6785:catechist,  n.,  one  who  instructs  by  questions  and answers.  —  Eccles.  L.  catechista,  fr.  Gk.  xaxrr -/iCT-rr,c,  fr.  xar/jx^ew.  See  next  word  and  -ist. Derivatives:  catechist-ic,  catechist-ic-al,  adjs., catechist-ic-al-ly,  adv.
7112:chafe  with  agential  suff.  -er.  Cp.  chauffer, chafer,  n.,  a  beetle.  —  ME.,  fr.  OE.  ceafor,  rel. to  OS.  kevera,  Du.  kever,  OHG.  chevar,  MHG. kever,  G.  Kdfer,  lit.  ‘gnawer’.  Cp.  MHG.  kiven, Du.  keveren,  ‘to  gnaw’,  OE.  ceafl,  ME.  chavel, G.  Kiefer,  ‘jaw’,  and  see  jowl,  ‘jaw’, chaff,  n.,  husk  of  grain.  —  ME.  chaf  fr.  OE.  ceaf rel.  to  MDu.,  Du.  kaf  G.  Kaff,  and  prob.  also to  OHG.  cheva,  MHG.  keve,  ‘husk’. Derivatives:  chaff,  tr.  v.,  chaff-y,  adj. chaff,  tr.  v.,  to  banter.  —  Prob.  a  var.  of  chafe, chaffer,  n.,  a  bargain.  —  ME.  cheapfare,  chapfare, chaffare,  fr.  OE.  ceap,  ‘price,  bargain’  and  faru, ‘going,  journey,  proceeding’.  For  the  first  ele¬ ment  see  chapman,  cheap,  for  the  second  see fare.
9275:correspond,  intr.  v.  —  F.  correspondre,  fr.  ML. corresponded,  fr.  cor-  and  L.  responded,  ‘to answer’.  See  respond.
11237:dialectic,  n.,  the  art  of  discussion.  —  OF.  (=  F.) dialectique,  fr.  L.  dialectica  (scil.  ars),  fr.  Gk. SiaXsxTixf)  (scil.  Tsyvr]),  ‘the  art  of  discussion by  question  and  answer’,  fem.  of  SiaXexxixA;, ‘skilled  in  discourse’.  See  dialectic,  adj. Derivatives:  dialectic-al,  adj.,  dialectic-al-ly,  n.
12383:duffel,  duffle,  n.,  a  thick  woolen  cloth  with  a thick  nap.  —  Du.  duffel,  fr.  Duffel,  a  town  near Antwerp.
18501:hypocrisy,  n.  —  ME.  ipocrisie,  fr.  OF.  ypocrisie, fr.  Eccles.  L.  hypocrisis,  fr.  Gk.  uxGxp'.atc,  ‘an acting  on  the  stage;  hypocrisy’,  from  the  stem of  uxoxpfvEC&ai,  ‘to  answer,  pretend,  play  a part’,  fr.  6x6  (see  hypo-)  and  xpfveaUat,  ‘to  dis¬ pute’,  middle  voice  of  xpfvetv,  ‘to  judge’.  F. hypocrisie  and  E.  hypocrisy  have  been  refash¬ ioned  after  the  Latin  form  of  the  word.  See critic  and  cp.  words  there  referred  to. hypocrite,  n.  —  ME.  ipocrite,  ypocrite,  fr.  OF. ipocrite,  ypocrite  (F.  hypocrite),  fr.  Eccles.  L. hypocrita,  fr.  Gk.  6xoxpixf)i;,  ‘an  actor,  pre¬ tender,  hypocrite’,  fr.  uxoxpEveaD-at.  See  prec. word.
20200:jawab,  n.,  an  answer;  a  building  corresponding to,  or  imitating,  another.  —  Hind,  jawab,  fr.
20201:Arab,  jawdb,  ‘answer’,  which  is  rel.  to  ajdba, jdwaba,  ‘he  answered’.
20488:juror,  n.,  a  member  of  a  jury.  —  ME.  juroure,  fr. AF.  jurour,  corresponding  to  OF.  jureor  (F. jureur),  ‘one  who  swears’,  fr.  L.  jurdtorem,  acc. of  jurator,  fr.  juratus,  pp.  of  jurare,  ‘to  take  an oath,  swear’.  See  jus  and  agential  stiff,  -or. jury,  n.,  a  body  of  persons  sworn  to  give  a  true answer  or  verdict  on  a  matter  submitted  to them.  —  OF.  juree,  ‘oath,  legal  inquiry’,  prop, fern.  pp.  used  as  a  noun,  fr.  OF.  (=  F.)  jurer, ‘to  take  an  oath,  swear’,  fr.  L.  jurare,  of  s.m., fr.  jus,  gen.  juris,  ‘right,  law’.  See  jus  and  -y (representing  OF.  -ee,  F.  -ee)  and  cp.  jurat  (in both  senses),  juror,  abjure,  adjure,  conjure, perjure.
21103:liamentary  assembly’.  Cp.  also  the  second  ele¬ ment  in  Reichstag,  Rigsdag,  Riksdag, landwehr,  n.,  military  reserve  of  trained  armed forces  in  Germany  and  other  countries  (mil.)  — G.,  fr.  MHG.  lantwer,  fr.  OHG.  lantweri,  ‘army for  the  protection  of  the  country’,  which  is  com¬ pounded  of  lant,  ‘land’,  and  weri,  ‘protection’. See  land  and  weir.
22759:Mandaic,  adj.  and  n.  —  See  prec.  word  and  -ic. mandamus,  n.,  a  writ  from  a  superior  court  to  an inferior  court  that  a  specified  thing  be  done (law).  _  l.,  ‘we  command’,  1st  person  pi.  of the  pres,  indie,  of  mandare.  See  mandate, mandarin,  n.,  a  Chinese  public  official.  Port. mandarim ,  fr.  Hind,  mantri,  fr.  OI.  mantrin -, ‘conselor’,  fr.  mantrah,  "counsel  ,  which  derives fr.  I.-E.  base  ‘men-,  ‘to  think’,  whence  also  Ol. manyate,  ‘thinks’.  The  Port,  word  was  influ¬ enced  in  form  by  Port,  mandar,  ‘to  command, order’.  See  mind  and  cp.  mantra.
22847:Derivative:  mantle,  tr.  and  intr.  v. mantra,  n.,  that  part  of  the  Vedas  which  contains hymns  ( Hinduism)  —  OI.  mantrah,  lit.  ‘speech, sacred  text,  counsel’,  rel.  to  Avestic  mqftra-,  of S.m.  See  mandarin.
23475:—  Heb.  mlnorah,  ‘candlestick’,  from  stem  n-w-r, ‘to  give  light,  shine’,  whence  also  ner,  ‘lamp’ ;  rel. to  Aram. -Syr.  nur,  ‘fire’,  Arab,  nara,  ‘shone’, nur,  ‘light’,  nar,  ‘fire’,  Aram,  mfnarta,  ‘candle¬ stick’,  Arab.  manarah,  ‘candlestick;  lighthouse; tower  of  a  mosque’,  Akkad,  nuru,  ‘light’,  nawa- ru,  namaru,  ‘to  give  light,  shine".  Cp.  the  second element  in  Abner.  Cp.  also  minaret  and  the  last element  in  Koh-i-noor.
23949:Minaean,  adj.  —  Formed  with  suff.  -an  fr.  L. Minaei  (pi.),  a  people  in  South  Arabia,  fr.  Gk. Mtvsiot,  fr.  Arab.  Ma'am,  they  are  mentioned in  the  Bible  under  the  names  of  M  'untm  (I  Chr. 4  :  41,  II  Chr.  26  :  7)  and  Ma'Sn  (Judg.  10  :  12). minaret,  n.,  a  slender  tower  attached^  to  a mosque.  —  Sp.  minarete,  fr.  Turk,  menaret,  fr. Arab.  manarah,  ‘candlestick ;  tower  of  a  mosque, lighthouse’,  fr.  nara,  ‘it  lighted’,  rel.  to  Heb. ner,  ‘lamp’,  mlndrdh,  Aram.  mlnartd,  ‘candle¬ stick’.  See  Menorah.
29177:plight,  n.,  pledge.  —  ME. pliht, pligt,  ‘danger;  en¬ gagement’,  fr.  OE.  pliht,  ‘risk,  danger’,  rel.  to OFris.,  MDu.,  Du.  plicht,  ‘care,  carefulness’, OHG.  pfliht,  MHG.,  G.  pflicht,  ‘obligation,  du¬ ty’,  MDu.  pleghen,  Du.  plegen,  ‘to  care  for’,  be accustomed  to’,  OHG.  pflegan,  MHG.,  G.  pfle- gen,  of  s.m.,  MDu.  plien,  ‘to  answer  for,  guar¬ antee’,  OE.  pleon  (for  * plehan ),  ‘to  risk,  expose to  danger’.  See  play,  v.,  and  cp.  plege. plight,  tr.  v.,  to  pledge.  —  ME.  plighten,  fr.  OE. plihtan,  ‘to  pledge’,  fr.  pliht,  ‘risk,  danger’.  Cp. Du.  ver-plichten,  G.  ver-pflichten,  ‘to  bind, oblige’,  and  see  plight,  ‘pledge’.
31432:quinquevalence,  quinquevalency,  n. ,  state  of  being quinquevalent  (chem.)  —  Formed  from  next word  with  suff.  -ce,  resp.  -cy. quinquevalent,  adj.,  having  a  valence  of  five (chem)  —  Compounded  of  quinque-  and  L. valens,  gen.  -entis,  pres.  part,  of  valere,  ‘to  have power’  (see  -valent) ;  prop,  loan  translation  of  G. funfwertig,  which  is  compounded  of fiinf  ‘five’, and  Wert,  ‘value’.  Cp.  pentavalent. quinquina,  n.,  cinchona.  —  Sp.,  fr.  Quechua  quin¬ quina.  See  quinine.
31873:Derivatives:  rebutt-able,  adj.,  rebutt-al,  n., rebutt-er,  n.,  that  which  rebuts, rebutter,  n.,  a  defendant’s  answer  to  a  plaintiff’s surrejoinder.  —  AF.  rebuter,  fr.  OF.  reboter',  see rebut.  For  the  subst.  use  of  infinitives  in  law terms  cp.  attainder  and  words  there  referred to.
32214:Derivatives:  rejoice-ful,  adj.,  rejoice-ment,  n., rejoic-er,  n.,  rejoic-ing,  verbal  n.  and  pres.  part, rejoin,  tr.  and  intr.  v.,  to  join  again ;  to  answer.  — ME.  rejoinen,  ‘to  answer  to  a  legal  charge’,  fr. OF.  (=  F.)  rejoin-,  stem  of  rejoindre,  ‘to  join again,  reunite’,  fr.  re-  (see  re-)  and  joindre,  ‘to join’.  See  join.
32216:rejoinder,  n.,  1)  the  defendant’s  answer  to  the  rep¬ lication  ;  2)  an  answer  to  a  reply,  answer,  reply. —  ME.  rejoiner,  fr.  OF.  (=  F.)  rejoindre,  ‘to join  again,  reunite’,  inf.  used  as  a  noun.  See rejoin.  For  the  subst.  use  of  infinitives  in  law terms  see  attainder  and  cp.  joinder. rejuvenate,  tr.  v.,  to  make  young  again;  intr.  v., to  become  young  „gain.  —  Formed  fr.  re-,  L. juvenis,  ‘young’  (see  juvenile),  and  verbal  suflT. -ate.
32384:Derivatives:  replenish-er,  n.,  replenish-ment,  n. replete,  adj.,  filled,  stuffed.  —  ME.  repleet,  fr. MF.  (=  F.)  replet,  fr.  L.  repletus,  pp.  of  replere, ‘to  fill  again’,  fr.  re-  and  plenus,  ‘full’.  See  full, adj.,  and  cp.  replum,  complete,  deplete, repletion,  n.,  surfeit;  fullness.  —  ME.  replecioun, ‘surfeit’,  fr.  OF.  (=  F.)  riplition,  of  s.m.,  fr.  Late L.  repletionem,  acc.  of  repletio,  ‘a  filling  up’,  fr. repletus,  pp.  of  replere.  See  prec.  word  and  -ion. replevin,  n.,  recovery  of  goods  wrongfully  taken {law).  —  AF.  replevin,  replevine,  fr.  replevir,  ‘to to  plege,  protect,  warrant’.  See  next  word, replevy,  tr.  v.,  to  recover  by  replevin;  intr.  v.,  to recover  goods  by  replevin  {law).  —  AF.  replevir, fr.  OF.,  ‘to  protect,  warrant’,  fr.  re-  (see  re-) and  plevir,  ‘to  warrant,  pledge’,  which  is  rel. to  plege,,  ‘pledge’.  See  pledge,  n. replica,  n.,  facsimile,  copy.  —  It.,  fr.  replicare,  ‘to duplicate’,  fr.  L.  replicare.  See  next  word, replicate,  tr.  v.,  to  answer  to,  reply.  —  Late  L. replicatus,  pp.  of  replicare,  ‘to  repeat,  reply’.  See reply.
32534:respond,  intr.  v.  —  MF.  respondre  (F.  repondre), fr.  VL.  respondere  (3rd  conjugation),  corre¬ sponding  to  L.  respondere  (2nd  conjugation),  ‘to promise  in  return,  offer  or  present  in  return;  to answer,  reply’,  fr.  re-  and  spondere,  ‘to  promise’ ; see  sponsion  and  cp.  correspond.  Cp.  also  riposte. For  a  similar  change  of  conjugation  cp.  summon. Derivatives:  respond,  n.,  respondence  (q.v.),  res¬ pondent  (q.v.),  respond-er,  n.
```


## [2026-09-07T20:16:42.806Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf (formfeed) index for lines\ndef leafof(lineno):\n    txt='\\n'.join(lines[:lineno])\n    return txt.count('\\f')\nfor ln in (1190,23474,23949):\n    print(ln, 'leaf', leafof(ln))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('---SYN', d['SYN']['page_offset'])\nprint('---KNT', d['KNT']['page_offset'], d['KNT'].get('lookup_hint'))\nprint('---HRN', d['HRN']['page_offset'])\nprint('---UNV', d['UNV']['page_offset'], d['UNV'].get('lookup_hint'))\nprint('---BQT', d['BQT']['page_offset'])\n\""
}
```


### [2026-09-07T20:16:44.235Z] TOOL RESULT

```
1190 leaf 14
23474 leaf 517
23949 leaf 527
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
---HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---UNV leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Pagination of the 1963 edition differs; use the glossary (Pahlavi words in transliteration) to verify substance.
---BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-07T20:16:50.372Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (515,516,517,518,527,528):\n    L=leaves[i]\n    print('=== leaf',i, repr(L[:120]))\n    print('   tail', repr(L[-120:]))\nEOF"
}
```


### [2026-09-07T20:16:51.686Z] TOOL RESULT

```
=== leaf 515 'elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  report’,  fr.  OHG. meldon,  of  s.m.,  which  is  rel.  to  O'
   tail 'iece,  bit’,  and  prob.  also  with Gk.  pTjviyl;  (for  *memsninx,  *mesninx),  ‘mem¬ brane’.  Cp.  membrane,  dismemb'
=== leaf 516 'er,  meninx. Derivatives:  member-ed,  adj.,  member-less,  adj., member-ship,  n.\nmembranaceous,  adj.,  membranous.  —'
   tail 'ool.)  —  ModL.,  compounded  of meno-,  ‘remaining’,  and  ppay/ia  (pi.)  ‘gills’. See  branchia.\nmenology,  n.,  a  c'
=== leaf 517 'alendar  of  the  months.  —  ModL. menologium,  fr.  Late  Gk.  pirjvoXoytov,  which  is compounded  of  Gk.  pvjv,  ge'
   tail 'ME.  marchaundise,  fr.  OF. marcheandise  (F.  marchandise),  fr.  OF.  mar- cheant,  ‘merchant’.  See  next  word  and'
=== leaf 518 '  subst. suff.  -ise.\nDerivative:  merchandise,  intr.  and  tr.  v. merchant,  n.  —  ME.,  fr.  OF.  marcheant  (later'
   tail 'i¬ bly  rel.  to  (a)pr)piv&os,  ‘thread’, mero-,  before  a  vowel  mer-,  combining  form meaning ‘part;  partial’.  �'
=== leaf 527 'ter,  Swed.  mjelte,  ‘spleen’, Norw.  mjelte,  ‘spleen;  milt  of  fish’,  OFris.  milte, ‘spleen’,  MDu.  milte,  Du. '
   tail 'gether’,  which  corresponds  to  I.-E. base  *menq-,  ‘to  knead,  mix’,  whence  OL  mu- cate,  mahcate,  ‘crushes’,  '
=== leaf 528 'OSlav.  mgknqti,  ‘to  be¬ come  soft’,  mgkdkii,  ‘soft’,  mqka,  ‘meal,  flour’, Lith.  minkau,  minkyti,  ‘to  knead’'
   tail ' minuere,  ‘to  make  smaller’.  See  minute,  n. minus,  prep.  —  L.,  neut.  of  minor,  ‘smaller,  less’. See  minor'
```


## [2026-09-07T20:17:00.348Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nyaka\\|niyaka\\|ny.ka\\|apanyaka\\|apa-nyaka\" KNT.txt | head -30; echo \"=== TLM\"; grep -n -i \"nyaka\\|apanyaka\" TLM.txt | head -20; echo \"=== BRT\"; grep -n -i \"nyaka\\|ny.k\" BRT.txt | head -20"
}
```


### [2026-09-07T20:17:00.431Z] TOOL RESULT

```
4270:47 : hacá : avadaga : abariya,: martiyà : karnuvakà : t 48 уату : afagam : akunavatà : avaiy : Yaund : uta 49 : Spardiyá : martiya : dàáraniyakará : tyaiy : daran 50 yam : akunavasa : avaiy : Mada : uta : Mudray
5277:kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
5523:déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.195-6).
5611:niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
=== TLM
914:hya  XShya  pu0ra  Xsayarcahya  Dara-3)yavausahya  XShya  pu0ra Darayavausahya  Vistaspahya  pu0ra  Haxamanfijsiya1  imam  apa- dana  Darayavaus  apanyakama  ak-4)unas  ab(i)ypara  [u]pa  Arta- [xsafl'am  nyajkam2  +   +   +   +   [An(a)]h(i)ta[hya  u]ta  [M‘]0ra[hya] +   +   +   +   da  +   +   +   m   +   a   +   +   +   AURAMAZDA  A-5)n(a)h(i)ta  ut[a M’]0ra  +   +   +   +   +   +   +   +
1114:apanyaka,  m.  ancestor.  Norm  sg.  apanyaka  (with  eucl.  ma,  abl. or  =   maiy;  cf.  Fov,  KZ,  35,  59),  Art.  Sus.  a.  imam  apadana  dar- ayavaus  apanyakama  akunas.  apa  (q.  V.)  +   nyaka  (Phi.  nyak).
1302:though  the  objections  to  assuming  ma  =   maiy  cannot  be  denied; cf.  apanyakama,  Art.  Sus.  a.  The  Elam,  version  shows  no  pro- noun here.  Instr.  pi.  kamnaibis.  YAv.  kamna  (New  Pers.  kam).
1562:nyaka,  m.  grandfather ,   supplied  in  Art.  Sus.  a.  arta[xsa0ram nyakamj,  Artaxerxes  my  grandfather.  YAv.  nyaka.
=== BRT
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3534:"n^  darayJ^vJ'ul  apanyäkJ'mt^  akuna/" Am./";  4'>.
3565:•  p.  apa-nyäka-  m.  'Vorfahr  des  Gross- vaters, Urältervatcr' :  därayi^ve^ui  'kJ'- «a*  "Darius  mein  Urältervater"  Am.  /.
3665:—  y!^  anyake  nairika  . .  yS  anyahe  *°ha (IS.)^  ..  a'^aurutum  *pararikacaiii  (sd.) N.  7;  77;  —  yat  he  aoxte  aisa  yeiihe  'ks hacatsuha  ms  *ana  "ka  (VS.)  N.5;  7,  *y, *io,  10 ;  —  'ktm  iiahmB.kßrpl)m  *syaokn3m.- v>r}Nm  (sd.)  V.7J.23;  ¥.2^.27.
4674:mit  vorausg.  ta-  dnw.  I;'  mä^a  .  .  tqm zqm  k3ray)n  .  .  vasff  .  .  tqm  'nyam  zqm k3ray>n  V.  ö.  a ;  —  yat  . .  bavül  paseaita ava  ta  'nya  maya  ifi/i  (sd.)  jasBiJ  V.5. 31.  d)  Sing,  mit  \oia.usg.  /tiseag/a  'der nächstfolgende':     asnyeke    (sd.)    pascauta
4678:maca  *frast3niite  .  .  ditSi  °iiye  (NPm.)  .  .  'nyeke  räkWB  V.  7.4.  I  i)  wiederholt *vaäsäz*/ramravainti..vTspa^qmia  aiwi.'  'Aex  eine  .  .  der  andere';  dsityB  *'inyS'^ srurwai/i  (sd.)  K.60;  —  aivB  pants  yB  havam  {^d^  *daityö  ^'inyB^  ya'ia  *va  . . a^ahe  vTspe  'nyalhm  apatitqm  {%A.)  \.y2.  li.107;  P.57;  —  yal  he  pukra  us^zaydi^e 11;  —  ^pasävi^  adam  käram  ..fraisayam  , .  .  tiaisB  'nys  .  .  aat  'iiyB  ,  .  Y.5. 10;  — hyt^  upa  mäm  äkJ* , .  hyJ^  °niyJ'  kärJ'  avi  *'iiy3^^  suruiiraiti  (statt  Du.)  nsil  'inyS ".  .  reliquus  exercitus  . ."  Bh.^.6;  —  eä  'S. 24;  — yay^  osH  'nyS  rasnus  razUtB asti  masyB  ..  an^rn  datpm  ..upairi'tiyai^'W.J^.^'PüZ.  (unvollst  Zitat);  — \,°myam sraväis  .  .  !  .  .  ya'^a  zrayB  vountJtahm '  (näml,  käram)  *ustrabilrim  akunavam upairi  °nyh  äpB  V. §.32{.;  —  vayaol . .  'myahyJ  aspilf^A^ paiiyariayatn^'Acnem^a taratatB  (Stverz.)  'tiysis  (als  APn.)  dämqtt  \  Teil  (des  Heers)  machte  ich  kamelberit- Y.22. 24;usw.; —  \' a^urcrmazdämaiy  upas-  ten  .  ."  Bh.7. 18'';  5. 4;  —  armaeflä  'iiyA
4681:Abi.  des  Verglichenen:  dahyunqm  yh  'nyi räjöii  Y, tr),iZ;  — yastä  daeiJSng ..  masyqsls tarS.mqstä  °nyiiig  ahmätyS  hBt  arBm(sd.)  .. ". .  die  andern  (alle)  ausser  dem,  der  .  ." Y.45. II.  II)  'ein  anderer,  alius':  yB .  .  'inyeke  v3  srSvayantB  paitUtanH  (sd.) 'f^B  vä  hl  dakmB  srttta  (sd.)  gS^S  daoäiti N. 25;  61,  V. J.9  PUZ.J  —yB  ..  *'imm*^
8478:—  mä  .  .  kaine  .  .  tarS  daxslim  pärayat (sd.)  tarö  ap?mca  (sd.)  'ramea  V./5.9; 10;  —  avi  tu  dim  disyata  (sd)  yä  apasca 'r-hca  zao>nhca  Y. A3,  a)  Du.  in Verbindung  mit  sp-  Du.;  yat  iurmaot a»haosimne  äpa  (Sh-erz.)  °vaire  Y.  9.  4; usw.  2)  mit  einer  einschränkenden Bestimmung :  aisma  .  .  yat  vä  aitaaham  . . 'ranam  yat  ätn.ciiranam  V.  ^75;  — altayh  °raya  aian^ar?}  V . S.-j ^-y  —  upa .  .  nmärum  baoiayaH  un-äsnayä  fä  .  . kamcit  v<l  hubaoi'At^manqm  °ranam  \.S. 2 ;  —  aoa  az»m  yS  ahurö  masda  °rä  bal- iasy'i  uzbamn  ".  .  die  Heilkräuter  . ."  V. JO.4;  —  ynän^m  vä  .  .  kamcit  vä  vlta- afianam(sd.)°ranainY.ij.i4; — yavanqmca vtlstranqm^a  'ranqm'a  :far?i5.bairyartqm (sd.)V.J.4;  —  'raaqm  s^awrlranqi'i  (sä.) Yt/>5S;  Vr.2/.i;  —  'rShu  paiti  barss- manyäku  Y.  2.11,  "Y't /0.14s;  —  imqmcä 'rqm  bansmanim  Y.  22.3,  a)  durch Namensnennung:  aetayh  *rayh  ya  i-aoÜ ha'jana^aia  V.  14.  4;  V.J.  3,  22.  i,  62.  9
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
19347:*)  Die  einerseits  mit  Bmjya  anderseits  mit Uiahina  in  Beziehung  gebracht  wird. Ableit.  —  Ableit.  aus  »mäita-.  —  Pü.  (zu  Y. 79) :  mänpai,  (za  A) :  mänyak,  erl. :  martum  i andar  s^Bkärm  dättnear;  vgl.  dazu  DsT.  ZA. /.  30-
19349:Ableit.  (mit  Verschiebung  des  Woitakzents) aus  'nmänya-  A.  —  Pü.:  mänyak.
19354:•  j.,  p.**  nyäka-  m.;  nyäkä-  f.  'Gross- vater, Grossmutter':  yal  'kB  para.iri%yeiti •ke  (NSf.)  Vä  .  .  cvai  alsqm  upa.mqnayjn naps  hala  °k3'^  napti  kaca  'ke'^  V.  72. 9; 11;  — iartax/a^''ä  'ka^mi^'^  "A.,  mein Grossvater"  Am.  I.
19888:nüiiya  (sd.)  xinstjm  Y.31. 3";  —  ts  (näml. s^ä^rä)  matdä  'inya  uxlyS  (sd.)  yl  ä nürSm^  . .  hämS  Y.31.  7'';  —  ahyä  *°in- ySuS  tvSm  ahl  tä  (Sp.  905  m.)  sf>nt^  ys ahmäi  gqm  .  .  hJmJa/at  Y.47.  3;  —  at tBi  mazds  tPm  'inysm  asaox^ayantyä  *ta- r^idyayä  (sd.)  .  .  Y.  J5.9;  —  äw?  ä  giul tala  (sd.)  as  *xratui  °inySus  masda  ahurä Y.31. 9  '^.  b)  der  Geist  des  Bösen  heisst angra-,  aka-  oder  dngvant-'.  mainya  (Sp. 1125  m.)  . .  yayä  spanyä  Biff  mravai  y^'" angr»m  Y.  45-  2 ;  —  hyat  vä  aka  manatahä ying  äafvSng  akascä  °inyul .  .  Jyaeharum fraSnas  ..  */«>■;»  (sd.)  Y.^2.s«;  — aya  *Mainivä(Sp.ii25m.)z'aratä y? drugvä acists  vfntys  Y.30.%.  b)  im  jAw.: ihä  'inyB  mamanaiti . .  vaoiatar!  . .  z/3- v>r>zätarS  Y.  ij.  4;  —  paslaäa  .  .  yat 'inyB  dSmqn  daSiltgin  Y.57. 17;  Yt.  TJ.yß ^'inyu);  —  yüthistB  'iniv&  damqn  V.  ig. 42;  Y.ip.is,  Yt.  13.  T  6  {'nivä);'^  ya%a apimim  'nivä  anhat  nivaiti/  Y.  10. 16; '9-9'>  —  "^'i  ■  •  ^hmi  paiti  nairi  dva *'inyu  rSnaisA.)  ava.stsvhat  ■V.7.52;  — rar  antarp  eam  asmammca  druja  (Sp.  781 m.)  °nivä  vaonyät  Yt.i3.iy,\^.  a)der Geist  des  Guten*'  heisst  spmta-,  spanyak-x ..yatmainyB  dqman  daCoTtfm yasia  spmtd 'inyul  yasca  attrö  Y.J7.r7;  Ytjy.76, 75.43,  Vyt.  47;  —  dqma  .  .  yi  hinti spfntahe  'inySus  Yttf.i;  Y.j.16,  Ä  6, 27.2,  Vr,/2.4,  Yt.Ä48,  70.142,  i^.^, V.5.33.  yi.  aS,  Vyt,5/;  —  yat  sp^ntS 'inyus  vitärayal  asmamm  Yt.  ij,  a8;  39, V./p.  9;  —  yS  dc&vä  Spante  »inyui  Yt 10.  r43;  —  avanayeni  spantim  'inyBm hala  . .  garS  nmSna  uspatayeni  anram 'inyBm  .  ,  haea  duiaaha;  tl  ml  vaifm 'kanjaysnte  spmtatla  'inyus  araras&i  Yt. ig,  44;    —    sfaranS  yahmi  paiti  "para-
22106:mit  aibT,  aiwi  i)  'hinschauen,  hinblicken auf  — '  (Akk.):  matshim  paiti.vaen3m  .  . I  m3t3h>m  aiwi.valfum  Ytj.j;  —  amtsanam .  .  yalsqm  atnyS  ainyeke  urvSngm  aiwi.- I  vamaiH  Yl  13. 84;  —  {yat  his)  spa  vS I  aiwi.valnaiti  frä  va  ^araiti  "(wenn  auf '  sie,  die  Leichname)  ein  Hund  hinsieht I  oder  sie  anfrisst"  FrW.  7/'';  —  yeä  »Sil I  näirika  Stnm  aiwi.vainitt  "sonst  könnte j  die  (menstruireode)  Frau  ins  Feuer  blicken" .W.  16.  2^';  —  yim  aiwi.*vainat  Vyt 1  10.  2)   'gewahr  werden':   kakrkäsB  .  .
23013:viratyst  YL  75.  40;  — -  pu^nm  anyakmat arsänai  varst?m  YL77.S8.  3)  'Jeman- dem (Dat)  etwas  erwirken,  durch  seme Tätigkeit  verschaffen';  tai  tts  nülXi  van^äni "ihn  (den  Anteil)  will  ich  jetzt  uns  ver- schaffen" Y.  57,  i">.  Undeutlich:  ya nairika  nmanspaiti  v>r>tyanti  N.  6;  — nSii  hi  alt  *^adinanqm  vfr»tySit  N.  16.
26986:KoDipA-i  Ableit  —  VgL  tpanyak;  sfiSniila-; ferne»  sfiSnai-'i>.  —  ksl.  svf/ü,  |[l.  in/tfilas 'heilig';  np.  vgl.  aspand  'Rtute'  (wozu  Hbu. AGr.  /.  Vji).  —  Pü.:  irmsümk,  Sü.:  mahalla- rai ,  mahallamah ,  gumlarak ,  auch  makän, ti^däkiki  s.  noch  No.  1-5,  S,  la  —  ')  Pü.: atozünlk  bavandak  mcniln  oder  spandaramal. —  i>  PQ.  I  sfieiiäk  (Sü. :  ma/iallarak)  meniiJi.  — 3)  Pü. :  ta  fa  ahräilh  awiäyenet  (Sä. :  fta- vardhayati).  —  4)  Pü.:  pa  an  i  ei  ewiäye- mtär  [Sä.:  firoT/arMayiat^)  marl,  —  S  PB,; pa  ,.  ojosäyFnÜH,  SQ.:  /j-tiiilatayä,  —  *)  Hds. ärPiaUilea  spiilasia.  —  7)  Hds.  spmlahcca ärmalSis.  —  *•)  Pu.i  amahraspand,  —  W  Hds. 'Om;  %,  vor-  nnd  nachher.  —  "*)  Pü.: mänsr  spand.  —  ")  Hds.  "/i.  —  ")  S.  S^'fl!/- No.  8.  —  '3)  Hds.  gaospinla.  —  'S  Die  Wörter setzen  eine  Basis  auf  (ar.)  -an  voraus.  Dass Gdn.  VSt.  3.  33,  SPreussAW.  ig.  433  und JN.  GlrPh.  3.  633  wegen  Pü.  aiiaiitiTi  sich neuestens  wieder  '.  dam  verstehen  konnten, ipjHia-  von  lit.  saifiUas,  ksl.  svftä  losiu- reissen,  ist  mir  nicht  begreiflich.  Wenn  dem awest.  spinia-  eine  andre  Bedeutung  als  'heilig' inkommen  sollte,  so  mijssie  es  eine  Bedeu- lungsverschiebung  oder  eine  Umdeutung  er- fahren haben;s.dazuBB. /;.6i,  IF.J.161N0.3. Das  ist  aber  nicht  der  Fall.  Ohne  die  Über- setzung annünii  würde  Niemand  auf  den  Ge- danken kommen,  spinta-  anders  als  mit  'heilig' wiederzugeben,  das  überall  vorzüglich  passt; sie  ist  wohl  insbesondere  durch  V.  51.  zi veranlasst  worden,  wo  wir  es  vielleicht  mit einem  Wortspiel  zu  tun  haben.  Die  Annahme, das  Wort  spjnta-  bedeute  eig.  'vorteil-,  gewinn-, heilbringend'  (Jn.  GlrPh.  2.  Ö35)  nimmt  doch auch  auf  dessen  Bildung  nicht  die  genügende Rücksicht.  Dass  awzünii,  np.  afsüdan  etymo- logisch mit  den  awestischen  Wörtern  nichts  zu schalTen  hat,  steht  fest,  trotz  Cdn.s  gegen- teiliger Meinung;  5.  sav-  No.  3. j.  spittlama  P.  44:  lies  spilama. •  j.  8pfliita.mamyav-  fem.  Adj.  'die Worte  sptntä  mainya  enthaltend,  damit  be- ginnend'; yufAäitisisd.y  Y.^jÜberschr.;
27317:—  iitum  tl  nanm  nisrinaomi  impm  ml narsm  nisrärayä^  upa  iürqm  fra^.- kfrftim  "diesen  Mann  überantworte  ich dir,  diesen  Mann  sollst  du  mir  (wieder) ausantworten  bei . ."  V.  18.  51.  3)  'aus- teilen, (Schläge)  versetzen':  balvan  ymqnä nisirinaoiti  Vt  10. 27.  4)  0  '(wieder)  in Stand  setzen,  einrichten':  ayadand  tyä gaumäta^  hy<^  magus  inyakcf  adam  niya- ^'ärayam  "die  Kultusstätten,  die  G.  . . zerstört  hatte,  setzte  ich  wieder  in  Stand" Bh./.  i4'>.
```


## [2026-09-07T20:17:01.319Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 238 area\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (258,259,260):\n    print('=== leaf',i)\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-07T20:17:02.662Z] TOOL RESULT

```
=== HRN 238 area
412
=== leaf 258
— 237 —
*m + V^göp- "behüten, verwahren*, vergl. ai. X^göp- ;
plilv. n(i)huflan 'verbergen*.
kurd. nixiftifi *sich verbergen*, nix^ftin Causat.
^verbergen.
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.
=== leaf 259
— 288 —
1062. niyä 'Grossvater, Ahne (Plur. myagän),
ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
Ahne'; phlv. nyok.
af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
(250).
1063. niymn 'Scheide*.
ap. *nigama', vergl. skr. w^ + l^f/am-, mgamd-
'Einfügung (aber nur als ritueller t. t.), vorgl. np.
peyam (de Lagarde, Ges. Abb. 79).
Unsicher ^).
1064. nirö {*n^rö) 'Kraft, Macht'.
aw, '^nairyava- 'Mannhaftigkeit', vergl. nrnrya-
mannhaft'; ai. ndrya-; phlv. nerök,
1065. ni» auch', hemz (Sahn. I, 167 Vers 691), ?:x (Is.
1, 15).
ap. *anyadadi^) 'irgend wie anders' (Säle mann,
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.
=== leaf 260
- 239 —
ap. fiaiha- \schön, gut* ; phlv. neicah, nSwakih, new
(PPÖl.) 0.
1069. nem 'Hälfte, halb*.
aw. naema- *halb* in naemo asm, na^me /saf^ti,
vd. 4, 45, Geld n er, Studien I, 100 [na^mqm im
ZPGl. bedeutet nicht *halb*); skr. nvma- halb*; phlv.
mm, nSmak.
kurd. nTw *Hälfte, vergl. nlwrfiz 'Mittag*; afy. mmai;
bei. vergl. nl^röt^, nSnnöc, n. nermös 'Mittag', mmsap,
n. nSmSaf 'Mitternacht* (269) ; sar. L W. naim.
Vergl. D''i13X (Talmud) 'halb (sc. gar), nur zur
Hälfte (sc. gebraten)*, de Lagarde, Semitica I, 39.
1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
aw. *n? — \/gaos-, vergl. apa gaosay^iti; phlv.
n(i)yösJtany n(i)yö/sltan bezw. n(i)gösltan'') 'hören'; ai.
[/"ghöS'^ ghösati mit d 'hören, horchen auf.
bei. mgösag, niyösay (262).
>) Vergl. Fr. Müller, WZKM. 5, 265.
Die jüngere phlv. Form tiek liest Justi fZDMG. 46, 288) zwoi
Mal auf Gemmen (die letztere derselben, JRAS. XIII No. 45, die ich
ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
ZDMG. 11, 320 als semitisch (!) entziffert, worauf mich Herr Cler-
mont-Ganneau aufmerksam macht).
*) de Lagarde^s CBeitr. zur altb. Lex. 76) von Darmesteter
f6t. ir. I, 85 Note 2) wiederholte Erklärung aus aw. yao^nti' ist ver-
fehlt ; phlv. ftffJyö/Sitan^ das auch gelegentlich n(i)ybHltan geschrieben
sein kann (aber wo?), beruht auf einer im Pchlevl häufigen graphischen
Eigentümlichkeit.
Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
l/kar8', kasiian u. s. w.), vergl. auch bereits aw. pä^no" gegen ai.
pärsni: Der Übergang von rs in /S ist dem gegenüber nur ein schein-
barer in äia^s aus ätars und Syäva^^ aus Si/ävarsati-; )^h soll hier bloss
eine scharfe oder wahrscheinlich etwas modificirte Aussprache des s
bezeichnen, wie sie in ^^ar^set (vergl. Hörn, Mitteiluiigen, Heft IV,
S. 34) berechtigt war. Diese Aussprache wurde dann weiter über-
tragen, z. B. phlv. Zartux^t (aw. Zara^usfra-), daraus Zerduhest etc. des
SähnSme, vielleicht kÜ^sUan (ältere Form nicht vorhanden), nCOyöxsitun
oder wohl nCi)yöxSUany vergl. nCOyo^s, wie nach MuqaddasI 418, 5 (Nöl-
d e k e ^ s Correktur nach mündlicher Mitteilung) die Bewohner Xüzistän^s
für *höre* sagten. Siehe auch Hörn, KZ. 82, 585 Xo. 18 und vorgl.
unter np. feyfere (No. 806).
```


## [2026-09-07T20:17:17.910Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nfor n in (5611,5523):\n    print(n,'leaf',leafof(n))\nleaves=t.split('\\f')\n# print leaves around\nfor i in (leafof(5611),):\n    print(leaves[i][:300])\nEOF\necho \"=== apa-niyaka in KNT\"\ngrep -n \"apaniy\\|apa-niy\" KNT.txt | head"
}
```


### [2026-09-07T20:17:19.168Z] TOOL RESULT

```
5611 leaf 217
5523 leaf 213
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. n
=== apa-niyaka in KNT
1802:III. Of somewhat uncertain analysis: niyàka-, apa-niyüka-, mari-ka- (see Lex. s.vv.).
5611:niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
```


## [2026-09-07T20:17:19.916Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nyak\\|niyak\" UNV.txt | head -20; echo \"=== PHD\"; grep -n -i \"niyag\\|nyak\\|niyāg\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n -i \"niyak\\|nyak\\|niyāk\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:17:19.995Z] TOOL RESULT

```
=== PHD
PHD.txt:397:hó 44. huniyagih
PHD.txt:785:ancestor niyāg.
PHD.txt:1546:delight huniyāgīh, urwahm(an)ih.
PHD.txt:1547:delightful huniyag.
PHD.txt:1776:entertainer huniyāgar.
PHD.txt:1777:entertainment huniyāgih.
PHD.txt:2135:grandfather niyag.
PHD.txt:5304:niyāg, wahāg
PHD_mackenzie.txt:2905:hi)                                44                       huniyagih
PHD_mackenzie.txt:2960:huniyag [hllmyd)k l , N xun)O(l] delightful.
PHD_mackenzie.txt:3810:niyag [nyd)k' i M ny)g, N niya] grandfather, ancestor.
PHD_mackenzie.txt:6474:easy asan, sabuk, xwar.                      entertainer huniyagar.
PHD_mackenzie.txt:6475:eat xwardan; cause to ,....., xwaren-.       entertainment huniyagih.
PHD_mackenzie.txt:6689:geometry zamig-paymanih.                      grandfather niyag.
PHD_mackenzie.txt:7109:Mithra Mihr.                                   musician huniyagar.
PHD_mackenzie.txt:10417:kirih-I                :.. ""'U \ to' \            niyag, wahiig                 \.t-'\.)'\
PHD_mackenzie.txt:12017:huniyagih                ~yd\'"                hangirdcn-                -~~t'"
PHD_mackenzie.txt:12018:huniyag                     \~\t"              hangirdcnidan           "~"'~t"'
PHD_mackenzie.txt:12019:huniyagar                  \.Y'U',....         hangirdigih             "U ~~.. t»
=== NYB
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
2682:névák [ndwk'] good in a general sense; beautiful, nice; favorable, comp. ~-tar 604; adv. well 220, 713. 7619; as an attr. commonly placed after its headw., but m jäyisn 1214 as against jāytšn + ~ 181, yatak i ~ 1133; — placed before its head w., with the ending -é or -en : —-ē āvām the favorable time 55%; ~-én kunišn good deeds 7227, v.s. v. ménói. — Ps. nywk- ; Paz. nek, nyak; NP nék.
6764:nyak: névak nyoxšidan: niyösitan
```


## [2026-09-07T20:17:25.783Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^apa\\|^apa-\" KNT.txt | head -20; echo \"---\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nimport re\nfor i in (178,180,182,217,218):\n    L=leaves[i]\n    print('=== leaf',i,'|', L[:150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:17:27.083Z] TOOL RESULT

```
2255:apa-. A
4994:apa- prefix (§206b) ‘away’: Av. Skt. apa, Gk.
4996:apataram adv. ‘farther off, far off’; nsn. of
4997:apatara-, which is apa- + comp. -fara- ($82,
4999:apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
5000:apantyüka- sb. ‘great-great-grandfather’: from apa- + niyäka- ‘grandfather’, cf. Lt. ab-avos
5003:apara- adj. "later, after’: Av. Skt. apara-, from apa- + comp. -ra- ($32, 419.11). арата пет, XPh 47. aparam asn. as adv. DB 4.37, 42, 48, 68, 70, 87; DSt 10° (not apara-ma, nsm. with enel. abl., DB 4.37, 68, 87—and DSt 10°—as Bthl. AiW 77 suggests, following АКК. $a be-la-a ar-kt-a ‘who shall rule after me’).
5004:apan*ydka-ma — (822,
---
nleaves 232
=== leaf 178 |  : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginnin
=== leaf 180 | d: LX (units) in weight. ‚.. (= Wb ЕЎ).- 157 INSCRIPTIONS ON SEALS SDa = Darius, SEAL A: adam : Darayavaus XS SDb = Darius, SEAL B: adam : Dàrayavaus 
=== leaf 182 | he field of historical romance. See also PW 3A.710-2, s.v. Smerdis. III. Tae HELPERS or DARIUS The names of the six Persian noblemen who co- operated 
=== leaf 217 | n üv-nara- (§142). nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm.
=== leaf 218 | with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and S
```


## [2026-09-07T20:17:32.540Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nprint('apaniyaka line 5000 leaf', leafof(5000))\nleaves=t.split('\\f')\nimport re\nfor i in range(185,232):\n    L=leaves[i]\n    m=re.findall(r'\\b(1[6-9]\\d|2[01]\\d)\\b', L[:400])\n    print(i, m[:6], '|', L[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:17:33.819Z] TOOL RESULT

```
apaniyaka line 5000 leaf 190
185 [] | ugh not mentioned in the Behistan inscription, must have fol
186 ['204'] | � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; 
187 [] | t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta
188 ['191'] | ’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadt
189 [] | n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-
190 [] | . Skt. apa, Gk. and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, 
191 [] |  formed like Gk. &exero to root *segh-, ёттєтө to root *pet-
192 ['189'] | -, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *a
193 [] | t’). - LEXICON ч. Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerx
194 [] | пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (
195 [] | 's avabäštā adj. apm. 'thus standing". avadà (ie. avadá) adv
196 [] | 3. asmanam (853) A?Pa 3. ašnaiy adv. ‘near’, lsn. of ašna- ‘
197 [] | �; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 
198 [] | DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43
199 [] |  by Hz, ApI 71-2). ufraSa- ufrasta- adj. ‘well punished": u-
200 [] | B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vri
201 [] | to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54
202 ['218', '219'] | om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2). акша aor. mi
203 [] | ted by the OP writing. регу. of Iran. root *kas- (89.V, §87,
204 ['181'] | , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, 181 28, 29, 
205 [] |  sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97,
206 [] | n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (con
207 ['163'] | 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&
208 ['215'] |  Skt. jū- ‘press for- ward, impel quickly, excite, promote’,
209 [] | it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 
210 [] | 1) XPh 23. tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) Am
211 ['188'] |  word of uncertain meaning, Sb 3. Sanuvaniya- sb. ‘bowman’: 
212 ['209', '218'] | fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wa
213 ['162'] | 5-6). Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 52
214 ['166'] | Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. Daha- adj. ‘
215 [] | rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far a
216 ['207', '191'] | e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as g
217 [] | n üv-nara- (§142). nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt.
218 ['166'] | with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing
219 ['167', '178'] | ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- 
220 [] | tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pf
221 ['186', '186', '166'] | r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 87
222 ['164', '162'] | -. — fra&aram asn. XPf 26f, 37. Fraéda- sb. ‘Frada’, a Margi
223 ['172'] | 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1
224 ['218'] | 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2
225 [] | BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; D
226 [] | 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе
227 ['203'] | ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80
228 [] | so a province of the Persian Empire, ‘Egypt’; тазе. sg. as s
229 ['196'] | d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220,
230 ['208'] | am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Tehera
231 ['210'] | 1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue,
```


## [2026-09-07T20:17:52.328Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN grandfather\"; grep -n -i \"grandfather\" SYN.txt | head -20; echo \"=== UNV\"; grep -n -i \"ny.k\\|niy\" UNV.txt | head -20"
}
```


### [2026-09-07T20:17:52.396Z] TOOL RESULT

```
=== SYN grandfather
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2505:Sp. nifio, nursery word belonging with A large group of affectionate terms for father, mother, grandfather’, ete. (be- mi p. 94). BEY 5817. Walde-P. 1.55.
2564:The principal groups of this kind may be cited here for future reference. In general, the forms characterized by a labial or dental stop are applied to male relatives ‘father’, ‘grandfather’, etc., and those with n or m to female rela- tives, ‘mother’, ‘grandmother’, ‘aunt’, ‘niece’, etc. But there are many ex- ceptions, as new forms for the opposite sex may arise from either type.
2566:Goth. aba ‘husband’, ON afi ‘srand- father, ete.’, Grk. rémzos ‘grandfather’. Slay. baba ‘grandmother, old woman’, whence Lith. boba ‘old woman’, and fr. this bobuté ‘grandmother’. Cf. also MHG bobe ‘old woman’, buobe ‘boy’, NE baby, etc.
2569:thetis ‘grandfather’), tévas, Lett. tévs, teta, Goth. atta, ON atte, OHG aitto, Alb. at, ChSI. ottct, etc., Hitt. attas, etc. Here also Slav. and Lith. teta ‘aunt’, etc.
2604:a close association between words for reciprocal relations, as between ‘grand- father’ and ‘grandson’ (NE grandson formed on the model of grandfather, etc.; OHG ano ‘grandfather’, but dim. enin- chil, NHG enkel ‘grandson’), or between ‘uncle’ and ‘nephew’ (OHG fetiro ‘uncle’, MHG vetere also ‘nephew’, NHG vetter now ‘cousin’).
2660:6. Goth. aba ‘husband’: ON afi ‘grandfather’, etc., orig. nursery word (above, p. 94). Walde-P. 1.47.
2933:9.46 GRANDFATHER
2937:foe hatnp) G ramos, TAT7TOUS yaya Ae avus avia It. nonno (avo, avolo) nonna Fr. grand-pere (aieul) grand’mére (aieule) Sp. abuelo > abuela : Rum. atid mare, bunic mama mare, bunica Ir. senathir senmathir ) Nir. seanathair seanmhathair W. taid nain Br. tadkoz mammgoz Goth. .....- J oe 2 aay: ON fodur-(mddur-)fadzr; afi fodur-(mddur-)moddir; amma Dan. _ bedstefar bedstemor Sw. farfar, morfar jfarmor, mormor OE ealdfader ealdmédor ME grauntstre, grandfather grandame, grandmother NE grandfather (grandsire) grandmother Du. grootvader grootmoeder OHG ano ana MHG ane ane NHG  grossvater grossmutter Lith. senelis (tévukas) bobuté, motiute Lett. vectévs vecmate ChSl. dédi baba SCr. djed baba, baka Boh. déd babitka Pol. dziad(ek) babka Russ. deduska babuska Skt. _ pita-(matd-)maha- pita-(mata-)mahi Av. nyaka- nyaka-
2945:2. Lat. avus, fem. avia, late ava: ON afi ‘grandfather’ (late), Goth. awa ‘grandmother’ etc. Hence, mostly in dim. forms, It. avo, avolo, Fr. aieul, aieule, Sp. abuelo, abuela, of which only the Spanish are now the usual words. Walde-P. 1.20. Ernout-M. 96f. REW 830, 839.
2956:4. Goth. awd ‘grandmother’, ON afi ‘grandfather’: Lat. avus, etc., above, 2.
2964:the partly anglicized grandfather, grand- mother. Cf. NED s.vv.
2967:5. Lith. senelis ‘grandfather’, fr. senas ‘old’, bobuté ‘grandmother’, dim. of boba ‘old woman’. Also tévukas dim. of tévas ‘father’, and mociuté dim. of moté ‘woman’, orig. ‘mother’.
2969:6. ChSl. dédi ‘grandfather’, etc., all the Slavic forms, pet name of the dada type (above, p. 94).
2971:7. Skt. pita@maha- ‘paternal grand- father’, cpd. with mah- ‘great’, but of unusual formation. Hence pitamahi- ‘paternal grandmother’, also matamaha- ‘maternal grandfather’, matamahi- ‘ma- ternal grandmother’. Delbriick, op. cit. 474,
2972:Av. nydka-, nyakd- ‘grandfather, grandmother’ (OPers. nydka- ‘grand- father’, apa-nydka- ‘ancestor’), etym.? Delbriick, op. cit. 474.
3025:NIr. garmhac ‘grandson’, fr. MIr, gormac ‘foster-son,’ epd. with prefix gor- (fr. Brittanic = Ir. for-: Grk. wrép, etc.), and mac ‘son’, as also in NIr. gar- athair ‘great grandfather’, etc. Hence also NIr. gairinghean ‘granddaughter’. Pedersen 1.23.
3029:NE grandson, granddaughter, formed after the opposites grandfather, grand- mother, as also grandniece after grand- aunt, etc., grand- being thus extended to denote corresponding relations of de- scent as well as ascent, as likewise great- in great-grandson after great-grandfather, etc.
3030:OHG eninchil, MHG enenkel, NHG enkel, dim. of OHG ano ‘grandfather’ (2.46). Hence new fem. enkelin. Walde-P. 1.55.
3040:grandfather etc.
=== UNV
151:man  he  dUtah :  niyösttan  framäyet  4.
155:tt  nämih  harne  räd  smäh  i  niyähän
191:.  estät  niyösit  zand  gyäh
817:.liuniycih  i  böö  ciyön  etön  böd  71.
```


## [2026-09-07T20:17:54.722Z] TOOL CALL #18: Bash

```json
{
 "command": "pdftoppm -f 371 -l 371 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371.png"
}
```


### [2026-09-07T20:17:56.577Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53926 Sep  7 16:17 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371.png
```


## [2026-09-07T20:18:05.985Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nfor n in (2933,2972,2945):\n    print(n,'leaf',leafof(n),'-> printed', leafof(n)-24)\nEOF\necho \"=== UNV grandfather/Ahn\"; grep -n -i \"grandfather\\|Grossvater\\|Ahn\\|ancestor\" UNV.txt | head -20; echo \"=== UNV size\"; wc -l UNV.txt; python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt',encoding='utf-8',errors='replace').read(); print('leaves',t.count(chr(12))+1)\""
}
```


### [2026-09-07T20:18:07.313Z] TOOL RESULT

```
2933 leaf 139 -> printed 115
2972 leaf 141 -> printed 117
2945 leaf 140 -> printed 116
=== UNV grandfather/Ahn
170:4.  Geruliet  zu  hören:  Die Familie,  der  ich  entstammt bin,  ist  immer,  dank  der  Gunst Gottes  und  eurer  Ahnen,  an¬ gesehen  und  wohlhabend  und unabhängig  gewesen ;
223:12.  Und  meine  Kunst  im Speerwerfen  ist  derart,  daß der'  Reiter  für  unglücklich gehalten  werden  muß,  der zu  Pferd  mit  Speer  und Schwert  zu  Kampf  und  Streit mit  mir  kommt ;  und  auf  der Rennbahn  bin  ich  des  Ball¬ spiels  wohl  kundig,  und  in kurzer  Zeit  steige  ich  auf die  Schultern  des  unterlie¬ genden  Gegners  ;  und  beim Werfen  der  Keule  treffe  ich so  unfehlbar"^,  als  wenn  sie das  Gesicht  eines  Sturmbocks
842:^  Eig.  'des  der  gute,  vornehme  Ahnen  hat’.
=== UNV size
1213 UNV.txt
leaves 48
```


## [2026-09-07T20:18:19.534Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('UNV.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nprint('line155 leaf', leafof(155), '-> printed', leafof(155)-2)\nprint(repr('\\n'.join(lines[148:175])))\nEOF"
}
```


## [2026-09-07T20:18:20.798Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (132,133,134,135,139):\n    print('=== leaf',i,'|',leaves[i][:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:18:20.971Z] TOOL RESULT

```
line155 leaf 15 -> printed 13
"3.  ^  Derselbe  Ausdruck  auch  in  §  20,  sowie  PahlT.  o£.  17  und  \\  rs.  6.\n13\nman  he  dUtah :  niyösttan  framäyet  4.\n[)]  ^)HXJ  [■’]  -H39e>>ey^  -^ey\n[u]  yazatän  [i]  äpäUh  hom  hüt  hacas\n)  2j-^)  ^ ■*\ntt  nämih  harne  räd  smäh  i  niyähän\no  ^  -^5  [»]\n.  hand  hüt  Mvim-häm  [n]  tuvängar\no  9e>‘»f^i2J  -»  m  j})^  )K)Oiy  o\n.  estät  x'^es  i  apäydst  pa  her  usän  5.\nfj)  •*ü-“^e>*  ))ö  ^  ^iy  1\nhe  apurnäyih  pa  i  pit  i  de  um  6.\n^  <!?npü  ^  ^\nhe  hom  hüt  pus  man  he  mät  u  vitart\n^  ^  Hy  -VHy\n.  hüt  ne  pus  an  emh  man\n-»  ))ö  [■»]  yHXjey  v\ni  stür  pa  man  [i]  hahrah  hacosän  7.\n5)r  yr  ^  >*üV  )  ^\ngönah-gmah  i  x'^arim  u  staivr  i  pärah  gnt .  hom  däst  neivah  cägmh  xüp  i  hraJim  u\n4.  Geruliet  zu  hören:  Die Familie,  der  ich  entstammt bin,  ist  immer,  dank  der  Gunst Gottes  und  eurer  Ahnen,  an¬ gesehen  und  wohlhabend  und unabhängig  gewesen ;\n5.  und  sie^  hatte  Vermö¬ gen,  entsprechend  ihren  Be¬ dürfnissen.\n6.  Und  mein  Vater,  der während  [meiner]  Kindheit . starb,  und  meine  Mutter,  de¬ ren  Sohn  ich  war,  hatten außer  ^  mir  keinen  anderen Sohn.\n7.  Von  ihnen  erhielt  ich als  mein  Erbteil  durch  den Sachwalter des  Vaters  statt¬ liches  Barvermögen  ^  und Nahrung  aller  Art  und  schö¬ nes,  feines,  gutes  Gewand.\n4.  ^  Hs8.  das  wäre  framayihet,  das  Passivuni;  aber  dann  verlangte\nman  den  Konjunktiv  90*°  'es  soll  geruht  werden\\  Sonst  steht  überall  s.  §  18,"
```


### [2026-09-07T20:18:22.322Z] TOOL RESULT

```
=== leaf 132 |  | Lat. coniugium, conutnin Dan. giftermaal, egte; bryl- Lett.  precéSands, lauliba; | tie ie ChSl. 6; rie 1 ) | : oe Sw. iftermdl, dkta; brél- .  brakit (maliizentstvo | een zoned, es SCr.  brak, Zen
=== leaf 133 | ri- monio), fr. mater ‘mother’, and orig. re- ferring to the woman’s lawful mother- hood, married status, as opposed to con- cubinage. Sp. boda(s), ‘wedding’, fr. Lat. vota ‘vows’. REW 9458. 2. Ir. la
=== leaf 134 | rati ‘take’, IE *bher- ‘bear’) , orig. ‘taking the bride’, like ‘lead the bride, marry’ in Lith. vestz, etc. Berneker 81. ChSI. malizZenisivo (late), Boh. man- Zelstvt, Pol. malzensivo : ChSl. maltize
=== leaf 135 |  Lett.  téus mate vecaki ChSl. _ otict mati rod ‘tela SCr. _otac mati roditeljt Boh. _ otec matka, mdtt rodite Pol. ojciec matka (maé) rodzice Russ. olec mat! roditelt Skt. —_ pitar- méatar- pitarau, 
=== leaf 139 | one for ‘own, full brother, sister’, more common than frater, soror in MLat. documents of Italy before a.p. 1000. Ernout-M. 417. Walde-H. 1.594. REW 3742. P. Ae- bischer, Z. rom. Ph. 57.211 f. 2.45. ‘
```


## [2026-09-07T20:18:34.210Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"نیاکان\\|نیاگان\" BQT_v4_pages.txt | head -20; echo \"=== pdf page 304 region\"; grep -n \"\\[pdf page 30[0-9]\\]\" BQT_v4_pages.txt | head"
}
```


### [2026-09-07T20:18:34.273Z] TOOL RESULT

```
1260:تولد بافته (بوستی . بندهش ص ۲۲۹) و هم نام چندتن از نیاکان منوچپر (ابضا مس ۲۳۹) است از
11034:برتخت زرین , وانوشه خور بجام جمشید ورسم نیاکان» در همت بلند ونیکوکاری و ورزش داد » و
12288:بممنی‌لیازمنداست که محتاج وحاجنمند باشد. نیاگان ۱ - باعاف فارسیبروزن‌بیابان,
=== pdf page 304 region
12044:[pdf page 300]
12078:[pdf page 301]
12126:[pdf page 302]
12171:[pdf page 303]
12204:[pdf page 304]
12243:[pdf page 305]
12282:[pdf page 306]
12320:[pdf page 307]
12367:[pdf page 308]
12405:[pdf page 309]
```


## [2026-09-07T20:18:37.536Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && sed -n '12204,12320p' BQT_v4_pages.txt"
}
```


### [2026-09-07T20:18:37.588Z] TOOL RESULT

```
[pdf page 304]
بیان بیست و چهارم
در نون با ای <طی مشتمل بریکصد و سیزده لغت و کنایت
نی ۱ - بفتح اول وسکون تالی, مشغفف نیا ۴ - بکر اول وئانی بال ف کشیده .
ای است که مزمار - وحلقوم باشد - وقلم و کلك | بیمنی جد باشد ۴ مطلقاً خواء پدر پدروخواءیدر
- ولیشکر وا لیز گویند - وبکسر اول افادة لای |[ مادر 8 - ویمعنی برادرماد رکه خالوباشد- ویرادر
افی می‌کند ۲ . بزرگه هم بنظرآمده است - وبمعنی‌قدرومظمت

۱ بای * نال , فی: کر[ های, سور [لای » شه[نای , نایزه . پارسی‌باستان- 88808
(ای) ۰ پپلوی 88 , فی 880 ؛ هندی باستان -8۶44. - 8244
( ای . نی ) ؛ ارمنی 361 ( تیر ) ؟. ره : امشق *۱۳۹ - نال (قارمی) آر
بممنی نای , ماقه , لوله ۳ اقغانی 8878 (سافه) ۳ ساسکریت -8244 ۱
(ای » بی) * آربایی -0827608 * هوبشمان ۰۶۱۰۹۰ پهاوی 224۳
« تاوادیا ۶۱۹۳ ۰ کردی 861 ( نپال نی » هزمار ) : لری 261 ( یزه )
« ژابا س 1۲۷ > - لی‌بگیاهی اطلاق شود که ساقةٌ آن دراز ومیان تهمی
وطغامت انگشتی با بیش ازآست . مثل «رقتآنجا که نی‌انداختمرب»>
رك : امثال و حکم دهغدا ص۸۹۹ . ۲ دنه (نفی). یب رکه-

[32 خوانده , پهلوی 26 (نه » نی) » ابرانی باستان 38811 ۰ اوستایی ی

1 * پارتولمه۱۰۷۲* رك : لیب که ص۱۵۹ ؛ هرن کلمه را ۰6 خوانده, با «نیست 20891۳
قیای کرده‌است. پارسی‌باستان 281 (نه). آوستا ۰8۵11 38661 , پازند 88. هندی‌باستان ۰8641
استی 8801 ۰ 8101 (هیج چبز) «اسشق ۴۱۰۹۱ ورك : هوبشمان۸ ۰۱*۱ :

۴ - بهلوی لاه ( جد ) [ جمع : 81282 ] ۰ ابرای باستان - 8)1(868
« پارتولمه ۲۱۶۹۸« لیب ر که ص ۰۶۱۹۲ پارسی باستان واوستا -8۳2[ ( پدر بزرکه) . اففاای
2 8 ( مادر بز رکه ) » بلوچی 22۴۵ . 2876 (عم) : *88 ( عادر بز رکه هرنجمع
فارسی را 8178887 داسته « اسشق ۱*۹۲ , افقانی*81868 ( راورتی : 81606[3 ). درپارسی
باستان 2082/81۳2 « هوبشمان ۱*۹۲ *. ۴ - « یا پدر پدر وپدر مادر بودهچنانکه
فردوسی (طوسی) گوید :

بیر هکه جنگه آورد با نیا هم‌ازابلهی باشد وکانیا.» (ابلعی‌است وکانالیا «دهخدا).

+« لغت فری ص ‎٩‏ .۰
جمع : لیاکان (ه.م.)
* - نیا (فربدون) تخت زرین و گرزکران
بدو ( منوچهر ) داد و پیروزه تاج سران.
فردوسی طوسی «شاهنامة بخ ج۱س ۹۹
( قرینون پدر مادر منوچهي بود) +
[pdf page 305]
بیابه ۲۲۲
هرچیز هم هست - تاج رآکوش ۴ - وبمعنی‌حاجتمند ماج
1( [چ 1 : زومند هم آمده‌است 6 - خواهش1 -
با یرای فان بای | وافارست وس مرها پزکر 7
نوبت باشد ؛ وباین معنی‌بجای حرف‌اول بای‌ایچ 7 ال
هم‌آمده وگفته شد . - و بمعنی قحط وغلا - وشره وحرص - وبلذت
نیارست ؟ - بنتح اول و رای قرشت خوردن طمام هت و بسنی دوست دبای
وسکون سين بی‌قطه وفوقانی, بعنی شواست‌واز دشمن ؛ و درجای دیگر درست دربراین ؛
دستش لدامد + ودرسخةٌ دیگر درشت در برایرهموار نوشته شدم
نیاز ۴ « بکراول بروزن‌حجاز,حاجت بود ؛ وهيچيك شاهد دامتند ۸ .
‎٩‏ < نیابة (لیابت) (عر) «نوبة بالفتح بار وپاس: نو ب کسرد جمع . بقال : جامت نوبتك
و لیابتك . . ليابة ككتابة بار و پای » * منتهی‌الارپ » - «النائب اسم فاعل و من قام مقام غیره
فی‌امراوعمل کنائب‌القاضی ودائب‌الملك » و عمله‌النيابة . ج نوب ونواب» « اقرب‌الموارد ». فارسی
دانستن اين‌لفت ناشی از لغت فری‌اسدی(س۶۸۸) است : «نیایه, نوبت بود. پوشکو رکفت :
آن به که نیایه را نگه داری کردار تن خویش راکنی فربه.»
۲ -ر4 : آرستن » بارستن . ۴ - پپلوی 81182 ( احتیاج » ضرورت,فقدان).
از اوستا -27- 81 ۹ 2 پیشولد است وريشهٌ 22 بمعنی بستن » فشار آوردن و مجبور کردن ]
( بتن , فداردادن ۰ بزور داخل کردن ) « بارتولمه ۰۶۳۹۲ 2283 ( ضرورت #تنگی» احتیاج)
« بارتولمه ۳۹۲ > رك : نیب رکه س ۱۹۳.
۴ - دگر بوبهای خوش آورد باز که دارند مردم ببوش لیاز -
فردوسی طوصی ۸« شاهنامهٌ بخ جاص ۲۵ ۰
۰ - باین معنی « نیازمند »۰ « لیازومند » و«لیازی» (ه.م.) است .
‎٩‏ - درفرهنگه نظامآمده : « نیاز. . بمعنی‌خواهش کردن, دیازش - نیاز فخر گر کالی:
سروشان را نام يك بتود بیازشهای بی‌اندازه بنمود . >
موْلف نهی‌الادب در فصل « بیان زبادت »گفته (س ۲۲۸ ): « شین نقطه‌دار , چون «نیازش» مزبد
علیه « بیاز» [است ]. فغرجرجانی درمثنوی ویس‌ورامین گوید : سروشان را ...» « لیازش» درلفت
فری. » جهانگیری » رشیدی » برهان قاطع وانجمنآرا نيامدء و درموضع دیگر درنظم وش دیده
نشده وبیت فوق هم درة وس ورامین » مصحح‌آفای مینوی (س۶4) بدین صورت است :
سروشان را بنام نيك بتود فیایشهای پی اندازه بنمود.
و*اپایش» (پهلوی82[18108 بمعنی‌ستایش)(۸.م.) صحیح است. «اسم مصدر بقلم‌نگارنده ص4۳*.
۷ - مجازاً نذری که برای گرفتن مراد و حاجت خود بنام لبی وولی داده شود که بیشتر
بشکل خوراك است « فرهنگه نظام ».۸ - رشید ی کوید : « لیکن بممنی دوست » لیازی
است نه نیاز » (ر4: نیازی)مژلف فرهنگه نظام نود : «ولی‌معنیاول که درسخهة (سحاح الفری)
زد من درست با سین «همله است (همچنین در لخهّآقای طاعتی) » در سغهةٌ جهانگیری با شین
منقوطه بوده » ودرسه دغخةٌ جهانگیری که نزد من‌است » چنین‌است» اسل این‌اقوال ناشی‌از کفتار
آسدی طوسی است : «نیاز » دوست بود . لبیبی گوید :
ایا نیاز بمن ساز ومر مرا مگذار که نا زکردن معمشوق دلگداز بود .>
« لت فري ۱۸۹ ۰
[pdf page 306]
۲۲۲۳۳ یم
نیاز ارم ۱ « بفتح اول و رای قرشت | نون » بممنی قسد وآهنگه نکردن ودست بطرف
بر وزن لیاسایم » معروف است بمنی آزار ندهم | چیزی دراز شمودن باشد - و بمعنی نیفکندن
-بممتی آزرده نشوم هم‌آمده است .48 و لینداختن - وناله نکردن و ثالیدن هم آمده
نیاز ومند ۲ يم دابع وسکود‌واوه است. .
بممنی‌لیازمنداست که محتاج وحاجنمند باشد. نیاگان ۱ - باعاف فارسیبروزن‌بیابان,
نیازی - بروزن حجازی, بامطابفه‌است | بهمنی اجداد پدری ومادری باشد +
از اففان - ومعشوق و محبوب و دوستدار را نیز نیا ۷ » بکسرارل بروزن حام.بممنی
کوبند ۴ . غلاف شمشیر است ۸ - ومیان و وسط لیخ وغیر
نیاز یان ۴ < بروزن حجازبان , بممنی | تیغرا نیز کوبند. هرچیز باشد ‎٩‏ - ویممتی‌تموی
حاجنمندان باشد - وکنایه ازعاشقان هم‌هست. | هم بنظر‌آمده است *۱- و چوب ین خیش رالیق
نیاز یدن * - بنتح اول ودال وسکون | کفته‌اند ۰۱۱ وآن چوبی است که برزیگران در
۹ -ر4 : آزاردن . ۴ - از: ییاز (ه.م.) طومند ( پوند اصاف *- مند) <
برازمند (م.) ۳ - از : لیاز (.م.) ی (نبت و اصاف) » حاجتمند (ر4 : بیازبان) ‌
وبممنی ممشوق :
چون این سلام زان لیازی شد نامزد شکیب سازی ...
نظامی کنجوی « رشیدی » .
دلم خستَةٌ نت زان » ای‌بیازی! که روزی لیاسایی از باز بازی -
مختاری غزدوی « فرهنگه نظام ».
ی - جمع « لیازی » (ه.م.) 8 - منفی « بازیدن > (ه.م.)
۹ جع «یا» (.م.) ؛ پهلوی 6۵5 ا8 رنه (رك : نیا )» درفارسی 8828( اسشق
۲ دارمتتر. تنبعات چاص ۱۲۳ » ولی بعضی «لیاکان» خوانند :
روان لیاکان ما خو شکنید دل بد سگلان پرآت شکنید. ‏ :
فردوسی طوسی « شاهنامةٌ بخ ج۱ ص۲۵۱*.
۷ - پارسی‌باستان ۰88182002 قس:ساسکربت 81 (پیشوند) ۳ 2189804-۰822
( کنجایش ) . قی : پیام . وجه اشتقاق قطمی لیست « اسشق ۰.۶۱۰۹۳
۸ - غلاف شمشیر وخنجر وکارد . السامی‌فی‌الاسامی‌در معنی فغلاف» » ارس مهذب‌الاسماه
در معنی* غلاف > همین‌کلمه راآورده اند « فرهنکه نظام » :
«مان تیز خنج رکشید از نیام نه بگشاد راز ونه برگفت نام...
فردوسی طومی « شاهنامةٌ بخ ج۱ ص ۵۹
‎٩‏ - بممتی وسط تیخ هوکز نیامده بلکه بممنی وسط هرچیز «میان» است ده « بیام »
سراج‌اللغات بنفل « فرهنگه نظام ج ۵ ص مب >. *۴- ۸« بممتی تعوبف « پنام» است یبای
فارسی». (سراح‌اللغات. ایضاً) - ۱ السامی‌فی‌الاسامی در معثی «المقوم» (عر) (همین‌کلمه
راآورده) فره هنگه نظام» .
۰ نیازهند - بکسر اول و فتح میم . از : لیاز ۳ مند ( پموند اتصاف ) ۳ لیازومند
(وم.) ؛ حاجتمند :
هر که برخود در سوال گشاد تا بمبرد لیازمند بود . «کلتان س ۱۲۳*.
[pdf page 307]
```


## [2026-09-07T20:18:58.770Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT minaret\"; grep -n -i \"minaret\" SKT.txt WEB_vol1.txt FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt LKT.txt PHN.txt DEV.txt HJB.txt 2>/dev/null | head -20"
}
```


### [2026-09-07T20:18:58.844Z] TOOL RESULT

```
=== SKT minaret
PHN.txt:4745:appel du haut des minarets porte le titre de mouezzin. — Voici
PHN.txt:7453:MINARET, s. m. (a.)
PHN.txt:7455:minaret, qui signifie proprement un endroit élevé et sur lequel on
PHN.txt:7463:qui dota d'un minaret la mosquée de Damas.
PHN.txt:7638:ments intérieurs. La tour se nomme minaret; c'est de là que le
PHN.txt:7677:\j^yi [mouàdzdtin^ crieur public, qui^du haut des minarets,
PHN.txt:10729:Minaret, s. m. (a.) 966
DEV.txt:1741:Minaret.  Esp.  minarete.  De  l'arabe  »^Lu  menâra  (pro- noncé à  la  turque),  signifiant  lieu  où  il  y  a  une  lampe  (de la  racine  ^L  nâr,  briller),  puis  lampe,  fanal,  phare,  et  enfin minaret.  Minarete  n'est  pas  dans  le  Glossaire  de  M.  Dozy, mais  on  y  trouve  ahnenara,  candélabre,  fanal,  et  alme- nar,  et  pied  de  fer  sur  lequel  on  mettait  des  torches  de  ré- sine ou  de  bois  résineux  pour  s'éclairer.  ??
DEV.txt:2661:Almpnar,  esp.  voy.  Minaret.
DEV.txt:2662:Almenara,  esp.  voy.  Minaret.
DEV.txt:3935:Minaret.
DEV.txt:3936:Minarete,  esp.  voy.  Minaret.
DEV.txt:5118:cy!  JaJLjL*  voy.  Almicantarat. (;5^lX«  voy.  Moucre, d2A-«  wîrt/.  voy.  Emblic. 2^  voy.  Alchimie,  /io. •^^D  voy.  Melchite,  Moloch L^;i.3X•  voy.  Mélochie, iÇj:k.^L»  voy.  Mélochie. <jl5^  voy.  Mélochie, y^Jm  mal.  voy.  Bambou, Uj«  voy,  Almène. »jU-«  voy.  Minaret. ^j^ULl«  turc,  voy.  Mangal. (S'^^pt  voy.  Moise. oo^  pers.  voy.  Mobed, y 3^  voy.  Muezzin, (^^yt  voy.  Astronomie,  36. •■^y9,  ï^yi  voy.  Musacées. j««^  voy.  Mousson. Juks^  voy.  Mousseline, ù^iyi  voy.  Mulâtre. J^  voy.  Mollah. -^  voy.  Momie, ^j:JL«p»  voy,  Miramolin, Ly«^  voy.  Momie. A^^  voy.  Momie, (^rl^  voy,  Mahari. y^  voy,  Mahari, OsJLg^  voy,  Ohnde. U~y9  pers.  voy,  Mirza. Jwu«  j^er.s,  voy.  Mils. ^Jy^  voy.  Mai  mon,
LKT.txt:3380:Eigentlich  manäi-a  'der  Platz,  wo  Feuer oder  Licht,  ar.  när,  ist';  das  minära ist  der  Turm  einer  Moschee,  von  dessen Brüstung  aus  der  Gebetrufer  niu'addin fünfmal  täglich  die  Gläubigen  zum  Ge- bete aufruft;  pers.  und  tk.  minaret; hieraus  frz.  minaret,  rum.  minarea, minaret;  engl.  ndl.  minaret,  dtsch.  Mi' narelt;  sp.  almenar  'Eisenfuß,  auf  dem man  die  Fackeln  stellt',  sp.  pg.  almenara 'dass.,  Leuchte  in  den  Leuchttürmen'.
LKT.txt:3427:'Gebetsausrufer',  der  von  der  Galerie  des Minaretts  [s.  hier  Nr.  1463a]  aus  den  Ge- betsruf adän  hören  läßt,  tk.  muezzin; hieraus  rum.  muezin,  frz.  muSzzin,  sp. almuecin,  almuedano;  engl,  mueddin, muezzin,  dtsch.  Muezzin.  [DE  150. Eguilaz  240/241.    MWiD  ö2.
LKT.txt:5838:Minarett  I4ü3  a
LKT.txt:6625:mahalep  135ti maharadja  1692 mahari  1"560 mahonfnje  144!) maimon  1365 malamoque  1384 malcuss  dial.  1379 mamlouk  1381 manimouth  1385 inandole  2016 mandore  2015 mangliev  1394 mangoustan  1395 mangue  1393 manguier  1393 «irtiime  1398 mardbout  141U marcassite  1374 Marion  1417 marionnette  1417 tnaroquin  1406 marotte  1417 mascarade  1436 masque  1436 massepain  1452 masser  1440 massicot  1735 »lai!  1443 matasse  476 matassin  1525 matelas  1446 mater  1443 materas  1446 maugrebin  674 milangine  161 melchites  1379 meranghie  161  • meschin(e)  afz.  1470 mesquin  1470 Messie  1437 migerat  afz.  1476 mimonet  1365 minaret  1463  a miqueht  1469 (grand)  Mogol  1494 moirS  1497 moirer  1497 »MoZoc/?  1379 momie  1510 momine  1365 >noMa  1365 morceau  d' Adam  19 mortaise  1713 mort-de-chien  1478 mosquee  1435 mosquete  afz.  1435 moucayarde  1497 moucre  1507 mousquet  1520 mousseline  1484 mousson  1451 mudzzin  1485
LKT.txt:7627:magazijn  1362 mameloek  1384 mango  1393 marokijn  1406 marsepein  1452 masker  (ade)  1436 matras  1446 meerschuim  1416 minaret  1463  a monsoen  1451 nioskee  1435 mousselien  1484 mummie  1510 Witte  1520
LKT.txt:8722:1443 matrapazUc  1445 mattif  1447 mazdrac  1476 mazil(ie)  1450 märgean  1416 märgicä  1416 mäscarä  1436 mascäriciü  1436 mätasä  476 mehenghiü  1498 meid  an  1364 meleag  1509 menzil  1401 merchez  1423 ■meremet(i)  1407 mertepea  1429 meschin  1470 mestß)  1459 >wep  1459 me^inä  1469a meterez  1475 mezat  1454 mezea  1453 mezelic  1453 »iez«7  1401 miambal  344 mic^unea  310 minarea  1463a minaret  1463a mindir(igiü)  1464a mintean  1571 miraz  1467a mirazenie  1467a mirigte  1403 /««««7  1401 mtrzac  69b mofluz(i)  1491 mofluzUc  1491 moft(angiü)  1492 moftangiorcä  1492 woZrt  1448 moloz  1481 momi^a  1365 »wo/nJe!  1510 momue  1510 mormagiu  1482 mosc(u^or)  1515a ntosor(a§)  1442 mo^ea  1435 moqmoalä  1518 moqmol  1518
SKT.txt:11580:Minarot,  a  lu.Tei  on  a  n —  Arab)     Span,  mimarcft, turret.— Arab,  wofiins/,  al.-tr minaret.  —  Arab,  mon^r,  can*  i light-house.      Allicl  to  Arab.  »rfr, iifb.  mandrAM,  a  caiidle-itick ; to  shine:.
```


## [2026-09-07T20:18:59.739Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ nur\"; grep -n -i \"n.r\\b\" FVQ_pages.txt | grep -i \"light\\|nur\" | head -20; echo \"=== AFM/PLA nur\"; grep -n \"نور\\|منار\" AFM_pages.txt | head -10"
}
```


### [2026-09-07T20:18:59.813Z] TOOL RESULT

```
=== FVQ nur
3705:1 It may be noted that the word occurs also in Turkish jj ; TurkI, tanur ;
5428:5 " ^JJ ^ * ine Wtymulogio : zur Bcdeutung ist hier nur daran zu orirmorn,
6032:religiosen Sprachgebrauch ausgesucht ist. Ich kann mir diese Erscheimmg nur aus
=== AFM/PLA nur
813:فاذا قطعة الصانع خرج نوره وحسنة تعر يب ببحّاده وفيه اقوال: فقيل هو الكهرباء .
1487:( الور ;31( الدنيا تعريب خنور وهي كئابة عن جيع 53 1
2056:5 فر بالقائل بالنور والظلمة او من لا يَرْمن بالاخرة او من يبطن
2234:فتحرق جيعا ܕܐܐ ܝ ܩ( قد 80 النار ابداء ܕ | هذا نور ' @( 1 11
3859:,0 ܬ ٠‏ والداعي الى تسميته بالنوروز ان الله تعاللى فيه 6 العالم والانسان الاوّل
3865:فضر بث ܣ التابم 057 امنتلاً ذلك الوضع نورًا وضماء ٠‏ فاستبدع :3
3866:المدظر فاستسغدوا ܛ || ܐܕܬ ا نورورًا ܥ انه يوم ܶܕ ܠܐܒ ܐܬܐ £
3872:8 اعيان الفرس في الايام السنّة التى بين نوروز 3 ܣ 3 يحيبون الى
5220:كنوره ܘܗܙܐ 3 ܨܢ
```


## [2026-09-07T20:19:20.141Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:19:20.149Z] TOOL RESULT

```


```


## [2026-09-07T20:19:22.887Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC nyaka\"; grep -n -i \"nyaka\\|nyāka\" IEC.txt POK_full.txt AHD_watkins1985.txt WLD_band3.txt 2>/dev/null | head -10; echo \"=== ARY nia\"; grep -n \"نیاکان\\|^نیا\\| نیا \" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin\"; grep -n -i \"NIYA\\|NIA\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T20:19:22.980Z] TOOL RESULT

```
=== IEC nyaka
IEC.txt:11122:moniàak-, see mon- “neck, etc. Skt. manyaka "neck nape’; Ober (in Gk.) maniákes, m. ‘necklace’; LW in Arm. maneak, id.; Ir. muineach, m. ‘ridge of hilP
=== ARY nia
710:۹ جنوب را مختمل تر می‌نماید. مضاقاً به اینکه قبل از آنان؛ نیا کان هندیان نیز در همین راستاکوج کرده
1110:مردم را به سرگذشت نیا کان و تاریخ خود آشنا می‌کرد بلکه وظایف آنها را یادآور شده و روحیه‌ی
1476:گرتبکه(شاید) (00714/0): نیا 3 4 ۶0090
1868:سانسکریت (84۸96/7): نیا ای ان پسگشت‌ها ند در
4145:تخاری 8 (8 (7۸۸ل705). لد۱4 هلندی (7ع776ا0): . نیا نان ها ۷
7537:آلمانی ((05701۸): نیا برهان قاطع + ۷۳۹۵
15799:لاتین (47100مل): نا نیا ادن اسلواکی (51.0(420): ۰ 81305110881۸7
=== ARY latin
1997:OLD HIGH GERMAN) «5 glJT ANIYA., ANA.
2414:SLAJNIA (POLISH) ions STR GOTHIC) Ss
2921:BARNHART: (BEAR) 87, (BURDEN) 126 BURTHINNIA
4702:PICE (BOHEMIAN) go PATEISTHAL, PANIA (GREEK) gli.
7342:SWINIA POLISH) gong) SUs, SUIS, SUINUS, SUCULA
9514:RUSSIAN) go 9 vu RUMANIA) gla,
11819:10" sebGdby CULTIVA RUMANIA) «gag,
13107:HNIEZDO s(SLOVAR) gel NIYASHA., NIYASHADYAM
13393:‘TANU., (TANU-TER) MANIYA — (OLD PERSIAN) dul gos),
14158:MEDHAL, MIDER NIYAMAGH, {(BALUCHD) gx 3h
```


## [2026-09-07T20:19:29.580Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7",
 "prompt": "Give the full Persian etymology section for نیا (niyā) 'ancestor, grandfather': Middle Persian form, Proto-Iranian/Old Iranian reconstruction, Avestan/Old Persian cognates, plural نیاکان, and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-07T20:19:30.540Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/minaret",
 "prompt": "Give the full etymology of minaret, including Arabic manarah, its root, and the route via Turkish/French/Spanish."
}
```


### [2026-09-07T20:19:35.466Z] TOOL RESULT

```
# Etymology of Minaret

The word **minaret** entered English in the 1680s from French *minaret*, which derived from a Turkish pronunciation of Arabic *manarah* or *manarat*, meaning "minaret," "lamp," or "lighthouse."

The Arabic root traces back to *manar* (candlestick), which itself originates from *nar*, meaning "fire." This Semitic root connects to Hebrew *ner* (lamp), the same source as the Jewish candelabrum *menorah*.

**The pathway:** Arabic *nar* → Arabic *manarah* → Turkish pronunciation → French *minaret* → English *minaret*

The word's journey reflects cultural transmission through trade and contact, with the architectural term traveling westward alongside the Ottoman Empire's influence on European languages during the 17th century.
```


### [2026-09-07T20:19:37.182Z] TOOL RESULT

```
# Persian Etymology of نیا (niyā)

Based on the Wiktionary content provided, here is the documented Persian etymology:

## Etymology Section

The entry states that نیا derives "From Middle Persian _nydʾk'_ (niyāg, 'grandfather; ancestor')." The source also notes comparison with "Manichaean Middle Persian _nyʾg_ (niyāg)."

## Limitations of Available Information

The webpage does not provide:
- Proto-Iranian or Old Iranian reconstructions
- Avestan or Old Persian cognates
- Citations to Hasandust, MacKenzie, or Cheung
- Extended historical linguistic analysis beyond the Middle Persian form

The entry indicates the noun's plural form is **نیاکان** (niāgān), with a Tajik spelling variant **ниё** (niyo).

The documented etymology in this Wiktionary entry remains relatively concise, focusing on the attested Middle Persian ancestor forms without the comprehensive comparative linguistics or specialized scholarly references you've requested.
```


## [2026-09-07T20:19:43.157Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9",
 "prompt": "Give the Arabic etymology of منارة (manāra): its root, morphological formation (place-noun of instrument?), meanings (lighthouse, minaret, lampstand), and any note on nūr/nār."
}
```


## [2026-09-07T20:19:44.375Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D7%95%D7%A8%D7%94",
 "prompt": "Give the Hebrew etymology of מנורה (menorah): root, formation, meanings, and cognates in Arabic/Aramaic/Akkadian."
}
```


### [2026-09-07T20:19:49.529Z] TOOL RESULT

```
# Hebrew Etymology of מנורה (Menorah)

**Root:** The word derives from the Semitic root נ־י־ר (n-y-r), which relates to light and illumination.

**Formation:** The noun is constructed from this root to denote "a light" or "a lamp."

**Primary Meanings:**
1. A light or lamp
2. A menorah or candelabrum
3. The menorah as a symbol (typically used in definite form)

**Cognates:**
- **Aramaic:** מְנָרְתָא (mənārəṯā)
- **Arabic:** مَنَارَة (manāra)

The word entered numerous European languages through Hebrew, spawning descendants in Dutch, English, German, Italian, Polish, Russian, and others. In Yiddish, it was borrowed directly from Hebrew as מנורה (menoyre).
```


### [2026-09-07T20:19:51.926Z] TOOL RESULT

```
# Arabic Etymology of منارة (manāra)

**Root:** ن و ر (n w r), relating to "light" and "fire"

**Morphological Formation:** The term is a noun of place derived from the root ن و ر, indicating a location associated with illumination.

**Meanings:**
- Lighthouse
- Beacon
- A stand or support for a lamp
- Minaret (in Islamic contexts)
- Menorah (in Jewish contexts)

**Linguistic Note:** The word shares cognates across Semitic languages, including Aramaic מְנָרְתָא (mənārəṯā), Hebrew מְנוֹרָה (mənōrā), and Ugaritic 𐎎𐎐𐎗𐎚 (mnrt). Scholars suggest possible contamination with Ancient Greek μιλιάριον (miliárion, "miles indicator") if the word is interpreted as denoting a landmark. The root fundamentally connects the word's semantic field to concepts of light, fire, and illumination.
```


## [2026-09-07T20:20:00.490Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1",
 "prompt": "List the Arabic and Persian entries for نور: Arabic nūr 'light' (root and plural anwār), Arabic nār 'fire', and the Persian entry (borrowed from Arabic?). Quote the etymologies."
}
```


## [2026-09-07T20:20:03.433Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON nur/manar\"; grep -n \"منار\\b\\|مناره\\|نورانی\\|منوّر\" MON_part1.txt MON_part2.txt 2>/dev/null | head -15; echo \"=== MON nia\"; grep -n \"نیاکان\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== sizes\"; wc -c MON_part1.txt MON_part2.txt"
}
```


### [2026-09-07T20:20:03.523Z] TOOL RESULT

```
=== MON nur/manar
MON_part1.txt:2498:تش رنگ» آذرگون. روشن» نورانی 
MON_part1.txt:9169:کلدسته و مناره و جز آن می‌ خو انند» الفاظ 
MON_part1.txt:30056:و شعاع که از جرمی نورانی ظاهر شود؛ 
MON_part1.txt:40859:نورانی ساختن. (مصل.) زبسا شدن. سوی 
MON_part1.txt:46385:نورانی جز برق و صاعقه و از آن جمله 
MON_part1.txt:56390:(جان.) جانورانی جزو شاخه ذی‌فقاران که به 
MON_part1.txt:69066:تابنا ک» درخشان» منور» نورانی؛ مق. 
MON_part1.txt:70324:درخشان» نورانی» منور. احمر زاهر: سرخ 
MON_part1.txt:92074:وی ذاتی نورانی آفریده شده که از روز 
MON_part1.txt:92077:نورانی نیز بدو پیوندد. این همزاد را طباع تام 
MON_part1.txt:92456:طربال: نها (ع.] (.) منارة بلند ساخته بر 
MON_part1.txt:93297:مناره حلقه‌ای نصب می‌کنند و از دور تیر 
MON_part1.txt:94412:مق. عالم نورانی (شرح حکمت‌اشراق ۱۵۷ 
MON_part1.txt:95847:سحت ترین استخوان‌های جانورانی را که 
MON_part1.txt:97664:(عک.) اشعةٌ نورانی صادر از شیٌ به وسیله 
=== MON nia
MON_part2.txt:7021:فروهرهای نیاکان و با کان اختصاص‌دارد. در 
=== sizes
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
```


### [2026-09-07T20:20:41.401Z] TOOL RESULT

```
# Arabic and Persian Entries for نور

## Arabic Entries

**Main noun (nūr):** "light, ray of light, light beam" with plural أَنْوَار (ʔanwār). The etymology states it is "inherited from Proto-Semitic *nūr-."

**Related term:** نَار (nār) meaning "fire" appears in the related terms section.

## Persian Entry

**Noun (nur):** Defined as "light" with plurals انوار (anvâr) or نورها (nur-hâ). The etymology notes it was "Borrowed from Arabic نُور (nūr)."

The word's path shows transmission from Proto-Semitic through Arabic into Persian and subsequently into multiple other languages including Ottoman Turkish, Urdu, and Kashmiri, demonstrating its wide regional linguistic influence across the Islamic world and beyond.
```


## [2026-09-07T20:20:48.327Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نور (ع\\|نور \\[ع\\|نار (ع\\|نار \\[ع\\|منار (ع\\|منار \\[ع\\|نیا (\\|نیا \\[\" MON_part1.txt MON_part2.txt | head -20; echo \"=== tail range part2\"; tail -c 3000 MON_part2.txt | head -40"
}
```


### [2026-09-07T20:20:48.397Z] TOOL RESULT

```
MON_part1.txt:20490:دنیا (به اعتبار روز و شب.) 
MON_part1.txt:26169:نماید. ( کن.) دنیا (به سب حوادث پسابی). 
MON_part1.txt:53646:شکسته» خرده و ریز. (کد.) مال دنیا (چه کم 
MON_part1.txt:76221:سرای شش در: (کد.) دنیا (به اعتبار شش 
MON_part1.txt:85192:(کد.) دنیا (به اعتبار شش جهت). (کد.) 
MON_part2.txt:14880:قمیش می آیی؛ دیگر قمیش نیا (فرعا.) 
MON_part2.txt:17663:دنیا (غالماً دای کارخانه, گویند.) قورخانه» 
MON_part2.txt:22000:شش گوشه: (کد.) دنیا (به اعتبار شش 
MON_part2.txt:30577:و جنگل‌ها و کوهستان‌های اکثر نقاط دنیا (از 
MON_part2.txt:37653:لابه گرد نیا (ص‌فا.) تضر ع کننده. متملق. 
MON_part2.txt:78295:مبین حال؛ زبان حال. نقد شش روزه: دنیا (به 
=== tail range part2
� بهتر است بصورت بخته شده 
مصرف شود اسیست» سست. سبیس» 
اسپیشتاه بر سیم ححازی» سفسف» قضصب» 
فشفشه» ینجه یونجه معمولی. زکام یونجه: 
(پز.) گونه‌ای زکام که در اثر حساسیت نسبت 
به گرده گیاهان مختلفه (خصوصاً گیاهان 
تبرةٌ گندمیان و يا بروانه‌واران و غیره) ایجاد 
می‌شود و در حقیقت یکك نوع زکام در اثر 
حساسیت است» زکام علوفه. يونجة رازکی: 
(گیاء) گونه‌ای پونجه که دو ساله است و 
ساقه‌اش روی زمین می‌خوابد و در اراضی 
رسی خوب می‌روید؛ این گونه یونجه 
پیش‌رس است و زودتر از اقسام دیگر یونجه 
رشد می‌کند و گل‌هایش زرد رنگ و خیلی 
کوچکند و گل آذینش سنبله‌ای است. یونجة 
زرد: (گیا.) یکی از گونه‌های یونجه که 
دارای گل‌های زرد لیمویی است. محصول و 
چین این گونه یونجه کمتر از یونجة معمولی 
است (یونجةٌ معمولی دارای گل‌های بنفش 
است) فسقط امتیاز آن ایسن است که در 
زمین‌هایی که يونجهٌ معمولی عمل نمی آید 
این گونه یونجه را می‌توان کاشت و چون 
ساقه‌هایش زود چوبی می‌شوند از این جهت 
قمل از آنکه در ساقه‌ها گل ظاهر شود باید 
آن را درو کرد. یونجهٌ شنی: ( گیا.) گونه‌ای 


۸ ۲ 
یونجه که دو رگه است و از آميزش دو گونه 
يونجة زرد و يونجة معمولی حاصل شده 
است» گل‌هایش ممکن است زرد با سز 
روشن و یا بنفش باشند و چنانکه از اسمش 
پیدا است در اراضی شنی ت ۳( 
ی ۶ سالی ۵ ها وان 
تقو لا : بیش از یکبار در سال قابل درو 
پیست. پونجةٌ معمولی: (گیا.) یونجه یونجة 
وحشی: (گیا.) یکی از گونه‌های خود روی 
یونجه که در مراتع می‌روید؛ عشب. نفل» 

مداد.
```


## [2026-09-07T20:20:54.628Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"انوار\" MON_part2.txt | head -20; echo \"=== nia ancestor\"; grep -n \"جد پدر\\|نیاگان\\|اجداد\" MON_part2.txt | head -10"
}
```


### [2026-09-07T20:20:54.706Z] TOOL RESULT

```
3119:اشراق) جهات فقری و ظلمانی انوار ناقص 
3121:و تحدید انوار می‌گردد و مقدار و کمیت و 
3123:بیان که از نورالانوار جز نور اقرب به ان 
3131:از جهت انتساب به اول (نورالانوار) غناء و 
3134:که در انوار ناقصه تحتقق دارد «غواس: 
4934:انوار اسماء الهیه است که منفی صفات روح 
15273:کلی انوار مجرده منقسم می‌شوند به انوار 
15275:باشند و انوار قاهره صوریه که ارباب اصنام 
15280:سهروردی انوار مجرده را بر دو گونه تقسیم 
15281:می‌کند: یکی انوار قاهره» دیگری انوار 
15282:اسفهبد یه يا انوار مدبرة برازخ. انوار قاهره را 
15292:انوار اسفهبدیه مودی به استکمال آنها نتواند 
15293:بود. چون حکیمان قدیم ایران انوار قاهرة 
15295:موجودات و انوار قاهرة عرضی را عبارت از 
40649:لا معه. در خشنده‌هاء رخشان‌ها. (تّص.) انوار 
61172:مراد انوار قاهره است.‎ 
74855:کوه طور که موسی(ع) انوار حق تعالی را بر 
80121:تاریکی؛ ظلمت. شعاع؛ ج. انوار. تر کیبات 
80147:تعالی که اقهر انوار و اعظم و اعلای آنها 
80149:هر یک از انوار در مراتب نازله ناقصتر از 
=== nia ancestor
44130:نشان می‌دهند ابت می‌کند که ماهیان اجداد
```


## [2026-09-07T20:20:57.933Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80100,80135p' MON_part2.txt; echo \"=== nia in MON\"; grep -n \"نیاک\\|نیا\\b\" MON_part2.txt | sed -n '1,30p'"
}
```


### [2026-09-07T20:20:58.005Z] TOOL RESULT

```
سبزی نو دميدة ایام بهار. 

نود. ۵ ( عد.) عددی است معادل هشتاد 
بعلاوة ده» تسعین. (.) دی کون. ضح.- این 
اطلاق به طریق تعمیه است زیرا که عدد نود 
در عقد انامل به همین شکل است. 
(سراجاللغات» به ثقل فر نظا.) 

نوداران: «۰۰-۹2 (.) پولی که به عنوان 
انعام به شا گُردان اصناف دهند. مودگانی. 
صله. 

نود و نه نام: مرجم 12۷20-0۵0 (امر .) مراد 
راسماء حسنی» الهی است که تعداد آنها ٩٩‏ 


است؛. 
نور: 02۷۲000۷0 [ع.] 0( شکوفهةٌ سییك. 


نور؛ 0۵۲ [ع.] (.) روشنایی» فروغ؛ مق. 
تاریکی؛ ظلمت. شعاع؛ ج. انوار. تر کیبات 


اسمی: ور چشم. روشنایی چشم. ( کد.) 


فرزند» قرة العین. نور عذرا: (کن.) دات 
مریم(ع) مادر عیسی. نور مبین: ( کد.) پیغمبر 
اسلام. (فل. اشراق) وجود. ضح.- حکمت 
اشراق مبتنی بر قاعدة نور و طلمت (بجای 
وجود و ماهیت در حکمت مشاء) است و 
چنانکه موجودات بالذات و بالعرض‌اند» نور 
بالذات و بالعرض است که نور حسی و 
عقلی باشد. شیخ اشراق نور را تعریف کرده 
است به آنچه ظاهر به نفسه و مظهر لغیره 
=== nia in MON
489:غانی: 0 [ع.] (ص.) بسی‌نیاز. توانگر» 
493:که به سیب حسن خویش بی‌نیاز از زیور 
495:شوهر خود بی‌نیاز باشد. زن جوان پا کدامن با 
496:شوی؛ ج. غانیات. 
1272:چشمهً سیماب: (کد.) مغرور و فریفتة دنیا. 
1289:معنی غریق در عربی نیامده» ولی در فارسی 
1609:کلمه بدین صورت در عربی نیامده و از 
2175:مثل جلد کتاب» شمشیر و جز آنها؛ نیام. 
2189:متفاوت است؛ نیام. 
2192:در غلاف گذاشتن» در نیام کردن. . (عم.) 
2752:غمد: 0۵ (ع.] (.) نیام شمشیرء غلام تیغ؛ 
3061:این معانی نیامد ۵. 
3803:نف سم نیا ری ی طاس ۱ بجته 
3809:بی‌بنیاد. 
4414:بدون نیاز به قصد زایدی بر علم (ایضا). 
4533:فاقه: ()«« (ع. فاقة| (۰.) نیازمندی. فقر 
5414:ایرانیان باستان فری است که از چهارپایان و 
5613:دنیا و بهره‌های مادی دنیوی باشد و گریز از 
6077:دفعه (مقد مه التفهيم ص قعا). انیا ی 
6207:زانیا رنان فارستی: 
7021:فروهرهای نیاکان و با کان اختصاص‌دارد. در 
7997:نیاز مندی است زبرا ننده همواره نبازمند 
8059:که نیازمند به حق باشد و دلت سوال را تنها 
8267:مسصدر را بر ساخته ایرانیان از ترکیب 
8496:وان که وه از نیا سا 
8659:شفاف و میوه‌اش نیام و دراز است. قسمت 
8708:تیره پولمونیاسه جزو رده دولپه‌یی‌های 
8716:فلونیا: سع] ,2117[7] (۱.) (یز.) معجونی است 
8839:گل‌هایش زرد رنگ و میوه‌اش نیام و دارای 
10141:غذایی مورد نیاز خود را آماده نمایند بنابراین
```


## [2026-09-07T20:21:04.933Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نیازمند\\|نیاسان\\|نیاگان\\|نیاکان\" MON_part2.txt | sed -n '1,20p'; echo \"---\"; awk 'NR>80200 && NR<83000 && /نیا/' MON_part2.txt | head -30"
}
```


### [2026-09-07T20:21:06.540Z] TOOL RESULT

```
4533:فاقه: ()«« (ع. فاقة| (۰.) نیازمندی. فقر 
7021:فروهرهای نیاکان و با کان اختصاص‌دارد. در 
8059:که نیازمند به حق باشد و دلت سوال را تنها 
26802:انواع نیازمند کلمةٌ دیگری است که معنی آن 
49949:بود و نیازمند به تأویل نباشد. 
63348:نیازمند» درویش. 
81763:نیازمند: 1۱-۵ [- نسبازومند | (ص.) 
81767:محتاجی» ضح.- فرق «نیاز, و «نیازمندی» در 
81769:نیازمندی به معنی محتاجی. محتاج بودن و 
81771:ویر اور بکار روند. نیازمندی‌ها: 
81772:جمع نیازمندی. حوایج. (لغت بیهقی. پارسی 
---
تازه. بزرگترین جشن ملی ایرانیان که در 
با فروردین ماه. بیرونی اول سال ایرانیان را 
۲۳ گوید: آغاز سال ایرانیان در اول 
ابرانیان در عهد هخامنشی و اشکانی و 
تواریح برمی آید در عهد ساسانیان نوروز - 
نزدیکترین سال‌های دنیا به سال شمسی 
چهار) ایرانیان باستان جشنی داشته‌اند به نام 
نوروز بزرگ می‌رسید» زندانیان را آزاد 
ساسانیان» فروردین ماه به شش بخش نقسیم 
مالیات‌های کشوری در روز کار ساسانیان در 
ولی در تمام این مدت ایرانیان مراسم جشن 
حاضر که آن بزرگترین جشن ملی ایرانیان 
(گواشت» گردانیاه سلمکك» نوروز اصل» 
نونیاز: ۱-2 (ص‌مر.) شخصی که تازه 
نیام فرهنگ فارسی معین ۱۹۹۹ 
ساز مزبور بعد از اختلاط عرب و ایرانیان 
ابرانیان «نی هفت نند» است که سازی است 
نیا " 7« [- نبا کک | (۱.) جد ( 
نیابت: ۷ (ع. . بان | (مص‌ل.) تانب 
نیابه فرهنگ فارسی معین 
به نیایت: از طرف؛ از جانب. نیابت تولیت: 
مقام کسی که جانشین متولی است. نیایت 
نیابت قضایی: (حق.) گاهی مدعی‌العلوم (و 
نمایندگی را نیابت قضایی نامند. 
نیابه: (ع-)۱۱۷۵0۸ [ع. ۰ تیابه ] ( 
) به نیات؛ به 
نیاح: (ع. | (مسصل.) گریه و زاری 
نیاز: 7 (.) حاجت. احتیاج. خواهش 
خوراک است (فرنظا.) |- نیازی] دوست. 
معشوق. هنگام نیاز: هنگام حاجت.
```


## [2026-09-07T20:21:11.459Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'نیا \" 7« \\|نیا \"' MON_part2.txt | head; echo \"---\"; grep -n \"\\[- نبا کک \\|- نبا کک\" MON_part2.txt | head"
}
```


### [2026-09-07T20:21:11.529Z] TOOL RESULT

```
81707:نیا " 7« [- نبا کک | (۱.) جد ( 
---
81707:نیا " 7« [- نبا کک | (۱.) جد (
```


## [2026-09-07T20:21:13.115Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '81700,81720p' MON_part2.txt"
}
```


### [2026-09-07T20:21:13.168Z] TOOL RESULT

```
خیزران. 

نی: : (قد. 118)[ [- نه] (ق.) نفی را رساند. 
(جمله) گاه بجای جمله ا تفه معنی 
(ز دسسست؟ )۰ 

نیا " 7« [- نبا کک | (۱.) جد ( 
با بدر مادر)؛ ج. . نبا کان. 
نیابت: ۷ (ع. . بان | (مص‌ل.) تانب 


عم از بدر پدر 


سودن» جانشین سشدن. (امص.) ناسی» 
جانشینی. (نظ.) درجه نایبی» ستوانی (غم.) 
امه زشگاه (مدرسة) تیایت. شعه‌ای از 


دانشکدهٌ افسری که در آن درجه‌داران لایق
```


## [2026-09-07T20:21:24.840Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | tail -3; echo \"---\"; grep -n \"نیا\" incoming/ARY/ARY_pages.txt | sed -n '1,40p'"
}
```


### [2026-09-07T20:21:24.903Z] TOOL RESULT

```
16115:[pdf page 543]
16156:[pdf page 544]
16179:[pdf page 545]
---
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
107:پوست هستند ولی زبان مادری بیشتر آنها یک زبان هند و اروپایی (یعنی اسپانیایی) است. :
122:اروپانیان از حاشبه آاز شده باشد. ضمناً دیگر قرائن نشان می‌دهند که زبان‌های هند و اروپائی این
160:اسپانیایی و غیره).
237:چیز باشد: ۱-کوج موی هدر اروپانیان از خاستگاهی واقم در مرکز به سوی حاشیه بوده است (از
341:این پرسش منطقی نیاز به جواب دارد: کاوش‌های باستانشناسی و واژگان غیر هند و اروپایی
344:جزیره) ایبری (اسپانیا و پرتغال) سنگك نیشته‌هایی پدست آمده که به یکك زبان غیر هند و اروپایی قبل
347:زبان «باسکك» (8۸80178) که امروزه در بخش کوچکی از شمال خاوری اسپانیا و جنوب
348:باختری فرانسه تکلم می‌شود در گذشته بخش عمده‌ی اسپانیا را زیر پوشش داشته است. شواهد فراوان
401:از این خانواده‌ها شامل چند زبان‌اند. مثلاً خانواده‌ی لاتین شامل ایتالیایی و فرانسه و اسپانیایی و
412:۸ کهن مادر,زبانهای |سپانیایی و ایتالیایی و پرتغالی و غیره هم هست. بدین روش کم کم بیشتر زبانهای
416:میان فرانسه‌ی کهن و اسپانیایی کهن بیشتر است تا شباهت میان فرانسه و اسپانیایی معاصر.
419:فرانسه کهن اسپانیایی کهن .
421:فرانسه اسپانیای
532:را بوجود آورد. طسبق این باور مردود کلیه‌ی زبانهای دنیا متعلق به یکی از این سه .
536:(1809-1382 ,۸۲ج 8 )که در سال ۱۸۵۹ در اروپا و امریکا و لوله ایجاد کرد؛ بنیاد
560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
563:۳ بوده است. همچئین همسنجی واژه‌های سانسکریت با سایر واژه‌های بنیادین هند و ۱
570:اروپایی نشان می‌دهد که در سانسکریت 0" تبدیل به **شده است. لذا واژه‌ی پنیادین هند و اروپایی
572:واژه‌های بنیادین *۸0۸05" بوده است). طی صد سال گذشته بازسازی واژه‌های بنیادین هند و"
580:نداشته تعیین دقیق آوا و معنی واژه‌های هند و اروپایی بنیادین فقط از روی پیگیری پسگرایانه و
587:پژوهش‌های مکرر شناسایی شده‌اند و آنقدر شبیه واژه‌های بنیادین هند و اروپایی هستند که یک
590:هند و اروپایی بنیادین (یعنی حدود ‎٩‏ هزار سال پیش) پپیگیری می‌شوند و اگر برای یک واژه‌ی
591:ند معاصر واژه بنیادین پیدا نشود؛ در هند و اروپایی بودن آن واژه تردید است. ۱
594:اروپایی و شناخت واژه‌های بنیادین کمک زیادی کرد. این زبانهای مرده (تخاری مربوط به قرن‌های "
630:که فاصله‌ی آن با زبان بنیادین هند و اروپایی نسبتاً قلیل است ارائه می‌دهند. بهمین دلیل در بنیاد یابی
645:برخی دانشمندان معتقد شوند که کوچگران هندی قبل از ایرانیان وارد فلات ایران شده و در سرزمین
660:(48-49 ,۱1۸110۷). قوم ایرانی دیگرا » الان‌ها (۸775آ۸) فرانسه و اسپانیا را زیر مهمیز کشیده و
666:گسترش اقوام ترک زبان (سده‌های ششم تا سیزدهم میلادی) موجب آمپزش آنها با ایرانیان و
707:اِ مردم شمال دریای سیاه را ناچیزتر از شباهت‌های فرهنگی میان ایرانیان و مردمان شمال و خاور
710:۹ جنوب را مختمل تر می‌نماید. مضاقاً به اینکه قبل از آنان؛ نیا کان هندیان نیز در همین راستاکوج کرده
715:حدود ۱۰۰۰ تا ۱۲۰۰ سال پیش از میلاد (یعنی تاریخ احتمالی کوج ایرانیان) است. خویشی بسیار
722:بخش‌های دیگر اوستا در سده‌های بعدی نگاشته شده‌اند. رویهم رفته اوستای اپرانیان و ودای ِ
724:سده‌های نوین و زبان هند و اروپایی بنیادین محسوب می‌شوند. داش ما درباره فارسی کهن پیشتر ."
727:از گذشت زمان» پارسی کهن تبدیل به پارسی میانه (پهلوی) شد. پهلوی زبان ایرانیان در دوران .. ؛
742:می‌دهد که یونانیان بومیان اصلی آن سرزمین نبوده و به آنجا کوج کرده‌اند.
747:اجنماعی یونانیان را ارائه می‌دهند و جزو شاهکارهای ادبی و فرهنگی جهان محسوب می‌شوند.
755:زبان لاتین نشان می‌دهد که لاتین زبانان نیز مانند یونانیان از خارج به ایتالیا کوچ کردند.
763:اسپانیایی و پرتغالی و رومانی و غیره گردیدند. کوچگران زبان‌های رومانس را به امریکای جنوبی و
766:نفر می‌رسد و زبان اسپانیایی (بعد از انگلیسی) یکی از عمده‌ترین زبانهای بین‌المللی شده است.
```


## [2026-09-07T20:21:26.209Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ny%C4%81kah",
 "prompt": "Does this reconstruction page exist? If so give the reconstruction, meaning and descendants (Avestan, Old Persian, Middle Persian, Persian)."
}
```


### [2026-09-07T20:21:27.962Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:21:33.409Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"NYAKA\\|NIYAKA\\|NIYAG\" incoming/ARY/ARY_latin_index_pages.txt incoming/ARY/ARY_pages.txt | head -10; echo \"=== HUB 192\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (202,):\n    print(leaves[i][:1800])\nEOF"
}
```


### [2026-09-07T20:21:34.694Z] TOOL RESULT

```
=== HUB 192
'messe*, up. pati-ma., paivastan Verbinden*, paz. paivasian
Min. Gl. 153, \M.patvastan, SLvm. pafvast 'ty^svxQtmq; payam
aus und neben paiyam *Botschaft', phi. paitdm oder paytam
fiir *patgam i), arm. patgam, aram. pi^gam (Daniel, Esra),
syr. pi&yama, ap. ^patigaTna-; paiyara 'Tadel* H. 358; paida
{paida A. M. p. 3, Z. 3 v. u. ; 4, Z. 12) oflfenbar = phi.
paitdk oder padtak fiir *patdak aus *patdayak oder *pa^-
dayak?^ vgl. zd. paitidaya- 'Aufseher (s. oben p. 44). Un-
klar ist pidram erfreut' (Fird. I, 139, 187) H. 287 und
padtruftan H. 290 (siehe oben p. 38), klar dagegen paiura
*entgegen H. 291 = phi. paitrak aus ap. '^patirya- fiir
^pati'ii-ya- (s. § 8, c) mit J fiir t zwischen Vokalen (nach
§ 84, a). Ueber patyara s. § 83, c.
Isolirt steht der Uebergang von t = d in w in dem aus
dem Avesta entlehnten und entstellten Parsenwort pandm,
penom — iph\, paddm 'Mundtuch*, arab. faddam (Tab. 243),
arm. pandam (Elise 40, 16 v. u.), zd. paitidana- vd. 14, 8.
Zu scheiden von phi. padtdn = zd. paitidana- 'Tunica* vd.
14, 9 (s. oben p. 45).
§ 86. Unsicher ist die Zeit des Ueberganges von t
in y = i, Im P<izend liegen paiman und paivastan nebst
Ableitungen sicher vor, auch peraisn 'adornment' und pBdd
^manifest' Shk. 263. Daneben aber padrastan *to prepare,
provide', padvdxtan *to answer ^), padmdxtan 'to clothe',
Shk. 261-262, Min. Gl. 151—152, patkar 'dispute* Shk.
263, Min. Gl. 157, patkoftan *to strike upon' Min. Gl.
157-158.
•
Im Pehlevi erscheint stets pat, vgl. Gl. and Ind.
p. 92 flg. u. s. w., im Armenischen dagegen
1. pat in patrast, patvast, patgam, patkandaran, patker
(siehe § 85, b), patmudan *Gewand', patvar Tormauer' = zd.
'^paitivdra-, patroik 'Docht' = ap. "^patirauka-j patspar-el
paivazidan
*) Vgl. mand. pugdawa 'Botsohaft*.
*) Np. bevaz 'responsio', bivc^zldan
```


## [2026-09-07T20:21:39.745Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"niyā\\|nyak\\|niyak\\|Grossvater\" HUB.txt | head -20"
}
```


### [2026-09-07T20:21:39.795Z] TOOL RESULT

```
3660:1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
5334:zd. myazda^; niyCt *Grossvater' = ap. zd. nyaka-; razm-yOz
6187:lauts an den Auslaut) = phi. "^pdp, arm. pap 'Grossvater ;
8601:'Ahne' = ap. nydkct- *Grossvater' (np. plur. niydgan); aMahd
```


## [2026-09-07T20:21:43.625Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nfor n in (3660,5334,8601):\n    print(n,'leaf',leafof(n),'-> printed',leafof(n)-10)\nprint('---- context 8601')\nprint('\\n'.join(lines[8592:8610]))\nprint('---- context 5330')\nprint('\\n'.join(lines[5328:5340]))\nprint('---- context 3655')\nprint('\\n'.join(lines[3652:3665]))\nEOF"
}
```


### [2026-09-07T20:21:45.057Z] TOOL RESULT

```
3660 leaf 114 -> printed 104
5334 leaf 162 -> printed 152
8601 leaf 251 -> printed 241
---- context 8601
Lautl. 26); c) nach tonenden^): buzurg 'gross' = sl^, vazrka-;
marg 'Tod' = zd. mahrka-; suturg 'stark', vgl. skr. sthilra-;
bang *Ruf, Stimme* = phi. vang^ arm. vang^ vanh, bal.
gvank] dang quarta pars dirhemi', arm. dang^ dank, phi.
dang H. 536. Doch fallt k nach a in der Regel ab: ni\
*) Ueber den Weohsel von ausl. k und g {kahg und hablc 'Reb-
huhn', mti^f und muiA; u. 8. w.) vgl. Blochmann, JASB. XXXVII,
I, 34.— 241 -
'Ahne' = ap. nydkct- *Grossvater' (np. plur. niydgan); aMahd
Drache; ha, aba mit' - phi. *apak, skr. upak^; -ba, -va
gebackeii; backend' = zd. -paka-', va *zuruck*, skr. apak
(oben p. 21—22); ma 'wir :-= zd. ahmakem; suma *ihr =
zd. xsmakem, Ueber pak^ bak u. s. w. siehe unten § 137, c.
2. Abweichend.
Die im Phi. in der Kegel neu entstandenen, leben-
digen Suffixe -afc, -ak, -ik, -uk, -ok sind (iiber ag, ag u. s. w.)
im Np. zu a, a, f, e*, 6 geworden :
a) handa *Sklave' = phi. bandak^ ap. bandaka- (mit
---- context 5330
asayad ruht, beruhigt*, skr. gayayati ; farmdyad 'befiehlt' H.
821; saya *Schatten H. 695; xaya *Er H. 468;' miyan 'Mitte
= zd. maidyqna- (doch s. § 41); ziyan *Schaden = zd.
zyana- ; siydh *schwarz' = zd. sycLva-, dazu Siyavas = zd.
syavarsan-; mayazd (besser miyazd) *6elage' (parsisch) =
zd. myazda^; niyCt *Grossvater' = ap. zd. nyaka-; razm-yOz
'kampfsuchend', arm. yoiz.
§ 41. Ap. y schwand nach s schon im Pehlevi: np.
sad *frohlich' = phi. sat, ap. siyati- 'Behagen, Freude'; sudan,
pr. savam gehen, werden*, ap. ipf. asiyavam. In beiden
Fallen ist np. s = ap. siy = arisch dy. Vgl. § 132. Aus
anlaut. dy- und jfy ist / geworden : np. ja^t Xeben, Seele* ^)
---- context 3655
Shk. 259. Ebenso jetzt Fr. Muller, WZKM. 8, 190.
1060. Np. nal 'Rohr, Stengel, Rfihre' — afgh. nam f.
'Stengel* = skr. nadd- 'Schilf, Schilfrohr = arisch
"^narda- (Geiger, Etym. und Lautl. des Afgh. Nr. 140).
*) Vgl. arm. hrauer *Einladung* = zd. frava^Sa^ ; arm. paiu&r
*Befehl' = zd. *paitivae3a' (jpaitiva^Say^mi *ioh kUndige an*) nach
Fr. Miiller, WZKM. 7, 371.— 104 -
1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
1064. Im Paz. stets ntro (Min. und Shk.) geschrieben !
1065. Die Etymologie ist lautlieh unmoglich. Nur ein
urspr. ^aniddid wiirde direct zu np. nl^ fiihren. Vgl.
oben Nr. 457 und Fr. M tiller, WZKM. 5, 67.
1067. Dazu afgh. LW. nes 'the sting of any venomous
```


## [2026-09-07T20:21:56.554Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('PHD_mackenzie.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n): return '\\n'.join(lines[:n]).count('\\f')\nprint('3810 leaf',leafof(3810),'-> printed',leafof(3810)-21)\nEOF\necho \"=== NYB niyak\"; grep -n \"niyāk\\|niyak\\|nyʾk\\|ancestor\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:21:57.857Z] TOOL RESULT

```
3810 leaf 81 -> printed 60
=== NYB niyak
463:Anēšē-zātān [/nw&yc?t?n'] patr. of Anošč- zat, the father (or ancestor) of Mihrak 1322, 1525. — From anos = anēšak + zat (q. v.) ‘Immortal-born’; as to the ending -ë in the composition cf s.v. mēnēt.
737:aškamb ['škmb'], aškam ['škm], aškom [škwm], also [KLSH 1013-18, 1111, 6513], belly, stomach, womb 3? etc. — MPrs škmb (A-H II; Sogd. 3176); Paz. aškum (Mx), iškam (SGV); NP iškam, šikam. Aškān ['ik?n!] n. pr., the ancestor of the Aškanian, or Arsacid, dynasty; Zēndān
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
3139:pēšēnīk [pyšynyk] predecessor, pl. cas. obl. ~-dn ancestors 11115, 11216; the troops of the front-line 181, — Derived from pésé, v.s.v. pés. MPrs pysyn ‘earlier’, pl. pyšyng'n; Paz. pl. pēšīnaga; NP pesin(ah), pl. pēšīnagān, pesiniyan.
3406:Säsän [s’s’n'] the ancestor of the Sassanid dynasty 17. 211, 619,
3792:tohmak extraction, parentage 391; pe- digree 4624; patvand u ~ 4 vazurg illus- trious relationship and lineage 72*; pl. cas. obl. ~-dn relatives 874; — family, house (= all the descendants of a common ancestor) dynasty 18-11, 618, 1018, 1321-26, 283; Mihrak i garan ~ u anäk ~ 14!. — MPrth pl. twxmg*n, MPrs twhmg’n, both ‘relatives’; Paz. tuxma, tuxmaa (SGV); NP tuxmah = tuxm.
3850:Urugadaspi [Paz.] one of ZartuxSt’s ancestors 46%, — BdA wanting, BdJ 79° Urvadasp [Paz.]; as to Zsprm, v. I, 189.
4279:Vizak [Paz.] one of Zartuxšt's ancestors 473,
```


## [2026-09-07T20:22:07.011Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371.png"
}
```


### [2026-09-07T20:22:07.496Z] TOOL RESULT

```

```


## [2026-09-07T20:22:07.492Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:22:27.953Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 371 -l 371 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg371hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg371hi.png'); print(im.size)\n# crop region around x 320-1000 y 550-1050 at 200dpi -> x2 for 400dpi\nim.crop((640,560,2100,1080)).save('pg371crop.png')\n\"; ls -la pg371crop.png"
}
```


### [2026-09-07T20:22:31.163Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 9084 Sep  7 16:22 pg371crop.png
```


## [2026-09-07T20:22:33.786Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371crop.png"
}
```


### [2026-09-07T20:22:33.804Z] TOOL RESULT

```

```


## [2026-09-07T20:22:46.479Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg371hi.png')\nim.crop((640,880,1600,1420)).resize((1440,810)).save('pg371crop2.png')\n\""
}
```


### [2026-09-07T20:22:48.066Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:22:50.455Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371crop2.png"
}
```


### [2026-09-07T20:22:50.508Z] TOOL RESULT

```

```


## [2026-09-07T20:23:05.584Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7\" \"https://www.etymonline.com/word/minaret\" \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9\" \"https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D9%88%D8%A7\" ; do echo \"-- $u\"; done; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7' --note 'page 371, root Nyaka, Persian niya < MP niyag' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/minaret' --note 'page 371, root N.w.r, English minaret < Fr < Turk < Arab manarah' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9' --note 'page 371, Arabic manara noun of place from root n-w-r' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D7%95%D7%A8%D7%94' --note 'page 371, Hebrew menorah root n-y-r/n-w-r' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1' --note 'page 371, Arabic nur < Proto-Semitic *nur-, Persian nur borrowed from Arabic' 2>&1 | tail -3"
}
```


### [2026-09-07T20:23:08.779Z] TOOL RESULT

```
-- https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7
-- https://www.etymonline.com/word/minaret
-- https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9
-- https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D9%88%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/9bca9f20c4d32a3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b1c36e279e348b49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8217149de5443a98.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b44de6c0dd6c64d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e35bcba6f9109373.txt
```


## [2026-09-07T20:23:30.975Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n '1,140p' tools/verify_check.py"
}
```


### [2026-09-07T20:23:31.017Z] TOOL RESULT

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


## [2026-09-07T20:23:35.655Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-*.json'))[:40]:\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            if not (n.get('words') or '').strip():\n                print(f, e.get('root'), n.get('id'), n.get('verdict'), '|', (n.get('derivation') or '')[:180])\nEOF"
}
```


### [2026-09-07T20:23:37.020Z] TOOL RESULT

```
page-101.json B.r.q 5 plausible | Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian 
page-103.json B.y.z, B.w.s 5 confirmed | The empty pass-through box is Latin byssus, -ī f. 'fine linen, byssus', borrowed from Greek βύσσος with the ordinary Latin rendering of upsilon by y and of the Greek nominative -os
page-105.json Chiang-yu 2 plausible | An empty pass-through box, and a reasonable one: French soja (also soya) is a borrowing of the Dutch word, spread through botany — Linnaeus' binomial Dolichos soja / Glycine soja i
page-105.json Chou-shu, Shu-shu 1 disputed | An empty pass-through box asserting Mongol transmission of the Chinese word into Persian. The idea is superficially attractive — the Ilkhanid period is exactly when the Chinese loa
page-105.json Cîrâğ 9 confirmed | An empty pass-through box, and the crucial one for this branch: the Iranian word reached Arabic through Aramaic, not directly. The Aramaic form is שְׁרָגָא šərāgā, Classical Syriac
page-107.json Čop, Čop-gân 6 confirmed | Pass-through node: the Greek box is printed empty in the book (only the header 'Greek  SKT:87'), so the extraction is faithful — no word was lost. The word Nourai means is Byzantin
page-112.json Deik 6 confirmed | A pass-through node with no word printed: it stands for the French forms that carried the Latin dic- family into Persian, i.e. dictée (feminine past participle of dicter, itself fr
page-112.json Deik 10 plausible | Another empty pass-through box, standing for French disque, the immediate source of Persian دیسک. Two corrections to the arrow as drawn. First, French disque did not come from Gree
page-113.json Dek 4 confirmed | Empty pass-through box: French is only the transmitting stage between the Latin words of #3 and the Persian loans of #5. The relevant French forms are docteur (Old French doctour, 
page-115.json Dekm 13 confirmed | A pass-through box with no word printed in it (the printed page shows an empty French box), standing for the French metric and commercial vocabulary built on Latin centum: centi- (
page-115.json Dekm 18 confirmed | An empty pass-through box (the printed page shows no word) standing for Aramaic קנטרא qenṭārā / Classical Syriac ܩܢܛܝܪܐ qanṭīrā 'hundredweight', the Aramaic adaptation of Gk. κεντη
page-116.json Dem, Domu 13 confirmed | An empty pass-through box: the Proto-Germanic node is *tem(b)ra- / *timram 'building material, structure', the zero-grade *dm̥- of the verbal sense 'to build' plus the instrument s
page-120.json Derk 5 confirmed | The empty box is the medieval Latin link: Latin tarchon / tarcon, and the reshaped tragonia, taken from Byzantine Greek tarkhon and used by the herbalists (Gesner still writes tarc
page-120.json Derk 8 confirmed | The empty box is Old French dragon, a semi-learned borrowing of the Latin accusative draconem (Latin -onem > OF -on is the regular oblique-case outcome that supplied French nouns o
page-121.json Deru 1 9 unverified | An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout arte
page-121.json Deru 1 13 confirmed | A pass-through box with no words: the Germanic stage between the root and node #14. Pokorny p.215–216 sets it out under three ablaut grades — '*dreu- in got. triu n. ‚Holz, Baum‘, 
page-127.json Dhem 3 confirmed | An empty pass-through box: it stands for the Germanic branch of the root, which Pokorny sets out on p.248 as three parallel enlargements of dhem- — with -p-: MHG dimpfen, dampf 'da
page-129.json Dher 2, Dherabh, Dhrâbh; Dhragh 2 5 plausible | Empty pass-through node: the Latin link is Modern (Medical) Latin trachōma, not a Classical Latin word. Greek τράχωμα 'roughness' (τραχύς + the noun suffix -ωμα, the ordinary medic
page-129.json Dher 2, Dherabh, Dhrâbh; Dhragh 2 6 confirmed | Empty pass-through node: French trachome, first attested 1752 (fr.wiktionary; the term spreads in French ophthalmology after the Egyptian campaign of 1798-1801, when 'ophtalmie d'É
page-130.json Dheu 2, Dhu, Dhu-bh 8 plausible | Empty pass-through box: it stands for the Modern (Medical) Latin typhus, the disease name coined by François Boissier de Sauvages in his Nosologia methodica (1759) directly from Gr
page-130.json Dheu 2, Dhu, Dhu-bh 9 plausible | Empty pass-through box for French typhus (attested from 1806, taken over unchanged from the medical Latin) and typhoïde, from Greek τυφώδης 'typhus-like'; fièvre typhoïde was estab
page-130.json Dheu 2, Dhu, Dhu-bh 17 confirmed | Empty pass-through box standing for the Proto-Germanic continuations of the root that Watkins/AHD collects under dheu-1: *dus- (whence OE dysig 'foolish'), *deuzam 'breathing creat
page-136.json Dhwer, Dhrugh, Dhwor 9 plausible | An empty pass-through box: it marks the language through which the Greek-Latin anatomical term reached Persian, and the book prints no word in it (confirmed on the page image). The
page-137.json Dinghw, Dnghu, Ghu 2, Ghuâ 6 unverified | There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language lab
page-139.json Dolmak 4 confirmed | Empty pass-through node: French doliman / dolman, the immediate source of the English word. French had doliman for the Turkish robe from the 16th century (through travellers' accou
```


## [2026-09-07T20:23:44.599Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD nur\"; grep -n -i \"nawaru\\|nûru\\|nuru\\b\\|namaru\" AKD.txt | head -10; echo \"=== FSD menorah/minaret\"; grep -n -i \"menorah\\|minaret\" FSD_vol3.txt FSD_vol2.txt 2>/dev/null | head -8; echo \"=== WEB\"; grep -n -i \"minaret\\|menorah\" WEB_vol1.txt | head -5; echo \"=== AFA nur\"; grep -n -i \"menorah\\|m.narta\\|nur\\b\" AFA.txt | head -8"
}
```


### [2026-09-07T20:23:44.718Z] TOOL RESULT

```
=== AKD nur
=== FSD menorah/minaret
FSD_vol3.txt:39949:I < Hp minaretf, <
FSD_vol3.txt:54698:and flunked by minarets, whence the faithful arc called
FSD_vol2.txt:32092:3.  Hence,  specif. [G-J,  the  toiver  of  the  ca- thedral of  Seville,  Spain, originally  a   Moorish minaret,  on  which.  In the  16th  century,  was erected  a   bronze  statue  of Faith  so  pivoted  as  to turn  [Sp.  girar]  with  the wind.  A   copy  of  this tower  In  Netv  York  bears a   statue  of  Diana  as  its giralda.
=== WEB
14422:äzän’, n. (from Ar. ddhan.] the Moslem sum- mons to prayer: it is usually ¢alled five times a day by the muezzin, from a minaret on the mosque.
=== AFA nur
36:und wissenschaftliches Vermögen dar, das häufig nur schwierig zu entdecken ist.
41:zugänglich zu machen. Öffentlich zugängliche Bücher gehören der Öffentlichkeit, und wir sind nur ihre Hüter. Nie htsdesto trotz ist diese
46:Dateien nur für persönliche, nichtkommerzielle Zwecke verwenden.
101:Im Allgemeinen habe ich nur solche Worter berücksich-
102:tigt, die mir aus der Litteratur bekannt waren; nur ver-
103:einzelt sind auch andere , nur in secundären Quellen erhaltene
256:schen Lehnwörtern, die nur wenig verändert waren, leicht
287:der Hegra hinabgehen. Gawäliki selbst scheint nur wenig
```


## [2026-09-07T20:23:50.307Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg371.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/371.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/371.png; sed -n '39940,39960p' /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt"
}
```


### [2026-09-07T20:23:50.412Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53926 Sep  7 16:23 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/371.png
In Menado residency, N. E. Celebes Island, under Dntdi
control, cupitai, Menado iret. lighthouse; tower
ml-nar\ 1 nu-nur', 3 iiil-nilri. n lAr 1 AloiUm Arr/i A lui-
mln'a-rrt* 1 mm'e-rnt; 2 mfn'ar-r6l, n. A tall eltuider
tower counected with a
mosque, usually surrounded
bv balconies, from which
the Tiiueasiii summons
the iieoplo to prayer
I < Hp minaretf, <
Turk minOre, < At
manOra, < rntnOr, light*
house. < nOr, shine 1
mln-ar'ient* 1 min-
dr'jcnt, 2 mln-ftr'gftrit.
n. An alloy of rupper,
nickel, and uiiiimonv,
with a little alumi-
num. (< -mi;i- (ill ALUMINUM) 4- T. argentum, silver]
Mruaa, n 1. 1 ml'nns. 2 uirnas. An agricultural depart-
ment In Uruguay, South America. 4.820 sq m 2. its
```


## [2026-09-07T20:25:09.035Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ns in (('BRT.txt',[3565,19354]),('TLM.txt',[1114,1562]),('SYN.txt',[2972])):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    for n in ns:\n        leaf='\\n'.join(lines[:n]).count('\\f')\n        print(f,n,'leaf',leaf)\nEOF\necho \"=== BQT nur?\"; grep -c \"نور\" incoming/BQT/BQT_v4_pages.txt; echo \"=== ARY nur\"; grep -c \"نورانی\" incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T20:25:10.448Z] TOOL RESULT

```
BRT.txt 3565 leaf 78
BRT.txt 19354 leaf 609
TLM.txt 1114 leaf 84
TLM.txt 1562 leaf 127
SYN.txt 2972 leaf 141
=== BQT nur?
305
=== ARY nur
0
```


## [2026-09-07T20:30:13.363Z] TOOL CALL #57: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-371.json <<'JSONEOF'\n{\n  \"pdf_page\": 371,\n  \"book_page\": 341,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"N.w.r\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *n-w-r 'to shine, give light' (verb *nawāru), with the nouns *nūr- 'light' and *nār- 'fire'\",\n      \"note\": \"The root, the language label and the gloss are all right. Klein s.v. Menorah (KLN:963) states it explicitly: Heb. mᵉnōrāh 'candlestick', 'from stem n-w-r, \\\"to give light, shine\\\", whence also ner, \\\"lamp\\\"; rel. to Aram.-Syr. nur, \\\"fire\\\", Arab. nara, \\\"shone\\\", nur, \\\"light\\\", nar, \\\"fire\\\", Aram. mᵉnartā, \\\"candlestick\\\", Arab. manarah, \\\"candlestick; lighthouse; tower of a mosque\\\", Akkad. nuru, \\\"light\\\", nawaru, namaru, \\\"to give light, shine\\\"'. Two caveats. (a) Nourai cites KLN:982, which is the 'minaret' page; that page only says 'fr. nara, \\\"it lighted\\\", rel. to Heb. ner ... See Menorah' — the root statement itself stands at KLN:963, which he cites on the two branch boxes. (b) In Hebrew the root surfaces with y, not w (nēr < *nīr, mᵉnōrāh, root נ־י־ר per Wiktionary); the w/y doublet is old in this root and does not affect Nourai's arrows, but the strictly Hebrew forms are not from n-w-r as written.\",\n      \"note_fa\": \"ریشهٔ سامی ن‑و‑ر «تابیدن، روشنی دادن» ریشه‌ای است شناخته و پذیرفته؛ عربی نور و نار و منارة، عبری نֵر «چراغ» و مנورה، آرامی نورا و مנרתא، و اکدی nūru «روشنایی» و nawāru «تابیدن» همه از همین ریشه‌اند. برچسب «سامی» و معنای «تابیدن، روشنی دادن» درست است و کلاین (ص ۹۶۳، ذیل Menorah) دقیقاً همین را می‌گوید. تنها دو نکته: نخست آنکه ارجاع نورایی به KLN:982 صفحهٔ minaret است و گزارهٔ ریشه در ص ۹۶۳ آمده؛ دوم آنکه در عبری این ریشه با «ی» ظاهر می‌شود (ن‑ی‑ر)، و این دوگانگی و/ی در همین ریشه کهن است. در مجموع ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1\",\n        \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9\",\n        \"https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D7%95%D7%A8%D7%94\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:982\", \"status\": \"partial\", \"note\": \"KLN_1966.txt line 23949 (s.v. minaret, vol. II p.982): 'Arab. manarah, \\\"candlestick; tower of a mosque, lighthouse\\\", fr. nara, \\\"it lighted\\\", rel. to Heb. ner, \\\"lamp\\\", mᵉnōrāh, Aram. mᵉnartā, \\\"candlestick\\\". See Menorah.' The page supports the family but refers the root itself back to p.963.\"},\n        {\"ref\": \"KLN:963\", \"status\": \"supports\", \"note\": \"not cited on the root box but on both branch boxes; KLN_1966.txt line 23475 (s.v. Menorah): 'from stem n-w-r, \\\"to give light, shine\\\" ... Akkad. nuru, \\\"light\\\", nawaru, namaru, \\\"to give light, shine\\\"' — verbatim Nourai's root and gloss.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"vol. II p.963 s.v. Menorah; p.982 s.v. minaret; vol. I p.1 s.v. Abner\", \"stance\": \"supports\", \"note\": \"the three headwords together give exactly the chart: stem n-w-r > Heb. mᵉnōrāh / nēr, Arab. nūr / nār / manārah, Akkad. nūru / nawāru, and Abner 'my father is light'\"},\n        {\"src\": \"DEV\", \"where\": \"p. s.v. Minaret (DEV.txt line 1741)\", \"stance\": \"supports\", \"note\": \"'De l'arabe menâra ... signifiant lieu où il y a une lampe (de la racine nâr, brûler/briller), puis lampe, fanal, phare, et enfin minaret'\"},\n        {\"src\": \"LKT\", \"where\": \"no. 1463a (LKT.txt line 3380)\", \"stance\": \"supports\", \"note\": \"'Eigentlich manāra \\\"der Platz, wo Feuer oder Licht, ar. nār, ist\\\"'\"},\n        {\"src\": \"AKD\", \"where\": \"grep 'nawaru|namaru|nuru' in AKD.txt\", \"stance\": \"silent\", \"note\": \"Zimmern's Akkadische Fremdwörter has no entry for the light-root (it treats loans into Akkadian, not native roots)\"},\n        {\"src\": \"FVQ\", \"where\": \"grep 'nur|light' in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery does not list nūr among the foreign vocabulary of the Qur'ān — i.e. he treats it as native Arabic, which agrees with Nourai\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"nŭr; nâr; manâreh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are ordinary Arabic derivatives of the hollow root ن‑و‑ر. The verb نَارَ nāra (impf. yanūru) / أَنَارَ anāra means 'to shine, give light'; نُور nūr 'light' (pl. أَنْوَار anwār) is the direct continuation of Proto-Semitic *nūr- (so Wiktionary, comparing Akkad. nūru); نَار nār (fem., pl. نِيرَان nīrān) 'fire' is the same root with ā for the medial w; and مَنَارَة manāra(t) is the regular ism al-makān / instrument noun of the pattern maCCaCa(t), 'place where there is a light' — hence 'lampstand', then 'beacon, lighthouse', and from the Umayyad period the tower of a mosque from which the muʾadhdhin calls (whence also the shorter مَنَار manār). Klein p.963 lists precisely nūr, nār and manārah under the stem n-w-r; Lokotsch no. 1463a and Devic give the same analysis of manāra. Nourai's manâreh renders the pausal/Persianised form manāra(h); the Arabic citation form is manāratun.\",\n          \"derivation_fa\": \"هر سه واژه ساخته‌های عادی ریشهٔ عربی ن‑و‑ر («ناره / أنار» یعنی تابیدن و روشنی دادن) هستند: «نور» (جمع: انوار) بازماندهٔ مستقیم سامی آغازین *nūr- است و با اکدی nūru همریشه؛ «نار» (مؤنث، جمع: نیران) همان ریشه با «ا» به جای واو میانی است؛ و «منارة» اسم مکان بر وزن مَفعَلة است، یعنی «جای روشنایی» ← «چراغدان» ← «فانوس دریایی» ← از دورهٔ اموی به بعد «گلدستهٔ مسجد» (و صورت کوتاه‌تر «منار»). کلاین در ص ۹۶۳ همین سه واژه را زیر ریشهٔ n-w-r می‌آورد و لوکوچ و دویک نیز «منارة» را «جای آتش/نور» می‌دانند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:963\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 23475: '... Arab. nara, \\\"shone\\\", nur, \\\"light\\\", nar, \\\"fire\\\", ... Arab. manarah, \\\"candlestick; lighthouse; tower of a mosque\\\"' — the node's three words with the node's three glosses\"},\n            {\"ref\": \"KLN:982\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 23949: 'Arab. manarah, \\\"candlestick; tower of a mosque, lighthouse\\\", fr. nara, \\\"it lighted\\\"'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. II pp.963, 982\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1463a (line 3380)\", \"stance\": \"supports\", \"note\": \"'das mināra ist der Turm einer Moschee, von dessen Brüstung aus der Gebetrufer muʾaddin fünfmal täglich die Gläubigen zum Gebete aufruft'\"},\n            {\"src\": \"PHN\", \"where\": \"p.966 s.v. MINARET (PHN.txt lines 7453-7463)\", \"stance\": \"supports\", \"note\": \"Pihan derives the French word from Arab. manāra, 'qui signifie proprement un endroit élevé et sur lequel on [place une lumière]'\"},\n            {\"src\": \"FSD\", \"where\": \"vol. III s.v. minaret (FSD_vol3.txt line 39949)\", \"stance\": \"supports\", \"note\": \"'[< Sp. minarete, < Turk. mināre, < Ar. manāra, < manār, lighthouse, < nūr, shine]'\"},\n            {\"src\": \"PLA\", \"where\": \"grep in PLA_pages.txt\", \"stance\": \"silent\", \"note\": \"Asbaghi lists Persian loans IN Arabic; nūr/nār/manāra are not there, i.e. no one claims an Iranian origin for them\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nŭr «نور (انوار ، انور)»; manâr «مَنار (مَناره)»; nâr «نار»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All of these are Arabic loanwords in New Persian, taken over with the Arabic morphology intact from the earliest Islamic-Persian prose onward. نور nūr 'light' keeps the Arabic broken plural انوار anwār and the elative انور anwar; the further forms printed in the box are the Arabic derivational set of the same root borrowed as a block — نورانی nūrānī (Arabic relational adjective in -ānī), نیّره nayyira 'luminous' (fem. of nayyir, Form-II-type intensive), منیر munīr (Form IV active participle, *mu-nwir > munīr with the regular hollow-root contraction), منوّر munawwar (Form II passive participle 'illuminated') and تنویر tanwīr (Form II verbal noun 'illumination'). منار / مناره manār(a) is the Arabic word for the mosque tower, taken into Persian in both shapes. نار nār 'fire' survives in Persian mainly in the religious and literary register (نار جهنم, نار دوزخ). Mo'in marks نور as [ع.] = Arabic and gives 'روشنایی، فروغ ... ج. انوار', so Nourai's Arabic → Persian arrow is exactly Mo'in's. There is no Iranian element anywhere here and no round trip: Asbaghi does not list the root among Persian loans in Arabic.\",\n          \"derivation_fa\": \"همهٔ این صورت‌ها وام‌واژهٔ عربی در فارسی نو هستند و با ساخت صرفی عربی خود وام گرفته شده‌اند: «نور» با جمع مکسر «انوار» و صفت برتر «انور»؛ و مجموعهٔ مشتقات عربی همین ریشه که یکجا وارد فارسی شده است — «نورانی» (صفت نسبی عربی با ‑انی)، «نیّره» (مؤنث نیّر)، «منیر» (اسم فاعل باب افعال، mu-nwir* که بر اثر اعلال به munīr بدل شده)، «منوّر» (اسم مفعول باب تفعیل) و «تنویر» (مصدر باب تفعیل). «منار/مناره» نیز به هر دو صورت به فارسی آمده، و «نار» بیشتر در بافت دینی و ادبی («نار جهنم») به کار می‌رود. معین در فرهنگ فارسی «نور» را با نشانِ [ع.] می‌آورد: «روشنایی، فروغ؛ مق. تاریکی؛ ظلمت. شعاع؛ ج. انوار» — یعنی همان مسیر عربی ← فارسی که نورایی کشیده است. هیچ عنصر ایرانی در میان نیست و اصبغی هم این ریشه را در فهرست وام‌واژه‌های فارسی در عربی نیاورده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi, s.v. نور (MON_part2.txt line 80121): 'نور، nur [ع.] (.) روشنایی، فروغ؛ مق. تاریکی؛ ظلمت. شعاع؛ ج. انوار' — tagged [ع.], Arabic, with the plural انوار\"},\n            {\"ref\": \"SAP:1734\", \"status\": \"not_checked\", \"note\": \"Sayyah's Farhang (Persian al-Munjid) is sold only as a paid ebook (refs_online.json: kind 'purchase'); no accessible copy\"},\n            {\"ref\": \"FVA:418\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vazheha-ye arabi dar farsi (1368) — refs_online.json records that no digital copy exists on any permitted platform\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 80121, s.v. نور\", \"stance\": \"supports\", \"note\": \"as quoted; the neighbouring entry نور۱ 'شکوفهٔ سپید' is also tagged [ع.]\"},\n            {\"src\": \"PLA\", \"where\": \"grep 'نور|منار' in PLA_pages.txt\", \"stance\": \"silent\", \"note\": \"Asbaghi has no entry — the root is not a Persian loan in Arabic, so the direction Nourai draws (Arabic → Persian) is the only one on offer\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep 'نور'\", \"stance\": \"silent\", \"note\": \"Addi Shir's hits for نور are all inside other entries (e.g. نوروز, الکهرباء); he does not claim نور itself as Persian\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'نورانی' in ARY_pages.txt (0 hits)\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary covers only the Indo-European stock of Persian, so an Arabic loan is correctly absent\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"minaret\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English minaret (first recorded in the 1680s, in travellers' accounts of the Ottoman lands) is from French minaret, which took the word from the Turkish pronunciation of Arabic مَنَارَة manāra(t) — Ottoman Turkish مناره minare, with the Turkish shift of the unstressed first vowel to i and the French -et ending; Spanish minarete is the parallel form and is what Klein and Skeat make the immediate source. So the English word is a descendant of the Semitic root through the Arabic noun of place, not directly out of the root: KLN:982 'Sp. minarete, fr. Turk. menaret, fr. Arab. manarah', Funk & Wagnalls 'Sp. minarete < Turk. mināre < Ar. manāra < manār, lighthouse, < nūr, shine', Lokotsch no. 1463a 'pers. und tk. minaret; hieraus frz. minaret ... engl. ndl. minaret'. NOTE ON THE ARROW: the JSON gives this box parent 0 (the root), but on the printed page (see data/verification/sources/refs/ocr/BOOK/371.png) the line that ends in this box leaves the bottom of the Arabic box and curves right, while the root's own left spine curves right into the Hebrew box below. The book therefore draws minaret out of Arabic manāreh (#1), which is also the historically correct parent — an extraction error in parent assignment, not a mistake of Nourai's.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی minaret (نخستین کاربرد در دههٔ ۱۶۸۰ در سفرنامه‌های عثمانی) از فرانسویِ minaret آمده و آن از تلفظ ترکی «منارهٔ» عربی، یعنی ترکی عثمانی minare، با ابدال واکهٔ نخست به i و پسوند فرانسویِ ‑et؛ صورت اسپانیایی minarete نیز موازی آن است و کلاین و اسکیت آن را منبع بی‌واسطهٔ انگلیسی می‌دانند. پس این واژه از راه «منارة» عربی به اروپا رسیده، نه یکسر از ریشهٔ سامی. نکتهٔ مهم: در فایل JSON پدرِ این جعبه ریشه (شمارهٔ ۰) ثبت شده، اما در تصویر صفحهٔ چاپی خطِ ورودی به این جعبه از پایین جعبهٔ «عربی» بیرون می‌آید (و ستون خودِ ریشه به جعبهٔ «عبری» می‌رود)؛ یعنی کتاب آن را از «منارهٔ» عربی گرفته است — خطای خوانش اسکن در تعیین پدر، نه خطای نورایی. ریشه‌شناسی خودِ واژه تأیید می‌شود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/minaret\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%A7%D8%B1%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:982\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 23949: 'minaret, n., a slender tower attached to a mosque. — Sp. minarete, fr. Turk. menaret, fr. Arab. manarah, \\\"candlestick; tower of a mosque, lighthouse\\\", fr. nara, \\\"it lighted\\\" ... See Menorah.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11580 s.v. Minaret\", \"stance\": \"supports\", \"note\": \"OCR is rough but legible: 'Minaret ... Span. minarete ... Arab. manārat, a minaret ... Arab. manār, candlestick/light-house. Allied to Arab. nūr, to shine'\"},\n            {\"src\": \"FSD\", \"where\": \"vol. III s.v. minaret (line 39949)\", \"stance\": \"supports\", \"note\": \"'[< Sp. minarete, < Turk. mināre, < Ar. manāra, < manār, lighthouse, < nūr, shine]'\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt line 1741 s.v. Minaret\", \"stance\": \"supports\", \"note\": \"'Esp. minarete. De l'arabe menâra (prononcé à la turque)'; Devic adds Spanish almenara 'candélabre, fanal' from the same word\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1463a\", \"stance\": \"partial\", \"note\": \"Lokotsch routes it 'pers. und tk. minaret; hieraus frz. minaret ... engl. ndl. minaret' — i.e. French from Turkish rather than English from Spanish; same origin, slightly different transmitting language\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 14422 s.v. azan\", \"stance\": \"supports\", \"note\": \"only an incidental mention ('called five times a day by the muezzin, from a minaret on the mosque'); vol. II with the M entries is not available\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Hebrew\",\n          \"words\": \"měnôrâh; ab-ner\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hebrew מְנוֹרָה mᵉnōrāh 'lampstand' is the instrument/place noun of the same light-root — in Hebrew the root appears with y (נֵר nēr 'lamp' < *nīr), and the noun is built with the m- prefix exactly like Aramaic מְנָרְתָא mᵉnārtā and Ugaritic mnrt, the direct cognate of Arabic manāra. Its classic referent is the seven-branched lampstand of the Tabernacle and the Temple (Ex 25:31-40). אַבְנֵר ʾAbnēr, Saul's cousin and commander of his army (1 Sam 14:50; 17:55; 2 Sam 2-3), is ʾābī 'my father' + nēr 'lamp, light' = 'my father is a lamp/light'; Klein compares the Babylonian personal name Abu-nūri built on the same two elements, which confirms the analysis and the Semitic root. Nourai's cross-reference ☞Ab 2 (to his root Ab 'father') is therefore right. Only nuance: the Hebrew forms strictly belong to the y-variant of the root (Wiktionary gives the root of mᵉnōrāh as נ־י־ר), so 'from N.w.r' is true at the Proto-Semitic level rather than within Hebrew.\",\n          \"derivation_fa\": \"عبری مנורה mᵉnōrāh «چراغدان» اسم آلت/مکانِ همان ریشهٔ روشنایی است؛ در عبری این ریشه با «ی» ظاهر می‌شود (נֵר nēr «چراغ» از *nīr) و واژه با پیشوند m‑ ساخته شده، درست مانند آرامی مנרתא mᵉnārtā و اوگاریتی mnrt، که همریشهٔ مستقیم «منارة» عربی‌اند؛ مصداق کلاسیک آن چراغدان هفت‌شاخهٔ خیمهٔ عبادت و معبد است (سفر خروج ۲۵:۳۱–۴۰). «ابنیر» (אַבְנֵר) نام پسرعمو و سردار سپاه شائول است و از ʾābī «پدرِ من» + nēr «چراغ» ساخته شده، یعنی «پدرم چراغ/نور است»؛ کلاین نام بابلی Abu-nūri را با همان دو جزء شاهد می‌آورد. بنابراین ارجاع نورایی به ریشهٔ «Ab ۲» درست است. تنها نکتهٔ باریک آنکه صورت‌های عبری به گونهٔ «ی»‌دارِ ریشه تعلق دارند، پس انتساب به ن‑و‑ر در سطح سامی آغازین درست است نه در درون عبری. ادعای نورایی پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D7%95%D7%A8%D7%94\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:963\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 23475 s.v. Menorah: 'the seven-branched candelabrum in the Tabernacle and in the Temple of Jerusalem. — Heb. mᵉnōrāh, \\\"candlestick\\\", from stem n-w-r ... Cp. the second element in Abner'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.1 s.v. Abner (KLN_1966.txt line 1190)\", \"stance\": \"supports\", \"note\": \"'Abner, n., masc. PN.; in the Bible, commander of Saul. — Heb. Abhnēr, lit. \\\"my father is light\\\", fr. abh, \\\"father\\\", and ner, \\\"light\\\"; cp. the Babylonian PN. Abunuri' — Nourai's gloss word for word\"},\n            {\"src\": \"AFA\", \"where\": \"grep 'menorah|mᵉnartā' in AFA.txt\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramaic loans in Arabic do not treat manāra/mᵉnōrāh, so he does not claim Arabic manāra is an Aramaic loan\"},\n            {\"src\": \"FVQ\", \"where\": \"grep in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"no Hebrew-mediation claim for nūr in Jeffery\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"menorah, Abner\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words come straight from Hebrew, by two different channels. Menorah is a 19th-century borrowing of Hebrew mᵉnōrāh into English through Jewish liturgical usage (German and Yiddish menoyre alongside), and is used both of the Temple lampstand and of the eight-branched Hanukkah lamp; Klein enters it as an English headword spelt Menorah. Abner reached English as a Bible name: Vulgate Abner, thence Wycliffe and the King James Version (1 Sam 14:50), and from the 17th century it was adopted as a Puritan given name in England and New England (Abner Doubleday). Neither shows any sound change beyond ordinary English adaptation of the stress and vowels.\",\n          \"derivation_fa\": \"هر دو واژه یکسر از عبری به انگلیسی رسیده‌اند، اما از دو راه. menorah وام‌واژه‌ای است از سدهٔ نوزدهم که از راه کاربرد دینی یهودیان (و همراهِ آلمانی/ییدیش menoyre) به انگلیسی درآمد و هم بر چراغدان هفت‌شاخهٔ معبد و هم بر چراغ هشت‌شاخهٔ حَنوکا اطلاق می‌شود؛ کلاین آن را با همین سرواژه Menorah آورده است. Abner از راه کتاب مقدس آمد: وولگاتای لاتین Abner، سپس ترجمهٔ ویکلیف و ترجمهٔ شاه جیمز (اول سموئیل ۱۴:۵۰)، و از سدهٔ هفدهم در انگلستان و نیوانگلند نامی پیوریتنی شد. هیچ دگرگونی آوایی ویژه‌ای جز سازگاری معمول انگلیسی در تکیه و واکه‌ها رخ نداده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D7%9E%D7%A0%D7%95%D7%A8%D7%94\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book; the substance is covered by Klein's own English headwords Menorah (p.963) and Abner (p.1), quoted under consulted\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. II p.963 s.v. Menorah; vol. I p.1 s.v. Abner\", \"stance\": \"supports\", \"note\": \"both are entered as English headwords, i.e. Klein treats them as English words borrowed from Hebrew — exactly this node\"},\n            {\"src\": \"FSD\", \"where\": \"grep 'menorah' in FSD_vol1-4\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls (1913 plates) has no menorah entry — the word was still rare in general English dictionaries\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (A-?), grep 'Abner|menorah'\", \"stance\": \"silent\", \"note\": \"no entry found in the available volume\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'menorah|Abner' in SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's Concise omits proper names and this Hebraism\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Nyâka, Nyâkâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Av. nyāka- m. 'grandfather', nyākā- f. 'grandmother'; OP niyāka- m. 'grandfather' (Old Iranian *nyāka-)\",\n      \"note\": \"The root box is right in every particular. Bartholomae's Altiranisches Wörterbuch has the double entry 'j., p. nyāka- m.; nyākā- f. \\\"Grossvater, Grossmutter\\\"' with Vidēvdād 12.9,11 for the Avestan and the Susa inscription of Artaxerxes II for the Old Persian ('Artaxšaçā nyākama' = 'A., my grandfather'); Old Persian spells it niyāka-, with the epenthetic i of the OP syllabary. Buck 2.46 (p.109-110) sets out the same pair. The one thing to add is that the family has NO known Indo-European ancestry: Buck ends 'etym.?', Kent §146.III files niyāka- and apa-niyāka- under 'Of somewhat uncertain analysis', and Pokorny, Walde-Pokorny, Watkins/AHD and Mann all lack the word (greps silent). Nourai does not claim a PIE root for it, and is right not to.\",\n      \"note_fa\": \"جعبهٔ ریشه در همهٔ اجزا درست است. بارتولمه در «فرهنگ ایرانی باستان» مدخل دوگانهٔ nyāka- (مذکر، «پدربزرگ») و nyākā- (مؤنث، «مادربزرگ») را با شاهد وندیداد ۱۲٫۹ و ۱۱ برای اوستایی و کتیبهٔ شوشِ اردشیر دوم برای پارسی باستان می‌آورد؛ در پارسی باستان با «ی» میانجی niyāka- نوشته می‌شود. باک نیز در بند ۲٫۴۶ (ص ۱۰۹–۱۱۰) همین جفت را می‌آورد. تنها نکتهٔ افزودنی این است که این خانواده ریشهٔ هندواروپایی شناخته‌ای ندارد: باک با علامت سؤال «etym.?» تمام می‌کند، کنت در بند ۱۴۶٫III آن را در شمار صورت‌های «با تجزیهٔ نامعلوم» می‌گذارد، و پوکورنی، والده‑پوکورنی، واتکینز و مان هیچ‌کدام این واژه را ندارند. نورایی هم ریشهٔ هندواروپایی برای آن ادعا نکرده و درست کرده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"SYN:110\", \"status\": \"supports\", \"note\": \"Buck §2.46 GRANDFATHER; SYN.txt line 2972 (scan leaf 141 ≈ printed p.109-110): 'Av. nyāka-, nyākā- \\\"grandfather, grandmother\\\" (OPers. nyāka- \\\"grandfather\\\", apa-nyāka- \\\"ancestor\\\"), etym.? Delbrück, op. cit. 474' — Nourai's root box, gloss and both branch words in one line\"},\n        {\"ref\": \"KNT:194\", \"status\": \"supports\", \"note\": \"Kent, Lexicon (KNT.txt line 5611, scan leaf 217 ≈ printed p.194-195): 'niyāka- sb. \\\"grandfather\\\": Av. nyāka- (§146.III); cf. apaniyāka-. niyāka nom. DSl 13; n[iyā]kama asm. A²Sa 4.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"s.v. nyāka- (BRT.txt line 19354, scan leaf 609; AiW n- section)\", \"stance\": \"supports\", \"note\": \"'j., p. nyāka- m.; nyākā- f. \\\"Grossvater, Grossmutter\\\": yat °kē para.irixyeiti °kē (NSf.) vā ... V.12.9; 11; — Artaxšaçā °kama \\\"A., mein Grossvater\\\" Am. I.'\"},\n        {\"src\": \"SYN\", \"where\": \"§2.46, p.109-110\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check; Buck also notes the reciprocal-term pattern and gives Skt. pitāmaha- as the Indic replacement\"},\n        {\"src\": \"KNT\", \"where\": \"§146.III (KNT.txt line 1802) and Lexicon p.194\", \"stance\": \"partial\", \"note\": \"'III. Of somewhat uncertain analysis: niyāka-, apa-niyāka-, marīka- (see Lex. s.vv.)' — Kent accepts the word but not any deeper analysis\"},\n        {\"src\": \"HUB\", \"where\": \"Persische Studien p.152 (HUB.txt line 5334) and p.241 (line 8601)\", \"stance\": \"supports\", \"note\": \"'niyā \\\"Grossvater\\\" = ap. zd. nyāka-' (p.152) and 'niyā \\\"Ahne\\\" = ap. nyāka- \\\"Grossvater\\\" (np. plur. niyāgān)' (p.241)\"},\n        {\"src\": \"POK\", \"where\": \"grep 'nyaka|niyaka' in POK_full.txt\", \"stance\": \"silent\", \"note\": \"no entry — Pokorny reconstructs no PIE root for this word\"},\n        {\"src\": \"AHD\", \"where\": \"grep in AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"Watkins has no root covering Av. nyāka-\"},\n        {\"src\": \"IEC\", \"where\": \"grep in IEC.txt (only manyaka- 'neck' matched)\", \"stance\": \"silent\", \"note\": \"Mann gives no IE comparison for the grandfather word\"},\n        {\"src\": \"WLD\", \"where\": \"grep in WLD_band3.txt\", \"stance\": \"silent\", \"note\": \"not in the Walde-Pokorny index\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"niyâk, niyâkân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian nyʾk' — read niyāg by MacKenzie, niyāk in the older transliteration Nourai follows — is the regular continuation of Old Iranian *nyāka-, with the OP-style epenthesis in the initial cluster (ny- > niy-) and the post-vocalic stop written k but pronounced -g in later Middle Persian, as the Manichaean spelling nyʾg shows. The plural is niyāgān, formed with the ordinary MP animate plural -ān; because the -g- is now intervocalic it is preserved there, which is why New Persian has the pair niyā / niyāgān. Attestations: MacKenzie p.60 'niyāg [nyʾk' | M nyʾg, N niyā] grandfather, ancestor'; the Pahlavi Husrav ud Rēdag §4 (Unvala 1917 p.13) 'u šmāh niyāgān' = German 'und eurer Ahnen'; Nyberg's Kārnāmag glossary quotes 'Mānušcihr amāh niyāg' 'Manuščihr our forefather'. So both the singular and the plural form of the node are genuine Pahlavi words with exactly the sense 'grandparents, forefathers'.\",\n          \"derivation_fa\": \"فارسی میانهٔ nyʾk' — که مکنزی آن را niyāg می‌خواند و نورایی به شیوهٔ کهن‌تر niyāk آورده — بازماندهٔ منظمِ ایرانی باستان *nyāka- است: خوشهٔ آغازی ny- با واکهٔ میانجی به niy- بدل شده و همخوان پایانی که با k نوشته می‌شود در فارسی میانهٔ متأخر ‑g تلفظ می‌شده، چنانکه املای مانوی nyʾg نشان می‌دهد. جمع آن niyāgān است با پسوند جمع جاندارِ ‑ān؛ چون ‑g‑ در این صورت میان دو واکه قرار می‌گیرد حفظ شده، و همین است سرّ جفتِ فارسی نو «نیا / نیاکان». شواهد: مکنزی ص ۶۰ «niyāg [nyʾk'] پدربزرگ، جد»؛ متن پهلوی «خسرو و ریدگ» بند ۴ (اونوالا ۱۹۱۷، ص ۱۳): «اُ شماه نیاگان» یعنی «و نیاکان شما»؛ و واژه‌نامهٔ نیبرگ که «مانوشچیهر اَماه نیاگ» («مانوشچیهر نیای ما») را نقل می‌کند. پس هم صورت مفرد و هم جمعِ این جعبه واژهٔ اصیل پهلوی است با همان معنایی که نورایی داده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2221\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 4, printed p.2221 = BQT_v4_pages.txt [pdf page 304] (the running heads of the next two leaves read ۲۲۲۲ and ۲۲۲۳, confirming the offset). Mo'in's footnote 4 to نیا: «پهلوی nyāk (جد) [جمع: nyākān]، ایرانی باستان *ni(y)āka-، بارتولمه ۱۶۹۸ ... پارسی باستان و اوستا nyāka- (پدر بزرگ)» — precisely Nourai's Pahlavi box\"},\n            {\"ref\": \"UNV:52\", \"status\": \"partial\", \"note\": \"Unvala's 1963 Paris edition (the one Nourai cites) is not online; the 1917 Heidelberg dissertation, which is (UNV.txt), has the word in the text itself at §4, printed p.13: 'u šmāh niyāgān' rendered 'und eurer Ahnen'. So the substance is confirmed, the page number cannot be\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.60 (PHD_mackenzie.txt line 3810)\", \"stance\": \"supports\", \"note\": \"'niyāg [nyʾk' | M nyʾg, N niyā] grandfather, ancestor'; English-Pahlavi part p.? 'grandfather niyāg', 'ancestor niyāg'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. kurušk (NYB_vol2_glossary.txt line 2347)\", \"stance\": \"partial\", \"note\": \"quotes the Bundahišn passage 'cigēn gōbēt kū Mānušcihr amāh niyāg kurušk-ē pat bārak dāšt' — the word is attested in Nyberg's texts with the sense 'forefather', though it is not a headword of his glossary\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 1062, p.238 (HRN.txt leaf 259)\", \"stance\": \"supports\", \"note\": \"'ap. aw. nyāka- \\\"Grossvater\\\", vergl. ap. apanyāka- \\\"Ahne\\\"; phlv. nyōk' — Horn's Pahlavi reading is nyōk, an older reading of the same spelling nyʾk'\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.241\", \"stance\": \"supports\", \"note\": \"cites the Pahlavi/OP form as the base from which NP niyā loses final -k\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nîyâ «نیا ، نیاکان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian نیا niyā 'forefather, ancestor; grandfather' is Middle Persian niyāg with the regular loss of the final stop after long ā. Hübschmann sets this out as a rule (Persische Studien p.241): after a the -k of Middle Persian normally drops — 'niyā \\\"Ahne\\\" = ap. nyāka- \\\"Grossvater\\\" (np. plur. niyāgān)' — and the plural keeps the consonant because there it is intervocalic, giving نیاگان niyāgān (often written نیاکان in the manuscripts and so printed by Nourai). Mo'in's dictionary states the derivation outright: «نیا [< نیاک] (ا.) جد (اعم از پدر پدر یا پدر مادر)؛ ج. نیاکان» — 'grandfather, whether father's father or mother's father'. The sense widened from 'grandfather' to 'forefather, ancestor' already in the Shāhnāme, which uses both (Ferdowsī's «نیا (فریدون) تخت زرین و گرز گران / بدو داد» has the narrow sense, Nourai's quoted line «چنین بود رسم نیاکان تو» the wide one). Wiktionary's entry agrees: 'From Middle Persian nyʾk' (niyāg, \\\"grandfather; ancestor\\\")', plural نیاکان.\",\n          \"derivation_fa\": \"فارسی نو «نیا» بازماندهٔ فارسی میانهٔ niyāg است با افتادنِ قاعده‌مندِ همخوان پایانی پس از «ای» کشیده؛ هوبشمان (پژوهش‌های فارسی، ص ۲۴۱) این را قاعده می‌شمارد: «ک» پس از ā در فارسی نو معمولاً می‌افتد — «niyā «جد» = پارسی باستان nyāka-، جمعِ فارسی نو niyāgān» — و در جمع، چون همخوان میان دو واکه است، نگه داشته می‌شود: «نیاگان» (که در نسخه‌ها و در کتاب نورایی «نیاکان» نوشته شده). معین نیز صریح می‌گوید: «نیا [< نیاک] (ا.) جد (اعم از پدر پدر یا پدر مادر)؛ ج. نیاکان». تحول معنایی از «پدربزرگ» به «جد، پیشین» از همان شاهنامه دیده می‌شود؛ در بیتِ «نیا (فریدون) تخت زرین و گرز گران بدو داد» معنای تنگ و در بیتِ نقل‌شدهٔ نورایی «چنین بود رسم نیاکان تو» معنای گسترده به کار رفته است. ویکی‌واژه هم همین را می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2221\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt [pdf page 304] = printed p.2221: the headword نیا with the definition «بمعنی جد باشد مطلقاً خواه پدر پدر و خواه پدر مادر» and Mo'in's footnote 4 giving the Pahlavi and Old Iranian forms and citing «اشتقاق ۱۰۶۲» — i.e. Horn's no. 1062, the very entry Nourai cites as HRN:238. The نیاکان entry follows on printed p.2223 with footnote 6: «جمع «نیا»؛ پهلوی nyākān ... در فارسی niyāgān»\"},\n            {\"ref\": \"HRN:238\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 259 = printed p.238, entry 1062: 'niyā \\\"Grossvater, Ahne (Plur. niyāgān)\\\", ap. aw. nyāka- \\\"Grossvater\\\", vergl. ap. apanyāka- \\\"Ahne\\\"; phlv. nyōk' — root, Pahlavi stage, New Persian word and plural, exactly as charted\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, s.v. نیا (MON_part2.txt line 81707)\", \"stance\": \"supports\", \"note\": \"«نیا [< نیاک] (ا.) جد (اعم از پدر پدر یا پدر مادر)؛ ج. نیاکان»\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 printed pp.2221 and 2223 (pdf pages 304, 306)\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check; Mo'in's footnote also gives Pashto nīka, Baluchi nākō and reports Horn's reading of the Persian plural as niyāgān\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.241 (and p.152)\", \"stance\": \"supports\", \"note\": \"'ni[yā] \\\"Ahne\\\" = ap. nyākă- \\\"Grossvater\\\" (np. plur. niyāgān)', in the paragraph on the loss of final k after ā\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.60 s.v. niyāg\", \"stance\": \"supports\", \"note\": \"the entry's bracket '[nyʾk' | M nyʾg, N niyā]' explicitly gives New Persian niyā as the descendant\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'نیا' / 'NYAKA' in ARY_pages.txt and ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"no headword found in the OCR (the Persian hits are all دنیا/نیاز/اروپاییان); Aryanpur has no Indo-European root for the word either\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"apa-nyâka\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The compound is genuine and the analysis is Nourai's: Old Persian apaniyāka- = apa- 'away, off' (PIE *apo-, cf. Skt. apa, Gk. apo, Lat. ab) + niyāka- 'grandfather', i.e. the generation removed beyond the grandfather. It is attested once, in Artaxerxes II's Susa inscription A²Sa 4: 'imam apadāna Dārayavauš apaniyākama akunauš' 'this apadāna Darius my ancestor built' (apaniyākama = the word plus enclitic -ma(iy) 'my'). Two corrections. (i) The gloss: Kent p.168 renders it 'great-great-grandfather', comparing Latin ab-avus, which is the same formation (ab- + avus); Bartholomae has 'Vorfahr des Grossvaters, Urältervater'. Nourai's 'great grandfather' is one generation short, though his second gloss 'ancestor' is what Tolman and Buck give and is how the inscription is normally translated. (ii) The label: apa-nyāka- is Old Persian only — Bartholomae marks it 'p.' (altpersisch) alone, not 'j., p.' as he does for nyāka- itself — so the box's 'Avestan / Old Persian' header overstates the attestation. Hence plausible rather than confirmed: the arrow root → apa-nyāka- is right, the gloss and language label are loose.\",\n          \"derivation_fa\": \"این ترکیب اصیل است و تجزیهٔ آن همان است که نورایی می‌گوید: پارسی باستان apaniyāka- از apa- «دور، آن‌سو» (هندواروپایی *apo-، سنسکریت apa، یونانی apo، لاتین ab) + niyāka- «پدربزرگ»، یعنی نسلی فراتر از پدربزرگ. تنها یک شاهد دارد، در کتیبهٔ شوشِ اردشیر دوم (A²Sa 4): «ایمَم اَپَدانا دارَیَوَئوش اَپَنیاکَمَ اَکوناوش» یعنی «این کاخ را داریوشِ نیایِ من ساخت». دو اصلاح لازم است: نخست معنا — کنت (ص ۱۶۸) آن را «پدرِ پدربزرگِ پدر» (great-great-grandfather) می‌گیرد و با لاتین ab-avus می‌سنجد که همان ساخت است، و بارتولمه «نیای پدربزرگ» می‌آورد؛ پس «جد» نورایی یک نسل کوتاه است، هرچند معنای دومش «نیا/جد» همان است که تولمن و باک داده‌اند. دوم برچسب زبان — این واژه تنها در پارسی باستان گواه دارد و بارتولمه آن را فقط با نشان «p.» می‌آورد، نه «j., p.»؛ پس عنوان «اوستایی / پارسی باستان» جعبه بیش از گواهی موجود است. به همین دو دلیل: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:168\", \"status\": \"partial\", \"note\": \"Kent, Lexicon (KNT.txt line 5000, scan leaf 190 = printed p.168, the offset confirmed by the lexicon's alphabetical run): 'apaniyāka- sb. \\\"great-great-grandfather\\\": from apa- + niyāka- \\\"grandfather\\\", cf. Lt. ab-avos'. The page is the right one and gives Nourai's morphology, but glosses the word one generation further back than Nourai's 'great grandfather'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. apa-nyāka- (BRT.txt line 3565, scan leaf 78)\", \"stance\": \"partial\", \"note\": \"'p. apa-nyāka- m. \\\"Vorfahr des Grossvaters, Urältervater\\\": dārayavaʾuš °kaʾmaʾ \\\"Darius mein Urältervater\\\" Am. I.' — Old Persian only, and 'Urältervater', not 'great grandfather'\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon s.v. apanyaka (TLM.txt line 1114, scan leaf 84)\", \"stance\": \"supports\", \"note\": \"'apanyaka, m. ancestor. Nom. sg. apanyaka ... imam apadana darayavaus apanyakama akunas. apa (q.v.) + nyaka (Phl. nyak).' — Nourai's second gloss and his morphology\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §2.46, p.110\", \"stance\": \"supports\", \"note\": \"'OPers. ... apa-nyāka- \\\"ancestor\\\"' — again the loose gloss, and again Old Persian only\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.104, addendum to Horn no. 1062 (HUB.txt line 3660)\", \"stance\": \"supports\", \"note\": \"'1062. Lies afgh. nīka (Raverty nīkceh) und ap. apanyaka-' — Hübschmann correcting Horn's spelling of exactly this compound\"},\n            {\"src\": \"KNT\", \"where\": \"§146.III (KNT.txt line 1802)\", \"stance\": \"partial\", \"note\": \"'Of somewhat uncertain analysis: niyāka-, apa-niyāka-, marīka-' — Kent flags the formation as not fully clear\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify. On the printed page (pdf 371 = book p.341; image saved at data/verification/sources/refs/ocr/BOOK/371.png) the box hanging to the right of the apa-nyāka box is a completely empty double-ruled rectangle: no language header, no reference, no word, and no arrow leaving it. It is a layout artefact of Nourai's chart software — the same blank filler box that appears on other pages (cf. the verified pages 121 and 137) — and the extraction is faithful in recording it with no language, no refs and no words. No claim is made, so none can be checked.\",\n          \"derivation_fa\": \"چیزی برای بررسی نیست. در صفحهٔ چاپی (صفحهٔ ۳۴۱ کتاب = برگ ۳۷۱ پی‌دی‌اف؛ تصویر در data/verification/sources/refs/ocr/BOOK/371.png ذخیره شده) جعبه‌ای که در سمت راستِ جعبهٔ apa-nyāka آویخته است مستطیلی است کاملاً خالی با دو خط حاشیه: نه نام زبان دارد، نه ارجاع، نه واژه، و نه پیکانی از آن بیرون می‌رود. این جعبه صرفاً بازماندهٔ صفحه‌آرایی نمودارهای نورایی است — همان جعبهٔ خالیِ پرکننده که در صفحه‌های دیگر (مانند صفحه‌های ۱۲۱ و ۱۳۷ که پیش‌تر بررسی شده‌اند) هم دیده می‌شود — و خوانش اسکن درست عمل کرده و آن را بدون زبان و بدون واژه ثبت کرده است. چون ادعایی در آن نیست، داوری‌ای هم نمی‌توان کرد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference; nothing to look up\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BOOK\", \"where\": \"printed page 341 (pdf 371), rendered at 200 and 400 dpi\", \"stance\": \"silent\", \"note\": \"the box is empty on the page itself — verified on the image copied to data/verification/sources/refs/ocr/BOOK/371.png\"},\n            {\"src\": \"KNT\", \"where\": \"Lexicon pp.168, 194\", \"stance\": \"silent\", \"note\": \"no further derivative of apa-niyāka- exists in Old Persian that the box could stand for\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-371.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T20:30:15.040Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T20:30:20.136Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 tools/verify_check.py 371"
}
```


### [2026-09-07T20:30:21.407Z] TOOL RESULT

```
nodes verified: 9/9
node verdicts: {'confirmed': 7, 'plausible': 1, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 4, 'partial': 2}
books consulted: {'supports': 21, 'silent': 12, 'partial': 4} | by book: {'KLN': 3, 'FSD': 3, 'HUB': 3, 'LKT': 2, 'PLA': 2, 'MON': 2, 'ARY': 2, 'SKT': 2, 'WEB': 2, 'PHD': 2, 'KNT': 2, 'PHN': 1, 'AFM': 1, 'DEV': 1, 'AFA': 1, 'FVQ': 1, 'NYB': 1, 'HRN': 1, 'BQT': 1, 'BRT': 1, 'TLM': 1, 'SYN': 1, 'BOOK': 1}
```


## [2026-09-07T20:30:41.872Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-371.json` written, `verify_check.py 371` reports 9/9 nodes, 0 PROBLEM lines.

**Page 371 (book p. 341) — 2 entries, 9 nodes**

Verdicts: roots 2 confirmed; nodes 7 confirmed, 1 plausible, 1 unverified.
Ref checks: 8 supports, 2 partial, 4 not_checked. Books consulted: 21 supports, 4 partial, 12 silent.

- **Entry 0 `N.w.r` [Semitic] — confirmed.** Klein p.963 (s.v. Menorah) states the stem n-w-r with Akkad. nūru/nawāru, Arab. nūr/nār/manārah, Heb. nēr/mᵉnōrāh, and Abner — verbatim Nourai's chart. Nourai's root citation KLN:982 is the *minaret* page (partial: it refers the root back to p.963). Persian node confirmed by Mo'in's `[ع.]` tag on نور; minaret confirmed by Klein/Skeat/Funk&Wagnalls/Devic/Lokotsch/Pihan/Etymonline.
- **Entry 1 `Nyâka, Nyâkâ` [Av./OP] — confirmed.** Buck §2.46 (p.109–110) and Kent p.194 give exactly the root box; Bartholomae has nyāka- m. / nyākā- f. Note: no PIE ancestry exists (Buck "etym.?", Kent §146.III "uncertain analysis"; Pokorny, Walde-Pokorny, Watkins, Mann all silent) — Nourai rightly claims none. BQT:2221 located and confirmed (Borhan vol. 4, pdf p.304); Horn no. 1062 (p.238) matches the Pahlavi→NP chain exactly.

**`plausible` items**
- Entry 1 #3 `apa-nyâka` — derivation (apa- + niyāka-, A²Sa 4) is sound, but Kent p.168 glosses it *great-great-*grandfather (cf. Lat. ab-avus) and Bartholomae "Urältervater"; Nourai's "great grandfather" is a generation short. Also the form is Old Persian only, so the box's "Avestan / Old Persian" label overstates the attestation.

**`unverified`**
- Entry 1 #4 — a genuinely empty double-ruled box on the printed page (no language, refs or word); layout artefact, extraction faithful.

**Extraction error for the owner to fix**
- `data/extracted/batch/page-371.json`, entry 0, node **#3 (English "minaret") has `parent: 0`; the printed page draws the arrow out of the Arabic box, so `parent` should be `1`.** Confirmed at 400 dpi: the line into the minaret box leaves the bottom of the Arabic box and curves right, while the root's own left spine curves right into the Hebrew box below. (Historically the Arabic parent is also the correct one: manāra → Ott. Turk. minare → Fr./Sp. → Eng.)

No `disputed` or `transcription_suspect` nodes. Page image archived at `data/verification/sources/refs/ocr/BOOK/371.png`; 5 web pages archived via `fetch_source.py`.
