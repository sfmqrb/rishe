# Verification process log — verify-page-68


## [2026-09-05T05:22:42.284Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 68 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-68.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-68.json. Write /home/sfmqrb/git/rishe/data/verification/page-68.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 68` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:22:43.920Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:22:44.631Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:22:44.645Z] TOOL RESULT

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


## [2026-09-05T05:22:44.829Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-68.txt"
}
```


### [2026-09-05T05:22:44.851Z] TOOL RESULT

```
1	=== PDF page 68 (book page 38) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Âtos, Atta, Ato, Athal : father, mother, family, race  (refs POK:71; AHD:1507)
4	#1 (parent #0) [Avestan] refs=POK:71; FAF:10 | âthoya, âthwya : husband, man, father of Thraêtaona (King Feraydoun)
5	  #2 (parent #1) [Pahlavi] refs=FAF:10 | Âspiyan
6	    #3 (parent #2) [Persian] refs=SNS:135; MON5:7; FAF:10 | Âbtîn «آبتین» : name of one of the early kings in Iran | extra: آتبین
7	#4 (parent #0) [Old High German] refs=KLN:27,44; AHD | adal : lineage, ancestry ; adel-beraht : bright in nobility (Albert) ☞Bhereg ; athal-wolf : noble wolf (Adolph) ☞Wel 2
8	  #5 (parent #4) [English] refs=KLN:44; AHD | Albert ; Adolph
9	#6 (parent #0) [Indo-European] refs=SYN:94; WLD1:44; IEC:178,1369 | Tât, Tâta : daddy ; Dhědh : grandfather
10	  #7 (parent #6) [Sanskrit] refs=SYN:94; IEC:1369 | tata, tâta : grandfather
11	  #8 (parent #6) [Greek] refs=IEC:178; SYN:94 | tĕthĕ : father, grandfather
12	  #9 (parent #6) [Latin] refs=SYN:94 | tata : father, grandfather
13	  #10 (parent #6) [Russian] refs=KLN:396 | tata : father
14	  #11 (parent #6) [English] refs=KLN:396 | dad ; daddy | NOTE: KLN:396 claims these and most other words on this chart to be of childish origin and does not provide the derivation path
15	  #12 (parent #6) [Persian] refs=IEC:178; MON:1499 | dadeh «دده» : grandfather, aunt
16	--- entry 1 ---
17	ROOT Atr -> redirect to Ater
18	--- entry 2 ---
19	ROOT Atta -> redirect to Âtos
20	--- entry 3 ---
21	ROOT Au 1 -> redirect to Ôus 1
22	
```


## [2026-09-05T05:22:48.075Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-68.json",
 "description": "Read source JSON page 68"
}
```


### [2026-09-05T05:22:48.118Z] TOOL RESULT

```
{
  "pdf_page": 68,
  "book_page": 38,
  "entries": [
    {
      "root": {
        "name": "Âtos, Atta, Ato, Athal",
        "lang": "Indo-European",
        "refs": "POK:71; AHD:1507",
        "gloss": "father, mother, family, race"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:71; FAF:10",
          "words": [
            {"translit": "âthoya, âthwya", "gloss": "husband, man, father of Thraêtaona (King Feraydoun)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FAF:10",
          "words": [
            {"translit": "Âspiyan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:135; MON5:7; FAF:10",
          "words": [
            {"translit": "Âbtîn", "gloss": "name of one of the early kings in Iran", "script": "آبتین"}
          ],
          "script_extra": "آتبین",
          "note": null,
          "quote": {
            "text": "تو بشناس کز مرز ایران زمین - یکی مرد بُد، نام او آبتین",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old High German",
          "refs": "KLN:27,44; AHD",
          "words": [
            {"translit": "adal", "gloss": "lineage, ancestry", "script": null},
            {"translit": "adel-beraht", "gloss": "bright in nobility (Albert)", "script": null, "see": ["Bhereg"]},
            {"translit": "athal-wolf", "gloss": "noble wolf (Adolph)", "script": null, "see": ["Wel 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:44; AHD",
          "words": [
            {"translit": "Albert", "gloss": null, "script": null},
            {"translit": "Adolph", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "SYN:94; WLD1:44; IEC:178,1369",
          "words": [
            {"translit": "Tât, Tâta", "gloss": "daddy", "script": null},
            {"translit": "Dhědh", "gloss": "grandfather", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Sanskrit",
          "refs": "SYN:94; IEC:1369",
          "words": [
            {"translit": "tata, tâta", "gloss": "grandfather", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Greek",
          "refs": "IEC:178; SYN:94",
          "words": [
            {"translit": "tĕthĕ", "gloss": "father, grandfather", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "Latin",
          "refs": "SYN:94",
          "words": [
            {"translit": "tata", "gloss": "father, grandfather", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "Russian",
          "refs": "KLN:396",
          "words": [
            {"translit": "tata", "gloss": "father", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:396",
          "words": [
            {"translit": "dad", "gloss": null, "script": null},
            {"translit": "daddy", "gloss": null, "script": null}
          ],
          "note": "KLN:396 claims these and most other words on this chart to be of childish origin and does not provide the derivation path",
          "quote": null
        },
        {
          "id": 12,
          "parent": 6,
          "lang": "Persian",
          "refs": "IEC:178; MON:1499",
          "words": [
            {"translit": "dadeh", "gloss": "grandfather, aunt", "script": "دده"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Atr",
        "redirect": "Ater"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Atta",
        "redirect": "Âtos"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Au 1",
        "redirect": "Ôus 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:22:48.231Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:22:48.280Z] TOOL RESULT

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


## [2026-09-05T05:22:52.167Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','FAF','SNS','MON','KLN','SYN','WLD','IEC','BQT','ARY','FSF','FRS','IRN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-05T05:22:54.053Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v
```


## [2026-09-05T05:22:59.658Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','IEC','KLN','WLD','AHD','SNS']:\n    print(k, d[k].get('page_offset'))\n    print('  hint:', str(d[k].get('lookup_hint'))[:400])\n\""
}
```


### [2026-09-05T05:23:01.056Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
  hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
  hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
```


## [2026-09-05T05:23:04.053Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: at\" POK_full.txt | head -30; echo ====; grep -n \"Page(s): 71\" POK_full.txt | head"
}
```


### [2026-09-05T05:23:04.114Z] TOOL RESULT

```
Exit code 1
4120:Root / lemma: ati!^- 
7174:Root / lemma: ati, ato- 
7237:Root / lemma: at-, *atno- 
7243:n. year' prove that Root/ lemma: en-2: year' : Root/ lemma: at-, *atno-\ to go; year' : 
9350:Root / lemma: at(e)r- 
9356:Root/ lemma: at(e)r-\ "fire, *blow the fire' derived from a suffixed Root/ lemma: au(e)-10, 
9390:Root / lemma: atos, atta {hatta) 
26886:n. year' prove that Root/ lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
29546:Root/ lemma: etro-\ "hurried, swift' derived from Root/ lemma: at(e)r-\ fire' 
36219:n. year' prove that Root / lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
(eval):1: === not found
```


## [2026-09-05T05:23:04.226Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==79' POK_01.txt | head -80"
}
```


### [2026-09-05T05:23:05.820Z] TOOL RESULT

```
  assimiliert  sein);  lat.  ai<i7|j|
,ein   störähnliclier   großer   Fisch   im    Fo^  (wohl   gall.   oder  ligur.:    Holderl
Altcelt.    Sprachsch.  s.  v.,  M.-L.  766;    anders    Hirt   IF.  37,  222);   alit.  aiis^
lit.  Ötas,  lett.  äte  ^Steinbutten
WP.  I  44  WH.  I  78.
ati,  ato-  ,über  etwas  hinaus^,  daher  bei  einer  dem  Sprecher  zugewendeteij Bewegung-  ^(über  den  Standort  des  Sprechenden)  zurück^,  endlich  ein fach  ,her^  unter  Verblassen  der  Vorstellung  eines  überrannten  Zieles oder  Ortes.  Vgl.  zur  Bedeutungsfrage  bes.  Brugmann  Grdr.  IP  2,  844 f. Die  Färbung  des  anlautenden  Vokals  steht  durchs  Lat.-Kelt.  (Griech.V als  idg.  a-  fest,  und  es  liegt  kein  triftiger  Grund  vor,  den  balt.-slav.| germ.  (und  ar.)  Formen  idg.  *o-  zuzuschreiben,  bloß  weil  dies  einen schulgerechten  Ablaut  zum  e-  von  *e^i  bildete.  Mit  eti  (s.  dort)  be^ stand  mindestens  Gleichheit  der  Bedeutung  und  Austausch  im  Ge-:- brauche.    Ist  ati  Reduktionsstufe  zu  eti?  '•
Ai.  ati  , über— hinaus  (adnominal  m.  Akk.),  überaus,  sehr^  (Adv.  und Präverb),  av.  aiti-^  apers.  atiy-  ds.  Adv.  (als  1.  Kompos. -Glied  und  Präverb (vor  i-  ,gehen^  als  ,vorübergehen,  vorüberziehen^  und  hai^-  , tragen'  als , wieder  hinüberbringen,  tragen  zu');  ar.  ati  kann  auch  idg.  *eti  mit  ver- treten.
Gr.  vermutlich  in  dc-aQ  ,aber'  (vgl.  avTäg  aus  a-öv^  äg]  Brugmann-Thumb 623,  KVG.  616;  bei  Verbindung  mit  äusg,  got.  sundrö,  bliebe  der  att.  Lenis' unerklärt).     Lat.  at  ,aber'  aus   steigernd-entgegensetzendem  , darüber  hin- aus',   welch    letztere    Bed.  in    at-avus,    at-nepos    (nicht   in   a'pprwiE  u.  dgl.,* s.  Skutsch  AflL.   12,  213).     Gall.  ate-  (aus  "^ati-)    in  Aiegnätus  (=  mbret.^ {h)aznat,    nbret.    anat  ,bekannt')    u.  dgl,    abrit.  Ate-cotti  ,die    sehr    Alten',! air.  aith-,  vortonig  ad-  , wieder,  ent-',  mcjmr.  at-,  ncymr.  ad-,  ed-  (Belege* z.  B.  bei  Fick  IP  8,  Pedersen  KG.  II  292);  hierher  als  *ate-ko-n  wohl  mir4 athach   n.   ,eine   gewisse  Zeit',    cjmr.  adeg  m.  ds.,    vgl.   gall.  ATENOVX (Bezeichnung  der  2.  Monatshälfte),  Thurneysen  ZcP.  20,  358?
Got.  ap-Pan  ,aber,  doch'  (sehr  fraglich  ist  dagegen   Herleitung  von  got.  ^ as.  ak,    ags.   ac   ,aber',    ahd.    oh   ,sondern,   aber'    aus    *ap- -{-  ke  =  gr.  ys] anders,  aber  kaum  zutreffend  Holthausen  IF.  17,  458:  =  gr.  itys,  lat.  age ,geh!  wohlan!').
Lit.  at-,  ata-,  jünger  auch  ati-,  in  Nominalkompos.  atö-  ,zurück-,  ab-, her-'  (s.  Brugmann  Grundr.  II  ^  2,  844  f.),  apr.  et-,  at-  (wohl  nur  aus  halt. at-,    Trautmann  46);
^  aksl.   ot-,    ot^  ,weg,   ab,    aus',   adnominal  m.  d.  Gen.-Abl.,   führt   Meillet Et.  155  f.  auf  gen.-ablativisches  "^atos  zurück  (ob  =  ai.
```


## [2026-09-05T05:23:10.341Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9385,9440p' POK_full.txt"
}
```


### [2026-09-05T05:23:10.393Z] TOOL RESULT

```
Possibly affiliation from Irish a/th {Gen. atho) f., cymr. odynt ' oven, stove ', s. Pick 11^ 9. 

References: WP. I 42, WH. I 75 f., 849 f. 
Page(s): 69 

Root / lemma: atos, atta {hatta) 
Meaning: father, mother 
Material: 

In a- grade: 

Hittite at-ta-as {attas) 'father'. 
Old Indie 5//a 'mother, older sister ', atti-h ' older sister ', osset. ada, gr. aiTa ' old man, old 
fellow, father', dial. Akk. qtsiv, ottsiv 'grandfather', Latin aftam. 'father; term of 
endearment of the children towards the father ', Gothic a//a 'father' (Demin. Attila), Old 
Frisian aththaAs., Old High German a//c» 'father, forefather, ancestor' (//by running always 
besides unpostponed neologism), alb. {*h2at) at, PI. e/e/'' father'. 

In e- grade: 

Demin. Old High German Ezz//o 'father'. 

In o- grade: 

Old Church Slavic c»/6Cb 'father'; alb. {*h30t-sja) joshe^ (on the maternal side) 

grandmother'. 

Common /7->y- Slavic Albanian; h->J-, y-0\6 Indie Tocharian. 

In a- grade: 



A similar *ato-s\n Germanic *a/=>a/a, *dA'e/5 appears the basis from Old High German 
ada/' sex, gender', Modern High German Ade/, Old Saxon atha//, Old English sedeluH. 
PL ' noble parentage ', Old Icelandic adar (the rudimentary basis of an organ or other 
part, esp. in an embryo) aniage, sex ', Tocharian A ataF man '; here also Avestan a^wya- 
" name of the fathers Oraetaond ^ as ' from noble parentage '? 

The affiliation from gr. mokoc, ' in a juvenile manner, childish ', araAAw ' gathers, waits 
and is in habit ' and " jumps cheerfully like a child ', Redupl. ariTaAAu) " draws up (Redupl. 
under influence from TiGnvr) " nurse '?), is denied by Leumann Gl. 15, 154. 

In e- grade: 

Adj. Old High German edili. Old Saxon ethili. Old English aedele^ noble, aristocratic ' 

In o- grade: 

lengthened grade Old High German uodal. Old Saxon othil, here Gothic haimot^liu. " 
genotype ', compare with the same vocal length Old High German Uota (actually ' great- 
grandmother '), Old Norse 0(fa/" (fatherly) genotype ' (compare also Old High German 
fater-uodal. Old Saxon fader-odiV property inherited from a father, patrimony '); 

In e- grade:
```


## [2026-09-05T05:23:11.042Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==80' POK_01.txt | head -60"
}
```


### [2026-09-05T05:23:12.774Z] TOOL RESULT

```
  atah  ,von  da'?  eher
71
-St   *e-  mit  dem  ablat.  Adv.-Formans  -tos)]  idg\  '-^ati  (und '-^eti)  wäre dazu  Lok.;   beides  bleibt  sehr  unsicher.
*  D'o  Doppelheit  lit.  ata- :  atö-  erinnert  an  pa- :  pö    (s.  *ajp6),    und    es  ist ,  frao-lich^  ob  man  in  atö  einen  nach  Art  der  o-St.  gebildeten  Abla-
*  ♦  *atüd   sehen    darf.     Im  Slav.  ist    die   Form  auf  langen  Yokal  weiter- bildet in  russ.  usw.  otdva  ^Grummet^;    wie    apr.  attolis,   lit.  atölas,    lett.
^täls  atals  ^Grummet^  Für  idg.  Alter  der  kurzvokalischen  Form  lit.  atä- e»  id«»-.   *«^ö-  (vgl.  zum  Ausgang  '^ajpo,  *upo)  spricht:
lir.  do-  to-  Präfix  ^zu^  mit  (idg.  ?)  Schwund  des  anl.  Vokals  (Meillet aaO./stokes  BB.  29,  171,  Federsen  KG.  II  74),  wohl  auch  illyr.  to-,  alb. te    zu,  bei'  (Skok  bei  Pokorny  Urill.  50).
WP.  I  42  f.,  WH.  I  75,  421  f.,  863.
itoSf  atta  Lallwort  ,Vater,  Mutter^
Ai.  ctttä , Mutter,  ältere  Schwester^,  atti-h  ,ältere  Schwester^,  osset.  äda^  gr. ÄVf«  , Väterchen*,  dial.  Akk.  ärstv,  äzTsiv  , Großvater',  lat.  atta  m.  , Vater; Kosewort  der  Kinder  dem  Vater  gegenüber',  got.  atta  , Vater'  (Demin.  Attila, tXA.Ezz'do),  afries.  aththa  ds.,  ahd.  atto  ,Vater,Vorfalir'  {tt  durch  stets  daneben- laufende Neuschöpfung  unverschoben),  aksl.  othc^  (*attikös)  , Vater'';  alb.  at , Vater';  jos/iö, mütterliche  Großmutter'  (^ät-siä?),  hett.  at-ta-as  (attas) ,Ya.ter'.
Ein  ähnliches  *äto-s  in  germ.  *apala,  '^öpela  scheint  auch  die  Grundlage von  ahd.  adal  , Geschlecht',  nhd.  Adelj  as.  athali,  ags.  zdelu  N.  PL  ,edle Abkunft',  aisl.  adal  , Anlage,  Geschlecht'^  Adj.  ahd.  edili,  as.  ethili,  ags. xdele  ,adelig,  edel',  dehnstufig  ahd.  nodal,  as.  öthil,  ags.  edel,  anord.  ödal , (väterliches)  Erbgut'  (vgl.  auch  ahd.  fater-uodal,  as.  fader-ödil  ,patrimo- nium');  hierher  got.  halmöpli  n.  , Erbgut',  vgl.  mit  derselben  Vokallänge ahd.  Vota  (eigentlich  , Urgroßmutter'),  afries.  edila  , Urgroßvater';  toch.  A ätäl  ,Mann';  hierher  auch  av.  ä-^icya-  ,Name  des  Vaters  QraEtaona's^  als ,von  adeliger  Abkunft'?
Die  Zugehörigkeit  von  gr.  äTaXög  ,]ugendlich,  kindlich',  äräXXo}  _,ziehe auf,  warte  und  pflege'  und  ,springe  munter  wie  ein  Kind',  red.  «TtraAAw ,ziehe  auf  (Redupi.  unter  Einfluß  von  Tid^rjvr]  ,Amme'?),  wird  von  Leu- mann Gl.  15,  154  bestritten.
Ein  auf  den  verschiedensten  Sprachgebieten  sich  stets  neu  bildendes Lallwort  (z.  B.  elam.  atta,  magy.  atija  , Vater',  türk.  ata,  bask.  aita  ds.). Ahnlich  tata.
WP.  I  44,  WH.  I  77,  850,  Feist  62,  233,  Trautmann  16.
■T-  au  Ausruf  des  Schmerzes,   der  Verwirrung,  Entrüstung.
Ai.  0,  lat.  au,  ags.  ea,  mhd.  ou(ioe),  nhd.  au,  lett.  aü,  äu  (zweisilb.  au, avu  bei
```


## [2026-09-05T05:23:32.110Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD watkins atta ===\"; grep -n \"^at-\\|^atta-\\|^ater-\\|atta-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T05:23:32.172Z] TOOL RESULT

```
=== AHD watkins atta ===
298:at-. To go; with Germanic and Latin derivatives meaning a year (conceived as “the period gone through, the revolving year”). Suffixed form *at-no- in Latin annus, year: ANNALS, ANNUAL, ANNUITY; ANNIVERSARY, BIEN- NIUM, DECENNIUM, MILLENNIUM, OCTENNIAL, PEREN- NIAL, QUADRENNIUM, QUINDECENNIAL, QUINQUENNIUM, SEPTENNIAL, SEXENNIAL, SUPERANNUATED, TRIENNIUM, VICENNIAL. [Pok. at- 69.]
299:ater-. Fire. 1. Suffixed zero-grade form *dér-o- in Latin ater (feminine dtra), black (< “blackened by fire’): ATRABILIOUS. 2. Suffixed zero-grade form *dér-yo- in Latin dtrium, forecourt, hall, atrium (perhaps originally the place where the smoke from the hearth escaped through a hole in the roof): ATRIUM. 3. Compound shortened zero-grade form “atro-akv- (*ok¥-, “-looking”; see ok"-) in Latin dtréx, “black-looking,” frightful: aTRocIOUvS. [Pok. die)r- 69.]
1006:steg-. Pole, stick. O-grade form *stog- in Germanic *stak- in: a. Old English staca, stake: sTAKE!; b. Old Norse stakkr, haystack: stack; c. Old Norse staka, to push, cause to stumble (as with a stick): STAGGER; d. Old Italian attacare, to attack: ATTACK; e. Old French atta- chier, to attack: ATTACH; f. Spanish estaca, stake: STOCKADE. [Pok. 2. (s)teg- 1014.]
```


## [2026-09-05T05:23:32.642Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK tata ===\"; grep -n \"lemma: tata\\|lemma: dhe-dh\\|lemma: dhēdh\\|Lallwort\" POK_full.txt | head -20"
}
```


### [2026-09-05T05:23:32.697Z] TOOL RESULT

```
=== POK tata ===
84715:Root / lemma: tata- teta- 
84738:verbreitete Lallwortgruppe.
```


## [2026-09-05T05:23:36.113Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ADOLPH\\|ALBERT\\|athal\\|adal\\|at-al\" AHD_watkins1985.txt | head -20; echo \"=== al- entries ===\"; grep -n \"^al-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T05:23:36.225Z] TOOL RESULT

```
300:[athal-. Race, family. Germanic root, possibly related to Greek atallein, to foster. 1. Germanic *athal- in Old English ztheling, prince: ATHELING. 2, Variant Germanic *6thel- in Old High German edili, noble: EDELWEIss. [In Pok. atos 71.]]
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
=== al- entries ===
278:al-'
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
```


## [2026-09-05T05:23:36.705Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '84715,84760p' POK_full.txt"
}
```


### [2026-09-05T05:23:36.765Z] TOOL RESULT

```
Root / lemma: tata- teta- 
Meaning: Daddy; expr. child word 

Material: Old Indie tata-la\her\ tata- 'father, son, Lieber'; gr. TeiTa (Hom.) Vok., Tara Vok. 
'o father!'; alb. /a/e 'father'; Latin /a/a 'father (in the baby talk); Ernahrer'; cymr. tad, corn, 
/a/'father', /7e/7-o'a/ 'grandfather'; Old Icelandic t^jazi^a giant ' {* t^eda-sal); Latvian teta, 
Lithuanian tetis, tete, /e/y/zs 'father'. Old Prussian //7e//s 'grandfather' (Old Prussian taws 
'father', //7eM//s'Vaterbruder', Lithuanian tevas, Latvian /e^es 'father'), Lithuanian teta 
'aunt', zemait. ////s 'father'; russ. tata etc. 'father', russ. -Church Slavic teta etc. 'aunt'. Old 
Church Slavic tetbka6s.; Modern High German Tate, East Frisian /a//e 'father'; Norwegian 
/aa/e'Lutschbeutel', isl. tata 6s., Norwegian Swedish /a//e'Frauenbrust, teat'; 



besides Germanic forms with /and u. Old Engiisli titt' nipple, Kuhzitze', Middle High 
German zitze "teat'; 

Maybe alb. s/se 'teat, breast' 

Swedish //l^a'aunt, old unverheiratete wife, woman'; Middle High German zutzel 
"Sauglappen', Swedish /y/Za'old wife, woman, Muhme', Old High German tutta, tuta^ 
nipple ' ; similarly gr. tutGo^, -ov 'small, noch totally young ', tutGov 'ein biftchen', inschr. 
also 'pp£cpo(;, nai5iov'; tuvv6(; small, little'; eine also out of the Indo Germanic Sprachen 
verbreitete Lallwortgruppe. 

References: WP. I 704, WH. II 650, Trautmann 320, Vasmer3, 81. 
Page(s): 1 056 

Root / lemma: taus- 

Meaning: still, silent, peaceful 

Material: Old Indie /i/syaZ/'beruhigt sich, is zufrieden', /i/5/a-'befriedigt, zufrieden', tusmm 

Adv. 'still, closemouthed ' (: Avestan tusni-. Old Prussian tusnan), Kaus. tosayati 

'beschwichtigt, stellt zufrieden, pleases '; Avestan /^s/7/- 'stillschweigend' {tusnisad- 'wer 

stillschweigend dasitzt'); 

Middle Irish td{*tauso) 'still, closemouthed ', Old Irish /z/ae 'silentium' (basic form 
*tausiaR), mcymr. /an/'schweige!', ncymr. /an/'Schweigen; closemouthed ', tawer 
closemouthed ', bret. /ao 'Schweigen; still!', abret. taguelguiliat(j\. to dem as 
'schweigendes Wachen' miftverstandenen Latin silicernium; guo-teguis 'compescuit', 
nbret. tever keep mum, keep quiet ';
```


## [2026-09-05T05:23:48.930Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^atto-\\|atto-, awo\" AHD_watkins1985.txt | head -3; echo \"=== IEC dhedh ===\"; grep -n \"dh[eēěė]dh\\|dhēdh\" IEC.txt | head -20"
}
```


### [2026-09-05T05:23:49.010Z] TOOL RESULT

```
301:atto-. Father (nursery word). Possibly Latin atta, father: ATAVISM. [In Pok. atos 71.]
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
=== IEC dhedh ===
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


