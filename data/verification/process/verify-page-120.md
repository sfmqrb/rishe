# Verification process log — verify-page-120


## [2026-09-05T18:02:59.957Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 120 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-120.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-120.json. Write /home/sfmqrb/git/rishe/data/verification/page-120.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 120` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:03:01.560Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:03:02.221Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:03:02.239Z] TOOL RESULT

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


## [2026-09-05T18:03:02.361Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-120.txt"
}
```


### [2026-09-05T18:03:02.385Z] TOOL RESULT

```
1	=== PDF page 120 (book page 90) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Der 2, Deru 2 : to run  (refs POK:205)
4	#1 (parent #0) [Avestan] refs=POK:205 | draonah : travel goods
5	  #2 (parent #1) [Persian] refs=HRN:274; BQT:844 ? | darŭn «درون ۱» : a Zoroastrian prayer
6	#3 (parent #0) [Germanic] refs=AHD | tred : to step
7	  #4 (parent #3) [English] refs=None | tread, trade, trap, trip
8	#5 (parent #0) [Greek] refs=AHD | dromos : a course, path
9	  #6 (parent #5) [English] refs=None | -drome, syndrome
10	--- entry 1 ---
11	ROOT [Indo-European] Derk : to see  (refs POK:218)
12	#1 (parent #0) [Greek] refs=KLN:480,1574 | drakoon : a serpent with devil eyes
13	  #2 (parent #1) [Arabic] refs=KLN:1554; TAD:49 | tarxŭn : an aromatic bushy plant
14	    #3 (parent #2) [Persian] refs=MON | tarxŭn «ترخون» : tarragon
15	    #4 (parent #2) [Greek] refs=KLN:1574 | tarxŭn
16	      #5 (parent #4) [Latin] refs=None | 
17	        #6 (parent #5) [English] refs=None | tarragon : an aromatic herb
18	  #7 (parent #1) [Latin] refs=AHD; KLN:480 | dracŭ, dracŭnem : dragon
19	    #8 (parent #7) [French] refs=None | 
20	      #9 (parent #8) [English] refs=None | dragon
21	--- entry 2 ---
22	ROOT Derô -> redirect to Der 1
23	
```


## [2026-09-05T18:03:05.577Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-120.json",
 "description": "Read page 120 source JSON"
}
```


### [2026-09-05T18:03:05.617Z] TOOL RESULT

```
{
  "pdf_page": 120,
  "book_page": 90,
  "entries": [
    {
      "root": {
        "name": "Der 2, Deru 2",
        "lang": "Indo-European",
        "refs": "POK:205",
        "gloss": "to run"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:205",
          "words": [
            {"translit": "draonah", "gloss": "travel goods", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:274; BQT:844 ?",
          "words": [
            {"translit": "darŭn", "gloss": "a Zoroastrian prayer", "script": "درون ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tred", "gloss": "to step", "script": null}
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
            {"translit": "tread, trade, trap, trip", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "dromos", "gloss": "a course, path", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "-drome, syndrome", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Derk",
        "lang": "Indo-European",
        "refs": "POK:218",
        "gloss": "to see"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:480,1574",
          "words": [
            {"translit": "drakoon", "gloss": "a serpent with devil eyes", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:1554; TAD:49",
          "words": [
            {"translit": "tarxŭn", "gloss": "an aromatic bushy plant", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "tarxŭn", "gloss": "tarragon", "script": "ترخون"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Greek",
          "refs": "KLN:1574",
          "words": [
            {"translit": "tarxŭn", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "tarragon", "gloss": "an aromatic herb", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD; KLN:480",
          "words": [
            {"translit": "dracŭ, dracŭnem", "gloss": "dragon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dragon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Derô",
        "redirect": "Der 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T18:03:05.876Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:03:05.916Z] TOOL RESULT

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


## [2026-09-05T18:03:14.079Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','HRN','BQT','MON','TAD','WLD','BRT','IEC','SYN','SKT','LEW','LAT','PHD','NYB','HUB','ARY','FSD','WEB','LKT','PLA','AFM','FVQ','DEV','PHN','AFA','ARB','HJB','RCH','CHEUNG','IRN','SIN','AKD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-05T18:03:15.762Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
CHEUNG null
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://
```


## [2026-09-05T18:03:20.012Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AHD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T18:03:21.785Z] TOOL RESULT

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
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
```


## [2026-09-05T18:03:25.538Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: der\" POK_full.txt | head -40; echo ---; grep -n \"lemma: dre\" POK_full.txt | head -20"
}
```


### [2026-09-05T18:03:25.608Z] TOOL RESULT

```
18198:Root / lemma: der(ep)- 
18204:The Root/ lemma: der(ep)-\ "to see, *mirror' derived from Root/ lemma: deii(-\ "to look'. 
18216:Root / lemma: dera-, dra- 
18239:Root / lemma: dergh- 
18323:Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 
18343:Clearly Root/ lemma: der-1{. dor-, deT-) or dor-, dor-: "hand span' derived through Root/ 
18349:derived from truncated ghesor. The source of Root / lemma: der-1 {. dor-, der-) or dor-: 
18377:meaning two hands. That means both Root/ lemma: der-1 {. dor-, der-) or dor-, dor-: 
18476:Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
18538:Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru- 
18770:Root / lemma: der-, heavy basis dera-, dre- 
18776:Root / lemma: der-, heavy basis dera-, dre- : "to cut, split, skin (*the tree)' derived from 
18778:Root /lemma: deru- doru-, dr(e)u-, drou-, dreuQ-: dru-\ tree' 
19134:derived from Root / lemma: der/c-: 'to look, light'; gr. SspKopai ' look, keep the eyes open, 
37187:Clearly Root / lemma: der-1{. dor-, der-) or dor-, dor-: "hand span' derived through Root/ 
---
23555:Root / lemma: dregh- 
23577:Root/ lemma: tr-eu-d-\ "to press, push, * displeasure' derived from Root/ lemma: dregh-: 
23587:Root / lemma: dre- : dra-, extended dr-em- 
87449:Root/ lemma: tr-eu-d-\ 'to press, push, * displeasure' derived from Root/ lemma: dregh-:
```


## [2026-09-05T18:03:27.690Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23587,23640p' POK_full.txt; echo \"=== dera-,dra-\"; sed -n '18216,18245p' POK_full.txt"
}
```


### [2026-09-05T18:03:27.767Z] TOOL RESULT

```
Root / lemma: dre- : dra-, extended dr-em- 

Meaning: to sleep 

Material: Old Indie drati, draya-ti, -/e "asleep", n/'-dra 's\eep'] in addition zero grade ni-drita- 

/7 'sleeping, dozed off; 

Armenian tartam^s\o\N, sleepy ' {*der-d-, Pedersen KZ. 39, 416); 

gr. horn. Aor. sSpaGov ( *e-dr-6^-om), new sSapGov " slept ', secondary KaraSapGavu) " 
dozed off '; 

Latin dorm/d's\eep, drowse ' {*drm-Tid)\ 

Slavic *dremjd^ drowse ' in Church Slavic dremlju drematT drowse ', serb. dr'ijemljem 
drijemati^ have sleep desire ', etc 

maybe alb. drem/t^ drowse'. 

About the formal Verhaltnisse s. EM. 284, to -e/77- extension also Pedersen Groupement 
22. 

References: WP. I 821, WH. I 372, Trautmann 60. 
Page(s): 226 



Root / lemma: dumb- {-b^ ?) 
Meaning: penis, tail 

Material: Avestan duma-m. "tail', npers. dum, dumb {* durr{h)ma-). Old High German 
zi//77yC>/c» "penis'. Middle High German zumpf{e), zumpfelTn {Su\.\.er\\v\ IF. 4, 93); in addition 
perhaps Avestan dumna-v\. "hand (?)' {*dumbna-), s. Scheftelowitz IF. 33, 142 with 
numerous parallels for the meaning-development " shaft, pole, staff- penis, tail' and "staff - 
arm, hand'. Probably to Middle Low German t/mpe^cusp, peak, acme, apex ', Old English 
a///77p//5/7 "provide with nails', nasal, form from Germanic *f/ppa't\p, tail' in engl. //p"cusp, 
peak'. Middle High German z/'p^e/); Germanic *tuppa-'p'\g\.a'\\' in Old Norse topprds., Old 
English topprw. "acme, apex'. Middle High German zo/?rplait, tress', with bb. Middle Low 
German tobbe, tubbe 'sp'\go\.\ compare Latvian duba ' assigned sheaf; Germanic *tappan 
"spigot' in Old English taeppaxu. (engl. tap). Middle Low German tappem.. Old High 
German zapho. Middle High German zapfem. apparently "popular saying' with intensive 



consonant increase, nasalization and vowel change a: i: u, compare above S. 221 drop-. 

drip-: drup-. 

References: WP. I 816, Pick III 155, 164, 168, Petersson Heterokl. 70 f. 

See also: see also above S. 177. 

Page(s): 227 
=== dera-,dra-
Root / lemma: dera-, dra- 

Meaning: to work 

Material: Gr. 5pau) (*5paiu)) "make, do', Konj. 5p(I), Aeolic 3. PI. 5paiai, Aor. Attic sSpaaa, 

hom. Spnorrip "worker, servant', Spaija "action', 5pavo(; spyov, npa^K; . . . 5uvapii(; Hes., 

aSpavrjc; "inactive, ineffective, weak'; 

Maybe alb. nasalized form nder{*der-) "hang loose'; 

hom. oAiyoSpavsojv "make only less powerful, fainting, unconscious'; hom. and Ionian (see 

Bechtel Lexil. 104) 5paivu) "do'; 

Lithuanian dar{i)a~u, daryti, Latvian darft^6o, make'; in spite of MiJhlenbach-Endzelin s. 
V. dar?tr\otto Lithuanian dereti^ be usable', Latvian deref arrange, employ, engage' etc, 
because the meaning deviates too strongly. 

References: WP. I 803, Specht KZ. 62, 110, SchwyzerGr. Gr. I 675^, 694. 
Page(s):212 

Root / lemma: dergh- 



Meaning: to grasp 

Material: Armenian trcak^ brushwood bundle ' (probably from *turc-ak, *turc- kom *c/orgh-
```


## [2026-09-05T18:03:36.915Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 20[3-9]\" POK_full.txt | head -20; echo ===; grep -n \"lemma: drem\\|lemma: dr-em\\|dreu-2\\|lemma: dreu\" POK_full.txt|head"
}
```


### [2026-09-05T18:03:36.975Z] TOOL RESULT

```
Exit code 1
18152:Page(s): 203 
18383:Page(s): 203 
18413:Page(s): 203-204 
18536:Page(s): 204-206 
19224:Page(s): 206-211 
(eval):1: == not found
```


## [2026-09-05T18:03:38.532Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18413,18540p' POK_full.txt"
}
```


### [2026-09-05T18:03:38.599Z] TOOL RESULT

```
Page(s): 203-204 

Root / lemma: {der-3), dra-, dreb- drem-, dreu- 
Meaning: to run 
Material: dra- 

Old Indie drati^ runs, hurries ', Intens. daridratT wanders around, is poor ', dari-dra-^ 
wandering, beggarly '; 

gr. ano-5i5paaKU) " run away ', Put. 5paao|jai, Aor. sSpav; 5paafj6(;, Ionian 5pr|a|j6(; 
"escape', a5pC(aT0(; "striving not to escape', 5pc(n£Tr|<; " fugitive ', SpansTSuu) " run away, 
splits, separates from' (compare to -n- Old Indie Kaus. drapayati^ brings to run ', Aor. 
ao'/ioV-ayoa/ [uncovered] "runs'); 

Old High German zittarom {*di-dra-mi) "tremble (*ready to flee)'. Old Icelandic titra 
"tremble, wink' (originally perhaps " walk on tiptoe; trip, wriggle restlessly '); 

perhaps here Slavic *dropy^ bustard ' (Machek ZslPh. 17, 260), poln. Czech drop, older 
drop{i)a etc, out of it Middle High German trap(pe), trapgans. 

dreb-: 

Lithuanian drebu, -e// "tremble, quiver'; 



poln. (etc) drabina'\a66ef; 

Old English treppan {* trapjan) "tread', Middle Low German Dutch frappen ' stomp' , ndd. 
trippen. Modern High German (Low German) trappe/n, trippein. Middle High German (Low 
German) treppe, trappei.. Modern High German Treppe, Old English traeppei. 'trap', 
Modern High German Trappei, East Frisian trappe, trap'trap, splint, staircase, stairs '; 

through emphatic nasalization, as in Modern High German patschen - pantschen, ficken 
- fiencken{see W. Wissmann Nom. Postverb. 160 ff., ZdA. 76, 1 ff.) to define: 

Gothic ana-tr/mpan' approach, beset'. Middle Low German trampen' stomp'. Middle 
High German (ndd.) trampe/n ^ appear crude' , engl. tramp, trample^ tread'. Middle High 
German trumpfen^ rur\, toddle'. 

drem-: 

Old Indie dramati' running ', Intens. dandramyate^ runs to and fro '; 

gr. Aor. sSpapov, Perf. 5£5popa "run', 5p6iJO(; "run'; 

Old English trem, trym^ Fufttapfe ', Old Norse //'a/77/' "fiend, demon' (see above). Middle 
High German fremen'\Na\/er', Danish tr/m/e'roW, fall, tumble', Swedish Dialectal trumlads.. 
Middle High German trame^ rung of a leader, stairs'; 

here probably Modern High German FIN £'/'a/77/77e(Gottingen), Z7/'(9/77se (Magdeburg), 
from *DromJa ar\d *Dromisa {probab\)/ North lllyrian), in addition poln. (Illyrian) Drama 
(Silesia), Bulgarian Dramatica {thrak.); s. VasmerZslPh. 5, 367, Pokorny UrillyrierS, 37, 
127; 

Maybe alb. dromce 'p'\ece, chip (of a blow)' 

insecure is Woods KZ. 45, 62 apposition of serb o'/777a//" shake', dfmnut/" upset, allow to 
shake ', sloven, drmaf/" shake, jiggle', dram/t/" jiggle from the sleep ', drampaf/" ungentle 
jiggle '; 

maybe alb. d rem it ^s\eep', derrmonj^ exhaust, tire, destroy' Slavic loanwords. 

Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
derived Root/ lemma: {der-3), dra-, drab- dram-, drau-\ "to run'. 



Czech drmlatr flit, stir; move tlie lips, as if one sucking', drmolitr take short steps ' (these 
in the good suitable meaning; 'shake' from " stumble with the foot '?), drmotiti^chai, prate' 
(probably crossing of meaning with the onomatopoeic word root der-der-2, see there). 

o^re:/- (partly with J as zero grade, probably because of *dreua'<-), FIN (participle) 
dr(o)u(u)enff/iff. 

Old Indie dravati^ runs, also melts ', FIN DravantT, o^m/a- "hurrying', Avestan dravaya- 
"run' (being from daevischen), draoman-v\. 'attack, onrush', aesmd-drOi{a)- " calling from 
Aesma, sends to attack ' (very doubtful Old Indie dravina-m, dravinas-v\. "blessing, 
fortune', Avestan draonah-v\. ' bei der Besitzverteilung zufallendes Gut, Vermogensanteil ' 
perhaps as "traveling fortune'?); 

Illyrian-Pannonian FIN Dravos {* drouos), out of it serbokr. Drava, compare apoln. 
Drawa {\\\yr\an loanword); Indo Germanic *drouent- ^\r\urry\ng' > lllyrian *drauent-{: above 
Old Indie Dravanti), out of it dial. *trauent- in FIN TpasvT- (Bruttium) > Italian Trionta, Indo 
Germanic *druuent-, lllyrian *druent- in poln. FIN DrwQca, Modern High German Drewenz, 
Italian *truent-\n FIN 77Y/e/7/^s(Picenum); 

maybe alb. {*druent-) Dr/nosrWer name "hurrying water?' common alb. nt > n. 

gall. FIN (from North lllyrian?) Druenf/a {French la Drance, Drouance, Durance, Swiss/a 
Dranse); *Drutos, French le Drot, Druta, French la Droude; 

Lithuanian sea name *Druv-lntas {wruss. Drywiaty); Old Prussian stream, brook Drawe. 

Auf dreu-, participle *dru-to-base6 on perhaps (see Osthoff Par. I 372 f. Anm.) Gothic 
trudan^ tread', Old Norse troda, trad 6s.; Old English tredan. Old High German tretan 
"tread' (by Osthoffs outlook of ablaut neologism). Old High German trata "tread, spoor, 
way, alley, drift, trailing'. Old Saxon trada'iread, spoor'. Old English trodr\., trodui. "spoor, 
way, alley' (engl. trade'trade' is nord. loanword). Old High German trofa. Middle High 
German trottei. " wine-press ', Intens. Old High German trotton 'tread'; Modern High 
German dial, trottein " go slowly '. 

Here also Germanic root *tru-s- in East Frisian trusein '\urc\\, stumble, go uncertainly or 
staggering ', truser dizziness, giddiness ', Dutch treuzelen' to be slow, dawdle, loiter', 
westfal. trusein, truesein' roll slowly ', Middle High German trollen {*truzldn) "move in short 
steps constantly'. Modern High German trollen, Swedish Dialectal trdsalela\ry demon, 
ghost', Norwegian Dialectal trusar\6\ot, fool', trusk' despondent and stupid person'; 



Maybe through metathesis alb. {*trusal) trullos, trains' xwake the head dizzy', //^y 'brain' 

as well as (as *truzla-) Old Norse troll v\. "fiend, demon'. Middle High German trol, trollevn. 
"fairy demon, ghost, fool, uncouth person' (compare unser Trampel\(\ same meaning; the 
Wandals called the Goths TpouAou(;, Loewe AfdA. 27, 107); it stands in same the way 
besides Germanic tre-m-{see below) Old Norse //'a/77/' "fiend, demon'. 

In Germanic furthermore with /-vocalism Middle Low German trTseIn, westfal. triasein 
"roll, lurch', holl.//'///e'/7 "tremble' (from which Italian trIllare'quWer, trill hit') etc against 
association of Old Indie dravatl\N\Vr\ Avestan dvara/tr goes' see below "^^eu-, '^^euer- 
"flee'. 

References: WP. I 795 ff., Krahe IF. 58, 151 f.. Feist 45. 
Page(s): 204-206 

Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru- 

Meaning: tree
```


## [2026-09-05T18:03:59.705Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: der/c\\|lemma: derk\\|lemma: der-k\" POK_full.txt | head; echo \"---pages 213-220\"; grep -n \"Page(s): 21[2-9]\" POK_full.txt | head -20"
}
```


### [2026-09-05T18:03:59.774Z] TOOL RESULT

```
19134:derived from Root / lemma: der/c-: 'to look, light'; gr. SspKopai ' look, keep the eyes open, 
---pages 213-220
18262:Page(s): 212-213 
18768:Page(s): 214-217 
19358:Page(s): 217-218 
19416:Page(s): 218-219 
19476:Page(s): 219-220
```


## [2026-09-05T18:04:01.511Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19340,19430p' POK_full.txt"
}
```


### [2026-09-05T18:04:01.566Z] TOOL RESULT

```
The cause of -(e)s- stem seems to belong to: Old Indie dosa, new dosa-h ' evening, 
darkness ', Avestan daosatara-, daosastara-^ situated towards evening, to the west ', 
npers. o'ds "the former yesterday night'; 

gr. bz\zKoc, (more properly bz\zKb(;) "evening' (metr. lengthening for *bzzKoc, from 
SsuoEAoq? originally Adj. " vespertine ', as still in hom. SsisAov npap); gr. 5uu) (Attic u:, ep. 
u), trans. " sink, dive, swathe ' (only in compounds: KaraSuu) "sink'), intrans. (in simplex 
only in participle 5uu)v; Aor. £5uv) "dive in, penetrate (e.g. aiOspa, zc, novTOv), slip in, pull 
in (clothing, weapons; so also £v5uu), ano5uu), nspiSuu)), sets (from the sun and stars, 
dive, actually, in the sea)', also med. 5uopai and Suvw (hom. 5ua£T0 is old augment tense 
to the future, Schwyzer Gr. Gr. 1 788); aAip5uu), Kallimachos "sink in the sea' (p unclear, 
s. Boisacq s. v.; preposition *[5]/0[c»]?); 5unTU) "dip, dive, sink' (after punru)); aSuTOv " the 
place where one may not enter ', 5uaic; " disappearing, dive, nook, hideaway, setting of the 
sun and stars ', np6(; nAiouSuaiv " towards evening ', 5ua|jai PI. " setting of the sun and 
stars '; unclear apcpi5upo(;, 5i5u|Joc; " coupled ' s. Schwyzer Gr. Gr. I 589; after Frisk Indog. 
16 f. here also 5uTr| "shrine'. 

References: WP. I 777 f., WH. I 3, 682. 
Page(s): 217-218 

Root/ lemma: {deu-2ox dou^ : du- 
Meaning: to worship; mighty 

Material: Old Indie duvas-x\. " offering, worship instruction ', duvasyati^ honors, reveres, 
recognizes, recompenses ', duvasyu-, o'^i/dyi/- "venerating, respectful '; Old Latin duenos, 
then duonos. Classical bonus'good' (Adv. bene, Demin. bellus{*duenelos] "pretty, cute'); 
Note: common Latin du- > im- 
probably = Old Irish o'e/? "proficient, strong', Subst. " protection'; Latin bed, -are^ to bless, 
enrich, make happy ', beatus^ blessed, lucky' {*du-ejd, participle *du-enos); in addition Old 
Saxon /M//7/7d/7 "grant'. Middle Low German twTden^ please, grant'. Old English langtwTdig^ 



granted long ago', Middle High German zmc/en' grant', md. getwed/c'tame, domesticated, 
compliant ' {* du-ei-to-; Wood Mod. Phil. 4, 499); 

after EM2 114 perhaps still here gr. Su-va-piai " has power '. 

Perhaps also here Germanic *faujan' make' (from "* be mighty ') in Gothic taujan, 
taw/da^ make', Proto Norse faw/dsl made'. Old High German zc»^^//^/7'exercebant 
(Cyclopes ferrum)'. Middle High German zouwen, zouwen^ finish, prepare ', Middle Low 
German /o^M/e/7 'prepare, concoct, tan, convert hide into leather', wherefore Old English 
getawa' an implement, utensils, tools, instruments ' (therefrom again {ge)taw/an ^ prepare' , 
engl. faw^ make ready, prepare, or dress (raw material) for use or further treatment; spec, 
make (hide) into leather without tannin ') and (with original prefix stress in nouns) Old 
English geatwei. PI. 'armament, armor, jewellery, weapons ' = Old Norse ggtvari. PI. ds.. 
Old Frisian touw, /on/ 'tool, rope, hawser'. Modern Frisian touw^ the short coarse fibres of 
flax or hemp, tow ', Middle Low German touwe^\.oo\, loom', touwe, tou^rope, hawser' (out 
of it Modern High German Tau), Old High German gizawa^ household furniture, apparatus 
' (but also 'succeed', see above). Middle High German gezduwer\. 'appliance' (out of it 
with Bavarian-dial, vocalization Middle High German zawe). Modern High German Gezahe 
(see about these forms Psilander KZ. 45, 281 f.). 

In addition with e (Psilander aaO. expounded also *taujan through proto Germanic 
abridgement from *t^wjan) perhaps Gothic /en/a 'order, row', gatewjan ^ 6\spose' , Old High 
German zawa^ coloring, paint, color, dyeing', langobard. zawa^ row, division of certain 
number, uniting'. Old English sel-tsewe^ altogether, wholly, entirely well, sound, whole, 
healthy, well ' (about possible origin of Germanic *tewairom *fej-wasee below *de/(- 
'take'; then it would be natural to separate from taujan); with oGothic fau/. Gen. foj/'s 
'action', ubiltojis^ evildoer, wrongdoer ', Old Norse tdr\. 'uncleaned wool or flax, linen 
thread material ' = Old English /on/ 'the spinning, the weaving' in tow-hOs^ spinnery ', tow- 
craefV skillfulness in spinning and weaving ', engl. tow^ the short coarse fibres of flax or 
hemp, tow '; with Asuffix Old Norse tdlr\. 'tool'. Old English tdlr\. ds. {*tdwula-), verbal only 
Old Norse Wja, /j^a 'utilize, make usable ', actually 'align', denominative to *tdwja-a^er 
Psilander aaO., while Falk-Torp seeks under /0/e therein belonging to Gothic tiuhan 
*tauhjan, *tiuhjan. 

Thurneysen places (KZ. 61, 253; 62, 273) Gothic taujan to Old Irish do'id^ exert, 
troubled '; the fact that this, however with do'id^ catches fire ' is identical and the meaning 
'make' has developed from ' kindle the fire, inflame', seems unlikely. 

About other interpretations of taujan s. Feist 474 f. 



References: WP. I 778, WH. 11 11 , 324 f., 852. 
Page(s): 218-219 



Root / lemma: deu-3, deua-, dua-, du- 
Meaning: to move forward, pass 

Material: Old Indie du-ra-h^ remote, distant, wide' (mostly locally, however, also 
chronologically), Avestan durae. Old pers. dura/y'aiar, far there ', Avestan duraf' at a 
distance, far, far there, far away ', compounds Sup. Old Indie davTyas-, dav/sfha-' more 
distant, most distant'; ved. duvas- " moving forward, striving out ', transitive Avestan duye' 
chase away ', avi-fra-5avaite " carry away itself (from water)'; Old Indie dOta-h, Avestan 
duta- " summoner, delegator'; perhaps here Old Indie dosa-hm. 'lack, fault, error' {*deu-s- 

o-y,
```


## [2026-09-05T18:04:06.999Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SspKopai\\|Root / lemma: der\" POK_full.txt | sed -n '1,40p'; echo \"=== search derk\"; awk '/Root ?\\/ ?lemma: der/{print NR\": \"$0}' POK_full.txt | head -20"
}
```


### [2026-09-05T18:04:08.783Z] TOOL RESULT

