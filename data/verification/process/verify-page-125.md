# Verification process log — verify-page-125


## [2026-09-05T18:22:37.572Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 125 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-125.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-125.json. Write /home/sfmqrb/git/rishe/data/verification/page-125.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 125` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:22:39.263Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:22:39.967Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:22:39.985Z] TOOL RESULT

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


## [2026-09-05T18:22:40.108Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-125.txt"
}
```


### [2026-09-05T18:22:40.129Z] TOOL RESULT

```
1	=== PDF page 125 (book page 95) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dhě 2 : to do, set  (refs AHD:1512; POK:235)  PART 2
4	#1 (parent #0) [Greek] refs=AHD | tithenai : to put ; apo-tithenai : to put away, store ; para-en-tithenai : to put in besides ☞En ; thěma : thing placed
5	  #2 (parent #1) [French] refs=AHD:156,1334 | botica : gift store ; paranthese, these, theme
6	    #3 (parent #2) [Persian] refs=MON:625,1076,1137 | bŭtîk «بوتیک» : gift store ; parântez «پرانتز» : parenthesis ; tem, tez «تیم ، تز» : subject
7	    #4 (parent #2) [English] refs=AHD:156,1334 | boutique, theme, thesis, parenthesis
8	#5 (parent #0) [Germanic] refs=AHD | dôn : to do
9	  #6 (parent #5) [English] refs=AHD | do, deed
10	#7 (parent #0) [Latin] refs=AHD | facere : to do, make ; faciěs : shape, face ; opi-facium : work to do, office ☞Op ; facilis : that which can be done
11	  #8 (parent #7) [English] refs=None | -fy, fortify, modify ; fact, benefit, defeat, perfect, profit, factor, factory, affect, effect, face, surface ; office ; facility, difficult, faculty
12	#9 (parent #0) [Indo-European] refs=KLN:573 | Dhě-mo, Dh-mo : house (something built or done)
13	  #10 (parent #9) [Latin] refs=KLN:573 | famul, famulus, familia : belonging to the house
14	    #11 (parent #10) [English] refs=KLN:573 | family, familiar
15	    #12 (parent #10) [Sanskrit] refs=KLN:573 | dhâman : seat, house
16	--- entry 1 ---
17	ROOT Dhědh -> redirect to Âtos
18	--- entry 2 ---
19	ROOT [Indo-European] Dhedh 2 : nurse  (refs IEC:178)
20	#1 (parent #0) [Persian] refs=MON:1499 | dadeh «دَده ۲» : maid servant, nurse
21	#2 (parent #0) [Greek] refs=IEC:178 | těthě 2 : nurse
22	--- entry 3 ---
23	ROOT Dhegh -> redirect to Dhogh
24	--- entry 4 ---
25	ROOT Dhehem -> redirect to Ghdhem
26	
```


## [2026-09-05T18:22:43.931Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-125.json",
 "description": "Read page 125 source JSON"
}
```


### [2026-09-05T18:22:43.972Z] TOOL RESULT

```
{
  "pdf_page": 125,
  "book_page": 95,
  "entries": [
    {
      "root": {
        "name": "Dhě 2",
        "lang": "Indo-European",
        "refs": "AHD:1512; POK:235",
        "gloss": "to do, set"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "tithenai", "gloss": "to put", "script": null},
            {"translit": "apo-tithenai", "gloss": "to put away, store", "script": null},
            {"translit": "para-en-tithenai", "gloss": "to put in besides", "script": null, "see": ["En"]},
            {"translit": "thěma", "gloss": "thing placed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": "AHD:156,1334",
          "words": [
            {"translit": "botica", "gloss": "gift store", "script": null},
            {"translit": "paranthese, these, theme", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:625,1076,1137",
          "words": [
            {"translit": "bŭtîk", "gloss": "gift store", "script": "بوتیک"},
            {"translit": "parântez", "gloss": "parenthesis", "script": "پرانتز"},
            {"translit": "tem, tez", "gloss": "subject", "script": "تیم ، تز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:156,1334",
          "words": [
            {"translit": "boutique, theme, thesis, parenthesis", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "dôn", "gloss": "to do", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "do, deed", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "facere", "gloss": "to do, make", "script": null},
            {"translit": "faciěs", "gloss": "shape, face", "script": null},
            {"translit": "opi-facium", "gloss": "work to do, office", "script": null, "see": ["Op"]},
            {"translit": "facilis", "gloss": "that which can be done", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "-fy, fortify, modify", "gloss": null, "script": null},
            {"translit": "fact, benefit, defeat, perfect, profit, factor, factory, affect, effect, face, surface", "gloss": null, "script": null},
            {"translit": "office", "gloss": null, "script": null},
            {"translit": "facility, difficult, faculty", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KLN:573",
          "words": [
            {"translit": "Dhě-mo, Dh-mo", "gloss": "house (something built or done)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Latin",
          "refs": "KLN:573",
          "words": [
            {"translit": "famul, famulus, familia", "gloss": "belonging to the house", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "KLN:573",
          "words": [
            {"translit": "family, familiar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "Sanskrit",
          "refs": "KLN:573",
          "words": [
            {"translit": "dhâman", "gloss": "seat, house", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhědh",
        "redirect": "Âtos"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhedh 2",
        "lang": "Indo-European",
        "refs": "IEC:178",
        "gloss": "nurse"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1499",
          "words": [
            {"translit": "dadeh", "gloss": "maid servant, nurse", "script": "دَده ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:178",
          "words": [
            {"translit": "těthě 2", "gloss": "nurse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhegh",
        "redirect": "Dhogh"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhehem",
        "redirect": "Ghdhem"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T18:22:44.523Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:22:44.571Z] TOOL RESULT

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


## [2026-09-05T18:23:02.772Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls tools/",
 "description": "List verification dir and tools"
}
```


### [2026-09-05T18:23:02.822Z] TOOL RESULT

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
page-118.json
page-119.json
page-120.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
----
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-05T18:23:05.479Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 125 -l 125 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg125 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 125 to PNG"
}
```


### [2026-09-05T18:23:08.141Z] TOOL RESULT

```
total 35960
drwx------ 3 sfmqrb sfmqrb     4096 Sep  5 14:23 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58735 Sep  5 14:20 mk120.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  5 14:22 p117
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
-rw-rw-r-- 1 sfmqrb sfmqrb   330167 Sep  5 14:18 pg121_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82335 Sep  5 14:17 pg121.png
-rw-rw-r-- 1 sfmqrb sfmqrb   461010 Sep  5 14:18 pg121_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61026 Sep  5 14:18 pg123.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75202 Sep  5 14:23 pg125.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T18:23:12.195Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg125.png"
}
```


### [2026-09-05T18:23:12.885Z] TOOL RESULT

```

```


## [2026-09-05T18:23:12.882Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T18:23:24.607Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg125.png')\nprint(im.size)\nim.crop((1450,470,2000,700)).resize((1650,690)).save('p125_persian.png')\nim.crop((550,1250,1450,1650)).resize((1800,800)).save('p125_dhemo.png')\n\"",
 "description": "Crop Persian and Dhe-mo regions"
}
```


### [2026-09-05T18:23:26.773Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-05T18:23:29.399Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_persian.png"
}
```


### [2026-09-05T18:23:29.425Z] TOOL RESULT

```

```


## [2026-09-05T18:23:39.795Z] TOOL CALL #10: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_dhemo.png"
}
```


### [2026-09-05T18:23:39.823Z] TOOL RESULT

```

```


## [2026-09-05T18:23:52.952Z] TOOL CALL #11: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','POK','KLN','IEC','MON','LEW','LAT','SKT','WLD','SYN','FSD','WEB','ARY','BQT']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T18:23:54.997Z] TOOL RESULT

```
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
```


## [2026-09-05T18:24:00.031Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==244' POK_01.txt | head -80",
 "description": "Print Pokorny leaf 244"
}
```


## [2026-09-05T18:24:00.909Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhē-\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD for dhe root"
}
```


### [2026-09-05T18:24:03.072Z] TOOL RESULT

```
nen,  -ön  ,zweifach  zusammendrehen',  mhd.  ziüirn^  mnd.  tioern ,doppelt  zusammengedrehter  Faden'  wohl  =  ags.  twlrij  holl.  twijn  , Zwirn, Leinen'  (ags.  getwinne  ,bini',  getwinnas  , Zwillinge'  ist  dann  auf  *twi-nja- zurückzuführen).  Daneben  auf  Grund  eines  *ticllia-j  idg.  '^dtiei-ko-,  got. ticeihnai  ,zwei',  ags.  Dat.  tweonum^  betweonum^  engl,  betiveen  ,z wischen';
lit.  m.  PL  dvynat,  russ.  dvöjni  ,Zwillinge'.  /
Mit  -ko-:  /
ai.  dvikd-  ,aus  zweien  bestehend,  zweifach'  (dvakd-  ,paarweise  verbunden nach  ekakd-)',
ahd.  zioe(h)o,  as.  twe{}i)Oj  ags.  tweo  m.  ,Zweifel',  ags.  be-tioih,  -tioeoli ,zwischen',  mid  unc  twlh  ,zwischen  uns  beiden'  (vgl.  oben  got.  tweih-nai)]
von  duis-  aus:  ahd.  zwisk,  as.  twisk  ,zweifach',  PL  , beide'  Dat.  PL  ahd. {undar,  en)  zioisken,  nhd.  zwischen]  dazu  ags.  getwisa  m.,  as.  gitioiso,  mhd. zwiselinc  ,Zwilling'.
232
Mit  duis-  ^zweimal^  identisch  ist  diiis-  ^entzwei,  auseinander^  in  got.  tx standan  ^sich  trennen^  und  den  Ableitungen  anord.  tvistra  ^trennen^_,  m£J afries.  ticlst,  mhd.  zwist  , Zwist  (Entzweiung)^  und  mengl.  ticist  =  anoi kvistr  ^Zweig'^  (wie  auch  bair.  zioist),  ferner  anord.  kvisl  f.  , gespaltener  Zwei oder  Werkzeug,  Arm  eines  Flusses^  (dies  mit  idg.  ei)\  ferner  anord.  ^viVüc ^zweimaF,  tvistr  ^zwiespältig,  traurig^  (=  ai.  dvistJia-  ,zweideutig^ *diaTOQ  in  dLaxaC^co  ,zweifle^,  idg.  *dui{s)-sto- -.Wz.  stä-,  allenfalls  duis^i mit  formantischem  -to-),  ags.  twisla  ,Arm  eines  Flusses^,  twislian  ^zwe teilen^,  ahd.  zwisila,  nhd.  Ziviesel  ^gabelförmiger  Gegenstand,  Zweigt,  mli^ zwisel  ,doppelt^j  hierher  sehr  wahrscheinlich  ar.  dvls-  ,hassen^  (s.  untel *duei-  ,fürchten^).
6.  Idg.  Nebenform  dis-  in  lat.  dis-j  as.  afries.  te-,  ti-,  ags.  te-j  ahd.  zi-^  zt (jünger  zir-  durch  Verquickung  von  zi-  und  ir-)  ,zer-^,  got.  dis-  ,auseinau^ der^  (wohl  aus  dem  Lat.  entlehnt,  kaum  vortonig  aus  *tis-  =  lat.  du^ alb.  tsh-  z.  B.  in  tshk'ep  ,auf trennen^,  gr.  dia  (d.  i.  nach  ^asra  usw.  auS gefülltes  *Jt[(7]a),  z.  B.  dia-axilI,o)  :  lat.  discindo,  ,durch^  (,*mitten  entzwei*) als  Präf.  auch  ,durch  und  durch*  =  ,sehr^  (äol.  ^a-).
WP.  I  817 ff.,  WH.  I  104ff.,  354f.,  381  ff.,  860,  861,  Feist  484ff.,  Traut- mann  64,  Schwyzer  Gr.  Gr.  I  588  f.,  Wackernagel-Debrunner  Ai.  Gr.  III, 342  f.
Dh.
j.  dh^bb'  ;Stauiien;  betreten^  sprachlos  sein^  nasaliert  dbamb(h)-]  vermutlich als  ^geschlagen,  betroffen  sein^  aus  einer  Grundbed.  .schlagen*'. Gr.  'rdq)og  n.  .Staunen,  Verwunderung'.  Perf.  ep.  ion.  ze&rjTta,  Partiz. Aor.  tacpoyv  .erstaunen'.  d^cjjtTWy  S-üjtisvu)  (.staune  an  =)  schmeichle'  (s. Boisacq  s.  v.  d-öjxp),  nasaliert  d-d(,ißog  n.  .Staunen.  Verwunderung.  Schrecken'. i^aixßso)  .staune,  erstaune,  erschrecke';  zum  ß  vgl.  Schwyzer  Gr.  Gr.  I  333, 833;
o-ot.  afdöhn  .verstumme!'.
Unter  Voraussetzung  einer  Grundbed.  .schlagen'  kann  folgende  germ. Sippe  angereiht  werden:  anord.  dafla  .im  Wasser  plätschern',  norw.  dial. dahba  .stampfen,  festklopfen',  ano
```


### [2026-09-05T18:24:03.118Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:24:09.509Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 246 247 248; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt | head -40; done",
 "description": "Print Pokorny leaves 246-248"
}
```


## [2026-09-05T18:24:10.535Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"to set, put\" AHD_watkins1985.txt | head -20; echo ----; grep -n \"^dhe\" AHD_watkins1985.txt | head; echo ---- ; head -40 AHD_watkins1985.txt",
 "description": "Explore AHD Watkins file"
}
```


### [2026-09-05T18:24:11.689Z] TOOL RESULT

```
=== leaf 246 ===
 ,gehe  hervor,  sprosse,  entspringe reiche  hin',  Partiz.  dal'd  (*dalno-)  usw.  (über  djale  ,Kind,  Jüngling' s.  unter  3.  del-).
Da    das   Alb.   nur    ursprünglichem   «2 -Vokalismus  sich  fügt   und  daher, auch  im  Griech.  die  Stufe  ö  nicht  als  Ablautsneubildung  zu  ä  aufzufassei ist,   das   an   sich   aus  l  entwickelt  sein  könnte,  sind    bestenfalls  auf  eine Parallelwz.  "^dhel-  zu  beziehen:
vielleicht  arm.  dei  , Arznei'  (falls  aus  *Kraut);
cymr.  dail  , Blätter'  (analogischer  Sg.  dalen),  acorn.  delen  ,Blatt'  usw (i-Umlaut  von  o),  mir.  duille  (*dolln{a)  Kollekt.  f.  ,Blätter',  gall.  nojxnedovXa ,quinque  folium'  (Dioskor.) :  leg.  *pimpe-dola.
Sachlich  unbefriedigend  ist  Anreihung  von  germ.  *dilja  in  ags.  dile, as.  dilli,  ahd.  tilli,  dilli  ,Dill,  eine  stark  riechende  Doldenpflanze',  ablautend ags.  dyUj  älter  dän.  dyllßj  nhd.  mdartl.  tülle  ds.,  mit  anderer  Bed.  anord. dylla  ,Sonchus  arvensis  L.,  Gänsedistel';  wenigstens  sehr  unsicher  die  von ahd.  tola  ,racemus',  toldo  m.  ,Wipfel  oder  Krone  einer  Pflanze',  nhd.  Dolde.
Eine  in  der  Bed.  abliegende  Sippe  ist  die  von  ags.  deall  ,berühmt', s.  dhel-  ,leuchten'.
WP.  I  825  f.,   Schwyzer  Gr.  Gr.  I  302,  703,  714,  720,  WH.  I  524.
dhanu'  oder  dhonu-  ,eine  Baumbezeichnung^  (?).
Ai.  dhdnvan-  n.,  dhdnu-  m.,  dhdnus-  n.  ,Bogen',  dhanvana-  m.  ,ein  be- stimmter Fruchtbaum'  :  ahd.  tanna  ,Tanne,  Eiche'  (*daniüö),  mhd.  tanne, and.  dennia  ,Tanne'.
WP.  I  825.
.:^. j&<.-
235
dbaü'  ,würg-en,  drücken,  pressen'.
j^v.  dvaidl  1.  Du.  Präs.  Med.  ,wir  bedrängen',  davqs-cinä  (kann  für dtivqs-  stehen)  , obwohl  sich  dazu  drängend';  phryg.  ödog'  .  .  .  vrtd  Oovywv Iv/.og  Hes.  (davon  der  Volksname  /läot,  Dä-ci),  1yd.  Kav-davXrjg  {^-kw- äyXV?  , Hundswürger'),  vgl.  Kav-ödwv,  Name  des  thrak.  Kriegsgottes,  illyr. Q\,T  Can-davia]  dhauno-s  ,Wolf'  als  , Würger'  im  lat.  GN  Faunus  (zu  gr. ^avvoV  -d-TjQiov  Hes.)  =  illyr.  Daunus  (davon  VN  Javnoi,  Bewohner  der apul.  Landschaft  JDaimia]  vgl.  thrak.  Javviov  Tslyog)-  gr.  Zevg  QavXiog (].  i.  ,Würger'  (thessal.;  s.  auch  Fick  KZ.  44,  339),  mit  Ablaut  gr.  ^cog, ^u){J=)ög  , Schakal'  (d.  i.  , Würger');
o-ot.  af-dauips  ,iGy,vl^€vogj  geplagt';
aksl.  davljg,  daviti  .sticken,  würgen',  russ.  davith  , drücken,  pressen, würben,  zerquetschen',  ddvka  , Gedränge'.
WP.  I  823,  WH.  I  468.
Über  dhäu-  , staunen^  s.  u.  dheid-,
j.  dhe-,  redupl.  dhe-dh{e)-  Lallwort  der  Kindersprache  für  ältere  Familien- glieder. Gr.  d-slog  , Onkel',  dela  , Tante'  (*^rj-og,  ^rj-ä),  rrj&rj  , Großmutter'  (aus *^j-^r]),  ital.  (venet.)  deda  ,Tante'(?),  gr.  rrj&ig  ,Tante'  (dazu  GN  QsTig)', illyr.  deda  , Amme'  (Krähe  IF.  55,  121  f.),  also  wohl  ursprüngl.  zur  Wz. dhe(i)-  , säugen';  lit.  dede,  dedis  , Oheim'  (aber  diedas  , Greis'  aus  wr.  dzed ds.),  aksl.  dedz  , Großvater';  ähnlich  nhd.  deite,  feite,  Schweiz,  däddi  ,Vater, Greis',  russ.  djddja  , Onkel'.
WP.  I  826,  Trautmann  47,    Schwyzer  Gr.  Gr.  I  193.
2. 
=== leaf 247 ===
  dhe-    , setzen,    stellen,    legen';    Nominalbildungen:    -dhe-,    db-i-,  -dh-o-; dhe-k-ä;  dhe-li-,  dhe-lo-;  dhe-men-,  dhe-mi-,  dho-mi-,  dhö-mo-, dho-mo-;    dhe-dh-mo-;    dhe-no-;    dhe-tel-;    dhe-ter-,    dhQ-ter-; dhe-to-,  dhQ-to-,  dhe-tu-. Ai.  dddliäti,  av.  daöäitl  ,er  setzt',  apers.  Impf.   Sg.  adadä   ,er   hat  ein- gerichtet', ai.  Aor.  d-dhä-m  ,ich  setzte',  Med.  3.  Sg.  d-dhita  (=  gr.  ed^ezo) ;  to- Partiz.   ai.  hitd-h  (-dhitd-h  in  ved.  Kompositis)  , gesetzt'  (=  lat.  con-dituSj ab-ditus,  creditus,  wohl  auch  gr.  dsTog  ,gesetzt,  bestimmt'),   mit  Vollstufe av.  apers.  data-  (=  lit.  detas  ^gesetzt',  apr.  sen-ditans  Akk.  PL  f.  ,gefaltet*, auch  gr.  d-r^TOV  ßco^iöv  Hes.,  eig.  , Aufgestelltes,  Aufsatz');  Inf.  ai.  dhä-tum (=  lit.  det%  Supin.,  aksl.  deth  ,zu  setzen'  :  lat.  [spät]  conditus,  -ns  m.  , Grün- dung', Supin.  -um,  -ü,  vgl.  auch  ai.  dhätu-h  m.  , Bestandteil,  Satz',  av.  vldätu- n.  ,Begründung,  feste  Fügung');  to-Präs.  ai.  dhäyate  , setzt  für  sich'  (=  lett. dejn,  det  ,Eier  legen',  deju  det   , zusammenlöten',   aksl.   däj^  ,lege',   acech. deju  ,tue,  mache');  Perf.  ai.  dadhäu,  dadhimd,  av.  3.  Sg.  dada  (:  gr.  rs&e- uccL,  lat.  -didl,  osk.  pril-ffed,  ahd.  teta  usw.).
236
Arm.  ed  Aor.  ,er  setzte'   (=  ai.  cUdhät]   1.  Sg.  edi,  2.  Sg.  ecZtV),  p^i dnem  ,ich  setze'  (*dinem,  idg.  *dhe-no-,  vgl.  russ.  cZenw  , setze,  stelle,  le, skr.  djenem  ,tue,  stelle,  lege') ;
phryg.  sdaeg  ,posuit'  (*e-dkd-es-t?  eher  =  hitt.  da-a-is)] gr.  Ti&rjiu  , setze'  (Aor.  I';9'jjxa  —  s.  unten  — ,  ed-eixEv^  ed-exo,  Fut.  ^^^ Partiz.  d-axog)]
messap.  hi-pa-des  ,posuit'  (*gh{-po-dhes-t,   J.  B.  Hofmann  KZ.  63,  267). lat.    abdere    , wegtun,    verstecken,   äTtozid-evar,    con-dere    , gründen,   eia-       ' legen;  bergen,  bedecken'  (dazu  Cönsus  [*kom-d-to-]  Gott  des  Ackerbaues)    ''"  '■ 2)erdere    , vernichten',    credere    .glauben,    vertrauen'    (s.  u.  *ke7'ed-  ,Herz')- über  Einmischung  von  zu  dao-e  gehörigen  Formen  s.  WH.  I  362;   Perf condidl  usw.,  osk.  irrü-ffed  ,posuit'  {*-fefed).
Mit  einer  /c-Erw.  lat.  faciö,  -ere,  fecl  (:  edrjxa),  factum  ,tun,  machen' osk.  fakiiadj  umbr.  facia  ,faciat',  fahurent  Fut.  II  ,fecerint*,  praeu. (Manios-Inschrift)  fhej^haked  ,fecit',  osk.  fefacit  Konj.  Perf.  ,fecerit' fefacMst  Fut.  II  ,fecerit';
mit  *fek-  umbr.  feitic,  fette  ,facito':
fac'ilis  , (tunlich)  leicht',  umbr.  facefele  ds.;  facies  , Aussehen,  Erschei- nung,  Antlitz',  facinus,  pontifeXj  ar
=== leaf 248 ===
tifex  bene-ficus  u.  dgl.;  zur  Bed.  von interficiö  ,töte'  (,*lasse  verschwinden')  vgl.  ai.  antar-hita-h  ,versch wunden'. Dieselbe  /c-Erw.  außer  in  gr.  eO^rjxa  auch  in  &rj'Ar]  , Behältnis',  ai.  dha- kd-h  , Behälter'  und  phryg.  ad-öayisv  ,afficit',  Med.  aö-öaxsTOQ]  ven.  vha^s&o ,fecit'  (*fak-s-to,  das  /  wohl  aus  dem  Ital.);  hitt.  dak-ki-es-zi  (dakkeszi) , macht,  stellt  hin'  (:  lat.  facessö),  dak-su-ul  (daksul)  , freundlich'  (:  alat. facul)]  vielleicht  toch.  A  täkä  ,ich  wurde',  B  takäwä  ds.  (anders  Pedersen Toch.  194);
gall.  dede  .posuit'j  vgl.  lat.  con-,   ab-,   cre-didi,   ahd.    teta   ,ich   tat';   air. -tarti  ,gibt'  {Ho-ro-ad-dit  aus  *dhe-t),  Perf.  do-rat  {*to-ro-ad-dat  aus  *dhd-t),     ■ Thurneysen  Gr.  35;
ahd.    töm,    tuom,   as.    tön,   ags.    dorn    ,tue',    Inf.    ahd.  tuoiij    as.   ags.  dön (*dhö-m)   ,tun',   Prät.  ahd.  teta   ,ich  tat'  (2.  Sg.  täti,  PI.  tätu-m;   nach  dem Typus  got.  setum  umgebildet),  as.  deda  (2.  Sg.  dedös,  3.  PI.  dädun,  dedun),   .v/ ags.  dyde  <  dudi  (s.  oben  zu  ai.  dadhäu);  Part.  Perf.  Pass.  ahd.  gi-tän,  ags.  ^' dön  ,getan'  aus  *dhe-no-  =  aksl.  o-dem  ,umgelegt,  bekleidet';  "
in    der  Endung   des    schwachen   Präter.  (got.    salbö-dedun   usw.)    pflegt man  meist    die    Wurzel    dhe-   zu    suchen,    hingegen    in    got.    kunpa   , er- kannte',   das   idg.    't'   enthalten   muß,    eine   andere   Bildung   anzunehmen.     - Vgl.  Hirt,  Idg.  Gr.  IV,  99,    Sverdrup  NTS.  2,  55  ff.,   Marstrander,  NTS. 4,  424 f.,  Specht  KZ.  62,  69  ff.,  Kretschmer  Sbb.  Wien,  225.  Bd.,  2.  Abb.,  6 f.
lit.  deti  ,legen,  stellen',  Präs.  2.  PL  alt  deste  (*dhe-dh-te),  Sg.  demi,  desie-s,      : dest{i)  (vgl.  Büga  Kalba  ir  s.  158,  213),  neugebildet  dedii]  lett.  det  (s.  oben);  ^
237
aksl.  cUti  , legen'  (auch  ,sag-en'),  Präs.  dezdo  (^dediö)  und  dej^  (s.  oben); lit^o,  dejatl  ..legen,  verrichten';  -va-Iterativ  caksl.  o-dcvatl  ,(uratun),  bekleiden'^ ••uss.  devdtb  , hinlegen,  tun,  setzen';
dcazu  wohl  lit.  deviit,  devett  , Kleider  anhaben';  ein  formantisches  u  auch in  gr.  *x^o/axog  und  (assim.)  '■^•d-aJ'ay.og,  vgl.  ^occ^w  ,sitze',  ion.  ^wxog  (hom. ^öcoyiog  für  ^6[J^]ccy,og  geschrieben)  ,Sitz',  d-aßamv  ^ä^ov  )]  S-qovov  Hes., att.  auch  ^äxog  ds.,  hom.  ^adaaco  , sitze',  att.  poet.  d'daao)  ds.  (s.zur  gr.  Gruppe Hechtel  Lexil.  161  f.,  Boisacq  335);  vgl.  auch  thrak.  -dava  , Siedlung'  aus *diieuä  oder  *dh9uä]  wohl  Umbildung  nach  dem  Nebeneinander  *dü-: *dou-  , geben';
hitt.  da-a-i  (däl)  ,setzt,  legt',  1.  Sg.  te-eh-hi  {tehlii\  3.  PI.  ti-an-zi  (Pe- dcrseu  Tlitt.  91,  112 f.,  166),  Prät.  3.  Sg.  da-a-is]  vielleicht  auch  dak-ki-eszi (s.  oben);
toch.  A  tä-,  täs-,  tas-^  B  tes-  .l
```


### [2026-09-05T18:24:11.755Z] TOOL RESULT

