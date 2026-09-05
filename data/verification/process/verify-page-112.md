# Verification process log — verify-page-112


## [2026-09-05T17:32:02.738Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 112 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-112.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-112.json. Write /home/sfmqrb/git/rishe/data/verification/page-112.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 112` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:32:03.969Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:32:04.691Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:32:04.708Z] TOOL RESULT

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


## [2026-09-05T17:32:05.207Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-112.txt"
}
```


### [2026-09-05T17:32:05.228Z] TOOL RESULT

```
1	=== PDF page 112 (book page 82) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Deik : to show  (refs POK:188)
4	#1 (parent #0) [Avestan] refs=POK:188 | daěs : to show, demonstrate
5	  #2 (parent #1) [Persian] refs=HUB:65; BQT:912 | dîs, dîz «دیس ، دیز» : color, appearance, resemblance | extra: تندیس ، طاقدیس ، شبدیز
6	#3 (parent #0) [Germanic] refs=AHD | taikjan : to show
7	  #4 (parent #3) [English] refs=None | teach, token, toe
8	#5 (parent #0) [Latin] refs=AHD | digitus : pointer, finger ; dîcere : to say, dictate ; index : indicator ; jŭdex : one who indicates
9	  #6 (parent #5) [French] refs=None | 
10	    #7 (parent #6) [Persian] refs=MON | dîkteh «دیکته» ; dîktâtor «دیکتاتور»
11	  #8 (parent #5) [English] refs=None | digit, dictate, index, judge
12	#9 (parent #0) [Greek] refs=AHD | dikein : to direct an object, throw
13	  #10 (parent #9) [French] refs=KLN:459 | 
14	    #11 (parent #10) [Persian] refs=MON |  «دیسک»
15	  #12 (parent #9) [English] refs=KLN:433,459 | disc, desk, discuss
16	--- entry 1 ---
17	ROOT Deiw -> redirect to Dei
18	
```


## [2026-09-05T17:32:08.478Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-112.json",
 "description": "Read page 112 source JSON"
}
```


### [2026-09-05T17:32:08.513Z] TOOL RESULT

```
{
  "pdf_page": 112,
  "book_page": 82,
  "entries": [
    {
      "root": {
        "name": "Deik",
        "lang": "Indo-European",
        "refs": "POK:188",
        "gloss": "to show"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:188",
          "words": [
            {"translit": "daěs", "gloss": "to show, demonstrate", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HUB:65; BQT:912",
          "words": [
            {"translit": "dîs, dîz", "gloss": "color, appearance, resemblance", "script": "دیس ، دیز"}
          ],
          "script_extra": "تندیس ، طاقدیس ، شبدیز",
          "note": null,
          "quote": {
            "text": "نه شیرین تر ز شیرین خلق دیدم - نه چون شبدیز شبرنگی شنیدم",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "taikjan", "gloss": "to show", "script": null}
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
            {"translit": "teach, token, toe", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "digitus", "gloss": "pointer, finger", "script": null},
            {"translit": "dîcere", "gloss": "to say, dictate", "script": null},
            {"translit": "index", "gloss": "indicator", "script": null},
            {"translit": "jŭdex", "gloss": "one who indicates", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "dîkteh", "gloss": null, "script": "دیکته"},
            {"translit": "dîktâtor", "gloss": null, "script": "دیکتاتور"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "digit, dictate, index, judge", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "dikein", "gloss": "to direct an object, throw", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": "KLN:459",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": null, "gloss": null, "script": "دیسک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:433,459",
          "words": [
            {"translit": "disc, desk, discuss", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Deiw",
        "redirect": "Dei"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T17:32:09.244Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:32:09.280Z] TOOL RESULT

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


## [2026-09-05T17:32:15.843Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HUB','BQT','KLN','AHD','MON','ARY','HRN','BRT','IEC','SYN','WLD','SKT','LEW','LAT','PHD','NYB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\""
}
```


## [2026-09-05T17:32:15.972Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && head -60 data/verification/page-66.json"
}
```


### [2026-09-05T17:32:17.603Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
```


### [2026-09-05T17:32:17.638Z] TOOL RESULT

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
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
----
{
  "pdf_page": 66,
  "book_page": 36,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "A`.s.r",
      "verdict": "confirmed",
      "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'",
      "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.",
      "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://www.ahdictionary.com/word/semitic.html",
        "https://www.ahdictionary.com/word/search.html?q=alizarin",
        "https://en.wiktionary.org/wiki/عصارة"
      ],
      "ref_check": [
        {
          "ref": "KLN:50",
          "status": "supports",
          "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\", which is rel. to Heb. ʿātzar, Aram.-Syr. ʿătzār, \"he retained\".' Exactly the root, the gloss and the Romance chain Nourai draws."
        },
        {
          "ref": "FVA:273",
          "status": "not_checked",
          "note": "FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989). refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M)."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Arabic",
          "words": "a`sârah; al-a`sârah",
          "verdict": "confirmed",
          "derivation": "Arabic عُصَارَة ʿuṣāra (Klein: ʿaṣārah) is the regular fuʿāla/faʿāla noun of result built on the triliteral ʿ-ṣ-r 'to press': Wiktionary defines it as 'somewhat viscose liquid that one obtains by wringing, sap, juice, extract'. Nourai's two lines are one and the same word, indefinite ʿuṣāra and definite al-ʿuṣāra; he lists both because it is the article-bearing shape that travelled into Romance (Sp. alizari), the same fossilised al- seen in alcohol, alidade, alkali, almanac. The word is native Arabic — no Semitic dictionary treats it as a loan — and it is the hinge of both branches of the chart, the Persian loan عصاره and the Spanish/French dye name.",
          "derivation_fa": "واژهٔ عربی عُصارَة بر وزن فُعالَة از ریشهٔ سه‌حرفی «ع ص ر» ساخته شده و به معنای «شیره و مایعی است که از فشردن گیاه به دست می‌آید». دو صورتی که نورایی آورده (عصارة و الْعصارة) در حقیقت یک واژه‌اند، یکی نکره و دیگری معرفه؛ آوردن صورت معرفه از آن روست که همین شکلِ همراه با «الـ» بوده که به زبان‌های اروپایی راه یافته است، درست مانند alcohol و alkali و alidade. این واژه در عربی اصیل است و هیچ فرهنگ سامی آن را وام‌واژه نمی‌داند؛ ادعای نورایی در این گره درست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/عصارة",
            "https://www.ahdictionary.com/word/semitic.html"
          ],
          "ref_check": [
            {
              "ref": "FVA:273",
              "status": "not_checked",
              "note": "no digital copy of Nahvi's dictionary exists (see root ref_check); the page cannot be inspected."
            }
          ],
          "consulted": [
            {
              "src": "KLN",
              "where": "KLN_1966.txt leaf 38 (≈p.52) s.v. alizari",
              "stance": "supports",
              "note": "'fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\"' — same word, same morphology."
            },
            {
              "src": "AHD",
              "where": "online Appendix of Semitic Roots s.v. ʿṣr",
              "stance": "supports",
```


## [2026-09-05T17:32:21.433Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dei̯ḱ\\|deiḱ\\|deik̂\\|dei k̂\" POK_01.txt | head -30"
}
```


### [2026-09-05T17:32:21.479Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:32:22.601Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^deik\\|deiḱ-\\|deik̑\" AHD_watkins1985.txt | head -20; echo ===; grep -n -i \"deik\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T17:32:22.653Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T17:32:25.726Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"deik\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T17:32:25.773Z] TOOL RESULT

```
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
1199:yewes-. Law. 1. Latin jis, law, and its derivative jirare, “to pronounce a ritual formula,” swear: JURAL, JURIST, JURY}; ABJURE, ADJURE, CONJURE, INJURY, JURIDICAL, JURISCONSULT, JURISDICTION, JURISPRUDENCE, (NON- JUROR), OBJURGATE, PERJURE. 2. Compound form *yewes-dik-, “one who shows or pronounces the law” (see deik-), in Latin jidex, judge: JUDGE; ADJUDICATE, PREJUDICE. 3. Suffixed form *yewes-to- in Latin jistus, just: sust!. [Pok. ievos 512.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1288:BEND! bhendh- BEND? bhendh- BENEATH ni BENEDICTION deik-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1503:FATE bha-2 FATHER peter- FATHOM pete- FATIDIC deik- FAUBOURG bhergh-?, dhwer- FAVA BEAN bha-bha- FAVOR ghow-é- FAVORITE ghow-é- FAWN! pek-t FAWN? dhé(i)- FAY} pag- FEALTY bheidh- FEAR per-4 FEASIBLE dhé-1 FEasT dhés- FEAT! dhé-1 FEATHER pet- FEATURE dhé-1 FEBRIFUGE bheug-! FECUND dh@(i)- FEDERAL bheidh- FEDERATE bheidh- FEE peku- FEEBLE bhlé-1 FEED pa-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
```


## [2026-09-05T17:32:27.055Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"deiḱ\\|dei\\^k\\|deiĝ\\|deik\" POK_01.txt | head -30; echo \"--- awk page for POK p.188: leaf = p+8 = 196\"; awk 'BEGIN{RS=\"\\f\"} NR==197' POK_01.txt | head -60"
}
```


### [2026-09-05T17:32:28.923Z] TOOL RESULT

```
993:Mal  —  das  andere  Mal^  (aus  diesem  korrelativen  Gebrauche  erst  scheint das  jener-deiktische  poln.  öw  und  das  ich-deiktische  serb.  bvaj,  ebenso nbulg.  -V  [*uo-s]  entwickelt).
2615:de-,  dO'  Demonstrativstamm,  z.  T.  ich-deiktisch;  Grundlage  verschiedener Partikeln.
2617:o-r.  -de  in  6-06,  '^-öe,  tö-ös  ,der  hier'  (ich-deiktisch),  iv&d-d€j  iv-d^sv-ds, xsl'de,  hinter  Akk.  der  Richtung,  z.  B.  dö^ov-ds,  ohov  Ss,  ohövös,  "A^vaC^e (*^&GvävG-Ö€),  wie  av.  vaesmdn-da  (arkad.  ^vgSa'  IJw  Hes.,  Umbildung von  -äs  nach  Doppelformen  wie  rcQoa&e  :  Ttgöa^a),  auch  in  ds-vgo  {öevrs nachgebildeter  PI.)  ,hierher*,  lat.  qiian-de,  quam-de  ,als  wie*  =  osk.  paUj umbr.  pane  ,quam',  ebenso  osk.  pwn,  umbr.  pon(n)e  ,quom*  {^qiiom-de), lat.  in-de  ,von  da*  {*im-de),  un-de  ,woher*;  gr.  6s  ,aber*;  gr.  örj  ,eben,  nun, gerade,  gewiß',  }j-dr]  ,schon*,  ifrsi-ö^  ,quoniam';  dal  hinter  Fragewörtern ,(was)  denn?';
2716:deik-  ,zeigen',  woraus  lat.  und  germ.  z.  T.  ,mit  Worten  auf  etwas  hinweise] sagen',  mehrfach  auch  ,das  Recht  weisen,  auf  den  Täter  hinweisej beschuldigen'  entwickelt;  Partiz.  Pass.  dik-tö-s;  dikä  ,Richtunj dik'ti-  ,  An  Weisung',  deiko-s  ,Richtung'.
2719:lat.  dlcere  ,sagen',  dlcäre  ,feierlich  verkünden,  zusprechen,  weihen',  oskJ deikum  ,dicere',  umbr.  teitu,  deitu  ,dicito',  ablautend  osk.  dicust  ,dixerit'^ umbr.  dersicust  ds.,  osk.  da-dikatted  ,dedlcavit' ,  lat.  diciö  ,die  Macht  eines Herrn  über  andere,  Botmäßigkeit,  Gerichtsbarkeit',  indicäre  ,anzeigen', index  ,Anzeiger,  Angeber;  Zeigefinger'  (wie  auch  ai.  deHnl  ,Zeigefinger^), iudex  ,der  das  Recht  Weisende',  vindex  (yindicäre  =  vim  dicere),  causidicus] über  urir.  *Ekuo-decas,  Lugudec(c)as  (Gen.  Sg.)  s.  unter  1.  dek-.
2728:Ob  deik-  und  deig-  aus  dei-  ,hell  glänzen'  (auch  ^sehen')  als  ^sehen  lassen, aufblitzen  lassen'  erweitert  sind?
2736:air.  deck  ,der  beste'  (=  lat.  decus);  auch  in  PN  Ecliuid  (^ekvo-de%-^ Gen.  Echdach,  Lnguid,  Gen.  Luigdech  (urir.  Lugu-deccas  mit  cc  =  k),  falls nicht  e  für  älteres  i  steht;  dann  zu  deik-  ,zeigen',  in  der  Bed.  ,befehlei
4083:i  (betont  zur  Verstärkung  eines  deiktischen  Wortes,  unbetont  hinter einem  relativ  gebrauchten  Wort) :
4087:air.  {h)l  deiktische  Partikel  und  Stützpartikel  vor  Relativsätzen;
--- awk page for POK p.188: leaf = p+8 = 196
iff  ,Gott,  Göttliches^  ausge.1 gangen,  sondern  (wie  d-av^ia  von  d^edo/uai)  stellen^  sich  zu  klr.  dyvl'ii] dyvyty  sja  , schauen^,  cech.  divam  se  ,schaue,  betrachte^,  das  sich  zu  ai.i di-de-ti  ,leuchtet'  in  der  Bed.  verhält  wie  z.  B.  mhd.  blick  , Glanz,  Blitz*"* und  ,Blick  der  Augen^,  nhd.  glänzen :  slav.  gl^dati  ,schauen^
erz-St.  *deien'  (thematisch  deino-,  dino-)  nur  in  der  Bed.  ,Tag^: ursprüngl.  kons,  noch  in  aksl.  dhnh,  Gen.  dhne  ,Tag';  ai.  dina-m  (bes. in  Kompos.  ;Tag',  lat.  nundinae  ,der  an  jedem  neunten  Tag  gehaltene^ Markt',  air.  denus  ,spatium  temporis',  tredenus  ,triduum';  alb.  gdJiinj , mache  Tag'  aus  *-di-n-iö]  hochstufig  lit.  dienäj  lett.  diena,  apr.  Akk.  f.  deinan ,Tag',  (Mühlenbach-Endzelin  I  432 f.,  Büga  Kalba  ir.  S.  227 f.);  got.  sinteins^ ,täglich,  immerwährend';  vielleicht  hierher  ahd.  len(gi)zin  ,Lenz'  aus' *langat-tin  als  ,lange  Tage  habend'.
Kretschmer  führt  gr.  Ttv-dagiöat  , Zeussöhne',  etr.  Tin,  Tinia  ,Juppiter' auf  ein  vorgr.  Tin-  ,Diespiter',  bzw.  ital.  *Dinus  (idg.  *din-  ,Tag,  Himmel') zurück  (Gl.  13,  111;  14,  303 ff.,  19,  207;  s.  auch  Schwyzer  Gr.  Gr.  I  65); aber  die  ältere  Form  ist  Tvvöaoidai!
r-Er Weiterung  dei-ro-,  di-ro-  in:
germ.  *tera-  (*dei-ro-)  und  *tlra-  (*diro-)  in  ahd.  ze7'z,  ziari  ,kostbar, herrlich,  schön',  ziari  ,Schönheit,  Zier',  ziarön  ,zieren',  mnd.  ter  , Glanz, Ruhm,  Gedeihen,  gute  Beschaffenheit',  tei^e  und  tlre  ,Beschaffenheit,  Art und  Weise',  ags.  as.  tir  ,Ehre,  Ruhm',  anord.  tlrr  ds.;  norw.  dial.  ür , Ausguck,  Spähen,  Leuchten,  Glanz',  tlra  ,gucken,  funkeln';
dazu  lit.  dyretij  dyrofi  ,gaffen,  lauern',  dairytis,  lett.  dairities  , umher- gaffen', apr.  endyritioei  (u.  dgl.,  siehe  Büga  Kalba  ir.  s.  227  f.,  Mühlenbach- Endzelin  I  432  f.)  , ansehen'  (aber  bulg.  diH  , suche'  bleibt  fern,  s.  Ber- neker  201);
toch.  A  tiri  ,Art  und  Weise'.
Über  hitt.  siwat-  ,Tag',  Hivanni-  ,Gott'  (aus  *dieu-?),  hierogl.-hitt.  tina- ,Gott',  §ijäri  ,erscheint'  (*diä-?)  s.  Pedersen  Hitt.  57,  175  f.
Zu  ai.  divyati  ,spielt,  würfelt'  (angeblich  ,wirft  das  Auge')  vgl.  mit anderen  Ablautstufen  dyütdm  , Würfelspiel',  ferner  devanam  ,das  Spiel, Würfelspiel',  und  oben  dyötate  ,leuchtet',  dyutih  , Glanz',  dyumdnt-  ,hell, licht'.  Ob  hierher  auch  av.  ä-dlvyeinti  ,bemühen  sich  worum'  als  ,es  worauf abgesehen  "haben'?  Vgl.  Wackernagel,  Berl.  Sbb.  1918,  396 f.
;.<^fc
-4
187
niß  unsere  Wz.  als  ^vibrierendes  Liclit^  mit  deid-  ,eilen^  wirbeln'  ursprgl.
eins  g-ev^-esen  sei,  scheint  denkbar
^VP.  I   772  f.,  WH.  I   345 f.,   347,   349  f.,   355,   357  f.,    727,    732,    860, Sclnvyzer  Gr.  Gr.  I
```


## [2026-09-05T17:32:57.337Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n=NR; if (index($0,\"deik-  ,zeigen\")>0) print \"LEAF(1-based NR)=\"n}' POK_01.txt"
}
```