```
18198:Root / lemma: der(ep)- 
18216:Root / lemma: dera-, dra- 
18239:Root / lemma: dergh- 
18288:gr. SspKopai ' look, keep the eyes open, be alive', 5£5opKa, sSpoKov, bt^%\Q, 'vision' 
18323:Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 
18349:derived from truncated ghesor. The source of Root / lemma: der-1 {. dor-, der-) or dor-: 
18476:Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
18538:Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru- 
18770:Root / lemma: der-, heavy basis dera-, dre- 
18776:Root / lemma: der-, heavy basis dera-, dre- : "to cut, split, skin (*the tree)' derived from 
19134:derived from Root / lemma: der/c-: 'to look, light'; gr. SspKopai ' look, keep the eyes open, 
37187:Clearly Root / lemma: der-1{. dor-, der-) or dor-, dor-: "hand span' derived through Root/ 
42522:Gr. ^6p^, ^opKQc;, with folk etymology connection in SspKopai mostly 56p^, 5opK6(;; bopmq 
=== search derk
18198: Root / lemma: der(ep)- 
18204: The Root/ lemma: der(ep)-\ "to see, *mirror' derived from Root/ lemma: deii(-\ "to look'. 
18216: Root / lemma: dera-, dra- 
18239: Root / lemma: dergh- 
18323: Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 
18343: Clearly Root/ lemma: der-1{. dor-, deT-) or dor-, dor-: "hand span' derived through Root/ 
18349: derived from truncated ghesor. The source of Root / lemma: der-1 {. dor-, der-) or dor-: 
18377: meaning two hands. That means both Root/ lemma: der-1 {. dor-, der-) or dor-, dor-: 
18476: Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
18538: Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru- 
18770: Root / lemma: der-, heavy basis dera-, dre- 
18776: Root / lemma: der-, heavy basis dera-, dre- : "to cut, split, skin (*the tree)' derived from 
18778: Root /lemma: deru- doru-, dr(e)u-, drou-, dreuQ-: dru-\ tree' 
19134: derived from Root / lemma: der/c-: 'to look, light'; gr. SspKopai ' look, keep the eyes open, 
37187: Clearly Root / lemma: der-1{. dor-, der-) or dor-, dor-: "hand span' derived through Root/
```


## [2026-09-05T18:04:11.060Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18270,18325p' POK_full.txt"
}
```


### [2026-09-05T18:04:11.118Z] TOOL RESULT

```
cursive present other root 

Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 

shine, shimmer + zero grade of Root/ lemma: ok"-: to see; eye 

Material: Old Indie [present is pasyat/] Perf. dadarsa^have seen', Aor. adarsat, adraksTt 

{adrak), participle drsta-, kaus. darsayati^xx\ake see'; Avestan daras-^ behold ', Perf. 

dadarasa, participle darasta-. Old Indie dfs-i. 'sight', ahardrs-^ looking day ', upa-dfs-i. 

'sight', drst/'-t 'sight', Avestan aibTdarasti- 6s. (Gen. Sg. darstois). Old Indie darsata- 

'visible, respectable ', Avestan darasa-m. 'sight, gaze, look'; 

common Old Indie gh- > ks- 

gr. SspKopai ' look, keep the eyes open, be alive', 5£5opKa, sSpoKov, bt^%\Q, 'vision' 
(with a changed lengthened grade compared with Old Indie drsti-), 5£py|ja 'sight', 5£pYp6(; 
'look, gaze', 5ua-5£pK£TO(; 'heavy to behold' (= Old Indie dargata-), un65pa Adv. 'one 
looking up from below' (*-5paK = Old Indie drg-, or from *-5paK-T), SpoKOc; n. 'eye', 5paKU)v, 
-ovTO(; 'dragon, snake' (from banishing, paralyzing look), fem. 5paKaiva; 

alb. o'/vM 'light' (*£yM--/a); 



Note: 

Maybe alb. darke'supper, evening meal, evening' : o'/'e/re'dinner meal, midday' : Old Irish 
an-dracht' loathsome, dark'. 

after Bonfante (RIGI. 19, 174) here Umbrian terkantur' seen, discerned, perceived ' 
(that is to say ' shall be seen, discerned, perceived '); 

Old Irish [present ad-cTu] ad-con-darc'\r\ave seen' (etc, s. Pedersen KG. II 487 f.; 
present adrodarcar^ can be seen'), derc^eye', a/A-oV/r" illustrious', bret. ofe/r'/7 "sight', abret. 
e/r/e/r'evidentis', zero grade Irish drechi. {*drka) "face', cymr. drychm. {*drksos) "sight, 
mirror', cymr. drem, trem, bret. dremmlace' {*drk-sma). Old Irish an-drachV loathsome, 
dark' {an- neg. + *drecht= alb. drite); 

Gothic ga-tarhjan " make distinct ' (= Old Indie darsayati); Germanic *tor^a- "sight' (== 
Old Indie drs^ in Norwegian PN Target, Torghatten e\.c, Indo Germanic to- suffix in 
Germanic *turhta- : Old English torht. Old Saxon toroht. Old High German zoraht, newer 
zo///"bright, distinct'. 

References: WP. I 806 f. 

See also: Perhaps with derfepj- {above S. 212) remote, distant related. 

Page(s):213 

Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 

Meaning: hand span, *hands
```


## [2026-09-05T18:04:30.373Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['HRN','HUB','BRT','PHD','NYB','MON','BQT']:\n  x=d[k]; print(k, x.get('page_offset'), '||', x.get('lookup_hint'))\n  print()\n\""
}
```


### [2026-09-05T18:04:32.178Z] TOOL RESULT

```
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

MON None || Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). || grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-05T18:04:36.909Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 295 (p.274)\"; awk 'BEGIN{RS=\"\\f\"} NR==296' HRN.txt | head -60"
}
```


### [2026-09-05T18:04:38.584Z] TOOL RESULT

```
=== HRN leaf 295 (p.274)
verdrängt. Desshalb scheint mir arm. dav *Nach-
stellung, Hinterlist, Verrat', davem nachstellen', dav-
acan *Nachsteller (Hübschmann, No. 80) nicht aus
dem Persischen entlehnt zu sein.
74. flrün bezw. drfm der Pärsen.
aw. draonah- 'Opferbrot'; ai. vergl. drdvim-j drä-
vinaS' Gut, Besitz'.
np. drün soll, abgesehen von dem pärsischen 1. 1.,
auch ein *Getreidemass' bezeichnen, d. h. so viel als
zu einem Opferkuchen nötig ist; doch ist diese Be-
deutung nicht belegt.
75. dürös *den Tod fernhaltend' (Haoma).
aw. düraosa- 'den Tod fernhaltend', Geld n er 'un-
antastbar' *), Bart hol omae (mir nicht wahrscheinlich)
'weithin leuchtend*.
76. dusäkäs unwissend', dtisükäslh (Men.).
Hier könnten noch eine ganze Reihe mit dus- ge-
bildeter Composita, die im Neupersischen aufgegeben
worden sind, aufgeführt werden; z. B. dtisden (aw.
duzdaena-), dtisdänäk (aw. duMäo), dmgand (Men.,
aw. duzgainti') u. v. a. m. Im Pehlevi erscheint nur
die Form dus-, nicht auch duz-, wie das Päzend noch
daneben hat. Np. duzhü/t, diShü/t etc. (z. B. Sahn. I,
52 Vers 341; 119 Vers 998) ist bloss päzendische
Umschreibung.
E.
77. enik 'Antlitz (PPGl.).
aw. ainika- 'Antlitz'; ai. dmka-,
78. erayf gottlos'.
nnDI^N gottlos' (Is. 58, 4), ^:^n5l^N 'Gottlosigkeit'
(Is. 58, 6) sind Pärsenworte, die im Sadder u. dgl.
auch vorkommen.
*j Y. 82, 14 überfletzt er Mieilig* (KZ. 28, 258 j.
```


## [2026-09-05T18:04:44.803Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT draonah\"; grep -n \"draonah\\|draonaŋh\\|draonah-\" BRT.txt | head -20; echo \"=== PHD dron\"; grep -n \"^dro\\|^drōn\\|dron \" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T18:04:44.880Z] TOOL RESULT

```
=== BRT draonah
3288:•  j.  a-Jiäityö-draonah-  Adj.  'der  nicht die  gehörige  Nahrung,  Kost  hat':  dahmS niuruzdö  (sd.)  'nä  N.  77;  —  *gai-sstryaca vansna  *v»r3zyantö  .  .  'nauhasca  *hmtö N.52.
9407:s^aniraiahe  Vr. /o.  i.  '•  j.  *^kasu.draonah- "  Adj.   'der  geringe
13323:daityö.draonah-
13341:•  j.  dÜtyö.draonah-  Adj.  'der  die  ge- hörige Nahrung,  Kost  hat';  ilai  "ailaya fracarmti  kirisas^a  gaositisca  ..°nar?has^a haiitS  ^.53.
14040:•  j.,  g.  draonah-  n.  'bei  der  Besitzver- teilung zufallendes  Gut,  Vennögens(usw.)- anteil,  Teil"':  data  vi  amtnihscä  utayBitl ^ fsd.)  haurvatas  'ns  Y._j_j.  8;  —  vup»n  ^ avat  aipi  'nS  iaiat  (sd.)  a^aurunalca  .  ,[ Yt/p.  8;  —  US  mf  pita  haomai  -nS  frir»- riaot  (sd.)  .  .  Aaauharfru  .  .  yö  mam  tat 'rts  sinai  (sd.)  .  .  yat  mi  da%at  akurS  Y. li.4,i.\  —  ya  tal yat  kaemahe  'nS  nigä- tahanti  *mMiiaitHsd.)  Y.  /o,  1 5 ;  —  /a^wärü *nd  fraianntarUi  Vd."/0;  io,4;  —  mit Gen.:  ^wä/pm  a  gJus  ß-a^wansS (ßA.)  .  . Aaomai   'tis  Y.  //.  7.         a)  'Vennögens-
14045:*)    Das   mp.  Ritualwort  drSn  wird  als  gelW. dem  Aw.  draonah-  entsprechen;  aber  seine  Be- deutung 'Opferbrot'   (vgl.  Dst.  ZA.  /.  Lxv)   ist im  Awesta  -  Vd.  zählt  nicht  mit  -  nicht  zu  be- legen.   Wahrscheinlich    sind   die   in  Y.  //  be- nannten FleischopferitQcke  späterhin  durch  Brote ersetit  worden. KompE.  —  ai.  drivinas-  n.  'Gut,  Geld';  mp. drS»,  t.*).  -    Pü.  ™>,    erl.  (lu  Y.  33):  mizd. (zu  Y.  ro,  II.  7);  drön.  —  1)  Wo  daraon'.  — ')  Nach  der  a-DekL  —  Si  Die  Stelle  ist   aus dem  Zusammenhang  gerissen,  ihr  Sinn  daher nicht   sicher   zu    ermitteln.     Mir  tcbeinl,   es handelt   sich   um   die  Herabmiitdcnlng   einer Leibessirafe  unter  der  Vo raussei tung.  dass  der Geschädigle  vom  Verurteilten  eine  pekuniäre sahne  erhält.    Ändert  Gdn.  KZ.  25. 305,  Dst. ZA.  2.  74.
24295:•  j.  vtrö.draonah-  Adj.  '(der  die  Nahrung der  Männer  ha^  d.  i.)  der  die  selbe  Nahrung wie  die  Männer  hat,  seine  Nahrung  von den  (speisenden)  Männern  abbekommt', vom  Hund:  späntm  däkfm  . .  'nar^Aim gafhanqm  harihrai  V.  7^.  39.
=== PHD dron
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:1175:cauldron dēg.
PHD.txt:1699:drop passing, paššinjag, srešk.
PHD_mackenzie.txt:2065:dro [KDBA < A kdb); d1wb' I M drw, (N daro,,)] lie, deceit.
PHD_mackenzie.txt:2066:drod [SRM < A f1m; d1wt l I M drwd, N darod] health, well-being,
PHD_mackenzie.txt:2068:dro-dadwarih [KDBA d'twblyh] false judgement.
PHD_mackenzie.txt:2069:Idron [dlwn l I N daruna] bow.
PHD_mackenzie.txt:2070:2dron [d1wn I N darun] consecrated bread, ceremony in which c.b. is
PHD_mackenzie.txt:2073:dron yaAtan                                               duA-~ihr
PHD_mackenzie.txt:2075:dron yaAtan: consecrate the sacrificial bread.
PHD_mackenzie.txt:2076:droA [dlwl] mark, branding; punishment.
PHD_mackenzie.txt:2078:droAidan, dros- [dlwl-ytn ] brand.
PHD_mackenzie.txt:2080:drosom [dlwlwm] mark.
PHD_mackenzie.txt:2081:droz-,v. druxtan.
PHD_mackenzie.txt:2082:drozan [dlwcn l 1M, J drwzn] lying, liar.
PHD_mackenzie.txt:6173:cauldron deg.                           child aburnay(ag), frazand, rahig,
PHD_mackenzie.txt:9703:dro1                              ~,            karframan                \~~,
PHD_mackenzie.txt:9704:drodiidwarih      I
PHD_mackenzie.txt:10525:dro, 1-2graw
PHD_mackenzie.txt:10534:1-2dron                     ,,~    draz, grab                W,
```


## [2026-09-05T18:04:57.590Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('draonah-  n.')\nprint(repr(t[i-200:i+50]))\n# find leaf index\nleaf=t[:i].count('\\f')\nprint(\"leaf\",leaf)\nEOF"
}
```


### [2026-09-05T18:04:59.339Z] TOOL RESULT

```
"äky,  was  für  den  vorhandenen  Raum viel  M  viel  ist  Vgl  ludem  Rl,JRAS. /?.  vi, wonach  »  and  p  noch  zu  lesen  sind.\nj.  aiiä  draojytkt  N.  6g-.  lies  ae!ä.dräJaAytie.  I\n•  j.,  g.  draonah-  n.  'bei  der  Besitzver- teilung zufall"
leaf 440
```


## [2026-09-05T18:05:01.679Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==441' BRT.txt | head -8; echo \"...tail\"; awk 'BEGIN{RS=\"\\f\"} NR==441' BRT.txt | tail -5"
}
```


### [2026-09-05T18:05:03.966Z] TOOL RESULT

```
�  p.  Mraujiya-'*  den.  Praes.  31  'für Lüge,  erlogen  halten':  tyJ'  manä  kartam vamavatäm  %uväm  mätya!'  draujiyähy'^ "was  von  mir  getan  ist,  soll  dich  Über- zeugen, du  sollst  es  nicht  für  Lüge  halten" Bh.  4-  &■
Ableit.  aus  'drauja-  m.  'Lüge',  zum  V.  drang:
—  aL  'drekä-  m.,  mp.  dröi,  —  ■)  Anders  NA., s.  No.  1.  —  *)  Also  STa.  dunixlani  'iiaa-,  vgl. Bh.^.8.  NA.  ergänil  (milOppERT)  duruxlam maniyäky,  was  für  den  vorhandenen  Raum viel  M  viel  ist  Vgl  ludem  Rl,JRAS. /?.  vi, wonach  »  and  p  noch  zu  lesen  sind.
j.  aiiä  draojytkt  N.  6g-.  lies  ae!ä.dräJaAytie.  I
•  j.,  g.  draonah-  n.  'bei  der  Besitzver- teilung zufallendes  Gut,  Vennögens(usw.)- anteil,  Teil"':  data  vi  amtnihscä  utayBitl ^ fsd.)  haurvatas  'ns  Y._j_j.  8;  —  vup»n  ^ avat  aipi  'nS  iaiat  (sd.)  a^aurunalca  .  ,[ Yt/p.  8;  —  US  mf  pita  haomai  -nS  frir»- riaot  (sd.)  .  .  Aaauharfru  .  .  yö  mam  tat 'rts  sinai  (sd.)  .  .  yat  mi  da%at  akurS  Y. li.4,i.\  —  ya  tal yat  kaemahe  'nS  nigä- tahanti  *mMiiaitHsd.)  Y.  /o,  1 5 ;  —  /a^wärü *nd  fraianntarUi  Vd."/0;  io,4;  —  mit Gen.:  ^wä/pm  a  gJus  ß-a^wansS (ßA.)  .  . Aaomai   'tis  Y.  //.  7.         a)  'Vennögens-
BAaTHOi.OMAa.  AliiuB,  Wb.
draoSiävant-
770
...tail
Eig.  tU.  ■mit(Fels)trümmenibedeckt'i  *dra^-
dby  Google
drag-
•  j.  drag-  V.  'halten*.  Praes.  2  draza-, 10  iiarimi-'\  —  Inf.  dräjatike.
'halten,  an  sich,  mit  sich  haben,  führen', Med:  ys  *paeurvd  väs?m  (sd.)  vazäite qxna  (sd.)  drazaite  väsake  Yt  5. 1 1 ;  — saranaitam  paiti.dän>m  vaauhi  Aiitatte drazimnö  (statt  NSf.)  andvi  Vt  5. 133.  a)  bes.  mit  IS.  oder  LS.  aus sasta-  m.:  tardhustrS  .  .  asänS  %asta äraiimrtö  V. /(^,  4;  —  *avazaite .  .  snai- äi7  sastaya  drasimnS  Y.  57.  31;  V.  ig. 15;  —  mtkirfm  yS  . .  aiwyäiti  .  .  vazrvm tastaya  *dra3imitiiYt.io.g6.  Unklar: kva  hs  draiahe  aiiiAs
```


## [2026-09-05T18:05:08.683Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN tarragon\"; grep -n \"^tarragon\" KLN_1966.txt KLN_1971.txt; echo \"=== KLN dragon\"; grep -n \"^dragon,\" KLN_1966.txt KLN_1971.txt"
}
```


### [2026-09-05T18:05:08.768Z] TOOL RESULT

```
=== KLN tarragon
KLN_1971.txt:241526:tarragon, n., a plant with aromatic leaves. — Sp. 
KLN_1971.txt:241534:tarragona, n., a kind of Spanish wine resembling 
KLN_1966.txt:38234:tarragona,  n.,  a  kind  of  Spanish  wine  resembling port.  —  Short  for  Tarragona  wine,  fr.  Tarragona, a  province  in  N.-E.  Spain, tarras,  n.  —  A  var.  of  trass, tarrock,  n.,  a  young  kittiwake.  —  From  Green¬ land  Eskimo  taterdq.
=== KLN dragon
KLN_1971.txt:76192:dragon, n. — OF. (— F.), fr. L. draconem , ace. 
KLN_1971.txt:177350:dragon, for the second see gwyniad.
```


## [2026-09-05T18:05:10.656Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '241520,241536p' KLN_1971.txt; echo \"=== dragon\"; sed -n '76188,76215p' KLN_1971.txt"
}
```


### [2026-09-05T18:05:10.756Z] TOOL RESULT

```
betrayed the capitol to the Sabines, and was 
buried at its foot. The name Tarpeia is prob. of 
Etruscan-Tyrrhenian origin, 
tarpon, n., a large fish of the herritig family. — 
Prob. of American Indian origin, 
tarradiddle, n., lie, fib. — An invented word, 
tarragon, n., a plant with aromatic leaves. — Sp. 
taragona , fr. Arab, farkkun, ‘dragon wort’, fr. 
Gk. SpaxovTtov, ‘adderwort’, lit. ‘a little drag- 
on’; dimin. of $paxo>v, gen. SpaxovTOt;, ‘drag- 
on’. Cp. It. targone and F. estragon, which 
are of the same origin and meaning, and see 
dragon. 

tarragona, n., a kind of Spanish wine resembling 
port. — Short for Tarragona wine , fr. Tarragona , 
a province in N.-E. Spain, 
=== dragon
8payoup.avo<;, fr. targumdn, Egypt, pronuncia- 
tion of Arab, tarjumdn, fr. Aram. turgh*mdn&, ult. 
fr. Akkad, targumanu, ‘interpreter’. See Targum. 

dragon, n. — OF. (— F.), fr. L. draconem , ace. 
of draco, ‘a kind of a serpent ; dragon’, fr. Gk. 
Spaxcuv, which prob. means lit. ‘the sharp- 
sighted one’, and is rel. to 8£px£<x&at, ‘to look 
at’, fr. I.-E. base *derfc-, *dfk-, ‘to see, look at’, 
whence also OI. dars-, ‘to see’, da-daria, ‘I have 
seen*, darsatah , ‘visible’, dfs-, ‘seeing, sight*, 
Avestic darshti -, ‘sight’. Alb. drite (for *dpktd-), 
‘light’, Goth. ( ga)tarhjan , ‘to make distinct’, 
OE. torht , ‘bright’, OHG. zoraht , ‘clear’, OIr. 
derc, ‘eye’, W. drych , ‘aspect’, drem, Bret. 
dremm (for *dfk-sma), ‘face’. Cp. darshana, 
Dracaena, Dracontium, dracunculus, dragoon, 
drake, ‘dragon’, rancle, tarragon. 

Derivatives: dragon-ess , n., dragonet (q.v.), dra- 
gonnade (q.v.) 

dragonet, n., 1) a little dragon; 2) a small marine 
fish. — OF., dimin. of dragon. See dragon‘ 
and -et. 

dragonnade, n., persecution of the French pro- 
testants during Louis XIV; military attack on
```


## [2026-09-05T18:05:24.014Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 250 251 252 253; do echo \"--- leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -3; done"
}
```


### [2026-09-05T18:05:25.823Z] TOOL RESULT

```
--- leaf 250
iculate,  v.
Derivative:  disarticulat-ion,  n. disassociate,  tr.  v.  —  Formed  fr.  dis-  and  associ¬ ate,  v.  Cp.  dissociate.
Derivative:  disassociat-ion,  n. disaster,  n.,  misfortune,  calamity.  —  F.  desastre, fr.  It.  disastro  (but  with  the  substitution  of  the F.  prefix  des-  for  It.  dis-).  It.  disastro  is  a  back
--- leaf 251
d  countenance.  Cp.  F.  de- contenancer.
discourage,  tr.  v.  —  OF.  descoragier,  descoura- gier  (F.  decourager),  fr.  des-  (fr.  L.  dis-)  and corage  (F.  courage).  See  dis-  and  courage  and cp.  encourage.
discouragement
--- leaf 252
inheriting  (archaic).
—  Fr.  earlier  disheriteson,  fr.  OF.  desherileison, fr.  desheriter,  ‘to  disinherit’,  fr.  des-  (fr.  L.  dis-) and  heriter,  ‘to  inherit’,  fr.  L.  hereditare,  ‘to  in¬ herit’.  See  heredity  and  cp.  disinherit.
dishevel,  tr.  v.  —  Back  formation  fr.  disheveled, disheveled,  dishevelled,  adj.,  disarranged;  untidy; tousled. —  Formed  with  suff.-ed  fr.  OF .descheve- le,  ‘disheveled’,  fr.  ML.  discapiilatus,  ‘stripped of  hair’,  fr.  dis-  and  L.  capillus,  ‘hair’.  In  F. echevele,  ‘disheveled’,  the  pref.  des-  has  been  re¬ placed  by  the  pref.  e-  (fr.  L.  ex-,  ‘out  of,  from’ ; see  1  st  ex-).  See  capillary, dishonest,  adj.  —  ME.  dishoneste,  fr.  OF.  des-
--- leaf 253
cent  and  cp. words  there  referred  to.
Derivatives:  dispers-al,  n.,  dispers-ed-ly,  adv., dispers-ible,  adj.,  dispers-ibil-ity,  n.,  dispersion (q.v.),  dispers-ive,  adj.,  dispers-ive-ly,  adv., dispers-ive-ness,  n.
dispersion,  n.  —  F.,  fr.  L.  dispersidnem,  acc.  of dispersio,  ‘a  scattering’,  fr.  dispersus,  pp.  of  dis¬ pergere.  See  prec.  word  and  -ion. dispirit,  tr.  v.,  to  discourage.  —  Formed  fr.  dis¬ and  spirit.
```


## [2026-09-05T18:05:30.604Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor key in ['dragon,  n.','tarragon,  n.','tarragon','dracunculus','Dracontium']:\n    i=t.find(key)\n    print(key, i, 'leaf', t[:i].count('\\f') if i>0 else None)\nEOF"
}
```


### [2026-09-05T18:05:32.634Z] TOOL RESULT

```
dragon,  n. 2973268 leaf 262
tarragon,  n. 9619333 leaf 834
tarragon 2971281 leaf 262
dracunculus 2971101 leaf 262
Dracontium 2958969 leaf 261
```


## [2026-09-05T18:05:45.110Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 262 834; do echo \"=== leaf $n head\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -2; echo \"--- tail\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | tail -3; done"
}
```


### [2026-09-05T18:05:46.632Z] TOOL RESULT

```
=== leaf 262 head
—  See  doom  palm.
dour,  adj.,  hard,  stern  ( Scot .)  —  L.  durus,  ‘hard’. See  dure.
--- tail
Derivatives:  drag,  n.  (q.v.),  dragg-er ,  n.,  dragg¬ ing,  adj.,  dragg-ing-ly,  adv„  dragg-y,  adj.,  dragg- i-Iy,  adv.,  dragg-i-ness,  n. drag,  n.  —  Fr.  prec.  word.  The  various  meanings of  this  noun  are  all  traceable  to  the  original meaning,  ‘that  which  drags  or  is  dragged’.  Cp. drogue.
draggle,  tr.  and  intr.  v.  —  Formed  from  the  verb drag  with  freq.  suff.  -le.  Cp.  drawl.
Derivative :  dragg-ly,  adv. dragoman,  n.,  guide  and  interpreter.  —  F.  drago¬ man,  drogman,  fr.  It.  dragomano,  fr.  MGk. Spayoupavo^,  fr.  targumdn,  Egypt,  pronuncia¬ tion  of  Arab,  tarjumdn,  fr.  Aram.  turghlmanA,  ult. fr.  Akkad,  largumdnu,  ‘interpreter’.  See  Targum. dragon,  n.  —  OF.  (=  F.),  fr.  L.  draconem,  acc. of  draco,  ‘a  kind  of  a  serpent ;  dragon’,  fr.  Gk. Spaxcov,  which  prob.  means  lit.  ‘the  sharp- sighted  one’,  and  is  rel.  to  S^pxeaHai,  ‘to  look at’,  fr.  I.-E.  base  *derk-,  *dpk-,  ‘to  see,  look  at’, whence  also  01.  dars-,  ‘to  see’,  da-darsa,  ‘I  have seen’,  darsatah,  ‘visible’,  dps-,  ‘seeing,  sight’, Avestic  darshti-,  ‘sight’.  Alb.  drite  (for  *dpkta-), ‘light’,  G
=== leaf 834 head
 see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also  Teut.  loan  words.  G. Tartsche,  ‘small  round  shield;  target’,  has  been re-borrowed  fr.  OF.  targa.
