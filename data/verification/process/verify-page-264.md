# Verification process log — verify-page-264


## [2026-09-06T20:34:20.761Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 264 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-264.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-264.json. Write /home/sfmqrb/git/rishe/data/verification/page-264.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 264` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:34:22.443Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:34:23.048Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:34:23.062Z] TOOL RESULT

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


## [2026-09-06T20:34:23.178Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-264.txt"
}
```


### [2026-09-06T20:34:23.204Z] TOOL RESULT

```
1	=== PDF page 264 (book page 234) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Keu 4, Keu-bh : to shine, bright  (refs POK:594)
4	#1 (parent #0) [Avestan] refs=POK:594; BRT:221,1631; SYN:995 | sŭr, savah 2 : morning ; sŭram : early morning ; a-sŭr : not (yet) morning, dawn ☞Ne 1 ; sŭirya : breakfast ; savahî : the East
5	  #2 (parent #1) [Pahlavi] refs=HRN:166 | sŭr : breakfast, meal, festivity
6	    #3 (parent #2) [Persian] refs=BQT:1185; HRN:237 | sŭr «سور» : festivity, party ; sŭrnâ «سورنا، سورنای» : a horn played at festivities ☞Nedo
7	#4 (parent #0) [Old Persian] refs=POK:594 | caune : bright red, a plant with bright colored fruits
8	  #5 (parent #4) [None] refs=None | 
9	--- entry 1 ---
10	ROOT Kěu 5 -> redirect to Kǔ 1
11	--- entry 2 ---
12	ROOT Keub -> redirect to Gěu 1
13	--- entry 3 ---
14	ROOT Keu-bh -> redirect to Keu 4
15	--- entry 4 ---
16	ROOT Keud -> redirect to Keued
17	--- entry 5 ---
18	ROOT [Indo-European] Keued, Keud, Qeud, Skeud 2 : to yell  (refs POK:595)
19	#1 (parent #0) [Persian] refs=POK:595; WLD1:378; HUB:102 | nekŭkîdan «نکوهیدن» : to blame | extra: نکوهش
20	#2 (parent #0) [Sanskrit] refs=POK:595 | kutsa : blame
21	#3 (parent #0) [Middle English] refs=POK:596; SYN:1251 | sčŭten : to yell
22	  #4 (parent #3) [English] refs=None | shout
23	
```


## [2026-09-06T20:34:31.063Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-264.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T20:34:31.149Z] TOOL RESULT

```
{
  "pdf_page": 264,
  "book_page": 234,
  "entries": [
    {
      "root": {
        "name": "Keu 4, Keu-bh",
        "lang": "Indo-European",
        "refs": "POK:594",
        "gloss": "to shine, bright"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:594; BRT:221,1631; SYN:995",
          "words": [
            {"translit": "sŭr, savah 2", "gloss": "morning", "script": null},
            {"translit": "sŭram", "gloss": "early morning", "script": null},
            {"translit": "a-sŭr", "gloss": "not (yet) morning, dawn", "script": null, "see": ["Ne 1"]},
            {"translit": "sŭirya", "gloss": "breakfast", "script": null},
            {"translit": "savahî", "gloss": "the East", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:166",
          "words": [
            {"translit": "sŭr", "gloss": "breakfast, meal, festivity", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1185; HRN:237",
          "words": [
            {"translit": "sŭr", "gloss": "festivity, party", "script": "سور"},
            {"translit": "sŭrnâ", "gloss": "a horn played at festivities", "script": "سورنا، سورنای", "see": ["Nedo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:594",
          "words": [
            {"translit": "caune", "gloss": "bright red, a plant with bright colored fruits", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kěu 5",
        "redirect": "Kǔ 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keub",
        "redirect": "Gěu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keu-bh",
        "redirect": "Keu 4"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keud",
        "redirect": "Keued"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keued, Keud, Qeud, Skeud 2",
        "lang": "Indo-European",
        "refs": "POK:595",
        "gloss": "to yell"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:595; WLD1:378; HUB:102",
          "words": [
            {"translit": "nekŭkîdan", "gloss": "to blame", "script": "نکوهیدن"}
          ],
          "script_extra": "نکوهش",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:595",
          "words": [
            {"translit": "kutsa", "gloss": "blame", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Middle English",
          "refs": "POK:596; SYN:1251",
          "words": [
            {"translit": "sčŭten", "gloss": "to yell", "script": null}
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
            {"translit": "shout", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
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


## [2026-09-06T20:34:32.949Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BRT','SYN','HRN','BQT','WLD','WLD1','HUB','MON','PHD','NYB','AHD','KLN','ARY','IEC','CHEUNG','SKT','WEB','FSD','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T20:34:35.177Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
WLD1 MISSING
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
CHEUNG MISSING
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-06T20:34:52.266Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls POK* && for f in POK_full.txt; do echo \"== $f\"; grep -n \"594\\|595\\|596\" $f | head -40; done"
}
```


## [2026-09-06T20:34:53.471Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"k̑eu-2\\|keu-2\\|k̑eu\\b\" POK_full.txt | head -30; echo \"---kutsa---\"; grep -n \"kutsa\" POK_full.txt | head -20; echo \"---sūra morgend---\"; grep -n \"morgendlich\" POK_full.txt | head -20"
}
```


### [2026-09-06T20:34:54.371Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
== POK_full.txt
6599:gall. PN. Ario-manus{Q\\-, III 4594); Irish aire{Q\. primas) besides airech, where is to be 
6694:stands dpi- " very much, very ' in compounds, wherewith Reuter KZ. 31, 594a 1 also Old 
17379:deRrp-to-sxn gr. Sekqtoc; (see also Schwyzer Gr. Gr. I 595); Gothic tafhunda. Old Norse 
19475:References: WP. I 778 ff., WH. I 378 f., 861, Schwyzer Gr. Gr. I 348, 595, 685. 
21456:("mortal, human being', Brugmann ZfceltPh. 3, 595 ff.); s. also under ghdem-, 
29665:References: WP. I 537 f., WH. I 143 f., Trautmann 77; different MiJhlenbach-Endzelin I 596 
29807:carafe, glass bottle, jar, pitcher, vase ', s. Meyer-LiJbke 1596, Gamillscheg EWb. d. Franz. 
35602:References: WP. I 609 f., WH. I 594, 596, Loth RC 40, 375 f. 
46658:Page(s): 595-596 
47062:Page(s): 596-597 
50806:Page(s): 595 
50942:Page(s): 592-594 
50991:Page(s): 594-595 
51115:Page(s): 595 
51133:Page(s): 595 
51993:Note: probably extension from Reu-, S. 594 f. 
52324:See also: derivative from the color root Rehu-2, S. 594. 
59130:groin, loins'; different Muhlenbach-Endzelin II 596 (from *meldm- to S. 718); 
75342:References: WP. II 596, Trautmann 264 f.; 
76633:See also: compare also keuod- above S. 595 f. 
81040:References: WP. II 610 f., WH. II 595; 
81796:References: WP. II 643, WH. I 755 f., 769 f., 772 f., II 596, Trautmann 286, Vasmer 3, 10; 
82492:References: WP. II 627 ff., WH. II 595, 601 f., 606 f., 692, Trautmann 284 f., 325, Vasmer 
83465:References: WP. I 215, II 517 f., WH. II 531 f., Vasmer2, 594 f. 
84138:References: WP. II 529 f., Trautmann 295, Vasmer 2, 589, 596 f. 
90447:References: WP. I 298; Frisk 493; different MiJhlenbach-Endzelin IV 534, 596. 
92778:Latin vapor{o\d vapos) "vapor, heat' sein (incorrect about vaporabove S. 596), wherefore 
92824:References: WP. 1311, Vasmer 1 , 191 f.. Frisk 594 f.
```


### [2026-09-06T20:34:54.453Z] TOOL RESULT

```
31761:lemma: (s)keu-2, (s)keua : (s)ku- : to cover, wrap 
43677:Old High German /7Ji75 "bonnet' etc. (compare keu-2) respective words; Cretan Kucpspov n 
46749:Root / lemma: keu-2, keua- 
76692:Root / lemma: (s)keu-2, (s)keu9 : (s)ku- 
---kutsa---
46627:Material: Old Indie kutsayati^ blasphemes, reproves ', kutsa^ abuse, reprimand ', npers. 
---sūra morgend---
```


## [2026-09-06T20:34:58.292Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46590,46680p' POK_full.txt"
}
```


## [2026-09-06T20:34:58.306Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46680,46800p' POK_full.txt"
}
```


### [2026-09-06T20:34:58.362Z] TOOL RESULT

```
ks-es-\n: gr. ^eoj {*ks-es-d), Aor. ^taoai "scrape, smooth', ^sarot; " scraped '; common 
Old Indie gh- > ks- : Avestan gh- > gz-, z- : gr. z- 

ks-eu-\^: 

Old Indie ksura-xw. " shearing knife, thorn plant '; npers. sor^ salty ', Kurdish sur6s.\ 
common Old Indie gh- > ks- 

Note: 

The inanimate suffix -ur- : Old Indie ksura- m. " shearing knife, thorn plant ' : 'lAAOpioi , oi, 
lllyrians, 'lAAupia , n, lllyria, also'lAAupi? , n. Adj. 'lAAupiKO? , n, 6v, lllyrian: -Kr|, the region 
or province of lllyria, UAupi^U) , speak the lllyrian language, 'IAAupla:-hence Adv. 
lAAupiaTi. 

gr. ^uu) ' scrape, rub, smooth ', participle ^ugto^ ' scraped, smoothed ', -6v "(smooth) 
spear shaft', ^uapa " scrapings ', ^uarpa "currycomb', ^uarrip " rasper', ^upov (: Old Indie 
ksura-) " shearing knife ', ^upov Topov, iaxvov, o^u Hes.; ^oavov ( *ks-ou-enom) " image 
carved of wood, image, statue, esp. of a god ' common Old Indie gh- > ks- : Avestan gh- > 
gz-, z- : gr. z- 

gr. ^cbarpa HJr|KTpi(;, HJnKTpia Hes. ("currycomb '), rather with ksdfuj-\r\ere, as with *ksds- 
to root form ks-es-, 

here probably with metathesis Baltic *skuud' shave ' in Latvian skuvu, skut, Lithuanian 
skutu, skust/ ds. 

References: WP. I 449 ff., WH. I 178 f., Trautmann 119 f., 268, Specht Indo Germanic 
Dekl. 239, 250, Kuiper Nasalpras. 85^. 
Page(s): 585-586 

Root / lemma: keuad- kud- 
Meaning: to cry 

Material: Old Indie kutsayati^ blasphemes, reproves ', kutsa^ abuse, reprimand ', npers. 
nikOhTdan^rebxAe, vilify, scold'; 

gr. Ku5a^u), -o\xa\ " abuse, revile, scold ', KuSayxaq |jaxa(;, ko\bo^\ac, Hes., KuSayxoiJSva 
Aoi5opouM£va Hes.; from a stem ku5oi- : KuSoiiJoq " din of battle, uproar, hubbub ', 
Ku5oi[j£Tv " make an uproar, spread confusion ', ku5oi-5ottc(v ds.; 



agutn. huta^ send for, call out to, summon ', Norwegian dial, huta^ shout, make a noise, 
at a dog shout threateningly, contemptuously treat ' (Middle English huten, hoten, nengl. to 
/70o/'cry, make a sound like the cry of an owl ' from Old Norse /7d/a 'threaten'); 

Maybe alb. huta' owl'. 

Old English husc{*kud-sko-),0\6 High German Old Saxon hose {*kud-sko-) " abuse, 
derision, ridicule'. Old English hosp^ disgrace, shame, insult', hyspan^ mock ' (with -sp- 
suffix). Middle High German hiuze' cheeky, alert, awake, smart', hiuzen^ sich erfrechen ' 
("*shout challengingly '), gehiuze, gehuze^ din, clamor, derision, ridicule', hiuzen, huzen^ 
shout to the pursuit ' (in addition the Interj. hussa?); 

with aniaut. s- (previously after schallen, schreienl) perhaps Middle English schuten^ 
cry out, shout, bawl, exclaim ', engl. to shout^ cry loudly ', Old Icelandic skOta, skutT 
derision, gibe '; 

Old Bulgarian kuzdg, kuditT ruin ', Church Slavic also "vilify, scold, rebuke', russ. 
prokuditb " make bad pranks, play practical joke ', kudbi. " black art, black magic, 
witchcraft ', Serbo-Croatian kudJm, -///'rebuke, slander', poln. dial, prze-, przy-kudzic 
'spoil, tire, bore '. 

References: WP. I 378 f. 
Page(s): 595-596 

Root / lemma: keu-1, skeu-, lengthened grade keu- 

Meaning: to notice, observe, feel; to hear 

Note: heavy basis koua-\ s-extension keu-s-, about forms with aniaut. 5-s. at the end; 

Ao^o-5'sorgsam'; ctextension keud-\ kud- in keudos : kudos iame' . 

Material: 1. Old Indie kavf- 'smart, wise; seer, bard', kavarf-^ selfish; penurious ', a-kava- 

'not stingy'; a-kuvate^ intentional, deliberate ', a-kuta-v\., a-kuti-i. ' intention'; 

Avestan cov/sn. Sg. Med. Aor. ' ich erhoffte, versah myself; 

gr. koecjo ' mark, perceive, hear' (Denomin. from *kouos, = Latin caved); *koFo(; placed 
in Ionic-Attic avoKux; exeiv ' carefully, look well to a thing, give good heed to it '; Doric 
£KOC(|j£(; HKOuaapsv Hes.; Koir|<;, K0i6Ar|<; i£p£U(;; koTov, kojiov svsxupov; Koua, Kwa svsxupa 
Hes.; maked. Koioq 'number'; PN Aao-K6(F)u)v, Aao-Kowaa, etc.; ku5oc; n. 'fame' (see 
below to Slavic cudo);
```


### [2026-09-06T20:34:58.369Z] TOOL RESULT

```
from the basis keu-s-: aKouw "hear' (*aKouqi(jo), aKori, horn. aKoun " ear, hearing ' 
(*aKOuaa), unriKOOc; ' hearkening, answering with both gifts, a hearer, scholar, obeying, 
subject ', lak. EiraKOoq ' witness, testifier ', qkeusi iripeT Hes., gort. aK£uovTO(; (with old e- 
Vok., during qkouu) depends from *aKOuaa:); about Ku5og see below; 

QKOuu) ' hear, understand ' etc. at first related to Gothic hausjaneic, see below; d- is 
barely = /7'in', but = a- ( 77a-KOuhiu), *ha-K£uh(ji)) through breath dissimilation, or Indo 
Germanic s/77- 'together'; different above S. 18, whereas oksuu) ablaut formation would 
have to be kept away what is not likely; 

Latin caved, -ere^ to be on one's guard, take care, take heed, beware, guard against, 
avoid ' ( *covere, Denom. from *kouos), cautus " careful ', Umbrian kutef " careful '; 

Maybe alb. {*koutos) kujtoj^ mark, perceive, remember'. 

Gothic hausjan. Old Icelandic heyra. Old English hTeran, Old Saxon horian. Old High 
German horfrjen 'hear' (see above); lengthened gradees *keu-\n Old English hawian 
"see, show'; 

Latvian kavet{: Latin cavere) " vacillate, hesitate'; 

wruss. s-kuma-ju, -c' understand, comprehend ', Czech koumati, s-koumatT mark, 
perceive, hear, become aware' (denominative a (s)kou-mo-, -ma)\ Old Bulgarian cujg, cuti 
" feel, mark, perceive, hear ', serb. cujem cuti'heax, feel ' (etc.; *keu-)\ 

Old Bulgarian cudo, -ese 'wonder, miracle', cuditi s§' to wonder at, be surprised ' {*keu- 
dos, changing through ablaut:) 

Maybe alb. f^oV "wonder, miracle, surprise', guditem' to wonder at, be surprised ' a Slavic 
loanword, common Slavic alb. c >q. 

gr. k05o^ "fame, honour', kuSigtoc; " most honoured, noblest '; 

serb. cuvat/' beware, guard'; proto Slavic *cevg, *ceviti\r\ Old Czech vs-cieviti, na-vs- 
cieviti, nowadays navstfviti' call, visit '. 

Maybe alb. gohem' get up, wake up', goj' send' Slavic loanwords, common Slavic alb. c > 
?■ 

keu-s-\r\ russ. dial, cuchatb 'percewe, hear', sloven, cuha-m, -//"feel, foresee, predict ', 
Czech c/ic/7 "sense, mind, scent, spoor'; compare above to qkouw. 



2. With initial sound s-: 

miran. skoh, np. s/koh, 5^/rd/7(Proto- Iranian *skaua^a-) " splendor, glory, magnificence, 
majesty, stateliness '; Armenian cucanem^ allow to look, point, show ' coyc^ pointing, 
show ' {skeu-sRd); 

gr. GuoGKOOc; " sacrificing priest ' from gr. Guoa "a sacrifice, offering'; 

Gothic us-skaws'i* looking out =) prudent, cautious, careful ', Old English sceawian. 
Old Saxon skauwon. Old High German scouwon "see, show'; Old Icelandic skygn ' seeing 
', skygg/nn 'c\ear, bright' {*skuvvini-), whereoi skygna^ peer'; Gothic s/r5^/7s "beautiful' 
{ibna-skauns^ from the same figure '), Old High German scon/ 6s., Old Icelandic skjoni. 
Old Saxon s/ro/7/"gleaming, beautiful'. Old English saencds. (actually "conspicuous'); zero 
grade *sku-n/-\n Old Icelandic skyni. n. "order, information, message, discernment', 
skynja^ examine, understand, comprehend '; Old Icelandic skoda^ peer'; 

Maybe alb. shquaf perceive, distinguish '. 

Old Prussian au-schaudTtwei^\xus{\ 

References: WP. I 368 ff., WH. I 186 f., Trautmann 132. 
Page(s): 587-588 

Root / lemma: keu-2, keua- 

Meaning: to bend 

Note: Numerous parallel formations from the root geu-see there, compare esp. the 

confrontations by Persson Beitr. 1 00 f., 1 04 Anm. 1 . - About the attempt of a mediation 

with fsjkeu-' cover' see there. 

Material: The f. root in Old Indie kora- m. " movable joint '; Avestan fra-, apa-kava- " vorn, 

^inten buckelig '; kir. ku//ty' shrink up, before coldness', poln. ku//c'pu\\ together, crook'. 

Also the prehistory from Latvian kuza "craw, goiter ' and such is not to be judged 
because of the rhyme relation to guza etc. not certain, see below ^e^- "bend' above S. 
395. 

Under an initial sound variation A/? Petersson KZ. 47, 277 here will place Old Indie 
kho/aka-' ant heap ' (also Lithuanian kulys^ bundle straw'), more confidently Armenian 
xoyi. Gen. xuli^ a scrofulous tumor, swollen gland, struma, scrofula, tuberculosis of the 
lymph glands of the neck ', russ. s^^a/a "testicles', serb. suljevi' golden vein'. 



Maybe alb. kule^ hernia' = Armenian xoyi. Gen. xuir swollen gland ', alb. kulpra, kulper 
"bendable ivy, clematis ' = {*kupra) thupra, thuper^ twig, rod' see below. 

Maybe alb. per-kul, perkur bend'. 

A. Dental extension (redupl.) ka-ku-cf- 0\d Indie kakud-' summit, acme, apex ', kakuc/-' 
oral cavity, palate', kakudmant-' provide with a summit or hump '; Latin cacumen^cusp, 
peak, acme, apex ' (the men- further formations probably after acumen), basic meaning " 
bulge '; in Germanic *hagu= Old Indie kakud- one introduces also Old Frisian /7e//a'head' 
back ( *hagila-, with suffix change for hagu-la-)\ compare also Old Indie kakubh- " acme, 
apex ' under "labial extensions'. 

B. guttural extensions. 

B. I. keu-g-: 

Old Icelandic huka " cower, cringe, crouch ' {hukta, stem participle hokinn), hoka, hokra 
" grovel, truckle, creep ', h0ykiask^s\v\k down, creep together'. Middle High German 
huchen^ cower, cringe, crouch ', Modern High German hocken; Swiss hockrw. 'heap', 
Tirol hockenm. "heap of hay', with aniaut. 5- Middle High German schochem. " stacked 
heap of hay ', (with kk.) asachs. skokm. "60 pieces'. Middle High German schoc(kes) 
"heap tussock, number of 60 pieces ', Middle English shock^ heap sheaves (12 - 16)'; 
about Schochs. lastly Sommer " Zum Zahlwort ', S. 78 ff., S.-B. Bayr. Akad. 1950, Heft 7; 

Lithuanian kauge, ablaut, kiugis^ hay heap ', Old Prussian kugis^ Knauf am 
Schwertgriff ', Lithuanian kaugure^ small precipitous hill ', Latvian kaudze^heap, barn, 
haystack' (and skaudze).
```


## [2026-09-06T20:35:10.085Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50930,51160p' POK_full.txt"
}
```


### [2026-09-06T20:35:10.142Z] TOOL RESULT

```
sau//s{0\6 Lithuanian) "hip, haunch', suka' haycock on the field ', susn/s' heap', sut/'s' 
woodpile ', sut/'s "heap of stone or wood '??); 

Maybe alb. suke'hWV. (in PIE word and hill are of the same origin). 

Old Bulgarian sujb' void, vain'; compare Buga Kalba ir. sen. I 291. 

A root form Ru-e/- perhaps in Old English hi/i/y/ca{\eg. hweica) " pustule, swelling, lump, 
growth ', wherefore hwelian^ fester' and (?) Latvian Rveldet, kve/et'g\o\N' (MiJhlenbach- 
Endzelin II 352). 

References: WP. I 365 ff., WH. I 188, 191 f., 277, 306, SchwyzerGr. Gr. I 301. 
Page(s): 592-594 

Root / lemma: /(eu-2 

Meaning: to shine, bright 

Material: Avestan savahT- "name of the continent situated in the east ' (actually Nom. Du. 

from *savah-' morning, east '), with zero grade root syllable Old Indie svah My. "early to- 



morrow morning '; A-stem Avestan sursm " early in tlie morning' (tliematic Akk. a 
conservative stem), a-suiri^ in the morning darkness ' {suirya-), Akk. suinm^ breakfast '; 

perhaps Armenian sukh^ radiance, splendor, fame' (as *Rud-ko-\ therefrom skhei 
"glamorous etc.'), sorxay, beam of light' (as *Ruo-lo-), nsoyr light, radiance, sparkle ' ( *ni- 
Ruoljd), probably sand, S5/7/' "spark, lightning, glowing iron' {Runti-, probably from a 
participle-stem Ru-ent-\ Ru-nt- denve ). 

no-stem: Old Indie 50/75- "red, bright red ' (/7for n), gall. C01//VOS(coin), Old Irish 
*cuan-dae, Middle Irish cuanna, (common Celtic -ns-, -nt- > -nn-), cymr. cun' mellifluous' 
(Sommerfelt BSL. 24, 219 ff.); russ. sunica, sunika, Serbo-Croatian sunica^ raspberry '; 
russ. /ri//75 "marten' etc., Lithuanian Riaune, Latvian cauna, caune. Old Prussian caune6s. 
could lie a corresponding color adj. from a root form with velar of the basic; about 
Lithuanian sv/naslea6', Persson Beitr. 745 between adds as Rueno-, s. Boisacq s. v. 
Kuavoq 'cyanus, a dark-blue substance'. 

Maybe alb. kunadhei. 'marten' : gr. Kouvapi "marten' : russ. /r^/7a "marten'. 

Root extensions: 



Reu-b'^-. Old Indie sumbhat/" sh\nes', sobhate^ ist stattlich, nimmt sich schon aus ', 
sdi6'/75/75- "beautiful, gleaming', subha-' pretty, pleasant, joyful, gratifying', subhra- 
"beautiful, gleaming, light color' = Armenian surb^pwe, holy', srbem^c\eav\, holy, sacred '. 

Reu-ci"^-. Old Indie 5'^/7o'/7a//"purifies, cleans', sudhyate^ becomes pure ', suddha-' pure', 
Kaus. sundbayat/ ^pur\f\es, cleans' (Avestan sudu-^ cleaning of the grain? grain mill? ' s. 
Bartholomae Wb. 1583). 

Reu-k-see below esp. headword {Reuk-); 

Ru-en-'}r\o\6 festivities, sanctify '? see below esp. headword {Ru-en-), 

Ru-eid-, Ru-eit-see below esp. headword {Ruei-3). 

References: WP. I 368, Trautmann 122 f., Specht Indo Germanic Dekl. 121 ; s. Ryon- dog'. 
Page(s): 594-595 

Root / lemma: Re- 
See also: see below Ro- 
Page(s): 537 



Root / lemma: Rei-b'^- 

Meaning: quick, hasty 

Material: Old Indie sfbhamMN. 'rash, hasty, quick, fast', sfbhya-^ wandering quickly, fast ', 

sibhra- "horny, lustful (?)'; 

Gothic /7a/>fe/s 'fight, quarrel'. Old Norse heipt, heifsti. 'enmity, rage, fury, hate'. Old 
High German he/ft/g Wo\ent'; Old English /7^s/ 'force, might, vehemency'. Old Frisian 
/75e5/'haste, hurry'. Middle Low German /7e/5/ 'vehemency'; Old English haeste. Old High 
German /7e/s// "violent, forcible '. 

References: WP. I 364 f.; belongs to Rei-gh-, see below. 
Page(s): 542 

Root / lemma: Rei-gh- 
Meaning: quick, hasty 
Material: Old Indie sFghra-^ash, hasty, quick, fast'; 

Old English hTgian^ stretch, make tense, stretch out, spread out, distend, extend, 
hasten, make haste, be in haste, hurry, be quick, bear upon, press upon, lean, support 
oneself, engl. /7/e 'hurry', geminated Norwegian hikka^ sob ', Old Swedish hikka^ gasp, 
have the hiccups ' (onomatopoeic words?); 

russ. sigatb, s/gnutb ' spnng' , wruss. s/gac, s/gnuc' walk, make big steps '; wherefore 
also russ. s/g'a kind offish', as Sa/mto salid, so that Lithuanian sykiseic. and Old Norse 
s/Ttr maybe are borrowed from Russ.. 

References: WP. I 363, Wissmann Nom. postverb. 174, Specht Indo Germanic Dekl. 249; 
See also: belongs to Rei-b'^-, see above. 
Page(s): 542-543 

Root / lemma: Re(i)- : Rd(i)- : RsO)- 

Meaning: to sharpen, whet 

Note: probably further formations from a^- 'sharp' (see 18 ff.) 

Material: Old Indie si-sa-ti{si-sT-t§), sy-at/" sharpens, whets ', participle s/ta- ' sharpened, 

pointed ' (= Latin catus, Old Irish cath), sata- ds., sana- m. (with Middle Indie /7for n) ' 

whetstone, touchstone, yardstick, criterion ' (= npers. s5/7 'whetstone'); perhaps also Old 

Indie S//5 'stone, rock' ( *ka-la)\ 



Avestan 5ae/7/-"cusp, peak, treetop, sharp' (npers. sayad'reM) = Old Norse he/rr, 

Armenian s^r'sharp' {*Rd-ro-), sre/T? "sharpen', sur. Gen. sroy 'sword, knife', sair 
"cutting edge' {*Re-ri-), compound s5//'a^//'"cutting edge', therefrom *sardrem, sadrem^ 
irritate, annoy, itch, anger, tease; arouse, excite, set in motion '; perhaps also sal. Gen. sail 
"flagstone, anvil ' ( *Ra-li-, compare above Old Indie sila); 

gr. Kwvoq m. " cone, a pine-cone, the cone of a helmet, top ' (= Old Indie sana-), 
therefrom kwveiov " hemlock, Conium maculatum ' (after the leaves); 

Latin ca/i/5 (after Varro Sabine) "acutus, sharp witted, shrewd' (= Old Indie si-ta-. Old 
Irish cath); cos, C0//5 "whetstone', also cotes, cautesi. PI. " pointed rock, reef {-au- 
hyperurbanism); catanus' cedar juniper ' is perhaps gall, loanword; 

Old Irish cath^mse' (= Latin catus. Old Indie si-ta-); 

Old Icelandic heini. "whetstone'. Old English han^ boundary stone ', engl. hone 
"whetstone' ( *Rai-n- : Avestan saeni-); Middle High German har^ tools to sharpen the 
scythe ' ( *Re-r-), Middle Low German haren " sharpen, be sharp '. 

References: WP. I 454 f., WH. 1181, 183 f., 190 f. 
Page(s): 541-542 



Root / lemma: Reko- 

Meaning: green grass, green fodder 

Material: Old Indie saka-m. n. " edible herb, vegetables '; 

Lithuanian seRas^ freshly mowed grass, green fodder", Latvian seRs6s., Old Prussian 
schokis "grass' (these at first from *sjaRas, -ya-from -e-1); 

Old Icelandic hat " bumper crop, byproduct' (probably from Germanic *hehdn-). 

References: WP. I 381. 
Page(s): 544 

Root / lemma: Re-ro- 
Meaning: a kind of colour 



Material: Old Indie sar^- "varicolored, dappled, dotted, spotted ', this -ra- as formant was 
verified through the Avestan composition form *sa-{i)i- in sai-muzay- EN " varicolored 
colored female donkey '; 

gr. KPipuAoq "the blue kingfisher ' (diminutive formants -uAo(;). 

*/re-/'c»- perhaps as *Re[i]-ro-\.o Rei-2\v\ " color names '? 

References: WP. I 420, WH. I 133. 
Page(s): 582 

Root / lemma: Reu-1 : Ru- 

Meaning: to sway 

Material: Latin ceved, -ere "wobble, sway; to agitate one's self, (the figure taken from the 

wagging of the tail of a dog), to fawn, flatter '; 

Old Bulgarian po-kyva-Jg, -//(mainly with glavg) " shake the head, nod ', Czech kyvati 
"wave, beckon, nod, wag, move, shake' (etc.). 

References: WP. I 376. 
Page(s): 595 

Root/ lemma: Reu-2{. Rau- Ru-) 
Meaning: to light, to burn 
Note: Only gr. and Lithuanian 

Material: Gr. Kaiw (Ionian), kqu) (Attic) from *KaF-i(jo "to light, kindle', Aor. hom. £Kr|Fa, Old 
Attic Gen. Sg. keqvtoc; (*Kr|FavT-), New Attic CKauaa, Med. Epic Kr|afjr|v, Pass. £KC(r|v, 
£Kau9r|v, delph. Kr|ua, Guaia', Kpia KaGappara and keTq ds. Hes., hom. Kr|cb5r|<; " smelling 
as of incense, fragrant ' (from a *Kr|Fo(; "blaze, incense '), kqugk;, Kaupa n. "blaze', kqAov " 
dry wood' (*KaF-£Aov), Aeolic KauaA£0(; " burning hot', hom. KriA£0(; {*mFaktoq) etc.; 

Lithuanian kOleti^ become blight-ridden, of corn, grain ', kule^ smut, blight '. (common 
Celtic alb. abbreviation) 

Maybe alb. kule^ hernia '. 

References: WP. I 376 f. 
Page(s): 595 

Root / lemma: Reuero-, Rouero- (also sRuro-1) 



Meaning: north, north wind 

Material: Latin caurus {corns) "northerly wind' {*Rauero-)\ 

Lithuanian siduret "north', siaurysm. "northerly wind'; 

Old Bulgarian severb {*Reuero-) "north'; 

Maybe reduced alb. {sven) veri^ north' a Bulgarian loanword?. 

moreover perhaps changing through ablaut and with aniaut. s-: 

Armenian curt^co\&, coldness, shiver' {*sRur-do-)\ 

Old Icelandic Old High German skur^ thunderstorm ', Modern High German Schauer, 
Old Frisian Old Saxon Old English scur, sceor^ shiver', Gothic skura m///7o'/s "whirlwind', 
Norwegian dial. sk0yra {*skauridn-) " Windschauer ', skj0ra {*skeurdn-) ds., Norwegian 
sk0yra, skura " drive off blindly on something ', Old Icelandic skyra " run there fast '. 

Note: 

Uralic etymology :
```


## [2026-09-06T20:35:26.118Z] TOOL CALL #10: Bash

```json
{
 "command": "ls site/pages/264.jpg 2>/dev/null; pdftoppm -f 264 -l 264 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg264 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:35:28.404Z] TOOL RESULT

```
site/pages/264.jpg
total 76
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 16:35 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   132 Sep  6 16:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb 57862 Sep  6 16:35 pg264.png
```


## [2026-09-06T20:35:28.652Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN sur ===\"; grep -n \"sûr\\|sūr\\|sur\\b\" HRN.txt | grep -in \"gastmahl\\|festlich\\|hochzeit\\|mahl\" | head -20; echo \"=== HRN nikuh ===\"; grep -n -i \"nikûh\\|nikuh\\|nikōh\\|niküh\" HRN.txt | head -20; echo \"=== HUB nikuh ===\"; grep -n -i \"nikûh\\|nikuh\\|nikōh\\|niküh\\|kūd\" HUB.txt | head -20"
}
```


### [2026-09-06T20:35:28.741Z] TOOL RESULT

```
=== HRN sur ===
8:6570:bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
=== HRN nikuh ===
=== HUB nikuh ===
3593:Hierher nach Horn (KZ. 33, 434) np. nikuhtdan
```


## [2026-09-06T20:35:32.650Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',d.count('\\f'))\nprint(len(d))\n\" ; echo \"---\"; head -3 HRN.txt"
}
```


## [2026-09-06T20:35:33.149Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3580,3610p' HUB.txt"
}
```


### [2026-09-06T20:35:34.573Z] TOOL RESULT

```
formfeeds 411
667366
---
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
```


### [2026-09-06T20:35:34.620Z] TOOL RESULT

```
gestaltet werden, vgl. basta- = skr. baddha^ etc.
Also liegt kein Grund zur Annahme einer Wrzl. naph
vor. Ist das Wort iiberhaupt indogermanisch ? —
Hierzu arm. navf 'Erdharz, Erdpech, ErdSl* (5. Jhd.),
gr. vd^&a.
^) Dieses nikSn 'begraben, yersohArrt' = paz. nag^n u. s. w. siehe
bei Horn p. 286, Nr. 148.-- 102 —
1038. Im Phi. steht, so viel ich sehe, immer nikfrisn, niki-
rttan etc., im Paz. nigeriSn^ nigareSn etc. Phi. niklret
= ap. *nikriyafiy? Vgl. oben Nr. 992 phi. m^nisn fiir
paz. manisn.
Hier fehlt np. nigun = phi. nikun *uingekehrt,
umgestiirzt* = arm. nkun 'niedrig'? WZKM. 7, 380.
Hierher nach Horn (KZ. 33, 434) np. nikuhtdan
'tadeln, schmahen' = skr. kutsay- schmahen, tadeln .
Schon bei Vullers, Radices, s. v.
1039. Np. nam aus *namna- ~ *nabna- wie kam aus ap.
kamna- = *kabna'. Dazu afgh. numd, nUmd u. s. w.
(Geiger).
1040. Die iranischen Dialektformen sind schwerlich ent-
lehnt, also iran. ^namad- anzusetzen.
1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend-
Avesta n, p. 45, Anm. — Dazu osset. nimdt, nmdt
Tilz, Filzmantel', s. Verfasser, Etym. und Lautl. der
osset. Sprache, p. 129, Miller-Stackelberg, Fiinf
osset. Erzahlungen p. 62. Skr. namata- Tilz' ist LW.
1043. In phi. anaumet (sprich anomef) ist die Anlaut-
schreibung beibehalten. Np. naumed (= afgh. LW.
naurmd) ist eine neue Zusammensetzung aus na und
umU. Vgl. naumed Fird. I, 133, Z. 2.
1044. Lallwort.
```


## [2026-09-06T20:35:39.995Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==187' HRN.txt | head -60"
}
```


### [2026-09-06T20:35:41.838Z] TOOL RESULT

```
- 165 -
747. Aeny 'Stein ; Gewicht, Würde', senrjin.
ap. ad^a(n)(jaina' steinern'; phlv. sa{n)(j (P.-V. z. B.
vd. 19 (13)), sang (AV.)
Allgemein entlehnt, z. B. kurd. senk^ seng; af/.
sang ; bei. sing (289) ; sangL. song,
Np. senjJdm (mit sekundärem Infinitiv se/ten —
phlv. sa/tan, sanßt , PP61. ; g. satnmn, Käs. örsaten,
örsatman, verset — PPP. sf?;^^e, Sahn. I, 1 Vers 10)
^wiegen* ist ein sekundäres Denominativum von seng,
Nöldeke (mündliche Mitteilung) schlägt vor, das
altpersische Wort (wie Spiegel, (jlossar) mit an-
lautendem d zu lesen, indem er dieses a in np.
murd]aseng 'Bleiglätte' und must\aseng \Schleuderstein'
wiederfindet. Auch denkt er an Zusammenhang mit
ai. ägman- 'Stein* (vergl. np. rts, No. 22) und (mit
Spiegel und Darmestete r) dem schwierigen aw.
asengöl.gäum (yt. 19, 43)^).
748. sün Stil 'Richtung, Seite', "^ID (Jer. 17, 1).
phlv. sük *Seite, Richtung' 2).
Eine ältere Form ist nicht vorhanden; das np. l
•ff
beruht auf Übertragung (vergl. No. 373). Ursprüng-
lich soft, wie skr. LW. söya- beweist (Weber, Pär.
des Kpn.).
749. suwär, eswär (Lex.) 'Reiter'.
ap. as(s)a]bära- 'Reiter' (doch wohl = *aspabara- ^) ;
phlv. (tsbär 'Reiter, aspwar Ritter (Nöldeke, Karn.
39 Note 2)4).
LW. kurd. suvär ; afy. spör, swör ; bei. sawär (232).
750. sötten 'anzünden, verbrennen, Praes. söz-em^ söz,
nw-^^yü (Qiss. Dan.).
') Zu derselben Auffassung über aw. aaehyö.gäum ist soeben auch
Burtholomae, Indog. Forsch. II, 268 gelangt (Correkturnote).
^) Arab. LW. cahärsüj *Markt', syr. LW. "^IDlNnii^ scheinen
herher zu gehören (ursprünglich *Vierseit, Viereck'); dann etwa auch
die mit s beginnenden, zuletzt von Hübschmann, ZDMG. 46, 247
No. 90 zusammengestellten Worte?
^) Aspa- auch in aw. A8(s)a\hana- {ß. pr.)?
^) Savärdk (vd. 1 (24 J) kann nicht *Reiter* sein.
```


## [2026-09-06T20:35:49.091Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"###### rec188 (p166)\"; awk 'BEGIN{RS=\"\\f\"} NR==188' HRN.txt; echo \"###### rec259 (p237)\"; awk 'BEGIN{RS=\"\\f\"} NR==259' HRN.txt"
}
```


### [2026-09-06T20:35:51.025Z] TOOL RESULT

```
###### rec188 (p166)
- 16() -
Käs. Q. bdsüy, Causat. sujünüden, K. bisiij^ Z. bosot,
aw. l/'saoc-, saoöayähi 'anzünden', atare. |saofca- Teuer-
brand', saocant' 'brennend'; phlv. sö/tan, Praes. söcem
(päz. sözet), söc(i)sn, söcäk (vd. 8, 253), söclmtan ; ai.
l/"(;öc-, gocati.
kurd. sötm^ ez disuzim brennen* ; afy. sezal, sejal '),
smjavul; oss. d. sojun^ t. s^/i« Verbrennen (226);
bei. sucarj^ n. s?«5ay intr. 'brennen (349), söcag ^ n.
sösay trans. 'brennen* (358) ; wa/. LW. säz^ sar. srfw^
'Brand'.
751. 8üd 'Nutzen, Vorteil'.
g. sid 'Zinsen*.
aw. [/'saV' 'nützen'; phlv. süt , sütih, sütömand,
sütlnUa/L
bei. sät, Sit (357); sonst allgemein entlehnt.
752. Süden 'reiben', Praes. säy-em, sät/lden.
ai. l/'cd' 'wetzen, schärfen .
kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
Die Bedeutung ist im Neupersischen verblasst ;
vergl. aber das Kurdische.
753. sür *Fest, Gelage'. •
aw. süirya- 'Morgenessen* (Darniesteter, Et. ir.
II, 161 und Geldner, KZ. 25, 531 Note 228); phlv.
5/Tr 'Morgenmahl, Mahl'.
bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
mehr als im Np. specialisirt).
754. sTirfii, sülax, ^Nt^lD (Is. 11, 8) 'Loch'.
Darmesteter's Etymologie (Et. ir. I, 62) aus
aw. *siifräka' , phlv. "^sufräk , "^suhräk , ^süräk in
säräk]öniand bezw. süläk]ömand ist unmöglich, da im
Aw. nur suwrä- ('Ring' oder Pfeil') vorkommt (vergl.
oben No. 740).
kurd. LW. särä/; afy. sürai^ LW. süläy.
*) Vergl. bezüglich des Vokals Kas. V. bdslz, bäalzün neben
Inf. Hüten, hafilznv (Oftusat.), g. lie.^(Ji(J (3. Sg.), sejeuph 'Tripper*.
###### rec259 (p237)
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
```


## [2026-09-06T20:36:01.755Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['BRT','SYN','BQT','WLD']:\n  print(k, json.dumps(d[k],ensure_ascii=False)[:1200]); print()\n\""
}
```


### [2026-09-06T20:36:03.552Z] TOOL RESULT

```
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", "notes": "Nourai's Table IV says 1979; that is the unchan

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.", "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_t
```


## [2026-09-06T20:36:09.776Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT savah ===\"; grep -n \"savaŋh\\|savahi\\|savahī\\|sūirya\\|suirya\\|sūirīm\\|suirim\\|sūrəm\\|surem\" BRT.txt | head -30; echo \"=== BRT 1631 ===\"; grep -n \"^1631\\|^ *1631 *$\" BRT.txt | head; echo \"=== BRT 221 ===\"; grep -n \"^221$\\| 221 $\" BRT.txt | head"
}
```


## [2026-09-06T20:36:11.515Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,5p'; echo \"---\"; grep -n \"kutsa\\|nikūhīdan\\|nikuhidan\\|kudázo\\|kuda\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-06T20:36:11.598Z] TOOL RESULT

```
=== BRT savah ===
6129:noch  No.  s-8,  10-15,  ^^f-  — Vgl.  alafojria-)  mit  No.  —  '1  Es  ist  ebenso unmöglich,  fiberall  die  verschiedenen  Bedeu- tungen des  Worts  auseinanderzuhalten,  als überall  zu  entscheiden,  ob  der  Begriff  oder dessen  Fersonitiliation  gemeint  ist;  vgl.  BB. 74.  10.  JAOS.  20.  31,  277,  IF.  12.  130.  - 3)  Vgl.  Cld.  KZ.  JO.  540,  jt.  268,  Gdn.  KZ. jt.  319,  Bthl.  Stud.  3.  124.  —  41  VgL  I  X b  &  —  i)  Hds.  aiava.  Pü. :  fia  hulaadlk  S  U i  akrirv  bulandih  ,.(?).  —  ')  Pü.  erl.:  rät  1 /rärön.  —  7)  -Pü.i  6t  vfh  mart  i  akrav  bül hFnd.  —  B)  So  Pt4.  NA.!  aiaakäeä,  %  26S. 30.  Pü. ;  an  i  fit  i  göspandän  —  tu  däi —  u  aArä- Hh—silt  i  iwiiW.  —  9)ünd  vgl.  Y,^/.  1  unter I  1  a.  —  u)  So  MI3  usw.  NA,  asira  nach Jp  I,  M[  2  usw.  und  angeblicli  nach  Pü.;  s. aber  oben  unter  Pü.  mitND.25.  —  lOPü.:  ic  ä ahräkik  ^aläiiA  iästt,  erl. :  fätixSäfüh  pa  frä- rämh  därii.  —  ")  Pü.  erl.:  an  i  pa  miiä  i akrSkiA  däränlA  afe  daAend,  Sü.:  yah praiäda^ panyasamgrake  diyalt.  —  1 1)  Pü. :  fa  öiän iuniln  !mäk  aAräiiA  S  imäi  daAJhef,  erl.: mild.  —  14)  ra. :  »e  .  .  aAräiiA  .  .  *viadil, erl.:  kiii  karpak  vinäi  ape  ni  kanel.  —  iS)Pü.: kc  .  .  räsBA  iSsel,  erLi  ku  viSir  (oder  däiawa- riA)  kunei.  —  '6)  Anders  Gdn.  KZ.  sy.  248, B>,  Stud-  /.  3i4>  West  SEE.  37.  175  (wo auch  lU  Pü.),  DsT.  ZA.  /.  200.  —  'ti  Vgl.  zu aiJAi«-3.  EN.— '»)NA.fli3.ÄfW.  Y^.:  SArmazd u  asavahisl  ki  tan  an  ...  —  '9)  NA,  asäjii. —  »)  VIL  lu  'asa-,  s.  DsT.s  Übersetzung.  — ")  Heilst  das:  "Soll  sie  für  ihn  die  kirckat- dienstUiAe  Vfrtichlung  vollziehen?"?  Pö.:  (un- deutlich): cigön  öl  iHtrai  rai  5  yazalän  lariä- iäslh...  —  "}  Ob  adverbial?  Pü.  hat  ein- fach aAräiiA.  —  >}>  Pü. :  haiar  ast  ahräkTA  iut xtat  nnirai.  —  '»  Np.  tägitd,  das  FrMOller WZKM.  5.  66  beraniieht,  ist  gewiss  femzu- hallen.  Eher  ist  'ai-ä^kj-lßi-  zu  Grunde  zu legen,  s.  np.  iarta  unter  ai.variiah-  und  unten Sp.  309,  —  »S)  Vgl.  zu  aiay-  mit  No.  9  f.
7938:idjektivisch :  D  'mam  bumim  ..  aram  as- mänam  D.6.1,  X.1.1,  6.  j,  Ao./.ij  — attm  asman>m  ys  'mam  sqm  äca  pairi^a bväva  Yt/j.  a;  153;  —  ava  raoffi  .. -mam  zqm  Yt  10.85,  89;  H./.  16;  —  'ms raoch  .  '.  avat  (sd.)  y.li  hzar}  aväcl  Y.jö', 6;  —  'mat  nmäniin  ..  käu  mat^a  trnrrjS ..  ace  awni  Yt.14.41.  a)  mit  einer relativischen  Ergänzung:  avat  karhar» yat  *ar7zaki  *savahi  .  .  'mat  karh-an yat  ^anira'i9m  V.  IQ. ^9.  2)  ohne  sol-
26003:savahi-
26040:•  j.  savahi-  (n.)  Name  des  im  Osten  ge- legenen Erdteils  (iarfyar-,  sd.):  avi  ar>- zahi  ''<4i{AD,)  Yt. /o.  15;  133,  *V.  ip.  39''; —  upa  karhan  yat  'hi  YLJ2. 10;  — anzahibyS  (sd.)  'hibyS  fradata/suiiyS  .  . Vr.  10. 1.
=== BRT 1631 ===
27180:1631
=== BRT 221 ===
```


### [2026-09-06T20:36:11.682Z] TOOL RESULT

```
---
23825:Ai. kutsitynti „schmaht, tadelt ££ , kutsa „Schmahung, Tadel ££ (nicht besser 
26336:Ai. kudayati ,.sengt" (' *kr-d -, d. i. *k e ro-d-, s. u. km- ..anzfinden 11 , nasa- 
26354:sprechen (-b- wohl = -dh-, vgl. ai. kudayati mit idg. d , dt. Herd mit idg. t ; 
48622:und die slav. Bildungen wie russ. kuda „wohin", aksl. kqdn, kqdc „woher“,
```


## [2026-09-06T20:36:16.766Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23800,23860p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== page tag ===\"; grep -n \"378\" incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T20:36:16.830Z] TOOL RESULT

```
keuq- , leuchten, hell, weiB sein. gliihen". 

Ai. cb^ati, euryati, coclti „leuchtet, gliinzt, gliiht, brennt, leidet heftigen 
Schmerz, trauert'*, cocayati „entziindet. betriibt; 1st traurig, beklagt ££ , gdk'i 
m. „Glut, Fbiniine, Qual, Sclimerz, Trailer*, cuci- „leuchtend, glanzend, 
blank, rein, lauter, tadellos“, ctikru- ,,licht, klar, hell, weiB, rein'*, cukti- 
f. „Huschel, Perlenmusehel, Perlmutter" (wenn .,*glanzend“), vielleicht 
< ukta- „sauer ££ (wenn ,,brennend von Geschmack“) ; av. saoeant- „brennend‘ £ , 
saocayciti ..inflammat = incitat", npers. srxtan „anziinden, verbrennen ££ , av. 
upn-suxta- „angezundet ££ , atro-saoka- m. ,,Feuerbrand“, np. sog ,,Trauer, 
Kummer" (arm. tug „Trauer‘ ist iran. Lw. ; idg. kuq- ware arm. *sus-, 
s. Pedersen KZ. 39. 3S9), av. surra-, up. -siirx „rot ££ . Dazu wahrsclieinlich 
gr. y.vy.vog „Schwan ££ als „der Weifie" (Wood AJPh. 21, 179; wohl nicht 
zu kog-ono- „Togelname ££ , s. d.). 

Ganz fraglicli hingegen got. hugs „Sinn ££ , hugjan ,,denken, meinen‘ £ usw. 
etwa als „helle sein ,£ (z. B. Fiek I 1 426, III 4 91, Hirfc Abl. 110, Persson 
Beitr. 726; Ubersicht anderer Deutungsversucbe bei Falk-Torp u. ha, wozu 
noch Lewy IF. 32, 161). — Erw. von Leu-, s. d. ; da6 ai. coksa-, cauksu- 
„rein ££ einer velar anl. Variante entstamme (Petersson LUA. 1916, 12 
Anm. t) ist ebenso unsicher, wie die Yerbindung von r. usw. kuna „Marder £ 
mit ai. goua- „rot £ \ 

qeud- „schreien; anschreien, schelten, liohnen, spotten". 

Ai. kutsitynti „schmaht, tadelt ££ , kutsa „Schmahung, Tadel ££ (nicht besser 
nach Wackernagel Ai. Gr. I 115 zu cotlati ,,wetzt‘ £ ), npers. niltlhtdau „tadeln, 
schniahen"' Horn KZ. 33, 434, 443, Hiibschmann Pers. St. 102, 239. 

Gr. y.vddgco, -op at „schmilhe, beschimpfe“, y.vbog m. (wahrscheiulich dor., 
speziell sizil., s. Boisacq, y.vbayyag • payag Xoibooia g Hes., y.vbayyopeva ■ 
/.oibogovuera Hes., xvddneiv . smcpcoveiv Hes, von einem St. y.cboi- (siehe 
Solmsen Beitr. I 51, Bechtel Lex. 208) y.vboiuog „Schlachtlarm, -getummeh 1 , 
y.vboipeiv „Liirm, Tumult verursaehen ££ , y.vboibondv ds. ; agutn. huta „her- 
beirufen", norw. mdartl. huta „schreien, larmen, einen Hund drohend zum 
Schweigen oder Sitzen bringen, veriichtlich behandeln ££ , huta ut „unter 
drohendem Zuruf und larmend austreiben ££ , schwed. huta at „hart anfahren“ 
( s. Persson Beitr. 1 86 f., gegen Falk-Torp’s u. hytte II Herleitung aus einer 
Interjektion hut; niengl. htltm, hrten, nengl. to hoot „schreien, jucheien 1 ' 
halt Persson fiir skandinavisch und mit nord. hola „drohen ££ ; got. Jvbfa 
,.Drohung“ vermischt\ ags. luisc (* qaO-sko -), ahd. as. hose ( *qad-sko-t 
.Schmahung, Spott, IIohn‘ £ , ags. hosp „Schande, Schmach, Beleidigung *, 
hyspan „spotten' £ (mit -s^i-Suffix, Persson Beitr. 317; nicht als „sticheln“: 
, Stich, spitz“ zu lat. cuspis nach Johansson IF. 19, 128, Holthausen IF. 
20, 319 f.), mhd. hiuy „frech, munter ££ , luuyn „sich erfrechen ££ („*heraus- 
fordernd schreien“), grhiuy, gehuy „Larm, Geschrei, Spott, Hohn ££ , hiuyn. 
hhyn „zur Yerfolgung rufen ££ (dazu die Interj. hussat). 

Mit anl. s- (erst nach sch alien , schreien u. dgl. ?) vielleicht mengl. schutm 
, vociferari ££ , engl. to shout „laut schreien, rufen, jauchzen ££ , aisl. shut a. 
skiiti Spott, Stichelei“, skot-yrdi ds. ; 

abg. kusclq, kacliti „zugrunde riehten ££ , ksl. auch „schmahen, tadelrr, 
russ. prokudits „schlechte Streiche machen, Schabernack spielen‘ £ , prokudn 



qegep- 


:(79 
=== page tag ===
8727:noch im urspriinglichen anaphorisclien Sinne; Lit. bei Boisacq 231 f., 378;.
9758:378, Horton-Smith BB. 22, 189ff. (mit unannehmbarer Heranziehung von
14184:lieraus, hinaufA dessen Yergleichung mit gr. slevoofiai er KG. II 378 offen-
31791: I 4 18, 378; fiber gr. y.gs s. aber u. kdu- Schallwz. Ygl. Mtihlenbach-End-
32589:Alb. St. Ill 4, Alb. Wb. 198 f.) kopste „Garten“. Ygl. z. B. Fick I 4 378,
```


## [2026-09-06T20:36:17.319Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25980,26060p' BRT.txt"
}
```


### [2026-09-06T20:36:17.367Z] TOOL RESULT

```
•  j.  sanaka-  il  'Mündung"':  yajdit  'ie ra»Aayä  yaiHt  vTmaihrm  (sd.)  ai>ihä  zfmS Yt  io.  104;  —  upa  aoiaisu  raakayä  .. upa  'Ae  ranhayä  YtT2,  i8f.
Et,?  —  0  Ich  nehme  diese  Bedeutung  an wegen  Yt./2.  l%i., -wo  aiüaeni  r'  \ai.d  sanaii  r' einander  gegenübergestellt  sind.  Nach  Yt. 10.  [04  liegt  sanak>m  r'  am  Ende  der  Erde.
•  j.  tant- :  sat-  f.  'Dekade'.
KompE.  —  Vgl.  gr-  «-ivr^-miir-a  :  bL  faiicä- Idi-ah.  —  zEt  (Ableit.  aus  daia)  %.  Beil.  Gidi.
dby  Google
1559  "sand-
•  j.  'sand-,  p.  ^a''d-  V,  'videri'.  Praes. 13  b  lan-'^,  34  sahaya-,  sadaya-,  %adaya-f 36  sa^ya-,  30  (Kaus.)  smdaya-.
i)  'sichtbar  werden,  zum  Vorschein kommen':  uSa^him  . .  yü  sanaj'^  aot  .. zqm  G.5,  5;  —  gSUi  .  .  yim  upairi  sruye sana£'^  amS  \t14.T,  9;  —  atihä  dim vataya  frSrtnla  (sd.)  salayeiti  yä  hava dalna  H.  2. 9.  3) 'gesehen  werden,  vidcri', mit  Ergänzung  durch  a)  Adj.,  b)  InC; a)  ham.urvlivi?f&S  jöiäij'äW  (statt  Plur.)  "(in fugam  se  convertentes  videntur  sva.)  man sieht  sie  sich  zur  Flucht  wenden"  V. j.  3a.  b)  %rityi   xsaps  %raosta  vyusq
(sd.)  sahayeiti  ".  .  illucesccre  videtur"  H. 2.7.  3)  'scheinen,  es  scheint,  sieht  so aus  als  ob  — ',  mit  Ergänzung  durch  Adj.: *JananA3  saitin  (sPPrA.)  nsit  jatun  "es sieht  so  aus  als  schlügen  sie,  (aber)  sie schlagen  nicht"  ¥1/4.56;  56.  4)  'er- scheinen', mit  praedik.  a)  Adj.,  b)  Adv.; zu  a):  abda{sA)ia  tia  .  .  sadaySt  (näml. daiiikul)  V.  2.  34;  —  sonst  mit  Dat  fGen.) der  Person:  XkyJ'  J'urJ'masdäh^  fra- mänä  hauvtaiy  gastä  (sd.)  mS  %aday^ (3SPrA.)  D.  ff.  6;  —  mätyt^  kyc/'  imUm dipim  paliparsäiiy  avahyä  paruv  *hadtiyä* (3SKA.)''  /ya*  manS  kariam  "damit nicht  dem,  der . .,  (zu)  viel  erscheine,  was von  mir  getan  ist"  Bk^-S;  0  —  sfarmat^hs ml  satayeAi  Az.  r;  Vyt.  r.  zu  b);  mit
Dat,  der  Person;  ya%a  yat  (Sp.  1250  o.) tn!  sa}>ayehi  "so  wie  du  mir  erscheinst" H.  2. 11;  —  ya%a  yat  ti  salayemt  H. 2. 1 2.  s)  'es  scheint,  kommt  (einem) so  vor,  es  ist  (ihm)  so  als  ob  -,  er  glaubt zu—';  mit  Ergänzung  durch  a)  ParL,  b)Inf.; zu  a):  ä  dim  vätö  upa.vUvS  saliayeiii  .  . Bat  tim  vsttm  ninAaya  *usgr?mbayS  sota- yeiti  yS  nars  afaene  urva  "es  ist  als  ob ein  Wind  sie  anwehe  .  . ;  drauf  ist  es  der Seele  .  .  so,  als  ob  sie  den  Wind  mit der  Nase  wahrnehme"  H.s.yf.;  3sf.;  — yff  nari  drvatS  urva  *alxahuca  paiti *gainilsca  vJdilarfmnö  sdtayeiti  "der  Seele des  Ungläubigen  ist  es  so  als  ob  sie  auf Eisfeldern  (sich  bewege)  und  ��ble  Gerüche empfinde"  H.a.  35;  7.  zu  b):  na^.a manyäe  jaynvi  */ia^a.am  y»nam  sadayetti yavata  .  .  "nicht  glaubt  er  geschlagen  zu  I haben,  und  es  ist  ihm  nicht  so,  als  ob  I er  einen  Schlag  führe,  bis  . ,"  Yt  /o.  7 1 ;  —  ■ ava  ml  ätis  . .  parSil  pairihmm  a»hvqm  \
'sand-
1560
*avaJirmqm  sadayäli  "es  ist,  als  ob  Asay (sd.)  mir  die  Lebenskraft  ganz  und  gar entzweisprenge"  V./Ä  19".  6)  Kaus., Med.  'sich  etwas  scheinen,  gutdUnken lassen,  an  etwas  (Akk.)  Gefallen  finden': alta  vaca  moQayarJÄa  ahe  vaea  sprufa- yartha  "an  diesen  (meinen?)  Worten  er- götze dich,  seine  (wessen?)  Worte  lass  dir gefallen"  Vx.S.i.  Undeutlich:  sadayat F.  72 ;  —  u^tm  sadayat  N.  6y,  —  D  "^ada- yamiy  D,  13  (s.  Sp.  1009  u.).
mit  a  dnwS.  s,  mit  Ergänzung  durch Inf,:  «/  hau  as  .  .  yS  ml  asadayat  fra- äa%3m  apa^arap .  .yashiit  upa.iarap'^wa ist  der,  der  mir  sichtlich  . .  wegbringt  . . herzubringt"  V.(j.  51.
ai.  ehadiyati,  ckandayaii  \  mp.  sahil  'videtor'  Sl ; pasand  'ßetällig'.  —  VgL  lEt.  YJL.  33,  \(>$, Hbm.  PSt.  41,  Ho»N  GlrPh.  /b.  956),  zKoiutr. des  Verbs  WILHELM  Mu«£od  /.  135.  —  Pü.: sahistan,  (lU  Vr.);  ifarsandik.  —  ')  Tbem. flektirt.  —  •)  NA,  Xadayäüy;  »gL  Bthl.  KZ. 2g.  585,  ZDMG.  46.  395.  —  4)  Die  von  Gnu. SPreussAW.  /JJ.  435  für  pair&mm  vorge- schlagene  Fasiang  halte  ich  für  uomÖgUclt. Maji  verlangte  dann  den  AbL !  —  5)  Zn  3  ■ und  5  mit  dem  "verkürzten'  Infinitiv  verbnndeD : Aam^asf,  väyit,  uzgn/t,  api  daSt,  ap€*darrU,  — ^)  Wo  mp. /äsandilan  (Gab.)  nachzutragen; auch  x'arsand  gehört  hierher. •  j.,  g.  'sand-  V.  'efficere,  perficere'. Praes.  2  sSndä—,  j-Aor.  1  sqs-.  —  Inf. sqsträi,  'sastrai,  satdyai.
i)  'bewirken,  schaffen,  zu  Stande  bringen': i:Jclt  msi  sqs  (aSr-AorA.)'*  tvSm  masdä vaidiÜB  "und  das  wirst  du  mir  bewirken, 0  M.,  der  du  es  am  besten  zu  ver- schaffen wcisst"  ¥.4*^.19;  —  <i%a  mü sqstä  (3Pj'-AorA.)"  voha  vastryä  "so schaffet  mir  denn  das  Gut  der  Landwirt- schaft" Y.  29. 1  ^;  —  sädra  mBi  sqs*^ mafyaisB  *trasdäitil  tat  vir^syädyal  Ayat.. "soll  mir  Leid  bei  den  Menschen  schaffen mein  Vertrauen,  das  zu  tun,  was  . .?"  Y. 43.  II.  2)    'vollziehen,    vollstrecken';
gavSi  srüis  (sd.)  *a  *syndä^  stäil  iyao- ^anaiscä  sSUgiaii/a  yS  Ts  s9nghs  (sd.)  .  . ".  .  vollstrecke  (an  ihnen)  ob  ihres  Tuns und  Sprechens  den  Spruch,  der  . ."  V. 5/.  14;  —  vaxbm  tttl  asqsat  (Augm.) tara%ustrS    V.  ig.  15.  3)    absol.    'es
vollenden,  die  Vollendung  herbeiführen': s.InC
mit  a
i.  Inf.
dby  Google
.S6i
sayana-
savahi-
156*
i^arsandik;  s.  'sand-.  —  ')  Pü.:  elen  man  räi säät  an  i  vch  västr.  —  J)  VgL  Vr.  /j".  1,  wo '^v^r^syafffmcä  iia  voAu  vajtrya.  ~~i)Pä.i  g^/(-
—  5)  Pü.:  ämSxtind;  i.iufia4ßJ^HJa-lio,2. — *)  Pu.  r  laAist;  s.  'samf:
•  j,  sayana-  Adj,  PPM. :  s.  ssy.
j.  fara^ayanfflf)  N.  So;  s.  'ay-  mit  No.  34.
•  j,  sayamna-  Adj.,  PPM:  s.  say.
•  j-  (1  g)  sav-  V.  'nützen',  Praes.  17 (Fut.)  saoiya-,  25  (Pass.)  suya-,  30  (Her.) sävaya-.  —  Inf.  süidysi,  styg,  savayS.  S. noch  spaya%ra-.
'nützen,  Nutzen  schaffen',  mit  Akk.  des wem?:  ya%a  väts  .  .  vTsptm  ahüm  .,/rä- la/icä  var3%atUa  saosyanti{ila.Xl  Sing.)& A.  4.  6;  —  ys  daitihave  hu.vaxsai  frdh>m- nake  vanltimnahe  .  .  suyamnahe  N.4-  2 Gl.  a)  insbes.  'den  Nutzen,  den  Vor- teil schaffen,  erwirken',  d.  i.  das  gute  Loos im  andern  Leben'';  wua^a  sao^qs  (sd.) ya%a  vispftn  akum  astvanhm  sävayät  Yt, y"9i  —  Aarp'hrai  asahe  gaihanqm suyaiitnanqmla  saosyantqmca  "um  zu wachen  . .  über  die,  die  den  Nutzen  be- kommen und  die  ihn  schaffen  werden" Y.55. 3;  — y^a  vS  saofyatttS  dahyunqm suyamna  väcim  ^barmti  Y,  yo.  4;  — sttoSyant-  s.  auch  bes. np.  tgl.  iSd  'Nutien'').  —  PQ.  (lu  Y,  55): sütan  u  nilömattdan,  (m  Y./O);  sütömand,  (lu V.  4);  süßiüt  (3.Sg.;^  erl.:  kui  tut  palas  kuneU
—  >)  Im  Gegens.  lu  rah.  —  ')  Wegen  np. a/zSdan  a.  Hbm.  PSt.  16,  Salzmank  GIrPb. 1. 340.  Falsch  neuerdings  Gdn.  VSe.  3.  45.
•  g.,  j.  sava-  m.,  n.;  g.  savä-  £  'Nutzen, Vorteil'  uzw.  der  ewige  im  andern  I-eben; hyatlä  dartgSm  ^dngvS-dibyS  raÜ!  (sd.) •va(fiSi.)ea  aiavabys  Y.  ^.  u;  benutzt Vr.  13. 1 1  'va  aSavabyS  yazamaide;  —  auch Plur.:  yS  ma  dngvä  (Sp.  776  o.)  äzc^  °vä paiturfte  "der  Druggenosse,  der  gegen deinen  Nutzen  auftritt"  Y.  44. 12'^;  —  aj tsi  'väii  vahmtm  (Sp.  1403  m.)  vaxsat aAura  Y.  4S.  1;  —  lä  vi  voka  mananhs aiaüä  °vais  *c3ViiX  (Sp.  442  o.)  Y.  51, I S-  a)  Du.  ('die  beiden  Nutzen,  Vor- teile', ellipt.  sva.)  'Vorteil  und  Nachteil, der  (ewige)  Nutzen  und  der  (ewige)  Schaden' im  andern  Leben*':  ait  .  .  yä  vX  alts *ränei6yä  'vSi  (ADf.)  vidayäi  "Alay  .  ., die  als  Belohnungen  an  die  beiden  Par- teien den  Nutzen  und  Schaden  verteilen wird"  V.  43.  12;  —  ye&ya  (näml.  masdä) °vä  (ADra.)  isänti  radatfhs  ySi ..  ". .  des,
der  darüber  verfügt,   Nutzen  und   (oder aber)  Schaden  erfahren  werden  (alle)  .  .
Y.45-7''-
Zum  V.  tav-    —    Vgl.  'savaA-.    —    Pü.r  sül,
SQ.:  läbhah.  —  0  D.i.  der  durch  seine  Lehren
die  Erlangung  des  Nutiens  vereilcll.  —  ')  Vgl.
Y.  JO.  II.     z.\uadr.    a.    Der.    VglS.    /.  137;
ferner    unter   pitar-,  nar-   (Sp.  1048   o.)   und
^art%a'.     Vgl.  noch  No.  3.  —  3)  In  Zeile  c
und  d  wird  «usgefiihrt,    was  unter  savt  in  a
zu  verstehen  sei;  s.  in  sädra-  und  iacia-.
•  g.  savayö  Inf.  'Jemandem  (Akk.)  den
Nutzen  (im  andern  I.«ben)  zu  schaffen':
yqm    xihät^m    rännibya  (sd.)  di  .  .  raSa-
ye^kl  (sd.)    dngvanttm    j*    aiavanitn    Y.
5^-9-
Zum  V.  sav'%    anscheini 2+24;  S  »ob-  a  a.  —  I
inem  Prae«.
■t  OSc).
•  j.  sava'vant-  Adj,  'der  den  Nutzen, Vorteil  hat';  'va  "d^i  Hi  att^  'S. 33.
Y\i.\  pa  !Ök.  —  Gani  unsicher.
•  j.,  g.  'aavah-  n.  'Nutzen,  Vorteil';  us na  aiiihai  vise  JamyJi  asimca  xsa%r)mca 'vasca  j^atfnascia  ,  .\.6o.2;  —  :^ar>nS.. 'vS  mazdatähm  Y.2. 14,8.2. 9; — a^arnta- nh5 'va>3ks  mazdahatake  Y.i.  14,  Ny.5.  5;
—  ahe  nmanahi  Jradäkäi  ahe  nmänahe 'vatths^''  Vr. //.  13.  a)  gAw.  nur  vom 'ewigen  Nutzen'  im  andern  Leben  (s.  sava-): yS  nä  fnzBs  'vank^  pa%ö  sJsSii  (sd.)  Y. 43.y,  —  Jr-a' (Sp.  185  o.)  zJ  kudanks vTspais  mazda  xsmavasa  'vS  Y.J4-3;  —
—  tat  vS  TiS  hazaosätahs  (sd.)  vlspSnhs daidyli  -vS  Y.  5/,  20;  —  xsa%r>tn  .  . xsmakim  ,,  vahmai  (Sp.  1403  m.)  däidl ■vat»hs  Y.57. 2;  —  auch  Plur.;  yaiSm ■■?vütyär)hs  (sd.)  T^S  xia%r3miä  'vattkqm ^.28.^.  \^-33'  li«  aS)SgavS',  —  Y. '.  20:  lies  savar3ke\
KompE.;  Ableit.  —  Zorn  V.  sav-.  —  Vgl. »jflfB*-EN.  — Pü.!  jü/,  Sü.:  libhah;  (lu  Y.  aJ, 43):  sSlömand.  ~  t)  Man  e
•  j.  'savah-  m.  EN.  eines  Gläubigen: nljarahe  'varghs  alaota  YL  j_y.  101.
Eig.  'der  Nutien  schafTende';  ar.  *iagis- neben  *sä^as-  (=  'im/aA-,  sd.)
•  j.  savahi-  (n.)  Name  des  im  Osten  ge- legenen Erdteils  (iarfyar-,  sd.):  avi  ar>- zahi  ''<4i{AD,)  Yt. /o.  15;  133,  *V.  ip.  39''; —  upa  karhan  yat  'hi  YLJ2. 10;  — anzahibyS  (sd.)  'hibyS  fradata/suiiyS  .  . Vr.  10. 1.
Eig.  ND.  zu 'jopjÄ-  n.  'Morgen;  Osten';  »gl. unter  oi-waiiil.  —  «Et.  s,  unter  niar-.  —  Pü.i transskr.  —  >>  Hds.  'he.
dby  Google
»S63
savahvant-
•  j.  savah'vant-  Adj.  (fem.  'vaitl-)  'den ' Nuuen,  Vorteil  schaffend  dir  -'  {Akk.)'>-. nisbayani  uyrä  *alaonqm  fravalayS  vispk  l ääman  'varmAatti/ (KP{.)  ". .  die  Fr.  .  ^\ die  allen  Wesen  den  Nutzen  schaffen"  \ V.  ig.  37.
Pü. :    ie   kannsp   dSmin  süßnel,    —     i>  Wohl
nach  Analog!«  eine»  etva  gteicbbedeut enden Paniiips;  doch  vgl.  auch  ai.  na«  kaminl  bei Dbr.  VglS.  /.  386,
•  g.  savä-  f.:  s.  unter  sava-,
•  j.  savö.gae9-ä- Adj. 'derdenLebewesen, dem  lebendigen  Besitz,  Haus  und  Hof, Hab  und  Gut  Nutzen  schatil':  arltätsm /rääal^al'iqm  vandai^atham  *%qm  Vr,
7. 2 ;  —  arstätS  fradat^ai^aya  vandat.- gai%ay3  '^ayä  Yt  li.  1 6.
Bildunß  wie  iarä.zai>%rä- ;  tum  V.  lav-.  —  Pü. : lülinUär  i  glhän.
•  p.  mäm  J'urJ'mazda  patuv  haÖl  sar»» ut^maiy  vi'iam  utä  imänt  dakyäum  "mich soll  ÄhM.  schützen  vor . .  und  mein  Haus und  dieses  Land"  D.  G.  3.
Das  fehlende  Wort  -  ein  AblS.  -  mus»  'Un- gemach, Unglück'  od.  dgL  bedeuten').  — Eü. ;  musniia  (wie  für  gasli),  Aü. :  bist  'böse'. —  1)  Herstellungsv ersuche  bei  JusTi  GGA. /itf^  48s  (™ra«ä*),  jN.JAOS.^o.SS.  f'-'7i- (jflni*;,  FOY  KZ.  J5.51,  37.  527  (j-^/ä*>  Ich bemerke  dazu,  dass  zwei  neiteie  Phologra- phien  der  Inschiifl,  die  ich  Reichelt  ver- danke, hinter  hacä  nur  noch  den  Wortteiler und  einen  senkrechten  Keil,  sowie  am  Ende der  Zeile  wieder  einen  senkrechten  Keil  er- kennen lassen,  während  alles,  was  dazwischen Bland,  völlig  zerstört  ist.
•  g.  'sar-  V.  "vereinigen'.  Praes.  4  sara-; J-Aor.  I   särts:  —  Inf.  sarS,  sarBt.
1)  'vereinigen  mit—,  anschliessen  an (Instr.):  y!  damqm  vohä  *s3rjstä^''  mana- tahä  ärmatöii  kasclt  .  .  huzSntus  (sd.) "wer  immer  sein  Ich  mit  VM.  vereinigt . ." Y.^ys''.  2)  Med.  'sich  vereinigen  mit  -, sich  anschliessen  an  — ;  es  halten  mit  — ' (Instr.);  aHfys  mazda  ahurB  sartmns voha  manarihä  xsä^räi  hacä  patti.mraot asa  hui.haxä  :^Snvaiä  "ihnen  erteilte MAh.,  der  mit  VM.  vereinte,  mit  dem lichten  A.  wohlbefreundete,  durch  Xs.  die Antwort"  Y.^2.  23>;  —  a  vi  *g3us.ä  (sd.) hSm.yantü  ySi  v!  fyao%an3is  sännte  ahurs aiä  *hisva  ux^aisvat>A7u/mafiaisAff"..die es  in  den  Taten,  in  der  Zunge  Reden mit  euren  Worten,  o  AA.  und  As'a,  mit denen  des  VM.  halten"  Y.5/.  3*'.
Vgl-  gr-  tipaiitu,  ai.  aiitta-;    %  iSj.  —  zBed.
Gdn.  KZ.  2S.  260.  —  S.  auch  »lar-.  —  Pü, (dRn.):  iordärVi,  pa  sardärih,  sardär.  —  ')Pt4 usw.  -  ')  Vgl.  Y.  ja.  I.  -  j)  Vgl.  \.49.S.-~
4)  s.  iSt  bthl.  if.  s-  364-
•  j.,  g,  'sar-  f.  'Vereinigung,  Verbindung, Genossen-,  Gemeinschaft  mit  -'  (Gen. oder  Instr.);  y^  tal  ups.jamyama  tavacä 'nm  aSaRyälS  vispai  yavl  "dass  wir  dazu gelangen,  zur  Vereinigung  mit  dir  und dem  Aia  für  alle  Zeit"  Y..^/.6'*;  — f)raiaoiträi  un/äzistqm  (sd-J  asahya  da •rSm  (AS.)  Y.  4g.  8;  —  mazdä  dadät  ahurö haurvats  amtntätaslä  . ,  asahyacä  . .  xla- %rahya  'rS  (GS.)  vatthSus  vazdvari  (sd.) manarths  yj  .  .  Y.JI.  21 '';  —  tfmcä  . , vaahSus  *pailylstim  (sd.)  manaahs  asaAyä matdasla  taibyB  dal  'rf"*  Y.5J.  3;  —  vi daXvais  .  .  'rym  mruyi  "ich  entsage  der Gemeinschaft  mit  den  D''  Y. /2, 4;  6'; —  vL.ana  'nm  mruyl  yakanä  dngväia Y. /2. 4;  —  neben  virt^Sna-,  vantäna- (sd.,  Sp.  1424  u.):  asahyä  .  .  sairl(LS.) asaAyä  v»rfssta  "in  der  Genossenschaft des  A.,  in  der  Gemeinde  des  A."  Y. ^5-8;  —  yai  tat  frajasat  aniar>  sairi (AD.)  vansänei^  "wenn  das  (die  Nieder- kunft) vor  sich  geht  innerhalb  (des  Be- zirks) der  Genossenschaft  und  der  Ge- meinde" V.  /j,  17.  a)  konkret  'der Gemeinschaft  hat  mit  -,  Genosse':  «Sit ?r)sva^ä  'rim  (GP.)  didqs  dnigväta  hyat.. aiä  yuxtä  . .  "nicht  wird  der,  des  Sprüche die  rechten  sind,  sich  um  die  kümmern, die  mit  dem  Z^/T^jgenossen"  Gemeinschaft haben,  während  die  mit  dem  A.  ver- bündeten . ."  Y.  49. 9.  GS.  sar7,  DS. sarsi  als  Inf,  sbes.
KompE.  —  Zum  V.  sar-.  —  iBed.  vgl.  Bthl, AF.  3.  184,  IF.  j.  364,  Gdn-  KZ.  28.  195, Bn.  Stud.  /.  354,  JN.  A  hymn  55 ;  faUch neuerdings  Gdn.  VSt  2.  iH.  Enischeidend sind;  Y.  40.  z  mit  haximä  gegenüber  tarim in  Y.  4r.  6;  Y.  4g.  3,  wo  sich  vaohiui  sari maiiaiihö  und  dngvatS  haxming,  und  Y.  4g,  9, wo  sich  sarim  ärtgvati  and  asä  yuxtä  g^en- Qberstehen.  —  Pü.;  sardätih,  (lu  V.  75);  siya 'er  liegt"  I).  —  ')  Vgl.  V.  40.  2.  —  »)  Vgl. zu  saröi.  —  3)  Dualrerbindung ;  BB.  /o,  269. —    4)    Wie  Y.  32.  5;    vgL  liayö  No.  1,    —
```


## [2026-09-06T20:36:24.978Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27170,27200p' BRT.txt | head -60; echo \"=====suiri=====\"; grep -n \"suiri\\|sūiri\\|s0iri\\|Morgenessen\\|Morgenmahl\\|Frühstück\\|Fruhstuck\" BRT.txt | head -20"
}
```