```
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
119:The notion of carrying is represented by the widespread root bher-' (BEAR!), found in every branch except Anatolian. This root is noteworthy in that it formed a phrase né- men- bher-, “to bear a name,” which is re- constructible from several traditions, includ- ing English. This phrase formed a counterpart to né-men- dhé-, “to give a name,” with the verb dhé-', “to set, put,” in Sanskrit, Greek, and Slavic tradition. The persistence of these expressions attests the importance of the name-giving ritual in Indo- European society.
375:mild, gentle: DAFT. 2. Probably suffixed form *dhabh-ro- in Latin faber, artisan (< “he who fits together”): FABRIC, (FABRICATE), FORGE}. [Pok. 2. dhabh- 233.] dhal-. To bloom. Suffixed form *dhal-yo- in Greek thal- lein, to flourish, bloom, sprout (> thallos, a shoot): THALIA, THALLUS; PROTHALLUS. [Pok. dhail- 234.] dhé-', To set, put. Contracted from *dheo-. 1. O-grade form *dhé- in Germanic *don in Old English dén, to do: Dol; FORDO. 2. Suffixed form *dhé-ti-, “thing laid down or done, law, deed,” in Germanic *dédiz in Old English déd, doing, deed: DEED. 3. Suffixed o-grade form *dho-mo- in Germanic *démaz in: a. Old English dom, judgment (< “thing set or put down”): Doom; b. Old English -d6m, abstract suffix indicating state, condition, or power: -DOM; c. Old Norse -démr, condition (see ka-); d. Gothic déms, judgment, akin to the Germanic source of Russian Duma, Duma: Duma; e. Germanic denomina- tive *“ddmjan in Old English déman, to judge: DEEM. 4. Suffixed o-grade form *dhé-t- in Latin agential suffix -dés in Latin sacerdés, priest, “(performer of sacred rites” (see sak-). 5. Zero-grade form “dha- in: a. prefixed form *kom-dha- in Latin condere, to put together, establish, preserve (*kom, together; see kom): CONDIMENT; AB- SCOND, INCONDITE, RECONDITE, SCONCE?; b. compound *kred-dha- (see kerd-'). 6. Suffixed zero-grade form *dha-k- in: a. Latin facere (< *fak-yo-), to do, make (> French faire, to do), and Latin combining form -fex (< *.fak-s), “maker”: -FACIENT, FACT, FACTION, FACTITIOUS, FACTOR, FASHION, FEASIBLE, FEAT!, FEATURE, (FETISH), -FIC, (-FY); AFFAIR, AFFECT!, (AFFECT2), (AFFECTION), AMPLIFY, ARTIFACT, ARTIFICE, BEATIFIC, BENEFACTION, BENEFIC, (BENEFICE), (BENEFICENCE), BENEFIT, CHAFE, COMFIT, CONFECT, (CONFETTI), COUNTERFEIT, (DEFEA- SANCE), DEFEAT, DEFECT, (DEFICIENT), (DISCOMFIT), EDIFICE, (EDIFY), EFFECT, (EFFICACIOUS), (EFFICIENT), FACSIMILE, FACTOTUM, FORFEIT, HACIENDA, INFECT, JUSTIFY, MALEFACTOR, MALFEASANCE, MANUFACTURE, MISFEASANCE, MODIFY, MOLLIFY, NIDIFY, NOTIFY, NUL- LIFY, OFFICINAL, PERFECT, PETRIFY, (PLUPERFECT), PON- TIFEX, PREFECT, (PROFICIENT), PROFIT, PUTREFY, QUALIFY, RAREFY, RECTIFY, REFECT, (REFECTORY), RU- BEFACIENT, SACRIFICE, SCIRE FACIAS, SPINIFEX, SUF- FICE, (SUFFICIENT), SURFEIT, TUBIFEX, TUMEFACIENT, viviry; b. Latin derivative faciés, shape, face (< “form imposed on something”): FACADE, FACE, (FACET), (FA- CIAL), FACIES; (DEFACE), EFFACE, PRIMA FACIE, (SUR- FACE); c. Latin compound officium (< *opi-fici-om), service, duty, business, performance of work (*opi-, work; see op-'): OFFICE; d. further suffixed form *dha-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY. 7. Suffixed zero-grade form *dha-s- in Latin fds, divine law, right: NEFARIOUS. 8. Possibly Latin -farius, -doing: MULTIFARIOUS, OMNI- FARIOUS. 9. Reduplicated form *dhi-dhé- in Greek tithe- nai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, (APOTHECIUM), BODEGA, BOUTIQUE, DI- ATHESIS, EPENTHESIS, EPITHET, HYPOTHESIS, METATHE- SIS, PARENTHESIS, PROSTHESIS, PROTHESIS. 10. Suffixed form *dhé-k- in Greek théké, receptacle: THECA, TICK?; AMPHITHECIUM, BIBLIOTHECA, CLEISTOTHECIUM, ENDO- THECIUM, PERITHECIUM. 11. Suffixed zero-grade form *dha-mn in Greek thema, “thing placed,” proposition: (THEMATIC), THEME. 12. Reduplicated form *dhe-dhé- in Sanskrit dadhdti, he places: SANDHI. 13. Reduced form *dh- (see aw-2). [Pok. 2. dhé- 235.] dhé-2. To vanish. Contracted from *dhea-. 1. Possibly Old Norse d%sa, to languish, decay: DASTARD. 2. Possibly Old Norse *dasa, to tire out (attested only in reflexive form dasask, to become exhausted), akin to the Scandi- navian source of Middle English dasen, to stun: DAZE. [Pok. 3. dhé- 239.] dheb-. Dense, firm, compressed. Germanic suffixed form *dap-ra- in Middle Dutch and Middle Low German
----
376:dher-'
378:dher-2
----
American Heritage — Dictionary
of
Indo-European Roots
Revised and edited by Calvert Watkins
JUN 01 1985
American Heritage , Dictionary Indo-European Roots
American
Heritage
Dictionary do-European
Root
In
Revised and edited by Calvert Watkins
Houghton Mifflin Company Boston
Copyright © 1985 by Houghton Mifflin Company. All rights reserved. No part of this work may be reproduced or trans- mitted in any form or by any means, electronic or mechani- cal, including photocopying and recording, or by any infor- mation storage and retrieval system, except as may be expressly permitted by the 1976 Copyright Act or in writing by the Publisher.
All correspondence and inquiries should be directed to Reference Division, Houghton Mifflin Company One Beacon Street, Boston, MA 01208
Manufactured in the United States of America
Library of Congress Cataloging in Publication Data Main entry under title:
The American heritage dictionary of Indo-European roots.
Includes index. 1. Indo-European languages—Roots—Dictionaries. 2. English language—Etymology—Dictionaries. I. Watkins, Calvert. P615.A43 1985 412'.0321 84-27911 ISBN 0-395-37888-5 ISBN 0-395-36070-6 (pbk.)
Contents
Staff
Foreword
Preface Indo-European and the Indo-Europeans
Guide to the Dictionary
Indo-European Roots
Index
Table of Indo-European Sound Correspondences Chart of Indo-European Languages
Staff
Marion Severynse - Editor and Etymologist
Howard Webber - Publisher Margery S. Berube - Director of Editorial Operations
Dolores R. Harris - Senior Editor Pamela B. DeVinne - Editor Kaethe Ellis - Editor
Christopher Leonesio - Production Manager Patricia McTiernan - Editorial Production Assistant Donna Lee Muise - Editorial Production Assistant
Keyboarding Staff
Brenda J. Bregoli Celester Jackson Ron Perkins Caren Raimondi
Design Geoffrey Hodgkinson
Special Contributors
Elizabeth Collins Colin Danby Francine D. Figelman Susan Innes Trudy Nelson Amy Walton
Foreword
The American Heritage Dictionary of Indo-European Roots is a revised and expanded version of the Appendix of Indo-European Roots in The American Heritage Dictionary of the English Language published in 1969. This material is presented here for the first time in a separate volume. The present work has been designed as a companion to The American Heritage Dictionary: Second College Edition and contains a complete index to all the English words whose antecedents are given in the Dictionary of Indo-European Roots. The wealth of information about the Indo-European origins of the English vocabulary has now been made readily accessible to scholars, students, and all those who are interested in the history and development of the English language.
Marion Severynse
```


## [2026-09-05T18:24:30.644Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 297 298 299; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | grep -n -i -m5 \"famil\\|famul\\|dhaman\" ; done",
 "description": "Find Klein family entry leaf"
}
```


## [2026-09-05T18:24:30.796Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"famulus\" KLN_1966.txt | head -20",
 "description": "Grep Klein for famulus"
}
```


### [2026-09-05T18:24:32.242Z] TOOL RESULT

```
=== leaf 297 ===
=== leaf 298 ===
=== leaf 299 ===
16:eucairite,  n.,  a  copper  silver  selenide  (mineral.)  — Swed.  eukairit,  formed  with  suff.  -it  (represent¬ ing  Gk.  -iiry.  see  subst.  suff.  -ite)  fr.  Gk. Euxalpoic,  adv.  of  cuxatpoi;,  ‘seasonable,  op¬ portune’,  fr.  eu,  ‘well’  (see  eu-),  and  xoapXc,  ‘the right  season,  the  right  time’  (see  kairine).  The mineral  was  so  called  because  it  was  found  by the  Swedish  chemist  Baron  Jons  Jakob  Berzelius (1 779- 1 848)  soon  after  the  discovery  of  selenium. Eucalyptus,  n.,  a  genus  of  plants  of  the  myrtle family  (bot.)  —  ModL.,  lit.  ‘well  covered’, coined  by  the  French  botanist  L’Hdritier  de Brutelle  (1746-1800)  in  1788  fr.  eu-  and  Gk. xaXu7tx64,  ‘covered’,  verbal  adj.  of  xocXurexeiv, ‘to  cover,  conceal’  (see  calyptra);  so  called  in allusion  to  the  cap  covering  the  bud.
17:Eucharis,  n.,  a  genus  of  the  plants  of  the  amar¬ yllis  family  (bot.)  —  ModL.,  fr.  Gk.  e6xaP1?. ‘pleasant,  agreeable’,  fr.  e5,  ‘well’,  and  X“P‘S> ‘favor,  grace’.  See  next  word.
23:euclase,  n.,  a  brittle  green  silicate  of  beryllium and  aluminum  (mineral.)  —  Lit.  ‘that  which breaks  easily’;  formed  fr.  eu-  and  Gk.  xXamc, ‘a  breaking’,  from  the  stem  of  xXav,  ‘to  break’. See  clastic  and  cp.  words  there  referred  to. Euclea,  n.,  a  genus  of  plants  of  the  ebony  family (bot.)  —  ModL.,  lit.  ‘glorious’,  fr.  eGxXekx,  ‘glory’, fr.  euxXe(£,  ‘famous,  glorious’,  which  is  formed fr.  eu  (see  eu-)  and  xXeo?,  ‘fame’  (see  Eteocles); so  called  in  allusion  to  the  beautiful  foliage. Euclid,  euclid,  n.  —  Short  for  Euclid's  geometry, i.e.  geometry  based  on  the  treatise  of  Euclid, the  great  Greek  mathematician  who  lived  about 300  B.C.E.  (The  name  lit.  means  ‘renowned’, and  is  rel.  to  euv.Xeyp,  ‘renowned’,  prop,  ‘of good  report’,  fr.  e5,  ‘well’,  and  xX(op,  ‘fame’; see  prec.  word.)
44:Eupatorium,  n.,  a  genus  of  plants  of  the  thistle family  (bot.)  —  ModL.,  fr.  Gk.  Eomxxopiov, Agrimonia  Eupatorium,  named  after  Eupator Mithridates,  who  first  used  it  for  medicinal purposes.
```


### [2026-09-05T18:24:32.292Z] TOOL RESULT

```
14349:family,  n.  —  L.  familia,  fr.  famulus,  fr.  OL.  famut, ‘servant’,  which  is  of  uncertain  origin.  It  pos¬ sibly  means  lit.  ‘belonging  to  the  house’,  and derives  fr.  I.-E.  base  *d¥-mo-,  ‘house’,  whence also  OI.  dMman,  ‘seat,  house’,  Gk.  ffaqi.6; (Hesychius),  ‘house’.  Base  *dhe-mo-  is  an  en¬ largement  of  base  *dhe-,  ‘to  put,  place;  to  do, make’.  See  do  and  fact  and  cp.  famulus  and  the second  element  in  forisfamiliate.
14353:Derivatives:  famous-ly,  adv.,  famous-ness,  n. famulus,  n.,  attendant,  esp.  on  a  magician.  — L.,  ‘servant’.  See  family, fan,  n.,  an  instrument  for  winnowing.  —  ME.,  fr. OE.  fann,  fr.  L.  vannus,  ‘winnowing  fan’.  See van,  ‘winnowing  fan’.
```


## [2026-09-05T18:24:39.217Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.index('family,  n.  —  L.  familia')\nleaf=t[:i].count('\\f')\nprint('leaf',leaf)\n\" ",
 "description": "Compute Klein leaf for family"
}
```


## [2026-09-05T18:24:40.641Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhedh\\|dhēdh\\|tēthē\\|tethe\\b\" IEC.txt | head -20",
 "description": "Grep Mann IEC for dhedh"
}
```


### [2026-09-05T18:24:40.928Z] TOOL RESULT

```
leaf 310
```


### [2026-09-05T18:24:41.000Z] TOOL RESULT

```
2701:nature’; Finn. LW tapa, id.; Li. cf. dabnùs, dabinti “elegant; to adorn’ dhābh- ‘limp, flaccid’. Cf. dhabros D Skt. (ambig.) -dābhyah (‘frivolous’, in a- ° *serious); Alb. i dobë, í dobët ‘weak’; Sw. dof (‘sultry, blunt, stupid". Infl. of LG? & NG döf ‘stupid’. See dhoubh-); Go. cf. af- dobnan ‘grow dumb’ dhabhló, dhabhró, ið (?) ‘surge’. Cf. dabh- Skt. dabhráh (ocean; EMDu. daveren ‘tremble’; ON dafla ‘dabble, splash? dhadhló, dhadhró, ið (?) ‘waver, tremble’. Cf. dhedher- MHG tatern ‘chatter’; G tattern ‘shake, dod- der, twaddle’; Icel. daðra ‘flirt; Sw. darra ‘tremble’; cf. E dial. daddle ‘stagger, dawdle’. (A form *dhadh- seems to be present in EME to dade ‘to toddle’ and Li. dadu, eti “cackle') dhagh- ‘beautiful, fine, abundant, good, harmonious’ Gaul. dago-; OBr. da; W da ‘good’; MHG tagen, tegen ‘confer, arbitrate’; Du. dagen ‘summon’; G cf. Reichs-tag; Du. Rijks-dag; EME days-man ‘arbitrator’; EMDu. cf. dege- lijk ‘honest’; LG cf. d&g, m & f ‘good man- ners’; Li. dažyti ‘to eeh daZalas “orna- ei: ; dažnas ‘many 3... * Latv daZs, id. dhaloros, is ‘verdant, lush". WP I, 825. Cf. dhalió Arm. dalar (i-st. *green"); Gk. thalerós, id. dhalgho “hold, squeeze'
2728:dhedh- ‘nurse’ Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-é-) Tēthús (nurse of Hera) and (alleged) téthe ‘nurse’; Ir. cf. deol, diúl ‘suckling’, isophonic w. Gk. thēlé, see dhēl-; cf. also Ir. dedel ‘she-calf
2730:dhedherið ‘shake, dither, hesitate, lounge’. Cf. dhadhlo Arm. dederim ‘lounge, loiter; LG dädern ‘frolic; EME didder, v. ‘shiver; Lat. cf. *fibrillare ‘to twitch’ and (o-gde) G tattern ‘tremble; ON daðra ‘dally, flir? but see dhadhló
2731:dhedhló (?) “suck? Lat. cf. fellare, id.; Ir. deolaim, id.
2732:dhedhmos, à ‘statute, law’. Cf. WP I, 829 and dhé-mi, dhídhe-, etc. . Gk. tethmós, thesmós; W deddf, id.; cf. MIr. dethbir (laws; adj. 'legal). See next
2733:dhedho, ið “put, set? (intensive form of dhé-mi, etc.) WP I, 827 OCS deZzdo; Srb. dedem; Li. dedü
2756:dhēiô dhēmi (2) ‘put, lay’. Cf. dhídhemi, dhesnos, dhetis, dhētos, etc. WP I, 827-820 and cf. also dhedh-, dhesio Ober da-; Tokh. AB Gs, B tes- (= Skt. dhàsyàmi: Arm. edic: Gk. thésó: Li. désiu &
2880:dhodhorio see dhadhlo, dhedher-
2933:-dhmos (deverbative noun-formant) Gk. sta-thmós, skar-thmós, etc. Cf. dhedhmos
```


## [2026-09-05T18:24:52.712Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==311' KLN_1966.txt | grep -nE \"^[0-9]{3}|[[:space:]][0-9]{3}[[:space:]]*$\" | head; echo \"--- first/last lines ---\"; awk 'BEGIN{RS=\"\\f\"} NR==311' KLN_1966.txt | head -3; echo ...; awk 'BEGIN{RS=\"\\f\"} NR==311' KLN_1966.txt | tail -3",
 "description": "Look for page numbers on Klein leaf 310"
}
```


### [2026-09-05T18:24:54.251Z] TOOL RESULT

```
--- first/last lines ---
air,  adv.,  fair-ly,  adv.,  fair-ness,  n. fairy,  n.  —  ME.  faierie,  ‘enchantment,  fairy’,  fr. OF.  faerie  (F.  feerie),  ‘enchantment’,  fr.  fae (F.  fee),  ‘fairy’.  See  fay,  ‘fairy’.
Derivatives:  fairy,  adj.,  fairy-dom,  n.,  fairy- hood,  n.,  fairy-ism,  n.,  fairy-like,  adj. fairy  tale.  —  Loan  translation  of  F.  conte  de  fe. faith,  n.  —  ME.  feith,  fr.  OF.  feid,  fei  (F.  foi), fr.  L.  fidem,  acc.  of  fides,  ‘trust,  belief’.  See  bid and  cp.  fidelity  and  words  there  referred  to. Derivatives:  faith-ful ,  adj.,  faith-ful-ly ,  adv., faith- ful-ness,  n„  faith-less,  adj.,  faith-Iess-ly, adv.,  faith-less-ness,  n.
Faith,  fern.  PN.  —  From  prec.  word, fake,  tr.  v. ,  1 )  to  counterfeit ;  2)  to  alter,  to  tamper with;  intr.  v.,  to  practice  faking  ( colloq .)  — Perh.  a  var.  of  feague.
...
Derivatives:  fame,  tr.  v.,  fam-ed,  adj. familiar,  adj.  —  OF.  (=  F.)  familier,  fr.  E.fami- lidris,  ‘pertaining  to  a  household,  domestic', dissimilated  fr.  *familia-lis,  fr.  familia,  ‘house¬ hold’.  See  family  and  adj.  suff.  -ary. Derivatives:  familiar,  n.,  familiar-ism,  n.,  fami¬ liarity  (q.v.),  familiar-ize,  tr.  v.,  familiar-iz- ation,  n.,  familiar-iz-er,  n.,  familiar-ly,  adv. familiarity,  n.  —  F.  familiarite,  fr.  L.  familidri-
tatem,  acc.  of  familiaritas,  fr.  familiaris.  See familiar  and  -ity.
family,  n.  —  L.  familia,  fr.  famulus,  fr.  OL.  famut, ‘servant’,  which  is  of  uncertain  origin.  It  pos¬ sibly  means  lit.  ‘belonging  to  the  house’,  and derives  fr.  I.-E.  base  *d¥-mo-,  ‘house’,  whence also  OI.  dMman,  ‘seat,  house’,  Gk.  ffaqi.6; (Hesychius),  ‘house’.  Base  *dhe-mo-  is  an  en¬ largement  of  base  *dhe-,  ‘to  put,  place;  to  do, make’.  See  do  and  fact  and  cp.  famulus  and  the sec
```


## [2026-09-05T18:24:54.254Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.index(\\\"dhedh- 'nurse'\\\") if \\\"dhedh- 'nurse'\\\" in t else t.index('dhedh- ‘nurse’')\nprint('leaf',t[:i].count('\\f'))\n\"",
 "description": "Compute IEC leaf for dhedh"
}
```


### [2026-09-05T18:24:56.167Z] TOOL RESULT

```
leaf 111
```


## [2026-09-05T18:25:10.160Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 105 112; do echo \"== leaf $((n-1)) ==\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -c 400; echo; done",
 "description": "Check IEC leaves 104 and 111 content"
}
```


### [2026-09-05T18:25:11.854Z] TOOL RESULT

```
== leaf 104 ==
o; Cz. (ambig.) drdol "dot: Li. cf. dirdénu, -dénti ‘crawl, as traf- fic’. (For Arm. tartam ‘hesitant’, cf. Gk. tetra- maíno ‘tremble’, qua *títrém-)
drgl- (?) ‘fail, fal LG torkeln ‘tumble, stumble’; Big. cf. drágla ‘feeble woman, trollop’; drágla$ ‘weakling; jade (horsey; drágliv «lean, weak’. The Blg. forms are ambig. cf. dhrugh-.
drgh- ‘têar, pull, pluck�
== leaf 111 ==
 (?) talgen ‘knead’. (Cor. dalgh, m. dalghen, f. ‘hold, grip’ represents a formula *dhalghs-)
dhalio (dhaliio, dhales-) ‘fortune, produce, outcome”. Cf. dhalio
Gk. thalía, f. thálea, npl.; W daili, pl deilliau -
*próduce?; (?) OCz. dole ‘fortune, success’; R dolja ((2) ‘destiny’. In sense (1) see dal- ‘part, share’, as in OCS, but SI. forms are ambig.).
dhalið ‘come o
```


## [2026-09-05T18:25:19.452Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(100,120):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', t[i])\n    nums2=re.findall(r'\\b1[5-9]\\d\\b', t[i][:200]+t[i][-200:])\n    print(i, nums, nums2)\n\"",
 "description": "Find printed page numbers in IEC leaves"
}
```


### [2026-09-05T18:25:20.863Z] TOOL RESULT

```
100 ['157', '10', '15', '20', '25', '30', '35', '40', '45', '158'] []
101 ['159', '20', '25', '30', '35', '40', '45', '160'] []
102 ['161'] []
103 ['10', '15', '20', '25', '30', '35', '40', '45', '162', '163'] ['162']
104 ['10', '15', '20', '25', '30', '35', '40', '45', '164', '165'] []
105 ['15', '20', '23', '30', '35', '40', '45', '166', '167'] []
106 ['10', '15', '20', '25', '30', '35', '40', '45', '168', '169'] ['169']
107 ['10', '20', '25', '30', '35', '40', '45', '170'] []
108 ['171', '20', '25', '30', '35', '40', '45', '172'] ['171']
109 ['173', '20', '25', '30', '35', '40', '45', '174'] ['173']
110 ['175', '176', '20', '25', '30', '35', '40', '45', '177'] ['177']
111 ['10', '20', '25', '30', '35', '40', '45', '178', '179'] ['179']
112 ['10', '20', '25', '30', '35', '40', '45', '180'] []
113 ['181', '20', '25', '30', '35', '40', '45', '182'] []
114 ['183', '15', '20', '25', '30', '35', '40', '45', '184'] []
115 ['185', '186'] []
116 ['187', '10', '15', '20', '25', '30', '35', '40', '45', '188'] ['188']
117 ['189'] []
118 ['15', '20', '25', '30', '35', '40', '45', '190', '191'] []
119 ['20', '25', '30', '35', '40', '45', '192', '193'] []
```


## [2026-09-05T18:25:25.020Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(307,314):\n    print(i, re.findall(r'(?m)^\\s*(\\d{3})\\s*$', t[i]), re.findall(r'\\b5[6-9]\\d\\b', t[i]))\n\"",
 "description": "Find Klein printed page numbers"
}
```


### [2026-09-05T18:25:26.974Z] TOOL RESULT

```
307 ['566', '567'] ['566', '567']
308 ['300'] []
309 ['570', '571'] ['570', '571']
310 [] []
311 ['574', '575'] ['574', '575']
312 ['576', '311'] ['576']
313 ['578', '579'] ['578', '579']
```


## [2026-09-05T18:25:36.054Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW famulus ===\"; grep -n \"famulus\" LEW_1910.txt | head -5; echo \"=== LEW facio ===\"; grep -n \"^facio\\|faciö\\|facio,\" LEW_1910.txt | head -5; echo \"=== LAT famulus ===\"; grep -n \"famulus\\|famul \" LAT.txt | head -8; echo \"=== LAT facio ===\"; grep -n \"facio\" LAT.txt | head -5",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-05T18:25:36.174Z] TOOL RESULT

```
=== LEW famulus ===
=== LEW facio ===
=== LAT famulus ===
3700:famulus et seruus. Le diminutif d'affection ancilla est au contraire
20489:famulus, -f m.: serviteur, domestique; famula, -ae f.: servante
20490:(semble un substitut recent de anci l la). L'adj .famulus, -a, -un parait
20494:trouver plus frequemment 1 1 adj .famulus: il y sert a rendre SouXoC.
20502:mel = famulus - , osq .famelo = familia’, ombr.fameflas = familiae. Les
20503:graamairiens differencient seruus de famulus, e.g. Isid., Diff. 1,535,
20533:De famulus sont formas: famularis - , famulitas (arch., rare); famulor,
57852:nata?). Comme pour famulus , 1 'emploi de 1 'adj. semble secondaire >
=== LAT facio ===
997:malorum; abolitor, abolefacio (Tert.). La glose amXeicfw, CGL II 333,45, se
1516:aussi dans 1 'indigitamentum Adolenda, et le compos6 adolefacio (Acta
2173:"impropre" (Br^al-Bailly). - Ago est essentiellement "dnratif"; facio,
3134:Apparaissent en bas latin: amaro, -as; amare facio; amaresco, -is,
4369:cf. facio, pro-ficiscor) dont il existe un doublet actif apisco chez
```


## [2026-09-05T18:25:38.158Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT family ===\"; grep -n \"^FAMILY\\|^FAMOUS\\|^BOUTIQUE\\|^THEME\\|^THESIS\\|^DEED\\|^DO,\" SKT.txt | head -10; echo \"=== WLD Bd1 dhē ===\"; grep -n \"dhē-\\|dhē(i)\" incoming/WLD/WLD_Bd1_pages.txt | head -10",
 "description": "Grep Skeat and Walde-Pokorny"
}
```


### [2026-09-05T18:25:38.236Z] TOOL RESULT

```
=== SKT family ===
19535:THEME,
=== WLD Bd1 dhē ===
```


## [2026-09-05T18:25:40.546Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20489,20545p' LAT.txt",
 "description": "Read Ernout-Meillet famulus entry"
}
```


### [2026-09-05T18:25:40.601Z] TOOL RESULT

```
famulus, -f m.: serviteur, domestique; famula, -ae f.: servante
(semble un substitut recent de anci l la). L'adj .famulus, -a, -un parait
avoir 4 te forme secondairement sur le nom; 1'emploi en est assez rare
(un ex. de Pomponius k l* 4 poque r^publicaine; les ex. de 1 'epoque
imperiale sont po^tiques). Il faut arriver a la 1. de 1'figlise pour
trouver plus frequemment 1 1 adj .famulus: il y sert a rendre SouXoC.
Cf. serua, cr 4 e sur seruus.
Deriv^: familia f. Cf. pour la phonetique Siculus/Sicilia.
Famulus, familia sont des mots italiques, et, en latin, peut-etre
des emprunts a 1 'osque: famuli origo ab Oscis dependet, apud quos
seruus famel nominabatur, unde et familia uocata, P.F.77,11. Le t 4 moi-- 383 -
fanum
gnage de Festus est confim^ par les inscriptions, oaq.famel, p£l. fa-
mel = famulus - , osq .famelo = familia’, ombr.fameflas = familiae. Les
graamairiens differencient seruus de famulus, e.g. Isid., Diff. 1,535,
serui sunt in bello capti... famuli autem ex propriis familiis orti.
Mais la distinction ne r^pond pas aux faits; Andromaque, captive
de guerre, se designe par famula dans Vg., Ae.3,3*9, me famulam famu¬
loque Heleno transmisit habendam. Famulus, qui senble contenir un
suffixe de non d'agent (cf. baiulus, gerulus), a d 4 sign£ peut-etre un
esclave charg^ d'une fonction speciale, valet, etc., mais ce sens est
impossible a pr^ciser par les temoignages qui nous restent, tandis
que seruus designe la condition juridique de 1'esclave.
Familia (ancien g£n. peut-etre dialectal familias dans pater, mater,
filius familias) a du designer 1 1 ensemble des esclavAs et des ser-
viteurs vivant sous un m£me toit, par opposition a la gens, cf. les
expressions conserv^es dans des l.techniques familia gladiatoria,
familia monetalis, etc.; puis la maison tout entibre, maitre, d'une
part, et femme, enfants et serviteurs vivant sous sa domination, cf.
Pl.,Au.«, ego sum Lar familiaris ex hac familia. Aprbs la mort du
pater familias, le mot familia designe le groupe de ceux qui etaient
autrefois sous sa puissance et qui en sont sortis p«.r son d^cbs ( agnati,
agndtio). L'expression familia pecuniaque designe la fortune du maitre,
res familiaris, patrimonium - , familia englobe les res mancipi, l'en-
semble des choses indispensables k la famille; la terre, les animaux
de labour, les esclaves, e.g. Caton, Agr. 138, asinis feriae nullae
in familia sunt. Par extension de sens, familia est arriv£ k designer
les agnSti et les cognati et k devenir le synonyme de gens, tout au
moins dans la langue courante, mais non dans la langue du droit. Sur
ces diverses acceptions, v. Kohm, A It late in.Forschungen, lsqq.
Derives: familiaris: "ex eadem familia" fr^quent dans 1 'expression
res familiaris-, puis par extension "familier"; subst. fami l iaris m.:
ami, familier, intime, et familiaritas, familiariter, familiaricus;
familiarSsco,-is (Sid.); familiola (tard.); familiosus (id.).
De famulus sont formas: famularis - , famulitas (arch., rare); famulor,
-aris (famulS, tardif) avec ses d£riv 4 s, famulatus,-us m.(cic.), et
famulitium cr 6 e d'aprbs seruitium et non atteste avant Apulee, mais
peut-etre ancien, cf. P.F., 77, y, famuletium (sic) dicebatur quod nunc
seruitium - , confanulus,-lor.
Mots anciens, uSuels. - Les repr^sentants de familia dans les lan¬
gues romanes sont assez nombreux, en partie de formation savante; il
est k noter que 1'ital .famiglio designe le serviteur, et, plus spe-
cialement dans certains dialectes, le valet de ferme. M.L.3180.
Les autres langues indo-europ^ennes n'offrent aucun rapprochement.
On peut se demander sile mot, dont la forme n f est gubre indo-europ 4 enne,
n'est pas emprunt 4 , peut-etre a 1'etrusque qui a du fournir aux langues
italiques des mots de cette sorte.
```


## [2026-09-05T18:25:51.732Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT facio headword ===\"; grep -n \"^facio\\|^faci5\\|^facio,\" LAT.txt | head; grep -n \"facio, -is, feci\\|facio, -is\" LAT.txt | head; echo \"=== LEW famul ===\"; grep -n \"famul\" LEW_1910.txt | head -8; echo \"=== LEW facio ===\"; grep -n \"facio\\b\" LEW_1910.txt | head -8",
 "description": "Grep more Latin sources"
}
```


