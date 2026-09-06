# Verification process log — verify-page-252


## [2026-09-06T16:04:12.348Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 252 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-252.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-252.json. Write /home/sfmqrb/git/rishe/data/verification/page-252.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 252` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:04:13.839Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:04:14.667Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:04:14.683Z] TOOL RESULT

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


## [2026-09-06T16:04:15.227Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-252.txt"
}
```


### [2026-09-06T16:04:15.260Z] TOOL RESULT

```
1	=== PDF page 252 (book page 222) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kel 4, Qel : gray, black, dark  (refs POK:546; KLN:316)
4	#1 (parent #0) [Persian] refs=POK:547 | čarmeh «چرمه» : horse
5	#2 (parent #0) [Greek] refs=POK:547 | kolumbos : a gray bird
6	#3 (parent #0) [Latin] refs=AHD:264 | col-umba : gray bird, pigeon, dove
7	  #4 (parent #3) [English] refs=AHD | Columbia, Colombia, Columbus, Columba, Colombo ; columbarium : a pigeonhole in a dovecote | NOTE: These words reached English through Italian, Spanish and other languages
8	--- entry 1 ---
9	ROOT [Indo-European] Kel 5 : cup, bowl  (refs POK:550)
10	#1 (parent #0) [Greek] refs=POK:550 | kalix : cup
11	  #2 (parent #1) [Syriac] refs=AFM:131 | 
12	    #3 (parent #2) [Persian] refs=AFM:131; MON | kâseh «کاسه ( کاس ۱ ، کاسبرگ )» : bowl ; kŭzeh «کوزه ( کوز ۱ )» : pitcher, jug
13	      #4 (parent #3) [Arabic] refs=AFM:131; VDQ:355 | ka`s : cup
14	  #5 (parent #1) [Latin] refs=POK:550 | calix : cup
15	#6 (parent #0) [Sanskrit] refs=POK:550 | kalasah : cup
16	--- entry 2 ---
17	ROOT [Indo-European] Kel 6 : to strike, cut, stab  (refs POK:545)
18	#1 (parent #0) [Persian] refs=MON:3037; IEC:464 | kaland, kolang «کلند ، کلنگ» : spade
19	#2 (parent #0) [Latin] refs=AHD:1521 | gladius : sword
20	  #3 (parent #2) [English] refs=AHD | gladiator
21	  #4 (parent #2) [French] refs=VOP:307 | gladiyator
22	    #5 (parent #4) [Persian] refs=VOP:307 | gelâdîyâtor «گلادیاتور» : gladiator
23	#6 (parent #0) [Latin] refs=AHD:1521 | clamitas : injury
24	  #7 (parent #6) [English] refs=AHD | calamity
25	#8 (parent #0) [Greek] refs=AHD:1521 | klon : twig
26	  #9 (parent #8) [English] refs=AHD | clone
27	
```


## [2026-09-06T16:04:18.336Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-252.json",
 "description": "Read source JSON for page 252"
}
```


### [2026-09-06T16:04:18.375Z] TOOL RESULT

