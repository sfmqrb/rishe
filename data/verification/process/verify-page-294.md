# Verification process log — verify-page-294


## [2026-09-06T22:13:48.238Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 294 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-294.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-294.json. Write /home/sfmqrb/git/rishe/data/verification/page-294.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 294` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:13:49.557Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:13:50.379Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:13:50.398Z] TOOL RESULT

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


## [2026-09-06T22:13:50.924Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-294.txt"
}
```


### [2026-09-06T22:13:50.955Z] TOOL RESULT

```
1	=== PDF page 294 (book page 264) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwes : to pant, to breathe fast  (refs POK:631; CEL6:284)
4	#1 (parent #0) [Avestan] refs=POK:631; SYN:260 | suši, suš : the lungs
5	  #2 (parent #1) [Pahlavi] refs=SNS:192 | suš : lung
6	    #3 (parent #2) [Persian] refs=HRN:173; BQT:1266 | šoš «شُش» : lung
7	#4 (parent #0) [Persian] refs=CEL6:284 | havâ «هوا» : air
8	#5 (parent #0) [Greek] refs=AHD | kustis : bladder, bag
9	  #6 (parent #5) [English] refs=None | cyst
10	#7 (parent #0) [Latin] refs=AHD | queri : complain
11	  #8 (parent #7) [English] refs=None | quarrel
12	#9 (parent #0) [Old Norse] refs=CEL6:286 | hwosan : puff
13	
```


## [2026-09-06T22:13:55.101Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-294.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','CEL','SYN','SNS','HRN','BQT','AHD','MON','PHD','NYB','WLD','IEC','KLN','SKT','HUB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T22:13:56.914Z] TOOL RESULT

```
{
  "pdf_page": 294,
  "book_page": 264,
  "entries": [
    {
      "root": {
        "name": "Kwes",
        "lang": "Indo-European",
        "refs": "POK:631; CEL6:284",
        "gloss": "to pant, to breathe fast"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:631; SYN:260",
          "words": [
            {"translit": "suši, suš", "gloss": "the lungs", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:192",
          "words": [
            {"translit": "suš", "gloss": "lung", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:173; BQT:1266",
          "words": [
            {"translit": "šoš", "gloss": "lung", "script": "شُش"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Persian",
          "refs": "CEL6:284",
          "words": [
            {"translit": "havâ", "gloss": "air", "script": "هوا"}
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
            {"translit": "kustis", "gloss": "bladder, bag", "script": null}
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
            {"translit": "cyst", "gloss": null, "script": null}
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
            {"translit": "queri", "gloss": "complain", "script": null}
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
            {"translit": "quarrel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old Norse",
          "refs": "CEL6:286",
          "words": [
            {"translit": "hwosan", "gloss": "puff", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
CEL {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Ha
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-06T22:14:11.979Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


### [2026-09-06T22:14:12.016Z] TOOL RESULT

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


## [2026-09-06T22:14:12.710Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T22:14:12.758Z] TOOL RESULT

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


## [2026-09-06T22:14:17.000Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"hwosan\\|hwōsan\\|hvæsa\\|hvaesa\" POK_full.txt | head -20; echo \"--- kues 631 ---\"; grep -n \"ku̯es-\\|kues-\\|kṷes-\" POK_full.txt | head -20"
}
```


### [2026-09-06T22:14:17.059Z] TOOL RESULT

```
52212:lengthened grade Old Icelandic hvaesa. Old English hiA^osan^ pant, gasp'; 
--- kues 631 ---
```


## [2026-09-06T22:14:18.013Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kwes ===\"; grep -n -i \"kwes\\|kustis\\|queri,\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T22:14:18.063Z] TOOL RESULT

```
=== AHD kwes ===
266:agwesi. Ax. Germanic *akwesi, *akusj6- in Old English zx, ax: AX. [Pok. agu(e)si 9.]
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
2146:QUA kWo- QUACKSALVER gWébh-2, selp- QUADRANT kWetwer- QUADRATE kWetwer- QUADRENNIUM at- QUADRI- kWetwer- QUADRILLE! kWetwer- QUADRILLE? kwetwer- QUADROON kWetwer- QUADRUMANOUS man-2 QUADRUPLE pel-3 QUAESTOR quaerere QUAGMIRE meu- QUAINT gnd- QUALIFY dhé-1 QUALITY kWo- QUANTITY k¥o- QUARANTINE kWetwer- QUARREL! kwes- QUARREL2 kwetwer- QUARRY! kerd-1 QUARRY? kwetwer- QUART kWetwer- QUARTAN kwetwer- QUARTER kWetwer- QUARTO kWetwer- QUARTZ twer-2 QUASH kes-2
2149:QUELL gWel-1 QUENELLE gen- QUERCETIN perkWu- QUERCITRON perk"u- QUERIST quaerere QUERN gWera-2 QUERULOUS kwes- QUERY quaerere QUEST quaerere QUESTION quaerere QUIBBLE kWo- QUICHE kak-2
```


## [2026-09-06T22:14:22.839Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52195,52240p' POK_full.txt"
}
```


### [2026-09-06T22:14:22.892Z] TOOL RESULT

```
Wannebobbeir arum maculatum ', Lithuanian svendraiP\. "a kind of reed, Typhalatifolia '. 
References: WP. I 472, WH. I 253. 
Page(s): 631 



Root / lemma: Rues- Rus- {*k"'ehus-) 

Meaning: to puff, sigh 

Material: Old Indie sVas/// (inflection perhaps previously after an/'t/^ breathes '), svasat/" 

breathes, wheezes, sighs ', a'susana- " piping, whistling ', Avestan susi^ both lungs '; 

Latin queror, -T, questus sum " to express grief, complain, lament, bewail ' (: Old Indie 
svasati); 

lengthened grade Old Icelandic hvaesa. Old English hiA^osan^ pant, gasp'; 

Lithuanian sus/nt/" mit zischendem Gerausch durch die Luft fahren ' (it could be like Old 
High German suson^ buzz, whirr, whiz, swish, whistle ' an independent onomatopoeic 
word). 

The Rues-\s an extension of a Ru-, ^e:/- through -es-{a\. most onomatopoeic origin), one 
supposes because of the same initial sound in Old Indie sOt-kara- m. " the whistle, hiss ' 
(perhaps rather like sTt-kara- new onomatopoeic word formation?), Armenian sulem^ 
whistle, fizz ' (from *soyl= keu-lo-or kou-lo-)\ Lithuanian 5i/-5/7/rs//" breathe, wheeze, pant, 
gasp': Armenian 5i//7c 'breath, breeze, soul, ghost' {kuonkio-); Lithuanian 5i//?/rs// "whistle, 
buzz, whirr ', svilptT whistle, pipe, sing, whine, howl, whiz, whirr, hiss, hurtle ' and in the 
root Ruei-2Y(\ss ' see there. 

References: WP. I 474 f., WH. II 403 f. 
Page(s): 631-632 

Root/ lemma: Ruon-, Run-{*k'^ehun-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: dog (*animal with a strong sense of smell) 
Grammatical information: originally Nom. Sg. Ruud(n), Gen. Runos 
Material: 

In e- grade: 

French chien: Albanian {*kjen) qen: Furlan cjan: Dzoratai tsin: Breton ki: Welsh ci: 

Viestano cheh : Wallon tchen " dog'. 

Common Hittite Slavic /?£/-> alb. Geg y, alb. Tosc /)/
```


## [2026-09-06T22:14:37.554Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 474 kues ===\"; grep -n -i \"susi\\|hvaesa\\|hwosan\\|hwōsan\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20; echo \"=== SYN lung ===\"; grep -n -i \"4\\.46\\|LUNG\" SYN.txt | head -20"
}
```


### [2026-09-06T22:14:37.617Z] TOOL RESULT

```
=== WLD Bd1 474 kues ===
1023:Osk. aisusis abl. pi. „sacrifieiis“, marnuc. aisos d. pi. „dis“, piilign. 
7831:schwundstufig aus dem schwachen Kasusi, got. tanpus i aus dem Akk. 
23035:beck Ai. Wb. 338 wohl besser als susi-; Holthausen KZ. 47, 31 1 setzt gusi- 
29871:rrdsati „atmet. schnauft, seufzt“, iiguiilnd- „pfeifend“, ay. susi ,,die beiden 
=== SYN lung ===
340:Abh. Preuss. Akad. Abhandlungen der preussischen Akademie der Wissenschaften.
341:Abh. Siichs. Ges. Abhandlungen der siichsischen Gesellschaft der Wissenschaften.
353:Ber. Sichs. Ges. Berichte iiber die Verhandlungen der siichsischen Gesellschaft der Wissen- schaften zu Leipzig.
1380:Most of the words are derived from roots meaning ‘flow, run’. Some are cognate with words for ‘water’, perhaps originally ‘flowing water’ (cf. 1.31). Some are from verbs for ‘rush, plunge’, or ‘roar’, applied first to a rushing, roar- ing stream.
1393:4. Grk. rorapss (NG POp. wordt), fr. root of rimrw ‘fall’, réropat ‘fly’, Skt. pat- ‘fly, fall’, etc. That is, Torayés was at first the ‘falling, plunging, rushing’ stream. Walde-P. 2.19. Persson, Bei- trige 654. Kretschmer, Glotta 27,248 f.
2513:OE cild, ME, NE child : Goth. kilpez ‘womb’, Skt. jathara- ‘belly, womb’ (4.46). Shift from ‘womb’ to ‘child in the womb’ (so sometimes in OF), hence “Gnfant? (cf. Grk. Bpédos ‘foetus’ and ‘newborn babe’), then with extension of scope as in Fr. enfant fr. Lat. infans. Walde-P. 1.614. NED s.v. child.
4536:3. Lat. caballus, in part attested as ‘gelding’, mostly ‘work horse’ (cf. xaBéd- dys’ Epyarns tmmos Hesych.), sometimes pejorative ‘old nag’, but eventually simply ‘horse’, in VLat. displacing equus, and so the source of the Romance words, also Ir. capall, W. ceffyl (Pedersen 1.226, Vendryes, De hib. voc. 121). Cf. also late Lat. cabd, Onis in glosses (cabal- Tus, caballus magnus, equus castratus), Grk. xaBnXos ‘castrated’ (Hesych.), ChSI. kobila ‘mare’, ete. Certainly a loanword, but precise source dub. Prob. orig. ‘gelding’ and of ethnic orig. (Anatolian or Balkan) like Fr. hongre, NHG wallach, ete. (3.43). Walde-H. 1.125. Ernout- M. 124. Maas, Rh. M. 74.469. Kretgch-
5972:Grk.  -yAdooa Goth. tuggd NG yAGooa ON tunga Lat. lingua Dan. - tunge It. lingua Sw. tunga Fr. langue OE lunge Sp. lengua ME tounge Rum. limbd NE longue Ir. lenge Du. tong Nir. teanga OHG zunga W. tafod ; MHG zunge Br. teod NHG zunge
6498:4.46 BELLY; STOMACH
6578:are related to those wo eye aa have been discussed in 4.46. Yee others the commonest source is mou er", while some are words for ‘body’ or lap used in specialized sense, or of various other sources.
6582:ely, ete. (4.46) with
6732:Skt. ¢vas-, cvdsa-: Av. susi- ‘the lungs’, Lat. quer? ‘lament, bewail’, ON hvesa, OF hwesan ‘pant’, etc. Walde-P. 1.474,
7098:OE-NE dung, Sw. dynga (Dan. dynge ‘heap’), OHG tunga (‘manuring’), MHG lunge, NHG diinger (ON dyngja, OHG, MHG tune ‘underground room’) : Lith. ae i cover’, danga ‘a cover’, IE i lg -. Development fr. ‘covering’ to
7265:G (y) yaor we Ais + 12600; iste et, oF ere belly, Womb’ (4.46) pe GIK. Yaorhp
9810:2. Grk. e&étw (‘put on’, mid. ‘be clothed in’: cf. é&éiw ‘take off’), NG pop. vrivw, cpd. of diw ‘sink, plunge, en- ter’ : Skt. wpd-du- ‘put on’. Walde-P. 1.777.
13908:wm foul, skoulm 13 e, cord, etc., 1S & pa a ie words are mostly means a Pics denoting ‘tie, fasten’ cognate ee Pefnstening: The applica- Sa jump or protuberance in the body or on a tree is clearly secondary in at, nodus. For the Gme. group as @ whole the view that the latter sense 1s the earlier (cf, Paul, Deutsches Wtb. s.v. Knoten, “bedeutet urspriinglich ‘riind- liche Anschwellung an einem Gegen- stand’”) is favored by the nearest cog- nates like OHG knopf ‘knob, knot’, OF cnoll ‘hilltop’, etc. But in the history of OE cnotta—NIE knot, this sense is chronologically later (NED s.v. knot, sb!, 13-16) and for the prevailing earlier use, cf. the derivative OE cnytta ‘tie with a knot’ (NE knit). i Gre Guua (anything for tying, cov- a te opr),
14416:From the central notion of ‘stretch’ involving tension come a great variety of special uses, as ‘stretch out, put forth’ (the hand, etc.), ‘reach for, tend’, ‘spread out, extend, lengthen’, etc., with considerable divergence in this respect between the different words (as ‘tend, strive’ esp. in Lat. tendere, ‘extend, lengthen’ dominant in NHG dehnen). Conversely, some one of these notions may be the more original, as in the case of NE stretch (cf. below, 5), or if a word for ‘lengthen’ is used for ‘stretch’, as It. allungare.
16929:6. ChSI., SCr. pasti, Padati, ete general Slavic : Skt. pad- ‘fall, go’, hee pad-, paés- ‘move downward, plunge down’, prob. the same root as in Skt, pad-, Grk. wots, etc. ‘foot’. Walde-P, 2,28.
17113:Raa Wash’ (through ‘dip, plunge into
17127:K. Meyer, Contrib. 161), NIr. baidhim, badhaim : W. boddi, Br. beuzi ‘drown’, Skt. gah- ‘plunge (into)’, gaha- ‘depth’, IE *g’ddh-. Walde-P. 1.665. Pedersen 2.458 f.
```


## [2026-09-06T22:14:38.874Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT susi ===\"; grep -n -i \"sušI\\|suši\\|su.i-\\b\" BRT.txt | head -20; echo \"=== BRT search 2 ===\"; grep -n \"Lunge\" BRT.txt | head -20"
}
```


### [2026-09-06T22:14:38.951Z] TOOL RESULT

```
=== BRT susi ===
20955:duqnmaihyascä  yaogst  (jSPrA.)!'  äsa  Y. 44. 4.  3)  'vertraut  machen  mit  — ,  ge- wöhnen an  — '  (Instr.)''':  xswiräÜ  yüjSn AarapartO  kävayascä  akäis  ^ao%anäis ahüm  mjnngidyäi  tnaslm  "durch  ihre Herrschaft  gewöhnen  die  Karapan  und die  Kavay  den  Menschen  an  böse  Taten, um  das  (zweite)  Leben  zu  zerstören"  Y. 46.  II.  4)  'einer  Sache  (Lok.)  teilhaftig machen':  hyat  dai^M  vahi^t! yUpn  mXidi as'i  yuxiä  (s. ab)  y<lAl  dijämaspä  "wenn die  mit  Aih  verbündeten  ihr  Ich  beim Schlusswerk  des  besten  Lohns  teilhaftig machen,  oJSm."  V.^p.g.  a)  Med.  'teil- haftig werden' :  at  asiää  yaojanU  ä  htiliisU i-auhSus  jnanaahö  mazdä  asahyäiä  yöi  .  . "aber  des  verheissenen  Lohnes  werden  in der  guten  Wohnung  des  VM.,  des  M.  und des  A-"a  die  teilhaftig  werden,  die  .  ," Y._jt).  10.  5)  Med.  'sich  rüsten,  sich bereit  machen' :_j'ax/a  (jSPrM.)  pmrulaspö tyKf/iwVe  (3PPM.)5>  n ysi  ptikra  ^raitao- nahe  F.4(.
=== BRT search 2 ===
26437:•  j.  suä-  £,  Du.  'Lungen':  °si  F.jg, lEt.  s.  S  ja  —   mp.  (Pü.)  sui,  np.  his,  kurd. /«;  S  f/S  b.
```


## [2026-09-06T22:14:50.730Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ctx ===\"; sed -n '26425,26445p' BRT.txt; echo \"=== BRT page marker ===\"; awk 'NR<=26437 && /^[0-9]{3,4}$/ {p=$0; n=NR} END{}' BRT.txt; grep -n \"^\\s*1580\\|^\\s*1581\" BRT.txt | head"
}
```


## [2026-09-06T22:14:52.070Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD 29860-29885 ===\"; sed -n '29860,29885p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== WLD 23025-23040 ===\"; sed -n '23025,23040p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T22:14:52.644Z] TOOL RESULT

```
=== BRT ctx ===
V.  19.23.
•  j.  sürö.yazata-  m.  EN.  eines  Gläubigen: *tahe  aSaonS  Yt  13, 118.
Eig.  Bed.?
•  j.  suri-  i.  'Häuf  uzw.  des  Menschen: •rr  F.  Jb.
vgl-  Ut  skurä  'Haut'  (lu  %  ,55.  1),  ai.  chavt-^. 'Haut';  Bthl.  Stud.  2.  57.  —  Pü. :  pöst  i  martum i  üvandak.
•  j.  "suru  N.  21.
Im   Original   muss
gestanden  haben:  lurun-
vainü  ufit.iraaläröl%i^zrularS.  Der  Abschreiber hat  wohl  eine  Zeile  ausgelassen. j.  mmn':  s.  bei  tr'.
•  ').  süirya-  n.  'FrUhmahl,  -stück':  yaHbyS afm  (näml.  ätarl)  kamfpacaiti  xlsfitlmca 'rJmca  "denen  er  das  Nacht-  und  das Frtihmahl  kocht"  Y.6'2.  7; —  «jff/n  (sd.) "rJtn  is»mnS  Vt.  14.  20.
AbleiL  aas  ivar-.  —  np.  sär  'Gelage'. —  PB. : sir,  SQ. :  utiavapäiah.  —  1)  F  I  hat  hier  ivi- rim;  vgl.  unter  kvirinla-.
•  j.    susniäsmna-    Adj.,    PP16M. ;    s.
•  j.  suä-  £,  Du.  'Lungen':  °si  F.jg, lEt.  s.  S  ja  —   mp.  (Pü.)  sui,  np.  his,  kurd. /«;  S  f/S  b.
•  j.  skatay-  f.  'Heuschrecke"  (?) ",  als  Land- plage von  Gava  (Sogdiane):  gilum  yim suyös.sayanfm  aal  ahe  paityär^m  fräkiryii- tat  anrö  mainyus  .  .  'ilim  yqm  gavaca daya(sd.)ca  pouru.mahrk>m  V.  r.  4,
Der  Text  ist  inkorrekt  und  inhaltlich  unklar.  — Pu. :  knrkn  maW  ('Heuschrecke')  i  gSspan- dän  dadtrii  i pur  mark;  erl.:  ma\ak  ape  äyil iiirläk  -  ku  ape  vSitr  apt  äyil  —  gäv  baslan HC  säytt  gäspandma  mariih  bavel.  AuchOrBd. (s.DST.ZA.2.8)  bietet  'Heuschrecke'  -  kmca; s.  PPGI.  ff.  3  -  für  skailJm.  —  0  So  nach der  Tradition;  s.  oben.  Anders  FkMOllek WZKM.  3.  366,  6.  183.
•  j.  skapta-  Adj.  'erstaunlich,  wunderbar':
mp.  (Pö.)  SliafI  (in  SO.:  adMutai),  np,  ügr// 'Erstaunen',  iiguflan  'sich  wandern'.
•  j.  skand- V. 'brechen'.   Praes.9  +  24'>
scandaya-,  ^shndaya-,  scindaya:
'zerbrechen,  zerstören,  zu  nichte  machen' : yS  rasmanö  iHndayäti  Yt  14.  62;  — Jra- vasayS  .  .  yä  .  .  aurva%anqm  ,  .  iSsBs scandayeinti  YtJj.  31;  —  ime  nS  *^uyra *bäzava  kanta  .  .  sHndayeinti  "die  da machen  unsere  starken  Arme  . .  mit  dem Messer  zu  nicht"  Yt.  /o.  42;—  tum  aisqm.. Ibaisi  scindayehi  Yt. 70.76;  —  alsqm  ihai^S scindaydmtmYt.i.tT,  —  sSndaya  {i%lh..) asavajanS  Yt.  iO.  76;  —  scindayat  F.  12,
mit  ai>i  'entzweibrcchen'(?):  yS ratmanS sHndayäti  . .  avi  rasmans  *sc?ndayeiti'^ Yt  14.  62.
=== BRT page marker ===
```


### [2026-09-06T22:14:52.704Z] TOOL RESULT

```
=== WLD 29860-29885 ===
DaB lat. culcita „Kissen, PolsterA ai. k ft red- m. JBiindel, Ballen, Biischel 1 
(s. Yf. LEWb. 2 s. v.) iin Verhaltnis der Wurzelvariation (*quel-q- : -p-) zu 
obigen Worten stehn (Zupitza und Petersson aaO., der das gemeinsame 
Element quel- weiter als qu-e 1- auf ein qeu- „biegen“ zuruckfiihren mochte). 
ist ganz unsicher, da eine Gdbed. „gewolbtes“ fur culcita, kiirgd- bloBe An- 
nahme ist (daB mit letztern nach Hirt BB. 24, 249 ai. cuda- m., cuda „Wulst, 
Schopf, Kopf, Gipfel“ entfernter verwandt sei, ist nicht glaublich). 

■kues- ,,keuchen, schnaufen, seufzen“. 

Ai. gvdsiti (set-Flexion vielleicht erst nach aniti ,,atmet“', Sommer KE. 82), 
rrdsati „atmet. schnauft, seufzt“, iiguiilnd- „pfeifend“, ay. susi ,,die beiden 
Lungen“ (die ar. Worte kaum nach Osthoff Pf. 495 ff., Bartholomae Grdr. 
I 19 — s. auch Wackernagel AiGr. I 226, Charpentier IF. 25, 250 Anm. 2 — 
zu ahd. suson „sausen“); lit. s us inti „mit zischendem Gerausch durch die 
Luft fahren' 1 (?? konnte wie ahd. suson eine unabhangige Schallnachahmung 
sein) ; lat. qucror, questus sum „klagen, sich woriiber beklagen, weh- 
klagen"' ( = ai. rvdsati; Yanicek LEWb. 2 73, s. auch Sommer KE. 82 gegen 
die Zweifel Ostholfs aaO. und Hirts BB. 24, 289); dehnstufig aisl. hvcesa , 
ags. hwcBsan „keuchen“ (nicht nach Berneker 655 f. zu si. kvasz, lat. ca- 
seus ; dt. Hasten gehort zu *qas-) ; Falk-Torp u. dan. vaasc „faseln“, alter 
hvase reihen zw. dieses, sowie schwed. dial, hvasa „sausen“, hvassma 
„scbnarren“, iilter dan. hvasle „verleumden“, mhd. tvaschen „schwatzen, 
faseln 1- nhd. (lewdsch an. Lautlich unwahrscheinlich ist Entstehung von air. 


=== WLD 23025-23040 ===
go-pha- m. (s. Persson Beitr. 565) „Geschwulst, Geschwiir"; goLva- m. „das 
Junge eines Tieros" (Tierjunge und Kinder hiiufig als ; ,rundlich, dicker 
Stopsel" u. dgl. benannt, ebenso aisl. hunn und:) ai. gi-gu- m. , ; Kind, 
Junges" (das damit oft verglichene gr. xlxvg, xixog „Kraft, Starke" s. aber 
u. *kdq- „springen“); 

gvd-trd- „gedeihlich, kraftig", n. ,, Kraft, Starkung" (grctntd — unsicherer 
Bed. — „ruhig?“ ist etymologisch daher nicht zu beurteilen; s. Waeker- 
nagel Ai. Gr. I 16). Von einer s-Erw. wahrscheinlicb gust- m. „Hohlung 
eines Rohrs", guhira- „hohl“; n. „H6hlung, ein Blasinstrument" (nacb Ublen- 
beck Ai. Wb. 338 wohl besser als susi-; Holthausen KZ. 47, 31 1 setzt gusi- 
= ags. hyse „Jungling“, vgl. zu solcher Bed. oben zu gdra-). 

Av. spa{y)~, redupl. Praes. Ptc. sispimna- „aufschwellen‘ (s. dazu Bar- 
tbolomae Airan. Wb. 1617); sura- (= ai. cura-) „stark, gewaltig", Sup. 
sdvista- (=ai. gdvistha-); sura- m. „Loch, lacuna", np. surux „Loch“ ( : xvao
```


## [2026-09-06T22:15:04.024Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=26200 && NR<=26440 && /^\\s*1[0-9]{3}\\s*$/ {print NR\": \"$0}' BRT.txt | tail -5; echo \"---formfeeds---\"; awk 'BEGIN{c=0} NR<=26437{if(/\\f/)c++} END{print \"pages before: \"c}' BRT.txt; echo \"--- any [pdf page ---\"; grep -c \"pdf page\" BRT.txt"
}
```


### [2026-09-06T22:15:05.583Z] TOOL RESULT

```
26277: 1577
26280: 1578
26306: 1579
26422: 1586
---formfeeds---
pages before: 863
--- any [pdf page ---
0
```


## [2026-09-06T22:15:05.794Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD sus ===\"; grep -n -i \"^sus\\|sus \\[\\|šuš\\|suš\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"suš\\|sus \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T22:15:05.857Z] TOOL RESULT

```
=== PHD sus ===
PHD.txt:572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
PHD.txt:1541:degree (of arc) suš.
PHD.txt:3903:suspend āgustan.
PHD.txt:3904:sustenance rozig.
PHD.txt:5030:sus
PHD_mackenzie.txt:4718:sust [swst l I = M, N -] slack, lazy.
PHD_mackenzie.txt:4856:susar [Iwsl = Av. xIu3ra-] liquid, fluid; semen.
PHD_mackenzie.txt:10882:susan                    ,to to      des, gel>
PHD_mackenzie.txt:10906:Susyans           -()~'t'O
=== NYB ===
2821:opastan ["wpst?n'] fallen, naughty: disan ~ rähdär (g. v.) 335. — Cf, as to the formation, MPrs 'spyxt*n ‘resplendent’, an epithet of Jesus (A-H II, BBB; it seems difficult to take this as a pl. in the sense of 'splendour', as does Henning).
3665:Sus [šws] Susa 11619. — OP Cusä, Elam. Susan, Bab. šu-ša-an; Arab al-Süs, v. Yāgūt 3,188—190.
4190:virrčyišn-var [wylwdšnw'1] pl. cas. obl. =--ān 110" applied to Jesus and Mani; meaning not clear. If -vdr is the well- known Milr and NP final element of compounds in the sense of 'resembling, like’ (cf šāh-vār), ~ could possibly be explained as a bahuvrihi: ‘having a semblance of faith, a sham faith', but I know of no other instance of -vàr being used in this pejorative sense.
4588:casus obliguus casus rectus causative
```


## [2026-09-06T22:15:14.913Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=26420 && NR<=26520 && /^\\s*1[0-9]{3}\\s*$/ {print NR\": \"$0}' BRT.txt | head"
}
```


## [2026-09-06T22:15:16.329Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 173 ===\"; sed -n '1,5p' HRN.txt >/dev/null; grep -n \"šuš\\|schusch\\|Lunge\" HRN.txt | head -20"
}
```


### [2026-09-06T22:15:17.239Z] TOOL RESULT

```
26422: 1586
```


### [2026-09-06T22:15:17.291Z] TOOL RESULT

```
=== HRN 173 ===
6814:784. snM 'Lunge'.
6816:aw. SKsi' *Lunge* (ZP61.); phlv. sus; ai. vergl.
```


## [2026-09-06T22:15:21.154Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6805,6830p' HRN.txt"
}
```


### [2026-09-06T22:15:21.206Z] TOOL RESULT

```
und No. 785, 795).
Das Verhältniss des Praes. sürem {*sörem (?); vergl.
auch Kä§.-Dial., jüd.-pers. Is. l, 1(5) zu söi/em ist
nicht klar^).
ses 'sechs'.
aw. /S2?flf^ *sechs': phlv. saä^ sasnm; Sii. sds; arm.
vec (H. No. 26(>).
kurd. LVV. ses; afy. spag; oss. d. t. äx^^äz (45);
wa;f. säl, säd, siyii. /aus etc.
784. snM 'Lunge'.
g. svs,
aw. SKsi' *Lunge* (ZP61.); phlv. sus; ai. vergl.
\/^gvas-, gvasiti ^schnaufen rvasand- *blasend, zischend,
schnaufend*, skr. cvkä?- 'Wind' 2).
afy. sayai; wa;^. LW. sifs, sar. sül.
785. seyäl 'Schakal'.
skr. g^gäld' (die Schreibung srgald- ist wohl falsch)
*) Eine Form äöä/, wie Vamb^ry ZDMG. 45, 414 druckt, giebt
es nicht und hat es nie gegeben. Allerdings wohl bisher auch noch
nicht eine derartige Behandlung eines persischen Textes wie sie die
Gedichte persischer Frauen hier erfahren. Der Autor bezeichnet sich
in seiner *Rei8e in Mittelasien' und in seinen 'Wanderungen und Er-
lebnissen in Persien' durchweg als einen genauen Kenner des Porsischen;
in dem letzterwähnten Buche, 8. 346 der deutschen Ausgabe, spricht or
von seiner 'eleganten persischen Sprache*. Der Leser des Aufsatzes in
der ZDMG. wird hiervon wenig spüren, wenn er nicht gar schon von
```


## [2026-09-06T22:15:26.313Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=6600 && NR<=6900 && /^\\s*1[0-9]{2}\\s*$/ {print NR\": \"$0}' HRN.txt | head -20; echo \"=== formfeed count ===\"; awk 'BEGIN{c=1} NR<=6814{if(/\\f/)c++} END{print c}' HRN.txt"
}
```


### [2026-09-06T22:15:28.176Z] TOOL RESULT

```
=== formfeed count ===
188
```


## [2026-09-06T22:15:33.329Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 186 187 188 189; do echo \"### file page $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HRN.txt | head -4; done"
}
```


### [2026-09-06T22:15:34.930Z] TOOL RESULT

```
### file page 186:
- 164 —
743. seg *Hund'; vergl. arab. sij[ihistan d. i. np. seglpistän
'Fructus Cordiae Myxae , Sebestenen , Brustbeere*
(AM. 155).
### file page 187:
- 165 -
747. Aeny 'Stein ; Gewicht, Würde', senrjin.
ap. ad^a(n)(jaina' steinern'; phlv. sa{n)(j (P.-V. z. B.
vd. 19 (13)), sang (AV.)
### file page 188:
- 16() -
Käs. Q. bdsüy, Causat. sujünüden, K. bisiij^ Z. bosot,
aw. l/'saoc-, saoöayähi 'anzünden', atare. |saofca- Teuer-
brand', saocant' 'brennend'; phlv. sö/tan, Praes. söcem
### file page 189:
— 167 —
755. Hözen 'Nadel'.
g. sejen ; Käs. Z. sö^ö,
aw. vergl. snlca- 'Nadel'; plilv. säcau (päz. süzan,
```


## [2026-09-06T22:15:40.499Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /784\\. snM/ {print \"RECORD \"NR; print substr($0,1,300)}' HRN.txt"
}
```


### [2026-09-06T22:15:42.092Z] TOOL RESULT

```
RECORD 195
— 173 —
södafj , n. sööay, sözay Vaschen, reinigen, baden-
(373).
Passt lautlich, aber nicht der Bedeutung nach zu
a\v. \/^xsaod' *fliessen', während das Umgekehrte für
ai. I ^förfA-, nimUiafi reinigen gilt. Hübschmann,
ZDM6. 44, 560 beanstandet daher die Zusammen-
stellung (doch vergl.
```


## [2026-09-06T22:15:47.028Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/BQT/BQT_v3_pages.txt && grep -n \"pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3 && wc -l incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T22:15:47.086Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2499427 Sep  4 14:06 incoming/BQT/BQT_v3_pages.txt
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
51425 incoming/BQT/BQT_v3_pages.txt
```


## [2026-09-06T22:15:50.653Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\n# find pages containing ۱۲۶۶ or 1266\nfor i in range(1,len(parts),2):\n    n=int(parts[i]); body=parts[i+1]\n    if '۱۲۶۶' in body or '1266' in body:\n        print('pdfpage',n, repr(body[:200]))\nEOF"
}
```


### [2026-09-06T22:15:52.522Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:15:55.021Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1266 --image 2>&1 | head -60"
}
```


### [2026-09-06T22:16:01.953Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1266.png
REF: BQT:1266  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 57  OCR-lang: fas

شستگانی -۱۷۹۹-
سازها بندد . ‎٩‏ - حلقهٌ زلف و حلقهٌ کیو شستّه - بروزن خفته . ممروف است ۴
و حلقةٌ رسن وکمند و امثال آنرا گوبند . که از شستن و پاکیزه کردن باشد - و بمعنی
۰ شت گاه زنان باشد - و با اول مکور رو پاك و دستارچه هم گفته‌اند و معرب آن
مختصر بشت باشد که در مقابل‌برخاست‌است 9. | شستجه (۱) است.
شتگانی ۲ - بکر اول و اسکون شن - بفتح اول وسکون آخ رکه‌نون
انی و فوقانی و کاف فارسی بالف کشیده و دون باشد وحر کت تانی مجپول . سدق را گویند
- و ۰ که کوش ماهی باشد - و نامیه رانیز گفته‌اند
بتحتانی رسیده » بمعنی بنیاد و پی عمارت باشد | ,.مء : رم
0 ۳ ۷ مطلقاً پمنی هرچیز که آن نمو کند و ببالد
وبعربی آساس خوانند ۴ ۰ :
شست‌ اون - نان ور ام و بیفزاید - وانی شکر را نیز میگوبند -
گرآن - بنتح‌کاف فارسی, ناییه و بمعنی خار تراجبین هم هست - و رحم را لیز
از تیراندازان و کمانداران باشد چه اشستگر کفته‌اند که بچه‌دان باشد ؛ و بجای حرف ثالی
کماندار را کونند .8 شین نقطه‌دار (؟) هم بنظر آمده است .
بیان باز دهم
درشن نققطه دار با شین نقطه دارمشتمل بر بست ونه لغت و کنات
شش < بح اول عددی است معروف ۵ بد دل وید آسرون ونامرد باشد.
- وضم اول چیزست مفید : شش اندار » بروزن پس انداز, کسی
بسرخی مایل مانند کوغت 1 راگوبند که غش بجول بازی میکرده باشدوآن
وبجگرمتصل‌است ‎٩‏ وبادزن ای نوعی از قمار است - و نرادرا نیز کفته‌اند (۴)
ومروحة دل باشد- وکنایه ۰ : 1 یعنی کسی که لرد بازی کند - و شخصی‌را پیز
از پستان‌لرم‌وستوآوبشته 8( 1 1 کفته‌اند که شش کوی الوان مدور از چوب پا
هم هست . ی ۵ غیر آن بهر دو دست بگیرد برهردستی سه عند
شش آماسیده  ‎٩۷‏ در هوا اندازد و میگیرد هر شش را چنانکه بر
جم اول » کنایه از مردم شش زمین نمی‌افتد وپیوسته چهار عدد آن درهواست
() چش : شتجة(۱) . (+) چك : - قطه دار . 6 چك: کوبند.
۱-ر4: شتن (ح) . ۴ - از غست (نشت) ۳ کانی (پیوند نبت) .
۴ - زقلب درکه اوساز شتگانی همر که قلب کعبه‌بود شستگانی محراب .
« ابوالفرج رولی ۲*۰ .
۴ -اسم مفعول از «شستن»(جم اول,وئیز وبفتح آن بمعنی لشته) .8 -وآن‌شماراست
بي‌پنج وهفت,دوبرابر سه؛ اوستا- 2511۷2510 (شغش) . پهلوی 50380 * هندی‌باستان 5083 »
ارمنی ۷۵۶ کردی ع 586810 ؛ افغانی «ل552082 . استی 33832 .وخی لقْطه «طلقطه
بقیه در صفحةٌ ۱۲۹۷
```


## [2026-09-06T22:16:24.482Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1266 --image --pdf-page 27 2>&1 | head -50"
}
```


### [2026-09-06T22:16:26.560Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1266.png
REF: BQT:1266  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 57  OCR-lang: fas

شستگانی -۱۷۹۹-
سازها بندد . ‎٩‏ - حلقهٌ زلف و حلقهٌ کیو شستّه - بروزن خفته . ممروف است ۴
و حلقةٌ رسن وکمند و امثال آنرا گوبند . که از شستن و پاکیزه کردن باشد - و بمعنی
۰ شت گاه زنان باشد - و با اول مکور رو پاك و دستارچه هم گفته‌اند و معرب آن
مختصر بشت باشد که در مقابل‌برخاست‌است 9. | شستجه (۱) است.
شتگانی ۲ - بکر اول و اسکون شن - بفتح اول وسکون آخ رکه‌نون
انی و فوقانی و کاف فارسی بالف کشیده و دون باشد وحر کت تانی مجپول . سدق را گویند
- و ۰ که کوش ماهی باشد - و نامیه رانیز گفته‌اند
بتحتانی رسیده » بمعنی بنیاد و پی عمارت باشد | ,.مء : رم
0 ۳ ۷ مطلقاً پمنی هرچیز که آن نمو کند و ببالد
وبعربی آساس خوانند ۴ ۰ :
شست‌ اون - نان ور ام و بیفزاید - وانی شکر را نیز میگوبند -
گرآن - بنتح‌کاف فارسی, ناییه و بمعنی خار تراجبین هم هست - و رحم را لیز
از تیراندازان و کمانداران باشد چه اشستگر کفته‌اند که بچه‌دان باشد ؛ و بجای حرف ثالی
کماندار را کونند .8 شین نقطه‌دار (؟) هم بنظر آمده است .
بیان باز دهم
درشن نققطه دار با شین نقطه دارمشتمل بر بست ونه لغت و کنات
شش < بح اول عددی است معروف ۵ بد دل وید آسرون ونامرد باشد.
- وضم اول چیزست مفید : شش اندار » بروزن پس انداز, کسی
بسرخی مایل مانند کوغت 1 راگوبند که غش بجول بازی میکرده باشدوآن
وبجگرمتصل‌است ‎٩‏ وبادزن ای نوعی از قمار است - و نرادرا نیز کفته‌اند (۴)
ومروحة دل باشد- وکنایه ۰ : 1 یعنی کسی که لرد بازی کند - و شخصی‌را پیز
از پستان‌لرم‌وستوآوبشته 8( 1 1 کفته‌اند که شش کوی الوان مدور از چوب پا
هم هست . ی ۵ غیر آن بهر دو دست بگیرد برهردستی سه عند
شش آماسیده  ‎٩۷‏ در هوا اندازد و میگیرد هر شش را چنانکه بر
جم اول » کنایه از مردم شش زمین نمی‌افتد وپیوسته چهار عدد آن درهواست
() چش : شتجة(۱) . (+) چك : - قطه دار . 6 چك: کوبند.
۱-ر4: شتن (ح) . ۴ - از غست (نشت) ۳ کانی (پیوند نبت) .
۴ - زقلب درکه اوساز شتگانی همر که قلب کعبه‌بود شستگانی محراب .
« ابوالفرج رولی ۲*۰ .
۴ -اسم مفعول از «شستن»(جم اول,وئیز وبفتح آن بمعنی لشته) .8 -وآن‌شماراست
بي‌پنج وهفت,دوبرابر سه؛ اوستا- 2511۷2510 (شغش) . پهلوی 50380 * هندی‌باستان 5083 »
ارمنی ۷۵۶ کردی ع 586810 ؛ افغانی «ل552082 . استی 33832 .وخی لقْطه «طلقطه
بقیه در صفحةٌ ۱۲۹۷
```


## [2026-09-06T22:16:28.746Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n '1,80p' tools/ref_page.py"
}
```


### [2026-09-06T22:16:28.790Z] TOOL RESULT

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
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-06T22:16:44.669Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 -c \"\nimport subprocess\nsubprocess.run(['pdftoppm','-f','27','-l','27','-r','200','-png','-singlefile','data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf','/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt27'])\n\" && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:16:46.812Z] TOOL RESULT

```
total 117664
drwx------ 3 sfmqrb sfmqrb     4096 Sep  6 18:16 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      748 Sep  6 18:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90831 Sep  6 18:04 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
```


## [2026-09-06T22:16:50.832Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt27.png"
}
```


### [2026-09-06T22:16:50.858Z] TOOL RESULT

```

```


## [2026-09-06T22:16:57.834Z] TOOL CALL #28: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1266.png"
}
```


### [2026-09-06T22:16:58.308Z] TOOL RESULT

```

```


## [2026-09-06T22:16:58.306Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T22:17:13.817Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1267 --image 2>&1 | head -8"
}
```


### [2026-09-06T22:17:20.264Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1267.png
REF: BQT:1267  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 58  OCR-lang: fas

-۱۹۷- شش خانون
- وماه شب چهارده را نیز میگوبند(۱) ‎٩‏ . عدقه بردرختها پیچد و آلرا بمیرازی سیاه دارو "
ششی بافو ۴ -کنایه ازشی کوک | دبتریی گردة سود خواند.
است که آن زحل و «شتری و مریخ و زهره شش تا - با فوقانی‌بالف کشیده «طنیور
و عطارد و قمر باشد. شش‌تار راکونند چنانکه سه تا طنبوره سه تاره
```


## [2026-09-06T22:17:24.651Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1267.png')\nw,h=im.size\nprint(w,h)\nim.crop((0,int(h*0.72),w,h)).save('bqt1267_foot_p294.png')\n\""
}
```


### [2026-09-06T22:17:26.619Z] TOOL RESULT

```
1650 2546
```


## [2026-09-06T22:17:29.054Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1267_foot_p294.png"
}
```


### [2026-09-06T22:17:29.081Z] TOOL RESULT

```

```


## [2026-09-06T22:18:08.383Z] TOOL CALL #32: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BQT && cat > data/verification/sources/refs/ocr/BQT/1266.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1266 (running head شستگانی; vol. 3 pdf p. 57).\nRead from the page image by a vision model, 2026-09-06.]\n\nبیان یازدهم\nدر شین نقطه‌دار با شین نقطه‌دار مشتمل بر بیست و نه لغت و کنایت\n\nشش ● بفتح اول عددی است معروف ۵ ـ وضم اول چیزیست سفید بسرخی مایل مانند\nگوشت وبجگر متصل است ۶ وبادزن ومروحهٔ دل باشد ـ وکنایه از پستان نرم وسست\nوآویخته هم هست .        [a woodcut of a pair of lungs, captioned شش]\n\nشش آماسیده ـ بضم اول ، کنایه از مردم بددل وبدد اندرون ونامرد باشد .\n\nشش انداز ـ بروزن پس انداز، کسی را گویند که شش بجول بازی میکرده باشد …\n\n--- footnotes (bottom of p. 1266) ---\n(۱) چنی : شنجة(۱) .   (۲) چك : ـ نقطه دار .   (۳) چك: گویند.\n۱ ـ رك: شستن (ح) .   ۲ ـ از: شت (نشت) + گانی (پیوند نبت) .\n۳ ـ ز قلب درکه اوساز شستگانی عمر / که قلب کعبه‌بود شستگانی محراب . «ابوالفرج رونی ۲۰» .\n۴ ـ اسم مفعول از «شستن»(بضم اول، ونیز وبفتح آن بمعنی نشسته) .\n● ـ وآن شمار است بین پنج وهفت، دو برابر سه؛ اوستا xshvash (خشوش) ، پهلوی shash ،\nهندی‌باستان shásh ، ارمنی veç ، کردی shesh ، افغانی shpazh ، استی äxsäz ، وخی shâdh, shâl\nبقیه در صفحهٔ ۱۲۶۷\nEOF\ncat > data/verification/sources/refs/ocr/BQT/1267.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1267 (running head شش خانون; vol. 3 pdf p. 58).\nBottom-of-page footnote block, read from the page image by a vision model, 2026-09-06.\nThis is footnote 6 continued from p. 1266 — Mo'in's etymology of شش «lung».]\n\n۶ ـ اوستا sushi ، افغانی xâush «استق ۷۸۳» ، گیلکی shish ، تهرانی shish .\nسانسکریت çvas (دمیدن) «هوبشمان ۷۸۴» ، پهلوی sush ، افغانی saghai ، وخی shush ،\nسریکلی sül «استق ۷۸۴» ، بعربی آنرا ریه (رئه) گویند .\n\n* شستن ـ بفتح اول وسوم ، مخفف «نشستن» (ه.م.) ورك: شت .\n* شستن ـ بضم اول وفتح سوم ، پهلوی shustan ، کردی ع shushtin (تطهیر) ،\nبلوچی shôzag, shôdhagh, shôdag (تطهیر ، پاك كردن ، استحمام كردن) «استق ۷۸۲» .\nبقول Fr. Müller از سانسکریت kshud (زدن ، پایمال كردن). اما درفارسی بمعنی تطهیر،\nپاك كردن (بوسیلهٔ آب) آمده ، قس: پازند shustan (تطهیر ، پاك كردن) «هوبشمان ۷۸۲» ،\nدزفولی shoshtan «امام» ، گیلکی shostan ، اورامانی shot (شت) «ك. اورامان ۱۲۶» .\nEOF\necho saved; ls data/verification/sources/refs/ocr/BQT/ | grep 126"
}
```


### [2026-09-06T22:18:10.143Z] TOOL RESULT

```
saved
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
```


## [2026-09-06T22:18:14.427Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 784 area / schusch ===\"; grep -n \"Lunge\" HUB.txt | head; echo \"=== MON شش ===\"; grep -n \"شش \\[\\|(شش)\\|شش:\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T22:18:14.494Z] TOOL RESULT

```
=== HUB 784 area / schusch ===
2801:sa^ai 'Lunge' zu skr. gvas gehort, kann es nicht auch
=== MON شش ===
MON_part2.txt:23504:کشش: ۵ ۱:۱۵ (امعص.) جذب؛ جلب» 
MON_part2.txt:23509:کشش: ۰۰8-۰ (امص.) کشتن؛ فتل. کشش 
MON_part2.txt:23510:با بخشش: در بعضی نواحی ایران (از جمله 
MON_part2.txt:28028:کوشش: ۲:۹ (اسص.) سعی؛ جهد. 
MON_part2.txt:28029:جنگ و جدال. کوشش و کشش: سعی و 
MON_part2.txt:28030:جذبه (از طرفین)؛ قس. کوشش و کشش: 
MON_part2.txt:45915:مترشش: ۱00۵۵ [ع.] (افا.) چکنده؛ 
MON_part2.txt:58553:ود و ماقلف شون کرد تماشش: هلو 
MON_part2.txt:73786:بینی. نای شش: قصبة الریه. نای گلو: حلقوم» 
MON_part1.txt:1579:اب‌شش: 20-304 (امر.) (جاد.) دستگاه
```


## [2026-09-06T22:18:15.638Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN cyst ===\"; grep -n -i \"cyst\\b\\|kystis\\|κύστις\" KLN_1966.txt | head -10; echo \"=== KLN quarrel ===\"; grep -n -i \"^quarrel\\|quarrel, n\\|queri, to complain\\|queror\" KLN_1966.txt | head -10"
}
```


### [2026-09-06T22:18:15.709Z] TOOL RESULT

```
=== KLN cyst ===
7502:cholecyst,  n.,  the  gall  bladder  (anal.)  —  Medical L.  cholecvstis,  incorrect  formation  fr.  Gk.  yo/:r„ 'gall,  bile",  and  xvctic,  ’bladder,  bag,  pouch’. See  choler  and  cyst.
7503:cholecyst-,  form  of  cholecysto-  before  a  vowel, cholecystitis,  n.,  inflammation  of  the  gall  bladder. —  Medical  L.,  formed  fr.  cholecyslis  (see  prec. word)  with  suff.  -itis.
7504:cholecysto-,  before  a  vowel  cholecyst-,  combining form  denoting  the  gait  bladder.  —  See  prec. word.
8012:hunig,  ‘honey’.  See  honey, cnida,  n.,  a  nematocyst  (zool)  —  ModL.,  fr.  Gk. xviSr;,  ‘nettle’,  from  the  stem  of  xvi^eiv,  ‘to scratch,  scrape’,  rel.  to  Homeric  Gk.  xviov), Att.  xviaoc,  ‘smell  of  a  burnt  sacrifice,  steam, savor’,  and  cogn.  with  L.  nidor  (for  *cnidos), ‘smell  of  burnt  things,  savor’.  See  nidor. co-  short  form  of  com-,  con-, coacervate,  tr.  v.,  to  heap  up  (obsol.)  —  L.  co- acervatus,  pp.  of  coacervdre,  ‘to  heap  together, heap  up’,  fr.  co-  and  acervare,  ‘to  heap  up’.  See acervate.
10031:cutis,  n.,  the  skin  beneath  the  epidermis,  the derma  (anat.)  —  L.  cutis,  ‘skin’,  lit.  ‘that  which covers’,  fr.  I.-E.  base  *(s)qeut-,  ‘to  cover’, whence  also  OE.  hyd,  ‘skin’.  See  hide,  ‘skin’,  and cp.  cutaneous,  cuticle.  Cp.  also  cyst,  -cyte,  ecu, escutcheon,  esquire,  scudo,  scum,  Scutellaria, scutellum,  scuttle,  ‘receptacle’,  scutum,  syncy¬ tium,  zuchetto.  Base  *(s)qeut-  is  rel.  to  base *(s)qeudh-,  ‘to  cover’;  see  custody.
10095:cyst
10133:cyst,  n.,  a  closed  membranous  pouch  or  sac  con¬ taining  fluid  (med.)  —  Medical  L.  cystis,  fr.  Gk. xua-rip,  ‘bladder,  bag, pouch’,  which  is  prob.cogn.
10134:cyst-
10135:with  Of.  svdsati,  svdsiti,  ‘blows,  breathes,  sighs'. L.  queri,  ‘to  complain’.  See  quarrel,  ‘dispute’, cyst-,  form  of  cysto-  before  a  vowel.
10136:-cyst,  combining  form  meaning  ‘pouch,  sac’,  as in  cholecyst.  - —  Fr.  Gk.  xiitro?,  ‘bladder,  bag, pouch’.  See  prec.  word, cysti-,  combining  form.  —  See  cysto-. cystic,  adj.,  pertaining  to  a  cyst;  esp.,  pertaining to  the  urinary  bladder.  —  F.  cystique,  fr.  Medi¬ cal  L.  cysticus ,  fr.  cystis.  See  cyst  and  -ic. cysticercus,  n.,  the  larval  form  of  tapeworms C zool .)  —  ModL.,  compounded  of  cysti-  and Gk.  x£pxo4,  ‘tail’.  See  cercus  and  cp.  words there  referred  to.
=== KLN quarrel ===
8795:Derivatives:  conquer-able,  adj.,  conquerable¬ ness,  n.,  conquer-ing,  adj.,  conquer-ing-ly,  adv., conqueror  (q.v.)
8796:conqueror,  n.  —  ME.  conquereour,  fr.  OF.  con- quereor,  fr.  conquerre,  ‘to  conquer’.  See  prec. word  and  agential  suff.  -or. conquest,  n.  —  ME.,  partly  fr.  OF.  conquest  (F. conquet),  ‘acquisition’,  partly  fr.  OF.  conqueste (F.  conquete),  ‘acquisition,  conquest’.  These words  prop,  are  the  masc.,  resp.  fem.  pp.  of  OF. conquerre,  and  derive  fr.  VL.  *conquaesitus, resp.  *conquaesita  (corresponding  to  L.  con- quisitus,  conquisita),  pp.  of  *conquaerere.  See conquer  and  cp.  conquistador, conquian,  n.,  a  card  game  with  two  players.  — Fr.  Sp.  icon  quienl,  ‘with  whom?’  Sp.  con  derives fr.  L.  cum,  ‘with’ ;  see  i  st  con-.  Sp.  quien  comes  fr. L.  quern,  acc.  of  quis,  ‘who’ ;  see  who.  Cp.  cooncan. conquistador,  n.,  a  conqueror,  applied  esp.  to  the Spanish  conquerors  of  Mexico  and  Peru.  —  Sp., fr.  conquistar,  ‘to  conquer’,  fr.  VL.  conquistdre, fr.  L.  conquisitus,  pp.  of  conquirere,  ‘to  seek  for’ ; see  conquer.  L.  conquisitus  stands  for  *con- quaesitus.  For  the  change  of  Latin  ae  (in  quae- situs)  to  f  (in  con-quisitus)  see  acquire  and  cp. words  there  referred  to.
12036:domesday,  n.  —  Ancient  form  of  doomsday. Domesday  (Book),  the  record  of  the  Great  In¬ quest  of  the  lands  of  England  made  by  the  order of  William  the  Conqueror  in  1086.  —  OE. ddmesdxg,  lit.  ‘day  of  judgment’.  See  doomsday, domestic,  adj.  —  F.  domestique,  fr.  L.  domesticus, ‘pertaining  to  the  house,  private’,  fr.  domus, ‘house,  home’;  see  dome,  ‘building’.  The  form domesticus  is  enlarged  fr.  *domestis ,  which  was formed  on  analogy  of  agrestis,  ‘pertaining  to land’  (fr.  ager,  ‘land’).
31329:quarrel,  intr.  v.,  to  engage  in  a  quarrel.  - —  Partly fr.  OF.  quereler  (F.  quereller),  partly  fr.  prec. word.
31330:quarrel,  n.,  1)  arrow  or  bolt,  formerly  used  with  a crossbow;  2)  small  diamond-shaped  pane  of glass.  —  ME.,  fr.  OF.  quarel,  quarrel  (F.  car- reau),  fr.  ML.  quadrellus,  dimin.  of  quadras, ‘square’.  See  quadrate,  adj.,  and  -el. quarry,  n.,  anything  hunted,  prey.  —  ME.  querre, quirre,  fr.  OF.  cuiree  (F.  curee),  ‘the  spoil,  quar¬ ry’,  fr.  cuir,  ‘hide,  skin’,  fr.  L.  corium.  The  orig¬ inal  meaning  of  quarry  was  ‘parts  of  a  slain animal  placed  on  its  hide  as  the  hound’s  reward’. See  corium  and  cp.  cortex,  cuirass, quarry,  n.,  quarrel.  —  A  later  var.  of  3rd quarrel.
```


## [2026-09-06T22:18:24.359Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN quarrel dispute ===\"; sed -n '31320,31332p' KLN_1966.txt | grep -o \"quarrel,  n.,  a  dispute.\\{0,700\\}\"; echo; grep -n \"querulous\" KLN_1966.txt | head -3"
}
```


