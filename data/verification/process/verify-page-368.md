# Verification process log — verify-page-368


## [2026-09-07T19:29:23.099Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 368 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-368.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-368.json. Write /home/sfmqrb/git/rishe/data/verification/page-368.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 368` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:25.616Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T19:29:26.328Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:26.338Z] TOOL RESULT

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


## [2026-09-07T19:29:26.866Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-368.txt"
}
```


### [2026-09-07T19:29:26.915Z] TOOL RESULT

```
1	=== PDF page 368 (book page 338) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nôğ, Snôğ : whim, triviality, fancy  (refs IEC:848, 1236)
4	#1 (parent #0) [Old Iranian] refs=FFD:77 | nâz : happiness, pride
5	  #2 (parent #1) [Pahlavi] refs=FFD:77 | nâz : to be happy, mince ; nâčuk : delicate
6	    #3 (parent #2) [Persian] refs=FFD:77; HRN:228 | nâz «ناز» : affected manners, pride ; nâzok «نازک» : thin, delicate | extra: نازیدن ، نازنین
7	#4 (parent #0) [Greek] refs=IEC:848,1236 | nôgla : snacks
8	  #5 (parent #4) [Latin] refs=IEC:848,1236 | nŭgae, nôgae : trifles
9	--- entry 1 ---
10	ROOT [Indo-European] Nogh, Onogh : nail  (refs POK:780)
11	#1 (parent #0) [Sanskrit] refs=POK:780; SNS:258 | nakhâ, naxâ : nail
12	  #2 (parent #1) [Pahlavi] refs=SNS:258; HRN:228 | nâxun : nail
13	    #3 (parent #2) [Persian] refs=POK:780; BQT:2089; SYN:245; KLN:1028 | nâxon «ناخن» : nail
14	#4 (parent #0) [Germanic] refs=AHD | nagla : nail
15	  #5 (parent #4) [English] refs=None | nail
16	
```


## [2026-09-07T19:29:29.692Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-368.json",
 "description": "Read source JSON for page 368"
}
```


### [2026-09-07T19:29:29.731Z] TOOL RESULT

```
{
  "pdf_page": 368,
  "book_page": 338,
  "entries": [
    {
      "root": {
        "name": "Nôğ, Snôğ",
        "lang": "Indo-European",
        "refs": "IEC:848, 1236",
        "gloss": "whim, triviality, fancy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Iranian",
          "refs": "FFD:77",
          "words": [
            {"translit": "nâz", "gloss": "happiness, pride", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:77",
          "words": [
            {"translit": "nâz", "gloss": "to be happy, mince", "script": null},
            {"translit": "nâčuk", "gloss": "delicate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FFD:77; HRN:228",
          "words": [
            {"translit": "nâz", "gloss": "affected manners, pride", "script": "ناز"},
            {"translit": "nâzok", "gloss": "thin, delicate", "script": "نازک"}
          ],
          "script_extra": "نازیدن ، نازنین",
          "note": null,
          "quote": {
            "text": "نازی که داشتم به پدر چون عزیز مصر - در غربت این زمان ز خریدار میکشم",
            "poet": "Sâeb"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:848,1236",
          "words": [
            {"translit": "nôgla", "gloss": "snacks", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "IEC:848,1236",
          "words": [
            {"translit": "nŭgae, nôgae", "gloss": "trifles", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nogh, Onogh",
        "lang": "Indo-European",
        "refs": "POK:780",
        "gloss": "nail"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:780; SNS:258",
          "words": [
            {"translit": "nakhâ, naxâ", "gloss": "nail", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:258; HRN:228",
          "words": [
            {"translit": "nâxun", "gloss": "nail", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:780; BQT:2089; SYN:245; KLN:1028",
          "words": [
            {"translit": "nâxon", "gloss": "nail", "script": "ناخن"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "nagla", "gloss": "nail", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nail", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:31.558Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','POK','SNS','HRN','BQT','SYN','KLN','AHD','FFD','WLD','MON','PHD','NYB','ARY','SKT','WEB','FSD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Look up reference metadata"
}
```


### [2026-09-07T19:29:32.850Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
```


## [2026-09-07T19:29:52.710Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/page-316.json'))\ne=d['entries'][0]\nprint(json.dumps(e,ensure_ascii=False,indent=1)[:3000])\n\""
}
```


## [2026-09-07T19:29:53.291Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T19:29:54.096Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دانند و چنین معنایی نمی‌دهند (ویکی‌واژه دیدگاهی اقلیتی را گزارش می‌کند که *méh₂- را ریشهٔ فعلی «شیر دادن، مادری کردن» می‌گیرد). در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های پایین‌دست درست اند؛ تنها خطای جدی این صفحه در گرهٔ ۸ («ممه») است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r",
  "https://www.etymonline.com/word/mother"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny 694 is 'mā-3, Meaning: mother (expr. root), Note: redupl. māmā, māmmā ... Material: Old Indic mā ‘mother’ ... npers. mām, māmā, māmī ‘mother’ ... Latin mamma ... mamilla ‘nipple’ ... Page(s): 694' (POK_full.txt l.57758ff, grep 'lemma: mah 3'). It therefore supports the Mā- half of the root box, but glosses it ‘mother’, not ‘breast’; Pokorny's separate lemma 'mahter-, Meaning: mother, Note: based on a babble-word mah-, see there ... Page(s): 700-701' is where Mā-ter belongs, i.e. p.700-701 and
```


### [2026-09-07T19:29:54.131Z] TOOL RESULT

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


## [2026-09-07T19:30:01.962Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full grep nogh ===\"\ngrep -n -i -E \"lemma: .*nogh|lemma: .*onogh\" POK_full.txt | head -20\necho \"=== POK_02 leaf 436 (p780) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==437' POK_02.txt | head -60"
}
```


### [2026-09-07T19:30:03.296Z] TOOL RESULT

```
=== POK_full grep nogh ===
63942:Root / lemma: onogh-{. ongh-, nogh-, Ce\^\c Qgh^, ongh-li-{* huen(e)gh-) 
63975:Note: alb. thoi, thua, pi. thonj^ nail ' : alb. thengjiir {*co3\) ash'; Root/ lemma: onogh-{: 
=== POK_02 leaf 436 (p780) ===
```


## [2026-09-07T19:30:03.782Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 439 (p848) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==440' IEC.txt | grep -n -i -E \"nog|snog|nug\" | head -30\necho \"=== IEC grep nogal/nugae ===\"\ngrep -n -i -E \"nogal|nugae|nūgae|snōg|nōg-\" IEC.txt | head -30"
}
```


### [2026-09-07T19:30:05.061Z] TOOL RESULT

```
=== IEC leaf 439 (p848) ===
=== IEC grep nogal/nugae ===
16581:snóg-, possible variant of type no$-, q.v. Per. & Gk. ambig. Per. naz, s. ‘flirtation’; nazam, -1dan, v. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’; OE cf. snóca, wm. (queried: ‘nook’, but E snook = “a rude gesture"). (Lat. nugae ‘trifles’ here only if dia- lectal for *nogae)
```


## [2026-09-07T19:30:13.492Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'snóg-, possible variant' in l:\n        print('leaf idx (0-based)',i,'-> printed pages approx', (i-15)*2, (i-15)*2+1)\n        print(l[:2500])\n        break\nEOF"
}
```


## [2026-09-07T19:30:14.398Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"^nog-|nog-, \" IEC.txt | head -20\necho \"=== nog- context ===\"\ngrep -n -i -E \"nog-\" IEC.txt | head -30"
}
```


### [2026-09-07T19:30:14.774Z] TOOL RESULT

```
leaf idx (0-based) 682 -> printed pages approx 1334 1335
 beside nirü ‘strength’; Tokh. B sfor, s. ‘sinew’; W cf. (?) nyw, pl. -iau, m. ‘vigour’; OHG sénawa, MHG sénewe, s & wf. ‘sinew, nerve’; Sw. sno, pl. at m. ‘string’; Slovene, cf. snov, f. “material, stuff; R cf. o-snova, f. ‘warp’
sneuoros (sneuros, à, io) (extn. of type sneua, etc. q.v.) ‘sinew, nerve, vein". WP II, 696. Cf. sneu- (2) and sneru- (variant). (Iran. Arm. w. suffixed article) Skt. cf. a-snávirah, adj. 'sinewless'; Av. snávars (sic), s. ‘sinew’; Oss. nwar, pl. nordtä, s. ‘vein, nerve’; Per. navard, s. “twist, fold’; Arm.
sneu- — snoiguhos
15
20
25
30
35
40
45
 
1236
neard, gs: nerdi, ab. s. -iv, s. ‘sinew, fibre’; Tokh. B. sfiaur ‘nerve’ beside fare, s. ‘thread’; Gk. neüron, n. ‘sinew, bowstring’; neurá, f. ‘sinew’; Lat. nervus, 1, m. as Gk. (also: ‘string of instrument; nerve’); cf. also nervium, n. ‘string of instrument’; nervia, f. ‘stringed in- strument; MHG snuor, sv. (‘string, bond, cord’. Phonol. obscure) beside snar, sf. id.; Du. snaar, f. ‘string’; OE sner, f. ‘string of instrument; ON snæri, n. ‘cord’; (radical in) Cz. snuju, snouti, v. (spin, twist. Cf. sneu- 2) and in Norw. snu ‘turn’. An extn. arises in Arm. niwt,, o-st. ‘substance’, cf. W nwydd, m. id. and the OCS and com. Sl. inf. snuti *weave; shape”
sneuó (1) & (2), see sneu- (1) & (2)
Sneuos, see sneuor-
sniguh- (sninguh-) ‘snow’. Cf. sneiguh-, snoiguh-. WP II, 695 Skt. cf. snih, f. *moisture'; snihyati, 3s. “gets oily, moist; Gk. cf. nípha, acc. f. ‘snow’; niphei, 3s. ‘snows’; OLat. ninguit, nivit, Lat. ningit, 3s. id. beside nix, gs: nívis, f. ‘snow’; Olr. snige, Ir. snighe, m. ‘drip, shower’; sni- gim, snighim, v. id. beside Ir. sneachta, m. ‘snow’; OHG and OE sniwan, v. id., MHG snie, sf. ‘snow, -storm’; ON snjófa, v. id.; snifinn, adj. ‘snowed under’; Li. cf. sniñga, 3s. ‘snows’ beside OLi. (e-gde) sniegti, 3s. id. and Li. snygurioti, inf. ‘flurry — as snow’; Latv. cf. snigt, 3sg: snieg ‘to snow; it snows’
sniu- (?) “strong; strength’. Cf. sneu- (1) E sneuå. Per. niv, adj. ‘strong’; W nyw, m. ‘vigour. (For Go. sniwan ‘hasten’, cf. ksneu-)
snóg-, possible variant of type no$-, q.v. Per. & Gk. ambig. Per. naz, s. ‘flirtation’; nazam, -1dan, v. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’; OE cf. snóca, wm. (queried: ‘nook’, but E snook = “a rude gesture"). (Lat. nugae ‘trifles’ here only if dia- lectal for *nogae)
(snoidh-, possible reconstruction as alterna- tive to type sneudh-. See Supt: S)
snoiguhos ‘snow’ (Skt: *grease"). Cf. sniguh- Skt. snehah, m. ‘grease’; Av. cf. snaeze
```


### [2026-09-07T19:30:14.845Z] TOOL RESULT

```
=== nog- context ===
```


## [2026-09-07T19:30:25.048Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'\\b848\\b', l) and re.search(r'no[gq$]', l, re.I):\n        print('LEAF',i)\n        print(l[:3000])\n        print('======')\nEOF"
}
```


### [2026-09-07T19:30:26.635Z] TOOL RESULT

```
LEAF 473
ám, n. ‘hollow, depression’; Gaul, nanto- ‘valley; W nant, pl. nentydd & nannau, m. id.; Cor. nans, pl. -0W, m. id.; Br. nant, pl. -ed, m. ‘brook’ For the form *nm-nós ‘low’, cf. Gk. nànos (dwarf. LW in Lat. nanus) and (uncertainly) Br. W. nam ‘blemish, fault’, cf. namn- above
nnk- (nnkió, nonkio) ‘press, force, squeeze, thrust, stab'. Cf. nnt-
Gk. násso, adj: naktós (press, cram, pile up, trampte'. The adj. nastós, also linked w. nássó, derives from a parallel form *npt-, q. v.); cf.
847 nnt-, (nntið also pí-naks, -nakos, m. “writing-tablef”; dó- naks, -nakos, m. ('two-thrust, hence “split quill, reed, arrow’); trí-naks, m. ‘trident’; cf. bo-nassos “wild bull’, fr. *guou-nnkios) and perhaps wá-naks, gs: -naktos 'ruler' and aga- naktéo (‘be incited’. Cf. ngnt- for px.); Pol. nekac, inf. ‘oppress’; Cz. v-nukat, v. ‘impress’, from *nonk-
nnt-, (nntio, nontio) *press, press on, force, squeeze’. Variant of nnk-, q.v. Cf. WP II, 317 Gk. násso, adj: nastós, as above (pf. pass. né- nasmai here; nénagmai to *nnk- above); Olr. cf. néit, f. ‘fight’; Ir. néid, f. id. (and *wound"), beside Ir. néata ‘fierce, violent’, both forms contaminated with neith, nioth, given under wt- (1); cf. also Olr. nét ‘Mars’; Go. ana- nanpjan ‘dare’; OHG nenden, id. (beside (e- gde) nindan, sv. 3 ‘grapple with"); nand, s. ‘daring’; OS naóian ‘strive’; OFris. netha ‘dare’; néth, s. ‘daring’; OE nop ‘daring; booty’; ON nenna ‘intend’; Pol. ngcic, inf. ‘allure’; Cz. nutit, inf. ‘force’; cf. (?) Hitt. nannahi, v. “drive; march" & OCS notrjo se, notriti se ‘penetrate; instil
(nó, aphetic form of type ang, q.v. in Li. nuo, Latv. no, prp. & px. “from; down- cf. Gk. nõton ‘back, top")
nó (nõu, noi) "we two’ Skt. cf. nau, id.; Gk. n6j, nói, id.; OCS (acc. & dat.) na, id.; Blg, na, nas (acc. pl. *us?) be- side enclitic ni, acc. & dat. pl. id.; Li. dial. nuo-du, id.
nobh- ‘nave, navel, hub, centre’. WP I, 130 Skt. nábhyam, n. id.; Av. nabis, f. ‘navel’; Per. naf ‘navel, middle; Oss. Dig. naffä ‘navel; OHG naba, f. “hub, nave’; OE nafu, d. ON nof, f. id. OHG cf. nabalo, wm. ‘navel’; OE nafela, wm. id. beside nafeóa, wm. ‘thub’; Latv. LW naba ‘nave’; Finn. LW napa ‘navel, hub’. (Latv. naba also = ‘navel; axle- tree, crossbar of plow’)
nobhesos (nebhos, -es-?) ‘centre-bit of drill (9). Cf. nobh- above ON nafarr, ds: nafri, m. *gimlet'; Cz. nebozez, id.
nóbhrios ‘fine, acute, astute’. Cf. ono (nö), bhrio (3) Arm. nurb, gs nrbi, i-st. “thin, fine'; Bayr.
, nontió) — nö-
20
25
30
35
40
45
848
(alleged) nuober ‘able’; MLG (alleged) nofer, id. (Holthausen); ON noefr “clever”
nódos, is, io ‘knot, tie’. WP II, 328 Alb. (LW or « *nodio) nye, gs: neni, m. & nye, def: nyja, f. id.; Lat. nodus, gs: -i, m. ‘knot, noose, knot in wood: MLG nuot, sf. “joint, fitting; LG opt nüte, f. ‘wood joint, dovetail, mortice'; Du. Fris. neut, f. ‘tenon, bolt, nut’; Icel. nóti, m. “match, equal" beside nót, f. pl. nætr "large net’; Norw. not, pl. noter, Sw. not, pl. -ar, f. 'fishing-net; Ukr. cf. pry-nada ‘lure, charm’
======
```


## [2026-09-07T19:30:31.370Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[473][2500:6000])\nprint(\"###### LEAF 474\")\nprint(leaves[474][:2500])\nEOF"
}
```


### [2026-09-07T19:30:32.686Z] TOOL RESULT

```
uober ‘able’; MLG (alleged) nofer, id. (Holthausen); ON noefr “clever”
nódos, is, io ‘knot, tie’. WP II, 328 Alb. (LW or « *nodio) nye, gs: neni, m. & nye, def: nyja, f. id.; Lat. nodus, gs: -i, m. ‘knot, noose, knot in wood: MLG nuot, sf. “joint, fitting; LG opt nüte, f. ‘wood joint, dovetail, mortice'; Du. Fris. neut, f. ‘tenon, bolt, nut’; Icel. nóti, m. “match, equal" beside nót, f. pl. nætr "large net’; Norw. not, pl. noter, Sw. not, pl. -ar, f. 'fishing-net; Ukr. cf. pry-nada ‘lure, charm’; Cz. cf. v-nadidlo, n. ‘bait’
nogudos, nogutos (noguito-) ‘naked’. Variant: nogumnos (nogunos, nongu-). WP II, 339 First form in Lat. nūdus; MIr. nocht, Ir. nocht; W noeth; Br. nôaz; Cor. nōth; Go. naqabs; OE nacod; MHG nacket & nackent, (G dial. nackend); ON noktr & nokirðr, id. beside mod. nekt, f. ‘nudity’. Second form in Skt. nagnáh; Hind. Sind. nanga, Romani nango; Av. mayno (sic), id.; Arm. cf. t-nank, gs: -1, ab.s: -av “poor” beside s-nank, i, av ‘bankrupt’; MHG nacken; ON nakinn; Sw. naken “naked. (The antecedents of Per. nang, Kurd. neng ‘shameful; shame’ and of Gk. gumnós ‘naked’, < *p-gum-? are obscure). Cpd. in Oss. bá$- näg “naked? and perh. in Gk. kín-nabos 'sculp- tor's model, if for *-nogu-?). A long-gde form arises in OCS and com. SI. nagü “naked; 
###### LEAF 474
cf. R naglyj ^barefaced, impudent; Blg. naglo, adv. ‘impudently’; Li. nuogas *naked'; An e- gde form arises in Hitt. nekumanc ‘naked’, fr. *ne-gum- ‘uncomely’?
(noguhos, à, variant of type onugh-, q.v. in Icel. naggur, m. ‘peg’; Li. nagas, naga ‘nail, claw, hoof; Latv. nags, m. id.)
nóg- (1) ^whim, triviality, fancy, dalliance, teasing, mockery'
Per. nàz ‘flirtation, flattery’; cf. nazuk ‘flashy’; nàzidan, inf. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’ (if not < *no, eno, and *&olok?); OLat. nogae, cpds. naug-, Class. nügae 'trifles'; Fris. noekje “darling, favourite" beside noekerje, v. ‘cajole, coax’; (but G Nucke, Nücke, f. *whim' is fr. MLG nucke, id., and Du. nuk, f. id. is appa- rently fr. LG); R cf. za-nóza, f. ‘irritant; irri- table person' (?); Li. (?) nuoZ-mas, -mus, adj.
849
“grim”
nóg- (2) Q) Per. nàZu 'fir, juniper'; Oss. naz, nazu, id. beside näzí ‘Scotch fir; LW in Arm. noč, noci ‘cypress and in Georgian nadzvi “fir
noid- ‘hate’. Cf. ne-, n-, uoid- (?). WP II, 322 Skt. cf. à-nedyah ‘blameless’; Go. ga-naitjan, v. ‘denigrate’; MHG neis, s. ‘torture’; neisen, v. id.; OE nætan, v. “hurt, harm'; ON neita, v. “deny, refuse'; Latv. naids, m. “hate, hosti- lty’; cf. (z-gde) nidu, inf. nist, v. ‘hate’. (For Gk. ón-eidos, n. “shame, blame”, cf. uon- “lack? and ueidos 'face")
noigos, à “gentle, fair; gentility, fairness, beauty” OCS něga, f. ‘delight’; R ‘effeminacy’; Srb. ‘cherishing’; Cz. něha ‘gentility, fondness’; Latv. naigs, adj. (3) ‘beautiful
noigh- OE nægan, v. ‘accost, attack’; ge-nāg (hapax) ‘dashing’; Latv. naigs, adj. (1) ‘quick’
noik- ‘force, impetus’. Cf. neik-, nik- (2) Lat. cf. per-nix, -nicis, adj. (quick; persistent". Vocalism ambig.); Latv. naiki, adv. ‘violently, excessively’; (Li. isophone: naikùs 'perish- able’). E-gde in Gk. neikos, n. ‘strife’; z-gde in Gk. nike ‘victory and in Li. i-nikti, pr. -ninku ‘strive; tackle, grapple with’; i-nykis, gs -io, m. ‘gusto’ Å
noit- (nit-) (1) “inflame, kindle; be inflamed, burn brightly”. Lat. niteo, ere, v. ‘shine’; cf. nitidus, adj. ‘bright’; o-gde in OCz. nietiti, Pol. niecic, Slovene netiti, inf. (inflame, kindle’. Not re- lated to the OCS type gnétiti ‘inflame, arouse’)
noit- (2), o-gde variant of type *neit-, see nit- (1) Lat. cf. (vowel ambig.) nitor, sup. nisus & nixus (of two separate origins but here in the sense of “strive*); Cz. cf. pod-nét 'enter- prise’; pod-nítit, inf. ‘undertake’. (For sup. nixus, cf. niks- (1) above)
(nói, nou, forms of the dual number "we two’. See no. WP II,
```


## [2026-09-07T19:30:47.918Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/FFD/\necho \"=== search naz in FFD ===\"\ngrep -n \"ناز\" incoming/FFD/FFD_pages.txt | head -20\necho \"=== pdf page tags near ===\"\ngrep -n \"pdf page 7[5-9]\" incoming/FFD/FFD_pages.txt | head"
}
```


### [2026-09-07T19:30:47.976Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
=== search naz in FFD ===
2096:نازیدن
2098:ناز ج فارسی میانه 232 + ایرانی باستان ۸32*. 232 در ایرانی باستان اسم است به
=== pdf page tags near ===
1886:[pdf page 75]
1910:[pdf page 76]
1944:[pdf page 77]
1967:[pdf page 78]
1989:[pdf page 79]
```


## [2026-09-07T19:30:49.443Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nazuk/naxun ===\"\ngrep -n -i -E \"n[aā][zžc][uū]k|nāxun|naxun|nāxwn\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i -E \"nāzuk|nazuk|nāxun|naxun\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:30:49.517Z] TOOL RESULT

```
=== PHD nazuk/naxun ===
PHD.txt:506:nāxun [whwn! | N ~] (finger) nail.
PHD.txt:1923:fickle nāzuk, r6zward.
PHD.txt:2094:gentle Carb, nazuk.
PHD.txt:3948:tender nāzuk.
PHD.txt:5255:naxcir 1-2wazidan nazuk
PHD.txt:5303:niyäyišn wihān, wiyān nāxun wihānag
PHD_mackenzie.txt:582:read nixun [n' hwn' I P nxwn, N naxun] (finger) nail.
PHD_mackenzie.txt:3680:naxun [n)hwn ' I N --] (finger) nail.
PHD_mackenzie.txt:3696:nazuk [n)cwk l I (M n)zwg), N --] tender, gentle; fickle.
PHD_mackenzie.txt:6686:gentle carb, nazuk.                           grace (prayer) waz; say                  waz
PHD_mackenzie.txt:7123:monkey kabig.                                  nail mcx; (finger) naxun, sru.
PHD_mackenzie.txt:7768:tender nazuk.                             three se.
PHD_mackenzie.txt:10270:wadrang            .I~~\.                   nazuk
=== NYB ===
```


## [2026-09-07T19:30:59.515Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1944,1990p' incoming/FFD/FFD_pages.txt\necho \"=== around line 2096 ===\"\nsed -n '2085,2105p' incoming/FFD/FFD_pages.txt\necho \"=== which pdf page is 2096 ===\"\nawk 'NR<=2100 && /\\[pdf page/ {p=$0} END{}' incoming/FFD/FFD_pages.txt\ngrep -n \"\\[pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1<2100' | tail -3"
}
```


### [2026-09-07T19:31:00.842Z] TOOL RESULT

```
[pdf page 77]
کچ یا ی فعلهای فارسی دری
گرفتن
گرفت + فارسی میانه 878 < ایرانی باستان 87۳-4۵ *. برای 13 > آراست. 870 صورت
: اصلی 871 است» ۳ پیش از ۲ به / بدل شده است. 870 صورت ضعیف ريشةٌ 8780 به
معنی «گرفتن» است.
گیر + فارسی میانه 8۲3 < ایرانی باستان 8۲8-72*. 72 نشانه‌ای بوده که برای ساختن
ماده از ريشه به کار می‌رفته است.
گروستن, گرویدن
گروست + فارسی میانه ۷۷07۲2۷۷181. ۱۷۷۵۳۷۷/۶1 مادةٌ ماضی جعلی از مادهٌ مضارع
است. «گروید» در فارسی دری مادهٌ ماضی جعلی است. از مادهٌ مضارع.
گرو + فارسی میانه ۷۷۵۶۶۷۷ + ایرانی باستان ۴۷۶۵۷ ۷۲ صورت ضعیف ريشةٌ
57 به معنی «گُزیدن) است. 1820 برای ساختن ماده مضارع از ريشه به کار می‌رفته است.
گریختن ۱
گریخت + فارسی میانه ۷۷788 + ایرانی باستان ۷۷1-۵0-1۵*. برای 18 -> آراست. ۷:1
پیشوند فعلی است. 7211 صورت اصلی 731 است» 1 پیش از 1 به تابدل شده است. ريشةٌ
جه به معنی «ترک کردن» است. (ریختن» از ریشةٌ انة7 آمده است + «ریختن».
گریز + فارسی میانه ۷762« ایرانی باستان ۷1-۵16-2*. برای ۵ -> آرای. ابه جای ۸
آمده است.
گریست < فارسی میانه افاولاع. 81اررزتع ماده مأضی جعلی است» از مادهٌ مضارع
ساخته شده است.
گری + فارسی میانه 1تع + فارسی باستان 8۲4-78* « ایرانی باستان 8۳۵2-78 *. 2
برای ساختن مادةٌ مضارع از ريشه به کار می‌رفته است. ريشهٌ 8792 به معنی «گله کردن»
[pdf page 78]
ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
گُزیدن
گُزید ج فارسی میانه ۷127۵ < ایرانی باستان ۶۷-6۲-1۵ برای ۵ > آراست. ۷
پیشوند فعلی است. آت صورت ضعیف ریشةٌ له به معنی «گزیدن» است.
گزین ج فارسی میانه ۷۵217 < ایرانی باستان ۹1-61-۵*. 120 نشانه‌ای بوده که برای
ساختن ماده مضارع از ريشه به کار می‌رفته است.
گزیدن
۰ کِ شت.+
گستردن
گسترد < فارسی میانه ۷181۵74 < ایرانی باستان ۴۷۷1-81۵۳-12. برای ۵ -> آراست. ۷1
پیشوند فعلی است. ريشهٌ 5187 به معنی «پاشیدن» است.
گستر < فارسی میانه ۷۷۶17 < ایرانی باستان ۷1-۹1۵۳-۵*. برای 2 -> آرای.
ا گسست < فارسی میانه ۷9181 < ایرانی باستان ۷:1-918-1۵*. برای 2 > آراست. ۷:1
؛ پیشوند فعلی است. 814 صورت اصلی ريشه به معنی «بریدن» است و 4 پیش از ]به بدل
[pdf page 79]
4۳ نفعلهای فارسی دری
=== around line 2096 ===
ماده‌های ماضی و مضارع قارسی دزی شش ۷۷
مشت.
مُشت + فارسی میانه 151 + ایرانی باستان 1۹-1۵*. برای ۵ > آراست. 177
صورت.اصلی ۲5 است» 2 پیش از ۲ به 5 بدل شده است. 172 صورت ضعیف ريشهةٌ
2 به معنی «مالیدن» است.
مال + فارسی میانه 721 + فارسی باستان 1۵۳4-8* < ایرانی باستان 1۵72-۵*. برای
3 > آرای.
موییدن
«مویید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
موی < فارسی میانه 136 < ایرانی باستان 1۳۵-2*. برای 2 آرای.
ریش 13200 به معنی «نالیدن» است.
نازیدن
«تازید» مادهٌ ماضی جعلی است. از مادةٌ مضارع ساخته شده است.
ناز ج فارسی میانه 232 + ایرانی باستان ۸32*. 232 در ایرانی باستان اسم است به
معنی «شادی»» «افتخار». 132 در فارسی میانه «شاد بودن» «مفتخر بودن» معنی
می‌دهد.
نالیدن
«نالید» ماده ماضی جعلی است. از ماده مضارع ساخته شده است.
نال ج فارسی میانه 281 < ایرانی باستان 8۵۲۵-۵*. برای 2 آرای. ريشةٌ 1874 به ۱
معنی «بانگ کردن» است.
نشاست < فارسی میانه 213391 < ایرانی باستان 339-۵-زم"
=== which pdf page is 2096 ===
2027:[pdf page 80]
2060:[pdf page 81]
2084:[pdf page 82]
```


## [2026-09-07T19:31:15.154Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 249 (p228) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==250' HRN.txt | head -70"
}
```


## [2026-09-07T19:31:15.599Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full onogh entry ===\"\nsed -n '63935,63990p' POK_full.txt"
}
```


