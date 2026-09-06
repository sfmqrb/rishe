# Verification process log — verify-page-208


## [2026-09-06T14:51:49.982Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 208 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-208.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-208.json. Write /home/sfmqrb/git/rishe/data/verification/page-208.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 208` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:51.149Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:51.834Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:51.850Z] TOOL RESULT

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


## [2026-09-06T14:51:52.443Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-208.txt"
}
```


### [2026-09-06T14:51:52.466Z] TOOL RESULT

```
1	=== PDF page 208 (book page 178) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwen 1, Gwenâ, Gwŭnâ : woman, female  (refs POK:473)
4	#1 (parent #0) [Avestan] refs=POK:473; SYN:82 | ğnâ, genâ, žaini, jâni : woman
5	  #2 (parent #1) [Persian] refs=POK:473; BQT:1033 | zan «زن» : woman, wife
6	#3 (parent #0) [Sanskrit] refs=POK:473 | gnâ, gunâ, jani, kan, kanya : woman
7	#4 (parent #0) [Germanic] refs=AHD | kweniz : woman
8	  #5 (parent #4) [English] refs=None | queen
9	#6 (parent #0) [Greek] refs=None | gune : woman
10	  #7 (parent #6) [Latin] refs=None | 
11	    #8 (parent #7) [English] refs=None | gyno-, gynecology
12	--- entry 1 ---
13	ROOT Gwen 2 -> redirect to Gwa
14	--- entry 2 ---
15	ROOT Gwenâ -> redirect to Gwen 1
16	--- entry 3 ---
17	ROOT [Indo-European] Gwer 1 : heavy  (refs POK:476)
18	#1 (parent #0) [Avestan] refs=POK:476 | gouru : heavy
19	  #2 (parent #1) [Persian] refs=BQT:1781; MON:3214 | gerân «گران» : heavy, expensive
20	#3 (parent #0) [Latin] refs=AHD | gravis : heavy
21	  #4 (parent #3) [English] refs=None | grave : serious ; gravity, grief
22	#5 (parent #0) [Greek] refs=AHD | barus : heavy ; baros : weight
23	  #6 (parent #5) [French] refs=None | 
24	    #7 (parent #6) [Persian] refs=MON:451,452 |  | extra: باریم ، بارومتر
25	  #8 (parent #5) [English] refs=None | barium, barometer
26	
```


## [2026-09-06T14:51:56.106Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-208.json",
 "description": "Read source JSON for page 208"
}
```


### [2026-09-06T14:51:56.152Z] TOOL RESULT

```
{
  "pdf_page": 208,
  "book_page": 178,
  "entries": [
    {
      "root": {
        "name": "Gwen 1, Gwenâ, Gwŭnâ",
        "lang": "Indo-European",
        "refs": "POK:473",
        "gloss": "woman, female"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:473; SYN:82",
          "words": [
            {"translit": "ğnâ, genâ, žaini, jâni", "gloss": "woman", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:473; BQT:1033",
          "words": [
            {"translit": "zan", "gloss": "woman, wife", "script": "زن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:473",
          "words": [
            {"translit": "gnâ, gunâ, jani, kan, kanya", "gloss": "woman", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kweniz", "gloss": "woman", "script": null}
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
            {"translit": "queen", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "gune", "gloss": "woman", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": null,
          "words": [],
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
            {"translit": "gyno-, gynecology", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwen 2",
        "redirect": "Gwa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwenâ",
        "redirect": "Gwen 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwer 1",
        "lang": "Indo-European",
        "refs": "POK:476",
        "gloss": "heavy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:476",
          "words": [
            {"translit": "gouru", "gloss": "heavy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1781; MON:3214",
          "words": [
            {"translit": "gerân", "gloss": "heavy, expensive", "script": "گران"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سینه تنگ من و بار غم او ، هیهات - مرد این بار گران نیست دل مسکینم",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "gravis", "gloss": "heavy", "script": null}
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
            {"translit": "grave", "gloss": "serious", "script": null},
            {"translit": "gravity, grief", "gloss": null, "script": null}
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
            {"translit": "barus", "gloss": "heavy", "script": null},
            {"translit": "baros", "gloss": "weight", "script": null}
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
          "refs": "MON:451,452",
          "words": [],
          "script_extra": "باریم ، بارومتر",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "barium, barometer", "gloss": null, "script": null}
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


## [2026-09-06T14:51:56.762Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && head -80 data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix head"
}
```


### [2026-09-06T14:51:56.819Z] TOOL RESULT

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
----
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
```


## [2026-09-06T14:52:11.184Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','BQT','MON','AHD','BRT','PHD','HRN','HUB','KLN','WLD','IEC','SKT','ARY','NYB','SOD','LEW','LAT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\"",
 "description": "Show refs_online entries"
}
```


## [2026-09-06T14:52:11.961Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-205.json",
 "description": "Sample recent verification file"
}
```


### [2026-09-06T14:52:14.150Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-06T14:52:14.192Z] TOOL RESULT

```
{
  "pdf_page": 205,
  "book_page": 175,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Gwei",
      "verdict": "confirmed",
      "modern_form": "PIE *gʷeyh₃- (Pokorny 'gʷei-3, gʷeiə-, gʷii̯ē-, gʷi̯ō-, gʷī-, frequent, often with -u̯- extended') 'to live'",
      "note": "The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended. Meaning: to live', with 'Page(s): 467-469', so Nourai's 'Gwei : to live' with POK:467 reproduces Pokorny's own heading and page; Watkins in the AHD appendix has 'gʷei-. Also gʷeiə-. To live ... [Pok. 3. gʷei- 467]'; Wiktionary reconstructs *gʷeyh₃- 'to live' (alternative *gʷyeh₃-); Cheung, for the Iranian verb, writes '*jaiH2 ... «PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f.'. What is striking about this chart is how much of it is simply Pokorny's own article rearranged: pages 467-469 contain, in order, Avestan gaya- and gaēθā-/Old Persian gaiθā, Avestan jīti- and jīra-, Old Persian jīva-/Avestan jva-, Greek bios, zōḗ, zōion and hygiḗs, Latin vīvus/vīvō/vīta, and Old English cwicu / OHG queh — that is, every branch of the page except the modern coinages. Klein's article 'quick' (p.1288, Nourai's own citation on node 1) carries the same set in one paragraph. Three things need qualifying rather than correcting: the Avestan citation forms in node 1 ('jîta', 'merezu-jîta' for jīti-, mərəzu-jīti-/-jva-); the gloss 'to exist' given to the noun gaēθā- in node 8; and the presence of two 19th/20th-century neologisms ('mikro-bios' in the Greek box, 'vitamine' in the French box) among inherited words. Everything on the Iranian side — zīwistan/zīwandag → زیستن/زنده/ژیوه, the Arabic round trip زیبق, gayō.marətan- → کیومرث, gaēθanąm → gēhān → گیتی/کیهان/جهان, jīra- → زیرک/آژیر — checks out against Horn, Hübschmann, MacKenzie, Nyberg, Bartholomae, Asbaghi and Moʿin's footnotes on the very Borhān pages Nourai cites.",
      "note_fa": "جعبهٔ ریشه از هر سه جهت درست است: پوکورنی مادّهٔ «gʷei-3 و gʷeiə-…» را با معنای «زیستن» در صفحات ۴۶۷–۴۶۹ آورده، پس هم صورت و هم برچسبِ زبان و هم معنا و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است؛ واتکینز نیز همین را می‌گوید و ویکی‌واژه آن را *gʷeyh₃- بازسازی می‌کند و چونگ در فرهنگِ فعلِ ایرانی ذیل *jaiH₂ همین ریشه را می‌آورد. نکتهٔ چشمگیر این است که بیشترِ نمودار در واقع بازچینشِ همان مقالهٔ پوکورنی است: اوستایی gaya- و gaēθā-، پارسی باستان gaiθā، jīti- و jīra-، jīva-/jva-، یونانی bios و zōḗ و hygiḗs، لاتین vīvus و vīta، و انگلیسی کهن cwicu همه در همان سه صفحه‌اند. سه نکته باید روشن شود، نه اصلاح: صورت‌های اوستاییِ گرهٔ ۱ («jîta» به‌جای jīti-)، معنای نادرستِ «to exist» برای اسمِ gaēθā- در گرهٔ ۸، و حضورِ دو نوواژهٔ سدهٔ نوزدهم و بیستم (mikro-bios و vitamine) در کنارِ واژه‌های موروثی. تمامِ بخشِ ایرانیِ نمودار — از zīwistan تا «زیستن» و «زنده» و «ژیوه»، چرخهٔ «زیبق»، gayō.marətan- تا «کیومرث»، gaēθanąm تا «گیهان/گیتی/کیهان/جهان»، و jīra- تا «زیرک/آژیر» — با هرن، هوبشمان، مکنزی، نیبرگ، بارتولمه، اصباغی و حواشیِ معین بر همان صفحاتِ برهانِ قاطع که نورایی ارجاع داده می‌خواند.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-"
      ],
      "ref_check": [
        {
          "ref": "POK:467",
          "status": "supports",
          "note": "POK_full.txt lines 38677-38790: 'Root / lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended || Meaning: to live || Material: A. from *gʷei-: Old Indic jīvatu-ḥ \"life\", gaya-ḥ \"house, courtyard\" ... Avestan gaēθā, Old pers. gaiθā \"entity, house and courtyard\" ... References: WP. I 668 ff. ... Page(s): 467-469.' Exactly the root box as drawn."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, IE roots appendix s.v. gʷei- (AHD_watkins1985.txt line 540)",
          "stance": "supports",
          "note": "'gʷei-. Also gʷeiə-. To live. I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- ... [Pok. 3. gʷei- 467.]' — the same root, gloss and Pokorny page."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 668-669 (WLD_Bd1_pages.txt leaves 676-677, running head 'gʷei(ə)-')",
          "stance": "supports",
          "note": "the source article that Pokorny 467 abridges, with the Germanic and Greek material set out at length ('mhd. verquīnen ... ags. cwīnan ... got. qistjan')."
        },
        {
          "src": "KLN",
          "where": "Klein 1966 p.1288 s.v. quick",
          "stance": "supports",
          "note": "'fr. I.-E. *gwigwos, fr. base *gwei-, \"to live\", whence Goth. *qius ... OI. jivah ... Avestic jvaiti ... OPers. jiva- ... Gk. bios ... zōē ... L. vivus ... vita ... OIr. bith, W. byd, \"world\" ... Cp. also zodiac, zoetic, zoo-.'"
        },
        {
          "src": "CHEUNG",
          "where": "Etymological Dictionary of the Iranian Verb, *jaiH2, p.223",
          "stance": "supports",
          "note": "'«PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f. *IE COGNATES: Lat. vivo, OCS živǫ, Lith. gyju, Latv. dzīvu \"I live\", Toch. śaw- \"to live\"'."
        },
        {
          "src": "SYN",
          "where": "Buck, Dictionary of Selected Synonyms",
          "stance": "silent",
          "note": "grep of SYN.txt for the root shapes produced no clean hit (the OCR mangles the labiovelar notation); Buck's chapter 4.74 'live' was not located in the text file."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan / Old Persian",
          "words": "jiva, jîta, jva; merezu-jîta; hu-jyâti",
```


## [2026-09-06T14:52:22.687Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gʷenā\\|gᵘ̯enā\\|gʷenā\\|gu̯enā\\|gʷen-\\|Page(s): 473\" POK_full.txt | head -30",
 "description": "Grep Pokorny for gwena"
}
```


### [2026-09-06T14:52:22.761Z] TOOL RESULT

```
39103:Page(s): 473 
39292:Page(s): 473 
39898:Page(s): 473-474
```


## [2026-09-06T14:52:23.459Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 476\\|Page(s): 473\\|Page(s): 476-477\\|Page(s): 473-474\" POK_full.txt | head -20",
 "description": "Find Pokorny pages 473 476"
}
```


### [2026-09-06T14:52:23.511Z] TOOL RESULT

```
39103:Page(s): 473 
39292:Page(s): 473 
39606:Page(s): 476-477 
39898:Page(s): 473-474
```


## [2026-09-06T14:52:25.905Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39020,39110p' POK_full.txt",
 "description": "Print Pokorny 473 context"
}
```


### [2026-09-06T14:52:25.954Z] TOOL RESULT

```
Sardinian Logudoresu 



vida 



Sicilian 



vita 



Triestino 



vita 



Umbro-Sabino 



vita 



Wallon 



veye 



2. with ApiOTH, masc. pioTO(;; 'life, means of living, substance, the world, mankind, etc.'; 
Note: common lllyrian g"- > b-. 



with or. Lithuanian gaivus^a\er{, awal<e, smart, living '; 

verbal derivative: Old Indie y7i/a//i Avestan Jva/'t/ {\.e. jTva/t/) "lives', ap.y/Va" live!' = Latin 
v/vo, Old Church Slavic z/vg' live ' (Inf. z/t/see above), extended Lithuanian gyvenu' live 
'; Old Indie y»7i/a/A pra-jinosi^ be alive, get excited; stimulate, animate, refresh '. 

References: WP. I 668 ff., Meillet Introduction^ 165, Specht KZ. 62, 11 1, Schwyzer Gr. Gr. 
I 298, 300, 330, 5014, 6756, Trautmann 75 f. 
Page(s): 467-469 

Root / lemma: g^eb^- 

Meaning: womb; young of animal 

Material: Old Indie garbha-h, Avestan garawa- "womb, foetus', garabusu. " the young of 

an animal '; Old Indie sa-garbhya-h^ son of the same mother, brother and sister ' (= gr. 

a5£A(p£6(; ds.); 

gr. SsAcpuq, -uoc; f., Doric SsAcpua " womb, uterus' (see below); *5£A(poc; n. ds. as base 
from aSsAcpsoc; (Hom.) "couterinus, brother ' (*a-5£A(p£[a]-6^), next to which Attic a5£A(p6(; 
ds.; SsAcpa^ m. f. "piglet', 5£A(pi(;, hvo(; m. "dolphin', 5oAcp6(; n MHTpa Hes.; Specht (Indo 
Germanic Dekl. 268) reconstructs from gr. a5£Ai(p-r|p a5£A(p6q. AaKU)V£c; (Hes.) an 
originally root *g"el-\ 

the -^s-stem reappears in Old High German kilburu., chilburra\. "mother lamb'. Old 
English cilforlamb6s. (besides of es^stem Old High German kilbira6s. and - with gradation 
o after ostem as 5oA(p6(;, garbha-h- Modern High German Kalb, see above S. 359 under 
*gel-, *ge/d3^-' clench '), which point to purely velar aniaut (as gall. -Latin ga/baan6 Gothic 
A//-A'e/"womb' etc.). 

Different and mutually influencing but similar in sound families lie before: *g"'eto'^-, 
*g"'ereb'^-, and from ge/- extended b^-forms whose stem formation and specific meaning, 
however, in Germanic are presumably assumed by absorption from g"'eb^-^orms. 

References: WP. I 692 f., WH. I 578, Schwyzer Gr. Gr. I 295. 
Page(s): 473 

Root / lemma: g^el-l 

Meaning: to stick; pain, death 

Material: 1. Gr. btKKxQzo, " wasp, hornet', Hes.; [^"'-o'- 1 Nyhan Albanian].
```


## [2026-09-06T14:52:26.700Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39530,39620p' POK_full.txt",
 "description": "Print Pokorny 476-477 context"
}
```


### [2026-09-06T14:52:26.757Z] TOOL RESULT

```
gr. papu(; " heavy ', papuvw "beschwere", papo^ n. " heaviness'; Note: common lllyrian 
g"'-> b-. 

Maybe alb. barre^ burden, pregnancy '. 

Latin gravis ' heavy, weighty ' ( *g"ra-u-is)\ 

Middle Irish bair^ heavy ' (?), baire^ distress (?)', bruth^ weight, mass' {*g"rutu-), cymr. 
it'/yn/ 'strong, strength ' {*bruwo). Middle Irish br6^bu\k, mass'; Note: common lllyrian g"- > 
b-. 

Gothic kaurJosUoxu. PI. f. ' heavy ', kaurjan' grouch'; 

Lithuanian gurstu, gurti^ lie down (from the winds) ', Latvian gurstu, gurt^ tire; lie down 
(from the winds) ', gufds^ fatigued, faint, languid' (compare also papuq and gravis\v\ the 
meaning ' weighted, pressed down, faint, languid'), whereof with further shifting from ' 
faint, languid, weighted ' to "tame, domesticated, mild' (compare Old High German 75/775/"' 
sorrowful ' : gr. n[J£poc; "tame, domesticated') perhaps: 

Gothic qafrrus^ of persons, gentle, kind ', qafrrei^ gentleness, softness, kindness ', Old 
Norse kyrr, kvirr^sWW, peaceful'. Middle High German kurre. Modern High German kirre^ 
tame, domesticated, trustful ' {*g'^er-ar6s or -eras, -uros); 

Latvian gruts " heavy ' = Latin brutus (Oscan-Umbrian loanword) " heavy, clumsy, 
insensible, unreasonable '; 

Tocharian A kra-marts^ heavy ' (?); Van Windekens Lexique 44. 

Here further as n- derivatives from g"era-av\6 g"erau-: Go\h\c {asilu-) qafrnus^ 
(Esels)muhle ' {*g"er9nu-). Old Norse kverni. {*g"erna) " millstone, quern ', Old English 
cweorn6s.. Old High German quirn, quirna^s.; 

zero grade Balto Slavic J-stem gTrnu-t "quern ' {*gfnu-) in: 

Old Prussian girnoywis {* girnuwis), Latvian dzirnus, dzirnavas, besides Latvian dzirnas 
f. PI. and Lithuanian girnos^. PI.; in addition Lithuanian gerukstis, Latvian dzerukslism. " 
pens molaris'; 



Old Church Slavic zrhnbv/i. PI. "mlN', in addition zrbnovb m. " millstone '; sloven, z'rnav 
f. 'quern ', poln. zarnaH. PI. ds.; russ. zernovm. " millstone '; 

Old Church Slavic zrbny'mWV, and on the other hand Old Indie gravan- m. " stone to 
press the Soma ', Armenian erkan^ millstone ' ( *g"rana). Old Irish brau. Gen. broon^ 
millstone, quern ', cymr. breuan {irom the stem of the oblique case *g"'raun-), acorn, brou, 
bret. breo (nominative case form *g"'raud) ' millstone '. 

5'"'e/f-; besides Old Indie gan-yan (?, see above) here: 

gr. ppT0O(; n. " force, weight, load', ppTGuc; " massive, heavy ', pplGu) 'be heavy, loaded, 
trans, grouch ', probably also pplpn "( massive) attack, rage, fury, abusive word, insult ', 
ppTpouoGai " heavy be angry with', 6ppi|J0(; "vast, grand, strong', ppiM6(; |J£Ya(;, xqAsttoc; 
Hes.; ppiap6(; "tight, firm, strong', next to which the composition form *ppi(i)- in (3pi-nnuo(; " 
crying intensely ' Note: common lllyrian g"- > b-. 

Maybe alb. britme^ scream', britme^ autumn month '. 

gr. Bpi-ap£(jO(; ("wer groften Schaden bringt'), ppi-r|p6v (jsyaAajq K£xapia|j£vov Hes. (ppT 
ppiapov and ppi sni tou [JEyaAou perhaps previously from den compounds released, 
liberated), here with prefix gr. u- {*ud) probably also gr. uppi(; " wanton violence, arising 
from the pride of strength or from passion, insolence, lust, lewdness ', uppi(; avrjp " violent 
man, husband' on grounds of the image " rush with the whole weight of one's strength 
towards something '; -v5-present ppivSsTv 9u|Joua9ai, spsGi^siv Hes.; 

Old Irish bng^ force, power, value, worth ', cymr. bri^ stateliness ', corn, bry^ value, 
worth '; Note: common lllyrian g"- > b-. 

Modern High German Krieg, Old High German kreg^ stubbornness ', Middle High 
German kriec^ exertion, fight, struggle', md. Middle Low German kngen^ exert 
themselves, strive, fight, attain, achieve ' {*grTgh-, respectively Germanic partly greigh-)ll 

Latvian grins "cruel, savage, angry, irate', gnnums " hardness, austereness, severeness 
'? 

References: WP. I 684 ff., WH. I 117 f., 621 , Trautmann 89. 
Page(s): 476-477 

Root / lemma: g^er-S, g^or- 
Meaning: mountain 



Grammatical information: originally inflection g'^ores, Gen. g^eros 
l\^aterial: Old Indie girf-h m. "mountain', Avestan gairi- ds.; 

gr. 5£ip6(; (Hes.) "hill', ui|ji5£ipo(; " with high cliffs ', 5£ipaq, Cretan 5r|pc((; f. "hill, 
tableland, hill, plateau ' {*g"'erio-'7); 

Note: common lllyrian g"- > d-.
```


## [2026-09-06T14:52:33.274Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39820,39900p' POK_full.txt",
 "description": "Pokorny 473-474 article"
}
```


### [2026-09-06T14:52:33.338Z] TOOL RESULT

```
Root / lemma: g^ei- (or g^eia^. gl"- 

Meaning: skin 

Note: with formants -no-, -lo- 

Material: Old Indie y/775- ' leather bag', y^a-/? "hose'; Middle Irish bTan^sV\v\, fell, fur'; Note: 

common lllyrian g"- > b-. 

the Irish cognate word could certainly belong also to b^ez-'hit', whose Celtic representative 

have also the meaning 'cut, clip' (compare scortum : scheren ) ; see above S. 118. 

References: WP. I 666. 

Page(s): 469 

Root / lemma: g''ena {* ghfenS) 

Meaning: woman, wife, *goddess 

Grammatical information: Gen. g'^n-asand *g''^-as, also Nom. g^ena-, g^enT- 

Note: 

Root/ lemma: gh^ena^ woman, wife, *goddess' could be a truncated Root/ lemma: ghau- 

ghaua-{* ghauvana): "to call, *priestess': mnl. godinne. Old English ^yofe/7 "goddess' 



Material: Old Indie gna{*g"'nS) f. " divine woman, goddess ' (to partly disyllabic *g^n^, 
Gen. gnas-\ Avestan gsna, yna'\N\ie, woman'; Old \nd\c jan/-h= Avestan Ja/nh, npers. zan 
ds. (Old Indie a\sojan/j; in compounds Old Indie lengthened grade -Jani-= Avestan ya/?/- 
ds.; 

Armenian kin {*g"'ena) "woman', PI. kanai-k {*g"en-ai + Plur.- ending-A) ; Old Phrygian 
povoK, New Phrygian pav£KO(; ' woman, wife ' is probably loanword from Aeolic Gr.; 
differently Kleinhans with Pedersen Groupement 48 Anm. 

gr. yuvn 'woman' {*g'^una). Gen. yuvaiKOc;, beside Boeotian pava {*g'^enS), PI. pavr|K£(;; 
*g"'na-, from it *pvc(-, gr. \x\cx- puts in pvao|jai " unengaged, free ', in addition pvpoTrip " 
suitor ', pvPiOTuc; ' courtship ', (jvpiarn aAoxoc; " lawful wife ' (with secondary -a-); 

Old Irish ben{*g"enS), Gen. Sg. mna{*g"'n-as), Gen. PI. ban {*g"'en-dm), ), in the 
compound ban-{ban-chu^ female dog '); besides bev\. " woman ' {*g"en)\ cymr. ben-yw^ 
feminine, female ', corn, ben-en^ bride, betrothed woman '; [common lllyrian g"- > b^. 

alb. gheg. grue, Tosc grua'wie, woman' {*g"'n-dn), pi. gra, 
Note: alb. grua : Breton gwreg: Welsh gwraig^m^e, woman'. 

after Vetter Gl. 23, 204 here Messapic benna'wi^e' and (?) lepont. ven/a{G\. 15, 12); 

Note: corn, ben-en' bride, betrothed woman ' = Messapic benna'\N\ie'. 

Gothic qino {*g"en-dn-) = Old English cwene. Old High German quena. Middle High 
German quene'woman, wife'; besides zero grade Middle High German kone, ds.. Old 
Norse kona {Gen. PI. kvenna) 'wife, woman' {*g"en-on-)\ lengthened grade Gothic qens 
"wife' {*g"'eni-s= Avestan Jan/-, Old \nd\c Jan/-), Old Norse kv^n, kvan. Old English cwen, 
asachs. quands.; 

Old Prussian genna, Vok. genno'\N'\ie, woman'; 

Old Church Slavic zena'\N\ie, woman'; zen/nb " female ' = Gothic q/ne/ns ds.; 

alb. zonje' mistress, wife, woman' {*g"enia). 

Maybe alb. {*g"ania) za/75 "nymph, goddess', {*g"onia) zotm., PI. zotai. "god' [common 
alb. n > nt> /\ : npers. zan, Old Church Slavic zena "wife, woman' 



Tocharian A sarh (PI. snu) = B sana (Obi. sno) "wife, woman'; Pedersen Tocharian 
Sprachg. 37 f. 

References: WP. I 681 f., WH. I 112 f., Trautmann 84, Meillet Esquisse 84, Schwyzer Gr. 
Gr. 296, 582 f., Tagliavini L'Albanese di Dalmatia 126. 
Page(s): 473-474 

Root / lemma: g^heA^-
```


## [2026-09-06T14:52:33.744Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=39460 && NR<=39535' POK_full.txt",
 "description": "Pokorny gwer lemma heading"
}
```


### [2026-09-06T14:52:36.724Z] TOOL RESULT

```
Lithuanian gargaliuoju^ groan, gurgle '; after Specht KZ. 59, 110'' here Lithuanian 
gvrTgsti, gvarzdeti^ be hoarse ', Latvian gverg(z)det^ creak, babble, chatter '; s. above WH. 
1628; 

3. With formants -ua-: 

gr. Attic 5£pr|, Ionian 5£ipn, Lesbian Ssppcc, 5£pa, Doric 5npa " neck, nape ' ( *g'^er-ua); 

Note: [common lllyrian Albanian g- > o'-]. 

due to an h feminine *g"'(e)r7. *g''nua^ neck, throat area ' in: 

Old \v\6\c gnvat, Avestan grJva^ nape ', Latvian grJva^ embouchure, estuary; triangular 
land between rivers ', gnvis " tall grass'; 

Old Church Slavic gr/va ' mane' , gr/vbna 'coWar, neckband'. 

Maybe alb. krifa 'mane', grifshe' jay, shrew, lumberjack ' Slavic loanwords. 



4. As p'^extension presumably here *g'rogh-\ 

in gr. sppo^s, Aor. " devoured ', horn, ava-, Kara-ppo^Eis, ava-ppox£i<;, ppo^ai pocpnaai 
Hes., ppoxSoq m. 'gullet, throat'; Note: common lllyrian g"- > b-. 

Middle High German krage^ neck, throat, nape '; Modern High German Kragen ' collar ', 
Old Norse kragi^ neckwear, collar ', Middle English crawe, engl. craw^ bird or insect's 
crop; stomach ' (lengthened grade in addition Middle Low German kroch, kruch^ hostelry, 
inn ', Modern High German Krug\v\ the meaning ' inn '? meaning as in Latin gurgustium' a 
small, mean dwelling, a hovel, hut '); 

Old Irish bragae' neck, nape ' ( *gfg-nt-), acymr. abal-brouannou^ throat ' (actually ' 
Adam's apple'), mcymr. breuanV windpipe ' (proto Celtic *brag-)\ acorn. i6'/7a/7se'/7 "guttur', 
abret. Brehant-Dincat<^\. " gunu^receptaculi pugnae ', maybe from *brg-, Pedersen KG. 
100. Note: common lllyrian g""- > b-. 

With nasalization in addition perhaps gr. pp6yxo(; m., Ionian ppoyxir) " windpipe ', 
ppayxia, papayxia ' gill offish; trachea, windpipe ' seems in Vok. reshaped after ppayxaoj 
"be hoarse', ppaYXO(; " hoarseness ', that related to Old Irish brongide ^hoarse' (above 
103), but it must be separated from ppoyxot; to (: sppaxs " jangle, crack, shout ', Old Indie 
brmhatr barrire '? Johansson KZ. 36, 345). 

Note: 

Gr. ppayxia, papayxia ' gill offish' : alb. Geg {* g"er- g"ha) verza^ (*throat), gill offish' : 
Latvian barda^<^\\\ offish' : Latvian : M/'o'a "beard' [fa]; barzda {'6\a\.) "beard'. 
Root / lemma: g^er-l, g^ere-: " to devour; throat ' > Root/ lemma: b'^arH^a: " beard' 

5. With pure velar: gr. y£py£pO(; ppoyxoq Hes., yapyapscbv " uvula in mouth', yapyapi^w 
"gurgle' (: Armenian kerker/m 'become hoarse'?) perhaps through labialization after forms 
with yup- (yopyupn "subterraneous, underground jail, water pipe '), yet is previously ger- 
besides g"er- because of ge/- besides g^e/- is safe. 

References: WP. I 682 ff., WH. I 627 f., Trautmann 89 f., 98, Specht KZ. 59, 1 10, 1 . 
Page(s): 474-476 

Root / lemma: g''er-2, g^erQ-, g^erQu-, g^en- 

Meaning: heavy 

Material: Old Indie gurii-h' heavy, important, venerable ' (compounds ganyan. Sup. 

garistha-h), agru-' available, unoccupied; unmarried', gru-mustf-h' heavy handful ', 



garima^ heaviness' {*g"'er9-); Avestan gouru- (in compound) " lieavy '; npers. giran^ lieavy 
' {*grana-\ reshuffling after *frana-^i\}\\y, 

gr. papu(; " heavy ', papuvw "beschwere", papo^ n. " heaviness'; Note: common lllyrian 
g"'-> b-. 

Maybe alb. barre^ burden, pregnancy '. 

Latin gravis ' heavy, weighty ' ( *g"ra-u-is)\
```


## [2026-09-06T14:53:16.178Z] TOOL CALL #13: Bash

```json
{
 "command": "ls site/pages/208.jpg 2>/dev/null; pdftoppm -f 208 -l 208 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg208 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render printed page 208"
}
```


## [2026-09-06T14:53:16.720Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; ls | grep -i mon",
 "description": "List refs dir"
}
```


### [2026-09-06T14:53:19.270Z] TOOL RESULT

```
site/pages/208.jpg
total 292
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 10:53 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb 77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb 67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb 59146 Sep  6 10:53 pg208.png
```


### [2026-09-06T14:53:19.313Z] TOOL RESULT

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
MON_part1.txt
MON_part2.txt
```


## [2026-09-06T14:53:21.166Z] TOOL CALL #15: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/208.jpg"
}
```


### [2026-09-06T14:53:21.196Z] TOOL RESULT

```

```


## [2026-09-06T14:53:34.621Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gwen ===\"; grep -n -A12 \"^g[wʷ]en-\" AHD_watkins1985.txt | head -60; echo \"=== AHD gwere ===\"; grep -n \"g[wʷ]er[aə]*-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for gwen and gwer"
}
```


### [2026-09-06T14:53:34.685Z] TOOL RESULT

```
=== AHD gwen ===
=== AHD gwere ===
```


## [2026-09-06T14:53:35.972Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN queen ===\"; grep -n -B2 -A10 \"^queen,\" KLN_1966.txt | head -40; echo \"=== KLN gyneco ===\"; grep -n -B2 -A8 \"gynecology\\|gynaecology\\|gyneco-\\|gyno-\" KLN_1966.txt | head -50",
 "description": "Grep Klein for queen and gyneco"
}
```


### [2026-09-06T14:53:36.052Z] TOOL RESULT

```
=== KLN queen ===
=== KLN gyneco ===
2027-ague,  n.,  malarial  fever.  —  OF.  ague,  ‘an  acute fever’,  prop.  fem.  of  the  adjective  agu  (F.  aigu), ‘sharp,  acute  (scil.  fever)’,  fr.  L.  ( febris )  acuta, ‘an  acute  fever’,  fem.  of  acutus,  ‘sharp,  acute’. See  acute.
2028-Derivatives:  agu-ish,  adj.,  agu-ish-ly,  adv.,  agu- ish-ness,  n.,  ague-like,  adj. agunah,  n.,  a  woman  prevented  from  remarrying because  she  has  no  proof  of  her  husband’s  death (Jewish  religion).  —  Heb.  'aghiindh,  lit. ‘restrained (from  marrying)’,  passive  fem.  part,  of  ‘aghan, ‘he  restrained,  shut  up’,  which  is  rel.  to  Arab. 'S' jama,  IV  (=  causative)  form  of  stem  ‘-j-m,  ‘to shut  up’.
2029:Agyieus,  n.,  a  name  of  Apollo  (Greek  mylhol.)  — Gk.  ’Ayjieu;,  lit.  ‘guardian  of  the  streets’,  fr. ayuia,  ‘street’,  lit.  ‘that  through  which  some¬ thing  is  led  or  driven’,  fr.  ayeiv,  ‘to  drive’, which  is  cogn.  with  L.  agere,  ‘to  set  in  motion, drive;  to  do,  act’.  See  agent,  adj. agynary,  adj.,  having  no  female  organs  (bot.)  — Formed  fr.  priv.  pref.  a-,  Gk.  yjvr;,  ’woman’ (see  gyneco-),  and  adj.  suff.  -ary. ah,  interj.  —  Of  imitative  origin, aha,  interj.  —  Of  imitative  origin.
2030-Ahabah  Rabbah,  the  second  of  two  benedictions preceding  the  Shema  in  the  morning  prayer (Jewish  liturgy).  —  Heb.  ahabhdh  rabbd h,  lit. with  great  love’  (so  called  from  the  two  first words  of  the  text  of  the  benediction).  Ahabhdh, l°ve’,  derives  fr.  ahabh,  ‘he  loved’,  which  is  rel. to  Aram,  ahabh,  ‘he  loved’,  and  possibly  also to  Arab,  habba,  ‘he  was  moved’.  Rabbdh  is  fem.
2031-rabh.  'great’  (whence  Mishnaic  Heb.  rabh, ‘master’).  See  rabbi  and  cp.  the  first  element  in •aroboam.
2032-^■hath  Olam,  the  second  of  the  two  benedic¬ tions  preceding  the  Shema  in  the  evening  prayer
2033-( Jewish  liturgy).  —  Heb.  ahabhath  'oldm,  ‘with everlasting  love’  (so  called  from  the  two  first words  of  the  text  of  the  benediction).  Ahabhath is  the  state  construct  of  ahabhdh,  ‘love’;  see prec.  word.  ‘ Oldm  means  ‘eternity’  (in  Mishnaic Hebrew  also  ‘world’) ;  see  Olam  Habba. Ahasuerus,  n.,  name  of  a  Persian  king  (Bible)’, identical  with  Xerxes.  —  Heb.  Ahashwerosh  (al¬ so,  in  the  kethib  of  the  Book  of  Esther  10:1, Ahashresh),  fr.  OPers.  Xshaydrshan-  (whence also  Gk.  Eip5r|s),  ‘lit.  ‘male  (i.e.  hero)  among kings’,  fr.  xshaya-,  ‘king’,  and  arshan-,  ‘male, man’.  The  first  element  derives  fr.  I.-E.  base * qpe(i )-,  *qpe( /’)-,  ‘to  rule’ ;  see  check,  ‘a  sudden stop’.  The  second  element  is  cogn.  with  Gk. apOTjv,  ‘male,  masculine’,  OI.  psabhdh,  ‘bull, steer’,  fr.  I.-E.  base  *eras-,  *ras-,  *eres-,  *ers-, ‘to  flow,  wet,  moisten’,  whence  also  L.  ros,  gen. roris,  ‘dew’ ;  see  roric  and  cp.  rasa.  Cp.  Xerxes, ahead,  adv.  and  adj.  — -  Formed  fr.  a-,  ‘on’,  and head.
2034-aheap,  adv.  —  Formed  fr.  a-,  ‘on’,  and  heap, ahem,  interj.  —  Of  imitative  origin.
2035-Ahi,  a  serpent  in  Vedic  mythology,  identified with  Vritra.  —  Ol.  ahih,  ‘serpent’,  rel.  to  Avestic azish  and  cogn.  with  Gk.  lyiq,  ‘viper’,  L,  anguis, ‘serpent,  snake’.  See  anguine  and  cp.  echidna, ahoy,  interj.  —  A  natural  sound,  compounded  of the  interjections  a,  ‘ah’,  and  Aoy.Seeah  and  hoy. Ahriman,  n.,  the  spirit  of  evil  in  the  Zoroastrian religion.  —  Gk.  ’ApEqrdvto?  (in  Aristotle)  or ’ApsipLavY]?  (in  Agathias),  fr.  Avestic  ahra  mai- nyu,  ‘the  evil  (lit.  hostile)  spirit’, ahull,  adv.  (naut.)  —  Formed  fr.  a-,  ‘on’,  and hull,  ‘body  of  a  ship’.
2036-ahura,  n.,  a  benevolent  deity  (Persian  mythology). —  Avestic  ahura-,  ‘a  god,  a  good  spirit',  rel.  to OL  dsurah,  of  same  meaning.  Sec  asura  and  cp. the  first  element  in  Ormazd.
2037-Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
--
4504-basaree,  n.,  a  Hindu  flageolet  (music).  —  Hind. basree,  fr.  OI.  vamsah,  ‘bamboo’,  which  is  cogn. with  Mir.  feice,  Ir.  feige  (for  •vankia),  ‘lintel, rafter’;  L.  vacerra,  ‘log,  stock,  post’,  however, is  not  cognate.
4505-bascule,  n.,  an  apparatus  based  on  the  principle of  the  seesaw.  —  F.,  ‘seesaw’,  from  orig.  basse cule,  altered  from  earlier  bacule  under  the  in¬ fluence  of  basse,  fern,  of  bas,  ‘low’.  Bacule  is composed  of  the  imper.  of  battre,  ‘to  strike , and  cul,  ‘posterior’.  See  batter,  ‘to  beat’,  and culet.
4506:base,  n.,  bottom;  foundation,  pedestal.  —  F.,  fr. L.  basis,  fr.  Gk.  (idci^,  ‘a  stepping,  step,  pede¬ stal,  foot,  base’,  from  the  stem  of  (3aivto,  ‘I  go’, which  prob.  stands  for  *(3avLCt>,  fr.  *P<x|z-io), fr.  l.-E.  base  *gwem-,  'to  go;  to  come’,  whence also  L.  venio  (prob.  for  *gwmio),  ‘I  come’,  Goth. qiman,  OE.  cuman,  ‘to  come’.  See  come  and  cp. venue,  ‘arrival’.  Cp.  also  basis,  abasia,  acrobat, aerobatics,  amphisbaena,  Anabaena,  anabas,  ana¬ basis,  -bates,  bathmism,  batophobia,  bema,  cata- basis,  diabase,  adiabatic,  diabetes,  ecbatic,  gyno- base,  hyperbaton,  metabasis,  Odobenus,  Ori- batidae,  parabasis,  presby-,  stereobate,  stylobate. As  a  term  of  chemistry  base  was  introduced  by the  French  chemist  Guillaume-Fran^ois  Rou-
4507-elle  (1703-70)  in  1 754-
4508-Derivatives  ;  base,  tr.  v.,  to  form  a  base  for; intr.  v.,  to  be  based  (on  or  upon  something); base-ment,  n.
4509-base,  adj.  —  ME.  bas ,  fr.  OF  (=  F.)  bas,  ‘low’, fr.  Late  L.  bassus,  ‘thick  fat,  stumpy’  (in  classical L.  occurring  only  as  a  cognomen);  of  un¬ certain  origin.  Cp.  abase,  bass  (music),  basset, basso,  bassoon,  debase.
4510-Derivatives:  base-ly,  adv.,  base-ness,  n. bash,  tr.  v.,  to  strike  violently.  —  Of  imitative origin.  Cp.  Swed.  basa,  Dan.  baske,  ‘to  strike’, bashaw,  n.  —  A  variant  of  pasha  (q.v.) bashful,  adj.  —  Aphetic  for  abash-ful.  See  abash and  -ful.
4511-Derivatives:  bashful-ly,  adv.,  bashful-ness,  n. bashi-bazouk,  n.,  a  Turkish  irregular  soldier.  — Turk,  bashi-bozuq,  lit.  ‘(one  whose)  head  is turned’.  Cp.  the  first  element  in  bashlyk  and  the second  element  in  bimbashee. bashlyk,  also  bashlik,  n.,  hood  covering  the  cars. —  Turk,  bashlyq,  ‘any  kind  of  headgear’, basic,  adj.  —  Formed  with  suff.  -ic  fr.  base,  n. Cp.  the  second  element  in  monobasic,  di¬ basic.
4512-Derivative:  basic-al-ly,  adv. basidium,  n.,  a  form  of  sporophore  characteristic of  the  fungi  of  the  class  Basidiomycetes  (bot.)  —
4513-basil
4514-batnos
--
16933-gymnosperm,  n,  a  plant  that  has  its  seeds  naked (i.e.  not  enclosed  in  an  ovary).  —  ModL.  gym- nospermus,  fr.  Gk.  YU(iv6<mepp.o<;,  ‘having  naked seeds’,  compounded  of  yupvoc;,  ‘naked’,  and mrEppia,  ‘seed’.  See  gymno-  and  sperm  and  cp. angiosperm.
16934-gymnospermous,  adj,  having  the  seeds  not  en¬ closed  in  an  ovary.  —  See  prec.  word  and  -ous. Gymnotus,  n,  a  genus  of  fishes,  the  electric  eel (ichthyol.)  —  ModL.  Gymnotus,  contraction  of Gymnondtus,  which  is  compounded  of  Gk.  yup.- v6?,  ‘naked’,  and  vuto?,  ‘the  back’ ;  so  called  be¬ cause  of  the  absence  of  the  dorsal  fin.  See  gym¬ no-  and  noto-.  The  contraction  of  Gymno-ndtus into  Gymnotus  is  due  to  haplology.  (Cp.  Gym¬ nonoti,  which  is  formed  without  such  contrac¬ tion).
16935:gyn-,  form  of  gyno-  before  a  vowel, gynaeceum,  n,  1)  apartment  for  women  ( Greek antiq.y,  2)  the  pistils  of  a  flower  collectively  (hot.)
16936:—  L.  gynaeceum,  fr.  Gk.  yovatxEtov,  ‘women’s apartment’,  prop.  neut.  of  the  adjective  yuvat- xciop,  ‘pertaining  to  a  woman;  womanly,  fe¬ minine,’  used  as  a  noun,  fr.  yuvi rj,  gen.  yuvatxo?, ‘woman’.  See  gyneco-.
16937:gynaeco-.  —  See  gyneco-.
16938:gynandrous,  adj,  having  the  gynoecium  and  an- droecium  united  in  a  column  (as  in  orchids).  — Gk.  ydvavSpoq,  ‘of  doubtful  sex’,  fr.  yuvr;, ‘woman’,  and  <4vf)p,  gen.  avSpos,  ‘man’.  See gyneco-  and  andro-  and  cp.  androgynous.  For E.  -ous,  as  equivalent  to  Gk.  -os,  see  -ous. gynarchy,  n,  government  by  a  woman  or  women.
16939-—  Compounded  of  gyn-  and  Gk.  -ocpxia,  ‘rule’. See  -archy.
16940:gynec-,  form  of  gyneco-  before  a  vowel, gynecium,  n.  —  See  gynoecium. gyneco-,  before  a  vowel  gynec-,  combining  form meaning  ‘woman’.  —  Gk.  yjvatxo-,  yuvatx-, fr.  yuvf],  gen.  yuvaixop,  ‘woman’,  rel.  to  Boeo¬ tian  P<xv8,  fr.  I.-E.  *gv:und,  *gwena,  ‘woman’, whence  also  OI.  gnd,  gand,  ‘wife  of  a  god,  god¬ dess’,  jdnih,  ‘wife’,  Goth,  qind,  ‘woman,  wife’, qens,  ‘woman’,  OE.  cwen,  ‘woman,  wife,  queen’. See  quean  and  cp.  queen.  Cp.  also  agynary,  an¬ drogynous,  misogyny,  monogynous. gynecocracy,  gynaccocracy,  n,  government  by  a woman  or  women.  —  Gk.  yuvatxoxpaTta,  com¬ pounded  of  ywir),  gen.  yuvatxop,  ‘woman’,  and -xpa-rla,  ‘rule  of’,  fr.  xpaxos,  ‘strength,  power, rule'.  See  gyneco-  and  -cracy. gynecocrat,  gynaecocrat,  n,  an  adherent  of  gyne¬ cocracy.  —  See  prec.  word  and  -crat. Derivatives:  gynecocrat-ic,gynecocrat-ic-al,  adjs. gynecology,  gynaecology,  n,  the  study  of  diseases peculiar  to  women.  —  Compounded  of  gyneco- and  Gk.  -Xoyia,  fr.  -Xo yop,  ‘one  who  speaks  (in  a certain  manner) ;  one  who  deals  (with  a  certain topic)’.  See  -logy.
16941-Derivatives:  gynecolog-ic,  gynecolog-ical,  adjs, gynecolog-ist,  n.
16942-gyniatrics,  n,  the  treatment  of  diseases  peculiar  to
16943-691
16944-gyve
16945:women.  —  Compounded  of  Gk.  yuvf),  ‘woman’, and  la-rptxi?,  ‘pertaining  to  healing’.  See  gyneco- and  -iatric.
16946:gyno-,  combining  form,  equivalent  to  gyneco-.  — Fr.  Gk.  yovf),  ‘woman’.  See  gyneco-. gynobase,  n,  the  flat  enlargement  of  the  recep¬ tacle  of  a  flower  bearing  the  gynoecium  (bot)  — Compounded  of  gyno-  and  base,  n. gynocracy,  n,  gynecocracy.  —  Compounded  of gyno-  and  -cracy.  Cp.  gynecocracy. gynoecium,  gynecium,  n,  the  pistils  of  a  flower collectively  (bot.)  —  ModL,  usually  explained as  compounded  of  Gk.  yovf),  ‘woman’,  and olxop,  ‘house’  (see  gyno-  and  economy),  but  in reality  a  corruption  of  gynaeceum  (taken  in  its second  meaning).  This  corruption  was  suggested by  the  ending  -oecium  in  androecium.
16947:-gynous,  combining  form  meaning  1)  ‘female’,  as in  polygynous;  2)  ‘having  female  organs  or  pis¬ tils’,  as  in  androgynous  (bot)  —  Gk.  -yuvo q,  fr. yuvfj,  ‘woman’.  See  gyneco-  and  -ous. gyp,  n,  a  male  college  servant  (at  Cambridge or  Durham).  —  Of  uncertain  origin;  possibly short  for  gypsy.
16948-Gypaetus,  n,  a  genus  of  birds,  the  lammergeier (ornithol)  —  ModL,  compounded  of  Gk.  yut)/, gen.  yoizbc,,  ‘vulture’,  and  as-rop,  ‘eagle’.  See Gyps  and  aeto-.
16949-Gyps,  n,  a  genus  of  birds,  the  griffon  vulture  (or¬ nithol.)  —  ModL,  fr.  Gk.  yuiji,  gen.  yu/rAc,  ‘vul¬ ture’,  rel.  to  yuTTY],  ‘cave,  den,  hole’,  fr.  I.-E. *geu-p-,  a  -//-enlargement  of  base  *geu-,  ‘to  bend, curve,  arch’.  See  cove,  ‘a  small  bay’,  and  cp. gyre.
16950-gypseous,  adj,  1)  containing  gypsum;  2)  resem¬ bling  gypsum.  —  L.  gvpseus,  ‘of  gypsum’,  fr. gypsum.  See  gypsum  and  -ous. gypsiferous,  adj,  producing  gypsum.  —  See gypsum  and  -ferous.
16951-Gypsophila,  n,  a  genus  of  plants  of  the  pink family  (bot)  —  ModL,  compounded  of  Gk. yuil*/?,  ‘chalk,  gypsum’,  and  9Uelv,  ‘to  love’. See  gypsum  and  philo-. gypsous,  adj.  —  A  var.  of  gypseous, gypsum,  n.  —  L,  fr.  Gk.  yuij/oc,  ‘chalk’,  of  Sem. origin.  Cp.  Arab,  jibs,  Mishnaic  Heb.  gebhes, gephes,  ‘plaster,  mortar,  gypsum’,  which  prob. derive  fr.  Akkad,  gassu  (whence  also  Aram. gassd,  whence  Arab,  jass,  jiss,  juss,  qa$s,  qisf), ‘gypsum’.  —  Cp.  gesso.
16952-gypsy,  gipsy,  n.  —  Fr.  earlier  gypcian,  aphetized fr.  still  earlier  Egypcian,  ‘Egyptian,  gypsy’,  fr. OF.  Egyptien  (F.  £gyptien),  fr.  L.  Aegyptianus, ‘Egyptian’.  See  Egyptian  and  cp.  gitano.  Cp. aiso  gyp.
16953-Derivatives:  gypsy,  intr.  v,  gypsy-ish,  adj. gyr-,  form  of  gyro-  before  a  vowel, gyral,  adj,  moving  in  a  gyre  or  circle.  —  Formed with  adj.  suff.  -al  fr.  L.  gyrus.  See  gyre. Derivative:  gyral-ly,  adv. gyrate,  intr.  v,  to  revolve.  —  L.  gyrdtus,  ‘cir¬ cular’,  pp.  of  gyrare,  ‘to  turn  round  in  a  circle’.
16954-fr.  gyrus.  See  next  word  and  verbal  suff.  -ate. Derivatives:  gyrat-ion,  n„  gyrat-ion-al,  gyrat¬ ory,  adjs.
16955-gyre,  n,  a  circular  motion.  —  L.  gyrus,  fr.  Gk. yupo<;,  ‘circle,  ring’,  which  is  rel.  to  yiipop, ‘rounded,  curved’,  and  cogn.  with  Arm.  kor, ‘crooked’,  kurn,  ‘the  back’,  Lith.  gurnets,  hip, ankle,  bone’,  Norw.  kaure,  ‘a  curly  lock  of  hair’, Swed.  kura,  Dan.  kure,  ‘to  squat’,  MLG.  kuren, ‘to  lie  in  wait’,  G.  kauern,  ‘to  squat,  cower’.  All these  words  are  derivatives  of  I.-E.  *geu-r-,  an -/•-enlargement  of  base  *geu-,  ‘to  bend,  curve, arch’.  See  cove,  ‘a  small  bay’,  and  cp.  cower.  Cp. also  gyrus,  the  first  element  in  girandole,  virelai, and  the  second  element  in  autogiro,  circumgyrate, helicogyre.  Cp.  also  Gyps, gyre,  intr.  v,  to  gyrate.  —  L.  gyrare,  ‘to  turn round  in  a  circle’,  fr.  gyrus.  See  gyre,  n. gyrfalcon,  n.  —  A  var.  of  gerfalcon, gyro-,  combining  form  meaning  ‘circle,  circular, spiral’.  - — •  Gk.  yupo-,  fr.  yupop,  ‘circle’.  See gyre,  n.
--
17710-heterography,  n.,  incorrect  spelling.  —  Com¬ pounded  of  hetero-  and  Gk.  -ypxipla,  fr.  ypacpetv, ‘to  write’.  See  -graphy.
17711-Derivatives :  heterograph-ic,  heterograph-ic-al, adjs.
```


## [2026-09-06T14:53:46.600Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"queen\\b\" AHD_watkins1985.txt | head -10; echo ===; grep -n -i \"gravity\\|gravis\" AHD_watkins1985.txt | head -10; echo === ; grep -n -i \"barometer\\|baros\" AHD_watkins1985.txt | head",
 "description": "Grep AHD Watkins for queen, gravis, baros"
}
```