### [2026-09-05T18:25:51.833Z] TOOL RESULT

```
=== LAT facio headword ===
19915:facio, -is, feci, f&ctum, facere, yerbe italique; osq.fakilad,
19946:facio
20109:facio, ne peut passer pour indo-europienne; mais elle est parallfele
29254:facio, tardif, d'aprbs / erue facio.
4922:-is: se dessAcher (et exaresco), interarescS (Cic.); arefacio, -is
19915:facio, -is, feci, f&ctum, facere, yerbe italique; osq.fakilad,
=== LEW famul ===
=== LEW facio ===
```


## [2026-09-05T18:25:53.548Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN do/make 9.11 ===\"; grep -n \"9\\.11 DO\\|9\\.11 MAKE\\|MAKE, DO\" SYN.txt | head; echo \"=== SYN FAMILY ===\"; grep -n \"FAMILY\" SYN.txt | head -5; echo \"=== SYN NURSE ===\"; grep -n \"NURSE\" SYN.txt | head -5",
 "description": "Grep Buck synonyms"
}
```


### [2026-09-05T18:25:53.631Z] TOOL RESULT

```
=== SYN do/make 9.11 ===
=== SYN FAMILY ===
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2277:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 81
2314:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 83
2352:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 85
2402:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 87
=== SYN NURSE ===
```


## [2026-09-05T18:25:57.209Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19915,19950p' LAT.txt; echo \"..... 20105\"; sed -n '20100,20115p' LAT.txt",
 "description": "Read Ernout-Meillet facio entry"
}
```


### [2026-09-05T18:25:57.285Z] TOOL RESULT

```
facio, -is, feci, f&ctum, facere, yerbe italique; osq.fakilad,
ombr./asta, volsque FACIA "faciat", osq. fefacust, ombr. fakust "fecerit",
pr^nestin fhefhaked "fecit". Le pr^nestin et 1 'osque ont un parfait
A redoublement, en face de la forme A alternance du latin fSci (cf.
gr. e-Oqxa), qui, sons la forme feced, figure dejA sur le vase de Duenos;
1 1 ombr. facust a sans doute perdu un redoublement. Imp^r.present fac,
de *faci, comme dic de *dice (A cote de face Catulle, etc.); anciennes
formes en -s, faxo, faxim (dont une forme de passif faxitur ap.T.L.
33,10,6). Les temps de 1 'infectum du passif sont empruntes A un verbe
actif d'aspect duratif signifiant proprement "devenir" : fio, fieri
(arch./tere (?), fieri), fiebam, fiam (pas de participe pr^sent), qu'on
retrouve dans osque /itet "fiunt", et dont quelques formes sont con-
servees en roumain et dans certains dialectes italiens, M.L.3388.
La signification passive donn^e A ce verbe a amen£ la creation de
quelques formes passives, cosme fieri (d'emploi normal) et fitur,
fiebantur (rares et archaiques; cf. Thes. VI 84,8osqq.; un ex. de fitum
est est rest^.dans Liv. Andr., Od.30). Du reste 1 1 analogie aaaen£ la'crea¬
tion de quelques formes passives du type facidtur (Titinius, Com.97),
cf. Thes. VI 83,isqq.; et les compos 4 s de facio ont A l' 4 poque clas¬
sique leur passif en -ficior: adficior, conficior, tandis que 1'^poque
archaique connait encore des formes en fio : confit, defit (repris
par Vg., et sur lequel Pl. a fait superfit) ; interfieri, formes qui
sont demeur^es dans les composes du type calefio. Composes en - ficiS :
ad-, con-ficio, etc.
Le verbe appartient A une racine qui signifiait "mettre, placer,
poser" (TtGevat), ou, dans 1 'emploi absolu,"se mettre, se placer".
Le sens ancien est "poser, placer"; le passage au sens de "faire" a
du se faire par des emplois techniques: cf. en gr. ev 8 ’6X1,061, veoov.
11.18,541: lA-dessus (sur le bouclier d'Achille) il posa (c.-A-d.
"il repr^senta, il executa") un champ nouvellement d£frich 4 ; 8 op 7 K>u...
otov . ..e|ieAXe 0 T|Crenevai,, Od.30,394: 1 & repas qu'il devait placer37 3
facio
(c.-a-d."dresser" et "preparer"); sacrum facere (v. sacerdos) "placer
(sur 1 'autel) an sacrifice", d'on "faire un sacrifice". Le sens de
"poser, placer" apparait encore nettement en latin dans le simple, et
surtout dans ses compos 4 s et ses derives. Dans le simple, dans des
..... 20105
facinus,-oris n.: acte (bon ou mauvais ), actio n, cf. Serv., Ae. 1,51,
bonum facinus et malum facinus dicimus... Dans la 1 . familiAre "chose":
mirum facinus (Pl.), Figura etymologica dans Plaute, Au.587, hoc est
serui facinus frugi, facere quod ego persequor. A 1 'epoque classique,
se prend souvent en aauvaise part, cf.Cic.Verr.3,s,66 qui emploie en
gradation facinus, scelus, parricidium-, d'oA facinorosus = scelerosus.
Cf. Reichenbecher, De uocum scelus facinus usu, lena 1913. Meme suffixe
que dans fe-nus (v. ce mot).
La formation, itant tirie de l'iliment radical complexe fac- de
facio, ne peut passer pour indo-europienne; mais elle est parallfele
k celle de av. varsna-x "acte" en face de varazyeiti "il agit", et sans
doute k celle de skr . enah, av. agno "acte violent".
factio: reflete les deux sens de facere "faire" et "placer": i° ma-
nifere de faire, faqon" (rare, deux ex. dans Plaute, Ba.843 et Ru.1371,
quae haec factio est?-, les autres exemples sont trAs tardifs), usiti
comme terae de droit, testamenti factio. Conservi dans le sens de
```


## [2026-09-05T18:26:07.179Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"بوتیک\" \"پرانتز\" \"دده\" \"تِم\"; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done",
 "description": "Grep Mo'in files for Persian words"
}
```


### [2026-09-05T18:26:09.243Z] TOOL RESULT

```
Exit code 1
=== بوتیک ===
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
=== پرانتز ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
=== دده ===
MON_part1.txt:35
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26
incoming/MON/MON_2vol_Adena_v1_djvu.txt:35
MON_part2.txt:26
=== تِم ===
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
```


## [2026-09-05T18:26:12.611Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دده\" MON_part1.txt | head -20",
 "description": "Grep Mo'in for dadeh"
}
```


### [2026-09-05T18:26:12.670Z] TOOL RESULT

```
3823:کم‌بها دردده دله‌دزد. 
5666:کردار. اندازه» حد» عدده شمار. قاعده» 
6117:معدوم نگردده باقی؛ مق. ازلی. 
8027:احصان؛ حدجدده [ع. ۳ (مسص م ۰) استوار 
9661:محاسبه؛ شناخت خواص عددها. 
10133:0 عددها. در تداول بازاربان مجموع 
10664:ازل: ادده [ع.] (مص‌ل.) ابتدا نداشتن» آغاز 
10807:اژدها: قددهته (امر.) مار بزرگك. جانوری 
17551:انحناء: قععدده ۹ ف. انحنا] (مصل.) 
21628:کوینده» بددهان» فحاش)؛ مق. خوش زبانی. 
23976:بسشسسسیر: ۱ [ع] (رص.) مدده‌آور؛ 
26361:بهت: اه رادده [ع.] (مسص‌ل.) متحیر 
35887:ببوندده خواهد بیبوست» سوند» ببوندنده» 
38574:تنحفد: فمررددها [ع.] (مصل.) کینه گرفتن. 
39409:باد آوری. پنددهی؟ ج . تذ کیرات. 
41513:زباد شدن عدده تاد کت (امص.) 
58764:دادا؛ 1202 [تر. - دده] (ا.) کنیز. کنی ز کی که 
58800:دادده: .1 [ - داددهنده] (رص‌فا.) آنکه 
59965:دده: (۵-)1202 [- دد] (.) جانور درنده دد. 
59972:دده: (6-)4202 [قس. دادا] (۱.) جد بدری با
```


## [2026-09-05T18:26:15.692Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '58760,58770p;59960,59985p' MON_part1.txt",
 "description": "Read Mo'in dadeh entries"
}
```


### [2026-09-05T18:26:15.750Z] TOOL RESULT

```
داداف‌رین: 0 [- داد آفر بننده] 
(ص‌فا.) آنکه عدالت ابجاد کند. خدای 
تعالی. (مست.) داد ]ورد 

دادا؛ 1202 [تر. - دده] (ا.) کنیز. کنی ز کی که 
فرزندان کسی را خدمست کند. 

دادار؛ 11-1 (رص.) آفر یننده. بخشانند ه. 
خداء خلاق. 

دادار: 120-۲ (ص‌مر.) عادل؛ داد دهنده. 
کودکی که میل دارد غالبا به کوچه و خیابان 
رود. (کد.) زنی که گاه گاه از خانه بدر رود و 
با مردان بیگانه درآمیزد. شخص هرزه و 
بدعمل. 

دده: (۵-)1202 [- دد] (.) جانور درنده دد. 
قلندر؛ ج. ددگان. 


۰۴ فرهنگ فارسی معیر ۵ د ۵ 


دده: (6-)4202 [قس. دادا] (۱.) جد بدری با 
مادری. خال بیر» دابی‌بیر. کنیزکی که 
کودکان زا نز رک کند) کنیز ساه: 

ددیگرن 10-۲ [ - دودیگر] (ق. . تر تیب.) 
دوم انا 

در: 127 (ا.) آنجه که از چوب با آهن و 
غبره سازند و در دبوار» اشکاف» صندوق و 
جز آنها کار گذارند و آن باز و سته شود. 
در خروجی: دری که از آن خارج شوند؟ 
مق. در ورودی. در مخفی: دری نهانی در 
سرای که به هنگام ضرورت از آن خارج 
شوند. در ورودی: دری که از آن وارد
```


## [2026-09-05T18:26:46.362Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg125.png')\nim.crop((1820,630,1960,690)).resize((1120,480)).save('p125_tem.png')\n\"",
 "description": "Crop tem/tez script"
}
```


### [2026-09-05T18:26:48.337Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:26:51.278Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_tem.png"
}
```


### [2026-09-05T18:26:51.299Z] TOOL RESULT

```

```


## [2026-09-05T18:27:16.319Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 125 -l 125 -r 900 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg125_900 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg125_900.png'); print(im.size)\n# scale 3x from 300dpi coords\nim.crop((1800*3,600*3,1980*3,700*3)).save('p125_tem_hi.png')\nim.crop((1780*3,470*3,1980*3,560*3)).save('p125_butik_hi.png')\n\"",
 "description": "Render page at 900 dpi and crop"
}
```


### [2026-09-05T18:27:24.688Z] TOOL RESULT

```
(7650, 9900)
```


## [2026-09-05T18:27:26.897Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_tem_hi.png"
}
```


### [2026-09-05T18:27:26.918Z] TOOL RESULT

```

```


## [2026-09-05T18:27:35.750Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_butik_hi.png"
}
```


### [2026-09-05T18:27:35.763Z] TOOL RESULT

```

```


## [2026-09-05T18:27:42.343Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T18:27:42.387Z] TOOL RESULT

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


## [2026-09-05T18:27:48.536Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-\" \\\n \"https://www.etymonline.com/word/boutique\" \\\n \"https://www.etymonline.com/word/family\" \\\n \"https://en.wiktionary.org/wiki/famulus\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%CF%84%CE%AE%CE%B8%CE%B7\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 125, roots Dhe 2 / Dhedh 2: PIE *dheh1-, boutique, family/famulus, Persian dadeh, Greek tethe\" ;\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T18:27:51.249Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5f46c64056f8ef06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb98afe56665ecc7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1800323614bd8976.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7268d4ab7eb60974.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e5ef654e74f23ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61245d34e7c84c79.txt
```


## [2026-09-05T18:27:54.500Z] TOOL CALL #41: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"=== boutique ===\"; sed -n '1,60p' eb98afe56665ecc7.txt | grep -i -A5 \"boutique\"| head -30; echo; echo \"=== family ===\"; grep -i -m3 -A6 \"family (n\" 1800323614bd8976.txt | head -30",
 "description": "Read archived etymonline pages"
}
```


### [2026-09-05T18:27:54.580Z] TOOL RESULT

```
=== boutique ===
URL: https://www.etymonline.com/word/boutique
FETCHED: 2026-09-05T18:27:50Z
STATUS: 200
TITLE: Boutique - Etymology, Origin & Meaning

Boutique - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
--
 Origin and history of boutique 

 boutique (n.) 

 "trendy fashion shop," 1950, earlier "small shop of any sort" (1767), from French boutique (14c.), from Old Provençal botica , from Latin apotheca "storehouse" (see apothecary ). Latin apotheca directly into French normally would have yielded *avouaie .
 also from 1950 

 Entries linking to boutique 

 apothecary (n.) 

 mid-14c., apotecarie , "shopkeeper," especially "pharmacist; one who stores, compounds, and sells medicaments," from Old French apotecaire (13c., Modern French apothicaire ), from Late Latin apothecarius "storekeeper," from Latin apotheca "storehouse," from Greek apothēkē "barn, storehouse," literally "a place where things are put away," from apo "away" (see apo- ) + thēkē "receptacle" (from a suffixed form of PIE root *dhe- "to set, put").

 The same Latin word produced French boutique , Spanish bodega , German Apotheke . Cognate compounds produced Sanskrit apadha- "concealment," Old Persian apadana- "palace." Also in Middle English ypoticarie , potecarie , ipoticar . The modern spelling is a classical correction from c. 1600.

 Drugs and herbs being among the chief items of non-perishable goods, the meaning narrowed 17c. to "druggist" (the Apothecaries' Company of London separated from the Grocers' in 1617).

 Apothecaries were notorious for "the assumed gravity and affectation of knowledge generally put on by the gentlemen of this profession, who are commonly as superficial in their learning as they are pedantic in their language" [Francis Grose, "A Classical Dictionary of the Vulgar Tongue," 1796]. Hence, Apothecary's Latin , barbarously mangled, also known as Dog Latin .

=== family ===
 family (n.) 

 early 15c., "servants of a household," from Latin familia "family servants, domestics collectively, the servants in a household," thus also "members of a household, the estate, property; the household, including relatives and servants," abstract noun formed from famulus "servant, slave," which is of unknown origin.

 The Latin word rarely appears in the sense "parents with their children," for which domus (see domestic (adj.)) was used. Derivatives of famulus include famula "serving woman, maid," famulanter "in the manner of a servant," famulitas "servitude," familiaris "of one's household, private," familiaricus "of household slaves," familiaritas "close friendship."

 In English, sense of "collective body of persons who form one household under one head and one domestic government, including parents, children, and servants, and as sometimes used even lodgers or boarders" [Century Dictionary, 1889] is attested by 1540s. It is attested from 1660s as "parents with their children, whether they dwell together or not," also in a more general sense, "persons closely related by blood, including aunts, uncles, cousins;" earlier "those who descend from a common progenitor, a house, a lineage" (1580s).
```


## [2026-09-05T18:27:58.967Z] TOOL CALL #42: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"=== dadeh ===\"; grep -n -i -m40 \"Persian\\|Turkish\\|Etymology\\|nurse\\|nanny\\|دده\" 8e5ef654e74f23ef.txt | sed -n '1,60p'",
 "description": "Read Wiktionary dadeh page"
}
```


### [2026-09-05T18:27:59.027Z] TOOL RESULT

```
=== dadeh ===
4:TITLE: دده - Wiktionary, the free dictionary
6:دده - Wiktionary, the free dictionary 
62: Etymology 1 
71: Etymology 2 
80: Ottoman Turkish 
82: Toggle Ottoman Turkish subsection 
85: Etymology 
103: Persian 
105: Toggle Persian subsection 
108: Etymology 
132: دده 
199: Etymology 1
205: دده ( definite accusative دده‌ݧ , plural دده‌لر ) 
212: Declension of دده 
220: دده 
222: دده‌لر 
226: دده‌ݧ 
228: دده‌لریݧ 
232: دده‌که 
234: دده‌لرکه 
238: دده‌ݧ 
240: دده‌لری 
244: دده‌چه 
246: دده‌لرچه 
250: دده‌ده 
252: دده‌لرده 
256: دده‌له 
258: دده‌لرله 
262: دده‌واره 
264: دده‌لرواره 
266: Etymology 2
272: دده ( definite accusative دده‌ݧ , plural دده‌لر ) 
279: Declension of دده 
287: دده 
289: دده‌لر 
293: دده‌ݧ 
295: دده‌لریݧ 
299: دده‌که 
301: دده‌لرکه 
305: دده‌ݧ
```


## [2026-09-05T18:28:01.397Z] TOOL CALL #43: Bash

```json
{
 "command": "cd data/verification/sources/web && awk 'NR>=320 && NR<=420' 8e5ef654e74f23ef.txt | grep -n . | head -60",
 "description": "Read Persian section of dadeh page"
}
```


### [2026-09-05T18:28:02.919Z] TOOL RESULT

```
2: instrumental
4: دده‌له 
6: دده‌لرله 
8: equative
10: دده‌واره 
12: دده‌لرواره 
14: Ottoman Turkish
15: [ edit ] 
17: Etymology
18: [ edit ] 
20: Inherited from Proto-Turkic *tēte ( “ grandfather ” ) ; cognate with Azerbaijani dədə , Kazakh тәте ( täte ) and Turkmen däde .
22: Noun
23: [ edit ] 
25: دده • ( dede ) ( definite accusative دده‌یی ( dedeyi ) , plural دده‌لر ( dedeler ) ) 
27: grandfather , grandpa , gramp , a father of someone's parent 
28: Synonym: جد ( cedd ) 
30: ( by extension ) old man , gaffer , whitebeard , an elderly man 
31: Synonym: شیخ ( şeyh ) 
33: dervish , a Sufi mystic practicing voluntary poverty in devotion to God 
34: Synonym: درویش ( derviş ) 
36: dede , a religious leader in the Alevi and Ishiki communities
38: Declension
39: [ edit ] 
41: Declension of دده ( dede ) 
43: singular
45: plural
47: nominative
49: دده ( dede ) 
51: دده‌لر ( dedeler ) 
53: definite accusative
55: دده‌یی ( dedeyi ) 
57: دده‌لری ( dedeleri ) 
59: dative
61: دده‌یه ( dedeye ) 
63: دده‌لره ( dedelere ) 
65: locative
67: دده‌ده ( dedede ) 
69: دده‌لرده ( dedelerde ) 
71: ablative
73: دده‌دن ( dededen ) 
75: دده‌لردن ( dedelerden ) 
77: genitive
79: دده‌نك ( dedeniñ ) 
81: دده‌لرك ( dedeleriñ ) 
83: Possessive forms
85: 1st person singular
87: singular
89: plural
91: nominative
93: دده‌م ( dedem ) 
95: دده‌لرم ( dedelerim ) 
97: definite accusative
99: دده‌می ( dedemi ) 
101: دده‌لرمی ( dedelerimi )
```


## [2026-09-05T18:28:06.657Z] TOOL CALL #44: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -n \"Persian\" 8e5ef654e74f23ef.txt | tail -20; echo ----; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/web/8e5ef654e74f23ef.txt',encoding='utf-8').read()\ni=t.rfind('\\nPersian\\n')\nprint(t[i:i+1800])\nEOF",
 "description": "Read Persian dadeh etymology"
}
```


### [2026-09-05T18:28:08.113Z] TOOL RESULT

```
103: Persian 
105: Toggle Persian subsection 
688: Persian
699: ( Classical Persian ) IPA ( key ) : /da.ˈda/ 
756: Iranian Persian dialectal kinship terms
758: Iranian Persian dialectal kinship terms
764: Standard Iranian Persian
898: Dari Persian dialectal kinship terms
900: Dari Persian dialectal kinship terms
1044: Persian terms with IPA pronunciation 
1045: Rhymes:Persian/a 
1046: Rhymes:Persian/a/2 syllables 
1047: Persian lemmas 
1048: Persian nouns 
1049: Persian dialectal terms 
1050: Persian colloquialisms 
1051: Persian terms with quotations 
1052: Persian terms with historical senses 
1058: Persian terms with non-redundant manual transliterations 
----
```


## [2026-09-05T18:28:10.499Z] TOOL CALL #45: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '686,760p' 8e5ef654e74f23ef.txt",
 "description": "Read Persian section text"
}
```


### [2026-09-05T18:28:10.545Z] TOOL RESULT

```
 Redhouse, James W. ( 1890 ), “ دده ”, in A Turkish and English Lexicon ‎ [5] , Constantinople: A. H. Boyajian, page 892 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 A babble word .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /da.ˈda/ 

 ( Dari, formal ) IPA ( key ) : [d̪ä.d̪á] 

 ( Dari, formal ) IPA ( key ) : [d̪ä.d̪á] 
 ( Kabuli ) IPA ( key ) : [d̪ä.d̪á] 

 ( Hazaragi ) IPA ( key ) : [d̪ä.d̪á] 

 ( Iran, formal ) IPA ( key ) : [d̪æ.d̪é] 

 ( Tajik, formal ) IPA ( key ) : [d̪ä.d̪á] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 dada

 Dari reading ? 

 dada

 Iranian reading ? 

 dade

 Tajik reading ? 

 dada

 ( Bushehr ) IPA ( key ) : [d̪e.d̪é] 

 Noun
 [ edit ] 

 دده • ( dada / dade ) ( Tajik spelling дада ) ( dialectal or colloquial ) 

 sister (blood relative)

 sister , sis (word of address for women of similar age)
 2025 , داریوش غریب زاده , زیر درخت بابُل , Shiraz, Iran: Pirsook, page 40 : شما محبت کردین چای و شربت و قلیون دادین، لیمو چه قابلی داره دِدِه . šomâ mohabbat kardin čây o šorbat o qelyun dâdin, limu če qâbeli dâre dede . You were very kind to give me tea and sherbet and hookah. You really deserve the lemons, sis . 

 ( historical ) maidservant , housemaid 

 ( historical ) female slave 

 Descendants
 [ edit ] 

 → Khalaj: dədə 

 See also
 [ edit ] 

 Iranian Persian dialectal kinship terms

 Iranian Persian dialectal kinship terms
 واژگان لهجه‌های فارسی ایرانی برای خویشاوندان نسبی 
 vâžegân-e lahja-hâ-ye fârsi-ye irâni barâ-ye xišâvandân-e nasabi
```


## [2026-09-05T18:28:16.806Z] TOOL CALL #46: Bash

```json
{
 "command": "cd data/verification/sources/web && python3 - <<'EOF'\nt=open('61245d34e7c84c79.txt',encoding='utf-8').read()\ni=t.find('Etymology')\nprint(t[i-200:i+1400])\nEOF",
 "description": "Read Wiktionary tethe page"
}
```


### [2026-09-05T18:28:18.404Z] TOOL RESULT

```
 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Ancient Greek 

 Toggle Ancient Greek subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Inflection 

 1.4.2 
 Coordinate terms 

 1.4.3 
 Derived terms 

 1.5 
 References 

 1.6 
 Further reading 

 Toggle the table of contents 

 τήθη 

 5 languages 

 Deutsch 
 Ελληνικά 
 Français 
 Kurdî 
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

 Ancient Greek
 [ edit ] 

 Alternative forms
 [ edit ] 

 τηθή ( tēthḗ ) 

 Etymology
 [ edit ] 

 From Proto-Indo-European *dʰeh₁dʰ- ( “ grandparent ” ) . Cognate with Proto-Slavic *dědъ ( “ grandfather ” ) , Lithuanian dė̃dė , dė̃dis ( “ uncle ” ) , and Latvian dȩ̀ds ( “ old man ” ) . [ 1 ] Probably originally an onomatopoeia of babies' speech.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /tɛ̌ː.tʰɛː/ → /ˈti.θi/ → /ˈti.θi/ 

 ( 5 th BCE Attic ) IPA ( key ) : /tɛ̌ː.tʰɛː/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈte̝.tʰe̝/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈti.θi/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈti.θi/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈti
```


## [2026-09-05T18:28:21.757Z] TOOL CALL #47: Bash

```json
{
 "command": "cd data/verification/sources/web && python3 - <<'EOF'\nt=open('61245d34e7c84c79.txt',encoding='utf-8').read()\ni=t.find('Noun\\n [ edit ]', t.find('Pronunciation'))\nprint(t[i:i+700])\nEOF",
 "description": "Read tethe noun senses"
}
```


### [2026-09-05T18:28:23.645Z] TOOL RESULT

```
Noun
 [ edit ] 

 τήθη • ( tḗthē )  f ( genitive τήθης ) ; first declension 

 grandmother 
 Synonym: μᾰ́μμη ( mắmmē ) 

 Inflection
 [ edit ] 

 First declension of ἡ τήθη ; τῆς τήθης ( Attic )

 Case / #

 Singular

 Dual

 Plural

 Nominative

 ἡ τήθη 
 hē tḗthē 

 τὼ τήθᾱ 
 tṑ tḗthā 

 αἱ τῆθαι 
 hai têthai 

 Genitive

 τῆς τήθης 
 tês tḗthēs 

 τοῖν τήθαιν 
 toîn tḗthain 

 τῶν τηθῶν 
 tôn tēthôn 

 Dative

 τῇ τήθῃ 
 tēî tḗthēi 

 τοῖν τήθαιν 
 toîn tḗthain 

 ταῖς τήθαις 
 taîs tḗthais 

 Accusative

 τὴν τήθην 
 tḕn tḗthēn 

 τὼ τήθᾱ 
 tṑ tḗthā 

 τᾱ̀ς τήθᾱς 
 tā̀s tḗthās 

 Vocative

 τήθη 
 tḗthē 

 τήθᾱ 
 tḗthā 

 τῆθαι 
 têthai 

 Notes:

 This table gives Attic inflectional end
```


## [2026-09-05T18:28:34.788Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT دده ===\"; grep -n \"دده\" BQT_v2_pages.txt BQT_v1_pages.txt 2>/dev/null | head -20; echo \"=== HRN dade ===\"; grep -n -i \"dâdä\\|dada\\|dade\" HRN.txt | head -6; echo \"=== HUB ===\"; grep -n -i \"dada\\|dade\" HUB.txt | head -6",
 "description": "Grep BQT, Horn, Hubschmann for dadeh"
}
```


### [2026-09-05T18:28:34.877Z] TOOL RESULT

