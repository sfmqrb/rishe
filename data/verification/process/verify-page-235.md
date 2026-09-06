# Verification process log — verify-page-235


## [2026-09-06T15:37:55.380Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 235 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-235.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-235.json. Write /home/sfmqrb/git/rishe/data/verification/page-235.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 235` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:37:56.798Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:37:57.534Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:37:57.552Z] TOOL RESULT

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


## [2026-09-06T15:37:58.019Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-235.txt"
}
```


### [2026-09-06T15:37:58.032Z] TOOL RESULT

```
1	=== PDF page 235 (book page 205) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kâk 2, Kank, Kâkha : twig, branch  (refs POK:523)
4	#1 (parent #0) [Sanskrit] refs=POK:523 | šâxa, čâxa : branch
5	  #2 (parent #1) [Persian] refs=POK:523; BQT:1219; SYN:525 | šâx «شاخ» : horn, branch | extra: شاخه
6	#3 (parent #0) [Sanskrit] refs=POK:523 | šakala : part, piece
7	  #4 (parent #3) [Persian] refs=BQT:1280 | šeklah «شکله» : slice, piece, a torn piece of garment
8	#5 (parent #0) [Sogdian] refs=SOD:376 | šnk : branch
9	--- entry 1 ---
10	ROOT [Indo-European] Kak 3 : to become thin  (refs POK:521)
11	#1 (parent #0) [Avestan / Old Persian] refs=POK:521; FFD:67 | kasu : small ; kâs : to reduce ; kas-yah : less ☞Yah 5 ; kas-išta : smallest, least ☞Isto
12	  #2 (parent #1) [Persian] refs=HUB:86; BQT:1564; HRN:185; FFD:67 | -ak «ـک» : suffix indicating smallness ; kâstan «کاستن» : to reduce | extra: مرغک ؛ کاهیدن ، کاه ۲ ، کاهش ، کاست | NOTE: See "Akos" for another possible root of suffix "-ak"
13	--- entry 2 ---
14	ROOT [Aramaic / Indo European] Kak 4, Gag : a round object (loaf), cake  (refs POK:349; BQT:1572; AHD:1520)
15	#1 (parent #0) [Persian] refs=BQT:1572 | kâk «کاک» : dry hard bread, a dry cookie
16	  #2 (parent #1) [Arabic] refs=SDQ:71; PLA:233 | ka`k : a dry bread
17	    #3 (parent #2) [Persian] refs=BQT:1572 | ka`k «کعک» : dry bread
18	#4 (parent #0) [Germanic] refs=POK:349; AHD | kakan
19	  #5 (parent #4) [English] refs=None | cake
20	#6 (parent #0) [Dutch] refs=AHD | koek
21	  #7 (parent #6) [English] refs=None | cookie
22	--- entry 3 ---
23	ROOT Kâkha -> redirect to Kâk 2
24	--- entry 4 ---
25	ROOT Kakîna -> redirect to Kakis
26	
```


## [2026-09-06T15:38:02.458Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-235.json",
 "description": "Read source JSON for page 235"
}
```


### [2026-09-06T15:38:02.510Z] TOOL RESULT

```
{
  "pdf_page": 235,
  "book_page": 205,
  "entries": [
    {
      "root": {
        "name": "Kâk 2, Kank, Kâkha",
        "lang": "Indo-European",
        "refs": "POK:523",
        "gloss": "twig, branch"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:523",
          "words": [
            {"translit": "šâxa, čâxa", "gloss": "branch", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:523; BQT:1219; SYN:525",
          "words": [
            {"translit": "šâx", "gloss": "horn, branch", "script": "شاخ"}
          ],
          "script_extra": "شاخه",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:523",
          "words": [
            {"translit": "šakala", "gloss": "part, piece", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1280",
          "words": [
            {"translit": "šeklah", "gloss": "slice, piece, a torn piece of garment", "script": "شکله"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:376",
          "words": [
            {"translit": "šnk", "gloss": "branch", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kak 3",
        "lang": "Indo-European",
        "refs": "POK:521",
        "gloss": "to become thin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:521; FFD:67",
          "words": [
            {"translit": "kasu", "gloss": "small", "script": null},
            {"translit": "kâs", "gloss": "to reduce", "script": null},
            {"translit": "kas-yah", "gloss": "less", "script": null, "see": ["Yah 5"]},
            {"translit": "kas-išta", "gloss": "smallest, least", "script": null, "see": ["Isto"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HUB:86; BQT:1564; HRN:185; FFD:67",
          "words": [
            {"translit": "-ak", "gloss": "suffix indicating smallness", "script": "ـک"},
            {"translit": "kâstan", "gloss": "to reduce", "script": "کاستن"}
          ],
          "script_extra": "مرغک ؛ کاهیدن ، کاه ۲ ، کاهش ، کاست",
          "note": "See \"Akos\" for another possible root of suffix \"-ak\"",
          "quote": {
            "text": "درد تاریکیست درد خواستن - رفتن و بیهوده خود را کاستن",
            "poet": "Forŭgh Farrokh-Zâd"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Kak 4, Gag",
        "lang": "Aramaic / Indo European",
        "refs": "POK:349; BQT:1572; AHD:1520",
        "gloss": "a round object (loaf), cake",
        "note": "This word is apparently of Egyptian origin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1572",
          "words": [
            {"translit": "kâk", "gloss": "dry hard bread, a dry cookie", "script": "کاک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "SDQ:71; PLA:233",
          "words": [
            {"translit": "ka`k", "gloss": "a dry bread", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1572",
          "words": [
            {"translit": "ka`k", "gloss": "dry bread", "script": "کعک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:349; AHD",
          "words": [
            {"translit": "kakan", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cake", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Dutch",
          "refs": "AHD",
          "words": [
            {"translit": "koek", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cookie", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kâkha", "redirect": "Kâk 2"},
      "nodes": []
    },
    {
      "root": {"name": "Kakîna", "redirect": "Kakis"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:38:04.934Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SYN','HUB','HRN','FFD','AHD','SOD','SDQ','PLA','WLD','MON','ARY','PHD','NYB','BRT','KNT','KLN','IEC','FVQ','AFM','LKT','SKT','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T15:38:06.709Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SDQ {"title": "A. Siddiqi, Studien über die persischen Fremdwörter im klassischen Arabisch, Göttingen 1919", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/studienberdiep00sidd", "identifier": "studienberdiep00sidd", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SDQ.txt", "page_offset": "leaf = printed + 14..15 (e.g. leaf 16 = p.1/2). local 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
CHEUNG MISSING
```


## [2026-09-06T15:38:21.196Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


### [2026-09-06T15:38:21.233Z] TOOL RESULT

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
```


## [2026-09-06T15:38:21.385Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:38:21.429Z] TOOL RESULT

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
```


## [2026-09-06T15:38:25.445Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AHD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SYN'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T15:38:27.188Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
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
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
```


## [2026-09-06T15:38:31.183Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 52[0-4]\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 349\" POK_full.txt | head"
}
```


### [2026-09-06T15:38:31.240Z] TOOL RESULT

```
43185:Page(s): 520 
43238:Page(s): 520 
43262:Page(s): 520 
43290:Page(s): 521 
43302:Page(s): 521 
43340:Page(s): 521 
43380:Page(s): 523-524 
43399:Page(s): 524 
43417:Page(s): 524 
43443:Page(s): 524-525 
44166:Page(s): 521 
44182:Page(s): 521 
44194:Page(s): 524 
49317:Page(s): 521-522 
49361:Page(s): 522 
49508:Page(s): 522-523 
49553:Page(s): 523 
---
29625:Page(s): 349 
29667:Page(s): 349-350 
34794:Page(s): 349
```


## [2026-09-06T15:38:32.033Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==180' POK_02.txt | head -60"
}
```


### [2026-09-06T15:38:33.929Z] TOOL RESULT

```
heidr,  ags.  hced,  engl,  heath,  ahd.  heida  f.  ,Heide- kraut',  mhd.  heide  f.  ,Heide' ]  daneben  ags.  *häd,  engl.  dial.  hoath]  urgerm. *Äaij{>ana5, steppenbewohnend,  wild',  wohl  Lehnübersetzung  von  iat.pä^änws ( :  pägtis  ,Land'),  dazu  got.  haipnö  f.  , Heidin',  aisl.  heidinn,  ags.  häeden, engl,  heathen,  asächs.  hethin,  ahd.  heidan,  heidin,  heidanisk  ^heidnisch' -^ anders  W.  Schulze  Kl.  Schriften  521  ff.
über  lat.  hücetum  ,Kuh-Trift'  s.  WH.  I  120,  Vendryes  RC  48,  398.
WP.  I  328  f..  Feist  237  f.
kaiur-t,  kaiun-t  , Grube,  Kluft'. Ai.  kivata-  m.  , Grube';
gr.  Tialara'  ÖQvy^ara  Hes.,  hom.  -/.aLaxösoGa  {AaY£Öaiy.(jov]  so  für  über- liefertes -KTjrcbsaaa  herzustellen)  , klüftereich',  y.aiddag  Erdschlund  in  Sparta (d  wie  in  dsy,dS-  :  lit.  deHmt-). WP.  I  327,  Specht  Idg.  Dekl.  25.
kakka-  ,cacäre';  Lallwort  der  Kindersprache.
Arm.  Hakor  ^Mist',  gr.  xaxx«w  ,cacö',  xaxxTj  , Menschenkot',  lat.  cacö, -äre,  mir.  caccaim  ,caco',  cacc  ,Kot',  cymr.  cach,  bret.  cach,  com.  caugh ds.,  russ.  usw.  käkatt  ,cacare',  nhd.  kacken-^
dazu  yielleicht  als  Kinderwort  —  vgl.  nhd.  gegga  ,pfui'  —  auch  gr. 7iay,6g  , schlecht';  neuphryg.  %a:^ow  ,Böses',  nach  Friedrich  (Eberts  Real- lexikon I  139)  gr.  Lw. ;  kaum  hierher  Kayiao ßog,  kleinas.  Reitergott  (in Lykien),  vgl.  oben  S.  309.
WP.'l  336.
käk-  Nachahmung  des  Krächzens.
Ai.  käka-  m.  , Krähe',  käkäla-,  käkola-  m.  ,Rabe';  lett.  käk'is  , Dohle' (auch  apr.  koce  ds.,  wenn  so  für  kote  zu  bessern) ;  zum  lett.  FIN  Kak'upe, lit.  FIN  Kakupis  (vgl.  Ka^vrtaQLg,  FIN  in  Sizilien?)?  Anders  über  die halt.  Worte  Mühlenbach-Endzelin  II  190.
WP.  I  335.
kak-  , abmagern'.
Av.  kasii-  ,klein,  gering',  Komp.  Superl.  kasyah-,  kasista-] nhd.  hager  (Trautmann  ZfdtWtf.  7,  267,  KZ.  43,  153);
522  •
lit.  nukaseti  ,ganz  entkräftet  werden'. WP.  I  334.
kak-  (kek-?)  , vermögen,  helfen'.
Ai.  saknöti  ,kann,  ist  imstande,  hilft',  Desid.  nksati  ,hilft,  huldigt, dient,  lernt',  sakti-  f.  ,Hilfe',  sakra-  ,vermögend',  sagma-  ,vermögend,  hilf- reich', sdcl  f.  ,Vermögeu,  Hilfe',  sdka-  m.  ,Kraft,  Hilfe',  ääkd-  ,kräftig, helfend;  m.  Helfer',  säkman-  n.  ,Hilfe';  y^\.  sdkvan-  ,geschickt';
av.  sacaiti  , versteht  sich  worauf,  Desid.  sixsaiti  , lernt',  npers.  saxt ,hart,  fest,  sehr'  =  Ki.Jakta-  ,vermög
```


## [2026-09-06T15:38:40.612Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==181' POK_02.txt | head -70"
}
```


## [2026-09-06T15:38:41.447Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43360,43400p' POK_full.txt; echo ===; sed -n '43280,43350p' POK_full.txt"
}
```


### [2026-09-06T15:38:43.395Z] TOOL RESULT

```
end' ;
air.  cedit  , Macht'  {*kankt-  oder  *kenkt-)]
Vielleicht  lit.  kankü,  käkti  , wohin  gelangen,  genügen,  hinreichen' (Reihenwechsel?);  unsicher  auch  ags.  hagan  ,genitalia',  mhd.  Äa^ew  , Zucht- stier', nhd.  dial.  hegel  ds.,  haksch  , Zuchtschwein',  nhd.  hecken  ,sich  paaren (von  Vögeln)',  engl,  hatch  ,hrüten',  ahd.  hegi-diniosa  ,Hode'.  Ebenso,  weil  nie -Ä-,  sondern  nur  -g-  im  Wurzelauslaut,  die  germ.  Sippe  aisl.  hagr  ,passend, geschickt',  liagr  m.  ,Lage,  Vorteil,  Wohlstand',  haga  , anordnen',  högr, hegr  ,passend,  bequem',  hättr  (*hahtu-)  ,Art  und  Weise'  (wäre  «w-St. neben  dem  ^i-St.  ai.  sakti-),  ahd.  st.  Partiz.  ki-hagan,  bihagan  ,heiter', mhd.  behagen  ,passen,  recht  sein',  nhd.  behagen,  mhd.  hage  m.  , Behagen, Wohlgefallen',  as.  bihagön  , behagen,  gefallen',  ags.  onhagian  ,passen,  be- hagen', gehagian  unpers.  , Gelegenheit  sein' ;  unter  Annahme  von  ausl.  -gh- vergleicht  Zupitza  Gutt.  104  sie  mit  prakr.  ca{y)ati  ,ist  fähig',  A9oka- Inschr.  caghati  ,ist  zu  etwas  bereit,  willig',  av.  cagdd-  (mit  rafdördm) , Hilfe  gewährend',  cagdman-  n.  , Geschenk',  cagvah-  ,bietend,  gewährend', die  freilich  w^iederum  in  ihrem  e-Vokalisraus  nicht  so  unmittelbar  zum germ,  a  :  ö  stimmen ;
toch.  A  käkmart,  B  kamart  ,Herrschaft'.
WP.  I  333,  334.
I.  käk-  :  kdk-,  wahrscheinlich  kä[i]k-  :  kik-  (mit  kdk-  als  Ablautneubildung von  kak-  aus)  , springen,  hervorsprudeln,  kräftig  sich  tummeln'.
Gr.  xrjKLüj  , entspringe,  sprudle  hervor',  xäx/w'  ISqovv  ItQxo^ai.  ^aY,(avsq Hes.,  x'^xfg,  -Idog^  dor.  xflix/g  f.  ,alles  Hervorsprudelnde  (Blut;  Purpursaft; ausbratendes  Fett;  Dampf)';  lesb.  xa/xvAi;  ds.  Hes.;
lit.  sökti  , springen,  tanzen';  nasaliert  sanküs  ,flink',  sankinti  ,(ein  Pferd) springen  machen'  (vgl.  Y.ayv.vh])  und  ahd.  hengist,  ags.  hengest  ,Hengst', eig.  Superl.  ,am  besten  springend,  bespringend',  germ.  *hangista  neben *hanhista  (gramm.  Wechsel)  in  anord.  hestr  ,Pferd',  zum  Positiv  *hanha-, dazu  Dat.  urnord.  hahai  ,dem  Renner'  und  ahd.  Häh-,  Hang-,  aisl,  Ha- in PN;   dazu  kelt.  *kankstikä  , Stute'  in   cymr.  caseg  ds.,   bret.   PL  kezeg
I
523
Pferde',  dial.  , Stuten',  acorn.  cassec  , Stute',  gall.  ON  Cassiciate  (Lok.) , Pferdepark'.
Für  käik-'.klk'  führt  man  das  wohl  thrak.-phryg.  aULv(v)Lg  ,Tanz  der Satyrn  zu  Ehren  des  Dionysos'  (zwar  i  bei  den  Lex.,  aber  Eur.  Cycl.  37 auch  mit  l  meßbar)  an,  wohl  auch  xtxvg  f.  , Kraft',  genauer  , Beweglichkeit, Frische',  ztxvw  *  Ta;fT;vw,  layvo)  Zonar.,  ep.  ion.  IjcxiKvgy  -vog  , schwach, schlapp';
Pedersen  KG.  I  51  stellt  hierher
```


### [2026-09-06T15:38:43.444Z] TOOL RESULT

```
Exit code 1
Note: 

Wrong etymology, alb. akuir\ce' derived from Old Norse yip/ri///m. " hanging down icicle, 
glacier ' see Root / lemmai^e^'- : ice' 

Old Irish Middle Irish calath, ca/ad'\r\ar6', cymr. ca/ec/6s., gall. VN Caleti, Caletes, in 
addition gallo-rom. *calJo-, *caliauo-^ sioue' (M.-L. 1519a), as well as gall. -Latin callio- 
marcus' coltsfoot, herb (Tussilago Farfara), whose leaves and root are employed in 
medicine to treat coughs ' {^ox*callio marcT testiculus equi '), epo-calium {\eQ. -callium), 
ebul-calium {ior *epalo-callium, to mcymr. ebawl, bret. ebor plenitude ') ds., to cymr. caill, 
bret. kelli. "testicle' (Dual *kalnai); 

Church Slavic kaliti^ temper, harden (glowing iron)', serb. prlkala' hoarfrost '. 

Maybe alb. kaliV temper ' a Slavic loanword. 

References: WP. I 357, WH. I 139 ff.; 388. 

See also: Zusamenhang with AeA'hit' would be possible. 

Page(s): 523-524 

Root / lemma: kal-2, kali-, kalu- 
Meaning: handsome; healthy 

Material: Old Indie /ra/ya-'fit, healthy, lively ', ka/yana- ^beaut\iu\, healthful ' {-ana-= *alno- 
to gr. u)A£vr|, cbAAov, above S. 308 f.); gr. *KaAAo- = Old Indie kalya- (?) as base from 
KaAAiwv, KaAAiGToq "schoner, schonst', KtxKKoc, n. 'beauty'. kqAAuvu) 'make beautiful', 
Ionian KoAAovn 'beauty', koAAi- as 1 .composition part; besides with formants -u- Boeotian 
KaKVbc, = hom. kqAoc;, Attic etc. kqAoc; 'beautiful'; in addition as Spottname KoAAiac; 'ape' 
and perhaps kqAAoiov n. (mostly PI.) ' cockscomb, crest on head of cock, rooster's comb '. 

/■stem Old Norse halr{*hali-) 'man, husband, master, mister' (poet.). Old English 
/7^/e(^dy/'man, husband', asachs. helid. Old High German helfd^mau, husband, 
combatant, hero ', Old Swedish halith, besides ^stem Old Norse bg/drlree farmer, man, 
husband' {*halut^). 

References: WP. I 356, 443, Specht Indo Germanic Dekl. 128, 195; Seller, The primaren 
gr. Steigerungsformen 68 ff. 
Page(s): 524 

(eval):1: == not found
```


## [2026-09-06T15:38:53.006Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: k\" POK_full.txt | grep -iE \"sak|sok|kak|kank|kakh|khak\" | head -30"
}
```


### [2026-09-06T15:38:53.094Z] TOOL RESULT

```
43320:Root / lemma: kakka- 
44168:Root / lemma: kak- 
47756:Root / lemma: ko ko, kak(k)-, ku(r)kur-
```


## [2026-09-06T15:38:53.809Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sakha\\|shakha\\|s'akha\\|sakala\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:38:53.867Z] TOOL RESULT

```
49514:Material: Old Indie sakhai. "bough' (: Gothic hoha, Armenian caA); sakala-xx\. n. "chip, 
49523:Indie sakha; after Meillet Esquisse2 36, Slave commun^ 23 f. rather from Indo Germanic 
49535:Gothic /7o/7a "plough' (= Old Indie sakha). Old High German huohili^ a small arable field 
49539:Lithuanian saAa "bough' (ablaut, with Old Indie sakha), sake^ fork ', saAa/ys "splinter' (: 
49540:Old Indie sakala-), saknis. Old Prussian sagn/st, Latvian sakne \oot'; Lithuanian sakarnis 
72889:because of Aryan A/? dubious: Old Indie sakha {sakhi-) ' fellow, comrade, friend',
```


## [2026-09-06T15:38:55.701Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49500,49560p' POK_full.txt"
}
```


### [2026-09-06T15:38:55.753Z] TOOL RESULT

```
honor of the Dionysos ' (namely /by Lex., but Eur. Cycl. 37 also may be evaluated with /), 
probably also kTkuc; f. " power ', accurate " flexibility, briskness', kTkuu) tqxuvu), iaxuu) 
Zonar, ep. Ionian qkIku^, -\joc, 'weak, flabby'; 

Pedersen KG. I 51 places here (kTku(;:) Irish cTchi. " female breast', cymr. cig, bret. kik, 
acorn, c/7/ic "flesh'. 

References: WP. I 334, Hofmann Etym. Gr. Wb. 142, Kluge^i s. v. Hengst. 
Page(s): 522-523 

Root / lemma: Rak-2, nasalized Rank- 

Meaning: branch 

Material: Old Indie sakhai. "bough' (: Gothic hoha, Armenian caA); sakala-xx\. n. "chip, 

splinter, splinter, wooden log, schnitzel, shred' (: Lithuanian sakalys); sa/jku-m. " wooden 

nail, peg, plug, picket, pole, stick ' (: Old Church Slavic sgkb, cymr. ca/nc, Old Norse ha/); 

sakti-i. "spear, javelin' (: Old Irish cecht); 

Armenian c5A'"twig, branch', perhaps loanword from pers. sax6s., and these from Old 
Indie sakha; after Meillet Esquisse2 36, Slave commun^ 23 f. rather from Indo Germanic 
*ksakh-\ 

because of the meaning doubtful alb. //7e/re "fringe, tail ', compare after all the same 
meaning from Norwegian heker corner, tail' under *keg-, 

cymr. cainc{*kanku, compare i/-stem of Old Indie sarjku-), PI. cangau, mcymr. canghau 
"bough'. Middle Irish gee, nir. ^ea^" bough' (with secondary voiced-nonaspirated in aniaut), 
with -sk- suffix gallo-rom. *gascar/a {French Jachere) " arid land', actually " arable field ', 
Hubschmied Vox Rom. Ill 123^; Old Irish gescae^bN'\g, branch, bough'; with /-suffix Old 
Irish cec/7/ "plough' (probably as */r5/7/r-/c»- next-related to Old Indie sakti-); 

Gothic /7o/7a "plough' (= Old Indie sakha). Old High German huohili^ a small arable field 
'; nasalized Old Norse har^ oarlock' {*hanha, Finnish loanword), hse//^peg, plug, stick' 
{*hanhila-); 

Lithuanian saAa "bough' (ablaut, with Old Indie sakha), sake^ fork ', saAa/ys "splinter' (: 
Old Indie sakala-), saknis. Old Prussian sagn/st, Latvian sakne \oot'; Lithuanian sakarnis 



' brachiating ', Latvian sakarnis^ Wurzelenoe '; Old Church Slavic *SQkTD " a tender young 
twig, branch, shoot, sprout, sprig '; 

Slavic 5c»c/7a"club, cudgel (Old Church Slavic etc.), hook, plough (russ.), Gabelstange ' 
(poln.), poln. rozsocha^ forked bough'. Old Church Slavic pc»sc»c/7bm. "cudgel, club'. 

References: WP. I 335, Trautmann 297 ff., Specht Indo Germanic Dekl. 55, 254; 
See also: compare under ke(n)g-, ke{n)k- "peg, plug, hook' S. 537 f. and kenk-, konk- 
"waver, hang ', S. 565. 
Page(s): 523 

Root / lemma: Ras-, Ras- 
Meaning: to teach, indicate 
Note: only Aryan and Armenian 

Material: Old Indie sasti, 1. PI. 5/s/77a/7 "weist zurecht, zijchtigt, herrscht, befiehit, belehrt', 
participle Aor. 5/5a/7/- "teaching', sista- " reprimanded, instructed, instructed ' (newer sasta-
```


## [2026-09-06T15:39:10.903Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29600,29680p' POK_full.txt"
}
```


### [2026-09-06T15:39:10.949Z] TOOL RESULT

```
Material: Isl. Aa/ra "cake', Norwegian and Swedish /ra/ra "small, round and flaches bread', 

Danish kage " cake' (Germanic *kakan-), wherefore the diminutive Old English cicel, cycel 

" small cake' (engl. cake\s Norse loanword) and changing through ablaut Norwegian kok 

"clump', Swedish koka^ clod, clod of earth'. Middle Low German koke. Old High German 

/ri/oc/70 (Germanic *kdkan-) "round bread, cake', in addition the diminutives Old English 

caecil, cec/7 and Old High German kuocheli(n)^ small cake'; 

Maybe alb. /ro/re "round object, head' 



Lithuanian guoge' cabbage head, head, thick skull ', guogJngas' mit Kopf versehen ', 
guogiotr Kopfe ansetzen (vom Kohl) '. 

From Germanic *kakan- der'we Finnish kakko, lapp. gakko^ cake', Finnish kakkara ^c\od 
of earth, lump of earth, bread'; 

about prov. katal. coca' cake' (ndd. loanword) s. Meyer-Lubke^ 4734. 

References: WP. I 530 f., Kluge^ 333. 
Page(s): 349 

Root / lemma: ga/-1 



Meaning: bald; naked, *callow (without feathers) 

Note: 

Root / lemma: gal-1\ "bald; naked' derived from Root/ lemma: koi-lo-\ "naked; miserable'. 

Material: Old High German kalo{*kalua-), inflectional kalwer. Middle High German kal 

"naked, bald, bleak'. Old English calu, engl. ca//o\/v'nake6, bald, bleak, callow'; Old High 

German ca/ua " baldness, a bald spot '; 

Latvian ga/a, ga/et (lengthened grade) " thin ice cover, glazed frost, ice ', ga/s^ ice- 
smooth '; 

aki. go/b "naked', sloven, gof, russ. gdty/^ba\6, bleak, naked', Czech holy 6s., holek^ 
beardless fellow ', /7o//ra"girr, etc.; in addition Church Slavic golotbi. "ice', Czech holot, 
russ. goiotbi. " ice, icing, glazing '; 

baltoSlavic *galuat "head' in: 

Latvian ga7vat, Lithuanian ga/va {Akk. galv^) f. "head (substantive Adj.)', 

Old Prussian gallu, Akk. ga/wan6s.; Lithuanian ga/votas' kopfig ' (= Serbo-Croatian 
g/avaf); 

Old Church Slavic g/ava'hea6', Serbo-Croatian g/ava {Akk. glavu), russ. goiova {Akk. 
goiovu); Serbo-Croatian glavaV having a large head ', Czech hlavaty^ kopfig '; 

Baltic and slaw, intonation {galvc[ : goiovu) do not agree; compare Meillet Slave 
commun2 183, 503; Baltic pushed intonation spoke after Trautmann 77 rather for kinship 
with Armenian ^/^-^"head' from *^/7dA/-/rc»- (Meillet Esquisse 36); then however, Germanic 
words must be observed as Latin loanword (from calvus). 

References: WP. I 537 f., WH. I 143 f., Trautmann 77; different MiJhlenbach-Endzelin I 596 
f., Specht Dekl. 85, 132. 
Page(s): 349-350 

Root / lemma: gal-2 

Meaning: to call, cry 

Material: 1. Cymr. ga/w'caW, shout, cry, subpoena, send an invitation to court, summon'. 

Middle Breton ga/u 'caW, appeal; claim, summons; plea' {*ga/-uo-), Middle Irish ga//lan\e, 

glory, honor ' ( *gal-no-s, covered only doubtfully), probably also ga/Z'swan';
```


## [2026-09-06T15:39:11.603Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"^(gog|kake|kaka)\" AHD_watkins1985.txt | head; echo ===; grep -n -i \"gog-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:39:11.657Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T15:39:16.149Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29588,29602p' POK_full.txt; echo \"=== AHD gog\"; grep -n \"gog\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:39:16.222Z] TOOL RESULT

```
probably as "the swelling, the swollen', compare russ. uditb or udetb "to bloat, bulge, 
swell', also perhaps the Volscan FIN Oufens, Ufens. 

References: WP. 1111, Trautmann 334, Schwyzer Gr. Gr. I 518. 
Page(s): 347 

Root / lemma: gag- gog- 

Meaning: a round object 

Note: word the Kindersprache 

Material: Isl. Aa/ra "cake', Norwegian and Swedish /ra/ra "small, round and flaches bread', 

Danish kage " cake' (Germanic *kakan-), wherefore the diminutive Old English cicel, cycel 
=== AHD gog
```


## [2026-09-06T15:39:22.177Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gag-\" AHD_watkins1985.txt | head -20; echo \"=== cake\"; grep -n -i \"\\bcake\\b\" AHD_watkins1985.txt | head -20; echo \"=== cookie\"; grep -n -i \"cookie\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:39:22.249Z] TOOL RESULT

```
573:[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE. 2. Middle Dutch koeke, a cake: cooky. 3. Middle Low German koéke, cake: COCKAIGNE. 4. Old High German kuocho, cake: KUCHEN, QUICHE. [In Pok. gag- 349.]]
=== cake
573:[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE. 2. Middle Dutch koeke, a cake: cooky. 3. Middle Low German koéke, cake: COCKAIGNE. 4. Old High German kuocho, cake: KUCHEN, QUICHE. [In Pok. gag- 349.]]
709:mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
832:pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
860:plat-. To spread. Extension of pele-?. 1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: rLAT!; b. Old French flater, to flatter: FLATTER!. 2. Suffixed variant form *plad-yo- in Germanic *flatjam in Old English flei(t), floor, dwelling: FLAT?. 3. Basic form *plat- in Germanic *flathd(n), flat cake, in Late Latin
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
=== cookie
```


## [2026-09-06T15:39:33.838Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 incoming/BQT/BQT_v3_pages.txt; echo ...; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3; grep -c \"\" incoming/BQT/BQT_v3_pages.txt; echo ===V4; grep -n \"\\[pdf page\" incoming/BQT/BQT_v4_pages.txt | head -3"
}
```


### [2026-09-06T15:39:33.931Z] TOOL RESULT

```
Exit code 1
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
...
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
51425
(eval):1: ==V4 not found
```


## [2026-09-06T15:39:34.478Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"376\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:39:34.529Z] TOOL RESULT

```
4101:      >rd>kwy VJ 99, 142, 376, 383, BSTBL, Padm. 23,          ayat Cyt-) ©<*a-gata      ©intrans. v.; pt. st.
4870:376 »ykwn(w)     B, M, S              ^bjU^JbjU                        az ©ob. -y «=**zh
6290:       GMS 1376; Tales. 475.19, ZTmn
7453:      VJ 73, 106, 207, 1376; AVS 98                           1285 'prt'k B                                    J&kfifjr
7749:1376 »pw5pn    B                           J^^^^               (o)pu patzman
9204:1881 >wy>yz- S                                                     Hen. JRAS 1944, 143.18; GMS 376, 263n 1; AVS
10614:      0<?)make return                                            2376 *zyy my8 S                                      jJjl(,
11304:           GMS 376                                                     S W, TPS 1994, 179
11660:       MDii pll4n20, /?r*y                                             TSP  22.18 n p235; Hen. Texts. 376 n 1; Gersh.
12498:     GMS 376, 483                                              diamantine
13366:                                                                     3376 cywnd       M =* cyw'nt
13803:     GMS 430, 1331-6; VJ 290, 376; MSP bl2, 54,                3524 dbz-      C =» 6Pz-
14404: 3760 Syn'pr'st M, S                      ^U ^jf ^ jU j
14412: 3761 5ynJk B                                          ^
14417: 3762 6yn}r M =* Syn'r                                            STii 3.7
14418: 3763 Syn'rk'h S                                     ^j^     3775 SynfVS M                              J^ *jiJ 'tri-* C^
14422: 3764 Syn'rt'wspyh M              ^u ^LJT jlf jujf           3776 Synh      B, M, S                                       j*-' w
14430:3765 5yn>rtwspy) =» 8yn>rt>wspyh                                    pl83; MSP p45;Synmzt)yzm pYy "the god of
14431:3766 8yn>y B                                   vk>tf«J«*J           Mazda-yasna religion", Sund. Liste 1994, 459
14436:3767 6yn>yk M, S            '         yi> ^         ***jf
```


## [2026-09-06T15:39:41.324Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"branch\" SOD_pages.txt | head -30"
}
```


### [2026-09-06T15:39:41.403Z] TOOL RESULT

```
24412:%        parsa ?, parsa ©<Av. pdrdsu ©ace. f.                           branch
30087:      TSP 13ii 15 apud. S W, IIJ 1976 p55 n p615                            branch
30585:         branch
30786:       Mack, n p51-8;" mussel" GMS 113, 266                           branch
37799:branch 7215, 9148, 9311, 9377               Buddhist law    3596                   calm     1941, 7813, 10179, 10422,
```


## [2026-09-06T15:39:42.071Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"^\\s*[0-9]{3,5} (sn|Sn|šn)k\" SOD_pages.txt | head -20; echo ===; grep -n \"snk\\b\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:39:44.003Z] TOOL RESULT

```
Exit code 1
29238:                                                             8857 snk1 B, S                             ^X
29249:                                                             8858 snk2 =* snk>
29270:                                                             8863 snk'yn'k B
29284:                                                             8866 snks}>r B              (^/jujL<£JJ£^;)<>Jtj.> jjy
29305:8868 snksV =* snks'r
(eval):1: == not found
```


## [2026-09-06T15:39:49.306Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"(^|[^0-9])(7215|9148|9311|9377) \" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:39:49.352Z] TOOL RESULT

```
24410:                                                                  7215 prsnx(y)   M                            ^V^^^^
30085:                                                                       9148 s'yh M
30579:9311 snx M                                                              s(s)rfaz,
30783:                                                                 9377 sx1 C                                        <^U
37799:branch 7215, 9148, 9311, 9377               Buddhist law    3596                   calm     1941, 7813, 10179, 10422,
```


## [2026-09-06T15:39:50.025Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==443{print}' SOD_pages.txt | head -40"
}
```


### [2026-09-06T15:39:52.086Z] TOOL RESULT

```
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
```


## [2026-09-06T15:40:01.159Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n=NR; c+=gsub(/\\n/,\"\\n\"); if(!seen && c>=30579){print \"leaf\",NR; seen=1}}' SOD_pages.txt | head -2; echo ===; awk 'BEGIN{RS=\"\\f\"} NR>=443 && NR<=445 {print \"----LEAF\",NR\"----\"; print}' SOD_pages.txt | grep -n \"9311\" "
}
```


### [2026-09-06T15:40:02.722Z] TOOL RESULT

```
leaf 444
(eval):1: == not found
```


## [2026-09-06T15:40:05.285Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==444' SOD_pages.txt | sed -n '1,10p'; echo \"......\"; awk 'BEGIN{RS=\"\\f\"} NR==444' SOD_pages.txt | grep -n -A8 \"9311\""
}
```