### [2026-09-06T14:53:46.654Z] TOOL RESULT

```
Exit code 1
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
2148:QUEAN gWen- QUEBRACHO ker-2, skep- QUEEN gWen-
(eval):1: == not found
```


## [2026-09-06T14:53:47.829Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN grave/gravity ===\"; grep -n \"gravity,  n\\|^grave,  adj\\|grave,  adj\" KLN_1966.txt | head; echo === ; grep -n \"grief,  n\\|barium,  n\\|barometer,  n\" KLN_1966.txt | head",
 "description": "Grep Klein for grave gravity grief barium barometer"
}
```


### [2026-09-06T14:53:47.886Z] TOOL RESULT

```
Exit code 1
=== KLN grave/gravity ===
5619:Briareus,  n.,  a  hundred-handed  giant  (Greek mythol.)  —  L.,  fr.  Gk.  Bpiapsox;,  fr.  (ipiapoc, ‘strong’,  fr.  base  ppi-  (cp.  the  compound  (ipi- tjttuoi;,  ‘loud-shouting’),  whence  also  ppiOut;, ‘heavy’,  pptfteiv,  ‘to  be  laden,  to  be  heavy’,  fr. I.-E.  base  *gwer-,  ‘heavy’,  whence  also  Gk. papup,  L.  gravis,  ‘heavy’.  See  grave,  adj.,  and cp.  baro-.  Cp.  also  Bridget,  Brigit. bribe,  n.  —  OF.  bribe,  ‘crumb,  piece  of  bread’,  esp. ‘piece  given  to  a  beggar’,  fr.  briber,  brimber, ‘to  beg’,  which  is  of  uncertain  origin. Derivatives:  bribe,  tr.  v.,  brib-able,  adj.,  brib-ee, n.,  brib-er,  n.,  brib-er-y,  n. bric-a-brae,  n.,  odds  and  ends  of  furniture,  artist¬ ic  objects,  etc.  —  F.  bric-a-brac,  ‘odds  and  ends, curiosity  shop’;  of  imitative  origin, brick,  n.  —  F.  brique,  ‘brick’,  fr.  MDu.  bricke, of  s.m.,  lit.  ‘a  broken  piece’,  rel.  to  E.  break (q.v.)  Cp.  briquette.
5748:brut,  adj..  dry  (said  of  wines,  esp.  of  champagne). —  F.,  ‘raw,  crude’.  See  brute, brutal,  adj.  —  See  brute  and  adj.  suff.  -al. Derivatives:  brutal-ity,  n.,  brutal-ize,  tr.  v. brute,  n.  —  F.  brut,  fem.  brute,  ‘raw,  crude’,  fr. L.  brutus,  ‘heavy,  dull,  stupid’,  which  is  cogn. with  Lett,  gruts,  ’heavy’,  OI.  guruh,  Gk.  (bap ti?, L.  gravis,  ‘heavy’.  See  grave,  adj.,  and  cp.  baro-, Briareus.
16617:Derivative:  grave-less,  adj. grave,  tr.  v.,  to  clean  (the  wooden  hull  of  a  ship) of  grass,  etc.  —  OF.  grave  (F.  grive),  ‘strand of  sand,  sandbank’.  See  gravel  and  cp.  Graves, grave,  adj.,  weighty.  —  F.,  fr.  L.  gravis,  ‘heavy, weighty;  troublesome,  painful,  grievous,  hard; important,  honorable’,  which  is  cogn.  with  OI. gurufi,  ‘heavy,  weighty’  (compar.  gariyas-; superl.  garifthah),  Avestic  gouru-  (only  in  com¬ pounds),  ‘heavy,  weighty’,  Gk.  (Japoi;,  ‘weight’, ^apu?,  ‘heavy’,  Pptffeiv,  ‘to  be  laden  with’ ,  Ppiffu?, ‘heavy’,  ppuxp6e,  ‘strong’,  Goth,  kaurus,  ‘heavy’, Lett,  grids,  ‘heavy’.  Cp.  gravedo,  gravid,  gravity, grief,  grieve,  grievous,  aggravate,  aggrieve,  in¬ gravescent.  Cp.  also  baro-,  bary,  Briareus,  brute, centrobaric,  charivari,  garce,  guru,  isobar, grave,  n.,  a  count;  used  esp.  of  the  counts  of Nassau.  —  MDu.  grave  (whence  Du.  graaf), ‘count’,  rel.  to  OHG.  gravo  (whence  MHG. grave,  G.  Graf),  MLG.  grive  (whence  ON. greifi,  Dan.,  Swed.  greve),  ‘count’.  The  orig.
16628:gravity,  n.  —  F.  gravite,  fr.  L.  gravitatem,  acc.  of gravitas,  ‘weight,  seriousness’,  fr.  L.  gravis, ‘heavy’.  See  grave,  ‘weighty’,  and  -ity. gravure,  n.  —  Short  for  photogravure.  Cp.  helio¬ gravure,  rotogravure.
(eval):1: == not found
```


## [2026-09-06T14:54:05.650Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT gouru ===\"; grep -n \"gouru\" BRT.txt | head -20; echo \"=== BRT jaini ===\"; grep -n \"jaini\\|ǰaini\\|Jaini\" BRT.txt | head -20; echo \"=== BRT gena/gna ===\"; grep -n \"gdnd\\|gənā\\|ynā\\|gena-\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T14:54:05.724Z] TOOL RESULT

```
=== BRT gouru ===
10386:Vgl.  lat.  fei,  ßilis,  k<!.  iiüü  'Galle'.  —  Pü. : .  •  j.  gouru.zaoSra-  Adj.  (mask.  °ra-)  'des Hak  tirrcnihiSniouii ,  dam  als  Weihgüsse  schwer,  zähflüssig  Sind"':  ^»«•n'J "■■''*■"""'  t  Yt./o.ri3.
=== BRT jaini ===
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
7024:ff(rai>/(Stverz.)  «^«röMasi/J  V.2, 1  f.,  usw.;'eines  koordiniiten  Satzes  an  das  Voraus- Y.p.z.s,  16,  7J.2,  V.j&ai,  H.  2.ii,Nik.  2, 1  gehende 'und';  die  zeitliche  Folge  tritt  min- yyt.8,22;  —  ä3tar3..kd  avalia..vl.l>arat..}'  dest  sehr  zurück;  a)  eines  Hauptsatzes:  tarn a°  aoxta  ahurö  mazdä  V.  2.42;  40,  Yt  5.  ^yatata  haofyauA^  .  ,  ä'  Alm  jaloyal  Yt. 9°>  95!  —  ahmäi  fradaisaSm  dainqm  .  .  ij.2^{.;  5.18,  5.17,  /j.40;  —  vagiipmnsm ä°  hl  mraont  .  .  visanha  mg  yima  .  .  ä'\  *apa  karsayjn  Jainis  .  .  ä°  tä  .  .  hazö ml  alm  paityaoxta  yimS  .  ,  ä"  h!  mraom  '  nivamay?n  (sd.)  Yt.  /5.80;  —  J  tat  han- .  .  ä'  mE  aem  paityaoxta  .  .  ä"  kl  saya  [jamarum  paiti.jasat .  .  ahurö  mazdä  .  .  ä° "       ■    "    "  ahurff  riazdfv.  2.21  f.;—  ,iat{s.  8}
7252:w/ra£>/(Stver2.)  «>4»/T5ffiaai'i?V.2.if.,  usw.;!  eines  koordinirten  Satzes  an  das  Voraus- Y.p.2,3, 16,  7J.2,V.iÄ3i,  H.2.ii,Nik.3, 1  gehende 'und';  die  zeitliche  Folge  tritt  min- Vyt5,22;  —  d3iari..ks  ava%a..vtJ>arai..'}  AesKstAazMrXck;  a)  eines  Hauptsatzes:  tqm ä°  aoxia  ahur5  mazds  V.  2.42;  40,  Yt.j.  \yazata  AaofyanAö  .  .  ä°  Aim  jaiiyai  Yt. 901  95;  —  aAmäi  fradaSsaSm  daltiqm  .  .  ij.z^f.;  5.18,  p.17,  /5-40;  —  j'alrismrum a°  Al  mraom  .  .  visanAa  ml  yima  .  .  a°  i  *apa  kariay>ii  jainis  .  .  ä°  th  .  .  ha-iS ml  alm  paityaoxta  yimS  .  .  ä"  hl  mraom  I  tiivar^zaym  (sd.)  Yt  if).  80;  —  ä  tat  Aan- .  .  ä'  ml  aim  paityaoxta  ,  .  ä°  hl  xaya  Jamatmn  paitijasal .  .  ahurS  mazda  .  .  3'
7857:frayazaite  . .  kahmaiHt  °zat)Aqm  biwivä Yt.  ry.  41;  —  ravasla  o^idrimla  (sd.)  . . aiaonö  stsil  'eas/a  dtäa'intiUa  . .  drvats stSisY.S.8; — yas/a  ml  ail^m  nanm  "zö <vi  avag>r?pt>m  ravöhu  paiti  uzbäraya£ 'imd  wer  den  .  .,  der  in  Gefangen- schaft verbracht  ist,  wieder  in  Freiheit versetzt"  V.  r<?.  10;  —  haoma  .,  yalcit ■zahu  dirilärihs  Jaininam  *upa  *d?rfzaAu (sd.)  Y.  io.17.  a)  liS.  'zaKAe  als  Inf.
8256:'bei;  in',  räumlich:  yatHl  ahi  . .  'pa  sanake (sd.)  rauhaya  Yt,  i2. 19;  —  °pa  aolaisu (sd.)  rai^haya  Yt/2.18,  V./.19;  —  'pa upaMdi  (sd.)  harayi  ¥1.5.21;  —  yaecit qzaAu  diniäaks jaininqfn  *'pa  *dpmshu*'' Y.  10. 1 7.  3)  mit  Gen.  (?)  'bei',  räum- lich: yatcit  ahi  .  ,  "pa  raoxsnahe  garS nmänahe  Yt.12.37*'.  Wertlos:  II  "imam ustasa/iäm  .  .  mäm  'pä  mäm  karta^  Ao. /.3*>.  U)  Pracv.  (mit  ^ay-,  gam-,  'mar-, Sil};  tav-  usw.).  A)  bei  Ellipse  des Verbums:  'pa  ta  nS  aiwyilsta  (NS.) harjsma  .  .  Vjrt.2j(?).
9954:\janya-,   PiT.'jaini;    Perf.   i  /ajn-,    PfPr.
11557:(sd,)  jainis  (AP,)  Aa^a  masyäkaHbyS  Yt /§.  80.  a)    'Weib'    mit    verächtlichem
11560:•  j.  jaini'  Adj.,  nur  KompA.  'tötend, mordend',
11562:•  j.  }aiiii.mahrka-  m.  'mordender  Tod': jaini.yaskahe  apanastahe  'kahe  apanailake V.  21.  2.
11564:•  j.  Iaini.yaska-  m,  'mordende  Krankheit': 'kahe  apanaitahe  jaini jnahr kahe  apanas- tahe V.  21. 3.
11725:yacif  !a%'wärS  arsana;  tl  mqm.^vinrunte V.iS.^if.;  —  vaifomtam  ^apaMarlaym (sd.)  jainii  .  .;  äat  tä  (APf)  .  .  hazü >tivat7zaym  daiva;  aal  tl  (als  APm.)  .  . ahutiS  vairyS  . .  *samar)guza  avazai  Yt  ig. So£;  —  p>n%w5  .  .  aiwica  tl  (als  AP.) \r3fSva  (sd.)  V.  2.  30;    —    . .  /ravasayS,
11867:•  j.  taCat-vohuni-  Adj.  'wobei  Blut  fliesst', mit  i^ara-  m.  (sd.)  Term.  techn.  für  die der  Schwere  nach  zweite  Art  der  Körper- verletzung'': yö  nanm  °nlm  x^arsm  (sd.) jainii  V.  4.34,  36.
13548:•  j.  Marazä-"  f.  'Bande,  Fessel':  vlspe kaoma  upastaomi  yatai  bar^uSva  gairi- nqm  ynliit  jqfnuk;a  raenqm  yafai  qzaku dtritatshs  jaininqm  *upa  *°BJ^a"  "alle H.  preise  ich,  sei  es,  dass  sie  auf  den Höhen  der  Berge,  sei  es,  dass  sie  in  den Tälem  der  Flüsse  sind;  auch  die,  welche in  Gefangenschaft  gehalten,  sich  in  den Fesseln  der  Weiber'*  befinden"  Y,  10.  17.
16205:•  j,  p3^.8ära-  Adj.  'des  Haupt  verwirkt, dem  Gericht  verfallen  ist,  tockündig':  ys mqm  .  .  därayehi  ya^a  tayam  -nm  nava (sd.)  akmi  'rS  Y,  /;.  3;  —  väcö  ysi  p^simHt sär?m  "  bunjainii  ". .  die  selbst  den  noch retten,  des  Haupt  schon  dem  Gericht  ver- fallen isr  Yt./4.46.
17695:•  j.  fraorasyan-  m.  EN.  emes  sagenhaften Einsehen  Königs  und  Feinds  dei  Iranier: ufritn  a:far)hm  3^ar»ns ..yat  isat  mairyO loirys  °«(NS.)"  Yti^.  56;  82';- —  artdvlm . .  yazata  mairyS  tütryS  'se  hankame  (sd.) paiti  *anAa  ztmS  Yt^.  41;  —  äat  ava.- patal  'se  türd  alvarpcä . .  avi  trayö  veuru.- ia&m..iat  :^arm5  isS  Yt 7^.58;  57;  — yim  (näml.  va^im)  barat  'se  türö  yat  .  . sainigäus  jaini  yim  barat  kava  haosrava yat  tUrS  jaini  *«  Yt. /p,  93;  —  mä  hwä kaomS  bandayäi  ya'^a  bändaya^  mairTm yim  tnirTm  "syarum  , .  *pairil,ifaxt3m  (sd.) ayankahe  Y.7/.7;  Yl p.  18,  aa,  Jg.TT.
22264:'c5  ySi  pisimcit  sanm  (Sp.  898  o.)  bun- Jainii  YL/4-46;  46;  —  havaram  va!a ipa.staomi  Y.  lO.  2';  F.  8\  —  varatayanuha nana  vaca  Y.  ro.  5;  Vr.  Ä  r=;    —   ku-^^ra
23027:mit  ni  'etwas  verüben  gegen  — ',  mit dopp.  Akk.:  aat  tä  (näml,  jainit) . .  hasS nivamaysn  daiva  "und  die  D.  taten  ihnen ..  Gewalt  an"  Yt.  79.  80.
27099:—  ime  alte  vacaysi  hfnti  at»rahe  mainySus •äj-jw  (statt  NS.)')V.io.  16.  a)in.Schlag, Hieb  (mittelst  einer  Waffe)':  yii  .  .  ut- gjnpbmal  '^tm  apüla  apaji^amiainH{sA.) YL74.46.  A)  im  Strafrecht;  a)  mit andus-  (sd.):  y3  nanm  andusa  °^a  Jainti V.  4,  a6,  39.  b)  wAfrazabai^ah-  (sd): yS  narptn  JrasäbatShaaham  *%gm  jainii  V. ^40.  4i;5-37.  0-'2,  '4-^.  AS.  "ä^m und  DS.  'äa/  als  Inf.  sbes.
27642:•  j.  zaini'gav-  m.  EN.  eines  von  Frat»- rasyan  getöteten  Feinds  des  iranischen Volks:  yim  (näml.  wa^ä?«)  barat  fratirait iBrB  yat  drvä  'gaul  jaini  Yti^.  93,
28959:irf.12;  —  pairi  dim  tanava  ('distinebo') ..  urvSmm  h°  vahiltat  attkaot  y.ig.T, 7/.  IS;  —  kö  .  .  a'^rB  ta/nus  darayat ('detinuit')  tanaot  h'  masyeht  V,  20.  i ;  — '  va^>mn>m  .  .  äalva  .  .  *apa  karsaym ('deripicbant')  jainii  h'  maiyakaäbyd  Yt 715.80;  —  ya'ia  vthrkB  .  .  barti^ryai  A' pu^r^m  niidaiydairyat  C^npiat')  V.JÄ38; —  vivaiti  ('fiigat')  Ai^  zrayaahai  A'  vouru- ka^SI  YtÄ4o;  —  Hyris  . .  yim  aaAal { jeci t')  »nxsd . .  airyöjcsu%  at  A'gardi^  s^an- vanttm  avi  gairlm  Yt. 8.6;  —  yS  ATm (näml.  daOtqm)  . .  utvasat  ('expedivit')  h° hinaiwyö  .  .  Yt,  13.  100;  —  upa  . .  naad rafS^wat  nänhanat  h'  ". .  intrabit  fa  naribus sva.)  per  nares"  V.J.  14;  —  s.  noch  unter bß(Sp.i749  0.)dieStcUenY57.i4,  V.33, y.3. 16, 13. 17.  ß)  bei  anderen  Verben; yS  naomyaSt  A'  daitihaol  . .  xrßm  (sd.) i»'zci>i7Ai(»'A' ('conspicit')  Yt/4.33;/6. 10;
=== BRT gena/gna ===
```


## [2026-09-06T14:54:07.184Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD zan ===\"; grep -n \"^zan\\| zan \\|zan  *\\[\" PHD.txt | head -20; echo \"=== PHD gran ===\"; grep -n \"grān\\|gran \" PHD.txt | head -20",
 "description": "Grep MacKenzie PHD"
}
```


### [2026-09-06T14:54:07.239Z] TOOL RESULT

```
=== PHD zan ===
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
286:brëzan [blycn' | M bryzn, N barézan] oven.
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
4897:zanisnt
5095:zan
=== PHD gran ===
2428:infinite anagr; ~ Light anagrān, anagr-rūšn(īh).
4422:23 Day pad Dén 27 Asman 24 Dén 28 Zamyad 25 Ard (Ahrišwang) 29 Māraspand 26 Aštād зо Anagran (v) Gāhs Hawan—morning Ēbsrūsrim—sunset to midnight Rapihwin—afternoon Ušahin--midnight to dawn Uzérin—evening
```


## [2026-09-06T14:54:17.747Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11540,11562p' BRT.txt",
 "description": "Print Bartholomae jaini entry"
}
```


### [2026-09-06T14:54:17.844Z] TOOL RESULT

```
Zum  V.  gan-,  —  Pu. :  ianän,  Sü. :  vighätaiam.
—  ')  S.  iSt.  saoi-  No.  3,
•  j.  *Jai8ysim''  Inf.  'um  zu  bitten':  yat bä  paiti  n3  aSava  frayat . .  äxstalia  dai' naya  va^a  framrU  (sd.)  iiit^Dmca  .  .  j° rämaca  s^ästnm  V.  _y.  1.
Zum  (p  Pracf.  16  des)  V.  gaä-;  s.  dam  GRiGOlRE KZ.  3S-  97^-1  wo  weilte  Litt.  —  Pu.:  iaiil, jSg.  —■  ')  So  die  meislen  Hds.;  NA,  'yq. Gdn.s  Bemerkung  datu  verstehe  ich  nicht.
•  ').  JaiwLvafra-  Adj.  'mit  tiefem  Schnee' : ipmö  ('des  Winters')  .  .  °raAe  V.  7.  27.
*jai'ari',  nnr  KompA-,  sva.  yri/ra-'t,  s.  unter imzi-.    —    Pü. :    inprnndkr,    d.  i.  ii./r  ..  .
—  i|  iVersch.  I"  -/  s.  S  23  b.
•  j.  Jafra-  Adj.  (fem,  °/-ä-)  'tief:  var5is .  .  'rahe  Yt.5.49;  ■y.46;  —  'ra  varayS Yt /O.  14;  F. /5J  —  bune  'ranam  vair- yanam  Yt  15.51,  V.  75.42 ;  —  ranAaya .  .  'raya  hasarirS.vlraya  Yt.  i^.  29;  — frayanä  (sd.)  , .  °ra  Yl/0.  112;  —  dsnui ..  'ra  (NSf.)  Aog.  77  (?)■).
Vgl.  JaJ-wi-   und  S  2J  b.  —  np.  :>ir/,  nbulj.iil.
—  Pii. ;  su/r.  —  ')  GdK.s  Ausgabe  enthäll das  Wort  nicht,  wohl  aber  sein  Glossar;  es muss  also  doch  hdslich  bezeugt  sein.  S.  auch unler  rfaeld-ainüa-.
j.  paiü.jatfhiil  N.  Sl:  s,  .^aw-  Sp.  498.
•  j,  Jatia-  Adj,  'schlagend':  *°nSu/tS''> saioin  (sd.)  nHt  janm  Yt/4.56->.  [V. z^.  40:  lies  daatm.jantm^
Zum  \.  gan-;  vgl.  ^gan-.  —  Npü.:
(mi  rmad  äti  tahrSni  i  Uad  az  x^ähis  i  iFadj.
—  ■)  Hds.  ja»a  kö.  —  J|  Sehr  unsichere  Stelle.
•  j.  Janant-  Adj.,  PPA.:  s.  ^gan-  (mit No.  3).
KompE. ■  j.  Janay-,  g.  J^nay-  'Weib,  Frau':  t^ä i  hati^yä  (sd.)  «ürj  a>S  JjtiayJ  (VF.)  Y. 53-  6 ;  —  da^va . .  vasnfmram  *apa.kariay.>n
(sd,)  jainis  (AP,)  Aa^a  masyäkaHbyS  Yt /§.  80.  a)    'Weib'    mit    verächtlichem
Nebensinn;  avanksnsämi  *janyöis^'>  ünam (sd.)  mairyayh  . ,  yä  .  .  Y.  lo.  15;  — jaitUnqm  *upa  *di^»aähu  (sd.)  Y. /0. 17; —  vispe  yätavS  pairikäsla  vispa  *janayS (als  AP.)'>  yä  drvaitti  V.  20. 10.
ai.  jänay-  t,  np.  iow.  —  VgU  Jqnay-.  —  mp. in«,  (in  A):JiA;  s.  noch  No.  i.  —  0  Pt4 usw. ;  NA.  janyaos  (woiu  Bthl.  AF.  3.  64). Das^  erklärt  sich  wie  in  al.  säkhyau.  Pu.: /fl  io»im,  — ')  S.  Vir.  NA./ancfl,  ohne  Epen- these 1
•  j.  jaini'  Adj.,  nur  KompA.  'tötend, mordend',
ZuraV.^-iii-.  —  Vgl.  unter  bina'  ondjin/rä; —  Unsicher.
•  j.  }aiiii.mahrka-  m.  'mordender  Tod': jaini.yaskahe  apanastahe  'kahe  apanailake V.  21.  2.
```


## [2026-09-06T14:54:19.241Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gouru-\\|gouru\\.\" BRT.txt | head; echo \"=== search Weib gena ===\"; grep -n \"yn'i-\\|gdna-\\|g»na\\|gana- f\" BRT.txt | head",
 "description": "Grep BRT gouru and gena"
}
```