## [2026-09-05T05:23:49.103Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==105' IEC.txt | head -60"
}
```


### [2026-09-05T05:23:50.640Z] TOOL RESULT

```
o; Cz. (ambig.) drdol "dot: Li. cf. dirdénu, -dénti ‘crawl, as traf- fic’. (For Arm. tartam ‘hesitant’, cf. Gk. tetra- maíno ‘tremble’, qua *títrém-)
drgl- (?) ‘fail, fal LG torkeln ‘tumble, stumble’; Big. cf. drágla ‘feeble woman, trollop’; drágla$ ‘weakling; jade (horsey; drágliv «lean, weak’. The Blg. forms are ambig. cf. dhrugh-.
drgh- ‘têar, pull, pluck’. Cf. dorgheið Ir. cf. driog ‘pang, pain’; Icel. torga ‘devour’; R. dérgat, nut ‘pluck, pull, pil’; Cz. drhnout ‘scour, scrub’, cf. drhlice, f. ‘pilling imple- ment: Li. dírginti ‘irritate’
drêh- ‘scrape, graze’. Cf. drgh- Oss. äv-därzín ‘wipe, graze’; Big. drázam ‘break (flax)'; dárzalka ‘hackle, flax-breaker’
drK- (radical) ‘see’. See derK-, dorK-, drks-. WP I, 806 & see next Skt. dr$, adj. ‘seeing’; dr$ih 'sight'; Olr. cf. drech (&aspect', fr. *drKs-); Ir. dreach, drioch, id.; W drych *mirror
drbh- (dorbh-) — drs-
10
15
20
25
30
35
40
45
164
drKmn- ‘aspect Gk. cf. (e-gde) dérgma “look, aspect; Br. dremm, W drem, id.
drKsos, à, ios “vision”. See derK-, dorkK-, drK-, etc. | Skt. -drksah (cpds. “-looking'); Olr. drech; Ir. dreach, drioch “aspect, appearance; W drych ‘mirror’; Per. cf. duruxsam “shine”
drktis “seeing, sight, brightness? Cf. derk-, dork-, drk- & WP I, 806 Skt. drstih; Av. (o-gde) darstis; Alb. dritë ‘light’; MIr. cf. drithle ‘flash’; OBr. cf. -drichet- ‘scope’; OHG zorcht, zoraht, adj. ‘bright; OS torht, id. OE torht (id. & *brightness")
drm- “sleep, drowse'. WP I, 821 Lat. dormio, ire; EMCz. cf. drmek (a sedative: *agnus castus")
drnos, is (drmn-, dorn-) (1) “piece, part. Cf. dero Delphic Gk. cf. dárma 'skin'; Br. Cor. W darn ‘piece’; LW in ONorm. darne, id. (fr. *dorn-); Du. cf. tornen “rip up, come unsewn'; Russ. dern, Blg. & OCS drán, drünü; Pol. dar: Cz. drn ‘clod, sod?
drnos (2) *harsh'. Cf. drs- Skt. dirnáh ‘desperate’; MIr. drenn ‘warlike’; OBr. cf. ar-dren, id. MHG (ambig.) zorn (*angry'. Cf. dusnós); OE torn ('cruel, bitter, oppressive’. Ambig. as MHG); Du. cf. tornen, v. ‘dun, press for payment’; Gk. cf. draíno *be strong, be prepared for
dro, ið (dor-) ‘skin, tan, téar. Cf. dero, dor- & WP I, 797 Skt. drnami, tr. intr. ‘burst, téar'; Av. cf. də- rota, pp. ‘cleft’; Gk. daíro, adj. dartós ‘flay, flog; MHG cf. pp. ge-zoren: E torn; OCS díro, dréti & diréti ‘plunder’; Cz. du dřít ‘scour, swot beside deru, drát ‘strip, pluck a fowl’; Li. diriu, dirti ‘skin’; Late cf. (freq.) diraju, diråt, id.
drpo, io ‘fling, rant, rage’. Cf. drbh- Skt. drpyami ‘set on fire; rage’; OE torfian ‘fling, shoot, stone, surge’; ge-tyrfan “strike, afflict; E cf. to turf out; Du. turven op, Fris. turvje op ‘hit, beat. (The Gmc. forms ambig. cf. drbh- and drubh-. Cf. also dhrbh-). Cf. OSw. tyrva, Sw. torva till ‘to pelt
drs- “hard, harsh; hardness, harshness'.
165
Skt. cf. drsad ‘rick, stone of mil; Av. doros ‘sorrow’; Du. torsen ‘endure, be weighed down’; OCz. drsati sé ‘defy’; Cz. drsný “harsh?
drtis ‘têaring, scraping; têar, skin’. See next & cf. WP I, 797: dero Skt. drtih ‘skin’; Per. dül *water-skin'; Gk. dársis ‘skinning; milling’; Go. ga-taürps “de- struction’; Cz. drť? ‘powder, sawdust’; R (al- leged) derť ‘bran’
drtos (1) ‘torn, flayed, cut, worn, ground’. Cf. drtis, dero, etc. Av. doroto (1) ‘cut, mown’; Gk. dartós, dra- tós *flayed'; Ir. cf. dartán ((clod', fr. *dort-); Pol. darty ‘split’; Big. dárt
```


## [2026-09-05T05:24:01.221Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nimport re\n# find offset of line 2728\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:2727])\nleaf=t[:off].count('\\f')\nprint('dhedh leaf(0-based ff count)=',leaf)\n# find tata entry\nfor i,l in enumerate(lines):\n    if re.match(r'^tat[aā]',l) or 'tata- ‘father' in l or \"tata ‘father\" in l:\n        print(i+1, l[:300])\nEOF"
}
```


### [2026-09-05T05:24:03.277Z] TOOL RESULT

```
dhedh leaf(0-based ff count)= 111
```


## [2026-09-05T05:24:09.357Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==112' IEC.txt | grep -n \"^1[0-9][0-9]$\\|17[0-9]\\|18[0-9]\" | head; echo \"--- context ---\"; awk 'BEGIN{RS=\"\\f\"} NR==112' IEC.txt | sed -n '1,10p' | cut -c1-200"
}
```


## [2026-09-05T05:24:10.636Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"tāta\\|^tata\\|tata, ‘\\|tata ‘dad\" IEC.txt | head -20; echo ===; grep -n \"‘daddy’\\|daddy\" IEC.txt | head -20"
}
```


### [2026-09-05T05:24:11.228Z] TOOL RESULT

```
21:178
33:179
--- context ---
 (?) talgen ‘knead’. (Cor. dalgh, m. dalghen, f. ‘hold, grip’ represents a formula *dhalghs-)
dhalio (dhaliio, dhales-) ‘fortune, produce, outcome”. Cf. dhalio
Gk. thalía, f. thálea, npl.; W daili, pl deilliau -
*próduce?; (?) OCz. dole ‘fortune, success’; R dolja ((2) ‘destiny’. In sense (1) see dal- ‘part, share’, as in OCS, but SI. forms are ambig.).
dhalið ‘come out, project, succeed’. WP I, 825. Alternative form: dhalno Gk. thállo ‘sprout, bloom’; Alb. dal ‘go out, come out
dhalos, is ‘bud, sprout, excrescence’. Cf. dhalio Gk. thálos, n.id.; Alb. e dalë “boil, blain'
dhálom, is (dhol-?) “mark, end, matter’ (?) See dhol- Ir. dáil (1) "matter, case, decision'; OFris. dól ‘aim’; Fris. & Du. doel, id. (Du. also “sense; boundary”. Cf. be-doelen, v. “in
dhám-, see dhom-
dhambos ‘dim, cloudy; dimness’. Cf. WP I, 824 & 851. Cf. dhmb- Arm. cf. damarim (‘get confused’. Ambig. cf. dhmb-); Gk. thambós, adj., thámbos, m. ‘dim; dimness’; OHG dampf; LG damp ‘s
dhámol-, see dhemol-, etc.
```


### [2026-09-05T05:24:11.322Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T05:24:15.134Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 699 700 701; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | grep -n \"^13[0-9][0-9]$\" ; done"
}
```


### [2026-09-05T05:24:16.706Z] TOOL RESULT

```
Exit code 1
=== leaf 699 ===
=== leaf 700 ===
=== leaf 701 ===
```


## [2026-09-05T05:24:19.626Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"tatta\\|tāt-\\|tat- ‘\\|tat-, \\|tati\" IEC.txt | sed -n '1,30p'; echo \"=== search 1369 ===\"; grep -n \"^1369$\\|^1368$\\|^1370$\" IEC.txt | head"
}
```


### [2026-09-05T05:24:21.267Z] TOOL RESULT

```
45:“As to many words which we have in common with the Germans, it is doubtful whether the old Teutons borrowed them from the Latins, or the Latins from the Teutons, or both had them from some common original”. The object of the present work is to indicate what words in the living or the dead languages of the Indo-European family appear to have a common origin, and to give them an acceptable prototype form. Equations are sometimes tentative, but they are based on the “sound-laws” that have proved their validity by the rational process of analogy, a mode of thought also present in the work of the Latin lexi- cographer Robert Ainsworth, who began his Latin dictionary in 1720, and who died in 1736.
46:The present Dictionary was begun tentatively in January 1925 before the appearance of Walde's and Pokorny's Indogermanisches Worterbuch (1927-32), but was set aside for a number of years because certain information was lacking to give it complete authenticity. The most acutely felt deficiencies were the absence of a full Albanian dictionary, made good by the author between 1939 and 1948; a full dictionary of Old Irish; the absence of a Welsh etymological dictionary; inadequate dictionaries of Lithuanian and Latvian; and a confused & inadequate understanding of, and exploitation of, the vocabulary of old and modern Armenian. Hittite, deciphered by the Czech Bedfich Hrozny in 1915, was unavail- able, as were the documents of Mycenaean in Linear B deciphered by M. Ventris, and ad- ded to by Bennett, Blegen and Mabel Lang. Tokharian became more fully available only with the publication of Van Windekens's Tokharian Etymological Dictionary of 1941, with additions in “Orbis” in 1968-70. Ossetic, believed to be the only surviving relic of ancient Scythian, became available with the publication of Vsevolod Müller's three-volume dictionary of 1927-34.
48:No prehistoric culture was possessed of a powerful political centre able to impose its norm over a large area, and it is therefore idle to search for a single Indo-European homeland for a culture that reflects both the animal husbandry of nomads and the agriculture of a static community, both of which are implied in the reconstructed language as presented herewith. This must therefore be regarded not as a beginning, but as an end-product, a language caught
51:My thanks are due to all previous lexicographers (“harmless drudges”) and etymologists who have unknowingly contributed to the material of this Dictionary, and who have served as a necessary corrective to a work whose only aim is to present a common denominator rather than a lost primitive speech. As an independent study, Indo-European linguistics can claim to be an exact, albeit empirical science, since it fulfils the three requisites of science, viz. collection, classification and interpretation. For such a science, absolute and final proof is probably unattainable, but if a relationship can, in terms of Euclid, be “de- monstrated" by an adequate amount of analogy, the result can be both probable and con- vincing. Historical linguistics is unique in being probably the only exact science that is linked exclusively to human behaviour. It stands or falls by the logic inherent within it, and does not depend op the dicta of any one scholar, dead or alive. In bringing this work to a close after 55 years of intense and unremitting labour, the author has tried to avoid the German fault of overloading etymologies with irrelevancies, the French fault of trim- ming the evidence to achieve a neat pattern, and the Anglo-Saxon fault of being content with approximations.
462:alo (1), alio ‘rear, breed, grow’. WP I, 86 Gk. cf. trog-aliá ‘crops’, phut-aliá ‘plantation’, beside aldo ‘feed’; Lat. alo, Gre cf. co-aleo, alesco; Olr. alim, Ir. alaim, ailim rear, foster’; W alu ‘bring forth”; Br. ala, id.; cf. Cor. els (stepson', fr. *alitos); Go. alan, aljan; ON ala; OE alan
801:augos, om, ios, io “growth, increase, rein- forcement'. Cf. augó, aueg- Tokh. cf. okar ‘plant; Lat. cf. augmen; OE eaca; ON auki beside aukan 'increase'; Latv. augs ‘growth, plant? beside audze ‘plantation; generation’. (Av. aogō, n. ‘help and Skt. ugráh “powerful? may belong here, but seem to be contradicted by Skt. ójas: Av. aojo, -áh- ‘power’ (*& or a secondary *g?) beside Av. aogo, -áh- *help")
905:(N.B. Words containing IE *-b- are far fewer than those with IE *-bh-. A degree of am- biguity arises with alleged cognates from Iranian, Albanian, Celtic, Baltic and Slavon- ic, and especially with citations from Hit- tite and Tokharian, where (initial) *p, *b and *bh are represented similarly).
928:belbetióo, belbotio, see bolbotió Cz. cf. blebtati, Srb. blebetati ‘twaddle’
933:bobotió “bubble; prate’. Cf. bəbədið, etc. Arm. papačem ‘bubble’; Br. (ambig.) babaza (‘twaddle’. Cf. bəbad-); Blg. bobótja ‘rumble’; Srb. boboćem, bobotati ‘shiver’.
938:pypčam, -čem “bubble, babble’ (fr. *bulbu- dio); Lat. balbütire; Br. balbuza 'stammer, twaddle; OCz. blabcu, blabtati beside blbotati; cf. Li. balbatuóju
1335:bhit- ‘bee’. WP II, 185 Hind. cf. bhir ‘wasp’; Arm. cf. bčič (a-st. ‘honey-cell’, fr. *bhit-itio (?)); Ir. cf. beath- mhan, beathóg (allegedly = ‘bee’ — Lane, but of uncertain documentation), W cf. byd-af (‘hive of wild bees’, fr. *bhitəma); Li. bitis, f. and bite ‘bee’; Latv. bite, id.
1337:bhladó (?) ‘make a ritual pronouncement’ Lat. (?) cf. flamen (“high priest’. Link w. Skt. brahmáà still maintained tentatively by Meil- let-Vendryes and M. Müller. See bleghó); W (?) blawdd “active, ready; OW blawó ‘tumulť are ambig. cf. bhldh-; OHG bluozan, OE blotan, sv. 7 ‘sacrifice’; ON blóta *wor- ship, curse, swear’; (Li. blódziu, blódeti *blight, sour by overgrazing’ seems to be un- related). Cf. OE blot ‘sacrifice; ON blót ‘curse’; blæti ‘idot
1433:(bhlüst- variant, cf. bhluskos, bhluks-) Srb. blistati ‘shine’, blistav ‘shining’; Li. blüscioti ‘gutter, sputter as candle’
1679:bhronghes, à (2) ‘swollen; swelling’. Cf. bronsghos NAIb brángé, Alb. brengë (2) ‘tumour, esp. in cattle; ulcer; MHG branc, gs. -ges *boast- ing; brenge ‘ostentation’; cf. brangen, V., (Upper) Ger. prangen “boast'; Icel. braggast ‘thrive’; Latv. cf. brangs ‘luxuriant, fat. (A variant *bhrong- occurs in Scots branks ‘mumps’). See next. (Alb. brángé, brengë are ambiguous, cf. brongh-)
1994:bhütolos (bhütlos), om, à, io “life, growth, dwelling’. Cf. bhū- Gk. phūtalià ‘plantation’; phútle ‘generation’; Alb. cf. bitojé ‘sapling’; Li. büklas, a ‘dwelling- place; bükle “position” beside büklüs 'cus- tomary'
2278:diKos, iom, à ‘manifestation’. Cf. deik-, diK- etc. WP I, 776 Skt. dis, disa; Av. disyəm ‘teaching’; Gk. díkë ‘custom, right’; W cf. go-ddeg Cutter: ance’, fr. *upo- ?); MHG zic, gs ziges (oxy- tonic: *diKós «accusation"); ON tigi, n. id.
2593:dupso, ið ‘trample, beat, thresh’ Arm. tpem “beat; scutch'; Sw. tofsa, tufsa ‘lug, touse’; OCz. & Cz. depsati ‘tread, trample, plod’; OCz. cf. also deptati, Isg depcu: Pol. deptać, id.
2784:dhémn- “setting, fixture, form, shape, sub- stance’. WP I, 828. Cf. dheio (2) *dhemen-, *dhemn- in Gk. thé- ma, cf. also thémis: Myc. temi- “Justice? and Hes. thémeros “firm, stationary'; Lat. femen, gs -inis & femur, gs femoris & feminoris (*thigh': Cz. dymé, gs demene ‘groin’, beside Lat. femin-àlia *drawers"); Ir. damhna 'substan- ce; cause’; W defn ‘substance, material’ beside defnydd, pl. iau (elemen? fr. *dhemniio-); MHG tinne (‘forehead’; pl. ‘temples’); Swiss Tenn ‘main room in hut’; G Tenne ‘threshing- floor’; *dhemn-, *dhēmō(n) in Skt. dhàman ‘fixed abode, reaim, place, common-law, rule, pleasure’; Av. dama, obl. daman- ‘creature’; Gk. théma ‘tomb’, themón ‘heap’; Li. démé “mark, note’; demuó, eps “item, theme, com- ponent, datum’. Cf. further dhomn-. (Av. dax- məm ‘repository for bones’ seems to represent a type *dhesmom. Cf. dhesno-. For Ir. deimh- in ‘certainty’ see above: dhémen-)
2927:dhià, dhiam- (extn. of dhi-, q. v.) ‘sign, mark, note’ Skt. dhyami ‘think’; dhya ‘meditation’; dhya- nam “thought”, cf. also dhyåmab "dark black’; Gk. séma, Dor. -ā- ‘sign, device, landmark. (For Cz. z-dieti sé, z-dát se see deio (2))
3136:dhrugh- (1) ‘tremble, waver, shudder’ Ir. cf. drogall ‘shyness’; OCS drüZg, ati and drúgajo, ati ‘tremble’; OCz. držěti, dřežeti, id.; Pol. drgac, Cz. drhat ‘shudder, twitch’; R drožàť, id.; cf. OCz. drhy ‘tremors’; R droži, Pol. dreszcz, id. & Slovene drgetati ‘tremble’; Li. drugýs ‘fever, tremors’; Latvian drudzis, id. Å
3759:(Initial IE *ə- is of uncertain documentation. It is often indistinguishable from initial a-, q.v. and cf. also initial i-. In general, Lat. Gk. -a-: Skt. -i-: IE *o, but Lat. Gk. -i-: Skt. -a-: IE *í, the so-called shva secundum. There are some unexplained initials in u-).
3775:-euó, -euuó (1) frequentative verbal extn. Gk. théreuo "bunt": nuktereúo ‘spend the night; OCS lénujo, -ovati ‘lounge’; Li. Svil- pauju, -auti ‘keep on whistling’. Cf. also Cz. u-bytuji (lodge, quarter’: Gk. phüteuo *plant")
3866:gagətið (gogotio) cf. gagodio, gagó, gagol- Arm. kakacem ‘cackle’; Cor. gesya “mock, jeer’; (MHG cf. kachezen, OE ceahhetan, E chat, fr. *gagodio); OCz. hohcu, hohtati ‘cackle’; R gogotàt, id.; gógot, m. id.
3997:gígémo ‘squeeze, grasp’. Cf. gemó Arm. Czmem, id.; Gk. aor. mp. génto ‘he grasped'; OCS Zen 1sg. Zímo; R žať, Zmu; Cz. cf. also (frequentative) Zdímat ‘squeeze’
4134:glondhos ‘unpleasant; nausea, annoyance’. Cf. WP I, 617 Ir. glonn ‘nausea’; ON Kand ‘molestation’; G Klant ‘bad news’; cf. also ON klandr ‘molestation’; Icel. klandur ‘abuse’, klandra v. id.; Sw. klander “abuse”, klandra as Icel.
4168:glüt- (1) ‘guip, swallow’; gluto(n), glutən- ‘gullet Oss. qürtt ‘gulp’; Lat. glutio, ire, v.; gluto, gs.-onis ‘glutton’; gluttus ‘gullet, foodpipe'; Ir. glota, gs. glotan ‘gullet’; cf. glothar ‘gurgle’; Gaelic glut ‘voracity’; glutair ‘glutton’; Br. glut ‘gluttonous; glutton'; OCS glüsto, glütiti “swallow? (= Lat. glutio); Cz. hlt ‘gulp’; hitan, hltoii ‘glutton’; Slovene gólt, m. ‘gullet’; Ukr. (*-ū-) hlytaty (devour ; Cz. hltati, id.);
4438:grt- ‘gather, assemble’ Hes. cf. á-garris (for á-garsis ‘meeting’, fr. ageíro); Srb. græem, grtati ‘gather’; ginuti, id.; Cz. hrnout; Pol. garnać: Ukr. pri-hornuty, id. (Gk. px. fr. *sm-, q.v.) (Slav. perfectives fr. *grt-n-)
5040:ghrt- ‘thrus? (?), ‘coerce’ (?). (Variant *ghrst-?) Arm. gahem (strike, thrust’, phon. of mah ‘death’, fr. *mrt-); Lat. (?) hortor, ari (urge on”, beside a variant (?) hostio, ire ‘strike’ of type *ehrst-, cf. hostorium *strickle'; hostia “vic- tim’; Srb. (?) cf. grčem, grtati ‘scrape together”. Obscure; possibly two roots, and for Srb. cf. Lat. co-hors, -hortis
5255:gulen- (expressive variant: gulenn-) ‘mucus, slime’. WP II, 288. Cf. glinos Gk. blénna, id. (expr. as in Hes. glítton, Lat. lippus, Gk. tatta, etc.); MIr. blinn *gpittle'". (MHG kl&n- cpds. ‘daub’, kl&nen, v. id. ambig. cf. glin-. OCS glénü ‘mucus’ represents a type *egloin-)
5416:gurgot- (gurgot-) “neck, throat, gullet’. WP I, 683 Per. gulü; Oss. qür ‘throat’; qürtt ‘gulp’; Arm. cf. kokord, i, av, a-st. ‘throat, gullet; Lat. gur- ges, gs -itis ‘whirlpool, glutton’; OI gorgozza *windpipe, throat' beside gargata, gargozza, id.; Mir bráge, gs brágat, beside bráighe, gs bráighid ‘throat’; Mod. Ir. brágha & brághad, pl. bráighde, id.; W cf. breuant, brefant *wind- pipe; OBr. brouant, id.; Cor. cf. breiansen, bryonsen ‘throat’; Srb. cf. grgocem, grgotati *gargle'. See next
=== search 1369 ===
18214:1368
18224:1369
18242:1370
```


## [2026-09-05T05:24:23.787Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '18200,18245p' IEC.txt | cut -c1-400"
}
```


### [2026-09-05T05:24:23.883Z] TOOL RESULT

```
-tálos, agent-suffix in Gk. aró-tes, m. *plowman'; OCS ra-taj, id.; Li. artojas, id.
tak- ‘silent; silence’. WP I, 703 Lat. taceo, ere, v. ‘be silent’; Ir. cf. tachtaim, v. ‘choke’; W tagu, inf. tr. ‘choke’; Cor. taga, inf. tegys, pp. id.; Go. bahan E pagon, inf. ‘be silent; OHG dagen, id.; cf. MHG ge- degen, tr. ‘quieten’; be-dagen, id.; ON pegja, inf. ‘be silent”; bogn, f. ‘silence’
tākā “ground, earth’. Cf. tēkā (5). (Iran. & Alb. ambig.) Pahi. tak, s. ‘ground, bottom’; (LW in) Arm. tak, i, av, id. (and 'arse?); Hitt. cf. takan, adv. ‘to the ground’; Alb. (ambig.) tokë, f. “earth, Soil; Lat. cf. (?) -tax, gs: -tacis in for-tax, f. (“floor of furnace’. Cf. guhor-)
tako, aio ‘touch, hit” (?). Cf. tuk-. Evidence ambig. For Alb. takoj, tokoj, v. “hit, meet? as LWs, cf. It. at-taccare, s-taccare: Fr. at-tacher, dé- tacher for *-á-, and It. toccare, for *-u-; Cor. takya, inf. ‘clap — the hands’; tak, pl. taccow, m. ‘clap’. For Srb. taknem, inf: taknuti, v. ‘touch’, qua OCS tüknoti, see tuk- below
GL (1) ‘so, so much, so many; such’. Cf. təl- & tl- (2). WP I, 743 Gk. cf. tél-íkos, adj. ‘so big’; Lat. talis, adj. ‘such’; OCS tali, gs: -i, m. ‘pledge, hostage’; cf. talinü, m. (a measure’; (variant of type *tol-): OCS toli, adv. ‘so’; R ‘so many’
tāl- (2) “separate, distant Hitt. cf. dāliya(mi), v. and talā(hi), v. ‘leave, let; W toli, inf., tawl, 3sg. ‘divide, cut’; be- side tolli, inf. ‘take away’; Cz. cf. o-tálet, inf. ‘dally, delay; remove’; cf. also talácet, inf. ‘wander’; Li. toli, adv. ‘far’; tolüs, adj. ‘dis- tant”; Latv. tāli, tālu, adv. ‘far’; tals, adj. ‘dis- tant’. (NB. For Gk. tēle-
tāl- (3) ʻooze, flow; tāləuos ‘seepage, pus, matter’. Cf. taið (1) Ir. tálaim, v. “drip, pour, flow’; tál, pl: táil, m. (2) ‘flow, milk-yield'; OCS talü, adj. ‘liquid’; Slovene taliti, inf. “melt, dissolve’; Srb. cf. talog, m. ‘sediment. Extn. in Oss. táläw, s. ‘carbuncle’; Cz. talov, m. ‘pus’; R talyj, adj. ‘thawed, melted’
-tàios — tap-
20
25
30
35
40
45
1368
tal- (4) (tālis, os, iə) “cutting, new growth, shoot, branch’. WP I, 705 Skt. talah, m. & talih, f. *palm-tree"; cf. talikà, f. ‘palm of hand’; Oss. tála, s. ‘shoot, sapling’: Gk. Aeolic tális, gs: -idos, f. (young woman’. Semantics of Lat. virga: virgō; Cz. hůl: holka; Ir. géag ‘branch’ & ‘young woman’; E slip, id. id.); cf. further (?) télis, gs: -eos, f. ‘fenu- 
. layer, graft; W tawl, pl. tolion, m. (2) ‘cutting,
lopping’; OCS talija, f., talije, n. ‘green growth, branchiness'; R (alleged) tal, m. ‘salix cinerea’
tal- (5) Skt. cf. talakah, m. ‘ʻa poisonous insect; Ukr. cf. po-tàla, f. ‘ruin, destruction?
tálikos ‘such’. Cf. tal- (1) and tol-, tl- (2). WP I, 743 Gk. telíkos "of such size or age: OCS, Cz. tolikü, tolik ‘so much, so many’. (Isophone: R talíka “skein, hank': Li. tolika, id.)
talið “cut off, separate’. Cf. tal- (2) MW toli, 3sg: tawl, v. ‘cut off; Mir. cf. tallaim, v. ‘cut’; Lat. talið, are, v. ‘cut, split’; Cz. tálet, inf. ‘separate’; Latv. cf. at-talinat, inf. 're- move’; Li. tolstu, tolti, inf. ‘depart
tàm- (1) ‘quieten; expire; silence; expiry’ Skt. tàmyami, pp: tantah, v. “grow faint, ex- pire’; Av. tam-, v. ‘wane, stifle, expire’; Olr. támaim, p.t: tathaim, redup. ‘expire’; tám, m. ‘death-coma’ beside táim, s. ‘expire, collapse’; Ir. támhaim, v. ‘languish, expire’; támh, f. ‘trance, expiry’; táimhe, adj. ‘still, dead’; tá- mar, m. ‘death’; R ta
tām- (2) ‘swell, distend' Lat. tama, f. ‘swelling of feet; W tofi, inf., tawf, 3sg. 'distend'. (Hybridism may be pre- sent in Lat. con-tàminàre ‘contaminate’, cf. tabh-?). (Isophone in Latv. tameju, v. “intend: tame, f. “plan, proposal)
tap- “press, tread, trample'. WP I, 705 Skt. cf. vi-, sam-tapami, v. ‘press’; Gk. cf. tapei- nós, adj. (humble, lit. *downtrodden'?)); ON pefja, v. ‘stamp’; þóf, n. 'crowd^; R tópat, topnut, v. ‘trample’; Srb. cf. topotati, inf. “pad, plod'; R topotnjà, f. ‘stamping, pawing’; Li.
1369
cf. tapšnoti, inf. ‘tap, clap, slap”
tap- ‘plod, lumber, totter, fumble’ ON beta, v. lumber along, stumble along”; -st, refi. ‘bicker’; boefa (w. til ... “struggle for’); Cz. tápu, tápat, v. ‘fumble, grope’
-tár-, agent-suffix in Oss. cf. mud-tár, míd-tar (‘beekeeper’, fr. *medhu-"); Gk. cf. gene-tér ‘parent’; op-tér, gs: -téros, m. ‘surveyor’; Av. (short vowel) zao-tar, m. ‘priest’; Alb. der-tar, m. ‘doorman’; krye-tar “chief”; Cz. novo-táf, m. ('innovator'; cf. Lat. novà-tor, id.)
tat- (1) (tatis) ‘secrecy, theft; thief". Cf. Gig (2) and tàios. WP IL, 610 Olr. táid, m. ‘thief; táide, f. ‘secrecy; theft’; táidim, v. ‘steal’; OCS tati, m., Slovene tat, m. ‘thief’. (NB. For Gk. tétē, tetáo, see quāt-)
-tāt- (2) (theme of abstracta) Gk. cf. neó-tēs, gs: -tētos (Doric: -tāt-); orthó- tēs, barú-tēs, etc.; Lat. novi-tās, gs -tātis, gravi- tas, etc.; W drew-dod, m. ‘stench’ beside drew m. id. (but the Welsh LW trindod ‘trinity’ is fem.)
tāt- (3) ‘molten; melting, liquescence’. Cf. taio (1) and WP II, 19 Av. táto, adj. “liquescent, flowing’; Olr. táth, m. ‘soldering’; Ir. id.; Cz. tát, pp. ‘molten’
tăt- (4) (tàtà) ‘daddy’. WP I, 704 Skt. tatah, m. id.; Arm. tat, id. (and *'ancestor); Hiero-Hitt. tatai, dat. sg. id.; Alb. tatë, def: tata, id. beside Sic-Alb. tot, m. *grandpa'; Lat. tata, It. tata, m. ‘father’; Ir. tath, m. ‘chief’; OBr. -dat, cpd. ‘daddy’; Br. tat, tad, m. ‘father’; W tâd, pl. tadau, id. beside taid, pl. teidiau, m. (grandfather, fr. *tatjo-); Cor. ta
tatis ‘thief, see tat- (1)
taulo, ið ‘how!’ (?) (Evidence ambig.) Alb. tall, tállem, v. ‘mock, jeer’; Srb. tulim, iti, v. ‘howl’
táuros (tour-, teur-) “bull, bison". WP I, 711 Hiero-Hitt. cf. Tarawas “god of the weather’; Scyth. cf. tarandus (a fictitious monster); Myc. & Gk. taüros, m. ‘bull’; Alb. cf. tar-ak, tarok, m. dim. *bullock, steer'; Lat. taurus, gs: -1, m. ‘bull’; Osc. taurom, acc. id.; Umb. turuf, acc. pl. id.; Olr. tarb, Ir. tarbh, m. id.; W tarw,
tāp- — tebh-, us
20
25
30
35
40
45
1370
pl. teirw, m. id.; Br. tarw, pl: tirvi, id.; Cor. tarow, pl. terewy, id.; OCS (and common SI.) turü, m. ‘bison’; Li. taüras, m. id.; (LW in) Finn. tarvas *roedeer'; (variant in) ON pjórr, m. ‘bull’; Sw. tjur, m. id. Adjectival form of type táurelos in Gk. taüreios, taüreos; Lat. taureus *bull's'; Cz. oft *bison's'. (Isophones: Li. tauré, f. ‘cup’; taurüs ‘noble’; Late, taur
tàuió (1) “melt, dissolve’. Variant of type tàio (1), q.v. OS thóian, v. ‘thaw, digest; MHG douwen, dóuwen, v. “digest, consume'; OE pawian v. ‘thaw’ Du. dooien, id.; dooi, m. id.; ON beyja, v. id.; beyr, pl. peyir, m. id.; Sw. (oa, v. id.; Cz. tavit, inf. ‘melt, smelt’
tauiü (2) “silence; be silent". Variant tauuió W tewi, inf., taw, 3sg. "be silent’; ON þagga, v. ‘silence’
```


## [2026-09-05T05:24:33.264Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 leaf 53 (p.44) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==53' incoming/WLD/WLD_Bd1_pages.txt | head -40 | cut -c1-300"
}
```


## [2026-09-05T05:24:33.910Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN leaf 118 (p.94) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==118' SYN.txt | head -50 | cut -c1-300"
}
```


### [2026-09-05T05:24:34.964Z] TOOL RESULT

```
=== WLD Bd1 leaf 53 (p.44) ===
44                                    *ati-, ateli-, -o             ad


  Die arm. Ablativendung -e aus nachgesetztem            (Bugge KZ. 32,
75, Pedersen KZ. 38, 224; 39,438). Kein Yertrauen habe ich zu Peder-
sens KZ. 38, 421 ErschlieBung einer Schwundstufe *ti aus aksl. lb- zb „emb-
vv[iog“.


*ati-, ateli-, -o-      Fischname?
     Gr. irsllg „Goldbrassen“         (kann aus *dr elk assimiliert sein), lat. attilns
„ein storiihnlicher groBer Fiseh im           Po“ (wohl gall, oder ligur.: Holder
Alteelt     Spracbsch.   s.   v.;   Zw. bei             Hirfc    IF. 37, 222);      alit.   nt'is,   lit.   otas
„Steinbutte“.       Z B. Yanicek LEWb. 2 11.

atta Lallwort „Yater, Mutter“.
  ai. atta „Mutter, altere Sehwester“, atti-li „altere Schwester“, gr. arret

„Yaterchen“, lat. atta „Vater; Kosewort der Kinder dem Yater gegeniiber“,
got. atta „Yater“, anord. atte ds., ahd. aito „Yater, Yorfahr“(tt durch stets
danebenlaufende Neuschdpfung unverschoben), aksl. otbtb ( *attikos) „Yater“;
Curtius 5 207; aber mir. aite „Pfiegevater“ steht wegen des cl von nir. oide
abseits (s. Zupitza KZ. 36, 243); alb. at „Yater‘    (G. Meyer BB. 8, 187,
                                                                            !




Alb. Wb. 20).
   Ein ahnliches *ato-s, germ. *apala-, *opela- „vaterliches“ scheint nach
Schrader IA. 9, 172, RL. 815 auch die Grundlage von ahd. adal „Geschlecht“,
nhd. Add, as. athali, ags. cedelii n. pi. „edle Abkunft“, anord. adal „An-
lage, GeschlechY, Adj. ahd. edili, as. ethili, ags. cedele ,.adelig, edel ‘, dehn-                   :




stufig    ahd. nodal,    as. othil, ags. edel anord. tided „(vaterliches) Erbgut"
                                                          ,
```


### [2026-09-05T05:24:36.575Z] TOOL RESULT

```
=== SYN leaf 118 (p.94) ===
. féta ‘pregnant, newly delivered’, with shift of application to ‘one capable of childbearing’, as REW 3269, Puscariu 588, Tiktin s.v.).
3. Ir. mace ‘boy’ and ‘son’ (NIr. mac, W., Br. mab ‘son’), see under ‘son’ (2.41),
NIr. buachaill ‘boy, servant, cow- herd’, fr. MIr. buachaill ‘cowherd’, like W. bugail ‘cowherd’, Corn. bugel ‘herds- man, shepherd’, Br. bugel ‘child’: Grk. Bouxédos ‘cowherd’. Walde-P. 1.696. Pedersen 1.54. Henry 47.
W. bachgen, cpd. of bach ‘little’ and cen of cenau ‘offspring’ : Ir. cinim ‘spring from’, cenél ‘race’, etc. Pedersen 2.33.
W. hogyn, prob. new masc. to hogen ‘girl’ (2.26).
Br. paotr ‘boy, valet’, MBr. pautr, loanword through OFr. fr. Gme. Cf. OFr. pautraille ‘canaille’, orig. ‘pack of ragamuffins’, LG palirig ‘ragged’, NE paliry, dial. palt ‘rubbish’, Dan. pjalt ‘rag’, etc. Henry 217. Falk-Torp 831.
4. Goth. magus ‘boy’, ON mogr ‘boy, son, man’, OF magu ‘son, servant, young man’, with derivs. for ‘girl’, Goth. mawt (magaps ‘virgin’), ON m@r, OE megep, megden, ME, NE maiden, maid, Du. meisje (dim. of meid, dial. form of maagd, Franck-v. W. s.v. meid), OHG magad, MHG maget, NH
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 89
ah ith a common notion married! oO z ae perh. fr. the same f ‘young person. ’ ; ony ‘can’, mahts ‘strength, tas Goth. mag ’ me nt’, NE might, etc. Walde-P. 2.228. Falk Torp 748. Feist 339. nee
ON pilir ‘boy’, Dan., Sw. poll sma boy’, orig. dub., but perh. (cf. Br. pam, above, 3) : SW: palt, Dan. pjalt rag’, Sw. dial. pult ‘bit of wood’, orig. some- thing broken off. Johansson, KZ 36.377. Cf, NE runt, orig. ‘stump’ now applied to a small person, a litile runt.
Dan. dreng : Sw. dréng ‘servant’, ON drengr ‘youth, brave man’, drangr ‘rock pillar’, ChSl. drag ‘beam’. Cf. NHG bengel ‘cudgel’ applied to a child, der kleine bengel. Falk-Torp 154. Johans- son, KZ 36.374.
Norw. gui (vs. Dan. dreng) = Du. guit ‘rogue’ : Norw. dial. gauta ‘prate, chat- ter’, MDu. guiten ‘make fun of’, etc. Falk-Torp 362. Torp, Nynorsk 191.
Sw. gosse : Norw. gosse ‘strong fellow’ and ‘boar’, NE dial. gussze ‘swine, pig’, etc., a collog. word of the most diverse applications. Bjérkman, IF 30.252 ff. Hellquist 294.
Sw. pojke, fr. Finn. poika ‘boy’, Hell- quist 774.
OE cnapa, cnafa, ME knave ‘boy, ser- vant’ (NE knave ‘rascal’), Du. knaap, OHG knabo, MHG, NHG knabe (also OHG knappe ‘boy, youth’, NHG knappe ‘Bage’) : ON knappr ‘knob’, OE cnep top’, Sw. dial. knabb ‘peg, knob, small thick-set person or animal’. Falk~Torp 543, 544. Johans
might), OHG, MHG kneht ‘boy, sotvant’ (NHG knecht) : ME, LG knagge Heke, Wood, Mod. Ph. 2.474. ausen, KZ 47.307. Falk-Torp
1498 f. Walde-P. 1.580. a = ate E. Pris. bot ‘boy’, prob. : » Vu. doef ‘knave, rogue’, NHG
bube ‘knave, servant’, dial. ‘boy’, orig. a nursery word like NE baby, ete. NED s.v. Weigand-H. 1.298.
ME ladde, NE lad, etym. dub., but perh., as orig. ‘attendant’, fr. the pass. pple. of
```


## [2026-09-05T05:24:43.977Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==53' incoming/WLD/WLD_Bd1_pages.txt | sed -n '40,80p' | cut -c1-300"
}
```


## [2026-09-05T05:24:45.547Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 122 123 124; do echo \"=== SYN leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | grep -n \"FATHER\\|MANKIND.*9[0-9]\\|2\\.3\" | head -5; done"
}
```


### [2026-09-05T05:24:46.013Z] TOOL RESULT

```
(vgl.    aucli   ahd. fater-nodal, as. fadcr-ddil „patrimonium“; s. noch Falk-
Torp   s. v. Adel 11 und 1413, und Odd 787 und 1524; daB auch got. hai-
 mopli n. „Erbgut“ unser Wort en halte, bezweifelt kaum mit Recht Feist
 Got. Wb. 120 wegen ahd. Iieimoti neben heimoclie ); vgl. mit derselben Yokal-