### [2026-09-06T15:40:06.917Z] TOOL RESULT

```
                                                                                                                         376


 Silt—

                                                                  9320 sryw B, S                                          ^
           year B-8 R4 B-4 R2 B-3, 2
          MDii                                                          saryu ©Khot. sarau; MP sagn Parth. sarg;
 9309 snt-      C                                        d^jj             Khwar. srY\ <*sarYawa ^srwy
                                                                        lion
......
22:9311 snx M                                                              s(s)rfaz,
23-                                                                        wine cup srafz
24-                                                                                  ?    ? ©MP lsfrz-y Heb. sprzyyri
25-                                               ^■Lt* i4**-iZ'
26-         sanx (sny) ©<IE fcank ©pi. -r =»prsnx(y)
27-                                                                        Sogdica. 31, lib, 33.11b
28-         branch
29-                                                                  9323 srwy M, C                              (c^)jU o^
30-         Frag. Len. pl09; Snxyt, GMS n 2, 1142
```


## [2026-09-06T15:40:15.945Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T15:40:15.998Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-06T15:40:16.118Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls ocr/ 2>/dev/null; ls ocr/BQT 2>/dev/null | head -40"
}
```


### [2026-09-06T15:40:16.174Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1275.png
1275.txt
1294.png
1294.txt
1294.vision.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1453.png
```


## [2026-09-06T15:40:18.577Z] TOOL CALL #29: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT | grep -E \"^(1219|1280|1564|1572)\" "
}
```


### [2026-09-06T15:40:18.681Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:40:20.967Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1219 --image 2>&1 | tail -40"
}
```


### [2026-09-06T15:40:29.030Z] TOOL RESULT

```
و بش وباین‌می بجی بای ۳۳۶۱ ۶4 ی | واروبی است ماد کماء (۲ ) خشك و آنرا
هم مده است. ظاهر1 تصحیف خوانی شده‌باشد., 9 ۱
ال اعلم ۰ بعیرازی روشنك خوانند و معر ب. آان شاطل

است .
شا بور گان ؟ - با رای قرفت‌بروزن فا ۷
آسودکان ؛ فولاد معدلی راکونبند و معرب آن شاخ < بکون خای نقطه دارءچند
شابورقان احت. معني دارد :
(۱) چك: وها.. () چش: کمای .
۹ - رك: خسرو وشبدرین نظامی چاپ ارمفان ص 4۸ ۵۵ :۵۸ ۹۲۷۹۱۷ ۰۹۵۱۹4
۳۲ - مصحف #شابورد» (.م.) ۰ ۳۴ - معرب آن شابورقان 3« دزی جاص4 [ هرد
* شابورن < شابرن . ایا شابو رگان ۳ شابرن 9( ۰ شابهار در ادییات
پارسی بعنوان تام دشتّی در تاحیهة کابل آمده :
با هن بشابهار بهم بود چاشتگاه ماه من‌آنکه رشغك برد زو دوهفته ماه
گفت این فراخ پهنادشت گشاده چیست ؟ گفتم که عرضه گاه شه بیعدد سپاه .
«فرخی سیستالی ۳4۵ ور4: تاریخ بیهقی‌س ۲۵۵ ۰
«رچند بمید نیست که در ازمنهٌ قدیم دربن دشت بتخانه‌ای بوده باشد ولی ماًغذی برای
این اسناد پافته نشد وممکن است «شابهار» را بقیای «لوبپار» ساخته باشند . ر4: فرهنگه نظام .
‎٩‏ - رك: ساتل . ۷ - هندی باستان - ۲02می ( شاخه )۰ پهلوی 5321

وی ارمنی987 *کردی ع اففانی 525 » بلوچی 5220 ( قرن » شاخ جانور)

و5035 .(عاخة درخت) » وخی 51017 ,سریکلی 51005 (شاخه) »ییزوخی 53040,سریکلی 780

(«جموعةٌ شاخه ها) «اسشق ۷۹۹ *.

بقیه از صقحهةٌ ۱۲۱۸

(پس) ۰ 3 ۳ سر شاه در سلله سامانی هن بدین نام پادشاهی کرده‌اند:شایوراول پس اردشیر

۱ ۳.) #شاپور دوم (ذوالا کتاف) یس هرمزدوم (۳۹۰- اخشد)6) ۰ شاپور سوم پسرشاپور

دوم ( ۳۸۸-۳۸۵ م .) ر4:

۰ ,ده طععندط) مهم داه‌هاکننتا مهد طاعو 3710 2.۷۰

6۰ بو ,1937 ,[6ل8۸
ورك : کربتشن . ساسان . فهرمت .
```


## [2026-09-06T15:40:37.871Z] TOOL CALL #31: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/1219.* "
}
```


### [2026-09-06T15:40:37.912Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 393921 Sep  6 11:40 data/verification/sources/refs/ocr/BQT/1219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3603 Sep  6 11:40 data/verification/sources/refs/ocr/BQT/1219.txt
```


## [2026-09-06T15:40:39.881Z] TOOL CALL #32: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1219.png"
}
```


### [2026-09-06T15:40:40.436Z] TOOL RESULT

```

```


## [2026-09-06T15:40:40.434Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:40:59.622Z] TOOL CALL #33: Bash

```json
{
 "command": "cat > data/verification/sources/refs/ocr/BQT/1219.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, p. 1219 — read from the page image]\nHeadword (right col., bottom of left col.): شاخ ۷ - بسکون خای نقطه‌دار، چند معنی دارد:\nMo'in's etymological footnote 7 (bottom of page):\n۷ - هندی باستان çâkhâ (شاخه)، پهلوی shâk، ارمنی çax، کردی shâx، افغانی shâx،\nبلوچی shâh (قرن، شاخ جانور) و shâx (شاخهٔ درخت)، وخی sholx، سریکلی shox (شاخه)،\nیزغلامی shâo، سریکلی xâo (مجموعهٔ شاخه‌ها) «اسکن ۷۶۶».\n[i.e. Mo'in equates NP شاخ with Old Indic śākhā and Pahlavi šāk and lists Armenian\nçax, Kurdish/Afghan/Baluchi/Wakhi/Sarikoli/Yazghulami cognates — a cognate list, not a\nstatement that Persian borrowed the word from Sanskrit.]\nEOF\necho saved"
}
```


### [2026-09-06T15:40:59.712Z] TOOL RESULT

```
saved
```


## [2026-09-06T15:41:00.303Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1572 --image 2>&1 | tail -40"
}
```


### [2026-09-06T15:41:07.839Z] TOOL RESULT

```
کاك - بسکون کاف . بسنی‌مرد باشد |[ . :
که متا ند ۱ ۱ 7 - وقرص ماه را نیز کوبند که ماه شب چهارده

درمقابل زن است٩‏ - و بمعنی‌مردم ۵5 آدمی
باشد - و مردمك چشم هم هست و جربی انسان باشد 8 - ونام قلعه ایست ازقلاع آنربایجان -
الم خوانند ۴ - وهرچیز خشك راکوبندعموم | وبمعنیکاواك ومیان خالی‌همآمده است۹ .
وگوشت قدید را خصوصاً - وآدمی وحیوانی که کاکا - بپردوکاف بالف کشیده . برادر
یار لاغر و ضمعیف شدء باشد ۴ - ونان خشك | کلان را کوبند ۷ - وغلامی قدیمی ۸ که در
۱- «کاك . بلفت ماوراء‌النپر مرد باشد ۰ قریع‌الدهر کوید:
همه چون غول بیابان همه چون مار صلیب
همه‌ید زهره‌بخوی وهمه (بومرء نجدی همه. دهخدا) چون کاك غدنك».

لغت فری ص۲۵۱ > واگر اصل «بومرء‌نجدی» (شطان) باشد ( ر4: لغت نامه : آبومرء نجدی)
آنگاه «کاك غدنگه > هم باید اشاره یکی باشد . ۴ - «كيك وکاك. مردمك چشم‌بود.»
رك : لغت فری ص ۷ ونیز بمعنی سرزبان آمده . رك: لغت فرس ۰۳*۱

۴ - دوش چون‌احمقان زخالهٌ خوش سوی کوهر ستی کاك شدم
هیج القصه تا بگردن و رش همجچو جولاهه درمغاك شدم.
آنوری آبیوردی درهجوزيك لاغری « جهانگیری..
۴ - هرن «کا4» بدین معنی را ازلغات متمار ازآرامی میداند «اسفا ۲:۱ص۹*درآرامی

[ ۹۹۵ ۵ ها ۷ معرب آن كمك (] ۳۲۵۲۵۵۷۷۵۴۸67,۳.7 ,51440) درزبانهای 1 لمانی
وانگلیسی بگفتةٌ لیتمان 36615 و 28165 باكاك و کعکه و كمك فارسی وعربی بیکی‌است. : اها
چون در زبان یونانی 8۳88619 و در قبطی 1216 وجود دارد » میتوان گفت که این کلمه اصلا از
سرزمین مصر است «هرمزدنامه ۱۳۳ بنقل از لیتمان» وآ ترا درمشهد «قاق» کوبند .جوالیقی کوید
(س ۹۷؟) : ۶ الكعك . نان خشك . لیث کوید :گمان برم که معرب است و اشادکرده ::

با حبذا الكعك بلحم مثرود و خشکنان وسویق مقنود .>
8 - نداخت بهره ز علمی که اوج منبر جت
بزرد روبی موسوم ازان قبل شد کاك .
رضی‌الدین نیشابوری « جهانگیری ی
‎٩‏ - در مازندران باین هعنی مستعمل است « فرهنگه نظام > .
۲ - در فاری 6860 ( برادر ) » در طبری 8388 ( پرادر ) » در مازندرانی کنونی

4 و 8۴82 (برادر) « واژه نامه ۹۵۰ > اما درکردی 86 بمعنی پدراست « ژابا س 2۳۳۸

و قی +کاکو ,کاکویه .۸ - باین معنی ترکی است . در جفتایی « کاکا > بمتتی للم
واتاييك و مربی خانزادگادت « تورك لغتی . قدری». :ْ
```


## [2026-09-06T15:41:16.663Z] TOOL CALL #35: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1572.png"
}
```


### [2026-09-06T15:41:17.272Z] TOOL RESULT

```

```


## [2026-09-06T15:41:17.269Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:41:46.416Z] TOOL CALL #36: Bash

```json
{
 "command": "cat > data/verification/sources/refs/ocr/BQT/1572.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, p. 1572 — read from the page image]\nHeadword: کاک - بسکون کاف. بمعنی مرد باشد که در مقابل زن است ۱ - و بمعنی مردم که آدمی باشد -\nو مردمک چشم هم هست و چربی انسان الْعین خوانند ۲ - و هرچیز خشک را گویند عموماً و گوشت\nقدید را خصوصاً - و آدمی و حیوانی که بسیار لاغر و ضعیف شده باشد ۳ - و نان خشک ... و معرب آن کعک۴ است ...\nMo'in's footnote 4 (the etymological one):\n۴ - هرن «کاک» بدین معنی را از لغات مستعار از آرامی می‌داند «اسفا ۱:۲ ص ۶»؛ در آرامی\n[Aramaic word printed in large Semitic type, = gaggā / ggʾ] ، معرب آن کعک (Siddiqi, Fremdwörter, p.71)\nدر زبانهای آلمانی و انگلیسی به گفتهٔ لیتمان Keeks و cakes با کاک و کعکه و کعک فارسی و عربی\nیکی است، اما چون در زبان یونانی kakeis و در قبطی kake وجود دارد، می‌توان گفت که این کلمه\nاصلاً از سرزمین مصر است «هرمزدنامه ۱۳۳ بنقل از لیتمان»؛ و آنرا در مشهد «قاق» گویند.\nجوالیقی گوید (ص ۲۹۷): «الکعک، نان خشک. لیث گوید: گمان برم که معرب است ...»\nFootnote 7 (کاکا): در فارسی kâko (برادر)، در طبری gaga (برادر)، در مازندرانی کنونی gâgâ و gegâ (برادر)\n«واژه‌نامه ۶۵۰»، اما در کردی kek بمعنی پدر است «ژابا ص ۳۳۸».\nEOF\necho ok"
}
```


### [2026-09-06T15:41:46.467Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:41:48.543Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=84 && NR<=87 {print \"--- leaf\",NR\" ---\"; print}' SDQ.txt | grep -n -i -B3 -A6 \"ka.k\\|Kuchen\\|Kek\" | head -60"
}
```


### [2026-09-06T15:41:50.182Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:41:53.844Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ka'k\\|kaʿk\\|ka.k\\b\" SDQ.txt | head -20; echo \"=== grep kak\"; grep -n -iE \"k[aā][ʿ'’]?k\" SDQ.txt | head -30"
}
```


### [2026-09-06T15:41:53.976Z] TOOL RESULT

```
=== grep kak
```


## [2026-09-06T15:41:56.488Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c SDQ.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR\" leaves\"}' SDQ.txt; awk 'BEGIN{RS=\"\\f\"} NR==86' SDQ.txt | head -40"
}
```


### [2026-09-06T15:41:58.397Z] TOOL RESULT

```
225642 SDQ.txt
143 leaves
t),  das  v  in  .äc  (=  cciQoc)  u.  s.  w. (Vgl.  Fraenk.  108,  233  u.  FraenkMß.  11  und  Nöld. Mand.  Gr.  71  Anm.  2).
(b)  durch  das  Bestreben  bei  Fremdwörtern,  sie  deutlich auszusprechen,  wodurch  mancher  einfache  Laut  zum emphatischen  wird.  Dieser  Umstand  macht  sich  im Anlaut  besonders  bemerkbar  beim  Antritt  des  arabi- schen Artikels,  wo  man  ja  bestrebt  ist  das  Verschwinden des    leichten  Lautes   zu   vermeiden.     Dieses    geht  aus
der  Warnung  Farrä's  (G.  106)  hervor:  ^^i>f^.l^*,  0!r^^"*'' Q^j^J!  Ji-äj"b5^  o'o'^'-5  O^i)^'  ^   'li^kj).      Das    c    in    Ji^c^
1)  Die  beiden  Formen  bildeten  eine  Streitfrage  schon  zwischen Abu  'Ali  und  Siräfi  (s.  oben  S.  41-42).  Vgl.  noch  Mittw.  119  Anm,  1 und  Hamza:  Annal.  158.
2)  Vgl.  Fraenk.  190  u.  Gesen.-Buhl,  S.  6172.  [-^^„ch  im  Syri- schen kommt  die  Form  mit  i  neben  der  mit  c  vor ;  erstere  ist  aus dem  Griechischen,  letztere  aus  dem  Hebräischen  entlehnt.  Es  wäre für  das  Arabische  noch  genauer  zu  untersuchen,  ob  sich  die  beiden Formen  nicht  jede  an  ein  besonderes  syrisches  Vorbild   anschließt.  L.]
—     70     —
sclion  bei  Härit  b.  'Abbäd  (Snasr.  273  Vers  5  v.  u.), Umaiya  b.  abi  's-Salt  {U-amhA^.  S.  213),  Mälik  b.  'Urwa (Harn.  Buht.  121),  ist  wohl  kein  echtes.  Man  über- nahm wahrscheinlich  das  persische  X^l  ^),  welches  zu *al-laskar  werden  mußte;  dies  konnte,  mit  dem  Weg- fall des  einen  /,  wie  aJ-nslar  ausgesprochen  werden, und  aus  dieser  Form  hätte  sich  dann  ^aWasliar  und al-askar  entwickelt.  iüiJÜ  (allgemein  für  echt  gehalten) „auf  einem  Berg  gelegenes  Fort"  kommt  schon  bei dem  in  al-Hira  lebenden  Dichter  Laqit  b.  Ya'mar  in  der
Pluralform  «JL5  vor  (IQutKsws.  98  Z.  8— 9)  und   zwar in  auffallendem  Zusammenhang  mit  Färs : ^1  <S^ll\  iiXi]  ^J^Ji  J)j»-\
Lati-äJi  ^Oy  p^-*==-  t^-*-^^  er
Das  Original  des  Wortes  ist  das  persische,  oft  als Ortsname  vorkommende  ot^5  „auf  einem  Berg  gele- genes Fort  oder  Dorf",  woran  das  o  erst  später  an- getreten ist  -).  Nach  dem  armen,  kholalh  muß  die alte  Form  *kaläJc  gelautet  haben,  woraus  regelrecht das  neupersische,  in  den  zahlreichen  zusammengesetzten Ortsnamen  von  Mäzändärän  als  zweites
```


## [2026-09-06T15:42:02.226Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==87' SDQ.txt"
}
```


### [2026-09-06T15:42:04.311Z] TOOL RESULT

```
 Glied  vor- kommende ^^  (käla)  ^)  entstanden  ist.  [Hier  wäre also    auch   ein   p   an   ein  persisches  Wort   angetreten.
1)  IQutAk.  532;  Ibn  Duraid  (G.  105).  Daß  die  Perser  das .jCjm«.£  von  den  Arabern  als  .jCw^i  übernahmen  (Fraeak.  239),  kann schon  wegen  des  (ji,  nicht  richtig  sein.  Das  .^m*.£  ist  auch  im  Per- sischen tatsächlich  aslcar  gehlieben  und  nicht  etwa  *laskar  oder  *askar geworden.
FN.  (s.  V.)  will  Ji^li  aus  ^^j  „Stück"  ableiten.  Wenn  der Übergang  der  Bedeutung  „Stück",  „Teil" ;  „Abteilung"  —  „Truppe" auch  nicht  unmöglich  ist,  so  bleibt  doch  die  Endung  unerklärt.
2)  Das  arab.  ö  hat  also  nichts  mit  diesem  o  zu  tun,  wie  Fraenkel S.  237  annimmt.
3)  Vgl.  Bemerkungen  von  Andreas  über  ^ÜA^b'  MVAsG.  1807, Heft  I,  S.   124  flg.;  Schwarzl.  130  u.  133.
—     71     —
Die  Gründe  für  die  Entstehung  dieses  c.  sind  nicht  mit Sicherheit  zu  erkennen.  Vielleicht  ist  es  durch  ^  be- einflußt.   L.]
Das  c  in  i^xS^  ist  schon  im  aram.  JIä^.o  (p.  ^\^)  vor- handen. J^*J  (eine  jüngere  Entlehnung)  ^)  ist  womöglich von  den  Persern  selbst  mit  c  geschrieben  worden,  um S^  {^3t.l)  „Rubin",  welches  Wort  übrigens  ins  Arabische übergegangen  war,  von  S^  „rot"  zu  unterscheiden"^).
6.  Persisches  i_j  wird   durch  o  oder   auch  durch  v-j
wiedergegeben:  ^j^^li  (=  p.  ij^J^S),  ^^i  (=  p.  _^^J),  (J^^J> neben  /  ijLj  (=  mp.  parvänak  >  ^^i^^-j) ,    «Ai^-i   neben   uX.i^
(=  p.  cXi-j  „Glanz  des  Schwertes  u.  s.w.").
7.  Eür  persisches  o  erscheint  auch  _b,  vielleicht  ein
1)  Das  Wort  fehlt  bei  Gauhari.
2)  Einige  schreiben,  nach  Gauhari  (s.  v.  Xäa«),  in  medizinischen Schriften  JCäao  für  .Äx*«,  um  es  (wenn  ohne  Punkte  geschrieben)  von jj^nXi  unterscheiden  zu  können.  [Man  darf  jedoch  nicht  vergessen, daß  die  Aussprache  satar  vorgekomme
```


## [2026-09-06T15:42:13.036Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/PLA/; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['PLA'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T15:42:14.811Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
{
 "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
 "edition_found": null,
 "kind": "archive_djvu",
 "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)",
 "identifier": null,
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"
 ],
 "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).",
 "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "notes": "Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "first_printed": 1,
   "last_printed": 300,
   "pdf_offset": 0,
   "lang": "deu+ara"
  }
 ],
 "cites": "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
}
```


## [2026-09-06T15:42:17.262Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==248' incoming/PLA/PLA_pages.txt | head -50"
}
```


### [2026-09-06T15:42:20.501Z] TOOL RESULT

```
kaSni                                                                             233                                                            kalam_
  .                  z                                                                       .£              PR
GEST            kaönl:           "hungrig                   sein"!          7 pers.               gurusne,
                                                                                                         as) goSne mp.                             EIAN
           gursnag                >rur guänag                     1

                                                                                          I _                                               BP}
A 7          kack:          "Biskuit,                  Torte"           <      pers.     JYkäk 2 ‚ syr.                    K&%o (pers. SIE)               3,
           dtsch.           Kuchen             /Keks,             engl.        cake    pers.           käk           4,

       ._/                                                                                                   .
Aa) - kufta:                     "Fleischbällchen,                             Kloß"          pers.     Ci                küftan    "schlagen,
           klopfen,              hacken"               Kg mp.Naı9 koftan,                      kob     ®,

                            u                                                                                    7
a2 - kafkag:                         "Ranunculus,                     Ranunkel;          Hahnenfuß"                  ‘.

       /
ae -              safikaf = kafkaf a. v.

Je                    kul-käsni:                      s.        käsnl     ®.
       _                                                                                                         / kolbe <Tmp. 983 kurpak,
—Lb_-           kulbak:              "Hütte,               Zelle,         Keller" <           pers. ab
           s.    qarbaq,              karbag               u.     karbaq.         9,


_AZb"-
      d, 7              x
                 kol5ikar:                  "Rosenzucker"                      pers.
                                                                                         10 eg pers.                      Yan
                                                                                                                           ygol "Blume,     Rose
                                                                                                                                                   n
           mp. Ip gul <T aw.varada.-                                      aram.        Lw.   wrd”     1,             pers._& Sikar s.              Sikar
           ar.     sukkar.


                kalafs           = karafs                  q. v.

       _
OJE”-            kulkün:              "wie            die        Rose"      pers.            ©,       gulgün s.               gul    in kolsikar          u.
           gün     in       asmänfün.                  12,


ri         kalam            =   karam            q.        v.




 1.    Mackenzie                 s.       v.
 2.    Wahrmund                 s.    v.,        TaCalibi                figqh    al-luga      s.     v.,        al-MuCarrab           s.   v.
```


## [2026-09-06T15:42:26.300Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==248' incoming/PLA/PLA_pages.txt | sed -n '50,90p'"
}
```


### [2026-09-06T15:42:28.213Z] TOOL RESULT

```
 2.    Wahrmund                 s.    v.,        TaCalibi                figqh    al-luga      s.     v.,        al-MuCarrab           s.   v.
 3.    Brockelmann                    Ss.      v.
4.     Littmann                 s.    v.
 5.    Chista           Bd.          10     S.        1191.
 6.    Mackenzie                 s.       v.
 7.    Löw       s.     v.
 8.    ebda.
 9.    Nyberg           Bd.          II     s.        v.
 10. Muhit              s. v.
 11.       Nyberg           Bd.       IIs.v.
 12,       Addai        Scher             s.     v.
```


## [2026-09-06T15:42:32.634Z] TOOL CALL #44: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1280 --image 2>&1 | tail -30"
}
```


### [2026-09-06T15:42:39.574Z] TOOL RESULT

```
آی از آن چون چراغ پیشانی آی از آن زلفك شکت ومکت.
« لغت فری ۶4۸ ۰ ۰
۲« عکاعك . ۴ < اهکفت (همم.) ‏ کردی 51016۷۷۲ ,2906201 (غار)

«اسشق ۰.۷۸۷ ۴ <شکوفتن <- شکوفدن (ه.م.) پهلوی -512۳۵]1 ( شکوفه داد )

« اوتوالا ۱۹۶* و قس : بشکوفه . ۶ اسشق ص ۱۷۵ از - 58۳۷0 ( زدن » فغار دادن ) »

بهودی --فارسی 8185801۵]128 » ساسکریت ‎٩۹۴۷۷-۵11‏ و1) 516101180 (جدا کردن »

شکافتن) وريشةٌ 51600 هم مبدل - 810 است . قس: پارسی میانه وفارسی ( دری ) 16۵1180

( زدن ,کوببدن).ريشه اوستائی 51۳2012 ۶ بارتولمه ۱۵۸۹ رك : نیب رکه ۲۱۹ ورك: شگفت.

ه - ر4: شکفتیدن . ‎٩‏ - ر4: شکفتن . ۷ - ر4: شکوفه .
۸-ظ . مصحف شكنك ( بامغفف آن ) .

۹ -ساسکرت 5.313 . رك: ما للهند. بدرونی.صس ۰.۳۵۰

۴ ساسکرت لاف او (نکه , قطمه) و 51121818(/8 ( بقطسات تقسیم کردن )

«وبلیامز ۱۶۶۹ :۱و۲ .۰

* شم - بکر اول وفتح دوم (درلهجةٌ مرکزی) ۳ اشکم (ء.م.) ؛ آن جزه از بدن

که ممده و روده ها درآن واقع شده‌اند » بطن :

توان بلق فروبردن استخوان درشت(درست) ‏ اولی شکم بدرد چون بگیرد اندر تاف.
«کلتان 4۳ درون» ادرون هرچیز.
```


## [2026-09-06T15:42:45.100Z] TOOL CALL #45: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1280.png"
}
```


### [2026-09-06T15:42:45.568Z] TOOL RESULT

```

```


## [2026-09-06T15:42:45.566Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:43:04.102Z] TOOL CALL #46: Bash

```json
{
 "command": "cat > data/verification/sources/refs/ocr/BQT/1280.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, p. 1280 — read from the page image]\nHeadword (left col., bottom): شکله - بکسر اول و سکون ثانی و فتح لام، آلچه از جامه و امثال آن\nکه در جایی بند شود و پاره گردد - و پارچه‌ای را نیز گویند که از سر هندوانه و خربزه به کارد\nبردارند ۱۰ و آنرا به عربی قوارةالبطیخ گویند؛ و به فتح اول هم گفته‌اند.\nMo'in's footnote 10: ۱۰ - سانسکریت shákala (تکه، قطعه) و shakalaya (به قطعات تقسیم کردن)\n«ویلیامز ۱۰۴۶: ۱ و ۲» [= Monier-Williams p. 1046].\n(footnote 9, for شککال: سانسکریت Shakakâla)\nEOF\ntimeout 900 python3 tools/ref_page.py BQT:1564 --image 2>&1 | tail -35"
}
```


### [2026-09-06T15:43:11.994Z] TOOL RESULT

```
کاسجو ل4؟ - بنکون ثاك و جیم موزه‌دوز ندبآآن پیوند(۲) کنند؛ وبعضی کوبندموی
بوا و کشده ویکاف زده ۰ بمعنی‌کاسج است کدیار | سبلت خوکست‌و] نرابمریی‌هلب‌خوانند(۳)؛وبعضی
پشت کاان تیرانداز باشد . کفته‌اندموی‌سبات روباماست؛وآ نرا کاسموی
کاه ۴ - بنتح نات و سکون کان ,۱ با زیادتی تحتانی درآخر نیز میگوبند
مصفر کاسه باشد. کاسن < پروزن دامن » نام قربه‌است از
کاسگینه * - بروزن آبگینه . مرشی ۱ فرای سرقند ‎٩‏ :
باشد سبز ارنگه بسرخی مابل و آنرا سبزه نیز کاستی - بفتخ ناك‌ونون بتحتانی‌رسیده.
گونند . تاجی بر سر دارد ماتند هدهد و بعربی مردمیرا کوبند که بغربهٌ کاسن مشویند که
شفراق خوانند . قریه‌است از قرای سمرقند ۸ - ویسکون‌ئالت,
() خم۱ :ده (۷) خم۱ : ضصب .
(۳) چش : - موی سبلت ... خواند .
۹ - اسم مفعول ازهکاستن» . ۴ - کا-جوك :
بروی صف شده از زخم پاسج همه اعضاش همجون پشت کاسج.
: تزاری قپستانی « فرهنگه نظام >.
۴ -رك :کاسج :
از آن پیجد دل من همجو ماری که‌هجرانش براو چون کاسجوك است.
مولوی « فرهنگه نظام **
۴ - مصفر «کاسی >. 8 -_قی : کاسانه . ۹ ۶ کاسموی, موی خوكد
بو د که کفشگران بررشته بندند . فرخی (سیستانی) کوید :
چو کاسموی گیاهان او برهنه زی رک چو شاخ بید درختان او تهی از بار.»

2 لغت فری ۵۱۹ -
رك : کلی. آنچه درهندوستان رواج دارد آنت که موهای خوك را دسته ساخته کفشگران‌برای
جلای سقرلات و مخمل وچرم یش خود نگاهدارند و همچنین زرگران برای جلای .طلا ونقره .

۰ فرهنگه نظام > ۷ رك: کاس. ۸ -کاسن بفتح سین » ازقرای نخشب بماوراءالنهر
است «معجم‌البلدان» و موْلف با «کاسان» (ه.م.) خلط کرده است .

۵ کاستن ( بفتح چهارم) <* کاهیدن.پهلوی ۳31128 ۰ ۴30181188 بقول‌دارمستتر
۰ تبعات ج ۸۷ > وهرن «اسشق ۸۳۵؛از ربشهٌ اوستابی -885 891-0 ( ۳ که[ كوچك ]|
فارسی ) نشأت‌بافته, هوبشمان آنرا از مصدرقدیمی 8525131838 . #2511(نقصان ,خطا),110) 1280
از ربشهٌ - ۴2 . پپلوی 8588 مشتق میداند . در پهلوی 588121 ( کاسته ) و ۸331808
(کاهش) آمده که متعلق پريشهٌ پارسی باستان 1۴8 با ۴8 باشد ۰ هوبشمان ۸۳۵ >؛ کم کردن
و كوچك کردن چیزی .
```


## [2026-09-06T15:43:24.504Z] TOOL CALL #47: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1564.png"
}
```


### [2026-09-06T15:43:25.042Z] TOOL RESULT

```