### [2026-09-06T20:36:25.044Z] TOOL RESULT

```
Pü,  (zu  F.):   fräc  spSiiimh.    mit  undeutl.  Erl.;
Sü.  (zu  A.):    hastatiUkäbhis    sarvaira  jääpayi-
tum  3).  —  ■)  Steht  unter  den  slrafrecbtÜchen
Term.  techn.    —    >)  Ich  kenne  kein  zweites
Beispiel  für  idg.  xj  im  Germ.    —    J)  Als  ob
es  pazday'  hiesse,  sd.
•  g.  syazda-  Praes.  18  a  'zurück- weichen'.
mit  Abi.  'vor  — ':  ySi  , .  armaitlm  . . b>nxtqm  (sd.)  . ,  avatatai  . .  alifye  mai' ala  syazdai  yava^  ahmat  aurunH  xrafstra ".  .  vor  denen  weicht  Asa  gar  sehr  zu- rück, so  weit  als  vor  uns  die  wilden  Raub- tiere" Y,j4.  9.
Vgl.  lu  liläya-.  —  Pü.:  hal  Siän  vat  ahräkih
ob,Google
1631
syämaka-
163a
+nli/ (Ttaiuskr.)'),  SQ.:  ttbhyo  fnAhüta  ähar- mak  prabhraiyati.  —  ■)  Vgl.  zu  iildyamni  Y.
•  j.  syämalia-  m.  Name  eines  Bergs oder  Gebirgs*':  akmai  haca  garayS  frao- xSyqn  . .  'kasla  va/rayäs{^ya  Yt.  ig.  5.    j
*l  Der  Bd.  12.  3  syäinioimand  ('mit  schwarzen  | lliaren'),  12.  32  sy��tömand  genuint  wird.  S. im  Cbrißen  Sp.  1347  o.
ai.  fyäniaia-  Adj.  (auchEN.);  ai.  iyämä-  Adj.
—  Vgl.  säma-  und  zu  »syäva-,
"  j.  syäva-  Adj.  'schwarz'.
KompA.  —  ai.  fyävä-  Adj.  'scttwarzbraun', np.  siyäh  'scbwaiz';  weiteres  bei  Hbm.  AGr. /.  489,  IFAnz.  to-  zq.  —  S.  noch  Sävaiaii iliyih.  EN.  (=aL  iySvaka-  m.  EN.).  gebildet wie  syämaka:
•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
Komp. :  'iy5va-\-atiatf  (S  268.  3  b),  eig.  'der Rappbengsle  besitzt'.  —  >)  Them.
•  j,  syävaspi-  m,  EN.  eines  Gläubigen: */»V"  asaonS  Yt. /_J.  114.
Komp.:  iyäva--\-aspI-  {%  368.  3),  eig.  "Rapp- stuten  besitzend'').  —  ■)  Nach  der >-Delcl., YgL  oTjäraosIrl-,  daufrämatsi- .  —  ')  Ein  patr. Adj.  -  JUSTI  NB.  300,  GUBLSR  Patronymica [Baseler  Diss.  1903]  67  -  ist  nicht  am  Platz, j.  syötdim  '^.  48.  T:  lies  syödüm;  %.  sS:
•  j.  (svar-) :  sor-  n.  'Morgen,  Morgen- frühe', nur  AS.  sßnm'^  als  Adv.  'früh- morgens': mtäsnm  . .  yS  paoiril  voHäis (sd.)  *nm  frälaiÜ  Yt  10. 143.
KompE.;  Ableil.  —  Vgl.  imiakT-.  —  ai.  h/äi (LS.  als)  Adv.  'cfm'«).  —  lEL  s.  IFAnz.  t2. 27.  _  1)  Them.;  die  Bildung  kann  durch bedeutungsverwandCe  Zeitadverbien  -  vgL  ai. HÖilam,  Jofim,  säydm  -  veranlasst  sein.  — ')  Allerdings  wird  ja  ai.  hiäh  in  SandAiA  be- handelt, als  wäre  as  der  ar.  Ausgang;  doch s.  dazu  Wn.  AiGr.  i.  334,
•  j.  sraeS-  V.  '(sich)  heften',  Praes.  3 trUa;  17  (Fut)  srai^a-.  —  Absol.  sral- iyäntim.
1)  'haftenaß-' (Dat):  nSi^ *Ai/iu (sd.) iiiivsi  sraiiyäti  "Trocknes  wird  nicht  an Trocknern  haften"  V.  8. 34.  2)  'sich heften  an  -  (Akk.)  sva.  nachgehen,  ver- folgen'; yö , .  hala  gaiisabyS  paraiti  srai- hmns^^  tayol  v)hrk)mca  "wer ..  weggeht in  der  Absicht  die  Diebe  oder  den  Wolf zu  verfolgen"  V.  13. 1 7.
mit  Aam  'zusammenheften,  -binden':  yB I  bansma  ham^rüäiti  kam  vä  dantayeiti N.jp;  —  yff  bansma  *a^ahmSf  nalm3t '  iam.srifäili  Vi.  gg.
ai.  triiat,  iletfyaä  (G
Pfl.  (zu   V.  S) :  falinjün,
=====suiri=====
5926:1  Morgendunkel  sich  das  Morgenmahl
```