### [2026-09-06T14:54:19.297Z] TOOL RESULT

```
10386:Vgl.  lat.  fei,  ßilis,  k<!.  iiüü  'Galle'.  —  Pü. : .  •  j.  gouru.zaoSra-  Adj.  (mask.  °ra-)  'des Hak  tirrcnihiSniouii ,  dam  als  Weihgüsse  schwer,  zähflüssig  Sind"':  ^»«•n'J "■■''*■"""'  t  Yt./o.ri3.
=== search Weib gena ===
```


## [2026-09-06T14:54:33.998Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zan ===\"; grep -n \"زن\\b\" HRN.txt | head -10; echo \"--- HRN gerân ---\"; grep -n \"girān\\|giran\\b\\|gran-\\|گران\" HRN.txt | head -20",
 "description": "Grep Horn for zan and giran"
}
```


### [2026-09-06T14:54:34.061Z] TOOL RESULT

```
=== HRN zan ===
--- HRN gerân ---
```


## [2026-09-06T14:54:36.430Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"zan\\b.*Weib\\|Weib.*zan\\b\" HUB.txt | head -10; echo \"--- HUB giran ---\"; grep -n \"giran\\|girān\" HUB.txt | head -10; echo \"=== PHD_mackenzie zan/gran ===\"; grep -n \"zan \\[\" PHD_mackenzie.txt | head; grep -n \"grān\\|gr'n\" PHD_mackenzie.txt | head",
 "description": "Grep Hübschmann and MacKenzie"
}
```


### [2026-09-06T14:54:36.518Z] TOOL RESULT

```
=== HUB ===
8169:zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
--- HUB giran ---
6066:ap. grab *ergreifen' ; gir^ 'Hals* = zd. grwH- ; giran 'schwer ,
8806:garenU' (?) ; giran *schwer H. 898 ; giriftan ergreifen , girav
=== PHD_mackenzie zan/gran ===
822:ab-tazan ['pten l ] watercourse.
836:Ab-zan [lpzn l IN'""'] bath.
1192:arzan [PC < A prg); 'len' I N ---] millet.
1193:arzan [)/e'n I M: 'rz'n, N -] valuable, worthy.
1626:brezan [blycn' I M bryzn, N barezml] oven.
2082:drozan [dlwcn l 1M, J drwzn] lying, liar.
3478: ......,-arzan [-)lc)n l ] deserving death.
3567:mihr-zan [mtr1zn l ] = mihrodruj.
4158:paymozan [ptmwcn l 1M pymwcn] garment, dress.
4434:rozan [lwen ' IN,....,] window.
```


## [2026-09-06T14:54:42.283Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8160,8175p' HUB.txt; echo \"=== 6060 ===\"; sed -n '6060,6070p' HUB.txt; echo \"=== 8800 ===\"; sed -n '8800,8810p' HUB.txt",
 "description": "Print Hübschmann contexts"
}
```


### [2026-09-06T14:54:42.342Z] TOOL RESULT

```
§ 120. Ap. i (= idg. g^^ g^h) im Aniaut = np. j,
z und 2:
a) = np. j im N. pr. Jamasp, jamasp = phi. famdsp,
arm. jamasp (PerserkSnig, Sebeos p. 19) = zd. jamaspa-^
aber gd. dBjamaspa-, syr. Zdmasp, gr. Zafidanjjg Tab. 142;
javidan *kauen\ afgh. zOvql, ksl. zwati (Wrzl. iran. jyu^
oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
unter c).
b) ^=np. z: zadan 'schlagen' = zd. ap. jan, skr. han\
zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
jycL-; zistan 'leben', zd. skr. jiv\ zahr (oben p. 71), arm.
zahr 'Gift' = zd. *fal^ra-; zdv 'Spalt' H. 649, oben p. 68
und 70.
Die Dialekte ^) haben hier j, i, wahrend sie fiir z ==
iran. z {g^^ 9^h): z setzen , siehe das Material bei Horn
p. 143—151. Daher zud H. 673 mit z in den Dialekten
=== 6060 ===
d) Einschub von i in: biradar *Bruder = ap. bra-
tar-; biristan *braten', iran. brij, skr. bhrjj; Jinn/ *Kupfer, =
arm. pUnj; diraz ^) 'lang = zd. drajah-; diraxt *Baum'; dirafs
Tahne = zd. dtafsa-; giriftan *ergreifen', girau^) *Pfand*y
*) Neben daraz JASB. XXXVII, 1, p. 37.
') Ueber giravidan *glauben* siehe § 53,- 172 -
ap. grab *ergreifen' ; gir^ 'Hals* = zd. grwH- ; giran 'schwer ,
afgh. LW. gran; girtstan *klagen'; xirad 'Verstand' = zd.
xratU' ; xirdmldan schreiten*, skr. kram; firistCLdan schicken ,
firista *Bote' = ^rz. frMa Shk. 245; firEsta *Bote, Engel' =
arm. hrestak; firod (fiirDd) *hinunter' = paz. fro^; fireftan
=== 8800 ===
batten, so wird auch ap. g entsprechend = g und y ge-
wesen sein.
§ 188. Ap. g im Anlaut und nach n = np. g: gOdan
coire', iran. WrzL gd, H. 833 ; gdm 'Sehritt' = zd. gama- ;
gav *Rind*, zd. gau-, dazu gosala (oben p. 95), gospand H.
942; gah *Ort, Thron' = ap. gadu-; garr 'Kratze', zd.
garenU' (?) ; giran *schwer H. 898 ; giriftan ergreifen , girav
'Pfand', ap. grh, skr. grabh; girtstan *weinen, oben p. 93
garm 'warm' — zd. garenia-; gire 'Hals' -- zd. grwd-
guftan *sprechen', ap. gaub-; gila 'Klage = zd. gereza-
gulu *Kehle', zd. garah-; gulula 'Kugel* H. 929; gand 'Ge-
```


## [2026-09-06T14:54:42.961Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"898\\.\" HRN.txt | head -20",
 "description": "Find Horn entry 898"
}
```


### [2026-09-06T14:54:43.006Z] TOOL RESULT

```
7800:898. girun 'schwer.
12377:girän 898.
14788:UiHdiita- 898.
16998:'.898.
17619:' s/(Myas 898.
17626:^urü- 898.
18376:E. baudrmsdin 898.
18467:K. gerun 898.
18475:K. gurö^ 898.
18476:K. gurun 898.
21332:! d. fartin 898.
```


## [2026-09-06T14:54:46.066Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7795,7815p' HRN.txt",
 "description": "Print Horn no. 898 giran"
}
```


### [2026-09-06T14:54:46.106Z] TOOL RESULT

```
angeblichen Sähnämevers belegt, der aber des Metrums
halber kein solcher sein kann.
897. geräziden 'schreiten .
ai. V^vra}', vrdjati schreiten, gehen, fortgehen'
(Rückert, ZDMG. 10, 165).
898. girun 'schwer.
Kä§. gerün, gurun^ guro.
Vergl. aw. gouru- (d. i. garii-) ^) in gouru.zaodra-
unlustiger Opferer' (Geldner); phlv. gar an 'schwer ^);
ai. gurü' 'schwer, vergl. Comp, gdrtyas-^ Sup. gdrisfha-.
Die Grundform hatte einen r- Vokal.
899. gurd 'Held'.
[/^var- 'beschützen, wehren', vergl. ai. vft- 'Heer ;
phlv. gurt 'Held' (AV.), gurtlh vd. 20 (21).
*) Bartholomae, Handbuch § 8.
*) Gehört hierher auch das rätselhafte phlv. grM (vd. 5 (48) GH.,
z. B. hi^-l gräi 'grosse Unreinheit*?), vergl. np. giräi No. 5 bei
Vullers?— 201 —
Dialektisch (K*ä§än, Q.) bedeutet (jurd, gurdl *hoch,
Höhe'.
900. {lygird (Endung von Ortsnamen).
```


## [2026-09-06T14:54:54.646Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('data/verification/page-20*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            for r in n.get('ref_check',[]):\n                if r['ref'].startswith('MON') or r['ref'].startswith('BQT'):\n                    print(f, r['ref'], r['status'], r['note'][:300]); print('---')\nEOF",
 "description": "Show how MON/BQT refs were checked previously"
}
```


### [2026-09-06T14:54:56.864Z] TOOL RESULT

```
data/verification/page-200.json MON:3434 supports MON_part1.txt line 48890, s.v. جوراب: '[= گوراب ـ گورب] … پایتابه‌ای که آن را از نخ‌های پنبه‌ای یا پشمی و یا ابریشمی بافند و پا را بدان پوشانند؛ ج. (ع.) جوارب.' Page number not checkable in the local page-less scan; the same text stands under فرهنگ معین on abadis.ir.
---
data/verification/page-200.json BQT:1786 supports Borhān-e Qāteʿ with Mo'in's notes, s.v. گرد, footnote 9: 'در پهلوی gurt . از ریشهٔ var ، پارسی باستان -vrta- ، «هوبشمان ۸۹۹»'. Read from the rendered scan (data/verification/sources/refs/ocr/BQT/1786.png = BQT_v3_picofile.pdf p.583, saved as 1786.vision.txt). CAVEAT: the running head of that leaf pr
---
data/verification/page-200.json BQT:1786 supports Mo'in's footnote 9 to گرد in Borhān-e Qāteʿ (scan p.1789 = BQT_v3 pdf p.583, saved at data/verification/sources/refs/ocr/BQT/1786.vision.txt): 'در پهلوی gurt . از ریشهٔ var ، پارسی باستان -vrta- ، «هوبشمان ۸۹۹»' — the Pahlavi form and its reading gurt are Mo'in's own.
---
data/verification/page-200.json BQT:1786 supports Borhān-e Qāteʿ s.v. گرد: 'و بفتح اول، مبارز و دلاور و بهادر و شجاع را گویند ۹' with footnote 9 giving the Pahlavi and Old Persian forms and the Ferdowsi verse that the chart prints. Read from the rendered image (ocr/BQT/1786.png, pdf p.583); the leaf's running head prints ۱۷۸۹, ~3 pages ahead of the
---
data/verification/page-200.json MON:3470 partial Mo'in's entry does exist and matches the gloss — MON_part2.txt (s.v. گول): '(ص.) ابله، احمق، نادان' — and abadis.ir's فرهنگ معین text reads '۱- (ص.) ابله، نادان. ۲- (اِ.) مکر، فریب. ۳- دلق.' But Mo'in gives NO origin tag, so he supports the word and its meaning, not the Indo-European derivation. The
---
data/verification/page-202.json BQT:1765 supports Borhān-e Qāṭeʿ printed p.1765 (= scan pdf 562, running head ۱۷۶۵), s.v. گام, Mo'in's footnote 5: 'اوستا -gāman «بارتولمه ۵۲۲»؛ پهلوی gām «نیبرگ ص ۷۷»؛ کردی gāv (قدم، لحظه، زمان)' — Av. gāman- > Phl. gām > NP گام, as drawn.
---
data/verification/page-202.json BQT:2223 partial Borhān printed p.2223 (= v4 pdf 306), s.v. نیام, Mo'in's footnote 7: 'پارسی باستان *ni-gāma؛ قس: سانسکریت ni (پیشوند) + …-gāma (گنجایش). قس: پیام. وجه اشتقاق قطعی نیست «اشتقاق ۱۰۹۳»'. Mo'in does propose *ni-gāma — Nourai's source — but explicitly marks the etymology as uncertain.
---
data/verification/page-202.json BQT:434 partial Borhān v1 leaf 660 (printed ~434) has the headword 'پیام — بروزن سلام، بمعنی خبر و پیغام باشد'; Mo'in's own note stands with پیغام on the next opening (leaf 671, footnote to printed p.444): 'پیغام … هم‌ریشه و هم‌معنی پیام «اشتقاق ص ۸۰»؛ پیغامبر و مخفف آن پیغمبر مرکب از پیغام + بر (مخفف برنده)'. The 
---
data/verification/page-202.json BQT:1451 supports The Borhān page Nourai means is printed p.1449 in the scan (v3 pdf 244; the volume's running numbers drift by ~2 pages around here), s.v. فرجام, Mo'in's footnote 2: 'پهلوی frazhām «مناسی ۲۷۴» و frajāmīnītan، frajām از پارسی باستان *frajāma (از gam «رفتن») «اشتقاق ۸۱۸»'. That is precisely the arrow f
---
data/verification/page-202.json BQT:166 not_found Borhān v1: the انجمن headword sits on leaf 385 of BQT_v1_pages.txt ('انجمن — بفتح اول و فتح میم و سکون نون. مجلس و مجمع را گویند'), i.e. printed p.164-166 as cited, but the footnote band of that leaf was lost in the djvu OCR, so Mo'in's etymological note itself could not be read. Vol. 1 is not in th
---
data/verification/page-202.json BQT:1771 supports Borhān-e Qāṭeʿ printed p.1771 (= v3 pdf scan p.568, running head ۱۷۷۱), s.v. گاه: 'بر وزن ماه. تخت پادشاهان و کرسی زرین را گویند – و بمعنی وقت و زمان باشد … و بمعنی جا و محل و مقام هم هست'; Mo'in's footnote 3: 'پارسی باستان gathu (مکان، تخت)، اوستا gātu (جا، تخت)؛ پهلوی gās … ارمنی gah (تخت، کرسی) …
---
data/verification/page-202.json BQT:1773 supports Same volume, printed p.1773 (v3 pdf 570), s.v. گاهواره: Mo'in's footnote 2 'ظ. از: گاه + واره (پسوند) از مصدر bar [بردن]، لغةً حامل تخت (کودک) – گهواره (مخفف) – گاواره؛ پهلوی gāhvārak «تاوادیا ۱۵۱»' — the source of the extra گهواره and of node 6's gātu-bar.
---
data/verification/page-202.json MON supports Nourai cites MON without a page; the entry is Mo'in's جاه (MON_part1.txt line 47042): 'جاه: [- گاه، معرّب] (اِ.) مقام، منزلت، درجه، رتبه' — the Persian word, tagged as the Arabicised form of گاه, with exactly the gloss 'position' Nourai gives.
---
data/verification/page-202.json BQT:2368 supports Borhān printed p.2368 (= v4 pdf 451), Mo'in's footnote 5 s.v. همدان: 'پهلوی Hamadān «مارکوارت، شهرستانهای ایران»، پارسی باستان Ha(n)gmatāna «کنت، پارسی باستان»، … «اشپیگل» … که پایتخت شاهی در عهد مادها بود. در عیلامی ʾa(g)-ma-da-na، آکدی a-ga-ma-ta-nu، یونانی Agbatana / Ekbatana … محتملاً مشتق از …'
---
data/verification/page-202.json BQT:2368 supports Mo'in's footnote 5 to Borhān p.2368 s.v. همدان (v4 pdf 451) sets out exactly this: 'پهلوی Hamadān … پارسی باستان Ha(n)gmatāna «کنت» … در عیلامی …، آکدی …، یونانی Agbatana / Ekbatana …' — the Persian, Greek and cuneiform names of one place.
---
data/verification/page-202.json MON:1746 not_found Mo'in's Farhang-e Fārsi p.1746 could not be read: the local OCR (MON_part1/part2.txt) has no clean headword block for زمان (only compounds such as 'قد زمان', 'هر زمان'), and the web copies of Mo'in (abadis.ir/fatofa/زمان, fetched) render their content in JavaScript, so the archived text contains onl
---
data/verification/page-202.json MON:1746 not_found As for node 13: Mo'in p.1746 is not readable in the local OCR (MON_part1/part2.txt carry only running uses of ازمنه, e.g. 'هنگام‌ها؛ روزگارها، ساعات، ازمنه، اوقات', not the headword block), and the abadis/vajehyab copies of Mo'in are JavaScript-rendered, so the archived page text contains no entry.
---
data/verification/page-202.json BQT:2383 supports Borhān-e Qāṭeʿ printed p.2383 (= v4 pdf 466), s.v. هنگام: 'بر وزن اندام، بمعنی وقت و زمان و گاه باشد – و بمعنی موسم و فصل هم آمده است'; Mo'in's footnote 1: 'پارسی باستان *hangāma- (وقت، زمان)، قس اوستایی *hankāma-…؛ پهلوی hangām (پازند hangām) «اشتقاق ۱۱..»؛ ارمنی hangam (دفعه، مرتبه) … «هوبشمان ۱۱۳
---
data/verification/page-202.json BQT:2383 supports The Borhān page cited is the هنگام article itself (printed p.2383, v4 pdf 466), with Mo'in's footnote 1 giving 'پارسی باستان *hangāma- (وقت، زمان) … پهلوی hangām (پازند hangām)'; the same page carries هنگامه, هنگامه‌گیر and هنگامی, and a Ferdowsi line for the sense 'time'.
---
data/verification/page-203.json MON:75 supports Mo'in s.v. آکروبات (read through vajehyab, the Mo'in section): 'رُ [فر.] بندباز، ورزشکاری که کارهایی مانند بندبازی، ژیمناستیک و ... را انجام می‌دهد' — '[فر.]' = French, i.e. Mo'in's own page (vol. 1, p. 75 of the alef section) says what the arrow says.
---
data/verification/page-203.json MON:1588 supports Mo'in s.v. دیابت: 'مرضی که به واسطهٔ زیاد شدن مقدار قند خون ...' with French origin; the local OCR has the entry too (MON_part1.txt line 64279: 'دیابت: ... (بز.) مرضی که به سبب ازدیاد مقدار خون تولید گردد'), though the OCR carries no page numbers so p.1588 itself could not be re-counted.
---
data/verification/page-203.json MON:1244 not_found Mo'in's page could not be checked: the local Mo'in OCR (MON_part1/2.txt) has no جنبیدن headword — the word occurs only inside other entries (e.g. lines 81144, 41167) — and the files carry no page numbers, so p.1244 could not be located. Mo'in's Pahlavi bracket for جنبیدن is the likely support, since
---
data/verification/page-203.json MON:1244 not_found same as node #15: the OCR'd Mo'in on disk has no جنبیدن headword and no page numbers, so the cited page could not be read; the claim (Pahlavi junbītan > NP jonbīdan) is nevertheless what MacKenzie and Nyberg give.
---
data/verification/page-205.json BQT:606 supports Borhān-e Qāṭeʿ, entry جیوه ('بروزن میوه، سیماب را گویند ... و بعربی زیبق خوانند'), BQT_v2_pages.txt leaf 64 (printed ≈604-606; the file's leaf→page offset drifts ±2 in this stretch). Moʿin's footnote there: 'در اوستا žīv- آمده که در پهلوی zīvandak شده بمعنی زنده و نیز بمعنی گردنده و جهنده ... در فار
---
data/verification/page-205.json BQT:1038 supports BQT_v2_pages.txt leaf 500 (printed ≈1038-1040), footnote 8 on زنده: 'پهلوی zīndak (حی) از zīvandak با پسوند -ak ... از žīv- (zīvistan زیستن) ... zīndakīh'. Confirms both zīwandag and the infinitive, and gives the modern reading zīvistan.
---
data/verification/page-205.json MON supports Moʿin, Farhang-e Fārsi, s.v. جیوه: '[= ژیوه > زیبق، معر.]' (MON_part1.txt line 49349) — Moʿin himself makes جیوه the Persian original and زیبق its Arabicised form. No page number is given by Nourai, and the six-volume edition is not online, so the page cannot be checked.
---
data/verification/page-205.json MON:1768 partial The six-volume Moʿin is not digitised, so p.1768 could not be opened; the two-volume Adena condensation carries the same statement s.v. جیوه ('[= ژیوه > زیبق، معر.]', MON_part1.txt line 49349) and lists زیبق as a synonym of جیوه (MON_part2.txt lines 54257, 62922). Content supported, page number unch
---
data/verification/page-205.json BQT:1872 supports Borhān-e Qāṭeʿ p.1872 (vol.3 scan, pdf page 669; printed = pdf + 1203), footnote 1 to the entry گیومرت: 'پهلوی Gayōmart. اوستایی Gayō_maretan، بارتولمه ۵۰۳ ... جزء اول «گیو» و «گیه» بمعنی جان و زندگی است و جزء دوم «مرتن» صفت است بمعنی مردنی و درگذشتنی، وبتعبیر دیگر مردم ... پورداود، یشتها'. Exactly 
---
data/verification/page-205.json BQT:1872 supports Borhān p.1872 (vol.3 scan pdf 669): headword 'گیومرت ... نخستین کسی را گویند که در عالم پادشاهی کرد ... چه کیو بمعنی [جان] و مرت بمعنی زنده آمده است ودر لغت متأخرین ... و حال آنکه این رسم فارسی قدیم است ودر کلام فارسی قدیم ثای مثلثه نیامده است'; footnote 1 as quoted on node 6.
---
data/verification/page-205.json BQT:1868 supports Borhān-e Qāṭeʿ p.1868 (vol.3 scan, pdf page 665), entry گیتی 'بمعنی دنیا و جهان' with the compounds گیتی‌نورد, گیتی‌فروز; Moʿin's footnote 4: 'اوستا -gaēθa- ... پازند gētī, gētīh، پهلوی gētēh ... هوبشمان ۹۴۹ ... و قس: گهان. جهان.' The page also carries the گیهان entry with the footnote 'پهلوی gēhān 
---
data/verification/page-205.json MON supports Moʿin, entry ویتامین (MON_part2.txt line 87635) with the Latin-script European headword and the tag '(بز.)'; the run-on entries ویتامین‌ها (line 87645) and the note 'امراض ناشی از فقدان ویتامین را آویتامینوز [گویند]' (line 87642) show the French-based terminology. No page number was given by Nourai.
---
data/verification/page-205.json MON:4500 partial The six-volume Moʿin (vol. 4 = foreign compounds, where p.4500 would fall) is not digitised; the two-volume Adena condensation carries the entry 'میکرب: [European headword] (بز.)' (MON_part2.txt line 70425) and many run-on uses (میکرب‌ها, میکرب‌کش, MON_part1.txt lines 4095, 11780, 24869). Content su
---
```


## [2026-09-06T14:55:03.348Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | sed -n '1,3p'; echo ===; grep -n \"زن —\\|^زن\\b\" BQT_v2_pages.txt | head -20",
 "description": "Locate zan in Borhan vol2"
}
```


### [2026-09-06T14:55:03.416Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T14:55:05.122Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON gerân ===\"; grep -n \"^گران\\|گران:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== MON barium ===\"; grep -n \"باریم\\|بارومتر\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Moin for geran, barium, barometer"
}
```


### [2026-09-06T14:55:05.242Z] TOOL RESULT

```
=== MON gerân ===
MON_part2.txt:16613:گرانبها» با ارزش» انگشتر قیمتی 
MON_part2.txt:30351:گران: 2030 (ضن:] کیت تقیل» وزین؛ 
MON_part2.txt:30373:ضرب گران: (م.) ضرب سنگین؛ ضرب 
MON_part2.txt:30391:گرانبار: ۲-.:۱ (ص‌مر .) آنکه باری ک ان 
MON_part2.txt:30402:گرانها: 86۲808 (ص‌مر.) بر قیمت» 
MON_part2.txt:30405:گران‌پایه: :5۷ج (ص‌مر.) (کد.) 
MON_part2.txt:30408:گران‌جان: «15-.: (ص‌مر.) بسیار مقاومت 
MON_part2.txt:30421:گران‌سایه: (0-)۵272-.ع ( کد.) صاحب جاه و 
MON_part2.txt:30429:گران ۳ ۰ ۶ 0 (مسص‌ل.) تک 
MON_part2.txt:30437:گران‌فروش: 60758 (- گران‌فر وشنده] 
=== MON barium ===
MON_part2.txt:79539:باریم و کلسیم بقیه در آب حل می‌شوند. ۴ 
MON_part1.txt:788:دوباریم قرار داد. از ترکیب آنها آب 
MON_part1.txt:20212:بارومتر: ۲ لامر.) میزان الهواء» 
MON_part1.txt:30100:بجای صفحهة پلاتینو سیانور باریم صفحة 
MON_part1.txt:81383:محلول شوند و فقط سولفات سرب و باریم 
MON_part1.txt:81392:انواع متعدد دارد مانند سولفات باریم»
```


## [2026-09-06T14:55:08.739Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30348,30356p' MON_part2.txt; echo \"=== barometer ===\"; sed -n '20208,20218p' MON_part1.txt; echo \"=== barium headword search ===\"; grep -n \"باریم:\" MON_part1.txt MON_part2.txt | head",
 "description": "Print Moin geran and barometer entries"
}
```


### [2026-09-06T14:55:08.833Z] TOOL RESULT

```
گرامیکث» به.) آمده و «گرام ۲ - که در 
تداول بجای گرامی پا کرام عربی (ج. کریم) 
استعمال کنند . درست نیست. 
گران: 2030 (ضن:] کیت تقیل» وزین؛ 