### [2026-09-07T19:31:16.349Z] TOOL RESULT

```
=== HRN leaf 249 (p228) ===
— 228 —
N.
1013. ni'j Praefix nieder.
ap. m-, niy-; aw. ai. m- nieder-, ein-'; phlv. w(O^).
oss. d. m-, t. nt- (202).
1014. nä- *un-, nicht-', ne- (z. B. nespas).
aw. wa ; ai. nd.
1015. nä& rein, ungemischt*.
aw. anäp' ohne Wasser*; phlv. anap,
1016. nä%un *Nagel (am Finger oder an der Zehe)' 2).
ai. nakhä- 'Nagel, Kralle'; phlv. nä/un (Bund.),
kurd. neinuJc ^Nagel'; afy. nük; bei. näkun^ vahuft,
n. na/un (257).
1017. näi^uk 'zierlich, lieblich, zart', näz 'Freude, Ver-
gnügen ; Ruhm', nüzlden, näznln, HTiTW (Is. 66, 12).
Käs. Q. nac^ naster (Comp.) s. v. /üb.
phlv. näcuk.
LW. kurd. näzik; afj'. näzak, vergl. vPnzaka; bei.
näzurk, n. näzuk.
1018. näsüdefi 'abmagern'.
aw. [/^nas-, nasy^iti verschwinden', Causat. 'ver-
schwinden machen'; phlv. na^mtan Vernichten' (P.-
Vend.) ; ai. l^nag-, ndgyati verschwinden, verderben'.
wa/. nüs-am, Hiyn. hinis-am sar. binäs-am Ver-
lieren*.
1019. näStä 'nüchtern' (AM. 216 Zeile 5), benästa (AM.
232 Zeile 2, 3), nastab, nastat,
na + ai. V^aQ-, agndti *essen', Nöldeke, münd-
liche Mitteilung, doch vergl. unter np. äs (No. 29).
1020. nfe/ 'Nabel', nafe,
g. nafk.
aw. nafah' 'Geschlecht*, vergl. nOfya^ 'Verwandt-
schaft*; phlv. nafak, f?^/ 'Nabel', vergl. N[a]f^[far'nai
(Gemme, ZDMG. 18 No. 37 (IV)).
>) Vergl. S. 197 Anm. 1.
2) Vergl. Bartholomae, BB. XVII, 133.
```


### [2026-09-07T19:31:16.401Z] TOOL RESULT

```
=== POK_full onogh entry ===
ym en-yn {irom *emen-yn)\ compare above Old Indie ajyam. 

Maybe zero grade in alb. {*ng"h-en) ngjyenfXo wet, moisten; to dye, color, imbue'. 

References: WP. I 181, Kuiper Nasalpras. 122. 
Page(s): 779 

Root / lemma: onogh-{. ongh-, nogh-, Ce\^\c Qgh^, ongh-li-{* huen(e)gh-) 

Meaning: fingernail, claw 

Note: partly with formants -:/- (extended -ut-) and -lo- 

Material: Old Indie {* h2ahghli-) anghn-\. "foot' (presumably with rfrom /, *orjgh-li-)\ with 

Aryan A/? Old Indie nakham., n., nakhara-m. n., "nail, claw, talon ', np. naxun ds. (Aryan 

kh- an innovation); perhaps Armenian eiungnds. {*e-nungn): 

gr. (*/7j6vu^) ovu^, -uxo(; "nail, claw, talon ' (from *6vxu-?); 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Latin gw- > u-. 

Latin ungu-is^Vr\e nail an Fingern and Zehen', ungula^ claw, nail, hoof, later also "nail' 
{*ongh-(em; 

Maybe zero grade in alb. {*huengla) thua " nail ', thundia, thundra^ hoof ' : Italian unghia : 
Spanish una : Calabrese ugna : Catalan ungia : Furlan ongule : Galician unlla; una : Ladin 
aundia : Portuguese unha : Romanian unghie : Romansh ungIa : Sardinian Campidanesu 
unga: Sardinian Logudoresu ungra: Sicilian ugnu: Valencian ungIa: Wallon ongue^ nail 

i 

Ladin aundia^ nail ' = alb. thundia, thundra^ hoof, thembra^ heel ' reflects common alb. - 
ng- > -nd-, -mb-. 

Also alb. ke-the-ter, kthetec "nail, claw, talon '. 

Note: alb. thoi, thua, pi. thonj^ nail ' : alb. thengjiir {*co3\) ash'; Root/ lemma: onogh-{: 
ongh-, nogh-, Celtic Qgh^, ongh-li-{* huen(e)gh-)\ "fingernail, claw' : Root/ lemma: ong- 
(better ang^ {*heng-)\ "coal'; alb. has preserved the old laryngeal. 

Old Irish ingent Dat. PI. ingnib, Nom. PI. ingnea, acymr. eguin, ncymr. em'nf., corn. 
euu/n, bret. /v/n{m. has changed) "nail' {*nghu-Tna); 



Old High German nagal, Old English n^gerv\a\\\ Old Icelandic nag/6s. (conservative 
stem has changed, PI. neg/); neg/ perhaps originally reinterpreted Sg. /-stem, compare Old 
Indie atighri-, and to PI., whereof are attached the additional conservative Dekl.), Gothic 
ga-nagljan^ nail '; 

Lithuanian nagas m. " nail in fingers and toes; claw of birds of prey ', Latvian nags ds.; 
Lithuanian naga'hooT, Old Prussian nageloot', Old Bulgarian noga, russ. nogaloot'
```


## [2026-09-07T19:31:35.052Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK page tag ===\"\nsed -n '63990,64010p' POK_full.txt\necho \"=== AHD watkins nail ===\"\ngrep -n -i -E \"^\\(o\\)nogh|onogh|nogh-\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T19:31:35.115Z] TOOL RESULT

```
=== POK page tag ===
Lithuanian naga'hooT, Old Prussian nageloot', Old Bulgarian noga, russ. nogaloot' 
(collective a-formation); Lithuanian nagutis. Old Prussian nagutis^ fingernail ', Old 
Bulgarian nog-btb, russ. nogotb "nail, claw, talon '; 

after Specht to gr. oyKoq (above S. 46), also root on-. 

References: WP. I 180 f., Trautmann 192, Specht Indo Germanic Dekl. 253^. 
Page(s): 780 

Root / lemma: o/70-and one-, also (o)no-d- 

Meaning: to scold 

Material: Gr. ovopai ' scolds, reproves ', ovoto^ ' reproved, reproachable ', ovotq^w " 

scolds, reproves '; with -a- the second syllable of hom. wvaro and ovarai aripia^STai. 

IjepcpETai Hes.; 

Middle Irish 0/7' shame'; perhaps with reduplication-stem also the first syllable of Middle 

=== AHD watkins nail ===
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1900:NACELLE nau-2 NAG! ghen- NAIAD (s)nau- NAIL nogh- NAINSOOK nele- NAIVE gene- NAKED nogW- NAME no-men- NANA nana NANNY nana NANO- nana NAP] ken-2 NAP2 ken-2 NAPERY mappa NAPKIN mappa NAPPE mappa NARCO- (s)ner- NARCOSIS (s)ner- NARCOTIC (s)ner- NARES nas- NARK? nas- NARRATE gnoé- NARROW (s)ner- NARWAL (s)kWal-o- NARWHAL nau-! NASAL nas- NASCENT gene- NASO- nas-
1980:-ONYM no-men- -ONYMY no-men- ONYX nogh-
2061:PARGET per, yé- PARHELION sawel- PARI-MUTUEL pere-2 PARISH weik-1 PARITY2 pere-2 PARLAY pere-2 PARLEY gWelg-1 PARLIAMENT gWele-1 PARLOR gWelg-1 PARLOUS per-4 PARODY wed-2 PAROL gWele-1 PAROLE gWele-1_ PARONOMASIA n0-men- PARONYCHIA nogh- PARONYMOUS no-men- PAROTID GLAND ous- -PAROUS pere-) PAROUSIA es- PAROXYSM ak- PARRICIDE paso- PARRY pere-!
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2212:SAPID sep-1 SAPIENT sep-1 SAPONACEOUS _ seib- SAPONATE seib- SAPONIFY seib- SAPONIN seib- SAPONITE seib- SAPOR sep-! SAPROBE gWei- SAPSAGO skep- SARCASM twerk- SARCO-  twerk- SARCOCARP twerk- SARCOID twerk- SARCOLEMMA lep-1 SARCOMA twerk- SARCOPHAGUS twerk- SARCOPTIC MANGE skep-, twerk- SARCOUS twerk- SARDONIC sward- SARDONYX nogh- SARMENTOSE serp-1 SARTORIUS serk- SASTRUGA ghd, ster-2 SATE! sa-
2436:UNCIAL ol-no- UNCIFORM = ank- UNCINARIA ank- UNCINATE ank- UNCINUS ank- UNCLE awo- UNCOUTH gn6- UNCTION ong¥- UNCTUOUS ongW- UNCUS ank- UNDER ndher- UNDERNEATH ni UNDERSTAND sta- UNDINE wed-! UNDULATE wed-1 UNGAINLY gagina UNGUENT ong¥- UNGUIS nogh- UNI- oi-no- UNICORN ker-1, oj-no- UNION oi-no- UNIQUE oi-no- UNISON swen- UNITE oi-no-
```


## [2026-09-07T19:31:35.889Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 269 (p245) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==270' SYN.txt | head -60"
}
```


### [2026-09-07T19:31:37.066Z] TOOL RESULT

```
=== SYN leaf 269 (p245) ===
s ‘neck’ (below, 5), rather than fr. *kel- ‘rise, project’ in celsus ‘high’, collis ‘hill’, etc., though either connection is possible phonetically, and semantically accord- ing as the words orig. denoted the (round) neck’ or the ‘nape of the neck’. Ernout-M. 204. Walde-H. 1.245 (vs. Walde-P. 1.434). Feist 242.
Rum. git, orig. ‘throat’ (hence gitle7 ‘throat’), loanword fr. Slavic, SCr. gut ‘throat’ (obs., but gutati ‘swallow’), Slov. golt ‘throat’, Bulg. giiltitk ‘a swal- low’, etc., these : Lat. gula ‘throat’, etc. (4.29). Tiktin 684. Berneker 309.
3. Ir. brage ‘neck’ and rarely (inner) ‘throat’ (cf. K. Meyer, Contrib. 8.V.), Nir. bragha mostly ‘throat’ : MHG krage (below, 4), Grk. Bpéx6os ‘throat’,
Digitized by Arya Samaj Foundation Chennai and eGangotri
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
Skt. gr- ‘swallow’, Lith. gerti ‘drink’, ete. Walde-P. 1.683. Pedersen 1.100, 183.
Ir. muin, muinél ‘nape of the neck’? NIr. muinéal ‘neck’, W. mwn (arch,), mwnwgl ‘neck’: ON men, OE mene ‘necklace’ (also OF manu ‘mane’, etc.), Lat. monile ‘necklace, collar’, Skt. manya- ‘nape of the neck’, Av. miny, ‘necklace’, manaobri- ‘neck’ (both words in Yt. 5.127, cf. Barth. 1126), all prob, fr. IE *men- ‘project’ in Lat. eminére, prominere ‘project’, mons ‘mountain’, etc. Walde-P. 2.305, 265. Pedersen 1.33.
W. gwddf, Br. gouzoug (both also ‘throat’), etym.? Pedersen 1.63. Henry 142. Morris Jones 145 (cf. Loth, RC 36.170).
4. Goth. hals, etc., above, 2.
ON sviri, OE swéora, swira (so, not heals, always in the Gospels), ME swere (cf. NED s.v. swire) : OE swer, sweor ‘column’, Skt. svaru- ‘post’, etc. Walde- P. 1.528.
ME necke, NE neck, fr. OF hnecca ‘nape of the neck’ : ON hnakki, OHG hnac, NHG nacken, etc. general Gime. for ‘nape of the neck’, prob. : Ir. cnoc ‘hill’, etc. Walde-P. 1.391. Falk-Torp 754,
MHG krage ‘neck, throat, collar’ (NHG kragen ‘collar’, rarely ‘neck’, Du. kraag ‘collar’; ME crawe, NE craw with only specialized meaning) : Ir. brage, etc. above, 3.
5. Lith. kaklas, Lett. kakls : Grk. xbxdos ‘circle’, Skt. cakra- ‘circle, wheel’, OE hweol ‘wheel’, etce., fr. IE *kel- ‘turn’, as prob. also Lat. collum, Goth. hals,
```


## [2026-09-07T19:31:45.449Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"4\\.1[0-9] +NAIL|NAIL \\(OF FINGER|FINGER-?NAIL\" SYN.txt | head\necho \"---\"\ngrep -n \"naxun\\|nāxun\\|nāxun\\|näxun\" SYN.txt | head\necho \"--- persian nail\"\ngrep -n -i \"unguis\" SYN.txt | head"
}
```


### [2026-09-07T19:31:45.518Z] TOOL RESULT

```
---
--- persian nail
15090:4. (Goth. ga-nagljan, vb., ‘nail on’), ON nagli, OF nagel, ME nayl, NE nail, OHG nagal, MHG, NHG nagel, the same words as for ‘nail’ of the finger or toe (except that ON nagli and nagl are differentiated), this latter sense being the orig., as in the cognates, Grk. dvvé, Lat. unguis, etc. (4.39).
```


## [2026-09-07T19:31:47.750Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN nail entry ===\"\ngrep -n -E \"^nail|nail, n\\.|'nail'\" KLN_1966.txt | head -20\necho \"=== KLN grep nagl ===\"\ngrep -n \"OE. nægel\\|næ3el\\|nagl-\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T19:31:47.822Z] TOOL RESULT