```
=== BQT دده ===
BQT_v1_pages.txt:615:میشود منلادرزبان کردی مین از >و بباییددهات» میباشد . در لبجه‌های‌مختلف
BQT_v1_pages.txt:1424:نایینی ۰ [نار کی و یزدی ( که زرتشتیان یزدوچندده مجاور آن بدان
BQT_v1_pages.txt:1447:کلمات خوددهند . نمی بینی که‌اهل نیشابور گویند « برای‌اين > ومردم مرو
BQT_v1_pages.txt:1487:ودر نتیجه غلط‌های بیار وارد زبان فارسی گردده‌اینچنین:
BQT_v1_pages.txt:2447:تشر شبنم شاداب‌ظیمای تفرشی دده ۱۲
BQT_v1_pages.txt:5067:"قتار چهاددهم - در حرف شین‌نقطبه دار باحروف تهجی‌عبتنی
BQT_v1_pages.txt:5875:آب آ تش دده - کناب از اشك
BQT_v1_pages.txt:8415:نآ کج سکم رجوهادده با ۰۳
BQT_v1_pages.txt:12855:و رای بی نقطه بتحتانی رصدده و لام بالف کشیده
BQT_v1_pages.txt:13052:را باهم بيامیز ند وبدست بعالند تلدانه داله گُردده
BQT_v1_pages.txt:15005:م‌ ۲سدیج چش یم پسیدده 4
BQT_v1_pages.txt:15024:۰۷ د | , یه ده« |ردردم._ ندیه | دیدده
BQT_v1_pages.txt:15570:ددتشتی» بهودی( هريك يك نماینده) وادمنی (دوغماینده) دده‌جلیدورای‌ملی دارند . زبان رسمیو چون کل آن زرد و سفیدو کبود میباشدبنایر
BQT_v1_pages.txt:18174:بر ) و ددهسررزن سرایرد» ». شخصیرا
BQT_v1_pages.txt:19357:حم آمده است - و بروزن افیون کردا کرددهان
BQT_v1_pages.txt:20497:و تتالی بواو رسیده و بسچ بیط دیگی ژدده
BQT_v1_pages.txt:25187:خوانند - ویمعنی مر 3 هم مدده است وآن نوعی
BQT_v1_pages.txt:27358:پیر سالخودده- بسن پر دهفان
BQT_v1_pages.txt:28929:سمعتی رولدده باشد ۳۹
BQT_v1_pages.txt:30017:۱ فز فد2 ع بر وزن سمندده مرغکی‌است
=== HRN dade ===
4698:äväz däden 'rufen', ferämös daden 'vergessen' u. v. a. m.
4699:ap. l/^rfä-, adadä 'machen, setzen'; aw. [/'da-, dadaitl
11298:päz. vandadan,
11970:dadar 619.
17457:I vandadan 221.
=== HUB ===
4319:dadistdn 'Urtheil' = paz. dadastan. phi. datastan, arm. da-
4470:des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
4483:adada), zu dem np. dihis 'Gehen = np. dasan *Gabe, Geschenk'
4630:np.yaw/ *fiinf, zd. pandadasa 'fiinfzehn*; pOr *das vergangene
6733:phi. ebenso, arm. andadem priife' u. s. w. (§ 107, a);
7025:a) zu A: diham gebe* = zd. dadqmi^^di^. ipt. dadatuv
```


## [2026-09-05T18:28:35.782Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TTS dede/dada ===\"; grep -n -i \"dede\\|dada\" incoming/TTS/TTS_pages.txt | head -12",
 "description": "Grep Vambery for dede"
}
```


### [2026-09-05T18:28:35.851Z] TOOL RESULT

```
=== TTS dede/dada ===
8656:    osm.Ja2>maÄ;      = schliessen; Ja/^IÄ; = Pferdedecke; Jöfgan (von
```


## [2026-09-05T18:28:47.003Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"setzen, stellen, legen\\|dhē-mo\\|dhe-mo\\|famulus\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T18:28:47.058Z] TOOL RESULT

```
77596:2. dhe- „setzen, stellen, legen“.
77773:     lat.   famtdus ,, Diener", familia „Hausgenossenschaft", osk. famel „famulus",
```


## [2026-09-05T18:28:50.278Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '77590,77600p;77760,77790p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== page tags near ===\"; awk 'NR>=77400 && NR<=77800 && /\\[pdf page/' incoming/WLD/WLD_Bd1_pages.txt | tail -8",
 "description": "Read Walde-Pokorny dhe- and famulus lines"
}
```


### [2026-09-05T18:28:52.240Z] TOOL RESULT

```
„Tante“;       lit.   dilde       „Oheim“ (aber diedas „Greis“ aus                        wr. died ds.),            aksl.
dkh „GroBvater“               ;
                                   ahnlich     nhd.   deite,    teite       „Yater, Greis“,                russ.   djadja
„Oheim“,       s.     Delbriick Yerwandtschaftsn. 468, Berneker 191.


2. dhe- „setzen, stellen, legen“.
     Ai. dddhati, av. dadaiti „ersetzt“, ap. Impf.                           s.   sg.   adada,       ai.   Aor. adliam
„ich setzte",  med. s. sg. ddhita (= gr. s&ero)                         ;
                                                                            to-Ptc. ai. hita-h (-dhitd-h in
ved. Zs.) „gesetzt‘‘ (= lat. con-ditus, ab-ditas,                           cecditus, vgl.           auch gr. dezog

 ha (ei metr. Dehnung) „Grundlage, Grund"; da/id „in Haufen, scharen-
 weise;               haufig,   oft",     da/uiva          „haufig,    oft",   da/ihg,   dajueiai   PI.   „gehauft,
 haufig,              dicht gedrangt",               bduvog „Dickicht, Gebiisch, Strauch";                (so   auch
 aisl. dammr, nhd. Dumml s. u. *dheb- „dick“); aut ein *dhd-mo- „Nieder-
 lassung, Wohnstatte" (vgl. baipog     olxla, oeiogog, cpvTela lies., auch ai.
                                                                 *



 dhaman- „ Wohnstatte") oder „Haufe, Schar (der Diener)" bezieht man
 (s. Yf. LEWb. 2 270 m. Lit., Reichelt KZ. 46, 344) vielleicht mit Recht auch

     lat.   famtdus ,, Diener", familia „Hausgenossenschaft", osk. famel „famulus",
     bantin. famelo „familia“,    umbr. famefias „familia".
        5-stufig         gr. (ho yog
                            „Haufe, Schober" (vgl. zur Bed. skr. djenem sijeno
     „ich schobere              Heu
                                  phryg. dov/aog „avvodog, ovyxhjrog, ovyfikoaig“
                                         auf"),
     (Solmsen KZ. 34,53), got. doms „Urteil, Sinn" (dbmjan „urteilen“; aus dem
     Germ. russ. duma „Gedanke, Sorge; Ratsversammlung" usw., s. Berneker
     237), ags. dom „Meinung, Sinn, Urteil, Gericht", ahd. tuom „Urteil, Tat,
     Sitte, Zustand", lit. dom/:, domes ys „Aufmerksamkeit, Richten des Gedan-
     kens und Willens auf etwas" (usw., s. Trautmann GGA. 1911, 250, wo auch
     lit. deml „Lage, Zustand; ausgedachter Grund" usw., demetis     dometis „sich                  —
     merken, die Aufmerksamkeit worauf richten").
       Aisl. dcell „facilis“ (*dhe-li-s, Bugge PBrB. 21, 422); lit. pa-del ys „der
     Henne unterlegtes Ei", priedele, prtedelis „Beilage", abg. delo „Werk", (nicht
     zu lit. dailiis „zierlich, geschickt" usw.,                        s.   Berneker 194 f., Kcckel ZslPh. VI
67 ff.), wozu (s. Berneker 195 f., Trautmann BslWb. 48) aksl. del' a, dehmrt
=== page tags near ===
```


## [2026-09-05T18:29:02.212Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo ---; awk 'NR<77600 && /pdf page/{l=$0; n=NR} END{}' incoming/WLD/WLD_Bd1_pages.txt; python3 -c \"\nimport re\nlines=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split(chr(10))\nlast=None\nfor i,l in enumerate(lines[:77800]):\n    if 'pdf page' in l: last=(i+1,l.strip())\nprint(last)\n\"",
 "description": "Find page tag before famulus in WLD"
}
```


### [2026-09-05T18:29:03.975Z] TOOL RESULT

```
---
None
```


## [2026-09-05T18:29:09.876Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.index('2. dhe- „setzen, stellen, legen“')\nleaf=t[:i].count(chr(12))\nprint('leaf',leaf)\npages=t.split(chr(12))\nfor k in range(leaf-1,leaf+3):\n    nums=re.findall(r'(?m)^\\s*(8[0-9]{2})\\s*$', pages[k])\n    print(k,nums, re.findall(r'\\b8[2-3][0-9]\\b',pages[k])[:6])\n\"",
 "description": "Find WLD printed page for dhe-"
}
```


### [2026-09-05T18:29:11.487Z] TOOL RESULT

```
leaf 834
833 [] ['825']
834 [] []
835 [] ['827']
836 [] ['828']
```


## [2026-09-05T18:29:16.821Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.index('lat.   famtdus')\nprint('leaf',t[:i].count(chr(12)))\ni2=t.index('dkh „GroBvater“')\nprint('leaf 1.dhe',t[:i2].count(chr(12)))\n\"",
 "description": "WLD leaves for famulus and 1.dhe"
}
```


### [2026-09-05T18:29:18.612Z] TOOL RESULT

```
leaf 836
leaf 1.dhe 834
```


## [2026-09-05T18:29:24.764Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"FAMILY\\|Famil\" SKT.txt | head -5; echo ---; grep -n \"THESIS\\|Thesis\" SKT.txt | head -5; echo ---; grep -n -m3 \"^DEED\\|DEED,\" SKT.txt | head -5",
 "description": "Grep Skeat headwords"
}
```


### [2026-09-05T18:29:24.842Z] TOOL RESULT

```
6306:Family.  (F.-L.)  F  /Amilit.  -  L famiiia,  a  household.  — l^T^Mfs/ai;  a  aer vant.  O&cmn  /amt/\  &om  Oscan  ^^4Mi«i»  « hous.e.  Cf-  Skt.  dJtiiman,  a  house.  (^ DMA.)     Der^ami/i  ar  {L./amihsruy
---
13299:PARENTHESIS.
19573:Thesis:  see  Theme.
---
```


## [2026-09-05T18:29:34.312Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=t.index('Family.  (F.-L.)')\nleaf=t[:i].count(chr(12)); print('Family leaf',leaf,'=> printed p',leaf-20)\ni=t.index('Thesis:  see  Theme.')\nleaf=t[:i].count(chr(12)); print('Thesis leaf',leaf,'=> p',leaf-20)\n\"; echo \"=== KLN do/deed/fact/boutique/theme ===\"; grep -n \"^do,  intr\\|deed,  n\\.\\|fact,  n\\.\\|boutique\\|theme,  n\\.\\|thesis,  n\\.\" KLN_1966.txt | head",
 "description": "Skeat page numbers and Klein entries"
}
```


### [2026-09-05T18:29:36.336Z] TOOL RESULT

```
Family leaf 166 => printed p 146
Thesis leaf 531 => p 511
=== KLN do/deed/fact/boutique/theme ===
3009:antithesis,  n.  —  L.,  fr.  Gk.  dvxiftEm?,  ‘opposi¬ tion’,  lit.  ‘a  placing  against’,  fr.  dvxmfi^vat,,  ‘to set  one  thing  against  another,  to  oppose’,  fr. dvxi  (see  anti-)  and  xiOevoci,  'to  place’.  See
3152:apothecary,  n.  —  OF.  apotecarie  (F.  apothicaire ), fr.  ML.  apothecarius,  orig.  ‘storekeeper’,  fr. apotheca,  ‘storehouse’,  fr.  Gk.  Ajroff7)XT),  lit.  ‘a place  wherein  to  lay  up  a  thing’,  fr.  aromffevat, ‘to  put  away’,  fr.  atro  (see  apo-)  and  xiff£vai,  ‘to put,  place,  set  down’.  See  theme  and  -ary  and cp.  next  word  and  apothem.  Cp.  also  bodega, bottega,  boutique.
3547:artifact,  n.,  anything  made  by  human  art  (pale- ont.)  —  Compounded  of  L.  ars,  gen.  artis,  ‘art’, and  facere,  ‘to  make,  do’.  See  art  and  fact  and cp.  next  word.
5268:apothecary  and  cp.  bottega,  boutique, bodice,  n.  —  Prop.  pi.  of  body,  in  ‘pair  of  bodies’. —  For  formation  cp.  stays,  pence.
5415:botryo-,  before  a  vowel  botry-,  combining  form meaning  ‘cluster,  clusterlike'.  —  Gk.  poxpuo-, (3oxpu-,  fr.  (Mxpui;,  ‘a  cluster  of  grapes’,  of uncertain  origin.  Cp.  prec.  word, bottega,  n.,  shop,  workshop.  —  It.,  fr.  L.  apo- theca,  ‘storehouse  (esp.  of  wine)’,  fr.  Gk. a7ToSTfjxr),  ‘any  place  wherein  to  lay  up  some¬ thing;  magazine,  storehouse’.  See  apothecary and  cp.  bodega,  boutique, bottle,  n.  —  ME.  hotel,  fr.  OF.  ho  tele  (F.  bou- teille),  fr.  VL.  butticula,  dimin.  of  Late  L.  buttis. ‘cask’,  fr.  Gk.  mi-riv?],  ‘flask  covered  with  plaited osier’  (through  the  medium  of  Tarent.  poTtvr),  of s.m.).  Cp.  butt,  ‘barrel’,  butler.  For  the  change  of Gk.  7v  to  L.  b  cp.  ML.  buxida,  fr.  Gk.  7rj^tSa,  acc. of  TvShfc,,  ‘box’  (see  box,  ‘tree’,  and  box,  ‘re¬ ceptacle’).
5457:boutique,  n.,  a  shop.  —  F.,  fr.  OProven?.  botica (also  botiga),  fr.  Gk.  a7rofff]xi],  ‘any  place wherein  to  lay  up  something;  magazine,  store¬ house’,  whence  also  L.  apotheca.  See  apothecary and  cp.  bodega,  bottega.  The  vowel  i  (for  e)  is due  to  the  MGk.  pronunciation  of  t)  as  i. bouts-rimes,  n.  pi.,  rhyming  words  to  which  ver¬ ses  are  to  be  composed.  —  F.,  lit.  ‘rhyming ends’.  See  butt,  ‘the  thicker  end  of  anything’ and  rhyme.
8103:coelom,  n.,  the  body  cavity  of  Metazoa  (zool.)  — Coined  by  the  German  biologist  Ernst  Heinrich Haeckel  (1834-1919)  fr.  Gk.  xolXwfxa,  ‘a  hollow, cavity’,  fr.  xoiXoc,  ‘hollow’.  See  coelo-. Coelopleurum,  n.,  a  genus  of  plants.  —  ModL., compounded  of  Gk.  xoiXoc,  ‘hollow’,  and  rrXev- pov,  ‘rib’.  See  coelo-  and  pleura, coen-,  form  of  coeno-  before  a  vowel, coenesthesis.  coenaesthesis,  n.,  organic  sensation (in  contradistinction  to  external  sensation,  as hearing,  seeing,  etc.)  (psycho!.)  —  Fr.  Gk.  xoivr; ottolbjoic,  ‘common  sensation’.  See  coeno-  and esthesis.
10582:deductive,  adj.  —  L.  deductivus,  ‘derivative’,  fr. deductus,  pp.  of  deducere.  See  deduce  and  -ive. Derivative:  deductive-ly,  adv. deed,  n.  —  ME.  dede,  fr.  OE.  died,  rel.  to  OS.  dad, ON.  dad,  OFris.  dede,  ded,  Du.  daad,  OHG., MHG.  tat,  G.  Tat,  ‘deed,  act’,  Goth,  ga-defrs, ‘a  putting,  placing,  adoption’,  fr.  I.-E.  *dhe-ti-, whence  also  Lith.  delis,  ‘load,  burden’,  and  the second  element  in  OSlav.  blago-deti,  ‘good deed,  favor’;  cp,  I.-E.  *dhe-ti-,  whence  OI. -(d)hitih  (only  in  compounds),  ‘a  placing’,  Gk. •Seen;,  ‘a  placing,  setting’.  Late  L.  con-diti-o,  ‘a founding’  (fr.  L.  conditus,  pp.  of  condere).  I.-E. *dhe-ti-  and  *dhl-ti-  are  derivatives  of  base *dhe-,  *dhe-,  ‘to  put,  place;  to  do,  make’.  See do,  v.,  and  cp.  thesis.
11295:diathermic,  adj.,  diathermanous.  —  Formed  with suff.  -ic  fr.  Gk.  8tx.flEpp.og,  ‘thoroughly  warm’, fr.  dia-  and  Ssppr,,  ‘heat’.  See  therm, diathermy,  n.,  application  of  heat  in  the  tissues of  the  body  by  means  of  high-frequency  electric currents.  —  Medical  L.  diathermia,  coined  by Nagelschmidt  in  1908  fr.  dia-  and  -thermy. diathesis,  n.,  bodily  constitution  which  makes  sus¬ ceptible  to  disease  (med)  —  Medical  L.,  fr.  Gk. SiASfetrig,  ‘a  placing  in  order,  arrangement,  dis¬ position,  physical  condition’,  fr.  8ixti{>evxi,  ‘to place  separately,  arrange,  manage’,  fr.  Six  (see dia-)  and  ti9evxi,  ‘to  put,  place’.  See  theme  and cp.  thesis  and  words  there  referred  to. diatom,  n.,  any  of  microscopic  unicellular  algae
13333:epenthesis,  n.,  insertion  of  a  letter  or  a  syllable in  a  word  ( gramm .)  —  Late  L.,  fr.  Gk.  tnbv- beou;,  ‘insertion’,  fr.  invrn&txai,  ‘to  insert’, fr.  £7t(  (see  epi-)  and  £vtiS-£vixi,  ‘to  put  in’,  fr. 4v  (see  2nd  en-)  and  xifiivai,  ‘to  put,  place’. See  theme  and  cp.  thesis  and  words  there  re¬ ferred  to.
```


## [2026-09-05T18:29:46.475Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"parenthesis,  n\\.\" KLN_1966.txt | head -2; echo ---; grep -n \"theme,  n\\.\" KLN_1966.txt | head -2; echo ---; grep -n \"^fact,  n\\.\\|  fact,  n\\.\" KLN_1966.txt | head -2; echo ---; grep -n \"office,  n\\.\" KLN_1966.txt | head -2",
 "description": "Grep Klein for parenthesis, theme, fact, office"
}
```


### [2026-09-05T18:29:46.585Z] TOOL RESULT

```
27395:Derivative:  parenteral-ly,  adv. parenthesis,  n.,  word,  clause  etc.  inserted  into  a sentence.  —  ML.,  fr.  Gk.  Trapevffeai?,  ‘inser¬ tion’,  lit.  ‘a  putting  in  beside’,  fr.  napEm-Uevat, ‘to  put  in  beside’,  fr.  reapa,  ‘beside’,  ev,  ‘in’,  and Tiffsvai,  ‘to  put,  place’.  See  para-,  ‘beside’,  2nd en-  and  thesis.
---
38914:theme,  n.  —  ME.  teme,  fr.  OF.  tesme  (F.  theme), fr.  L.  thema,  fr.  Gk.  gen.  ff£p.axo?,  ‘that
---
14278:fact,  n.  —  L.  factum,  ‘deed,  act’,  lit.  ‘something done’,  neut.  pp.  of  facere,  ‘to  make,  do;  to  per¬ form,  accomplish;  to  act’,  fr.  I.-E.  base  *dhd-, *dhe-,  *dh1-,  ‘to  put,  place;  to  do,  make,  con¬ struct’.  See  do  and  theme  and  cp.  words  there referred  to.  Cp.  also  feat  (which  is  a  doublet  of fact)  and  the  words  facade,  facient,  facile,  facili¬ tate,  facility,  facinorous,  facsimile,  faction,  -fac¬ tion,  factor,  factory,  factotum,  factual,  affair, affect,  affettuoso,  artifact,  artifice,  benefaction, benefactor,  benefice,  benefit,  calefacient,  comfit, confect,  confection,  counterfeit,  defaced,  defeat, defect,  deficient,  deficit,  deific,  difficult,  dis¬ comfit,  dolce  far  niente,  efface,  effect,  efficacious, efficient,  face,  fashion,  feasance,  feasible,  fea¬ ture,  fecit,  feckless,  fetish,  -fy,  infect,  labe¬ faction,  magnificent,  malefic,  maleficence,  mal¬ feasance,  manufacture,  misfeasance,  munificent, office,  orifice,  perfect,  pontiff,  prefect,  proficient, refection,  rifacimento,  satisfaction,  savoir-faire, somnifacient,  Spinifex,  suffice,  sufficient,  super¬ ficial,  surface,  surfeit.
---
26133:Derivative:  offertori-al,  adj. office,  n.  —  ME.,  fr.  OF.  (=  F.),  fr.  L.  officium, ‘service’  (in  Eccles.  L.,  ‘church  service’),  which stands  for  *opi-faciom,  lit.  ‘work-doing’,  fr.
```


## [2026-09-05T18:29:58.154Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%A8%D9%88%D8%AA%DB%8C%DA%A9/\" \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/\" \"https://abadis.ir/fatofa/%D8%AA%D8%B2/\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 125, root Dhe 2, Persian node: French loans butik/parantez/tez in Mo'in-Dehkhoda\"; done",
 "description": "Archive abadis pages for Persian loans"
}
```


### [2026-09-05T18:30:03.749Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/be59d6b1f4bd902a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/009343e3dc6e44d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48cb103e25f59aec.txt
```


## [2026-09-05T18:30:07.689Z] TOOL CALL #59: Bash

```json
{
 "command": "cd data/verification/sources/web && for f in be59d6b1f4bd902a 009343e3dc6e44d5 48cb103e25f59aec; do echo \"=== $f ===\"; head -c 60 $f.txt; grep -o \"فرهنگ معین[^|]\\{0,200\\}\" $f.txt | head -3; grep -o \"\\[ فر[^]]*\\]\" $f.txt | head -3; grep -o \"فر\\. [^ ]\\{0,20\\}\" $f.txt | head -3; done",
 "description": "Inspect abadis archived pages"
}
```


### [2026-09-05T18:30:09.405Z] TOOL RESULT

```
=== be59d6b1f4bd902a ===
URL: https://abadis.ir/fatofa/%D8%A8%D9%88%D8%AA%DB%8C%DA%A9فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها
[ فر. ]
فر. ]
=== 009343e3dc6e44d5 ===
URL: https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AAفرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها
[ فر. ]
فر. ]
=== 48cb103e25f59aec ===
URL: https://abadis.ir/fatofa/%D8%AA%D8%B2/
FETCHED: 2026-09فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها
[ فر. ]
فر. ]
```


## [2026-09-05T18:30:12.297Z] TOOL CALL #60: Bash

```json
{
 "command": "cd data/verification/sources/web && for f in be59d6b1f4bd902a 009343e3dc6e44d5 48cb103e25f59aec; do echo \"=== $f ===\"; grep -o \".\\{80\\}\\[ فر\\. \\].\\{0,160\\}\" $f.txt | head -2; done",
 "description": "Extract Moin entries with French tag"
}
```


### [2026-09-05T18:30:13.927Z] TOOL RESULT

```
=== be59d6b1f4bd902a ===
=== 009343e3dc6e44d5 ===
=== 48cb103e25f59aec ===
```


## [2026-09-05T18:30:17.225Z] TOOL CALL #61: Bash

```json
{
 "command": "cd data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f in ['be59d6b1f4bd902a','009343e3dc6e44d5','48cb103e25f59aec']:\n    t=open(f+'.txt',encoding='utf-8').read()\n    print('===',f)\n    for m in re.finditer(r'\\[ ?فر\\.', t):\n        print(repr(t[max(0,m.start()-120):m.start()+200]))\n        print('---')\nEOF",
 "description": "Show context around French origin tag"
}
```


### [2026-09-05T18:30:18.775Z] TOOL RESULT

```
=== be59d6b1f4bd902a
'ترادف بوتیک : دکان، لوکس فروشی، مغازه\n برابر پارسی : دکان، بابکد\n معنی انگلیسی : boutique \n\n دنبال کنید \n\n فرهنگ معین\n\n [ فر. ] (اِ. ) مغازه ای که در آن لباس ، کفش ، عطر و مانند آن فروخته می شود. \n\n دانشنامه عمومی\n\n بوتیک ( به فرانسوی: Boutique ) یک فروشگاه است که در آن پوشاک، کفش، عطر و مانند آن فروخته می شود. [ ۱] در'
---
=== 009343e3dc6e44d5
'ب از نیم قوس عمودی بدان شکل ( ) و آن برای نوشتن جمل. معترضه و مانند آن بکار رود قوسین هلالین . \n\n فرهنگ معین\n\n (پَ تِ ) [ فر. ] (اِ. ) نشانه ای است قوسی شکل ( ) که برای نوشتن جملة معترضه و مانند آن به کار رود، هلال ، قوس ، کمان . (فره ) . \n\n فرهنگ عمید\n\n علامتی به شکل ( ) که در دو طرف کلمه، جملۀ معترضه، یا عبارت های ری'
---
=== 48cb103e25f59aec
'ده ای به اندازة گنجشک که آوازی خوش دارد، صعوه .\n (تَ ) (اِ. ) داندانة کلید، پره کلید.\n ( ~. ) (ص . ) تاس ، کچل .\n (تِ ) [ فر. ] (اِ. ) پایان نامه ، رساله ای که دانشجو پس از به پایان رساندن تحصیلات در رشتة تحصیلی خود می نویسد. \n\n فرهنگ عمید\n\n پرنده ای کوچک و خوش آواز شبیه گنجشک، صعوه: چون لطیف آید به گاه نوبهار / بانگ ر'
---
```


## [2026-09-05T18:30:28.019Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%AA%D9%85/\" --note \"pdf page 125, root Dhe 2, Persian tem 'theme' French loan\" && cd data/verification/sources/web && python3 - <<'EOF'\nimport re,hashlib\nh=hashlib.sha1(\"https://abadis.ir/fatofa/%D8%AA%D9%85/\".encode()).hexdigest()[:16]\nt=open(h+'.txt',encoding='utf-8').read()\nprint(h)\nfor m in re.finditer(r'\\[ ?فر\\.', t):\n    print(repr(t[max(0,m.start()-150):m.start()+200])); print('---')\nEOF",
 "description": "Fetch and inspect abadis tem entry"
}
```


### [2026-09-05T18:30:31.102Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4513ce285952339e.txt
4513ce285952339e
'اری آب مروارید، موضوع، بحث، ماده، مایه، موضوع انشائ، موسیقی\n( اسم ) ۱- موضوع اساسیمیایه. ۲- زمینه .\nو بکسر فصیح تر است . تمام . \n\n فرهنگ معین\n\n (تِ ) [ فر. ] (اِ. ) ۱ - موضوع اساسی ، مایه . ۲ - زمینه .\n (تَ ) [ په . ] (اِ. ) ۱ - تیرگی چشم ، بیماری ای که باعث نابینایی و کمی دید می شود. ۲ - تاریکی ، سیاهی . \n\n فرهنگ عمید\n\n ۱. (ادبی ) موضوع، مبحث.\n۲. '
---
```


## [2026-09-05T18:30:44.435Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg125_900.png')\nim.crop((1190*3,480*3,1470*3,690*3)).resize((840*2,630)).save('p125_french.png')\n\"",
 "description": "Crop French box at high res"
}
```


### [2026-09-05T18:30:47.171Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:30:49.319Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p125_french.png"
}
```


### [2026-09-05T18:30:49.339Z] TOOL RESULT

```

```


## [2026-09-05T18:31:02.051Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.index('dhé-¹, To set, put') if 'dhé-¹, To set, put' in t else t.index('To set, put. Contracted')\nprint('leaf',t[:i].count(chr(12)))\n\"; mkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg125.png ocr/BOOK/125.png && ls -la ocr/BOOK/ | tail -3",
 "description": "Find AHD leaf and copy page PNG"
}
```


### [2026-09-05T18:31:03.887Z] TOOL RESULT

```
leaf 42
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T18:31:06.549Z] TOOL CALL #66: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/125.png && cat /home/sfmqrb/git/rishe/tools/verify_check.py | head -60",
 "description": "Confirm PNG copied and inspect verify_check"
}
```


### [2026-09-05T18:31:06.604Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/125.png
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
```


## [2026-09-05T18:31:08.965Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '60,130p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-05T18:31:09.015Z] TOOL RESULT

```
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


## [2026-09-05T18:31:13.170Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-126.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Inspect page-126 verification style"
}
```


### [2026-09-05T18:31:14.912Z] TOOL RESULT