## [2026-09-06T20:36:30.246Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5905,5945p' BRT.txt"
}
```


### [2026-09-06T20:36:30.293Z] TOOL RESULT

```
•)  Nach  Bd.  /2.  26  in  Alut-plLiirin,  S.  noch Bd.  //.  7:  fa  aim-aiid  iöf  äliir  i  vusa<p  apr  0 ,/jt  i'äi  iiiiasl.     Vgl.  femct  DsT.  ZA.  /.  154.
D. i.  asmfvant;  % 26^.  12.  Eig-  Bed.  ?  —  OTbem.
•  j.,  p.  asman-  m.:  s.  unter  asan-.
•  j.  asmana-  Adj.  'steinern':  'na  (ND.) hlvana  Vr./2.5;  //.2,  Y.22.2,  V. 14.10; —  'nasibya  ftivanaiibya  Vr./o.2.
Ableit.  aus  asman-.  —  Pü.:  asimni  'silbern'i durch   den  Anklang   veranlasst;    falsch  DST.
dby  Google
asmamva-
asrutvm
ZA.  1.  179;  ;.  daia  Hehn  Kulturpfl.^  548, .NöLDEKE   SWienAW.  126.  13.  45.
•  j.  asmaniva-  n.,  Plur.  Bezeichnung  ge- wisser Teile  des  (tierischen)  Unterleibs'': hazanrtm  anumayanqm  frävinuyät  vTspa- nam:a  aSaSsam  fasvam  'vä  (AP.)  zaoira iire  . ,  frabarBil  bszva  aiwyS  . .  frabarnit ". .  und  von  all  diesen  Tieren  soll  man die  A.  sammt  Z.  dem  Feuer . ,  darbringen, die  Vorderfiisse  aber  soll  man  den  , , Wassern  darbringen"  V.1S.70.
Eig.  Adj.  asmaiiMfa;  Ableit.  an»  *asmaii;  Bed.  ? —  •)  FüZ.  fügt  hinzu:  yai  aalari  vtrAka  as *marjja  (sd.).    Nach   St.  jr.  4   gebührt  dem Feoer  das    Herz  des  Oprertiers. j.  asmintj  N.  103-.  lies  a'smim.
•  j.  asmo.x*anvant-"  m,  EN.  eines Gläubigen:  ahe  nari  a^aonS .  .  yS  asmS.- jfaf/j'j'>  aawta  Yt.7.30; — *asms.:^anfatB'^ aIattnoYi.ij.g6;  —  *asnöj^anvati!^^  asaenö Yt/j.96.
VeI.  SBE-  47.  165.  —  ')  Der  Mann  hLess  im Non.  luDächst  *asnia  j^airrS,  ä.  i.  'lichter lllmmer;  der  rcEcIrechte  Gen.  dazu  ist  alnS i'.im-atö  Yt,  13.  96  2.  Stelle.  Aus  *asma i'anz-a  entstand,  indem  das  Nominaliv-a  durch riis  KooipositionS'D  ersetit  wurde,  asmöJ^atn-i Yt.  /.  30,  dem  dann  als  neuer  Gen.  asmS.. i'aTK-atff  Vl  7J.  96  I.  Stelle  mr  Seite  trat. l)et  Kompilaior  von  Yt.  /j  hat  iwei  Männer draus  gemacht.    NA.  trennt  ßlscblich.
•  j.  a-svar-  :  'ssr-  n.  'Morgendunis  el, -dämmening':   'sSiri  (LS.)  süirim  ispmnS .»  j.  'a-srata-  Adj.  (fem.  'tä-)  'nicht  ge-
YtÄS9;  —  dulxraiUm  .
•  j.  a-sravayant-  Adj,  'nicht  vortragend, aufsagend,  rezitirend';  a)  mit  Akk.:  yB gaisS  (NS.)  'yS  tiaimpm  yäri.dräjJ  "wer  die G.  ein  halbes  Jahr  lang  nicht  aufsagt" N.  44;  41-45''.  b)  ohne  Obj.  '(die vorgeschriebenen  Gebete)  nicht  sprechend': yS  salte  haurvqm  tarasca  xsapatum  ayo' Z)mns  °yif  amarä  V.  /Ä  5 ;  —  *frasrävüy3 rüiufris  tidit  *'°yS'^  N.  104.
Vgi.airä!'aya/.ffä%ä-.  —  Fä.s  asrülär,  ke  gäsSn ne  sräyit  oder  ya%!l,  Jni  afräi sräyün.  —  ')  Hds. (t\Täv'\  die  Echtheit  der  bds.  I.esune  ist wenigstens  nicht  wahrscheinlich;  dach  &.  Aog- SrTi.
•  j.  *"a-srävayamna-''  Adj.  'was  nicht  auf- gesagt, rezitirt  wird':  'ii3t  paiti  ahuiia^ vairyat  "ohne  dass  der  AhV.  rezitirt  wird" N.  tiS'
Pü. ;  pa  asrSyiJii.  —  •)  So  T ;  Ausg.  äsr'.
•  j.  *asrü.azan- '*  Adj.  'Tränen  (treibend sva.)  vergiessend' :  'z3nS  (NP.)  hilt>nte anuxajand  (sd.)  takahe  Yt.  JO.38.
'asrai<-  n.  'Träne';  at.  äirav-  r.,  np.  ars.  — "azan-,  an-  Part,  lum  V.  U3-;  s.Bthl.  1F.  jO. 195.  —  ')  NA.  trennt;  s.  ebd.
1  Morgendunkel  sich  das  Morgenmahl
suchend"
Yt.  14-  2C
Eig.  'wa
s  bis   2um
Morgen  hin
reicht'
»  t<,dam<
T.  —  Vcl.  11
BöHTLiNfjK  BSäehsGW.  5/.  49
a  ai.  äl
•  j.  a-sraosa-  i)m. 'Ungehorsam' (nur  Ab- leit) 2)  Adj.  'ungehorsam' :  vUpe  adpriia.- Ikaiss  (sd.)  yJ  'iö"  vJspe  °A"  \ys\  anasa-  \ ranS  ". ,  aUe  die  (dem  Lehrer)  ungehorsam  1 siod,  sind  Glaubensfeinde"  V, /6. 18.
Ableit.  —  mp.  (Pu.)  asröi,  crl. :    iasän
hört,  nicht  hörbar':  y3 .  .  pailiitanti  (sd.) anyö  713  hl  da/iml  srutn  glisä  dänSiti *ratufris  'tä  daoniti  {aratufril)  "wenn einer. .,  und  ein  andrer  D.  die  Gäkäs.  fiir ihn  hörbar  vorträgt",  so  ist  er  r.\  wenn er  sie  nicht  hörbar  vorträgt",  ist  er  ar." N.  25.         asruhm  als  Absei,  sbes.
ai.  airula-  Adj.  —   Pü.:  astnl,   —   1)  So  laut (leis),  dass  er  sie  hören  (nicht  boren)  kann.
'a'sruta-  m.  EN.   eines  Gläubigen:
\fraturiJ  (sd.)  °/a  (GD.)  balMastiira  aiaonS Yt/j.iiS.
•  j.  asraoSya-  Adj.   (fem.  'yä-)   'imgehor- 1      Eig.  'berühmt'.  —  Vgl.  lat.  ind^lut. »m,  unbotmässig  (gegenüber  Gott)':  nsit\ ti  äl  'yanaitt    fanunam  asa/u  .  .  ''rioüiti ' ,
p..i.
Ableit.  aus  airrwia-  m,;  ».  Wh.  Gr.'  S  '^t^  <:■
```


## [2026-09-06T20:36:42.791Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== leaf 1019 (p995) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==1020' SYN.txt | head -70"
}
```


### [2026-09-06T20:36:44.562Z] TOOL RESULT

```
== leaf 1019 (p995) ==
s. of words for ‘fold’ or the like. Their earli- est extension from the literal sense must have been to ‘consisting of three parts’, as in Lat. triplex mundus ‘the threefold world’ (of sky, sea, and land). This sense shades off to that ‘of three kinds’, as in Lat. triplex ratio ‘a triple system, three kinds of reasoning’, a notion for which there may be also other more dis- tinctive terms (13.47). Or the notion of subordination of parts to a whole may be lost, so that ‘a whole consisting of three parts’ becomes ‘three making up 4 whole, three in a group or series’, as in Lat. triplex mirus ‘a triple wall’ or triplex aciés ‘a triple line of battle’. In such use the multiplicatives approach the collectives (13.51). Again, a group of three may be felt as one taken three times, a given unit raised to the third power, as in Lat. triplex equitt ‘triple pay for the horseman’. This proportional use, though occasionally marked off from the others by a distinctive formal type (as Att. rpumddowos) becomes in general the commonest use, and the only one which leads to a full series running up
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
946 SELECTED INDO-EUROPEAN SYNONYMS
into the high numerals (‘a hundred fold’, etc.).
In many of the modern languages this proportional sense, though included in the uses of the adjs. listed, is more com- monly expressed by a substantive phrase ‘three times as much’, as Fr, trois fois autant, etc. (below, 4), Lith. iris karts tiek, Russ. tri raza bol’ Se, etc.
1. From IE *pel-, *pelt-, *plek- in words for ‘fold’ or ‘plait’. Walde-P. 1.55 f., 97.
Grk. rpirddos, Att. rpurdods, the usual type of multiplicative in all dialects and in all uses, most commonly proportional and so used even in Attic (beside rputha- ows). Precise origin of formation un- certain, but separation from the main group and connection with rrtw ‘sail’, mAéos ‘voyage’ improbable. Forms like amhds, durdés are analogical fr. forms like fem. sg. d7Aj, neut. pl. dda, and not in- dependent formations corresponding to Lat. triplus, etc. Cf. also Loer. 6éex- Aetos, Cret. dirdcla.
Att. rpimddows, proportional, fr. -mhatwos formed to -rdaros, like rpidd- ows to -paros. Later tpitdaclwy with comp. suffix. Jon. diAjows, ete. (in Hadt., but not found in Ion. inser.) with n fr. fem. durd9(?).
Lat. triplex : p
```


## [2026-09-06T20:36:52.676Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 1069 1070; do echo \"##### NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | head -40; done"
}
```


### [2026-09-06T20:36:55.055Z] TOOL RESULT

```
##### NR=1069
 for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI.
tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen, ie Kit and only secondarily (like ‘sum- | Gram..35, 180. Pokorny KZ 50.43 if ne ss ‘winters’ for ‘years’) the com- (taking lae as of different orig., but cf. wehensive 94-hour ‘day’ (for which | Vendryes, RC 42.234 f.). Dan., Sw. have distinctive forms). 4. Goth. dags, ON dagr, OE deg, 1. Derivs. of IE *dei- ‘shine’, rare in | OHG fag, etc. general Gmc. (also derivs. verbal forms (Skt. 3sg. imperf. adzdet, Goth. fidur-dogs ‘of four days’, OE dégor etc.), but widespread in words for ‘sky, | ‘day’, ON degr ‘12-hour period, day or heaven’ as Skt. nom. sg. dydus and the | night’, Dan. dégn, Sw. dygn (the last two personified Grk. Zebs, Lat. Iupiter, Iovis; denoting the 24-hour day), etym. dub., ‘god’ as Skt. deva-, Lat. deus, etc.; and | but perh. (despite phonetic difficulties ‘ay’. Walde-P. 1.772 ff. Ernout-M. | with the gutturals) : Lith. dagas ‘(sum- 268 ff. Walde-H. 1.350. Here as ‘day’. | mer-) heat’, OPruss. dagis ‘summer’, Skt. a) IE *dyeu-, *diw-, etc. nidagha- ‘heat, summer’, fr. the root Lat, digs (> It. di, OF r. di, Sp. dia, | *dheg*h- in Skt. dah-, Lith. degti, etc., Rum. zi); Ir, dia, die, W. dydd, Br. | ‘burn’, and also (with init. doublets, as deiz; Skt, diva- (in dive dive ‘day by day’, | Skt. agru-, Lith. asara : Grk. daxpu otherwise divasa-); Arm. tiw. Lat. deriv. | Goth. tagr ‘tear’, etc.), Skt. ahan-, Ay. adj. diurnus ‘of the day’, late sb. diur- | azan ‘day’. Walde-P. 1.849 f. Walde- mm > Fr. jour, Prov., Cat. jorn; It. | H. 1.467. Falk-Torp 183, 176. Feist ee vs. di perh. due to lit. influence | 113. ea or Fr. REW 2632, 2700.| 5- Skt. gat Caisse ae il ae 3.71f., 105f. Bonfante, | instr. sg. ahna, etc.), Av. se . Sg. “74 59.877 ff. (with refs.). asni, etc.), see above, 4, with reis. b) With nasal suffix. Av. ayan- (nom. sg. ayara, gen. 8g. aes Lett. diena; ChSl. dint, ete., | war ete., neut r/n stem. like Skt eral Slavies Skt. di in epds.): | 2a" above), prob. : Grk. fier ‘in the Me ed (eap. in epds.); ning’, Goth. air, ON ar, etc., ‘early’, » tre-denus ‘triduum’, Goth. sin- he eee z
leing ‘daily’ Goth. jer, Av. yara ‘year’, etc. Walde-P. 2. Grk. ane ; 113}. Dor, a ‘népa, Dor. dutpa, poet. Fuap, OPers. rauca (xSapava raucapativa
Toot a ‘ Arm. awr (*admor) ‘day’, | ‘either by night or by day’, 1 rauéa ‘one
329 “ction? Walde-P. 1.53. Boi- day’, etc.) : Av. raoéah- ‘light’, Skt. ruc- ae ‘shine’, Grk. devxds ‘bright’, Lat. lax “laithe, beside Iae, laa, NIr. Ia, | ‘light’, ete. Walde-P. 2.308 ff.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
H ;
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.42 NIGHT Grk. vot Goth. nahis Lith. naktis ; NG voxra ON noatt Lett. nakts ; Lat. nox Dan. nat ChSl.  noStt i It. notte Sw. natt SCr. noé jj Fr. nuit OE nitht Boh. noc Ft Sp. noche ME night Pol. noc Rum. noapte NE night Russ. not! i Ir. adatg (nocht) Du. nacht Skt. ratrz., ksap-, nakt- 8 NIr. _ oidhche OHG = naht Av. OPers, 2Sap- W. nos MHG naht Br. noz NHG nacht tl Most of the words for ‘night’ belo
##### NR=1070
ng general Slavic; Ved. nakt- (nom. Sg. nak, to an inherited group, pointing clearly | acc. sg. naktam), nakti- (class. Skt. only ( to an IE word for ‘night’. In Irish, ex- | adv. naktam ‘by night’, cf. Wackernagel, cept for an adv. relic, and in Indo- | Altind. Gram. 3.233 ff.); Alb. naté;— \ Iranian, except in Vedic and a classical | with e-grade Hitt. nekuz ‘evening’, : Skt. adv. relic, the old word was dis- | nekuzi ‘goes to bed’ (Sturtevant, Hitt, lL placed by others, but’ elsewhere has per- | Gloss. 108). i sisted as the usual word to the pres- 2. Ir. adaig, aidche, NIr. oidhche, ent day. etym. dub. Walde-P. 1.34. Walde-H. : 1. IE *nokt(t)-. Walde-P. 2.337 ff. | 1.61. Stokes 326. ( Ernout-M. 682. Sturtevant (connect- 3. Skt. rdtri- : Grk. Anr&, Dor. Aard ; ing this group and that for ‘naked’, | ‘Leto, mother of Apollo and Artemis’, : 4,99) JAOS 52.10, Hitt. Gram. 122 f, orig. personification of the night, perh. Grk. vit, vuerés, NG vixra (v prob. | fr. the root in Grk. \6w ‘be hidden’, fr. a reduced grade); Lat. nox, noctis | ete. Walde-P. 2.377. Boisacq 555. n (> Romance words); Ir. nocht (in in- | Uhlenbeck 248. Y nocht ‘tonight’), W. nos, Br. noz; Goth. Skt. ksap-, Av. xap-, rfapan-, xSapar-, Mi nahis, ON ndtt, etc., general Gmc.; Lith. | OPers. xsap- (Barth. 548 f.) : Grk. pédas, naktis, Lett. nakts; ChSl. nostt, etc., | pédos ‘darkness’. Walde-P. 1.524 f. h q ‘ 14.48 DAWN Grk. dus, Sp8pos Goth. : Lith. auSra, brékSta x NG aby}, xapépyara, ON — dagan, dagsbrin Lett. rita blazma, rila Xapavyy Dan.  dagning, daggry krésla, ausma D Lat. aurora, prima liz Sw.  dagning, gryning ChSl. rano(adv.), -brézgi, di It. alba, aurora OE degréd, degrima, zore (pl.) Fr. ube, aurore dagung SCr. ora, svanuce 1 Sp. alba, aurora ME  dawing, dawning, Boh.  svitdnt, risvit Rum. zori, auroré dayrawe, etc. Pol. Swit, brzask, zorza Tr. dedal NE dawn, daybreak Russ. zarja, razsvel i) Nir. fainne an lae Du. —dageraad Skt.  ugas-, aruna-, pra- D W. = gwawr OHG = morgenrot, -rata, bhata- i Br. goulou-deiz, tarz tagarat Ay. uSah-, astir- ! an deiz MHG morgenrét, -rale,
tagerat
NHG morgenrot, -réte, tagesanbruch, mor- gendimmerung
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘dawn’ denote strictly the unrise, but some of be extended to cover ‘sun- en (morning ’- ' They are most- juding the inherited group, con- Md with words meaning grow bright, pectee * ht’, or ‘white, gray, red’, or in with the word for ‘day’.
8 ‘ist before §
ry few cases i IE *ausos-, etc., fr. a root seen in ‘ ‘ybl. forms Skt. ucchati, Av. usaite 9 vbl.
pright, shines (of the dawn)’,
if grows td quia, Lett. aust ‘it dawns’, etc. 0 also ¢qus-tero- in words for ‘east’
(1245). Walde-P. 1.26f. Ernout-M. 93, Walde-H. 1.86. Pedersen 1.82. Grk. Hom. 70s, Aeol. atws, Att. éws; lat, aurdra (mostly poet., as also the jit. It. Sp. aur
```


## [2026-09-06T20:37:08.648Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"14\\.4[0-9] [A-Z]\" SYN.txt | head -20; echo \"== shout section ==\"; grep -n \"18\\.1[0-9] [A-Z]\\|SHOUT\" SYN.txt | head -20"
}
```


### [2026-09-06T20:37:08.719Z] TOOL RESULT

```
24297:CHAPTER 14 TIME! 14.43 ae 14.44 ay 14.45 YounG 14.46 OLD 14.47 Barty (adv.) 14.48 Late (adv.) 14.49 Now 14.51 14.52
25291:TIME 991 14.41 DAY Goth. dags Lith. diena utp ON dagr Lett. diena jplpa Dan. dag ChSl. dint diés FS) Sw. dag SCr. dan giorno ( OE dag, dagor Boh. den jour ME day Pol. dzien dia NE day Russ. den’ (a . Du. dag Skt. ahan-, dina- laa, laithe, ae OHG tag diva(sa)- : la MHG tac Av. ayan-, azan-, OPers. ee NHG tag rauéa ei the majority of the words for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI.
25300:14.42 NIGHT Grk. vot Goth. nahis Lith. naktis ; NG voxra ON noatt Lett. nakts ; Lat. nox Dan. nat ChSl.  noStt i It. notte Sw. natt SCr. noé jj Fr. nuit OE nitht Boh. noc Ft Sp. noche ME night Pol. noc Rum. noapte NE night Russ. not! i Ir. adatg (nocht) Du. nacht Skt. ratrz., ksap-, nakt- 8 NIr. _ oidhche OHG = naht Av. OPers, 2Sap- W. nos MHG naht Br. noz NHG nacht tl Most of the words for ‘night’ belong general Slavic; Ved. nakt- (nom. Sg. nak, to an inherited group, pointing clearly | acc. sg. naktam), nakti- (class. Skt. only ( to an IE word for ‘night’. In Irish, ex- | adv. naktam ‘by night’, cf. Wackernagel, cept for an adv. relic, and in Indo- | Altind. Gram. 3.233 ff.); Alb. naté;— \ Iranian, except in Vedic and a classical | with e-grade Hitt. nekuz ‘evening’, : Skt. adv. relic, the old word was dis- | nekuzi ‘goes to bed’ (Sturtevant, Hitt, lL placed by others, but’ elsewhere has per- | Gloss. 108). i sisted as the usual word to the pres- 2. Ir. adaig, aidche, NIr. oidhche, ent day. etym. dub. Walde-P. 1.34. Walde-H. : 1. IE *nokt(t)-. Walde-P. 2.337 ff. | 1.61. Stokes 326. ( Ernout-M. 682. Sturtevant (connect- 3. Skt. rdtri- : Grk. Anr&, Dor. Aard ; ing this group and that for ‘naked’, | ‘Leto, mother of Apollo and Artemis’, : 4,99) JAOS 52.10, Hitt. Gram. 122 f, orig. personification of the night, perh. Grk. vit, vuerés, NG vixra (v prob. | fr. the root in Grk. \6w ‘be hidden’, fr. a reduced grade); Lat. nox, noctis | ete. Walde-P. 2.377. Boisacq 555. n (> Romance words); Ir. nocht (in in- | Uhlenbeck 248. Y nocht ‘tonight’), W. nos, Br. noz; Goth. Skt. ksap-, Av. xap-, rfapan-, xSapar-, Mi nahis, ON ndtt, etc., general Gmc.; Lith. | OPers. xsap- (Barth. 548 f.) : Grk. pédas, naktis, Lett. nakts; ChSl. nostt, etc., | pédos ‘darkness’. Walde-P. 1.524 f. h q ‘ 14.48 DAWN Grk. dus, Sp8pos Goth. : Lith. auSra, brékSta x NG aby}, xapépyara, ON — dagan, dagsbrin Lett. rita blazma, rila Xapavyy Dan.  dagning, daggry krésla, ausma D Lat. aurora, prima liz Sw.  dagning, gryning ChSl. rano(adv.), -brézgi, di It. alba, aurora OE degréd, degrima, zore (pl.) Fr. ube, aurore dagung SCr. ora, svanuce 1 Sp. alba, aurora ME  dawing, dawning, Boh.  svitdnt, risvit Rum. zori, auroré dayrawe, etc. Pol. Swit, brzask, zorza Tr. dedal NE dawn, daybreak Russ. zarja, razsvel i) Nir. fainne an lae Du. —dageraad Skt.  ugas-, aruna-, pra- D W. = gwawr OHG = morgenrot, -rata, bhata- i Br. goulou-deiz, tarz tagarat Ay. uSah-, astir- ! an deiz MHG morgenrét, -rale,
25353:14.44 MORNING
25391:14.45 NOON
25404:TIME 997 14.46 EVENING - Goth. andanahti Lith. vakaras loxtpm of i ON kveld, aptann Lett. sakars tor tp%y espera Dan. aften (kveld) ChSl.  veterit vespery Sw. afton, kvall SCr. _ veéer ee OE @fen : Boh.  veéer one ME even, evening Pol. wieczor : a NE evening Russ. veéer ‘ ie Du. avond Skt.  dosa-, sdya- jrathndna OHG abant Av. arazah- vin nos, WWYT MHG dbent ryardaee NHG abend part from an inherited group, of | sera, above). Pedersen 1.208. Loth, ions, words for ‘evening’ are Mots lat. 178.
25431:dosas-), pradosa- (cf. Av. daostara-, Skt. sdya-, perh. : Lat. sérug ‘ate daoSastara- ‘western’) : Grk. dbounat, dbvw | Goth. seibus ‘late’, etc. Walde-P, 2.461, ‘sink, go down’, dvopat ‘setting (of the | Uhlenbeck 334. ie sun), west’. Walde-P. 1.777f. Uhlen- Av. arazah-, etym. dub. Barth, 202 J beck 181. Walde-P. 1.82. 5 ' j 14.47 TODAY J i, Grk. — oyjpepov Goth. himma daga Lith. Sandien } NG onpepa, onpepov ON i dag Lett.  Suodien I st Lat. hodié Dan. i dag ChSl.  dintst ii It. oggi Sw. i dag SCr. danas i Fr. aujourd’ hut OE t6 dag Boh. —dnes \ Sp. hoy ME today Pol. = dzié Rum. astdzi, azi NE today Russ.  segodnja I Tr. indiu Du. heden, vandaag Skt. adya i Nix. indiu OHG  hiuiu Av. I W. heddyw MHG hiute ‘ Br. hizto NHG heute For 14.47-14.49, cf. Brugmann, Zu | epds. of Ir. article in(d) and Britannic | den Wortern fiir ‘heute’, ‘gestern’, ‘mor- | pron. stem he- (IE *so-) with old dat, gen’ in den idg. Sprachen, Ber. Siichs. | (orig. instr.) sg. of the word for ‘day’, Ges. 1917, No. 1. Ir. dia, etc. Pedersen 2. 92, 190. The expressions for ‘today’ are all de- Thurneysen, Gram. 217. rived from the words for ‘day’ (14.41), 4, Goth. himma daga dat. sg. (once but many of them are, unlike NE foday, | also hina dag acc. sg.), lit. ‘this day’ so disguised in form that there is no con- (pron. stem hi- fr. IE *fi-). sciousness of the relationship. The com- ON @ dag, Dan., Sw. 7 dag (also dag), ( bination with the pron. stem IE *hi-, | phrase with prep. 7 ‘in’; similarly OE seen in Lat. cis, citra ‘on this side’, Lith. | 10 deg, ME to day , NE today with to, } Sis, ChSI. st- ‘this’ is common to Grk., | and Du. vandaag with van ‘from, of”. Balto-Slavic, and a part of the Gmc. Du. heden, MDu. héden, beside ! forms. hude(n), OS hiudu, OHG hiutu, MHG s 4 1. Grk. Ion. ojpepov, Dor. capepov | hiute, NHG heute, fr. *hiu-tagu ‘on this (Att. riuepov rare), NG pop. oxuepa, fr. day’, cpd. with pron, stem in Goth. t A *xduepov, fr. auépa ‘day’ and pron. stem himma, etc. (above). Weigand-H. ( F *ki-, *ky-. Walde-P. 1.452f. Boisacq | 1.860, Franck—v. W. 237.
25454:14.48 TOMORROW
25472:14.49 YESTERDAY
== shout section ==
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
31450:18.11 WOICE (sb.)
31475:18.12 SING
31498:18.18 SHOUT, CRY OUT
```


## [2026-09-06T20:37:13.247Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25340,25400p' SYN.txt"
}
```


### [2026-09-06T20:37:13.317Z] TOOL RESULT

```
morgenréte, lit. ‘morning-red(ness)’. Weigand-H. 2.219. Kluge-G. 399.
NHG morgendémmerung, lit. ‘morn- ing-twilight’, (démmerung, OHG demar ‘twilight’ : Skt. tamas- ‘darkness’, etc., 1.62).
6. Lith. bréksta (with vb. brékst2), ChSl. brézgit in probrézgi (‘time before dawn’, Mk. 1.35), Pol. brzask (Boh. bresk ‘twilight’, Russ. obs. bresk ‘dawn’), with vbs. Russ. brezzit ‘dawns’, Boh. briskd se ‘becomes dark’, etc. : Skt. bhraj-, Av. braz- ‘shine, beam’, Goth. bairhts, etc. ‘bright’. Walde-P. 2.170. Berneker 85.
Lett. rita blazma, lit. ‘morning shine’. Mihl.-Endz. 1.312.
Lett. rita krésla, lit. ‘morning twilight’ (like NHG morgendémmerung). Mihl.- Endz. 2.276.
7. ChSl. brézgti, etc., above, 6.
ChSl. rano, adv. rendering ép8pos, 6p8ptos, See 14.16.
SCr. zora, Pol. zorza, Russ. zarja, lit.
‘shine, splendor, redness of the sky’ (sometimes with adjs. ‘of the Morning? to designate the dawn in particular) ChSI. zorja ‘ray of light’, pl. ‘dawn’ (eg, vt zore Supr. 205.21) : ChSl. ztrey ‘see, glance’, Lith. Zéréti ‘shine, sparkle’, Btn, Walde-P. 1.602. Trautmann 366...
SCr. svanuée, Boh. svitént, usvit, Pol, Swit, Russ. razsvet : vbs. SCr. svanuti Boh. svttati (se), Pol. Switaé, Russ. svetai! ‘grow light, dawn’, ChSI. svitcli, svinati, svitati, etc. ‘shine’, svéti ‘light? (1.61).
8. Skt. aruna-, lit. ‘reddish’, as ‘dawn’ chiefly personified as the chariotecer of the sun, hence aruni- ‘dawn’ (RY) : arusa- ‘red, fire-colored’, Av. aruga- ‘white’. Walde-P. 1.159.
Skt. prabhdta-, lit. ‘having shown forth, become light’, fr. pra-bha- ‘shine forth’, bha- ‘shine’.
Av. astr-, lit. (period of day) ‘until morning’, epd. of a- ‘to, until’, and sur- ‘morning’. Barth. 221. Or with neg. a- as ‘not (yet quite) morning’?
14.44 MORNING
Grk. (és), zpwta (late) Goth. maurgins Lith. rytas
NG mpwt ON morginn Lett. —rits
Lat. méne, matitinum Dan. morgen ChSl.  utro, jutro
It. mattino (-a) Sw. morgon SCr. jutro
Fr. malin OE morgen, mergen Boh. jitro, réno
Sp. manana ME —_ morwen, morwening Pol. rano, (po)ranek Rum. diminea{é NE morning (morn) Russ. tro
Ir. maten Du. morgen Skt. pratar (adv.), vastu-, Nir. maidin OHG morgan apicarvara- W. bore MHG morgen Av. stir-
Br. beure NHG morgen
Words for ‘morning’, though many of them orig. denoted the time of dawn or sunrise, are used more comprehensively to include all the early part of the day (up to noon, and even in this scope not ousted by new terms like NE forenoon, ete.). Several are connected with the advs. for ‘early’ (14.16), others with the old word for ‘dawn’ (14.43) or from no- tions applicable to the dawn or sunrise.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1. Grk. és ‘dawn’ (14.43) some- times extended to ‘morning’, for which there is no distinctive word in classical Greek.
Late Grk. xpwta (LXX, NT+), for mpwta dpa ‘early time of day’, fr. adj. mpwios, fr. adv. mpwt ‘early’ (14.16), NG ‘in the morning’ and sb. 7é mpwt ‘morn- ing’. i 2. Lat. mane, indecl. sb. ‘morning’
uo the morning, early’ (14.16).
ug *maneana) Sp. manana.
“tence It. mattino, mattina, Fr. NIr. maidin. Ernout-
“Tr, maten ality I OW Vendryes, De
REW 5434.
} , deriv. of late Lat. ‘tomorrow’,
pa > Fr. aenane ( REW 2348.
ate.), fr. mane Puseariu 1083. 3, Ir, maten, NIr. maidin, above, 2. W. bore, Br. beure : Ir. imbarach ‘to- morrow’, but etym.? Pedersen 1.99. Jimmer, KZ 30.17 f. Loth, RC 36.179 (vs. Morris Jones 163).
(above).
4, Goth. maurgins, ON morginn, OE morgen, etc., general Gme. (ME mor- wening, NE morning, with addition of suffix -ing) prob. (as orig. denoting the moming twilight) : ChSl. mriknati, mriicati ‘become dark’, Lith. merkti shut the eyes, wink’, ChSl. mraki ‘latkness’, beside Lith. mirgéti ‘glim- mer, twinkle’, fr. a guttural extension of the root in Grk. pappatpw ‘flash, gleam’, Skt. marici- ‘beam of light’. Walde-P. 2.274, Falk-Torp 731. Feist 350.
: Lith. rytas, Lett. rits : Lett. rietét . out, break forth’ (sun, light, etc.), * urresan, ON risa, etc. ‘rise’.
‘0
TIME
Digitized by Arya Samaj Foundation Chennai and eGangotri
995
‘Morning’ fr. ‘(sun)rise’. Walde-P. 1.141. Miihl.-Endz. 3.541.
6. ChSl. utro, jutro, SCr. jutro, Boh. jitro, Russ. utro (Pol. jutro now adv. ‘to- morrow’), prob. (despite the phonetic difficulty of tr fr. str, perhaps due to a blend) fr. *ustro (cf. ChSl. za ustra = za utra), *ausro- : Skt. usas-, Lith. ausra, etc. ‘dawn’ (14.43). Berneker 462 f. Meillet, Etudes 406. Briickner, KZ 46.212 ff.
Boh. rdéno, Pol. rano, (po)ranek : ChSl. adv. rano ‘early in the morning’ (14.16).
7. Skt. pratar, adv. ‘early’, and ‘in the morning’ (14.16), more usual than sb. forms (pratah pratah ‘every morning’, pratahkala- ‘morning time’, etc.).
Skt. vastu- (RV) ‘early morning’, lit. ‘time of dawn’, fr. vas- (3sg. ucchatt) ‘srow bright, shine (of dawn)’, the same root as in the old word for ‘dawn’ (14.43). Cf. Zimmer, Altind. Leben 361.
Skt. apicarvara- (RV) ‘early morning’, lit. (bordering) on the (starry) night’, fr. carvara- ‘gay, speckled’, fem. ‘starry night’. Cf. Zimmer, Altind. Leben 361 te (with other terms used for various times of morning, as sarigava- ‘time for gather- ing the cattle for milking’, prapitva- lit. ‘pressing forward’ (of the day), fr. pt- ‘swell, become fat’).
Av. siir-, only in acc. sg. stiram as adv. : Skt. cvas ‘tomorrow’, Av. savahi- ‘the east’, with n-suffix Skt. cona- ‘red’, etc. Walde-P. 1.368. Barth. 1631.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.45 NOON
HeonpBpla Goth. Lith. pietas NG Heonpépe ON mtor dagr, middegi, Lett. pusdiena, dienasviq, Lat. _meridiés hddegit ChSl.  poludine 2 It. mezzogiorno, mezzodt Dan. middag SCr. podne Fr. midt Sw. middag Boh. _ poledne Sp. mediodia OE middag Pol. poludnie Rum. amiazi, miezul zilet ME ~~ midday, none Russ. olden’ Ir. medon lat NE noon, midday Skt. madhydhan-, madhy- Nir. _meadhon lae, eadradh Du. middag, noen amdina- W. canol (hanner) dydd, OHG. mittitag Av. aram-pi0wa-, ra- nawn MHG mit(te)tac piowa- Br. kreisteiz NHG mittag
Most of the words for ‘noon’ are such as mean lit. ‘mid-day’, or in some cases ‘half-day’, rarely ‘high-day’. A few orig. denoted the (principal, i.e. midday) ‘meal’. Quite otherwise NE noon (see below, 5).
1. Combinations of words for ‘middle’ (12.37) and ‘day’ (14.41). Grk. peony Bpia (: juépa with reg. up > uBp), NG 76 Heonuépt (formed anew, with dim. type); Lat. meridiés (for medidiés by dissim.), It. mezzogiorno, mezzodt, Fr. midi (OFr. di ‘day���), Sp. mediodia, Rum. amiazi, amiadi (Lat. ad mediam diem), miezul zilet; Ir. medon lai (laithe), NIr. meadhon lae; W. canol dydd, Br. kreisteiz; ON mior dagr (also cpd. middagr), middegi, OE middeg, OHG mittitag, etc. (also two words as in ON, OE midd dag, OHG mitt, mitter tag, MHG mitter lac); Lett. dienasvidus (lit. ‘day’s middle’); Skt. madhyahan-, madhyamdina-.
2. Combinations of words for ‘half? (13.24) and ‘day’. W. hanner dydd; Lett.
pusdiena; ChS]. poludine, etc., general Slavic.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
3. ON hddegi (usual word in NIcel.), lit. ‘high-day’ (cf. also early NE high- day in this sense, NED s.y. 2).
4. NIr. eadradh, gen. eadartha (Din- neen, McKenna), fr. eadar ‘between’, but perh. blended with a form like Ir. anteirt, W. anterth ‘forenoon’, fr. Lat. ante (or inter, intra) tertiam (horam). Loth, Mots lat. 133.
5. ME none, NE noon, fr. Lat. néna (sc. hdra) ‘ninth hour’ (about 3:00 P.M.), but since 14th cent. usually ‘noon’, owing to a change in the time of the eccl. office or a mealtime (cf. the shifts of time among terms for ‘breakfast’, ‘lunch’, and ‘dinner’, 5.42-5.44). NED s.v. Simi- larly, OF r. none (still dial. for ‘mid-day meal’), Du. noen (now mostly obs.), and W. nawn (as ‘noon’ prob. semantic bor- rowing fr. English).
```


## [2026-09-06T20:37:26.285Z] TOOL CALL #27: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/264.jpg"
}
```


### [2026-09-06T20:37:26.331Z] TOOL RESULT

```

```


## [2026-09-06T20:37:36.383Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 264 -l 264 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg264hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg264hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.5),int(h*0.42),int(w*0.82),int(h*0.50))).save('crop_pers.png')\nim.crop((int(w*0.2),int(h*0.23),int(w*0.55),int(h*0.28))).save('crop_op.png')\nim.crop((int(w*0.2),int(h*0.46),int(w*0.5),int(h*0.51))).save('crop_me.png')\n\""
}
```


### [2026-09-06T20:37:39.626Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T20:37:41.725Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_pers.png"
}
```


### [2026-09-06T20:37:41.745Z] TOOL RESULT

```

```


## [2026-09-06T20:37:46.450Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_op.png"
}
```


### [2026-09-06T20:37:46.466Z] TOOL RESULT

```

```


## [2026-09-06T20:37:46.493Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_me.png"
}
```


### [2026-09-06T20:37:46.505Z] TOOL RESULT

```

```


## [2026-09-06T20:37:50.713Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg264hi.png'); w,h=im.size\nim.crop((int(w*0.2),int(h*0.49),int(w*0.5),int(h*0.535))).save('crop_me2.png')\n\""
}
```


### [2026-09-06T20:37:52.620Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:37:54.602Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_me2.png"
}
```


### [2026-09-06T20:37:54.617Z] TOOL RESULT

```

```


## [2026-09-06T20:38:14.208Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD1 page 378 context ===\"; sed -n '23770,23790p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"--- pages file ---\"; grep -n \"qeud\\|keuq-\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-09-06T20:38:14.268Z] TOOL RESULT

```
=== WLD1 page 378 context ===
ziehung zu den germ. Sippen ' von got. skcivjan — doch s. unter sqeq- 
„springen“ und qSu- „wackeln“ — , urid ahd. scac, mhd. schoc, -ekes ,,Wind- 
stoB, schaukelnde Bewegung“, nhd. Schaukel, ferner von mhd. schiech 
„scheu“, ags. sceoh „angstlich“, mhd. schhihe , nhd. Scheu, mnd. schuwc, 
schii „scheu, furchtsam“ stehen konnte, s. Wood Min. 21,228, Fick III 4 
467, Falk-Torp u. sky, skur II, skure, fur welche Gruppe abg. scuti „hetzen‘‘ 
(Berneker IF. 10, 155; trotz Prellwitz 2 416 nicht als Lw. aus mhd. sciahen 
„scheuchen“ verstandlich) auf velares q weist (lit. sauju, -ti „schieBen“, 
abg. sujq, sovati „stoBen, schieben" liegt in der Bed. den germ. Worten 
etwas ferner, doch s. u. skea „werfen“). Doch auch dies ganz unsicher; 
beachtenswert ist Scheftelowitz’ BB. 28, 294 Yergleich von skura windis 
mit arm. curt „balt; Kalte, Schauer" aus skiir-do-. — Mir. ciia, gen. cmd 
„Winter“, cymr. (usw.) cawad, cawod „Regenschauer“ (Fick II 4 74 zw.) 
bieten keine zuverlassige Wzvergleichung. 

keuk-, kuk- „durcheinandermischen, wirbeln ££ ? 

Bezzenberger BB. 27, 170 verbindet gr. xvxkov „Mischtrank“, y.vxdaj 
..riihre ein, misehe“, y.vxy&Qov „Ruhrkelle ; ‘ (s. auch Yf. LEWb. 2 u. cocc- 
tum , cinnus ) mit lett. susla „ein mit Syrup suB gemachtes Getrank“ (= russ. 
suslo n. „Bierwiirze“ nach Yasmer [miindlich]), lit. sdtdstas „L6fFel £ ‘, siuks- 
--- pages file ---
34473:s. qeud-);
35314:37S                                                                tenq           qeud-
35317:keuq-           ,   leuchten, hell, weiB sein. gliihen".
35377:    qeud- „schreien; anschreien, schelten, liohnen, spotten".
35472:skundd „Anklage“ fern, s. u. sqeud- „unwillig sein“), Persson Beitr. 1 S6 f.
```


## [2026-09-06T20:38:14.286Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1325' SYN.txt | head -50"
}
```


### [2026-09-06T20:38:16.147Z] TOOL RESULT

```
7.41), ‘object, thing’, etc., also ‘meaning’. Walde-P. 1.186. Uhlenbeck 13.
17.34 CLEAR, PLAIN (To the Mind)
Goth. skeirs, bairhts, swi- Lith. azikus , caps, vapyns , ) ce ce, si dis kunps Lett.  skaidrs iat clarus, planus, aper- ON skgrr ’ ChSl. (j)avé (adv.), jasno ; tus, évidens, etc. Dan. klar, tydelig (ady.) It chiaro Sw. klar, tydlig SCr. jasan Tr. clair OE swutol Boh. jasny Sp. claro ME cler, pleyn, sutel Pol. jasny Rum. clar NE clear, plain Russ. jasnyj, javnyj Ir _ follus, reil Du. klaar, duidelijk Skt.  spagta-, vyakta- Nir.
```


## [2026-09-06T20:38:22.611Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31490,31530p' SYN.txt"
}
```


### [2026-09-06T20:38:22.661Z] TOOL RESULT

```
6. Lith. dainuoti (Lett. dial. dainuot ‘sing’, refl. ‘dance’) : Lith. daina, Lett. dain'a ‘folksong’, outside connections? Miihl.-Endz. 1.432.
Lith. giedoti, Lett. dziedat, above, 2.
7. ChSl. poja, péti, SCr. pjevati, etc., general Slavic, in part epds., outside connections? Miklosich 245. Briickner 404,
8. Skt. ga-, above, 2
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
VV
Digitized by Arya Samaj Foundation Chennai and eGangotri
1250 SELECTED INDO-EUROPEAN SYNONYMS
18.18 SHOUT, CRY OUT
Grk.  Bodw, xpafw, xpavyatw Goth. hropjan, wopjan Lith. rékti, Saukti NG = gwvatw ON epa, kalla, hropa Lett. kliegt, sauke Lat. clamare Dan. raabe ChSl. vitpiti, vitztipiti, kpy It. gridare Sw. ropa tati 1s Fy. crier OE hryman, clipian, hrd- = SCr. _kritati, vikatj Sp. gritar pan Boh. —kiiéeti Rum. siriga, {ipa ME _ shoute, reme, clepe, Pol. —kerzyczeé Ir. gatrim rope Russ. kriéat’ NIr. _gairim, glaodhaim, NE _ shout, cry Skt. krue- screadaim Du. schreeuwen, roepen Av. xraos- W. bloeddio OHG  (h)ruofan, harén, Br. krial scrian
MHG ruofen, schrien NHG - schreien, rufen
Most of the words for ‘shout, cry out’ are of imitative origin, as are numerous others covering ‘scream, screech, shriek, yell’, etc. (cf. also 18.14). Several of those listed here are also used for ‘call’ = ‘summon’ (18.41).
1. Grk. Bodw, with sb. Bor ‘shout, cry’, prob. of imitative origin. Walde-P. 2.112. Other views in Boisacq 125.
Grk. xpé¢w, also and perh. orig. ‘croak’ (of frogs), ‘caw’ (of ravens), cf. xpatw ‘caw’, prob. : ON hrodkr, OE hréc, etc. ‘rook, raven’, Skt. kharj- ‘creak’, khar- gala- ‘a, certain night-bird’, all of imita- tive origin. Walde-P. 1.415. Boisacq 505.
Grk. xpavyétw, with sb. xpavyn ‘cry, shout’, perh.: ON hraukr ‘cormorant’ (but cf. Falk-Torp 866), Goth. hruk ‘crowing’, hrukjan ‘crow’, fr. *krau-g-. beside *krau-k- in ChSl. krukii ‘raven’, ete., *krau-k- in Skt. kruc-, Av. xraos- ‘ery, shout’, etc. (below, 7), all from parallel extensions of the root in Kpatw
(above). Walde-P. 1,417. Boisacq 511 f.
NG guvafa, fr. dart ‘voice’ (18.11).
2. Lat. clamare : calare ‘call, out, pro- claim, summon’, Gri. xadéw ‘call, name’, kéhados ‘noise’, Lett. kal’uot ‘chatter’, Lith. kalba ‘language’, etc. Walde-P. 1.443 f. Ernout-M. 136,192. Walde-H. 1.141 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
It. gridare, Fr. crier, Sp. gritar, fr. Lat, quirttare ‘cry plaintively, wail, scream’, this prob. of imitative orig. like quirritare ‘grunt’, Ernout-M. 844. REW 6967. Gamillscheg 278.
Rum. sériga, deriv. of Lat. striz, -gis ‘sereech-owl’. Puscariu 1656. Tiktin 1514 f.
Rum. tipa, doubtless based on some imitative syllable.
3. Ir. gairim, NIr. gairim (4 fr. gdir; gairim, goirim ‘call’ = ‘summon, name’), beside sbs. gairm and gdir ‘a cry’ : W. gawr ‘a cry’, gair ‘word’, Lat. garrire ‘chatter, prate’, Grk. yjpus, Dor. yapus ‘voice, speech’, etc. Walde-P. 1.537. Walde-P. 1.537. Walde-H. 1.533. Pe- dersen 1.144, 2.533 f.
NIr. glaodhaim, with glaodh, MIr. gloed ‘a shout, cry’, Olr. glaidim, gloi- dim ‘bellow, roar’, root connection? Pedersen 2.538 Anm.
NIr. screadaim, fr. sb. scread, Ir. secret: Dan. scratte ‘give a cracked sound’, etc. Walde-P. 1.415. Falk- Torp 1025. Loth, RC 43.151 f.
W. bloeddio, fr. bloedd ‘cry, shout’ = Ir. blaed ‘cry, clamor’, etym. dub. Walde-P. 2.211, 218.
Br. krial, fr. Fr. crier. Henry 81.
4. Goth. hropjan, ON hrapa (but older sense ‘slander, defame’; that of ‘ery out? fr. LG ropen > Dan. raabe, Sw
| | | | | j t ! | }
Digitized by Arya Samaj Foundation Chennai and eGangotri
VOCAL UTTERANCE, SPEECH; READING AND WRITING 1251
OE hropan, ME rope, Du. roepen, h)ruofan, MHG ruofen, NHG
(now esp. ‘call’, 18.41) with sbs. rufer ie c ) . Goth. hrops, OHG ruof ‘cry’, etc., root ponnection dub., perh. of imitative origin. Walde-P. 1.353. Falk-Torp g65. Feist 270.
Goth. wopjan, ON epa : OHG wuofan, OEwepen ‘weep’ (16.37). Walde-P. 1.217. Feist 572.
ON kalla, also ‘call, summon’ = OF callian (once; ME calle, NE call, prob. fr, ON), OHG callén ‘talk much or loud, chatter’ : ChSl. glasti ‘voice’, ete. (18.11). Walde-P. 1.538. Falk-Torp 485f. NED s.v. call.
OE hrgman, ME reme, deriv. of OE hrgam, ME ream ‘cry, outcry, tumult’, cf. ON hrawmi ‘noisy fellow’, perh. : Skt. kdrava-, Lat. corvus ‘raven’, from an extension of the root seen in Grk. xpatw, kpavyatw, etc. (above, 1). Walde- P. 1.417. Walde-H. 1.275.
OE clipian, ME clepe, cf. OF ris. klippe ‘ting’, LG klippen ‘sound, resound’, NHG dial. kliffen ‘yelp, yap’, all prob. fr. an imitative syllable parallel to that in clappan ‘clap’, OHG claphén ‘clap, resound’, etc. Cf. NHG klipp beside klapp! NED s.v. clepe, vb. Weigand- H. 1.1046.
ME shoute, NE shout : ON skuia, skitti ‘taunt, jibe’, prob. fr. *skeud- be- side *keud- in Grk. xvdatw, Skt. kuts- ‘tevile, abuse’. Walde-P. 1.378.
ME crie, NE cry, fr. Fr. crier (above, 2).
OHG serian, MHG schrien, NHG schreien, Du. schreeuwen : Dan. skrige, Sw. skrika, ME shriken ‘shriek, scream’, Ste., Gri. kpifw ‘creak, screech’, ChSl. oe ‘a ery’, vb. krigati, etc. (below, 6), ote fr. *(s)krei-, extension of the
Seen in Grk. xpdtw, etc. (above, 1). ae 1.416, Falk-Torp 1027f. nek-y. W. 598,
```