مق. سکك» خفیف. سخت؛ شد ید. بررکگک» 
عظیم. آنچه قیمتش به نسبت اشیای دیگر 
زیاد باشد؟ نمین 4 مسة. ارزان. سار انسوه» 
=== barometer ===
بارور: 03۲-1 (ص‌مر.) میوه‌دار (درخت)» 
میوه دهنده» ئمر دهنده» مئمر» بارآور؛ 
بردره 

بارومتر: ۲ لامر.) میزان الهواء» 
هواسنج. 

بارون: 02 (.) یکی‌از عنوان‌های اشراف 
و نجبای ارو پا. 

باره: (*-)۱2:2 [- بار] (.) جرم. بار. باره 
=== barium headword search ===
```


## [2026-09-06T14:55:10.093Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زن\" BQT_v2_pages.txt | grep -n \"بروزن فن\\|زن -\" | head; echo \"=== leaves ===\"; grep -n \"pdf page\" BQT_v2_pages.txt | head -5",
 "description": "Search Borhan v2 for zan"
}
```


### [2026-09-06T14:55:10.178Z] TOOL RESULT

```
643:7051:‫بروزن فند » مقدار غیرمعین‬        ‫چند ‪°‬‬                 ‫و چوبدستی که شتربانان و امثال ابشان بدست‬
=== leaves ===
```


## [2026-09-06T14:55:19.995Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt; echo ...; grep -c $'\\f' BQT_v2_pages.txt; grep -on \"page [0-9]*\" BQT_v2_pages.txt | head -5",
 "description": "Inspect BQT v2 pages file format"
}
```


## [2026-09-06T14:55:20.320Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1781 2>&1 | head -40",
 "description": "Fetch Borhan page 1781"
}
```


### [2026-09-06T14:55:22.480Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
...
680
```


### [2026-09-06T14:55:30.354Z] TOOL RESULT

```
REF: BQT:1781  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 578  OCR-lang: fas