lange ahd. Lota (eigentlich „UrgroBmutter“), afries. edila „UrgroBvater“.
[Ungliicklich iiber Uodal usw. Grienberger 104; s. dagegen auch Uhlen-
beck PBrB. 30, 286.] Nach Justi IA. 17, 1 09 f. hierher vermutlich auch
av. adu-ya- „Name des Yaters dractaona' s“ als „von adeliger AbkunftY
   Erwagensvvert ist Zugehorigkeit auch von gr. dialog ,.jugendlich, kind-
lich“, drallco „ziehe auf, warte und pflege“ und ..springe munter wie ein
Kind“, red. unrulier „ziehc auf (Redupl. unter EinfluB von rith)vi] „Amine“ ?),
                                           -
                                               ‘



s. Zimmermann KZ. 34, 584f.     35, 6 1 3 f. (andere Beurteilungen s. bei Prell-
                                       ;


witz 2 61, Boisacq 94).
   Ein auf den verschiedensten Sprachgebieten sich stets neu bildendes
Lalhvort (z. B. magy. atya „Yater“, tiirk. ata, bask, a Ha ds.). Ahnlich tat a.

ad „zu, bei, an“.
  Phryg. (Ramsay KZ. 28, 385) ad-day.sr, ap-fteQer lat. ad ,,zu, bei, an‘‘,     :




Praeverb und Praep. m. Acc., auch Gen. des Bereiches, atq tie, ac „und
dazu, und auch, und“           ('   ud-qne         ;
                                                       kaum     at-\-quc;       ebenso umbr. ap „ubi,
quum“ zeitlich, um       -7   erweitert ape), umbr. af- Praeverb, -ar Postposition
m. Acc., osk.  aclpiid „quoad“, sonst mit s-Erw. osk. as „ad“ Praep. m.
Acc.; air. ad- Praeverb (z. B. ad-gladur „appello“, eymr. add-, gall, cid-
Praefix (z. B. Ad-ltdns), abrit. Ad-minius (Fick II 4 9); mit g(A)-Erw. wahr-
```


### [2026-09-05T05:24:47.520Z] TOOL RESULT

```
=== SYN leaf 122 ===
25:MANKIND: SEX, AGH, FAMILY RELATIONSHIP 93
=== SYN leaf 123 ===
5:2.31 ff. WORDS FOR FAMILY RELATIONSHIP
=== SYN leaf 124 ===
11:4, nana, anna, etc. Walde-P. 1.55; 2.317. Skt. nand- ‘mother’, Grk. vavva ‘aunt’, vévvos ‘uncle’, It. nonna ‘grand- mother’, etc., Grk. avvis ‘grandmother’, Lat. anus ‘old woman’, OHG ano ‘grand- father’, ana ‘grandmother’, OPruss. ane ‘grandmother’, Lith. anyta ‘husband’s mother’. NG ypdavva ‘mother’, blend with forms like those in 3, above.
```


## [2026-09-05T05:24:52.569Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==123' SYN.txt | cut -c1-600"
}
```


### [2026-09-05T05:24:54.296Z] TOOL RESULT

```
ps of cognates pointing to specific words for these rela- tions existing in the parent speech. The most widespread are those which are represented by NE father, mother, son, daughter, brother, sister. Others for which there is sufficient agreement to indicate IE origin are words for ‘grand- son’ or ‘nephew’, for ‘paternal uncle’, and, in relationship by marriage, those for the ‘daughter-in-law’ and for her husband’s father, mother, brother, or sister, or even her husband’s brother’s wife. That is, the IE family was ob- viously not matriarchal. The wife be- came one of her
| the that : 6 er, either by extension of | ae group or otherwise. _1 or ‘husband’ and ‘wife’ there is great | divergence in the actual words, b | siderable apr Sy oaM Cons for ¢ : éreement in employing words man’ and ‘woman’, or, to as | , some ex | tent, words for ‘master’ al (os ; | Probably Ae eee an Mistress : € situation in the
of neg. ne-, nie- and Boh. mluvitz, Pol. mowié ‘speak’, prob. lit. formations in imitation of Lat. infans.
7. Skt. (beside bala, etc., 2.25) ¢gigu- ‘child, infant, fetus, young of an ani- mal’, orig. prob. ‘fetus’: Skt. ¢va- ‘swell’.
2.31 ff. WORDS FOR FAMILY RELATIONSHIP
parent speech. Words for ‘marry’ and ‘marriage’ are from the most diverse sources, and there is no group of cognates that can be certainly taken as reflecting an IE word for ‘marry’. Yet, of course, even from the other linguistic evidence, the existence of the institution in the IE period is apparent.
In the inherited group the suffix -ter- or in some cases -er-, -or-, is conspicuous (cf. Skt. pitar-, matar-, bhratar-, duhitar-, jamatar-, yatar-; devar-, svasar-). Owing to the well-known use of this suffix in agent-nouns, these words of relationship were also formerly interpreted as agent- nouns from certain roots, e.g. ‘father’ as ‘protector’, ‘mother’ as ‘measurer, thoughtful one’, or the like, ‘brother’ as ‘supporter’, ‘daughter’ as ‘milker’, either the ‘suckling’ or the ‘milkmaid’, etc. Most of these derivations now seem fan- ciful and pointless a
The actual root connection and ulti- mate meaning of these inherited words of relationship is mostly obscure. But those represented by Lat. pater, mater are probably based upon the intrinsical-
ee CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
94
ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such i
```


## [2026-09-05T05:24:58.897Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==123' SYN.txt | tail -c 2500"
}
```


### [2026-09-05T05:25:00.728Z] TOOL RESULT

```
��, etc.
| the that : 6 er, either by extension of | ae group or otherwise. _1 or ‘husband’ and ‘wife’ there is great | divergence in the actual words, b | siderable apr Sy oaM Cons for ¢ : éreement in employing words man’ and ‘woman’, or, to as | , some ex | tent, words for ‘master’ al (os ; | Probably Ae eee an Mistress : € situation in the
of neg. ne-, nie- and Boh. mluvitz, Pol. mowié ‘speak’, prob. lit. formations in imitation of Lat. infans.
7. Skt. (beside bala, etc., 2.25) ¢gigu- ‘child, infant, fetus, young of an ani- mal’, orig. prob. ‘fetus’: Skt. ¢va- ‘swell’.
2.31 ff. WORDS FOR FAMILY RELATIONSHIP
parent speech. Words for ‘marry’ and ‘marriage’ are from the most diverse sources, and there is no group of cognates that can be certainly taken as reflecting an IE word for ‘marry’. Yet, of course, even from the other linguistic evidence, the existence of the institution in the IE period is apparent.
In the inherited group the suffix -ter- or in some cases -er-, -or-, is conspicuous (cf. Skt. pitar-, matar-, bhratar-, duhitar-, jamatar-, yatar-; devar-, svasar-). Owing to the well-known use of this suffix in agent-nouns, these words of relationship were also formerly interpreted as agent- nouns from certain roots, e.g. ‘father’ as ‘protector’, ‘mother’ as ‘measurer, thoughtful one’, or the like, ‘brother’ as ‘supporter’, ‘daughter’ as ‘milker’, either the ‘suckling’ or the ‘milkmaid’, etc. Most of these derivations now seem fan- ciful and pointless and are generally given up. The use of the suffix is not to be connected directly with its use in agent-nouns, but rather with the use of -tero- (-ero) in words of contrasted rela- tionship, like Lat. dexter vs. sinister, nos- ter vs. vester, etc., that is, it was used in words for ‘father’ and ‘mother’, etc. as contrasted terms. Cf. Streitberg, IF 35.196.
The actual root connection and ulti- mate meaning of these inherited words of relationship is mostly obscure. But those represented by Lat. pater, mater are probably based upon the intrinsical-
ee CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
94
ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such i
```


## [2026-09-05T05:25:03.160Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==124' SYN.txt | cut -c1-3000"
}
```


### [2026-09-05T05:25:04.606Z] TOOL RESULT

```
nfantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
The principal groups of this kind may be cited here for future reference. In general, the forms characterized by a labial or dental stop are applied to male relatives ‘father’, ‘grandfather’, etc., and those with n or m to female rela- tives, ‘mother’, ‘grandmother’, ‘aunt’, ‘niece’, etc. But there are many ex- ceptions, as new forms for the opposite sex may arise from either type.
1. papa, appa, baba, etc. Walde-P. 1.47; 2.4, 105. For ‘father’ or ‘old man’, Grk. rarma (voc. in Hom.), érza, arga, etc., late Lat. papa, Fr. papa, NE papa, etc.; It. babbo.
Goth. aba ‘husband’, ON afi ‘srand- father, ete.’, Grk. rémzos ‘grandfather’. Slay. baba ‘grandmother, old woman’, whence Lith. boba ‘old woman’, and fr. this bobuté ‘grandmother’. Cf. also MHG bobe ‘old woman’, buobe ‘boy’, NE baby, etc.
2. tata, atta, dada, ete. Walde-P. 1.44, 704. For ‘father’ or ‘old man’, Skt. tata- (in Rigveda) , Grk. tara, TéTTA, aTTa (but Skt. atid- ‘mother’), Lat. tata (fre- quent in inscriptions), Rum. tatd, W., Br. tad, NE dad, Lith. tétis (OPruss,
SELECTED INDO-EUROPEAN SYNONYMS
thetis ‘grandfather’), tévas, Lett. tévs, teta, Goth. atta, ON atte, OHG aitto, Alb. at, ChSI. ottct, etc., Hitt. attas, etc. Here also Slav. and Lith. teta ‘aunt’, etc.
A related group is Grk. 778n ‘grand- mother’, rnGis ‘aunt’, Getos, Ocia ‘uncle, aunt’, Lith. dédé ‘uncle’, ChSl. dédy ‘srandfather’, NHG dial. dezte ‘father, old man’, etc.
3. mama, amma, etc. Walde-P. 1.53, 2.221. For ‘mother’, Grk. nauun (also ‘srandmother’), Lat. mamma _ (also ‘grandmother’ and ‘nurse’), It. mamma, Fr. mama, NE mamma, etc., familiar in nearly all the European languages, in some as reg. word for ‘mother’. Cf. also Lett. mdsa ‘sister’, Lith. mosa ‘hus- band’s sister’, OHG muoma ‘aunt’, later ‘niece’ or ‘cousin’ (NHG muhme).
Grk. dupa, dupas, dupta ‘mother’ or ‘nurse’, ON amma ‘grandmother’, OHG amma ‘mother, nurse’ (NHG amme), Lat. amita ‘aunt’, Alb. amé ‘mother’.
4, nana, anna, etc. Walde-P. 1.55; 2.317. Skt. nand- ‘mother’, Grk. vavva ‘aunt’, vévvos ‘uncle’, It. nonna ‘grand- mother’, etc., Grk. avvis ‘grandmother’, Lat. anus ‘old woman’, OHG ano ‘grand- father’, ana ‘grandmother’, OPruss. ane ‘grandmother’, Lith. anyta ‘husband’s mother’. NG ypdavva ‘mother’, blend with forms like those in 3, above.
Forms of the above groups are not repeated in the following lists when they are only pet names on a par with NE papa, mamma beside father, mother. They are listed where they have become the normal words, like W. tad, mam, or where they are serious rivals of the old words, as in the case of It. babbo, mamm
```


## [2026-09-05T05:25:15.215Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^Adolph\\|^Albert\\|^dad,\\|^daddy\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T05:25:15.268Z] TOOL RESULT

```
1690:Adolph,  Adolphus,  masc.  PN.  —  L.  Adolphus,  of Teut.  origin.  The  name  lit  means  ‘noble  wolf’; cp.  OHG.  Athalwolf,  Athaulf,  Adulf,  Adolf  (G. Adolf),  fr.  athal,  ‘noble’,  and  wolf,  ‘wolf’.  For the  first  element  see  Adelaide  and  cp.  words  there referred  to.  For  the  second  element  see  wolf.
2105:Albert,  masc.  PN.  —  F.,  fr.  OHG.  Adalbert,  lit. ‘bright  through  nobility’,  fr.  adal,  ‘nobility’, and  beraht,  ‘bright’.  Cp.  Ethelbert,  fr.  OE.  Aidet- bryght,  which  is  the  exact  equivalent  of  OHG. Adalbert.  For  the  first  element  see  atheling  and cp.  words  there  referred  to.  For  the  second element  see  bright  and  cp.  the  second  element in  the  names  Egbert,  Gilbert,  Herbert,  Hubert, Lambert.
2107:Alberta,  fern.  PN.  —  Formed  fr.  Albert, albertite,  n  ,  a  bituminous  mineral.  —  Named after  Albert  County  in  New  Brunswick,  where it  is  found.  For  the  ending  see  subst.  suff.  -ite. albescence,  n.  —  Formed  fr.  next  word  with suff.  -ce.
```


## [2026-09-05T05:25:18.686Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (1690,2105):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln, 'leaf(ff count)=', t[:off].count('\\f'))\nEOF\necho \"=== atheling ===\"; grep -n \"^atheling\" KLN_1966.txt | head"
}
```


### [2026-09-05T05:25:20.370Z] TOOL RESULT

```
1690 leaf(ff count)= 26
2105 leaf(ff count)= 35
=== atheling ===
3815:atheling,  n.,  a  noble,  a  prince.  - —  OE.  aedeling, ‘a  noble’,  fr.  tedele,  ‘noble’,  which  is  rel.  to OFris.  ethele,  OS.  edili,  OHG.  edili,  MHG. edele,  G.  edel,  ‘noble’.  The  orig.  meaning  of these  adjectives  was  ‘noble  by  birth’.  Cp.  odal and  the  first  element  in  Albert,  allerion,  Alphon- so,  Athelstan,  Audrey,  edelweiss,  Ethelbert, Etheldred,  Ethelinda,  Ulrica.
```


## [2026-09-05T05:25:25.098Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dad,  n\\|dad, n\\|daddy\" KLN_1966.txt | head -10; echo \"=== 1971 ===\"; grep -n \"^dad\\b\\|dad,  n\" KLN_1971.txt | head -5"
}
```


### [2026-09-05T05:25:25.168Z] TOOL RESULT

```
10196:Dacus,  n.,  a  genus  of  flies,  the  olive  fly  ( entomol .) —  ModL.,  fr.  Gk.  Saxo?,  ‘any  animal,  the  bite of  which  is  dangerous’,  lit.  ‘a  biting  animal’, rel.  to  Saxveiv,  ‘to  bite’,  8a£,  ‘biting’,  8rjy[za,  ‘a biting’,  8f]XTr)s,  ‘biter’,  fr.  I.-E.  base  *denk -, ‘to  bite’,  whence  also  OI.  ddsati  (for  *di}keti), ‘bites’,  ON.  tong,  OE.  tang,  tange,  ‘tongs’.  See tongs  and  cp.  the  second  element  in  carpodacus, Tridacna,  Demodex,  Mixodectes. dad,  daddy,  n.,  father.  —  A  child’s  word.  Cp. W.  tad,  dad ,  Ir.  daid,  Co.  tat,  ‘father’,  hendat, ‘grandfather’,  Czech  tata,  Russ,  tdta,  Lith. let  is,  tete,  'father',  OPruss.  thetis,  ‘father,  old man’,  Ir.  daid,  Co.  tat,  W.,  Bret,  tad,  tat,  ‘father’, Alb.  tats,  ‘father’,  L.  tata,  ‘father’,  Gk.  toct<x, ‘father’,  tol-ol,  tettx,  ‘O  father,  daddy’,  xaxa- Xt^etv,  ‘to  flatter’,  ModGk.  Sa8a?,  ‘father’,  OI. tatah,  ‘father,  son’,  which  all  are  of  childish origin.
17638:Derivatives:  heritabil-ity,  n.,  heritabl-y,  adv. heritage,  n.  OF.  eritage,  heritage  (F.  heritage), fr.  eriter,  heriter  (F.  heriter),  ‘to  inherit’,  fr.  ML. hereditare,  fr.  L.  heres,  gen.  heredis,  ‘heir’.  See heir  and  -age  and  cp.  heredity, heritor,  n.,  an  inheritor;  heir.  —  ME.  heriter,  fr. OF.  heritier  (F.  heritier),  ‘heir’,  fr.  L.  heredi¬ tdrius,  ‘relating  to  an  inheritance’  (whence  also OProvenip.  heretier,  eretier,  Sp.  heredero.  Port. herdeiro,  ‘heir’).  See  hereditary, hernia,  n.,  pillar  representing  a  head  of  the  god Hermes  (Greek  antiq.)  —  L.  Herma,  fr.  Gk. '  Epixrfi,  ‘Hermes ;  statue  of  Hermes’.  See  Hermes. Herman,  masc.  PN.  —  G.  Hermann,  fr.  OHG. Hariman,  lit.  ‘man  of  war,  warrior’,  fr.  hari,  heri, ‘host,  army’,  and  man,  ‘man'.  See  harry  and man  and  cp.  the  first  element  in  Herbert, hermandad,  n.,  name  of  a  league  originally  formed against  the  violence  of  the  nobles,  organized later  as  national  police.  —  Sp.  lit.  ‘brother¬ hood’,  fr.  hermano,  ‘brother’,  fr.  L.  germanus, ‘having  the  same  parents’  (said  of  brothers  or
=== 1971 ===
63425:dad, daddy, n., father. — A child’s word. Cp. 
89623:dad), acc. of facilitds, ‘easiness, ease, fluency,
```


## [2026-09-05T05:25:31.647Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:10195])\nprint('leaf=', t[:off].count('\\f'))\nEOF"
}
```


### [2026-09-05T05:25:34.100Z] TOOL RESULT

```
leaf= 218
```


## [2026-09-05T05:25:38.999Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==219' KLN_1966.txt | grep -oE \"^[0-9]{3}$|[0-9]{3}[[:space:]]*$\" | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==219' KLN_1966.txt | head -3 | cut -c1-200; echo \"--- tail\"; awk 'BEGIN{RS=\"\\f\"} NR==219' KLN_1966.txt | tail -3 | cut -c1-200"
}
```


### [2026-09-05T05:25:40.851Z] TOOL RESULT

```
396
397
---
 See  -cyte.
cytology,  n.,  study  of  the  structure,  functions  and life  history  of  cells  (biol.)  —  Lit.  ‘study  of  cells’, compounded  of  cyto-  and  -Xoyta,  fr.  -Xoyop, ‘one  who  speaks  
cytoplasm,  n.,  the  protoplasm  of  the  cells  (biol.
--- tail
397
is  compounded  of  Sat?,  8a:?  (gen.  8at8o?,  resp. 8x36?),  ‘torch’,  and  syeiv,  ‘to  hold,  have’.  The first  element  is  rel.  to  Sodetv  (for  *Sxft£iv),  ‘to blaze,  bum’,  a
daedal,  adj.,  ingenious,  skillful.  —  L.  daedalus,  fr. Gk.  SalSaXo?,  ‘cunningly  made’,  fr.  SatSaXXetv, ‘to  work  cunningly  or  skillfully’,  which  stands for  *8ai-8ctXieiv  an
```


## [2026-09-05T05:25:46.854Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT āthwya ===\"; grep -n \"āθwya\\|a\\^θwya\\|āthwya\\|Ā̊θwya\\|θwya\" BRT.txt | head -20"
}
```


### [2026-09-05T05:25:46.917Z] TOOL RESULT

```
=== BRT āthwya ===
```


## [2026-09-05T05:25:48.211Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD Aspiyan ===\"; grep -n -i \"spiyan\\|āspyān\\|aspyan\\|Ābtīn\\|abtin\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T05:25:48.276Z] TOOL RESULT

```
=== PHD Aspiyan ===
```


## [2026-09-05T05:25:50.412Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT thraetaona ===\"; grep -n -i \"raētaona\\|raetaona\\|Thraetaona\" BRT.txt | head -20"
}
```