## [2026-09-06T20:38:28.757Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; echo \"---\"; grep -n \"سورنا\\|سورنای\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-06T20:38:28.820Z] TOOL RESULT

```
---
35657: ‫پر می " مخفف سورنای‌است که نای‌رومی باشد‪.‬‬         ‫میشود ‪ .‬استنزال (‪ )۱‬اودررجمت بزیت وطرون‬
```


## [2026-09-06T20:38:30.442Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD sur ===\"; grep -n \"^sūr\\|sūr \\|sur '\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD nikoh ===\"; grep -n \"nikōh\\|nikoh\\|nigōh\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"sūr\\|nikōh\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T20:38:30.524Z] TOOL RESULT

```
=== PHD sur ===
PHD.txt:572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
=== PHD nikoh ===
PHD.txt:1010:blame (n.) āwēnišn, érang(ih), nikoh-
PHD.txt:5176:пірӣг- nigárag nigastar !màdag! mādagīhī nigēxtan kuš-! kuštanī niger- nakkīrā nakkīrāyīh nigerīdan nigerišnīg nigerišn nigēz nigéz- nigēzišn wak nikēh- nikēhīdan nikēhišnīg nikohisn nigünih nigün
PHD_mackenzie.txt:6045:beget (frazand) warzidan.                   blame (n.) iiwenisn, erang(ih), nikoh-
PHD_mackenzie.txt:6048:behaviour barisn, rawisnih, warisn.             nikohidan.
PHD_mackenzie.txt:6050:being axw, sti; come into"'" hambiis-       blameworthy awenisnig, nikohisnig.
PHD_mackenzie.txt:6550:execrable nikohisnig.                              far duro
PHD_mackenzie.txt:6551:execrate nikohidan.                                farmer dahigan, (dehgiin); v. hus-
PHD_mackenzie.txt:10093:                       \\"""~,       nikoh-               - .....,,'\
PHD_mackenzie.txt:10094:wircz-                     -.},      nikohidan           \\~",
PHD_mackenzie.txt:10095:w~lranigih             -"U '-l ~,    nikohisnig          \~~\~,
PHD_mackenzie.txt:10096:waranig                   ,!.\ ~ ,   nikohisn             \~\S,
=== NYB ===
2110:Jafar [y?pl] n. pr. Arab Ja‘far: abu [bw] ~ 117?! the calif al-Mansūr.
3562:sūlāk [swl’k] hole, aperture, gap 4419-22, 4927, 10222, 10317-18, — Cf Av. (1585) sūra- ‘hole’; Paz. sila (SGV); NP sülàx, sūrās. As to the final -x ef s. v. Sak.
7420:sūlāx, sūrāx: sūlāk, šāk
```


## [2026-09-06T20:38:39.713Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nikōhīdan\\|nikohidan\\|nikōhišn\\|nikohisn\" PHD.txt | head -5; echo \"=== CHEUNG ===\"; ls CHEUNG.txt && grep -n \"nikōh\\|nikoh\\|kaud\\|kauH\\|kutsa\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T20:38:39.771Z] TOOL RESULT

```
5176:пірӣг- nigárag nigastar !màdag! mādagīhī nigēxtan kuš-! kuštanī niger- nakkīrā nakkīrāyīh nigerīdan nigerišnīg nigerišn nigēz nigéz- nigēzišn wak nikēh- nikēhīdan nikēhišnīg nikohisn nigünih nigün
=== CHEUNG ===
CHEUNG.txt
22328:semantically similar roots: *dauH and *skauH. 
22686:*skauH 347 
22712:*skauH ‘to poke, touch; to earmark, ? to cover’ 
22727:displayed by these forms, a connection with *skauH can hardly be doubted: *kauH 
29453:skaudrus ‘flowing quickly’ and several names of rivers in Lithuania, Skäudinis, 
29456:Skaudupelis, etc. = LIV: 372 | Pok.: 625 
52674:skaudrüs, 456 
55598:*Hrais, *said' (s.v.), *skauH 
55880:(s.v.), *skauH (s.v.), *tard 
56165:*skauH 
56452:*skauH 
57379:*skauH 
58234:*Hmars, *Hrab/f. , *skauH
```


## [2026-09-06T20:38:41.201Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ===\"; grep -n -i \"sur\\b\\|surna\\|nekuhidan\\|nikuhidan\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY persian ===\"; grep -n \"نکوهیدن\\|سورنا\\|سور \" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T20:38:41.280Z] TOOL RESULT

```
=== ARY latin index ===
519:Ab shoal etbtth til 92 S pte 9 SUR L Wj eat 37 22 end GOL,
2105:DELAMARRE: (SUR, AU-DESSUS) 303 {OLD HIGH GERMAN) gS glasT
2727:nl ot ae UT gow oj pl Sal Fath ey par jT eed Sur pt "Sp jls”
4458:Srp gt e Cosa g! "SUR 9 4) PAs *PATy *PET- gly) gta eal bats call
6939:SCHAHER, SCHWIEGER- SKESUR, KVEKURA
9848:gly Sur oe ply SG SCHATTEN SLIT y SHADOW 5 SHADE 15) plsjiy -\
10541:. (697: POKORNY) cael 4) eas jj (SUR 245 phy SUXRA: glee) “ee” ges fly “1
10547:‘REFERENCES bethy sUR (PAHLAVI) «5 Sy
10637:SAIR, SROY, SUR (ARMENIAN) <I
11090:ONIONS: (sur sat = Poko. =—SSSC=~S~S~«é
=== ARY persian ===
191:چسر رس ری سور ی از کش
693:717 5۳7۸7۸1۸37۳858۹) سلطان آسور (۸۵۸ تا ۸۲۴ قبل از میلاد) خراج می‌دادند. از فحوای
10759:۴ سور (به چم *جشن و مهمانی" *خوراک") :
14780:نکوهش, نکوهیدن / ۴۹۹
16164:مها پرسور میور چیوز جم جوزرمتی‌زد بش00 ۸ بت۸ ,18082 و
```


## [2026-09-06T20:38:47.400Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY sur ===\"; sed -n '10740,10790p' incoming/ARY/ARY_pages.txt; echo; echo \"=== ARY nekuhidan ===\"; sed -n '14760,14810p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T20:38:47.475Z] TOOL RESULT

```
=== ARY sur ===

یادداشت:

9 (صفحه‌ی ۱۰۴-۴۱) می‌گرید واژه‌ی فارسی نوین "سفلیدن" يا "سبفلیدن" (8171,18880) نیز از همین
ْ واجریشه است ولی این واژه را در هیچ کدام از فرهنگه‌ها نیافتم. شاید منظورش "سرفیدن" به چم "سرفه کردن" باشد
۱ (لغت نامه دهخدا: ۱۳۹۰۸)

و یی
ِ

ا
۱ اوستایی (/487۵2): بلوچی (2171ل8۸): 517811۸671 ,بش81
ا 800۳1 ,85۸007771 افقانی (پشتر) (//4۳0۸): بل۸ل5 م832۸
۱ پهلری (۲7مانله): 9021510 ,8027۸0 سانسکریت (5/8077):

اوستی (0858776): ,ااتاژه5 1 ات80
کردی: (۳)8015): لااران
سا را
[pdf page 363]
۴ سور (به چم *جشن و مهمانی" *خوراک") :
پسگشت‌ها دای کدی را 5 (81783:1370 ,80ت81)
:215 1
یادداشت: ۱ 0 یی ۳
۱ واژه‌ی فارسی "سرخ" (اوستایی:511733۸؛ پهلوی: 51174) نیز از همین ریشه است. (۳01۳0387۷ :897)
۲- بازگشت به: سوگك ۰
اوستایی (4۲85742: 51718۸ ,8118026
پهلری (الاصاتلهه): " 8 |[ پسگشت‌ها 3/5
کردی (0ل6/718): 3 5 200520
بلوچی (671لاماه8): : ان :۸/5/22
سانسکریت (54//570077): 5۷۸1 ,۸8۸۷۸37 : 4 (81ف۲5) ,133 متغتیه)
آرمنی (( ۰.۸۵152 5 3 (۹1ف۲۳۸) ۸2/2۵
لیترانی (/(414هلا7ل7ل): ادل ۱۹۱ فرهنگ معین + ۱۹۳۹
آنونی (لتی) (4774(۷): ۲۸038 ب۳۸11۸۸ برهان قاطع : ۱۸۵
پروسی کهن (لزفاک2۲۶ ۰:۵۵ ۷8اه
بادداشت. :
چم اين واژه در زبان اوستایی: سحر َ
چم این واژه در زبان بلوچی: جشن عروسی
چم این واژه در زبان ارمنی: درخشش
اوستایی (/(4۲557:4): 818718181۸ م8۵ 71 مف 5۸018
پهلری (41الل۸): ,81860 ارمنی (/4/42/4): #نا ,808
کردی (8720153): ۸ . بونانی (07550): 58 بال۸نا 3
افغانی (پشتو) (4۳۵[۸/7): و ادن لانین (47/۸0): ۲۸۷2۸۸ ,۴۸۸ ,2۸7118
۰ سانمکریت (8۸۸/57): فرانسه (ل۳72(/6): 7
[pdf page 364]
نج ا ‏
سوزن / ۳۶۵
اسپانبایی (5۸(154): نی دا
ایتالیایی (/4ل74: ۰ ۲۸۷۸ ,۳۸۷8801۸ پسگشت‌ها 0/5
پرتغالی (۵07000252: ۰ ۲۸۷88۸۸ 4 ۶0/0800
ایسلندی کهن (۸۸ 5010۸۷ 0ا۵): 2 (۷۳ه۲) ای
11۸ 5 ر(تام2ی ند هار

=== ARY nekuhidan ===
| برهان قاطع + ۳۳۶
اوستایی (/45374۸): ,11511۸577 اینالیایی (/4سل )7 55032
را آرازا ان با رومانی (۸(/14۸ان): ار رون
پارسی باستان (۳8۴۶/۸۸ صا0): پرتغالی (۳070010252): 3 ادن
۸۸( ,3۳۸513۸۸۸۵6 گرنبک (00700): 5۸8118۸ ,ال517۸
پهلوی (47ا۳۸/7): رال۸]۹1۸57۸ ایسلندی‌کهن (270۸۲7۵اییو صاه).
اد ان لا 7 5177۸4
کردی (6080[5(7): ان لا ساکسونی کهن (/5400 2ا۵): 87771۸0۲
بلوچی (84/67/7): ,۸۷1۸10۸077 ,31310۸0 فریزی کهن (۷مهاکل۳# ا0): 517۸
انیا انا آلمانی کهن (027440 104 صام):
افغانی (پشتو) (//0/۸/: ۰ ۸۸۵ ۸۸8۲۸5 2 ,512252
سانسکربت (5(/9/0/7): م5۸77 ,510۸71 آلمانی (/02/04/۸): 3
آرمنی (/4/۵481۸): بات لا انگلیسی کهن (#لقلله8۷ ص۵): 51۳2۸۲
یونانی (088870): 1380۸82 ,118213571۸ انگلیسی (83لا8(/0): ان
نراد انا دانمارکی (0۸0۷/54): 00
لاتین (7/0ا): ,5528 ,850575 سرئدی (582157): ۸
6 ,88080 نر و ژ وج/0۷/0۵/). بان
فرانسه (۳6۸/627): 3 اند ننک هلندی (قع007): 72۳7
اسپانیایی (1ل5۸13): 3 ادن
[pdf page 498]
نکوهش, نکوهیدن / ۴۹۹
اسلاری کهن (ع7/ما5 67767 طا0): پسگشت‌ها 5
1 55057 0
لهستانی (374/-01): 0 1 (517) ای ان دنا
روسی ((05914): 5017 5 (۸888018) :ما05
چکه (280/1): لاد زرلر ال 41 (55۸7) ,133 (817) ۰ :8ل02(2 ۸۸
اسلواکی 81.0۸0): لا ادن 83334 ۸
لیتوانی (71704(14(۷/): 58017 ,560577 0 (8917) :005
لنونی (لتی) (#14(۷آبما): اند 5 (817) :547
ایرلندی کهن (7ل5ل۶] 0/.2): 355 برهان قاطع :۰ ۳۱۳۵
یادداشست:
چم این واژه در ایرلندی کهن: صندلی,
پهلری (۲1مالله): ,۸۷1607110۸۷ سوئدی (517501577): 117۸
لانت انا ان نروژی (۸۷07#014/1(محلی) 1307۸
سانسکریت (7ل5۸(/52): ان ره لهستانی (۳0/87)(محلی) ‏ ۳323/۰ 88280
ام ون ره روسی (#1891۸(1): ۳
برنانی 0788/9): متفدناتن بلفاری کهن (0(مل۸#ت.اتاظ ا0):
ایسلندی‌کهن ((7۵ م5 صا0): 71 ,۲2100
۸ ,1107۸ ایرلندی کهن (8ل1۶ ضا۵): 107 ۱
1 ی آلمانی کپن (05/۵1۵(1 ۲ز0الا هام).
دنه ۰ 09 پسگشت‌ها 5
آلمنی روم کار نو ین
انگلیسی کهن (لادلا2۸0 ص۳ا0): ۰ 186 4 (315شآ8) :25 ت لا
انگلیسی (6(/01/5/4): 7007 6 (1007) +57
دانمارکي (0۸۸/827): 117۳ برهان قاطع + ۳۱۶۱
یادداشست,
۱- چم این واژه در زبان‌های ژرمنی و اسلاوی: فریاد؛ داد زدن,
۱
[pdf page 499]
۲ احتمال دارد که واژه‌ی انگلیسی 811017 هم از همین ربشه باشد.
اوستایی (4۲257۸۸): 8۸ق3۷[8۵* ,۸7قشگل۸ ۰
```


## [2026-09-06T20:38:59.140Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T20:38:59.147Z] TOOL RESULT

```


```


## [2026-09-06T20:39:03.428Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B1",
 "prompt": "Persian entry سور — give the etymology sections verbatim, especially any meaning 'feast/banquet' and its derivation from Middle Persian and Avestan (dawn/morning). Also any mention of سورنا."
}
```


## [2026-09-06T20:39:05.110Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DA%A9%D9%88%D9%87%DB%8C%D8%AF%D9%86",
 "prompt": "Persian نکوهیدن — give the etymology verbatim: Middle Persian form, Proto-Iranian root, cognates (Sanskrit kutsayati), any citation of Cheung or Hasandust."
}
```


### [2026-09-06T20:39:13.616Z] TOOL RESULT

```
# Response

I cannot provide the etymology information you've requested. The Wiktionary page shown does not contain details about Middle Persian forms, Proto-Iranian roots, Sanskrit cognates, or citations from Cheung or Hasandust.

The page only displays that **نکوهیدن** (nekuhidan) is a Persian verb meaning "to blame" or "to execrate," with derived terms listed. No etymological section appears in this content.

To find detailed etymology, you would need to consult a more comprehensive Persian etymological dictionary or academic sources on Iranian linguistics.
```


### [2026-09-06T20:39:13.860Z] TOOL RESULT

```
# Persian Etymology of سور (sur)

## Etymology Section

According to the Wiktionary entry, the Persian word سور (sur) derives from Old Persian *θūryas ("banquet, feast"), which traces back through:

- Proto-Iranian: *cuHryás
- Proto-Indo-Iranian: *ćuHryás  
- Proto-Indo-European: *ḱewH- ("to shine")

The entry notes a possible connection to Sanskrit śvas (tomorrow) and mentions potential relatedness to Northern Kurdish sor (red).

## Meanings

The Persian noun سور carries two primary definitions:

1. **"Nuptials"** — referring to wedding ceremonies
2. **"Banquet, feast, entertainment"** — denoting festive gatherings

## Note on سورنا

The Wiktionary entry provided does not contain any mention of "سورنا" (sūrnā). This term does not appear in the Persian section or elsewhere in the document.
```


## [2026-09-06T20:39:19.799Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shout",
 "prompt": "Give the full etymology entry for 'shout' verbatim, including Middle English form, dates, and any proposed connection to Old Norse skuta or a root meaning 'shoot'."
}
```


## [2026-09-06T20:39:21.387Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B1%D9%86%D8%A7",
 "prompt": "Persian سورنا — etymology verbatim: is it a compound of سور 'feast' + نای 'reed pipe'? Any mention of zurna, Turkish, Arabic."
}
```


### [2026-09-06T20:39:25.546Z] TOOL RESULT

```
# Etymology of "Shout" (Verb)

According to the Online Etymology Dictionary, the word "shout" originated around 1300 from Middle English forms *shouten* and *schowten*, meaning "to call or cry out loudly." The source states: "a word of unknown origin; perhaps from the root of shoot (v.) on the notion of 'throw the voice out loudly,' or related to Old Norse *skuta* 'a taunt.'"

Both potential connections trace back to the Proto-Indo-European root *\*skeud-*, which means "to shoot, chase, throw." The transitive sense—"utter in a loud and vehement voice"—developed by the late 14th century. The phrase "all over but (the) shouting," indicating a certain outcome, dates to 1834.
```


### [2026-09-06T20:39:28.300Z] TOOL RESULT

```
# سورنا - Etymology Analysis

Based on the Wiktionary content provided, I cannot find information addressing your specific questions about Persian etymology.

**What the page contains:**

The Pashto entry notes: "Compare Persian _سرنا_" but doesn't explain the underlying etymological structure.

The Persian section lists two etymologies but provides no breakdown of morphological components or historical linguistic origins. There is no mention of:
- Whether سورنا compounds سور (feast) + نای (reed pipe)
- Zurna or Turkish cognates
- Arabic linguistic connections

**What's missing:**

This Wiktionary entry lacks detailed etymological discussion for the Persian noun form. For comprehensive etymology information about potential compound origins or cross-linguistic relationships with zurna, you would need to consult more specialized linguistic resources or the fuller Persian Wikipedia article referenced in the entry.
```


## [2026-09-06T20:39:38.209Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/zurna",
 "prompt": "Turkish zurna — give etymology verbatim: Persian سورنای surnāy, from سور sūr 'feast' + نای nāy 'reed pipe'? dates and sources."
}
```


## [2026-09-06T20:39:39.042Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1%D9%86%D8%A7/",
 "prompt": "Give the فرهنگ معین (Mo'in) and دهخدا entries for سورنا verbatim, including any etymological note (سور + نای)."
}
```


### [2026-09-06T20:39:43.621Z] TOOL RESULT

```
I appreciate your question, but the webpage content provided doesn't contain the etymological information you're requesting about Turkish *zurna*.

The page shows only header navigation and footer elements from Nişanyan Sözlük (Nişanyan Dictionary), including copyright and policy links. The actual dictionary entry with etymology details isn't included in the content excerpt you've shared.

To find the etymology you're asking about—whether it traces to Persian سورنای (*surnāy*) from سور (*sūr*, 'feast') + نای (*nāy*, 'reed pipe')—you would need to access the full dictionary entry directly on the Nişanyan Sözlük website.
```


### [2026-09-06T20:39:48.608Z] TOOL RESULT

```
# Lexicographic Entries for سورنا

## Dehkhoda Dictionary Entry

The Dehkhoda entry describes سورنا as a compound word (اِ مرکب), with سورنای as the full form. It identifies the term as "a pipe played at weddings and celebrations," noting that سرنا is an abbreviated form, also called شهنا. The entry references Burhan and Anandraj as sources.

## Mo'in Dictionary Entry

The Mo'in entry simply cross-references: "= سرنا" — indicating it directs readers to the سرنا entry for the full definition.

## Etymological Note

Both classical sources suggest the structure **سور + نای**, where سور relates to celebration/festivity and نای denotes a pipe or wind instrument. This composition reflects the instrument's cultural role in joyous occasions.
```


## [2026-09-06T20:39:55.308Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\\|صفحه\" BQT_v2_pages.txt | head -5; echo \"---count---\"; grep -c \"\" BQT_v2_pages.txt; echo \"--- around 35657 ---\"; sed -n '35630,35670p' BQT_v2_pages.txt"
}
```


### [2026-09-06T20:39:55.385Z] TOOL RESULT

```
121:‫اول برهان (صفحهٌ صد و سی و حفت)‪ .‬هرگاه «چپار مقاله » مطلق ذ کر‬     ‫و عریی وو‬
301:                          ‫‪ -۳‬عدد اول نمرٌ جلد وعدد دوم نمرة صفحه است ‪.‬‬
650:   ‫‪۷0۵‬‬    ‫در صفحه‬          ‫هه‬
1225:                                                                                                    ‫یه از صفحهٌ ‪۵1۵‬‬
1746:   ‫قه در صفحهً ‪۵۷۵‬‬
---count---
41071
--- around 35657 ---
 ‫‪«.‬گیری » وآن چنان است که کشتی گیر بای‌خود‬

 ‫را بپای دبگری بندکند و اورا بینداژد و آنرا‬         ‫رخکه‬
                                                       ‫سوکلون آ‬
                                                              ‫وما‬
                                                                ‫سر نای ‪ = ۲‬ض‬
 ‫بعربی شغزییه خوالند ‪ -‬و بمعنی ربسمالی باشد‬       ‫‪ ۰‬بمعنی نای رومی است که سرنا‬        ‫بیاحطشید‬
                                                                                             ‫با‬
 ‫خاك پنهان‬      ‫ور‬
                 ‫زدی‬
                   ‫رکنن‬‫دفه‬
                         ‫که بکر آنرا حل‬                         ‫باشد ؛ و محذف الف هم‌آمده است‪.‬‬
 ‫سازند و سر دیگر را شخصی گرفته در کمین‬            ‫سر نج ‪ = ۴‬بکر اول و انی و سکون‬
 ‫بنشیند تا آدمی با جانوری که پای درآن میان‬         ‫ثالث و جيم » سنج را کوبند‪ .‬وآن دوپاره روی‬
     ‫نید آن شخص بوی خود کشد واورایگیرد‪.‬‬
                                                  ‫تنک‌باشد مانند طبق بکنیاره‌وبریشت آن قبه‌ای‬
  ‫‪.‬ر‬
   ‫سر و له = بفتح الث و بای ابجد س‬                ‫سازند و بتدی برآن‌تعبیه کنند و بردست گرفته‬
 ‫کرده وریش فيد پاسبانانرا گویند‪.‬چه لوبه بر‬        ‫زلند تا صدا در آید و بشتر بالقاره‬       ‫گیگ‬
                ‫وزن توبه بمءنی پاسبان است ‪. ۴‬‬      ‫و دهل وامثال آن‌لوازند ‪ -‬و قلمی وسرب‌سوخته‬
  ‫سر شوت ‪ -‬حک ازل وفضای‌ازل‌است‬                    ‫را کلبوزبند وآن‌رنگی است که نقاشان‌ومصوران‬
         ‫بعتی آلجه در روز ازل تفدیر شده باشد‪.‬‬     ‫بکار برند و آن درفایت حمرت میباشد چه باطن‬
 ‫بروزن‬                                            ‫سرب سرخ است و بجند آتشل حمرتآن ظاهر‬
           ‫لحث‬
             ‫وفت‬
               ‫ثلا‬
                 ‫سر نی ِ‪ -‬بضم او‬
 ‫پر می " مخفف سورنای‌است که نای‌رومی باشد‪.‬‬         ‫میشود ‪ .‬استنزال (‪ )۱‬اودررجمت بزیت وطرون‬
                                                                             ‫است ترد اهل عمل‪.‬‬
                    ‫ونای ترکی‌هم مگیویند ‪.‬‬
  ‫سر و = نم اول والی بکوشایوده‪,‬مطلق‬                ‫وکون‬
                                                      ‫ولی س‬
                                                          ‫اول ا‬           ‫=کر‬
                                                                            ‫سر ذل ب‬
 ‫شاخرا کوبند خواه شاخ کاو باشد وخواه شاخ‬          ‫جالد ر»بسمالی باشدکه طفلان در‬    ‫ود‬‫الثب‬
                                                                                        ‫ثا‬
 ‫کاومیش و شکاوخسفند و امثالآن ® ‪ -‬وبال‬            ‫ابام عیدها و جشنها از جابی آریزند د بر آن‬
 ‫شراب را (‪ )۲‬نکیوزنند ‪ -‬وبمعنی‌دروغ وبهتان‬        ‫ولزغرا نیز‬‫هروا آبند و رولد ‪ -‬و ج‬
                                                                                 ‫تشته د‬
‫همگفته‌اند‪٩‬‏ ‪ -‬و بفتح اولوسکون ثانی وواو نام‬      ‫گفته‌اند» و آن چیزی باشد سبز که در آبپای‬
 ‫‪ .‬و آن سه فم‬         ‫وف‬
```


## [2026-09-06T20:40:03.193Z] TOOL CALL #50: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1185 --image 2>&1 | tail -40"
}
```


### [2026-09-06T20:40:05.302Z] TOOL RESULT

```
no scan of BQT covers printed page 1185 (see 'scans' in refs_online.json)
```


## [2026-09-06T20:40:11.657Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"۱۱۸۵\\|١١٨٥\" BQT_v2_pages.txt | head; echo \"--- formfeeds ---\"; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read(); print('ff',d.count('\\f'))\"; echo \"--- search سور headword ---\"; grep -n \"سور ‪=\\|‫سور\\b\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T20:40:13.367Z] TOOL RESULT

```
--- formfeeds ---
ff 683
--- search سور headword ---
365:                                                               ‫سوراخ دار که برسر نون خیمه گذارید‪۰ ۳‬‬
8536: ‫در زدن است که کنابه از طلب فتح باب کردن‬                     ‫سورنجان‬    ‫۔ بر وزن ترتیب ‪۰‬‬           ‫جلی‪wo‬ت‬
10002:                                                                  ‫سوراخ هم هست؛ و بکسراول لیزدرست است" ؛‬
13113: ‫او نشف‬   ‫سوراخ‬   ‫بباز و کندنا بر در‬    ‫او را ‪E‬‏‬                                                ‫ات ات‬
16043: ‫دای‬                                                                                              ‫سور‬
23360:                               ‫ِ‬   ‫ىا توسند‬   ‫سورت‬
26907:               ‫رك ‪ :‬زارخورش ‪.‬‬           ‫‪۵۸‬‬             ‫رك‪ :‬زاح‪.‬‬      ‫‪-‬‬    ‫‪۲‬‬         ‫سور‪.‬‬       ‫رکه‪ :‬زاج »‬        ‫‪-‬‬   ‫‪1‬‬
27084: ‫سوراخها دارد و طباخان و حلوائیان بدان برج‬                        ‫زار دهشت ‪ ۴‬نم دالابجدوسکون‬
30491:‫و سکن ثالی‬                 ‫سور‬
35880:‫سوروبرا یزکوبند که شاخپای آن بهر طرف‬                    ‫بآرتش و مرداد براشجار وبافی سروشرابمحافظت‬
36451:                             ‫سوراخ میکند ‪.‬‬                            ‫‪۰‬‬   ‫رضم اول همآمده ات‬
36462: ‫سوراخ کرده راگوبند همچو مرواربد سفتهولمل‬       ‫بمیزد خصوص جانوران زهردار» وطبیخ آن‌موی‌را‬
36523:                     ‫چشم زخم در آتش ریزند ‪.‬‬                  ‫سوراخ باشد ‪ -‬وکنابه از فرمان‌بردار و قبول‬
37931:                                                                                               ‫سورن‬
39041:                                                                                   ‫سورهم آمده اس‬
39071: ‫سور بای‬                                                                                                              ‫ی ‪ ۱ ۸‬اس‬
39075:                                                                      ‫بروزن شور » بمعنی هنکامه‬                        ‫سور‬
39080:                                                                                      ‫سوری ‪ -‬و بزم ایامعید با‬
39104: ‫سور نای = یمنی‌تابی که درسوروجشن‬                                     ‫ویراند ‪ -‬و شراب سرخ‌رالیز‬
39124:  ‫سوری‌است»«معجم‬                 ‫وه‌وب‌بدان‬      ‫الورین‬    ‫سن‬     ‫اد ممر وف‬    ‫فد‬   ‫است‬   ‫محله‌ای‬   ‫سور‬   ‫‪9‬‬
```


