# Verification process log — verify-page-107


## [2026-09-05T15:00:29.044Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 107 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-107.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-107.json. Write /home/sfmqrb/git/rishe/data/verification/page-107.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 107` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T15:00:30.569Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T15:00:31.279Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T15:00:31.298Z] TOOL RESULT

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


## [2026-09-05T15:00:31.477Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-107.txt"
}
```


### [2026-09-05T15:00:31.494Z] TOOL RESULT

```
1	=== PDF page 107 (book page 77) ===
2	--- entry 0 ---
3	ROOT [Old Persian] Čop, Čop-gân : stick, wood; a long stick  (refs HRN:99)
4	#1 (parent #0) [Persian] refs=HRN:99 | čŭb «چوب» : wood, stick ; čowgân «چوگان» : club, polo
5	  #2 (parent #1) [Turkish] refs=LKT:35 | čŭb : wood, stick ; čubŭq, chîbuq : smoking pipe (made from a wooden stem) | NOTE: Derivation of the Turkish word from Persian is not clear.
6	    #3 (parent #2) [Persian] refs=ARK:211 | čopoq «چپق» : smoking pipe
7	    #4 (parent #2) [French] refs=WEB:312 | chibouque : pipe
8	      #5 (parent #4) [English] refs=KLN:275 | chibouk : tobacco pipe
9	  #6 (parent #1) [Greek] refs=SKT:87 | 
10	    #7 (parent #6) [French] refs=WEB:312 | chicaner : to wrangle or dispute in a game
11	      #8 (parent #7) [English] refs=WEB:312 | chicane : trick ; chicanery : cheating
12	--- entry 1 ---
13	ROOT Čop-gân -> redirect to Čop
14	--- entry 2 ---
15	ROOT Črğâla -> redirect to Srgâla
16	
```


## [2026-09-05T15:00:35.339Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-107.json",
 "description": "Read page 107 source JSON"
}
```


### [2026-09-05T15:00:35.375Z] TOOL RESULT

```
{
  "pdf_page": 107,
  "book_page": 77,
  "entries": [
    {
      "root": {
        "name": "Čop, Čop-gân",
        "lang": "Old Persian",
        "refs": "HRN:99",
        "gloss": "stick, wood; a long stick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "HRN:99",
          "words": [
            {"translit": "čŭb", "gloss": "wood, stick", "script": "چوب"},
            {"translit": "čowgân", "gloss": "club, polo", "script": "چوگان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ای جوان سَرو قَد گویی بزن - پیش از آن کز قامتت چوگان کنند",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": "LKT:35",
          "words": [
            {"translit": "čŭb", "gloss": "wood, stick", "script": null},
            {"translit": "čubŭq, chîbuq", "gloss": "smoking pipe (made from a wooden stem)", "script": null}
          ],
          "script_extra": null,
          "note": "Derivation of the Turkish word from Persian is not clear.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "ARK:211",
          "words": [
            {"translit": "čopoq", "gloss": "smoking pipe", "script": "چپق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "WEB:312",
          "words": [
            {"translit": "chibouque", "gloss": "pipe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:275",
          "words": [
            {"translit": "chibouk", "gloss": "tobacco pipe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Greek",
          "refs": "SKT:87",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "WEB:312",
          "words": [
            {"translit": "chicaner", "gloss": "to wrangle or dispute in a game", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "WEB:312",
          "words": [
            {"translit": "chicane", "gloss": "trick", "script": null},
            {"translit": "chicanery", "gloss": "cheating", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Čop-gân",
        "redirect": "Čop"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Črğâla",
        "redirect": "Srgâla"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T15:00:37.068Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','LKT','ARK','WEB','KLN','SKT','MON','BQT','ARY','PHD','NYB','HUB','TTS','FSD','SOD','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Show ref metadata"
}
```


### [2026-09-05T15:00:39.078Z] TOOL RESULT

```
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
CHEUNG null
```


## [2026-09-05T15:00:47.935Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; grep -n -i \"čūb\\|cūb\\|Čūb\\|tschūb\\|çub\" HRN.txt | head -20",
 "description": "List refs and grep Horn"
}
```


### [2026-09-05T15:00:47.993Z] TOOL RESULT

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
---
```


## [2026-09-05T15:00:48.325Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T15:00:48.365Z] TOOL RESULT

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


## [2026-09-05T15:00:55.155Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf120 (p.99) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==121' HRN.txt | head -80",
 "description": "Print Horn p.99"
}
```


### [2026-09-05T15:00:56.668Z] TOOL RESULT

```
=== HRN leaf120 (p.99) ===
— 99 —
442. öu8t 'flink, tätig, passend'.
ai. l/cörf-, corföf^e 'antreiben ; sich beeilen' (Nöldeke,
mündliche Mitteilung).
Fr. Mtiller's (WZKM. 5, 68) Ableitung des Wortes
aus aw. cista- bezw. cista- ist schon wegen der Vokal-
difl^erenz (doch vergl. np. miizd) wenig wahrscheinlich.
443. eekuS 'Hammer .
aw. cakusqm, yt. 10, 130 'Hammer', Geldner, KZ.
25, 531 Note 210.
Das neupersische Wort ist nicht klar; eine Neben-
form ist öeköd oder deköj, vergl. dialektisch Kasan:
ceküSy rakoz, caküs, ödkös, vergl. kurd. cäqü, cek (H.-Sch.).
Nöldeke schlägt vor (mündliche Mitteilung), auch np.
öäk 'Spalt, Bruch' zu öekus zu stellen.
444. {\)ceni *Essen', cemfden 'trinken'.
ai. l/^(faw-, cämati (skr. camajiti) 'schlürfen',
oss. cimin, ba\dimin 'schlürfen* (320).
445. {2)ceni Sinn .
phlv. clm 'Urgrund, Ursache, Sinn .
Säle mann, Mol. asiat. IX, 233 Note 20.
446. cernber (geschrieben cenber) 'Kreis, Ring (z. B. Vis
und Ramin, S. 89 Vers 1)'.
V
phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
Zu np. cep 'links' (No. 435), gr. yAfiiJxct) 'biege',
adfinvXog (Nöldeke, mündliche Mitteilung).
Fick setzt als Wurzel für ai. capa- und gr. ad^iTiTO)
qep' an. Zu derselben Wurzel wird übrigens auch np.
xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
No. 12 — 'krumm, gebogen, yemtden etc. gehören.
447. eend 'einige*; wie viel?*, cendän, dendm, cendi,
aw. cvant' 'wie viel?'; phlv. cand.
kurd. LW. dend , dm; bei. cunt 'wie viel?' (64);
af;'. cof»[ira, com\ra wie viel?*; wa/. vum^ ciin, sar.
cund.
448. cöh 'Holz*.
phlv. 6öp 'Holz' (Guj. Ab.); kurd. cö, siw (H.-Sch.);
bei. LW. vöp (66); wa/. ^öpk, sar. /Jih,
7*
```


## [2026-09-05T15:00:57.152Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT leaf61 (p.35) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==62' LKT.txt | head -80; echo \"=== grep tschibuk/čubuk ===\"; grep -n -i \"schibuk\\|ubuk\\|schubuk\\|Tschibuk\\|čubuk\" LKT.txt | head -20",
 "description": "Print Lokotsch p.35"
}
```


### [2026-09-05T15:00:58.824Z] TOOL RESULT

```
=== LKT leaf61 (p.35) ===
 eigent- lich Abkürzung  für  china-dish  wie  turkey statt  turkey-carpet,  turquoise  statt  pne''>'e turquoise  [s.  hier  Nr.  2114].  [Hobson- Jobson  198/199.
422.  Chin.  chin^-ching:
Im  Dialekt  von  Peking  Höflichkeitsphrase als  Antwort  auf  'Danke!,  Auf  Wieder- sehen!' Aus  dem  Pigeon-Englisch  [aus fcatsmess-English  entstanden]  ging  der Ausdruck  in  den  Slang  des  Englischen
über  und  heißt  soviel  wie  'Gruß,  Kom- pliment'.   [Hobson-Jobson  200/201.
423.  Tk.  cift: [Wahrscheinlich  aus  pers.juft  'Genosse, Gatte;  Paar'  Horn  NpEt  S.  95,  Nr.  424] 'Paar',  besonders  'ein  Joch  Ackerstiere', daher  tk.  cißlik  'Landgut'.  Hieraus serb.  cift  'Paar',  bulg.  cift  'Paar,  Joch Ochsen',  ciftlik  'Landgut',  öiftcija  'Guts- besitzer, Bauer'.  —  [Daß  russ.  juft' 'Juchten'  usw.  hierhin  gehöre,  muß  be- zweifelt werden,  vgl.  vielmehr  hier Nr.  2128.]    [Bern  SlEtWb  156.
424.  Tk.  cifut:
Eine  Korruption  des  ar.  jahüd  'Jude' [s.  hier  Nr.  949],  dial.  gehud,  mit  der Bedeutung 'Ungläubiger';  das  Wort  wird tk.  als  Spottname  für  die  Juden  benutzt. Hieraus  rum.  ci^^fut  'Geizhals,  Wucherer, Jude',  bulg.  cifut,  öifutin,  serb.  civutin 'Jude',  it.  (dial.)  cifüt  'lästiger,  unver- schämter Junge;  Judenjunge'  (Monfer- rate),  cifü  'dass.'  (Nizza),  cifota  'schlech- ter Wein'  (Piemonte).  —  Ableitung  aus Joliannes  und  futuere  'coire'  ML  3622 scheint  nicht  angängig  trotz  prov.  jan- foutre,  piem.  gianfütre.  Lautlich  und semantisch  ist  die  gegebene  Etymologie viel  befriedigender.  [ZfromPh  XXXI, 272  (dagegen:  ZfromPh  XXXI,  659).
425.  Pers.  ciuär:
'Platane,  Platanus  orientalis';  hieraus angloind.  cheenar  'dass.'  und  russ.  cinar 'dass.,  morgenländischer  Ahorn'.  [Gor- jajew  414.    Hobson-Jobson  187.
426.  Tk.  cirag:
[Wohl  pers.  Ursprungs],  auch  cyrak 'Diener,  Lehrling';  hieraus  rum.  cirac 'Lehrling,  Eingeweihter',  ciraclic  'Lehre'.
427.  Tk.  ciris:
'Mehlpappe';  hieraus  rum.  ciri§  'Brei^ Mehlpappe  für  Buchbinder  u.  Schreiner'.
428.  Tk.  cit:
Auch  öyt  'buntes  Tuch,  gedruckter  Zitz' ; hieraus  rum.  cit  'feiner  Kattun,  gestreif- ter Stoff'.  —  Tk.  citary  'leichter  Stoff aus  Seide  und  Wolle';  hieraus  rum.  ci- tarea  'Kattun'.
429.  Tk.  cmid:
Auch  ciwit  gesprochen:  'Indigopflanze, Indigofera  tinctoria,  indigofarben' ;  hier- aus rum.  civit  'indigoblau'.
430.  Pers.  cTz:
'Etwas'  [Horn  NpEt  S.  101,  Nr.  457], hieraus  hind.  chlz  'etwas,  ein  Ding'  und schließlich  angloind.  cheeze,  ebenso  im engl.  Slang,  mit  der  Bedeutung  'etwas Gutes,  Echtes,  Ausgezeichnetes  oder  Vor- teilhaltes', z.  B.  'my  neiv  arab  is  the real  cheeze'.    [Hobson-Jobson  187.
431.  Tk.  cizme:
'Stiefel'  [vom  Vb.  ciztnek  'ziehen,  strei-
35
[Pers.  cöb.
chen,  liniieren',  Stamm  sil,  sir,  siz  'rei- ben, streichen;  Linie,  Strich'  Vdmbery TktEtWb  S.  147,  Nr.  159 III];  hieraus rum.  cizmä  'dass.',  bulg.  ciz^m,  cizma, serb.  cizma  'Stiefel',  klruss.  cyzmy 'Schuhe',  poln.  cizma,  czyznia  'Halb- stiefel'.   [Bern  SlEtWb  158.
432.  Pers.  cöb:
'Holz'  [Horn  NpEt  S.  99,  Nr.  448],  ebenso iV.  cob  'Stück  Holz,  Stock,  Sehmutz'; hieraus  rum.  ciob  'Scherbe,  Topf,  ciobesc.
433.  Tk.  coban:
'Hirt'  [aus  pers.  subän  'Schäfer'  Horn NpEt  S.  171,  Nr.  776  aus  päh  'Vieh' ebenda  S.  JJ87,  Nr.  153];  hieraus  bulg. serb.  öoban,  cobanin,  russ.  (dial.)  klruss. caban,  poln.  czuban  'Schäfer.  Hirt'. [Gorjajew  406.    Bern  SlEtWb  159.
434.  Pors.  cögän:
'Schlägel  (im  Ballspiel)'  [Horn  NpEt S.  100,  Nr.  449,  wahrscheinlich  aus präkrta  chaugäna  'vierfach',  dem  Namen für  den  Polospielplatz].  Das  Polo  ge- nannte Spiel  scheint  mediseh-persischen Ursprungs  zu  sein.  Während  es  jetzt nur  noch  in  einigen  Berglandschaften im  Norden  Indiens  erhalten  ist,  wurde es  früher  an  allen  mohammedanischen Höfen  Asiens  gespielt;  viele  Fürsten haben  es  mit  Leidenschaft  gespielt,  z.  B. Kaiser  Akbar  der  Große,  Saladin  u.  a. Vgl.  K.  Inostranzew,  Zur  Geschichte  des Polospieles.  In  Zapiski  Vostocnago  Ot- djelenija  Imp.  russk.  archeologiceskago Obsßestva.  St.  Petersburg.  Bd.  XIV, 4.  Lieferung.  Nach  Byzanz  gelangt,  hieß das  Spiel  mgr.  TluKdviov,  Vb.  tIukovi- Ceiv,  'Spielplatz  dafür'  x^uKaviaTripiov, und  in  Frankreich,  wo  es  zu  Fuß  ge- spielt wurde,  chicane.  Das  frz.  Wort bedeutete  dann,  daß  man  in  einem Kampfe  jeden  möglichen  Vorteil  wahr- nehmen durfte,  und  kam  so  zu  seiner heutigen  Bedeutung  frz.  chicane  'Kniffe, Schabernack,  Rechtsverdrehung,  Spitz- findigkeit', eigentlich  unübersetzbar,  da es  eine  wesentlic
=== grep tschibuk/čubuk ===
1183:'Pfeife'  [vom  pers.  cüh  'Stock',  s.  hier Nr.  432];  hieraus  rum.  ciuhuc  'Pfeifen- rohr; Gesimskranz',  bulg.  serb.  cihuk, russ.  klruss.  öubuk,  poln.  ci/buch,  öech. cibuk  'Pfeifenrohr,  Pfeife,  Mundstück'. [Gorjajew  417.    Bern  SlElWb  l.ö6.
```


## [2026-09-05T15:01:13.785Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT ctx around 1183 ===\"; sed -n '1175,1190p' LKT.txt; echo; echo \"=== which leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /Pfeifenrohr; Gesimskranz/ {print \"leaf(1-based)=\"NR}' LKT.txt",
 "description": "LKT cubuk entry"
}
```


## [2026-09-05T15:01:15.006Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf121 (p.100) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==122' HRN.txt | head -40",
 "description": "Horn p.100"
}
```


### [2026-09-05T15:01:17.296Z] TOOL RESULT