## [2026-09-05T17:32:57.784Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2700,2760p' POK_01.txt"
}
```


### [2026-09-05T17:32:59.723Z] TOOL RESULT

```
LEAF(1-based NR)=198
LEAF(1-based NR)=201
```


### [2026-09-05T17:32:59.755Z] TOOL RESULT

```
eins  g-ev^-esen  sei,  scheint  denkbar
^VP.  I   772  f.,  WH.  I   345 f.,   347,   349  f.,   355,   357  f.,    727,    732,    860, Sclnvyzer  Gr.  Gr.  I  576  f.
deiO'  (diS't  ^l^'f  ^^')  >sich  schwingen,  herum  wirbeln  (halt,  und  z.  T. o-riech.);  eilen,  nacheilen,  strebend
Ai.  diyati  , fliegt,  schwebt-;  gr.  dZvog  m.  ,Wirbel,  Strudel;  rundes  Ge- fäß runde  Tenne',  dhf]  (Hom.),  äol.  dlvra  (vgl.  Jivvof.i€vrjgj  Hoffmann  Gr. P.  II  484)  ,Wirbel,  Strudel',  divio),  ölrsvo),  äol.  dlvvrjfiL  , drehe  im  Wirbel oder  Kreise,  schwinge';  intr.  ,drehe  mich  beim  Tanz  im  Kreise'; pass.  , treibe  mich  herum,  taumle  umher,  rolle  (die  Augen),  wirble  (vom Fluß),  drehe  mich  tanzend  umher',  divw  äol.  öivvu)  , dresche',;  liom. <J/w  ,fliehe',  d'iouai  ,jage  weg'  (mit  auffälliger  Verteilung  der  intr. und  tr.  Bed.  auf  Aktiv  und  Medium),  hom.  öiswai  ,sie  eilen',  öieod^ai ,fliehen',  evöisoav  ,sie  hetzten',  disgög,  (Ttovg)  ,flüchtig'  (nach  hre,  i'srai  :  uvrai zum  thematischen  d/firat  analogisch  disvxai  statt  *SlovTaL  neugebildet?),  dicü-acü , verfolge'  (kontaminiert  aus  ficj-KO)  und  öieaai,  Meillet  MSL.  23,  50  f., Schwyzer  Gr.  Gr.  I  702);  hom.  di'Cr^t.iai  (Fut.  bom.  öi^rjaofiai)  , strebe  wo- nach, bemühe  micli  worum,  suche',  nachhom.  auch  ,forsche'  (*di,-diä-(.iai), woneben  auf  Grund  von  '*öiG-to-  att,  t^rjTeo)  , strebe  wonach,  lasse  mir angelegen  sein';  ob  hierher  mit  ursprgl.  *did- :  l&It]  ,Sturm,  heftige  Be- wegung, namentlich  des  Meeres',  t,&Xog  , Strudel,  heftige  Bewegung  des Wassers'?
Vgl.  über  die  ^  enthaltenden   gr.  Worte  Schwyzer  Gr.  Gr.  I  330^  833.
Air.  dlan  , schnell',  dene  ,Schnelligkeit' ;  lett.  deju,  diet  ,tanzen',  diedelet , müßig  gehen'.  Über  lit.  dainä  , Volkslied'  (zu  dejä  ,Wehklage?')  vgl. Mühlenbach-Endzelin  I  432  mit  Lit.
Ganz  fraglich  cymr.  dig  ,böse',  russ.  dikij  ,wild',  lit.  dykas  , übermütig, mutwillig,  unbeschäftigt,  müßig',  lett.  dtks  ,frei  von  Arbeit',  aksl.  divhjh ,wild'  (Berneker  203  f.,  Mühlenbach-Endzelin  I  478,  Trautmann  54).
Nicht  hierher  gr.  döva^  ,Rohr'  (Jüngeres  ion.  öovva^  und  vereinzeltes dor.  dajva^  metr.  Dehnung?  Schulze  Qu.  ep.  205,  Boisacq  196),  dovscj , schüttle',  äXidovog  ,im  Meer  herumgetrieben'  und  lett.  duonis,  duoni , Schilf,  Binsen'.
WP.  I  774  ff.
deigh-  , prickeln,  kitzeln'?  , zwickendes  Insekt'. Arm.  tiz  , Zecke';
mir.  dega,  Akk.  degaid  (*digät-)  ,Hirscbkäfer'; germ.  *tlkan-^    mit    Intensivschärfung    *tikkan-y    in    ags.    ticia   m.    (lies
'''  4  i
tiica  oder  ticca),  engl,  tike  und  tick  , Holzbock,  Schaflaus^,  mnd.  Zec^^  ] m.  f.  , Holzbock',  nhd.  Zecke]  daneben  eine  Vermittlungsform  ^tikan-yi^  ! mnd.  teke^  mhd.  Zeche,  engl,  teke  ds. ;  ;:2^
norw.  dial.  tikka,  ndd.  tickeri  gleicht  anstoßen',  mhd.  zlcken  ds.;  ahi zecÄön  ,pulsäre,  necken,  plänkeln';  engl,  tickle  ,kitzeln';  nasaliert  ags^ tinclian  ds.
Ein  Zusammenhang  mit  dheig-  ,stechen'  ist  nicht  nachweisbar.
WP.  I  777.
deik-  ,zeigen',  woraus  lat.  und  germ.  z.  T.  ,mit  Worten  auf  etwas  hinweise] sagen',  mehrfach  auch  ,das  Recht  weisen,  auf  den  Täter  hinweisej beschuldigen'  entwickelt;  Partiz.  Pass.  dik-tö-s;  dikä  ,Richtunj dik'ti-  ,  An  Weisung',  deiko-s  ,Richtung'.
Ai.  didestij   disdti,   deiayati  , zeigt,   weist',   av.  daes-  Aor.  döU-  ;Zeig^ {daesayeiti,    disyeiti,    daedöiU)    ,zeigen ;    jemandem    etwas    zuweisen, sprechen',  Partiz.  ai.  distd-  (=  lat.  dictus) ;  dlsti-h  ,Weisung,  Vorschrift av.   ädiHi-§  , Anweisung,   Lehre'   (=  lat.  dicti-ö,  ags.  tiht  , Anklage',  ahc in-,  bi'Ziht  ds.,  nhd.  Verzicht),  ai.  dis-  f.  , Weisung,  Richtung',  diSä  .Richtum (=r  SUt]  ,Recht',  woraus  wohl  lat.  dicis  causa  ,nur  der  Form  wegen,  zuiä Schein'),  desd-h  ,(Richtung),  Gegend'  =  an.  teigr  s.  unten;
gr.  dsUvv[.iL,  sekundär  öeL-Kvvo)  ,zeige',  kret.  TtQO-öUvVTi  ,irtLÖsUwai^ öeT^ig  ,das  Zur-Schau-Stellen'  (mit  sekundärer  Hochstufe),  dUrj  s.  obei^ öUaLog,  ÖLTLccl^u),  SSrAog',  das  Perf.  Med.  öiösiyfxai,  und  dety^a  ,Beweis,  Bei^ spiel'  nicht  mit  idg.  g,  sondern   gr.  Neuerung;
lat.  dlcere  ,sagen',  dlcäre  ,feierlich  verkünden,  zusprechen,  weihen',  oskJ deikum  ,dicere',  umbr.  teitu,  deitu  ,dicito',  ablautend  osk.  dicust  ,dixerit'^ umbr.  dersicust  ds.,  osk.  da-dikatted  ,dedlcavit' ,  lat.  diciö  ,die  Macht  eines Herrn  über  andere,  Botmäßigkeit,  Gerichtsbarkeit',  indicäre  ,anzeigen', index  ,Anzeiger,  Angeber;  Zeigefinger'  (wie  auch  ai.  deHnl  ,Zeigefinger^), iudex  ,der  das  Recht  Weisende',  vindex  (yindicäre  =  vim  dicere),  causidicus] über  urir.  *Ekuo-decas,  Lugudec(c)as  (Gen.  Sg.)  s.  unter  1.  dek-.
got.  gateihan  ,anzeigen,  verkündigen',  anord.  tea,  jünger  tia  ,zeigen, darstellen,  ankündigen',  ags.  teon  ,anzeigen,  verkündigen',  ahd.  zlhan  ,an- schuldigen,  zeihen^,  wozu  anord.  tigenn  ,(*monstratus)  vornehm',  t'ign  f. ,Rang;  vornehmer  Mann';  ahd.  zeigön  ,zeigen',  wovon  zeiga  ,Weisung'; inziht  usw.  s.  oben;  ferner  anord.  teigr  m.  ,geradliniges  Wiesenstück' (,*Richtung'  =  ai.  desd-h  ,Gegend,  Platz,  Land'),  ablautend  ags.  tig,  tili , Anger,  Weide',  mnd.  tl{g)  m.  öffentlicher  Sammelplatz  eines  Dorfes', ahd.  zieh  , forum'.
,    Hierher  vermutlich  mit  der  Bed.  ,Finger'  (=  ,*Zeiger')  und  sekundär, aber  bereits  alt  ,Zehe',  ahd.  zeha,  ags.  tahe,  tä,  anord.  tä  ,Zehe'  {*döikuä),
189
nind.  teice,  nhd.  und  südd.  zewe  ds.  {*doik-ua),  und  das  wohl  aus  *dicitus Hurcli  Dissimilation  gegen  das  tonlose   t   entstandene   lat.  digitus  _,Finger,
Zebe^
flitt.  tek-kus-sa-nu-mi  ^maclie  erkennbar^  zeige^  hierher  nach  Sturtevant Lang.  6;  ^'^  ^^  227 ff.;  bezweifelt  der  Bildung  wegen  von  E.  Forrer  bei Feis°t  204.
Daneben  idg.  doig-  in  got.  taikns  f.  ^Zeichen,  Wunder^;  taikn  n.  ds., abd.  (usw.)  zeihhan  n.  _, Zeichen^,  ags.  txcan,  engl.  <eacÄ  ^lehren^^  anord. teikna  ^zeigen^  bedeuten^  bezeichnen'^,  ahd.  zeihhonön  ^zeichnen^,  got.  taiknjan «oio-enS  3-hd.  zeihinen  ds.
Aus  germ.  *taikna  stammt  finn.  taika-  ^Vorzeichens
Ob  deik-  und  deig-  aus  dei-  ,hell  glänzen'  (auch  ^sehen')  als  ^sehen  lassen, aufblitzen  lassen'  erweitert  sind?
WP.  I  776  f.,  WH.  I  348  f.,  351,  860,  Schwyzer  Gr.  Gr.  I  696  f.,  Feist 204,  472.
X.  dek-   ,nehmen,   aufnehmen',    daher  ,begrüßen,   Ehre   erweisend    Aus  der Bed.   ,annehmen,   gern   aufnehmen'   fließt  die  Bed.  ,gut  passend,  ge- eignet, sich  schicken,  ziemen,  es  jemandem  recht  machen;   als  unan- nehmbar darstellen,  etwas  einem  gut  scheinend  machen,  lehren,  lernen'; dekos-  n.  , Zierde,  Ehre'. Ai.  dasasydti  ,erweist  Ehre,  verehrt  einen  Gott,  ist  gnädig'  (Denomin. von   *dasas-   ==  lat.   decus),   dasä    f.    ,Zustand,   Schicksal';    av.   dasdm   n. ,Habe,  Vermögensstück';  ai.  Desiderat,  dlksate  ,weiht  sich',  dlksä  ,Weihe' (*di-dk-s-  mit   sekund.  i),   ddksati  ,ist  tüchtig,   macht  es  einem   recht,  ist gefällig',  ddksa-h  ,tüchtig,  geschickt'  (aber  av.  dax§-  ,lehren,  unterweisen', npers.  daxs    , Geschäft,   Mühe'    bleiben  wegen   des   Gutturals    fern),  dehn- stufig ai.  däsnötij  dästi,  däsati  ,bringt  Opfer  dar,  erweist  Ehre,  gewährt', däsvds-  ,die  Götter  ehrend,  fromm';  av.  däUa-    ,erhalten,  erlangt'  (Partiz.); nach  Frisk  Etyma  Armen.  25  f.  hierher  arm.  dncay  ,Gabe'  aus  *9nd-tiS' äti-  (urarm.  -tis-  aus  *dek-);  ob  auch  hierzu  tesanem  ,ich  sehe'?  (vgl.  unten doy.sva))',  anders  Meillet  Esquisse  135;
gr.  (ion.  äol.  kret.)  di-AOuai  ,nelime  an',  att.  öexo^iaiy  athemat.  hom.  3.  PI. dexazai  (das  x  nach  *d6x^w,  Infin.  dexd-ai)y  Aor.  dfxro,  Partiz.  dayf-ievog, vgl.  TtQOTiösyf^iaL'  TVQoaöexoficcL  Hes.  (yf.i  statt  zw);  das  x  ist  bewahrt  in öoKÖg  ,[Aüfnahme]  balken',  doKav  dri-Ar^v  Hes.  (daraus  lat.  doga  ,Gefäß'), doY,ävaL'  Ol  GTcclLusg  Hes.,  de^dl^a)  ,besteche',  ö(OQO-S6y.og  ,der  Geschenke nimmt',  ös^af.LBvr]  (Partiz.  Aor.)  ,Wasserbehälter',  ägt-deiycstog  ,ausgezeichnet' {et  metr.  Dehnung);  Nasalpräsens  *(J€txw^/at  (:  3ii.däsnöti)  im  Partiz.  ösluvv- y-^vog  ,huldigend,  grüßend',   zu  dsLytavöcowo   ,sie  begrüßten';    Intensiv   dst-
190
dsxaxai  d.s.,  ösi-diOM(j,ai  ^begrüße^  (für  *d>y-Jf (x)-c7xo/ia^  nach  den  Prj auf  -i(jA(x))\  dsi-  kann  dr}-  (idg.  e)  gelesen  werden,  ösi/.v-  auch  deY,v-,  xi^ dsLv,a-  kann  metr.  Dehnung  für  ösx,a-  sein  (Schwyzer  Gr.  Gr.  I  648,  697j1 Kausativ  doyiso)  (=  lat.  doceö  ,meine,  scheine^,  So-asl  fxoi  ,es  scheint  mij (,ist  mir  annehmbar');  Sö^a  f.  ^Meinung,  Ruhm'  (*dox-ö-ß),  döyi-ia  n.  ^Be Schluß',  ö6yciiJ.og  ,ansehnlich,  erprobt';  Soxevo)  ,beobachte',  TCQoa-doy.d(o  ,ei warte';  über  diddayco)  s.  unter  1.  dens-.
alb.  ndieh  ,sich  befinden'  (*deksk5-?)]  ndesh  ,an treffen'  wohl  slav.  LwJ S.  unter  des-;
lat.  c?ece^,  -ere  ,es  ziemt  sich,  ziert,  paßt  gut',  decus,  -oris  n.  ,Zierd( Würde',  dignus  , würdig'  (aus  *dec-nos,  eigentl.  ,geziert  mit');  umbr.  tigi decef/  (s.  dazu  EM.  257);  Kausativ  doceö,  -ere  ,lehre'  (,lasse  einen  etwj annehmen');  discö,  -ere,  didici  ,lerne'  (aus  *di-dk-skö)]  ;',_^
air.  deck  ,der  beste'  (=  lat.  decus);  auch  in  PN  Ecliuid  (^ekvo-de%-^ Gen.  Echdach,  Lnguid,  Gen.  Luigdech  (urir.  Lugu-deccas  mit  cc  =  k),  falls nicht  e  für  älteres  i  steht;  dann  zu  deik-  ,zeigen',  in  der  Bed.  ,befehlei
Vielleicht  hierher  germ.  *teh-uön  in  ags.  teohhlan,  tiohhian  ,meinen,  b( stimmen',  teohh,  tiohh  ,Schar,  Gesellschaft',  teon  (*tehön)  ,bestimraen^J ahd.  gizehön  ,in  Ordnung  bringen',  mhd.  zeche  , Anordnung,  Zunft,  Zeche, Gesellschaft',  nhd.  Zeche,  mhd.  zesem  (*teksma-)  ,ununterbrochene  Reihe' wozu  vielleicht  mit  Dehnstufe  (*tez-uö)  got.  tewa  ,Ordnung',  gatSwjan  ,an'- ordnen';   s.  darüber   auch   unter   deuä-  ,sich  räumlich  vorwärts   bewegen'
Unsicher   aksl.  desg,  desiti  ,finden',  skr.   de.nm  desiti  ,treffen',    refl.  ,je- mandem  begegnen',  cech.  po-desiti  und  u-desiti  ,einholen,   erwischen'; lautend  russ.-ksl.  dositi  , finden,  begegnen';  s.  auch  unter  des-.
Toch.  A  täk-  ,urteilen,  entscheiden';  zweifelhaft  A  täskmäm  {^täksk-märrif ,ähnlich',  Van  Windekens  Lexique  137;  Pisani  Rc.  R.  Ist.  Lomb.  76,  2,  30.
Zum  es-St.   ai.  dasas(ydti),    lat.  decus  stellen   sich   auch  die  Worte   für; ,rechts'  (Specht  KZ.  62,  218).
deks-  mit  verschiedenen  Suffixen:
Ai.  ddksina-j  daksind-  ,rechts,  südlich,  geschickt',  av.  daHna-  ,rechts', lit.  desinas  diS.,  dekinl  ,die  rechte  Hand',  aksl.  desm  ,rechts';  gr.  de^Liegög =  lat.  dexter,  -tra,  -trum  (Komp.  dexterior,  Superl.  dextimus),  osk.  destrst (abgekürzt  für  *destrust)  ,dextra  est',  umbr.  destrame  ,in  dextram';  gr. ds^tog  ,rechts,  glückverkün*lend,  geschickt,  gewandt'  (von  de^i-  mit  For- mans -fo-j  vgl.  gall.  Dexsiva  dea);  (das  Suffix  -uo-  wohl  nach  HaiuoSy skai-uos  ,links')  air.  dess  ,rechts,  südlich',  cjmr.  deheu  {*deksovo-)  ds.,  got taihswa,  ahd.  zeso  ,rechts',  got.  taihswö-  ahd.  zes{a)wa  ,die  rechte  Hand'; alb.  djathte  ,rechts'  (das  von  G.  Meyer  damit  gleichgesetzte  ksl.  desh  ist wohl  Verderbnis  für  desm,  s.  Berneker  187).
191
^yp  I  782  f.,  WH.  I  330  f.,  346  f.,  Trautmann  53,  54,  Schwyzer  Gr.  Gr. «4^    (378    684^  697,  Wistrand  Instrumentalis  14  ff.
j  ^.  (:dok-,  dek-)  ^reißen,  zerreißen,  zerfasernd ^*  \[  dasä  ;die  am  Ende  eines  Gewebes  hervorragenden  Zettelfäden, r-ansen^;  ir.  dual  ,Locke^  {*doklo-)\  got.  tagl  n.  ,einzelnes  Haar^,  anord. titql  u.  ,die  Haare  im  Pferdeschwanz*^,  ags.  tcegl  (engl,  tau)  m.  _,Sch\vanz^,. alid.  2rt^e^  ,Sclnvanz,  Stachel,  männliches  Glied,  Rute^;  got.  tahjan  ,reißen,. zerren^,  distahjan  ,zerstreuen^,  isl.  tcßeja,  täa  ,karden^,  norw.  dial.  tceja (* tahjan)  und  taa  (*tahön)  ,fasern,  zerreißen^;  anord.  tag,  Fl.  tceger  und lagar  f.  ,Faser^,  mhd.  zäch,  zähe  f.  ,Docht,  Lunte^;  in  anderer  Bed. (zerrend  —  ziehend,  hinausziehend^)  norw.  mdartl.  taag  ,langsam  und andauernd^,  mnd.  tege,  ostfries.  tage  ,zähe^  und  ahd.  zag  ,zögernd,  unent- schlossen, zaghaft^,  wozu  zagen  ,verzagt  und  unentschlossen  sein';
vielleicht  hierher  als  ,woran  man  sich  reißt^  oder  ,abgerissenes,  rissiges StücV,  mhd.  zacke  m.  f.,  nhd.  Zacke,  mengl.  takke  ,fibula^,  engl,  tack Stift,  kleiner  NageF,  mit  anderem  Auslaut  tagg,  tagge  m.  ,hervorragende- Spitze,  Zacke^;  oder  gehört  Zacke  zu  lett.  degums  ,Nase,  Schuhspitze^?
S.  auch  unter  denk-.
WF.  I  785.
dektn,  dekm-t,  deku-  ,zehn',  Ordinale  dekeino-s,  dekmto-s.
Ai.  ddsa^  av.  dasa;  arm.  tasn  (nach  Meillet  Esquisse  42  aus  *djc-j. wie  russ.  (tri)dcath  ,S0'  aus  (tri-)dbseti),  gr.  öixa,  lat.  decem  {denl  ,je  zehn^ aus  *dek-noi]  PN  Decius  =  osk.  Dekis,  Gen.  Dekkieis),  osk.  deketasiüi, Nom.  PI.  degetasiüs  ,curatores  decimarum^  (*deken-täsio-),  umbr.  desen-{duf) ,duo-decim^,  air.  deich,  cymr.  deg,  corn.  bret.  dek,  got.  taihun  {-n  wie  in sihun,  niun),  an.  tiu,  ags.  tien,  tyn,  as.  tehan,  ahd.  zehan  {a  wohl  aus  den Kompositis,  Brugmann  II  2,  18),  toch.  A  säk,  B  &ak-^  finn.  deksan  ,10^ ist  nach  Jokl  Pr.  ling.  Baudouin  de  Courtenay  104  aus  dem  Idg.  entlehnt).
Auf  das  Zahlsubstantiv  dekm-t(i),  eigentl.  , Dekade^,  gehen  zurück:
ai.  dasat-,  dasati-  f.  , Dekade',  alb.  djete,  gr.  ösxdg^  -adog  (zum  a  s.. Schwyzer  Gr.  Gr.  I  498,  597),  got.  tdihun-tehund  , hundert'  (eigentlich jZehn  Dekaden'),  anord.  tiund  f.  ds.,  apreuß.  dessimpts  ,zehn',  lit.  de- Hmt,  alt  deHmtis,  lett.  alt  desimt,  metath.  desmit,  alt  desmits  (vgl.  desmits^ m.  f.  , Zehner');  aksl.  desetb  (kons.  Stamm  auf  -t,  Meillet  Slave  comm.^  "^^8);
deku-  wohl  in  lat.  decuria  , Zehntschaft'  (daraus  entlehnt  nhd.  Decher  m. ;Zehn  Stück';  spätlat.  *teguria  wii-d  durch  Schweiz.  Ziger  ,zehn  Pfund  Milch^ vorausgesetzt;  wohl  mit  mhd.  ziger  , Quark'  identisch)  =  umbr.  dequrier^ tekuries  ,decuriis,  Fest  der  Dekurien';  vgl.  osk.-umbr.  dekvia-  in  osk.  (via} Bekkviarim  ,(viam)  Decurialem',  umbr.  tekvias  ,decuvias';  dazu  wohl  germ..
192
*tig2i-  , Dekade'  in  <^ot.  fidwor-tigjus  ,40,  aisl.  fjörer-tiger,    ags.  ßower-ti^ abd.  fior-zug   ds.     ��ltere    Erklärungen    bei   WH.  I  327  f.  und   Feist  If S.  aucb  unten  unter  centuria  u.  Kluge ^^  unter  Becker.
Ablautendes  (d)ktpt'  (Dual),  {d)komt'  (Plur.)  in  den  Zebnerzablen  (^^ die  Bildungen  bis  50  sind  als  idg.  nacbweisbar),  z.  B.  ai.  trimsät  ,30', d-risqsj  arm.  ere-surij  griecb.  TQLd'KoiTa  (aus  *-xcüyra;  Näheres  bei  Schwyj Gr.  Gr.  I  592),    lat.  tri-gintä    (mit  unerklärtem  g),    gallo-lat.  Abi.  PI. oOiS^Tis,'  air.  tmcho  (mit  l  nach  tri  ,3'),  bret.  tregont   (*tri-komt-es),  acymj trimuceint  (in  der  Endung  nach  uceint  ,20*);   s.  auch   unter  ut-kmit  ,1
Ordinale  dekei^os  und  dekm-to-s:
dekeinO'S  in  ai.  da§amdhy  av.  dasdraa-,  osset.  däsäm]  lat.  decimus,  davo!
decumänus  ,zum  Zehnten  gehörig',  später   ,ansehnlich',  osk.  Dekm-anmii{
*Decumaniis^j  vgl.  auch  EN  DecumiuSj  daraus  entl.  etr.  tecumnalj  rilcy
```


## [2026-09-05T17:33:14.507Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==76' HUB.txt"
}
```


## [2026-09-05T17:33:15.347Z] TOOL CALL #14: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T17:33:15.989Z] TOOL RESULT

```
— 65 -
aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
das haufig vorkommt, auf mp. dsh zuriick?
589. Bei Rosen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
Weise', zd. dis Veisen', osset. dwd%8}n zeigen u. &. w.
Also doeh -dEs = zd. ^da^a-, auch wenn dies nicht
rait daesa- yt. 13, 104 (*Traumbild'?) identisch ist.
594. Wenn dBz, deza *Kochtopf zu got. deigan *kneten, aus
Thon formen* (Wzl. dhig%) gehOrt, ist es verwandt mit
Nr. 563 diz, dSz *Burg', s. oben. Ob auch deg *Koch-
topf dazu gehort, ist fraglich, da 1) idg. dhig^h durch
skr. dBgdhiy digdha- nicht gesichert ist (vgL Brug-
mann, Grundriss I, p. 344) und 2) idg. dhoi^ho- im
Neup. zu *d^y werden miisste. Np. d^ (afgh. LW.
dEg *Kesser) setzt ap. ^daika- voraus. Phi. dSg 'Kesser
(Gl. and Ind. 288) kann eine junge Form sein. Zu d.
Tiegel u. s. w. vgl. Kluge, Wb. 5. Aufl. s. v.
595. Piige hinzu : paz. dddlgar ^secondly, other' Shk. 240,
Min. Gl. 53, did 'second' Shk. 241, Min. Gl. 61, dadum
'second' Shk. 240. Dieses paz. did ist direct = ap.
duvitiya- *der zweite . Vgl. WZKM. 5, 262.
596. Die kurdische Form lautet dem *Gesicht' bei Socin,
kurd. Sammlungen II, p. 307 ; afgh. lies ISmq.
599. Besser *daidavara- (Fe&tungBmsiuer*)^) Sils *daigavara-
anzusetzen, vgl. oben Nr. 594 und 563. Anders Fr.
Mil Her, WZKM. 8, 95 {^daya-vara- *Scheidemauer).
Falls dtvar (mit i) die urspriingliche Form ist (vgl.
afgh. LW. dlval *a wall'), ware dUvdr iiber *diyvar =
*did-vclr auf ap. *dida-vara- zuriickzufiihren. Alles
unsicher. Nebenform dwal JRAS. 1893, 463.
600. NSldeke macht mich darauf aufmerksam, dass im
ersten Verse von Vis u Ramin ra Dativpartikel (und
niar an Nominativ) ist.
>) Vgl. bara I diz *Mauer der Festung' Fird. I, 452, 325.
HUbsohmann, Peraisohe Studien. 5
```


### [2026-09-05T17:33:17.676Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
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
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
```


## [2026-09-05T17:33:27.640Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=368 && NR<=372 {print \"=== leaf \"NR-1\" ===\"; print}' BQT_v2_pages.txt | head -160"
}
```


### [2026-09-05T17:33:29.334Z] TOOL RESULT

```
=== leaf 367 ===
‫دي‬                                                                                     ‫=‬

‫‪ » ۱‬بروزن افزوده » بمعنی‬      ‫دوه‬
                                ‫ده ب‬             ‫و تحتانی بواو مجپول رسیده و بای فارسی‬
                   ‫عشر باشد که ده بك است ‪.‬‬                          ‫مفتوح مدال ابجد زده ا‬
                                                ‫»مر‌معروف واهی‌منکررا‬




                                     ‫بیان بیست ویکم‬


‫ماه دهم باشد از سال شمسی ‪ ,‬وآن مدت بودن‬
                                                 ‫دی = بقتح اول وسکون انی‪ .‬نام‌ملکی‬
                                                 ‫است که تقددس امور و مصالح دیماه و روز دی‬
‫وتام روزنهم ‪ ۴‬ازهرماه فارسی » ودرین روز ازماه‬
‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
  ‫ظ‪ ,‬ممحف « دهوبه »‪ .‬این‌کله درعصر ساسانبان ویز در قرنهای اول اسلام معمول‬         ‫‪۱‬‬
 ‫بود ‪ .‬درالفهرست ابن‌الندیم(چاپ مصري ‪ )۸۳۳‬در موضوع اقل‌دبوان عرب ازفارسی بعربیآمدد‪:‬‬
  ‫صالح‌بن عبدالرحمن مولی‌بنی تمیم که" زیر دست مردایشام بر للفيخ صاحب دیوان حجاج بود‬
  ‫‪ :‬کیفتصنع بدهویه وششوبه؟‬           ‫قیول کرد که آنرا از فارسی بعربی بگرداند ‪ .‬رونام‬
     ‫قال ‪ :‬اکتب عثراً و نصف عشراً » در اینجا ظاهراً ششوبه مصحف « پنجوبه » است »ببااازب‬
  ‫مضیقه در اصطلاح عربی » تاگزیر شده صف عثر را بجای « شثوبه » بشنهاد کند ‪ .‬مب لمات ‪.‬‬
  ‫‪ - ۴‬دراوستا _تاکناا‪ 21‬با ‪ 2۷01021-‬بمعنیآ فربنندہ‪.‬‬    ‫‪ ۴‬هشتم صحیح‌است‪.‬‬
  ‫دادار و آفریدکار است و غالبا صفت اهورمزداست و آن ازمصدر ‪ 21‬بمعنی‌دادن وآفربدن است‪.‬‬
  ‫دی) برای تعین دهه‌ین ماه استممال شده ‪ .‬درمیان سی روز مامه‬      ‫در خود اوستا صفت دئوش [‪-‬‬

  ‫روزهای هشتم و پاتزدهم وبیست وسوم به دی( د=ئوش) موسوم است بنا بر تسمیه بنام ختا‪ .‬برای‬
  ‫بقیه درصفحةٌ ‪۸۰٩‬‏‬
                                                                          ‫‪4۰٩‬‏‬    ‫حة‬
                                                                                   ‫صبهفاز‬
                                                                                        ‫بق‬
       ‫رك ‪ :‬خاله گیر ء ده هزاران ‪.‬‬     ‫‪۸‬‬         ‫‪۲٩‬‏ ‪.‬‬   ‫‪:۸۹‬‬   ‫معرب آن دهنج‪ « .‬دزی ح ‪ ۱‬ص‬
        ‫عبارآن‌هفت دهم (طلامانقره) بوده‪.‬‬   ‫نی‬            ‫‏‪ ٩‬رك‪ :‬ده هزار خانه گیر‪.‬‬
  ‫‪ 0‬و بکشید ‪ « :‬و حن ( سلیمان ) گفت ‪ :‬دهید و حشمتی بزرکه افکتید بکشتن‬
      ‫بیار که کنید ‪ .‬تا یس از این دتدانها کند شود از ری» «تاریخ بیهقی ص‪ ۳4‬متن وحاشیه» ‪.‬‬
     ‫=ه بسعنی ناحیه وکشور ) [ رك ‪:‬ده ]‪= +‬‬
                                        ‫(ي‬
                                         ‫از ‪ :‬دهیو د‬             ‫=یت‬
                                                                   ‫دیوهیدیو‬
                                                                          ‫‪ -۴‬ده‬
  ‫یت (‏ بد سدواادرندکی ) مالك و فرماتروای تاحیه یاکشور ‪ ۰‬ودهیویدبه اسم عصدر آست‬
   ‫ومعرب وی « دهوفذیه ‪٩.‬‏ بیرونی گوید ا(رآالباقیه ‪ « : )۲۲-۱۲‬الدحوفذيه معناها حفظالدیا‬
  ‫حوراستها و التأمر فیها‪...‬فاما الدهوفذبه‌فقد صدرت عن اوشهنج ( هوشنگه ) > ‪ .‬ازعهد بيار‬
   ‫از ضی‌مستنی بر چپارمتخش‬   ‫جاهعة دودمالی تشکیل داده بودند که ازجهت تقیمات‬      ‫کپن ابرانیان‬

     ‫بود » اینچنین ‪ :‬خانه (‪ -‬هط‪ , )۳۳‬قربه (‪ . )8۷-‬قبیله ( ا‪ ) 242‬و کشور ( تاه‬
           ‫کربستنن ‪ .‬ساسان ‪۵۱٩‬‏ ودهیوید ( دهیویت ) رئیس کشور وناحيةٌ بزرگك بوده است‪.‬‬
                                      ‫‪ #‬دهن ‪ -‬بفتح اول و دوم» مخفف دهان (ه م‪.).‬‬

=== leaf 368 ===
   ‫سره‬                                                                                                         ‫دبافودا‬

‫دابا * = بروزن زببا ‪,‬قماشی باشد از‬                                               ‫اول رو ز گذشته را گوند ‪. ۱‬‬

‫ونابه از دیدارخوبان همهت ‪.‬‬
                         ‫حربرالوان ‪ -‬ک‬                      ‫دیاقود‪ - ۴ )۵‬بنتح اول و انیبالف‬
‫دییاجی ‪ = ۱‬بروزن تیماجی» دیبایاف‬                            ‫اقطه بالف‬    ‫دال ‪۳‬‬    ‫و‬       ‫کشیده و قاف بواو زسده‬

‫راگوند بعتی هرچه آزدیبا بافته شده باشد ‪#.‬‬                   ‫را گونند‬    ‫خشخاش‬     ‫‪ ۰‬بلغت عودانی شرت‬             ‫کشده‬

                                                             ‫که ازیوست خشخاش بخته باشند نهازشم آن‪:‬‬
‫دیبادین ‪ = ۳‬بفتح اول ودال دیگر بر‬
‫وزن شرم کین » نام فرشته است ‪ -‬و مکی از‬                      ‫دیا وش س با نون بر وزن قبایوش »‬
‫نامهای‌الهی هم هت ‪ -‬ونام روز بیست وسیم(‪)۱‬‬
‫از دیماه مغان‬    ‫روز‬       ‫در ین‬   ‫‪۰‬‬   ‫باشد ازهر ماه شمسی‬    ‫خشکی ودربا دزدی وراهزنی میکردند ‪ ۰‬وبصنی‬
‫روز‬     ‫بتن‬
          ‫دكراس‬
              ‫جشن سازند و عید کنند و لي‬                         ‫کگوبند دام شخصی است که عذرا را بفروخت ‪.‬‬
‫دعا کردن بجهت دفم شر شیاطین واز حق تمالی‬                     ‫دیب = پکسراول بروزن‪ :‬سیب » بندری‬
                                       ‫فرزند درخواستن ‪.‬‬
                       ‫‪۱‬‬                    ‫‪۰‬‬                      ‫باشد ازبنادر هند ‪ -‬ودر ترکی‌بیخ وین ه‬
                                                                ‫چریز‬
‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬

                                                                          ‫(‪ )۱‬چك‪ :‬ببست وسوم ‪.‬‬
  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
       ‫‪4:۲۰ ۶۸‬‬   ‫‪ .‬ورك‪ :‬دزی حاص‬             ‫‪۱۸۱‬‬    ‫(فر) «لك‪۲‬ص‬    ‫‪60062‬‬       ‫‪Ff‬‏ —‬              ‫‪.‬‬    ‫داسشق ‪۰۹۵۰‬‬
   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
  ‫‪ - ۴‬درترکی ‪ :‬شایستگی‪ ,‬خوشبختی؛ ته " پ »ا پابه «جفتابی‬                               ‫م«اللهند ص ‪ ۰۸‬ی ‪٩‬‏ > ‪.‬‬
      ‫* ‪ -‬بهلوی ‪ « 081‬تاوادیا ‪ ۰ ۰۹۱‬از هندی باستان ‪802۷010 . 01 -‬‬                                          ‫‪.‬‬         ‫‪۳‬‬
   ‫‪ .‬رجه اشتقاق آن قطعی ليست‬                        ‫( زبانه کشیدن » پرتو افکندن » درخشیدن) ‪٠‬‏ ارمنی ع‬
   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
  ‫‪ 06.‬است «اسفا ‪ ۲: ۱‬ص ‪ > ۵۷۱ ۰ ۱۷۱‬وآلرا از ربشة‬                            ‫‪06‬‬
                                                                             ‫‪.‬زو اول آن‬
                                                                                      ‫دیباح است ج‬
      ‫‪ ۷001۱ ,‬اکدی گرفته‌اند < فاب ‪۱‬ص ‪> ۲۱۱‬رك‪:‬‬                     ‫تالا سومری (لوحه ‪ .‬خط ) و ا‪00‬‬
                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
                                                                                      ‫‪.‬‬    ‫رك ‪ :‬دی‬   ‫‪ ۷‬س‬

      ‫‪ #‬ویاچه = بکس اول وینجم (درلهجة مر کزی) » از ‪ :‬دیبا( ه‪.‬م‪ +) .‬چە ( توب‬
  ‫آبنباجة « دزی ج ‪ ۱‬ص ‪۱۲٤:۲‬‏ »‪ .‬آنجه کهدرآغاز کتاب‬
                                                 ‫تصغیر ) « اسشق ‪» ۱۰‬؛ معرب د‬
                                                                         ‫برای تفهیم موضوع کتاب نویسند ‪.‬‬
                                                                                               ‫یه از صفحهٌ ‪۷۰٩‬‏‬

  ‫اینکه سه روز موسوم به«دی» باهم اشتباء نشوندنام‌هريك رابنام روز بعد بپیوندند مثلاروز هشتم‌را‬
   ‫«دی بآنر» و روز پاتردهم را «دی بمهر» و روز بیت وسوم را «دی بدین» با « دیبا دين » گوشد‬
   ‫وکاهی نیز دئوش ( دی) را درفارسی «دین» کفته‌اند و دین‌بآنر ودیبا دين ازشروست ولی‌ترجمة‬
   ‫صحیح دئوش«دی» است ‪ .‬ابورحان بیرونی درفهرست روزهای ابرانی هشتمن روز را « دی‌بآذر »‬
   ‫مشتهااص‪ « »4 ۲‬خرده اوستا‬                ‫ورده‪ ۶ .‬روزشماری ‪۵۲-۹۲‬‬       ‫و درسفدی «ادست؟ و درخوارزمی«دنو»‬
                                                                                ‫ص ‪ « ۳۱۲‬فاب ‪۱‬ص ‪۷۲‬؟‪.‬‬

=== leaf 369 ===
   ‫دور‬                                                                                                     ‫سس‬
 ‫اس * ‪ -‬برای بیقطه وجیم‬
                      ‫جیبر‬
                         ‫د‬                              ‫بروزن سودا کر ‪ ۰‬تلم روز هشم است ازهر ماه ‪.‬‬

 ‫بالف کشیده و سین مپمله و حرکت مجهول ‪.‬‬                   ‫شمسی و دربن روز ‪.‬از ماه دی که دیماه ماشد‬
           ‫بلغت ہوتانی نوعی از مرقشیشا باشد ‪.‬‬            ‫فارسیان عکیندند وجشن سازند بنا برقاعده‌کلیه‬
                                                        ‫که مبان ابشان معمول‌است‪.‬ونام ملکی است که‬
‫وسر میم‬
      ‫دی بمهر ‪ - ۱‬بفتح اول ک‬
                                                             ‫امور ومصالح اين روز بدوتعلق دارد‪ .‬ونيك است‬
 ‫وسکون ها ورای قرشت » نامی است از امهای‬
                                                         ‫درین‌روزصدقهدادن ابزهرتندرستی خود وفرزسدان‬
 ‫الهی ‪ -‬ونام فرشته‌ابست‪ -‬ونام روز پاتزدهم جود‬                                                          ‫ودعا کردن ‪.‬‬
‫هزاه دی‬
      ‫از هرماه شمسی » ومغان این روز را ا‬
 ‫مبارك دانند وجشن کنند وعیدسازند وصورتي از‬                   ‫دبال = بروزن تیتال‪ ,‬نام شخصی است‬
   ‫ننرد‬
      ‫هه گ‬
         ‫ارا‬
           ‫گل با از خمیر نان بازند و در‬                  ‫ودیبال پور که قصبه ابت در ملك‌پنجاب‪ .‬اوبتا‬
                                                                                                           ‫کرد ‪.‬‬
 ‫وتعظیم کنند چنانکه ملوك وسلاطین را میکنند‬
  ‫ومد ازآن بوزانند ‪ ,‬وفطام فرسون درین روز‬                ‫دیباو ند ‪ - ۱‬بروزن خویشاوند‪ .‬لقب‬
 ‫بوده بعنی درین روز از شیر بازشده و درین روز‬             ‫طهمورت دیوبند است » و مفنی آن تمام سلاح‬
 ‫ب رگاو نشسته وزردشت درین روز از ابران ببرون‬                                                                ‫باشفد ‪.‬‬

 ‫هکه سوسن‌دود‬
            ‫‪.‬وبند در شب ابن روز ر‬
                                ‫رفت ک‬                    ‫دییاه ‪ ۴‬د بروزن بیراه" نوعی آزقماش‬
 ‫کند تمام سال بفراغت کذراند و از قحطی‬                                                         ‫کران مابه است ‪.‬‬
 ‫و دروشی ایمن باشد وهر که بامداداین روزسیب‬
‫بخورد و ر گس ببوید تمام سال بی آزار باشد‬
                                                         ‫رته ‪ -‬دببابرا‬
                                                                     ‫دیبای پخته پدخ‬
 ‫وبراحت بگنراند » ودرین روز نك است صدقه‬
                                                                  ‫گوبند کهتاروپودش هيچيك خام نباشد ‪.‬‬
                ‫دادن وتزد ملوك و بز رکان رفتن ‪.‬‬          ‫دییدار ‪ ۴‬س بکر اول و دال ابجد‬
                                                         ‫بالف کشیده بروزن پشکار‪ .‬درختی است که آنرا‬
‫د لبه ‪ - ۲‬باظهار های هوز‪ .‬مخفف دیباء‬                      ‫مراف و جرال غوانته ‪۰:‬و آن نویر‬
 ‫است که نوعی از قماش اببشرمی کران بها باشد‪.‬‬              ‫هندی است‌وآ ترادبودار نگیوزنند چه درفارسی‬
                            ‫وممربآن دییق است ‪.‬‬
                                                                      ‫بای ابجد و واو بهم تبدیل می‌بابند ‪.‬‬
‫تیب خسر وی ‪ -‬باخای شلمدار (‪)0‬‬
                                                         ‫ذییك یی" ‪ -‬بنتح اول بروزن سرزمین »‬
 ‫وسین و رای بی‌نقطه (‪ )۳‬بروزن جيفةٌ دییوی »‬              ‫دامی است ازاسمای الهی‪ -‬و نام فرشته‌ای هم‌هست‪.‬‬
  ‫نامگنج دیبه است که کنج سیم (‪ )4‬اگزنجهای‬                ‫‪۰‬‬     ‫ولم روز ست وسم )‪ (۱‬باشد ازهرماه شمسی‬
                                                                                                  ‫ل‬
                         ‫خرو پرویز باشد ‪.‬‬                    ‫ودرین روز ازدیماه مقان‌عید کنند وجشن سازند‪.‬‬
  ‫بحو ر ت بفتح اول وضم جيم بورزن‬
                               ‫د‬                        ‫يك است درین روز دعا کردن و از خدا فرز لد‬

 ‫طیفور » شبی را گوبند که بغامت سیاه و تلريك‬              ‫خواستن » و بعضی کوبند نامروز بیست و هفتم‬
```


## [2026-09-05T17:33:36.578Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /دیس|دیز|تندیس|طاقدیس/ {print \"LEAF \"NR-1\" (printed ~\"NR-1+543\")\"}' BQT_v2_pages.txt | sed -n '1,60p'"
}
```


### [2026-09-05T17:33:39.192Z] TOOL RESULT

```
LEAF 13 (printed ~556)
LEAF 21 (printed ~564)
LEAF 63 (printed ~606)
LEAF 65 (printed ~608)
LEAF 70 (printed ~613)
LEAF 79 (printed ~622)
LEAF 97 (printed ~640)
LEAF 111 (printed ~654)
LEAF 145 (printed ~688)
LEAF 149 (printed ~692)
LEAF 152 (printed ~695)
LEAF 169 (printed ~712)
LEAF 225 (printed ~768)
LEAF 284 (printed ~827)
LEAF 310 (printed ~853)
LEAF 314 (printed ~857)
LEAF 335 (printed ~878)
LEAF 339 (printed ~882)
LEAF 365 (printed ~908)
LEAF 372 (printed ~915)
LEAF 373 (printed ~916)
LEAF 374 (printed ~917)
LEAF 378 (printed ~921)
LEAF 395 (printed ~938)
LEAF 400 (printed ~943)
LEAF 405 (printed ~948)
LEAF 413 (printed ~956)
LEAF 433 (printed ~976)
LEAF 450 (printed ~993)
LEAF 458 (printed ~1001)
LEAF 503 (printed ~1046)
LEAF 514 (printed ~1057)
LEAF 548 (printed ~1091)
LEAF 549 (printed ~1092)
LEAF 571 (printed ~1114)
LEAF 587 (printed ~1130)
LEAF 607 (printed ~1150)
LEAF 612 (printed ~1155)
LEAF 623 (printed ~1166)
LEAF 627 (printed ~1170)
LEAF 630 (printed ~1173)
LEAF 661 (printed ~1204)
LEAF 663 (printed ~1206)
LEAF 672 (printed ~1215)
LEAF 675 (printed ~1218)
```


## [2026-09-05T17:33:42.548Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=371 && NR<=376 {print \"=== leaf \"NR-1\" ===\"; print}' BQT_v2_pages.txt"
}
```


### [2026-09-05T17:33:44.271Z] TOOL RESULT

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/blfh7kwa9.txt

Preview (first 2KB):
=== leaf 370 ===
 ‫=‬                                                                                                    ‫دیع‬

‫دیده بان ‪ ۲‬س بروزنبی‌زبان» همان‬                           ‫یدبدا س بفتح اول بروزن شیدا » بمعنی‬
            ‫دیدیان است که بعربی ربیثه خوائند ‪.‬‬                                      ‫وم شده باشد ‪.‬‬
                                                                                                ‫تاپیدا ک‬
‫دید بانان عالم ت کنابه از هفت‬
                                                          ‫د دار ‪ ۱‬عم بر وزن دیوار » ترجمهةٌ‬
‫ک وکباست کهزحل‌ومشتری‌ومرشو فتاب‌وزهره‬                     ‫روت است ‪ -‬وبمعنی رخ وروی وچهره باشد ‪-‬‬
                             ‫وعطارد وماه باشد ‪.‬‬           ‫ویمعتی رخ لمودن ردیدن هم هست ‪ - ۴‬وچشم‬
‫دید م بان فلك ‪ -‬کنابهاز کوکبزحل‬                           ‫ویاعيننند ‪ -‬و ببنابی‬  ‫خرب‬
                                                                                  ‫کاویبزندکه یم‬‫ر‬
                    ‫است که درفلك هفتم میباشد ‪.‬‬             ‫وقوت باسرء رایز کفته‌اسوبمعنی پیدا ویدیدار‬
 ‫دیده بان کبود حصار ک‪-‬نابه‬                                                                          ‫همهت ‪.‬‬
‫از زحل است ‪ -‬وهربك اکزواکب سبع سیاره‬                       ‫بابای‌ابجدبروزن رسمان‪,‬‬        ‫دید بان ‪۴‬‬
                          ‫را بگیوزبند ‪.‬‬                  ‫شخصی را کویند که برجای بلند مانند سرکوه‬
‫‪ ۵‬بك ه بر داشتی د کنابه از منتظر‬                           ‫و بالای کشتی شیند وهرچه ازدوربیند خبردهد‬
                      ‫بودن وانتظار کشیدن باشد ‪.‬‬                          ‫نند ‪#.‬‬   ‫ایه‬‫ور‬
                                                                                      ‫خریی‬
                                                                                         ‫و او را خ‬
‫دة لشت = منم بای فارسی ‪ .‬اشاره‬
                             ‫د‬                             ‫‪ ۵‬بد ه = بااول بثالی رسیده وفتح‌ثالك‬
        ‫بمنفذ سفلی است که صوراخ مقعد باشد ‪.‬‬
...
</persisted-output>
```


## [2026-09-05T17:33:50.104Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دیس\" BQT_v2_pages.txt | head -40"
}
```


### [2026-09-05T17:33:50.157Z] TOOL RESULT

```
585:    ‫نرها در رسالهٌ پهلوی « باد کارزربران » ( رك ‪ :‬مزدیسناص ‪= ۲۹۳‬‬
1044: ‫وقايم (‪ )4‬و مسکم گردیدن چیزی باشدیسیب‬                          ‫وها ولون وکاف فارسی بر وزن خشمآ کند ›‬
3553:    ‫سوکون ثالیویون کواف » ناکمرجای‬                      ‫وزن دیگر» بمعنی فرادیس بودکهجمم فردوی‬
3957:‫مخفف چاشت دان ات » و آن ظرفی باشدکه‬                     ‫‪.‬‬    ‫حیله را همگفته‌الد‬      ‫مکر و‬       ‫و‬   ‫ندیسر باشد ‪-‬‬     ‫و‬
5636:      ‫بال فرح شبها امیر ررز غدیس ‪.‬‬                ‫‪ - ۴‬کیوس‌وارنگرد(بگیرد)همی‌بچشم آ لوی‬
8647:  ‫حاء بلغت حجاز تمررهندیست و ففرالیپود نیز نامند ‪« ».‬تحفةٌ حکي‌مومن» درت کر ضریرانطا کی‬
8812:  ‫»‬   ‫تمرهندیست‪.‬‬     ‫‪ 9‬حوهر»‬       ‫‪۴‬‬         ‫طریفلن است» «تحفةً حکیم مومن» ‪ .‬رك ‪ :‬حندقوفی (ح) ‪.‬‬
9907:       ‫الی‌کمتین ناصر خسرو‪ .‬مصحح لگار نده‪ .‬تهرانص‪ - ۱ .»4۰۲‬از‪ :‬خابه(ه‪.‬م‪-( ).‬دیسی(پسوندشیاهت)‪.‬‬
9910:                                                           ‫خ‪#‬ایدیه ‪ -‬رك ‪ :‬خابهدیس ‪.‬‬
13305:            ‫‪ ۳‬رك ‪ :‬خله ‪.‬‬            ‫و آلرا خله بیزگوبند » خابه دیس باشد» «لفت‌فرس ‪. ۰۳۲۰‬‬
16706:                                                      ‫خوانند ‪.‬‬     ‫لعابیسفید‬         ‫عگلوىبندیسببآنکه چون ‪3‬‬
18219:‫و دال أ جد‬    ‫اول‬   ‫بكر‬        ‫در ندیس ‪۰‬‬
18530: ‫مخفف دیس هم حت که شبیه ونظیراست ‪٩‬‏ ‪-‬‬                     ‫دس = بفتح اول وسکون انی» بمعنی‬
20073:         ‫وازآنجا توپ وتفنکه بقلمه اندازند‪. ۷‬‬                      ‫بیونالی طرغلودیس ‪ ۴‬و بعربی صفورالشوکه‬
21664:   ‫‪- ۴‬قن‪:‬بستگانی‪-8 .‬پهلوی‪« 0102080‬تاوادیا ‪۶5۹‬‬                         ‫آمده‌است‪.‬ر‪ :‬مزدیسنا ص ‪۶۹۳.‬‏‬
22024:‫دیس د با نانی مجهول بروزن کیس‪.‬‬                               ‫ادات دبگر که از کاکل تا‬   ‫وخر و بحییواز‬
22030:‫دیسقوریدوس ‏‪ ١‬بکراولوضم‬                                          ‫رمد کشیده کشند ‏ و چنبر دابره ‪ -‬و غربال‬
22043:  ‫فرخاردیی‌وطاقدیس آمده " بنابرین «شبدیز» لفة بمعنی شب نماء وتبدبل سین‌بزاه درکلمه‌اسپربی‬
22072:‫دیفرو جاس * = بکراول وسکون‬                       ‫دیس ناو ‪ ۱‬ب=الون بالف کشیده بر‬
22096:  ‫جمله‌های < و دربخشی از دیستاد » او (مزدك) میگوید» با ‪ ۶‬ودرهمین کتاب میگوید ‪ » ...‬ومانند‬
22101:                       ‫در برهان «دیسناد» براثر غلط در رسم الخط به «دیتاو» تبدبل شده‪ .‬ر ‪:‬‬
22104: ‫آبا « دیس‌اد » دبستان مصحف «دربت دبنان» (یهلوی ‪( ) 4517۵0 _ 0061‬بعلی دار کان‬
22376:     ‫دیو خوانندیسنی دبورامیدابد‪ .‬نوعی ازاسیست‌را که ‪-‬اق وبرگهآن ازامتال بزرکنراست دیوامیت‬
23594:                                       ‫انداز ید ‪.‬٭‬      ‫ولیمهد پدر شدیسیب هوا و وی بسیار ده سبط‬
27062:     ‫‪ - ۴‬خلطی است‬                 ‫‪ ۴‬رك ‪ :‬مزدیستا بخش ‪ 4‬بهر؛ ‪ : ۱‬بیگانگی و دوکانگی ‪.‬‬
32677:       ‫ویزدانیانر آبادبان وسیاسیان ووشیان وانوشکان وآ ذرهوشنگیانو آذربانگویند» «دیستان‌المذاهب‬
32757:           ‫بینداخت ‪.‬‏ «کلستان ‪( . ۰۲۰‬در نظام جدید «سیاء» واحدیست شامل چند «لشکره ) ‪.‬‬
34204: ‫بروزن نقدیس ‪ ۰‬قوس قزحرا گوداد ‪٩‬‏ ؛ وحرف‬              ‫هزار پارا گویند‪ ,‬وآن خزنده‌ایست زرد که در‬
35325:                       ‫حفظ کرد وآن‌همان بادیست که درآستین هریم دمیده شد ومسیح پوجود آمد ‪:‬‬
36761:                                     ‫‪.‬‬   ‫رومی است‬    ‫سقلیس ‪ - ۴‬بر رزن تقدیس » بلغت‬
37729:‫آنرا خابه دیس گوبند چه بتخم مرغ می‌مالد‬                             ‫واییرا یز‬ ‫رجل خواند ‪ -‬ج‬
39844:  ‫‏‪ , th rah -‬یبابرآ ‪ ( -1۳25‬ندبزرل ‪ ,‬ندیسرت ) كر[ ‪] :‬ندسرت كر ‪:‬بینركگ كرو؛‪: ۱۹۹‬‬
40002:               ‫واسمه عندالمجوی سیاه(درچاپ بارس ج‪ ۲‬ص‪ 4۲۱‬پستاء)» رك ‪ :‬مزدیسنا ص‪. ۵۵۲‬‬
40747:                                                   ‫لخستین پیرو مزدیسناست که صد سال‬
```


## [2026-09-05T17:33:55.907Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22010,22070p' BQT_v2_pages.txt; echo \"@@@ leaf:\"; awk 'NR<=22024 && /\\f/{c++} END{print c}' BQT_v2_pages.txt"
}
```


### [2026-09-05T17:33:57.683Z] TOOL RESULT

```
‫واسب واستر وخربرا کیوزبند که از کل تا‬                            ‫و زای قطه دار (‪ » )۱‬رنگك و لون راگوند‬
‫‪-‬لاغ‬
   ‫دمش خط سیاهی کشیده شده باشد ‪٩‬‏ وا‬                             ‫عموماً چنانکه اسب سياه خرو پرویزرا شبدیز‬
‫مایل‬    ‫سبری‬    ‫و‬    ‫و چاروابی که رنگه آن سیاهی‬                  ‫‪ - ۴‬و رنگه سیاه را‬        ‫نیگه‬
                                                                                              ‫بندربعن‬
                                                                                                    ‫شگفت‬
                                                                                                       ‫می‬
                                                 ‫‪5‬‬               ‫کوبند خصوصاً ‪ -۴‬و رنگه خاکتری بیاهی‬
                                                                 ‫اسب و استر‬     ‫صوص‬
                                                                                  ‫مدخکه‬
                                                                                      ‫ان‬            ‫ه‬
                                                                                                    ‫تیز‬
                                                                                                      ‫گلفرا ن‬
                                                                                                            ‫ماب‬
‫دیس د با نانی مجهول بروزن کیس‪.‬‬                               ‫ادات دبگر که از کاکل تا‬   ‫وخر و بحییواز‬
‫همتاومانندوشییهو نظیرباشد‪- ۸‬وبهندی‌بمعنی روز‬                    ‫عنی‬ ‫م‪-‬‬‫ب‪۴‬‬ ‫وشد‬
                                                                           ‫دمش خطی سیاه کشیده شده با‬
‫است که بعربی بوم خوانند‪ -‬وملك وولامت رانیز‬                       ‫حصار وقلعه ‪ 7‬وجاست ‪ - ۴‬ونوعی ازدیگه‬
                                          ‫کوند ‪٩‬‏ ‪.‬‬              ‫ويال باشد ‪۴‬ونوعی ازشیاف است که درچشم‬

‫دیسقوریدوس ‏‪ ١‬بکراولوضم‬                                          ‫رمد کشیده کشند ‏ و چنبر دابره ‪ -‬و غربال‬
‫خامی که واو باشد‬
               ‫قاف وسکون ثالی و الث و‬                                                   ‫و پرویزن را دگیوزیند ‪.‬‬
‫بواو‬   ‫ابجد‬   ‫دال‬   ‫رسینه و‬   ‫بی نقطه بتحتانی‬   ‫رای‬   ‫و‬          ‫دار ندان ‪ = °‬بروزن‌بی‌دندان» سهياية‬
‫دحاکمیمی است از‬                         ‫ا‬‫‪+‬‬                       ‫آهنی باشد که دیگه مین رابربالایآن گذارند‬

                                                                                      ‫(‪ )۱‬چك ‪:‬وزا‪.‬‬

  ‫ازکامة _ ‪ 2502‬باشد‬          ‫آفای‌پورداود نوشته اند‪ :‬شاید دیز»‬           ‫‪۴‬‬           ‫رك ‪ :‬ديرد‬      ‫‪۱‬‬

  ‫‪ :‬تمد یس ‪۰‬‬        ‫دادن که در کلمات‬   ‫وشان‬   ‫مودن‬        ‫اوستابی نمعتی‬       ‫‪682‬‬   ‫بمعنی نما ونشان ‪ ۰‬ازمصدر ‪-‬‬


  ‫فرخاردیی‌وطاقدیس آمده " بنابرین «شبدیز» لفة بمعنی شب نماء وتبدبل سین‌بزاه درکلمه‌اسپربی‬
  ‫= اسپریز دیده ميشود‪ .‬دیزودیزه جکداانه در ادبیات مابمعنی سیاء آمد وبوبژه ازبرای اسب‌سیاه‬
                                                          ‫بکار رفته مانند شبرنگه وشبگون ‪:‬‬
               ‫کرو رده زصرصر در تك وتیز‪.‬‬                           ‫یکی شبگون که امش بودشبدیز‬
                                             ‫آیدز ر‬
                          ‫‪.‬ودی ترديك دزقول ) ‪.‬‬                     ‫رك‪ :‬دز ‪ .‬دژ ؛ آب دیز (=‬           ‫‪۴‬‬
  ‫معنی از باد کلمةٌ « دیگه » («‪.‬م‪ ).‬د قاب اص ‪ ۱۹۲‬ح» ‪.‬قس‪ :‬دیزیی ورك ‪:‬‬                            ‫‪ ۴‬م‪-‬اين‬
  ‫یابه ) |د بگدان ‪ .‬دیگپابه ]‪ ,‬ماز سرانی کنونی‬               ‫س‬    ‫(‬            ‫طبری ‪0‬‬       ‫‪۶‬‬            ‫دىزتدان ‪.‬‬
                                                    ‫ر=‬
                                ‫ان) « راژه نامه ‪. ۷۸۳‬‬ ‫‪ +‬ادان (‬                      ‫‪ 0006211‬از د‪:‬یز ‪9‬‬
  ‫ابا از‬        ‫رن‬
                 ‫ه_‬‫ھ‬                    ‫رك ‪ :‬دوز ‪١‬‏ دز » دژ‪.‬‬          ‫‪۴‬‬                ‫‪ - ۱‬ره ‪ :‬دیز‬
  ‫ربشة اوستابی‪( 56۳20 -‬کء > نظر) ؛ حندی باستان ‪( 6۲0‬رویت » دیده شده )‪( - 49۴ ۰‬فظر‬
                                              ‫ولی ه‬                           ‫دیده شده ) میداند « اسشق ‪roc‬‬
  ‫وتمان آبرا از ره‪ çid ‎‬ساسکرت‪ ) .‬شان دادن‪) ‎‬‬

   ‫(ارائه) دانته «هوبشمان ‪۳۹٥٠‬‏ بر که هر دو‬                      ‫اوستا کل ش(اندادن» ارائه)‪ ,‬استی ‪81511۷3‬‬
   ‫رده گووید ‪ :‬در اوراق مانوی تورفان ‪( 560‬شکل‪ .‬ساختمان)»مفدی ‪680-‬‬                ‫هل‬‫وجه مذ کور را ک‬
  ‫‪ ,8‬ورك ‪ :‬دیز» دی »دسه‌وص‪ :‬له از‬ ‫‪6‬‬ ‫‪6‬‬ ‫‪2‬‬ ‫‪0‬‬ ‫‪-‬‬ ‫‪:‬‬ ‫‪۳‬‬ ‫‪۷‬‬ ‫ه‬ ‫م‬ ‫ل‬ ‫ه‬ ‫ت‬ ‫ر‬ ‫ا‬ ‫ب‬ ‫‪:‬‬ ‫ك‬ ‫ر‬ ‫و‬ ‫‪۹‬‬ ‫ه‬ ‫ک‬ ‫ر‬‫ب‬ ‫ی‬ ‫(ساختن) آمده «‬
     ‫»سلطنت)‬         ‫ل»‬
                     ‫ت‬ ‫اهره‬     ‫‪٩‬‏ مان کریت ‪( 456‬قطه ‪ ,‬تاحیه »جا »س‬
                          ‫اهمب» ب‬                                                                 ‫دىياچة مۇلف ‪.‬‬
            ‫_ ‪ . sedirocsoiD‬طبیب بوالی ترن اول مبلادی ‪.‬‬                                     ‫« وبلیامز ‪٩٩4‬‏ ‪:۲‬‬
 ‫دطروجاش‬                                                                                  ‫‪4‬‬    ‫سل‬


 ‫خرش" د با فا ورای بشیطه‬
                       ‫دیف د‬                      ‫حکمای بونان ‪ .‬گوبند نباتات و رحتنی را مسار‬
@@@ leaf:
370
```


## [2026-09-05T17:34:24.924Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^desk\\|^disc, \\|^disk\\|^discus\\|^discuss\\|^dais\\|^dish\\b\" KLN_1966.txt | head -30"
}
```


### [2026-09-05T17:34:24.974Z] TOOL RESULT

```
10233:dais,  n.,  a  raised  platform  in  a  hall.  —  ME.  deis, deys,  fr.  OF.  deis,  dois,  ‘table;  platform’  (whence F.  dais,  ‘canopy’),  fr.  VL.  discus,  ‘table’,  fr.  L. discus,  ‘quoit,  dish,  disc’.  See  dish,  disk  and cp.  desk.
10234:daisy,  n.  —  ME.  daies  eie,  fr.  OE.  dteges  ege, dzeges  enge,  lit.  ‘day’s  eye’  (see  day  and  eye);  so called  because  it  opens  its  flower  in  the  morning. Daisy,  fem.  PN.  —  Orig.  used  as  a  pet  name  for Margaret,  F.  marguerite  being  identical  in meaning  with  E.  daisy.
11048:desk,  n.  —  ME.  deske,  fr.  ML.  desca,  ‘a  desk, table’,  fr.  L.  discus,  ‘a  quoit,  a  disk;  a  table’. See  dish  and  cp.  dais,  disk.
11670:discus,  n„  a  disk.  —  L.,  fr.  Gk.  Staxo?,  ‘quoit, disk’.  See  disk.
11671:discuss,  tr.  and  intr.  v.  —  L.  discussus,  pp.  of  dis- cutere,  ‘to  shake  violently,  shatter,  dash  to  pie¬ ces,  scatter,  disperse’,  in  Late  L.  ‘to  discuss’, fr.  dis-  and  quatere,  ‘to  shake,  wield,  brandish, strike,  shatter’.  See  quash,  ‘to  annul’,  and  cp. concuss,  concussion,  percuss,  percussion. Derivatives:  discuss-er,  n.,  discuss-ible,  adj.,  dis¬ cussion  (q.v.),  discuss-ive,  adj. discussion,  n.  —  OF.  (=  F.),  fr.  L.  discussionem, acc.  of  discussio,  ‘a  shaking’,  in  Late  L.  ‘dis¬ cussion’,  fr.  discussus,  pp.  of  discutere.  See  prec. word  and  -ion.
11691:dish,  n.  —  ME.  disch,  fr.  OE.  disc,  ‘dish,  plate, bowl’,  rel.  to  ON.  diskr,  ‘dish’,  OS.  disk,  ‘table’, OHG.  tisc,  ‘dish;  table’,  MHG.,  G.  tisch, ‘table’,  fr,  L.  discus,  ‘quoit’,  in  Late  L.  ‘dish’ (so  called  because  of  its  shape),  fr.  Gk.  Stoxo?, ‘quoit,  disk’,  which  is  dissimilated  fr.  ‘Six-oxo? and  prop,  means  ‘that  which  is  thrown’,  from the  stem  of  Sixctv,  ‘to  throw,  cast',  whence  also Stxxuov,  ‘net’.  Cp.  dais,  desk,  disc,  discus  and the  second  element  in  oftish.  Cp.  also  Dictynidae, Dictynna,  dictyo-.
```


## [2026-09-05T17:34:25.751Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"desk, n\\.\\|disc, n\\.\\|discus, n\\.\\|discuss, tr\\|dictate, tr\\|digit, n\\.\\|index, n\\.\\|judge, n\\.\" KLN_1966.txt | head -30"
}
```


### [2026-09-05T17:34:25.814Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:34:34.427Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# map line number -> leaf\nleaf=0\nlineleaf={}\nfor i,l in enumerate(lines,1):\n    lineleaf[i]=leaf\n    leaf+=l.count('\\f')\nfor n in (10233,11048,11670,11671,11691):\n    lf=lineleaf[n]\n    print(n, 'leaf',lf, '=> printed ~', (lf-12)*2, 'to', (lf-12)*2+1)\nEOF"
}
```


## [2026-09-05T17:34:35.069Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^disk,\\|^teach,\\|^token,\\|^toe,\\|^dictate,\\|^digit,\\|^index,\\|^judge,\\|^dictator\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T17:34:36.231Z] TOOL RESULT

```
10233 leaf 219 => printed ~ 414 to 415
11048 leaf 238 => printed ~ 452 to 453
11670 leaf 251 => printed ~ 478 to 479
11671 leaf 251 => printed ~ 478 to 479
11691 leaf 251 => printed ~ 478 to 479
```


### [2026-09-05T17:34:36.280Z] TOOL RESULT

```
19159:index,  n.  —  L.  index,  gen.  indicia ,  ‘a  pointer,  in¬ dicator;  the  forefinger;  sign,  mark,  indication; guide,  witness,  informer’,  rel.  to  indicdre,  ‘to point  out,  show’.  See  indicate.
38337:teach,  tr.  v.  —  ME.  techen,  fr.  OE.  tScan,  ‘to show,  teach’,  rel.  to  OE.  tacen,  tdcn,  ‘sign, token’,  and  to  teon  (for  *tih-an ),  ‘to  accuse’,  of- teon,  ‘to  deny’,  OHG.  zihan,  MHG.  zihen,  G. zeihen ,  ‘to  accuse’,  OHG.  zeigon,  MHG.,  G. zeigen,  ‘to  show’,  Goth,  ga-teihan,  ‘to  announce’, fr.  l.-E.  base  *deik-,  *dik-,  ‘to  show’,  whence also  OI.  disdti,  ‘shows’,  Gk.  Sstxvtivoa,  ‘to  show’, L.  dicere,  ‘to  say’,  dicare,  ‘to  dedicate,  conse¬ crate’.  See  diction  and  cp.  teen,  toe,  token. Derivatives:  teach-able,  adj.,  teach-abil-ity,  n., teach-able-ness,  n.,  teach-er ,  n.,  teach-ing,  adj., teach-ing-ly ,  adv.
39440:token,  n.  —  ME.  taken,  token,  fr.  OE.  tacn,  sign, token’,  rel.  to  OS.  tekan,  ON.  teikn,  ‘sign  (in the  zodiac),  omen,  token’,  Swed.  tecken,  Dan. tegn,  OFris.,  MLG.,  MDu.  teken,  Du.  teken, OHG.  zeihhan,  MHG.,  G.  zeichen,  Goth,  taikn, ‘sign,  token’,  fr.  l.-E.  base  *deik-,  to  show  . See  teach  and  cp.  words  there  referred  to.  Cp. also  tache,  ‘spot  on  the  skin  .
```


## [2026-09-05T17:34:50.892Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (219,238,240,241,251):\n    L=leaves[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', L)\n    print(i, 'nums:',nums, '| first80:', L.strip()[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T17:34:52.970Z] TOOL RESULT

```
219 nums: [] | first80: odel’,  fr. OF.  affrodile,  a  var.  of  asfodile,  fr.  L.  aspho- delus.  See
238 nums: ['434', '435'] | first80: itus,  pp.  of  desinere,  ‘to  cease’.  See  de- sinent. desk,  n.  —  ME.  des
240 nums: ['438', '439'] | first80: also  Goth,  us-priulan,  ‘to  vex’, OE.  f> reotan,  ‘to  weary,  vex,  annoy’.
241 nums: ['440', '441'] | first80: deity. dewan,  n.,  minister  of  finance,  chief  officer  in  In¬ dia.  —  Ara
251 nums: [] | first80: d  countenance.  Cp.  F.  de- contenancer. discourage,  tr.  v.  —  OF.  descora
```


## [2026-09-05T17:35:03.163Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (250,251):\n    L=leaves[i]\n    print('=== leaf',i,'===')\n    print(L[:200].replace('\\n',' '))\n    print('...tail:', L[-300:].replace('\\n',' '))\nimport re\nprint('---- disk entry ----')\ni=txt.find('disk,  n.')\nprint(txt[i-200:i+700])\nEOF"
}
```


### [2026-09-05T17:35:04.754Z] TOOL RESULT

```
=== leaf 250 ===
iculate,  v. Derivative:  disarticulat-ion,  n. disassociate,  tr.  v.  —  Formed  fr.  dis-  and  associ¬ ate,  v.  Cp.  dissociate. Derivative:  disassociat-ion,  n. disaster,  n.,  misfortune,  cal
...tail:  and  L.  computare,  ‘to  count’.  See  count,  v. discount,  tr.  and  intr.  v.  —  OF.  descompter,  des- conterlfi .  decompter),  fr.  i6thcent.  F.  descompte. See  discount,  n. Derivative:  discount-able,  adj. discountenance,  tr.  v.,  to  discourage,  disapprove. —  Formed  fr.  dis-  an
=== leaf 251 ===
d  countenance.  Cp.  F.  de- contenancer. discourage,  tr.  v.  —  OF.  descoragier,  descoura- gier  (F.  decourager),  fr.  des-  (fr.  L.  dis-)  and corage  (F.  courage).  See  dis-  and  courag
...tail: p.  pp.  of  deshabiller,  ‘to  un¬ dress’,  used  as  a  noun,  fr.  des-  (fr.  L.  dis-)  and habiller,  ‘to  dress'.  See  dis-  and  habiliment.  For the  loss  of  the  French  pp.  suff.  -e  in  E.  deshabille cp.  costive  and  words  there  referred  to. disherison,  n.,  the  act  of  dis
---- disk entry ----
```


## [2026-09-05T17:35:17.263Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- BRT daēs ---\" && grep -n \"daēs\\|daes-\\|daēsa\\|dais-\" BRT.txt | head -20"
}
```


### [2026-09-05T17:35:17.307Z] TOOL RESULT

```
--- BRT daēs ---
12498:671  daevayaz-  —  daes-  3  (
12521:•  ').,  g.  daes-  V.  'zeigen'.  Praes.  7  dag- daü-,  3j  (auch  Pass.)  disya-,  30  (Iter.) daisaya-,   j-Aor.  1  däil- \  dsis- :  dti-.  —
12540:Zum  V.  dais-,  —  ai.  deli-  m.  'Gegend';  nip. uidfs  'Gätzenbild',  np.  'des  'ähnlich';  s.  dazu HOKN  GIrPb.  /  b.  35.
```


## [2026-09-05T17:35:18.095Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- CHEUNG dais ---\" && grep -n \"DAIS\\|\\*daiš\\|daiš\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T17:35:18.155Z] TOOL RESULT

```
--- CHEUNG dais ---
```


## [2026-09-05T17:35:24.554Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12490,12550p' BRT.txt"
}
```


### [2026-09-05T17:35:24.594Z] TOOL RESULT

```
Vgl.  JahiiJratarSla-.
•  j.  'daevi-  f.:  s.  unter  ^dtuva-.
•  j.  daevö.;qiit-  Adj.  'die  Vaiva  schlagend' : vaca  arJuxia  vär»%rayms  'ynita  (AP.) yasamaiäe  Vr.  20.  i ;  G.  2.  ö''.
^^»-ü■  Adj.  {S  1S3),  zum  V.  gan-.  —  PQ.:"dÄ talär.  -  ')  Hier  i,  %  363.  i.
•  j.  daevÖ.£idTa-  Adj.  {fem.  'rä-)  'von den  i^oArn  abstammend':  nase  datvT drvxs nate  're  (VSf.)  SrB.j.
Pü. :  äevan  iäxmai.
•  j.  daevö.)ata-  Adj.  (fem.  "«-)  'von den  Daiva  geschlagen':  haea  avaakät tanvai  yai  'tayä  (sUtt  AblS.)
np.  dcDtada  *wBhnsinnig'.  —  Pü ■)  Jp  1,  MCl  haben  'Ijyäl.
671  daevayaz-  —  daes-  3  (
'ttanant  tamt.pirihanqmca'^.^g', — yS xiit- \ fanäni  nasul  *ttm  \''tg,$;  —   nastts ärä  Hqm^ai%wayHH  dahmanqm  adahma-  -        —  -  _»_
namca  'nanam  adaivayasnanqmca  tanu.- p3r3%anani  atanu-pinhanatiua  V.iS.öz*^.
Komp^  —  «.  daiayajaä-  m.  'GöWetopfer'.  —
Pü.:    dev  yasH,    erl.:    aner   'Nichtiruiier'.    —
>)  Vgl.  Sf.  ZDMG.^/.  zS4  ond  die  PüErl.—
ä)  VgL  V.  iS.  63.  —  »  Hds.  'fosnS.  —  4l  Vgl.
N.  //.
•  j.  daeva-yaz-  Adj.  'der  zu  den  Da!va betet,  Z>tfA'iianbetei':  nyancs  'yä^  (NF.) V.J5.4Ö,  Ylj/.  6;  —  mafyaka  'yasS  Yt 14.SM —  Aäu  asti  daivff  Aäu 'yOtS  iHS.)'i V.-.54;  53.  <?-3i.  Sa-
Zum  V.  j-as-.   —   ai,  daiayäj-  Adj.,    mp.  »gl.
öirmiud  yai,  div  yatai. —  Pü.:  dcv  yanti. —
")  Tbem.
V.  79.46;    — 'tat  y.57.  35;  —  armkö  'ts  Y.g.  5;  — tyam  °»«  V./9.43;  1.2,  19,  7.37; — azifis ukhe  Y.  16.  8;  V.  t8. 19;  —  slMs  Ha  Yt 70.50.        [Ytjj.  90:  lies  äaevSJilüm^ Pü.:  drvän  dat.
•  j.''daevö.tbiä-"m.EN.  eines  Gläubigen: 'ibsii  taxmaht  aiwns  Yt  y.  98.
Eig.  'die  Feindschaft  der  D.  bildeod',  d.  L 'TOn  den  D.  befeindet'.  —  Wegen  des  Stamm- ansatiei  und  der  Kaiusbildung  $  3^4-  — >)  SoMf3;  NA.  mit'Fi  daaiaif,  wai  wegen t  weniger  wahrscheinlich.
•  j.  daevö.fra'karäta-  Adj.  (fem.  •/a-) 'von  den  D.  bewirkt,  geschaffen' :  paitistatse ainisteis  'tayä  Yty.  130;  —  nase  dagvl druxi ..  Ue  (VS£)  SrB.j.
Vgl  daevi.iarUa..  —  Pü. :  deväa  /räc  lärrenU.
•  j.  daevö.ira'däta-  Adj.  (fem.  Ha)  'durch die  Dalva  hervorgebracht,  geschaffen': nase  daiuT  druxl . .  nase  *'däite'^  (VSf.) SrB.j.
Pü. !  deiiän  fräl  däl.  —  ')  NA.   'lt.
•  g.  daevo.zuSta-  Adj,  'den  Daeüa%  er- wünscht, Liebling,  Freund  der  D':  yä masya  oHsiä  daniö  vaxsjntt  'tu  "dass  die Menschen,  die  das  Schlechteste  tun,  Lieb- linge der  Dafva%  heissen  sollen"  Y.^2.4.
ai.  äevöjutla-  Adj.  —  Pü.:  */  gämenJ  in  i dä/än  döSU,
•  j.  daevya-  Adj.  'rfoAdsch,  teuflisch': arirSi..vairTm  yim  xrvantim  aiktvanttm yim  °vTm  Aog.  2S.
Ableit.  aus  «rfaS^-.—  Vgl.  ai.  deiyA-  n.  'G«t- lichkeit',  dämya-  Adj.  'göttlich'.—  Pü.:  fehlt, Sü. :  narakagiipkäm  . .  yimta  drvhn.
•  ').,  g.  daes-  V.  'zeigen'.  Praes.  7  dag- daü-,  3j  (auch  Pass.)  disya-,  30  (Iter.) daisaya-,   j-Aor.  1  däil- \  dsis- :  dti-.  —
V.  ig.  10. 1  'it  "'^"V.
d^v  ia:  —       i)  'Jeniandem(Gen.)etwas(Akk.)  zeigen, sehen   lassen':   fravasayö  . .  yä    apqm  .  .
•  j,  *daevö.tät-"  f.  '.öt/ft/aschaft':  xara- ,  srirä  pa'iö  daesayänti  Vty.53;  — ./*»- '^usiraie  .  .  yS  vispqm  'lät^m'^  vavaca  vasayS  .  .  yä  stram  mhnhö  hürS  ..  pähB aytsnyqm  avähmyqm  Yt  y.  90.  XdaisaytnXX.i^.^'};  —  a^qm  ratui . .  aSahe
')  Hds.  daiiS.där'.  vgl.  za. ftcUimatil-  No.  \.\*dalst^!U  pantqm    Vyt  42\  *F.  /4'*;    —
•  j.  daevö.tama-  Adj.  'der  am  ta.i\^QTi\fravasayS ..yhitrvaraHqm..srlräurukmts Dafva  ist,  YAzdaliiä':  dacvanqm  'vum  YX.'' dalsayeinii  YtJ_j.  55;  —  at  tu  mUi  daü J.14';  —  daevü  paitiss  daluS  daei'anqm  (i^s-hatK^^  astm  kyatmä  zaozaomx'^\AS& °tnö  V.  75. 43.  |mich  das  A.  sehen,  nach  dem  ich  rufe'*
ai.  vgL  dc.aiama-  Adj.  —  Pü.:  fehlt  ,  Y.  43. 10  {Zar.  Spricht).         3)  'jemandem
•  j.  daevö.däta-  Adj.  (fem.  HH-')  'von  (Dat)  etwas  zuweisen,  zusprechen,  zu- den /^d^'d  geschaffen': /•in.i/vt  i/^mu  °/^m  sichern':    Msä  (3Sf-AorM.)^   mSi   istoif
dby  Google
673
dae»-  mit  avi
dauStar-
674
(sd.)  xiii'^fvm  Y.  51.  a;  —  6>rtx&am  mSi forasaeitrS  kvB.gvl!  däedöii't'i*  kihrpsm  .  . yam  . .  i^am  (sd.)  "den  geschätzten  Leib'' der  lieben  (Jui^;frau)  hat  mir  FrMv.  zuge- sprochen, welcher  . ."  Y.5J.  17;  —  <^^st (Pass.)*'  he a^Ae  avai  miiäfm{^) ..ya%a .. ^3-Tt  ^-5-44;  —  srTra  p^nsS  disyata yaha  mOvaya  ..Vyi.ß^i'i);  — jimama  tl dalsayama  U  .  .  Vyt_j2(?)  a)  '(Strafe) zuweisen  sva.  festsetzen':  avavantfm  asa- vaynyai  (sd.)  tqm  S^qm  daisayS  V.  5. 14.  3)  'Jemanden  (Dat-)  unterweisen in  — ,  belehren  über  — '  (Akk.):  ahmai  dal- nam  dalsayat  ahurd  Yt.  II.  14.  4)  'kund machen';  iä^a(ßd.)  ayärS ..firasayai dlsS (sSj-AorM.)  \.43-l.  5)  '(Jemandem) durch  —  (Instr.)  darauf  hinfuhren,  dazu verleiten,  dass  er—'  (KeUtivum):  «7a  dalna disyät  . .  yS  %riummaim  ratBm  aiwyän- kam  (sd.)  «Ji^  ahvyästi  V.  18.  9.
mit  ain,  aoi  1)  dnwS.  z  :  pasätSa  at>m yS  aAwö  .  .  aoi  urune  urväsma  (sd.)  dal- sayeni  P.J<¥.  t)  dnwS.  4:  yi' .  .y3^wa ..m^rrffnte  avi  tu  dim  disyatayh  apasca.. ". ,  den  macht  uns  kund,  ihr  Wasser und  .."  Y.Ä3.
mit  frä  dnwS.  3 :  koAmäi  fradasayö dalnam  V.  2.  i ;  —  ahmäi  fradalsaim  dag- nam  V.  2. 2;  —  aet?m  mq%nm  ma  fra- daesaysi^  ainyal  pihre  va  .  .  Yt.  14.  4Ö*'. mit  harn  Med.  'sich  weisen  lassen  in  — (Akk.),  sich  etwas  gesagt  sein  lassen': inja  avat  AandalsayaauÄa  .  .  yai  . .  "zu- rück !  lass  dir  das  gesagt  sein,  . . :  wenn . .'' Yt.ig.^8;  50.
ai,  äiiäti,  dldiiai,  diiyaii,  äeiayaä,  adii^i; woss.  äwdttu«.  —  PQ.  (lu  \.43,  Vi.  //,  V.  2, tS,  F.  14) :  nimütan ;  {in  V.  5,  p,  P.  38,  Y.  S) : nikeaian,  (tu  Y.  S)  erl. :  ftäiä*  ape  kartan  %  s. «och  No.  »f.  —  '>  Hds.  daev'.  —  »)  PB.: doMe,  Sa.:  diHL~il  Pfl.:  daAäl,  Sä.:  d^hi. 4)  NäinL  seinei  Tochler  znr  Ehe.  Pü.i niiebin  HÜeiil,  etl. :  iuia  dtal  ianih  afie  dahil. S.  anch  Dk.  g.  44.  17.  —  5)  Zu  S  S^S- ')  Vgl.  Yt.  4.  9,  wo  fradaxscQiö.
•  j.  daesa-  m.  'Zeichen,  Otnea':  pattiHatSe ayanqmca    :^a/nanqm    ayanqmca
VL/J.  104-
Zum  V.  dais-,  —  ai.  deli-  m.  'Gegend';  nip. uidfs  'Gätzenbild',  np.  'des  'ähnlich';  s.  dazu HOKN  GIrPb.  /  b.  35.
•  '}.  daez-  V.  'häufen,  schichten'  (Erde, Steine);  nur  mit  Praev,  Praes.  i  du-, 30  (Iter.)  da&aya-.  —  PPfP.  'dis'ta-'-\
mit  US  -aufhäufen,  -schichten,  -dämmen,
■mauern':  yS  latitn  utäalum  utdiäa'^ (3SPrM.)  "wer  diesen  Damm  (Mauer)  er- richtet haf  V. /5,  36;  —  affaXiva  dax- W  . .  ysi  bavairiti  (sd)  usdagia  us- dista'^  (NPm.)  V.7.S4.
mit  pairi  'rings-,  rundum  aufdämmen, mauern':  altera  he  alte  masdayasna  ai^ha e^rnH  pairi.dalxan  (sd)  pairi.datzayan  V. 3.  18.
Ar.  "dhailh-  {ygl.  oA. /eiAkss);  ai.  dlgdhi*^: diAänIi;  digdAäk').  —  Pii.:  umschreibt  mit däian  oder  kattan.  —  ')  S  5J  n.  —  »)  Mit inalogischem  gdh,  Sp.  413  n.
j.  daiza-  m.   "Häufen,   Schichten'  von Erde,  Steinen. KompE.  —  Zum  V.  dan-,  —  np,  dcz  "Burg', gr.  «rxoe  'Mauer',   osk.  /eihius  (AP.)   'WafP; ü.  deka-  m.  'Körper'.
j.  daoi^ri-  'Spruch,  Rede'uzw.  i/nji/ischer
Wesen,    nur  mit  aya-  Adj.:   frattrase  .  .
ayqm  °rTm  daomnl  Yt  jp.  57;  —    arfqm
■rfm  daunta  daiva  V,  ig.  45.
```


## [2026-09-05T17:35:25.127Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zeigen'\\|to show'\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T17:35:25.172Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:35:34.832Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN ==\" && grep -n \"ähnlich\" HRN.txt | grep -i \"des\\|dis\" | head -10; echo \"== HRN2 ==\"; grep -n \"tandts\\|tandîs\\|tandis\\|bntdes\\|butdes\\|-des \" HRN.txt | head -10"
}
```


### [2026-09-05T17:35:34.892Z] TOOL RESULT

```
== HRN ==
1982:181. {2)beber * wildes katzenähnliches aber schwanzloses
5310:593. "des, -dis, -des gleichend, ähnlich*.
== HRN2 ==
4917:np. bese, das wie np. -des (598) zu beurteilen ist.
5310:593. "des, -dis, -des gleichend, ähnlich*.
```


## [2026-09-05T17:35:36.166Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG size ==\"; wc -l CHEUNG.txt; grep -n \"daiš\\|dais\\b\\|DAIS\" CHEUNG.txt | head; echo \"== SOD dys ==\"; grep -n \"δys\\|dys-\\|δyš\" SOD.txt | head -5"
}
```


### [2026-09-05T17:35:36.243Z] TOOL RESULT

```
== CHEUNG size ==
58427 CHEUNG.txt
4397:*dais! ‘to show’ 
4406:(Yt 19.48, Yt 19.50), 2р1. YAv. "daesaiiata (Y 8.3); Aor. s-: INJ. 2sg. OAv. dais (Y 43.10), SUBJ. 15р. 
4448:divis-/divixt ‘to show’ (d-v- < *óv- < *B-6, hence: *abi-dais ?) || (+ *fra-) Oss. D. 
4462:téon ‘to proclaim, announce’, see also *dais? 
4467:*dais? ? ‘to throw’ 
4489:*daiz (*dais) ‘to build, form’ 
4529:9 Rather than postulating a separate root *dais ‘to build’ it is better to assign the 
5604:(dais'), with *dixsta- > daxsta-. However, Schlerath 1962: 514 points out that this 
55320:*dais! (s.v.), *Hais, *Hnar, 
55903:*dais’ (s.v.), *harc, *ram 
== SOD dys ==
13981:984  'ndys-1  C  Oo-7>* 
13988:985  Jndys-:  C  j.bjUj 
30923:dys- 
32461:Ses   (dysd'r-,  dys-1)  =»5ystk,  Syst- 
32467:3786  dys-1   C  **  Sys-
```


## [2026-09-05T17:35:38.634Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5305,5325p' HRN.txt; echo \"=== leaf/page ===\"; awk 'NR<=5310 && /\\f/{c++} END{print \"leaf\",c,\"printed\",c-21}' HRN.txt"
}
```


## [2026-09-05T17:35:39.343Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4390,4420p' CHEUNG.txt; echo \"-----\"; sed -n '4460,4500p' CHEUNG.txt"
}
```


### [2026-09-05T17:35:40.441Z] TOOL RESULT

```
592. dlden 'sehen, dld 'Anblick; sehend', didär,
ap. i^dai-, didiy sehen'; aw. l/'rföi-, a]di^aifi:
phlv. dUan; ai. V^dhäi-, didhye.
kurd. dUin *sehen' ; af/. Udal ; bei. dU, diMr (LW.),
dtdö:^ ^Augapfel'; wa/. didig-am.
593. "des, -dis, -des gleichend, ähnlich*.
aw. dareS' 'Blick* (yt. 19, 94); ai. dfc- *das Sehen;
sehend*, -dfga- '-Aussehen; -sehend*.
Der r- Vokal ist hier durch e vertreten, wie in heSe
(No. 256). Aw. daesa- (yt. 13, 104), das Darmeste-
ter als *Traum' nimmt, ist zu unsicher, um ver-
glichen werden zu können.
594. deg *Topf*, vergl. dez, deze,
phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^
tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*.
LW. kurd. dizik; af/. deg^ decka; bei. deg, dez, dPd,
Oegci (59); wa/. dlg^ sar. deg.
Zu ai. \/'deh', degdhi 'bestreichen, kitten', got. deignn
'kneten, aus Thon formen*.
595. dlger, dediger (Vis und Rämin, S. 29 V. 5 v. u.)^)
anderer ; sidlger^ süHg ein Drittel* (AM. 110 Zeile 2 v. u.).
=== leaf/page ===
leaf 146 printed 125
```


### [2026-09-05T17:35:40.500Z] TOOL RESULT

```
exact Greek (Pindar) correspondence дубо, whence the formation may be already 
of IE date: *di-n-eH;-. 

*REFERENCES: Horn 1893: 132; Hübschmann 1895: 65; MacKenzie IV: 529; EVS: 55a; Nyberg II: 61; 
DKS: 208a; Narten 1987: 149 ff.; Werba 1997: 295; SVK III: 29; ESIJa II: 288 ff. 


*dais! ‘to show’ 

*AVESTAN: daés- ‘to show’ || (+ *fra-) ‘to show’ || (+ *ham-) ‘to be told, be shown, 
(?) contemplate’ — Liste: 30 

Pass.: pres. SUBJ. 3sg. YAv. disiiat; Caus.: pres. IND. 3pl. YAv. daesaiieinti (Yt 13.53, Yt 13.55), INJ. 
lsg. YAv. fradaesaem (V 2.2), 2sg. Y Av. daesaiio (V 5.14), 35р. Y Av. daösaiiat (Yt 11.14), 3pl. YAv. 
daesaiion (Yt 13.57), SUBJ. 159. YAv. daösaiieni (P 37), 35р. YAv. daesaiiat (Vyt 32), 1р1. ҮАУ. 
ааёѕайата (Vyt 32), OPT. 25р. Y Av. fradaesaiiois (Yt 14.46), IMPV. med. 2sg. YAv. handaésaiian‘ha 
(Yt 19.48, Yt 19.50), 2р1. YAv. "daesaiiata (Y 8.3); Aor. s-: INJ. 2sg. OAv. dais (Y 43.10), SUBJ. 15р. 
OAv. doisa (Y 51.2), IMPV. 2sg. OAv. doisi (Y 33.13); Intens.: pres. INJ. Zeg OAv. daedoist (Y 51.17) 
*MIDDLE PERSIAN: (+ *uz- BMP ’wzdys /uzdés/ ‘idol’, MMP (pl) ’wzdys’n 
‘images, icons; idols’ (LW) || (+ *ham-) MMP hndys-, ВМР hndys- /handés-/ ‘to 
think, contemplate’ > DMMPP: 77a, 180b 

(+ *ham-) Pres.: IND. 3sg. MMP "hyndysyd, ВМР hndysyt /handesed/; Partic.: perf. pass. BMP hndysyt 
/handésid/; Inf.: BMP hndyšytn /handesidan/ 

*PARTHIAN: (+ *apa- or ? *abi-) *bdys- ‘to show’, IPth. ’wpdys- ‘to issue (order), 
order, command’ || (+ *a-) ’dysg ‘sign’ || (+ *uz-) ’wzdys’n ‘images, icons; idols’ || 
(+ *ham-) ’ndys- ‘to think, contemplate, commemorate’ = Ghilain: 90, 61 | 
DMMPP: 152a, 77a 

Pres.: IND. 3sg. dysyd || (+ *ара- or ? *abi-) Pres.: IND. 3sg.’bdysyd, 1р1. IPth. ’wpdysywm, 3pl. MMP 
-----


téon ‘to proclaim, announce’, see also *dais? 
*REFERENCES: Abaev, Slovar’ I: 363, 198 f.; Abaev, Slovar’ II: 361; EVS: 30a; DKS: 160a; Werba 1997: 
194 f.; Steblin-Kamenskij 1999: 147; Cheung 2002: 165; ESIJa II: 301 ff. 


*dais? ? ‘to throw’ 

*KHOTANESE: LKh. dis- ‘to throw’ || (+ *uz-) uysdis- ‘to cast? © SGS: 46 

9 Clear evidence for this root is confined to a single language. For Khot. diss- a new 
etymology, different from Bailey's (apud SGS: l.c.), was suggested by Tichy 1979: 
l.c. She compared the Khot. form to Gr. &ö1Kov ‘I threw’, yielding an IE root *deik- 
‘to throw’, homonymous with IE *deik- ‘to show, point out’. The equation is 
semantically difficult to prove though, not in the least, as this putative root *deik- ‘to 
throw’ leaves so little or no unambigous traces in (Dlr. / IE. Perhaps, this may be 
inferred from the semantic range exhibited by Lat. dicere ‘to say’, Goth. gateihan ‘to 
announce, proclaim’, and especially Gr. ёікт ‘law, custom, justice’, Lat. indicare, 
OE téon, tion ‘to accuse’ (Ernout — Meillet: 255). These rather judicial meanings 
might be specialisations of ‘to throw’, cf. Engl. to throw in, out of court. 

«PIE? > LIV: 109 | Pok.: — 


*REFERENCES: Henning 1935: 121; WIM I: 71; Tichy 1979: 217 ff.; DKS: 159b f., 39a; SVK I: 56; WIM 
IV1: 81; WIM III: 113; ESIJa П: 306 


*daiz (*dais) ‘to build, form’ 
*AVESTAN: (+ *uz-) YAv. uzdaéz- (uzdis-) ‘to heap (up)’ || (+ *pari-) YAv. 
pairi.daéz- ‘to build, fence (around)’ = Liste: 30 f. 


*daj 53 


Pres. athem.: INJ. med. 3sg. YAv. uzdista (V 15.36); Caus.: pres. SUBJ. 3р1. YAv. pairi.daezaiian (V 
3.18, V 5.49); Partic.: perf. pass. YAv. uzdista- (V 7.54)
```


## [2026-09-05T17:36:08.012Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd1 deik ==\"; grep -n \"deik\\|dei\\^k\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -15"
}
```


### [2026-09-05T17:36:08.060Z] TOOL RESULT

```
== WLD Bd1 deik ==
6548:*t (betont zur Yerstarkung eines deiktischen \Yortes, unbetont hinter einem 
6553:206, Thurneysen KZ. 48, 52); air. ( h)7 deiktische Partikel und Stiitzpartikel 
12058:erst scheint das jener-deiktische poln. 6iv und das ich-deiktische serb. ovaj. 
28491:ich-deiktisch, s. Brugmann Dem. 38 f., 51 f., 143f. m. Lit., Grdr. II 2 2, 
28515:etru „altero“; die ich-deiktische Bed. ware zur Bed. eines bloBen Artikels 
32186:wohl idg. *q?cg- neben *q'ick- (vgl *deik- : *deig- ,.zeigen"); fiir einen Ansatz 
48516:de-, do--Demonstrativstamm, z. T. ich-deiktisch; Grundlage verscliiedener 
48519:Gr. -de in o-de, tj-S e, ro-de „der hier" (ich-deiktisch), evda-d e, tr&h'-de, 
48912:deik- 
48927:deik- „zeigen", woraus lat. und germ. z. T. „mit Worten auf etwas hin- 
48941:dicare „feierlich verkiinden, zusprechen, weihen“, osk. deikum „dicere“, 
48981:*deik- und *deig- scheinen aus *dei- „hell glanzen" (auch z. T. „blicken, 
48986:decet als *diek-) mit *deik- unter **deiek- zusammenzuschweiBen. 
49438:und Wz. *deik- „zeigen", s. Yf. LEWb. 2 s. v.); 
50907:neben *deik- „zeigen“ stehendes *dek- zuriickfiihren ;?).
```


## [2026-09-05T17:36:08.812Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"^deik\\|^dik-\\|^deiko\\|^dikā\" IEC.txt | head -15; echo \"== SYN 15.51 show ==\"; grep -n \"15\\.5[0-9] \" SYN.txt | head -20"
}
```


### [2026-09-05T17:36:08.875Z] TOOL RESULT

```
== IEC ==
2108:deik- (theme of next entry). Cf. also dik- *show, tell ; Oss. cf. äv-dīsän ‘witness’; Hitt. (Luvian?) tekusanumi (vb. of uncertain mng.); Gk. deigma ‘proof; MHG zich “proof, distinction, fame’
2109:deikó (deiKnu-, diK-) ‘show, tell’. Cf. deiKs-, diK-. WP I, 776 Skt. cf. di$àmi; Oss. cf. dis, des 'marvel', áv-disín, -desun ‘show’; Hitt. cf. tekkusami, tekkusnumi ‘show’ (fr. *deiKs-); Gk. deíknu- mi; Lat. dico; Osc. inf. deíkum; Olr. im- décim "look round’; Go. ga-teihan ‘announce’; OHG zhan; MHG zihen “report; accuse’; OE t&on, tion ‘show, accuse’; ON tjá “show, tell
2275:dik- (root-theme of deiK-, doiK-, q.v.) Oss. cf. áv-disan; (ambig.) MHG zich (“proof; fame'; Gk. cf. deigma, id.)
9841:dik- (1), see leik- (1))
== SYN 15.51 show ==
25854:15.51 SEB
25855:15.52 Loox (vb.), Loox at
25856:15.53 SteuT (subj.)
25857:15.54 Sten? (obj.), Loox (obj.), APPEAR- ANCE
25859:15.56 Save
25865:15.57 Bricut
26319:15.51 15.52 SEE LOOK (vb.), LOOK AT
26344:15.54 SIGHT (obj.), LOOK (obj.),
26445:e gk. ven ers P rm) further connections dub. Walde- | notice’ but mostly, with transfer to ae 9 mental perception, ‘think’, Walde-P. P, i di- ‘look at, observe’ (Barth. | 1.831 f. 15.55 SHOW (vb.)
26475:15.56 SHINE
26519:15.57 BRIGHT
35364:7, Skt. derivs. of bandh- ‘bind, cap- ture’ (9.16), pple. baddha- ‘captured’, as baddhaka- (AV), bandhana-stha-, also (with d, as if Iran.) bandin-, bandikrta-. So Av., OPers. basta- (in form= Skt. baddha-) is prob. ‘prisoner’ rather than lit, ‘bound’. So OPers. basta in Bh. 2, 13, 14 “I cut off his ears, nose, and tongue, and put out his eyes; he was held prisoner in my court”. Av. bastd- Yt. 15.52 is translated ‘prissonier’ by Darmesteter.
```


## [2026-09-05T17:36:13.740Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26445,26480p' SYN.txt"
}
```


### [2026-09-05T17:36:13.785Z] TOOL RESULT

```
e gk. ven ers P rm) further connections dub. Walde- | notice’ but mostly, with transfer to ae 9 mental perception, ‘think’, Walde-P. P, i di- ‘look at, observe’ (Barth. | 1.831 f. 15.55 SHOW (vb.)
5 tv Goth. (at)augjan Lith. (pa)rodyti ae ae ON visa, syna Lett. adit Ne monstrare, ostendere Dan. vise ChSl. pokazati, (j)aviti fe “ mostrare Sw. visa SCr. pokazati Th montrer OE éawan, etéowan Boh. ukazati a, mostrar ME _ shew Pol.  okaza¢, pokazaé ian, ardta NE show Russ. pokazat’, ukazat’ Tr. taisfenim Du. —_toonen Skt.  dig-, dargaya- Nir.  taisbeanaim OHG zeigin, ougen Av. dis- W.  dangos MHG zeigen, zougen, zounen Br. diskouez NHG zeigen
‘Show’ is virtually ‘cause to be seen’, and, in fact, the most common relation- ship of the terms is with words for ‘see, look, eye, appear, shine’. A few are connected with words for ‘wise’ or ‘know’, hence orig. ‘cause one to know’. In one case the development is ‘stretch’ > ‘spread out’ > ‘display, show’. In the one inherited group (below, 1), if one takes into account all the derivs. (e.g. Skt. dig- ‘direction, cardinal point, region’, Lat. digitus ‘finger’, etc.), it seems likely that the primary notion eS ‘point (as with the finger), point out’,
1. TE deik-. Walde-P. 1.776. hout-M. 265 ff. Walde-H. 1.348 f.
Here as ‘show’. Grk. delxvigxr, NG a Belxven; OHG zeigon, MHG, NHG se Skt. dig-, Av. dis- ; ef. in second- in ae Lat. dicere ‘say’ (earlier sense Goth se pointer’, itdex ‘judge’, etc.),
* ga-lethan ‘announce’, OE tion,
2 than ‘accuse’. tee at ‘bring to light, cause to ‘shine’ ‘3 Ow’, mid. ‘appear’ : Skt. bha-
Bete (15.56). Walde-P. 2.123 f.
* Monstradre (> It. mostrare, Fr.
Er-
montrer, Sp. mostrar), fr. monstrum ‘por- tent, monster’, but through an earlier unrecorded sense like ‘memorable ob- ject’, fr. the root of monére ‘remind, ad- vise’, memint ‘remember’, Skt. man- ‘think’, etc. Ernout-M. 629. REW 5665.
Lat. ostendere, fr. *obs-tendere, cpd. of tendere ‘stretch, spread out’ (9.32).
Rum. ardia, etym. dub. REW 671. Tiktin 91. Puscariu 108.
4, Ir. taisfenim (cf. asfenim ‘testify’), NIr. taisbeanaim, cpd. of fen- : fiad- ‘announce’, finn- ‘know’, etc. Pedersen 2.517.
W. dangos, dan- as in dan-fon beside an-fon ‘send’ (Pedersen 2.302), but sec- ond part? Morris Jones 269 (very dub.).
Br. diskowez, fr. dis- and MBr. goez in a-goez ‘publicly’ : Grk. efdos ‘appear- ance’, etc. Henry 101. Pedersen 1.58.
5. Goth. augjan, at-augjan, OK éawan, et-ecowan, OHG ougen, OHG, MHG z-ougen, also MLG t-énen, Du. toonen, MHG zounen, all : Goth. augé ‘eye’, etc. Walde-P. 1.171. Feist 64. Franck-v. W. 702.
ON visa, Dan. vise, Sw. visa (OB wisian ‘show the way, guide, direct,’
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1046 SELECTED INDO-EUROPEAN SYNONYMS
OHG wisan, MHG wisen, NHG weisen, Du. wijzen ‘show the way, direct, point’, etc.), fr. adj. ON vtss, OE, OHG wis ‘wise’ (17.21), hence orig. ‘make one wise, knowing’ (put one wise in US. slang). JFalk-Torp 1387.
ON syna (but most common in refl. for ‘show itself, appear, seem’), fr. sijnn ‘visible’, syn ‘sight, appearance’ : Goth. siuns ‘sight’, etc., all derivs. of vb. for ‘see’, Goth. saihvan, etc. (15.51). Falk- Torp 1227.
ME shew, NE show, fr. OF scéawian ‘look at’ (15.52), with shift to caus. sense. NED s.v. show, vb.
6. Lith. (pa)rodyti, Lett. radit, perh. : ChSI. raditi ‘care, be anxious’, Goth.
garédan ‘be mindful of’, radjan ‘speak’ etc. (18.21). Mihl.-Endz, 3.495. Traut’ mann 235.
7. ChSl. kazati, mostly pokazati, ete this or other epds. of kazati general Slavic : Skt. kdg- ‘appear, shine’, Ay kas- ‘look at, see’ (Barth. 459), with variant finals (§, &) of root. Walde-P 1.511. Berneker 497, |
ChSl. aviti, javiti (freq. in Gospels etc.) beside adv. avé, javé ‘openly’ : Skt, avis, Av. avis ‘openly’, Grk. aicPavoua ‘perceive’, Lat. audire ‘hear’, etc. Walde- P. 1.17. Berneker 34.
8. Skt. dig-, Av. dis-, above, 1.
Skt. dargaya-, caus. of dr¢- ‘see’ (15.51).
15.56 SHINE
Grk. ddpurw, daclyw, orlhBw Goth. skeinan, liuhtjan, Lith.  Sviesti, Zibéti, NG Napa, yuarlfw glitmunjan spindeli Lat. licére, nitére, splen- ON skina, lisa, glita Lett.  spidét, spist
dére, candére Dan. _ skinne, lyse ChSl.  svétiti, bl¢Stati, sijati, It. rilucere, (ri)splen- Sw. skina, lysa, glinsa liStalt se
dere, brillare OE scinan, lihtan, lixan SCr. _svijetliti(se), blistatt, Fr. briller, luire ME _ schine, lihte sjati Sp. lucir, brillar NE shine Boh. _ svttzti, blyskati Rum. © strdluci, luct Du. schijnen, glansen Pol. $wiecié, blyszczed Ir. as-toidi (3 sg.) taitnim OHG - scinan, liuhten, glizan Russ.  svelit'sja, blistat’, Nir. _ soillsighim MHG sschinen, liuhten, gli- sjat’ W. disgleirio, llewyrchu zen Skt. ruc-, bhd-, dyut-, Br. lugernt, skedit NHG - schetnen, leuchten, bhraj-, cuc-
glanzen Ay. rué-, braz-, ba-
The majority of the words listed un- der ‘shine’ are used primarily of lumi- nous bodies (the sun shines, etc.), and then also of things with surfaces which ‘shine, gleam, glisten’ with reflected light. But some are used only or mainly with either the former or the latter ap- plication. The number of words that may be used for ‘shine, gleam, glisten’, etc. is appallingly large, and only those that seem the most important are con- sidered.
```


## [2026-09-05T17:36:14.847Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n \"^uzdēs\\|uzdes\\|^handēs\\|handes\\|^dēs\\b\" PHD.txt PHD_mackenzie.txt | head -10; echo \"== NYB ==\"; grep -n \"uzdes\\|handes\\|^des \" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T17:36:14.933Z] TOOL RESULT

```
== PHD ==
PHD_mackenzie.txt:5088:uzdes ['we-, 'wzdys I M 'wzdys] idol.
PHD_mackenzie.txt:6259:  dastan, handesidan, hangardan,             corn Jorda.
PHD_mackenzie.txt:6832:idol but, uzdes.                         inactive agar, armest.
PHD_mackenzie.txt:6833:idolater uzdesparist.                    inactivity agiirih.
PHD_mackenzie.txt:6834:idolatry dew-esnih / -ezagih, uzdes-     incantation afson, nerang.
PHD_mackenzie.txt:6836:idol-temple uzdes-zar.                   incline grayidan.
PHD_mackenzie.txt:7403:                                               reflect handesidan.
PHD_mackenzie.txt:7404:question fralin, pursisn.                      reflection handesisn, uskarisn(ih).
PHD_mackenzie.txt:7750:tamarisk gaz.                             think handesidan, menidan, uskar-
PHD_mackenzie.txt:7763:teaching afrah, casisn, hammozisn.        thought handesisn, menisn; v. con-
== NYB ==
1270:des [dys] shape, form, v. zäyak-des. — MPrs dys; NP -dčs, e. g. mäh-des ‘moon- like’; v. also uzdés. From daés-, v. distan.
2561:mihrān-druž [mtr'ndlwc'] breaking one’s promise, one’s word; apostate 71% | uzdes-paristar; v. also mihr-druž. — Cf mihrän kartan to form an alliance KnS VI, 2. — Paz. mihiran-dru£.
```


## [2026-09-05T17:36:23.807Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1270 && /\\f/{c++} END{print \"NYB leaf\",c,\"printed\",c-8}' NYB_vol2_glossary.txt; grep -n \"^des\\b\\|^desag\\|^dēsag\\|desag \" PHD_mackenzie.txt | head -5; awk 'NR<=5088 && /\\f/{c++} END{print \"PHD leaf\",c,\"printed\",c-21}' PHD_mackenzie.txt"
}
```


## [2026-09-05T17:36:24.631Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT ==\"; grep -n \"^TEACH\\|^TOKEN\\|^TOE\\|^DESK\\|^DISC\\|^DISH\\|^DISCUSS\\|^DIGIT\\|^INDEX\\|^JUDGE\\|^DICTATE\" SKT.txt | head -20"
}
```


### [2026-09-05T17:36:25.533Z] TOOL RESULT

```
NYB leaf 72 printed 64
1977:des(ag) [dys(k l ) I M dys] form, appearance.
2727:ham-desag [hmdysk ] of the same form, homomorphous.
PHD leaf 102 printed 81
```


### [2026-09-05T17:36:25.577Z] TOOL RESULT

```
== SKT ==
```


## [2026-09-05T17:36:29.473Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1977 && /\\f/{c++} END{print \"PHD des leaf\",c,\"printed\",c-21}' PHD_mackenzie.txt; echo \"== SKT grep ==\"; grep -n \"Desk\\|DESK, \" SKT.txt | head -5; grep -n -i \"disk\\b\" SKT.txt | head -5"
}
```


## [2026-09-05T17:36:30.950Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LAT digitus ==\"; grep -n \"^digitus\\|^dico\\|^index\\|^iudex\\|^iūdex\" LAT.txt | head -10; echo \"== LEW ==\"; grep -n \"^digitus\\|^dico\\|^index\\|^iudex\" LEW_1910.txt | head -10"
}
```


### [2026-09-05T17:36:31.277Z] TOOL RESULT

```
PHD des leaf 43 printed 22
== SKT grep ==
5169:Disk ;  see  Diso.
```


### [2026-09-05T17:36:31.333Z] TOOL RESULT

```
== LAT digitus ==
2282:iudex, cf. s. dico,Remex a eu 4 son tour un ddnominatif remigo, un abstrait
16540:dico, -as, -aui, dicatum, dicSre: foraea alternantes de la racine
16561:iudex "celui qui aontre le droit, juge" d'oh iudicium, iudicare, M.L.
16565:dico, -is, dixl, dictum, dicere (deico deixi eat encore attestt
16594:dico, addico. M.L.153.
16623:dico,-Ss (fornea anciennes en -ss- du type dicassit): pr 4 sent en
16711:dico, avec un correspondant osq. delkum, deicum "dicere", deicans "di¬
16858:digitus
16887:digitus, -i a. (gdn.pl .digitum Varr. ap. Charis. I 136,35; on trouve
16897:digitus index dans Hor., Sera.3,8,16, oi. il y a peut-^tre trace d'une
== LEW ==
```


## [2026-09-05T17:36:33.821Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16565,16580p;16700,16720p' LAT.txt; echo \"----- digitus -----\"; sed -n '16887,16920p' LAT.txt"
}
```


### [2026-09-05T17:36:33.886Z] TOOL RESULT

```
dico, -is, dixl, dictum, dicere (deico deixi eat encore attestt
dans lea inacriptiona de 1'epoque rtpublicaine; lea foraea en i n'y
apparaissent paa avant la Sententia Minuciorua [117 av. J.-C.], qui a
dixserunt ; certains nsa. ont ausai des graphiea avec ei, cf. Thes.
V 967,a7sqq. Le parfait a un i, c.-k-d. le degrt e de la racine, le
pcp. dictus un i, c.-k-d. le degre ztro de la racine, coaae 1'atteste
Aulu-Gelle, 9, 6 , confirat par 1 'ital. detto) : dire. Uaitt de tout teaps.
Panroaan, M.L.«6s8. Le verbe qui signifie "aontrer", dans lea autres
langues, a'est sptcialist en latin, coaae en osco-oabrien, dans le
sena de "aontrer, faire connaitre par la parole, dire". Le aena de
"designer" est encore sensible dans une phrase coaae: sequar, ut insti¬
tui, diuinum illum uirum quem saepius fortasse laudo quam riecesse est.dix
- 308 -
- Platone* videlicet dicis, Cic., Leg.3,1. Conne orare, dico a un ca-
ractfere aolennel et technique: c'est un terne de la langue de la religion
et du droit: ius dicere (cf.iudex et osq. meddiss) "exposer le droit",
d'autre part Varr., L.L.5,83, - quod a consule dicebatur cui dicto omnes
audientes essent, explication qu^on retrouve dans Cie* De rep. 1,40,63,
dictator ab eo appellatur quia dicitur. Mais, dans 1 'emploi, dictator
et ses derivas dictatura, dictatorius, etc., sont sans rapport avec
dictare. Iis forment un gronpe de sens independant. Cf.Mommsen, Bdb.
d.romisch. A Itert., tome II 1,136. Iri. dictatoir.
A en juger par le grec, oh le pr^sent Seixvujil. est une format ion
relat.ivement r 4 cente, et par 1 1 indo-iranien, oh l'on a skr. dicati "il
aontre" (et 1'intensif ved. dedi$te ), av. daesaye it i (it 6 r .-caus.) "il
roontre", il n'y avait pas, pour cette racine d'ancien pr^sent th 4 ma-
tique a vocalisme radical en e. La forne italique at-test 4 e par lat.
dico, avec un correspondant osq. delkum, deicum "dicere", deicans "di¬
cant", ombr. teitu^, deitu "dicito",n'a de correspondant qu'en germanique:
got .ga-teihan "aTOXYYeoXou", v.angl . teon "accuser", v.h.a.athcm (meme
sens); -mais un present germanique de ce type peut toujours etre secon-
daire. Le v.h.a .zeigon "montrer" a un autre vocalisme radical que
lat. -dicare. - Le perfectum dlxZ est un ancien aoriste en -S-, compa-
rable a gr. eSeu^a, qui doit etre ancien, et au moyen skr.adiksi '^'ai
montr^", cf. gath.ddt£ "tu as montr 4 ".
La forme nominale athematique conservee dans lat. dicis causa, et
dont dicio doit etre d^riv^, se retrouve, avec un autre sens, dans
----- digitus -----
digitus, -i a. (gdn.pl .digitum Varr. ap. Charis. I 136,35; on trouve
k basse epoque dicita fda. et dicita n.pl., cf. Thes. V H33,70sqq.;
ce dernier a subsiste dans les 1 .roaanes, a cote de digitus , cf. M.L.
3638; une forae dicitus, blande par l'app.Probi, GLK IV 198,10, se
trouve dans des inscriptions vulgaires, k cotd d'ailieurs de pures
fautes d'orthographe'conae ticidosy la forae contracte dictus, Varr.,
Men.408 ap.Non.117,30 et Catuli.66,73, est peu sure): doigt (de la
aain et du pied, de 1'hoaae et des aniaaux); aesure de longueur dgale
k la largeur d'un doigt. Digitus est le terae gdndral; chaque doigt
a un noa particulier: pollex, index (ou salutaris, dSmdnstrdtluus ;
digitus index dans Hor., Sera.3,8,16, oi. il y a peut-^tre trace d'une
parentd possible entre digitus et dico), famSsus (dit aussi medius,
summus, impudicus, infamis, etc.), quartus ( anularis, honestus, medi¬
cus),minimus ( auricularis, ultimus), cf. Thes. V ii37,i6sqq. Figure
dans de noabreuses expressions figurdes et proverbiales, cf. Thes.
Y ii36,63sqq.; H3i,iosqq., en particulier dans 1 'expression biblique
digitus dei. Se dit dgaleaent des branches secondaires des arbres
(cf. palma, palmes). Dana le pseudo-Apulde, Herb.87, et dans les gloses,
digitus (-turnj. Veneris ddsigne une piante aussi noaade caput (cerebrum)
canis. - Ancien, usuel; panroaan, M.L.3638. Iri.doit?
Ddrivds et coaposds*. digito, -Ure : 6awru\o8et.xx(o (Gloss.); digitalis :
de la largeur du doigt; digitale, digitabulum-, doigtier, gant (dd),
cf. gr. 6 axTi)Xi} 0 pa "gant"; panroaan, M.L.3637, digit&tus : anni de
doigts, fissipbde (Plin.); digitulus: petit doigt; digitellum (- tillum ;
digitellus a.): grande joubarbe; sesquidigitus: un doigt et deai
(cf. sesquipes) ; SSdigitus surnoa roaain, "qui a six doigts"; inter-
digitia,- 5 rum: espace entre deux doigts.dignus
314
Aucun rapprochenent net. Conne il n'y a pas de non indo-enropeen
connnn dn "doigt", digitus doit etre nne forne popnlaire sur laqnelle
il n'est possible de faire que des hypothbses vagues. Le groupe gema-
nique de v.h.a .zSha "doigt de pied" est diffdrent de tontes nanibres.
V. dico.
dignus: v. decet. •
```


## [2026-09-05T17:36:42.121Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T17:36:42.128Z] TOOL RESULT

```


```


## [2026-09-05T17:36:46.714Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dey%E1%B8%B1-",
 "prompt": "Give the reconstructed root, its gloss, and the full list of descendants/derived terms (especially Indo-Iranian, Avestan, Latin, Greek, Germanic). Quote the root gloss exactly and note any references (Pokorny page)."
}
```


## [2026-09-05T17:36:47.532Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/disk",
 "prompt": "Quote the full etymology of disk/disc, including the Greek diskos and dikein, and any PIE root given. Also state what related words are listed (desk, dais, dish)."
}
```


### [2026-09-05T17:36:53.191Z] TOOL RESULT

```
# Proto-Indo-European Root *deyḱ-

**Reconstructed Root:** *deyḱ- (imperfective)

**Gloss:** "to point out, to show"

**Original Meaning Context:** According to the Encyclopedia of Indo-European Culture, the term originally meant "something that is fixed; norm, rule," with the notion of speaking emerging from oral recounts of social customs and laws.

## Key Derived Terms & Descendants:

**Indo-Iranian:**
- Sanskrit: दिश् (diś), दिशति (diśáti), दिशा (díśā - "direction"), देश (deśá)

**Greek:**
- Ancient Greek: δείκνῡμι (deíknūmi), δεῖγμα (deîgma), δίκη (díkē)

**Latin:**
- index, iūdex, vindex, dictus, digitus

**Germanic:**
- Reconstructed forms including *taikjanąn, *taikną, *taihwǭ (toe)

**References:** Pokorny's *Indogermanisches etymologisches Wörterbuch* (pages 188-189); Ringe (2006); Mallory & Adams, *Encyclopedia of Indo-European Culture* (page 159)
```


### [2026-09-05T17:36:55.290Z] TOOL RESULT

```
The server returned HTTP 504 Gateway Timeout.
Retry-After: 120

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T17:37:01.561Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CF%83%CE%BA%CE%BF%CF%82",
 "prompt": "Quote the Ancient Greek etymology of δίσκος: is it derived from δικεῖν \"to throw\"? What does it say about the reliability of that etymology (Beekes, Pre-Greek)? Also list descendants (Latin discus, English disk/dish/desk/dais)."
}
```


## [2026-09-05T17:37:03.405Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%B3",
 "prompt": "Quote the Persian entry دیس: meaning(s) and etymology (Middle Persian dēs, Proto-Iranian, Avestan daēsa-, Proto-Indo-European root). Also any note about the suffix -dis in تندیس/طاقدیس."
}
```


### [2026-09-05T17:37:08.221Z] TOOL RESULT

```
# Etymology of δίσκος

**Traditional Derivation (Unreliable):**

The conventional theory proposes: "the traditional derivation from *δίκ-σκος (*dík-skos), from δικεῖν (dikeîn, 'to cast')" However, this explanation is problematic.

**Why It Fails:**

Furnée identified a critical flaw: "the suffix '-σκο-' is rare in nominal derivation." This makes the standard etymology "hardly possible."

**Modern Theory (Pre-Greek Origin):**

The scholar "suggested to start from *δισκ- (*disk-), a variant...of δικεῖν (dikeîn), which has Pre-Greek origin." This acknowledges the word likely derives from a substrate language predating Greek.

**Key Descendants:**

- **Latin:** discus (which spawned further Romance derivatives)
- **English:** disk, disc, dish, desk, dais (all descended from the Latin form)
- **Modern Greek:** δίσκος (dískos)
- **Other languages:** Romanian disc, Russian диск (disk)

The Pre-Greek hypothesis suggests this common object's name originated in an ancient Mediterranean language rather than being etymologically Greek.
```


### [2026-09-05T17:37:08.818Z] TOOL RESULT

```
# Entry: دیس (dis)

## Persian Definition
According to the Wiktionary entry, in Iranian Persian, **دیس** (dis) means **"platter"** — a flat dish used for serving food.

## Etymology Note
The Persian section indicates that "This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium." Unfortunately, the page does not provide the etymological information you requested about Middle Persian, Proto-Iranian, Avestan, or Proto-Indo-European roots for the Persian term.

## Other Languages
The word appears across multiple languages with different meanings:
- **Shina**: "day"
- **Urdu**: "homeland," "land," "country," or in music, "one of the five deepak rags"

The Urdu entry does contain detailed etymology tracing back through Sanskrit and Proto-Indo-European, but this applies to the Urdu word rather than the Persian entry.
```


## [2026-09-05T17:37:16.108Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%AF%DB%8C%D8%B3",
 "prompt": "Quote the Persian entry تندیس (tandis): meaning and etymology — is it تن (tan) + دیس (dis)? What is said about the element -دیس / Middle Persian dēs 'form, shape' and its Avestan/Proto-Iranian source?"
}
```


## [2026-09-05T17:37:17.182Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/discuss",
 "prompt": "Quote the etymology of \"discuss\" in full — from Latin discutere, dis- + quatere, and the PIE root given."
}
```


### [2026-09-05T17:37:22.358Z] TOOL RESULT

```
# Persian Entry: تندیس (tandis)

## Meaning
According to the Wiktionary entry, **تندیس (tandis)** means "[statue](/wiki/statue "statue")" with a synonym listed as مجسمه (mojassame).

## Etymology
The page confirms your analysis. The word is composed of:
- تن (tan) meaning "body"
- ـدیس (-dis) as a suffix

The etymology tree shows the term derives from Middle Persian *tn'*, tracing back through these component parts.

However, the article does **not** provide detailed information about the Proto-Iranian source, Avestan connections, or the specific historical meaning of the -دیس element beyond indicating it combines with "body" to form "statue." The etymology section focuses on the immediate Persian components rather than deeper etymological reconstruction or Middle Persian semantics.
```


### [2026-09-05T17:37:24.268Z] TOOL RESULT

```
# Etymology of "Discuss"

Based on the Online Etymology Dictionary, here is the full etymology:

The word "discuss" comes from Latin *discutere*, which combines two elements:

1. **dis-** meaning "apart" (from PIE *\*dis-*, a secondary form of *\*dwis-*, related to the concept of "two ways" or "in twain")

2. **quatere** meaning "to shake" (the source also referenced in the word "quash")

Together, the Latin verb meant "to dash to pieces, agitate, strike or shake apart." The sense evolved from this physical meaning through "scatter, disperse" to the post-classical meaning of "investigate, examine," and finally to the modern sense of "examine by argument, debate" attested from the mid-15th century.

The word entered English in the late 14th century as *discussen*.
```


## [2026-09-05T17:37:30.400Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%DB%8C%DA%A9%D8%AA%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for دیکته: the origin tag (e.g. [فر.] = French) and the definition. Also any mention of French dictée."
}
```


## [2026-09-05T17:37:31.761Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%DB%8C%D8%B3%DA%A9/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for دیسک: the origin tag (e.g. [فر.] = French, disque) and the definition."
}
```


### [2026-09-05T17:37:34.351Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for دیکته

**Origin tag:** [فر.] (French)

**Definition:** "(تِ) [فر.] (اِ.) مطلبی که کسی بخواند و دیگری بنویسد"

This translates to: content that one person reads aloud while another person writes it down.

**French connection:** The entry identifies this as a French loanword, with the original French term being *dictée*.
```


### [2026-09-05T17:37:37.548Z] TOOL RESULT

```
# فرهنگ معین Entry for دیسک

**Origin:** [فر.] (French)

**Definitions:**
1. "هر نوع صفحة گرد و تخت آهنین" (any type of round, flat metal plate)
2. "صفحه ای گرد و غضروفی در میان مهره ها که جابه جایی آن ایجاد درد می کند" (a round cartilaginous plate between vertebrae whose displacement causes pain)
3. "نوعی صفحة گرد با وزنی حدود دو کیلوگرم که در ورزش پرتاب دیسک از آن استفاده می کنند" (a round plate weighing approximately two kilograms used in the disc throwing sport)
4. "حافظة جانبی کامپیوتر برای نگه داری سیستم" (computer secondary storage for system maintenance)
```


## [2026-09-05T17:37:51.688Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 112 -l 112 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg112 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T17:37:52.827Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY latin index dis ==\"; grep -n \"DIS\\b\\|DAIS\\|DEIK\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== ARY persian دیس ==\"; grep -n \"دیس\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T17:37:53.714Z] TOOL RESULT

```
total 33488
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:37 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
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
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
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


### [2026-09-05T17:37:53.763Z] TOOL RESULT

```
== ARY latin index dis ==
4140:i FEDID — (414)(OLD IRISH) oS 5432! YAS, VADIS (ALELATIN) 3
4192:HOLD CHURCH $PAVIC) 345 539-1 PES, PEDIS LATIN) 3
4391:PALIZ, FALIZ, JALIZ, PARDIS ;
4393:PARADIS ERENCH) +i, OLD PERSIAN) jhly go,
4396:PARADIS :(RUMANIAN) go *PARI+DEHMI :(SANSKRIT) 2a Sie
4404:POKORNY, —=S*S~*~*«OL PARADIS (DANISH) Sis
4405:BARNHART: PARADIS (SWEDISH) $28 y=
4406:(PARDISE) 754, (PERI-) 777 PARADIS NORWEGIAN) «5$3
8265:DEDEIKHELOS, AGREEK) gly DAOZHAHVA, DVAESH-, DVAESHAH-
8578:SEYDIS TSEK- (TOKHARIAN A) A 5 jis
== ARY persian دیس ==
126:دیسدمان دیگر در باره‌ی گهواره‌ی آغازین هند و اروپایی‌ها این است که زادگاه
748:مهمترین این نوشتارها عبارتند از دو حماسه‌ی هومر به نام‌های «ایلیاد» و «اودیسه» و نمایشنامه‌ها و
1105:شاعر و داستان گزار دربار شاه السینوس (۸1.21770175) در حماسه‌ی ادیسه (0195883) نمونه
1145:ایرنیان به فلات ایران» تصنیف شده است. بخش متأخرتر اوستا دیسا .
4469:۴ _/ پالیز» فالیزء جالیز» پردیس (به چم
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
4513:۱- افردوس "نیز معرب "پردیس" است.
```


## [2026-09-05T17:37:57.613Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg112.png"
}
```


### [2026-09-05T17:37:57.953Z] TOOL RESULT

```

```


## [2026-09-05T17:37:57.950Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:38:09.308Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"Teach\" \"Token\" \"Toe,\" \"Desk\" \"Disc\" \"Discuss\" \"Digit\" \"Index\" \"Judge\" \"Dictate\"; do echo \"--- $w ---\"; grep -n \"^$w\" SKT.txt | head -3; done"
}
```


### [2026-09-05T17:38:10.853Z] TOOL RESULT

```
--- Teach ---
19248:Teach ;  sec  Token.
--- Token ---
19819:Token.  (E.)  hi.  K.  token.  AS. tden.  -  A.  S.  tedA  (  -  tdh  •),  pt  L  <rf usually  ti^n,  to  point  out.  todjciie, to  accuse,  criminate.  4*  Do  tetkm, tdhn,  teikn,  Dan  tegm.  Swed.  McAl uichen,  Goth  taikm.  All  from 'XWX^^ViWi,  whence  U  in point  out.     Sec  Diotlon.
--- Toe, ---
--- Desk ---
--- Disc ---
5146:Disclose:  see  CIaubo.
5150:Discord;  see  Cordial.
5151:Discount ;  sec  PutatiTS.
--- Discuss ---
5158:Discuss :  see  Qua»h.
--- Digit ---
5056:Digit,  a  finger,  figure.  CL.)  L.  digitns, a  fmj;ei ;  hence  a  figure,  from  counting  on the  finders.  +  Gk.  WjurvAuc.  ,\.  S.  id,  see Daotyl.Too.  (VlJAK,  to  lake  (Curtius).)
--- Index ---
9173:Index,  Indicate ;  see  Dlotlon.
--- Judge ---
9545:Judge.  (F.-L.)    F. /«of— L. ace  of  iudtjc,  a  judge,  lit.  *  one out  law.'  — L.   iuj,  law;   Jii out     Sec  Jury  and  Diotion. acUudge.   \J.  -  L.)     .M. also  aiugtm  (■cd/w^yi*),- O. decide  —  L.  adiuJicare,  lo  awai to ;  iuJuart^  to  judge,    from  iudit of  iuiUjK,  a  judge  I  above).
--- Dictate ---
```


## [2026-09-05T17:38:14.124Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dey%E1%B8%B1-' --note 'page 112, root Deik: PIE *deyḱ- \"to point out, show\", Pokorny 188-189, descendants incl. Latin index/iudex/digitus, Germanic *taikjaną/*taihwō' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CF%83%CE%BA%CE%BF%CF%82' --note 'page 112, node 9/12: Greek diskos, traditional derivation from dikein rejected by Furnee/Beekes as Pre-Greek' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/discuss' --note 'page 112, node 12: discuss < L. discutere = dis- + quatere, NOT from deik-'"
}
```


### [2026-09-05T17:38:16.385Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/405ea4c0f98f1669.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dff9639020a30f28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/662beae66826e5b4.txt
```


## [2026-09-05T17:38:26.790Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Diction\\|^Dish\\|^Dais\\|^Disk\\|^Discus\" SKT.txt | head; echo \"---\"; sed -n '5060,5070p' SKT.txt; echo \"--- pages ---\"; python3 - <<'EOF'\ntxt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=0; ll={}\nfor i,l in enumerate(lines,1):\n    ll[i]=leaf; leaf+=l.count('\\f')\nfor n in (5056,5158,9173,9545,19819):\n    print(n,'leaf',ll[n],'printed',ll[n]-20)\nEOF"
}
```


### [2026-09-05T17:38:28.405Z] TOOL RESULT

```
4651:Dais ;  see  Diso.
4652:Daisy ;  sec  Day.
5158:Discuss :  see  Qua»h.
5166:Dish ;  see  Dlao.
5169:Disk ;  see  Diso.
---
i
■
I
lay;
I
iS
DIGRESS.
DIORAMA.
(F, -L>  ILK.
-O.F. KicnfalcacH.  *  I.
r.  ^"nraF.
--- pages ---
5056 leaf 139 printed 119
5158 leaf 141 printed 121
9173 leaf 243 printed 223
9545 leaf 252 printed 232
19819 leaf 540 printed 520
```


## [2026-09-05T17:38:30.522Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%DB%8C%DA%A9%D8%AA%D9%87/' --note 'page 112, node 7: Moin dikte [فر.] French loan' ; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%DB%8C%D8%B3%DA%A9/' --note 'page 112, node 11: Moin disk [فر.] French loan' ; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%DB%8C%DA%A9%D8%AA%D8%A7%D8%AA%D9%88%D8%B1/' --note 'page 112, node 7: Moin diktator [فر.] French loan'"
}
```


### [2026-09-05T17:38:37.342Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5be0a7891b2b8e27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b606914be14b273.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f692cd0225240484.txt
```


## [2026-09-05T17:38:41.033Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5140,5172p' SKT.txt"
}
```


### [2026-09-05T17:38:41.070Z] TOOL RESULT

```
O,  P.  dtis^  dels,  B  high  table.  *L.  diicus, a  qaoit,  pUtter;  m  late  L.,  a  table.  «Gk. 9/<rMot  (abovel.
desk,  a  sloping  table.  (L  — f;V.)  M  E. daJ^e,  dtsk,  a  variant  of  dish  or  disc^lu. ducuf,  a  disc  (above).
diah,  a  platter.  (L.«>Gk.1  M.  E.  disrA. A.  S,  diic^  a  dish.  —  L.  ditcus^  a  quoit, putter  (abovel.
Disoem ;  see  Concern.
DlBciple.  (F.-I,.)  OF.  disnpJe.^t, disripuium,  ace.  of  ducipuiaij,  a   learner.
—  L.  discert,  to  learn;  alUetl  to  dccere,  to teach  ;  sec  DooUe.  Dor.  dt'jdfiiiru,  O.  F. dunpiin4,  L.  distiplina,  teaniiag.
Disclose:  see  CIaubo.
I>iBOomfit.  tF.  -  L.)  M,  E.  discomfit (Brace). —  O.F.  disconfiz,  discomfited,  ^p. oi  dacffftfirt,  *  to  discomfit,  vanquish/  C-ot
—  O.  F.  des-  (L-  dis-) ;  and  cenpre,  to  pre- serve, make  ready,  from  L.  c<mfiart»  to preserve ;  see  Faot.
Diacoosolate;  see  Bolaoa.
Discord;  see  Cordial.
Discount ;  sec  PutatiTS.
Diacourae:  see  Current
Discover ;  sec  Cover.
Discroot ;  see  Concern.
Discrepant ;  see  Crevice.
Discriminate :  sec  Conoem,
Discursive ;  &ee  Current.
Discuss :  see  Qua»h.
Disdain ;  e/;c  Disnlty,
Disease ;  see  Cone.
Disembark:  see  Buk  (1).
I>isembog:ue ;  see  Bebouoh.
Disfrrooe ;  see  Qraoe.
Diaguise ;  sec  Wise  (a).
DisgtiBt;  sceOu8t(a).
Dish ;  see  Dlao.
IMshevel ;  see  CapiUarr.
Disinterested  ;  sc*  Intoreat  (i).
Disk ;  see  Diso.
Dislocate ;  see  Looua.
DismaL  (F.-U?)  In  ok)  books,  the nsuftl  phr.  Ls  'dumai  days.'  which  proU refers  10  tithing-time.^O.  F.  ditma/,  adj. » L.  decimaiis,  relating  to  tithes  «  L. decima  (O.  F.  dismt),  a  tithe.  — L.  dccfm, ten.  C  Or  else  '  dismal  days '  -  O.  F.  d:. ffM/.—L.  dits  mail,  evil  days.
Diamantlo ;  9ct  Mantle.
```


## [2026-09-05T17:38:45.641Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5125,5142p' SKT.txt"
}
```


### [2026-09-05T17:38:45.685Z] TOOL RESULT

```
like  the  E.  verbal  prefix  Mn--
be^nnin^  with  ihit  prefix.
forms.    For  euimple.  for
and  so  un. Aater.
ite.  (L.-Ck.)
.  ..  —  Cik.  iitrmn,  a
iciir.  to  cast,  til  row.
iri  0oor  in  a  HaU.  iF.^L.*
o^  the  raikcd  iilaiform  on
table    in  a    hall    stands.
table  i!Mif\  but  was
over  a  scat  of  i^tate,
U.^d€i$,d£ys,'~
DISPEU
119
O,  P.  dtis^  dels,  B  high  table.  *L.  diicus, a  qaoit,  pUtter;  m  late  L.,  a  table.  «Gk. 9/<rMot  (abovel.
desk,  a  sloping  table.  (L  — f;V.)  M  E. daJ^e,  dtsk,  a  variant  of  dish  or  disc^lu. ducuf,  a  disc  (above).
diah,  a  platter.  (L.«>Gk.1  M.  E.  disrA. A.  S,  diic^  a  dish.  —  L.  ditcus^  a  quoit, putter  (abovel.
```


## [2026-09-05T17:38:55.610Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dictate,\\|dictator,\\|digit,\\|judge,  n\\|index,  n\" KLN_1966.txt | head -8"
}
```


### [2026-09-05T17:38:55.663Z] TOOL RESULT

```
11332:Dictamnus,  n.,  a  genus  of  plants  of  the  rue  family (bot.)  —  L.  dictamnus.  See  dittany, dictaphone,  n.,  a  phonographic  instrument  for recording  and  reproducing.  —  A  hybrid  coined fr.  L.  dictare,  ‘to  dictate’,  and  Gk.  tpiovif),  ‘sound, voice’.  See  dictate  and  phone,  ‘speech,  sound’, dictate,  tr.  and  intr.  v.  —  L.  dictatus,  pp.  of  dic¬ tare,  ‘to  say  often,  pronounce  repeatedly,  dic¬ tate  (for  writing)’,  freq.  of  dicere  (pp.  dictus), ‘to  say’.  See  diction  and  verbal  suff.  -ate  and  cp. dictum,  dight,  ditty,  indict, dictate,  n.  —  L.  dictatum,  ‘something  dictated’, neut.  pp.  of  dictare.  See  dictate,  v. dictation,  n.  —  ML.  dictatid,  gen.  -onis,  fr.  L. dictatus,  pp.  of  dictare.  See  dictate,  v.,  and  -ion. Derivative :  dictation-al,  adj. dictator,  n.  —  L.  dictator,  fr.  dictatus,  pp.  of  dic¬ tare.  See  dictate  and  agential  suff.  -or. dictatorial,  adj.  —  Formed  with  adj.  suff.  -al  fr. L.  dictatorius,  fr.  dictator.  See  prec.  word. Derivatives:  dictatorial-ly,  adv.,  dictatorial¬ ness,  n.
11334:consecrate,  devote’,  and  to  Oscan  deikum , deicum,  ‘to  speak’,  fr.  I.-E.  base  *deik-,  *dik-, ‘to  show,  point  out’,  whence  also  L.  digitus, ‘finger’  (lit.  ‘pointer’),  the  second  element  in  L. jit-dex,  ‘judge’  (lit.  ‘he  who  shows  or  teaches justice’),  in-dex,  forefinger,  index’  (lit.  ‘pointer’), and  OI.  disati,  ‘shows’,  disd,  ‘direction’,  desdh, ‘region’,  Hitt,  tekkushami,  ‘I  show’,  Gk. Sstxvuvai,  ‘to  show’,  8ixt),  ‘custom,  usage,  or¬ der,  right’,  Goth,  ga-teihan,  ‘to  announce’,  OE. teon  (for  *tih-an),  ‘to  accuse’,  tacen,  tacn,  ‘sign, token’,  tieean,  ‘to  show,  teach’.  Cp.  teach  and words  there  referred  to.  Cp.  also  abdicate,  addict, apodictic,  benediction,  benison,  condition,  con¬ tradict,  dedicate,  deictic,  dicast,  dictate,  diction¬ ary,  dictum,  dight,  digit,  ditto,  edict,  endeictic, epidictic,  fatidic,  index,  indicate,  indicia,  indict, indite,  interdict,  judge,  judicial,  juridical,  juris¬ diction,  malediction,  malison,  paradigm,  policy, ‘document’,  preach,  preconize,  predicate,  predict, soi-disant,  Swadeshi,  syndic,  valediction,  verdict, veridical,  vindicate.
11398:Derivatives:  digestive-ly,  adv.,  digestive-ness ,  n. dight,  tr.  v.,  to  adorn  {poetic).  —  ME.  dihten,  fr. OE.  dihtan,  ‘to  dictate,  guide,  compose,  set  in order’,  fr.  L.  dictdre,  ‘to  dictate’  (whence  also OHG.  dihton ,  tihton,  ‘to  write,  compose’,  MHG. tihten,  G.  dichten,  ‘to  write  poetry’).  See  dictate,  v. digit,  n.,  i)  a  finger  or  toe;  2)  any  figure  from o  to 9.  —  L.  digitus,  ‘finger,  toe’,  prob.  dissimilated fr.  orig.  *dic-itus,  prop,  ‘pointer’,  fr.  I.-E.  base *deik-,  ‘to  show’,  whence  also  OE.  tdhe,  td,  ‘toe’. See  diction  and  cp.  toe.  Cp.  also  interdigitate, dital,  and  the  second  element  in  hallux, digital,  adj.,  pertaining  to  the  fingers.  —  L.  di¬ gitalis,  fr.  digitus.  See  prec.  word  and  adj. suff.  -al.
11887:ditto,  n.,  the  same  (lit.  the  foresaid).  —  It.,  form used  in  Tuscany  for  literary  It,  detto,  ‘that  which has  been  said  (before)’,  pp.  of  dire,  ‘to  say’,  fr. L.  dicere,  ‘to  say’.  See  diction  and  cp.  dictum, dittography,  n.,  the  unintentional  repetition  of  a letter  or  letters  in  writing.  —  Compounded  of Gk.  Sitto?,  Att.  var.  of  Siacroc,  ‘double,  two¬ fold’,  and  -ypacpla,  fr.  ypacpsiv,  ‘to  write’.  For the  first  element  see  disso-  and  cp.  words  there referred  to,  for  the  second  see  -graphy. Derivative:  dittograph-ic,  adj. dittology,  n.,  a  twofold  reading  or  interpretation. —  Compounded  of  Gk.  8ixx6<;,  ‘double,  two¬ fold’,  and  -Xoyla,  fr.  -Xoyos,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  prec.  word  and  -logy, ditty,  n.,  a  short  song.  —  ME.  dite,  ditee,  fr.  OF. ditie,  dite,  fr.  L.  dictatum,  ‘anything  dictated’, prop.  neut.  pp.  of  dictare,  ‘to  say  often,  pro¬ nounce  repeatedly’,  freq.  of  dicere  (pp.  dictus), ‘to  say’.  See  diction  and  cp.  dictate,  dight. Derivative:  ditty,  it.  and  intr.  v. diuresis,  n.,  excessive  excretion  of  urine  (med.)  — Medical  L.,  fr.  Gk.  *Sioup7)at?,  ‘urination’,  fr. SioupcTv,  ‘to  pass  urine’,  fr.  Sta,  ‘through’,  and oupEiv,  ‘to  make  water’,  fr.  oupov,  ‘urine’.  See dia-,  urine  and  -esis,  and  cp.  next  word, diuretic,  adj.,  increasing,  or  tending  to  increase the  secretion  of  urine.  —  Late  L.  dureticus,  fr. Gk.  Siouprjxixi?,  ‘pertaining  to  urine’,  fr. Stoupcuv,  ‘to  pass  urine’.  See  prec.  word  and  -ic. Derivatives:  diuretic,  n.,  a  diuretic  drug,  diu- retic-al-ly,  adv.,  diuretic-al-ness,  n. diurnal,  adj.,  daily.  —  L.  diurnalis,  diurnal’,  fr. diurnus,  ‘daily’,  which  is  formed  fr.  di-(es),  ‘day’, with  -urnus,  an  adj.  suff.  denoting  time.  This suffix  is  a  contraction  of  orig.  *ri-nos,  which derives  fr.  Gk.  -pivo?,  a  suff.  of  the  same  mean¬ ing.  (Cp.  e.g.  Gk.  xei(xepiv<S<;  —  L.  hibernus, ‘wintry’.)  See  dies  non  and  adj.  suff.  -al  and  cp. next  word.  Cp.  also  journal,  which  is  a  doublet of  diurnal.  Cp.  also  journey,  adjourn,  sojourn. For  the  suff.  cp.  nocturnal,  modern.
19159:index,  n.  —  L.  index,  gen.  indicia ,  ‘a  pointer,  in¬ dicator;  the  forefinger;  sign,  mark,  indication; guide,  witness,  informer’,  rel.  to  indicdre,  ‘to point  out,  show’.  See  indicate.
19166:Derivative:  indicative-ly,  adv. indicative,  n.  —  F.  indicatif  See  indicative,  adj. indicator,  n.  —  Late  L.,  ‘one  that  points  out  or shows’,  fr.  L.  indicatus,  pp.  of  indicdre.  See  in¬ dicate  and  agential  suff.  -or. indicia,  n.  pi.,  indications.  —  L„  pi.  of  indicium, ‘information,  discovery,  disclosure;  sign,  mark’, fr.  index,  gen.  indicis.  See  index, indict,  tr.  v.,  to  charge  with  a  crime.  —  ME.  en- diten,  ‘to  dictate,  write  down,  accuse,  indict’, fr.  OF.  enditer,  ‘to  dictate,  write  down ;  to  sug¬ gest,  teach;  to  prescribe’,  fr.  VL.  *indictare,  ‘to declare,  proclaim  in  writing’,  fr.  in-,  ‘in’,  and L.  dictare,  ‘to  say  often,  declare,  prescribe,  dic¬ tate’.  See  dictate  and  cp.  indite,  which  is  a  dou¬ blet  of  indict.  Cp.  also  indicate,  indicia. Derivatives:  indict-able,  adj.,  indict-ee,  n.,  in- dict-or,  n.,  indict-ment,  n.
19197:Derivatives:  indistinct-ion,  n.,  indistinct-ive,  adj., indistinct-ive-ly,  adv.,  indistinct-ive-ness,  n.,  in- distinct-ly,  adv.,  indistinct-ness,  n. indite,  tr.  v.,  to  write,  put  down  in  writing.  — ME.  enditen,  ‘to  dictate,  write  down’.  See  indict. indium,n.,name  of  a  rare  metallic  element  (chem.) —  ModL.,  coined  by  its  discoverers,  the  Ger¬ man  chemists  Ferdinand  Reich  and  Theodor Richter,  in  1863,  fr.  L.  indicum,  ‘indigo’  (see
20419:Jude,  masc.  PN.  —  A  variant  of  Judah, judex,  n.,  a  judge.  —  L.  See  judge, judge,  n.  —  ME .  juge,  fr.  OF.  (=  F.)  juge,  fr.  L. judicem,  acc.  of  judex,  ‘judge’,  which  stands  for *jous-dik-s  and  orig.  meant  ‘one  who  shows right’,  fr.  jus,  ‘right’,  and  the  stem  of  dicere,  ‘to show,  tell,  say’.  See  jus  and  diction  and  cp.  pre¬ judice.  Cp.  also  the  second  element  in  preach, judge,  tr.  and  intr.  v.  —  ME.  jugen,  fr.  OF.  jugier, juger  (F .juger),  ‘to  judge’,  fr.  L.  judicare,  of  s.m., fr.  judex,  gen.  judicis.  See  judge,  n.,  and  cp. adjudicate.  Cp.  also  hoosegow. judgmatic,  judgmatical,  adj.,  showing  good  judg¬ ment  (colloq.)  —  A  hybrid  formed  fr.  judge,  n., with  the  ending  -matic  (on  analogy  of  dogmatic). Derivative:  judgmatic-al-ly,  adv. judgment,  judgement,  n.  —  ME .jugement,  fr.  OF. (=  F.)  jugement,  fr.  juger,  ‘to  judge’.  See  judge, v.,  and  -ment.
```


## [2026-09-05T17:39:30.659Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n'); leaf=0; ll={}\nfor i,l in enumerate(lines,1):\n    ll[i]=leaf; leaf+=l.count('\\f')\nimport re\nleaves=txt.split('\\f')\nfor n in (11332,11334,11398,19159,20419,38337,39440):\n    lf=ll[n]\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', leaves[lf])\n    print(n,'leaf',lf,'pagenums_on_leaf',nums)\nEOF"
}
```


### [2026-09-05T17:39:32.521Z] TOOL RESULT

```
11332 leaf 244 pagenums_on_leaf ['444', '445', '446']
11334 leaf 244 pagenums_on_leaf ['444', '445', '446']
11398 leaf 245 pagenums_on_leaf ['447', '448']
19159 leaf 422 pagenums_on_leaf ['786', '787']
20419 leaf 450 pagenums_on_leaf ['834', '835']
38337 leaf 836 pagenums_on_leaf ['1578', '1579']
39440 leaf 861 pagenums_on_leaf []
```


## [2026-09-05T17:39:42.625Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '48905,48950p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T17:39:42.679Z] TOOL RESULT

```
lit. daind und gr. dtvog zusammenzubringen und die iibrigen Worte als 



776 


deik- 


eine verschiedene Sippe der Bed. „naehschieBen“ von ihnen zu trennen? 

Mit einer Bed. „drehen“ und „drehend sehwingen" vereinbar, aber lautlieh 
sehr unsicber, ist die Yerknupfung von got. tains usw. mit gr. bora £ „Rohr" 
(jiingeres jon. bovva ij und vereinzeltes dor. da>va£ metr. Dehnung? Schulze 
Qu. ep. 205, Boisacq 196), <5or«o ,.schiittle“, aUdovog „imMeerherumgetrieben“ 
(fiir Boisacq klingt doreco nur zufiillig an dova£ an;?) und lett. duonis , duoni 
„Schilf, Binsen" (bzw. von Zubaty BB. 18, 250), s. Fick BB. 3, 169; 12, 161; 
26, 246, Wb. I 4 459 (hier unter Berufung auf das Ablautverhaltnis anord. 
hein , av. saeni : gr. y.&voz), Prellwitz 2 120 (mit *dei- ablautendes *ddi: *ddi- 
und *do[i] : do-), Wiedemann aaO., Miihlenbach-Endzelin I 534. 

deik- „zeigen", woraus lat. und germ. z. T. „mit Worten auf etwas hin- 
weisen, sagen", mehrfach auch zum gerichtlichen Sinn „auf den Tater 
hinweisen, beschuldigen" entwickelt. 

Ai. didesti , dicdti , zeigt, weist", av. dues- , zeigen" ( daesayeiti , disyeiti , 
daedoist) „zeigen; jemandem etwas zuweisen, zusprechen", ptc. ai. dista- 
= lat. dictus , diifi-h „Weisung, Yorschrift", av. adisti-s , Anweisung, Lehre" 
= lat. dicti-o, ags. tiht „Anklage“, ahd. in-, bi-ziht ds., nbd. Verzicht, ai. 
die- „Weisung, Richtung", diga „Ricbtung“ (=) SUrj „Recht“ (woraus wohl 
lat. dicis causa „nur der Form wegen, zum Schein", s. Yf. LEWb. 2 s. v.), dega-h 
„(Richtung), Gegend" = an. teigr s. u.; gr. beiy.vvyi ,,zeige“, kret. mbiy.vvzi 
„£mdetxvvoi'‘ , betgig „das Zur-Schau-Stellen" (mit sekundarer Hochstufe), 
dinrj s. o., bly.aiog, diy.d£a>, ubiy.og ; das Pf. med. debeiyfiai, und beiypa , ,Be- 
weis, Beispiel" nicht mit idg. g, sondern gr. Entgleisung) ; lat. dicere „sagen“, 
dicare „feierlich verkiinden, zusprechen, weihen“, osk. deikum „dicere“, 
umbr. teitu, deitu „dicito“, ablautend osk. dicast,, dixerit", umbr . dersicust 
ds., tig el „dicatio", osk . da-dikatted ,,dedzcavit“, u. tikamne „*dicamine“, lat. 
dicio „die Macht eines Herrn fiber andere, Botmabigkeit, Gerichtsbarkeit", 
indicare „anzeigen", index „Anzeiger, Angeber; Zeigefinger“ (wie auch ai. 
degini ,Zeigefinger“), index „der das Recht weisende", vindex, causidicus; 
got. gateihan ,.anzeigen, verkiindigen“, anord. tea, tia „zeigen, darstellen, 
ankiindigen", ags. tion ,,anzeigen, verkiindigen“, ahd. zihan „anschuldigen, 
zeihen-‘ , wozu (nach Osthoff MU. 4, 206 f.) anord. tigenn .^monstratus) vor- 
nehm", tign f. „Rang; vornehmer Mann‘; ahd. seigon „zeigen", wovon
```


## [2026-09-05T17:39:48.331Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg112.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/112.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T17:39:48.395Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T17:39:50.065Z] AGENT

Now let me write the verification file.


## [2026-09-05T17:46:25.706Z] TOOL CALL #65: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-112.json",
 "content": "{\n  \"pdf_page\": 112,\n  \"book_page\": 82,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Deik\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *deyḱ- 'to show, point out' (Pokorny 188 deiḱ- 'zeigen'; Walde-Pokorny I 776; Watkins/AHD deik- 'to show, pronounce solemnly'; LIV² 108-109)\",\n      \"note\": \"The root box is right on all three counts. Pokorny p.188 heads the entry 'deik- ,zeigen', woraus lat. und germ. z. T. ,mit Worten auf etwas hinweisen, sagen'', so the reconstruction, the label 'Indo-European' and the gloss 'to show' are exactly what the standard handbooks give. Two refinements a reader should know. (a) The root has a doublet *deig- (Pokorny: 'Daneben idg. doig- in got. taikns ... ags. tǣcan, engl. teach'); Nourai's Germanic branch (node 3) in fact belongs to that variant, and AHD explicitly files TEACH/TOKEN under 'Variant *deig-'. (b) The whole chart, including its wording, is copied from the AHD (Watkins) appendix entry deik-, which reads: 'deik-. To show, pronounce solemnly ... 1. O-grade form *doig- in: a. Germanic *taikjan, to show ... 2. Latin digitus, finger (< \\\"pointer\\\") ... 4. Agential suffix *-dik- in: a. Latin index ... b. Latin jūdex ... 6. Zero-grade form *dik- in Greek dikein, to throw (< \\\"to direct an object\\\"): DISK. [Pok. deik- 188.]' Nourai's node glosses are Watkins' glosses verbatim. That also means the chart inherits Watkins' weakest link, the Greek dikein/diskos branch (see nodes 9-12), and one plain error, 'discuss' (node 12). No Persian branch is affected by that: the Avestan → Persian dīs/dīz line (nodes 1-2) is the well-attested part.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *deyḱ- «نشان دادن، نمودن» ریشه‌ای اصیل و پذیرفته‌شده است؛ پوکورنی در صفحهٔ ۱۸۸ همین صورت و همین معنی را می‌آورد («deik- ,zeigen'») و والده-پوکورنی (جلد ۱، ص ۷۷۶) و پیوست واتکینز در فرهنگ American Heritage نیز همان را دارند. پس برچسب زبانی و معنای جعبهٔ ریشه در نمودار نورایی درست است. دو نکته: نخست آنکه این ریشه گونهٔ دیگری به صورت *deig- دارد و شاخهٔ ژرمنی نمودار (گرهٔ ۳) در حقیقت از همان گونه است، نه از *deik- ساده. دوم آنکه سراسر این نمودار، حتی معناهای انگلیسی گره‌ها، واژه‌به‌واژه از مدخل deik- در پیوست واتکینز برداشته شده است؛ از این رو ضعف همان مدخل — یعنی پیوند یونانی dikein و diskos — به نمودار نورایی هم راه یافته و یک خطای آشکار («discuss» در گرهٔ ۱۲) نیز از همان‌جا آمده است. بخش ایرانی نمودار (اوستایی daēs- ← فارسی دیس/دیز) استوارترین بخش آن است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:188\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt, form-feed leaf 197 (= printed p.188; the page numeral 189 follows inside the entry): 'deik- ,zeigen', woraus lat. und germ. z. T. ,mit Worten auf etwas hinweisen, sagen', mehrfach auch ,das Recht weisen, auf den Täter hinweisen, beschuldigen' entwickelt; Partiz. Pass. dik-tó-s; dikā ,Richtung', dik-ti- ,Anweisung', deiko-s ,Richtung'.' The page number Nourai cites is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p.776 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt line 48927)\",\n          \"stance\": \"supports\",\n          \"note\": \"'deik- „zeigen\\\", woraus lat. und germ. z. T. „mit Worten auf etwas hinweisen, sagen\\\", mehrfach auch zum gerichtlichen Sinn „auf den Täter hinweisen, beschuldigen\\\" entwickelt.' — Pokorny's 1959 entry is a reprint of this; Pokorny himself refers to 'WP. I 776 f.'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt line 360, s.v. deik-\",\n          \"stance\": \"supports\",\n          \"note\": \"'deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. ... [Pok. deik- 188.]' — Watkins' gloss and Pokorny reference are identical to Nourai's root box.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"IEC.txt line 2109, s.v. deikō\",\n          \"stance\": \"supports\",\n          \"note\": \"'deikó (deiKnu-, diK-) \\\"show, tell\\\". Cf. deiKs-, diK-. WP I, 776. Skt. cf. diśāmi; Oss. cf. dis, des \\\"marvel\\\", áv-disín, -desun \\\"show\\\"; Hitt. cf. tekkusami; Gk. deíknumi; Lat. dico; Osc. inf. deíkum; Go. ga-teihan \\\"announce\\\"' — Mann reconstructs the same root with the same meaning.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"SYN.txt concept 15.55 SHOW (vb.), section 1\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. IE deik-. Walde-P. 1.776. Ernout-M. 265 ff. Walde-H. 1.348 f. Here as \\\"show\\\": Grk. δείκνυμι ... Skt. diś-, Av. diś-; cf. in secondary sense Lat. dicere \\\"say\\\" ... Goth. ga-teihan \\\"announce\\\"'. Buck adds the semantic key Nourai's chart depends on: 'it seems likely that the primary notion was \\\"point (as with the finger), point out\\\"'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"daěs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan daēs- 'to show' is a real, well-attested verb: Bartholomae, Altiranisches Wörterbuch cols. 671-674, lists it as 'daēs- V. \\\"zeigen\\\". Praes. daēdōiš-, (auch Pass.) disya-, (Iter.) daēsaya-, s-Aor. dāiš-, dōiš- : diš-', with the senses '1) jemandem (Gen.) etwas (Akk.) zeigen, sehen lassen; 2) jemandem (Dat.) etwas zuweisen, zusprechen; 3) jemanden unterweisen, belehren; 4) kundmachen'. It is the regular Iranian continuant of PIE *deyḱ-: Proto-Indo-Iranian *daiś- gives Vedic diśáti / dideṣṭi 'shows' and Av. daēs- exactly (the Avestan e-grade daē- < *dai- < PIE *dei-, with the palatal *ḱ appearing as Iranian s, Skt. ś — the satem outcome). Nourai's transliteration 'daěs' uses his own diacritic for the ē of daēs-; the gloss 'to show, demonstrate' is Bartholomae's 'zeigen' plus 'kundmachen'. The one imprecision is that Nourai writes the bare root without the hyphen the Iranists use.\",\n          \"derivation_fa\": \"فعل اوستایی -daēs «نمودن، نشان دادن» واژه‌ای اصیل و پرکاربرد در اوستاست؛ بارتولومه در «فرهنگ ایرانی باستان» (ستون‌های ۶۷۱ تا ۶۷۴) آن را چنین ثبت کرده است: «daēs- فعل: نشان دادن»، با ستاک‌های حال daēdōiš-، disya- و daēsaya- و آاوریست dāiš-/dōiš-، و معناهای «چیزی را به کسی نشان دادن»، «چیزی را به کسی واگذاردن»، «کسی را آموختن» و «آشکار کردن». این فعل بازماندهٔ منظم ریشهٔ هندواروپایی *deyḱ- در ایرانی است: در هندوایرانی آغازین *daiś- شده و در سنسکریت diśáti و در اوستایی daēs- بازتاب یافته؛ همخوان کامی *ḱ در زبان‌های ساتم (از جمله ایرانی) به s / ś بدل شده است. ضبط نورایی («daěs») همان daēs- است با نشانهٔ ویژهٔ خودِ او برای ē. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:188\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt leaf 197 (p.188), inside the deik- entry: 'Ai. dideṣṭi, diśáti, deśayati ,zeigt, weist', av. daēs- Aor. dōiš- ,zeigen' (daēsayeiti, disyeiti, daēdōišt) ,zeigen; jemandem etwas zuweisen, zusprechen''. Pokorny's page therefore does carry the Avestan verb exactly as Nourai draws it under the root.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"BRT.txt cols. 671-674 s.v. daēs-\",\n              \"stance\": \"supports\",\n              \"note\": \"'daēs- V. \\\"zeigen\\\". Praes. daēdōiš-, (auch Pass.) disya-, (Iter.) daēsaya-, s-Aor. dāiš- / dōiš- : diš-.' followed by the four attested senses with Yasna/Vendidad citations (Y 43.10, Y 51.2, V 5.14, Yt 11.14).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"CHEUNG.txt line 4397 ff., root *daiš¹ 'to show'\",\n              \"stance\": \"supports\",\n              \"note\": \"'*daiš¹ \\\"to show\\\". AVESTAN: daēs- \\\"to show\\\" || (+ *fra-) \\\"to show\\\" || (+ *ham-) \\\"to be told, be shown\\\" — Liste: 30'; Cheung's Etymological Dictionary of the Iranian Verb then traces it into MP uzdēs 'idol', handēs- 'to think', Parthian ʾdysg 'sign'. This is the current standard treatment of the verb.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt line 360 s.v. deik-\",\n              \"stance\": \"silent\",\n              \"note\": \"Watkins' appendix lists no Iranian reflex at all (only Latin, Greek and Germanic), so Nourai's Avestan node comes from Pokorny, not from AHD, even though he tags the Germanic/Latin/Greek nodes 'AHD'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"dîs, dîz\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The chart's two Persian forms need to be judged separately. (a) -dīs / -dēs 'resembling, having the shape of' is solidly derived from Av. daēs-: Av. daēsa- m. 'Zeichen, Omen' (Bartholomae col. 673) → Middle Persian dēs / dēsag [dys(k)] 'form, appearance' (MacKenzie, Concise Pahlavi Dictionary p.22 'dēs(ag) [dys(k)| M dys] form, appearance'; Nyberg II p.64 'dēs [dys] shape, form ... MPrs dys; NP -dēs, e.g. māh-dēs \\\"moon-like\\\" ... From daēs-') → New Persian -dīs, the bound second member of تندیس tandīs 'body-shape' = statue, طاقدیس tāqdīs 'arch-shaped' (Khosrow's throne), فرخاردیس, خایه‌دیس 'egg-shaped'. The Middle Persian ē regularly raises to New Persian ī (majhūl ē > maʿrūf ī in the eastern/modern reading), which is why the book prints dīs beside the older dēs. The same daēs- gives MP uzdēs 'idol' (lit. 'image, thing shown'), Parthian ʾdysg 'sign'. (b) دیز dīz 'black, (dark) colour', as in شبدیز šabdīz, Khosrow Parvēz's black horse (Nezāmī's line quoted by Nourai) and دیزه dīza 'dark grey (horse)', is only tentatively attached here: Moʿin's footnote at Borhān-e Qāṭeʿ p.912 reports it as Pūrdāvūd's conjecture ('شاید «دیز» از کلمهٔ daēsa- باشد … بنابراین شبدیز لغةً بمعنی شب‌نما') and has to assume an ad-hoc s > z (he adduces اسپریس/اسپریز). So 'appearance, resemblance' is confirmed, 'color' is a conjecture. Also note the older dispute the chart hides: Horn (Grundriss no. 593, p.125) derived -dēs/-dis not from daēs- at all but from Av. darəs- / Skt. dṛś- 'to see' ('-dēs, -dis, -des \\\"gleichend, ähnlich\\\": aw. darəs- \\\"Blick\\\", ai. dṛś-'), calling Av. daēsa- 'zu unsicher, um verglichen werden zu können'. Hübschmann, whose page Nourai cites, was written expressly to overturn Horn on this point, and Bartholomae, Nyberg, MacKenzie and Cheung follow Hübschmann. Modern scholarship therefore sides with Nourai — but only for dīs.\",\n          \"derivation_fa\": \"دو صورتی که نورایی در این جعبه آورده باید جدا سنجیده شود. نخست «ـ دیس» (در تندیس، طاقدیس، فرخاردیس) به معنی «همانند، به شکلِ»: این جزء به‌روشنی از daēsa- اوستایی «نشانه، نمود» می‌آید که خود از مصدر daēs- «نمودن» ساخته شده؛ در فارسی میانه dēs / dēsag «شکل، صورت» شده (مکنزی، ص ۲۲؛ نیبرگ، ج ۲ ص ۶۴: «dēs … در فارسی نو ـ دیس، مانند ماه‌دیس، از daēs-») و ای مجهولِ فارسی میانه در فارسی نو به ی معروف بدل شده و «ـ دیس» به دست آمده است. از همین ریشه است uzdēs پهلوی «بت» (یعنی «نمود، تصویر») و ʾdysg پارتی «نشانه». دوم «دیز» به معنی سیاه و رنگ (در شبدیز، دیزه): این پیوند تنها گمانی است؛ معین در حاشیهٔ برهان قاطع (ص ۹۱۲) آن را از قول پورداود می‌آورد («شاید دیز از کلمهٔ daēsa- باشد … بنابراین شبدیز لغةً بمعنی شب‌نما») و ناچار است ابدال س به ز را با نمونهٔ اسپریس/اسپریز توجیه کند. نکتهٔ سوم آنکه هرن در «بنیاد ریشه‌شناسی فارسی نو» (شمارهٔ ۵۹۳، ص ۱۲۵) این «ـ دیس» را نه از daēs- بلکه از darəs- اوستایی و dṛś- سنسکریت «دیدن» می‌گرفت و daēsa- را «نامطمئن‌تر از آن» می‌دانست که بتوان سنجید؛ هوبشمان همان صفحه‌ای را که نورایی ارجاع می‌دهد برای رد نظر هرن نوشت و بارتولومه و نیبرگ و مکنزی و چونگ نیز از هوبشمان پیروی کرده‌اند. پس ادعای نورایی دربارهٔ «دیس» پذیرفتنی و امروزه پذیرفته است، ولی «دیز» با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تندیس\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HUB:65\",\n              \"status\": \"supports\",\n              \"note\": \"HUB.txt form-feed leaf 76 (= printed p.65, header '— 65 -'), entry no. 593: 'Ich stelle -dēs, -dis \\\"ähnlich\\\" zu gr. δείκνυμι \\\"zeige\\\", δείκηλον \\\"Ebenbild\\\", skr. diś \\\"zeigen\\\", subst. diś \\\"Hinweis, Art und Weise\\\", zd. diś \\\"weisen\\\", osset. ... Also doch -dēs = zd. *daēsa-, auch wenn dies nicht mit daēsa- Yt 13,104 (\\\"Traumbild\\\"?) identisch ist.' This is precisely Nourai's arrow, and the cited page is exact.\"\n            },\n            {\n              \"ref\": \"BQT:912\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt leaf 370 (printed ≈ p.912; running offset printed ≈ leaf + 543). The page carries both headwords: 'دیز … رنگ و لون را گویند عموماً چنانکه اسب سیاه خسرو پرویز را شبدیز گویند … و رنگ سیاه را نیز گویند' and 'دیس … همتا و مانند و شبیه و نظیر باشد'. Moʿin's footnote: 'آقای پورداود نوشته‌اند: شاید «دیز» از کلمهٔ daēsa- باشد بمعنی نما و نشان، از مصدر daēs- اوستایی بمعنی نمودن و نشان دادن، که در کلمات: تندیس، فرخاردیس و طاقدیس آمده؛ بنابرین «شبدیز» لغةً بمعنی شب‌نما، و تبدیل سین بزاء در کلمهٔ اسپریس = اسپریز دیده می‌شود.' A second footnote on دیس cites 'هوبشمان' and the Manichaean Turfan form dēs and Sogdian δys- 'to build/form'. Nourai's gloss 'color, appearance, resemblance' and his three examples تندیس، طاقدیس، شبدیز are lifted straight from this page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"PHD_mackenzie.txt line 1977 (printed p.22); also p.81 s.v. uzdēs\",\n              \"stance\": \"supports\",\n              \"note\": \"'dēs(ag) [dys(k)| M dys] form, appearance.' and 'uzdēs [ʾwzdys | M ʾwzdys] idol.' — the Middle Persian stage Nourai's chart jumps over.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"NYB_vol2_glossary.txt, printed p.64 s.v. dēs\",\n              \"stance\": \"supports\",\n              \"note\": \"'dēs [dys] shape, form, v. zāyak-dēs. — MPrs dys; NP -dēs, e.g. māh-dēs \\\"moon-like\\\"; v. also uzdēs. From daēs-, v. dīstan.' Nyberg states Nourai's whole chain (Av. daēs- → MP dēs → NP -dēs) in one line.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"HRN.txt printed p.125, entry no. 593\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'-dēs, -dis, -des \\\"gleichend, ähnlich\\\". aw. darəs- \\\"Blick\\\" (Yt 19,94); ai. dṛś- \\\"das Sehen; sehend\\\", -dṛśa- \\\"-Aussehen; -sehend\\\". Der r-Vokal ist hier durch e vertreten ... Aw. daēsa- (Yt 13,104), das Darmesteter als \\\"Traum\\\" nimmt, ist zu unsicher, um verglichen werden zu können.' Horn puts the word under *derḱ- 'to see', not *deiḱ-; Hübschmann's no. 593 (the page Nourai cites) is the rebuttal, and later scholarship followed Hübschmann.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"BRT.txt col. 673 s.v. daēsa-\",\n              \"stance\": \"supports\",\n              \"note\": \"'daēsa- m. \\\"Zeichen, Omen\\\" ... Zum V. daēs-, — ai. deśa- m. \\\"Gegend\\\"; np. butdēs \\\"Götzenbild\\\", np. -dēs \\\"ähnlich\\\"; s. dazu HORN GIrPh. I b. 35.' Bartholomae explicitly attaches New Persian -dēs 'ähnlich' to the Avestan noun.\"\n            },\n            {\n              \"src\": \"SOD\",\n              \"where\": \"SOD.txt lines 32461-32467, δys- / δyst-\",\n              \"stance\": \"supports\",\n              \"note\": \"Gharib's Sogdian dictionary has δys- (δysd'r-, δyst-) 'to build, form', the Sogdian cognate that Moʿin's Borhān footnote also cites — an independent East Iranian witness for the *daiš- 'shape' family.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"incoming/ARY/ARY_pages.txt, grep 'دیس'\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian has no headword دیس / تندیس (the hits are all in پردیس/اودیسه and running text); it offers no independent check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"taikjan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *taikjaną 'to show' (whence OE tǣcan, OHG zeigōn) is Watkins' reconstruction word for word, and it does go back to *deyḱ- — but strictly to its voiced-velar doublet: AHD files it under 'I. Variant *deig-. 1. O-grade form *doig- in: a. Germanic *taikjan, to show, in Old English tǣcan, to show, instruct: TEACH'. Pokorny p.189 says the same: 'Daneben idg. doig- in got. taikns f. \\\"Zeichen, Wunder\\\", ahd. zeihhan, ags. tǣcan, engl. teach \\\"lehren\\\", got. taiknjan \\\"zeigen\\\"'. Phonetically: PIE *doiǵ- > Gmc *taik- by Grimm's law (*d > t, *ǵ > k), then the causative/denominative suffix *-janą gives *taikjaną 'to cause to show'. The book's spelling 'taikjan' (without the reconstructed nasal ending) is Watkins' 1975 notation, not an error.\",\n          \"derivation_fa\": \"صورت ژرمنی آغازین *taikjaną «نشان دادن» (که انگلیسی کهن tǣcan و آلمانی کهن zeigōn از آن است) دقیقاً همان است که واتکینز در پیوست فرهنگ American Heritage بازسازی کرده و نورایی از او گرفته است. تنها نکتهٔ فنی این است که این صورت نه از خودِ *deyḱ- بلکه از گونهٔ واکدارِ آن، *deiǵ-، می‌آید: پوکورنی در ص ۱۸۹ می‌نویسد «در کنار آن هندواروپایی doig- در گوتی taikns «نشانه» و انگلیسی کهن tǣcan». دگرگونی آوایی منظم است: بنا بر قانون گریم، *d هندواروپایی در ژرمنی به t و *ǵ به k بدل می‌شود، و سپس پسوند سببی ‎*-janą‎ افزوده شده است. پس ادعای نورایی درست است، با این تصحیح که این شاخه از گونهٔ *deiǵ- است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 360 s.v. deik-: 'I. Variant *deig-. 1. O-grade form *doig- in: a. Germanic *taikjan, to show, in Old English tǣcan, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tācen, tācn, sign, mark: TOKEN ...'. Nourai's node reproduces the form and the gloss exactly; his only omission is the label 'Variant *deig-'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"POK_01.txt leaf 197, p.189\",\n              \"stance\": \"supports\",\n              \"note\": \"'Daneben idg. doig- in got. taikns f. \\\"Zeichen, Wunder\\\"; taikn n. ds., ahd. zeihhan n. \\\"Zeichen\\\", ags. tǣcan, engl. teach \\\"lehren\\\", anord. teikna \\\"zeigen, bedeuten, bezeichnen\\\", ahd. zeihhonōn \\\"zeichnen\\\", got. taiknjan \\\"zeigen\\\".'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 244 (pp. 444-446) s.v. diction; leaf 836 (p.1578) s.v. teach\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. teach: 'ME. techen, fr. OE. tǣcan, \\\"to show, teach\\\", rel. to OE. tācen, tācn, \\\"sign, token\\\" ... fr. I.-E. base *deik-, *dik-, \\\"to show\\\", whence also OI. diśáti, \\\"shows\\\", Gk. δεικνύναι, L. dicere.' Klein does not separate a *deig- variant, treating both under *deik-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"teach, token, toe\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the three are exactly right, the third is misplaced on the tree. TEACH < ME techen < OE tǣcan 'to show, instruct' < Gmc *taikjaną — the node's own parent — and TOKEN < ME token < OE tācn 'sign, mark' < Gmc *taiknan; both belong to the *deig- branch and both are Watkins' and Klein's examples. TOE, however, does not come from *taikjaną at all: OE tā, tāhe goes back to Gmc *taihwō, which AHD files under a different sub-branch ('II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihwō in Old English tā, tāhe, toe: TOE') and hedges with 'possibly'. Pokorny p.189 gives the same form with the same reservation ('Hierher vermutlich mit der Bed. \\\"Finger\\\" (= \\\"*Zeiger\\\") und sekundär ... \\\"Zehe\\\", ahd. zēha, ags. tāhe, tā, anord. tā \\\"Zehe\\\" (*dóikuā)'), and Ernout-Meillet reject the whole 'finger/toe' link (see node 5). So the node is right for teach and token, over-reaching for toe: the arrow should have come off the root box, not off taikjan, and even then the derivation is only 'probable'.\",\n          \"derivation_fa\": \"از سه واژهٔ این گره دو تا بی‌گمان درست است و یکی جای نادرست نشسته. teach از انگلیسی میانه techen و انگلیسی کهن tǣcan «نشان دادن، آموختن» است و token از انگلیسی کهن tācn «نشانه»؛ هر دو از همان *taikjaną / *taiknan ژرمنی که نورایی به‌درستی پدرشان گذاشته است. ولی toe از این ستاک نمی‌آید: انگلیسی کهن tā / tāhe بازماندهٔ *taihwō ژرمنی است و واتکینز آن را زیر شاخهٔ دیگری («صورت پایه *deik-، درجهٔ o یعنی *doik-») و آن هم با قید «شاید» می‌آورد؛ پوکورنی نیز در ص ۱۸۹ همین احتیاط را دارد («احتمالاً به معنی انگشت [= نشان‌دهنده] و سپس انگشت پا»). پس در این گره ادعای نورایی دربارهٔ teach و token درست است، ولی toe باید از خودِ جعبهٔ ریشه پیکان می‌گرفت، نه از taikjan، و آن هم با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives this node no reference of its own; it inherits 'AHD' from its parent node 3, and AHD is checked there (it lists TEACH and TOKEN under Germanic *taikjan/*taiknam but TOE separately under *doik- > *taihwō).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 836 (p.1578) s.v. teach; leaf 861 s.v. token; leaf 245 (p.447) s.v. digit\",\n              \"stance\": \"partial\",\n              \"note\": \"teach and token are put under 'I.-E. base *deik-' (quoted at node 3); but toe is reached only through digit: 'digit ... L. digitus, \\\"finger, toe\\\", prob. dissimilated fr. orig. *dic-itus, prop. \\\"pointer\\\", fr. I.-E. base *deik-, \\\"to show\\\", whence also OE. tāhe, tā, \\\"toe\\\". See diction and cp. toe.' — i.e. Klein too keeps toe off the taikjan branch, and hedges it with 'prob.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt printed p.520 s.v. Token (and 'Teach; see Token')\",\n              \"stance\": \"supports\",\n              \"note\": \"'Token. (E.) ... AS. tācn. — A.S. tǣcan ... to point out, to accuse, criminate. + Du. teeken, teikn, Dan. tegn, Swed. tecken, Goth. taikn. All from [base] ... to point out. See Diction.' Skeat groups teach with token, as Nourai does.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"POK_01.txt leaf 197, p.189\",\n              \"stance\": \"partial\",\n              \"note\": \"'Hierher vermutlich mit der Bed. \\\"Finger\\\" (= \\\"*Zeiger\\\") und sekundär, aber bereits alt \\\"Zehe\\\", ahd. zēha, ags. tāhe, tā, anord. tā \\\"Zehe\\\" (*dóikuā)' — 'vermutlich', and via a different formation from taikjan.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"digitus; dîcere; index; jŭdex\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four Latin words are textbook reflexes of *deyḱ-; the fourth is contested. dīcere 'to say' < *deik-e/o- is the Italic specialisation of 'point out' into 'point out with words' (Oscan deikum, Umbrian teitu/deitu 'dicito', perfect dīxī = an s-aorist beside Gk. ἔδειξα); index, gen. indicis 'forefinger, informer, index' is in- 'toward' + the agent stem *-dik-, and jūdex 'judge' is *yowes-dik-s 'one who points out the law' (jūs + dic-), both of which Klein, Pokorny and Watkins give in exactly Nourai's glosses ('index \\\"Anzeiger, Angeber; Zeigefinger\\\", iūdex \\\"der das Recht Weisende\\\"' — Pokorny p.188). digitus 'finger' is the doubtful one. Pokorny and Klein derive it from *dic-itus 'pointer' by dissimilation of the two voiceless stops (Klein: 'prob. dissimilated fr. orig. *dic-itus, prop. \\\"pointer\\\"'), which is what licenses Nourai's gloss 'pointer, finger'; but Ernout-Meillet, Dictionnaire étymologique de la langue latine s.v. digitus, reject it outright: 'Aucun rapprochement net. Comme il n'y a pas de nom indo-européen commun du \\\"doigt\\\", digitus doit être une forme populaire sur laquelle il n'est possible de faire que des hypothèses vagues.' De Vaan likewise leaves it unexplained. So the node should read: dīcere, index, jūdex confirmed; digitus a plausible but disputed member.\",\n          \"derivation_fa\": \"از چهار واژهٔ لاتینی این گره سه تا بی‌چون‌وچرا از ریشهٔ *deyḱ- است و یکی محل اختلاف. dīcere «گفتن» تخصیص معنایی همان «نشان دادن» است به «با سخن نشان دادن» (اسکی deikum، اومبریایی teitu «بگو»، ماضی dīxī برابر ἔδειξα یونانی). index «انگشت اشاره، نمایاننده» از پیشوند in- و ستاک فاعلی ‎*-dik-‎ است و jūdex «داور» از *yowes-dik-s یعنی «آنکه داد را می‌نماید» (jūs «داد» + dic-)؛ پوکورنی در ص ۱۸۸ هر دو را با همین معنی می‌آورد. اما digitus «انگشت» چنین روشن نیست: پوکورنی و کلاین آن را از *dic-itus «نشان‌دهنده» با ناهمگونی دو همخوان بی‌واک می‌گیرند (و همین است پایهٔ معنایی که نورایی نوشته: «نشانگر، انگشت»)، ولی ارنو و مِیه در «فرهنگ ریشه‌شناسی زبان لاتین» آن را یکسره رد می‌کنند: «هیچ پیوند روشنی نیست … digitus باید صورتی عامیانه باشد که دربارهٔ آن جز فرض‌های مبهم نمی‌توان کرد». پس ادعای نورایی دربارهٔ dīcere و index و jūdex درست، و دربارهٔ digitus با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 360 s.v. deik-: '2. Latin digitus, finger (< \\\"pointer,\\\" \\\"indicator\\\"): DIGIT ... II.2. Basic form *deik- in Latin dicere, to say, tell: DICTATE ... 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jūdex (< *yewes-dik-), judge, \\\"one who shows or pronounces the law\\\" (jūs, law; see yewes-): JUDGE'. All four of Nourai's Latin words and all four of his glosses come from this sentence.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"POK_01.txt leaf 197, pp.188-189\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. dīcere \\\"sagen\\\", dīcāre \\\"feierlich verkünden\\\" ... indicāre \\\"anzeigen\\\", index \\\"Anzeiger, Angeber; Zeigefinger\\\" (wie auch ai. deśinī \\\"Zeigefinger\\\"), iudex \\\"der das Recht Weisende\\\"' and, on p.189, 'das wohl aus *dicitus durch Dissimilation gegen das tonlose t entstandene lat. digitus \\\"Finger, Zehe\\\"'.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"LAT.txt s.v. digitus (p.314) and s.v. dico (pp.307-308)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"On dico Ernout-Meillet agree with the root ('Le verbe qui signifie \\\"montrer\\\" dans les autres langues s'est spécialisé en latin ... dans le sens de \\\"montrer, faire connaître par la parole, dire\\\"'; 'ius dicere ... cf. iudex'). On digitus they refuse the connection: 'Aucun rapprochement net ... digitus doit être une forme populaire sur laquelle il n'est possible de faire que des hypothèses vagues. Le groupe germanique de v.h.a. zēha \\\"doigt de pied\\\" est différent de toutes manières.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 244 (pp.444-446) s.v. diction; leaf 245 (p.447) s.v. digit; leaf 450 (p.834) s.v. judge\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. diction: 'fr. I.-E. base *deik-, *dik-, \\\"to show, point out\\\", whence also L. digitus, \\\"finger\\\" (lit. \\\"pointer\\\"), the second element in L. jū-dex, \\\"judge\\\" (lit. \\\"he who shows or teaches justice\\\"), in-dex, \\\"forefinger, index\\\" (lit. \\\"pointer\\\")'; s.v. judge: 'fr. L. judicem, acc. of judex, \\\"judge\\\", which stands for *jous-dik-s and orig. meant \\\"one who shows right\\\", fr. jus, \\\"right\\\", and the stem of dicere.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through node with no word printed: it stands for the French forms that carried the Latin dic- family into Persian, i.e. dictée (feminine past participle of dicter, itself from Latin dictāre, frequentative of dīcere) and dictateur (from Latin dictātor, agent noun of dictāre, the Roman magistrate 'so called', Varro says, 'quia dicitur'). Both are learned Latinisms re-formed in French rather than inherited popular words, which is why they keep the Latin ct. The step Latin → French is uncontroversial; Nourai leaves the node empty because his interest is only in the Persian loans two boxes down.\",\n          \"derivation_fa\": \"این گره جعبه‌ای گذرا و بی‌واژه است و تنها نمایندهٔ صورت‌های فرانسوی است که خانوادهٔ لاتینی dic- را به فارسی رسانده‌اند: dictée (اسم‌مفعول مؤنث فعل dicter از dictāre لاتینی، مکررساز dīcere) و dictateur (از dictātor لاتینی، اسم فاعل همان فعل، لقب فرمانروای روم). هر دو وام‌واژهٔ کتابی از لاتین‌اند نه بازماندهٔ عامیانه، و به همین سبب خوشهٔ ct لاتینی را نگاه داشته‌اند. پیوند لاتین ← فرانسه در اینجا هیچ اختلافی ندارد؛ نورایی جعبه را خالی گذاشته چون مقصودش تنها وام‌واژه‌های فارسیِ دو جعبه پایین‌تر است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/دیکته/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book; the Latin → French step is covered by the parent node's AHD citation and by Klein s.v. dictate (consulted below).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 244 (pp.444-446), s.vv. dictate, dictator\",\n              \"stance\": \"supports\",\n              \"note\": \"'dictate ... L. dictātus, pp. of dictāre, \\\"to say often, pronounce repeatedly, dictate (for writing)\\\", freq. of dicere (pp. dictus), \\\"to say\\\". See diction'; 'dictator, n. — L. dictātor, fr. dictātus, pp. of dictāre.' The French dictée/dictateur are the same two Latin bases.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"LAT.txt s.v. dico, p.308\",\n              \"stance\": \"supports\",\n              \"note\": \"'dictator ab eo appellatur quia dicitur' (Cic. Rep. 1,40,63, quoted by Ernout-Meillet), with the note that dictātor and dictātūra 'forment un groupe de sens indépendant' from dictāre — a nuance worth keeping, since Persian dīktātor comes through the political term, dīkteh through the schoolroom one.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"dîkteh; dîktâtor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are 19th-20th century French loans, taken in through the Dār al-Fonūn school system and the press, not inherited words. دیکته dīkteh is French dictée 'dictation exercise' — Moʿin's dictionary tags it '[فر.]' (French) and defines it 'مطلبی که کسی بخواند و دیگری بنویسد' ('what one person reads out and another writes down'), the schoolroom sense, and the final -e of the French feminine participle is rendered by Persian ـه, exactly as in کمیته komite (comité), ژنده-type spellings and دوجین. دیکتاتور dīktātor is French dictateur, with the -eur ending replaced by the Latinising -ātor shape common in Persian political borrowings of the Reza Shah era (compare امپراتور emperātor). Neither word passed through Arabic. Nourai's 'MON' citation is apt: Moʿin's foreign-word volume is where such loans are tagged.\",\n          \"derivation_fa\": \"هر دو واژه وام‌واژه‌ای نو از فرانسه‌اند که در سدهٔ سیزدهم و چهاردهم خورشیدی از راه دارالفنون و مطبوعات وارد فارسی شده‌اند، نه واژه‌هایی موروثی. «دیکته» از dictée فرانسوی «املا» است؛ معین آن را با نشانهٔ «[فر.]» می‌آورد و چنین معنی می‌کند: «مطلبی که کسی بخواند و دیگری بنویسد» — یعنی همان معنای آموزشگاهی. «ـه» پایانی فارسی برابرِ ‎-ée‎ فرانسوی است، مانند «کمیته» از comité. «دیکتاتور» از dictateur فرانسوی است، با این تفاوت که پایانهٔ ‎-eur‎ به الگوی لاتینی‌مآبِ ‎-ātor‎ بدل شده، همان الگویی که در «امپراتور» هم دیده می‌شود. هیچ‌یک از راه عربی نیامده‌اند. ارجاع نورایی به معین بجاست، چون جلد وام‌واژه‌های فرهنگ معین همین‌گونه واژه‌ها را نشان‌گذاری می‌کند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/دیکته/\",\n            \"https://abadis.ir/fatofa/دیکتاتور/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin's Farhang-e Fārsi, consulted through abadis.ir (the فرهنگ معین section, since the print volume's page numbers cannot be mapped online): دیکته '(تِ) [فر.] (اِ.) مطلبی که کسی بخواند و دیگری بنویسد' — the tag [فر.] is Moʿin's abbreviation for فرانسه. دیکتاتور is tagged the same way. Nourai cites 'MON' without a page; the tag is exactly what he is relying on.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab/abadis rendering of فرهنگ معین s.v. دیکته, دیکتاتور\",\n              \"stance\": \"supports\",\n              \"note\": \"'[فر.]' origin tag on both entries; دیکتاتور glossed as the absolute ruler, i.e. the political Latin term via French, not an Arabic or Turkish mediation.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 244 (pp.444-446) s.v. dictate/dictator\",\n              \"stance\": \"supports\",\n              \"note\": \"Confirms the ultimate Latin etyma dictāre/dictātor behind French dictée/dictateur, i.e. the chain Latin → French → Persian that the chart draws.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"digit, dictate, index, judge\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are Latin words taken into English, three of them through French. DIGIT is Latin digitus borrowed directly in the late 14th c. (Chaucer, of the numerals 0-9, from counting on the fingers). DICTATE is Latin dictātum/dictātus, pp. of dictāre, a 16th-c. learned borrowing. INDEX is Latin index 'forefinger, pointer', taken over unchanged in the 16th c. and specialised to the alphabetical list. JUDGE is the one popular transmission: Latin jūdicem (acc. of jūdex) > Old French juge > ME juge, with the verb from OF jugier < L. jūdicāre. Klein s.v. diction lists digit, index, judge and dictate together as members of the *deik- family, exactly as Nourai groups them; the only word here whose ultimate root membership is questioned is digit (see node 5).\",\n          \"derivation_fa\": \"هر چهار واژه از لاتین به انگلیسی رفته‌اند، سه تا از راه فرانسه. digit همان digitus لاتینی است که در پایان سدهٔ چهاردهم میلادی مستقیم وام گرفته شد و به معنی رقم‌های ۰ تا ۹ به کار رفت، چون شمارش با انگشتان بوده است. dictate از dictātum لاتینی وامی کتابی در سدهٔ شانزدهم است. index همان index لاتینی «انگشت اشاره» است که بی‌تغییر گرفته شد و سپس معنی «فهرست الفبایی» یافت. judge تنها واژهٔ این گره است که راه عامیانه پیموده: jūdicem لاتینی ← juge فرانسوی کهن ← juge انگلیسی میانه. کلاین نیز در مدخل diction همین چهار واژه را در خانوادهٔ *deik- کنار هم می‌آورد. تنها واژه‌ای که عضویتش در این ریشه محل تردید است digit است (نگاه کنید به گرهٔ ۵). ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference is printed on this node; it inherits 'AHD' from node 5, where Watkins lists DIGIT, DICTATE, INDEX, INDICATE and JUDGE among the English descendants of deik-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 244 (pp.444-446) s.v. diction; leaf 450 (p.834) s.v. judge; leaf 422 (p.786) s.v. index\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. index: 'L. index, gen. indicis, \\\"a pointer, indicator; the forefinger; sign, mark ...\\\", rel. to indicāre, \\\"to point out, show\\\"'; s.v. judge: 'ME. juge, fr. OF. (= F.) juge, fr. L. judicem, acc. of judex ... orig. meant \\\"one who shows right\\\"'. Klein's diction entry names abdicate, dictate, digit, index, judge among the cognates.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt printed p.119 s.v. Digit; p.223 'Index, Indicate; see Diction'; p.232 s.v. Judge\",\n              \"stance\": \"partial\",\n              \"note\": \"'Index, Indicate; see Diction' and 'Judge. (F.-L.) F. juge — L. acc. of iudex, a judge, lit. \\\"one who points out law\\\". — L. ius, law ... See Jury and Diction' support the node; but Skeat's Digit entry takes a different route — 'Digit, a finger, figure. (L.) L. digitus, a finger ... + Gk. δάκτυλος ... (√DAK, to take (Curtius))' — i.e. he links digitus with Greek daktylos, not with deik-, a further sign that digit is the shaky member.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Greek\",\n          \"words\": \"dikein\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek δικεῖν 'to throw, cast' (aorist infinitive; no present is attested) is real and its gloss is Watkins' — AHD: '6. Zero-grade form *dik- in Greek dikein, to throw (< \\\"to direct an object\\\"): DISK'. But this is the least secure link in the whole chart. Pokorny's deik- entry (p.188) lists δείκνυμι, δεῖξις, δίκη, δίκαιος, δικάζω — and does NOT list δικεῖν 'to throw'. Cheung's Etymological Dictionary of the Iranian Verb sets up a separate root '*daiš² ? \\\"to throw\\\"' (Khotanese diś- 'to throw') and records under it: 'Tichy 1979 compared the Khot. form to Gr. ἔδικον \\\"I threw\\\", yielding an IE root *deik- \\\"to throw\\\", homonymous with IE *deik- \\\"to show, point out\\\". The equation is semantically difficult to prove ... this putative root *deik- \\\"to throw\\\" leaves so little or no unambiguous traces', and marks it 'Pok.: —'. Watkins bridges the two senses with 'to direct an object', which is a plausible reading of the same semantic range that gave Latin dīcere 'say' and δίκη 'judgement' (Cheung makes the same suggestion, comparing English 'throw in / out of court'), but it is an interpretation, not a demonstrated derivation. Verdict: acceptable as Watkins' view, not established.\",\n          \"derivation_fa\": \"فعل یونانی δικεῖν «انداختن، پرتاب کردن» (تنها مصدر آاوریست آن به‌جا مانده و صورت حالِ آن ثبت نشده) واژه‌ای واقعی است و معنایی که نورایی نوشته همان معنای واتکینز است: «درجهٔ صفرِ *dik- در یونانی dikein، انداختن (< «چیزی را به سویی راندن»)». ولی این سست‌ترین حلقهٔ کل نمودار است. پوکورنی در مدخل deik- (ص ۱۸۸) δείκνυμι و δεῖξις و δίκη و δίκαιος را می‌آورد اما δικεῖν «انداختن» را نمی‌آورد. چونگ در «فرهنگ ریشه‌شناسی فعل ایرانی» ریشه‌ای جداگانه به نام «*daiš² ؟ انداختن» می‌گذارد (بر پایهٔ diś- ختنی) و می‌نویسد که تیشی (۱۹۷۹) آن را با ἔδικον یونانی سنجیده و ریشه‌ای *deik- «انداختن» هم‌آوا با *deik- «نمودن» فرض کرده، ولی «این برابری از نظر معنایی به‌دشواری اثبات‌پذیر است» و در پوکورنی نشانی از آن نیست. پیوندی که واتکینز میان دو معنی می‌زند («چیزی را به سویی راندن») تفسیری پذیرفتنی است — چونگ هم همین را با اصطلاح انگلیسی «to throw out of court» پیشنهاد می‌کند — اما اثبات‌شده نیست. پس ادعای نورایی در این گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/δίσκος\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 360 s.v. deik-: '6. Zero-grade form *dik- in Greek dikein, to throw (< \\\"to direct an object\\\"): DISK.' Nourai's node — form, gloss and the parenthetical 'to direct an object' — is a verbatim copy of this. The reference does say what the arrow says; the question is whether the reference is right.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"POK_01.txt leaf 197, p.188\",\n              \"stance\": \"silent\",\n              \"note\": \"The Greek section of Pokorny's deik- reads 'gr. δείκνυμι, sekundär δεικνύω \\\"zeige\\\", kret. προ-δείκνυτι, δεῖξις \\\"das Zur-Schau-Stellen\\\", δίκη s. oben, δίκαιος, δικάζω, δεῖγμα \\\"Beweis, Beispiel\\\"' — δικεῖν 'to throw' does not appear at all, so the page Nourai cites for the root does not support this branch.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"CHEUNG.txt lines 4467-4487, root *daiš² '?to throw'\",\n              \"stance\": \"partial\",\n              \"note\": \"'*daiš² ? \\\"to throw\\\". KHOTANESE: LKh. diś- \\\"to throw\\\" ... Tichy 1979 ... compared the Khot. form to Gr. ἔδικον \\\"I threw\\\", yielding an IE root *deik- \\\"to throw\\\", homonymous with IE *deik- \\\"to show, point out\\\". The equation is semantically difficult to prove though ... «PIE? > LIV: 109 | Pok.: —'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 251 (≈p.461) s.v. dish\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. δίσκος, \\\"quoit, disk\\\", which is dissimilated fr. *δίκ-σκος and prop. means \\\"that which is thrown\\\", from the stem of δικεῖν, \\\"to throw, cast\\\", whence also δίκτυον, \\\"net\\\".' Klein takes the δικεῖν etymology as established (as did all pre-Beekes handbooks).\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Another empty pass-through box, standing for French disque, the immediate source of Persian دیسک. Two corrections to the arrow as drawn. First, French disque did not come from Greek directly: it is a 16th-century learned borrowing of Latin discus (Rabelais uses it of the quoit), and Latin discus is itself the borrowing from Greek δίσκος — so the chart silently skips the Latin stage, which Klein's own entries (dish, discus, dais, desk) all route through Latin. Second, the Greek word's own derivation from δικεῖν is now doubted: Wiktionary, following Furnée and Beekes, notes that 'the traditional derivation from *δίκ-σκος, from δικεῖν (\\\"to cast\\\")' fails because 'the suffix -σκο- is rare in nominal derivation', and proposes instead a Pre-Greek *δισκ-. Klein's page 459-461, which Nourai cites, gives the older view. The French-from-Latin-from-Greek chain is certain; only the attachment of δίσκος to δικεῖν, and hence to this root, is uncertain.\",\n          \"derivation_fa\": \"این هم جعبه‌ای گذرا و بی‌واژه است و نمایندهٔ disque فرانسوی، خاستگاه بی‌واسطهٔ «دیسک» فارسی. دو تصحیح بر پیکانی که نورایی کشیده است. نخست آنکه disque فرانسوی یکراست از یونانی نیامده: وامی کتابی از discus لاتینی در سدهٔ شانزدهم میلادی است و خودِ discus لاتینی وام‌واژه‌ای از δίσκος یونانی است؛ پس نمودار مرحلهٔ لاتینی را نادیده گرفته، حال آنکه کلاین در مدخل‌های dish و discus و dais و desk همه را از راه لاتین می‌برد. دوم آنکه ریشه‌شناسی خودِ δίσκος از δικεῖν امروز مورد تردید است: به گزارش ویکی‌واژه بر پایهٔ فورنه و بیکس، اشتقاق سنتی از *δίκ-σκος پذیرفتنی نیست چون «پسوند ‎-σκο-‎ در اسم‌سازی بسیار کمیاب است» و به جای آن صورتی پیش‌یونانی *δισκ- پیشنهاد می‌شود. صفحهٔ ۴۵۹ تا ۴۶۱ کلاین که نورایی به آن ارجاع می‌دهد دیدگاه کهن‌تر را دارد. زنجیرهٔ یونانی ← لاتین ← فرانسه قطعی است؛ تنها پیوند δίσκος با δικεῖν و در نتیجه با این ریشه است که تردیدپذیر است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/δίσκος\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:459\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 251, whose printed pages are ≈460-461 (verified from the running numerals: leaf 238 carries '434 435', and the leaves advance two printed pages each) — i.e. Nourai's p.459 is within the scan's ±2 drift. s.v. dish: 'fr. L. discus, \\\"quoit\\\", in Late L. \\\"dish\\\" (so called because of its shape), fr. Gk. δίσκος, \\\"quoit, disk\\\", which is dissimilated fr. *δίκ-σκος and prop. means \\\"that which is thrown\\\", from the stem of δικεῖν, \\\"to throw, cast\\\". Cp. dais, desk, disc, discus.' Klein supports the Greek → Latin → Romance chain, but routes it through Latin, which the chart's arrow omits.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 219 (≈p.414) s.v. dais; leaf 238 (p.434) s.v. desk\",\n              \"stance\": \"partial\",\n              \"note\": \"'dais ... fr. OF. deis, dois, \\\"table; platform\\\" (whence F. dais, \\\"canopy\\\"), fr. VL. discus, \\\"table\\\", fr. L. discus, \\\"quoit, dish, disc\\\"' — the French words of this family are shown coming from Latin, never straight from Greek.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt printed p.119, s.v. Disc (with dais, desk, dish subsumed)\",\n              \"stance\": \"supports\",\n              \"note\": \"'... — Gk. δίσκος, a [quoit] ... [from] δικεῖν, to cast, throw'; then 'dais ... O.F. deis, dais, a high table. — L. discus, a quoit, platter; in late L., a table. — Gk. δίσκος (above)' and 'desk ... M.E. deske, a variant of dish or disc — L. discus, a disc (above).' Skeat, like Klein, inserts Latin between Greek and French/English.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"دیسک\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"دیسک dīsk is a modern French loan: Moʿin's dictionary tags it '[فر.]' and glosses it 'هر نوع صفحهٔ گرد و تخت آهنین' ('any round flat metal plate'), then the athletics discus, the intervertebral disc and the computer disk. The Persian form takes French disque with the final -que rendered by ک and no vowel added — the ordinary treatment of French final -que in Persian borrowings (compare بوتیک, چک). The word entered Persian in the 20th century in three separate waves (sport, medicine, computing), which is why Moʿin's entry has four numbered senses. It has nothing to do with the native دیس/دیز of node 2, despite the accidental similarity: this one is a European word, that one is Iranian. The book prints only the Persian script here, with no transliteration — that is what the printed page shows, so the JSON's null 'translit' is faithful.\",\n          \"derivation_fa\": \"«دیسک» وام‌واژه‌ای نو از فرانسه است. معین آن را با نشانهٔ «[فر.]» می‌آورد و نخستین معنایش را «هر نوع صفحهٔ گرد و تخت آهنین» می‌نویسد و سپس معناهای ورزشی (پرتاب دیسک)، پزشکی (صفحهٔ غضروفی میان مهره‌ها) و رایانه‌ای را برمی‌شمارد. صورت فارسی از disque فرانسوی گرفته شده و خوشهٔ ‎-que‎ پایانی بی‌افزودن واکه به «ک» بدل شده است، همان‌گونه که در «بوتیک» و «چک» می‌بینیم. این واژه در سدهٔ چهاردهم خورشیدی و در سه موج جداگانه (ورزش، پزشکی، رایانه) وارد فارسی شده و از همین روست که مدخل معین چهار معنی شماره‌دار دارد. با «دیس/دیز» ایرانیِ گرهٔ ۲ هیچ پیوندی ندارد و همانندی‌شان تصادفی است. ادعای نورایی در این گره درست است. (در متن کتاب برای این جعبه تنها صورت فارسی چاپ شده و آوانویسی لاتین ندارد؛ پس نبودِ آوانویسی در داده‌ها خطای استخراج نیست.)\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/دیسک/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin's Farhang-e Fārsi via abadis.ir (فرهنگ معین section): دیسک '[فر.]' + '۱- هر نوع صفحهٔ گرد و تخت آهنین ۲- صفحه‌ای گرد و غضروفی در میان مهره‌ها ... ۳- نوعی صفحهٔ گرد با وزنی حدود دو کیلوگرم که در ورزش پرتاب دیسک از آن استفاده می‌کنند ۴- حافظهٔ جانبی کامپیوتر'. The [فر.] tag is exactly the claim Nourai's arrow makes.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir rendering of فرهنگ معین s.v. دیسک\",\n              \"stance\": \"supports\",\n              \"note\": \"Origin tag [فر.] = French; no Arabic or Turkish intermediary is recorded.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 251 (≈p.461) s.v. discus/dish\",\n              \"stance\": \"supports\",\n              \"note\": \"Supplies the stage behind the French word: 'discus, n., a disk. — L., fr. Gk. δίσκος, \\\"quoit, disk\\\". See disk.' — i.e. Persian دیسک is at four removes (Greek > Latin > French > Persian).\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"disc, desk, discuss\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three belong here (with the reservation of nodes 9-10); the third does not belong at all. DISC/DISK is Latin discus < Gk. δίσκος, borrowed into English in the 17th c. DESK is ME deske < Medieval Latin desca 'a desk, table', itself Latin discus in its Late Latin sense 'table' (Klein, s.v. desk: 'ME. deske, fr. ML. desca, \\\"a desk, table\\\", fr. L. discus, \\\"a quoit, a disk; a table\\\". See dish and cp. dais, disk.'), so disc/desk/dish/dais are a set of doublets, which is why Nourai's two Klein pages (433 ≈ desk at p.434, 459 ≈ disk/dish at pp.460-461) are the right ones. DISCUSS, however, has nothing to do with *deyḱ-: it is Latin discussus, pp. of discutere 'to shake apart, shatter, disperse', from dis- 'apart' + quatere 'to shake' (Klein, on the very page Nourai cites, spells this out; Watkins files DISCUSS under kwēt-, not deik-; Etymonline: 'from dis- \\\"apart\\\" + quatere \\\"to shake\\\" ... \\\"to dash to pieces, agitate, strike or shake apart\\\"'). The English initial dis- is a pure homograph. This is a straightforward error in the book, and it is Nourai's own, not AHD's — Watkins lists only DISK under deik-.\",\n          \"derivation_fa\": \"از سه واژهٔ این گره دو تا (با همان احتیاطی که در گره‌های ۹ و ۱۰ گفته شد) در جای خود نشسته‌اند و سومی یکسره بیگانه است. disc/disk از discus لاتینی و آن از δίσκος یونانی است و در سدهٔ هفدهم میلادی وارد انگلیسی شده. desk از deske انگلیسی میانه و آن از desca در لاتین سده‌های میانه است که خود همان discus لاتینی در معنای متأخرِ «میز» است؛ کلاین می‌نویسد: «desk از desca لاتینی میانه «میز تحریر»، از discus لاتینی «قرص؛ میز»؛ نگاه کنید به dish و بسنجید با dais و disk». پس disc و desk و dish و dais چهار صورت دوگانهٔ یک واژه‌اند و همین است که دو ارجاع نورایی به کلاین (۴۳۳ ≈ desk در ص ۴۳۴ و ۴۵۹ ≈ disk/dish در ص ۴۶۰-۴۶۱) درست است. اما discuss هیچ پیوندی با *deyḱ- ندارد: از discussus لاتینی، اسم مفعول discutere «از هم پاشاندن، تکان دادن»، مرکب از dis- «جدا» و quatere «تکان دادن» است؛ کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد همین را می‌گوید و واتکینز نیز DISCUSS را زیر ریشهٔ kwēt- می‌آورد نه deik-. همانندی dis- آغازین تنها هم‌نویسگی است. پژوهش امروزی این جزء نمودار را رد می‌کند، و این خطا از خودِ نورایی است نه از منبعش، زیرا واتکینز زیر deik- فقط DISK را آورده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/discuss\",\n            \"https://en.wiktionary.org/wiki/δίσκος\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:433\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 238, whose printed numerals are '434 435'; the desk entry stands at the head of that leaf, i.e. p.434 (Nourai's 433 is one off, within the scan's drift): 'desk, n. — ME. deske, fr. ML. desca, \\\"a desk, table\\\", fr. L. discus, \\\"a quoit, a disk; a table\\\". See dish and cp. dais, disk.'\"\n            },\n            {\n              \"ref\": \"KLN:459\",\n              \"status\": \"contradicts\",\n              \"note\": \"KLN_1966.txt leaf 251 (printed ≈460-461) carries both the entry that supports 'disc' and the entry that refutes 'discuss', side by side: 'discus, n., a disk. — L., fr. Gk. δίσκος, \\\"quoit, disk\\\". See disk.' and immediately after it 'discuss, tr. and intr. v. — L. discussus, pp. of discutere, \\\"to shake violently, shatter, dash to pieces, scatter, disperse\\\", in Late L. \\\"to discuss\\\", fr. dis- and quatere, \\\"to shake, wield, brandish, strike, shatter\\\". See quash, \\\"to annul\\\".' The reference Nourai cites explicitly denies the derivation he draws for discuss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt, index lines 1429 and 360\",\n              \"stance\": \"contradicts\",\n              \"note\": \"The English index gives 'DISK deik-' but 'DISCUSS kwēt-'; the deik- entry itself lists only 'DISK' from the dikein branch. Nourai's own principal source therefore excludes discuss from this root.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt printed p.121, 'Discuss: see Quash'; p.119 s.v. Disc/desk/dish\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Skeat cross-refers discuss to Quash (i.e. Latin quatere), and keeps dais/desk/dish under Disc — the same split as Klein and Watkins.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt leaf 251 (≈p.461) s.v. dish\",\n              \"stance\": \"partial\",\n              \"note\": \"'Cp. dais, desk, disc, discus and the second element in oldish [sic, OCR]. Cp. also Dictynidae, Dictynna, dictyo-.' Klein groups disc and desk as Nourai does, and nowhere mentions discuss in that list.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T17:46:25.755Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-112.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T17:46:29.689Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-112.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 112"
}
```


### [2026-09-05T17:46:31.874Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 6, 'plausible': 5, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'not_checked': 3, 'contradicts': 1}
books consulted: {'supports': 20, 'silent': 3, 'contradicts': 4, 'partial': 6} | by book: {'KLN': 10, 'POK': 4, 'SKT': 4, 'BRT': 2, 'CHEUNG': 2, 'AHD': 2, 'LAT': 2, 'MON': 2, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'SOD': 1, 'ARY': 1}
```


## [2026-09-05T17:46:40.224Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%AF%DB%8C%D8%B3' --note 'page 112, node 2: Persian tandis = tan + -dis suffix' && python3 - <<'EOF'\nimport json,urllib.parse\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')]\nhave={urllib.parse.unquote(e.get('url','')) for e in idx}\nsrc=set()\nd=json.load(open('data/verification/page-112.json',encoding='utf-8'))\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources':\n                src.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for i in o: walk(i)\nwalk(d)\nfor s in sorted(src):\n    print('OK ' if urllib.parse.unquote(s) in have else 'MISSING ', s)\nEOF"
}
```


### [2026-09-05T17:46:42.414Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/adda4ba2532cf872.txt
OK  https://abadis.ir/fatofa/دیسک/
OK  https://abadis.ir/fatofa/دیکتاتور/
OK  https://abadis.ir/fatofa/دیکته/
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-
OK  https://en.wiktionary.org/wiki/δίσκος
OK  https://en.wiktionary.org/wiki/تندیس
OK  https://www.etymonline.com/word/discuss
```


## [2026-09-05T17:47:00.876Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-112.json` written; `python3 tools/verify_check.py 112` reports **0 PROBLEM lines** (12/12 nodes verified).

**Page 112 (book p.82) — root Deik (entry 1 "Deiw" is a redirect, skipped)**

Verdicts: root 1 confirmed · nodes 6 confirmed, 5 plausible, 1 disputed.
Ref checks: 10 supports, 1 contradicts, 3 not_checked (nodes the book gives no refs for). 13 different books consulted.

- **disputed — #12 English "disc, desk, discuss" (KLN:433,459):** *discuss* is not from *deyḱ-. It is L. *discussus* < *discutere* = *dis-* + *quatere* "to shake" — stated on the very Klein page Nourai cites (KLN_1966 leaf 251, ≈p.461), and Watkins indexes DISCUSS under *kwēt-*, DISK under *deik-*. Nourai's own error, not AHD's. *disc* and *desk* are fine.
- Plausible-with-caveats: **#9 Greek dikein** (Pokorny p.188 does *not* list δικεῖν; Cheung/Tichy posit a homonymous root, "Pok.: —"); **#10 French** (chart draws Greek→French, skipping Latin *discus*; Furnée/Beekes now call δίσκος Pre-Greek); **#5 Latin** (*digitus* rejected by Ernout-Meillet: "aucun rapprochement net"); **#4 English** (*toe* is Gmc *\*taihwō*, not from *taikjan*, and only "possibly" from the root).
- **#2 Persian dīs/dīz — the Iranian core is solid.** HUB:65 (no. 593) and BQT:912 (Moʿin's footnote quoting Pūrdāvūd) are both exact and both say what the arrow says; Bartholomae col. 673, Nyberg II p.64 ("NP -dēs … From daēs-") and MacKenzie p.22 (*dēs(ag)* "form, appearance") confirm Av. daēs- → MP dēs → NP -dīs. Marked *plausible* only because (a) the "color" sense of دیز rests on Pūrdāvūd's «شاید» plus an ad-hoc s > z, and (b) Horn no. 593 (p.125) derives -dēs from *dṛś-* "see" instead — a dispute the chart hides; modern scholarship sides with Hübschmann, i.e. with Nourai.

**No extraction errors.** I rendered PDF p.112 (copied to `data/verification/sources/refs/ocr/BOOK/112.png`) and the JSON is faithful, including node #11's Persian-only «دیسک» with no transliteration. One cosmetic detail only: the book prints the bound forms with leading hyphens, «ـ دیس ، ـ دیز», which the JSON records as "دیس ، دیز" — worth keeping if the data is ever used to show that these are suffixal.