### [2026-09-05T05:25:50.488Z] TOOL RESULT

```
=== BRT thraetaona ===
14459:•  j.  draetaona-  m.  £N.  eines  Helden der    iranischen    Sage,    Fariäün'^:    *mm
```


## [2026-09-05T05:25:51.186Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c . BRT.txt; head -20 BRT.txt | cut -c1-200"
}
```


### [2026-09-05T05:25:51.257Z] TOOL RESULT

```
30725
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  to  the  past,  representing  a  wealth  of  history,  cultuie  and  knowledge  that's  often  difficult  to  discover.
Marks,  notations  and  other  maiginalia  present  in  the  original  volume  will  appear  in  this  flle  -  a  reminder  of  this  book's  long  journcy  from  the
publisher  to  a  library  and  finally  to  you.
Usage  guidelines
Google  is  proud  to  partner  with  libraries  to  digitize  public  domain  materials  and  make  them  widely  accessible.  Public  domain  books  belong  to  the public  and  we  are  merely  the
+  Make  non-commercial  use  ofthefiles  We  designed  Google  Book  Search  for  use  by  individuals,  and  we  request  that  you  use  these  files  for personal,  non-commercial  purposes.
+  Refrain  fivm  automated  querying  Do  not  send  automated  queries  of  any  sort  to  Google's  System:  If  you  are  conducting  research  on  machinc translation,  optical  character  recogn
+  Maintain  attributionTht  GoogXt  "watermark"  you  see  on  each  flle  is essential  for  informingpcoplcabout  this  projcct  and  hclping  them  lind additional  materials  through  Google  Boo
+  Keep  it  legal  Whatever  your  use,  remember  that  you  are  lesponsible  for  ensuring  that  what  you  are  doing  is  legal.  Do  not  assume  that  just because  we  believe  a  book  is  
Äbout  Google  Book  Search
Google's  mission  is  to  organizc  the  world's  Information  and  to  make  it  univcrsally  accessible  and  uscful.   Google  Book  Search  hclps  rcadcrs discover  the  world's  books  while  hc
at|http: //books.  google  .com/l
db,Google
db,Google
db,Google
```


## [2026-09-05T05:25:58.082Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -iE \"a[0-9O@θϑc]wya|athwya|aspyan|Faridun|Farid[uü]n\" BRT.txt | head -20"
}
```


### [2026-09-05T05:25:58.140Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:26:00.381Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '14450,14470p' BRT.txt | cut -c1-300; echo \"=== wc ===\"; wc -l BRT.txt; grep -n \"Fariäün\\|Faria\" BRT.txt | head"
}
```


### [2026-09-05T05:26:00.467Z] TOOL RESULT

```
Super),  in  '%wyaHl-  Adj.,  PPA.  lum  V.  %'uiay-. —  PO.:  timakeittar.  —  >l  Es  sind  die  ebe  aen Sand-  und  SalzwQsten  im  Gegensati  zu  den Bergen  und  Tälern  gemeini.  Pü.  führt  als Beispiel«  für  die  beieichneten  drei  Örtlich- keiten der  Reibe  nach  an:  spähän
•  j.  aetahe  "9«asat"  tbisamiAa  V.  7.  52 PüZ.
')  Nach  JN.  JAOS.  16.  cxxvm  sva.  sHa%al, 35.;  aber  die  gegebene  Obersetiung  itt  un- möglich.
•  j.  Snätö   F.  2^:   -?-. Pü. :  faßrisH.
•  j,,  g.  iSyajah-,  iS'yeJah-''  n.  'Not, Gefahr" ;  yS  nanm  .  .  apa  qzankal . .  apa 'ajat)hat  baraiti  YL/0.  aa;  —  ayh  'ejä vöiinä  Y.  57.  14;  —  tbaiA  ..  'eja  .. •e/ä  Y.  65. 8.  a)  mit  Dat.  'fUr -':  täis' .  .  ^ao%anJis  ,  .  yaiiü  as  pairJ  pountbyö (
KompE. ;  Ableiu  —  ai.  lyd/as-  n.  (woiu  ZDMG. JJ.aSi).  —  Pü.:  lii  (s.  d«iu  HB«.  PSl.  iio), Sa.:  mj'lyuii.  —  ')  J  ajrf.  i.  —  a)  Sd.
•  j.  iS-yeJah'vant-  Adj.  (fem.  °vaiti-)  'ge- fahrvoll, mit  Gefaliren  umgeben':  'Javu- hatat  a>9haof  ai^yejavhuntim  avi  Bhum H.2. 16;  V.  7.  52,  75.31  (beide  Male  'jar^ katat);    —    tanvö  •jaauhaiti  (VSf)  Aog.
25-2*'^.
KompE.  —  Pü.:  asHömatui,  Sü.:  vinälai'än.
•  j.  draetaona-  m.  £N.  eines  Helden der    iranischen    Sage,    Fariäün'^:    *mm
idswyilHim  FrW.  2.  i ;  —  'naAe  ithwyanBif Vt./j.i3i,  *FrW.2.i,  3i  —  vm pu'^rff ähwyanSi!  vXsS  sarayä  'nö  Yt.5, 33,  17. 35;  —  vartnfm  yim  cahrugaospm  yakmäi tayata  'nB  Janta  aSsis  i/aAäiät  V. /.  17; —  'rur  yS  janal  aiim  äahäk^m  Y.g.jt; Yt.  j^  40,  lg.
*)  Er  ist  in  l^arma  als  Sohn  A%wyas  geboren;
leine  Haupttal  ist  die  Besiegung  JJaAäiai;  eine
weitere  Enählung  s.  utxter  fiäurTa- ;  vgl.  Y.  p.  7  f.,
Yt.  J.  33.  61.  Bd.  2j.  3,  is.  9,  j/.  9,  SBE.  47.
10.     Über   seine    Beiiehungen   inm   vedischen
TrilaAfitya  s.  luletrt  DsT.  ZA.  /.  86,  Bthl,  IF.
/.  iSo.
Wohl  Abteil,  ans  %rita-;  doch  ist  die  Bildung
unUar;  s.  IF.  1.  iSo.    Schwerlich  richtig  JusTi
NB.  513    (wonach   BB.   aj.  57).    —    ai.   »gl.
=== wc ===
30724 BRT.txt
14459:•  j.  draetaona-  m.  £N.  eines  Helden der    iranischen    Sage,    Fariäün'^:    *mm
```


## [2026-09-05T05:26:06.798Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"wya\" BRT.txt | head -30"
}
```


### [2026-09-05T05:26:06.861Z] TOOL RESULT

```
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
3026:manaKiAa  Y.iff.^.  \naos  apazaäauhö  •wya  {GSf.y*  "..  in  der
3247:'ra  als  Adv.  'unten,  untenhin':  nsmattha  °ra diia . .  upara  data  Yt.  lo.  1 1 8.  b)  ASa 'rtm  als  Adv.  'nach  unten':  at.kisca  .  . yai  *'r3m^^  aiwyankayanti ..yezi  *upar>m ". .  wenn  sie  sie  (von  oben)  nach  unten  an- ziehen . .,  wenn  (von  unten)  nach  oben  . ." N.53.  2)    'von    unten,    vom  Tiefland
3279:•  j.  a-8äitya-  Adj.  'nicht  so  wie  es  dem Gesetz  entspricht,  ungesetzUch,  ungehörig': duityanam  raiwyanqm .."yanqnt  ard^wya- tiqm  ^ao^nanamYr.  ij.i.  [N.io-:lies äiiityö.]
3414:Pü.  r  ablm.  —  i)  Mds.  aiwyai?k!m  )).  —  ')  Hds, \u1ayaah3m.  —  ])  Beibehaltung  und  Vergleich mit  ai.  bkiyäsa-  verbieten  die  folg.  Wörter.  — «  S.  iSt.  Bthl.  IF.  12.  1 14-
3629:•  j.  apa-srayamna-  Adj..,  PPM.:  s.  sray-. m  j.  apa-za<)ah-  Adj.  (auch  fem.)  'den Steiss  ab-,  weghaltend  (nach  oben?)''*, von  der  Fliege:  ^maxsiJiihrpa  prrfaitya frasnaol  °Sawi4ff(GSf.))  * akaramm.driwya (sd.)  V.7.2.
3663:—  5rJ5r?»i  (sd.)  .  .  Aapla  tar^a  'kahe V.75,4s;  —  yat  .  .  mazdayainS  'kS  avt hl  hapia  sania  frajasäiti  .  .  aiwyarahänS {sA^  paUis  he  ma^yäi  bBjyaman!!  VA-iS;
3953:I  j.  aiwyaahim  N.  lO:  lies  a'i-j}ayaah>m.
3964:aiwyaxätar-
3965:aiwyaohayamna-
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
3993:•  j.  aiwyaohayamna-  Adj.,  PFM.:  s. Komp.;  ahoi-Y^y&ah' .
3996:aiwyaohä-
3998:•  j.  aiwyaaha-  f.  'Lesen,  Studium'  uzw.  1  durch,  dass  ihm  (dem  Schüler)  kein  Be- der  heiligen  Texte:  ka  asti  ihy^a  »la/^!  scheid  wird?"  N.  ij; —  vtspagsu  "partnti saonB  {%A.)f  ..  aya  doEna  disyut  .  .  yB  .vlspaiiü  *'fi*i  ästryeiti  "jedes  Mal,  wenn %ritarymaEm  ratüm  'kam  nHit  aiwyästi  \  Einwendung  erhoben  und  kein  Bescheid Mit  gä'hs  srävaydti  "..  er  könnte  durch  gegeben  wird,  versündigt  er  sich"  N.7_J. seine  schlechte  Religion  (einen)  dazu  ver-  j  P"--  a/rälgda^Hnih.  —  ■>  s.  No.  3, 4.  —  i)  Ausg. leiten,  daas  er  wihrend  der  drei  (dafür!  l%^fZtl,^tl  ^- *)'m^^''Sr5ti~  ^'  "^ bestimmten)  Frühlinge'*  dem  Studium  (der  .""''  '',"^''  __  .  /'  ,™  '  .  ,  , ■    -       _       ,    .  ."    ,^..     •  ].  a-fra'oxiayant-  Adj.  (fem.  yan/i-)
4280:■anaiwyastay-
4300:•  j.  an-aiwi'ätay-,  an-aivi'ätay-"  f.  1) 'NichtStudium,  Unterlassen  des  Studiums'; yS  asrut^aosB  vä  a/ravaocS  vä  neit  lim afum  vääm  *aiwyas  tisit  *paslalta  'viM astryeili  yezi  dal  *öyum.pe  *v3am  *aiwyäs "wuti  ästryäti  "wenn  einer,  weil  er  taub ist  oder  stumm,  auch  nicht  ein  einziges Wort  lesen  kann,  dann  macht  er  sich durch  NichtStudium  nicht  sündig;  wenn er  aber  auch  nur  ein  einziges  Wort  lesen kann,  so  macht  er  sich  durch  NichtStudium sündig"  N.  i4;  — y5  .  .  nSii  aiwyästi  (sd.)
4819:—  *%rigamim  aiwyast/lt  haca  *bamm?n paräiti  N.  Ä^.  c)  mit  avi  oder  paiti und  Akk.  oder  mit  Dat.  oder  mit  Gen.  'hin
5317:•  j.  a-ra9Twya-  'unzeitig;  unangemessen, ungebührlich':  'wya  daxsta  "wimla  gar)- m3um  V. /.  18;  17;  —  ra%wyanqm  .  . syaohnanqm  . .  aoäityanqm  •wyanqm  dui- varstanam  iyao^nanam  Vr.  15.1;  —  °wya Vyt.47'-(?),  4^C?)-  '
6201:—  ^«M  jTvyqm  a°  usdätqm  Y.  22.  i;  — haoma  .  .  a'  usdata  a'  uzdahyamna  a' aiwi.vag'jayamna  Vr,(?.3;  3^^  Y.22.1;  — bansmanqmca  a'  */rashr^anqm  haoma- nqmca  a°  kutanqm  Vr. /2.3;  —  bar»sma . .  a'/rastar^fym  Y.2.1,  4~^,  /1.23,  V._j.i5, Ä14,  15,  Vyt2_3,Vr./i.  2;  io.  2;  —  bar)sma a'  aiwyasUm  Vyt  23;  —  yal  ba  paiti  .  . airihä  samS  naire  asaone  vprxyJi  a' daoaifi  V._J,  34".  a)  in  Verbindung mit  vanhuya  (sd.):  yat  na  kasvikamcina ya»huyanqm  .  .  naire  a/apne  jasia  a°  va- nhuya  riBij  daoaiti  V.  18.  $4;  28,  37,J-35'*;
6697:ai'hra.patsit   (sd.)  pairi    ^aiwyaahat    N,
6764:ra>wya  fräraihya  (sd.)  alahe  dätaisY.  KompE.;  Ableit.  (s.  auch  aahw);  s.  noch Je.  b)   sonst:    «»V   aH'a    aha    (NS.)'>       sniura..  —  Zum  V.  =Aif-*);  vgl.  a«*/fl-,  »u-i«.
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
7903:roer"V./5.45;  — cvat  nä  ape  ar»ialstaya\t3m  i°  hanjasatiU ya^  *mai,r3m.sp3niim.- ..paitijiarati  yd>ia  %ri^  i^anma  ..näva-\6a?sazyB'V.-j.^^;  —  kva  i'  aiwyatj/iayanii yayäi  *iii  ape  N. 6j;  —  akmäl  *mainy^s\ N. S5.  b)  doppelt  mit  folgendem  »J ränrfänti  (sd.)    dr»gva»tiS    .  .    nöit    'S,/ | 'sei  es  -  sei  es':  aesqmH^^sA.)  (•  vä  asni
8070:•  j.,  g.  izä-'>  f.  1)  'Stieben,  Eifer",  bes. 'frommer,  Glaub enseifer':  manS  voha  uru- nascä  asiiunqm  n>mascä  yä  ärmaiti/ (sd.) °zäcä  Y.4g.io;  —  mat  vä  padäis  (sd.) yä  frasrütä  (sd.)  -zaya  Y,  50. 8 ;  —  ^vldl- hmnäi  (sd.)  'zäcit  (IS.)  .  .  vahistsm  Y.jr. i;  —  ya%a  'za  (IS.)  viicim  näsima  Y, 70.4.  a)  Plur,  in  Verbindung  väwyaostay- usw.,  Plur.;    °m  yaostayS  fora^tayS  ärma-
8143:—  tiiig  zbayS  (sd.)  varthiul  "däii  manatshö Y.  ^f7. 14;  —  'iiMH  trlrpmF.jf.;  —  ra^wya 'da  F.^f.;  —  pjnse  %ioqm  rasnya  '%ahe YL  72. i;  —  gave  n>ms..'}am ..  v^r^'^rpm W  10. 20.  a)  insbes.  'von  den  Göttern verkündeter,  geoffenbarter  Spruch,  ora- culum':  Ayat  xsmä  'oJis  didaitihs  (sd.) paounJm  Y.  43- 1 1 ;  —  y<icä  vohu  'i>ä /rast  (sd.)  mananhit  yjca  asä  anhSus  Y. 44. 8 ;  —  ditidi  *asä  da  *dar3gäyü  prMvdis (sd.)  lü  '(..lis  maüdä  Y.2S.6;  —  aAm 7'oiB  manauhii  °'6il  (IS.)  yilil^  ärmaitis  .  . mazdJr  rapunm  lag^dS  (sd.)  ".  .  der  Ver- kündigung gemäss  .."  Y. 57.20;  —  aitatca aeiqm  'hanqm  uxhs.btrum  {stL)  yiit's  yaz-a fraia  vaece  ,  .  Y.  79. 10;  —  sarai^ustrahe .  .  paoiryäi  hat/hanuse  gqmca  ahmca '<ijm/a  •tiaSyäca^^  sraosjm  xsa&fvmca  Yt 7^.88.  2)  'Rede,  Reden,  Worte*  im Gegensatz  zu  Denken  (Gedanke)  und  Tun (Werk):  nüit  ttä  manä  ..  naaiä  varanä (sd.)  nSil  'hä  naldä  /yaohamJ  nett  daenä .  .  Aacaintl  Y.  45.3;  —  aiüä  hsi  scanta manatihä  'oiiis  fyao^anilisciJ  xsuüm  (sd.) mazda  Y.  5^.  2 ;  — paurvatätsm  (sd.)  mana- i^hascä  vatfhSui  .  .  syao^anakya  .  .  yäcii ^oahyJcä  .  .^  y.^j.  14;  4>8;  —  vanhSui
9671:•  j.  ^gaiwa  kUTÖ  kurö  lartwani  kara- panS  rä>wyasnam  buxtä  mähe"  FrW.2.  z.
10206:mit  avi  'preisen'(?):  avi  ratüs  aii rahwya  ginnle  (3SPM.)  Vr.  4-  t(?)  ''■
10335:•  j,  gä^iwya-  Adj.  ',fiiäisch,  in  den Cjäjs  enthalten':  Aakra  ana  °ya  vaca "mit  diesem  ^5>ischen  Wort"  Y.  70. 19, Ö5. 14,  Ny.  4.  8'*;  —  *imqm  'yqm  (APm.) vac9  srävayis  "diese  ^aSrischen  Worte  her- sagend" H.2.  20.
10442:fravartis  agarbäyatä  "Fr.  wurde  gefangen  i genommen"  Bh.  2. 13.  E  3)  'etwas  weg- 1 nehmen  von— (Abi.)':  g}urvaya  Äipälai'e. sävar»  Y.  r).  28.  4)  'einen  Anteil  be- ! kommen  von  — '  (Gen.):  tnä  hl  mairyö'. giurvayöit  "nicht  soll  davon  was  be- kommen , ."  Yt.  8. 59;  —  yezi  se  mairys gfurvay.V  Yt.Äöo;  —  mizdahe  .  .  g>r)W- 1 ytiti  yS  girswyaUe  VyL  JO  (?).  5)  'i^-
```


## [2026-09-05T05:26:12.552Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hwya\\|%wya\" BRT.txt | head -20"
}
```


### [2026-09-05T05:26:12.653Z] TOOL RESULT

```
5317:•  j.  a-ra9Twya-  'unzeitig;  unangemessen, ungebührlich':  'wya  daxsta  "wimla  gar)- m3um  V. /.  18;  17;  —  ra%wyanqm  .  . syaohnanqm  . .  aoäityanqm  •wyanqm  dui- varstanam  iyao^nanam  Vr.  15.1;  —  °wya Vyt.47'-(?),  4^C?)-  '
10206:mit  avi  'preisen'(?):  avi  ratüs  aii rahwya  ginnle  (3SPM.)  Vr.  4-  t(?)  ''■
14384:•  j.  ^Tvay-  V,  'Furcht  erwecken;  —  hegen'. Praes.  a  %waya-,  3  %wya-.
14385:"Furcht  erwecken' :  %wyatit-  (nur  Ableit).
14442:Jhwya-
14450:Super),  in  '%wyaHl-  Adj.,  PPA.  lum  V.  %'uiay-. —  PO.:  timakeittar.  —  >l  Es  sind  die  ebe  aen Sand-  und  SalzwQsten  im  Gegensati  zu  den Bergen  und  Tälern  gemeini.  Pü.  führt  als Beispiel«  für  die  beieichneten  drei  Örtlich- keiten der  Reibe  nach  an:  spähän,  afiärsen, äräsiänlf).     Vgl.  Dst.  ZA.  2.  15-
14460:idswyilHim  FrW.  2.  i ;  —  'naAe  ithwyanBif Vt./j.i3i,  *FrW.2.i,  3i  —  vm pu'^rff ähwyanSi!  vXsS  sarayä  'nö  Yt.5, 33,  17. 35;  —  vartnfm  yim  cahrugaospm  yakmäi tayata  'nB  Janta  aSsis  i/aAäiät  V. /.  17; —  'rur  yS  janal  aiim  äahäk^m  Y.g.jt; Yt.  j^  40,  lg.  9a ;  —  'ftSyat  äs  masyanqm ..  wrüravastimö  ..  Yt/9.36;  Az.2;  — päurvö  (sd.)  .  .  yal  dim  usca  usdvanayaj Vfrf%rajä  taxtnS  'ne  Vtj.  öi;  —  tl  ySi pü^ra  'nahe  F.4C
14461:*)  Er  ist  in  l^arma  als  Sohn  A%wyas  geboren;
21436:wa    aoxt5.namana  yasna    ra%wya   vaca
21935:c)  im  jAw.:  yö  sBne  pistr^m  jainti  us  v hl  gaohm  ^Wir>saili  apa  V  hl paihyqm kmntaiH  V.  13.10;  —  mqnay^n  bä  .. aipi  ta  nasus  zga'haite  ya'ia  iius..ya%a\ V*  ramais  .  .  yalia  v°  rdhwya  varma  V. ! 5.4Ö;  JiV. 65.  ni)  v  steht  bei  allen' Gliedern;  zu  I):  a)  im  Ap.:  tya^säm  ha- iiam<^  a%ahy^  xiapJ'va  raucc^paHva' Bh.  /.  7.  b)  im  gAw.;    nä  v*  nairT
22266:(sd.)  Yt7J.  64;  —  nSit  dim  bitlm  väcim  paiti£\.6^.q;  —  kaha  zaota  xsäta  vaca faiti.p?r>simnB  bva  (Sp.  929  u.)  V.  18.  29 ; '  apB  .  .  yazaite  Y.  ^5.  9 ;  —  yasi  %wa  .  . —  a  dim  tä  vaca  rämayat  {sd.)V.ß.  21 ; —  rdhwya  vaca  yazaite  Yi.10.30;  31,  56; yezica  Aj  narö  irisia  kva  Aisva  uxh)m  —  yakmäi  zaota  ..mikrahe  vaca  yazäite vahm  ..paiti  dyatti  vlspanqm  vacam  Yt.  70.137;  —  vacqmca  vänikrayninqm uxoanqmca  .  .  hary^nm  barät  Vd.2;  ■ —  fraväkäi  Vr.75.3;  —  väca  humata  küxta yai  Alm  afm  *draogpm  väcim  arahat^lm  kvarita  ayese yeiti  Y.J.4;  Ji.  18;  —  mit änmäne  (sd,)  paiti  barata  Yt,  79. 33;  —  dem  Beiwort  ar/iMräa-,  ^wiöirSa- (sd.):  ime dratr/B  växs  Yt3.g,  12;  —  vainlj  ahmi  hftiti  arhxta  väcB  däsmainis  värflbraynis nmäne  ..arsusäiB  Vax s  mikaoxlim  väcim  paiti.bisis  bais'azya  Y. /o.  18;  —  vaca Y,  60  S;  Yt  tg.  96".  4j  bes.  von  den  in  ariuxaa  . .  vänhraynis  darvö.ynlta  G.  2.6; festeForm  gefügten  Worten  der  »ia«alschen  Y.^.as  PüZ.,  71.10,  Vr.7.1,  20.1,  Yt.18.%; Religion^)  'Spruch,  Vers;  Gebet;  Zauber-  —  u^ta  tl  apivaiahe  *p0uru  *va(qm** formel':  airiha  damayä  mqs  (sd.)  vaca  fr)zux%anqm  Y.p.as;  27,7;  —  a^S  .. (AP.)  dähänahe  nöit  iyao%fikil  apayanlake  växs  gnzux^B  */ramrvqnB  .  .  sfanvanti (sd.)  Y.5.31;  —  äxstaioa  damaya  vaca  (sd.)  H.7.4;  —  mihr^m  . .  yim  yaaata jramrß  V,  j,  i ;  —  ahunB  vairyB  vacqm   haomS . .  anäAit?m  anahit3 . .  anäAitaiibyö
22358:asavatum  .  .  yd  anhat  °/j  arsvacH  (sd.) V.  ^.  2;  —  sonst  nur  neben  manah- (zum  Wortlaut  der  Stellen  s.  Sp.  11 39 unter  o)  und  ^aohna-:  yänJm  manö  .  , •CS  ,  .  ^ae%p>m  zar^uitrahe  Y.  i8.  o; V.7.  51',  Äioo,  Yty.  83; — ma  apama .  .  mä  manaaha  .  .  'canha  ,  ,  Syao%na ^mäha  ka%acina  *paiti.jime  Vr.  22,  a;  Y. 1.21,  Ji.  18  (•caaAä);  —  vJ  Jasväi/ .  . iarim  mruyl  .  .  vT  matisbli  .  .  °cSbll  ,  . ^ao%anaU  Y. /2. 4;  —  pairl  manä  .  . °/ä  .  .  iyao^ana  .  .  dadsmahl  Y.  $8.(s;  — nazdys  ahmt  .  .  atahlui  astvats  *matiasca 'cäs/a'>  *iyao%naca  ya^a  .  .  P.  2<S';  — t^m  yazala  .  .  zarahustrS  V3r7'hraynake paiti  manahi  . .  'caki  . .  ^aohne  Yt- 14.  a8; —  vavatu  buye  ra%wya  manaaha  .  . °iaf)ha  .  .  syaö>na  A.  ;.  1 1 ;  —  yas^a  .  . imat . .  vacö  (s,  Sp.  1341c)  fravaocäi  asa.- sara  manaaha  .  .  'canha  .  .  fyadhna  Yt. 11.4;  —  sSksi  manarthe  .  .  -cofske  .  . syaohnahe  H.68.4;  —  iistuyi  humaüm manS  hüxtim  'l5  Avarsüm  iyaü%anfm  Y. J2.  8;  Vr,  2.  s;  —  ma  %rayqm  vaAista- nam  aiwi^yS  iuyata  humataheca  manaighs hüxtaheca  'canhs  kvarstakeca  syaö^nahe %rayqm  aiistanqm  aiwi^yO  buyata  dul- mataheca  mananhö  duzüxtaheca  'caahd duivarsiahe'a  syaehnahe  V.  iK  17;  Yt. 16. 5,  3)    'Ausspruch,    Spruch,    Wort,
23041:pa%B  . .  därayahwfm  (sd,)  ,  .  düityanqm rdhwyanqm  hvarstanqm  syadhnanqm  V ". .  um  die  gehörigen,  angemessenen,  guten Werke  zu  tun"  Vr,  15.  i;  s.  unten  bei pairi.
23043:mit  pairi  'sich  von  dem  Tun,  der  Be- gehung von  —  (Gen.)  fem  halten,  sie  unter- lassen': pairi  dtäityanqm  ara%wyanqm duzvarsSanqm  lyaohnanqm  v°  "um  die ungehörigen,  unangemessenen,  bösenWerke zu  lassen"  Vr,  /j,  i ;  s.  Simpl.
30695:zu  duzvaHta-:  daityanqm  rahwyanqm 'lanqm  lyadhnanqm  var)zäi  pairi  . .  duz- variianqm  syaöknanqm  varjzäi  Vr.  7J. I,  a)  sonst  nur  neben  hüxta-  und humata- :  humataht paiti  manaahe  küxtahe paiii  vacatahs  °tahe  paiti  iyao%nahe  Yt 16.  6;  —  ästuyi  humatim  manO . .  küxUm vacö  .  .  •Um  syad^amm  Y.  J2.  8;  — fra- stuyl  kumaisibyascä  hüxtsibyascä  'tdibyascä mahwsibyascä  vax>hwSibyascä  varltvSi- byascä  Y.  //.  17;  —  nanm  alavamm dahrUfUm  kumatimca  manB  hüxümca  vac5 •Umca  syaohtum  Vr.  2.  5;  —  aa^. .  manya mananha  humahm  . .  hitsva  mrätoi  hUxttm .  .  sasiaiibya  var>za  't»m  syadhium  Aog. 25  ff.;  ^  *ar»m.maiti  *Aumata  mamne  (Sp. 1121  f)  *ar>m.uxti  *  hüxta  (vavaca)  anm.- varsti  °ia'^  (vavarfzd)F.2^; — yezi  kuma- tim  mainySt  kUxt^m  väcim  mrväl  'bm'^ v»nsyäl  syadhn»m  Gk-iöy;  —  narS  asa- vanö  humataü  mainimna  hüxtäU  ntrvats 'täis(3.\sOb}.)v>rpzyant3Y.jo.4;—AumiUa- nqm  hüxtanqm  •tanqm  iyadaca  anya- dacä  v»r>zyamnanqmcä  vävtmananqmca mahl  aibT.jaritärS  Y._J5,  aj  FrW.^,  i;  — "•"rfil^r* (sd,) ,  .paiti  nivaitis . .  humaialsuia haxtalsuca  •taisu^a^'*  ti.S4;  —  vTtpäi/ 'hwa   humatäii  .  .  huxtäis  .  .  'täis  pairi-
```


## [2026-09-05T05:26:23.851Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Vaters\" BRT.txt | head -20; echo \"=== line 14435-14449 ===\"; sed -n '14435,14449p' BRT.txt | cut -c1-200"
}
```