```


## [2026-09-06T15:43:25.039Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:43:42.758Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > data/1564 2>/dev/null; cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1564.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, p. 1564 — read from the page image; headword کاسته]\nMo'in's footnote 5 (for کاستن):\n۵ - کاستن (بفتح چهارم) = کاهیدن. پهلوی kâhîtan ، kâhînîtan. بقول دارمستتر «تتبعات ج ۲ ص ۲۰۸»\nو هرن «استق ۸۳۵» از ریشهٔ اوستایی -kas ، kasu (= که [کوچک] فارسی) نشأت یافته. هوبشمان آنرا\nاز مصدر قدیمی kâshtan ، kâstî ، kâshtîh (نقصان، خطا) از ریشهٔ kâh - kâs، پهلوی kâs مشتق\nمی‌داند. در پهلوی kâstak (کاسته) و kâhishn (کاهش) آمده که متعلق به ریشهٔ پارسی باستان\nkad یا kah باشد «هوبشمان ۸۳۵»؛ کم کردن و کوچک کردن چیزی.\nEOF\nawk 'BEGIN{RS=\"\\f\"} NR==96' HUB.txt | head -50"
}
```


### [2026-09-06T15:43:44.845Z] TOOL RESULT

```
(eval):1: no such file or directory: data/1564
— 85 —
823. Xp. farrar deckt sich lautlich ganz mit zd. fravara-^
= phi. fratar. Vgl. oben Nr. 210 und 304, Fr. Muller,
WZKM. 8, 97.
824. Kurd. /(PTiistm etc. (mits!), Justi, kurd. Gram. p. 190.
Ueber afgh. prolgl vgl. Geiger, Etym. und Lautl.
des Afgh. Nr. 361. Danach ist das kurdisehe wie das
afgh. Verbum aus dera Persischen entlehnt. Vgl. oben
Nr. 578.
825. Np. fuTod = phi. frot ist aus *fravai- = sLp*fravatd
= skr. pravdid contrahirt. Bartholoraae*s Ansatz
eines arischen *prauUl ist falsch.
826. Np. firih 'viel, mehr = paz. freh 'more* (sup. frehest
'most' Shk. 245 = phi. frahist) lasst sich leider nicht
= zd. frayd (sup. fra^a^ zum Positiv pouru^ Viel")
setzen. Nur ein zd. *frahy& = ap. *frahy(l (als nom.
sg. masc.) wurde paz. freh = np. firih genau ent-
sprechen.
828. Nach N old eke bedeutet np. farydd ursprunglich
nur 'Geschrei* und erst secundar *Hilfe*; vgl. gr. lio^
und lioTjd^oog (np. faryod^ras)^ fioiid^siv. Die Bedeutung
'Hilfe' belegt Horn aus Abu Muwaffaq, sie findet
sich auch schon Min. cap. 2, 166 (o friyOS ne rased
*kommt nicht zu Hilfe', phi. frayOt Phi. Min. p. 16,
Z. 5).
829. Anders Mann ZDMG. 47, 705. Ich stehe auf Horn's
Seite, vgl. meine Etym. und Lautl. der osset. Spr.
Xr. 271.
834. Zum Suffix -zar in hdrzdr == phi. kdrJcar (so kann
doch ohne Weiteres gelesen werden, wie auch karJjar
oder kanzdr) = paz. karlzdr Min. Gl. 121 vgL Dar-
mesteter, Etud. iran. I, p. 296. — Xp. kOrcan =
paz. kdravdn Shk. 253 hat nach Ausweis von arm.
LW. karavan 'Earavane, Heerhaufen (bei Elise, Fau-
stus etc.) im Phi. karavan oder karuran (geschrieben
karupdn) gelautet, kann also nicht so erklart werden
wie Fr. Muller WZKM. 5, 354 thut.
```