## [2026-09-06T20:40:16.162Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39060,39135p' BQT_v2_pages.txt"
}
```


### [2026-09-06T20:40:16.244Z] TOOL RESULT

```
 ‫‪ = ۸‬سودابه (هم‪).‬‬      ‫‪ -‬تاجر (مفرد( صحیح است‬                                 ‫‪.‬‬    ‫‪۸۸‬‬       ‫التواریخ والصص ص‬

 ‫اول و فتح سوم ؛ از ‪ :‬سود ‪٣‬‏ مند ( یواد اصاف ) » پهلوی‬                            ‫تم‬
                                                                                   ‫‪ #‬سوده‌ند ‪-‬‬
 ‫او سودمند‬    ‫نافع ‪ « :‬ملك راسیحت‬          ‫آنکه با آنجه سود دهد »‬                  ‫‪۱‬‬       ‫« اق‬          ‫‪10‬‬
                                                        ‫آمد و از سرخون او بخاس‪۰‬ت «‪۰‬کلتان ‪۲6٩‬‏ ‪.‬‬
 ‫‪ #‬سودن ‪ -‬بضم اول دفتحسوم » نوی باستان ریشه‪( 2-2‬نیز کردن) > کردی ‪niûs‬‏‬
 ‫‪ - ‘Ye‬پیلوی ‪natûs‬‏ «تاوادیا ‪۵۹۱٩‬‏ وقس ‪ :‬سان‪.‬افان‬    ‫‪ ) sûn ۳‬ساییدن » ا‪‎‬‬

 ‫(سنگه چافوتیز کن) «حوبشمان ‪۲۰۷٩‬‏ ؛ سابیدن » لمس‪.‬مالیدن» کویدن » صلابه کردن‪-‬خرد‬
                                          ‫کردن » ری زکردن ‪ -‬سفتن » سوراخ کردن ‪.‬‬
 ‫سور بای‬                                                                                                              ‫ی ‪ ۱ ۸‬اس‬


 ‫مانده اطعمه‬            ‫همز ه هم درعر ی لیم خورده ورس‬                                        ‫‪= ۱‬‬
                                                                      ‫بروزن شور » بمعنی هنکامه‬                        ‫سور‬
                                           ‫را گوند ‪۰‬‬    ‫‪ 3‬آشربه‬       ‫و جشن وطوی و مهمالی ‪ -‬و عروسی ‪ -‬و ختنه‪:‬‬
 ‫بورا ‪ ۰‬نلم شهری‬                    ‫سو را = بورزن‬                    ‫رنگه‬       ‫نی‬
                                                                                 ‫عو‬‫م‪-‬‬
                                                                                    ‫بشد‬
                                                                                      ‫سوری ‪ -‬و بزم ایامعید با‬
                                           ‫ومد بنه‌اسءت ‪٩‬‏ ‪#.‬‬             ‫خاکستری بیاهی مابل‌هم هست و‪-‬اسب‌واسشس‬
                                                                      ‫انند سمند‬        ‫‌همخط‬
                                                                                           ‫یک‬‫هیند‬
                                                                                                ‫اکو‬
                                                                                                  ‫یرا‬‫سغی‬
                                                                                                       ‫ور الا‬‫خ‬
 ‫سودان ‪ ۲‬بر وزن توران» بممنی‬
‫سارو باشد » وآن پرنده‌ایست‪ .‬سیامرنگو قطهای‬                            ‫شده‌باشد ‪ ۴‬؛ و بعضی‬    ‫دشه‬  ‫ی دم‬
                                                                                                     ‫شل تا‬
                                                                                                         ‫کا ک‬
                                                                                                            ‫از‬
                               ‫صفند دارد وخوشآواز باشد‪*-‬‬              ‫اسب بآن رنه را خوب نمی‌دانندلهذا میگویند‬
                                                                      ‫ولام مرغی هم هست_‪-‬ورنگه‬                 ‫«مور ازګله دور“‬
 ‫کزف‬
   ‫»وعی ا‬
        ‫سو ‪3‬ج » بر وزن تورح ب‬                                         ‫سرخ رکافنتیهز‌الد چهگل سرخ راگل سوری‬
‫درجابیکه تردمك بدربا کوه‬                   ‫خرن باشد ‪ ۸‬وآن‬
                                                                      ‫و لاله را لالة سوریوشراب لعلی‌راشراب‌سوری ‪۴‬‬
 ‫وماشد نمك‌شور موه‬                  ‫وسنگه باشد بهم هرسف‬
                                                                           ‫‪۳‬‬                  ‫مبگوشد ‪ -‬ویعصی از افتان‬
             ‫يكن از نمك سفیدتر لوطیف‌تر است‪.‬‬                          ‫‪ -‬ودر‬         ‫‌است‬
                                                                                       ‫وام شبهوریدههم‬
                                                                                                    ‫مشهورند ‪ - ۴‬ن‬
 ‫سور نای = یمنی‌تابی که درسوروجشن‬                                     ‫ویراند ‪ -‬و شراب سرخ‌رالیز‬
                                                                                              ‫عربی دیوار قکلعه‬
                                                                       ‫عربان خمرالسوری خوانند ‪ - ۳‬وض‌اولوسکون‬

  ‫‪ ( 2۷۲10-‬صحگاهی » روزانه) » پهلوی ‪ ( ۲005‬چاشت صبح » طمام) »‬
                                                            ‫‪ - ۱‬اوستا ‪5‬‬
      ‫هوشمان ‪۳۵۷‬‬
               ‫‪ ۰‬جدن‌عروسی (‪9۱‬دق »‬                           ‫‪,‬فنی ]لا‪ِ 5‬‬
                                                                       ‫) عروسی» نامزدی) »ش‬                       ‫بلوچیع ‪5‬‬
      ‫‪۱۱‬‬
       ‫ص‬          ‫‪۵‬‬    ‫|مٿ ‪ ۶‬مصلهٌ بشوتن سال اول شماره‬              ‫در لهج زرنشتیان ابران « سور ‪٩‬‏ بمعنی عروسی‬
                         ‫‪۵۲۱.۰‬‬        ‫ص‪۲۱‬‬        ‫لوروزنامه تملیقات‬    ‫!‬    ‫سول (ه‪.‬م‪ ).‬ورك‬      ‫‪-‬‬    ‫‪۲‬‬             ‫‪.‬‬    ‫‪٩ ۱٩‬‬   ‫‪‎‬ج‬

 ‫(میآسوری) آمده‬                    ‫‪hdam i‬‬     ‫‪ - ۳‬در رسالة بهلوی«خرو قبادان وريدك وی“ ‪kîrusa‬‏‬

 ‫‪٩‬‏ تعبدر کرده ‪ :‬بثابر ین‬             ‫‪٩‬‏ تمالمی درغرر اخبار ملوك الفرس آرا «* سوری‬                 ‫«اونوالا ص‪ : ۷۲‬بد ‪۸۵‬‬

                                                              ‫موب به"سور؟ بمعنی‌سرخ لیت‪« :‬ازان پس شصت‬
 ‫ام فیله‌ی درافغانتان درائرةالممارف اسلام ‪ :‬اففاستان»‪.‬‬                          ‫‪- ۴‬‬         ‫«مجمل التواريخ والقصمص ‪۰۸۰‬‬

  ‫سوری‌است»«معجم‬                 ‫وه‌وب‌بدان‬      ‫الورین‬    ‫سن‬     ‫اد ممر وف‬    ‫فد‬   ‫است‬   ‫محله‌ای‬   ‫سور‬   ‫‪9‬‬


  ‫‪.‬موضعی‬          ‫«سوراء‬   ‫=‬   ‫‪۹‬‬            ‫|ست از تاحیت خزران« حدود ‪۰۱۱٩‬‏ ‪.‬‬               ‫البلدان ‪ » ۵۰۳‬ويز موضعی‬
 ‫ادسی‬       ‫‪...‬‬       ‫وباالف «قصوره‌هم روات شظه‬           ‫بغداد ات‬     ‫است‌و کونشد ود‬       ‫شداد‬     ‫است‪ .‬گوند در جاب‬

 ‫از سر زین بال ‪۰‬‬               ‫عراق‬   ‫در‬    ‫ات‬       ‫‪ 9‬سورا ‪ 0‬دوهی‬    ‫گو بد ‪ ۱‬مورضه‌ی است بجر بره“ «ممجم‌البادان»‬

 ‫وآن شهر سریانیان است وشراب را بدان نبت کنند ‪« ».‬ممجم‌البلدان» ‪ ۷ ۰‬چهانگیری در‬
 ‫ذ کر «سارنج» «سوران» را از لهج مردم آذربایجان بادکرده ‪۸ .‬‏ =‪( efflorescence‬فر)‬
 ‫سرلی (ہ‪.‬م‪ . ).‬قی ‪ :‬کرای ت‬                       ‫=‬     ‫‪۳‬ای‬
                                                         ‫رن‬‫سدا‬
```


## [2026-09-06T20:40:34.493Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN shout ===\"; grep -n \"shout\" KLN_1966.txt | head -10; echo \"=== SKT shout ===\"; grep -n -i \"^shout\\|SHOUT\" SKT.txt | head -10; echo \"=== AHD watkins keu/skeud ===\"; grep -n -i \"skeud\\|keud\\|kutsa\\|shout\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T20:40:34.571Z] TOOL RESULT

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b0v5m63g8.txt

Preview (first 2KB):
=== KLN shout ===
2460:amuna,  ‘he  was  faithful’,  d'mana,  ‘he  believed’, amtn,  ‘faithful’.  Cp.  ameen.  Cp.  also  mammon, amenable,  adj.,  answerable;  willing;  submissive. —  Formed  with  suff.  -able  fr.  F.  amener,  ‘to lead,  or  bring  up,  to’,  fr.  a,  ‘to’  (see  a),  and mener,  ‘to  lead’,  fr.  VL.  minare,  ‘to  drive  (ani¬ mals)  by  shouting’,  fr.  L.  minari,  ‘to  threaten’. The  orig.  meaning  of  L.  minari  has  survived  in Rum.  mana,  ‘to  threaten’.  See  menace  and  -able. Derivatives :  amenabil-ity,  n.,  amenable-ness,  n., amenabl-y,  adv.
3969:auk,  n.  —  Scand.  Cp.  ON.  dlka,  Dan.  alke, Swed.  alka,  which  prob.  derive  from  the  I.-E. imitative  base  *el-,  *ol-,  ‘to  shout,  cry’,  whence also  L.  olor  (for  *elor),  ‘swan’,  Mir.  ela,  ‘swan’, and  possibly  also  Gk.  eXe a,  ‘a  marsh  bird’, cXtopto?,  ‘a  water  bird’.  Cp.  Alca. auklet,  n.,  any  of  small  species  of  auks.  —  Form¬ ed  fr.  prec.  word  with  dimin.  suff.  -let. auksinas,  n.,  a  money  of  account  in  Lithuania.  — Lith.,  lit.  ‘gulden’,  fr.  auksas,  ‘gold’,  fr.  OLith. ausas,  of  s.m.,  which  is  rel.  to  OPruss.  ausis  and cogn.  with  L.  aurum,  of  s.m.;  see  aureate.  See Walde-Hofmann,  LEW.,  I,  p.86  s.v.  aurum. aula,  n.,  a  large  hall.  —  L.,  ‘the  front  court  of  a Grecian  house’,  fr.  Gk.  au Xr(,  ‘open  court, court, hall’,  fr.  I.-E.  base  *au -,  ‘to  rest’,  whence  also Arm.  ag-anim,  ‘I  pass  the  night’,  Gk.  Eauco  (for *i-af-iw),  ‘I  sleep',  and  prob.  the  second  element in  Gk.  eviauxop,  ‘year’.  Cp.  oriel, aulaco-,  before  a  vowel  aulac-,  combining  form meaning  ‘furrow’.  —  Gk.  aOXooco-,  auXax-, from  the  stem  of  aoXaE;  (gen.  auXaxoc),  ’fur¬ row’,  which  stands  for  *a-fXax-c  and  is  cogn.
4696:belch,  intr.  and  tr.  v.,  to  erect.  —  ME.  belchen, fr.  OE,  bealcian,  prob.  rel.  to  LG.  and  Du.  bal- ken,  ‘to  shout,  bellow’.
...
</persisted-output>
```


## [2026-09-06T20:40:36.793Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC keud ===\"; grep -n \"keud\\|kudazo\\|kutsa\" IEC.txt | head -20; echo \"=== IEC keu shine ===\"; grep -n \"śvas\\|svas 'tomorrow'\\|savahi\" IEC.txt | head -10; echo \"=== HUB 239/257 ===\"; grep -n \"nikuhtdan\\|nikuhidan\" HUB.txt | head"
}
```


### [2026-09-06T20:40:36.869Z] TOOL RESULT

```
=== IEC keud ===
7100:keudh- “hide; hiding, secret, mystery; mys- terious, obscure'. Cf. WP I, 369 & II, 550. (Variant: kudh-) Gk. keütho ‘hide’; keüthos, n. *hiding-place'; Br. küz, pl. küsiu, m. id.; (adj. "secret: küza, küzat, inf. ‘hide’; küzet, pp. & adj. ‘hidden’;
8265:küd- (küdaio, kudio) (1) “fling, cast, reject, scorn'. Variant: kuds- Gk. küdázo ‘scorn’; cf. kud-oimós (‘onset of battle’, lit. *dashtrack)); Lat. cüdo, Gre OC ‘forge, hammer’, unless derived from the cpd. forms of caudo; cf. LLat. cudis ‘anvil’; MHG hüzen (and hiuzen “raise a hue and cry); hutzen, intr. ‘swing, sway’; G hotzen rock: MHG hotzen (2) ‘rock’, tr; Sw. huta ut ‘snub’; OCS kydajo, -ati “throw? beside per- fective kynoti, inf. id.; OCz. kydati, kynúti, id.; R(po-)kidat ‘throw, reject; Latv. küdu, inf: kūdīt *egg on’. A variant of type *kuds- occurs in Skt. kutsámi, kutsayami, kutsyami “abuse”, isophonic with MHG hossen, tr. “stir, move, shake', and a variant of type *kudsK- in Ger. hutschen ‘rock; inch forward”; Eng. dial. to hutch “inch forward’
8456:kusdhos (kuzdh-) ‘hollow, niche, receptacle’. Cf. kust-, kudh-, keudh-. WP 550-1 Gk. küsthos ‘hollow; cunnus'; Go. huzd ‘hoard, treasure’; huzdjan, v. ‘amass’; MHG hort, (hordes gs); OE hord; ON hodd, f. as Go., beside MHG hürten, v. ‘hoard’. Extn. of type *kusdhero-, *kusdhro- in Skt. küharah, m. ‘hole, cave’; W cwthr ‘vulva, anus’
15597:skérios — skeud-
15612:skeud- ‘fling, (Variant:
15828:skoud-, see skeud- (skheud-) O-gde in ON skeyti, n. ‘shaft, arrow’; Li. skausmenys, pl. ‘meteorites’
15982:skud- (1) ‘tip, tail, end, rear’. (Var: skhud-). Cf. skeud- , Oss. kūdi, s. “back, rear, tail; kūda, adj. *dock- ed, tailless'; Arm. cf. xuzem, v. ‘search’; xujz, gs: xuzi, i-st. ‘search’; Gk. skuzáo, v. “follow, tail — of animals'; beside Hes. skudízo, v. ‘kick’; Ir. scud, scod, m. (2) ‘skirt — of robe"; EME scut, v. ‘shorten’; s. ‘short garment; tai; ON skutr, m. ‘stern of ship’; OE cf. scota, wm. *camp-follower'?
16104:sKeud- (form of skeud- and skheud-, q.v.) The initial appears in Skt. Códàmi, v. ‘spur on’; cf. Li. Sauju, šauti, v. 'shoot'; MIr. (ambig.) brot-scuad, s. ‘rub- bish?
=== IEC keu shine ===
=== HUB 239/257 ===
3593:Hierher nach Horn (KZ. 33, 434) np. nikuhtdan
```


## [2026-09-06T20:40:44.084Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD keu shine ==\"; grep -n -i \"keu-\\b\\|kewə\\|keuə\" AHD_watkins1985.txt | head -20; echo \"== AHD skeud ==\"; grep -n -iE \"^skeud|skeud-\" AHD_watkins1985.txt | head -10; echo \"== AHD shout entry ==\"; grep -n -i \"shout\\.\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T20:40:44.179Z] TOOL RESULT

```
== AHD keu shine ==
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1212:ACORN 6g- ACOUSTIC keu-1 ACQUAINT gnd- ACQUIESCE kWeje-2 ACQUIRE quaerere ACRE agro- ACRID ak- ACRIMONY ak- ACRO- ak- ACROBAT ak-, g¥a- ACROMEGALY meg- ACROMELIC mel-3 ACROMION ak-, omeso- ACROPOLIS pele-3 ACROSPIRE ak-, spel- ACROSTIC  steigh- ACT ag-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1350:CHIEF kaput CHIEFTAIN kaput CHILIAD gheslo- CHILL gel-3 CHILOPOD ghel-una CHIME! keu-2
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1403:cup keu-2
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1580:HEAD kaput HEAL kailo- HEALTH kailo- HEAP keu-2 HEAR keu-! HEARKEN keu-! HEART kerd-* HEARTH ker-4 HEAT kai- HEATH kaito- HEATHEN kaito- HEAVE kap-
1587:HEEL? kel-4 HEGEMONY sag- HEIFER per-3 HEIGHT keu-2 HEINOUS kad-
1608:HIEROPHANT bha-!, eis-1 HIGH keu-2
1618:HINGE konk- HINTERLAND ko-, lendh-2 HIP! keu-2
1625:HIVE keu-2
1645:HOP! keu-2
== AHD skeud ==
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
== AHD shout entry ==
477:gal-2, To call, shout. 1. Germanic expressive form *kall- in Old Norse kalla, to call: CALL. 2. Germanic *klat- in Old English *clatrian (> Middle English clateren), to clatter: CLATTER. 3. Expressive form *gall- in Latin gallus, cock (< “the calling bird”; but probably also associated with Gallus, Gallic, as if to mean “the bird of Gaul,” the cock being archaeologically attested as an important symbol in the iconography of Roman and pre-Roman Gaul): GALLINACEOUS, (GALLINULE). [Pok. 2. gal- 350.]
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
785:neu-'. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin niintius, “announc- ing,” hence a messenger, also a message, and ndéntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu: 767.] neu-2, To nod. 1. Latin *nuere, to nod (attested only in compounds), frequentative nutdre, to nod: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
```


## [2026-09-06T20:40:51.650Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"shout,  intr\\|shout,  n\\|shout,  v\\|shouten\" KLN_1966.txt KLN_1971.txt SKT.txt | head -10"
}
```


### [2026-09-06T20:40:51.717Z] TOOL RESULT

```
SKT.txt:17179:Shout.  (Unknown).  M.  E.  shouten ; Chaucer,  Troil.  ii.  614.  Etym.  unknown; cf.  Iccl.  jktita^  skii/i,  a  taunt
KLN_1971.txt:221008:shout, intr. and tr. v. — ME. shouten, of uncer- 
KLN_1966.txt:35048:Derivative:  shoulder,  tr.  and  intr.  v. shout,  intr.  and  tr.  v.  —  ME.  shouten,  of  uncer¬ tain  origin.  Cp.  ON.  skuta ,  ‘a  taunt’. Derivatives:  shout,  n.,  shout-er,  n.,  shout-ing,  n. shove,  tr.  and  intr.  v.  —  ME.  shouven,  shoven,  fr. OE.  sciifan,  sceofan,  rel.  to  ON.  skufa,  Dan., Norw.  skyve,  OFris.  skuva,  Du.  schuiven,  OHG. scioban,  MHG.,  G.  schieben,  ‘to  push,  thrust', Goth,  af-skiuban,  ‘to  put  away’,  fr.  I.-E.  base *sqeubh-,  'to  throw,  to  shove’,  whence  also Lith.  skiibti,  ‘to  make  haste’,  skubinti,  'to  has¬ ten’.  Cp.  scoff,  scoop,  scupper,  ‘cut  through  a ship’s  side’,  shovel.
```


## [2026-09-06T20:41:02.358Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN tadeln ==\"; grep -n \"tadeln\\|schmähen\\|schmahen\" HRN.txt | head -10; echo \"== MON سور ==\"; grep -n \"سور\" MON_part1.txt MON_part2.txt | head -5; echo \"== NYB sur ==\"; grep -n \"sūr \\[\\|sūr '\" NYB_vol2_glossary.txt | head -5; echo \"== NYB nikoh ==\"; grep -in \"nikōh\\|nikoh\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-06T20:41:02.447Z] TOOL RESULT

```
== HRN tadeln ==
3579:*schmähen , tadeln , verachten*, tiraskära- 'Schelten,
9068:schmähen'.
== MON سور ==
MON_part2.txt:163:غار: 27:[ع.] (.) سوراخی در کوه که مانند 
MON_part2.txt:366:غال: ا2,(.) سوراخی که جانوران صحرایی 
MON_part2.txt:498:غاو: «,(.) سوراخی که در زیرزمین یا 
MON_part2.txt:791:شیپوری و مخاط گونه را سوراخ کرده و 
MON_part2.txt:852:می‌شوند؛ غدد سور رنال. (گیا.) اعضای 
== NYB sur ==
== NYB nikoh ==
```


## [2026-09-06T20:41:06.095Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9050,9080p' HRN.txt; echo \"=== which page ===\"; python3 -c \"\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(d):\n    if 'schmähen' in p or 'schmahen' in p:\n        print(i, repr(p[:120]))\n\""
}
```


### [2026-09-06T20:41:07.874Z] TOOL RESULT

```
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
=== which page ===
106 "— 85 —\n379. teöerv Tasan'.\nmed. TBxaQoq, mrvonu; Tasan' (Athen. IX, p. 387 DE).\nLit. tetervas, tetervinas ^Birkhahn', ap"
255 "- 234 —\nnicht 'äumand. Gewöhnlich wird allerdings phlv. ö\nim Wortinnern nur durch den einfachen «<- Strich\nausgedrückt, "
```


## [2026-09-06T20:41:17.766Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for سور verbatim — the sense 'مهمانی/جشن' and any etymological label (پهلوی sūr). Also دهخدا if it gives an etymology."
}
```


## [2026-09-06T20:41:19.595Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewH-",
 "prompt": "Does this reconstruction page exist? Give the root, gloss, and descendants (Avestan, Sanskrit śvas, śoṇa-)."
}
```


### [2026-09-06T20:41:21.593Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:24.898Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for سور

**The festive sense:**
The dictionary defines it as "جِ سوره" and notes "[ په . ] (اِ. ) ۱ - جشن ، ضیافت . ۲ - عروسی" — indicating a Pahlavi origin marked with the label "[ په . ]"

**Dehkhoda's etymology:**
The Dehkhoda entry provides more detail: "اوستا «سوئیریا» ( صبحگاهی ، روزانه )، پهلوی «سور» ( چاشت صبح ، طعام )" — tracing the word back through Pahlavi *sūr* (morning meal/food) to Avestan *suirya*.

The entry also documents the word's evolution into meanings of "جشن. هنگامه. طوی. مهمانی. عروسی" (celebration, banquet, wedding) in Persian literary tradition.
```


## [2026-09-06T20:41:47.492Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT caune ==\"; grep -n \"caune\\|cauna\\|θauna\\|çauna\" KNT.txt TLM.txt 2>/dev/null | head -10; echo \"== BRT caune ==\"; grep -n \"caune\" BRT.txt | head -5; echo \"== POK sunica/kuna context ok ==\"; grep -n \"sunica\" POK_full.txt | head -3"
}
```


### [2026-09-06T20:41:47.562Z] TOOL RESULT

```
== KNT caune ==
== BRT caune ==
== POK sunica/kuna context ok ==
50964:(Sommerfelt BSL. 24, 219 ff.); russ. sunica, sunika, Serbo-Croatian sunica^ raspberry ';
```


## [2026-09-06T20:41:49.433Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B1\" \"https://www.etymonline.com/word/shout\" \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1/\" \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1%D9%86%D8%A7/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 264, roots Keu 4 / Keued: Persian sur 'feast', surna, English shout\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T20:41:54.672Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9b10eccade661f38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84ad9b90b321745d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de5422840649abd5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9c5fb6d81b847b5.txt
```


## [2026-09-06T20:42:03.784Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%DA%A9%D9%88%D9%87%DB%8C%D8%AF%D9%86/",
 "prompt": "Give the دهخدا and معین entries for نکوهیدن verbatim, including any etymological note (پهلوی nikōhīdan, Avestan, ni- prefix)."
}
```


### [2026-09-06T20:42:10.024Z] TOOL RESULT

```
# Entries for نکوهیدن

## Dehkhoda Entry
The dictionary defines the term as "سرزنش کردن" (to blame), "ملامت کردن" (to reproach), and "مذمت نمودن" (to censure). It includes numerous synonyms such as "عیب گفتن" (to find fault), "بدگوئی کردن" (to speak ill), and "تحقیر نمودن" (to disparage). The entry also provides classical Persian literary examples demonstrating usage.

## Moein Entry
The Moein dictionary presents a concise definition: "(نَ یا ن دَ) (مص م . ) سرزنش کردن ، ملامت کردن" — identifying the word as a verbal noun meaning "to blame" or "to reproach."

**Note:** The provided webpage contains no etymological information regarding Pahlavi, Avestan, or prefix origins for this term.
```


## [2026-09-06T20:42:30.359Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nikoh\\|nikōh\\|nkwhytn\\|nigōh\" CHEUNG.txt | head -10; echo \"-- kauH --\"; sed -n '22720,22740p' CHEUNG.txt"
}
```


### [2026-09-06T20:42:30.423Z] TOOL RESULT

```
-- kauH --
nyšq `w; Impf.: IND. 3sg. MSogd. nyšq w, 3р1. CSogd. nysSq’wnt, Pret.: tr. 25р. CSogd. nysSqwyd ry, 3sg. 
CSogd. nysqwyd'rt; Fut.: IND. 1sg. CSogd. nysq’wmq’, CSogd. nySqwmq’ 

*CHORESMIAN: k’w- ‘to scratch, rub’; m/kw- ‘to pluck’ || (+ *pari-) prk’w- ‘to curry’ 
|| m/sksy- (pass./intr.) ‘to be split, slit’ || (+ *fra-) m/skwnd- (tr.) ‘to earmark’. ç The 
Chor. forms were considered to have an unclear etymology, cf. Samadi, Le: 99, 
despite the apparently precise Pamir correspondences. In view of the meanings 
displayed by these forms, a connection with *skauH can hardly be doubted: *kauH 
would then be the s-less variant. The sibilant may have been re-interpreted as prefix 
*us- and removed accordingly ? || Chor. m/Skwnd- ‘to earmark’ has a peculiar, 
probably secondarily arisen, -d-, cf. Sh. sikund ("with secondary -nd", EVS: 73b). 
c» Samadi: 99, 105, 153, 192, 194 

*NEIR: Oss. I. sk’,ynyn/sk’,yd, D. (&)sk’unun/(z)sk’ud ‘to vomit; to tear up; to 
destroy’, (old pass.) I. sk’,yjyn/sk’.yd, D. (&)sk’ujun/(z)sk’ud ‘to vomit; to be torn 
up, to be transferred, in transition, wither away, disappear’, I. sk’awyn/sk’awd, D. 
(z)skawun/(z)sk’awd ‘to pluck; to comb’, I. sqawyn/sqawd, D. (&)sgawun/ 
(z)sgawd (old caus.) ‘to peck; to chip; to pull at; to wipe (eyes)’, Pash. sköy- ‘to 
scrape, scratch, rub; [lex.] to shear’, ? Pash. skastol/skal-, skustal/skul- ‘to shear, 
clip’, Sh. sikünd ‘pitch-fork’, || Yi. &ü-/£üvd-, M. jüv-/juvd, ўйу-/ўйуа- ‘to pick’, Sh. 
cäw-t, Rosh. céw-t, Bart. Cäw-t/Eüd, Sariq. čew-/čid ‘to comb, scratch’, Ishk. kow-
```


## [2026-09-06T20:42:33.450Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%86%DA%A9%D9%88%D9%87%DB%8C%D8%AF%D9%86/\" --note \"page 264, root Keued: Persian nekuhidan 'to blame' (Dehkhoda/Mo'in definitions)\" 2>&1 | tail -2; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg264hi.png data/verification/sources/refs/ocr/BOOK/264.png && ls -la data/verification/sources/refs/ocr/BOOK/"
}
```


### [2026-09-06T20:42:36.488Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e818898e79864454.txt
total 11344
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 16:42 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
-rw-rw-r--  1 sfmqrb sfmqrb  68501 Sep  5 13:28 108.png
-rw-rw-r--  1 sfmqrb sfmqrb  63543 Sep  5 13:35 109.png
-rw-rw-r--  1 sfmqrb sfmqrb  67502 Sep  5 13:39 110.png
-rw-rw-r--  1 sfmqrb sfmqrb  72718 Sep  5 13:38 111.png
-rw-rw-r--  1 sfmqrb sfmqrb  50381 Sep  5 13:39 112.png
-rw-rw-r--  1 sfmqrb sfmqrb  83933 Sep  5 13:54 114.png
-rw-rw-r--  1 sfmqrb sfmqrb  64811 Sep  5 14:02 117.png
-rw-rw-r--  1 sfmqrb sfmqrb  42354 Sep  5 14:08 118.png
-rw-rw-r--  1 sfmqrb sfmqrb  50224 Sep  5 14:12 120.png
-rw-rw-r--  1 sfmqrb sfmqrb  82335 Sep  5 14:19 121.png
-rw-rw-r--  1 sfmqrb sfmqrb  61026 Sep  5 14:26 123.png
-rw-rw-r--  1 sfmqrb sfmqrb  91077 Sep  5 14:38 124.png
-rw-rw-r--  1 sfmqrb sfmqrb  75202 Sep  5 14:31 125.png
-rw-rw-r--  1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r--  1 sfmqrb sfmqrb  83553 Sep  5 16:14 128.png
-rw-rw-r--  1 sfmqrb sfmqrb  74748 Sep  5 16:15 130.png
-rw-rw-r--  1 sfmqrb sfmqrb  87739 Sep  5 16:21 134.png
-rw-rw-r--  1 sfmqrb sfmqrb  68320 Sep  5 16:17 136.png
-rw-rw-r--  1 sfmqrb sfmqrb  70436 Sep  5 16:19 140.png
-rw-rw-r--  1 sfmqrb sfmqrb  53357 Sep  5 16:18 142.png
-rw-rw-r--  1 sfmqrb sfmqrb  63658 Sep  5 16:18 144.png
-rw-rw-r--  1 sfmqrb sfmqrb  89133 Sep  5 16:21 145.png
-rw-rw-r--  1 sfmqrb sfmqrb  60631 Sep  5 16:21 147.png
-rw-rw-r--  1 sfmqrb sfmqrb  81770 Sep  5 16:21 148.png
-rw-rw-r--  1 sfmqrb sfmqrb  72186 Sep  5 16:36 149.png
-rw-rw-r--  1 sfmqrb sfmqrb  31185 Sep  5 16:32 150.png
-rw-rw-r--  1 sfmqrb sfmqrb  96854 Sep  5 16:42 151.png
-rw-rw-r--  1 sfmqrb sfmqrb  61486 Sep  5 16:35 153.png
-rw-rw-r--  1 sfmqrb sfmqrb  63033 Sep  5 16:38 154.png
-rw-rw-r--  1 sfmqrb sfmqrb  77057 Sep  5 16:41 155.png
-rw-rw-r--  1 sfmqrb sfmqrb 101504 Sep  5 16:44 156.png
-rw-rw-r--  1 sfmqrb sfmqrb 169880 Sep  5 16:48 158.png
-rw-rw-r--  1 sfmqrb sfmqrb  27814 Sep  5 16:35 159.png
-rw-rw-r--  1 sfmqrb sfmqrb  14765 Sep  5 16:41 161_am_detail.png
-rw-rw-r--  1 sfmqrb sfmqrb  76745 Sep  5 16:41 161.png
-rw-rw-r--  1 sfmqrb sfmqrb  25911 Sep  5 16:36 163.png
-rw-rw-r--  1 sfmqrb sfmqrb  59398 Sep  5 16:41 164.png
-rw-rw-r--  1 sfmqrb sfmqrb  61265 Sep  5 16:41 165.png
-rw-rw-r--  1 sfmqrb sfmqrb  60832 Sep  5 16:44 166.png
-rw-rw-r--  1 sfmqrb sfmqrb 116877 Sep  5 16:48 167.png
-rw-rw-r--  1 sfmqrb sfmqrb  73551 Sep  5 16:52 171.png
-rw-rw-r--  1 sfmqrb sfmqrb  73400 Sep  5 17:08 172.png
-rw-rw-r--  1 sfmqrb sfmqrb  52970 Sep  5 16:59 173.png
-rw-rw-r--  1 sfmqrb sfmqrb  70664 Sep  5 17:04 174.png
-rw-rw-r--  1 sfmqrb sfmqrb  54907 Sep  5 17:04 175.png
-rw-rw-r--  1 sfmqrb sfmqrb  83583 Sep  5 17:07 176.png
-rw-rw-r--  1 sfmqrb sfmqrb  88207 Sep  5 17:04 177.png
-rw-rw-r--  1 sfmqrb sfmqrb  64024 Sep  5 17:04 178.png
-rw-rw-r--  1 sfmqrb sfmqrb  57139 Sep  5 17:01 179.png
-rw-rw-r--  1 sfmqrb sfmqrb  81598 Sep  5 17:04 180.png
-rw-rw-r--  1 sfmqrb sfmqrb  56794 Sep  5 17:03 181.png
-rw-rw-r--  1 sfmqrb sfmqrb  53414 Sep  5 17:04 183.png
-rw-rw-r--  1 sfmqrb sfmqrb  77310 Sep  5 17:09 184.png
-rw-rw-r--  1 sfmqrb sfmqrb  79537 Sep  5 17:11 185.png
-rw-rw-r--  1 sfmqrb sfmqrb  53749 Sep  5 17:08 187.png
-rw-rw-r--  1 sfmqrb sfmqrb  77516 Sep  5 17:11 189.png
-rw-rw-r--  1 sfmqrb sfmqrb  65970 Sep  5 22:26 190.png
-rw-rw-r--  1 sfmqrb sfmqrb  78016 Sep  5 22:23 191.png
-rw-rw-r--  1 sfmqrb sfmqrb  66901 Sep  5 22:31 193.jpg
-rw-rw-r--  1 sfmqrb sfmqrb  75938 Sep  5 22:38 195.png
-rw-rw-r--  1 sfmqrb sfmqrb  85794 Sep  5 22:32 198.png
-rw-rw-r--  1 sfmqrb sfmqrb  78587 Sep  5 22:28 199.png
-rw-rw-r--  1 sfmqrb sfmqrb  78934 Sep  5 22:26 200.png
-rw-rw-r--  1 sfmqrb sfmqrb  54688 Sep  6 11:00 201.png
-rw-rw-r--  1 sfmqrb sfmqrb  98287 Sep  5 22:35 202.png
-rw-rw-r--  1 sfmqrb sfmqrb  75609 Sep  5 22:29 203.png
-rw-rw-r--  1 sfmqrb sfmqrb  70083 Sep  6 10:53 204.png
-rw-rw-r--  1 sfmqrb sfmqrb  87032 Sep  5 22:33 205.png
-rw-rw-r--  1 sfmqrb sfmqrb  77858 Sep  6 11:03 206.png
-rw-rw-r--  1 sfmqrb sfmqrb  67371 Sep  6 11:02 207.png
-rw-rw-r--  1 sfmqrb sfmqrb  59146 Sep  6 10:59 208.png
-rw-rw-r--  1 sfmqrb sfmqrb  53054 Sep  6 11:00 209.png
-rw-rw-r--  1 sfmqrb sfmqrb  74515 Sep  6 11:06 211.png
-rw-rw-r--  1 sfmqrb sfmqrb  75961 Sep  6 11:07 212.png
-rw-rw-r--  1 sfmqrb sfmqrb  83761 Sep  6 11:07 213.png
-rw-rw-r--  1 sfmqrb sfmqrb  83752 Sep  6 11:05 214.png
-rw-rw-r--  1 sfmqrb sfmqrb 117034 Sep  6 11:09 215.png
-rw-rw-r--  1 sfmqrb sfmqrb  76564 Sep  6 11:19 216.png
-rw-rw-r--  1 sfmqrb sfmqrb  82798 Sep  6 11:18 217.png
-rw-rw-r--  1 sfmqrb sfmqrb  82099 Sep  6 11:23 218.png
-rw-rw-r--  1 sfmqrb sfmqrb  71937 Sep  6 11:26 219.png
-rw-rw-r--  1 sfmqrb sfmqrb  63280 Sep  6 11:19 220.png
-rw-rw-r--  1 sfmqrb sfmqrb  71497 Sep  6 11:20 221.png
-rw-rw-r--  1 sfmqrb sfmqrb  84108 Sep  6 11:17 222.png
-rw-rw-r--  1 sfmqrb sfmqrb  81537 Sep  6 11:23 223.png
-rw-rw-r--  1 sfmqrb sfmqrb  55412 Sep  6 11:26 224.png
-rw-rw-r--  1 sfmqrb sfmqrb  80963 Sep  6 11:35 225.png
-rw-rw-r--  1 sfmqrb sfmqrb  74322 Sep  6 11:34 226.png
-rw-rw-r--  1 sfmqrb sfmqrb  54381 Sep  6 11:33 227.png
-rw-rw-r--  1 sfmqrb sfmqrb  42112 Sep  6 11:32 229.png
-rw-rw-r--  1 sfmqrb sfmqrb  65310 Sep  6 11:37 230.png
-rw-rw-r--  1 sfmqrb sfmqrb  69894 Sep  6 11:38 231.png
-rw-rw-r--  1 sfmqrb sfmqrb  67111 Sep  6 11:43 233.png
-rw-rw-r--  1 sfmqrb sfmqrb  82071 Sep  6 11:46 234.png
-rw-rw-r--  1 sfmqrb sfmqrb  69091 Sep  6 11:48 235.jpg
-rw-rw-r--  1 sfmqrb sfmqrb  73781 Sep  6 11:48 235.png
-rw-rw-r--  1 sfmqrb sfmqrb  47149 Sep  6 11:47 236.png
-rw-rw-r--  1 sfmqrb sfmqrb  67972 Sep  6 11:53 237.png
-rw-rw-r--  1 sfmqrb sfmqrb  78380 Sep  6 11:52 239.png
-rw-rw-r--  1 sfmqrb sfmqrb  81131 Sep  6 11:54 240.png
-rw-rw-r--  1 sfmqrb sfmqrb  97613 Sep  6 11:57 242.png
-rw-rw-r--  1 sfmqrb sfmqrb  80632 Sep  6 12:02 245.png
-rw-rw-r--  1 sfmqrb sfmqrb  79253 Sep  6 12:05 246.png
-rw-rw-r--  1 sfmqrb sfmqrb  64208 Sep  6 12:06 247.png
-rw-rw-r--  1 sfmqrb sfmqrb  49887 Sep  6 12:08 248.png
-rw-rw-r--  1 sfmqrb sfmqrb  82530 Sep  6 12:11 249.png
-rw-rw-r--  1 sfmqrb sfmqrb  89076 Sep  6 12:13 250.png
-rw-rw-r--  1 sfmqrb sfmqrb  75263 Sep  6 12:12 251.png
-rw-rw-r--  1 sfmqrb sfmqrb  74772 Sep  6 12:17 252.png
-rw-rw-r--  1 sfmqrb sfmqrb  71025 Sep  6 12:18 254.png
-rw-rw-r--  1 sfmqrb sfmqrb  55906 Sep  6 12:13 255.png
-rw-rw-r--  1 sfmqrb sfmqrb  83469 Sep  6 12:24 256.png
-rw-rw-r--  1 sfmqrb sfmqrb  81240 Sep  6 12:25 258.png
-rw-rw-r--  1 sfmqrb sfmqrb  79514 Sep  6 12:30 260.png
-rw-rw-r--  1 sfmqrb sfmqrb  71156 Sep  6 12:36 263.png
-rw-rw-r--  1 sfmqrb sfmqrb  92930 Sep  6 16:42 264.png
-rw-rw-r--  1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r--  1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r--  1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r--  1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r--  1 sfmqrb sfmqrb  44812 Sep  5 16:36 532.png
-rw-rw-r--  1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
-rw-rw-r--  1 sfmqrb sfmqrb  57649 Sep  5 01:38 69.png
-rw-rw-r--  1 sfmqrb sfmqrb  75801 Sep  5 01:35 71.png
-rw-rw-r--  1 sfmqrb sfmqrb  49860 Sep  5 01:47 72.png
-rw-rw-r--  1 sfmqrb sfmqrb  81180 Sep  5 01:53 73.png
-rw-rw-r--  1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
-rw-rw-r--  1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r--  1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r--  1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
-rw-rw-r--  1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r--  1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
-rw-rw-r--  1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
-rw-rw-r--  1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r--  1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r--  1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r--  1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
-rw-rw-r--  1 sfmqrb sfmqrb  63329 Sep  5 02:31 85.png
-rw-rw-r--  1 sfmqrb sfmqrb  31530 Sep  5 02:38 86.png
-rw-rw-r--  1 sfmqrb sfmqrb  79874 Sep  5 09:55 87.png
-rw-rw-r--  1 sfmqrb sfmqrb  98452 Sep  5 09:55 88.png
-rw-rw-r--  1 sfmqrb sfmqrb  80984 Sep  5 09:56 89.png
-rw-rw-r--  1 sfmqrb sfmqrb  77182 Sep  5 09:55 90.png
-rw-rw-r--  1 sfmqrb sfmqrb  63799 Sep  5 09:56 91.png
-rw-rw-r--  1 sfmqrb sfmqrb   3476 Sep  5 10:16 92_pahlavi_box.png
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T20:42:40.026Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T20:42:40.077Z] TOOL RESULT

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