```
{"pdf_page": 126, "book_page": 96, "verified_by": "claude-fable-5-1", "verified_on": "2026-09-04"}
{
 "entry": 0,
 "root": "Dheigh, Dhigha",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'",
 "note": "Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.",
 "note_fa": "ریشه همان *dʰeyǵʰ- هندواروپایی آغازین است به معنی «سرشتن گِل، ورز دادن و از آن دیوار ساختن»، و صورت اسمیِ درجهٔ o یعنی *dʰóyǵʰos «آنچه سرشته شده» که هم «دیوار» و هم «خمیر» از آن آمده است؛ پوکورنی (ص ۲۴۴) عیناً همین را می‌گوید و AHD نیز dheigh- «شکل دادن، ساختن» را با ارجاع به پوکورنی می‌آورد. نگارش دومِ نورایی، «Dhigha»، صورت درجه‌صفرِ همان ریشه است (پوکورنی: dhiĝh-lo-s). پس جعبهٔ ریشه و معنای آن درست است. اما دو شاخهٔ نمودار سست است: شاخهٔ «daika > دیگ» را ریشه‌شناسیِ ایرانیِ امروزی رد می‌کند (گره‌های ۱۱ و ۱۲) و آن را از *daiH- «تابیدن، سوختن» می‌گیرد؛ و گره‌های سغدی و «دژ» و «فردوس» هم‌ریشه یا وام‌واژهٔ رفت‌وبرگشتی‌اند نه فرزندِ مستقیمِ پدری که نمودار برایشان کشیده است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos",
  "https://www.thefreedictionary.com/_/roots.aspx?type=Indo-European&root=dheigh-",
  "https://www.etymonline.com/word/*dheigh-",
  "https://starlingdb.org/cgi-bin/etymology.cgi?root=config&basename=%2Fdata%2Fie%2Fpokorny&text_recno=1208&single=1"
 ],
 "ref_check": [
  {
   "ref": "POK:244",
   "status": "supports",
   "note": "POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... 'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (
{
 "id": 1,
 "lang": "Old Persian",
 "words": "didâ, děğa-vâra",
 "verdict": "disputed",
 "derivation": "OP didā- f. 'wall, fortress' is genuinely attested: DSf (Darius' Susa foundation charter) line 54 'tyaiy didām apiθa' — 'the men who adorned the wall were Medes and Egyptians' (Kent's Lexicon p. 191, which is Nourai's KNT:191). It is the regular SW-Iranian reflex of PIr *daizah < PIE *dʰóyǵʰos: Proto-Iranian *ǰ (< PIE *ǵʰ) gives Old Persian d where Avestan/Median give z (cf. Av. daēza-), and the reduplicated-looking di-dā- shows the OP treatment (Asatrian 2017, 'SWIran. *didā- fortress, walled residence'). The second word is not an attested OP word but Horn's/Hübschmann's reconstruction of the ancestor of dīvār, i.e. *daiza-vāra- 'wall-enclosure' (HRN:133); the JSON form 'děğa-vâra' with ě and ğ is almost certainly a scan misreading of the book's 'dēza-vâra' or 'daiza-vâra' (Nourai writes ž, not ğ, for the sound elsewhere on this page: dež). Modern reconstruction (Wiktionary, after Asatrian and Rastorgueva-Edelman) is OP didā- + *-wāra-, giving MP dēwār. Checked against the scan (data/verification/sources/refs/ocr/BOOK/126.png): the book prints 'didâ, děğa-vâra' with both breves exactly as the dataset has it, so the guess of a scan misreading of 'dēza-/daiza-vâra' above is wrong — 'děğa-' is Nourai's own transliteration of Horn's ap. *deghavāra- (HRN:133) and the extraction is faithful; what remains against the node is not a transcription error but the fact that *deghavāra- is Horn's reconstruction, rejected by Hübschmann/Nyberg in favour of *didā-vāra-. Reclassified after checking the scan: the book itself prints \"děğa-vâra\", so this is not a transcription problem but Nourai's rendering of Horn's reconstruction *deghavāra-, which Hübschmann and Nyberg reject in favour of *didā-vāra-; didā itself is attested and correct.",
 "derivation_fa": "didā- پارسی باستان «دیوار، دژ» واژه‌ای گواهی‌شده است: در منشور بنیادگذاریِ کاخ شوش (DSf، سطر ۵۴) عبارت «tyaiy didām apiθa» آمده و کنت آن را در واژه‌نامهٔ خود (ص ۱۹۱) ثبت کرده است. این صورت بازتاب قاعده‌مندِ جنوب‌غربیِ ایرانی باستانِ *daizah < *dʰóyǵʰos است: *ǰ ایرانیِ آغازین (< *ǵʰ هندواروپایی) در پارسی باستان d می‌شود، حال آنکه در اوستایی و مادی z می‌دهد (اوستایی daēza-). اما واژهٔ دوم گواهی‌شده نیست: *daiza-vāra- بازسازیِ هرن و هوبشمان برای نیای «دیوار» است. بررسی تصویر صفحه نشان می‌دهد که کتاب خود «didâ, děğa-vâra» را با همان دو نشانهٔ کوتاه چاپ کرده است، پس خطای خوانشِ اسکن در کار نیست و صورت عجیب از آنِ خودِ
```


## [2026-09-05T18:31:20.551Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دده\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY latin dhe ===\"; grep -n \"DHE\\|dhē-\\|DHĒ\" incoming/ARY/ARY_latin_index_pages.txt | head -8",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T18:31:20.619Z] TOOL RESULT

```
=== ARY latin dhe ===
1253:eh oh ey Stl 52 can Cal 98S yy. 9 gos y9 DHEIGH oly} y ua: Sa dle
2634:5" 4 SGU) 2519 Saag phe *NDHOS  *NDHERE 54h 2'y b a zrly gpl
7656:MALLORY & ADAMS 7 DHEN BARNHART:
7662:*DHE, “DHENA, “DHEDHN., *DHELU, *DHEI- (INDO-EUROPEAN) igtlysl 9 ie
7994:(DOUGH) 180, (DHEIGH) 753 (OLD ENGLISH) 9S efit
8380:MALLORY & ADAMS: DHEU TOU .
8486:INDHE, IN-DE :(OLD IRISH) 4S 543 p! AYER SPANISH) giles!
8750:DELAMARRE: (LIBRE) 226 LODHENN
```


## [2026-09-05T18:31:25.579Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7650,7670p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== page tag ===\"; awk 'NR<=7662 && /pdf page/{p=$0} END{print p}' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "ARY context around DHE"
}
```


### [2026-09-05T18:31:27.316Z] TOOL RESULT

```
DAGG (QUX(SHEDISH) 54 yo FINTINA ARUMANIAN) gly,
DAUW DUTCH) «gle FONTE PORTUGUESE) Ji
[pdf page 265]
eh Le
SKEAT: ‘REFERENCES beth
HEY) 75, DEM 167 POKORNY
MALLORY & ADAMS 7 DHEN BARNHART:
a seas aabicl (FOUNTAL) 404, (DEW) 273
ONIONS: (DEW) 263
: eatloak
hatte (ah A gslagy GUd;) OT 5I tl slabs 9 oY Obj 22 Ss tl o>
eet ei gend slab 22 ao ctl er
*DHE, “DHENA, “DHEDHN., *DHELU, *DHEI- (INDO-EUROPEAN) igtlysl 9 ie
DOJITI DAENO., DAENU-  :(AVESTAN) 3!
DENAID (LITHUANIAN) 3-3 DAYAK, DAYAG — (PAHLAVI) 5 shy
DEJU LATVIAN) (3) 5 DAIN, DAYUN AOSSETIC) sn 3}
DADAN (OLD PRUSSIAN) oS 3.4 DAIN, DAYE, DAE (KURDISH) 62,
DYNU WELSH) 59 DAL (BALUCHI) > sh
DENAFF XBRETON) 334 DAYI 4AFGHAND) (54) lait
DJATHE ALBANIAN) gisT DHA. DHATRI (SANSKRIT) <2 Sse
DAYEAK ARMENIAN) gs)!
=== page tag ===
[pdf page 265]
```


## [2026-09-05T18:32:28.270Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"dhedh\\|Lallwort\\|grandparent\" AHD_watkins1985.txt | head -5; echo \"=== KLN pages ===\"; python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split(chr(12))\ndef leafof(s):\n    return t[:t.index(s)].count(chr(12))\nfor s in ['boutique,  n.,  a  shop','parenthesis,  n.,  word,  clause','theme,  n.  —  ME.  teme','fact,  n.  —  L.  factum','office,  n.  —  ME.,  fr.  OF.','deed,  n.  —  ME.  dede']:\n    L=leafof(s)\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', pages[L]) or re.findall(r'(?m)^\\s*(\\d{3})\\s*$', pages[L-1])\n    print(s[:22],'leaf',L,'pagenums seen',nums, re.findall(r'(?m)^\\s*(\\d{3})\\s*$', pages[L+1]))\n\"",
 "description": "AHD dhedh check and Klein page numbers"
}
```


### [2026-09-05T18:32:30.372Z] TOOL RESULT

```
=== KLN pages ===
boutique,  n.,  a  sho leaf 112 pagenums seen ['193'] ['194', '195']
parenthesis,  n.,  wor leaf 603 pagenums seen [] []
theme,  n.  —  ME.  te leaf 848 pagenums seen [] []
fact,  n.  —  L.  fact leaf 309 pagenums seen ['570', '571'] []
office,  n.  —  ME.,   leaf 576 pagenums seen [] []
deed,  n.  —  ME.  ded leaf 227 pagenums seen ['410', '411'] ['414', '415']
```