## [2026-09-06T15:43:50.691Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==97' HUB.txt | head -60"
}
```


### [2026-09-06T15:43:52.615Z] TOOL RESULT

```
-^ 86 --
835. Np. Uastan *abnehmen, weniger werden' passt in der
Bedeutung trefflich zu zd. kasu-- = np. kih *klein*,
doch miisste, wenn etymologischer Zusammenhang
bestehen soil, kOstan aus alterem *kastan, kasil 'Ab-
nahme, Fehler aus *)castth und der Praesensstamm
kdh- aus phi. kos- entstanden sein. Es liegen aber
vor phi. kastak 'diminished, deficient' 61. and Ind. 195,
kahiSn 'decrease, decay* Phi. Min. p. 5, Z. 14 u. s. w.,
51, 2 — 3, Bdh. p. 27, 4 (*Abnahme') u. s. w., die auf
ein ap. kah oder kad als Wurzel deuten.
836. Np. kdStan (aus *kartan) *saen, pflanzen' gehSrt zum
praes. karad (3. sg.) = zd. karay^iti 'man saet, pflanzt,
baut an' (vd. 3, 4) ; dagegen kistan 'saen, pflanzen' zu
skr. karS, 3. pr. krHti pfliigt'. Vgl. ZDMG. 44, 558.
Zu ersterem gehSrt afgh. karql *ackern, pfliigen, saen'
(Geiger, Etym. und Lautl. des Afgh. Nr. 66 und 71),
zu letzrterem bal. Msay 'to cultivate'. Vielleicht ist
zd. karay- = np. Mr- = afgh. kar- der Causativ-
stamm der Wrzl. skr. kar'^), pr. 3. sg. kirdti 'aus-
streuen (auch vom Samen).
837. Np. kaft€i/a *spalten, graben ist schon bei Vullers,
Verborum linguae persicae radices s. v. mit gr. xdnsvog
sowie mit ksl. kopati graben zusammengestellt. Als
Praesens gibt Vullers kdbam^ kavam (arisclie Wrzl.
iap, kab oder kabh) und kafam (arisch kaph\ Sal.
Shuk. Gram. p. 56 nur kavam grabe an. Np. kaftan
spalten' ist das Causativum von kaftan 'gespalten
werden (Fird. I, 468, Z. 4), dessen Praesens nach
Vullers kafam (arisch kaph) lautet. Vgl. ia/'fissura,
ruptura'.
838. Np. kdm = afgh. kumai *Gaumen' ist schwerlich
identisch mit kam 'Wunsch, Wille'. Die germ.W5rter
fiir *Gaumen' setzen im Anlaut ein idg. gh, die irani-
schen ein idg. k voraus.
840. Dazu nach Geiger hsA, kdh 'frisches griines Gras,
das, wenn es nicht entlehnt ist, auf iran. *kah€h =
*) Besser: hari = idg. kor9 zweisilbig.
```


## [2026-09-06T15:44:00.084Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==206' HRN.txt | head -60"
}
```


### [2026-09-06T15:44:01.851Z] TOOL RESULT

```
— \Si -
826. ftHh viel, mehr.
aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
(Päz. freh^ frehest), ursprünglich freh^ vergl. freh[dätär
(AV.).
Die Aussprache ßrih (nicht fireh) bezeugen die
Keime der beiden bei Vullers s. v. mitgeteilten
Verse {bih und girih). Ich stelle das Wort zu den
von Andreas erklärten bih, kih, mih (No. 241).
827. ferl *lieb, schön .
aw. frya- geliebt, Freund*; ai. pnyä-,
828. feryäd *Hilfe; Hilferuf, Klage.
aw. fraöäia- ^Gedeihen, Förderung' (yt. 13, 68);
phlv. frayät bezw. fradät 'Hilfe*.
Die mittelpersische Bedeutung *Hilfe* findet sich
auch noch im Neupersischen, z. ß. AM. 43 Zeile 6, 82
Zeile 1 V. u., Öähn. I, 126 Vers Uli (NB. wohl un-
echter Vers).
LW. kurd. af/. feryad-, bei. paryat 'Geschrei* (199).
Anders Fr. Müller, WZKM. 5, 353.
829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
ßreftär, JTJKSnE^ (Jer. 20, 7).
ai. pra + [/"rep- 'anschmieren, betrügen', vergl. rip^
'Betrug, ripü' 'Betrüger ; phlv. freftan^ frepet^ f^^P^
frep(i)sn, freftär.
oss. d. fälewun, t. fäliwin 'betrügen* (271). Sar.
rof-am hat noch die Bedeutung 'beschmieren' bewahrt.
830. fe^, fuy 'Götterbild (Geliebter, Geliebte)', fuyistün
V
'Harem* (Sahn. II, 532 V. 198), fuyäk 'töricht', fuyvare
sprachlos, vergl. Fayfür (Seite 71 Note 1).
ap. baga- 'Gott*; aw. baya-; phlv. bag]baxt (ge-
schrieben baW) ; ai. bhdgha-.
Die echt persische Form hat sich im Np. nur in
Ba/däd erhalten, das / ist eine Arabisirung.
```


## [2026-09-06T15:44:05.713Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==207' HRN.txt | head -60"
}
```


### [2026-09-06T15:44:07.589Z] TOOL RESULT

```
1 85 —
K.
/,8:J1. (i)kär *Wcrk, Tlmt\
aw. kära- in käravaitl; plilv. kär; skr. -küra- *i:Iand-
limg, That\
Allgemein entlehnt.
832. (2)'kär 'Tliäter , z. B. in sitahkär, destkar,
ai. -kära- '-tuend'; plilv. -kär,
Vergl. np. gär (No. 884).
■ym, kärd 'Messer.
aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
kfntdti 'schneiden*.
kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
d. kärdtm, t. Mrdln 'schneiden'; bei. kärc^ kärca^
n. ßarca (195).
834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
phlv. kärejar (y. 11 (8)).
vergl. ap. kära- *Heer'; lit, käras 'Krieg'; ksl. kara
'Zank, Streit'; got. harjis 'Heer.
Das Suffix -eflr ist unklar. Im PehlevT lautet es
'jär, was nicht -cär gelesen werden kann; vergl.
dialektisch grl. käljär (Vullers), Kä§. K. kast^jori —
kistzär.
Fr. Müller (WZKM. 5, ;354) will dasselbe kär in
np. karwän 'Karawane' finden; Nöldeke (mündliche
Mitteilung) stellt hierher np. kärdär 'Vezir .
835. kästen Vermindern, verringern', Praes. käh-eni,
^ kahldefiy Icästi,
phlv. kahltan, kähet, kälünltan, käh{i)sn (Men. s. v.
khah"),
Wohl zu demselben Stamm wie aw. kasu-, np. kih
(No. 877).
y'836. kästen (Sahn. 111, 1544 Vers 842), kisten 'säen',
Praes. kär-em, kist,
g. kastmün,
aw. [/kars-f ya{i\lxarsti, vergl. karsosca frakäroyöis;
```


## [2026-09-06T15:44:15.716Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page 6[5-9]\\]\" incoming/FFD/FFD_pages.txt | head; echo ===; awk '/\\[pdf page 67\\]/,/\\[pdf page 69\\]/' incoming/FFD/FFD_pages.txt | head -60"
}
```


### [2026-09-06T15:44:17.592Z] TOOL RESULT

```
Exit code 1
1621:[pdf page 65]
1645:[pdf page 66]
1683:[pdf page 67]
1708:[pdf page 68]
1727:[pdf page 69]
(eval):1: == not found
```


## [2026-09-06T15:44:20.185Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1683,1730p' incoming/FFD/FFD_pages.txt"
}
```


### [2026-09-06T15:44:20.229Z] TOOL RESULT

```
[pdf page 67]
ار فعلهای فارسی دری
سودن
سود < فارسی میانه 80 + ایرانی باستان ۴۹-12۵ برای 2 > آراست. 5 صورت
: ضعیف ريشةٌ 52۷و آن به معنی «سودن» است.
سای < فارسی میانه 537 < ایرانی باستان ۵72-:۹37*. 272 برای ساختن مادهٌ مضارع
از ريشه به کار می‌رفته است. 839 صورت بالاندةٌ 82۲ است.
ساپ, ساو, که در فارسی دری به کار رفته‌اند» بازمانده‌های 83# پهلوی اشکانی
هستند. 378[2* ایرانی باستان در فارسی میانه به صورت 37 و در پهلوی اشکانی به
صورت 7 درآمده است.
شایسترد
شایست < فارسی میانه 19ر52. 1 مادهٌ ماضی جعلی و از مادهٌ مضارع ساخته
شده است.
شای < فارسی میانه 33 < ایرانی باستان 8-ر۹83*. برای 2 -> آرای. 529« صورت
بالاندة ريشهٌ وهکدو آن به معنی «توآنابودن» است.
شتافتن
شتافت < فارسی میانه 53130» صورت کهنتر 2۳15130 + ایرانی باستان ۵01-3110 *
برای 18 -> آراست. 201 پیشوند فعلی است. ۰8130 صورت بالاندةٌ ريشهٌ ۰۶127 صورت
اصلی 131 است. 0 پیش از 1به ؟بدل شده است. ريشهٌ به معنی «فشار آوردن» است.
در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
شتاب + فارسی میانه 053180» صورت کهنتر 2۳8130 + ایرانی باستان 201-8130-8*.
برای ۵ سه آرای.
شدن
شد < فارسی میانه 504 + ایرانی باستان 50-1۵*. برای 1۵ > آراست. 80 صورت
ضعیف ريشةٌ 5۵7و آن به معنی «رفتن» است.
[pdf page 68]
ماده‌های ماضی و مضارع فارسی دری سا ۳و۶
شو < فارسی میانه 32 + ایرانی باستان 32-۵*. برای 2 > آرای.
شست.
شست < فارسی میانه 5081 ج ایرانی باستان 3508-1۵*. برای 1۵ -> آراست. 7504
صورت اصلی 3۷8 است. 4 پیش از 1 به 5 بدل شده است. 7504 صورت ضعیف ريشةٌ
40 و آَن به معنی «تحریک کردن» است.
شوی < فارسی میانه 50 < ایرانی باستان 35200-8*. برای 2 آرای. «شور) به جای
اشوی» جدید است > جستن.
شکافت < فارسی میانه 531 < ایرانی باستان ۴2-31-1۵ برای 12 -> آراست. 2
پیشوند فعلی است. 831 صورت بالاندهٌ ریشهٌ قاا است و ۴۵۲ به معنی «شکافتن» است.
شکاف < فارسی میانه 5۶ + ایرانی باستان 2-3۶-۵*. برای 2 -> آرای.
شکست < فارسی میانه 5۵91 < ایرانی باستان ۹16۵۶-12*. برای 18 -> آراست. ‎٩1۵0‏
‏صورت اصلی ۶۵8 است. 4 پیش از ۲ به 8 بدل شده است. ۹24 صورت ضعیف ريشةٌ
4 است.برای‌ضعیف کردن ريشه #حذف شده‌است. 5۵74 به‌معنی «شکستن»است.
شکن < فارسی میانه 5۵7 < ایرانی باستان ۶1۸2-۵*. برای 2 -> آرای.
شکفت < فارسی میانه 5/1
شکف جشکوف ج فارسی میانه 501
شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏
[pdf page 69]
جوا را فعلهای فارسی دری
است. این ريشه به معنی «صبر کردنْ» است.
```


## [2026-09-06T15:44:25.753Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کاستن\\|کاست \" incoming/FFD/FFD_pages.txt | head"
}
```


### [2026-09-06T15:44:25.797Z] TOOL RESULT

```
1825:کاستن
1826:کاست < ایرانی باستان 1:39-12*. برای ۵) -> آراست. 139 صورت بالاندةٌ ريشه 1۵5
```


## [2026-09-06T15:44:29.517Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1810,1845p' incoming/FFD/FFD_pages.txt; echo \"=== page tag near:\"; awk 'NR<=1826 && /\\[pdf page/{p=$0} END{}' incoming/FFD/FFD_pages.txt; grep -n \"\\[pdf page\" incoming/FFD/FFD_pages.txt | awk -F'[][ ]' '$0!=\"\"' | awk -F: '$1<1826' | tail -3"
}
```


### [2026-09-06T15:44:31.819Z] TOOL RESULT

```
۴1۳-4۵ برای 1۵ > آراست. 2۵ پیشوند فعلی است. ۹38 صورت اصلی 83 است. 8
پیش از 1به #بدل شده است. ۹88 صورت ضعیف ريشةٌ ۹228 است. «برای ضعیف کردن
ريشه حذف شده است. 5288 به معنی «کشیدن» است.
فرهنج ج فارسی میانه [112822 < فارسی باستان 8-[0۵0 -8۵* < ایرانی باستان
2-[172-8۵2*. برای 2 - آرای. [به جای 8 آمده است. + آهختن.
«آهنگ» و «فرهنگ» هم از ريشةٌ 988 گرفته شده‌اندء به شرح زبر:
آهنگ + فارسی میانه 30228 < فارسی باستان 0208-8 -3* < ایرانی باستان
۶3-8288-2. 3 پیشوند و 2 پسوند است.
فرهنگ < فارسی میانه 13022 < فارسی باستان 0۵88-8 -8۸* < ایرانی باستان
۳۵-۵28۵
۱ فریفتن
فریفت < فارسی میانه 17211 < ایرانی باستان ۳2۵-427-1۵]*. برای 18 > آراست. 18
پیشوند فعلی است. 420 صورت اصلی ريشه است. پیش از 1 به ؟ بدل شده است. ريشهٌ
0 به معنی «فریفتن) است.
فریپ < فارسی میانه 1۳80 < ایرانی باستان 18-420-2*. برای ۵ -> آرای.
کاستن
کاست < ایرانی باستان 1:39-12*. برای ۵) -> آراست. 139 صورت بالاندةٌ ريشه 1۵5
است به معنی «کوچک بودن». صورت بالانده در معنی واداری به کار رفته است» به معنی
«ک و چککردن».
کاه « فارسی میانه 13 < ایرانی باستان 139-۵*. برای 2 - آرای.
کاشتن
کاشت < ایرانی باستان 37-5-12 *. برای 1۵ -> آراست. 837 صورت بالاندةٌ ريشة 1۵7
به معنی «زراعت کردن» است. 5 برای ساختن ريشهٌ جدید از ريشه به کار می‌رفته است.
[pdf page 73]
0 فارسی درق
کار + فارسی میانه 3 < ایرانی باستان ۸37-۵*. برای 2 -> آرای.
«کشت» مادةٌ ماضی دیگر است برای «کار» از فارسی میانةٌ 151 < ایرانی باستان
۵ا-65ا*. 1 صورت ضعیف ريشةٌ 1۵7 است.
کافتن
کافت + فارسی میانه 1311 + ایرانی باستان ۸3-1۵*. برای 18 -> آراست. 131 صورت
بالاندهٌ ریش 81 به معنی «شکاقتن» است.
کاو +کاف < فارسی میانه 13۶ < ایرانی باستان ۴32*. برای 2 -> آرای.
« کفت»» که مادهٌ مضارع آن «کف» است. از ريشةٌ ۵ به معنی «شکافتن» آمده است.
به شرح زیر
کفت « ایرانی باستان 1۵1-1۵* کف « ایرانی باستان 1۵1-8*.
«کفتن»در فارسی دری هم لازم و هم متعدی به‌کار رفته‌است. در شاهنامه آمده است:
=== page tag near:
1759:[pdf page 70]
1784:[pdf page 71]
1808:[pdf page 72]
```


## [2026-09-06T15:44:43.741Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1808,1812p' incoming/FFD/FFD_pages.txt; echo \"=== CHEUNG kah\"; grep -n -i \"kah\\b\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T15:44:43.814Z] TOOL RESULT

```
[pdf page 72]
ماده‌های ماضی و مضارع قاری دری سس ۶۷
۴1۳-4۵ برای 1۵ > آراست. 2۵ پیشوند فعلی است. ۹38 صورت اصلی 83 است. 8
پیش از 1به #بدل شده است. ۹88 صورت ضعیف ريشةٌ ۹228 است. «برای ضعیف کردن
ريشه حذف شده است. 5288 به معنی «کشیدن» است.
=== CHEUNG kah
15232:*kaH ‘to take pleasure, desire’ 
15307:IE nominal derivative of *keh;- (*kaH). 
15659:is perhaps a (infixed) nasal pres. stem of IE *keH;- (*kaH), although any connection 
16374:*MISC: (+ *à-) Arm. (LW) akah ‘knowing, aware’ || (+ *pari-) Arm. (LW) p'argast 
16376:nskah-em ‘to reject, condemn’ 
16439:*MIDDLE PERSIAN: MMP gh-, ВМР k’h- /kah-/ ‘to diminish, decrease, lessen’, MMP 
16442:Pres.: IND. 3sg. MMP qhyd, BMP k’hyt /kahéd/, Inf.: ВМР k’hynytn /kahénidan/ (from MX) 
16447:*NWIR: NP kastan/kah- ‘to lessen, diminish’, Nn. käs, Tr. kas ‘little; young’, Varz. 
41131:kastan/kah-, 247 
52270:akah, 246 
52397:nsSkah-em, 246 
54265:KAHÓVTEG, 330 
56308:*kaH', *kaHm, *rauj’, *xSij, 
58120:*kaH!, *kanH’, *naz, *zaus
```


## [2026-09-06T15:44:46.511Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16420,16470p' CHEUNG.txt"
}
```


### [2026-09-06T15:44:46.555Z] TOOL RESULT

```
*CHORESMIAN: (+ *apa-) ? bk’s- ‘to be stupefied’ || (+ *us-) m/sks- (intr./inch.) ‘to 
become high, ascend’, m/sk’sy- (caus.) ‘to lift, take up’ © Samadi: 19, 181 f., 180 
*NWIR: (+ *ham-) Bal. ankis(1)t/ankis- ‘to lie down, go to sleep’ 

Ó A root *kas’ is reconstructed on the basis of Khotanese and Choresmian evidence, 
to which a Bal. continuation can be added. The root is exclusively Ir. with no 
apparent IE origin. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: DKS: 56b f.; Shahbakhsh: s.v. ankis- 


*kas! ‘to be small, diminish, lessen’ 

*AVESTAN: YAv. kasu- ‘small, little’ (Yt 8.29), Yt 14.17, V 7.59, etc.), ҮАУ. 
kasiiah- ‘young’ (V 5.24, V 14.5, V 15.2, etc) 

*MIDDLE PERSIAN: MMP gh-, ВМР k’h- /kah-/ ‘to diminish, decrease, lessen’, MMP 
k’hysn, q’hysn ‘diminution’ = DMMPP: 205a, 201b 

Pres.: IND. 3sg. MMP qhyd, BMP k’hyt /kahéd/, Inf.: ВМР k’hynytn /kahénidan/ (from MX) 
*KHOTANESE: (+ *ni-) nyassa- ‘deficient, bad’ 

*CHORESMIAN: (+ *us-) sks- ‘to become short? = Samadi: 182 

*NWIR: NP kastan/kah- ‘to lessen, diminish’, Nn. käs, Tr. kas ‘little; young’, Varz. 
kas ‘little’ 

*NEIR: Oss. I. kæstær *young(er), little’ || ? I. &-gas, D. &-gas (+ neg. *a-) ‘whole, 
integer || (+ *ui-) D. igas *whole(some), healthy, alive’, Wa. kas ‘young man, lad, 
youth’ 

*SANSKRIT: kasü- (m.) PN ‘the Small One’ (RV 8.5.37) = EWAia I: 330 

© This apparently Пг. root has no certain IE provenance. It may even be an 
exclusively Ir. root, if the Skt. name kasü- is some sort of a borrowing, cf. EWAia, 
l.c.: "als „iranisch-westindoarische Dialekt-Isoglosse” aufzufassen ?". 

«PIE 9 Pokorny, Le cites NHG hager ‘gaunt, haggard’, Lith. kaséti ‘to lessen, 
become thin, dry’ as possible cognates. The origin of NHG hager (incl. Engl. 
haggard < Fr. hagard < Germanic ?) is obscure though, Seebold (Kluge 2002: 383b) 
considers Skt. krsä- ‘id.’ as a semantically more satisfactory connection to NHG 
hager. As for the Lith. form, it appears to have a variant katéti, both forms have a 
popular flavour according to Fraenkel I: 227b f. = LIV: — | Pok.: 521 f. 


248 *kaš
```


## [2026-09-06T15:45:00.155Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"^k'h|kah-|kahisn|kastan|k'st\" PHD_mackenzie.txt | head -20; echo \"=== sax\"; grep -n -iE \"s'k|sax\\b|s'x\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:45:00.218Z] TOOL RESULT

```
3145:kah-, ~lsn, v. kastan.
3148:kahidan [k)hytn l I N ~] = kastan.
3150:kah-rubay [khlp)d I N --TUba] amber.
3255:kastan, kah- [k'stn ' , k)h- I N -] diminish, decrease, lessen.
3259:kastar [k'st)l] diminisher.
3331:kastan [kwstn' I = M, N -] beat, pound.
4807:skastan, sken(n)- [TBLWN-tn' < A ...; tbr; fkstn', fkyn- I M (fkn-,
4808:       N fikastan, fikan-] break.
4816:sken(n)-, .....isn, v. skastan.
6122:break (vt.) skastan.                   bustard <:arz.
6350: decrease (vt.) kahenidan, kastan.          desirous kiimagomand.
6401:diminish kastan.                        di1)inity abargar, yazd; v. Appen-
6403:diminution kahisn, nirfsisn.            divisible bahromand.
8265:skastanl              \\l"'~ '\"     tex
8391:skastan                   \\\"eUYU          susar                 ~t"\)
9737:kah-                                  - AU"      kar-I
=== sax
1205:a~sag ['s'k l I M 's'g] innumerable, countless.
2868:hasal1lrd [hS'klt I M hS'gyrd, N fagird] disciple, pupil.
4094:passaxtan, passaz- [ps'htn', ps'c- I M ps'xt, ps'c-] fashion, prepare;
4462:sAg [s'k I P s'g] number.
```


## [2026-09-06T15:45:04.633Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"branch\" PHD_mackenzie.txt | head -10; echo \"=== NYB kah\"; grep -n -iE \"k'h|kahisn|kastan|kāstan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:45:04.695Z] TOOL RESULT

```
624:and tik [t}k' IN", 'vine'] branch.
1429:az~ [)zg I N azy] branch.
4887: Stag [t)k ' I N ta] branch.
6108:branch azg, tag.                       bun kulacag.
=== NYB kah
2159:kāhišn [k'hšn', k'hyšn'] the act or pro- cess of diminishing; the state of being diminished: 68°. 983.5. 1047. — MPrs k’hysn (A-H I); NP kästan käh- ‘to lessen, to diminish’ (Paz. zähidan, cf s. v. kandan). A factitive vb. derived from the stem *ka0-, SW form of kas-, v. s. v. !kas. The form k’hy$n' represents probably a hybrid spelling combining kähisn and [k'dšn' =] "kdyišn (cf xudyišn: audh-), since -i- is as a rule not written in the ending -išn.
2253:1kas [ks] small: hàn i hac tč ~ thy in- ferior 685; v. also haci§-kas. - NW form: Av. (460) kasu-, MPrth sup. ksyst; SW *ka0u- which has survived in the comp. *kadiyah- > kēh: MPrs gyh (BBB), Paz. NP keh; cf kahisn.
3637:Skastan
3646:škastan  [škstn', TBLWN-stn'] šken- [TBLWN-] to break down, to crush, to smash: 334, 4221-22, 8716, 943, 10718; amar tapäc škast cut off the scourge 427? (un- certain; MS ?pr?e = a-fräc for apäc; gl.: kū-š patiš apäc kart estat); ~ + dēvān
3648:Skastan
3649:kālpad i gētāhīk 8925-25, 9028-27; pat han + dašn pad frac škast trampled on it with his right foot and crushed it 5311-12; škast was broken, burst 542°; v. also s. v. stur. — Av. (1586 sq.) skand-; MPrs ‘Skn- (Sogd. 31%, 33. 59); Paz. škastan, seldom  škandan, škan-; NP  šikastan šikan-.
4149:"vikastan [wkstn'] "to disappear: *vikast she *disappeared 58°. — Uncertain. It could be < vi + Av. (459 sq.) kas- ‘to perceive’, v. s. v. Gkasi, a SW form with -st instead of -št; the NW form would be *vikašt. Perhaps better *vi/ni/kist ‘she was cut to pieces, she split’ < *vi- or ni-kirst < vi or ni- + *krsta- from Av. (452 sqq.) karat-, v. kirrenitan.
5337:skand-: Skastan
5864:‘Skn-: Skastan "'škwhyh: škēh šn'xtn, “Sn’s-: šnaxtan ty, ‘yg: d
6007:k'hyšn: kähisn
6817:šahar: šahr Saharyàr: šahridar Sav: Sap šayastan: šayistan šēvašn: ščp- šihastan: sahistan šina: ščvan škaft: » škandan y škastan, TA EKOLAN šnavašni: āšnavišnēh šnāxtan, šnās-: ~
6889:xühidan: kahisn
7234:kardan (kun-): 'kartan kargas: karkās ` kārzār: karēcār kāstan, kāh-: kāhišn
7447:šikastan, šikan-: škastan
```


## [2026-09-06T15:45:13.450Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kasu-\\|kasyah\\|kasista\\|kasi\\^sta\" BRT.txt | head -20"
}
```


### [2026-09-06T15:45:13.504Z] TOOL RESULT

```
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
9381:459  karätayaeffl  —  kasyah-  460
9385:Zum  V.  Jiari-.  —  Vgl.  ai.  kriläy-  f.  'Ansied-   *b5jim   X.31. 1 3 ;   —   "sJuIäl  nä  .  .   isväcU lung'  (woiu  FoYKZ.j4.i39ßeEenGDN.  VSt.    (sd.)   kas  faraoi  Y.4j.i^ X.  128).  —  PQ.:  kiilan,  kiil.  KompA.,  AbleLt.  —  VgL  kasyah-,  iasiUa-.  —
9428:■A.I.'.).   -  s.  »,J.,  *«A  und\ii»rÄ..   -  •  J.  kasyah- Adj.  (mch  fem.)  der  kltinere,
9431:4ÖI  kasyah-  a  —  Icata-  462
18728:Zum  V.  nartp:  —  Pü, :  :*/  m  i  15  dastawar nirfsenend  ('sie  vermindern')  vai  ..  .  —  •)  Vgl. lAusdr,  nnter  kasyah-  a.
19600:fra^mtmÜa  paoirysia  yasna  upamaHa  °m(Ua frahmala  Yt  ll.  i8;  VAp;  —  airyamarum . .  ys  upims  (sd.)  yB  *mS  yö  fratfmS  sao- tXzuye  G.  /.  6 ;  —  frafymstn  datühsul  nava pfn'hws  (sd.)  i?nnava  'mS  . .  nit?mS  V. 2.30;  30;  —  kasistahe  tr?svö  .  .  'make 3r}svB . .  *mati^fahe  irisvB  "des  kleinsten  . . eines  mitteigrossen .  ■  des  grössteo  Fingers" V.6'.  10— 14;  —  dvadasa  vitaraisd.)  upsma . . 'ma  (HP.) . .  »ihma  V.J4-14',  —  "'f'- m^m  staonm  .  .  -mim  .  .  ayrim  V.  7.  4 1 ; 43'.  A)  ASa  undDSn.  als  Adv.;  a)  ASn. •m^m  'mitten  hinein  in  — ,  unter  — '  (Gen.); /ravafayl! ..yä  'namHt  myeziiinqm  . .  upa- vtwnte  Yt  13.  64.  b)  DSn.  'mäi  'zur Mitte  hin —j  mitten  vor —' (Gen.) :  *haoyü.- tttnäi  darssman  .  .  *äaiiitS.ipiHäi  .  .  *mai
20132:•j.inasijtta-,p.ma9i$ta-Adj.'dergrÖsste'j i)  der  Ausdehnung  nach :  kasistahe  .  . mahmahe  .  .  °tahe  3r>svS  frat3m3m  iMsü V.  6. 14.  2)  U  dem  Rang  nach:  a*wra*- matdä  . .  hyer  -tJ'  baganam  D.4.1;  X. 6. 1.  a)  bes.  'der  Oberste'  cinerTruppe: AyO*  tnadaiitiva  *t^  akJ'  Bh.  2. 6;  —  hyJ' avahyä  karahyS  °ta*  äk^  Bh,_j.  11;  11, 2.4;  —  avamiam  'tarn  akunavam  Bh.2. 6;  I4,^.6j9,I4,  5.1,4; —  avam  'tarn akunavcl'ts  "den  machten  sie  zu  ihrem Obersten"  Bh.j.3,  5.1.
21119:—  yaihä  ainikö  bräzaiti  y*  HBrySMärahe  ?r>ti-S  V.  ö^  43 ;  —  yö  astim  upanh^rvtaiH Yl  JO,  142;  —  ahe  ti  na  *travanh3*afra-  ,.  *avai  atpi  y  kasistahe  ^rTtfS  fratanam mar7rUi{sA)astrjdley' gaianqm(itM.22;  tbifti   W.6.  10;     11,    14,    iz;    —   yas:a
```


## [2026-09-06T15:45:16.500Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9420,9440p' BRT.txt"
}
```


### [2026-09-06T15:45:16.555Z] TOOL RESULT

```
jAw.i(i/-);''auf  ir.  *;i/-jy' zurQckgeht;  IF.S.ä6i.  ^        "   Y(  ^j    jj^
•  j.  kas-  V.,  nur  mit  ä  'gewahr  werden,  Eig.  'der  wenig  Nahrung  hat   (braucht  oder
erblicken'.    Praes.  3  kasa-.  ail"'/-
lat    mqm    mairyS    äkaiat    "darauf  er-  •  j.   kasyapa-    m.   'Schildkröte',    die    als
blickte  mich  .  ."  V.  22.  2.  lAiiT'isches  Tier  gilt:  baevan  'panqm  ava.-
Vgl.  ai  kaiaif  'er  erscheint',    äkaiya    "im  Er-  janyät  \.J4.  5.
schauen';  np.  ü.cJ*  'kundig',  iti^Ah  'Anblick',  ü.  kaiyafa-  m.,  np.  ^.i  ('«/.  — Pü. :  undeutlich,
ooss.   k'äsin   'anschauen',   rih/'   ('Gesieht'  ^)       .    ,  ,_     .  j-    .-       i_  r       1  u      1  1   ■
■A.I.'.).   -  s.  »,J.,  *«A  und\ii»rÄ..   -  •  J.  kasyah- Adj.  (mch  fem.)  der  kltinere,
Vii.;  äH^Ji  a!  an  i  mar  iaiil,  ei\.:  j!ui amlar  geringere':   ya^a    masyayn    äß   'yurtham
db,Google
4ÖI  kasyah-  a  —  Icata-  462
(GPf.)  apam  *avi.frädavaiU  (sd)  V.5.  24;       ■>  Vgl.  iBed.  p.  pou-Aoc,  ai.  pari-cari-  m.;
—  *koys  hmti  masyanhs  asoa  (sd.)  .Maya       •-"  Osthoff  BB.  15.  316.
iffo'«»'*^  F.  Je.       a)  'verkleinernd,  herab-  J   '"'^  •"■  S'-  ''«s  '^'^a.
setzend'    in    'vawAf    Jfl»yi.lj     ^ai^jV/    'er  •  j-  iristanqm  "kaäin^m  Vd.  14.
setzt  herab,  verleumdet'  ■>,  Jemanden  (Akk.)      ^=?;='"*  '"  ™^^.A^^'.,™ ;  sd.  _  Pü. .  r«ü«
bei  -  (pat.)'>:  yJ  nar,m  amvan.m  myö_.-_        "-  \^^       ^_  ^^,^^  ^  ^._
i-arPttät    vä  .  ,     'yaime    saanlt     danäiti        .     .        „       s  „.«-,-    ^
y  "^  •  j.    ka-x*araoa-   m.,   -x'araioi-  f.   Be-
komplr.  itt  :*o«i-.   .-  mp.  *^^,  np.  kih.  -  Zeichnung  einer  Klasse  von   (männlichen
```


## [2026-09-06T15:45:23.362Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9381,9420p' BRT.txt | grep -n -i \"klein\\|kasu\\|gering\" "
}
```


### [2026-09-06T15:45:23.408Z] TOOL RESULT

```
3:*raoi'yttm  (sd.)  hixtayal'a  HayaSca  V.  d.t;  •  g-  (.  j-)  tasav-  Adj.  Tdein,  gering':  yS  vä
7:^''2^/?'  'p}-^^-    ,  ,,    „  •  j.  kasiSta-  Adj.  a)  'der  kleinste':  'iaÄe
9:•  j.  karsnaz-  m.  Name  einer  iranischen  masUtahe  V>.  10;  JÄ  44PUZ.  b)  'der Yz.TsM%\  yasmaoyö  parö  'nazS  {'^'2.)  hvira  geringfügigste':  yö  n��  matiltim  yasmm baon  sn-isfa  Yt.  13.  38.                                    yasäite  'titn  ^yasnat  frsyatät  (sd.)  Yt/.  24;
13:V..?.24;  —  zqm  'yqm  "^radyam  V. 14.13.  ,  j.  kasu.xratav-  Adj.  'der  geringe  Ein- PFP.  iura  V.  ik<ir!.  —  Pü.  (lu  V.  j):  kilürr,  sjcht besitzt' :  /<^^^a  vJ  'tus  masyöj(rtt'i>wam (zu  V.  I4\:  undeutlich.  ,    ,  ,  ....  .,-.  ,-  ■'  •
15:•  ].  karsvar-,  -van-  n. 'Kreis' der  Erde,  vgl  iasuxra%',i,an:  —  V\,tkctdiakxraihimi 'Erdteü'":  />//«/  -^.^r»  j-«/  x^aniraiim\  ■  feasu.xraO-wan-  Adj.  (auch  fem.) Yt.i£.i5,^o.i5,67,i33,Y.57-3i.y./p.39,  -der  geringe  Einsicht  besitzt':  noit  ia H.  /.  I4i  -  't'^rp  yat  ar.>zahi  Yt.  i2.  9;  „^i^^a  -^wa  (NSf.)  "nicht  darum  (?)  ein ,„_,..  _  .„./   .,..„  j.^/  vouru.bar»iU:^^^^  ^„„  geringer  Einsicht"  N.40'>.
19:•  j.  kasu.dänav-  Adj.  'mit  kleinen  (Samen-)
27:s^aniraiahe  Vr. /o.  i.  '•  j.  *^kasu.draonah- "  Adj.   'der  geringe
33:iaiiru-baiiiiay  und  Voutu-janiiay  im  Norden  ge-  •  j. kasu.pääna- Adj. 'mit  kleinenFcrsen'":
38:mp.  (Pu.),  np.  /li-'iir».  —  ■)  VgL  zF.  %3'js-  —  •  j-  kasu'pitav-  m.  EN.  eines  Gläubigen:
```


## [2026-09-06T15:45:33.309Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"^kas|kasu|kasaka\" KNT.txt | head -20"
}
```


### [2026-09-06T15:45:33.355Z] TOOL RESULT

```
1583:kasaka-, kásakaina-.
4102:DPi = Darus, PERSEPOLIS т. mayüxa : kasakaina : Dárayavahaus : XShya : уїйїуй : karta TRANSLATION OF DPi: Door-knob of precious stone, made in the house of Darius the King.
5285:kasaka- sb. ‘semi-precious stone’; Elam. ga- st-ga causes König and Wb. to write kás'ka, but this is not warranted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, despite Bv. BSLP 30.1.61); for meaning, cf. NEng.
5288:kasakaina-. Казака пзш. DSf 37, 39.
5289:kasakaina- adj. ‘of semi-precious stone’, | | namely, of lapis lazuli: adj. to preceding ($147. ;
```


## [2026-09-06T15:45:34.247Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sakala\\|śakala\" IEC.txt SYN.txt | head -20; echo \"=== SYN 525\"; awk 'BEGIN{RS=\"\\f\"} NR==549' SYN.txt | head -40"
}
```


### [2026-09-06T15:45:35.955Z] TOOL RESULT

```
SYN.txt:23474:Skt. sakala- ‘whole’, lit. ‘having (all its) parts’, cpd. of sa- cop. and kala- ‘part’.
=== SYN 525

CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
1. Grk. addat, fr. *&pAax- (beside *arodx-, *a¢hox-in Hom. Sk, Att. &dob) : Lith. vilkti, velku, ChSl. vlésti, vléka ‘draw’ (9.33). Hence NG aidaxt. Walde-P. 1.306.
2. Lat. sulcus (> It. solco, Sp. surco) : Grk. &xw ‘draw’ (9.33), ddxés ‘track,
See eee A
Ee
SS eS
ek ae ed
To I
1 made by the ybnot ‘furrow 5 B07. races © ih ‘plow’. Walde-P. 2. plows 999
renout °* ‘er use ‘heaped-up pra _ sill n, 10 a ‘heap up earth’, earth’ fr. iiic orig. Hence used for the prob: af ‘ea between furrows, then for es ‘gel, REW7797a. Gamill- the abe furrow’ in OFT. and still in | use more widespread than stllon tas linguistique, Carte 1234), fr. a ca word represented by W. rhych, ete. (below; 8). REW 7299. Gamill- scheg 736. Bloch 2.204. Rum. braadd, fr. Slavic (below, 6). 3. Ir. elrech, Nir. eitre, W. rhych, OBr. rec : OF furh, ete. (below, 4). Pedersen 1.122. Thurneysen, Kelto- rom. 74 f. Nir. clais, also ‘groove, trench’ as
Ir. class : claidim ‘dig’ (8.22).
, Boh. kopati, Pol. kopaé
noma fo k ny kapas ‘grave, 5; Kameros (UPS grave’, Grk. oxdme-
Tuncare ‘root up, tear out, pluck’, fr. an : reu-in Lith. rauts
Walde-P. 2.353. Er.
AGRICULTURE, VEGITATION
Digitized by Arya Samaj Foundation Chennai and eGangotri
497
Br. ero, erv = OCorn., W. erw ‘field’ : OHG ero ‘earth’, etc. (1.21). Walde-P. 1.142. Pedersen 1.63.
4, ON for, OE, OHG furh, etc., gen- eral Gme. : Lat. porca ‘ridge between furrows’, W. rhych ‘furrow’, etc., perh. Skt. pargana- ‘chasm’. Walde-P. 2.47. Falk-Torp 283.
5. Lith., Lett. Miihl.-Endz. 4.431.
6. ChSl. brazda, etc., general Slavic, prob. (as orig. the ridge between fur- rows) : Skt. bhrsti- ‘point, edge’, OE brerd ‘edge, brim’, ete. Walde-P. 2.133. Berneker 75.
7. Skt. stta-, perh. fr. IE *sé(z)- ‘throw’ and ‘sow’ (8.31). See under Skt. stra- ‘plow’ (8.21).
Skt. karsi-, Av. karga-, fr. Skt. krs-, Av. kars- ‘draw’ and ‘plow’ (8.21).
vaga, etym. dub.
8.22 DIG oxaxTw, dplcow, Goth. graban Lith. kastt Aaxalvw ON grafa Lett. rakt oxdBuo Dan. grave ChSl. kopati, ryti fodere Sw. grdva SCr.  kopatz, ritt vangare (scavare) OE grafan, delfan Boh.  kopati, ryti ‘ied (fouir, fouil- ME grave, digge, delve Pol. —kopae, ryé sa NE dig (delve) Russ. kopat’, ryt’ oe Du. graven (delven) Skt. khan- dlaidim OHG  graban, telban Av. kan- rehercin MHG graben, telben : NHG graben cloddio, palu f Klaza, kava 1. Gtk. okdarr : a) A ChSL., SCr. (NG pop. oxéw) Grk. daxaivw (not common): Ir.
laige ‘spade’, W. llain ‘blade’. Walde-P. 2.381.
2. Lat. fodere (> Fr. fouir) : Chsl., bodgq, bosti ‘stick, prick’, Lith. bedu, best ‘stick into’, Lett. bedu, best ‘bury’, W. bedd ‘grave’, Goth. badi ‘bed’, etc. Walde-P. 2.188. Ernout-M. 378. Walde-H. 1.521 f.
It. vangare, fr. vanga ‘spade’ (8.23).
It. scavare (tech. ‘excavate’), Sp.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
NT PAR. oD
are
498
cavar, fr. Lat. (ex-)cavare ‘make hollow, excavate, deriv. of cavus ‘hollow’ (12.72), REW 1788, 2964.
Fy. creuser, fr. creux ‘hollow’ (12.72).
Fr. fouiller (‘dig’, but mostly as archeological term for ‘excavate’; the pop. sense of the word is ‘rummage’), fr. *fodiculare extended fr. Lat. fodicare ‘dig, pierce’, fr. fodere (above). REW 3404. Wartburg 3.666 f.
Rum. sépa (cf. Fr. saper ‘undermine’, It. zappare ‘dig up’), deriv. of
```


## [2026-09-06T15:45:48.266Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"8\\.5[0-9] \" SYN.txt | head -20; echo ===; grep -n \"BRANCH\\|BOUGH\" SYN.txt | head -20"
}
```


### [2026-09-06T15:45:48.327Z] TOOL RESULT

```
Exit code 1
12204:CHAPTER 8 th AGRICULTURE, VEGETATION! : . A 8.11 FARMER 8.44 Bariey ac : 8.12 Frexp (for Cultivation) 845 Rys dl ¢ 8.13 GarRDEN 8.46 Oats i ‘a 8.14 Barn 8.47 Marzz, (U.S.) Corn q 8.15 Cuurivats, TLL 8.48 Rice Me ; 8.21 Pxow (vb.; sb.) 8.51 Grass ht : 8.212 Furrow 8.52 Hay a i 8.22 Dic 8.53 PLant al 8.23 SpavE 8.54 Roor ( 8.24 SHovEL 8.55 Brancu ba 8.25 Hor 8.56 Lear ere 8.26 Tork 8.57 FLowER me 8.27 Raks 8.58 Rosz M 8.28° Harrow 8.60 Tree = 1.42 * 8.31 Sow; Srep 8.61 Oak 8.32 Mow, Reap a oe Bo 8.33 Sickie; ScyrHE 8, 64 ei i 8.34 THREsH 8.65 = t in ? 8.35 TsresHinc-Foor 8.66 hee 8.41 Crop, Harvest 8.67 VINE mS 8.42 Grarn (Generic = British Corn) 8.68 Tosacco ‘co 843 Wxeat 8.69 SmoxE (Tobacco) (6. ink 8.11 FARMER - Grk. — -yewpyés Goth. (airpds) waurstwja i ikini ini : . Lith kininkas, laukinin- NG —-yewpyds, xwpixds, ON bondi, akrmasr, to, ieee a i fal Ra Lat. aa Dan. — dyrker, landmand, Lett. laucinieks, zemnieks Ia Hiesehee “aactnctiorglontts bonde ChSI. délatelt, tezatelt the : as ae iiva- Sw. dkerman, jordbru-  SCr. __ratar, teak, seljak 1 Tr ant re fee kare, bonde Boh. __rolnik, sedldk i ; 4 ee pied tiva- OE = (eord)tilia, wcerman, Pol. _rolnik, chlop It Sp Waban RUE gebir, etc. Russ. zemledelec, krest'ja- thi pes f r “i agricultor ME husbond(man), acre- nin, muzik DD Ir, : eke He abe man Skt. ksetrakarsaka-, P Nir. paecmba ugar Ne eld (husbandman) kselrapati- W. amaethwr, ffermur OHG ee ae Av. vdstrya-
13096:8.51 GRASS ba, xbpros Goth. hawi Lith. Zolé Ses 3 ON gras Lett.  zale ae, aroier Dan. gras ChSl.  trava herbe Sw. gras SCr.  trava hierba or gr@s, gars Boh.  irdva . tarba ME gras Pol. trawa fer NE grass Russ. trava fear Bua gras Skt. trna- pp, glaswellt MHG a ae Av. (vasira-) Words f, paiey off ‘ or ‘ ass’ tons as ‘green, prowine from such no- Grk. xépros, orig. ‘enclosure’, esp. 'D part also from fodde fat blade’, but | ‘feeding place for cattle’, whence ‘fodder, &t Was Usually grasg er’, since the fod- | grass, hay’ : Lat. hortus ‘garden’ (8.13), «tk. xb, Ton ia D Ir. gort ‘field’ (8.12), etc. Walde-P. Toy fot? 7 Vor. rota, fr. | 1.603. Hence NG xoprépt.
13108:8.52 Grk. —_xépros Goth. hawi NG xoprapt, cavds ON hey
13141:- €1 ; Goth. hawt, ON oe period also | etc., general Balto-Slavic : Grk. xow4. a Gme., 3? a Goth. hawt Jn. | xépros (Hesych.), root connection? gery (en 12 GOSP. att, 6.39), prob. | Walde-P. 1.466. re 10, 08 00" Fr 40 be mown’ : OF Sid rab 43 018 ‘mo i wan ‘hew’ (9.22) 6. Skt. irna- ‘grass’ (8.51), also used. Cn ed for ‘hay’? Hy j y . 8.53 PLANT th. Lith. augalas, Zole Grk. gutdy, Bordvn a urt Lett. augs, zale NG gute Borda Dan.  plante, url ChSl.  sadit at. herba ba Sw. planta, ort SCr. _ biljka, trava : Tt pianta, te OE wyrt Boh. rostlina, bylina, zelina fr Plante, san ME _ wort, erbe Pol. _roslina, ziele Sp. ee iarba NE plant, herb Russ. rastenie, trava Rum. Bs Du. plant, kruid Skt.  virudh-, ogadhi- el Ca OHG  pflanza, wurz, krit Av. urvara-
13165:8.54 ROOT Grk. pita Goth. waurts Lith. Saknis NG pita ON rot Lett. sakne Lat. radix Dan. rod ChSl.  korent It. radice Sw. rot SCr. _ korijen Fy. racine OE wyrltruma, wyrlwala Boh. _kofen Sp. raiz ME role Pol. korzen Rum. rdddcind NE root Russ. koren’ Ir. frém Du. wortel Skt. mila- Nir. fréamh OHG) wurzala Ay. varasaji- W. _ gureiddyn MHG  wurzel Br. gwrizienn NHG  wurzel
13192:8.55 BRANCH
13242:8.56 LEAF
13262:8.57 FLOWER Grk. Gos Goth. (bléma) Lith. —gélé (kvietka, 2iedas) NG &fos, NovAobdt ON blém, blomsir Lett. puk’e (zieds) Lat. flos Dan. blomst ChSl.  cvétit, cvéttet It. fiore Sw. blomma, blomster SCr. cvijet Fr. fleur OE blistma Boh.  kvélina Sp. Slor ME _blosme, flour, blome Pol. kwiat Rum. floare NE Slower Russ. cvelok Ir, lath, scoth Du. bloem Skt. puspa-, kusuma- NIr.  blath OHG bluomo Av. Bg oh W. blodeuyn, blodyn MHG bluome Br. bleunienn, boked NHG  blume
13293:8.58 ROSE Ab5ov Goth. .... Lith. rozeé tptavTagvAdo ON rds, rosa Lett. ruoze rosa Dan. rose Ch&l. Bee rosa Sw. TOS SCr. ruza rose OE rose Boh. _rtiZe . ‘rosa ME rose Pol. roza . trandafir NE Tose Russ. roza, rozan ros Du. 700s Skt. (japa-, odra) TOs OHG rosa Av. varaéa-(?) thosyn MHG rose rozenn NHG rose
28510:Lith. plakti ‘beat, punish’, OE flécan ‘clap in applause’ (OHG (fluohhon ‘curse’), and, with the same semantic de- velopment as in Italic, Goth. flokan ‘be- wail’ (Lk. 8.52 faiflokun fo = éxérrovto airnv), ChSl. plakati (se) ‘lament, weep’, etc. (below, 7). Walde-P. 2.91f. Er- nout-M. 775.
31433:18.51 Write
31434:18.52 Reap
31435:18.53 Lerrer (of the Alphabet) 18.54 Letrer (= Epistle) 18.55 TABLET
31436:18.56 PAPER
31437:18.57 Pen
31438:18.58 Ink
31439:18.59 Penci
32310:18.51 WRITE
32320:4, Lith. ragyti, etym.? (Wiedemann, BB 28.59 : Lith. rézti, ChSl. rézati ‘cut’, but formal relation difficult).
32330:18.52 READ
(eval):1: == not found
```


## [2026-09-06T15:45:51.512Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13192,13245p' SYN.txt"
}
```


### [2026-09-06T15:45:51.562Z] TOOL RESULT

```
8.55 BRANCH
4 Goth. asts Lith. aka Kk, ie Oi ON grein, kvistr Lett. zars
ee Dan. gren ChSl.  vétvt, véja ramo, rama Sw. gren : SCr.  grana branche, rameau OE telga, bog, twig Boh. vétev, haluz rama, ramo ME bow(e), braunche, Pol. gataz
. ramurd, cracd twist Russ. suk, vetv' craib, gésca NE branch, bough Skt.  gakha-, vaya- géag, craobh Du. tak Av. yaxslt-, frasparaya- cangen, cainc OHG ast, zwelge, zwig brank, barr MHG ast, zelge (zwic)
NHG | ast, zweig
3.213 ff. Walde-P. 1.186, 95 (with dif- ferent semantic view). Feist 60.
Grk. étos, Goth. asts, OHG-NHG ast, Arm. ost.
2. Grk. xdé5os, orig. the ‘broken-off’ branch : xAadapés ‘frail, easily broken’, Lat. percellere ‘strike down’, cladés ‘de- struction’, Lith. kalti ‘strike’, also OE holt, OHG holz ‘wood, woods’, ChSl. klada ‘beam, block’, etc. Walde-P. 1.438 f. Walde-H. 1.225 f.
3. Lat. ramus (> It., Sp. ramo, or, as orig. coll., It., Sp. rama; dim. forms > Fr. rameau, Rum. ramurd) : radix ‘root’, etc. (8.54). Ernout-M. 849. REW 1033, 7055.
Fr. branche (> ME braunche, NE branch; also Norm. Fr. form > Br. brank), fr. late Lat. branca ‘paw of an animal’ (> Rum. dbrincd, It. branca
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
im eeeees
SSRN
524. SELECTED INDO-EUROPEAN SYNONYMS
nae
ms : <000 ood » 3 melt pth dete itp aS
BY }!
- ‘paw, claw’), orig.? REW 1271. Wart- burg 1.498. Gamillscheg 139 f.
Rum. cracé, fr. Slavic, cf. Bulg. krak, kraka ‘leg, foot’, SCr. krak ‘long leg’, etc., also in ChSI. dligo-krakiu ‘sort of insect’ (lit. ‘long-leg’). Tiktin 429. Ber- neker 571 f.
4, Ir. craib, NIr. craobh (also a ‘tree’, as in Gael.), etym.? Macbain 104.
Ir. gésca, géc, NIr. géag, W. cangen, caine, Lith. Saka, Russ. suk (ChSI. sqkit ‘twig’, Boh. suk ‘knot’ in wood), Skt. gakha-, Arm. car: Skt. cafku- ‘peg’, Lith. Saknis, Lett. sakne, OPruss. sagnis ‘root’, Goth. hoha, Ir. cécht ‘plow’ (forked stick’), etc. Walde-P. 1.335. Pedersen 1.126, 494.
Br. barr ‘top’ (12.83), also ‘branch’ (as ‘tip’, cf. Du. tak, below, 5).
Br. brank, fr. a dial. form of Fr. branche (above, 8).
5. Goth. asts, OHG ast, etc., above, 1.
ON kvistr, mostly ‘small branch, twig’ (Dan. kvist, Sw. qvist ‘twig’), ME twist, twyste (cf. NED s.v.), cf. ON hkvisl ‘fork, branch’ (of a river, etc.), fr. Gmc. twis- (Goth. twis- ‘apart’), IE *dwis in Lat. bis, early Lat. duis ‘twice’: IE dwou- ‘two’ (cf. below, OE twig, etc.). Walde-P. 1.820. Falk-Torp 607 f.
ON grein, Dan., Sw. gren: Sw. gren ‘fork between two branches’, Sw. dial. grena ‘spread the legs’, MHG griten, id., Goth. grips ‘step’, etc., connections out- side Gmc. uncertain, but semantic development clearly ‘fork, angle’ > ‘branch’. Falk-Torp 345. Walde-P. 1.652.
OE itelga, OHG zwelge (with zw- for z fr. zwig), MHG zelge, zelch (ON talga ‘thin limb, long arm’, rare) : ON telgja ‘whittle’, Ir. dlongim, dluigim ‘split’,
Lith. dalgis ‘scythe’. Walde-P. 1.812. Falk-Torp 1252.
OE bag, boh, ME bow(e), NE bough, same word as OE bég ‘shoulder’ : OHG
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
buog ‘shoulder’, Skt. bahu-, Gri. 7
‘ ? Xus arm’, etc. (4.31). Early ang usual specialization to ‘bough’ of a tree. NED s.v. bough, sb.
OE twig, twigge (ME, NE twig ‘smal] branch, twig’, but in OR general ‘branch’, cf. Gospels, Mk, 13.28, Mt. 24.32, of the branches of the fig tree also Jn. 12.13 palm-treowa twigu), Dit twijg, OHG zwig (mostly ‘twig’, of. Graff 5.729; but also ‘branch’, ef, Tatian 116.4, 5), MHG zuice (likewise mostly ‘twig, sprout, cutting’), NHG 2weig, all derivs. of IE *dwi-, *dwei-- *dwou ‘two’, like ON kvistr, etc., above. Here also OHG zuog, OS tg, with vowel from the numeral. Walde-P. 1.819, Note the opposite tendencies of usage in Eng- lish (‘branch’ > ‘twig’) and German (‘twig’ > ‘branch’).
ME braunche, NE branch, fr. Fr, branche (above, 3).
Du. tak, fr. MDu. tacke, tac ‘point, branch’ = MHG zacke, NHG zacken ‘point, prong’, NE tack, etc. root con- nection dub. Franck-v. W. 685. Walde-P. 1.785.
6. Lith. Saka, above, 4.
Lett. zars, prob. : Lith. Zaras ‘beam of light’ (Lalis), Zéréti ‘shine, glitter’, ete. Cf. the opposite semantic development in OE beam, NE beam for ‘beam of light’ (NED s.v.19). Miihl.-Endz. 4.691.
7. ChSl. vélvi, Boh. vétev, Russ. velv’ : Lith. vytis ‘osier’, Lett. vitvols, OPruss. witwan, ON vidir, OHG wida ‘willow’, etc., formations of IE *wei- in ChSl. vé&ja, Skt. vayd- ‘branch’, Ir. fé ‘rod, measuring-rod’, Lat. viere ‘plait, Wealey Lith. vyti ‘twist’, ChSl. vité ‘wind, twist, ete. Jokl, Arch. sl. Ph. 29.44, Walde-P. 1.224, 225.
SCr. (Bulg., Slov.) grana, Ukr. hranok (Russ. granka ‘tuft, wisp’) : Russ. gra” ‘facet, limit’, granica ‘frontier’, Pol.
4 ‘beard '496, Berneker 346.
es h. “haluz, Ukr. hdtudz, oe liu, a *galq-2t : ae puss “Oy ‘bough’ Boh. hil ‘staff, gol fa (r m. kolr ‘branch’, root con-
Briickner
+t etC.y en Berneker 292, 326. D
3, oe suk, above, 4, g, Skt. cakha, above, 4
gkt, oaya : ChS. véja, etc. (above, 7). Ae yarsti- (in epds. pri-yaxsti-, etc.)
AGRICULTURE, ’ ll t rer. edge, etc., a _ hear e tpoint’ : ON gren, potio i ‘bearded’,
igitized by Arya Samaj Foundation Chennai and eGangotri
VEGETATION 525 = Skt. yasti- ‘staff, stick’, root connec- tions dub. Walde-P. 1.443. Barth. 809, 1236.
Av. frasparaya-, lit. ‘that which shoots forth’ (epd. of fra = Skt. pra, and sparaya : Skt. spurj- ‘burst forth, roar’) and fravazs- (cpd. of fra and vazés- ‘srow’) in this sequence, Yasna 10.5, are taken as ‘branch’—‘twig’ by Darmesteter and Mills (also frasparaya rendered by cakha- in Skt. translation), but as ‘twig’—‘stem, branch’ by Barth. (fras- paraya- rendered by spik ‘twig’ in Pah- lavi translation). Barth. 991, 1003.
8.56 LEAF
$iddov Goth. Jlaufs Lith. Jlapas
"taro ON laufsblad (lauf, blad) Lett. lapa folium Dan. _ blad (I¢v) ChSl.  listit foglia Sw. blad (laf) SCr. list feuille OE léaf (bled) Boh. list
.  hoja ME _leef Pol. lise
```


## [2026-09-06T15:46:03.649Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN cake\"; grep -n -iE \"^cake|^cooky|^cookie\" KLN_1966.txt KLN_1971.txt | head; echo \"=== SKT cake\"; grep -n -iE \"^cake|^cooky\" SKT.txt | head; echo \"=== LKT kek\"; grep -n -iE \"keks|kaʿk|ka.k\\b\" LKT.txt | head"
}
```


### [2026-09-06T15:46:03.743Z] TOOL RESULT

```
=== KLN cake
KLN_1971.txt:36880:cake, n. — ME., fr. ON. kaka, rel. to MDu. koke, 
KLN_1971.txt:46784:cake {Anglo-Indian). — Hind, chapati, fr. OI. 
KLN_1971.txt:56258:cooky, also cookie, n., a small cake. — Du. koekje, 
KLN_1971.txt:93962:cake’, G. Fladen , ‘flat cake’, Du. via , ‘baked 
KLN_1971.txt:142198:cake’, payeu?, ‘one who kneads, baker’, OSlav. 
KLN_1971.txt:183608:cake’, Swed., Norw. ftundra, MHG. vluoder , 
KLN_1971.txt:250285:cake’, fr. Late L. torta, of s.m., which is of un- 
KLN_1971.txt:267153:cake 5 , rel. to MDu. wegge, OE. wecg, ‘wedge’. 
KLN_1966.txt:6116:cake,  n.  —  ME.,  fr.  ON.  kaka,  rel.  to  MDu.  koke, Du.  koek,  its  dimin.  koekje,  OHG.  chuohho, kuocho,  MHG.  kuoche,  G.  Kuchen;  prob.  of imitative  origin.  The  a-o  gradation  of  these words  testifies  to  their  Teut.  origin  (cp.  ON. taka,  ‘take’,  tok,  ‘took’).  They  are  not  related to  cook.  Cp.  cooky,  kuchen.  Cp.  also  Cockaigne. Derivatives :  cake,  v.,  cak-y,  adj.
KLN_1966.txt:9093:cooky, also  cookie,  n.,  a  small  cake.  —  Du.  koekje, dimin.  of  koek,  ‘cake’.  See  cake  and  dimin. suff.  -y.
=== SKT cake
=== LKT kek
905:'Die  Pflanze  Piper  betel  L.  Betelpfetfer' mit  kleinen  roten  Blüten.  Ihre  Blätter werden  von  den  Europäern  Betel  ge- nannt; in  sie  werden  die  Arekanüsse [s.  hier  Nr.  17]  mit  Kalk  eingewickelt und  so  in  ganz  Südasien  als  Narkotikum, ähnlich  wie  bei  uns  der  Kautabak,  viel benutzt.
2386:Vollständig-  kafr  aljahüd  'Judenpech, Asphalt';  hieraus  sp.  acafelar  'Tür  oder Fenster  zumauern,  eine  Wand  mit Gips  oder  Kalk  tünchen'  [Dicc  Gast  21a], pg.  acafelar  'mit  Stein  und  Kalk  zu- mauern' [Constancio  Dicc  9  c].  —  DE 51/52.
2419:'Boot;  langer,  sehr  spitz  zulaufender  und von  leichtem  Holze  gebauter  pfeilschnel- ler Kahn';  hieraus  bulg.  serb.  kaik  'Kahn für  10  Mann',  poln.  kaik,  klruss.  kajuk 'Flußboot',  russ.  kaik,  kajuk  'Boot,  Last- schiff ;  rum.  caic  'Bai'ke',  caicgiü  'Barkeii- führer',  it.  caicco  'kleine  Barke  als  Ret- tungsboot, Schaluppe',  siz.  caiccu  auch 'Kuppler',  frz.  culq,  ca'ique,  calc\  ndl. kaick,  engl,  ca'ique  'Schaluppe,  Boot  auf dem  Bosporus  und  dem  Schwarzen Meere'. —  [Hobson-Jobson  143  fragt  mit Recht,  ob  das  Wort  zufällig  oder  durch tk.  Sprachverwandtschaft  hmdurch  mit dem  grönländischen  kajak  gleichlautet]. [Gorjajew  158.  Bern  SlEtWb  469.  Gr SVociSic  229.
2777:'Kalk'  [Kelekian  Kämüs  1066] ;  hieraus bulg.  kirec,  serb.  krec  'dass.'.
4747:'Zink,  Zinkoxyd'  [vielleicht  aus  dem  Ind. ZDMG  L,  650;  vgl.  auch  gr.  toutio; früher  bei  den  im  Orient  häufigen  Augen- erki  ankungen  benutzt],  ebenso  tk. ;  hier- aus rum.  tutea  'Zinkoxyd',  sp.  pg.  atutia, kat.  tutia,  frz.  tutie,  tuthie  'dass.';  poln. tucyja  'Art  Zinkkalk';  eng],  tntty  'Zink-
4814:Nach  Hobson-Jobson  89/90  soll  dieses Wort  'einfaches,  bloßes  Blatt'  bedeuten, es  ist  also  wohl  mal.  betul  [Pijn  32  b] 'echt,  wahr'  und  ist  für  den  Malayen das  Blatt  k.  €.,  nämhch  von  Chavica betle  Miq  ,  einer  Kletterpflanze  aus  der Familie  der  Fipeiaceen.  Hieraus  pg. helle,  betre,  betel  [Gonstancio  Dicc  171c], sp.  betel,  frz.  betel:  engl,  betel,  betle,  dtsch. Betel.  —  Man  wickelt  den  Kern  der Frucht  der  Arekapalme  Areca  Catechu  L. [s.  hier  Nr.  17]  in  das  Blatt  der  Chavica betle,  mit  etwas  Kalk  gemischt,  und kaut  dies  als  Narkotikum.  Die  Sitte  des Betelkauens  ist  in  allen  indischen  und malayischen  Ländern  weit  vei  breitet. Vgl.  L.  Lewin,  Über  Areca  catechu, Chavica  betle  und  das  Betelkauen.  Stutt- gart 1889;  über  die  sprachliche  Seite SCHMIDT  in  ZDMG  LXVII,  6.53/659.
7653:kabala  977 kaban  975 Ä;a6a^  971 kaczan  1192 Ä:a(ft  984 fcarfy  984 kafenauz  1005 kaftan  Iii. kaik  1014 kalauz  1276 Ä;a/efca  1040 kaleta  828 Ä;afÄ;aw  1034 kalkun(t)  1031 kamcha  1043 kamfora  1100 katnlot  653 kanczug  1042 kanczuk  1042 kanfora  1100 kaparki  978 kapary  978 kapinaz  1005 kapkan  1064 karabacz  1279 karaczan  2027 karafka  689 karawana  1075 karbacz  1279 karhona  1208 karbuz  824 karczma(rz)  825 karczoch  833 kardasz  1089 fcary  1070 Ä:a<MM  1272 ÄsttM^a  1005 kawak  1134 kawiar  851 kawon  1138 kazan  1144 kazna  855 kazmirek  1116
```


## [2026-09-06T15:46:14.791Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM كعك\"; grep -n \"كعك\\|الكعك\" AFM_pages.txt AFM.txt 2>/dev/null | head; echo \"=== AFA\"; grep -n -i \"ka.k\\|Kuchen\" AFA.txt | head -10; echo \"=== FVQ\"; grep -n -i \"ka'k\\|kaʿk\" FVQ_pages.txt | head"
}
```


### [2026-09-06T15:46:14.881Z] TOOL RESULT

```
=== AFM كعك
=== AFA
906:Schon frühe ist auch der Name des Kalkes luJjT aus
916:Noch ein anderer Name des Kalkes ^Ia^ (belegt mit
1736:(mit Yarr.) »ein Kuchen, den man vom Teige genommen
1809:Hui andeutet, webender Achnlichkcit mit einem solchen Kuchen benannt, son.
1848:diese Einwriude. {kotttxI sind auch speciell Kuchen aus
2565:Martin, Trad. Karkaph. facsira. nr. 2 und seinen Jacques
5916:2) Davon iSsüS BekH 160, 4. ErkUmngd«>s Kloster Karkaph |>>1»^ ^
6623:2) >,^J.^g •dünner Kuchen** ist wie iithiop. sarikat beweist ein Fehler für
6625:schon in der Tosepht.i als «dünne Kuchen'* gilt. AuJallig ist dann allenilni;8
10014:ten ohne Kalk und Tünche im heutigen Jemen Tgl. Renzo
=== FVQ
```


## [2026-09-06T15:46:18.403Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1730,1745p' AFA.txt; echo \"=== search kak in AFA\"; grep -n -iE \"\\bk[a']{1,3}k\\b|كعك\" AFA.txt | head"
}
```


### [2026-09-06T15:46:20.593Z] TOOL RESULT

```
ben das Syrische sowohl wie das Jüd. aram. das Original
erhalten: IriLsi-i und jüd. D'S'l^. Das jüdische Wort
findet sich im Talmud selbst nicht mehr, wohl aber noch
in einer jedesfalls aus gfiönilischer Zeit herrührenden Er-
klärung im ^Aruch s. v. DDH U. Es heisst dort zu San-
hedrin 14» = Kethuböth 17* f^DDIÜO N^l f^DalDQ N^
(mit Yarr.) »ein Kuchen, den man vom Teige genommen
hat u. so backt, wie er ist, kugelförmig, ohne dass man ihn
glatt und eben gemacht hat, wird 0*^31^12 genannt."
Ohne in eine Discussion über die Richtigkeit der Erklä-
rung des talmudischen Wortes einzugehen, ist der Ge-
danke, als könne dies D^^S'l^bS erst aus dem Arabischen
(das U fällt allerdings auf) eingedrungen sein . abzuweisen ,
weil in solchen Fällen ein ^«^32^^ fVj^^S oder n'^CS
(ri^ir**U3) nie fehlt. Abgesehen davon aber haben wir das
Syrische als deutlichen Beweis, dass das Wort im Aramä-
=== search kak in AFA
```


## [2026-09-06T15:46:29.740Z] TOOL CALL #70: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:46:29.749Z] TOOL RESULT

```


```


## [2026-09-06T15:46:34.781Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%AE",
 "prompt": "Give the full Persian etymology section for شاخ (šāx) 'horn, branch': the Middle Persian form, Proto-Iranian reconstruction, and cognates (Sanskrit śākhā etc.). Quote it."
}
```


## [2026-09-06T15:46:36.094Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%B9%D9%83",
 "prompt": "Give the Arabic etymology of كعك (kaʿk) 'cake, biscuit' — what language it is said to be borrowed from (Aramaic/Syriac, Persian, Latin?), and quote the etymology text and any Persian/Syriac forms cited."
}
```


### [2026-09-06T15:46:41.473Z] TOOL RESULT

```
# Etymology of كعك (kaʿk)

According to the Wiktionary entry, كعك is "Derived from or cognate with Aramaic" rather than borrowed from Persian or Latin.

The etymology text states:

> "Derived from or cognate with Aramaic _כַּעְכָּא_ / _ܟܥܟܐ_ (kaʿkā, 'cake, loaf'), from Akkadian _𒈖_ (kukku, 'cake, loaf, pastry, lump of dough')"

The document traces the word's origins further back to Sumerian _𒈖_ (gug, "offering; cake"), describing it as a widespread wanderwort found across multiple language families, with cognates in Egyptian and Proto-Indo-European.
```


### [2026-09-06T15:46:42.668Z] TOOL RESULT

```
# Persian Etymology of شاخ (šāx)

Based on the Wiktionary entry, here is the Persian etymology information:

**Proto-Indo-European Origin:**
The word traces back to Proto-Indo-European *ḱókh₂eh₂ ("branch"), inherited through Proto-Indo-Iranian *ćā́kʰaH.

**Cognates Listed:**
The entry identifies several related words across Indo-European languages:
- Sanskrit शाखा (śākhā, "branch, twig, limb, finger")
- Old Armenian ցախ (cʻax, "branch, twig")
- Lithuanian šakà ("branch")
- Gothic 𐌷𐍉𐌷𐌰 (hōha, "plough")
- Old East Slavic соха (soxa, "stake, club, brace, plough")
- Old Irish géc ("branch")

**Direct Quote from Etymology Section:**
"Inherited from Proto-Indo-Iranian *ćā́kʰaH, from Proto-Indo-European *ḱókh₂eh₂ ('branch')."

Note: The Wiktionary entry does not explicitly provide a Middle Persian form for this term.
```


## [2026-09-06T15:46:56.834Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B3%D8%AA%D9%86",
 "prompt": "Give the Persian etymology of کاستن (kāstan) 'to decrease, diminish': Middle Persian form, Proto-Iranian root, Avestan cognates. Quote the etymology."
}
```


## [2026-09-06T15:46:58.223Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cake",
 "prompt": "Quote the full etymology of 'cake' — Old Norse kaka, Proto-Germanic, and whether any Semitic/Egyptian source is mentioned. Also anything about 'cookie'."
}
```


### [2026-09-06T15:47:02.658Z] TOOL RESULT

```
# Persian Etymology of کاستن (kāstan)