```
=== LKT ctx around 1183 ===
auf  den  Pferdesattel  legt ;  Pferdedecke' ; hieraus  ruiii.  cioltar  'Schabracke'.
444.  Tk.  cullama:
'Speise,  die  oben  mit  Teig  bedeckt  ist'; hieraus  mit  leicht  erklärlichem  Bedeu- tungswandel[Bedeutungsverengung]rum. ciulama  'ein  gekochtes  Huhn  mit  einer dicken,  breiigen  Tunke  gemischt'.
445.  Tk.  cuina:
'Pest'  [nicht  bei  Kelekian,  aber  bei Hindoglu,  Dictiounaire  Turc-Fran(^ais. Vienne  1838.  S.  rJ2a,  synonym  mit jumnigak  Test'  awsjumni  'rund,  Beule' ; vom  Stamme^Mm,  cum,  s.  hier  Nr.  438]; hieraus  rum.  ciiiina,  bulg.  serb.  klruss. cutna.  poln.  dzuma  'Pest',  russ.  cuma Test,  Seuche'.  [Die  Zurückführung  auf lat.  cijma,  gr.  KÜjua  'Sprofs'  scheint  doch sehr  zweifelhaft,  da  das  Wort  in  den romanischen  Sprachen  in  der  Bedeutung 'Pest'  nicht  allgemein  vorkommt.]  [Bern SlEtWb  163.
446.  Tk.  cürük :
'Verfault'  [vom  Stamme  tir,  tiir,  til,  eil, cur:  cilrümek  'verfaulen'  Vämber}'  Tkt EtWb  S.  177,  Nr.  190  IV];  hieraus  rum. ciuruc  'Abfälle,  Gesindel'.
447.  Tk.  cybuk:
'Pfeife'  [vom  pers.  cüh  'Stock',  s.  hier Nr.  432];  hieraus  rum.  ciuhuc  'Pfeifen- rohr; Gesimskranz',  bulg.  serb.  cihuk, russ.  klruss.  öubuk,  poln.  ci/buch,  öech. cibuk  'Pfeifenrohr,  Pfeife,  Mundstück'. [Gorjajew  417.    Bern  SlElWb  l.ö6.
448.  Tk  cykryk:
'Rad';  hieraus  rum.  cicric  'Rädchen, Haspel'.
449.  Tk.  cykyu :
'Gruppe;  Paket  Gold-  oder  Silbergeld' [Kelekian  Kämüs  488  a];  hieraus  rum. ciochinä  'Sattelknopf.  —  Löbel  EITAP 32  fragt  nachdem  Bedeutuugszusammen- hang  zwischen  rum.  ciochinä  und  tk. cykyn.  Dieses  letztere  war  das  Geld, das  die  Großen  der  Hohen  Pforte  ver- teilten, wenn  bei  einer  Feuersbrunst die  Feuerwehrleute  angespornt  werden sollten;  es  war  also  weggeworfenes  Geld, das  man  ebenso  gut  unnütz  an  den Haken  oder  wie  wir  im  Deutschen  zu sagen  pflegen  ,an  den  Nagel  hängen" konnte.  Im  Rumänischen  sagt  man nun  genau  so  a  pnne  la  ciochinä  im Sinne  von  'beiseite  werfen'.  Der  Zu- sammenhang mit  der  Bedeutung  'Schnal- le, Haken,  Sattelknopf  wird  so  ziemlich einleuchtend.
450.  Tk.  cyrpy:
'Gestrüpp,  abgeschnittene  Baumzweige, Meßschnur'  [Kelekian  Kämüs  468  b]; hieraus  rum.  ciripie  'Meßschnur,  geracle Linie'.
451.  Ar.  dabarän:

=== which leaf ===
```


### [2026-09-05T15:01:23.197Z] TOOL RESULT

```
=== HRN leaf121 (p.100) ===
--- 100 -^
Lässt sich lautlich nicht mit skr. kSupa- 'Staude,
Busch', wozu es vielfach gestellt wird, vermitteln ; nur
das kurd. sltv, sowie die Formen der Pämirdialekte
könnten zu dem Sanskrit stimmen.
449. eögän 'Schläger (im Ballspiel)'^).
Das Wort sei hier nur wegen seiner in semitischen
Sprachen vorkommenden Formen angeführt, welche
ich der Freundlichkeit Herrn Prof. Nöldeke's ver-
danke.
*syr. |W':51l^tDN (wie Fraenkel, Fremdwörter, S. 291
das entstellte ^''jlt'ICOl^N verbessert); arab. sauljän;
phlv. jNJIDIli (Kam.), wie vielleicht auch die np. Neben-
form öölgän in cöhgän zu emendiren ist. In jüngeren
arab. Texten (1001 Nacht) erscheint jNt'Di:!, das nicht
aus JNÄlli erklärt werden kann .
450. cun Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
phlv. digün *wie?* {ci + aw. gaona-), cigämh, vergl.
np. cigüne (vergl. zeryün aus aw. zairLgaona-, No.661).
451. ci(h), ci (AM.) was?, wie?\ cirä warum?*.
ap. üyakaram, -ciy (enclit.); aw. eis, cit; päz. ci/i
(phlv. no); ai. -6it (enclit.).
af}'. ca 'was?; einige*; oss. d. ci, ci, t. ci 'was, was
für ein, welch?' (322).
Als Encliticon hat Salemann, Mel.asiat.IX,241 altes
ap. ciy, aw. cit in den dialektischen tnvn ji auch ich*
(Lokalität Sih dih bei Isfahän), memc *ich auch*, öle
'er auch' (Güräni), sowie in mehreren gebräuchlichen
neupersischen Worten erkannt {kes, heö, hergiz^ mz^
egerci, herci temämter), die sämmtlich an ihrem Orte
aufgeführt sind. Im PehlevT wird das Encliticon noch
») Im Journal Bomb. Br. R. As. Sog. 1891, Vol. XVIII, 39 ff. hat
Jivanji Jamshedji Modi kürzlich die Stellen gesammelt, an denen
bei Firdüsl vom Ballspiel die Rede ist (The Game of Ball-Bai -- Chowgän-
gui — among the ancient Persians, as described in the Epic of Fir-
dousij.
') Cu ist metrisQh nur kurz, die Länge dazu ist cün (Rüokert,
ZDMO. 10, 133). Cünän z. B. äähn. I, 148 Vera 354, cümn 157 Vers 523.
```


## [2026-09-05T15:01:38.408Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT chicane ===\"; grep -n -i \"chicane\" SKT.txt | head; echo \"=== SKT leaf107 (p.87) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==108' SKT.txt | head -60",
 "description": "Skeat chicane"
}
```


## [2026-09-05T15:01:39.445Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 chibouk ===\"; grep -n -i \"chibouk\\|chibouque\\|chibuk\" KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN chicane ===\"; grep -n -i \"chicanery\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Klein chibouk/chicane"
}
```


### [2026-09-05T15:01:41.300Z] TOOL RESULT

```
=== SKT chicane ===
3373:Chicanery,  y  F.  -  Pers.  ?)  F,  rt wraiiyling.  pettifogging;  Cot. —  Fa to  wraftjilc;  orig.  to  dispute  in of  the  mail  or  ckicam  (UrachctV <hica$u  is  from  the  medieval  Gk. a  woid  of  HyiantJue  oiigtn  (.id.; from  PcTS-  ehau^H^  a  club.  bat.  I
=== SKT leaf107 (p.87) ===
Mwx/i ciomsed,  benumbed ;  benumbed  fingers  are clumsy.    This  is  the  pp.  of  clomsen,  to  be- numb, or  to  feel  benumbed.  — Swed.  dial. klummun^   benumbed    (Kicti) ;    cf.   IceL klumsa,  lockjaw.     From   the  Teut.    base KLAM,    KRAM,  to   pinch,    whence  also Clamp.    Cramp.     Cf.    Du,    kUmmen,    to pinch.  •^/<'tf/ru-»,  to  be  betiumbed,  kleumsch^ numb  with  cold. Cluster,  a  bunch,    (E)      A.  S.  dtattr, clysUr,  a  bunch.     Allied  to  led   ilAstr^  a bunch,   klasi,  a  duster;  Dan.   and  Sw klau,  %  duster.     We  also  find  Swcil.  d klyi$e,  the  same  as  klifsa,  a  daslcr,  from klibba,  to  cleave,  stick  to.     This  links  it  to Cleave  (j). Clutch :  see  Latoh. 'Clutter  (I),  a  din ;  sec  Clatter. -Clutter  ^a),  to  clot ;  see  Olot. Clutter  (3>,  a  confuseil  heap;  to  hea up.  (W.)     W.  ^/JM^/,  a  heap,  pile;  cl\ einv.  to  heap  up ClysLer.  ^U-Gk.)    L.  cl/tfer,  *o
JO
B6
CO-
tiod  into  the  bowels.  —  Gk.  mXpcr^p,  a. clyster,  syringe. •- Gk.  mk^Cur^  to  wuh.4' L.  cJuert.  to  wash.     (^KLU.)
Co-,  prctix.  (L.)  L.  c€',  to;;;cther:  used for  <■«••  (  — rw«>,  together,  before  a  Towel. Hence  co-t^itnt^  ca-tqnal,  co-opcraUf  €0- of^ItHate.  See  otben  below ;  and  see Con-.
Coach.  (F.-Hunjj. :  or  F.-L.-Gk.) F.  coeh^,  '  a  coach;'  Col.  Elym. dispnted  ; it  was  Eaid,  as  early  as  a.d,  1553.  to  be  a Hang&riui  word  ;  from  Hung.  Jt&csit  a coach,  so  called  becaose  first  made  at  a Hung,  Tillage  called  JCfftsi ;  see  Littr^,  and Bcckmann,  Hi&t.  of  Inventions.  Still,  it seems  10  have  beco  confused  with  F.  cocfu^ a  kind  of  boat  (E.  eark-boai),  see  Littr^. This  is  derired  from  L.  cffncha,  a  shcU. conch  ;  see  Oonoh.
Coadjutor ;  see  Aid.
Coagulate;  see  Agent.
CoaL  (E)  M.E.  w/.  A.  S.  «/.+Du. kocf,  Iccl.  Swed.  M  Dan.  kui,  G.  kohU. Cf.  Skt-yt-d/,  to  bUie.
collier.  (E.)  M.E.<v/i>r;  from  M.  £. «/,  coal.     CC  baW'fer,  saw-yer*
Coaleaoe :  see  AUmenk
CoftTM;  sec  Cxxrrent.
Co&Bt.  (F.  -  L.)  M.  E.  t6st€.  -  O.  F. costt  (F.  c$U),  a  rib,  slope  of  a  hill,  shore, w  L  casta,  a  rib.
accost,   to  address.    (F.  -  L.)     O.  F.
arcosUr,  to  come  to  the  side  of.  —  Low  L.
arcojfart.^h.  ac-  {aJ);  and  cosfaf  rib,  side.
OOet&l,  relating  to  the  ribs.  (L.)     From
L.  tatts,  a  rib.
cutlet  (F.-L.)  F.  cfffeUeff,  a  cutlet; formerly  ccsteUttt,  a  little  rib;  dimin.  of coste,  rib  (above).
Coat;  see  Cot.
Coax.  (C?)  FonnerlT«*«,  vb.,  from eekes,  sb.,  a  simpleton,  dupe.  Perhaps  from W.  .-*v^,  vain,  foolish,  €otgyn^  a  conceited fellow;  Com.  toe,  rain,  fooli&h,  O,  Gael. rand,  void,  ^'gev^t  a  coxcomb.  See Cocker,  Cog  (1).
Cob  (i),  a  round  Inmp,  knob.  (C.)  As applied  to  a  po  y.  it  means  short  and  stout. M.  E.  ioh,  a  head,  a  person.  —  W.  cob,  a tuft,  a  spider,  ccp,  a  tult,  top  ;  €0/<i,  crown of  the  head.
cobble  (a),  a  small  round  lump.  (C.) M.  E  coiiyhtcne,  a  cobblC'Stone.  JUiaijn. of  W.  (ob,  a  tuft  (abovcy
cobweb.  lC.  anJ  E.)  From  W.  ceh,  a k*pi'1cT;  Of  fchort  for  M.E.  atUnap-wih, wlere  att4n9/>,  a  spider,   means  'potton-
COCK.
bunch,'  from  A.  S.  ^r,  poUoQ,  and  c^ a  bead,  tuft,  borrowed  from  W.  co6,  t»f, before.
Cob  (3>,  to  beat.    (C.)     W.  (Ok, thump ;  d  cobt  a  bunch.
Cobalt,  a  mioerel  (G.-Gk)  G cobalt ;  a  nickname  given  by  the because  considered  poisoaoos ;  better  cpi jkabo^,  meaning  (1)  a  demon,  (3)  cobalt. Low  L.  coba/us,  a  mountain-sprite,  dead *Gk.  it60a)Kos,  a  rogue,  goblin.
goblin.  (F.-U-Gk.)  O.P.  mMj —  Low  L.  gobilinm,  dimio.  of  Low  i cohaim  (aboT
```


### [2026-09-05T15:01:41.368Z] TOOL RESULT

```
=== KLN 1966 chibouk ===
KLN_1971.txt:45082:chibouk, chibouque, n., a Turkish tobacco 
KLN_1971.txt:45083:pipe. — F. chibouque , fr. Turk, chubuq, chibuq, 
KLN_1966.txt:7385:chiastolite,  n.,  a  variety  of  andalusite  (mineral.) —  Compounded  of  Gk.  yla.a'coc,  (see  prec. word)  and  Xt&o;,  ‘stone’.  See  -life,  litho-. chiaus,  n.,  a  Turkish  messenger.  —  Turk,  chd- wush,  chaush.  See  chouse, chiave,  n.,  clef  (music).  —  It.,  ‘key’,  fr.  L.  clavem, acc.  of  clavis,  ‘key’,  whence  also  F.  clef,  ‘key’. See  clavicle  and  cp.  clef,  conclave, chibouk,  chibouque,  n.,  a  Turkish  tobacco pipe.  —  F.  chibouque,  fr.  Turk,  chubuq,  chibuq, ‘pipe’,  prop,  meaning  ‘stick,  staff,  tube’,  and rel.  to  chub,  ‘stick,  staff’, chibrit,  n.,  elemental  mercury  supposed  to  pro¬ duce  metals  (alchemy).  —  Arab,  chibrtt,  ‘sulfur’, rel.  to  Heb.  gophrith,  Jewish-Aram.  guphrithd, kubhrithd,  Christ.-Palest.  Aram,  guphri,  Syr. kebhrithd,  Akkad,  kupritu,  ‘brimstone,  sulfur’, chic,  n.,  style,  elegance.  —  F.,  prob.  fr.  G.  Schick, ‘fitness,  tact,  skill’,  fr.  MHG.  schicken,  ‘to  ar¬ range,  set  in  order’,  whence  G.  schicken,  ‘to send',  Geschick,  ‘fitness,  aptness,  fate,  destiny’, Schicksal,  Schickung,  ‘fate,  destiny’. Derivatives:  chic,  adj.  and  tr.  v.
=== KLN chicane ===
KLN_1971.txt:41894:nia , ‘false accusation, chicanery’; see calumny 
KLN_1971.txt:45109:chicane, n., chicanery. — F., ‘quibble, evasion’, 
KLN_1971.txt:45116:Derivatives: chican-er, n., chicanery (q.v.) 
KLN_1971.txt:45117:chicanery, n., trickery, quibbling, sophistry. — 
KLN_1966.txt:6871:Cavia,  n.,  the  genus  of  cavies,  the  guinea  pig (zool.)  —  ModL.,  fr.  F.  cabiai,  from  a  Carib¬ bean  native  word.  Cp.  cavy,  capybara. caviar,  caviare,  n.  —  F.  caviar,  fr.  It.  caviaro  (now caviale),  fr.  MGk.  xaptxpiov,  fr.  Turk,  khavidr, fr.  Kaffah  (=  Theodosia),  name  of  a  trading town  on  the  SE.  shore  of  the  Black  Sea. cavicorn,  adj.,  hollow-horned.  —  Compounded of  L.  cavus,  ‘hollow’,  and  cormi,  ‘horn’.  See cave,  n.,  and  horn  and  cp.  corn,  ‘hardened  skin’. Cavicornia,  n.  pi.,  another  name  for  Bovidae (zool.)  —  Lit.  ‘hollow-horned’.  See  prec.  word, cavil,  intr.  v.,  to  find  trivial  faults,  to  carp.  — OF.  caviller,  fr.  L.  cavilldri,  ‘to  jest,  joke,  make captious  objections,  to  cavil  at’,  fr.  cavilla,  ‘jest, quibble,  trick’,  dissimilated  fr.  *calvilla,  and rel.  to  calvi,  ‘to  devise  tricks,  use  artifice’,  calum- nia,  ‘false  accusation,  chicanery';  see  calumny and  cp.  challenge.  For  the  suff.  cp.  L.  favilla, 'glowing  ashes,  embers'  which  is  rel.  to  fovere, ‘to  warm,  keep  warm'.
KLN_1966.txt:7386:chicane,  n.,  chicanery.  —  F.,  ‘quibble,  evasion’, fr.  chicaner.  See  chicane,  v. chicane,  intr.  v.,  to  trick.  —  F.  chicaner,  ‘to quibble,  wrangle,  quarrel’,  of  uncertain  origin; prob.  not  related  to  MHG.  schicken,  ‘to  arran¬ ge,  set  in  order’  (see  chic).
KLN_1966.txt:7387:Derivatives:  chican-er,  n.,  chicanery  (q.v.) chicanery,  n.,  trickery,  quibbling,  sophistry.  — - F.  chicanerie,  fr.  chicaner.  See  chicane,  v.  and -ery.
```