targe,  tr.  v.,  to  harass  with  questions  (Scot.)  — Of  uncertain  origin.
--- tail
tashrif,  also  tashreef,  n.,  honor,  respect  ( Anglo- Indian )  —  Arab,  tashrif,  ‘an  honoring’,  verbal noun  of  sharrafa,  ‘he  ennobled,  elevated,  honor¬ ed’,  second  form  of  sharufa,  ‘he  wras  exalted,  he was  noble’.  See  shereef  and  cp.  words  there  re¬ ferred  to.
tasimeter,  n.,  an  electrical  instrument  for  meas¬ uring  changes  in  pressure  caused  by  changes  in temperature.  —  Coined  fr.  Gk.  xxoip,  ‘stretch¬ ing,  tension’,  and  uixpov,  ‘measure’.  Gk.  xdai<; stands  for  I.-E.  *tntis,  whence  also  OI.  tatih, ‘row,  line,  thread’;  from  *tn-,  zero  degree  of base  *ten-,  ’to  stretch’,  whence  OI.  tanoti, ‘stretches’,  Gk.  xeiveiv,  L.  tendere,  ‘to  stretch’. See  tend,  to  move  in  a  certain  direction’,  and cp.  ectasis  and  words  there  referred  to. Derivatives:  tasimetr-ic,  adj.,  tasimetr-y,  n. task,  n.  — -  ME.  taske,  fr.  ONF.  tasque,  fr.  OF. tasche  (F.  tache)  fr.  VL.  *tasca,  metathesized  fr. ML.  taxa,  which  is  a  back  formation  fr.  L.  ta- xare,  ‘to  touch  sharply,  handle;  to  appraise, estimate’.  See  tax  and  cp.  tasse  and  the  second element  in  sabretache.
tass,  n. ,  a  drinking  cup ;  a  small  draft.— M  F.  ( =  F.) tasse,  ‘cup’,  fr.  OF.,  fr.  Arab.  tassah,  tass,  fr. Pers.  tdsht,  ’cu
```


## [2026-09-05T18:06:02.445Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==263' KLN_1966.txt | grep -nE \"^[[:space:]]*[0-9]{3}[[:space:]]*$\" ; echo \"--- any 3-digit standalone in leaves 260-265\"; for n in 260 261 262 263 264; do awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | grep -oE \"\\b(4[0-9]{2}|5[0-9]{2})\\b\" | head -4 | tr '\\n' ' '; echo \" <- leaf $n\"; done"
}
```


### [2026-09-05T18:06:04.122Z] TOOL RESULT

```
--- any 3-digit standalone in leaves 260-265
476  <- leaf 260
477  <- leaf 261
478 479  <- leaf 262
480 481 483  <- leaf 263
484 485  <- leaf 264
```


## [2026-09-05T18:06:10.643Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 832 833 834 835; do awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | grep -oE \"\\b(15[0-9]{2}|16[0-9]{2})\\b\" | head -4 | tr '\\n' ' '; echo \" <- leaf $n\"; done; echo \"=== find leaf with 1554\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'\\b155[34]\\b',p) and i>780:\n        print(i, p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T18:06:12.779Z] TOOL RESULT

```
1583 1561 1613  <- leaf 832
1572  <- leaf 833
 <- leaf 834
1577  <- leaf 835
=== find leaf with 1554
823 , orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  sword-, ‘dirty,  dark,  black’,  whence  also  sordes,  ‘dirt
824   waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to  OE.  swindan, ‘to  waste  away,  languish,  vanish’,  and
```


## [2026-09-05T18:06:24.385Z] TOOL CALL #27: Bash

```json
{
 "command": "ls site/pages/120.jpg 2>/dev/null; pdftoppm -f 120 -l 120 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg120 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T18:06:26.571Z] TOOL RESULT

```
site/pages/120.jpg
total 34636
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 14:06 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
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


## [2026-09-05T18:06:29.728Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg120.png"
}
```


### [2026-09-05T18:06:30.187Z] TOOL RESULT

```

```


## [2026-09-05T18:06:30.184Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:06:37.921Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 823 824 825; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -2; echo \"...\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | tail -2; done"
}
```


### [2026-09-05T18:06:40.371Z] TOOL RESULT

```
=== leaf 823
, orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  sword-, ‘dirty,  dark,  black’,  whence  also  sordes,  ‘dirt, filth’.  See  sordid  and  cp.  swarthy.
Derivative:  swart-ly,  adv. swarthy,  adj.,  dark;  dusky.  —  Formed  with  adj. suff.  -y  fr.  swarth,  dial.  var.  of  swart.
...
Derivatives:  swindle,  n.,  swindl-ing,  n.,  swindl- ing-ly,  adv.
swindler,  n.,  cheat,  sharper.  —  G.  Schwindler, ‘giddy  person;  dreamer,  visionary’,  fr.  schwin- deln,  ‘to  be  dizzy,  to  scheme  fantastic  things',  fr. MHG.  swindeln,  fr.  OHG.  swintilon,  ‘to  swoon; to  be  dizzy’,  freq.  of  swintan  (whence  MHG. swinden,  G.  schwinden),  ‘to
=== leaf 824
  waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to  OE.  swindan, ‘to  waste  away,  languish,  vanish’,  and  possibly cogn.  with  Aram,  k'andem,  ‘I  destroy’,  OIr.  a- sennad,  ‘finally’.  The  sense  development  of  G. Schwindler,  which  now  means  ‘cheat,  sharper, impostor’,  is  due  to  the  influence  of  E.  swindler. Derivative:  swindler-ly,  adj. swine,  n.  —  ME.  swin,  fr.  OE.  swin,  rel.  to  OS., OFris.,  MLG.,  OHG.  MHG.  swin,  ON.  svin, Dan.,  Swed.  svin,  MDu.  swijn,  Du.  zwijn,  G. Schwein,  Goth,  swein,  and  cogn.  with  Gk. ui ou<;,  ‘swine’,  utvo?,  ‘swinish’,  L.  sus, ‘swine’,  suinus,  ‘of  swine’,  OSlav.  svinu,  ‘of swine',  svinija,  ‘swine',  OE.  sugu,  su,  ‘sow’.  See sow,  n.,  and  cp.  words  there  referred  to.  Cp.  also the  second  element  in  keelson.
Derivatives:  swin-ery,  n.,  swin-ish,  adj.,  swin-ish- ly,  adv.,  swin-ish-ness,  n.
...
■ —  Formed  fr.  L.  syllaba,  ‘syllable’,  and  suff. -ficare.  See  syllable  and  -fy. syllabize,  tr.  v.,  to  syllabify.  —  ML.  syllabizare, fr.  Gk.  ouXXafU^Etv,  fr.  auXXa|3r; ,  ‘syllable’.  See next  word  and  -ize.
syllable,  n.  —  ME.  sillable,  fr.  MF.  sillabe  (F. syllabe),  fr.  OF.,  fr.  L.  syllaba,  fr.  Gk.  ouXXapf; , ‘syllable’,  lit.  ‘a  holding  together  (scil.  of  letters)’, fr.  auXXafjLpavEiv,  ‘to  take  or  put  together’,  fr. ouv  (see  syn-)  and  Xa(j.(3av£iv,  ‘to  take,  grasp, seize’.  See  lemma  and  cp.  word
=== leaf 825
s  there  referred to.  Cp.  also  monosyllable,  dissyllable,  trisyllable, tetrasyllable,  decasyllable,  dodecasyllable. syllable,  tr.  v.,  to  pronounce  in  syllables.  —  Fr. syllable,  n. ;  first  used  by  Milton.
Derivative:  syllabl-ed,  adj. syllabus,  n.,  outline,  compendium.  —  Eccles.  L. syllabus,  ‘list’,  fr.  Gk.  ouXXapot;,  prop,  an  er¬ roneous  reading  occurring  in  early  printed  edi¬ tions  of  Cicero's  Letters  to  Attic  us  (IV,  5  and 8)  for  otXXupoq,  ‘a  strip  of  parchment  attached to  a  book  and  bearing  the  name  of  the  author, title  slip’;  cp.  oiXXufla,  ‘fringes'.  Both  these words  are  prob.  alterations  of  orig.  oiTTu(3o<;, resp.  olttu(3oc,  aiTxuflf],  whose  etymology  is  un¬ known.
...
Symphytum,  n.,  a  genus  of  plants,  the  comfrey (bot.)  —  ModL.,  fr.  Gk.  aup9UTov,  ‘comfrey’, lit.  ‘grown  together’,  prop.  neut.  verbal  adj.  of oup<p>)eiv.  See  prec.  word  and  -phyte. sympiesometer,  sympiezometer,  n.,  a  barometer for  measuring  atmospheric  pressure  from  its  ac¬ tion  on  a  liquid.  —  Compounded  of  Gk.  aup- meau;,  ‘compression’,  and  pexpov,  ‘measure’. The  first  element  derives  fr.  aupmst^e'.v,  ‘to  com¬ press’,  fr.  auv  (see  syn-)  and  tus^eiv,  ‘to  com¬ press’;  see  piezo-.  For  the  second  element  see meter,  ‘poetical  rhythm’.  Cp.  piezometer. Symplegades,  n.  pi.,  two  rocks  at  the  entrance  of the  Hellespont,  which  clashed  together  and crushed  whatever  came  between  them  (Greek mythol.)  —  L.,  fr.  Gk.  SupirXifjYaSEi;  (scil. 7t£xpai),  ‘the  Clashing  (Rocks)’,  fr.  auv  (see syn-)  and  the  stem  of  tiX^ooeiv,  ‘to  strike’, whence  also  jtXijy?],  ‘blow,  stroke’.  See  plague and  words  there  referred  to  and  cp.  esp.  Ple- gadis.
Symplocarpus,  n.,  a
```


## [2026-09-05T18:06:46.569Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD tarkhun\"; grep -n \"طرخون\\|ترخون\" TAD.txt TAD_pages.txt | head; echo \"=== AHD der/drem/dreu/derk\"; grep -n \"^der-\\|^drem-\\|^dreu-\\|^derk-\\|^der\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T18:06:46.652Z] TOOL RESULT

```
=== TAD tarkhun
TAD.txt:1851:طرخون - تعريب «لااباءهدهةءل اللاتينى وهو نيات أصله فى الونانية 
=== AHD der/drem/dreu/derk
365:der-'
405:drem-. To sleep. Suffixed zero-grade form “drm-yo- in Latin dormire, to sleep: DORMANT, DORMER, DORMITORY. [Pok. dré- 226.]
```


## [2026-09-05T18:06:51.788Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1845,1860p' TAD.txt; echo \"=== leaf of that\"; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'طرخون' in p: print('leaf',i); print(p[:400])\nEOF"
}
```


### [2026-09-05T18:06:53.652Z] TOOL RESULT

```
طبتجة ‏ ترق « طابائجة 4 وهو الغد ار أي البارودة الصغيرة 

طر وش - فارسي م ركب من « سر 6 أي رأس و« وش » أي غطاء 

طرخان -- فارسي « ترخان 6 وهو زعم قوم معفى من الضراشب 

طرخون - تعريب «لااباءهدهةءل اللاتينى وهو نيات أصله فى الونانية 
لناك 511 لفك 

طرطير ع راجم دردي 

طرنا وطامبا ‏ ايطالى 552:ه6 قد بطل استعالها واعتاضوا ممها بلفظة 
ممم عريمها مض 

0 ايه باد وهاه 

=== leaf of that
```


## [2026-09-05T18:07:00.069Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '360,375p' AHD_watkins1985.txt; echo \"=== search TREAD/TRAP/TRADE\"; grep -n \"TREAD\\|TRAP\\b\\|TRADE\\|DROMEDARY\\|SYNDROME\\|drem\\|derk\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T18:07:00.144Z] TOOL RESULT

```
<persisted-output>
Output too large (41.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bsuy7v3hn.txt

Preview (first 2KB):
[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en)
...
</persisted-output>
```


## [2026-09-05T18:07:04.283Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"der-[^ ]\\{0,3\\} To run[^]]\\{0,900\\}\" AHD_watkins1985.txt | head -3; echo \"======\"; grep -on \"derk-[^]]\\{0,500\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-05T18:07:06.170Z] TOOL RESULT

```
======
366:derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.
377:derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, p
1434:derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
```


## [2026-09-05T18:07:13.472Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"der-1\\. To run[^]]\\{0,1200\\}\\]\" AHD_watkins1985.txt | head -2; echo \"=====INDEX\"; grep -on \"TREAD [a-z0-9-]*\\|TRADE [a-z0-9-]*\\|TRAP[!12]* [a-z0-9-]*\\|TRIP [a-z0-9-]*\\|SYNDROME [a-z0-9-]*\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T18:07:15.180Z] TOOL RESULT

```
=====INDEX
1464:TRAP der-1
2215:TRAP pase
2398:TRADE der-1
2402:TRAP! der-1
2403:TRAP2 der-2
2406:TREAD der-1
2411:TRIP der-1
```


## [2026-09-05T18:07:17.172Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"der-1[.,][^]]\\{0,1800\\}\\]\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-05T18:07:19.178Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:07:22.646Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"To run, walk\\|To run\\b\" AHD_watkins1985.txt | head; echo ---; grep -on \"der-!\\?[^ ]\\{0,2\\} *To run[^]]\\{0,1500\\}\" AHD_watkins1985.txt | head -2; echo \"--- search TRODDEN/tread context\"; grep -on \"[^]]\\{0,1200\\}Old English tredan[^]]\\{0,600\\}\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-05T18:07:26.704Z] TOOL RESULT

```
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
384:dhgvher-. To run. Perhaps Greek phtheir, louse: (ICH), PHTHIRIASIS. [Pok. g¥hdher- 487.]
388:dhregh-. To run. 1. Greek trekhein (< *threkhein), to run (> trokhos, wheel): TROCHAL, TROCHANTER, TROCHE, TROCHEE; TROCHOPHORE. 2. O-grade form *dhrogh- in Greek trokhileia, trokhilia, system of pulleys, roller of a windlass: TROCHLEA, TRUCK!, (TRUCKLE). [Pok. 1. dhregh- 273.]
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
1078:a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
---
--- search TRODDEN/tread context
ugrep: error: error at position 645
-\xbf][\x80-\xbf]){0,600}
                         \___exceeds complexity limits
```


## [2026-09-05T18:07:31.102Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('der-1.')\nif i<0:\n    import re\n    for m in re.finditer(r'der-.{0,3}\\s*(To run|To split)', t):\n        print(m.start(), repr(t[m.start()-60:m.start()+40]))\nEOF"
}
```


### [2026-09-05T18:07:32.721Z] TOOL RESULT

```
162580 '. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with deriva'
```


## [2026-09-05T18:07:35.468Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.rfind('der-',0,160000)\nj=t.find('[Pok. 3. (der-) 204.]',150000)\nk=t.rfind('der-1',0,j)\nprint(t[j-3000:j+60])\nEOF"
}
```


### [2026-09-05T18:07:37.108Z] TOOL RESULT

```
m-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
der-'
diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with deri
```


## [2026-09-05T18:07:53.315Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON tarxun\"; grep -n \"ترخون\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5; echo \"=== MON darun\"; grep -c \"درون\" MON_part1.txt 2>/dev/null; echo \"=== LKT estragon/tarragon\"; grep -n -i \"tarragon\\|Estragon\\|tarhun\\|ṭarḫūn\" LKT.txt | head -10; echo \"=== SKT tarragon/dragon\"; grep -n \"^tarragon\\|^Tarragon\\|^dragon\\|^Dragon\" SKT.txt | head"
}
```


### [2026-09-05T18:07:53.434Z] TOOL RESULT

```
=== MON tarxun
incoming/MON/MON_2vol_Adena_v1_djvu.txt:39845:ترخون فرهنگ فارسی معیر ۳۵ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:75003:مانند نعناع» ترخون» ریحان و جز آنها؛ ج. 
MON_part1.txt:39845:ترخون فرهنگ فارسی معیر ۳۵ 
MON_part1.txt:75003:مانند نعناع» ترخون» ریحان و جز آنها؛ ج. 
MON_part2.txt:90371:جعفری» نعنا» ترخون» مرزه» ریحان» 
=== MON darun
137
=== LKT estragon/tarragon
4576:'Kaisersalat,  Bertram  Arteraisia  dracun- culus'  [aus  gr.  bpdKUJv] ;  hieraus  it.  tar- gone,  mfrz.  targon,  frz.  targon,  estragon, prov.  draguneto,  estargon,  sp.  taragona, tarncontea,  pg.  estragäo,  rum.  tarhon; engl,  dragoon,  dtsch.  Dragun,  Esdragon; russ.  dragun,  estragon,  bulg.  estragon, cech.  dragön,  estragon,  poln.  estragon, draganek.  —  Der  Esdragon  ist  wahr- scheinlich zur  Zeit  der  Kreuzzüge  nach Europa  eingeführt  worden,  da  er  den Alten  unbekannt  war.  [DE  348.  Eguilaz 392.  Devic  DEt  112/113.  Lammens Rem  108/109.  [ML  8581.  Gorjajew 95.  432.
6487:estragon  2034
7646:estragon  2034
=== SKT tarragon/dragon
5383:tarragon,  a  plant.  (Span.  —  Pers. «  Gk.) Span.  taragoHtta  (whence  F.  /argffn),wm Pen.  tarkAUn^  dragi>n-wort.<-Gk.  fipiuran', a  dngon.
19206:Tarragon,  a  plant ;  see  Dragon.
```