-۱۷۸۱- کران‌پشت
گرا رد۱ < بروز ن کدازد » بمنی‌جلوه گراشیدن* » بروزنومعنی‌خراشیدن
کند واز روی از وتکیر بخرامد وبراه رود . باشد- وبمعنی پربشان شدن وکردن هم آمده
گر از نده۲ - بروزن گدازنده, ازروی | است .
تاز وتکبر خرامنده وبراه رونده راآکوبند . گرامی۱۰ * بر وزن نظامی » بمه‌نی
گراذه؟۴ - بنم اول وفتح رابع »۰ نام عزیز ومکرم ومحبوب وبز رکه باشد -
پهلوانی است ایرانی که در جنکه دوازده رخ گر ان - بکر اول بروزن نشان. نقیل
سبامك رابقتل آوردگ - وخوك‌نررا هم‌میگوبند | وسنگین باشد که در مقابل‌خفیف وسبك‌است۹۱-
که کراز باشد ۴ . ودر مقابل ارزان هم هت؟۴٩‏ - وضم اول دستهة
گر از یدن* * بروزن شماریدن, بناز کندم وجودرو کرده را گوبند که‌باخوشه‌باشد۹۴.
وتکبی وغمزه براه رفتن وخرامیدن باشد. گر آن‌باد - بابای‌ابجد پروزن‌نشانداره
گر اس۱ < بفتح اول بر وزن هراس , | بمعنی باردار وبازور باشد اعم از درخت وحیوان
بممنی تکه ونواله باشد وبعریی لقمه کوبند۷ . | وانان - وشخصی را نیز کویند که مال واسباب
گراش۸ - بروزن ومعنی خرائی باشد وبته وغنایم بسبار داشته باشد - وکنابه‌ازاسان
که ازخراشیدن‌است - وبمعتی پریشان‌وپرا کنده وحیوان آبتن هم هت .
هم هست. . گران پشت - بکر اول و ضم بای
۱ - مضارع از «گرازیدن» (هم.) . ۴ - اسم فاعل از «گرازیدن > ۰
۳ < کراز (هم.) . ۴ - وی ازخاندان کیو بود" رك: فهرست ولف ۰
8 - از : کراز میدن (پسوند مصدری ) ؛ هندی باستان - [۷۳۵ , ۷۲۸[811 ( قدم
نهادن ۰ رفتن) «اسشق 2۸۹۷ ورك : هوبشمان » اس ۰
باغ ملك ترا مباد خزان تا درو چون بهار بگرازی .
آ#وری آبیوردی «رشیدی» .
‎٩‏ - در خراسان کراسه ( با ضم اول ) بمعنی باقی مانده طمام است .
۷ - جمله‌نستهای الوان بهشت يك کرای ازخوان اسان تونیست.
غنایری رازی «جهانگیری » .
۸ - ر4 : خراش * غراش » ورك : کراش . ‎٩‏ - رك : خراعیدن * غراشیدن +
ورك : کراشیدن ۰ ۰ در پهلوی 82۳2016 ( عزیز» معزز ) از : 8872:
پذیره فزستاد خرو سوار کرانمایگان کرامی هزار .
فردوسی طوسی «شاهنامةٌ بخ ج٩‏ ص ۰4۲۷۹۳
رك : اضافه بقلم نگارنده چ ۱ پایان کتاب ص نله بیعد .
۱- پهلوی 82728 (سنگین . تقیل) » ازاوستا - 801۲1 از- 8871 «بارتولمهع ۰۵۱
۶ انیب رکه ص ۷۸ پارسی باستان 7 - 87382 5 « هوبشمان ۸۹۸ ورك : اسشق۸۹۸؛
کردی 8101138 ( نقیل کران » سخت ) « ژابا ۳۵۸ > : « فی‌الجمله بانواع عقوبت کرفتار
آمدم , تا درین اهفته که مژدة سلامت حجاج برسید » از بند کرام خلاس کرده ( ملك ) .>
«کلتان ص ۳۸ . ۴- کیلکی81۳28. :
۴- بك کران از کشت زارخوشتن بهتر از صد خرمن مال کان.
غضابری رازی «رشیدی» .
```


## [2026-09-06T14:55:43.624Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1033 2>&1 | head -45",
 "description": "Fetch Borhan page 1033 (zan)"
}
```


### [2026-09-06T14:55:45.757Z] TOOL RESULT

```
no scan of BQT covers printed page 1033 (see 'scans' in refs_online.json)
```


## [2026-09-06T14:55:50.303Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 496 497 498 499; do echo \"###### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done",
 "description": "Print Borhan v2 leaves around zan"
}
```


### [2026-09-06T14:55:51.931Z] TOOL RESULT

```
###### leaf 496
                                        ‫بیان بدانهزم‬

               ‫در زای نقطه دار بانون مشتمل بر هشتاد لفغت و کنابت‬
‫کنابه از موج پیالةً شراب است ‪ -‬و خطی را‬           ‫ثالی ‪.‬ممروف‬    ‫وون‬‫کول‬
                                                                      ‫سح ا‬
                                                                         ‫رن = بفت‬
‫یگزومند منحن یکه از شراب در بیاله معلوم‬              ‫ااوهلی‬
                                                          ‫یضم‬
                                                            ‫کوب‬
                                                              ‫است کهنقیض مرد باشد ‪٩‬‏ ‪-‬‬
                        ‫مشود تپارشدن بیاله ‪.‬‬     ‫است که آلرا دو سگروند و در میان زراعت‬
‫ر نباره » بنتح اول و بای اسجد (‪» )۲‬‬                                         ‫کندم و جو روید ‪.‬‬
‫را گومند چنانکه‬    ‫بر وزن انگاره » زن دوست‬       ‫زفراج‪ -‬بض اول و تالی مشدد بالف‬
‫را ‪ ۴‬چه باره بمعتی دوست‬      ‫ست‬
                              ‫دهوپر‬
                                  ‫غلام بار‬       ‫کشیده و بجیم زده ‪ ,‬چرب رود گوسفند را‬
                              ‫هم آمده است ‪.‬‬       ‫گوبند که دبه و برج را باهمکوفته درمیان‬
‫ز بر ‪ -‬بفتح اول بروزن چتبر ‪ ۰‬چهار‬                   ‫بشنعدروبی‬
                                                            ‫آن پر کرده براوغن بربان کرده با‬
‫چوب باشد مالند نردیان دو یایهکه ميان آبرا‬        ‫میب خوانند ‪ ۴‬؛ وباجیم فارسی‌هم آمدهات ‪.‬‬

 ‫ببافند و از خاك وخشت‬     ‫م‬   ‫برسمان بالوا‬
                          ‫چرربا‬                      ‫ن‬
                                                     ‫وددزبر‬
                                                          ‫ونی حش‬
                                                               ‫رنار ‪ ۴‬سس اول ا‬
 ‫و امثال آن پرکنند و د وکس برداشته اجزایی‬        ‫شته را گومفند عموماً و رشته ای‬
                                                                              ‫هر‬‫کفار » ر‬
‫یجابی برند و بعربی مثقل خوانند ® ‪ -‬ومشکی‬         ‫هرستان باخود دارید‬    ‫اش‬    ‫کهبت برستان و‬

‫را نیز کفته‌اند کهبردو سرآن دو چوب تعببه‬                                                ‫خصوصا‬
‫ر‪-‬شوك رانیز‬
          ‫زند‬
            ‫داون آب کش‬
                     ‫کرده بابشند‬                 ‫رنارساغر = بکسر رای قرشت( ‪)۱‬؛‬

                                     ‫ایجد ‪۰‬‬    ‫چك‪:‬‬   ‫(‪)۲‬‬        ‫(‪ )۱‬چك‪ - :‬قرشت ‪.‬‬

 ‫‪ ۱‬بهلوی ‪( 8202‬زن ‪ .‬زوجد) »اوستا_‪ [103 - , 102‬د بارتولمه ‪ .»+۳۰‬رك‪:‬یب رکه‬
  ‫‪înaJ‬‏ ) زن ‪ ۰‬زوجه)» ارمنی ‪nik‬‏ (زن ‪ ۰‬بانو) > کردی‬        ‫‪ ١ ۸۵ -‬هندی باستان ‪-1 -‬‬       ‫‪۷‬‏‬
  ‫(ازا ‪ , ) [06‬اففانی ‪ ° 12001 . [1281‬بلوچی ‪ [02‬شەنى ‪ , 01018‬سریکلی‬
                                                                  ‫‪ (۵‬زن ) ز‬
          ‫‪ . 01112,‬منجی ‪« 2801112‬اسذق‪»»۸۹1‬اورامانی ‪ 0802‬د‪ . 4‬اورامان ‪- ۸۲۱‬‬                ‫‪0‬‬
      ‫در عمرخوش آوبز له در عمر دراژ ‪.‬‬                ‫لنیه برنج هست زناج بهل‬
                                                                          ‫قچو‬
                                                                            ‫‪- ۴‬‬
   ‫بسحاق اطعمه «جهانگری»‪.‬‬
                                                       ‫رك‪ :‬رونج » روفجو » ریونجو » ریولجه ‪.‬‬
  ‫مصفر ‪ 8007‬بمعنی کمربند ومنطقه « فرهنک بوئانی ‪ -‬انگلیسیلیدل‌وامکات >‬                      ‫‪0‬‬
  ‫«تفس» زنار کمربندی‌بوده که ذمیان صرالی درمشرق زمین بامر مسلمانان مجبور بوده‌اند داشته‌باشند‬
  ‫نا بدینوسیله از مسلمانان ممتاز گردند » چنانکه بهودبان مجبور بوده‌اند عسلی ( وسله‌ای على‬
  ‫کرتاب های فارسی گاه زنار تین ( = کی ( («م‪).‬‬
                                            ‫رنگی ) بر روی لبای خود بدوزند » د‬
                             ‫زرنشتمان اطلاق شده است ‪ .‬رک ‪ :‬لو روزنامه ‪ .‬تمایقات ص ‪. ۳۲۱‬‬
  ‫© = زیل (ه‪.‬م‪ ).‬اکنون ‪ 20022‬کوند ‪:‬‬                    ‫‪۴‬ش‪-‬اعر بازه ‪ ,‬رکه ‪ :‬باره ‪.‬‬‫و‬
      ‫همی سوزد میان راغ ‪ .‬عثبرها بمجمرها‪.‬‬            ‫همی ریزد هيان باغ › للها بزتبرها‬
  ‫د منوچهری دامغالی‪۱‬؟‪.‬‬

###### leaf 497
      ‫و‬                                                                                                       ‫زلبری‬

 ‫صنبر زنبوراست‪ -‬وتوپ‬           ‫ز بورگ‬
‫کوچك را گیوزبند ‪ -‬و نوعی از اسلحه باشد‬                     ‫طوعام کنند ولخدوربعربی‌البرباریس خواند ‪۱‬‬
                          ‫سرآن بفابت تبز ® ‪.‬‬              ‫‪-‬نابه ازدبوث‬
                                                                     ‫و نام یکی ازآلات‌جنکه است ک‬
‫ر نبو ره = بروزن طنبوره ل‪.‬وعی ازساز‬                      ‫ور عردمی باشد که در محافل و مجالس قابل دقع‬

‫باشد که بتر اهل هند نوازند » و آن چوبی‬                    ‫کردن باشند ‪ -‬و شاهد بازار را نگیوزیند وم‬
‫بود که برد وسرآن دو کدو نصب کرده باشند و‬                 ‫رایر باد‬       ‫خود‬   ‫دهان‬   ‫باشد که کسی‬   ‫آن‬       ‫الت‬   ‫اول و‬



 ‫دو تار بر آن بته نوازند و آنرا کنگری یز‬                 ‫کند و دیگری بنوعی دست (‪ )۱‬بر آن زلدکه‬
‫کوبند یکسر کاف ‪ -‬وزنبور سیاه بز رکک راهم‬
‫میگوبند‪ -‬و نوعی از پیکان تیر واسلحة جنگه‬                   ‫ثریری = بابای ابجد (‪ ) ۲‬بورزن‬
 ‫کوچك رنایز گفته‌اسس ‪٩‬‏‬        ‫باشد ‪ - ۷‬و نوپ‬
                                                                    ‫روایند ‪.‬‬
                                                                           ‫لنگری» کشتی و جهاز بزر که ک‬
 ‫و بمعتی گروه بیار و مردم انبوه هم بنظرآمده‬
                                                 ‫اه‬       ‫‪ -‬سم اول و الث وغین‌و‪-‬کون‬                   ‫برقل‬
                                                          ‫وخر که لام باشد ؛ آنت که شخصی‌دهان‬
                                                                                           ‫انی آ‬
 ‫ر یه ‪ = ۲‬بفتح ارل و الث بروزن‌انبه‪.‬‬
‫کلی است سفید که ب رکه کلهای آن دراز و‬                     ‫خود را پرباد کند و دیگری چنان دستی بر آن‬
                                                           ‫زندکه آن باد باصدا از دهان از بجهد ‪# . ۴‬‬
        ‫خوشبوی میشود و معرب آن زبق است‬
‫فزبربر * س با بای ابجد بروزن زنجیر ‪.‬‬                     ‫ر بل ‪ -‬بروزن تنبل“ بمعنی زابر است‬
‫ظرفی باشد که آنرا حاصزیر بافند و دو دسته‬                  ‫ات ویمسشُی زرشك‬            ‫کشند ‪۳‬‬   ‫که بدان خاك وخشت‬


‫برآن‌صب کنند گووشت وبرنج وامثالآن‌درآن‬
               ‫گذارند و ازجایی بجابی برند ‪.‬‬              ‫نم میم ‪٠‬‏ فرماق و کس‬                 ‫هر ‪= ۵‬‬        ‫رن‬


  ‫ملع‪۰‬نی‬
       ‫بدی‬
         ‫فن‬     ‫وزن‬       ‫زرنبیل ‪٩‬‏ بر‬                           ‫کش رکاویند و بعربی قواده خوانند ‪.‬‬
‫زبیر است کهظرفی باشد ازحصیر بافته که‌چیزها‬                 ‫ربور سرخ = کنابه‌از اخگرآاش‬      ‫ل‬
           ‫درآن نهند و از جابی بجابی برند ‪.‬‬                                                                       ‫باشف ‪.‬‬


                                                 ‫(‪ )۲‬چك ‪ :‬بابا‪.‬‬               ‫(‪ )۱‬چش‪ :‬چنان دستی ‪.‬‬
                            ‫‪ :‬رشك‬   ‫انير باریس» رکه‬        ‫ومخفف‬         ‫ظ مصحف‬       ‫‪ -‬باین معنی »‬     ‫‪۱‬‬

               ‫نب‪:‬ر‬
                  ‫زکه‬
                    ‫‪ ۴‬ر‬                      ‫‪.‬‬     ‫رکه ‪ :‬زس‬         ‫‪۴‬‬                   ‫‪E‬‬
   ‫‪ -‬ممرب آن «زلبر کے (بضم اول وسوم وفتح چهارم ) کمانی آهنین مرادف «نابض»‬
    ‫عربی "تفس » رکه ‪ :‬زلبوره‪ :‬ونیززابور که آلتی‌است درساعت که چرخ های ]را ‪E‬‏ مر‬
                                                                                                  ‫آن‬
                      ‫‏‪ = ٩‬زبور که (ھ‪.‬م‪:).‬‬               ‫‌هز برکه» (جنماولوسوم وچپارم) «المنجد» ‪.‬‬
                 ‫‪۰.‬‬     ‫شده| هن‌وسنك را رویرش‬           ‫زورة تىر زلنور تیش‬
                                                                         ‫بلب‬
                                                                                                      ‫و‬
                            ‫نظامی کنجوی ک«نجینه‬
                                                                                                      ‫و‬
                 ‫‪. °‬‬

                  ‫زتبیل (ھ‪ .‬م‪: ).‬‬    ‫=‬   ‫‪۸‬‬             ‫‪ ۷‬رکك‪ :‬زق (ح) ‪۰‬‬
###### leaf 498
     ‫زتجیر‬
                                                                                                                  ‫‪ ۵‬ات‬       ‫ی‬




                                                                    ‫زرفج د بفتح اول وسکون الیو جیم‪.‬‬
                                                                   ‫و نخر‬            ‫بمعنی گریه و لوحه کردن است ‪۱‬‬
                                                                   ‫ولاخ رایزکوبند کهرعکسیخ‌باشد ‪ -‬و کرهی‬
                                                                    ‫برمی آید ‪ -‬ویم اول‪,‬چانه‬               ‫که از تنه درخت‬

                                                                   ‫‌بعخربویانند ‪- ۴‬ومطلق‬  ‫نو‬  ‫ذوب‬
                                                                                            ‫قند‬  ‫و زلخ را گ‬
                    ‫‪:‬‬                      ‫آواز طولانی (‪)۱‬‬         ‫صمخ را یز گفته‌اند خواه صمغ عربی باشد و‬
                                                                   ‫خواه غیر عربی ‪ -‬و بکر اول زاح سفدد باشد‬
                                                                    ‫ویعربی شب ممالی خوالند بتشدید بای ابجد‪.‬‬
‫‪ -‬باجیمفارسی بروزن )‪(1‬‬                     ‫ر نچك ‏‬
                  ‫وقحبه راگونه ‪.‬‬                ‫حزن‬
                                               ‫شه‬     ‫زر‬
                                                  ‫فدكا‪۰‬‬               ‫آن‬
                                                                       ‫ست ‪ ۴‬و‬
                                                                            ‫معرب زنگار ا ت‬                  ‫ر نجار‬

‫راجه » درد اندرون‬                 ‫زن‬ ‫ر نحه =‬
                                   ‫وبر‬                                ‫دو لوع میباشد‪ :‬معدنی وعملی‪ .‬بهتربن مآعندلی‬
                ‫شکم و زحیر باشد ‪ -‬ب‬
‫ومعنی کربه و نوحه‬
‫را فيز‬       ‫لل‬         ‫بو‬        ‫اس‬       ‫هم آمنه‬      ‫وهو به‬
                                                                                                          ‫مرهمها بکاربرند ‪.‬‬
                                                    ‫گوند ‪. ۷‬‬        ‫آوه‬                             ‫عیا‬            ‫‪6‬‬     ‫‪۰‬‬




    ‫ورن‌چمجهه‬
             ‫‪4‬‬     ‫بر‬
                             ‫فا‬   ‫‪ ۸‬كت با‬
                        ‫با چیم‌فارسی‬
                                                                            ‫ا‬                  ‫‪١9‬‬   ‫نوعی از ‪EE‬‏‬

‫ست که زن قاحشه وقحبه باشد ‪۰‬‬                                                            ‫کفته‌الد ‪ .‬مرای آنجم‬
                                                                    ‫‪-‬م المهای سرد رانافع‬
‫ویعربی‌ملله‬             ‫‏‪e‬ست‬                                                                                                 ‫ی‬
‫شار‬      ‫زمن‬       ‫باشد که سیت‬         ‫هنی‬                          ‫ر تحرف " = بمعنی شنجرف امت »‬
                                                                    ‫آن‬     ‫ین‬
                                                                            ‫ر‪۰‬‬‫تملی‬
                                                                                 ‫بلیهرع‬
                                                                                      ‫ونهری باشد کا‬
                                                                                                  ‫جآ‬‫و‬
                                                                    ‫را ازسبماب ساز وآن زهر‬                   ‫لوی‬ ‫عی ا‬
                                                                                                               ‫مست‬  ‫کان‬
                                                                                                                       ‫فاتل است‬


‫زمین‌شیار کرده را بدان هموارسازند ؛ وباین‌معنی‬                        ‫ر جر و ه بفتح اول وسکرن الی وجیم‬
‫؛‬     ‫است‬    ‫داز هم آمده‬           ‫بجای جیم خای نقطه‬                  ‫و رای بنقیطةٌ مضموم‌بواو زده ‪ ۰‬نام صمعی‌است‬
‫اول یز درست است ‪ -‬و در عربی صدا‬                         ‫وبکر‬       ‫که گاعی ورق طلا و لقره را بدان حل کنند‬
                                                                    ‫هردو خوالند؛ وبعضی‬  ‫وث‬  ‫ر و‬‫زورت‬     ‫وآ‬
                                                                                                     ‫الرا‬
                                                                                                  ‫نعنز‬
###### leaf 499
   ‫خر و‬                                                                    ‫زبیری‬
 ‫نزحیری د کنابه از دیوانه بادد ‪[| .‬وسخن سرابی وقصه‌خوابی‌باشد وکنابه‌ازسخنان‬
 ‫و لاطاتل‬     ‫بی لفم و بی معلی و هرزه و بیهوده‬                    ‫گ‬                                       ‫‪۰‬‬       ‫‪۰‬‬
   ‫‪۹‬‬                                                            ‫اندگان‬   ‫ر نج يان ‪ .‬کنابه از‬
 ‫گفتن و هرزه درایی کردن ‪ -‬و لاف زدن هم‬                                 ‫‪9‬‬               ‫بر‬
                                                                                             ‫باشد ‪.‬‬
                               ‫هت ؟ ‪.‬‬                                 ‫کر‬                   ‫‪۳‬‬
                                                 ‫و‬             ‫ن خای‬      ‫و ثالی و‬        ‫اول‬   ‫ر لح = بف‬
 ‫اول و سکون ثائی و دال‬            ‫» بفتح‬        ‫رلك‬              ‫‪.‬‬          ‫‪۳‬‬          ‫ِِ‬                ‫ِ‬
                                                               ‫قطه‌دار ‪ ۰‬معر ورف است وآنرا زیشدان‌هم کوبند‬
 ‫دعری‬      ‫أبجد » تامکتایی است که ابراهیم زردشت‬                                                               ‫‪1‬‬

 ‫شده است ‪۰‬‬
                      ‫ِ‬                     ‫‪۱‬‬
                ‫میکر د که از آسمان برای من ازل‬
                                                               ‫وبعربی‌ذفن خوانن‌د ‪٩‬‏ ‪ -‬و بمعنی‌مطلق سخن(‪)۱۱‬‬
  ‫‪:‬‬           ‫‪E‬‬           ‫‪ERE‬‏‬         ‫کوبند‬                       ‫ر‬
                                                                ‫هرزه‬     ‫آمده است عموما‪ .‬و سخنان بقیقحم‬
 ‫‪E‬‏‬        ‫ان‬         ‫رم‬     ‫بصعت‬                     ‫‪E‬‏‬       ‫ولاطابل ویپوده وخالی از معنی و لاف و کزاف‬
  ‫وند دونك اند اصزحف‬
                   ‫دوگ رگوبند زبنداز‬                                                              ‫‪۷‬‬   ‫انه خا‬
‫دو قسم از اقام آن ‪ - ۵‬ونام‬                  ‫عمن»ی‬
                                                ‫یاهی‬
                                                   ‫ابر‬                               ‫رت‬               ‫‏‪EE‬‬
       ‫‪۱‬‬          ‫‪۱‬‬              ‫‪9‬‬      ‫‪1‬‬             ‫‪۱‬‬        ‫ر نخ بر حون ردن = کابه از‬
‫هرراب بن رستمبود‬
               ‫پپلوالی بوده‌تورالی که وسزی‬                         ‫‪۹‬‬
‫خجل‌شدنوخجالت کشیدن وشرمند کیباشد ‪ | ۰‬ورستم او را ييك مشت کشت و او را زندههم‬

                                                                             ‫هم ‪.‬‬         ‫)‪ (۱‬چش ‪++‬‬

      ‫حندی باستان ‪( 1102 -‬زنخ) ‏ اوستا ‪" 2۷082 -‬ارمنی ‪( 608۳6‬فك‪ ,‬کونه)‪.‬‬                               ‫‪۱‬‬
  ‫افنانی ع ‪anaZ‬‏ ‪ « 618122‬بلوچی ‪ 6082 , 10022‬و‪( 8082‬ع) » وخی ‪( 80722‬ع)»‬
           ‫‪ ۴‬رك ‪ :‬رخ زدن ‪.‬‬      ‫‪. 4۹۹1‬‬  ‫تق‬‫اس «‬   ‫شفنی ‪ » 080012‬سریکلی ‪00‬‬
                                                           ‫‪ -‬چون رنگ خخجلت زده سرخ گردد ‪:‬‬             ‫‪۴‬‬

              ‫زنخ برخون زد اراج بعداد ‪.‬‬                               ‫تراج غبغبم را کر کنی باد‬
      ‫نظامی کنجوی‪ «.‬کنجینه ‪. ۰۸۰‬‬
                                                                      ‫‪ - ۴‬و بمعنی طمنه وتسخر ‪:‬‬
                      ‫‪.‬‬    ‫شد‬
                            ‫بخازدن‬
                                 ‫ریشخند و زا‬                          ‫آینجنن بخشش وصله لنود‬
      ‫کمال اسمعیل «گنجینه ‪*A.‬‏‬

      ‫‪4‬دراوستا ‪( 126022‬شناساندن»‬
                               ‫‪ - ۵‬زند در پهلوی ‪( 04۳82‬شرح ‪+‬تقسیر)«اونوالا ‪./44‬‬
      ‫معرفت) «بارتولمه ‪ .۹۹۱‬کلم اخیر از مصدر ‪ 022‬اوستابی (‪ 0121‬پارسی‌باستان) بمعنی‌داد‪-‬تن‬
      ‫ور تفر بهلوی بهازدن»‬
                         ‫وشناختن است که یا پیشود ‪ 2‬در اوستابی صورت ‪ 11022‬در آمده د‬
      ‫گردانیده شده ( پور داود ‪ .‬زلدیق ‪ ,‬سالنامةٌ دنا ‪ ۷۲۳۱‬ص ‪ )۸۱۱‬بابددالست که در ازمنة‌سیار‬

      ‫کهن تفیری برای اوستا بزبان اوستایی نوشته بودلد و ده‌ونه‌ای ازین تفیر درخوداوسنای کمولی‬
      ‫بافیمانده و بامتن مخلوط شده است ‪ .‬بعد هسااین تفیر را از زبان اوستابی بزبان پپلوی ترجمه‬
  ‫(اهراً بلاش‌اول اشکالی ‪). ۸۷ - ۱۵‬‬  ‫کردند ‪ .‬طبق سنت پس از تدوین اوستا در زمان ولخش ظ‬
   ‫تفر اوستا بعنی زلد » بزبان پپلوی شروع شد و ندوین این تفیرتا اواخر عهد ساسانیمخصوصاً‬
  ‫کوشید ( چه نام مزدك بامدادان دربند ‪٩4‬‏ از‬  ‫لط‬
                                              ‫تا زمان مزدگ مماصر فباد ( ‪۱۳۵ - ۰44‬م‪) .‬‬
      ‫فصل ‪ 4‬ولدندادآمده ) ‪ .‬زلد با تفیری که امروژه در دست داریم »ت>فسیرست اآزعهد ساسایان‪.‬‬
      ‫روبهم رفته از تفیر پهلوی اوستایمنی اززند ‪ ۰۰۰۱۶۱‬کلمه یما رسیده ‪ .‬در بار مفهوم و استعمال‬
  ‫کلمةٌ «زند» ازقدیم تاکنون دوبسند گان‌شرق وغرب‌دچار اشتباه شدء‌اند از جمله قولمژلف برهالست‬
```


## [2026-09-06T14:56:11.436Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T14:56:11.443Z] TOOL RESULT

```


```


## [2026-09-06T14:56:12.968Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN woman ===\"; grep -n \"2\\.22\\|WOMAN\" SYN.txt | head -20",
 "description": "Grep Buck synonyms for woman"
}
```


### [2026-09-06T14:56:13.024Z] TOOL RESULT

```
=== SYN woman ===
1622:etc., fr. IE *gel- in words denoting spherical shape, whence ‘protuberance’, then ‘cliff’, ‘tock’. Walde-P. 1.614. Miihl.-Endz. 2.229.
1939:Lett. makuona ‘cloud’ makna ‘swamp’, Lith. miklus ‘damp’, ChSI. mokri ‘wet’, Russ. moknut’ ‘get wet’, etc. ; with common notion of ‘moisture’, Walde-P. 2.224. Miihl-Endz. 2.580.
2304:NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE woman Pol. kobieta Tr. ben, fracc Du. vroww Russ. ZenSéina Nir. bean OHG  wib, quena Skt.  jani-, nari-, stri- W. gwraig, benyw, dynes MHG wip Av. Jant-, ndtri-, strz- Br. maouez NHG frau, weib
2341:The majority are obvious derivatives or compounds of the words for ‘man’ or ‘woman’ (2.21, 2.22) and need no further discussion.
2359:5. Skt. (beside adj. vrsan-) prefixed pums- or nara- (2.21) for ‘male’ human beings or animals. Similarly strz- (2.22) prefixed or added for ‘female’ human beings or animals.
2445:ah ith a common notion married! oO z ae perh. fr. the same f ‘young person. ’ ; ony ‘can’, mahts ‘strength, tas Goth. mag ’ me nt’, NE might, etc. Walde-P. 2.228. Falk Torp 748. Feist 339. nee
2571:3. mama, amma, etc. Walde-P. 1.53, 2.221. For ‘mother’, Grk. nauun (also ‘srandmother’), Lat. mamma _ (also ‘grandmother’ and ‘nurse’), It. mamma, Fr. mama, NE mamma, etc., familiar in nearly all the European languages, in some as reg. word for ‘mother’. Cf. also Lett. mdsa ‘sister’, Lith. mosa ‘hus- band’s sister’, OHG muoma ‘aunt’, later ‘niece’ or ‘cousin’ (NHG muhme).
2634:1. From words for ‘man’ and ‘wom- an’, which have already been discussed in 2.21, 2.22, Probably in every IE language the words for ‘man” and ‘wom- an’ may be used for ‘husband’ and ‘wife’, at least in colloquial or vulgar speech, as is true even in NE my man, my woman. Here are listed only those that are the usual terms. (So NG yuvaixa for ‘wife’ is not vulgar, like NE woman in this sense, but is used in the best circles, where cifvyos would be felt as super- refined, almost like NE spouse; Dan. kone is now in the best usage, more usu- al than hustru; NHG weib for ‘wife’, vul- gar in the north, is usual in southern Germany). While many of these retain also their earlier use, as Grk. dvp, yuri, Lat. vir, Fr. femme, NHG mann, ChSI. mgzt, Zena, etc., others have come to be used prevailingly or exclusively for ‘hus- band’, ‘wife’, as ON verr ‘husband’, Goth. géns ‘wife’, NE wife, Br. gwreg ‘wife’, Lith. Zmona, Pol. zona ‘wife’, Russ. muz, Zena ‘husband, wife’. All such relations are shown by a compari- son of the lists 2.21, 2.22 and 2.31, 2.32.
2637:than pats ‘husband’, which is mostly obs.), Toch. A pats ‘husband’ : Lat. potis ‘able’, Goth. brupfabs ‘bridegroom’, Hitt. -pat ‘self’. Walde-P. 2.77f. For similar development of ‘master, mis- tress’ (of the house) to ‘husband, wife’, ef. Dan., Sw. hustru ‘wife’ (below, 6), and NHG frau (2.22).
2816:starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
2817:2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
3107:2. Lat. matertera, OE médrige, OHG muotera ‘mother’s sister’, W. modryb, Br. moereb ‘aunt’ (Pedersen 1.48, 2.33), formed with various suffixes fr. the words for ‘mother’. Walde-P. 2.229.
3560:7. ChSI. nevésta ‘bride’ (see 2.22 under Pol. niewiasta), used also for vindn as ‘daughter-in-law’ (Mt. 10.35). So Russ. nevestka beside nevesta ‘bride’.
4163:3. Ir. laeg, léeg, NIr. laogh, W. llo, Br. leue, prob. fr. *lapego- : Alb. lopé ‘cow. Pedersen 2.22. Loth, RC 44,267 ff.
6196:daxxbdws), but etym. dub. Perh. orig. ‘tip’ (whence ‘finger’ and ‘toe’) : ON tindr ‘point, mountain peak’, OF tind, OHG zinna ‘prong’, etc., though for these there are other possible connec- tions. Walde-P. 1.120 ff. Boisacq 164. 2. Lat. digitus (>the Romance words), prob. fr. IE *deig- in Goth. taikns ‘sign’, etc., beside deik- in Grk. delxviupt, Skt. dicg- ‘point out’, Lat. dicere ‘say’ (fr. ‘point out’), zndex ‘index finger’, prob. also OF ¢a@ ‘toe’, etc. (as orig. ‘finger’). Walde-P. 1.776f. Er- nout-M. 268, 271. Walde-H. 1.351. 3. Ir. mér, NIr. méar, etym. dub. Walde-P. 2.221, 223. Pedersen 1.134. W. bys, Br. biz, possibly : ON kvisir ‘twig’. Walde-P. 1.694. Pedersen 1.79. 4. Goth. figgrs, OF finger, etc., gen- eral Gmce., perh. fr. *penkrés : Ir. cotcer ‘number of five’, fr. I *penkve ‘five’. Walde-P. 2.26. Falk-Torp 218. Feist 150.
6220:TS 0 a ullicaris (> sbs. Sp. pulgar, : log. policar) prob. (formed on mm, ne" index ‘forefinger’) : Lat. E re strong’, Skt. phala- ‘fruit, pollere *. 1) with a common notion ee ‘ll kening’; here prob. also prev a etc. ‘thumb’ (below, 6). Us s 2 102. Ernout-M. 785 f. es “ore, NIr. ordég, Gael. ordag, sie ord ‘hammer’ (9.49). Macbain ee bawd (also bodfys, epd. wiih bye ), OW maut, a meud, fr. font . Arm. matu ‘finger’, root con- ie Walde-P. 2.221. Henry 200 f. 4,ON *pumi, pumalfingr, Dan. (lomme formerly ‘thumb’, now only finch’) tommelfinger, Sw. (tum ‘inch’) tumme, OE puma, ME thoum(b)e, etc., NE thumb, Du. duim, OHG dumo,
6559:‘purse’, W. megin ‘bellows’. Walde-P. 2.225.
7618:n : as ON maltugr, OE “7. etc. general Gme. th. maht _MLG) fr. sb. Go ; 0 is fr, vb. Goth. magan, at mist ie) (9.95). Walde-P. 2.227. te. rk, Sw. stark (OE violent’, steare
7645:Boh. mocny, Pol. mocny, Russ. most- nyj, fr. sbs. for ‘might’, Boh. moc, etc. = ChSI. mogti, fr. vbs. for ‘be able’ ChSI. mosti, mogq, ete. : Goth. magan ‘be able’, etc. (above, 4). Walde-P. 2.227.
8035:4, ON méddr, OE méfe, OS modz, Du. moede, OHG muodi, MHG muede, NHG miide : Goth. af-mauipfs (only nom. pl. afmauidat ‘éxdvopevor, wearied’, pple. of *afmodjan), OHG muojan, muoan ‘dis- turb, torment’, Russ. majat’ ‘fatigue, harass’, prob. Grk. u&)os ‘toil, moil’, Lat. moles ‘large mass’, molestus ‘trouble- some’. Walde-P. 2.302. Feist 9. Wei- gand-H. 2.225, 227.
```


## [2026-09-06T14:56:21.635Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{leaf=1} {if(NR==2304){print \"line 2304 is on leaf\", leaf; exit}} /\\f/{n=gsub(/\\f/,\"\\f\"); leaf+=n}' SYN.txt; echo ---; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:2303])\nleaf=t[:pos].count('\\f')+1\nprint('leaf',leaf,'printed',leaf-24)\nEOF",
 "description": "Locate Buck 2.22 leaf/page"
}
```


### [2026-09-06T14:56:23.381Z] TOOL RESULT

```
line 2304 is on leaf 112
---
leaf 112 printed 88
```


## [2026-09-06T14:56:28.826Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 105 106 107 111 112; do echo \"##### leaf $n (printed $((n-24)))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -12; done",
 "description": "Inspect Buck leaves around printed 82"
}
```


### [2026-09-06T14:56:30.538Z] TOOL RESULT

```
##### leaf 105 (printed 81)
. ZeSti, #ega, SCr. deci (Boh. Zeci, Pol. gec for- merly the usual words for ‘burn’, now mostly ‘scorch, singe’), Russ. ge¢’; NIr. doigim (denom., ef. MIr. daig ‘fire’, NIr. doigh ‘pain’); Alb. djégé ‘burn’; Toch. tsdk- ‘burn’; cf. Lat. fovére ‘warm’.
2. IH *eus-. Walde-P. 1.111. Er nout-M. 1137 £, eee us-, Lat. arere ‘burn’, Grk. ew
3. Grk, Kalw, A
tt. xéw, fr, *xé i : zy aor. Hom. gna (# ’ aF-Lw,
Peay exnfa), Att. 2
ia Gr nt ee,
Withers with numerous derivatives.
Walde-p a clear outside connections.
Te 76. Kato &, Kaiouar b (or mer also ‘light for themselves’).
kal 4 + a,b (ch xale ‘it burns’), dis-
tinguished in aor. éaya (éavoa) a, éxanka b.
Grk. civrpnue : rpnfw ‘blow up, in- flate’, Russ. pret’ ‘stew, sweat’, ChSI. para ‘steam, vapor’, ete. Walde-P. 2.27. Prob. first intrans. ‘burn’ from the no- tion of ‘spurting out’.
##### leaf 106 (printed 82)
hre-n-wo-, may be combined with *bher-, *bhreu- in words used for the gushing and seething of liquids, as Lat. fervére ‘boil’, Goth. brunna ‘spring’, etc, Walde-P. 2.168. Feist 106. Falk. Torp 111.
7. Lith. degti, ChSI. Zest, etc., above, 1.
ChSl. goréti, etc., general Slavic for ‘burn’ b, : Skt. gharma- ‘heat’, Grk. Gepuds ‘hot’, etc. (15.85), Ir. vb. gorim ‘heat, warm’. Walde-P. 1.688. Berne- ker 333 f.
Boh. spaliti, Pol. palié (now the usual words for ‘burn’ a and used with reflexive for ‘burn’ b) = ChS&l. palzti (also poléti) ‘blaze, burn’ (e.g. Supr. = ¢déyoua), SCr. paliti ‘set on fire, burn’ a, Russ. palit’ ‘blaze, burn, singe’, all with pri- mary notion of ‘blaze’ fr. *pel- in ChSI. plamy ‘flame’, etc. (1.82). Walde-P. 2.59 f. Miklosich 235. Briickner 392.
1.86 LIGHT (vb.), KINDLE
Grk.  (4v)arrw (Sale, atdw) Goth. tandjan Lith. uédegti
NG Gvadrw, dvapw ON tendra, kynda Lett.  atz- (or te-)dedzinat
Lat.  incendere (also ac-, Dan. (an)tende ChSl.  vtiZeSti $uc-) Sw. (upp)ténda SCr. zapaliti
It. accendere OE on@lan, (on)tendan Boh. zapdliti
Fy. allumer ME Iihte, kindle Pol. —_zapalié
Sp. encender NE light, kindle Russ. zazeé!
Rum. aprinde, tncinge Du. _—aansteken Skt. idh-
##### leaf 107 (printed 83)
, outside root connection wholly dub. Feist 474. Falk-Torp 1311. NED s.v. tind, vb.
ON kynda, whence ME, NE kindle, etym.? Falk-Torp 610. NED sv. kindle, vb.
ME lihte, NE light (much more com-
_ Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS
UE
mon than kindle even with fire, and only light, not kindle, with candle, lamp, pipe, etc.), orig. ‘give light’. NED s.v. light, vb.?2.
Du. aansteken, cpd. of steken ‘thrust.’ So locally NHG anstecken, Kretschmer, Wortgeogr. 79f.
5. Lith. uzdegti, Lett. azz- (or ie-)degt, more commonly dedzenat, cpds. of Lith. degti, Lett. degt ‘burn’ (1.85).
6. ChSI. viizesti, Russ. zazeé’, epds. of ChSI.. Zegtz, Russ. Zee’ ‘burn’ (1.85).
Ser. zapaliti, Boh. zapdliti, Pol. za- palié, epds. of ChSI. paliti ‘blaze, burn’, etc. (1.85).
Boh. rozsvititi (‘light’ a candle, etc.), epd. of svititd ‘make light, light the way’ : ChSI. svéti ‘light’, etc. (1.61).
##### leaf 111 (printed 87)
�die’ in Skt. mr-, Lat. morz, etc. Walde- P, 2.276. Barth. 1148 ff.
2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
Many of the words for ‘man’, namely most of the Romance and Germanic and all the Slavic, were originally words for ‘man’!, or derivatives of these and have been included in the discussion 2.1.
Many of the words for ‘man’? were also used for ‘husband’, and some of them are quotable only in the latter sense, so that they do not appear in this list (so ON verr).
1. TE *wiro-, that is, *wt-ro- : Lat. vis, Skt. vayas, ete. ‘strength’. Walde- ot ff. Ernout-M. 1112 f.
at. vir, Umbr. uiro (ace. pl.): Ir. Jer, Nir. fear, W. gur, Nie nas Ge ae with neg. for ‘no one’); Goth. wair Gat Chee OE wer, ete. (old : ) Dut now obs. except in epds.,
as NE Werewolf, N. ? Weitere ae HG wergeld; also NE
» Ay, vira-,
2. TE *ner-, nert ‘strength, tion of ‘stren
Lith. vyras, Lett. virs;
Various cognates, as Ir. might’, show that the no- gth’ is dominant, as in IE
*wiro-, but the ultimate root connection is uncertain. Walde-P. 2.332f. Er- nout-M. 667 f.
##### leaf 112 (printed 88)
 burg 1.254 f. (best account of the com- plicated history). REW 962. Gamill- scheg 83. NED s.v. baron.
Rum. bdrbat, fr. Lat. barbatus ‘beard- ed’ through Byz. BapBaros used for one who was not aeunuch. Cf. NG BapBaros used of an animal that is not castrated, as adoyo BapBaro ‘stallion’.
4. Br. gwaz, fr. OBr. guas, MBr. goas
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
82 SELECTED INDO-EUROPEAN SYNONYMS
‘servant’ = W. gwas, Ir. foss ‘servant’, etc. (19.438).
5. ON karl and karlmadr, OF ceorl, OHG karl, all meaning ‘man’, esp. the ‘man without rank, freeman’, in the earlier period a term of esteem (as in the proper name Karl), later one of dis- paragement or contempt, asin NE churl,
OE wep(en)-man, wepned-man ‘man, male’, cpds. of w&pen ‘weapon, penis’ (4.492), wepned ‘male’.
OHG gomman, cpd. of gomo (2.1) and man.
6. Skt., Av. vtra-, nar-, above 1, 2. Skt. pumazis-, pums- ‘man, male’ (ys,
NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE woman Pol. kobieta Tr. ben, fracc Du. vroww Russ. ZenSéina Nir. bean OHG  wib, quena Skt.  jani-, nari-, stri- W. gwraig, benyw, dynes MHG wip Av. Jant-, ndtri-, strz- Br. maouez NHG frau, weib
```


## [2026-09-06T14:56:38.187Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==113' SYN.txt | head -30",
 "description": "Buck 2.22 commentary"
}
```


### [2026-09-06T14:56:40.081Z] TOOL RESULT

```
�), gen. yuvatkds, NG yuvatca (yurt lit.); Ir. ben, NIr. bean, W. benyw; Goth. gind (and géns ‘wife’); ON kona (gen. pl. kvinna); Dan. kvinde (and kone ‘wife’), Sw. kvinna, OE cwene (and cwén ‘wife’), OHG quena; OPruss. genna, ChSl. Zena, etc.; Skt. jani-, jani-, -jani-, Av. jani- (NPers. zan), gana-, etc.; Arm. kin; Toch. $dm.
2. Lat. mulier (>It. moglie ‘wife’, OFr. moillier ‘wife’, Sp. mujer ‘woman,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
— Digitized by Arya Samaj Foundation Chennai and eGangotri
| ! | | )
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 83
Rum. muzere formerly ‘woman, derogatory), etym. Sere ee
: vith a comp. suffix from SY i Lat mollis ‘soft, delicate’, ia so used of the weaker sex, Or gas the same root in an obscene sense! Walde-P. 2.285. Ernout-M. 637 f.
‘Lat. fémina ‘a female’ in general and ‘woman’ (> It. femmina formerly ‘wom- an’, now only ‘female’, Fr. femme ‘yoman, wife’, Sp. hembra ‘female’), orig. mid. pple. fr. the root of Lat. félare ‘suck’, Grk. @fc8a. ‘suck’, @fdus ‘female’, Skt. dhayatz ‘sucks’, etc., (5.16), hence ‘one who gives suck’. Walde-P. 1.829 ff. Ernout-M. 341, 343.
It. donna, now ‘woman’, formerly ‘mistress, lady’, like Fr. dame, etc., fr. Lat. domina ‘mistress’.
Rum. femete ‘woman, wife’, dial. ‘children, family’, fr. Lat. familia ‘house- hold’. REW 3180. Puscariu 595.
3. Ir. frace ‘woman’, W. gwrach ‘old woman, witch’, gwraig ‘woman, wife’, Br. gwreg ‘wife’, prob. fem. derivs. of Ir. Jer, W. gwr, etc. ‘man’? (Pedersen, 1.159 dub.). Cf. Lat. viragd ‘manlike female’, virgo ‘maiden’, fr. vir, W. dynes ‘woman’ (cf. Morris Jones 223) fr. dyn ‘man”, and Skt. nar7- ‘woman’ fr. nar- ‘man”,
Br. maouez : Corn. mowes ‘girl’, Goth. mawt ‘girl’, fem. of Ir. magu ‘servant’, Goth. magus ‘boy’, ete. (2.25-26). Walde-P. 2.298, Pedersen 1.98.
wife’, wife’, DOW
nally displacing wife mm ais Wider sense (except dial. or in cpds.), OHG wib, MHG wip, NHG » Now mostly €rogatory and re-
placed by frau, as likewise Du. wijf by vrouw. Etym. much discussed and whol- ly dub. Falk-Torp 1390. Weigand-H. 2.1224. Paul, Deutsches Wtb. s.v. Weib (on its use).
NHG frau, Du. vrouw, orig. ‘mistress’ as OHG frouwa, fem. of OHG fré, Goth. frauja ‘master’ : Skt. pirva- ‘in front, former’, Grk. rpdros ‘first’, etc. Walde- P. 2.37. Falk-Torp 278.
NHG frauenzimmer, orig. a room for the women at court, then coll. for ‘wom- en’, finally ‘a woman, female’, now most- ly with derogatory feeling. Weigand-H. 1.577.
5. Lith. moté, gen. moters (now usual- ly moteris or moterigké), orig. ‘mother’ = Lett. mate, ChSl. mati, Lat. mater, etc. (2.42).
Lith. Zmona (but now mostly ‘wife’), fem. of Zmogus ‘man’ (2.1).
Lett. steva ‘wife’ (2.32), also ‘woman’.
6. Pol. niewiasta, formerly the com- mon word for ‘woman’ (zona being ‘wife’), orig. ‘bride’: ChSl. nevésta ‘bride’, this a cpd. of neg. prefix ne and fem. of véstii ‘known’, hence the ‘un- known’, that is, the newcomer in the husband’s family. Zubat¥, Arch. sl. Ph. 16.406. Briickner 362.
Pol. kobieta, first appearing as a derogatory epithet and plausibly ex- plained as a blend of kobyla ‘mare’ (this also epithet of a ‘clumsy, stupid woman’, as is also Russ. kobyla) with names like Bieta
```


## [2026-09-06T14:56:50.539Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC gwena ===\"; grep -n \"gʷenā\\|gwena\\|gu̯enā\\|gʷēn\" IEC.txt | head -10; echo \"=== IEC gweru ===\"; grep -n \"gʷerəus\\|gʷrəu\\|gweru\" IEC.txt | head -10; echo \"=== IEC alt ===\"; grep -n \"^g[”\\\"']en\" IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-06T14:56:50.609Z] TOOL RESULT

```
=== IEC gwena ===
20007:uenos, -es- ‘desire’. Cf. uén- (1) and WP I, 259 Skt. vanas, n. ‘loveliness’ beside vanā & vanih, f. id.; vanús, adj. ‘keen; loving’; Lat. Venus, gs: -eris, f. ‘Venus’; beside vinulus & vinnulus, adj. ‘dainty; wanton’; W gwên, pl. gwenau, f. “smile”, cf. Gweno, f. “evening star, Venus’; (z-gde in) OHG wunja, MHG wunne, wünne, f. (2) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
=== IEC gweru ===
=== IEC alt ===
```


## [2026-09-06T14:56:51.713Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"681\\|684\" WLD_Bd1_pages.txt | head -5; echo \"=== search gena ===\"; grep -n \"gena-.*Weib\\|Weib.*gena\" WLD_Bd1_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-06T14:56:51.775Z] TOOL RESULT

```
52632:                      '.       Ygl. Muhlenbach-Endzelin 1 611, 684, 686: Trautmann Bsl. Wb. So.
57928:Bthl. Wb. 1684);                           zarstva- n.„Stein“ (Fick I 4 435; vgl. bes. mars, sabin.
64487:                                                                      g“ena                                                        681
64882:ist    (s.    Brugmann IF. 33, 302 m. Lit., Miihlenbach-Endzelin I 684;                                                        Gdf.
72984:av. dit „es",          dis pi. m. f., (Bartliolomae 684) und apr. Akk. sg.
=== search gena ===
```


## [2026-09-06T14:56:54.287Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '64480,64530p' WLD_Bd1_pages.txt",
 "description": "Print Walde-Pokorny I 681 gwena"
}
```


### [2026-09-06T14:56:54.343Z] TOOL RESULT

```
 naldi-qone ,(Nachthut ££ naldi-gonis „Nachtschwarmer“
                                                ,                                                             ;
                                                                                                                lit. genf/s ,,Spechr
                                                                                                                                                   -
                                                                                                                                                           gin-
                                                                                                                                                       ,
                                                                      g“ena                                                        681

cid     (= ai. hatyd),                          gincas „Streit", ginklas ,,Waffe“ isganiis „heilbringend ££
(lit.   gdmioti             ist       Iterativum zu ginti, s. Berneker 294, 328);                          lett.   (vgl. B. bei
Fick II          4
                     110 undoben ir. geind) dzenis „das zwischen den beiden Zacken der
Gabel der Pflugscbar eingeklemmte Holz", dzenulis „Stachel“                                                              (vgl.     zur
Bed. u. aksl. zglo „Stachel“).
  Aksl. zenq gvnati „treiben“ (wie lit. genu), Iter, gonjq, goniti „treiben,
                            ,


jagen", wovon wieder pogcinjati „verfolgen“; russ. usw. gon „Treiben, Jagd“
(= gpovog), cech. uhonci „Verletzung, Schaden", serb. prijegon „Kampf“
(dazu vielleicbt klr. honoba „Belastigung, Plage", sloven, gonoba „Schaden,
Verderben", ugonoba „Yernichtung, Untergang" v. d. Osten-Sacken IF. 26,
322 Anm. 1 eine andere Auffassung u. *gen~, *genebh- „zusammendrfieken“)
                        ;


   aksl. zbnjq ,                     zqti       (serb. ziti,       also   set-Basis) „ernten“, zctva (serb. zetva)
„Ernte“ (: ai. hantva-); aucb zclo „Stachel“, poln. zqdlo ds., russ. zalo „Stacbel,
Schneide eines Messers, einer Axt" (Liden aaO.; nicht besser zu cymr.
banadl, acorn, banuthel, mbret. balazn „Ginster“, B. bei Fick II 4 161, was
Media gV, voraussetzen wiirde); unter Annahme urslavischer Entnasalierung
reiht Jokl AfslPh. 28, 3; 29, 16f., IF. 27, 308 nicbt fiberzeugend aucb cech.
hasdk .Sense" (: zcti), poln. gas „das Hauen, Schlagen, Untergang ££ russ.
             ,                                                                                                             ,


gasdtb „ein Pferd tummeln" usw. an.
    Vgl. J. Schmidt KZ. 25, 168f., Fick I 4 39 f., 203 f., 415, III 4 124.


gjena „\Veib, Frau g‘i enu g'Lna-, im Germ, und Arm. auch en-St. *g’ten-en-;
                                                ££
                                                     ,         ,

    im Gr. ein Stamm auf -aik, im Arm. ein St. auf ai (aus -aikl), unklar,
    ob in Beziehung zum Typus lat. gcnetr-J-c - auberdem ar. *g ieni- und,                    ;
                                                                                                                     l
```


## [2026-09-06T14:56:59.156Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '64530,64580p' WLD_Bd1_pages.txt; echo \"===== 684 gwer =====\"; grep -n \"g\\\"er\\|g‘‘er\\|gerU\\|„schwer\" WLD_Bd1_pages.txt | sed -n '1,25p'",
 "description": "Continue WLD gwena and find gwer"
}
```


### [2026-09-06T14:56:59.234Z] TOOL RESULT

```
        wie auch germ., *g ieni- (-i in Ablaut zu arm. gr. ail).
                                                           ,
                                                                                                                   S. fiber         das
                  und die Staminbildung Brugmann IF. 22, 171
        flexivische                                                                                           — 193 m.             Lit..
        Kretschmer Gl. I 375.
  Ai. gana i* gH e na ) und gna (*g"na) „Gotterweib", av. j.ma, yna „Frau,
Weib"; ai. jani-h = av. jani-, np. zan „Weib“ (ai. auch .jam), in Zs. ai.
-jani- ( dvi-jani „zwei Weiber besitzend") = av. jqni- .AVeib";
   arm. kin (g"ena) „Gattin“ (Hfibschmann Arm. Gr. I 460), pi. kanai-ft (ft
Pluralsuffix; kainai- aus g'X en-aikl ), in einigen Ivasus St. kanan- (wie im
Ivollektiv kanani                           ,   .Frauen")
    gr.        „Frau" aus *g u una neben *g i enu in boot. (Java, und *g'ina-,
             yvvi                                                                  l




*flvd   in  /Livdo/aai „freie“ (Osthoff KZ. 26, 326; dazu /uvtjcmjg „Freier“,
juvrjoT Vs „Werbung“, pygari] dkoyog „rechtmiibige Gattin", mit -a- nach den
primaren Yerben, Solmsen KZ. 29, 102, Brugmann -Thumb GrGr. 4 328,
Kasus obliqui yvvaixog usw., boot, yflavqy.ag yvvatxag Hes.
       ben (*g]iena), gen. mna (*gjjia-s), g. pi. ban(*g u en-om), in Zs. ban-
      air.
(ban-chu „weiblicher Hund") ,,Frau" (aber cymr. bun ds. bleibt fern trotz
Pedersen KG. I 384                               1
                                                     ,
                                                         cymr. ben-yw „weiblich“             (s.   auch Pedersen KG. I 47),
 corn, ben-ni „sponsa“;
  got. qinii (* guenon -) = ags. cwene, ahd. quuia, mhd. queue und kone „Frau,
Ehefrau", anord. kona (g. pi. kvenna ) „Frau" aus *g%nun--, got. <-St. gens
(— av. jani-, ai. -jani an. kveen , kvan. ags. cicen, as. quan                                                ;


  apr. genna , geuno ,Frau“, aksl. zena ,Frau"; zenim „weiblich"           got.                                                =
qincius              ds.,       z.    B. Curtius 5 175.              Fick     I4       34,   196, 401.    — Uber alb. zone
„Herrin, Frau                    ££
                                      s.    Pedersen KZ. 36, 324.                  Derselbe erklart KZ. 39, 419 arm.
kanailc aus einem alten Kollektiv leeway- = *kanati      doch                                                                  ist   der obige
Vergleich des -ai- mit gr. yvvaix- wohl nicht triigerisch.

1. g“er- „Berg‘‘ (g lt ora, g%ri-).

     Ai. girl-lb m. „Berg“, av. ga i ri- ds., aksl. gom „Berg“,                                                     lit.   nugara .(Riickcn
(eines  Menschen oder Tieres, aber auch eines Berges)“, alb. gur „Stein“
(Pedersen KZ. 36,319, Gdf. g~ e ri~; dazu aucb gr. dsigdg (Hes.) „Hiigel‘%
                                                                ;i
bipidttgos „mit hohen Bergen     detoa  kret. dygas „Hugel, Anliohe*' (Ehr-
                                                                        ,

===== 684 gwer =====
8612:„schwer“), vielleicht auch in                 ol/na      und andern unter              *eis- „sich heftig   be-
9218:ita- „schwer zuganglich“, prdtar-itvan- „fruh ausgehend oder -kommend",
17866:                                          unter *g*er- „schwer“;
24883:laut su-)                        lit.   sveriit , sverti „wagen“, svarits                       „schwer“, svdras „Wage, Pfund“,
24903:Stvtlr, sicCiri „schwer, driickend, lastig“, as. swar „schwer“, got. steers (iiber-
32404:anord. hqfugr, ags. hefig, as. hcblg, ahd. heb/c, -g „schwer“ (eigentlich „et-
33965:ds., alter   auch „nach Luft schnappen", schw. mdartl. hikja „schwer atmen",
35578:lit. kupuoti „schwer atmen", lett. kupet „rauchen, dampfen, stieben", kupi-
49880:       gr. %aio            „Hirtenstab“; gall. -lat. gaesum, gall.-gr. yaloov „schwerer eiserner
50519:gajgemin „schwer sprechend“, russ gugnati alt) „murmeln“, gagnja „Stot-
57029:    fr>n,.zermalmen“ (beide nicht wahrscheinlicher zu g«er- „schwer" durcli
64617:2.    g"er- ,,veischlingen, Schlund“.
64816:3. g'ler-      „schwer“       (n'-'^rv-s   Adj.; daneben die Wzformen giiera-                          :
64850:      Gr. fiagvg „schwer“, fiagvvm „besehwere", pagv&co „bin beschwert", ftagog
64852:fernzuhaltenden);                    lat.   gravis „schwer, gewichtig" (*g u ra-u-is; vgl. oben ai.
64866:got. Jcaurjos n. pi. f. „schwer", kaurjan „beschweren“; aus dem Balt, ver-
64887:      Lett, grids „schwer"                       =
64891:von g u erj- und g"ernn- (Bezzenberger BB. 16, 239, Fick I 4 411, Hirt Abl. 79
65240:g"er(e;bh-, gjrebh- „Leibesfrucbt, Kind, Junges".
68601:keit, Schwermut usw.; die Bed. „schwer“ (eig. ,was herunterzieht“), „trage“
68632:     aisl.   pungr „schwer“, punge m. „Biirde, Last", pyngia „beschweren u                    ,
68639:getretene   Gruppen, „ziehen“ und „schwer“, wobei dann fiir erstere die
71570:troim   „schwer“ als *trud-smos „*drfickend“ (Fick II 4 139, Pedersen
71571:KG. I 362; Zup. KZ. 36, 243 verglich es mit serb. trom „schwerfallig,
71574:„machtig", as. thrim „schwerer Kummer (?)“, ffir die aber eine Gdbed.
```


## [2026-09-06T14:57:02.423Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '64816,64860p' WLD_Bd1_pages.txt",
 "description": "Print WLD gwer- schwer"
}
```


### [2026-09-06T14:57:02.485Z] TOOL RESULT

```
3. g'ler-      „schwer“       (n'-'^rv-s   Adj.; daneben die Wzformen giiera-                          :
                                                                                                            u
                                                                                                           g ,(i')rd{u)-
        und    g’icri-).    An iilterer Lit. vgl. Fick BB. 2, 188, YaniiSek LEWb. 2 82,
        Curtius 5 475.
   Ai. gnrit-h                                (Komp. gdrlyan Sup. garistha-h
                        .,schwer, wichtig, ehrwiirdig"                                     ,                           ;


Persson Beitr. 775     vermutet urspriingliehe Zugehorigkeit dieser Formen
zur /-Basis ^y'lrri-, so dal.i sie zu den Musterformen fiir die Komparativ-
bildung auf ai. -i-yas-, gr. 7-ms zu rechnen waren; unsicher), gru-mustl- It
..schwere Handvoll", gnr'md m. Schwere“ (kaum von
                                               ,;
                                                                 sondern von
*yZera-, vgl. Iat. gravis aus *g"r9-ui-)\ av. gouru-zaodra- „des AYeihegiisse
schwer, ziihfliissig sind*'; np. giran ,.schwer“ *yrann   kein Beleg fiir die
                                                                       (_



Hochstufe *<f‘(p)r<i x zu *y"(e)r.>-, sondern Umbildung etwa nach *frann-
,,voll‘*).

  Gegen Auffassung von ai. agrn- „unverheiratetes Miidchen' (daraus se-
kundiir agru-h m. „unvermahlter Mann'*), av. ayru- ,,jungfraulich“ als „nicht
schwanger    (: ai. f. gitrrf ..schwanger",
                1
                    '                       das aber erst nachvedisch) be-
achtenswert             Sommer    IF. 36.     197.    — Ai. garva-h ..Hochmut" liierher als
„gravitutisches AVesen, Wichtigtuerei"? (z. B. Persson aaO.: an yavgos wird
man freilich kaum denken diirfen).
                                                                 gijer-                                                         68 5

      Gr. fiagvg „schwer“, fiagvvm „besehwere", pagv&co „bin beschwert", ftagog
„Schwere" (auch ipgvo&g                         ejieoev Hes. ? Pick KZ. 42, 288 mit anderem sicker
fernzuhaltenden);                    lat.   gravis „schwer, gewichtig" (*g u ra-u-is; vgl. oben ai.
gari-man-, und bes. das Yerhaltnis ai. prthu-h prthivf) 1 ); mir. hair „sch\ver“(?),
                                                                                 :



baire     „Kummer (?)                ;(
                        (Stokes Rc. 27, 85; ?), bruth ,,Gewicht, Masse ' (Stokes
IF. 12, 186), cymr. bri/w „stark, Starke" (Ficlc II 4 186, Pedersen KG.
```


## [2026-09-06T14:57:15.185Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%E1%B8%97n",
 "prompt": "Give the reconstruction, meaning, declension notes, and the full list of descendants (especially Indo-Iranian: Sanskrit, Avestan; Greek; Germanic; Persian). Quote the Avestan and Persian forms exactly."
}
```


## [2026-09-06T14:57:16.285Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/kanya",
 "prompt": "What is the etymology of Sanskrit kanyā (कन्या) 'girl, maiden'? Which PIE root is it derived from? Is it related to *gʷen- 'woman'?"
}
```


### [2026-09-06T14:57:20.645Z] TOOL RESULT

```
I cannot answer your question based on the provided content. The webpage is a Wiktionary entry for "kanya" that covers definitions in Hanunoo and Tagalog languages, but it contains no information about Sanskrit etymology, Proto-Indo-European roots, or the word's relationship to the root *gʷen-.

To find this etymological information, you would need to consult a Sanskrit dictionary, etymological reference like the American Heritage Dictionary of Indo-European Roots, or specialized linguistic resources on Sanskrit word origins.
```


### [2026-09-06T14:57:21.894Z] TOOL RESULT

```
# Proto-Indo-European *gʷḗn (Woman)

**Reconstruction:** *gʷḗn (feminine or neuter; oblique stem *gʷnéh₂-)

**Meaning:** Woman

**Declension Notes:** Athematic, proterokinetic noun with ablaut between strong stem *gʷénh₂- (nominative) and weak stem *gʷnéh₂- (oblique cases).

**Major Descendants:**

- **Armenian:** Old Armenian *kin*, modern Armenian *kin*
- **Balto-Slavic:** *génāˀ
- **Celtic:** *benā
- **Germanic:** *kwenǭ (ancestor of English "queen," "quean")
- **Greek:** *gʷənā
- **Indo-Iranian:** *ǰánHs, *gnáHs (leading to Sanskrit and Avestan forms)
- **Tocharian:** *ćänā
- **Anatolian:** *gʷón- (Luwian *wanattis*)

**Note:** The page indicates this originally was neuter in PIE, still preserved uniquely in Old Irish *bé*. Specific Sanskrit and Avestan forms are not detailed on this Wiktionary entry; you would need to consult those individual language pages for exact quotations.
```


## [2026-09-06T14:57:26.139Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A4%BE",
 "prompt": "Sanskrit कन्या (kanyā): give the etymology section verbatim — which Proto-Indo-Iranian / PIE root, cognates, and any mention of *ken- 'fresh, young' or of *gʷen- 'woman'."
}
```


## [2026-09-06T14:57:27.618Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gynecology",
 "prompt": "Give the full etymology of gynecology, gyneco-, gyno-, including dates of coinage, the Greek source, and whether Latin or French is an intermediary."
}
```


### [2026-09-06T14:57:31.775Z] TOOL RESULT

```
# Sanskrit Etymology of कन्या (kanyā)

The word derives from **Proto-Indo-Iranian *kanyáH** ("maiden, virgin, unmarried girl"), which comes from **Proto-Indo-European *ken-** ("new, fresh").

## Key Cognates

The documented cognate languages include:

- **Avestan**: 𐬐𐬀𐬥𐬌𐬌𐬁 (kaniiā, "maiden")
- **Middle Persian**: knykʿ /kanīg/ (ancestor of Persian کنیز)
- **Latin**: re-cēns ("recent; fresh; young")
- **Ancient Greek**: καινός (kainós, "new")

The astrological sense represents a semantic loan from Ancient Greek Παρθένος (Parthénos), paralleling the Latin Virgō.
```


### [2026-09-06T14:57:33.276Z] TOOL RESULT

```
# Etymology of Gynecology

**Gynecology (1847):** The term originated from French *gynécologie*, combining the Latinized Greek form *gynaiko-* (from *gynē* meaning "woman, female") with French *-logie* (from Greek, meaning "study of"). The Greek root traces to the PIE root *\*gwen-* ("woman").

**Gyneco- (prefix):** This combining form derives from the same Greek source (*gynaiko-*), used to construct related medical terms.

**Gyno- (prefix):** Similarly, this prefix comes from the same Greek etymological base, functioning as a variant combining form.

**Key Details:**
- French served as the intermediary for the full term *gynecology*
- The Greek-to-Latin-to-French pathway was: *gynē* (Greek) → Latinized *gynaiko-* → French *gynécologie* → English *gynecology*
- Related terms emerged later: "gynecologist" (1851) and "gynecological" (1858)
```


## [2026-09-06T14:57:38.922Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/barium",
 "prompt": "Etymology of barium: who coined it, when, from what Greek word, and what about barometer (date, coiner, language of coinage)?"
}
```


## [2026-09-06T14:57:40.056Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/grief",
 "prompt": "Etymology of grief and grieve and grave (adj.) and gravity: give the Old French / Latin chain and dates."
}
```


### [2026-09-06T14:57:44.102Z] TOOL RESULT

```
# Etymology of Barium and Related Terms

**Who coined "barium" and when:**
"1808, coined in Modern Latin by its discoverer, English chemist Sir Humphry Davy"

**Greek origin:**
The name derives from the mineral barytes, which Lavoisier named from Greek *barys*, meaning "heavy." Interestingly, despite this heavy-sounding etymology, the actual metal is relatively light.

**About barometer:**
The provided content does not include a separate etymology entry for "barometer." However, it does note that "barometer" is one of several words linked to the same Proto-Indo-European root *gwere-* (meaning "heavy") that gives barium its name. The document lists barometer among related terms but doesn't provide its coinage date, original coiner, or language of origin.
```


### [2026-09-06T14:57:46.045Z] TOOL RESULT

```
# Etymology Chain: Grief, Grieve, Grave, and Gravity

**Grief (n.)** - early 13c.
- Old French: *grief* "wrong, grievance, injustice, misfortune, calamity" (13c.)
- Latin: *gravare* "make heavy; cause grief"

**Grieve (v.)** - c. 1300
- Old French: *grever* "afflict, burden, oppress"
- Latin: *gravare* "make heavy; cause grief"

**Grave (adj.)** - c. 1300
- Old French: *grevos*
- Latin: *gravis* "heavy, ponderous, burdensome, loaded; pregnant"

**Gravity (n.)**
- All derive from Latin *gravis* "heavy"
- Ultimate source: PIE root *gwere-* meaning "heavy"

The entire word family shares a consistent etymological path through Old French and Latin, unified by the core concept of "heaviness" or burden.
```


## [2026-09-06T14:57:51.440Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/barometer",
 "prompt": "Etymology of barometer: date, coiner, Greek elements."
}
```


## [2026-09-06T14:57:52.866Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D9%86",
 "prompt": "Persian گران (gerān): give the etymology section verbatim — Middle Persian form, Proto-Iranian, PIE reconstruction, Avestan cognate, and any cited authorities (Hasandust, MacKenzie)."
}
```


### [2026-09-06T14:57:56.029Z] TOOL RESULT

```
# Etymology of Barometer

**Date of Origin:** The term "barometer" emerged in the 1660s.

**Coiner:** English scientist Robert Boyle (1627-1691) probably coined the word and certainly popularized it, though the actual instrument was invented earlier.

**Greek Elements:** The word combines two components:
- **Baros** (Greek for "weight"), derived from a Proto-Indo-European root meaning "heavy"
- **-Meter** (Greek suffix meaning "device or instrument for measuring")

**Historical Context:** Italian physicist Evangelista Torricelli created the barometer in 1643. Initially called the "Torricelli tube," it was renamed when Boyle introduced the Greek-derived term "barometer" approximately two decades later to describe this "instrument for measuring the weight or pressure of the atmosphere."
```


### [2026-09-06T14:57:58.144Z] TOOL RESULT

```
# Etymology of Persian گران (gerān)

According to the Wiktionary entry, the etymology section states:

"From Middle Persian glʾn' (garān, 'heavy'), from Proto-Iranian *grā-na- ('heavy'), ultimately from Proto-Indo-European *gʷréh₂us ('heavy'). Cognate to Latin gravis ('heavy')."

The entry cites **Rastorgujeva, V. S. and Edelʹman, D. I. (2007)** in their *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages] (Moscow: Vostochnaya Literatura, volume 3, page 181) as the reference authority for this etymological information.

The webpage does not include references to Hasandust, MacKenzie, or Avestan cognates in the etymology section provided.
```


## [2026-09-06T14:58:01.391Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%86",
 "prompt": "Persian زن (zan) 'woman, wife': give the etymology section verbatim — Middle Persian form, Proto-Iranian, PIE, Avestan cognate, and cited authorities."
}
```


## [2026-09-06T14:58:02.876Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/queen",
 "prompt": "Etymology of queen: Old English cwen, Proto-Germanic form, PIE root, and cognates (Gothic qino/qens, Greek gyne, Sanskrit jani, Avestan)."
}
```


### [2026-09-06T14:58:07.012Z] TOOL RESULT

```
# Persian زن (zan) Etymology

**Middle Persian Form:**
"Inherited from Middle Persian [script needed] (zan)"

**Proto-Iranian Origin:**
Derived from "Proto-Iranian *ǰánHs," which descended from Proto-Indo-Iranian *ǰánHs.

**Proto-Indo-European Root:**
Traced to "Proto-Indo-European *gʷénh₂s, from *gʷḗn"

**Cognates:**
The entry lists several related words across Indo-European languages, including English "queen," Northern Kurdish "jin," Greek "γυναίκα" (gynaíka), and Russian "жена" (žena).

**Note on Avestan:**
The provided text does not include a specific Avestan cognate or citation to Avestan authorities. The etymology section traces the word back through documented Middle Persian, Proto-Iranian, and Proto-Indo-European stages, but does not reference Avestan sources or cognates.
```


### [2026-09-06T14:58:09.485Z] TOOL RESULT

```
# Etymology of Queen

The word "queen" originates from Middle English *quene*, derived from Old English *cwen*, meaning "female ruler of a state; woman; wife." It traces back through Proto-Germanic *kwoeniz* to the PIE root *gwen-, meaning "woman."

## Key Historical Points

**Original Sense**: The most ancient Germanic usage referred simply to "wife," which later specialized to mean "wife of a king" by Old English times.

**Linguistic Distinction**: "English is one of the few Indo-European languages to have a word for 'queen' that is not a feminine derivative of a word for 'king.'" Scandinavian languages share this feature.

**Extended Meanings**: By late Old English, the term was applied figuratively to anything personified as chief or greatest with female attributes. Modern uses include:
- Chess piece (c. 1400)
- Playing card (1570s)
- Queen bee (c. 1600)
- Slang for male homosexuals (1924)
- Bed size designation (1954)

The word demonstrates how semantic specialization transformed a general term for "woman" into a specific reference for female monarchs and rulers.
```


## [2026-09-06T14:58:15.094Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"زن (\" ARY_pages.txt | head -5; echo \"=== gran ===\"; grep -n \"گران\" ARY_pages.txt | head -8; echo \"=== latin index ===\"; grep -n \"GWEN\\|GWER\" ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur for zan and geran"
}
```


### [2026-09-06T14:58:15.187Z] TOOL RESULT

```
=== gran ===
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
123:نواحی زبان‌های اولیه این سّرزمین‌ها نبوده‌اند و توسط کوچگران به آنجا برده شده‌اند. ۳-بسیاری از
170:دستوری و آوایی و واژگان آن) زبان کوچگران هند و اروپایی را متقابلاً تحت تأثیر قرار داد. این
176:بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
210:خواهیم رسید که مرکز تغل باگرانیگاه (67۸۷17۷ 05 032۲788) این موج‌ها در حدود مرز... |
309:کوچگران وقتی به گیاه یا جانور تازه‌ای برمی‌خورند يا نام محلی را می‌پذپرفتند» یا نام جدیدی را
440:ارائه شد (زبانها لتوانی و آلبانی و ارمنی و تخاری بعداً توسط دیگران شناسایی و به فهرست ری
645:برخی دانشمندان معتقد شوند که کوچگران هندی قبل از ایرانیان وارد فلات ایران شده و در سرزمین
=== latin index ===
2886:GWENT ABRETON) is 2 VIND (NORWEGIAN) ($333
```


## [2026-09-06T14:58:19.998Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"^زن\\|^ *زن \" ARY_pages.txt | head -10; echo \"=== geran headword ===\"; grep -n \"گران:\\|^گران\\|گران \" ARY_pages.txt | head -10; echo \"=== QUEEN ===\"; grep -n \"QUEEN\\|GRAVIS\\|BARUS\" ARY_latin_index_pages.txt | head -10",
 "description": "Search ARY for headwords"
}
```


### [2026-09-06T14:58:20.082Z] TOOL RESULT

```
153:زندگی می‌کردند و بهمین دلیل زبان آنها پا فاقد گویش‌ها ی گوناگون بود و یاگویش‌های آن بهم بسیار
665:زندگی می‌کنند. :
8941:زنراز ۱ برهان قاطع : . ۹۳۹
9630:زنخ» زنخدان (به چم "چانه") | ۳۲۷
=== geran headword ===
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
123:نواحی زبان‌های اولیه این سّرزمین‌ها نبوده‌اند و توسط کوچگران به آنجا برده شده‌اند. ۳-بسیاری از
170:دستوری و آوایی و واژگان آن) زبان کوچگران هند و اروپایی را متقابلاً تحت تأثیر قرار داد. این
309:کوچگران وقتی به گیاه یا جانور تازه‌ای برمی‌خورند يا نام محلی را می‌پذپرفتند» یا نام جدیدی را
440:ارائه شد (زبانها لتوانی و آلبانی و ارمنی و تخاری بعداً توسط دیگران شناسایی و به فهرست ری
645:برخی دانشمندان معتقد شوند که کوچگران هندی قبل از ایرانیان وارد فلات ایران شده و در سرزمین
646:وسیعی از بین‌النهرین تا شمال شبه قاره‌ی هند ماندگار شدند. سپس کوچگران ایرانی آمدند و فلات
736:چندین دهه قبل» کاوشگران حدود سه هزار خشت سفالی دارای نوشتار در جزیره‌ی کرت و :
763:اسپانیایی و پرتغالی و رومانی و غیره گردیدند. کوچگران زبان‌های رومانس را به امریکای جنوبی و
1026:هومر) نشان می‌دهند که رسم چند زنی نیز در میان توانگران هند و اروپایی رایج بوده است. ژول
=== QUEEN ===
3404:BALBASYTI, —_—:(LITHUANIAN) gp BARBARUS, BARBAR — (LATIN) 3)
9446:QUEAN, QUEEN (ENGLISH) AS! JANIS (SANSKRIT) 24 Sie
9461:BARNHART: — (QUEAN, QUEEN) 874 ‘ZHENA L(SERBIAN) 9 po :
9465:ONIONS: (QUEAN, QUEEN) 731 SIEVA LATVIAN) (93) 53 |
9466:SKEAT:  (QUEAN) 491, (QUEEN) 492 GENNA — (OLD PRUSSIAN) on 9.1 |
9470:sel WSL" QUEEN pp y cael “Ahcbe 63543 03° QUEAN 65 yy St 52 |
12410:POKORNY. ——=~S*«~*~*«*«TGATD GRAVIS ALATIN) opi
```


## [2026-09-06T14:58:23.892Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '9440,9480p' ARY_latin_index_pages.txt; echo \"##### gravis\"; sed -n '12400,12440p' ARY_latin_index_pages.txt",
 "description": "Print Aryanpur zan and geran entries"
}
```


### [2026-09-06T14:58:23.961Z] TOOL RESULT

```
QVENA, — (OLD SAXON) oS gp-S ZAN (PAHLAVI) 5 3h
QVAN . JIN (KURDISH) 63,5
(OLD HIGH GERMAN) oS gl JAN S(BALUCHI) gx sh
QUENA, GUENA JINAL AFGHAN) ( =), 3lsi!
CWENE, (OLD ENGLISH) oS ssi SAM -(TOKHARIAN A) A 5,65
CWEN SANA -(TOKHARIAN B) B ys 63
QUEAN, QUEEN (ENGLISH) AS! JANIS (SANSKRIT) 24 Sie
KVINDE, KONE —«(DANISH) S\ail2 KIN ARMENIAN) «gi 5)
KVINNA, KONA (SWEDISH) 3» GYNE (GREEK) ii.
KVINNE (NORWEGIAN) (5335 QUING, GENS, GOTHIC) S36
QUENE (DUTCH) sachs KWENS
(OLD CHURCH SLAVIC) ot Gel (OLD SCANDINAVIAN) 45$4h—11
a
[pdf page 326]
‘
TYV | Calle” pep) Oladj G35
\
ZONJE ALBANIAN) gi3T ZHENA
ZONA (POLISH) lng)
‘REFERENCES bok, ‘ZENA, ZENSHCHINA :(RUSSIAN) +5,
POKORNY. = =~S~S*~*~*~*~*~S*S«TS: ZHENA CZECH) Soy '
BARNHART: — (QUEAN, QUEEN) 874 ‘ZHENA L(SERBIAN) 9 po :
DELAMARRE: (FEMME) 49 ‘ZHENA (SLOVAK) Suit
MACKENZIE: (WOMAN) 140 ZHENA BOHEMIAN) gas |
BUCK: 82-83 ZHMONA (LITHUANIAN) gy |
ONIONS: (QUEAN, QUEEN) 731 SIEVA LATVIAN) (93) 53 |
SKEAT:  (QUEAN) 491, (QUEEN) 492 GENNA — (OLD PRUSSIAN) on 9.1 |
rr ight iby GEN, BEN «(OLD IRISH) oS 544 p1
BENYW (WELSH) §3)y
deeds
sel WSL" QUEEN pp y cael “Ahcbe 63543 03° QUEAN 65 yy St 52 |
!
|
|
|
ZIN, KIN. (OLD FRISIAN) oS 3,3 ZANVA HAVESTAN) glogl
KINNI:(OLD HIGH GERMAN) yf gst (KURDISH) 59,5
KINN (GERMAN) (glT CHENE, CHENG, ZAND i
CIN HOLD ENGLISH) iy poSSi\ ZENA HAFGHAND) (5-4) gi |
CHIN ENGLISH) S61 SANWEM —(TOKHARIAN A) A 65 . |
KIND DANISH) Sails HANUS (SANSKRIT) idg Suite ae
##### gravis
et $3 alae ty 5l gpa 2 OT ley Seo b coe gel salty a geal Gb) alah UY
eet AL) glass 4a seal Je blac,
KYRR, KUIRR GOURO, GARU —{AVESTAN) gles!
GRAVE (Ail, jIHENGLISH) pS! *GRANA — (OLD PERSIAN) dtl, go sh,
GORSTU, GURTI (LITHUANIAN) gly GARAN _ HPAHLAYD 8 4,
GRUTS LATVIAN) (3) 93 GHIRAN, GIRAN (KURDISH) (52
BAIR OLD IRISH) eS 5-4) ph GRAN AFGHANI) (32) sil
BRYW (WELSH) ($315 KRAMARTS  :(TOKHARIAN A)A 55
GUROH, GURUS (SANSKRIT) St
‘REFERENCES thy BARYS, BAROS GREEK) gli,
POKORNY. ——=~S*«~*~*«*«TGATD GRAVIS ALATIN) opi
BARNHART: (GRAVE) 447 GRAVE H(PRENCH) Wil
DELAMARRE: (LOURD) 223 GRAVE SPANISH) gill
MACKENZIE: (HEAVY) 117 GRAVE LUTALIAN) .glls\
ONIONS: (GRAVE) 411 GREU RUMANIAN) «gay,
SKEAT: (GRAVE) 248 GRAVE (PORTUGUESE) Js x
AMINDAROV: (HEAVY) 235 KAGRUS GOTHIC) SF
YVAN L eu oly :(OLD SCANDINAVIAN) 48 44!
[pdf page 426]
mies
detlasl
Bish gh Tiga call 2 03s ol
Obi 2 039 gh gle) 32 059 onl
feet re |
*URPA (OLD PERSIAN) ky eo
‘REFERENCES bch GURPAK, GURBAG  :(PAHLAVI) 5 hy |
POKORNY. —=~SO*~*~S~S~*~«a URUPIS SANSKRIT) 2 Sila
war | sbi Oey GADOU ARMENIAN) 31
icetlook
HGSGATO pile) CHAT gests y CATUS oS yKATZE gliT 5 CAT poJ63i laejly lt
hts Lead Uy i pST Sly gel el tiie Lalita, ly et ly LA eel A rly coe
(BARNHART: 149)
GARDER GaRgDHO AVESTAN) poe 3b
HOLD SAXON) 5 gip-Sle *  SKRTA (OLD PERSIAN) ileal, gs
GARD, GARDO KART | APAHLAVD) 5 34
GARDA HOLD FRISIAN) 5 52.3 GORAD, GORAET = :(OSSETIC) c=)
(OLD HIGH GERMAN) pS glasT KERCIYE —_:(TOKHARIAN B) B «5 ,\55, “4! w
GARTO, GART GRHAS 1 ANSKRED SS |
GARRTEN GERMAN) gtT GARTH 1 NY (ARMENIAN) ys)
GEARD — {OLD ENGLISH) oy ,-&i\ KORTHIS, KORTOS (GREEK) giz
YARD, GARDEN (ENGLISH) y1Si\ HORTUS (LATIN) 3
```


## [2026-09-06T14:58:39.699Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'NR<=9446 && /\\[pdf page/{p=$0; n=NR} END{}' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<9446' | tail -2; echo ---; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<12410' | tail -2",
 "description": "Find ARY pdf page tags"
}
```