## [2026-09-05T15:01:52.752Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Chicanery')\nprint('leaf(1-based) =', t[:i].count('\\f')+1)\nprint(repr(t[i-1500:i+600]))\nEOF",
 "description": "Locate Skeat chicane leaf"
}
```


### [2026-09-05T15:01:54.295Z] TOOL RESULT

```
leaf(1-based) = 100
' Curtius dcMibis.\nChert,  a  kind  of  quarti.  (C?)  The Keiitiib  form  ts  chart,  rough  ^ruuniL  Pro- bably from  Irish  ceart,  a  i«:bble;  cf.  Gael. *WT,  a  shelf  of  rock,  W.  carts»  stone\nCherub.  (Heb.)  The  inie  pi.  is  iMentb- $m,  «  Hcb.  k\'nlv  ^pl.  k^nivim),  a  mystic ficure.\nCh«Trtl»  a  plant,  (U-Gk.)  A.S.  r<rf- ^//.  —  L.  cartjolium  (Pliny),  — Gk.  x^f><- fw^Xo•\',  chervil,  Itt.  plea&ant  leaf.-Gk. Xaf»-\'«i\',  to  rejoice ;  ^^vXAoa*,  leaf.\nChvBa ;  see  Oheok.\nChast  Cl— Gk.)  M.E  chestt,  chistt. A.S.  cyiti.^L.  nJ/a.-Gk.  Kltrnj,  a  chest. box  (whence  G. kiste.  Sec)\ndat,  a  soit  of  tomb.  (L. «  Gk.)  h.  <utci ; SI  above.\noistem.  (F.-L.-Ck.)  T.eu/emf.-^ L.  cisttfma^  a  re&crvoir  for  vralcf.— L,  iistm (above).\nChestnut.  Chesnut.  (F.-L..Gk) Cktmut  is  short  for  cktstant,  which  is shoit  for  cktstm-nut,  nut  of  the  cJUtten, which  is  the  old  name  ol  the  tree,  called in  M.  E  iA€JttiH.  ••  O.  F,  ekaseai^fu  ^F. tkJt*ij(m).^L.  tmstama^  chestnut -tree.  • Gk.  «arT«j>or,  a  cbcstnut ;  checnuu  were •Ikllcd  ««#nva.  or  mt/wa  KiAr«rnra,  from\nOik\nKtiffTova,  Ca^tana,  the  name  of  a  dt}j PontDs  where  tlicy  abounded-\nCheval-de-frlse,  an  obstnK sj\'ikes.  (FO     Ul.  \'horie  of  Fri( jocular  name ;  the  pi.  iktvamx-Jt-i commoner.\nChevalier :  see  Cavalier,\nChew,   Chaw.    ^E)      M.  E A.S.  f^rwjw.  lochcw.eaL  +  Du. G,  kaucn  ;  Rtiss.  Jafaf9,     Der. a  jaw;  now  spclt/dtv.\nChicanery,  y  F.  -  Pers.  ?)  F,  rt wraiiyling.  pettifogging;  Cot. —  Fa to  wraftjilc;  orig.  to  dispute  in of  the  mail  or  ckicam  (UrachctV <hica$u  is  from  the  medieval  Gk. a  woid  of  HyiantJue  oiigtn  (.id.; from  PcTS-  ehau^H^  a  club.  bat.  I\nChicken.    (E)     Somciimes  sh«tt| to  ekiik\\    bnl  the  M.  E.   wonl A.  S.  ticm  ^.for  eycen  •.  not dimin,  oitocc,  acock  (cf.  k^ So  also  Du.  *rVAf#(,  *"\'■"" pears  to  be  a  diniin. cock  ;  cf  E.  ekuck,  a G.  kiichUifh  «  chicken.      %  Moie  \\ aot  an  exact  dimiii.  of  <0cc.  but  f(<« same  imi'
```


## [2026-09-05T15:01:55.618Z] TOOL CALL #14: Bash

```json
{
 "command": "ls site/pages/107.jpg 2>/dev/null; pdftoppm -f 107 -l 107 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg107\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render page 107"
}
```


### [2026-09-05T15:01:58.431Z] TOOL RESULT

```
site/pages/107.jpg
total 32828
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 11:01 .
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


## [2026-09-05T15:02:09.749Z] TOOL CALL #15: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/107.jpg"
}
```


### [2026-09-05T15:02:09.779Z] TOOL RESULT

```

```


## [2026-09-05T15:02:18.897Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD cwb/cob ==\"; grep -n -i \"c'ob\\|čōb\\|cob \\[\\|cwp\\|čōbag\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== PHD grep 'wood' near c ==\"; grep -n \"cwp\\|cōb\\|cob,\" PHD_mackenzie.txt | head -20",
 "description": "MacKenzie cob"
}
```


### [2026-09-05T15:02:18.951Z] TOOL RESULT

```
== PHD cwb/cob ==
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:303:3b [cwp | N ~) wood, stick.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD_mackenzie.txt:1749: ·~aw(la)gAn [cwpk)n' ! I Ar. ~awlaJiin, N laugiin] (curved) polo-stick; polo.
PHD_mackenzie.txt:5777:   ...... -~obag [.cwpk I N ......caba] turmeric.
== PHD grep 'wood' near c ==
1749: ·~aw(la)gAn [cwpk)n' ! I Ar. ~awlaJiin, N laugiin] (curved) polo-stick; polo.
5777:   ...... -~obag [.cwpk I N ......caba] turmeric.
7969:where kii (gyag).                      wood cob, dar; wesag.
```


## [2026-09-05T15:02:20.841Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB ==\"; grep -n -i \"čōb\\|cob 'Holz'\\|čōgān\\|cōgān\\|čaugān\" HUB.txt | head -20; echo \"== NYB ==\"; grep -n -i \"cōp\\|čōp\\|cwp\" NYB_vol2_glossary.txt | head -20",
 "description": "Hübschmann and Nyberg"
}
```


### [2026-09-05T15:02:20.902Z] TOOL RESULT

```
== HUB ==
== NYB ==
1163:eovčgan [cwpyg’n'] the stick used in playing polo 16!!; the game of polo itself 314.15, 49. 167. — NP caugän; Arab. lw. saulajün-; Fraenkel, Aram. Fremdw. 291; Horn, NP Et. no. 499 and Hubsehmann,
```


## [2026-09-05T15:02:33.383Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,pat,off in [('PHD.txt','3b [cwp | N ~) wood, stick.',21),('PHD.txt','*taw(la)gan [cwpk',21),('NYB_vol2_glossary.txt','[cwpyg',8)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.find(pat)\n    leaf=t[:i].count('\\f')\n    print(f,pat[:20],'leaf0=',leaf,'printed=',leaf-off)\nEOF",
 "description": "Compute PHD/NYB pages"
}
```


### [2026-09-05T15:02:35.284Z] TOOL RESULT

```
PHD.txt 3b [cwp | N ~) wood, leaf0= 45 printed= 24
PHD.txt *taw(la)gan [cwpk leaf0= 44 printed= 23
NYB_vol2_glossary.txt [cwpyg leaf0= 67 printed= 59
```


## [2026-09-05T15:02:35.761Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== TTS cubuk ==\"; grep -n -i \"cubuk\\|čubuk\\|tschybyk\\|cypyk\\|cyb\" incoming/TTS/TTS_pages.txt 2>/dev/null | head -20; echo \"== ARY چوب ==\"; grep -n \"چوب\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY چوگان ==\"; grep -n \"چوگان\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Vambery and Aryanpur"
}
```


### [2026-09-05T15:02:35.851Z] TOOL RESULT

```
== TTS cubuk ==
== ARY چوب ==
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
3190:باهو (به چم"چوبدستی بزرگ» "دیرک") / ۱۱۱
3226:این باشد که پل‌های اولیه را از تیرهای چوبی می‌ساختند. ۱ ید
4977:معنی واژه‌ی ۳08718 در زبان لاتین: یاهر (هریکك از دو تبر عمود چارچوب در).
6146:۱- چم اين واژه در زبان‌های ژرمنی: چوبدستی. َ
7663:۱ در بیشتر زبان‌های هند و اروپایی این واژه هم به چم آدرخت" و هم به چم "چوب" بکار می‌رفته.
10090:چم این واژه در گوتبک و بونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی. :
10246:چم این واژه در زبان یونانی: چوبدستی» خصاء
10274:ِ چم اين واژه در زبان‌های ژرمنی: چوبدستی.
10947:چم‌های این واژه در دیگر زبان‌های هند و اروپایی این فهرست؛ تیر چوبی» ستون چوبی؛ دیرک
== ARY چوگان ==
```


## [2026-09-05T15:02:43.353Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON چپق ==\"; grep -n \"چپق\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head -8; echo \"== MON چوگان ==\"; grep -n \"چوگان\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head -8",
 "description": "Mo'in grep"
}
```


### [2026-09-05T15:02:43.419Z] TOOL RESULT

```
== MON چپق ==
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34020:پیپ: «آ (.) چپق کوچک دسته کوتاه 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:49786:دسته‌ای چوبی و سرسفالی. توتون چپق را 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:76631:چپق متصل سازند. داخل آن را از زغال 
MON_part1.txt:34020:پیپ: «آ (.) چپق کوچک دسته کوتاه 
MON_part1.txt:49786:دسته‌ای چوبی و سرسفالی. توتون چپق را 
MON_part1.txt:76631:چپق متصل سازند. داخل آن را از زغال 
== MON چوگان ==
MON_part1.txt:33755:چوگان که سر آن مانند کفچه پهن است و 
MON_part1.txt:51660:چوگان: (66:10) 2۳257 (امر.) چوبی که 
MON_part1.txt:51663:(چوگان‌بازی) گوی زنند. هر چوب سر کج 
MON_part1.txt:51670:چوگانی : (-.00080-1)060 (ص‌نست.) استی 
MON_part1.txt:51671:ورزیده که مناسب چوگان‌بازی باشد. 
MON_part1.txt:71027:گوی چوگان 3 جناغ رین سازند؛ درخت 
MON_part1.txt:90586:صولجان: (2۷/۱2[20)50۷۰: [معر . چوگان] 
MON_part1.txt:90587:.( چوگان. عصا» عصای شاهی» ج.
```


## [2026-09-05T15:02:44.084Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt; do echo \"== $f چپق ==\"; grep -n \"چپق\" $f | head -5; echo \"== $f چوگان ==\"; grep -n \"چوگان\" $f | head -5; done",
 "description": "Borhan grep"
}
```


### [2026-09-05T15:02:45.755Z] TOOL RESULT

```
== BQT_v2_pages.txt چپق ==
4568:   ‫‪ #‬چپق ‪ -‬سم اول و دوم ازترکی«چوبوق»» درجغتابی بمعنی لولة چپق ‪ ,‬قطمه چوب‬
== BQT_v2_pages.txt چوگان ==
6130: ‫‪ - ۷‬چفته دریزد چوگانی راست ومنقش رکاوبندکه بطول‬           ‫‪ - ۱‬رك‪ :‬چفت‪.‬‬
6877:   ‫َ‪۱‬‬     ‫قامت چون سرو وزلقکاش چوگان ‪.‬‬                          ‫از کفنر کی سیاه چمش پری روی‬
7611:   ‫‪ _۴‬اتی در «چوگان» (<‪۰‬م‪ ).‬بامسحف «چوپگان»یپلوی‪.‬‬         ‫اء غا ‪۱ ۲ :۱‬ص‪٩‬ض‪۰۳۰۳۱۵‬‏ ‪.‬‬
40806:                                         ‫«چوگان» ‪۰‬‬    ‫معرب‬‫‪۸‬‬             ‫آذرکیوان ‪ .‬رك ‪ :‬سیم‬
== incoming/BQT/BQT_v3_pages.txt چپق ==
== incoming/BQT/BQT_v3_pages.txt چوگان ==
```


## [2026-09-05T15:02:54.145Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nf='BQT_v2_pages.txt'\nlines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\ndef pagetag(n):\n    for i in range(n,-1,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n        if m: return m.group(1),i\n    return None,None\nfor n in [4568,7611,6877]:\n    print(n, pagetag(n-1))\nprint('---context 4560-4580---')\nprint('\\n'.join(lines[4558:4578]))\nprint('---context 7600-7620---')\nprint('\\n'.join(lines[7598:7620]))\nEOF",
 "description": "Borhan page tags and context"
}
```


### [2026-09-05T15:03:00.066Z] TOOL RESULT

```
4568 (None, None)
7611 (None, None)
6877 (None, None)
---context 4560-4580---
           ‫بیداد گرست و چیلك» بخرد ومت‪.‬‬            ‫بنشست‬     ‫دواری‬
                                                                 ‫ا انز ن‬
                                                                       ‫پجز‬
                                                                         ‫جو ب‬
                                                                            ‫هبر ک‬
    ‫«منوچهری بنقل جهانگیری ورشیدی»‪.‬‬
  ‫‪ « 20020 _ ¥‬هوشمان ‪ »0۳‬؛ چیه شدن؛‬                     ‫‪ - ۱‬رك ‪ :‬چاپلوی » چابلوی ‪.‬‬
               ‫یکو افتادن اتومبیل درحین حر کت ( اصطلاح رانند کان) ؛ رك‪ :‬چپسدن‪.‬‬

   ‫‪ #‬چپق ‪ -‬سم اول و دوم ازترکی«چوبوق»» درجغتابی بمعنی لولة چپق ‪ ,‬قطمه چوب‬
                                ‫فابل انمطاف » شاخ کوچك س‪«.‬بجفتابی‪121001010 .)۱۹۲‬‬

               ‫ی‬                    ‫فراسه از همینکلمة ترکیمأخون است‪ .‬آتلدتخین م رکب‬
                                                                             ‫از حقه‌ای ک‬
                                       ‫نلکیه در آن توتون ریزند بداسته ای چویین‬
                ‫جیق‬          ‫ومجوف کهاتهای آن بحقه متصل است و سر آنرا دردهان گذارند ‪.‬‬

                                                             ‫رك ‪ :‬چیق ‪.‬‬   ‫‪ #‬جو ق ‪-‬‬
 ‫‪YY‬‬                                                                                             ‫چیدن‪‎‬‬

---context 7600-7620---
  ‫«هوبشمان‪»4 4‬معرب آن صولجان " وکمةٌ فرانوی ‪ 611201016‬ازفارسی‌مأخون امت « اسفا ‪۱:۲‬‬
 ‫‪۴‬خ‪-‬تی حر‬   ‫ص؟‪ .‬‏ در بوت‪1‬ان‪2‬ي‪ 00108511‬آلمانی‪ « 0082005‬دائرة المعارف اسلام » ‪ .‬ل‬
                                              ‫ی( نبت ) ‪:‬‬         ‫‪ - ۴‬از ‪ :‬چوکان‬        ‫«چگون» و«چگونه»‪.‬‬
             ‫‪۰‬‬    ‫سرد‬   ‫را بچ وکانی خود‬           ‫عنان‬                 ‫سکندر که ازخروان گوی برد‬
  ‫نظامی گنجوی« کنجینه»ع» ‪.‬‬
  ‫‪٩‬‏ ‪ -‬باین‌معنی«تر کی» است«جفتای ‪ ۷۹۲‬؟‪.‬‬                        ‫رکک‪ :‬چغو‪ .‬چفد‪ .‬جفد‪ .‬ورك‪ :‬چفك‪.‬‬                      ‫©‬
            ‫«لغت‌فری ‪۳‬‬           ‫«چول› خمنده بود › مصراع ‪ :‬زلفك جول و آنرخان‌چوماء»‬                            ‫‪¥‬‬

                      ‫رکه ‪ :‬چر (ضم اول) وچل بضم اول‪ ,‬نیز درتر کی «چو کث»(«‪.‬م‪).‬‬ ‫‪۸‬‬
                                  ‫‏‪ = ٩‬چون ‪ +‬آن ‪ .‬رک ‪ :‬اسفا ‪ ۲ : ۱‬ص‪.۰۳,۰۲۱۰۵۹۱‬‬
  ‫لد این ‪.‬ر کث‪:‬‬         ‫چون‬      ‫=‬   ‫‪۱۱‬‬            ‫شده ‪.‬‬   ‫(ه‪.‬م‪ ).‬خاط و تخت‬           ‫با«چونن»‬   ‫ظ‪.‬‬       ‫‪--‬‬    ‫‪۶‬‬

   ‫‪ _۴‬اتی در «چوگان» (<‪۰‬م‪ ).‬بامسحف «چوپگان»یپلوی‪.‬‬         ‫اء غا ‪۱ ۲ :۱‬ص‪٩‬ض‪۰۳۰۳۱۵‬‏ ‪.‬‬
                    ‫‪ ¥‬جوماق ‌‪ -‬رک ‪ :‬جماق ‪۰‬‬        ‫* چولاق رک ‪ :‬چلاق ‪.‬‬
   ‫(ونه‌رنك )‪ .‬مخفف آن» چو‬
                         ‫‪ #‬چون ‪ -‬پهلوی ‪ 0081‬از (»(چه) ‪ 201028 +‬گ‬
   ‫«نیب رکك ‪« »4 4‬تاوادی‪4۵۱‬؟؛ *بوستی ‪ .‬بندهش ‪۱۲۱6‬؛ چگونه ‪ -.‬چسانب موثملانند(ر که‪:‬ص به‬
                                                         ‫‪-‬را ازبرای ‪ -‬وقتیکه» هنگامنکه‪.‬‬
                                                                                      ‫از دبباچة ملف) ز‬
                                    ‫بیان بیست و یکم‬
              ‫درجیم فارسی‌با ها مشتمل برسی و چهار لغت و کنات‬
```