The word derives from **Proto-Iranian *kas-** meaning "to be small, diminish, lessen." 

According to the Wiktionary entry, it is "Cognate with" several related forms across Iranian languages. The **Avestan cognate** is listed as **𐬐𐬀𐬯𐬫𐬀𐬵 (kasyah)**, meaning "smaller, lesser."

The entry notes that **Middle Persian** had the form **ks**, meaning "small(er), less(er), young(er)," which served as an intermediate stage in the word's development from Proto-Iranian to modern Persian.

The root shows remarkable continuity across Indo-European languages, with suggested comparisons to German *hager* ("gaunt") and Lithuanian *kašėti* ("to lessen, become thin").
```


### [2026-09-06T15:47:05.501Z] TOOL RESULT

```
# Etymology of "Cake"

**Full Etymology:**
The word "cake" comes from early 13th century Old Norse *kaka*, which derives from West Germanic *\*kokon-*. This appears in related forms across Germanic languages: Middle Dutch *koke*, Dutch *koek*, Old High German *kuohho*, and German *Kuchen*. The entry explicitly states it is "not believed to be related to Latin *coquere* 'to cook,' as formerly supposed" and replaced the Old English cognate *coecel*.

**Semitic/Egyptian Sources:**
No Semitic or Egyptian sources are mentioned in this etymology.

**On "Cookie":**
The article notes that "cookie" (meaning "small, flat, sweet cake") derives from Dutch *koekje*, a diminutive of *koek* "cake," which itself traces back through Middle Dutch *koke* to the same Germanic roots as "cake." The cookie entry references: "from Dutch koekje 'little cake,' diminutive of koek 'cake,' from Middle Dutch koke (see cake (n.))."
```


## [2026-09-06T15:47:12.126Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-%DA%A9",
 "prompt": "Give the Persian suffix -ak (ـک) entry: its meaning (diminutive) and its etymology — Middle Persian -ak, Proto-Iranian *-aka-, PIE *-kos? Quote the etymology section."
}
```


## [2026-09-06T15:47:13.202Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%DA%A9",
 "prompt": "Is there a Persian entry کاک (kāk)? Give any senses ('dry bread', 'brother') and etymology given."
}
```


### [2026-09-06T15:47:14.229Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:47:19.469Z] TOOL RESULT

```
# Persian Entry: کاک (kâk)

Yes, there is a Persian entry for کاک (kâk). According to Wiktionary, the word has multiple senses:

**Senses:**
1. "a kind of layered pastry"
2. Archaic: "a kind of bread"
3. Archaic: "dry bread" (synonym: نان خشک)
4. Archaic/anatomy: "pupil" (of the eye)
5. Archaic: "full moon"

**Etymology:**
The entry notes the term is "akin to Gilaki کاکا (káká, 'a kind of cookie'), Kurdish, Arabic كعك (kaʕk), and Classical Syriac ܟܥܟܐ (kaʿkā)."