## [2026-09-06T20:42:42.402Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T20:42:42.443Z] TOOL RESULT

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


## [2026-09-06T20:42:52.058Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^36[5-9]\\b\\|368\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,20p'; echo \"=== search sumbhati/savahi ===\"; grep -n \"savahi\\|sumbhati\\|çvás\\|cvas \" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T20:42:52.118Z] TOOL RESULT

```
1407:1088,368.
4614:sekundar erhalten haben (so u. a. Hoops Waldb. 477 f., Meillet Msl. 368
4856:   Nach Zimmermann KZ. 44, 368 f., 47, 174 gehort auch lat. amornus
4920:367,     3
9757:  Froehde BB. 5, 27o“; 7, 325, Osthoff MU. 4, 368, Fick I 4 123, 542, III 4
12064:vog, Fick I 4 368), lat. unco, -are „vom Naturlaut des Biiren" iBzzbg. BB. 1,
15067:apoln. *lito; oder zu lit. lieti „gie8en“? s. Trautmann Apr, 368.  Nicht          —
16435:     S. FickI 4 16, 167, 368 f., Ill 4            16 (iiber lit. iimaras „Sturm, Ungestiim“ usw.
28946:KG. II 368.            — Nasaliert               as. ivlank ..iibermiitig,               kiihn",       ags. ivlanc, wlonc
29035:fangen, der freien Bewegung beraubt" (Bartholomae Airan. Wb. 1368; kann
30428: KG. II 368j.
31021: „Heide, unbebautes Feld, Trift, Einode, Wald '. Fick KZ. 21, 368 f., Wb. II 4 1
33301:„Verstand“ (Pedersen KZ. 39, 368, wo aueh nicht iiberzeugend arm. xorh-
34307:368                                                              keu-   — qeu-
43718:  Fick KZ. 21, 368, Curtius 5 152, Fiek I 4 389, II 4 95, III 4 74, Zupitza
49278:sei,   erwagt abweichend Brugmann II 2 2, 368 f.).
51792:Bsl. Wb. 368, Persson Beitr. 318 f., 835).
55547:     Yielleicht nach Yerf.         LEWb. 2 368 hier zu vereinigen lat. honos „Ehre,
59512:Halbdunkel“, Trautmann Bsl. Wb. 364, 368 (oder zu *gel- „hell, heiter,
59732:368, 372         und bes. Persson Beitr. 790ff., 876f.
=== search sumbhati/savahi ===
```


## [2026-09-06T20:42:55.321Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34290,34350p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T20:42:55.379Z] TOOL RESULT

```
                                                                                                      gr.   y.vxvov
x ov   aixvov usw.            s.   Yf. LEWb. 2 s. v.
  Auf eine Wzf. ku-el- bezieht Petersson LUA 1915, 7f., 1916, 40 arm.
setj „IIaufe, Menge" ( *kuel-dh-io oder -gh-(o -), ags. lucylco „Ivrampf-
ader", wozu lucelian      eitern"; gegen Zupitzas Gut. 57 Yerbindung
                                               ,


mit lett. kvclc „Entziindung einer Wunde", woriiber u. qcu- „anziinden,
verbrennen", wendet sich Petersson LUA 1916, 48 Anm. 1), aisl. hvCill
..rundlicher Iliigel"                (vgl.         auch nschw. mdartl. hvlilin ..Ileuhaufe", Zupitza
KZ. 37. 403, der in beideu nicht iiherzcugend ei:i g'td- nebcn gel- ,.heben-
                                         :                                                                                                ;




368                                                              keu-   — qeu-
sieht).           Unsicher         ist       Yerwandtschaft               Yon *kueg-
                                                                                2
                                                                                     „klaffen“,                   ebenso            von
*hu(ti)on-         „Hund“.              Im Yok. und im Guttural verschieden ist qaul-                                     ;)
                                                                                                                               hohl“.


2.  keu- „leuchten, hell '.                    -

                                                  4
   Av. savaM- „Name des im Osten gelegenen Erdteils" (eig. Nom. Du.
von *savah- „Morgen, Osten", Bartholomae Airan. Wb. 1562), mit sclnvundst.
Wzsilbe ai. gvah Adv. „cras" (s. Brugmann II 2, 179, 693, 746, Persson
Beitr. 745; nicht mit ursprgl. -ar und in formaler Beziehung zum flgdn.
nacb Bartholomae Wb. 1631); r-St. av. siirdin „friih morgens" (them. Acc.
eines kons. St. nach Bartholomae    7
                                                                      W
                                      b. aaO.), a-suiri „im Morgendunkel",
(suirya-),  Acc. suirim „Friihstiick“ (ibd. 221, 1586, fruhere Lit. bei Bar-
tholomae IA. 12, 26);
   wo-St. ai. qona- „rot, liochrot" (n fur n; Fick I 213, Persson Beitr. 745),
russ. sunica sunika skr. sunicci „Himbeere“ (Petersson PBrB. 40, 87; ganz
                       ,            ,


fragwtirdig ist Peterssons                              LUA 1916, 12 Anm. 1, Erwagung, daB dem russ.
kuna „Harder“ usw.                       —             s.   Berneker 644    —    ,
                                                                                     lit.    kiaune   ,
                                                                                                          lett. cauna ,    caiine,
apr. caune ds. ein entsprechendes Farbadj. von einer Wzf. mit Yelar zugrunde
liegen konne;                iiber      lit.       Sv'tnas „Blei“,        sowie iiber gr. xvavog „dunkelblaue
Substanz", die Persson Beitr. 745 zw. als kue no - anreiht,                                                s.   Boisacq        s.   v.)

     vielleicht arm. (s. Petersson                            LUA 1915, 3    f.;     1916, 47) sukh „Glanz, Pracht,
Rubin" (als *kud-qo-; davon skhel „ glanzvoll us\v.“), sol „Strahl, Lichtstrahl"
(als *kuo-lo-),             nsoyl „Licht,                    Glanz,     Gefunkel"           ( *ni-kuolio)       wahrscheinlich
sancl,       sant „Funke,               Blitz,              gliihendes Eisen"        (
                                                                                         kunti     allerdings mit kuen-
„feiern, heiligen"                 — selbst wenn dies aus keu- erweitert                                  ist   — wegen der
Bed. nicht in nahern Zshang zu bringen, sondern vrohl von einem Ptc.-St.
ku-ent-    ku-nt- ausgegangenl
              :
```