## [2026-09-05T15:03:15.458Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt; echo ---; grep -n -o \"\\[pdf page [0-9]*\\]\" BQT_v2_pages.txt | head -3; echo \"--- formfeeds:\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff count',t.count('\\f'))\nimport re\nlines=t.split('\\n')\nfor n in [4568,7601,7611]:\n    i=sum(len(l)+1 for l in lines[:n-1])\n    print(n,'leaf0=',t[:i].count('\\f'))\n\"",
 "description": "Inspect BQT_v2 page structure"
}
```


### [2026-09-05T15:03:17.159Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
---
--- formfeeds:
ff count 683
4568 leaf0= 79
7601 leaf0= 129
7611 leaf0= 129
```


## [2026-09-05T15:03:22.306Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\"",
 "description": "BQT offsets"
}
```


### [2026-09-05T15:03:23.817Z] TOOL RESULT

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


## [2026-09-05T15:03:32.613Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (79,129):\n    p=t[n]\n    print('=== leaf',n,'first 3 lines / last 3 lines ===')\n    L=[l for l in p.split('\\n') if l.strip()]\n    print(L[:3]); print(L[-3:])\nEOF",
 "description": "Check running heads"
}
```


### [2026-09-05T15:03:34.370Z] TOOL RESULT

```
=== leaf 79 first 3 lines / last 3 lines ===
[' \u202bیه\u202c                                                                                     \u202b\u202a14\u202c\u202c', '\u202bبا کسی خود را یکی\u202c         \u202bبچسبانشد \u202a-\u202c\u202c     \u202bبچیزی\u202c    \u202bچیدار = با زای هوز بروزن مقراض »\u202c', '                                                  \u202bسر موزه راگوبند » وکآفنشی باشدکه مردم\u202c']
['                                       \u202bنلکیه در آن توتون ریزند بداسته ای چویین\u202c', '                \u202bجیق\u202c          \u202bومجوف کهاتهای آن بحقه متصل است و سر آنرا دردهان گذارند \u202a.\u202c\u202c', '                                                             \u202bرك \u202a :\u202cچیق \u202a.\u202c\u202c   \u202b\u202a #\u202cجو ق \u202a-\u202c\u202c']
=== leaf 129 first 3 lines / last 3 lines ===
[' \u202bچوبگان\u202c                                                                                                                \u202bسب \u202a۷\u202c\u202c', '\u202bوآن درتدهأ ست تامبارك و ددوسته در\u202c                    \u202bکون\u202c           \u202bبعنی\u200cبزانودرای \u202a .\u202cگوبند باین\u200cمعنی ترکی\u200cاست\u202a. ۱\u202c\u202c', '                                                                      \u202bجو گان \u202a = ۲\u202cبکااف فارسی بورزن\u202c']
['   \u202b«نیب رکك \u202a« »4 4\u202cتاوادی\u202a4۵۱\u202c؟؛ *بوستی \u202a .\u202cبندهش \u202a۱۲۱6\u202c؛ چگونه \u202a -.\u202cچسانب موثملانند(ر که\u202a:\u202cص به\u202c', '                                                         \u202b\u202a-\u202cرا ازبرای \u202a -\u202cوقتیکه» هنگامنکه\u202a.\u202c\u202c', '                                                                                      \u202bاز دبباچة ملف) ز\u202c']
```


## [2026-09-05T15:03:40.115Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T15:03:40.122Z] TOOL RESULT

```


```


## [2026-09-05T15:03:44.063Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%88%D8%A8",
 "prompt": "Give the Persian etymology section for چوب (čub) verbatim: Middle Persian form, Proto-Iranian reconstruction, cognates, and any cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-05T15:03:45.187Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%88%DA%AF%D8%A7%D9%86",
 "prompt": "Give the Persian etymology of چوگان (čowgān) verbatim: Middle Persian forms, whether it is derived from چوب, Arabic صولجان, Greek τζυκάνιον, and any cited authorities."
}
```


### [2026-09-05T15:03:49.422Z] TOOL RESULT

```
# Persian Etymology for چوب (čub)

Based on the Wiktionary entry, here is the etymology section:

**Middle Persian form:** [script needed] (cwp /⁠čōb⁠/, "wood, stick")

**Proto-Iranian reconstruction:** Not provided in this source.

**Cognates listed:**
- Central Kurdish _چێو_ (çêw)
- Northern Luri _چوو_ (çu)
- Sanskrit _क्षुप_ (kṣupa, "bush")

**Note on further connections:** "Further connections outside Indo-Iranian uncertain."

**Cited authorities:** 
The article cites MacKenzie, D. N. (1971) for the Pahlavi dictionary entry, but does not reference Hasandust or Cheung. The references section lists Steingass, MacKenzie, Horn, and Nourai as scholarly sources on this word's etymology.
```


### [2026-09-05T15:03:50.346Z] TOOL RESULT

```
# Persian Etymology of چوگان

Based on the Wiktionary content provided, the etymology information is limited:

The word is **inherited from Middle Persian** with two attested forms:
- *cwpkʾn'* (čōbagān, *čaw(la)gān)
- *cwgʾn'* (čōgān)

The source document does not provide information about:
- Whether it derives from چوب (wood/stick)
- Any connection to Arabic صولجان
- Any Greek etymology (τζυκάνιον)
- Citations to scholarly authorities on the word's origin

The entry only confirms the Middle Persian precedents without discussing the deeper etymological path or alternative theories about the word's ultimate source.
```


## [2026-09-05T15:03:53.788Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chicanery",
 "prompt": "Give the full etymology of chicanery and chicane verbatim, including any mention of Greek tzukanion, Persian chaugan, and the alternative Spanish/Latin proposals."
}
```


## [2026-09-05T15:03:54.786Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%C3%A7ubuk",
 "prompt": "Give the Turkish etymology of çubuk verbatim: is it from Old Turkic çıbık/çubuk, or borrowed from Persian? List cited sources."
}
```


### [2026-09-05T15:04:00.079Z] TOOL RESULT

```
Based on the provided content, I cannot give you the full etymology you're requesting. The page does not mention Greek "tzukanion," Persian "chaugan," or alternative Spanish/Latin proposals.

Here's what the source actually provides:

**Chicanery:** "c. 1610s, 'legal quibbling, sophistry, mean or petty tricks,' from French *chicanerie* 'trickery,' from *chicaner* 'to pettifog, quibble' (15c.), which is of unknown origin, perhaps from Middle Low German *schikken* 'to arrange, bring about,' or from the name of a golf-like game once played in Languedoc."

**Chicane:** The term derives "apparently all ultimately from an archaic verb *chicane* 'to trick' (1670s), from French *chicane* 'trickery' (16c.), from *chicaner* 'to pettifog, quibble' (15c.)."

Both etymologies remain uncertain, with the source acknowledging unknown origins and offering only speculative Germanic or French gaming connections—not the Middle Eastern or Romance language sources you mentioned.
```


### [2026-09-05T15:04:00.839Z] TOOL RESULT

```
Based on the Wiktionary content provided, the Turkish etymology of **çubuk** is:

The word is inherited from Ottoman Turkish *چبوق* (çibuk, çıbuk, çubuk), which derives from Proto-Turkic *\*čöpik* meaning "stick, twig."

**No Persian borrowing is mentioned.** The etymology traces the word back through Ottoman Turkish to Proto-Turkic roots.

**Cited sources:** The article does not provide explicit academic sources or citations beyond referencing Ottoman Turkish and Proto-Turkic as the etymological path. It relies on Wiktionary's internal structure linking to these language varieties.
```


## [2026-09-05T15:04:11.377Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/chicane",
 "prompt": "Give verbatim the TLFi etymology of chicane / chicaner: what origins are proposed and rejected, including any mention of Byzantine Greek tzukanion (τζυκάνιον) and Persian tchaugan."
}
```


## [2026-09-05T15:04:12.825Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/%C3%A7ubuk",
 "prompt": "Give the etymology of Turkish çubuk verbatim: Old Turkic forms, root, earliest attestation, and whether Persian is involved."
}
```


### [2026-09-05T15:04:16.387Z] TOOL RESULT

```
I apologize, but the web page content provided only shows "Portail lexical" (Lexical Portal), which appears to be a header or title rather than actual dictionary content containing the TLFi etymology for *chicane* or *chicaner*.

To provide the verbatim TLFi etymology with information about proposed and rejected origins—including any discussion of Byzantine Greek *tzukanion* (τζυκάνιον) and Persian *tchaugan*—I would need the actual lexicographical entry text from the TLFi (Trésor de la Langue Française informatisé).

Could you provide the full etymological entry from the TLFi?
```


### [2026-09-05T15:04:22.500Z] TOOL RESULT

```
I cannot provide the etymology of Turkish "çubuk" based on the content provided. The web page shown is merely the header and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website, containing navigation elements and copyright information, but not the actual dictionary entry for "çubuk" itself.

To obtain the etymological information you're seeking—including Old Turkic forms, root origins, earliest attestation, and Persian connections—you would need to access the full dictionary entry for this word on the Nişanyan Sözlük website.
```


## [2026-09-05T15:04:27.414Z] TOOL CALL #33: Bash

```json
{
 "command": "cd \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\" && curl -sL -A \"Mozilla/5.0\" \"https://www.cnrtl.fr/etymologie/chicane\" -o chicane.html; python3 -c \"\nimport re,html\nt=open('chicane.html',encoding='utf-8',errors='replace').read()\nt=re.sub('<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\\s+',' ',t)\ni=t.lower().find('tymol')\nprint(t[i-200:i+3000])\n\"",
 "description": "Fetch CNRTL chicane"
}
```


### [2026-09-05T15:04:33.668Z] TOOL RESULT

```
 Portail lexical
```


## [2026-09-05T15:04:38.408Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/chicane",
 "prompt": "Give the English and French etymology sections of \"chicane\" verbatim, including any mention of Byzantine Greek τζυκάνιον, Persian چوگان, Medieval Latin, or Spanish chico."
}
```


## [2026-09-05T15:04:38.562Z] TOOL CALL #35: WebSearch

```json
{
 "query": "τζυκάνιον tzykanion Byzantine polo Persian chawgān chicane etymology"
}
```


### [2026-09-05T15:04:42.242Z] TOOL RESULT

```
# Etymology Sections for "Chicane"

## English Etymology

"Borrowed from French *chicane*."

## French Etymology

"From *chicaner*, ultimately from Proto-West Germanic *\*skikkijan*. Related to French *chic*."

---

**Note:** The provided content contains no mentions of Byzantine Greek τζυκάνιον, Persian چوگان, Medieval Latin, or Spanish "chico" in either etymology section.
```


### [2026-09-05T15:04:48.294Z] TOOL RESULT

```
Web search results for query: "τζυκάνιον tzykanion Byzantine polo Persian chawgān chicane etymology"

Links: [{"title":"Etymology: Greek (suffix) - τζυκανιστήριον - tzykani(steria), tzykani(sterion) | WordReference Forums","url":"https://forum.wordreference.com/threads/etymology-greek-suffix-%CF%84%CE%B6%CF%85%CE%BA%CE%B1%CE%BD%CE%B9%CF%83%CF%84%CE%AE%CF%81%CE%B9%CE%BF%CE%BD-tzykani-steria-tzykani-sterion.3103387/"},{"title":"Tzykanisterion","url":"https://en.wikipedia.org/wiki/Tzykanisterion"},{"title":"About: Tzykanisterion","url":"https://dbpedia.org/page/Tzykanisterion"},{"title":"Polo | encyclopedia article by TheFreeDictionary","url":"https://encyclopedia.thefreedictionary.com/Polo"},{"title":"Polo - Wikiwand","url":"https://www.wikiwand.com/en/Polo"},{"title":"Polo - Wikipedia","url":"https://en.m.wikipedia.org/wiki/Polo"},{"title":"Chovgan facts for kids","url":"https://kids.kiddle.co/Chovgan"},{"title":"Tzykanisterion — Grokipedia","url":"https://grokipedia.com/page/tzykanisterion"},{"title":"Chovgan","url":"https://en.wikipedia.org/wiki/Chovgan"}]

Based on the search results, here's what I found about the relationships between these terms:

## Etymology and Etymology

The tzykanion (τζυκάνιον) is the Greek name for Chovgan, from Middle Persian čaukān, čōkān, a kind of polo adopted by the Byzantines from Sassanid Persia.

The adaptation from Sassanid Persian to Byzantine Greek involved the transformation of the initial affricate /č/ (as in čaukān) into the Greek cluster /tz/ (τζ), a palatalized sound typical in loanwords from Iranian languages, while the vowel sequence and final nasal were Hellenized to fit Greek morphology, resulting in forms like τζυκάνιον.

## Connection to Chicane

Regarding "chicane," the search results do not contain information connecting this term to tzykanion, chawgān, or the Byzantine polo game. If you're interested in exploring whether there's an etymological connection between "chicane" and these Persian/Greek polo terms, that would require additional research beyond what these results provide.

## Historical Context

The sport was very popular among the Byzantine nobility: Emperor Basil I excelled at it, his son Emperor Alexander died from exhaustion while playing, and John I of Trebizond died from an injury during a game.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T15:04:57.034Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== DEV chicane ==\"; grep -n -i \"chicane\\|tzycanion\\|tchugan\\|tchaugan\\|chaugan\" DEV.txt PHN.txt LAM.txt 2>/dev/null | head -20",
 "description": "Devic/Pihan chicane"
}
```


### [2026-09-05T15:04:57.085Z] TOOL RESULT

```
== DEV chicane ==
DEV.txt:1127:Chicane.  Ce  mot,  aujourd'hui  passablement  détourné de  son  sens,  a  dû  désigner  primitivement  le  jeu  du  mail.
DEV.txt:1130:D'après  Beschereile,  il  se  dit  encore  d'une  certaine  ma- nière de  jouer  au  billard,  au  maiil,  a  la  paumée  Dans certains  appareils  de  chauffage  et  de  ventilation,  on  ap- pelle chicanes  des  pièces  de  diverses  formes  disposées  de manière  à  contrarier,  à  diriger  successivement  en  divers sens  un  courant  d'air  chaud  ou  froid;  à  quoi  on  peut comparer  l'expression  des  marins  chicaner  le  vent.  De  plus, on  trouve,  en  bas  grec,  TlvKdviov\  jeu  de  mail;  t^vKavi- ^siv,  jouer  au  mail.  Tout  cela  ne  laisse  aucun  doute  sur l'étymologie  :  c'est  le  persan  (jt^j^  tchaugân,  bâton  re- courbé, maillet  pour  jouer  au  mail.  Aussi  comprend-on difïicilement  que  Diez  et  Génin  aient  voulu,  après  Mé- nage, chercher  l'origine  de  chicane  dans  l'espagnol  chico, petit,  qui  n'explique  ni  la  forme,  ni  les  sens  de  ce  terme. De  {J^y=^  cljôkân,  forme  arabe  de  Jf^iy^^  dérive  le  por- tugais choca.  (Voy.  Dozy,  Gloss.  p.  2  54.)  Le  changement  de ^  u,  ou,  ou  en  i  est  si  fréquent  qu'il  est  à  peine  besoin  de s'y  arrêter.
DEV.txt:1133:'  Voy.  Defrémery,  Mém.  d'hist.  orient,  p.  2  35.  Le  savant  professeur  cite un  passage  du  Voyage  de  Chapelle  et  de  Bachaumont,  ({ui  montre  qu'au XVII*  siècle  chicane  se  disait  du  jeu  du  mail  :  «Nous  y  arrivâmes  à  travers mille  boules  de  mail  :  car  on  joue  là,  le  long  dos  chemins,  à  la  chicane. '•
DEV.txt:3263:Chico,  esp.  voy.  Chicane.
DEV.txt:3269:Choca,  pg.  voy.  Chicane,
DEV.txt:4412:Térenjubin,  voy.  Téréniabin. Terniabin,  voy.  Téréniabin. Ti^/i^pa,  voy.  Chiffre. T^^vKixvi^eiv,  voy.  Chicane. T^vKÛvtov,  voy.  Chicane. Thérenjabin,  voy.  Téréniabin. Thuban.
DEV.txt:4740:djesm,  Corps. c->yLa^  voy.  Julep. ^j^j^s:;^  voy.  Zinzolin. Nn'?3'?3  voy.  Golgotha. (^^Ijr  voy.  Gemmadi. ^^  voy.  Amalgame. jJ-^îr  mai  voy.  Jambose. ^j^  mal.  voy.  Jambose. n")D3  voy.  Gémara. isjtîr  voy.  Amalgame. ^j2^  voy.  Djinn. y::5Acs^^  voy.  Gengéli. j^Jes^  voy.  Astronomie,  3o. *Kya^  voy.  Bételgeuse,  Astron.  18. ^15^  voy.  Chicane. Ju^j^  voy,  Dame-j canne. ^Lsj^  voy.  Alchimie,  l'i, □  •in~''3  voy.  Géhenne, voy.  Alchimie,  1  /i.
PHN.txt:3648:CHICANE, s. f. (p.)
PHN.txt:3652:s'applique au jeu de mail lui-même. — L'exercice de la chicane,
PHN.txt:3657:chicane, pour désigner un combat où l'on se dispute le terrain
PHN.txt:3665:Perse avajnt la fondation de Constantinople. — Chicane se dit
PHN.txt:3670:dâklit^ Il lança avec la chicane de l'éloquence la halle du discours
PHN.txt:3672:ici sur lorigine du mot chicane sont extraits d'une note fort
PHN.txt:3676:tale où chicane signifie, comme chez nous, dispute, objection
PHN.txt:10401:Chicane, s. f. (p.) iiA
```