## [2026-09-05T18:07:58.948Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4565,4580p' LKT.txt; echo \"=== MON entry\"; sed -n '39840,39860p' MON_part1.txt"
}
```


### [2026-09-05T18:07:59.019Z] TOOL RESULT

```
Ar.  Urb.]
160
2030.  Ar.  tarb:
'ümenlum,  Netz',  d.  h.  Faltungen  (Dupli- katuren)  des  Bauchfells  (Peritonium)  der Wirbeltiere,  also  auch  beim  Menschen [aus  pers.  därb  'tetf  Horn  NpEt  ö.  97, Nr.  43ö];  hieraus  nilat.  der  Anatomen zirbits,  it.  zirbo,  sp.  pg.  zirbo,  zerbo 'Leibesnetz',  unmittelbar  mit  Metathesis it,  tn'ppn,  frz.  tripe,  prov.  kat.  sp.  pg. tripj  'Eingeweide,  Kaidaunen',  it.  (dial. Piemont  bis  Neapel)  tripa  'Bauch'. [HArHebrAn  247/250.    ML  8703.
2031.  Ar.  tarbüs:
'Roter  Fez'  [Dozy  Vetem  220,  250,  289 ; aus  tk.  ter  'Schweiß'  und  pers.  püs, Präsensstamm  püsidän  'bedecken',  s.  hier Nr.  1625,  also  'Schweifskappe'] ;  hieraus frz.  tarbouch,  dlsch.  Tarbusch,  engl,  tar- boosh,  tarbouche.
2032.  Ar.  tarfä':
'Tamariske,  Tamarix  gallica' ;  hieraus  in gleicher  Bedeutung  sp.  atarfe,  taray. [DE  212.  348.    Eguilaz  305.  ML  8578.
2033.  Ar.  iargumän:
'Ausleger,  Dolmetscher'  [Vb.  targama 'dolmetschen'  aus  syr.  targem  'erläutern', vgl.  targüm  'Erläuterung,  Erklärung'; beachte  assyr.  ragämu  'sprechen',  rigmu 'Wort',  eigentlich  'schreien,  rufen';  'Ge- schrei, Ruf,  DelHWB  612  a,  sowie  assyr. targumänu  'Dolmetsch',  ebenda  713  a]; hieraus  it.  dragomanno,  turcimanno  [mit Anlehnung  au  turco  'Türke'],  prov. drogoman,  frz.  drogoman,  drogman, trucheman,  kat.  sp.  drogoman,  trujaman, pg.  dragomano,  trugimäo;  engl,  drogo- man, druggerman,  ndl.  drogoman,  drog- man, dtsch.  Dragoman,  (älter)  Dnitzel- mann,  Trutschelmann;  russ.  dragoman. [DE  351.  Eguilaz  508.  ML  8580. Kluge  96.
2034.  Ar.  tarhün :
'Kaisersalat,  Bertram  Arteraisia  dracun- culus'  [aus  gr.  bpdKUJv] ;  hieraus  it.  tar- gone,  mfrz.  targon,  frz.  targon,  estragon, prov.  draguneto,  estargon,  sp.  taragona, tarncontea,  pg.  estragäo,  rum.  tarhon; engl,  dragoon,  dtsch.  Dragun,  Esdragon; russ.  dragun,  estragon,  bulg.  estragon, cech.  dragön,  estragon,  poln.  estragon, draganek.  —  Der  Esdragon  ist  wahr- scheinlich zur  Zeit  der  Kreuzzüge  nach Europa  eingeführt  worden,  da  er  den Alten  unbekannt  war.  [DE  348.  Eguilaz 392.  Devic  DEt  112/113.  Lammens Rem  108/109.  [ML  8581.  Gorjajew 95.  432.
2035.  Hind.  tärl:
'Palm wein  vom  Palmbaume  tär'';  hier- aus engl,  toddy  'der  süße  Saft  gewisser Palmen,  gesüßter  Branntwein  mit  heißem Wasser'.
2036.  Ar.  tarlda: 'Transportschiff  für  Pferde,  Schlepp- schiff' ;  hieraus  it.  prov.  kat.  sp.  tarida 'Lastschiff'.  Hiermit  muß  auch  it.  tar- tana,  frz.  tartane,  kat.  sp.  pg.  tartana; ndl.  tartaan  'kleines  Seefahrzeug'  zu- sammenhängen [das  ML  8588  genannte Grundwort  ar.  tarfaneh  existiert  wohl nicht  oder  ist  selbst,  wenn  es  belegt werden  könnte,  romanischen  Ursprungs]. [DE  349.    Eguilaz  503.    ML  8582.
2037.  Ar.  ta'rif: 'Bekanntmachung'  [subst.  Inf,  II  vom Vb.  'arafa  'wissen'];  hieraus  it.  tariffa 'Warenverzeichnis',  frz.  tarif,  sp.  pg. tarifo,  rum.  tarif,  Vb.  tarif a  'besteuern'; ndl.  tarief,  dtsch.  Tarif,  engl,  tariff 'Warenverzeichnis,  Preisliste';  russ.  tarif, cech.  tarifa,  poln.  taryfa.  [DE  348. Eguilaz  503.    ML  8583.
=== MON entry
طعام که از گندم بلغور سازند و با داروهای 
گرم در آب بجو شانند ۳ 
گیرد و قدری آب غوره یا شیر در آن ر بزند 


ترخون فرهنگ فارسی معیر ۳۵ 


و آن را به شکل گلوله‌هایی درآورند و 
خشک کنند و در زمستان خو رند. 
ترخود: ۱2۲۲ (ص‌ مر .) مردم خونی و 
بی‌با ک و دزد و اوباش. 

ترخیص: :۱۸۳ [ع.] (مص‌م.) دستوری 
دادن» اجازت؛ ج. ترخیصات. ترخیص کال 
(متاع): اجازة خروج دادن از گمرکث و 
غیر ه. 

تسرحصیص: 5 [.] (سص‌م.) ارزان 
کردن از بها کاستن. (امص.) ارزانی؛ ج. 
ترخیصات.
```


## [2026-09-05T18:08:07.114Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39800,39845p' MON_part1.txt"
}
```


### [2026-09-05T18:08:07.167Z] TOOL RESULT

```
یک قافیه می‌گوید و سپس چند بیت دیگر 
در همان بحر و به قافیةٌ دیگر و همچنین و 
یک بیت (به همان وزن) را در میان بندها 
تکرا رکند؛ مق. ت رکیب‌بند. 


ترحال: ۱921 [ع.] (مسصل.) باربستن» 
کوچیدن. (امص.) رحلت» کوچ. 
ترحصل: ۱۵۲0۱ [ع.] (مسصل.) بار 
انیت (امص.) رحلت» 
ترحم: : 000ظ۲۵ه) [ع. ۰] (مص‌ل.) بخشودن» 
رحم کردن؛ بخشایش آوردن» بر سر لطف 
و مسهربانی آمدن. (امص.) مهرورزی» 
ترجيیب. نآ [ع.] (مسصع.) مرجم 
گفتن» خوشامد گفتن. جارا فراخ کردن. 
(امص.) خوشامدگویی؛ ج. ترحیبات. 
ترحیل: ۱:3 [ع.] (مص‌م.) کوچانیدن» 
کوچ فرمودن؛ ج. ترحیلات. 

ترحیم: 2 [ع.) (مصم.) رحم کردن» 
مهربانی کردن. طلب آمرزش کردن» درود 
فرستادن برای میت. مجلسی که برای طلب 
مغفرت جهت مرده خویشاوندان وی تر تیب 
دهند و در آن قرآن تلاوت می‌شود و واعظ 
پس از وعظ از مناقب مسبت اد و برای او 
طلب آمرزش می‌کند. 

ترخان: «قدها [- طرخان» تر. مف.] (ا.) 
شاهزادة ترک و مغول و بزرگی که از بعض 
مزایای موروثی از جمله معافیت از مالیات و 
عوارض متعدد برخوردار بود و مجاز بود که 
ه رگاه می خو است به نزد سلطان رود» بعض 
روحانیان نیز بدین مقام کب 
ترحص: 25| [ع.] (مسصل.) اسان 
گرفش. آسان وا گرفتن. اجازه گرفتن» 
رخصت یافتن» دستوری یافتن. جایز بودن» 
روا سودن. (امص.) اجازه» رخضصت؛ ج. 
ترخصات. 

ترخوانه: (0-)۱۵۳502 [- ترخینه ] (۱.) نوعی 
طعام که از گندم بلغور سازند و با داروهای 
گرم در آب بجو شانند ۳ 
گیرد و قدری آب غوره یا شیر در آن ر بزند 


ترخون فرهنگ فارسی معیر ۳۵
```


## [2026-09-05T18:08:15.310Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T18:08:15.318Z] TOOL RESULT

```


```


## [2026-09-05T18:08:17.824Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tarragon",
 "prompt": "Full etymology section for tarragon: give the exact chain (Middle English/French/Latin/Arabic/Greek forms) verbatim."
}
```


## [2026-09-05T18:08:19.499Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%AE%D9%88%D9%86",
 "prompt": "Give the Arabic entry طرخون: etymology, meaning, and also any Persian entry ترخون on the page (etymology, whether borrowed from Arabic)."
}
```


### [2026-09-05T18:08:22.620Z] TOOL RESULT

```
# Etymology Chain for "Tarragon"

According to the Wiktionary entry, the etymological path is:

**English** ← **Middle French** _targon_ (modern _estragon_) ← **Medieval Latin** _tragonia_ ← **Arabic** _طَرْخُون_ (ṭarḵūn) ← **Ancient Greek** _δρακόντιον_ (drakóntion, meaning "dragonwort")

The Greek term derives from _δράκων_ (drákōn, "dragon, serpent"), reflecting the herb's historical association with dragon imagery. The entry notes that English "tarragon" and "estragon" are doublets sharing this common ancestry.
```


### [2026-09-05T18:08:24.961Z] TOOL RESULT

```
# Arabic Entry طرخون

**Etymology:** Derived from Ancient Greek *δρακόντιον* (drakóntion, "edder-wort"), from *δράκων* (drákōn, "dragon, serpent"), referencing the leaf shape.

**Meaning:** The term refers to tarragon (*Artemisia dracunculus*) in both its growing and processed forms, also known as estragon.

# Persian Entry ترخون

**Etymology:** The page displays this Persian term but provides no separate etymology section for it. Based on the Arabic entry's extensive descendants list, Persian *ترخون* (tarxun) appears to be borrowed directly from the Arabic *طَرْخُون* (ṭarḵūn).

The word traveled across multiple language families through medieval trade routes, eventually reaching European languages like English "tarragon" and French "estragon."
```


## [2026-09-05T18:08:27.585Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tarragon",
 "prompt": "Full etymology of tarragon verbatim, including Medieval Latin, Arabic, Greek forms and any mention of Byzantine Greek tarkhon."
}
```


## [2026-09-05T18:08:29.303Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der%E1%B8%B1-",
 "prompt": "Give the reconstruction *derḱ-: meaning, Pokorny page, and the derived forms (Greek δέρκομαι, δράκων; Avestan; Sanskrit)."
}
```


### [2026-09-05T18:08:33.407Z] TOOL RESULT

```
# Etymology of Tarragon

The word "tarragon" originates from Medieval Latin *tragonia*, which derives from Byzantine Greek *tarchon*. This Greek term came from Arabic *tarkhon*, "said to be from a non-Arabic source, perhaps Greek *drakon* 'serpent, dragon'"

The etymological path traces back through multiple languages:

- **Arabic**: *tarkhon*
- **Byzantine Greek**: *tarchon*
- **Medieval Latin**: *tragonia*
- **English**: tarragon (1530s)

Related forms evolved in Romance languages: Spanish *taragona*, Italian *targone*, and French *estragon* (which added an unetymological prefix).

The plant's scientific name is *Artemisia Dracunculus*, a composite plant native to Russia and temperate Asia. The connection to the Greek word for "dragon" likely relates to the plant's appearance or properties, as "the one with the (deadly) glance" was a proposed literal sense for the dragon etymology.

Historically, "its aromatic leaves long have been used for flavoring (especially vinegar)."
```


### [2026-09-05T18:08:34.798Z] TOOL RESULT

```
# Proto-Indo-European Root *derḱ-

**Meaning:** "to see" (perfective aspect)

**Pokorny Reference:** Page 213 of *Indogermanisches etymologisches Wörterbuch* (1959)

**Key Derived Forms:**

- **Greek:** δέρκομαι (dérkomai, "to see"); δράκων (drákōn, "serpent, dragon")
- **Avestan:** 𐬛𐬀𐬭𐬆𐬯𐬆𐬨 (darəsəm, aorist form)
- **Sanskrit:** दृश् (dṛś, "to see"); दृष्टि (dṛ́ṣṭi, "sight/vision")

The root demonstrates typical Proto-Indo-European ablaut patterns, with forms like *dérḱ-e-ti (present) and *dérḱ-s ~ *dr̥ḱ-és (eye, as a root noun). It appears across multiple language families including Celtic, Germanic, Albanian, and Armenian branches.
```


## [2026-09-05T18:08:40.014Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Dron_(Zoroastrianism)",
 "prompt": "What is drōn/darun in Zoroastrianism, and what is its etymology (Avestan draonah-)? Quote the etymology."
}
```


## [2026-09-05T18:08:40.022Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Avestan draonah- Middle Persian drōn darun Zoroastrian sacred bread etymology"
}
```


### [2026-09-05T18:08:42.493Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T18:08:50.618Z] TOOL RESULT

```
Web search results for query: "Avestan draonah- Middle Persian drōn darun Zoroastrian sacred bread etymology"

Links: [{"title":"DRŌN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/dron/"},{"title":"Dron Yasht","url":"https://en.wikipedia.org/wiki/Dron_Yasht"},{"title":"Baj, Dron, and Ritual Power ('amal) - Zoroastrian .org.uk","url":"http://www.zoroastrian.org.uk/lib/avesta-org/ritual/rcc15.htm"},{"title":"Zoroastrian Rituals: Dron, Baj, and Ritual Power","url":"https://www.avesta.org/ritual/rcc15.htm"},{"title":"ZOROASTRIANISM - JewishEncyclopedia.com","url":"https://www.jewishencyclopedia.com/articles/15283-zoroastrianism"},{"title":"Zoroastrian bāj and drōn—l | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/abs/zoroastrian-baj-and-dronl/A3DB4FD1C4D0A4543056E3EBBE31DF0E"},{"title":"Cardiff Theosophical Society in Wales, UK:- Glossary of Zoroastrianism","url":"http://www.theosophycardiff.org.uk/theosophyuk_reference_glossary_of_zoroastrianism_theosophywales_cardiff_theosophical_society_in_wales_uk_cf24-1dl.htm"},{"title":"Did Islam adapt any rites or rituals from Zoroastrianism? - Quora","url":"https://www.quora.com/Did-Islam-adapt-any-rites-or-rituals-from-Zoroastrianism"},{"title":"Zoroastrian Global Glossary v2 (A-M) | FEZANA","url":"https://fezana.org/zoroastrian-global-glossary-v2-a-m/"},{"title":"Zoroastrian Global Glossary | FEZANA","url":"https://fezana.org/glossary/"}]

Based on the search results, here's what I found about the etymology and meaning of the Zoroastrian sacred bread:

## Etymology and Linguistic Development

The Middle Persian term drōn derives from Avestan draonah- meaning "portion of food", with the Gujarati Parsi form being darūn.

## Meaning and Semantic Evolution

In Avestan, draonah literally means 'portion, possession'. However, the term originally referred to a "sacred portion" designating a ritual offering to divine beings. 

In later Zoroastrian tradition, as reflected in the Pahlavi books and contemporary Parsi practice, drōn came to denote only the flat, round unleavened wheat bread that constitutes the regular offering.

## Physical Description and Preparation

The dron refers to 'round, sacred unleavened breads made of wheat flour with nine cuts in the middle'. According to stipulations in the Nērangestān, drōn must be prepared from dry, ritually clean, unleavened wheat flour moistened with pure water and kneaded only by priests or their wives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T18:08:53.289Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/dron/",
 "prompt": "Quote the etymology of drōn: Avestan draonah-, its meaning, Middle Persian and New Persian/Parsi forms (darūn), and any statement about the Indo-European connection."
}
```


## [2026-09-05T18:08:54.912Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dragon",
 "prompt": "Full etymology of dragon verbatim: Old French, Latin draco/draconem, Greek drakon, and the derivation from derkesthai/PIE root."
}
```


### [2026-09-05T18:08:55.020Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T18:08:59.895Z] TOOL RESULT

```
# Etymology of Dragon

The word "dragon" traces back through multiple languages. It entered English in the mid-13th century from Old French *dragon* and Latin *draconem* (nominative *draco*), meaning "huge serpent, dragon."

The Greek root *drakon* ("serpent, giant seafish") likely derives from *drak-*, described as "the strong aorist stem of *derkesthai* 'to see clearly,'" which connects to the Proto-Indo-European root *\*derk-* meaning "to see."

**Proposed literal meaning:** Scholars suggest the term may originally refer to "the one with the (deadly) glance, the one with (paralyzing) sight," emphasizing the creature's piercing gaze as a defining characteristic.

The concept appears across many cultures and languages, with related forms appearing in Old English, Gothic, Sanskrit, and other Indo-European languages—all tracing back to this ancient root connected with sight and vision.
```


## [2026-09-05T18:09:03.683Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-05T18:09:03.725Z] TOOL RESULT

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
```


## [2026-09-05T18:09:04.957Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tread",
 "prompt": "Etymology of tread verbatim (Old English tredan, Proto-Germanic *tredan, PIE root). Also mention any listed related words."
}
```


### [2026-09-05T18:09:11.106Z] TOOL RESULT

```
# Etymology of Tread

## Verb Origins
The word "tread" traces back through Middle English *treden* to Old English *tredan*, defined as "go by feet, walk; step on, trample; traverse, pass through or over."

This descends from Proto-Germanic *tred-*, which also produced cognates like Old Saxon *tredan*, Old High German *tretan*, and German *treten*.

The ultimate source is the Proto-Indo-European root *der- (1), described as the "assumed base of roots meaning 'to run, walk, step.'"

## Notable Usage Evolution
Early specialized meanings include "crush with the feet, thresh grain, press grapes" (late 14c.) and, in reference to birds, "to copulate" (early 14c.).

Idiomatic phrases developed later: "tread a measure" (dance, 1590s), "tread water" in swimming (1764), and "tread the stage" (perform drama, 1690s).

## Related Words
Connected etymologically are: **downtrodden**, **retread**, **treadle**, **treadmill**, **treadway**, and the past forms **trod** and **trodden**.
```


## [2026-09-05T18:09:13.877Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trade",
 "prompt": "Etymology of trade (noun) verbatim: Middle Low German trade, Old Saxon trada, PIE root *der-. Also note whether it is 'course, track'."
}
```


## [2026-09-05T18:09:14.902Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trap",
 "prompt": "Etymology of trap (noun) verbatim: Old English træppe, treppe, Proto-Germanic *trep-, PIE root *der- 'to run, walk, step'."
}
```


### [2026-09-05T18:09:19.346Z] TOOL RESULT

```
# Etymology of "Trade" (Noun)

Based on the Online Etymology Dictionary, the noun "trade" originated in the late 14c. from Middle Dutch or Middle Low German *trade*, meaning **"a track, a trace, course."** This term referred to a ship's course and was introduced via Hanse merchants.

The word connects to Old English *tredan* (meaning "to tread"), sharing Proto-Germanic roots with similar words across Germanic languages.

**Semantic Evolution:**
The meaning shifted significantly from mid-16c. onward:
- Mid-15c.: "way, customary course of action, manner of life"
- 1540s: "one's habitual business" or "occupation"
- 1550s: "the buying and selling or exchange of commodities"

The document notes: *"The connection to tread is obscure now."* This reflects how dramatically the word's meaning transformed from its original nautical sense of a pathway or course to its modern commercial connotations.
```


### [2026-09-05T18:09:21.680Z] TOOL RESULT

```
# Etymology of "Trap"

The word "trap" has an interesting linguistic journey. According to etymological sources, it originates from "contrivance for catching unawares," deriving from Middle English *trappe* and Old English *træppe*.

## Origin Chain

The term traces back through Proto-Germanic *trep-*, eventually connecting to the Proto-Indo-European root *der-*, which relates to "to run, walk, step." This ancestral meaning—literally "that on or into which one steps"—makes sense for a device designed to catch someone unaware.

## Evolution of Meaning

The earliest senses involved hunting and animal capture. By around 1200, the word acquired figurative theological applications, and by 1400, it developed the sense of "'deceitful practice, device or contrivance to betray one unawares.'"

Interestingly, the word expanded beyond catching devices. By 1776, "trap" became slang for "mouth," and starting in 1833, it referred to "U-shaped section of a drain pipe" designed to prevent air passage.

## Related Forms

The verb form emerged in the late 14th century, meaning to ensnare or capture, giving rise to modern compounds like mousetrap, firetrap, and sand-trap.
```


## [2026-09-05T18:09:24.264Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/syndrome",
 "prompt": "Etymology of syndrome verbatim: Medical Latin, Greek syndrome, syn- + dromos, and the PIE root given."
}
```


## [2026-09-05T18:09:24.954Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trip",
 "prompt": "Etymology of trip (verb) verbatim: Old French triper, Frankish/Middle Dutch trippen, PIE root *der-."
}
```


### [2026-09-05T18:09:29.362Z] TOOL RESULT

```
# Etymology of Syndrome

The word "syndrome" originates from medical Latin and Greek. It entered English around the 1540s, meaning "a number of symptoms occurring together."

The Greek root is *syndrome*, derived from *syndromos*, literally meaning "a running together." This breaks down into two components:

- **syn-**: "with" or "together"
- **dromos**: "a running, course"

The term's medical application emerged from this vivid imagery of symptoms converging simultaneously, much like multiple paths meeting at a single location.

Interestingly, the modern usage pattern—such as "Stockholm syndrome" or "survivor syndrome"—didn't develop until the mid-20th century. The phrase structure "_____ syndrome" became established by 1955 through psychological terminology, allowing the word to describe characteristic complexes of behaviors and beliefs beyond purely physical symptoms.
```


### [2026-09-05T18:09:32.966Z] TOOL RESULT

```
# Etymology of "Trip"

The word "trip" has Germanic roots tracing back to the late 14th century. The verb originally meant "move lightly and nimbly on the feet; skip, dance briskly, caper," deriving from Old French *triper* and ultimately from Germanic sources including Middle Dutch *trippen*.

**Key etymological points:**

- **Verb origin (late 14c.):** "jump around, dance around, strike with the feet"
- **Related languages:** The term connects to words meaning "stair, step, tread" across Germanic languages
- **Proto-Indo-European root:** PIE *\*der-*, meaning "to run, walk, step"

The meaning evolved significantly over time. By the mid-15th century, it developed the sense of stumbling or causing someone to stumble. By around 1500, it gained figurative usage meaning "make a false movement, err, go wrong."

The noun form emerged in the early 14th century from the verb, initially meaning "act or action of tripping." The familiar modern sense of "a short journey or voyage" appeared by the mid-15th century, though etymologists note "the exact connection to the earlier sense is uncertain."

More recently, the word acquired 1960s slang meaning related to hallucinogenic drug experiences.
```


## [2026-09-05T18:09:38.834Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 299 300 301 302 303; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' BQT_v2_pages.txt | head -25; done 2>/dev/null | head -140"
}
```


### [2026-09-05T18:09:40.766Z] TOOL RESULT

```
=== leaf 299
                                                                                       ‫رت‬
                           ‫بردن بکسی باشد ‪.‬‬        ‫درفشه = بم اول وثانی وسکون‌فاوفتح‬
‫در فنحك = بفتح اول وئالك وسکون‪:‬‬                         ‫بیغ وشمشیر باشد ‪.‬‬      ‫عتن»ی‬
                                                                                   ‫مرش‬
                                                                                     ‫بن ف‬
                                                                                        ‫شی‬
‫ثانی ولون که رابع باشد وجیم مفتوح بکاف زده»‬        ‫فرشی۔ بکراول وفتح انی وسکون‬
                                                                             ‫‪3‬‬
 ‫گرا ییکه‌درخواب برمردم‌افتد نورآابحربی‌کابوی‬      ‫ت‪,‬رحابتعانی کشیده ‪ ,‬خودرا مشهور ماختن‬
                                                                                       ‫بلث‬
                                                                                         ‫ثا‬
                                     ‫خوالند ‪.‬‬                               ‫وعلم کردن ماشد ‪. ۱‬‬

  ‫واف‬‫در قه = بفتح اول وسکون انی ق‬                  ‫در فشیدان ؟ ‪-‬بروزن‌ومعنید‪.‬خشیدن‬
 ‫مفتوح» بمعنی زره باشد که بعربی درع خوانتد‬        ‫است که تابن ومنورباشد ‪ -‬و بمعنی لرزیدن هم‬
‫است کهبعریی جنه‬        ‫ه‬
                       ‫دظر‬
                         ‫ممبن‬
                            ‫آر ه‬
                               ‫وبمعنی سپ‬                                           ‫‪1‬‬   ‫است‬   ‫اى‬


                                   ‫گنت ‪. ۴‬‬

                                ‫‪ - ٩‬درفشی کردن ب‌عنی مشهور کردن » رسوا کردن‪: ‎‬‬
=== leaf 300
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف انی زای نقطه‌دار همأ مده‌است‪ -‬ودر‬

 ‫در لورینه سیر خوردن ‪- ۴‬‬                                                               ‫عربی مممنی مال باشد ‪.‬‬

‫کنابه از فرب خوردن ‪ -‬و کردن‌کاری باشد" که‬
‫عمش کنن را منخص سازند ‪ -‬ویمعئی درشادی‌غم‬                  ‫‪ ۰‬و عصی یخی را گوند که درزیر‌ناودان‬           ‫گوند‬

                                                                                                     ‫به ود‬
‫کنابه‬              ‫در لور بنه سیر دآدن‬                        ‫‪3‬ممنی‌ابن ات‬
                                                                         ‫در کحامی خو ر ۔ب‬
 ‫کاازری‌باشد که عش کے رابرهم زنند ‪ -‬وفریب‬                 ‫‪٩‬‏ عدی‬     ‫است‬   ‫و کی درخور‬       ‫هی زد‬     ‫که کسا‬

 ‫خوردن ازکی ‪ -‬ودرعین شادی غم‌پیش آمدن‌را‬                                                             ‫می زسد ‪.‬‬
                                         ‫نز گوند ‪۰‬‬
                                                              ‫از نتوشدن‬          ‫در کشیدن ه کنابه‬
 ‫در ليك ‪ = 3‬یکراول ولام وسکون‬                             ‫محو کردن ‪ -‬و رد نمودن‬               ‫‪-‬‬   ‫و سر کدن‬
 ‫ثالی و تحتالی و کاف» به‌عنی‌در (اكاست کدقبای پیش‬                                                      ‫باشد‪¥ .‬‬
                           ‫واز آستن کوناه باشد ‪۶#.‬‬
                                                          ‫‪ -‬باکاف فارسی بروزن دختر »‬           ‫در گر‬
‫در ها ۔ بروزن سرما » خ رکوش را‬                                                             ‫درود کررگاویند ‪.‬‬
                                           ‫گومنت ‪:‬‬        ‫در لاله = بفح اول و صکون ثالی‬
=== leaf 301
 ‫دروا‬                                                                                                      ‫ب‪۱‬ح‬


‫گونشد‪ -‬و نمعتی وقت‬      ‫‪ ۹۳‬وهللا کت راز‬    ‫ومحنت ‪6‬‬         ‫ين‬
                                                            ‫اول و فستح‬              ‫در مسرا اتاک‬
‫وساعت وزمان باشد ‪ - ۱‬ویم‌نی‌ئبات وآرام ‪١‬‏ ۔‬                             ‫باشد‬   ‫‪٤‬‏ دار المرب وضرانخانه‬   ‫می‌قطه(‪)۱‬‬

‫وتأخبرهم هت ‪ - 1‬وعالمآ خرت رانز کفته‌اند‪-‬‬
                                                          ‫‪-‬ف فارسی ‪ ۰‬صراف‬
                                                                        ‫دبرمنگ‌زفکنا‬
‫نمام ‪(۱۲‬‬       ‫درکات‬     ‫اشاره است‬     ‫و ترد موقن‬
                                                                                                         ‫را گویند ‪۱‬‬
 ‫محبوس‌ودن‪.‬‬     ‫بازماند گان و بقمد تغیدات وهمی‬
                                                           ‫درمل = بورزن بلبل » غله رکاویند‬
‫دنرگیدان‪ ۷‬د بکراول‪ .‬بعنی‌درنگه‬
                                                          ‫که هنوز خوب نرسیده باشد وآنرا بربان کنند‬
‫کردن است که ثبات و آرام ورز‪,‬دن ‪ -‬وتأخیر‬
                                                                                                          ‫وخور ند ‪.‬‬
                                       ‫کردن باشد ‪.‬‬
                                                          ‫در میان بودن = بمعئی در رهن ودر‬
‫نون‬     ‫بفتح‬     ‫زهادن =‬        ‫در ورد‬
                                                                                 ‫گروبودن باشد ‪.‬‬
‫و واو ک»نابه ازدرهم پیچیدن ‪ -‬و ینهان کردن‪-‬‬
‫و بی نام و تان ساختن ‪ -‬و در ‪-‬وراخ نهادن‬                   ‫درن = بالون وحرکت‌غیرمعلوم» زلورا‬
                                               ‫باشد ‪.‬‬
=== leaf 302
  ‫‪~A‬‬                                                                                              ‫حره اج‬

                                                      ‫فام سلاطین وبزرگان هندوستان است ‪ -‬وبمعنی‬
                                                      ‫درست وتحتیق هم‌آمده است‪ ۷‬؛ ودروای باضافة‬
                                                                                     ‫تسانی تدز گفته‌اند ‪۰‬‬
‫باشد کهبر دو طرف راه از برای شان فرسنگك‬
                                          ‫صاز لد ‪.‬‬    ‫درواخج ‪ = 5‬بفتح اول وسکون آخر‬
                                                      ‫قطه دار باشد » حالت برخاسن از‬              ‫که خای‬
 ‫درو انه = بر وزن پروانه ‪ ۰‬سوراخی‬
‫باشد که بربام خانه کنند واردیان برآن گذاشته‬            ‫بیماری باشد که بعربی نقاهت گوبند و‪-‬بمعنی‬
                                                      ‫شجاع و دلیر ‪ -‬و شجاعت ودلیری ‪ -‬و محکم‬
                            ‫برالوالد ویزیر ایند ‪.‬‬
                                                      ‫ومضبوط ایزنگدفتسهو‌ایمعنی‌بقین ودرست وتحقیق‬
 ‫درواه ‪ = 1‬بر وزن درگاه " بمعنی‬                      ‫همرت کهلقیض کمان باشد ‪ -‬و بمعنی درشتی‬
          ‫سرلگون ‪ -‬وحبران ‪ -‬وضروری باشد ‪*.‬‬            ‫؛ و بجای حرف‬        ‫و علظت نیز (‪ )۱‬آمده ات‬

 ‫دروابست ‪ = ۳‬بروزن ومعتی‌دریاست‬                       ‫تائی زای فارسی هم گفته‌اند ‪ -‬وعیب وعار رایز‬
                                                                                                  ‫ّي‬
             ‫باشد که ضروری ومایحتاج است ‪.‬‬
‫درو بطارس ‪ ۰ ۵‬بح اول و ثالی‬                           ‫درو ار ‪ - ۲‬بر وزن خروار » بمعنی‬
 ‫بواو رسیاه کوسربای ابجد (‪ )۳‬وطای حطی(‪)4‬‬              ‫درواب تاست که‌خروریومابستاح باشد‪.‬وسرگشته‬
 ‫ھا ن هر دو‬      ‫و ن‬    ‫ورای مکور‬      ‫بالف کشده‬
                                                                  ‫وسرنگون وحىراقرا همگویند ‪¥.‬‬

                                                      ‫بقتح اول ‪ 3‬سکون آخر‬            ‫از ‪۳‬‬       ‫درو‬
=== leaf 303
 ‫دروقیئون‬                                                                            ‫مرت‬
‫میگشاید وبعربی مبضم خوانند ‪ ۴‬؛ وباین ممثی‬     ‫استغفار واز انان سناش و دعا وحیوانات دیگر‬

‫بفتح اول همگفته‌اند ‪ -‬و با واو معروف درعربی‬    ‫تسبیح باشد ‪ -‬و نام روز پاجم امت از خمة‬
‫داغ وشاترا خوانند ‪ - 6‬و بکر اول بر وزن‬         ‫مترقةٌ سالهای ملکی ‪ -‬وماضی دروندن‌هم‌هست‬
‫وممنی درفش است که افزار دفش دوزان و امثال‬      ‫رد ‪ -‬وبا واو مجهول» چوب‬
                                                                     ‫یعتی غله را دکرز‬
‫آتیاباشد؟ ‪ -‬وطم روزجنکه را کهممته‌اند ‪-‬‬        ‫ودرخت وتخته باشد وچوب نراش را ازین جهت‬
‫وفوطه را یز کونند که درروزجنگه‌بربالای خود‬                          ‫برند ‪*. ۴‬‬    ‫وگ‬‫کود‬
                                                                                     ‫در‬
‫آهنین ودستار بندند ‪ -‬و بمعنی روشنی آهمده‬      ‫در ودن ؟ د بروز نکشودن‪.‬در وکردن‬
                                 ‫است ‪#. ۷‬‬
                                              ‫و بربدن غله باشد ‪ ۰‬و درو يدن هم باین معئی‬
                                                                                        ‫أت ‪.‬‬
‫درو فینون‪ -‬بفتح‌اول وثائیبواورسیده‬
‫وقاف مفتوح و تحتالی ساکن ولون بوواکشده‬         ‫دروش ‏ م اول و واو مجهول بر‬
‫متی ‪ ۸‬و بعنی‬
           ‫رتیواس‬
                ‫و بنون دیگر زده » لف‬           ‫نشتر<جام راگوبن دکه بدان رکه‬         ‫وزن صروش»‬


 ‫‪ - ۴‬دردخهة خطی «لفت محای شوشتر» متعاق‬                ‫» دروندنل ‪.‬‬   ‫‪ - ۷‬رك‪ :‬درودن‬
 ‫بكتابخانة علامه دهشدا لز آهده‪ :‬درود یمعتی جوب و تخته و درخت و از بجهت جوت تراش را‬

 ‫‪ - ۴‬از‪:‬درو ‪« ۵۲‬هوشمان‪۹۵‬ه» ‪٣‬‏ دن* بوندمصدری؟پاز دد‪ .0۲4 01‬کردی‬                ‫ند‪.‬‬
```