## [2026-09-05T18:32:40.794Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split(chr(12))\ni=t.index('dhēiô dhēmi (2)')\nL=t[:i].count(chr(12)); print('leaf',L, re.findall(r'(?m)^\\s*(\\d{3})\\s*$',pages[L]))\n\"",
 "description": "IEC page for dhemi"
}
```


### [2026-09-05T18:32:42.402Z] TOOL RESULT

```
leaf 113 ['181', '182']
```


## [2026-09-05T18:39:11.643Z] TOOL CALL #73: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-\"\nW_FAM   = \"https://en.wiktionary.org/wiki/famulus\"\nW_DADEH = \"https://en.wiktionary.org/wiki/%D8%AF%D8%AF%D9%87\"\nW_TETHE = \"https://en.wiktionary.org/wiki/%CF%84%CE%AE%CE%B8%CE%B7\"\nE_BOUT  = \"https://www.etymonline.com/word/boutique\"\nE_FAM   = \"https://www.etymonline.com/word/family\"\nA_BUTIK = \"https://abadis.ir/fatofa/%D8%A8%D9%88%D8%AA%DB%8C%DA%A9/\"\nA_PAR   = \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/\"\nA_TEZ   = \"https://abadis.ir/fatofa/%D8%AA%D8%B2/\"\nA_TEM   = \"https://abadis.ir/fatofa/%D8%AA%D9%85/\"\n\nPOK_NOTE = (\"POK_01.txt leaves 246-247 (the printed page number 235 stands on leaf 246, 236 on leaf 247): \"\n            \"\\\"2. dhē- ,setzen, stellen, legen'; Nominalbildungen: -dhē-, dh-i-, -dh-o-; ... dhē-men-, dhē-mi-, \"\n            \"dho-mi-, dhō-mo-, dho-mo-; ... Ai. dádhāti, av. daδāiti ,er setzt' ... gr. τίθημι ,setze' ... \"\n            \"Mit einer k-Erw. lat. faciō, -ere, fēcī ... facilis ,(tunlich) leicht' ... faciēs ,Aussehen, \"\n            \"Erscheinung, Antlitz' ... ahd. tōm, tuom, as. tōn, ags. dōn ,tun'\\\" — Nourai's page number is exact.\")\n\nAHD_NOTE = (\"AHD_watkins1985.txt leaf 42: \\\"dhē-¹. To set, put. Contracted from *dheə-. 1. O-grade form *dhō- in \"\n            \"Germanic *dōn in Old English dōn, to do: DO¹ ... 2. Suffixed form *dhē-ti-, 'thing laid down or done, \"\n            \"law, deed' ... Old English dēd ... 6. Suffixed zero-grade form *dhə-k- in: a. Latin facere ... b. Latin \"\n            \"derivative faciēs, shape, face ... c. Latin compound officium (< *opi-fici-om) ... d. Latin facilis ... \"\n            \"FACILE, (FACILITY), FACULTY; DIFFICULTY. 9. Reduplicated form *dhi-dhē- in Greek tithenai, to put: \"\n            \"THESIS ... APOTHECARY, ... BODEGA, BOUTIQUE, ... PARENTHESIS ... 11. Suffixed zero-grade form *dhə-mn̥ \"\n            \"in Greek thema, 'thing placed', proposition: (THEMATIC), THEME. [Pok. 2. dhé- 235.]\\\" — every branch \"\n            \"Nourai draws is in this one AHD entry. The 1975 New College page 1512 cannot be checked directly \"\n            \"(that printing is lending-only); the local copy is the 1985 standalone reprint of the same appendix.\")\n\nWLD_NOTE = (\"incoming/WLD/WLD_Bd1_pages.txt leaf 834 = WP I 826: \\\"2. dhē- ,setzen, stellen, legen'. Ai. dádhāti, \"\n            \"av. dadāiti ... to-Ptc. ai. hitá-ḥ ... (= lat. con-ditus, ab-ditus, creditus)\\\" — same root, same gloss \"\n            \"as Nourai's root box.\")\n\n\ndef entry0():\n    nodes = []\n\n    nodes.append({\n        \"id\": 1, \"lang\": \"Greek\",\n        \"words\": \"tithenai; apo-tithenai; para-en-tithenai; thěma\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"Greek τιθέναι (1 sg. τίθημι) 'to put, place' is the reduplicated athematic present *dʰi-dʰeh₁-mi of \"\n            \"PIE *dʰeh₁-, the exact formal match of Sanskrit dádhāti and Avestan daδāiti; Greek θ is the regular \"\n            \"reflex of aspirated *dʰ. ἀποτιθέναι 'to put away' (ἀπό 'away' + τιθέναι) is real, but the sense 'store' \"\n            \"that Nourai attaches to it belongs to its derived noun ἀποθήκη 'place where things are put away, \"\n            \"storehouse', which is the form that actually travelled into Latin apotheca and thence to botica/\"\n            \"boutique/bodega. 'para-en-tithenai' is Nourai's morpheme-by-morpheme spelling of attested παρεντιθέναι \"\n            \"'to put in beside' (παρά + ἐν + τιθέναι), whose verbal noun παρένθεσις gives parenthesis. θέμα \"\n            \"(gen. θέματος) 'thing placed, proposition' is *dʰh₁-mn̥, exactly Nourai's 'thing placed'.\"),\n        \"derivation_fa\": (\n            \"فعل یونانی τιθέναι/τίθημι «نهادن، گذاشتن» صورت حالِ مضاعف‌شدهٔ *dʰi-dʰeh₁-mi از ریشهٔ هندواروپایی آغازین \"\n            \"*dʰeh₁- است و همتای دقیقِ dádhāti سنسکریت و daδāiti اوستایی است؛ θ یونانی بازتاب قاعده‌مندِ *dʰ دمیدهٔ \"\n            \"هندواروپایی است. ἀποτιθέναι «کنار نهادن» درست است، اما معنای «انبار کردن» که نورایی به آن داده در حقیقت \"\n            \"از اسمِ مشتقِ آن ἀποθήκη «انبار» می‌آید و همین صورت است که به لاتینی apotheca و سپس به botica/boutique \"\n            \"راه یافته است. صورتِ «para-en-tithenai» نگارشِ تکواژبه‌تکواژِ نورایی از παρεντιθέναι است که اسمِ آن \"\n            \"παρένθεσις ریشهٔ parenthesis است. θέμα «آنچه نهاده شده» نیز از *dʰh₁-mn̥ است. ادعای نورایی درست است.\"),\n        \"sources\": [W_PIE, E_BOUT],\n        \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_NOTE}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 235-236 (POK_01.txt leaf 247)\", \"stance\": \"supports\",\n             \"note\": \"\\\"gr. τίθημι ,setze' (Aor. ἔθηκα ... Partiz. θετός)\\\"; and on the following leaf \\\"Dieselbe k-Erw. außer in gr. ἔθηκα auch in θήκη ,Behältnis'\\\" — the ἀποθήκη family.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 603 (~p. 1182) s.v. parenthesis; leaf 112 (p. 193) s.v. boutique; leaf 848 (~p. 1672) s.v. theme\", \"stance\": \"supports\",\n             \"note\": \"\\\"parenthesis, n. ... fr. Gk. παρένθεσις, 'insertion', lit. 'a putting in beside', fr. παρεντιθέναι, 'to put in beside', fr. παρά, 'beside', ἐν, 'in', and τιθέναι, 'to put, place'\\\"; \\\"apothecary ... fr. Gk. ἀποθήκη, lit. 'a place wherein to lay up a thing', fr. ἀποτιθέναι, 'to put away'\\\".\"},\n            {\"src\": \"IEC\", \"where\": \"p. 181-182 (leaf 113) s.v. dhēiō, dhēmi (2)\", \"stance\": \"supports\",\n             \"note\": \"\\\"dhēiô dhēmi (2) 'put, lay'. Cf. dhídhemi, dhesnos, dhetis, dhētos, etc. WP I, 827-829\\\" — Mann derives the Greek reduplicated present from the same root.\"}]\n    })\n\n    nodes.append({\n        \"id\": 2, \"lang\": \"French\",\n        \"words\": \"botica; paranthese, these, theme\",\n        \"verdict\": \"transcription_suspect\",\n        \"error_in\": \"book\",\n        \"book_prints\": \"botica : gift store / paranthese, these, theme\",\n        \"correct_form\": \"boutique (< Old Provençal botica) ; parenthèse, thèse, thème\",\n        \"derivation\": (\n            \"The route is right but two of the four forms as printed are not French. (a) botica is Old Provençal, \"\n            \"not French: Klein s.v. boutique, 'F., fr. OProvenç. botica (also botiga), fr. Gk. ἀποθήκη ... The vowel \"\n            \"i (for e) is due to the MGk. pronunciation of η as i'; Etymonline the same ('from French boutique \"\n            \"(14c.), from Old Provençal botica, from Latin apotheca'). Latin apotheca inherited directly into French \"\n            \"would have given *avouaie, which is why the word had to come north from Provence in the 14th c. Its \"\n            \"sense is 'shop, storehouse', never 'gift store'. (b) 'paranthese' is not a French word; French has \"\n            \"parenthèse (ML. parenthesis < Gk. παρένθεσις). The 900-dpi scan of the printed page (copy at \"\n            \"data/verification/sources/refs/ocr/BOOK/125.png) shows 'paranthese' with an a, so the extraction is \"\n            \"faithful and the misprint is Nourai's own; the a is probably back-formed from the Persian pronunciation \"\n            \"parântez. (c) 'these, theme' are the book's unaccented renderings of French thèse and thème, both \"\n            \"regular learned borrowings of L. thesis/thema < Gk. θέσις/θέμα.\"),\n        \"derivation_fa\": (\n            \"مسیر وام‌گیری درست است اما دو صورت از چهار صورتِ چاپ‌شده فرانسوی نیستند. نخست، botica واژه‌ای پرووانسالیِ \"\n            \"کهن است نه فرانسوی: کلاین در مدخل boutique می‌نویسد «فرانسوی، از پرووانسالیِ کهن botica، از یونانی \"\n            \"ἀποθήκη»؛ اتیمانلاین نیز همین را می‌گوید. اگر apotheca لاتینی به‌طور موروثی در فرانسوی می‌ماند *avouaie \"\n            \"می‌شد، پس واژه در سدهٔ چهاردهم از جنوب (پرووانس) به فرانسه رفته است، و معنای آن «دکان، انبار» است نه \"\n            \"«فروشگاه هدیه». دوم، «paranthese» واژهٔ فرانسوی نیست؛ فرانسوی parenthèse دارد. تصویرِ صفحهٔ چاپی نشان \"\n            \"می‌دهد که خودِ کتاب «paranthese» را با a چاپ کرده است، پس خطای خوانشِ اسکن نیست بلکه غلطِ چاپیِ کتاب است \"\n            \"و احتمالاً از تلفظِ فارسیِ «پرانتز» ساخته شده. سوم، these و theme همان thèse و thème فرانسوی‌اند بدون \"\n            \"علامت‌های زبر و زیر.\"),\n        \"sources\": [E_BOUT],\n        \"ref_check\": [{\"ref\": \"AHD:156,1334\", \"status\": \"partial\",\n                       \"note\": \"The content is right — Watkins' dhē-¹ entry (AHD_watkins1985.txt leaf 42) lists BOUTIQUE and BODEGA under §9 (Greek tithenai > apothēkē) and THEME under §11 — but the 1975 New College main-dictionary pages 156 and 1334 cannot be opened (that printing is lending-only on archive.org), and the AHD entry for boutique itself gives Old Provençal botica, not a French botica.\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 112 = p. 193 s.v. boutique (and leaf 112 s.v. bottega, leaf 111 bodega)\", \"stance\": \"partial\",\n             \"note\": \"\\\"boutique, n., a shop. — F., fr. OProvenç. botica (also botiga), fr. Gk. ἀποθήκη, 'any place wherein to lay up something; magazine, storehouse', whence also L. apotheca. See apothecary and cp. bodega, bottega.\\\" — botica is Old Provençal in Klein, not French.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 42, dhē-¹ §9\", \"stance\": \"supports\",\n             \"note\": \"\\\"9. Reduplicated form *dhi-dhē- in Greek tithenai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, ... BODEGA, BOUTIQUE, ... PARENTHESIS ...\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 (≈ p. 511) s.v. Thesis\", \"stance\": \"supports\",\n             \"note\": \"\\\"Thesis: see Theme.\\\" — Skeat groups thesis/theme under the same Greek τίθημι family.\"}]\n    })\n\n    nodes.append({\n        \"id\": 3, \"lang\": \"Persian\",\n        \"words\": \"bŭtîk «بوتیک»; parântez «پرانتز»; tem, tez «تیم ، تز»\",\n        \"verdict\": \"transcription_suspect\",\n        \"error_in\": \"extraction\",\n        \"book_prints\": \"تِم ، تِز\",\n        \"correct_form\": \"تِم ، تِز\",\n        \"derivation\": (\n            \"All three are 20th-century French loans in Persian, so the arrow French → Persian is right; but the \"\n            \"JSON's Persian script for the third line is wrong. The 900-dpi render of the printed page shows «تِم ، \"\n            \"تِز» — tā with a kasra, then mīm — while the extraction reads the kasra as a yā and gives «تیم» (tīm), \"\n            \"which is a different word ('team'). Mo'in confirms the correct forms: تِم [فر.] «۱- موضوع اساسی، مایه. \"\n            \"۲- زمینه» = thème, and تِز [فر.] «پایان‌نامه، رساله» = thèse. پرانتز (پَ رِ تِ) [فر.] «نشانه‌ای است قوسی \"\n            \"شکل ( )» from French parenthèse is correct, and بوتیک [فر.] is correct as a form, but Mo'in glosses it \"\n            \"«مغازه‌ای که در آن لباس، کفش، عطر و مانند آن فروخته می‌شود» — a clothes/fashion shop, not the 'gift \"\n            \"store' of the chart. Chronologically these entered Persian through French-language schooling and the \"\n            \"press from the late Qajar period onward, not through any inherited Iranian line.\"),\n        \"derivation_fa\": (\n            \"هر سه واژه وام‌واژه‌های فرانسویِ سدهٔ اخیرند، پس پیکانِ فرانسوی ← فارسی درست است؛ اما نگارشِ فارسیِ سطر \"\n            \"سوم در داده‌ها نادرست است. تصویرِ ۹۰۰ نقطه‌ایِ صفحهٔ چاپی «تِم ، تِز» را نشان می‌دهد (ت با کسره و سپس م)، \"\n            \"حال آنکه استخراجِ ماشینی کسره را «ی» خوانده و «تیم» ثبت کرده است که واژهٔ دیگری است. معین این را تأیید \"\n            \"می‌کند: «تِم [فر.] (اِ.) ۱- موضوع اساسی، مایه. ۲- زمینه» و «تِز [فر.] (اِ.) پایان‌نامه، رساله». «پرانتز» \"\n            \"نیز در معین «(پَ تِ) [فر.] (اِ.) نشانه‌ای است قوسی شکل ( )» آمده و درست است. «بوتیک» هم [فر.] است اما \"\n            \"معین آن را «مغازه‌ای که در آن لباس، کفش، عطر و مانند آن فروخته می‌شود» تعریف می‌کند، نه «فروشگاه هدیه» \"\n            \"که در نمودار آمده. پس خطای خوانشِ اسکن در «تیم»، و لغزشِ کوچکِ معناییِ کتاب در «بوتیک».\"),\n        \"sources\": [A_BUTIK, A_PAR, A_TEZ, A_TEM],\n        \"ref_check\": [{\"ref\": \"MON:625,1076,1137\", \"status\": \"partial\",\n                       \"note\": \"The three entries exist in Mo'in and all three carry his French-origin tag [فر.]: بوتیک «[فر.] (اِ.) مغازه‌ای که در آن لباس، کفش، عطر و مانند آن فروخته می‌شود»; پرانتز «(پَ تِ) [فر.] (اِ.) نشانه‌ای است قوسی شکل ( ) که برای نوشتن جملهٔ معترضه ... به کار رود»; تِم «(تِ) [فر.] (اِ.) ۱- موضوع اساسی، مایه. ۲- زمینه» and تِز «(تِ) [فر.] (اِ.) پایان‌نامه، رساله» (all read via abadis.ir, section فرهنگ معین). The page numbers 625/1076/1137 belong to the 6-vol. Amir Kabir printing (loanwords are in vol. 4), which is not the copy on disk — the 2-vol. Adena abridgement (MON_part1/part2) omits all three — so the exact pages are unverified; the substance is confirmed.\"}],\n        \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab/abadis, section فرهنگ معین, s.v. بوتیک، پرانتز، تم، تز\", \"stance\": \"supports\",\n             \"note\": \"All four tagged [فر.] = French. تِم is printed with a kasra and no yā, which is what settles the extraction error.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt / BQT_v2_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"grep for بوتیک/پرانتز/تم returns nothing usable; Borhan-e Qate' is a 17th-century dictionary and cannot contain modern French loans.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'butik\\\\|parantez' finds nothing; Horn's Grundriss (1893) covers inherited Persian vocabulary only.\"}]\n    })\n\n    nodes.append({\n        \"id\": 4, \"lang\": \"English\",\n        \"words\": \"boutique, theme, thesis, parenthesis\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"boutique entered English from French in 1767 in the general sense 'small shop', and was re-borrowed in \"\n            \"1950 in the fashion sense (Etymonline). theme is Middle English teme, from Old French tesme (mod. \"\n            \"thème) < Latin thema < Gk. θέμα (Klein, leaf 848). thesis is the Latin/Greek θέσις taken directly into \"\n            \"learned English (Skeat: 'Thesis: see Theme'). parenthesis is Medieval Latin parenthesis < Gk. \"\n            \"παρένθεσις, in English from the 1560s. All four are therefore descendants of τιθέναι through French \"\n            \"or through learned Latin, exactly as the chart draws them.\"),\n        \"derivation_fa\": (\n            \"«boutique» در ۱۷۶۷ به معنی «دکان کوچک» و دوباره در ۱۹۵۰ به معنی «مغازهٔ مد» از فرانسوی وارد انگلیسی شد. \"\n            \"«theme» از انگلیسی میانهٔ teme از فرانسوی کهن tesme و آن از thema لاتینی و θέμα یونانی است. «thesis» \"\n            \"مستقیماً از θέσις یونانی از راه لاتینیِ عالمانه گرفته شده و «parenthesis» از παρένθεσις یونانی از راه \"\n            \"لاتینیِ میانه در سدهٔ شانزدهم وارد انگلیسی شده است. پس هر چهار واژه، چنان‌که نمودار نشان می‌دهد، \"\n            \"بازماندگانِ τιθέναι یونانی‌اند. ادعای نورایی درست است.\"),\n        \"sources\": [E_BOUT],\n        \"ref_check\": [{\"ref\": \"AHD:156,1334\", \"status\": \"partial\",\n                       \"note\": \"Content confirmed from Watkins' dhē-¹ (leaf 42), where BOUTIQUE, THEME, THESIS and PARENTHESIS are all listed as English reflexes; the 1975 New College pages 156 and 1334 are not accessible.\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 112 (p. 193) boutique; leaf 848 theme; leaf 603 parenthesis\", \"stance\": \"supports\",\n             \"note\": \"\\\"theme, n. — ME. teme, fr. OF. tesme (F. thème), fr. L. thema, fr. Gk. θέματος\\\"; \\\"parenthesis, n. ... fr. Gk. παρένθεσις, 'insertion'\\\".\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 ≈ p. 511\", \"stance\": \"supports\",\n             \"note\": \"\\\"Thesis: see Theme.\\\"\"}]\n    })\n\n    nodes.append({\n        \"id\": 5, \"lang\": \"Germanic\",\n        \"words\": \"dôn\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"West Germanic *dōn 'to do' (Old English dōn, Old Saxon dōn, Old High German tuon) continues PIE *dʰoh₁-m \"\n            \"/ *dʰeh₁-, the o-grade of the same root: Grimm's law turns PIE *dʰ into Germanic *d, and the long ō is \"\n            \"the root's lengthened grade. Pokorny gives the paradigm directly: 'ahd. tōm, tuom, as. tōn, ags. dōn \"\n            \"\\\"tue\\\", Inf. ahd. tuon, as. ags. dōn (*dhō-m) \\\"tun\\\", Prät. ahd. teta \\\"ich tat\\\"'. The verb is \"\n            \"confined to West Germanic (Gothic has no *dōn), so 'Germanic' in the chart means West Germanic.\"),\n        \"derivation_fa\": (\n            \"*dōn ژرمنیِ باختری «کردن» (انگلیسی کهن dōn، ساکسونی کهن dōn، آلمانی علیای کهن tuon) دنبالهٔ *dʰoh₁-m/\"\n            \"*dʰeh₁- هندواروپایی است؛ بر پایهٔ قانونِ گریم، *dʰ هندواروپایی در ژرمنی به d بدل می‌شود و ōی کشیده \"\n            \"درجهٔ کشیدهٔ ریشه است. پوکورنی (ص ۲۳۶) خودِ صرف را می‌آورد: «ahd. tōm, tuom, as. tōn, ags. dōn ,tue‘ ... \"\n            \"(*dhō-m)». این فعل تنها در ژرمنیِ باختری هست (گوتی آن را ندارد)، پس «ژرمنی» در نمودار یعنی ژرمنیِ \"\n            \"باختری. ادعای نورایی درست است.\"),\n        \"sources\": [W_PIE],\n        \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n                       \"note\": \"AHD_watkins1985.txt leaf 42: \\\"1. O-grade form *dhō- in Germanic *dōn in Old English dōn, to do: DO¹; FORDO.\\\"\"}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 236 (POK_01.txt leaf 248)\", \"stance\": \"supports\",\n             \"note\": \"\\\"ahd. tōm, tuom, as. tōn, ags. dōn ,tue', Inf. ahd. tuon, as. ags. dōn (*dhō-m) ,tun', Prät. ahd. teta ,ich tat'\\\"\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 227 (≈ p. 412) s.v. deed / do\", \"stance\": \"supports\",\n             \"note\": \"\\\"deed, n. — ME. dede, fr. OE. dǣd ... fr. I.-E. *dhē-ti- ... derivatives of base *dhē-, *dhə-, 'to put, place; to do, make'. See do, v., and cp. thesis.\\\"\"}]\n    })\n\n    nodes.append({\n        \"id\": 6, \"lang\": \"English\",\n        \"words\": \"do, deed\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"English do is the direct continuation of Old English dōn (inf.), 3 sg. dēþ, pret. dyde; the modern \"\n            \"spelling keeps the OE long ō, which raised to /uː/ in the Great Vowel Shift. deed is OE dǣd < Germanic \"\n            \"*dēdiz < PIE *dʰeh₁-ti- 'thing put/done', the same ti-abstract that gives Greek θέσις and Latin \"\n            \"condicio; Klein sets them side by side. So both English words hang on the Germanic node as drawn.\"),\n        \"derivation_fa\": (\n            \"«do» انگلیسی دنبالهٔ مستقیمِ dōn انگلیسیِ کهن است (سوم‌شخص dēþ، ماضی dyde) و املای امروزی همان ōی کشیدهٔ \"\n            \"انگلیسیِ کهن را نگاه داشته که در «جابه‌جاییِ بزرگِ واکه‌ها» به /uː/ بدل شده است. «deed» از dǣd انگلیسیِ \"\n            \"کهن و آن از *dēdiz ژرمنی و *dʰeh₁-ti- هندواروپایی «آنچه نهاده/کرده شده» است؛ همان اسمِ مصدرِ ti-دار که \"\n            \"θέσις یونانی را هم ساخته است. کلاین این دو را کنار هم می‌گذارد. پس هر دو واژه، چنان‌که نمودار می‌گوید، \"\n            \"به گرهِ ژرمنی می‌پیوندند. ادعای نورایی درست است.\"),\n        \"sources\": [W_PIE],\n        \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n                       \"note\": \"AHD_watkins1985.txt leaf 42: \\\"...Old English dōn, to do: DO¹; FORDO. 2. Suffixed form *dhē-ti-, 'thing laid down or done, law, deed,' in Germanic *dēdiz in Old English dēd, doing, deed: DEED.\\\"\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 227 (≈ p. 412) s.v. deed\", \"stance\": \"supports\",\n             \"note\": \"\\\"deed, n. — ME. dede, fr. OE. dǣd, rel. to OS. dād, ON. dáð ... G. Tat, 'deed, act' ... fr. I.-E. *dhē-ti- ... See do, v., and cp. thesis.\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt (Concise Etym. Dict.), s.v. Deed/Do\", \"stance\": \"supports\",\n             \"note\": \"Skeat files Deed and Do under the root DHA, the same base he gives for Family (\\\"(√DHA.)\\\", leaf 166 ≈ p. 146).\"}]\n    })\n\n    nodes.append({\n        \"id\": 7, \"lang\": \"Latin\",\n        \"words\": \"facere; faciěs; opi-facium; facilis\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"Latin faciō, facere 'to do, make' is the zero grade *dʰh₁-k- with a k-enlargement, thematised as \"\n            \"*fak-yō; PIE *dʰ gives Latin f- initially. The perfect fēcī matches Greek ἔθηκα, and the Praenestine \"\n            \"fibula's fhefhaked 'fecit' and Oscan fefacid preserve the old reduplication (Ernout-Meillet p. 373). \"\n            \"Ernout-Meillet state the semantics explicitly: 'Le verbe appartient à une racine qui signifiait \"\n            \"\\\"mettre, placer, poser\\\" (τιθέναι) ... Le sens ancien est \\\"poser, placer\\\"'. faciēs 'shape, \"\n            \"appearance, face' is a derivative of the same stem ('form imposed on something'). 'opi-facium' is \"\n            \"Nourai's spelling of the reconstructed *opi-fici-om that underlies officium 'service, duty' (opus \"\n            \"'work' + facere) — Klein s.v. office: 'L. officium ... stands for *opi-faciom, lit. \\\"work-doing\\\"'. \"\n            \"facilis 'doable, easy' is *dʰh₁-k-li-, older facul.\"),\n        \"derivation_fa\": (\n            \"فعلِ لاتینی faciō/facere «کردن، ساختن» از درجهٔ صفرِ ریشه با گسترشِ k یعنی *dʰh₁-k- ساخته شده و به صورتِ \"\n            \"*fak-yō ستاکِ حال گرفته است؛ *dʰ هندواروپایی در آغازِ واژهٔ لاتینی f می‌دهد. ماضیِ fēcī همتای ἔθηκα یونانی \"\n            \"است و صورت‌های کهنِ fhefhaked (سنجاقِ پرانستین) و fefacid اُسکی مضاعف‌سازیِ کهن را نگاه داشته‌اند. \"\n            \"ارنو-مه‌یه (ص ۳۷۳) صریح می‌گوید: «این فعل به ریشه‌ای تعلق دارد که معنایش \\\"نهادن، گذاشتن\\\" (τιθέναι) \"\n            \"بوده است». faciēs «چهره، نمود» مشتقِ همان ستاک است. «opi-facium» نگارشِ نورایی از *opi-fici-om بازسازی‌شده \"\n            \"است که پایهٔ officium «خدمت، وظیفه» است (opus «کار» + facere)، و کلاین نیز همین را می‌گوید. facilis \"\n            \"«شدنی، آسان» از *dʰh₁-k-li- و صورتِ کهن‌ترِ facul است. ادعای نورایی درست است.\"),\n        \"sources\": [W_PIE],\n        \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n                       \"note\": \"AHD_watkins1985.txt leaf 42, dhē-¹ §6: \\\"a. Latin facere (< *fak-yo-), to do, make ... b. Latin derivative faciēs, shape, face (< 'form imposed on something') ... c. Latin compound officium (< *opi-fici-om), service, duty ... d. further suffixed form *dhə-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY.\\\" — all four of Nourai's Latin words, in order.\"}],\n        \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt lines 19915-19946 (printed p. 373) s.v. facio\", \"stance\": \"supports\",\n             \"note\": \"\\\"facio, -is, feci, factum, facere, verbe italique; osq. fakiiad ... prénestin fhefhaked 'fecit' ... Le verbe appartient à une racine qui signifiait 'mettre, placer, poser' (τιθέναι) ... Le sens ancien est 'poser, placer'.\\\"\"},\n            {\"src\": \"POK\", \"where\": \"IEW 235-236 (POK_01.txt leaf 247)\", \"stance\": \"supports\",\n             \"note\": \"\\\"Mit einer k-Erw. lat. faciō, -ere, fēcī (: ἔθηκα), factum ,tun, machen' ... facilis ,(tunlich) leicht' ... faciēs ,Aussehen, Erscheinung, Antlitz', facinus, pontifex, artifex, beneficus u. dgl.\\\"\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 576 (≈ p. 1128) s.v. office\", \"stance\": \"supports\",\n             \"note\": \"\\\"office, n. — ME., fr. OF. (= F.), fr. L. officium, 'service' ..., which stands for *opi-faciom, lit. 'work-doing'\\\" — Nourai's opi-facium.\"}]\n    })\n\n    nodes.append({\n        \"id\": 8, \"lang\": \"English\",\n        \"words\": \"-fy, fortify, modify; fact, benefit, defeat, perfect, profit, factor, factory, affect, effect, face, surface; office; facility, difficult, faculty\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"Four sub-lists, matching the four Latin words above. (a) -fy is Old French -fier < Latin -ficāre, the \"\n            \"combining form of facere in compounds (fortify < fortificāre, modify < modificāre). (b) fact < factum \"\n            \"'thing done'; benefit < benefactum/bene facere; defeat < Old French desfait < *disfacere; perfect < \"\n            \"perfectus; profit < prōfectus/prōficere; factor, factory < factor, factōrium; affect, effect < \"\n            \"afficere, efficere; face and surface from faciēs via Old French face and surface. (c) office < \"\n            \"officium (*opi-fici-om). (d) facility < facilitās, difficult back-formed from difficulty < \"\n            \"difficultās, faculty < facultās (a doublet of facilitās) — all from facilis. Klein's article on fact \"\n            \"lists this same set explicitly.\"),\n        \"derivation_fa\": (\n            \"چهار زیرفهرست، متناظر با چهار واژهٔ لاتینیِ بالا. یکم، پسوندِ -fy از -fier فرانسویِ کهن و آن از -ficāre \"\n            \"لاتینی است، یعنی صورتِ ترکیبیِ facere (fortify < fortificāre، modify < modificāre). دوم، fact از factum \"\n            \"«آنچه کرده شده»؛ benefit از bene facere؛ defeat از desfait فرانسویِ کهن؛ perfect از perfectus؛ profit از \"\n            \"prōficere؛ factor و factory از factor و factōrium؛ affect و effect از afficere و efficere؛ face و \"\n            \"surface از faciēs از راهِ فرانسویِ کهن. سوم، office از officium. چهارم، facility از facilitās، difficult \"\n            \"از difficultās و faculty از facultās (دوگانهٔ facilitās) — همه از facilis. کلاین در مدخل fact دقیقاً \"\n            \"همین فهرست را می‌آورد. ادعای نورایی درست است.\"),\n        \"sources\": [W_PIE],\n        \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n                       \"note\": \"The node carries no reference of its own in the book; it inherits AHD from the Latin parent, whose §6 lists -FIC, (-FY), FACT, ... BENEFIT, ... DEFEAT, ... EFFECT, ... FACSIMILE, FACTOTUM, ... MODIFY, ... OFFICE, PERFECT, ... PROFIT ... FACILE, (FACILITY), FACULTY; DIFFICULTY, and §6b FACE, (SURFACE).\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 309 (p. 570-571) s.v. fact\", \"stance\": \"supports\",\n             \"note\": \"\\\"fact, n. — L. factum, 'deed, act', lit. 'something done' ... fr. I.-E. base *dhē-, *dhə-, ... Cp. also feat ... and the words facade, facient, facile, facilitate, facility, ... factor, factory, factotum, ... affect, ... benefit, ... counterfeit, ... defeat, defect, ... difficult, ... efface, effect, ... face, fashion, ... -fy, ... office, ... perfect, ... proficient, ... surface, surfeit.\\\" — Klein's list is Nourai's list.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 42, dhē-¹ §6\", \"stance\": \"supports\",\n             \"note\": \"Same English set under the Latin facere branch.\"}]\n    })\n\n    nodes.append({\n        \"id\": 9, \"lang\": \"Indo-European\",\n        \"words\": \"Dhě-mo, Dh-mo\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\n            \"The formation is real but the gloss and the reconstruction are Klein's, not the standard ones. A \"\n            \"*men-/*mo- noun to *dʰeh₁- is well attested — Sanskrit dhā́man- 'place, abode, statute' (*dʰeh₁-mn̥), \"\n            \"Greek θωμός 'heap' (*dʰoh₁-mo-) — and Pokorny lists 'dhē-men-, dhē-mi-, dho-mi-, dhō-mo-, dho-mo-' \"\n            \"among the nominal derivatives of 2. dhē- on the very page Nourai cites for the root. Walde-Pokorny \"\n            \"(WP I 828) posits '*dhō-mo- \\\"Niederlassung, Wohnstätte\\\" (vgl. ... ai. dhāman- \\\"Wohnstätte\\\") oder \"\n            \"\\\"Haufe, Schar (der Diener)\\\"'. What is not standard is the gloss 'house' as the primary meaning and \"\n            \"the shape *dhē-mo-/*dh-mo-: the sense is 'thing set down > settlement, abode', and it is reached only \"\n            \"through the Sanskrit and Greek forms, not reconstructible as a PIE word for 'house' (that is *domos, a \"\n            \"different root, *dem-).\"),\n        \"derivation_fa\": (\n            \"این ساختِ اسمی واقعی است اما معنا و صورتی که کلاین (و به پیروی او نورایی) می‌دهد معیار نیست. اسمِ *-men-/\"\n            \"*-mo- از ریشهٔ *dʰeh₁- به‌خوبی گواهی شده است: dhā́man- سنسکریت «جایگاه، قانون» (< *dʰeh₁-mn̥) و θωμός \"\n            \"یونانی «توده» (< *dʰoh₁-mo-)؛ پوکورنی نیز در همان صفحهٔ ۲۳۵ که نورایی به آن ارجاع می‌دهد «dhē-men-، \"\n            \"dhē-mi-، dho-mi-، dhō-mo-، dho-mo-» را در میان مشتقاتِ اسمیِ ریشه می‌آورد و والده-پوکورنی (جلد ۱، ص ۸۲۸) \"\n            \"*dhō-mo- «سکونتگاه، جایگاه» را بازسازی می‌کند. آنچه معیار نیست، یکی معنای نخستینِ «خانه» است و دیگری \"\n            \"صورتِ *dhē-mo-/*dh-mo-؛ معنای اصلی «آنچه نهاده شده > سکونتگاه» است و واژهٔ هندواروپاییِ «خانه» چیز \"\n            \"دیگری است (*domos از ریشهٔ *dem-). پس با احتیاط پذیرفتنی است.\"),\n        \"sources\": [W_PIE, W_FAM],\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"supports\",\n                       \"note\": \"KLN_1966.txt leaf 310 (printed pp. 572-573; leaf 309 carries 570/571 and leaf 311 carries 574/575), s.v. family: \\\"It possibly means lit. 'belonging to the house', and derives fr. I.-E. base *dhē-mo-, 'house', whence also OI. dhāman, 'seat, house', Gk. θαμός (Hesychius), 'house'. Base *dhē-mo- is an enlargement of base *dhē-, 'to put, place; to do, make'.\\\" — Nourai's node is a transcript of this sentence, including the page. Note Klein's own hedge, 'possibly'.\"}],\n        \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 828 (incoming/WLD/WLD_Bd1_pages.txt leaf 836)\", \"stance\": \"partial\",\n             \"note\": \"\\\"auf ein *dhō-mo- 'Niederlassung, Wohnstätte' (vgl. ... ai. dhāman- 'Wohnstätte') oder 'Haufe, Schar (der Diener)' bezieht man ... vielleicht mit Recht auch lat. famulus 'Diener', familia 'Hausgenossenschaft'\\\" — the same idea, but with 'vielleicht mit Recht' and the o-grade *dhō-mo-, not Klein's *dhē-mo-.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 235 (POK_01.txt leaf 247)\", \"stance\": \"partial\",\n             \"note\": \"The headword line lists the nominal derivatives \\\"dhē-men-, dhē-mi-, dho-mi-, dhō-mo-, dho-mo-; dhē-dh-mo-\\\" but Pokorny does not gloss any of them 'house' and does not bring famulus in under them.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 42, dhē-¹ §3\", \"stance\": \"partial\",\n             \"note\": \"Watkins has the o-grade *dho-mo- only in the Germanic 'judgment/doom' branch (\\\"Suffixed o-grade form *dho-mo- in Germanic *dōmaz\\\") and nowhere derives famulus/familia from the root.\"}]\n    })\n\n    nodes.append({\n        \"id\": 10, \"lang\": \"Latin\",\n        \"words\": \"famul, famulus, familia\",\n        \"verdict\": \"disputed\",\n        \"derivation\": (\n            \"The Latin words are real — famul is the Old Latin nominative (Ennius, Ann.), famulus 'servant', \"\n            \"familia 'the household slaves, the household' — and their Italic antiquity is guaranteed by Oscan \"\n            \"famel 'famulus', Oscan famelo and Umbrian fameřias 'familia' (Festus/Paulus 77.11: 'famuli origo ab \"\n            \"Oscis dependet, apud quos servus famel nominabatur, unde et familia vocata'). But the derivation from \"\n            \"*dʰeh₁-mo- 'house' that the arrow draws is not the modern view. Ernout-Meillet (p. 383) conclude: 'Les \"\n            \"autres langues indo-européennes n'offrent aucun rapprochement. On peut se demander si le mot, dont la \"\n            \"forme n'est guère indo-européenne, n'est pas emprunté, peut-être à l'étrusque'. Etymonline (s.v. \"\n            \"family) and de Vaan likewise call famulus 'of unknown origin'. Klein, Nourai's own source, hedges with \"\n            \"'which is of uncertain origin. It possibly means...'; Walde-Pokorny with 'vielleicht mit Recht'. The \"\n            \"gloss 'belonging to the house' is likewise a guess, not an attested sense: famulus means 'servant', \"\n            \"and the -ulus looks like the agent suffix of baiulus, gerulus.\"),\n        \"derivation_fa\": (\n            \"خودِ واژه‌های لاتینی درست‌اند: famul صورتِ فاعلیِ لاتینیِ کهن (انیوس)، famulus «خدمتکار» و familia «مجموعهٔ \"\n            \"بردگان و اهلِ خانه». کهنگیِ ایتالیاییِ آن‌ها را famel اُسکی و fameřias اومبریایی تضمین می‌کند و فستوس نیز \"\n            \"می‌نویسد «famuli origo ab Oscis dependet». اما اشتقاقی که پیکانِ نمودار نشان می‌دهد، یعنی از *dʰeh₁-mo- \"\n            \"«خانه»، دیدگاهِ امروزی نیست. ارنو-مه‌یه (ص ۳۸۳) نتیجه می‌گیرند: «دیگر زبان‌های هندواروپایی هیچ همتایی \"\n            \"ندارند. می‌توان پرسید که آیا این واژه، که صورتش چندان هندواروپایی نیست، وام‌واژه — شاید از اتروسکی — \"\n            \"نباشد». اتیمانلاین و دخان نیز famulus را «با خاستگاهِ ناشناخته» می‌خوانند. خودِ کلاین هم می‌گوید «خاستگاهش \"\n            \"نامعلوم است؛ شاید به معنی ...». پس پژوهشِ امروزی ادعای نورایی را رد می‌کند و famulus را واژه‌ای ایتالیایی \"\n            \"با خاستگاهِ ناشناخته (احتمالاً اتروسکی) می‌داند.\"),\n        \"sources\": [E_FAM, W_FAM],\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"partial\",\n                       \"note\": \"KLN_1966.txt leaf 310 = p. 573 s.v. family: \\\"L. familia, fr. famulus, fr. OL. famul, 'servant', which is of uncertain origin. It possibly means lit. 'belonging to the house', and derives fr. I.-E. base *dhē-mo-, 'house'\\\". Klein supplies the three words and the gloss Nourai copies, but explicitly marks the etymology 'uncertain'/'possibly' — Nourai's chart drops the hedge.\"}],\n        \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt lines 20489-20545 (printed p. 383) s.v. famulus\", \"stance\": \"contradicts\",\n             \"note\": \"\\\"Famulus, familia sont des mots italiques, et, en latin, peut-être des emprunts à l'osque: famuli origo ab Oscis dependet ... Les autres langues indo-européennes n'offrent aucun rapprochement. On peut se demander si le mot, dont la forme n'est guère indo-européenne, n'est pas emprunté, peut-être à l'étrusque.\\\"\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 828 (leaf 836)\", \"stance\": \"partial\",\n             \"note\": \"\\\"bezieht man ... vielleicht mit Recht auch lat. famulus 'Diener', familia 'Hausgenossenschaft', osk. famel 'famulus', bantin. famelo 'familia', umbr. fameřias 'familia'\\\" — offered as a possibility only.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 166 (≈ p. 146) s.v. Family\", \"stance\": \"supports\",\n             \"note\": \"\\\"Family. (F.-L.) F. famille. — L. familia, a household. — L. famulus, a servant. Oscan famel ... Cf. Skt. dhāman, a house. (√DHĀ.)\\\" — Skeat (1911) still holds the connection Nourai draws, which is why the 19th-century handbooks and Klein pass it on.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, dhē-¹ (leaf 42) and index\", \"stance\": \"silent\",\n             \"note\": \"Watkins lists no FAMILY/FAMULUS under dhē-¹ (nor under any root); grep 'famul' returns nothing.\"}]\n    })\n\n    nodes.append({\n        \"id\": 11, \"lang\": \"English\",\n        \"words\": \"family, familiar\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\n            \"This link — Latin familia/familiāris to English — is beyond dispute whatever the ultimate origin of \"\n            \"famulus. family is attested from the early 15th c. in the sense 'servants of a household', from Latin \"\n            \"familia 'family servants, domestics collectively'; the sense 'parents with their children' is only \"\n            \"1660s (Etymonline). familiar is Old French familier < Latin familiāris 'pertaining to a household, \"\n            \"domestic', dissimilated from *familiālis (Klein).\"),\n        \"derivation_fa\": (\n            \"این حلقه — از familia و familiāris لاتینی به انگلیسی — بی‌چون‌وچرا درست است، هرچه خاستگاهِ نهاییِ famulus \"\n            \"باشد. واژهٔ family از آغازِ سدهٔ پانزدهم به معنی «خدمتکارانِ خانه» گواهی شده است و معنای «پدر و مادر و \"\n            \"فرزندان» تنها از دههٔ ۱۶۶۰ پیدا شده است. واژهٔ familiar از familier فرانسویِ کهن و آن از familiāris \"\n            \"لاتینی «وابسته به خانه» است که به گفتهٔ کلاین از *familiālis ناهمگون شده است. ادعای نورایی در این گره \"\n            \"درست است؛ تنها پیوندِ بالاترِ آن با ریشهٔ هندواروپایی مورد اختلاف است.\"),\n        \"sources\": [E_FAM],\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"supports\",\n                       \"note\": \"KLN_1966.txt leaf 310-311 (pp. 573-574): \\\"familiar, adj. — OF. (= F.) familier, fr. L. familiāris, 'pertaining to a household, domestic', dissimilated fr. *familia-lis, fr. familia, 'household'. See family\\\"; and \\\"family, n. — L. familia ...\\\".\"}],\n        \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 166 (≈ p. 146) s.v. Family\", \"stance\": \"supports\",\n             \"note\": \"\\\"Family. (F.-L.) F. famille. — L. familia, a household ... Der. famili-ar (L. familiaris)\\\".\"},\n            {\"src\": \"AHD\", \"where\": \"etymonline s.v. family (archived) as the modern statement\", \"stance\": \"supports\",\n             \"note\": \"\\\"family (n.) early 15c., 'servants of a household', from Latin familia 'family servants, domestics collectively' ... abstract noun formed from famulus 'servant, slave', which is of unknown origin.\\\" — the English chain is confirmed even though the ultimate origin is not.\"}]\n    })\n\n    nodes.append({\n        \"id\": 12, \"lang\": \"Sanskrit\",\n        \"words\": \"dhâman\",\n        \"verdict\": \"disputed\",\n        \"derivation\": (\n            \"The word is genuine: Vedic dhā́man- n. 'thing set down; law, statute; abode, dwelling place, domain' \"\n            \"(RV), an n-stem *dʰeh₁-mn̥ built straight on dhā- 'to put, place' (dádhāti). What is wrong is the \"\n            \"arrow. On the printed page (see data/verification/sources/refs/ocr/BOOK/125.png) the curve into the \"\n            \"Sanskrit box leaves the bottom-left corner of the Latin box, so the extraction's 'parent 10' is \"\n            \"faithful to the layout — but Sanskrit dhā́man- cannot descend from Latin famulus/familia; the two are \"\n            \"at best collateral relatives, and Klein, from whom the whole sub-tree is copied, names dhāman only as \"\n            \"a comparandum ('whence also OI. dhāman, \\\"seat, house\\\"'). Nourai's own convention elsewhere is to \"\n            \"hang cognates off the IE node, so the arrow should start at node 9. The gloss 'seat, house' is Klein's \"\n            \"abbreviation of Monier-Williams' 'dwelling-place, house, abode'.\"),\n        \"derivation_fa\": (\n            \"خودِ واژه اصیل است: dhā́man- ودایی «آنچه نهاده شده؛ قانون، نهاد؛ جایگاه، خانه» (ریگ‌ودا)، اسمی با ستاکِ \"\n            \"n از *dʰeh₁-mn̥ که یکراست بر فعلِ dhā- «نهادن» (dádhāti) ساخته شده است. آنچه نادرست است پیکانِ نمودار \"\n            \"است. در صفحهٔ چاپی، منحنیِ ورودی به جعبهٔ سنسکریت از گوشهٔ پایین-چپِ جعبهٔ لاتینی بیرون می‌آید، پس ثبتِ \"\n            \"«پدر = گرهٔ ۱۰» در داده‌ها با چیدمانِ کتاب می‌خواند؛ اما dhā́man- سنسکریت به هیچ روی نمی‌تواند از famulus \"\n            \"لاتینی آمده باشد — این دو در بهترین حالت هم‌ریشه‌اند، و کلاین که همهٔ این زیرشاخه از او گرفته شده dhāman \"\n            \"را تنها «هم‌سنجه» می‌آورد. پس این پیکان باید از گرهٔ ۹ (هندواروپایی) می‌آمد، نه از لاتین. پژوهشِ امروزی \"\n            \"این پیکان را رد می‌کند.\"),\n        \"sources\": [W_PIE],\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"partial\",\n                       \"note\": \"KLN_1966.txt leaf 310 = p. 573 s.v. family: \\\"derives fr. I.-E. base *dhē-mo-, 'house', whence also OI. dhāman, 'seat, house', Gk. θαμός (Hesychius), 'house'\\\" — Klein makes dhāman a cognate of the IE base, NOT a derivative of Latin famulus; the page supports the word and its gloss but not the edge drawn in the chart.\"}],\n        \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 828 (leaf 836)\", \"stance\": \"supports\",\n             \"note\": \"\\\"auf ein *dhō-mo- 'Niederlassung, Wohnstätte' (vgl. ... ai. dhāman- 'Wohnstätte')\\\" — Sanskrit dhāman- belongs to the IE root directly, alongside (not under) the Italic words.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 235 (POK_01.txt leaf 247)\", \"stance\": \"partial\",\n             \"note\": \"Pokorny lists the Sanskrit material of the root (dádhāti, dhā́tu- 'Bestandteil, Satz') and the nominal type dhē-men-/dhō-mo- but treats none of it as Italic-derived.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 166 (≈ p. 146) s.v. Family\", \"stance\": \"partial\",\n             \"note\": \"\\\"Cf. Skt. dhāman, a house. (√DHĀ.)\\\" — 'Cf.' = comparison, again not descent from Latin.\"}]\n    })\n\n    return {\n        \"entry\": 0,\n        \"root\": \"Dhě 2\",\n        \"verdict\": \"confirmed\",\n        \"modern_form\": \"PIE *dʰeh₁- 'to put, place, set' (Pokorny 2. dhē- 235; Watkins dhē-¹ 'to set, put')\",\n        \"note\": (\n            \"The root box is exactly right. Pokorny IEW 235 has '2. dhē- \\\"setzen, stellen, legen\\\"' and Watkins' \"\n            \"dhē-¹ 'To set, put' closes with '[Pok. 2. dhé- 235.]', so Nourai's two references agree with each \"\n            \"other and with him; his 'to do, set' is the same thing, the 'do' sense being the Germanic and Italic \"\n            \"specialisation of 'put'. 'PART 2' means the Greek/Germanic/Latin branches shown here; the Iranian and \"\n            \"Indic reflexes (Av. daδāiti, OP adadā, Skt dádhāti) are on the other part. Nothing in the root box \"\n            \"needs correcting. Two things on the page do: the French box (node 2) prints an Old Provençal form as \"\n            \"French and misspells parenthèse, and the whole Dhē-mo/famulus sub-tree (nodes 9-12) rests on Klein's \"\n            \"hedged guess, which Ernout-Meillet and current Latin etymology reject.\"),\n        \"note_fa\": (\n            \"جعبهٔ ریشه کاملاً درست است. پوکورنی در صفحهٔ ۲۳۵ «2. dhē- ,setzen, stellen, legen‘» را دارد و واتکینز نیز \"\n            \"dhē-¹ «نهادن، گذاشتن» را با ارجاعِ «[Pok. 2. dhé- 235]» می‌آورد؛ پس هر دو ارجاعِ نورایی با یکدیگر و با \"\n            \"او می‌خوانند، و «to do» تخصیصِ معناییِ ژرمنی و ایتالیایی از همان «نهادن» است. «بخش ۲» یعنی شاخه‌های \"\n            \"یونانی و ژرمنی و لاتینی که در اینجا آمده‌اند؛ بازتاب‌های ایرانی و هندی (daδāiti اوستایی، adadā پارسیِ \"\n            \"باستان، dádhāti سنسکریت) در بخشِ دیگرند. دو نکته در این صفحه نیازمندِ اصلاح است: جعبهٔ فرانسوی (گرهٔ ۲) \"\n            \"صورتی پرووانسالی را فرانسوی خوانده و parenthèse را غلط نوشته است؛ و کلِ زیرشاخهٔ Dhē-mo/famulus (گره‌های \"\n            \"۹ تا ۱۲) بر حدسِ محتاطانهٔ کلاین استوار است که ارنو-مه‌یه و ریشه‌شناسیِ لاتینیِ امروز آن را نمی‌پذیرند.\"),\n        \"sources\": [W_PIE, E_BOUT, E_FAM, W_FAM],\n        \"ref_check\": [\n            {\"ref\": \"AHD:1512\", \"status\": \"supports\", \"note\": AHD_NOTE},\n            {\"ref\": \"POK:235\", \"status\": \"supports\", \"note\": POK_NOTE}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 235-237 (POK_01.txt leaves 246-248)\", \"stance\": \"supports\", \"note\": POK_NOTE},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 826-829 (incoming/WLD/WLD_Bd1_pages.txt leaves 834-836)\", \"stance\": \"supports\", \"note\": WLD_NOTE},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 42, s.v. dhē-¹\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n            {\"src\": \"IEC\", \"where\": \"Mann, pp. 181-182 (IEC.txt leaf 113)\", \"stance\": \"supports\",\n             \"note\": \"\\\"dhēiô dhēmi (2) 'put, lay'. Cf. dhídhemi, dhesnos, dhetis, dhētos, etc. WP I, 827-829 ... Tokh. AB tes-, B tes- (= Skt. dhāsyāmi: Arm. edic: Gk. thḗsō: Li. dėsiu)\\\"\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed., leaf 309 (p. 570) s.v. fact; leaf 227 s.v. deed\", \"stance\": \"supports\",\n             \"note\": \"\\\"fr. I.-E. base *dhē-, *dhə-, *dhī-, 'to put, place; to do, make, construct'. See do and theme\\\" — the same root, the same double gloss Nourai gives ('to do, set').\"}],\n        \"nodes\": nodes,\n    }\n\n\ndef entry2():\n    nodes = []\n    nodes.append({\n        \"id\": 1, \"lang\": \"Persian\",\n        \"words\": \"dadeh «دَده ۲»\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\n            \"The Persian word and its sense are right: Mo'in has دده ۲ '[cf. دادا] paternal or maternal \"\n            \"grandparent; a maidservant who looks after the children, a black maidservant', and Wiktionary gives \"\n            \"دده dada/dade '(dialectal) sister; (historical) maidservant, housemaid; female slave'. What is \"\n            \"uncertain is the descent. Both Pokorny and Wiktionary class the whole family as a nursery Lallwort \"\n            \"('Lallwort der Kindersprache für ältere Familienglieder'; Wiktionary s.v. دده: 'A babble word'), and \"\n            \"such CVCV reduplications are re-created independently in every generation, so a Persian dada need not \"\n            \"be an inherited *dʰedʰ- at all. Mo'in himself points the other way: his headword دادا is tagged \"\n            \"[تر.] = Turkish and glossed 'maidservant who serves someone's children', and Turkic has dede \"\n            \"'grandfather' (< Proto-Turkic *tēte) and dadı 'nanny', so a Turkic route into Persian is at least as \"\n            \"likely as inheritance. Nourai's arrow is therefore compatible with the sources but not established by \"\n            \"them.\"),\n        \"derivation_fa\": (\n            \"خودِ واژه و معنایش درست است: معین «دَده ۲ [قس. دادا] (اِ.) جد پدری یا مادری؛ کنیزکی که کودکان را \"\n            \"نگه‌داری کند، کنیز سیاه» را دارد و ویکی‌واژه نیز «دده (dada/dade): خواهر (گویشی)؛ کنیز، خدمتکارِ زن \"\n            \"(تاریخی)» می‌آورد. آنچه نامسلم است خودِ اشتقاق است. هم پوکورنی و هم ویکی‌واژه این خانواده را واژهٔ \"\n            \"کودکانه (Lallwort) می‌دانند، و چنین ساخت‌های مضاعفی در هر نسل از نو ساخته می‌شوند؛ پس «دده» فارسی \"\n            \"لزوماً بازماندهٔ موروثیِ *dʰedʰ- نیست. خودِ معین هم به سوی دیگری اشاره می‌کند: مدخلِ «دادا» را با نشانِ \"\n            \"[تر.] یعنی ترکی آورده است، و در ترکی dede «پدربزرگ» (از ترکیِ آغازین *tēte) و dadı «دایه» هست. پس \"\n            \"وام‌گیری از ترکی دستِ‌کم به اندازهٔ توارث محتمل است و ادعای نورایی تنها با احتیاط پذیرفتنی است.\"),\n        \"sources\": [W_DADEH],\n        \"ref_check\": [{\"ref\": \"MON:1499\", \"status\": \"partial\",\n                       \"note\": \"The entry is in Mo'in (read in the 2-vol. Adena abridgement, MON_part1.txt lines 59965-59975): \\\"دده: (۲) [قس. دادا] (اِ.) جد پدری یا مادری. خال پیر، دایی‌پیر. کنیزکی که کودکان را نگه‌داری کند، کنیز سیاه\\\" — i.e. exactly Nourai's 'maid servant, nurse' and his numbering '۲'. But Mo'in gives no Indo-European etymology; he cross-refers to دادا, whose own entry (line 58764) reads \\\"دادا: [تر. = دده] (اِ.) کنیز. کنیزکی که فرزندان کسی را خدمت کند\\\" — tagged Turkish. The printed page 1499 belongs to the 6-vol. Amir Kabir edition, which is not the copy on disk, so the page itself is unverified.\"}],\n        \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 58764 and 59965-59975 (Adena 2-vol. abridgement) s.v. دادا، دده\", \"stance\": \"partial\",\n             \"note\": \"\\\"دادا: [تر. - دده] (اِ.) کنیز ...\\\" / \\\"دده: (۲) [قس. دادا] ... کنیزکی که کودکان را نگه‌داری کند\\\" — the sense supports Nourai, the origin tag [تر.] points to Turkic, not to Indo-European.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt (Horn, Grundriss der neupersischen Etymologie)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'dada\\\\|dade' returns only forms of dādan 'to give' (nos. around p. 126) and vandādan; Horn has no article on دده.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt (Hübschmann, Persische Studien)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'dada\\\\|dade' returns only dādistān 'Urteil', dadqmi and similar forms of dā- 'to give'; no دده.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt (Borhan-e Qate', د section)\", \"stance\": \"silent\",\n             \"note\": \"grep 'دده' over the Borhan OCR returns only broken OCR fragments of other words; no usable دده article, so Mo'in's footnotes there could not be read.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt, [pdf page 265] = printed p. 266\", \"stance\": \"partial\",\n             \"note\": \"Aryanpur's page for the nursing family lists \\\"*DHE, *DHENA, *DHEDHN., *DHELU, *DHEI- (INDO-EUROPEAN)\\\" with Avestan daēnu-, Pahlavi dāyag, Kurdish dayē, Sanskrit dhā-/dhātrī — i.e. he attaches the Persian nursing words (دایه) to Pokorny's dhē(i)- 'suckle', not to a separate *dhedh-; he has no entry for دده.\"}]\n    })\n\n    nodes.append({\n        \"id\": 2, \"lang\": \"Greek\",\n        \"words\": \"těthě 2\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\n            \"Greek τήθη is a real word and does belong to this reduplicated nursery root — Wiktionary: 'From \"\n            \"Proto-Indo-European *dʰeh₁dʰ- (\\\"grandparent\\\"). Cognate with Proto-Slavic *dědъ, Lithuanian dė̃dė, \"\n            \"dė̃dis (\\\"uncle\\\") ... Probably originally an onomatopoeia of babies' speech' — and Pokorny lists it \"\n            \"under 1. dhē- on p. 235: 'gr. θεῖος \\\"Onkel\\\", θεία \\\"Tante\\\" ... τήθη \\\"Großmutter\\\"'. But its \"\n            \"attested sense is 'grandmother', not 'nurse'; the nursing sense belongs to the Titaness Τηθύς, nurse \"\n            \"of Hera, and Mann himself flags the gloss as doubtful: 'Gk. cf. (*-ē-) Tēthús (nurse of Hera) and \"\n            \"(alleged) téthē \\\"nurse\\\"'. Nourai has taken over Mann's word and his gloss without Mann's caveat.\"),\n        \"derivation_fa\": (\n            \"τήθη یونانی واژه‌ای واقعی است و به همین ریشهٔ مضاعفِ کودکانه تعلق دارد؛ ویکی‌واژه می‌نویسد «از \"\n            \"*dʰeh₁dʰ- هندواروپاییِ آغازین \\\"پدربزرگ/مادربزرگ\\\"، هم‌ریشه با *dědъ اسلاویِ آغازین و dė̃dė لیتوانیایی \"\n            \"\\\"عمو\\\" ... احتمالاً در اصل تقلیدِ آواییِ زبانِ کودکان»، و پوکورنی نیز آن را در همان صفحهٔ ۲۳۵ ذیل \"\n            \"«1. dhē-» می‌آورد: «θεῖος \\\"عمو\\\"، θεία \\\"عمه\\\" ... τήθη \\\"مادربزرگ\\\"». اما معنای گواهی‌شدهٔ آن \"\n            \"«مادربزرگ» است نه «دایه»؛ معنای دایگی به Τηθύς، الههٔ دایهٔ هرا، بازمی‌گردد. خودِ مان نیز این معنا را \"\n            \"مشکوک می‌داند و می‌نویسد «(alleged) téthē \\\"nurse\\\"». نورایی واژه و معنای مان را بی‌آنکه احتیاطِ او را \"\n            \"نگه دارد برداشته است.\"),\n        \"sources\": [W_TETHE],\n        \"ref_check\": [{\"ref\": \"IEC:178\", \"status\": \"supports\",\n                       \"note\": \"IEC.txt leaf 111 (which carries the printed page numbers 178 and 179): \\\"dhedh- 'nurse' Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) téthe 'nurse'; Ir. cf. deol, diúl 'suckling', isophonic w. Gk. thēlé, see dhēl-; cf. also Ir. dedel 'she-calf'\\\" — Nourai's page is exact and his node is a transcript of Mann's line, minus Mann's '(alleged)'.\"}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 235 (POK_01.txt leaf 246)\", \"stance\": \"partial\",\n             \"note\": \"\\\"1. dhē-, redupl. dhē-dh(e)- Lallwort der Kindersprache für ältere Familienglieder. Gr. θεῖος ,Onkel', θεία ,Tante' (*θη-ος, θη-ᾱ), τήθη ,Großmutter' (aus *θη-θη) ... illyr. deda ,Amme' ... also wohl ursprüngl. zur Wz. dhē(i)- ,säugen'\\\" — Pokorny's gloss for τήθη is 'Großmutter', and only Illyrian deda means 'Amme' (nurse).\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 825-826 (incoming/WLD/WLD_Bd1_pages.txt leaf 834)\", \"stance\": \"partial\",\n             \"note\": \"The same family, ending \\\"lit. dėdė 'Oheim' (aber diedas 'Greis' aus wr. died ds.), aksl. dědъ 'Großvater'; ähnlich nhd. deite, teite 'Vater, Greis', russ. djadja 'Oheim'\\\" — kin terms, no 'nurse'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n             \"note\": \"grep -i 'dhedh' finds nothing; Watkins has no root of this shape, because no English word descends from it.\"}]\n    })\n\n    return {\n        \"entry\": 2,\n        \"root\": \"Dhedh 2\",\n        \"verdict\": \"plausible\",\n        \"modern_form\": \"PIE *dʰedʰ- / *dʰeh₁dʰ- 'grandparent, elder relative' (Pokorny 1. dhē-, redupl. dhē-dh(e)-, IEW 235; Mann dhedh- 'nurse', IEC 178)\",\n        \"note\": (\n            \"Nourai's root box is a faithful copy of Mann, IEC 178, where the headword really is \\\"dhedh- 'nurse'\\\" \"\n            \"with Persian dade and Greek tethe under it — so the reference checks out to the page. The reservation \"\n            \"is about Mann, not about Nourai's reading of him: every other authority reconstructs this reduplication \"\n            \"as a kinship Lallwort, not a word for 'nurse'. Pokorny (IEW 235, on the very same page as Dhě 2 on this \"\n            \"sheet) has '1. dhē-, redupl. dhē-dh(e)- Lallwort der Kindersprache für ältere Familienglieder', with \"\n            \"Gk. τήθη 'grandmother', Lith. dėdė 'uncle', OCS dědъ 'grandfather'; only Illyrian deda is glossed \"\n            \"'Amme'. Wiktionary reconstructs *dʰeh₁dʰ- 'grandparent' and adds that it is 'probably originally an \"\n            \"onomatopoeia of babies' speech'. Since nursery words are re-coined rather than inherited, neither \"\n            \"branch of this two-node tree can be proved to descend from a common proto-form; the meaning 'nurse' is \"\n            \"secondary in both.\"),\n        \"note_fa\": (\n            \"جعبهٔ ریشهٔ نورایی رونوشتِ دقیقِ مان (IEC، ص ۱۷۸) است؛ آنجا مدخل واقعاً «dhedh- \\\"nurse\\\"» است با «دده» \"\n            \"فارسی و tethe یونانی زیرِ آن، پس ارجاع تا حدِ شمارهٔ صفحه درست است. ایراد متوجهِ مان است نه خوانشِ نورایی: \"\n            \"همهٔ مرجع‌های دیگر این صورتِ مضاعف را واژه‌ای کودکانه برای خویشاوندانِ سالمند می‌دانند نه واژه‌ای به \"\n            \"معنی «دایه». پوکورنی در صفحهٔ ۲۳۵ — همان صفحه‌ای که ریشهٔ Dhě 2 در آن است — می‌نویسد «1. dhē-، مضاعف \"\n            \"dhē-dh(e)-، واژهٔ کودکانه برای اعضای سالمندِ خانواده» و τήθη «مادربزرگ»، dėdė لیتوانیایی «عمو» و dědъ \"\n            \"اسلاویِ کهن «پدربزرگ» را می‌آورد؛ تنها deda ایلیریایی «دایه» معنی شده است. ویکی‌واژه نیز *dʰeh₁dʰ- \"\n            \"«پدربزرگ/مادربزرگ» را بازسازی می‌کند و می‌افزاید که «احتمالاً در اصل تقلیدِ آواییِ زبانِ کودکان» است. چون \"\n            \"واژه‌های کودکانه در هر زبان از نو ساخته می‌شوند، هیچ‌یک از دو شاخهٔ این نمودارِ دوگره‌ای را نمی‌توان \"\n            \"به‌یقین بازماندهٔ یک صورتِ نیایِ مشترک دانست؛ معنای «دایه» در هر دو ثانوی است. پس با احتیاط پذیرفتنی است.\"),\n        \"sources\": [W_TETHE, W_DADEH],\n        \"ref_check\": [{\"ref\": \"IEC:178\", \"status\": \"supports\",\n                       \"note\": \"IEC.txt leaf 111 (printed pp. 178-179): \\\"dhedh- 'nurse' Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) téthe 'nurse' ...\\\" — headword, gloss and both daughters are Nourai's, on the page he cites.\"}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 235 (POK_01.txt leaf 246)\", \"stance\": \"partial\",\n             \"note\": \"\\\"1. dhē-, redupl. dhē-dh(e)- Lallwort der Kindersprache für ältere Familienglieder ... τήθη ,Großmutter' ... illyr. deda ,Amme' (Krahe IF. 55, 121 f.), also wohl ursprüngl. zur Wz. dhē(i)- ,säugen'; lit. dėdė, dėdis ,Oheim' ... aksl. dědъ ,Großvater'\\\" — same reconstruction, different gloss.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 825-826 (leaf 834)\", \"stance\": \"partial\",\n             \"note\": \"The identical article in the earlier edition, ending with \\\"russ. djadja 'Oheim', s. Delbrück Verwandtschaftsn. 468, Berneker 191\\\" — kinship terms only.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, p. 178 (leaf 111)\", \"stance\": \"supports\", \"note\": \"Nourai's source; see ref_check.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n             \"note\": \"No *dhedh- root in Watkins (grep -i 'dhedh' empty).\"}],\n        \"nodes\": nodes,\n    }\n\n\nout = {\n    \"pdf_page\": 125,\n    \"book_page\": 95,\n    \"verified_by\": \"claude-opus-5\",\n    \"verified_on\": \"2026-09-05\",\n    \"entries\": [entry0(), entry2()],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-125.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-05T18:39:11.678Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:39:16.745Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py && python3 -m json.tool data/verification/page-125.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 125",
 "description": "Generate and validate page-125.json"
}
```