```
{
  "pdf_page": 252,
  "book_page": 222,
  "entries": [
    {
      "root": {
        "name": "Kel 4, Qel",
        "lang": "Indo-European",
        "refs": "POK:546; KLN:316",
        "gloss": "gray, black, dark"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:547",
          "words": [
            {
              "translit": "čarmeh",
              "gloss": "horse",
              "script": "چرمه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "پر از خشم و پر کینه سالار نو - نشست از بر چرمهٔ تیز رو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:547",
          "words": [
            {
              "translit": "kolumbos",
              "gloss": "a gray bird",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:264",
          "words": [
            {
              "translit": "col-umba",
              "gloss": "gray bird, pigeon, dove",
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
          "refs": "AHD",
          "words": [
            {
              "translit": "Columbia, Colombia, Columbus, Columba, Colombo",
              "gloss": null,
              "script": null
            },
            {
              "translit": "columbarium",
              "gloss": "a pigeonhole in a dovecote",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "These words reached English through Italian, Spanish and other languages",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kel 5",
        "lang": "Indo-European",
        "refs": "POK:550",
        "gloss": "cup, bowl"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:550",
          "words": [
            {
              "translit": "kalix",
              "gloss": "cup",
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
          "lang": "Syriac",
          "refs": "AFM:131",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "AFM:131; MON",
          "words": [
            {
              "translit": "kâseh",
              "gloss": "bowl",
              "script": "کاسه ( کاس ۱ ، کاسبرگ )"
            },
            {
              "translit": "kŭzeh",
              "gloss": "pitcher, jug",
              "script": "کوزه ( کوز ۱ )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "AFM:131; VDQ:355",
          "words": [
            {
              "translit": "ka`s",
              "gloss": "cup",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Latin",
          "refs": "POK:550",
          "words": [
            {
              "translit": "calix",
              "gloss": "cup",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:550",
          "words": [
            {
              "translit": "kalasah",
              "gloss": "cup",
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
        "name": "Kel 6",
        "lang": "Indo-European",
        "refs": "POK:545",
        "gloss": "to strike, cut, stab"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:3037; IEC:464",
          "words": [
            {
              "translit": "kaland, kolang",
              "gloss": "spade",
              "script": "کلند ، کلنگ"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "کو حمیّت تا زتیشه وز کلند - اینچنین کُه را بکلی برکنند",
            "poet": "Molavî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1521",
          "words": [
            {
              "translit": "gladius",
              "gloss": "sword",
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
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "gladiator",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "VOP:307",
          "words": [
            {
              "translit": "gladiyator",
              "gloss": null,
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
          "lang": "Persian",
          "refs": "VOP:307",
          "words": [
            {
              "translit": "gelâdîyâtor",
              "gloss": "gladiator",
              "script": "گلادیاتور"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1521",
          "words": [
            {
              "translit": "clamitas",
              "gloss": "injury",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "calamity",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1521",
          "words": [
            {
              "translit": "klon",
              "gloss": "twig",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "clone",
              "gloss": null,
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


## [2026-09-06T16:04:19.063Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:04:19.101Z] TOOL RESULT

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


## [2026-09-06T16:04:30.484Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','AFM','MON','IEC','VDQ','VOP','LKT','SYN','WLD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-06T16:04:31.258Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kel-\" POK_full.txt | sed -n '1,80p'"
}
```


### [2026-09-06T16:04:32.469Z] TOOL RESULT

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
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


### [2026-09-06T16:04:32.524Z] TOOL RESULT

```
29740:See also: compare the similar to onomatopoeic words ghel-, kel-. 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44749:Note: separation from kel- 'prick' and from skel- 'cut, clip' is barely feasible; observed esp. 
44793:from *kel-nd: percello, -culi^ to beat down, throw down, overturn, upset ', se procellere^ 
44875:Beitr. 169), kalka-m. 'ordure, filth ', casa- m. "the blaue Holzhaher' {*kel-so-)\ 
44898:II. root form kal- : Ara/-(with unclear relationship to kel-): 
44927:Root / lemma: kel-5 
44960:See also: probably identical with kel-6; s. also keleu-^ wander '. 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45034:Similar to skel-, (sjk^el- {s-D\Me\.\.e besides kel-)\ 
45036:1. skel-: Old Icelandic skja//a stem V. 'sound, clink, loud hit' = Old English sciellan 
45048:"bell'; with plain /(-/A based on the aforementioned in a /7-present *skel-nd) Old Icelandic 
45064:also KuAAa okuAq^. HAeToi Hes., as from *skel-\.\\e above called Lithuanian skalikas, and 
45065:from kel- from: Lithuanian kale, /ra/e "bitch', alb. ke/i/sh'cub, esp. young dog'. Middle Irish 
45074:See also: probably identical with kel-5. 
45077:Root / lemma: kel-7{kol-, kj^ 
45096:There s- also in Modern High German Schale^ shell ' (that to {s)kel- "cut, clip') and in gr. 
45105:Root / lemma: kel-7 
45109:See also: see below (s)kel- 
46436:Note: and probably also bloftes ker-, compare also kel-4 and ker-6. 
47147:Root / lemma: kel-, kol-, kal- 
47347:References: WP. I 490; compare 6. kel-. 
49898:See also: about kel- ' incline ' (with velar) s. (s)kel- 'bend'. 
49989:also under (s)kel-^S'^\\\!\ Old High German Old Saxon halla. Old English heair hall ', Old 
51377:rhyme word Lithuanian kleTvas, klyvas^ bowlegged' see below (s)kel- ^ber\d'; different 
51392:See also: extension from Rel-2^ incline '; s. also under (s)kel-bev\6\ 
51565:applied, would be for kleu- : kel- the relation sreu-' flow ' : ser- either model or parallel. 
73956:Root / lemma: ser-1 ( *ker- < *kel-) 
75123:Root / lemma: (s)kel-1 
75127:Note: not reliable from kel- 'hit' and kel- 'prick' (above S. 545 f.) to separate. 
75154:/7c»/e"thin, fine, tender'; f. "Zartheif {*skel-)\ /7e/"Pfrieme, pricker, awl', /7e/e"Bratspieft, spit, 
75163:without anI. 5- perhaps here: Latin cu/ter, -//7 "knife' {*kel-tro-s, *kol-tro-s or* M-tros); celtis 
75204:with lengthened grade *skel- (compare alb. Iioie): Old Icelandic skalai. "drinking bowl, 
75322:Root / lemma: (s)kel-2 
75346:See also: compare (s)kel-47 
75351:Root / lemma: (s)kel-3 
77543:See also: whether expressive formation to (s)kel-41 
77870:Root / lemma: (s)k''el-5, (s)kel- 
77872:See also: see above S. 550 {kel-). 
93757:Note: probably extension from kel-5.
```


## [2026-09-06T16:04:37.340Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: kel\" POK_full.txt; echo ---; sed -n '44745,44760p;44920,44975p' POK_full.txt"
}
```


### [2026-09-06T16:04:37.408Z] TOOL RESULT

```
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
47147:Root / lemma: kel-, kol-, kal- 
93753:Root / lemma: keleu- 
---
Root / lemma: kel-3, kela-, A/a- extended klad- 

Meaning: to hit, cut down 

Note: separation from kel- 'prick' and from skel- 'cut, clip' is barely feasible; observed esp. 

Slavic *^d///'prick' = Baltic kalti'hW:. 

Material: Gr. kzKzoq, {*kzKzV6(^) ' green woodpecker ' (as 5puKoAanTr|<;); keAsk; a^ivr) Hes.; 

KsAoi ' ^uAa ' after Hesee below KzKzoy^ao;, SiKcAAa ' two-pronged fork, hack, mattock, hoe 

'; compare OKaAic; 'hack, mattock, hoe' under s/re/- 'cut, clip';K6Aoq 'mutilated, unhorned ', 

K6A-oupo(; ' with trimmed tail ', KoAa^u) ' mutilate, hinder; castigate, punish ', koAouoj ' 


Maybe alb. kaush " cup ' a Slavic loanword. 

References: WP. I 440 ff., WH. I 139 f., 249, Specht Indo Germanic Dekl. 118, 140, 1433, 
Trautmann 113f., Petersson Heterokl. 146 f. 
Page(s): 547-548 

Root / lemma: kel-5 

Meaning: to drive, force to move quickly 

Material: Old Indie kalayati^ floats, carries, perceives, holds '; 

alb. Geg qil, sizil. (/©/"bring, bear', shqiltse^ rennin, enzyme used to curdle milk and 
produce cheese, active component in rennet (derived from the mucous membrane of the 
fourth stomach of young cows), a means of coagulation, a coagulum or coagulator (the 
curdled milk in the stomach of a sucking animal, the stomach itself, etc.), rennet or runnet, 
(that which holds or binds together) ', probably also kal, kair cause, make happen, bring 
about, put, place ' (Jokl IF. 30, 198); 

gr. keAAcjo "drive on; land; go ashore (from a boat); arrive on the ground, touch ground ' 
(present only by Gramm. and in 6-keAAu) trans. " go ashore; run ashore, fail, be 
unsuccessful, make unsuccessful, break down, fall through '; otherwise only Aor. Fut. 
£K£Aaa, KsAaoj), KsAric;, -nTO(; " rusher, racer (horse); quick-sailing ship'; kAovoc; " intense 
movement', kAoveoo " drive tumultuously or in confusion, o be agitated, rush wildly, o be 
beaten by the waves ' (compare 9p-6voc;, xp-6vo^; Boisacq s. v. m. Lithuanian); perhaps 
(Persson Beitr. 179) koAeTv sAGeTv undKoAsa, KoAia 'kind of dance ' Hes.; 

Latin ce/eA "quick, fast, rash, hasty' (as K£Ar|<;), celeber, -bris, -bre^ frequented, much 
visited, thronged, crowded, populous, abounding ' {*keleA^lo-, -d'^/f-); 

as /-present Gothic haldan^ tend, feed, graze cattle ' (to a-Vok. s. Brugmann IF. 32, 
181), Old High German ba/tan ^beware, guard, hold, stop'. Old Saxon haldan. Old English 
healdan. Old Icelandic halda. Old Swedish halla {* halt^an) "hold, stop'. Middle Low 
German hilde, /7///e"rash, hasty, keen, eager'. 

References: WP. I 442 f., WH. I 194f.; 



See also: probably identical with kel-6; s. also keleu-^ wander '. 
Page(s): 548 

Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 

Meaning: to call, cry 

Material: Old Indie usa-kala-m. 'rooster, cock' ('rii-Kav6(;'), kaladhika-, kalavika-^s., kala- 

v/fjka-' sparrow', ka/a- - " leise tonend, undeutlich vernehmbar', ka/aka/a-m. ' bewildered 

clamor, noise'; 

gr. kqAeoj (instead of *KaA(jo) " call, summon, name, rufe herbei' (Aeolic KaAnM')- Futur. 
KaAsGU), Attic kqAu), Perf. K£KAr|Ka, kApitoc;; sniKAnoK; "epithet', kAhok; "shout, call, 
invitation, subpoena, invitation to court, summoning ', KAr|Tn(;, K(a)AriTwp "Rufer', opiOKAr)
```


## [2026-09-06T16:04:38.620Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kel-4\\|kel- 4\\|Kel 4\" POK_full.txt | head -20; echo \"=== POK_01/02 page hunt ===\"; grep -n \"columba\\|kolumbos\\|kolumbis\" POK_full.txt | head -20"
}
```


### [2026-09-06T16:04:38.702Z] TOOL RESULT

```
46436:Note: and probably also bloftes ker-, compare also kel-4 and ker-6. 
75346:See also: compare (s)kel-47 
77543:See also: whether expressive formation to (s)kel-41 
=== POK_01/02 page hunt ===
36457:holub ds., etc.; to this formation compare Latin columba, palumbesds.; 
44884:Latin columbai., -usm. " a dove, pigeon ' from *ko/-on-b^o- or *kolu-irb^o-, then
```


## [2026-09-06T16:04:44.291Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44820,44930p' POK_full.txt"
}
```


### [2026-09-06T16:04:44.361Z] TOOL RESULT

```
fltextension kelad-, klad-: 

Gr. KAa5ap6q {*kladeros) "frail, breakable; decrepit, antiquated ', KAaSaaai oeTaai Hes., 
ablaut. KaAa5ia puKavri Hes., Kkdboo, m. "twig, branch', conservative o'-stem *KKdc„ KKdbza\ 
etc. ds., KAa5u)v, -ovoq Hes. ds., KAaara^u) " dress vines, cut grapevine '; 



Latin cladesi. ' injury; damage, mischief, beating '; 

Middle irisli c/a/c//m'6'\tc\r\, grub' (witli acf- " pursue, liunt, cliase, fisli, catcli fisli ' etc.), 
cymr. claddu, bret. c/aza'dig'. Middle Irish clad, cymr. cladd^6\\.c\\, trench, channel'; 
lengthened grade cymr. clawdd, corn, c/a^o'" ditch, trench, channel', bret. A/e^z "ditch, 
trench, channel, hedge ' {*klado-)\ cymr. c/eddyr sword', bret. /r/eze "sword, blade' {cleddyf 
diss, from *cledyd, Celtic *kladjos), Irish claideb\s loanword from Cymr., Latin gladius 
"sword' from Celtic; 

Middle Irish ca/7/{Gen. caille) "wood, forest', cymr. ce///"wood, forest', corn, kelli^ a tract 
of woodland, forest pasture, meadow with shade, grove ' (Celtic *kaldl); 

Old Irish cymr. coll, bret. /rc»//"ruin, damage'; Middle Irish cellach^war, fight' and those 
related to it Old Icelandic hlldrt "fight, struggle, fight goddess ', Old Saxon Old English hlld 
" struggle, war, fight'. Old High German hlltia, M/a "fight, struggle' have Indo Germanic -d^- 
and probably as basic meaning "hit, lash out '; 

Gothic halts. Old Icelandic haltr. Old English healt. Old High German /75/z"lame' (= Old 
Irish coll, basic meaning " broken '), perhaps at first from fragmented limbs; 

Old Icelandic Old English holt. Old High German /7o/z"wood, forest' (= KAaSoq), in 
addition Old Icelandic hjaltu. " the hilt of a sword ', Old English hiitt ds.. Old High German 
helza " the hilt of a sword, haft ', Old Saxon helta " handle in the oar '; 

Old Bulgarian klada^ba\k, beam, block', russ. koloda^ chunk of wood, clot, chunk, tree 
block, from a chopped piece trunk ' etc.; Church Slavic /r/aoVVo "hammer' (proto Slavic 
*klad-: Latin clades). 

Labial extension: 

klomb(h)o-\n. gr. KAa|jp6(; "mutilated'. Old English laempi-halt, lamp-healt^ lame ' 
(Specht Indo Germanic Dekl. 262); compare Lithuanian klumbas^\axr\e\ 

References: WP. I 436 ff., WH. I 135 f., 225 f., 691, Specht Indo Germanic Dekl. 130 f., 
262, 322, Trautmann 1 14 f. 
Page(s): 545-547 

Root / lemma: AeMand kal- 
Meaning: a kind of dark/light spot 
Note: compare also ker-3ax\(i kers-1. 



Material: I. Old Indie kalaijka-xw. " stain, Rost', kalana-v\. " stain, smut', ka/usa-'dkiy, 
filthy, black', kalmasa- m. " stain, smut', /ra//77asa- 'varicolored, dappled '; with formants - 
ko-: karka- "white', m. " mildew ', karkTvasa^ white cow', karka^ white mare' (Persson 
Beitr. 169), kalka-m. 'ordure, filth ', casa- m. "the blaue Holzhaher' {*kel-so-)\ 

npers. carma^ mildew ', Kurdish ce/777e "white' (: Swiss helm); 

gr. KsAaivoq "black', KiAAoq "gray', k\KKoc, " donkey ' and " cicada ' (vowel as in niAv6(; 
besides -nzhbc;, -kk- from -Av-?); very probably K6Au|jpO(; ( *ko/u-nib'^os) " diver (bird's kind) 
', whereof KoAuppaw " dive ', called from the dark color; here also K\kk-ovpoq " wagtail ' 
Hes.; 

Latin columbai., -usm. " a dove, pigeon ' from *ko/-on-b^o- or *kolu-irb^o-, then 
identical with K6AupipO(;; to -mb- from -irb^- s. Schwyzer Gr. Gr. I 333; 

Modern High German Swiss /7e//77 "weifter stain beim Vieh auf the forehead', helme 
"name of a cow with white-mottled head ', Swedish dial, hjalm " white ox or white horse' 
(compare to /77-forms Old Indie kalmasa-); probably Middle High German hilwei. "fine fog', 
Bavarian geh/'/blog, Herdrauch' {-\/v-\n relationship to i/from Old Indie kalusa-h), 
wherefore Old High German huliwa' moisture, dampness, swamp, marsh, bog, mud ', 
Middle High German /7j/M/e "puddle, slop, pool, swamp ' stands in ablaut; 

here (from the black berries) also Old High German holuntar, ho/antar'e\6er', Old 
Swedish hylleAs.; s. Berneker473 m. Lithuanian, the also for russ. /ra///7a "Viburnum 
opulus, common snowball ' considers affiliation to kalt (see below). 

II. root form kal- : Ara/-(with unclear relationship to kel-): 

Gr. Kr|Ai(;, -\boc, (Doric mK\c;) " stain ', Kr|Ai56u) "sully, dirty, soil ', Kr|Arivr| [jsAaiva Hes., 
Kr|Aa(; vscpsAn avuSpoc; Koi x£i|J£pivn t\\xipa Koi ai^, nriq Kara to petojttov ar||J£Tov 
£X£iTuAo£i5£(; Hes.; 

Latin calidus, callidus {G\.) " warm, hot, fiery, rash, eager, spirited, fierce, impassioned, 
vehement, hasty, rash, practised, shrewd, experienced, adroit, dexterous *(from horses)' = 
Umbrian kalefuf{buf) " adroit, (oxen)'; Latin calTgoi. "fog, darkness '; 

Old Irish caile. Middle Irish gaib " stain '; 



Lithuanian kalybas, kalyvas " weiflhalsig '; 



Old Church Slavic kali, " dark-coloured, ordure' with the meaning "swamp, marsh, 
morass, smudge with ordure '; in addition (after the paint, color) russ. kalfna " Viburnum 
opulus, common snowball ', as also sloven. /ra///7a "puddle, slop' and russ. kalu-ga 
"morass', /ra/Z/-za "puddle'. 

Maybe alb. kaush " cup ' a Slavic loanword. 

References: WP. I 440 ff., WH. I 139 f., 249, Specht Indo Germanic Dekl. 118, 140, 1433, 
Trautmann 113f., Petersson Heterokl. 146 f. 
Page(s): 547-548 

Root / lemma: kel-5 

Meaning: to drive, force to move quickly
```


## [2026-09-06T16:05:04.992Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"calix\\|kalasa\\|KuAiE\\|kylix\\|Kelch\" POK_full.txt | head -30"
}
```


### [2026-09-06T16:05:05.040Z] TOOL RESULT

```
45083:Material: Old Indie kalasa-hxn. "pot, pan, crock, pitcher, bowl' {*koleko-, -oko-); 
45087:= Latin callx, -Iclsm. "deep bowl, goblet, calix' (from callx6emes Old High German 
45088:chellh. Modern High German Kelch " calix '), wherefore perhaps with moveable s Umbrian 
45093:low bowl, flattened dish, saucer, libation-saucer '; Latin culigna^ small calix' from gr. 
45100:(different in gutturals of suffixes from kalasa-h).
```


## [2026-09-06T16:05:05.469Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/Page\\(s\\): 549|Page\\(s\\): 550|Page\\(s\\): 549-550|Page\\(s\\): 550-551/{print NR\": \"$0}' POK_full.txt | head"
}
```


### [2026-09-06T16:05:07.735Z] TOOL RESULT

```
45103: Page(s): 550-551
```


## [2026-09-06T16:05:09.851Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45077,45115p' POK_full.txt"
}
```


### [2026-09-06T16:05:09.902Z] TOOL RESULT

```
Root / lemma: kel-7{kol-, kj^ 

Meaning: goblet 

Note: with ^-suffix 

Material: Old Indie kalasa-hxn. "pot, pan, crock, pitcher, bowl' {*koleko-, -oko-); 

gr. KuAi^, -iKoq "goblet' {*keli-k); 

= Latin callx, -Iclsm. "deep bowl, goblet, calix' (from callx6emes Old High German 
chellh. Modern High German Kelch " calix '), wherefore perhaps with moveable s Umbrian 
skalge-ta, scalse-to lormer \ow bowl, flattened dish, saucer, libation-saucer', scalsle"\n a 



low bowl, flattened dish, saucer, libation-saucer '; Latin culigna^ small calix' from gr. 
KuAixvP) (*KuAiK-ava) ds.; 

There s- also in Modern High German Schale^ shell ' (that to {s)kel- "cut, clip') and in gr. 
GKoAAiov, aKaAi(; ds. Hes.,. 

In addition gr. kqAu^, -ukoc; f. " fruit cup, grain cup ' and perhaps Old Indie kalika\. "bud' 
(different in gutturals of suffixes from kalasa-h). 

References: WP. I 442, WH. 1138 f. 
Page(s): 550-551 

Root / lemma: kel-7 

Meaning: " chop, cut '; " be at fault, be to blame, be wrong; " parch, dry '; " bend ' 

See also: see below (s)kel- 

Page(s): 551 

Root / lemma: kelp-, l^lp- 

Meaning: jar, cauldron
```


## [2026-09-06T16:05:45.309Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins kel ===\"; grep -n \"kel-\\b\" AHD_watkins1985.txt | head; echo \"--- gladius/clades/calamity in AHD ---\"; grep -n -i \"gladius\\|clades\\|calamity\\|columba\\|kolumbos\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T16:05:45.401Z] TOOL RESULT

```
=== AHD watkins kel ===
602:kel-1, To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. I. Basic form *kel- in suffixed o-grade form *kol-o- in Greek kolos, docked, kolobos, maimed: COLOBOMA. II. Extended form *keld-. 1.Germanic *helt- in Old English hilt: HILT. 2. Zero-grade extended form *kid- in a. Germanic *hulta- in Old English holt, wood: HOLT; b. Greek klados, branch, shoot: CLADOCERAN, CLADODE, CLADOGENESIS, CLADOPHYLL, PHYLLOCLADE. 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad- ibo- in Gaelic claidheamh, sword: CLAYMORE. 4. O-grade extended form *kold- in: a. Germanic *haltaz, “with a broken leg,” in Old English compound lemphealt, limp- ing, halting (lemp-, hanging loosely; see leb-'), probable source of obsolete limphalt, lame: LIMP; b. Germanic derivative verb *haltén in Old English healtian, to limp: HALT’, III. Extended form *keb-. 1. Zero-grade form *klo- in: a. Greek kia- in (i) Greek klan, to break: CLAST, CLASTIC; CLASMATOCYTE, OSTEOCLAST, PLAGIOCLASE (ii) Greek klén (< *kla-6n), twig: CLONE; b. suffixed form *klo-ro- in Greek kléros, lot, allotment (< “that which is cut off”): CLERK; C. suffixed form *kb-mn in Greek kléma, twig: CLEMATIS; d. suffixed form *kb-mo- in Latin calamitds, injury, damage, loss: CALAMITY. 2. O-grade form *kob- in suffixed form *kols-bho- in Greek kolaphos, a blow: coPE!, coup. See extension kleg-. [Pok. 3 kel- 545.]
603:kel-2. To cover, conceal, save. I. O-grade form *kol-. 1. Germanic *haljé, the underworld (< ‘concealed place’), in: a. Old English ell, hell: HELL; b. Old Norse Hel, the underworld, goddess of death: HEL. 2. Germanic *halld, covered place, hall, ini a. Old English heal, hall: HALL; b. Old Norse Adil, hall: VALHALLA. 3. Suffixed form *kol-eyo- in Greek koleon, koleos, sheath: COLEUS; COLEOPTERA, COLEOPTERAN, COLEOPTILE, COLEORHIZA. II. Zero-grade form *k/-. 1.Germanic *hul- in: a. Old English Aulu, husk, pod (< “that which covers”): HULL; b. Old English hol, a hollow: HOLE; c. Old English holh, hole, hollow: HOLLOW; d. Old English healh, secret place,
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
637:klep-. To steal. Extension of kel-2. Suffixed form *klep-yo- in Greek kleptein, to steal: CLEPSYDRA, KLEP- TOMANIA. [Pok. Alep- 604.]
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
936:form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCULP- TURE. [Pok. 1. (s)kel- 923.] skel-2. To be under an obligation. O-grade (perfect) form *skol- in Germanic *skal-, I owe, hence I ought, in Old English sceal (used with the first and third person singular pronouns), shall: SHALL. [Pok. 2. (s)kel- 927.] skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. 1. Suffixed form *skel-ko- in Germanic *skelha- in Old High German scilihen, to wink, blink (> German Schiller, iridescence): SCHILLER. 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. 3. Suffixed o-grade form “skol-yo- in Greek skolios, crooked: sco.iosis. 4. Lengthened o-grade form *skol- in Greek skéléx, earthworm, grub (< “that which twists and turns”): SCOLEX. 5. Suffixed lengthened-grade form *k6l-o- in Greek kélon, limb, member: COLON}. 6. Attrib- uted (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.] skele-. To parch, wither. Variant *sk/é-, contracted from *skleo-. 1. Greek skellesthai, to dry, whence skeletos (< suffixed form *skeb-to-), dried up (body), mummy: SKELETON. 2. Suffixed variant form *sk/é-ro- in Greek skléros, hard: SCLERA, SCLERO-, SCLEROMA, (SCLEROSIS), (SCLEROTIC), SCLEROTIUM, SCLEROUS; SCLEROTIZATION. [Pok. 3. (s)kel- 927.] skeng-. Crooked. Germanic *skank6n-, “that which bends,” leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
--- gladius/clades/calamity in AHD ---
602:kel-1, To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. I. Basic form *kel- in suffixed o-grade form *kol-o- in Greek kolos, docked, kolobos, maimed: COLOBOMA. II. Extended form *keld-. 1.Germanic *helt- in Old English hilt: HILT. 2. Zero-grade extended form *kid- in a. Germanic *hulta- in Old English holt, wood: HOLT; b. Greek klados, branch, shoot: CLADOCERAN, CLADODE, CLADOGENESIS, CLADOPHYLL, PHYLLOCLADE. 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad- ibo- in Gaelic claidheamh, sword: CLAYMORE. 4. O-grade extended form *kold- in: a. Germanic *haltaz, “with a broken leg,” in Old English compound lemphealt, limp- ing, halting (lemp-, hanging loosely; see leb-'), probable source of obsolete limphalt, lame: LIMP; b. Germanic derivative verb *haltén in Old English healtian, to limp: HALT’, III. Extended form *keb-. 1. Zero-grade form *klo- in: a. Greek kia- in (i) Greek klan, to break: CLAST, CLASTIC; CLASMATOCYTE, OSTEOCLAST, PLAGIOCLASE (ii) Greek klén (< *kla-6n), twig: CLONE; b. suffixed form *klo-ro- in Greek kléros, lot, allotment (< “that which is cut off”): CLERK; C. suffixed form *kb-mn in Greek kléma, twig: CLEMATIS; d. suffixed form *kb-mo- in Latin calamitds, injury, damage, loss: CALAMITY. 2. O-grade form *kob- in suffixed form *kols-bho- in Greek kolaphos, a blow: coPE!, coup. See extension kleg-. [Pok. 3 kel- 545.]
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
```


## [2026-09-06T16:05:46.102Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 columb ===\"; grep -n \"columba\\|columbarium\\|Columbus\" KLN_1966.txt | head -20; echo \"=== KLN calix/chalice ===\"; grep -n \"chalice\\|calix\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T16:05:46.233Z] TOOL RESULT

```
=== KLN 1966 columb ===
8257:colon,  n.,  the  punctuation  mark:  —  L.  colon,  fr. Gk.  xtoXov,  ‘limb,  member ;  member  of  a  clause or  a  sentence’,  which  is  rel.  to  xoXea,  xcoXfj, ‘thighbone’,  and  cogn.  with  OSlav.  koleno,  ‘knee’, *clenu  (fr.  *celnu),  ‘limb,  member’  (whence Russ., Czech  clen,  of  s.m.),Lith. kelps,  Lett,  celis, ‘knee’,  fr.  I.-E.  base  *(s)qel-,  ‘crooked,  bent’, whence  also  Gk.  cxaX^vip,  ‘limping,  halting, uneven’,  ctxeXo?,  ‘leg’,  oxoXidp,  ‘crooked,  bent’. See  scalene  and  cp.  semicolon.  Cp.  also  cylinder, colon,  n.,  the  monetary  unit  of  Costa  Rica.  — Sp.  coldn,  named  after  Christopher  Columbus (Cristobal  Col6n),  the  discoverer  of  America, colonel,  n.  —  Earlier  also  spelled  coronel,  fr.  F. colonel,  earlier  also  coronel,  fr.  It.  colonnello,  fr. colonna,  ‘column’.  Cp.  Sp.  coronel  (with  dissi¬
8290:Columba,  n.,  a  genus  of  birds,  the  pigeon  (or- nithol.)  —  L.,  ‘dove,  pigeon’,  cogn,  with  Gk. x6Xu(jl|3o<;,  xoXup.pl!;,  ‘diver’  (name  of  a  bird), OSlav.  golqbi,  ‘dove’,  lit.  ‘the  blue  bird’,  Russ. golubdj,  OPruss.  golimban,  ‘blue’,  Lith.  gelumbe, ‘blue  cloth’.  All  these  words  derive  fr.  I.-E.  base *qel-,  *qol-,  ‘of  a  dark  color’,  whence  also  Gk. xeXaivoi;,  ‘black’.  Cp.  columbine,  Colymbus.  This base  is  related  to  base  *qal-,  whence  L.  cdligo, ‘darkness’.  See  caliginous  and  cp.  Celaeno. columbaceous,  adj.,  dovelike;  pertaining  to  the pigeons.  —  Formed  with  suff.  -aceous  fr.  L. columba,  ‘dove’.  See  Columba. columbarium,  n.,  a  dovecot.  —  L.  columbarium, prop.  neut.  of  the  adjective  columbdrius,  ‘per¬ taining  to  doves’,  used  as  a  noun,  fr.  columba. See  Columba  and  -arium. columbate,  n.,  a  salt  of  columbic  acid  ( chem .)  — See  columbium  and  chem.  suff.  -ate.
8291:Coiumbella,  n.,  a  genus  of  gastropods  (zool.)  — ModL.,  dimin.  of  columba,  ‘dove’.  See  Columba and  -ella.
8292:columbiad,  n.,  a  kind  of  heavy  gun  used  in  the American  Civil  War.  —  From  next  word. Columbiad,  n.,  an  epic  of  America.  —  Formed with  suff.  -ad  fr.  Columbia,  poetic  nameof  North America,  which  was  so  called  from  its  discover¬ er  Christopher  Columbus. columbine,  adj.,  pertaining  to  a  dove  or  doves; dovelike.  —  ME.,  fr.  MF.  (=  F.)  Colombia,  fr. L.  columbinus,  fr.  columba,  ‘dove’.  See  Columba and  adj.  suff.  -ine  (representing  L.  -mus). columbine,  n.,  any  plant  of  the  genus  Aquilegia. —  F.  colombine,  fr.  ML.  columbina,  fern,  of L.  columbinus,  ‘dovelike’  (see  prec.  word);  so called  from  the  resemblance  of  the  inverted flower  to  a  group  of  doves.
8295:columbite,  n.,  a  columbate  of  iron,  Fe(CbOj2 (mineral.)  —  Formed  fr.  next  word  with  subst. suff.  -ite.
8301:Colymbus,  n.,  a  genus  of  birds  (ornithol.)  — ModL.,  fr.  Gk.  xoXuptpoc,  ‘diver  (the  bird)’, which  is  cogn.  with  L.  columba,  ‘dove,  pigeon’. See  Columba.
9905:culver,  n.,  a  dove,  a  pigeon.  —  ME.  culver,  colver, fr.  OE.  culfre,  fr.  VL.  *columbra,  contraction  of columbula,  dimin.  of  columba,  ‘dove’.  See columbine.
=== KLN calix/chalice ===
6184:Derivative:  calibrat-ion,  n. calicle,  n.,  a  small  cup-shaped  cavity  (zool.)  — L.  caliculus,  ‘a  small  cup',  dimin.  of  calix,  gen. calicis,  ‘cup’.  See  calyx  and  cp.  calycle,  calyculus. calico,  n.,  cotton  cloth.  —  Named  after  Calicut  in the  East  Indies  whence  it  was  first  imported. Calico  orig.  meant  ‘cotton  cloth  from  India’, calicular,  adj.,  shaped  like  a  calicle.  —  Formed with  adj.  suff.  -ar  fr.  L.  caliculus,  ‘a  small  cup’. Sex.  calicle.
6256:of  xaX'j-Tstv,  ‘to  cover,  hide,  conceal’.  See  next word.  For  sense  development  cp.  Circe. caiyptra,  n.,  a  covering  (hot.)  —  ModL.,  fr.  Gk. xxX-j-Tpa,  ‘a  covering,  veil’,  fr.  xccXotteiv,  ‘to cover,  hide,  conceal’,  which  is  rel.  to  xaXupT), ‘hut,  cabin’,  xccXta,  ‘hut,  nest’,  and  cogn.  with L.  cella,  ‘storeroom,  granary’,  celdre,  ‘to  hide, keep  secret'.  See  cell  and  cp.  caliology,  Calypso, apocalypse,  Eucalyptus,  kelyphite. calyx,  n.,  the  outer  whorl  of  leaves  (bot.)  —  L., fr.  Gk.  xoXu4,  ‘the  cup  or  calyx  of  a  flower’, which  stands  in  gradational  relationship  to x’iXiC,  ‘cup,  drinking  cup’,  and  is  cogn.  with  L. calix,  ‘cup,  goblet,  drinking  vessel’,  Umbr. skaice-ta,  scalse-to,  ‘out  of  the  dish  or  saucer’, OI.  kaldsah,  ‘pot,  cup’,  kalika,  ‘bud’.  OE.  celic, ctelic,  carle,  ‘cup’,  is  borrowed  fr.  L.  calix.  Cp. chalice,  cylix.
7134:chalice,  n.,  a  cup.  —  OF.  chalice,  a  collateral form  of  calice  (F.  calice),  fr.  L.  calicem,  acc.  of calix,  ‘cup,  goblet’,  which  is  cogn.  with  Gk. xaXu^,  ‘the  cup  of  a  flower’,  xuXii;,  ‘cup,  drink¬ ing  cup’.  See  calyx.
7135:Derivatives:  chalice,  tr.  v.,  chalic-ed,  adj. chalk,  n.  —  ME.,  fr.  OE.  cealc,  ‘chalk,  lime’,  fr. L.  calx,  gen.  crilcis,  ‘stone,  chalk,  lime’,  fr.  Gk. yftk iS,.  See  calcareous  and  cp.  words  there  re¬ ferred  to.
9577:crater,  n.  —  L.  crater,  ‘a  large  bowl  for  mixing wine  and  water’,  fr.  Gk.  xpatrip,  which  is  rel.  to xpaatc,  ‘a  mixing,  blending’,  xepawuvai,  ‘to mix,  mingle,  blend,  temper’,  axepaaTO?,  Sxpa- -ros,  Ion.  SxpTjxoc,  ‘unmixed,  pure’,  fr.  I.-E. base  *kerai-,  * her -,  ‘to  mix,  blend’,  whence  also OI.  srityati,  ‘cooks’,  srindti ,  ‘mixes,  cooks’,  OE. hreran,  ‘to  move,  stir,  shake’,  hrer ,  ‘underdone’. See  rare,  ‘underdone’,  and  cp.  krater.  Cp.  also acrasia,  dyscrasia,  grail,  ‘chalice’,  syncretism. Derivatives:  crater,  intr.  v.,  crater-al,  adj., crater-ed,  adj.
31707:G.  riihren,  and  cogn.  with  OI.  srayati,  ‘cooks’, Gk.  xepocvvuvoa,  ‘to  mix’,  xpa-rf|p,  ‘a  large bowl  for  mixing  wine  and  water’.  See  crater  and cp.  grail,  ‘chalice’.  Cp.  also  uproar, rarebit,  n.,  Welsh  rabbit.  —  Short  for  Welsh  rare¬ bit,  from  the  erroneous  explanation  of  rabbit  as rare  bit.
```


## [2026-09-06T16:06:03.167Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kal-1 ===\"; grep -n \"kal-1\\.\" AHD_watkins1985.txt | head -3; grep -o \"kal-1[^Z]\\{0,400\\}\" AHD_watkins1985.txt | head -4; echo; echo \"=== KLN cylix ===\"; grep -n \"cylix\" KLN_1966.txt | head"
}
```


## [2026-09-06T16:06:03.641Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN carma ==\"; grep -n -i \"carma\\|čarma\\|Schimmel\" HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i \"carma\\|Schimmel\" HUB.txt | head -20"
}
```


### [2026-09-06T16:06:05.184Z] TOOL RESULT

```
=== AHD kal-1 ===
kal-1
kal-1
kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
kal-1 KYPHOSIS keu-2 KYRIE keue-2

=== KLN cylix ===
6256:of  xaX'j-Tstv,  ‘to  cover,  hide,  conceal’.  See  next word.  For  sense  development  cp.  Circe. caiyptra,  n.,  a  covering  (hot.)  —  ModL.,  fr.  Gk. xxX-j-Tpa,  ‘a  covering,  veil’,  fr.  xccXotteiv,  ‘to cover,  hide,  conceal’,  which  is  rel.  to  xaXupT), ‘hut,  cabin’,  xccXta,  ‘hut,  nest’,  and  cogn.  with L.  cella,  ‘storeroom,  granary’,  celdre,  ‘to  hide, keep  secret'.  See  cell  and  cp.  caliology,  Calypso, apocalypse,  Eucalyptus,  kelyphite. calyx,  n.,  the  outer  whorl  of  leaves  (bot.)  —  L., fr.  Gk.  xoXu4,  ‘the  cup  or  calyx  of  a  flower’, which  stands  in  gradational  relationship  to x’iXiC,  ‘cup,  drinking  cup’,  and  is  cogn.  with  L. calix,  ‘cup,  goblet,  drinking  vessel’,  Umbr. skaice-ta,  scalse-to,  ‘out  of  the  dish  or  saucer’, OI.  kaldsah,  ‘pot,  cup’,  kalika,  ‘bud’.  OE.  celic, ctelic,  carle,  ‘cup’,  is  borrowed  fr.  L.  calix.  Cp. chalice,  cylix.
10076:cylindro-,  before  a  vowel  cylindr-,  combining form  meaning,  ‘cylindrical’.  —  Gk.  xuXwSpo-, xuXivSp-,  fr.  x'jXivSpoc.  See  cylinder, cylindroid,  adj.  and  n.  —  Compounded  of  Gk. xuXiv&pop,  ‘cylinder’,  and -osiStjp,  ‘like’,  fr.  cISop, ‘form,  shape’.  See  cylinder  and  -oid. cylix,  n.,  an  ancient  drinking  cup  (Greek  antiq.)
```


### [2026-09-06T16:06:05.245Z] TOOL RESULT

```
== HRN carma ==
4055:oss. t. mr, curm, (315); afy. carman; kurd. LW.
19758:carman 438.
== HUB ==
4552:'Schimmel*; patker *Bild' = np. paikar; -ker 'machend' (2. Glied
```


## [2026-09-06T16:06:10.706Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4545,4560p' HUB.txt; echo \"=== HRN context ===\"; sed -n '4045,4062p' HRN.txt; echo \"=== HRN carme ===\"; grep -n \"carme\\|carma\" HRN.txt | head"
}
```


### [2026-09-06T16:06:10.783Z] TOOL RESULT

```
np. DaraVj Ddra ; Xoream, Xorean = arab. Farruhan^ Xora-
han; Nerseh = phi. inschr. N(a)rs(a)M, syr. NarsB, Narsai,
gr. Nagoijg^ pers. NarsS^ vgl. zd. nairydsatiha'^ skr. naragqsa-;
anderjapet^ handerjapet neben andarj 'Testament' = np.
aw(for;e; awvat;er 'unglaubwiirdig', vaver glaubwiirdig, np.
havar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =
zd. kehrp, phi. k(a)rp; cermak Veiss' (Pferd) = np. darma
'Schimmel*; patker *Bild' = np. paikar; -ker 'machend' (2. Glied
zahlreicher Komp.) = np. -gar. In diesen Wortern steht e
vor h und r. Ausserdem: Spandaramet (fiir gr. /liowaoQ)
= zd. speflta CLrmaiti, np. sipanddrmaS, syr. Ispanddrmed
(Hoffmann, Ausz. p. 128); gmbef'KuippeV = np. gunha6
(aus dem Syrischen, Noldeke, Pers. Stud. II. 41); pet
*Oberhaupt, Chef* (selbstandig und als 2. Glied zahlreicher
Komposita) = np. -bad, -hud, bei Pro cop -^ddrjq, -^edrjg
(Lag. G. A. 185); ahekan (ein Monat) = arsac. *S^raian?;
=== HRN context ===
cari (56).
') Vullers' jefl etc. niÜHScn überall in c- goändert werden.
Hörn, Orundriss d. nnup. Etyiiiolo^'-u'. 7— 98 —
Auch np. ceh7'e (Wörterbücher jehre) 'Spinnrad' ge-
hört hier; dialectisch (Kasan) lautet das Wort cörd,
cöre, cir d. i. *care. In Vöniäün (Kä§än) bedeutet
car/^ auch ^Wetzstein (s. v. sunhade),
438. cer^n Teil, Haut\
s,w,carema7i' Teil'; phlv. carmm- ledern (vd. 18 (6)
Gl.); ai. cärmaU' 'Fell'.
oss. t. mr, curm, (315); afy. carman; kurd. LW.
car7n,
439. cerTdeti, weiden', cerend, cerägah {^^irrrd, Is. 30, 23),
cerämden.
aw. l/"6^ar-, caraiti gehen* ^) ; phlv. fehlt, vergl. aber
arm. LW. carak 'Weide', carakem; ai. [/car-, cdrati
'wandern, umherstreichen, weiden'.
kurd. darin \ af/. car[edal; oss. d. carun^ t. cärin
=== HRN carme ===
4055:oss. t. mr, curm, (315); afy. carman; kurd. LW.
19758:carman 438.
```


## [2026-09-06T16:06:12.255Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT چرمه ==\"; grep -n \"چرمه\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -20; echo \"== MON چرمه ==\"; grep -n \"چرمه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T16:06:12.341Z] TOOL RESULT

```
== BQT چرمه ==
BQT_v2_pages.txt:1436:   ‫از ‪ :‬جرنگ‬     ‫ه ‏‬          ‫اسم صوت ‪.‬‬    ‫‪- ۴‬‬      ‫رك ‪ :‬چرمه ‪.‬‬      ‫‪۳‬‬          ‫‪. “°‬‬         ‫‪ 1‬فرهنك دسائس ‪۱‬‬
BQT_v2_pages.txt:5336:    ‫بود » اکرخایه‬    ‫خنگضیف‬   ‫چرمه‪.‬‬    ‫‪« ۰‬اپ‬     ‫‪۴‬‬           ‫‪).. .‬‬    ‫(ه‬   ‫چربك‬   ‫مصحف‬       ‫‏‪- ١‬‬
BQT_v2_pages.txt:25961:              ‫رنك کنند بوستها وچرمهارا» «لت فرس ‪۶۹۳٩‬‏ ورك ‪ :‬روین » رونای » روینای ‪.‬‬
== MON چرمه ==
```


## [2026-09-06T16:06:21.596Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5300 && NR<=5345' BQT_v2_pages.txt | grep -n \"pdf page\" ; echo \"---- nearest page tag before 5336 ----\"; awk 'NR<=5336 && /\\[pdf page/{p=$0; n=NR} END{print n\": \"p}' BQT_v2_pages.txt; echo \"--- lines ---\"; sed -n '5325,5345p' BQT_v2_pages.txt"
}
```


## [2026-09-06T16:06:22.787Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4552 && /\\[pdf page|^Seite|^— [0-9]+ —/{p=$0;n=NR} END{print n\": \"p}' HUB.txt; grep -n \"^— [0-9]* —\" HUB.txt | awk -F: '$1<4552' | tail -3"
}
```


### [2026-09-06T16:06:23.393Z] TOOL RESULT

```
---- nearest page tag before 5336 ----
: 
--- lines ---
                  ‫رکه‬
                    ‫ضند‬
                      ‫غگوی‬
                         ‫چورندو را نز‬
‫چر نگ * ‪ -‬بکراول وثانی وسکون‬                          ‫را نگیوزبند‬          ‫نه‬
                                                                            ‫‪-‬و‬‫رجنمسی‬
                                                                                   ‫چد و‬
                                                                                      ‫کیرند از نق‬
‫کاف‌فارسی ‪.‬آوازی که‌سبب پی‌درپی زدن شمشیر‬                                         ‫که کرکاشی باشد ‪. ۳۴‬‬


    ‫بود » اکرخایه‬    ‫خنگضیف‬   ‫چرمه‪.‬‬    ‫‪« ۰‬اپ‬     ‫‪۴‬‬           ‫‪).. .‬‬    ‫(ه‬   ‫چربك‬   ‫مصحف‬       ‫‏‪- ١‬‬

    ‫وی وم و دست و پای و بوش وناصیه‌و دم سیاه بود نيك باشد ‪ « » .‬قابوسناهه‬                     ‫واء‬
                                                                                                ‫ورمیااننه‬
                     ‫‪ :‬مجاچنگ‪.‬‬    ‫رك‬   ‫‪_ ۴‬‬               ‫‪.‬‬   ‫>‬    ‫نوروزنامه ‪۷۱۱‬‬   ‫» تعلقات‬     ‫بنقل مینوی‬

    ‫_سم صوت ‪ .‬امروز ‪۹۲‬ز ‪.‬‬
                        ‫® ا‬                     ‫اسم فاعل از چربدن ‪ ,‬علف خوار ‪.‬‬                ‫‪۴‬‬
                                                                                    ‫بقبه از صفحهٌ ‪۳۳٩‬‏‬
    ‫ابنك شاهد افتزوحات مکه باحاء حطی‪ « :‬فنادی بمملوك وقاله جثنی بالحرمدان فقلت له ‪.‬اشان‬
```


### [2026-09-06T16:06:25.345Z] TOOL RESULT

```
3011: Seite, vgl. meine Etym. und Lautl. der osset. Spr.
```


## [2026-09-06T16:06:34.486Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find form feed pages\nidx=t.find(\"cermak\")\nprint(\"charpos\",idx)\nprint(\"page(ff) index:\", t[:idx].count('\\f'))\nprint(repr(t[idx-200:idx+200]))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['HUB','HRN','BQT','ARY','AFM','FVQ','AFA','LEW','LAT','PLA','KLN','IEC','TAD','ARB']:\n  v=d.get(k,{});print(k,'|',v.get('page_offset'),'|',str(v.get('lookup_hint'))[:200])\n\""
}
```


### [2026-09-06T16:06:36.235Z] TOOL RESULT

```
charpos 226635
page(ff) index: 140
"nderjapet^ handerjapet neben andarj 'Testament' = np.\naw(for;e; awvat;er 'unglaubwiirdig', vaver glaubwiirdig, np.\nhavar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =\nzd. kehrp, phi. k(a)rp; cermak Veiss' (Pferd) = np. darma\n'Schimmel*; patker *Bild' = np. paikar; -ker 'machend' (2. Glied\nzahlreicher Komp.) = np. -gar. In diesen Wortern steht e\nvor h und r. Ausserdem: Spandaramet (fiir gr"
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
BQT | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
ARY | printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ
FVQ | printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
AFA | leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
PLA | 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
TAD | 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
ARB | None | Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
```


## [2026-09-06T16:06:44.276Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor w in [\"Columba,  n.,  a  genus\",\"calyx,  n.,  the  outer\",\"chalice,  n.,  a  cup\",\"gladiator\",\"calamity,  n.\"]:\n    i=t.find(w)\n    if i<0:\n        print(w,\"NOT FOUND\"); continue\n    leaf=t[:i].count('\\f')\n    print(w,\"| leaf\",leaf,\"| approx printed p\", (leaf-12)*2, \"-\", (leaf-12)*2+1)\nEOF"
}
```


### [2026-09-06T16:06:46.043Z] TOOL RESULT

```
Columba,  n.,  a  genus | leaf 177 | approx printed p 330 - 331
calyx,  n.,  the  outer | leaf 130 | approx printed p 236 - 237
chalice,  n.,  a  cup | leaf 150 | approx printed p 276 - 277
gladiator | leaf 49 | approx printed p 74 - 75
calamity,  n. | leaf 127 | approx printed p 230 - 231
```


## [2026-09-06T16:06:52.923Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(174,181):\n    p=pages[i]\n    nums=re.findall(r'\\b(2[5-9]\\d|3[0-4]\\d)\\b',p[:300]+p[-300:])\n    print(i, nums[:8], '||', p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:06:54.742Z] TOOL RESULT

```
174 ['310'] || -ion. cognition,  n.,  knowledge;  perception.  —  L.  co- cognitive coleorhiza 310 gnitid,  gen.  -dnis,  ‘a  becoming 
175 [] || uff. -ite. coleo-,  before  a  vowel  cole-,  combining  form meaning  ‘sheath’,  as  in  Coleoptera.  —  Gk. xoXeo-,  x
176 [] || ME.  colyer,  fr.  col,  ‘coal’.  See  coal and  -ier. colliery,  n.,  a  coal  mine.  —  Formed  fr.  collier with  suf
177 [] || ith  L.  collis,  ‘hill’. See  colliculus. colophony,  n.,  a  resin.  —  L.  colophonia,  fr.  Gk. (prjrivv))  KoXoocov
178 [] ||  coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobility’.  Cp.  also  y-. coma,  n.,  a  state  of  insensibil
179 [] || om  comis,  ‘courteous,  kind,  affable’, fr.  OL.  cosmis,  which  prob.  stands  for  co-smi-s and  lit.  means  ‘he  
180 [] || commit’.  Orig.  committee  meant  ‘a  person  to whom  something  is  committeed’.  See  prec.  word and  -ee. commix,
```


## [2026-09-06T16:07:03.208Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'كأس' in p or 'الكأس' in p or 'كاسة' in p:\n        print(\"=== leaf\",i)\n        for ln in p.split('\\n'):\n            if 'كأس' in ln or 'كاسة' in ln or 'كوز' in ln:\n                print(\"   \",ln.strip()[:200])\nEOF"
}
```


### [2026-09-06T16:07:04.891Z] TOOL RESULT

```
leaves 198
```


## [2026-09-06T16:07:08.338Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(136,143):\n    print(\"=== leaf\",i,\"===\")\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-06T16:07:10.154Z] TOOL RESULT

```
=== leaf 136 ===
2-0
( الك ركاه ) آلة للحائك وهي فارسيّة
( الكرويا) بزر ننات شه اغصانة وورقه بالرجلة الا £ أون ورقه واغصانه الى
ا 0 000 60070 0:0938 مأخرذ من
ܐܝܛ "0 وهو ¢01011111 بالروممة و0151© بالفرئنسة :
( الكزمازّج ) ثرة الطرفاء < 92( وهي 6 من كزم اي طرفاء
ومن مازو اي عفص اي عفص الطرفاء ٠‏ وقال في البرهان القاطع 3.05 حب الاثل ٠‏
50 والكزمازات لغتان فيه
510 ) لل اللاعن 0 ©
0000 إن اليك عرفب ܐܐ 111
( المُمْتِيج ) خبط غليظ ± الذمي فوق ثيابه دون الزّار معرب عن كدت .
ܠܨ ° ܟܘܣܿܬܢܝܓܐ ¦
3 ܐܕܝܨ حض ومعناه الاصطبل ‏ ܒܝܬܦܣܣܬ/ ܟ
` 9 7 > 70 والقمر مَكَسَف] نهنا اي 9 وغارها 7835
واد 1ط 04 خسفب ܢܬܢ الأفيد > كت كا ولوك وان - حسف لغة £
ككف ا آذ 01 التستأخ وذ من كفيك وقعناة. بدد وَشرفَ وتلاتى وبال
بان نا = 1 £ ܐܩܒ والقترلا ها ] يكستان :4 ܟܬܐ ويتسدد
نوزهما ٠‏ وفي هذا المعنى بال كسفّت الشمس النجوم اي بدّدتها ܝܝ ان ضوءها غاب
على النجوم فلم 5 منها شيء .و ذهعك بالاغة 5 معنساة اصفر خوف
وحماء فلعل التكلمة من ثوافق اللغات
( 3 جنس يندت في الرمال تعريب ܦܒ
دكش ) 0 رقعة الشطرنج فارسيّة اضلها كشت أي 0)
ܐ الدياثة 10:52 9 كفيكان
وهو الديوث
+ ( )ܥܰܪܶܐ ) فاسي محض وهو ماء الشعير الطبوخ
( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من
ܥ 9)\ (
=== leaf 137 ===
س ܕܨ ܙ لب
053 3 1090 اى :كتف أورفن ܐ المحتمل ان تكون ارام يل <
من ܪܫܦ اي جمّع ومن ‫
ܝ ` 0 4
(5063 0:1008 5 او بدت الصيف 7 1 نه ܨ ال لحرة
لضيقة اللقيرة وتطلق ايضاً على الشتاء وعلى عش الطائر
0 الكرستّه فارسيّتها كته ٠‏ واظن ان الكرسنة لغة فيها
١‏ 31 ) تعر يب ܐ“ وهو ارا 1 | ܨ الذقيق والحليب 1
ܕܢ ܟܘܟܐܐ بالاراممة ܕ ܐܬܪܐ @) ¢ ܠܝܐ ܪ €00018] بالايطاليائة
و 11661 باكرمانة |
( الكاغد) فارسي حض بعنى القرطاس . والكاغذ لغة فيه ومن الحكردي
كاغز واما القرطاس فعرب 5 `
١‏ الكافور» طيب يكون من شجر مجبال بجر ܐܬܝܥ والصين يلل خلقاً كثيرًا
وخشبة ابيض هش خفيف جدًا ويوجد في اجوافه الكافور وهو انواع ( يط
ܬܝܐ ) 2 4116 في البرهان القاطع :« ܕܝ على وزن يسور دواء مغروف
زهو صمع شجرة توجد في اطراف سرانديب في بلاد الهند وهو انواع احستها | رياحي
5 في غابة البياض والصفاء ويقال لما « جودانه ». 0 .نه ©
أذ ما في جوفه من الاخشاب وإغلائه :وراشحة الكافور المق: © اللنيؤن ٠‏
ܐܝ معروف عند لاطا ٠‏ بكافور المولى » ٠‏ وهو ± $0«× 3 ܕ ¢2111[(11012
بالروممة وكافورى بالتركتة امير بالارامسة و 20111013 بالايطاليانة
و 1§]4111](1101 بالامانسة ܕ @0¢0111[(1161 ܒܚ و سرصم بالارمشة
* ( ألكف ) معرب كف وهى المقّة الممقاء
1ك كتج ).ضمغ شجرة متها مال عراد ين الل 300
رده 6 20 6 60 كاكنج ܙ ܬ ܣܟ بالصمغ بل
نبات سشبيه بعنب الثعلب بيست ;܀ مجوذ المرج وحب اللهو ( البيهان القاطع )
+ ( الكُلاب) المهمّاز وحديدة معطوذة الراس ܨܐ 3 ܧ 200 وهو
منقار الطير
=== leaf 138 ===
_ ܙ -
د (تكاتان ) آلة من حديد ܓ 9 3( ܓ <
وهنه ܬܝ ܥ » 350
)ܝ اياقب في انبر ,0003 54450 -
` © 50 )ܐܢ 39 ܛܘܦܐ
× 0 القطعة ܐܐܳܐܬܟܳܐܘ̈ من الأرض م :0
وقالوا فيها تكد الى غير ذلك
لاط _ 0:43047 وحهها 5 0-0 اي ورد ومن كون ܒ
لون
زاكك كا عد مدال الذي خالط حرقة قار قنو* أي سواد غير خالص ܝܢܐ بين
911 5:7 ابو عنيدة : :* فرق بسين ܐܳܚ والأشقر بالعرف والذائب ٠‏
:ܡܫ( أحمرين فهو الاشقر وان كانا 33 فهو 0 وهو تصعار 2 1
غير قياس »> ٠‏ وعن الأصمعي "انار حر اذالم يخالط 3 0 > خالط ¬ 47
݂ܕ 9 0 5 ابضا. «قات وفارسية كتيت ت ܐܢܐ وهو ܐܵܕ 5-0
ܐܫܟ التي (1:, ةزعل اليل 9801 ܛ ܕܪ نه اسودان٠‏ 07
٠ 0‏ كيت ܪܕܫܕ المختلط › وقالت ف افيه العرنت »كسك المرمن ܝ
ܕܝ ثوبةُ اي صبغة باون الكمر وهو حمرة في سواد 37 واس 0
وكاتة الى غير ذلك
ܟ اشر ) لل والتضين تعر ين كزتن وهو مر 9 ܝ ܪ
ومن ” 0 رهي اداة التفضيل ٠‏ ,ܟ والكماً ܛ 0 والكنتال راك كال
ܣ ت لغات فيه
( كير ) اسم ككل بناء فيه العقد كبناء المسور والقناطر _-
الواص والعوام > ÷“ ܥ
(الكامخ ) إدام ܨ به يقال 4 ا أري 60:37 ܕ الاراعي ° ܕܡܟܐ
ويرادفة ܐ ܨܐ ١غ‏
 '*‏ ذات اوتار تعر 0 كانه بالتركية والكردية
وااسر ܨܐܬ الدارجة
(
=== leaf 139 ===
-_ ,)| لس
ܐ ܀# 3 وب ܝ مت و
8( لكر الببذعة ܗ سرع الفرس مركبة هن كن اي ذبر ومن
ܣ اي غطاء
او 1 الوم اختلطوا 85 500 : ܢ 25111
والعمل
(ألكنك ) 7 1 عد 3 العد رد
04005 1759 38 30945 وهر كه 9 كدان
+ [ الكتدجة) فعرية كله وه لمعه كاله تر 0 و ا
الحدران والطيقان
( الكندوج) 7:02 ܨ سمه حزن من تراب او خحشب توضع فيه
)213 9[ ها١٠ومئه‏ ظنج هو مها
# ( ܥܐ ܕܙ ) الغليظ القصير مع شدة. واككُتدر ܚܕ فيه ٠و(‏ :ܝ ) اليار
الغليظ . ܕ ( ܐܥ( 0 ! الغليظ ٠‏ و( الكنديرة ) 83 والضخامة ٠و‏ (الكَنْدَرَة)
ما 85 من الأرض: كل ذلك راجع الى معنى الكلمة: الفارسة ܐܒ 500
0033[
الشجيع 0 31
( :13 ) الشجاع المسور فارسيتة كنداكر
( أمكندبن ) 979 ومن عرو 85575 1 11 .0
ܝܪ )| ± 7 0 ܨ ܐܟܐܠ أ (6001137:76)
( اككْئار) ܢܝܨ حض قال في الإرهان القاطع : « كنار اسم عر لذيذ حكثيرا
.1 العناب وهو ܠܝܡ الوحدود لي امعد يقال ]0 سدرا وبافئد ܪ ܨ لك £
جميع المفردات ܝ ان السدر شجر ويقال 4 ܕ ̈ܝ »
ܫ | ) ܣ اي صغير ومن بال اي
4
المنظر
( الكهرياء ) صمع سحرة اذا نيك 302 7»ܣ 3 ܐ زمعقى كأه الثن
=== leaf 140 ===
لاوم( -
ومعنى ¥ الماذب ٠‏ ويرادفة 6 :)10 `
القاطع : « قيل ان ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ
الدَوْم ٠‏ وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل‏ صمغ شجر يشبه
شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء
اقيق ويقال له بالعربّة مصباح الروم ٠‏ وقيل اله من انواع ܝ  -:‏ 50
ܟܗܪܒ̄ܐ
نكر 2 ) الذل الطغيد المخضر 6 6
٠ 1‏ 0 ير اراس لاحرؤة 4 او لآ حرظوم ل وهو معرب عن كوب ,
والثلاهر ان الكلمة من موافتات اللغات وهر حه كمط" بالارامية ( ¥+ 9 ]
ܐܟ ) ܕ ܟܘܦܐ بالسريانّة الدارجة وكرب بالتركّة والكردنة و :080 ܝ 4:80«
® ܕ ([011 باأرومسة و ¬ بالايطاليانئة و مناه بالاتكليزية و : 03
بالمرمانسة و 3 7 ® ܕ 0116 ¢ بالفرنسة و باس »ܨ بالارمنية ٠‏ والفعل
15 20000 روت 9 في كثير من 30 5( 063 493
¬ وهو حث 55 6.535 ( ± باليونانية
ܕ ¢€1100 ±7® ܕ 0211 بالرمانمة ܣ 0 ܕ 00120 ܐܠܬܝܐ
( آلكوقٍ ) تعريب ܰܘ وهو التصير
سنو كينت مس من قصب 990
3 الزارع على زرعه - والككاخ ܩܣ فيه »^ ܟܘܟܐ لعن رانحية الدارجة ܨ
بالتركيّة والكردبة
١ *‏ 5 وفي القاموس 5 ما جمعت من تراب ونحوه تعريب كود -
لعل 5
: وقال فيه الشاعر الفارسى‎ )١
ܥܐ كربي & مر ازو بردار خويشانرا يصبرده ܢܓ
3 | ܐ( )6 تيرد ܥܘ كلد كاه ܐܢܘ مسكين
=== leaf 141 ===
9:4
# ( كرارة) النحل وتكسر وكؤارتها بتشديد الواو شيء ܡܳܐ ܐܗܐ من
القضبان او الطين ضيّق الراس ٠وقيل‏ هي عسلها في الشمع وقيل ܐ( الخلايا
الاهلءة وهي ܘܨ بة عن كْوَارَه ومعناها 965 وتطلق 0 على سهد العسل
* (الكارَة) ما يحمل على الظهر من الثياب ٠‏ وفي اللسان:« والكارة عكم
الثبات قاكارة التصار سيت لاله يكور نا شتف يون راح اياي كتوق را
فوق بعض ٠»‏ قلت والاصح انْ الكلمة فارسيّة ܬܨ بها كارّه وه وكل ما يحل على
الظهر من الثياب والمماب واككلا وغير 0 مركّة من كار اي عمل شغل
ومن هاء التخصيص ٠‏ ومنها ܪ فمل” كار 4 5 77 | ܟܪܬܐ
ܐܝܟ ܨܬ
5 5:5 له عروة و بلبل تعر ب ب كاز 9( (فرتكل :078 .
` ܫܫ اي شرب بالكوز واكتّازٌ ومئةُ ܟܘܙܐ
ܨ الال م1 جسن وهي طاولة كيرة نظير الكربة ار
أثناء المحاربة: واضل ܐܫܝ 30 ارا
بالفارسسة
( المُوسَح » الاثط والناقص 7 ٠‏ قال الأزهري لا أصل له في 3 `
وقال عضهم معرب واصلة كرسق او كوسه ٠وقيل‏ هوعرلي من ܚܝܢ الرجل ايم
بشت له .4 ( خبط الحيط)٠قلت‏ ان كُمَج مشتق من أ ܚܝ والكوسج معرب
01 َه وهو ال ܝܐ تظ والذى 3 عأ نبة وعشرون ٠‏ ܕ 4 4 كوسه ܓ والسر ±
الدارجة والكردنة
( انكر كع لانن عر كا نزي
* ( كاش يكوش ) اجتَهّد مثل أكوشيدن لفظاً ومعنى
* ( ألُولان ) فارسيّتة ܠ وهو ننت البردي
002390) | 32 ® 810 جسلئيوس في معجمه العبرائي 00
الكلمة ® ܘܐ من ܠ جدى ± اي عادل (ܟܐܢܝܐ) ܠܚܟ 20300
فارسّة الاصل 0 0 أي رفيع القدر ومن وان اي رقيب < ܨ
حى
=== leaf 142 ===
‫ 1
ܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك
ܨ
* (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده
قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف
([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ
والمسك واللادن والكافور
```


## [2026-09-06T16:07:24.610Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef norm(s):\n    return s.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ء','').replace('ؤ','و').replace('ئ','ي').replace('ى','ي')\nfor i,p in enumerate(pages):\n    n=norm(p)\n    for pat in ['كاس','كاسه','كوزه','قدح']:\n        for m in re.finditer(pat,n):\n            ln=n[max(0,m.start()-120):m.start()+120].replace('\\n',' ')\n            print(i,pat,'|',ln)\nEOF"
}
```


### [2026-09-06T16:07:26.663Z] TOOL RESULT

```
7 كاس | 10101 وبالكردنة ܬܕ يم ( الاربريق) انا من حرف او معدن 71 عروة ܬ و بلملة ܨ $ ܠ يصب الما وهو يطلق بالفارسسة علي الدلو ܢܸܐ وكاس الممام والسطل وغير ذلك مما يضارعها ٠‏ ومية السر يالي ܐܒ ܘܝܩ والفرذ. ܨ 80 والايطا !3 95 :ܐ ܠ كردي × يق وهر به الرمالي
17 قدح | ب لامنس في كتاب الفروق الها ܐ عن )!$ 000 “الذي 18016 ܢ 5 مشتقة من بيله الفارسي ومعناه الوعا وشرنقة القز او 55( ومعناه القدح © ¢ كك . وما البالة عني السمكة واحلوت شعربة عن اليوالي »ܐܬܐܤ واحلوت نفسة معرب عن ?× ( يسان) هم بسان واحد وعلي سان وا
29 كاس |  اصل الثي ومنة الكردي بن (البنكام » ܓ < ܒ في البيهان القاطع > ` باككاف الفارسيّة علي وزن سندان يطلق سموماً علي القدح والكاس وخصوصاً علي 0 من النحاس متعارف بين فلاحي الهند يتقاسمون به !ܬܐ ٠‏ وذلك انْ اصعاب تكروم والزروع والبساتين يتمعون في ر
29 قدح | ححض وهو اصل الثي ومنة الكردي بن (البنكام » ܓ < ܒ في البيهان القاطع > ` باككاف الفارسيّة علي وزن سندان يطلق سموماً علي القدح والكاس وخصوصاً علي 0 من النحاس متعارف بين فلاحي الهند يتقاسمون به !ܬܐ ٠‏ وذلك انْ اصعاب تكروم والزروع والبساتين يتمع
31 كاس | سن ع الريح ٠وقيل‏ ܝ < بزهر ±[ ܚܨ وهو ܕ احمر 1 ٠و‏ يعرف 06 اف تبسن مقزل ان ا ܨ ܫ ܐ ± (المَهَو) الميث المقدم امام البيوت وكاس = ܙ فارستتة مهو وهو يطلق علي الغرفة والسرادق وقصر الماك وغير ذلك * (المهيّانة ) 80:60 الخفيفة الروح تعريب بهتانه وهو
45 قدح |  مع بياض وزرقة 0 ܚܝ ܐ في البرهان القاطع : : واسمة ܐ ܐ ܨ .وهو اذا :| وضع ܐܵܪܵܐ( اوورك ܝ 25 الاحتلام وان الخمز اذا شر بت بقدح مصنوع «نة لا تسكر ابدًا وكذا اذا وضع فيها 3 1 نوع من اللعل » ( الجَمَسَفْرم ) ܒ قوتة ,ܢ شبيهة بقوة الشّيح عل ا 0 ܨܐ 
47 قدح | (الجتاغ » فشر بضرب من ܓ قلت فارسيّتَهُ مجناغ ثوب مرضع منقّش يِلتَي علي السرج لازينة ١٠و‏ من المحتمل الَّهُ معرب عن 39 القدح والقصعة ( الجَنك) من الات الطرب تعريب جنك (الغنان) تعريب جنار وهو الدلل ٠‏ والصنار لغة فيه ٠‏ ومنة الكردي رحنار ܨ 0 
49 قدح | ووسهن ܢ القميص ܨ ܝܚ ` +( 05 للنسا 10 5 ¢ وق 8 ܡ ® ج000 (فردتكل ص 04 ير * (الجوار» الما الكثير التعير 2 تعر يب جور وهو القدح الطفحان *< الخورة) 1 تعريب كور وهر )× ( الجَوَرَب) .231 2 تعرينت #وديا دا مف دا اي قبر الرجل ٠‏ < ܥ 208 ܐܘ ܨ | الدار
53 كاس |  الشيوخ وبالاركة 7 قوحه ريحالي وقوجه باربوزي ܗ9() ܡ 3( سات ورقة ܐ الخمل 15 3006 ܣ £ الارهان القاطع : « الخريق نبات ورقة كاسان الممل ܠܦ < 0 للابيض منة في جيلان « بلخم او بلاخم » ܫ « اق حو بلمه وماروطق ويبان مازوسي وقار حيجكي 002 ܚ € .وال سود
108 قدح | ن صد اي الماية * (الصخن ) القصعة الصغيدة تعريب سيني ٠واما‏ فرتكل .38 فال 3 تعر باب ܝ 5011 (الصاخرة) تعريب ساغر ومعناه القدح (القد )ا قرريتك سدا ( الصاروج) الذورة واخلاطها معرب 0 003 لغة فيه وقالوا فيعها 2 ܨ ܩ ماخوذ ܒ ܚܝ ) والدهارج والصهري ܓ
123 قدح |  يتداوي بها من الصرع فارسيّها ܢܐ وتركيّتها كلنجك حرج ي دا كي + (الفو) ܐܝܒ ܨ < ܝ 232 ود لايل نات ورقه ܕ ا رفس وزهره نظير قدح من ذهب 0 قدر ذراع : ( الوم ) ععني النطة والختص !ܡ وساير المموب التي 9 فارستتها فوم ܓ 17; علي الخنطة والشعير (الفوة )
124 كاس |  ٠وقالوا‏ فيه قاب للا ا سرت كل ما الا ٠‏ والتَوْبٍ والمتَابٍ اي ܨܓ الشرب ٠‏ .2 200 غلي ® 5 + ( القنّة) ܝܢ 3 واصل معناها كاس )ܚܐ ܐܝܬ ܕ ܒܕܢ علي ااتفاغ كل : 6 كالقة وغيرها وممه 4 الكردي كه وهو ورم انا ل عد ق الغنم فاليا بج ) الحجل 3 3¢ ¦ + 00 
125 كاس | غة فيه * ( 0 ارتفع وَعلمل مره الارض 1 0# دسة) المبلذية والكناه 2 دا )1 اا .060 ( القَردما ܣ ) 031 اي حمل وبق ٠‏ سلاح للدكاسرة او الدروع الغليظة او الغفر له بيضة او قبا بحشو ( ܬܐ َّ الغليل ) ( ܨܢ( 7 ا 0 لطو دل مر مت من لخر اي حار ومن شب اي ل
132 كاس | بة عن ܩܦܠܐ بالارامسة باب الكاف 6 1: ( ܐܐܟ ) اي القدح وهو بالفارسيّة كاه وبالاراميّة ܟܣܐ وبالباباية 65 3 6 ` ¬ وبالكردية كاسك اظن انْ 3 097 الاصل ماخردة من . ܦܣܐ ܠܐܐ ܠܟ سب النسمية ظاهر .0 الكرز ذهر ܘܡ{ ٠‏ فتكون الفارسية قذ اخذت من اللغات الس
132 قدح | لي 6 ܕ ܐܠܐܘ سس سم رما والعر يي ܣ 391 والسر ܠܐܠ الدارج جذهي .وام | ܐ فعربة عن ܩܦܠܐ بالارامسة باب الكاف 6 1: ( ܐܐܟ ) اي القدح وهو بالفارسيّة كاه وبالاراميّة ܟܣܐ وبالباباية 65 3 6 ` ¬ وبالكردية كاسك اظن انْ 3 097 الاصل ماخردة من . ܦܣܐ ܠܐܐ ܠܟ س
136 قدح | طرنج فارسيّة اضلها كشت اي 0) ܐ الدياثة 10:52 9 كفيكان وهو الديوث + ( )ܥܰܪܶܐ ) فاسي محض وهو ما الشعير الطبوخ ( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من ܥ 9)\ (
146 قدح | ر اي مريض ومن ܚ اي حل المريض ٠و‏ يقال 4 ܢ ܠ خستهخانه (المرك) الما برن ماختوذ عن رك اي اموت د (المزو) ` بيض دقاق برَاقة تقدح منها النار. 71 ايضاً اسم جا لانراع. الرياحين فارسيتة عزو وقيل هو ضرب من الرياحين يقال له بالعر يّة ران الشيوخ ٠‏ وقي
175 كاس | لات ܙ كلاه )ܡܙ كات ܚ كلية سي كايدن لاسو ܚܐ ١4‏ كاته ܙ كاادي عب :12 كله ١2‏ ܟܢ ^[ ܙ كله خم ¥ ܙ كايوش ١78‏ كيري 43 ܬ ¥« ܙ كاستر ܫܘ ܨ( 4[ و لاسو ` كانجه .ܝܙ ܙ كان كين + ( كمخت لاسر كمر لاسو( 1 ا ܗ ܙ ( كبتار ܢܙ ܙ 15 ܀ ܚ ܙ ܢܬ )ܙ ܡ ܚܣ كنجر به"( ك
183 كاس | ܙ + ف ا فاق * ܙ ܙ فستق ܀ ‏ | فلفل ١١‏ فيل ܙ« ܙ + ي + فز هوه ترعز ١6‏ قفس +¥« ܙ قلات *« ܙ ܒܚܢ ¥« | ܪܐ به"( ܪܕ لمي جد ك + كاسك وسو كاغز وس( ܐ ܀ ܚܕ | "كيان ܙ ܙ | 0 ܠܝܐ ماسو كوب لوسرو كرح روسو 6܀‫> كوزر | جد 3 ܡ كازر | ܐܨ ¢ 0:02 كد سس 50 3 57 ك
```


## [2026-09-06T16:07:40.138Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[132][:2500])\nEOF"
}
```


### [2026-09-06T16:07:42.002Z] TOOL RESULT

```
ܢ ܗܙ ܝܝ
660 ܣ 70 2 7 75:35 20
0 _ +> ال 40016 معرب 6.076
73 ܙܝ حاروان والفرشي 1376 ¢ ܥ | الى 200124
و الاتكليزي 00011 والالالي 6 ܕ ܐܠܐܘ سس سم رما والعر يي
ܣ 391 والسر ܠܐܠ الدارج جذهى .وام | ܐ فعربة عن ܩܦܠܐ
بالارامسة
باب الكاف
6
1:
( ܐܐܟ ) اي القدح وهو بالفارسيّة كاه وبالاراميّة ܟܣܐ وبالباباية
65 3 6 ` ¬ وبالكردية كاسك اظن انْ 3 097
الاصل ماخردة من . ܦܣܐ ܠܐܐ ܠܟ سب النسمية ظاهر .0 الكرز ذهر
ܘܡ{ ٠‏ فتكون الفارسية قذ اخذت من اللغات السامة كه :3 نا
413 ® ܟܘܙܐ بالسر ܐܸܝ واامابامة ٠‏ و يقرب ܟܣܐ 1 اه
0 ܕܐ 3 واأر دعي عتلى :
* (آلكنابة) دواء صيني فارسلتة كا به . قال في ܫܐ )5 بد على
وزن ܐܢܬ دواء معروف و سسميه البعض كا به مه ويقال 4 ܝܚ حب 3 .
واحسنة الذي ܐܝܢ من ܥܨ يرة شلاهاط من جزائر الصين و يسمِيه البعض ܫ
 ( °‏ )ܒ )
00 0.0 95 9 وهر 79959 9505 0:75
ܪ ܥ 20015 والاتكايزي 1ه والفرنسى اع لمق
```


## [2026-09-06T16:08:00.265Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; echo ...; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T16:08:01.906Z] TOOL RESULT

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
...
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-06T16:08:18.291Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFA Becher/kūzā ==\"; grep -n -i \"Becher\\|Krug\" AFA.txt | head -20"
}
```


### [2026-09-06T16:08:18.342Z] TOOL RESULT

```
== AFA Becher/kūzā ==
1227:»eine Art kleiner eiserner Becher, in denen sich die Thür-
2663:neinen möchte , zu sein. Diesen , nicht eiuen Krug zahlen
2741:kocht, in einen Krug gethan und von da tropfenweise
2825:(belegt bei (uiuh. s. v. ^jo\) »Seherbe eines Kruges" oder
2885:vorzuschlagen. Auch das jemeuische üJU »Krug'* scheint
2922:[Zwei echt arabische Namen für den Krug sind J^^l^ und
2929:ren, iis^ »Krug" gehört zur Wurzel I^. »ziehen", wie
2930:|?&^, »Krug, Becher", zu ^33. Auf dieses Wort geht
2931:bekanntlich fr. giarre »SchiflFskrug, ital. giarra zurück.]
2950:und Aramäisch bei \^ einem kleinen Kruge, das ebenso-
3073:]Ji^c^ >Krug" als Bedeutung angegeben wird, während
3084:halber Krug, in den man Pflanzen (D*3^> » übersetzt aus
4620:eine ganz andere Bedeutung »Becher". Auch fehlt das Wort
5708:spricht von gepfeffertem Weine f (i*Äj) ; Becher , die ge-
5860:den Rasatün rein, in einem mächtigen Glaskruge.** Es ist,
5911:mit einer Schnauze versehenen Kruge für den Wein (so
5998:S^b »Becher'* Zuh. 9,7; 'Alle. 13,41; Divän Leb. 132,
6096:Gewi=s aramäisch ist auch äjLi >Weiiikrug" Näh. 24, 10;
6149:Im Jüd. amm. bedeutet Sr!2 direct »Becher Weines"
7223:dern ist eine allgemeine Bezeichnung für »Krug". Wo es
```


## [2026-09-06T16:08:20.040Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW calix ==\"; grep -n \"^calix\\|calix,\" LEW_1910.txt | head; echo \"== LEW columba ==\"; grep -n \"^columba\\|columba,\" LEW_1910.txt | head; echo \"== LEW gladius ==\"; grep -n \"^gladius\\|gladius,\" LEW_1910.txt | head; echo \"== LEW calamitas ==\"; grep -n \"^calamitas\\|calamitäs\\|calamitas,\" LEW_1910.txt | head"
}
```


### [2026-09-06T16:08:20.141Z] TOOL RESULT

```
== LEW calix ==
== LEW columba ==
== LEW gladius ==
== LEW calamitas ==
```


## [2026-09-06T16:08:24.247Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5985,6015p' AFA.txt; echo \"===\"; sed -n '6140,6165p' AFA.txt"
}
```


### [2026-09-06T16:08:24.318Z] TOOL RESULT

```
p. 87, 18 und Nüldeke dazu ZDMG. Bd. XXXV. p. 497.
Unser Wort aber ist übernommen aus )ALwo Bar Bahlül
bei Payne Smith s.v. ^hz) [Barh. gr. I. 33,8; Overbeck
49,20 Nöld.] und gehört zur aram. Wurzel »lautern'*, die
auch im Jüd. aram. sehr üblich ist (rgl. ^Arüch s. ▼. /V
I; Low Aram. P/iittu. p. 90) auch meist vom Weine ge-
braucht. Ein drittes Wort Jl^lmu« soll nach Ibn Doreid
jemenisch sein. Da aber IL^^ als »Seiher** durchaus üblich
und ein zufälliges Zusammentreffen schwer anzunehmen ist,
so ist es als aramäisches Lehnwort anzusprechen. JiioJt
ist dann denominativ. Es gehört zu /HIS^ »tropfen** Jdmä
78«» Mitte =\--k.
Schon in der Form zeigt seinen aramäischen Ursprung
S^b »Becher'* Zuh. 9,7; 'Alle. 13,41; Divän Leb. 132,
12; Jät:üt IL 180, 3; 538, 8 (A'äa). Es ist syr. ha^
nur ProY. 25, 11. Im Jüd. aram. scheint es auch zu
fehlen ^). Es ist zunächst »Schaale** und leitet sich wohl
von r^ »ziehen" ab, also »Zieher'*. Zu vgl. ist rielleicbt
gl^ ron ^^. »Heber**. Für die Sicherheit der arabischen Tra-
dition erweckt es ein günstiges Vorurtheil , dass Gaub. an er-
ster Stelle »Schaale'* als Bedeutung angiebt. Ob'Abdd. Zar. 88^
für »Ui:3, (das man eventuell von 1233 = Cp^ (vgl. Nöl-
deke Mand, Gramm. b4) ableiten könnte) *X"T^31 zu lesen
ist, wie ich De vocabulis etc. p. 15 vorgeschlagen hab6|
1) DtM et sich io den Proverbien auch im Targüm ftndtt, bedtatct BAck
dem Charakter dictes. bekaonilich «ui dem S/ritchen übemommenea Werket
nirhtt.*:*> rvv^r^,-.-- :, \ :i68
v"^V.-'
»>#
-»r- ' •. V.
^"'?- •':*■■■■■• ^ ■ • - *■ .
===
17, 5: Jäküt II. 220, 10. Man trank ihn am Häufigsten
gemischt mit Honig und Wasser Kamil 73, 17; zur Hälfte172
mit Wasser Amrk. 17, 9; Kamil 26, 11; Bekn 361 ult.;
Tar. Mu'all. 57; Koran 76, 17; Bekri 163, 7; Tab. I.
752, 17; Agäni II. 34, 8 v.u. — Das technische Wort
dafür ist dasselbe, wie im Aramüischeu, numlich ^Ct*
Dies ist gewiss erst deuominativ von --fCo» welches ge-
nau aramäischem U^}^ entspricht. Es bezeichnet ursprüng-
lich den Zusatz an Wasser, dann die ganze Mischung.
Im Jüd. amm. bedeutet Sr!2 direct »Becher Weines"
Levy Nhbr. Wtb. 111. 62. Vgl. auch UV,>1^ als Flüssigkeits-
maass Lüw Aram. PjianzA&l. Anm. DerWeiu wurde aber auch
ungemischt (akpxtsc) getrunken. Ein vorislamischer Dichter
sagt: »Und ich kam in die Kneipe und gab ihm den Mor-
gentrunk von altem ungemischtem Weine , der nicht ge-
tödtet wurde" Agäni XIX. 93, 13. Später bedeutet yt
mischen überhaupt. »Den bitteren Tod zu kosten ist süss,
wenn wir ihn gemischt haben mit rühmendem Geden-
ken" Kämil 542, 14. [Das Gegentheil von ^\y9 ist
ol^ der lautere Wein]. »-fL« im Sinne von »Tempera-
ment" ist dann selbst gelehrte Übersetzung von l-*^!^^
••
xpiffii bei Ärzten und Philosophen. Vgl. Kuhn LitteraturbL
für Orient. Phil. I. 413 »)•
Ein aramäisches Wort ist gewiss auch der Name der
Kneipe vL^li T^r. Mu'all. 74; Kämil 459, 2; Agäni XIX.
```


## [2026-09-06T16:08:26.095Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"==LEW==\"; grep -n \"calix\" LEW_1910.txt | head -5; grep -n \"columba\" LEW_1910.txt | head -5; grep -n \"gladius\" LEW_1910.txt | head -5; echo \"==LAT==\"; grep -n \"calix\" LAT.txt | head -5; grep -n \"columba\" LAT.txt | head -5; grep -n \"gladius\" LAT.txt | head -5; grep -n \"calamitas\\|calamitäs\" LAT.txt | head -5"
}
```


### [2026-09-06T16:08:26.216Z] TOOL RESULT

```
==LEW==
==LAT==
8684:calix
8717:calix, -icis m.: coupe, vase A boire; puis toute espfece de vase,
8718:marmite; cf. Varr., L.L.5,133, calix a caldo (i), quod in eo calda puls
8724:Les Latina voient dans calix un emprunt au gr. xuXl<i;, ainsi Prisc.,
8725:GIX II 167,1; calix CK.710 xou xuXiJ;. En realite, le mot peut etre d'ori-
13076:columba
13116:columba, -ae f. et columbus, -1 m. : colombe, pigeon. Correspon-
13118:columba 7 . dicit... nam agrestes palumbes uocantur. Sur le genre, cf.
13119:Varr., L.L.9,56, tum omnes mares et feminae dicebantur columbae, quod
13121:cos usus quod intemouimus, appellatur mas columbus, femina columba.
5072:menta corporis essent, tela in hostem hastaque et gladius. Designe
12592:parma, gladius, lorica, lancea, etc.). Cf. sub ina et sibina-, lumpa et
18825:ensis, -is m.: epee. Meme sens que gladius, d'aprbs Quint .10,1,11,
18831:a ete supplante par gladius, qui doit etre celtique, et celui-ci a
25231:des langues etrangeres, comae gladius, gubernare, gummi, un g latin
2486:alapa, calamitas, ete.
2568:alacer (cf. anas, calamitas, etc.), v. Devoto, Riv. di Filol. Class.
8605:entre calamus et calamitas d'aprfes le rapport ollua, olluitds; ficus,
8608:culmi pereunt, quod a rusticanis calamitas appellatur ; de m 3 me encore
8609:Don., He.a, uitium et calamitas: bene secundum augures. Vitium enim
```


## [2026-09-06T16:08:42.749Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8717,8735p' LAT.txt; echo \"=== columba ===\"; sed -n '13116,13135p' LAT.txt; echo \"=== gladius ===\"; grep -n \"^gladius\" LAT.txt | head; sed -n '18825,18840p' LAT.txt; echo \"=== calamitas ===\"; sed -n '8600,8625p' LAT.txt"
}
```


### [2026-09-06T16:08:42.863Z] TOOL RESULT

```
calix, -icis m.: coupe, vase A boire; puis toute espfece de vase,
marmite; cf. Varr., L.L.5,133, calix a caldo (i), quod in eo calda puls
apponebatur et caldum eo bibebant . Specialement: tuyau d’aquednc.
Fr6quent dans la langue de 1 'Aglise, au sens de "calice". M.L.1519.
Germ.: v.h.a. helih, etc.; celt.: iri. cailis, calich, britt. celeguel .
Derives: caliculus M.L.1513; calicellus; calicldre (-rium) (Gloss.):
ubi conduntur calices.
Les Latina voient dans calix un emprunt au gr. xuXl<i;, ainsi Prisc.,
GIX II 167,1; calix CK.710 xou xuXiJ;. En realite, le mot peut etre d'ori-
gine indo-europeenne^ ancien *k'lik--, outre xuXui; (dont l'u 3'explique
par 1 'existence de k°lu-) et xaXu?;, on rapproche skr. kaldcah "pot,
coupe" et kalikd "bouton de fleur". Il y a des formes A s- initial:
gr. oxuAXi.ov, oxaXiS, chez Hesychius et ombr. sca Ise-to , skalpe-ta "ex
paterS.". - Le groupe de v.h.a. scala "enveloppe" est A separer. Mais
il a pu se produire une confusion entre calix et calyx, emprunt savant
au gr. xotXui; "enveloppe de fleur, calice" et qui a pour derivas: ca-
lyc(u) lus; calycia f., nom de piante; calyc(u)laris, -ria (herba), ca¬
lycis lata (herba) (cani-, cali-) "jusquiame", dont la forme diff6ren-
ci6e caniculdta a ete influencee par un rapprochement avec canis, cf.calllomarcus
=== columba ===
columba, -ae f. et columbus, -1 m. : colombe, pigeon. Correspon-
dant A 1 'oiseau sauvage palumbes, cf. Serv., Ae.5,313, de his domesticis
columba 7 . dicit... nam agrestes palumbes uocantur. Sur le genre, cf.
Varr., L.L.9,56, tum omnes mares et feminae dicebantur columbae, quod
non erant in eo usu domestico quo nunc; <nunc > contra, propter domesti¬
cos usus quod intemouimus, appellatur mas columbus, femina columba.
Toutefois columbus se lit d 4 jA dans Piante, Ru.887 A cot 4 de columba,
Mil.163. Les deux formes sont representees en roman, M.L.3066. Passe
en germ.: ags. cui (u)fre, et en celt.: iri. colu*, britt . colomen.
D 4 riv 4 s: columbare (columbar) n.(d'un adj. columbaris); columbarium:
i°colombier, pigeonnier; 3 0 niche pour les urnes fun 4 raires, M.L. 30 & 3 a;
columbinus, M.L.3064; columbula, M.L.3065; columbor, -aris "se becque-
ter ".columbares
340
La comparaison de lat. palumbes (7. ce mot) et de v. sl. golfbi "pigeon"
(cf. r. go lu boj "bleu") engage A voir dans coi- la d 6 signation d'une
couleur; le_ grec a en effet xoXu(Apoc "petit grbbe" 4 cote de xeXotivoc
"noir, sombre".
colunbares (oliuae): olives confites. Deformation populaire (Pal-
lad.) de colymbades (oliuaej = KoXu^a8eS eXaou qu'on lit dans Colon.,v.
=== gladius ===
26244:gladius, -i a. (gladium, cf. Lncil.1x87, Varr. L.L.5,116; S,45j9,
58746:gladius usu splendescit, situ rubiginat) ; par suite: vetuste, de-
ensis, -is m.: epee. Meme sens que gladius, d'aprbs Quint .10,1,11,
mais surtout reserve 4 la langue de la po^sie, cosme ensifer, ensiger
(imitation du gr. Ejt.cpqpTiC, designant Orion), ens ipotens. Dis. : ensiculus
(Pl.). Le caractere poetique et litteraire du mot explique qu'il n 1 ait
pas passe dans les langues romanes. Du reste les noms d 1 armes se re-
nouvellent et s'empruntent avec les objets qu'ils designent; ensis
a ete supplante par gladius, qui doit etre celtique, et celui-ci a
subi dans les 1.romanes la concurrence de spatha qui est grec, cf.
M.L.8138; Couissin, Les armes ronaines, p.489.
Le mot a un correspondant exact dans skr. astji "^pee" et n'en a pas
d'autre. Il est possible, mais incertain, que gr.aop soit apparenti.
L'i de ensis n'est pas plus essentiel que celui de axis.
enthSca, -ae f.: 4 pargne; materiei d'une exploitation; greniers
publics. Bmprunt tardif fait par les juristes au gr.evGi^HTi; de 14
enthecdtus, -carius. M.L.3876.
enubro: inhibenti, P.F.67,10. A rapprocher du meme, 97,13, inebrae3S1
=== calamitas ===
perdition (joint k clades Pl>,Cap.gn, k uitiun Ter.,Hec.a, etc.);
a° ap 4 cialement toute espfece de fl 4 au qui atteint lea r 4 coltes: aaladie
qui frappe lea tigea du bl 4 , grele (qui lea renTerae), etc. - Ce aecond
aena, bien qu'anciennement attest 4 , r 4 suite sana doute d'une sp 4 cioli-
sation aecondaire, due 4 un rapprochement fait par la langue rustique
entre calamus et calamitas d'aprfes le rapport ollua, olluitds; ficus,
flcitds, etc.; cf. Don., Eu.79, calamitatem rustici grandinem dicunt,
quod calamos comminuat, et Serv., G.i,151, robigo genus est uitii quo
culmi pereunt, quod a rusticanis calamitas appellatur ; de m 3 me encore
Don., He.a, uitium et calamitas: bene secundum augures. Vitium enim
est, si tonet tantum; uitium et calamitas, si tonet et grandinet simul,
uel etiam fulminet. - Calamitas doit Stre d 4 riv 4 d'un adjectif, ce
qui eat la formation normale des abatraits en -tds, cf.nouus, nouitds,
et dans ce cas il est k rapprocher de incolumis, oh le vocalisae 0 en
syllabe int 4 rieure eat command 4 par l qui suit, et par 14 4 clddes,
etc., si bien que le rapprochement de clddes calamitdsque signal 4 plus
haut dans Plaute doit Stre une figura etymologica. V. *celld.
Pour le maintien de d en syllabe int 4 rieure, cf. a lacer. - La pro-
nonciation et la graphie kadamitas attribu 4 es 4 Pomp 4 e par Mar. Viet.,
GLK VI 8,15, r 4 aultent d’un autre faux rapprochement arec cadere, cf.
Iaid., Or.1,37,14. La glose d'H 4 sychius xa 5 a(ioS; TuepXoC, SaXajiivioi.
ne fournit de rapprochement ni pour le sens ni pour la forme.
Ancien, uauel et classique, mais banni de la po 4 sie dactylique par
sa forme. Non roman.
D 4 riv 4 : calamitosus, ancien, classique, form 4 sans doute directement,
aans qu'il soit n 4 cessaire de supposer une haplologie de *kalamitdt- 8 sus,
```


## [2026-09-06T16:09:04.245Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\nfor i in (246,247,248):\n    print(\"=== leaf\",i,\"(≈pp\",(i-15)*2,\"-\",(i-15)*2+1,\")\")\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-06T16:09:06.243Z] TOOL RESULT

```
leaves 858
=== leaf 246 (≈pp 462 - 463 )
 1-rem. Cf. also itós, itis. The vocalism of Hitt. iyami ‘go’ is uncertain
-i, an adverbial theme.
Skt. div-i “by day’; Gk. di(w)i, id.; Lat. (Plau- tine) cf. diu, id.; Arm. brni ‘violently’; art mni ‘awake’; heti Con foot’, cf. Lat. pede-pressim, -tentim, cf. Gk. par podí; Lat. pro-pe (*d)
£hül- — -ibhi(s)
20
25
30
40
45
426
t
ehut-, radical extn. of type ghu-, see ĝhuuð, 8heuó, cf. &hütis in Skt. hutih ‘sacrifice’; Av. a-züitis "libation; Myc. cf. (queried) e(n)- kusewe ‘funnels’; Gk. khüsis ‘pouring, melt- ing, liquid’; OLat. fütis, f. ewer Li. Zütis, f. end. death’. For *&hutlo-, *&hutil-: Av. cf. u(s)zui6ya- *welling-up'; Gk. khütlon, khutla ‘fluid’; Lat. cf. fütile *sacrifical vessel; Umb. cf. ficla (equated in a parallel text w. sopa- *sacrifical liquor'; a LW in Lat. fitilla. For IE *-ü- > Umb. -i- cf pir "Drei MHG goder ‘vortex’, represents a form *$hutros
$hutós ‘poured, cast, libated; liquid, liba- tion’. Cf. &hu-, $huuó, etc. Skt. hutáh "libated'; hutám ‘offering’; Arm. (?) dzu, gs dzvo, o-st. “egg? (isophonic only. Se- mantics obscure); Gk. khutós (cast; s. "mound Myc. kut-; Lat. futum ‘sprinkler’; Umb. cf. hufie ‘to a certain god'; Go. gup, OE god, ON guð ('god', and com. Gmo.); Li. fütas *perished'
8huuo (1) *pour, shed, cast, scatter, destroy'. Form of gheu-, q. v. Gk. cf. khúto “was poured'; khümenos, pt.; cf. khudaios ‘poured; vulgar; Li. Züvu, Son ‘perish’
êhuuð (2), see ĝuhuð, etc. Vedic huvámi, pp. hütáh; OCS züvo züvati ‘call’
&hu-. For forms with ĝhu- as an initial, see
£uh-
*near); Arm. gari “very”, etc.; Doric cf. auteí: Alb. ven “of itself; aty pari as an adv. ‘round there’, etc. Gk. cf. autó-mati (“of itself. See meníh- ment- ‘move, stir, z-gde mnt(h)-); Latv. liegi “gently”, etc.
-ibhi(s), instrumental extn. as an adv. for- mant. Cf. iebhi. (
=== leaf 247 (≈pp 464 - 465 )
glow’; (un- certainly ong "Drei: OW cf. enn-ynny, W cy- nneu (?) *ignite'; beside enn-yn, m. (‘kindling, ignition’, fr. *endo-Ígn-?); Cor. cf. (?) c-cena, v. ‘ignite’; OCS (and com. Sl.) ogni, gs and ds ogni, m. ‘fire’; Li. ugnis, gs -iés, m. id.;
-ibhos, à, om — -iið
20
25
30
35
40
45
428
Latv. uguns, gs id., gp ugunu, id. (Of uncer- tain provenience are MIr. indeoin, Ir. inneoin ‘anvil’; OBr. ennian, Br. annéw, id.). Extns. Seng ‘inflame’: Lat. ignio, -ire; Cz. roz-ohnit; Li. ugnytis, id. Cf. Latv. ugunot illuminate". *ígnikos “little fire’: Skt. agnikah; OCS ognici, id.; *ígnisthios: Skt. agnistháh ‘brazier’; OCS ogniste ‘hearth’; ognistü, adj. ‘aflame’; ognistvo ‘torch’; *ígniuos: Lat. ig- neus: Cz. ohňový
iĝ- (?) “ice? W ia; Swiss Jäch; Li. íZas “floating ice’; OE cf. gicel, gicela, m. “icicle*; ON jokull, id. (dim. type). The vocalism of Mir aig, gs ega "ice is obscure
iieto, -u, pl. iionto, -u, an impersonal verb- type: ‘go’. Cf. ei-mi, i- Skt. cf. 1yáte, tyánte, impf. -ata, -anta (in other verbs); Hitt. iyata “he goes’; iyanta ‘they go’; cf. iyanta-ru “let them go’; Gk. cf. iónton “let them go’; Lat. itur (“there is a journey’, perh. for *iieto + Ē, q.v.)
-iiə (-iia, -io) collective extension of a sim- plex Skt. gavya ‘kine’; $Sunya “pack of dogs’; Av. cf. jonayo "of women’; Arm. majri (forest: majr “pine”); uri (^willow*: ur *vine-tendril); Gk. oikía ‘household’; Lat. familia, cüria; Ir. bráithre ('kinsmen": bráthair ‘brother’); luibh ‘herb’; W adein, adenydd “wings”, fr. *potonio, *peteniieo: adan, sg. ‘wing; OBr. mined ‘mines’; modreped ‘aunts’; Go. bandi ‘fetter’, mawi ‘girl’; OE bece (Cbeech": boc); OCS lovlja (hunting: lovi); gospodZa (Clady': gospodi); bratija “brethren”; Li. avijà (*flock': avis); eile ‘Jine’; Latv. spiede (‘the Press’: spiest, v. ‘print
=== leaf 248 (≈pp 466 - 467 )
akah, dim. id.); Lat. canticus (‘song’: can- tus); cf. carrüca, beside carrus “little cart’; Bret. moedik (‘little thumb’: moed); OCS cf. otici (*daddy', cf. Gk. átta); potoðici ("little stream’: potokü); etc.; Li. kulikas (little bag’: kule); Sunikas (‘rascaľ’: Suð); cf. Li. avike *ewe-lamb'. For Cz. srnec (‘fallow deer: OCS srini 'roe- buck', see Krn-)
-ikos, -ikā (2) descriptive adj. extn. (often becoming the basis of an agent-noun)
Skt. cf. matrkah; Av. vorozika- (vorozo); Gk. statikós (stásis), kunikós (kuon); Lat. müricus (mūs), canticus (cantus); Osc. tüvtiks, toutico- (touto); Br. groenek (groen); W boneddig (bo-
sa a = -iiom (-iom) — -imos
20
25
30
35
40
45
430
nedd); MHG stætic, gs -iges (cf. stat); OE ste- dig (‘sterile’, cf. stede “fixed point); OCS lo- vici, adj. & s. (lovið: Li. cf. teltikas summo- ner”; tarpikas “entry”
-ilis, adj. extn. of quality Alb. cf. í vogël ((small', fr. *suagilis or *uag(h)-); Lat. cf. qualis, tālis, gracilis, habilis, etc.; OCS cf. koli, tolí “how much, so much’: Latv. cf. svilis (“red pig’, cf. Lat. suile 'sty^)
1ló, ið ‘come, go, rush’. Cf. eilà Skt. dëm ‘come’, cf. íla ‘flow’; Irah ‘wind’; Gk. cf. hom-iléo ‘consort’; Myc. cf. om-irijo- (‘of an assembly’: homilou); OS (an, MHG (en *be eager, hurry'
Vos, üs (eil-) ‘mud, filth’. WP I, 162 Gk. ilüs “mud”, eilüs ‘fen’; Ir. ile ‘grease’; OCS ilú ‘mug’; Pol. it “blue clay’; Li. cf. (?) yla ‘sandbank’; Latv. ils ‘dark’
im, enclitic acc. pers. prn. ‘him, her, it Skt. cf. im-ám, mf. acc. ‘this’; Arm. cf. in-kn (self, fr. *im-suom); Dor. in “him, -self, her, -self; Go. cf. ina; OHG in, inan ‘him’; OCS i ‘him’; je ‘her’; jet: OLat. im (^him'. Fest.)
-im, adverbial suffix. Cf. -imi Gk. cf. pál-in, prin; Lat. noct-im, carpt-im, etc.; Latv. cf. pret-im, prp. ‘towards’; OCS pré- mí ‘straight
```


## [2026-09-06T16:09:14.495Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (264,265,266):\n    print(\"=== leaf\",i)\n    print(pages[i][:1600])\nEOF"
}
```


### [2026-09-06T16:09:16.536Z] TOOL RESULT

```
=== leaf 264
nt obscure)
kaik- (1), kaikos “blind, dim, dark WP I, 328 Skt. cf. kekarah 'squint-eyed'; Lat. caecus ‘blind’; MIr. cáech, adj. “blind, one-eyed, squinting’; Ir. caoch 'dim-sighted'; W coeg, adj. ‘vain’; coeg-ddall “half blind”; Br. (dial.) kuik, OCor. cuic, Cor. cók, coek (*one-eyed'. Cor. also ‘empty, vain"); Go. haihs ‘one-eyed’; Swiss cf. ge-hei ‘nebulous, obscure’; G Hai “fog?
kaik- (2) “croak, screech' Skt. heka ‘screech’; Br. koaga, v. ‘croak, caw’; Cz. cek ‘noise’; MHG cf. heiger ‘heron’; LW in Finn. haikara, id.
kāĝ- — kaist-
10
15
20
25
30
35
40
45
460
kailiið ‘cover, shelter, protect. Cf. kailos, à (1) Go. hailjan ‘heal; MHG heilen, id.; OFris. cf. heli- (brain-', cpds.); ON heili, n. id.; OCS (and com. S1.) céljo, céliti heal; Li. cf. káilis "hide, skin”
kailos, à, is, io (1) ‘protective, safe; cover, shelter, sanctuary, bliss". WP I, 329 Skt. cf. celah, cailah ‘garment’; Lat. caelum; Osc. kaíla “temple, shrine’; W coel, pl. ion, f., cpds: coel- ‘rune; omen; trust’; Late Olr. *cáel (written cél omen"); Go. hails ‘whole, sound”; OHG heil, id.; MHG heile 'security, bliss; OE häl, as Go.; hæl ‘omen’; hæle ‘safe’; ON heill adj. “hale”; s. Tuck, omen’; hæli ‘refuge’; OCS célü, adj. ‘whole’; cély, gs célüve, f. “healing”; OPr. kails, as Go.; kailü-, in cpds.; Li. cf. pats kails! ‘good health"; káilis, gs io “hide, pelt
kailos (2) ‘single, alone, deprived'. See kai-, kaikos Lat. cf. cael-ebs, gs. -ibis beside coel-ebs *un- married; bachelor’; Latv. kails ‘bare’; OCS cf. célizna ‘wasteland’
kaisər- ‘rough, shaggy; tangle, shag’. WP I, 329 Skt. késaram “hair, mane’; Lat.
=== leaf 265
acify’. See quieio
kàios, à “base, pedestal, trunk, stem, stand, leg’. WP I, 362 & 509 Skt. kayah ‘trunk, stem, body’; Arm. kaj, kajk, i-st. ‘seat, position’; kajan, Let lodge"; kajun, adj. ‘stable, firm’; MHG hei, heie, f. (ram- mer, beetle’; G Heie 'paving-ram'; Du. hei, id.; Sw. cf. hajare 'pile-driver'; Li. kója “leg, foot’; Latv. kāja, id. (& “base, stand")
kakā (kakk-) ‘excrement’. WP I, 336 Per. kak ‘biscuit’; Gk. káke “evi” beside kákkeé ‘excrement’; Alb. kaké, id.; Lat. cf. caco, are, v.; MIr. cacc, f.; Ir. cac, m.; W cach; Li. kaka
kakāið (kakk-) “void excrement'. WP I, 336. Cf. kakā Gk. kakáo, kakkáo; Lat. caco, are; Mlr. cac- caim; Ir. cacaim; Cor. caca; Li. kakóju, óti, id. (an onomat. term, non-historical in Cz. kakat, G kacken, etc.). Br. kach, s., kacha, v. indicates a prototype *kakk-
kākāið ‘cackle, guffaw, mock? Gk. këkázo ‘revile’; OHG huohon, MHG huo- hen, id. beside huoh, m. id. (Onomat. and am- big. in Gz. kákat ‘cackle’. Cf. quaquaió)
kakolos (kakk-) fdropping(s), berry, grain’. Cf. kokolos Skt. (ambig.) kakkolah “a berry-bearing plant’;
kait- — kakupit (kaput-)
10
20
25
30
35
40
45
462
Arm. kakyi (clime-tree" from the fruit); Gk. kakalía (a seed or plant, prob. not ‘coltsfoot’, cf. Lat. LW cacalia ‘wild caraway’); Br. kagal ‘droppings’; W cagl. id.; Cor. cagal, id. & ‘clot, lump’; OHG hagal (and com. Gmc. "hal": cf. also G Hágel (^millet', and perh. Gk. kákh- lex ‘pebble’ if fr. *kaghl-)
kakoros “bird, cockerel" or sim. (Ambig. cf. kokoros). Onomat. Skt. cf. kakarah (a bird); MHG cf. hageln (‘rail at; haggle’. Onomat.); cf. also hagel-gans («heathco
=== leaf 266
ncers’; Alb. cf. n-gath ‘Impede; be- numb’ beside sh-kath ‘loosen, limber up’; MHG cf. hegen ‘keep, save’; LG id.; OS cf. hagu-stald (‘servantť’, lit. 'retainer); ON cf. hogld, npl. hagldir ‘buckle, cleat, toggle’, hagi, m. ‘pasture, meadow’; OE haga ‘enclosure’. (The Gmc. forms are ambig.)
kak- (3) (?) ‘withered, miserable, diminu- tive’. Cf. koK- Av. kasus ‘little’; Oss. cf. käs-tår ‘younger’; G hager, EME hagger (Clean" LW in Fr. hagard); R kósnyj ‘sluggish’; Li. cf. kašiù, éti, v. ‘wither, shrink’. (Alb. ngath ‘benumb’, fr. *en-kak- here, or to (2))
kak- (4) ‘strike’ (Phonol. ambig.) Skt. ka$àmi “strike, kil; Arm. kasum, aor. kasi ‘thresh’; OCS cf. pri-kosno -noti “touch?
kakKiom (?) ‘milk curdled and strained, cot- tage cheese. Lat. caseus, caseum “cheese” beside It. caccio, id.; Alb. kos *yoghurt; Li. cf. kósiu, kósti ‘strain, filter’; Latv. kaSu, kāst, id.
kal- (1) (kalt-) ‘slope’. Cf. WP I, 430 and kalt- Skt. cf. katakah 'slope'; Go. wilja-halpei, f. ‘favour’; OHG hald, adj. ‘inclined’; G Halde ‘slope’; Du. cf. hellen, v. ‘tilt’; ON hella *de- cant’; R cf. po-kolét ‘die off”; Li. kaliuos, kal- tis ‘lean’; üZ-kaliu, -kalti ‘lean’; at-kaltis, f. “back of chair; LW in Finn. kaltto, kalteva ‘sloping’
kal- (2) ‘bright, white’. Cf. WP I, 429 Gk. kalós (‘bright, beautiful’. Despite Boeot. kalwós?); cf. kállos, n. ‘beauty’; (-a- in) kelás, gs -ádos ‘goat w. white blaze’; Lat. cf. calidus (or calidus) *white-blazed'; Latv. cf. kaleju, et ‘bleach’. (Link w. Lat. caleo, ere "be bot, and w. LG hellig ‘thirsty’ uncertain). Cf. kali-
kak- — kaldhos
20
25
30
35
40
45
 
464
tero-
k
```


## [2026-09-06T16:09:22.547Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[266][1400:4200])\nprint(\"=== leaf 267 ===\")\nprint(pages[267][:2500])\nEOF"
}
```


### [2026-09-06T16:09:24.405Z] TOOL RESULT

```
f. calidus (or calidus) *white-blazed'; Latv. cf. kaleju, et ‘bleach’. (Link w. Lat. caleo, ere "be bot, and w. LG hellig ‘thirsty’ uncertain). Cf. kali-
kak- — kaldhos
20
25
30
35
40
45
 
464
tero-
kal- (3) (kalaio, kaleio) “call, name, summon, invite, accuse'. Skt. cf. usa-kalah ‘cockerel’; Hitt. cf. kalles- “invite, entice’; Gk. kaléo; Alb. kall ‘slander’; OLat. caló, are ‘call’, cf. concilium ‘council; Mir cf. cailech, mod. coileach ‘cockerel’ be- side Ir. caileachas (‘cocksfoot’, bot.); W cei- liog ‘cockerel’; OHG halon, v. ‘call, invite’; MHG haln, id.; Li. cf. kal-bà ‘speech’, kaltas, adj. ‘accused’; kaltis, ies, f. ‘accusation’; cf. also kalenti ‘gabble, as cranes’
kal- (4) ‘fix, fasten, hold’. Cf. WP I, 437. Same as (5) and (6)? Skt. kalami, kalayami, id.; Arm. kalnum, ka- lanem, id.; kalank ‘arrest’; Alb. cf. ngel (“hold, stop”, fr. *en-kalio); Lat. cf. inter-calō, -calāre (2) “delay, stop’; Li. ap-kalinti ‘imprison’
kal- (5) ‘thrust’. (Same as (4) and (6)?). Cf. WP I, 437, but cf. kol- Skt. kalāmi, kalayāmi (2) ‘thrust, drive’; Arm. cf. kal, o-st. ‘threshing floor” (fr. *kalios); Alb. kall (2) ‘thrust, insert, bung’; Lat. cf. inter- calo, are (1) “insert”; OCS (here or under (6)) koljọ, klati ‘stab’; Li. kalù, kálti ‘drive in; forge’; Latv. kaļu, -t, id.
kal- (6) ‘strike’. Same as (4) and (5)? Cf. WP I, 437 Per. cf. kaland ‘spade’; Arm. cf. kal, o-st. (‘threshing floor’, but equally to kal- (5)): Gk. kalís *adze'; Lat. cf. hordi-calia (for *fordi-°: ‘sacrifice of cows in calf; ON heljast (toil but equally to kal- (5); OCS koljo, klati (‘stab’, equally to (5))
kal- (kaleio, -āið) “lure, deceive’. WP I, 446 Gk. kéléo (allure, if w. IE *-a-); Go. holon ‘curse’; OHG huolian, v. ‘cheat’; ON hoela ‘flatter, praise’; Du. heulen ‘conspire’
(kalbhā, see Supt: K)
kaldhos “firm, tight; firmness, strength'. See next and kadlos Lat. (ambig.) callus ‘hardness; hard skin’; MHG halt (Cholding; condition, place’; adv. ‘rather, moreover’; OS hald, id. beside Go. (and com. Gmc.) haldan ‘hold’; Dan. Norw. Sw. cf. hellere, heller, hellre ‘rather’; Sw. helst ‘preferably’; Ukr. kolod-ka ‘padlock’. Cf. Norw. helle, Sw. hälla ‘hobble, an animal’
465
kaletos (kalət-, kalit-) “firm, brave; firmness, lock, enclosure’. Cf. kal- and kaldhos,
=== leaf 267 ===
 and see WP I, 357 & 442 MIr calath, calad “hard, firm, solid’; m. “har- bour; sound of water, shore; Ir. calad, id.; Gaul. caleto- “hard, brave’; W caled ‘hard’; Br. kalet, Cor. calez, id.; DW in Sp. caleta "bar, bour’; OHG helid, OS helith ‘hero’; OE haelep, id.; ON holdr *man, squire'
kalitero-, extn. of kal- (2), q. v. Alb. i kaltër ‘blue’; Du. helder ‘bright, dear
kalk- ‘bend, corner; knee, hock’. Cf. WP II, 599 and kələk- Lat. calx, gs calcis ‘heel; butt-end; kick’; OE healh ‘nook, recess, small hollow’; Finn. LW kolkka (‘corner’. Vowel? See kolquos)
kalos (kāl-) (1) “dry, leap’. Per. (ambig.) kar ‘deaf; Gk. cf. kēlós ‘parched’; këlon, Dor. -ã- ‘timber’; Lat. (ambig.) callus & callum (‘hardness’, but cf. kaldh-); OHG hal ‘withered’; LG haal, id. beside halig ‘ripe; dead-tired'; R (*-à-) kalit (2) ‘dry’; Srb. kaliti ‘temper steel: Pol. cf. kal-eki ‘crippled’; Ukr. kal-ika, f. ‘cripple’; Li. cf. kalstu, kalsti ‘go dry”: Latv. kalst, id.; R cf. za-kal ‘tempering, hard- ening' (*-à-)
kalos (2) ‘sagacious’. Variants: kalios, kalis. Cf. WP I, 356 l Skt. kalyáh “fit; clever’; Gk. cf. peu-kálimos ‘sagacious’; Lat. callidus ‘wise’ (-11- unex- plained); Umb. kalefu- ‘tame, of oxen’; W call ‘wise, sly’; Cz. cf. ne-kolný ‘stubborn’
kalos, is (1) “black, blackened, stained; stain’. WP I, 441. Cf. qual- (Slav & Skt. am- big.) Skt. (ambig.) kalah ‘black’; Romani kalo, id.; Lat. cf. calo, gs -onis 'camp-follower'; cal-1go ‘darkness’; càl-umnia ‘blackening of a charac- ter”; Ir. cf. caile (stain, fr. *kal-i-); Gk. kelís, id.; Cz. R kal, Pol. kat (ambig. ‘dung’. Cf. qual-); OE cf. hol *calumny'; cf. Li. kólioti, v. ‘abuse’; dim. extn. in Lat. caliculus *inkpot
kálos, is (2) “easy; ease’ Gk. cf. eú-kelos (Doric: -à-) “easy, quiet, care- free’ beside he-kelos id.; Du. heul ‘comfort’
kals- (1) *hard paving'. Cf. kal-, kalos Lat. callis, m. f. “track, path’; Norw. helle *flag- stone'
kaletos (kalot-, kalit-) — kam- (kom-?)
15
20
25
30
35
40
45
466
kals- (2), form of kal- "hard etc. see kal- (4) and kalos (1) Lat. cf. callus “hard”; calleo, Gre ‘be hard, be tough”; Latv. kalstu, kaist ‘dry, wither; grow lean’; kalsens ‘emaciated’; Li. cf. kalstyti, v. ‘buttress’; Du. cf. be-helzen ‘enclose, contain’
kaltos, à (1) “pile, heap' Skt. cf. kattayami ‘pile up”; Br. kalzen ‘heap’; kalza, v. ‘pile’; Cor. calz, calj (-£), id.; G Halde (2) “pile of ore?
kaltos, à (2) (koltos?) ‘leaning; lean, slope, declivity'. Cf. WP I, 430 Skt. cf. katakab (dim. type: ‘slope’); OHG hald ‘inclined’
```


## [2026-09-06T16:09:32.684Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -c \"کلنگ\" $f; grep -n \"کلند\" $f | head -5; done"
}
```


### [2026-09-06T16:09:34.349Z] TOOL RESULT

```
== MON_part1.txt
8
23183:کلند» مفتاح» بنگ. 
== MON_part2.txt
9
4615:صاحب فال گوید. فال کلند: شخصی سر و 
4617:رود و غربالی یا کلندی همراه برد و غربال را 
4618:بر کلند نوازد. صاحب خانه چیزی از ما کول 
22371:بیضی شکلند. . تخم‌ها با مدفوع خارج 
24042:پناهگاه او را با کلند و تبر بتدریج وسیعتر
```


## [2026-09-06T16:09:34.540Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY کلنگ ==\"; grep -n \"کلنگ\\|کلند\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY کاسه/کوزه ==\"; grep -n \"کوزه\\|کاسه\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY چرمه ==\"; grep -n \"چرمه\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T16:09:34.620Z] TOOL RESULT

```
== ARY کلنگ ==
1971:۱- معنی این واژه در هند و اروپایی و اکثر زبان‌های دیگر: کلنگ؛ پفکهه" 6
== ARY کاسه/کوزه ==
7192:خم» خمّب» خمّبه غحنب (به چم "خمره"» *کوزه) / ۲۴۵ ‌
7197:فارسی (/885140: خم, حَمُب, خعبه, خنب (به چم آخمره: آکوزه)
13143:چم‌های این واژه در زبان‌های غیرایرانی: کاسه» ظرف گرد و گنبد مانند؛ فرورفتگی گرد به شکل کاسه» سس کله. ۱
== ARY چرمه ==
```


## [2026-09-06T16:09:44.575Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,50p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-06T16:09:44.618Z] TOOL RESULT

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
```


## [2026-09-06T16:09:49.951Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/columba#Latin\" \\\n \"https://en.wiktionary.org/wiki/κόλυμβος\" \\\n \"https://en.wiktionary.org/wiki/calix#Latin\" \\\n \"https://en.wiktionary.org/wiki/κύλιξ\" \\\n \"https://en.wiktionary.org/wiki/gladius#Latin\" \\\n \"https://en.wiktionary.org/wiki/calamitas#Latin\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 252 verification (Kel 4 columba; Kel 5 calix/kylix; Kel 6 gladius/calamitas)\"; done"
}
```


### [2026-09-06T16:09:56.242Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/columba#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/015096e19c620557.txt
### https://en.wiktionary.org/wiki/κόλυμβος
/home/sfmqrb/git/rishe/data/verification/sources/web/b1108df87f62460f.txt
### https://en.wiktionary.org/wiki/calix#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/13ca7d09292c7378.txt
### https://en.wiktionary.org/wiki/κύλιξ
/home/sfmqrb/git/rishe/data/verification/sources/web/c4169f520f6677fb.txt
### https://en.wiktionary.org/wiki/gladius#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/6b7216a01189ba06.txt
### https://en.wiktionary.org/wiki/calamitas#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/41fb24c8e6f1c5a3.txt
```


## [2026-09-06T16:09:58.874Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 015096e19c620557 b1108df87f62460f 13ca7d09292c7378 c4169f520f6677fb 6b7216a01189ba06 41fb24c8e6f1c5a3; do echo \"###### $f\"; grep -n -A14 \"^Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-06T16:10:01.482Z] TOOL RESULT

```
###### 015096e19c620557
###### b1108df87f62460f
###### 13ca7d09292c7378
###### c4169f520f6677fb
###### 6b7216a01189ba06
###### 41fb24c8e6f1c5a3
```


## [2026-09-06T16:10:03.531Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 015096e19c620557.txt && head -c 800 015096e19c620557.txt"
}
```


### [2026-09-06T16:10:03.580Z] TOOL RESULT

```
5479 015096e19c620557.txt
URL: https://en.wiktionary.org/wiki/columba#Latin
FETCHED: 2026-09-06T16:09:52Z
STATUS: 200
TITLE: columba - Wiktionary, the free dictionary

columba - Wiktionary, the free dictionary 

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
 Latin 

 Toggle Latin subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Declension 

 1.4.2 
 Related terms 

 1.4.3 
 Descendants 

 1.5 
 See also 

 1.6
```


## [2026-09-06T16:10:06.793Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '60,200p' 015096e19c620557.txt"
}
```


### [2026-09-06T16:10:06.833Z] TOOL RESULT

```
 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Declension 

 1.4.2 
 Related terms 

 1.4.3 
 Descendants 

 1.5 
 See also 

 1.6 
 References 

 2 
 Romansh 

 Toggle Romansh subsection 

 2.1 
 Etymology 

 2.2 
 Noun 

 Toggle the table of contents 

 columba 

 26 languages 

 Azərbaycanca 
 Čeština 
 Deutsch 
 Ελληνικά 
 Esperanto 
 Español 
 Eesti 
 Euskara 
 Suomi 
 Français 
 Galego 
 Magyar 
 Italiano 
 日本語 
 한국어 
 Lietuvių 
 Malagasy 
 Nederlands 
 Norsk bokmål 
 Polski 
 Română 
 Русский 
 Sängö 
 தமிழ் 
 Türkçe 
 中文 

 Entry 

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

 See also: Columba and columbă 

 Latin
 [ edit ] 

 English Wikipedia has an article on: columba 

 Wikipedia 

 columba 
 Alternative forms
 [ edit ] 

 colonbu ( Vulgar Latin ) 

 Etymology
 [ edit ]
```


## [2026-09-06T16:10:09.314Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '200,400p' 015096e19c620557.txt"
}
```


### [2026-09-06T16:10:09.354Z] TOOL RESULT

```
 [ edit ] 

 From Ancient Greek κόλυμβος ( kólumbos , “ a diver ” ) , from κολυμβάω ( kolumbáō , “ dive, plunge headlong, swim ” ) . (Aristophanes [ Birds, 304 ] and others use the word κολυμβίς ( kolumbís , “ diver, sea-bird ” ) .)

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [kɔˈɫʊm.ba] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [koˈlum.ba] 

 Noun
 [ edit ] 

 columba   f ( genitive columbae , masculine columbus ) ; first declension 

 dove , pigeon 

 a term of endearment 

 Declension
 [ edit ] 

 First-declension noun.

 singular

 plural

 nominative 

 columba 

 columbae 

 genitive 

 columbae 

 columbārum 

 dative 

 columbae 

 columbīs 

 accusative 

 columbam 

 columbās 

 ablative 

 columbā 

 columbīs 

 vocative 

 columba 

 columbae 

 Related terms
 [ edit ] 

 columbārium 
 columbārius 
 columbīnus 
 columbus 

 Descendants
 [ edit ] 

 Catalan: coloma 

 Galician: comba 

 Italian: colomba 

 Occitan: colomba 

 Romanian: columbă 

 Romansh: columba 

 Sicilian: culumma 

 Borrowings 
 → English: Columba 

 → French: Colombe 

 → Old Irish: columb , colum Middle Irish: colum Irish: colm 
 Manx: colum 
 Scottish Gaelic: calum 

 → Spanish: Columba 

 → Translingual: Columba 

 → Welsh: colomen 

 See also
 [ edit ] 

 palumbus 

 References
 [ edit ] 

 “ columba ”, in Charlton T. Lewis and Charles Short ( 1879 ), A Latin Dictionary , Oxford: Clarendon Press 

 “ columba ”, in Charlton T. Lewis ( 1891 ), An Elementary Latin Dictionary , New York: Harper & Brothers 

 " columba ", in Charles du Fresne du Cange, Glossarium Mediæ et Infimæ Latinitatis (augmented edition with additions by D. P. Carpenterius, Adelungius and others, edited by Léopold Favre, 1883–1887)

 “ columba ”, in Gaffiot, Félix ( 1934 ), Dictionnaire illustré latin-français , Hachette. 

 “ columba ”, in William Smith, editor ( 1854, 1857 ), A Dictionary of Greek and Roman Geography , volume 1 & 2 , London: Walton and Maberly 

 Romansh
 [ edit ] 

 Etymology
 [ edit ] 

 From Latin columba .

 Noun
 [ edit ] 

 columba   f ( plural columbas )

 dove , pigeon 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=columba&oldid=90746025 "

 Categories : Latin terms borrowed from Ancient Greek 
 Latin terms derived from a Pre-Greek substrate 
 Latin terms derived from Ancient Greek 
 Latin 3-syllable words 
 Latin terms with IPA pronunciation 
 Latin lemmas 
 Latin nouns 
 Latin first declension nouns 
 Latin feminine nouns in the first declension 
 Latin feminine nouns 
 la:Columbids 
 Romansh terms inherited from Latin 
 Romansh terms derived from Latin 
 Romansh terms derived from a Pre-Greek substrate 
 Romansh terms derived from Ancient Greek 
 Romansh lemmas 
 Romansh nouns 
 Romansh feminine nouns 
 rm:Columbids 

 Hidden categories: Pages with etymon 
 Latin entries with etymon 
 Pages using etymon with no ID 
 Pages with entries 
 Pages with 2 entries 
 Romansh entries with etymon 

 This page was last edited on 11 May 2026, at 17:30.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 columba 

 26 languages 

 Add topic
```


## [2026-09-06T16:10:21.798Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in b1108df87f62460f c4169f520f6677fb 13ca7d09292c7378 6b7216a01189ba06 41fb24c8e6f1c5a3; do echo \"###### $f\"; awk '/Etymology/,/Retrieved from/' $f.txt | grep -v \"^ *$\" | head -40; echo; done"
}
```


### [2026-09-06T16:10:23.785Z] TOOL RESULT

```
###### b1108df87f62460f
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Inflection 
 1.3.2 
 Derived terms 
 1.3.3 
 Descendants 
 1.4 
 References 
 1.5 
 Further reading 
 Toggle the table of contents 
 κόλυμβος 
 4 languages 
 Ελληνικά 
 Français 
 한국어 
 Русский 
 Entry 
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

###### c4169f520f6677fb
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 1.4.1 
 Declension 
 1.4.2 
 Derived terms 
 1.4.3 
 Descendants 
 1.5 
 Further reading 
 Toggle the table of contents 
 κύλιξ 
 5 languages 
 Ελληνικά 
 Eesti 
 Français 
 Italiano 
 Malagasy 
 Entry 
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

###### 13ca7d09292c7378
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.3.1 
 Declension 
 2.3.2 
 Descendants 
 2.4 
 References 
 2.5 
 Further reading 
 Toggle the table of contents 
 calix 
 16 languages 
 Català 
 Deutsch 
 Esperanto 
 Eesti 
 Suomi 
 Français 
 Magyar 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Português 
 Русский 
 தமிழ் 
 Tiếng Việt 
 中文 
 Entry 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools

###### 6b7216a01189ba06
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Translations 
 2 
 Dutch 
 Toggle Dutch subsection 
 2.1 
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.3.1 
 Usage notes 
 2.3.2 
 See also 
 3 
 Finnish 
 Toggle Finnish subsection 
 3.1 
 Etymology 
 3.2 
 Pronunciation 
 3.3 
 Noun 
 3.3.1 
 Declension 
 3.3.2 
 Related terms 
 4 
 Latin 
 Toggle Latin subsection 
 4.1 
 Etymology 
 4.2 
 Pronunciation 

###### 41fb24c8e6f1c5a3
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.3.2 
 Derived terms 
 1.3.3 
 Descendants 
 1.4 
 References 
 2 
 Spanish 
 Toggle Spanish subsection 
 2.1 
 Noun 
 Toggle the table of contents 
 calamitas 
 7 languages 
 Deutsch 
 Eesti 
 Français 
 한국어 
 Kurdî 
 Malagasy 
 Русский 
 Entry 
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
```


## [2026-09-06T16:10:28.141Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in b1108df87f62460f c4169f520f6677fb 13ca7d09292c7378 6b7216a01189ba06 41fb24c8e6f1c5a3; do echo \"###### $f\"; awk '/^ From Wiktionary, the free dictionary/,0' $f.txt | grep -v \"^ *$\" | head -60; echo; done"
}
```


### [2026-09-06T16:10:29.947Z] TOOL RESULT

```
###### b1108df87f62460f
 From Wiktionary, the free dictionary
 Ancient Greek
 [ edit ] 
 Etymology
 [ edit ] 
 Possibly borrowed from Pre-Greek . [ 1 ] Compare Latin columba ( “ dove ” ) , which may be a borrowing from Greek. Also compare with Proto-Slavic *kъlpь ( “ swan ” ) . Compare also Proto-Nuristani *carāmba ( “ parrot ” ) and Old Armenian սալամբ ( salamb ) .
 According to Beekes, κολῠμβᾰ́ω ( kolŭmbắō , “ to dive ” ) is a denominative verbal derivation.
 Pronunciation
 [ edit ] 
 IPA ( key ) : /kó.lym.bos/ → /ˈko.lym.bos/ → /ˈko.lim.bos/ 
 ( 5 th BCE Attic ) IPA ( key ) : /kó.lym.bos/ 
 ( 1 st CE Egyptian ) IPA ( key ) : /ˈko.lym.bos/ 
 ( 4 th CE Koine ) IPA ( key ) : /ˈko.lym.bos/ 
 ( 10 th CE Byzantine ) IPA ( key ) : /ˈko.lym.bos/ 
 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈko.lim.bos/ 
 Hyphenation: κό‧λῠμ‧βος 
 Noun
 [ edit ] 
 κόλῠμβος • ( kólŭmbos )  m ( genitive κόλῠμβου ) ; second declension 
 alternative form of κολυμβῐ́ς ( kolumbĭ́s , “ diver; little grebe ( Podiceps minor ) ” ) 
 alternative form of κολύμβησῐς ( kolúmbēsĭs , “ pearl fishing ” ) 
 alternative form of κολυμβήθρᾱ ( kolumbḗthrā , “ place for swimming ” ) 
 Inflection
 [ edit ] 
 Second declension of ὁ κόλῠμβος ; τοῦ κολῠ́μβου ( Attic )
 Case / #
 Singular
 Dual
 Plural
 Nominative
 ὁ κόλῠμβος 
 ho kólŭmbos 
 τὼ κολῠ́μβω 
 tṑ kolŭ́mbō 
 οἱ κόλῠμβοι 
 hoi kólŭmboi 
 Genitive
 τοῦ κολῠ́μβου 
 toû kolŭ́mbou 
 τοῖν κολῠ́μβοιν 
 toîn kolŭ́mboin 
 τῶν κολῠ́μβων 
 tôn kolŭ́mbōn 
 Dative
 τῷ κολῠ́μβῳ 
 tōî kolŭ́mbōi 
 τοῖν κολῠ́μβοιν 
 toîn kolŭ́mboin 
 τοῖς κολῠ́μβοις 
 toîs kolŭ́mbois 
 Accusative
 τὸν κόλῠμβον 
 tòn kólŭmbon 
 τὼ κολῠ́μβω 
 tṑ kolŭ́mbō 
 τοὺς κολῠ́μβους 
 toùs kolŭ́mbous 
 Vocative
 κόλῠμβε 
 kólŭmbe 

###### c4169f520f6677fb
 From Wiktionary, the free dictionary
 Ancient Greek
 [ edit ] 
 Alternative forms
 [ edit ] 
 κῠλῐ́σκη ( kŭlĭ́skē ) 
 Etymology
 [ edit ] 
 Traditionally compared to Latin calix ( “ deep bowl; cup ” ) but a variation *a/u is unknown in Indo-European words. For the same reason, κᾰ́λῠξ ( kắlŭx , “ husk ” ) is not identical with this word. The presence of the variation leads to a Pre-Greek origin, as well as the typical Pre-Greek suffix -ικ- ( -ik- ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ký.liks/ → /ˈcy.liks/ → /ˈci.liks/ 
 ( 5 th BCE Attic ) IPA ( key ) : /ký.liks/ 
 ( 1 st CE Egyptian ) IPA ( key ) : /ˈky.liks/ 
 ( 4 th CE Koine ) IPA ( key ) : /ˈcy.liks/ 
 ( 10 th CE Byzantine ) IPA ( key ) : /ˈcy.liks/ 
 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈci.liks/ 
 Noun
 [ edit ] 
 κῠ́λῐξ • ( kŭ́lĭx )  f ( genitive κῠ́λῐκος ) ; third declension 
 a cup ( often for wine ) 
 Declension
 [ edit ] 
 Third declension of ἡ κῠ́λῐξ ; τῆς κῠ́λῐκος ( Attic )
 Case / #
 Singular
 Dual
 Plural
 Nominative
 ἡ κῠ́λῐξ 
 hē kŭ́lĭx 
 τὼ κῠ́λῐκε 
 tṑ kŭ́lĭke 
 αἱ κῠ́λῐκες 
 hai kŭ́lĭkes 
 Genitive
 τῆς κῠ́λῐκος 
 tês kŭ́lĭkos 
 τοῖν κῠλῐ́κοιν 
 toîn kŭlĭ́koin 
 τῶν κῠλῐ́κων 
 tôn kŭlĭ́kōn 
 Dative
 τῇ κῠ́λῐκῐ 
 tēî kŭ́lĭkĭ 
 τοῖν κῠλῐ́κοιν 
 toîn kŭlĭ́koin 
 ταῖς κῠ́λῐξῐ / κῠ́λῐξῐν 
 taîs kŭ́lĭxĭ(n) 
 Accusative
 τὴν κῠ́λῐκᾰ 
 tḕn kŭ́lĭkă 
 τὼ κῠ́λῐκε 
 tṑ kŭ́lĭke 
 τᾱ̀ς κῠ́λῐκᾰς 
 tā̀s kŭ́lĭkăs 
 Vocative
 κῠ́λῐξ 
 kŭ́lĭx 
 κῠ́λῐκε 

###### 13ca7d09292c7378
 From Wiktionary, the free dictionary
 See also: Calix and cálix 
 English
 [ edit ] 
 Noun
 [ edit ] 
 calix ( plural calixes or calices ) 
 Archaic spelling of calyx .
 Derived terms
 [ edit ] 
 glycocalix 
 References
 [ edit ] 
 “ calix ”, in Webster’s Revised Unabridged Dictionary , Springfield, Mass.: G. & C. Merriam , 1913 , →OCLC . 
 Latin
 [ edit ] 
 Etymology
 [ edit ] 
 In view of Umbrian skalçeta ( “ sacrifical vessel ” ) , perhaps from a Proto-Italic *(s)kalik- , [ 1 ] from a Proto-Indo-European *(s)kel- ( “ a kind of vessel ” ) , and compared with Ancient Greek σκάλλιον ( skállion , “ small cup ” ) , σκαλίς ( skalís , “ shovel ” ) . [ 1 ] Pokorny considered a parallel formation in Sanskrit कलश ( kaláśa- , “ (water-)jar, tub, pot, dish ” ) , for Proto-Indo-European *kel-eḱ- , [ 2 ] but De Vaan finds this unlikely. Alternatively, borrowed from Ancient Greek κύλιξ ( kúlix , “ drinking cup ” ) or an unattested variant thereof, maybe with contamination from κάλυξ ( kálux , “ shell, hull ” ) , but it is also possible that all were borrowed from related substrate words. [ 1 ] 
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈka.lɪks] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈkaː.liks] 
 Homophone : calyx ( pronunciations of ⟨y⟩ as /i/ ) 
 Noun
 [ edit ] 
 calix   m ( genitive calicis ) ; third declension 
 cup , chalice 
 cooking pot 
 small pipe 
 Declension
 [ edit ] 
 Third-declension noun.
 singular
 plural
 nominative 
 calix 
 calicēs 
 genitive 
 calicis 
 calicum 
 dative 
 calicī 
 calicibus 
 accusative 
 calicem 
 calicēs 
 ablative 
 calice 
 calicibus 
 vocative 
 calix 
 calicēs 
 Descendants
 [ edit ] 
 Asturian: calce , cálcer , cálcere 
 Italian: calice 
 Old Occitan: 
 Catalan: calze 
 Occitan: calici 

###### 6b7216a01189ba06
 From Wiktionary, the free dictionary
 English
 [ edit ] 
 English Wikipedia has an article on: gladius 
 Wikipedia 
 English Wikipedia has an article on: gladius (cephalopod) 
 Wikipedia 
 Etymology
 [ edit ] 
 From Latin gladius ( “ Roman short sword, gladius ” ) . Doublet of glaive .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ˈɡlæd.i.əs/ 
 Noun
 [ edit ] 
 gladius ( plural gladiuses or gladii ) 
 ( historical ) A Roman sword roughly two feet long.
 1882 , “ The Genesis of the Sword ”, in Popular Science Monthly , volume 21 , page 81 : Finally, the Romans made the gladius —sharp, of highly-tempered steel, and strongly piercing—the first real sword (Figs. 17, 18, 19), of which only five specimens are now known to exist. 
 2007 , Pat Southern, The Roman Army: A Social and Institutional History , page 212 : The gladius was effective either for cutting or for thrusting and was used by legionaries and auxiliaries. 
 ( zoology ) A pen , a hard internal bodypart of certain cephalopods , made of chitin -like material.
 2017 October 31, Mark Carnall, The Guardian ‎ [1] : From the Cretaceous of North America fossilised gladii in the enigmatic genus Tusoteuthis have been estimated to give a mantle length (body size) of 1.8m, just less than that of the giant squid’s. 
 Translations
 [ edit ] 
 Roman sword
 Arabic: غْلَادِيُوس   m ( ḡlādiyus ) 
 Dutch: gladius   (nl)   m 
 Finnish: gladius 
 Latin: gladius   (la)   m 
 Marathi: ग्लेडियस   f ( gleḍiyas ) 
 Old English: sweord   n 
 Polish: gladius   (pl)   m 
 Portuguese: gládio   (pt)   m 
 zoology: internal skeleton of squid
 Finnish: selkäkilpi 
 Polish: gladius   (pl)   m 
 Portuguese: gládio   (pt)   m 
 Dutch
 [ edit ] 
 Etymology
 [ edit ] 
 Gladius. 
 From Latin gladius ( “ Roman short sword, gladius ” ) .
 Pronunciation
 [ edit ] 
 Audio : ( file ) 
 Noun
 [ edit ] 
 gladius   m ( plural gladii , diminutive gladiusje   n ) 
 Roman short sword ; gladius
 Hypernym: kortzwaard 
 Usage notes
 [ edit ] 
 Like many Dutch words borrowed from Latin, the plural takes the form of the Latin nominative plural.
 See also
 [ edit ] 
 spatha 
 Finnish
 [ edit ] 
 Etymology
 [ edit ] 

###### 41fb24c8e6f1c5a3
 From Wiktionary, the free dictionary
 Latin
 [ edit ] 
 Etymology
 [ edit ] 
 According to Schrijver, probably built from an unattested adjective *calamis or *calamus + -tās . This same base adjective is probably also continued by incolumis . According to this theory, the second syllable was not syncopated due to the influence of the adjective from which it derived. Schrijver connects this adjective to the root Proto-Indo-European *kelh₂- ( “ to beat ” ) , suggesting perhaps a pre-form of the shape *kelh₂-mo- , which would yield *kela-mo- with the vocalization of the laryngeal and eventually *cala-mo- with a sound change of *e > *a after a pure velar (compare also scandō ( “ to jump ” ) for a possible example of a similar development). Regarding the ablaut grade of this PIE adjective, Schrijver compares Ancient Greek θερμός ( thermós , “ warm ” ) (< *gʷʰer-mo-s ). Alternatively, Schrijver suggests that it may reflect an *m -stem adjective of the shape *kl̥h₂-em- , though he concedes that there are no other known adjectives of this type. However, terms of a similar structure are attested in nouns, such as Ancient Greek κάλαμος ( kálamos , “ reed ” ) . [ 1 ] This second proposal is supported by De Vaan, who considers there to be no other good explanation for the initial ca- . [ 2 ] An old form by l - d -alternation is Old Latin kadamitās .
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [kaˈɫa.mɪ.taːs] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [kaˈlaː.mi.tas] 
 Noun
 [ edit ] 
 calamitās   f ( genitive calamitātis ) ; third declension 
 loss , damage , harm 
 Synonyms: damnum , dētrīmentum , incommoditās , iniūria , vulnus , noxa , maleficium , pauperiēs , fraus , āmissiō 
 Antonyms: beneficium , favor 
 misfortune , calamity , disaster 
 Synonyms: plāga , miseria , incommodum , dētrīmentum , clādēs , perniciēs , exitium , incommoditās , interitus , īnfortūnium , cruciātus , cāsus , malum 
 Antonyms: commodum , commoditās 
 63 BCE , Cicero , In Catilinam orationes 1.11 : [ … ] dēnique, quotiēnscumque mē petīstī, per mē tibi obstitī, quamquam vidēbam perniciem meam cum magnā calamitāte reī pūblicae esse coniūnctam. In short, as often as you attacked me, I opposed you by my own efforts, although I saw that my ruin was connected with great disaster for the Republic. 
 military defeat 
 Synonyms: clādēs , incommodum , dētrīmentum , vulnus 
 Antonym: victōria 
 blight , crop failure 
 Declension
 [ edit ] 
 Third-declension noun.
 singular
 plural
 nominative 
 calamitās 
 calamitātēs 
 genitive 
 calamitātis 
 calamitātum 
 dative 
 calamitātī 
 calamitātibus 
 accusative 
 calamitātem 
 calamitātēs 
 ablative 
 calamitāte 
 calamitātibus 
 vocative 
 calamitās 
 calamitātēs 
 Derived terms
 [ edit ] 
 calamitōsus 
 Descendants
 [ edit ] 
 Aragonese: calamidat 
 Asturian: calamidá 
 Catalan: calamitat 
 Emilian: calamitè 
 English: calamity 
 French: calamité 
 Friulian: calamitât 
 Galician: calamidade
```


## [2026-09-06T16:10:40.122Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Latin$/,/^ Old French/' 6b7216a01189ba06.txt | grep -v \"^ *$\" | head -30"
}
```


### [2026-09-06T16:10:42.016Z] TOOL RESULT

```
 Latin
 [ edit ] 
 gladius 
 Etymology
 [ edit ] 
 Possibly from Gaulish *kladyos ( “ sword ” ) , from Proto-Celtic *kladiwos ( “ sword ” ) (compare Old Irish claideb ( “ sword ” ) , Welsh cleddyf ( “ sword ” ) from Proto-Indo-European *kelh₂- ( “ to beat, break ” ) ). [ 1 ] Cognate with Latin clādēs , clāva , percellō .
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈɡɫa.di.ʊs] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈɡlaː.di.us] 
 Noun
 [ edit ] 
 gladius   m ( genitive gladiī or gladī ) ; second declension 
 sword 
 Synonyms: ēnsis , mucrō , spatha 
 Mitte gladium in vaginam. ― Put the sword into its sheath. 
 in gladium incumbere ― to fall on one's sword 
 8 CE , Ovidius , Fasti 2.101 : quid tibi cum gladiō ? What are you doing with a sword ? 
 ( figuratively ) murder , death 
 Synonym: mors 
 a gladiatorial contest 
 swordfish 
 Synonym: xiphiās 
 Declension
 [ edit ] 
 Second-declension noun.
 singular
 plural
 nominative 
 gladius
```


## [2026-09-06T16:10:42.600Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/كأس\" \\\n \"https://en.wiktionary.org/wiki/کاسه\" \\\n \"https://en.wiktionary.org/wiki/کوزه\" \\\n \"https://en.wiktionary.org/wiki/کلنگ\" \\\n \"https://en.wiktionary.org/wiki/κλών\" \\\n \"https://www.etymonline.com/word/clone\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 252 verification (Kel 5 kase/kuze/kas; Kel 6 kolang, klon/clone)\"; done"
}
```


### [2026-09-06T16:10:52.400Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/كأس
/home/sfmqrb/git/rishe/data/verification/sources/web/724674b0abe31773.txt
### https://en.wiktionary.org/wiki/کاسه
/home/sfmqrb/git/rishe/data/verification/sources/web/15abe6f767be23b7.txt
### https://en.wiktionary.org/wiki/کوزه
/home/sfmqrb/git/rishe/data/verification/sources/web/09c738b87de63f09.txt
### https://en.wiktionary.org/wiki/کلنگ
/home/sfmqrb/git/rishe/data/verification/sources/web/1a868c8cb9b965ef.txt
### https://en.wiktionary.org/wiki/κλών
/home/sfmqrb/git/rishe/data/verification/sources/web/8010838e4078cf92.txt
### https://www.etymonline.com/word/clone
/home/sfmqrb/git/rishe/data/verification/sources/web/0e3b45e8a2070753.txt
```


## [2026-09-06T16:10:55.481Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 724674b0abe31773 15abe6f767be23b7 09c738b87de63f09 1a868c8cb9b965ef 8010838e4078cf92 0e3b45e8a2070753; do echo \"###### $f\"; awk '/^ From Wiktionary, the free dictionary/,0' $f.txt | grep -v \"^ *$\" | head -45; echo; done"
}
```


### [2026-09-06T16:10:57.388Z] TOOL RESULT

```
###### 724674b0abe31773
 From Wiktionary, the free dictionary
 See also: کاش , گاش , and کاس 
 Arabic
 [ edit ] 
 Root 
 ك ء س ( k ʔ s ) 
 1 term 
 Etymology
 [ edit ] 
 Has been envisioned as from Proto-Semitic *kaʔs- . The Arabic form could be a hypercorrection after a borrowing from the Aramaic  forms listed under it however, since inheritance of Akkadian 𒃲 ( kāsum ) from such a proto-form is irregular as one expects vocalism like in Akkadian 𒊕 ( rēšum ) from Proto-Semitic *raʔš- , so also considering the absence in Ethiopian Semitic  one may conclude a post-Proto-Semitic external borrowing.
 Pronunciation
 [ edit ] 
 IPA ( key ) : /kaʔs/ 
 Noun
 [ edit ] 
 كَأْس • ( kaʔs )  f ( plural كُؤُوس ( kuʔūs ) or أَكْؤُس ( ʔakʔus ) or كِئَاس ( kiʔās ) ) 
 a glass , especially a wine glass or arak glass
 a cup , goblet , tumbler 
 a cup trophy
 كَأْس العَالَمِ ― kaʔs al-ʕālami ― world cup 
 Declension
 [ edit ] 
 Declension of noun كَأْس ( kaʔs )
 singular
 basic singular triptote 
 indefinite
 definite
 construct
 informal
 كَأْس 
 kaʔs 
 الْكَأْس 
 al-kaʔs 
 كَأْس 
 kaʔs 
 nominative
 كَأْسٌ 
 kaʔsun 
 الْكَأْسُ 
 al-kaʔsu 
 كَأْسُ 
 kaʔsu 
 accusative
 كَأْسًا 
 kaʔsan 

###### 15abe6f767be23b7
 From Wiktionary, the free dictionary
 See also: كاسة and كاسه 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( *kʾsk' /⁠kāsag⁠/ ) (compare Baluchi کاسگ ( kāsag , “ bowl ” ) ), possibly from Old Persian 𐎣𐎠𐎿𐎣 ( kāsaka , “ semi-precious stone, glass ” ) , or perhaps related to Sanskrit कोश ( kośa , “ pot, cask, cup ” ) . Likely not related to Sanskrit काच ( kāca , “ glass ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /kaː.ˈsa/ 
 ( Dari, formal ) IPA ( key ) : [kʰɑː.sá] 
 ( Dari, formal ) IPA ( key ) : [kʰɑː.sá] 
 ( Kabuli ) IPA ( key ) : [kʰɑː.sá] 
 ( Hazaragi ) IPA ( key ) : [kʰɔː.sá] 
 ( Iran, formal ) IPA ( key ) : [kʰɒː.sé] 
 ( Tajik, formal ) IPA ( key ) : [kʰɔ.sá] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 kāsa
 Dari reading ? 
 kāsa
 Iranian reading ? 
 kâse
 Tajik reading ? 
 kosa
 Audio ( Iran ) : ( file ) 
 Noun
 [ edit ] 
 کاسه • ( kāsa / kâse ) ( plural کاسه‌ها ( kāsa-hā / kâse-hâ ) , Tajik spelling коса ) 
 bowl 
 Derived terms
 [ edit ] 
 کاسه سر ( kâse-ye sar ) 
 کاسه‌گر ( kâse-gar ) 
 کاسه و کوزه ( kâse-o-kuze ) 
 Descendants
 [ edit ] 
 Tajik: коса ( kosa ) 
 → Armenian: քասա ( kʻasa ) 
 → Azerbaijani: kasa 
 → Bashkir: каса ( kasa ) 
 → Kazakh: кесе ( kese ) 
 → Northern Kurdish: kas , kase 
 → Kyrgyz: кесе ( kese ) 

###### 09c738b87de63f09
 From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: کوزه 
 Wikipedia fa 
 یک کوزه‌ی لعاب‌دار ― a glazed pottery vase 
 Etymology 1
 [ edit ] 
 Akin to Old Armenian կուժ ( kuž ) , Rutul кӏуж ( ḳuž ) , Classical Syriac ܟܘܙܐ ( kūzā ) , Arabic كُوز ( kūz ) , Iranian borrowings. Related to کوژ ( kuž ) and گوژ ( guž ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /koː.ˈza/ , /kuː.ˈza/ 
 ( Dari, formal ) IPA ( key ) : [kʰoː.zá] 
 ( Dari, formal ) IPA ( key ) : [kʰoː.zá] 
 ( Kabuli ) IPA ( key ) : [kʰoː.zá] 
 ( Hazaragi ) IPA ( key ) : [kʰʊː.zá] 
 ( Iran, formal ) IPA ( key ) : [kʰuː.zé] 
 ( Tajik, formal ) IPA ( key ) : [kʰɵ.zá] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 kōzá, kūzá
 Dari reading ? 
 kōza
 Iranian reading ? 
 kuze
 Tajik reading ? 
 küza
 Noun
 [ edit ] 
 کوزه • ( kōza / kuze ) ( plural کوزه‌ها ( kōza-hā / kuze-hâ ) , Tajik spelling кӯза ) 
 a pottery vase with a long neck
 Synonyms: خُم ( xom ) , خُمره ( xomre ) , سَبو ( sabu ) 
 an urn 
 Derived terms
 [ edit ] 
 فوتِ کوزه‌گری ( fut-e-kuze-gari , literally “ the potter's blow ” ) 
 کوزه‌گر ( kuze-gar , “ potter ” ) 
 کوزه‌گر از کوزه شکسته آب می‌خورد ( kuze-gar az kuze šekaste âb mi-xorad ) 
 کوزه‌گری ( kuze-gari , “ pottery ” ) 
 Descendants
 [ edit ] 
 → Chagatai: کوزه ( kōzä ) 
 Uyghur: كوزا ( koza ) 
 Uzbek: koʻza 

###### 1a868c8cb9b965ef
 From Wiktionary, the free dictionary
 See also: كلنك 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 From Proto-Indo-European *kelh₂- ( “ to beat, strike, break ” ) . Compare کلند ( koland ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ku.ˈlanɡ/ 
 ( Dari, formal ) IPA ( key ) : [kʰʊ.läŋɡ] 
 ( Dari, formal ) IPA ( key ) : [kʰʊ.läŋɡ] 
 ( Kabuli ) IPA ( key ) : [kʰʊ.läŋɡ] 
 ( Hazaragi ) IPA ( key ) : [kʰu.läŋɡ̥] 
 ( Iran, formal ) IPA ( key ) : [kʰo.læɲɡʲ̥] , [kʰo.loɲɡʲ̥] 
 ( Tajik, formal ) IPA ( key ) : [kʰu.läŋɡ] 
 Rhymes: -anɡ 
 Readings
 Classical reading ? 
 kulang
 Dari reading ? 
 kulang
 Iranian reading ? 
 kolang, kolong
 Tajik reading ? 
 kulang
 Noun
 [ edit ] 
 کلنگ • ( kolang, kolong ) 
 pickaxe 
 Alternative forms
 [ edit ] 
 کلنت ( kolant ) ( dialectal , Kerman ) 
 Derived terms
 [ edit ] 
 خانه کلنگی ( xâne-ye kolangi ) 
 Descendants
 [ edit ] 
 → Armenian: քլունգ ( kʻlung , “ pickaxe ” ) 
 → Old Anatolian Turkish: كلنك ( külünk, külüng , “ pickaxe ” ) [since 13 th century] 
 Azerbaijani: külüng 
 Ottoman Turkish: كلنك ( külünk ) , كولونك ( külünk ) Turkish: külünk 
 → Romanian: chilom 
 → Turkmen: külüň 
 Etymology 2

###### 8010838e4078cf92
 From Wiktionary, the free dictionary
 Ancient Greek
 [ edit ] 
 Etymology
 [ edit ] 
 Of uncertain origin. Probably related to κλάδος ( kládos , “ branch, twig ” ) , κλαστός ( klastós , “ broken off ” ) , and κλᾰ́ω ( klắō , “ to break off ” ) , as in English clastic , though Beekes considers this semantically tenuous, as plant twigs and sprouts are not generally considered "broken". He does not offer any alternative explanations, however. [ 1 ] 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /klɔ̌ːn/ → /ˈklon/ → /ˈklon/ 
 ( 5 th BCE Attic ) IPA ( key ) : /klɔ̌ːn/ 
 ( 1 st CE Egyptian ) IPA ( key ) : /ˈklon/ 
 ( 4 th CE Koine ) IPA ( key ) : /ˈklon/ 
 ( 10 th CE Byzantine ) IPA ( key ) : /ˈklon/ 
 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈklon/ 
 Noun
 [ edit ] 
 κλών • ( klṓn )  m ( genitive κλωνός ) ; third declension 
 twig , spray , slip 
 Inflection
 [ edit ] 
 Third declension of ὁ κλών ; τοῦ κλωνός ( Attic )
 Case / #
 Singular
 Dual
 Plural
 Nominative
 ὁ κλών 
 ho klṓn 
 τὼ κλῶνε 
 tṑ klône 
 οἱ κλῶνες 
 hoi klônes 
 Genitive
 τοῦ κλωνός 
 toû klōnós 
 τοῖν κλωνοῖν 
 toîn klōnoîn 
 τῶν κλωνῶν 
 tôn klōnôn 
 Dative
 τῷ κλωνῐ́ 
 tōî klōnĭ́ 
 τοῖν κλωνοῖν 
 toîn klōnoîn 
 τοῖς κλωσῐ́ / κλωσῐ́ν 

###### 0e3b45e8a2070753
```


## [2026-09-06T16:11:16.909Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves\",len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'\\bKa\\W?s\\b|Ka\\'s|Kaʾs|KAʾS|Ka.s\\b', p[:400]) or 'كأس' in p:\n        print(\"leaf\",i,\"printed p\",i-17,\"||\",p[:300].replace('\\n',' '))\nEOF\ngrep -n -i \"cup\\b\" FVQ.txt | head -20"
}
```


### [2026-09-06T16:11:18.897Z] TOOL RESULT

```
leaves 335
8358:filled for him a full cup." 
8373:would mean " a cup pressed out", referring to the wine pressed to 
8374:fill the cup. 
12540:A drinking cup. 
12542:It occurs only in the Joseph story for the king's drinking cup 
12556:Pharaoh's cup in the Joseph story of Gen. xl l in the Ethiopic Bible. 
15311:Cup. 
16432:for the eucharistic cup of mixed water and wine. In fact the Syr. ..lio
```


## [2026-09-06T16:11:22.611Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15300,15340p' FVQ.txt; echo \"== find leaf ==\"; python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Cup.' in p and ('kas' in p.lower() or 'Ka\\'s' in p):\n        print(\"leaf\",i,\"printed\",i-17)\n        print(p[:1400]); break\nEOF"
}
```


### [2026-09-06T16:11:25.397Z] TOOL RESULT

```
Hirschfeld, Beitrage, 38, would derive it from Hebrew, and certainly 
D^p is used in connection with TT in Jewish texts of the oldest 
period, 2 but ]V)O is also commonly used in the same sense and we 
cannot absolutely rule out a Syriac origin for the word. 



(Ka's). 

xxxvii, 44 ; lii, 23 ; Ivi, 18 ; Ixxvi, 5, 17 ; Ixxviii, 34. 

Cup. 

It is found only in early passages in descriptions of the pleasures 
of Paradise. 

This is not a S. Semitic word, as it is entirely lacking in Eth. and 
without a root and of uncertain plu. in Arabic. There can thus be 
little doubt of its Aram, origin. 3 

The Heb. word is 013, while in the Ras Shamra texts we have 



03, and in Aram. 8013, N03, and WO (cf. Ar. j j> ), and 
Syr. V*^- 4 As the Syr. ]fiCO seems to be the source of the Pers. 



1 as-Suyutl, Ih/ 9 324 ; Mutaw, 54. 

2 Fraenkel, Vocab, 23 ; Noldeke-Schwally, i, 184, n. ; and sec Sprcngcr, Leben, 
ii, 204, n. It is noteworthy that the best attested variant reading f\ agrees closely 
in form with DJ(5. See also Horovitz, JPN, 219, who, as a matter of fact, would 
derive the morel ^. also from the Jewish ^!"1. 

3 Fraenkel, Fremdw, 171 ; Zimmern, Akkad. Fremdw, 34. 1). H. Muller, how- 
ever, irZA'J/, i, 27, thinks that the medial Hamza proves it to be genuine Arabie. 

* Cf. also the D2 of the Elephantine papyri (Cowley, Aramaic Papyri, 
No. 61). 
== find leaf ==
leaf 262 printed 245
FOREIGN VOCABULARY OF THE QUR*AN 245
The Commentators are unanimous that the meaning is ^rU))
^ijjl (Tab., Baid., and as-Sijistani, 250), but they were in difficulties
over the form, and there are variants A US, ^J*, and ^rS. Their
trouble in explaining the form is well illustrated by al-'Ukbari, Imld 9 ,
i, 70, for the only possibility is to take it as on the measure
and we have reason to suspect all words of this form. It is not strange,
therefore, in spite of its obvious connection with *S, to find that some
of the authorities took it as a word borrowed from the Syriac. 1
Hirschfeld, Beitrage, 38, would derive it from Hebrew, and certainly
D^p is used in connection with TT in Jewish texts of the oldest
period, 2 but ]V)O is also commonly used in the same sense and we
cannot absolutely rule out a Syriac origin for the word.
(Ka's).
xxxvii, 44 ; lii, 23 ; Ivi, 18 ; Ixxvi, 5, 17 ; Ixxviii, 34.
Cup.
It is found only in early passages in descriptions of the pleasures
of Paradise.
This is not a S. Semitic word, as it is entirely lacking in Eth. and
without a root and of uncertain plu. in Arabic. There can thus be
little doubt of its Aram, origin. 3
The Heb. word is 013, while in the Ras Shamra texts we have
03, and in Aram. 8013, N03, and WO (cf. Ar. j j> ), and
Syr. V*^- 4 As the Syr. ]fiCO seems to be the source of the Pers.
1 as-Suyutl, Ih/ 9 324 ; Mutaw, 54.
2 Fraenkel, Vocab,
```


## [2026-09-06T16:11:33.044Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[263][:1200])\nEOF"
}
```


### [2026-09-06T16:11:35.017Z] TOOL RESULT

```
246 FOREIGN VOCABULARY OF THE QUR^AN
^ufc'i we may take it as most probable that the Arabic also was
borrowed at an early period 2 from the same source.
jjilj (Jfa/iif).
Ixxvi, 5.
Camphor.
The verse is an early one descriptive of the joys of Paradise, where
the Commentators were uncertain whether J^O was the name
of the fountain from which the Blessed drink, or the material used to
temper the drink (cf. Tab. and Baid. on the verse).
It is usually taken as an Arabic word (LA, vi, 465), but the variety
> ' *
of spellmgg jjitf, j^k, jji-J, and jjii would suggest
otherwise, and several of the early authorities noted it as a loan-word
from Persian. 3
The ultimate source is probably to be found in the Munda dialects
of India, whence it passed into Dravidian, e.g. Tamil */fu(>/ni,
Malayalam OgGO, and into Skt., cf. jrfj;. 4 It passed also
into Iranian, where we find Phlv. \$) Mpur,* which
gives the Mod. Pers. j^iw, and Arm. .f>ui^i"-p 9 B and into
Aram, where we find Syr. lioao ? and Maud. K1KDU 8
It is very probable that the Syriac like the Gk. Kafyovpd is from the
Iranian, and Addai Sher, 136, would make the Arabic also a borrowing
from the Persians. The probabilities are, however, that
```


## [2026-09-06T16:11:44.824Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/gladiator\" \\\n \"https://www.etymonline.com/word/calamity\" \\\n \"https://www.etymonline.com/word/columbarium\" \\\n \"https://www.etymonline.com/word/Columbia\" \\\n \"https://en.wiktionary.org/wiki/कलश\" \\\n \"https://en.wiktionary.org/wiki/चरمे\" \\\n \"https://en.wiktionary.org/wiki/چرمه\" \\\n \"https://abadis.ir/fatofa/چرمه/\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 252 verification\"; done"
}
```


### [2026-09-06T16:11:52.338Z] TOOL RESULT

```
### https://www.etymonline.com/word/gladiator
/home/sfmqrb/git/rishe/data/verification/sources/web/c82df06e922f0da9.txt
### https://www.etymonline.com/word/calamity
/home/sfmqrb/git/rishe/data/verification/sources/web/7c7bdb49995a819e.txt
### https://www.etymonline.com/word/columbarium
/home/sfmqrb/git/rishe/data/verification/sources/web/74bb1ffff4e282de.txt
### https://www.etymonline.com/word/Columbia
/home/sfmqrb/git/rishe/data/verification/sources/web/90abb36398180788.txt
### https://en.wiktionary.org/wiki/कलश
/home/sfmqrb/git/rishe/data/verification/sources/web/a2b353cd703f8bf3.txt
### https://en.wiktionary.org/wiki/चरمे
/home/sfmqrb/git/rishe/data/verification/sources/web/5edfe64ce81ee291.txt
### https://en.wiktionary.org/wiki/چرمه
/home/sfmqrb/git/rishe/data/verification/sources/web/6d095a82f9d3e3c1.txt
### https://abadis.ir/fatofa/چرمه/
/home/sfmqrb/git/rishe/data/verification/sources/web/4743c4573f4f3d10.txt
```


## [2026-09-06T16:11:56.174Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c82df06e922f0da9 7c7bdb49995a819e 74bb1ffff4e282de 90abb36398180788; do echo \"###### $f\"; grep -v \"^ *$\" $f.txt | sed -n '1,6p;/Advertisement/,+0d' ; grep -o \"gladiator[^|]\\{0,400\\}\\|calamity[^|]\\{0,400\\}\\|columbarium[^|]\\{0,300\\}\\|Columbia[^|]\\{0,300\\}\" $f.txt | head -3; echo; done"
}
```


### [2026-09-06T16:11:58.171Z] TOOL RESULT

```
###### c82df06e922f0da9
URL: https://www.etymonline.com/word/gladiator
FETCHED: 2026-09-06T16:11:47Z
STATUS: 200
TITLE: Gladiator - Etymology, Origin & Meaning
Gladiator - Etymology, Origin & Meaning 
 Search 
gladiator
gladiator 
gladiator (n.) 

###### 7c7bdb49995a819e
URL: https://www.etymonline.com/word/calamity
FETCHED: 2026-09-06T16:11:47Z
STATUS: 200
TITLE: Calamity - Etymology, Origin & Meaning
Calamity - Etymology, Origin & Meaning 
 Search 
calamity
calamity 
calamity (n.) 

###### 74bb1ffff4e282de
URL: https://www.etymonline.com/word/columbarium
FETCHED: 2026-09-06T16:11:48Z
STATUS: 200
TITLE: Columbarium - Etymology, Origin & Meaning
Columbarium - Etymology, Origin & Meaning 
 Search 
columbarium
columbarium 
columbarium (n.) 

###### 90abb36398180788
URL: https://www.etymonline.com/word/Columbia
FETCHED: 2026-09-06T16:11:48Z
STATUS: 200
TITLE: Columbia - Etymology, Origin & Meaning of the Name
Columbia - Etymology, Origin & Meaning of the Name 
 Search 
Columbia
Columbia - Etymology, Origin & Meaning of the Name
Columbia - Etymology, Origin & Meaning of the Name
```


## [2026-09-06T16:12:00.658Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c82df06e922f0da9 7c7bdb49995a819e 74bb1ffff4e282de 90abb36398180788; do echo \"###### $f\"; grep -v \"^ *$\" $f.txt | sed -n '6,25p'; echo; done"
}
```


### [2026-09-06T16:12:02.844Z] TOOL RESULT

```
###### c82df06e922f0da9
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of gladiator 
 gladiator (n.) 
 mid-15c., "Roman swordsman," from Latin gladiator (fem. gladiatrix ) "fighter in the public games; swordsman," from gladius "sword" (there is no verb *gladiare ), which probably is from Gaulish (compare Welsh cleddyf , Cornish clethe , Breton kleze "sword;" see claymore ). Old Irish claideb is from Welsh.
 The close connection with Celtic words for 'sword', together with the imperfect match of initial consonants, and the semantic field of weaponry, suggests that Latin borrowed a form 
 *gladio- or 
 *kladio- (a hypothetical variant of attested British Celtic 
 *kladimo- 'sword') from [Proto-Celtic] or from a third language. [de Vaan]
 also from mid-15c. 
 Entries linking to gladiator 
 claymore (n.) 
 1749, "two-edged, heavy broadsword of ancient Scottish Highlanders," from Gaelic claidheamh mor "great sword," from claidheb "sword" (compare Welsh cleddyf ), which is possibly from a PIE root *kel- "to strike" (see holt ) + mor "great" (compare Welsh mawr ; see more ).

###### 7c7bdb49995a819e
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps

###### 74bb1ffff4e282de
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of columbarium 
 columbarium (n.) 
 "subterranean sepulchre in ancient Roman places with niches for urns holding remains," 1540s, neuter of Latin columbarius , "dove-cote" (the funereal place so called from resemblance), literally "pertaining to doves;" from columba "dove, pigeon," a word of uncertain origin. Literal sense of "dove-cote" in English is attested from 1881.
 also from 1540s 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 niche 
 1610s, "shallow recess in a wall," from French niche "recess (for a dog), kennel" (14c.), perhaps from Italian nicchia "niche, nook," which is said to be from nicchio "seashell," itself said by Klein, Barnhart, etc. to be probably from Latin mitulus "mussel," but the change of -m
 vault 
 "arched roof or ceiling," c. 1300, vaute, from Old French voute "arch, vaulting, vaulted roof or chamber," from Vulgar Latin *volta, contraction of *volvita, noun use of fem. of *volvitus, alteration of Latin volutus "bowed, arched," past participle of volvere "to turn, turn arou
 recess 

###### 90abb36398180788
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of Columbia 
 Columbia 
 poetic name for United States of America, earlier for the British colonies there, 1730s, also the nation's female personification, from name of Christopher Columbus (also see Colombia ) with Latin "country" ending -ia .
 A popular name for places and institutions in the U.S. in the post-Revolutionary years, when former tributes to king and crown were out of fashion: such as Columbia University (New York, U.S.) founded in 1754 as King's College; re-named 1784. Also District of Columbia (1791, as Territory of Columbia ); " Hail, Columbia, " Joseph Hopkinson's patriotic song that served in 19c. as an unofficial national anthem (1798); "Columbiad," Joel Barlow's attempt to write an epic for the United States (1807). Columbiad also was the name of a heavy, cast-iron, smooth-bore cannon introduced in the U.S. in 1811. Related: Columbian .
 also from 1730s 
 Entries linking to Columbia 
 Colombia 
 South American nation, independent from 1819 as part of Gran Colombia (after its breakup in 1830, known as New Granada , then Colombia from 1863); named for Italian explorer Christopher Columbus (Italian Colombo , Portuguese Colom , Spanish Colón ). Related: Colombian .
 Columbus 
 his name is Latinized from his native Italian Cristoforo Colombo , in Spanish Cristóbal Colón .
 America was discovered accidentally by a great seaman who was looking for something else, and most of the exploration for the next fifty years was done in the hope of getting through or around it. [S.E. Morison, "The Oxford History of the United States," 1965]
```


## [2026-09-06T16:12:11.107Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a2b353cd703f8bf3 6d095a82f9d3e3c1 5edfe64ce81ee291; do echo \"###### $f\"; awk '/^ From Wiktionary, the free dictionary/,0' $f.txt | grep -v \"^ *$\" | head -25; echo; done; echo \"###### abadis\"; grep -v \"^ *$\" 4743c4573f4f3d10.txt | sed -n '1,60p'"
}
```


### [2026-09-06T16:12:12.900Z] TOOL RESULT

```
###### a2b353cd703f8bf3
 From Wiktionary, the free dictionary
 See also: क्लेश and क्लिश् 
 Hindi
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Sanskrit कलश ( kalaśa ) .
 Noun
 [ edit ] 
 कलश • ( kalaś )  m ( Urdu spelling کلش ) 
 pitcher , pot 
 ( Hinduism ) kalasha 
 Declension
 [ edit ] 
 Declension of कलश (masc cons-stem) 
 singular
 plural
 direct
 कलश 
 kalaś 
 कलश 
 kalaś 
 oblique
 कलश 
 kalaś 

###### 6d095a82f9d3e3c1
 From Wiktionary, the free dictionary
 See also: حرمة , حزمة , جزمة , and چزمه 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Compare with Central Kurdish چەرمگ ( çermig , “ white ” ) and the Iranian borrowings: Old Armenian ճերմակ ( čermak , “ white (of a horse) ” ) , Georgian ჭარმაკი ( č̣armaḳi ) , ჭარმაგი ( č̣armagi ) , ჭარმაღი ( č̣armaɣi ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /t͡ʃar.ˈma/ 
 ( Dari, formal ) IPA ( key ) : [t͡ʃʰäɾ.mä] 
 ( Dari, formal ) IPA ( key ) : [t͡ʃʰäɾ.mä] 
 ( Kabuli ) IPA ( key ) : [t͡ʃʰäɾ.mä] 
 ( Hazaragi ) IPA ( key ) : [t͡ʃʰäɾ.mä] 
 ( Iran, formal ) IPA ( key ) : [t͡ʃʰæɹ.me] 
 ( Tajik, formal ) IPA ( key ) : [t͡ʃʰäɾ.mä] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 čarma
 Dari reading ? 
 čarma
 Iranian reading ? 
 čarme
 Tajik reading ? 

###### 5edfe64ce81ee291

###### abadis
URL: https://abadis.ir/fatofa/چرمه/
FETCHED: 2026-09-06T16:11:52Z
STATUS: 200
TITLE: چرمه - معنی در دیکشنری آبادیس
چرمه - معنی در دیکشنری آبادیس 
 دیکشنری مترجم بپرس 
 چرمه
 /Carme/
 مترادف چرمه : اسب، اسب سفید
 دنبال کنید 
 فرهنگ اسم ها
 اسم: چرمه (دختر) (فارسی) (تلفظ: charma) (فارسی: چَرمَه) (انگلیسی: charmah) 
 معنی: اسب به ویژه اسب سفیدرنگ
 برچسب ها: اسم ، اسم با چ ، اسم دختر ، اسم فارسی 
 لغت نامه دهخدا
 چرمه. [ چ َ م َ / م ِ ] ( اِ )مطلق اسب را گویند عموماً. ( برهان ). اسب. ( ناظم الاطباء ). مطلق اسب بهر رنگ و زیور که باشد : 
یکی چرمه ای برنشسته سمند
نکو گامزن باره ای بی گزند. دقیقی.
شوم چرمه گامزن زین کنم 
سپیده دمان جستن کین کنم. فردوسی.
بر آن چرمه تیزرو زین نهاد
چو زین از برش خشک بالین نهاد. فردوسی.
سپه راند و بربست بر چرمه تنگ 
برآمد چو شیری به پشت پلنگ. فردوسی.
که تا زنده ام چرمه جفت منست 
خم چرخ گردان نهفت من است. فردوسی.
سرانجام ترک آن چنان تاخت گرم 
که اززور بر چرمه بنوشت چرم. اسدی.
سلطان یکسواره گردون بجنگ دی 
بر چرمه تنگ بندد و هرا برافکند. خاقانی.
 || اسب سفیدی موی خصوصاً. ( برهان ). اسب خنگ را گویند. ( جهانگیری ) ( انجمن آرا ) ( آنندراج ) ( فرهنگ نظام ). اسب سفیدموی. ( ناظم الاطباء ). اشهب. اسب سپید : 
برانگیخت پس چرمه گرم خیز
درافکند در هندوان رستخیز. اسدی ( از جهانگیری ).
چو ابرش شده چرمه از خون مرد
شده بازچون چرمه ابرش ز گرد. اسدی ( از انجمن آرا ).
ز شبدیز چون شب بیفتاد پست 
برون شدْش چوگان سیمین ز دست 
بزد روز بر چرمه تیزپوی 
بمیدان پیروزه زرینه گوی. اسدی 
اسب چرمه خنگ ضعیف بود، اگر خایه و میان و رانهاء وی و سم و دست و پای و بوش و ناصیه و دم سیاه بود، نیک باشد. ( قابوسنامه ).
دواسبه درآی و رکابی درآور
کزو چرمه صبح یکران نماید. خاقانی ( از جهانگیری ).
رجوع به اشهب شود. || آنچه پسران امرد از صاحب مذاقان گیرند، از نقد و جنس. ( برهان ) ( آنندراج ). نقد و جنسی که امردان بی آبرو و معیوب از فاسق خود گیرند. ( ناظم الاطباء ). || چرمینه را نیز گویند، که کیر کاشی باشد. ( برهان ) ( آنندراج ). چرمینه و کیر کاشی. ( ناظم الاطباء ). مچاچنگ. رجوع به چرمینه و مچاچنگ شود. || مصغر چرم. ( ناظم الاطباء ). رجوع به چرم شود. || قاطر و الاغ سفید. خر و استر سپیدموی : 
از استر صد آرایش بارگاه 
یکی نیمه زآن چرمه دیگر سیاه. اسدی.
هرکرا احمقی تمام بود
خلق گویند مغز خرخورده است 
ور چنین است ، مجد قزوینی بیشتر بخوانید ... 
 فرهنگ فارسی
 دهی از دهستان نیم بلوک بخش قاین شهرستان بیرجند کوهستانی و معتدل ۱۸۳۹ سکنه . آب از قنات محصول : غلات و زعفران . شغل زراعت مالداری و قالیچه بافی .
اسب، مطلق اسب، مخصوصااسب سفید
( اسم ) ۱- اسب ( مطلقا ) . ۲- اسب سفید. ۳- چرمینه مچاچنگ .
دهی از دهستان نیم بلوک بخش قاین شهرستان بیرجند . 
 فرهنگ معین
 (چَ مَ ) (اِ. ) ۱ - اسب . ۲ - اسب سفید. 
 فرهنگ عمید
 اسب، مخصوصاً اسب سفید: سلطان یک سوارۀ گردون به جنگ دی / بر چرمه تنگ بندد و هّرا برافکند (خاقانی: ۱۳۶ ). 
 گویش مازنی
 /charme/ نوعی شلتوک نامرغوب - گوسفندی که بر پا و پوزه و پشتش لکه های سفید دارد ۳گوسفند کبود رنگ
 واژه نامه بختیاریکا
```


## [2026-09-06T16:12:29.479Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/کلنگ/\" \"https://abadis.ir/fatofa/کاسه/\" \"https://abadis.ir/fatofa/کوزه/\" \"https://abadis.ir/fatofa/گلادیاتور/\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 252 verification: Mo'in/Dehkhoda entries\"; done"
}
```


### [2026-09-06T16:12:38.404Z] TOOL RESULT

```
### https://abadis.ir/fatofa/کلنگ/
/home/sfmqrb/git/rishe/data/verification/sources/web/d879225ad5ab1473.txt
### https://abadis.ir/fatofa/کاسه/
/home/sfmqrb/git/rishe/data/verification/sources/web/5e6540ec649ced55.txt
### https://abadis.ir/fatofa/کوزه/
/home/sfmqrb/git/rishe/data/verification/sources/web/7f2cc1c80d7d13d5.txt
### https://abadis.ir/fatofa/گلادیاتور/
/home/sfmqrb/git/rishe/data/verification/sources/web/1df4dd4debde7335.txt
```


## [2026-09-06T16:12:42.323Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in d879225ad5ab1473 5e6540ec649ced55 7f2cc1c80d7d13d5 1df4dd4debde7335; do echo \"###### $f\"; grep -v \"^ *$\" $f.txt | grep -A6 \"فرهنگ معین\" | head -20; echo \"--- دهخدا snippet ---\"; grep -v \"^ *$\" $f.txt | grep -A4 \"لغت نامه دهخدا\" | head -8; echo; done"
}
```


### [2026-09-06T16:12:44.246Z] TOOL RESULT

```
###### d879225ad5ab1473
 فرهنگ معین
 (کُ لَ ) (اِ. ) ۱ - آلت آهنی نوک تیز که از آن برای کندن جاهای سفت زمین استفاده می کنند. ۲ - دُرنا. 
 فرهنگ عمید
 وسیلۀ آهنی نوک تیز با دستۀ چوبی برای کندن زمین.
= درنا 
 واژه نامه بختیاریکا
 ( کُلُنگ ) اوج؛ قله
--
نام کلنگ در گذشته، به شکل کلند بوده است. کُلَند یا کَلَند، دست افزار نقب کنان و گل کاران و سنگ تراشان است که با آن زمین را می کنند و به آن کلنگ نیز گویند. ( برهان ) [ ۱] در فرهنگ معین، دو واژهٔ کلندی و کلندگر نیز آمده است. [ ۲] همچنین در فرهنگ دهخدا، واژهٔ مصدری کلندیدن و کلندافکندن هم اشاره شده اند. [ ۳] واژهٔ «کلند» در شعر شاعران فارسی زبان نیز به کار رفته است، مانند دو بیت زیر:
«ای شده عمرت به باد از بهر آز
بر امید سوزنت گم شد کلند». ( ناصرخسرو ) . 
«پس کلند آورد و بیل او شاد شاد
کند آن موضع که آن تیر اوفتاد». ( مولوی ) . 
 wiki: کلنگ (ابزار) 
 کلنگ (کامپایلر). کلنگ /ˈklæŋ/ ، به عنوان فرانت اند کامپایلر برای C , C ++، زبان Objective - C و هدف - C ++ زبان های برنامه نویسی، و همچنین به عنوان کتابخانه، [ ۶] از OpenCL، از RenderScript، CUDA، و HIP[ ۷] چارچوب ها استفاده می شود. کلنگ به عنوان جایگزینی برای مجموعه کامپایلر گنو ( GCC ) عمل می کند و از اکثر پرچم های کامپایل و پسوندهای زبان غیررسمی پشتیبانی می کند. [ ۸] [ ۹] کلنگ شامل یک تحلیلگر استاتیک و چندین ابزار تجزیه و تحلیل کد است. [ ۱۰] 
--
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
 لینک ها 
 حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
 استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
--- دهخدا snippet ---
 لغت نامه دهخدا
 کلنگ. [ ک ُ ل َ / ل ُ ] ( اِ ) دست افزاری باشد که چاه جویان و گل کاران بدان زمین و دیوار کنند. ( برهان ). بمعنی افزاری است برای کندن زمین که از آهن می سازند و دسته از چوب می دارد و به این معنی کلند نیزآمده. ( آنندراج ). کلند و دست افزاری که بدان زمین و دیوار کنند. ( ناظم الاطباء ). مِعوَل. آهنی نوک تیز بادسته چوبین که بدان زمین و دیوار کنند. کلند. ( یادداشت به خط مرحوم دهخدا ) : پس الیاس گفت اگر روزی که شما باز نشینید، این آبهای شما خشک شده باشد شما چه خواهید کردن ؟ گفتند کلنگ و تیشه را کار فرماییم. آن شب همه بخفتند بامداد که بازنشستند همه راآب به چشم فرود آمده بود و چشمه ها خشک شده... آن پیمبر ایشان را گفت کلنگ و تیشه را کار فرمایید. ( اسکندرنامه نسخه نفیسی ، یادداشت به خط مرحوم دهخدا ).
کلنگی می زند چون شیر جنگی 
کلنگی نه که او باشد کلنگی نظامی ( خسرو و شیرین چ وحید ص 254 ).
- خانه کلنگی ؛ در تداول عامه ، خانه ای که ساختمان آن بحساب نیاید و به بهای زمین خرید و فروش شود.

###### 5e6540ec649ced55
 فرهنگ معین
 (س ) [ ازع . ] (اِ. ) ۱ - پیاله ، ظرف . ۲ - کوس . ۳ - بیرونی ترین پوشش گل . ،~ی داغ تر از آش کنایه از: واسطه ای که از صاحب حق بیشتر جوش می زند. ،~ ای زیر نیم ~بودن کنایه از: نیرنگی در کار بودن . ، ~کوزة کسی را به هم زدن کنایه از: شر و فساد و خرابی 
 فرهنگ عمید
 ١. ظرف سفالی یا چینی توگود که در آن غذا می خورند.
٢. (زیست شناسی ) حقۀ گل، کالیس.
* کاسهٴ سر: (زیست شناسی ) جمجمه، استخوان سر: روزی که چرخ از گِل ما کوزه ها کند / زنهار کاسهٴ سر ما پرشراب کن (حافظ: ۷۹۲ ).
* کاسهٴ زانو: (زیست شناسی ) استخوان روی مفصل زانو، آیینۀ زانو، سر زانو، کشکک.
--
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
 لینک ها 
 حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
 استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
 © 2006-2026 abadis.ir
--- دهخدا snippet ---
 لغت نامه دهخدا
 کاسه. [ س َ / س ِ ] ( اِ ) ظرفی باشد که چیزی در آن خورند. ( برهان ). ناجود و قدح و جام و ساغر و پیاله و دوری و طبقچه بزرگ و یا کوچک مسین و یا چوبین و یا گلین و بادیه و قدح چینی بزرگ و کوچک و هرظرفی که در آن چیزی خورند. ( ناظم الاطباء ). ظرف مدور از فلز یا گل که دیواره اش بلند باشد و برای حمل غذا و آب استعمال میشود و قسم بزرگ آن را قدح هم گویند. این لفظ مأخوذ از کاس عربی است. ( فرهنگ نظام ). کاس. رجوع به کاس شود : و از آمل آلاتهای چوبین خیزد چون کفچه و شانه و شانه نیام و کاسه و طبق. ( حدود العالم ).
که چون شاه کسری خورش خواستی 
یکی خوان زرّین بیاراستی 
سه کاسه نهادی برو از گهر

###### 7f2cc1c80d7d13d5
 فرهنگ معین
 (زَ یا زِ ) (اِ. ) ظرف دسته دار یا بی دستة سفالین . ،در ~گذاشتن و آبش را خوردن بیهودگی چیزی را آشکارا دیدن . 
 فرهنگ عمید
 ظرف سفالی دسته دار یا بی دسته، کوچک تر از خم برای آب یا چیز دیگر. 
 واژه نامه بختیاریکا
 کیزِه
 دانشنامه عمومی
--
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
 لینک ها 
 حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
 استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
 © 2006-2026 abadis.ir
--- دهخدا snippet ---
 لغت نامه دهخدا
 ( کوزة ) کوزة. [ ک ِ وَ زَ ] ( ع اِ ) ج ِ کوز. ( منتهی الارب ) ( ناظم الاطباء ) ( از اقرب الموارد ). رجوع به کوز شود. کوزه. [ زَ /زِ ] ( اِ ) ظرفی است گردن دراز که در آن آب نگهدارند.( آنندراج ). صراحی سفالی آبخوری که گردن دراز تنگی دارد. ( ناظم الاطباء ). ظرفی است گلین و گردن دراز که درآن آب و مایعات دیگر ریزند. ( فرهنگ فارسی معین ). ظرف سفالین با سری تنگ و با دسته که در آن آب کنند. ظرفی سفالین چون خمی خرد و آب در آن کنند. کوز. جوه. سبو. سبوی. ( یادداشت به خط مرحوم دهخدا ) : 
گولی تو از قیاس که گر برکشد کسی 
یک کوزه آب از او به زمان تیره گون شود. عنصری.
از کوزه چو آب خوش نوشی نبود باک 

###### 1df4dd4debde7335
 فرهنگ معین
 (گِ تُ ) [ فر. ] (اِ. ) در روم قدیم به بردگان و غلامانی می گفتند که می بایست در میدان های عمومی با یکدیگر یا با حیوانات درنده تا دم مرگ بجنگند. 
 فرهنگ عمید
 در روم باستان، غلامان، بردگان، یا محکومینی که در سیرک یا میدان عمومی و در مقابل امپراطور و سایر تماشاچیان با یکدیگر یا حیوانات درنده می جنگیدند. 
 دانشنامه عمومی
 گلادیاتور (فیلم ۱۹۳۸). گلادیاتور ( انگلیسی: The Gladiator ) یک فیلم به کارگردانی ادوارد سجویک است که در سال ۱۹۳۸ منتشر شد. از بازیگران آن می توان به جو ای براون و جون تراویز اشاره کرد. 
 wiki: گلادیاتور (فیلم ۱۹۳۸) 
--
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
 لینک ها 
 حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
 استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
 © 2006-2026 abadis.ir
--- دهخدا snippet ---
 لغت نامه دهخدا
 گلادیاتور. [ گْلا / گ ِ تُرْ ] ( فرانسوی ، اِ ) کسی که در بازیهای سیرک چه با یک انسان و چه با یک حیوان درنده پیکار میکند.و این از آداب و رسوم مردم روم قدیم بوده است. غلامان و بردگان زندانی با نهایت قوت و قدرت در میدانهای عمومی با حیوانات درنده ای که بوسیله مردم روم تربیت شده بودند مبارزه میکردند و گلادیاتور مجرم را نمی گذاشتند در مقابل حیوانات درنده از خود دفاع کند. گلادیاتور ناگزیر از خود دفاع می کرد و در زیر پنجه های حیوانات درنده کشته میشد و این عمل در حالی انجام میگرفت که امپراتور در لژ خود این صحنه را نظاره میکرد. 
 فرهنگ فارسی
 درروم قدیم کسانی رامیگفتندکه درسیرک یامیدان عمومی باحیوانات درنده پیکارمیکردند
( صفت و اسم ) کسی که با انسان یا حیوانی درنده پیکار کند . توضیح در روم قدیم مرسوم بود که غلامان و بردگان زندانی در میدانهای عمومی با جانوران درنده ای که بوسیل. مردم روم تربیت شده بودند مبارزه می کردند و این عمل در حالی انجام میگردید که امپراتور در لژ خود ناظر این صحنه بود .
```


## [2026-09-06T16:13:03.473Z] TOOL CALL #59: Bash

```json
{
 "command": "ls site/pages/252.jpg 2>/dev/null; pdftoppm -f 252 -l 252 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg252 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:13:05.947Z] TOOL RESULT

```
site/pages/252.jpg
total 10500
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:13 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1144 Sep  6 12:09 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:13:08.814Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg252.png"
}
```


### [2026-09-06T16:13:09.253Z] TOOL RESULT

```

```


## [2026-09-06T16:13:09.250Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:13:30.635Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && D=incoming/WLD/WLD_Bd1_pages.txt; echo \"== WLD Bd1 columba/kolumbos ==\"; grep -n \"columba\\|κόλυμβος\\|kolumbos\" $D | head -8; echo \"== WLD calix/κύλιξ/kalaça ==\"; grep -n \"calix\\|kalaça\\|kalaśa\\|Kelch\" $D | head -10; echo \"== WLD gladius/clades ==\"; grep -n \"gladius\\|clades\" $D | head -8"
}
```


## [2026-09-06T16:13:32.629Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN dove ==\"; grep -n \"columba\" SYN.txt | head -5; echo \"== SYN cup ==\"; grep -n \"calix\\|kalasa\\|kylix\" SYN.txt | head -5; echo \"== SYN sword ==\"; grep -n \"gladius\" SYN.txt | head -5; echo \"== SKT ==\"; grep -n \"^gladiator\\|^calamity\\|^clone\\|^columbine\" SKT.txt | head; grep -n \"gladiator\\|calamity\" SKT.txt | head -5"
}
```


### [2026-09-06T16:13:33.457Z] TOOL RESULT

```
== WLD Bd1 columba/kolumbos ==
54582:hin   auch (s. Zupitza Cfutt. 147, Berneker 327) ahd. kembil „columbar
== WLD calix/κύλιξ/kalaça ==
11770:gesttilpte Ivnopfchen), buwaxk „der Kelch der Eichel“ (deren Yergleich
42157:folgende i bedingtsein) = lat. ralix, -ids „tiefe Schale, Beeher, Kelch“ (oder
42164:nhd. Kelch ), wozu vielleicht mit beweglichem s umbr. skalge-ta, scalse-to
== WLD gladius/clades ==
3463:cymr. aer „Schlacht, Kainpf“ ( *agra ), eigentlieh „Hetze“, acorn, hair ,,clades“,
41694:und qel sehlagen“ mit Meillet aaO., Vf. LEWb. 2 u. clades Berneker 551,   ,
41739: Saussure 309f., Vf. LEWb. 2          u. clades).
41774:      Lat. clades „Yerletzung; Schaden, Unheil, Niederlage (iiber clava s. o.),
41820:aus     dem Cymr., lat. gladius aus dem Kelt., Yendryes Mel. Saussure 3l0f.
58340: 1405, hint ..Schwertknauf"                                     Lw. aus mnd        klrt      =   dt.   Kloft:       lat.   gladius   ist
```


### [2026-09-06T16:13:33.554Z] TOOL RESULT

```
== SYN dove ==
== SYN cup ==
8868:calix (above, 1).
8874:OE calic (reg. word for ‘cup’ in Gos- pels, as also Lat. caliz in Vulgate), OHG kelih, NHG kelch, etc., fr. Lat. calix (above, 1).
== SYN sword ==
34804:20.27 SWORD Grk.  Elos, paxatpa Goth. hairus, méki (acc. sg.) Lith. kalavijas, kardas NG orabl, Elpos (lit.) ON sverd, mekir, hjorr Lett. zuobens Lat.  gladius, énsis (poet.), Dan. svard ChSl. met, kor(ti)da spatha (late) We svdrd SCr. maé It. spada OE sweord, méce, heoru Boh. meé Fr. épée (glaive) ME _ swerd Pol. miecz Sp. espada NE sword Russ. meé Rum. sabie, spadé Du. zwaard Skt. _asi-, khadga- Ir. claideb, colg OHG - swert Av. karata- Nir. clatdheamh MHG ss swert W. cleddyf NHG | schwert
34811:2. Lat. gladius (> Olt. ghiado; Fr.
34815:Lat. énsis (old word, but only poet., in prose replaced by gladius) : Skt. asi- ‘sword’, root connection? Ernout-M. 302. Walde-H. 1.406.
34816:Lat. spatha ‘spattle’, also ‘sword’ of the auxiliaries (Tac.), later reg. word for ‘sword’, displacing gladius, loanword fr. Grk. o746y (above, 1). Hence It. spada (> Rum. spadé), Fr. épée, Sp. espada. Couissin, op. cit. 489. REW 8128.
34818:3. Ir. claideb, NIr., Gael. claidheamh (hence with mor ‘great’, NE claymore), W. cleddyf, Br. kleze, Corn. clethe, be- side Lat. gladius (fr. Celtic) : Ir. claidim, W. claddu ‘dig’, Lat. clddés ‘damage, in- jury’, Skt. khadga- ‘sword’, Lith. kalti
== SKT ==
926:Arena.  1,1.)  L.  arnwu,  sand  ;  the  sanded S{:>a*x  in  which  gladiators  fought.  Propettj »r<lt  karena,  and  im/  allied  to  artrt.
18689:distreM,  calamity.    (P.  -  L.)     O.  F.
```


## [2026-09-06T16:13:42.531Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && D=incoming/WLD/WLD_Bd1_pages.txt; echo \"=== WLD 42145-42175 ===\"; sed -n '42145,42175p' $D; echo \"=== WLD 41815-41825 ===\"; sed -n '41812,41826p' $D; echo \"=== nearest pdf page tags ===\"; awk 'NR<=42157 && /\\[pdf page/{p=$0} END{print p}' $D; awk 'NR<=41820 && /\\[pdf page/{p=$0} END{print p}' $D"
}
```


### [2026-09-06T16:13:44.548Z] TOOL RESULT

```
=== WLD 42145-42175 ===

bei  Persson Beitr. 32; etwas anders halt Reichelt aaO. die Bed. „Fleck“,
sei es weiB auf dunklem oder dunkel auf hellem Grunde fiir das urspriing-
liche ; kaum auszumachen.


5.  qel- (qol-, q c l) mit /j-Suffix „Becher“.
     Ai. kalaga-m. „Topf, Krug, Schale" ( *qoJeko -, -oko-); gr. xvkt£, -ixog
„Becher“ ( *qeIi-k die Entwicklung zu -vX- laBt Giintert Abl. 32 durch das
                    ;


folgende i bedingtsein) = lat. ralix, -ids „tiefe Schale, Beeher, Kelch“ (oder
-ix, -ids fiir *~ex, ids mit dem ai. -aca- naherstehender Bildungsweise ?
der Nom, -ix dann unterstiitzt dureh gr. xvXt £ aus eulix stammt ahd. chflih
                                                              ;
                                                                                                    ,


nhd. Kelch ), wozu vielleicht mit beweglichem s umbr. skalge-ta, scalse-to
wohl „expatera“, scalsie „in patera" (? v. Planta I 473; anders Fay Cl.
Rev. 13, 351. Das -s hat keine Parallele an dt. Schale, das zu Wz. *sqel-
„spalten" und an gr. axaXhov, oxaX.ig ds. Hes., das wohl ebendahin).
   Dazu gr. y.dXvg, -vxog „Fruchtkelch, Samenkelch" und vielleicht ai. kalika
„Knospe“ (wenn als noch geschlossener Beeher angeschaut; svare im Gutt.
des Suffixes von kaldga- verschieden).
   Yanit'ek LEWb. 314, Fick II 3 57, I 4 26, 28, 386 (mit unrichtiger An-
kniipfung an kel- „bergen, hiillen").                Nicht iiberzeugendes aus dem Ai. bei
Petersson IF. 34, 232.

6.    qel- „treiben, zu schneller       Bewegung antreiben".
=== WLD 41815-41825 ===

„Schwert, Klinge ( cleddyf diss. aus *cledt/d, kelt. *Icladios; ir. da deb ist Lw.
                                              44
                                                                                                                                                                                           >




aus     dem Cymr., lat. gladius aus dem Kelt., Yendryes Mel. Saussure 3l0f.
Yf. LEWb. 2 u. glad'ud).
                                  u
      Mir. caill (gen. caille) „Wald  cymr. edit „Wald“, corn. Tceili „nemus (kelt.                                                                                                                     44

                                                                                         ,

=== nearest pdf page tags ===
```


## [2026-09-06T16:13:58.214Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT calamity ==\"; sed -n '18686,18694p' SKT.txt; echo \"== SKT gladiator ==\"; grep -n -i \"gladiate\\|Gladiator\\|glaive\" SKT.txt | head -5; echo \"== KLN calamity ==\"; grep -o \"calamity,  n\\.[^|]\\{0,400\\}\" KLN_1966.txt | head -2; echo \"== KLN gladiator ==\"; grep -o \"gladiator,  n\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2; echo \"== KLN clone ==\"; grep -o \"clone,  n\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2"
}
```


## [2026-09-06T16:13:59.972Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD kasag ==\"; grep -n -i \"kas\\b\\|kasag\\|kāsag\\|kwzg\\|kōzag\" PHD.txt PHD_mackenzie.txt | head -15; echo \"== NYB ==\"; grep -n -i \"kasak\\|kasag\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-06T16:14:00.398Z] TOOL RESULT

```
== SKT calamity ==
constrain,  to  compel.  (F.  —  L.)  O.  F. constraindrf,  later  ctmtraimirt.  —  L.  emt- rtn'Hfftrtf  to  bind  leather,  fetter.
distrain.  (F.-L.)  O  F.  Uettraifidft» to  strain,  press,  vex  extremely  (hencc  to seize  goods  for  debt).  -•  l^  di-itrmgtrt,  tc poll  asonder.
STRIP
distreM,  calamity.    (P.  -  L.)     O.  F.
diitriSH.  oldest  form  distrtre.  A  verbal sb.  fioaj  a  I*ow  L.  districiiart  •  (not  ased>. regularly  formct!  (rom  L.  districtus,  pp.  of disiringtre,  to  pull  asunder  (in  late  L.  to pnnish,  affiict);  sec  aboTC.
district,  a  region.  (F.  -  L.)  O.  F. district,  m.  Low  L.  Jist rictus.  ierrxXory  where- in a  lord  has  power  to  di^itram  (Duconge). ••L.  distriitus,  pp.  oi  di-stringert.
obstriction,  obligation.  (L.)  Coined from  L.  obstri£ttu,  pp.  of  cihstringtrt,  to bind,  fasten.
reetrain,  (F.  —  L.)  0.¥.  rtstmindrt (F.  rtstrtinJrt).  lo  restrain. ••L.  restring' ert,  to  draw  back  tightly,  bind  back. Dor.  rtstraint,  from  O.  F.  rtstnupttt,  fem. of  pp.  of  rtstraindn.
restrict,  (l..)  From  L.  rtstrutui,  pp. of  rt  itringtrt,  lo  bind  back.
== SKT gladiator ==
926:Arena.  1,1.)  L.  arnwu,  sand  ;  the  sanded S{:>a*x  in  which  gladiators  fought.  Propettj »r<lt  karena,  and  im/  allied  to  artrt.
7624:Gladiator,  ft  swordsman.  (U)  L.^ diatar.  —  L.  giaJitUj  a  sword.
7626:glaive,  a  sword.  cF.*L.)  Q.T.gUm —  L.  giadium,  ace.  o\  giadius^  a  sword.
7628:Glaive ;  see  OUdiator.
== KLN calamity ==
calamity,  n.,  misery;  disaster.  —  F.  calamite,  fr. L.  calamitatem,  acc.  of  calamitas,  ‘damage,  in¬ jury,  loss,  misfortune’,  with  the  primary  mean¬ ing  ‘blow’,  rel.  to  in-columis,  ‘unimpaired,  un¬ injured’,  fr.  I.-E.  base  *qel(a)-,  *qol(a)-, ‘to  strike, beat’,  whence  also  Gk.  xXav,  ‘to  break’,  xXvjpo?, Dor.  xXapo?,  prop,  ‘little  piece  of  wood  lopped off  (used  for  
== KLN gladiator ==
gladiator,  n.,  a  Roman  swordsman  who  fought in  the  arena  for  the  entertainment  of  spectators.
== KLN clone ==
clone,  n.  —  Coined  by  the  English  scientist Sir  Francis  Galton  (1822-1911)  fr.  anti-  and cyclone.
clone,  n.  —  Irregularly  formed  fr.  Gk.  xuxXoq,
```


### [2026-09-06T16:14:00.451Z] TOOL RESULT

```
== PHD kasag ==
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:807:anybody kas-iz.
PHD.txt:2927:nobody kas-iz.
PHD.txt:3106:person kas, tan, P keé.
PHD.txt:3729:somebody kas, P keč.
PHD_mackenzie.txt:3250:kas [AYS < A )yfl M ks, N -] person, somebody.
PHD_mackenzie.txt:3332:kas-, V. koxs-.
PHD_mackenzie.txt:5922:Ahuramazda Ohrmazd.                       anybody kas-iz.
PHD_mackenzie.txt:5954:anemone alalag.                           armpit kas.
PHD_mackenzie.txt:6711:goat buz.                                     greeting erkas.
PHD_mackenzie.txt:7170:11Obody kas·iz.                        omen jadag, Jahisn, murwag.
PHD_mackenzie.txt:7263:person kas, tan, P kec.                    pleasant xwaS.
PHD_mackenzie.txt:7474:roaring yarranisn.                         salutation erkas.
PHD_mackenzie.txt:7618:skin carm, dawal, post; toz; (a.) post-       somebody kas, P kec.
PHD_mackenzie.txt:9481:                                  kas, ki;i                          -"U,
== NYB ==
2257:käsakön [+k’skyn'] a kind of stone: ~ spet rošn dazzlingly white k., the element of which the vault of heaven was created 928, 9312. . In the text only ken, but the emendation is almost certain. BdA p. 210: the fortress Kangdiz had seven walls (ll. 9-10) 1. of gold, 2. of silver, 3. of steel. 4. of copper, 5. of iron, 6. of glass, 7. käsakenen ‘of kdsakén’. Same enumeration in Jamaspik, ed. by Messina, 73, where kāsakēn instead of -enen. OP käsakaina-, adj. of käsaka-, defined by Kent as ‘a semi-precious stone’, whereas kasakaina- in his opinion is rather lapis lazuli. (Absurdities by Herzfeld, ApI 230-233).
4904:kasakaina- (käsaka-): kasakčn
```


## [2026-09-06T16:14:12.582Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN clon ==\"; grep -o \"clon[ae][^|]\\{0,250\\}\" KLN_1966.txt | head -6; echo \"== KLN 1971 clone ==\"; grep -o \"clone[^|]\\{0,220\\}\" KLN_1971.txt | head -4"
}
```


### [2026-09-06T16:14:14.414Z] TOOL RESULT

```
== KLN clon ==
clone,  n.  —  Coined  by  the  English  scientist Sir  Francis  Galton  (1822-1911)  fr.  anti-  and cyclone.
clone,  n.  —  Irregularly  formed  fr.  Gk.  xuxXoq,
clones. —  Compounded  of  cyclone  and  Gk.  -Xoyta,  fr. -Xoy 0?,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivative :  cydonolog-ist ,  n.
clone  in  the  western  Pacific.  — Chin,  tai  fung,  lit.  ‘great  wind’;  influenced  in form  by  Arab,  tufan  (whence  also  Port,  tufao), fr.  Gk.  TO9COV,  ‘whirlwind’  (see  typhus). typhous,  adj.,  pertaining  to  typhus.  —  Formed with  suf
== KLN 1971 clone ==
clone, n. — Coined by the English scientist 
clone. 
clone, n. — Irregularly formed fr. Gk. xoxXoc;, 
clones.
```


## [2026-09-06T16:14:14.736Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN kase/kuza/kulang ==\"; grep -n \"kasa\\|kuza\\|kulang\\|kaland\" HRN.txt | head -12; echo \"== HUB ==\"; grep -n \"kasa\\|kuza\\|kulang\\|kaland\" HUB.txt | head -12; echo \"== LKT ==\"; grep -n -i \"Kelch\\|kuza\\|kase\" LKT.txt | head -8; echo \"== ARY 1965-1985 ==\"; sed -n '1960,1990p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T16:14:14.833Z] TOOL RESULT

```
== HRN kase/kuza/kulang ==
784:aw. ä + i^kas-, äkasat er erblickte'; phlv. äkäs, äkäslh^
7075:fräh[(f\T.h^ fräh[e\Jmtan^ frah[e\kart (aw. Vourukasa-),
7441:aw. kasa- 'Achselhöhle'; phlv. kas; ai. kdksa- 'Gurt-
7470:kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
8867:aw. *anäkasa' *improvisus* ; phlv. anakäslhd 'un-
8991:aw. *nikasa- (vergl. ägäh, No. 40); phlv. n(i)käs.
== HUB ==
333:steht nicht fest. Im Balu^i wird altes rs zu s, vgl. kasag^),
1441:u. s. w.) kann weder =-- zd. *upakasa' noch = zd.
1935:das mit np. kuza (arm. LW. kuS 'Krug* = zd. ^kum-)
3082:856. Afgh. kasap nach Raverty.
3158:geht mit diesem auf ein ap. *kuza (oder *kuja) zuriick.
6307:Fiir 6; v aus p erscheint unregelmassig / in kasaf
6309:afgh. kasap ; fdm *Schuld* = vam s. § 66 ; afranjan = avran-
6546:Vgl. auch kasaf 'SchildkrSte* = zd. kasyapa- (§ 71).
7541:vas = s\iv, vag Vollen'?); kargas 'Geier = zd. kahrkasa-;
7562:•^ zd. syava- (aber kasaf 'Schildkrote' = zd. kasyapa-,
8244:kuza (oben p. 89); oiz *Kraft' = paz. oz, Shk. 230, zd.
8418:kas 'AchselhQhle' = zd. kasa-, skr. kaksa-: sas *sechs'
== LKT ==
2633:Kasmir  ist  eine  Stadt  und  ein  größeres Gebiet  im  nordwestlichen  Indien,  wo Schals  in  vorzüghcher  Qualität  her- gestellt wurden.  Hieraus  engl,  cashmere, ndl.  cachemir,  dtsch.  Kaschmir  (früher Kasimir);  it.  casimiro,  sp.  casimiro,  pg. Casimir a,  frz.  cachemire;  russ.  kazmir, kasemir,  poln.  kazmirek,  cech.  kazimir. [Bern  SlEtWb  496.
2991:'Kaserne'  [aus  kys  'Winter'  vom  Stamme kar,  kir  'Schnee,  Reif,  Winter',  also 'Zeit  des  Schnees  und  Schneegestöbers', vgl.  slav.  zima  'kalt'  und  'Winter',  sskr. hima  'Schnee'  und  lat.  Iiiems  'Winter'; dazu  das  Suffix  -Ja  zur  Bezeichnung eines  Ortes,  demgemäß  kysla  eigentlich 'Winterquartier'];  hieraus  rum.  cä^lä 'Rammel-  oder  Schafherde',  cä§lärie 'Gutshof'.
== ARY 1965-1985 ==
روسی (805540۷): 1۸7116۸ 0 20000
لیعوانی (17[411۸01۸/7.): ی ۱۲۷۷۱۹ ی
ایرلندی کهن. (1/3 ۰:0 ۰۰:۰۰ :11۸0۸0 .: زد رفن6 نکنام ب۵هه6 متام ما
0 6ر 5 ما موه
ی ی 3 راهم 0
با مود ون رکد صعسن هی
۸7 هامید
: : اس ی بردانعطع: 7
1 ۰ 1 اک لفت‌نامه دهدا:؟: ۹:۰ :۱ ۳۳
۱ با ار 1 فرهتگه معینن از اه ۸۶
باداش 1 0 وس
۱- معنی این واژه در هند و اروپایی و اکثر زبان‌های دیگر: کلنگ؛ پفکهه" 6
معنی اين واژه در سانسکریت: خیش؛ چنگکك زمین صاف‌کنی. یی
1 معنی اين واژه در رومانی: چماف, اک
1 معنی این واژه در آلمانی کهن: شُخم. ما دا وراه
1 ۲- 8168۸7 ,0217088 این واژه را فقط تا ریشه‌ی لاتین پیگیری می‌کند ‏ دا اش برع ورد
[ رس رآ ۹
رایس مورا 16
:
ارستایی 0۸90:8700 ,3۸018031 پوناني 108880 8۸1008 ر99ل4....
3 ان اقا رب را را هه
. پارسی نباستان (4(۷اق۶8 00 لائین (7100مل):(شاید) ۰ * :۲ هش :
بالالاز الک ما۸ روت واهررسیت : ی ‏ ب۸
پپلری (/اماتهم): ۰2۸3۸0 ,۱۸۵۸۵ اسپانبْانیٌ (52۸۸/7877): (شاید) 7 1 8
تخاری ۸ (۸4 70874/7): اه ,اقق ایتالیایی آ(( 4 2/): (شاید) ری ادن یه
تخاری 8(:8 ((فن702): 6۸۸ ,الا رومانی 21/4 #): (شاید) ۷1
ساسکریت رازه اد سا پرتغالی "(۳0877010832): (شاید) :۹ ۱7 :۰.۹8۱
اا۸#ق2 باقع باتفللفه نامرد گرتیک:0071/10): متام
ارمنی (۸4/8(/14۸): انا انش نررش کهْنْ (۸0888 0): 04
[pdf page 70]
تج
```


## [2026-09-06T16:14:27.830Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1928,1945p' HUB.txt; echo \"-----\"; sed -n '3150,3165p' HUB.txt; echo \"--- page markers ---\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nfor w in [\"mit np. kuza (arm\",\"auf ein ap. *kuza\"]:\n    i=t.find(w); print(w,\"-> leaf\",t[:i].count('\\f'),\"printed p\",t[:i].count('\\f')-10)\nEOF"
}
```


### [2026-09-06T16:14:29.758Z] TOOL RESULT

```
bildet. Wo findet sich das pr. xartnam (Sal. Shuk.
p. 53)? 1st es alt (== skr. krinami) oder eine dialekti-
sche Neubildung? Jedenfalls das letztere. Vgl. die
Dialektformen bei Horn und ZDMG. 36, 74.
488. Ich trenne xafj ephialtes* von xuspidan schlafen' und
stelle es mit de La garde zu zd. xawza" (phi. xafzik
Phi. Vd. 113, 4 V. u., 114, 4 v. oben: lies xafzak?),
das mit np. kuza (arm. LW. kuS 'Krug* = zd. ^kum-)
nichts zu thun hat. Vgl. afgh. xapasa fem. night-
mare'*
488. Lies afgh. LW. xa^ta 'Ziegel*.
489. Ich sehe nicht ein, was der Begriif 'Aehre' (np. xoSa)
mit dem Begriflf 'trocken' (np. xuSk) zu thun hat. Np.
xdsa bedeutet zudem auch 'die Traube' (des Wein-
stockes und der Dattelpalme). Ebenso urteilt Geiger,
Etym. und Lautl. der Afgh. unter Nr. 266: vami
*Aehre*.
492. Zd. hareii- = phi. halak ^= paz. hala *foolish, silly
-----
abgeleitet, zu dem das auf schwachster Wurzelstufe
stehende zd. ktUaka- *klein* gehSrt. Horn's Erklarung
von kodak aus ^kvataka- (vom Pronominal stamm kva-,
ku"?) ist mir unverstandlich.
872. Np. fcil^a 'irdene Krug, Kanne* = afgh. kUza an earthen
vessel for water with a spout* ist abgeleitet mittelst
des Suffixes a (= phi. ak) von kUz = arm. LW. kuz
'Krug, Kanne' = arab. LW. hOz *kleiner Krug und
geht mit diesem auf ein ap. *kuza (oder *kuja) zuriick.
Ueber zd. xawza- vgl. oben Nr. 483.
Hier fehlt np. Uui {kUz und kUza) gekriimmt' {kuz-pust
Fird. I, 503, Z. 7), afgh. ko^ (LW.?) crooked, bent*
= skr. kubja^ 'krumm, bucklig*.
873. Die Zusammenstellung setzt eine idg. Wrzl. kul-
(hochstufig ketd^ kouT) voraus, die es nicht giebt.
874. Zu streichen.
--- page markers ---
mit np. kuza (arm -> leaf 66 printed p 56
auf ein ap. *kuza -> leaf 99 printed p 89
```


## [2026-09-06T16:14:42.416Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8855,8880p' SYN.txt"
}
```


### [2026-09-06T16:14:42.465Z] TOOL RESULT

```
late form of ciipa ‘tub,
kireddov, etc., above, 1.
Hence It. coppa, coupe), SP. copa, Rum. cupd, etc., now
used for a large drinking-vessel and otherwise replaced by. tazza etc.; NG sobna; In. copp, copan, etc. (Vendryes, Dehib. voc. 130), NIr. cupdn, W. cwpan, Br. kop; and so prob. the Gme. group, ON koppr, OF cuppe, OHG kopf, etc. (otherwise, as genuine Gmce., fr. IE *geu-, parallel to *keu-. Persson, Bei- trige 104, Falk-Torp 564, Walde-P. 1.562), Walde-H. 1.311. REW 2409. Weigand-H. 1.118 f. NED s.v. cup.
It. tazea, Fr. tasse (> Br. tas; NHG lasse, this > Lett. tase), Sp. taza, fr. Arab, tassah ‘bowl, basin’. REW 8594.
Rum, ceased fr. Slavic éa%a (below, 6).
8. In. airidech,
chd. of air (the late g ink?
(above, 2),
Ir. coupe (> ME
idee airdech, apparently a for , but second part obscure pelling trdeoch, as if fr. deoch only a pop
en, Z. celt, Ph, 8.71 Ir, cailech, fr. Lat. Ir, Copan
Saag Thurney-
calix (above, 1).
» etc, fr. Mat. cuppa 4. Goth, stikls
p’
& the Pointed
RINK; COOKING AND UTENSILS 349
ON koppr, OE cuppe, etc., see above, 2.
OE calic (reg. word for ‘cup’ in Gos- pels, as also Lat. caliz in Vulgate), OHG kelih, NHG kelch, etc., fr. Lat. calix (above, 1).
OHG behhare, MHG, NHG becher, like NE beaker, fr. the same source as NE pitcher (5.34).
5. Lith. puodelis, puodukas, dims. of puodas ‘pot’ (5.26).
6. ChSI., SCr. casa, Boh. cise, Russ. éaska (Russ. ¢asa ‘bowl or large drink- ing-cup’), Skt. casaka-, Arm. éagak, all perh. fr. Iranian (cf. NPers. éasidan ‘taste’). Berneker 137.
Boh. Salek, dim. fr. NHG schale ‘bowl’.
Pol. czarka, dim. of czara ‘drinking- bowl’ (cf. Russ. éar, carka ‘drinking- glass’), prob. fr. Turk. dial. cara ‘large bowl’. Berneker 136. Briickner 72.
7. Skt. casaka-, above, 6.
```


## [2026-09-06T16:14:48.805Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:14:48.852Z] TOOL RESULT

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


## [2026-09-06T16:16:48.670Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/clone\" \"https://en.wiktionary.org/wiki/gladiateur\" \"https://www.etymonline.com/word/calamity\" \"https://en.wiktionary.org/wiki/کلند\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 252 verification\"; done"
}
```


### [2026-09-06T16:16:52.430Z] TOOL RESULT

```
Exit code 1
### https://en.wiktionary.org/wiki/clone
/home/sfmqrb/git/rishe/data/verification/sources/web/876b82eddd172d1a.txt
### https://en.wiktionary.org/wiki/gladiateur
/home/sfmqrb/git/rishe/data/verification/sources/web/11e4dd9d47f3b413.txt
### https://www.etymonline.com/word/calamity
/home/sfmqrb/git/rishe/data/verification/sources/web/7c7bdb49995a819e.txt
### https://en.wiktionary.org/wiki/کلند
/home/sfmqrb/git/rishe/data/verification/sources/web/1735bff7d48a6986.txt
```


## [2026-09-06T16:16:55.410Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 876b82eddd172d1a 11e4dd9d47f3b413 1735bff7d48a6986; do echo \"###### $f\"; awk '/^ From Wiktionary, the free dictionary/,0' $f.txt | grep -v \"^ *$\" | head -18; echo; done"
}
```


### [2026-09-06T16:16:57.883Z] TOOL RESULT

```
###### 876b82eddd172d1a
 From Wiktionary, the free dictionary
 See also: cloné 
 English
 [ edit ] 
 English Wikipedia has an article on: clone 
 Wikipedia 
 Alternative forms
 [ edit ] 
 clon ( obsolete ) 
 Etymology
 [ edit ] 
 Coined (in botany) in 1903, based on Ancient Greek κλών ( klṓn , “ twig ” ) . Figurative use from the 1970s.
 Pronunciation
 [ edit ] 
 enPR : klōn 
 ( General American ) IPA ( key ) : /kloʊn/ 
 Audio ( US ) : ( file ) 
 ( Received Pronunciation ) IPA ( key ) : /kləʊn/ 

###### 11e4dd9d47f3b413
 From Wiktionary, the free dictionary
 French
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Latin gladiātōrem ( “ gladiator, swordsman , swordman (uncommon) ” ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ɡla.dja.tœʁ/ 
 Audio : ( file ) 
 Audio ( France ( Vosges ) ) : ( file ) 
 Audio ( France ( Somain ) ) : ( file ) 
 Hyphenation: gla‧dia‧teur 
 Noun
 [ edit ] 
 gladiateur   m ( plural gladiateurs , feminine gladiatrice or gladiateure ) 
 gladiator 
 Synonym: belluaire 

###### 1735bff7d48a6986
```


## [2026-09-06T16:17:02.588Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg252.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/252.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/252.png"
}
```


### [2026-09-06T16:17:02.650Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74772 Sep  6 12:17 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/252.png
```


## [2026-09-06T16:27:27.831Z] TOOL CALL #74: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-252.json",
 "content": "{\n  \"pdf_page\": 252,\n  \"book_page\": 222,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kel 4, Qel\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kel- 'a kind of dark (or light) spot; grey, dark' (Pokorny kel-4, IEW 547-548; Watkins/AHD kel-5 'gray, black, dark'; Klein *qel-, *qol- 'of a dark color')\",\n      \"note\": \"The root is real and the language label is right. Pokorny's own gloss is wider than Nourai's: 'eine Art Farbe/Fleck', a dark spot on a light ground OR a light spot on a dark one (hence Skt. karka- 'white', karkī 'white mare', NHG Schweiz. helm 'white blaze', all in the same article) — which is precisely why Persian čarmeh 'white horse' can belong here. Nourai's 'gray, black, dark' is copied from AHD's kel-5. The page reference POK:546 is one page early: p.546 is still inside kel-3 'schlagen, hauen' (545-547); kel-4 begins on p.547, which is exactly the number given on the three daughter nodes. KLN:316 is exact. Note that the modern handbooks (Beekes 2010, de Vaan 2008) treat the Greek and Latin bird names as Pre-Greek/substrate, which undermines the two western branches of this chart while leaving the Iranian one intact.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kel- به معنی «لکهٔ تیره یا روشن، خاکستری، سیاه» است که پوکورنی آن را در «برگ ۵۴۷-۵۴۸» زیر مدخل kel-4 آورده و واتکینز در پیوست AHD زیر kel-5 «خاکستری، سیاه، تیره» و کلاین (ص ۳۱۶) زیر *qel-, *qol- «به رنگ تیره». معنایی که نورایی داده درست ولی تنگ‌تر از معنای پوکورنی است؛ پوکورنی هم لکهٔ تیره و هم لکهٔ روشن را زیر همین ریشه می‌آورد (سنسکریت karkī «مادیان سپید») و همین است که راه را برای «چرمه» یعنی اسب سپید باز می‌کند. ارجاع POK:546 یک صفحه زودتر است: صفحهٔ ۵۴۶ هنوز بخشی از kel-3 «زدن، بریدن» است و kel-4 از ص ۵۴۷ آغاز می‌شود — همان شماره‌ای که نورایی روی گره‌های زیرین آورده. ارجاع KLN:316 دقیق است. باید افزود که ریشه‌شناسی امروزی (بیکس، دِ فان) واژه‌های یونانی و لاتینی این نمودار را وام‌واژهٔ پیشایونانی می‌داند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/columba#Latin\",\n        \"https://en.wiktionary.org/wiki/κόλυμβος\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:546\", \"status\": \"partial\", \"note\": \"POK_full.txt (database dump of IEW), the article after kel-3: 'Root / lemma: [kel-4] and kal-; Meaning: a kind of dark/light spot ... References: WP. I 440 ff. ... Page(s): 547-548'. The root is real and is Pokorny's kel-4, but it stands on pp.547-548, not 546; p.546 belongs to kel-3 'to hit, cut down' (545-547).\"},\n        {\"ref\": \"KLN:316\", \"status\": \"supports\", \"note\": \"Klein 1966 (KLN_1966.txt, form-feed leaf 177; the running head of leaf 174 reads 'cognitive coleorhiza 310', so leaf 177 = pp.316-317) s.v. 'Columba': 'L., dove, pigeon, cogn. with Gk. κόλυμβος, κολυμβίς, diver (name of a bird), OSlav. golǫbь, dove, lit. the blue bird ... All these words derive fr. I.-E. base *qel-, *qol-, of a dark color, whence also Gk. κελαινός, black.' — Nourai's root name 'Kel 4, Qel' and the gloss come straight from this entry.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 440 ff. (qel-4 'Fleck')\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt: '... etwas anders hält Reichelt aaO. die Bed. „Fleck“, sei es weiß auf dunklem oder dunkel auf hellem Grunde für das ursprüngliche; kaum auszumachen' — Walde-Pokorny explicitly leaves open whether the original sense was a light spot on dark or a dark spot on light.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, kel-5\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.]' — the source of Nourai's gloss, and it too cites Pokorny p.547.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. columba\", \"stance\": \"supports\", \"note\": \"'La comparaison de lat. palumbes et de v.sl. golǫbь „pigeon“ (cf. r. goluboj „bleu“) engage à voir dans col- la désignation d'une couleur; le grec a en effet κόλυμβος „petit grèbe“ à côté de κελαινός „noir, sombre“.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"čarmeh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian چرمه čarme is real and Nourai's gloss is right: Dehkhoda s.v. چرمه '[مطلق] اسب را گویند عموماً (برهان)' with a second sense 'اسب سفیدموی خصوصاً ... اسب خنگ', Mo'in '(چَ مَ) (اِ.) ۱- اسب. ۲- اسب سفید', ʿAmid 'اسب، مخصوصاً اسب سفید'. Pokorny puts it under exactly the cited page: IEW 547 'npers. čarma „Schimmel“, kurd. čelme „weiß“' — German Schimmel here means 'white/grey horse' (the machine-English of the online IEW dump mistranslates it 'mildew'), so the chart's 'horse' is the correct rendering. Phonetically: PIE *kel- with the colour suffix *-mo- gives Indo-Iranian *čar-ma- — the Indo-Iranian law of palatals turns *k into *č before the front vowel *e, and PIE *l merges with *r (compare non-palatalised Skt. kalmāṣa- 'speckled' from the *kal- variant). The Middle Iranian stage is guaranteed by the Armenian loan čermak 'white (of a horse)' (Hübschmann); the Persian noun then took the New Persian -a/-e ending, čarma > čarme. Central Kurdish çermig 'white' and Georgian č̣armaḳi are the same word. The Ferdowsi hemistich quoted in the chart is genuine usage of the word (compare Dehkhoda's Ferdowsi citations 'شوم چرمه گامزن زین کنم', 'بر آن چرمه تیزرو زین نهاد').\",\n          \"derivation_fa\": \"«چرمه» واژه‌ای اصیل فارسی است و معنایی که نورایی داده درست است: دهخدا به نقل از برهان «مطلق اسب را گویند عموماً» و در معنی دوم «اسب سفیدموی، اسب خنگ»، معین «۱- اسب ۲- اسب سفید». پوکورنی در همان صفحهٔ ۵۴۷ می‌آورد: «npers. čarma „Schimmel“, kurd. čelme „weiß“» و Schimmel در آلمانی «اسب سپید» است (نه «کپک»، که ترجمهٔ ماشینی متن انگلیسیِ پوکورنی آن را به خطا چنین برگردانده). از دید آوایی: هندواروپایی *kel- با پسوند رنگ *-mo- در هندوایرانی به *čar-ma- بدل شده؛ زیرا در هندوایرانی k پیش از واکهٔ پیشین e به č کامی می‌شود («قانون کامی‌شدگی») و l هندواروپایی با r یکی می‌گردد. مرحلهٔ ایرانی میانه را وام‌واژهٔ ارمنی čermak «سپید (دربارهٔ اسب)» گواهی می‌کند (هوبشمان، پژوهش‌های فارسی، ص ۱۳۰)؛ سپس در فارسی نو پایانهٔ ـه افزوده شده: čarma > čarme. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/چرمه/\",\n            \"https://en.wiktionary.org/wiki/چرمه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:547\", \"status\": \"supports\", \"note\": \"POK_full.txt, root kel-4 (Page(s): 547-548): 'npers. čarma „Schimmel“, Kurdish čelme „weiß“ (: Swiss helm)' — exactly the arrow Nourai draws. (The 'mildew' of the English dump is a mistranslation of German Schimmel 'white horse'; the parallel Swiss dial. hjalm 'white ox or white horse' in the same paragraph settles the sense.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.130 (HUB.txt, form-feed leaf 140; offset leaf = printed + 10)\", \"stance\": \"supports\", \"note\": \"In the list of Armenian words borrowed from Middle Persian: 'čermak „weiss“ (Pferd) = np. čarma „Schimmel“' — Hübschmann equates Armenian čermak 'white (horse)' with NP čarma.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 438 'čerm „Fell, Haut“' (HRN.txt line 4055)\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has only čarm/čerm 'leather, hide' (= Av. čarəman-, Skt. cárman-); no entry for čarma 'white horse'. A grep for 'carme|carma|Schimmel' in HRN.txt returns nothing else, so Horn is silent on this word (and it must not be confused with čarm 'leather').\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ s.v. چرمه (BQT_v2_pages.txt line 5336; also quoted verbatim by Dehkhoda)\", \"stance\": \"supports\", \"note\": \"The OCR of the Borhan page is broken but legibly contains 'چرمه' next to 'خنگ' (white horse) and the Qābusnāma citation 'اسب چرمه خنگ ... اگر خایه و میان و رانها و سم و دست و پای و بوش و ناصیه و دم سیاه بود نیک باشد', which Dehkhoda reproduces s.v. چرمه; Borhan glosses it 'مطلق اسب' and 'اسب سفیدی موی خصوصاً'.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. چرمه (via abadis.ir, section فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'(چَ مَ ) (اِ. ) ۱ - اسب . ۲ - اسب سفید.' — no foreign-origin tag, i.e. Moʿin treats it as a native Persian word.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"kolumbos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek κόλυμβος (kólumbos) is real, but it is not simply 'a gray bird': it is the diver/little grebe (Podiceps), an alternative form of κολυμβίς used by Aristophanes (Birds 304), whence the verb κολυμβάω 'to dive'. Pokorny 547 does put it here — 'sehr wahrscheinlich κόλυμβος (*kolu-mbʰos) „Taucher (Vogelart)“, wovon κολυμβάω „tauchen“, benannt von der dunklen Farbe' — so the bird is named from its dark plumage, which is what Nourai means by 'a gray bird'; Klein p.316 says the same. The modern view is more sceptical: Beekes (followed by Wiktionary) treats κόλυμβος as a Pre-Greek loan, the -υμβ- cluster being un-Indo-European, and derives the verb from the noun rather than the reverse. Hence plausible, not confirmed: the arrow is the standard 19th-20th-c. handbook etymology but not the current consensus.\",\n          \"derivation_fa\": \"واژهٔ یونانی باستان κόλυμβος (kólumbos) واقعی است، اما معنای دقیق آن «پرندهٔ خاکستری» نیست، بلکه «غوّاص، کشیم کوچک» است (صورت دیگرِ κολυμβίς نزد آریستوفانس، پرندگان ۳۰۴) و از همین‌جا فعل κολυμβάω «غوطه خوردن» ساخته شده. پوکورنی در ص ۵۴۷ آن را از *kolu-mbʰos می‌گیرد و می‌گوید نام این مرغ از رنگ تیره‌اش برگرفته شده؛ کلاین (ص ۳۱۶) نیز همین را می‌گوید و مقصود نورایی از «پرندهٔ خاکستری» همین است. ولی پژوهش امروزی (بیکس و به پیروی او ویکی‌واژه) این واژه را وام‌واژه‌ای پیشایونانی می‌شمارد، چون خوشهٔ -υμβ- در هندواروپایی سابقه ندارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/κόλυμβος\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:547\", \"status\": \"supports\", \"note\": \"POK_full.txt, kel-4 (pp.547-548): 'very probably κόλυμβος (*kolu-mbʰos) „diver (bird's kind)“, whereof κολυμβάω „dive“, called from the dark color; here also κιλλ-ουρος „wagtail“ Hes.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p.316 s.v. Columba / p.317 s.v. Colymbus\", \"stance\": \"supports\", \"note\": \"'Colymbus, n., a genus of birds (ornithol.) — ModL., fr. Gk. κόλυμβος, „diver (the bird)“, which is cogn. with L. columba, „dove, pigeon“.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 440 ff.\", \"stance\": \"supports\", \"note\": \"The qel- 'Fleck' article of Walde-Pokorny is the source Pokorny abridges; it carries the same Greek material (κελαινός, κίλλος, κόλυμβος) under the colour root.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. columba\", \"stance\": \"supports\", \"note\": \"'le grec a en effet κόλυμβος „petit grèbe“ à côté de κελαινός „noir, sombre“' — E-M treats the grebe name as a colour word beside κελαινός 'black'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"col-umba\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin columba f. / columbus m. 'dove, pigeon' is real and the gloss is right. The traditional derivation, which Nourai follows, is Pokorny 547: 'lat. columba, -us „Taube“ aus *kol-on-bʰo- oder *kolu-mbʰo-, dann identisch mit κόλυμβος' — a colour name, the bird called from its dark/slate plumage, exactly like Old Church Slavonic golǫbь 'dove' beside Russian goluboj 'blue' and Latin palumbēs; Ernout-Meillet and Klein 316 argue the same way, and Watkins reconstructs *kel-omb(h)-. Nourai's hyphenation 'col-umba' is his own way of exposing that suffix. Two reservations keep this from 'confirmed': (a) the current Wiktionary/Beekes line makes Latin columba a straight borrowing from Ancient Greek κόλυμβος (itself Pre-Greek), so the word would not descend from the root at all but be a loan — and in that case the chart's direct root→Latin arrow, drawn parallel to (not under) the Greek node, is wrong; (b) Etymonline, following de Vaan, simply calls columba 'a word of uncertain origin'. The root affiliation is the older standard, not a settled fact.\",\n          \"derivation_fa\": \"واژهٔ لاتینی columba (مؤنث) / columbus (مذکر) «کبوتر» واقعی است و معنایش درست آمده. ریشه‌شناسی سنتی که نورایی از آن پیروی می‌کند از آنِ پوکورنی (ص ۵۴۷) است: columba از *kol-on-bʰo- یا *kolu-mbʰo- و «همان κόλυμβος یونانی»، یعنی نام رنگ؛ درست مانند golǫbь در اسلاوی کهن در کنار goluboj روسی «آبی». ارنو-مِیه و کلاین نیز همین را می‌گویند و واتکینز *kel-omb(h)- بازسازی می‌کند. جداسازی «col-umba» شیوهٔ خود نورایی برای نشان‌دادن پسوند است. اما دو نکته مانع از تأیید کامل است: نخست آن‌که ریشه‌شناسی امروزی (ویکی‌واژه بر پایهٔ بیکس) columba را یکسره وام‌واژه از یونانی κόλυμβος می‌داند و در آن صورت پیکان مستقیمِ نمودار از ریشه به لاتین نادرست است و باید از زیر گرهٔ یونانی می‌گذشت؛ دوم آن‌که اتیمانلاین به پیروی دِ فان آن را «واژه‌ای با خاستگاه نامعلوم» می‌خواند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/columba#Latin\",\n            \"https://www.etymonline.com/word/columbarium\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:264\", \"status\": \"partial\", \"note\": \"The 1975/76 New College main-dictionary page 264 is not available to me; what I could check is the appendix that Nourai's AHD references ultimately rest on, Watkins 1985 (AHD_watkins1985.txt): 'kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.]' — the claim is AHD's, but from the appendix (p.1521 area), not from p.264, and the AHD index confirms 'CoLuMBA kel-5, COLUMBARIUM kel-5'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. lat. s.v. columba (LAT.txt lines 13116-13135)\", \"stance\": \"supports\", \"note\": \"'columba, -ae f. et columbus, -i m.: colombe, pigeon ... La comparaison de lat. palumbes et de v. sl. golǫbь „pigeon“ (cf. r. goluboj „bleu“) engage à voir dans col- la désignation d'une couleur.'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p.316 s.v. Columba, columbarium\", \"stance\": \"supports\", \"note\": \"'columbarium, n., a dovecot. — L. columbarium, prop. neut. of the adjective columbarius, „pertaining to doves“, used as a noun, fr. columba.' and, s.v. Columba, the derivation from I.-E. *qel-, *qol- 'of a dark color'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 440 ff.\", \"stance\": \"supports\", \"note\": \"Same colour article; Latin columba is filed with Greek κόλυμβος there, and the -mb- from -mbʰ- is referred to Schwyzer Gr. Gr. I 333.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"Columbia, Colombia, Columbus, Columba, Colombo; columbarium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All of these do go back to Latin columba/columbus, and the chart's NOTE is right for most of them. Columbus is the Latinisation of the Genoese navigator's Italian name Cristoforo Colombo (Spanish Cristóbal Colón), Italian colombo being the regular reflex of Latin columbus 'dove'; Colombo is that Italian surname itself; Columbia is a 1730s coinage, the poetic name of the British colonies and then of the United States, Columbus + the Latin country-ending -ia (Columbia University 1784, District of Columbia 1791); Colombia is the South American state, so named in 1819 for Gran Colombia, again after Columbus. Columba is Latin 'dove' used as a proper name — the constellation Columba (1592) and St Columba of Iona (Old Irish colum, colomb 'dove' is itself an early loan from Latin columba, whence Irish colm, Welsh colomen). columbarium is different and did not come through Italian or Spanish: it is Latin columbārium, neuter of the adjective columbārius 'pertaining to doves', taken directly into English in the 1540s in the funerary sense 'sepulchre with niches for cinerary urns', so called from the resemblance of the niches to the pigeonholes of a dove-cote; the literal sense 'dove-cote' is only attested in English from 1881 (Etymonline).\",\n          \"derivation_fa\": \"همهٔ این واژه‌ها به‌راستی به columba/columbus لاتین «کبوتر» بازمی‌گردند و یادداشت نمودار («این واژه‌ها از راه ایتالیایی و اسپانیایی و زبان‌های دیگر به انگلیسی رسیده‌اند») دربارهٔ بیشترشان درست است. Columbus صورت لاتینی‌شدهٔ نام ایتالیایی کریستوفر کلمب، Cristoforo Colombo (اسپانیایی Cristóbal Colón) است و colombo بازماندهٔ قاعده‌مندِ columbus لاتین است؛ Colombo همان نام خانوادگی ایتالیایی است؛ Columbia برساختهٔ دههٔ ۱۷۳۰ است، از Columbus با پسوند لاتینی -ia؛ Colombia نام کشور آمریکای جنوبی از ۱۸۱۹ (کلمبیای بزرگ)؛ و Columba همان واژهٔ لاتین است که نام صورت فلکی و نام قدیس ایرلندی شده (colum ایرلندی کهن خود وام‌واژه‌ای از لاتین است). اما columbarium از راه ایتالیایی نیامده: در دههٔ ۱۵۴۰ یک‌راست از لاتین columbārium (صفتِ خنثای columbārius «وابسته به کبوتر») به انگلیسی رفته، در معنی «آرامگاهِ دارای طاقچه‌های خاکستردان»، به سبب شباهت طاقچه‌ها به لانه‌های کبوترخانه؛ معنی لفظی «کبوترخانه» تازه از ۱۸۸۱ در انگلیسی گواهی شده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Columbia\",\n            \"https://www.etymonline.com/word/columbarium\",\n            \"https://en.wiktionary.org/wiki/columba#Latin\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index and the kel-5 entry: 'CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5'; the appendix entry lists COLUMBA, COLUMBARIUM, COLUMBINE, CULVER as the English descendants of Latin columba. (Nourai gives 'AHD' here without a page, i.e. the same appendix.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.316-317 s.v. Columbiad, columbine, columbarium, culver\", \"stance\": \"supports\", \"note\": \"'Columbiad, n., an epic of America. — Formed with suff. -ad fr. Columbia, poetic name of North America, which was so called from its discoverer Christopher Columbus'; 'culver, n., a dove, a pigeon. — ME. culver, fr. OE. culfre, fr. VL. *columbra, contraction of columbula, dimin. of columba.'\"},\n            {\"src\": \"WEB\", \"where\": \"grep of WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"The available first volume of Webster's New Twentieth Century Dictionary does not reach the entries needed for these proper names.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Kel 5\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"IEW *kel- (kol-, kl̥-) with ḱ-suffix, 'Becher / goblet' (Pokorny 550-551 = WP I 442); modern handbooks rather posit a Mediterranean/Pre-Greek culture word\",\n      \"note\": \"The page reference is exact: Pokorny's article 'kel- (kol-, kl̥-) mit ḱ-Suffix „Becher“' begins on IEW p.550 (Page(s): 550-551), and the gloss 'cup, bowl' renders 'Becher' correctly; the material Pokorny lists is precisely Nourai's three IE nodes — Skt. kalaśa-, Gk. κύλιξ, Lat. calix. The verdict is 'plausible' rather than 'confirmed' because this 'root' is no longer generally accepted: the vowel alternation κύλιξ ~ κάλυξ ~ calix (a ~ u) is impossible in inherited Indo-European material, so Beekes takes κύλιξ as Pre-Greek and de Vaan doubts the Sanskrit connection; Wiktionary sums this up as 'it is also possible that all were borrowed from related substrate words'. The whole Semitic wing of this chart (Syriac, Persian, Arabic) is a separate matter and does not belong to this root at all — see the nodes.\",\n      \"note_fa\": \"ارجاع صفحه دقیق است: مدخل پوکورنی «kel- (kol-, kl̥-) با پسوند ḱ، به معنی Becher (جام)» از ص ۵۵۰ آغاز می‌شود (۵۵۰-۵۵۱) و برابرنهاد «cup, bowl» ترجمهٔ درستِ Becher است؛ همان سه شاخهٔ هندواروپایی نمودار (سنسکریت kalaśa-، یونانی κύλιξ، لاتین calix) در همان‌جا آمده‌اند. اما این ریشه امروز پذیرفتهٔ همگان نیست: تناوب واکه‌ای κύλιξ ~ κάλυξ ~ calix (a در برابر u) در واژگان موروثی هندواروپایی ناممکن است، از این رو بیکس κύλιξ را پیشایونانی می‌شمارد و دِ فان پیوند سنسکریت را بعید می‌داند؛ ویکی‌واژه نتیجه می‌گیرد که شاید هر سه از واژه‌های زیرلایه‌ای خویشاوند وام گرفته شده باشند. بنابراین با احتیاط پذیرفتنی است. افزون بر این، بال سامی این نمودار (سریانی، فارسی، عربی) اساساً به این ریشه بستگی ندارد؛ نگاه کنید به توضیح گره‌ها.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/calix#Latin\",\n        \"https://en.wiktionary.org/wiki/κύλιξ\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:550\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: kel-[7] (kol-, kl̥-) — Meaning: goblet — Note: with ḱ-suffix — Material: Old Indic kalaśa- m. „pot, pan, crock, pitcher, bowl“ (*koleko-, -oko-); gr. κύλιξ, -ικος „goblet“ (*kelik-) = Latin calix, -icis „deep bowl, goblet“ ... References: WP. I 442, WH. I 138 f. Page(s): 550-551.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 442 (qel- mit ḱ-Suffix „Becher“)\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt: '5. qel- (qol-, ql̥-) mit ḱ-Suffix „Becher“. Ai. kalaśa- m. „Topf, Krug, Schale“ (*qoleko-, -oko-); gr. κύλιξ, -ικος „Becher“ (*qeli-k-) ... = lat. calix, -icis „tiefe Schale, Becher, Kelch“ ... wozu vielleicht mit beweglichem s umbr. skalçe-ta, scalse-to.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'CALIX kal-1'\", \"stance\": \"partial\", \"note\": \"The Watkins appendix does NOT set up a *kel- 'cup' root: its index files CALIX under kal-1, i.e. the colour/vessel material is distributed differently, and calix is not among the English descendants of any kel- root. AHD therefore does not corroborate Nourai's 'Kel 5'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 5.33 'Cup', pp.348-349\", \"stance\": \"partial\", \"note\": \"'OE calic (reg. word for „cup“ in Gospels, as also Lat. calix in Vulgate), OHG kelih, NHG kelch, etc., fr. Lat. calix (above, 1)' — Buck records the Latin word and its Germanic/Celtic offspring but offers no PIE root for it, and gives no Iranian material.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"kalix\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no Greek word *kalix. The Greek cup-word of this root is κύλιξ, gen. κύλικος, transliterated kúlix/kylix — this is the form Pokorny 550 and Walde-Pokorny I 442 print ('gr. κύλιξ, -ικος „Becher“'), and it is the standard name of the Attic drinking cup. Nourai's 'kalix' looks like a conflation of κύλιξ with κάλυξ (kálux) 'husk, seed-vessel, calyx', which Pokorny files in the same article ('dazu gr. κάλυξ, -υκος „Fruchtkelch, Samenkelch“'), or a back-formation from Latin calix. I checked the printed page (book p.222, pdf 252, copy at data/verification/sources/refs/ocr/BOOK/252.png): the box really reads 'Greek | kalix : cup', so the JSON extraction is faithful and the odd form is the book's. On the substance the arrow is Pokorny's and defensible for its date; Beekes, however, calls κύλιξ Pre-Greek precisely because the a/u variation with calix and κάλυξ cannot be Indo-European.\",\n          \"derivation_fa\": \"واژه‌ای به صورت *kalix در یونانی وجود ندارد. واژهٔ یونانیِ این ریشه κύλιξ (حالت اضافی κύλικος) است، یعنی kúlix / kylix — همان صورتی که پوکورنی در ص ۵۵۰ و والده-پوکورنی در جلد یکم ص ۴۴۲ آورده‌اند و نام شناختهٔ جامِ شرابِ آتنی است. «kalix» ظاهراً آمیزه‌ای است از κύλιξ با κάλυξ «کاسبرگ، غلاف میوه» (که پوکورنی آن را در همین مدخل می‌آورد) یا صورتی ساخته‌شده از روی calix لاتین. صفحهٔ چاپی را دیدم (کتاب ص ۲۲۲؛ تصویر در data/verification/sources/refs/ocr/BOOK/252.png): در خانهٔ نمودار به‌روشنی «kalix» چاپ شده است؛ پس خطای خوانش اسکن نیست، خطای چاپی خود کتاب است. از نظر محتوا پیکان همان چیزی است که پوکورنی می‌گوید، هرچند بیکس κύλιξ را پیشایونانی می‌داند، دقیقاً به دلیل همین تناوب a/u که در هندواروپایی ناممکن است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"kalix\",\n          \"correct_form\": \"kúlix (Ancient Greek κύλιξ, gen. κύλικος)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/κύλιξ\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:550\", \"status\": \"partial\", \"note\": \"POK_full.txt, 'goblet' root, Page(s) 550-551: 'gr. κύλιξ, -ικος „goblet“ (*kelik-) = Latin calix'. Pokorny supports a Greek cup-word of this root on exactly the cited page, but the form is κύλιξ, not the 'kalix' the book prints.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 442\", \"stance\": \"partial\", \"note\": \"'gr. κύλιξ, -ικος „Becher“ (*qeli-k-; die Entwicklung zu -υλ- läßt Güntert Abl. 32 durch das folgende i bedingt sein)' — again κύλιξ, with an explicit note on the -υ- vocalism; no *kalix anywhere.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. calyx, cylix\", \"stance\": \"partial\", \"note\": \"'calyx, n. — L., fr. Gk. κάλυξ, „the cup or calyx of a flower“, which stands in gradational relationship to κύλιξ, „cup, drinking cup“, and is cogn. with L. calix ... OI. kalaśaḥ „pot, cup“, kalikā „bud“'; and a separate entry 'cylix, n., an ancient drinking cup (Greek antiq.)'. Klein keeps κάλυξ and κύλιξ apart, exactly the distinction the book's 'kalix' blurs.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Syriac\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The empty Syriac box stands for Classical Syriac ܟܣܐ kāsā 'cup', the word both of Nourai's references name at this point (Addi Shir s.v. كأس: 'وهو بالفارسية كاسه وبالآرامية ܟܣܐ وبالبابلية kāsu'; Jeffery, FVQ 245: 'in Aram. kāsā ... and Syr. kāsā'). What no source supports is the arrow drawn INTO this box: nobody derives Syriac kāsā from Greek κύλιξ. Phonetically the two are irreconcilable (κ-υ-λ-ι-κ- with an -l- and a final velar, against a triliteral k-ʔ-s with a sibilant), and the Semitic word is old and widespread on its own account — Akkadian kāsu(m), Hebrew kōs, Ugaritic (Ras Shamra) ks, Jewish Aramaic kāsā — so it is either Proto-Semitic *kaʔs- or an ancient Mesopotamian culture word, and Jeffery calls the Aramaic origin of the family beyond doubt. The Greek→Syriac step is therefore Nourai's own construction, made to hang the Persian and Arabic cup-words on his Indo-European root; it should be removed.\",\n          \"derivation_fa\": \"خانهٔ خالیِ «سریانی» در نمودار به واژهٔ سریانی ܟܣܐ kāsā «جام، پیاله» اشاره دارد؛ همان واژه‌ای که هر دو مرجعِ نورایی در همین‌جا نام می‌برند (ادّی شیر ذیل «كأس»: «وهو بالفارسیة کاسه وبالآرامیة ܟܣܐ وبالبابلیة kāsu»؛ جفری، واژه‌های دخیل در قرآن، ص ۲۴۵). آنچه هیچ منبعی تأیید نمی‌کند پیکانِ ورودی به این خانه است: کسی kāsā سریانی را از κύλιξ یونانی نمی‌گیرد. از دید آوایی این دو آشتی‌ناپذیرند (κ-υ-λ-ι-κ- با لام و کافِ پایانی در برابر ریشهٔ سه‌همخوانیِ ک-ء-س) و واژهٔ سامی خود کهن و گسترده است: اکدی kāsu(m)، عبری kōs، اوگاریتی ks، آرامی یهودی kāsā. پس ریشه یا سامی آغازین *kaʔs- است یا واژه‌ای فرهنگی از بین‌النهرین باستان. این پیوند ساختهٔ خود نورایی است تا واژه‌های فارسی و عربی را به ریشهٔ هندواروپایی‌اش بیاویزد و پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/كأس\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AFM:131\", \"status\": \"partial\", \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, first entry of باب الكاف (AFM_pages.txt form-feed leaf 132; the leaf→printed offset in this scan is only approximate, ≈ leaf − 8, so this is p.124-131 — the cited 131 is at the edge of the plausible range): '( كأس ) أي القدح وهو بالفارسية كاسه وبالآرامية ܟܣܐ وبالبابلية [kāsu] ... وبالكردية كاسك ... فتكون الفارسية قد أخذت من اللغات السامية ... ܟܘܙܐ بالسريانية'. Addi Shir does supply the Syriac word and does route it to Persian — but from the Semitic side, with no mention whatever of Greek κύλιξ.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qurʾān, p.245 (FVQ_pages.txt leaf 262; printed = leaf − 17)\", \"stance\": \"partial\", \"note\": \"s.v. كأس: 'This is not a S. Semitic word, as it is entirely lacking in Eth. and without a root and of uncertain plu. in Arabic. There can thus be little doubt of its Aram. origin. The Heb. word is kōs, while in the Ras Shamra texts we have ks, and in Aram. kāsā ... and Syr. kāsā.' Jeffery gives the Syriac word but derives the family within Semitic; no Greek source is contemplated.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, p.~167 (AFA.txt lines 5997-6002)\", \"stance\": \"contradicts\", \"note\": \"'Schon in der Form zeigt seinen aramäischen Ursprung [كأس] „Becher“ Zuh. 9,7; ʿAlq. 13,41; Divān Leb. 132,12 ... Es ist syr. kās(ā)' — Fraenkel makes the Aramaic word the source, not the borrower, and knows nothing of a Greek etymon.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. chalice, calyx\", \"stance\": \"silent\", \"note\": \"Klein traces the calix/κύλιξ family only into Latin, Germanic and Old English (chalice < OF calice < L. calicem); he connects no Semitic word with it.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"kâseh; kŭzeh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both Persian words are real with the glosses given (Dehkhoda کاسه 'ظرفی باشد که چیزی در آن خورند'; کوزه 'ظرفی است گردن‌دراز که در آن آب نگهدارند'; the parenthetic «کاس ۱، کاسبرگ» and «کوز ۱» are Moʿin-style cross-references, kāsbarg being the botanical 'sepal, calyx'). The chart's arrow, however, is only half defensible and only for one of the two words. (a) کاسه kāse: Jeffery FVQ 245-246 does say 'the Syr. kāsā seems to be the source of the Pers. kāsa', Addi Shir says the same ('فتكون الفارسية قد أخذت من اللغات السامية'), and Moʿin actually tags the headword [ازع.] = 'from Arabic', with Farhang-e Neẓām quoted by Dehkhoda: 'این لفظ مأخوذ از کاس عربی است'. So a Semitic source for kāse is a real, respectable opinion — but the current Iranian-side view (Wiktionary, following Hasandust) is native: New Persian kāse < Middle Persian *kāsag (compare Balochi kāsag 'bowl'), possibly from Old Persian kāsaka- 'semi-precious stone, glass' (the word behind MP kāskēn 'of lapis lazuli' in MacKenzie and Nyberg), with the regular MP -ag > NP -a/-e. Either way the ultimate Greek κύλιξ of the chart is not in play. (b) کوزه kuze: here the arrow is simply reversed. Hübschmann, Persische Studien no.872 (p.89): 'Np. kūza „irdener Krug, Kanne“ ... ist abgeleitet mittelst des Suffixes -a (= phl. -ak) von kūz = arm. LW. kuz „Krug, Kanne“ = arab. LW. kūz „kleiner Krug“ und geht mit diesem auf ein ap. *kūza (oder *kūja) zurück' — i.e. Old Persian *kūza > kūz + -ag > NP kūza, and Armenian kuž and Arabic kūz are borrowings FROM Persian; Wiktionary agrees, listing Syriac ܟܘܙܐ kūzā and Arabic كوز among the 'Iranian borrowings' and connecting the word to کوژ/گوژ 'bent, curved' (the shape of the vessel). Verdict: disputed — Syriac→Persian is defensible for kāse only, and for kuze the traffic goes the other way.\",\n          \"derivation_fa\": \"هر دو واژه واقعی‌اند و معنایشان درست است (دهخدا: «کاسه: ظرفی باشد که چیزی در آن خورند»؛ «کوزه: ظرفی است گردن‌دراز که در آن آب نگهدارند»)؛ آنچه در پرانتز آمده («کاس ۱، کاسبرگ» و «کوز ۱») ارجاع‌های درون‌فرهنگیِ سبک معین است. اما پیکان نمودار تنها نیمی از راه و تنها برای یکی از دو واژه پذیرفتنی است. الف) «کاسه»: جفری (ص ۲۴۵-۲۴۶) به‌روشنی می‌گوید سریانی kāsā خاستگاه فارسی kāsa می‌نماید، ادّی شیر نیز همین را می‌گوید، و معین خودِ سرواژه را [ازع.] یعنی «از عربی» نشان کرده و دهخدا از فرهنگ نظام نقل می‌کند «این لفظ مأخوذ از کاس عربی است». پس وام‌گیری از سامی نظری جدی است — ولی دیدگاه ایرانی‌شناسیِ امروز (ویکی‌واژه به پیروی حسن‌دوست) آن را ایرانی می‌داند: فارسی نو کاسه از فارسی میانهٔ *kāsag (سنجید با بلوچی kāsag «کاسه»)، شاید از پارسی باستان kāsaka- «سنگ نیمه‌گران‌بها، شیشه» (همان واژه‌ای که در پهلوی kāskēn «از لاجورد» بازتاب یافته: مکنزی، نیبرگ)، با تحول قاعده‌مندِ ‑ag پهلوی به ‑هٔ فارسی نو. در هر دو حال κύλιξ یونانی در میان نیست. ب) «کوزه»: اینجا جهت پیکان یکسره وارونه است. هوبشمان (پژوهش‌های فارسی، شمارهٔ ۸۷۲، ص ۸۹): «فارسی نو kūza از kūz با پسوند ‑a (= ‑ak پهلوی) ساخته شده و kūz برابر است با وام‌واژهٔ ارمنی kuz و وام‌واژهٔ عربی kūz، و همگی به پارسی باستانِ *kūza بازمی‌گردند» — یعنی سریانی و عربی از فارسی وام گرفته‌اند نه برعکس؛ ویکی‌واژه نیز kūzā سریانی و کوز عربی را «وام‌واژه‌های ایرانی» می‌شمارد و واژه را با «کوژ/گوژ» (خمیده) می‌پیوندد. پس: پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/کاسه\",\n            \"https://en.wiktionary.org/wiki/کوزه\",\n            \"https://abadis.ir/fatofa/کاسه/\",\n            \"https://abadis.ir/fatofa/کوزه/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AFM:131\", \"status\": \"partial\", \"note\": \"Addi Shir, باب الكاف (AFM_pages.txt leaf 132): '( كأس ) ... وهو بالفارسية كاسه ... أظن أن الأصل مأخوذة من ... فتكون الفارسية قد أخذت من اللغات السامية ... ܟܘܙܐ بالسريانية والبابلية'. He does route Persian kāse from the Semitic word (as Nourai's Syriac→Persian arrow requires), but as a Semitic, not a Greek, word — and he attaches kūz(a) to Syriac kūzā, which Hübschmann reverses.\"},\n            {\"ref\": \"MON\", \"status\": \"contradicts\", \"note\": \"Moʿin, Farhang-e Farsi s.v. کاسه (read via abadis.ir, section فرهنگ معین): '(س ) [ازع . ] (اِ. ) ۱ - پیاله ، ظرف' — the tag [ازع.] means 'from Arabic', i.e. Moʿin makes Persian kāse a loan FROM Arabic kaʾs, the exact opposite of the Persian→Arabic arrow Nourai draws below this node. His entry for کوزه, '(زَ یا زِ ) (اِ. ) ظرف دسته‌دار یا بی‌دستهٔ سفالین', carries no foreign tag at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no.872, p.89 (HUB.txt leaf 99)\", \"stance\": \"contradicts\", \"note\": \"'Np. kūza „irdener Krug, Kanne“ = afgh. kūza ... ist abgeleitet mittelst des Suffixes a (= phl. ak) von kūz = arm. LW. kuz „Krug, Kanne“ = arab. LW. kūz „kleiner Krug“ und geht mit diesem auf ein ap. *kūza (oder *kūja) zurück.' Hübschmann makes the Armenian and Arabic forms loans from Persian.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. kāskēn (PHD.txt line 426)\", \"stance\": \"partial\", \"note\": \"'kāskēn [kʾskyn] lapis lazuli ... ~ēn blue-green; of lapis lazuli' — MacKenzie has no Middle Persian kāsag 'bowl', so the MP stage of کاسه is a reconstruction; what he does record is the derivative of OP kāsaka-.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. kāsakēn (NYB_vol2_glossary.txt line 2257)\", \"stance\": \"partial\", \"note\": \"'kāsakēn ... OP kāsaka-, adj. of kāsaka-, defined by Kent as „a semi-precious stone“' — confirms the Old Persian base that Wiktionary proposes as the source of kāse, and again shows no Semitic or Greek route in the Middle Iranian record.\"},\n            {\"src\": \"HRN\", \"where\": \"grep of HRN.txt for kasa / kuza / kaland\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered entry for kāsa or kūza (the hits for 'kas' are Av. kasa- 'armpit' and ā-kās 'perceive'); his silence is why Hübschmann's Persische Studien no.872 supplies the kūza entry as an addendum to Horn.\"},\n            {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for کاسه / کوزه\", \"stance\": \"silent\", \"note\": \"Aryanpur's Farhang-e rishe-hā only mentions کوزه in passing as a gloss of خم/خنب (line 7192) and کاسه as a meaning of an unrelated root (line 13143); no headword for either word.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"ka`s\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic كَأْس kaʾs 'cup, wine-glass' is real (Qurʾān xxxvii.45, lii.23, lvi.18, lxxvi.5,17, lxxviii.34, always of the cups of Paradise); Nourai's backtick transcribes the hamza, not an ʿayn. But the arrow Persian → Arabic is rejected by every source that actually discusses the word, including the two Nourai cites. Jeffery (FVQ 245-246), whose Persian translation is the VDQ Nourai quotes, writes: 'This is not a S. Semitic word ... There can thus be little doubt of its Aram. origin ... As the Syr. kāsā seems to be the source of the Pers. kāsa, we may take it as most probable that the Arabic also was borrowed at an early period from the same source' — i.e. Arabic and Persian are parallel borrowings from Aramaic, and Arabic did not take the word from Persian. Fraenkel says the form itself betrays its Aramaic origin. Wiktionary sets it beside Akkadian kāsu(m), Hebrew kōs and the Aramaic forms, either from Proto-Semitic *kaʔs- or a post-Proto-Semitic borrowing from Aramaic, the medial hamza being possibly a hypercorrection. If anything the chart's arrow should point the other way (Arabic/Aramaic → Persian kāse), which is exactly what Moʿin's [ازع.] tag on کاسه says.\",\n          \"derivation_fa\": \"واژهٔ عربی «کَأْس» (جام، پیالهٔ شراب) واقعی است و در قرآن شش بار در وصف جام‌های بهشتی آمده (صافات ۴۵، طور ۲۳، واقعه ۱۸، انسان ۵ و ۱۷، نبأ ۳۴)؛ علامت ` در آوانگاری نورایی همزه است نه عین. اما پیکانِ «فارسی ← عربی» را هیچ‌یک از منابع، از جمله همان دو مرجعی که نورایی آورده، تأیید نمی‌کند. جفری (که VDQ ترجمهٔ فارسی کتاب اوست) در ص ۲۴۵-۲۴۶ می‌نویسد: «این واژه سامیِ جنوبی نیست ... در آرامی‌بودن خاستگاهش تردیدی نیست ... و چون kāsā سریانی خاستگاه kāsa فارسی می‌نماید، محتمل‌تر آن است که عربی نیز در دورانی کهن از همان سرچشمه وام گرفته باشد» — یعنی عربی و فارسی هر دو جداگانه از آرامی وام گرفته‌اند. فرنکل می‌گوید خودِ ساختِ واژه خاستگاه آرامی آن را آشکار می‌کند. ویکی‌واژه آن را کنار اکدی kāsu(m)، عبری kōs و صورت‌های آرامی می‌نشاند. اگر پیکانی باید کشیده شود، جهتش وارونه است (عربی/آرامی ← کاسهٔ فارسی)، همان که معین با نشانهٔ [ازع.] گفته است. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/كأس\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AFM:131\", \"status\": \"contradicts\", \"note\": \"Addi Shir lists كأس as an arabicised Persian word (that is the whole point of his book), but his own note undercuts the claim: '( كأس ) أي القدح وهو بالفارسية كاسه وبالآرامية ܟܣܐ وبالبابلية [kāsu] ... فتكون الفارسية قد أخذت من اللغات السامية' — 'so the Persian will have taken it from the Semitic languages' (AFM_pages.txt leaf 132, باب الكاف).\"},\n            {\"ref\": \"VDQ:355\", \"status\": \"supports\", \"note\": \"VDQ is Badreʾi's Persian translation of Jeffery's FVQ (no scan online; refs_online.json gives kind=website with a JavaScript-only viewer), so I checked the identical passage in the English original, FVQ p.245-246 (FVQ_pages.txt leaves 262-263): the entry exists and discusses كأس exactly where Nourai points — but it derives the Arabic from Aramaic, not from Persian: 'As the Syr. kāsā seems to be the source of the Pers. kāsa, we may take it as most probable that the Arabic also was borrowed at an early period from the same source.' So the citation is genuine while its content contradicts the arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, p.~167\", \"stance\": \"contradicts\", \"note\": \"'Schon in der Form zeigt seinen aramäischen Ursprung [كأس] „Becher“ Zuh. 9,7 ... Es ist syr. kās(ā)' — the Arabic word is Aramaic, with no Persian intermediary.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p.245-246\", \"stance\": \"contradicts\", \"note\": \"See ref_check above; Jeffery also cites Fraenkel, Fremdw. 171 and Zimmern, Akkad. Fremdw. 34 for the Aramaic/Akkadian pedigree, and notes D. H. Müller's dissenting view that 'the medial Hamza proves it to be genuine Arabic'.\"},\n            {\"src\": \"KLN\", \"where\": \"grep of KLN_1966.txt\", \"stance\": \"silent\", \"note\": \"Klein has no entry for Arabic kaʾs and connects no Semitic word to calix/κύλιξ.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"calix\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin calix, gen. calicis, m. 'deep bowl, goblet, cup' is real and correctly glossed; it is the ancestor of Ecclesiastical Latin calix 'chalice', of Old High German chelih > German Kelch, of Old English calic, and, through Old French calice/chalice, of English chalice (Klein s.v. chalice). Nourai's arrow makes it a descendant of Greek κύλιξ. That is the ancient Roman opinion — Ernout-Meillet: 'Les Latins voient dans calix un emprunt au gr. κύλιξ, ainsi Priscien, GLK II 167,1' — but not the handbook one: Pokorny and Walde-Pokorny write 'gr. κύλιξ = lat. calix', an equation of cognates from the same *kel-i-k-, so the Latin word should hang from the ROOT beside the Greek one, not below it. Ernout-Meillet continue 'En réalité, le mot peut être d'origine indo-européenne, ancien *k'lik-', pointing to Umbrian skalçeta/scalse-to with mobile s-; de Vaan (via Wiktionary) reconstructs Proto-Italic *(s)kalik- but concedes 'alternatively, borrowed from Ancient Greek κύλιξ ... but it is also possible that all were borrowed from related substrate words'. So the arrow is one of three live options, hence plausible.\",\n          \"derivation_fa\": \"واژهٔ لاتینی calix (اضافی calicis) «کاسهٔ گود، جام» واقعی است و معنایش درست آمده؛ همین واژه نیای calix کلیسایی «جام عشای ربانی»، chelih آلمانی کهن و Kelch امروزی، calic انگلیسی کهن، و از راه فرانسهٔ کهن calice/chalice نیای chalice انگلیسی است (کلاین ذیل chalice). نورایی آن را از κύλιξ یونانی می‌گیرد. این همان نظر رومیان باستان است — ارنو-مِیه: «رومیان calix را وام‌واژه‌ای از κύλιξ می‌دانستند، چنان‌که پریسکیانوس گفته» — اما نظر فرهنگ‌های ریشه‌شناسی نیست: پوکورنی و والده-پوکورنی می‌نویسند «κύλιξ یونانی = calix لاتین»، یعنی هر دو هم‌ریشه‌اند و از *kel-i-k- آمده‌اند؛ پس در نمودار باید کنار گرهٔ یونانی و زیر ریشه می‌نشست نه زیر یونانی. ارنو-مِیه می‌افزاید که واژه می‌تواند خاستگاه هندواروپایی داشته باشد (*k'lik-، با گواهی امبریایی skalçeta با s متحرک) و دِ فان *(s)kalik- ایتالیایی آغازین بازمی‌سازد و در عین حال احتمال وام‌گیری از یونانی یا وام‌گیری هر سه از زیرلایه‌ای مشترک را باز می‌گذارد. بنابراین با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/calix#Latin\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:550\", \"status\": \"partial\", \"note\": \"POK_full.txt, 'goblet' root (550-551): 'gr. κύλιξ, -ικος „goblet“ (*kelik-) = Latin calix, -icis „deep bowl, goblet, calix“ (from calix comes Old High German chelih, Modern High German Kelch)'. Pokorny has the Latin word on exactly the cited page but joins it to the Greek with '=' (cognate), not with a derivation arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. calix (LAT.txt lines 8717-8732)\", \"stance\": \"partial\", \"note\": \"'Les Latins voient dans calix un emprunt au gr. κύλιξ, ainsi Prisc., GLK II 167,1 ... En réalité, le mot peut être d'origine indo-européenne, ancien *k'lik-, outre κύλιξ (dont l'u s'explique par l'existence de *k°lu-) et κάλυξ, on rapproche skr. kalaśaḥ „pot, coupe“ et kalikā „bouton de fleur“.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 442\", \"stance\": \"partial\", \"note\": \"'gr. κύλιξ, -ικος „Becher“ (*qeli-k-) = lat. calix, -icis „tiefe Schale, Becher, Kelch“ (oder -ix, -icis für *-ex, -icis ... der Nom. -ix dann unterstützt durch gr. κύλιξ; aus calix stammt ahd. chelih, nhd. Kelch)' — the equation is again one of cognates, with only the shape of the nominative said to be supported by Greek.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. chalice, calicle, calyx\", \"stance\": \"supports\", \"note\": \"'chalice, n., a cup. — OF. chalice, a collateral form of calice (F. calice), fr. L. calicem, acc. of calix, „cup, goblet“, which is cogn. with Gk. κάλυξ ... κύλιξ, „cup, drinking cup“' — Klein, like Pokorny, says cognate ('cogn. with'), not derived.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 5.33 'Cup', p.349\", \"stance\": \"supports\", \"note\": \"'OE calic (reg. word for „cup“ in Gospels, as also Lat. calix in Vulgate), OHG kelih, NHG kelch, etc., fr. Lat. calix' — documents the Latin word's spread but takes no position on the Greek relation.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"kalasah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit कलश kalaśa- m. is real, but its meaning is 'pot, jar, water-jar, dish' (a ritual water-pot in Hindu usage) rather than narrowly 'cup'; Pokorny 550 glosses it 'Topf, Krug, Schale'. The chart hangs it directly on the root, which is what Pokorny does: he reconstructs *koleko-/-oko-, a parallel ḱ-suffix formation beside Greek κύλιξ (*kelik-) and Latin calix, with -ś- from the palatalised velar of the suffix. Pokorny himself flags the difficulty in the same paragraph — Sanskrit kalikā 'bud' is said to be 'different in the guttural of the suffix' from kalaśa- — and de Vaan (reported by Wiktionary) finds the whole Sanskrit connection unlikely, since a *k-suffix appearing in three branches with three different vowels is more easily explained as three separate borrowings of a Mediterranean vessel-word. Hence plausible: the affiliation is Pokorny's, on exactly the cited page, but it is one of the weaker links in his article.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت कलश (kalaśa-) واقعی است، ولی معنای آن «دیگ، کوزه، خمرهٔ آب، ظرف» است (در آیین هندو کوزهٔ آبِ آیینی) نه دقیقاً «جام»؛ پوکورنی در ص ۵۵۰ آن را «Topf, Krug, Schale» معنی می‌کند. نمودار آن را یک‌راست به ریشه می‌بندد و این همان کاری است که پوکورنی می‌کند: بازسازی *koleko-/-oko-، ساختی موازی با κύλιξ یونانی (*kelik-) و calix لاتین، که در آن ś سنسکریت از کامی‌شدن k پسوند پدید آمده است. خود پوکورنی در همان بند به دشواری کار اشاره می‌کند و می‌گوید kalikā «غنچه» در همخوان پسوند با kalaśa- تفاوت دارد؛ دِ فان نیز (به نقل ویکی‌واژه) پیوند سنسکریت را بعید می‌داند، چون پسوندی که در سه شاخه با سه واکهٔ گوناگون ظاهر شود آسان‌تر با سه وام‌گیریِ جداگانه از یک واژهٔ فرهنگیِ مدیترانه‌ای توضیح داده می‌شود. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/calix#Latin\",\n            \"https://en.wiktionary.org/wiki/कलश\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:550\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'goblet' root (Page(s): 550-551): 'Material: Old Indic kalaśa- m. „pot, pan, crock, pitcher, bowl“ (*koleko-, -oko-)' — first item of the article, exactly as the chart draws it, though glossed more widely than 'cup'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 442\", \"stance\": \"supports\", \"note\": \"'Ai. kalaśa- m. „Topf, Krug, Schale“ (*qoleko-, -oko-)', with the caveat at the end of the article: 'ai. kalikā „Knospe“ ... svare im Gutt. des Suffixes von kalaśa- verschieden'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary, grep for kalasa\", \"stance\": \"silent\", \"note\": \"Mann has no *kel-/*kal- 'goblet' entry answering to Pokorny's; his kal- entries (leaves 266-267, cols. 464-466) are 'slope', 'bright, white', 'call', 'fix', 'thrust', 'strike', 'lure' — no vessel root, so Mann gives Nourai's 'Kel 5' no support.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. calix\", \"stance\": \"supports\", \"note\": \"'on rapproche skr. kalaśaḥ „pot, coupe“ et kalikā „bouton de fleur“' — E-M keeps the Sanskrit comparison, but only as a rapprochement.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Kel 6\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kelh₂- 'to strike, beat, break' (Pokorny kel-3 'schlagen, hauen', IEW 545-547 = WP I 436 ff.; Watkins/AHD kel-1 'to strike, cut')\",\n      \"note\": \"Root, language label, gloss and page are all right: Pokorny's kel-3 'to hit, cut down' runs from p.545, the number cited, and its own note ('separation from kel- „prick“ and from skel- „cut, clip“ is barely feasible') covers Nourai's added 'stab'. Watkins files the same root as kel-1 'To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. [Pok. 3 kel- 545]' — and the four western nodes of this chart (gladius, calamitas, klōn, and thence gladiator, calamity, clone) are simply the contents of that AHD article, which is why every one of them carries the reference AHD:1521. In modern notation the root is *kelh₂-, still current (LIV, de Vaan, Schrijver). The numbering 'Kel 6' is Nourai's own running count of his kel- roots, not Pokorny's.\",\n      \"note_fa\": \"ریشه، برچسب زبان، معنی و شمارهٔ صفحه همگی درست‌اند: مدخل kel-3 پوکورنی «زدن، بریدن، فروکوفتن» از همان ص ۵۴۵ آغاز می‌شود و یادداشت خود پوکورنی («جدا کردن این ریشه از kel- „سوراخ کردن“ و از skel- „بریدن“ به‌سختی شدنی است») معنی افزودهٔ «stab» را پوشش می‌دهد. واتکینز همین ریشه را زیر kel-1 «زدن، بریدن؛ پایهٔ فرضی مشتقاتی که به چیز شکسته یا بریده‌شده، شاخه، تکه‌چوب اشاره دارند [Pok. 3 kel- 545]» آورده و چهار گرهٔ غربی این نمودار (gladius، calamitas، klōn و از آن‌ها gladiator، calamity، clone) دقیقاً محتوای همان مدخل AHD است؛ از همین رو همهٔ آن‌ها ارجاع AHD:1521 دارند. در نگارش امروزی ریشه *kelh₂- است و همچنان معتبر (LIV، دِ فان، شرایور). شمارهٔ «Kel 6» شمارش شخصی نورایی است نه شمارهٔ پوکورنی. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/gladius#Latin\",\n        \"https://en.wiktionary.org/wiki/calamitas#Latin\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:545\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: kel-3, kelə-, klā- extended klad- — Meaning: to hit, cut down — Note: separation from kel- „prick“ and from skel- „cut, clip“ is barely feasible ... Latin clades „injury; damage, mischief, beating“ ... Latin gladius „sword“ from Celtic ... References: WP. I 436 ff. ... Page(s): 545-547.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, kel-1\", \"stance\": \"supports\", \"note\": \"'kel-1. To strike, cut ... 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE ... III. Extended form *kelə-. 1. Zero-grade form *klā- in: a. Greek klā- ... (ii) Greek klōn (< *klā-ōn), twig: CLONE ... d. suffixed form *klə-mo- in Latin calamitās, injury, damage, loss: CALAMITY. [Pok. 3 kel- 545.]' — the entire western half of the chart in one paragraph.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 436 ff.\", \"stance\": \"supports\", \"note\": \"The Walde-Pokorny article behind IEW 545-547; it carries 'lat. gladius aus dem Kelt., Vendryes Mél. Saussure 310 f.' and the clades material.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, cols. 464-465, kal- (4)/(5)/(6)\", \"stance\": \"supports\", \"note\": \"'kal- (6) „strike“. Same as (4) and (5)? Cf. WP I, 437 — Per. cf. kaland „spade“; Arm. cf. kal „threshing floor“; Gk. kalís „adze“; Lat. cf. hordi-calia; ON heljast; OCS koljǫ, klati („stab“)' — Mann's root gloss 'strike' plus 'stab' is almost word for word Nourai's 'to strike, cut, stab'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 20.27 'Sword', p.1180 f.\", \"stance\": \"supports\", \"note\": \"'Ir. claideb, NIr., Gael. claidheamh ..., W. cleddyf, Br. kleze, Corn. clethe, beside Lat. gladius (fr. Celtic): Ir. claidim, W. claddu „dig“, Lat. clādēs „damage, injury“, Skt. khadga- „sword“, Lith. kalti.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"kaland, kolang\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Persian forms are real and are variants of one word: کلند kaland/koland and کلنگ kolang, the iron digging tool. Dehkhoda s.v. کلنگ: 'دست‌افزاری باشد که چاه‌جویان و گل‌کاران بدان زمین و دیوار کنند (برهان) ... و به این معنی کلند نیز آمده (آنندراج)'; Moʿin '(کُ لَ) (اِ.) ۱- آلت آهنی نوک‌تیز که از آن برای کندن جاهای سفت زمین استفاده می‌کنند', with no foreign-origin tag. The etymology the chart gives is exactly Mann's: IEC col.464, 'kal- (6) „strike“ ... Per. cf. kaland „spade“', i.e. the Iranian reflex of PIE *kelh₂- 'to strike' (which regularly keeps k- before the back vowel *o/*a, unlike čarmeh in the first chart) plus an instrument formation in -and/-ang; the two Persian endings are the familiar -and ~ -ang doublet (compare کلند/کلنگ, and the dialectal Kerman کلنت kolant). Wiktionary independently gives 'کلنگ ... From Proto-Indo-European *kelh₂- „to beat, strike, break“. Compare کلند (koland)'. The word travelled outwards, not inwards: Old Anatolian Turkish külünk 'pickaxe' is attested from the 13th c., Armenian kʻlung, Turkmen külüň, Romanian chilom are all borrowings from Persian. One gloss quibble: kolang/kaland is a pickaxe or mattock (معول), not a spade (بیل) — Mann's 'spade' is the loose rendering Nourai copied. The homonymous کلنگ 'crane (the bird)' is a different word.\",\n          \"derivation_fa\": \"هر دو صورت واقعی‌اند و دو گونهٔ یک واژه‌اند: «کلند» و «کلنگ»، ابزار آهنیِ کندن. دهخدا ذیل کلنگ: «دست‌افزاری باشد که چاه‌جویان و گل‌کاران بدان زمین و دیوار کنند (برهان) ... و به این معنی کلند نیز آمده (آنندراج)»؛ معین: «آلت آهنی نوک‌تیز که از آن برای کندن جاهای سفت زمین استفاده می‌کنند»، بی هیچ نشانهٔ وام‌واژگی. ریشه‌شناسیِ نمودار همان است که مان در ستون ۴۶۴ آورده: «kal- (6) „زدن“ ... فارسی kaland „بیل“»، یعنی بازتاب ایرانیِ *kelh₂- هندواروپایی («زدن») — که برخلاف «چرمه» در نمودار نخست، k آن پیش از واکهٔ پسین کامی نشده — به‌علاوهٔ پسوند ابزارساز ‑ند/‑نگ (همان دوگانهٔ آشنای کلند/کلنگ، و گونهٔ کرمانیِ «کلنت»). ویکی‌واژه نیز جداگانه می‌نویسد: «کلنگ از هندواروپایی آغازین *kelh₂- „کوبیدن، زدن، شکستن“؛ سنجید با کلند». جهت وام‌گیری هم بیرون‌سو است نه درون‌سو: külünk ترکیِ آناتولیایی کهن از سدهٔ هفتم هجری، kʻlung ارمنی، külüň ترکمنی و chilom رومانیایی همه از فارسی گرفته شده‌اند. تنها ایراد خرد، برابرنهاد انگلیسی است: «کلنگ» معول است نه بیل؛ «spade» را نورایی از مان برداشته. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/کلنگ\",\n            \"https://abadis.ir/fatofa/کلنگ/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:464\", \"status\": \"supports\", \"note\": \"Mann, An Indo-European Comparative Dictionary, col. 464 (IEC.txt form-feed leaf 266, whose marginal column number is 464): 'kal- (6) „strike“. Same as (4) and (5)? Cf. WP I, 437 — Per. cf. kaland „spade“; Arm. cf. kal, o-st. („threshing floor“, but equally to kal- (5)); Gk. kalís „adze“; Lat. cf. hordi-calia; ON heljast; OCS koljǫ, klati („stab“, equally to (5)).' The citation is exact, page and all.\"},\n            {\"ref\": \"MON:3037\", \"status\": \"supports\", \"note\": \"Moʿin's lexicon volumes are not on disk in the 6-volume pagination Nourai cites, so I read the entry through abadis.ir (section فرهنگ معین): 'کلنگ (کُ لَ ) (اِ. ) ۱ - آلت آهنی نوک تیز که از آن برای کندن جاهای سفت زمین استفاده می کنند. ۲ - دُرنا.' The word, the sense and the absence of a foreign-origin tag are as Nourai's arrow requires; the printed page number 3037 (vol. 3, ک section) I could not confirm directly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"grep of HRN.txt for kaland / kulang\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered entry for kaland or kulang.\"},\n            {\"src\": \"HUB\", \"where\": \"grep of HUB.txt for kaland / kulang\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien likewise has nothing on the word.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt near [pdf page 70] (printed p. 71)\", \"stance\": \"partial\", \"note\": \"Aryanpur's Farhang-e rishe-hā has a page whose Persian gloss line reads '۱- معنی این واژه در هند و اروپایی و اکثر زبان‌های دیگر: کلنگ' with Avestan/Old Persian/Pahlavi columns; the OCR of the page is too broken to identify the headword or the root with confidence, so I record it only as a probable parallel treatment.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ s.v. کلند, quoted by Dehkhoda\", \"stance\": \"supports\", \"note\": \"'کُلَند یا کَلَند، دست‌افزار نقب‌کنان و گل‌کاران و سنگ‌تراشان است که با آن زمین را می‌کنند و به آن کلنگ نیز گویند. (برهان)' — Borhan makes kaland and kolang the same tool, exactly as the chart's single node does.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"gladius\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin gladius, -ī m. 'sword' (the Roman legionary's short sword) is real and correctly glossed, and it does belong to this root — but not by direct descent. Every authority makes it a borrowing from Celtic: Pokorny 546 'Latin gladius „sword“ from Celtic' beside Welsh cleddyf, Breton kleze, Middle Irish claideb (< Celtic *kladios); Walde-Pokorny I 'lat. gladius aus dem Kelt., Vendryes Mél. Saussure 310 f.'; Watkins 'Variant Celtic zero-grade extended form *klad- ... suffixed form *klad-yo-, Celtic source of Latin gladius'; Ernout-Meillet 'ensis a été supplanté par gladius, qui doit être celtique'; de Vaan (quoted by Etymonline) 'The close connection with Celtic words for „sword“, together with the imperfect match of initial consonants ... suggests that Latin borrowed a form *gladio- or *kladio- ... from [Proto-Celtic] or from a third language.' The chain is therefore PIE *kelh₂- > zero-grade extension *kl̥h₂-d- > Proto-Celtic *kladiwos 'sword' (a d-extension, 'the thing that hews', cf. Old Irish claidid 'digs', Welsh claddu 'to dig') > Gaulish *kladyos, borrowed into Latin in the Republican period with an unexplained voicing of k- to g-. Nourai's arrow, drawn straight from the root to Latin, is right in substance but hides the Celtic stage and the anomaly of the initial consonant; hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"واژهٔ لاتینی gladius «شمشیر» (شمشیر کوتاه لژیونر رومی) واقعی است و معنایش درست، و به‌راستی به همین ریشه بستگی دارد — اما نه با وراثت مستقیم. همهٔ مراجع آن را وام‌واژه‌ای از سلتی می‌دانند: پوکورنی (ص ۵۴۶) «gladius لاتین از سلتی» در کنار cleddyf ولزی، kleze برِتونی و claideb ایرلندی میانه؛ والده-پوکورنی «lat. gladius aus dem Kelt.»؛ واتکینز «صورت سلتیِ *klad-yo-، سرچشمهٔ gladius لاتین»؛ ارنو-مِیه «gladius که باید سلتی باشد»؛ و دِ فان (به نقل اتیمانلاین) که ناهمخوانی همخوان آغازین را برجسته می‌کند و می‌گوید لاتین صورتی *gladio- یا *kladio- را از سلتی آغازین یا از زبانی سوم وام گرفته است. پس زنجیره چنین است: هندواروپایی *kelh₂- ← صورت صفرِ گسترش‌یافتهٔ *kl̥h₂-d- ← سلتی آغازین *kladiwos «شمشیر» (سنجید با claidid ایرلندی کهن «می‌کَنَد» و claddu ولزی «کندن») ← گالی *kladyos ← وام‌گیری در لاتینِ دورهٔ جمهوری، با واک‌دار شدنِ توضیح‌ناپذیرِ k به g. پیکان نورایی که یک‌راست از ریشه به لاتین کشیده شده در اصلِ مطلب درست است ولی مرحلهٔ سلتی و آن بی‌قاعدگی آوایی را پنهان می‌کند؛ از این رو با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gladius#Latin\",\n            \"https://www.etymonline.com/word/gladiator\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1521\", \"status\": \"supports\", \"note\": \"The New College appendix page cannot be opened online, but the same Watkins text is on disk (AHD_watkins1985.txt, kel-1): '3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad-ibo- in Gaelic claidheamh, sword: CLAYMORE.' — AHD does place gladius under this root, though via Celtic, which the chart omits.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ensis (LAT.txt lines 18825-18836)\", \"stance\": \"supports\", \"note\": \"'ensis a été supplanté par gladius, qui doit être celtique, et celui-ci a subi dans les l. romanes la concurrence de spatha qui est grec.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 436 ff.\", \"stance\": \"supports\", \"note\": \"'cymr. cleddyf „Schwert, Klinge“ (cleddyf diss. aus *cledyd, kelt. *kladios; ir. claideb ist Lw. aus dem Cymr.), lat. gladius aus dem Kelt., Vendryes Mél. Saussure 310 f.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 20.27 'Sword'\", \"stance\": \"supports\", \"note\": \"'Lat. gladius (> OIt. ghiado; Fr. glaive) ... Ir. claideb ... W. cleddyf ... beside Lat. gladius (fr. Celtic)'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Gladiator/glaive\", \"stance\": \"partial\", \"note\": \"'Gladiator, a swordsman. (L.) L. gladiator. — L. gladius, a sword.' and 'glaive, a sword. (F.-L.) O.F. glaive — L. gladium, acc. of gladius, a sword.' Skeat stops at Latin and says nothing of Celtic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"gladiator\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English gladiator is a straightforward Latinism: Latin gladiātor 'fighter in the public games, swordsman' (fem. gladiātrīx), an agent noun in -tor built directly on gladius (there is no verb *gladiāre), taken into English in the mid-15th century in the sense 'Roman swordsman' and only later extended figuratively. Skeat: 'Gladiator, a swordsman. (L.) L. gladiator. — L. gladius, a sword.' The doublet glaive came the vernacular way, through Old French glaive from the accusative gladium. The arrow Latin gladius → English gladiator is uncontroversial.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی gladiator وام‌واژه‌ای مستقیم از لاتین است: gladiātor «مبارز بازی‌های همگانی، شمشیرزن» (مؤنث gladiātrīx)، اسم فاعلِ ‑tor که یک‌راست بر gladius ساخته شده (فعل *gladiāre وجود ندارد)، و در میانهٔ سدهٔ پانزدهم میلادی به معنی «شمشیرزن رومی» وارد انگلیسی شده و بعدها معنی مجازی یافته است. اسکیت: «Gladiator، شمشیرزن. (لاتین) از gladiator لاتین، از gladius «شمشیر»». دوگانهٔ مردمیِ همین واژه glaive است که از راه فرانسهٔ کهن و از حالت مفعولی gladium آمده. این پیکان بی‌مناقشه است و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gladiator\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt, kel-1: '... Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE'. GLADIATOR is listed among the English descendants exactly as the chart has it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Gladiator (SKT.txt line 7624)\", \"stance\": \"supports\", \"note\": \"'Gladiator, a swordsman. (L.) L. gladiator. — L. gladius, a sword.'; and line 7626 'glaive, a sword. (F.-L.) O.F. glaive — L. gladium, acc. of gladius, a sword.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. gladiator\", \"stance\": \"supports\", \"note\": \"'gladiator, n., a Roman swordsman who fought in the arena for the entertainment of spectators' (entry present, derived from Latin gladius in the following lines).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"gladiyator\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The French word is gladiateur, m. (plural gladiateurs), borrowed from the Latin accusative gladiātōrem; there is no French form 'gladiyator'. I checked the printed page (book p.222 = pdf 252, image copied to data/verification/sources/refs/ocr/BOOK/252.png): the box really reads 'French | gladiyator', so the JSON is faithful and the form is Nourai's own. What has happened is transparent: he has written the French intermediary back out of the Persian گلادیاتور instead of giving the actual French spelling — the Persian y-glide of gelādiyātor has been carried into the 'French' line. The link itself (Latin gladiātōrem > French gladiateur, and thence into Persian) is correct; only the shape of the word is wrong.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی gladiateur (جمع gladiateurs) است که از حالت مفعولی لاتین gladiātōrem وام گرفته شده؛ صورتی به شکل «gladiyator» در فرانسه وجود ندارد. صفحهٔ چاپی را دیدم (کتاب ص ۲۲۲، برگ ۲۵۲ پی‌دی‌اف؛ تصویر در data/verification/sources/refs/ocr/BOOK/252.png): در خانهٔ نمودار به‌روشنی «gladiyator» چاپ شده است؛ پس خطای خوانش اسکن نیست، خطای چاپیِ خود کتاب است. آنچه رخ داده روشن است: نورایی صورت فرانسوی را از روی «گلادیاتور» فارسی بازنویسی کرده و همان یایِ میانجیِ فارسی را به سطر فرانسه برده است. خودِ پیوند (لاتین gladiātōrem ← فرانسوی gladiateur ← فارسی) درست است و تنها شکل واژه نادرست.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"gladiyator\",\n          \"correct_form\": \"gladiateur\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gladiateur\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:307\", \"status\": \"not_checked\", \"note\": \"Mahshid Moshiri, Farhang-e vāžehā-ye orupāyi dar fārsi (Alborz 1371/1992) has no copy online — refs_online.json records kind 'none' and a 2026 re-search that found nothing (only decoys such as Zomorrodian's similarly-titled book). The claim itself (French → Persian) is independently confirmed by Moʿin's [فر.] tag on گلادیاتور.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"grep of PHN.txt (Pihan, mots français dérivés de l'arabe, du persan ou du turc)\", \"stance\": \"silent\", \"note\": \"Pihan covers French words taken FROM the East, not French words exported to Persian, and has nothing on gladiateur.\"},\n            {\"src\": \"DEV\", \"where\": \"grep of DEV.txt (Devic, mots français d'origine orientale)\", \"stance\": \"silent\", \"note\": \"Same direction of borrowing; no entry.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. gladiator\", \"stance\": \"supports\", \"note\": \"Klein gives the Latin agent noun gladiātor as the source of the modern European forms, which is the etymon French gladiateur continues.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"gelâdîyâtor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian گلادیاتور gelādiyātor is a modern learned loan from French gladiateur, exactly as drawn. Moʿin's dictionary tags the headword '[فر.]' = 'from French' and glosses it 'در روم قدیم به بردگان و غلامانی می‌گفتند که می‌بایست در میدان‌های عمومی با یکدیگر یا با حیوانات درنده تا دم مرگ بجنگند'; Dehkhoda likewise files it as '(فرانسوی، اِ)'. Phonetically the borrowing follows the normal 20th-century route for French words in Persian: French [ɡla-] is broken by an epenthetic vowel into ge-lā- because Persian tolerates no initial cluster; French -ia- [ja] is written ‑یا‑ with the glide; and the French agent suffix -teur [tœʁ] is regularly rendered ‑تور -tor, as in دیکتاتور diktātor, امپراتور emperātor, رادیاتور rādiyātor. The word entered Persian with the European classical education and journalism of the late Qajar/early Pahlavi period.\",\n          \"derivation_fa\": \"«گلادیاتور» وام‌واژه‌ای نوآیین از فرانسوی gladiateur است، درست همان‌گونه که در نمودار آمده. معین سرواژه را با نشانهٔ «[فر.]» یعنی «از فرانسه» آورده و چنین معنی کرده: «در روم قدیم به بردگان و غلامانی می‌گفتند که می‌بایست در میدان‌های عمومی با یکدیگر یا با حیوانات درنده تا دم مرگ بجنگند»؛ دهخدا نیز آن را «(فرانسوی، اِ)» نشان کرده است. از دید آوایی، وام‌گیری از قاعدهٔ آشنای واژه‌های فرانسوی در فارسی پیروی می‌کند: خوشهٔ آغازینِ [ɡla] در فارسی شکسته و با واکهٔ میانجی به ge-lā- بدل می‌شود، زیرا فارسی خوشهٔ همخوانی آغازین نمی‌پذیرد؛ ‑ia‑ فرانسوی با یای میانجی «‑یا‑» نوشته می‌شود؛ و پسوند فاعلیِ ‑teur به‌قاعده «‑تور» می‌شود، چنان‌که در دیکتاتور، امپراتور و رادیاتور. واژه در دورهٔ اواخر قاجار و آغاز پهلوی همراه با آموزش کلاسیک اروپایی و مطبوعات وارد فارسی شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/گلادیاتور/\",\n            \"https://en.wiktionary.org/wiki/gladiateur\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:307\", \"status\": \"not_checked\", \"note\": \"Moshiri's Farhang-e vāžehā-ye orupāyi dar fārsi is not available in any digital form (refs_online.json: kind 'none', re-searched 2026-09). Its claim is however independently corroborated by Moʿin and Dehkhoda, both of whom label گلادیاتور a French loan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Farsi s.v. گلادیاتور (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'(گِ تُ ) [ فر. ] (اِ. ) در روم قدیم به بردگان و غلامانی می گفتند که می بایست در میدان های عمومی با یکدیگر یا با حیوانات درنده تا دم مرگ بجنگند.' — the tag [فر.] is Moʿin's abbreviation for فرانسه.\"},\n            {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for گلادیاتور\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian does not treat modern European loanwords, and has no entry.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"clamitas\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no Latin word *clamitas. The word meant is calamitās, gen. calamitātis, f. 'damage, loss, injury; misfortune, disaster; military defeat; blight' — this is the form in AHD:1521, the very reference cited: Watkins, kel-1, 'suffixed form *klə-mo- in Latin calamitās, injury, damage, loss: CALAMITY', and it is glossed there word for word as Nourai's 'injury'. I looked at the printed page (book p.222 = pdf 252; copy at data/verification/sources/refs/ocr/BOOK/252.png) and the box does read 'clamitas : injury', so the extraction is faithful and the fault is the book's: a dropped syllable, very likely helped by the other Latin member of this root, clādēs 'injury, damage, defeat', which Pokorny prints two lines away ('Latin clades „injury; damage, mischief, beating“', IEW 546). On the substance the arrow is sound and in fact better supported now than in 1959: Schrijver and de Vaan derive calamitās from an unattested adjective *calamis/*calamus < *kelh₂-mo- or *kl̥h₂-em-, the same adjective that underlies incolumis; Ernout-Meillet already said 'calamitas doit être dérivé d'un adjectif ... il est à rapprocher de incolumis ... et par là à clādēs' and dismissed the ancient rustic association with calamus 'stalk' as a folk etymology; Klein: 'calamitas ... with the primary meaning „blow“, rel. to in-columis, fr. I.-E. base *qel(ə)-, *qol(ə)-, „to strike, beat“'.\",\n          \"derivation_fa\": \"واژه‌ای به صورت *clamitas در لاتین وجود ندارد. واژهٔ مقصود calamitās (اضافی calamitātis، مؤنث) است به معنی «زیان، آسیب، خسارت؛ بدبختی، بلا؛ شکست نظامی؛ آفت زراعی». همین صورت در مرجعی که خود نورایی آورده (AHD:1521) هست: واتکینز ذیل kel-1، «صورتِ پسونددارِ *klə-mo- در calamitās لاتین، injury, damage, loss: CALAMITY» — و معنی «injury» را نورایی از همان‌جا برداشته است. صفحهٔ چاپی را دیدم (کتاب ص ۲۲۲؛ تصویر در data/verification/sources/refs/ocr/BOOK/252.png) و در خانه به‌روشنی «clamitas : injury» چاپ شده؛ پس خطای خوانش اسکن نیست، خطای چاپی کتاب است: افتادن یک هجا، احتمالاً به سبب آمیختن با عضو دیگر همین ریشه در لاتین، یعنی clādēs «آسیب، زیان، شکست» که پوکورنی دو سطر پایین‌تر (ص ۵۴۶) آورده است. از نظر محتوا پیکان درست و امروزه حتی مستندتر از ۱۹۵۹ است: شرایور و دِ فان calamitās را از صفتی ناموجود *calamis/*calamus از *kelh₂-mo- می‌گیرند، همان صفتی که زیربنای incolumis است؛ ارنو-مِیه هم پیش‌تر گفته بود که calamitas باید از صفتی مشتق باشد و با incolumis و از آن راه با clādēs پیوند دارد و ارتباط عامیانه‌اش با calamus «ساقه» ریشه‌شناسی عامیانه است؛ کلاین: «calamitas ... با معنی نخستینِ „ضربه“، خویشاوند in-columis، از ریشهٔ هندواروپایی *qel(ə)- „زدن، کوبیدن“».\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"clamitas\",\n          \"correct_form\": \"calamitās\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/calamitas#Latin\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1521\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt, kel-1, III.1.d: 'suffixed form *klə-mo- in Latin calamitās, injury, damage, loss: CALAMITY.' The reference supports the derivation and simultaneously shows that the printed 'clamitas' is a misprint for calamitās; the gloss 'injury' is AHD's first word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. calamitas (LAT.txt lines 8600-8625)\", \"stance\": \"supports\", \"note\": \"'Calamitas doit être dérivé d'un adjectif, ce qui est la formation normale des abstraits en -tās ... il est à rapprocher de incolumis ... et par là à clādēs'; and, on the rustic sense, 'ce second sens ... résulte sans doute d'une spécialisation secondaire, due à un rapprochement fait par la langue rustique entre calamus et calamitas'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. calamity (p.~230)\", \"stance\": \"supports\", \"note\": \"'calamity, n., misery; disaster. — F. calamité, fr. L. calamitatem, acc. of calamitas, „damage, injury, loss, misfortune“, with the primary meaning „blow“, rel. to in-columis, „unimpaired, uninjured“, fr. I.-E. base *qel(ə)-, *qol(ə)-, „to strike, beat“, whence also Gk. κλᾶν, „to break“, κλῆρος ...'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 436 ff.\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny's article gives clādēs ('Latin clades „Verletzung; Schaden, Unheil, Niederlage“') and the klad- extension but does not itself list calamitās, which is why the misprint is so easy to make.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"calamity\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English calamity (late 15th c.) comes through Middle French calamité (14th c.) from Latin calamitātem, the accusative of calamitās; the -ity of the English word is the regular reflex of Latin -itātem through French -ité. Klein s.v. calamity: 'F. calamité, fr. L. calamitatem, acc. of calamitas'. The AHD index likewise files 'CALAMITY kel-1', so the arrow from the Latin node, and through it to the root, is exactly what Nourai's own reference says.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی calamity (اواخر سدهٔ پانزدهم میلادی) از راه فرانسهٔ میانه calamité (سدهٔ چهاردهم) از calamitātem لاتین، حالت مفعولیِ calamitās، آمده است؛ پایانهٔ ‑ity انگلیسی بازتاب قاعده‌مندِ ‑itātem لاتین از مجرای ‑ité فرانسوی است. کلاین ذیل calamity: «از فرانسوی calamité، از calamitatem لاتین، حالت مفعولی calamitas». نمایهٔ AHD نیز «CALAMITY kel-1» را ثبت کرده است؛ پس پیکانِ نمودار از گرهٔ لاتین و از آن‌جا به ریشه، همان است که مرجع خود نورایی می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/calamitas#Latin\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index: 'CALAMITY kel-1' (line 1329), and the kel-1 article ends its Latin section with 'in Latin calamitās, injury, damage, loss: CALAMITY'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. calamity (p.~230)\", \"stance\": \"supports\", \"note\": \"'calamity, n., misery; disaster. — F. calamité, fr. L. calamitatem, acc. of calamitas ... fr. I.-E. base *qel(ə)-, *qol(ə)-, „to strike, beat“.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"partial\", \"note\": \"Skeat's word-list uses 'calamity' only as a gloss (s.v. distress, 'distress, calamity. (F.-L.)'); the concise edition on disk has no headword entry of its own for calamity.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. calamitas\", \"stance\": \"supports\", \"note\": \"Records calamitās as 'ancien, usuel et classique ... Non roman', i.e. the Romance and English forms are learned borrowings, not inherited — which fits the 14th-c. French date.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"klon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek κλών, gen. κλωνός, m. 'twig, spray, slip' is real and correctly glossed. Watkins, at the page Nourai cites, derives it from the extended form *kelə- of this root: 'Zero-grade form *klā- in Greek klā- ... (ii) Greek klōn (< *klā-ōn), twig: CLONE' — a lengthened-grade -ōn formation beside κλάω 'to break off', κλάδος 'branch, shoot' and κλάσμα, i.e. a twig is 'what is broken off', which is why it sits under a root meaning 'strike, cut'. Pokorny has the same family (κλάδος, κλαδαρός, κλαδάσσαι) at IEW 545-546. The reservation is semantic and comes from Beekes, reported by Wiktionary: κλών is 'of uncertain origin. Probably related to κλάδος, κλαστός and κλάω ... though Beekes considers this semantically tenuous, as plant twigs and sprouts are not generally considered „broken“'. He offers no alternative, so the traditional connection stands as the best available but not as a certainty.\",\n          \"derivation_fa\": \"واژهٔ یونانی باستان κλών (اضافی κλωνός) «شاخهٔ نازک، ترکه، قلمه» واقعی است و معنایش درست آمده. واتکینز در همان صفحه‌ای که نورایی ارجاع داده آن را از گسترش *kelə- همین ریشه می‌گیرد: «صورت صفرِ *klā- ... یونانی klōn (< *klā-ōn) „ترکه“: CLONE» — ساختی با پایانهٔ ‑ōn در کنار κλάω «شکستن، جدا کردن» و κλάδος «شاخه» و κλάσμα؛ یعنی «ترکه» همان «چیزِ شکسته‌شده» است و از این رو زیر ریشه‌ای به معنی «زدن، بریدن» می‌نشیند. پوکورنی نیز همین خانواده را در ص ۵۴۵-۵۴۶ آورده است. تنها تردید، تردیدی معنایی است که از بیکس می‌آید (به نقل ویکی‌واژه): κλών «خاستگاهی نامعلوم دارد؛ احتمالاً با κλάδος و κλαστός و κλάω خویشاوند است، هرچند بیکس این پیوند را از نظر معنایی سست می‌داند، چون ترکه و جوانهٔ گیاه معمولاً „شکسته“ انگاشته نمی‌شوند». چون او جانشینی پیشنهاد نمی‌کند، همین ریشه‌شناسی سنتی بهترین گزینهٔ موجود است؛ پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/κλών\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1521\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt, kel-1, III.1.a.(ii): 'Greek klōn (< *klā-ōn), twig: CLONE' — the form, the gloss 'twig' and the English descendant are all Nourai's, taken from this article.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 436 ff. (klād- extension)\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny and Pokorny carry the κλάδος/κλαδαρός/κλάω family under this root ('Gr. κλαδαρός (*kladeros) „frail, breakable“ ... κλάδος m. „twig, branch“ ... κλαστάζω „dress vines, cut grapevine“'), but the specific noun κλών is not itemised there.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, entries for 'clone'\", \"stance\": \"silent\", \"note\": \"Klein's two 'clone' entries are both about cyclone ('Coined by the English scientist Sir Francis Galton fr. anti- and cyclone'; 'Irregularly formed fr. Gk. κύκλος'); the biological clone < κλών is absent from the 1966 and 1971 editions.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"clone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English clone is a scientific coinage of 1903, made in botany (originally spelled clon, by H. J. Webber) directly on Ancient Greek κλών 'twig, slip', because the plants of a clone are propagated from cuttings — twigs — of one parent and are therefore genetically identical; the spelling clone settled in within a few years, the biological sense was extended to cells and organisms, and the figurative sense ('exact copy of a person or thing') dates from the 1970s. Wiktionary: 'Coined (in botany) in 1903, based on Ancient Greek κλών (klṓn, „twig“). Figurative use from the 1970s.' AHD's index files 'CLONE kel-1', which is the arrow Nourai draws. Note that Klein (1966, 1971) does not yet have the word in this sense, so the chart is relying on AHD alone among its own sources — correctly.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی clone برساخته‌ای علمی از سال ۱۹۰۳ است که نخست در گیاه‌شناسی (به صورت clon، به دست هـ. ج. وبر) یک‌راست بر پایهٔ κλών یونانی باستان «ترکه، قلمه» ساخته شد، زیرا گیاهان یک «کلون» را از قلمه‌های یک بوته می‌رویانند و از این رو از نظر ژنتیکی یکسان‌اند؛ املای clone در همان سال‌ها جا افتاد، معنی زیستی به یاخته و جانور گسترش یافت و کاربرد مجازی («رونوشت بی‌کم‌وکاست کسی یا چیزی») از دههٔ ۱۹۷۰ رواج گرفت. ویکی‌واژه: «برساخته (در گیاه‌شناسی) در ۱۹۰۳ بر پایهٔ κλών یونانی باستان „ترکه“؛ کاربرد مجازی از دههٔ ۱۹۷۰». نمایهٔ AHD نیز «CLONE kel-1» را ثبت کرده و همین پیکان نمودار است. شایان یادآوری است که کلاین (چاپ ۱۹۶۶ و ۱۹۷۱) هنوز این واژه را در این معنی ندارد، پس نمودار در این گره تنها بر AHD تکیه دارد — و به‌درستی. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/clone\",\n            \"https://en.wiktionary.org/wiki/κλών\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt, kel-1: 'Greek klōn (< *klā-ōn), twig: CLONE' — CLONE is listed as the English descendant of κλών under this root, which is what the chart's unpaged 'AHD' reference points to.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 / 1971, s.v. clone\", \"stance\": \"silent\", \"note\": \"Both editions have only the cyclone-related entries ('clone, n. — Coined by the English scientist Sir Francis Galton (1822-1911) fr. anti- and cyclone'); the botanical/biological clone is not in Klein.\"},\n            {\"src\": \"FSD\", \"where\": \"grep of the Funk & Wagnalls volumes\", \"stance\": \"silent\", \"note\": \"The 1913/1940 New Standard Dictionary predates the general currency of the word; no usable entry for clone in the biological sense.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T16:27:27.865Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-252.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:27:32.029Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-252.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 252"
}
```


### [2026-09-06T16:27:36.594Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 7, 'plausible': 6, 'transcription_suspect': 3, 'disputed': 3}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 13, 'partial': 5, 'contradicts': 2, 'not_checked': 2}
books consulted: {'supports': 26, 'silent': 15, 'partial': 12, 'contradicts': 4} | by book: {'KLN': 13, 'WLD': 8, 'LAT': 7, 'HUB': 3, 'HRN': 3, 'ARY': 3, 'SKT': 3, 'BQT': 2, 'MON': 2, 'FVQ': 2, 'AFA': 2, 'SYN': 2, 'WEB': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'PHN': 1, 'DEV': 1, 'FSD': 1}
```


## [2026-09-06T16:27:54.517Z] AGENT

Page 252 (book p.222) verified — 3 charts, 19 nodes, 0 PROBLEM lines.

**Verdicts:** roots 2 confirmed / 1 plausible; nodes 7 confirmed, 6 plausible, 3 transcription_suspect, 3 disputed. Ref checks: 13 supports, 5 partial, 2 contradicts, 2 not_checked.

**Disputed (all in Kel 5 "cup, bowl"):**
- Syriac node (#2) — Nourai's Greek κύλιξ → Syriac arrow has no support; Syriac ܟܣܐ kāsā is Semitic (Akkadian kāsu, Hebrew kōs, Ugaritic ks; Jeffery FVQ 245 "little doubt of its Aram. origin").
- Persian kâseh/kŭzeh (#3) — kāse from Syriac is defensible (Jeffery, Addi Shir, and Moʿin actually tags it [ازع.] "from Arabic"), but the Iranian view is MP *kāsag < OP kāsaka-; kuze runs the *other* way: Hübschmann Pers. Stud. no.872 p.89 derives NP kūza from OP *kūza and makes Armenian kuz and Arabic kūz loans **from** Persian.
- Arabic ka's (#4) — Nourai's own reference (Jeffery = VDQ) says the opposite: Arabic kaʾs and Persian kāsa are parallel borrowings from Aramaic; Fraenkel agrees; Addi Shir himself writes "فتكون الفارسية قد أخذت من اللغات السامية".

**transcription_suspect — all three are the BOOK's own misprints, extraction is faithful** (verified against the printed page; image copied to `data/verification/sources/refs/ocr/BOOK/252.png`):
- Kel 5 #1 Greek "kalix" → should be κύλιξ *kúlix* (conflation with κάλυξ / Latin calix).
- Kel 6 #4 French "gladiyator" → should be *gladiateur* (Nourai back-wrote it from Persian گلادیاتور).
- Kel 6 #6 Latin "clamitas" → should be *calamitās* (as in his own AHD:1521; probably contaminated by clādēs).

**No extraction errors** — the JSON matches the printed page everywhere, including the Persian script and both poetry quotes.

**Other notes for the owner:** POK:546 on the Kel 4 root box is one page early (Pokorny's kel-4 runs 547-548; the node refs POK:547 are right). KLN:316 and IEC:464 are exact hits — Mann col. 464 literally reads "kal- (6) 'strike' … Per. cf. kaland 'spade'". Kel 5 as a PIE root is doubted by Beekes/de Vaan (Pre-Greek/substrate), hence the plausible root verdict; the Watkins appendix does not recognise it at all (it files CALIX under kal-1). VOP:307 (Moshiri) remains unobtainable — marked not_checked, but Moʿin's [فر.] tag independently confirms the French→Persian gladiator link.