## [2026-09-06T22:18:24.946Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ctx ===\"; sed -n '2790,2812p' HUB.txt"
}
```


### [2026-09-06T22:18:26.074Z] TOOL RESULT

```
=== KLN quarrel dispute ===

31378:querimonious,  adj.,  querulous.  —  ML.  querimd- niosus,  fr.  L-  querimdnia,  ‘complaint’,  fr.  queri, ‘to  complain’;  see  quarrel,  ‘dispute’.  For  the  L. suff.  -monia  see  -mony  and  cp.  words  there  re¬ ferred  to,  for  the  ending  see  suff.  -ous. Derivatives:  querimonious-ly,  adv.,  querimo- nious-ness,  n.
31381:querulous,  adj.,  fretful.  —  ML.  queruldsus,  fr.  L. querulus,  ‘complaining’,  fr.  queri,  ‘to  complain’. See  quarrel,  ‘dispute’,  and  -ous.
31382:Derivatives:  querulous-ly,  adv.,  querutous-ness, n.
```


### [2026-09-06T22:18:26.114Z] TOOL RESULT

```
=== HUB ctx ===
Das arm. LW. stap kann nur auf ein phi. §tap, istap
oder ustap zuriickgehen. Der von Horn angefiihrte
pehl. Infinitiv kann ostaftan oder ttstaftan gelesen
werden, da anlaut. D und u gleich geschrieben werden.
782. Nach F r. M ii 1 1 e r , WZKM. 8, 96 zu skr. ksud 'schlagen,
stampfen*. Aber die Bedeutung von np. Sustan ist
'waschen = reinigen', pOkTza kardan, vgl. paz. sus-
tan Vaschen, reinigen , bal. SOday Vaschen, reinigen,
baden etc.— 80 -
784. Np. SuS Xunge' aus suS mit Assimilation des Anlautes
an den Auslaut. Wenn sus = zd. 8U§i- = afgh.
sa^ai 'Lunge' zu skr. gvas gehort, kann es nicht auch
zu (dem unsichern) ^uksi- gehSren.
785. Np. Saydl ist Lehnwort aus dem Indischen, wie auch
Andreas annimmt, der bemerkt, dass tOra das echt
persische Wort fiir 'Schakal' ist (vgl. Horn Nr. 403).
Fiir skr. grgOla- miisste man np. ^sirydl erwarten.
Dazu afgh. daydl^) und als pers. LW. saycH *Schakar.
786. Dazu afgh. LW. skOr 'hunting, chase, prey', kurd. LW.
sigar 'Wild' ZDMG. 38, 75 = np. Sikdr; afgh. sikrai
'a hawk, falcon' = np. sikara, sakara 'Jagdhabicht'.
Vgl. arm. sakr u. s. w. ZDMG. 46, 266. Np. sikar
nicht = *aiwisk^ra^ sondern == "^skCl/ra^ von einer
```


## [2026-09-06T22:18:32.413Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"quarrel\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T22:18:32.458Z] TOOL RESULT

```
1301:aeariatre,  adj.,  bad-tempered.  —  F.,  ‘contrary, crabbed,  quarrelsome’,  orig.  meaning  ‘possess¬ ed  by  a  demon’,  formed  with  pejorative  suff. -atre,  from  the  name  of  Acharius,  bishop  of Noyon  in  the  7th  cent.,  renowned  for  curing folly.  The  suff.  -atre  derives  fr.  OF.  -astre,  fr.  L. -aster;  see  -aster.
1944:Derivatives:  aggregat-ion ,  n.,  aggregat-ive,  adj., aggregat-or,  n.,  aggregat-ory,  adv. aggregate,  adj.,  gathered  into  a  mass.  —  L.  aggre¬ gates,  pp.  of  aggregare.  See  aggregate,  v. Derivatives:  aggregate ,  n.,  a  collective  mass; sum  total,  aggregate-ly,  adv.,  aggregate-ness,  n. aggress,  intr.  v.,  to  start  a  quarrel.  —  F.  agresser, fr.  Late  L.  aggressare ,  freq.  of  L.  aggredi  (pp.  ag¬ gress  us),  ‘to  go  to,  approach,  attack’,  fr.  ad- and  gradi  (pp.  gressus),  ‘to  step,  go’,  fr.  gradus, ‘step’.  See  grade.  For  the  change  of  Latin  a  (in gradi )  to  e  (in  ad-gressus,  ag-gressus)  see  accent and  cp.  words  there  referred  to.  For  the  form of  gressus ,  pp.  of  gradi ,  see  congress.
2249:allege,  tr.  v.  —  ME.  aleggen,  ‘to  bring  forward  as evidence’,  fr.  AF  alegier,  which  is  formed— with  change  of  prefix— fr.  OF.  esligier,  ‘to  free, disengage,  buy,  pay,  possess’,  fr.  VL.  *ex!iti- gdre,  ‘to  free  from  a  lawsuit’,  fr.  1st  ex-  and litigare,  ‘to  sue,  quarrel’.  See  litigate. Derivatives:  alleg-ed-ly,  adv.,  alleg-er,  n. allegiance,  n.  —  ME.  alegeance,  formed  fr.  a  (fr. L.  ad),  ‘to’,  and  OF.  ligeaunce,  ligeance,  fr.  lige. See  ad-,  liege  and  -ance  and  cp.  ligeance. allegorize,  tr.  and  intr.  v.  —  F.  allegoriser,  fr.  L. allegorizdre,  fr.  allegoria.  See  next  word  and -ize.
2350:the  sense  of  the  compar.  suff.  -ter — denotes  ‘the other  of  two’,  the  latter  means  ‘another  picked out  of  many  (at  least  three)  persons’.  See  alias, else  and  cp.  altercate,  altem,  alternate,  adulter¬ ate,  adultery,  altruism.  For  the  compar.  suff.  -ter see  -ther  and  cp.  words  there  referred  to. Derivatives:  alter-able,  adj.  alter-abil-ity,  n., alter-ation,  n.,  alter-at-ive,  adj. altercate,  intr.  v.,  to  dispute,  quarrel.  —  L.  al- tercatus  pp.  of  altercari,  to  dispute,  wrangle, quarrel’,  fr.  *altercus,  ‘disputing’,  fr.  alter,  ‘an¬ other’.  See  prec.  word  and  verbal  suff.  -ate. altercation,  n.,  dispute,  quarrel.  —  F.,  fr.  L. altercationem,  acc.  of  altercatio,  ‘a  dispute, wrangling’,  fr.  altercatus,  pp.  of  allercdri.  See altercate  and  -ion.
4478:barracks,  n.  pi.,  soldiers’  lodgings.  —  F.  baroque, fr.  Sp.  barraca,  orig.  ‘hut  of  bricks’,  a  derivative of  barro ,  ‘clay’,  which  is  prob.  of  Iberian  origin, barracuda,  also  barracouta,  n.,  a  large  sea  fish.  — Sp.  barracuda,  of  uncertain  origin, barrage,  n.,  dam.  —  F.,  fr.  barrer,  ‘to  bar,  ob¬ struct’.  See  bar,  v.,  and  -age. barrage,  n.,  curtain  fire  (mil.)  —  Fr.  F.  tir  de barrage,  'curtain  fire’.  See  prec.  word, barranca,  n.,  ravine.  —  Sp.,  fr.  barranco,  ‘pre¬ cipice,  ravine’,  fr.  VL.  barrancus,  fr.  Gk.  (papay!;, gen.  papayy oc,,  ‘deep  chasm,  ravine,  gully’, which  is  rel.  to  cpdcpuyt;,  ‘throat,  chasm,  gulf’, (papciv,  ‘to  cleave,  part’,  and  cogn.  with  L. fordre,  ‘to  bore’,  OH.  horian,  ‘to  bore’.  See  bore ‘to  pierce',  and  cp.  pharynx, barrandite,  n.,  a  hydrous  phosphate  of  iron  and aluminum  (mineral.)  —  F.,  named  after  the French  geologist  Joachim  Barrande  (1799- 1883). For  the  ending  see  subst.  suff.  -ite. barrator,  n.,  one  guilty  of  barratry.  —  ME.  bara- tour,  ‘a  quarrelsome  person’,  fr.  OF.  barateor, ‘deceiver,  swindler’,  fr.  barater,  ‘to  deceive, barter’.  See  barter.
4874:bewray,  tr.  v.,  to  reveal,  divulge  ( archaic )  — ME.  bewreien,  bewreyen,  ‘to  reveal’,  fr.  be-  and OE.  wregan,  ‘to  accuse’,  which  is  rel.  to  OS. wrogian,  OFris.  wrogia,  OHG.  ruogen,  MHG. riiegen,  ‘to  accuse’,  G.  riigen,  ‘to  censure’,  Goth, wrohjan,  ‘to  accuse’,  ON.  rcegja,  ‘to  slander,  de¬ fame’,  Du.  wroegen,  ‘to  prick’  (said  of  con¬ science),  OE.,  OS.  wrdht,  OFris.  wrogie,  MHG. ruoge,  riiege,  Goth,  wrohs,  ‘accusation’,  G.  Riige, ‘censure’,  ON.  rog,  ‘quarrel,  slander’, bey,  n.,  1)  governor  of  a  district  in  Turkey;  2)  a Turkish  title  of  honor.  —  Osmanli  equivalent of  Turk.  beg.  Cp.  beg,  ‘bey’,  begum, beylic,  beylik,  n.  —  Turk.,  formed  fr.  bey  and -lik,  a  suff.  expressing  quality.  Cp.  pashalik. beyond,  adv.  and  prep.  —  ME.  biyeonde,  biyonde, fr.  OE.  begeondan,  ‘beyond’,  fr.  be-  and  geond, ‘yond,  yonder’.  See  yon,  yond,  yonder. Derivative:  beyond,  n.
4939:bicker,  intr.  v.,  to  squabble,  quarrel.  —  ME.  bi- keren,  of  uncertain  origin;  possibly  formed  with suff,  -er  fr.  base  *bik-,  a  collateral  form  of  *pik-, whence  the  verb  pick, bicker,  n.  —  Scot,  form  of  beaker, bicuspid,  adj.,  having  two  points.  —  Formed  fr. bi-  and  L.  cuspis,  gen.  cuspidis,  ‘point’.  See  cusp and  cp.  tricuspid.
5565:fr.  bravo,  ‘courageous,  brave’,  with  suff.  -lira. See  brave,  adj.,  and  -ure. brawl,  intr.  v.  —  ME.  braulen,  ‘to  scold,  quarrel’, fr.  braule,  ‘scold,  quarrel’,  rel.  to  Du.  and  LG. brallen,  ‘to  brag’.
7386:chicane,  n.,  chicanery.  —  F.,  ‘quibble,  evasion’, fr.  chicaner.  See  chicane,  v. chicane,  intr.  v.,  to  trick.  —  F.  chicaner,  ‘to quibble,  wrangle,  quarrel’,  of  uncertain  origin; prob.  not  related  to  MHG.  schicken,  ‘to  arran¬ ge,  set  in  order’  (see  chic).
10135:with  Of.  svdsati,  svdsiti,  ‘blows,  breathes,  sighs'. L.  queri,  ‘to  complain’.  See  quarrel,  ‘dispute’, cyst-,  form  of  cysto-  before  a  vowel.
14639:feud,  n.,  enmity.  —  ME.  fede,  feide,  fr.  OF.  fede, fr.  OHG .  fehida  (MHG.  vede,  G.  Fehde),  ‘con¬ tention,  quarrel,  feud’,  which  is  rel.  to  OE. fShd(o),  ‘feud,  enmity’,  MDu.  vede,  vote,  (Du. vete),  of  s.m.,  OE.  fah,  ‘hostile’.  See  foe. Derivative:  feud-al,  adj.
14943:flite,  flyte,  intr.  v„  to  quarrel;  tr.  v„  to  quarrel with,  to  scold.  —  ME.  fliten,  fr.  OE.  flitan,  ‘to contend,  struggle,  quarrel’,  rel.  to  OHG.  flisan, ‘to  strive’,  OHG.,  MHG./fe,  ‘contest,  diligence', G.  Fleifi,  Du.  vlijt,  ‘diligence,  industry’, fliting,  flyting,  n.,  1)  a  scolding;  2)  an  abusive speech.  —  ME.  fliting.  See  prec.  word  and  -ing, suff.  forming  verbal  nouns, flitter,  intr.  v.,  to  flutter.  —  Freq.  of  flit.  Cp. flutter.
15214:forsake,  tr.  v.  —  ME.  forsaken,  ‘to  forsake’,  fr. OE.  forsacan,  ‘to  oppose,  refuse’,  fr.  for-  and OE.  sacan,  ‘to  contend,  dispute’,  fr.  sacu,  ‘dis¬ pute,  quarrel’.  See  sake.
15279:fount,  n.,  the  British  equivalent  of  font.  —  F. fonte.  See  font,  ‘set  of  type  of  one  size’, fountain,  n.  —  OF.  (=  F.)  fontaine,  fr.  Late  L. fontana,  prop.  fern,  of  fontanus,  ‘pertaining  to a  spring’,  used  as  a  noun,  fr.  L  .fons,  gen  .fontis, ‘spring’.  See  font,  ‘receptacle’,  and  cp.  fontanel, four,  adj.  and  n.  —  ME.  feower,  fower,  foure, four,  fr.  OE.  feower,  rel.  to  OS.  fiuwar,  fiwar, OFris.  fiuwer,fidr,  Du.  vier,  OHG.  for,  MHG., G.  vier,  ON.  fjorir,  Dan  .fire,  Swed  .fyra,  Norw. fire,  Goth,  fidwor,  ‘four’,  and  cogn.  with  OI.  cat- vArah,  Avestic  cad  ward,  Pers.  catvdr,  Toch.  A stwar,  B  stwer,  Arm.  cork',  Gk.  -r6<j<rape<;,  Att. -nhrrapes,  Ion.  -reaaepes,  Aeol.  rrfcrjpet;,  toctu- pep,  L.  quattuor,  Oscan  petora,  Umbr.  petur-, OSlav.  cetyre,  Lith.  keturi,  OIr.  cethir,  W.  pet- guar,  pedwar,  ‘four’.  (Alb.  katsr  is  a  loan  word fr.  L.  quattuor.)  All  these  words  derive  fr.  I.-E. base  *quetwAr-,  ‘four’.  Cp.  fardel,  ‘fourth  part’, farthing,  firkin,  forty.  Cp.  also  cadre,  cahier, carfax,  carillon,  cater,  ‘four  at  cards  or  dice’, charpoy,  quadrant,  quadrate,  quadri-,  quadrille, quadroon,  quarantine,  quarrel,  ‘arrow,  bolt’, quarry,  ‘a  place  for  excavating  stones’,  quart, quatrain,  quaternion,  quire  of  paper,  squad, square,  tessara-,  tetarto-,  tetra-,  tetrakis-,  te- trarch,  trapezium,  trocar, fourchee,  fourche,  adj.,  forked,  divided  (her.)  —
17260:harry,  tr.  v.,  1)  to  ravage;  2)  to  harass.  —  ME. harien,  herien,  fr.  OE.  hergian,  ‘to  ravage,  lay waste’,  rel.  to  ON.  herja,  ‘to  make  a  raid,  to plunder’,  OHG.  herion,  MHG.  hern,  ‘to  ravage, plunder’,  OHG.  firherion,  MHG.  verhern,  ‘to destroy  by  war’,  G.  verheeren,  ‘to  destroy’. These  words  lit.  mean  ‘to  afflict  with,  or  destroy by,  an  army’,  being  denominated  fr.  OE.  here, resp.  ON.  herr  (whence  Dan.  hser,  Swed.  har), OHG.  hari,  heri,  MHG.  her,  G.  Heer,  ‘host, army’,  which  are  rel.  to  OS.,  OFris.  heri,  Du. heir,  Goth,  harjis,  of  s.m.  These  latter  words orig.  meant  ‘that  which  pertains  to  war’,  and are  cogn.  with  Lith.  karas,  ‘war,  quarrel’,  kare, ‘war’,  karias,  ‘host,  army’,  OPruss.  karjis, ‘army’,  OSlav.  kara,  ‘strife’,  Mir.  cuire,  ‘troop’, OPers.  kara,  ‘host,  army’,  Gk.  xoipavo?,  ‘ruler, leader,  commander’  (prop,  ‘leader  of  an  army’, fr.  *xoipa,  for  *xopta,  ‘army’).  Cp.  prec.  word. Cp.  also  the  first  element  in  arriere-ban,  har¬ binger,  harbor,  harness,  Harold,  herald,  Herbert, heretoga,  heriot,  Herman,  hership,  and  the second  element  in  Lothario,  Oliver,  Walter. Harry,  masc.  PN.  —  F.  Henri.  See  Henry, harsh,  adj.  —  ME.  harsk,  of  Scand.  origin.  Cp. Dan.,  Norw.,  harsk,  Swed.  harsk,  ‘rancid’, which  are  rel.  to  MLG.,  G.  harsch,  ‘harsh, rough,  raw’;  fr.  I.-E.  base  *qars-,  ‘to  scrape, scratch,  rub",  whence  Lith.  karsiu,  karsti,  ‘to comb’,  OSlav.  krasta  (for  *korsta),  Russ. kordsta,  ‘itch’,  MLG.  harst,  ‘rake’,  L.  carrere,
20152:Janet,  fem.  PN.  —  A  dimin.  of  Jane  (q.v.) jangada,  n.,  a  kind  of  catamaran.  —  Port.,  fr. Malayalam  cahhdtam,  fr.  OI.  sarpghatah,  a joining  together  of  timber,  union’, jangar,  n.,  a  raft.  —  Port,  jangada.  See  prec.  word, jangle,  intr.  and  tr.  v.  —  ME .janglen,  ‘to  chatter, quarrel’,  fr.  OF.  jangler,  ‘to  chatter’,  which  is of  Teut.  origin.  Cp.  MDu.  jangelen,  Du.  jen- gelen,  ‘to  whine’,  dial.  G.  jangeln,  ‘to  speak  in a  whining  manner', 'which  are  prob.  imitative. Cp.  jingle.
20402:used  both  for  men  and  women;  of  Celtic  origin, joyous,  adj.  —  OF.  joios,  joious,  joyous  (F.  joy- eux),  fr.  joie,  ‘joy’.  See  joy  and  -ous. Derivatives:  joyous-ly,  ad joyous-ness,  n. jube,  n„  rood  loft  in  a  church.  —  F.  jube,  fr.  L. jube,  ‘bid  thou’,  imper.  of  jubere,  ‘to  bid,  com¬ mand’,  fr.  OL.  joubere,  of  s.m.,  orig.  ‘to  set in  motion,  stir’,  fr.  I.-E.  base  *yeudh-,  whence also  OI.  yodhayati,  ‘involves  in  a  fight’,  yudh-, ‘fight’,  yudhmah,  ‘warlike,  warrior’,  Avestic yuidyeinti,  ‘they  fight’,  yaoshti -, ‘activity,  agility’. Arm.  yuzem,  ‘I  stir  up’,  Gk.  uafxtvy]  (for  *yudh- s-mine),  ‘battle’  (prop,  ‘turmoil’),  Lith.  judit, judeti,  ‘to  move  trembling,  to  quarrel’,  L.juba, ‘mane’,  lit.  ‘that  which  waves,  flutters’.  All  these words  derive  fr.  I.-E.  base  *yeu-dh-,  "to  be moved,  to  be  shaken’,  which  seems  to  be  a dental  enlargement  of  base  *yeu-,  ‘to  mix,  stir’. The  rood  loft  is  called  from  the  first  word  of  a Latin  prayer,  which  was  said  from  the  gallery above  the  rood  screen.
21948:Derivatives:  lithotrit-ic,  adj.,  lithotrit-y,  n. Lithuania,  n.  —  Lith.  Lietuva,  ‘Lithuania’,  of  un¬ certain  origin;  perh.  rel.  to  Lith.  *lei-,  ‘to  pour, drop’,  fr.  I.-E.  base  *lei-,  ‘to  flow’,  whence  pos¬ sibly  also  L.  lit  us,  ‘shore’ ;  see  littoral.  Accord¬ ingly  Lietuva  would  lit.  mean  ‘shoreland’.  For sense  development  cp.  ML.  Ripudrii,  lit.  ‘people living  on  the  banks  of  a  river’  (see  Ripuarians). Derivatives:  Lithuani-an,  adj.  andn. litigant,  adj.,  engaged  in  a  lawsuit;  n.,  a  party  in  a lawsuit.  —  F.,  fr.  L.  litigans,  gen.  -antis,  pres, part,  of  litigate.  See  next  word  and  -ant. litigate,  intr.  v.,  to  go  to  law;  tr.  v.,  to  contest  in  a lawsuit.  —  L.  litigdt-(um),  pp.  stem  of  litigate, ‘to  dispute,  quarrel,  strive',  formed  from  the term  litem  agere,  lit.  ‘to  lead  a  dispute  or  strife’. Litem  is  the  acc.  of  Us,  ‘dispute,  quarrel,  strife, lawsuit’.forearlierrffe,  which  stands  for*rf/-f-Fs, lit.  ‘that  which  is  placed’,  fr.  I.-E.  base  *stel-, ‘to  place’,  whence  also  OL.  stlocus,  locus,  ‘place’, lit.  ‘where  something  is  placed’.  See  locus  andcp. allege.  For  the  etymology  of  L.  agere  see  agent. For  the  formation  of  L.  litigate,  fr.  litem  agere, cp.  L.  jurigare,  ‘to  quarrel,  scold,  chide’,  fr.  jure agere  (see  objurgate).
21950:litigation,  n.,  the  act  of  litigating;  a  lawsuit.  — Late  L.  iitigdtid,  gen.  -onis,  ‘a  dispute,  quarrel’, fr.  L.  litigatfum),  pp.  stem  of  litigare.  See  prec. word  and  -ion.
21951:litigator,  n.,  one  who  litigates.  —  L.  litigator,  ‘a disputant’,  fr.  litigat-(um),  pp.  stem  of  litigare. See  litigate  and  agential  suff.  -or. litigious,  adj.,  quarrelsome.  • —  ME.,  fr.  MF  (=F.) litigieux  (fern,  litigieuse),  fr.  L.  litigidsus,  ‘full  of disputes;  fond  of  disputes,  quarrelsome’,  fr.  li- tigium,  ‘dispute,  litigation’,  fr.  litigare.  See  liti¬ gate  and  -ous.
```


## [2026-09-06T22:18:36.586Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=31325 && NR<=31331' KLN_1966.txt | fold -w 200 | head -30"
}
```