### [2026-09-06T14:58:41.338Z] TOOL RESULT

```
9376:[pdf page 324]
9420:[pdf page 325]
---
12364:[pdf page 424]
12390:[pdf page 425]
```


## [2026-09-06T14:58:51.075Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%DA%AF%D8%B1%D8%A7%D9%86",
 "prompt": "Give the Mo'in (فرهنگ معین) entry text for گران verbatim, including any bracketed origin tag such as [په.] or [پهلوی]."
}
```


## [2026-09-06T14:58:52.234Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A8%D8%A7%D8%B1%D9%88%D9%85%D8%AA%D8%B1",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for بارومتر verbatim, including any bracketed origin tag such as [فر.] (French)."
}
```


### [2026-09-06T14:58:55.031Z] TOOL RESULT

```
# Mo'in Dictionary Entry for گران

According to the webpage, the Mo'in (فرهنگ انتشارات معین) entry for گران reads:

"سنگی ( ~ . سَ) (حامص .) سنگینی ، وقار."

This entry indicates the word can mean weightiness or dignity, with a notation referencing Hamasa and including what appears to be a diacritical mark indicator.
```


### [2026-09-06T14:58:56.350Z] TOOL RESULT

```
According to the Mo'in dictionary entry shown on this page, the definition for بارومتر is:

"(رُ مِ) \[ فر. \] ( اِ.) اسبابی برای اندازه گیری فشار جو، فشارسنج هوا، فشار - سنج . (فره )."

This indicates the word is of French origin [فر.] and refers to an instrument for measuring atmospheric pressure, also called a barometer or air pressure gauge.
```


## [2026-09-06T14:59:01.287Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A8%D8%A7%D8%B1%DB%8C%D9%85",
 "prompt": "Give the Mo'in entry for باریم verbatim, including the origin tag (e.g. [فر.]) and the gloss."
}
```


## [2026-09-06T14:59:02.575Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30340,30352p' MON_part2.txt",
 "description": "Print Moin geran neighborhood"
}
```


### [2026-09-06T14:59:02.627Z] TOOL RESULT

```
گرامافون: 0- ۳6۲۱05 (- گرامافن | .( 
التن اشت که صفحه‌ای را که آوازی در 
آن ضط شده به گردش در آورد و همان 
آواز را به گوش رساند. جعبةً صوت. 
گرامی: 1-:5:»: (ص.) عزیزه محترم. 
ضح.- در نظم و نثر فصیح همه جا گرامی (- 
گرامیکث» به.) آمده و «گرام ۲ - که در 
تداول بجای گرامی پا کرام عربی (ج. کریم) 
استعمال کنند . درست نیست. 
گران: 2030 (ضن:] کیت تقیل» وزین؛
```


### [2026-09-06T14:59:03.324Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T14:59:37.776Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷḗn\" \\\n \"https://en.wiktionary.org/wiki/कन्या\" \\\n \"https://en.wiktionary.org/wiki/زن\" \\\n \"https://en.wiktionary.org/wiki/گران\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 208, roots Gwen 1 / Gwer 1: PIE *gʷḗn woman, Skt kanyā, NPers zan, NPers gerān\" 2>&1 | tail -2; done",
 "description": "Archive wiktionary sources"
}
```


### [2026-09-06T14:59:41.061Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e2458573e88483ff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c04cce32cdc04c57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c8941709e12af7c5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b9a9c020ce00f33.txt
```


## [2026-09-06T14:59:44.905Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/gynecology\" \\\n \"https://www.etymonline.com/word/queen\" \\\n \"https://www.etymonline.com/word/barium\" \\\n \"https://www.etymonline.com/word/barometer\" \\\n \"https://www.etymonline.com/word/grief\" \\\n \"https://vajehyab.com/moein/بارومتر\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 208, roots Gwen 1 / Gwer 1: gynecology, queen, barium, barometer, grief, Mo'in barometer entry\" 2>&1 | tail -1; done",
 "description": "Archive etymonline and vajehyab sources"
}
```


### [2026-09-06T14:59:49.081Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a8063b32e5981c03.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cbc689d10efba1e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/858b5eb403f6adcf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95482496c96b01ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30e92d0fcd5b0d0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93a0defd9ef37424.txt
```


## [2026-09-06T14:59:53.642Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check script"
}
```


### [2026-09-06T14:59:53.696Z] TOOL RESULT

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


## [2026-09-06T14:59:58.532Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py; mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg208.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/208.png && echo copied",
 "description": "Rest of verify_check and copy page image"
}
```