### [2026-09-05T18:39:19.439Z] TOOL RESULT

```
written
JSON_OK
nodes verified: 14/14
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 3, 'disputed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 7, 'partial': 6, 'not_checked': 1}
books consulted: {'supports': 21, 'partial': 11, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 7, 'POK': 6, 'AHD': 6, 'SKT': 6, 'WLD': 4, 'MON': 2, 'BQT': 2, 'HRN': 2, 'LAT': 2, 'IEC': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-05T18:39:26.126Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"familia, a household\\|fr. L. familia\\|L. familia,\" WEB_vol1.txt FSD_vol2.txt 2>/dev/null | head -5; echo ---; grep -n \"familiar\" WEB_vol1.txt | head -3",
 "description": "Grep Webster/FSD for family"
}
```


### [2026-09-05T18:39:26.256Z] TOOL RESULT

```
WEB_vol1.txt:70651:fa-mil/ial (-y41), a. [from L. familia, a family.] „of, involving. or common to a family.
WEB_vol1.txt:70679:Fam/i-list, n. (L. familia, a family.]
WEB_vol1.txt:70681:2. [£-] the head of a family; a family man. [Rare.] fam/i-lis-tér-y, n. [Fr. familistère, from famil- liste, lit., one of a family, from L. familia, a family.] a community living toget as one family; also, the building in which they live. fam-i-lis’tic, fam-i-lis’tic-Al, a. pertaining to ee or ee onn T fate ‘am/ily, n.; pl. fam/i-lies, [L. familia, servants in a household, a pek er from Jamani a servant, from Oscan famel, a serw- ant. 1. the collective body of persons who live in one house. 2. a father, mother, and their children. 3. the children of same parents, 4. one's husband (or wife) and children. 5. a group of people related marriage: relatives. 6. those who descend from one common progenitor; a tribe or race; as were a branch of the family of 7. descent; Ii
---
95:Because of the general familiarity of the reading public with the diacritical markings for indicating pronunciation already in use in this dictionary, it was decided to retain this system with some minor modifications to allow for a more nearly pre- cise transcription. The pronunciations themselyes have been carefully restudied, and where some radical change, as in the stress pattern, has taken place in the prevailing pronuncia- tion, this has been recorded. Variant pronunciations have been given only where these are heard with some degree of fre- quency. Because the system of diacritical markings, based on that used by Webster, was designed to avoid, wherever possi- ble, the necessity of respelling for pronunciation, some of the diacritics have deliberately been given an elasticity that will accommodate the phonetic patterns of speakers from different parts of the country. A full pronunciation key and a guide to the pronunciation system will be found on p. xii. For the addi- tional convenience of users of this dictionary, an abbreviated —_ key has been included at the bottom of every two-page spread of the text.
188:The English language after the end of the ME. period does not lend itself to any such schematic treatment as we have attempted for Old and Middle English. The varied and flexible instrument used by Shakespeare, Milton, and, eventually, by ourselves, is altogether too gigantic to be compressed neatly into mnemonic schedules. Moreover, most of us have read the great authors of the EMnE. period and we are at least aware of the external] ap- pearance of EMnE. To proceed further, to delve beneath the spelling in order to explore the progress of the Great Vowel Shift during the 16th, 17th, 18th, and 19th centuries, would require the use of some such probe as the alphabet of the International Pho- netic Association. And even if we familiarized ourselves with some
1957:make familiar by use; to habituate or inure; as, to accustom oneself to a diet. 3
```


## [2026-09-05T18:39:35.158Z] TOOL CALL #76: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "            {\"src\": \"AHD\", \"where\": \"etymonline s.v. family (archived) as the modern statement\", \"stance\": \"supports\",\n             \"note\": \"\\\"family (n.) early 15c., 'servants of a household', from Latin familia 'family servants, domestics collectively' ... abstract noun formed from famulus 'servant, slave', which is of unknown origin.\\\" — the English chain is confirmed even though the ultimate origin is not.\"}]",
 "new_string": "            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 70681 s.v. family\", \"stance\": \"supports\",\n             \"note\": \"\\\"family, n.; pl. families, [L. familia, servants in a household, a household, from famulus, a servant, from Oscan famel, a servant.]\\\" — the Latin-to-English chain, stopping at Oscan without any Indo-European base.\"}]"
}
```


### [2026-09-05T18:39:35.217Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:39:39.942Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Deed\\.  (E\\.)\\|Deed\\.\" SKT.txt | head -4; echo ---; grep -n \"^Do\\.\\|Do,  to\\|Do\\.  (E\\.)\" SKT.txt | head -4",
 "description": "Grep Skeat Deed/Do"
}
```


### [2026-09-05T18:39:40.005Z] TOOL RESULT

```
---
21553:Do.  tt'i/j,  Dan.  vit'r,  Swed.  vis,
```


## [2026-09-05T18:39:42.989Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"DEED\" SKT.txt | head -6; echo ---; grep -n \"DHA\\b\\|(^ DHA)\\|√ DHA\\|DHA.)\" SKT.txt | head -8",
 "description": "Search Skeat deed and DHA root"
}
```


### [2026-09-05T18:39:43.058Z] TOOL RESULT

```
67:But  it  is  precisely  with  respect  to  these  Teutonic  words  that  most light  is  desired.  Even  a  school-boy  would  correctly  make  out  most of  the  derivatives  of  cede  (though  he  would  very  likely  miss  a$icesior and  decease)^  but  very  few  even  of  our  best  schokirs  could  correctly draw  up  the  list  of  words  connected  with  do^  such  as  ado,  deed,  deem, doff,  don,  doom,  dout,  dup,  indeed.  This  I  claim  to  have  done  (and  in the  main  correctly)  for  the  first  time ;  whilst  I  also  endeavour  to emphasise  the  fact  that  deem  is  derived  from  doom,  and  not  (conversely) doom  from  deem,  as  is  so  oflen  ignorantly  said  by  those  who  have  pro- bably never  even  heard  of  the  phonetic  laws  by  which  Anglo-Saxon sounds  are  regulated.
4188:deed ;  see  Pans.
4839:Deed:  ^ec  Do  (i).
4933:'   deeds   wcfift   est   with
5045:dead.  (E.)  M.  E.  deed.  A.  S.  dtdd, dead.  ^  Da.  dcod,  Dan.  dod,  Swed.  do^f, IceL  dau^r,  Goth.  dauiAs.  7*he  Goih. dnu-tfu  is  formed  with  weak  pp.  sufTtx  -/4j from  day,  pt.  t.  of  strong  \crhditoaH,  Iodic death.  (E.)  M.  E.  decth.  A.  S.  ./^rfff. •f  Du  </<V(f.  Dan.  Swed.  dod,  Iccl.  dauISi, Goih.  dauthus.  G.  /iv/.  The  Goth,  daufkut il  form(<l  with  suffix  -Mi«  from  «/««,  pt.  t. of  the  strong  verb  Jixvan,  to  die.
5253:fiu|»  truly.   (E.)     Pot  for  in [hst  t  ne  deed  i  abort).
---
9050:pk*^  Miftt«r^-(%.  kwK  ndcri  « m  W>r«i,  I  pUce.    (VDHA.)
19543:Theme.  (F.-L.-Gk.)  M.E.  ftwr- O.  K.  ttmt,  later  ihrme,  'a  theam  ;  *  Cot.— L.  thema.  —  GV.  Qi^a,  that  which  is  laid down,  a  theme  for  argument.  — Gk.  ba^ tf«-.  to  place;  ri'erj-fu,  I  place.  +S](t.  dJitt, to  put;  see  Do  U).     (VDHA.)
22408:162.  VJDHA  (-  V^A).  to  pUce.  set. «t.  do.
```


## [2026-09-05T18:39:51.262Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor s in ['Deed:  ^ec  Do  (i).','Theme.  (F.-L.-Gk.)','162.  VJDHA']:\n    L=t[:t.index(s)].count(chr(12)); print(repr(s[:20]),'leaf',L,'≈ p',L-20)\n\"",
 "description": "Skeat page numbers for Deed, Theme, root list"
}
```


### [2026-09-05T18:39:53.323Z] TOOL RESULT

```
'Deed:  ^ec  Do  (i).' leaf 134 ≈ p 114
'Theme.  (F.-L.-Gk.)' leaf 531 ≈ p 511
'162.  VJDHA' leaf 620 ≈ p 600
```


## [2026-09-05T18:40:06.871Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'PY'\nimport io\np='mk125.py'\ns=io.open(p,encoding='utf-8').read()\n\nold6 = '''            {\"src\": \"SKT\", \"where\": \"SKT.txt (Concise Etym. Dict.), s.v. Deed/Do\", \"stance\": \"supports\",\n             \"note\": \"Skeat files Deed and Do under the root DHA, the same base he gives for Family (\\\\\"(\\\\u221aDHA.)\\\\\", leaf 166 \\\\u2248 p. 146).\"}]'''\nnew6 = '''            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 134 (\\\\u2248 p. 114) s.v. Deed; root list leaf 620 (\\\\u2248 p. 600) no. 162\", \"stance\": \"supports\",\n             \"note\": \"\\\\\"Deed: see Do (1).\\\\\" and, in Skeat's list of roots, \\\\\"162. \\\\u221aDHA (= \\\\u221aDH\\\\u0112), to place, set, ... do.\\\\\" \\\\u2014 Skeat puts do/deed and the Greek \\\\u03c4\\\\u03af\\\\u03b8\\\\u03b7\\\\u03bc\\\\u03b9 family under one and the same root.\"}]'''\nassert old6 in s, 'old6'\ns = s.replace(old6, new6)\n\nold4 = '''            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 \\\\u2248 p. 511\", \"stance\": \"supports\",\n             \"note\": \"\\\\\"Thesis: see Theme.\\\\\"\"}]'''\nnew4 = '''            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 (\\\\u2248 p. 511) s.v. Theme, Thesis\", \"stance\": \"supports\",\n             \"note\": \"\\\\\"Theme. (F.-L.-Gk.) M.E. teme, O.F. tesme, later theme ... \\\\u2014 L. thema. \\\\u2014 Gk. \\\\u03b8\\\\u03ad\\\\u03bc\\\\u03b1, that which is laid down, a theme for argument. \\\\u2014 Gk. \\\\u03b8\\\\u03b5-, to place; \\\\u03c4\\\\u03af\\\\u03b8\\\\u03b7\\\\u03bc\\\\u03b9, I place. + Skt. dh\\\\u0101, to put; see Do (1). (\\\\u221aDHA.)\\\\\" and \\\\\"Thesis: see Theme.\\\\\"\"}]'''\nassert old4 in s, 'old4'\ns = s.replace(old4, new4)\nio.open(p,'w',encoding='utf-8').write(s)\nprint('ok')\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-125.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 125",
 "description": "Patch script and regenerate"
}
```


### [2026-09-05T18:40:08.966Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
AssertionError: old6
written
JSON_OK
nodes verified: 14/14
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 3, 'disputed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 7, 'partial': 6, 'not_checked': 1}
books consulted: {'supports': 21, 'partial': 11, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 7, 'POK': 6, 'SKT': 6, 'AHD': 5, 'WLD': 4, 'MON': 2, 'BQT': 2, 'HRN': 2, 'LAT': 2, 'IEC': 1, 'WEB': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-05T18:40:16.574Z] TOOL CALL #81: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "            {\"src\": \"SKT\", \"where\": \"SKT.txt (Concise Etym. Dict.), s.v. Deed/Do\", \"stance\": \"supports\",\n             \"note\": \"Skeat files Deed and Do under the root DHA, the same base he gives for Family (\\\"(√DHA.)\\\", leaf 166 ≈ p. 146).\"}]",
 "new_string": "            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 134 (≈ p. 114) s.v. Deed; Skeat's list of roots, leaf 620 (≈ p. 600) no. 162\", \"stance\": \"supports\",\n             \"note\": \"\\\"Deed: see Do (1).\\\" and \\\"162. √DHA (= √DHĒ), to place, set, ... do.\\\" — Skeat puts do/deed and the Greek τίθημι family under one and the same root.\"}]"
}
```


### [2026-09-05T18:40:16.608Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:40:22.332Z] TOOL CALL #82: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 ≈ p. 511\", \"stance\": \"supports\",\n             \"note\": \"\\\"Thesis: see Theme.\\\"\"}]",
 "new_string": "            {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 531 (≈ p. 511) s.v. Theme, Thesis\", \"stance\": \"supports\",\n             \"note\": \"\\\"Theme. (F.-L.-Gk.) M.E. teme, O.F. tesme, later theme ... — L. thema. — Gk. θέμα, that which is laid down, a theme for argument. — Gk. θε-, to place; τίθημι, I place. + Skt. dhā, to put; see Do (1). (√DHA.)\\\" and \\\"Thesis: see Theme.\\\"\"}]"
}
```


### [2026-09-05T18:40:22.360Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:40:26.026Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-125.json >/dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 125 && python3 /home/sfmqrb/git/rishe/tools/verify_archive_sources.py 2>/dev/null | tail -5",
 "description": "Regenerate and validate"
}
```