### [2026-09-06T22:18:38.419Z] TOOL RESULT

```
rection’,  and  pp.  of  vertere,  ‘to  turn’.  See  qua and  version.
Derivative:  quaquaversal-ly,  adv. quarantine,  n.,  a  period  (orig.  of  forty  days)  of isolation  to  prevent  the  spread  of  disease.  —  It. quarantina,  fr.  quaranta,  ‘forty’,  fr.
  L.  quadra- gintd.  See  quadragenarian  and  cp.  cuarenta.  The term  goes  back  to  It.  quaranta  giorni,  ‘forty days’.  Ships  coming  from  the  Levant  and  Egypt were  isolated  at  sp
ecial  ports  for  thirty,  later forty,  days.  This  measure  for  preventing  the spread  of  contagious  diseases  was  first  enforced atRagusainl377.  SeeK.  Sudhoff,  “Epidemiolo¬ gical  Rul
es  from  the  Past”,  in  Essays  in  the History  of  Medicine,  trans.  F.  H.  Garrison,  New York,  1926,  p.  152.
Derivatives:  quarantine,  tr.  v.,  quarantin-er,  n. quarrel,  n.,  dispute.  —  ME.  quarel,  quarelle,  que- rele,  fr.  OF.  querele  (F.  querelle),  fr.  L.  querela, also  querella,  ‘comp
laint’,  fr.  queri,  ‘to  complain’, which  is  prob.  cogn.  with  OI.  svdsati,  svasiti, ‘blows,  breathes,  sighs’,  OE.  hwSsan,  ‘to wheeze’.  See  wheeze  and  cp.  querimonious,
  quer¬ ulous.  Cp.  also  cyst.
Derivatives:  quarrel,  v.  (q.v.),  quarrel(l)-er ,  n., quarrel(l)-ing,  adj.,  quarrel(l)-ing-Iy,  adv.,  quar¬ rel-some,  adj.,  quarrel-some-ly,  adv.,  quarrel- some-ness,  n.
quarrel,  intr.  v.,  to  engage  in  a  quarrel.  - —  Partly fr.  OF.  quereler  (F.  quereller),  partly  fr.  prec. word.
quarrel,  n.,  1)  arrow  or  bolt,  formerly  used  with  a crossbow;  2)  small  diamond-shaped  pane  of glass.  —  ME.,  fr.  OF.  quarel,  quarrel  (F.  car- reau),  fr.  ML.  quadrellus,  dimi
n.  of  quadras, ‘square’.  See  quadrate,  adj.,  and  -el. quarry,  n.,  anything  hunted,  prey.  —  ME.  querre, quirre,  fr.  OF.  cuiree  (F.  curee),  ‘the  spoil,  quar¬ ry’,  fr.  
cuir,  ‘hide,  skin’,  fr.  L.  corium.  The  orig¬ inal  meaning  of  quarry  was  ‘parts  of  a  slain animal  placed  on  its  hide  as  the  hound’s  reward’. See  corium  and  cp.  cor
tex,  cuirass, quarry,  n.,  quarrel.  —  A  later  var.  of  3rd quarrel.
quarry,  n.,  a  place  for  excavating  stones.  —  ME. quarey,  fr.  earlier  quarrere,  fr.  OF.  quariere  (F. carriere),  fr.  Late  L.  quadraria,  fr.  L.  quadrare, ‘to  square’  (said  
also  of  stones).  See  quadrate,  v. Derivatives:  quarry,  tr.  v.,  to  excavate  stones from  a  quarry,  quarri-ed,  adj.,  quarri-er,  n., quarry-ing,  n.
```