## [2026-09-06T20:48:47.707Z] TOOL CALL #70: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-264.json",
 "content": "{\n  \"pdf_page\": 264,\n  \"book_page\": 234,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Keu 4, Keu-bh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱewH- 'to shine, be bright' (Pokorny's k̑eu-2, k̑eu̯ə-, IEW 594-595; Walde-Pokorny I 368 '2. k̑eu- leuchten, hell'); root extension *ḱewbʰ- (Pokorny's k̑eu-bʰ-) in Skt. śumbhati 'shines', śubhra- 'beautiful, gleaming'\",\n      \"note\": \"Both the root name and the gloss are copied straight from Pokorny: IEW p. 594 heads the lemma 'k̑eu-2, k̑eu̯ə-' with the meaning 'to shine, bright', and lists 'k̑eu-bʰ-' among its Wurzelerweiterungen on the same page — so Nourai's double heading 'Keu 4, Keu-bh' and the redirect 'Keu-bh → Keu 4' on this page are exactly Pokorny's arrangement. The only silent modernisation needed is that the initial is a PALATAL *ḱ (Pokorny's k̑, satem s- in Indo-Iranian, hence Av. s-, Skt. ś-), which Nourai's plain Latin 'K' does not show, and that current reconstruction writes a final laryngeal, *ḱewH-. Watkins/AHD has no such root (it keeps only keu-1 'to see, observe'), so the appendix is silent rather than contradicting. Nourai's own numbering 'Keu 4' is his, not Pokorny's.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱewH- «درخشیدن، روشن بودن» است که پوکورنی (ص ۵۹۴–۵۹۵) آن را k̑eu-2 و گسترش آن را k̑eu-bʰ- می‌نامد و والده-پوکورنی (ج ۱ ص ۳۶۸) نیز همان را «leuchten, hell» می‌آورد؛ پس نام و معنای ریشه در نمودار نورایی دقیقاً برگرفته از پوکورنی است. تنها نکته آن است که همخوان آغازین کامی (palatal) است — یعنی *ḱ — و در زبان‌های هندوایرانی (گروه ساتِم) به s/ś بدل می‌شود؛ از این‌روست که صورت اوستایی با s و صورت سنسکریت با ś آغاز می‌گردد، حال آنکه نویسهٔ لاتینی «K» در کتاب این تمایز را نشان نمی‌دهد. ریشه‌شناسی امروزی صورت *ḱewH- را با حنجره‌ای پایانی بازسازی می‌کند. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B1\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:594\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 50942ff. (lemma printed with 'Page(s): 594-595'): 'Root / lemma: k̑eu-2 — Meaning: to shine, bright — Material: Avestan savahī- \\\"name of the continent situated in the east\\\" (actually Nom. Du. from *savah- \\\"morning, east\\\"), with zero grade root syllable Old Indic śvaḥ … Avestan sūrəm \\\"early in the morning\\\" …, a-suiri \\\"in the morning darkness\\\" (suirya-), Akk. sūirīm \\\"breakfast\\\" … Root extensions: k̑eu-bʰ-: Old Indic śumbhati \\\"shines\\\" …'. Nourai's root name, gloss and the Keu-bh extension all come from this page verbatim.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p. 368 (WLD_Bd1_pages.txt line 34307 '368  keu- — qeu-')\",\n          \"stance\": \"supports\",\n          \"note\": \"'2. k̑eu- \\\"leuchten, hell\\\". Av. savahī- \\\"Name des im Osten gelegenen Erdteils\\\" (eig. Nom. Du. von *savah- \\\"Morgen, Osten\\\", Bartholomae Airan. Wb. 1562), mit schwundst. Wzsilbe ai. śvaḥ Adv. \\\"cras\\\" …; r-St. av. sūrəm \\\"früh morgens\\\" …, a-suiri \\\"im Morgendunkel\\\", (suirya-), Acc. sūirīm \\\"Frühstück\\\" (ibd. 221, 1586)'. This is Pokorny's own source and it names exactly the Bartholomae columns Nourai cites.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, root list (AHD_watkins1985.txt)\",\n          \"stance\": \"silent\",\n          \"note\": \"No root *keu-/*ḱeu- 'to shine' in the appendix; the only keu- entries are keu-1 'to see, observe' (SHEEN, SHOW) and keu-2/keuə-2 'to bend'. Watkins simply does not carry Pokorny's k̑eu-2, so no support and no contradiction.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck p. 995, §14.44 MORNING (SYN.txt, awk record 1069/1070)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Av. sūr-, only in acc. sg. sūrəm as adv. : Skt. śvas \\\"tomorrow\\\", Av. savahī- \\\"the east\\\", with n-suffix Skt. śoṇa- \\\"red\\\", etc. Walde-P. 1.368. Barth. 1631.' Buck groups exactly the words Nourai puts under this root.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, Indo-European Comparative Dictionary (IEC.txt)\",\n          \"stance\": \"silent\",\n          \"note\": \"Grep for 'savahi', 'śvas', 'sumbhati' returns nothing; Mann has no lemma corresponding to Pokorny's k̑eu-2.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"sŭr, savah 2; sŭram; a-sŭr; sŭirya; savahî\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five items are genuine Avestan and all five stand under Pokorny's k̑eu-2 on p. 594. (a) sūr- n. 'morning, early morning' — Bartholomae AiW col. 1631 s.v. '(svar-) : sər- n. \\\"Morgen, Morgenfrühe\\\", nur AS. sūrəm als Adv. \\\"frühmorgens\\\"' (Yt. 10.14); Nourai's 'sŭram' is exactly that accusative-adverb, so 'sūr' and 'sūram' are one lexeme cited in two shapes, correctly glossed 'morning' / 'early morning'. (b) savah- n. 'morning; east' (Nourai's 'savah 2', his homonym-number), attested chiefly in the dual derivative savahī- 'the eastern continent (karšvar)', AiW col. 1562: 'j. savahī- (n.) Name des im Osten gelegenen Erdteils … Eig. ND. zu *savah- n. \\\"Morgen; Osten\\\"' — so 'savahî : the East' is right, with the caveat that savahī- is properly the name of the eastern karšvar of Zoroastrian cosmography rather than the common noun 'east'. The semantic bridge 'morning' > 'east' is the same as in Skt. pūrva- and Gk. anatolē: the quarter where the light comes up. (c) a-sūr(i) 'the dark before morning', AiW col. 221 s.v. 'a-svar- : ˚sər- n. \\\"Morgendunkel, -dämmerung\\\": ā˚sūiri (LS.) sūirīm išəmnō \\\"im Morgendunkel sich das Morgenmahl suchend\\\" Yt. 14.20. Eig. \\\"was bis zum Morgen hin reicht\\\"' — i.e. the ā- is the preposition 'up to, until' (not the privative ne-), so Nourai's gloss 'not (yet) morning, dawn' and his cross-reference to root Ne 1 read the a- as the negative prefix; Bartholomae explicitly prefers 'reaching up to morning', while Walde-Pokorny I 368 leaves both open. (d) sūirya- 'breakfast, morning meal', the derived adjective/neuter of sūr-, quoted in the same Yt. 14.20 passage as the acc. sūirīm 'Frühstück' (AiW 221, 1586). PIE *ḱewH- 'shine' > Proto-Iranian *sauH-/*sūr- with the regular satem outcome ḱ > s and the Iranian r-stem suffix; the same stem in the zero grade gives Skt. śvaḥ 'tomorrow'.\",\n          \"derivation_fa\": \"هر پنج صورت این جعبه اوستایی راستین‌اند و همگی در پوکورنی (ص ۵۹۴) زیر همین ریشه آمده‌اند. اوستایی sūr- «بامداد، سپیده‌دم» است که بارتولومه در ستون ۱۶۳۱ فرهنگ ایرانی باستان آن را «Morgen, Morgenfrühe» معنی کرده و تنها در حالت رایی sūrəm به‌گونهٔ قید «بامدادان» به‌کار رفته است؛ پس sŭr و sŭram یک واژه‌اند در دو صورت. savah- «بامداد؛ خاور» است و مشتق دوگانهٔ آن savahī- نام «کِشوَرِ خاوری» در جهان‌شناسی زردشتی است (بارتولومه ستون ۱۵۶۲)؛ تحول معنایی «بامداد ← خاور» همان است که در «پورو»ی سنسکریت نیز دیده می‌شود، چرا که روشنایی از خاور برمی‌دمد. دربارهٔ a-sūiri باید گفت بارتولومه (ستون ۲۲۱) آن را «تاریکیِ پیش از بامداد» می‌داند و پیشوند ā- را حرف اضافهٔ «تا، تا هنگامِ» می‌گیرد، نه پیشوند نفی؛ بنابراین ارجاع نورایی به ریشهٔ Ne 1 (نفی) با احتیاط پذیرفتنی است. sūirya- نیز «چاشتِ بامداد» است، از همان ستاک sūr-. از دید آوایی، *ḱ کامیِ هندواروپایی در شاخهٔ ساتِم به s بدل شده و ستاکِ r-دار ایرانی sūr- را پدید آورده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:594\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt (Page(s): 594-595): 'Avestan savahī- \\\"name of the continent situated in the east\\\" … Avestan sūrəm \\\"early in the morning\\\" …, a-suiri \\\"in the morning darkness\\\" (suirya-), Akk. sūirīm \\\"breakfast\\\"'. Every word of Nourai's node is in that sentence.\"\n            },\n            {\n              \"ref\": \"BRT:221\",\n              \"status\": \"supports\",\n              \"note\": \"BRT.txt line ~5926 (a- section, cols. 220-222): 'j. a-svar- : ˚sər- n. \\\"Morgendunkel, -dämmerung\\\": ā˚sūiri (LS.) sūirīm išəmnō … \\\"im Morgendunkel sich das Morgenmahl suchend\\\" Yt. 14.20. Eig. \\\"was bis zum Morgen hin reicht\\\"'. Confirms both a-sūiri and sūirīm 'breakfast'; but Bartholomae's own gloss makes ā- 'up to', not the negative.\"\n            },\n            {\n              \"ref\": \"BRT:1631\",\n              \"status\": \"supports\",\n              \"note\": \"BRT.txt line 27180 prints the column number 1631, and the lemma there is 'j. (svar-) : sūr- n. \\\"Morgen, Morgenfrühe\\\", nur AS. sūrəm als Adv. \\\"frühmorgens\\\" … Vgl. asuiri-. — ai. śvaḥ (LS. als) Adv. \\\"cras\\\"'. Exactly Nourai's sūr / sūram.\"\n            },\n            {\n              \"ref\": \"SYN:995\",\n              \"status\": \"supports\",\n              \"note\": \"Buck p. 995 §14.44 MORNING: 'Av. sūr-, only in acc. sg. sūrəm as adv. : Skt. śvas \\\"tomorrow\\\", Av. savahī- \\\"the east\\\", with n-suffix Skt. śoṇa- \\\"red\\\", etc. Walde-P. 1.368. Barth. 1631.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 221, 1562, 1631\",\n              \"stance\": \"partial\",\n              \"note\": \"Supports every form, but col. 221 glosses a-sūiri 'Morgendunkel' with ā- = 'until', and col. 1562 makes savahī- the name of the eastern karšvar rather than plain 'the East'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 368\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. savahī- … eig. Nom. Du. von *savah- \\\"Morgen, Osten\\\" … r-St. av. sūrəm \\\"früh morgens\\\" …, a-suiri \\\"im Morgendunkel\\\", (suirya-), Acc. sūirīm \\\"Frühstück\\\" (ibd. 221, 1586)'.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian lexicon (KNT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grep for sūr-/savah- returns nothing — as expected, these are Avestan and not attested in the Old Persian inscriptions.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"sŭr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian sūr [swl | Manichaean swr] 'meal, feast, banquet' (MacKenzie, CPD p. 79) continues an Old Iranian *sūrya-/*θūrya- 'of the morning, morning meal', the exact cognate of Av. sūirya- 'Frühstück'. Horn, Grundriss no. 753 (p. 166) states the chain in one line: 'sūr \\\"Fest, Gelage\\\". aw. sūirya- \\\"Morgenessen\\\" (Darmesteter, Ét. ir. II 161; Geldner KZ 25.531 n.228); phlv. sūr \\\"Morgenmahl, Mahl\\\"'. Semantically the word travels 'morning meal' > 'meal' > 'banquet, feast', the same shift as in NE breakfast > feast in some dialects, and in Bal. sīr 'wedding, betrothal' (a Persian loan, Horn ibid.). Phonetically Old Iranian intervocalic/postvocalic material is lost and the long ū of the root syllable is kept unchanged into MP; in Book Pahlavi the word is written <swl> because l regularly renders /r/ in Pahlavi orthography.\",\n          \"derivation_fa\": \"فارسی میانه (پهلوی) sūr به‌نویسهٔ <swl> «خوراک، سور، مهمانی» است؛ مکنزی در فرهنگ کوچک پهلوی (ص ۷۹) آن را «meal, feast, banquet» معنی کرده است. این واژه دنبالهٔ صورت ایرانی باستان *sūrya- «بامدادی، چاشتِ بامداد» است، یعنی همان که در اوستایی sūirya- شده. هرن در بند ۷۵۳ (ص ۱۶۶) همین زنجیره را می‌آورد: «sūr «جشن، بزم». اوستایی sūirya- «چاشت بامداد»؛ پهلوی sūr «چاشت بامداد، خوراک»». تحول معنایی روشن است: «خوراکِ بامداد ← خوراک ← بزم و مهمانی». در املای پهلوی حرف l به‌جای /r/ نوشته می‌شود، از این‌رو صورت نوشتاری <swl> است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:166\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt, awk record 188 (printed '- 166 -'), no. 753: 'sūr \\\"Fest, Gelage\\\". aw. sūirya- \\\"Morgenessen\\\" …; phlv. sūr \\\"Morgenmahl, Mahl\\\". bel. LW. sīr \\\"Hochzeit, Verlobung\\\" (241); šiγn. sur \\\"Gelage, Hochzeitsfest\\\"'. Precisely Nourai's Avestan → Pahlavi → Persian arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 79 s.v. sūr (PHD.txt line 572)\",\n              \"stance\": \"supports\",\n              \"note\": \"'sūr [swl | M swr, N ~] meal, feast, banquet.' Listed separately from '*sūr [swl] strong' and 'sūrāg/sūrāx hole'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"The glossary has sūlāk/sūrāx 'hole' (line 3562) but no entry for sūr 'meal, feast' — the word does not occur in Nyberg's selection of texts.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 753, p. 166\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; Horn is the standard authority for this chain and is quoted by Mo'in's footnote in Borhān-e Qāṭeʿ.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sŭr «سور»; sŭrnâ «سورنا، سورنای»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"(a) NP سور sūr 'feast, banquet, wedding party' is the direct continuation of MP sūr 'meal, feast' with no phonetic change at all (MP ū > NP ū). Moʿin's Farhang-e Fārsi marks it '[په.] (اِ.) ۱- جشن، ضیافت ۲- عروسی', i.e. explicitly a Pahlavi inheritance, and Dehkhodā gives the full chain 'اوستا «سوئیریا» (صبحگاهی، روزانه)، پهلوی «سور» (چاشت صبح، طعام)' — the very chain Nourai draws. Mo'in's own etymological footnote to Borhān-e Qāṭeʿ s.v. سور repeats it (Avestan sūirya- 'of the morning, daily', Pahlavi sūr 'morning meal, food', citing Hübschmann) and adds Baluchi sūr 'wedding, betrothal' and Zoroastrian-Dari sūr 'wedding'. Wiktionary reconstructs the same word through the Old Persian rather than the Avestan dialect: OP *θūryas < PIr. *cuHryás < PIE *ḱewH- — a real refinement, since New Persian descends from Old Persian and Avestan sūirya- is a sister form, not the ancestor; Nourai's arrow Avestan → Pahlavi should be read as 'Old Iranian (as attested in Avestan)'. (b) سورنا/سورنای sūrnā(y) is a transparent Persian compound سور 'feast' + نای nāy 'reed pipe' = 'the pipe played at feasts'; Borhān-e Qāṭeʿ, on the same page as سور, defines 'سور نای = یعنی نایی که در سور و جشن ...' and Dehkhodā 'نایی که در عروسی و جشن نوازند', with the shortened form سرنا. Horn no. 1060 (p. 237) lists it under nai/nāy: 'nei \\\"Schilf\\\", nāi \\\"Flöte\\\", nāl; vergl. karre-nāi, sūrnāi \\\"Festflöte\\\", seh-nāi', with the footnote 'Kauk.-bergjüd. sūrnai \\\"Schalmei\\\", russ. LW. zurna' — which is why Nourai cross-refers to his root Nedo (the reed word). The instrument name travelled onward into Ottoman Turkish and the Balkans as zurna and into Arabic as زرنا.\",\n          \"derivation_fa\": \"«سور» در فارسی نو دنبالهٔ بی‌واسطهٔ sūr فارسی میانه است و هیچ دگرگونی آوایی رخ نداده (ū پهلوی همان ū مانده است). فرهنگ معین آن را با نشانِ «[په.]» یعنی پهلوی می‌آورد: «۱- جشن، ضیافت ۲- عروسی»، و لغت‌نامهٔ دهخدا زنجیرهٔ کامل را می‌دهد: «اوستا سوئیریا (صبحگاهی، روزانه)، پهلوی سور (چاشت صبح، طعام)» — همان که در نمودار نورایی آمده است. حاشیهٔ ریشه‌شناختی معین بر برهان قاطع (ذیل «سور») نیز همین را با استناد به هوبشمان تکرار می‌کند و بلوچی sūr «عروسی، نامزدی» و «سور» گویش زردشتیان ایران به معنی عروسی را می‌افزاید. تنها نکتهٔ فنی آنکه فارسی نو دنبالهٔ فارسی باستان است نه اوستایی؛ ویکی‌واژه صورت فارسی باستان *θūryas را بازسازی می‌کند و اوستایی sūirya- را هم‌ریشه (نه نیا) می‌شمارد. «سورنا/سورنای» نیز ترکیبی روشن است: «سور» + «نای»، یعنی نایی که در سور و جشن می‌نوازند (برهان قاطع و دهخدا)؛ صورت کوتاه‌شدهٔ آن «سرنا» است و همین واژه به ترکی عثمانی و بالکان به‌صورت zurna راه یافته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B1\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1/\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B1%D9%86%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1185\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ vol. 2 (BQT_v2_pages.txt lines 39071-39110, the leaf whose running head reads ۱۱۸۵): headword 'سور — بروزن شور، بمعنی هنگامه و جشن و طوی و مهمانی ـ و عروسی ـ و ختنه سوری …' and, in the same column, 'سور نای = یعنی نایی که در سور و جشن …'. Mo'in's footnote 1 on that page: 'اوستا s[ūirya] (صبحگاهی، روزانه)، پهلوی sūr (چاشت صبح، طعام)، هوبشمان …؛ بلوچی sūr (عروسی، نامزدی)؛ در لهجهٔ زرتشتیان ایران «سور» بمعنی عروسی'. Both of Nourai's Persian words are on this one page, with his exact etymology in the footnote.\"\n            },\n            {\n              \"ref\": \"HRN:237\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt, awk record 259 (printed '— 237 —'), no. 1060: 'nei \\\"Schilf\\\", nāi \\\"Flöte\\\", nāl; vergl. karre-nāi, sūrnāi \\\"Festflöte\\\", seh-nāi; nāize.' Footnote: 'Kauk.-bergjüd. sūrnai \\\"Schalmei\\\", russ. LW. zurna.' Supports sūrnā as sūr + nāy and Nourai's cross-reference to root Nedo.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Moʿin s.v. سور (via abadis.ir)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[په.] (اِ.) ۱- جشن، ضیافت. ۲- عروسی' — Mo'in labels the word a Pahlavi inheritance, exactly Nourai's Pahlavi → Persian arrow. For سورنا Mo'in only cross-refers '= سرنا'.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2 p. 1185 s.v. سور and سورنای\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check. Dehkhodā (same portal) adds for سورنا: 'نایی که در عروسی و جشن نوازند … سرنا مخفف آن است' citing Borhān and Ānandrāj.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-hā, p. 363 s.v. سور\",\n              \"stance\": \"supports\",\n              \"note\": \"'سور (به چم «جشن و مهمانی»، «خوراک»)' with Avestan and Pahlavi cognates and the notes 'چم این واژه در زبان اوستایی: سحر' (Avestan sense: dawn), 'چم این واژه در زبان بلوچی: جشن عروسی', 'چم این واژه در زبان ارمنی: درخشش' (Armenian sense: radiance) — an independent modern Persian source giving the same 'shine → dawn → morning meal → feast' path; it cites برهان قاطع ۱۱۸۵ and فرهنگ معین.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"nos. 753 (p. 166) and 1060 (p. 237)\",\n              \"stance\": \"supports\",\n              \"note\": \"Both Persian words covered; see ref_check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"caune\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no Old Persian word 'caune', and 'bright red / a plant with bright-coloured fruits' is not one word's meaning. The form and the gloss both come from Pokorny p. 594, but from three different items in the no-stem paragraph, which Nourai has run together and then labelled 'Old Persian'. Pokorny (IEW 594, = Walde-Pokorny I 368) writes: 'no-stem: Old Indic śoṇa- \\\"red, bright red\\\" (ṇ for n), Gaul. Counos, Old Irish *cuan-dae … ; russ. sunica, sunika, Serbo-Croatian sunica \\\"raspberry\\\"; russ. kuna \\\"marten\\\", Lith. kiaunė, Latvian cauna, caune, Old Prussian caune ds.' — so (i) 'bright red' is Skt. śoṇa-, (ii) 'a plant with bright coloured fruits' is Russ. sunica / SCr. sunica 'raspberry', and (iii) caune is OLD PRUSSIAN (with Latv. cauna, Lith. kiaunė, Russ. kuna) meaning 'marten'; Walde-Pokorny explicitly abbreviates it 'apr. caune ds.' and Pokorny himself calls the marten group only a possible colour-derivative 'from a root form with velar', i.e. NOT from the palatal *ḱeu- at all. Neither Kent's Old Persian lexicon nor Bartholomae's Altiranisches Wörterbuch knows any Iranian *cauna-. The page image (site/pages/264.jpg, copy at data/verification/sources/refs/ocr/BOOK/264.png) shows the box printed exactly as extracted — 'Old Persian … caune : bright red, a plant with bright colored fruits' — so the extraction is faithful and the conflation is Nourai's own. The Iranian member of this no-stem group that Nourai could have cited is rather Av. suxra- / NP سرخ surx 'red', which Pokorny puts under the neighbouring root k̑euk- 'to shine'.\",\n          \"derivation_fa\": \"در فارسی باستان واژه‌ای به‌صورت caune وجود ندارد و معنای «سرخِ روشن، گیاهی با میوهٔ رنگین» نیز معنای یک واژه نیست. نورایی سه چیزِ جدا را از یک بندِ پوکورنی (ص ۵۹۴، برابرِ والده-پوکورنی ج ۱ ص ۳۶۸) در هم آمیخته و برچسبِ «فارسی باستان» بر آن نهاده است: نخست، «سرخِ روشن» معنای śoṇa- سنسکریت است؛ دوم، «گیاهی با میوهٔ رنگین» ترجمهٔ sunica روسی و صربی به معنی «تمشک» است؛ و سوم، خودِ صورت caune پروسیِ باستان (هم‌ردیفِ cauna لتونیایی، kiaunė لیتوانیایی و kuna روسی) به معنی «سمور» است — والده-پوکورنی صریحاً می‌نویسد «apr. caune ds.» و خودِ پوکورنی این گروهِ سمور را تنها «شایدْ» صفتِ رنگی از ریشه‌ای با همخوانِ ملازی (velar) می‌داند، یعنی نه از این ریشهٔ کامی. نه در فرهنگِ فارسی باستانِ کِنت و نه در فرهنگِ ایرانی باستانِ بارتولومه چنین واژه‌ای نیست. تصویر صفحهٔ چاپی نشان می‌دهد که متن کتاب دقیقاً همین است، پس خطای خوانشِ اسکن نیست؛ خطا از خودِ نورایی است. پژوهش امروزی این گِرِه را رد می‌کند. (نمایندهٔ ایرانیِ همین گروهِ رنگی در حقیقت suxra- اوستایی و «سرخ» فارسی است که پوکورنی زیر ریشهٔ همسایهٔ k̑euk- آورده است.)\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:594\",\n              \"status\": \"contradicts\",\n              \"note\": \"POK_full.txt (Page(s): 594-595): 'no-stem: Old Indic śoṇa- \\\"red, bright red\\\" (ṇ for n), gall. Counos (coin), Old Irish *cuan-dae … russ. sunica, sunika, Serbo-Croatian sunica \\\"raspberry\\\"; russ. kuna \\\"marten\\\" etc., Lithuanian kiaunė, Latvian cauna, caune, Old Prussian caune ds. could lie a corresponding color adj. from a root form with velar of the basic'. Pokorny's caune is Old Prussian 'marten', not Old Persian, and he doubts it belongs here at all.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 368\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'wo-St. ai. śoṇa- \\\"rot, hochrot\\\" …, russ. sunica sunika skr. sunica \\\"Himbeere\\\" …; ganz fragwürdig ist Peterssons … Erwägung, daß dem russ. kuna \\\"Marder\\\" usw. …, lit. kiaunė, lett. cauna, caune, apr. caune ds. ein entsprechendes Farbadj. von einer Wzf. mit Velar zugrunde liegen könne'. Explicitly Old Prussian ('apr.') and explicitly doubted.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon (KNT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grep for 'caune', 'cauna', 'çauna', 'θauna' in the Old Persian lexicon returns nothing — no such word is attested in the Achaemenid inscriptions.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grep for 'caune' returns nothing; Bartholomae records no Old Iranian *cauna-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Empty pass-through box: on the printed page (site/pages/264.jpg) an arrow runs from the 'Old Persian caune' box to a blank framed box at the right margin with no language label, no reference and no word in it. It is a layout stub — the slot where a descendant (presumably a European reflex of the 'marten'/'raspberry' group) would have gone — and carries no claim that could be verified. The extraction is faithful to the page.\",\n          \"derivation_fa\": \"این جعبه در خودِ کتاب تهی است: در صفحهٔ چاپی پیکانی از جعبهٔ «فارسی باستان caune» به یک قاب خالی در کنارهٔ راست می‌رود که نه نام زبان دارد، نه مأخذ و نه واژه. بنابراین ادعایی در آن نیست که بتوان سنجید؛ ظاهراً جای خالیِ یک بازماندهٔ اروپایی بوده که نویسنده آن را پر نکرده است. خوانشِ اسکن با صفحهٔ چاپی مطابق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book (refs=None) and no word, so there is nothing to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 594-595\",\n              \"stance\": \"silent\",\n              \"note\": \"Nothing in Pokorny's k̑eu-2 article corresponds to an unlabelled box after the no-stem paragraph; the descendants there (Gaul. Counos, OIr. cuanda, Russ. sunica, Baltic caune) are all listed inside the paragraph itself.\"\n            },\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page 234 = pdf 264 (data/verification/sources/refs/ocr/BOOK/264.png)\",\n              \"stance\": \"silent\",\n              \"note\": \"The box is drawn empty on the page; there is no lost text for the extractor to have missed.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Keued, Keud, Qeud, Skeud 2\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Pokorny's keuəd-, kūd- 'to cry' (IEW 595-596) = Walde-Pokorny's qeud- 'schreien; anschreien, schelten, höhnen, spotten' (WP I 378); the s-mobile variant *(s)keud- is invoked for ME shouten\",\n      \"note\": \"Nourai's four-name heading reproduces the two standard reference works exactly: Pokorny p. 595-596 heads the lemma 'keuəd- kūd-' (whence 'Keued, Keud') and Walde-Pokorny I 378 heads the same article 'qeud-' (whence 'Qeud'), while Buck p. 1251 writes the s-form '*skeud- beside *keud-' (whence 'Skeud 2'). The gloss 'to yell' is a fair rendering of Pokorny's 'to cry' / WP's 'schreien, schelten'. Verdict is plausible rather than confirmed because this root is a 1927/1959 reconstruction that current handbooks no longer carry: Watkins/AHD has no keud- 'to cry' (its skeud- is 'to shoot, chase, throw', Pok. 956, a different root), LIV has no such verbal root, and Mann (IEC) reshapes it as kūd- 'fling, cast, reject, scorn' rather than 'yell'. The Indo-Iranian-plus-Greek core (Skt. kutsayati, NP nikūhīdan, Gk. kudázō) is solid; the Germanic and Middle English members are the disputed part.\",\n      \"note_fa\": \"چهار نامی که نورایی برای این ریشه آورده، دقیقاً از دو مرجع کلاسیک گرفته شده است: پوکورنی (ص ۵۹۵–۵۹۶) مدخل را «keuəd-، kūd-» می‌نامد و والده-پوکورنی (ج ۱ ص ۳۷۸) همان مقاله را «qeud- «فریاد زدن؛ بر کسی بانگ زدن، سرزنش کردن، ریشخند کردن»» عنوان می‌دهد، و باک (ص ۱۲۵۱) صورتِ با s- را چنین می‌نویسد: «*skeud- در کنار *keud-». معنای «فریاد زدن» نیز برگردانِ درستِ «schreien/schelten» است. با این همه، حکم را «با احتیاط پذیرفتنی» گذاشتم، زیرا این ریشه در ریشه‌شناسی امروزی جایگاه استواری ندارد: واتکینز در پیوستِ AHD چنین ریشه‌ای ندارد (skeud- او به معنی «تیر انداختن، پرتاب کردن» و ریشه‌ای دیگر است)، LIV نیز آن را نمی‌آورد، و مان (فرهنگ تطبیقی هندواروپایی) آن را kūd- «افکندن، خوار شمردن» بازسازی می‌کند نه «فریاد زدن». هستهٔ هندوایرانی و یونانیِ ریشه (kutsayati سنسکریت، «نکوهیدن» فارسی، kudázō یونانی) استوار است؛ اندام‌های ژرمنی و انگلیسی میانه‌اند که مورد اختلاف‌اند.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/shout\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:595\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 46626ff. (printed 'Page(s): 595-596'): 'Root / lemma: keuəd- kud- — Meaning: to cry — Material: Old Indic kutsayati \\\"blasphemes, reproves\\\", kutsa \\\"abuse, reprimand\\\", npers. nikūhīdan \\\"rebuke, vilify, scold\\\"; gr. kudázō … agutn. huta … with anlaut. s- (previously after schallen, schreien!) perhaps Middle English schuten \\\"cry out, shout, bawl\\\", engl. to shout \\\"cry loudly\\\", Old Icelandic skūta, skūtī \\\"derision, gibe\\\" … References: WP. I 378 f.' Every node of Nourai's entry is in this one article.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p. 378 (WLD_Bd1_pages.txt line 35314 '378  keuq- qeud-', article at line 35377)\",\n          \"stance\": \"supports\",\n          \"note\": \"'qeud- \\\"schreien; anschreien, schelten, höhnen, spotten\\\". Ai. kutsáyati \\\"schmäht, tadelt\\\", kutsa \\\"Schmähung, Tadel\\\" …, npers. nikūhīdan \\\"tadeln, schmähen\\\" Horn KZ. 33, 434, 443, Hübschmann Pers. St. 102, 239. Gr. κυδάζω … Mit anl. s- (erst nach schallen, schreien u. dgl.?) vielleicht mengl. schuten \\\"vociferari\\\", engl. to shout, aisl. skúta, skúti \\\"Spott, Stichelei\\\"'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 root list and English index\",\n          \"stance\": \"contradicts\",\n          \"note\": \"No root *keud-/*keuəd- 'to cry' exists in the appendix; SHOUT does not appear in the English word index at all, while SHOOT/SHOT/SHUT/SHEET are put under 'skeud-. To shoot, chase, throw. [Pok. 2. (s)keud- 956.]' — a different Pokorny lemma from the one Nourai uses.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IEC s.v. kūd- (IEC.txt line 8265)\",\n          \"stance\": \"partial\",\n          \"note\": \"'kūd- (kūdaiō, kudiō) \\\"fling, cast, reject, scorn\\\". Variant: kuds- Gk. kūdázō \\\"scorn\\\" … A variant of type *kuds- occurs in Skt. kutsāmi, kutsayāmi, kutsyāmi \\\"abuse\\\"'. Mann keeps the Greek–Sanskrit equation but reconstructs the meaning as 'fling, reject, scorn', not 'yell', and does not include the Persian or English words.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck p. 1251, §18.13 SHOUT, CRY OUT\",\n          \"stance\": \"supports\",\n          \"note\": \"'ME shoute, NE shout : ON skūta, skūti \\\"taunt, jibe\\\", prob. fr. *skeud- beside *keud- in Grk. κυδάζω, Skt. kuts- \\\"revile, abuse\\\". Walde-P. 1.378.' This is the source of Nourai's 'Skeud 2' alongside 'Keud'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"nekŭkîdan «نکوهیدن»\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The etymology is sound but the printed Latin transliteration is wrong. The book prints 'nekŭkîdan' with a k where an h belongs; the Persian script in the same box, نکوهیدن (نکوهش), is correct, and every source spells the word nikūhīdan / nekūhīdan 'to blame, revile'. The word is a prefixed verb: preverb نـ ni- 'down' + a stem *kauH-/kūh- 'to revile', continuing MP nikōhīdan (MacKenzie, CPD: 'blame (n.) āwēnišn, ērang(īh), nikōh-; blame (v.) nikōhīdan', with nikōhišn 'blame', nikōhišnīg 'blameworthy'); MP ō regularly raises to NP ū before h, and the MP infinitive in -īdan is carried over unchanged, giving نکوهیدن with the verbal noun نکوهش nikūhiš. The Indo-European connection is Hübschmann's, on the very page Nourai cites: Pers. St. p. 102 'Hierher nach Horn (KZ. 33, 434) np. nikuhīdan \\\"tadeln, schmähen\\\" = skr. kutsay- \\\"schmähen, tadeln\\\"', and Walde-Pokorny I 378 and Pokorny 595 both adopt it. So the arrow root → Persian is exactly what all three cited references say; only the spelling in the box is corrupt. Cheung's Etymological Dictionary of the Iranian Verb has no entry for this stem, so no modern Iranist re-examination is available on disk.\",\n          \"derivation_fa\": \"ریشه‌شناسی این بند درست است ولی آوانگاری لاتینِ چاپ‌شده غلط است: کتاب «nekŭkîdan» چاپ کرده، با k به‌جای h، حال آنکه صورت فارسیِ همان جعبه، «نکوهیدن (نکوهش)»، درست است و همهٔ منابع آن را nikūhīdan می‌نویسند. این فعل پیشوندی است: پیشوند نـ (ni- «فرود، پایین») + ستاکِ *kauH-/kūh- «سرزنش کردن»، و دنبالهٔ nikōhīdan فارسی میانه است که مکنزی آن را ثبت کرده (nikōh-، nikōhīdan، nikōhišn «نکوهش»، nikōhišnīg «نکوهیده، سزاوار سرزنش»). واکهٔ ō فارسی میانه پیش از h در فارسی نو به ū برکشیده شده و پایانهٔ مصدریِ -īdan بی‌تغییر مانده است. پیوند هندواروپاییِ آن از آنِ هوبشمان است، درست در همان صفحه‌ای که نورایی ارجاع داده: «مطالعات فارسی» ص ۱۰۲: «به گفتهٔ هرن، فارسی نو nikuhīdan «تادِلن، شمَهِن» برابر است با kutsay- سنسکریت «سرزنش کردن»» — و والده-پوکورنی (ج ۱ ص ۳۷۸) و پوکورنی (ص ۵۹۵) نیز همان را پذیرفته‌اند. پس خطا، خطای چاپی کتاب است نه خطای خوانش اسکن و نه خطای ریشه‌شناسی.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"nekŭkîdan\",\n          \"correct_form\": \"nekūhīdan (nikūhīdan) «نکوهیدن»\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%86%DA%A9%D9%88%D9%87%DB%8C%D8%AF%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:595\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, lemma keuəd- (Page(s): 595-596): 'Old Indic kutsayati \\\"blasphemes, reproves\\\", kutsa \\\"abuse, reprimand\\\", npers. nikūhīdan \\\"rebuke, vilify, scold\\\"'. Pokorny spells the Persian word with h.\"\n            },\n            {\n              \"ref\": \"WLD1:378\",\n              \"status\": \"supports\",\n              \"note\": \"WLD_Bd1_pages.txt p. 378, article qeud-: 'npers. nikūhīdan \\\"tadeln, schmähen\\\" Horn KZ. 33, 434, 443, Hübschmann Pers. St. 102, 239'. Walde-Pokorny even names Hübschmann p. 102 — Nourai's third reference.\"\n            },\n            {\n              \"ref\": \"HUB:102\",\n              \"status\": \"supports\",\n              \"note\": \"HUB.txt line 3593 (page marker '— 102 —' just above, in note 1038): 'Hierher nach Horn (KZ. 33, 434) np. nikuhīdan \\\"tadeln, schmähen\\\" = skr. kutsay- \\\"schmähen, tadeln\\\". Schon bei Vullers, Radices, s. v.' Exactly Nourai's Persian ↔ Sanskrit equation.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD, English–Pahlavi index s.v. 'blame' (PHD_mackenzie.txt lines 6045-6050)\",\n              \"stance\": \"supports\",\n              \"note\": \"'blame (n.) āwēnišn, ērang(īh), nikōh-; (v.) nikōhīdan … blameworthy āwēnišnīg, nikōhišnīg' and 'execrate nikōhīdan'. The Middle Persian ancestor of نکوهیدن is well attested.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb (CHEUNG.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grep for 'nikōh', 'nikoh', 'kaud' finds no entry; Cheung's only *kauH is the s-less variant of *skauH 'to poke, scratch, earmark', an unrelated root. He does not treat this verb.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-hā, pp. 498-499 s.v. نکوهش، نکوهیدن\",\n              \"stance\": \"supports\",\n              \"note\": \"The entry lists Pahlavi NIKŌHĪDAN, Sanskrit KUTSAYATI, Greek KUDAZŌ and the Germanic/Slavic 'shout, cry' words, with the note '۲- احتمال دارد که واژه‌ی انگلیسی SHOUT هم از همین ریشه باشد' — an independent modern Persian source reproducing Nourai's whole entry.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Moʿin s.v. نکوهیدن (via abadis.ir)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(نَ یا نِ دَ) (مص م.) سرزنش کردن، ملامت کردن' — confirms the gloss 'to blame'; Dehkhodā adds 'مذمت نمودن، عیب گفتن'. Neither gives an etymology.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss (HRN.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"The Grundriss has no numbered entry for nikūhīdan (the neighbouring n- entries are 1044 nēne, 1046 nevāxtan, 1047 nevāde); Horn made the claim in KZ 33, 434, the article Hübschmann and Walde-Pokorny cite, not in the Grundriss.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"kutsa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. kutsā- f. / kutsa- 'abuse, reproach, censure', with the denominative verb kutsayati 'reviles, reproaches' (Monier-Williams; already Vedic as the personal name Kutsa). Pokorny 595 and Walde-Pokorny I 378 make it the Indic member of the very root Nourai draws: 'Old Indic kutsayati \\\"blasphemes, reproves\\\", kutsa \\\"abuse, reprimand\\\"'. Formally it is a *kud-s- or *kuts- stem beside Gk. kudázō 'revile' and the Persian verb; Walde-Pokorny notes that Wackernagel's alternative (linking it to Skt. cotati 'whets') is 'nicht besser'. Mann (IEC) also keeps the kutsayati ~ kūdázō equation, so the word and the equation are secure even where the wider root is doubted.\",\n          \"derivation_fa\": \"سنسکریت kutsā- «سرزنش، نکوهش» و فعل مشتقِ آن kutsayati «سرزنش می‌کند، ناسزا می‌گوید» است (در وداها نیز نامِ خاصِ Kutsa از همین ریشه). پوکورنی (ص ۵۹۵) و والده-پوکورنی (ج ۱ ص ۳۷۸) همین واژه را عضو هندیِ ریشه می‌شمارند و آن را در کنارِ kudázō یونانی و «نکوهیدن» فارسی می‌نشانند؛ از دید ساخت‌واژه ستاکی است با پسوندِ -s- (یعنی *kud-s-). والده-پوکورنی می‌افزاید که پیشنهاد جایگزینِ واکِرناگِل (پیوند با cotati «تیز کردن») «بهتر نیست». مان نیز در فرهنگ تطبیقی خود همین برابریِ سنسکریت–یونانی را نگاه داشته است. پس ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:595\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, lemma 'keuəd- kud-, Meaning: to cry' (Page(s): 595-596): 'Old Indic kutsayati \\\"blasphemes, reproves\\\", kutsa \\\"abuse, reprimand\\\"'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 378 s.v. qeud-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. kutsáyati \\\"schmäht, tadelt\\\", kutsa \\\"Schmähung, Tadel\\\" (nicht besser nach Wackernagel Ai. Gr. I 115 zu cotati \\\"wetzt\\\")'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. kūd- (IEC.txt line 8265)\",\n              \"stance\": \"partial\",\n              \"note\": \"'A variant of type *kuds- occurs in Skt. kutsāmi, kutsayāmi, kutsyāmi \\\"abuse\\\"' — same equation, but Mann's root gloss is 'fling, cast, reject, scorn'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck p. 1251 §18.13\",\n              \"stance\": \"supports\",\n              \"note\": \"'… *keud- in Grk. κυδάζω, Skt. kuts- \\\"revile, abuse\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle English\",\n          \"words\": \"sčŭten\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Middle English verb exists but not in this shape. Pokorny 596 and Walde-Pokorny I 378 print the German-style spelling 'mengl. schuten \\\"vociferari / cry out, shout, bawl\\\"', and Nourai has mechanically re-transliterated the German digraph sch- as 's' + 'č', producing 'sčŭten', which is not a Middle English spelling and not a possible one (ME had no č). The real headword is MED shouten (also schouten, shuten, showten) 'to shout, cry out', first in Chaucer, Troilus ii.614 (c. 1385) per Skeat, and c. 1300 per Etymonline; NE shout continues it with the regular ME /uː/ > /aʊ/ Great Vowel Shift diphthongisation. The page image (data/verification/sources/refs/ocr/BOOK/264.png) shows 'sčŭten' printed, so the extraction is faithful and the fault is the book's. On substance the arrow root → ME is only tentative even in Nourai's own sources: Pokorny prefixes it 'with anlaut. s- (previously after schallen, schreien!) PERHAPS Middle English schuten', and Walde-Pokorny 'Mit anl. s- … vielleicht mengl. schuten' — i.e. an s-mobile guess, not an established derivation.\",\n          \"derivation_fa\": \"این فعل انگلیسی میانه هست، اما نه به این صورت. پوکورنی (ص ۵۹۶) و والده-پوکورنی (ج ۱ ص ۳۷۸) آن را به شیوهٔ آلمانی «mengl. schuten» می‌نویسند و نورایی سه‌نگارِ sch- را ماشین‌وار به «s + č» برگردانده و «sčŭten» ساخته است؛ چنین صورتی در انگلیسی میانه وجود ندارد و اصلاً ممکن نیست، زیرا انگلیسی میانه واجِ č با این نگارش نداشت. صورت درست shouten (نیز schouten، shuten) «فریاد زدن» است که نخستین‌بار در «تروئیلوس» چاسر (حدود ۱۳۸۵ م.) و به گفتهٔ اتیمانلاین از حدود ۱۳۰۰ م. گواهی شده است. تصویر صفحهٔ چاپی نشان می‌دهد که کتاب همین «sčŭten» را چاپ کرده، پس خطای چاپی کتاب است نه خطای خوانش اسکن. افزون بر این، خودِ پیوند این بند با ریشه در منابعِ موردِ استنادِ نورایی نیز تنها «شاید» است: پوکورنی می‌نویسد «با s- آغازین (پس از واژه‌های آوایی؟) شایدْ انگلیسی میانه schuten».\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"sčŭten\",\n          \"correct_form\": \"schuten / shouten (ME)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/shout\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:596\",\n              \"status\": \"partial\",\n              \"note\": \"POK_full.txt, lemma keuəd- (Page(s): 595-596): 'with aniaut. s- (previously after schallen, schreien!) perhaps Middle English schuten \\\"cry out, shout, bawl, exclaim\\\", engl. to shout \\\"cry loudly\\\", Old Icelandic skūta, skūtī \\\"derision, gibe\\\"'. The word is there and on Nourai's page, but the spelling is schuten and the connection is flagged 'perhaps'.\"\n            },\n            {\n              \"ref\": \"SYN:1251\",\n              \"status\": \"supports\",\n              \"note\": \"Buck p. 1251 §18.13 SHOUT, CRY OUT: 'ME shoute, NE shout : ON skūta, skūti \\\"taunt, jibe\\\", prob. fr. *skeud- beside *keud- in Grk. κυδάζω, Skt. kuts- \\\"revile, abuse\\\". Walde-P. 1.378.' Buck spells the ME word shoute.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 378 s.v. qeud-\",\n              \"stance\": \"partial\",\n              \"note\": \"'Mit anl. s- (erst nach schallen, schreien u. dgl.?) vielleicht mengl. schuten \\\"vociferari\\\", engl. to shout \\\"laut schreien, rufen, jauchzen\\\", aisl. skúta, skúti \\\"Spott, Stichelei\\\"'. Spelling schuten; connection 'vielleicht'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict. s.v. Shout (SKT.txt line 17179)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Shout. (Unknown). M.E. shouten; Chaucer, Troil. ii.614. Etym. unknown; cf. Icel. skúta, skúti, a taunt.' Skeat spells the ME form shouten and declines any IE root.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. shout (KLN_1966.txt line 35048)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'shout, intr. and tr. v. — ME. shouten, of uncertain origin. Cp. ON. skuta, \\\"a taunt\\\".' Again shouten, and no root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"shout\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NE shout is the straightforward continuation of ME shouten (c. 1300; Chaucer, Troilus ii.614), with ME /uː/ diphthongised to /aʊ/ by the Great Vowel Shift and the -en infinitive lost; the transitive sense 'utter in a loud vehement voice' is late 14th c. So the ME → NE arrow itself is beyond doubt. What is doubtful is what stands behind it, i.e. the whole chain back to Nourai's root. The English etymological tradition treats the word as of unknown origin: Skeat '(Unknown) … cf. Icel. skúta, skúti, a taunt', Klein 'of uncertain origin. Cp. ON. skuta \\\"a taunt\\\"', Etymonline 'a word of unknown origin; perhaps from the root of shoot (v.) on the notion of \\\"throw the voice out loudly\\\", or related to Old Norse skuta \\\"a taunt\\\"' — and where Etymonline does reach for a root it reaches for *skeud- 'to shoot, chase, throw' (Pokorny 956, Watkins skeud-), a DIFFERENT root from Nourai's keuəd- 'to cry' (Pokorny 595). Watkins/AHD does not index SHOUT at all. Only Buck (p. 1251) and Walde-Pokorny/Pokorny place it with *keud-/*skeud- 'revile', and both hedge ('prob.', 'vielleicht'). Verdict plausible: the node is a real word correctly derived from its ME parent, but the attachment of that parent to this root is a minority, pre-war view.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی shout دنبالهٔ بی‌واسطهٔ shouten انگلیسی میانه است (نخستین گواهی حدود ۱۳۰۰ م.)؛ واکهٔ کشیدهٔ /uː/ در «جابه‌جایی بزرگ واکه‌ها» به دوواکهٔ /aʊ/ بدل شده و پایانهٔ مصدری -en افتاده است، پس خودِ این پیکان بی‌چون‌وچراست. آنچه محل تردید است، پیوندِ این واژه با ریشهٔ نورایی است. سنّت ریشه‌شناسی انگلیسی آن را «نامعلوم» می‌داند: اسکیت «(نامعلوم) … سنجیده شود با skúta ایسلندی «طعنه»»، کلاین «خاستگاه نامطمئن»، و اتیمانلاین «واژه‌ای با خاستگاه ناشناخته؛ شاید از ریشهٔ shoot به معنی «صدا را با نیرو بیرون افکندن»، یا مرتبط با skuta نُرس باستان «طعنه»». نکتهٔ مهم آنکه ریشه‌ای که اتیمانلاین و واتکینز پیشنهاد می‌کنند، *skeud- «تیر انداختن، پرتاب کردن» (پوکورنی ص ۹۵۶) است، نه keuəd- «فریاد زدن» (پوکورنی ص ۵۹۵) که نورایی به کار برده. تنها باک و والده-پوکورنی این واژه را زیر ریشهٔ «نکوهیدن» می‌نشانند و آن هم با قید «شاید». بنابراین حکم: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/shout\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own in the book; the parent Middle English box cites POK:596 and SYN:1251, both checked there.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. shout (KLN_1966.txt line 35048)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'shout, intr. and tr. v. — ME. shouten, of uncertain origin. Cp. ON. skuta, \\\"a taunt\\\".' No Indo-European root offered.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Shout (SKT.txt line 17179)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Shout. (Unknown). M.E. shouten; Chaucer, Troil. ii.614. Etym. unknown; cf. Icel. skúta, skúti, a taunt.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 2252)\",\n              \"stance\": \"silent\",\n              \"note\": \"The index runs '… SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- SHOW keu-! SHOWER! kēwero-' — SHOUT is simply absent, i.e. Watkins assigns it to no root.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck p. 1251 §18.13 SHOUT, CRY OUT\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME shoute, NE shout : ON skūta, skūti \\\"taunt, jibe\\\", prob. fr. *skeud- beside *keud- in Grk. κυδάζω, Skt. kuts- \\\"revile, abuse\\\". Walde-P. 1.378.'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T20:48:47.743Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-264.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T20:48:52.117Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-264.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 264"
}
```


### [2026-09-06T20:48:55.866Z] TOOL RESULT

```
JSON OK
nodes verified: 9/9
node verdicts: {'confirmed': 4, 'disputed': 1, 'unverified': 1, 'transcription_suspect': 2, 'plausible': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 12, 'contradicts': 1, 'not_checked': 2, 'partial': 1}
books consulted: {'partial': 3, 'supports': 13, 'silent': 9, 'contradicts': 5} | by book: {'WLD': 4, 'HRN': 3, 'BRT': 2, 'KNT': 2, 'PHD': 2, 'MON': 2, 'ARY': 2, 'SYN': 2, 'SKT': 2, 'KLN': 2, 'NYB': 1, 'BQT': 1, 'POK': 1, 'BOOK': 1, 'CHEUNG': 1, 'IEC': 1, 'AHD': 1}
```


## [2026-09-06T20:49:17.255Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-264.json`; `verify_check.py 264` reports 9/9 nodes, 0 PROBLEM lines.

**Page 264 (book p. 234) — Keu 4 / Keued**

- Roots: 1 confirmed (Keu 4, Keu-bh), 1 plausible (Keued, Keud, Qeud, Skeud 2)
- Nodes: 4 confirmed, 1 plausible, 1 disputed, 2 transcription_suspect, 1 unverified (the blank pass-through box #5)
- Ref checks: 12 supports, 1 partial, 1 contradicts, 2 not_checked (nodes with no refs). All of Nourai's citations that could be located were located: POK 594/595/596, BRT 221 + 1631, SYN 995 + 1251, HRN 166 + 237, HUB 102, WLD1 378, BQT 1185 (vol. 2, the leaf carrying both سور and سورنای with Mo'in's footnote).

Flagged items:
- **disputed — Keu 4, node #4 "Old Persian caune 'bright red, a plant with bright colored fruits'"**: no such Old Persian word (silent in Kent and Bartholomae). Nourai conflated three separate items from Pokorny 594 / Walde-Pokorny I 368: "bright red" = Skt. śoṇa-, "plant with bright coloured fruits" = Russ./SCr. sunica 'raspberry', and *caune* = **Old Prussian** 'marten' (apr. caune, beside Latv. cauna, Lith. kiaunė) — which Pokorny himself doubts belongs to this palatal root at all.
- **transcription_suspect — Keued, node #1 "nekŭkîdan"**: book misprints *k* for *h*; correct is nekūhīdan (the Persian script نکوهیدن in the same box is right). Etymology itself sound (MP nikōhīdan; HUB 102 = Skt. kutsay-).
- **transcription_suspect — Keued, node #3 "sčŭten"**: Nourai re-transliterated Pokorny's German-style "mengl. schuten" as s + č; no such ME spelling exists. Correct: ME schuten / shouten.

Extraction errors for the owner: **none** — the page image (300/400 dpi renders, copy saved at `data/verification/sources/refs/ocr/BOOK/264.png`) shows "caune", "nekŭkîdan", "sčŭten" and the empty box all printed exactly as the JSON has them; every oddity is the book's.

Notable substantive finding beyond the flags: the Persian سور chain is fully independently corroborated (MacKenzie CPD p. 79 "sūr … meal, feast, banquet"; Horn no. 753; Mo'in "[په.] جشن، ضیافت"; Dehkhoda "اوستا سوئیریا … پهلوی سور"; Aryanpur p. 363), though modern reconstruction routes NP sūr through Old Persian *θūryas rather than through Avestan itself. Conversely the *Keued* root is a 1927/1959-only reconstruction: Watkins/AHD has no such root and does not index SHOUT; Klein, Skeat and Etymonline call *shout* of unknown origin, and Etymonline's tentative root is the *other* *skeud-* 'to shoot' (Pok. 956).