```
=== KLN nail entry ===
24913:nail,  n.,  1)  the  horny  substance  on  the  ends  of  the fingers  and  toes;  2)  a  small  spike  of  metal  or wood.  —  ME.  naile,  neil,  fr.  OE.  nsegl,  ntegel, ‘fingernail;  metal  nail,  peg’,  rel.  to  OS.,  OHG. nagal,  OFris.  neil,  MDu.  naghel,  Du.,  MHG., G.  nagel,  ‘fingernail;  metal  nail’,  ON.  nagl,  ‘fin¬ gernail’,  nagli,  ‘metal  nail’,  Goth,  ganagljan,  ‘to nail’,  fr.  I.-E.  base  *nogho-.  *ngho-,  *ongho-, ‘nail’,  whence  also  OI.  ahghrih,  amhrih,  ‘foot’, Gk.  ovu^,  L.  unguis,  ‘nail,  claw’,  OSlav.  noga, Russ,  noga,  Czech  and  Slovak  noha,  ‘foot’,  Lith. naga,  ‘hoof’,  ndgas,  Lett,  nags,  ‘nail’,  OPruss. nage,  ‘foot’,  OSlav.  nogiiri,  ‘nail,  claw’,  Lith. nagiitis,  OPruss.  nagutis,  ‘fingernail’,  OIr.  ingen, OW.  eguin,  W.,  Co.,  ewin,  Bret,  twin,  ‘nail,  claw’. Cp.  OI.  nakhdft,  Pers.  naxun,  ‘nail,  claw’,  where qh-  (for  gh-)  is  prob.  due  to  Caucasian  influence. —  Cp.  agnail.  Cp.  also  onyx,  ungual. Derivatives:  nail,  v.  (q.v.),  nail-less,  adj.
24914:nail,  tr.  v.,  to  fasten  with  a  nail  or  nails.  —  ME. nailen,  fr.  OE.  nseglian,  fr.  nsegel,  ‘nail’;  rel.  to OS.  neglian,  ON.  negla ,  OHG.  negilen,  MHG. negelen,  nagelen,  G.  ndgeln,  Goth,  ganagljan,  ‘to nail’.  See  nail,  n.
=== KLN grep nagl ===
```


## [2026-09-07T19:31:56.241Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'4\\.\\s*39\\s+NAIL|NAIL\\s*\\(OF', l, re.I):\n        print('LEAF',i)\n        print(l[:3000]); print('=====')\nEOF"
}
```


### [2026-09-07T19:31:57.544Z] TOOL RESULT

```
LEAF 282
var, hval- ‘go crookedly, go astray, err’, etc. Barth. 1699, Walde-P. 1.648.
Av. dvariéra-, fr. dvar- ‘go, hasten’ (of evil beings), prob. : Skt. dhur- ‘run’ (only Dhatup.), further connections stil] more dub. Walde-P. 1.842. Otherwise
OPruss. nage ‘foot’, Lith. naga ‘hoof’, all | Barth. 765.
4.38 TOE Grk.  daxrvdos Goth. Lith. pirStas (kojos) NG daxr7vd0 (Tod zodtod) ON ta Lett. (kdjas) pirksts Lat.  digitus Dan. taa ChSl.  priistii(?) It. dito (del piede) Sw. td SCr. _ prst (od noge) Fr. orteil, doigt du pied OE ta Boh.  prst (na nahou) Sp. dedo (del pie) ME to Pol. palec (u nogi) Rum. deget de la picior NE toe Russ. alec (na noge) Ir. mér (coise) Du. teen Skt.  anguli-, padaiiguli- NIr. = méar (coise) OHG zaha Av. angusta- W. bys troed MHG ze(he) Br. biz troad NHG zehe
‘Toe’ is usually expressed by the word for ‘finger’ (4.34) with or without the addition of ‘of the foot’. The use of parentheses in the list attempts to show the situation. The distinctive words for ‘toe’ are:
1. Fr. oréeil, fr. OF r. arteil, fr. Lat. articulus ‘joint, knuckle, limb’, also of
the fingers (articulus manus), but crossed with Gall. ordiga ‘big toe’ (Cassel Glosses). REW 687. Wartburg 1.149 f.
2. ON Za, etc., all the Gme. words, prob. orig. ‘finger’ as ‘pointer’ : Lat. index ‘index finger’, digitus ‘finger’ (4.84). Walde-P. 1.776. Falk-Torp 1237. Walde-H. 1.351.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
yp BODY; BODIL
Y FUNCTIONS AND CONDITIONS
Digitized by Arya Samaj Foundation Chennai and eGangotri
245
4.39 NAIL Goth. «.-- Lith. mnagas Lett. nags out ON _ nagl J oe ie Dan. negli ChSl.  nogittt N unguts Sw. nagel SCr.  nokat Bs unghia OE negl Boh. nehet " — ongle ME We oe pene “ ufia NE nat E Rum. unghie Du. nagel Skt. nakha- ingen OHG  nagal Av. sri, srvd- Nir. tong MHG  nagel ' lal NHG  nagel ivin
+ *(o)nogh- (with wide variation of ae aad suffixes in different Ik languages). Walde-P. 1.180 f. Ernout- Sa all the words listed except Av. sri, srva (below), but represented in Iranian by NPers. nazun (Skt. also nakha-, with unexplained kA for gh). NG viy. fr. dim. dvixcov; the Romance
forms fr. the Lat. dim. ungula (REW 9071); Pol. paznokieé, cpd. with prefixed paz-: pazur ‘claw’, pazucha ‘breast’, Boh. page ‘arm’ (4.31), etc. (Briickner 400).
2. Av. sri, srvd, also ‘horn’ (the earlier meaning) : Grk. xépas, etc. ‘horn’ (4.17). Walde-P. 1.404. Barth. 1647 f.
4.392 WING Grk. —-rrépué Goth. Lith. sparnas NG  ¢repobya ON vengr Lett. sparns Lat. dla, penna Dan.  vinge ChSl._ krilo ; ala Sw. vinge SCr. _krilo aile OE fipere, fepera (pl.) Boh.  kridlo . ala ME wenge, winge Pol. skrzydlo Rum. aripd NE wing Russ. krylo . elle, sctath Du. vleugel Skt.  paksa-, pattra- NI eile, etleog, sciathan OHG  federah, fettach Ay. parena- + adain, asgell MHG _  vliigel, vedrach askell NHG  fligel
Many of the words for ‘wing’ are de- tived from verbs for ‘fly’, whence also ay of those for ‘feather’, in this case a Secondary sense, which are then included
y the joint or a
=====
```


## [2026-09-07T19:31:58.126Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'the  horny  substance  on  the  ends' in l:\n        print('LEAF',i)\n        import re\n        print([m for m in re.findall(r'\\b10[0-9][0-9]\\b', l)][:20])\n        print(l[:400])\n        break\nEOF"
}
```


### [2026-09-07T19:31:59.398Z] TOOL RESULT

```
LEAF 549
[]
l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  from  the  stem  of na'em  ‘was  pleasant  or  lovely’,  whence  also na'tm,  ‘pleasant,  lovely’,  nd'am,  ‘pleasantness, loveliness’,  and  the  PN’s  Na‘dmdh,  No‘dmt ;  rel. to  Arab,  na'ima,  ‘was  easy  or  pleasant’,  an'ama, ‘he  granted  a  favor,  favored’.  Cp.  cnam,  Naomi. Cp.  also  anemone.
Naassenes,  n.
```


## [2026-09-07T19:32:07.271Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-07T19:32:08.575Z] TOOL RESULT

```
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
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/
```


## [2026-09-07T19:32:19.472Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(544,553):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', leaves[i])\n    print(i, nums, leaves[i][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T19:32:20.816Z] TOOL RESULT

```
544 ['1015', '1016', '1017']  like  a  mummy,  to  dry  up,  shrivel.  — F.  momifier,  compounded  of  momie
545 [] urrain’,  which  also  derive  fr. VL.  *morire.  Cp.  murrina. murre,  n.,  1) 
546 ['1021'] appoint,  something;  to  have  room; to  be  able;  to  be  obliged’,  d-degree
547 ['1022']   ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  because  according to
548 [] d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'or
549 [] l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  fro
550 ['1028']  B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  
551 []   of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr
552 ['1033'] us,  ‘birth,  des¬ cent,  origin,  race,  sort,  kind,  class’.  See  genus and
```


## [2026-09-07T19:32:36.913Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 naxon ===\"\ngrep -n \"ناخن\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== BQT v4 naz ===\"\ngrep -n \"^ناز\\|ناز(\\|نازک\" incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-07T19:32:36.977Z] TOOL RESULT

```
=== BQT v4 naxon ===
4546:که دربن ناخنها پدیدآید ؛ وبستی کویندتقیلهای ملکان < بروزن مرجان » نام پدر خض
4547:سفید اس ت که برناخن افتد۴ - و درعربی بممنی | علیه‌اللام باشد و او از احفاد سام پن :توح است
4556:۳ - « ملك . سپیدی پن ناخن باشد . احمد برمك گفت :
4557:ملك از ناخن همی جدا خواهی کرد دردت کندای دوست . خطا خواهی کرد.»
6844:ناچو ؟ - با جیم بواوکشیده » درخت ناخن آفتاب - کنایه از آش
6845:کاج‌است وبمربی صنوبر خوانند . است -شاکنایه از ناخن مطلوب و شاهد هم
6847:- وظرف شرابخوربراکوبند ‏ ناخن پال ۸ با بای فارسی بالف
6849:که سوراخ وسط شکم باشد . بر اطراق ناخن مردم پدید آید ودرد بسیارکند
6851:کوبند که از جای خود تتواند برخاست بمنی ناخن بد ند آن - بستی‌انگت‌بدندان-
6862:۹-« ناخن آفتاب یعنی آتش . خاقانی کوید :
6863:چشم سهیل وناخنه ناخنآقتاب ونی کانش وقند او دهد با نی ویاد یاوری.
6866:با آنکه دیدن سهیل ناخنه را دفم کند و درناخن آفتاب - که عبارت از خطوط شماعی است -
6868:لب‌او - با نی نواختن وباد درآن دمیدن مشغول شود.» فرشیدی». رك:ناخنه. ۷ رك : رشیدی .
6869:۸ - از : ناخن + یال ( پالودن بممنی افزون وزبادهگشتن ) (4) قس : ناخن‌خاره .
6870:َ 2 ناخی - جم سوم * ناخون (ء.م.) , هندی باستان -281۳84 ( ناخن اسان » ناخن
6874:چون نداری ناخن درنده تیز با ددان آن به ک هکم کیری ستیز .
6878:است که کنایه ازحیرت وافوی ومتأسف وحیران ناخن‌خامه « بکسر نون » کنایه از
6881:قرشت بالف کشیده, بمعتی مقراض وقیجی باشد. وآن ورمی‌باشد که دراطراف ناخن‌پهم رسد وناخن
6884:ناخن پریات ۴ - بفتح بای فارسی | خای نقطه‌دار و سکون واو معدوله وشین قرشت.
6885:وکسر رای قرشت وتختانی بالف کشیده و بنون | بممنی‌ناخن پربان است وآن نوعی ازسدف باشد
=== BQT v4 naz ===
7209:نازگ ۱ - بنم ثاك و سکون کاف . گفته‌اند که بعربی سنور خوانند .3۴
7212:ناز لگ پدن < بنتح باودالابجدوسکون ناه ۴ با زای فارسی بر وزن تازه »
7216:ناز نوروز - بکر تاك و فح نون ناصازی * » با سین بی نقطه" و زای
```


## [2026-09-07T19:32:38.205Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS 258 ===\"\ngrep -n \"\\[pdf page 25[5-9]\\]\\|\\[pdf page 26[0-3]\\]\" SNS_pages.txt | head\necho \"--- grep naxun/naz in SNS\"\ngrep -n -i \"n[aā]xun\\|naxwn\\|nāz\\b\" SNS.txt | head -10"
}
```


### [2026-09-07T19:32:38.272Z] TOOL RESULT

```
=== SNS 258 ===
--- grep naxun/naz in SNS
14489:•O*^ :naxun: \*o- 
32104:naxun 258/3
```


## [2026-09-07T19:32:44.912Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS glossary entry around 14489 ===\"\nsed -n '14480,14495p' SNS.txt\necho \"=== BQT v4 pdf page for line 6870 ===\"\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v4_pages.txt | awk -F: '$1<6875' | tail -3\necho \"=== context 6855-6880 ===\"\nsed -n '6836,6875p' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-07T19:32:46.120Z] TOOL RESULT

```
=== SNS glossary entry around 14489 ===


TO^ 




• Y*-Tft/lV«f -TT/W -{Mir. Man. II,52)wh a ng : ^fc 

•O*^ :naxun: \*o- 
tfotw<2Z,158)n'xwn:^ GffP*. 228) nakha-:^*^ 

•y/it*5 .6r-T-r/v^ 

• ojU.Uj,^^ miyayisn: «*->*-«o* 
l/T»irf *{&>&>) nySiSn : ^ 
=== BQT v4 pdf page for line 6870 ===
6765:[pdf page 170]
6802:[pdf page 171]
6838:[pdf page 172]
=== context 6855-6880 ===
جدا نگردد .
8 ناجرهکي - موب به « ناجرم > (همی)
[pdf page 172]
-۲۸۹- اخن بدسان
ناجزانجام ۱ -» بنم جیم و سکون | زمن‌کیر .
زای نقطه‌دار وفتح همزه ونون ساکن وجیم بالف ناخد) ‎٩‏ - مغفف ناو خدا است پمنی
کشیده وبمیم زده » بمعنی‌نامتناهی باشد وبمربی صاحب و خداوند ناو که کنایه از کتتی و جهاز
الی غیرالنهایه کوبند - است .4۳
ناچو ؟ - با جیم بواوکشیده » درخت ناخن آفتاب - کنایه از آش
کاج‌است وبمربی صنوبر خوانند . است -شاکنایه از ناخن مطلوب و شاهد هم
ناجود - بر وزن نابود , کاسه بز رکه | هت ۷ .
- وظرف شرابخوربراکوبند ‏ ناخن پال ۸ با بای فارسی بالف
ناخ ۴ - بروزن شاخ » بمعنی‌ناقف است | کشیده و بلام زده» ورمی باشد بسرخی مای ل که
که سوراخ وسط شکم باشد . بر اطراق ناخن مردم پدید آید ودرد بسیارکند
ناخاست ۴ - بروزن ناراست , کبرا | وآترا بعربی داح ی کوبند .
کوبند که از جای خود تتواند برخاست بمنی ناخن بد ند آن - بستی‌انگت‌بدندان-
۱-ظ . از برساخته های فرقةٌآذ رکیوان » ولی ترکیبی عجیب است , چه ۵ #اانبجام >
بمعنی بی‌پایان تواند باشد و در دساتیر (ص ۲۹۷ ) بمعنی « ابدالاباد بمتی روزی که آشها پدیر
نباعد از طرق متقبل » آورده » و« جز » زاید بنظن میرسد. ۴ ۳ باژوت با بو 4
پنتو نیز 84[0 « پلیو س۱۹۲ ۹ :
ناجوی این باغ بوجد و خروش بود چو سکان فلك سبزپوش -
نظامی گنجوی « جهانگیری > .
۴ - رك : ناف . ۴ - از : نا (نفی , سلب )4 خاست (از خاستن) بمعنی خیز
( خیزند ) - - از : با (* ناو [«م] خدا: (م.) هویشمان ۱۶۹۶ :
خدا کشتی آنجا که خواهد برد وگر ناخدا جامه بر تن درد -
سعدی شیرازی « امثال وحکم دهشدا >.
۹-« ناخن آفتاب یعنی آتش . خاقانی کوید :
چشم سهیل وناخنه ناخنآقتاب ونی کانش وقند او دهد با نی ویاد یاوری.
( ر3 : دبوان خاقانی شرواتی ص 2۲۷ ) .
اما درین بیت خاقانی بمعنی آتش نیست , بلکه ممنی آست که در چشم سهبل تاخاه می افتد »
با آنکه دیدن سهیل ناخنه را دفم کند و درناخن آفتاب - که عبارت از خطوط شماعی است -
تی‌می‌افتد » با آنکه نی در تاخن افتادن محالست وقت ی که‌آتش وقند تائی- بعنی سرخی وشیربنی
لب‌او - با نی نواختن وباد درآن دمیدن مشغول شود.» فرشیدی». رك:ناخنه. ۷ رك : رشیدی .
۸ - از : ناخن + یال ( پالودن بممنی افزون وزبادهگشتن ) (4) قس : ناخن‌خاره .
َ 2 ناخی - جم سوم * ناخون (ء.م.) , هندی باستان -281۳84 ( ناخن اسان » ناخن
حیوانات) ۰ پپلوی 23512 (بندهشن) ۰ افغانی 2۵16 , بلوچی88168 ۰ 22018 ۰ 22208
« اسشق ۰۶۱۹۱۹ کردی ع 823080 [ کردی اسیل : نین وکه] « ژابا ص 2۱۶ > پشتوع
2 بلیو س ۱۹۲ ؛ مادهٌ شاخ ی که در اههای انگشتان اسان وجانوران میروید :
چون نداری ناخن درنده تیز با ددان آن به ک هکم کیری ستیز .
۰ گلتان س ۹۳ ۰
```


## [2026-09-07T19:33:05.251Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" SNS_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'naxun', t):\n    s=t.rfind('[pdf page', 0, m.start())\n    print(t[s:s+20], '|', t[m.start()-120:m.start()+160].replace('\\n',' '))\nEOF"
}
```


## [2026-09-07T19:33:06.374Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 naz headword region ===\"\nsed -n '7195,7240p' incoming/BQT/BQT_v4_pages.txt\necho \"=== pdf page ===\"\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v4_pages.txt | awk -F: '$1<7200' | tail -2"
}
```


### [2026-09-07T19:33:06.660Z] TOOL RESULT

```
 |                                   wt^'                                                                            •O*^ :naxun:                        \*o-                                                                                   ^•               tfotw<2Z,158)n'xwn:^      
 | Li*.L y>   ^At tfl**;'* ^-vr» mahraanih 239/14             mazdist 241/17                     raiySnag 237/12           naxun 258/3 Mahraspand/Maraspand         raazdistan 241/20                  raizag 253/6              nSyrlg 264/19   240/8                      raazg     243/1
```


### [2026-09-07T19:33:07.942Z] TOOL RESULT

```
=== BQT v4 naz headword region ===
نه عجب کرچو خواجه حکم کند وی نکشد بار ناز چون بنده.
« کلتان س ۱۳۳ *.
- نسمت و رفاه وآسایش : « فی‌الجمله پر را بناز و نعمت برآوردند و استاد ادیب را بتربیت او
غصب کردند .>« کلتان ص ۲4-۲۳ *. ۸ <باز (همم.)
‎٩‏ < باژو (ه.م.) * باز * نوژ ( لفت فری اس ۱۷۶ ۳۲ نعك « لغت فری اس ۲۹۶
< نوژن (ه.م.) * نوج « جهانگیری »۳ 52۳0108 700106۲05 (۹۵۷106 7686۷167 قر)
که درختی‌است ازلوع صنوبر وسروه هرمزدنامه س ۱۹۱ ح ۱ » بعتی‌ناژرا همان عرعرداسته‌اند:
ر4: ایض ازین بیت‌منوچهری شاید استتباط شود که « ناژ » و «عرع » دو درخت ازیکنوع باشند:
توکویی بباغ اندر ۰ آتروژ ( بباغ اندرون » روز ) برف صف باز برد وف عرعران.
منوچهری دامغانی س ۹۱ * ۰
*- دخت خوارزم شاه نازپری کش (خوش) خرامی بسا ن كيك دری...
نظامی کنجوی در عنوان « دبدن بهرام صورت هفت پیکررا در خورلق ». رك : هفت پیکرص ۷۷
[pdf page 181]
بازد مها
نازگ ۱ - بنم ثاك و سکون کاف . گفته‌اند که بعربی سنور خوانند .3۴
معروف است وآنرا تنك هم میگوبند - وکنایه ناژ ۴ - با زای فارسی بواو کشیده .
از ممعوق ومطلوب وشاهد باشد . * .]| بممنی ناجو است که درخت صنویر باشد:.
ناز لگ پدن < بنتح باودالابجدوسکون ناه ۴ با زای فارسی بر وزن تازه »
نون »؛ فوعی از رستلی باشد شبیه بیستان افروز | ازبائٌ قیان راکویند -
لیکن سلقش سرخ وخوش رنگه میباشد ! وبعبی ناژین - بازای فارسی بر وزن آچین ۰
گوبند سرخ مرد همان است . درخت پشه‌غال راکوبند .8
ناز نوروز - بکر تاك و فح نون ناصازی * » با سین بی نقطه" و زای
و واو ساکن و رای بی لقطةٌ موم بواو و زای | نقطه‌دار بروزن آزادی , مخالفت وبی اصولی(٩)‏
نقطه‌دار زدء » نام نوابی است از موسیقی.#ه کردن وخارج مبحث بودن و بد وضمی باشد.
فا - بروزن مازو. نوعی ازطیورباشد؛ ناسپال ‎٩‏ « با بای قارسی‌پروژن پارسال»
و یی کویند قمری است ۲ - و گربه رانیز | پوست انار راکوبن د که نار پوست باشد .
() چش : بی اصول .
۹ - پپلوی 2821 « هوبشمان ۱۰۱۷ > . 28216 ( لطیف. ظربف ) از رمعهٌ «ناز».
شکل اخیر پپلوی تبدیل وگذشتی است از 8 به 1 . شاید بتوان بای 076/1۴ شکل 8۲/7۵/6
سباژطاژانطه ( آواز ‏ نوا) را تصورکرد. قس : آرمنی ع 8188 (آهنگه, اغمه. موسیقی).
از 083۷28 ۸« پیب رکه س ۱۵۵ * ؛ اففانی 53210 ۰ 232868 , 8687268 (عروسکه )
« عوبشمان ۱۰۱۷ ۰ بلوچی 88713۲1 . 8821 * اسشق ۱۶۱۷ > + کردی 8226 (ظریف)
‎٩ 825666 ۷‏ ژابا س 4۱4
۴ - نازیدن نازو وتواهای سر‌بچه ناطق کند آن مردة بی نطق وییان وا
« سنائی غزنوی ص ۲۳۰ .
۴ < ناجو " باز (ه.م.) ۴ - مصحف «* تاره » (ه.م.)
* - از : ناساز («.م.) ی ( اسم ممتی , حاصل مصدر ) .
۹ - ر4 : جهانگیری . این لفظ درهندی هم هست « فرهنکه نظام >.
< لارلیی - از : « باز) (هم.) [ رك : اسفق ۱۳۱۷] این (ین سبت ) [ قی :
بوزنینه ۳ بوزینه ] ؛ دارندة تاز - لطیف وظریف (ممشوق ) :
کر بر سر چشم ها قشینی نازت بکه م که نازلینی . «گلتان صس 4۰ 4.
لازیدن - بفتح دال , از : ناز (ه.م.) ۳ بدن ( پسوند مصدری ) رك : اسشق ۹۱۶۹۷
قی: آرمتی ع 8827-1-0 ( بنواز » نوازش کن ) « هوبشمان ۹۱*۹۷ ؛ نا زکردن » استغنالمودن,
تفاخی کردن ( برای شاهد رك : ح ۷ همین صفحه ) .
ناساز - از : نا ( نفی , سلب )۳ ساز (ساختن ) ؛ کردی 82-987 ۰ 132 (خشن ,
زمخت ) « ژابا ص 4۱4 > ؛ بی‌تناسب » نامتناسب +
=== pdf page ===
7110:[pdf page 179]
7169:[pdf page 180]
```


## [2026-09-07T19:33:23.193Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T19:33:23.201Z] TOOL RESULT

```