## [2026-09-06T22:18:50.629Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT cyst/quarrel/wheeze ===\"; grep -n -i \"^cyst\\|Cyst,\\|Quarrel,\\|Wheeze,\" SKT.txt | head -10"
}
```


### [2026-09-06T22:18:50.679Z] TOOL RESULT

```
=== SKT cyst/quarrel/wheeze ===
4622:Cyst,  a  pouch  (ill  animals)  containing morbid  matter.  (L.  -  Gk.)  Fonnerly written  c^'slu  —Late  U  ryj/tf.  — Gk.  *n/ffTi», a  hng.  pouch.  •■  Gk.  jcvfir,  to  cotitaiu. iV  KU.)
12410:Noise.  (F.-L.-Gk.  \)  M.  E.  noist.~ V.  Hoist,  O.  F.  nose,  a  debate,  quarrel, noiie  Cf.  Prov.  noisa,  nausa,  nun'ut. p.  Diez  holdn  that  it  can  only  be  derived from  L.  nausea,  &ea-sickness,  disgust,  hence annoyance,  Stc. ;  the  L.  word  being  bor- rowed from  Gkl  See  Nauaea.  >.  Some attempt  to  derive  il  from  L.  noxia,  barm, put  for  m>xa,  harm;  see  Noxioua.  (Di:«- putcd ;    bcc    Uicx,  Schelcr^  laltre.)     Der.
22837:fuack,  quail,  quarrel,  quarry,  quill,  quire, Quiver.
```


## [2026-09-06T22:18:51.428Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW queror ===\"; grep -n \"queror\" LEW_1910.txt | head -5; echo \"=== LAT queror ===\"; grep -n \"queror\\|queri\" LAT.txt | head -8"
}
```


### [2026-09-06T22:18:51.486Z] TOOL RESULT

```
=== LEW queror ===
=== LAT queror ===
3753:rizo) - ayYOCpeuco "requerir pour une corree de transports" d'ou "con-
10551:cauilla, -&e f.(cauillum n., -us, m.): plaisanterie, moquerie. Ar-
11402:crimen par *querimen deveau *quirimen sous 1'influence de quiritare.
26852:d’an adj. *gratulus, derive de grator comme querulus de queror, etc.
34882:ludibrium: moquerie, derision, et objet de moquerie (formi sans doute
40625:pour acquerir une valeur plus expressive, cf. ne—c (different de neque,
48331:deux tardifs); complBrB (dpoq. ispdr., cf. conqueri ); dgplBrB (cf.
51898:queror, -eris, questus stim, queri: "ponsser des eris plaintifs”,
```