### [2026-09-06T14:59:58.601Z] TOOL RESULT

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
copied
```


## [2026-09-06T15:11:37.162Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk208.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE_GWEN = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷḗn\"\nW_KANYA = \"https://en.wiktionary.org/wiki/कन्या\"\nW_ZAN = \"https://en.wiktionary.org/wiki/زن\"\nW_GERAN = \"https://en.wiktionary.org/wiki/گران\"\nE_GYN = \"https://www.etymonline.com/word/gynecology\"\nE_QUEEN = \"https://www.etymonline.com/word/queen\"\nE_BARIUM = \"https://www.etymonline.com/word/barium\"\nE_BAROM = \"https://www.etymonline.com/word/barometer\"\nE_GRIEF = \"https://www.etymonline.com/word/grief\"\nV_BAROM = \"https://vajehyab.com/moein/بارومتر\"\n\nPOK473 = (\"POK_full.txt lines 39830-39898: 'Root / lemma: gʷenā (*ghʷenā) || Meaning: woman, wife, *goddess || \"\n          \"Grammatical information: Gen. gʷn-as and *gʷē-as, also Nom. gʷenə-, gʷenī- || Material: Old Indic gnā (*gʷnā) f. \"\n          \"'divine woman, goddess' ... Avestan gənā, ɣnā 'wife, woman'; Old Indic jani-h = Avestan jaini, npers. zan ds. ... \"\n          \"gr. γυνή 'woman' (*gʷunā) ... Gothic qino (*gʷen-ōn-) = Old English cwene ... lengthened grade Gothic qēns 'wife' \"\n          \"(*gʷēni-s = Avestan jani-, Old Indic jani-) ... Old English cwēn ... Page(s): 473-474.'\")\n\nPOK476 = (\"POK_full.txt lines 39525-39606: 'Root / lemma: gʷer-2, gʷerə-, gʷerəu-, gʷerī- || Meaning: heavy || Material: \"\n          \"Old Indic guru-h 'heavy, important, venerable' ... Avestan gouru- (in compound) 'heavy'; npers. giran 'heavy' (*grāna-, \"\n          \"reshuffling after *frāna- 'full'); gr. βαρύς 'heavy', βάρος n. 'heaviness'; Latin gravis 'heavy, weighty' (*gʷra-u-is) \"\n          \"... Gothic kaurjos 'heavy' ... Page(s): 476-477.'\")\n\nAHD_GWEN = (\"Watkins 1985 IE-roots appendix (AHD_watkins1985.txt line 542): 'gʷen-. Woman. 1. Suffixed form *gʷen-ā- in: \"\n            \"a. Germanic *kwenōn- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben ...; c. Persian zan, woman: ZENANA. \"\n            \"2. Suffixed lengthened-grade form *gʷēn-i- in Germanic *kwēniz, woman, wife, queen, in Old English cwēn: QUEEN. \"\n            \"3. Suffixed zero-grade form *gʷn-ā- in Greek gunē, woman: GYNO-, -GYNOUS, -GYNY; GYNAECEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gʷenā 473.]'\")\n\nAHD_GWER = (\"Watkins 1985 (AHD_watkins1985.txt line 542): 'gʷerə-2. Heavy. I. Zero-grade form *gʷrə-. 1. Suffixed form *gʷrə-u-i- in \"\n            \"Latin gravis, heavy, weighty: GRAVE2, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form *gʷrə-u- in: \"\n            \"a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, ...; b. Sanskrit guru-, heavy, venerable: GURU. \"\n            \"3. Suffixed form *gʷrə-es- in Greek baros, weight: BAR2, BARO-; ... ISOBAR. ... [Pok. 2. gʷer- 476.]'\")\n\nBUCK82 = (\"Buck, Selected Synonyms, printed p.82 (the leaf carries the running head '82 SELECTED INDO-EUROPEAN SYNONYMS'), table \"\n          \"'2.22 WOMAN': 'Grk. γυνή ... Goth. qinō ... OE cwene, wif, wifman ... ME quene, wife, woman ... Skt. jani-, nārī-, strī- ... \"\n          \"Av. jani-, nāirī-, strī-', and the discussion running on to p.83: 'Skt. jani-, jānī-, -jani-, Av. jaini- (NPers. zan), gənā-, etc.; \"\n          \"Arm. kin; Toch. śäm.'\")\n\nBQT1033 = (\"Borhān-e Qāteʿ, the زن article with Mo'in's footnote 1 (BQT_v2_pages.txt leaf 496, printed ≈1031-1033; vol. 2 has no page tags \"\n           \"and the leaf→page offset drifts ±2 here — leaf 500 = printed ≈1038-1040): 'پهلوی zan (زن، زوجه)، اوستا jaini- «بارتولمه»، \"\n           \"رک: نیبرگ، هندی باستان jani- (زن، زوجه)، ارمنی kin (زن، بانو)، کردی žīn، افغانی، بلوچی، شغنی، سریکلی، منجی «اشتقاق ۸۹۱»' \"\n           \"— precisely the Avestan → Pahlavi → New Persian chain the arrow draws.\")\n\nBQT1781 = (\"Borhān-e Qāteʿ printed p.1781 (= BQT_v3_picofile.pdf p.578; rendered and OCR'd with tools/ref_page.py BQT:1781, \"\n           \"running head '۱۷۸۱ گران‌پشت'), headword 'گران — بکسر اول بروزن نشان. ثقیل و سنگین باشد که در مقابل خفیف و سبک است \"\n           \"— و در مقابل ارزان هم هست', with Mo'in's footnote 1: 'پهلوی garān (سنگین، ثقیل)، از اوستا gouru- از garu- «بارتولمه»، \"\n           \"نیبرگ ص ۷۸، پارسی باستان *garu- «هوبشمان ۸۹۸»، کردی girān (ثقیل، گران، سخت) «ژابا ۳۵۸»' — exactly the arrow Avestan gouru- → Persian gerān, \"\n           \"with the Pahlavi link the chart leaves out. (The Latin-script forms are digit-garbled in the OCR; they are read off the rendered page image.)\")\n\ndata = {\n  \"pdf_page\": 208,\n  \"book_page\": 178,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gwen 1, Gwenâ, Gwŭnâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷḗn, oblique *gʷnéh₂s (Pokorny 'gʷenā', Nom. also gʷenə-, gʷenī-) 'woman, wife'\",\n      \"note\": \"The root box is right on all four counts — form, language label, gloss and page. Pokorny's lemma at p.473-474 is literally 'gʷenā ... Meaning: woman, wife, *goddess', with the Genitive *gʷn-as that produces the Greek *gʷunā; Watkins has 'gʷen-. Woman. [Pok. gʷenā 473.]'; Wiktionary reconstructs the proterokinetic *gʷḗn / *gʷnéh₂-. Nourai's three headings therefore correspond one-to-one to Pokorny's three quoted stems: Gwen = gʷen-, Gwenâ = gʷenā, Gwŭnâ = the *gʷunā that Walde-Pokorny I 681 posits behind Greek γυνή. Like the Gwei chart two pages earlier, almost the whole tree is Pokorny's own article rearranged: Old Indic gnā / jani-, Avestan gənā / ɣnā / jaini-, npers. zan, Greek γυνή, Gothic qinō / qēns and Old English cwene / cwēn all stand in those two pages, and Buck p.82-83 (Nourai's SYN:82) prints the same list in tabular form. Only two things need correcting: the Sanskrit box smuggles in kan / kanya, which belong to a different root (*ken- 'fresh, young', whence Av. kainiiā, MP kanīg, NP کنیز), and a form 'gunâ' that no Sanskrit dictionary knows (the Sanskrit forms are gnā and gánā); and the Latin pass-through box before gyno-/gynecology is at best a Neo-Latin, in fact a French, stage.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۷۳–۴۷۴ مادهٔ *gʷenā را با معنای «زن، همسر» آورده و همان سه صورتی را می‌دهد که نورایی در سر‌واژه نوشته است (gʷen-، gʷenā و — در پشت یونانی γυνή — *gʷunā که والده–پوکورنی در جلد یک، ص ۶۸۱ بازسازی کرده)؛ ویکی‌واژه آن را *gʷḗn با حالت غیرمستقیم *gʷnéh₂s می‌نویسد. بیشتر نمودار در واقع بازچینش همان دو صفحهٔ پوکورنی است و بوک نیز در ص ۸۲–۸۳ همین فهرست را جدول‌وار آورده است. دو نکته باید اصلاح شود: در جعبهٔ سنسکریت دو واژهٔ kan و kanyā آمده که از ریشهٔ دیگری است (*ken- «تازه، جوان»، اوستایی kainiiā، فارسی میانه kanīg، فارسی نو «کنیز»)، و صورتی به شکل gunâ در سنسکریت وجود ندارد (صورت‌های درست gnā و gánā است)؛ دیگر آنکه جعبهٔ خالی «لاتین» پیش از gynecology در بهترین حالت لاتینی نو است و در واقع واسطهٔ فرانسوی بوده است.\",\n      \"sources\": [W_PIE_GWEN, W_ZAN, W_KANYA],\n      \"ref_check\": [\n        {\"ref\": \"POK:473\", \"status\": \"supports\", \"note\": POK473}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 681 (WLD_Bd1_pages.txt lines 64487-64570, running head 'gʷena')\", \"stance\": \"supports\",\n         \"note\": \"'gʷena \\\"Weib, Frau\\\", gʷenu, gʷīnā-, im Germ. und Arm. auch en-St. *gʷen-en- ... Ai. gánā (*gʷenā) und gnā (*gʷnā) \\\"Götterweib\\\", av. gənā, ɣnā \\\"Frau, Weib\\\"; ai. jani-h = av. jani-, np. zan \\\"Weib\\\" ... gr. γυνή \\\"Frau\\\" aus *gʷunā neben *gʷenu in boot. βανά ... got. qinō (*gʷenon-) = ags. cwene, ahd. quena ... got. ē-St. qēns (= av. jani-)' — the source article behind Pokorny 473, and the explicit authority for Nourai's third root form Gwŭnâ.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷen- (AHD_watkins1985.txt line 542)\", \"stance\": \"supports\", \"note\": AHD_GWEN},\n        {\"src\": \"SYN\", \"where\": \"Buck, printed p.82-83, §2.22 WOMAN\", \"stance\": \"supports\", \"note\": BUCK82}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ğnâ, genâ, žaini, jâni\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are real Avestan words for 'woman' and all four stand in Pokorny's article on the very page cited. ɣnā- (Nourai's 'ğnâ') and gənā- ('genâ') are the two sandhi variants of one ā-stem — the zero grade *gʷn-éh₂ giving ɣnā- with the regular Iranian gʷ > g > ɣ before a nasal-less cluster, and the anaptyctic variant gənā- with the prop vowel ə that Avestan inserts in initial clusters; both mean 'woman, wife' and both are cognate with Old Indic gnā 'divine woman'. The i-stem ǟaini- (nom. ǟainiš, acc. pl. jainīš in Yt.15.80) and its compound form -jǟni-/jāni- continue PIE lengthened-grade *gʷēn-i- (= Gothic qēns, Old Indic jáni-); PIE *gʷ > Indo-Iranian ǵ > Iranian Ǟ- before front vowels is the standard palatalisation, so *gʷēn-i- > *ǵáni- > Av. ǟaini-. Bartholomae's own headword is 'ǟanay-, Gathic ǟẗnay- \\\"Weib, Frau\\\"', explicitly glossed with 'ai. jánay- f., np. زن'. The one blemish is the spelling 'žaini': Avestan ž is a distinct sound (as in žbā-), and the woman-word has ǟ (j); the printed page (p.178) really does read 'žaini', so this is Nourai's own transliteration slip, not an extraction error — note that he writes 'jâni' with j in the same box.\",\n          \"derivation_fa\": \"هر چهار صورت اوستایی اند و همه در همان دو صفحهٔ پوکورنی آمده‌اند: ɣnā- و gənā- دو گونهٔ یک ستاک اند که از درجهٔ صفر *gʷn-éh₂ می‌آیند، یکی با واکهٔ میانجی ٔ، و هم‌ریشهٔ سنسکریت gnā «زن ایزدی» اند؛ و ǟaini- و jāni- از درجهٔ کشیدهٔ *gʷēn-i- اند که با پادشدگی (تاویزی) همخوان لبی–کامی پیش از واکهٔ پیشین در هندوایرانی به ǵ و سپس در ایرانی به Ǟ بدل شده است. بارتولمه مادهٔ «ǟanay-، گاهانی ǟẗnay- „Weib, Frau“» را خود با «ai. jánay- f.، np. زن» توضیح داده است. تنها ایراد، نوشتن «žaini» به جای ǟaini- است؛ صفحهٔ چاپی هم همین را دارد، پس خطای خود مؤلف است نه خطای خوانش اسکن. در مجموع ادعای نورایی درست است.\",\n          \"sources\": [W_PIE_GWEN, W_ZAN],\n          \"ref_check\": [\n            {\"ref\": \"POK:473\", \"status\": \"supports\", \"note\": \"Pokorny p.473-474 has, in one sentence, 'Avestan gənā, ɣnā \\\"wife, woman\\\"; Old Indic jani-h = Avestan jaini, npers. zan ds. ... in compounds Old Indic lengthened grade -jani- = Avestan jāni- ds.' — all four of Nourai's forms, in his order (POK_full.txt lines 39845-39850).\"},\n            {\"ref\": \"SYN:82\", \"status\": \"supports\", \"note\": BUCK82}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch, s.v. ǟanay- (BRT.txt line 11557)\", \"stance\": \"supports\",\n             \"note\": \"'j. ǟanay-, g. ǟẗnay- \\\"Weib, Frau\\\" ... daēva ... *apa.karšayən jainīš (AP.) hača mašyākaēibyō Yt.15.80', with the etymological line 'ai. jánay- f., np. زن'. The homonym at line 11560, 'j. jaini- Adj., nur KompA. \\\"tötend, mordend\\\"' (to the verb gan- 'strike'), is a different word and shows why the reading ǟ/j matters.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷen-\", \"stance\": \"partial\", \"note\": \"Watkins reaches Persian zan directly from *gʷen-ā- ('c. Persian zan, woman: ZENANA') without listing the Avestan forms, so he supports the root but is silent on this node's four citation forms.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 681\", \"stance\": \"supports\", \"note\": \"'av. gənā, ɣnā \\\"Frau, Weib\\\"; ai. jani-h = av. jani-, np. zan \\\"Weib\\\" ... in Zs. ai. -jani- (dvi-jani \\\"zwei Weiber besitzend\\\") = av. jāni- \\\"Weib\\\"' — the same four forms.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zan «زن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian زن zan 'woman, wife' continues Middle Persian zan (Book Pahlavi zn), from Old Iranian *ǵani- — the same i-stem as Avestan ǟaini- — from PIE *gʷḗn / *gʷénh₂s. The Persian consonant is the expected outcome: Proto-Iranian initial *Ǟ (from palatalised *gʷ before a front vowel) is preserved as j in Avestan but becomes z in Old and Middle Persian, exactly as in *ǟan- 'strike' > OP jan- / MP zadan (Hübschmann's §120b lists zan under this very rule). The final -i of the stem is lost in Middle Persian; the word has no plural marker of its own in classical usage. Strictly the parent drawn here, the Avestan box, is a cognate rather than the ancestor of the Persian word — zan descends from the Persian-dialect continuant of the same Old Iranian stem — but that is the chart's standing convention, and Pokorny, Buck, Bartholomae and Mo'in all set 'Av. jaini- : NPers. zan' side by side in the same way.\",\n          \"derivation_fa\": \"«زن» در فارسی نو دنبالهٔ zan فارسی میانه (پهلوی zn) است، از ایرانی باستان *ǵani- — همان ستاکی که در اوستا ǟaini- شده — و سرانجام از هندواروپایی آغازین *gʷḗn. دگرگونی آوایی قاعده‌مند است: Ǟ آغازین ایرانی در اوستا j می‌ماند ولی در گویش پارسی (پارسی باستان و پهلوی) به z بدل می‌شود — همان‌گونه که اوستایی jan- در فارسی «زدن» شده است (هوبشمان، بند ۱۲۰ دقیقاً «زن» را ذیل همین قاعده می‌آورد). حاشیهٔ معین بر برهان قاطع نیز همین زنجیره (اوستا jaini- ← پهلوی zan ← فارسی زن) را می‌دهد. ادعای نورایی درست است؛ تنها باید دانست که صورت اوستایی هم‌ریشه است نه نیای مستقیم.\",\n          \"sources\": [W_ZAN, W_PIE_GWEN],\n          \"ref_check\": [\n            {\"ref\": \"POK:473\", \"status\": \"supports\", \"note\": \"Pokorny p.473: 'Old Indic jani-h = Avestan jaini, npers. zan ds.' — the arrow as drawn (POK_full.txt line 39846).\"},\n            {\"ref\": \"BQT:1033\", \"status\": \"supports\", \"note\": BQT1033}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §120b (HUB.txt line 8169)\", \"stance\": \"supports\",\n             \"note\": \"'zan \\\"Weib\\\" = zd. jəni- \\\"Weib\\\"', listed among the words showing ap. j (= idg. gʷ, gʷh) > np. z, next to 'zadan \\\"schlagen\\\" = zd. ap. jan, skr. han' — both the etymology and the sound law.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt line 5095, the entry list 'zan')\", \"stance\": \"supports\",\n             \"note\": \"MacKenzie's glossary carries 'zan [zn | N ~] woman, wife'; the OCR of the local scan is broken in this stretch but the headword zan is legible, and Aryanpur's entry cites 'MACKENZIE: (WOMAN) 140' for the same form.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, entry زن (ARY_latin_index_pages.txt pdf page 325 = printed 326)\", \"stance\": \"supports\",\n             \"note\": \"The cognate list runs 'ZAN (PAHLAVI) – JANIS (SANSKRIT) – KIN (ARMENIAN) – GYNE (GREEK) – QUING, GENS (GOTHIC) – CWENE, CWEN (OLD ENGLISH) – QUEAN, QUEEN (ENGLISH) – ZENA (RUSSIAN) ...', with references 'POKORNY 473 ... BUCK: 82-83 ... MACKENZIE: (WOMAN) 140' — an independent modern Persian source citing the very Pokorny and Buck pages Nourai cites.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p.82-83\", \"stance\": \"supports\", \"note\": \"'Av. jaini- (NPers. zan)' — Buck writes the arrow in parentheses.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"gnâ, gunâ, jani, kan, kanya\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The box mixes two roots. gnā- 'wife of a god, goddess' (also gánā-) and jáni- / jāní- 'wife, woman' do belong here: gnā is the zero grade *gʷn-éh₂ and jáni- the *gʷén-i- form, and Pokorny prints both on p.473 as the Indic members of this root. But kan- and kanyā do not: Sanskrit kanyā 'maiden, girl' goes back to Proto-Indo-Iranian *kanyaH and PIE *ken- 'new, fresh, young' (whence Latin re-cēns, Greek kainós), with Avestan kainiiā 'maiden' and Middle Persian kanīg the Iranian cognates — that is the source of Persian کنیز, not of زن. The initial k- is itself proof: a PIE labiovelar *gʷ cannot yield Sanskrit k-, it yields j- or g-. Nourai has evidently been misled by the surface resemblance kanā/ganā. The third form 'gunâ' is not a Sanskrit word at all (guṇā is 'thread, quality'); the printed page (p.178) does read 'gunâ', so the extraction is faithful — the form is Nourai's own, apparently the Greek preform *gʷunā (his root heading 'Gwŭnâ') mistakenly filed under Sanskrit, or a misprint for gánā.\",\n          \"derivation_fa\": \"این جعبه دو ریشه را در هم آمیخته است. gnā- «زن ایزدی» و jáni- «زن، همسر» درست از همین ریشه اند و پوکورنی هر دو را در ص ۴۷۳ آورده است؛ اما kan و kanyā چنین نیستند: سنسکریت kanyā «دختر، دوشیزه» از هندوایرانی *kanyaH و ریشهٔ هندواروپایی *ken- «تازه، نو، جوان» است (لاتین re-cēns، یونانی kainós)، هم‌ریشهٔ اوستایی kainiiā و فارسی میانهٔ kanīg، که در فارسی نو «کنیز» شده است نه «زن». خود واک k آغازین گواه قاطع است، زیرا *gʷ هندواروپایی در سنسکریت هرگز k نمی‌دهد، بلکه j یا g می‌دهد. صورت «gunâ» نیز در سنسکریت وجود ندارد؛ صفحهٔ چاپی همین را دارد، پس خطای کتاب است نه خطای خوانش اسکن، و ظاهراً همان *gʷunā یونانی است که به غلط زیر سنسکریت نشسته است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"gnâ, gunâ, jani, kan, kanya\",\n          \"correct_form\": \"gnā, gánā, jáni- (kan-, kanyā belong to PIE *ken- and should be removed)\",\n          \"sources\": [W_KANYA, W_PIE_GWEN],\n          \"ref_check\": [\n            {\"ref\": \"POK:473\", \"status\": \"partial\", \"note\": \"Pokorny p.473 supports gnā and jani- ('Old Indic gnā (*gʷnā) f. \\\"divine woman, goddess\\\" ... Old Indic jani-h ... Old Indic also jāni'), but neither kan nor kanyā nor any 'gunā' appears in the article; kanyā is treated by Pokorny under ken-3 'frisch, jung' (p.563), a different lemma.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 681\", \"stance\": \"partial\", \"note\": \"'Ai. gánā (*gʷenā) und gnā (*gʷnā) \\\"Götterweib\\\" ... ai. jani-h = av. jani-' — Walde-Pokorny gives gánā (with a), never gunā, and knows nothing of kan/kanyā here.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷen- and s.v. ken- 'fresh, new, young'\", \"stance\": \"contradicts\", \"note\": \"Watkins puts Sanskrit kanyā-'s family under ken- ('fresh, new, young'), not under gʷen-; his gʷen- article lists no Sanskrit k-form at all.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p.82-83 §2.22\", \"stance\": \"partial\", \"note\": \"Buck's Sanskrit entry for 'woman' is 'jani-, nārī-, strī-' with 'Skt. jani-, jānī-, -jani-' in the discussion; kanyā is absent (it belongs to his §2.26 'girl').\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"kweniz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *kwēniz 'woman, wife' is the regular continuant of the PIE lengthened-grade i-stem *gʷēn-i-s (the same stem as Gothic qēns and Avestan jāni-): PIE *gʷ > Proto-Germanic *kw by Grimm's Law, and PIE long *ē > Germanic *ē¹. Germanic in fact inherited two grades side by side — *kwenōn- (from *gʷen-ā-), which gives Old English cwene, Old High German quena, Old Norse kona 'woman, wife', and *kwēniz, which gives Old English cwēn. Nourai's spelling 'kweniz' drops the length mark on the ē that distinguishes the ancestor of queen from that of quean; the printed page shows 'kweniz', so the omission is the book's.\",\n          \"derivation_fa\": \"ژرمنی آغازین *kwēniz «زن، همسر» دنبالهٔ قاعده‌مند ستاک i-دار با درجهٔ کشیدهٔ *gʷēn-i-s است (همان که در گوتی qēns و در اوستا jāni- شده): بر پایهٔ قانون گریم، *gʷ هندواروپایی در ژرمنی به *kw بدل می‌شود. ژرمنی دو درجه را کنار هم به ارث برده است: *kwenōn- (انگلیسی کهن cwene، آلمانی علیای کهن quena) و *kwēniz (انگلیسی کهن cwēn). نورایی نشانهٔ کشش را نیاورده است؛ در متن چاپی هم همین است. در کل ادعا درست است.\",\n          \"sources\": [E_QUEEN, W_PIE_GWEN],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_GWEN + \" — the form *kwēniz and the gloss 'woman, wife, queen' are Watkins's own words; Nourai's citation is exact apart from the vowel length.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.473-474\", \"stance\": \"supports\", \"note\": \"'Gothic qino (*gʷen-ōn-) = Old English cwene, Old High German quena ... lengthened grade Gothic qēns \\\"wife\\\" (*gʷēni-s = Avestan jani-, Old Indic jani-), Old Norse kvạn, kvan, Old English cwēn, asachs. quān' — both Germanic stems.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.691 s.v. gyneco-\", \"stance\": \"supports\", \"note\": \"'... whence also OI. gnā, gānā \\\"wife of a god, goddess\\\", jániḥ \\\"wife\\\", Goth. qinō \\\"woman, wife\\\", qēns \\\"woman\\\", OE. cwēn \\\"woman, wife, queen\\\". See quean and cp. queen.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p.82-83\", \"stance\": \"supports\", \"note\": \"'Goth. qinō (and qēns \\\"wife\\\"); ON kona (gen. pl. kvinna); ... OE cwene (and cwēn \\\"wife\\\"), OHG quena.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"queen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English cwēn 'wife; female ruler of a state' > Middle English quene > Modern English queen, with the regular Great Vowel Shift raising of Middle English long ē to /iː/ (hence the modern spelling with -ee-). The semantics narrowed inside English: the oldest Germanic sense is simply 'wife', specialised to 'king's wife' already in Old English — English is one of the very few Indo-European languages whose word for 'queen' is not a feminine derivative of the word for 'king' (the Scandinavian languages share this). The doublet quean 'woman, hussy' comes from the other Germanic stem *kwenōn- (OE cwene) and shows the older, unspecialised meaning.\",\n          \"derivation_fa\": \"انگلیسی کهن cwēn «همسر؛ فرمانروای زن» > انگلیسی میانه quene > انگلیسی نو queen؛ کشیدهٔ ــــē در جریان جابه‌جایی بزرگ واکه‌ها به /iː/ بدل شد و املای ee پدید آمد. تحول معنایی درون‌زبانی است: معنای کهن‌تر ژرمنی تنها «همسر» بوده که در دورهٔ انگلیسی کهن به «همسر پادشاه» تخصیص یافته است. دوگانهٔ آن، quean، از ستاک دیگر (*kwenōn-) می‌آید و معنای عام «زن» را نگه داشته است. ادعای نورایی درست است.\",\n          \"sources\": [E_QUEEN],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent Germanic box carries AHD, whose article ends '... in Old English cwēn, woman, wife, queen: QUEEN', i.e. it covers this arrow too.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. gyneco- (p.691), cross-referring to quean/queen\", \"stance\": \"supports\", \"note\": \"'OE. cwēn, \\\"woman, wife, queen\\\". See quean and cp. queen.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (cited in Aryanpur's own reference block as 'SKEAT: (QUEAN) 491, (QUEEN) 492')\", \"stance\": \"supports\", \"note\": \"Skeat treats quean p.491 and queen p.492 as the two Germanic grades of one word, the reading Aryanpur takes over.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p.82 §2.22 table\", \"stance\": \"supports\", \"note\": \"'ME quene, wife, woman / NE woman' — Buck lists ME quene in the 'woman' column, showing the pre-specialisation sense.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"gune\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek γυνή gunḗ 'woman', gen. γυναικός gunaikós, comes from a zero-grade *gʷunā — the very shape Nourai names in his root heading 'Gwŭnâ'. The labiovelar *gʷ before the back vowel would normally give Attic β, and that outcome is preserved in the Boeotian doublet βανά baná (< *gʷenā); γυνή with γυ- reflects the assimilation of the labial element to the following u. The oblique stem γυναικ- is a Greek innovation of unclear origin (Walde-Pokorny already calls the -aik- 'unklar'); it is that stem, not the nominative, that supplies the learned combining form gynaeco-/gyneco-.\",\n          \"derivation_fa\": \"یونانی باستان γυνή (gunḗ) «زن»، با حالت اضافی γυναικός، از درجهٔ صفر *gʷunā است — همان صورتی که نورایی در سرواژه «Gwŭnâ» نوشته است. در گویش بئوتیایی همان واژه βανά است که نشان می‌دهد همخوان لبی–کامی در یونانی به β می‌دهد؛ در γυνή عنصر لبی در مجاورت u همگون شده است. ستاک غیرمستقیم γυναικ- نوآوری یونانی است و همین ستاک است که در ترکیب‌های علمی gyneco- به کار رفته است. ادعای نورایی درست است.\",\n          \"sources\": [W_PIE_GWEN, E_GYN],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed on this node. The root box's POK:473 covers it: 'gr. γυνή \\\"woman\\\" (*gʷunā), Gen. γυναικός, beside Boeotian βανά (*gʷenā)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.691 s.v. gyneco-\", \"stance\": \"supports\", \"note\": \"'Gk. γυναικο-, γυναικ-, fr. γυνή, gen. γυναικός, \\\"woman\\\", rel. to Boeotian βανά, fr. I.-E. *gʷunā, *gʷenā, \\\"woman\\\"' — both root shapes of Nourai's heading.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 681\", \"stance\": \"supports\", \"note\": \"'gr. γυνή \\\"Frau\\\" aus *gʷunā neben *gʷenu in boot. βανά ... Kasus obliqui γυναικός usw.', with the -aik- expressly left 'unklar'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p.82-83\", \"stance\": \"supports\", \"note\": \"'Grk. γυνή, gen. γυναικός, NG γυναίκα'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box: Nourai routes the English learned words through Latin without naming a Latin form. There is a genuine Latin member of the family — gynaecēum 'women's apartments', borrowed from Greek γυναικεῖον, and it is from that Latinised shape that the modern combining form gynaeco-/gyneco- is built. But the actual route of gynecology is not Latin: the word was coined in French as gynécologie and taken into English in 1847, and gyno-/gyneco- are 19th-century scientific formations directly on the Greek stem. So the box is defensible only if read as 'Neo-Latin (scientific Latin)'; as a claim about classical Latin transmission it is too strong. A French box, as Nourai himself uses in the Gwer 1 chart below for barium/barometer, would have been the right one here.\",\n          \"derivation_fa\": \"این جعبه تهی است و نورایی صورت لاتینی را نمی‌آورد. لاتین واقعاً وام‌واژهٔ gynaecēum «اندرونی زنان» را از یونانی گرفته بود و صورت ترکیبی gyneco- بر همین قالب لاتینی‌شده ساخته شده است؛ اما راه واقعی واژهٔ gynecology فرانسوی است: gynécologie در فرانسه ساخته شد و در ۱۸۴۷ به انگلیسی راه یافت. پس این جعبه فقط اگر «لاتینی نو (علمی)» خوانده شود پذیرفتنی است، و درست‌تر آن بود که مانند نمودار Gwer 1 جعبهٔ فرانسوی گذاشته می‌شد. ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [E_GYN],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on this node, and the root's POK:473 says nothing about Latin — Pokorny's article has no Latin member at all, which is itself telling.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.691, s.vv. gynaeceum and gyneco-\", \"stance\": \"partial\", \"note\": \"Klein routes only gynaeceum through Latin ('L. gynaeceum, fr. Gk. γυναικεῖον'); for the combining form he writes 'gyneco- ... — Gk. γυναικο-, γυναικ-, fr. γυνή', with no Latin stage.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷen-\", \"stance\": \"partial\", \"note\": \"Watkins lists GYNAECEUM together with GYNO-, GYNECOCRACY and (GYNECOLOGY) straight under 'Greek gunē, woman', again without a Latin node.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"gyno-, gynecology\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"gyno- and gyneco- (British gynaeco-) are learned combining forms taken from Greek γυνή / stem γυναικ-, used in English from the 19th century in botanical and medical compounds (gynandrous, -gynous, gynoecium, gynecocracy). gynecology itself is dated 1847 and is a borrowing of French gynécologie, formed on the Latinised Greek gynaeco- plus -logie; gynecologist follows in 1851 and gynecological in 1858. The semantic content is unchanged from Greek — 'woman' — with the modern narrowing to 'diseases of women' supplied by the -logy compound, not by the root.\",\n          \"derivation_fa\": \"gyno- و gyneco- صورت‌های ترکیبی علمی اند که از یونانی γυνή و ستاک γυναικ- گرفته شده و از سدهٔ نوزدهم در انگلیسی در اصطلاحات پزشکی و گیاه‌شناسی به کار رفته‌اند. خود gynecology وام‌واژهٔ فرانسوی gynécologie است که در ۱۸۴۷ به انگلیسی راه یافته (و gynecologist در ۱۸۵۱)؛ یعنی نوواژه است نه واژهٔ موروثی. از نظر معنا همان «زن» یونانی است و تخصیص پزشکی از جزء -logy می‌آید. ادعای نورایی در این گره درست است، جز آنکه واسطه فرانسوی بوده نه لاتین.\",\n          \"sources\": [E_GYN],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this node; Watkins's gʷen- article (cited on the Germanic box) ends the Greek section with 'GYNO-, -GYNOUS, -GYNY; GYNAECEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY', i.e. it lists exactly these English words under the root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.691, s.vv. gyno-, gyneco-, gynecology\", \"stance\": \"supports\", \"note\": \"'gyno-, combining form, equivalent to gyneco-. — Fr. Gk. γυνή, \\\"woman\\\"'; 'gynecology, gynaecology, n., the study of diseases peculiar to women. — Compounded of gyneco- and Gk. -λογία'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷen-\", \"stance\": \"supports\", \"note\": \"'3. Suffixed zero-grade form *gʷn-ā- in Greek gunē, woman: GYNO-, -GYNOUS, -GYNY; GYNAECEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Gwer 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷerh₂- / adj. *gʷréh₂us 'heavy' (Pokorny 'gʷer-2, gʷerə-, gʷerəu-, gʷerī-', pp. 476-477)\",\n      \"verdict_note\": \"\",\n      \"note\": \"Root form, language label, gloss and page all check out: Pokorny's second gʷer- lemma, headed 'Meaning: heavy', occupies pp.476-477, and Watkins numbers it 'gʷerə-2. Heavy. [Pok. 2. gʷer- 476.]'. What makes this chart unusually solid is that Pokorny's article itself, in the space of six lines, names four of the chart's five branches in Nourai's own order — 'Avestan gouru- (in compound) \\\"heavy\\\"; npers. giran \\\"heavy\\\" (*grāna-); gr. βαρύς \\\"heavy\\\", βάρος n. \\\"heaviness\\\"; Latin gravis \\\"heavy, weighty\\\" (*gʷra-u-is)' — so the Avestan→Persian and the Greek and Latin boxes are not Nourai's inference but Pokorny's text. The Iranian link is independently confirmed by Horn no. 898, by Mo'in's footnote on the very Borhān page Nourai cites (BQT:1781), and by Aryanpur, who reconstructs the same chain (Av. gouru/garu → OPers. *grāna → Pahl. garān → گران). The only qualification worth making is chronological rather than etymological: the Persian and English boxes at the bottom right hold 19th-century coinages (barium 1808, barometer 1660s) that reached Persian through French, which the chart in fact draws correctly.\",\n      \"note_fa\": \"ریشه، برچسب زبان، معنا و شمارهٔ صفحه همه درست است: مادهٔ دوم gʷer- در پوکورنی با معنای «سنگین» در صفحات ۴۷۶–۴۷۷ آمده و واتکینز نیز آن را «gʷerə-2. Heavy» می‌نامد. نکتهٔ جالب آنکه متن پوکورنی در شش سطر چهار شاخه از پنج شاخهٔ نمودار را به همین ترتیب می‌آورد: «اوستایی gouru- ، فارسی نو giran (*grāna-)، یونانی βαρύς و βάρος، لاتین gravis». زنجیرهٔ ایرانی را هرن (شمارهٔ ۸۹۸)، حاشیهٔ معین بر همان صفحهٔ برهان قاطع (۱۷۸۱) و آریان‌پور نیز تأیید می‌کنند: اوستا gouru/garu ← پارسی باستان *grāna ← پهلوی garān ← «گران». تنها یادآوری تاریخی لازم است: «باریم» و «بارومتر» نوواژه‌های سدهٔ نوزدهم اند که از راه فرانسه به فارسی آمده‌اند — و نمودار هم دقیقاً همین را رسم کرده است.\",\n      \"sources\": [W_GERAN, E_BARIUM, E_BAROM, E_GRIEF],\n      \"ref_check\": [\n        {\"ref\": \"POK:476\", \"status\": \"supports\", \"note\": POK476}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 684-685 (WLD_Bd1_pages.txt lines 64816-64855, running head 'gʷer-')\", \"stance\": \"supports\",\n         \"note\": \"'3. gʷer- „schwer“ ... Ai. guru-h „schwer, wichtig, ehrwürdig“ ... av. gouru-zaoθra- „des Weihegusse schwer, zähflüssig sind“; np. giran „schwer“ (*grāna-, kein Beleg für die Hochstufe ... sondern Umbildung etwa nach *frāna- „voll“) ... Gr. βαρύς „schwer“, βάρος „Schwere“ ... lat. gravis „schwer, gewichtig“ (*gʷra-u-is)' — the whole chart in one paragraph, with the Persian form's morphology explained.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-2 (AHD_watkins1985.txt line 542)\", \"stance\": \"supports\", \"note\": AHD_GWER},\n        {\"src\": \"ARY\", \"where\": \"Aryanpur, entry گران (ARY_latin_index_pages.txt pdf page 425 = printed 426)\", \"stance\": \"supports\",\n         \"note\": \"Cognate list: 'GOURO, GARU (AVESTAN) – *GRANA (OLD PERSIAN) – GARAN (PAHLAVI) – GHIRAN, GIRAN (KURDISH) – GUROH, GURUS (SANSKRIT) – BARYS, BAROS (GREEK) – GRAVIS (LATIN) – GRAVE (FRENCH/ENGLISH/SPANISH/ITALIAN) – KAURUS (GOTHIC)', references 'POKORNY 476 ... SKEAT: (GRAVE) 248 ... MACKENZIE: (HEAVY) 117' — an independent Persian handbook reproducing Nourai's tree.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gouru\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan gouru- 'heavy' is real but attested only as the first member of a compound, gouru.zaoθra- (Yt.10.113), which Bartholomae glosses 'des… Weihgüsse schwer, zähflüssig sind' — 'whose libations are heavy, viscous'. The form is the u-stem adjective *gʷrə-u- (= Sanskrit gurú-, Greek barú-s): syllabic *ṛ before the -u- suffix gives Avestan ərə > ou in this position, so the real reading is roughly garū-/gərū- (Horn writes 'aw. gouru- (d.i. garū-)'). Klein makes the same reservation — 'Avestic gouru- (only in compounds), \\\"heavy, weighty\\\"'. Nourai's box is therefore correct but slightly flatters the evidence by presenting a bound compound-form as a free word.\",\n          \"derivation_fa\": \"صورت اوستایی gouru- «سنگین» واقعی است، اما تنها در جزء نخست رکیب gouru.zaoθra- (یشت ۱۰، بند ۱۱۳) به کار رفته و بارتولمه آن را «کسی که زوهرهٔ او سنگین و غلیظ است» معنا کرده است. این صفت ستاک u-دار *gʷrə-u- است (= سنسکریت gurú-، یونانی barús)؛ روان‌خوانی واقعی آن تقریباً garū- است، چنانکه هرن می‌نویسد «aw. gouru- (d.i. garū-)». پس جعبه درست است، جز آنکه صورتی مقید به ترکیب را واژهٔ آزاد نشان داده است.\",\n          \"sources\": [W_GERAN],\n          \"ref_check\": [\n            {\"ref\": \"POK:476\", \"status\": \"supports\", \"note\": \"Pokorny p.476: 'Avestan gouru- (in compound) \\\"heavy\\\"' — with the same parenthetical caution about its being a compound form (POK_full.txt line 39528).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch, s.v. gouru.zaoθra- (BRT.txt line 10386)\", \"stance\": \"supports\",\n             \"note\": \"'j. gouru.zaoθra- Adj. (mask. °ra-) \\\"des… Weihgüsse schwer, zähflüssig sind\\\" ... Yt.10.113' — the only attestation; there is no free-standing gouru- headword in Bartholomae.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 898, p.200\", \"stance\": \"supports\", \"note\": \"'Vergl. aw. gouru- (d. i. garū-) in gouru.zaoθra- \\\"unlustiger Opferer\\\" (Geldner); phlv. garān \\\"schwer\\\"; ai. gurú- \\\"schwer\\\".'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grave, adj.\", \"stance\": \"supports\", \"note\": \"'L. gravis ... cogn. with OI. guruḥ \\\"heavy, weighty\\\" ... Avestic gouru- (only in compounds), \\\"heavy, weighty\\\", Gk. βάρος, βαρύς ... Goth. kaurus.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gerân «گران»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian گران gerān / girān 'heavy; expensive' continues Middle Persian garān (Book Pahlavi gl'n'), from Old Iranian *grāna- — the zero-grade *gʷṛh₂- of this root with the adjectival suffix -na-. Pokorny and Walde-Pokorny both remark that the long ā is not an inherited full grade but an analogical remodelling on *frāna- 'full' (NP پر، فراوان), a neat instance of one adjective being re-cut on the pattern of its antonym-partner. Mo'in's footnote on the very page Nourai cites gives the same chain — 'Pahlavi garān (سنگین، ثقیل), from Avestan gouru- from garu-; Old Persian *garu-; Kurdish girān' — and Horn no.898 adds the Kashan dialect forms gerūn, gurūn, gurō. The sense 'expensive' is a Persian development from 'heavy' via 'weighty, burdensome (to the purse)', already opposed to ارزان in the Borhān entry; Hāfez's line quoted in the chart uses the older concrete sense, 'بار گران' = 'heavy load'.\",\n          \"derivation_fa\": \"«گران» در فارسی نو دنبالهٔ garān فارسی میانه (پهلوی gl'n') است، از ایرانی باستان *grāna- که درجهٔ صفر ریشه به‌علاوهٔ پسوند صفت‌ساز -na- است. پوکورنی و والده–پوکورنی هر دو یادآور می‌شوند که ـــāــ کشیده درجهٔ افزودهٔ موروثی نیست بلکه به قیاس *frāna- «پر، فراوان» بازساخته شده است. حاشیهٔ معین بر همان صفحهٔ برهان قاطع (۱۷۸۱) همین زنجیره را می‌دهد و هرن (شمارهٔ ۸۹۸) گونه‌های کاشانی gerūn و gurūn را می‌افزاید. معنای «گران‌بها» تحولی فارسی است از «سنگین»، و در بیت حافظ که نورایی آورده («بار گران») هنوز معنای عینی قدیم به کار رفته است. ادعای نورایی درست است.\",\n          \"sources\": [W_GERAN],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1781\", \"status\": \"supports\", \"note\": BQT1781},\n            {\"ref\": \"MON:3214\", \"status\": \"partial\", \"note\": \"The six-volume Mo'in is not digitised, so p.3214 itself could not be opened; the two-volume Adena condensation carries the entry (MON_part2.txt line 30351): 'گران: [‎په.] (ص.) ثقیل، وزین؛ مق. سبک، خفیف. سخت؛ شدید. بزرگ، عظیم. آنچه قیمتش به نسبت اشیای دیگر زیاد باشد؛ مق. ارزان' — the gloss 'heavy, expensive' of the chart, with an origin bracket (the OCR of the bracket is corrupt, but Mo'in's tag for this word is the Pahlavi one). Content supported, page number unchecked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie, no. 898, p.200\", \"stance\": \"supports\",\n             \"note\": \"'898. girān \\\"schwer\\\". Kāš. gerūn, gurūn, gurō. Vergl. aw. gouru- (d. i. garū-) in gouru.zaoθra- ...; phlv. garān \\\"schwer\\\"; ai. gurú- \\\"schwer\\\" ... Die Grundform hatte einen r-Vokal.' — the whole node, with the Pahlavi stage.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §188 (HUB.txt line 8806) and § on epenthesis (line 6066)\", \"stance\": \"supports\",\n             \"note\": \"'girān \\\"schwer\\\" H. 898' among the words with ap. g > np. g; and, under the insertion of i in initial clusters, 'girān \\\"schwer\\\", afgh. LW. grān' — i.e. NP girān from a cluster *gr-, exactly the *grāna- Pokorny posits.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (cited by Aryanpur as 'MACKENZIE: (HEAVY) 117')\", \"stance\": \"supports\",\n             \"note\": \"MacKenzie's entry garān [gl'n'] 'heavy, grievous' is the Middle Persian link; the local OCR of PHD is broken in the g- stretch, so this is taken from Aryanpur's page reference to MacKenzie.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, entry گران, printed p.426\", \"stance\": \"supports\",\n             \"note\": \"'GOURO, GARU (AVESTAN) – *GRANA (OLD PERSIAN) – GARAN (PAHLAVI) – GHIRAN, GIRAN (KURDISH)' — the same descent, with the Old Iranian *grāna- spelled out.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"gravis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin gravis 'heavy, weighty, burdensome; serious' goes back to *gʷrə-u-is, the same u-stem adjective as Avestan gouru- and Greek barús but recharacterised with the i-stem ending: PIE *gʷ before r gives Latin gr- (via *gʷr > gr), and the syllabic laryngeal-coloured *ə is lost. The doublet brūtus 'heavy, dull' preserves the b- outcome and is an Oscan-Umbrian loan into Latin, which is why the two forms differ. The sense range 'heavy → grievous → serious, dignified' is already fully developed in classical Latin (gravitas).\",\n          \"derivation_fa\": \"لاتین gravis «سنگین، گران، جدی» از *gʷrə-u-is است، یعنی همان صفت ستاک u-داری که در اوستا gouru- و در یونانی barús شده، منتها با پایانهٔ i-دار بازساخته. همخوان لبی–کامی *gʷ پیش از r در لاتین gr- می‌دهد. دوگانهٔ آن، brūtus «سنگین، کند‌ذهن»، وام‌واژه‌ای اسکی–امبریایی است که برون‌داد b- را نگه داشته است. گسترهٔ معنایی «سنگین ← طاقت‌فرسا ← جدی و موقر» در خود لاتین کلاسیک کامل شده است. ادعای نورایی درست است.\",\n          \"sources\": [E_GRIEF],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985: 'I. Zero-grade form *gʷrə-. 1. Suffixed form *gʷrə-u-i- in Latin gravis, heavy, weighty: GRAVE2, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE.' — the node and its English children in one line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.476\", \"stance\": \"supports\", \"note\": \"'Latin gravis \\\"heavy, weighty\\\" (*gʷra-u-is)'; and, for the doublet, 'Latvian grūts \\\"heavy\\\" = Latin brutus (Oscan-Umbrian loanword) \\\"heavy, clumsy, insensible\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grave, adj., weighty\", \"stance\": \"supports\", \"note\": \"'F., fr. L. gravis, \\\"heavy, weighty; troublesome, painful, grievous, hard; important, honorable\\\", which is cogn. with OI. guruḥ ... Avestic gouru- ... Gk. βάρος ... Goth. kaurus, Lett. grūts. Cp. gravedo, gravid, gravity, grief, grieve, grievous, aggravate.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 685\", \"stance\": \"supports\", \"note\": \"'lat. gravis „schwer, gewichtig“ (*gʷra-u-is; vgl. oben ai. gari-man-)'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"grave : serious ; gravity, grief\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Latin words that reached English through French. grave (adj.) 'weighty, serious', c.1300, is Old French grevos / French grave from Latin gravis — a different word from the noun grave 'burial place', which is Germanic (OE græf) and only a homograph. gravity is French gravité from Latin gravitātem (acc. of gravitās 'weight, seriousness'), the physical sense of the English word being a 17th-century scientific specialisation of 'heaviness'. grief, early 13c., is Old French grief 'wrong, grievance, misfortune' from Latin gravare 'to make heavy, burden, cause grief' (whence also grieve, c.1300, from OF grever); the semantic path is 'weight → burden → affliction → sorrow'. Watkins lists GRAVE2, GRAVITY-family and (GRIEF), GRIEVE under this root together.\",\n          \"derivation_fa\": \"هر سه واژه لاتینی اند که از راه فرانسه به انگلیسی رسیده‌اند. grave «جدی، موقر» (حدود ۱۳۰۰ م.) از فرانسهٔ کهن grevos و لاتین gravis است — و با grave «گور» که ژرمنی است (انگلیسی کهن græf) تنها هم‌نگاشت است نه هم‌ریشه. gravity از فرانسهٔ gravité و لاتین gravitātem «سنگینی، وقار» است که معنای فیزیکی آن تخصیصی سدهٔ هفدهم است. grief (اوایل سدهٔ ۱۳م.) از فرانسهٔ کهن grief و لاتین gravare «سنگین کردن، بار نهادن» است و تحول معنایی آن «سنگینی ← بار ← رنج ← اندوه» است. واتکینز هم هر سه را ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [E_GRIEF],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this node; the parent Latin box carries AHD, whose gʷerə-2 article names GRAVE2, GRAVID, (GRIEF), GRIEVE, AGGRAVATE and AGGRIEVE as the English outcomes of gravis.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. grave (adj.), gravity\", \"stance\": \"supports\", \"note\": \"'gravity, n. — F. gravité, fr. L. gravitatem, acc. of gravitas, \\\"weight, seriousness\\\", fr. L. gravis, \\\"heavy\\\". See grave, \\\"weighty\\\", and -ity.' Klein's grave (adj.) article expressly lists 'gravity, grief, grieve, grievous' as cognates and keeps the noun grave 'burial place' separate.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-2\", \"stance\": \"supports\", \"note\": \"'Latin gravis, heavy, weighty: GRAVE2, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat (cited by Aryanpur as 'SKEAT: (GRAVE) 248')\", \"stance\": \"supports\", \"note\": \"Skeat p.248 treats grave 'weighty' as the French/Latin word, distinct from the Germanic grave 'trench, tomb'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"barus : heavy ; baros : weight\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek βαρύς barús 'heavy' is the u-stem *gʷrə-u- (exactly cognate with Sanskrit gurú- and Avestan gouru-), and βάρος báros 'weight' the s-stem *gʷrə-es-. The initial β is the regular Greek outcome of the voiced labiovelar *gʷ before a non-front vowel (the same change that gives βανά beside γυνή in the chart above), and the syllabic *ṛə gives αρ. Both nouns are Homeric and both feed the modern scientific vocabulary — barús the mineral name baryte/barium, báros the measuring words bar, baro-, isobar, barometer.\",\n          \"derivation_fa\": \"یونانی βαρύς (barús) «سنگین» همان ستاک u-دار *gʷrə-u- است (دقیقاً هم‌ریشهٔ سنسکریت gurú- و اوستایی gouru-) و βάρος (báros) «وزن» ستاک s-دار *gʷrə-es-. واک آغازین β برون‌داد قاعده‌مند *gʷ پیش از واکهٔ غیرپیشین است — همان دگرگونی که βανά را در برابر γυνή نمودار بالا پدید آورده است. هر دو واژه هومری اند و هر دو پایهٔ اصطلاحات علمی نو شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [E_BARIUM, E_BAROM],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985: '2. Suffixed form *gʷrə-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA ... 3. Suffixed form *gʷrə-es- in Greek baros, weight: BAR2, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR.' Both words, both suffixes, and the modern derivatives.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.476\", \"stance\": \"supports\", \"note\": \"'gr. βαρύς \\\"heavy\\\", βαρύνω \\\"beschwere\\\", βάρος n. \\\"heaviness\\\"', with the note on the labiovelar outcome b-.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Briareus and s.v. grave (adj.)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *gʷer-, \\\"heavy\\\", whence also Gk. βαρύς, L. gravis, \\\"heavy\\\". See grave, adj., and cp. baro-.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 685\", \"stance\": \"supports\", \"note\": \"'Gr. βαρύς „schwer“, βαρύνω „beschwere“, βαρύθω „bin beschwert“, βάρος „Schwere“'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box, and here it is the right one: the Persian words in the next box are French loans. French coined baryum (Davy's barium naturalised) and baro-/baromètre on the Greek stems βαρύς / βάρος, and 19th- and early 20th-century Persian took its chemical and instrument vocabulary overwhelmingly from French, through the Dār al-Fonūn curriculum and French-trained physicians. Mo'in tags بارومتر '[فر.]' — French — which is precisely this box.\",\n          \"derivation_fa\": \"جعبهٔ تهی واسطه است و این‌بار درست نهاده شده: واژه‌های فارسی جعبهٔ بعدی وام‌واژهٔ فرانسوی اند. فرانسه بر پایهٔ ستاک‌های یونانی βαρύς و βάρος واژه‌های baryum و baromètre را ساخت، و فارسی در سدهٔ سیزدهم و چهاردهم خورشیدی واژگان شیمی و ابزارهای علمی را عمدتاً از فرانسه وام گرفت (از راه دارالفنون و پزشکان فرنگ‌آموخته). معین نیز ذیل «بارومتر» نشانهٔ [فر.] را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [V_BAROM, E_BAROM],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed on this box; its content is carried by the MON:451,452 citation on the Persian box below, where Mo'in's origin tag is '[فر.]' (French).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi, s.v. بارومتر (read through vajehyab)\", \"stance\": \"supports\", \"note\": \"'(رُ مِ) [فر.] (اِ.) اسبابی برای اندازه‌گیری فشار جو، فشارسنج هوا' — the bracket [فر.] is Mo'in's own tag for a French loan.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, entry گران, printed p.426\", \"stance\": \"partial\", \"note\": \"Aryanpur lists 'GRAVE (FRENCH)' in the same cognate block, i.e. he recognises the French branch of this root, though he does not track the Persian scientific loans.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"باریم ، بارومتر\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"باریم bārium and بارومتر bārometr are modern Persian loans from French baryum and baromètre, not inherited words — note that they keep the European bār- rather than showing the inherited Iranian treatment of the root, which in Persian is گران in the box above; the chart is thus quietly displaying a doublet, one word inherited and one re-imported from the same PIE root two and a half millennia later. Mo'in prints بارومتر with the tag [فر.] 'French' and the gloss 'اسبابی برای اندازه‌گیری فشار جو، فشارسنج هوا' beside the calque میزان‌الهواء and the Persian هواسنج. The transliteration of the French ‑eu‑/‑y‑ of baryum as Persian ــیــ is the usual treatment.\",\n          \"derivation_fa\": \"«باریم» و «بارومتر» وام‌واژه‌های تازهٔ فارسی از فرانسهٔ baryum و baromètre اند و موروثی نیستند؛ گواه آن همین آغازهٔ bār- است که برون‌داد یونانی–اروپایی ریشه است، در حالی که برون‌داد ایرانی همین ریشه در فارسی «گران» است. پس نمودار در واقع یک دوگانه (doublet) را نشان می‌دهد: یک واژهٔ موروثی و یک واژهٔ بازوام‌گرفته از همان ریشه پس از دو هزاروپانصد سال. معین ذیل «بارومتر» نشانهٔ [فر.] و معنای «فشارسنج هوا» را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [V_BAROM, E_BARIUM, E_BAROM],\n          \"ref_check\": [\n            {\"ref\": \"MON:451,452\", \"status\": \"supports\", \"note\": \"Mo'in's بارومتر entry, read through vajehyab: '(رُ مِ) [فر.] (اِ.) اسبابی برای اندازه گیری فشار جو، فشارسنج هوا، فشار-سنج'; the local two-volume condensation has it too (MON_part1.txt line 20212: 'بارومتر: ... میزان الهواء، هواسنج'), directly after بارور and before بارون — i.e. exactly where pp.451-452 of the six-volume edition fall. باریم appears in the condensation only inside chemical entries ('سولفات باریم', MON_part1.txt lines 81383, 81392), the six-volume page itself not being digitised.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in via vajehyab, s.v. بارومتر\", \"stance\": \"supports\", \"note\": \"Origin tag '[فر.]' = French, exactly the route Nourai draws (Greek → French → Persian).\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, entry گران, printed p.426\", \"stance\": \"silent\", \"note\": \"Aryanpur's entry lists only the inherited Iranian and European reflexes of the root and says nothing about the modern Persian loans باریم / بارومتر.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"barium, barometer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are modern scientific coinages on Greek material, correctly hung under the Greek box. barium was coined in Modern Latin in 1808 by its discoverer Sir Humphry Davy, on the mineral name barytes, which Lavoisier had built on Greek barús 'heavy' (an irony Davy noted, since the metal itself is light). barometer, 1660s, was coined — or at least made current — by Robert Boyle from Greek báros 'weight' + -metron 'measure', for Torricelli's 1643 instrument, which until then had been called the 'Torricellian tube'. So the two words come from the two different Greek stems in the parent box, barú- and báros, which is why Nourai lists both there.\",\n          \"derivation_fa\": \"هر دو نوواژهٔ علمی اند که از مادهٔ یونانی ساخته شده‌اند. barium را در ۱۸۰۸ همفری دیوی، کاشف آن، در لاتینی نو بر پایهٔ نام کانی barytes ساخت که لاوازیه آن را از یونانی barús «سنگین» گرفته بود. barometer در دههٔ ۱۶۶۰ به دست رابرت بویل از báros «وزن» + -metron «اندازه» ساخته شد، برای ابزاری که توریچلی در ۱۶۴۳ ساخته بود. پس هر یک از دو واژه از یکی از دو ستاک یونانی جعبهٔ مادر است و همین سبب آوردن هر دو صورت در آن جعبه بوده است. ادعای نورایی درست است.\",\n          \"sources\": [E_BARIUM, E_BAROM],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this node; the parent Greek box's AHD citation lists (BARIUM) under barus and BAR2, BARO- under baros, covering both words.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-2\", \"stance\": \"supports\", \"note\": \"'Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA' and 'Greek baros, weight: BAR2, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR' — barometer belongs to the BARO- group.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. baro- (cross-referenced from grave, adj. and Briareus)\", \"stance\": \"supports\", \"note\": \"Klein's grave (adj.) article ends 'Cp. also baro-, bary-, Briareus, brute, centrobaric, charivari, garce, guru, isobar', grouping the barium/barometer family with gravis under one base *gʷer-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nfor e in data[\"entries\"]:\n    e.pop(\"verdict_note\", None)\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-208.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk208.py",
 "description": "Write page-208 verification JSON"
}
```