## [2026-09-05T15:04:58.634Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB chibouque ==\"; grep -n -i \"chibouque\\|chibouk\" WEB_vol1.txt | head -5; echo \"== WEB chicane ==\"; grep -n -i \"chicanery\" WEB_vol1.txt | head -5; echo \"== FSD chibouk ==\"; grep -n -i \"chibouk\" FSD_vol1.txt | head -3; echo \"== FSD chicane ==\"; grep -n -i \"chicanery\" FSD_vol1.txt | head -3",
 "description": "Webster and Funk grep"
}
```


### [2026-09-05T15:04:58.737Z] TOOL RESULT

```
== WEB chibouque ==
== WEB chicane ==
32128:and unfair tricks and artifices; trickery; tepasi chicanery..
32130:chi-cine’, v.t.; chicaned, pt., pp.; chicaning, ber. [Fr. chicaner, to use trickery.] to use chicanery.
32132:2. to get by chicanery.
32133:chi-can/ér, n. one who employs chicanery.
== FSD chibouk ==
64630:2.  Chibouk  of  an Arab  Sheik.
== FSD chicane ==
63554:Syru  sec  artifice;  chicanery:  fraud;  hypocrite. cheat*,  n.  Coarse  wheat  bread,  cheat  bread*, cheat*,  n.  Bol.  The  European  chess  or  wild  oat  {Bromm secallnus).  cheats*.  See  chess*. cheat 'er,  1   dhlt'er;  2   chSt'er,  n.  1.  One  who  or  that  which cheats.  2*.  An  cscheator.—  tame  cheater,  an  animal  of  a domestic  or  tame  variety  employed  for  decoying  purposes. Cheat 'ham,  1   <fhlt'am;  2   chC-t'am.  n.  1.  Benjamin  F.
64704:Charges  of  political  chicanery  were  brought  against  him  [Van Buren].  .   .   .   But  he  invariably  extricated  himself  by  artifice  and choice  management.  Ben;  Perlev  Poore  Reminiscences  vol.  i, ch.  9,  p.  130.  [w.  a.  n.  18S6.1 [<  F.  chicanerie,  <   chicaner ;   see  chicane,  n.J Syiu  cheat,  chicane,  dodge,  mystification,  pettifogging, prevarication,  quibble,  shift,  sophlstn',  stratagem,  subter- fuge, subtlety,  trickery,  underhandedness. — Antj  candor, fairness,  frankness.
```


## [2026-09-05T15:05:08.754Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32115,32135p' WEB_vol1.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=sum(len(l)+1 for l in lines[:32120])\nprint('leaf0=',t[:i].count('\\f'))\n\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['WEB'];print(d['page_offset']);print(d.get('lookup_hint'))\"",
 "description": "Webster chicane entry and page"
}
```


### [2026-09-05T15:05:10.710Z] TOOL RESULT

```
straight, wooden stem, a clay bowl, and an
amber mouthpiece.
chic, a.; comp. chicquer; superl. chicquest; stylish and original; effective in style; ele- gant; clever and fashionable.
chic, n. [Fr., from M.H.G. schic, manner, or schicken, form, appearance, from schicken, to arrange, prepare.] elegance and originality in attire; cleverness of style: said especially of women or their clothes.
chi’ca, n. [Sp] an orange-red coloring matter obtained from the Bignonia chica, a climbing
eat South poena A 7
-ca:lo’te, n. ex.] a prickly. poppy o
Mexico and the southwestern United States,
Argemone platyceras. chi-cine’, n. [Fr., from Per. chaugdn, the game
of polo. The various senses are figurative of
the methods of the game.] A
1. the art of protracting a contest or discus-
sion by the use of evasive stratagems or mean
and unfair tricks and artifices; trickery; tepasi chicanery..
._in bridge, a hand without trumps. |
chi-cine’, v.t.; chicaned, pt., pp.; chicaning, ber. [Fr. chicaner, to use trickery.] to use chicanery.
‘cane, v.t. 1. to trick.
2. to get by chicanery.
chi-can/ér, n. one who employs chicanery.
chi-can/ér-y, n.; pl. chi-can/ér-ies, 1. trick- ery, especially legal trickery; sophistry; mean or unfair artifices used in contest or discus- sion; chicane.
2. a trick or quibble, `
=== leaf ===
leaf0= 341
not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
```


## [2026-09-05T15:05:15.818Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32095,32118p' WEB_vol1.txt",
 "description": "Webster chibouk entry"
}
```


### [2026-09-05T15:05:15.960Z] TOOL RESULT

```
chi-i-rd-scii/rd, chï-ä”rö-os-çü’rð, n. [It., lit- erally, clear dark; L. clarus, clear, and ob- scurus, dark.] k
1. a style of painting, drawing, etc. using only light and shade, in order to achieve the effect of a third dimension.
2. the effect achieved by such a style.
3. the way that an artist uses light and shade.
4. a painting, etc. in which chiaroscuro is used.
chi/asm, n. same as chiasma.
chi-as’ma, n.; pl. chi-ag’ma-ta, [Gr. chiasma, two lines crossed, from chiasein, to mark with the Greek letter chi.]
1, in anatomy, a crossing or intersection of the optic nerves on the ventral surface of the brain.
2. any crosswise fusion.
chi-as’mal, a. pertaining to the chiasma.
chi-as’ma-typ-y, 7. [from chiasma, type, and ~y.] in genetics, a supposed twisting of homol- ogous chromosomes about each other during one stage of meiosis, resulting in a possible interchange of genes, or factors, by the chromosomes.
chi-as’mus, 7.; pl. chi-as’mi, [Mod. L.; Gr. ¢hiasmos, placing crosswise.] an inversion of the second of two parallel phrases, clauses, etc.; as, do not live to eat, but eat to live.
chi-as/to-lite, n. (Gr. chiastos, marked with a chi (X), and lithos, stone.] a variety of anda- Tusite characterized by the diagonal arrange- ment of its crystals as seen when the stone is cut transversely: also called macle.
chiaus (chous), n. [Turk. chawush.] in Turkey, a messenger, emissary, sergeant, etc.
chib/bal, 7. cibol. [Obs.]
Chib’cha, n. 1. a member of a tribe of Chib- chan Indians who lived in eastern Colombia and had a highly developed civilization.
2. their language? A Chib’chăn, a. designating or of a linguistic
group of South and Central American Indians. chi-béuk’, chi böuque’ (-bök’), n. [Turk.
chibug, a pipe.) a tobacco pipe used by the
Turks, Persians, Arabs, etc., having a long,
straight, wooden stem, a clay bowl, and an
amber mouthpiece.
chic, a.; comp. chicquer; superl. chicquest; stylish and original; effective in style; ele- gant; clever and fashionable.
chic, n. [Fr., from M.H.G. schic, manner, or schicken, form, appearance, from schicken, to arrange, prepare.] elegance and originality in attire; cleverness of style: said especially of women or their clothes.
```


## [2026-09-05T15:05:23.419Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['KLN'];print(d['page_offset']);print(d.get('lookup_hint'))\"; echo ---; sed -n '7378,7386p' KLN_1966.txt | cut -c1-200",
 "description": "Klein page offset"
}
```


### [2026-09-05T15:05:25.495Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---
i
wan,  rel.  to  MLG.  keuwen,  Du.  kauwen,  OHG. kiuwan,  MHG.  kiuwen,  MG.  kiiwen,  ‘to  chew’ (whence  G.  kauen,  ‘to  chew’;  but  cp.  G.  wieder- kauen,  ‘to  chew  the  cud’,  fr
Derivatives:  chew,  n.,  chew-er,  n.,  chew-y,  adv. cheyney,  n.,  a  woolen  fabric.  —  Lit.  ‘china  ware’. The  word  represents  the  former  pronunciation of  China.
Chian,  adj.,  pertaining  to  the  island  Chios.  — Formed  with  suff.  -an  fr.  L.  Chius,  fr.  Gk.  XCog, name  of  an  island  off  the  coast  of  Asia  Minor. Chian,  also  chian,  n.  —
chiasma,  n.,  a  crossing  or  decussation  ( anat .)  — ModL.,  fr.  Gk.  xta.csy.01,  ‘two  things  placed  cross¬ wise’,  which  is  rel.  to  xfaopuk,  ‘a  placing  cross¬ wise’.  See
Derivatives:  chiasm-al,  chiasm-ic,  adjs. chiasmus,  inversion  of  word  order.  —  ModL.,  fr. Gk.  ylacs[JjQ,  ‘a  placing  crosswise’,  fr.
‘to  write  the  letter  x’,  fr-  XSL  XL  name  of  the 22nd  letter  in  the  Greek  alphabet.  Cp.  chiasma. chiastic,  adj.,  pertaining  to,  or  characterized  by chiasmus.  —  Formed  wi
chiastolite,  n.,  a  variety  of  andalusite  (mineral.) —  Compounded  of  Gk.  yla.a'coc,  (see  prec. word)  and  Xt&o;,  ‘stone’.  See  -life,  litho-. chiaus,  n.,  a  Turkish  messenger. 
chicane,  n.,  chicanery.  —  F.,  ‘quibble,  evasion’, fr.  chicaner.  See  chicane,  v. chicane,  intr.  v.,  to  trick.  —  F.  chicaner,  ‘to quibble,  wrangle,  quarrel’,  of  uncerta
```


## [2026-09-05T15:05:29.229Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('chibouk,  chibouque')\nprint('leaf0=',t[:i].count('\\f'), '-> printed ~', (t[:i].count('\\f')-12)*2)\n\"",
 "description": "Klein chibouk leaf"
}
```


### [2026-09-05T15:05:30.744Z] TOOL RESULT

```
leaf0= 155 -> printed ~ 286
```


## [2026-09-05T15:05:38.307Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (154,155,156):\n    L=[l for l in t[n].split('\\n') if l.strip()]\n    print('--- leaf',n,'---')\n    print(L[0][:120]); print(L[-1][:120])\nEOF",
 "description": "Klein leaf headers"
}
```


### [2026-09-05T15:05:40.487Z] TOOL RESULT

```
--- leaf 154 ---
 color’,  fr.  T.-E.  base  *ska(i)-, ‘to  shine,  flicker,  glimmer’.  See  skiagraphy, chazzan,  n.  —  See  hazzan. c
chemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. 
--- leaf 155 ---
See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  action
Derivatives:  chican-er,  n.,  chicanery  (q.v.) chicanery,  n.,  trickery,  quibbling,  s
--- leaf 156 ---
ophistry.  — - F.  chicanerie,  fr.  chicaner.  See  chicane,  v.  and -ery.
Chink,  n.,  a  Chinese  (slang).  —  Fr.  Chi
```


## [2026-09-05T15:05:55.658Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT cub ==\"; grep -n -i \"\\bčub\\|cub-\\|dāru-\\|wood\" KNT.txt | head -10; echo \"== BRT ==\"; grep -n -i \"Holz'\" BRT.txt | head -5; echo \"== TTS files ==\"; ls incoming/TTS/ 2>/dev/null; echo \"== TTS grep ==\"; grep -n -i \"cybyk\\|tschybyk\\|cop \" incoming/TTS/TTS_pages.txt 2>/dev/null | head -10",
 "description": "Kent, Bartholomae, Vambery"
}
```


### [2026-09-05T15:05:55.721Z] TOOL RESULT

```
== KNT cub ==
ugrep: error: error at position 12
(?mi)\(?:b|B)(?:č|Č)ub|cub-|(?:d|D)(?:ā|Ā)ru-|wood
            \___mismatched ( )


== BRT ==
2726:i.  aesma-   m.    'Brennholz',   Flur,    und
2743:•  j.  aesmö.barvtay-  f.  'Darbringuog  von  isa^ta  Yt.  i^.  53;  — yff  naeeim  isaiti  huna- Brennholz':  alvayacif  °niii  (IS.)'*  aiva-  ranqm'V.ij.i9;Aog.48;  —  äiä ..Ayämii , . yacit  bar7sm3.stir?iH  Y.24~  aiavanö  tnsyä  istsm^^  rJiVl'(sd,)  Y.  40. 4;
== TTS files ==
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
== TTS grep ==
```


## [2026-09-05T15:05:57.388Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHN chicane ==\"; sed -n '3640,3690p' PHN.txt; echo \"== FSD chibouk entry ==\"; grep -n -B1 -A3 \"Chib'ouk\\|chibouk,\" FSD_vol1.txt | head -20",
 "description": "Pihan chicane, Funk chibouk"
}
```


### [2026-09-05T15:05:57.470Z] TOOL RESULT

```
== PHN chicane ==
expriment pas mieux la valeur.
CHIBOUQUE, s. f. (t.)
(jiyJi>^ [tchiboûq]^ qui signifie' proprement baguette, se dit aussi
de la pipe turque à long tuyau , en bois de cerisier ou en jasmin .
et au bout duquel est placé le foyer. L'usage de la chibottque est
' lu
très-commun en Orient et dans TAfrique septentrionale. Quant
à la pipe persane , elle s'appelle narguileh. Voyez ce mot.
CHICANE, s. f. (p.)
^j^y>^ [tchevkiân]^ chez les Persans, désigne la raquette pour
jouer à la paume , ou la petite masse en bois qui sert à chasser
avec force une balle appelée isy^ [s^%]'' P^'' ^^^tension il
s'applique au jeu de mail lui-même. — L'exercice de la chicane,
inventé par les anciens habitants de la Perse , avait lieu à cheval ,
dans le but de figurer des évolutions militaires, et Tardeur
qu'on y déployait exposait souvent à de graves dangers. C'est
de là probablement que nous avons tiré l'expression guerre de
chicane, pour désigner un combat où l'on se dispute le terrain
pied à pied, par des marches et contre-marches. Autrefois le
jeu de la paume à cheval était aussi en grande faveur chez les
Arabes. Suivant l'historien Mas'oudy, le premier khalife qui s'y
livra publiquement dans un manège fut Haroun arrachid. Dans
la suite, on s'y exerça simplement à pied. — La connais-CHI 115
sauce de ce jeu en France ne paraît pas remonter au delà de
Tëpoque des Croisades, tandis qu'il était en usage dans la
Perse avajnt la fondation de Constantinople. — Chicane se dit
quelquefois en persan, au figuré, dans le sens de force, énergie.
En void un exemple, où le mot isy^ [s^v] ^^^^^ ^^ trouve
également employé : iJUu ^^I«>h^ j^ ^^W u^yf? p^ iSy^
01.^1 «Xj| [goûy kélâm betchevkiân béiân der méîdân mouqâlet en--
dâklit^ Il lança avec la chicane de l'éloquence la halle du discours
dans le manège de Félocution, — Les renseignements qu'on lit
ici sur lorigine du mot chicane sont extraits d'une note fort
intéressante , publiée par M. Quatremère dans sa traduction
de Y Histoire des Sultans mamlouks de l'Egypte, tome 1'', 1 " partie ,
pages isiàiSa. — Je n'ai pas rencontré de phrase orien-
tale où chicane signifie, comme chez nous, dispute, objection
vétilleuse, en matière de jeu ou de procès; mais, comme le jeu
fait souvent naître des querelles, on aura pu donner le nom
du jeu lui-même aux contestations qui en résultent ordinaire-
ment. — Le terme persan {j^^^^ [tchevkiân] s'applique encore,
en Turquie, au bâton recourbé dont se servent les cavaliers
pour ramasser les javelots de leurs adversaires, dans l'exercice
du DJÉRiD. Voyez ce dernier mot.
CHICOTIN, s. m. (a.)
fj^jWim [soqol!oriyy].socotrin, de Socotora. Nom donné au suc de
l'aloès, dont la meilleure espèce provient de Socotora, fle
située à l'entrée du détroit appelé Bâb elmandeb. — Les nour-
rices se frottent quelquefois avec ce suc le bout des ma-
8.116 CHl
melles, pour en éloigner les enfants qu'elles veulent sevrer. —
== FSD chibouk entry ==
```