## [2026-09-06T22:18:53.645Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51895,51930p' LAT.txt"
}
```


### [2026-09-06T22:18:53.690Z] TOOL RESULT

```
"aesculus”.
Snr la forae dissinilie cerquus, ▼. en dernier lieu Niederaann,
Baerita, HI 1944, P• 3 »•
queror, -eris, questus stim, queri: "ponsser des eris plaintifs”,
se dit des personnes conae des aninaux; pnis plus giniralenent ”se
plaindre". Transi-tif et absoln: queri fortunas suas. Anci en et clas¬
si que, mais ne semble plns enployi aprbs le preaier sibcle de l'Bapire.
La langue de 1 'tiglise 1 'ignore. Le verbe n'est pas passi dans les
l.romanes, qui ont iviti peut-etre 1 'homonymie de quaerS.
Dirivis en quer-, et en quest-: querela (querella; la forae ea -Sia
seable la plus ancienne, cf.Benveniste, Orig. de la form. des ncms
en t.-e., p.4«),-oe f.: plainte, d'oi querelor, -dris (Arn.Serr.);
queribundus (rafe, nais classique, Cic.Sull.10,30); queritor,-dris
(Plin., Tac.) j querulus (surtout poit.)j querulSsus (b.lat.); queri-
nffriia, forae ancienne (Pl.), demeurie partielleaent dans les langues
roaanes, M.L.6934 {quaeri-?) ; questus, -Os a.(surtout au pluriel
dans la 1 . classi que): plainte(s); questis? Cic.Bru.x43 (peut Stre
une glose), Cf. aussi Querolus (Lv s.) comme Pseudolus.
Composis: conqueror: se plaindre avec, cf.Pl.Mi.155: conqueritur
aecos mulier fortunas suas } d T ob conquestiS: plainte en coaaun,
spicialement devunt un juge; cf. Cic.Inu.1,160 conquestio est oratio
auditorum misericordiam captans.
Le rapprochement usuel avec skr .gvdsiti "il souffle fort" n'est
pas pleinement satisfaisant: les sens ne concordent pas d'une maniore
exacte, et le latin n'a pas trace dn caractbre dissyllabique de la
racine, net en sanskrit. Le sens de "pousser un siffLeaent” se retrouve
dans v.isl. huaesa, v.angi .hwdesan. Le verbe latin est assez iaoli.
querquerus, -a, -un: adj. employi au fiminin dans querquera,
scii, febris-, cf.P.F.309,3, querqueram frigidam cum tremore a Qraeco
xapxapot certum est dici, unde et carcer. Lucilius (1194): "iactans
me ut febris querquera' 1 . St alibi (1377): "querquera consequitur
capitisque dolores". Item Plautus (fr.79): "is mihi erat bilis, quer-
queratus". Outre ces fragmenta, le not ne figure que dans Aulu-Gelle,'
Arn.,Apul., et dans les gloses.
Mot expressif k redoublenent sans cbrrespondant exact; cf.gr.
xapxatpw. — Si febris a signi fi i d'abord "frisson", querquera est
```


## [2026-09-06T22:19:01.200Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ hawa ===\"; grep -n -i \"hawā\\|hawa'\\|هواء\" FVQ.txt | head -8; echo \"=== KLN hawa ===\"; grep -n -i \"Arab\\. hawa\\|hawa',\" KLN_1966.txt | head -5; echo \"=== ARY هوا ===\"; grep -n \"هوا\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T22:19:01.274Z] TOOL RESULT

```
=== FVQ hawa ===
=== KLN hawa ===
=== ARY هوا ===
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
110:.۰ "(۷۰1۷۸۵۵ 0۸2/6811022 3۰) چنین فرض کرده‌اند که گهواره‌ی مردمان هند و اروپایی
126:دیسدمان دیگر در باره‌ی گهواره‌ی آغازین هند و اروپایی‌ها این است که زادگاه
136:باستانشناسی و ویژگی‌های زبان شناختی زبان‌های ژرمنیکه؛ دیدمان گهواره بودن آلمان را نی ی
145:گهواره‌ی هند و اروپائیان از دیدگاه هواداران «آلمان مرکزی»
150:گهواره گاه این مردم هند و اروپایی کجا بود؟ واضح است که زبان هند و اروپایی خود بگی از
163:کوج می‌کردند. بدین دلیل» فرض بر این است که گهواره هند و اروپایی‌ها وسیع تر از حد معمول بود و
202:از بررسی زبالشناختی برای یافت گهواره‌ی هندو اروپائیان چه دتایچی گرفته
220:دست نیست. وی علت تعیین محل گهواره در نواحي شمال دریاهای سیاه و خزر منحصر به پیش بالا
256:۲ هسانی‌های فوق‌الذکر (ا زگهواره به سوی باختر و اروپایی باختری و جنوبی و همچنین از
```


## [2026-09-06T22:19:03.612Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 260 page check ===\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"Av. sušI-\")\nif i<0: i=t.find(\"cvasa-: Av\")\nif i<0:\n    import re\n    m=re.search(r\"Av\\. su.i-\", t); i=m.start() if m else -1\nprint(i)\nprint(t[max(0,i-3000):i+700])\nEOF"
}
```


### [2026-09-06T22:19:05.490Z] TOOL RESULT

```
=== SYN 260 page check ===
622884
ele ‘skin, hide’, Sp. piel ‘pelt’; fr, dim. also Sp. pellejo ‘hide’), Goth. pruts- fill leprosy’, ON berfjall ‘bearskin’, OR fell, ME, NE fell, Du. vel, OHG fel, MHG vel, NHG fell : Grk. épugi-redas ‘inflam- mation of the skin’, Lith. plévé ‘film’, etc., prob. fr. a *pel- ‘cover’, an extension of which may be seen in Goth. filhan ‘hide, bury’ (4.78). Walde-P. 2.58f. (ad- versely to this root connection). Er- nout-M. 749. Falk-Torp 217. Persson, Beitrige 226, 946.
Lat. cortum ‘hide, leather’ (> It. cuoio, Fr. cuir, Sp. cuero all mostly ‘leather’, but sometimes ‘skin, hide’), Pol. skéra, Russ. skura, Skt. carman-, Ay. €araman-, all fr. IE *(s)ker- ‘cut’ in Grk. xelpw ‘shear’, etc. Walde-P. 2.573 ff. Ernout-M. 220. Walde-H. 1.274.
3. For the following, and some other, less important, Celtic words (as Ir. codal, bian ‘hide’) cf. esp. Vendryes, Les noms de la “peau” en celtique, Wort. u. Sach. 12.241 ff.
Tr. cness, NIr. cneas, W. cnes (rare), perh. fr. *knid-ta-: Ir. cned ‘wound’, Grk. xvifw ‘scrape, chafe’, OE hnitan ‘strike’, ete. (Walde-P. 1.395, without inclusion of Ir. eness, etc.). Vendryes, loc. cit.
Ir: croccenn, NIr. croiceann, W. croen,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
7H BODY; BOD!
*frokno-, perh., like Lat g) fr. IB *(s)ker- ‘cut. Vendryes, loc. cit. oe (both now AS eke
ee Ir. cennt ‘scales’) : opds.)> ce aaa and ON skinn, Walde-P. 2.563. seithe : Lat. secare Walde-P. 2.475. 3, OF hgd, OHG hit, etc., the general Gme. word for ‘skin’ ae hide DOW properly only os animals) : Grk. oxdros ide, leather’, Lie: cutis skin’, Lith. kiautas ‘hull, husk’, OPnuss. keuto ‘skin’, Ir. codal ‘hide’; Grk. xev@w, OE hgdan ‘cover, hide’, ete., fr. IE *(s)keu- with various extensions. Walde- Pp. 2,546ff. Ernout-M. 249. Falk- Torp 4265.
ON skinn (> ME skinn, NE skin), Dan. skind, Sw. skin: MHG_ schint ‘fruit skin’, Du. dial. schinde ‘hide, bark’, OHG scintan, NHG schinden ‘remove the skin or bark’, ON hinna ‘mem- brane’, W. cen ‘skin’, etc. (above, 3), fr. an IE *(s)ken- ‘cut off’, perh. an exten- sion of *sek- ‘cut’. Walde-P. 2.563 f.
fr. boveé,
‘out’, etc. 4, ON hi
Digitized by Arya Samaj Foundation Chennai and eGangotri
LY FUNCTIONS AND CONDITIONS 201
ON Aad and skinn are both applied to the skin of man or beast. The dis- tinction prevailing in Dan., less marked- ly in Sw., is secondary (cf. Falk-Torp 997), like the opposite distinction in NE.
For ON horund ‘flesh, skin’ (of a hu- man being, but even here not the usual word), see 4.13.
5. Lith. oda, Lett. dda, etym.?
ChSl., SCr. koza (> Rum. coaje ‘bark, rind’), Boh. kiize, pokozka, Russ. koda, orig. ‘goatskin’, fr. koza ‘goat’. Cf. Skt. ajina-, below, 6. Walde-P. 1.336. Berneker 597 f. Briickner 263.
Pol. skéra, Russ. skura (WhRuss. skura > Lith. skira) : Lat. coriwm, etc.,
above, 2.
6. Skt. tvac-, -tvacas- : Grk. cakos ‘shield’, root connection? Walde-P. 1.747.
Skt. carman-, Av. éaraman- ‘hide’ : Lat. cortum, etc., above, 2.
Skt. cyavi-, fr. IE *(s)keu- ‘cover’? Walde-P. 2.546.
Av. suri- (once, Barth. 1586), etym.?
Skt. ajina- ‘hide’: ChSl. jazno ‘leather’, derivs. of word for ‘goat’, Skt.
Falk-Torp 997. aja-, etc. Walde-P. 1.38. fe 4.13 FLESH NG ia xptas Goth. mimz, mammé Lith. mésa oe a aidan ON hold, horund Lett. miesa It. carne Dan. kd ChSl. _pliitt, meso Be igtiags Sw. kétt SCr. meso Sp. carne OE Sl@sc Boh. maso Rims carne ME fleshe Pol. —_ mieso ae feoil, cua NE flesh Russ. mjaso Nir, feoil oe é ei Skt.  mdnsa-, mas- ‘cig, evs Av. av- (NPers. gust Br kig giaiad tS vleisch es be Most of th ee € words ‘ : ot all, are also ead a flesh’, though | semantic sources, where clear, are partly Meat (5,61), Words Ae Beshy as food, | ‘covering, surface’, referring to ‘f
```


## [2026-09-06T22:19:09.432Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6720,6740p' SYN.txt"
}
```


### [2026-09-06T22:19:09.496Z] TOOL RESULT

```
‘blow’ (10.38) ; Sp. resollar, Rum. rdsufla (whence sb. rdsuflare), fr. new cpd. parallel to Lat. resptrare. REW 8430. Puscariu 1447.
Sp. huelgo (Port. folego), back-forma- tion to Sp. holgar (Port. folgar) ‘rest, cease from labor’, orig. ‘stop for breath’ from ‘pant’, fr. VLat. follicare ‘swell or move as a bellows’, deriv. of Lat. follis ‘bellows’. REW 3417.
4. Ir. do-berim andl lit. ‘give breath’; for andl, etc., see above, 1.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5. Goth. anan, OF orpian, above, 1.
OE @)m, Du. adem, OHG alum MHG, NHG atem, whence the vbs, OR épian, Du. ademen, OHG alumon, ete, : Skt. diman- ‘breath, soul, life’, connection? Walde-P. 1.118.
ME breth, breeth, NE breath (whence vb. ME brethe, NE breathe), fr. OF braep ‘odor, smell, scent’ : OHG bradam ‘ex. halation, heat’ (fr. the root in ON bradr ‘heated’, OE bre@dan, OHG bratan ‘bake’, etc.). The meaning ‘breath’ comes by specialization, either of ‘exhalation’ (the sense ‘exhalation, vapor, steam’ com- mon in ME). Walde-P. 2.158. NED s.v. breath.
NHG hawch, fr. hauchen, MHG hichen ‘blow the breath, breathe out’, of imita- tive orig. Weigand-H: 1.820.
6. Lith. kvépuoti,  kvapas : kvépti ‘blow the breath’, kvepéti ‘smell, emit an odor’, Lett. kvépt ‘steam, smoke’, Grk. xamvos ‘smoke’, Lat. vapor ‘steam’, ete. Specialization of ‘exhalation’. Walde-P. 1.380.
Lett. dvasuot, dvasa (Lith. dusti ‘get out of breath’, dvésti ‘expire, die’, dvésuoti ‘pant’, dvasia ‘spirit’ also ‘breath’), ChSl. dychati (duchati ‘blow’) with sbs., dychanije, duchii, etc., general Slavic, fr. IE *dhwes-, *dhus-, extension of *dheu- in Skt. dhi- ‘shake, agitate’, Grk. Giw ‘rage, seethe’, etc. Walde-P. 1.846. Berneker 234 ff., 249.
Lett. elpét, fr. the noun elpe, this prob. through ‘weak breath’ or ‘pant’ (ef. also Lett. alpa ‘moment of time’) : Lith. alpti ‘faint’, alpnas ‘weak’, this perh. : Skt. alpa- ‘small’. Miihl.-Endz. 1.568.
7. Skt. an-, ana-, Av. dnti-, pardnit-, above, 1.
Skt. ¢vas-, cvdsa-: Av. susi- ‘the lungs’, Lat. quer? ‘lament, bewail’, ON hvesa, OF hwesan ‘pant’, etc. Walde-P. 1.474,
Skt. atman-, : OE @pm, etc., above, 5.
ete,,
Toot
d here is ‘open th any of them may be extended to ‘open wide
in general (of the earth, etc.). Nearly all of them show secondary associations with mental attitudes of which the ac- tion is indicative, namely wonder, stu- pidity, or fatigue. In such secondary associations they may be differentiated, as NE yawn (with fatigue) and gape (in- dicating wonder or stupidity; hence also ‘stare at? with open mouth, as usually NHG gaffen; but gape formerly and still locally ‘yawn’), or be restricted to one or another of these notions.
1, IE *9he(i)-, *ghi-, *Ghia-. Walde- P. 1.548 ff. Ernout-M. 453 f. Walde-H. 1.648, space anes eee Tenth, Ee ‘gape’, aha see a aC ag (0s if from pees t.) or Xacwouprodpan ‘gorge! oo) x giioac, like khewcodpa
2 oe Sit.) NOW ‘yawn’; Lat. hiadre; ON gina, OER ginan 14) Z . =) sane gan, ganian, ME zone, 1 gane, NE yawn (NED vb. and yawn S.VV. gane, Ginén, geinon, ae Du - geeuwen, ONG Teton omen, ots. Wace iene th. Ziovaut; in ees AG gahnen; “Avdties; Chg). 4; cpds. ~Zioti, Lett. tnd eijaja), ete. penn at (Pres: ahha tr (G8 ty eREAl Slave; Took “ane, Language 21.21),
ODILY FUNCTIONS AND CONDITIONS
```


## [2026-09-06T22:19:16.556Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=6660 && NR<=6740 && /BODILY|BODY|4\\.5[0-9]|25[0-9]|26[0-9]/ {print NR\": \"substr($0,1,150)}' SYN.txt | head -20"
}
```


### [2026-09-06T22:19:18.264Z] TOOL RESULT

```
6690: ILY FUNCTIONS AND CONDITIONS 259
6693: 4.51 BREATHE; BREATH
6712: 260 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-06T22:19:22.931Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ریه\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-06T22:19:22.985Z] TOOL RESULT

```
MON_part2.txt:148:گیلاس در پزشکی آب مقطر لوریه سریز 
MON_part2.txt:1375:خرخری که به سبب گریه يا فشردن گلو در 
MON_part2.txt:1839:گریه و نله سیار کردن. غش و ضعف کردن: 
MON_part2.txt:2002:و قصبة الریه و لالا گوش و مفاصل موجود 
MON_part2.txt:2214:جاریه؛ ج. غلمان. غلام پست: مأمور پست 
MON_part2.txt:3292:غوره (عم.) گریه کردن (در مقام سرزنش 
MON_part2.txt:7072:این وزارت در اواسط قاجاریه بنام وزارت 
MON_part2.txt:7257:فریه. (۵-)2۲۷۸] [ع.] ۳1 درو غ بهتان افتر ا. 
MON_part2.txt:10371:قاضی لشکر (صفویه» قاجاریه» پهلوی). 
MON_part2.txt:10945:ناهریه: (0-)۸- ۷2136۲1۷۷ [ع. قاهر به ] 
MON_part2.txt:12041:قری و قصبات میگ فتند (قارجاریه). 
MON_part2.txt:12107:واحد پول ايران در عهد قاجاریه و اوایل 
MON_part2.txt:12168:ثر به: (۵-) ۲۵۲۳2 [غ. فریه] (.) مشکك شیر. 
MON_part2.txt:12616:فریه. (۵-)۱۸۵ (ع. قریه ] (۱.) دهء روستا. 
MON_part2.txt:12631:قاجاریه). سرباز ایرانی که تحت تعلیمات 
MON_part2.txt:12633:قراقان روسی ملبس بودند (اواخر قاجاریه). 
MON_part2.txt:12680:باشد که چون در قریه‌ای کسی کشته شود و 
MON_part2.txt:12681:اهل قریه گویند که قاتل معلوم نیست؛ پنجاه 
MON_part2.txt:12682:کس را از اهل قریه سوگند دهند. مصالحة 
MON_part2.txt:13747:بیست و چهار کیله. (رسالةٌ مقداریه. فرهنگ
```


## [2026-09-06T22:19:24.570Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"شش\" incoming/ARY/ARY_pages.txt | head -20; echo \"=== ARY latin index SHOSH ===\"; grep -n -i \"shosh\\|SHUSH\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T22:19:24.631Z] TOOL RESULT

```
21:۲- کوشش کرده‌ام که پیگیری واژه‌های فارسی را در این مسیر انجام دهم: فارسی -> پهلوی >"
152:اروپایی زبان واحد مردمی بود که حدود چهار تا شش هزار سال پیش در ناحیه‌ی نسبتاً محدودی
178:اس است: درفرن, ششم پس از میلاد» مردم ترک زبان فقً در ناحيه‌ي نسبتاً کوچکی در شمال مغولستان و
180:و اسب‌سواران ماهری پودند. این مردم در طی هفت قرن (از سده‌ی ششم تا سیزدهم پس از میلاد) طی
348:باختری فرانسه تکلم می‌شود در گذشته بخش عمده‌ی اسپانیا را زیر پوشش داشته است. شواهد فراوان
666:گسترش اقوام ترک زبان (سده‌های ششم تا سیزدهم میلادی) موجب آمپزش آنها با ایرانیان و
685:گمترش زبان‌ها و افوام ایرانی تا حدود قرن ششم میلادی
725:ناشی از سنگك نوشته‌ها و سکه‌ها و لوحه‌های دوران هخامنشی از سده‌ی ششم تا چهارم پیش از میلاد:
790:قرن ششم میلادی از میان رفت ولی بررسی ساختار دستوری و واژگان آن در شناخت زبان‌های
863:شش میلیون نفر به این دو زبان سخن می‌گویند.
870:دوران باستان در همین سرزمین رواج داشته» مشتق شده باشد. امروزه حدود شش میلیون نفر به ان
935:تصویر کلی فرهنگ و جامعهی هند و اروپایی حدود شش هزار سال پیش را به تقریب ترسیم کنند.
940:ایزدسازی عوامل طبیعی (ماه و خورشید و توفان و غیره) استوار بود. مثلاً واژه‌ی «شاه» در شش زبان
1144:زرتشتی است. بخش قدیمی‌تر آن (گاتها) در سده‌های پازدهم تا ششم پیش از میلاد یعنی دوران کوج
1225:همچون بارتولومه و معین بطرر نسبتاً کامل بازتاب شده است. کوشش من در کتاب حاضر این بوده
1234:به همین دلیل بخش عمده‌ی کوشش من در این کناب صرف یافتن واژه‌های فارسی نوین که با"
1256:سوم -بخش دیگری از کوشش‌های من در این کناب صرٍف یافتن ریشه‌های هند و اروپایی
1292:متفاوتی استفاده می‌کنند. در این کناب کوشش شده است تا حد امکان املای واژه‌ها یکدست بشود.
1762:ایسلند یکهن (1۸27 564/0104۸ 0ا0): پسگشت‌ها شش تا
3309:بخش, بخشیدن, بخشش / ۱۱۵
=== ARY latin index SHOSH ===
10937:GIOTAN (OLD SAXON) pS pS SHUSHTIN KURDISH) «52,5
10998:SAZHAI, SAGHAT SHUSH, SUSH PAHLAVI] 5 3h44
11003:SHUSHINTI (LITHUANIAN) 53, SHUNCH ARMENIAN) +
```


## [2026-09-06T22:19:28.386Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10990,11010p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T22:19:28.427Z] TOOL RESULT

```
POKORNY SSOS*S~*~*~«dS SEX HOLD FRISIN) oS 53.5
BARNHART: (SIX) 1011 SEHS :(OLD HIGH GERMAN) of lal
DELAMARRE: 212-213 SECHS (GERMAN) glalT
MACKENZIE: (SIX) 133 SIEX (OLD ENGLISH) pS g-sSil
1tPF seb olny SIX ENGLISH) gS
SEKS DANISH) jails

AFGHAND (+4) gil SUSHI HAVESTAN) glu 3) q
SAZHAI, SAGHAT SHUSH, SUSH PAHLAVI] 5 3h44
KwAs (TOKHARIAN A) A 5,\55 PISHIK (KURDISH) 53,5
[pdf page 378]
| YA | pts
HVASE (DUTCH) ihe CVAS, SHVASITI :(SANSKRIT) 24 Sil.
SHUSHINTI (LITHUANIAN) 53, SHUNCH ARMENIAN) +
QUEROR, QUERI S(LATIN) 3
REFERENCES beth HOLD SCANDINAVIAN) 245 5-thes)
POKORNY, = ==S*S*~*«S HVASA
BARNHART: (WHEEZE) 1230 HOLD ENGLISH) pf gS:
MACKENZIE: (LUNG) 122 HWOSAN, HWAST
‘MALLORY & ADAMS: KUESH WHEEZE ENGLISH) 5-83)
ev ebb ob, VASA SWEDISH) $2 y=
```


## [2026-09-06T22:19:36.202Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10960,11035p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T22:19:36.243Z] TOOL RESULT

```
[pdf page 377]
|

ot | ra

i

i SEX SWEDISH) 48 yo SHPAZH 4AFGHAND) (4) gti

SEKS NORWEGIAN) $95 sik -(TOKHARIAN A) A. jis

i ZES , here gale SKAS :(TOKHARIAN B) B jis

| “jp + HOLD.CHURCH SLAVIC) yf 5 3% my ASANSKRIT) 2 Suibe

a oP asm SHASH, SHAT, SAS., SAT

CZESEIU POLISH) Jlong) VECH, VETSS (ARMENIAN) «gs!

j SHEST AARUSSIAN) guys HEKS, WEKS, HEX (GREEK) gly
SHEST $(CZECH) Soy SEX LATIN) 3
SHEST (BULGARIAN) <6 a, six (FRENCH) sil
SHEST (SLOVAK) 1 jLa\ SEIS SPANISH) glia!
SHESHI (LITHUANIAN) gl 3 SEL AUTALIAN) glu!
st HOLD IRISH) oS 545 p\ SASE :(RUMANIAN) giog y
CHWECH AGAULISH) JE SEIS (PORTUGUESE) Js 4
GJASHTE, GASHTE:(ALBANIAN) JU SAIHS GOTHIC) Sif

SEX .(OLD SCANDINAVIAN) oA oly!
‘REFERENCES beth SEHS — (OLD SAXON) oS pS
POKORNY SSOS*S~*~*~«dS SEX HOLD FRISIN) oS 53.5
BARNHART: (SIX) 1011 SEHS :(OLD HIGH GERMAN) of lal
DELAMARRE: 212-213 SECHS (GERMAN) glalT
MACKENZIE: (SIX) 133 SIEX (OLD ENGLISH) pS g-sSil
1tPF seb olny SIX ENGLISH) gS
SEKS DANISH) jails

AFGHAND (+4) gil SUSHI HAVESTAN) glu 3) q
SAZHAI, SAGHAT SHUSH, SUSH PAHLAVI] 5 3h44
KwAs (TOKHARIAN A) A 5,\55 PISHIK (KURDISH) 53,5
[pdf page 378]
| YA | pts
HVASE (DUTCH) ihe CVAS, SHVASITI :(SANSKRIT) 24 Sil.
SHUSHINTI (LITHUANIAN) 53, SHUNCH ARMENIAN) +
QUEROR, QUERI S(LATIN) 3
REFERENCES beth HOLD SCANDINAVIAN) 245 5-thes)
POKORNY, = ==S*S*~*«S HVASA
BARNHART: (WHEEZE) 1230 HOLD ENGLISH) pf gS:
MACKENZIE: (LUNG) 122 HWOSAN, HWAST
‘MALLORY & ADAMS: KUESH WHEEZE ENGLISH) 5-83)
ev ebb ob, VASA SWEDISH) $2 y=
HVESE, KVESE (NORWEGIAN) 533,
sethsl
AAS oh ee a La 625 ob rl Lale® lads 92 05a cal pe
op AOU 2 Ns atl ee
HS 52S 4393 todY O05 22 05 cal |
SEXTOTA, SEXTO XSHTVA HAVESTAN) plans!
SAIHSTA GOTHIC) S36 SHASHUM. A(PAHLAVD) 5 Sy,
SENSTO {OLD SAXON) oS gS SHPAZHAM — :(AFGHANT) (5-4) gl
OLD HIGH GERMAN) if gies SKAST X{TOKHARIAN A) A 5 j\53
SENSTO SKASTE —(TOKHARIAN B) B 5 ,\53
SECHSTE GERMAN) lat SASTHAS (SANSKRIT) ey Suite
HOLD ENGLISH) eS gS HEKTOS sectay HORRERY gy an
SIEXTA, SYXTE SEXTUS 7 a8 am ey
SIXTH ENGLISH) 583! SIXIEME FRENCH) sui}
ZESDE (DUTCH) gscla SEXTO SPANISH) lil
OLD CHURCH SLAVIC) 553%! SESTO HITALIAN) g\al
SHESTO (RUMANIAN) giles,
SZOSTY, SZOSTA (POLISH) Jn) AS SASELEA, A SASEA
LITHUANIAN) ip PORTUGUESE) Ji 4
[pdf page 379]
‘REFERENCES WacotKoy SHISHTAS, SHESTY
POKORNY, = SS*~S:*~*« USCHTS (OLD PRUSSIAN) oS goo.
BARNHART: es ! 4S1XTH) 1011 SESSED HOLD IRISH) oyS $33 4)
apn DELAMARRE: (SIXIEME) 213 CHWECHED NGAULISH) JE
VPA i gbG ohn
```


## [2026-09-06T22:19:42.898Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['ARY'];print(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T22:19:45.137Z] TOOL RESULT

```
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
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
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"
}
```


## [2026-09-06T22:19:50.172Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport subprocess\nsubprocess.run(['pdftoppm','-f','378','-l','378','-r','160','-png','-singlefile','/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf','ary378_p294'])\nfrom PIL import Image\nim=Image.open('ary378_p294.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.42))).save('ary378_top_p294.png')\n\""
}
```


### [2026-09-06T22:19:52.484Z] TOOL RESULT

```
(800, 1280)
```


## [2026-09-06T22:19:54.882Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary378_top_p294.png"
}
```


### [2026-09-06T22:19:54.903Z] TOOL RESULT

```

```


## [2026-09-06T22:20:06.493Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport subprocess\nsubprocess.run(['pdftoppm','-f','377','-l','377','-r','160','-png','-singlefile','/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf','ary377_p294'])\nfrom PIL import Image\nim=Image.open('ary377_p294.png'); w,h=im.size\nim.crop((0,int(h*0.62),w,h)).save('ary377_bot_p294.png')\n\""
}
```


### [2026-09-06T22:20:08.605Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:20:10.888Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary377_bot_p294.png"
}
```


### [2026-09-06T22:20:10.903Z] TOOL RESULT

```

```


## [2026-09-06T22:20:18.614Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 294 -l 294 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg294_p294 && ls -la pg294_p294.png"
}
```


### [2026-09-06T22:20:20.838Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 36312 Sep  6 18:20 pg294_p294.png
```


## [2026-09-06T22:20:23.046Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg294_p294.png"
}
```


### [2026-09-06T22:20:23.373Z] TOOL RESULT

```

```


## [2026-09-06T22:20:23.371Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:20:30.658Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS sus ===\"; grep -n -i \"suš\\|sus\\b\\|lung\" SNS.txt | head -20; echo \"=== SNS_pages ===\"; grep -n \"lung\\|Lung\" SNS_pages.txt | head -10"
}
```


### [2026-09-06T22:20:30.720Z] TOOL RESULT

```
=== SNS sus ===
8441:J j> tr*-^ ^ pasus.haurva-: t« 
9977:(AiW>. ^ : /kas: 3 l caksus-: &S a *to caiman- :£l- 
11564:•*o -yii :sus: -*_»tu 
11565:■f/U<* Ut^. 1586) sus-: km 
12384:.fll\£ (pasus hvar: 
15357:Ijb^jOil L«:nasay: .o^vt ^U-^bAy-nasus: -*o<u I 
28698:cSksus- 158/7 
29045:sus- 192/6 
29382:pasus.haurva- 124/19 
31145:sus 192/5 
31743:pasus-hvar 124/18 
32135:nasus 274/16 
=== SNS_pages ===
```


## [2026-09-06T22:20:35.300Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11558,11572p' SNS.txt"
}
```


### [2026-09-06T22:20:35.344Z] TOOL RESULT

```
U„ t .173 )a sa-^ t^M.. 2 17>asva- 1 ^. aspa _ : < ; . 
-pt****&&)ri :asp i karzarlg: »>1~JX»J - ^^^ 



•*o -yii :sus: -*_»tu 
■f/U<* Ut^. 1586) sus-: km 



■*/ir*U*», 155!) .^:/Sav:,. saosyant-:,:
```


## [2026-09-06T22:20:40.717Z] TOOL CALL #59: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T22:20:40.726Z] TOOL RESULT

```


```


## [2026-09-06T22:20:44.981Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%B4",
 "prompt": "Give the full Persian etymology sections for شش (both \"six\" and \"lung\"). Quote the etymology of شش meaning \"lung\": Middle Persian form, Proto-Iranian reconstruction, Avestan cognate, PIE root, and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-06T22:20:46.422Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%A7",
 "prompt": "Give the Persian and Arabic etymology sections for هوا. What is the origin of Persian هوا \"air, weather\"? Is it borrowed from Arabic هَوَاء (hawāʾ)? What is the Arabic root and its etymology?"
}
```


### [2026-09-06T22:20:52.820Z] TOOL RESULT

```
# Etymology of Persian هوا

## Persian Etymology

According to the Wiktionary entry, Persian **هوا** (hawā / havâ) is "[Borrowed](/wiki/Appendix:Glossary#loanword "Appendix:Glossary") from [Arabic](https://en.wikipedia.org/wiki/Arabic "w:Arabic") _[هَوَاء](/wiki/%D9%87%D9%88%D8%A7%D8%A1#Arabic "هواء")_ (hawāʔ, "air")."

Yes, the Persian term is indeed a loanword from the Arabic term.

## Arabic Etymology

The document indicates that Arabic **هَوَاء** (hawāʔ) belongs to the Semitic root **ه و ي** (h-w-y). However, the Wiktionary page does not provide further etymological information about the Arabic root's origin—it only documents that various Arabic dialects (Egyptian, Gulf, Hijazi, Moroccan, and South Levantine) inherit or derive from this classical Arabic word.

The entry shows the term spread throughout multiple languages via both direct Arabic borrowing and through Persian intermediaries.
```


### [2026-09-06T22:20:52.944Z] TOOL RESULT

```
# Persian Etymology Sections for شش

## Etymology 1: "Six"

From Middle Persian (šaš), from Proto-Iranian *[\*šwáš](/wiki/Reconstruction:Proto-Iranian/%C5%A1w%C3%A1%C5%A1), from Proto-Indo-Iranian *[\*šwáćš](/wiki/Reconstruction:Proto-Indo-Iranian/%C5%A1w%C3%A1%C4%87%C5%A1), from Proto-Indo-European *[\*swéḱs](/wiki/Reconstruction:Proto-Indo-European/sw%C3%A9%E1%B8%B1s).

Cognate comparisons span multiple language families, including Northern Kurdish şeş, Avestan xṣ̌uuaš, Sanskrit ṣáṣ, Hindi chah, Spanish seis, German sechs, Russian шесть, and Lithuanian šeši.

## Etymology 2: "Lung"

**Middle Persian form:** [Book Pahlavi needed] (suš, "lung")