```


## [2026-09-07T19:33:26.442Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB naz/naxun ===\"\ngrep -n -i \"nāzuk\\|nazuk\\|nācuk\\|nacuk\\|nāxun\\|naxun\\|näzuk\\|nä%un\\|na%un\" HUB.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"nāzu\\|nazu\\|nāxu\\|naxu\" NYB_vol2_glossary.txt | head -20\necho \"=== ARY latin index naz ===\"\ngrep -n -i -E \"N[AĀ]Z|N[AĀ]XON|NAKHA\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T19:33:26.542Z] TOOL RESULT

```
=== HUB naz/naxun ===
3542:Afgh. nazuk (mit u) bei Raver ty; nazaka, nenzdka f.
7110:*) ^S^- p^irSyiS, pairayanda bei Yullers, naxun-pair&i 'anail-
=== NYB ===
465:Paz. anaxusmär; from ēšmār ‘number’, Paz. zuasmär (for xo$màr); MPrth 'šm?r (MHC). V. ošmurtan.
2655:nax®ist [nhwst'] the first 3512. 1114; adv. 1163. — MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuzust; sup. of the pre- ceding w. l
6053:nihuftan nm?e: naīnāc nmwdn, nm’y: nimütan nrm: *a-namr-tom nrysh-yzd: Narsah ns'h: nasāi nw(w)m: nahom nwx: Naxu-Ohurmazd nxwst: naxUist nym: nem nymrwz: nöm-röc nyrwg: nörök nyyšydn, nyyš-: murv- niš nzd: nazd nzdyk: nazdik
6357:anaxušmār: anösmär
6746:naxust: naxlist
=== ARY latin index naz ===
4127:over sHasens aabicail NAZE DANISH) S asl3
9519:REFERENCES behey NAZHIVU, ZHIJICI
11150:| OLD IRISH) 6 5439! SNAZ, SNACIDAN (PAHLAVI) 5 4
11541:POKORNY, —=~=~=~S*~S~«~SAL-NAZ”||©—KRRNATI, KART KRNOTI, KRTIS.
14286:NAGEL (SWEDISH) (gt yp NAXON (PAHLAVI) «5 gay
14287:NEGL s(NORWGIAN) $35 5 NAXONB (KURDISH) 53,5
14291:NOGOT RUSSIAN) «3 NAKHAS, A(SANSKRIT) 3 Sale
14292:NEHET HCZECH) Soy NAKHAM
14392:IMIE, NAZWA (POLISH) long!
14456:NAZDISHTA-, NAZDA- NAZDYO, ASNA — :(AVESTAN) plus!
14459:NAZD, NAZDIK (PAHLAVI) 5 1,
14462:DELAMARRE: (NEAR) 697, (NIGH) 704 NAZIK, NAZIX, NAZI :(BALUCHD) gx ss
```


## [2026-09-07T19:33:32.481Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14280,14300p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY_pages naxon ===\"\ngrep -n \"ناخن\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY_pages naz ===\"\ngrep -n \"^ناز\\|ناز \" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T19:33:32.558Z] TOOL RESULT

```
b22T Dk cay etl ile oly gal 9 a SOUL; 22 5p gg! Glew Glee
pe
[pdf page 490]
FL et
lady) cae jj -MANIC, MANIA (slas}ly -¥
[Mae tm cn |
NAGEL (SWEDISH) (gt yp NAXON (PAHLAVI) «5 gay
NEGL s(NORWGIAN) $35 5 NAXONB (KURDISH) 53,5
NAGEL (DUTCH) gale KAKUN, NAHUN, —(BALUCHI) x
HOLD CHURCH SLAVIC) 4S 5 3%! NAXUN
NocUT! : NUK HAFGHAND) (24), gli
NOGOT RUSSIAN) «3 NAKHAS, A(SANSKRIT) 3 Sale
NEHET HCZECH) Soy NAKHAM
NOGA {OLD BULGARIAN) oS 50 ONYX,ONYCHOS = (GREEK) by
NOKAT (SERBIAN) «9 po UNGUIS “ALATIN) oS
~ NEHET (BOHEMIAN) gas y ONGLE AFRENCH) ail
NECHT H{SLOVAR) joi UNA (SPANISH) giles!
NAGAS LITHUANIAN) gi 3 UNGHIA AUTALIAN) Adley
NAGAS LATVIAN) (.93),¢ 93 UNGHIE RUMANIAN) gles)
NAGE HOLD PRUSSIN) 45 gos. UNHA PORTUGUESE) Ji 5
INGEN, IONGA:(OLD IRISH) G4) p! GA-NAGLJAN GOTHIC) S36
=== ARY_pages naxon ===
559:قاعدتاً باید بتوان از طریق «پازسازی زبانشناخنی» (88007187717071001 113101119716) این
934:می‌شناخنند. پهلوی هم‌گذازی و همسنجی صدها واژه‌ی مشابه دیگر» دانشمندان را قاد رکرده است که
=== ARY_pages naz ===
7553:7 وناز ,۷۷0۸ ,2110۸ انگلیسی کهن (54/-ا۸0ظ 010): رید
```


## [2026-09-07T19:33:43.433Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"NAXON\\|GA-NAGLJAN\\|ONYX\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== try naz in ARY latin index ===\"\ngrep -n -E \"NAZ(UK|IK)|NAZ,|NAZIDAN|NAZ \\(\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T19:33:43.497Z] TOOL RESULT

```
=== try naz in ARY latin index ===
11150:| OLD IRISH) 6 5439! SNAZ, SNACIDAN (PAHLAVI) 5 4
14462:DELAMARRE: (NEAR) 697, (NIGH) 704 NAZIK, NAZIX, NAZI :(BALUCHD) gx ss
```


## [2026-09-07T19:33:45.558Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%AE%D9%86",
 "prompt": "Give the full Persian etymology section for ناخن (nāxon) 'nail': Middle Persian form, Proto-Iranian/Proto-Indo-Iranian/PIE reconstruction, cognates, and any cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


### [2026-09-07T19:33:53.783Z] TOOL RESULT

```
# Persian Etymology of ناخن (nāxon) 'nail'

**Proto-Indo-European Root:**
The word derives from PIE *[\*h₃nṓgʰs](/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83n%E1%B9%93g%CA%B0s).

**Descent Chain:**
The Wiktionary entry traces the development through "Proto-Indo-Iranian *[Hnā́kš](/wiki/Reconstruction:Proto-Indo-Iranian/Hn%C4%81%CC%81k%C5%A1), from Proto-Iranian *[Hnā́xš](/wiki/Reconstruction:Proto-Iranian/Hn%C4%81%CC%81x%C5%A1), and a derivative of *[Hnāxunah](/w/index.php?title=Reconstruction:Proto-Iranian/Hn%C4%81xunah&action=edit&redlink=1)."

**Cognates:**
The entry lists Indo-Iranian relatives including "Central Kurdish *[نینۆک](/wiki/%D9%86%DB%8C%D9%86%DB%86%DA%A9#Central_Kurdish)* (nînok), Northern Kurdish *[neynok](/wiki/neynok#Northern_Kurdish)*, Baluchi *[ناہن](/wiki/%D9%86%D8%A7%DB%81%D9%86#Baluchi)* (náhun), and Sanskrit *[न॒ख](/wiki/%E0%A4%A8%E0%A4%96#Sanskrit)* (nakhá)."

**Noted Limitation:**
The Wiktionary source provided does not cite specific authorities like Hasandust, MacKenzie, or Cheung, nor does it include Middle Persian forms.
```


## [2026-09-07T19:34:00.781Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B2",
 "prompt": "Give the full Persian etymology section for ناز (nāz) — any Middle Persian form, proposed origins, and cited authorities. Also any Etymology sections mentioning نازک."
}
```


## [2026-09-07T19:34:01.578Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nugae",
 "prompt": "Give the Latin etymology of nugae/nūgae 'trifles' — what origin is given, is it said to be of unknown origin, any mention of Greek or Old Latin nogae?"
}
```


### [2026-09-07T19:34:05.507Z] TOOL RESULT

```
# Etymology of *nūgae*

According to the Wiktionary entry, the origin of *nūgae* is **unknown**. The source states:

> "Unknown. Perhaps a borrowing from another Italic language, cognate with nux ("nut") and naucum ("nutshell, trifle")."

The entry does not mention Greek or Old Latin *nogae*. Instead, it suggests a possible connection to other Italic languages and proposes a relationship with Latin words for "nut" and "nutshell," which themselves may relate to the meaning of trifles or worthless things.
```


### [2026-09-07T19:34:05.632Z] TOOL RESULT

```
# Persian Etymology for ناز (nāz)

## Etymology 1

The word derives from **Parthian** *nʾz* (nāz, "pleasure, delight") or is inherited from **Middle Persian** [script needed] (*nʾz-* /nāz-/, "to take pleasure, to delight"). Both sources trace to **Proto-Iranian** *\*nāz-* ("to be coquettish").

As noted in the entry: "No Indo-European etymology per Cheung 2007."

A cognate appears in **Old Armenian** *նազիմ* (nazim), identified as an Iranian borrowing.

## Etymology 2

This represents a shortened form of *نازنین* (nâzanin), used colloquially as an adjective meaning "cute."

---