## [2026-09-05T15:06:05.602Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Tzykanisterion",
 "prompt": "Quote verbatim the etymology of tzykanion/tzykanisterion: the Middle Persian source word, when the game reached Byzantium, and any statement about French chicane."
}
```


## [2026-09-05T15:06:06.661Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%BE%D9%82",
 "prompt": "Give the Persian etymology of چپق (čapoq/čopoq) verbatim: is it borrowed from Ottoman Turkish çubuk? Any cited sources?"
}
```


### [2026-09-05T15:06:09.862Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T15:06:10.760Z] TOOL RESULT

```
# Etymology of Tzykanisterion

## Middle Persian Source
The Middle Persian origin is provided as: "čaukān, čōkān"

According to the article, the Greek term tzykanion derives from "Middle Persian _čaukān_, _čōkān_" and represents a type of polo game adopted by Byzantines from Sassanid Persia.

## Important Limitation
The Wikipedia article contains **no information about French "chicane"** or any connection between this Byzantine sport and French terminology. The content focuses exclusively on the Persian-to-Greek linguistic transmission.

The article also does not specify precisely when the game reached Byzantium, only noting it was adopted from Sassanid Persia.
```


## [2026-09-05T15:06:16.381Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%86%D9%88%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D9%88%DA%AF%D8%A7%D9%86\" \\\n \"https://www.etymonline.com/word/chicanery\" \\\n \"https://en.wiktionary.org/wiki/%C3%A7ubuk\" \\\n \"https://en.wiktionary.org/wiki/chicane\" \\\n \"https://en.wikipedia.org/wiki/Tzykanisterion\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 107, root Čop/Čop-gân: čūb/čowgān, Turkish çubuk, chibouk, chicane chain\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T15:06:20.065Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/694fa33cffeb72c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c94d15eb4f2ce22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88f043cf71a313a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ae8a82c36135ac9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19cbf578ecf9d6c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2eaf8db3d8ce5cc6.txt
```


## [2026-09-05T15:06:25.039Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^چوب\\|چوب:\" MON_part1.txt | head -5; echo \"== ctx 51655-51672 ==\"; sed -n '51650,51672p' MON_part1.txt",
 "description": "Mo'in chub/chowgan"
}
```


### [2026-09-05T15:06:25.106Z] TOOL RESULT

```
3039:چوبین که سنگ آسیا را از درون سو به 
3992:چوبی کرده به وسبلة آن کشتی دشمن را 
9984:چوب مخصوص بوده و آن در داخل چهار 
9985:چوب حرکت می‌کرد و با پایین و بالا رفتن» 
10046:چوب خوارک» چوب‌خواره» دیوچه 
== ctx 51655-51672 ==
و باریک» مانند چوق‌الف. 

جوک: (قد. -0016)066 (مرغ حق] (.) 
(جاذ.) مرغی است مانند جغد که خود را از 
درخت آویزان سازد و فریاد کسند» 


شب آویز» مرغ حق. 

جوک: :50 (.) آلت تناسل مرد؛ نره. 
چوگان: (66:10) 2۳257 (امر.) چوبی که 
دستة آن راست و باریک و سرش کمی 
خمیده است و بدان در بازی مخصوصی 
(چوگان‌بازی) گوی زنند. هر چوب سر کج 
عموما. چوب سر کجی که دهل و نقاره را 
بدان نوازند. چوبی بلند و سرکج که فولادی 
از آن آویخته باشند و آن از لوازم پادشاهی 
انیت کنو کته و کان تم ( کد رت 
معشوق. 

چوگانی : (-.00080-1)060 (ص‌نست.) استی 
ورزیده که مناسب چوگان‌بازی باشد. 
جول: الا [- چوله] (ص.) خمیده؛» منحنی.
```