### [2026-09-05T05:26:23.989Z] TOOL RESULT

```
5569:is)v.  —  Pu.i  m/ian,  frmän  x'aiiiiiiA.  ,  j    »auTvat-aspa-    m.    EN'.    des  Vaters
7413:.j.  ärästya-  m.  EN.  eines  Gläubigen. '  f^" " ^  ~  "^''^^  "'^ -^^'''^•v  Y*^" des  Vatersbruders   Zara>uilras:   numyH-  ^<'r>m(^d.)  ^f^'-^f^y^i   'tt^J.43.^^.
12354:•  j.  *tüirya-  m.,  tüiryä-  f.  'Vatersbnider, -Schwester':  yat  •ye..ya  va  para.iriäyei/i V.  72.  15,  [tairya'  V.  72.  19:  s,  unter duymiri;  —  V.  72. 17:  lies  täiryS.pu%rS, tBiTyaJuyha^
12357:•  j.  *tüirya.du/()ar-'>  f.  Tochter  der Vatersschwester':  yat  *taiTyB./iu^rS. .  'dujla va  para.iriiiyäH  V.  72.  17.
12359:•  j.  *tüiryö.puflTa-  m.  'Sohn  des  Vaters- braders': yai  '"hrs.-.  mirya.durj\a  vafara.- irihyeiti  V.  12. 17.
14602:•  j.  Srita-  m.  EN.  zweier  Gläubigen; i)  des  Vaters  des  UrvSxsaya  und  K^n- säspa  aus  der  ^amo&milie*':  °ts  sämanqm snistö  .  .  tai  akmäi  jasat  ayapttm  yat  hl puhra  usjoysiire  urväxsayS  ktnsäspasca Y.5. 10;  —  US  paoiryS  masyänqm  %am- namihatqm  .  .  yashm  yaskai  därayai  V. 20.  2,  2)  des  Sohns  des  Ssyuidri: aiavasdatiAll  *taht  *säyusdröis\l.i3.iiy, —  asavazdasca  °tasla  täyuidrsii  (sd.) Pukra  YL5.  72.
16313:•  j.  pourusaspa- '*  m.  EN.  des  Vaters Zara^ustras:  'ps ..yat  hi  tum  ussayaaha .  .  tara%ultra  nmänahe  'paheH.g.xy,  V. IQ.  4,  46,  F.4£;  —  puhnm  yai  'pahe  . . zarahustnm  Yl  5.  18;  V.  jp.  6;  —  mä OtaraySis  saraiustrake  {sXaXXVS.)  mä  'pake (statt  AS.)  mä  duyts.vqm  "erziime  nicht,  ■ oZ.,  den  F.,  nicht  die  Z»."  FrD.  ^;  — I pouru.aspB{sA.Y^ yä^a  'pahe  Vyt2  ";  hz.4.  \
19653:des  Vaters  Zara%uStrM,    zu    dessen  ersten  An>
24612:•  j.  viäaya-  Adj.  'giftig',  als  Subsl.  'giftige  ^  ^^va  'pa  (oder  'psi)  Vyt,  1',  6,  \  g,  lo, Substanz':  :^ar}ianiim  hl*bantqm  'yjalca  ^  jj  /n  's/'',  22  24,  26  28  34,37,  40,43, *vls^aiiitijy.latca  "als  Speisen  soll  ihm  ge- i  ^^^  ^j^  (p^j  —  aiium  'pa  Vyt  Vji  '3, bracht  werden  giftiges  und  nach  G\ii\i,z_2,5.  2)  |  des  Vaters  .Oanajl,  Sohns stinkendes  Zeug"  H.2. 36».  .Jes    Arsäma:     manl    (nämL  Z»ar/w   I.)
27190:•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
=== line 14435-14449 ===
Zum  V.  %viar>s.;  %  igS.  3  b.—  Vgl.  ^varix- ilat:  —  Pii.:  äfrinkar;  s,  noch  No.  I.  — »)  S.  iBed.  Yt.  /.  12;  päyusca  .  .  dälä^a,  femer Y.  tg.  8  und  3g.  6  Pü. 
•  j.  %v/e^-  V.,  nur  Praes.  14  (Inkoh.) *%wqzja-'^  'in  BediUngnis  geraten'.
*^wqzjaiti''>  ahurö  masda paitisa  damqn da%ane  "in  Bedrängnis  gerät  (soll  geraten) AhM.  beim  Schaffen  der  widrigen  Ge- schöpfe" Yt  ig.  58.
ahd.  dwittgan  sl'drängen'.  — Vgl.  aJ>%i(/S.zga' .  — ')  NA.  Prol.  XLivb.  Aus  »t.*tuantgha-,  miti^^ aus  idg. -7i+/.*(A>j  S5jl,  BTHL.Slud.  2,  8,46, Pedeesek  1F.  j.  72,  73  {10  
•  g.  ÖTWisra-  Adj.  'leuchtend*:  t,l  (asmTng
dby  Google
799
Jhwya-
*raoi-
800
(sd.)   -ra  (IS.)   harS  .  .  vainahl  vUpä  Y.
Au»  ar,  *lifiihra- ').  —  ai.  vgl.  hitfum  cakiuh RV.  5.  8.  6;  s.  Bthl.  IF,  /.  49a,  10.  9.  — Pü.: /a  vimilai.  —    ■)  Das  im  Ai.  'iviccira-
•  j.  Jhvyi-  f.  'Schrecknis,  Gefahr";  avi dli  aim  . .  aihim  baräiti  "yqmÜa  Yt  10. 37 ; —  tum  .  .  ma^anam  avi  3^alpaihy/lsf tanvS  'yam  avaiaraht  Vt  10.  sj.
Zum  V.  %iiiay:
•  ].  ÖTvya^stama-  Adj.  'der  schrecklichste, furchtbarste':  yat^a  anhat  Hgmaihi  ata- tfham  yatca  afihat  banhui^  faiti  gairi- nam  yat^a  Jqfnusva  raonam  paxrumalfu (sd.)  nmanaiiu  "
```


## [2026-09-05T05:26:42.888Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Sohn  A%wyas\\|Sohn A%wyas\" BRT.txt; echo \"=== search col 43/44 header ===\"; grep -n \"  43$\\|  44$\\|^43 \\|^44 \" BRT.txt | head; echo \"=== athwya candidates ===\"; grep -nE \"ä[^ ]{0,3}wya-  m\\.|a[^ ]{0,3}wya-  m\\.\" BRT.txt | head"
}
```


### [2026-09-05T05:26:44.932Z] TOOL RESULT

```
14461:*)  Er  ist  in  l^arma  als  Sohn  A%wyas  geboren;
=== search col 43/44 header ===
1172:44  ■■  Vt.  14.  7-
1264:43  ■■  Yt  y:y.  43.  44-
1267:44  :  Yt.  /5. 43-
1357:26  :  Yt.  //.  31,   3S.   39.  43
1406:43  (115);  44(118);  45(123);
1533:44  (134)  :V../.  20.
1556:43  (Uo)-
1623:43  185)  :  V.^.  12,  »4,  x6.  29,
1625:44  (92)  :  V.  6.  49.
1651:43  ("4);  44  (118). 45  (122):  V./.46,  47,  49. 4Ö  (123),  47  (I24):V.7.4S,48.
=== athwya candidates ===
```


## [2026-09-05T05:26:55.892Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD/NYB fredon ===\"; grep -n -i \"frēdōn\\|fredon\\|frētōn\\|Frāsiyāb\" PHD_mackenzie.txt NYB_vol2_glossary.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T05:26:55.942Z] TOOL RESULT

```
=== PHD/NYB fredon ===
```


## [2026-09-05T05:26:57.576Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS ===\"; grep -n -i \"spiyan\\|spyan\\|abtin\\|āptīn\\|Frēdōn\\|fredon\" SNS_pages.txt | head -10; echo \"=== FSF آبتین ===\"; grep -n \"آبتین\\|آتبین\" FSF_pages.txt | head -10"
}
```


### [2026-09-05T05:26:57.651Z] TOOL RESULT

```
=== SNS ===
5806:                   •   o^jTjj^j^jla^aLio^ ^^j^ji :fredon:                                        M>*>
16214:Fredon 135/6
=== FSF آبتین ===
```


## [2026-09-05T05:27:00.517Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5795,5820p' SNS_pages.txt | cut -c1-300"
}
```


### [2026-09-05T05:27:00.563Z] TOOL RESULT

```
                                                                                                                                                 J Jiu* *", »°l 1
                                                                                                                                                                                        '
                                                                                                                                                                                            "»/M
                                                                                                                                                                                            r


                                .   oi-S t>y; . Aijb^ : pardazerld :                             -»»0^




                   •   o^jTjj^j^jla^aLio^ ^^j^ji :fredon:                                        M>*>
 jCM-Stf^C'jk* <ji^ j,J°\-l ;*      £ <SU~ tmS j*^) t^ (aflwya
                                      <                                                  :    /-)



  .^VMiW>- 799)traitana-: ^4*1* flraetaona-: fa-                                                                             J
                                                                                                                                                                    0^:parnigan:                    *~> o
                              U/To ^
                                                                                                                         '
                                                                                                                                     ' *-* Prng n   :   ""*    •«>«*       .^/L^,^
                                                tfotwaZ.                  143.)frydwn                                                                                                               IkJ
```


## [2026-09-05T05:27:11.625Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f ===\"; grep -c \"آبتین\" $f 2>/dev/null; grep -n \"آبتین\" $f 2>/dev/null | head -3 | cut -c1-250; done"
}
```


## [2026-09-05T05:27:12.818Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt; do echo \"=== $f  دده ===\"; grep -n \"دده\" $f 2>/dev/null | head -5 | cut -c1-300; done"
}
```


### [2026-09-05T05:27:13.412Z] TOOL RESULT

```
=== MON_part1.txt ===
0
=== MON_part2.txt ===
1
64130:گس آبتین: (ها آمکین کته یکی 
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt ===
0
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt ===
1
64130:گس آبتین: (ها آمکین کته یکی
```


### [2026-09-05T05:27:15.982Z] TOOL RESULT

```
=== MON_part1.txt  دده ===
3823:کم‌بها دردده دله‌دزد. 
5666:کردار. اندازه» حد» عدده شمار. قاعده» 
6117:معدوم نگردده باقی؛ مق. ازلی. 
8027:احصان؛ حدجدده [ع. ۳ (مسص م ۰) استوار 
9661:محاسبه؛ شناخت خواص عددها. 
=== MON_part2.txt  دده ===
6224:فر ستد» خواهد فرستاد» بفرست: فر‌ستندده 
7128:فریادرسی: 1-.۲-] (حامص.) باری» مدده 
14863:قمیز: عآدده, (تر. مغ.] (.) نوعی شیر ترش 
36913:ایک متخلت رمتعدده به اسو و 
40260:کودکان اعبان؛ لا لا؛ مق. دده (مر سه). 
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt  دده ===
3823:کم‌بها دردده دله‌دزد. 
5666:کردار. اندازه» حد» عدده شمار. قاعده» 
6117:معدوم نگردده باقی؛ مق. ازلی. 
8027:احصان؛ حدجدده [ع. ۳ (مسص م ۰) استوار 
9661:محاسبه؛ شناخت خواص عددها.
```


## [2026-09-05T05:27:24.089Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '40255,40265p' MON_part2.txt | cut -c1-300; echo \"=== BQT دده ===\"; grep -n \"دده\" BQT_v2_pages.txt | head -10 | cut -c1-300"
}
```


### [2026-09-05T05:27:24.152Z] TOOL RESULT

```
بیخ ران تا سر انگشتان پا. (کشتی) فنی است 


از کم : 
له (ه-) نا اد | (.) مربی شاهزادگان و 
کودکان اعبان؛ لا لا؛ مق. دده (مر سه). 
لم: ۷ (.) لمیدن. 
: ۱:0 (۱.) (گیا.) ازملک. (گُیا.) (نو 


ماز ندران) تمشکك. 
=== BQT دده ===
947:‫ونام کلی حم هت وآن در هندوستان‬      ‫باشف ‪-۴‬‬       ‫و بیار‬       ‫دده‬
3441:                  ‫جها نيدده کن‬                       ‫را نیز گویند » و بکراول هم‌امده است‪ -‬ومال‬
6303:                                                                ‫‪ - ۴‬امد دوان دده با‬
7800:              ‫لغت و کنات‬            ‫دده‬           ‫در‬   ‫درجم فارسی با بای حطی فطل‬
8185:                                                    ‫موی وراز گردده وهر که دارندةآ نراببیند‬
13574:                                                                ‫شتنحج اوولل و وئاالی هماآممدده‬        ‫وتی‬
14109:              ‫سلطانيم‬     ‫بنندده بارگاه‬                    ‫‪ - ۴‬من وتو هردو خواجه تاشالیم‬
14946:                            ‫‪ ۴‬اسم مفعول از«خوشیدن»‪.‬‬                     ‫کخیدده‌استعمال شود «واژه نامه ‪.*۱۰۱‬‬
15108:‫گذارند ‪ - ۸‬وبا تحتالی مشددهبعریی زمین دشت‬                                ‫و بسکون ثالی بمعنی خوی است که عرق آدمی‬
15514:‫باشد که ددهت دقع حوای کرم از کتان ساز ند‬                             ‫و آن چنان باشد که‬           ‫نووعی از بازی ههمت‬
```


## [2026-09-05T05:27:31.545Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T05:27:31.551Z] TOOL RESULT

```


```


## [2026-09-05T05:27:35.462Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/átta",
 "prompt": "Give the full reconstruction entry: the reconstructed form, gloss, whether it is described as a nursery/Lallwort, and the full list of descendants (Hittite, Sanskrit, Greek, Latin, Gothic, OHG, Old Church Slavonic, Albanian etc.). Also note any mention of Germanic *aþalaz / OHG adal or Avestan Āθwya."
}
```


## [2026-09-05T05:27:37.796Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/a%C3%BEalaz",
 "prompt": "Give the full entry for Proto-Germanic *aþalaz / *aþalą: meaning, etymology (does it derive from PIE *átta 'father'? or is it of unclear origin / related to *ōþalą?), and descendants including Old High German adal, Old English æþelu."
}
```


### [2026-09-05T05:27:41.324Z] TOOL RESULT

```
# Proto-Indo-European *átta

**Reconstructed Form:** *átta (masculine noun)

**Gloss:** father

**Lallwort Status:** The entry describes it as "Likely a Lallwort," noting comparisons to Proto-Turkic *ata, Proto-Uralic *attɜ, and Proto-Eskimo *ata-ata.

**Descendants Listed:**
- Albanian: atë
- Hittite: attas
- Lydian: ata
- Ancient Greek: átta
- Ossetian: æda (grandfather)
- Assamese: ata (dialectal, grandfather)
- Latin: atta
- Proto-Germanic: *attô (with further descendants)
- Proto-Slavic forms: *otъ, *ota, *otьcь
- Old Irish: aite (foster father, teacher, tutor)

**Notable Omissions:** The page does not mention Germanic *aþalaz, Old Church Slavonic, Old High German forms, Sanskrit descendants beyond Proto-Indo-Iranian notation, or Avestan Āθwya.
```


### [2026-09-05T05:27:43.783Z] TOOL RESULT

```
# Proto-Germanic *aþalaz

**Meaning:** The term means "noble" according to Wiktionary's documentation.

**Etymology:** The entry states it derives from "*aþalą" ("nature; nobility"), though the document doesn't discuss PIE origins or connections to *ōþalą. The source references Vladimir Orel's *Handbook of Germanic Etymology* for this reconstruction.

**Key Descendants:**

The word produced extensive reflexes across Germanic languages:

- **Old High German:** adal (modern German *Adel*)
- **Old Saxon:** *athal* (leading to Middle Low German *adel*, modern Low German *Adel*)
- **Old Frisian:** *athel/ethel* 
- **Old Dutch:** *athal* (becoming Middle Dutch and modern Dutch *adel*)
- **Old Norse:** aðal (Icelandic *aðall*, Faroese *aðal*, Swedish *adel*)

The term also spread beyond Germanic through contact languages, appearing in Estonian *aadel*, Finnish *aateli*, and other borrowings.

The document doesn't explicitly address Old English æþelu, though given the systematic Germanic correspondences shown, it would represent the expected Anglo-Saxon evolution of this root.
```


## [2026-09-05T05:27:46.900Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/a%C3%BEal%C4%85",
 "prompt": "Full entry for Proto-Germanic *aþalą: meaning, etymology — is it connected to PIE *átta or to *ōþalą 'ancestral property', or of uncertain origin? Quote the etymology section."
}
```


## [2026-09-05T05:27:48.836Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/abtin-mid",
 "prompt": "Encyclopaedia Iranica entry ĀBTĪN: give the full text — the Avestan and Middle Persian forms of the name, the etymology, and the relation to Āθwya / Āspiyān."
}
```


### [2026-09-05T05:27:50.813Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:27:51.537Z] TOOL RESULT

```
# Proto-Germanic *aþalą Etymology

Based on the Wiktionary entry, the etymology is uncertain. The entry states:

> "Unknown; possibly from Proto-Indo-European *h₂et-olo- ("family, race")"

The word is hypothesized to derive from PIE *h₂et- ("beyond, over") combined with *h₂el- ("to nourish, grow"), though this remains speculative.

The entry does **not** connect it to PIE *átta. Regarding *ōþalą, the page lists it only as a related term, not as an etymological source. The etymology is ultimately marked as unknown with one proposed but unconfirmed PIE origin.
```


## [2026-09-05T05:27:53.247Z] TOOL CALL #56: WebSearch

```json
{
 "query": "Ābtīn Āθwya Āspiyān father of Ferēdūn Encyclopaedia Iranica etymology"
}
```


### [2026-09-05T05:28:01.826Z] TOOL RESULT

```
Web search results for query: "Ābtīn Āθwya Āspiyān father of Ferēdūn Encyclopaedia Iranica etymology"

Links: [{"title":"ĀBTĪN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/"},{"title":"Tafażżolī, Aḥmad - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/scholar/ahmad-tafazzoli/"},{"title":"FERĒDŪN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/feredu/"},{"title":"AFRĀSĪĀB (PERSON) - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/afrasiab-turanian-king/"},{"title":"Iran Chamber Society: Persian Language & Literature","url":"https://www.iranchamber.com/literature/shahnameh/characters_ferdowsi_shahname.php"},{"title":"FERĒDŪN — Brill","url":"https://referenceworks.brillonline.com/entries/encyclopaedia-iranica-online/feredun-COM_9761"},{"title":"FEREYDŪN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/fereydun/"},{"title":"Abtin — Grokipedia","url":"https://grokipedia.com/page/abtin"}]

Based on the search results from Encyclopaedia Iranica, here's what I found about Ābtīn, the father of Ferēdūn:

## Etymology and Linguistic Development

The name appears in the Avesta (Y. 9.7) as āθwya-, equivalent to Sanskrit āptya-. From it is derived the adjective āθwyānay-, applied to the family of Ferīdūn.

## Name Variants Across Traditions

In Pahlavi literature the name appears as Āswīān or Āsbīān (written ʾspydʾn or ʾspykʾn). In Islamic texts the same form is rendered Āṯfīān. A Pahlavi variant, Ātbīn, is also recorded as the name of Ferīdūn's father, and this, metathesized to Ābtīn, has come down in the Šāhnāma.

## Genealogy

Ferēdūn is identified as the son of Ābtīn, a descendant of Jamšēd, and of Farānak.

The search results show that the name has a continuous etymological line from the Avestan āθwya-, through various Pahlavi forms, to the modern Persian Ābtīn found in Ferdowsi's Šāhnāma.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T05:28:09.992Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/",
 "prompt": "Give the complete text of the Encyclopaedia Iranica article ĀBTĪN, including the Avestan form, the Sanskrit equivalent, the Pahlavi spellings, the metathesis explanation, and the author/bibliography."
}
```


### [2026-09-05T05:28:11.598Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T05:28:11.782Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%AF%D9%87",
 "prompt": "Give the Persian entry for دده: pronunciation, etymology, and all senses/meanings. Does it mean 'nurse', 'elder sister', 'grandfather', or 'aunt'? Is it linked to a nursery word or to Turkish dede 'grandfather'?"
}
```


### [2026-09-05T05:28:17.536Z] TOOL RESULT

```
# Persian Entry for دده

**Pronunciation:** /da.ˈda/ (Classical Persian); [d̪ä.d̪á] (Dari, formal); [d̪æ.d̪é] (Iran, formal)

**Etymology:** A babble word (not derived from Turkish)

**Senses:**
1. Sister (blood relative)
2. Sister/sis (form of address for women of similar age)
3. Maidservant/housemaid (historical)
4. Female slave (historical)

**Answer:** The word means "sister" primarily, though historically it also referred to "maidservant" or "female slave." It is **not** linked to Turkish *dede* ("grandfather"). Rather, the Persian دده originates as "a babble word," making it distinct from the Turkic term etymologically.
```


## [2026-09-05T05:28:24.122Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dad",
 "prompt": "Give the full etymology of 'dad' and 'daddy' — the date of first attestation, the explanation of it as a nursery/child's word, and the comparanda in Welsh, Irish, Lithuanian, Greek, Latin, Sanskrit."
}
```


## [2026-09-05T05:28:26.011Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%84%CE%AE%CE%B8%CE%B7",
 "prompt": "Give the Ancient Greek entry for τήθη: meaning, etymology, and related forms (τηθίς, Τηθύς). Does it mean grandmother or father/grandfather?"
}
```


### [2026-09-05T05:28:30.374Z] TOOL RESULT

```
# Etymology of "Dad" and "Daddy"

## Dad
**First Attestation:** circa 1500

**Origin:** The word derives from child's speech and is "probably much older" and "probably prehistoric" in origin.

**Explanation:** It functions as a nursery word for father, with the note that such terms are "nearly universal" across languages.

**Comparanda:** The entry lists related forms across multiple languages:
- Welsh: *tad*
- Irish: *daid*
- Lithuanian: *tėtė*
- Sanskrit: *tatah*
- Czech: *tata*
- Latin: *tata*
- Greek: *tata* (used by youths addressing elders)

## Daddy
**First Attestation:** circa 1500

**Origin:** A "colloquial diminutive of dad, with -y" suffix.

**Additional Notes:** The slang term "daddy-o" emerged by 1949 from bop talk. "Daddy-long-legs" appeared in British usage from 1814 (crane-fly reference) and in American usage by 1865 (arachnid reference).

The entry emphasizes that these paternal terms represent a widespread linguistic pattern found across Indo-European and other language families, suggesting deep historical roots in child-directed speech.
```


### [2026-09-05T05:28:31.415Z] TOOL RESULT

```
# τήθη (Ancient Greek)

**Meaning:** τήθη means "grandmother," not grandfather or father.

**Etymology:** The word derives from Proto-Indo-European *dʰeh₁dʰ- ("grandparent"). It shares cognates with Proto-Slavic *dědъ ("grandfather"), Lithuanian dė̃dė ("uncle"), and Latvian dȩ̀ds ("old man"). The term likely originated as baby talk.

**Related Forms:**
- τηθίς (tēthíc) — a derived term
- τηθία (tēthía) — another derivative
- The synonym is μάμμη (mắmmē)

**Distinction:** In the family terminology table, τήθη occupies the "grandmother" position under "grandparent," while πάππος (páppos) represents "grandfather." The noun is feminine, first-declension, and was used specifically for one's paternal or maternal grandmother in ancient Greece.
```


## [2026-09-05T05:28:40.366Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Adolf",
 "prompt": "Etymology of the name Adolf/Adolph: the Old High German source (Adalwolf / Athalwolf), the elements adal 'noble' and wolf, and any Proto-Germanic reconstruction given."
}
```


## [2026-09-05T05:28:41.434Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Albert",
 "prompt": "Etymology of the name Albert: Old High German Adalbert / Adalberht, the elements adal 'noble' and beraht 'bright', and the route into English (via French / Old English Æþelberht)."
}
```


### [2026-09-05T05:28:45.978Z] TOOL RESULT

```
# Etymology of Adolf/Adolph

The name Adolf derives from Old High German elements combining nobility with animalistic power.

**Source Components:**
The name comes from Old High German *adal* ("noble") + *wulf* ("wolf"), creating a compound meaning roughly "noble wolf." As the Wiktionary entry states: "From Old High German _adal_ ("noble") + _wulf_ ("wolf")."

**Related Forms:**
English has a doublet called Ethelwolf, which descended from Old English *Æþelwulf*, showing how the same Germanic roots evolved differently across language families.

**Proto-Germanic Background:**
While the document doesn't explicitly provide a Proto-Germanic reconstruction, it confirms the Old High German origin, suggesting the name traces to early Germanic naming conventions that favored combinations of prestigious qualities (nobility) with powerful animals (wolves).

**Modern Usage Note:**
Interestingly, the name's popularity peaked between 1890-1905, then declined sharply after World War II due to historical associations, becoming "very rare" in modern usage across Germanic-speaking regions.
```


### [2026-09-05T05:28:46.348Z] TOOL RESULT

```
# Etymology of Albert

The name Albert derives from Old High German *Adalbert*, combining two elements: **adal** (noble) and **beraht** (bright). 

The name entered English through multiple routes. It came via Old English *Æþelbeorht*, as well as through Old French and Latin *Albertus*, which itself derived from the Germanic source. As the Wiktionary entry notes, "It became popular in 19th-century England due to Queen Victoria's consort, Prince Albert of Saxe-Coburg-Gotha."

The name is also "a doublet of *Ethelbert*," meaning both names share the same ultimate Germanic origin despite their different forms in English.
```


## [2026-09-05T05:28:52.974Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/' --note 'page 68, root Atos, entry ABTIN: Avestan athwya-, Pahlavi Aswian/Asbian, Atbin > Abtin metathesis' 2>&1 | tail -20"
}
```


### [2026-09-05T05:29:05.442Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c752bbfdf2b9d05.txt
```


## [2026-09-05T05:29:07.649Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -i -A5 -B5 \"athwya\\|Ātbīn\\|Atbin\\|metathes\\|Āsbīān\\|Aswian\" data/verification/sources/web/5c752bbfdf2b9d05.txt | head -60"
}
```


### [2026-09-05T05:29:07.706Z] TOOL RESULT