### [2026-09-05T18:40:28.859Z] TOOL RESULT

```
written
JSON_OK
nodes verified: 14/14
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 3, 'disputed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 7, 'partial': 6, 'not_checked': 1}
books consulted: {'supports': 21, 'partial': 11, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 7, 'POK': 6, 'SKT': 6, 'AHD': 5, 'WLD': 4, 'MON': 2, 'BQT': 2, 'HRN': 2, 'LAT': 2, 'IEC': 1, 'WEB': 1, 'HUB': 1, 'ARY': 1}
1066 cited URLs, 5 not yet archived
archived 5, failed 0
```


## [2026-09-05T18:40:31.755Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -3; git status --short | head -20",
 "description": "Re-check archived sources and git status"
}
```


### [2026-09-05T18:40:34.310Z] TOOL RESULT

```
1066 cited URLs, 5 not yet archived
archived 5, failed 0
?? data/verification/page-125.json
```


## [2026-09-05T18:40:39.979Z] TOOL CALL #85: Bash

```json
{
 "command": "git status --short; echo \"---untracked in web---\"; git status --short data/verification/sources/web | head; echo \"--- check gitignore ---\"; git check-ignore -v data/verification/sources/web/5f46c64056f8ef06.txt",
 "description": "Check git status details"
}
```


### [2026-09-05T18:40:41.563Z] TOOL RESULT

```
Exit code 1
?? data/verification/page-125.json
---untracked in web---
--- check gitignore ---
```


## [2026-09-05T18:40:46.058Z] TOOL CALL #86: Bash

```json
{
 "command": "ls -la data/verification/sources/web/5f46c64056f8ef06.txt data/verification/sources/web/4513ce285952339e.txt 2>&1; git log --oneline -3; cat .gitignore 2>/dev/null | head -20",
 "description": "Check web files and git log"
}
```


### [2026-09-05T18:40:46.136Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 10687 Sep  5 14:30 data/verification/sources/web/4513ce285952339e.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  7665 Sep  5 14:27 data/verification/sources/web/5f46c64056f8ef06.txt
72a5224 README: describe the verification layer
d2c7bcd Verify page 123 (Dhars/dorosht, Dhe/dayeh, daneh)
7736694 Verify page 121 (Deru 1: dar, derakht, daf, tree)
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-05T18:40:51.862Z] TOOL CALL #87: Bash

```json
{
 "command": "git ls-files --error-unmatch data/verification/sources/web/4513ce285952339e.txt 2>&1 | head -2; sed -n '1,40p' .gitignore",
 "description": "Check tracked status of web file"
}
```


### [2026-09-05T18:40:51.925Z] TOOL RESULT

```
data/verification/sources/web/4513ce285952339e.txt
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-05T18:40:57.388Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,os,hashlib\nidx={}\nfor line in open('/home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: d=json.loads(line)\n    except: continue\n    idx[d['url']]=d\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-125.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nfor u in sorted(urls):\n    print('OK ' if u in idx else 'MISS', u)\nEOF",
 "description": "Check page-125 sources are archived"
}
```


### [2026-09-05T18:40:59.069Z] TOOL RESULT

```
OK  https://abadis.ir/fatofa/%D8%A8%D9%88%D8%AA%DB%8C%DA%A9/
OK  https://abadis.ir/fatofa/%D8%AA%D8%B2/
OK  https://abadis.ir/fatofa/%D8%AA%D9%85/
OK  https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%A7%D9%86%D8%AA%D8%B2/
OK  https://en.wiktionary.org/wiki/%CF%84%CE%AE%CE%B8%CE%B7
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%AF%D9%87
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-
OK  https://en.wiktionary.org/wiki/famulus
OK  https://www.etymonline.com/word/boutique
OK  https://www.etymonline.com/word/family
```


## [2026-09-05T18:41:06.004Z] TOOL CALL #89: Bash

```json
{
 "command": "cd data/verification/sources/web && python3 - <<'EOF'\nt=open('7268d4ab7eb60974.txt',encoding='utf-8').read()\ni=t.find('Latin\\n')\nj=t.find('Etymology',i)\nprint(t[j:j+700])\nEOF",
 "description": "Read Wiktionary famulus etymology"
}
```


### [2026-09-05T18:41:08.107Z] TOOL RESULT

```
Etymology
 [ edit ] 

 From earlier famelus , from Proto-Italic *famelos ( “ slave ” ) (whence Oscan 𐌚𐌀𐌌𐌄𐌋 ( famel , “ slave ” ) ), from earlier *θamelos ; probably ultimately from Proto-Indo-European *dʰeh₁- ( “ to do, put, place ” ) . Probably as a backformation from the predecessor of familia (see there for details).

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [ˈfa.mʊ.ɫʊs] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈfaː.mu.lus] 

 Noun
 [ edit ] 

 famulus   m ( genitive famulī , feminine famula ) ; second declension 

 a servant , slave 
 ūnā cum famulō tuō, pāpā nostrō, N., together with thy servant , our Pope, N., 

 Declension
 [ edit ] 

 Second-declens
```


## [2026-09-05T18:41:20.424Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/familia\" --note \"pdf page 125, root Dhe 2 node 10: Latin familia/famulus origin\" >/dev/null && cd data/verification/sources/web && python3 - <<'EOF'\nimport hashlib\nh=hashlib.sha1(b\"https://en.wiktionary.org/wiki/familia\").hexdigest()[:16]\nt=open(h+'.txt',encoding='utf-8').read()\nprint(h)\ni=t.find('Latin\\n')\nj=t.find('Etymology',i)\nprint(t[j:j+1500])\nEOF",
 "description": "Fetch Wiktionary familia"
}
```


### [2026-09-05T18:41:22.430Z] TOOL RESULT

```
00446da837c05ca7
Etymology
 [ edit ] 

 From Proto-Italic *fameliā ( “ of the house → household ” ) , from earlier *θameliā . Further from Proto-Indo-European *dʰh₁-m-eló-m ( “ fundament ” ) , from *dʰeh₁- ( “ to do, put, place ” ) . Cognate with Sanskrit धामन् ( dhāman , “ order; dwelling-place, temple; family ” ) , Ancient Greek θεμέλιος ( themélios , “ of the foundation ” ) , θέμις ( thémis , “ justice, law ” ) . [ 1 ] 

 In view of the semantic shift illustrated in the cognates, famulus ( “ servant, slave ” ) (with Oscan 𐌚𐌀𐌌𐌄𐌋 ( famel , “ servile ” ) ) is probably a backformation from it and not the other way around.

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [faˈmɪ.li.a] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [faˈmiː.li.a] 

 Noun
 [ edit ] 

 familia   f ( genitive familiae or familiās ) ; first declension 

 a household ( all persons subject to the control of one man (whether relations , freedmen or slaves ) ) 

 the slaves of a household, servants 

 a group of slaves stationed in one place; a brigade , gang (used for some purpose)
 one's personal retinue 

 a family , kin ( a group of people closely related to one another ) 
 Synonym: domus 
 Vulgate, Genesis 10.32: Hae familiae Nōē iū̆xtā populōs et nātiōnēs suās. Ab hīs dīvīsae sunt gentēs in Terrā post dīluvium. These are the families of Noah, according to their peoples and tribes. From them split the nations on Earth after the deluge. 

 an intellectual school (e.g., of philosophy)
 Synonym: dom
```


## [2026-09-05T18:42:11.000Z] TOOL CALL #91: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "        \"id\": 10, \"lang\": \"Latin\",\n        \"words\": \"famul, famulus, familia\",\n        \"verdict\": \"disputed\",\n        \"derivation\": (\n            \"The Latin words are real — famul is the Old Latin nominative (Ennius, Ann.), famulus 'servant', \"\n            \"familia 'the household slaves, the household' — and their Italic antiquity is guaranteed by Oscan \"\n            \"famel 'famulus', Oscan famelo and Umbrian fameřias 'familia' (Festus/Paulus 77.11: 'famuli origo ab \"\n            \"Oscis dependet, apud quos servus famel nominabatur, unde et familia vocata'). But the derivation from \"\n            \"*dʰeh₁-mo- 'house' that the arrow draws is not the modern view. Ernout-Meillet (p. 383) conclude: 'Les \"\n            \"autres langues indo-européennes n'offrent aucun rapprochement. On peut se demander si le mot, dont la \"\n            \"forme n'est guère indo-européenne, n'est pas emprunté, peut-être à l'étrusque'. Etymonline (s.v. \"\n            \"family) and de Vaan likewise call famulus 'of unknown origin'. Klein, Nourai's own source, hedges with \"\n            \"'which is of uncertain origin. It possibly means...'; Walde-Pokorny with 'vielleicht mit Recht'. The \"\n            \"gloss 'belonging to the house' is likewise a guess, not an attested sense: famulus means 'servant', \"\n            \"and the -ulus looks like the agent suffix of baiulus, gerulus.\"),\n        \"derivation_fa\": (\n            \"خودِ واژه‌های لاتینی درست‌اند: famul صورتِ فاعلیِ لاتینیِ کهن (انیوس)، famulus «خدمتکار» و familia «مجموعهٔ \"\n            \"بردگان و اهلِ خانه». کهنگیِ ایتالیاییِ آن‌ها را famel اُسکی و fameřias اومبریایی تضمین می‌کند و فستوس نیز \"\n            \"می‌نویسد «famuli origo ab Oscis dependet». اما اشتقاقی که پیکانِ نمودار نشان می‌دهد، یعنی از *dʰeh₁-mo- \"\n            \"«خانه»، دیدگاهِ امروزی نیست. ارنو-مه‌یه (ص ۳۸۳) نتیجه می‌گیرند: «دیگر زبان‌های هندواروپایی هیچ همتایی \"\n            \"ندارند. می‌توان پرسید که آیا این واژه، که صورتش چندان هندواروپایی نیست، وام‌واژه — شاید از اتروسکی — \"\n            \"نباشد». اتیمانلاین و دخان نیز famulus را «با خاستگاهِ ناشناخته» می‌خوانند. خودِ کلاین هم می‌گوید «خاستگاهش \"\n            \"نامعلوم است؛ شاید به معنی ...». پس پژوهشِ امروزی ادعای نورایی را رد می‌کند و famulus را واژه‌ای ایتالیایی \"\n            \"با خاستگاهِ ناشناخته (احتمالاً اتروسکی) می‌داند.\"),\n        \"sources\": [E_FAM, W_FAM],",
 "new_string": "        \"id\": 10, \"lang\": \"Latin\",\n        \"words\": \"famul, famulus, familia\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\n            \"The Latin words are real — famul is the Old Latin nominative (Ennius), famulus 'servant', familia \"\n            \"'the household slaves, the household' — and their Italic antiquity is guaranteed by Oscan famel \"\n            \"'famulus', Bantine famelo and Umbrian fameřias 'familia' (Festus/Paulus 77.11: 'famuli origo ab Oscis \"\n            \"dependet, apud quos servus famel nominabatur, unde et familia vocata'). The link to *dʰeh₁- is \"\n            \"genuinely defended but not agreed. For it: Walde-Pokorny I 828 ('vielleicht mit Recht'), Klein \"\n            \"(Nourai's source, 'possibly'), Skeat, and Wiktionary, which reconstructs familia < Proto-Italic \"\n            \"*fameliā < *θameliā < PIE *dʰh₁-m-eló-m 'fundament', cognate with Skt dhāman and Gk θεμέλιος, θέμις. \"\n            \"Against it: Ernout-Meillet (p. 383) — 'Les autres langues indo-européennes n'offrent aucun \"\n            \"rapprochement. On peut se demander si le mot, dont la forme n'est guère indo-européenne, n'est pas \"\n            \"emprunté, peut-être à l'étrusque' — and Etymonline and de Vaan, who call famulus 'of unknown origin'. \"\n            \"One detail of the chart is wrong even on the favourable account: Nourai (after Klein) derives familia \"\n            \"from famulus, while Wiktionary argues the reverse, 'famulus is probably a backformation from it and \"\n            \"not the other way around', since only familia carries the 'household' semantics the root would give. \"\n            \"The gloss 'belonging to the house' is a reconstruction, not an attested sense of famulus, which means \"\n            \"simply 'servant' and whose -ulus looks like the agent suffix of baiulus, gerulus.\"),\n        \"derivation_fa\": (\n            \"خودِ واژه‌های لاتینی درست‌اند: famul صورتِ فاعلیِ لاتینیِ کهن (انیوس)، famulus «خدمتکار» و familia «مجموعهٔ \"\n            \"بردگان و اهلِ خانه». کهنگیِ ایتالیاییِ آن‌ها را famel اُسکی و fameřias اومبریایی تضمین می‌کند و فستوس نیز \"\n            \"می‌نویسد «famuli origo ab Oscis dependet». پیوند با ریشهٔ *dʰeh₁- را برخی می‌پذیرند و برخی نه. در سوی \"\n            \"پذیرش: والده-پوکورنی (جلد ۱، ص ۸۲۸) با قیدِ «شاید به‌درستی»، کلاین (مأخذِ نورایی) با قیدِ «احتمالاً»، \"\n            \"اسکیت، و ویکی‌واژه که familia را از ایتالیاییِ آغازینِ *fameliā و آن را از *dʰh₁-m-eló-m «بنیاد» \"\n            \"بازسازی می‌کند و هم‌ریشه با dhāman سنسکریت و θεμέλιος و θέμις یونانی می‌داند. در سوی رد: ارنو-مه‌یه \"\n            \"(ص ۳۸۳) می‌نویسند «دیگر زبان‌های هندواروپایی هیچ همتایی ندارند؛ می‌توان پرسید که آیا این واژه، که صورتش \"\n            \"چندان هندواروپایی نیست، وام‌واژه — شاید از اتروسکی — نباشد»، و اتیمانلاین و دخان نیز آن را «با خاستگاهِ \"\n            \"ناشناخته» می‌خوانند. یک نکتهٔ نمودار حتی در روایتِ موافق هم نادرست است: نورایی به پیروی از کلاین familia \"\n            \"را از famulus می‌گیرد، حال آنکه ویکی‌واژه عکسِ آن را می‌گوید و famulus را ساختِ قهقراییِ familia می‌داند. \"\n            \"پس این گره با احتیاط پذیرفتنی است.\"),\n        \"sources\": [E_FAM, W_FAM, W_FAMILIA],"
}
```


### [2026-09-05T18:42:11.040Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:42:26.340Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'PY'\nimport io\np='mk125.py'; s=io.open(p,encoding='utf-8').read()\n\ns = s.replace('W_FAM   = \"https://en.wiktionary.org/wiki/famulus\"',\n              'W_FAM   = \"https://en.wiktionary.org/wiki/famulus\"\\nW_FAMILIA = \"https://en.wiktionary.org/wiki/familia\"',1)\n\n# node 10: add a Wiktionary consulted entry (as a web source under LAT-adjacent slot is wrong; append to its consulted list)\nold = '''            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, dhē-¹ (leaf 42) and index\", \"stance\": \"silent\",\n             \"note\": \"Watkins lists no FAMILY/FAMULUS under dhē-¹ (nor under any root); grep 'famul' returns nothing.\"}]'''\nnew = '''            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, dhē-¹ (leaf 42) and index\", \"stance\": \"silent\",\n             \"note\": \"Watkins lists no FAMILY/FAMULUS under dhē-¹ (nor under any root); grep 'famul' returns nothing.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 70681 s.v. family\", \"stance\": \"partial\",\n             \"note\": \"\\\\\"[L. familia, servants in a household, a household, from famulus, a servant, from Oscan famel, a servant.]\\\\\" — Webster stops at Oscan and offers no Indo-European base, i.e. neither confirms nor denies Klein's *dhē-mo-.\"}]'''\nassert old in s\ns = s.replace(old, new, 1)\n\n# entry note: soften the famulus judgement\noldn = \"and the whole Dhē-mo/famulus sub-tree (nodes 9-12) rests on Klein's \\\"\\n            \\\"hedged guess, which Ernout-Meillet and current Latin etymology reject.\\\")\"\nnewn = \"and the whole Dhē-mo/famulus sub-tree (nodes 9-12) rests on Klein's \\\"\\n            \\\"hedged guess — defended today by Wiktionary (familia < *dʰh₁-m-eló-m) but rejected by Ernout-Meillet \\\"\\n            \\\"and de Vaan, who call famulus a word of unknown, possibly Etruscan origin; and its Sanskrit box is \\\"\\n            \\\"drawn as a descendant of Latin, which it cannot be.\\\")\"\nassert oldn in s\ns = s.replace(oldn, newn, 1)\n\noldfa = \"«خانه») استوار است که ارنو-مه‌یه و ریشه‌شناسیِ لاتینیِ امروز آن را نمی‌پذیرند.\\\")\"\nif oldfa not in s:\n    # find the fa sentence\n    import re\n    print([x for x in s.split('\\n') if 'ارنو-مه‌یه و ریشه' in x])\nio.open(p,'w',encoding='utf-8').write(s)\nprint('ok')\nPY",
 "description": "Patch script for Wiktionary familia and entry note"
}
```


### [2026-09-05T18:42:28.061Z] TOOL RESULT

```
['            "۹ تا ۱۲) بر حدسِ محتاطانهٔ کلاین استوار است که ارنو-مه\u200cیه و ریشه\u200cشناسیِ لاتینیِ امروز آن را نمی\u200cپذیرند."),']
ok
```


## [2026-09-05T18:42:37.707Z] TOOL CALL #93: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "            \"۹ تا ۱۲) بر حدسِ محتاطانهٔ کلاین استوار است که ارنو-مه‌یه و ریشه‌شناسیِ لاتینیِ امروز آن را نمی‌پذیرند.\"),",
 "new_string": "            \"۹ تا ۱۲) بر حدسِ محتاطانهٔ کلاین استوار است — حدسی که ویکی‌واژه امروز هم از آن دفاع می‌کند (familia از \"\n            \"*dʰh₁-m-eló-m) اما ارنو-مه‌یه و دخان آن را رد می‌کنند و famulus را واژه‌ای با خاستگاهِ ناشناخته و شاید \"\n            \"اتروسکی می‌دانند؛ افزون بر این، جعبهٔ سنسکریتِ آن زیرِ لاتین کشیده شده است که ناممکن است.\"),"
}
```


### [2026-09-05T18:42:37.743Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:42:44.571Z] TOOL CALL #94: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py",
 "old_string": "            \"through the Sanskrit and Greek forms, not reconstructible as a PIE word for 'house' (that is *domos, a \"\n            \"different root, *dem-).\"),",
 "new_string": "            \"through the Sanskrit and Greek forms, not reconstructible as a PIE word for 'house' (that is *domos, a \"\n            \"different root, *dem-). Wiktionary, which does accept the Italic connection, reconstructs it \"\n            \"differently again, as *dʰh₁-m-eló-m 'fundament' behind familia, cognate with Skt dhāman and Gk \"\n            \"θεμέλιος 'of the foundation', θέμις 'law'.\"),"
}
```


### [2026-09-05T18:42:44.608Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-05T18:42:59.518Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'PY'\nimport io\np='mk125.py'; s=io.open(p,encoding='utf-8').read()\n\n# node 9 fa: append the Wiktionary reconstruction\noldfa = \"\\\"دیگری است (*domos از ریشهٔ *dem-). پس با احتیاط پذیرفتنی است.\\\"),\"\nnewfa = \"\\\"دیگری است (*domos از ریشهٔ *dem-). ویکی‌واژه نیز که پیوندِ ایتالیایی را می‌پذیرد، بازسازیِ دیگری می‌دهد: \\\"\\n            \\\"*dʰh₁-m-eló-m «بنیاد» در پسِ familia، هم‌ریشه با dhāman سنسکریت و θεμέλιος و θέμις یونانی. پس این گره \\\"\\n            \\\"با احتیاط پذیرفتنی است.\\\"),\"\nassert oldfa in s; s = s.replace(oldfa, newfa, 1)\n\n# node 9 sources\nold = '\"sources\": [W_PIE, W_FAM],\\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"supports\",'\nnew = '\"sources\": [W_PIE, W_FAM, W_FAMILIA],\\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"supports\",'\nassert old in s; s = s.replace(old, new, 1)\n\n# node 12: mention Wiktionary cognate status\nold12 = '\"abbreviation of Monier-Williams\\' \\'dwelling-place, house, abode\\'.\")'\nnew12 = '\"abbreviation of Monier-Williams\\' \\'dwelling-place, house, abode\\'. Wiktionary s.v. familia names Sanskrit \\\"\\n            \"धामन् (dhāman) as a cognate of the Latin word, i.e. a sister form, never its child.\")'\nassert old12 in s; s = s.replace(old12, new12, 1)\n\nold12s = '\"sources\": [W_PIE],\\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"partial\",'\nnew12s = '\"sources\": [W_PIE, W_FAMILIA],\\n        \"ref_check\": [{\"ref\": \"KLN:573\", \"status\": \"partial\",'\nassert old12s in s; s = s.replace(old12s, new12s, 1)\n\n# entry-level sources\nolde = '\"sources\": [W_PIE, E_BOUT, E_FAM, W_FAM],'\nnewe = '\"sources\": [W_PIE, E_BOUT, E_FAM, W_FAM, W_FAMILIA],'\nassert olde in s; s = s.replace(olde, newe, 1)\nio.open(p,'w',encoding='utf-8').write(s); print('ok')\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk125.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-125.json >/dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 125",
 "description": "Apply remaining patches and regenerate"
}
```


### [2026-09-05T18:43:01.521Z] TOOL RESULT

```
ok
written
JSON_OK
nodes verified: 14/14
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 4, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 7, 'partial': 6, 'not_checked': 1}
books consulted: {'supports': 21, 'partial': 12, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 7, 'POK': 6, 'SKT': 6, 'AHD': 5, 'WLD': 4, 'MON': 2, 'BQT': 2, 'HRN': 2, 'LAT': 2, 'WEB': 2, 'IEC': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-05T18:43:06.261Z] TOOL CALL #96: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -2 && python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-125.json'))\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: idx.add(json.loads(line)['url'])\n    except: pass\nurls=set()\ndef w(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: w(v)\n    elif isinstance(o,list):\n        for x in o: w(x)\nw(d)\nprint('missing:', [u for u in urls if u not in idx])\nprint('nodes:', sum(len(e['nodes']) for e in d['entries']))\nEOF",
 "description": "Final source archive verification"
}
```


### [2026-09-05T18:43:08.772Z] TOOL RESULT

```
1067 cited URLs, 5 not yet archived
archived 5, failed 0
missing: []
nodes: 14
```


## [2026-09-05T18:43:27.710Z] AGENT

Done. `data/verification/page-125.json` written; `verify_check.py 125` reports **0 PROBLEM lines** (14/14 nodes, 2 roots).

**Page 125 (book p. 95) — verdicts**
- Roots: 1 confirmed (Dhě 2), 1 plausible (Dhedh 2). Redirects Dhědh / Dhegh / Dhehem skipped.
- Nodes: 7 confirmed, 4 plausible, 1 disputed, 2 transcription_suspect.
- Ref checks: 7 supports, 6 partial, 1 not_checked. Books consulted: KLN, POK, SKT, AHD, WLD, LAT, WEB, MON, BQT, HRN, HUB, IEC, ARY.

**Flagged items**
- `transcription_suspect` #2 French "botica / paranthese, these, theme" — **error in the book**: `botica` is Old Provençal (Klein, Etymonline), not French, and means "shop/storehouse", not "gift store"; `paranthese` is a misprint for *parenthèse*. The 900-dpi scan confirms the page prints both that way.
- `transcription_suspect` #3 Persian — **extraction error, owner should fix**: JSON has `«تیم ، تز»`; the printed page shows **`«تِم ، تِز»`** (kasra misread as yā). Mo'in confirms تِم [فر.] "موضوع اساسی، مایه". Also, Nourai's gloss "gift store" for بوتیک is off (Mo'in: a clothes/shoes/perfume shop).
- `disputed` #12 Sanskrit `dhâman` — the word is genuine (*dʰeh₁-mn̥*, RV), but the page draws the arrow from the **Latin** box (the curve leaves the Latin box's bottom-left corner, so the extraction's `parent 10` is faithful). Sanskrit dhāman cannot descend from Latin famulus; Klein, the source of the sub-tree, lists it only as a cognate. The arrow should start at node 9.
- `plausible` #9/#10 (*Dhē-mo* → famul/famulus/familia): defended by Klein ("possibly"), Walde-Pokorny ("vielleicht mit Recht"), Skeat and Wiktionary (*familia < *dʰh₁-m-eló-m*), but Ernout-Meillet p. 383, Etymonline and de Vaan call famulus of unknown, possibly Etruscan origin. Wiktionary also reverses Nourai's direction: famulus is a back-formation from familia.
- `plausible` entry 2 (Dhedh 2 "nurse"): IEC:178 is verbatim Nourai's node — but Mann himself writes "(alleged) téthe 'nurse'"; Pokorny 235 and Wiktionary call the reduplication a nursery Lallwort meaning "grandparent", and Mo'in tags the Persian cognate دادا as **Turkish** [تر.].

**Reference-page findings**: POK:235 exact (both roots sit on Pokorny p. 235); KLN:573 exact (leaf 310 = pp. 572-573); IEC:178 exact (leaf 111 carries printed 178/179). AHD:1512 / 156,1334 could not be page-checked (1975 New College printing is lending-only) but the content is fully in Watkins' `dhē-¹`. MON page numbers belong to the 6-vol. Amir Kabir edition not on disk; entries verified via Mo'in on abadis.ir instead.

10 web sources archived via `fetch_source.py`; page scan copied to `data/verification/sources/refs/ocr/BOOK/125.png`.