**Proto-Iranian reconstruction:** *[\*cušíH](/wiki/Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH) ("lungs")

**Avestan cognate:** 𐬯𐬎𐬱 (suš, "lung")

**Etymology summary:** The term derives from Proto-Iranian, with related forms appearing across Iranian languages including Pashto sëģay, Northern Kurdish sîh, and Ossetian sos.

**Cited source:** MacKenzie, D. N. (1971), "¹suš", in *A concise Pahlavi dictionary*, Oxford University Press, page 78.
```


## [2026-09-06T22:21:14.672Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH",
 "prompt": "Give the full reconstruction entry: the Proto-Iranian form, gloss, the Proto-Indo-Iranian / PIE root it comes from, all descendants (Avestan, Middle Persian, Persian, Pashto, Kurdish, Ossetian), and cited references."
}
```


## [2026-09-06T22:21:16.642Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CF%83%CF%84%CE%B9%CF%82",
 "prompt": "Give the Ancient Greek etymology of κύστις 'bladder'. Does it derive from PIE *kʷes- / *ḱwes- 'to pant, breathe'? What does Beekes say? List cited sources and any alternative proposals."
}
```


### [2026-09-06T22:21:22.812Z] TOOL RESULT

```
# Ancient Greek Etymology of κύστις (Bladder)

## Stated Etymology

According to the Wiktionary entry, κύστις derives from **Proto-Indo-European *\(s\)kewH-** meaning "to cover," or alternatively from **κύω (kúō)**.

## Regarding PIE *kʷes-/*ḱwes-