```
 Print

 cite 
 share 

 ĀBTĪN (in poetry, ĀBETĪN), father of the mythical king Ferīdūn (Av. Thraētaona) of the Pīšdādī dynasty. The name appears in the Avesta (Y. 9.7) as āθwya- , equivalent to Skt. āptya- . From it is derived the adjective āθwyānay- , applied to the family of Ferīdūn. In Pahlavi literature the latter appears as the name of Ferīdūn’s father in the form Āswīān or Āsbīān (written ʾspydʾn or ʾspykʾn;Dēnkard , pp. 319.19, 438.15; Zātspram , p. 53.12). In Islamic texts the same form is rendered Āṯfīān (Ṭabarī, I, p. 205; Bīrūnī, Āṯār al-bāqīa , p. 104; Ḥamza Eṣfahānī, Senī molūk al-arż , Beirut, 1961, pp. 17, 27; Moǰmal , pp. 13, 26, 27). A Pahlavi variant, Ātbīn, is also recorded as the name of Ferīdūn’s father ( Pahl. Texts , p. 23.8); and this, metathesized to Ābtīn, has come down in the Šāhnāma (Moscow, I, p. 57. 117f. ) and the Moǰmal (p. 25). In this latter work (pp. 25, 27) the name of Aṯfīān’s father is given as Homāyūn (variant: *Nunak, nwnk ). However, this genealogy does not occur in the older sources.
 The Bundahišn ( Bd. , p. 229.4; ms TD 1 , ed. P. Anklesaria, Tehran, 1349 Š./1970, fol. 98r.3) states that there are ten generations from Jamšīd to Ferīdūn in addition to Asbīān-e Porgāv (the name given to Ferīdūn’s father); but it actually names only eight persons. According to this tradition, each of the ten ancestors lived for 100 years; and the span of their lives coincided with Żaḥḥāk’s thousand year reign. Zātspram (p. 54.1) also preserves the tradition of these ten generations, while the names of all ten ancestors are provided in the Dēnkard (p. 613.16), Ṭabarī (I, pp. 227f. ), and the Fārsnāma of Ebn al-Balḵī (p. 11). Bīrūnī’s Āṯār al-bāqīa (p. 104) names only eight. By a comparison of these various lists, Ferīdūn’s genealogy can be readily reconstructed. It follows, in reverse order, the forms in Ṭabarī coming first, those in the Dēnkard and Bundahišn in parenthesis. Each name is preceded by the patronymic Aṯfīān: 1. Aṯfīān Porgāv (Asbīān or Aswīān Porgāv), 2. Aṯfīān Nēkgāv or Nēvgāv (Nēkgāw Asbīān, only in the Dk .), 3. Aṯfīān Sōgāv (Asbīān Sōggāw), 4. Aṯfīān Bōrgāv (Asbīān Bōrgāw), 5. Aṯfīān Aḵšīngāv ( Dk. only, Kerdārgāw Asbīān; Fārsnāma: Gōrgāv), 6. Aṯfīān Sīāhgāv (Asbīān Sīāgāw), 7. Aṯfīān Esbēdgāv, also written Esbādgāv and pronounced with the emāla (Asbīān Spēdgāw), 8. Aṯfīān Kabargāv, for Dabrgāv (Asbīān Dabrgāw), 9. Aṯfīān Ramēngāv, for Ramakgāv (Asbīān Ramakgāw), 10. Aṯfīān Banfrawešn (Asbīān Wanfrawišn), 11. Asbīān, son of Jamšīd. This last name occurs only in the Bundahišn, and is very likely a spurious, late addition to the traditional genealogy.

 Bibliography
 See also Justi, Namenbuch , pp. 49-50.
```


## [2026-09-05T05:29:13.354Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/átta' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalaz' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalą' \\\n 'https://en.wiktionary.org/wiki/دده' \\\n 'https://en.wiktionary.org/wiki/τήθη' \\\n 'https://www.etymonline.com/word/dad' \\\n 'https://en.wiktionary.org/wiki/Albert' \\\n 'https://en.wiktionary.org/wiki/Adolf' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 68, root Atos/Atta/Athal verification' 2>&1 | tail -1\ndone"
}
```


### [2026-09-05T05:29:17.952Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7a80f66e235110f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/653f661ad1dc4584.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03e659711f2f63fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/160246b6c382fe6a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/878573f66ecb7ba1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fd4d48a2093da72.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb79245677bba27e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4e7fabbff16daed.txt
```


## [2026-09-05T05:29:29.811Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A4%BE%E0%A4%A4",
 "prompt": "Sanskrit तात (tāta): meaning(s), etymology (nursery word? from PIE *tata?), and usage. Does it mean 'father', 'grandfather', or a term of endearment?"
}
```


## [2026-09-05T05:29:31.592Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY latin index ===\"; grep -n -i \"ABTIN\\|DADEH\\|DADE\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY persian ===\"; grep -n \"آبتین\\|دده\" incoming/ARY/ARY_pages.txt | head -10 | cut -c1-200"
}
```


### [2026-09-05T05:29:31.666Z] TOOL RESULT

```
=== ARY latin index ===
=== ARY persian ===
```


### [2026-09-05T05:29:36.370Z] TOOL RESULT

```
# तात (Tāta): Etymology and Meanings

## Primary Meanings

In Sanskrit, तात (tāta) functions as a masculine noun with two main definitions:

1. **"daddy, papa"** - a direct familial term
2. **A vocative term of affection** - used when addressing juniors or seniors, or multiple persons

## Etymology

The word has two distinct etymological paths depending on context:

**As "father":** The Hindi adjective तात derives from Sanskrit तप्त (taptá), tracing back through Proto-Indo-European *tep- ("to be warm"), though this etymology seems semantically distant from the familial meaning.

**As a nursery word:** The Sanskrit noun तात is explicitly described as **"onomatopoeic, mimicking baby talk."** This etymology compares it to Latin *tata* and Ancient Greek *τατᾶ* (tatâ), suggesting shared Indo-European baby-talk origins.

## Linguistic Classification

तात appears in Sanskrit as an **a-stem masculine noun** with full declension patterns. The word is notably a **palindrome** in both Hindi and Sanskrit forms.

The onomatopoetic nature—characteristic of how infants and caregivers universally produce similar sounds across languages—best explains this term's presence across multiple language families.
```


## [2026-09-05T05:29:44.780Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D8%AF%D9%87/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for دده verbatim, plus لغت‌نامه دهخدا if present. What senses does Mo'in give and does he tag an origin?"
}
```


## [2026-09-05T05:29:47.224Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSF بتین ===\"; grep -n \"بتین\\|فریدون\" FSF_pages.txt | head -8 | cut -c1-250; echo \"=== PHD aspiyan variants ===\"; grep -n -i \"spyʾn\\|ʾspyd\\|Ābtīn\\|Frēdōn\\|Frēton\" PHD_mackenzie.txt NYB_vol2_glossary.txt UNV.txt 2>/dev/null | head"
}
```


### [2026-09-05T05:29:47.337Z] TOOL RESULT

```
=== FSF بتین ===
656:               ‫از مسعود سعد (دیوان (‪Ff‬‏‬               ‫مهرگان جشن فریدونست و او راحرمتست‬
2201: ‫فریدون بهکاخت آمدو برتخت نشست و‪:‬‬                       ‫(‪)۷-۴۱۴-۱۳۹۱‬‬
2212:        ‫همه بند و نیرنگ از رنگ برد‬                      ‫(فریدون) زسالش چویک ینجه‌اندرکشید‬
2558:           ‫ز پیش فریدون چنان بازگشت‬               ‫کلم نداو خحطاب است بهمعنی ایاءای؛ و‬
2997:‫دوم آنکه مصراع دوم اینبیت بدان شکل‬            ‫فردوسی است و در داستان فریدون و سه‬
2998: ‫که در فرهنگ‌های نامبره امده است» یعنی‬         ‫پسرش آمده است‪ .‬پس از آنکه فریدون‬
3008:‫فریدون در نامه خود به‌سلم و تور به‬             ‫فریدون به خواهش ایرج که حاضر است‬
3596:                                                ‫کزان بارورتر فریدون نکشت‬
=== PHD aspiyan variants ===
```


### [2026-09-05T05:29:53.740Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for دده

According to the dictionary section labeled "فرهنگ معین," Mo'in provides these definitions:

**(دَ دَ)** [marked as Turkish origin - تُر.]: "a female caretaker of children; a nursemaid" (plural: ددگان، دادگان)

**(دَ دِ)** [marked as Pashto origin - په.]: 
1. "a wild/ferocious animal"
2. "a dervish/ascetic"

Mo'in explicitly tags the first sense as Turkish ("تُر.") and the second set as Pashto ("په."), indicating recognized foreign etymologies.

**Regarding Dehkhoda:** The "لغت‌نامه دهخدا" section appears extensively in the document with historical Persian literary examples and etymological discussions, but presents the primary historical sense as a fierce/wild animal (درنده) with later semantic extensions to familial terms and caretakers.
```


## [2026-09-05T05:30:08.361Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/دده/' --note 'page 68, node 12: Moin entry for دده — tagged [تر.] Turkish, meaning dāya/nursemaid' 2>&1 | tail -1; ls site/pages/68.jpg 2>/dev/null || echo \"no jpg\""
}
```


### [2026-09-05T05:30:11.294Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/83c7c80ad7e7df9c.txt
site/pages/68.jpg
```


## [2026-09-05T05:30:12.722Z] TOOL CALL #71: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/68.jpg"
}
```


### [2026-09-05T05:30:12.764Z] TOOL RESULT

```

```


## [2026-09-05T05:30:28.643Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"آبتین\\|آتبین\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt 2>/dev/null | head -5 | cut -c1-250; echo \"=== HRN/HUB dade ===\"; grep -n -i \"dade\\b\\|dâde\\|dada \" HRN.txt HUB.txt 2>/dev/null | head -8 | cut -c1-200"
}
```


### [2026-09-05T05:30:28.736Z] TOOL RESULT

```
BQT_v1_pages.txt:6483:و بنای‌این سحیح دآتبین» است که ناسخان در رس‌الخط آنرا به ۶ آبتین * تبدی لکرده‌اند . اما در
BQT_alt_v1.txt:10085:و بنابراین صحیح «آتبین» | دک اس ما زا دما اج 
BQT_alt_v1.txt:10086:ساسکریت 800128 بانشدیم باه فارسی برتاء آمده < بارتولمه ۳۷۳ » و بنابراین آبتین نیزمحملی 
BQT_v1.txt:10973:و بنای‌این سحیح دآتبین» است که ناسخان در رس‌الخط آنرا به ۶ آبتین * تبدی لکرده‌اند . اما در 
=== HRN/HUB dade ===
```


## [2026-09-05T05:30:31.932Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6470,6495p' BQT_v1_pages.txt | cut -c1-400; echo \"======= alt =======\"; sed -n '10075,10095p' BQT_alt_v1.txt | cut -c1-400"
}
```


### [2026-09-05T05:30:32.007Z] TOOL RESULT

```
(۳) خم ۳ : شرار؛ آش و سرشلك وا .
(٩)خم‏ ۲ : قرشت .
۹
پر جیحون را ابرانیان در قرون وسطی ۶ به رود *مینامیدند و این اسم » صفت اوستالی ونگوهی
نت۷۵8 (به ‏ خوب ) میباش د که اغلب برای رود « دایتی ‏ آمده است . در شدهش مکرر
دوم روت )۷۵-۲۵ » ( به رود ) باد شدداست. « نا ص۵۲ » .آبهی ظاهراً مخفف < ,آب‌بهی»
است بمعنی لفوی < به رود » ( از افادات آقای پور داود ) . ۲ موجه‌اناه عن6۷۵082
ابتی ٩۱۵۷‏ ,« کل کلاب ۲۲۷ 6 ۰ ۴ - درکتاب حاضرلیز داییز».و «آبیژ» همینستی آمیه ‏
در پیش فرهثگها «آیده را بمعنی مرحك , آب شم . اشك و دمع هم نوشته‌اند و ظاهراً معنی
کي او فان زب ت ناشی از کلمة سرشك آش . «لفت‌نادد». ۴ - ترديك دارابگرد .
موف برهان در «آبین» یز همین مفتی را آورده‌انت « لقت‌نافه * و بیرونی دالجنامر( ص‌
۶ ) در ذکر مومیالی گومد : « تردبكك آن ( غار دارابجرد ) فربه ات ممی بنه آیین ؛ و
مومیابی بدان‌منشسوبست وآنرا مومآ ین گونند. ‏ ۷ - در اوستا 800۷012 نام پدرفربدون است
و بنای‌این سحیح دآتبین» است که ناسخان در رس‌الخط آنرا به ۶ آبتین * تبدی لکرده‌اند . اما در
ساسکریت 8۵396 باهدیم باه فارسی برتاء آمده « بارتولمه ۳۹۳ * و بنابراین آبنین نیزمحملی
پیداکند. طبری «افربذون بن ائفیان» «ج ۱ ص٩۹‏ »» بیرونی « ائفیان » « آثارالبافیه۷۲۲۹ *»
مجمل‌النواریخ والصص ض ۲٩‏ < انقیال << انفیان » , شاهناسه « آنبین » « شاهنامةٌ جخ ج ۱ :
( ۷ - این مستی مأخون از دساتیر است . « فرهنگه دساتیر ۲۳۰ ٩‏ .
- ارستا »قا۵ و 0اتقاث , پهلوی تلا , ۵ دیب رکه ۱: ۲۵ و ۳4 و نصا
هه درصفحه 4 ۱2 دب۱ آخن آب پرود ۱ ۱ اه
کیره راگونند ؛ یمنی حرچی ز که بدان آش
افروزند همچو خس و خاشالك-و مانند آن - و
چتماق را نز کفتداند . #
]آتش پادسی (۲)- ه پکس رایع »
مرضی است غبر آنفك مشهور آنرا بعربی تلر
فارسی خوانند ا بسن کوند آتك فرنگ (۳)
======= alt =======
۷۵۷0۲1 (به - خوب ) میباشدکه اغلب برای رود « دایتی » آهده است . در بندهش سکرر 
د وم روت )۷6-۲۵ » ( به رود ) باد شده‌است. « یسنا ص۵۲ » .آبهی ظاهراً مخفف < آب‌بهی» 
است بمعنی لفوی « به رود » ( از افادات آقای پور داود ) ۰ ۴ - 0۵اه 67002 
« ثایثی ٩۱۵۷‏ .«ک لکلاب ۲۲۷ ۰ ۴ - درکتاب حاضرلیز «اییز».و «آییژ» همی‌ستی آمده ‏ 
در بعض فرهنگها <آییده را بمعنی مر‌خك , آب چشم . اشك و دمع هم بوشته‌اند و ظاهر؟ معنی 
اخیر اشتباه و غلعلی است ناثی از کلمةٌ سرشك آش . «لفت‌نامه». 2 

۵ نوف برهان در «آبین» یز همین مفتی را آورده‌انت ۶ لقت‌نامه * و بیرونی درالجناعر (س 
۶ ) در ذکر مومیالی گومد ی ی وج ی 
مومیایی بدان‌منوبت وآلرا موم‌آیین گویند. ‏ ۷ - در اوستا 8111۷07/2 نام پدرفیبدون است 
و بنابراین صحیح «آتبین» | دک اس ما زا دما اج 
ساسکریت 800128 بانشدیم باه فارسی برتاء آمده < بارتولمه ۳۷۳ » و بنابراین آبتین نیزمحملی 
پیداکند. طبری «افرمذون بن ائفیان» «ج ۱ س۹۸ ۴ بیرونی د ائقیان » « آثارالبافیه۲۲۹ »۰ 
مجمل‌اتواري والصص سس ۲٩‏ < انیال - نان » , شاعتاسه « ین » « شاعنمً بغ ج ۱ : 
ِِ ۷ - این معنی مأخوذ از دساتیر است . « فرهنکه دساتیر ۷۲۳۰ ٩‏ . 

اوستا تصاق و تاعتها8 ء پهلوی تداا۵ , 875 دیب رکه ۱ : ۷۵ و ۳۶ و تاقصاا 


هه درمضعهٌ ۱8 -.
```