**Note:** The page contains no Etymology sections mentioning *نازک* (nāzak).
```


## [2026-09-07T19:34:24.318Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG naz ===\"\ngrep -n -i -E \"^\\*?n[aā]z|\\*nāz-|NAZ \" CHEUNG.txt | head -20\necho \"=== LEW/LAT nugae ===\"\ngrep -n -i \"nugae\\|nūgae\\|naucum\" LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-07T19:34:24.384Z] TOOL RESULT

```
=== CHEUNG naz ===
7930:naz(y)ard ‘to steep [of land, plants]’ 
18794:*naz 285 
18816:nazénd ut garténd (Dd 36.22), the first verb would contain the base näz-, naZ- ‘to 
18842:*naz ‘to take pleasure in, coquet; to be glorious, proud, delicate (< *‘to be soft, 
18866:naz-/naza ‘to caress’, NP пах ‘glory, glorification; pride; coquetry, playfulness; 
41194:naz, 286 
41195:nazan, 286 
41196:nazidan, 286 
43811:naz-/naza, 286 
52389:nazeli, 286 
52390:nazim, 286 
55011:nazi, 286 
55363:*naz 
55469:*naz 
55504:*naz, *uraz 
55514:*mraH, *naz (s.v.), *urad 
57945:*mraH, *naz (s.v.), *urad 
=== LEW/LAT nugae ===
LAT.txt:10591:populaires et obscurs: nugae, raudus, etc. Sans doute variations dia-
LAT.txt:11677:lupini. S'emploie comme hilum, naucum* M.L.1899. Emprunt au gr. xhxxoC
LAT.txt:18788:Pl., Asin.808, hae non sunt nugae, non enim mortualia. Enim est usite
LAT.txt:40541:naucus ou naucum, -I (nomin. non atteste): genitif seul employe
LAT.txt:40544:Le sens pr 4 cis du mot est inconnu. On lit dans Festus 166,11, naucum
LAT.txt:40607:plique. Ni le rapprochement avec naucum, ni celui avec nauis qu r indique
LAT.txt:42303:nugae ( nogae, naugae"?), -arum f.pl.: bagatelles, plaisanteries,
LAT.txt:42315:nugae, et que le mot ait 4 t 4 pris dans le sens imag 4 , comme naucus,
LAT.txt:42316:naucum (auquel il est joint par Ennius: illic nugator nili, non
LAT.txt:56351:farci"? Cf . raudus / rOdus / rudusnogae et nugae.
```


## [2026-09-07T19:34:25.723Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 onogh / nagal ===\"\ngrep -n -i \"onogh\\|nogh-\\|nagal\" incoming/WLD/WLD_Bd2_pages.txt | head -20\necho \"=== WLD band3 register ===\"\ngrep -n -i \"naxun\\|nakha\\|onogh\" WLD_band3.txt | head -10"
}
```


### [2026-09-07T19:34:25.793Z] TOOL RESULT

```
=== WLD Bd2 onogh / nagal ===
2252:setzung mit gr. nagal^ entscheidet nach Thurneysen Hdb. 451 f. die Syn-
21614:Abl. 130 mit aksl. nhzq ablautlich gleichgesetzt Yok. 98 auf nogh- zuriick-
=== WLD band3 register ===
```


## [2026-09-07T19:34:31.526Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG *naz ===\"\nsed -n '18840,18880p' CHEUNG.txt\necho \"=== which page? ===\"\ngrep -n \"\\[pdf page\" CHEUNG.txt | head -2"
}
```


### [2026-09-07T19:34:31.596Z] TOOL RESULT

```
=== CHEUNG *naz ===


*naz ‘to take pleasure in, coquet; to be glorious, proud, delicate (< *‘to be soft, 
mild, tender’ ?)’ 

*MIDDLE PERSIAN: MMP n’z- ‘to take pleasure, delight; exult, triumph’, BMP n’csn 
/nazisn/ ‘boasting; kindness’ 

Pres.: IND. 3р1. MMP n’zynd, n’zyynd, SUBJ. MMP 1р1. n’z’m; Partic.: pres. MMP n’z’g, pl. n’z’g’n 
*PARTHIAN: n’z- ‘to take pleasure, delight; exult, triumph’, n’z ‘pleasure, delight’ 


= Ghilain: 59 | DMMPP: 238b f. 
Pres.: IND. 3sg. n’zyd, 3pl. n’zynd, SUBJ. 3sg. n’z’h 


286 *раё 


*KHOTANESE: (+ *fra-) ? LKh. hanäys- ‘to be proud, delicate’. o The Khot. entry 
nasa- ‘tender, caressing’ in DKS: 180b is unconnected, on which see Emmerick, Fs 
Gignoux: 64; SVK Ш: 175. © SGS: – 

*SOGDIAN: BSogd. n’zwk’, MSogd. n’zwk ‘dear, beloved’ 

*NWIR: NP näzidan ‘to dissemble (as lovers); counterfeit, feign, coquet, etc.’, Gz. 
naz-/naza ‘to caress’, NP пах ‘glory, glorification; pride; coquetry, playfulness; 
delicacy’, NP nazan ‘sporting, toying (as lovers)’ 

*MISC: Arm. (LW) nazim ‘I act proudly, coquettishly, caress’, nazeli ‘lordly, 
worthy’, Georg. (LW) nazi ‘delicate beauty’ 

The root seems to be denominal: no IE etymology can be cited. 


*PIE— > LIV: — | Pok.: 
*REFERENCES: DKS: 180a, 451b; WIM II/1: 80; Gharib: 234 


*pat ‘to cook’ 

=== which page? ===
```


## [2026-09-07T19:34:32.531Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT nugae ===\"\nsed -n '42300,42325p' LAT.txt\necho \"=== WLD Bd1 p180 onogh ===\"\ngrep -n -i \"onogh\\|ongh-li\\|nogh-\" incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-07T19:34:32.609Z] TOOL RESULT

```
=== LAT nugae ===
la theorie fait difficulte. L'armenien meme, avec m- initial comme
dans la forme avestique, a un autre mot: merk, qui se laisse concilier
avec les precedents.
nugae ( nogae, naugae"?), -arum f.pl.: bagatelles, plaisanteries,
sottises, riens; nugas agere "plaisanter, perdre son temps". - Ancien
(Pl.), mot de la 1 . pariae, populaire ou familier, dont le forme est
mal fix 4 e.
Derives: nugor, - 5 ris; nugator,-trlx,-torius; nugSmenta (Apul ,), nugax,
nugacitas-, nugalis (tardif), M.L.SyOy, nugdlitas (Gloss.); nUg 5 ,-onis
(Apul.).
Composes plautiniens: nugi-uendus,-gerulus, -epiloquides (Per.703);
nugiparus (Gloss.).
Dans quelques dialectes italiens se trouve un representant d'un
deriv 4 nUglna, nogina, cf.M.L.syyo, qui a le sens de "p 4 pin de melon
cni de citrouille". II est possible que ce soit la le sens ancien de
nugae, et que le mot ait 4 t 4 pris dans le sens imag 4 , comme naucus,
naucum (auquel il est joint par Ennius: illic nugator nili, non
nauci st homo), hilum, etc.
Pas d' 4 tymologie,
nullus, -a, -um adj. et pron.: nui, aucun. De ne + ullus . Cf.
unus. Se substitue, des les plus anciens textes, a nemo a certains
cas, et tend a 1 'eliminer dans la langun pariae. Le neutre nullum
au sens de "aucune chose" est rare, la forme qui le remplace est
nihil (um), nll. S'emploie quelquefois en guise de n 4 gation renforc 4 e.
De meme que nullus sum veut dire " j e ne suis plus rien du tout, je
suis bien mort", nullus peut se joindre comme une sorte d'apposition
=== WLD Bd1 p180 onogh ===
16496:ISO                                        oner-       — onogh-      (   :   ongh-, nogh-                     ;
55556:     Nur in den Erweiterungen ghnegh- ghnogh- (auch ghndd(h)-l)                          :
```


## [2026-09-07T19:34:41.265Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16490,16560p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-07T19:34:41.314Z] TOOL RESULT

```
s.   1431).
     Vgl. weiter Fick I 4 17, 167, 372.                          Vielleicht       ist   wegen amld-h, amarus
amper eine eigene Wz. am-                  „bitter,          sauer“ anzusetzen.
     Walde, Etymologifcches Worterbuch. I.                                                        13
ISO                                        oner-       — onogh-      (   :   ongh-, nogh-                     ;
                                                                                                                      ngh-)


oner- „Traum“.
  Gr. ovag nom. acc. n. „Traum“ und Adv. „im                                                                      Traum“; dveigog             ,
                                                                                                                                                  - ov ,       aol.
dvotgog,    kret. avaigog(wohl durch Ass. aus *ovaigov, -cg) „Traum“, gen.
att. jon. dvdguzog ; arm. anurj „Traum“ (a- aus anl. o- wie z. B. in atnmn

„Zahn“, ateam „hasse“; -nr- aus -or-, so daft anur-j drag = zexfuog zex-                                                      :                            :




/Liag; -rj- aus -ri-, vgl. oveigog, *ovatgog  welcher i’o-St wohl auf Grund                ,


eines /-Lokativs *oneri, on e ri neben *onr, *onur entstanden ist. Ygl. Bar-
tholomae BB. 17, 103, IF. 2, 26S, Johansson BB. 18, 34; Hiibschmann Arm.
Gr. I 420, IF. 19, 476, wo gegen Pedersens KZ. 39, 405, auch Bartholomaes
Leugnung von r)aus ri) alb. gegh. ciders, tosk. endere „Traum“ (aber Gdf.
                                                   ;


*anrio-, alter *onrio-, G. Meyer Alb. Wb. 11, lautlich unmoglich).
   Der anl. Yokal wil'd durch dvag, oveigog als idg. o- bestimmt, da deren
ov- nicht als Aolismus fur dv- wahrscheinlicli zu machen ist.


oho- und ono-                        „schmiihen“.
   Gr. ovo/uai              „schelte,          tadle“,            dvozdg und (nach dvoooaodcu s. u.j dvooiog
„getadelt, tadelnswert“, ovozdCco „schelte, tadle“                                  mit -a- der zweiten Silbe     :




horn, covazo               und dvazai          •       djit/na^eiai. /le/ug erm                             Hes.        (s.       Bechtel Hauptprobl.
234, Persson Beitr. 669); mir. on ,,Schande‘ ? (Stokes Mel. Kern [RC. 24,
                                                                                                        :




21 7 1) vielleicht (Fickll 4 14, Pedersen KG. II 61) mit Red. -St. auch der
       ;



ersten Silbe    ir. mum   (/-St.) „Makel, Fehler“, acymr. anamou „mendae“,
                                                                                               11
ncymr. unaf, mbret. nnuff „Makel, Fehler                                                            .




   Aberlat. nota (s. Yf. LEWb. 2 m. Lit.) ist *gno-tu, s.gcn- „erkennen“. Uber
ahd. anndo usw. „Krankung“ s. u. an- „atmen“.
   Erw. (o)no-d- in ai. nd-nd-ati „schmaht. tadelt, verachtet", av. imdnito
„schmahende, lasternde" (s. auch u. n°.id- ,,heruntermachen“: ai. nadnt't
.,ertont, briillt, schreit“ ist wegen der Bed. fernzuhalten), gr. dvoooaotiut
usw., dvoozog (Osthoff Pf. 394 Anni. I, wo aber das Yerhaltnis zu dvo/iut
f-owie zu neid- „dveidog“ unrichtig beurteilt ist; Fick I 4 272).
```


## [2026-09-07T19:34:43.357Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dnw%2Fgala",
 "prompt": "Give the LSJ entry for νώγαλα / νώγαλον — meaning, attestations, and any related words (νωγαλεύω, νωγαλίζω)."
}
```


### [2026-09-07T19:34:48.479Z] TOOL RESULT

```
# LSJ Entry: νώγαλα

**Meaning:** The lexicon defines this as "dainties, sweetmeats, eaten after dinner, dessert," comparing it to τρωγάλια (similar confections).

**Attestations:** Two specific sources are cited:
- Antiphanes (fragment 65)
- Ephippus (fragment 24)

**Related Words:** The entry includes several related forms:
- νωγαλέος (adjective form)
- νωγάλευμα (a noun form)
- νωγαλεύω (verb: to eat sweetmeats)
- νωγαλίζω (verb form)
- νωγάλισμα (noun form)

The entry appears in the Liddell-Scott-Jones Greek-English Lexicon, revised edition (1940).
```


## [2026-09-07T19:34:55.487Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16560,16620p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-07T19:34:55.537Z] TOOL RESULT

```
ouogh-       ( :       ongh-, uogli-                    :   kelt.   ngh-)           Nagel an Fingern und Zehen‘‘.
                                                                                      ,.


      z.   T. mit           Formans                -u- (erw. -id-)                und do-, wie bei *<pp-ut-, -(ejln-
      „Kopf    -i
                       i
                       v
                           s.   Reichelt IvZ. 46, 336).
  Ai. dughri-                   m.
                   ,,FuC'‘ (vermutlich mit r aus l, *ouyhdi-); mit ar. Idi ai.
nukha- m. n., nnkhctru- m. n. „Nagel. Kralle“, np. nd.vun ds. (ar. kh- eher
eine noch aufzukliirende ar. Neuerung, als ins Idg. als Nebenform zuriick-
zuprojizieren, obwohl auch fiir die gr., lat. [?] und germ. Formen qh als
Grundlage erwogen wurde,s. Bezzenberger BB. 16, 257 f., Brugmann I 2 632j.
   Gr. dvi’i -e^o? „Nagel, Kralle“ (-e- wcist nicht auf labiovelaren Cha-
rakter des Gutturals, dem das Germ, widerspricht; s. Brugmann I 2 591> ;
ahd. nagid ags. ncegel „Nagel‘, aisl. nag! ds. ikons. St. geworden, PI.
                   ,



negl); negl vielleicht ursprgl. sg. /-St., vgl. ai. aughri-, und in paradigma-
tischer Yerb. mit dem o-St. *naglah nach dem Yorbild der kons. Deklina-
tion zum PI. umgedeutet, woran sich die weitere kons. Dekl. angliederte).
got. ganagljcin „annageln“.
  Lat. ungu-is „der                        Nagel an Fingern und Zehen",                                                       lingula ,,Klaue,             Huf.
spiiter    auch Nagel                  ‘
                                             (
                                               “ungui-la ?          oder          ((-loses *ongh-ie)la                               ,
                                                                                                                                         niiher   zu           ahd.
nagal ?);    air.          ingni       t..    Dat.          pi.   uignib     ,   n.        pi.              ingunt      ,
                                                                                                                            acymr. (gum, ncymr.
                                                            ong-   — onct-, nd-                                                   181


‘Win f., corn, cuiiin bret. iviu I'm. geworden) „Nagel“ l*uy]ni-tna, Thur-
                                            ,


neysen bei Brugmann II 332, besser Handbuch 127; -ii- formantisch wie in
lat. img-u-is   s. Osthoff IF. 4,272 f., Pedersen KG I 107; mir. inga mit
jiingerm Ubertritt zu den /i-Stammen, Pedersen KG. II 111); lit. nugas
„Nagel an Fingern und Zehen; Klaue bei Raubvogeln". lett. nags ds. lit.                                                       ;


naga ,Huf“, apr. nagc „Fu6“, abg. noga, russ. nogd ,,FuB“ (kollektive d-
Bildung, HirtlF. 10, 49: lit. nagittis, apr. nagutis „Fingernageb‘. abg. nogzfb,
russ. nugotb  Nagel, Kralle“.
                      ,,


   Das Wesentliche bei Curtius 32 It".          Audi arm. etunyn „Nagel an         —
Fingern oder Zehen. Klaue, Eisenhakeu“ i^Bugge Beitr. z. Erl. d. arm. Spr.
34, Meillet Rev. crit. 1S97, 3SS, Msl. 10. 2S0. Osthoff Par. I 278 ff.) scheint
hierher zu gehoren; Osthoff vermutet darin eine Zs. ef-ungcu „Horn-nagel“(Y                                                             .
```


## [2026-09-07T19:34:56.213Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nail",
 "prompt": "Give the full etymology of English \"nail\" (noun) — Old English form, Proto-Germanic reconstruction, PIE root, cognates cited."
}
```


### [2026-09-07T19:35:01.475Z] TOOL RESULT

```
# Etymology of English "Nail" (Noun)

**Old English Form:** *negel* (tapering metal pin) and *nægl* (fingernail)

**Proto-Germanic:** *\*naglaz*, which also produced Old Norse *nagl*, Old Saxon and Old High German *nagel*, Dutch *nagel*, and German *Nagel*

**PIE Root:** *\*(o)nogh*, meaning "nail of the finger or toe"

**Cognates:** The source document cites Greek *onyx* ("claw, fingernail"), Latin *unguis* ("fingernail, claw"), Old Church Slavonic *noga* ("foot") and *noguti* ("fingernail, claw"), Lithuanian *naga* ("hoof") and *nagutis* ("fingernail"), and Old Irish and Old Welsh forms meaning "fingernail, claw."

The document notes that "the 'fingernail' sense seems to be the original one," with the metal spike sense developing later and generating figurative expressions like "hard as nails" (1828) and "hit the nail on the head" (1520s).
```


## [2026-09-07T19:35:34.618Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 368 -l 368 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg368 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:35:36.246Z] TOOL RESULT

```
total 31688
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:35 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:35:36.793Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW nugae ===\"\ngrep -n -i \"nugae\\|nug&\\|nugor\" LEW_1910.txt | head\necho \"=== SKT nail ===\"\ngrep -n -i \"^Nail\\|NAIL,\" SKT.txt | head\necho \"=== POK_full nugae/nogala ===\"\ngrep -n -i \"nugae\\|nogala\\|nōgala\" POK_full.txt | head\necho \"=== greek dicts on disk ===\"\nls | grep -i -E \"frisk|beekes|greek|GRK|CHN\""
}
```


### [2026-09-07T19:35:36.881Z] TOOL RESULT

```
=== LEW nugae ===
=== SKT nail ===
466:Agnail,  (i^  a  sore  beside  the corn  on  lhe|  fool.  ^E.  ^  K.  — i worsts  appear  to  be  coiiFusctl A.  S.  angfur^J,  a  sore  by  ike  nail Leechdoms,  U.  81.  |  34),  with  wim Friesic  egtut'i,  on^qmii,  apparently  u a  i-imilar  senile:  lhi&  is  from  a  piclix fiignif\'ing  afiliciing,  paining,  and  *Mt/
3593:Clove  (0.  a  kind  of  spice.  ^F.  »  _ M.  E.  <hxv  (the  change  to  r/tftv.  in  the XVIib  cent.,  may  have  been  due  to  con fuiiion  with  Span.  r/<2T'o.)  — F.  clou,  a  nail ; chu  dt  girvpi,  *  a  clove/  Cot. :  from  the resemblance  to  a  nad.  Cf.  Span,  clavff^ nail,  also  a  dove.  —  L.  tiauum,  ace (iauHs,  a  nail.
3594:cloy.  (F.  —  L.)    Orig.  to  stop  up,  hence' sate-    O  F.  c foyer,  '  to  cloy,  slop  np,'  Cot. ; a  by  fonn  of  F.  doutr  {O.  F.  doer),  to  nail, fasten  up.     [A  horse  pricked  wilii  a  noil, in  shoeing,  wis  said  to  be  chyedJ^^O. eh,  F.  clou,  a  nail,  as  above. Clove  {i),  a  bulb;  see  Oleave  (i). Clover.  (E.>    M.E,  r/ar^r.   A.S.  da/re. trefoil. +  Dii.  khiver,   Swed.   klo/ver,  Dan. klUver,  G.Al/e.   ^  The  supposed  connection with  cleave  (i)  is  very  doubtful. Clown.  (Scand.)   led-  kiunni,  a  clumsy, boorish  fellow;  Swed.  diaL  klunn,  a  log. kiuHS,  a  clownish  fellow;  Dan.  klunf,  a log;  cf.  Dan.  kluntet,  clumsy.     Allied  to Clump.    The  orig.  sense  is  •  a  log.'     Sec Clumsy. Cloy  ;  sec  Clova  (i). Club  (i).  a  stick :  see  damp. Club  (i),  an  association  ;  see  Clamp Cluck-  (E.)    See  Clack. Clue  ;  see  Clew. Clump ;  see  Clamp. Clunuy.  (Scand.)    From  M.E.r/Mwx/i ciomsed,  benumbed ;  benumbed  fingers  are clumsy.    This  is  the  pp.  of  clomsen,  to  be- numb, or  to  feel  benumbed.  — Swed.  dial. klummun^   benumbed    (Kicti) ;    cf.   IceL klumsa,  lockjaw.     From   the  Teut.    base KLAM,    KRAM,  to   pinch,    whence  also Clamp.    Cramp.     Cf.    Du,    kUmmen,    to pinch.  •^/<'tf/ru-»,  to  be  betiumbed,  kleumsch^ numb  with  cold. Cluster,  a  bunch,    (E)      A.  S.  dtattr, clysUr,  a  bunch.     Allied  to  led   ilAstr^  a bunch,   klasi,  a  duster;  Dan.   and  Sw klau,  %  duster.     We  also  find  Swcil.  d klyi$e,  the  same  as  klifsa,  a  daslcr,  from klibba,  to  cleave,  stick  to.     This  links  it  to Cleave  (j). Clutch :  see  Latoh. 'Clutter  (I),  a  din ;  sec  Clatter. -Clutter  ^a),  to  clot ;  see  Olot. Clutter  (3>,  a  confuseil  heap;  to  hea up.  (W.)     W.  ^/JM^/,  a  heap,  pile;  cl\ einv.  to  heap  up ClysLer.  ^U-Gk.)    L.  cl/tfer,  *o
3656:ftikU^   a  snail,  allied  to
12074:nail  gap  in  a  hedge.  (F.) 'a  little  hole:*  Cot.  Dimio. '.  a  Kcrtt  comer.  —  F.  mujser, l&leh.  Hoot  unknown, (um^  iF  -L -Pe«. -Skt.) ace  of  tnusiui  » muthka,  a  testicle: •ma*  ot)l4if>ed  from  a  bag  be-
12136:.  xc  Onnw. V-,.,  lL.  -Gk.)  L. fa  of  jrafoj.  «Gk.  ycu6t,  a  water- He  ^tiv,  10  flow.  (*^SNU.) I)  M.  E.  war/.  A.  S.  ».r^^/.+ Dtn.  m^Vif,  Swcd.  Mrt^v/,  G !.  na^/,  the  human  nail,  na^li, spike,  p.  The  Tcut.  tjpc  is »c.  gnawer,  scratchcr,  or  piercer ; ',  Allied  to  Lithaon.  nagas^  a .  ncgpfr,  a  nail,  Skt  naJtAa, •),  nail  of  the  finger  or  toe t).  %  Kut  Ck.  Cvv(,  U  urt^is, k;  m  nail,  »ccm  to  come  from  a I  perhaps  a  variant  of  the  root
16640:Scimet&r,  Cimet&r.  (F.  pr  Ital.  - Ters.  ?)  F.  cim^Urt^,  *%  scj'mitar;'  Cot. Cf.  Ital.  fd'mifarm,  '»  simitar,'  Florio, Prob.  from  Pcrs.  sAimskfr,  sAamsklr,  "a cimeter.'  Rich.  Diet,  p.  009.  Lit.  lion's claw.  —  rers  jAam,  nail,  claw;  iM/r,  lion.
17552:Smack  (3),  a  fishing-boat  (Dil)  O Du.  imaeke,  Du.  smak,  a  smack,  hoy.4 Dan.  smakke.  Generally  thoiu;ht  to  stind for  snaek,  allied  to  snaJU\  cl.  A.  S.  i*^c, a  smack,  small  vessel ;  IceL  sntkk^  a smack,  so  named  from  its  snake-like  mottea in  the  water.  So  also  Dan.  snekl*  (i)  « snail,  (2)  a  vessel  or  smack.  Sec  Sttalu, Sne&k.
18077:Du.  sfijker,  a  nail,  Iccl.  s/>fkt  &c^  are  bor- rowed from  L.
18078:spigot.  (C.-LO  M.K  spigt>t,  A  prg for  a  cask.— 'Irish  and  Gael,  spiocaid,  a spigot  ;  dimin.  of  Trish  spitty  n  spike, long  nail,  peg.  Borrowed  from  L.  spUa (above).
=== POK_full nugae/nogala ===
=== greek dicts on disk ===
```


## [2026-09-07T19:35:45.949Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg368.png"
}
```


### [2026-09-07T19:35:46.385Z] TOOL RESULT

```

```


## [2026-09-07T19:35:46.383Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:36:19.112Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nhits=0\nfor f in sorted(glob.glob('page-3*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        nodes={n['id']:n for n in e.get('nodes',[])}\n        for n in e.get('nodes',[]):\n            pass\n    # simpler: search derivation text\nfor f in sorted(glob.glob('page-*.json')):\n    t=open(f,encoding='utf-8').read()\n    for m in re.finditer(r'not descend from Sanskrit|not from Sanskrit|sister|parallel reflex', t):\n        pass\nEOF\ngrep -l \"does not descend from Sanskrit\\|not descended from Sanskrit\\|not from Sanskrit\" page-*.json | head -5"
}
```


### [2026-09-07T19:36:20.948Z] TOOL RESULT

```
page-111.json
page-128.json
page-167.json
page-171.json
page-302.json
```


## [2026-09-07T19:36:24.628Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,re\nfor f in ['page-302.json','page-171.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if re.search(r'not (descend|descended|from) Sanskrit', n.get('derivation','')):\n                print(f, n['id'], n['lang'], n['verdict'])\n                print(n['derivation'][:700])\n                print('---')\nEOF"
}
```


### [2026-09-07T19:36:25.851Z] TOOL RESULT

```
page-171.json 7 Persian disputed
The word is real and belongs to this word-family, but not by the route drawn. New Persian قرمز qermez is a re-borrowing from Arabic قِرْمِز qirmiz (hence the qāf, impossible in an inherited Iranian word), and the Arabic itself came from Middle Iranian, not from Sanskrit: Wiktionary derives Arabic qirmiz from Persian *کرمست *kermest, ultimately Proto-Indo-Iranian *kŕ̥miš 'worm', 'whence also the inherited doublet کرم (kerm, "worm")'. So qermez is Persian's own word for 'worm' come home through Arabic — a classic Persian > Arabic > Persian round trip — and the Sanskrit form kṛmi-ja is at best a parallel Indo-Aryan formation, not the ancestor of the Persian word. Mo'in's own footnote in Borhān 
---
```


## [2026-09-07T19:36:32.315Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob\nfrom collections import Counter\nc=Counter(); ex=[]\nfor f in sorted(glob.glob('page-*.json')):\n    try: d=json.load(open(f))\n    except Exception: continue\n    for e in d.get('entries',[]):\n        nodes={n.get('id'):n for n in e.get('nodes',[])}\n        # need parent info; verification files may not carry parent. check\n        if e.get('nodes') and 'parent' in e['nodes'][0]: pass\n    break\nprint('has parent field?', 'parent' in json.load(open('page-316.json'))['entries'][0]['nodes'][0])\nEOF"
}
```


### [2026-09-07T19:36:33.525Z] TOOL RESULT

```
has parent field? False
```


## [2026-09-07T19:36:50.387Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD nazuk ===\"\ngrep -n -i \"n'zwk\\|nāzūk\\|nazuk\\|nʾzwk\" SOD.txt SOD_pages.txt | head -10\necho \"=== MON naz/naxon ===\"\ngrep -n \"ناخن\\|نازک\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T19:36:50.474Z] TOOL RESULT

```
=== SOD nazuk ===
SOD.txt:47006:5847  nVkk   S(AL)  **  n'zwkw 
SOD.txt:47018:5850  n'zwk^  B,  M  jJjb^jU 
SOD.txt:47019:nazuk  (n^kk) 
SOD_pages.txt:20464:                                                                           5847 nVkk S(AL) ** n'zwkw
SOD_pages.txt:20473:        5837 n'xyd C «# n>xy5      $                                       5850 n'zwk^ B, M                               jJjb^jU
SOD_pages.txt:20474:        5838 nV S                                                               nazuk (n^kk)
=== MON naz/naxon ===
MON_part1.txt:4480:مورق می کردد. و مفتول‌های سیار نازک از 
MON_part1.txt:5716:ورقه‌ای بسیار نازک از نقره یا جیوه رسوب 
MON_part1.txt:6252:زخمه بابه ناخن نوازند. (سد.) مطلق 
MON_part1.txt:6607:مخطط و راه راه» لطبف و نازک بافته و 
MON_part1.txt:9746:دیگر می بوشیدند. نوعی از قماش نازکك. 
MON_part1.txt:13544:عضوی به سر دو ناخن» چنانکه آن عضو به 
MON_part1.txt:16162:نازکتر» سبکتر. 
MON_part1.txt:16368:طرح و نمونه و روبری از چوب نازکث یا 
MON_part1.txt:16369:مقوا و کاغذ و یا پارچة نازک که از روی آن 
MON_part1.txt:22629:برگر دانیده. (ا.) کاغذ نازکی که یک روی
```


## [2026-09-07T19:36:56.624Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%AE%D9%86' --note 'page 368, root Nogh/Onogh, node 3: Persian ناخن from PIE *h3nogh-s via PIr *Hnaxunah (not from Sanskrit)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B2' --note 'page 368, root Nog/Snog, nodes 1-3: Persian ناز from Proto-Iranian *naz-; Cheung 2007 no IE etymology' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/nugae' --note 'page 368, root Nog/Snog, node 5: Latin nugae origin unknown, not a Greek loan' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/nail' --note 'page 368, root Nogh/Onogh, nodes 4-5: Germanic *naglaz, PIE *(o)nogh-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dnw%2Fgala' --note 'page 368, root Nog/Snog, node 4: LSJ nogala dainties, sweetmeats (Antiphanes fr.65, Ephippus fr.24)' 2>&1 | tail -3"
}
```


### [2026-09-07T19:37:00.073Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/343cafa30bcf5cf5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1f44a6eb8a2fe6d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ea434ae679fa360.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/834302654cc0915b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ef24ad8f2ab6315.txt
```


## [2026-09-07T19:37:07.652Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<20465' | tail -2\nsed -n '20460,20480p' SOD_pages.txt"
}
```


### [2026-09-07T19:37:09.092Z] TOOL RESULT

```
                                                                                 3sg. pres. n'zu TSP 2.292; Hen. Texts. 718; S W,
                                                                                   BSOAS 1983, 43
        5835 n>xwp M                                       x<c— UU
             na-xup
                                                                           5847 nVkk S(AL) ** n'zwkw
             not good                                                      5848 nVntk B                                .x^-ok/
             GMS 1156                                                           turning
                                                                                nazande
        5836 n*xy5     M                    (<**! <o^*j ijojb^jLAl
             naxiS (n'xyd) ©anahitd ©ob. -y; pr, name                           BSTBL, Dhy. 45, 55, 254, 401; Benv. Notesii 218;
             VcnusCtfar), Nahid (godess, Anahita)                                 GMS 1068
             BBB 724; GMS 269; C2, 12V 11, 12, 9                           5849 n'z'yny =* n'zyny
                                                                    ■)<
        5837 n'xyd C «# n>xy5      $                                       5850 n'zwk^ B, M                               jJjb^jU
        5838 nV S                                                               nazuk (n^kk)
             nc *=»ny                                                           delicate, dear
                                                                                VJ 64, 1387-, GMS 978; Gersh. JNES 1965, 183;
1?
```


## [2026-09-07T19:37:10.317Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83n%C3%B3g%CA%B0s",
 "prompt": "Give the reconstruction, meaning, and descendants for PIE *h₃nógʰs — including Proto-Germanic, Proto-Indo-Iranian, Greek, Latin, and Balto-Slavic reflexes, plus any cited sources (Pokorny, Kroonen, Beekes, de Vaan)."
}
```


### [2026-09-07T19:37:11.705Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T19:37:18.772Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83nog%CA%B0-",
 "prompt": "Give the reconstruction, meaning, and descendants for this PIE nail/claw root — Proto-Germanic, Proto-Indo-Iranian, Greek, Latin, Balto-Slavic reflexes and cited sources."
}
```


## [2026-09-07T19:37:20.720Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" SOD_pages.txt | head -2\npython3 - <<'EOF'\nimport re\nlines=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlast=None\nfor i,l in enumerate(lines[:20470]):\n    m=re.search(r'\\[pdf page (\\d+)\\]', l)\n    if m: last=(i+1,m.group(1))\nprint(last)\nEOF"
}
```


### [2026-09-07T19:37:24.080Z] TOOL RESULT

```
# Proto-Indo-European Nail/Claw Root

## Reconstruction
The PIE root is **\*h₃nṓgʰs** (masculine), meaning "nail (of the finger or toe)."

## Key Descendants

**Proto-Germanic:** \*naglaz (from \*h₃nógʰ-l̥)

**Proto-Indo-Iranian:** \*Hnā́kš

**Ancient Greek:** ὄνυξ (ónux)

**Latin:** unguis and ungula

**Balto-Slavic:** \*nágas (Lithuanian nãgas, Latvian nags)

## Cited Sources

Primary references include Mallory & Adams's *Oxford Introduction to Proto-Indo-European* (2006), Kroonen's *Etymological Dictionary of Proto-Germanic* (2013), De Vaan's *Etymological Dictionary of Latin* (2008), and Beekes's *Etymological Dictionary of Greek* (2010).