## [2026-09-05T18:09:52.146Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'درون' in p and 290<i<320:\n        import re\n        print('leaf',i,'printed~',i+543, p.count('درون'))\nEOF\necho \"=== leaf 304,305\"; for n in 304 305; do echo \"--- leaf $n (p~$((n+543)))\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' BQT_v2_pages.txt | head -30; done"
}
```


### [2026-09-05T18:09:54.071Z] TOOL RESULT

```
leaf 291 printed~ 834 1
leaf 292 printed~ 835 2
leaf 295 printed~ 838 1
leaf 296 printed~ 839 2
leaf 298 printed~ 841 1
leaf 303 printed~ 846 2
leaf 304 printed~ 847 8
leaf 305 printed~ 848 10
leaf 307 printed~ 850 1
=== leaf 304,305
--- leaf 304 (p~847)
 ‫)‪“1‬‬                                                                                                  ‫دروك‬




 ‫باشدا ‪ -‬ونام شهربست (‪ )۳‬درخراسان مابن مرو‬                ‫کوبند بونالی است » بمەنی نباتی کهبدرخت‬
‫وناکه‌آنها یز دوشپراند © ‪ -‬وینم اول پیمانة‬                ‫زیتون ماند لکن از بك کز کوناه تر میباشد‬
‫غله راء‌گوبند ‪ -‬و دعابی باشد که مفان درستایش‬             ‫وبر کش درازتر از برک زیتون امت وکل آن‬
‫خدابتمالی‌و ذرآخوانندویرخوردایها بدمند‪ .‬وبعداز‬            ‫سفید میشود ر تخم آن بمقدار کرسنة کوچك‬
‫آن‌بشورندا وهرچز که‌یر آن‌درون‌خوانده‌ودمیده‬              ‫میباشد و طبع آن همچوطبم بنرالینج (‪ )۱‬است‬
‫ند گوبند مشته شده و هرچیز تخوانده باشند‬
                                        ‫باش‬
                                                                   ‫واگ زیده خوزه یم کهلتز برد‬
‫تایشته یمنی‌ناخوانده " چه یشتن با نحتانی وشین‬             ‫دروك ‪ -‬م اول بروزن‌سلوك ه»یزم‬
‫قرشت (‪ )4‬وفوقاتی» بمعنی خواندن باشد بزبان‬                                             ‫پاريك رکاوبند ‪.‬‬
                                 ‫زند وپازند (‪. ۷ )۵‬‬       ‫در و گر = بض‌اول وثالی (‪ )۲‬وفتح‌کاف‬
‫درون اروده کنابه از صاحب دل‬                               ‫فارسی » مخفف درود گر الست که استاد چوب‬
               ‫وصاحب مجاهده باشدب و‬
‫کی را دگزونند که‬                                          ‫تراش باشد وبعربی‌تجار گوبند‪ -‬ویک اول وفاح‬
                         ‫دل مردمان بدست آ ورد ‪4۸‬‬         ‫ثالی‪ .‬شخصبکه غله میبرد ودروميکند ‪ ۴‬واو را‬
‫درو نج = بفتح اول و رابع و سکون‬
                                                                                ‫بعربی حصاد خوانند ‪. ۴‬‬
‫» ‪ ۰‬وآن دوای باشد‬            ‫جيم ‪ +‬معرب درو لك ات‬         ‫درون = بفتح اول » بمعنی اندرون ‪۴‬‬

   ‫(‪ )۳‬چك ‪ :‬شهری ه‌هت ‪۰‬‬                     ‫وئالی ‪۳‬‬      ‫)‪ (۲‬چك‪:‬‬         ‫بزراشیج ‪۰‬‬   ‫جك‪:‬‬      ‫)‪(۸‬‬


                                       ‫‪ :‬ژند و باژند ‪.‬‬   ‫(ه) چك‬          ‫(‪ )4‬چك ‪- :‬قرشت ‪.‬‬

          ‫‪. ۴‬از درو (هم‪( ۳ + ).‬یوند فاعلی و شنل ‪).‬‬                        ‫رك‪ :‬درود کر ‪.‬‬       ‫‪- ۱‬‬
--- leaf 305 (p~848)
  ‫دره‬                                                                                                                ‫ز‪6‬ح‬
                                                                                                                       ‫بی‬


 ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪- ۱ )۳‬‬                         ‫بشکل عقرب وببب آن درونج عفربی خوانندش‪.‬‬
 ‫کومان‌حلاجی رانیزکوبندا ؛ وم اول هم‌بدو‬                      ‫کرم وخشك‌است دردویم(‪ ۱)۰‬کز ندکی‌جانورانرا‬
  ‫ون‬
   ‫ک‪۳‬م)ا‬
       ‫معنی آخر است کقهوس قزح (‬                                ‫کوش اکر فدری از آن درمان‌خانه‬                         ‫افع است‬

                              ‫حلاجی ‪ ۷‬باشد ‪#.‬‬                  ‫بیاویزند از طاعون ایمن باشند‪ .‬و اکرسوراخ‬
                                                                ‫کنند ودرمیان هردوران زن حانملدهفآوریززند‬
 ‫درو لزه و درو یره ‪ ۵‬س با زای‬
                                                                                    ‫آن زن از آفتها محفوظ باشد ‪.‬‬
 ‫هوز و زای فارسی ‪ .‬هر دو آمده است برءزن‬
  ‫تحققه (‪ » )4‬بمعنی دربوزه کودایی باشد ‪9.‬‬                     ‫درو ند = بفتح‌اول بروزن فرزند »نام‬
                                                                ‫پهلوانی‌است ‪-‬ودام داروبی‌هم‌هست ‪ - ۱‬وچنکک‬
‫درو یش سلطان دل = شاره‌برور‬                                     ‫وقلاب رانیز کوبند وبعربی‌معالاق خوانند ‪ -‬وم‬
 ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
                               ‫وسلم باشد ‪.‬‬                                                                 ‫ویازند (‪ )۲‬؟ ‪.‬‬
 ‫دره = بفتح اول و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
 ‫کوسفند وغیرء باشد ‪ -‬کوشادکی ميان ده کوه‬                                                                    ‫ومنافق باشد ‪.‬‬
‫رکاپریبزند ‪٩‬‏ ؛ویتخفیف ثالی از همین معنی‬                        ‫؛صفر‬
                                                                   ‫‪ -۳‬بروزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
                                                                                                              ‫د‬
 ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
‫آنجا یخوش صورتی مشپورند و انارخوب درا لجا‬                       ‫که آنرا درونج عقربی گویند » و درونج معرب‬
                                                                                                    ‫زک‬
‫مدشود ‪ .-‬و ضاحمول و تشدید الی پوستی چند‬
```


## [2026-09-05T18:10:20.957Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==305' BQT_v2_pages.txt | tail -20"
}
```


### [2026-09-05T18:10:22.501Z] TOOL RESULT

```
   ‫بقلم نگارنده‬        ‫نهاد ند ‪«( €.‬مفدمة مرجم قدم ارداو برافنامه‪ .‬رك ‪:‬ارداوبرافنامه‬    ‫درون‬    ‫وان‬     ‫(یه)‬

                                       ‫‪- ۸‬صفتی ات خدای را بمعنی مربی باطن ‪:‬‬                         ‫‪. )+۲‬‬
                                                                                                        ‫ص‬
                   ‫بختای |‬       ‫رشد‬
                                   ‫خد بخ‬
                                       ‫ب خر‬
                                          ‫وی‬                       ‫ای درون برور برون ارای !‬
    ‫‪.‬‬    ‫‪٩°‬‏‬   ‫ص‬    ‫چاپ مدری‬    ‫حدبقه سنابی ‪.‬‬   ‫«‬

                         ‫‪: - ٩‬كر ‪,‬كنورد هنورد = ‪ 0۲0016‬جیزد« ‪‎‬صا ‪. ٩۲ :۳۸‬‬

                                                                                       ‫‪۳٩۸‬‏‬         ‫حه‬
                                                                                                     ‫صبهفاز‬
                                                                                                          ‫بق‬
        ‫‪۲‬طبری ‪ , 0۲61‬مازندرانی کنونی ‪ 0180۳0‬د«واژه‌نامه ‪, ۰۵۳۰‬گیلکی ‪ 80۳01‬؛ کذب‪:‬‬
                                                                               ‫‪.‬‬
                                                                       ‫سخن خلاف حققت » ضد راست ‪:‬‬
    ‫«کلتان ‪4۵٩‬‏ ‪.‬‬            ‫جهان دیده بسیارکوید درو غ‪.‬‬             ‫اکر راست میخواهی از من شنو‬
```


## [2026-09-05T18:10:30.666Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB drun/dron\"; grep -n \"drün\\|drun\\b\\|drön\\|draonah\" HUB.txt | head -10; echo \"=== NYB dron\"; grep -n \"drōn\\|dron\\b\\|draonah\" NYB_vol2_glossary.txt | head -10; echo \"=== LEW draco\"; grep -n \"^draco\\|draco,\" LEW_1910.txt | head; echo \"=== LAT draco\"; grep -n \"draco\" LAT.txt | head -5"
}
```


### [2026-09-05T18:10:30.760Z] TOOL RESULT

```
=== HUB drun/dron
4218:vdrun ^) perversus, miser ^= paz. awdrun 'irregular, wicked*
4230:ist paz. phi. frdrun Regular, right, exceUent*. War die altere Pehlevi-
4976:Gl. 64 — zd. draonah-; surun (surln) 'Hinterbacken' = zd.
=== NYB dron
=== LEW draco
=== LAT draco
3831:uipera, sans doute aussi coluber, colubra ; ou 1’emprunt au gr. draco.
5516:se en a fait un aasculin, d'aprbs anguis, draco. M.L.711; irL asf.
17733:draco, -onis «.: i° dragon; 3 0 serpent (poAt.). Emprunt latinisA an
17734:gr. Spaxwv, -ovtoC qui existe 6galenent en traascription; gin.dracontis,
17735:acc. dracontem, M. 1 . 3759 ; passA en germ.: T.h.a .trahho "Drache", etc.,
```


## [2026-09-05T18:10:32.858Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4970,4985p' HUB.txt; echo \"=== LAT draco full\"; sed -n '17730,17745p' LAT.txt"
}
```


### [2026-09-05T18:10:32.924Z] TOOL RESULT

```
Kapitel 6: ap. au.
§ 31. Ap. au {^' idg. aw, ew, ou) wird im Mp. und
Np. zu 0: roz Tag = ap. raudah- u. s. w.
§ 32. Ap. au = phi. 6 wird vor w, m im Paz. und
Np. zu U: gun^) *Farbe, Art und Weise' — p^z. jrim, gUna^
arm. goin^ zd. gaona- ; paz. driew 'a consecrated cake' Min.
Gl. 64 — zd. draonah-; surun (surln) 'Hinterbacken' = zd.
sraoni"^ Faredunf i^^?., Fredun, arm, Hruden (sassanidisch,
aus *Hredun umgestellt) = zd. &ra^iaona-\ mUm 'Wachs',
arm. mom (5. Jhd.); rum (bei Vullers rom) 'Schamhaare*
= skr. rdman-; hum 'Homapflanze' (vgl. hUm bei Mu-
waffaq p. 268, s. Horn Nr. 1113) = paz. hum Min. Gl.
106, zd. haoma-, Vgl. auch Bum *das byzantinische Reich'
(reimt auf bum Fird. I, 403) =' Poi/nT], lat. Roma, — Ausser-
dem ist altes o z\i U geworden in : samur 'Zobel' = parth.
aifuoo (de Lag. G. A. 71, 226), arm. samoir (= phi. ^samor)
=== LAT draco full
dos, dotis: v. do.
doslnus, -a, -uni; gris cendre. Epithfete de la robe des chevaux,
attestee en bas latin (isid., Glos.), d'origine germanique. M.1.3755a.
draco, -onis «.: i° dragon; 3 0 serpent (poAt.). Emprunt latinisA an
gr. Spaxwv, -ovtoC qui existe 6galenent en traascription; gin.dracontis,
acc. dracontem, M. 1 . 3759 ; passA en germ.: T.h.a .trahho "Drache", etc.,
et celt.: iri. drac, britt. draig.
D6rive: dracunculus: 1° petit dragon; 3° poisson venimeux; 3 0 estragon.
Cf.M.l.3760. V. fr.draoncle "abcbs, tumear".
dracuma,-ae f. : drachme. Emprunt oral, ancien au gr. Spa^Gii^, usit6
dans la l.des comiques; pour 1 'epenthbse de u, cf. Tecumessa.
Deriv6: drac (hjumisso,-as (Pl.). - Derive tardif et savant: drachmdlis
(Cass.Pel. ); Passe en gotique: drakma (savant).
drappus, -I m.: chiffon. Mot bas latin (Orib., Vie de Cesaire,
Not. Tir . ), peut-etre gaulois; cf. les noms propres Drappo, Drappus,
Drappes, Draponus. M.1.3765.
```


## [2026-09-05T18:10:53.737Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 120 -l 120 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg120_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg120_400.png'); print(im.size)\nW,H=im.size\n# fraction based on 1700x2200 base: box approx x 455-720, y 975-1005 of 1700x2200\nc=im.crop((int(0.26*W),int(0.435*H),int(0.45*W),int(0.465*H))).resize((int(0.19*W*2),int(0.03*H*2)))\nc.save('c_latin120.png')\nc2=im.crop((int(0.20*W),int(0.135*H),int(0.72*W),int(0.17*H)))\nc2.save('c_avestan120.png')\n\"; ls -la c_latin120.png c_avestan120.png"
}
```


### [2026-09-05T18:10:57.092Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb  5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb 13469 Sep  5 14:10 c_latin120.png
```


## [2026-09-05T18:10:59.015Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_latin120.png"
}
```


### [2026-09-05T18:10:59.035Z] TOOL RESULT

```

```


## [2026-09-05T18:11:08.712Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_avestan120.png"
}
```


### [2026-09-05T18:11:08.729Z] TOOL RESULT

```

```