## [2026-09-05T05:30:57.580Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT ===\"; grep -n -i \"aptya\\|athwya\\|Thraetaona\\|Fredon\" KNT.txt | head -5; echo \"=== SKT dad/atheling ===\"; grep -n -i \"^dad\\|atheling\\|^Adolphus\\|noble.*wolf\" SKT.txt | head -8 | cut -c1-250; echo \"=== LEW tata ===\"; grep -n \"tata\" LEW_1910.txt | head -6 | cut -c1-250; echo \"=== LAT tata ===\"; grep -n \"tata\" LAT.txt | head -6 | cut -c1-250"
}
```


### [2026-09-05T05:30:57.679Z] TOOL RESULT

```
=== KNT ===
=== SKT dad/atheling ===
4638:Dad    (C*     VV.  tad  Irish  daid^  Hret.  /«/, /*/.  father -fCk.  T'"n,  Skt.  ftiJd  dad.
23987:Dado.  (Ital.  — L.)  Formerly  used  of the  die,  or  square  part  in  the  middle  of  the pedestal  of  a  column ;  afterwards  applied to  the  pore  of  an  apartment  between  the plinth  and  the  impost  moulding.  O.  Ital. dttdoy
=== LEW tata ===
226:Ammat I 39 amnud I 36, II 210 ampert I 686, II 284, 285 amprufid I 686, II 364, 366 ampt I 36 ampu<bulum I 46, 546 Apunuco I 45 amviannud I 36, IGEYAS an- I 686 avaSaxet I 43, 440 Anafriss I 681,687 Anagtiai I 47, 693 anamum I 49 ancensto I 199, 
227:brateis I 619, II 75 Boatmp I 619 “6 Ih IY cadets I 136, 178 kahad I 188, 631 xakac I 188 katas I 129, 137 katla I 131, 187 kaispatar I 134, 853 Kalaviis, Kalivieis I 144 xamitop I 160 karanter I 168, 170, 204 carta, carneis I 170 kasit I 167 c
816:takart II 645 taksaka- II 653 taksati, taksan- II 678 tata-h ,,Ufer“* IT 655 tatd- ,,gestreckt“
838:tata-h II 650
1719:Reihenfolge des Alphabets: 4, 7, a; k, x, qY; ¢; if t, 0, ¢, d, n; p, f, b, m; Y¥, iy Us DE SS Gy BE We a I 642 a-, an- I 686 aitiy I 407 aistata II 548 Ayawpmévne II 551 dyyagos I 46 atiy- I 75, 421 adakaiy I 30 adada I 441 adanah II 176 ad
1721:zyam I 720 uta, uta I 31 udapatata IT 298 upariy II 616 kaufa- I 311 xamtOn I 159 kama- I 175 kara- I 169 zauda- I 301 asadram IT 481 xsapa I 289 xwsnasatiy II 176 gausa I 644 garmapada- I 532 éa IT 401 cistiy II 410 éiy I 3810, II 406, 410 j
=== LAT tata ===
3579:-in; cf. fatim tire de ad fatim: et emussitata employ 4 par Plaute, Mil.
3658:anclabris, -e: - mensa, ministeriis aptata diuinis. Vasa quoque in
4454:apostata, -ae m. : emprunt de la 1 . de l'Agl. au gr. a. 7 iooTaTr]C; de IA
5486:cinerea et rabuscula et asinusca, *inus tamen caudas uulpium imitata
5809:lat. tata et, pour le type, lat. amma.
5824:empruntees: attatae, dttattatae.
```


## [2026-09-05T05:31:03.047Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5800,5830p' LAT.txt | cut -c1-400; echo \"=== LAT tata headword ===\"; grep -n \"^tata\\|tata, -ae\\|tata:\" LAT.txt | head"
}
```


### [2026-09-05T05:31:03.116Z] TOOL RESULT

```
qui anrait servi a former des adjectifs de sens analogue aux adjectifs
en ~ax: cf. uelox corne capax; cf. toutefois Ernout, Philologica, p.156,
et Brugmann, Grdr. II i, p.501, § 383.
atta, -ae m. : grand-pbre, on plutot ,: grand-papa". Attat 1 pro reueren-
tia seni cuilibet dicimus, quasi eum aui nomine appellemus, P.F.n,ao.
Mot du langage enfantin, qu'on retrouve sans doute dans atauus.
L'un des nons faniliers du "pfere" ( p)iter etait un non solennel, a
forte valeur juridique et religieuse). Cf. gr. axxtx, got. atta (deriv^
en *-en~), v.sl. ot tct (derive en *- iko- ), alb. at . - Cf. le groupe de
lat. tata et, pour le type, lat. amma.
attae: appellantur qui propter uitium crurum aut pedum plantis in¬
sistunt et adtingunt terram magis quam ambulant, quod cognomen Quintio poetae
adhaesit , P.F.11,17. Mot de type populaire a vocalisme a (cf .uatia,
pansa), e t qui aune consonne geminee comme beaucoup d’adjectifs marquant
une difformit^. N’est atteste que comme cognomen; cf. Attus, Attius.
attagena, -ae f. : g^linotte des bois. Forne latinis^e de axrtXYnv,
tiree de l'acc. grec. Horaee, Epod.2,54, emploie attagen.
attamino: v. contamini).
attanus: v. atalla.
attat {attat Pl. Au.713, sans doute avec allongement "emphatique",
cf. Hofmann, Latein.Umgangsspr. p.11): interjection marquant 1 'etonne-
ment a 1 'aspect d'une chose dont on s'aper5oit. Diom., GLK I 419,1, ex
improuiso aliquid deprehendentem (significat interiectio). Le grec a
de» formes axxaxai, axxaxaxou (<xxxocxou,aJ;) que la comedie latine a
empruntees: attatae, dttattatae.
L'existence de la forme rencontree en grec donne a supposer que
attat doit etre lui aussi emprunte. Mais il ne semble pas que axxax
soit atteste. En tout cas, 1 1 explication de l.Havet, Manuel § «96,qui
voit dans attat le redoublement de at(t) ne concorde pas aveclesens
de 1 1 inter j ection, et n 1 explique pas les formes attatae, attattatae.
attegia, -ae f.: hutte, cabane. Premier ex. dans Juv^nal, Sat.14,
=== LAT tata headword ===
4454:apostata, -ae m. : emprunt de la 1 . de l'Agl. au gr. a. 7 iooTaTr]C; de IA
18747:emussitata: v. amussis.
63105:tata, -ae m.: papa. Mot enfantin, cite par Varr. ap.Non.81,3,
72082:tatana, tatne, 1206.
81967:tata pol., 1195.
```


## [2026-09-05T05:31:05.483Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '63105,63120p' LAT.txt | cut -c1-400"
}
```


### [2026-09-05T05:31:05.539Z] TOOL RESULT

```
tata, -ae m.: papa. Mot enfantin, cite par Varr. ap.Non.81,3,
et atteste epigraphiquement, ainsi que tatula, CIL VI 35636, cf.
mamma, pappa. M.L.85y6. Cf. Tatius?
Y.atta. Cf.gr. Taxa, corn. tat (avec ancien t gemine), pol. tata
(ou a represente a). Sur tout le groupe, v.W.Heraeus, Kleine Schrift.,
p.163 et s.
taurus, -I m.: taureau. Nom d'une constellation du zodiaque.
S'applique a des animaux ou a. des objets qui rappellent par 1 -eur
cri, leur aspect, etc., le taureau: butor (oiseau), Plin.10,116; frelon
(scarabee), Plin.30,3y; racine d'arbre (Quint.8,3,13). Designe aussi
le p 4 rinee (ou plus exactement les testicules?) dans une victime,
cf.F.373,31, atque harum hostiarum inuiolati sunt tauri quae pars
scilicet caeditur in castratione; et Diom., GLK I 450,8, et en gr.tautanus
1196 -
1 1 emploi de xccupog (Poli. 3,173). Pe taurus a et 4 cr 4 e un f 4 m. taura
dans la 1 . rustique (Varr., Coi.), cf. P.F.481,1, tauras uaccas steriles ...
```


## [2026-09-05T05:31:17.096Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T05:31:17.161Z] TOOL RESULT

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


## [2026-09-05T05:32:21.136Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/तात' --note 'page 68, node 7: Sanskrit tāta — nursery word, daddy/papa' 2>&1 | tail -1"
}
```


### [2026-09-05T05:32:23.182Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e9455d475dc0066b.txt
```


## [2026-09-05T05:34:26.657Z] AGENT

Now I'll write the verification file.


## [2026-09-05T05:40:45.020Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-68.json <<'JSONEOF'\n{\n  \"pdf_page\": 68,\n  \"book_page\": 38,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Âtos, Atta, Ato, Athal\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *átta 'father' (a Lallwort / nursery word); Pokorny IEW 71 'atos, atta Lallwort \\\"Vater, Mutter\\\"', with the derivative *āto-s underlying Gmc. *aþala- 'noble descent'\",\n      \"note\": \"The root box is a faithful copy of Pokorny p. 71, which is exactly what Nourai cites. Pokorny's headword is 'atos, atta Lallwort \\\"Vater, Mutter\\\"' — hence the language label (Indo-European) and the gloss 'father, mother' are right, and 'family, race' comes from the second half of the same entry, 'Ein ähnliches *āto-s in germ. *aþala-, *ōþela- scheint auch die Grundlage von ahd. adal \\\"Geschlecht\\\", nhd. Adel'. Two reservations keep this from 'confirmed'. (1) The fourth name in the box, 'Ato', is not an independent root anywhere: it is Pokorny's *āto-s, i.e. the same etymon in lengthened grade, and 'Athal' is a Germanic, not an Indo-European, form. (2) Modern handbooks decline the merger. Watkins/AHD splits the material into two entries — 'atto-. Father (nursery word). Possibly Latin atta … [In Pok. atos 71.]' and '[athal-. Race, family. Germanic root, possibly related to Greek atallein, to foster … [In Pok. atos 71.]]' (the square brackets in Watkins mark a non-PIE, Germanic-only root) — and Wiktionary/Orel derive PGmc. *aþalą from *h₂et-olo- 'family, race' (*h₂et- + *h₂el-), with no link to *átta at all. Above all, Pokorny himself ends the entry 'Ein auf den verschiedensten Sprachgebieten sich stets neu bildendes Lallwort (z. B. elam. atta, magy. atya \\\"Vater\\\", türk. ata, bask. aita ds.). Ähnlich tata.' — a word constantly re-created, so 'descent' in the ordinary sense is not what the arrows on this chart can mean.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *átta «پدر»؛ پوکورنی (ص ۷۱) آن را با عنوان «atos, atta واژهٔ کودکانه (Lallwort): پدر، مادر» آورده است، پس برچسب زبانی و معنای «پدر، مادر» در نمودار درست است و «خاندان، نژاد» نیز از بخش دوم همان مدخل («*āto-s در ژرمنی *aþala- که پایهٔ ahd. adal «تبار» و آلمانی Adel است») گرفته شده. دو نکته: نخست آنکه «Ato» ریشهٔ مستقلی نیست بلکه همان صورت با واکهٔ کشیده است و «Athal» صورتی ژرمنی است نه هندواروپایی؛ دوم آنکه ریشه‌شناسی امروزی این یکی‌سازی را نمی‌پذیرد — واتکینز در پیوست AHD دو مدخل جداگانهٔ atto- و [athal-] دارد و [athal-] را «ریشهٔ ژرمنی» می‌نامد، و ویکی‌واژه *aþalą ژرمنی را از *h₂et-olo- می‌گیرد نه از *átta. مهم‌تر اینکه خود پوکورنی تصریح می‌کند این واژه‌ای کودکانه است که در هر زبانی از نو ساخته می‌شود (مانند ata ترکی و aita باسکی)، و «tata نیز همانند آن است» — یعنی رابطهٔ «اشتقاق» به معنای متعارف در اینجا برقرار نیست. ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/átta\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalaz\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalą\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:71\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 80 (= printed p. 71, offset leaf = p+8): 'atos, atta Lallwort ,Vater, Mutter‘. Ai. attā ,Mutter, ältere Schwester‘ … lat. atta m. ,Vater‘, got. atta ,Vater‘ … hett. at-ta-as (attas) ,Vater‘. Ein ähnliches *āto-s in germ. *aþala, *ōþela scheint auch die Grundlage von ahd. adal ,Geschlecht‘, nhd. Adel … Ein auf den verschiedensten Sprachgebieten sich stets neu bildendes Lallwort … Ähnlich tata. WP. I 44'. Headword, language label and gloss are exactly Nourai's.\"},\n        {\"ref\": \"AHD:1507\", \"status\": \"partial\", \"note\": \"Nourai's page number is in the 1976 New College appendix, which is not open online; the 1985 Watkins standalone (AHD_watkins1985.txt) has the same root list. Line 301: 'atto-. Father (nursery word). Possibly Latin atta, father: ATAVISM. [In Pok. atos 71.]' and line 300: '[athal-. Race, family. Germanic root, possibly related to Greek atallein, to foster. 1. Germanic *athal- in Old English ætheling, prince: ATHELING. 2. Variant Germanic *ōthel- in Old High German edili, noble: EDELWEISS. [In Pok. atos 71.]]'. AHD therefore has the material Nourai cites but keeps it in two entries and marks athal- as Germanic-only, not PIE.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW p. 71 (POK_01.txt leaf 80; POK_full.txt line 9390 'Root / lemma: atos, atta (hatta), Meaning: father, mother')\", \"stance\": \"supports\", \"note\": \"'atos, atta Lallwort ,Vater, Mutter‘ … Ähnlich tata.' Supports the root and its gloss, but flags it as a nursery word and keeps *tata separate.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 44 (WLD_Bd1_pages.txt leaf 53; printed = leaf − 9)\", \"stance\": \"supports\", \"note\": \"'atta Lallwort ,Vater, Mutter‘. ai. atta ,Mutter, ältere Schwester‘ … Ein ähnliches *ato-s, germ. *aþala-, *oþela- ,väterliches‘ scheint nach Schrader IA. 9, 172, RL. 815 auch die Grundlage von ahd. adal ,Geschlecht‘ … Ähnlich tata.' Pokorny 1959 is a revision of this page; note the attribution of the adal link to Schrader.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 pp. 3-4, entries atto- and [athal-]\", \"stance\": \"partial\", \"note\": \"Both entries cross-refer '[In Pok. atos 71]' but are printed separately; [athal-] is bracketed = 'Germanic root', not reconstructible for PIE.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck pp. 94-95 (SYN.txt leaves 123-124; leaf = printed + 29)\", \"stance\": \"partial\", \"note\": \"'2. tata, atta, dada, etc. Walde-P. 1.44, 704. For \\\"father\\\" or \\\"old man\\\", Skt. tata- (in Rigveda), Grk. τατα, τεττα, αττα … Goth. atta, ON atte, OHG atto, Alb. at, ChSl. otĭcĭ, etc., Hitt. attas.' Buck puts atta and tata in one list, but as 'infantile syllables or nursery words' of 'loose application', not as one etymon with descendants.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt leaf 112 (= printed p. 178) and leaf ~700 (= printed p. 1369)\", \"stance\": \"partial\", \"note\": \"Mann has no *atos/*atta headword in the sections consulted; he treats 'tăt- (4) (tàtà) \\\"daddy\\\". WP I, 704' (p. 1369) and 'dhedh- \\\"nurse\\\"' (p. 178) as separate lemmas.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"âthoya, âthwya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan Āθwya- is a genuine, well attested name: Yasna 9.7 names Āθwya as the second man to press the haoma and the father of θraētaona (later MP Frēdōn, NP Fereydūn), and the derived adjective āθwyāna- 'of the family of Āθwya' is used of Fereydūn's line. Bartholomae, Altiranisches Wörterbuch s.v. θraētaona- (BRT.txt line 14459 ff., col. ~802) says in the footnote 'Er ist in Varəna als Sohn Āθwyas geboren' and quotes the phrases 'nafəδrō āθwyānōiš' and 'vīsō āθwyānahe'. Its Vedic counterpart is Āptya- (Trita Āptya), with the regular Iranian/Indic correspondence Av. θw : Skt. pt. The link to *atos, however, is only a guess, and Nourai's own reference says so: Walde-Pokorny I 44 has 'Nach Justi IA. 17, 109 f. hierher vermutlich auch av. āθwya- \\\"Name des Vaters θraētaona's\\\" als \\\"von adeliger Abkunft\\\"?' — with a question mark, repeated verbatim by Pokorny 71. It rests on reading Āθwya- as an -ya- derivative of the *āt(h)- of Germanic *aþala- 'noble birth'. Iranists work instead with the Indo-Iranian equation Āθwya- = Āptya-. Finally, the gloss 'husband, man' is unsupported: no dictionary gives Āθwya- a common-noun sense; that part presumably comes from FAF (Daneshgar's Farhang-e Aʿlām-e Fārsī), which is not available. 'âthoya' is a loose rendering of the disyllabic reading āθwiya-.\",\n          \"derivation_fa\": \"«آثویه/آثویَه» (Āθwya-) در اوستا نام پدر فریدون (θraētaona-) است و در یسنا ۹٫۷ به عنوان دومین کسی که هوم را فشرد یاد شده؛ صفت نسبی آن āθwyāna- «از خاندان آثویه» است. بارتولمه در ذیل θraētaona- می‌نویسد «او در وَرِنَ به عنوان پسر آثویه زاده شد» و ترکیب‌های nafəδrō āθwyānōiš و vīsō āθwyānahe را می‌آورد. همتای ودایی این نام Āptya- است (تریتَه آپتیه)، با تناظر منظم θw ایرانی در برابر pt هندی. اما پیوند دادن این نام به ریشهٔ *atos تنها یک گمانه است و خود مأخذ نورایی هم آن را با علامت پرسش آورده: والده-پوکورنی (جلد ۱، ص ۴۴) و پوکورنی (ص ۷۱) می‌نویسند «به گفتهٔ یوستی شاید آثویهٔ اوستایی نیز به همین‌جا تعلق داشته باشد، به معنی «از تبار نجیب»؟». افزون بر این، معنای «شوهر، مرد» که نورایی برای این واژه آورده در هیچ فرهنگی نیامده است؛ آثویه اسم خاص است نه اسم عام. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:71\", \"status\": \"partial\", \"note\": \"POK_01.txt leaf 80: 'hierher auch av. ā-θwya- ,Name des Vaters θraētaona's‘ als ,von adeliger Abkunft‘?' — Pokorny does list the name under atos, but as a question, and gives no sense 'husband, man'.\"},\n            {\"ref\": \"FAF:10\", \"status\": \"not_checked\", \"note\": \"FAF = A. Daneshgar, Farhang-e Aʿlām-e Fārsī (Hafez Novin 1370). refs_online.json records kind 'none': nothing digitised on archive.org, Google Books or the Persian ebook sites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. θraētaona-, col. ~802 (BRT.txt lines 14459-14461)\", \"stance\": \"supports\", \"note\": \"'j. θraētaona- m. EN. eines Helden der iranischen Sage, Farīdūn' with footnote 'Er ist in Varəna als Sohn Āθwyas geboren'; the text quotes 'nafəδrō āθwyānōiš' Yt.13.131 and 'vīsō āθwyānahe' Yt.5.33. Confirms the name and the patronymic; Bartholomae offers no IE etymology of it here.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 44 (WLD_Bd1_pages.txt leaf 53)\", \"stance\": \"partial\", \"note\": \"'Nach Justi IA. 17, 109 f. hierher vermutlich auch av. āθwya- ,Name des Vaters θraētaonas‘ als ,von adeliger Abkunft‘?' — the connection is credited to Justi and marked doubtful.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (KNT.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'aptya|athwya|Thraetaona|Fredon' in KNT.txt returns nothing; the Old Persian inscriptional corpus does not contain the name.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"Âspiyan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Persian form of the name does exist, but it continues the Avestan patronymic āθwyāna-, not āθwya- itself. Encyclopaedia Iranica s.v. ĀBTĪN: 'From it is derived the adjective āθwyānay-, applied to the family of Ferīdūn. In Pahlavi literature the latter appears as the name of Ferīdūn's father in the form Āswīān or Āsbīān (written ʾspydʾn or ʾspykʾn; Dēnkard, pp. 319.19, 438.15; Zātspram, p. 53.12).' The Bundahišn calls Fereydūn's father Asbīān-ī Purgāw and gives a genealogy of ten 'Asbīān' ancestors (Asbīān Sōggāw, Asbīān Spēdgāw, etc.). The reading of the Pahlavi spelling is not settled — Āswīān / Āsbīān / (Nourai's) Āspiyān are all readings of the same ʾspydʾn/ʾspykʾn, and the Arabic-script transmission (Ṭabarī, Bīrūnī, Ḥamza Iṣfahānī, Moǰmal al-tawārīḵ) has Āṯfīān, which preserves the Avestan θ (ث) and w (ف) much better than the Pahlavi grapheme does. So: real form, right family, but the immediate Avestan source is the adjective āθwyāna-, and the vocalisation printed here is one option among several.\",\n          \"derivation_fa\": \"صورت فارسی میانهٔ این نام واقعاً وجود دارد، اما دنبالهٔ صفت نسبی اوستایی āθwyāna- است نه خودِ āθwya-. دانشنامهٔ ایرانیکا در مدخل «آبتین» می‌نویسد که در ادبیات پهلوی نام پدر فریدون به صورت Āswīān یا Āsbīān (نوشتهٔ ʾspydʾn / ʾspykʾn؛ دینکرد ۳۱۹٫۱۹ و ۴۳۸٫۱۵، زادسپرم ۵۳٫۱۲) آمده است، و بندهش او را «اسبیانِ پُرگاو» می‌خواند و ده نیای «اسبیان» برای فریدون برمی‌شمارد. خوانش این املای پهلوی قطعی نیست: «آسویان»، «آسبیان» و «آسپیان» (خوانش نورایی) همه خوانش‌های یک نویسه‌اند، و صورت عربی‌نویسِ «اثفیان» در طبری و بیرونی و حمزهٔ اصفهانی و مجمل‌التواریخ، ثِ اوستایی و و را بهتر نگاه داشته است. پس صورت واقعی است ولی خاستگاه بی‌واسطهٔ آن صفت āθwyāna- است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/\"],\n          \"ref_check\": [\n            {\"ref\": \"FAF:10\", \"status\": \"not_checked\", \"note\": \"Farhang-e Aʿlām-e Fārsī: no copy online or on disk (refs_online.json FAF kind = 'none').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary (PHD.txt, PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'spiyan|spyan|abtin|Frēdōn|fredon' returns nothing; MacKenzie's dictionary excludes proper names, so it cannot speak to this node.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II Glossary (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"same grep, no hit.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol. 1 s.v. آبتین, editor's footnote 7 (BQT_v1_pages.txt line 6470 ff.; BQT_alt_v1.txt line 10085)\", \"stance\": \"supports\", \"note\": \"Moʿin's footnote lists the transmitted variants: 'طبری «افریدون بن اثفیان» (ج۱ ص۹۸)، بیرونی «اثفیان» (آثارالباقیه ۲۲۹)، مجمل‌التواریخ والقصص ص۲۶ «اثفیان»، شاهنامه «آبتین»', and ends with a line giving 'اوستا āθwya و āθwyāna, پهلوی …'. Confirms that the Pahlavi/Arabic form of the name is a reflex of āθwyāna-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"Âbtîn «آبتین» (also آتبین)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP آبتین Ābtīn (in verse Ābetīn) is the father of Fereydūn in the Šāhnāma, and the chart's Ferdowsī line ('تو بشناس کز مرز ایران زمین — یکی مرد بُد، نام او آبتین') is genuine. The etymological route, though, runs past Āspiyān rather than through it. Encyclopaedia Iranica s.v. ĀBTĪN: 'A Pahlavi variant, Ātbīn, is also recorded as the name of Ferīdūn's father (Pahl. Texts, p. 23.8); and this, metathesized to Ābtīn, has come down in the Šāhnāma (Moscow, I, p. 57.117f.) and the Moǰmal (p. 25).' Moʿin says the same in his footnote to Borhān-e Qāṭeʿ s.v. آبتین: 'در اوستا Āθwya نام پدر فریدون است و بنابراین صحیح «آتبین» است که ناسخان در رسم‌الخط آن را به «آبتین» تبدیل کرده‌اند. اما در سانسکریت Āptya … و بنابراین آبتین نیز محملی پیدا کند' — i.e. Ātbīn (the variant the JSON records as script_extra آتبین) is the etymologically expected form from Av. Āθwya-, and the metathesis to Ābtīn is a scribal habit, though the Sanskrit cognate Āptya- makes the -bt- order defensible too. So the chain is Av. Āθwya- → Pahl. Ātbīn → (metathesis) NP Ābtīn, in parallel with Av. āθwyāna- → Pahl. Āsbīān/Āswīān; the chart's arrow Āspiyān → Ābtīn joins two sister forms rather than a parent and a child. The gloss is also loose: Ābtīn is not a king but Fereydūn's father, a descendant of Jamšīd killed by Żaḥḥāk.\",\n          \"derivation_fa\": \"«آبتین» (در شعر «آبتین/آبِتین») در شاهنامه نام پدر فریدون است و بیت فردوسی که در نمودار آمده اصیل است. اما مسیر اشتقاق از کنار «آسپیان» می‌گذرد نه از میان آن. ایرانیکا می‌نویسد صورت پهلوی «آتبین» نیز برای پدر فریدون ثبت شده و همین صورت با قلب (metathesis) به «آبتین» بدل شده و به شاهنامه و مجمل‌التواریخ رسیده است. معین نیز در حاشیهٔ برهان قاطع ذیل «آبتین» می‌نویسد: «در اوستا Āθwya نام پدر فریدون است و بنابراین صحیح «آتبین» است که ناسخان در رسم‌الخط آن را به «آبتین» تبدیل کرده‌اند. اما در سانسکریت Āptya … و بنابراین آبتین نیز محملی پیدا کند» — یعنی همان صورت «آتبین» که در داده‌ها به عنوان صورت دوم ثبت شده، صورت درست‌تر است. پس زنجیره چنین است: اوستایی Āθwya- ← پهلوی Ātbīn ← (قلب) فارسی نو «آبتین»، در کنارِ اوستایی āθwyāna- ← پهلوی Āsbīān؛ یعنی «آسپیان» و «آبتین» دو شاخهٔ هم‌عرض‌اند نه پدر و فرزند. معنای «نام یکی از شاهان نخستین ایران» هم دقیق نیست؛ آبتین شاه نبود، پدر فریدون و از تبار جمشید بود. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.iranicaonline.org/articles/abtin-father-of-the-mythical-king-feridun/\"],\n          \"ref_check\": [\n            {\"ref\": \"SNS:135\", \"status\": \"partial\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast: the index (SNS_pages.txt line 16214) reads 'Fredon 135/6', and the glossary entry at line 5806 is ':fredon:' with the Latin forms 'āθwya', 'θraetaona-', 'traitana-', a Bartholomae column reference '799)' and the Pahlavi spelling 'frydwn'. So p. 135 does carry the Avestan base of the name — but as the entry for Frēdōn, not for Ābtīn; it says nothing about the Āspiyān → Ābtīn step.\"},\n            {\"ref\": \"MON5:7\", \"status\": \"not_checked\", \"note\": \"Moʿin, Farhang-e Fārsī vol. 5 (Aʿlām) p. 7 — the aʿlām volumes are not on vajehyab/abadis (which carry only the lexicon vols 1-3) and are not on disk; grep 'آبتین' in MON_part1/MON_part2 and the Adena 2-vol djvu produced only OCR noise.\"},\n            {\"ref\": \"FAF:10\", \"status\": \"not_checked\", \"note\": \"no copy of Farhang-e Aʿlām-e Fārsī available.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol. 1 s.v. آبتین, footnote 7 (BQT_v1_pages.txt line 6483; duplicate in BQT_alt_v1.txt line 10085 and BQT_v1.txt line 10973)\", \"stance\": \"supports\", \"note\": \"'۷ - در اوستا Āθwya نام پدر فریدون است و بنابراین صحیح «آتبین» است که ناسخان در رسم‌الخط آنرا به «آبتین» تبدیل کرده‌اند. اما در سانسکریت Āptya … به فارسی بر تاء آمده «بارتولمه ۳۷۳» و بنابراین آبتین نیز محملی پیدا کند. طبری «افریدون بن اثفیان» … بیرونی «اثفیان» … شاهنامه «آبتین»'. Directly on point, and it is Moʿin — the editor Nourai cites elsewhere as MON.\"},\n            {\"src\": \"FSF\", \"where\": \"Noushin, Vāže-namak (Šāhnāma glossary), FSF_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'آبتین' and 'آتبین' find nothing (فریدون occurs on eight leaves); Noushin glosses only difficult common words, not the proper names.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'آبتین' and 'ABTIN' return no hits.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old High German\",\n          \"words\": \"adal; adel-beraht; athal-wolf\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The words are all real. OHG adal 'Abstammung, edles Geschlecht' (> NHG Adel) reflects PGmc. *aþalą 'nature, nobility', beside the adjective *aþalaz > OHG edili, OS ethili, OE æþele 'noble'; the OE noun æþelu 'noble descent' and ON aðal are the same word. The two compounds are ordinary Germanic dithematic names: OHG Adalberht = adal + beraht 'bright through nobility' (Klein p. 44 s.v. Albert) and OHG Athalwolf / Adalwolf / Adolf = athal + wolf 'noble wolf' (Klein p. 27 s.v. Adolph). The problem is the arrow from *atos. Pokorny 71 and WP I 44 do attach *aþala- to it — 'Ein ähnliches *āto-s in germ. *aþala, *ōþela scheint auch die Grundlage von ahd. adal' — but the verb is 'scheint' and WP credits the idea to Schrader, not to comparative phonology. Watkins/AHD keeps [athal-] as a bracketed Germanic root ('possibly related to Greek atallein, to foster'), and Wiktionary, following Orel, derives *aþalą from PIE *h₂et-olo- 'family, race' (*h₂et- 'beyond' + *h₂el- 'to nourish, grow'), explicitly not from *átta. So the node's words are sound and the compounds correctly analysed; only their attachment to the nursery word *atta is a nineteenth-century conjecture that current handbooks have dropped. A small formal point: the book prints 'adel-beraht' with the e-grade adjective stem, whereas the attested OHG name is Adalberht/Adalbert; 'athal-wolf' matches Klein's OHG Athalwolf.\",\n          \"derivation_fa\": \"واژه‌های این گره همه واقعی‌اند: adal آلمانی علیای باستان «تبار، خاندان شریف» (> Adel آلمانی امروز) بازماندهٔ *aþalą ژرمنی آغازین است، در کنار صفت *aþalaz > edili آلمانی علیای باستان و æþele انگلیسی باستان «نجیب». دو ترکیب نیز نام‌های دوجزئی معمول ژرمنی‌اند: Adalberht = adal + beraht «درخشان از نجابت» و Athalwolf = athal + wolf «گرگ نجیب» (کلاین، صص ۲۷ و ۴۴). اما پیوند این‌ها با ریشهٔ *atos جای چون‌وچرا دارد: پوکورنی و والده-پوکورنی آن را با فعل «به نظر می‌رسد» و به نقل از شرادر آورده‌اند، واتکینز [athal-] را «ریشهٔ ژرمنی» جداگانه می‌داند، و ویکی‌واژه به پیروی از اورل *aþalą را از *h₂et-olo- «خاندان، نژاد» می‌گیرد و صراحتاً پیوند با *átta را رد می‌کند. نکتهٔ صوری: کتاب «adel-beraht» چاپ کرده، حال آنکه صورت گواهی‌شده Adalberht است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalaz\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/aþalą\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:27\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 1690, leaf 27 (= printed pp. 27-28): 'Adolph, Adolphus, masc. PN. — L. Adolphus, of Teut. origin. The name lit. means \\\"noble wolf\\\"; cp. OHG. Athalwolf, Athaulf, Adulf, Adolf (G. Adolf), fr. athal, \\\"noble\\\", and wolf, \\\"wolf\\\".' Exactly the chart's athal-wolf.\"},\n            {\"ref\": \"KLN:44\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2105, leaf 36 (= printed pp. 44-45): 'Albert, masc. PN. — F., fr. OHG. Adalbert, lit. \\\"bright through nobility\\\", fr. adal, \\\"nobility\\\", and beraht, \\\"bright\\\". Cp. Ethelbert, fr. OE. Æðelbryght … For the first element see atheling.' Klein's headword is Adalbert, not the book's 'adel-beraht'.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 line 300: '[athal-. Race, family. Germanic root, possibly related to Greek atallein, to foster. 1. Germanic *athal- in Old English ætheling, prince: ATHELING. 2. Variant Germanic *ōthel- in Old High German edili, noble: EDELWEISS. [In Pok. atos 71.]]'. Has the element and the Pokorny cross-reference, but treats it as Germanic-only and lists no personal names.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 27, 44 (KLN_1966.txt lines 1690, 2105) and s.v. atheling (line 3815)\", \"stance\": \"supports\", \"note\": \"s.v. atheling: 'OE. æðeling \\\"a noble\\\", fr. æðele \\\"noble\\\", which is rel. to OFris. ethele, OS. edili, OHG. edili, MHG. edele, G. edel, \\\"noble\\\". The orig. meaning of these adjectives was \\\"noble by birth\\\".'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, entry [athal-]\", \"stance\": \"partial\", \"note\": \"Germanic root, bracketed; no derivation from *atto-.\"},\n            {\"src\": \"POK\", \"where\": \"IEW p. 71\", \"stance\": \"supports\", \"note\": \"'Ein ähnliches *āto-s in germ. *aþala, *ōþela scheint auch die Grundlage von ahd. adal ,Geschlecht‘, nhd. Adel, as. athali, ags. æðelu N. Pl. ,edle Abkunft‘, aisl. aðal ,Anlage, Geschlecht‘, Adj. ahd. edili …'. Note the hedge 'scheint'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 44\", \"stance\": \"partial\", \"note\": \"Same sentence, with the source of the idea named: 'scheint nach Schrader IA. 9, 172, RL. 815 auch die Grundlage von ahd. adal ,Geschlecht‘'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt\", \"stance\": \"silent\", \"note\": \"grep 'atheling|Adolphus|noble.*wolf' in SKT.txt returns nothing relevant; Skeat's concise dictionary omits personal names.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"Albert; Adolph\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English names are borrowings of the Old High German compounds of the parent node, not native developments. Albert came in from French Albert (Latinised Albertus) < OHG Adalbert, and was made popular in nineteenth-century England by Queen Victoria's consort Prince Albert of Saxe-Coburg-Gotha; the native English reflex of the identical compound is Ethelbert < OE Æþelbeorht, so Albert and Ethelbert are doublets. Adolph is from Latin Adolphus, the Latinisation of OHG Athalwolf/Adalwolf (German Adolf), whose native English doublet is Ethelwolf < OE Æþelwulf. Klein's entries on pp. 27 and 44, which Nourai cites, give exactly this and add the pairing with the Old English forms.\",\n          \"derivation_fa\": \"هر دو نام انگلیسی وام‌واژه‌اند نه بازماندهٔ بومی: Albert از فرانسهٔ Albert (لاتینی‌شدهٔ Albertus) و آن از Adalbert آلمانی علیای باستان گرفته شده و در سدهٔ نوزدهم به سبب شهرت شاهزاده آلبرت، همسر ملکه ویکتوریا، در انگلستان رواج یافت؛ صورت بومی همان ترکیب در انگلیسی Ethelbert است از Æþelbeorht انگلیسی باستان، پس این دو «دوگانه» (doublet) اند. Adolph نیز از لاتینی Adolphus، صورت لاتینی‌شدهٔ Athalwolf آلمانی علیای باستان است و دوگانهٔ بومی آن Ethelwolf از Æþelwulf است. کلاین در صفحه‌های ۲۷ و ۴۴ دقیقاً همین را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Albert\",\n            \"https://en.wiktionary.org/wiki/Adolf\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:44\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 36 (printed p. 44/45): 'Albert, masc. PN. — F., fr. OHG. Adalbert … Cp. Ethelbert, fr. OE. Æðelbryght, which is the exact equivalent of OHG. Adalbert.' The Adolph entry stands on p. 27 (line 1690).\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 [athal-] gives ATHELING and EDELWEISS as the English derivatives; personal names are outside the scope of the appendix, so it neither supports nor contradicts this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 27 and 44\", \"stance\": \"supports\", \"note\": \"See quotes above; Klein is the modern standard for these two names.\"},\n            {\"src\": \"WEB/Wiktionary\", \"where\": \"en.wiktionary.org s.v. Albert, Adolf\", \"stance\": \"supports\", \"note\": \"'From Old High German adal (\\\"noble\\\") + wulf (\\\"wolf\\\")… doublet Ethelwolf, from Old English Æþelwulf' (Adolf); 'From Old High German Adalbert, from adal + beraht … also via Old English Æþelbeorht, and through Old French and Latin Albertus … a doublet of Ethelbert' (Albert).\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"no entries for Albert or Adolph.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Tât, Tâta : daddy; Dhědh : grandfather\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both etyma exist, but neither descends from *atos, and Nourai's own references say so. Pokorny has a separate lemma 'tata-, teta- Daddy; expr. child word' at IEW 1056 (WP I 704, Trautmann 320, Vasmer 3.81), and Mann has 'tăt- (4) (tàtà) \\\"daddy\\\". WP I, 704' at IEC 1369 and 'dhedh- \\\"nurse\\\"' at IEC 178; the 'grandfather' etymon proper is PIE *dʰeh₁dʰ- (Gk. τήθη 'grandmother', ChSl. dědъ 'grandfather', Lith. dėdė 'uncle'). What no source supplies is the arrow. Pokorny closes the atos, atta entry with 'Ein auf den verschiedensten Sprachgebieten sich stets neu bildendes Lallwort … Ähnlich tata' — 'similarly tata', i.e. an independent parallel formation, not a descendant; WP I 44 has the identical sentence. Buck, the reference Nourai leans on hardest here, prints '2. tata, atta, dada, etc. Walde-P. 1.44, 704' as one bundle of nursery syllables and introduces the whole section with 'Infantile syllables or nursery words play a considerable role in the words of relationship … A similar use of infantile syllables … is observed in languages from all over the world'; and he sets off the *dʰedʰ- material as 'A related group is Grk. τήθη \\\"grandmother\\\" …'. Nourai has converted Buck's list of look-alikes into a genealogy. Also, Mann's dhedh- is glossed 'nurse', not 'grandfather', so the second gloss in the box is not from IEC:178 either.\",\n          \"derivation_fa\": \"هر دو ستاک واقعی‌اند، اما هیچ‌یک از *atos مشتق نشده و خود مآخذ نورایی این را می‌گویند. پوکورنی مدخل جداگانهٔ «tata-, teta- واژهٔ کودکانه: بابا» را در ص ۱۰۵۶ دارد و مان در IEC ص ۱۳۶۹ «tăt- (4) tàtà «بابا»» و در ص ۱۷۸ «dhedh- «دایه»» را؛ ستاک «پدربزرگ» در واقع *dʰeh₁dʰ- هندواروپایی است (τήθη یونانی «مادربزرگ»، dědъ اسلاوی کهن «پدربزرگ»، dėdė لیتوانیایی «عمو»). آنچه هیچ منبعی تأیید نمی‌کند خودِ پیکان است: پوکورنی مدخل atos را با این جمله می‌بندد که «این واژه‌ای کودکانه است که در هر حوزهٔ زبانی از نو ساخته می‌شود … tata نیز همانند آن است» — یعنی ساختی موازی و مستقل، نه فرزند. باک (SYN ص ۹۴-۹۵) نیز «tata، atta، dada» را یکجا به عنوان «هجاهای کودکانه» فهرست می‌کند و تصریح می‌کند که چنین کاربردی «در زبان‌های سراسر جهان دیده می‌شود». نورایی فهرستِ شباهت‌های باک را به شجره‌نامه بدل کرده است. افزون بر این، معنای dhedh- نزد مان «دایه» است نه «پدربزرگ». پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/τήθη\"],\n          \"ref_check\": [\n            {\"ref\": \"SYN:94\", \"status\": \"partial\", \"note\": \"Buck pp. 94-95 (SYN.txt leaves 123-124): the discussion 'infantile syllables or nursery words' begins on p. 94 and the numbered list on p. 95, where group 2 is 'tata, atta, dada, etc. Walde-P. 1.44, 704'. Buck groups them; he does not derive one from the other, and he calls them words 'of loose application' repeatedly re-created.\"},\n            {\"ref\": \"WLD1:44\", \"status\": \"partial\", \"note\": \"WLD_Bd1_pages.txt leaf 53 = WP I p. 44 is the atta entry, whose last words are 'Ähnlich tata' — Buck's own cross-reference (WP 1.44, 704) is why Nourai cites this page, but the page says 'similar to', not 'source of'. The tata material is at WP I 704, not 44.\"},\n            {\"ref\": \"IEC:178\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 112 (= printed p. 178, page numbers 178/179 visible on the leaf): 'dhedh- \\\"nurse\\\" Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) tēthe \\\"nurse\\\"; Ir. cf. deol, diúl \\\"suckling\\\"'. Mann's gloss is 'nurse', not 'grandfather', and he gives no link to *atta.\"},\n            {\"ref\": \"IEC:1369\", \"status\": \"supports\", \"note\": \"IEC.txt, leaf carrying printed pp. 1368-1369: 'tăt- (4) (tàtà) \\\"daddy\\\". WP I, 704 — Skt. tatah, m. id.; Arm. tat, id. (and *\\\"ancestor\\\"); Hiero-Hitt. tatai, dat. sg. id.; Alb. tatë, def. tata, id. beside Sic-Alb. tot, m. \\\"grandpa\\\"; Lat. tata, It. tata, m. \\\"father\\\"; … Br. tat, tad, m. \\\"father\\\"; W tâd … taid \\\"grandfather\\\"'. Fully supports the form and gloss 'daddy' — but as a lemma of its own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW p. 1056 (POK_full.txt line 84715) and p. 71\", \"stance\": \"contradicts\", \"note\": \"p. 1056: 'Root / lemma: tata- teta-, Meaning: Daddy; expr. child word … eine auch aus den indogermanischen Sprachen verbreitete Lallwortgruppe. References: WP. I 704'. p. 71 ends 'Ähnlich tata.' Two lemmas, 985 pages apart, with no derivational link.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck pp. 94-95\", \"stance\": \"partial\", \"note\": \"See ref_check; Buck's framing is typological, not genealogical.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann pp. 178 and 1369\", \"stance\": \"partial\", \"note\": \"Two independent lemmas, dhedh- 'nurse' and tăt- 'daddy'; neither is referred to *atta.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I pp. 44 and 704\", \"stance\": \"partial\", \"note\": \"WP treats atta (I 44) and tata (I 704) as separate articles.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 396 s.v. dad, daddy\", \"stance\": \"contradicts\", \"note\": \"'… which all are of childish origin' — Klein declines to reconstruct a proto-form for this group at all.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"tata, tâta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit tatá- / tā́ta- is attested from the Rigveda on and does belong to the nursery group named in the parent box, so the immediate arrow (*tāta → Skt. tāta-) is unobjectionable; Mann IEC 1369 opens the tăt- (4) entry with 'Skt. tatah, m. id.' and Pokorny 1056 has 'Old Indic tata- \\\"father\\\", tāta- \\\"father, son, Lieber\\\"'. The gloss in the chart is what is wrong: tāta- means 'daddy, papa' and is used vocatively as an affectionate address downwards (to a son or pupil) as much as upwards, and Wiktionary/Monier-Williams describe it as 'onomatopoeic, mimicking baby talk', comparing Latin tata and Greek τατᾶ. 'Grandfather' in this group belongs to the extended forms — Cornish hen-dat, Welsh taid, OPruss. thetis — not to the Sanskrit simplex. Nourai's own SYN:94 lists Skt. tata- under 'father' (Buck p. 95, 'Skt. tata- (in Rigveda)'). The failure further up the chart (node 6) applies here too.\",\n          \"derivation_fa\": \"«tāta-» سنسکریت از ریگ‌ودا به بعد گواهی شده و به‌درستی به همان گروه واژه‌های کودکانه‌ای تعلق دارد که در جعبهٔ بالادست آمده است؛ پس پیکان بی‌واسطهٔ *tāta ← tāta- سنسکریت ایرادی ندارد: مان (IEC ص ۱۳۶۹) مدخل tăt- را با «Skt. tatah, m. همان» آغاز می‌کند و پوکورنی (ص ۱۰۵۶) «tata- «پدر»، tāta- «پدر، پسر، عزیز»» دارد. آنچه نادرست است معنای مندرج در نمودار است: tāta- یعنی «بابا، باباجان» و در حالت ندایی هم برای بزرگ‌تر و هم برای کوچک‌تر (پسر یا شاگرد) به کار می‌رود؛ مونیه-ویلیامز و ویکی‌واژه آن را «برگرفته از زبان کودکانه» می‌دانند و با tata لاتینی و τατᾶ یونانی می‌سنجند. معنای «پدربزرگ» در این گروه به صورت‌های گسترده (hen-dat کرنوالی، taid ولزی، thetis پروسی باستان) تعلق دارد نه به صورت سادهٔ سنسکریت. خود مأخذ نورایی، باک (ص ۹۵)، tata- را زیر «پدر» آورده است. ادعای نورایی با احتیاط پذیرفتنی است، ولی معنای «پدربزرگ» درست نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/तात\"],\n          \"ref_check\": [\n            {\"ref\": \"SYN:94\", \"status\": \"partial\", \"note\": \"Buck p. 95 (the list beginning on p. 94): 'For \\\"father\\\" or \\\"old man\\\", Skt. tata- (in Rigveda), Grk. τατα, τεττα, αττα (but Skt. attā \\\"mother\\\")'. Buck's gloss is 'father / old man', not 'grandfather'.\"},\n            {\"ref\": \"IEC:1369\", \"status\": \"supports\", \"note\": \"'tăt- (4) (tàtà) \\\"daddy\\\". WP I, 704 — Skt. tatah, m. id.' Supports form and membership; gloss again 'daddy'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"Mann p. 1369\", \"stance\": \"supports\", \"note\": \"Skt. tatah heads the descendant list of tăt- (4) 'daddy'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 95\", \"stance\": \"partial\", \"note\": \"Skt. tata- listed for 'father'/'old man' under nursery words.\"},\n            {\"src\": \"POK\", \"where\": \"IEW p. 1056\", \"stance\": \"partial\", \"note\": \"'Old Indic tata- \\\"father\\\", tāta- \\\"father, son, Lieber\\\"' — the second gloss shows the vocative-of-affection use in both directions; no 'grandfather'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"tĕthĕ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek τήθη is a real word and it does belong to the second etymon named in the parent box, Nourai's 'Dhědh': Wiktionary derives τήθη from PIE *dʰeh₁dʰ- 'grandparent', with ChSl. dědъ 'grandfather', Lith. dėdė 'uncle', Latv. dēds 'old man', and calls it baby talk; the derivatives τηθίς, τηθία 'aunt' and the Titaness Τηθύς (Hera's nurse) belong with it. So the derivation drawn is defensible. The gloss, however, is simply wrong: τήθη is a feminine first-declension noun meaning 'grandmother' (the male counterpart is πάππος), never 'father' or 'grandfather'. Both of Nourai's own references say so — Buck p. 95: 'A related group is Grk. τήθη \\\"grandmother\\\", τηθίς \\\"aunt\\\"', and Mann IEC 178 s.v. dhedh- 'nurse': 'Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) tēthe \\\"nurse\\\"'. Neither gives a masculine sense. The extraction is faithful to the printed page (p. 38 of the book prints 'tĕthĕ : father, grandfather'), so this is Nourai's own slip, not a scan error.\",\n          \"derivation_fa\": \"τήθη یونانی واژه‌ای واقعی است و به‌درستی به دومین ستاکِ جعبهٔ بالادست، یعنی «Dhědh» نورایی، تعلق دارد: ویکی‌واژه آن را از *dʰeh₁dʰ- هندواروپایی «پدربزرگ/مادربزرگ» می‌گیرد، هم‌ریشه با dědъ اسلاوی کهن «پدربزرگ»، dėdė لیتوانیایی «عمو» و dēds لتونیایی «پیرمرد»، و آن را واژه‌ای کودکانه می‌شمارد؛ مشتقات τηθίς و τηθία «عمه/خاله» و نام تیتان Τηθύς (دایهٔ هرا) نیز از همین ستاک‌اند. پس اشتقاق رسم‌شده پذیرفتنی است. اما معنای داده‌شده نادرست است: τήθη اسمی مؤنث از صرف اول و به معنی «مادربزرگ» است (همتای مذکر آن πάππος)، و هرگز «پدر» یا «پدربزرگ» نیست. هر دو مأخذ خود نورایی همین را می‌گویند: باک (ص ۹۵) «Grk. τήθη «مادربزرگ»، τηθίς «عمه»» و مان (IEC ص ۱۷۸) ذیل dhedh- «دایه». تصویر صفحهٔ ۳۸ کتاب نشان می‌دهد استخراج داده‌ها درست بوده و این خطای خودِ کتاب است. ادعای نورایی در اشتقاق پذیرفتنی است ولی معنای آن نادرست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/τήθη\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:178\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 112 (printed p. 178): 'dhedh- \\\"nurse\\\" … Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) tēthe \\\"nurse\\\"'. Mann has the word under dhedh-, as Nourai's parent box implies, but glosses it 'nurse' and marks it 'alleged'.\"},\n            {\"ref\": \"SYN:94\", \"status\": \"contradicts\", \"note\": \"Buck p. 95: 'A related group is Grk. τήθη \\\"grandmother\\\", τηθίς \\\"aunt\\\", θεῖος, θεία \\\"uncle, aunt\\\", Lith. dėdė \\\"uncle\\\", ChSl. dědŭ \\\"grandfather\\\", NHG dial. deite \\\"father, old man\\\"'. Buck gives 'grandmother', directly against the chart's 'father, grandfather'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"Buck p. 95\", \"stance\": \"contradicts\", \"note\": \"τήθη = 'grandmother'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 178\", \"stance\": \"partial\", \"note\": \"τήθη under dhedh- 'nurse'.\"},\n            {\"src\": \"WEB/Wiktionary\", \"where\": \"en.wiktionary.org s.v. τήθη\", \"stance\": \"contradicts\", \"note\": \"'τήθη (tḗthē) f — grandmother', from PIE *dʰeh₁dʰ- 'grandparent'; occupies the 'grandmother' slot in the family-terms table, with πάππος for 'grandfather'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"tata\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin tata 'daddy' is genuine and belongs precisely to the *tata nursery group of the parent box: Ernout-Meillet s.v. tata: 'tata, -ae m.: papa. Mot enfantin, cité par Varr. ap. Non. 81,3, et attesté épigraphiquement, ainsi que tatula, CIL VI 35636 … Cf. atta. Cf. gr. τατᾶ, corn. tat …, pol. tata', and Buck p. 95 lists 'Lat. tata (frequent in inscriptions)' in the same group; Italian tata 'father' continues it. The immediate arrow is therefore fine. The gloss is again inflated: 'grandfather' in Latin is atta, not tata — Ernout-Meillet s.v. atta: 'atta, -ae m.: grand-père, ou plutôt \\\"grand-papa\\\" … Mot du langage enfantin, qu'on retrouve sans doute dans atauus.' Latin happens to have both members of the pair that Nourai's chart merges, and they are semantically distinct; conflating them is what produces the double gloss here.\",\n          \"derivation_fa\": \"tata لاتینی «بابا» واژه‌ای اصیل است و دقیقاً به همان گروه واژه‌های کودکانهٔ *tata تعلق دارد که در جعبهٔ بالادست آمده: ارنو-مِیه ذیل tata می‌نویسد «tata, -ae مذکر: بابا. واژهٔ کودکانه، نقل‌شده از وارو نزد نونیوس ۸۱٫۳، و در کتیبه‌ها گواهی‌شده، همچنین مصغّر آن tatula … بنگرید به atta؛ نیز τατᾶ یونانی، tat کرنوالی، tata لهستانی»، و باک (ص ۹۵) نیز «Lat. tata (پرکاربرد در کتیبه‌ها)» را در همین گروه آورده است؛ tata ایتالیایی «پدر» دنبالهٔ همان است. پس پیکان بی‌واسطه درست است. اما معنا دوباره بزرگ‌نمایی شده: «پدربزرگ» در لاتینی atta است نه tata — ارنو-مِیه ذیل atta: «پدربزرگ، یا بهتر بگوییم «بابابزرگ» … واژه‌ای از زبان کودکانه». لاتینی هر دو عضو جفتی را دارد که نمودار نورایی یکی کرده است و معنای آن دو یکی نیست. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SYN:94\", \"status\": \"supports\", \"note\": \"Buck p. 95, group 2 of the nursery words listed from p. 94: '… Lat. tata (frequent in inscriptions), Rum. tată, W., Br. tad, NE dad …'. Supports the form and its membership; Buck's heading for the group is 'father / old man'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. tata (LAT.txt line 63105) and s.v. atta (line ~5803)\", \"stance\": \"partial\", \"note\": \"tata = 'papa. Mot enfantin'; atta = 'grand-père, ou plutôt \\\"grand-papa\\\"'. Confirms the word, splits the two glosses the chart merges.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 95\", \"stance\": \"supports\", \"note\": \"Latin tata listed in the nursery-word group.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 1369\", \"stance\": \"supports\", \"note\": \"'Lat. tata, It. tata, m. \\\"father\\\"' in the tăt- (4) list.\"},\n            {\"src\": \"POK\", \"where\": \"IEW p. 1056\", \"stance\": \"supports\", \"note\": \"'Latin tata \\\"father (in the baby talk)\\\"' under tata-, teta-.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Russian\",\n          \"words\": \"tata\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Russian та́та 'daddy, father' is a real colloquial/dialectal word (the standard word is оте́ц) and belongs with Czech táta, Polish tata, ChSl. teta 'aunt'. Klein p. 396 — the page Nourai cites — lists it among the comparanda of dad: 'Czech tata, Russ. táta'; Pokorny 1056 has 'russ. tata etc. \\\"father\\\", russ.-Church Slavic teta etc. \\\"aunt\\\"', on Vasmer 3.81. So the immediate arrow from the *tata nursery syllable holds. Two qualifications: Klein's whole point on that page is that these forms 'all are of childish origin', i.e. repeatedly re-created rather than inherited in the technical sense; and the Slavic reflex of the OTHER etymon, *atta, is the ordinary Russian word for 'father', оте́ц < ChSl. отьць < *attikos — which is exactly the pair that Pokorny keeps in two lemmas and this chart collapses into one.\",\n          \"derivation_fa\": \"«та́та» روسی به معنی «بابا، پدر» واژه‌ای واقعی و محاوره‌ای/گویشی است (واژهٔ معیار оте́ц است) و با táta چکی، tata لهستانی و teta اسلاوی کهن «عمه» هم‌گروه است. کلاین در ص ۳۹۶ — همان صفحه‌ای که نورایی ارجاع می‌دهد — آن را در کنار «Czech tata, Russ. táta» می‌آورد، و پوکورنی (ص ۱۰۵۶) به نقل از فاسمر «russ. tata و جز آن «پدر»» دارد. پس پیکان بی‌واسطه پذیرفتنی است. دو نکته: نخست آنکه سخن اصلی کلاین در همان صفحه این است که این صورت‌ها «همه خاستگاه کودکانه دارند»؛ دوم آنکه بازماندهٔ اسلاویِ ستاکِ دیگر، یعنی *atta، همان واژهٔ معمول روسی برای «پدر» است: оте́ц از отьць اسلاوی کهن از *attikos — یعنی همان جفتی که پوکورنی در دو مدخل جدا نگاه داشته و این نمودار یکی کرده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/dad\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:396\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 10196, leaf 219 = printed pp. 396-397 (the leaf carries the printed numbers 396 and 397): 'dad, daddy, n., father. — A child's word. Cp. W. tad, dad, Ir. daid, Co. tat, \\\"father\\\", hendat, \\\"grandfather\\\", Czech tata, Russ. táta, Lith. tetis, tete, \\\"father\\\", OPruss. thetis, \\\"father, old man\\\" … which all are of childish origin.' Russian táta is there, exactly as the chart says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 396 s.v. dad, daddy\", \"stance\": \"supports\", \"note\": \"Russ. táta listed; but with the caveat 'all are of childish origin'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW p. 1056\", \"stance\": \"supports\", \"note\": \"'russ. tata etc. \\\"father\\\", russ.-Church Slavic teta etc. \\\"aunt\\\". Old Church Slavic tetŭka ds. … References: WP. I 704, WH. II 650, Trautmann 320, Vasmer 3, 81.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck pp. 94-95\", \"stance\": \"partial\", \"note\": \"Buck's group 2 covers the Slavic material; he adds 'Here also Slav. and Lith. teta \\\"aunt\\\", etc.' and stresses their status as nursery words.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"dad; daddy\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart's own NOTE concedes the problem, and modern scholarship sides with Klein against the arrow. Klein p. 396: 'dad, daddy, n., father. — A child's word. Cp. W. tad, dad, Ir. daid … Czech tata, Russ. táta … L. tata, \\\"father\\\", Gk. τατᾶ, τεττα, \\\"O father, daddy\\\" … OI. tatah, \\\"father, son\\\", which all are of childish origin' — a list of parallels with an explicit refusal to reconstruct descent. Etymonline agrees: dad and daddy are first recorded c. 1500, 'from child's speech', 'nearly universal' and 'probably prehistoric' only in the sense that infants everywhere produce the syllable. There is also a hard phonological objection: a PIE *t- inherited into Germanic becomes þ- by Grimm's Law (PIE *tū > OE þū 'thou'), so English d- in dad cannot be the regular reflex of a PIE *tāta; the initial d- of Irish daid and the t- of Welsh tad are likewise fresh formations in each language. The verdict is therefore that dad is a look-alike of *tāta rather than its descendant, and Nourai's chart draws an inheritance line where his own source declines to.\",\n          \"derivation_fa\": \"خودِ یادداشت نمودار به این مشکل اعتراف می‌کند و پژوهش امروزی جانب کلاین را می‌گیرد، نه جانب پیکان. کلاین در ص ۳۹۶ می‌نویسد: «dad, daddy: واژه‌ای کودکانه. بسنجید با tad ولزی، daid ایرلندی … tata چکی، táta روسی … tata لاتینی، τατᾶ یونانی … tatah سنسکریت — که همه خاستگاه کودکانه دارند» — یعنی فهرستی از موازی‌ها با خودداری صریح از بازسازی اشتقاق. اتیمولوژی آنلاین نیز می‌گوید dad و daddy از حدود ۱۵۰۰ م. ثبت شده‌اند و «از گفتار کودکانه» برخاسته‌اند. افزون بر این یک ایراد آوایی قاطع هست: *t هندواروپایی در ژرمنی بر پایهٔ قانون گریم به þ بدل می‌شود (*tū > þū انگلیسی باستان «تو»)، پس d آغازینِ dad نمی‌تواند بازتاب منظمِ *tāta هندواروپایی باشد؛ d ایرلندی daid و t ولزی tad نیز هرکدام ساخت تازهٔ همان زبان‌اند. پس dad شبیهِ *tāta است نه فرزند آن. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://www.etymonline.com/word/dad\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:396\", \"status\": \"contradicts\", \"note\": \"KLN_1966.txt line 10196 (printed p. 396): '… which all are of childish origin.' Klein lists cognate-looking forms but explicitly gives no derivation — exactly what the chart's NOTE reports, and it is a contradiction of the arrow drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 396 s.v. dad, daddy\", \"stance\": \"contradicts\", \"note\": \"See quote; no proto-form, no descent.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt line 4638 s.v. Dad\", \"stance\": \"partial\", \"note\": \"'Dad (C.) W. tad, Irish daid, Bret. tat, tad, father + Gk. τατά, Skt. tāta, dad.' Skeat too only compares; the '(C.)' marks it Celtic-comparanda, not an inherited chain.\"},\n            {\"src\": \"WEB/Etymonline\", \"where\": \"etymonline.com/word/dad\", \"stance\": \"contradicts\", \"note\": \"'dad' c. 1500, from child's speech; the entry stresses that such paternal terms are 'nearly universal' rather than genetically inherited.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"dadeh «دده»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian word exists but means neither 'grandfather' nor 'aunt', and its origin is contested three ways, none of them Nourai's. Moʿin — the very dictionary cited as MON:1499 — gives '(دَ دَ) [تُر.] دایه، پرستار کودکان' (pl. ددگان/دادگان), i.e. 'wet-nurse, children's carer', tagged as a Turkish loan (cf. Turkish dadı 'nanny', dede 'grandfather'); the homograph (دَ دِ) [په.] is the unrelated word for 'wild beast'. Wiktionary gives دده dada as 'sister', as a form of address to a woman of similar age, and historically 'maidservant, female slave', and calls it a babble word, expressly not from Turkish. Mann (IEC 178) does list 'Per. dade' under dhedh- 'nurse' beside South Italian deda and Greek Tēthús — which agrees on the sense 'nurse' but not on 'grandfather, aunt'. So: the gloss in the chart is unsupported by any of the three, and the derivation PIE *átta → *Tāt/*Dhědh → Persian dadeh is supported only by Mann's bare listing, while Nourai's other cited authority, Moʿin, calls it a Turkic loan. Phonologically the form settles nothing: a nursery reduplication da-da can arise in Persian at any date without an Iranian ancestor.\",\n          \"derivation_fa\": \"واژهٔ فارسی «دده» وجود دارد، اما نه «پدربزرگ» است و نه «عمه/خاله»، و در خاستگاه آن سه رأی متفاوت هست که هیچ‌کدام رأی نورایی نیست. معین — همان فرهنگی که نورایی با نشانهٔ MON:1499 به آن ارجاع داده — می‌نویسد «(دَ دَ) [تُر.] دایه، پرستار کودکان» (جمع: ددگان، دادگان) و آن را وام‌واژهٔ ترکی می‌داند (بسنجید با dadı ترکی «دایه» و dede «پدربزرگ»)؛ هم‌نگاشتِ «(دَ دِ) [په.]» به معنی «جانور درنده» واژهٔ دیگری است. ویکی‌واژه «دده» را به معنی «خواهر»، شکل خطاب به زنِ هم‌سن، و در کاربرد تاریخی «کلفت، کنیز» می‌آورد و آن را واژه‌ای کودکانه (babble word) می‌داند و صراحتاً ترکی‌بودن آن را رد می‌کند. مان (IEC ص ۱۷۸) «Per. dade» را ذیل dhedh- «دایه» آورده است — که در معنای «دایه» با معین همسو است ولی با «پدربزرگ، عمه» نه. پس معنای مندرج در نمودار از هیچ‌یک از این سه منبع پشتیبانی نمی‌گیرد و زنجیرهٔ *átta ← *Tāt/*Dhědh ← «دده» تنها بر فهرست خشک مان استوار است، در حالی که مأخذ دیگرِ خود نورایی آن را وام ترکی می‌خواند. از نظر آوایی هم صورت مضاعف «دده» در هر دوره‌ای می‌تواند در فارسی از نو ساخته شود. پژوهش امروزی این ادعا را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/دده\",\n            \"https://abadis.ir/fatofa/دده/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:178\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 112 (printed p. 178): 'dhedh- \\\"nurse\\\" Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-ē-) Tēthús (nurse of Hera) and (alleged) tēthe \\\"nurse\\\"'. Mann has the Persian word, glossed 'nurse' — not 'grandfather, aunt' — and does not connect it to *atta.\"},\n            {\"ref\": \"MON:1499\", \"status\": \"contradicts\", \"note\": \"Moʿin's entry, read in the فرهنگ معین section of abadis.ir/fatofa/دده/: '(دَ دَ) [تُر.] دایه، پرستار کودکان (ج. ددگان، دادگان)'. Moʿin tags the word as Turkish and glosses it 'nursemaid', against both Nourai's gloss and his Indo-European derivation. (The print page 1499 of the 6-vol. edition could not be checked directly: Moʿin's lexicon volumes are online only as entry text, without page numbers; grep of MON_part1/MON_part2 for دده returned only OCR noise.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. دده (via abadis.ir)\", \"stance\": \"contradicts\", \"note\": \"'(دَ دَ) [تُر.] دایه، پرستار کودکان' — Turkish loan, 'nursemaid'.\"},\n            {\"src\": \"WEB/Wiktionary\", \"where\": \"en.wiktionary.org s.v. دده\", \"stance\": \"partial\", \"note\": \"Persian دده dada: 'sister'; 'sis' (address to a woman of similar age); historically 'maidservant', 'female slave'. Etymology: 'a babble word', explicitly not from Turkish. Confirms a nursery origin but not the chart's gloss or its IE pedigree.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 178\", \"stance\": \"partial\", \"note\": \"'Per. dade' under dhedh- 'nurse'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol. 2 (BQT_v2_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'دده' in BQT_v2_pages.txt returns only OCR noise (lines 947, 7800 etc. are broken column text); no usable entry with Moʿin's etymological footnote could be located.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie (HRN.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'dade|dâde|dada ' returns nothing; Horn has no entry for the word.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"same grep, no hit.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-68.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-05T05:40:47.225Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T05:40:50.888Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/verify_check.py 68"
}
```


### [2026-09-05T05:40:52.868Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'plausible': 8, 'confirmed': 1, 'disputed': 3}
root verdicts: {'plausible': 1}
ref checks: {'partial': 10, 'not_checked': 4, 'supports': 7, 'contradicts': 3}
books consulted: {'supports': 13, 'partial': 14, 'silent': 10, 'contradicts': 7} | by book: {'KLN': 5, 'POK': 5, 'SYN': 5, 'IEC': 5, 'WLD': 3, 'BQT': 3, 'SKT': 3, 'WEB/Wiktionary': 3, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'FSF': 1, 'ARY': 1, 'AHD': 1, 'LAT': 1, 'WEB/Etymonline': 1, 'MON': 1, 'HRN': 1, 'HUB': 1}
```


## [2026-09-05T05:41:20.452Z] AGENT

Done. `verify_check.py 68` reports 0 PROBLEM lines.

**Page 68 (book p. 38) — root `Âtos, Atta, Ato, Athal`, 12 nodes (3 redirect entries skipped)**

- Root verdict: **plausible** (1)
- Node verdicts: **confirmed 1, plausible 8, disputed 3**
- Ref checks on Nourai's own citations: supports 7, partial 10, contradicts 3, not_checked 4 (all FAF = Daneshgar's *Farhang-e Aʿlām*, not digitised anywhere, plus MON vol. 5 Aʿlām)

**Disputed items**
- `#6 [Indo-European] Tât, Tâta / Dhědh` — no source derives *tata from *atta. Pokorny (IEW 71) ends the *atos* entry "Ähnlich tata" (a *parallel* Lallwort) and gives tata- its own lemma at p. 1056; Buck 94-95, Nourai's own SYN:94, lists "tata, atta, dada" as one bundle of nursery syllables, not a genealogy. Mann's `dhedh-` (IEC 178) is glossed 'nurse', not 'grandfather'.
- `#11 [English] dad, daddy` — the chart's own NOTE is right and modern scholarship sides with Klein p. 396 ("all are of childish origin", no derivation given). Also phonologically blocked: PIE *t- > Gmc. þ- by Grimm's Law, so d- in *dad* cannot be inherited from *tāta.
- `#12 [Persian] dadeh «دده»` — gloss "grandfather, aunt" is unsupported. Moʿin (Nourai's MON:1499) has "(دَ دَ) [تُر.] دایه، پرستار کودکان" — a *Turkish* loan meaning 'nursemaid'; Wiktionary has 'sister / maidservant', a Persian babble word; Mann (IEC 178) has it as 'nurse'. Three incompatible origins, none of them the chart's.

**Notable non-disputed findings**
- `#3 Âbtîn`: Iranica and Moʿin's footnote to Borhān-e Qāṭeʿ agree the chain is Av. *Āθwya-* → Pahl. **Ātbīn** → (metathesis) NP **Ābtīn**, while *Āspiyān* (< Av. *āθwyāna-*) is a **sister** form, not the parent. Nourai's own second spelling in the box, آتبین, is exactly Moʿin's preferred form.
- `#8 Greek tĕthĕ`: τήθη is feminine 'grandmother' (Buck p. 95, Wiktionary), not "father, grandfather" — the derivation from *dʰeh₁dʰ- is fine, the gloss is Nourai's error.
- `#1 Avestan âthwya`: real (Y. 9.7, Bartholomae s.v. θraētaona-), but the link to *atos is Justi's guess, printed with a "?" in both WP I 44 and POK 71; the gloss "husband, man" has no source.
- Root: Watkins/AHD splits Nourai's merged box into `atto-` and bracketed Germanic-only `[athal-]`; Wiktionary/Orel derive PGmc *aþalą from *h₂et-olo-, not *átta.

**Extraction errors: none.** I read `site/pages/68.jpg`; the JSON is faithful to the printed page, including "adel-beraht", "tĕthĕ : father, grandfather" and "dadeh : grandfather, aunt" (all book-side, not scan-side). No `transcription_suspect` nodes, so no page PNG was copied to `refs/ocr/BOOK/`.

11 web pages archived via `fetch_source.py` (Iranica ĀBTĪN, Wiktionary *átta / *aþalaz / *aþalą / دده / τήθη / तात / Albert / Adolf, Etymonline *dad*, abadis Moʿin دده).