## [2026-09-05T15:06:33.570Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT ==\"; grep -c . KNT.txt; grep -n -i \"cub\" KNT.txt | head -5; echo \"-- KNT 'wood' --\"; grep -n \"wood\" KNT.txt | head -5; echo \"== BRT čub? ==\"; grep -n \"kSupa\\|ksupa\" BRT.txt HUB.txt | head -5",
 "description": "Kent Old Persian check"
}
```


### [2026-09-05T15:06:33.654Z] TOOL RESULT

```
== KNT ==
5869
1118:thus the pAr. *aratn- aratan- gave Av. dual arana, but OP arašn- and (with extension of the $) arasan- ‘cubit’, in inst. pl. arašaniš (see
2761:was packed down, some 40 cubits in depth, another (part) 20 cubits in depth’. Appositive substantives do not necessarily agree in gender; thus DPd 6f уат dahydus Pürsa ‘this province Persia’, where dahydus is feminine and Påãrsa is masculine.
4292:$3e. 22-7. This palace which I built at Susa, from afar its ornamentation was brought. Down- ward the earth was dug, until I reached rock in the earth. When the excavation had been made, then rubble was packed down, some 40 cubits in depth, another (part) 20 cubits in depth. On that rubble the palace was constructed.
5049:araían- sb. ‘cubit’ (832, §82, S155.ID): Av. nom. dual araénd, to Iran. stem aratan- атап, ef. Skt. aratnt-; Lg. 15.176-7 (borrowed from Iran. into General Slavic as aršin ‘ell’, Wb. AfOF 7.41, against Berneker, Slav. etym. Wrtb. 31, who thinks it borrowed from Turkish); cf. also Bv. Orig. 105. arasanit ipm. (§187) DSf 26 bis (not nom. sg., with Ву. Gr. $308, $318: not асс. pl.).
-- KNT 'wood' --
66:of press of work, delegated the task of proofread- grateful to any reader who sends me a list of ing in his stead. Her repeated skillful readings such misprints and errors as he may discover. caught numerous misprints that had escaped R.G. К. me; yet with all our care I dare not think that Wynnewood, Pa.,
357:86. DIALECT MIXTURE IN THE OLD PERSIAN Inscriptions. Like most or perhaps all other series of documents, the OP inscriptions are not in pure OP dialect, free from admixture from outside.’ They contain the expected borrowings of names of persons and places, and presumably of some cultural materials. Thus Aurà ‘Assyria’, Babiruí ‘Babylon’, Mudrdya ‘Egypt’ are from Semitic; Гаа (a district in Assyria), Dubdla (a district in Babylonia), Labandna ‘Mt. Lebanon’, Haldita- (name of an Armenian) betray their non- Iranian character by the l; a few words lack a convincing IE etymology; such as si"kabrus ‘car- nelian’, багт ‘timber’, yakd (a kind of wood), skauhiS ‘weak, lowly’, or are obvious borrowings, such as maškā- ‘inflated skin’ from Aramaic. But the main outside influence is that of the Median dialect, seen in phonetic and lexical differences, perhaps also in variant grammatical forms. Aramaic also seems to have had a certain influence on the phrasing and the syntax. There is no evidence that OP itself, at the time of the inscriptions, possessed a literature of any kind apart from these inscriptions themselves.
3051:1 In the phrase asd ddruv (DSf 41; see Lex. s.v. dáru-) it is uncertain which word. is-appositive;to the other; is it ‘stone that is wood’, or ^wood that 1s stone’?
4301:§3k. 49-55. The goldsmiths who wrought the gold, those were Medes and Egyptians. The men Who wrought the wood, those were Sardians and Egyptians. The men who wrought the baked brick, those were Babylonians. The men who adorned the wall, those were Medes and Egyptians.
5156:ета or lismar\uy asn., of uncertain mean- ing, possibly ‘(gold) inlay’ (Cameron, Persepolis Treasury Tablets 129-30), DSf 51; supplied by Hz. AMI 3.74-5, as a borrowing from Elam. 25- ma-lu (@%ma-lu ‘wood’ Hinz, Orientalia 1950, shortly to appear), or from the lost Akk. original of both; сЁ JAOS 53.21, 56.220. But read rather Idàr|uv with Hinz, see Lex. s.v.
== BRT čub? ==
```


## [2026-09-05T15:06:42.243Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-05T15:06:42.287Z] TOOL RESULT

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


## [2026-09-05T15:07:54.074Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(f,pat,off=None):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.find(pat)\n    if i<0: return None\n    l=t[:i].count('\\f')\n    return l, (l-off if off is not None else None)\nprint('LKT 447 cybuk', leafof('LKT.txt',\"447.  Tk  cykryk\"),'| entry447 leaf', leafof('LKT.txt',\"'Pfeife'  [vom  pers.\",26))\nprint('DEV chicane', leafof('DEV.txt','Chicane.  Ce  mot'))\nprint('PHN chicane', leafof('PHN.txt','CHICANE, s. f. (p.)'))\nprint('SKT chicanery', leafof('SKT.txt','Chicanery',20))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['DEV','PHN']: print(k, d[k].get('page_offset'))\"",
 "description": "Compute pages for LKT/DEV/PHN/SKT"
}
```


### [2026-09-05T15:07:55.925Z] TOOL RESULT

```
LKT 447 cybuk None | entry447 leaf (62, 36)
DEV chicane (125, None)
PHN chicane (145, None)
SKT chicanery (99, 79)
DEV leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHN leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-05T17:21:46.287Z] AGENT

Now I'll write the verification file.


## [2026-09-05T17:25:43.622Z] TOOL CALL #52: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-107.json",
 "content": "{\n  \"pdf_page\": 107,\n  \"book_page\": 77,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Čop, Čop-gân\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Middle Persian čōb 'wood, stick' (Pahl. cwp), with its derivative čōbagān / čōbgān (Pahl. cwpk'n', cwpygʾn'; MacKenzie reads čaw(la)gān) 'curved polo-stick, the game of polo' — not an Old Persian word\",\n      \"note\": \"The etymon itself is real and the gloss is right: MacKenzie, A Concise Pahlavi Dictionary p.24 'čōb [cwp | N ~] wood, stick', and p.23 'čaw(la)gān [cwpkʾn' | Ar. sawlajān, N čawgān] (curved) polo-stick; polo'; Nyberg, Manual of Pahlavi II p.59 'čōwčgān [cwpygʾn'] the stick used in playing polo … NP čaugān; Arab. lw. saulajān'. What is wrong is the language label: there is no Old Persian *čub-. Kent's Old Persian lexicon has no such stem (OP for 'wood' is dāru-, DSf 41), and Horn no.448 himself labels the older form 'phlv. čōp', i.e. Pahlavi/Middle Persian. So the root box should read 'Middle Persian' (or simply 'Persian'), not 'Old Persian'. The old attempt to attach čōb to Sanskrit kṣupa- 'bush' is rejected by Horn ('Lässt sich lautlich nicht mit skr. kṣupa- … vermitteln') and Wiktionary likewise says 'further connections outside Indo-Iranian uncertain'. Two further page-level observations: (a) HRN:99 covers čōb (no.448) but čōgān is no.449 on p.100; (b) the Greek box on the printed page really is empty — the extraction is faithful (see node #6).\",\n      \"note_fa\": \"ریشهٔ این مدخل واقعی است اما برچسب زبانی آن نادرست است. کهن‌ترین صورت گواهی‌شده فارسی میانه (پهلوی) čōb «چوب، چوبدست» است (مکنزی، فرهنگ کوچک پهلوی، ص ۲۴: cwp) و مشتق آن čōbagān/čōbgān «چوگان» (مکنزی ص ۲۳؛ نیبرگ ج۲ ص ۵۹: cwpygʾn'). در پارسی باستان چنین ستاکی گواهی نشده است؛ کنت در واژه‌نامهٔ پارسی باستان تنها dāru- «چوب» را دارد. هرن نیز (شمارهٔ ۴۴۸، ص ۹۹) صورت کهن‌تر را «پهلوی čōp» می‌نامد، نه پارسی باستان. پیوند دادن čōb به سنسکریت kṣupa- «بوته» را هرن به دلیل ناسازگاری آوایی رد می‌کند و ویکی‌واژه نیز آن را نامطمئن می‌داند. بنابراین ادعای معنایی نورایی درست است ولی «پارسی باستان» باید به «فارسی میانه» اصلاح شود.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%86%D9%88%D8%A8\",\n        \"https://en.wiktionary.org/wiki/%DA%86%D9%88%DA%AF%D8%A7%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:99\", \"status\": \"partial\", \"note\": \"Horn, Grundriss p.99 no.448 (HRN.txt leaf 120): '448. čōb \\\"Holz\\\". phlv. čōp \\\"Holz\\\" (Guj. Ab.); kurd. čō, siw; bal. LW. čōp; wa. čōpk, sar. čūb.' — it supports the word and gloss but labels the ancestor Pahlavi, not Old Persian; and čōgān is no.449 on p.100, not p.99.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"PHD\", \"where\": \"p.24 s.v. čōb (PHD.txt leaf 45)\", \"stance\": \"supports\", \"note\": \"'čōb [cwp | N ~] wood, stick.' — the Middle Persian etymon exactly as Nourai's root, but Middle not Old Persian.\"},\n        {\"src\": \"NYB\", \"where\": \"Part II Glossary p.59 (NYB_vol2_glossary.txt leaf 67)\", \"stance\": \"supports\", \"note\": \"'čōwčgān [cwpygʾn'] the stick used in playing polo …; the game of polo itself. — NP čaugān; Arab. lw. saulajān-; Fraenkel, Aram. Fremdw. 291; Horn, NP Et. no. 4[4]9 and Hübschmann' — the Pahlavi spelling cwpygʾn' shows the word is built on cwp = čōb.\"},\n        {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon and §86 (KNT.txt)\", \"stance\": \"contradicts\", \"note\": \"No stem čub-/čōb- in Kent's OP lexicon; the OP word for wood is dāru- ('asā dāruv', DSf 41). Nothing supports an Old Persian label.\"},\n        {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt), grep čōb / čōgān / čaugān\", \"stance\": \"silent\", \"note\": \"no hit in the OCR of Hübschmann's Persische Studien (Mo'in's footnote cites 'هوبشمان ۴۴' for čōgān, but that page is not retrievable in this scan).\"},\n        {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt, grep چوب / چوگان\", \"stance\": \"silent\", \"note\": \"no headword چوب or چوگان; the word occurs only inside other entries (e.g. 'چوبدستی').\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"čŭb «چوب»; čowgân «چوگان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"چوب čūb continues Middle Persian čōb (Pahlavi spelling cwp, MacKenzie p.24) with the regular New Persian raising of Middle Persian ō to ū (cf. rōz > rūz, sōz > sūz); Horn no.448 gives the same chain with the dialect cognates kurd. čō, bal. čōp, sar. čūb. چوگان čowgān is a derivative of the same čōb: Middle Persian čōbagān / čōbgān (Pahl. cwpkʾn', cwpygʾn'), i.e. čōb 'stick' + the denominal suffix -agān, whence loss of the intervocalic -b- gives čōgān > NP čowgān. Borhan-e Qate' still carries the older headword چوبگان beside چوگان, which is direct evidence for the derivation from چوب. From the Sasanian court game the word passed into Arabic as صولجان ṣawlajān (MacKenzie p.23 'Ar. sawlajān'; Mo'in s.v. صولجان '[معرّب چوگان]') and into Byzantine Greek as τζυκάνιον (see node #6). So both words of the node, and the arrow čōb → čowgān, are correct.\",\n          \"derivation_fa\": \"«چوب» دنبالهٔ فارسی میانهٔ čōb (املای پهلوی cwp) است؛ واکهٔ ō فارسی میانه در فارسی نو به ū بدل شده (همان دگرگونی که در rōz > روز و sōz > سوز دیده می‌شود). هرن (شمارهٔ ۴۴۸) همین سلسله را با هم‌ریشه‌های گویشی کردی čō، بلوچی čōp و سریکلی čūb می‌آورد. «چوگان» نیز مشتقِ همین ستاک است: فارسی میانه čōbagān/čōbgān (پهلوی cwpkʾn' و cwpygʾn') یعنی čōb + پسوند -agān؛ با افتادن بِ میان‌واکه‌ای čōgān و سپس «چوگان» به دست آمده است. برهان قاطع هنوز سرواژهٔ کهن‌تر «چوبگان» را در کنار «چوگان» دارد و این خود گواه اشتقاق آن از «چوب» است. همین واژه به عربی «صولجان» (معرّب چوگان، به گواهی معین) و به یونانی بیزانسی τζυκάνιον راه یافته است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%88%D8%A8\",\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%88%DA%AF%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:99\", \"status\": \"partial\", \"note\": \"Horn p.99 no.448 'čōb \\\"Holz\\\". phlv. čōp \\\"Holz\\\"' supports čūb exactly; but čōgān is Horn no.449 on p.100 ('čōgān \\\"Schläger (im Ballspiel)\\\"', with the note that the NP variant čōlgān 'in čōbgān zu emendiren ist' — i.e. Horn himself reads the word as čōb-gān), so the citation should be HRN:99-100.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.24 and p.23\", \"stance\": \"supports\", \"note\": \"'čōb [cwp | N ~] wood, stick' and 'čaw(la)gān [cwpkʾn' | Ar. sawlajān, N čawgān] (curved) polo-stick; polo'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg II p.59\", \"stance\": \"supports\", \"note\": \"'čōwčgān [cwpygʾn'] the stick used in playing polo … NP čaugān; Arab. lw. saulajān' — the Pahlavi spelling with cwp- is the decisive evidence for čōb + -agān.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, vol. 2, leaf 129 of BQT_v2_pages.txt (printed ≈ p.672); running head چوبگان\", \"stance\": \"supports\", \"note\": \"the dictionary's headword is چوبگان (with the variant چوگان below it) and Mo'in's footnote there reads '«هوبشمان ۴۴» معرب آن صولجان و کلمهٔ فرانسوی chicane از فارسی مأخوذ است' — Mo'in derives Arabic صولجان and French chicane from the Persian word.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. چوگان (MON_part1.txt line 51660) and s.v. صولجان (line 90586)\", \"stance\": \"supports\", \"note\": \"'چوگان … چوبی که دستهٔ آن راست و باریک و سرش کمی خمیده است و بدان در بازی مخصوصی (چوگان‌بازی) گوی زنند' — defined as a kind of چوب; and 'صولجان: [معرّب چوگان]'.\"},\n            {\"src\": \"HRN\", \"where\": \"p.99 no.448, p.100 no.449\", \"stance\": \"supports\", \"note\": \"see ref_check; Horn emends the variant čōlgān to čōbgān, i.e. he too analyses the word as containing čōb.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Turkish\",\n          \"words\": \"čŭb; čubŭq, chîbuq\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai follows Lokotsch, who in no.447 (p.36) writes 'Tk. cybuk \\\"Pfeife\\\" [vom pers. čūb \\\"Stock\\\", s. hier Nr.432]', Nr.432 being 'Pers. čōb \\\"Holz\\\" [Horn NpEt S.99, Nr.448]' on the cited p.35. Modern Turkology rejects this: Turkish çubuk 'rod, twig, pipe-stem' goes back to Old Turkic/Ottoman چبوق çıbuk ~ çubuk, from Proto-Turkic *čöpik, a diminutive of *čöp 'twig, chaff, bit of stick' (Turkish çöp) — a native Turkic word with a good internal Turkic family, and no Iranian intermediary is needed. Lokotsch himself, in the very same entry no.432, quotes 'N. cob \\\"Stück Holz, Stock, Schmutz\\\"' — that is Turkish çöp, the native word, which he mistook for a reflex of Persian čōb. Nor is a Turkish lemma 'čŭb' real: Turkish has çöp, not *çub. The chart's own NOTE ('Derivation of the Turkish word from Persian is not clear') already flags the doubt, and modern scholarship comes down on the native-Turkic side; the Persian and Turkic words are look-alikes, not the same word.\",\n          \"derivation_fa\": \"نورایی در اینجا از لوکوچ پیروی می‌کند که در شمارهٔ ۴۴۷ (ص ۳۶) می‌نویسد ترکی çubuk «پیپ» از فارسی čūb «چوب» گرفته شده است. اما ترک‌شناسی امروزی این را نمی‌پذیرد: ترکی çubuk «ترکه، شاخهٔ نازک، نی چپق» از ترکی باستان/عثمانی çıbuk ~ çubuk و آن از ترکی آغازین *čöpik، مصغّرِ *čöp «ترکه، خاشاک» (ترکی امروز çöp) است؛ یعنی واژه‌ای بومی ترکی با خانوادهٔ درون‌ترکی روشن، و نیازی به وام‌گیری از ایرانی نیست. جالب آنکه خودِ لوکوچ در همان مدخل صورت «cob به معنی تکه چوب، چوبدست، خاشاک» را می‌آورد که همان çöp ترکی است و آن را به خطا بازتاب čōb فارسی پنداشته است. افزون بر این، سرواژهٔ «čŭb» به عنوان واژهٔ ترکی وجود ندارد. یادداشت خودِ کتاب نیز به این تردید اشاره کرده است؛ پژوهش امروزی ریشهٔ ترکی بومی را ترجیح می‌دهد و این دو واژه را تنها شبیه هم می‌داند، نه یکی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%C3%A7ubuk\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"LKT:35\", \"status\": \"partial\", \"note\": \"Lokotsch p.35 (LKT.txt leaf 61) has no.432 'Pers. čōb: \\\"Holz\\\" [Horn NpEt S. 99, Nr. 448], ebenso N. cob \\\"Stück Holz, Stock, Schmutz\\\"; hieraus rum. ciob' — the cited page carries the Persian word but not the Turkish derivation. The claim Nourai draws the arrow from is one page later, p.36 no.447: 'Tk. cybuk: \\\"Pfeife\\\" [vom pers. čūb \\\"Stock\\\", s. hier Nr. 432]; hieraus rum. ciubuc …, bulg. serb. cibuk, russ. čubuk, poln. cybuch'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"p.35 no.432 and p.36 no.447 (leaves 61-62)\", \"stance\": \"partial\", \"note\": \"Lokotsch does make Nourai's claim, but from p.36; and his own 'N. cob' form is Turkish çöp, the native word.\"},\n            {\"src\": \"TTS\", \"where\": \"Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, incoming/TTS/TTS_pages.txt, grep cubuk / cybyk / tschybyk / 'cop '\", \"stance\": \"silent\", \"note\": \"no hit in the OCR; Vámbéry's stem list (cited by Lokotsch elsewhere, e.g. sil/sir/siz for çizme) is not retrievable for this word in our scan.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.114 s.v. CHIBOUQUE\", \"stance\": \"contradicts\", \"note\": \"Pihan tags the word '(t.)' = Turkish, not '(p.)' Persian: 'چبوق [tchiboûq], qui signifie proprement baguette, se dit aussi de la pipe turque à long tuyau' — i.e. he treats it as a Turkish word from the start (he reserves '(p.)' for chicane).\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. chibouk (KLN_1966.txt leaf 155)\", \"stance\": \"partial\", \"note\": \"'fr. Turk. chubuq, chibuq, \\\"pipe\\\", prop. meaning \\\"stick, staff, tube\\\", and rel. to chub, \\\"stick, staff\\\"' — Klein keeps the word inside Turkish and does not name Persian.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"čopoq «چپق»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian چپق čopoq/čapoq 'long-stemmed tobacco pipe' is a loan back from Ottoman Turkish چبوق çubuk, taken over in the tobacco era (Ottoman-Safavid contact, 17th c.); Turkish u of the first syllable is rendered by Persian o and the final -q is kept, giving čopoq. Mo'in's footnote in Borhan-e Qate' says exactly this: '# چپق — [ضمّ اول و دوم] از ترکی «چوبوق»، در جغتایی بمعنی لولهٔ چپق، قطعهٔ چوب قابل انعطاف، شاخ کوچک'. So the arrow Turkish → Persian is right. Note, however, that this makes the word a Turkic word inside Persian, not (as the chart implies) a Persian word making a round trip through Turkish: the Turkish source is itself native Turkic (node #2).\",\n          \"derivation_fa\": \"«چپق» وام‌واژه‌ای است از ترکی عثمانی چبوق (çubuk) که در دورهٔ رواج توتون (سدهٔ یازدهم هجری / هفدهم میلادی، در پی داد و ستد صفوی-عثمانی) وارد فارسی شده است؛ ضمّهٔ هجای نخست ترکی در فارسی به «ـُ» بدل شده و قاف پایانی برجای مانده است. معین در حاشیهٔ برهان قاطع همین را می‌گوید: «چپق — [به ضمّ اول و دوم] از ترکی «چوبوق»، در جغتایی به معنی لولهٔ چپق، قطعهٔ چوب قابل انعطاف، شاخ کوچک». پس جهت وام‌گیری در نمودار (ترکی ← فارسی) درست است؛ تنها نکته آنکه چون خودِ واژهٔ ترکی بومی است (بنگرید به گرهٔ ۲)، این «چپق» وام‌واژهٔ ترکی در فارسی است، نه بازگشتِ واژه‌ای فارسی از راه ترکی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%C3%A7ubuk\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ARK:211\", \"status\": \"not_checked\", \"note\": \"ARK = Rokn-zadeh Adamiyyat, Arkan-e Sokhan (Sharq 1347/1968). refs_online.json records it as not digitised on any accessible platform ('nothing digitised on any permitted platform … check opac.nlai.ir manually'), so p.211 could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, vol. 2, leaf 79 of BQT_v2_pages.txt (printed ≈ p.622), s.v. چپق\", \"stance\": \"supports\", \"note\": \"'# چپق ‑ [ضم اول و دوم] از ترکی «چوبوق»، در جغتایی بمعنی لولهٔ چپق، قطعهٔ چوب قابل انعطاف، شاخ کوچک [جغتایی ۱۹۲]', continuing '… [کلمهٔ] فرانسه از همین کلمهٔ ترکی مأخوذ است' — both the Persian and the French word are taken from Turkish.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, چپق (MON_part1.txt lines 34020, 49786, 76631)\", \"stance\": \"partial\", \"note\": \"the entry describes the object ('دسته‌ای چوبی و سرسفالی؛ توتون چپق را …') and glosses پیپ as 'چپق کوچک دستهٔ کوتاه'; it confirms the word and meaning but the origin tag is not legible in this OCR.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.114 CHIBOUQUE (t.)\", \"stance\": \"supports\", \"note\": \"confirms that the pipe-word is Turkish چبوق in all its onward forms.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"chibouque\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French chibouque 'long Turkish pipe' entered French in the early 19th century with the Romantic travel literature of the Levant (Lamartine, Gautier, Nerval), directly from Ottoman Turkish چبوق çubuk 'pipe, rod'; French spells the Turkish ç as ch- and the final -uk as -ouque. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, p.114, heads the entry 'CHIBOUQUE, s. f. (t.)' — the tag (t.) meaning Turkish — and explains 'چبوق [tchiboûq], qui signifie proprement baguette, se dit aussi de la pipe turque à long tuyau, en bois de cerisier ou en jasmin'. Mo'in's footnote in Borhan-e Qate' s.v. چپق likewise says the French word comes from the same Turkish word. So the arrow Turkish → French is correct; the transfer was direct, with no Persian stage.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی chibouque «چپق درازِ ترکی» در آغاز سدهٔ نوزدهم میلادی همراه با ادبیات سفرنامه‌ای شرق‌گرای فرانسه (لامارتین، گوتیه، نروال) و مستقیماً از ترکی عثمانی چبوق (çubuk) وارد فرانسه شده است؛ چِ ترکی با ch و قافِ پایانی با ‑ouque بازنمایی شده است. پیهان در فرهنگ ریشه‌شناسی واژه‌های فرانسوی برگرفته از عربی و فارسی و ترکی (ص ۱۱۴) این مدخل را با نشانهٔ (t.) یعنی «ترکی» می‌آورد و می‌نویسد چبوق در اصل به معنی «ترکه» است و سپس بر پیپِ درازلولهٔ ترکی نیز اطلاق شده. معین نیز در حاشیهٔ «چپق» می‌گوید واژهٔ فرانسه از همین واژهٔ ترکی گرفته شده است. پس پیکانِ ترکی ← فرانسوی درست است و واسطهٔ فارسی در کار نبوده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%C3%A7ubuk\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"WEB:312\", \"status\": \"supports\", \"note\": \"Webster's New Twentieth Century Dictionary, 2nd ed., s.v. (WEB_vol1.txt leaf 341, the 'chi-' page = p.312): 'chi-bouk', chi-bouque' (-bōk'), n. [Turk. chibuq, a pipe.] a tobacco pipe used by the Turks, Persians, Arabs, etc., having a long, straight, wooden stem, a clay bowl, and an amber mouthpiece.' — Webster gives chibouque as a variant spelling with a Turkish etymology; it supports 'from Turkish' but does not itself label the form French.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"Pihan p.114 s.v. CHIBOUQUE (PHN.txt leaf 145)\", \"stance\": \"supports\", \"note\": \"'CHIBOUQUE, s. f. (t.) چبوق [tchiboûq], qui signifie proprement baguette, se dit aussi de la pipe turque à long tuyau …' — a French dictionary entry marking the word Turkish.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. chibouk (KLN_1966.txt leaf 155)\", \"stance\": \"supports\", \"note\": \"'chibouk, chibouque, n., a Turkish tobacco pipe. — F. chibouque, fr. Turk. chubuq, chibuq, \\\"pipe\\\"' — explicitly makes French chibouque the intermediary.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, vol. 2 leaf 79, footnote to چپق\", \"stance\": \"supports\", \"note\": \"'[کلمهٔ] فرانسه از همین کلمهٔ ترکی مأخوذ است' — the French word is taken from the same Turkish word.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale (DEV.txt), grep chibouque\", \"stance\": \"silent\", \"note\": \"no entry for chibouque in Devic's list.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"chibouk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English chibouk (also chibouque, chiboque) 'long Turkish tobacco pipe' is first recorded in 1813 in Byron's The Giaour and belongs to the same Romantic-orientalist wave as the French word; it is borrowed from French chibouque, the -ouk spelling being an anglicisation of French -ouque. Klein s.v.: 'chibouk, chibouque, n., a Turkish tobacco pipe. — F. chibouque, fr. Turk. chubuq, chibuq, \\\"pipe\\\", prop. meaning \\\"stick, staff, tube\\\"'. Webster takes it straight from Turkish without the French stage, which is a difference of route rather than of origin. Either way the arrow French → English as drawn is the standard account.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی chibouk «چپقِ درازِ ترکی» نخستین بار در ۱۸۱۳ میلادی در منظومهٔ The Giaour اثر بایرون دیده می‌شود و از همان موج شرق‌گرایی رمانتیک برخاسته است؛ خاستگاه بی‌واسطهٔ آن فرانسوی chibouque است و املای ‑ouk انگلیسی‌شدهٔ ‑ouque فرانسوی است. کلاین می‌نویسد: «chibouk, chibouque — از فرانسوی chibouque، از ترکی chubuq/chibuq «پیپ»، که در اصل به معنی چوب، عصا، لوله است». وبستر آن را بی‌واسطه از ترکی می‌گیرد که تفاوت در مسیر است نه در خاستگاه. بنابراین پیکانِ فرانسوی ← انگلیسی همان روایت پذیرفته‌شده است و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%C3%A7ubuk\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:275\", \"status\": \"supports\", \"note\": \"Klein, Comprehensive Etymological Dictionary (KLN_1966.txt leaf 155, in the 'chemo-…chicanery' block; the scan's rough offset formula puts the leaf at printed ≈ 286, so Nourai's p.275 is a few pages out or from another printing, but the entry is unmistakable): 'chibouk, chibouque, n., a Turkish tobacco pipe. — F. chibouque, fr. Turk. chubuq, chibuq, \\\"pipe\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WEB\", \"where\": \"Webster 2nd ed. p.312 (WEB_vol1.txt leaf 341)\", \"stance\": \"partial\", \"note\": \"'chi-bouk', chi-bouque' … [Turk. chibuq, a pipe.]' — same origin, but Webster omits the French intermediary.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 1 (FSD_vol1.txt line 64630)\", \"stance\": \"partial\", \"note\": \"only the plate caption 'Chibouk of an Arab Sheik' survives legibly in this OCR; the word is in the dictionary but its etymology line could not be read.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.114 CHIBOUQUE\", \"stance\": \"supports\", \"note\": \"documents the French form that English borrowed.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through node: the Greek box is printed empty in the book (only the header 'Greek  SKT:87'), so the extraction is faithful — no word was lost. The word Nourai means is Byzantine (medieval) Greek τζυκάνιον tzykánion 'the game of polo, mall', with the verb τζυκανίζειν 'to play at mall' and τζυκανιστήριον, the polo ground built beside the Great Palace in Constantinople. It was taken over from Middle Persian čawgān/čōkān when the Sasanian court game reached Byzantium; the Iranian affricate č- is rendered by the Greek cluster τζ-, the regular treatment of č in Greek loans from Iranian, and the ending was Hellenised with the neuter diminutive -ιον. Skeat s.v. chicanery states the same: 'chicane is from the medieval Gk. …, a word of Byzantine origin …, from Pers. chaugān, a club, bat', and Lokotsch p.35 no.434: 'Nach Byzanz gelangt, hieß das Spiel mgr. τζυκάνιον, Vb. τζυκανίζειν, \\\"Spielplatz dafür\\\" τζυκανιστήριον'.\",\n          \"derivation_fa\": \"این گره در کتاب تهی چاپ شده است (تنها عنوان «Greek  SKT:87»)، پس خطای خوانش اسکن در کار نیست و متن استخراج‌شده وفادار است. واژه‌ای که نورایی در نظر دارد یونانیِ بیزانسی τζυκάνιον (tzykánion) «بازی چوگان» است، با فعل τζυκανίζειν «چوگان بازی کردن» و τζυκανιστήριον «میدان چوگان» که در کنار کاخ بزرگ قسطنطنیه ساخته شده بود. این وام‌گیری هنگامی روی داد که بازی درباری ساسانی به بیزانس رسید؛ چِ ایرانی در یونانی با خوشهٔ τζ بازنمایی شده — دگرگونی آوایی معمول در وام‌واژه‌های ایرانی در یونانی — و پایانهٔ خنثای ‑ιον به آن افزوده شده است. اسکیت و لوکوچ (ص ۳۵، شمارهٔ ۴۳۴) هر دو همین را می‌گویند. ادعای نورایی در این پیوند (فارسی ← یونانی بیزانسی) درست است.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Tzykanisterion\",\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%88%DA%AF%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:87\", \"status\": \"supports\", \"note\": \"Skeat, Concise Etymological Dictionary, s.v. Chicanery — in our 1911 scan the entry is on leaf 99 = printed p.79, not p.87 (p.87 of that scan carries Clumsy–Cobalt), so Nourai used a printing with different pagination; but the text is exactly his claim: 'Chicanery, (F. – Pers. ?) … chicane is from the medieval Gk. …, a word of Byzantine origin … from Pers. chaugān, a club, bat.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch p.35 no.434 (LKT.txt leaf 61)\", \"stance\": \"supports\", \"note\": \"'434. Pers. čōgān: \\\"Schlägel (im Ballspiel)\\\" [Horn NpEt S.100, Nr.449] … Nach Byzanz gelangt, hieß das Spiel mgr. τζυκάνιον, Vb. τζυκανίζειν, \\\"Spielplatz dafür\\\" τζυκανιστήριον, und in Frankreich, wo es zu Fuß gespielt wurde, chicane.'\"},\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Chicane (DEV.txt leaf 125, printed ≈ p.95; cross-references at 'Τζυκανίζειν, voy. Chicane. Τζυκάνιον, voy. Chicane')\", \"stance\": \"supports\", \"note\": \"'on trouve, en bas grec, τζυκάνιον, jeu de mail; τζυκανίζειν, jouer au mail. Tout cela ne laisse aucun doute sur l'étymologie: c'est le persan تشوگان tchaugân, bâton recourbé, maillet pour jouer au mail.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg II p.59 s.v. čōwčgān\", \"stance\": \"supports\", \"note\": \"documents the Middle Persian source form cwpygʾn' that the Greek word renders.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"chicaner\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"This is the weak link of the chart. A 19th-century Orientalist tradition — Brachet, Quatremère, Devic, Pihan, Skeat, Lokotsch, and Mo'in in his footnotes to Borhan-e Qate' — derived French chicane / chicaner from Byzantine Greek τζυκάνιον by way of a Languedoc game of mail: Devic quotes Chapelle and Bachaumont (17th c.), 'on joue là, le long des chemins, à la chicane', and concludes 'Tout cela ne laisse aucun doute sur l'étymologie: c'est le persan tchaugân', explicitly rejecting Ménage's, Diez's and Génin's Spanish chico 'small'. Modern etymology does not accept it. The decisive objection is chronological and semantic: chicaner appears in the 15th century as a legal term 'to quibble, pettifog', a century and more before any French evidence for the game sense, and no Old French or Occitan form linking it to τζυκάνιον is attested. Klein calls chicaner 'of uncertain origin'; Etymonline: 'of unknown origin, perhaps from Middle Low German schikken \\\"to arrange, bring about\\\", or from the name of a golf-like game once played in Languedoc'; Wiktionary derives it from Proto-West-Germanic *skikkijan (whence also chic). So Nourai's arrow reproduces a once-standard but now minority view.\",\n          \"derivation_fa\": \"این حلقه سست‌ترین بخش نمودار است. سنّت شرق‌شناسیِ سدهٔ نوزدهم — براشه، کاترمر، دُویک، پیهان، اسکیت، لوکوچ و نیز معین در حواشی برهان قاطع — واژهٔ فرانسوی chicane/chicaner را از یونانی بیزانسی τζυکάνιον و از راه بازی گوی‌وچوگانِ لانگدوک گرفته‌اند؛ دُویک با استناد به شاهدی از سدهٔ هفدهم («در آنجا در امتداد راه‌ها chicane بازی می‌کنند») نتیجه می‌گیرد «هیچ تردیدی در این ریشه‌شناسی نیست: همان چوگان فارسی است» و ریشه‌شناسی مِناژ و دیتس (اسپانیایی chico «کوچک») را رد می‌کند. اما ریشه‌شناسی امروزی این را نمی‌پذیرد. ایراد اصلی تاریخی و معنایی است: chicaner از سدهٔ پانزدهم و در معنای حقوقی «مو از ماست کشیدن، پیچ‌وخم انداختن در دعوا» گواهی شده، یعنی بیش از یک سده پیش از هر گواهِ فرانسویِ معنای بازی، و هیچ صورت فرانسویِ کهن یا اکسیتانی که آن را به τζυκάνιον بپیوندد در دست نیست. کلاین آن را «با خاستگاه نامعلوم» می‌داند، اتیمانلاین «ناشناخته، شاید از آلمانی میانهٔ سفلی schikken»، و ویکی‌واژه آن را از ژرمنیِ باختریِ آغازین *skikkijan (هم‌ریشه با chic) می‌گیرد. پس پژوهش امروزی ادعای نورایی را نمی‌پذیرد و آن را دیدگاهی کهنه و اقلیتی می‌شمارد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chicanery\",\n            \"https://en.wiktionary.org/wiki/chicane\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"WEB:312\", \"status\": \"supports\", \"note\": \"Webster's New Twentieth Century Dictionary, 2nd ed. (WEB_vol1.txt leaf 341, the p.312 'chi-' page): 'chi-cane', n. [Fr., from Per. chaugān, the game of polo. The various senses are figurative of the methods of the game.]' and 'chi-cane', v.t. … [Fr. chicaner, to use trickery.]' — Webster states Nourai's claim word for word, but it represents the older lexicographic tradition.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Chicane (DEV.txt leaf 125, printed ≈ p.95)\", \"stance\": \"supports\", \"note\": \"'Ce mot … a dû désigner primitivement le jeu du mail … Tout cela ne laisse aucun doute sur l'étymologie: c'est le persan tchaugân, bâton recourbé, maillet … Aussi comprend-on difficilement que Diez et Génin aient voulu, après Ménage, chercher l'origine de chicane dans l'espagnol chico, petit.'\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.114-116 s.v. CHICANE, s. f. (p.) (PHN.txt leaf 145)\", \"stance\": \"supports\", \"note\": \"'چوگان [tchevkiân], chez les Persans, désigne la raquette pour jouer à la paume … L'exercice de la chicane, inventé par les anciens habitants de la Perse, avait lieu à cheval …' — tagged (p.) = Persian; Pihan credits Quatremère's note in the Histoire des sultans mamlouks.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Chicanery (SKT.txt leaf 99, printed p.79)\", \"stance\": \"supports\", \"note\": \"'chicane is from the medieval Gk. …, a word of Byzantine origin …, from Pers. chaugān, a club, bat' — but note Skeat's own question mark in the heading '(F. – Pers. ?)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. chicane, v. (KLN_1966.txt leaf 155)\", \"stance\": \"contradicts\", \"note\": \"'chicane, intr. v., to trick. — F. chicaner, \\\"to quibble, wrangle, quarrel\\\", of uncertain origin; prob. not related to MHG. schicken' — Klein names no Persian or Greek source at all.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch p.35 no.434\", \"stance\": \"supports\", \"note\": \"'… und in Frankreich, wo es zu Fuß gespielt wurde, chicane. Das frz. Wort bedeutete dann, daß man in einem Kampfe jeden möglichen Vorteil wahrnehmen durfte, und kam so zu seiner heutigen Bedeutung frz. chicane \\\"Kniffe, Schabernack, Rechtsverdrehung, Spitzfindigkeit\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"chicane; chicanery\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The step drawn here — French → English — is uncontested. English chicanery is recorded from c.1610 in the sense 'legal quibbling, sophistry, mean or petty tricks', from French chicanerie 'trickery' (itself from chicaner, 15th c.); the noun chicane follows in the 1670s from French chicane 'trickery' (16th c.), later also 'a hand without trumps' in bridge and 'an artificial bend in a racing circuit'. Klein: 'chicanery, n., trickery, quibbling, sophistry. — F. chicanerie, fr. chicaner'; Webster: 'chi-canér-y, n. … trickery, especially legal trickery … [from chicane]'. Both English words are therefore correct as printed and correctly attached to the French parent; what remains open is only the origin of the French word itself (node #7).\",\n          \"derivation_fa\": \"این پله — فرانسوی ← انگلیسی — بی‌مناقشه است. واژهٔ انگلیسی chicanery از حدود ۱۶۱۰ میلادی در معنی «موشکافی و پیچاندنِ حقوقی، سفسطه، ترفندهای خرد» گواهی شده و از فرانسوی chicanerie «حیله» گرفته شده است، که خود از chicaner (سدهٔ پانزدهم) است؛ اسم chicane در دههٔ ۱۶۷۰ از فرانسوی chicane «حیله» (سدهٔ شانزدهم) وارد شده و بعدها معناهای تازه‌ای مانند «دستِ بدونِ خال حکم» در بریج و «پیچ ساختگی در پیست مسابقه» یافته است. کلاین و وبستر هر دو همین را می‌آورند. پس هر دو واژهٔ این گره درست‌اند و درست به پدرِ فرانسوی خود بسته شده‌اند؛ آنچه ناروشن می‌ماند تنها خاستگاه خودِ واژهٔ فرانسوی است (گرهٔ ۷).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chicanery\",\n            \"https://en.wiktionary.org/wiki/chicane\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"WEB:312\", \"status\": \"supports\", \"note\": \"Webster 2nd ed. p.312 (WEB_vol1.txt leaf 341): 'chi-cane', n. … 1. the art of protracting a contest or discussion by the use of evasive stratagems or mean and unfair tricks and artifices; trickery' and 'chi-canér-y, n.; pl. chi-canér-ies, 1. trickery, especially legal trickery; sophistry; mean or unfair artifices used in contest or discussion; chicane.' — both glosses as in the chart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. chicane, chicanery (KLN_1966.txt leaves 155-156)\", \"stance\": \"supports\", \"note\": \"'chicane, n., chicanery. — F., \\\"quibble, evasion\\\", fr. chicaner' and 'chicanery, n., trickery, quibbling, sophistry. — F. chicanerie, fr. chicaner.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 1 (FSD_vol1.txt line 64704)\", \"stance\": \"supports\", \"note\": \"'[< F. chicanerie, < chicaner; see chicane, n.]' with the synonym list 'cheat, chicane, dodge, mystification, pettifogging, prevarication, quibble …'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Chicanery (SKT.txt leaf 99, printed p.79)\", \"stance\": \"supports\", \"note\": \"'Chicanery, (F. – Pers. ?) F. chicanerie, wrangling, pettifogging; Cot. — F. chicaner, to wrangle; orig. to dispute in [the game] of the mail or chicane (Brachet).'\"},\n            {\"src\": \"WEB\", \"where\": \"Webster 2nd ed. p.312\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T17:25:43.666Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-107.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T17:25:46.051Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-107.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 107",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T17:25:50.380Z] TOOL RESULT

```
JSON OK
nodes verified: 8/8
node verdicts: {'confirmed': 6, 'disputed': 2}
root verdicts: {'plausible': 1}
ref checks: {'partial': 2, 'not_checked': 1, 'supports': 5}
books consulted: {'supports': 22, 'partial': 5, 'silent': 2, 'contradicts': 2} | by book: {'PHN': 5, 'KLN': 4, 'BQT': 3, 'LKT': 3, 'DEV': 3, 'NYB': 2, 'MON': 2, 'WEB': 2, 'FSD': 2, 'SKT': 2, 'PHD': 1, 'HRN': 1, 'TTS': 1}
```


## [2026-09-05T17:26:13.299Z] AGENT

Done. `verify_check.py 107` reports 8/8 nodes, 0 PROBLEM lines.

**Page 107 (book p. 77) — root Čop / Čop-gân**

- Root verdicts: 1 plausible. Node verdicts: 6 confirmed, 2 disputed.
- Ref checks: 5 supports, 2 partial, 1 not_checked. 31 `consulted` entries across HRN, PHD, NYB, KNT, HUB, ARY, BQT, MON, LKT, TTS, SKT, KLN, WEB, FSD, DEV, PHN.

Disputed / notable:
- **Root "Old Persian Čop"** — plausible, not confirmed: there is no Old Persian *čub-. Kent's OP lexicon has only `dāru-` for "wood"; Horn no. 448 himself labels the ancestor "phlv. čōp"; MacKenzie p. 24 `čōb [cwp]`. The label should be **Middle Persian**, not Old Persian.
- **#2 Turkish čŭb / čubŭq — disputed.** Lokotsch (p. 36 no. 447) derives Turkish çubuk from Persian čūb, but modern Turkology takes it as native: Ottoman çıbuk/çubuk < Proto-Turkic *čöpik, dim. of *čöp "twig" (Turkish çöp). Lokotsch's own "N. cob" form is in fact Turkish çöp. A Turkish lemma "čŭb" does not exist. The chart's own NOTE already flags the doubt.
- **#7 French chicaner — disputed.** The Byzantine-Greek τζυκάνιον → chicane route (Devic, Pihan, Skeat, Lokotsch, Webster, and Mo'in's Borhan footnote) is a 19th-c. consensus that modern etymology rejects: chicaner is attested from the 15th c. as a legal term, long before any French game sense; Klein "of uncertain origin", Etymonline "unknown", Wiktionary/TLFi favour Proto-West-Germanic *skikkijan. #8 (F → E chicane/chicanery) is itself sound.

Confirmed highlights: čūb < MP čōb; čowgān < MP čōbagān/čōbgān (Pahl. cwpygʾn', Nyberg p. 59) — Borhan-e Qate' still heads the entry چوبگان, direct evidence for čōb + -agān; چپق < Ottoman çubuk (Mo'in's footnote s.v. چپق, which also says the French word comes from the same Turkish word); Greek node = τζυκάνιον < MP čawgān.

Extraction errors: **none**. The Greek box (#6) is genuinely printed empty in the book (checked `site/pages/107.jpg`); the JSON is faithful. Two citation slips are Nourai's, not the extraction's: HRN:99 covers čōb but čōgān is p. 100 no. 449; LKT:35 has Pers. čōb (no. 432) but the Turkish-from-Persian claim is p. 36 no. 447. SKT:87 and KLN:275 land a few pages off in our scans (chicanery at p. 79, chibouk ≈ p. 286) — different printings, the entries say what he claims.

Six web pages archived via `fetch_source.py` (Wiktionary چوب / چوگان / çubuk / chicane, Etymonline chicanery, Wikipedia Tzykanisterion). Not committed — let me know if you want a commit.