The entry documents multiple morphological derivations, showing how different Indo-European branches developed distinct forms from the original root through various suffixation patterns and phonological changes.
```


### [2026-09-07T19:37:25.379Z] TOOL RESULT

```
None
```


## [2026-09-07T19:37:46.147Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- WLD nugae/nogala ---\"; grep -c -i \"nugae\\|nogala\" incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt 2>/dev/null\necho \"--- POK nugae/nogala/whim ---\"; grep -c -i \"nugae\\|nogala\" POK_full.txt\necho \"--- AHD nugae/nogala/naz ---\"; grep -c -i \"nugae\\|nogala\" AHD_watkins1985.txt\necho \"--- BRT naz ---\"; grep -n -i \"nāz-\\|naz-\" BRT.txt | head -5\necho \"--- SYN nail page again nāxun quote ---\"; grep -c \"nazun\" SYN.txt\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83nog%CA%B0-' --note 'page 368, root Nogh/Onogh: PIE *h3nogws nail, PGmc *naglaz, PII *Hnaks' 2>&1 | tail -2"
}
```


### [2026-09-07T19:37:47.539Z] TOOL RESULT

```
--- WLD nugae/nogala ---
WLD_band3.txt:0
incoming/WLD/WLD_Bd2_pages.txt:0
incoming/WLD/WLD_Bd1_pages.txt:0
--- POK nugae/nogala/whim ---
0
--- AHD nugae/nogala/naz ---
0
--- BRT naz ---
4008:'  Eig.  'einen  Strom  von  Wasser  enthallend'f?),  | Ableit.  aus  'aatl-dänaz--  m. 11/V"  F.  J  h :  lies  a/r
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeitit^m  upa  vayoan»ni Auxmao%re  (sd.)  .  .  YL/4.13;  — para  te gaosp^nta  .  .  hao^asca  . .  *fraisyämaAi  naz- dista  upa  . .  raocä  . .  P.  34.  ß)  'bei, an':  ipanS yöi  hislmte  a:^arö  °pa  ^^anntjm V.  13.28;  —  tqm  yazata  ..  °pa  zrayi^ vouruJcaam  Ytf.iiö;  33,  38,  54,  72,  76, /2.16,  /5. 19,  27,  31';  —  *"/a  *mailUn (sd.)  barfsatiham  ^.3.20;  —  at-a  tu  anya mays  äitt  (sd.)  JasOit  .  .  paoirim  °pa mayiin  ..  tanüm  pairi.yaozdai^ita'^ .<).^\; 31',  Ö.38,  5.54;  —  minum  bara^ ..  aridvl
9389:•  j.  karsnaz-  m.  Name  einer  iranischen  masUtahe  V>.  10;  JÄ  44PUZ.  b)  'der Yz.TsM%\  yasmaoyö  parö  'nazS  {'^'2.)  hvira  geringfügigste':  yö  n��  matiltim  yasmm baon  sn-isfa  Yt.  13.  38.                                    yasäite  'titn  ^yasnat  frsyatät  (sd.)  Yt/.  24;
--- SYN nail page again nāxun quote ---
1
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-07T19:37:51.207Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83nog%CA%B0-' --note 'page 368, root Nogh/Onogh: PIE *h3nogws nail, PGmc *naglaz, PII *Hnaks' 2>&1 | tail -2"
}
```


### [2026-09-07T19:37:52.859Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f028074dfcb2ec85.txt
```


## [2026-09-07T19:37:57.637Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T19:37:57.691Z] TOOL RESULT

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


## [2026-09-07T19:39:18.025Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg368.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/368.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/368.png"
}
```