The provided sources do **not** mention the PIE root *kʷes-/*ḱwes- ('to pant, breathe'). The etymology presented focuses exclusively on *(s)kewH-* as the primary derivation.

## Beekes' Analysis

The webpage contains **no reference** to Beekes or his etymological proposals for this word.

## Cited Sources

The entry references:
- Liddell & Scott (1940) *A Greek–English Lexicon*
- Liddell & Scott (1889) *An Intermediate Greek–English Lexicon*
- Autenrieth (1891) *A Homeric Dictionary for Schools and Colleges*
- Bailly (1935) *Le Grand Bailly: Dictionnaire grec-français*
- Cunliffe (1924) *A Lexicon of the Homeric Dialect*
- Pokorny (1959) *Indogermanisches etymologisches Wörterbuch*

None of these sources are quoted directly regarding κύστις's etymology in the provided content.
```


### [2026-09-06T22:21:22.938Z] TOOL RESULT

```
# Proto-Iranian *cušíH (Lungs)

**Proto-Iranian Form:** *cušíH (dual)

**Gloss:** "lungs"

**Etymology:**
The term derives from Proto-Indo-Iranian *ćušíH, which traces back to Proto-Indo-European *ḱus-íh₁(e), the dual form of *ḱus-í-s ~ *ḱus-éy-s. This combines the root *ḱwes- ("to puff, sigh") with the suffix *-is.

**Major Descendants:**

- **Avestan:** suši (feminine dual)
- **Middle Persian:** swš (suš)
- **Persian:** شش (šuš); Dari and Tajik cognates exist
- **Pashto:** سږى (sëģay)
- **Kurdish:** Central Kurdish sî; Northern Kurdish sîh; Southern Kurdish/Laki variants süye/süe
- **Ossetian:** Digor сос (sos); Iron сус (sus)

The word also appears in Khotanese, Gurani, Shahrudi, and several other Iranian language branches.

**References:**
Citations include de Vaan (2003), Kroonen (2013), and Kümmel (2016), documenting this reconstruction across Central, Northeastern, Southeastern, Northwestern, and Southwestern Iranian language groups.
```


## [2026-09-06T22:21:32.273Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cyst",
 "prompt": "Give the full etymology of \"cyst\" and of \"quarrel\" (n., dispute) and \"wheeze\" if present. Quote the PIE roots given."
}
```


## [2026-09-06T22:21:33.393Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/quarrel",
 "prompt": "Give the full etymology of \"quarrel\" (noun, dispute) — Old French, Latin querela, queri, and the PIE root cited."
}
```


### [2026-09-06T22:21:36.561Z] TOOL RESULT

```
# Etymology Requested

Based on the provided content, I can only offer information about **cyst**:

**Cyst (n.):** First recorded in 1713, deriving from Modern Latin *cystis* (used in English since the 1540s), which came from Greek *kystis* meaning "bladder, pouch." The source notes the Greek origin is of "uncertain etymology." The relevant PIE root mentioned is *ghel-* (2), meaning "to shine," with derivatives indicating colors like green and yellow, and by extension, bile.

**Quarrel** and **wheeze** are not discussed in the provided webpage content, so I cannot supply their etymologies based on this source material.
```


### [2026-09-06T22:21:39.369Z] TOOL RESULT

```
# Etymology of "Quarrel" (Noun, Dispute)

**Old French Origin:**
From Old French *querele* meaning "dispute, controversy," which evolved into Modern French *querelle*.

**Latin Source:**
The Old French term derives directly from Latin *querella*, defined as "complaint, accusation; lamentation."

**Verbal Root:**
Latin *querella* stems from the verb *queri*, meaning "to complain, lament."

**Proto-Italic:**
The Latin *queri* traces back to Proto-Italic *\*kwese-*, whose etymology remains uncertain.

**PIE Root:**
The proto-language ancestor is theorized as PIE *\*kues-*, possibly meaning "to hiss" (from a notion of sighing). This root also appears in Sanskrit *svasiti* ("to hiss, snort"), though scholars acknowledge this etymology as "not very compelling" with no superior alternative currently established.

**Historical Development:**
The noun entered Middle English around the mid-14c. with the sense of "dispute, altercation," and by the 1570s had developed the modern meaning of "angry contention between persons."
```


## [2026-09-06T22:21:46.711Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1wes-",
 "prompt": "Give the reconstruction entry for PIE *ḱwes-: gloss, derived terms, descendants by branch (Indo-Iranian, Italic, Germanic, Balto-Slavic), and whether Latin queri and Greek kustis are included."
}
```


## [2026-09-06T22:21:48.935Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hw%C5%8Dsan",
 "prompt": "Is hwōsan an Old English verb? Give its meaning, etymology (Proto-West Germanic / Proto-Germanic form), cognates including Old Norse hvæsa, and the descendant Modern English \"wheeze\". Is there any Old Norse word \"hwosan\"?"
}
```


### [2026-09-06T22:21:51.123Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:21:53.657Z] TOOL RESULT

```
# Proto-Indo-European *ḱwes- Entry

**Gloss:** The root means "to puff, sigh" according to the Wiktionary reconstruction entry.

**Derived Terms:** The entry shows numerous formations including:
- Athematic root present (*ḱwés-ti ~ *ḱus-énti)
- Narten-type present (*ḱwḗs-ti ~ *ḱwés-n̥ti)
- Zero-grade ye-present (*ḱus-yé-ti)
- Eye-causative (*ḱwos-éye-ti)

**Descendants by Branch:**

- **Indo-Iranian:** Sanskrit *śvasiti* ("to breathe"), Pashto *suṇ* ("panting, wheezing")
- **Italic:** Latin *queror* ("to complain")
- **Germanic:** Old English *hyssan*, Proto-Germanic *hwēsaną* ("to wheeze")
- **Balto-Slavic:** Lithuanian *švankšti* ("to wheeze")
- **Armenian:** Old Armenian *šunčʻ* ("breath; spirit; wind")

**Note on Greek:** The entry does not mention Greek *kystis*. Latin *queror* is included as a thematized derivative (*kwesō).
```


## [2026-09-06T22:22:04.357Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hw%C4%93san%C4%85",
 "prompt": "Give the Proto-Germanic *hwēsaną entry: gloss, etymology (PIE root), and descendants — specifically which language has hwōsan and which has hvæsa. Is hwōsan Old English and hvæsa Old Norse?"
}
```


### [2026-09-06T22:22:09.469Z] TOOL RESULT

```
# Proto-Germanic *hwēsaną Entry

**Gloss:** "to wheeze"

**Etymology:** Derived from Proto-Indo-European *ḱwes- ("to pant"), with Latin queror as a cognate.

**Descendants:** The entry shows only one documented descendant line:
- Proto-West Germanic: *hwāsan
  - Old English: hwǣsan
    - Middle English: whesen
      - English: wheeze

**Regarding your specific questions:** The provided content does not include forms like *hwōsan* or *hvæsa*, nor does it mention Old Norse descendants. The page only traces the word through the West Germanic branch, ending with modern English "wheeze."
```


## [2026-09-06T22:22:27.169Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T22:22:27.213Z] TOOL RESULT

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


## [2026-09-06T22:22:28.750Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG kues/swas ===\"; grep -n -i \"\\*cuš\\|suši\\|śwas\\|\\*swah\\|swas-\" CHEUNG.txt | head -10; echo \"=== IEC kues ===\"; grep -n -i \"kues-\\|kuesi\\|quesor\" IEC.txt | head -10"
}
```


### [2026-09-06T22:22:28.826Z] TOOL RESULT

```
=== CHEUNG kues/swas ===
11959:*IE COGNATES: Gr. oo, OCS sušiti, Lith. satisti, Latv. sust ‘to become dry’, OEngl. 
24078:Iranian ’lung(s)’ words may also derive from the root *suah: Y Av. suši (du.), BMP 
33754:suši, 369 
=== IEC kues ===
9241:Kueio (Kuueióo, Kuueiio) ‘teem, swell Skt. $Sváyami ‘swell, increase’ beside $üye, mp. ‘swell’; Gk. kuéo, kúo “contain; be pregnant (fr. *&uueijo; Kuuio); Koos, n. ‘foetus’, küma, n. ‘swell, surge’; Lat. cf. fre-quens, -quentis (abounding'. For *ku- > Lat. qu-, cf. Kues- Lat. quer-or; a zero-gde form is possible in L. -cundus as in fe-, jü-cundus, etc.); Cor. cf. coey, v. ‘to foal; Sw. cf. (?) hyende, n. ‘pillow’; zero-gde in OCS sytü 'sated' beside Skt. Sunah ‘swollen’
9244:Kuel- (2) ‘whizz, whistle". WP I, 473 and cf. Kues-, Kuesl-
9265:Kueso, io ‘whistle, whizz, wheeze, shriek’. Tokh. B. kwas-, v. ‘lament’; Skt. $vasimi ‘hiss, pant'; Oss. (?) cf. cass, Dig. casä “opening, hole’; Gk. cf. seiren, gs. -énos ('siren, bee, wasp, beetle’, fr. *Kuesrien- or *Kuesrjan-); Lat. queror, queri, questus ‘warble, chirp, sing; wail’; Ir. ceasaim ‘grieve, complain’; long-gde in ON hvasa, Sw. hvàsa “hiss? (E wheeze derives apparently fr. OE hwosan, with initial as above. An apparent isophone occurs in Gk. seíros “hot, searing’, fr. *Kues- rios?)
```


## [2026-09-06T22:22:36.980Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24070,24090p' CHEUNG.txt; echo \"=== cheung 33754 ctx ===\"; sed -n '33750,33758p' CHEUNG.txt"
}
```


### [2026-09-06T22:22:37.039Z] TOOL RESULT

```
*suaH 369 


*SANSKRIT: Svas ‘to bluster, hiss, snort? (RV, AV+) = EWAia П: 677 

9 It is uncertain whether the Chor. form s’s- has other cognates: it may well have an 
(internal) expressive/onomatopoetic origin. The initial consonant group *su appears 
to yield sp in Chor., rather than s (hence: s’s- is the result of assimilation ?). The 
Iranian ’lung(s)’ words may also derive from the root *suah: Y Av. suši (du.), BMP 
sws, Khot. suv’ä (orig. du. ?), NP sus, Sh. sus, etc. 

«PIE *Kues- ‘to snort, hiss’ — LIV: 341 | Pok.: 631 f. 

*IE COGNATES: Lat. queror ‘I complain’, Toch. B kwäs- ‘to lament, mourn’, ON 
hvosa ‘to hiss, snort’, OE hwösan ‘to cough, gasp’ 

*REFERENCES: EVS: 72; DKS: 428a f.; Werba 1997: 421 f.; Adams 1999: 237; NEVP: 74 


*suaH ‘to move, throw, erect’ 
*AVESTAN: YAv. spa- ‘to throw’ || (+ *apa-) ‘to throw away, let go’ || (+ *api-) ‘to 
=== cheung 33754 ctx ===
star-, star-, 364 
Stor-, stri-, star-, 363 
stij-, 361 

suši, 369 


sü-, sáuu-, 341 
su-ka-, 29
```


## [2026-09-06T22:22:48.379Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9200 && NR<=9270 && /^[0-9]{3,4}$|page [0-9]+/ {print NR\": \"$0}' IEC.txt | tail -5; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /Kueso, io/{print \"rec \"NR; print substr($0,1,120)}' IEC.txt | head -5"
}
```


### [2026-09-06T22:22:50.210Z] TOOL RESULT

```
9205: 645
9224: 646
9235: 647
9258: 648
9267: 649
---
rec 367
s; OHG (?) hwint, OFris, hwind ('greyhound'. Hence G Wind- hund); OCS (and com. Sl.) svetü ‘holy’; Li. Svefitas, id
```


## [2026-09-06T22:23:00.328Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1wes-\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CF%83%CF%84%CE%B9%CF%82\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hw%C4%93san%C4%85\" \\\n \"https://www.etymonline.com/word/cyst\" \\\n \"https://www.etymonline.com/word/quarrel\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 294, root Kwes: verification of suši/suš/šoš, havâ, kustis/cyst, queri/quarrel, hwosan\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T22:23:05.340Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/45bfcf25854c8f39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cbbab2079061d68a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/546c9be78d12daf2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/141771c24a4ff645.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4865988acdc5562e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ba772146d28fe4c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/850c614a1f7f59dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/935d144baefa4522.txt
```


## [2026-09-06T22:23:12.502Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM هواء ===\"; grep -n \"هواء\\|الهواء\" AFM.txt | head -5; echo \"=== PLA hawa ===\"; grep -n -i \"hawāʾ\\|hawa'\\|هواء\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5; echo \"=== LKT hawa ===\"; grep -n -i \"hawa\" LKT.txt | head -5; echo \"=== FVQ hawa ===\"; grep -n -i \"hawa\" FVQ.txt | head -5"
}
```


### [2026-09-06T22:23:12.582Z] TOOL RESULT

```
=== AFM هواء ===
752:05225 غرض في الهواء على رأس رمح او نوه فارسيتها برجاس ومعناما 
5640:من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء 
=== PLA hawa ===
=== LKT hawa ===
582:'ümsonst,  gratis'  [Kelekian  233  b,  wohl aus  ar.  bädi-hawä  'Luft  verursachend'] ; hieraus  bulg.  badihawa,  badlawa  'dass.', serb.  badawad  'dass.',  slov.  badava  und mit  slav.  Präposition  zabadava  'verge- bens, umsonst'.    [Bern  SlEtWb  37.
2541:bei  hoher  Glut  'Stahl' ;  hieraus  russ.  (alt) hawalug  'dass.'.  [Gorjajew  135.  Bern SlEtWb  385  u.  488.
5525:badem  154 badiawa  160 badihawa  160 badzeica  625 Z>afca  169 bayr(anica)  1349 bag%n  1349 &aj6afc  181 iö/Zr  348 irtiraÄ;  182 bakalija  189 fcaÄ's/s  178 bakzr  193 buldahin  170 6a^Ä;on  197 balsani  293 6«Zte  207 hat•as^k  258
=== FVQ hawa ===
7186:jl-lo- (Hawaii). 
7404:j AI j 1 *>- (Hawanyun) . 
7415:ad-Dahhak that Hawanyun moans washermen in Nabataean." 7
```


## [2026-09-06T22:23:13.264Z] TOOL CALL #75: WebSearch

```json
{
 "query": "Beekes Etymological Dictionary Greek κύστις kustis bladder etymology Pre-Greek kuo"
}
```


### [2026-09-06T22:23:21.830Z] TOOL RESULT

```
Web search results for query: "Beekes Etymological Dictionary Greek κύστις kustis bladder etymology Pre-Greek kuo"

Links: [{"title":"Reconstruction:Proto-Indo-European/(s)kewH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-"},{"title":"Beekes Etymological Dictionary Greek","url":"https://www.scribd.com/document/698401131/Beekes-Etymological-Dictionary-Greek"},{"title":"κύστις - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CF%83%CF%84%CE%B9%CF%82"},{"title":"cysto- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/cysto-"},{"title":"Etymological Dictionary of Greek Online","url":"https://dictionaries.brillonline.com/greek"},{"title":"Robert S. P. Beekes","url":"https://en.wikipedia.org/wiki/Robert_S._P._Beekes"},{"title":"κύστιον - Wiktionary","url":"https://en.wiktionary.org/wiki/κύστιον"},{"title":"κύστη - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CF%83%CF%84%CE%B7"},{"title":"Beekes - Etymological Dictionary of Greek | PDF","url":"https://www.scribd.com/document/371380654/Beekes-Etymological-Dictionary-of-Greek"},{"title":"Beekes' Etymological Dictionary of Greek - Learning Greek - Textkit Greek and Latin","url":"https://www.textkit.com/t/beekes-etymological-dictionary-of-greek/15376"}]

I've found relevant information about the Beekes Etymological Dictionary of Greek and the etymology of κύστις (kustis, "bladder").

Based on the search results, κύστις (kustis) has been proposed to derive from Proto-Indo-European *(s)kewH- ("to cover") or from κῡ́ω (kŭ́ō). Additionally, Ancient Greek κύστις (kústis, "bladder") can be explained with *(s)kewH-tis, or alternatively from *ḱewh₁-.

Regarding Beekes' approach to etymology, in cases where a word can be proven to be of Pre-Greek origin, the Etymological Dictionary sometimes retains old reasoning to illustrate the flaws in the traditional approach, according to which practically every word is bound to have an Indo-European etymology. This reflects Beekes' proclivity towards Pre-Greek etymologies, which some scholars have noted are "contentious."

The search results show both Indo-European and Pre-Greek etymological possibilities for κύστις, reflecting the complexity of Greek etymology as treated in Beekes' dictionary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T22:23:34.532Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%A7%D8%A1",
 "prompt": "Give the Arabic etymology of هَوَاء (hawāʾ) \"air\": the root, the related verb هوى (hawā), Semitic cognates, and descendants (including Persian هوا, Turkish hava, Urdu). Quote any cited sources."
}
```


## [2026-09-06T22:23:36.969Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB cyst ===\"; grep -n -o -i \"cyst,.\\{0,300\\}\" WEB_vol1.txt | head -3; echo \"=== FSD cyst ===\"; grep -n -o -i \"cyst .\\{0,250\\}\\|cyst,.\\{0,250\\}\" FSD_vol1.txt | head -3; echo \"=== KLN hawa/air arabic ===\"; grep -n -i \"Arab\\. hawā\\|hawa,\\|'air'.*Arab\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T22:23:42.012Z] TOOL RESULT

```
# Etymology of هَوَاء (hawāʔ) "Air"

## Root and Meaning
The word derives from the Semitic root **ه و ي** (h w y). According to the source, this root originally meant "a hole or hollow, a depression or declivity, a valley or chasm, hence the empty space or air that fills them."

## Primary Definitions
The noun **هَوَاء** (hawāʔ) carries multiple meanings:
1. Air (uncountable)
2. Atmosphere (uncountable)
3. Empty space, vacancy, void

## Descendants
This Arabic term spread extensively across languages:

**Persian:** هوا (havâ)
**Turkish:** hava (via Ottoman Turkish)
**Urdu:** ہوا (havā)

The word also entered numerous other languages including Indonesian, Malay, Kurdish, Tajik, Uzbek, and various Caucasian and South Asian languages, demonstrating the widespread influence of Arabic vocabulary through trade and cultural contact.

The Wiktionary entry lists over 50 descendant languages, reflecting Arabic's historical linguistic impact across the Mediterranean, Middle East, Central Asia, and South Asia.
```


### [2026-09-06T22:23:44.114Z] TOOL RESULT

```
=== WEB cyst ===
1996:cyst, n. (Gr. akephalos, headless, and kystis, bladder.) a headless larval tape-
3868:cyst, n. [aero-, and Gr. kystis, bladder.] an air cell or air bladder of an alga.
32014:cyst, cest, a jesti t n: L. cista; Gr. kiste, a box, chest.] 1. a box provided with a lid and, some- times, a lock; as, tool chest, treasure chest. 2. a box for the safe transportation of
=== FSD cyst ===
5879:cyst,  n.  Helminth.
6293:cyst,  n. An  encysted  larval  tapeworm  or  hydatid.—  a-ceph"a-Io- cys'tlc,  a. —   a-cepfi'a-Io-gas^tcr,  n.  A   monster  lacking head,  chest,' and  upper  part  of  abdomen.—  a-ceph"a-lo- gas-te'rl-a,  n.  Tcrat.  Absence  of  head,  chest,  and  
6901:cyst,  n.  Zooph.  An  ex- ternal sac  formed  on  the  summit  of  a   bydrold  gonanglum and  serving  as  the  receptacle  of  ova.—  ac"ro-dac’fcy-luin, n.  [-la,  pi. 1   [Rare.]  Qrnith.  The  upper  surface  of  a   toe.
=== KLN hawa/air arabic ===
17888:hawwdh ,  ‘tent-village,  village’,  which  prob.  de¬ rives  fr.  base  h-w-h,  ‘to  gather’,  and  is  rel.  to Arab,  hawa,  ‘he  collected,  gathered’,  hiwa\ ‘circle  of  tents’.
```


## [2026-09-06T22:24:10.651Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%A7%D8%A1\" --note \"page 294, node #4 havâ: Arabic hawāʾ root h-w-y, Persian هوا is a loan from it\" 2>&1 | tail -2\nmkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg294_p294.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/294.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/294.png"
}
```


### [2026-09-06T22:24:12.734Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1bfb0f2872133ee7.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 36312 Sep  6 18:24 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/294.png
```


## [2026-09-06T22:29:02.897Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk294.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 294,\n \"book_page\": 264,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kwes\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱwes- 'to puff, sigh, wheeze' (Pokorny 631-632 k̑u̯es-, k̑us-; LIV 341)\",\n   \"note\": (\n     \"The root is real and Nourai's gloss is right. Pokorny IEW 631-632 has the lemma \"\n     \"'k̑u̯es-, k̑us- : to puff, sigh', with exactly Nourai's material: Skt. śvasiti 'breathes, \"\n     \"wheezes, sighs', Av. suši 'both lungs', Lat. queror, Old Icelandic hvæsa, OE hwōsan, \"\n     \"Lith. sušinti. Walde-Pokorny I 474 f. has the same set under '*ḱues- keuchen, schnaufen, \"\n     \"seufzen'. Watkins/AHD prints the root as 'kwes-, to pant, wheeze', which is the shape \"\n     \"Nourai copied ('Kwes'). One qualification: because Skt. ś- and Av./Ir. s- require a \"\n     \"PALATAL *ḱ, the modern reconstruction (LIV 341, Cheung 369, Wiktionary, Kümmel 2016) is \"\n     \"*ḱwes-, not the labiovelar *kʷes- that AHD's spelling suggests; the labiovelar of Lat. \"\n     \"queror is exactly why Ernout-Meillet and de Vaan doubt the Latin member (see node #7). \"\n     \"Pokorny himself calls the -es- extension 'meist schallnachahmenden Ursprungs' \"\n     \"(mostly onomatopoeic). The verdict is confirmed for the root; the two branches that do \"\n     \"not belong are Persian havâ (#4, an Arabic loan) and Greek kustis (#5).\"\n   ),\n   \"note_fa\": (\n     \"ریشهٔ «Kwes» نزد نورایی همان ریشهٔ هندواروپایی آغازین *ḱwes- «دمیدن، نفس‌زدن، خس‌خس کردن» \"\n     \"است که پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صفحهٔ ۶۳۱ـ۶۳۲ با همین معنی و با همین \"\n     \"شواهد (سنسکریت śvasiti، اوستایی suši «دو شش»، لاتینی queror، ایسلندی کهن hvæsa، انگلیسی \"\n     \"کهن hwōsan) آورده است؛ والده‌ـ‌پوکورنی جلد ۱ ص ۴۷۴ نیز همین را دارد. تنها نکته آن است که \"\n     \"چون «ش» سنسکریت و «س» ایرانی از کام‌گونهٔ *ḱ می‌آید، ریشه‌شناسی امروزی (LIV ۳۴۱، چونگ ۳۶۹، \"\n     \"ویکی‌واژه) آن را *ḱwes- می‌نویسد نه *kʷes- که املای واتکینز/AHD (و به‌تبع آن نورایی) القا \"\n     \"می‌کند. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ اما دو شاخهٔ «هوا» و «kustis» یونانی به آن \"\n     \"تعلق ندارد.\"\n   ),\n   \"sources\": [\n     W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1wes-\",\n     W + \"Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH\",\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:631\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt (Pokorny IEW), 'Page(s): 631-632': \\\"Root/lemma: k̑ues-, k̑us- … Meaning: to puff, sigh. Material: Old Indic śvasiti …, Avestan suši 'both lungs'; Latin queror, -ī, questus sum 'to express grief, complain'…; lengthened grade Old Icelandic hvæsa, Old English hwōsan 'pant, gasp'; Lithuanian sušinti… References: WP. I 474 f., WH. II 403 f.\\\" — exactly Nourai's root, gloss and (with one language label wrong, see #9) his branches.\"},\n     {\"ref\": \"CEL6:284\", \"status\": \"not_checked\",\n      \"note\": \"S. K. Gupta, A Comparative Etymologic Lexicon of Common IE Words, vol. 6 — refs_online.json marks CEL as 'catalog only'; no copy online or on disk, so p. 284 could not be read.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I 474 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt line 29869 ff.)\", \"stance\": \"supports\",\n      \"note\": \"\\\"*ḱues- 'keuchen, schnaufen, seufzen'. Ai. śvásiti …, av. suši 'die beiden Lungen' …; lat. queror, questus sum 'klagen' …; dehnstufig aisl. hvǣsa, ags. hwǣsan 'keuchen'\\\" — the same root with the same members; Walde-Pokorny too has no Greek kustis here.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kwes- (AHD_watkins1985.txt line 652)\", \"stance\": \"supports\",\n      \"note\": \"\\\"kwes-. To pant, wheeze. 1. Germanic *hwēsjan in Old Norse hvæsa, to hiss: WHEEZE. 2. Latin queri, to complain: QUARREL¹, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< 'bellows'): CYST, CYSTO-. [Pok. kues- 631.]\\\" — this single AHD entry is the direct source of Nourai's #5, #6, #7, #8 and #9; note that AHD's Germanic member is Old NORSE hvæsa, not 'hwosan'.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, col. 648 s.v. Kʷeso, io\", \"stance\": \"supports\",\n      \"note\": \"\\\"Kʷeso, io 'whistle, whizz, wheeze, shriek'. Tokh. B kwäs- 'lament'; Skt. śvasimi 'hiss, pant'; … Lat. queror, queri, questus …; long-gde in ON hvāsa, Sw. hvåsa 'hiss' (E wheeze derives apparently fr. OE hwōsan…)\\\" — same root; Mann labels hwōsan Old English.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck §4.51 BREATHE, p. 260\", \"stance\": \"supports\",\n      \"note\": \"\\\"Skt. çvas-, çvāsa-: Av. suši- 'the lungs', Lat. querī 'lament, bewail', ON hvæsa, OE hwēsan 'pant', etc. Walde-P. 1.474.\\\"\"},\n     {\"src\": \"CHEUNG\", \"where\": \"p. 369, root *swaH\", \"stance\": \"partial\",\n      \"note\": \"Cheung files the Iranian material under his verbal root *swaH and adds: \\\"The Iranian 'lung(s)' words may also derive from the root *swaH: YAv. suši (du.), BMP swš, Khot. suvʾä (orig. du.?), NP sus, Sh. sus, etc.\\\", with \\\"PIE *ḱues- 'to snort, hiss' — LIV: 341 | Pok.: 631 f.\\\" — same root, but written with a palatal ḱ.\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"suši, suš\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Avestan suš- f., attested only in the dual suši 'the two lungs' (Frahang ī ōīm; Bartholomae \"\n   \"AiW col. 1586-1587 'suš- f., Du. \\\"Lungen\\\": °si'). Formally it is the PIE i-stem *ḱus-i-s, \"\n   \"dual *ḱus-ih₁(e), built on the zero grade of *ḱwes- 'to puff' — the lungs named as the \"\n   \"'bellows/panters', the same image Borhan-e Qate' still uses in Persian (بادزن و مروحهٔ دل \"\n   \"'the fan and bellows of the heart'). PIE *ḱ gives Indo-Iranian *ć, hence Proto-Iranian \"\n   \"*cušíH (Skt. has the matching root śvas-). Nourai's chart gives two forms in the box, \"\n   \"suši and suš: suši is the actually attested Avestan dual, suš is Bartholomae's stem \"\n   \"citation-form (and the Pahlavi form); both are legitimate, so the node is confirmed.\"\n ),\n \"derivation_fa\": (\n   \"«suši» اوستایی، مادّهٔ suš- و در متن تنها به صورت مثنّای suši «دو شش» (فرهنگ اویم) به کار \"\n   \"رفته است؛ بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۵۸۶ آن را چنین آورده: «suš- مؤنث، مثنّی: \"\n   \"Lungen». از نظر ساخت، ستاکی است بر پایهٔ *ḱus-i- (درجهٔ صفر ریشهٔ *ḱwes-)، یعنی «دمنده، \"\n   \"دم‌زننده»؛ همان تصویری که برهان قاطع هنوز با تعبیر «بادزن و مروحهٔ دل» برای شش به کار می‌برد. \"\n   \"کام‌گونهٔ *ḱ هندواروپایی در هندوایرانی به *ć و در ایرانی به s بدل شده است (ایرانی آغازین \"\n   \"*cušíH). ادعای نورایی درست است.\"\n ),\n \"sources\": [W + \"Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH\", W + \"%D8%B4%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"POK:631\", \"status\": \"supports\",\n    \"note\": \"Pokorny 631: \\\"Avestan suši 'both lungs'\\\" stands in the Material of the lemma k̑ues- itself (POK_full.txt line 52205 ff.).\"},\n   {\"ref\": \"SYN:260\", \"status\": \"supports\",\n    \"note\": \"Buck, Selected Synonyms, §4.51 'BREATHE', p. 260 (SYN.txt line 6732): \\\"Skt. çvas-, çvāsa-: Av. suši- 'the lungs', Lat. querī 'lament, bewail', ON hvæsa, OE hwēsan 'pant', etc.\\\" — Buck derives the Avestan lung-word from the breathe-root, as Nourai does.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1586-1587 s.v. suš- (BRT.txt line 26437)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j. suš- f., Du. 'Lungen': °si F. 3b … — mp. (Pahl.) suš, np. šuš, kurd. …\\\" — Bartholomae himself draws Nourai's whole Iranian chain (Av. → Pahl. → NP) in one line.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 474\", \"stance\": \"supports\",\n    \"note\": \"\\\"av. suši 'die beiden Lungen'\\\" listed directly under *ḱues-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 369 (root *swaH)\", \"stance\": \"supports\",\n    \"note\": \"\\\"The Iranian 'lung(s)' words may also derive from the root *swaH: YAv. suši (du.), BMP swš, Khot. suvʾä, NP sus…\\\" with \\\"PIE *ḱues- 'to snort, hiss'\\\".\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p. 378, headword شُش SHOSH 'LUNG'\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's cognate list for شش gives \\\"SUSHI (AVESTAN)\\\" under the root \\\"*KUESH-, *KUS-, *KWES-\\\" — an independent modern Persian cross-check of the same arrow.\"}\n ]\n})\n\nN.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"suš\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Book Pahlavi swš = suš 'lung' continues the Avestan/Old Iranian *cuši- unchanged: the \"\n   \"Old Iranian short *u stays, the dual is lost and the word is reinterpreted as a singular. \"\n   \"MacKenzie, Concise Pahlavi Dictionary p. 78, lists it exactly so: \\\"¹suš [swš | (N šus)] \"\n   \"lung\\\" — with the New Persian outcome already noted in the same entry, which is precisely \"\n   \"Nourai's #2 → #3 arrow. The word is attested in the Zoroastrian Pahlavi literature that \"\n   \"Nourai's reference SNS (the Šāyast nē-šāyast glossary) indexes.\"\n ),\n \"derivation_fa\": (\n   \"«suš» فارسی میانه (نوشتار swš) دنبالهٔ بی‌واسطهٔ صورت ایرانی باستان *cuši- است؛ در گذر از \"\n   \"ایرانی باستان به پهلوی مقولهٔ مثنّی از میان رفته و واژه مفرد شده، اما پیکرهٔ آوایی دست‌نخورده \"\n   \"مانده است. مکنزی در «فرهنگ کوچک پهلوی» ص ۷۸ می‌نویسد: «¹suš [swš | (N šus)] lung» و در همان \"\n   \"مدخل صورت فارسی نو را هم می‌آورد؛ یعنی درست همان پیکانی که نورایی از پهلوی به فارسی کشیده \"\n   \"است. ادعای نورایی درست است.\"\n ),\n \"sources\": [W + \"%D8%B4%D8%B4\", W + \"Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:192\", \"status\": \"supports\",\n    \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast nē-šāyast: the glossary's index (SNS.txt lines 29045, 31145) gives \\\"sus 192/5\\\" and \\\"sus- 192/6\\\", and the entry itself (SNS.txt lines 11564-11565) shows the Pahlavi headword followed by \\\"(AiW 1586) suš-\\\" — i.e. p. 192 glosses Pahlavi sus 'lung' and refers it to Bartholomae's Avestan suš-, exactly Nourai's arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 78 (PHD.txt line 572)\", \"stance\": \"supports\",\n    \"note\": \"\\\"¹suš [swš | (N šus)] lung.\\\" — Pahlavi form, meaning and the New Persian reflex all as in the chart. (MacKenzie also has a homograph \\\"*suš [stwš] degree (of arc)\\\", unrelated.)\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'suš'/'sus ' in NYB_vol2_glossary.txt returns only \\\"Sus [šws] Susa\\\" (the city) and unrelated words; Nyberg's glossary covers his selected texts only and has no lung-word.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p. 378 s.v. شُش\", \"stance\": \"supports\",\n    \"note\": \"cognate list gives \\\"SHUSH, SUSH (PAHLAVI)\\\" between Avestan SUSHI and Persian شُش; reference box cites \\\"MACKENZIE: (LUNG) 122\\\".\"}\n ]\n})\n\nN.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"šoš\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"New Persian شُش šoš/šuš 'lung' < Middle Persian suš, with one small extra step that \"\n   \"Hübschmann isolated: the initial s- was assimilated to the final -š. Hübschmann, Persische \"\n   \"Studien no. 784 (p. 80): \\\"Np. šuš 'Lunge' aus suš mit Assimilation des Anlautes an den \"\n   \"Auslaut\\\" — i.e. s…š > š…š, the ordinary Persian sibilant harmony also seen in šeš 'six' \"\n   \"beside Pahl. šaš. Horn, Grundriss no. 784 (p. 173) sets out the same chain: \\\"šuš 'Lunge'. \"\n   \"Aw. suši 'Lunge'; phlv. suš; ai. vergl. √śvas-, śvasiti 'schnaufen'\\\". Mo'in's etymological \"\n   \"footnote in Borhan-e Qate' (fn. 6 to p. 1266, printed on p. 1267) gives \\\"اوستا sushi … \"\n   \"سانسکریت çvas (دمیدن) … پهلوی sush … بعربی آنرا ریه گویند\\\". The Persian script شُش in the \"\n   \"JSON matches both the printed page and Aryanpur's headword.\"\n ),\n \"derivation_fa\": (\n   \"«شُش» فارسی نو از فارسی میانهٔ suš است، با یک دگرگونی کوچک که هوبشمان آن را بازشناخته: \"\n   \"«س» آغازین به «ش» پایانی همگون شده است — هوبشمان، «مطالعات فارسی» شمارهٔ ۷۸۴ (ص ۸۰): \"\n   \"«np. šuš 'Lunge' aus suš mit Assimilation des Anlautes an den Auslaut». همین همگونیِ \"\n   \"سایشی‌ها را در «شش» (عدد) در برابر šaš پهلوی هم می‌بینیم. هرن در «مبانی ریشه‌شناسی فارسی نو» \"\n   \"شمارهٔ ۷۸۴ (ص ۱۷۳) همین زنجیره را می‌آورد: «šuš 'شش'؛ اوستایی suši؛ پهلوی suš؛ سنسکریت √śvas-». \"\n   \"معین نیز در حاشیهٔ برهان قاطع (پانویس ۶ صفحهٔ ۱۲۶۶ که در ص ۱۲۶۷ چاپ شده) می‌نویسد: «اوستا \"\n   \"sushi … سانسکریت çvas (دمیدن) … پهلوی sush … بعربی آنرا ریه گویند». پس ادعای نورایی درست \"\n   \"است و املای «شُش» نیز با متن چاپی می‌خواند.\"\n ),\n \"sources\": [W + \"%D8%B4%D8%B4\", W + \"Reconstruction:Proto-Iranian/cu%C5%A1%C3%ADH\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:173\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 784, printed p. 173 (HRN.txt, form-feed record 195, header '— 173 —'): \\\"784. šuš 'Lunge'. … aw. suši 'Lunge' (ZPGl.); phlv. suš; ai. vergl. √śvas-, śvasiti 'schnaufen' … afγ. saγai; wax. LW. šifs, sar. sül.\\\" — Nourai's page is exact.\"},\n   {\"ref\": \"BQT:1266\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1266 (vol. 3 pdf p. 57; page image saved as data/verification/sources/refs/ocr/BQT/1266.png, transcription in 1266.vision.txt). The page opens the section شین/شین and has: \\\"شش … وضم اول چیزیست سفید بسرخی مایل مانند گوشت وبجگر متصل است ⁶ وبادزن ومروحهٔ دل باشد\\\" (with a woodcut of a pair of lungs). Footnote 6 is continued on p. 1267: \\\"اوستا sushi، افغانی xâush «استق ۷۸۳»، … سانسکریت çvas (دمیدن) «هوبشمان ۷۸۴»، پهلوی sush …\\\" — Mo'in's own etymology is Nourai's chain, citing Horn and Hübschmann.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 784, p. 80 (HUB.txt line 2801)\", \"stance\": \"supports\",\n    \"note\": \"\\\"784. Np. šuš 'Lunge' aus suš mit Assimilation des Anlautes an den Auslaut. Wenn suš = zd. suši- = afgh. saγai 'Lunge' zu skr. śvas gehört, kann es nicht auch zu (dem unsichern) *šukṣi- gehören.\\\" — supplies the exact sound change for the Pahlavi → New Persian step.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1586-1587\", \"stance\": \"supports\",\n    \"note\": \"\\\"suš- f., Du. 'Lungen' … mp. (Pahl.) suš, np. šuš, kurd. …\\\" — Bartholomae ends the entry with the New Persian form.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp. 378-379, headword «شُش» SHOSH\", \"stance\": \"supports\",\n    \"note\": \"Headword \\\"SHOSH — فارسی (PERSIAN) شُش | LUNG | *KUESH-, *KUS-, *KWES- (INDO-EUROPEAN)\\\", with SUSHI (Avestan), SHUSH/SUSH (Pahlavi), SAZHAI/SAGHÁI (Pashto), PISHIK (Kurdish); reference box: POKORNY 631-632, BARNHART (WHEEZE) 1230, MACKENZIE (LUNG) 122, MALLORY & ADAMS, برهان قاطع ۱۲۶۷.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in's etymological footnote in BQT, p. 1266 fn. 6 (printed p. 1267)\", \"stance\": \"supports\",\n    \"note\": \"\\\"۶ ـ اوستا sushi … گیلکی shish، تهرانی shish. سانسکریت çvas (دمیدن) «هوبشمان ۷۸۴»، پهلوی sush، افغانی saghai، وخی shush، سریکلی sül … بعربی آنرا ریه (رئه) گویند.\\\" (transcribed to data/verification/sources/refs/ocr/BQT/1267.vision.txt)\"}\n ]\n})\n\nN.append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"havâ\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Persian هوا havâ 'air, weather' is not an Iranian word at all and has nothing to do with \"\n   \"*ḱwes-. It is a straightforward Arabic loan: Arabic هَوَاء hawāʾ 'air, atmosphere, empty \"\n   \"space', a maṣdar-type noun of the Semitic root ه-و-ي (h-w-y) whose base sense is 'a hollow, \"\n   \"a chasm, a declivity — hence the empty space that fills it' (cf. the verb هوى hawā 'to fall, \"\n   \"to drop down'). It entered Persian with the Arabic lexical wave after the 7th-century \"\n   \"conquest and spread on from Persian and Arabic to Ottoman Turkish hava, Urdu ہوا, Kurdish, \"\n   \"Tajik, Malay and dozens of other languages. No Iranist derives it from an inherited root: \"\n   \"there is no Middle Persian *hawā, and the Old Iranian word for 'air/wind' is vāta- (NP bâd). \"\n   \"Nourai's only support here is CEL6:284 (Gupta), which is not accessible and is not a \"\n   \"standard authority; Pokorny, Walde-Pokorny, AHD, Horn, Hübschmann and Bartholomae all \"\n   \"list no Persian air-word under this root. Nourai has evidently been misled by the \"\n   \"accidental resemblance of hav- to the root's 'breathe/puff' sense.\"\n ),\n \"derivation_fa\": (\n   \"«هوا» در فارسی واژه‌ای ایرانی نیست و هیچ پیوندی با ریشهٔ *ḱwes- ندارد. این واژه معرَّب نیست، \"\n   \"بلکه وام‌واژه‌ای است از عربی هَوَاء «هوا، جوّ، فضای تهی»، از ریشهٔ سامی «ه‌ـ‌و‌ـ‌ی» که معنای \"\n   \"پایه‌اش «گودی، پرتگاه، درّه و در نتیجه فضای تهیِ درون آن» است (قس. فعل هَوَی «فروافتادن»). \"\n   \"این واژه پس از فتح ایران در سدهٔ نخست هجری همراه انبوه وام‌واژه‌های عربی وارد فارسی شد و از \"\n   \"فارسی و عربی به ترکی عثمانی hava، اردو ہوا، کردی، تاجیکی و ده‌ها زبان دیگر رفت. در فارسی \"\n   \"میانه صورتی چون *hawā وجود ندارد و واژهٔ ایرانی باستانِ «باد/هوا» vāta- است. تنها مأخذ \"\n   \"نورایی در اینجا CEL6:284 (گوپتا) است که نه در دسترس است و نه از مراجع معتبر؛ پوکورنی، \"\n   \"والده‌ـ‌پوکورنی، واتکینز، هرن، هوبشمان و بارتولومه هیچ‌یک واژه‌ای فارسی به معنی «هوا» زیر این \"\n   \"ریشه ندارند. پژوهش امروزی ادعای نورایی را رد می‌کند.\"\n ),\n \"sources\": [W + \"%D9%87%D9%88%D8%A7\", W + \"%D9%87%D9%88%D8%A7%D8%A1\"],\n \"ref_check\": [\n   {\"ref\": \"CEL6:284\", \"status\": \"not_checked\",\n    \"note\": \"Gupta, Comparative Etymologic Lexicon vol. 6 — no copy online or on disk (refs_online.json: 'catalogue only'), so the page could not be read. It is in any case the only reference Nourai offers for this arrow, and no standard work supports it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, s.v. hawwāh etc. (KLN_1966.txt line 17888)\", \"stance\": \"silent\",\n    \"note\": \"Klein has no English word from Arabic hawāʾ 'air'; grep for 'Arab. hawā'/'air … Arab' in KLN_1966.txt returns only the unrelated Semitic base h-w-h 'to gather' (hawwāh 'tent-village'). Nothing links hawāʾ to an IE root.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep 'hawa'/'هواء' in PLA_asbaghi_1988_ia_djvu.txt finds nothing — Asbaghi's dictionary of PERSIAN loans in Arabic does not contain هواء, i.e. the borrowing does not run in that direction.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\",\n    \"note\": \"the two hits for الهواء in AFM.txt (lines 752, 5640) are incidental uses inside other entries (birjās, marble); Addi Shir does not list هواء among the Persian words arabicised, which he would have if it were Iranian.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'ān\", \"stance\": \"silent\",\n    \"note\": \"no entry: grep 'hawā'/'هواء' in FVQ.txt returns only the proper names Hawāʾī/Hawānīyūn. Jeffery treats hawāʾ as native Arabic, not a foreign word.\"}\n ]\n})\n\nN.append({\n \"id\": 5,\n \"lang\": \"Greek\",\n \"words\": \"kustis\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Ancient Greek κύστις kústis 'bladder, pouch, bag' really exists with that meaning (Hippocrates, \"\n   \"Aristotle onwards), so the word and gloss are right; what is wrong is the parentage. Nourai \"\n   \"follows Watkins/AHD, who put it here as a \\\"suffixed zero-grade form *kus-ti- … (< 'bellows')\\\", \"\n   \"and Klein repeats the same guess (\\\"Gk. κύστις … prob. cogn. with OI. śvásati … L. queri\\\"). \"\n   \"But Pokorny 631-632 and Walde-Pokorny I 474 f. — the very pages Nourai cites for the root — do \"\n   \"NOT list κύστις under the root at all, and modern Greek etymology has abandoned the connection: \"\n   \"Etymonline (following Beekes) calls κύστις 'of uncertain etymology', and Wiktionary derives it \"\n   \"either from PIE *(s)kewH- 'to cover' (*(s)kewH-tis, i.e. the same base as Latin cutis, English \"\n   \"hide) or from κύω 'to be pregnant, swell' — both of which suit 'bladder, sac' better than \"\n   \"'panting'. The phonology is a further obstacle: since the root is palatal *ḱwes- (Skt. ś-, \"\n   \"Av. s-), a Greek reflex should show σ-, not κ-. The arrow is therefore rejected by current \"\n   \"scholarship, though it was standard in the 1966-1985 dictionaries Nourai used.\"\n ),\n \"derivation_fa\": (\n   \"واژهٔ یونانی باستان κύστις «مثانه، کیسه» به‌راستی وجود دارد و معنایش همان است که در نمودار \"\n   \"آمده؛ اشکال در نسب‌نامهٔ آن است. نورایی از واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American \"\n   \"Heritage) پیروی کرده که آن را «صورت پسوندیِ درجهٔ صفر *kus-ti-، یعنی دَم/کوره» زیر همین ریشه \"\n   \"می‌آورد و کلاین نیز همین حدس را تکرار می‌کند. اما پوکورنی (ص ۶۳۱ـ۶۳۲) و والده‌ـ‌پوکورنی (جلد ۱ \"\n   \"ص ۴۷۴) — همان صفحه‌هایی که نورایی برای ریشه ارجاع می‌دهد — اصلاً κύστις را زیر این ریشه \"\n   \"نیاورده‌اند، و ریشه‌شناسی امروزیِ یونانی این پیوند را کنار گذاشته است: اتیمانلاین (به پیروی \"\n   \"از بیکس) آن را «با ریشه‌شناسی نامعلوم» می‌خواند و ویکی‌واژه یا از *(s)kewH- «پوشاندن» (همان \"\n   \"پایهٔ cutis لاتینی) یا از κύω «آبستن بودن، آماسیدن» می‌گیرد. افزون بر این، چون ریشه کام‌گونه \"\n   \"(*ḱwes-) است، بازتاب یونانی آن باید σ- باشد نه κ-. پژوهش امروزی این پیکان را رد می‌کند.\"\n ),\n \"sources\": [W + \"%CE%BA%CF%8D%CF%83%CF%84%CE%B9%CF%82\", \"https://www.etymonline.com/word/cyst\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. kwes-: \\\"3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< 'bellows'): CYST, CYSTO-.\\\" — Nourai's cited reference does say exactly this; it is later scholarship that disagrees.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 631-632, lemma k̑ues-\", \"stance\": \"contradicts\",\n    \"note\": \"the Material lists Old Indic, Avestan, Latin, Old Icelandic, Old English and Lithuanian — no Greek word at all; κύστις is absent from the root.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 474 f.\", \"stance\": \"contradicts\",\n    \"note\": \"same members as Pokorny, no Greek; Walde-Pokorny place the Greek κύ-/κυ- 'swell' family elsewhere.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cyst (KLN_1966.txt line 10133)\", \"stance\": \"supports\",\n    \"note\": \"\\\"cyst, n. … Medical L. cystis, fr. Gk. κύστις, 'bladder, bag, pouch', which is prob. cogn. with OI. śvásati, śvásiti, 'blows, breathes, sighs', L. queri, 'to complain'. See quarrel, 'dispute'.\\\" — Klein (1966) holds Nourai's view, hedged with 'prob.'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, col. 645-648 (Kʷeio 'teem, swell' vs Kʷeso)\", \"stance\": \"partial\",\n    \"note\": \"Mann puts Gk. κυέω, κύω 'be pregnant, swell', κῦμα under Kʷeio 'teem, swell' and keeps κύστις out of his Kʷeso 'wheeze' entry — i.e. he agrees with the modern κύω-family placement rather than with AHD.\"}\n ]\n})\n\nN.append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"cyst\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"The arrow Greek κύστις → English cyst is correct and uncontroversial, whatever the ultimate \"\n   \"root: κύστις 'bladder, pouch' was taken into scientific Latin as cystis, used in English from \"\n   \"the 1540s in that Latin shape and anglicised to cyst by 1713 in medical writing ('a closed \"\n   \"membranous sac containing fluid'); the combining forms cysto-/-cyst (cholecyst, nematocyst) \"\n   \"follow. Only the ultimate parentage is doubtful (see #5): if κύστις is not from *ḱwes-, then \"\n   \"cyst is not either. The node has no reference of its own in the book; it hangs on the AHD \"\n   \"citation of its parent.\"\n ),\n \"derivation_fa\": (\n   \"پیکان «κύστις یونانی ← cyst انگلیسی» درست و بی‌مناقشه است: κύστις «مثانه، کیسه» به لاتین علمی \"\n   \"به صورت cystis راه یافت، از دههٔ ۱۵۴۰ در انگلیسی به همان شکل لاتینی به کار می‌رفت و در ۱۷۱۳ در \"\n   \"متون پزشکی به صورت cyst انگلیسی شد؛ ترکیب‌های cysto-/-cyst (مانند cholecyst) نیز از همین‌جاست. \"\n   \"تنها نسب نهاییِ خودِ واژهٔ یونانی مورد تردید است (نک. گرهٔ ۵). این گره در کتاب مأخذی ندارد و به \"\n   \"ارجاع AHD در گرهٔ مادرش تکیه دارد.\"\n ),\n \"sources\": [\"https://www.etymonline.com/word/cyst\", W + \"%CE%BA%CF%8D%CF%83%CF%84%CE%B9%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"—\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book (refs=None); the parent Greek node's AHD citation covers it (\\\"Greek kustis … : CYST, CYSTO-\\\").\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cyst (KLN_1966.txt line 10133)\", \"stance\": \"supports\",\n    \"note\": \"\\\"cyst, n., a closed membranous pouch or sac containing fluid (med.) — Medical L. cystis, fr. Gk. κύστις, 'bladder, bag, pouch'.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Cyst (SKT.txt line 4622)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Cyst, a pouch (in animals) containing morbid matter. (L. – Gk.) Formerly written cystis. — Late L. cystis. — Gk. κύστις, a bag, pouch.\\\" — Skeat, like Etymonline, gives no IE root beyond the Greek.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., s.v. cyst (WEB_vol1.txt lines 1996, 3868)\", \"stance\": \"supports\",\n    \"note\": \"\\\"cyst, n. [… Gr. kystis, bladder.]\\\" — the Greek etymon only.\"}\n ]\n})\n\nN.append({\n \"id\": 7,\n \"lang\": \"Latin\",\n \"words\": \"queri\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Latin queror, querī, questus sum 'to utter plaintive cries, to complain, lament' (Plautus, \"\n   \"Cicero; obsolete after the 1st c. CE) is put under this root by Pokorny 631 (\\\"Latin queror … \"\n   \": Old Indic śvasati\\\"), Walde-Pokorny I 474, Watkins/AHD, Klein and Wiktionary, which \"\n   \"reconstructs a thematised *kʷes-o-. The semantic step is 'to gasp, sigh' > 'to lament'. But \"\n   \"the connection is not secure and Nourai's chart presents it as settled. Ernout-Meillet, \"\n   \"Dictionnaire étymologique de la langue latine s.v. queror, state plainly: \\\"Le rapprochement \"\n   \"usuel avec skr. śvásiti 'il souffle fort' n'est pas pleinement satisfaisant: les sens ne \"\n   \"concordent pas d'une manière exacte, et le latin n'a pas trace du caractère dissyllabique de \"\n   \"la racine, net en sanskrit. Le verbe latin est assez isolé.\\\" De Vaan (via Etymonline) likewise \"\n   \"calls the etymology 'not very compelling', though no better one exists. A third difficulty is \"\n   \"phonological: Latin qu- points to a labiovelar *kʷ, while Skt. ś- / Av. s- require a palatal \"\n   \"*ḱ. Hence 'plausible' rather than 'confirmed'.\"\n ),\n \"derivation_fa\": (\n   \"فعل لاتینی queror, querī «نالیدن، شکایت کردن» (پلاوتوس، سیسرون؛ پس از سدهٔ نخست میلادی از کاربرد \"\n   \"افتاد) را پوکورنی (ص ۶۳۱)، والده‌ـ‌پوکورنی (جلد ۱ ص ۴۷۴)، واتکینز، کلاین و ویکی‌واژه زیر همین \"\n   \"ریشه می‌آورند و ویکی‌واژه صورت *kʷes-o- را بازسازی می‌کند؛ تحول معنایی از «نفس‌زدن، آه کشیدن» به \"\n   \"«نالیدن» است. اما این پیوند قطعی نیست: ارنو و مِیه در «فرهنگ ریشه‌شناختی زبان لاتینی» می‌نویسند \"\n   \"«مقایسهٔ رایج با śvásiti سنسکریت کاملاً رضایت‌بخش نیست: معناها دقیقاً بر هم منطبق نیستند و در \"\n   \"لاتینی نشانی از دوهجایی بودنِ ریشه — که در سنسکریت آشکار است — دیده نمی‌شود؛ فعل لاتینی نسبتاً \"\n   \"منزوی است». دِ‌فان نیز آن را «چندان متقاعدکننده نیست» می‌خواند. اشکال آوایی هم هست: qu- لاتینی \"\n   \"بر لب‌کامیِ *kʷ دلالت دارد حال آنکه śـ سنسکریت و sـ ایرانی کام‌گونهٔ *ḱ می‌خواهد. پس ادعای نورایی \"\n   \"با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [\"https://www.etymonline.com/word/quarrel\", W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1wes-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. kwes-: \\\"2. Latin queri, to complain: QUARREL¹, QUERULOUS.\\\" — Nourai's citation is accurate.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 631\", \"stance\": \"supports\",\n    \"note\": \"\\\"Latin queror, -ī, questus sum 'to express grief, complain, lament, bewail' (: Old Indic śvasati)\\\" stands in the Material of the root.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL s.v. queror (LAT.txt line 51898 ff.)\", \"stance\": \"partial\",\n    \"note\": \"\\\"Le rapprochement usuel avec skr. çvásiti 'il souffle fort' n'est pas pleinement satisfaisant … Le sens de 'pousser un sifflement' se retrouve dans v.isl. hvæsa, v.angl. hwǣsan. Le verbe latin est assez isolé.\\\" — accepts the Germanic side of the root but doubts the Latin membership.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 648 s.v. Kʷeso, io\", \"stance\": \"supports\",\n    \"note\": \"\\\"Lat. queror, queri, questus 'warble, chirp, sing; wail'\\\" listed with Skt. śvasimi and Tokh. B kwäs-.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. quarrel 'dispute' (KLN_1966.txt line 31328)\", \"stance\": \"supports\",\n    \"note\": \"\\\"L. querela … fr. queri, 'to complain', which is prob. cogn. with OI. śvásati, śvásiti, 'blows, breathes, sighs', OE. hwǣsan, 'to wheeze'.\\\"\"}\n ]\n})\n\nN.append({\n \"id\": 8,\n \"lang\": \"English\",\n \"words\": \"quarrel\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"The Latin → English chain is certain: Latin querī 'to complain' → the deverbal noun querēla \"\n   \"(older) / querella 'complaint, accusation, lamentation' → Old French querele 'dispute, \"\n   \"controversy' (Mod.Fr. querelle) → Middle English quarel, querele, first in the sense 'dispute, \"\n   \"altercation' in the mid-14th century, narrowing to 'angry contention between persons' by the \"\n   \"1570s; the verb to quarrel follows partly from OF quereler. Klein's entry gives exactly this \"\n   \"route. (This quarrel must be kept apart from the homonym quarrel 'crossbow bolt, diamond-shaped \"\n   \"pane', which is from ML quadrellus, dimin. of quadrus 'square' — a different root, *kʷetwer- \"\n   \"'four'; Nourai's chart has the right one.) Like #6, this node carries no reference of its own.\"\n ),\n \"derivation_fa\": (\n   \"زنجیرهٔ لاتینی تا انگلیسی در اینجا قطعی است: querī لاتینی «شکایت کردن» ← اسم فعلی querēla/querella \"\n   \"«شکایت، ناله» ← فرانسهٔ کهن querele «نزاع، مشاجره» (فرانسهٔ امروز querelle) ← انگلیسی میانه \"\n   \"quarel/querele که از میانهٔ سدهٔ چهاردهم به معنی «نزاع» به کار رفت و تا دههٔ ۱۵۷۰ به معنی امروزی \"\n   \"«ستیز میان اشخاص» محدود شد؛ فعل to quarrel نیز تا اندازه‌ای از quereler فرانسهٔ کهن است. کلاین \"\n   \"دقیقاً همین مسیر را می‌آورد. (این واژه را نباید با هم‌آوای آن quarrel «تیر کمان‌ زنبورکی، شیشهٔ \"\n   \"لوزی» اشتباه گرفت که از quadrellus لاتینی میانه، مصغّرِ quadrus «چهارگوش»، و از ریشهٔ *kʷetwer- \"\n   \"«چهار» است؛ نمودار نورایی همان واژهٔ درست را برگزیده است.) این گره در کتاب مأخذی ندارد.\"\n ),\n \"sources\": [\"https://www.etymonline.com/word/quarrel\"],\n \"ref_check\": [\n   {\"ref\": \"—\", \"status\": \"not_checked\",\n    \"note\": \"no reference printed on this node (refs=None); the parent Latin node's AHD citation names QUARREL¹ explicitly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. quarrel, n., dispute (KLN_1966.txt line 31328)\", \"stance\": \"supports\",\n    \"note\": \"\\\"quarrel, n., dispute. — ME. quarel, quarelle, querele, fr. OF. querele (F. querelle), fr. L. querela, also querella, 'complaint', fr. queri, 'to complain' … Cp. also cyst.\\\"\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. kwes-\", \"stance\": \"supports\",\n    \"note\": \"index line \\\"QUARREL¹ kwes-\\\" and \\\"QUERULOUS kwes-\\\" (AHD_watkins1985.txt line 2146, 2149), against \\\"QUARREL² kʷetwer-\\\" for the crossbow bolt — confirming which homonym belongs here.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, list of qu- words from *kʷetwer- (SKT.txt line 22837)\", \"stance\": \"partial\",\n    \"note\": \"Skeat groups 'quarrel' among the words traced to the 'four' family, i.e. he indexes the bolt-homonym; his entry does not contradict the querī derivation of the dispute-word.\"}\n ]\n})\n\nN.append({\n \"id\": 9,\n \"lang\": \"Old Norse\",\n \"words\": \"hwosan\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"Old Norse ⌷ CEL6:286 | hwosan : puff\",\n \"correct_form\": \"Old English hwōsan 'to cough, pant, gasp' (the Old Norse cognate is hvæsa / hvōsa 'to hiss')\",\n \"derivation\": (\n   \"The verb is real and does belong to the root, but the language label is wrong, and the printed \"\n   \"page (pdf 294 = book p. 264, image kept at data/verification/sources/refs/ocr/BOOK/294.png) \"\n   \"shows 'Old Norse' in the box, so the error is the book's, not the extraction's. Every source \"\n   \"makes hwōsan Old English: Pokorny 631 \\\"lengthened grade Old Icelandic hvæsa, Old English \"\n   \"hwōsan 'pant, gasp'\\\"; Walde-Pokorny I 474 \\\"aisl. hvǣsa, ags. hwǣsan 'keuchen'\\\"; Buck §4.51 \"\n   \"\\\"ON hvæsa, OE hwēsan 'pant'\\\"; Mann col. 648 \\\"long-gde in ON hvāsa, Sw. hvåsa 'hiss' (E wheeze \"\n   \"derives apparently fr. OE hwōsan)\\\"; Cheung p. 369 \\\"ON hvōsa 'to hiss, snort', OE hwōsan 'to \"\n   \"cough, gasp'\\\"; Aryanpur p. 379 lists \\\"HVASA — OLD SCANDINAVIAN\\\" and \\\"HWŌSAN, HWAST — OLD \"\n   \"ENGLISH\\\" in two separate rows. Morphology decides it too: an infinitive in -an is West \"\n   \"Germanic; Old Norse infinitives end in -a. Phonetically OE hwōsan continues Proto-Germanic \"\n   \"*hwēs-/*hwōs- with Grimm's Law *ḱw > *hw and lengthened-grade vocalism; the sister form OE \"\n   \"hwǣsan gives Middle English whesen > Modern English wheeze. So: the derivation from *ḱwes- is \"\n   \"confirmed, but 'Old Norse' should read 'Old English' (or the word should read hvæsa).\"\n ),\n \"derivation_fa\": (\n   \"خودِ فعل واقعی است و به این ریشه تعلق دارد، اما برچسب زبانِ آن نادرست است؛ و چون در صفحهٔ چاپی \"\n   \"(صفحهٔ ۲۹۴ پی‌دی‌اف = ص ۲۶۴ کتاب، تصویر در data/verification/sources/refs/ocr/BOOK/294.png) نیز \"\n   \"«Old Norse» چاپ شده، خطا از کتاب است نه از خوانش اسکن. همهٔ منابع hwōsan را انگلیسی کهن \"\n   \"می‌دانند: پوکورنی ص ۶۳۱ «ایسلندی کهن hvæsa، انگلیسی کهن hwōsan»؛ والده‌ـ‌پوکورنی جلد ۱ ص ۴۷۴ \"\n   \"«aisl. hvǣsa، ags. hwǣsan»؛ باک بند ۴٫۵۱ «ON hvæsa، OE hwēsan»؛ مان ستون ۶۴۸؛ چونگ ص ۳۶۹ «ON \"\n   \"hvōsa … OE hwōsan»؛ و آریان‌پور ص ۳۷۹ که HVASA را «ایسلندی کهن» و HWŌSAN را «انگلیسی کهن» در دو \"\n   \"سطر جداگانه آورده است. ساخت واژه هم گواه است: مصدرِ پایان‌یافته به -an ژرمنی باختری است و مصدر \"\n   \"نورس کهن به -a ختم می‌شود. از نظر آوایی hwōsan دنبالهٔ ژرمنی آغازین *hwōs-/*hwēs- است با تبدیل \"\n   \"*ḱw > *hw بر پایهٔ قانون گریم، و صورت خواهرش OE hwǣsan به انگلیسی میانه whesen و انگلیسی امروز \"\n   \"wheeze رسیده است. پس ریشه‌شناسی درست است ولی «Old Norse» باید «Old English» می‌بود: خطای چاپی \"\n   \"کتاب.\"\n ),\n \"sources\": [\n   W + \"Reconstruction:Proto-Germanic/hw%C4%93san%C4%85\",\n   W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1wes-\"\n ],\n \"ref_check\": [\n   {\"ref\": \"CEL6:286\", \"status\": \"not_checked\",\n    \"note\": \"Gupta CEL vol. 6 p. 286 — no copy online or on disk (refs_online.json: 'catalogue only'). Since the mislabel is Nourai's only support here, it cannot be traced to the source; but every accessible authority (POK, WLD, SYN, IEC, CHEUNG, ARY) calls hwōsan Old English.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 631, lemma k̑ues-\", \"stance\": \"partial\",\n    \"note\": \"\\\"lengthened grade Old Icelandic hvæsa, Old English hwōsan 'pant, gasp'\\\" — the root membership supports Nourai, the language label contradicts him.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 648 s.v. Kʷeso, io\", \"stance\": \"partial\",\n    \"note\": \"\\\"long-gde in ON hvāsa, Sw. hvåsa 'hiss' (E wheeze derives apparently fr. OE hwōsan, with initial as above)\\\" — Mann separates the ON and the OE form explicitly.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 369, IE cognates of *swaH\", \"stance\": \"partial\",\n    \"note\": \"\\\"IE COGNATES: Lat. queror 'I complain', Toch. B kwäs- 'to lament, mourn', ON hvōsa 'to hiss, snort', OE hwōsan 'to cough, gasp'\\\" — two different languages, two different forms.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p. 379 (cognate list of شُش)\", \"stance\": \"contradicts\",\n    \"note\": \"two separate rows: \\\"ایسلندی کهن (OLD SCANDINAVIAN): HVASA\\\" and \\\"انگلیسی کهن (OLD ENGLISH): HWŌSAN, HWAST\\\", then \\\"انگلیسی (ENGLISH): WHEEZE\\\".\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.51, p. 260\", \"stance\": \"partial\",\n    \"note\": \"\\\"ON hvæsa, OE hwēsan 'pant'\\\" — again the -n form is the English one.\"}\n ]\n})\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-294.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk294.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-294.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 294"
}
```


### [2026-09-06T22:29:07.637Z] TOOL RESULT

```
ok 9
JSON OK
nodes verified: 9/9
node verdicts: {'confirmed': 5, 'disputed': 2, 'plausible': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'not_checked': 4}
books consulted: {'supports': 19, 'silent': 5, 'contradicts': 3, 'partial': 7} | by book: {'KLN': 5, 'ARY': 4, 'POK': 3, 'IEC': 3, 'BRT': 2, 'WLD': 2, 'CHEUNG': 2, 'SKT': 2, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'MON': 1, 'PLA': 1, 'AFM': 1, 'FVQ': 1, 'WEB': 1, 'LAT': 1, 'AHD': 1, 'SYN': 1}
```


## [2026-09-06T22:29:30.753Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-294.json` written; `verify_check.py 294` reports 9/9 nodes, **0 PROBLEM lines**.

**PDF page 294 (book p. 264) — one entry, root "Kwes" (IE, "to pant, to breathe fast")**

Verdicts: root confirmed; nodes 5 confirmed, 1 plausible, 2 disputed, 1 transcription_suspect.
Ref checks: 7 supports, 4 not_checked (all CEL = Gupta, catalogue-only, unobtainable).

- **disputed — #4 Persian havâ هوا "air"**: not Iranian at all; a plain Arabic loan (هَوَاء hawāʾ, root ه‑و‑ي "hollow/chasm → the empty space in it"). No MP *hawā; the inherited Iranian word is vāta- > bâd. Asbaghi, Addi Shir, Jeffery, Klein all silent; Nourai's only support is the unavailable CEL6:284.
- **disputed — #5 Greek kustis "bladder"**: Watkins/AHD (Nourai's cited ref) and Klein do put it here as *kus-ti- "bellows", but Pokorny 631‑632 and Walde‑Pokorny I 474 — the very pages cited for the root — omit Greek entirely; Etymonline (after Beekes) says "of uncertain etymology" and Wiktionary derives it from *(s)kewH- "cover" or κύω "swell". Palatal *ḱwes- would also give Greek σ-, not κ-. (#6 cyst still confirmed as an arrow.)
- **transcription_suspect — #9 "Old Norse hwosan 'puff'"**: `error_in: "book"`. The printed page really prints "Old Norse" (page PNG saved to `data/verification/sources/refs/ocr/BOOK/294.png`), so the extraction is faithful. But hwōsan is **Old English** (Pokorny 631, Buck §4.51, Mann col. 648, Cheung 369, Aryanpur 379 all label it OE; an ‑an infinitive is West Germanic). Old Norse has hvæsa/hvōsa.
- **plausible — #7 Latin queri**: in Pokorny/WLD/AHD/Klein/Wiktionary, but Ernout‑Meillet ("le rapprochement usuel … n'est pas pleinement satisfaisant … le verbe latin est assez isolé") and de Vaan/Etymonline ("not very compelling") dissent; qu- needs *kʷ while Skt ś-/Av s- need *ḱ.
- The Iranian spine **#1 suši → #2 suš → #3 šoš شش** is fully confirmed and unusually well documented: Bartholomae AiW col. 1586 draws the whole chain in one line; MacKenzie p. 78 "¹suš [swš | (N šus)] lung"; Horn no. 784 p. 173 (Nourai's HRN:173 exact); Hübschmann no. 784 p. 80 supplies the sound change (s…š > š…š by assimilation); Borhan-e Qate' p. 1266 (verified against the page image — Nourai's BQT:1266 is exact) with Mo'in's footnote 6 printed on p. 1267.

**No extraction errors found** — the JSON matches the printed page in every box, including the script شُش.

New artefacts: `refs/ocr/BQT/1266.vision.txt`, `refs/ocr/BQT/1267.vision.txt`, `refs/ocr/BOOK/294.png`, and 9 archived web sources.