The entry does not list "brother" as a sense. The primary modern meaning appears to be the layered pastry, with other definitions marked as archaic.
```


## [2026-09-06T15:47:23.766Z] TOOL CALL #77: WebSearch

```json
{
 "query": "Wiktionary Persian diminutive suffix -ak ـک Middle Persian -ak Proto-Iranian *-aka",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


### [2026-09-06T15:47:32.649Z] TOOL RESULT

```
Web search results for query: "Wiktionary Persian diminutive suffix -ak ـک Middle Persian -ak Proto-Iranian *-aka"

Links: [{"title":"نیک - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%DB%8C%DA%A9"},{"title":"ـه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%80%D9%87"},{"title":"-ակ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/-%D5%A1%D5%AF"},{"title":"اینک - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86%DA%A9"},{"title":"ـی - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%80%DB%8C"},{"title":"-आ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/-%E0%A4%86"},{"title":"Wiktionary:Persian entry guidelines - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Wiktionary:About_Persian"},{"title":"Category:Middle Persian suffixes - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_suffixes"},{"title":"Category:Persian suffixes - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_suffixes"},{"title":"Category:Persian terms by suffix - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_by_suffix"}]

Based on the search results, I found relevant information about the Persian diminutive suffix -ak ـک and its etymological connections:

The Persian suffix -ak comes from Middle Persian -k' (-ag), from Proto-Iranian *-akah, from Proto-Indo-Iranian *-akas.

The suffix -ak (ـک) is used as a diminutive suffix in Persian. For example, the word نیک (nik, "good") comes from Middle Persian nēk, and is equivalent to نیو (niv, "brave, valiant") plus the diminutive suffix -ak.

The search results also show comparative evidence: Compare Old Armenian -ակ (-ak), indicating this suffix has related forms in other Indo-European languages.

Additionally, the results document the suffix's use beyond just diminutives, as noted in a scholarly reference that states "[The suffix] -ak (-k) makes diminutives: and 'so much': and-ak 'a little'; nēw 'good': nēk 'good'; Man. M Pers. kōdak and kōdag 'small'".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:47:39.644Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^شاخ\\|شاخ \" incoming/ARY/ARY_pages.txt | head -10; echo \"=== kastan\"; grep -n \"کاستن\\|کاهیدن\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== kak\"; grep -n \"^کاک\\|کاک \" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-06T15:47:39.718Z] TOOL RESULT

```
601:شاخه‌های زبانهای هند و اروپایی ی
6063:چم این واژه در زبان انگلیسی کهن: شاخ و برگ» برگ دادن,
10966:در فارسی شاخ دارای دو چم است: سرودن با شاخ جانور و شاخه‌ی گیاه.
=== kastan
=== kak
```


## [2026-09-06T15:47:42.813Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10950,10985p' incoming/ARY/ARY_pages.txt; echo \"=== pdf page tag\"; awk 'NR<=10966 && /\\[pdf page/{p=$0; n=NR} END{print n, p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T15:47:44.655Z] TOOL RESULT

```
کر دی (821574(ا): آاکتختزه ۰ 1111011
بلوچی (لللعنابلمه): ۳ ,لل52 اسلاوی کهن (۲16ماد هنابز صرم,
افغانی (پشتو) (4۳01۸/1): ختا806
ٍ ۸5 بالق بقظترو لهستانی (/۶0/5): 020۸
سانسکریت (۸/812/7مع), رومی (0951۸(0): ۸ تناو
1 بقتل526 بقانةه یترانی (00هااهمناب12م, 4 ان
آرمنی (4527۸(م). تا بخ لتونی (لتی) (701۸مل): ی
گو نیک (007]/0): 110۸ پروسی کهن (الفاددتا2 هام کرو
[pdf page 370]
شاد / ۳۷۱
اپرلندی کهن (5ل2/ صا0):
7 ,0380۸5 پسگشت‌ها 5
گالی (بققلاناه): هه ۲۰ ۳
ولزی (ک8): هه 0 (68۸۲6) جازم 02
آلبانی (4لهالمقله): 76 برهان قاطع + ۱۳۹
یادداشت: 8
در فارسی شاخ دارای دو چم است: سرودن با شاخ جانور و شاخه‌ی گیاه.
اوستایی (۸۷887۸2۷): ابسلندی کهن ((701۸۸۷4(ی5 ضا0):
71 ,57187۸ ,511۸۷270 ۲۷۲۸
پارسي باستان (۳28۵(۷ 012): 811۳۷2718 تورس کهن (۸08۶5 0ا0): زره ایا
پهلوی (۲7هاتلهه): ۸ ,0ق5 ساکسونی کهن (542:0۸ 012): رید
آوستی (0558716): فریزی کهن (/(4ا5ل۴۲ صا0): ند 8 انا
7 ,22613۸0 ,۸۲۸94 آلمانی کهن (/(۸/ن027 بلاط صز:
کردی (03/0[54): 510 ۷۸ ,ش1۷11
بلرچی (اتللاملم8): رازن آلمانی (68721۸21): 2 اد ریا
تخاری 8 (8 ۸۸ل7052۸): ۵:۳۷ انگلیسی کهن (0کلا80/0 ۰:00 ,1711
سفدی (/(۸ا300۸2): ان انگلیسی (#ل5لباه67): ۲/8۵
سانسکربت (8۸(/58/7): 0۳ دانمارکی (0۸(/184): ۷1
ارمنی (لفا اگم سوئدی (87201577): ۸آ]۷
ی 7 11۸01667310 نروژی (۸۸0۲804۷: ۰ 6۷۲۳8 بلتا30
لاتین (3(0سل): 0 01۹ اسلاری کهن (ع۷۲بما؟ بط#نابن 0ا۵):
فرانسه کهن (ل۸۷ظ۲۴ صان): ۰ 0-1815 71 با[۳050
اسپانیایی (5۳۸۸/5): 017820 ,01-1870 ۱
ایتالپایی (انمته7): ۰ 613270 ,0171270
پرتغالی (۳0770017885): 010 :
گرتیکك (00774/6): 17781۸
=== pdf page tag
10958 [pdf page 370]
```


## [2026-09-06T15:48:00.980Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%95%E0%A4%B2",
 "prompt": "Give the Sanskrit entry शकल (śakala): meaning and etymology (which PIE root / Pokorny root it is assigned to)."
}
```


## [2026-09-06T15:48:02.884Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%DA%A9%D9%84%D9%87/",
 "prompt": "Give the دهخدا / معین / عمید entries for شکله — the meaning and any etymology (Sanskrit śakala?)."
}
```


### [2026-09-06T15:48:03.058Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:48:10.994Z] TOOL RESULT

```
# شکله Dictionary Entries

## Dehkhoda (لغت نامه دهخدا)
Multiple senses are recorded:

1. **Color**: "سرخ و سپیدی" (red and white coloring), specifically redness mixed with whiteness, often describing the eye.

2. **Resemblance**: "همانندی. مشابهت" (similarity, likeness)—as in the phrase "فیه شکلة من ابیه" (there is a resemblance to his father in him).

3. **Woman**: "زن با ناز و کرشمه" (a woman with grace and charm).

4. **Cloth fragment**: A piece of cloth or fabric that becomes torn when tied to something.

5. **Melon slice**: "پارچه ای که با کارد از خربزه و هندوانه...بردارند" (a strip cut from melon or watermelon with a knife).

## Moein (فرهنگ معین)
"یک برش یا قاچ از هندوانه و مانند آن" (a slice or piece cut from watermelon or similar fruit).

## Amid (فرهنگ عمید)
Two entries: torn cloth stuck on nails or branches; or a small piece of melon/watermelon cut with a knife.

**Note**: No Sanskrit etymology is mentioned in the provided content.
```


## [2026-09-06T15:48:21.089Z] TOOL CALL #82: Bash

```json
{
 "command": "ls site/pages/235.jpg 2>/dev/null || pdftoppm -f 235 -l 235 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg235 && echo done"
}
```


### [2026-09-06T15:48:22.796Z] TOOL RESULT

```
site/pages/235.jpg
done
```


## [2026-09-06T15:48:25.024Z] TOOL CALL #83: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/235.jpg"
}
```


### [2026-09-06T15:48:25.053Z] TOOL RESULT

```

```


## [2026-09-06T15:48:42.177Z] TOOL CALL #84: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp site/pages/235.jpg data/verification/sources/refs/ocr/BOOK/235.jpg 2>/dev/null; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg235.png data/verification/sources/refs/ocr/BOOK/235.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-06T15:48:42.297Z] TOOL RESULT

```
Exit code 1
cp: cannot stat '/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg235.png': No such file or directory
```


## [2026-09-06T15:48:45.574Z] TOOL CALL #85: Bash

```json
{
 "command": "pdftoppm -f 235 -l 235 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/235 && ls -la data/verification/sources/refs/ocr/BOOK/235*"
}
```


### [2026-09-06T15:48:48.021Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 69091 Sep  6 11:48 data/verification/sources/refs/ocr/BOOK/235.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 73781 Sep  6 11:48 data/verification/sources/refs/ocr/BOOK/235.png
```


## [2026-09-06T15:48:58.459Z] TOOL CALL #86: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/شاخ|page 235, root Kâk 2, Persian šâx: Wiktionary says inherited from PII *ćā́kʰaH < PIE *ḱókh₂eh₂, cognate (not descendant) of Skt śākhā\" \\\n \"https://en.wiktionary.org/wiki/كعك|page 235, root Kak 4, Arabic ka'k: Wiktionary derives it from/cognate with Aramaic kaʿkā < Akkadian kukku < Sumerian gug (wanderwort)\" \\\n \"https://en.wiktionary.org/wiki/کاستن|page 235, root Kak 3, Persian kâstan: Wiktionary from Proto-Iranian *kas- 'to be small, diminish', Av. kasyah-\" \\\n \"https://www.etymonline.com/word/cake|page 235, root Kak 4, English cake/cookie: Etymonline derives cake from ON kaka < W.Gmc *kokon-, cookie from Du. koekje; no Semitic source\" \\\n \"https://en.wiktionary.org/wiki/کاک|page 235, root Kak 4, Persian kâk: Wiktionary senses 'dry bread' etc., akin to Arabic كعك and Syriac kaʿkā\" \\\n \"https://abadis.ir/fatofa/شکله/|page 235, root Kâk 2, Persian šeklah: Dehkhoda/Mo'in/Amid give 'torn piece of cloth; slice of melon', no etymology\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; timeout 120 python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:49:04.131Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/edb44ac7a81d8643.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d0b838ba560418ea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0baec37fed01db4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16fb413c45af20d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36c514949524b2a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3fa88dcc399ed09.txt
```


## [2026-09-06T15:49:09.804Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%80%DA%A9",
 "prompt": "Persian suffix ـک (-ak): give its meaning and etymology (Middle Persian, Proto-Iranian) verbatim."
}
```


### [2026-09-06T15:49:15.199Z] TOOL RESULT

```
# Persian Suffix ـک (-ak)

## Meaning

According to the Wiktionary entry, this suffix has three primary functions:

1. "suffix which forms diminutives"
2. An alternative form of ـه (-e), which creates words meaning "pertaining to, related to"
3. In Yazd dialect, it marks nouns as definite

## Etymology

The entry states it was "Inherited from Middle Persian" with the form shown as /⁠-ak⁠/. However, the page does not provide information about Proto-Iranian origins—only the Middle Persian source is documented in the etymological section.

The Middle Persian ancestor is listed but marked as a missing etymon link, so the complete Proto-Iranian reconstruction is not included in this Wiktionary article.
```


## [2026-09-06T15:49:18.593Z] TOOL CALL #88: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/ـک\" --note \"page 235, root Kak 3, Persian suffix -ak: Wiktionary derives it simply from Middle Persian -ak (diminutive), not from Av. kasu-\" 2>&1 | tail -2"
}
```


### [2026-09-06T15:49:21.018Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d63d044e44b9a1a7.txt
```


## [2026-09-06T15:49:27.159Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '340,345p'; echo \"=== find page 335\"; awk '/\\[pdf page 3[0-9][0-9]\\]/{print NR\": \"$0}' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T15:49:29.472Z] TOOL RESULT

```
=== find page 335
```


## [2026-09-06T15:49:33.569Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 incoming/WLD/WLD_Bd1_pages.txt; grep -c \"\" incoming/WLD/WLD_Bd1_pages.txt; grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo \"=== search sakha\"; grep -n -i \"sakha\\|çakha\\|kakan\\|kaka \" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T15:49:33.655Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

81975
=== search sakha
23793:skaka „schutteln“ (s. u. sqeq- „spiingen ££ _, vorzuziehen. 
24004:kaka (aber fiir „Gro£Svater, -mutter") in afrik. Sprachen.
```


## [2026-09-06T15:49:36.853Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23990,24020p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T15:49:36.905Z] TOOL RESULT

```
Falk-Torp u. nype , Schroder Abl. 62 f. (: mnd. wepe „Hagebutte“ unter 
*heuep- ?). 

keq“- „cacare, Mist". 

Ai. gdkrt , Gen. gakndh „Hist'‘, gr. xojiqo? „Mist, Diinger, Schmutz" (setzt 
das r des ai. Nom.-Acc., aber ohne dessen - 1 , voraus, s. Bartholomae BB. 
15, 41; ein nicht zum o-St. umgebildetes Paradigma *x6jicoq, *xo7iato ; nach 
Art von vdoQ, -aiog vermutet Brugmann II 2 1, 579 als Ursache dafiir, daS 
oxtbg den Gen. zu axarog umbildete); lit. sikii, sikti „cacare“. Z. B. Fick 
I* 42, 205 f., 421, Hirt BB. 24, 230. Yielleicht nach Fick II 4 66, Stokes 
KZ. 33, 78 hierher auch air. cechor Gl. „palus", mir. cechair „Schlamm, 
Unflat, Kot“ (wenn „leibliche Ausscheidung" die urspriingliehe Bed. ist). 
S. nach *kakka „cacare“, und Kretschmer Einl. 353 iiber das Lallwort 
kaka (aber fiir „Gro£Svater, -mutter") in afrik. Sprachen. 

kek- „Wiesel, Iltis“. 

Ai. kaca- m. kaclka f. ,,’Wiesel", aber mit anl. Pal. lit. heskns „Iltis“ 
lett. sesks ds. Fick I 4 22, Zupitza KZ. 37, 401. Ist bait, s- durch progress. 
Ass. von *keskas zu erklaren, wobei die Nachholung des im Anlaut ver- 
drangten k- im Ausgang der 1. Silbe durch den Anlaut k- der 2. Silbe 
verhindert ^yurde? 

keqO- „Grunfutter, frisches eBbares Grun“. 

Ai. gdka- m. n. „eBbares Kraut, Gernuse"; lit. sekas „frisch gemahtes 
Gras, Griinfutter", lett. seks ds., apr. schokis „Gras“ (dies zunachst aus 
*sjakas; -jd- aus -< 7 - ?) ; aisl. ha f. „Grummet“ (void aus germ. *hehon-; 
an sich auch auf *hiihdn -, oder, unter Annahme labiovelaren Anlauts, auf 
*hahwon , *he(^)wun- zuriickfiihrbar).
```


## [2026-09-06T15:49:43.773Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gakha\\|saka „Ast\\|Ast, Zweig\\|,,Ast\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T15:49:43.828Z] TOOL RESULT

```
4866:Aber lat. ramus „Ast, Zweig“ ist trotz Hirt Abl. 76 (und Charpentier Gl. 6, 
18263:Lat. radix, -lets ..Wurzel -- ; wahrscheinlich ramus ,,Ast, Zweig" (als 
21134:kak- (oder kok-?), nasaliert kank- (oder kouk-?) : knk- ,.Ast, Zweig. 
21148:,,Ast ‘ (mit sekundarer Media im Anlaut, s. Zupitza KZ. 37, 392, Pedersen 
24132:kaum zu anord. lair , kail, s. u. kak- ,,Ast"). Die Yerbindung der germ. 
40301:Russ, gohja „Zweig“ (usw., s. Berneker 326); arm. kofr „Ast, Zweig“ 
51225:„Ast, Zweig" (nicht zur Zweizahl wie dt. Zweig, trotz ahd. zuelga „Zweig“,
```


## [2026-09-06T15:49:46.306Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21134,21160p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T15:49:46.357Z] TOOL RESULT

```
kak- (oder kok-?), nasaliert kank- (oder kouk-?) : knk- ,.Ast, Zweig. 

Pflock“. 

Ai. cdJcha „Ast" (: got. hoka, arm. rax .) ; c/ikala- m. n. „Span, Splitter. 
Holzscheit, Schnitzel, Stfickchen" (: lit. sakcdf/s ); qanku- m. „Holznagel, 
Pflock, Pfahl, Stecken" (: aksl. sriko, cymr. cainc , anord. liar)-, rakti - f. 

, , Speer" (: air. cccht ): 

arm. rax „Zweig“ (= ai. qdkha, s. Bartholomae BB. 10, 290, Stud. II II): 

cymr. cainc \^kanku oder knku, vgl. den «-St. ai. qatalcn--, Pedersen 
KG. I 372, II 88), pi. cangau, mcymr. canghau „Ast“, mir. gcc, nir. gcag 
,,Ast ‘ (mit sekundarer Media im Anlaut, s. Zupitza KZ. 37, 392, Pedersen 
KG. I 494), mit -s/Ao- Suffix air. gescae „Zweig, Ast", mit /-Suffix air. c edit 
„Pflug“ (wohl als *knk-to- nachstverwandt mit ai. rakti-, das eher a = n 
als = a oder 0 hat; nicht besser zu ai. hhokqta- m. „Kamm u. dgl.“. 
Uhlenbeck Ai. Wb. 301 zw.); got. liTJta ..Pflug" (= ai. qdkha), ahd . hnohtlt 
„aratiuncula“ ; nas. anord. liar ,,Ruderdolle" (*hanha; s. auch Boisacq u. 
y.rjrog), hall „Pflock, Stock" ( *hanhila-; Liden Uppsalastud. 89f. ; da- 
gegen ahd. hahila. -ala ,,Kesselhaken" mnd. hale ds. wohl zu liiingcn. 
Falk-Torp u. lirel)-, lit. ;aka „Ast" (abl. mit ai. qukha), take ..Gabel". 
sakalys „Splitter" (:ai. rdkala -), salniis, apr. saynis {., lett. sakne ,,Wurzel" : 
aksl. sqH „surculus"; wegen der Bed. unsiclier alb. -deles ,.Franse, Zipfel" 
(Pedersen KZ. 36, 332, KG. I 126; vgl. immerhin dieselbe Bed. von norw. 
hekel .Zipfel" u. *keg-).
```


## [2026-09-06T15:49:54.264Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gag- gog-\\|gag-, gog-\\|gog- „\\|kaka „Kuchen\\|Kuchen“\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T15:49:54.307Z] TOOL RESULT

```
19530:Im Ablaut wohl ahd. wastel (frz. gateau ) „Kuchen“. tTber Beziebuug zu 
28628:') ^icht nach Hirt BB. 24, 278 zu apr. kalso ,,flacher Kuchen“, das aus poln. kolacz 
33329:ghauo gag-, gog- 
33387:gag-, gog- „etwas Rundes, Klumpiges". 
33403:„kleiner Kuchen“; lit. guoge „Kohlkopf, Kopf, Dickschadel", guog'ingus „mit 
33411:(fin. kakko, lapp. gakko „Kuchen“, fin. kakkara „Erdscholle, Erdklumpen,
```


## [2026-09-06T15:49:56.960Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33387,33420p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T15:49:57.006Z] TOOL RESULT

```
gag-, gog- „etwas Rundes, Klumpiges". 

Isl. ha ha ,.Ivuchen ', norw. und schw. h-iha , kleines, rundes und flaches 
Hrot", diin. huge ..Kuchen", wozu das Deminutiv ags. cicel, eyed ..kleiner 



g'„ l hagk ghadh- 


531 


Kuclien" (engl. cake ist nord. Lehnwort) und ablautend norw. kok „Klum- 
pen“, scliw. koka „Scholle, Erdscholle", mnd. kuke, ahd. kuocho „rundes 
Brot, Kuchcir , dazu die Deminutiva ags. cocci! , Cecil und ahd. kuochelvn ) 
„kleiner Kuchen“; lit. guoge „Kohlkopf, Kopf, Dickschadel", guog'ingus „mit 
Kopf versehen", guogioti „Kopfe ansetzen (vom Kohl)“. — Da idg. Wurzeln 
mit unaspirierter Media nicht zugleich an- und auszulauten pflegen (siehe 
gSb-), bleiben an der sonst tadellosen Zusammenstellung Zweifel. 

Pick III 4 33, Falk-Torp 4S3, Trautmann KZ. 43, 176. 

Germ, kokon wegen der Ablautsformen und der fin.-ugr. Lehnworte 
(fin. kakko, lapp. gakko „Kuchen“, fin. kakkara „Erdscholle, Erdklumpen, 
Brot" vgl. Thomsen fiber den Einflufi der germ. Sprachen 138) nicht aus 
dem Romanischen, vielmehr umgekehrt nach Meyer-Liibke Rom.-E. Wb. 
Nr. 4734 u. Gamillscheg EWb. d. Franz. 232) prov. katal. coca „Kuchen" 
aus got. *koka (anders Schuchardt, SBdAdW. Wien 141,23). 

Abzulehnen Woods (Mod Lang Notes 19, 2) Verbindung der germ. Worte 
mit lit . guzgs „Ivropf" usf. (s. fiber diese Sippe Trautmann Bsl. Wb. 101 f.). 

ghagl'li- „Junge eines Tieres, bes. eines Vogels 1 '.
```


## [2026-09-06T15:50:05.462Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"k[āa]kh?[āa]|sakha|cakha\" IEC.txt | head -15; echo \"=== gogos\"; grep -n -iE \"^gog|^gag\" IEC.txt | head"
}
```


### [2026-09-06T15:50:05.530Z] TOOL RESULT

```
3848:gagodio (gogodio) ‘chatter’. Cf. gagotio, gagorió Arm. kakazem ‘stammer, jabber, lisp’; MHG kachezen ‘guffaw’; OE ceahhetan, id.: E chat. Cf. also OE ceahhe ‘daw, chough’
3866:gagətið (gogotio) cf. gagodio, gagó, gagol- Arm. kakacem ‘cackle’; Cor. gesya “mock, jeer’; (MHG cf. kachezen, OE ceahhetan, E chat, fr. *gagodio); OCz. hohcu, hohtati ‘cackle’; R gogotàt, id.; gógot, m. id.
5101:guag- (2), guāg- ‘quack, squeak, squeal’ Per. cf. žāž ‘twaddle’; Oss. cf. zågin, pp. zagd ‘say’; Arm. cf. kakan, a-st. ‘clamour, lament’; Gk. bázō ‘talk’, bágma ‘talking’; cf. babáx *prattler'; Alb. cf. gagac, adj. ‘stammering’; ON kvaka ‘chirp’; G quaken ‘moan, complain’; Du. kwaken ‘quack, croak’; Li. (ambig.) gagiu, eti (*quack', see gag-). Long vowel in Lat. vā- gire, v. ‘scream’; Slovene gágam, Blg. gagam ‘cackle’; Latv. gāgāju, id. and cf. Li. gógšiu, gókšiu, eti ‘sob’; gókčioju (2) ‘squeaľ
6623:kakā (kakk-) ‘excrement’. WP I, 336 Per. kak ‘biscuit’; Gk. káke “evi” beside kákkeé ‘excrement’; Alb. kaké, id.; Lat. cf. caco, are, v.; MIr. cacc, f.; Ir. cac, m.; W cach; Li. kaka
6624:kakāið (kakk-) “void excrement'. WP I, 336. Cf. kakā Gk. kakáo, kakkáo; Lat. caco, are; Mlr. cac- caim; Ir. cacaim; Cor. caca; Li. kakóju, óti, id. (an onomat. term, non-historical in Cz. kakat, G kacken, etc.). Br. kach, s., kacha, v. indicates a prototype *kakk-
6625:kākāið ‘cackle, guffaw, mock? Gk. këkázo ‘revile’; OHG huohon, MHG huo- hen, id. beside huoh, m. id. (Onomat. and am- big. in Gz. kákat ‘cackle’. Cf. quaquaió)
6636:Arm. kakyi (clime-tree" from the fruit); Gk. kakalía (a seed or plant, prob. not ‘coltsfoot’, cf. Lat. LW cacalia ‘wild caraway’); Br. kagal ‘droppings’; W cagl. id.; Cor. cagal, id. & ‘clot, lump’; OHG hagal (and com. Gmc. "hal": cf. also G Hágel (^millet', and perh. Gk. kákh- lex ‘pebble’ if fr. *kaghl-)
6637:kakoros “bird, cockerel" or sim. (Ambig. cf. kokoros). Onomat. Skt. cf. kakarah (a bird); MHG cf. hageln (‘rail at; haggle’. Onomat.); cf. also hagel-gans («heathcock? or sim.); Cz. cf. kokořík (“Solo- mon's seal’, bot.); Blg. kokórja se, v. ‘strut’; Li. cf. kakarlis ‘chatterbox’; kakarine ‘larynx’
6638:kakot-, kakut- (kakud-) “tip, point, peak, pile” Skt. cf. kaküd ‘peak, tip’; Arm. košt, Let. ‘mound, hump’ (SEM: AIS 117); Br. kakad ‘rick, stook’; OCz. kokot ‘cockerel; penis’
6640:kakos, ios ‘foul, filthy’. WP I, 336 and cf. kākstios, kakā Skt. cf. kacakuh ‘wicked, intolerable’ beside kaccarah ‘foul, bad?; Gk. kakós; Alb. i keq, f. e keqe ‘bad’; Lat. cacus ((camp-boy', Dei: Ligurian (in Rumansch) cac, f: caca ‘ugly’; Big. (?) koc ("latrine' fr. kakios?)
6643:kakulos /(dung-like, soft. Cf. kakā (iso- phone: kakolos) Arm. kakuy, gs kakyo "soft Lat. cacula 'camp- boy’; ON (?) haell, m. (!) 'soldier's widow’
6644:kakupit (kaput-) “tip, top, head'. WP I, 346. (Lat. & Olr. by crasis) Skt. cf. kapucéhalam *topknot; lip of ladle’; Hitt. cf. kakapas (queried: *club^); Lat. caput, gs capitis; MIr. (alleged) caut (fhead'. K. Meyer); Go. haubip; OHG houbit; OE hea-
6879:kauKos, à, io “shell, skull, bowl, cup’. Cf. kaukolos, etc. WP II, 548-551 Skt. kosah “shell, cup, pail, box, cask’; kośam, id.; cf. koSika, kausika ‘goblet; case? (dim.); Per. cf. kofče (Cladie'. LW in R kovš, id.); Oss. küsi, id.; Gk. (gloss) kaükos ‘cup’; Kaka ‘skull’; kaukíon, dim. ‘cup’; Maced. kausia ‘felt hat worn by kings’; Lat. caucum (LW? as Gk. kaükos); MIr. coach Ir. cuach “bowl, cup’; W cawg ‘dish’; ON hauss ‘skull’; Du. (?) hauw ‘siliqua, poď’; Li. kiáušas ‘skull, cup made from a skull, shell; dial. kaušas ‘ladle, Skull; kiáušē, f. *skull; kiaušis, io, m. ‘egg’;
7147:kolok-, kolk- (klk- w. u-basis) (1) “ankle, heel, hock, knee'. (Variants: klk-, kolquos, kuluk-, kalks-, kalk-). WP II, 599 Lat. calx, gs calcis, m.f. (2) “heel, tip’; OE healh, pl. hal(h)as “corner, nook, dingle'; OCS klüka ‘bend of knee’; Blg. Kaka ‘hip’; Cz. klk “fold of intestine’; Li. cf. kulkšis, kul- šis, f. ‘haunch, hip, ankle, heel"; cf. pa-kulšē ‘thigh’; Latv. cf. cilksnis “hand of pork’ (Iso- phones: OCS klükü ‘woof; OCz. kluk ‘bolt of crossbow’; Cz. ‘boy’; Blg. kláka (2) ‘club’; Cz. kik (2) ‘clot, lump’. Note the Czech variants klk and kluk, the latter w. ambiguous vocalism). See next
7213:kiriquaquos, à ʻa cackling bird'. Cf. Kris, krk-, etc. etc. (quiri-). Skt. Cirikakah 'crow'; Alb. cirikoké (jackdaw; warbler', fr. an assimilated *quiriquaqua); Cz. cf. Cirikavka ‘partridge’ beside crkat ‘to chirp’ and Per. Ciryad ('cricket' insect), Li. kirkauti, inf. ‘to shriek’?
=== gogos
3848:gagodio (gogodio) ‘chatter’. Cf. gagotio, gagorió Arm. kakazem ‘stammer, jabber, lisp’; MHG kachezen ‘guffaw’; OE ceahhetan, id.: E chat. Cf. also OE ceahhe ‘daw, chough’
3849:gagol- ‘cackle’ Lat. gallus (“cockerel', fr. *gaglo-); Du. kakelen
3865:gagorio, see next and cf. gagodio, gago. E dial. to chacker ‘chatter’; Li. gagarà “arctic diver-bird'. (W gair “word? seems to represent a form *geger-)
3866:gagətið (gogotio) cf. gagodio, gagó, gagol- Arm. kakacem ‘cackle’; Cor. gesya “mock, jeer’; (MHG cf. kachezen, OE ceahhetan, E chat, fr. *gagodio); OCz. hohcu, hohtati ‘cackle’; R gogotàt, id.; gógot, m. id.
3867:gagð, ið ‘cackle, chatter. WP I, 526. Cf. gagodio, etc. Br. cf. gagéi (stammer, jabber’, a secondary formation with -g- internally); MHG kachen;
4216:gogolos, ios (gog9l-) ‘knob, tapering object Per. gazar ‘carrot; Arm. kakyi (“lime-tree”, fr. the fruit); OS kakeli ‘icicle’?
```


## [2026-09-06T15:50:14.888Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"^k[āa]kh?[āaā]?[^a-z]*.{0,40}branch\" IEC.txt | head; echo ===; grep -n \"śākhā\\|sakha ‘branch\\|cakha\" IEC.txt | head; echo \"=== kankos\"; grep -n -iE \"^kank|^kakos.*branch|kanku\" IEC.txt | head"
}
```


### [2026-09-06T15:50:17.180Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T15:50:20.680Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Skt. sakha\\|sakhā\\|śakha\\|sākhā\" IEC.txt | head; echo \"--- kaka branch\"; grep -n \"‘branch\" IEC.txt | grep -i \"kak\\|kank\\|kok\" | head"
}
```


### [2026-09-06T15:50:20.744Z] TOOL RESULT

```
--- kaka branch
8538:Kakis, io (Kakus, os, à, Kakina) ‘spike, prong’. Cf. Kakolos and Kaks- WP I, 333 Skt. cf. $akuláh ‘spur on cow's hoof; Per. (dim. form) (?) sagak ‘buckle’; Alb. thek, pl. thaké (fringe'; pl. ʻawns’) beside thekén, f. ‘rye’; Li. Sakà ‘branch’; Sake ‘fork’
8557:Kankos, is, us ‘spike, limb, branch, peg’. WP I, 335. Cf. Kiaks-, Kaks- Skt. Sanküh “peg, nail, spike, spear’; Oss. cong “arm, branch’; OW ceing, W caing, pl. cein- giau, and cang, pl. -au, f. ‘branch’; OCS sokü ‘shoot, twig’; Pol. sek, Cz. suk ‘knot in wood’; R suk ‘branch, knot in wood’
8821:kos. (Variants: Kiakos, à, is) Skt. $akha “branch, limb’; Per. Sax “branch, Shoot, horn’; (Oss. xix, Dig. xexä “branch? beside ságoi *dungfork' suggest a doublet of type *qusak-, q.v. for xix, xexá); Arm. çax *heather; shrub; branch' beside caKan (Awge- rian); cak (Kerestedjian) ‘harrow’; OCS soxa ‘stem, stake’; R soxà ‘primitive plow’; Srb. soha ‘prop, stay, forked stick’. The Gothic form hōha ‘plow’; LW in Finn. kuokka ‘hoe’ is of uncertain phonology. Li. šakà ‘branch’; sake ‘fork: šaknis "root represent a variant of type *kak-
```


## [2026-09-06T15:50:27.787Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8818,8822p' IEC.txt"
}
```


### [2026-09-06T15:50:27.834Z] TOOL RESULT

```
id.; Oss. saw, 1d.; Arm. seav, gs sevo; mod. sev, id.; LW in Georg, Sawi, id.; Alb. cf. thij, v. tr. “turn grey”; Ir. cf. ceo, m. “mist, darkness"; ciobh-ach ‘dark’; ciob-ar ‘dirt; OE hæwe ‘grey, blue’; OCS sivü ‘grey’; Li. Sývas, id.; Latv. cf. SIvs, sive, m. f. ‘effluent’
Kia, Kio, fem. form. of Kis, q.v. WP I, 453 Arm. sa ‘this, that’; Myc. cf. tsa- in tsa-wete(s-) ‘this year’s’; Alb. so- in so-t (Ctoday', for *so ditë) and so-nte (tonight, for *sonate < *Kja- noktei); OS hiu- in hiu-du, -digu ‘today’; Fris. hja ‘she’; OE heo, id.; OCS si, id.; Slovene sija, id.; Li. šo- in So-nakt ‘tonight’; Latv. šā-, šī- in Sa-ritéjs, S1-ritejs ‘this morning’. Extns. in ON hé-óan “hence; Slovene sád “now? and Latv. šādi ‘thus’
Kiäks- “branch, twig, spike’. Cf. Kāksā, Kan-
kos. (Variants: Kiakos, à, is) Skt. $akha “branch, limb’; Per. Sax “branch, Shoot, horn’; (Oss. xix, Dig. xexä “branch? beside ságoi *dungfork' suggest a doublet of type *qusak-, q.v. for xix, xexá); Arm. çax *heather; shrub; branch' beside caKan (Awge- rian); cak (Kerestedjian) ‘harrow’; OCS soxa ‘stem, stake’; R soxà ‘primitive plow’; Srb. soha ‘prop, stay, forked stick’. The Gothic form hōha ‘plow’; LW in Finn. kuokka ‘hoe’ is of uncertain phonology. Li. šakà ‘branch’; sake ‘fork: šaknis "root represent a variant of type *kak-
Kiā-noktei, -nokt ‘tonight, last night. Cf. Kia, nokts Alb. sonte ‘tonight’; Venetic (queried) sahna- teh ‘today’; OHG, MHG hinaht “tonight, last night’; G heint, id.; OCS si nošči, Srb. sinoć, OCz s nóci, Ukr. s-nocy; Li. šonakt, id. Cf. WP I, 453
```


## [2026-09-06T15:51:10.140Z] TOOL CALL #100: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T15:51:10.184Z] TOOL RESULT

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


## [2026-09-06T15:51:12.902Z] TOOL CALL #101: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T15:51:12.951Z] TOOL RESULT

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


## [2026-09-06T15:51:26.509Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -oE \"^kak-[0-9]?\\.[^.]{0,80}\" AHD_watkins1985.txt | head; echo ---; grep -n -c \"\" /dev/null; grep -n \"Pok. 2. kak-\\|In Pok. .*523\\|kak- 523\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:51:28.227Z] TOOL RESULT

```
---
0
```


## [2026-09-06T15:51:31.048Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '570,576p' AHD_watkins1985.txt | cut -c1-600"
}
```


### [2026-09-06T15:51:31.095Z] TOOL RESULT

```
kailo-. Whole, uninjured, of good omen. 1. Germanic *hailaz in: a. Old English Adal, hale, whole: HALE!, WHOLE; b. Old English *halsum, wholesome (> Middle English holsom): WHOLESOME; c. Old Norse heill, healthy: (HAIL?); WASSAIL. 2. Germanic *hailithé in Old English h#ith, health: HEALTH. 3. Germanic *hailjan in Old English h&lan, to heal: HEAL. 4. Germanic *hailagaz in: a. Old English hdlig, holy, sacred: HOLY; b. Germanic derivative verb *hailagén in Old English hdlgian, to consecrate, bless: HALLOW. [Pok. kailo- 622.]
kaito-. Forest, uncultivated land. 1. Germanic *haithiz in Old English A&th, heath, untilled land: HEATH. 2. Ger- manic *haithinaz in: a.Old English h@then, heathen, “savage” (< “one inhabiting uncultivated land”): HEA- THEN; b. Middle Dutch heiden, heathen: HOYDEN. [Pok. kaito- 521.]
kak-'. To enable, help. Sanskrit saknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]
[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE. 2. Middle Dutch koeke, a cake: cooky. 3. Middle Low German koéke, cake: COCKAIGNE. 4. Old High German kuocho, cake: KUCHEN, QUICHE. [In Pok. gag- 349.]]
kakka-. Also kaka-. To defecate. Imitative root. 1. Old Norse *kiika, to defecate, akin to the source of Middle English cukken, to defecate: CUCKING STOOL. 2. Latin cacGre, to defecate: POPPYCOCK. 3. Greek kakos, bad: CACO-; CACODYL, CACOETHES, CACOPHONOUS, CACOPH- ony. [Pok. kakka- 521.]
kal-'. Cup. 1. Suffixed zero-grade form *l-ik- in: a. Latin calix, cup, goblet: CALIX, CHALICE; b. Greek kulix, cup: KYLIX. 2. Suffixed zero-grade form *kl-uk- in Greek kalux, seed-vessel, cup: CALYX. [Pok. 7. kel- 550.]
kal-2, Beautiful. 1. Suffixed form *kal-wo- in Greek kalos, beautiful: CALLISTO; CALOMEL, CALOYER, KALEIDO- SCOPE. 2. Suffixed form *kal-yo- in Greek kallos, beauty: CALLIGRAPHY, CALLIOPE, CALLIPYGIAN. [Pok. 2. kal- 524.]
```


## [2026-09-06T15:59:47.399Z] TOOL CALL #104: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk235.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SAX   = \"https://en.wiktionary.org/wiki/شاخ\"\nW_KAK   = \"https://en.wiktionary.org/wiki/کاک\"\nW_KAAK  = \"https://en.wiktionary.org/wiki/كعك\"\nW_KAST  = \"https://en.wiktionary.org/wiki/کاستن\"\nW_AK    = \"https://en.wiktionary.org/wiki/ـک\"\nETY_CAKE= \"https://www.etymonline.com/word/cake\"\nAB_SEKL = \"https://abadis.ir/fatofa/شکله/\"\n\ndoc = {\n \"pdf_page\": 235,\n \"book_page\": 205,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ---------------- entry 0 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Kâk 2, Kank, Kâkha\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱāk-2, nasalised *ḱank- 'branch, twig, peg' (Pokorny 523 = Walde-Pokorny I 335); Wiktionary reconstructs the ā-stem as *ḱókh₂eh₂ 'branch'\",\n \"note\": (\"Pokorny I 523 has the lemma verbatim: 'Root/lemma: ḱāk-2, nasalized ḱank-; Meaning: branch', with the material \"\n          \"Skt. śākhā 'bough' (: Goth. hōha, Arm. cʿax), śakala- 'chip, splinter', śaṅku- 'peg', Welsh cainc, Lith. šakà, \"\n          \"OCS *sǫkъ, Slav. socha. Language label ('Indo-European'), page (523) and gloss ('twig, branch') are therefore all \"\n          \"correct. The third root-name 'Kâkha' is not a separate Pokorny lemma: it is Nourai's citation form of Skt. śākhā \"\n          \"(the aspirated ā-stem), which is why entry 3 of this page redirects 'Kâkha' back here. 'Kank' = Pokorny's nasalised \"\n          \"ḱank-, which is also the etymology Gharib gives for the Sogdian word in node #5.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ḱāk- (و گونهٔ خیشومی‌شدهٔ *ḱank-) به معنی «شاخه، ترکه» در پوکورنی، ص ۵۲۳، دقیقاً با همین \"\n             \"برچسب و همین معنا آمده است و مواد آن سنسکریت śākhā، ارمنی کهن cʿax، لیتوانیایی šakà، گوتیک hōha و اسلاوی کهن soxa است. \"\n             \"«Kâkha» ریشهٔ جداگانه‌ای نیست، بلکه صورت استنادی نورایی برای همان śākhā سنسکریت است؛ به همین سبب در همین صفحه «Kâkha» \"\n             \"به «Kâk 2» ارجاع داده شده. ویکی‌واژه همین ریشه را به صورت *ḱókh₂eh₂ بازسازی می‌کند. ادعای نورایی دربارهٔ ریشه درست است.\"),\n \"sources\": [W_SAX],\n \"ref_check\": [\n   {\"ref\": \"POK:523\", \"status\": \"supports\",\n    \"note\": (\"POK_full.txt (line ~49508) 'Root / lemma: ḱak-2, nasalized ḱank- | Meaning: branch | Material: Old Indic śākhā \"\n             \"\\\"bough\\\" (: Gothic hoha, Armenian cʿax); śakala- \\\"chip, splinter, wooden log, shred\\\" (: Lithuanian šakalỹs) ... \"\n             \"Page(s): 523'; the same text stands on leaf 181 of POK_02.txt (printed p. 523).\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 335 (WLD_Bd1_1930_dli_70244_djvu.txt line 21134)\", \"stance\": \"supports\",\n    \"note\": \"'ḱak- (oder ḱok-?), nasaliert ḱank- (oder ḱonk-?) : ḱn̥k- „Ast, Zweig, Pflock“. Ai. śākhā „Ast“ (: got. hōha, arm. cʿax); śakala- m. n. „Span, Splitter, Holzscheit, Schnitzel, Stückchen“ (: lit. šakalỹs)' — Pokorny's own earlier version of the same root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Ḱiāks- (IEC.txt line 8821)\", \"stance\": \"supports\",\n    \"note\": \"'Ḱiāks- \\\"branch, twig, spike\\\". Cf. Ḱāksā, Ḱankos. Skt. śākhā \\\"branch, limb\\\"; Per. šāx \\\"branch, shoot, horn\\\"; Arm. cʿax ...; OCS soxa; Li. šakà' — Mann keeps the same family and adds the nasal variant Ḱankos (line 8557, 'WP I, 335').\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"silent\",\n    \"note\": \"grep of AHD_watkins1985.txt finds no root of this shape ('branch'); the appendix lists only roots with English derivatives, and this one has none.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.55 BRANCH, pp. 523-525\", \"stance\": \"supports\",\n    \"note\": \"'Ir. gésca, géc, NIr. géag, W. cangen, cainc, Lith. šaka, Russ. suk (ChSl. sǫkŭ \\\"twig\\\"), Skt. śākhā-, Arm. caṙ : Skt. śaṅku- \\\"peg\\\", Lith. šaknis ... Goth. hōha, Ir. cécht \\\"plow\\\" (\\\"forked stick\\\"). Walde-P. 1.335.'\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"šâxa, čâxa\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Sanskrit शाखा śākhā f. 'branch, bough, limb, finger' (RV onwards) is the headword of Pokorny's entry and of \"\n   \"Walde-Pokorny I 335. It continues PIE *ḱākā / *ḱókh₂-eh₂: palatal *ḱ > Skt. ś-, the aspirate *kʰ shows up as -kh-, and the \"\n   \"same stem gives Armenian cʿax 'twig', Lithuanian šakà 'branch' and (in the o-grade/other suffix) Gothic hōha 'plough' and \"\n   \"OCS soxa. Nourai's two transliterations are one word, not two: 'čâxa' is the nineteenth-century transliteration çākhā \"\n   \"(ç = ś, still used by Moʿin in the Borhān footnotes) and 'šâxa' the modern one; the correct citation form has a long final \"\n   \"-ā and an aspirated -kh-, which Nourai's spelling flattens to -x-.\"),\n \"derivation_fa\": (\"سنسکریت शाखा śākhā (مؤنث) به معنی «شاخه، شاخ، اندام» از ریگ‌ودا به بعد شاهد دارد و همان واژه‌ای است که \"\n   \"پوکورنی (ص ۵۲۳) و والده-پوکورنی (ج ۱، ص ۳۳۵) در صدر این ریشه آورده‌اند. کام هندواروپایی *ḱ در سنسکریت به ś بدل شده و *kʰ به \"\n   \"kh؛ هم‌ریشه‌های آن ارمنی کهن cʿax، لیتوانیایی šakà و گوتیک hōha «خیش» است. دو صورت «šâxa» و «čâxa» در کتاب یک واژه‌اند: \"\n   \"«čâxa» همان آوانگاری کهن çākhā است که معین نیز در حواشی برهان قاطع به کار برده. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:523\", \"status\": \"supports\",\n    \"note\": \"Pokorny p. 523 opens the Material with 'Old Indic śākhā \\\"bough\\\" (: Gothic hōha, Armenian cʿax)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 335\", \"stance\": \"supports\",\n    \"note\": \"'Ai. śākhā „Ast“ (: got. hōha, arm. cʿax)' — with the reference to Bartholomae BB. 10, 290 for the Armenian equation.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.55, p. 525\", \"stance\": \"supports\",\n    \"note\": \"Buck's Sanskrit column for BRANCH is 'śākhā-, vayā-' and his discussion (§4) groups 'Skt. śākhā-, Arm. caṙ, Lith. šaka, Russ. suk' with 'Walde-P. 1.335'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Ḱiāks-\", \"stance\": \"supports\",\n    \"note\": \"'Skt. śākhā \\\"branch, limb\\\"' heads Mann's material for the root.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"šâx «شاخ»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"New Persian شاخ šāx 'horn; branch' goes back to Middle Persian šāk — Moʿin's etymological footnote 7 on the very \"\n   \"page Nourai cites (BQT p. 1219) reads 'هندی باستان çâkhâ (شاخه)، پهلوی shâk، ارمنی çax، کردی shâx، افغانی shâx، بلوچی shâh \"\n   \"(قرن، شاخ جانور) و shâx (شاخهٔ درخت)، وخی sholx، سریکلی shox، یزغلامی shâo' — i.e. a list of COGNATES, not a statement that \"\n   \"Persian borrowed from Sanskrit. Wiktionary derives شاخ straight from Proto-Indo-Iranian *ćā́kʰaH < PIE *ḱókh₂eh₂, and Mann \"\n   \"(IEC s.v. Ḱiāks-) lists 'Per. šāx \\\"branch, shoot, horn\\\"' as a primary member of the root beside Skt. śākhā. Phonetically the \"\n   \"Iranian line is regular: PIr. *ćāxā- > OIr. *sāxa- > MP šāk (written šʾk) > NP šāx, the -x- being the inherited reflex of the \"\n   \"aspirate, and the sense 'horn' an Iranian specialisation ('branch of an antler'; Baluchi keeps the two senses apart as šāh \"\n   \"'horn of an animal' vs šāx 'branch of a tree'). Nourai's arrow Skt > Persian is nevertheless exactly what Pokorny 523 floats: \"\n   \"'Armenian cʿax \\\"twig, branch\\\", perhaps loanword from Pers. šāx, and these from Old Indic śākhā' — so the chart follows its \"\n   \"cited source, but the loan hypothesis is not the modern view: the two words are siblings, not parent and child. The extra \"\n   \"Persian form شاخه šāxe is the ordinary NP -a(g) derivative 'twig, branch'.\"),\n \"derivation_fa\": (\"«شاخ» فارسی نو از فارسی میانهٔ šāk، از ایرانی باستان *ćāxā-، از هندوایرانی آغازین *ćā́kʰaH و در نهایت از \"\n   \"هندواروپایی *ḱókh₂eh₂ است؛ یعنی «شاخ» با śākhā سنسکریت هم‌ریشه (cognate) است، نه وام‌گرفته از آن. حاشیهٔ ۷ معین در برهان قاطع \"\n   \"ص ۱۲۱۹ نیز فهرستی از هم‌ریشه‌ها می‌دهد (هندی باستان çâkhâ، پهلوی shâk، ارمنی çax، کردی و افغانی shâx، بلوچی shâh «شاخ جانور») \"\n   \"و سخنی از وام‌گیری از سنسکریت ندارد. معنی «شاخِ جانور» تحول معنایی ویژهٔ ایرانی است (شاخهٔ شاخِ گوزن). با این حال خودِ پوکورنی \"\n   \"(ص ۵۲۳) احتمال داده که ارمنی cʿax از فارسی šāx و این‌ها از śākhā هندی باستان باشند، و منبعِ پیکانِ نورایی همین جمله است. \"\n   \"پس: با احتیاط پذیرفتنی است، ولی پژوهش امروزی «شاخ» را واژه‌ای موروثی می‌داند نه وام‌واژه.\"),\n \"sources\": [W_SAX],\n \"ref_check\": [\n   {\"ref\": \"POK:523\", \"status\": \"partial\",\n    \"note\": \"Pokorny p.523: 'Armenian cʿax \\\"twig, branch\\\", perhaps loanword from pers. šāx ds., and these from Old Indic śākhā; after Meillet ... rather from Indo-Germanic *ḱsakh-.' — the loan idea is offered with 'perhaps' and immediately countered by Meillet's alternative.\"},\n   {\"ref\": \"BQT:1219\", \"status\": \"partial\",\n    \"note\": \"Read from the page image (data/verification/sources/refs/ocr/BQT/1219.png, transcript in 1219.vision.txt): footnote 7 s.v. شاخ gives 'هندی باستان çâkhâ (شاخه)، پهلوی shâk' plus Armenian/Kurdish/Afghan/Baluchi/Wakhi/Sarikoli/Yazghulami forms — a cognate list with a Pahlavi ancestor, not a Sanskrit etymon.\"},\n   {\"ref\": \"SYN:525\", \"status\": \"partial\",\n    \"note\": \"Buck 8.55 BRANCH runs pp. 523-525; p. 525 carries the end of the discussion (Skt. vayā-, Av. vaxš-/frasparəγa-). Buck has no New Persian column at all, so the page supports the IE family of śākhā but says nothing about Persian šāx.\"}\n ],\n \"consulted\": [\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Ḱiāks- (IEC.txt line 8821)\", \"stance\": \"contradicts\",\n    \"note\": \"'Skt. śākhā \\\"branch, limb\\\"; Per. šāx \\\"branch, shoot, horn\\\"' — Mann lists Persian as a direct continuant of the root, i.e. a cognate of the Sanskrit word, not a loan from it.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 371 (ARY_pages.txt, [pdf page 370])\", \"stance\": \"supports\",\n    \"note\": \"Entry شاخ with the note 'در فارسی شاخ دارای دو چم است: سرودن با شاخ جانور و شاخه‌ی گیاه' followed by an Avestan / Old Persian / Pahlavi (šāk) / Sogdian / Sanskrit / Armenian cognate列; the Latin transliterations are badly OCR'd but the language sequence is legible, and the entry cites برهان قاطع.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, searched s.v. 'branch'\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie's English index gives 'branch azg, tag' and the entries azg [ʾzg] and tāg; no šāk is listed in the Concise Pahlavi Dictionary, so the MP form rests on Moʿin/Aryanpur rather than on MacKenzie.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"šakala\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Sanskrit शकल śakala- m./n. 'chip, splinter, piece, log, shred, half' is placed under this very root by Pokorny \"\n   \"523 — 'śakala- m. n. \\\"chip, splinter, splinter, wooden log, schnitzel, shred\\\" (: Lithuanian šakalỹs)' — and by \"\n   \"Walde-Pokorny I 335 in the same words. The formal match is Lith. šakalỹs 'splinter' beside šakà 'branch'; the short-vowel \"\n   \"*ḱak- stands beside the lengthened *ḱāk- of śākhā, and the semantic step is 'branch, forked stick' > 'piece broken off, \"\n   \"splinter'. So the arrow root > śakala is exactly what the cited page says.\"),\n \"derivation_fa\": (\"سنسکریت शकल śakala «تکه، پاره، تراشه، کندهٔ چوب» را پوکورنی در همان صفحهٔ ۵۲۳ ذیل همین ریشه آورده است \"\n   \"(«śakala- در برابر لیتوانیایی šakalỹs») و والده-پوکورنی (ج ۱، ص ۳۳۵) نیز همین را می‌گوید. گونهٔ کوتاه‌واکهٔ *ḱak- در برابر \"\n   \"گونهٔ کشیدهٔ *ḱāk- در śākhā است و تحول معنایی از «شاخه، چوب دوشاخ» به «تکهٔ جداشده، تراشه» است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:523\", \"status\": \"supports\",\n    \"note\": \"'śakala- m. n. \\\"chip, splinter, splinter, wooden log, schnitzel, shred\\\" (: Lithuanian šakalỹs)' — second item of the Material on p. 523.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 335\", \"stance\": \"supports\",\n    \"note\": \"'śakala- m. n. „Span, Splitter, Holzscheit, Schnitzel, Stückchen“ (: lit. šakalỹs)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Ḱakis/Ḱakus (IEC.txt line 8538) and Ḱiāks-\", \"stance\": \"partial\",\n    \"note\": \"Mann keeps the 'splinter/spike' words (Li. šakà, šakė) in the family but files Skt. śakuláḥ rather than śakala- there; śakala- itself is not separately headed.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.55, p. 524-525\", \"stance\": \"supports\",\n    \"note\": \"'Lith. šaka ... šakalys \\\"splinter\\\" (: Skt. śakala-)' in the same paragraph as śākhā, citing Walde-P. 1.335.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"šeklah «شکله»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The word is real: Borhān-e Qāṭeʿ p. 1280 s.v. شکله (read from the page image) — 'آلچه از جامه و امثال آن که در \"\n   \"جایی بند شود و پاره گردد - و پارچه‌ای را نیز گویند که از سر هندوانه و خربزه به کارد بردارند ... و آنرا به عربی قوارةالبطیخ \"\n   \"گویند' — i.e. exactly Nourai's gloss 'slice, piece, a torn piece of garment'. Dehḵodā, Moʿin and ʿAmid give the same two \"\n   \"senses. The etymology is Moʿin's own footnote 10 on that page: 'سانسکریت śákala (تکه، قطعه) و śakalaya (به قطعات تقسیم \"\n   \"کردن) «ویلیامز ۱۰۴۶»' (Monier-Williams p. 1046) — so Nourai's arrow reproduces his source faithfully. It stays 'plausible' \"\n   \"rather than 'confirmed' because Moʿin offers no route: there is no Middle Persian *šakal, no Sogdian or Khotanese \"\n   \"intermediary, and Indic loanwords of this shape normally arrive in Persian only in the Indo-Persian period. Persian also \"\n   \"has a homograph شُکله from Arabic šuklaʰ 'redness mixed with white' (Dehḵodā, first sense), and a native formation could \"\n   \"as easily rest on شکل or on the *(s)kel- 'split' family. No independent source confirms the Sanskrit derivation.\"),\n \"derivation_fa\": (\"«شکله» واژه‌ای است ثبت‌شده: برهان قاطع (ص ۱۲۸۰) آن را «آلچه از جامه ... که در جایی بند شود و پاره گردد» و «پارچه‌ای \"\n   \"که از سر هندوانه و خربزه به کارد بردارند» معنی کرده و دهخدا، معین و عمید نیز همین دو معنی را آورده‌اند. ریشه‌شناسیِ آن از آنِ \"\n   \"خود معین است: در حاشیهٔ ۱۰ همان صفحه آن را با سانسکریت śákala «تکه، قطعه» و śakalaya «به قطعات تقسیم کردن» (مونیه-ویلیامز ۱۰۴۶) \"\n   \"سنجیده است؛ بنابراین نورایی دقیقاً منبع خود را بازتاب داده. اما راهِ وام‌گیری نشان داده نشده — نه صورتی در فارسی میانه هست نه \"\n   \"در سغدی — و در فارسی «شُکله»ای عربی (سرخی آمیخته به سپیدی) نیز هست. پس با احتیاط پذیرفتنی است.\"),\n \"sources\": [AB_SEKL],\n \"ref_check\": [\n   {\"ref\": \"BQT:1280\", \"status\": \"supports\",\n    \"note\": \"Read from data/verification/sources/refs/ocr/BQT/1280.png (transcript in 1280.vision.txt): headword شکله with Moʿin's footnote 10 'سانسکریت shákala (تکه، قطمه) و shakalaya (بقطعات تقسیم کردن) «ویلیامز ۱۰۴۶: ۱ و ۲»' — precisely Nourai's arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin via abadis.ir s.v. شکله\", \"stance\": \"partial\",\n    \"note\": \"'یک برش یا قاچ از هندوانه و مانند آن' — the sense is confirmed; Moʿin's lexicon entry carries no etymology (the Sanskrit note lives only in his Borhān footnote).\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss — searched\", \"stance\": \"silent\",\n    \"note\": \"no entry for šakla/šekle in Horn's Neupersische Etymologie; the word is not part of the classical NP etymological canon.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien — searched\", \"stance\": \"silent\",\n    \"note\": \"no entry; Hübschmann treats no Indic loan of this shape.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"šnk\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"šnk\",\n \"correct_form\": \"šnx\",\n \"derivation\": (\"The cited page is right and the word is right, but the last letter is wrong. Gharib's Sogdian dictionary, entry \"\n   \"9311 on printed p. 376 (leaf 444 of SOD_pages.txt — the page Nourai cites as SOD:376) reads: '9311 šnx  M | šanx (šnγ) \"\n   \"©<IE ḱank ©pl. -t ⇒ pršnx(y) | branch | Frag. Len. p109; šnxyt, GMS n 2, 1142'. The Sogdian form is šnx /šanx/, the \"\n   \"nasalised *ḱank- grade of the root (compare the compound pr-šnx(y), entry 7215, also glossed 'branch'), with -nx- from \"\n   \"*-nk- by the regular Sogdian spirantisation of postvocalic/postnasal *k. Gharib's own etymology, '<IE ḱank', is word for \"\n   \"word Nourai's second root name 'Kank', so the derivation drawn in the chart is confirmed by the cited entry. Only the \"\n   \"transcription is defective: page 235 of the printed dictionary shows 'šnk' (checked on the page image, copied to \"\n   \"data/verification/sources/refs/ocr/BOOK/235.png), so this is the author's misprint, not an extraction error — the JSON \"\n   \"faithfully reproduces what the book prints.\"),\n \"derivation_fa\": (\"در فرهنگ سغدیِ بدرالزمان قریب، مدخل ۹۳۱۱ در ص ۳۷۶ — همان صفحه‌ای که نورایی ارجاع داده — چنین است: \"\n   \"«šnx (šanx) ©<IE ḱank ©جمع -t ⇒ pršnx(y): شاخه». پس صورت درست سغدی šnx است نه šnk؛ خوشهٔ *-nk- ایرانی باستان در سغدی به \"\n   \"-nx- بدل شده (قس ترکیب pr-šnx(y) «شاخه» در مدخل ۷۲۱۵). نکتهٔ مهم آنکه ریشه‌شناسیِ خودِ قریب، «<IE ḱank»، عیناً همان نام دومِ \"\n   \"ریشه در نمودار نورایی («Kank») است؛ یعنی خودِ اشتقاق تأیید می‌شود. تصویر صفحهٔ ۲۳۵ کتاب چاپی نشان می‌دهد که در کتاب «šnk» \"\n   \"چاپ شده است: پس خطای چاپیِ کتاب است، نه خطای خوانشِ اسکن.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:376\", \"status\": \"partial\",\n    \"note\": \"SOD_pages.txt leaf 444 (printed page number 376 visible at the head of the leaf), entry '9311 šnx M ... sanx (šnγ) ©<IE ḱank ©pl. -t ⇒prsnx(y) | branch'. The page and the meaning are right; the form is šnx, not the šnk of the chart. Gharib's English index confirms: 'branch 7215, 9148, 9311, 9377'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 523, s.v. ḱāk-2, nasalized ḱank-\", \"stance\": \"supports\",\n    \"note\": \"the nasalised grade Gharib invokes for the Sogdian word is exactly Pokorny's 'nasalized ḱank-' on the page Nourai cites for the root.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, entry 7215 pršnx(y), p. ~292\", \"stance\": \"supports\",\n    \"note\": \"the compound 'pršnx(y) M' is also glossed 'branch' in the English index, confirming the stem-final -nx of entry 9311.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Ḱankos (IEC.txt line 8557)\", \"stance\": \"supports\",\n    \"note\": \"'Ḱankos, is, us \\\"spike, limb, branch, peg\\\". WP I, 335 ... Oss. cong \\\"arm, branch\\\"' — the nasal variant is an accepted Iranian-bearing form of the root.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------- entry 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Kak 3\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Proto-Iranian *kas- / *kah- 'to be small, diminish' (Cheung, EDIV 247); Pokorny 521 kak- 'abmagern' is doubtful as an IE root\",\n \"note\": (\"Pokorny I 521 does carry the lemma Nourai cites — leaf 180 of POK_02.txt prints 'kak- „abmagern“. Av. kasu- „klein, \"\n   \"gering“, Komp. Superl. kasyah-, kasišta-; nhd. hager ...; lit. nukašėti „ganz entkräftet werden“. WP. I 334' — so the root, \"\n   \"the page, the language label and the gloss ('to become thin') are Nourai's source verbatim. Modern Iranian scholarship, \"\n   \"however, does not accept it as Indo-European: Cheung, Etymological Dictionary of the Iranian Verb, p. 247 s.v. *kas¹ 'to be \"\n   \"small, diminish, lessen', writes 'This apparently Ir. root has no certain IE provenance. It may even be an exclusively Ir. \"\n   \"root', dismisses Pokorny's two non-Iranian comparanda (NHG hager 'is obscure though'; Lith. kašėti 'popular flavour'), and \"\n   \"records 'LIV: – | Pok.: 521 f.' — i.e. LIV has no entry for it. Verdict: the root box faithfully reports Pokorny, but the \"\n   \"'Indo-European' label is what today's handbooks withhold.\"),\n \"note_fa\": (\"پوکورنی در ص ۵۲۱ ریشهٔ kak- «لاغر شدن» را با همین مواد آورده است: اوستایی kasu- «خرد، اندک»، برترین‌ها kasyah- و \"\n   \"kasišta-، آلمانی hager و لیتوانیایی nukašėti؛ پس نام ریشه، صفحه و معنایی که نورایی داده دقیقاً از منبع اوست. اما \"\n   \"ریشه‌شناسی امروزیِ ایرانی این را ریشه‌ای هندواروپایی نمی‌داند: چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ص ۲۴۷، ذیل *kas¹ «خرد \"\n   \"بودن، کاستن») می‌نویسد که این ریشه «خاستگاه هندواروپاییِ مطمئنی ندارد و شاید یکسره ایرانی باشد» و هم‌سنجه‌های غیرایرانیِ \"\n   \"پوکورنی را رد می‌کند؛ در LIV نیز مدخلی ندارد. پس: با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_KAST],\n \"ref_check\": [\n   {\"ref\": \"POK:521\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt leaf 180 (printed pp. 521-522): 'kak- „abmagern“. Av. kasu- „klein, gering“, Komp. Superl. kasyah-, kasišta-; nhd. hager ...; lit. nukašėti „ganz entkräftet werden“. WP. I 334.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 247 s.v. *kas¹\", \"stance\": \"contradicts\",\n    \"note\": \"'*kas¹ \\\"to be small, diminish, lessen\\\" ... This apparently Ir. root has no certain IE provenance. It may even be an exclusively Ir. root ... LIV: – | Pok.: 521 f.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 334 (referenced by Pokorny)\", \"stance\": \"supports\",\n    \"note\": \"Pokorny's own back-reference 'WP. I 334' for kak- 'abmagern'; the 1927 version already had the same thin Avestan+Germanic+Lithuanian material.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 root list\", \"stance\": \"silent\",\n    \"note\": \"grep finds 'kak-1. To enable, help ... [Pok. kak- 522]' and '[kak-2. A round object ...]' but no root 'to become thin' — the 1521-ff. appendix has no English derivative of this root.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"kasu; kâs; kas-yah; kas-išta\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Three of the four forms are solid Younger Avestan, all in Bartholomae's Altiranisches Wörterbuch cols. 459-461: \"\n   \"'kasav- Adj. \\\"klein, gering\\\"' (kasu-, Yt 8.29, V 7.59 etc.), 'kasyah- Adj. (auch fem.) \\\"der kleinere, geringere\\\"' — \"\n   \"comparative, glossed by Bartholomae himself 'mp. kēh, np. kih' — and 'kasišta- Adj. a) \\\"der kleinste\\\", b) \\\"der \"\n   \"geringfügigste\\\"' (V 6.10-14), with the compounds kasu.xraθwan-, kasu.dānav-, kasu.pāsna-, kasu.draonah-. Cheung (EDIV 247) \"\n   \"cites the same set as YAv. kasu- (Yt 8.29) and kasiiah- (V 5.24). Two things do not hold. (a) There is no Avestan or Old \"\n   \"Persian verb kās- 'to reduce': Bartholomae's Avestan kas- is 'nur mit ā: gewahr werden, erblicken' (col. 459), a different \"\n   \"root (Skt. kāś- 'appear, shine'); the lengthened causative stem kāh-/kās- 'diminish' is first attested in Middle Persian. \"\n   \"(b) The label 'Old Persian' is unsupported: Kent's OP lexicon (p. 179) has only kasaka- 'semi-precious stone', which he \"\n   \"derives from 'Iran. root *kas-' = Skt. kaś- 'be visible, shine' — the seeing root, not the small root. Nyberg (Manual of \"\n   \"Pahlavi II, s.v. ¹kas) is explicit that kasu- is the NORTH-WEST form and that the South-West (i.e. Persian) form was \"\n   \"*kaθu-, surviving only in the comparative *kadyah- > MP kēh.\"),\n \"derivation_fa\": (\"سه صورت از چهار صورتِ این گره اوستایی متأخرند و در فرهنگ ایرانی باستانِ بارتولومه (ستون‌های ۴۵۹–۴۶۱) آمده‌اند: \"\n   \"kasav- (=kasu-) «خرد، اندک»، kasyah- «خردتر» (که بارتولومه خود آن را برابر «فارسی میانه kēh و فارسی نو کِه» می‌داند) و \"\n   \"kasišta- «خردترین». اما دو نکته درست نیست: نخست، فعلی به صورت kās- «کاستن» در اوستایی یا پارسی باستان گواهی نشده — kas- \"\n   \"اوستایی (تنها با پیشوند ā) به معنی «دیدن، آگاه شدن» است و ستاکِ kāh-/kās- «کاستن» نخست در فارسی میانه پیدا می‌شود. دوم، \"\n   \"برچسب «پارسی باستان» پشتوانه ندارد: در واژه‌نامهٔ کنت تنها kasaka- «سنگ نیمه‌گران‌بها» هست که آن هم از ریشهٔ «درخشیدن» است. \"\n   \"نیبرگ نیز kasu- را صورت شمال‌غربی می‌شمارد و صورت جنوب‌غربی را *kaθu- بازسازی می‌کند. پس: با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:521\", \"status\": \"supports\",\n    \"note\": \"Pokorny p. 521 s.v. kak- 'abmagern': 'Av. kasu- „klein, gering“, Komp. Superl. kasyah-, kasišta-' — the three Avestan words of this node, in Nourai's order.\"},\n   {\"ref\": \"FFD:67\", \"status\": \"partial\",\n    \"note\": \"Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari, printed p. 67 (= FFD_pages.txt [pdf page 72], whose running head reads '۶۷'): s.v. کاستن 'کاست < ایرانی باستان *kāh-ta- ... kāh صورت بالاندهٔ ریشهٔ kah است به معنی «کوچک بودن»'. He reconstructs an Old Iranian root kah-, not an Avestan verb kās-, and says nothing about Old Persian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 459-461\", \"stance\": \"supports\",\n    \"note\": \"'kasav- Adj. „klein, gering“'; 'kasišta- Adj. a) „der kleinste“ ... V. 6.10'; 'kasyah- Adj. (auch fem.) „der kleinere, geringere“ ... mp. kēh, np. kih'. But s.v. kas- V.: 'nur mit ā \\\"gewahr werden, erblicken\\\"' — no verb 'to reduce'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon s.v. kasaka-\", \"stance\": \"contradicts\",\n    \"note\": \"'kasaka- sb. \\\"semi-precious stone\\\" ... deriv. of Iran. root *kas-, = Skt. kaś- \\\"be visible, appear, shine\\\"' — the only OP word of this shape, and it belongs to the other root; no OP kasu-.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. ¹kas\", \"stance\": \"partial\",\n    \"note\": \"'¹kas [ks] small ... NW form: Av. (460) kasu-, MPrth sup. ksyšt; SW *kaθu- which has survived in the comp. *kadyah- > kēh: MPrs gyh, Paz. NP keh; cf kāhišn.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 247 s.v. *kas¹\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: YAv. kasu- \\\"small, little\\\" (Yt 8.29, Yt 14.17, V 7.59, etc.), YAv. kasiiah- \\\"young\\\" (V 5.24, V 14.5, V 15.2)'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"-ak «ـک»; kâstan «کاستن»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The verb is right, the suffix is not. (1) kāstan 'to reduce', pres. kāh-: Horn no. 835 (Grundriss p. 185, one of \"\n   \"Nourai's citations) has 'kāsten \\\"vermindern, verringern\\\", Praes. kāh-em ... phlv. kahītan, kāhēt, kāhīnītan, kāh(i)šn. Wohl \"\n   \"zu demselben Stamm wie aw. kasu-, np. kih (No. 877)'; MacKenzie PHD prints 'kāstan, kah- [kʾstn', kʾh-] diminish, decrease, \"\n   \"lessen' and 'kahišn'; Nyberg (Manual II s.v. kāhišn) calls it 'a factitive vb. derived from the stem *kaθ-, SW form of kas-', \"\n   \"referring to his ¹kas 'small' = Av. kasu-; Abolqāsemi (FFD 67) reconstructs OIr. *kāh-ta- > kāst, the lengthened causative \"\n   \"grade of a root kah- 'to be small'; Cheung EDIV 247 files 'NP kāstan/kah-' under *kas¹. Moʿin's footnote 5 on BQT p. 1564 \"\n   \"says the same, citing Darmesteter and Horn. The only dissenting note is Hübschmann no. 835 (Persische Studien p. 86 — again \"\n   \"Nourai's own citation): kāstan 'passt in der Bedeutung trefflich zu zd. kasu-', BUT the attested Pahlavi kastak and kahišn \"\n   \"'deuten auf ein ap. kah oder kad als Wurzel'. So: MP kāh-/kāst- (past stem kāst < *kāh-ta-, with -h-t- > -st-) > NP \"\n   \"kāstan/kāhidan; the byforms کاهیدن، کاهش، کاست listed in the chart are all the same stem. (2) The diminutive suffix ـک -ak \"\n   \"(morḡak 'little bird') has nothing to do with kasu-: it continues Middle Persian -ak/-ag (kōdak 'small'), from Proto-Iranian \"\n   \"*-aka-, PII *-akas, the ordinary IE *-ko- adjective-forming suffix, cognate with Old Armenian -ak. Nourai's own NOTE, 'See \"\n   \"\\\"Akos\\\" for another possible root of suffix \\\"-ak\\\"', points to the correct answer; as drawn here the arrow is wrong, and \"\n   \"because the node's worst word governs, the node is disputed.\"),\n \"derivation_fa\": (\"فعل درست است، پسوند نادرست. «کاستن» (ستاک حال kāh-) از فارسی میانهٔ kāh-/kāst-، از ایرانی باستان *kāh-ta- \"\n   \"است؛ خوشهٔ *-ht- به -st- بدل شده و از همین‌جاست «کاهیدن، کاهش، کاست» که در نمودار آمده. هرن (شمارهٔ ۸۳۵، ص ۱۸۵) و مکنزی و \"\n   \"نیبرگ و چونگ و ابوالقاسمی همگی آن را به ریشهٔ kah/kas «خرد بودن» و به اوستایی kasu- می‌رسانند؛ تنها هوبشمان (شمارهٔ ۸۳۵، ص ۸۶) \"\n   \"احتیاط می‌کند و می‌گوید صورت‌های پهلویِ kastak و kāhišn بر ریشه‌ای kah یا kad دلالت دارند. اما پسوند تصغیرِ «ـک» ربطی به \"\n   \"kasu- ندارد: بازماندهٔ فارسی میانهٔ -ak/-ag (کودک) است، از ایرانی باستان *-aka- و هندوایرانی *-akas، همان پسوند \"\n   \"هندواروپایی *-ko-؛ هم‌ریشه با -ak ارمنی کهن. خودِ نورایی در یادداشت به ریشهٔ «Akos» اشاره کرده که پاسخ درست است. \"\n   \"پژوهش امروزی این بخش را رد می‌کند.\"),\n \"sources\": [W_KAST, W_AK],\n \"ref_check\": [\n   {\"ref\": \"HUB:86\", \"status\": \"partial\",\n    \"note\": \"Hübschmann, Persische Studien, printed p. 86 (leaf 97 of HUB.txt), no. 835: 'Np. kāstan „abnehmen, weniger werden“ passt in der Bedeutung trefflich zu zd. kasu- = np. kih „klein“, doch müsste ... Es liegen aber vor phl. kastak ..., kahišn ..., die auf ein ap. kah oder kad als Wurzel deuten.' Supports the sense-link, doubts the formal one; says nothing about the suffix -ak.\"},\n   {\"ref\": \"HRN:185\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss, printed p. 185 (leaf 207 of HRN.txt), no. 835: 'kāsten „vermindern, verringern“, Praes. kāh-em ... phlv. kahītan, kāhēt, kāhīnītan, kāh(i)šn. Wohl zu demselben Stamm wie aw. kasu-, np. kih (No. 877).'\"},\n   {\"ref\": \"BQT:1564\", \"status\": \"supports\",\n    \"note\": \"Read from data/verification/sources/refs/ocr/BQT/1564.png (transcript 1564.vision.txt), footnote 5 s.v. کاسته: 'کاستن = کاهیدن. پهلوی kâhîtan، kâhînîtan. بقول دارمستتر ... و هرن ... از ریشهٔ اوستایی kas-، kasu (= که [کوچک] فارسی) نشأت یافته ... در پهلوی kâstak (کاسته) و kâhishn (کاهش) آمده «هوبشمان ۸۳۵»'. No mention of the suffix -ak.\"},\n   {\"ref\": \"FFD:67\", \"status\": \"supports\",\n    \"note\": \"FFD_pages.txt [pdf page 72], running head '۶۷', s.v. کاستن: 'کاست < ایرانی باستان *kāh-ta- ... kāh صورت بالاندهٔ ریشهٔ kah است به معنی «کوچک بودن». صورت بالانده در معنی واداری به کار رفته است، به معنی «کوچک کردن». کاه < فارسی میانه kāh.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp. 49/50 (PHD_mackenzie.txt lines 3145, 3255)\", \"stance\": \"supports\",\n    \"note\": \"'kāstan, kah- [kʾstn', kʾh-] diminish, decrease, lessen'; 'kah-, ~išn, v. kāstan'; 'kāhidan [kʾhytn] = kāstan'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. kāhišn\", \"stance\": \"supports\",\n    \"note\": \"'kāhišn [kʾhšn'] the act or process of diminishing ... NP kāstan kāh- \\\"to lessen, to diminish\\\". A factitive vb. derived from the stem *kaθ-, SW form of kas-, v. s.v. ¹kas.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 247 s.v. *kas¹\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: NP kāstan/kah- \\\"to lessen, diminish\\\", Nn. käs, Tr. kas \\\"little; young\\\", Varz. kas \\\"little\\\"'; MP 'k'h- /kah-/ to diminish, decrease, lessen'.\"},\n   {\"src\": \"MON\", \"where\": \"Wiktionary/Moʿin tradition for the suffix ـک\", \"stance\": \"contradicts\",\n    \"note\": \"the Persian diminutive suffix ـک -ak is uniformly derived from Middle Persian -ak/-ag (< PIr. *-aka-), e.g. nēw > nēk, kōdak/kōdag 'small'; no source connects it with Av. kasu-.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\n# ---------------- entry 2 ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Kak 4, Gag\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"two separate etyma: (a) Aramaic/Syriac kaʿkā 'cake, loaf' < Akkadian kukku < Sumerian gug (a Near-Eastern wanderwort); (b) Germanic *kakōn-/*kōkan- 'cake' = Pokorny 349 gag-, gog- 'a round object', a nursery word of doubtful IE status\",\n \"note\": (\"The box merges two unrelated families. (a) The Semitic side. The Aramaic/Syriac word is kaʿkā (ܟܥܟܐ, Jewish Aramaic \"\n   \"כַּעְכָּא) 'cake, loaf', which Wiktionary takes from Akkadian kukku 'cake, loaf, pastry, lump of dough', ultimately Sumerian \"\n   \"gug 'offering; cake' — a wanderwort with look-alikes in Egyptian and Europe. Nourai's own source is Moʿin's footnote 4 on \"\n   \"BQT p. 1572, which reports Horn's view that Persian کاک is 'از لغات مستعار از آرامی' (borrowed from Aramaic), prints the \"\n   \"Aramaic word in Semitic type, cites Siddiqi p. 71 for the Arabicised کعک, and then adds Littmann's speculation: because \"\n   \"Greek kakeis and Coptic kake exist, 'می‌توان گفت که این کلمه اصلاً از سرزمین مصر است «هرمزدنامه ۱۳۳ بنقل از لیتمان»'. That \"\n   \"sentence, at second hand, is the sole basis for the chart's note 'This word is apparently of Egyptian origin'; no modern \"\n   \"Semitist repeats it. (b) The Germanic side. Pokorny 349 does have 'gag-, gog- \\\"a round object\\\", Note: word of the \"\n   \"Kindersprache', but its whole material is Germanic (Icel. kaka, Norw./Swed. kaka, Dan. kage, MLG kōke, OHG kuocho) plus \"\n   \"Lith. guogė 'cabbage head'; Walde-Pokorny I 530f. adds the warning 'Da idg. Wurzeln mit unaspirierter Media nicht zugleich \"\n   \"an- und auszulauten pflegen, bleiben an der sonst tadellosen Zusammenstellung Zweifel'. Watkins prints it in square \"\n   \"brackets — '[kak-2. A round object, disk. GERMANIC ROOT ... [In Pok. gag- 349.]]' — the AHD convention for a root that is \"\n   \"NOT Indo-European. Klein s.v. cake: 'prob. of imitative origin. The a-o gradation of these words testifies to their Teut. \"\n   \"origin.' So the 'Aramaic / Indo European' root as drawn, with Persian kāk and English cake hanging off one node, is a \"\n   \"conflation of two homophonous nursery/bread words; the Semitic branch and the Germanic branch have no common ancestor.\"),\n \"note_fa\": (\"این جعبه دو ریشهٔ نامرتبط را یکی کرده است. یکم، سویهٔ سامی: آرامی/سریانی kaʿkā «کاک، نان» که ویکی‌واژه آن را از \"\n   \"اکدی kukku «قرص نان، خمیر» و در نهایت سومری gug «قربانی؛ کاک» می‌گیرد — یک واژهٔ جهانگرد (wanderwort) خاورنزدیکی. منبع خودِ \"\n   \"نورایی حاشیهٔ ۴ معین در برهان قاطع ص ۱۵۷۲ است که رأی هرن را نقل می‌کند («کاک از لغات مستعار از آرامی است») و سپس گمانهٔ \"\n   \"لیتمان را می‌افزاید که چون در یونانی kakeis و در قبطی kake هست «می‌توان گفت که این کلمه اصلاً از سرزمین مصر است»؛ یادداشت \"\n   \"«خاستگاه مصری» در نمودار تنها بر همین جملهٔ باواسطه استوار است. دوم، سویهٔ ژرمنی: پوکورنی (ص ۳۴۹) ریشهٔ gag-/gog- «چیز گرد» \"\n   \"را دارد اما خود آن را «واژهٔ زبان کودکانه» می‌نامد و مواد آن یکسره ژرمنی است؛ والده-پوکورنی (ج ۱، ص ۵۳۰) در هندواروپایی \"\n   \"بودنش تردید می‌کند و واتکینز (AHD) آن را در قلاب و با برچسب «ریشهٔ ژرمنی» می‌آورد. کلاین نیز cake را «احتمالاً محاکات‌آمیز و \"\n   \"ژرمنی» می‌داند. پس پژوهش امروزی این ریشهٔ یگانه را رد می‌کند: کاکِ سامی و cake ژرمنی همانندهای تصادفی‌اند.\"),\n \"sources\": [W_KAAK, ETY_CAKE, W_KAK],\n \"ref_check\": [\n   {\"ref\": \"POK:349\", \"status\": \"partial\",\n    \"note\": \"POK_full.txt line 29594: 'Root / lemma: gag- gog- | Meaning: a round object | Note: word the Kindersprache | Material: Isl. kaka \\\"cake\\\", Norwegian and Swedish kaka ..., Danish kage ... (Germanic *kakan-) ... Old High German kuocho (Germanic *kōkan-) \\\"round bread, cake\\\" ... Page(s): 349'. The page supports the Germanic half of the box and nothing else — no Aramaic, no Persian, no Egyptian.\"},\n   {\"ref\": \"BQT:1572\", \"status\": \"supports\",\n    \"note\": \"Read from data/verification/sources/refs/ocr/BQT/1572.png (transcript 1572.vision.txt), footnote 4 s.v. کاک: 'هرن «کاک» بدین معنی را از لغات مستعار از آرامی می‌داند ...؛ در آرامی [Aramaic word in Semitic type]، معرب آن کعک (Siddiqi, Fremdwörter, p.71)؛ در زبانهای آلمانی و انگلیسی به گفتهٔ لیتمان Keeks و cakes با کاک و کعک ... یکی است، اما چون در زبان یونانی kakeis و در قبطی kake وجود دارد، می‌توان گفت که این کلمه اصلاً از سرزمین مصر است «هرمزدنامه ۱۳۳ بنقل از لیتمان»' — Nourai's root name, his Aramaic label and his Egyptian note all come from this footnote.\"},\n   {\"ref\": \"AHD:1520\", \"status\": \"partial\",\n    \"note\": \"the 1976 New College appendix is not open, but the same root stands in Watkins 1985 (AHD_watkins1985.txt line 573): '[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE. 2. Middle Dutch koeke, a cake: cooky. ... [In Pok. gag- 349.]]'. The square brackets mark it as a Germanic, not Indo-European, root — so AHD supports the Germanic sub-tree but contradicts the 'Indo European' label of the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 530-531\", \"stance\": \"contradicts\",\n    \"note\": \"'gag-, gog- „etwas Rundes, Klumpiges“ ... Da idg. Wurzeln mit unaspirierter Media nicht zugleich an- und auszulauten pflegen (siehe geb-), bleiben an der sonst tadellosen Zusammenstellung Zweifel.' Walde-Pokorny themselves doubt the IE status; the material is Germanic + Lith. guogė only.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cake (KLN_1966.txt line 6116)\", \"stance\": \"contradicts\",\n    \"note\": \"'cake, n. — ME., fr. ON. kaka, rel. to MDu. koke, Du. koek, its dimin. koekje, OHG. chuohho, kuocho, MHG. kuoche, G. Kuchen; prob. of imitative origin. The a-o gradation of these words testifies to their Teut. origin ... They are not related to cook.' No Semitic or Egyptian source.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. kakā (kakk-) (IEC.txt line 6623)\", \"stance\": \"partial\",\n    \"note\": \"'kakā (kakk-) \\\"excrement\\\". WP I, 336. Per. kak \\\"biscuit\\\"; Gk. káke ...' — Mann does record Persian kāk 'biscuit' in an IE comparative dictionary, but files it with the nursery word kakka-, not with gag- 'round object'; a further sign that all of these are Lallwörter rather than a reconstructible root.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen — searched\", \"stance\": \"silent\",\n    \"note\": \"grep for كعك / kaʿk finds no entry; Fraenkel does not treat the word among the Aramaic loans in Arabic.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"kâk «کاک»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Persian کاک kāk 'dry hard bread, a dry biscuit' is well attested (Borhān-e Qāṭeʿ p. 1572: 'و هرچیز خشک را گویند \"\n   \"عموماً و گوشت قدید را خصوصاً ... و نان خشک ... و معرب آن کعک است'; Loghat-e Fors p. 251 for the older sense 'man'; still \"\n   \"current in Kurdistan and Khorasan, where Moʿin notes it is called qāq in Mashhad). Nourai's arrow 'Aramaic gag > Persian \"\n   \"kāk' reproduces the view Moʿin reports in footnote 4 of that page: 'هرن «کاک» بدین معنی را از لغات مستعار از آرامی می‌داند' \"\n   \"— Horn treats it as a loan from Aramaic (kaʿkā), the ʿayn being lost in a Persian mouth (kaʿkā > kāk, with compensatory \"\n   \"lengthening of the first vowel). That is plausible and is the majority view for the Near-Eastern bread word; but Siddiqi \"\n   \"(p. 71) and Asbaghi (p. 233) run the traffic the other way (Arabic kaʿk < Persian kāk), and Wiktionary declines to choose, \"\n   \"saying only that Persian کاک is 'akin to ... Arabic كعك and Classical Syriac ܟܥܟܐ (kaʿkā)'. What is NOT plausible is the \"\n   \"root's second half: nothing links this word to the Germanic cake family.\"),\n \"derivation_fa\": (\"«کاک» فارسی به معنی «نان خشک، قرص خشک» گواهی استوار دارد (برهان قاطع ص ۱۵۷۲: «هر چیز خشک را گویند عموماً ... \"\n   \"و نان خشک ... و معرب آن کعک است»؛ معین می‌افزاید که در مشهد آن را «قاق» گویند). پیکانِ نورایی («از آرامیِ gag») همان رأیی است \"\n   \"که معین در حاشیهٔ ۴ همان صفحه از هرن نقل می‌کند: «هرن کاک را بدین معنی از لغات مستعار از آرامی می‌داند». از آرامی kaʿkā، با \"\n   \"افتادن عین و کشیده شدن واکهٔ نخست، به kāk فارسی می‌رسیم. این پذیرفتنی است، اما صدیقی (ص ۷۱) و اصباغی (ص ۲۳۳) جهت وام‌گیری را \"\n   \"وارونه می‌دانند و ویکی‌واژه هم داوری نمی‌کند. آنچه پذیرفتنی نیست پیوند این واژه با cake ژرمنی است.\"),\n \"sources\": [W_KAK],\n \"ref_check\": [\n   {\"ref\": \"BQT:1572\", \"status\": \"supports\",\n    \"note\": \"headword کاک with the senses Nourai gives, and footnote 4 'هرن «کاک» ... از لغات مستعار از آرامی می‌داند «اسفا ۱:۲ ص ۶»؛ در آرامی [ggʾ/kʿkʾ]' — read from the page image, transcript at data/verification/sources/refs/ocr/BQT/1572.vision.txt.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin's footnote in BQT 1572 (his Farhang has the same word)\", \"stance\": \"supports\",\n    \"note\": \"'و آنرا در مشهد «قاق» گویند' — Moʿin records the living Persian dialect forms alongside the Aramaic etymology.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. kakā (kakk-)\", \"stance\": \"partial\",\n    \"note\": \"'Per. kak \\\"biscuit\\\"' is listed, but under the nursery root kakā, not under gag- 'round object'.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss — the view cited by Moʿin\", \"stance\": \"supports\",\n    \"note\": \"Moʿin attributes to Horn the judgement that کاک is an Aramaic loanword; Horn's Grundriss keeps such Semitic loans out of the main IE numbering, which is why no numbered entry turns up on grep.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā — searched\", \"stance\": \"silent\",\n    \"note\": \"no کاک headword in ARY_pages.txt; Aryanpur covers only Indo-European material, so a Semitic loan is outside his scope.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"ka`k\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Arabic كعك kaʿk 'dry bread, biscuit, cake' is old (al-Jawāliqī, Muʿarrab p. 297, quoted by Moʿin: 'الكعك، نان \"\n   \"خشک. لیث گوید: گمان برم که معرب است'). Both of Nourai's citations do say what his arrow says. Siddiqi, Studien über die \"\n   \"persischen Fremdwörter im klassischen Arabisch, p. 71 (leaf 87 of SDQ.txt), in the section on how Persian sounds are \"\n   \"rendered in Arabic: 'Das ع in كعك ist schon im aram. ܟܥܟܐ (p. کاک) vorhanden' — i.e. the Arabic word answers to Persian \"\n   \"kāk, and its ʿayn is inherited from the Aramaic shape, not invented by the Arabs. Asbaghi, Persische Lehnwörter im \"\n   \"Arabischen p. 233, heads the entry 'kaʿk: \\\"Biskuit, Torte\\\" < pers. كاك kāk, syr. kaʿkā (pers. kāk), dtsch. Kuchen/Keks, \"\n   \"engl. cake', citing Brockelmann and Littmann. Modern lexicography prefers a shorter route: Wiktionary derives Arabic كعك \"\n   \"'from or cognate with Aramaic כַּעְכָּא / ܟܥܟܐ (kaʿkā, cake, loaf), from Akkadian kukku', with no Persian stage at all. So \"\n   \"the node's form and meaning are right and Nourai's references back him, but the direction Persian > Arabic is only one of \"\n   \"two competing accounts of a Near-Eastern culture word.\"),\n \"derivation_fa\": (\"عربی «کعک» واژه‌ای کهن است؛ جوالیقی در المعرّب (ص ۲۹۷) آن را «نان خشک» معنی کرده و از لیث نقل می‌کند که «گمان \"\n   \"برم معرّب است». هر دو ارجاع نورایی همین را می‌گویند: صدیقی (ص ۷۱) می‌نویسد «عینِ کعک از پیش در صورت آرامی ܟܥܟܐ (فارسی: کاک) \"\n   \"بوده است» و اصباغی (ص ۲۳۳) مدخل را چنین آورده: «kaʿk «بیسکویت، کیک» < فارسی کاک، سریانی kaʿkā». اما فرهنگ‌نویسیِ امروز راهِ \"\n   \"کوتاه‌تر را ترجیح می‌دهد: ویکی‌واژه «کعک» را یکسره از آرامی kaʿkā و آن را از اکدی kukku می‌گیرد، بی هیچ حلقهٔ فارسی. پس \"\n   \"با احتیاط پذیرفتنی است: صورت و معنا درست، ولی جهتِ وام‌گیری قطعی نیست.\"),\n \"sources\": [W_KAAK],\n \"ref_check\": [\n   {\"ref\": \"SDQ:71\", \"status\": \"supports\",\n    \"note\": \"SDQ.txt leaf 87 (printed p. 71): 'Das ع in كعك ist schon im aram. ܟܥܟܐ (p. کاک) vorhanden.' — the Arabic word is treated as the Persian kāk with the Aramaic ʿayn.\"},\n   {\"ref\": \"PLA:233\", \"status\": \"supports\",\n    \"note\": \"PLA_pages.txt leaf 248 (printed p. 233): 'kaʿk: \\\"Biskuit, Torte\\\" < pers. كاك kāk, syr. kaʿkā (pers. kāk), dtsch. Kuchen/Keks, engl. cake pers. kāk', with footnotes 3 Brockelmann, 4 Littmann.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cake\", \"stance\": \"contradicts\",\n    \"note\": \"Klein derives the European cake words purely from Germanic, so Asbaghi's parenthetic 'dtsch. Kuchen/Keks, engl. cake' beside kaʿk is a look-alike list, not an etymology.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān — searched\", \"stance\": \"silent\",\n    \"note\": \"grep of FVQ_pages.txt for kaʿk finds nothing; the word is not Qurʾānic, so Jeffery has no entry.\"},\n   {\"src\": \"AFM\", \"where\": \"Addī Shīr, al-Alfāẓ al-Fārisiyya al-Muʿarraba — searched\", \"stance\": \"silent\",\n    \"note\": \"grep of AFM_pages.txt for كعك returns no hit (the OCR of the Arabic headwords is poor, so this is a weak negative).\"},\n   {\"src\": \"BQT\", \"where\": \"Moʿin's footnote 4, p. 1572\", \"stance\": \"supports\",\n    \"note\": \"'معرب آن کعک (Siddiqi, Fremdwörter, p.71)' — Moʿin himself calls کعک the Arabicised form of کاک and cites the same Siddiqi page Nourai does.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"ka`k «کعک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"This is the return leg of an Arabic-mediated round trip, and it is exactly what the cited page states: Borhān-e \"\n   \"Qāṭeʿ p. 1572, in the entry کاک itself, 'و معرب آن کعک است' — the Arabicised form کعک re-entered Persian as a separate word \"\n   \"beside the native کاک. In modern Persian کعک is the ordinary word for a plain cake or sponge cake, spelt with the ʿayn \"\n   \"although Persian has no ʿayn phoneme (pronounced kaʿk/kak), the classic orthographic signature of an Arabic loan. Whether \"\n   \"the ultimate source is Aramaic (Horn, Wiktionary) or Persian کاک itself (Siddiqi, Asbaghi), the Persian کعک of this node is \"\n   \"in either case borrowed back through Arabic, so the arrow #2 > #3 stands.\"),\n \"derivation_fa\": (\"این گره حلقهٔ بازگشت یک دورهٔ وام‌گیری با میانجیِ عربی است و برهان قاطع (ص ۱۵۷۲) در همان مدخل «کاک» صریحاً \"\n   \"می‌گوید: «و معرب آن کعک است». صورت معرّبِ «کعک» دوباره به فارسی وارد شده و امروز واژهٔ معمول برای «کیک» است؛ نوشتنِ آن با \"\n   \"عین — با آنکه فارسی واج عین ندارد — نشانهٔ آشکار وام‌واژهٔ عربی است. چه خاستگاه نهایی آرامی باشد (هرن، ویکی‌واژه) چه خودِ \"\n   \"«کاکِ» فارسی (صدیقی، اصباغی)، این گره در هر دو حال از راه عربی به فارسی بازگشته است. ادعای نورایی درست است.\"),\n \"sources\": [W_KAAK],\n \"ref_check\": [\n   {\"ref\": \"BQT:1572\", \"status\": \"supports\",\n    \"note\": \"s.v. کاک, left column: '... و معرب آن کعک۴ است و بعضی گویند کاک قرص نان و روغنی است و آنرا بعربی کعک خوانند' (read from the page image).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p. 233\", \"stance\": \"supports\",\n    \"note\": \"Asbaghi's entry is for the Arabic kaʿk with Persian kāk as etymon; the Persian کعک of this node is that Arabic form re-borrowed, which is what Moʿin's 'معرب آن' means.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin (footnote 4 on BQT 1572)\", \"stance\": \"supports\",\n    \"note\": \"Moʿin quotes al-Jawāliqī p. 297: 'الکعک، نان خشک. لیث گوید: گمان برم که معرب است' — the Arabic lexicographers themselves treated کعک as a loan.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Germanic\", \"words\": \"kakan\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The form is right as a reconstruction: Pokorny 349 sets up Germanic *kakan- for Icelandic kaka, Norwegian and \"\n   \"Swedish kaka 'small, round and flat bread', Danish kage 'cake', beside the o-grade *kōkan- of MLG kōke and OHG kuocho \"\n   \"'round bread, cake' (with the diminutives OE cicel, cycel and OHG kuochelīn). Walde-Pokorny I 530 gives the same, and adds \"\n   \"that Germanic *kōkon- cannot be a loan from Romance because of the ablaut and the Finnic loans (Finn. kakko, Lapp. gakko \"\n   \"'cake'). What is doubtful is the parent: Pokorny himself files it as 'gag-, gog-', a 'word of the Kindersprache', \"\n   \"Walde-Pokorny state that a root with unaspirated media at both ends is against IE root structure, and Watkins brackets it \"\n   \"as a 'Germanic root'. So *kakan- descends from the Germanic/(pseudo-)IE gag- half of Nourai's box, and not at all from its \"\n   \"Aramaic half; and Nourai's bare 'kakan' should carry the asterisk and the final -an- of a reconstruction.\"),\n \"derivation_fa\": (\"صورتِ بازسازی‌شده درست است: پوکورنی (ص ۳۴۹) ژرمنی *kakan- را برای ایسلندی kaka، نروژی و سوئدی kaka «نان گردِ \"\n   \"کوچک و پهن» و دانمارکی kage بازمی‌سازد و در کنار آن گونهٔ o-دار *kōkan- را برای آلمانی میانهٔ سفلی kōke و آلمانی علیای باستان \"\n   \"kuocho. والده-پوکورنی نیز همین را می‌گوید و می‌افزاید که این واژه از رومی وام گرفته نشده، بلکه وام‌واژه‌های فنلاندی (kakko) \"\n   \"از ژرمنی‌اند. اما نسبِ آن مشکوک است: خودِ پوکورنی آن را «واژهٔ زبان کودکانه» می‌نامد، والده-پوکورنی ساختِ ریشه را با قواعد \"\n   \"هندواروپایی ناسازگار می‌بیند و واتکینز آن را «ریشهٔ ژرمنی» (نه هندواروپایی) می‌شمارد. افزون بر این، این گره تنها از نیمهٔ \"\n   \"ژرمنیِ جعبه سرچشمه می‌گیرد، نه از نیمهٔ آرامی آن.\"),\n \"sources\": [ETY_CAKE],\n \"ref_check\": [\n   {\"ref\": \"POK:349\", \"status\": \"supports\",\n    \"note\": \"'Isl. kaka \\\"cake\\\", Norwegian and Swedish kaka \\\"small, round and flat bread\\\", Danish kage \\\"cake\\\" (Germanic *kakan-) ... Old High German kuocho (Germanic *kōkan-) \\\"round bread, cake\\\"' — POK_full.txt s.v. gag- gog-, Page(s) 349.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985: '[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE ... [In Pok. gag- 349.]]' — same reconstruction, explicitly labelled Germanic.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 530-531\", \"stance\": \"partial\",\n    \"note\": \"gives the identical Germanic material but doubts the IE root: 'bleiben an der sonst tadellosen Zusammenstellung Zweifel'; also 'Germ. *kōkon ... nicht aus dem Romanischen'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cake\", \"stance\": \"supports\",\n    \"note\": \"'ON. kaka, rel. to MDu. koke, Du. koek ... OHG. chuohho, kuocho, MHG. kuoche, G. Kuchen ... The a-o gradation of these words testifies to their Teut. origin.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs — searched\", \"stance\": \"silent\",\n    \"note\": \"grep for Keks/kaʿk finds no entry: Lokotsch, whose whole subject is European words of Oriental origin, does not list cake/Kuchen among them — indirect evidence against an Aramaic source for the Germanic word.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"cake\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English cake first appears in the early 13th century, borrowed from Old Norse kaka (the Danelaw contact \"\n   \"period), not inherited: Etymonline, 'from early 13c. Old Norse kaka, from West Germanic *kokon-', noting that it 'replaced \"\n   \"the Old English cognate coecel' and that the old derivation from Latin coquere is abandoned; Klein s.v. cake, 'ME., fr. ON. \"\n   \"kaka'; Pokorny 349 says the same in passing, 'engl. cake is a Norse loanword'; Watkins routes CAKE through 'Old Norse \"\n   \"kaka'. The node is therefore right in substance — cake continues Germanic *kakan- — with the one refinement that the \"\n   \"immediate donor is Old Norse rather than a continuous English line.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی cake در آغاز سدهٔ سیزدهم میلادی از نورس باستان kaka به انگلیسی میانه وام گرفته شده است، نه اینکه \"\n   \"میراثی باشد؛ این وام‌گیری در دورهٔ دِین‌لا رخ داده و صورتِ بومیِ انگلیسی باستان coecel را کنار زده است (اتیمانلاین؛ کلاین: \"\n   \"«ME., fr. ON. kaka»). خودِ پوکورنی نیز در ص ۳۴۹ می‌نویسد «engl. cake وام‌واژه‌ای نورسی است». پس محتوای گره درست است — cake \"\n   \"دنبالهٔ ژرمنی *kakan- است — تنها با این ظرافت که وام‌دهندهٔ بی‌واسطه نورس باستان است.\"),\n \"sources\": [ETY_CAKE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book; verified instead against Etymonline, Klein and Pokorny 349 (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cake (KLN_1966.txt line 6116)\", \"stance\": \"supports\",\n    \"note\": \"'cake, n. — ME., fr. ON. kaka, rel. to MDu. koke, Du. koek, its dimin. koekje, OHG. chuohho, kuocho ... G. Kuchen.'\"},\n   {\"src\": \"POK\", \"where\": \"p. 349 s.v. gag-, gog-\", \"stance\": \"supports\",\n    \"note\": \"'wherefore the diminutive Old English cicel, cycel \\\"small cake\\\" (engl. cake is Norse loanword)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 [kak-2]\", \"stance\": \"supports\",\n    \"note\": \"'1. Old Norse kaka, cake: CAKE.'\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Dutch\", \"words\": \"koek\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Dutch koek 'cake' continues Middle Dutch koke, from the o-grade Germanic *kōkan- (Pokorny 349 groups 'Middle \"\n   \"Low German kōke, Old High German kuocho (Germanic *kōkan-) \\\"round bread, cake\\\"' with the a-grade *kakan- of ON kaka); \"\n   \"Klein lists 'MDu. koke, Du. koek' in the same set as ON kaka, and Watkins routes cooky through 'Middle Dutch koeke'. The \"\n   \"word is therefore a genuine member of the family, and Nourai is right to hang the English cookie off it. The 'plausible' \"\n   \"rather than 'confirmed' verdict is for the parentage drawn: koek does not descend from an 'Aramaic / Indo European' root \"\n   \"but from the Germanic ablaut variant *kōkan-, so it is a sibling of the node #4 form, not an independent branch of a \"\n   \"Semitic etymon.\"),\n \"derivation_fa\": (\"هلندی koek «کیک، نان شیرین» دنبالهٔ هلندی میانهٔ koke است، از گونهٔ o-دار ژرمنی *kōkan- که پوکورنی (ص ۳۴۹) \"\n   \"آن را در کنار گونهٔ a-دارِ *kakan- (نورس باستان kaka) می‌آورد؛ کلاین نیز MDu. koke و Du. koek را در همان خوشه جای می‌دهد. \"\n   \"پس واژه به‌راستی عضو این خانواده است و انشعابِ cookie از آن درست است. علت «با احتیاط پذیرفتنی»، نسبِ ترسیم‌شده است: koek از \"\n   \"ریشه‌ای «آرامی/هندواروپایی» نمی‌آید بلکه از دگرگونیِ آوایی درونِ ژرمنی برخاسته و در واقع خواهرِ صورتِ گرهِ ۴ است، نه شاخه‌ای \"\n   \"مستقل از ریشه‌ای سامی.\"),\n \"sources\": [ETY_CAKE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 [kak-2]: '2. Middle Dutch koeke, a cake: cooky.' — the AHD entry Nourai cites gives exactly this node and the next.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 349 s.v. gag-, gog-\", \"stance\": \"supports\",\n    \"note\": \"'Middle Low German koke, Old High German kuocho (Germanic *kōkan-) \\\"round bread, cake\\\"' — the ablaut grade behind Du. koek.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cake and s.v. cooky\", \"stance\": \"supports\",\n    \"note\": \"'rel. to MDu. koke, Du. koek, its dimin. koekje'; 'cooky, also cookie, n., a small cake. — Du. koekje, dimin. of koek, \\\"cake\\\".'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 530\", \"stance\": \"partial\",\n    \"note\": \"same Germanic set, but the IE root above it is questioned.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"cookie\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English cookie (cooky) 'a small, flat, sweet cake' is an American borrowing of Dutch koekje 'little cake', the \"\n   \"diminutive of koek, taken over from the Dutch of New Netherland in the 18th century: Klein, 'cooky, also cookie, n., a \"\n   \"small cake. — Du. koekje, dimin. of koek, \\\"cake\\\". See cake and dimin. suff. -y'; Etymonline, 'from Dutch koekje \\\"little \"\n   \"cake\\\", diminutive of koek \\\"cake\\\", from Middle Dutch koke'; Watkins likewise routes cooky through Middle Dutch koeke. \"\n   \"The only refinement to the chart is that the immediate source is the diminutive koekje, not the simplex koek — hence the \"\n   \"English -ie, which is the Dutch -je respelt.\"),\n \"derivation_fa\": (\"انگلیسی cookie «شیرینیِ کوچک و پهن» وام‌واژه‌ای آمریکایی از هلندیِ koekje «کیکِ کوچک» است؛ صورتِ مصغّرِ koek \"\n   \"که در سدهٔ هجدهم از هلندیِ نیو نِدِرلَند (نیویورکِ امروز) وارد انگلیسی شده. کلاین: «cooky, also cookie ... — Du. koekje, \"\n   \"dimin. of koek»؛ اتیمانلاین نیز همین را می‌گوید. تنها ظرافتِ لازم آن است که وام‌دهندهٔ بی‌واسطه صورتِ مصغّرِ koekje است نه \"\n   \"خودِ koek، و پایانهٔ -ie انگلیسی همان -je هلندی است. ادعای نورایی درست است.\"),\n \"sources\": [ETY_CAKE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"no reference in the book for this node; checked against Klein, Etymonline and Watkins (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cooky (KLN_1966.txt line 9093)\", \"stance\": \"supports\",\n    \"note\": \"'cooky, also cookie, n., a small cake. — Du. koekje, dimin. of koek, \\\"cake\\\". See cake and dimin. suff. -y.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 [kak-2]\", \"stance\": \"supports\",\n    \"note\": \"'2. Middle Dutch koeke, a cake: cooky.'\"}\n ]\n})\n\ndoc[\"entries\"].append(e2)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-235.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk235.py"
}
```


### [2026-09-06T15:59:49.928Z] TOOL RESULT

```
written
```


## [2026-09-06T15:59:54.608Z] TOOL CALL #105: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-235.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 235"
}
```


### [2026-09-06T15:59:57.232Z] TOOL RESULT

```
valid json
nodes verified: 14/14
node verdicts: {'confirmed': 5, 'plausible': 7, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1, 'disputed': 1}
ref checks: {'supports': 14, 'partial': 6, 'not_checked': 2}
books consulted: {'supports': 27, 'contradicts': 4, 'silent': 7, 'partial': 6} | by book: {'IEC': 5, 'KLN': 5, 'WLD': 4, 'MON': 4, 'POK': 3, 'SYN': 2, 'ARY': 2, 'PHD': 2, 'HRN': 2, 'NYB': 2, 'CHEUNG': 2, 'AHD': 2, 'HUB': 1, 'SOD': 1, 'BRT': 1, 'KNT': 1, 'FVQ': 1, 'AFM': 1, 'BQT': 1, 'PLA': 1, 'LKT': 1}
```


## [2026-09-06T16:00:02.256Z] TOOL CALL #106: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io,re\np=\"data/verification/page-235.json\"\ns=io.open(p,encoding=\"utf-8\").read()\ns=s.replace(\"cognate列\",\"cognate list\")\nio.open(p,\"w\",encoding=\"utf-8\").write(s)\nd=json.load(open(p))\n# scan for CJK\nbad=re.findall(r\"[一-鿿぀-ヿ]\", s)\nprint(\"cjk leftover:\", set(bad))\nEOF\npython3 tools/verify_check.py 235 | tail -3"
}
```


### [2026-09-06T16:00:04.049Z] TOOL RESULT

```
cjk leftover: set()
root verdicts: {'confirmed': 1, 'plausible': 1, 'disputed': 1}
ref checks: {'supports': 14, 'partial': 6, 'not_checked': 2}
books consulted: {'supports': 27, 'contradicts': 4, 'silent': 7, 'partial': 6} | by book: {'IEC': 5, 'KLN': 5, 'WLD': 4, 'MON': 4, 'POK': 3, 'SYN': 2, 'ARY': 2, 'PHD': 2, 'HRN': 2, 'NYB': 2, 'CHEUNG': 2, 'AHD': 2, 'HUB': 1, 'SOD': 1, 'BRT': 1, 'KNT': 1, 'FVQ': 1, 'AFM': 1, 'BQT': 1, 'PLA': 1, 'LKT': 1}
```


## [2026-09-06T16:00:20.662Z] AGENT

Page 235 (book p. 205) verified — `data/verification/page-235.json` written, `verify_check.py 235` reports 14/14 nodes, **0 PROBLEM lines**.

**Counts** — roots: 1 confirmed, 1 plausible, 1 disputed. Nodes: 5 confirmed, 7 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 14 supports, 6 partial, 2 not_checked (nodes with no refs in the book). 21 different books consulted.

**Flagged items**
- **disputed — Kak 3, #2 `-ak` (ـک)**: the Persian diminutive suffix continues MP `-ak/-ag` < PIr `*-aka-` < IE `*-ko-`; it has nothing to do with Av. `kasu-`. The verb `kāstan` in the same node is fully confirmed (Horn 185, MacKenzie, Nyberg, Cheung 247, FFD 67), so the node takes the worse verdict. Nourai's own NOTE ("see Akos") points to the right answer.
- **disputed — ROOT Kak 4, Gag**: the box merges two unrelated etyma. Aramaic/Syriac `kaʿkā` < Akkadian `kukku` < Sumerian `gug` (a Near-Eastern wanderwort) vs. Germanic `*kakan-` = Pokorny 349 `gag-/gog-`, which Walde-Pokorny I 530 itself doubts as IE and Watkins brackets as a *Germanic* root; Klein calls cake "prob. of imitative origin… Teut." The "apparently of Egyptian origin" note traces to Littmann's guess quoted at second hand in Moʿin's footnote on BQT 1572.
- **transcription_suspect — Kâk 2, #5 Sogdian `šnk`**: Gharib SOD entry 9311, printed p. 376 (the cited page) prints **`šnx`** /šanx/ with the etymology "<IE ḱank" — i.e. the derivation is confirmed, only the final letter is wrong. `error_in: book` — the printed page 235 shows `šnk`, so this is Nourai's misprint, faithfully extracted.

**Extraction errors: none.** The JSON matches the printed page throughout (checked against the page image, copied to `data/verification/sources/refs/ocr/BOOK/235.png`).

Notable partials: Persian `šāx` is inherited (PIr `*ćāxā-` > MP `šāk`), a cognate of Skt `śākhā`, not a descendant — though Pokorny 523 himself floats the loan idea Nourai drew. Root Kak 3 stands in Pokorny 521 verbatim but Cheung (EDIV 247) calls it "apparently Ir. … no certain IE provenance." Four new BQT page transcriptions were saved (`ocr/BQT/1219|1280|1564|1572.vision.txt`) and 7 web pages archived via `fetch_source.py`.