### [2026-09-07T19:39:18.098Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49419 Sep  7 15:39 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/368.png
```


## [2026-09-07T19:45:11.525Z] TOOL CALL #62: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk368.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_NAZ   = \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B2\"\nW_NAXON = \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%AE%D9%86\"\nW_NUGAE = \"https://en.wiktionary.org/wiki/nugae\"\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83nog%CA%B0-\"\nETY     = \"https://www.etymonline.com/word/nail\"\nLSJ     = \"https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dnw%2Fgala\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Nôğ, Snôğ\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"No Indo-European root of this shape is recognised in current scholarship. The box is a verbatim copy of S. E. Mann, IEC 848–849 '*nóg- (1) whim, triviality, fancy, dalliance, teasing, mockery' plus IEC 1236 '*snóg-, possible variant of type nóg-'. Modern Iranology reconstructs only Proto-Iranian *nāz- 'to take pleasure in, coquet' and denies it any IE ancestry (Cheung, Etymological Dictionary of the Iranian Verb, 2007, pp. 285–286, s.v. *naz: 'The root seems to be denominal: no IE etymology can be cited', with '*PIE — > LIV: — | Pok.: —').\",\n \"note\": \"The root box is faithfully copied from Nourai's source and the gloss is Mann's own wording word for word, so Nourai has not invented anything; the problem is that Mann's *nóg-/*snóg- is a private reconstruction that no other IE dictionary accepts. Pokorny has no such lemma (grep 'nugae|nogala' in POK_full.txt = 0 hits), nor do Walde–Pokorny (0 hits in WLD_Bd1/Bd2/band3) or Watkins/AHD (0 hits in AHD_watkins1985.txt). Mann himself hedges every limb of it: the Greek word is introduced with 'Gk. cf. nógala' and the parenthesis '(if not < *no, eno, and *ǵolok?)', the Iranian and Greek evidence is labelled 'Per. & Gk. ambig.', and Latin is admitted only conditionally — '(Lat. nugae \\\"trifles\\\" here only if dialectal for *nogae)'. Cheung 2007 and Wiktionary (after Cheung) state positively that the Iranian verb has no IE etymology, and Ernout–Meillet close their nugae article with 'Pas d'étymologie'. What survives is a solid Iranian family (Proto-Iranian *nāz- > Parthian and Middle Persian nāz- > NP ناز, نازیدن, نازک, Sogdian nāzuk, borrowed into Armenian nazim and Georgian nazi) and two unexplained European words that happen to begin with n-g. Note also two form errors in the lower branch: the Greek word is νώγαλα nṓgala, not 'nôgla' (node #4), and the Greek→Latin arrow reverses Mann, who makes Latin an independent branch (node #5).\",\n \"note_fa\": \"این ریشه از «فرهنگ تطبیقی هندواروپایی» استوارت مان (ص ۸۴۸–۸۴۹ و ۱۲۳۶) گرفته شده و معنای جعبه واژه‌به‌واژه ترجمهٔ همان است؛ اما *nóg-/*snóg- بازسازی شخصی مان است و در پوکورنی، والده‌پوکورنی و واتکینز هیچ مدخلی به این شکل وجود ندارد. مان خود نیز با احتیاط سخن گفته است: واژهٔ یونانی را با «cf.» و با تردید آورده و لاتینی nugae را تنها «اگر گونهٔ گویشی *nogae باشد» به این ریشه بسته است. چونگ (۲۰۰۷، ص ۲۸۵–۲۸۶) دربارهٔ ستاک ایرانی *nāz- صریح می‌گوید که «هیچ ریشه‌شناسی هندواروپایی برای آن نمی‌توان آورد» و ارنو–مِیه هم دربارهٔ nugae می‌نویسند «ریشه‌شناسی ندارد». پس آنچه استوار می‌ماند تنها خانوادهٔ ایرانی «ناز» است و ادعای هندواروپایی بودن ریشه را پژوهش امروزی رد می‌کند.\",\n \"sources\": [W_NAZ, W_NUGAE, LSJ],\n \"ref_check\": [\n   {\"ref\": \"IEC:848\", \"status\": \"supports\", \"note\": \"Mann, IEC leaf 474 (printed p. 849, running head 'ong- — onct-, nd-' with the page number 849 in the column): 'nóg- (1) \\\"whim, triviality, fancy, dalliance, teasing, mockery\\\" | Per. nāz \\\"flirtation, flattery\\\"; cf. nazuk \\\"flashy\\\"; nāzidan, inf. \\\"flirt\\\"; Gk. cf. nógala, npl. \\\"snacks\\\" (if not < *no, eno, and *ǵolok?); OLat. nogae, cpds. naug-, Class. nūgae \\\"trifles\\\"; Fris. noekje \\\"darling, favourite\\\"…' The lemma begins at the foot of printed p. 848 (leaf 473/474 boundary), so Nourai's page reference is right and his gloss is Mann's wording verbatim.\"},\n   {\"ref\": \"IEC:1236\", \"status\": \"partial\", \"note\": \"IEC leaf 682, printed p. 1236 (page number printed in the column, running head 'sneu- — snoiguhos'): 'snóg-, possible variant of type nóg-, q.v. Per. & Gk. ambig. Per. naz, s. \\\"flirtation\\\"; nazam, -idan, v. \\\"flirt\\\"; Gk. cf. nógala, npl. \\\"snacks\\\"; OE cf. snóca… (Lat. nugae \\\"trifles\\\" here only if dialectal for *nogae)'. The 'Snôğ' half of Nourai's box therefore exists, but Mann marks it only a 'possible variant' and calls the Iranian/Greek evidence 'ambig.', which Nourai's flat root box conceals.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, whole file\", \"stance\": \"silent\", \"note\": \"grep -i 'nugae|nogala' POK_full.txt returns 0 hits; Pokorny has no lemma meaning 'whim, triviality' with this shape (his nearest n-g lemmas are nogʷ- 'naked' 769 and onogh- 'nail' 780).\"},\n   {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt, WLD_Bd2_pages.txt, WLD_band3.txt\", \"stance\": \"silent\", \"note\": \"grep -ci 'nugae|nogala' = 0 in all three volumes of Walde–Pokorny; no such root.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"grep -ci 'nugae|nogala' = 0; Watkins' appendix has no root for these words.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 285–286 s.v. *naz\", \"stance\": \"contradicts\", \"note\": \"'*naz \\\"to take pleasure in, coquet; to be glorious, proud, delicate (< *\\\"to be soft, mild, tender\\\"?)\\\" … The root seems to be denominal: no IE etymology can be cited. *PIE— > LIV: — | Pok.: —' (CHEUNG.txt ll. 18842ff).\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. nugae\", \"stance\": \"contradicts\", \"note\": \"'nugae (nogae, naugae?), -arum f.pl.: bagatelles, plaisanteries, sottises, riens … mot de la langue parlée, populaire ou familier, dont la forme est mal fixée … Pas d'étymologie.' (LAT.txt ll. 42303–42317).\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1,\n   \"lang\": \"Old Iranian\",\n   \"words\": \"nâz\",\n   \"verdict\": \"disputed\",\n   \"derivation\": \"The FORM and the glosses are exactly right and exactly what Nourai's reference says: Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 77, s.v. نازیدن, writes «ناز < فارسی میانه nāz < ایرانی باستان *nāz-. nāz در ایرانی باستان اسم است به معنی «شادی»، «افتخار»» — 'in Old Iranian nāz is a noun meaning \\\"happiness\\\", \\\"pride\\\"', which is Nourai's 'nâz : happiness, pride' translated. Cheung 2007 pp. 285–286 sets up the same Iranian item as a (denominal) root *naz 'to take pleasure in, coquet; to be glorious, proud, delicate', with Middle Persian and Parthian nʾz-, Sogdian nʾzwk, and loans into Armenian (nazim) and Georgian (nazi). What is disputed is the ARROW, not the node: neither Abolghasemi nor Cheung takes the Old Iranian form any further back, and Cheung states explicitly that no IE etymology can be cited, so deriving Old Iranian *nāz- from Mann's *nōg-/*snōg- is Nourai's own step. Bartholomae's Altiranisches Wörterbuch has no Avestan root nāz- (the naz- strings in BRT are nazdišta- 'nearest' and the personal name Karsnaz-), so the reconstruction rests on Middle Iranian evidence projected back, which is legitimate as 'Old Iranian' but gives no PIE foothold.\",\n   \"derivation_fa\": \"شکل و معنای این گره درست است و همان است که مرجع خود نورایی می‌گوید: ابوالقاسمی در «ماده‌های ماضی و مضارع فعل‌های فارسی دری» ص ۷۷ ذیل «نازیدن» می‌نویسد «ناز < فارسی میانه nāz < ایرانی باستان *nāz-؛ nāz در ایرانی باستان اسم است به معنی شادی، افتخار». چونگ (۲۰۰۷) نیز ستاک ایرانی *naz «لذت بردن، نازیدن، سرافراز بودن» را با گواه فارسی میانه و پارتی nʾz- و سغدی nʾzwk بازسازی کرده است. اما پیوند این ستاک با ریشهٔ هندواروپایی *nōg-/*snōg- افزودهٔ نورایی است: چونگ صریحاً می‌گوید ریشه‌شناسی هندواروپایی برای آن نمی‌توان آورد و در «فرهنگ ایرانی باستان» بارتولومه نیز ریشهٔ اوستایی nāz- وجود ندارد. پس گره خودش پذیرفتنی است و تنها پیکان بالادست آن رد می‌شود.\",\n   \"sources\": [W_NAZ],\n   \"ref_check\": [\n     {\"ref\": \"FFD:77\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf page 82 (printed page number ۷۷ visible in the running head): «نازیدن — «نازید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. ناز < فارسی میانه nāz < ایرانی باستان *nāz-. nāz در ایرانی باستان اسم است به معنی «شادی»، «افتخار». nāz در فارسی میانه «شاد بودن»، «مفتخر بودن» معنی می‌دهد.» (grep 'نازیدن' incoming/FFD/FFD_pages.txt, l. 2096).\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"CHEUNG\", \"where\": \"pp. 285–286 s.v. *naz\", \"stance\": \"partial\", \"note\": \"Confirms the Iranian root ('*naz \\\"to take pleasure in, coquet; to be glorious, proud, delicate\\\"') but ends 'The root seems to be denominal: no IE etymology can be cited', i.e. supports the node and denies the arrow.\"},\n     {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, index of naz- strings\", \"stance\": \"silent\", \"note\": \"grep -i 'nāz-|naz-' BRT.txt yields only nazdišta-/nazdyō 'nearest' (col. ~1055) and the PN Karsnaz-; there is no Avestan root nāz-, so no Old Iranian attestation earlier than Middle Iranian.\"},\n     {\"src\": \"HRN\", \"where\": \"no. 1017, p. 228\", \"stance\": \"partial\", \"note\": \"Horn gives 'nāzuk … nāz \\\"Freude, Vergnügen; Ruhm\\\"' with Pahlavi nācuk and the Kurdish/Afghan/Baluchi loans, but offers no Old Iranian or IE preform.\"}\n   ]\n  },\n  {\n   \"id\": 2,\n   \"lang\": \"Pahlavi\",\n   \"words\": \"nâz; nâčuk\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Both Pahlavi forms are real and the Old Iranian > Middle Persian step is regular (no change: *nāz- > nāz-). For nāz Cheung 2007 p. 285 cites Manichaean Middle Persian nʾz- 'to take pleasure, delight; exult, triumph' (3pl. nʾzynd, subj. nʾzʾm, part. nʾzʾg) and Book Pahlavi nʾcšn /nāzišn/ 'boasting; kindness', plus Parthian nʾz- and the noun nʾz 'pleasure, delight'; Nourai's gloss 'to be happy' is Abolghasemi's «شاد بودن، مفتخر بودن», and his 'mince' renders the coquetry sense (to affect delicacy). For nâčuk: this is not a misreading but the Book Pahlavi spelling read letter for letter. MacKenzie's Concise Pahlavi Dictionary (p. 58) prints 'nāzuk [nʾcwk | (M nʾzwg), N —] tender, gentle; fickle', i.e. the Book Pahlavi script writes the /z/ of this word with the character conventionally transliterated ⟨c⟩, while the Manichaean script (which distinguishes them) writes ⟨nʾzwg⟩ = nāzug. Horn no. 1017 (p. 228) prints exactly 'phlv. nācuk', which is where Nourai got the shape, and Mo'in's footnote in Borhān-e Qāteʿ (vol. 4, printed p. 2098) says the same in Persian: «nāzuk (لطیف، ظریف) از ریشهٔ «ناز». شکل اخیر پهلوی تبدیل و گذشتی است از z به č». So the node is correct; the reading is nāzuk/nāzug and the -uk is the Middle Iranian adjective suffix (cf. Sogdian nʾzwk 'delicate, dear', Gharib no. 5850).\",\n   \"derivation_fa\": \"هر دو صورت پهلوی واقعی است و گذر از ایرانی باستان به فارسی میانه در اینجا بی‌دگرگونی است (*nāz- > nāz-). چونگ (ص ۲۸۵) برای «ناز» فارسی میانهٔ مانوی nʾz- «لذت بردن، شادمان بودن، بالیدن» و پهلوی کتابی nʾcšn /nāzišn/ «بالش، مهربانی» و پارتی nʾz- و نام nʾz «لذت» را می‌آورد. «nâčuk» نیز خطای خوانش نیست، بلکه حرف‌نویسی خط پهلویِ کتابی است: مکنزی (ص ۵۸) می‌نویسد «nāzuk [nʾcwk | (M nʾzwg)] لطیف، ملایم؛ دمدمی»، یعنی در خط پهلوی کتابی /z/ این واژه با حرفی نوشته می‌شود که به قرارداد ⟨c⟩ حرف‌نویسی می‌شود، در حالی که خط مانوی ⟨nʾzwg⟩ دارد. هرن (شمارهٔ ۱۰۱۷، ص ۲۲۸) هم عیناً «phlv. nācuk» چاپ کرده و معین در حاشیهٔ برهان قاطع (ج ۴، ص ۲۰۹۸) همین را می‌گوید: «nāzuk (لطیف، ظریف) از ریشهٔ «ناز»؛ شکل اخیر پهلوی تبدیل و گذشتی است از z به č». پس خوانش درست nāzuk/nāzug است و پسوند -uk پسوند صفت‌ساز ایرانی میانه است (قس سغدی nʾzwk «نازنین، عزیز»).\",\n   \"sources\": [W_NAZ],\n   \"ref_check\": [\n     {\"ref\": \"FFD:77\", \"status\": \"partial\", \"note\": \"FFD p. 77 (pdf page 82) supports only nāz: «nāz در فارسی میانه \\\"شاد بودن\\\"، \\\"مفتخر بودن\\\" معنی می‌دهد». Abolghasemi's book is a dictionary of verb stems and has no entry for nāzuk/nācuk, so the second word of this node is not covered by the reference Nourai cites for it.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 58 s.v. nāzuk\", \"stance\": \"supports\", \"note\": \"'nazuk [n)cwk l I (M n)zwg), N --] tender, gentle; fickle.' (PHD_mackenzie.txt l. 3696) — the ⟨nʾcwk⟩ spelling that Nourai transliterates 'nâčuk', with the Manichaean ⟨nʾzwg⟩ showing the reading is nāzuk.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"pp. 285–286 s.v. *naz\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: MMP nʾz- \\\"to take pleasure, delight; exult, triumph\\\", BMP nʾcsn /nazisn/ \\\"boasting; kindness\\\" … *PARTHIAN: nʾz- … nʾz \\\"pleasure, delight\\\"'.\"},\n     {\"src\": \"SOD\", \"where\": \"Gharib no. 5850\", \"stance\": \"supports\", \"note\": \"'5850 nʾzwk B, M — nazuk … delicate, dear | VJ 64, 1387; GMS 978; Gersh. JNES 1965, 183' (SOD.txt ll. 47018–19): the same -uk adjective in Buddhist and Manichaean Sogdian, confirming it is Middle Iranian and not a New Persian formation.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep -i 'nāzu|nazu' NYB_vol2_glossary.txt = 0 hits; the word does not occur in Nyberg's selected texts (his n-entries jump from naxwist to nazd/nazdik).\"}\n   ]\n  },\n  {\n   \"id\": 3,\n   \"lang\": \"Persian\",\n   \"words\": \"nâz «ناز»; nâzok «نازک»\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"New Persian ناز nāz 'coquetry, affected manners, pride' and نازک nāzok/nāzuk 'thin, delicate' continue Middle Persian nāz and nāzuk directly, with no sound change beyond the ordinary New Persian shortening of final -uk to -ok in modern pronunciation; the verb نازیدن nāzīdan and the participial نازنین nāzanīn (the two words Nourai adds in the box) are New Persian denominal formations on the same stem (نازیدن = ناز + پسوند مصدری -īdan). Both of Nourai's cited pages say exactly this. Horn no. 1017, p. 228: 'nāzuk \\\"zierlich, lieblich, zart\\\", nāz \\\"Freude, Vergnügen; Ruhm\\\", nāzīden, nāznīn … phlv. nācuk' — Nourai's glosses and even his two extra words come straight from that line. FFD p. 77 gives ناز < MP nāz < Old Iranian *nāz-. Mo'in's footnote at Borhān-e Qāteʿ vol. 4 p. 2098 adds the comparative material: «پهلوی nāz «هوبشمان ۱۰۱۷»، nāzuk (لطیف، ظریف) از ریشهٔ «ناز» … افغانی nāzuk، بلوچی nāzuk، nāz، کردی nāzik (ظریف)» and, s.v. نازیدن, «از: ناز + یدن (پسوند مصدری) … قس آرمنی naz-el». Cheung 2007 lists NP nāz 'glory, glorification; pride; coquetry, playfulness; delicacy', nāzidan and nāzan under the same Iranian root. Saʿeb's couplet in the box («نازی که داشتم به پدر چون عزیز مصر…») uses ناز in exactly the sense given.\",\n   \"derivation_fa\": \"«ناز» و «نازک» فارسی نو مستقیماً ادامهٔ nāz و nāzuk فارسی میانه‌اند و جز کوتاه‌شدن -uk پایانی به -ok در تلفظ امروزی دگرگونی آوایی دیگری رخ نداده است؛ «نازیدن» و «نازنین» هم ساخته‌های فارسی نو بر همان ستاک‌اند (ناز + پسوند مصدری -یدن). هر دو مرجع نورایی همین را می‌گویند: هرن (شمارهٔ ۱۰۱۷، ص ۲۲۸) می‌نویسد «nāzuk «زیبا، دلپذیر، نازک»، nāz «شادی، خوشی؛ افتخار»، nāzīden، nāznīn … پهلوی nācuk» — یعنی حتی دو واژهٔ افزودهٔ جعبه هم از همین سطر آمده است. معین در حاشیهٔ برهان قاطع (ج ۴، ص ۲۰۹۸) پهلوی nāz و nāzuk و همتاهای افغانی، بلوچی و کردی را می‌آورد و ذیل «نازیدن» می‌نویسد «از: ناز + یدن (پسوند مصدری)». ادعای نورایی در این گره درست است.\",\n   \"sources\": [W_NAZ],\n   \"ref_check\": [\n     {\"ref\": \"FFD:77\", \"status\": \"supports\", \"note\": \"FFD p. 77 (pdf page 82): «ناز < فارسی میانه nāz < ایرانی باستان *nāz-» under the headword نازیدن — supports ناز/نازیدن but says nothing about نازک.\"},\n     {\"ref\": \"HRN:228\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 250 = printed p. 228 (the leaf opens '— 228 —'), no. 1017: 'nāzuk \\\"zierlich, lieblich, zart\\\", nāz \\\"Freude, Vergnügen; Ruhm\\\", nāzīden, nāznīn … phlv. nācuk. LW. kurd. nāzik; afγ. nāzak, vergl. *nāzaka; bel. nāzurk, n. nāzuk.' Every word in Nourai's box, including the two he adds in parentheses, is on this page.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ ed. Moʿin, vol. 4, printed p. 2098 (BQT_v4_pages.txt pdf page 181)\", \"stance\": \"supports\", \"note\": \"Moʿin's footnote: «پهلوی nāz «هوبشمان ۱۰۱۷»، nāzuk (لطیف، ظریف) از ریشهٔ «ناز». شکل اخیر پهلوی تبدیل و گذشتی است از z به č … افغانی nāzuk … بلوچی nāzuk، nāz … کردی nāzik (ظریف)»; s.v. نازیدن: «از: ناز (ه.م.) + یدن (پسوند مصدری) … قس: آرمنی naz-el (بنواز، نوازش کن)».\"},\n     {\"src\": \"CHEUNG\", \"where\": \"pp. 285–286 s.v. *naz\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP nāzidan \\\"to dissemble (as lovers); counterfeit, feign, coquet\\\", Gz. naz-/naza \\\"to caress\\\", NP nāz \\\"glory, glorification; pride; coquetry, playfulness; delicacy\\\", NP nazan \\\"sporting, toying (as lovers)\\\"'.\"},\n     {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\", \"note\": \"The local Moʿin OCR is partial and carries no ناز/نازک headword (grep 'نازک' finds only definitions of other words that use it, ll. 4480, 6607, 16368…); Moʿin's etymology was read instead in his own footnotes to Borhān (above).\"}\n   ]\n  },\n  {\n   \"id\": 4,\n   \"lang\": \"Greek\",\n   \"words\": \"nôgla\",\n   \"verdict\": \"transcription_suspect\",\n   \"derivation\": \"The Greek word exists but not in this shape: it is νώγαλα nṓgala (n. pl.; sg. νώγαλον), glossed by LSJ 'dainties, sweetmeats, eaten after dinner, dessert', cf. τρωγάλια, attested in fourth-century Middle Comedy (Antiphanes fr. 65, Ephippus fr. 24) with the derivatives νωγαλέος, νωγάλευμα, νωγαλεύω, νωγαλίζω 'to nibble sweetmeats'. Nourai's source has it right — Mann prints 'Gk. cf. nógala, npl. \\\"snacks\\\"' at both IEC 849 and IEC 1236 — so the printed 'nôgla' has lost the second -a-; the printed page (368) shows 'nôgla' plainly, i.e. this is the book's own misprint and the extraction is faithful. Beyond the misspelling the derivation is also unsupported: Mann himself flags the word with 'cf.' and the parenthesis '(if not < *no, eno, and *ǵolok?)', Pokorny/Walde–Pokorny/Watkins do not connect it to anything, and no source bridges 'dessert' to Iranian 'coquetry'. The root→Greek arrow should therefore be read as disputed as well as misprinted.\",\n   \"derivation_fa\": \"واژهٔ یونانی وجود دارد اما به این شکل نه: صورت درست νώγαλα (nṓgala، جمع؛ مفرد νώγαλον) است که لیدل–اسکات آن را «شیرینی و تنقّلاتِ پس از شام، دسر» معنی کرده و در کمدی میانهٔ سدهٔ چهارم پیش از میلاد (آنتیفانس قطعهٔ ۶۵، افیپوس قطعهٔ ۲۴) گواه دارد، با مشتقاتی چون νωγαλεύω. مرجع خود نورایی، یعنی مان، در هر دو صفحهٔ ۸۴۹ و ۱۲۳۶ «nógala» نوشته است؛ پس افتادن یک «a» خطای چاپی کتاب است و خوانش اسکن درست انجام شده (تصویر ص ۳۶۸ روشن «nôgla» را نشان می‌دهد). گذشته از این، پیوند معنایی «دسر» با «ناز» ایرانی نیز پشتوانه‌ای ندارد: مان خود آن را با «cf.» و با تردید آورده و پوکورنی و واتکینز اصلاً چنین پیوندی نمی‌شناسند. یعنی هم خطای چاپی کتاب است و هم پیکانِ ریشه به یونانی پذیرفتنی نیست.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"nôgla\",\n   \"correct_form\": \"nôgala (Gk. νώγαλα nṓgala 'dainties, sweetmeats')\",\n   \"sources\": [LSJ],\n   \"ref_check\": [\n     {\"ref\": \"IEC:848\", \"status\": \"partial\", \"note\": \"IEC printed p. 849 (leaf 474) has 'Gk. cf. nógala, npl. \\\"snacks\\\"' — the gloss 'snacks' is Mann's word, but the form is nógala, not nôgla, and Mann adds '(if not < *no, eno, and *ǵolok?)', i.e. he does not commit to the connection.\"},\n     {\"ref\": \"IEC:1236\", \"status\": \"partial\", \"note\": \"IEC printed p. 1236 (leaf 682) s.v. snóg-: 'Per. & Gk. ambig. … Gk. cf. nógala, npl. \\\"snacks\\\"' — again nógala, and 'ambig.' is Mann's own warning about this very Iranian–Greek equation.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\", \"note\": \"grep -i 'nogala' = 0 hits; Pokorny nowhere lists νώγαλα.\"},\n     {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt / WLD_Bd2_pages.txt\", \"stance\": \"silent\", \"note\": \"grep -ci 'nogala' = 0 in both volumes.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"no section on sweetmeats/dainties that would list νώγαλα; grep 'nogala' SYN.txt = 0 hits.\"}\n   ]\n  },\n  {\n   \"id\": 5,\n   \"lang\": \"Latin\",\n   \"words\": \"nŭgae, nôgae\",\n   \"verdict\": \"disputed\",\n   \"derivation\": \"The two Latin forms are genuine and correctly paired: Ernout–Meillet head the article 'nugae (nogae, naugae?), -arum f.pl.: bagatelles, plaisanteries, sottises, riens', note it is old (Plautus, Asin. 808 'hae non sunt nugae') and 'mot de la langue parlée, populaire ou familier, dont la forme est mal fixée' (they compare the same wobble in raudus/rōdus/rudus ~ nogae/nugae), and list the derivatives nugor, nugator, nugax, nugalis and Plautus' compounds nugiuendus, nugigerulus. But the ARROW is wrong twice over. (a) Historically: nūgae is not a Greek loan. No Latin etymological dictionary derives it from νώγαλα; Greek -αλ- would not yield Latin -ū-/-o- with loss of the syllable, and a colloquial Plautine word of unstable shape is not the profile of a fifth/fourth-century Greek borrowing. Ernout–Meillet end 'Pas d'étymologie'; Wiktionary (following the standard Latin handbooks) says 'Unknown. Perhaps a borrowing from another Italic language, cognate with nux (\\\"nut\\\") and naucum (\\\"nutshell, trifle\\\")' — the same guess Ernout–Meillet float, resting on Ennius' pairing 'illic nugator nili, non nauci st homo' and on the Italian dialect derivative nugīna/nogīna 'melon or pumpkin seed'. (b) Even Nourai's own source contradicts the arrow: at IEC 849 Mann lists 'OLat. nogae, cpds. naug-, Class. nūgae \\\"trifles\\\"' as an independent branch of *nóg-, parallel to (not descended from) the Greek word, and at IEC 1236 he restricts it further — '(Lat. nugae \\\"trifles\\\" here only if dialectal for *nogae)'.\",\n   \"derivation_fa\": \"دو صورت لاتینی درست و درست جفت‌شده‌اند: ارنو–مِیه مدخل را «nugae (nogae, naugae؟)، جمع مؤنث: چیزهای بی‌ارزش، شوخی، بیهوده» می‌آورند، آن را واژه‌ای کهن و «از زبان گفتار، عامیانه یا خودمانی که شکلش استوار نشده» می‌خوانند و مشتقات nugor، nugator، nugax را برمی‌شمارند. اما پیکان یونانی → لاتینی از دو جهت نادرست است: نخست آنکه هیچ فرهنگ ریشه‌شناسی لاتین nūgae را وام‌واژهٔ یونانی νώγαλα نمی‌داند و ارنو–مِیه با صراحت می‌نویسند «ریشه‌شناسی ندارد»؛ ویکی‌واژه هم می‌گوید «نامعلوم؛ شاید وام از زبانی ایتالیک دیگر، هم‌ریشه با nux «گردو، آجیل» و naucum «پوست گردو، چیز بی‌ارزش»». دوم آنکه حتی مان، مرجع خود نورایی، لاتینی را شاخهٔ مستقل ریشه می‌گیرد («لاتینی کهن nogae … کلاسیک nūgae») و در ص ۱۲۳۶ می‌افزاید «nugae لاتینی تنها در صورتی به این ریشه می‌خورد که گونهٔ گویشیِ *nogae باشد». پس پژوهش امروزی این پیکان را رد می‌کند.\",\n   \"sources\": [W_NUGAE],\n   \"ref_check\": [\n     {\"ref\": \"IEC:848\", \"status\": \"partial\", \"note\": \"IEC printed p. 849 (leaf 474) s.v. nóg- (1): 'OLat. nogae, cpds. naug-, Class. nūgae \\\"trifles\\\"'. The page gives Nourai both of his forms and their gloss, but as a Latin branch of the root — not as a loan from Greek, which is what the chart's arrow says.\"},\n     {\"ref\": \"IEC:1236\", \"status\": \"contradicts\", \"note\": \"IEC printed p. 1236 (leaf 682) s.v. snóg-: '(Lat. nugae \\\"trifles\\\" here only if dialectal for *nogae)'. Mann attaches the Latin word conditionally and never routes it through Greek.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. nugae (LAT.txt ll. 42303–42317)\", \"stance\": \"contradicts\", \"note\": \"'nugae (nogae, naugae?) … mot de la langue parlée, populaire ou familier, dont la forme est mal fixée … Il est possible que ce soit là le sens ancien de nugae, et que le mot ait été pris dans le sens imagé, comme naucus, naucum (auquel il est joint par Ennius: illic nugator nili, non nauci st homo) … Pas d'étymologie.' Cf. also LAT.txt l. 56351 'raudus / rōdus / rudus — nogae et nugae' on the vowel wobble.\"},\n     {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'nugae|nugor' LEW_1910.txt = 0 hits; the n- fascicle is missing/illegible in this OCR, so Walde could not be consulted here.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein, s.v. nugatory/nugae\", \"stance\": \"silent\", \"note\": \"grep -i 'nugae' KLN_1966.txt returns no etymology tying nugae to Greek; Klein has no entry deriving the Latin word from νώγαλα.\"}\n   ]\n  }\n ]\n}\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Nogh, Onogh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₃nṓgʰs / *h₃nogʰ- 'nail (of finger or toe), claw' (Pokorny 780 'onogh-: ongh-, nogh-, Celtic ọgh-, ongh-li- (*h₃uen(e)gh-)', meaning 'fingernail, claw'; Watkins/AHD 'nogh-. Also enogh-, ongh-. Nail, claw')\",\n \"note\": \"Root, language label, gloss and even the two shapes 'Nogh, Onogh' are all correct and are Pokorny's own lemma title on the very page Nourai cites (p. 780). Both branches drawn from the root are the standard ones: the Indo-Iranian *nakha-/nāxun- group and the Germanic l-suffixed *nagla- group. The one structural fault on the chart is the Sanskrit → Pahlavi arrow (node #2): Pahlavi nāxun is a sister of Sanskrit nakhá-, not its descendant. Also note that the -kh- of the Indo-Iranian words is not the regular reflex of PIE *-gʰ-: Pokorny calls it 'an innovation', Walde–Pokorny 'eine noch aufzuklärende ar. Neuerung', Buck 'unexplained kh for gh' and Klein guesses at 'Caucasian influence' — a caveat Nourai's flat arrow hides. Modern reconstruction adds the initial laryngeal (*h₃-, whence Greek ὄ-νυξ and Latin u-nguis), which is exactly the alternation Pokorny wrote as onogh- ~ nogh-.\",\n \"note_fa\": \"ریشه، برچسب زبان، معنا و حتی هر دو صورت «Nogh, Onogh» درست است و عیناً عنوان مدخل پوکورنی در همان صفحه‌ای است که نورایی ارجاع داده (ص ۷۸۰): «onogh-: ongh-, nogh- … معنا: ناخن، چنگال». هر دو شاخهٔ رسم‌شده هم شاخه‌های شناخته‌شده‌اند: گروه هندوایرانی nakha-/nāxun و گروه ژرمنی با پسوند -l یعنی *nagla-. تنها ایراد ساختاری این نمودار پیکان «سنسکریت ← پهلوی» است (گرهٔ ۲): nāxun پهلوی خواهرِ nakhá سنسکریت است، نه فرزند آن. نکتهٔ دیگر آنکه kh هندوایرانی بازتاب قاعده‌مند *gʰ هندواروپایی نیست؛ پوکورنی آن را «نوآوری» و والده‌پوکورنی «نوآوری آریایی که هنوز توضیح داده نشده» می‌خواند و باک آن را «kh بی‌توضیح در برابر gh» می‌نامد. بازسازی امروزی حنجره‌ای آغازی *h₃- را نیز می‌افزاید که همان تناوب onogh- ~ nogh- پوکورنی است.\",\n \"sources\": [W_PIE, W_NAXON, ETY],\n \"ref_check\": [\n   {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"POK_full.txt ll. 63942–63997: 'Root / lemma: onogh-: ongh-, nogh-, Celtic ọgh-, ongh-li- (*h₃uen(e)gh-) | Meaning: fingernail, claw | Note: partly with formants -u- (extended -ut-) and -lo- | Material: … Old Indic nakham n., nakhara-m n. \\\"nail, claw, talon\\\", np. naxun ds. (Aryan kh- an innovation) … gr. ὄνυξ, -υχος … Latin unguis … Old High German nagal, Old English nægel \\\"nail\\\", Old Icelandic nagl … Gothic ga-nagljan \\\"nail\\\" … References: WP. I 180 f., Trautmann 192 … Page(s): 780'. The printed page tag 'Page(s): 780' confirms Nourai's citation exactly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde–Pokorny Bd. I pp. 180–181\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt ll. 16496, 16560ff: header '180 oner- — onogh- (: ongh-, nogh-; ngh-)' then 'onogh- (: ongh-, nogh-; kelt. ngh-) \\\"Nagel an Fingern und Zehen\\\", z. T. mit Formans -u- (erw. -ut-) und -lo- … ai. nakha- m. n., nakharu- \\\"Nagel, Kralle\\\", np. nāxun ds. (ar. kh- eher eine noch aufzuklärende ar. Neuerung…) … ahd. nagal, ags. nægel \\\"Nagel\\\", aisl. nagl … got. ganagljan \\\"annageln\\\". Lat. unguis…' — the source Pokorny abbreviates as 'WP. I 180 f.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nogh-\", \"stance\": \"supports\", \"note\": \"'nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-elo- in Germanic *nagla- in Old English nægl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX … 3. Variant form *ongh- in Latin unguis … [Pok. onogh- 780.]' (AHD_watkins1985.txt l. 787).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.39 NAIL, printed p. 245 (SYN.txt leaf 282, page number 245 printed in the leaf)\", \"stance\": \"supports\", \"note\": \"'4.39 NAIL … *(o)nogh- (with wide variation of … suffixes in different IE languages). Walde-P. 1.180 f. … all the words listed except Av. sri, srvā …, but represented in Iranian by NPers. nāxun (Skt. also nakha-, with unexplained kh for gh).'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. nail, n.\", \"stance\": \"supports\", \"note\": \"'nail, n. … ME. naile, neil, fr. OE. nægl, nægel, \\\"fingernail; metal nail, peg\\\" … fr. I.-E. base *nogho-, *ngho-, *ongho-, \\\"nail\\\", whence also OI. aṅghriḥ … Gk. ὄνυξ, L. unguis … Cp. OI. nakháḥ, Pers. naxun, \\\"nail, claw\\\", where qh- (for gh-) is prob. due to Caucasian influence.' (KLN_1966.txt l. 24913).\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1,\n   \"lang\": \"Sanskrit\",\n   \"words\": \"nakhâ, naxâ\",\n   \"verdict\": \"plausible\",\n   \"derivation\": \"Sanskrit नख nakhá- (neuter, nom. nakhám; also nakhara-) 'nail, claw, talon' is genuine and descends from the root as drawn, via Proto-Indo-Iranian *Hnā́kš / *Hnakha- from PIE *h₃nṓgʰs; Pokorny prints it on the cited page ('Old Indic nakham n., nakhara-m n. \\\"nail, claw, talon\\\", np. naxun ds.'). Two reservations. (1) The -kh- is not the regular Indo-Iranian reflex of PIE *-gʰ-, which should give -h-; every authority flags this: Pokorny '(Aryan kh- an innovation)', Walde–Pokorny 'ar. kh- eher eine noch aufzuklärende ar. Neuerung, als ins Idg. als Nebenform zurückzuprojizieren', Buck 4.39 '(Skt. also nakha-, with unexplained kh for gh)', Klein 'where qh- (for gh-) is prob. due to Caucasian influence'. So the arrow is right but not phonetically regular, which the chart does not say. (2) 'naxâ' is not a Sanskrit form — Sanskrit has no /x/ phoneme and no lexeme naxā; it is Nourai's own x-for-kh respelling of the same word (a habit of his throughout the book, aligning the Indic form visually with Persian nāxon), and the final -â in both spellings misrepresents an -a stem whose nominative is nakhám. The printed page 368 does show 'nakhâ, naxâ', so the extraction is faithful.\",\n   \"derivation_fa\": \"«نَخَ» سنسکریت (نَخَـ، خنثی، حالت فاعلی nakhám؛ همچنین nakhara-) به معنی «ناخن، چنگال» واژه‌ای واقعی است و همان‌گونه که در نمودار آمده از ریشه می‌آید، از راه هندوایرانی آغازین *Hnā́kš و در نهایت *h₃nṓgʰs هندواروپایی؛ پوکورنی در همان ص ۷۸۰ آن را آورده است. دو نکته: نخست آنکه kh بازتاب قاعده‌مند *gʰ هندواروپایی نیست (که باید h می‌شد) و همهٔ مراجع این را یادآور می‌شوند — پوکورنی «نوآوری آریایی»، والده‌پوکورنی «نوآوری آریایی که هنوز توضیح داده نشده»، باک «kh بی‌توضیح در برابر gh» و کلاین حتی «تأثیر قفقازی» را حدس می‌زند. دوم آنکه «naxâ» صورت سنسکریت نیست؛ در سنسکریت واج /x/ وجود ندارد و این تنها بازنویسی خود نورایی از همان nakhá است (شیوهٔ همیشگی او در سراسر کتاب، برای همسان کردن ظاهری با «ناخن» فارسی). تصویر ص ۳۶۸ نیز «nakhâ, naxâ» را نشان می‌دهد، پس خطای خوانش اسکن نیست.\",\n   \"sources\": [W_PIE, W_NAXON],\n   \"ref_check\": [\n     {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"POK_full.txt l. ~63950: 'with Aryan kh- Old Indic nakham., n., nakhara-m. n., \\\"nail, claw, talon\\\", np. naxun ds. (Aryan kh- an innovation)', under 'Root / lemma: onogh-: ongh-, nogh-…', 'Page(s): 780'.\"},\n     {\"ref\": \"SNS:258\", \"status\": \"supports\", \"note\": \"Tavoosi's Shāyast-nē-Shāyast glossary: the index gives 'naxun 258/3' (SNS.txt l. 32104, i.e. text p. 258 line 3) and the glossary entry (SNS.txt l. 14489) reads ':naxun:' with the cross-references '…n'xwn' and '(HRN. 228) nakha-', i.e. the entry itself pairs the Pahlavi word with Sanskrit nakha- and cites Horn p. 228 — the same page Nourai cites on the next node.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p. 180\", \"stance\": \"supports\", \"note\": \"'ai. nakha- m. n., nakharu- m. n. \\\"Nagel, Kralle\\\", np. nāxun ds. (ar. kh- eher eine noch aufzuklärende ar. Neuerung…)' — supports the derivation while flagging the kh.\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. nail, n. (KLN_1966.txt l. 24913)\", \"stance\": \"supports\", \"note\": \"'Cp. OI. nakháḥ, Pers. naxun, \\\"nail, claw\\\", where qh- (for gh-) is prob. due to Caucasian influence.'\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 4.39, p. 245\", \"stance\": \"supports\", \"note\": \"'Skt. nakha-' is in the word list, with the footnote '(Skt. also nakha-, with unexplained kh for gh)'.\"},\n     {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p. 490 (ARY_latin_index_pages.txt ll. 14286–14292)\", \"stance\": \"supports\", \"note\": \"The index of the Persian ناخن entry lists 'NAKHAS, A (SANSKRIT) / NAKHAM' beside 'NAXON (PAHLAVI)', 'ONYX, ONYCHOS (GREEK)', 'UNGUIS (LATIN)', 'GA-NAGLJAN (GOTHIC)', 'NAGAS (LITHUANIAN)' — the same cognate set, i.e. an independent modern Persian-language handbook agrees.\"}\n   ]\n  },\n  {\n   \"id\": 2,\n   \"lang\": \"Pahlavi\",\n   \"words\": \"nâxun\",\n   \"verdict\": \"plausible\",\n   \"derivation\": \"The Pahlavi word is exactly right: MacKenzie 1971 p. 58 has 'nāxun [nʾhwn | N ~] (finger) nail' (Book Pahlavi ⟨h⟩ writing /x/), and Horn no. 1016, p. 228, gives 'phlv. nāxun (Bund.)', i.e. attested in the Bundahišn; Moʿin's footnote at Borhān 2089 says the same, «پهلوی nāxun (بندهشن)». Morphologically it is *nāxu- (< Proto-Iranian *Hnā́xš, whence the -x- where Indic has -kh-) extended by the Iranian suffix -na/-una: Wiktionary reconstructs Proto-Iranian *Hnāxunah, whose reflexes are Baluchi nākun/náhun, Kurdish nēnok/neynok and Pashto nūk (all listed by Horn and by Moʿin). That extension is precisely why the arrow as drawn is wrong: Sanskrit nakhá- has no -un- and Pahlavi cannot descend from it — the two are sister reflexes of the same PIE root through Proto-Indo-Iranian, and every source Nourai cites (Pokorny, Walde–Pokorny, Buck, Klein, Horn, Moʿin) lists them side by side as cognates, never in a line. Hence 'plausible' rather than 'confirmed': right word, right ultimate root, wrong immediate parent.\",\n   \"derivation_fa\": \"واژهٔ پهلوی دقیقاً درست است: مکنزی (ص ۵۸) «nāxun [nʾhwn] ناخن» و هرن (شمارهٔ ۱۰۱۶، ص ۲۲۸) «پهلوی nāxun (بندهشن)» دارند و معین نیز در حاشیهٔ برهان (ص ۲۰۸۹) می‌نویسد «پهلوی nāxun (بندهشن)». از نظر ساخت، این واژه *nāxu- (از ایرانی آغازین *Hnā́xš، که x آن در برابر kh هندی است) به‌همراه پسوند ایرانی -una است؛ ویکی‌واژه ایرانی آغازین *Hnāxunah را بازسازی می‌کند که بلوچی nākun، کردی نینۆک و پشتو nūk از آن‌اند. همین پسوند نشان می‌دهد پیکان نمودار نادرست است: nakhá سنسکریت پسوند -un ندارد و پهلوی نمی‌تواند از آن گرفته شده باشد؛ این دو هم‌ریشه (خواهر) اند، نه پدر و فرزند، و همهٔ مراجعی هم که نورایی آورده آن‌ها را در کنار هم و نه در یک زنجیره فهرست کرده‌اند. پس واژه و ریشهٔ نهایی درست است و تنها پدرِ بی‌واسطه نادرست است.\",\n   \"sources\": [W_NAXON],\n   \"ref_check\": [\n     {\"ref\": \"SNS:258\", \"status\": \"supports\", \"note\": \"SNS glossary entry ':naxun:' (SNS.txt l. 14489) with the Book Pahlavi spelling 'nʾxwn' and the reference '(HRN. 228) nakha-'; the index confirms the attestation 'naxun 258/3' (SNS.txt l. 32104).\"},\n     {\"ref\": \"HRN:228\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 250 = printed p. 228, no. 1016: 'nāxun \\\"Nagel (am Finger oder an der Zehe)\\\" — ai. nakhá- \\\"Nagel, Kralle\\\"; phlv. nāxun (Bund.), kurd. neinuk \\\"Nagel\\\"; afγ. nūk; bel. nākun, vahuft; n. naxun (257).' Note that Horn lists the Sanskrit as a cognate ('ai. …'), not as the source of the Pahlavi.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 58 s.v. nāxun\", \"stance\": \"supports\", \"note\": \"'nāxun [nʾhwn | N ~] (finger) nail.' (PHD.txt l. 506; PHD_mackenzie.txt l. 3680). MacKenzie's 'N ~' means the New Persian form is identical.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep -i 'nāxu|naxu' NYB_vol2_glossary.txt returns only naxwist 'first' (l. 2655) and the index line 'nxwst: naxwist' (l. 6053); nāxun does not occur in his texts.\"},\n     {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ ed. Moʿin, vol. 4, printed p. 2089 (BQT_v4_pages.txt pdf page 172, page number ۲۰۸۹ visible in the running head)\", \"stance\": \"supports\", \"note\": \"Moʿin's footnote s.v. ناخن: «هندی باستان nakhá- (ناخن انسان، ناخن حیوانات)، پهلوی nāxun (بندهشن)، افغانی nūk، بلوچی nākun … کردی nēnok [کردی اصیل: نینوک]، پشتو … ؛ مادهٔ شاخی که در سر انگشتان انسان و جانوران می‌روید».\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. I p. 180\", \"stance\": \"partial\", \"note\": \"Lists 'np. nāxun' directly under the root without a Pahlavi step and without any Sanskrit intermediary, i.e. treats Iranian and Indic as parallel branches.\"}\n   ]\n  },\n  {\n   \"id\": 3,\n   \"lang\": \"Persian\",\n   \"words\": \"nâxon «ناخن»\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"New Persian ناخن continues Middle Persian nāxun without change of consonants; the only development is in the final syllable, classical/literary nāxun (so Saʿdi, Golestān p. 93, quoted by Moʿin at Borhān 2089: «چون نداری ناخن درنده تیز…») versus modern colloquial and standard nāxon, the regular New Persian lowering of unstressed final -un to -on. All four of Nourai's references carry this exact chain: Pokorny 780 'np. naxun'; Buck 4.39 p. 245 'represented in Iranian by NPers. nāxun'; Klein s.v. nail 'Cp. OI. nakháḥ, Pers. naxun'; and Moʿin's footnote at Borhān 2089, which gives the whole line Old Indic nakhá- → Pahlavi nāxun (Bundahišn) → NP ناخن with the cognates Afghan nūk, Baluchi nākun and Kurdish nēnok. Wiktionary states the ancestry in modern terms: ناخن < Proto-Iranian *Hnāxunah, a derivative of *Hnā́xš < Proto-Indo-Iranian *Hnā́kš < PIE *h₃nṓgʰs, with Sanskrit nakhá- as cognate, not ancestor.\",\n   \"derivation_fa\": \"«ناخن» فارسی نو دنبالهٔ بی‌واسطهٔ nāxun فارسی میانه است و همخوان‌ها هیچ تغییری نکرده‌اند؛ تنها هجای پایانی است که در فارسی کلاسیک nāxun تلفظ می‌شد (چنان‌که در بیت سعدی که معین در حاشیهٔ ص ۲۰۸۹ آورده: «چون نداری ناخن درنده تیز…») و در فارسی امروزی nāxon شده است، که همان تحول قاعده‌مندِ -un بی‌تکیهٔ پایانی به -on است. هر چهار مرجع نورایی همین را دارند: پوکورنی ص ۷۸۰ «np. naxun»، باک بند ۴٫۳۹ ص ۲۴۵ «در ایرانی با nāxun فارسی نو نمایندگی می‌شود»، کلاین ذیل nail «قس nakháḥ هندی باستان و naxun فارسی»، و حاشیهٔ معین بر برهان قاطع ص ۲۰۸۹ که زنجیرهٔ هندی باستان nakhá- ← پهلوی nāxun (بندهشن) ← ناخن را با همتاهای افغانی nūk و بلوچی nākun و کردی نینۆک می‌آورد. ادعای نورایی در این گره درست است.\",\n   \"sources\": [W_NAXON, W_PIE],\n   \"ref_check\": [\n     {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"'…Old Indic nakham., n., nakhara-m. n., \\\"nail, claw, talon\\\", np. naxun ds. (Aryan kh- an innovation)…', 'Page(s): 780' (POK_full.txt ll. 63948–63996).\"},\n     {\"ref\": \"BQT:2089\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt pdf page 172 carries the printed page number ۲۰۸۹ in the running head, and the footnote to the headword ناخن reads «هندی باستان nakhá- (ناخن انسان، ناخن حیوانات)، پهلوی nāxun (بندهشن)، افغانی nūk، بلوچی nākun … کردی nēnok … مادهٔ شاخی که در سر انگشتان انسان و جانوران می‌روید». Nourai's page number is exact.\"},\n     {\"ref\": \"SYN:245\", \"status\": \"supports\", \"note\": \"SYN.txt leaf 282 (the printed number 245 appears in the leaf, section '4.39 NAIL'): '*(o)nogh- (with wide variation of … suffixes in different IE languages). Walde-P. 1.180 f. … represented in Iranian by NPers. nāxun (Skt. also nakha-, with unexplained kh for gh).'\"},\n     {\"ref\": \"KLN:1028\", \"status\": \"supports\", \"note\": \"Klein s.v. nail, n.: '…Cp. OI. nakháḥ, Pers. naxun, \\\"nail, claw\\\", where qh- (for gh-) is prob. due to Caucasian influence.' (KLN_1966.txt l. 24913). In this scan the entry sits on leaf 549, whose facing leaf 550 carries the printed page marker 1028, so the entry is on p. 1026/1027 — Nourai's citation is off by at most one page.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"HRN\", \"where\": \"no. 1016, p. 228\", \"stance\": \"supports\", \"note\": \"'nāxun \\\"Nagel (am Finger oder an der Zehe)\\\" … phlv. nāxun (Bund.), kurd. neinuk; afγ. nūk; bel. nākun … n. naxun (257).' Horn's 'n.' = neupersisch.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie p. 58\", \"stance\": \"supports\", \"note\": \"'nāxun [nʾhwn | N ~] (finger) nail' — the 'N ~' explicitly marks the New Persian form as identical to the Pahlavi.\"},\n     {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p. 490\", \"stance\": \"supports\", \"note\": \"The ناخن entry's index lists NAXON (PAHLAVI), NAKHAS/NAKHAM (SANSKRIT), ONYX (GREEK), UNGUIS (LATIN), NAGEL (DUTCH/SWEDISH), NOGA (OLD BULGARIAN) — an independent modern Persian handbook reaching the same root.\"},\n     {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\", \"note\": \"The local Moʿin OCR has no ناخن headword (grep 'ناخن' finds only quotations inside other entries, ll. 6252, 13544); Moʿin's own etymological note was read in his Borhān footnote instead.\"}\n   ]\n  },\n  {\n   \"id\": 4,\n   \"lang\": \"Germanic\",\n   \"words\": \"nagla\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Proto-Germanic *naglaz (Nourai's 'nagla' is Watkins' stem notation *nagla-) 'nail, fingernail; metal peg' is the l-suffixed derivative of the root: PIE *h₃nogʰ-l̥ / Watkins' 'suffixed (diminutive) form *nogh-elo-'. Its reflexes are Old High German nagal, Old Saxon nagal, Old English nægl/nægel, Old Frisian neil, Old Norse nagl 'fingernail' beside nagli 'metal nail', Gothic ga-nagljan 'to nail' — all listed by Pokorny on the cited page and by Walde–Pokorny I 180, with Pokorny's note that ON negl was 'perhaps originally reinterpreted Sg. i-stem'. The -l- extension is what marks the Germanic branch off from Greek ὄ-νυξ and Latin u-nguis, and Nourai's reference is exactly on target: AHD/Watkins s.v. nogh- gives the Germanic branch as its point 1. Nourai's bare 'AHD' with no page is his usual way of citing the 1975 appendix.\",\n   \"derivation_fa\": \"*naglaz ژرمنی آغازین (صورت «nagla» نورایی همان ستاک‌نویسی واتکینز *nagla- است) به معنی «ناخن؛ میخ» مشتقِ پسوند-l ریشه است: *h₃nogʰ-l̥ هندواروپایی، یا به نوشتهٔ واتکینز «صورت پسوندی (تصغیری) *nogh-elo-». بازتاب‌های آن — nagal آلمانی علیای باستان، nægl انگلیسی باستان، nagl ایسلندی باستان (در برابر nagli «میخ») و ga-nagljan گوتی — همه در همان صفحهٔ ۷۸۰ پوکورنی و در والده‌پوکورنی ج ۱ ص ۱۸۰ آمده‌اند. همین پسوند -l است که شاخهٔ ژرمنی را از ὄ-νυξ یونانی و u-nguis لاتینی جدا می‌کند. ارجاع نورایی به AHD دقیقاً درست است: واتکینز ذیل nogh- نخستین بند را به همین شاخهٔ ژرمنی داده است. ادعای نورایی درست است.\",\n   \"sources\": [W_PIE, ETY],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt l. 787): 'nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-elo- in Germanic *nagla- in Old English nægl, nail: NAIL. … [Pok. onogh- 780.]' — the Germanic reconstruction *nagla- is Watkins' own form, exactly what the chart prints.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"p. 780\", \"stance\": \"supports\", \"note\": \"'Old High German nagal, Old English nægel \\\"nail\\\", Old Icelandic nagl ds. (conservative stem has changed, Pl. negl) … Gothic ga-nagljan \\\"nail\\\"' (POK_full.txt ll. 63978ff).\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. I p. 180\", \"stance\": \"supports\", \"note\": \"'ahd. nagal, ags. nægel \\\"Nagel\\\", aisl. nagl ds. (kons. St. geworden, Pl. negl) … got. ganagljan \\\"annageln\\\"' — same set, with the -lo- formant noted in the lemma header ('z. T. mit Formans -u- … und -lo-').\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. nail, n.\", \"stance\": \"supports\", \"note\": \"'OE. nægl, nægel, \\\"fingernail; metal nail, peg\\\", rel. to OS., OHG. nagal, OFris. neil, MDu. naghel, Du., MHG., G. nagel … ON. nagl, \\\"fingernail\\\", nagli, \\\"metal nail\\\", Goth. ganagljan, \\\"to nail\\\", fr. I.-E. base *nogho-, *ngho-, *ongho-, \\\"nail\\\".'\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Nail\", \"stance\": \"supports\", \"note\": \"'M. E. nayl. A. S. nægel. + Dan. nagle, Swed. nagel, G. nagel, the human nail, nagli, spike… Allied to Lithuan. nagas… Skt. nakha, nail of the finger or toe' (SKT.txt l. 12136, heavily OCR-damaged but legible); Skeat adds that Gk. ὄνυξ and L. unguis 'seem to come from' a variant of the root.\"}\n   ]\n  },\n  {\n   \"id\": 5,\n   \"lang\": \"English\",\n   \"words\": \"nail\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Proto-Germanic *naglaz gave Old English nægl / nægel 'fingernail' and negel 'tapering metal pin', which merged in Middle English naile/nayl/neil and became modern nail; the verb follows (OE næglian > ME nailen). The 'fingernail' sense is the original and the 'metal spike' sense a Germanic transfer already present in Old English and Old High German (Etymonline: 'the \\\"fingernail\\\" sense seems to be the original one'; Buck 4.39/4.16 notes the Germanic words for the metal nail are 'the same words as for \\\"nail\\\" of the finger or toe (except that ON nagli and nagl are differentiated), this latter sense being the orig., as in the cognates, Grk. ὄνυξ, Lat. unguis'). The node carries no reference in the book and needs none: the OE > ME > NE chain is uncontroversial and covered by Klein, Skeat and Etymonline alike.\",\n   \"derivation_fa\": \"*naglaz ژرمنی آغازین در انگلیسی باستان به nægl/nægel «ناخن» و negel «میخ» رسید که در انگلیسی میانه در naile/nayl یکی شدند و امروز nail است (فعل آن نیز از næglian انگلیسی باستان). معنای «ناخن» کهن‌تر است و معنای «میخ» انتقالی ژرمنی است که در همان انگلیسی باستان و آلمانی علیای باستان دیده می‌شود؛ اتیمانلاین می‌نویسد «معنای ناخن به‌نظر معنای اصلی است» و باک نیز یادآور می‌شود که واژه‌های ژرمنیِ «میخ» همان واژه‌های «ناخن» اند و این معنای دوم اصلی است، چنان‌که در همتاهای ὄνυξ یونانی و unguis لاتینی. این گره در کتاب ارجاعی ندارد و نیازی هم ندارد، زیرا زنجیرهٔ انگلیسی باستان ← میانه ← نو بی‌چون‌وچراست. ادعای نورایی درست است.\",\n   \"sources\": [ETY],\n   \"ref_check\": [\n     {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (the box prints only 'nail' with no citation), so there is no reference of Nourai's to check; the chain was verified against Klein, Skeat, Buck and Etymonline instead (see consulted).\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"s.v. nail, n. and nail, v. (KLN_1966.txt ll. 24913–24914)\", \"stance\": \"supports\", \"note\": \"'nail, n., 1) the horny substance on the ends of the fingers and toes; 2) a small spike of metal or wood. — ME. naile, neil, fr. OE. nægl, nægel, \\\"fingernail; metal nail, peg\\\"…'; 'nail, tr. v. … ME. nailen, fr. OE. næglian, fr. nægel, \\\"nail\\\".'\"},\n     {\"src\": \"SKT\", \"where\": \"s.v. Nail\", \"stance\": \"supports\", \"note\": \"'M. E. nayl. A. S. nægel. + Dan. nagle, Swed. nagel, G. nagel, the human nail, nagli, spike.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nogh-; index p. 1900 'NAIL nogh-'\", \"stance\": \"supports\", \"note\": \"'…in Germanic *nagla- in Old English nægl, nail: NAIL', and the reverse index line 'NAIL nogh-'.\"},\n     {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., vol. 1 (A–?)\", \"stance\": \"silent\", \"note\": \"Only vol. 1 is on disk, so the entry for 'nail' (N) is not available in the local copy.\"}\n   ]\n  }\n ]\n}\n\nout = {\n \"pdf_page\": 368,\n \"book_page\": 338,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [e0, e1]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-368.json', 'w', encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\n"
}
```