## [2026-09-05T18:11:20.278Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DEV estragon\"; grep -n -i \"estragon\\|targon\" DEV.txt PHN.txt | head -10; echo \"=== AFM tarkhun\"; grep -n \"طرخون\" AFM.txt AFM_pages.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10; echo \"=== PLA\"; grep -n -i \"tarhun\\|ṭarḫūn\\|tarḫūn\\|طرخون\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5; echo \"=== ARY\"; grep -n \"ترخون\\|درون\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== RCH\"; grep -n \"tarkhun\\|طرخون\" RCH.txt | head -5"
}
```


### [2026-09-05T18:11:20.434Z] TOOL RESULT

```
=== DEV estragon
DEV.txt:65:Telle  quelle,  notre  tâche   était  suffisante;   et  le présent  volume,  nous  l'avouons  en  toute  humilité, n'a  pas  laissé  de  nous  coûter  un  long  et  persévérant travail.  Prenant  pour  base  les  publications  de  nos devanciers,  nous  y  avons  joint  les  résultats  de  nos recherches  personnelles  pendant  plusieurs  années. Aussi  trouvera-t-on  dans   ce  dictionnaire  plus   de cent  articles  sur  des  mots  dont  l'origine  orientale n'avait  jamais  été   établie  :  les   uns  peu  connus, comme  alizari,  auffe,  alquifoux,  bédégar,  ciiine,  ché- hule,  nizeré,  gamache,  orcanète,   etc.;   d'autres  plus généralement  usités,  tels  que  épinard,  estragon,  far- deau, gâche,  moise,  moire,  houle,  mortaise,  etc.  Nous avons  combattu  ou  confirmé,  à  l'aide  d'arguments nouveaux,  les  hypothèses  précédemment  émises  sur des  termes  comme  artichaut,  arsenal,  avanie,  avarie, caraque,    escarpin,    nuque,   siroc,    etc.   L'examen  de quelques  ouvrages  scientifiques  arabes,  dont  les  tra- ductions latines   étaient  fort  répandues  au  moyen âge,  mais  dont  le  texte  arabe  n'a  jamais  été  publié,
DEV.txt:1288:Estragon.  Esp.  estragon,  taragona,  portug.  esiragâo,  ital. largone.  On  a  voulu  tirer  ces  mots  du  latin  draconem^ , (Iraco  étant  supposé  employé  dans  le  sens  de  dracuncidus , nom  d'une  plante  dans  Pline,  tdequel ,  dit  M.  Littré,  ne paraît  pas  avoir  été  donné  à  l'estragon,  mais  que  les  bo- tanistes lui  ont  appliqué.  ??  Sans  parler  de  ce  qu'il  y  a  de bizarre  dans  cette  dérivation,  historiquement  parlant,  on trouvera  assurément  quelques  difficultés  phonétiques  à tirer  estragon  de  draconem.  Ce  serait  le  seul  exemple  de  dr latin  devenu  tr  en  français.  Aussi  faut-il  chercher  ailleurs la  vraie  dérivation.  Les  formes  taragona,  targone,  anc.  fr. tragon'^^  nous  ramènent  a  l'arabe-pcrsan  ,jyi^J^  tarkhoUn , mot  qu'on   trouve   dans  Ibn-Beithar,   dans  Avicenne   et
DEV.txt:1293:Nos  anciens  botanistes  écrivaient  iarcon  ou  tarchon;  cette dernière  orthographe  est  celle  de  Gesner,  qui  a  donné  le nom  de  tarchon  sauvage  à  ïAchUlea ptannica^.  Vaillant,  un siècle  et  demi  plus  tard,  a  appelé  tarchonante,  tarchonan- thus,  un  arbrisseau  d'Afrique  dont  les  fleurs  ont  quelque rapport  avec  celles,  de  l'estragon  [tarchon,  oivOosy
DEV.txt:1294:En  dernière  analyse,  il  peut  se  faire  que  tarkhoûn  ait été  emprunté  par  les  Arabes  au  grec  SpoLKwv,  et  que,  par suite,  ceuv  qui  tirent  estragon  de  draconem  ne  se  trompent qu'à  moitié.  Dans  tous  les  cas,  je  signale  le  mot  à  l'atten- tion de  M.  Dozy,  qui  ne  l'a  pas  inséré  dans  son  Glossaire. La  syllabe  initiale  es  dans  estragon  et  estragâo  pourrait  être l'article  arabe  eJ,  et  défiguré  par  suite  de  la  prononciation emphatique  du  h  t.
DEV.txt:1494:'  Gtsner  comiaissail  ia  lan(>ae  arabe ,  ainsi  qu'il  a  été  dit  précédemment (art.  estragon).  J'ajouterai  que  l'iiarmale  n'est  pas  mentionné  dans  ceux  des aiuidotaiies  latins  du  moyen  âge  qui  n'ont  pas  fait  d'emprunts  aux  Arabes, (  Voy.  par  exemple  le  man.  n"  7009  anc.  fonds  de  la  Bibl.  nat.)  Voir  toutefois le  passage  mentionné  dans  le  Thcsaur.  d'Henri  Estienne  :  Brjo-aaa,  a-népyLOt. Se  êaliv  èv  ^vpia.  yevvœ^evov  toU  àypiov  is-nyiivov,  6  §y)  cî  èvioiitoi  à'pfiaAa xaAoùoiv.  (Edit.  Didot.)
DEV.txt:3369:Dracunlium,  lat.  voy.  Estragon.
DEV.txt:3373:IpoLKÔvTiov,  voy.  Estragon.
DEV.txt:3374:ApixKCûv,  voy.  Estragon.
DEV.txt:4407:Tarchon,  voy.  Estragon. Tarcbonante,  voy.  Estragon. Tarchonanlbus,  lat.  bol.  voy.  Estra- gon. Tarcon,  voy.  Estragon. Tare.
DEV.txt:4409:Targone,ùa/.  voy.  Estragon. Targum,  voy.  Drogman. Tari,  vov.  Téréniabin. Tarif.
=== AFM tarkhun
AFM_pages.txt:2856:( الطرخون ) نبات ُيَكْبّس في ܐܘ والملح واللبن واصل عروقه العاقر قرعا معرب
AFM.txt:4579:( الطرخون ) نبات ُيَكْبّس في ܐܘ والملح واللبن واصل عروقه العاقر قرعا معرب 
=== PLA
=== ARY
325:در درون گور ساخته شده از سنگه‌های تراشیده شده قرار دارند و روی گور تپه‌ی کوچکی
701:و تپه‌های کوچکی بر فراز آنها قرار دارد. در درون آنها استخوان انسان و اسب و گهگاه اجاقی و اسلحه
1658:چم اين واژه در آزبان‌هایاژرمی: نگرانی» عذاب درونی؛ دلواپسی» تنگ» تنگنا.
2682:۴ اندر اندرون
2716:۱- واژه‌ی "اندرونه" از پیشنهادهای فرهنگستان ایران است ولی با واژه‌های پیشین ایرانی خویشی و هماهنگی دارد.
=== RCH
56636:tarkhashkuHy  Wild  endive. tar khaf  (or  liskjiff  tarkhafat)y  Thin  butter. AP^ys>-JL  tarkhun  (or^^^^  tarkht)y  Tarragon,  or  dracun- culus hortensis  (an  herb).
69468:Aj^  kazaz  (from J^)y  Being  dry,  contracted.  Avarice, p   kaztarkhuny  Pellitory.  Dracunculiis.
69511:p   kajtarkhun^  Pellilory.  Drncunculus.
```


## [2026-09-05T18:11:31.557Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4575,4585p' AFM.txt; echo \"=== AFM leaf\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'الطرخون' in p: print('leaf',i)\nEOF"
}
```


### [2026-09-05T18:11:33.251Z] TOOL RESULT

```
الطرخانية الى من يردي خدمة جلية عظيمة للدولة ٠فنكان‏ يصبح بذلك معائى من 
كل الوسجوه ومعزّزًا ومكرما عند السلطان أكثر من الجميع ٠‏ وكان ܦܕ اي السلطان 
يغمض العين عن نقائصه ويحيب الى جميع التّاساته > 

( الطرخون ) نبات ُيَكْبّس في ܐܘ والملح واللبن واصل عروقه العاقر قرعا معرب 
عن بر خون 

* (الطرزرأن) 530 48 والطرنيان لغة فيه 

(الطراز» عَلم الثرن عاب تراز 

=== AFM leaf
leaf 113
```


## [2026-09-05T18:11:47.150Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 der- run\"; grep -n \"draonah\\|dromos\\|δρόμος\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"--- WLD Bd1 795\"; grep -n \"tredan\\|trada\\|draviṇa\\|dravina\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8; echo \"=== IEC\"; grep -n \"^dromos\\|drómos\\|derk-\\|drakon\" IEC.txt | head -8; echo \"=== SYN run\"; grep -n -i \"dromos\" SYN.txt | head -5; echo \"=== FSD tarragon\"; grep -n -i \"tarragon\" FSD_vol4.txt | head -3; echo \"=== WEB dragon\"; grep -n \"^dragon\\b\" WEB_vol1.txt | head -3"
}
```


### [2026-09-05T18:11:47.297Z] TOOL RESULT

```
=== WLD Bd1 der- run
50166:dravinas- n. ,.Gut, Yermogen", av. draonah- n. ,,bei der Besitzverteilung 
--- WLD Bd1 795
50165:„von Aesma her anlaufend, zum Angriff entsendet"' (ob auch ai. dravina-m , 
50166:dravinas- n. ,.Gut, Yermogen", av. draonah- n. ,,bei der Besitzverteilung 
50185:anord. troda , trad ds. ; as. ags. tredan , ahd. tretan „treten“ (bei Osthoffs 
50187:trada ,,Tritt, Spur 1 , ags. trod n., trodu f. „Spur, Weg“ (engl. trade „Handel“ 
=== IEC
2471:dromos ‘course, way’. WP I, 796 Skt. cf. dram- ‘to run’; Gk. drómos; LG tram ‘rung of ladder’; OE. trem ‘footstep’; Norw. tram ‘threshold’
2533:drktis “seeing, sight, brightness? Cf. derk-, dork-, drk- & WP I, 806 Skt. drstih; Av. (o-gde) darstis; Alb. dritë ‘light’; MIr. cf. drithle ‘flash’; OBr. cf. -drichet- ‘scope’; OHG zorcht, zoraht, adj. ‘bright; OS torht, id. OE torht (id. & *brightness")
=== SYN run
=== FSD tarragon
30842:tar'a-gon,  n   Same  as  tarragon
30900:‘   of  tarragon  vinegar  Compare  tarragov
37253:tor'so*,n  Arch  A   column  with  a   twisted  shaft  [<  torse*, n]  Tor-to'la*,  1   ter-tO'la,  2   t6r-t6'la,  n   One  of  the  Virgin tor"so-clu'slon,  1   ter'so-klfl'aan,  2   tOr  so-cly'zhon,  n   Islands  British  West  Indies,  24  sq  m   capital  Roadtown Surg  A   cupressure  In  which  the  needle  Is  Inserted  parallel  Tor-to'sa,  1   tor-tfi'sa,  2   tor-tO'sa,  n   A   fortified  town  In with  the  artery,  then  twisted  across  it,  and  confined  [<  Tarragona prov ince  Spain
=== WEB dragon
```


## [2026-09-05T18:11:56.340Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tar.ra.gon\" FSD_vol4.txt | head -5; echo \"---\"; sed -n '30895,30905p' FSD_vol4.txt"
}
```


### [2026-09-05T18:11:56.574Z] TOOL RESULT

```
---
tar-na'flon,  ltar-n6'^an.2tar-n5'8hon,a  &adv  [Dial  &   cultivated  for  the  sake  of  its  aromatic  leaves,  which  are Slang  I   A   semiprofane  epithet  similar  to  tarnat,  as,  forna-  '   '   .   .   ,   .
lion  slow  (Cor  of  damnation  I
The  lungs  of  mi  soul  begin  to  play  after  having  been  all  but asphyxiated  mth  tarnation  folb  Mrs  Cajii.yi.e  m   Froude’a jane  ir  Carfvfe\oI  u,  p   90  (a  18S3  I Tarn''*et*Ga''ronne',  1   tam'-C-go'rfin',  2   tSm'-e-ua  rOn',  n A   department  In  S   W   France,  1,440  sq  m   capital
used  for  seasomng  salads  and  in  the  preparation  of tarrag^'n  vinegar  and  oil  [<  OF  targon,  <   Ar. tZT^hiin  <   Or  drakon,  see  dragon]
Tar''ra-go'’na,  1   tdr'ra-gO'na,  2   tar'ra-g5'na,  n   1.  A   coast province  in  N   E   Spain,  2,505  sq  m   2.  Its  capital,  the Mon-  ancient Tarraco.  sometimes  eironeouslj  cited  as  thesource
‘   of  tarragon  vinegar  Compare  tarragov
t   T'rt  looaon  Tar'raut,  1   tar'ant,  2   tfiriant,  n   A   county  In  N   central
A»  AO  T*PTf»Q-  DOO  an  m   rniintt  .cppr  TTnrr
tauban
tar'nlsh,  1   t^'m^,  2   tflr'msh,  r   I.  t   ±.  lo  lesaeu  Texas.  900  sq  m   .   countj -seat,  Fort  Worth or  destroy  the  luster  of  in  anj  way,  as  by  soiling  or  by  Tar^ra-sI'I-dse,  1   tar'a-sal'i-dl.  2   tSr’a-sli-dP  n   pi  Jeh destrojung  the  polish  said  cspeciallj  of  alight  chemical  a   Carboniferous  famllj  of  crossopterjglan  fishes  with  axo- action  of  the  atmosphere  or  the  gases  contained  in  it  nosts  and  baseosta  of  median  fins  In  simple  regular  series
2.  Figuratively,  to  dimimsh  or  destroy  the  punty  of;  fewer  than  fln-ra>s  Tar-ra'sl-us,  n   (t  g   )   [<  Tarrasa,
```


## [2026-09-05T18:12:09.171Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.avesta.org/ritual/rcc15.htm",
 "prompt": "Quote what this page says about the word drōn/darun: its Avestan origin (draonah-), meaning 'portion', and the ritual bread."
}
```


## [2026-09-05T18:12:10.960Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%AC%CE%BA%CF%89%CE%BD",
 "prompt": "Ancient Greek δράκων: etymology (from δέρκομαι, PIE *derḱ-), meaning, and descendants (Latin draco, Arabic?)."
}
```


### [2026-09-05T18:12:14.416Z] TOOL RESULT

```
# Dron: Avestan Origin and Meaning

The page explains that **dron** derives from the Avestan term **draonah**, which means **'portion, possession'**. 

Regarding the ritual bread itself, the text describes it as follows: "Dron (Av. _draonah_, lit. 'portion, possession') refers to 'round, sacred unleavened breads made of wheat flour with nine cuts in the middle.'"

The page notes these breads are flexible, approximately palm-sized, and feature three rows of three marks made before frying while reciting "humat, hukht, huvarsht" (one word per cut). The dron ritual functions as "an act of blessing and thanksgiving for our food."
```


### [2026-09-05T18:12:16.882Z] TOOL RESULT

```
# δράκων (Dragon) - Etymology and Meaning

## Etymology
The Ancient Greek word δράκων (drắkōn) is traditionally connected to δέρκομαι (dérkomai), meaning "to see." The literal sense is interpreted as **"one who stares"** or **"sharp-sighted."**

## Meaning
The noun has two primary definitions:
1. A dragon or serpent
2. A serpent-shaped bracelet

## Linguistic Descendants
The word spread across numerous languages through Greek's historical influence:

- **Romance languages**: Latin *dracō* (leading to Romance language variants)
- **Slavic languages**: Russian дракон (drakon), Ukrainian дракон, Bulgarian дракон, Belarusian дракон
- **Other European languages**: Armenian դրակոն, Georgian დრაკონი, Hebrew דרקון
- **Ancient languages**: Classical Syriac ܕܪܩܘܢܐ, Coptic ⲇⲣⲁⲕⲱⲛ

The word's pervasiveness across Indo-European and Mediterranean languages demonstrates its deep cultural significance in describing the mythological creature.
```


## [2026-09-05T18:12:23.412Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/tarragon' \\\n 'https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%AE%D9%88%D9%86' \\\n 'https://www.etymonline.com/word/tarragon' \\\n 'https://www.etymonline.com/word/dragon' \\\n 'https://www.etymonline.com/word/tread' \\\n 'https://www.etymonline.com/word/trade' \\\n 'https://www.etymonline.com/word/trap' \\\n 'https://www.etymonline.com/word/trip' \\\n 'https://www.etymonline.com/word/syndrome' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der%E1%B8%B1-' \\\n 'https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%AC%CE%BA%CF%89%CE%BD' \\\n 'https://www.avesta.org/ritual/rcc15.htm' ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 120 (book p.90), roots Der 2/Deru 2 and Derk: tarragon/dragon/tread chain and Av. draonah- > drōn\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-05T18:12:29.316Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/84d3825b1c67643f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e7dfb4fb27047a77.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b37ce8b6492525b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e1a2269ff127674.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/434bd1622c1ac58a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b5de67f2cc5d4b9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55b81fdd47d59d6a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f312f6f8d2bfa948.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9fab172bb82fa40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24a784742966b88d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb18a6dc15f4b2c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e2c0dee9fec4d2f.txt
```


## [2026-09-05T18:12:33.640Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg120.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/120.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head; echo \"=== verify_check help\"; sed -n '1,50p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T18:12:33.732Z] TOOL RESULT

```
total 3552
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 14:12 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
=== verify_check help
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
```


## [2026-09-05T18:12:36.240Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '50,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T18:12:36.287Z] TOOL RESULT

```
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


## [2026-09-05T18:12:40.062Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls page-11*.json 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('page-118.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:1800])\n\""
}
```


### [2026-09-05T18:12:41.545Z] TOOL RESULT

```
Exit code 1
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
Traceback (most recent call last):
  File "<string>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'page-118.json'
```


## [2026-09-05T18:12:43.932Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json;d=json.load(open('page-116.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2000])\n\""
}
```


### [2026-09-05T18:12:46.230Z] TOOL RESULT

```
{"pdf_page": 116, "book_page": 86, "verified_by": "claude-opus-5", "verified_on": "2026-09-05"}
{
 "id": 1,
 "lang": "Avestan",
 "words": "daraga, daragâ, drâjah; drang",
 "verdict": "plausible",
 "derivation": "Gathic Avestan daraga-, Younger Avestan darəγa- 'long' (fem. darəγā-) is the regular Iranian outcome of PIE *dl̥h1ghós: syllabic *l̥ > Ir. ar, and the voiced aspirate *gh > Av. g/γ intervocalically (Bartholomae AiWb 693 s.v. 'd. p. darga-, g. daraga-, j. darəγa- Adj. (fem. °γā-) \"lang\"'). Beside it Avestan has the s-stem drāj- / drājah- 'length, extent' (only in compounds such as ayarə.drājah- 'the duration of a day', asə.drājahyehe, mazdrājah-), the zero-grade *dr̥Hǰ-as- of the same root, which is the ancestor of NP derāz. The third word Nourai lists here, drang 'hesitation', is the problem: Bartholomae's two Avestan verbs drang- are '1drang- V. firmare' and '2drang- V. \"auswendig lernen\"' (to fix, to learn by heart) - not 'hesitation'; the form with the sense 'delay, period of time' is Middle Persian drang (Pokorny explicitly files it under */d/longho-s: 'Middle Persian drang, npers. dirang'), and Wiktionary derives NP درنگ from MP dlng' (drang) 'period, duration' via Old Persian, not from Avestan. Nourai's source for putting drang in the Avestan box is Tavoosi (SNS 324), who does refer the Pahlavi word back to Av. drang- (AiWb 772); that is a defensible but minority link, so: forms 1-3 confirmed, drang mislabelled Avestan and mis-glossed.",
 "derivation_fa": "اوستایی daraga- (گاهانی) / darəγa- (اوستای نو) «دراز» بازتاب منظم ایرانی *dl̥h₁gʰós هندواروپایی است: لِ هجایی به ar بدل شده و *gʰ در میان دو واکه در اوستایی g/γ داده است (بارتولمه، ستون ۶۹۳). در کنار آن ستاک drāj-/drājah- «درازا، امتداد» (تنها در ترکیب‌هایی چون ayarə.drājah- «درازای یک روز») هست که پایهٔ «دراز» فارسی است. اما واژهٔ سوم، drang «درنگ»، جای چون‌وچرا دارد: بارتولمه دو فعل اوستایی drang- را «استوار کردن» و «از بر کردن» معنی می‌کند، نه «درنگ»؛ صورتی که معنی «مدت، درنگ» دارد فارسی میانهٔ drang است و پوکورنی هم آن را زیر *dlongʰos آورده است («فارسی میانه drang، فارسی نو dirang»). ط
```


## [2026-09-05T18:14:05.782Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD leaf\"; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'طرخان' in p or 'طرطير' in p or 'طرخ' in p: print('leaf',i, p[:80].replace('\\n',' '))\nEOF\necho \"=== LEW draco\"; grep -n \"draco\" LEW_1910.txt | head -5; echo \"=== SKT trade/tread\"; grep -n \"^trade\\|^tread\\|^trap\\|^trip\" SKT.txt | head -6"
}
```


### [2026-09-05T18:14:07.786Z] TOOL RESULT

```
=== TAD leaf
leaf 49 ‫‪50‬‬          ‫طاولة ‪ 9‬س ايطالى ‪ 21002‬ممناه فى الاصل لوح ولوحةنمار‬  ‫قوام
=== LEW draco
=== SKT trade/tread
20057:trap  (d),  a  kind  of  igneous  rock.  (Scand.) Swcd.  trappa,  a  stair,  'irapp,  trap-rock; Man.  trappi,  stnir,  trap,  trap-rock,  So called  from  its  appearance ;  lu  tabular masses  seem  to  rise  in  steps.
20058:trapan,  trepan  {_i),  to  ensnare.  (F.  • O.  H.  G.)  Formerly  trapan.  -  O.  F.  trap^ pan.  trapoMt,  a  snare,  trap  (Roquefort). rrob.  for  trapant*,  prcs.  pt.  of  O.  K.  traptr^ trapper,  to  trap  (from  which  it  is,  in  any case,  derived).  — F.//-fl//rf,  airap.  — O.H.G. tr^po,  A  trap  (above).
20149:triplicate,  threefold.    (L.)     From of  L.  triplicart,  to  trcUe.  — U  fr»-, pUcart,  to  weave,  fold;  tec  Plr.
20150:tripod.   (U-Gk.)    L./- tripus.  —  Gk.   rpiwijvt    (steu. tripod,    three-footed    brais    ItUlc,   i^ legged  table.  — Gk.  rf^-.  three;  ••lii,  fts sec  Foot.
```


## [2026-09-05T18:14:15.069Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==50' TAD_pages.txt | grep -n \"طرخون\\|طرخان\" ; echo \"---head\"; awk 'BEGIN{RS=\"\\f\"} NR==50' TAD_pages.txt | head -6"
}
```


### [2026-09-05T18:14:16.853Z] TOOL RESULT

```
11:           ‫طرخان ‪ --‬فارسي « ترخان‪ 6‬وهو زعم قوم معفى من الضراشب‬
---head
‫‪50‬‬          ‫طاولة ‪ 9‬س ايطالى ‪ 21002‬ممناه فى الاصل لوح ولوحةنمار‬
 ‫قوامكولأوا عامها طعامهممرادفبامائدةومنضدة ولووحلةع‪.‬بة الطاولة اعلنعدامة‬
                                                                           ‫مرادفها تراد‬
‫يو‪-‬نفاى‪:‬ئ‪.‬ية ‪ 65024‬لهخنةدية حمينثشأ هذا الطائر اعجيب‬
                                                   ‫‪6‬ولوس‬
                                                       ‫طاا‬
```


## [2026-09-05T18:14:25.486Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A6 \"^tread, intr\" KLN_1971.txt | head -14; echo ===; grep -n -A5 \"^trade, n\" KLN_1971.txt | head -10; echo ===; grep -n -A4 \"^-drome\\|^dromedary\" KLN_1971.txt | head -12"
}
```


### [2026-09-05T18:14:25.556Z] TOOL RESULT

```
Exit code 1
252141:tread, intr. and tr. v. — ME. treden, fr. OE. tre- 
252142-dariy rel. to OS. tredan, , OFris. ireda, OHG. tre- 
252143-tan , MHG., G. t re ten, ON. fro da, Dafti. trxde, 
252144-Swed. trdda , Norw. traa Goth, trudan, ‘to 
252145-tread’, OHG. trotton , of s.m., MHG. trotten , ‘to 
252146-run’. Cp. F. trotter , It. trottare , OProven?. Sp. 
252147-and Port, trotar, ‘to trot*, which are borrowed 
(eval):1: == not found
```


## [2026-09-05T18:14:28.391Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '252147,252160p' KLN_1971.txt; echo \"=== trade\"; grep -n \"^trade, n\" KLN_1971.txt; sed -n \"$(grep -n '^trade, n' KLN_1971.txt | head -1 | cut -d: -f1),+8p\" KLN_1971.txt; echo \"=== -drome\"; grep -n \"^-drome\\|^drome\" KLN_1971.txt | head -4"
}
```


### [2026-09-05T18:14:30.151Z] TOOL RESULT

```
and Port, trotar, ‘to trot*, which are borrowed 
fr. OHG. trotton , and see trot. Cp. also trade, 
treadle . 

Derivatives: tread , n., tread-er , n., tread-ing , n. 
treadle, n. — ME. tredyl, ‘a step (to mount by)’, 
fr. OE. tredel, which is formed with instrumen- 
tal suff. -e/, fr. tredan , ‘to tread’. See prec. word 
and instrumental suff. -le. 

Derivative: treadle , tr. and intr. v. 
treason, n. — ME. tresun , treisun, traisoun (F. 
froArion), fr. L. traditionem , acc. of traditio , *a 
giving up, delivering up, surrender’. See tradi- 
=== trade
251025:trade, n. — ME. ‘path, track, course’, fr. MLG. 
trade, n. — ME. ‘path, track, course’, fr. MLG. 
trade, of s.m., which is rel. to OS. trada , OHG. 
trata, of s.m., and to E. tread. 

Derivatives: trade, tr. and intr. v., trad-er, n., 
trad-ing , n. 

Tradescantia, n., a genus of plants, the spidewort 
{bot.) — ModL., named after John Tradescant, 
=== -drome
7907:dromedary. 
14056:dromedary and cp. catadromous. For E. -ous, as 
76663:-drome, combining form lit. meaning ‘running, 
76671:dromedary, n. — OF. dromedaire (F. dromadairej ,
```


## [2026-09-05T18:14:31.926Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '76663,76680p' KLN_1971.txt"
}
```


### [2026-09-05T18:14:31.991Z] TOOL RESULT

```
-drome, combining form lit. meaning ‘running, 
course’, as in aerodrome. — Gk. -8popto<;, fr. 
8p6pto<;, ‘a running, course, race, racecourse’. 



See dromedary. 