### [2026-09-06T15:11:42.271Z] TOOL RESULT

```
written
```


## [2026-09-06T15:11:45.930Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-208.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 208",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T15:11:47.921Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 2, 'not_checked': 7}
books consulted: {'supports': 37, 'partial': 6, 'contradicts': 1, 'silent': 1} | by book: {'KLN': 10, 'AHD': 6, 'WLD': 5, 'SYN': 5, 'ARY': 4, 'POK': 3, 'BRT': 2, 'HUB': 2, 'PHD': 2, 'SKT': 2, 'HRN': 2, 'MON': 2}
```


## [2026-09-06T15:11:53.245Z] TOOL CALL #72: Bash

```json
{
 "command": "grep -o \"ǟ[a-zA-Zāī-]*\" data/verification/page-208.json | sort | uniq -c; grep -o \"ǵ[a-zA-Zāī-]*\" data/verification/page-208.json | sort | uniq -c; grep -c \"Ǟ\" data/verification/page-208.json",
 "description": "Find stray characters in JSON"
}
```


### [2026-09-06T15:11:53.346Z] TOOL RESULT

```
      5 ǟ
      1 ǟaini
      6 ǟaini-
      1 ǟan-
      4 ǟanay-
      1 ǟni-
      3 ǵ
      2 ǵani-
4
```


## [2026-09-06T15:12:01.734Z] TOOL CALL #73: Bash

```json
{
 "command": "grep -o \"ǟ[^ ,\\\"]*\\|Ǟ[^ ,\\\"]*\\|ǵ[^ ,\\\"]*\" data/verification/page-208.json | sort | uniq -c",
 "description": "List all stray char contexts"
}
```


### [2026-09-06T15:12:01.782Z] TOOL RESULT

```
      1 ǟ
      3 Ǟ
      1 Ǟ-
      5 ǟaini-
      1 ǟaini-.
      1 ǟainiš
      1 ǟan-
      3 ǟanay-
      1 ǟanay-،
      1 ǟ/j
      1 ǟni-/jāni-
      3 ǟẗnay-
      2 ǵ
      2 ǵani-
      1 ǵáni-
```


## [2026-09-06T15:12:07.362Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/page-208.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('ǟẗnay-','ǰə̄nay-')\ns=s.replace('ǟni-/jāni-','ǰāni-/jąni-')\ns=s.replace('ǟ/j','ǰ/j')\ns=s.replace('ǟ','ǰ').replace('Ǟ','ǰ')\ns=s.replace('*ǵani-','*ǰani-')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\ngrep -o \"ǟ\\|Ǟ\" data/verification/page-208.json | wc -l; grep -o \"ǰ[^ ,\\\"]*\\|ǵ[^ ,\\\"]*\" data/verification/page-208.json | sort | uniq -c; python3 -m json.tool data/verification/page-208.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 208",
 "description": "Fix stray characters and revalidate"
}
```


### [2026-09-06T15:12:09.896Z] TOOL RESULT

```
0
      2 ǵ
      1 ǵáni-
      4 ǰ
      1 ǰ-
      5 ǰaini-
      1 ǰaini-.
      1 ǰainiš
      1 ǰan-
      3 ǰanay-
      1 ǰanay-،
      2 ǰani-
      1 ǰāni-/jąni-
      3 ǰə̄nay-
      1 ǰ/j
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 2, 'not_checked': 7}
books consulted: {'supports': 37, 'partial': 6, 'contradicts': 1, 'silent': 1} | by book: {'KLN': 10, 'AHD': 6, 'WLD': 5, 'SYN': 5, 'ARY': 4, 'POK': 3, 'BRT': 2, 'HUB': 2, 'PHD': 2, 'SKT': 2, 'HRN': 2, 'MON': 2}
```


## [2026-09-06T15:12:27.493Z] AGENT

Page 208 (book p.178) verified; `verify_check.py 208` reports **0 PROBLEM lines** (16/16 nodes).

**Counts** — roots: 2 confirmed. Nodes: 14 confirmed, 1 plausible, 1 disputed.
Ref checks: 10 supports, 2 partial, 7 not_checked (nodes Nourai left without refs). Books consulted: 45 entries across POK, WLD, AHD, KLN, SYN(Buck), BRT, HRN, HUB, PHD, SKT, MON, ARY.

**Flagged items**
- **disputed** — Gwen 1, node #3 [Sanskrit] `gnâ, gunâ, jani, kan, kanya`: gnā/jáni- are genuine, but `kan, kanya` belong to PIE *ken- "fresh, young" (Av. kainiiā, MP kanīg → NP کنیز), not *gʷen- — a Sanskrit k- cannot come from *gʷ. `gunâ` is not a Sanskrit word (the forms are gnā/gánā); the printed page does read "gunâ", so `error_in: book`, apparently *gʷunā (his own root heading "Gwŭnâ") misfiled under Sanskrit.
- **plausible** — Gwen 1, node #7 [Latin] (empty pass-through to gyno-/gynecology): gynecology is 1847 from French *gynécologie*; Klein and Watkins route the combining form straight from Greek, with Latin only for *gynaeceum*. A French box would have been correct — as Nourai himself uses in the Gwer 1 chart.

**No extraction errors** — the JSON matches the printed page exactly (checked against `site/pages/208.jpg`, copy saved at `data/verification/sources/refs/ocr/BOOK/208.png`), including "žaini" (Nourai's own slip for ǰaini-) and "kweniz" (for *kwēniz).

**Notable positives**: Nourai's own citations check out unusually well — POK:473 and POK:476 reproduce his root boxes almost verbatim; SYN:82 really is Buck's "2.22 WOMAN" table (running head confirms p.82) with "Av. jaini- (NPers. zan)"; BQT:1781 (fetched via `ref_page.py`, v3 pdf p.578) is the گران article whose Mo'in footnote gives Pahlavi garān ← Av. gouru- ← garu-, matching the arrow exactly; BQT:1033 is the زن article (BQT_v2 leaf 496) with the same Avestan→Pahlavi footnote. Aryanpur independently cites the same Pokorny and Buck pages for زن.