### [2026-09-07T19:45:11.563Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk368.py (file state is current in your context — no need to Read it back)
```


## [2026-09-07T19:45:15.363Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk368.py && python3 -m json.tool data/verification/page-368.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 368"
}
```


### [2026-09-07T19:45:17.595Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 10/10
node verdicts: {'disputed': 2, 'confirmed': 5, 'transcription_suspect': 1, 'plausible': 2}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'supports': 12, 'partial': 4, 'contradicts': 1, 'not_checked': 1}
books consulted: {'partial': 3, 'silent': 11, 'supports': 21, 'contradicts': 1} | by book: {'WLD': 4, 'KLN': 4, 'CHEUNG': 3, 'PHD': 3, 'HRN': 2, 'NYB': 2, 'BQT': 2, 'MON': 2, 'POK': 2, 'SYN': 2, 'ARY': 2, 'SKT': 2, 'BRT': 1, 'SOD': 1, 'LAT': 1, 'LEW': 1, 'AHD': 1, 'WEB': 1}
```


## [2026-09-07T19:45:42.199Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-368.json` written; `verify_check.py 368` reports 10/10 nodes, 0 PROBLEM lines.

**Page 368 (book p. 338) — 2 entries, 10 nodes**
- Root verdicts: 1 confirmed (Nogh/Onogh "nail"), 1 disputed (Nôğ/Snôğ "whim")
- Node verdicts: 5 confirmed, 2 plausible, 2 disputed, 1 transcription_suspect
- Ref checks: 12 supports, 4 partial, 1 contradicts, 1 not_checked (node with no refs)

**Disputed / flagged**
- ROOT `Nôğ, Snôğ` — the box is a verbatim copy of Mann IEC 848–849 + 1236, but no other IE dictionary has such a root (0 hits in Pokorny, Walde–Pokorny, Watkins), and Cheung 2007 p. 285–286 s.v. *naz says outright "no IE etymology can be cited". Mann himself hedges every limb ("cf.", "ambig.", "only if dialectal").
- `#1 Old Iranian nâz` (disputed) — form and glosses are exactly Abolghasemi FFD p. 77 («ایرانی باستان *nāz-… شادی، افتخار»), but the IE parent is Nourai's own step; Bartholomae has no Avestan nāz-.
- `#4 Greek nôgla` (transcription_suspect, error_in = **book**) — the word is νώγαλα *nṓgala* "sweetmeats, dessert" (LSJ; Antiphanes fr. 65, Ephippus fr. 24); Mann prints "nógala" on both cited pages, so the book dropped an -a-. The extraction is faithful (page image checked, copied to `data/verification/sources/refs/ocr/BOOK/368.png`). The root→Greek link is also unsupported.
- `#5 Latin nŭgae, nôgae` (disputed) — forms correct (Ernout–Meillet head the article "nugae (nogae, naugae?)") but the Greek→Latin arrow is wrong twice: E-M end "Pas d'étymologie", Wiktionary "Unknown… perhaps cognate with nux/naucum", and Mann himself makes Latin an independent branch, admitting it "only if dialectal for *nogae".

**Plausible (arrow correction, not error)**
- `#1 Sanskrit nakhâ, naxâ` — nakhá- is right; "naxâ" is Nourai's own x-for-kh respelling (Sanskrit has no /x/), printed in the book. All authorities flag the -kh- as an unexplained Indo-Iranian innovation, which the flat arrow hides.
- `#2 Pahlavi nâxun` — word confirmed (MacKenzie p. 58 ⟨nʾhwn⟩; Horn 1016 "phlv. nāxun (Bund.)"; Moʿin at Borhān 2089), but it is a *sister* of Skt nakhá-, from Proto-Iranian *Hnāxunah, not its descendant; the Sanskrit→Pahlavi arrow is genealogically wrong.

**Notable positives**
- `nâčuk` is NOT a misreading: it is the Book Pahlavi transliteration ⟨nʾcwk⟩ of nāzuk (MacKenzie; Manichaean ⟨nʾzwg⟩), and Horn p. 228 prints "phlv. nācuk" verbatim; Moʿin explains it («تبدیل و گذشتی است از z به č»).
- Page numbers check out exactly: FFD p. 77, HRN p. 228 (nos. 1016 & 1017), POK "Page(s): 780", SYN p. 245 (§4.39), BQT vol. 4 printed p. ۲۰۸۹. KLN:1028 is off by ≤1 page in the scan (entry on leaf 549, marker 1028 on leaf 550).

**Extraction errors for the owner:** none — the JSON matches the printed page in every field, including `nakhâ, naxâ` and `nôgla`.