dromedary, n. — OF. dromedaire (F. dromadairej , 
fr. Late L. dromeddrius (came/us), fr. dronrns , 
gen. - adis , ‘running’, fr. Gk. 8po(xa<;, gen. -a8o<;, 
of s.m., which is rel. to Spocpielv, ‘to run’, 
8e8pop.a, ‘I ran’, Spopioq, ‘a running, course, 
race, racecourse’, fr. l.-E. base *drem ‘to run’, 
whence also Ol. dramati, ‘runs’. Base *drem- is a 
collateral form of base ‘to move quickly, to 
run’, whence OI. drdti, ‘runs, hastens’, Gk. 0:71081- 
Spsaxetv, ‘to run away’ (with reduplication of
```


## [2026-09-05T18:20:49.710Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk120.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\ndata = {\n \"pdf_page\": 120,\n \"book_page\": 90,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Der 2, Deru 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *der- (Pokorny '(der-3), drā-, dreb-, drem-, dreu-') 'to run, walk, step'\",\n   \"note\": (\"Pokorny IEW pp. 204-206 heads the entry 'Root/lemma: (der-3), dra-, dreb-, drem-, dreu-. \"\n            \"Meaning: to run', so Nourai's POK:205 falls inside it and the gloss 'to run' is Pokorny's own. \"\n            \"Watkins (AHD IE appendix) files the same material as der-1, 'Assumed base of roots meaning \\\"to run, \"\n            \"walk, step\\\"' [Pok. 3. (der-) 204], with exactly the derivatives Nourai draws (tread/trade/trap/trip \"\n            \"from Germanic *tred-/*trep-, Greek dromos from *drem-). The numbering 'Der 2, Deru 2' is Nourai's own \"\n            \"book-internal one, kept apart from his Der 1 ('to split, skin' = Pok. der- 206-211) and Deru 1 \"\n            \"('tree' = Pok. deru- 214-217); it is not Pokorny's numbering, where this root is der-3. \"\n            \"Root, language label and gloss are all correct.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *der-/*drem-/*dreu- «دویدن، گام برداشتن» است که پوکورنی آن را در صفحه‌های \"\n               \"۲۰۴ تا ۲۰۶ فرهنگ ریشه‌شناختی خود زیر «(der-3), drā-, dreb-, drem-, dreu-» با معنی «to run» آورده \"\n               \"است؛ پس ارجاع نورایی (پوکورنی ۲۰۵) درست و در محدودهٔ همان مدخل است. واتکینز در پیوست ریشه‌های \"\n               \"هندواروپایی فرهنگ American Heritage همین ماده را der-1 می‌نامد و همان مشتق‌هایی را می‌آورد که \"\n               \"نورایی رسم کرده است. شماره‌گذاری «Der 2, Deru 2» از خود نورایی است و با شماره‌گذاری پوکورنی \"\n               \"(der-3) یکی نیست؛ در مجموع ریشه، برچسب زبانی و معنی درست‌اند.\"),\n   \"sources\": [\"https://www.etymonline.com/word/tread\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:205\", \"status\": \"supports\",\n     \"note\": (\"POK_full.txt (indo-european.info dump) block 'Root / lemma: (der-3), dra-, dreb- drem-, dreu- / \"\n              \"Meaning: to run ... Page(s): 204-206'; page 205 is inside the entry. The same block carries the \"\n              \"Avestan and Germanic material Nourai uses (grep -n 'Page(s): 204-206' POK_full.txt).\")}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW I 204-206, '(der-3), drā-, dreb-, drem-, dreu-'\", \"stance\": \"supports\",\n     \"note\": \"'Meaning: to run ... drem-: ... gr. Aor. ἔδραμον, Perf. δέδρομα \\\"run\\\", δρόμος \\\"run\\\" ... dreu-: ... Avestan draonah- ... Gothic trudan \\\"tread\\\", Old English tredan'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 795 ff. (Bd. I, dli scan)\", \"stance\": \"supports\",\n     \"note\": \"'anord. troda, trad ds.; as. ags. tredan, ahd. tretan \\\"treten\\\" ... trada \\\"Tritt, Spur\\\", ags. trod n., trodu f. \\\"Spur, Weg\\\" (engl. trade \\\"Handel\\\" ...)' — the same root file Pokorny cites as WP. I 795 ff.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. der-1\", \"stance\": \"supports\",\n     \"note\": \"'der-1. Assumed base of roots meaning \\\"to run, walk, step.\\\" ... [Pok. 3. (der-) 204.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, col. s.v. dromos\", \"stance\": \"supports\",\n     \"note\": \"'dromos \\\"course, way\\\". WP I, 796  Skt. cf. dram- \\\"to run\\\"; Gk. drómos; LG tram \\\"rung of ladder\\\"; OE. trem \\\"footstep\\\"'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"draonah\", \"verdict\": \"plausible\",\n     \"derivation\": (\n      \"Avestan draonah- is a real neuter s-stem (Y. 11.4, Y. 10.15, Vd. 18, Yt. 10), but its attested sense is not \"\n      \"'travel goods'. Bartholomae, Altiranisches Woerterbuch col. 769-770, glosses it 'bei der Besitzverteilung \"\n      \"zufallendes Gut, Vermoegens(usw.)anteil, Teil' - the share of property that falls to one at a distribution - \"\n      \"and equates it with Sanskrit draviṇas- n. 'Gut, Geld'. Formally it is *drau-nas-, built on the *dreu- \"\n      \"extension of the root; Pokorny p. 205 lists it under dreu- ('Old Indic dravati \\\"runs, also melts\\\" ... Avestan \"\n      \"draonah- n. \\\"bei der Besitzverteilung zufallendes Gut\\\" perhaps as \\\"traveling fortune\\\"'), and Nourai's gloss \"\n      \"'travel goods' is a rendering of exactly that parenthetical guess. Pokorny himself hedges it ('very doubtful \"\n      \"Old Indic dravina-m, dravinas- n.'), so the attachment of draonah- to the 'run' root is a possibility, not an \"\n      \"established derivation, and the gloss printed in the chart is the etymological speculation rather than the \"\n      \"philological meaning. Form and language label are correct.\"),\n     \"derivation_fa\": (\n      \"واژهٔ اوستایی draonah- ستاکی است خنثی از گونهٔ s-دار و در یسنا ۱۱٫۴ و ۱۰٫۱۵ و وندیداد آمده است، اما معنی \"\n      \"گواهی‌شدهٔ آن «توشهٔ سفر» نیست: بارتولمه در ستون ۷۶۹–۷۷۰ فرهنگ ایرانی باستان آن را «بهره‌ای از دارایی که در \"\n      \"هنگام بخش کردن به کسی می‌رسد» معنی می‌کند و با سنسکریت draviṇas- «مال، دارایی» هم‌ریشه می‌داند. از نظر ساخت \"\n      \"*drau-nas- است بر پایهٔ گسترش *dreu- از ریشه، و پوکورنی در صفحهٔ ۲۰۵ آن را زیر همین *dreu- آورده و با تردید \"\n      \"افزوده است «شاید به معنی مالِ در سفر»؛ معنی‌ای که نورایی در نمودار نوشته دقیقاً همین حدسِ پوکورنی است، نه \"\n      \"معنی زبان‌شناختیِ گواهی‌شده. خودِ پوکورنی این پیوند را «بسیار تردیدآمیز» خوانده است. صورت واژه و برچسب زبانی \"\n      \"درست است، ولی ادعای نورایی دربارهٔ معنی و پیوستگی به ریشهٔ «دویدن» تنها با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://www.avesta.org/ritual/rcc15.htm\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:205\", \"status\": \"partial\",\n       \"note\": (\"Pokorny p. 205 (POK_full block 'Page(s): 204-206', section dreu-) does carry the word: 'Avestan \"\n                \"draonah- n. \\\"bei der Besitzverteilung zufallendes Gut, Vermogensanteil\\\" perhaps as \\\"traveling \"\n                \"fortune\\\"?' - i.e. the page supports the arrow only as a guess, and hedges the whole Skt./Av. group \"\n                \"as 'very doubtful'.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiWb col. 769-770 s.v. draonah- (BRT.txt leaf 440/441)\", \"stance\": \"partial\",\n       \"note\": \"\\\"j., g. draonah- n. 'bei der Besitzverteilung zufallendes Gut, Vermoegens(usw.)anteil, Teil'\\\"; footnote: 'Das mp. Ritualwort droen wird als gleichw. dem Aw. draonah- entsprechen; aber seine Bedeutung \\\"Opferbrot\\\" ... ist im Awesta nicht zu belegen'; 'ai. dravinas- n. \\\"Gut, Geld\\\"; mp. droen'. Confirms the word but not the gloss 'travel goods'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 795 f. (Bd. I dli scan, line ~50166)\", \"stance\": \"partial\",\n       \"note\": \"'... dravinas- n. \\\"Gut, Vermogen\\\", av. draonah- n. \\\"bei der Besitzverteilung ...\\\"' with the same '(ob auch ai. dravina-m ...)' hedge that Pokorny reproduces.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 74, p. 274\", \"stance\": \"supports\",\n       \"note\": \"'aw. draonah- \\\"Opferbrot\\\"; ai. vergl. draviṇa-, drāvinas- \\\"Gut, Besitz\\\"' - Horn too glosses it by the property word, and by the ritual bread, not by 'travel goods'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"darŭn\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"Avestan draonah- gave Middle Persian droen (written dlwn'), which MacKenzie, Concise Pahlavi Dictionary, \"\n      \"glosses '2droen [dlwn' | N daruen] consecrated bread, ceremony in which c.b. is used' (and 'droen yashtan: \"\n      \"consecrate the sacrificial bread'). The sound history is regular: the Avestan s-stem ending -nah is lost, and \"\n      \"Old Iranian -ao- becomes Middle Persian oe; the New Persian/Pazand form druen ~ daruen shows the raising of \"\n      \"that oe to u before a nasal that Huebschmann documents as a rule (Persische Studien Sec. 32: 'ap. au = phl. oe \"\n      \"wird vor w, m im Paz. und Np. zu u: gun ... paz. druen \\\"a consecrated cake\\\" Min. Gl. 64 = zd. draonah-; surun \"\n      \"= zd. sraoni-; hum = zd. haoma-'). Horn, Grundriss no. 74 (p. 274), heads the entry exactly as Nourai's arrow \"\n      \"requires: 'druen bezw. droen der Parsen. aw. draonah- \\\"Opferbrot\\\"'. In the Zoroastrian ritual the drOn is \"\n      \"primarily the small round unleavened bread marked with nine cuts, and by extension the baj/drOn ceremony and \"\n      \"the formula recited over it - which is the sense Borhan-e Qate' records ('a prayer that the Magi recite in \"\n      \"praise of God and breathe over the foodstuffs'), and which Nourai's gloss 'a Zoroastrian prayer' reflects. \"\n      \"The chart's index '1' on the Persian script marks it off from the homograph daruen/darun 'inside'.\"),\n     \"derivation_fa\": (\n      \"«درون ۱» (darun/drun) واژه‌ای دینی است و از اوستایی draonah- می‌آید: در فارسی میانه drōn (نوشتهٔ dlwn') شده \"\n      \"که مکنزی در فرهنگ کوچک پهلوی آن را «نان مقدس و آیینی که در آن این نان به کار می‌رود» معنی کرده است. تحول \"\n      \"آوایی منظم است: پایانهٔ ستاک s-دار اوستایی از میان رفته و دوواکهٔ ایرانی باستان -ao- در فارسی میانه به ō بدل \"\n      \"شده؛ سپس ō پیش از «ن» در پازند و فارسی نو به ū برکشیده شده است، همان قاعده‌ای که هوبشمان در «پژوهش‌های \"\n      \"فارسی» بند ۳۲ با نمونه‌های gōn > gūn، sraoni- > surūn و haoma- > hūm آورده و در همان‌جا paz. drūn «قرص \"\n      \"نذری» را از zd. draonah- گرفته است. هرن نیز در بند ۷۴ صفحهٔ ۲۷۴ همین را می‌گوید: «drūn یا drōnِ پارسیان، از \"\n      \"اوستایی draonah- «نان قربانی»». در آیین زردشتی drōn نخست همان نان گِرد فطیر با نُه برش است و سپس به آیین و \"\n      \"دعایی که بر آن می‌خوانند گفته شده؛ برهان قاطع هم درون را «دعایی که مغان در ستایش خدای تعالی بر آن می‌خوانند \"\n      \"و بر خوردنی‌ها می‌دمند» تعریف کرده است. پس ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.avesta.org/ritual/rcc15.htm\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:274\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss, p. 274 (HRN.txt leaf 295), numbered entry '74. drun bezw. droen der Parsen. aw. draonah- \\\"Opferbrot\\\"; ai. vergl. draviṇa-, drāvinas- \\\"Gut, Besitz\\\". np. drun soll ... auch ein \\\"Getreidemass\\\" bezeichnen' - precisely Nourai's Avestan > Persian arrow.\"},\n      {\"ref\": \"BQT:844 ?\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate', vol. 2, archive leaf 304 (printed page ~846/847 by the running-head offset, so Nourai's own '844 ?' is within the scan-offset uncertainty of two or three pages): headword 'درون = بفتح اول، بمعنی اندرون' and, in the same entry, '... و دعایی باشد که مغان در ستایش خدای تعالی و ذر آن خوانند و بر خوردنی‌ها بدمند ... و هر چیز که بر آن درون خوانده و دمیده باشند گویند مشته شده' - the Zoroastrian-prayer sense Nourai glosses. Grepped BQT_v2_pages.txt for درون, leaves 303-305.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 28 s.v. 2droen\", \"stance\": \"supports\",\n       \"note\": \"'2droen [dlwn' | N daruen] consecrated bread, ceremony in which c.b. is used'; 'droen yashtan: consecrate the sacrificial bread'. (PHD.txt line 314 / PHD_mackenzie.txt line 2070.)\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien Sec. 32\", \"stance\": \"supports\",\n       \"note\": \"'paz. drun \\\"a consecrated cake\\\" Min. Gl. 64 - zd. draonah-' listed among the regular ap. au > phl. oe > np. u cases (HUB.txt line 4976).\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 2, archive leaf 304 s.v. درون\", \"stance\": \"supports\",\n       \"note\": \"Same passage as in the ref_check; Mo'in's footnote on the page cross-refers to the Ardaviraf-nama for the drOn.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n       \"note\": \"grep -n 'dron\\\\|droen\\\\|draonah' NYB_vol2_glossary.txt returns nothing; the glossary of Nyberg's texts does not carry the ritual word.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"tred\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"Germanic *tred- 'to step' is the regular outcome of the zero-grade *dr̥- of the root with Grimm's Law \"\n      \"(PIE *d > Gmc *t): Watkins der-1.1 '*dr̥- in extended Germanic form *tred- in: a. Old English tredan, to step: \"\n      \"TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE'. The same form family is in Gothic trudan, \"\n      \"Old Norse troda, Old Saxon tredan, Old High German tretan, all listed by Pokorny p. 205 under dreu- and by \"\n      \"Walde-Pokorny I 795. The extension *dreb- gives Germanic *trep- ('something on or into which one steps'), the \"\n      \"source of trap and trip, which Nourai keeps in the same box.\"),\n     \"derivation_fa\": (\n      \"ستاک ژرمنی *tred- «گام نهادن» بازتاب منظم درجهٔ صفر *dr̥- این ریشه است پس از اِعمال قانون گریم (د هندواروپایی \"\n      \"> ت ژرمنی). واتکینز زیر der-1 می‌نویسد: «درجهٔ صفرِ *dr̥- در صورت گسترشِ ژرمنی *tred-: انگلیسی کهن tredan \"\n      \"«گام نهادن» > TREAD, TREADLE؛ آلمانی سفلای میانه trade «راه، رد» > TRADE». همین خانواده در گوتی trudan، \"\n      \"نروژی باستان troda، ساکسونی کهن tredan و آلمانی علیای کهن tretan هست و پوکورنی (ص ۲۰۵) و والده-پوکورنی \"\n      \"(جلد ۱ ص ۷۹۵) هر دو آن را زیر *dreu- آورده‌اند. گسترشِ *dreb- نیز ژرمنی *trep- «آنچه بر آن یا در آن گام \"\n      \"می‌نهند» را داده که خاستگاه trap و trip است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/tread\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. der-1: '1. Zero-grade form *dr̥- in extended Germanic form *tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. der-1\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 795\", \"stance\": \"supports\",\n       \"note\": \"'anord. troda, trad ds.; as. ags. tredan, ahd. tretan \\\"treten\\\" ... ahd. trata \\\"Tritt, Spur\\\"'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW I 205 (dreu- section)\", \"stance\": \"supports\",\n       \"note\": \"'Auf dreu-, participle *dru-to- based on perhaps ... Gothic trudan \\\"tread\\\", Old Norse troda, trad ds.; Old English tredan, Old High German tretan \\\"tread\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"tread, trade, trap, trip\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"All four are English reflexes of the Germanic *tred-/*trep- family. TREAD: ME treden < OE tredan 'go by feet, \"\n      \"walk, step on, trample' (Klein: 'rel. to OS. tredan, OFris. treda, OHG. tretan, ON. troda, Goth. trudan, \\\"to \"\n      \"tread\\\"'). TRADE: not native but a Middle Low German / Middle Dutch loan brought in by Hanse merchants in the \"\n      \"late 14c., ME trade 'path, track, course' (Klein s.v. trade: 'ME. \\\"path, track, course\\\", fr. MLG. trade, ... \"\n      \"rel. to OS. trada, OHG. trata, and to E. tread'); a ship's regular course > 'customary course of action' \"\n      \"(mid-15c.) > 'habitual business' (1540s) > 'buying and selling' (1550s). TRAP: OE traeppe, treppe 'snare', \"\n      \"from Germanic *trep-, literally 'that on or into which one steps' (Watkins der-1.2a). TRIP: late 14c. 'skip, \"\n      \"dance briskly', from Old French triper, itself from a Germanic source, Middle Dutch trippen 'to stamp, \"\n      \"trample' (Watkins der-1.2e). Watkins lists all four under der-1 in his index (TREAD der-1, TRADE der-1, \"\n      \"TRAP-1 der-1, TRIP der-1).\"),\n     \"derivation_fa\": (\n      \"هر چهار واژه بازتاب انگلیسی خانوادهٔ ژرمنی *tred-/*trep- اند. tread از انگلیسی میانهٔ treden و انگلیسی کهن \"\n      \"tredan «راه رفتن، پا نهادن، لگدمال کردن»؛ کلاین آن را با ساکسونی کهن tredan، گوتی trudan و آلمانی علیای کهن \"\n      \"tretan هم‌ریشه می‌داند. trade واژه‌ای بومی نیست، بلکه در اواخر سدهٔ چهاردهم از آلمانی سفلای میانه/هلندی \"\n      \"میانهٔ trade «راه، رد، مسیر» به دست بازرگانان هانزا وام گرفته شده و از «مسیر همیشگی کشتی» به «روش همیشگی \"\n      \"کار» (میانهٔ سدهٔ پانزدهم)، سپس «پیشه» (۱۵۴۰م) و سرانجام «داد و ستد» (۱۵۵۰م) رسیده است. trap از انگلیسی کهن \"\n      \"træppe «دام» و از ژرمنی *trep- به معنی تحت‌اللفظی «آنچه بر آن پا می‌گذارند» است، و trip از فرانسهٔ کهن triper \"\n      \"که خود از هلندی میانهٔ trippen «پای کوبیدن» وام گرفته شده. واتکینز هر چهار را در نمایهٔ خود زیر der-1 آورده \"\n      \"است؛ پس ادعای نورایی درست است.\"),\n     \"sources\": [\n      \"https://www.etymonline.com/word/tread\",\n      \"https://www.etymonline.com/word/trade\",\n      \"https://www.etymonline.com/word/trap\",\n      \"https://www.etymonline.com/word/trip\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"Nourai gives no reference on this box; the parent Germanic box carries AHD, and Watkins' index confirms all four words (TRADE der-1, TRAP1 der-1, TREAD der-1, TRIP der-1).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. der-1 and the index\", \"stance\": \"supports\",\n       \"note\": \"'a. Old English treppe, traeppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP2; ... e. Middle Dutch trippen, to stamp, trample: TRIP'; index lines 'TRADE der-1', 'TRAP! der-1', 'TREAD der-1', 'TRIP der-1'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. tread and s.v. trade\", \"stance\": \"supports\",\n       \"note\": \"'tread ... fr. OE. tredan, rel. to OS. tredan, OFris. treda, OHG. tretan ... Goth. trudan, \\\"to tread\\\". ... Cp. also trade, treadle.'; 'trade, n. - ME. \\\"path, track, course\\\", fr. MLG. trade, ... rel. to OS. trada, OHG. trata, ... and to E. tread.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 795\", \"stance\": \"supports\",\n       \"note\": \"'ags. trod n., trodu f. \\\"Spur, Weg\\\" (engl. trade \\\"Handel\\\" ...)'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Greek\", \"words\": \"dromos\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"Greek dromos 'a running, race, racecourse' is the o-grade *drom-o- of the *drem- extension of the root, \"\n      \"beside the aorist edramon and perfect dedroma 'I ran' (Pokorny p. 205, section drem-: 'Old Indic dramati \"\n      \"\\\"running\\\" ... gr. Aor. edramon, Perf. dedroma \\\"run\\\", dromos \\\"run\\\"'). Watkins der-1.6 has it verbatim: \"\n      \"'Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, racecourse'. \"\n      \"Nourai's gloss 'a course, path' is the standard one.\"),\n     \"derivation_fa\": (\n      \"یونانی dromos «دویدن، مسابقه، میدان دو» درجهٔ o از گسترشِ *drem- این ریشه است، در کنار ماضی سادهٔ edramon و \"\n      \"ماضی نقلی dedroma «دویدم». پوکورنی در صفحهٔ ۲۰۵ زیر بخش drem- می‌نویسد: «سنسکریت dramati «دونده» ... یونانی \"\n      \"aorist ἔδραμον، perfect δέδρομα «دویدن»، δρόμος «دو»»؛ و واتکینز همان را زیر der-1 می‌آورد: «صورت ریشه‌ای \"\n      \"*drem- در ساخت پسوندیِ درجهٔ o یعنی *drom-o-: یونانی dromos». معنی‌ای که نورایی داده («راه، مسیر») همان \"\n      \"معنی متعارف است و ادعای او درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/syndrome\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 der-1.6: 'Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, racecourse: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dromas, running: DROMEDARY.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW I 205, drem- section\", \"stance\": \"supports\",\n       \"note\": \"'drem-: Old Indic dramati \\\"running\\\", Intens. dandramyate \\\"runs to and fro\\\"; gr. Aor. edramon, Perf. dedroma \\\"run\\\", dromos \\\"run\\\"'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dromos\", \"stance\": \"supports\",\n       \"note\": \"'dromos \\\"course, way\\\". WP I, 796  Skt. cf. dram- \\\"to run\\\"; Gk. drómos; LG tram \\\"rung of ladder\\\"; OE. trem \\\"footstep\\\"; Norw. tram \\\"threshold\\\"'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. -drome / dromedary\", \"stance\": \"supports\",\n       \"note\": \"'-drome ... Gk. -dromos, fr. dromos, \\\"a running, course, race, racecourse\\\"'; 'dromedary ... fr. Gk. dromas ... rel. to dramein, \\\"to run\\\", dedroma, \\\"I ran\\\", dromos ... fr. I.-E. base *drem- \\\"to run\\\", whence also OI. dramati, \\\"runs\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"-drome, syndrome\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"The English combining form -drome is Greek -dromos taken over through Latin/French in learned compounds \"\n      \"(hippodrome, aerodrome 1902, velodrome), Klein: '-drome, combining form lit. meaning \\\"running, course\\\", as in \"\n      \"aerodrome. - Gk. -dromos, fr. dromos'. SYNDROME entered English in the 1540s through medical Latin, from \"\n      \"Greek syndrome 'concurrence (of symptoms)', the noun to syndromos 'running together', from syn- 'with, \"\n      \"together' + dromos; the '____ syndrome' pattern is only mid-20c. So the box is a straight continuation of \"\n      \"the Greek dromos node.\"),\n     \"derivation_fa\": (\n      \"جزء ترکیبی ‎-drome‎ در انگلیسی همان ‎-dromos‎ یونانی است که از راه لاتین و فرانسه در ترکیب‌های عالمانه \"\n      \"(hippodrome، velodrome و aerodrome از ۱۹۰۲م) وارد شده است؛ کلاین می‌نویسد: «‎-drome‎ ... از یونانی \"\n      \"‎-dromos‎، از dromos». واژهٔ syndrome در دههٔ ۱۵۴۰م از راه لاتینِ پزشکی از یونانی syndromē «هم‌آیی (نشانه‌ها)» \"\n      \"گرفته شده که اسمِ syndromos «با هم دونده» است، از پیشوند syn- «با، هم» و dromos؛ کاربرد الگویی «فلان \"\n      \"سندروم» تازه از میانهٔ سدهٔ بیستم رواج یافته است. پس این جعبه ادامهٔ مستقیم جعبهٔ یونانی است و ادعای نورایی \"\n      \"درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/syndrome\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference printed on this box; the parent Greek box carries AHD, whose der-1 entry lists -DROME among the English derivatives.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. -drome\", \"stance\": \"supports\",\n       \"note\": \"'-drome, combining form lit. meaning \\\"running, course\\\", as in aerodrome. - Gk. -dromos, fr. dromos, \\\"a running, course, race, racecourse\\\". See dromedary.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 der-1.6a\", \"stance\": \"supports\",\n       \"note\": \"'Greek dromos ...: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Derk\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *derḱ- 'to see, look'\",\n   \"note\": (\n    \"The root is real and the gloss is right: Pokorny 'Root/lemma: derḱ- Meaning: to look ... Page(s): 213', with \"\n    \"Old Indic dadarsa 'have seen', Avestan daras- 'behold', Greek derkomai 'look, keep the eyes open', drakon \"\n    \"'dragon, snake' (from banishing, paralyzing look), Gothic ga-tarhjan, Old English torht. Watkins: 'derk-. To \"\n    \"see. ... [Pok. derk̑- 213.]' Nourai's page citation POK:218 is WRONG - Pokorny p. 217-219 carries deu-1 \"\n    \"'to lack' / deu-2 'to worship; mighty', not derḱ-; the root is on p. 213, so 218 looks like a digit slip for \"\n    \"213. This is a citation error, not an etymological one.\"),\n   \"note_fa\": (\n    \"ریشهٔ *derḱ- «دیدن، نگریستن» ریشه‌ای واقعی و معنی داده‌شده درست است: پوکورنی آن را در صفحهٔ ۲۱۳ آورده با \"\n    \"شواهدی چون سنسکریت dadarśa «دیده‌ام»، اوستایی daras- «نگریستن»، یونانی δέρκομαι «نگاه کردن، چشم گشوده \"\n    \"داشتن» و δράκων «اژدها، مار» (به سبب نگاه خیره و فلج‌کننده)، گوتی ga-tarhjan و انگلیسی کهن torht. واتکینز نیز \"\n    \"می‌نویسد: «derk-. To see ... [پوکورنی derk̑- ۲۱۳]». اما ارجاع نورایی (پوکورنی ۲۱۸) نادرست است: صفحه‌های \"\n    \"۲۱۷ تا ۲۱۹ پوکورنی به deu-1 و deu-2 «پرستیدن؛ نیرومند» اختصاص دارد و derḱ- در صفحهٔ ۲۱۳ است؛ ظاهراً \"\n    \"۲۱۸ خطای چاپی به جای ۲۱۳ است. این خطای ارجاع است نه خطای ریشه‌شناختی.\"),\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der%E1%B8%B1-\",\n    \"https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%AC%CE%BA%CF%89%CE%BD\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:218\", \"status\": \"not_found\",\n     \"note\": (\"Checked POK_full.txt: the blocks ending 'Page(s): 217-218' and 'Page(s): 218-219' are deu-1/deu-2 \"\n              \"('to worship; mighty'), with no trace of derḱ-. The derḱ- block ends 'Page(s): 213'. Wiktionary's \"\n              \"Reconstruction:Proto-Indo-European/derḱ- also cites Pokorny 213.\")}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW I 213 s.v. derḱ-\", \"stance\": \"supports\",\n     \"note\": \"'Root / lemma: derḱ-: to look ... gr. derkomai \\\"look, keep the eyes open, be alive\\\", dedorka, edrakon ... drakon, -ontos \\\"dragon, snake\\\" (from banishing, paralyzing look)'; 'References: WP. I 806 f.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. derk-\", \"stance\": \"supports\",\n     \"note\": \"'derk-. To see. Suffixed zero-grade form *dr̥k-on(t)- in Greek drakon (> Latin draco), serpent, dragon (< \\\"monster with the evil eye\\\"): DRAGON, (DRAGOON), (DRAKE2), RANKLE. [Pok. derk̑- 213.]'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. dragon (pp. 479-480)\", \"stance\": \"supports\",\n     \"note\": \"'fr. Gk. drakon, which prob. means lit. \\\"the sharp-sighted one\\\", and is rel. to derkesthai, \\\"to look at\\\", fr. I.-E. base *derk-, *dr̥k-, \\\"to see, look at\\\"'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. dr̥ktis\", \"stance\": \"supports\",\n     \"note\": \"'dr̥ktis \\\"seeing, sight, brightness\\\". Cf. derk-, dork-, dr̥k- & WP I, 806  Skt. dr̥ṣṭiḥ; Av. (o-gde) darstis; Alb. dritë \\\"light\\\" ...' - the same root, referred to Walde-Pokorny I 806.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Greek\", \"words\": \"drakoon\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"Greek drakon, gen. drakontos, is the zero-grade *dr̥ḱ-ont- (originally a participle) of derkomai 'to look, \"\n      \"fix the gaze', so it means literally 'the one that stares / the sharp-sighted one'. Pokorny p. 213 has it \"\n      \"under derḱ- with exactly that motivation ('drakon, -ontos \\\"dragon, snake\\\" (from banishing, paralyzing \"\n      \"look)'), Watkins glosses it '< \\\"monster with the evil eye\\\"', and Klein 'prob. means lit. \\\"the sharp-sighted \"\n      \"one\\\", and is rel. to derkesthai'. Nourai's gloss 'a serpent with devil eyes' is a paraphrase of Watkins' \"\n      \"evil-eye formula. The word is Homeric (Il. 2.308, 11.39, 12.202) and its cognate feminine drakaina is \"\n      \"attested from Hesiod on.\"),\n     \"derivation_fa\": (\n      \"یونانی δράκων (اضافی δράκοντος) درجهٔ صفرِ *dr̥ḱ-ont- است، در اصل صفت فاعلی فعل δέρκομαι «نگریستن، چشم \"\n      \"دوختن»؛ پس معنی تحت‌اللفظی آن «خیره‌نگر، تیزبین» است. پوکورنی در صفحهٔ ۲۱۳ همین انگیزهٔ نام‌گذاری را می‌آورد \"\n      \"(«δράκων «اژدها، مار» از نگاه خیره و فلج‌کننده») و واتکینز آن را «جانوری با چشم بد» معنی می‌کند و کلاین \"\n      \"می‌نویسد «احتمالاً به معنی تحت‌اللفظی «تیزبین» و هم‌ریشه با δέρκεσθαι». عبارت نورایی («ماری با چشمان دیو») \"\n      \"بازگفت همان تعبیر «چشم بد» است. واژه در ایلیاد هومر هم آمده است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%AC%CE%BA%CF%89%CE%BD\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:480\", \"status\": \"supports\",\n       \"note\": \"Klein 1966, the entry 'dragon, n. - OF. (= F.), fr. L. draconem, acc. of draco ... fr. Gk. drakon, which prob. means lit. \\\"the sharp-sighted one\\\", and is rel. to derkesthai, \\\"to look at\\\", fr. I.-E. base *derk-, *dr̥k-, \\\"to see, look at\\\"' stands at the foot of KLN_1966 leaf 262 and runs onto leaf 263; the standalone page numerals on those leaves are 478/479 and 480/481, so Nourai's p.480 is right.\"},\n      {\"ref\": \"KLN:1574\", \"status\": \"supports\",\n       \"note\": \"Klein p. 1574 (KLN_1966 leaf 834, between the numerals 1572 and 1577) is the 'tarragon' entry, which ends 'and see dragon' - i.e. it is the page that ties drakon to tarkhun.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW I 213\", \"stance\": \"supports\",\n       \"note\": \"'gr. derkomai \\\"look, keep the eyes open, be alive\\\" ... drakos n. \\\"eye\\\", drakon, -ontos \\\"dragon, snake\\\" (from banishing, paralyzing look), fem. drakaina'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. derk-\", \"stance\": \"supports\",\n       \"note\": \"'Suffixed zero-grade form *dr̥k-on(t)- in Greek drakon (> Latin draco), serpent, dragon (< \\\"monster with the evil eye\\\")'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"tarxŭn\", \"verdict\": \"plausible\",\n     \"derivation\": (\n      \"Arabic ṭarḫūn (طرخون), the name of Artemisia dracunculus, has no Arabic root ṭ-r-ḫ-n and is agreed on all \"\n      \"hands to be a loan whose ultimate source is the Greek dragon word. Where the sources differ from Nourai is in \"\n      \"the immediate Greek etymon: Klein, Wiktionary and Ernout-Meillet's dracunculus point not to the simplex \"\n      \"drakon but to its derivative drakontion 'dragonwort, adderwort' (lit. 'little dragon'), the standard \"\n      \"Dioscoridean plant name, Arabised with emphatic ṭ- for Greek d- (a normal substitution before a back vowel), \"\n      \"ḫ for the Greek k, and the ending reshaped to the Arabic pattern faʿlūn; Lokotsch (no. 2034) and Funk & \"\n      \"Wagnalls do write it '[aus gr. drakon]' just as Nourai does, and Skeat likewise. Etymonline is the most \"\n      \"cautious, calling it 'said to be from a non-Arabic source, perhaps Greek drakon'. So Nourai's arrow is the \"\n      \"traditional formulation of a claim that is right in substance but imprecise in the etymon; hence plausible \"\n      \"rather than confirmed. The word is well attested in Arabic medical literature (Ibn Sina, Ibn al-Baytar).\"),\n     \"derivation_fa\": (\n      \"واژهٔ عربی «طَرْخون» نام گیاه Artemisia dracunculus است و ریشهٔ سه‌حرفی عربی (ط-ر-خ-ن) ندارد؛ همهٔ منابع آن را \"\n      \"وام‌واژه‌ای می‌دانند که سرچشمهٔ آن واژهٔ یونانیِ «اژدها» است. اختلاف با نمودار نورایی در صورتِ بی‌واسطهٔ یونانی \"\n      \"است: کلاین و ویکی‌واژه و اِرنو-مِیه (زیر dracunculus) نه خودِ δράκων بلکه مشتق آن δρακόντιον «اژدهاگیاه» را \"\n      \"خاستگاه می‌دانند، که نام گیاه‌شناختی متعارف در دیوسکوریدس است؛ در معرّب‌سازی، دالِ یونانی به طای مفخم و کافِ \"\n      \"یونانی به خ بدل شده و پایانه بر وزن فَعلون بازساخته شده است. در برابر، لوکوچ (شمارهٔ ۲۰۳۴) و فانک و \"\n      \"واگنالز و اسکیت درست مانند نورایی می‌نویسند «از یونانی drakōn». اتیمونلاین محتاط‌تر است و می‌گوید «گفته‌اند \"\n      \"از منبعی غیرعربی، شاید یونانی drakōn». پس ادعای نورایی در اصل درست ولی در جزئیات نادقیق است و با احتیاط \"\n      \"پذیرفتنی است.\"),\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%AE%D9%88%D9%86\",\n      \"https://www.etymonline.com/word/tarragon\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1554\", \"status\": \"not_found\",\n       \"note\": \"Klein p. 1554 is nowhere near this word: KLN_1966 leaf 824 (interpolating between the running numerals 1572 on leaf 833 and the swart-/swindle- material) covers 'swine ... syllable, syllabus', and the tarragon entry is on p. 1574, which Nourai cites correctly on the Greek box below. KLN:1554 looks like a typo for 1574.\"},\n      {\"ref\": \"TAD:49\", \"status\": \"supports\",\n       \"note\": \"al-Unaysi, Tafsir al-alfaz al-dakhila, TAD_pages.txt leaf 49 (printed numeral 50 at the head, so Nourai's 49 is right to within one page): 'طرخون - تعريب «...» اللاتيني وهو نبات أصله في اليونانية' - 'ṭarḫūn: an Arabicization of the Latin [word]; it is a plant whose origin is in Greek', i.e. a foreign, ultimately Greek word, exactly the direction Nourai draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2034\", \"stance\": \"supports\",\n       \"note\": \"'2034. Ar. ṭarḫūn: \\\"Kaisersalat, Bertram, Artemisia dracunculus\\\" [aus gr. drakon]; hieraus it. targone, mfrz. targon, frz. targon, estragon, prov. draguneto, sp. taragona, pg. estragao, rum. tarhon; engl. dragoon, dtsch. Dragun, Esdragon ... Der Esdragon ist wahrscheinlich zur Zeit der Kreuzzuege nach Europa eingefuehrt worden, da er den Alten unbekannt war.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. tarragon, p. 1574\", \"stance\": \"partial\",\n       \"note\": \"'Sp. taragona, fr. Arab. ṭarkhun, \\\"dragon wort\\\", fr. Gk. drakontion, \\\"adderwort\\\", lit. \\\"a little dragon\\\"; dimin. of drakon' - same route but via the diminutive drakontion, not the simplex.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt leaf 113 s.v. الطرخون\", \"stance\": \"contradicts\",\n       \"note\": \"'(الطرخون) نبات يكبس في [الخل] والملح واللبن وأصل عروقه العاقر قرحا، معرب عن ترخون' - Addi Shir makes the Arabic word a muʿarrab of the PERSIAN tarkhūn, i.e. Persian > Arabic, the reverse of Nourai's next arrow.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, s.v. Estragon (pp. 112-113)\", \"stance\": \"partial\",\n       \"note\": \"'Les formes taragona, targone, anc. fr. tragon nous ramenent a l'arabe-persan tarkhoun, mot qu'on trouve dans Ibn-Beithar, dans Avicenne ... En derniere analyse, il peut se faire que tarkhoun ait ete emprunte par les Arabes au grec drakon, et que, par suite, ceux qui tirent estragon de draconem ne se trompent qu'a moitie.'\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. tarragon\", \"stance\": \"supports\",\n       \"note\": \"'[< OF targon, < Ar. ṭarkhun < Gr drakon, see dragon]'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"tarxŭn\", \"verdict\": \"plausible\",\n     \"derivation\": (\n      \"Persian ترخون tarxun 'tarragon' is the same word with the Arabic emphatic ṭāʾ replaced by plain tāʾ, the \"\n      \"normal Persian treatment of Arabic ṭ in a plant name that was current in the Arabic medical corpus (Ibn Sina \"\n      \"writes طرخون). Wiktionary lists Persian ترخون among the descendants of Arabic طرخون, which is Nourai's arrow. \"\n      \"But the direction is genuinely disputed: Addi Shir (Alfaz al-farisiyya al-muʿarraba) heads the Arabic word \"\n      \"'muʿarrab of Persian tarkhūn'; Skeat writes 'Span. taragona ... from Pers. tarkhun, dragon-wort, from Gk. \"\n      \"drakon'; Devic speaks of an 'arabe-persan tarkhoun'; and al-Unaysi's neighbouring entry ṭarḫān is expressly \"\n      \"'Persian'. Since the plant name is in any case a Mediterranean/Greek term, and since Persian took most of \"\n      \"its Graeco-Arabic pharmacological vocabulary through Arabic, Nourai's arrow is the likelier of the two, but \"\n      \"it cannot be called established: hence plausible.\"),\n     \"derivation_fa\": (\n      \"«ترخون» فارسی همان واژه است با تبدیل طای مفخم عربی به تای ساده، رفتاری معمول در فارسی برای نام‌های گیاهی \"\n      \"که از پیکرهٔ پزشکی عربی آمده‌اند (ابن سینا «طرخون» می‌نویسد). ویکی‌واژه «ترخون» فارسی را در فهرست بازماندگان \"\n      \"«طرخون» عربی آورده است، یعنی همان جهتی که نورایی رسم کرده. با این همه جهت وام‌گیری به‌راستی محل اختلاف است: \"\n      \"أدّی شیر در «الألفاظ الفارسیة المعرّبة» واژهٔ عربی را «معرّب عن ترخون» یعنی معرّبِ فارسی می‌داند، اسکیت \"\n      \"می‌نویسد «اسپانیایی taragona ... از فارسی tarkhūn»، و دوویک از «طرخونِ عربی-فارسی» سخن می‌گوید. چون این نام \"\n      \"گیاه در اصل واژه‌ای مدیترانه‌ای/یونانی است و فارسی بیشترِ واژگان داروشناسی یونانی را از راه عربی گرفته، \"\n      \"جهتِ پیشنهادی نورایی محتمل‌تر است، اما قطعی نیست؛ پس با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%AE%D9%88%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"not_found\",\n       \"note\": \"Nourai cites Mo'in without a volume/page. The only local copy is the 2-volume Adena abridgement (MON_part1.txt): its running head 'ترخون' is on the page (line 39845), but the OCR jumps from ترخوانه straight to ترخود/ترخیص, so the headword entry itself is not recoverable from this text; the 6-volume print Nourai used is not available.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"RCH\", \"where\": \"Richardson-Johnson, Persian-Arabic-English Dict.\", \"stance\": \"supports\",\n       \"note\": \"'tarkhun (or tarkhi), Tarragon, or dracunculus hortensis (an herb)' - the Persian word is well recorded with exactly this meaning (RCH.txt line 56636).\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir leaf 113 s.v. الطرخون\", \"stance\": \"contradicts\",\n       \"note\": \"'معرب عن ترخون' - makes Persian the source and Arabic the borrower, the reverse of the arrow.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. tarragon\", \"stance\": \"contradicts\",\n       \"note\": \"'tarragon, a plant. (Span. - Pers. - Gk.) Span. taragona (whence F. targon), from Pers. tarkhun, dragon-wort. - Gk. drakon, a dragon.' Skeat routes the word through Persian, not Arabic.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye hend-o-orupayi\", \"stance\": \"silent\",\n       \"note\": \"grep of ترخون in ARY_pages.txt returns no headword; the book has no entry for this plant name.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"tarxŭn\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"This box is the round trip: the Arabised form came back into Greek as Byzantine Greek tarkhon, from which \"\n      \"the medieval Latin plant name was taken. Etymonline states the chain explicitly - 'Medieval Latin tragonia, \"\n      \"from Byzantine Greek tarchon, from Arabic tarkhon' - and the older botanical Latin form is documented by \"\n      \"Devic: 'Nos anciens botanistes ecrivaient tarcon ou tarchon; cette derniere orthographe est celle de Gesner', \"\n      \"with Vaillant's genus name tarchonanthus built on it. So a Greek tarkhon distinct from (and later than) \"\n      \"drakon really existed, and Nourai's separate Greek box is justified.\"),\n     \"derivation_fa\": (\n      \"این جعبه همان «سفر رفت‌وبرگشت» واژه است: صورت معرّب دوباره به یونانی بازگشت و در یونانی بیزانسی ταρχών شد و \"\n      \"از همان صورت، نام گیاه در لاتینِ سده‌های میانه گرفته شد. اتیمونلاین این زنجیره را روشن می‌آورد: «لاتینِ \"\n      \"میانه tragonia، از یونانی بیزانسی tarchon، از عربی tarkhon». صورت لاتینِ کهن‌تر را دوویک گواهی می‌کند: \"\n      \"«گیاه‌شناسان قدیم ما tarcon یا tarchon می‌نوشتند؛ املای دوم از آنِ گِسنِر است»، و نام جنسِ tarchonanthus \"\n      \"ساختهٔ وایان بر همین پایه است. پس یونانیِ tarkhōn جدا از (و متأخرتر از) drakōn به‌راستی وجود داشته و جعبهٔ \"\n      \"جداگانهٔ نورایی موجه است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/tarragon\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1574\", \"status\": \"partial\",\n       \"note\": \"Klein's tarragon entry (p. 1574) is there and is about this word, but it routes English through Spanish taragona from Arabic ṭarkhun straight from Greek drakontion and says nothing about a Byzantine Greek tarkhon; Klein therefore supports the Arabic and the Greek origin but not this particular Greek re-borrowing box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Estragon (pp. 112-113)\", \"stance\": \"supports\",\n       \"note\": \"'Nos anciens botanistes ecrivaient tarcon ou tarchon; cette derniere orthographe est celle de Gesner, qui a donne le nom de tarchon sauvage a l'Achillea ptarmica. Vaillant ... a appele tarchonante, tarchonanthus, un arbrisseau d'Afrique.'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2034\", \"stance\": \"silent\",\n       \"note\": \"Lokotsch goes straight from Arabic ṭarḫūn to the Romance and Germanic forms; no Byzantine Greek stage is mentioned.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"The empty box is the medieval Latin link: Latin tarchon / tarcon, and the reshaped tragonia, taken from \"\n      \"Byzantine Greek tarkhon and used by the herbalists (Gesner still writes tarchon). Latin had in addition its \"\n      \"own inherited name for the plant, dracunculus 'little dragon', which Ernout-Meillet list under draco with \"\n      \"the gloss 'estragon' - so the same dragon-image reached Latin twice, once directly and once round through \"\n      \"Arabic. It is from the tarchon/tragonia form that the vernacular names come.\"),\n     \"derivation_fa\": (\n      \"این جعبهٔ تهی حلقهٔ لاتینِ سده‌های میانه است: لاتین tarchon/tarcon و صورت بازساختهٔ tragonia که از یونانی \"\n      \"بیزانسی گرفته شده و گیاه‌شناسان (تا گِسنِر) به کار می‌برده‌اند. لاتین افزون بر آن نام بومی خود را هم برای همین \"\n      \"گیاه داشت: dracunculus «اژدهای کوچک»، که اِرنو-مِیه زیر مدخل draco با معنی «estragon» آورده‌اند؛ یعنی همان \"\n      \"تصویرِ «اژدها» دو بار به لاتین رسیده است، یک بار یکراست از یونانی و یک بار از راه عربی. نام‌های زبان‌های \"\n      \"اروپایی از همین صورتِ tarchon/tragonia می‌آیند. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/tarragon\", \"https://en.wiktionary.org/wiki/tarragon\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference is printed on this pass-through box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. draco\", \"stance\": \"supports\",\n       \"note\": \"'Derive: dracunculus: 1o petit dragon; 2o poisson venimeux; 3o estragon' - Latin itself used a dragon-derivative for tarragon.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Estragon\", \"stance\": \"supports\",\n       \"note\": \"'Nos anciens botanistes ecrivaient tarcon ou tarchon' - the Latin botanical form behind the vernaculars.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"tarragon\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"English tarragon is first recorded in the 1530s; it comes from the medieval Latin/Romance form, through \"\n      \"Middle French targon (whence modern estragon, with an unetymological es-, perhaps the Arabic article \"\n      \"misparsed) - so Wiktionary; Klein and Skeat prefer Spanish taragona as the immediate donor, and Funk & \"\n      \"Wagnalls Old French targon. Nourai's chart draws Latin > English directly and so passes over the Romance \"\n      \"intermediary, but the substance - a Greek dragon word, Arabised, returned to Europe through Byzantine Greek \"\n      \"and medieval Latin, and applied to Artemisia dracunculus - is exactly the standard account. Lokotsch adds \"\n      \"the historical setting: the herb 'was probably brought to Europe at the time of the Crusades, since it was \"\n      \"unknown to the ancients'.\"),\n     \"derivation_fa\": (\n      \"واژهٔ انگلیسی tarragon نخستین بار در دههٔ ۱۵۳۰م گواهی شده و از صورتِ لاتینِ میانه/رومی می‌آید، از راه \"\n      \"فرانسهٔ میانهٔ targon (که estragon امروزی از آن است، با es- زائد که شاید بدخوانیِ حرف تعریف عربی باشد) — این \"\n      \"نظر ویکی‌واژه است؛ کلاین و اسکیت اسپانیایی taragona و فانک و واگنالز فرانسهٔ کهن targon را واسطهٔ بی‌واسطه \"\n      \"می‌دانند. نمودار نورایی پیکان را یکراست از لاتین به انگلیسی می‌کشد و واسطهٔ رومی را نادیده می‌گیرد، اما اصلِ \"\n      \"مطلب — واژه‌ای یونانی به معنی «اژدها» که معرّب شده و از راه یونانی بیزانسی و لاتینِ میانه به اروپا بازگشته و \"\n      \"بر گیاه Artemisia dracunculus نهاده شده — همان روایت متعارف است. لوکوچ می‌افزاید که این گیاه احتمالاً در \"\n      \"روزگار جنگ‌های صلیبی به اروپا آمده، چون قدما آن را نمی‌شناختند.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/tarragon\", \"https://www.etymonline.com/word/tarragon\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference printed on this box; the chain's citation is KLN:1574 on the Greek box above, whose 'tarragon' entry covers the English word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. tarragon\", \"stance\": \"partial\",\n       \"note\": \"'tarragon, a plant. (Span. - Pers. - Gk.) Span. taragona (whence F. targon), from Pers. tarkhun, dragon-wort. - Gk. drakon, a dragon.' Same ultimate origin; Spanish, not Latin, as the immediate donor.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. tarragon\", \"stance\": \"partial\",\n       \"note\": \"'[< OF targon, < Ar. ṭarkhun < Gr drakon, see dragon]' - French, not Latin, as the immediate donor.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2034\", \"stance\": \"supports\",\n       \"note\": \"lists 'it. targone, mfrz. targon, frz. targon, estragon ... sp. taragona' from Ar. ṭarḫūn and dates the plant's arrival to the Crusades.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Latin\", \"words\": \"dracŭ, dracŭnem\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"dracŭ, dracŭnem\",\n     \"correct_form\": \"dracō, dracōnem\",\n     \"derivation\": (\n      \"The etymology in this box is right but the forms as printed are impossible Latin. Rendered at 400 dpi, the \"\n      \"printed page (pdf 120 = book p. 90) clearly shows 'dracŭ, dracŭnem' with u-breve; the JSON reproduces the \"\n      \"page faithfully, so this is Nourai's own misprint (his long-o glyph has come out as u-breve in this box \"\n      \"only - the neighbouring 'tarxŭn' and 'darŭn' are genuine u's). The Latin is draco, gen. draconis, acc. \"\n      \"draconem. Ernout-Meillet: 'draco, -onis m.: 1o dragon; 2o serpent (poet.). Emprunt latinise au gr. drakon, \"\n      \"-ontos qui existe egalement en transcription; gen. dracontis, acc. dracontem ... passe en germ.: a.h.a. \"\n      \"trahho \\\"Drache\\\", et celt.: irl. drac, britt. draig.' So Latin borrowed the Greek word (attested from \"\n      \"Plautus and Cicero on) and re-cut its stem onto the Latin -o/-onis type, which is what gives the accusative \"\n      \"draconem from which all the Romance forms descend.\"),\n     \"derivation_fa\": (\n      \"ریشه‌شناسی این جعبه درست است اما صورت‌های چاپ‌شده لاتینِ ممکن نیستند. صفحهٔ چاپی (صفحهٔ ۱۲۰ پی‌دی‌اف = صفحهٔ \"\n      \"۹۰ کتاب) در تفکیک ۴۰۰ نقطه بر اینچ به‌روشنی «dracŭ, dracŭnem» با «او»ی کوتاه‌نشان نشان می‌دهد؛ داده‌های \"\n      \"استخراج‌شده وفادار به صفحه است، پس این خطای چاپیِ خودِ کتاب است (نشانهٔ «ای بلند» نورایی تنها در همین جعبه به \"\n      \"شکل ŭ درآمده، حال آنکه tarxŭn و darŭn در همان صفحه «او»ی واقعی‌اند). صورت درست لاتین draco، اضافی draconis \"\n      \"و مفعولی draconem است. اِرنو-مِیه می‌نویسند: «draco, -onis: ۱- اژدها ۲- مار (شاعرانه). وام‌واژه‌ای لاتینی‌شده \"\n      \"از یونانی δράκων, -οντος ... مفعولی dracontem ... به ژرمنی رفته: آلمانی علیای کهن trahho «اژدها»، و به \"\n      \"کلتی: ایرلندی drac». پس لاتین واژهٔ یونانی را وام گرفته و ستاک آن را بر الگوی -o/-onis لاتین بازساخته و از \"\n      \"همین صورتِ مفعولی draconem است که همهٔ صورت‌های زبان‌های رومی می‌آیند. خطای چاپی کتاب است، نه خطای خوانش اسکن.\"),\n     \"sources\": [\"https://www.etymonline.com/word/dragon\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. derk-: 'Greek drakon (> Latin draco), serpent, dragon' - and note that Watkins too writes draco, not *dracu.\"},\n      {\"ref\": \"KLN:480\", \"status\": \"supports\",\n       \"note\": \"Klein p. 480 s.v. dragon: 'OF. (= F.), fr. L. draconem, acc. of draco, \\\"a kind of a serpent; dragon\\\", fr. Gk. drakon'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. draco (LAT.txt line 17733)\", \"stance\": \"supports\",\n       \"note\": \"'draco, -onis m.: 1o dragon; 2o serpent (poet.). Emprunt latinise au gr. drakon, -ontos ... gen. dracontis, acc. dracontem, M.l.3759; passe en germ.: a.h.a. trahho \\\"Drache\\\", etc., et celt.: irl. drac, britt. draig.'\"},\n      {\"src\": \"LEW\", \"where\": \"Walde, Lat. etym. Wb., 2nd ed. 1910\", \"stance\": \"silent\",\n       \"note\": \"grep -n 'draco' LEW_1910.txt returns nothing - the OCR of the 1910 edition does not yield the entry.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. dragon, pp. 479-480\", \"stance\": \"supports\",\n       \"note\": \"same wording as the ref_check; Klein also gives the acc. draconem as the source of the Old French form.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"The empty box is Old French dragon, a semi-learned borrowing of the Latin accusative draconem (Latin -onem \"\n      \"> OF -on is the regular oblique-case outcome that supplied French nouns of this class). Klein: 'dragon, n. \"\n      \"- OF. (= F.), fr. L. draconem, acc. of draco'. The word is in French from the 12th century (Chanson de \"\n      \"Roland, Wace) in both the mythological and the military-standard sense, and the modern French form is \"\n      \"unchanged.\"),\n     \"derivation_fa\": (\n      \"این جعبهٔ تهی همان dragon فرانسهٔ کهن است، وامی نیمه‌عالمانه از صورت مفعولیِ لاتین draconem (پایانهٔ لاتینِ \"\n      \"-onem در فرانسهٔ کهن به -on بدل می‌شود و همین حالتِ غیرفاعلی است که اسم‌های این دسته را در فرانسه ساخته \"\n      \"است). کلاین می‌نویسد: «dragon — فرانسهٔ کهن (و امروزی)، از لاتین draconem، مفعولیِ draco». این واژه از سدهٔ \"\n      \"دوازدهم در فرانسه (چانسون دو رولان، واس) هم به معنی اژدها و هم به معنی درفشِ سپاهی به کار رفته و صورت \"\n      \"امروزی آن دگرگون نشده است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/dragon\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference printed on this pass-through box; the parent Latin box carries AHD; KLN:480, which covers the French link.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. dragon\", \"stance\": \"supports\",\n       \"note\": \"'dragon, n. - OF. (= F.), fr. L. draconem, acc. of draco, \\\"a kind of a serpent; dragon\\\", fr. Gk. drakon'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. draco\", \"stance\": \"supports\",\n       \"note\": \"gives the accusative dracontem/draconem with Meyer-Luebke's REW no. 3759, the etymon of the Romance forms including French dragon.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"dragon\", \"verdict\": \"confirmed\",\n     \"derivation\": (\n      \"English dragon is a Middle English borrowing of Old French dragon, first recorded in the early/mid 13th \"\n      \"century; the spelling and stress were never re-Latinised. Etymonline: 'from Old French dragon and directly \"\n      \"from Latin draconem (nominative draco) \\\"huge serpent, dragon\\\", from Greek drakon'. Klein's derivatives \"\n      \"(dragonet, dragonnade, dragoon) hang off the same entry. This closes Nourai's chain PIE *derḱ- > Gk drakon > \"\n      \"L draco(nem) > OF dragon > E dragon, which is uncontroversial.\"),\n     \"derivation_fa\": (\n      \"واژهٔ انگلیسی dragon وامی از dragonِ فرانسهٔ کهن در انگلیسی میانه است و نخستین گواهی آن به اوایل/میانهٔ سدهٔ \"\n      \"سیزدهم می‌رسد؛ املا و تکیهٔ آن هرگز دوباره لاتینی‌سازی نشده است. اتیمونلاین می‌نویسد: «از فرانسهٔ کهن dragon و \"\n      \"یکراست از لاتین draconem (فاعلی draco) «مار بزرگ، اژدها»، از یونانی drakōn». مشتق‌های dragonet و dragonnade \"\n      \"و dragoon در همان مدخل کلاین آمده‌اند. بدین‌سان زنجیرهٔ نورایی — هندواروپایی *derḱ- ← یونانی drakōn ← لاتین \"\n      \"draco(nem) ← فرانسهٔ کهن dragon ← انگلیسی dragon — کامل و بی‌چون‌وچرا است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/dragon\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference printed on this box; KLN:480 on the Latin box covers the whole Greek-Latin-French-English chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. dragon, p. 480\", \"stance\": \"supports\",\n       \"note\": \"'Derivatives: dragon-ess, n., dragonet (q.v.), dragonnade (q.v.)'; the headword derives English dragon from OF dragon < L draconem < Gk drakon.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. derk-\", \"stance\": \"supports\",\n       \"note\": \"'... serpent, dragon (< \\\"monster with the evil eye\\\"): DRAGON, (DRAGOON), (DRAKE2), RANKLE.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-120.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk120.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-120.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 120"
}
```


### [2026-09-05T18:20:53.139Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 3, 'confirmed': 11, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 2, 'supports': 9, 'not_checked': 6, 'not_found': 2}
books consulted: {'partial': 6, 'supports': 30, 'silent': 4, 'contradicts': 3} | by book: {'KLN': 7, 'AHD': 5, 'WLD': 3, 'POK': 3, 'LKT': 3, 'DEV': 3, 'LAT': 3, 'AFM': 2, 'FSD': 2, 'SKT': 2, 'BRT': 1, 'HRN': 1, 'PHD': 1, 'HUB': 1, 'BQT': 1, 'NYB': 1, 'IEC': 1, 'RCH': 1, 'ARY': 1, 'LEW': 1}
```


## [2026-09-05T18:21:11.341Z] AGENT

Page 120 (book p. 90) verified; `verify_check.py 120` reports **0 PROBLEM lines** (15/15 nodes, 2 roots).

**Counts** — nodes: 11 confirmed, 3 plausible, 1 transcription_suspect. Roots: 2 confirmed. Ref checks: 9 supports, 2 partial, 2 not_found, 6 not_checked (boxes with no refs printed). 40 `consulted` entries across 20 books.

**Flagged items**
- `Derk` #7 (Latin) — **transcription_suspect**, `error_in: "book"`. The page really prints `dracŭ, dracŭnem` (verified at 400 dpi); impossible Latin. Correct form `dracō, dracōnem`. Nourai's own misprint — the extraction is faithful, so **no data fix needed**. Page image copied to `data/verification/sources/refs/ocr/BOOK/120.png`.
- `Der 2, Deru 2` #1 Av. `draonah` — **plausible**: Bartholomae (AiWb col. 769-770) glosses it "share of property allotted at distribution", not "travel goods"; Nourai's gloss reproduces Pokorny's own hedged guess ("perhaps as 'traveling fortune'"), which Pokorny calls "very doubtful".
- `Derk` #2 Arabic `tarxŭn` — **plausible**: Klein/Wiktionary derive Ar. ṭarḫūn from Gk *drakontion* (the plant derivative), not the simplex *drakōn*; Lokotsch 2034, Funk & Wagnalls and Skeat do write "from gr. drakon" as Nourai does.
- `Derk` #3 Persian `tarxŭn` — **plausible**: direction disputed. Addi Shir (AFM leaf 113) and Skeat make Arabic borrow *from* Persian, reversing the arrow.

**Bad citations by Nourai (not extraction errors)**
- `Derk` root, `POK:218` → **not_found**: Pokorny pp. 217-219 are `deu-1`/`deu-2`; `derḱ-` is on p. **213** (Watkins also cites 213). Likely a digit slip.
- `Derk` #2, `KLN:1554` → **not_found**: Klein p. 1554 is in the "swine–syllabus" range; the tarragon entry is p. **1574**, which he cites correctly on the Greek box below.
- `Der 2` #2, `BQT:844 ?` (his own question mark) → **supports**: the درون entry with the Zoroastrian-prayer sense is at vol. 2 archive leaf 304, printed ≈846/847 — within the scan-offset uncertainty.

No extraction errors found: the JSON matches the printed page everywhere (`HRN:274; BQT:844 ?`, `KLN:1554; TAD:49`, `draonah`, `darŭn «درون ۱»` all confirmed against the rendered page). 12 web sources archived via `fetch_source.py`.
