# Verification process log — verify-page-69


## [2026-09-05T05:22:44.395Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 69 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-69.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-69.json. Write /home/sfmqrb/git/rishe/data/verification/page-69.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 69` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:22:45.638Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:22:46.419Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:22:46.436Z] TOOL RESULT

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


## [2026-09-05T05:22:46.879Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-69.txt"
}
```


### [2026-09-05T05:22:46.900Z] TOOL RESULT

```
1	=== PDF page 69 (book page 39) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Au 2, We 2 : away, off, down  (refs POK:72)
4	#1 (parent #0) [Avestan / Old Persian] refs=KLN:132; POK:72; HID:209 | ava 1, aorâ : down ; avara : downward
5	  #2 (parent #1) [Avestan] refs=KLN:132; HRN:105; BQT:733 | ava-pat : fall down ☞Pet 1 ; avara-sad : settle down, satisfy ☞Sed
6	    #3 (parent #2) [Persian] refs=HRN:22; BQT:145,180 | oftâdan «افتادن» : to fall ; xorsand «خرسند» : satisfied
7	    #4 (parent #2) [Avestan] refs=AEF:175; BQT:180 | ava-par : fill down ☞Pel 1
8	      #5 (parent #4) [Persian] refs=BQT:180; AEF:175 | obârdan «اُباردن» : to swallow ; obâsh «اوباش» : a tough or rowdy fellow, a gangster | extra: اوباشتن
9	#6 (parent #0) [Old Russian] refs=AHD:1391 | u- : away, off ; u-krai : far away edge, border land ☞Sek
10	  #7 (parent #6) [English] refs=None | Ukraine
11	#8 (parent #0) [Indo-European] refs=KLN:1740 | We-spero : going down (of the sun)
12	  #9 (parent #8) [Germanic] refs=None | westo : sunset, west
13	    #10 (parent #9) [English] refs=None | west
14	--- entry 1 ---
15	ROOT Au 3 -> redirect to I 2
16	--- entry 2 ---
17	ROOT Aŭe 1 -> redirect to Wě 1
18	--- entry 3 ---
19	ROOT Aŭe 2 -> redirect to Wed
20	
```


## [2026-09-05T05:22:49.837Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-69.json",
 "description": "Read page 69 source JSON"
}
```


### [2026-09-05T05:22:49.879Z] TOOL RESULT

```
{
  "pdf_page": 69,
  "book_page": 39,
  "entries": [
    {
      "root": {
        "name": "Au 2, We 2",
        "lang": "Indo-European",
        "refs": "POK:72",
        "gloss": "away, off, down"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:132; POK:72; HID:209",
          "words": [
            {
              "translit": "ava 1, aorâ",
              "gloss": "down",
              "script": null
            },
            {
              "translit": "avara",
              "gloss": "downward",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KLN:132; HRN:105; BQT:733",
          "words": [
            {
              "translit": "ava-pat",
              "gloss": "fall down",
              "script": null,
              "see": [
                "Pet 1"
              ]
            },
            {
              "translit": "avara-sad",
              "gloss": "settle down, satisfy",
              "script": null,
              "see": [
                "Sed"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:22; BQT:145,180",
          "words": [
            {
              "translit": "oftâdan",
              "gloss": "to fall",
              "script": "افتادن"
            },
            {
              "translit": "xorsand",
              "gloss": "satisfied",
              "script": "خرسند"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Avestan",
          "refs": "AEF:175; BQT:180",
          "words": [
            {
              "translit": "ava-par",
              "gloss": "fill down",
              "script": null,
              "see": [
                "Pel 1"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:180; AEF:175",
          "words": [
            {
              "translit": "obârdan",
              "gloss": "to swallow",
              "script": "اُباردن"
            },
            {
              "translit": "obâsh",
              "gloss": "a tough or rowdy fellow, a gangster",
              "script": "اوباش"
            }
          ],
          "script_extra": "اوباشتن",
          "note": null,
          "quote": {
            "text": "پس بیوبارید ایشان را همه - نی شبان را میش زنده ، نی رمه",
            "poet": "Rūdakî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Russian",
          "refs": "AHD:1391",
          "words": [
            {
              "translit": "u-",
              "gloss": "away, off",
              "script": null
            },
            {
              "translit": "u-krai",
              "gloss": "far away edge, border land",
              "script": null,
              "see": [
                "Sek"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "Ukraine",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KLN:1740",
          "words": [
            {
              "translit": "We-spero",
              "gloss": "going down (of the sun)",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Germanic",
          "refs": null,
          "words": [
            {
              "translit": "westo",
              "gloss": "sunset, west",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "west",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Au 3",
        "redirect": "I 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Aŭe 1",
        "redirect": "Wě 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Aŭe 2",
        "redirect": "Wed"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:22:50.209Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:22:50.257Z] TOOL RESULT

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


## [2026-09-05T05:23:17.659Z] AGENT

Let me check the reference index and an existing output for format.


## [2026-09-05T05:23:19.772Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HID','HRN','BQT','AEF','AHD','BRT','MON','PHD','ARY','CHEUNG','IEC','SYN','WLD','SKT','TTS','LKT','FVQ','AFM','PLA']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


## [2026-09-05T05:23:20.380Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-66.json && echo ---- && ls tools/"
}
```


### [2026-09-05T05:23:21.300Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HID {"title": "C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883", "edition_found": "1883", "kind": "archive_djvu", "url": "https://archive.org/details/handbuchderalti00bartgoog", "identifier": "handbuchderalti00bartgoog (also handbuchderalti01bartgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt", "page_offset": "leaf = printed + 13 (e.g. leaf 14 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar by numbered 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG MISSING

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
```


### [2026-09-05T05:23:21.342Z] TOOL RESULT

```
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


## [2026-09-05T05:23:26.498Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 79 80 81; do echo \"=== POK_01 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -80; done"
}
```


## [2026-09-05T05:23:27.728Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"au-, au̯e\\|au̯e-, u̯e\\|herab, weg von\" POK_full.txt | head -20"
}
```


### [2026-09-05T05:23:28.233Z] TOOL RESULT

```
=== POK_01 leaf 79 ===
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
=== POK_01 leaf 80 ===
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
=== POK_01 leaf 81 ===
  Unwillen,  Abweisung,  Überraschung),   poln.  au,  cech.  ou. WH.  I  78.
72
2.  au-,  au-es-,  aus-  ^übernachten,  schlafend
Arm.  aganim  ,übernachte';  vair-ag  ,au£  dem  Lande  lebend',  aut'  ,Über- nachten,  Nachtruhe,  Station^
Gr.  lavo)  ,scblafe^  aus  redupl.  "^i-ausö,  Aor.  i-avaai,  woneben  unredupl. Aor.  Usaa,  Inf.  äfea{o)ai]  avXtg,  -löog  , Aufenthaltsort,  Lager,  Stall,  Nacht- -  lager^,  avUlop^ai  ,bin  im  Hofe,  übernachte',  äygavXog  ,im  Freien  übernach- tend^, aiUj  ,Hof,  Wohnung^  (ursprüngl.  wohl  ,der  eingezäunte  Raum  ums Haus,  in  dem  das  Vieh  für  die  Nachtzeit  zusammengetrieben  wird');  von lavco  stammt  außer  lavd-i-iög  ,Nachtlager^,  ^r]?uavd^iA,6g  ,Schafstall^,  iviavd- (.lög  , Aufenthaltsort'  (:  hom.  inavstv  ,sein  Ruhequartier  haben')  auch  gr. Eviavxog  eigentlich  ,Rast,  Ruhestation',  daher  die  Sonnenwenden  als  Ruhe- stationen im  Sonnenlauf  {solstitium)^  dann  .Jahr,  Jahrestag'  (anders  Specht Idg.  Dekl.  15,  Schwjzer  Gr.  Gr.  l,  424^,  s.  auch  en-  ,Jahr').
Eine  schwere  Basis  *aue-,  ^auö-  in  den  wohl  anzureihenden  hom. dcoretg  ijTtvov  (von  Schulze  Qu.  ep.  72  unmittelbar  zu  lavo)  gestellt  unter formalem  Vergleich  von  ^q{J^)o)t&u)  :  eiQOiiai  aus  *£QJ^O[.iac)  und  äcogog (Sappho),  (hgog  (Kallimachos)  ,v7tvog^  (Benfey  Wzl.-Lex.  I  298),  wozu  ags. loerig,  engl,  loeary^  as.  wörag,  icörig  ,müde',  ahd.  louorag  , berauscht';  über ai.  väyati  ,wird  müde';  s.  aber  Wz.  awe-  ,sich  mühen,  anstrengen'.
WP.  I  19f.  Schwjzer  Gr.  Gr.  1  690.''
Über  ues-  ,verweilen'  s.  unter   besonderem  Artikel.
5.  aU'  (aue) ;  ue-  ,herab,  weg  von  — '.
Ai.  dva  ,ab,  herab',  meist  Präfix  von  Verben  und  Subst.,  selten  Präp. m.  Abi.,  av.  ap.  ava  Präfix  ,herab'  und  (indem  mehr  das  Ziel  als  der Ausgangspunkt  der  Bewegung  zum  Bewußtsein  kam)  ,worauf  zu,  heran' (z.  B.  avabar-  ^hinabbringen,  wegtragen'  und  ,hinzubringen,  verschaffen'), ebenso  Präp.  m.  Akk.  , hin— zu,  hin— an';  davon  ai.  dvara-  ,inferior'  und  av. aorä  ,nach  unten,  hinab'  (nach  pa7^ä  aus  avavd  erweitert),  av.  avard  Adv. ,hinab,  herab' =  ai.  avdr  RV.  I  133,  7;  ai.  avdh  {avds)  , herab',  wovon avastäd  ,unten';  ohne  ausl.  Vokal  (vgl.  av.  ao-ra)  ai.  ö-  z.  B.  in  ö-gand-h ,alleinstehend,  erbärmlich'  (:  gand-h  ,Schar';   Wackernagel   Ai.  Gr.  I  54);
gr.  ai)-  wohl  in  avxdvTsiv'  dvaxcDQelv,  ävaxaC,eG d-ai  Hes.  (Schulze  Qu. ep.  60);
illyr.  au-  ,ad'  in  Eigennamen?  (Krähe  IF.  49,  273);
lat.  au-  ,fort'  in  auferö  (=  av.  dva-hharati,  av.  ava-bar-),  aufugiö]
gall.  au-tagis  ,dLccTa^LgV  (Vendryes  BSL.  25,  36);
air.  vielleicht  ö,  üa  ,von,  mit,  durch',  als  Präp.  m.  Dat.,  acymr.  liou, jünger  0  ,wenn',  0
```


### [2026-09-05T05:23:28.282Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:23:35.451Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==82' POK_01.txt | head -60"
}
```


### [2026-09-05T05:23:36.960Z] TOOL RESULT

```
Präp.  ,von';
apr.  lit.  lett.  au-  ,weg,  ab'  (z.  B.  lett.  au-manis  ,unsinnig'),  aksl.  u  Präfix ,weg,  ab',  z.  B.  u-myti  ,abwaschen'  (u-Uzati  ,aufugere'),  als  Präp.  m.  Gen.
73
i  /bei  Verben  des  VerLangens^  EmpfangenS;  Nehmens)   und,   mit  Ver- blassen des  Begriffes  des  Ausgangspunktes,  ,bei';
1  ett    Präverb  u-    (^it'e-,  i(^ci-)  , hierher^,    a-ica-an  ,hinweg^   (Sturtevant   Lg.
7,  1  ff.).
Davon   mit  ^Formans    aut{i)o-:    gr.  aljzojg  ,vergeblich^,  aljoiog  ds.  und
*>-üt  aiipja-  (N.  Sg.  *aupeis  oder  *aups)  ,'öde,  verlassen^  (*,abgelegen^), auhida  Wüste^,  ahd.  öcli,  nhd.  Öde,  anord.  audr  ,öde^;  air.  üathad  , Einzel- heit Vereinzelung^  —  Geht  auf  die  Schrecken  der  Einöde,  Wildnis  auch mir.  üath  _,Schrecken,  schrecklich'  (fernzuhalten  sind  cjmr.  uthr  , schreck- lich' corn.  uth,  euth,  bret.  euz  , Schrecken')  ?  Wenigstens  ist  deren  Ver- bindung mit  lat.  pavere  ,sich  ängstigen,  vor  Furcht  zittern'  alles  eher  als sicher,  s.  pou-  , Angst'.
Neben  aut(i)o-  steht  vielleicht  ablautendes  u-to^  in  alb.  hut  ,vergeb- lich,  leer,  eitel',  ue-to-  (s.  unten  *iß-)  in  gr.  ov'a  irog  ,nicht  umsonst, nicht  ohne  Grund',  STcoffLog  (/  bei  Homer)  , vergeblich,  ohne  Erfolg,  unnütz'.
*u'e-,  mit  *au-  wohl  unter  *aue-  zu  vereinigten :
lat.  *vS-  in  vescor  ursprüngl.  , wovon  abessen'  (:  escd)^  woraus  rückgebildet üßscMS  , gefräßig;  wählerisch  im  Essen  (*nur  abknabbernd);  abgezehrt';  ve- zur  Bezeichnung  eines  fehlerhaften  Zuviel  oder  Zuwenig,  ve-cors  , aber- witzig, verrückt,  tückisch',  ve-grandis  , nicht  groß,  winzig',  vesänus  ,ver- rückt',   Ve-jovis,  umbr.  ve-purus  (Abi.  PL),  wenn  .(legä)  ^nvqa^.
U0-:  Gr.  J^o-  in  ark.  J^o-cpXrjKÖdL,  att.  d-(phaxdv(x),  dcpelXa),  lesb.  ö-SLyrjv , öffnen',  att.  oiyw,  jünger  oYyvv^xi  (Prellwitz  ^  345,  Brugmann  IF.  29,  241, BSGW.  1913,  159).
ues-i  Mit  ai.  avds  ,herab'  hängt  formantisch  germ.  ices-  zusammen  in nhd.  Westj  ahd.  icestar  ^westwärts',  anord.  vestr  n.  ,Westen',  Adv.  ,im  W., gegen  W.'  (*we5-^(e)ro-,  vgl.  anord.  nor-dr),  ahd.  westana  ,von  W.'  usw. (Brugmann  IF.  13,  157  ff.;  über  die  Erklärung  der  Wisigothae  als  ,West- Goten'  s.  Kretschmer  Gl.  27,  232).
Hierher  (nach  Brugmann  aaO.)  auch  der  Anlaut  des  Wortes  für  Abend, idg.  uesperos  und  iteqeros,   s.  dort.
Verwandtschaft  von  idg.  *aw-,  iß-  mit  dem  Pron.-St.  au-,  u-  .jener'  als ,von  jenseits,  von  dorther'  ist  denkbar.
WP.  I  13  f.,  WH.  I  79,  850,  Trautmann  16.
4-  au-,    u-    (:  ue-,    uo-)    Pronominalstamm   ,jener',   auch    gegenüberstellend , alter,    alius',   , andrerseits,   hinwiederum',    in   zwei    aufeinanderfolgen- den Satzgliedern  gesetzt  ,der  einerseits  —  der  andrerseits',  , einerseits —  andrerseits'. awo-:  Ai.  av.  apers.  ava-  ,jener';  aksl.  aruss.  ov^^  —  ov^-  ,der  einerseits —  der  andrerseits,
```


## [2026-09-05T05:23:37.282Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"u̯es-pero\\|wes-pero\\|ues-pero\\|uesperos\\|vesperos\" AHD_watkins1985.txt POK_full.txt | head -20; echo ===; grep -n -i \"^west\\b\\|wes-pero\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T05:23:37.362Z] TOOL RESULT

```
Exit code 1
AHD_watkins1985.txt:133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
AHD_watkins1985.txt:1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
AHD_watkins1985.txt:1601:HERPES serp-2 HERPETOLOGY serp-2 HESITATE ghais- HESPERIAN wes-pero- HEST kei-3
POK_full.txt:7533:uesperos and ueqeros, see there. 
POK_full.txt:92617:the variation uesperos : uekeros perhaps after Specht Indo Germanic Dekl. 1 1 9 taboo to 
(eval):1: == not found
```


## [2026-09-05T05:23:46.289Z] TOOL CALL #11: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','HID','HRN','BQT','AHD','BRT','SKT','IEC','SYN','ARY','FSD','WEB','LKT','PHD','NYB','HUB','CHEUNG','MON']:\n    v=d.get(k)\n    if v: print(k,'|offset:',v.get('page_offset'),'|hint:',v.get('lookup_hint'))\n    print()\n\""
}
```


### [2026-09-05T05:23:47.981Z] TOOL RESULT

```
KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

HID |offset: leaf = printed + 13 (e.g. leaf 14 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Grammar by numbered §; Glossar at the end. grep the Avestan word.

HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

AHD |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).

BRT |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

SKT |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

IEC |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

SYN |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

ARY |offset: printed page = pdf page + 1 |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image

FSD |offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.

WEB |offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.

LKT |offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.

PHD |offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

HUB |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.


MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
```


## [2026-09-05T05:23:54.849Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 77 78 79; do echo \"=== KLN_1966 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -8; done"
}
```


## [2026-09-05T05:23:55.937Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"OI\\. áva\\|OI. ava\\|Avestic ava\\|Av\\. ava\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T05:23:56.586Z] TOOL RESULT

```
=== KLN_1966 leaf 77 ===
n  anatomist  Andreas  Vesalius (1514-64).  See  Joseph  Hyrtl,  Onomatologia anatomica,  Vienna,  1880,  p.59. atlas,  n.,  silk-satin.  —  Arab,  atlas,  lit.  ‘wiped smooth’,  fr.  talasa,  ‘he  wiped,  smoothed  away’, atle,  atlee,  n.,  the  tamarisk  salt  tree.  —  Arab. athlah,  ‘a  species  of  tamarisk’,  prop,  unit  name of  athl,  rel.  to  Aram,  athld,  Heb.  eshel,  ‘tama¬ risk  tree’.
atman,  n.,  the  supreme  soul,  the  principle  of  life (Hinduism).  —  OI.  atman,  prop,  ‘breath,  soul’, orig.  ‘cover,  body’,  cogn.  with  OHG.  atum, MHG.  dtem,  G.  Atem,  MDu.  ddern,  OFris. ethma,  OS.  athom,  OE.  xdm,  ‘breath’.  Cp.  the second  element  in  mahatma, atmido-,  before  a  vowel  atmid-,  combining  form meaning  ‘vapor’.  —  Gk.  4x;ju8o-,  4xpu8-,  fr. aTfjd?,  gen.  4x(iL8op,  ‘steam,  vapor’,  rel.  to  d-rpos, of  s.m.  See  atmo-.
atmidometer,  n.,  an  atmometer.  —  Compounded of  atmido-  and  Gk.  pixpov,  ‘measure’.  See meter,  ‘poetical  rhythm’, atmo-,  before  a  vowel  atm-,  combining  form meaning  ‘vapor’.  —  Gk.  4xpo-,  dxp-,  fr.  dxpoc, ‘steam,  vapor’,  contraction  of  dexpo 9,  which prob.  stands  for  ‘dfs-x-po-?  and  is  rel.  to deXXa  (for  *Sf  e-X-ia),  ‘tempest,  whirlwind’,  and to  S7)pi  (for  *dfrjpi),  ‘I  blow’,  fr.  I.-E.  base *we-,  ‘to  blow’,  whence  also  OI.  vdti,  ‘blows’, Goth,  waian,  OE.  wdwan,  ‘to  blow’.  See  wind, ‘air  in  motion’,  and  cp.  Aello. atmology,  n.,  the  study  of  the  laws  of  aqueous vapor. — Compounded  of  atmo-  and  Gk.  -XoyiS, fr.  -Xoyoq,  ’one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)’.  See -logy.
Derivatives:  atmolog-ic,  atmolog-ic-al,  adjs.,  at- molog-ist,  n.
atmolysis,  n.,  separation  of  mixed  gases.  —  Com¬ pounded  of  atmo-  and  Gk.  X'Wg,  ‘a  loosing; dissolution’.  See  -lysis.
atmometer,  n.,  an  instrument  for  measuring  the rate  of  evaporation.  —  Compounded  of  atmo- and  Gk.  p£xpov,  ‘measure’.  See  meter,  ‘poetical rhythm’.
Derivatives:  atmometr-ic,  adj.,  atmometr-y,  n. atmosphere,  n.  —  Compounded  of  Gk.  dxpop, ‘steam,  vapor’,  and  cnpoupa,  ‘ball,  sphere’;  see atmo-  and  sphere.  The  word  atmosphere  was  first used  by  the  English  bishop  and  scientist  John Wilkins  (1614-72)  in  1638  with  reference  to  the moon  (which  in  reality  has  no  atmosphere). Derivatives :  atmospher-ic,  atmospher-ic-al,  adjs., atmospher-ic-al-ly,  adv.,  atmospher-ics,  n.pl. atocia,  n.,  sterility  of  the  female  (med.)  —  Medi¬ cal  L.,  fr.  Gk.  axoxla,  ‘sterility’,  fr.  6x0x04, having  never  yet  brought  forth’,  fr.  4-  (see  priv. pref.  a-)  and  XOX04,  ‘childbirth,  parturition’, which  is  rel.  to  xoxefx;,  ‘father’,  in  the  pi., ‘parents’.  See  -tocia,  toco-,  and  cp.  anatocism, atoll,  n.,  a  coral  island.  —  Malayalam.
123
=== KLN_1966 leaf 78 ===
ust’,  fr.  ad- and  L.  temperdre,  ‘to  divide  duly;  to  temper  . See  temper,  v.
Derivatives:  attemper-ed,  adj.,  attemper-ment ,n. attemperate,  tr.  v.  (obsol.) —  Late  L.  attemperatus, pp.  of  attemperare.  See  prec.  word  and  cp.
temperate.
124
Derivatives :  attemperat-ion,  n.,  attemperat-or,  n. attempt,  tr.  v.  —  OF.  atenter,  also  atempter  (F. attenter),  fr.  L.  attentdre,  attemptare  (whence also  It.  attentare,  OProven?.,  Port,  attentar,  Sp. atentar),  ‘to  attempt,  try’,  fr.  ad-  and  tentare, temptare,  ‘to  put  to  the  test,  try’.  See  tempt  and cp.  attentat.
Derivatives:  attempt,  n.,  attempt-able,  adj.,  at- tempt-er,  n.
attend,  intr.  and  tr.  v.  —  OF.  atendre  (F.  atten- dre),  ‘to  expect,  wait  for’,  fr.  L.  attendere  ( ani - mum),  ‘to  stretch  one’s  mind  to’,  fr.  ad-  and tendere,  ‘to  stretch,  extend’.  Cp.  It.  attendere, OProven?.  atender,  which  are  of  the  same  ori¬ gin.  See  tend,  ‘to  move  in  a  certain  direction’, and  cp.  tend,  ‘to  attend’.  Cp.  also  contend,  in¬ tend,  portend.
Derivatives:  attendance,  attendant  (qq.v.),  at- tend-er,  n.,  attend-ing-ly,  adv. attendance,  n.  —  OF.  atendance,  fr.  atendant  (F. attendant),  pres.  part,  of  atendre.  See  next  word and  -ce.
=== KLN_1966 leaf 79 ===
  L. aucupdtus,  pp.  of  aucupdre,  later  aucupari,  ‘to go  fowling’,  fr.  auceps,  ‘fowler;  spy,  eaves¬ dropper’,  for  *avi-cap-s,  fr.  avis,  ‘bird’,  and capere,  ‘to  catch,  seize,  take,  receive’.  See  auspice and  captive.
audacious,  adj.,  daring,  bold.  —  F.  audacieux (fern,  audacieuse),  fr.  L.  auddcia,  ‘daring,  bold¬ ness,  courage,  intrepidity’,  fr.  audax,  gen.  au- dacis,  ‘daring,  bold,  courageous,  intrepid’,  fr. audere,  ‘to  dare’,  which  stands  for  *avidire,  ‘to be  eager’,  fr.  avidus,  ‘eager’.  The  meaning  ‘to dare’  first  arose  from  the  negative  form:  non audere  orig.  meant  ‘to  wish  or  to  have  a  mind not  to  do  something’,  whence  it  came  to  denote ‘not  to  risk  or  dare  to  do  something’.  L.  avidus is  a  derivative  of  avere,  ‘to  wish,  desire,  long  for, crave’,  whence  also  avarus,  ‘greedy’.  See  avid and  cp.  avarice.
Derivatives:  audacious-ly,  adv.,  audacious¬ ness,  n.
audacity,  n.,  daring,  boldness.  —  Formed  with suff.  -ity  fr.  L.  audax,  gen.  -dm,  ’bold’,  fr.  au¬ dere,  ‘to  dare’.  See  prec.  word  and  -ity. audible,  adj.  —  ML.  audibilis,  fr.  L,  audio,  audire, ‘to  hear’,  which  prob.  stands  for  * awis-d-id ,  fr. I.-E.  base  *awei-,  *au-,  ‘to  perceive’,  whence  also OL  avifi,  Avestic  avish,  ‘openly,  evidently’,  Gk. alaffdvopai  (for  *4Fia-ff-<xvo[iai),  ‘I  perceive’, afo)  (for  ‘aft. to),  ‘I  hear’  (lit.  ‘I  perceive  by  the
ear’),  OSlav.  ave,  jave,  ‘open,  public’,  aviti, javiti,  ‘to  reveal’.  Cp.  obedient,  obeisance,  obey, oyer,  oyez.
Derivatives:  audibii-ity ,  n.,  audible-ness,  n., audibl-y,  adv.
audience,  n.  —  F.,  fr.  L.  audientia,  ‘a  hearing, audience’,  fr.  audiens,  gen.  -entis,  pres.  part,  o audire.  See  audible  and  -ence. audient,  n.,  a  hearer,  listener.  —  L.  audiens,  gen. -entis.  See  prec.  word  and  -ent. audile,  adj.,  auditory.  —  Formed  with  suff.  -ile fr.  L.  audire,  ‘to  hear’.  See  audible.
Derivative:  audile,  n.,  a  person  whose  imagery is  chiefly  auditory  ( psychol .) audiology,  n.,  the  science  of  curing  defective  hear¬ ing.  —  A  hybrid  coined  fr.  L.  audire,  ‘to  hear’, and  Gk.  -Xoyia,  fr.  -Xoyoi;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  audible  and  -logy.
```


### [2026-09-05T05:23:56.683Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:24:05.258Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 81 82 83; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -n \"^1[0-9][0-9]$\\|^ *1[0-9][0-9] *$\" ; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -3; done"
}
```


### [2026-09-05T05:24:07.069Z] TOOL RESULT

```
=== leaf 81 ===
9:130
10:131
ple.  —  OF. austere  (F.  austire),  fr.  L.  austerus,  ‘dry,  harsh, sour,  tart’,  fr.  Gk.  auax^pit;,  ‘harsh,  rough, bitter’,  fr.  aiisiv,  ‘to  dry’,  fr.  auo<;,  ‘dry’.  See auantic.
Derivatives:  austere-ly,  adv.,  austere-rtess,  n., austerity ,  n.  (q.v.)
austerity,  n.,  the  quality  of  being  austere.  —  OF. austerite  (F.  austiritfi),  fr.  L.  austeritatem,  acc. of  austeritas,  fr.  austerus.  See  prec.  word  and  -ity. Austin,  tnasc.  PN.  —  Abbreviation  of  Augustin (qv.)  ...
=== leaf 82 ===
16:132
50:133
ous-ly,  adv. autogeny,  n.,  autogenesis.  —  See  autogenesis  and -geny.
autograph,  n.,  signature.  • —  L.  autographum,  fr. Gk.  auxdypaipov,  neut.  of  auxoypaqxx;,  ‘written with  one’s  own  hand’,  compounded  of  auxo- (see  auto-)  and  -ypa 905,  fr.  ypatpetv,  ‘to  write’.
See  -graph.
=== leaf 83 ===
33:134
�� (see  Suetonius,  Claudius  2 1).  The  usual  rendering is:  ‘Hail,  Emperor,  who  are  about  to  die  salute you’.  In  fact,  however,  the  Latin  words  express a  perfect  antithesis.  According  to  my  opinion, their  original  meaning  was:  ‘Live,  Emperor! They  who  are  about  to  die  salute  you.’) avellan,  avellane,  adj . ,  pertaining  to,  or  resembling, a  filbert  or  hazel.  —  Fr.  L.  avellana ,  ‘filbert’, shortened  from  nux  avellana,  lit.  ‘nut  of  Avella’, fr.  Avella,  Abella ,  name  of  a  town  in  Campania, abounding  in  nuts.  See  apple.
Avena,  n.,  a  genus  of  grasses;  the  oat  grass  (bot)
—  L.  avena,  ‘oats’,  prob.  formed  fr.  orig.  *avig- snd,  but  influenced  in  form  by  the  ending  of arena,  ‘sand’;  cogn.  with  OSlav.  ovisu,  ‘oats’, Russ,  oves,  Lith.  aviza,  Lett,  auza,  OPruss. wyse,  of  s.m.  Cp.  avener.
```


## [2026-09-05T05:24:11.687Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==82' KLN_1966.txt | sed -n '1,60p'"
}
```


### [2026-09-05T05:24:13.320Z] TOOL RESULT

```
ous-ly,  adv. autogeny,  n.,  autogenesis.  —  See  autogenesis  and -geny.
autograph,  n.,  signature.  • —  L.  autographum,  fr. Gk.  auxdypaipov,  neut.  of  auxoypaqxx;,  ‘written with  one’s  own  hand’,  compounded  of  auxo- (see  auto-)  and  -ypa 905,  fr.  ypatpetv,  ‘to  write’.
See  -graph.
Derivatives:  autograph-y,  n.,  autograph-ical, adj. autogravure,  n.,  a  kind  of  photogravure.  —  A hybrid  coined  fr.  Gk.  aux<S?,  ‘self’  and  F.  gra¬ vure,  fr.  graver  ‘to  grave’.  See  auto-,  grave,  v., and  -ure.
autogiro,  n.,  a  type  of  airplane.  —  Sp.,  compound¬ ed  of  auto-  and  Gk.  yupo?,  ‘ring’.  See  gyre, autointoxication,  n.,  self-poisoning  ( med .)  — Compounded  of  auto-  and  intoxication, automatic,  adj.  —  Formed  with  suff.  -ic  fr.  Gk. ocux6(xaxoi;  (see  automaton);  first  used  by  the English  physician  and  philosopher  David  Hart¬ ley  (1705-57)  in  1748.
Derivatives:  automatic,  n.,  automat ic-al  ,  adj., automatic-al-ly,  adv.
automation,  n.,  a  method  in  which  manufacturing processes  are  automatically  performed  by  self- operating  devices.  —  A  hybrid  coined  by  D.  S. Harder,  a  vice-president  of  the  Ford  Motor
Company,  fr.  automatic  and  suff.  -tion. automatism,  n.,  the  state  of  being  automatic;  in¬ voluntary  action.  —  Gk.  auxo|j.axiapi6?,  ‘that which  happens  of  itself’,  fr.  auxopaxoc.  See  next word  and  -ism.
automaton,  n.,  1)  any  automatic  device;  2)  any living  being  that  acts  automatically.  —  Gk. auxiipaxov,  neut.  of  auxoptaxop,  ‘acting  of  one’s own  will,  happening  of  itself’,  compounded  of auxo-  (see  auto-)  and  I.-E.  *mqtds .  ‘thinking’, fr.  base  *men-,  ‘to  think’,  whence  also  Gk. [jivxoip,  ‘adviser’.  See  mind  and  cp.  mentor. Automedon,  n.,  a  friend  and  charioteer  of  Achil¬ les  ( Greek  mythol.)  —  Gk.  AuxoptiSov,  lit. ‘ruling  by  himself’,  compounded  of  auxo-  (see auto-)  and  piiScav,  [teosoiv,  ‘guardian,  ruler’ (prop.  pres.  part,  of  the  ancient  verb  piiSstv, ‘to  protect,  rule  over’),  fr.  I.-E.  base  *mid-,  ‘to measure,  limit,  consider’,  which  is  a  -rf-enlarge- ment  of  base  *me-,  ‘to  measure’.  See  meditate and  cp.  the  second  element  in  Andromeda  and in  words  there  referred  to. automobile,  adj.  and  n.  —  Lit.  ‘moving  of  itself’, a  hybrid  coined  fr.  Gk.  auxop,  ‘self’,  and  L. mobilis,  ‘movable’ ;  see  auto-  and  movable.  The modern  Greek  calls  it  auxoxlvvjxo,  ‘moved  of itself’  (see  cinema).
Derivatives:  automobile,  n.  and  intr.  v.,  auto- mobil-ism,  n.,  automobil-ist,  n. automotive,  adj.,  self-moving;  automobile;  per¬ taining  to  automobiles.  —  A  hybrid  coined  fr. Gk.  auxoc,  ‘self’,  and  L.  motivus,  ‘moving’.  See auto-  and  motive.
autonomic,  adj.  —  See  autonomous  and  -ic. autonomist,  n.  —  Formed  with  suff.  -ist  fr.  Gk.
aux6vopiop.  See  next  word, autonomous,  adj.  self-governing.  —  Gk.  auxo- vopux;,  ‘living  by  one’s  own  laws’,  compounded of  auxo-  (see  auto-)  and  voptop,  ‘law’.  See  nomo-. For  E.  -ous,  as  equivalent  to  Gk.  -oq,  see  -ous. autonomy,  n.,  self-government.  —  Gk.  auxovopux, ‘independence’,  fr.  auxovoptop.  See  prec.  word and  -y  (representing  Gk.  -(a), autonym,  n.,  a  person’s  own  name.  —  Lit.  ‘one’s own  name’,  formed  fr.  auto-  and  Gk.  ovupia, dialectal  form  of  Svopta,  ‘name’.  See  name  and cp.  onomato-.  Cp.  also  antonym  and  words  there referred  to.
autonymous,  adjv  —  See  prec.  word  and  -ous. autonymy,  n.,  a  word  used  as  a  name  for  itself.  — Compounded  of  auto-,  Gk.  Svupia,  dialectal form  of  Svopux,  ‘name’,  and  suff.  -y;  introduced by  Rudolf  Carnap  (bom  in  1891).  See  autonym and  -y  (representing  Gk.  -la), autoplasty,  n.  ( surg .)  —  Compounded  of  auto- and  -plasty.  Derivative:  autoplast-ic,  adj. autopsy,  n.,  post-mortem  examination  of  a  body. - —  Gk.  auxoijjta,  ‘a  seeing  with  one’s  own  eyes’, compounded  of  auxo-  (see  auto-)  and  S-^iz, ‘sight’.  See  -opsis.
Derivatives:  autopsy,  tr.  v.,  autops-ic,  autops-ic- al,  adjs.
autoptic
132
autoptic,  adj.,  based  on  personal  observation.  — Gk.  fr.  auTOTirr,?,  ‘seeing  oneself’,
which  is  compounded  of  au-ro-  (see  auto-)  and the  stem  of  6i^o;jLa'.,  ‘I  shall  see’,  ‘sight’. See  -opsis  and  cp.  prec.  word, autosuggestion,  n.  —  A  hybrid  coined  fr.  Gk. au-ro?.  ‘self’,  and  L.  suggested.  See  auto-  and suggestion.
autotelic,  adj.,  doing  something  for  its  own  sake.
—  Formed  with  suff.  -ic  fr.  Gk.  au-ra-reXf)?, ‘ending  in  itself’,  which  is  compounded  of  adeo- (sce  auto-)  and  -reXoc ‘end’.  See  tele-.
autotoxin, n.,  toxin  formed  within  the  body  (med.)
—  Compounded  of  auto-  and  toxin, autotype,  n.,  a  facsimile.  —  Compounded  of
auto-  and  type.
autotvpography,  n.,  a  process  of  drawing  designs on  gelatin.  —  Compounded  of  auto-  and  typo¬ graphy.
autumn,  n.  —  OF.  autompne  (F.  automne),  fr.  L. aitlunmus,  which  is  prob.  of  Etruscan  origin.  Cp.
It.  out  anno ,  Rum.  toamnti.  Proven?,  autom,  Sp. otofio,  OPort.  atuno ,  Port,  outono,  ‘autumn  , which  all  derive  fr.  L.  autumnus.  Cp.  also ratoon.
autumnal,  adj.  —  L.  autumndlis ,  ft.  autumnus.
See  autumn  and  adj.  suff.  -al. autumnity,  n.,  the  quality  of  autumn.  —  L.  autum- m'tds,  ‘the  season  of  autumn’,  fr.  autumnus.  See
autumn  and  -ity.
autunite,  n.,  a  hydrous  uranium  calcium  phos¬ phate  (mineral.)  —  Named  after  Autun  in France.  For  the  ending  see  subst.  suff.  -ite. auxano-,  combining  form  meaning  ‘increase, growth’,  as  in  auxanonieter.  —  Gk.  au^avo-,  fr. a u'iveiv,  ‘to  increase’,  which  is  rcl.  to  au?av, of  s.m.,  and  cogn.  with  L.  augere,  pp.  auetus ,  ‘to increase’.  See  auction  and  cp.  auxesis,  auxctic, auxo-.
auxanonieter,  n.,  an  instrument  for  measuring the  growth  of  plants.  —  Compounded  of  auxa¬ no-  and  Gk.  uexpov,  ‘measure’.  See  meter,  ‘poeti¬ cal  rhythm'.
auxesis,  n.,  amplification,  hyperbole  (rhet.)  — Gk.  front  the  stem  of  ooi-xveiv,  ‘to  in¬
crease".  See  auxano-.
auxctic,  auxetical,  adj.,  pertaining  to  auxesis.
Gk.  x'jcrj'.y.o?,  fr.  a’j'r,Tcic,  ‘that  may  be  in¬ creased',  verbal  adj.  of  a’j'xvsiv.  See  auxano-. Derivative:  auxetical-ly,  adv. auxiliary,  adj.  —  L.  auxilidris ,  helpful ,  fr.  auxi- lium,  ‘help,  aid,  assistance,  support’,  which  is rel.  to  augere.  pp.  auetus ,  ‘to  increase  .  See  auc¬ tion  and  adj.  suff.  -ary.
Derivative:  auxiliary,  n.
auxin,  n.,  a  substance  that  stimulates  stem  growth ( biochem .)  —  Coined  fr.  Gk.  aiiEctv,  "to  increase’ (see  auxo-),  and  chem.  sulf.  -in. auxo-,  combining  form  meaning  ‘stimulating growth’.  —  Gk,  ocu^o-,  fr.  au^etv,  ‘to  increase  . See  auxano-.
avail,  intr.  and  tr.  v.  —  ME.  availen,  fr.  OF.  a.
‘to’  (see  a),  and  vail-,  the  pres,  stem  of  valoir,  ‘to be  worth’,  fr.  L.  valere ,  ‘to  be  well,  be  strong, be  worth’.  See  valiant.
Derivatives:  avail,  n.,  avail-abil-ity,  n.,  avail¬ able,  adj.,  avail-able-ness,  n.,  avail-abl-y,  adv., avail-ing-ly,  adv.
aval,  n.,  endorsement  on  a  bill.  —  F.,  fr.  It.  avallo, of  s.m.,  fr.  Arab.  hawdlah,  ‘money  order’,  fr. hita,  ‘he  changed’.
avalanche,  n.,  mass  of  snow  sliding  down  a  moun¬ tain.  —  F.,  fr.  dial.  Swiss  avalantse,  formed  un¬ der  the  influence  of  F.  a  val,  ‘downhill’,  avaler,
‘to  descend’,  fr.  Savoy,  lavantse,  fr.  VL.  *labanca, ‘avalanche’,  which  is  prob.  of  pre-Latin  origin (cp.  the  suff.  -anca  in  *labanca,  which  is  of  Li¬ gurian  origin).  Cp.  OProven?.  lavanca,  ‘ava¬ lanche’,  which  also  derives  fr.  VL.  *labanca.  For another  related  word  of  pre-Latin  origin  sec moraine.  The  derivation  of  VL.  *labanca  fr.  L. labi,  ‘to  glide  down’,  is  prob.  folk  etymology, avale,  tr.  v.,  to  cause  to  descend.  —  F.  avaler,  fr. a  val,  ‘downhill’,  lit.  ‘to  the  valley’,  fr.  a,  ‘to’ (see  a),  and  val,  ‘valley’,  fr.  L.  vallis,  ‘valley  . See  vale,  n.,  ‘valley’,  and  cp.  vendaval. avant-courier,  n.,  a  herald.  —  For  F.  avant-eour- rier,  ‘forerunner’.  See  avaunt  and  courier, avarice,  n.,  greed.  —  OF.  (—  F.)  avarice,  fr.  L. avdritia,  ‘greed’,  fr.  avdrus,  ‘greedy’,  which  is rel.  to  avere,  ‘to  long  eagerly  for,  wish,  de¬ sire’.  See  avid  and  -ice.
avaricious,  adj.,  greedy.  —  F.  avaricieux  (fern. avaricieuse ),  ‘greedy’,  fr.  avarice,  greed  .  See prec.  word  and  -ous.
Derivatives  :uvu/ir/Vj/rv-/v,  ail  v.,u  vunnous-m’ss.  n .
avast,  interj.,  hold!  stop!  ( naut .)  Prob.  cor¬
ruption  of  Du.  houd  vast,  ‘hold  fast  .  Sec  hold, v.,  and  fast,  adj.
avatar,  n.,  descent  of  a  Hindu  deity  (Hindu  my- thol.)  —  OI.  avatdrah,  ‘descent’,  fr.  ava,  ‘down’, and  tdrati,  ‘crosses  over’.  The  first  element  is  rel. to  OI.  avdh,  ‘down,  downward’,  Avestic  ava, ‘down’,  and  cogn.  with  Gk.  au-  (in  aj/aTTeiv, ‘to  go  back,  retire’),  L.  an-,  ’away’  (in  auferre, ‘to  carry  away’,  etc.),  Lith.,  Lett.,  OPruss.  priv. pref.  au-,  OSlav.  u,  ‘at,  with  ,  OIr.  d,  iia,  down, from’;  cp.  the  first  element  in  vesania  and  in vesper.  OI.  tdrati  derives  fr.  I.-E.  base  *ter-, ‘to  pass  beyond,  cross  over'.  See  term  and  cp. words  there  referred  to.
avaunt,  interj.,  begone.  —  F.  avant ,  ‘forward’,  fr. L.  ab  ante,  ‘from  before’,  whence  also  It.  avanti, OSp.,  Port,  avante,  Catal.  avant,  OProven?. avails.  See  advance  and  cp.  ci-devant.  Cp.  also the  first  element  in  vambrace,  vamp,  ‘front  part of  a  boot’,  vamplate,  vanguard,  vanward. ave,  interj.,  i)  hail! ;  2)  farewell!;  n.,  the  salutation ave.  —  L.  ave,  in  vulgar  speech  have,  ‘hail,  fare¬ well’,  fr  Phoen. -Punic,  hawi,  corresponding  to Heb.  hayih,  imper.  sing.  masc.  of  Phoen. -Punic hawd,  resp.  Heb.  hdydf‘,  ‘he  lived'.  Cp.  Plautus, Poenulus,  994,  998,  tool,  and  see  Walde-Hof- mann,  LEW.,  I,  pp.  80-8 1 .  —  The  identity  of  the
133
aviary
Semitic  bases  h-w-h  (h-w-')  and  h-y-h  is  illustrat¬ ed  in  Gen.  3 : 20,  ‘And  the  man  called  his  wife’s name  Eve  (Hawwdh),  because  she  was  the  mother of  all  living  (hay)'.  See  Eve.  For  sense  de¬ velopment  cp.  Heb.  yehi  ddhdnt  hammelekh Dciwidh  I'o/dm:  ‘Let  my  lord  king  David  live  for ever!’  (1  Kings  1:31;  cp.  Dan.  2:4  and  passim), E.  ‘Long  live  the  King!’,  F.  ‘Vive  le  roi’,  etc., all  used  as  formulas  of  greeting.
(The  origin  of  L.  ave  being  thus  established,  we shall  be  able  to  find  the  exact  meaning  of  the words  with  which  the  gladiators  greeted  the emperor:  ‘Ave,  Imperator,  morituri  te  salutant�
```


## [2026-09-05T05:24:23.169Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^west,\\|^west, adv\\|^wester\\b\" KLN_1966.txt | head; echo \"=== find leaf\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'west,  n.' in l or 'west,  adv' in l or re.search(r'\\bwest,\\s+n\\.', l):\n        print('leaf',i)\n        print(l[:20])\nEOF"
}
```


### [2026-09-05T05:24:25.535Z] TOOL RESULT

```
=== find leaf
```


## [2026-09-05T05:24:29.269Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i,l in enumerate(leaves):\n    if 1740 <= i*2 <= 1760 or ('1740' in l and i>800):\n        pass\nfor i in (884,885,886,887):\n    import re\n    nums=re.findall(r'\\n\\s*(1[67]\\d\\d)\\s*\\n', leaves[i])\n    print(i, nums, leaves[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T05:24:36.914Z] TOOL RESULT

```
903
884 [] of  two',  fr.  did,  ‘two’. Derivatives:  twigg-ed,  twigg-
885 [] Truravov, ‘kettledrum’.  See  tympanum  and  subst.  suff.  
886 [] (i.e.  ‘alms,  charity’).  Cp. the  second  element  in  Mel
887 ['1675'] rich’.  The  first  element  is  rel.  to  OE.  eedele, ‘nob
```


## [2026-09-05T05:24:42.816Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'west,?\\s+n\\.,?\\s+(the|one)', l) or 'Wes-to' in l or 'wes-to' in l or \"‘west’\" in l and 'OE.  west' in l:\n        print('---leaf',i)\n        j=l.find('west')\n        print(l[max(0,j-200):j+1400])\n        break\nEOF"
}
```


### [2026-09-05T05:24:44.718Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:24:46.912Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Westen\\|OE\\.  west\\|vestr,\\|westar\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T05:24:46.974Z] TOOL RESULT

```
35365:Derivative:  sissy-ish,  adj. sister,  n.  —  ME.  sister,  of  Scand.  origin;  cp.  ON. systir,  Swed.  sister,  Dan.  .tester,  which  are  rel. to  OE.  sweostor,  swustor,  OS.  swestar,  OFris. swester,  suster,  MDu.  suster,  Du.  zuster,  OHG., MHG.  swester,  G.  Schwester,  Goth,  swistar, from  I.-E.  base  *swesdr,  whence  also  OI.  svasar-, Avestic  xvatjhar-,  Toch.  A  sar,  B  ser,  Arm.  k'oir, L.  soror,  OSlav.  sestra,  OPruss.  swestro,  Lith. sesud,  OIr.  sittr,  W.  chwaer,  OCo.  huir,  ‘sister’, Gk.  lop  (in  the  vocative  Sop).  I.-E.  *swesor  is compounded  of  the  reflexive  base  *swe-,  ‘his, one’s  own’  (see  sui)  and  -sor,  ‘woman’,  fr.  I.-E. *ser-,  ‘woman’,  which  appears  also  in  the  OI. fern,  forms  tisrdh  (dissimil.  fr.  *tri-sor ),  ‘three’, and  catasra(i,  ‘four’.  Accordingly  sister  orig. meant  ‘the  woman  belonging  to  one’s  own kindred’.  Cp.  cousin,  cozen,  sorority. Derivatives:  sister,  tr.  v.,  sister-hood,  n.,  sister¬ ly,  adj.,  sister-li-ness,  n.
```


## [2026-09-05T05:24:49.792Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"vesper\" KLN_1971.txt | head -5; echo ===; grep -n \"westan\\|OE. west\\|OHG. westan\" KLN_1971.txt | head -5"
}
```


### [2026-09-05T05:24:49.866Z] TOOL RESULT

```
Exit code 1
8270:‘vespertine, western’. Cp the second element in 
23740:vesper. OI. tarati derives fr. I.-E. base *ter~, 
113038:L. vesper, ‘evening’. See vesper. 
162133:word), on the analogy of vesper-tilid, ‘bat’. 
183086:through metathesis fr. L. vespertilid, ‘bat’. See 
(eval):1: == not found
```


## [2026-09-05T05:24:51.502Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8240,8290p' KLN_1971.txt"
}
```


### [2026-09-05T05:24:51.570Z] TOOL RESULT

```
Derivative: advocate , tr. v. 
advocation, n. — L. advocatio, gen. -dnis, ‘a cal- 
ling to’, fr. advoedtus , pp. of advocare. See ad- 
vocate and -ion and cp. advowson, which is a 
doublet of advocation. 

advowson, n., the right of presenting a nominee 
to a church benefice. — ME. avoweisoun, fr. 
OF. avoeson , fr. L. advocationem , acc. of advo- 
catio. See advocation. 

adynamia, n., lack of vital force ( med .) — Gk. 
dSuvajjLia, ‘want of strength, debility’, fr. 4- 
(see priv. pref. a-) and 8uvxp.tp, ‘power, strength’ . 
See dynamic and -ia. 

adynamic, adj., weak. — Formed fr. prec. word 
with suff. -ic. 

adytum, n., 1) the innermost part of a temple; 
2) a sanctum. — L., fr. Gk. 48 utov, ‘innermost 
sanctuary’, lit. ‘a place not to be entered*, subst. 
use of the neut. of the adj. 48 uxo<;, ‘not to be 
entered’, fr. 4 - (see priv. pref. a-) and Sueiv, 
‘to sink into, plunge into, penetrate into, dive, 
enter’; ‘to put on’ (lit. ‘enter into’) clothes; ‘to 
set’ (prop, ‘to dive into the sea’ ; said of the sun 
and stars), which is cogn. with OI. upa-du, ‘to 
put on (clothes)’, and perh. also with OI. dosd, 
‘vespertine, western’. Cp the second element in 
Anadyomene, Aptenodytes, eedysis, Endymion, 
endysis, ependyma. 

adz, adze, n., an axlike tool. — OE. adesa, ‘ax’, 
fr. OF. aze, a secondary form of aisse, ‘ax’ fr. 
L. ascia, ‘ax, adz’, which is metathesized fr. 
*acsia and cogn. with Gk. 4 £fvq, ‘battle ax, ax’, 
Goth, aqizi, OE. eax, sex, ‘ax’. See ax. 
Derivative: adz-er , n. 

Aeacus, n., one of the three judges in Hades, 
famous for his piety and prayers (1 Greek mythol .) 

— L„ fr. Gk. Alax6<;, a word of uncertain 
origin. It is possibly rel. to ald^eiv, ‘to wail, 
lament’, which derives from the interj. at, ‘ah’. 

Aechmophorus, n., a genus of large grebes ( zool .) 

— ModL., fr. Gk. atxjio96poc, ‘spear bearer’,
```


## [2026-09-05T05:24:54.498Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^west, \\|^west,\" KLN_1971.txt | head; echo ===; grep -n \"‘west’\" KLN_1971.txt | head -10"
}
```


### [2026-09-05T05:24:54.560Z] TOOL RESULT

```
Exit code 1
266215:west, adv., adj. and n. — ME., fr. OE. H’<?sr(adv.), 
(eval):1: == not found
```


## [2026-09-05T05:24:56.586Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '266205,266260p' KLN_1971.txt"
}
```


### [2026-09-05T05:24:56.666Z] TOOL RESULT

```
hero of the novel Die Leiden des jungen Werthers 
by the German poet Johann Wolfgang von 
Goethe (1749-1832). 

Wesleyan, adj., pertaining to John Wesley, found- 
er of Methodism (1703-91). — For the ending 
see sutf. -an. 

Wesleyanism, n., doctrine of the Wesleyans. — 
Formed from prec. word with suff. -ism. 
west, adv., adj. and n. — ME., fr. OE. H’<?sr(adv.), 
‘to the west’ (whence also F. ouest, ‘west’), rel. 
to ON. vestr , Dan,, Swed. vest, OFris., MLG., 
MDu., Du. west , OHG. -west (only in com- 
pounds, whence MHG., G. west), the enlarged 
forms OHG. westan, MHG., G. westen, ‘west’, 
fr. Teut. *west-, which is prob. an enlargement 
of I.-E. *we-, ‘to go down’, whence also OI. 
avdh, ‘down, downward’. Cp. I.-E. *we-spero, 
whence L. ve-sper, ‘evening’, Gk. garcepoc (for 
•fe-airepot;), Ia7repa (for *fE-a7repa), ‘eve- 
ning’. OE. west, etc., orig. meant ‘the region 
where the sun sets’ (lit. ‘goes down’). See vesper 
and cp. words there referred to. Cp. also the 
first element in Visigoth. 

Derivatives : wester (q.v.), western (q.v.) 
wester, intr. v. to go or turn westward. — ME. 
westren, formed fr. west with suff. -ren. See west. 
Derivatives: wester-ing, adj. and n. 
westerly, adj., pertaining to the west; western. — 
Formed with adj. suff. -ly fr. obsol. E. wester, fr. 
ME. wester, fr. OE. westra, ‘more toward the 
west’, which was formed fr. west with compar. 
suff. - ra . See west and compar. suff. -er. 
western, adj. and n. — ME. westeren , westerne , 
fr. OE. westerne. See west and -ern. 

Derivatives: western-er , n., western-ize, tr. and 
intr. v., western-iz-ation, n. 



westward, adj. — ME., fr. OE. westeweard. See 
west and -ward. 

westward, westwards, adv. — See prec. word and 
-wards. 

wet, adj. — ME. we/e, wette, partly fr. pp. of 
weten , ‘to wet’, partly fr. OE. wxt, ‘wet’, which 
is rel. to OFris. wet, ON. vdtr, Swed. vat, Dan. 
vaad , ‘wet’, and to OE. wxter, ‘water’. See water. 
Derivatives: wet, n., wet, v. (q.v.), wet-ly , adv., 
wet-ness, n., wett-ish, adj. 
wet, tr. v. — ME. weten, fr. OE. wxtan, ‘to wet’,
```


## [2026-09-05T05:25:08.909Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 126 127; do echo \"=== HRN leaf $n (p.$((n-21))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-05T05:25:10.540Z] TOOL RESULT

```
=== HRN leaf 126 (p.105) ===
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
=== HRN leaf 127 (p.106) ===
— 105 —
. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
phlv. /arböjhia, kharbuzak (PP61.), vergl. höjlna =
/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
V
(FS); die letzteren beiden neupersischen Worte sind
nur Fehle vlumschriften, noch mit aramäischem -a.
Vergl. NT2il2, de Lagarde, Semitica 56.
Weit gewandert, vergl. türk. qarpuz etc.
>. y^ereeuf/ *Krebs', vergl. kilinjar, kulenöek (Wo Ilaston:
karanjäl, kalanjär).
skr. vergl. karkiffa- 'Krebs, Krebs im Tierkreise'
(karkä- etc. sind bedenklich) ; phlv. karcany 'Krebs im
Tierkreise (Bund.); gr. -^nQy.lvo^ 'Krebs', vergl. md^j/ar
yjumi'oi 2itY.t\oi , Hesych.; lat. Cancer wird ebenfalls
dazu gehören (vergl. Brugmann, Grundriss, I, § 282
Ende). / ist erst neupersisch.
>. -/ired 'Verstand*.
aw. /ratu- 'Verstand'; phlv. xrat, /j'attk[tum (vd.
19 (47), arm. LW. /art)\ ai. krdtU",
\ yiirs 'Bär.
aw. aresa- *Bär (Aog.) ; phlv. xO)^^ (Bund.) ; ai. /ksa- ;
arm. arj (H. No. 46).
oss. d. t. a7's (85); siyn. ytir}, sar. yürx,
Aw. Ere/sa-, vergl. ai. Ärksa- (Goldschmidt bei
Nöldeke, ZDMG. 86, 447) sind hiervon zu trennen,
vergl. Hübsch mann, ZDMG. 38, 429; anders Bar-
tholomae, Studien II, 21.
B. yftirsend ^fröhlich, zufrieden .
aw. ^hurasant-; phlv. /ursand 'zufrieden, fröhlich*
(Bund., Men.), /ursandih (AV.).
Darmestete r. Et. ir. I, 265; die päz. Aussprache
X'arsand spricht allerdings gegen diese Etymologie,
doch kann sie nicht ausschlaggebend sein.
'j Brugsch, Reise der K. Preuss. Gesandtschaft nach Persien
: vermug Band und Seitenzahl augenblicklich nicht anzugeben) hat
i eine nicht sehr geistreiche Volksetymologie des Wortes aufbinden
en.
```


## [2026-09-05T05:25:30.960Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^xwarsand\\|xwarsand\\|hwarsand\\|xursand\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20; echo \"=== obard\"; grep -n \"^ōbār\\|obārdan\\|ōbārdan\\|ōbārd\\|ʾwbʾl\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20; echo \"=== oftadan\"; grep -n \"^ōbast\\|ōftād\\|ʾwpt\\|obast\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T05:25:31.054Z] TOOL RESULT

```
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
=== obard
=== oftadan
PHD_mackenzie.txt:3836:·obad-,v.obastan,·oftadan.
PHD_mackenzie.txt:3838:obastan, .obad- [NPLWN-stn l < A ...; npl; )wpstn', )wpt- (if not oft-,
PHD_mackenzie.txt:6538:evil-minded duswir.                                fall kaftan, obastan, Oftiidan, pad-.
PHD_mackenzie.txt:9965:obastanl           \'~ \~Q)\            wistax                   ,~~,
PHD_mackenzie.txt:11864:hucasmih                ~qt""              obastan                    \\M» Q)yt
```


## [2026-09-05T05:25:44.909Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3820,3850p' PHD_mackenzie.txt"
}
```


### [2026-09-05T05:25:44.980Z] TOOL RESULT

```
nizarih- [nz)lyh-] become weak.
no [TSA < A tS' I M nwlt, N nuh] nine.
nog [1l'1:ck l I 1\'1 nwg, N llfl'lv] new, recent.
 --roz [-lwe I N nawroz] New Year's day.
 .......-zad(ag) [-Z)t(k)' I N nawzad] new-born.
nohom [nhwm I = M, N -] ninth.
ni)zdah [nwzdh IN .......] nineteen.
nun [KON < A k<ll I M, J nwn] now.



                                     o
o [OL < A <l: )w I M )w] to, at: v. also oh.
 - gird amadan: gather, collect (intr.).
 - ham kardan: gather (tr.).
 - ham madan: gather (intr.); come to an end.
·obad-,v.obastan,·oftadan.
obardan, obar- [)wp)l-tn' I M )wb)rd] swallow, devour.
obastan, .obad- [NPLWN-stn l < A ...; npl; )wpstn', )wpt- (if not oft-,
  q.v.) I M )wbyst, J )w,8st-] fall.
·oftadan, Oft- [)wpt- I M )wpt)d, N uft-] fall.
ogar [)wk)l] ebb.
ogardan, ogar- Cwk)l-tn ] remove, expel.
*ogra [)wgl)y] declination,' dip.
oh [KN < A kn I M )wlt] so, thus: (with verbs, giving a sense of uncertainty)
  may, perhaps.
Ohrmazd [)whrm:;:d I M )whrm(y)zd, N H6rmuzd] Ahura Mazda: astr.
  Jupiter: cal. 1St day of the month.
-om [-wm I = M, N .......] suffix forming ordinal numbers from panJom
  onwards.
-omand [-)wmnd I M -wmnd, N -mand] suffix forming adjectives of
```


## [2026-09-05T05:25:46.215Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"obar\\|ōbār\\|obārdan\" PHD_mackenzie.txt | head -20; echo === ; grep -n -i \"sand.*seem\\|\\*sand\\b\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T05:25:46.287Z] TOOL RESULT

```
Exit code 1
3837:obardan, obar- [)wp)l-tn' I M )wb)rd] swallow, devour.
10837:gilagobar               ~Q),....r                   sust
11923:obar-                      -\...~~         uspurrig                  \~\b''''
11924:obardan                 '\~tJ'"            hangezisn                  ,r-uCl»~
(eval):1: == not found
```


## [2026-09-05T05:25:59.864Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ōbārdan\\|obārdan\\|ōbār-\\|aw-bār\\|ʾwbʾr\" CHEUNG.txt | head -20; echo \"=== bar1\"; grep -n \"^\\*bar\\|\\*bar- .*carry\\|to carry, bring\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T05:25:59.947Z] TOOL RESULT

```
=== bar1
1700:*bar ‘to bring, carry’ 
1723:*bar 7 
1824:*bar 9 
1832:barda/ber-, Varz. barte/ber- ‘to carry, bring (to)’, Nn. barte/bir- ‘to carry off, take 
1882:‘to carry, bring’, Arm. berem ‘I carry, bring’, Alb. bie ‘I carry, bring, lead’ 
1894:*barH ‘to move rapidly ? 
1924:*barj ‘to praise, honour’ 
1931:*barj 11 
2044:*barz! ‘to make high’ 
2052:*barz2 13 
2096:*barz? ‘to cover, cushion’ 
14495:settle’, (?) Wa. yund-/yut- ‘to carry, bring; to marry (wife)’ 
18423:catch (birds, animals)’ || (+ *upa-) Yi. van-/vad-, M. vín-/vád- ‘to carry, bring, carry 
27391:*bar ‘to carry, bring’, *pari-bar, as suggested by Samadi. || The Chor. forms cannot 
55187:*bar (s.v.), *cai', *daiz (s.v.), 
55612:*bar, *tauH (s.v.), *xsamH 
55785:*baru', *iah, *urad (s.v.) 
55858:*bary! 
55860:*bar, *Haz (s.v.), *Huad 
55896:*bar, *cap (s.v.), *gam' (s.v.),
```


## [2026-09-05T05:26:01.696Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1700,1900p' CHEUNG.txt"
}
```


### [2026-09-05T05:26:01.759Z] TOOL RESULT

```
*bar ‘to bring, carry’ 

*AVESTAN: bar- ‘to bring, carry’ || (+ *ati-) ‘to carry over, to’ || (+ *apa-) ‘to take, 
carry away, off’ || (+ *abi-) ‘to procure’ || (+ *aua-) ‘to bring down, insert; to take 
out (clothes) from above’ || (+ *ä-) ‘to carry with; to bring to’ || (+ *upa-) ‘to bring 
on’ || (+ *uz-) ‘to bring, carry out’ || (+ *pati-) ‘to bring back; to commence’ || (+ 
*para-) ‘to carry off, forth’ || (+ *pari-) ‘to take around ? || (+ *fra-) ‘proferre, to 
carry, bring forward to, offer’ || (+ *niZ-) ‘to take, carry, bring out’ || (+ *ui-) ‘to 
separate, split, divide’ || (+ *ham-) ‘conferre, to take, bring together, collect’ 


c» Liste: 37 

Pres. them.: IND. Isg. YAv. barämi (Yt 5.77, FrK 12, FrW 7.2), YAv. auui.barämi ! (Yt 8.25, cf. 
Panaino, Тїї. I: 116), med. Y Av. baire (Yt 14.57), 2sg. Y Av. Багам (Yt 10.23), YAv. auua.barahi (Yt 
10.23), med. YAv. barahe (at 50), 3sg. baraiti (Y 31.12, Y 50.6, Y 38.1, etc.), YAv. apa.baraiti (V 
5.38), ҮАУ. abaraiti (Yt 14.12), YAv. upa.baraiti (Yt 17.58, N 103), YAv. vi.baraiti (V 8.80), med. YAv. 
baraite (Yt 13.18, F 240), 3du. YAv. ham barato (Yt 8.22), med. Y Av. “baraéte (F 240), Ipl. ҮАУ. 
ham.baramahi (V 5.39), med. YAv. pairi.baramaide (Yt 11.7), 3р1. YAv. baronti, YAv. äbaronti (Yt 
14.55), med. Y Av. auua.baronte (Yt 5.15, Yt 8.47), Y Av. uzbaronte (Yt 13.65, V 8.14), YAv. frabaronte 
(Yt 5.94), INJ. 1sg ҮАУ. uzbarom (V 20.4), Y Av. frabarom (V 2.6), Y Av. niZbarom (Yt 4.5), med. YAv. 


*bar 7 


uzbaire (Yt 5.6), 3sg. YAv. barat, YAv. apa.barat (V 9.51), YAv. upa.barat (V 2.33, V 2.35 f., V 2.38, 
etc.), med. YAv. barata (Yt 19.29, Yt 19.33 f.), 3pl. YAv. baron (Yt 13.1, Yt 13.19), YAv. vibaron (Y 
10.11), SUBJ. 159. ҮАУ. Багат (Yt 5.63, Yt 15.12, V 19.12), ҮАУ. apa.baräni (Yt 9.10), YAv. apabarani 
(Yt 10.111), 2sg. YAv. barahi (Vyt 50), YAv. paiti.barahi (Y 55.4), 3sg. YAv. barat, YAv. vi.barat (N 
108), 3du. YAv. barato, 1р1. YAv. barama (V 6.44, V 6.49), 3р1. YAv. paiti.baranti (N 54), ҮАУ. aiti 
baran (V 5.41 f£), YAv. para.baran (V 3.27), ОРТ. 25е. YAv. baröis (Yt 10.23), YAv. apa.barois (V 
17.4), YAv. abarois (V 17.5, V 17.7), Y Av. frabarois (Y 65.10, V 19.21, V 19.24, etc.), 3sg. YAv. baroit, 
Y Av. auuaröit (Yt 10.73), Y Av. uzbaröit (V 6.27), med. 3sg. YAv. baraeta (V 12.2), 3pl. YAv. Багайәп 
(V 5.40, V 8.2, V 82, V 8.8, etc.), IMPV. 25р. YAv. bara, YAv. upa.bara (V 2.25, V 2.27 f., V 2.30), 
med. Y Av. ham baranha (Yt 10.32), 2pl. YAv. barata (N 103C). 3р1. Y Av. barontu (Yt 13.157); Aor. 
athem.: IMPV. 3g. OAv. barotü (Y 33.9), med. ? YAv. borotam (H 2.18); Perf.: IND. 3sg. ҮАУ. 
frabauuara (Yt 10.79), 3pl. YAv. baBrara (Y 65.6), ОРТ. 3pl. ҮАУ. auui.baßriian (Yt 8.24); Partic.: pres. 
Y Av. barant- (Y 52.2, Yt 8.40, Yt 13.136, etc.), med. YAv. baromna- (Yt 13.121, V 6.26, V 8.73, etc.), 
perf. pass. Y Av. borota- (Y 62.9, Vr 2.11, Vyt 64), Y Av. aborota (Yt 17.14); Pass.: pres. IND. 3sg. YAv. 
Баігііеіе° (У 5.40), 3р1. YAv. bairiiente (V 3.29), SUBJ. 3pl. OAv. bairiianté (Y 32.15); Caus.: pres. IND. 
3р1. YAv. hanbäraiieinti (Yt 6.1, rep.), INJ. 3sg. YAv. uzbäraiiat (V 19.19), SUBJ. 3sg. ? ҮАУ. 
*uzbàraiiat (У 18.10), 1р1. YAv. ham.baraiiama (V 19.44 Ё), OPT. 3pl. YAv. uzbäraiion (Yt 8.58, Yt 
14.50), Y Av. frabaraiion (V 9.39), Y Av. niZbaraiion (V 6.29, V 6.31, V 6.37), YAv. ham.bäraiion (V 
4.44) 

*OLD PERSIAN: bar- ‘to bear, lift, esteem’ || (+ *4-) ‘to perform’ || (+ *pati-) ‘to bring 
back’ || (+ *pari-ä-) ‘to bring back, restore’ || (+ *para-) ‘to bear way, take away’ || 
(+ *fra-) ‘to offer, grant’ => Kent: 200a 

Pres. them.: IND. 15р. paribaramiy <p-r-b-r-a-mi-i-y> (DNb 17), 35р. äbaratiy (+ а) <a-b-r-t-i-y> (DNb 
25), 3р1. bara"tiy <b-r-t-y> (DB 5.22), <b-r-t-y> (DNa 42), impf. 1sg. abaram <a-b-r-m> (DB 1.22), 
<a-[b]-r-m> (DB 4.66), 35р. abara <a-b-r> (DB 1.25, DB 1.55, DB 1.88, DB 1.94, etc.), <a-b-r> (2.34), 
<a-[b]-[r]> (DB 3.87), <a-b-r> (DNa 50), 3pl. abara <a-b-r> (DPe 10), <[a]-[b]-r> (DSf 34), abarahan 
<a-b-[r]-h> (DNa 19), ? <a-b-r-n> (XPh 17), med. 3pl. abara'tà <a-b-r-t-a> (DB 1.19), SUBJ. 25р. 
paribarahy <p-r-i-b-r-a-h-y> (DB 4.78), paribarah" (+ pron. -dis) <p-r-i-b-r-a-h-°> (DB 4.74), IMPV. 25р. 
paribara <p-r-i-b-r-a> (DB 4.72, DB 4.88), 35р. baratuv <b-r-tu-u-v> (DPd 14, DSk 5); Partic.: perf. pass. 
"brta- (+ u- ‘good, well-’) «?-b-r-t-^» (DB 1.21, DB 4.66); Inf.: bartanaiy <b-r-t-[n]-[i]-y> (DNb 47); 
Pass.: impf. IND. 3sg. abariya <a-b-[r]-i-y> (DSf 31), <a-[b]-[r]-i-y> DSf 35), <a-b-r-i-y> (DSf 36, DSf 
40, DSf 45), <a-b-r-i-y> (DSf 38), < [a]-b-r-i-y> (DSf 43), 3р1. abariya" <a-b-r-i-y> (DSf 41, DSf 47) 
*MIDDLE PERSIAN: MMP br-, BMP bl- (YBLWN-) ‘to carry, bear, take, endure’ || (+ 
*ара-) MMP ’pr-, MMP ’pwr-, BMP "pwl- /appur-/ (sec. stem) ‘to carry off, steal’ || 
(+ *a-) MMP "'wr-, BMP ’wwl- (YHYTYWN-) /awar- ‘to bring’ || (+ *pari-) BMP 
plyw'l /parwär/ ‘citadel; circumvallation; suburb, surroundings’ || (+ *niz-) MMP 
nzbwrd (pret. stem) ‘to humiliate’, BMP nzbwityhy /nizburdthi/ ‘humiliation, 
abasement' || (+ *ш-а-) MMP wy’wr- ‘to talk, speak; to answer’ (Pth. ?) || (+ *ham-) 
MMP hmb’r-, BMP hnb’I- /hambar-/ ‘to fill, collect’. Ф The etymology of Nyberg II: 
28b (and accepted by Back 1978: 176 f.) for BMP ’pwl- /appur-/ is unacceptable. 
The reconstruction *apa-par- (*par? ‘to go over, cross over’) is hardly possible, as 
the preverb *apa- ‘off, away’ is semantically incongruous with the root *par?. 
> DMMPP: 109 f., 50, 70a, 351a, 257a, 178a 


8 *bar 


Widely attested: Pres.: IND. 1sg. MMP brwm, 3sg. MMP bryd, 1р1. MMP brym, 3р1. MMP brynd, etc. || 
(+ *ара-) Pres.: IND. 3sg. MMP ’pwryd, ВМР "pwlyt /appuréd/, 1р1. ВМР "pwlym /appurém/, SUBJ. 
lsg. MMP *’pr’n, 3sg. MMP ’pr’d; Partic.: perf. pass. MMP ’pwrd; Inf.: MMP *’pwrdn || (+ *à-) widely 
attested: Pres.: IND. 25р. MMP "wryy, 3sg. MMP ’’wryd, etc. || (+ *ш-а-) Pres.: IND. 3sg. MMP 
wy’wryd, 3pl. MMP “wy’wrynd, IMPV. 2pl. MMP wy’wryd; Partic.: perf. pass. MMP wy’wrd || (+ 
*ham-) Pres.: IND. 1р1. MMP hmb’rwm, MMP hmb’rym, 3р1. MMP hmb’rynd; Partic.: pres. pl. MMP 
hmb’r’g’n 

*PARTHIAN: br- ‘to carry, bear, bring’ || (+ *ā-) ”’wr- ‘to bring’ || (+ *pari-) IPth. 
prybr ‘surroundings’ || (+ *ui-à-) wy’wr- ‘to talk, speak; to answer’ || (+ *ham-) 
"mb'r- ‘to amass, collect? = Ghilain: 58, 57 | DMMPP: 109 f., 70a, 351a 

Pres.: IND. 2sg. bryh, 35р. bryd, 3р1. brynd, SUBJ. 1sg. br’m, 2sg. br’h, 3sg. br’h, OPT. 3sg. "bryndyh, 
IMPV. 2sg. br; Partic.: perf. pass. bwrd; Inf.: bwrdn || (+ *a-) Pres.: IND. 3sg. *’wryd; Partic.: perf. pass. 
"wrd || (+ *ui-a-) Pres.: IND. 1р]. wy’wr’m, 3pl. wy’wrynd, 35р. wy’wr’, IMPV. 25р. wy’wr, 2pl. 
wy ’wryd; Partic.: pres. wy’wr’g, perf. pass. wy’wrd || (+ *ham-) Partic.: pres. ’mb’rg ‘collector, gatherer’ 
*KHOTANESE: bar- ‘to carry’, (med.) ‘to ride’ || (+ *ati-) ttuvar- ‘to bring’ || (+ 
*para-) puror- ‘to take away’ || (+ *fra-) haur- ‘to give’, haura- ‘word’ || (+ *ni- or ? 
*anu-) LKh. *nuvar- (nvid-, nud-) ‘to offer’ = SGS: 93 f., 39, 85, 155, 59 
*SOGDIAN: SSogd. Br-, BSogd. Br-, CSogd. br-, MSogd. Br- ‘to bear, take, perform’ || 
(+ *apa-fra- ?) ? SSogd. ’pößyr (caus.) ‘to let give’ || (+ *a-) BSogd. "Gr CSogd. 
"br, CSogd. "Dr ‘to carry’, MSogd. "Br ‘to carry’ || (+ *uz-) CSogd. ’zBr- ‘to cross 
(river)’ || (+ *para-) SSogd. pr’Byr (pass.) ‘to be delivered’ || (+ *pari-) SSogd. 
prB’yr, BSogd. prB’yr, CSogd. prbyr, MSogd. prB’yr (caus.) ‘to explain, expound, 
relate’ || (+ *fra-) SSogd. ößr-, BSogd. öß’r-, CSogd. Obr-, MSogd. dBr- ‘to give’ || (+ 
*ш-) MSogd. yB’r- ‘to take care of || (+ *ш-а-) BSogd. wy’’Br, MSogd. wy Вг ‘to 
speak, say’ || (+ *ham-) BSogd. ’nßrt "kw ‘in brief? 

Widely attested: Pres.: IND. 15р. SSogd. Br’m, 2sg. dur. CSogd. brysq, 3sg. BSogd. prt, Brt’, Brty, CSogd. 
brty, MSogd. Brty, dur. BSogd. Brty ’skwn || (+ *ui-) Partic.: pres. MSogd. yB’ryny || (+ *ui-ä-) Pres.: 
IND. 3sg. BSogd. wy’’Brt, BSogd. wy’ ’Brty; Impf.: IND. 35р. BSogd. wy’ Br, Partic.: pres. "wy’bryny, 
CSogd. wy’brn’, CSogd. wy’brnyt pl. ‘speaking, capable of speech’ 

*CHORESMIAN: Вг- ‘to bring; to fast’ || (+ *ati-) cBr- ‘to lean on, put in, insert’ || (+ 
*а-) m/’B’ry- ‘to forgive’ || (+ *upa-) bBr- ‘to declare, speak; to describe’, (intens.) 
bB’ry- ‘to explain, expound; to inform’ || (+ *ni-) m/nB’ry- ‘to treat (wrongly), get 
(someone) into trouble’ = Samadi: 40, 49, 1, 13, 150, 86 f., 118 

*BACTRIAN: Bap- ‘to bear, bring, take’, -Bapo poss. suff. || (+ *a-) оВоро ‘delivery’ || 
(+ *uz-) об(о)Вор- (обоВор-, eCBap-) ‘to bring forth, produce’ (supplet. aGyado, 
s.v. *gam-) || (+ *para-) napoßap- ‘to bring forth, produce’ || (+ ham-) 
anßapo-Bıpsadoyo, apBapo-BipoapAoyo ‘store-keeper’ = S-W, Bact.: 173, 178a, 
216b, 179b 

*NWIR: Widely attested: NP burdan/bar- ‘to carry off, take’, Bal. burt/bar- ‘to carry, 
bring’, Kurd. birin/bi-, birdin/ba(r)-, biran/biré-, Anar. barte/bir, Awrom. 


*bar 9 


bardäy/bar-, Jow. bam-ba(r)t/a-ber-, Shamerz. -vórd-/berán- ‘to take, carry (away, 
off)’, Awrom. berd/ber-, Gur. (Kand.) bärd-/-ir- (subj./impv. bär-) ‘to carry off’, 
Zaz. berdis/ben-, (subj.) ber-, Abz. barda/bor-, ber-, Abyan. barda/bar-, Fariz. 
-bärd-/-bär-, Yar. -Бага-/-Баг-, Ham. bärtan/ber-, Isfah. bärtän/bär-, Jow. 
bam-ä:rt/a-ta:r-, Meim. bem-ba/a-ber-, Mah. bir-, Natan. -bord-/bor-, -bär-, Qohr. 
barda/ber-, Varz. barte/ber- ‘to carry, bring (to)’, Nn. barte/bir- ‘to carry off, take 
away’, Khuns. ber-, bir-/birt ‘to carry (away); to win (in games)’, Semn. bärd-/-bär 
‘to carry away, forth’, Sang. -bart-/bänd-, (subj./impv.) -bär-, Soi -bär-, Sorkh. 
-Bord-/ (supplet. bé-n-, be-nn- < *naiH!), Lasg. -bard-/ (supplet. pres. Isg. bi-n < 
*naiH!) ‘to bring, carry (away, along)’ || (+ *2-) NP ävurdan/ä(va)r- ‘to bring’, Kurd. 
(Sina) hawirdin/er-, Awrom. awirdáy/-ar- ‘to bring; to set to’, Abyan. агаап/ (subj.) 
b-or-, Anar. -iyorto/iyor-, Bakht. avérdan, Fariz. -t-är-/-m-ärd-, Yar. -t-är-/-m-ärd-, 
Gil. (Rsht.) avárdaen/zvár-, Gur. (Kand.) -awürd-, äwird-/-är-, Ham. artän/ar-, Isfah. 
arän/ar-, Jow. bam-ä:rt/a-ta:r-, Meim. bem-t-/a-tar- (infl. caus. of *tarH! ?), Khuns. 
ar-/art, Khr. bi-oword-, bi-owurd-, Mah. 4r-, Nn. yart/t-ar-, Natan. -ärd-/-är- ‘to 
bring, fetch’, Semn. ävärd-/ bi-ar-‘to bring’, Shamerz. -ord-, urän-, Sorkh. -cerd-/ 
(supplet. a-vi-n-, a-ve-n- < *4- + *паіН!), Lasg. -ord-/ (supplet. ó-ví-n < *4- + 
*паіН!), Sang. -jórt-/ (supplet. ä-vä-n- < *4- + *naiH!) ‘to bring, lead’ || (+ *fra-) 
Kurd. (Kurm.) farwar(a) (f.) ‘favour; gift, present’ || (+ *ham-) NP anbar ‘ricks, 
stacks of corn’ 

*NEIR: Oss. I. baryn/barst, D. barun/barst ‘to contemplate, measure’; to forgive’, 
Pash. wr-/wral ‘to carry (something), Sh. var-/vud, Orosh. var-/vug, Sariq. 
vor-/vewg, Yzgh. var-/vag, Yghn. var-/vurta, várta ‘to bring’, Wa. vər ‘load, 
burden’ || (+ *ati-) Yghn. divar-, dévar-/déwar-/ (supplet. diyáta < *ati-gam-) ‘to 
insert, introduce’ || (+ *à-) Yi. avor-/avor, M. aver-/aver- ‘to bring (something)? || (+ 
*para-) Yzgh. porvar-/*porvag ‘to drag across’, Khf. parfur ‘transfer of hay or 
sheaves to the carrying frame’ || (+ *fra-) Oss. I. læværd, D. lavard (pret.) ‘gave’ 
(supplet. of deddyn, D. daeddun, s.v. *daH'), (orig. caus.) ? Sh. (Baj.) rivir-/rivirt ‘to 
force a cow to give milk’, Oss. lavar ‘gift, present’, Yghn. tifar-, téfar-, tfar-/tiráfta, 
térafta “о give’ (see Sogd.) || (+ *ni-) Yi. navor-/navar-, M. never- ‘to take out, draw 
out’, Wa. navoir ‘provision (on the way)’ || (+ *niZ-) Yghn. Zivar-, Zévár-, Ziwár-/ 
(supplet. Ziyäta < *niz-gam-) ‘to bring, lead, drag, pull out’ || (+ *ui-) Oss. ivar 
“punishment, prohibition’ (< *‘act of carrying away, confiscation’) || (+ *ham-) Oss. 
І. embaryn/emberst ‘to understand, comprehend’, (old ppp.) І. zmbyrd, D. 
amburd ‘meeting’ 

*MISC: Par. bar-/bur ‘to carry’ || (+ *ара-) Arm. (LW) арш ‘booty’ || (+ *aua-) ? 
Orm. ur-uk ‘to hold, keep’ || (+ 4-) Par. ar-/awur ‘to bring’ || (+ *ni-) Orm. 
nawär-/nawulök ‘to take out, draw out’ = nawar-/nawólók || (+ *ham-) Arm. (LW) 
(h)ambar ‘store’, Arab. (LW) anbar ‘ricks, stacks; storehouse’ 


10 *barH 


*SANSKRIT: bhar ‘to carry, bear’ (RV) = EWAia П: 246 

© The Ir. root *bar has an impeccable IE etymology. 

«PIE *b'er- ‘to bring, bear, carry, sim.’ — LIV: 76 f. | Pok.: 128 

*IE COGNATES: Gr. фёро, Lat. fero, Olrish biru ‘I carry’, Welsh cymeraf ‘I take’, 
Goth. bairan, ON Бега, OHG beran, OE beran ‘to bring, carry, bear’, OCS bero, 
Russ. Беги, SCr. bérem ‘I gather, take’, Lith. beriu, Latv. beru ‘I scatter’, Toch. pär- 
‘to carry, bring’, Arm. berem ‘I carry, bring’, Alb. bie ‘I carry, bring, lead’ 
*REFERENCES: КРЕТ. 79a f., 133b, 134b, 205a, 243b; КРЕП: 183, 178 Ё; Ivanow 1926: 419, 427; HFL I: 
242a, 403a, 235a, 387b, 277a; EVP: 92; Christensen, Contributions I: 58, 151, 153, 255 f.; Christensen, 
Contributions П: 49 ff., 111, 155; HFL II: 259, 234a, 547, 194a; Abrahamian 1936: 110, 107, 126 #; 
Lambton 1938: 41a, 77a; Andreev — Pe&cereva: 343b f., 247b, 334a f., 370a Ё; Abaev, Slovar’ I: 238, 135 
f., 141 £, 553; MacKenzie 1966: 90, 89; Abaev, Slovar' II: 35 £.; EVS: 84b, 59b f., 70a; Lecoq 1974: 62; 
WIM I: 65 f.; Back 1978: 176 f., 246; DKS: 271, 278; Sims-Williams 1989: 260; Vahman — Asatrian 
1991: 78; Werba 1997: 212 f.; Paul 1998: 292; Steblin-Kamenskij 1999: 385, 250; Cabolov 2001: 184, 
349; Cheung 2002: 160, 194; Lecoq 2002: 120, 122, 125 (passim); ESIJa II: 84 ff.; Kiefer 2003: 202; 
Korn 2005: 269 f., 354 (passim) 


*barH ‘to move rapidly ? 

*AVESTAN: YAv. baranti (Lsg.) ‘when it storms’ (V 8.4) 

*SOGDIAN: (+ *pari-) BSogd. prByr- ‘to cross (arms, legs)’ 

Impf.: IND. 3sg. BSogd. pryByr ‘he crossed (arms, legs)’; Partic.: perf. pass. BSogd. prBrt- (in -p’ö
```


## [2026-09-05T05:26:08.347Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"‘to fill\" CHEUNG.txt | head -20; echo ===; grep -n \"ubārdan\\|ōbārdan\\|obardan\\|wbʾrdn\\|awbārdan\" CHEUNG.txt | head"
}
```


### [2026-09-05T05:26:08.424Z] TOOL RESULT

```
Exit code 1
1766:MMP hmb’r-, BMP hnb’I- /hambar-/ ‘to fill, collect’. Ф The etymology of Nyberg II: 
6605:«PIE pres. stem *pleH,-d'e/o- ‘to fill’ > LIV: 482 f. | Pok.: 798 ff. 
15458:reconciled with derivation *pari-kan’- ‘to fill’. A different meaning and, 
15480:different root, *Кат- ‘to fill’ ? > Samadi: 51, 181, 140, 149, 129, 215 
15507:‘to fill’ forms are homonymous and therefore often show mutual interference. For 
15521:*kan? ‘to fill’ 
15522:*MIDDLE PERSIAN: (+ *pati-) MMP phykn- ‘to fill, enter, penetrate’ || (+ *ham-) 
15525:MMP hnen- ‘to fill in^ = DMMPP: 275a, 181a 
15530:*PARTHIAN: (+ *ä-) ’gn-, "gn- ‘to fill’ = Ghilain: 55 | DMMPP: 29b f. 
15534:*SOGDIAN: (+ *4-) MSogd. "kn ‘to fill’ 
15538:*CHORESMIAN: (+ *upa-) bkn- ‘to fill, load’, bkny- (intr./pass.) ‘to become full’ 
15541:*NWIR: (+ *4-) NP agandan/agin- ‘to fill, stuff’, (caus.) NP aganidan/agan- ‘to stuff, 
15548:9 Several Iranian languages point to the existence of a separate root *kan- ‘to fill’. 
15554:*AVESTAN: YAv. °kan- ‘to dig’ || (+ *api-) ‘to fill out by digging, fill (a pit)’ || + 
19423:*parë ? ‘to fill’ 
19426:derives the Chor. form "nbrs-/m[nbrs- from the (new) inch. of *ham-par- ‘to fill’ 
19448:PIE 1. *perk- ‘to fill up’ || 2. with increment *-k-, *pel-k- ‘to fill’ => LIV: 476 | 
19480:*parH! ‘to fill; to nourish’ 
19482:*AVESTAN: pər- (fr-) ‘to fill’ || (+ *ham-) ‘to fill, stuff with’ = Liste: 33 
19488:entire, perfect’ || (+ *ham-) MMP hmb’r-, BMP hnb'l- /hambar-/ ‘to fill’ 
(eval):1: == not found
```


## [2026-09-05T05:26:10.698Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19480,19540p' CHEUNG.txt"
}
```


### [2026-09-05T05:26:10.791Z] TOOL RESULT

```
*parH! ‘to fill; to nourish’ 

*AVESTAN: pər- (fr-) ‘to fill’ || (+ *ham-) ‘to fill, stuff with’ = Liste: 33 

Pres. nà-: IMPV. 2sg. OAv. porona (Y 28.10); Perf.: IND. med. 3sg. pafré (Y 49.1, V 11.4), SUBJ. med. 
3sg. Y Av. ham.pafraite (V 4.48) 

*MIDDLE PERSIAN: (+ *us-) MMP ‘spwr, BMP spwlyk, BMP ’wspwlyk ‘complete, 
entire, perfect’ || (+ *ham-) MMP hmb’r-, BMP hnb'l- /hambar-/ ‘to fill’ 
c DMMPP: 65a f., 87a 

(+ *ham-) Pres.: IND. 1р1. MMP "hmb'rym, 3р1. MMP "hmb’rynd, BMP hnb’lynd /hambarend/, SUBJ. 
1р1. MMP hmb'rwm; Partic.: pres. MMP hmb’r’g’n 

*PARTHIAN: (+ *ham-) ? ’mb’r- ‘to fill’ = Ghilain: 75 | DMMPP: 39a 


296 *parHl 


Pres.: IND. 15р. ’mb’r’m 

*KHOTANESE: pār- (orig. caus.) ‘to nourish’, OKh. pir- (intr./pass.) ‘to be filled’ || (+ 
*us-) LKh. uspurra- ‘full, completed’ || (+ *ham-) OKh. hambir- (etc.) ‘to be filled 
[intr./pass.]’, OKh. hamber- (caus.) ‘to fill = SGS: 81, 84, 143 

*SOGDIAN: BSogd. p’r, CSogd. p’r ‘to fill, nourish’ || (+ *us-) BSogd. ’spwrn, 
MSogd. ‘spwrn ‘perfect, compete’, BSogd. ’spt’k, ’sptk, 'spty, CSogd. spt- 
‘complete, perfect’ || (+ *ham-) ’mbyr- ‘to fill’ 

Pres.: IND. 3sg. BSogd. p’rt; Impf.: IND. 1sg. BSogd. p’r’w; Partic.: pres. CSogd. p’my ‘nurturing’, 
MSogd. "p'rynyy 

*CHORESMIAN: (+ *ham-) ’nbf- ‘to become saturated’, ’nb’fy- (caus.) ‘to saturate’. © 
For Chor. "nbrs-/mjbrs- ‘to be satisfied’ see s.v. *paré. => Samadi: 116 

*NWIR: (+ *us-) NP sipari ‘complete’ (+ Sudan: ‘to end, pass, be finished’) || (+ 
*ham-) NP anbästan/anbär- ‘to fill’, NP anbar ‘full to the brim, replete; filth, 
manure, dung’. Ò Differently NP anbar ‘ricks, stacks of corn’, Arm. (LW) (h)ambar 
‘store’, Arab. (LW) anbar ‘ricks, stacks; storehouse’, on which see *bar!. 

*NEIR: (+ *api-us- ?) Pash. ЬӘ$рәг ‘complete, full, perfect’ || (+ *us-) Sh. (Baj.) 
sipen-, Rosh. sipön- ‘to strew, scatter, pour into, fill into (excess), place, Sariq. 
spon-, Yzgh. s(o)pan- ‘to fill, replenish’, Wa. sppm-/spat- (spat-) ‘to fill (up); swell’ 
|| (+ *ham-) Yi. bär-/bary, bär-/bary ‘to be satisfied’ 

*MISC: (+ *us-) Arm. (LW) aspar ‘entirely’ 

*SANSKRIT: раг ‘to fill’ (RV+) > EWAia II: 89 

9 The meaning ‘to nourish, feed’ attested in Sogd. and, notably, Khot. can easily 
derive from ‘to fill’ and does not necessarily point to a different origin, as hinted by 
Bailey, DKS: 230. Almost all of the IIr. / IE forms cited by Bailey, 1.с. in support of 
a root *par- / IE *per ‘to rear’ prove to be wrong or irrelevant: Skt. palayati does not 
mean ‘nourishes’, but rather ‘protects, guards’ (EWAia II: 124), whereas päranä- 
“breaking fast’ is a quite obscure form; although the origin of Khot. para- ‘cake’, MP 
/pésparag/ ‘an appetizer’ (pés- ‘before’, parah 1. ‘portion, piece’, 2. ‘gift, offering’), 
is not wholly clear (Khot. pāra- ‘cake’ < *‘sacrificial offering’, *parH? ‘to give, 
present’ ?), these forms do not unequivocally point to a (separate) root *par- ‘to 
feed’ though. Also, the IE forms quoted by Bailey, l.c. from Pokorny: 818, are 
unconnected: the meaning of Lat. pario (peperi, partus) ‘I give birth’, parens ‘parent’
```


## [2026-09-05T05:26:28.025Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اوباشتن\\|اوباردن\\|اوباش\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T05:26:28.106Z] TOOL RESULT

```
3119:بریشت خوددازد وبجهث بچه‌های خودآورد. گوبند چون فوت اونزديك شود فیلی دریشت اوباشد
4020:6 نظامالدین حیدر متخلص باوباش « که بحليه علم ودانش آراسته
13525:ات یم اول ؛ بمعتی اوباش د که ضصر الاحی . باجیم فارسی مَحتانی زسیلدهه»
14799:۵ او بار دی رك : اوباردن اوجاق _ اجاق . زک مطخ ء کانون - خانواده‌قبلة
17821:را ثبت ا گرچند باوباش‌دهند
29413:وئولی و بیباك ودزد واوباش را کوبند - و چوب
29967:ثر یه » بفتح اول و رابم که واوباشد
```


## [2026-09-05T05:26:28.113Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خرسند\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-05T05:26:28.211Z] TOOL RESULT

```
4830:   ‫اصاف ومکان)‪ ,‬رك‪:‬چراغ بره » چراغ واره‪ - ۸ .‬رك‪ :‬چراخوار ‪ :‬خرسند شدی بخوردکیتی‪-‬‬
```


## [2026-09-05T05:26:32.477Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'اوباردن' in l or 'اوباش' in l and i>380:\n        head=l.strip().split('\\n')[0][:80]\n        print('leaf',i, '| first:',head)\nEOF"
}
```


### [2026-09-05T05:26:34.259Z] TOOL RESULT

```
leaf 399 | first: رل اس
leaf 460 | first: باشد .
leaf 709 | first: - ۳و -
leaf 722 | first: 3
```


## [2026-09-05T05:26:36.499Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==399' BQT_v1_pages.txt"
}
```


### [2026-09-05T05:26:38.859Z] TOOL RESULT

```
کوبند که بدشواری از انا شود و حل
9
| ثیشه - بر‌رزن‌همینه .جاسوی‌وچاپلوی
هر چیز بسته و منجمد بأشدچه درفارسی‌سینوشن
تب ۱۵۰ ,
0 زمین ۰ ء ظرفی باشد ازسنال
مانند مو وخمچأیزگی که دوغ وا جر آ ‌کنند
او * نم اول : و سکونِ نافی » ۳
۳ 0 ه‌ ۰
او اه بروزن هوا » بمعنی آوازباشد ٩‏
-وبمعنی ابا هم هت که شوربا و آش باشد .
دفتر و حساب دبوائی باشد ۷ - و بضم‌اول کرما
و هوای کرم را یز گویشد .
آواده - بفتح اول بروزن شرآره. دفش
حمایی باشدکه حسابهای پراگندث دیوانی را در
آن نوبند و در این زمان آن دفتر را اوارجه
کویند ۸ - و بمعتی دبوان خانه بمنی‌دارالاماره
هم آهده اس تکه بار کاء ملوك وسلاطین بلشد -
و ریز آحنی را نیز گوبندکه در وفت سوراخ
کردن تعل اسب برآید - وبنم او لگرماوهوای
۱ - رگ : اشسثه .
گرم را کوبند ٩‏ ۰
" آوادلن » بروزن شیاطین, زشتوبدرا
کوبند چنانکه پرآرین خوب و بنکورا . .
اوا۵ » بر وزن عوام 4 قرض و وام را
کویند»۱- وبنعنی رنگه ولون‌هم آمدماست٩٩.‏
او پا - با بای ابجد بروزن سودا ؛ دم
پسرزادء سلیمان‌علهاللام اس که‌پسررجوعام ۱۴
او پار ۲۴ بفتح اول‌بروزن افار ,چیزی
بگلو فروبرنده و 0 را کوبند سوهرچیز
که فرو رود بعنی کد بلم‌شود - و هرجانوری که
جانور زندمرا قرو برد گویند «اوبارید» سوبمعنی
آتش غالب و زهر مهلك ی زکفثه‌اند - و بمعنی
خاله و سرا هم آهده است - و امر بفروبردن
و یرون افکندن هم‌هست بعنی فرو ببروییرون
۴ رك : انسه واتسته.
+ اوتوالا ۵٩‏ > استی
است ۷ , فارسی نیز آوی ۰ وف .
۵ رك , ص: به . ۱ ول : آوا . ۷ - رک : آواره وآهار .
۸ رد۵ : آواره و آمار . ۸ رك : اوار  .‏ *9 رك : وام . ٩‏ رگ : فلم.
۴- *رحبعام» پسر و جانشین سلیمان است. «قاموی‌مقدس 4۱۱*. ۴ پهلوی
۲7 آزایرانی باستان۳26221- 2۷2 مر کب از:2۷3 پیشوند وجزو دوم مشتق از021 (پر
```


## [2026-09-05T05:26:49.044Z] TOOL CALL #36: Bash

```json
{
 "command": "awk 'BEGIN{RS=\"\\f\"} NR==400' data/verification/sources/refs/BQT_v1_pages.txt | head -40"
}
```


## [2026-09-05T05:26:49.554Z] TOOL CALL #37: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-05T05:26:50.682Z] TOOL RESULT

```
رل اس
یفکن - و بشم اول ناله و زاربراگویند . *
او باریدن ۱ - بنتح اول بروزن سر
خاریدن ؛ ناجاویده فرو بردن را گویشد و بعری
پلع خوانند ‏ و بمعنی افگندن هم هست-ویضم
اول بممتی ناله و زاری کردن باشد .
5 ۱ ۳۹
او باش ‏ بر وزن افراش » مردم عامی
هیچ نافهمید: )۱( بی‌سرویا و جلف و بر خود
و هتعصصت را گوند ۴ ۰
شش رهپس
پر کردن و افگندن باشد .
او برث ۱ - ینم ناك بر وزن افترد .
بحئی ناجاویده فروبرد و پلع کرد .
او ببس - نم اول وکر الك بر وزن
مونن ؛ خوش و پیوند و قرابت را گونند .
او به شم اول و سکرن انی مجپول
کر ثالث و ظهورها » دام قربه است از فرای
هرات ,
اوج - بفتح اول بر وزن موج » معرب
او گه است که مقابل حضیض باشد ؛ و بلندترین
درجهٌ کوا کب بود و آن نقطهٌملافات سطح‌محدب
فلك باشد از افلاك جزئیةٌسبعة سیاره با حوامل
ایشان - و نام نفمه ایست از عوسیقی؛ و سنی
)۱( چش, چب ۱: نفهملده.
(۳) چك : ژند و یاژند .
آو چت هی - با جیم فارسی و فوفانی
و بای فار سی و میم بروزن تعزل نکن (۲) بلفت
زند و پازد (۳) بمعنی انگشت باشد مطلفًخواء
انگشت پا و خواء انگت دست ۳ .
نام شهر و مدننه‌است :
او چیز ی « بازای هوز بروزن+وسیفی»
بمعنی ماهت و چگونگی چیزی باشد ۴ ۰
او چیز بان- بضم‌اول بروزن‌نوشیروان»
کوه را کو,ند و بعربی جبل خوانند ۷ .
می‌نقطهُ بالف کشیده و کسرلام وتستانی بواورسیده
و بنون زده ۰ بیونانی کرفس کوهی باشد. چهاودا
بمعنی کوه ٩‏ وسالیونکرفس را کویند وتخمآترا
فطرا سالیون خوانند چه فطرا بیو:انی مطلق‌تخم
راگوتد ۸ . ِ"
```


### [2026-09-05T05:26:50.721Z] TOOL RESULT

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
```


## [2026-09-05T05:27:05.011Z] TOOL CALL #38: Bash

```json
{
 "command": "awk 'BEGIN{RS=\"\\f\"} NR==400' data/verification/sources/refs/BQT_v1_pages.txt | tail -25"
}
```


## [2026-09-05T05:27:05.425Z] TOOL CALL #39: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:180 --image 2>&1 | tail -30"
}
```


### [2026-09-05T05:27:06.942Z] TOOL RESULT

```
او چیز ی « بازای هوز بروزن+وسیفی»
بمعنی ماهت و چگونگی چیزی باشد ۴ ۰
او چیز بان- بضم‌اول بروزن‌نوشیروان»
کوه را کو,ند و بعربی جبل خوانند ۷ .
می‌نقطهُ بالف کشیده و کسرلام وتستانی بواورسیده
و بنون زده ۰ بیونانی کرفس کوهی باشد. چهاودا
بمعنی کوه ٩‏ وسالیونکرفس را کویند وتخمآترا
فطرا سالیون خوانند چه فطرا بیو:انی مطلق‌تخم
راگوتد ۸ . ِ"
اودد بقئح اول و سکون انی و کس
تال و دای بی نقطهٌ ساکن » برآدد مدر باشد که
محر نی م گوبند ۰
او دددن * - نم اول و ثاك بروزن
بوبردن » بلفت زند و بازند (۳) سه‌نی‌مردن واز
عالم رفتن باشد ,
: رك : اویر . ۴ عریی » جمع وبش » مقلوب بوش . « محیطالمحیط‎ - ٩
. ۰*۱ ان ۴ - حز ۵620۳۵0 , پپلوی ؛أ5لا208 , انگشت «بونکر‎
۴ - در دسانیر * اوجیژ» و * ارچیز » بمعنی حقیقت د ماهیت چیزی آعده « فرهنگه
۵ رك : او چزی.
۲ - صحیف بونانی
دسائیر ۷۲۳۳ » وآن مجمول «فاب4۷:۱» وترجمةٌ «ماهو» عربی‌است.
۹ ت_ مصحف 6۳۲۵ بونانی بسعنی کوه رك اوداسالبون
0 ه«اشتنکس» . ۸ رد : فطرامالون . ٩‏ - بهلوی۷2۸2۲120
۵ او بار دی رك : اوباردن اوجاق _ اجاق . زک مطخ ء کانون - خانواده‌قبلة
بز رگ «حفتابی ٩۶۷‏ .
```


### [2026-09-05T05:27:08.819Z] TOOL RESULT

```
no scan of BQT covers printed page 180 (see 'scans' in refs_online.json)
```


## [2026-09-05T05:27:20.809Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef conv(s): return ''.join(str(fa.index(c)) if c in fa else c for c in s)\nfor i in range(392,406):\n    l=leaves[i]\n    nums=set()\n    for m in re.finditer(r'[۰-۹]{3}', l):\n        nums.add(conv(m.group()))\n    for m in re.finditer(r'\\b\\d{3}\\b', l):\n        nums.add(m.group())\n    print(i, sorted(nums)[:12])\nEOF"
}
```


### [2026-09-05T05:27:23.537Z] TOOL RESULT

```
392 ['173', '235', '۱۷۳', '۲۳۵']
393 []
394 ['175', '٩٩۵', '۱۷۵']
395 ['210', '231', '۲۳۱']
396 ['6۷۹']
397 ['090', '333', '918', '۰۹۰']
398 ['150', '2۷2', '2۷3', '4۱۱', '۱۵۰']
399 ['325', '723', '٩۶۷']
400 []
401 ['۳44']
402 ['309', '۳۰۹']
403 ['302', '۳۰۲']
404 ['175', '22۰', '252', '257', '3۶2', '460', '٩۶2']
405 ['015', '180', '۰۱۵', '۱۸۰', '۳6۲', '۷20']
```


## [2026-09-05T05:27:50.820Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(360,370):\n    if 'افتادن' in leaves[i] or 'افتاد' in leaves[i]:\n        print('=== leaf',i)\n        print(leaves[i][:1500])\nEOF"
}
```


### [2026-09-05T05:27:52.389Z] TOOL RESULT

```
=== leaf 361
فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند
و او را برآوردند و پزبان رومی اینچنین شخصی
را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در
زمان او بوجود آمد . وبقوط سین اول بروزن
فربوی هم بنظر امده است -
اغشته با اول وئانی مفتوح و سکون
شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده
وتر کرده باشد؟ .
لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن
کومفندان ساژند؟ .
اغلیسون » با سن بی قطه بر وزن
افربدون ۰ قوس قرح را خوانند .
افتدستا
اغلیقی ‌ َنح اول,قلف سحتا سدكهه
بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته
جوشانیده‌اند ومیفختج همان است » وبکسر اول
نیز آعده شتگن «
اغول ه بر وزن ملول » از روی خشم
وفهر بگوث؛ چشم نگریستن باشد .
اغیرس < بنتح اولوثانی‌بتحتانی رسیده
و کسر رای قرشت و سکون سین سعفص ؛ جوز
رومی است و آن بار درختی باشد که صمغ آن
کهرباست ؛ و بعضی گویند چوب آن درخت
کهرباست .
اغیسی ‏ بروزن نفیس , نخمی اس ت که
آنرا بشیرازی تخم دلاشوب کونند » و ری
افتاد جنم اول بروزن استاد ۰ بعنی از
بای درآمد - و کنابه از دور شد هم هست که
ماضی دورشدن است .
افتاث گان » کاب از مظلومان
ویر بشان شدکان‌باشد .3۶
افتاده ممعثی عاجز و سقط وخراب
که و ژبرن گردننه باخد..
اقتال ‏ یک راون بروزن اقبال . به‌عنی
برا گنده وباشیده - وشکاقه ودریده باشد .
افتا ليفن « بکراول مصدر افتالاست
که بمعنی پراکندن و یائیدن و افشاندن -
وشکافتن ودربدن باشد .
افتان و خیز ان - کنابه از آحته
ودیر براه رفن باشد .
افقد - بنتم اود و کسر الث مر وژن
محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت
وبععنی شگفت وعجب ونعجب هم‌هسته .
افتدستا - کلمه ابیت مرکب از افتد
ستایش‌عجب وئیکوترین ستاش‌وبند گی- ویمعنی
2 ۱ متفه
۴ - ب
```


## [2026-09-05T05:28:00.075Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (362,363,364,365):\n    print('=== leaf',i,'===')\n    print(leaves[i][:900])\nEOF"
}
```


### [2026-09-05T05:28:01.739Z] TOOL RESULT

```
=== leaf 362 ===
اتمون
حمف خدایتمالی هم هست! -
/ لتیهاون » بعتح‌اول. دوابی‌است‌ممروف
وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر
شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه
کوفت صرع را نافع است ۰ و آنرا بعربی سبع
الثمرا خوانئد , وی کوبند زیر رومی است
وتیزطعم میباشد .
اقچ4 - بن اول بروزن بقچه , علامتی
است که در غله زار ها و کشت و زراعت بجهت
رمیدن مرغان ساژند . وبفتح اولعم گفته‌اند .
اقد فتح ارل و رای وسکون دال
ابچد » بممنی افتد است که شگفت
روا ماه تور گر ۳
وآن سورخ و:
و عجب
افدد » بر وزن صقذر ؛ برادر در را
وخواهرزاده تبزامده ات ۰
اقدستا » با تای قرخت بروزن‌مجلهاء
جمعتی افتدستاست که ستایش عجب و نبکو نرین
متایش - و حمد خدای عز وجل باشد بزبابن
پهلوی ۴‏
اقد‌یدن » بروزن فهمیدن . شگفتی
کردن وتعجب نمودن باشد ۴ .
اقر) - بر وزن صفرا ۰ بمعنی آفرین
ونحسین پاشه .
ار احت ‏ بر وزن پرداخت » یعنی
برداشت وبلند ساخت .
. رک : اد وافدستا‎ ٩
ب 30۸
اقفر اختن - بر وزن برداختن 4 بمعنی
برداشتن وبلشد ساختن باشد .
افر احته بر وزن بردا
=== leaf 363 ===
افر اشتن بروزن ومعنی‌برداشتن: بلند
ساختن باشد .
افر اشته بروزث ومعنی برداشته‌و بطند
ماخته و بالارده )۱( باشد ۰
۱ فر دون - بفتح اول رانی‌وسکون‌نالث
و کربای ابجد وبای حطی بواو رسیده و بنون
زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر
کزند کی جانوران را نانع است .
که آنرا بشیرازی بالنگوی خوورو (۲گوبند .
ء اس را نافع است ۳
نام شهرست که نوشیروان آ ادکرده بود در کتار
دربای مصی » و مادر عثرا از آن شهر است ۱ -
وم ولایتی‌است از زنگبا - وم زمینی ه‌هست
در بلاد غرب ۰
ارف » بروزن فرزند ۰ فر و نیکوبی
وزیبایی وحشمت باشد؟ .
افر ندیدن مصدر افرید است بعنی
زب دادن وزشت کردن وآراستن .
افر نگ . بروژن و معنی اورنگت لست
تخت پادشاهان باشد - وبمعثی فر وفکوبی
کون که بمربی صاری‌خوانند؟ .
49 چث : (- شده .
۱ -ظ , معرب افرنگه.
۲ ۱۳
افر و خشن؟ « بروزن اندوختن بسعنی
روئن کردن آتش رچراغ باشد .
افر ود بر وزن سردوز . بممنی
روشن و روشن کردن باشد - و روشن کننده را
نز گویند - وامر بدین‌معنی م‌عست بمنی‌روشن
کن ویفروز . *
افر و
=== leaf 364 ===
آفری
کشوث و نخم آنرا بذرالکشوث خوانند . فواق
را تافع است .
افری فتح اول وثانی بروزن سفری »
مخفف آفرین است که دد مقام تصی نگوند .
و بسکون انی هم درست است .
افر یدون ‏ - فربدونباشد. واویادشاهی
بوده. ءشهوره ویستی گویند افربدون نوح علیه ب
اللام است ۰ و بعضی ذوالقرنین اعظم او را
صسدانند ۰
اقفر پسموسش_ » بسکون سی‌بی نفطه
وم حیموواو وسین دیکرساکن, پیونانی؟ مرضی
است که مردانرا بهم میرسد و آن شدت تعوظ
است بعنی بوسته لت مردی ایستاده هیباشد ۰
وباسقاط همرز ه ی شت. -
گویندمقراض کرده وسوخته| تر | درمعاأجین‌خوردن
عفن را فربه سازد .
افز | ح بفتح اول‌بازای هوز بروزن‌اجزا»
1 ۱۳ اسج ۰
افز اد ه بر وزن رفتار , بمعنی کفش
ویای افزار باشد - وبادبانکشتی را نیز گویند -
والات مشهوران باشد عموماودفتن جولاگانرا
را کربند خصوصا ‏ وادوبة کرمی که در طعام
کنند همجو فلفل و دارچنی و ژبره و مانند
آن۴ .
۹ م2 : فربدون و آفربدون.
۳ ‌- ره 4 ابریشم.
4
افژ ول با زای قلرسی بروزن مقبول.
بمعنی تقاضا وانگیز باشد - و بمعتی پریشان هم
۳
=== leaf 365 ===
ات
وافرا یمرن الیل خوالند .
اسر ۵لن؟ « بر وزن افشردن » بمعنی
سردشدن ویخ بستن ومنجمد کردیدن باشد - واز
چیزی ‏ وکسی‌دل سرد شدن هم هست -
آقتاب عالمتاب است .
افسرسگزی « بکس مین بی شله
و سکون کاف فارسی و زای نقطه دار بتحتانی
رسیده ۰ نام سازی باشد که نوازند - ونام تصنیفی
وقولی است ازصنیفات بارید .
افسر شدن » کنابه از پادشاء خدن
باشك .
افستتین ۴ -
بکسر الث و سکون
نون و فوقانی بتحتانی
رسیده و بنون‌زده» نوعی
از بوی مادران کوهی
است .کلآن بافحوان
وتلخی آن صبر تزديك
است . دردچشم‌را سود
دارد . افنئی
افوس؟ با واو مجپول بر وزن
محبوی » بمعتی ظلم و ستم - ویراهی باشد -
ودریغ و حسرت را نیز گویند - و بمعنی بازی
وظرات - وسخر ولاغ هم‌هست - وبا واو معروف
تام‌شهر دقیاتوی بوده ۴» وبسنی گویند باین‌معنی
افتون
عربی‌است .
افسون؟ » بر وزن افیون ۰ خوادن
حصول مقاصد خود - و بمعنی حیله و تروبر هم
عست ۰ 3
اقشاد - با شین شلهدار بی‌وزن‌دستار ,
بمعنی افتردن باشد یمثیاب ازچیزی‌بزور دست
گرفتن - و ریزنده - و رشن یی دری را یز
گو
```


## [2026-09-05T05:28:14.989Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[361][-700:])\nEOF"
}
```


## [2026-09-05T05:28:16.074Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in range(180,200):\n    l=leaves[i]\n    if 'خرس' in l or 'خرم' in l:\n        print('=== leaf',i, l[:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T05:28:16.527Z] TOOL RESULT

```
ن نفیس , نخمی اس ت که
آنرا بشیرازی تخم دلاشوب کونند » و ری
افتاد جنم اول بروزن استاد ۰ بعنی از
بای درآمد - و کنابه از دور شد هم هست که
ماضی دورشدن است .
افتاث گان » کاب از مظلومان
ویر بشان شدکان‌باشد .3۶
افتاده ممعثی عاجز و سقط وخراب
که و ژبرن گردننه باخد..
اقتال ‏ یک راون بروزن اقبال . به‌عنی
برا گنده وباشیده - وشکاقه ودریده باشد .
افتا ليفن « بکراول مصدر افتالاست
که بمعنی پراکندن و یائیدن و افشاندن -
وشکافتن ودربدن باشد .
افتان و خیز ان - کنابه از آحته
ودیر براه رفن باشد .
افقد - بنتم اود و کسر الث مر وژن
محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت
وبععنی شگفت وعجب ونعجب هم‌هسته .
افتدستا - کلمه ابیت مرکب از افتد
ستایش‌عجب وئیکوترین ستاش‌وبند گی- ویمعنی
2 ۱ متفه
۴ - بوتانیلا ان «اشتینگای».
```


### [2026-09-05T05:28:18.143Z] TOOL RESULT

```
684
=== leaf 183   ‫خریزء هددی‬                                                                                    ‫ا‬ |                                                                                                 ‫پ‪۷‬‬ |  | ‫‪ ۱‬زانوها (‪ )4‬گذارند وسرربسمالی رابردست کیرند‬       ‫خرامیی » بکر اول بروزن ریاحین ‪۰‬‬ | ‫
=== leaf 185   ‫خر حه‬                                                                                              ‫‪۳-۷ ۲۷‬‬ |  |  |  |   ‫باعد و آرن بکیزی‬        ‫ان‬ |                            ‫لشیر‬ |                               ‫کز»‬ |                                 ‫معنی سا‬               ‫باشد وانکررایکوبند وبر 
=== leaf 188  ‫یر ار —‬                                                                                                     ‫خردر‬ |  | ‫وفارسی ‪ ۵‬میباشد ‪ -‬بوستانی سرخ رنگه و فربه‬                        ‫آقتاب است دربرج جوزا ‪ -‬ونام روز شم باشد‬ | ‫بود وچون بکوبند زرد شود ‪.‬گرم وخشك است‬                         
=== leaf 190  ‫‪A‬‬                                                                                  ‫خرد* مینا‬ | ‫خر د هره ع بفتح‌اول وئالث ؛ معروف‬                ‫خر دة همینا = ممروف است کهمینای‬ |  | ‫است کهزهرءٌخر‪-‬وزهرة بزر که‌باشد ‪۴‬سودرختی‬          ‫شکته وریزه رزه شده ‪ - ۱‬کونابه از شراب‬ | ‫امت که برک آن ب
=== leaf 191                                                                                                ‫‪— ۳۳‬‬ |  | ‫افشاند بکهدرام که پای او بخورد او را بدرون‬                ‫اسبهارا‬   ‫دراز که درطو لپا نصب کنندوزمنهاوبراق‬ |  |  | ‫خط بجای خود آورد واین بازیرا عربان حجوره‬                  ‫بر بالای آن نهند ‪ -‬
=== leaf 192    ‫پات‬ | ‫ثالك وفتح فوقالی» بمعنی خرام وخرامیدن باشد‬        ‫ی‬               ‫رن رک‬                ‫کی‬ |          ‫یعنی براه رفن از روی از وسر کشی ‪.‬‬        ‫بزرکه ناهموار ناراشده را گوند که در مدان‬ |  |  ‫حشره‪ -‬بفتح اول وثالی وثالك » مخفف‬                ‫شد (‪ )۱‬مردم‬           ‫و مالع عمور و 
=== leaf 194     ‫‪۷۳۹‬‬ | ‫را‬    ‫مدور‬    ‫بز رگ‬    ‫زا کوب شوم ارا‬                   ‫ومع‬    ‫کرمان بیز ند وبخورند وارد نیزسازند ونان هم‬ |                                                ‫خت ‪۲‬‬                                                 ‫يزنك ‪.‬‬ | ‫‪۰‬‬     ‫دوم‬     ‫بم خای‬     ‫=‬   ‫خر گاه خصر‬ |    
=== leaf 195     ‫خرم‬                                                                                             ‫‪ ۳‬اس‬ |                                                ‫آمده ات ‪.‬‬         ‫کمان حلقه را بدان چکلنهند » وآن دوپارچه‬ |                                                                  ‫چوب است که ا
=== leaf 196    ‫و‪۳۷‬‬                                                                                            ‫خرمای ابوجهل‬ |  |  ‫خرم روز ‪ - ۴‬نام روزهشتم است‌از‬                        ‫است که ماه دهم‌باشد ازسال شمی وبودن فت|اب‬ |  ‫هرماه شمسی‪ .‬کوبند ملوك عجم درین روزلیکن‬              ‫در برح جدی ‪ - ۱‬ونا
=== leaf 197  ‫خر اد‬                                                                                                  ‫‪۷ ۳۹۰-‬‬ | ‫و آ براحر هیمه نز‬        ‫پهم هیرسد‬   ‫که بردورماه‬       ‫نمعتی‬   ‫خر مگاه ‪ - ۱‬با تشدید انی ‪.‬‬ |  | ‫گویند محذف الف ‪ - ۵‬وخط عذار خوبالرا هم‬                 ‫و مدور باشد ؛‬
```


## [2026-09-05T05:28:26.801Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(186,196):\n    l=leaves[i]\n    hits=[m.start() for m in re.finditer('سند',l)]\n    nums=re.findall(r'[۰-۹]{3}', l)\n    print(i, nums[:6], len(hits))\n    for h in hits[:4]:\n        print('   ...',l[max(0,h-120):h+120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T05:28:28.714Z] TOOL RESULT

```
186 ['۰۷۲', '۰۰۸', '۹۲۷'] 0
187 ['۲۸۲', '۵۳۱', '۲۵۷', '۷۹۱', '۷۲۱', '۷۷۱'] 0
188 ['۷۲۲', '۹۲۷', '۰۳۷', '۵۸۲', '۸۸۳', '۲۹۲'] 1
   ... ن ‪.‬‬                     ‫(‪ )۱‬چك ‪ .‬چش ‪ :‬ازماه‪.‬‬ |  ‫ره ‪ :‬خر جسته‪.‬‬     ‫ظ ‪:‬م تسیده؛ و با‪:‬جماعتی باشند‌متسند‪.‬‬          ‫(‪)۵‬چنین است درخ‬         ‫(‪ )4‬چك‪ .‬چس ‪ - :‬نام‬ |                                   ‫مزدسنا ‪. )۰۳
189 ['۷۳۱', '۷۳۳'] 0
190 ['۱۹۳', '۲۱۱', '۲۷۲', '۹۷۱', '۱۳۷', '۵۳۸'] 0
191 ['۹۹۱', '۵۲۵', '۹۷۱', '۵۵۱', '۰۲۱', '۷۱۰'] 1
   ... ‬ |      ‫( بسوی باین)«بارتولمه ‪ » ۳4۹‬سالسکریت ‪ ( 2123۷2 -‬پاین « (‪ıı‬‏ ؛ ‪adnaS‬‏ ‪ .#‬از ‪dnas‬‏‬ |                 ‫(سندیده بافتن) « بارتولمه ‪ 4۵۵۱‬رلك ‪ :‬نىمرك ‪ ۳-1‬و اسشق وهوشمان ‪. ۸۷1‬‬ |      ‫‪ #‬خر س۔ بکسراول‪ .‬پهلوی ‪ « 572[ 5۳
192 ['۸۱۱', '۰۲۷', '۳۹۳'] 0
193 ['۵۹۳', '۱۵۷'] 0
194 ['۷۳۹'] 0
195 ['۵۸۲', '۱۱۹', '۷۰۳'] 0
```


## [2026-09-05T05:28:40.734Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[191]\ni=l.find('سند')\nprint(l[max(0,i-3000):i+1500])\nEOF"
}
```


### [2026-09-05T05:28:42.320Z] TOOL RESULT

```
 آورد واین بازیرا عربان حجوره‬                  ‫بر بالای آن نهند ‪ -‬وسه بایه را قیز گفته‌اند‬
                                       ‫گوند(‪. ۴ )۲‬‬        ‫که زین اسب رایربالای ان گذارند ونکیه گاهی‬

‫خر سگیاهم بعنی گیاه خری و بیخ‬                              ‫را نکیوزبند که بکروشهای صفهاسازند و‪-‬نوعی‬
                                                                                            ‫ازیالان هم هت‬
                                  ‫گن‬
              ‫یاء شقاقل است و خرس ن‬
 ‫آرا بسیار دوست‬                     ‫آ‬                                                 ‫‪۷.‬‬

                                           ‫داردو برغت‬
‫(‪)۳‬؛وبعضی گوبند زردك‬           ‫تمام خورد‬                   ‫حرست د بفتح اول ونانی وسکون‌سن‬
‫گوزر بری است و بعضی دیگر کونند کرفی‬                        ‫نبةیعله وفوقانی» بم‌منی‌سیاه هست‌است که بعربی‬
                                           ‫صحرای ات‬                                        ‫طافح گویند ‪. ۱‬‬
                      ‫‪2‬‬            ‫‪۶‬‬           ‫ی‬
          ‫‪۳‬‬
‫بقح ثالث ولام بالف کشیده‬        ‫خر سالاك =‬
                                                           ‫سرته = بکراول وانی‌وسکون ثالث‬
                                                                                       ‫خ‬
        ‫باشد » و أ‬
    ‫شنخصی‬                          ‫» بم‬
                                ‫نعنی‬
                               ‫ده‬     ‫ن‬ ‫رده‬  ‫بکا‬
                                          ‫خف ز‬
                                                            ‫وفتح فوقانی » بمعنی زلو باشد ‏ و آکنرمی‬
                  ‫ت که خرالاغ بکرابه میدهد‬
‫خرسطه = بروزن مرحله ‪ .‬نام داروبی‬                                    ‫بجبانند (‪ )۱‬خون ازآن عضو بمکد ‪.‬‬

                                                           ‫خرسك = بکراول وفتح‌ثالث » تصفیر‬
‫خسرنك ‪ = ۴‬بنم اول بروزن گل قند»‬                             ‫خرس است؛ آون‌جانوری‌باشد معروفسوفرشی‌است‬

                                                           ‫توص ویو ای راو‬
 ‫بمعنی شادمان وهمیشه خوش وخوشنود باشد ‪-‬‬                   ‫وآتجنان باشد که‬     ‫یشم‌دار‪ -‬ونوعی‌آز بازی‌هم هت‬

 ‫هضاقضاداده باشد وهرچه‬
                     ‫و کسیرالیز گوبندک ر‬
              ‫کر وراش بو ‪:‬‬             ‫ادا یش آنا‬          ‫آبند واورا زنند و او بای خود را بجانب اشان‬

‫‪.‬‬    ‫‪ :‬ورد‬    ‫‪٠‬‏ چش‬       ‫چك‬   ‫‪۳‬‬            ‫(‪)۲‬چك‪.‬چش‪ :‬خوانند‪.‬‬             ‫(‪.)۱‬چك ‪ :‬بجپانشد ‪.‬‬

         ‫بیم ندارم ابزلا تنللا تلا تلا‪.‬‬                  ‫‪ - ۱‬مت‌خرست میروم‌ازمیعشق بوالعلا‬
     ‫مولوی بلخی‌رومی‪.‬‬
              ‫خرسك باکزولددکان در بازار‪.‬‬
      ‫«گلتان ‪.۹۹۱‬‬
     ‫( کود)‬    ‫‪7‬‬
               ‫‪0‬ع‬‫‪1‬تی‬
                   ‫‪dnas‬‏ ‪ rûx +‬در ارم‬               ‫‪ - ۴‬پپلوی ‪( 0085۲0‬قالم‪ ,‬راضی)؛ ‪۲۵6‬‬
     ‫بمعنی کودی و ورطه‪ . # ۲۵ ۰ 2۳2۷2# ,‬از اوستا ‪( ۵۲۵3۷4‬بپاین) « بارتولمه‪2702 ۹۷۱۰‬‬
     ‫( بسوی باین)«بارتولمه ‪ » ۳4۹‬سالسکریت ‪ ( 2123۷2 -‬پاین « (‪ıı‬‏ ؛ ‪adnaS‬‏ ‪ .#‬از ‪dnas‬‏‬
                ‫(سندیده بافتن) « بارتولمه ‪ 4۵۵۱‬رلك ‪ :‬نىمرك ‪ ۳-1‬و اسشق وهوشمان ‪. ۸۷1‬‬
     ‫‪ #‬خر س۔ بکسراول‪ .‬پهلوی ‪ « 572[ 5۳11‬بونکر ‪ ۰۲۱>]۰‬اوستا ‪« 3159۲4‬اسفا ‪۱:۷‬‬
     ‫ص‪ ۷۱۰‬بارسی باستان‪( 20158‬در ‪ ) 2۳12015۳23‬اآ‪:‬رشام ]‪ ,‬اشکاشمی ‪ 5۳106‬دشغنی ‪۵5۲1۷۷۰‬‬
     ‫‪.‬یلکی ‪ ( 5721‬در ‪ ۱ .۵‬ص‬      ‫‪ : 5‬لك ‪ .‬ات ‪ ۷۰۱۲‬گ‬                   ‫یودغا ‪« 158‬کربرسن ‪ .»۵۸‬استی‬
                                               ‫‪ )KS‬فریزندی ‪ » 5۲685‬برنی ونطنزی ‪« 5۲66۱‬ك ‪.‬‬            ‫‪۷‬‏‬
                                           ‫و‬       ‫و ‪9‬‬    ‫و سرخهی‬         ‫‪ ۰‬ق‬     ‫سمنالی ‪5131‬‬    ‫ص ‪»* ۷۸۲‬‬

                                            ‫شهمیرزادی ‪ ۲ .#« 5۲6‬ص ‪ 4۸۱‬سفدی ‪۸5۸S‬‏ « بنولیست‬
                                            ‫نوعی از بت‌انداران کوشت خوار » شامل‌جانوران‌سنگن‬          ‫‪۰‬‬
                      ‫خری‬
```


## [2026-09-05T05:29:07.121Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt733.jpg \"https://archive.org/download/borhan-ghate-v2/page/n191.jpg\" -w \"%{http_code} %{size_download}\\n\" ; file bqt733.jpg"
}
```


### [2026-09-05T05:29:13.251Z] TOOL RESULT

```
200 669351
bqt733.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-09-05T05:29:17.846Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('bqt733.jpg')\nw,h=im.size\nprint(w,h)\nim.crop((0,int(h*0.62),w,int(h*0.88))).resize((int(w*0.75),int(h*0.26*0.75))).save('bqt733_foot.png')\nEOF\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T05:29:19.842Z] TOOL RESULT

```
2569 3970
total 1012
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 01:29 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  71145 Sep  5 01:29 pg71.png
```


## [2026-09-05T05:29:21.600Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt733_foot.png"
}
```


### [2026-09-05T05:29:21.643Z] TOOL RESULT

```

```


## [2026-09-05T05:29:56.521Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^au-\\|^au- \\|^awo-\\|Away, off\" AHD_watkins1985.txt | head; echo ===; grep -n \"ukraina\\|Ukraine\\|krai\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T05:29:56.575Z] TOOL RESULT

```
Exit code 1
302:au-', To stay the night, dwell. Suffixed form *au-/d- in Greek aulé, court, dwelling: autic. [Pok. 2. au- 72.]
303:au-?. Pronominal base appearing in particles and adverbs. Suffixed form *au-ge in Germanic ‘*auke in Old English éac, éc, also: EKE?. [Pok. 4. au- 73.]
304:au-3, Off, away. 1. Old Russian u-, away, in Russian ukazat’, to order: UKASE. 2. Sanskrit ava, off, down: AvaTAR. [Pok. 3. au- 72.]
305:au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.]
306:au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.]
(eval):1: == not found
```


## [2026-09-05T05:29:57.344Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*sand\\b\\|sand ‘to seem\\|‘to seem, appear\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T05:29:57.404Z] TOOL RESULT

```
21757:332 *sand 
21769:*sand ‘to appear, seem (good)’ 
21797:*SOGDIAN: SSogd. sy-, BSogd. sy-, CSogd. sy-, MSogd. syy- ‘to seem, appear, 
21801:pleased’. Ó It is difficult to separate BSogd. sy- from the root *sand- (zero grade: 
21815:*sand 333 
21856:1965: 165 ff. Note that the meaning ‘to shine’ is absent in Iranian *sand. The Khot. 
21884:sasanhan (V 2.16). 0 OAv. sazdiiai may have a different etymology, viz. from *sand. 
55139:*sam, *sand (s.v.), *zaus 
55201:(s.v.), *sand, *spas (s.v.), 
55355:*saiH (s.v.), *sand (s.v.),
```


## [2026-09-05T05:30:02.046Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21769,21800p' CHEUNG.txt; echo \"...\"; sed -n '21840,21870p' CHEUNG.txt"
}
```


### [2026-09-05T05:30:02.117Z] TOOL RESULT

```
*sand ‘to appear, seem (good)’ 

*AVESTAN: Av. sand- ‘to appear, seem (good)’ — Liste: 61 

Pres. aja-: IND. 15р. YAv. saóaiiemi (H 2.12), 25р. YAv. saóaiiehi (H 2.11, AZ 1), 3sg. YAv. saóaiieiti 
(H, Vyt), INJ. 3sg. YAv. sadaiiat (F 522), 3р1. YAv. saióin (Yt 14.56), SUBJ. 3sg. Y Av. sadaiiät (V 
2.24); Aor. s-: INJ. 2sg. OAv. sas (Y 46.19), 3sg. OAv. sas (Y 43.11), IMPV. 2pl. OAv. sastä (Y 29.1); 
Caus.: IMPV. med. 25р. YAv. sondaiian‘ha (Vr 8.1) 


*OLD PERSIAN: @ad- ‘to seem’ = Kent: 187b 

Pres. aja-: INJ. 35р. 0adaya <0-d-y> (DNa 58, DNb 53), SUBJ. med. 35р. 0adayataiy <@d-y-a-[t]-[i]-[y]> 
(DB 4.49, DSj 6), <0-d-y-a-t-i-y> (DSa 5) 

*MIDDLE PERSIAN: MMP shyn ‘apparent; prominent, splendid’ || (+ *pati-) MMP 
psyn-, psn-, BMP psnd- /passand-/ ‘to approve’ = DMMPP: 307a, 284a 

(+ *pati-) Pres.: IND. 3sg. BMP psndyt /passanded/; Partic.: perf. pass. BMP psndyt /passandid/ 
*PARTHIAN: ? swnd- ‘to slander’, swnd’g ‘slanderer’, swnd’dyft ‘deceptive talk’ (< 
Sogd., see below) || (+ *pati-) psynd- (old caus.) ‘to take a liking to” = Ghilain: - | 
DMMPP: 310b, 284b 

Pres.: IND. 3pl. swndynd {hapax} || (+ *pati-) Pres.: IND. 3pl. psyndynd {hapax} 

*KHOTANESE: OKh. sad- (sai-, sei-, sas-) ‘to appear, seem’ || (+ *pati-) pasad- (pasai-, 
pasas-) ‘to seem good’ => SGS: 130 f., 78 

*SOGDIAN: SSogd. sy-, BSogd. sy-, CSogd. sy-, MSogd. syy- ‘to seem, appear, 
show’, CSogd. syd ‘to appear, seem’, BSogd. swntk, swnt’y, CSogd. swnty ‘liar, 
deceitful’, MSogd. swndyh ‘liar’ (GMS: §966) || (+ *pati-) SSogd. ptsynt, BSogd. 
pts’ynt ‘to approve’, CSogd. ptsynt ‘to consent’, MSogd. ptsynd ‘to agree, be 
...
vo-o1ıvönıo ‘pleased’ || (+ *hu-ni-) DVo-vacoıvönuo, vo-vootvóo ‘content, satisfied’ || 
(+ *hua-) xoo-ouvóoo, xo-ouvóo ‘acting willingly, acting freely in accordance with 
one’s own wishes’ = S-W, Bact.: 223b, 177b, 229a 

*NWIR: Zaz. 4-sayis/a-sen- ‘to appear’ || (+ *pati-) NP pasandidan/passand- ‘to 
approve; cherish’, Abz. pesändowa/pesänd- ‘to agree’, Gz. pisánd-/pisánda, Ham. 
pesändayän/pesänd-, Khuns. pisend-/pisendä ‘to approve’ 

*NEIR: Wa. sodbry-, ѕыа(ы)у-/ѕәаоуа-, sodoyd, sodoyd ‘to appear, seem’ || (+ *pati-) 
Sarig. püsan-d ‘to approach, match, suit, correspond to, be equal, come up to’ 
*SANSKRIT: chand ‘to appear, please’ (RV+), chändas- (n.) ‘hymn of praising’, 
chándu- ‘pleasant, agreeable’ = EWAia I: 528 

9 This root is widely attested in Ir. 

«PIE ? *(s)Kend- ‘to agree, approve; to appear, seem (to agree)’. © Cf. Hoffmann 
1965: 165 ff. Note that the meaning ‘to shine’ is absent in Iranian *sand. The Khot. 
form cadana- ‘shining’, with atypical c- (rather than regular tc- < Ir. *C-), is most 
likely a borrowing from BSkt. = LIV: 546 | Pok.: — 

*IE COGNATES: Lat. censeo ‘I approve, judge, am of the opinion’, Gr. кёкос|цол, 
кекоёрёуос ‘to excel’, ? OCS sets ‘inquit. 0 Lat. censeo has -s- from ppp. (?), cf. 
scandö/scänsus ‘to climb, rise’, or rather from *Kens- (s.v. *sanh) ? 


334 *sanh 


*REFERENCES: TFL П: 539; Abrahamian 1936: 118; EVS: 61b; WIM I: 71; WIMII/1: 81; DKS: 418b f., 
224b; Werba 1997: 185; Paul 1998: 291b; Steblin-Kamenskij 1999: 320; Kümmel 2000: 181 ff.; Lecoq 
2002: 124
```


## [2026-09-05T05:30:11.596Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aorā\\|aora-\\|^aorā\" BRT.txt | head -10; echo \"=== avapat\"; grep -n \"ava-pat\\|avapat\\|ava.pat\" BRT.txt | head -10; echo \"=== avabar\"; grep -n \"ava-bar\\|avabar\" BRT.txt | head -5"
}
```


### [2026-09-05T05:30:11.687Z] TOOL RESULT

```
2963:IS.  aus  'aora-  Adj.,  Kompar.  aus  'ava.  —  ai. . ". .  mit   dem  ward  dieser  Sterblich"  V.  2.
3118:•  j.  ajryÖ.staora-  Adj.  'worauf  ein  Stück I  Grossvieh  erster  Qualität  (alsEusse)  steht" ": 'ye  .  .   ainim    dahm>m  Jatnti  .  .  'rim    vd
4095:aora-  104
5842:KompA.»,  E.;  AblciL  —  «i.  äifa-  m-,  ojz-J- f. ;  mp.  -(j/.  —  Pü. :  asf.  S.  noch  zu  sparman-. —  ')  Unter  den  slaora-  (sd.)  das  iweitwert- Tothte  Tier.  —  ')  Vgl.  auch  *a4bäray-,
7845:Ans  ar.  *a«j-lha- ;  ygl,  (Et.  unter  aora- ').  — Pü.;  aiuufih,  (EU  N,  41)  erl,!  ka  gäwit  ku  den ntsi;  [iD  V.  44):  anasi  iat;  Sü.:  nSsäiatvam, anäitiiatvam  'Ungläubigkeit'.  —  >>  Hds.  ifslä.
9099:'*J    Das    weltvollste    Tier"  unter    den    slaora- r.tossvieh)  nach  V.  /.  4Z-
13615:Vgl.  tdahma-,  dqjfi-ä-,  daora-,  daakak-.  —  gr. *ß«  (USW.);  Litt  IF-  7.  108  No.  I.  —  Pü.: ka  imäk  sax^an  pa  niiiähi  niktzilfratum,  erl.: dSfi.  —  OS  368.  ig;  ihem.
14248:•  j.  drvö.staora-  Adj.  (fem.  'ra-)  'das Grossvieh  gesund  erhaltend':  drväspqm  .. drvS.pasvqm  °rqm  Ytp.  r.
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
17298:•  3.  bi-3taora-  Adj.  'worauf  zwei  Stück Grossvieh  (als  Busse)  stehen' J*:  ayryS.- staorj/n  vä  'nm  vä  . .  :\^arjm{sd.)  N.  45.
=== avapat
=== avabar
9830:'o/  gaonahe  (sd.)  avabarät  .  .  *dann3m   U-A,;  *Vd.  4\  —  nmafum  ..  ä%ravat^ a  va  *vat5  *bar}snv3  vä  paiH  vayhanaAe  ^-S-^i  —  airyamm  :fannU .  ,  'vaiflm
20880:elegerint"  N.  i;  —  mi^r?m  tnä  janya  ,  , mä  yim  drvatat  ptnsitahe  mä  yitn  . . asaonai  "pactum  ne  frangito  .  .  ne  (id) quod  cum  .  .  feceris,  ne  (id)  quod  .  ." Yt  jo.  z;  —  usta  bä  yim  hacahi  ".  .  (ei) quem  sequeris"  Yt/7.  7;  —  taFöi  ayare mainyente  yat  (NSn.)  _>>««  ", .  halten  lür einen  Tag  (das)  was  ein  Jahr  (ist)"  V. 2.41;  —  ustä  astl  .  .  hyat  asäi  vakistäi ahm  (Sp.  233  u.)  ",  .  (id)  quod  (est)  .  . praemium"  Y.  27.  14;  —  ma  as  aFvB barB  (sd.)  yat  irUOm  "ne  quis  solus ferto  (id)  quod  mortuum  (est)"  V.5. 14; 14;  —  iva  dqma  ,  .  yas(ASa.)^a  da'hat spmlB  mainyuiyasca  äa^aj. .  ". .  utramque creaturam  . .  et  (eam)  quam  creavit  . ." Ytij.43;  —  ^riiat{sd.ya  .  .  glui  apa.- jasal  yatla  aiihal  .  .  yatca''  .  .  "et  tertia pars  . .  pecudum  . .  (eius)que  quod  (pe- cudum)  crit . ."  V.  2,  23;  —  tata  yal  paiii.- bannti  yä  (N.-APn.)  andu^at  *afaititat ^äjayaurva  yä..ya  aoäiti  *fr3raihyanqm (sd,)  Jrapa  *yai  nSit  visttm  (sd.)  drvatö "femer  wenn  sie  (das)  darbringen,  was.." N.54;  —  däya  ms  . .  yä  (ISn.)  ml  ai^hat afrasatfha  "des  mihi ..  (id)  quo.."  Y. 62. 6; —  iA;(sd.)  vTseyahmal{hh\'im)  kaca . .  Y. 68.1^; — havatqm  fiafia(sd.)yaÄmi(LSni.) "parynti  "..  (is)  apud  quem,."  N, /_j;  — a/raourvisvat  hrsnavainti  inm  yahmya jassnti  "..impetum  (eins)  quem  visitant"  Yt. 13.  26; — milGen.  pait,(?):^5<ja';w(  uslrd.- stärum  uzdasta  yerihä  (?)  vU  aSiö  usirB,- s/äfii/  (sd.)  aiikal  aetakm^yus  . .  V,  1$. a4(?);  —  im  Sinn  von  quantus  (s.  Sp.  120a m.):  cvail  yat  hi  kasihahe  irnvS  frat»- tntm ßisis" quaatam}  (tantum)  quantum.." V. /Ä44PiiZ.;  —  s.  noch  N.;oi?  unter "ii/.^nfis/J;  —  im  Sinn  von  quot:  ci'atgao- nahe  (sd.)  avabaräti  yä  (APn.)  *dvaeibya trizubya  (sd.)  * hartgtriwnät  ". .  (tot)  quot . . cohibuerit"  Ü-ÖS-  a)  wie  Sp.  1316  u.; erste  Person:  buyama  ahurafu  mazda  .  . astayl  yOi  narS  asavanS  humatäis  mai- nimna  , .  "wir  möchten  . .  sein,  die  (sva. indem)  wir  als  gläubige  Männer  . ."  Y. 70.4; —  zweite  Person:  uia  buyi  ajra- taintis  .  .  yH  mqm  .  .  nait  baxlake  Y.  u. *j  ^i  3i  —  ^^  ahi  yS  mqm  sbayehi  ye^he ..  srailUm  susruye  vaam  Yt. /J,  17;  — kä  tian  ahT  yim  , .  sralsttm  dädarpsa  Y, _().  I ;  —  Hsca  caräitis  ahi  yqm  . .  sralstqm dädarisa  H.  2.  10;  —  usihiiia  pliri.htiiaa-
26469:•  j.  skairya-  n.  eine  Art'*  Vorrichtung zur  Feuerung:  yö  ätnm  °yat  kaca  dsitlm gatBm  avi  avabaraiti  V.  8.  95.
```


## [2026-09-05T05:30:12.312Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==222' HID.txt | head -50"
}
```


### [2026-09-05T05:30:13.796Z] TOOL RESULT

```
Bezüglich der Benutzung des folgenden Glossars bemerke ich:
1. Alle Wuizeln und Stämme sind in ihrer mittlem Form an-
gesetzt.
2. Wurzeln, bei denen im Anlaut Gutt. und Pal. neben einander
vorkommen, sind theils mit dem Gutt., theils mit dem Pal. angesetzt, je
nachdem die Mehrzahl der bezeugten Formen den einen oder den andern
Laut bietet.
3. Bei Nominal Stämmen sind die einschlägigen Formen in der
Keihenfolge : Sing., Dual., Flur, und innerhalb der Numeri in der Reihen-
folge: Nom., Acc, Instr., Dat., Gen., Abi., Lok., Vok. gegeben. — Bei
Adj ektiy Stämmen sind die Formen verschiedener Genera in der Keihen-
folge: Mask., Neutr., Fem. aufgeführt.
4. Bei Verbalstämmen ist die Keihenfolge: Praes., Praet. (Imp.),
Imp., Konj., Opt. innegehalten.
```


## [2026-09-05T05:30:19.089Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 223 224; do echo \"=== HID leaf $n (p.$((n-13))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HID.txt | head -60; done"
}
```


### [2026-09-05T05:30:20.533Z] TOOL RESULT

```
=== HID leaf 223 (p.210) ===
I. Zu den altpersischen Lesestücken.
Buclistabenf olge :
aäituükg^Ugtdppb/nmjvr
l 8 8 8 z h.
a (ä)
Im Anlaut nicht geschieden.
1 ö-] Dem. »dieser«; § 258. —
dhjäjä,
2 a (a)] Verb.-Praef. ; = L, av. i.
aita-\ Dem. »dieser«; § 256. —
aita.
aiva-^ Nimi. »einscc, § 270. —
aivam.
j/at«-] = i. 1 j/e«-, z. }/ae«-; m./ra
Kauss. »entsenden«.
Fraes. 9 : frairnjam^ fräuaja,
a%8\ s. l/q/-.
auramaze^äA-] S. m., Name des
höchsten Gottes , »Ormazd«; §182;
cf. av. ahura- -[- mazdäh". — ^dä,
^däm, ^däha,
>akütä] s. ykar-,
atij] Verb.-Praef.; = i. dti, z.
aiti.
a dam] § 266.
apatara-] A. Komp. »anderswo
befindlich, sonstig«. — ®am.
a piß Part, »auch«; = i. dpi, z.
abij] Praep. m. Acc. »zu«; = i.
ab^t, z. aitvi.
anämaka-] S. m., Monatsname.
— ^kdhjä,
a n ij a-] A. »ein andrer, feindlich« ;
= i. anja-t av. an^a", — anija,
anüsija-] A. »nachfolgend, An-
hänger« ; aus anu = i., z. dnu -f- (;V<-,
§ 108 und Wh., § 1245 b. — »5.
amä^am] § 266.
amtj'] s. j/aÄ-,
amüpa] Adv. »von dort her« ; cf.
i. amütas,
yaj-] = i. i/a/-, av. ]/«;(-; »gehen,
marschiren« ; — m. atij »vorbei m.«;
— m. para »fort m.«.
Praes. 1 1 : ais, atißis , paraitä
(2. PI.).
P.P.P.: paraitä (d 64; sc. hatij
»sie zogen aus«}.
aj'] Dem. »dieser« ; § 262. — ijam.
a ja star-] S. m. »possessont; aus
tf + 1^/«^ — h Suff, tar-; m. Acc.
konstruirt. — ajaatä (c 47: af*
uväipaaijam akütä s. v. a. »er machte
sich zum Selbstherrscher« ; — d 42:
käram q;*® s. v. a. »mit seinem Heer«),
ava] Verb.-Praef.; = i. dva, z.
a^a.
ava-] Dem. »jener«; § 259. —
avain. — ava, avahjä, avahja^.
avadä, avada^] Adv. »dort«; s=
=== HID leaf 224 (p.211) ===
210
in. Glossar.
arikch] A. »feindlich«, cf. i.
ardj-, — ^ka.
ar had raj-] S. m., Name eines
Bergs; cf. i. arkd- und ^d^raj-, —
""dns.
m
artavardtja-] S. m. , Name
eines Feldherm. — ya, yam.
ars°] s. |/ar-.
araadä-] S.f .,Name einer Festung.
— ""da.
a Sahara-] S. m. »Reiter«; aus
asor »Pferd« (§ 87 Anm.) + 6® = i.
"Sard-, — ^raibis.
a smart-] S. m. »Himmel«; =s i.
asman-, av. asman-. — ^mänam.
azdä-] S.f. »Kunde«; = i. add^or,
g. azdä-, — azdä,
yah'] = i. Ij/a»-, av. 1 j/oä-; »sein«.
Fraes. 11 : armj. — aha; ahatä.
•
t
id a] Adv. »hier«; s= i. ihd, z. täa.
{Jam] s. fl[/-.
tm^] Dem. »dieser«; § 257. —
»ma. — imäm,
u
utä] Part, »und«, dopp. »sowohl —
als auch« ; = i., z. utd.
ud] Verb.-Praef.; = i. tid.
upastä-] S. f. »Beistand«; = z.
upastär-. — °stäm.
upä] Praep. m. Acc. »bei«; = i.,
z. üpa,
umartijä-]A. »menschenreich« ;
aus u=si, SU, av. hu + w®. — °tijä.
UV asp ä-] A. »rossereich«; = i.
svdsva-, z. h^a8pa-, — ^pä.
uväipasija-] S. n. »Selbst-,
Alleinherrschaft«; cf. i. svdpataj-,
— yarn. .
uvädaiU a Ja-] S. m., Name einer
Stadt. — ""Maja.
uvämars ija v-] A. »durch Selbst-
mord sterbend« ; aus uvä = av. $ä,
cf. i. sva- + m° = i. mrijäv-, av.
merepia^-, — ^*m».
uzma-] A. »über der Erde befind-
lich«; aus ud -[- a®, cf. av. zorn-
ig 177). — uzmc^a (Sg. L. n.) patij
4- l/A;ar- s. v. a. »kreuzigen«.
k
k a-] Interr. »wer« ; § 254 ; — m.
UiJ »irgend einer«. — kasMiJ,
kaufa-] S. m. »Berg«; = z. kao-
fa-. — ya,
kahugija-] S. m. »Kambyses«.
— ya, y'am, yahjä, y'ä,
```


## [2026-09-05T05:30:30.035Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if \"'aora-  Adj.,  Kompar.\" in l:\n        print('leaf',i)\n        nums=re.findall(r'\\n\\s*(\\d{2,4})\\s*\\n', l)\n        print('nums',nums[:20])\n        j=l.find(\"'aora-  Adj.\")\n        print(l[max(0,j-1500):j+600])\n        break\nEOF"
}
```


### [2026-09-05T05:30:31.843Z] TOOL RESULT

```
leaf 61
nums []
 128;   129—132*,
ASn.  aus  tava:  —  0  Vgl.  toa  mit  No.  3.
•  j.  aoman-"  Adj.  'helfend,  beistehend': tä  nS  . .  %räy?nle  .  .  'mtta  (IS.)  ahura mazda  sraoiaea  .  ,  ".  .  una  cum  juvante AhM.  et  Sr."  Ytij.146.
Zum  V.  av-.  —  ai.  <<man-  Adj.  —  0  Falsch DST.  ZA.  2.  555;  s.  Bthl.  IF.  u.  104.
dby  Google'
43  aorS  —  *aka-  44
j.  oömim  FrW.  g.  tt:  lies  amim.
j.  ai  aoyaiHii'  P.  2/1  lies:  aSaiy*,  amal. •  j,  g.  aora  Adv.  'nach  unten,  tünunter, hinab':  raocä  (sd.)  usca  usraocayeiti  . .  °ra äraocayäti  V,  2.40  PüZ.;  —  yai  äim  usüa
'9Zi  46;  —  aAy3  veha  'iö  vidi  (sd.) fftanatjM  Y.4ff.  i ;  —  me/u  t/it  paiti  aiin- ttaot   "Sarshai   kva  Aisra  V.  2. 5  PüZ.  (?)
Ableit.  —  aL  •öiai-.  —  \g\.  aosa-.  —  Fü. :  öS. •  j.  aoäah'vant-  Adj,  (fem.  "vaiii-)  'dem
uüdvanayal . .  nOii  °ra  avßirisyät  (s^.)  Yt.  Untergang  ausgesetzt,  vergänglich,  slerb- 5.62;  —  'ra  vatiuhls  ußa.saaa  {%A.)  VLjlich':  azdibl^  ,. 'sati/iat'^yäs?  tanvö  V.4. y.  147;  —  paracil  mraoüs  (sd.)  'r^lcä ;  $0;  —  am  "/uwAs"  'iaauAaiti^^  qshm yairJ  mainyus  drfgvats  ^-  53-T,  —  °ra\isaili  tanva  Aog.4<?;  —  ahmi  dhn  patti F.  7;  —  *°rä(a'>  paraca  tarasl'a  F._ya.     \  fran/nnzal  {&&.)    ahmi  fw    bazal  'lanha
IS.  aus  'aora-  Adj.,  Kompar.  aus  'ava.  —  ai. . ". .  mit   dem  ward  dieser  Sterblich"  V.  2.
vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
T""'7  ^  Hds.  Iu,ra.a,  m,t  k  statt  a;  vgl.  p,_.  ..^.^^_^_  _-;j  j-^^^^^^  6^-^  unsicher.  - *■  ■'■'■  '■  =)    Dk.  JJ.  22.   12:    «  in   pa    äa   äiSmaJul  bül,
•  g.  aoz-  V.  'achten'.     Praes.  i  uz-.       \     näml.  Kavay  Vi,,»-,  vgl.  Dst.  ZA.  j.  39. 'achten  für  -',  mit  dopp.  Aklc. :  ki  kvö  ,  j.  ao§ö.tara-  Adj.  'der  verderblichere,
y}m3  arsdrv  m>a
```


## [2026-09-05T05:30:38.819Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'\\b175\\s+ava', l) or re.search(r'176\\s+av', l) or ('avar?' in l and i<160):\n        print('leaf',i, l[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T05:30:40.650Z] TOOL RESULT

```
leaf 127 n^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>. Pn.:_/>ö/  ianih^.    —    ■)  iSL  t,  unter  ullre.- •  j.  ava-kanta-  n.  'Graben,  fossa':  yai aisa  gaViOa  'ttüfva  frajasät  V.  /5
```


## [2026-09-05T05:30:43.624Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(124,132):\n    l=leaves[i]\n    print('=== leaf',i, re.findall(r'\\b1[67]\\d\\b', l)[:8])\n    print(l[:400].replace('\\n',' | ')[:400])\nEOF"
}
```


### [2026-09-05T05:30:45.342Z] TOOL RESULT

```
=== leaf 124 []
J  'va  '>  apaMm  (sd.)  gayeAe  Yt.  /().  44.  hat  dich  gern  gehabt  wegen  jener  (deiner) KompA.  i  Abldt.  ^  a^rS).  -  S._  auch  a-^ö  ~-  ^  q^q^^^  ^^^  .  .'■  H.  2. 11 ;  —  ai/at  tljas.lni ai.    ai'fl   Fraen.,   Praev.j    mp.  n  dm.    —    I  u.  .,  -  ,,  ,     , | (zu  V.  9):  afar.  (in  V.  5):  afar  S,{t.xi.  2  und  I  ava&lu..avi  -Vat  varS_  Yt  72.4  (Vgl.3,  
=== leaf 125 ['166', '168']
'vam  asiyav^  Bh.;.ii;  —  *utilmaiy amyaiiiy  vasiy  astiy  kartam  °v<^  .  .  naiy nifistam  Bh.  4.8;  —  tuvam  ks  hyc^ imäm  dipim  vainahy  .  .  imatvä  patikarä . .  yävä  (sd.)  *taumä  *ahatiy  *äva  °vaiy pariiarä  Bh.4-i5;  — ya'^a  «J  snaihi^. paiti.vaiaMt  'vat  paiti.päpayamnS  "..eine Waffe  .  ^  sich  dagegen  zu  decken  suchend' P.  2/;  —  afavatum  mahrka'^ni  aon äinrnta
=== leaf 126 ['169']
 .  .  yä  .  .  upa.dvqsaiti  V, 17;  17;  —  Aaca  'vai/ihai  Jahikayäi  .  . yä  .  .  upa.baraiti  (sd.)  Yt.  17. 58;  —  nsU 'va  (APf.)  zaoira  ..  yä  ..  framthar>nii Yt5.93;  I4.\i\  —  *'va}ika  (APf.)  > va^ays  .  .  yä  .  .  anhan  Y.  2j.  1 ;  —  •; (APn.)  dämqn  . .  yi  A^nti  . .  Vr.  7.4;  — •w7(/  uroaikis  (sd.)  ya  ta  . .  didirszd  Y. 44--ii;—''*'vä  (NPf.)  dakyäve^ 
=== leaf 127 []
n^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>. | Pn.:_/>ö/  ianih^.    —    ■)  iSL  t,  unter  ullre.- | •  j.  ava-kanta-  n.  'Graben,  fossa':  yai aisa  gaViOa  'ttüfva  frajasät  V.  /5.38, | Zum    V.  *ian-;    vgl.    niiania:    —    Pü.:   frei | •  j.  ava-;iiana-  Adj.,  PPM. :  s.  'gan-. | •  j.  a-va£ah-  Adj.  'stimmlos*  sva.  'der seine  Stimme  nicht  braucht'  (vo
=== leaf 128 []
'  '^"■„^ür '  (angegebene)  Weise  sind  sie  . ."  V.5.S4; ')  Aber  Bh.  3.  1 1  steht  miadahm.  —  3)  Hds.    0°  ^^  '  ^       j-     .       .     * | a^apa;   s.  ^.15.  -   «  Wörtl.  'tod  da  ihin'i*36.  0-4»,  7=3;—  '^a /robfnta  *zao- Btatt   'da  von  ihm' ;   halä  fa*  (AbS. ;  e.  ki'n-) ,  är«   frabarStt  N,  03.  b)    zeitlich    'zur | wie  hammJ';  Bthl.  BB.   7^^.  247
=== leaf 129 ['173', '174']
: tiS«,  Sü.:  rt'am, | •  j.  ava(he  (indekL):  ihe  (sd.)  tha  yahna ahmai  av°   iha  yahna  ahmsi  avSya  iha | lyahna  ahmai  Yt  75.63.  Sinnlose  Fluch- worte. | *ava.3Twar98a-    m.    'Abschneiden, | dby  Google | 173 | avaSra | avant- | 174 | •  j.  ava-Duhabdamna-,  -Dhabdamna- Adj.,  PPM.:  s.  :e'ap: | KompE. | j.  avanräsayäl  N.  ^j  s.  ras-. | •  j,  ava-ahabdant-  Adj.,  PPA.: 
=== leaf 130 ['176']
Pü.: aiapt  Sflisn.  —  D  iSt  und  Konttr.  s.  RV.  1. 17.  S,  /.  105.  3- | dby  Google | I7S  avanta- | naire  mßd^m  aaAal  A.4.^—6.-  a)  ASn. als  Adv.  'so  lang,  tamdiu',  mit  dem  Kor- relat yavat'.  yavat  isäi  itniäca  'val  xsäi.. Y.2^.4. | Ob  alt?  Vll.  Neuschöpfung  t\x  y/nanl-  (nach yahoiäi :  ahmäi  usw.);  vgl.  p.  *ävä.  Annahme von  Haplol.  (KZ.  2$.  49SJ  ist  jed
=== leaf 131 ['177', '178']
^qm  hl  'Iqm  altahmifi  naire frabi!ray?n  V.5.39;  ig.id;  —  zur5.bir»ta ,'iä  F.:.'0;  —  Ptspanqm  *°tanqm  saiiavai- | dby  Google | 177 | avareS'a- | avahmya- | 178 | lanam  (sd.)  Vd.iy;  —  a^ö  baysm  haca 'la/iam  Vd.  2.  a)  insbes.  mit  ySahuya- (sd.)  Adj.  'bewegliches  Besitztum,  fahrende Habe':  *yri»huya  'ta  F.  4fi  —  kasvikftm- iina  yhtfhuyanqm  °tanam  V.l$.^4,  37, ?.
```


## [2026-09-05T05:30:49.930Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[130][:3000])\nEOF"
}
```


### [2026-09-05T05:30:51.598Z] TOOL RESULT

```
Pü.: aiapt  Sflisn.  —  D  iSt  und  Konttr.  s.  RV.  1. 17.  S,  /.  105.  3-
dby  Google
I7S  avanta-
naire  mßd^m  aaAal  A.4.^—6.-  a)  ASn. als  Adv.  'so  lang,  tamdiu',  mit  dem  Kor- relat yavat'.  yavat  isäi  itniäca  'val  xsäi.. Y.2^.4.
Ob  alt?  Vll.  Neuschöpfung  t\x  y/nanl-  (nach yahoiäi :  ahmäi  usw.);  vgl.  p.  *ävä.  Annahme von  Haplol.  (KZ.  2$.  49SJ  ist  jedenfalls  un- nötig. —  S.  noch  »oi-fl-.  —  Pii. ;  an  i  and. Sü.;  lävän.  —  ')  NA.  avavali  s.  aber  Var. und  NA.  lu  V.  //.  7.
•  j.  a-vanta-  Adj.:  s.  unter  abania-,
j.  asiantarf  V.  5.  11 ;  lies  aua-anlata.
•  j.  ava,m9r«tay-  f.  'Sterben,  Tod'  uzw. i/dA^cher  Wesen'*:  tat  asti  yUnd  duhna- nat?hs  . .  i^arshfm  pasca    'ntfim    H.  2.
3«;  36.
Pü.:  ftSl  minmi/i.  —  1)  Im  Gegensati  10 paraJrislay',  vgl.  H.  2.  18.
•  j.  avaya-  m.  EN.  eines  Gläubigen;  yehe sptnghahe  alaonS  Yt  Jj.  123.
Et.  und  Bed.?  —  Var.  avahythr  MfJ.
•  j.  ava-yam-"  f.  'Abwendung*;  aSat  te .  .  aiAke  °yqm  (AS.)  *dqnmaki  yat  %'W3 didvtsma  "das  machen  wir  dir  .  .  zur  Ab- wendung dessen,  dass  wir  dich  beleidigt haben"  Y.  68.  i.
KompE.  —  Zum  V.  j-a«- 1) ;  ai.  vgl.  avayäldr- m.  —  Fü. :  pa  aySviirik.  —  ■)  Anders  (falsch) Gdh.  KZ.  iS.  407,  Jn.  JAOS.  13.  ccxu,  Bthi. JF.  3.  37  und  S  SSi- j.  avayäl  F.  7:  lies  avdiil.
•  j.  avavaitya  Adv.  'tantundem',  mit  Akk. der  Beziehung;  als  Korrelat  folgt  ya^a: pairi  dim  tanava . .  urväntm  . .  av  bazascä frakasla  fairi.tanuya  yai^a  Im  zS  Y.79.7,
LS.  aus  atiavanl-,  —  Pü.:  pa  äiti  and  takäk  » faknäk.
•  j.  avavat  Adv.  'in  solcher  Grösse,  Masse, Entfernung,  Weise;  ebensosehr,  ebenso': *av'  F.  7  " ;  —  'vatat  Vd.  75.  a)  sonst  1 mit  dem  Korrelat. ^a^u :  ye^Ju  av  . .  tüti  1 SpS  ava.barpnte  yaia  vupa  imi  äpS  .  . Yt  5.  1 S ;  —  ^^  haca  iristaäbyS  yaia ^rigäim  V.Äii;  39,  76,  p.39;  — yd^a iattm  kaydhanqm  av  asava./aalYt  JO.z; — y3  av°  xSva^zvs  vasaiti .. yäka  tiyris.. YtÄö;  —  'vaiai  yaka  kv5  ptruahe'^. 7.53  PüZ.
ASn,  aus  avavant-.  —  K.:  an  i  and,  (Vd.):  and {and.  —  ')  Hds.  aj-aial.
'].  avaz'at  Yl.  5.  ISO:  s.  iaV:
•  j.  ava'vant-  Adj.  (fem.  'vaitf-)  'tantus; talis':  °Tani>m  asavayny,li  (sd.)  tarn  ctiqm daisayS  V.  5. 14(?).  A)  sonst  mit  dem Korrelat',!'!!^!!;   1) 'wie,  als':   -i'atät yaka
avarata-  176
sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern
```


## [2026-09-05T05:31:01.156Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==43' HRN.txt | head -60"
}
```


### [2026-09-05T05:31:02.693Z] TOOL RESULT

```
- 21 —
85. U8tu%än, geschrieben ustux^än *Knochen, Kern'.
phlv. aslux^dn (AV.); zu aw. ast- 'Knochen', s. est
(No. 81).
Die merkwürdige Form findet sich als LW. im
Kurdischen, in den Pämirdialekten (sar. ust/än, wa/.
usta/än und wohl auch Uyn, sit/än) u. ö.
86. ester ^Maulesel'.
phlv. astar; ai. agvatard- 'Maulesel'.
kurd. istir, histir; bei. istal, n. hastal (438).
87. iiStur *Kameer, sutur.
aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68);
ai. üstra-,
kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161);
wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?).
88. eSk *Thräne .
g. sah,
aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog.
Forsch., II, 136).
afy. ö^a resp. ö/a; wsl/, ya^k, sar. yujck,
Vergl. ers (No. 69).
89. iiSnän Name einer zum Waschen gebrauchten Pflanze,
Herba Alkali (AM. 28; 37 Zeile 2), sunan (DWlfi'IN,
Jer. 2, 22).
arm. LW. ausnan 'Seifenkraut*,
aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
Zu aiwis vergl. indessen unter bes-, bis- (No. 221).
90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
germ. Vhnus bezw. /wws, vergl. ahd. niosan^ mhd.
') Die Awestaform ist von de Lagarde falsch angesetzt, der
die Lautverhältnisse verkennt.
V V
*) FR und FJ haben die folgenden Belege (nur FJ constatirt
einen Majhülvokal): (Metr. Hezej)
deniäyl pisk'l ö esnösc'l ter
cü äred gös^ gerdünrä küned her
Abu'l Xeir.
(Metr. Hezej):
merä imröz^ tobe süd^ däred
ciinänci derd-i dendänrä senöse
Rüdegl.
```


## [2026-09-05T05:31:06.095Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==44' HRN.txt | head -60"
}
```


### [2026-09-05T05:31:07.637Z] TOOL RESULT

```
- 22
niesen, an. hnjosa, mittelengl. fnesen niesen', ver-
schieden von mittelengl. snesan, engl, to snee:se
(Kluge, Etymolog. Wörterbuch).
kurd. heenlsum *ich niese' (Justi, No. 66, wo auch
die Etymologie).
Die neupersische Grundform müsste *senöse sein.
91. ef-, ew-, Praefix, ß-, fu-,
ap. abiij 'herzu'; aw. aihi, aiwi *herzu, oben' etc.;
phlv. a/-, päz. awa-; ai. abhi 'herzu, oben' etc.
92. uftäden ^fallen', Praes. uft-em, fitaden, uftädegt
(Sa dl, Bostän 4, 1 Graf).
aüa-\- [/^pat'\ phlv. öftätan, öftet (vd. 6, (73) Gl.,
16, (20) Gl.), öftad (vd. 19, 94), oft falle (Göät-I Fr.),
vergl. öfttnltan, äwäZ'öft(i)smh (vd. 16 (64) Gl.),
öft(i)sn (Ys. 43, 4, aw. avapasti-) ^).
Im Neupersischen findet sich bei Dichtern noch
öf laden (die Aussprache mit ö ist allerdings nicht
bezeugt), z. B. Vis und Rämin, S. 61, Vers 5 v. u..
Sahn. I, 88, Vers 494, Sa di, Gul. (Sprenger), 38 Zeile 9.
93. efräiten 'erheben', efrästen, Praes. efräz-em, ewrästen,
ewraz (AM.), ini^N^DN (jüd.-pers.).
phlv. afrästan {afrä/tan zu lesen?) erheben.
Zu [/reg- + ahhi richten, aufrichten'; ai. irajydti
er richtet'; gr. oQfyw^ oQsyvv/Lu Vecke'; lat. rego richte';
got. uf-rakjan 'in die Höhe recken'.
wa;^. püt\rüzam, sar. pat\räzam 'sich recken, gerade
stehen'.
So viel ich sehe, ist die nahe liegende Etymologie
vor KZ. 32, 579 No. 4 noch nicht ausgesprochen
worden.
(Wohl die ersten zwei Misrä^'s eines Rubä*l)
cHn sepled ez m^y-l mü*ambär-t ^öse
göyed k*ekimn nemänd^ jäi/'i senöse
Minöcihrl.
*) Bevorzugter ist im Pehlevl öpa^tan.
```


## [2026-09-05T05:31:16.169Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"obärden\\|obarden\\|ubär\\|obär\\|awbär\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-05T05:31:16.231Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:31:19.281Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"verschlingen\\|schlucken\" HRN.txt HUB.txt | head -10; echo \"=== nyberg\"; grep -n \"^ōbār\\|obār\\|ʾwpʾl\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T05:31:19.354Z] TOOL RESULT

```
HUB.txt:6240:arm. gaz-pen ; Dbdstan anfiillen, verschlingen', phi. opdrtan ;
HRN.txt:745:ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
HRN.txt:746:wa;^. nez-yar-am verschlingen*.
HRN.txt:1569:132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
HRN.txt:1573:phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
HRN.txt:8047:gala-; lat. gula; arm. vergl. -kul '-verschlingend' (H.
=== nyberg
```


## [2026-09-05T05:31:22.891Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1560,1600p' HRN.txt; echo \"=== which page\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:1568])\nleaf=t[:idx].count('\\f')\nprint('leaf',leaf,'printed page',leaf-22+1)\nEOF\necho \"=== HUB context\"; sed -n '6225,6255p' HUB.txt"
}
```


### [2026-09-05T05:31:24.523Z] TOOL RESULT

```
*) Der Wechsel von st und st ist häufig.
'') Vergl. Fr. Müller, WZKM. 5, 264.— 31 —
Darmesteter's Erklärung (Et. ir. I, 75) aus
*apama' d. i. apa 4- ama- = lat. abemptum ist aus zwei
Gründen unmöglich: erstens weil die Grundbedeutung
von emö nicht ^kaufen*, sondern nehmen* ist (vergl.
lit. imü, ifriti nehmen', air. ein 'nehmen*, ksl. imq,
jpM 'nehmen'); zweitens weil lat. emö auch zu got.
tnman gehört, also seine Urform *^rwö lautet.
132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
(Jer. 51, 44).
ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
V. u.); Thron*.
ap. *avaranga- oder wohl besser '^abiranga- (vergl.
skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
134. euJzen (geschrieben evzen) 'tödtend*, in ser]ewzen
(Sahn. I, 100 Vers 714, 450 Vers 288), hezber\ewzen
(Sahn. I, 356 Vers 659).
aw. aiwi + l/^aw- 'tödten' ; phlv. afzatan (PPGL),
päz. awazadan.
Np. evzendlden der Wörterbücher ist nur eine gram-
matische gelehrte Bildung ; über die Emendation ewzen
vergl. Salemann-Shukovski, Neup. Grammatik, § 7
(dieselbe verbietet die Ableitung von ava-),
135. östUm, ustam 'treu, ergeben' (Vis und Rämin, Seite 78
Vers 12 1).
ap. ^avastaman- 'zuverlässig*, vergl. skr. ava-r
i/^sthä' 'bleiben, verharren*, avasthita- (von Personen)
'standhaft, zuverlässig*; phlv. östam bezw. tistäm
'Helfer (Men., vergl. awastäm, West ib.).
136. öi 'er, jener, vei,
ap. ava' + hya-; päz. öi.
*j Hier scheint es aber ^schwach* zu bedeuten.— 32 —
öi und vei sind im Neupersischen zwei Doubletten
ohne jede Bedeutungsnüance ; vei wird dann auch im
Sinne des lat. -plex verwendet.
öweste (nnoziN) siehe unter pest (No. 316).
=== which page
leaf 52 printed page 31
=== HUB context
sev = seb 'Abhang' H. 799; mar i sehd * Viper (bei Vis u
Ramin 178, 7 v. u. nach v. Stackelberg), sevd 'beredt*,
phi. s^dk, H. 800 und 804, oben p. 82 und 83; vEm - beza
Vein*, phi. apecak oder apejak; abranfan *Spange* = avranjan
(§ 72) ; barvdr neben varvdra 'balcony* (oben p. 28) u. s. w.
Ueber verdn 'wiist* berdn = (JRAS. 1894, p. 430) s. oben
p. 105.
§ 68. Ap. p = np. 6 (paz. tv) in:
be. abe ohne = phi. ape- ; bumd *Jungling , zd. aperen-
dt/u-; bdxtar 'Westen, zd. apdxtara- (siehe § 2); bdz
zuriick, offen', skr. apdc-; baxsudan 'gnadig sein', phi. apux-
sdyisn ; bar, abar auf, iiber , ap. upariy ; bd *mit', skr. updke;
bayad *ist nothig, phi. apdyat; dbis-ian *schwanger , zd. *^/?w-
d^ra- (oben p. 5) ; dsob *Verwirrung, phi. dsop (s. oben p. 7);
abresum 'Seide', arm. aprisum ; angubm 'Honig , phi. angpeti^
arm. gaz-pen ; Dbdstan anfiillen, verschlingen', phi. opdrtan ;
bob Tater' aus *pa5 = phi. *pdp (oben § 65); -bad, -bud
'Herr (in Komp., vgl. H. 188 und 1115), zd.paiti-; biydbdn
*Wuste' (? H. 248) ; taham 'brenne, warme, leuchte', tdbistdn- 177 -
Sommer*, tcA *Fieber , tabis *Hitze', skr. zd. tap, arm. tap *Warme,
Hitze*, tapanam *fiebere'; dob *Holz, Stock' = phi. dOp; ocub
gut, sch5n' = skr. suvapufi-; dibtr 'Schreihev = arm. dpir;
deba *Brokat' = arm. dipak; rubayad raubt' = *rupaffati^
rObad *fegt* = *raupati; rdhah 'Fuchs' = phi. rOpas; sab
*Nacht*, ap. xsapa-va; sitab *Eile', arm. stap; farbih 'fett',
zd. frapidwo; kabast 'Koloquinthe' (? H. 840); kabk Reb-
huhn' (? H. 841) ; kabutar 'Taube', kabud *blau*, arm. kapoit
'dunkelblau ; lab Xippe (oben p. 96) ; 7iab rein, ungemischt*,
zd. andpem (ace); wat^ *Fruchtsaft, Wein H. 1025****; nisBb
'Unteres, unten H. 1034; vireb *curvus', arm. vr^ 'torto,
perverse*; kobm *Mitgift', arm. kapenR; kabl *ASe = phi.
```


## [2026-09-05T05:31:42.472Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '1,50p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-05T05:31:42.513Z] TOOL RESULT

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


## [2026-09-05T05:31:45.851Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/خرسند\" \"https://en.wiktionary.org/wiki/افتادن\" \"https://en.wiktionary.org/wiki/اوباش\" \"https://en.wiktionary.org/wiki/west\" \"https://en.wiktionary.org/wiki/Ukraine\"; do python3 tools/fetch_source.py \"$u\" --note \"page 69, root Au 2/We 2 — checking Nourai's derivation\"; done"
}
```


### [2026-09-05T05:31:51.990Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4388b1ee49f04b4a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c737378475aa2481.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f013839dec9af46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7710d581e6f13ecd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1975d30506154cd6.txt
```


## [2026-09-05T05:31:53.955Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 4388b1ee49f04b4a c737378475aa2481 9f013839dec9af46; do echo \"######## $f\"; grep -n -A15 -i \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-05T05:31:55.635Z] TOOL RESULT

```
######## 4388b1ee49f04b4a
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Adjective 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.5 
80- References 
--
155: Etymology
156- [ edit ] 
157-
158- Inherited from Middle Persian [script needed] ( hwnsnd /⁠hunsand⁠/ , “ happy, contented ” ) . [ 1 ] 
159-
160- Pronunciation
161- [ edit ] 
162-
163- ( Classical Persian ) IPA ( key ) : /xur.ˈsand/ 
164-
165- ( Dari, formal ) IPA ( key ) : [xʊɾ.sán̪d̪] 
166-
167- ( Dari, formal ) IPA ( key ) : [xʊɾ.sán̪d̪] 
168- ( Kabuli ) IPA ( key ) : [xʊɾ.sán̪d̪] 
169-
170- ( Hazaragi ) IPA ( key ) : [xuɾ.sán̪d̪̥] 
######## c737378475aa2481
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Conjugation 
75-
76- 1.4.2 
77- Derived terms 
78-
79- 1.5 
80- References 
--
157: Etymology
158- [ edit ] 
159-
160- From Middle Persian [script needed] ( ’wpt- /⁠ōft-⁠/ , “ fall ” ) , from Proto-Iranian *ava- ( “ away, down ” ) + *pat- ( “ to fly, rise; to fall ” ) , the former from Proto-Indo-Iranian *Háwa ( “ away, down ” ) , the latter from Proto-Indo-European *peth₂- ( “ to spread out; to spread one's wings, fly ” ) . [ 1 ] 
161-
162- Pronunciation
163- [ edit ] 
164-
165- ( Classical Persian ) IPA ( key ) : /ʔuf.taː.ˈdan/ , /ʔaf.taː.ˈdan/ 
166-
167- ( Dari, formal ) IPA ( key ) : [ʔʊf.t̪ʰɑː.d̪án] , [ʔäf.t̪ʰɑː.d̪án] 
168-
169- ( Dari, formal ) IPA ( key ) : [ʔʊf.t̪ʰɑː.d̪án] , [ʔäf.t̪ʰɑː.d̪án] 
170- ( Kabuli ) IPA ( key ) : [ʔʊf.t̪ʰɑː.d̪án] , [ʔäf.t̪ʰɑː.d̪án] 
171-
172- ( Hazaragi ) IPA ( key ) : [ʔuf.t̪ʰɔː.d̪án] , [ʔäf.t̪ʰɔː.d̪án] 
######## 9f013839dec9af46
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Usage notes 
72-
73- 1.4 
74- Further reading 
75-
76- Toggle the table of contents 
77-
--
145: Etymology
146- [ edit ] 
147-
148- Borrowed from Arabic أَوْبَاش ( ʔawbāš ) , plural of وَبَش ( wabaš ) .
149-
150- Pronunciation
151- [ edit ] 
152-
153- ( Classical Persian ) IPA ( key ) : /ʔaw.ˈbaːʃ/ 
154-
155- ( Dari, formal ) IPA ( key ) : [ʔäw.bɑ́ːʃ] 
156-
157- ( Dari, formal ) IPA ( key ) : [ʔäw.bɑ́ːʃ] 
158- ( Kabuli ) IPA ( key ) : [ʔäw.bɑ́ːʃ] 
159-
160- ( Hazaragi ) IPA ( key ) : [ʔäw.bɔ́ːʃ]
```


## [2026-09-05T05:32:05.143Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '150,175p' 4388b1ee49f04b4a.txt; echo \"#### refs\"; grep -n -i \"Hasandust\\|References\" -A6 4388b1ee49f04b4a.txt | sed -n '1,40p'"
}
```


### [2026-09-05T05:32:05.214Z] TOOL RESULT

```
 خورسند ( xorsand ) ( misspelling ) 

 خنسند ( xunsand ) ( obsolete ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [script needed] ( hwnsnd /⁠hunsand⁠/ , “ happy, contented ” ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xur.ˈsand/ 

 ( Dari, formal ) IPA ( key ) : [xʊɾ.sán̪d̪] 

 ( Dari, formal ) IPA ( key ) : [xʊɾ.sán̪d̪] 
 ( Kabuli ) IPA ( key ) : [xʊɾ.sán̪d̪] 

 ( Hazaragi ) IPA ( key ) : [xuɾ.sán̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [xoɹ.sǽn̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [χuɾ.sán̪d̪] 

#### refs
80: References 
81-
82- Toggle the table of contents 
83-
84- خرسند 
85-
86- 4 languages 
--
227: References
228- [ edit ] 
229-
230- ^ MacKenzie, D. N. ( 1971 ), “hunsand”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 45 
231-
232- Retrieved from " https://en.wiktionary.org/w/index.php?title=خرسند&oldid=92293107 "
233-
```


## [2026-09-05T05:32:06.597Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### west\"; grep -n -i \"Proto-Germanic \\*west\\|Etymology\" -A12 7710d581e6f13ecd.txt | sed -n '20,80p'; echo \"### ukraine\"; grep -n -i \"Etymology\" -A12 1975d30506154cd6.txt | sed -n '20,70p'"
}
```


### [2026-09-05T05:32:06.692Z] TOOL RESULT

```
### west
108- 2.2.1 
109- Synonyms 
110-
111- 2.2.2 
112- Antonyms 
113-
114- 2.2.3 
115- Derived terms 
--
123: Etymology 
124-
125- 3.2 
126- Pronunciation 
127-
128- 3.3 
129- Adverb 
130-
131- 3.3.1 
132- Synonyms 
133-
134- 3.3.2 
135- Antonyms 
--
152: Etymology 
153-
154- 4.2 
155- Pronunciation 
156-
157- 4.3 
158- Noun 
159-
160- 4.4 
161- References 
162-
163- 5 
164- Kashubian 
--
169: Etymology 
170-
171- 5.2 
172- Pronunciation 
173-
174- 5.3 
175- Noun 
176-
177- 5.3.1 
178- Declension 
179-
180- 5.3.2 
181- Coordinate terms 
--
200: Etymology 1 
201-
202- 7.1.1 
203- Alternative forms 
204-
205- 7.1.2 
206- Pronunciation 
207-
208- 7.1.3 
209- Noun 
### ukraine
108- 2.3 
109- Proper noun 
110-
111- 3 
112- Danish 
113-
114- Toggle Danish subsection 
115-
--
117: Etymology 
118-
119- 3.2 
120- Proper noun 
121-
122- 3.2.1 
123- Related terms 
124-
125- 3.3 
126- See also 
127-
128- 4 
129- French 
--
134: Etymology 
135-
136- 4.2 
137- Pronunciation 
138-
139- 4.3 
140- Proper noun 
141-
142- 4.3.1 
143- Related terms 
144-
145- 4.3.2 
146- Descendants 
--
157: Etymology 
158-
159- 5.2 
160- Pronunciation 
161-
162- 5.3 
163- Proper noun 
164-
165- 5.3.1 
166- Usage notes 
167-
168- 5.3.2 
169- Declension 
--
```


## [2026-09-05T05:32:11.825Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Proto-West Germanic\\|\\*westraz\\|Proto-Germanic\" 7710d581e6f13ecd.txt | head -6; echo \"###\"; grep -n \"Ukrainian\\|ukraina\\|Україна\\|окраина\\|borderland\\|край\" 1975d30506154cd6.txt | head -12"
}
```


### [2026-09-05T05:32:11.886Z] TOOL RESULT

```
487: From Middle English west , from Old English west , from Proto-West Germanic *westr ( “ western ” ) , from Proto-Germanic *westrą ( “ west ” ) , from Proto-Germanic *westraz ( “ west ” ) , from Proto-Indo-European *wek⁽ʷ⁾speros ( “ evening ” ) .
1842: From Middle Dutch west , from Old Dutch west , from Proto-West Germanic *westr , from Proto-Germanic *westrą . Compare German West , English and West Frisian west , Danish vest .
1953: Proto-Germanic *westraz 
1954: Proto-West Germanic *westr 
2070: From Old English west , from Proto-West Germanic *west , *westr , from Proto-Germanic *westrą , from *westraz , from Proto-Indo-European *wek⁽ʷ⁾speros ( “ evening ” ) .
2338: From Proto-West Germanic *westr , see also Old High German west , Old Norse vestr .
###
474: Old East Slavic оукраина ( ukraina ) der. 
479: Old East Slavic оукраина ( ukraina ) 
484: Borrowed from Polish Ukraina or Russian Украи́на ( Ukraína ) , from Old East Slavic оукраина ( ukraina ) , which is most commonly taken to have meant "borderland, marches " in this context, though for about a century now Ukrainian scholars have articulated an alternative theory that it meant "region, country, the land around (a given center)" in this context instead. See Name of Ukraine for more.
513: Since the country's independence in 1991, Ukraine without an article (as in “a musician from Ukraine”) has been the most common way to refer to the country [ 1 ] and is recommended by style guides. Previously, it was more common to refer to the Ukraine (as in “a musician from the Ukraine”), [ 2 ] [ 3 ] but this has become increasingly uncommon. One reason why Ukrainians suggest their country's English name should not be addressed as the Ukraine is due to the Ukraine making it sound like it was a part of Russia, promoting Russian irredentist views or supporting the 2022 Russian war against the country.
554: Ukrainian 
614: → Ukrainian: Юкре́йн ( Jukréjn ) 
804: Cyrillic: Украин ( Ukrain ) , Украйн ( Ukrajn ) 
825: Pannonian Rusyn: Україна   f ( Ukrajina ) 
875: Tajik: Украйина   (tg) ( Ukrayyina ) , Укроин ( Ukroyin ) 
898: Ukrainian: Украї́на   (uk)   f ( Ukrajína ) , Вкраї́на   f ( Vkrajína ) ( rare, poetic, after vowels ) 
930: Ukrainian SSR 
1027: From Ukrainian Украї́на ( Ukrajína ) or Russian Украи́на ( Ukraína ) , from Old East Slavic оукраина ( ukraina ) .
```


## [2026-09-05T05:32:32.686Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT west\"; grep -n \"^WEST\" SKT.txt | head -3; grep -n -A6 \"^WEST\\b\" SKT.txt | head -20; echo \"### KNT ava\"; grep -n \"ava-\\|'ava'\\|ava,\" KNT.txt | grep -n -i \"prefix\\|down\" | head -10"
}
```


### [2026-09-05T05:32:32.778Z] TOOL RESULT

```
### SKT west
### KNT ava
24:2379:(c) Double prefixes are perhaps found in two forms: pait-à- in patiydbaram DB 1.68, ava-à-in avajaniya DB 1.51, 52; but there are some dubi- ous features even about these, сї. JAOS 62.274-5.
32:2648:§244, Tue FUTURE PASSIVE PARTICIPLE IN -elo- is typified by Skt. yajatá-, Av. yazata- ‘worthy of worship’, to (Skt.) yaj- ‘worship’; but the forma- tion often comes to have virtually the force of a perfect passive in -/0-: cf. Skt. pacaid-, but Gk. merrós, Lt. coctus ‘cooked’. Cf. also СК, &-exeros ‘unchecked’, to éyw ‘I hold, have’. The OP ex- amples happen to be from intransitives, and are therefore active in meaning: nsn. dakatam, npn. Sakata ‘past’, to root ak- ‘pass’; and -gmata- ‘gone’ to gam- ‘go’, in npm. ha"-gmatd ‘assembled’, nsf. pará-gmalü ‘gone forth’, perhaps nsf. [ava- дтађа ‘gone down, fallen’, cf. Av. yomata- as well as the regular passive participle gata- (pIE *g*m- to-, also in Skt. gald-, Gk. -Baros, Lt. ventum).
48:4928:Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
49:5042:ava- + ar- ‘go down to, arrive at^: avd{rasam] Ist sg. imf. ($131) DB 5.23f; [ајратазат DSf 24.
52:5091:’ava- prefix ‘away, down’: GAv. avd, LAV. ava, Skt. dva; with verbs ar-, *kan-, gam-, jan-, à-jan-, !rad-, sta-, hard-. Cf. JAOS 62.274-5,
57:5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
60:5240:ava- + kan- ‘put down on, place on’: avakanam Ist sg. imf. (8213, 5226.1) DB 1.86.
62:5362:ava- + gam- ‘go down, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
63:5405:ava- + jan- and ava- + à + jan- ‘smite down, slay’ (apparently ava- in avajata, ара-й- in avàjan- iyà, others ambiguous; cf. §206c, JAOS 62.274): avàjanam 1st sg. imf. ($226.IT) DB 1.57, 59, 73, 83; 2.5; 481; 5.13, 27°. арфа" imf, ($228.IT) DB 1.31 bis; 3.75.  avàjana" За pl. imf. ($208, $232. П) DB 2.13. avájantyü opt. (§206c, $2281, §228.1I) DB 1.51, 52 (858, JAOS 62.274; hardly with Foy, KZ 35.34). avajata nsm. past pte. pass. (8122, §242.1) DB 1.32 (error for avdjata, ace. to Gray AJP 21.13, Bthl. AW 491).
68:5706:fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhill’). DSf 23f, 28.
```


## [2026-09-05T05:32:33.805Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"herab, weg von\\|au-, aue-\\|aue-, ue-\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T05:32:33.861Z] TOOL RESULT

```
1036:au- (aue?); ue- „herab, weg von — 
1379:au-, aue-, auei- — au-
```


## [2026-09-05T05:32:39.529Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '1030,1075p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T05:32:39.579Z] TOOL RESULT

```
aldeoiuai (*aideo-ojiiai) „al'6o/j.ai“ 2 ) ; tiefstufig ai. „verehre, preise, flehe an“. 

Bugge BB. 3, 116, Bezzenberger BB. 4, 313, Walde KZ. 34, 552, Solm- 
sen IF. 13, 137, Schulze Qu. ep. 210 f.; s. auch Yf. LEWb. 2 18, Boisacq 22, 
1088,368. 

au- (aue?); ue- „herab, weg von — 

Ai. dva „ab, herab“, meist Praefix vor Verben und Subst., selten Praep. 
m. Abl., av. ap. ava Praefix „herab“ und (indem mehr das Ziel, als der 
Ausgangspunkt der Bewegung zum Bewufitsein kam) „worauf zu, heran“ 
(z. B. avabar- „hinabbringen, wegtragen“ und „hinzubringen, verschaffen <: ). 
ebenso Praep. m. Akk. „hin-zu, hin-an“; davon ai. avara- „inferior“, und 
av. aord „nach unten, hinab“, adv. Instrumental eines *aora- ( : ai. avara- 
— lit. Jcatrds : ai. katard-h , Bartholomae Altiran. AVb. 43), av. avaro Adv. 
„hinab, herab“ = ai. avdr RY. I 133,7 (s. Bartholomae IF. 11, 1401’., Alt- 
iran. Wb. 176); ai. avdh ( avds ) „herab“, wovon avastad „unten“ oluie ausl. 
Yokal (vgl. av. ao-ra ) ai. o- z. B. in o-gana- „alleinstehend, erbiirmlich‘ ! 
(: gana-h „Schar“; Wackernagel Ai. Gr. I 54). 

Ar. ava ist an sich keine sichere Stiitze fur bereits idg. *auc x , da viel- 
leicht nach apa (= idg. *apo) aus *uu erweitert, tvelchenfalls ai. avara- 
jiingerer Priigung als av. aora- wiire. Doch vgl. unten *ue. 

') Stammhaft durch etrusk. aesar „Gott“ beeiufluCt, dessen Wz. item Ital. entlehut 
ist; umgekehrt lafit Bugge, Das Yerhilltnis der Etrusker zu den Indogernmnen 127, 
den ital. St. ais- aus dem Etruskischen kommen. 

2 ) Aber lat. aesiumo bleibt fern, da urspriinglich „den Wert einer Sache feststellen". 



14 


an- (aue?); ue- 


Gr. at- wohl in avyaxTEiv ' avaycogeTv, avaya^eodai Hes. (Schulze Qu. 
ep. 60) ; 

lat. an- „fort“ in aufero (=--= ai. ava-bharati , av. ava-bar-), aufugio; 

air. vielleicht o, ua „von, mit, durch“, als Praep. m. Dat. (z. B. Pick II 4 
22; vgl. bes. Thurneysen Hdb. I 475, aber auch die Zweifel ebenda II 99 f. 
und bei Pedersen KG. I 43S, 535 = Nachtr. zu S. 49, Sommer Miscellany
```


## [2026-09-05T05:32:48.394Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON اوباش\"; grep -n \"اوباش\" MON_part1.txt | head -5; echo \"### MON خرسند\"; grep -n \"خرسند\" MON_part1.txt | head -5; echo \"### ARY\"; grep -n \"اوباش\\|خرسند\\|افتادن\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T05:32:48.531Z] TOOL RESULT

```
### MON اوباش
7284:بی‌مفرد) گروه غوغا طلب؛ اوباش» مردم 
18669:اوبسردن» ق. اوباشتن] (مسص‌م.) (اوبارد؛ 
18677:صح.- «اوباش» گاهی در فارسی بجای مفرد 
18678:استعمال شود و جمع آن (اوباشان) آید. 
18680:(مص م.) (اوباشت» اوبارد» خواهد اوباشت» 
### MON خرسند
65875:خرسند فرق دارد ولی بعدا به معنی آن 
### ARY
80:علت از رونق افتادن واژه‌های «آریا» و «آرین» و (آریایی» چه بود؟
5698:چم این واژه در سانسکریت و لیترانی و لثرنی و یونانی : لرزیدن» به لرزه افتادن
```


## [2026-09-05T05:32:49.537Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"12\\.4[0-9] .*WEST\\|WEST$\\|EAST, WEST\" SYN.txt | head -8; echo \"### IEC\"; grep -n \"^wes-pero\\|^uespero\\|^wespero\" IEC.txt | head -5"
}
```


### [2026-09-05T05:32:51.134Z] TOOL RESULT

```
22241:870 12.45 HAST 12.46 WEST Grk. — dvarody, éws éoxépa, dvopal, dbots NG évarody Shots Lat. _oriéns occidéns, occdsus It. est, levante ovest, ponente Fr. est ouest Sp. este oeste, poniente Rum. est, rdsdrit vest, apus Ir. airther iarthar Nir. oirthear tarthar W. dwyrain gorllewin Br. reler, savheol kuzheol, kornaoueg Goth. urruns saggqs ON austr vesir Dan. gst vest Sw. Oster vdster OE éast west ME est west NE east west Du. oosten westen OHG dstan westan MHG  dsten west(en) NHG  osten westen Lith. rytai vakarat Lett. austrums, rili rielums, vakari ChSl.  vitstokiz zapadit SCr.  istok zapad Boh.  vgchod zdpad Pol. wschéd zachéd Russ. vostok zapad Skt.  purvd-(dig-), pratici-(dig-), praci-(di¢-) paccima-(di¢-) Av. upaosanhva-, daosatara- (adj.)
### IEC
```


## [2026-09-05T05:32:53.259Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22241,22270p' SYN.txt | head -40"
}
```


### [2026-09-05T05:32:53.310Z] TOOL RESULT

```
870 12.45 HAST 12.46 WEST Grk. — dvarody, éws éoxépa, dvopal, dbots NG évarody Shots Lat. _oriéns occidéns, occdsus It. est, levante ovest, ponente Fr. est ouest Sp. este oeste, poniente Rum. est, rdsdrit vest, apus Ir. airther iarthar Nir. oirthear tarthar W. dwyrain gorllewin Br. reler, savheol kuzheol, kornaoueg Goth. urruns saggqs ON austr vesir Dan. gst vest Sw. Oster vdster OE éast west ME est west NE east west Du. oosten westen OHG dstan westan MHG  dsten west(en) NHG  osten westen Lith. rytai vakarat Lett. austrums, rili rielums, vakari ChSl.  vitstokiz zapadit SCr.  istok zapad Boh.  vgchod zdpad Pol. wschéd zachéd Russ. vostok zapad Skt.  purvd-(dig-), pratici-(dig-), praci-(di¢-) paccima-(di¢-) Av. upaosanhva-, daosatara- (adj.)
uSastara- (adjs.)
The majority of words for the main points of the compass are based either on the position of the sun at a given time of day (‘sunrise, dawn, morning’ = ‘east’; ‘sunset, evening’ = ‘west’; ‘mid- day’ = ‘south’) or on one’s orientation, which among the TE-speaking peoples was usually facing the sunrise (‘in front’ = ‘east’; ‘behind’ = ‘west’; Tight? = ‘south’; ‘left? = ‘north’), though there are also traces of orientations toward the north or south (the latter in the Avesta, where ‘in front’ = ‘south’ 3 ‘be- hind’ = ‘north’). Cf. Schrader Reallex. 1.500 f.
A few are from names of characteristic winds, and among those for ‘north’ some are connected with the name of a con- stellation in the north, with ‘winter’, or
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a ————w
SELECTED INDO-EUROPEAN SYNONYMS
re 12.47 NORTH 12.48 SOUTH of Bopéas, Boppas véros, peonuBpla 3Y Boptas, Boppas véros, peonuBpla sk septentrid meridiés, auster : nord sud, mezzogiorno, mezzod ef nord sud, midi 'p0 norte sur, mediodia sto nord sud ltiascert descert , tuaisceart deisceart gogledd deheu, de mt hanternoz kreistetz i mW nordr sudr ‘be nord syd din nord, norr séder norp stip | north south wo north south for noorden zuiden nord, nordan sundan up nort, norden stiden, sunden aul norden stiden 10 Siauré, Ziemiai pieltis | ztemel't dienvidus séverit jugit At sjever jug (* sever, piilnoc jih ; péinoc poludnie ea sever jug 12. ultara-(di¢-), daksind-(dic-) ate udici(dig-) § apdaztara- (adj.) paurva-, rapi0witara- iit (adjs.) ; Ch with ‘midnight’ as opposite of ‘midday’ Uy = ‘south’. lar Notable is the spread of the English for words, first as nautical terms, to the ) Romance languages. a The attested Goth. words for ‘east’ ave and ‘west’ (Mt. 8.11; those for ‘north’ | and ‘south’ are not quotable) are not ‘rs general Gme. terms, but literal transla- on tions of the Grk. Cf. G. S. Lane, Phil. Quarterly 12.323 f. fr, But it may be noted that Luther used i the Gme. terms only for the winds, otherwise those for ‘morning’, ‘evening’, M etc., and that these or others had almost . replaced the old terms fora while. Paul, a Deutsches Wtb. 379. §
The words are listed in the sb. forms so far as possible. But some of the early
gpATIAL RELATIONS:
ple only as advs. Ga forms o OL gast, etc. (see NED or it ep Av. forms are adjs., and the 3) The adjs. with dig- ‘direction ; au “a point of the sky’ (: dig- ayes either expressed or under- ou
yota
or ‘east’ are connected or ‘dawn’ or ‘morning’, for’ ‘rise’, OF with words for Gn front’, all referring to the aon of the rising Sun.
oa +qus-, *Gusos-, *ysos-, etc., in ah for ‘dawn’ and ‘east’, beside verb forms a8 Skt. ucchatt, Av. usatt ‘lights up’ (esp. of the dawn), Lith. aust, Lett. ust ‘to dawn’. Walde-P. 1.26f. Er- nout-M. 93. Walde-H. 1.86.
Grk. Aeol. atws, Dor. aus, Hom. 7ws, Att, tos dawn’ and ‘east’; Lat. aurora (‘ausis-a) ‘dawn’ and (mostly poet.) fast’ (prob. also auster ‘south wind’, 1248); ON ausir, OF éast, OHG dstan, etc, general Gmc., with various suffixes; lith. ausra ‘dawn’, Lett. austrums ‘east’ ; ChSl. za ustra ‘in the morning’; Skt. yas, Av. usd ‘dawn’, whence Av. usas- eae (fr. *wpa-usah-) adjs.
9.45. Words f
ipefore’ OT
A Gtk. avarohy ‘a rising’, esp. pl. barohal miov ‘sunrise’, hence ‘east’ : a ‘rise’ (esp. of the sun).
e “a ed pres. pple. of oriri *. Hence ag |i g Sie literary terms, It., Sp. : ;
: Sea Sp. levante, Fr. levant), ion, Talse, lift?, refl. ‘rise’. REW
Ry, \ ine It., Rum. est), Sp. este fr. a Pe 2917a. Wartburg 3.247. bs ie tee lit. ‘(sun)rise’, fr. rdésdri, Si om es (of sun), epd. of raz- iktin 1209, ics Spring’ fr. Lat. salire.
* aD, ay ;
tther, NIy, oirthear, Br. reter,
CC-0. In Public Domain
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 871
fr. Ir. air-, Br. ar- ‘before’ (: Skt. pari ‘against, toward’, Grk. wept ‘around’, etc.), but also ‘east’ in advs. ¢-air ‘in the east’, s-air ‘to the east’, an-air ‘from the east’. Walde-P. 2.33. Pedersen 2.187. Ernault, Glossaire 572.
W. dwyrain, orig. ‘sunrise’, perh. fr. a epd. of the root in Ir. rigim ‘stretch out’, Lat. regere ‘direct, rule’, ete. Peder- sen 1.237, 2.56, 596 note 3.
Br. savheol, cpd. of sav ‘upright, raised’ and heol ‘sun’.
5. Goth. urruns (lit. translation of Grk. évarodn) : urrinnan ‘run out, go up, rise (of sun)’, ON renna, OE rinnan ‘run’, etc. Feist 528.
```


## [2026-09-05T05:32:54.072Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18665,18690p' MON_part1.txt; echo \"#### 7280\"; sed -n '7280,7290p' MON_part1.txt"
}
```


### [2026-09-05T05:32:54.155Z] TOOL RESULT

```
اوبار: (03۲)0۷۷.۰ 20 [ع.] ج. ونر. شوح‌هاء 
چرک‌ها. زواید پوست بدن از قبیل چرک و 
مو در انسان و پشم در حیوان. 
اوباردن: (-.120,)0۷-]03 2۷ [- اوباریدن ع 
اوبسردن» ق. اوباشتن] (مسص‌م.) (اوبارد؛ 
اوبارد» خواهد اوبارد؛ بیوباره اوبارنده؛ 
اوبارده) نا جویده فرو بردن» بلع کردن» 
بلعیدن. 
اوب_اش: (2۷028)0۷۰ [ع.] (.) ج. وش 
(مفرد» غم.) - بوش (غم.) فرومایگان؛ 
نا کسان» مردم پست» بی‌سر و پایان» سفلهة 
مردم. ولگردان. عامبان» بی ترستان. بی‌با کان. 
صح.- «اوباش» گاهی در فارسی بجای مفرد 
استعمال شود و جمع آن (اوباشان) آید. 
اوب‌اشتن: (-.0),جها-083 2۳ [- اوباردن] 
(مص م.) (اوباشت» اوبارد» خواهد اوباشت» 
بیوبار» اوبارنده» اوباشته). 
اوبه: (2۷0۵)۵ [تسر. - ابه] (.) چادر 
ترکمانان» خیمه‌ای که ترکمنان در زیر آن 
زندگانی کنند. 
اوت: 2 (.) هشتمین ماه سال فرنگی. 
اوتاد: ,۸۳۵۵ [ع.] (.) ج. وتد. 
میخ‌ها. (عر.) و تدهای عروضص و آنها سه‌اند: 
مقرون» مفروق» مجتمع. (تص.) پیشوایان 
بقت. (تص.) چهار تن از بزرگان که در 
چهار جهت دنیا باشند و به منزلهةٌ چهار رکن 
#### 7280
آنکه فرزند ندارد. بلاعقب» بی‌خلف. 
ها نازاه عقیم 

اج‌امر: ۳ 2 [ع.] (ا. جمعی است 
بی‌مفرد) گروه غوغا طلب؛ اوباش» مردم 


ولگرد. 


اجانب
```


## [2026-09-05T05:33:04.044Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ON vestr\\|OE west, etc\\|Gmc. \\*west\" SYN.txt | head -5; grep -n -m3 -B2 -A8 \"12.46. Words for\" SYN.txt | head -40"
}
```


### [2026-09-05T05:33:04.110Z] TOOL RESULT

```
22297:ON vestr, OF west, OHG westan, etc., general Gmc., prob. deriv. of a Gmc. *wes-: Skt. avas ‘down’ beside ava ‘down from’, and Grk. éomepos, etc. ‘evening’ (14.46). Walde-P.1.15. Falk- Torp 1371 f.
22274-8. Skt. pirva-(dig-) fr. adj. purva- ‘in front, former, eastern’ = Av. paorva- in front, former’, but ‘southern’ (see 12.48). OPers. paruva- ‘eastern’ (Barth. 871) is to be deleted. The correct read- ing is paradraya ‘beyond the sea’. Cf. Cameron, J. Near East. Stud. 2.307 fs
22275-Skt. pract-(dig-), fr. praiic- ‘directed forward, in front, facing, eastern’.
22276:12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
22277-1. Grk. éorépa ‘evening’ (14.36) and ‘west’.
22278-Grk. dvopy (esp. pl. dvepat), and dics, both lit. ‘the setting of the sun’ (sc. Mov) : btw ‘sink, go down, set’ (of the sun). Walde-P. 1.777 f.
22279-2. Lat. occidéns, pres. pple. of occidere ‘fall down, perish, set (of the sun)’, epd.
22280-. Gurukul Kangri Collection, Haridwar
22281-TT
22282-Rashes
22283-; { q 1] 4 | | ] ; }
22284-Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-05T05:33:19.122Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/оукраина\" --note \"page 69, Old Russian u-krai node\" ; python3 tools/fetch_source.py \"https://www.etymonline.com/word/Ukraine\" --note \"page 69, Ukraine etymology\"; ls site/pages/69.jpg 2>/dev/null; pdftoppm -f 69 -l 69 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg69 && echo rendered"
}
```


### [2026-09-05T05:33:24.614Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/051927f0990f56f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e066e6d17ee0017f.txt
site/pages/69.jpg
rendered
```


## [2026-09-05T05:33:27.241Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### oukraina\"; grep -n -i -A8 \"Etymology\" 051927f0990f56f9.txt | sed -n '1,60p' | tail -30; echo \"### etymonline\"; grep -n -i -A6 \"Ukraine\" e066e6d17ee0017f.txt | head -30"
}
```


### [2026-09-05T05:33:27.473Z] TOOL RESULT

```
### oukraina
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
141: Etymology
142- [ edit ] 
143-
144: Etymology tree
145-
146- Proto-Indo-European *h₂ew 
147- Proto-Balto-Slavic *au 
148- Proto-Slavic *u 
149- Proto-Slavic *u- 
150-
151- Proto-Indo-European *krey- 
152- Proto-Indo-European *kreh₁y- 
--
278: Pages with etymology trees 
279: Old East Slavic entries with etymology trees 
280- Pages using etymon with no ID 
281- Pages with entries 
282- Pages with 1 entry 
283-
284- This page was last edited on 26 August 2026, at 13:09.
285-
286- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
287-
### etymonline
1:URL: https://www.etymonline.com/word/Ukraine
2-FETCHED: 2026-09-05T05:33:23Z
3-STATUS: 200
4:TITLE: Ukraine - Etymology, Origin & Meaning
5-
6:Ukraine - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of Ukraine 
22-
23: Ukraine 
24-
25- by 1670s, from Russian or Polish Ukraina , a specific use of ukraina "border, frontier," according to Room, from Old Russian oukraina , from ou "by, at" + kraj region. He also notes that "The territory was so called because it was the borderland or 'frontier zone' of medieval Russia at the time of the Tatar invasion in the 13th century."
26-
27: Ukraine was formerly also known as 
28- Little Russia , so called by contrast with 
29- Great Russia , when the medieval principality here became separated from 'mainstream' czarist Russia as a result of the Mongol invasion. [Room, 2006] 
30-
31: Related: Ukrainian; Ukrainer .
32- also from 1670s 
33-
34- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
35-
36- More to explore
37-
```


## [2026-09-05T05:33:35.747Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg69.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.55))).save('pg69_top.png')\nEOF"
}
```


### [2026-09-05T05:33:38.221Z] TOOL RESULT

```
(1700, 2200)
```


## [2026-09-05T05:33:40.047Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg69_top.png"
}
```


### [2026-09-05T05:33:40.153Z] TOOL RESULT

```

```


## [2026-09-05T05:33:55.447Z] TOOL CALL #83: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T05:33:55.531Z] TOOL RESULT

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


## [2026-09-05T05:34:04.564Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"avapasti\\|ava.pasti\\|ava-pasti\\|paiti.pat\\|'pat-  V\" BRT.txt | head -8; echo \"### cheung pat\"; grep -n \"\\*pat ‘to fly\\|\\*pat \" CHEUNG.txt | head -5"
}
```


### [2026-09-05T05:34:04.832Z] TOOL RESULT

```
### cheung pat
18879:*pat ‘to cook’ 
18988:9 The formally and semantically similar roots *pad and *pat probably show mutual 
19683:*pat 299 
19739:*pat ‘to fly, rise; (?) fall’ 
19746:300 *pat
```


## [2026-09-05T05:34:07.128Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19739,19760p' CHEUNG.txt; echo \"...\"; sed -n '19790,19830p' CHEUNG.txt | grep -n -i \"NP \\|uftadan\\|oftadan\" "
}
```


### [2026-09-05T05:34:07.509Z] TOOL RESULT

```
*pat ‘to fly, rise; (?) fall’ 

*AVESTAN: Y Av. pat- ‘to fly’ || (+ *aua-) ‘to fall down, off’ || + *4-) ‘to come, rush 
to [daévic]’ || (+ *us-) ‘to come, go ош [daévic]’ || (+ *fra-) ‘to fly up; to enter 
[daévic]’ || (+ *ham-) ‘to fall, crash’ = Liste: 32f. 


300 *pat 


Pres. them.: IND. 3sg. YAv. frapataiti (Yt 8.61, V 18.54, V 18.65), YAv. ham.pataiti (V 19.41), 3pl. 
Y Av. patonti (Yt 10.128 ff., V 13.42 £), impf. 3sg. YAv. 4... apatat (Yt 19.41, Yt 19.82), INJ. 3sg. YAv. 
patat (Yt 3.13, F 475), YAv. auua.patat (Yt 19.58), YAv. us.patat (Yt 19.57, Yt 19.60, Yt 19.63), SUBJ. 
2sg. ? Y Av. “frapatäi (Yt 19.50), 3pl. YAv. frapatanti (Yt 14.53, Yt 8.61), YAv. fra patan (V 5.12), OPT. 
3pl. YAv. pataiion (Yt 19.80), YAv. apataiion (Y 9.15), IMPV. 3pl. YAv. patontu (Y 10.1); Partic: pres. 
Y Av. patant- (Yt 15.50); Caus.: pres. SUBJ. 1sg. YAv. uspataiieni (Yt 19.44) 


*OLD PERSIAN: (+ *uz-) udpat- ‘to rise up, rebel’ = Kent: 194 

MED.; Pres. them.: impf. IND. 3sg. udapatatä <u-d-p-t-t-a> (DB 1.36, DB 1.38, DB 2.10, etc.), 
<u-d-p-t-t-a> (DB 2.14), <u-d-p-t-[t]-[a]> (DB 1.78) 
...
20:postvocalic РІг. *p > b, v (= B]) compare ВМР npstn, MMP nbyst-/nbys-, NP 
23:*NWIR: (+ *aua-) NP öftadan/uft-, (Judeo-Pers.) ’wBst- ‘to fall (down); to happen,
```


## [2026-09-05T05:34:13.068Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19795,19825p' CHEUNG.txt"
}
```


### [2026-09-05T05:34:13.212Z] TOOL RESULT

```
*CHORESMIAN: (+ *aua-) wbd ‘to plunge into’, ? (LW) hwg- ‘to fall down; collapse’ 
|| (+ *para-) prpd- ‘to fall off || (+ *ni-) m/npd- ‘to fall down’, (caus.) m/np‘cy- ‘to 
tear down (of houses)’. ó The etymology of hwf- is uncertain. Samadi remarks that 
the forms are similar to Skt. subh- ‘to suffocate; to strike’ in appearance, whereas 
MacKenzie 1990: 112 cautiously suggests a connection with Oss. xawyn ‘to fall’. 
Both etymologies meet unsurmountable difficulties and are best to be discarded. 
Borrowing from (dial.) Persian seems to me the best solution to account for the 
Chor. forms: the initial h- may be considered "prothetic" or it may be identified as 
the (productive) preverb *fra-. For the Middle and New Persian development of 


*pau 301 


postvocalic РІг. *p > b, v (= B]) compare ВМР npstn, MMP nbyst-/nbys-, NP 
nibistan (rare), nivistan, nivés- (< *ni-p(a)is-). || Samadi: 211, 155, 130 

*NWIR: (+ *aua-) NP öftadan/uft-, (Judeo-Pers.) ’wBst- ‘to fall (down); to happen, 
vorfallen’, Bakht. vastan ‘to fall’, Sist. aft, aftid ‘to fall’, Isfah. oftän/ous-, Ham. 
dor-oftan/dor-ows- (inch.) ‘to sleep’, vor-osayán/vor-aws-, Isfah. ver-osän/ver-os- 
“to stand up’ 

*NEIR: (+ *uz-) Wa. z(a)bat-, z(o)bo0-/z(o)bon- ‘to snap (of boots)’ (= zübüt- ‘to 
burst, IFL II: 556) || (+ *ham-) Sh. ambi0- Rosh. ambé6-/Ambost, Sariq. 
imbis-/imbist, Yzgh. ambis-/ambust ‘to fall down, roll down, crumble’, Ishk. ambid- 
‘to fall down, be destroyed’, Wa. bə0-/bə0t, bot-/bon- ‘to fall; to throw off, down; to 
collapse (of wall)’ 

*MISC: (+ *ni-) Orm. nwastak ‘to lie down, go to sleep’ 

*SANSKRIT: pat ‘to fly, fall (down)’ (RV+) = EWAia П: 71
```


## [2026-09-05T05:34:26.687Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/اوباردن\" --note \"page 69, node 5 obârdan\" ; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ōpārtan\\|opartan\\|ʾwpʾl\\|obārtan\" NYB_vol2_glossary.txt UNV.txt | head -10"
}
```


### [2026-09-05T05:34:28.985Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/85e6c7af8f236bfe.txt
```


## [2026-09-05T05:34:32.244Z] TOOL CALL #88: Bash

```json
{
 "command": "head -30 /home/sfmqrb/git/rishe/data/verification/sources/web/85e6c7af8f236bfe.txt; echo \"###\"; grep -n -i \"etymology\" -A6 /home/sfmqrb/git/rishe/data/verification/sources/web/85e6c7af8f236bfe.txt | head -20; echo \"### NYB opar\"; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"opar\\|Opar\\|öpar\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T05:34:32.425Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/اوباردن
FETCHED: 2026-09-05T05:34:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found###
### NYB opar
```


## [2026-09-05T05:34:44.276Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^west, \" FSD_vol4.txt | head -3; grep -n \"AS. west\\|OHG. westan\" FSD_vol4.txt | head -5"
}
```


### [2026-09-05T05:34:44.395Z] TOOL RESULT

```
54963:west,  adv  1.  In  a   -westerly  direction  2.  Ecd  In  a direction  opposite  to  the  altar,  toward  the  nate  as  seen from  the  altar  —   wcst'*a-bout",  adr  Westwardij West,  Benjamin  (»Vnl"3S-*/ul820)  An  American  painter, chiefly  resident  in  London,  one  of  the  four  original  members and  second  president  of  the  Ho>al  Academy West  ,   adbr  Westminster
```


## [2026-09-05T05:34:46.841Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54950,54963p' FSD_vol4.txt | grep -n -i \"west\" | head; echo ---; sed -n '54955,54962p' FSD_vol4.txt"
}
```


### [2026-09-05T05:34:46.940Z] TOOL RESULT

```
5:no,  a   west  window  2.  Coming  from  the  west,  as,  the west  wind  3   Ecel  Opposite  the  high  altar  of  a   church —   T7est  End,  the  fashionable  part  of  London,  westward from  Charing  Cross  In  the  vicinity  of  St  James s   Fara Green  Park  and  Hyde  Park  with  the  definite  article  —   »> SyTlan  Church,  same  as  Jacodite  Church  Sre  under Jacobite  —   IF.  Syrfaa  liturgies,  the  Ssxiac  ilturslcs  See EiTtrnoT,  1   (1)
6:west*  ti  1   That  one  of  the  four  cardinal  points  ot  tne compass  which  is  exactly  opposite  tho  cast,  that  point where  the  sun  sets  at  the  equinoxes  in  common  pa^ Jance  including  the  part  of  tho  horizon  near  that  point 2   Any  region  in  the  western  part  of  a   country ,   or  to  t   w westward  of  another,  as,  tbe  west  of  England  Speaf (I)  [W-J  Same  as  Occident,  1   opposed  to  Orienf  (-)  ine-
10:K’estera  hemisphere  (3)  IW-3  ItT  SJ  Formerj>,  that  part of  the  countri”  west  of  the  Alleghanj  mountalna  still looselj  so  used  as  the  Queen  City  of  the  TTcrf  (Cincinnati) , now  usually,  the  region  beginning  with  the  prairies  and  ex- tending to  the  Pacific  or  to  the  Pacific  slope  of  the  Sierra Ne\ada3,  especially  the  northwestern  part  of  this  region, ciompare  just
12:3.  Eccl  (1)  In  a   church  building,  the  part  of  a   church opposite  "the  east  Compare  oriektation  (2)  pS'’-] Same  as  'Westera*  C^hurch  See  chubcb  {<  AS vest,  west.  <   V   tear  dwell  1   —   Empire  of  the  West,  same as  E5TER^  Empire  See  empire  —   w.  by  north,  vr  by sooth,  n. 'northwest,  w.  southwest,  see  illus  of  foists
14:west,  adv  1.  In  a   -westerly  direction  2.  Ecd  In  a direction  opposite  to  the  altar,  toward  the  nate  as  seen from  the  altar  —   wcst'*a-bout",  adr  Westwardij West,  Benjamin  (»Vnl"3S-*/ul820)  An  American  painter, chiefly  resident  in  London,  one  of  the  four  original  members and  second  president  of  the  Ho>al  Academy West  ,   adbr  Westminster
---
west*  ti  1   That  one  of  the  four  cardinal  points  ot  tne compass  which  is  exactly  opposite  tho  cast,  that  point where  the  sun  sets  at  the  equinoxes  in  common  pa^ Jance  including  the  part  of  tho  horizon  near  that  point 2   Any  region  in  the  western  part  of  a   country ,   or  to  t   w westward  of  another,  as,  tbe  west  of  England  Speaf (I)  [W-J  Same  as  Occident,  1   opposed  to  Orienf  (-)  ine-
2699
Key  1   aI^e;cra  =   oiit,oIl,  iii=feud;  <iliin,go,  jet;  rj^sing,  so;^p,  flun,  tiiis,  a3ure,  F   bon,dune;H=:loch  obsolete,  ^vananU  TVelsh
EEr2  book,  bdbt;  fall,  rnle,  cQre,  bfit,  bOrn; <iiI,boj ,   €   =   k;  c   =   s,  go,  irem,  ink;  s   =   z;  thin,  tins;  F.  bon,  dune;  h   =   IocIi.  Wet
K’estera  hemisphere  (3)  IW-3  ItT  SJ  Formerj>,  that  part of  the  countri”  west  of  the  Alleghanj  mountalna  still looselj  so  used  as  the  Queen  City  of  the  TTcrf  (Cincinnati) , now  usually,  the  region  beginning  with  the  prairies  and  ex- tending to  the  Pacific  or  to  the  Pacific  slope  of  the  Sierra Ne\ada3,  especially  the  northwestern  part  of  this  region, ciompare  just
Few  people  even  know  the  trne  definition  of  the  term  *   Wtat and  where  la  its  location‘s  pbantom-Uke  it  flies  before  us  as  we travel.  CxTioji  A*  Am  Indians  \o\  i.  p   62  la  c   B   1857  1
3.  Eccl  (1)  In  a   church  building,  the  part  of  a   church opposite  "the  east  Compare  oriektation  (2)  pS'’-] Same  as  'Westera*  C^hurch  See  chubcb  {<  AS vest,  west.  <   V   tear  dwell  1   —   Empire  of  the  West,  same as  E5TER^  Empire  See  empire  —   w.  by  north,  vr  by sooth,  n. 'northwest,  w.  southwest,  see  illus  of  foists
OP  THE  COMPASS  Under  poi>rr
```


## [2026-09-05T05:35:12.657Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqtv1_361.jpg \"https://archive.org/download/borhan-ghate-v1/page/n361.jpg\" -w \"%{http_code}\\n\" && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('bqtv1_361.jpg'); w,h=im.size; print(w,h)\nim.crop((0,0,w,int(h*0.10))).save('bqtv1_361_head.png')\nEOF"
}
```


### [2026-09-05T05:35:19.591Z] TOOL RESULT

```
200
2479 3508
```


## [2026-09-05T05:35:21.551Z] TOOL CALL #92: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv1_361_head.png"
}
```


### [2026-09-05T05:35:21.633Z] TOOL RESULT

```

```


## [2026-09-05T05:35:21.631Z] INPUT

[Image: original 2479x350, displayed at 2000x282. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-05T05:35:43.341Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqtv1_399.jpg \"https://archive.org/download/borhan-ghate-v1/page/n399.jpg\" -w \"%{http_code}\\n\" && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('bqtv1_399.jpg'); w,h=im.size\nim.crop((0,0,w,int(h*0.09))).save('bqtv1_399_head.png')\nim.crop((0,int(h*0.80),w,h)).save('bqtv1_399_foot.png')\nEOF"
}
```


### [2026-09-05T05:35:47.100Z] TOOL RESULT

```
200
```


## [2026-09-05T05:35:49.014Z] TOOL CALL #94: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv1_399_foot.png"
}
```


### [2026-09-05T05:35:49.274Z] TOOL RESULT

```

```


## [2026-09-05T05:35:49.271Z] INPUT

[Image: original 2479x702, displayed at 2000x566. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-05T05:35:58.565Z] TOOL CALL #95: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv1_399_head.png"
}
```


### [2026-09-05T05:35:58.633Z] TOOL RESULT

```

```


## [2026-09-05T05:35:58.631Z] INPUT

[Image: original 2479x315, displayed at 2000x254. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-05T05:36:01.912Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('bqtv1_399.jpg'); w,h=im.size\nim.crop((0,int(h*0.05),w,int(h*0.14))).save('bqtv1_399_head2.png')\nEOF"
}
```


### [2026-09-05T05:36:03.683Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:36:05.760Z] TOOL CALL #97: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv1_399_head2.png"
}
```


### [2026-09-05T05:36:05.840Z] TOOL RESULT

```

```


## [2026-09-05T05:36:05.838Z] INPUT

[Image: original 2479x316, displayed at 2000x255. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-05T05:36:18.676Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqtv1_398.jpg \"https://archive.org/download/borhan-ghate-v1/page/n398.jpg\" -w \"%{http_code}\\n\" && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('bqtv1_398.jpg'); w,h=im.size\nim.crop((0,int(h*0.78),w,int(h*0.97))).save('bqtv1_398_foot.png')\nEOF"
}
```


### [2026-09-05T05:36:24.072Z] TOOL RESULT

```
200
```


## [2026-09-05T05:36:25.868Z] TOOL CALL #99: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv1_398_foot.png"
}
```


### [2026-09-05T05:36:26.004Z] TOOL RESULT

```

```


## [2026-09-05T05:36:26.002Z] INPUT

[Image: original 2479x666, displayed at 2000x537. Multiply coordinates by 1.24 to map to original image.]


## [2026-09-05T05:37:17.880Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o hrn127.jpg \"https://archive.org/download/grundrissderneu00horngoog/page/n127.jpg\" -w \"%{http_code}\\n\" && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('hrn127.jpg'); w,h=im.size; print(w,h)\nim.crop((int(w*0.05),int(h*0.55),w,int(h*0.85))).save('hrn127_crop.png')\nEOF"
}
```


### [2026-09-05T05:37:22.701Z] TOOL RESULT

```
200
2956 4974
```


## [2026-09-05T05:37:24.757Z] TOOL CALL #101: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/hrn127_crop.png"
}
```


### [2026-09-05T05:37:25.016Z] TOOL RESULT

```

```


## [2026-09-05T05:37:25.013Z] INPUT

[Image: original 2809x1492, displayed at 2000x1062. Multiply coordinates by 1.40 to map to original image.]


## [2026-09-05T05:37:35.497Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o hrn126.jpg \"https://archive.org/download/grundrissderneu00horngoog/page/n126.jpg\" -w \"%{http_code}\\n\" && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('hrn126.jpg'); w,h=im.size; print(w,h)\nim.crop((int(w*0.05),int(h*0.60),w,int(h*0.95))).save('hrn126_crop.png')\nEOF"
}
```


### [2026-09-05T05:37:40.281Z] TOOL RESULT

```
200
2956 4974
```


## [2026-09-05T05:37:42.268Z] TOOL CALL #103: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/hrn126_crop.png"
}
```


### [2026-09-05T05:37:42.510Z] TOOL RESULT

```

```


## [2026-09-05T05:37:42.508Z] INPUT

[Image: original 2809x1741, displayed at 2000x1240. Multiply coordinates by 1.40 to map to original image.]


## [2026-09-05T05:38:38.366Z] TOOL CALL #104: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT 2>/dev/null | head"
}
```


### [2026-09-05T05:38:38.419Z] TOOL RESULT

```
ARY
BOOK
BQT
IRN
PLA
SNS
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
```


## [2026-09-05T05:38:43.931Z] TOOL CALL #105: Bash

```json
{
 "command": "set -e\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nO=/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr\nmkdir -p $O/HRN $O/BOOK $O/BQT\ncp $S/bqtv1_398.jpg $O/BQT/180.png\ncp $S/bqtv1_399.jpg $O/BQT/181.png\ncp $S/bqt733.jpg $O/BQT/733.png\ncp $S/hrn126.jpg $O/HRN/105.png\ncp $S/pg69.png $O/BOOK/69.png\nls -la $O/BQT/180.png $O/BQT/181.png $O/BQT/733.png $O/HRN/105.png $O/BOOK/69.png"
}
```


### [2026-09-05T05:38:45.743Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/69.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/180.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/181.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/733.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/HRN/105.png
```


## [2026-09-05T05:39:27.366Z] TOOL CALL #106: Bash

```json
{
 "command": "O=/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr\ncat > $O/BQT/180.vision.txt <<'EOF'\nBorhan-e Qate' ed. Mo'in, vol. 1, printed page 180 (archive.org borhan-ghate-v1 leaf n398;\nrunning head of the next leaf reads \"— ۱۸۱ —\", so this leaf is p.180).\nRead from the page image on 2026-09-05 (verification of PDF page 69, root \"Au 2, We 2\").\n\nEntry (main text, right column):\n  «او بار ۱۴ ـ بفتح اول بروزن افار، چیزی بگلو فروبرنده و بلع کننده را گویند … و هر جانوری که\n   جانور زنده را فرو برد گویند «اوبارید» … و امر بفروبردن و بیرون افکندن هم هست»\n\nMo'in's etymological footnote 14 at the foot of the page (verbatim):\n  «۱۴ـ پهلوی ôpâr از ایرانی باستان ava-pârayati مرکب از: ava پیشوند و جزو دوم مشتق از par\n   (پر کردن) «بارتولمه ۸۵۰». رک: انبار «نیبرگ ۱۶۵»؛ اوباردن و اوباریدن و اوباشتن و گواردن\n   وفلاردن (در «فیه مافیه» مولوی آمده) از این ریشه است.»\n\ni.e. Pahlavi ōpār, from Old Iranian ava-pārayati = prefix ava + a second element derived\nfrom par \"to fill\" (Bartholomae col. 850); cf. anbār (Nyberg 165); ōbārdan, ōbārīdan,\nōbāštan … belong to this root.\nEOF\ncat > $O/BQT/181.vision.txt <<'EOF'\nBorhan-e Qate' ed. Mo'in, vol. 1, printed page 181 (archive.org borhan-ghate-v1 leaf n399;\nrunning head \"— ۱۸۱ —\", catchword اوچیدن).\nRead from the page image on 2026-09-05 (verification of PDF page 69, root \"Au 2, We 2\").\n\nEntries on this page:\n  «اوباریدن ـ بفتح اول بروزن سرخاریدن؛ ناجاویده فرو بردن را گویند و بعربی بلع خوانند …»\n  «اوباش ـ بر وزن افراش، مردم عامی هیچ نافهمیده، بی‌سر و پا و جلف و بی‌خرد و متعصب را گویند ۹»\n  «اوباشتن ـ … پر کردن و افگندن باشد.»\n  «اوبرد ـ بضم اول بر وزن افترد؛ بمعنی ناجاویده فروبرد و بلع کرد.»\n\nMo'in's footnote 9 (to اوباش), verbatim:\n  «۹ ـ عربی، جمع وبش، مقلوب بوش. «محیط المحیط».»\n  = \"Arabic, plural of وبش, metathesis of بوش (Bustani, Muhit al-Muhit).\"\n\nFootnote at the very foot of the page:\n  «۵ اوباردی ـ رک: اوباردن. اوجاق ـ اجاق. ترکی؛ مطبخ، کانون ـ خانواده، قبیلهٔ بزرگ «جغتایی ۴۷».»\nEOF\ncat > $O/BQT/733.vision.txt <<'EOF'\nBorhan-e Qate' ed. Mo'in, vol. 2, printed page 733/734 (archive.org borhan-ghate-v2 leaf n191).\nRead from the page image on 2026-09-05 (verification of PDF page 69, root \"Au 2, We 2\").\n\nEntry: «خرسند ـ بضم اول بروزن گلقند، بمعنی شادمان و همیشه خوش و خوشنود باشد …»\n\nMo'in's etymological footnote 4 (verbatim, Latin forms as printed):\n  «۴ ـ پهلوی xorsand (قانع، راضی)؛ xôr+sand : xôr در ارمنی xor (کود) بمعنی کودی و ورطه،\n   * ôr، *avara ـ، از اوستا avarə (پایین) «بارتولمه ۱۷۶»، aorâ (بسوی پایین) «بارتولمه ۴۳»،\n   سانسکریت avara ـ (پایین، پست)؛ * sanda، از sand (پسندیده یافتن) «بارتولمه ۱۵۵۹»\n   رک: نیبرگ ۱۳۳ـ۴ و اسشق(؟) و هوبشمان ۴۷۸.»\n\ni.e. Mo'in analyses MP xorsand as xôr + sand, xôr < *ôr < *avara-, cf. Av. avarə \"downward\"\n(Bartholomae 176) and aorā \"downwards\" (Bartholomae 43), Skt. avara-; second element *sanda-\nfrom sand- \"to find pleasing\" (Bartholomae 1559); cf. Nyberg 133-4, Hübschmann 478.\nEOF\ncat > $O/HRN/105.vision.txt <<'EOF'\nP. Horn, Grundriss der neupersischen Etymologie (1893), printed page 105\n(archive.org grundrissderneu00horngoog leaf n126). Read from the page image on 2026-09-05\n(verification of PDF page 69, root \"Au 2, We 2\"; Nourai cites HRN:105 for \"avara-sad\").\n\nEntry 478 (verbatim):\n  «478. χursend 'fröhlich, zufrieden'.\n   aw. *hurasant-; phlv. χursand 'zufrieden, fröhlich' (Bund., Mēn.), χursandīh (AV.).\n   Darmesteter, Et. ir. I, 265; die pāz. Aussprache χʷarsand spricht allerdings gegen\n   diese Etymologie, doch kann sie nicht ausschlaggebend sein.»\n\nHorn therefore derives xursand from Avestan *hu-rasant- (hu- \"good\" + ras- \"arrive\"),\nNOT from ava-/avara- \"down\".\n\nAlso used, entry 92 on p.22 (leaf n43 of the same scan):\n  «92. uftāden 'fallen', Praes. uft-em, fitaden, uftādegī. ava- + √pat; phlv. ōftātan, ōftet …,\n   vergl. ōft(i)šn (Ys. 43,4, aw. avapasti-).»\nAnd entry 132 on p.31:\n  «132. ōbāšten 'anfüllen; verschlingen (d. i. sich anfüllen)'. Praes. ōbārem, ōbārīden;\n   ōbāš 'Gesindel' … ap. *ava + √par- (vergl. skr. avapūrṇa- 'anfüllen');\n   phlv. avpartan bezw. ōpārtan 'verschlingen' (Mēn., AV.).»\nEOF\nls $O/BQT $O/HRN"
}
```


### [2026-09-05T05:39:29.074Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT:
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1488.png
1488.txt
1803.png
1803.txt
180.png
180.vision.txt
181.png
181.vision.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
2143.png
2143.txt
2222.png
2222.txt
2246.png
2246.txt
2246.vision.txt
2407.png
2407.txt
31.vision.txt
58.vision.txt
70.vision.txt
72.vision.txt
733.png
733.vision.txt

/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/HRN:
105.png
105.vision.txt
```


## [2026-09-05T05:39:38.632Z] TOOL CALL #107: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ew\" --note \"page 69, root Au 2/We 2 = PIE *h2ew 'away, off'\"; tail -3 data/verification/sources/web/index.jsonl | cut -c1-200"
}
```


### [2026-09-05T05:39:40.986Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1b288f442872df6b.txt
{"url": "https://abadis.ir/fatofa/%D9%87%D9%88%D8%B4%D8%A8%D8%A7%D9%85/", "file": "data/verification/sources/web/ceaf725535fa7d45.txt", "fetched": "2026-09-05T05:33:42Z", "status": 200, "bytes": 2738,
{"url": "https://en.wiktionary.org/wiki/اوباردن", "file": "data/verification/sources/web/85e6c7af8f236bfe.txt", "fetched": "2026-09-05T05:34:28Z", "status": -1, "bytes": 39, "title": "", "note"
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ew", "file": "data/verification/sources/web/1b288f442872df6b.txt", "fetched": "2026-09-05T05:39:40Z", "status": 200, "byt
```


## [2026-09-05T05:39:44.176Z] TOOL CALL #108: Bash

```json
{
 "command": "grep -n -i -m1 -A25 \"Proto-Indo-European\" /home/sfmqrb/git/rishe/data/verification/sources/web/1b288f442872df6b.txt | sed -n '1,40p'; echo ...; grep -n -i \"Particle\\|Adverb\\|away\\|down\" /home/sfmqrb/git/rishe/data/verification/sources/web/1b288f442872df6b.txt | head -12"
}
```


### [2026-09-05T05:39:44.246Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ew
2-FETCHED: 2026-09-05T05:39:40Z
3-STATUS: 200
...
62: Adverb 
123: Download as PDF 
140: Adverb
145: away from, off 
152: Dunkel separates the material into *aw ( “ away, off ” ) [ 5 ] and *h₂u ( “ besides; and, also ” ) (with full grade *h₂éw ). [ 6 ] 
239: ^ Dunkel, George E. ( 2014 ), “*au̯ 'weg, fort, ab'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [1] (in German), volume 2: Lexikon, Heidelberg: Universitätsverlag Winter, →ISBN , pages 96-105 
241: ↑ 6.0 6.1 6.2 6.3 Dunkel, George E. ( 2014 ), “2.*-h₂o 'dabei, dazu; und; auch'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [2] (in German), volume 2: Lexikon, Heidelberg: Universitätsverlag Winter, →ISBN , pages 334-345 
249: ^ Dunkel, George E. ( 2014 ), “*au̯ó- 'jener'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [4] (in German), volume 2: Lexikon, Heidelberg: Universitätsverlag Winter, →ISBN , pages 111-113 
261: Proto-Indo-European adverbs
```


## [2026-09-05T05:39:46.573Z] TOOL CALL #109: Bash

```json
{
 "command": "sed -n '138,175p' /home/sfmqrb/git/rishe/data/verification/sources/web/1b288f442872df6b.txt"
}
```


### [2026-09-05T05:39:46.615Z] TOOL RESULT

```
 [ edit ] 

 Adverb
 [ edit ] 

 *h₂ew [ 1 ] [ 2 ] [ 3 ] [ 4 ] 

 away from, off 

 again 

 Reconstruction notes
 [ edit ] 

 Dunkel separates the material into *aw ( “ away, off ” ) [ 5 ] and *h₂u ( “ besides; and, also ” ) (with full grade *h₂éw ). [ 6 ] 

 Derived terms
 [ edit ] 

 *h₂ew-o [ 2 ] 
 Proto-Albanian: *awa- [ 7 ] 
 Albanian: v- 

 Proto-Indo-Iranian: *Háwa ( see there for further descendants )

 *h₂ew-ti [ 2 ] [ 6 ] 
 Proto-Hellenic: 
 Ancient Greek: αὖτις ( aûtis ) 

 Proto-Italic: *auti ( see there for further descendants )

 *h₂ew- tó- [ 1 ] 
 Proto-Hellenic: *autós ( “ self ” ) ( see there for further descendants )

 Phrygian: αυτος ( autos ) 

 *h₂ew-o-s [ 8 ] [ 9 ] [ 10 ] 
 Proto-Balto-Slavic: *awas
```


## [2026-09-05T05:39:56.887Z] TOOL CALL #110: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^au- \\|^au-,\\|^au \\\"\" IEC.txt | head -5; echo \"### wesper\"; grep -n -i \"wesper\\|uesper\" IEC.txt | head -5"
}
```


### [2026-09-05T05:39:56.946Z] TOOL RESULT

```
791:au- (onomat. particle) (1) Skt. cf. au! beside auh noise"); Gk. cf. aúð; Latv. cf. aura ‘howl’ and passim as an inter- jection
792:au-, au- (2) “away”. Cf. aue. WP I, 13 Skt. cf. ava-, px.; Hitt. cf. awan “apart, off; Arm. aw- in aw-ctem ('detach', fr. *au-sKid-); Gk. a- in some cpds. (amélgo); Olr. ó, úa “from is ambig., cf. apo; ON au- (FH); OCS u- (in u-bero “take away”, u-bogü ‘poor’, etc.). (The px. au- in Lat. auferð and au-fugio is best regarded as a conditioned variant of ab-. Thus also Ainsworth and traditional etymology generally). For Gk. aü, see aut.
853:au- (1), see aue
854:au- (2) (same as (1)?) “refuse, chaff, oats’ Lat. cf. avena; OCS ovísü “oats'; ovinü 'gran- ary’; jevinü ‘stubble’; R ovin, id.; Li. avižos *oats'; Latv. auzas, id.
### wesper
```


## [2026-09-05T05:45:59.457Z] TOOL CALL #111: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-69.json",
 "content": "{\n  \"pdf_page\": 69,\n  \"book_page\": 39,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Au 2, We 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂ew (older notation *au-, *au̯e-, beside *u̯e-) 'away, off, down' — Pokorny 72 f. (3. au- (au̯e-), u̯e- 'herab, weg von')\",\n      \"note\": \"The root box is right on all three counts. Pokorny IEW p.72 has exactly '3. au- (au̯e-), u̯e- \\\"herab, weg von —\\\"', i.e. the two shapes Nourai prints as 'Au 2, We 2', with the gloss 'down, away from' that his 'away, off, down' renders; Walde-Pokorny I 13 f. (the source Pokorny condenses) heads the same article 'au- (au̯e?); u̯e- \\\"herab, weg von\\\"'. Watkins/AHD lists it as 'au-³, Off, away. [Pok. 3. au- 72]', Mann IEC 791 as 'au-, au̯- (2) \\\"away\\\", WP I,13'. Modern notation writes the particle *h₂ew 'away from, off' (Wiktionary, after Dunkel LIPP II 96-105 *au̯ 'weg, fort, ab'), with Proto-Indo-Iranian *Háwa and Proto-Balto-Slavic *au continuing it; the laryngeal is the only difference from Nourai's 1959-vintage shape. The label 'Indo-European' is correct. One caveat that runs through the chart: Pokorny himself is careful that *u̯e- is only 'wohl unter *au̯e- zu vereinigen' ('probably to be united with au̯e-'), so the West/vesper branch (nodes #8-#10) hangs on a probability, not a certainty.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی (ص ۷۲) دقیقاً همین ریشه را با دو گونهٔ au- (au̯e-) و u̯e- به معنای «به پایین، دور از» آورده است و همان دو صورتی است که نورایی با نام‌های «Au 2, We 2» ثبت کرده؛ والده-پوکورنی (جلد ۱، ص ۱۳ـ۱۴) و واتکینز در پیوست فرهنگ American Heritage («au-³ off, away») و مان نیز همین را دارند. در نگارش امروزی این ذره را *h₂ew «دور، کنار» می‌نویسند (ویکی‌واژه به پیروی از دونکل) و هندوایرانی آغازین *Háwa و بالتواسلاوی آغازین *au دنبالهٔ آن‌اند؛ تنها تفاوت با صورت نورایی افزودن حنجره‌ای h₂ است. برچسب زبانی «هندواروپایی» و معنای «دور، پایین» درست است. یک نکتهٔ احتیاطی: خودِ پوکورنی پیوند گونهٔ u̯e- را با au̯e- «محتمل» می‌داند نه قطعی، و شاخهٔ «باختر/وسپر» (گره‌های ۸ تا ۱۰) بر همین احتمال استوار است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ew\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:72\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01 leaf 81 (printed p.72): '3. au- (au̯e-), u̯e- \\\"herab, weg von —\\\". Ai. áva \\\"ab, herab\\\", meist Präfix …, av. ap. ava Präfix \\\"herab\\\" … davon ai. ávara- \\\"inferior\\\" und av. aorā \\\"nach unten, hinab\\\" …'. Exactly the root box and node #1. The article continues on p.73 with 'aksl. u Präfix \\\"weg, ab\\\"' (node #6) and 'ai. avás \\\"herab\\\" … germ. wes- in nhd. West' (nodes #8-#10).\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I pp. 13-14\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd1 line 1036: 'au- (aue?); ue- \\\"herab, weg von —\\\". Ai. áva \\\"ab, herab\\\" … av. ap. ava Praefix \\\"herab\\\" … av. aorā \\\"nach unten, hinab\\\", adv. Instrumental eines *aora- (: ai. avara-, Bartholomae Altiran. Wb. 43), av. avarə Adv. \\\"hinab, herab\\\" = ai. avár (Altiran. Wb. 176)'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, root list s.v. au-³\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985 line 304: 'au-³, Off, away. 1. Old Russian u-, away … 2. Sanskrit ava, off, down: AVATAR. [Pok. 3. au- 72.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. au-, au̯- (2)\",\n          \"stance\": \"supports\",\n          \"note\": \"IEC line 792: 'au-, au̯- (2) \\\"away\\\". Cf. au̯e. WP I, 13. Skt. cf. ava-, px.; Hitt. awan \\\"apart, off\\\"; … OCS u- (in u-bero \\\"take away\\\")'.\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"1966 ed. pp. 132-133, s.v. avatar\",\n          \"stance\": \"supports\",\n          \"note\": \"'OI. avatāraḥ … fr. ava, \\\"down\\\" … rel. to OI. avaḥ, \\\"down, downward\\\", Avestic ava, \\\"down\\\", and cogn. with Gk. au-, L. au-, \\\"away\\\" (in auferre), Lith., Lett., OPruss. priv. pref. au-, OSlav. u … cp. the first element in vesania and in vesper.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ava 1, aorâ; avara\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three forms are real and correctly labelled. Av./OP ava- is the inherited preverb and preposition 'down, off' (< PIE *h₂ew), still a living prefix in Old Persian (Kent, Old Persian, lexicon: '*ava- prefix \\\"away, down\\\": GAv. avā, LAv. ava, Skt. áva; with verbs ar-, kan-, gam-, jan-, rad-, sta-, hard-'), e.g. OP ava-jan- 'smite down', ava-kan- 'put down'. aorā is the Younger-Avestan adverb 'downwards' (Bartholomae AiWb col. 43-44: 'j., g. aorā Adv. \\\"nach unten, hinunter, hinab\\\"'), formally the instrumental singular of an adjective *aora- which is the comparative of *ava-, i.e. the same stem as Skt. ávara- 'lower'; its Old Persian counterpart is aura in Auramazdā-context (Kent, s.v. Aura, 'downward, isn. of aura-, zero-grade of avara-, comparative of *ava-, cf. Av. aora \\\"down\\\"'). avara is Avestan avarə 'down, downwards' (AiWb col. 176) = Skt. avár (RV I 133,7), beside the adjective avara- 'lower, inferior'. The only imprecision is the merged language label: ava is both Avestan and Old Persian, aorā is Avestan (OP has aura), and avara-/avarə is Avestan and Sanskrit — the chart's 'Avestan / Old Persian' box collapses that distribution.\",\n          \"derivation_fa\": \"هر سه صورت اصیل و درست‌اند. ava- پیشوند و حرف اضافهٔ ارثی اوستایی و پارسی باستان به معنای «به پایین، دور» است (از *h₂ew هندواروپایی آغازین) و در پارسی باستان پیشوندی زنده است؛ کنت در واژه‌نامهٔ پارسی باستان می‌نویسد «*ava- پیشوند «دور، پایین»: اوستایی گاهانی avā، اوستایی متأخر ava، سنسکریت áva»، مانند ava-jan- «فروکوفتن» و ava-kan- «فرو نهادن». aorâ قید اوستایی متأخر به معنای «به سوی پایین» است (بارتولمه، ستون ۴۳ـ۴۴: «aorā Adv. nach unten, hinunter, hinab») و از نظر ساخت، بایِ ابزاری صفتی *aora- است که خودْ صورت برترِ *ava- شمرده می‌شود، هم‌ریشه با ávara- سنسکریت «فروتر»؛ همتای پارسی باستانش aura است. avara همان avarə اوستایی «به پایین» (بارتولمه ستون ۱۷۶) و برابر avár ودایی است. تنها بی‌دقتی نورایی در برچسب زبانی یکجاست: ava اوستایی و پارسی باستان است، aorâ اوستایی است و avara اوستایی و سنسکریت؛ نمودار این تفاوت‌ها را در یک جعبه ادغام کرده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ew\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:132\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 leaf 82 = printed pp.132-133, entry 'avatar' (it begins on p.132 and runs over to p.133): 'OI. avatāraḥ, \\\"descent\\\", fr. ava, \\\"down\\\" … The first element is rel. to OI. avaḥ, \\\"down, downward\\\", Avestic ava, \\\"down\\\"'. Exactly Nourai's ava/avara box.\"\n            },\n            {\n              \"ref\": \"POK:72\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p.72 (POK_01 leaf 81): 'av. ap. ava Präfix \\\"herab\\\" … av. aorā \\\"nach unten, hinab\\\" (nach parā aus avā erweitert), av. avarə Adv. \\\"hinab, herab\\\" = ai. avár RV. I 133,7'. All three of Nourai's words, with his glosses.\"\n            },\n            {\n              \"ref\": \"HID:209\",\n              \"status\": \"partial\",\n              \"note\": \"Bartholomae, Handbuch der altiranischen Dialekte: p.209 (HID leaf 222) is the first page of the Glossar (its preliminary remarks); the entry itself stands on the next page, p.210 (leaf 223): 'ava] Verb.-Praef.; = i. áva, z. ava.' So the citation is one page short of the entry, but it does point at the right glossary; the Handbuch has no aorā/avarə entry (it glosses only the Old Persian texts).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 43-44 and 176\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT leaf 61 (col. 43-44): 'j., g. aorā Adv. \\\"nach unten, hinunter, hinab\\\" … IS. aus *aora- Adj., Kompar. aus *ava. — ai. ávara-'. Col. 176 (leaf 130) is the avarata-/avarə region. These are the two columns Mo'in cites in his Borhān footnote to خرسند.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, lexicon s.v. ava-, Aura\",\n              \"stance\": \"supports\",\n              \"note\": \"KNT line 5091: '*ava- prefix \\\"away, down\\\": GAv. avā, LAv. ava, Skt. áva; with verbs ar-, *kan-, gam-, jan-, ā-jan-, rad-, sta-, hard-'; line 4928 s.v. Aura: '\\\"downward\\\", isn. of aura-, zero-grade of avara-, comparative of *ava-, cf. Av. aora \\\"down\\\"'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.13\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. aorā \\\"nach unten, hinab\\\", adv. Instrumental eines *aora- (: ai. avara-, Bartholomae Altiran. Wb. 43), av. avarə Adv. \\\"hinab, herab\\\" = ai. avár (… Altiran. Wb. 176)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"ava-pat; avara-sad\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The two words fare very differently. (a) ava-pat- 'to fall down' is genuine Avestan and exactly as drawn: Cheung, Etymological Dictionary of the Iranian Verb, s.v. *pat 'to fly, rise; (?) fall', lists Av. pat- with '(+ *aua-) \\\"to fall down, off\\\"' and cites YAv. auua.patat (Yt 19.58); the verbal noun avapasti- 'falling down' is attested (Horn quotes it from Yasna 43,4 Pahlavi glosses). Nourai's cross-reference ☞Pet 1 (PIE *peth₂- 'to fly, fall') is correct. (b) avara-sad 'settle down, satisfy' is not an attested Avestan compound, and both of its members are questionable. Nourai is following Mo'in's footnote in Borhān-e Qāṭeʿ p.733, which analyses MP xorsand as xôr + sand with xôr < *ôr < *avara- (citing Bartholomae 176 avarə, 43 aorā) and *sanda- from sand- 'to find pleasing' (Bartholomae 1559). But modern Iranian studies derive the word from Middle Persian hunsand 'happy, contented' — hu- 'good' + sand — so the first element is *hu-, not *ava-ra- (MacKenzie, Concise Pahlavi Dictionary p.45 'hunsand [hwnsnd | = P, (N xursand)] happy, contented'; Wiktionary follows MacKenzie). Horn, the other reference Nourai cites here, gives yet a third analysis, Av. *hu-rasant- (p.105), and warns that the Pāzand pronunciation xʷarsand tells against it. Even on Mo'in's own reading the second member is sand- 'to seem, please' (Proto-Iranian *sand, PIE *(s)ḱend-, cf. Latin cēnseō, NP pasandīdan), not *sed- 'to sit': Nourai's cross-reference ☞Sed is therefore wrong, and his gloss 'settle down' follows from that wrong identification.\",\n          \"derivation_fa\": \"سرنوشت دو واژهٔ این گره یکسان نیست. (الف) ava-pat- «فروافتادن» اوستایی اصیل و درست است: چونگ در فرهنگ ریشه‌شناختی فعل ایرانی ذیل *pat «پریدن، افتادن» صورت اوستایی pat- را با پیشوند *aua- به معنای «فروافتادن» می‌آورد و شاهد auua.patat (یشت ۱۹:۵۸) را نقل می‌کند؛ اسم مصدر avapasti- نیز گواه است. ارجاع نورایی به ریشهٔ Pet 1 (هندواروپایی *peth₂-) درست است. (ب) اما avara-sad «فرونشستن، خرسند شدن» ترکیبی اوستایی گواهی‌شده نیست و هر دو جزء آن جای چون‌وچرا دارد. نورایی در اینجا پیرو حاشیهٔ معین بر برهان قاطع (ص ۷۳۳) است که خرسند را xôr + sand می‌داند و xôr را از *ôr و آن را از *avara- (با ارجاع به بارتولمه ۱۷۶ و ۴۳) می‌گیرد. ولی ایران‌شناسی امروز این واژه را از فارسی میانهٔ hunsand «خشنود» می‌داند، یعنی از پیشوند hu- «خوب» + sand، نه از ava-ra- (مکنزی، فرهنگ کوچک پهلوی، ص ۴۵؛ ویکی‌واژه نیز از او پیروی می‌کند). هرن هم — که خودِ نورایی به او ارجاع داده — در ص ۱۰۵ صورت اوستایی *hu-rasant- را پیشنهاد می‌کند. افزون بر این، حتی بنا بر خوانش معین، جزء دوم sand- «پسندیده نمودن» است (ایرانی آغازین *sand، هندواروپایی *(s)ḱend-، هم‌ریشه با پسندیدن) نه sad- «نشستن»؛ پس ارجاع نورایی به ریشهٔ Sed نادرست است و معنای «فرونشستن» هم از همان اشتباه زاده شده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/خرسند\",\n            \"https://en.wiktionary.org/wiki/افتادن\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:132\",\n              \"status\": \"partial\",\n              \"note\": \"Klein pp.132-133 (s.v. avatar) documents Avestic ava 'down' but says nothing about ava-pat- or about xursand; it can support only the preverb, not this node's compounds.\"\n            },\n            {\n              \"ref\": \"HRN:105\",\n              \"status\": \"contradicts\",\n              \"note\": \"Horn, Grundriss p.105 no.478, read from the page image (saved as refs/ocr/HRN/105.png, transcript 105.vision.txt): 'χursend \\\"fröhlich, zufrieden\\\". aw. *hurasant-; phlv. χursand … Darmesteter, Et. ir. I, 265; die pāz. Aussprache χʷarsand spricht allerdings gegen diese Etymologie'. Horn's first element is hu- 'good', not ava-/avara-.\"\n            },\n            {\n              \"ref\": \"BQT:733\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ ed. Mo'in vol. 2 p.733/734 (archive borhan-ghate-v2 leaf n191; image saved as refs/ocr/BQT/733.png, transcript 733.vision.txt), footnote 4 to خرسند: 'پهلوی xorsand … xôr+sand … *ôr، *avara ـ، از اوستا avarə (پایین) «بارتولمه ۱۷۶»، aorâ (بسوی پایین) «بارتولمه ۴۳» … *sanda، از sand (پسندیده یافتن) «بارتولمه ۱۵۵۹»'. This is precisely Nourai's avara-sad, so he reports his source faithfully — but the source is Mo'in's 1963 analysis, not today's consensus.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pat and *sand\",\n              \"stance\": \"partial\",\n              \"note\": \"*pat 'to fly, rise; (?) fall': 'YAv. pat- … (+ *aua-) \\\"to fall down, off\\\"', INJ. 3sg. YAv. auua.patat (Yt 19.58) — supports ava-pat. *sand 'to appear, seem (good)': Av. sand-, OP θad-, MP (+ *pati-) passand-, PIE *(s)ḱend- — the second element of xursand is this root, not *sed-.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p.45 s.v. hunsand\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~īh: happiness, content.' The Pahlavi word is hu-nsand, and MacKenzie equates NP xursand with it; no ava- anywhere.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1559 (sand-), cols. 43/176 (aorā/avarə)\",\n              \"stance\": \"partial\",\n              \"note\": \"Bartholomae has both members separately — aorā col.43, avarə col.176, sand- 'scheinen, dünken' col.1559 (the columns Mo'in cites) — but no compound *avara-sand-; the compound is a reconstruction, not an Avestan attestation.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"oftâdan «افتادن»; xorsand «خرسند»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"oftādan is impeccable: Old Iranian *ava-pat- gave Middle Persian ōbastan/ōftādan (MacKenzie: 'ōbastan, ōbad- [ʾwpstn', ʾwpt-] fall' and 'ōftādan, ōft- [ʾwpt- | M ʾwptʾd, N uft-] fall'), whence NP اوفتادن/افتادن with the regular loss of the initial ō- in unstressed position (Horn still quotes ōftāden from Vīs u Rāmīn and the Šāhnāma); the present stem uft-/oft- continues *pata-. Wiktionary: 'From Middle Persian ʾwpt- (ōft-) \\\"fall\\\", from Proto-Iranian *ava- + *pat-'; Cheung lists NP ōftādan/uft- under *pat + *aua-. xorsand, by contrast, does not come from the node above it on any modern account: Middle Persian is hunsand (hu- 'good' + sand 'seeming, pleasing'), so NP خرسند is 'well-pleased', a formation of exactly the type of پسند/پسندیدن (*pati-sand-), and the xu-/xo- of the New Persian form is the regular reflex of Middle Persian hu- (cf. husraw > خسرو). Nourai's ava-ra- first element is Mo'in's older etymology (Borhān p.733) and is rejected by MacKenzie and Wiktionary; Horn (p.105), whom Nourai also cites, proposed *hu-rasant-, which agrees with the modern account at least in taking hu- as the first member. The Persian spellings افتادن and خرسند in the chart are correct.\",\n          \"derivation_fa\": \"«افتادن» بی‌عیب است: ایرانی باستان *ava-pat- در فارسی میانه ōbastan / ōftādan شده است (مکنزی: «ōftādan, ōft- [ʾwpt-] افتادن») و از آن فارسی نو «اوفتادن ← افتادن» با افتادن ō- آغازی در جایگاه بی‌تکیه پدید آمده؛ هرن هنوز صورت ōftāden را از ویس و رامین و شاهنامه نقل می‌کند و ستاک حال uft-/oft- دنبالهٔ *pata- است. ویکی‌واژه نیز همین را می‌گوید: «از فارسی میانهٔ ōft- از ایرانی آغازین *ava- + *pat-». اما «خرسند» بنا بر هیچ‌یک از پژوهش‌های امروزی از گرهِ بالای خود نمی‌آید: صورت فارسی میانه hunsand است، یعنی hu- «خوب» + sand «پسندیده نمودن»، و «خرسند» درست از همان گونهٔ ساختمانیِ «پسند/پسندیدن» (*pati-sand-) است؛ خِ فارسی نو نیز دنبالهٔ قاعده‌مند hu- فارسی میانه است (مانند husraw ← خسرو). جزء نخستِ ava-ra- در نمودار نورایی ریشه‌شناسی قدیم‌ترِ معین (حاشیهٔ برهان، ص ۷۳۳) است که مکنزی و ویکی‌واژه آن را نمی‌پذیرند؛ هرن هم (ص ۱۰۵) *hu-rasant- را پیشنهاد کرده که دست‌کم در جزء نخست با دیدگاه امروزی هم‌داستان است. املای فارسی «افتادن» و «خرسند» در نمودار درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/افتادن\",\n            \"https://en.wiktionary.org/wiki/خرسند\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:22\",\n              \"status\": \"supports\",\n              \"note\": \"Horn p.22 (HRN leaf 44) no.92: 'uftāden \\\"fallen\\\", Praes. uft-em, fitaden, uftādegī … ava- + √pat; phlv. ōftātan, ōftet …, vergl. ōft(i)šn (Ys. 43,4, aw. avapasti-)'. Exactly the arrow drawn (for oftādan).\"\n            },\n            {\n              \"ref\": \"BQT:145\",\n              \"status\": \"partial\",\n              \"note\": \"Borhān vol. 1 p.145 (archive borhan-ghate-v1 leaf n361; the running head reads '— ۱۴۵ —' and the catchword افتدستا, so the page number is confirmed from the image) carries the headwords افتاد 'fell', افتادگان, افتاده — the right page for oftādan, but Mo'in adds no etymological footnote there.\"\n            },\n            {\n              \"ref\": \"BQT:180\",\n              \"status\": \"not_found\",\n              \"note\": \"Borhān vol. 1 p.180 (leaf n398) is the اوبار page — the page Nourai correctly cites for node #4/#5 — and has nothing on افتادن or خرسند; خرسند is at p.733 (cited on node #2). The '180' in this box looks like a carry-over from the box below.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie pp.60, 45\",\n              \"stance\": \"partial\",\n              \"note\": \"'ōbastan, ōbad- [… ʾwpstn', ʾwpt- (if not ōft-, q.v.) | M ʾwbyst, J ʾwβst-] fall' and 'ōftādan, ōft- [ʾwpt- | M ʾwptʾd, N uft-] fall' support oftādan; 'hunsand … (N xursand)' contradicts the xorsand arrow.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pat, NWIr section\",\n              \"stance\": \"supports\",\n              \"note\": \"'*NWIR: (+ *aua-) NP ōftādan/uft-, (Judeo-Pers.) ʾwβst- \\\"to fall (down); to happen\\\"' — the Persian verb is filed exactly under *ava- + *pat.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 1 p.145; vol. 2 p.733\",\n              \"stance\": \"partial\",\n              \"note\": \"Borhān has افتاد without an etymology (p.145) and خرسند with Mo'in's *avara-sanda footnote (p.733), i.e. it backs Nourai only for the disputed half.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"ava-par\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both members are real, but the compound is a reconstruction, not an attested Avestan verb, and the label 'Avestan' is therefore too strong. Avestan par-/pərə- 'to fill' is well attested (Bartholomae col. 850, the column Mo'in cites; Cheung s.v. *parH¹ 'to fill; to nourish', with OAv. imperative pərənā, PIE *pelh₁-, whence also Skt. pṛṇāti, pūrṇa-), so Nourai's cross-reference ☞Pel 1 is right, and his rendering 'fill down' is a literal calque of Horn's 'anfüllen'. The compound itself comes from Horn no.132, who writes 'ap. *ava + √par- (vergl. skr. ava-pūrṇa- \\\"anfüllen\\\")' — i.e. an Old Iranian, asterisked form — and from Mo'in, who at Borhān p.180 posits Old Iranian *ava-pārayati with 'the second element derived from par (to fill), Bartholomae 850'. Cheung, who reconstructs the Iranian verbal roots exhaustively, registers no *aua- compound of *parH¹ at all, and MacKenzie's Pahlavi ōbārdan [ʾwpʾl-tn'] would formally also fit *ava-bar- 'to carry down' (Cheung's *bar has Av. '(+ *aua-) to bring down'). Since Middle Persian lenites postvocalic *p to b (Cheung, s.v. *pat: 'for the Middle and New Persian development of postvocalic PIr. *p > b, v compare BMP npstn, NP nivištan < *ni-paiš-'), the b of MP ʾwbʾrd cannot decide between par- and bar-, and the meaning 'to swallow' = 'to fill oneself' favours par-. Hence: plausible, on the authority of Horn, Hübschmann and Mo'in, but with the compound unattested and a live rival in *ava-bar-.\",\n          \"derivation_fa\": \"هر دو جزء این ترکیب واقعی‌اند، ولی خودِ ترکیب صورتی بازسازی‌شده است نه فعلی گواهی‌شده در اوستا، و از این رو برچسب «اوستایی» گزافه است. ریشهٔ اوستایی par-/pərə- «پر کردن» به‌خوبی گواهی شده است (بارتولمه ستون ۸۵۰ — همان ستونی که معین به آن ارجاع می‌دهد؛ چونگ ذیل *parH¹ «پر کردن، پروردن»، از هندواروپایی *pelh₁-، هم‌ریشه با pṛṇāti و pūrṇa- سنسکریت)، پس ارجاع نورایی به ریشهٔ Pel 1 درست است و ترجمهٔ «fill down» گرته‌ای است از «anfüllen» هرن. خودِ ترکیب از هرن (شمارهٔ ۱۳۲) می‌آید که می‌نویسد «*ava + √par- (سنجیده شود با ava-pūrṇa- سنسکریت)» — یعنی صورتی ستاره‌دار از ایرانی باستان — و از معین که در حاشیهٔ برهان (ص ۱۸۰) صورت ایرانی باستان *ava-pārayati را با «جزو دوم مشتق از par (پر کردن)، بارتولمه ۸۵۰» می‌آورد. چونگ که ریشه‌های فعلی ایرانی را یک‌به‌یک بازسازی کرده، هیچ ترکیبِ *aua- با *parH¹ ثبت نکرده، و صورت پهلویِ مکنزی ōbārdan از نظر صوری با *ava-bar- «فروبردن، پایین آوردن» هم می‌سازد. اما چون در فارسی میانه پِ ایرانی باستان در میان دو واکه به ب نرم می‌شود (چونگ: nivištan از *ni-paiš-)، حرف ب در ʾwbʾrd نمی‌تواند میان par- و bar- داوری کند و معنای «بلعیدن = خود را پر کردن» جانب par- را می‌گیرد. پس: با احتیاط پذیرفتنی است، به پشتوانهٔ هرن و هوبشمان و معین، ولی با این هشدار که ترکیب گواهی‌شده نیست و رقیبی زنده به نام *ava-bar- دارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AEF:175\",\n              \"status\": \"not_checked\",\n              \"note\": \"Khāleqi Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian version of Horn with Hübschmann's notes) is not online — refs_online.json marks it 'catalog', print-only. Its German original is checkable and says what Nourai's arrow says: Horn no.132 (p.31) 'ōbāšten \\\"anfüllen; verschlingen\\\" … ap. *ava + √par- (vergl. skr. ava-pūrṇa-)'.\"\n            },\n            {\n              \"ref\": \"BQT:180\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān vol. 1 p.180 (archive borhan-ghate-v1 leaf n398, page number fixed from the running head '— ۱۸۱ —' on the following leaf; image saved as refs/ocr/BQT/180.png, transcript 180.vision.txt), Mo'in's footnote 14 to اوبار: «پهلوی ôpâr از ایرانی باستان ava-pârayati مرکب از: ava پیشوند و جزو دوم مشتق از par (پر کردن) «بارتولمه ۸۵۰» … اوباردن و اوباریدن و اوباشتن … از این ریشه است». Word for word Nourai's ava-par 'fill down'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 132, p.31\",\n              \"stance\": \"supports\",\n              \"note\": \"'132. ōbāšten \\\"anfüllen; verschlingen (d. i. sich anfüllen)\\\". Praes. ōbārem, ōbārīden; ōbāš \\\"Gesindel\\\" … ap. *ava + √par- (vergl. skr. avapūrṇa- \\\"anfüllen\\\"); phlv. avpartan bezw. ōpārtan \\\"verschlingen\\\" (Mēn., AV.).'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *parH¹ 'to fill; to nourish' and *bar\",\n              \"stance\": \"partial\",\n              \"note\": \"*parH¹ lists Av. pər- 'to fill' with only *ham- and *us- compounds — no *aua- compound and no NP ōbārdan; *bar lists Av. '(+ *aua-) to bring down, insert'. Cheung thus neither confirms nor excludes ava-par-, but leaves *ava-bar- available.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 850 (par- 'füllen')\",\n              \"stance\": \"partial\",\n              \"note\": \"The column Mo'in cites for the second element; Bartholomae has the simple root, no *ava-par- compound entry.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"obârdan «اُباردن»; obâsh «اوباش» (+ اوباشتن)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The verb and the noun must be separated. (1) obārdan 'to swallow' (Borhān: «ناجاویده فرو بردن … بلع کردن») and its by-form اوباشتن «پر کردن و افگندن» do continue MP ōbārdan, ōbār- (MacKenzie p.60: 'ōbārdan, ōbār- [ʾwpʾl-tn' | M ʾwbʾrd] swallow, devour'), which Horn no.132, Hübschmann §68 (Persische Studien p.176: 'ōbāstan \\\"anfüllen, verschlingen\\\", phl. ōpārtan', listed among the words where Old Persian p appears as New Persian b) and Mo'in's Borhān footnote all analyse as ava- + par- 'to fill' — 'to fill oneself down' > 'to gulp down'. The Rudaki line quoted in the chart («پس بیوبارید ایشان را همه…») is a real 10th-century attestation of the verb. This half is plausible-to-confirmed. (2) obāš 'rowdy, rabble' is not from this verb: it is an Arabic loan, أَوْبَاش ʔawbāš, the broken plural of وَبَش wabaš (metathetic doublet بَوْش bawš) 'mixed rabble' (Wiktionary; and Mo'in himself, in the footnote to اوباش on the very next page of Borhān, p.181: «عربی، جمع وبش، مقلوب بوش. «محیط المحیط»», and in his Farhang-e Fārsi, where اوباش is tagged [ع.] 'Arabic, plural of وبش'). Nourai has taken over Horn's 1893 aside ('ōbāš \\\"Gesindel\\\"') without noticing that his own main Persian authority rejects it; the Persian plural-looking shape اوباش with a singular sense, and the pair بوش/اوباش, are the marks of the Arabic plural. On the orthography: the printed chart writes the verb اُباردن (alef + damma, no wāw) — verified on the page image of PDF p.69 — where Borhān, Dehḵodā and Mo'in all write اوباردن; the JSON reproduces the book faithfully, so the odd spelling is Nourai's, not the extraction's.\",\n          \"derivation_fa\": \"فعل و اسم این گره را باید از هم جدا کرد. (۱) «اوباردن» به معنای «ناجاویده فروبردن، بلعیدن» و گونهٔ آن «اوباشتن» («پر کردن و افگندن» به گفتهٔ برهان) براستی دنبالهٔ ōbārdan فارسی میانه است (مکنزی ص ۶۰: «ōbārdan, ōbār- بلعیدن») و هرن (شمارهٔ ۱۳۲)، هوبشمان (پژوهش‌های فارسی، بند ۶۸، ص ۱۷۶، در فهرست واژه‌هایی که پِ ایرانی باستان در آن‌ها به ب فارسی بدل شده) و حاشیهٔ معین بر برهان، هر سه آن را ava- + par- «پر کردن» تحلیل می‌کنند: «خود را از پایین پر کردن» ← «بلعیدن». بیت رودکی که در نمودار آمده گواه سدهٔ چهارمی همین فعل است. این نیمه پذیرفتنی است. (۲) اما «اوباش» از این فعل نیست؛ وام‌واژه‌ای عربی است: أوباش جمع مکسر وَبَش (و مقلوب بَوْش) به معنای «گروه درهم و فرومایه» (ویکی‌واژه؛ و خودِ معین در حاشیهٔ اوباش در صفحهٔ بعدِ برهان، ص ۱۸۱: «عربی، جمع وبش، مقلوب بوش. محیط المحیط»، و نیز در فرهنگ فارسی با نشانِ [ع.]). نورایی اشارهٔ گذرای هرن (۱۸۹۳) را پذیرفته و ندیده است که مرجع اصلی فارسی خودش آن را رد می‌کند؛ صورتِ جمع‌گونهٔ «اوباش» با معنای مفرد و جفتِ بوش/اوباش نشانهٔ روشن جمع عربی است. دربارهٔ املا: کتاب چاپی این فعل را «اُباردن» (بدون واو) نوشته است — از روی تصویر صفحهٔ ۶۹ راستی‌آزمایی شد — حال آنکه برهان و دهخدا و معین «اوباردن» می‌نویسند؛ پس داده‌های استخراج‌شده وفادار به کتاب است و این املای غریب از خودِ نورایی است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"اُباردن ( اوباشتن )\",\n          \"correct_form\": \"اوباردن (اوباشتن)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/اوباش\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:180\",\n              \"status\": \"partial\",\n              \"note\": \"p.180 (image refs/ocr/BQT/180.png) supports the verb: Mo'in's footnote 14, «پهلوی ôpâr از ایرانی باستان ava-pârayati … مشتق از par (پر کردن) «بارتولمه ۸۵۰» … اوباردن و اوباریدن و اوباشتن … از این ریشه است». But اوباش itself is on p.181 (image refs/ocr/BQT/181.png), where Mo'in's footnote 9 says «عربی، جمع وبش، مقلوب بوش. «محیط المحیط»» — i.e. the cited work contradicts the obāš half of the node.\"\n            },\n            {\n              \"ref\": \"AEF:175\",\n              \"status\": \"not_checked\",\n              \"note\": \"Not online (print-only). Its German original, Horn no.132, does list ōbāš 'Gesindel' with ōbāšten — so Nourai's source really is Horn/Khāleqi Motlaq here; the claim is old, not invented.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p.60\",\n              \"stance\": \"supports\",\n              \"note\": \"'ōbārdan, ōbār- [ʾwpʾl-tn' | M ʾwbʾrd] swallow, devour' — the Middle Persian ancestor of اوباردن, with the preverb ō- < *ava-.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §68, pp.176-177\",\n              \"stance\": \"supports\",\n              \"note\": \"'§68. Ap. p = np. b in: … ōbāstan \\\"anfüllen, verschlingen\\\", phl. ōpārtan …' — Hübschmann files the word among those whose New Persian b goes back to an original p, i.e. par- 'fill'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Fārsi s.vv. اوباردن, اوباشتن, اوباش\",\n              \"stance\": \"contradicts\",\n              \"note\": \"MON_part1: «اوباردن [= اوباریدن، اوبردن؛ ق. اوباشتن] … ناجاویده فرو بردن، بلع کردن» (no foreign tag = Persian), but «اوباش: [ع.] (اِ.) ج. وبش (مفرد، غم.) = بوش، فرومایگان …» — Mo'in marks اوباش explicitly as Arabic.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old Russian\",\n          \"words\": \"u-; u-krai\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Church Slavonic / Old East Slavic u- is the regular Slavic reflex of the particle: PIE *h₂ew > Proto-Balto-Slavic *au > Proto-Slavic *u (Pokorny p.73 'aksl. u Präfix \\\"weg, ab\\\", z. B. u-myti \\\"abwaschen\\\"'; Mann IEC 792 'OCS u- (in u-bero \\\"take away\\\", u-bogŭ \\\"poor\\\")'; Watkins/AHD au-³ 'Old Russian u-, away, in Russian ukazat', to order: UKASE'). Old East Slavic оукраина (ukraina) is u- + краи/край kraj 'edge, border', and Wiktionary's etymology tree makes both halves explicit: PIE *h₂ew > PBSl. *au > PSl. *u-, plus PIE *krey-/*kreh₁y- > *krajь. Two qualifications. (a) The gloss: Etymonline (after Room) analyses ukraina as 'ou \\\"by, at\\\" + kraj \\\"region\\\"', i.e. 'the land at the edge, march', and Wiktionary notes the meaning is 'most commonly taken to have been \\\"borderland, marches\\\"', with a modern Ukrainian counter-reading 'region, country'; Nourai's 'far away edge' over-translates the preverb, which in this compound has its locative sense 'at, by' rather than the ablative 'away'. (b) The cross-reference ☞Sek: kraj does belong to a 'cut' root, but to PIE *krey- 'to cut, separate, sift' (Slavic krojiti 'to cut'), not to *sek-.\",\n          \"derivation_fa\": \"پیشوند -u در اسلاوی کلیسایی کهن و اسلاوی شرقی کهن بازتاب قاعده‌مند همان ذره است: هندواروپایی *h₂ew ← بالتواسلاوی آغازین *au ← اسلاوی آغازین *u (پوکورنی ص ۷۳: «aksl. u پیشوند weg, ab، مثلاً u-myti شستن/زدودن»؛ مان: «OCS u- در u-bero بردن، u-bogŭ بینوا»؛ واتکینز ذیل au-³: «روسی کهن -u دور، در ukazat'»). صورت оукраина در اسلاوی شرقی کهن از -u + край «کناره، مرز» ساخته شده و درخت ریشه‌شناسی ویکی‌واژه هر دو جزء را جدا نشان می‌دهد: *h₂ew ← *au ← *u-، و *krey-/*kreh₁y- ← *krajь. دو نکته: (الف) در معنا، اتیمآنلاین (به نقل از روم) ukraina را «ou به معنای نزد، کنارِ + kraj ناحیه» یعنی «سرزمینِ کنارهٔ مرز» می‌داند و ویکی‌واژه هم معنای رایج آن را «سرزمین مرزی» می‌آورد؛ پس ترجمهٔ نورایی («کنارهٔ دوردست») در پیشوند اغراق می‌کند، چون -u در این ترکیب معنای مکانیِ «نزدِ، کنارِ» دارد نه معنای «دور». (ب) ارجاع او به ریشهٔ Sek: kraj براستی به ریشه‌ای با معنای «بریدن» می‌رسد، ولی به *krey- «بریدن، جدا کردن» (اسلاوی krojiti) نه به *sek-.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/оукраина\",\n            \"https://www.etymonline.com/word/Ukraine\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1391\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai's page 1391 is in the body of the 1975/76 American Heritage Dictionary New College Edition (the geographical entry Ukraine), not in the Indo-European appendix (pp.1505-1550); those 1970s AHD scans on archive.org are lending-only, so the page itself could not be opened. The corresponding root entry is checkable and says the same thing: Watkins 1985, 'au-³, Off, away. 1. Old Russian u-, away … [Pok. 3. au- 72]'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.73\",\n              \"stance\": \"supports\",\n              \"note\": \"'apr. lit. lett. au- \\\"weg, ab\\\" …, aksl. u Präfix \\\"weg, ab\\\", z. B. u-myti \\\"abwaschen\\\" (u-běžati \\\"aufugere\\\"), als Präp. m. Gen. … und, mit Verblassen des Begriffes des Ausgangspunktes, \\\"bei\\\"' — Pokorny himself notes the drift from 'away from' to 'at, by', which is the sense in ukraina.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. au-, au̯- (2) 'away'\",\n              \"stance\": \"supports\",\n              \"note\": \"'… ON au- (FH); OCS u- (in u-bero \\\"take away\\\", u-bogü \\\"poor\\\", etc.)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p.133 s.v. avatar\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein lists 'OSlav. u, \\\"at, with\\\"' among the cognates of OI ava — same element, with the locative gloss.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"Ukraine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Ukraine is a borrowing of the Slavic place-name, not an inherited form: it appears in English from the 1670s, taken from Polish Ukraina or Russian Украина Ukraína, itself from Old East Slavic оукраина ukraina 'borderland' (Etymonline, after Room 2006: 'from Russian or Polish Ukraina, a specific use of ukraina \\\"border, frontier\\\" … from Old Russian oukraina, from ou \\\"by, at\\\" + kraj \\\"region\\\"'; Wiktionary s.v. Ukraine: 'Borrowed from Polish Ukraina or Russian Украи́на, from Old East Slavic оукраина'). The territory was so named because it was the frontier zone of medieval Rus'. The chart gives the node no reference of its own, and none is needed for so recent and well-documented a loan; the only thing to keep in mind is that the English word is a proper name borrowed wholesale, so the 'derivation' from node #6 is a borrowing, not sound change.\",\n          \"derivation_fa\": \"«اوکراین» در انگلیسی وام‌واژه است نه صورتی ارثی: از دههٔ ۱۶۷۰ در انگلیسی دیده می‌شود و از Ukraina لهستانی یا Украина روسی گرفته شده که خود از оукраина اسلاوی شرقی کهن به معنای «سرزمین مرزی» است (اتیمآنلاین به نقل از روم؛ ویکی‌واژه: «وام‌گرفته از لهستانی Ukraina یا روسی Украи́на، از اسلاوی شرقی کهن оукраина»). این سرزمین از آن رو چنین نام گرفت که ناحیهٔ مرزی روسِ سده‌های میانه بود. نمودار برای این گره ارجاعی نمی‌دهد و برای وامی چنین متأخر و مستند نیازی هم نیست؛ تنها باید توجه داشت که پیوند این گره با گرهٔ ۶ وام‌گیری است، نه دگرگونی آوایی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Ukraine\",\n            \"https://www.etymonline.com/word/Ukraine\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book (refs=None); nothing of Nourai's to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"s.v. Ukraine\",\n              \"stance\": \"supports\",\n              \"note\": \"'by 1670s, from Russian or Polish Ukraina, a specific use of ukraina \\\"border, frontier\\\" … from Old Russian oukraina, from ou \\\"by, at\\\" + kraj region.'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. Ukraine (English)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Borrowed from Polish Ukraina or Russian Украи́на (Ukraína), from Old East Slavic оукраина (ukraina), which is most commonly taken to have meant \\\"borderland, marches\\\" in this context.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Indo-European\",\n          \"words\": \"We-spero\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form is real — PIE *wesperos / *wekʷeros 'evening', Pokorny 1173, whence Latin vesper and Greek hésperos — and the analysis Nourai draws is the classical one of his sources: Pokorny states at the end of the very article he cites (p.73) that 'hierher (nach Brugmann) auch der Anlaut des Wortes für Abend, idg. u̯esperos und u̯ekʷeros', i.e. the *we- of *wesperos is this same particle; Klein s.v. west says west is 'prob. an enlargement of I.-E. *we-, \\\"to go down\\\" … Cp. I.-E. *we-spero, whence L. ve-sper'; Watkins heads the entry 'wes-pero-. Evening, night'. So Nourai's 'We-spero: going down (of the sun)' is a faithful report of Klein's segmentation *we- + *spero-. It is marked plausible rather than confirmed for two reasons: (a) the gloss — the word means 'evening', and 'going down of the sun' is the etymological motivation Klein assumes, not an attested sense; (b) current handbooks (Wiktionary, following Beekes and Kroonen) reconstruct *wek(ʷ)speros as an unanalysed inherited word for 'evening' and do not derive its first syllable from *h₂ew/*we-, and Pokorny's own wording ('nach Brugmann') already flags the analysis as one scholar's proposal.\",\n          \"derivation_fa\": \"خودِ صورت واقعی است — *wesperos / *wekʷeros هندواروپایی به معنای «شامگاه»، پوکورنی ص ۱۱۷۳، که vesper لاتین و hésperos یونانی از آن‌اند — و تجزیه‌ای که نورایی رسم کرده همان تحلیل کلاسیک منابع اوست: پوکورنی در پایان همان مقالهٔ ص ۷۲ـ۷۳ می‌نویسد «آغازِ واژهٔ شامگاه، یعنی u̯esperos و u̯ekʷeros هندواروپایی، نیز (بنا بر بروگمان) از همین ریشه است»؛ کلاین ذیل west می‌گوید این واژه «گسترشی از *we- هندواروپایی به معنای فرو رفتن است … سنجیده شود با *we-spero که vesper لاتین از آن است»؛ واتکینز نیز مدخل را «wes-pero- شامگاه، شب» عنوان می‌دهد. پس «We-spero: فرو رفتن (خورشید)» گزارش وفادارانهٔ تجزیهٔ کلاین است. اینکه به جای «تأیید» گفته‌ایم «با احتیاط پذیرفتنی»، دو دلیل دارد: (الف) معنا — واژه «شامگاه» است و «فرو رفتن خورشید» انگیزهٔ ریشه‌شناختیِ فرضی کلاین است نه معنای گواهی‌شده؛ (ب) دستنامه‌های امروزی (ویکی‌واژه به پیروی از بیکس و کرونن) *wek(ʷ)speros را واژه‌ای ارثی و تجزیه‌ناپذیر برای «شامگاه» می‌دانند و هجای نخست آن را از *h₂ew نمی‌گیرند؛ خودِ پوکورنی هم با آوردن «بنا بر بروگمان» نشان داده که این تحلیل پیشنهاد یک پژوهشگر است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/west\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1740\",\n              \"status\": \"supports\",\n              \"note\": \"Klein's 'west' entry (vol. II, in the 1966 pagination around p.1740; read in the 1971 one-volume text, which is verbally identical): 'fr. Teut. *west-, which is prob. an enlargement of I.-E. *we-, \\\"to go down\\\", whence also OI. avaḥ, \\\"down, downward\\\". Cp. I.-E. *we-spero, whence L. ve-sper, \\\"evening\\\", Gk. hesperos … OE. west, etc., orig. meant \\\"the region where the sun sets\\\" (lit. \\\"goes down\\\").' This one entry underwrites nodes #8, #9 and #10 together.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.72-73 (and 1173 s.v. wesperos)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Hierher (nach Brugmann aaO.) auch der Anlaut des Wortes für Abend, idg. u̯esperos und u̯ekʷeros, s. dort.' — Pokorny attaches *wesperos to this root, with attribution to Brugmann.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. wes-pero-\",\n              \"stance\": \"supports\",\n              \"note\": \"'wes-pero-. Evening, night. I. Reduced form *wes-. 1. Suffixed form *wes-to- in Germanic *west- … II. Basic form *wespero-. 1. Latin vesper … 2. Greek hesperos. [Pok. wesperos 1173.]'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. west (English etymology)\",\n              \"stance\": \"partial\",\n              \"note\": \"'from Proto-Germanic *westrą, from *westraz, from Proto-Indo-European *wek⁽ʷ⁾speros (\\\"evening\\\")' — the same etymon, but reconstructed unanalysed, with no link to *h₂ew.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"westo\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Germanic *west- 'west' is the reduced grade *wes- of *wes-pero- plus a suffix: Watkins is explicit — 'I. Reduced form *wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west' — which is exactly Nourai's 'westo' (his spelling of *wes-to-). The comparanda are ON vestr, OFris./MLG/MDu./Du. west, OHG westan, MHG/G westen (Klein), and Buck reaches the same result independently: 'ON vestr, OE west, OHG westan, etc., general Gmc., prob. deriv. of a Gmc. *wes-: Skt. avás \\\"down\\\" beside ava \\\"down from\\\", and Grk. hésperos, etc. \\\"evening\\\"'. The gloss 'sunset, west' is half etymological: the attested Germanic meaning is 'west', 'sunset' being the motivation ('the region where the sun goes down'). Modern reconstructions prefer *westrą / *westraz (with the *-ro- suffix seen in ON norðr : vestr), so the exact suffix is *-to- (Watkins, Klein) or *-ro- (Wiktionary, Kroonen) depending on the handbook; the derivation from *wes- is not in dispute.\",\n          \"derivation_fa\": \"*west- ژرمنی به معنای «باختر» همان درجهٔ کاستهٔ *wes- از *wes-pero- به‌علاوهٔ پسوند است: واتکینز صریح می‌گوید «صورت کاستهٔ *wes-؛ با پسوند *wes-to- در ژرمنی *west- و از آن انگلیسی کهن west»، و این دقیقاً همان «westo»ی نورایی است. هم‌ریشه‌ها: نورس کهن vestr، هلندی و ساکسون west، آلمانی علیای کهن westan و آلمانی westen (کلاین). باک نیز مستقلاً به همین نتیجه می‌رسد: «vestr نورس کهن، west انگلیسی کهن، westan آلمانی علیای کهن و … در سراسر ژرمنی، احتمالاً مشتق از *wes- ژرمنی: سنجیده شود با avás سنسکریت «به پایین» در کنار ava و hésperos یونانی «شامگاه»». معنای «غروب، باختر» نیمه‌ریشه‌شناختی است: معنای گواهی‌شدهٔ ژرمنی «باختر» است و «غروب» انگیزهٔ نام‌گذاری است («جایی که خورشید فرو می‌رود»). بازسازی‌های امروزی *westrą/*westraz را ترجیح می‌دهند، یعنی پسوند بسته به دستنامه *-to- (واتکینز، کلاین) یا *-ro- (ویکی‌واژه) است؛ ولی در اشتقاق از *wes- اختلافی نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/west\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own (refs=None); it hangs on KLN:1740 in the parent box, which does cover it ('fr. Teut. *west-').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. wes-pero-\",\n              \"stance\": \"supports\",\n              \"note\": \"'I. Reduced form *wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne: WESTERN.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 12.46 'west'\",\n              \"stance\": \"supports\",\n              \"note\": \"'ON vestr, OE west, OHG westan, etc., general Gmc., prob. deriv. of a Gmc. *wes-: Skt. avás \\\"down\\\" beside ava \\\"down from\\\", and Grk. hésperos, etc. \\\"evening\\\" (14.46). Walde-P. 1.15.' Buck also states the semantic rule: 'Words for \\\"west\\\" are derived from those for the \\\"setting, going down\\\" (of the sun), or \\\"evening\\\"'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.72\",\n              \"stance\": \"supports\",\n              \"note\": \"'Mit ai. avás \\\"herab\\\" hängt formantisch germ. wes- zusammen in nhd. West, ahd. westar \\\"westwärts\\\", anord. vestr n. \\\"Westen\\\" (*wes-t(e)ro-, vgl. anord. nor-ðr), ahd. westana \\\"von W.\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"west\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Straightforward inheritance: Germanic *west- > Old English west (adverb 'to the west', with the derived westerne 'western', westra 'more westerly') > Middle English west > Modern English west; the French ouest is itself a borrowing of the Old English adverb, which shows how early the word travelled (Klein). Wiktionary gives the same chain: 'From Middle English west, from Old English west, from Proto-West Germanic *westr, from Proto-Germanic *westrą … from Proto-Indo-European *wek⁽ʷ⁾speros'. One dissenting older source is worth recording: Funk & Wagnalls (New Standard Dictionary, p.2699) derives west '< AS. west … < √wes \\\"dwell\\\"', i.e. from the homonymous root *wes- 'to stay, dwell' (Pokorny's 2. au-/wes-, p.72), which is the one competing etymology; Klein, Watkins, Pokorny and Buck all prefer the 'evening/sunset' root that Nourai draws.\",\n          \"derivation_fa\": \"زنجیرهٔ ارث‌بری ساده است: *west- ژرمنی ← west انگلیسی کهن (قید «به سوی باختر»، با مشتقات westerne و westra) ← west انگلیسی میانه ← west انگلیسی امروز؛ حتی ouest فرانسوی وام‌گرفته از همین قیدِ انگلیسی کهن است و نشان می‌دهد این واژه چه زود از مرزها گذشته است (کلاین). ویکی‌واژه همین زنجیره را می‌آورد: «از انگلیسی میانه west، از انگلیسی کهن west، از ژرمنی باختری آغازین *westr، از ژرمنی آغازین *westrą … از هندواروپایی *wek⁽ʷ⁾speros». یک دیدگاه مخالفِ قدیمی هم شایان ثبت است: فرهنگ فانک و واگنالز (ص ۲۶۹۹) west را از «ریشهٔ wes به معنای مسکن گزیدن» می‌گیرد، یعنی از ریشهٔ هم‌آوای *wes- «شب را گذراندن، ماندن» (پوکورنی، au- شمارهٔ ۲، ص ۷۲)؛ ولی کلاین، واتکینز، پوکورنی و باک همگی همان ریشهٔ «شامگاه/غروب» را که نورایی رسم کرده ترجیح می‌دهند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/west\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference printed on this node; the chain is covered by KLN:1740 in the ancestor box.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. west\",\n              \"stance\": \"supports\",\n              \"note\": \"'west, adv., adj. and n. — ME., fr. OE. west (adv.), \\\"to the west\\\" (whence also F. ouest, \\\"west\\\"), rel. to ON. vestr … the enlarged forms OHG. westan, MHG., G. westen, \\\"west\\\", fr. Teut. *west-'.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls, New Standard Dictionary, p.2699 s.v. west\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'[< AS. west, west, < √wes \\\"dwell\\\"]' — F&W attach the word to the root 'dwell, stay the night' (Pokorny's 2. au-, au-es- 'übernachten', p.72) rather than to 'evening'; a minority view, but it shows the segmentation is not universally accepted.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. west\",\n              \"stance\": \"supports\",\n              \"note\": \"'From Middle English west, from Old English west, from Proto-West Germanic *westr (\\\"western\\\"), from Proto-Germanic *westrą (\\\"west\\\"), from Proto-Germanic *westraz, from Proto-Indo-European *wek⁽ʷ⁾speros (\\\"evening\\\").'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T05:45:59.492Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-69.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T05:46:04.149Z] TOOL CALL #112: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-69.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 69"
}
```


### [2026-09-05T05:46:06.288Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 5, 'disputed': 3, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6, 'partial': 4, 'contradicts': 1, 'not_found': 1, 'not_checked': 6}
books consulted: {'supports': 19, 'partial': 7, 'contradicts': 3} | by book: {'BRT': 3, 'CHEUNG': 3, 'PHD': 3, 'POK': 3, 'Wiktionary': 3, 'KLN': 2, 'AHD': 2, 'KNT': 1, 'WLD': 1, 'BQT': 1, 'HRN': 1, 'HUB': 1, 'MON': 1, 'IEC': 1, 'Etymonline': 1, 'SYN': 1, 'FSD': 1}
```


## [2026-09-05T05:46:26.276Z] AGENT

Done. `verify_check.py 69` reports 0 PROBLEM lines.

**Page 69 (book p. 39), root "Au 2, We 2" — 1 non-redirect entry, 10 nodes** (3 redirect entries skipped)

- Root: **confirmed** (Pokorny 72 "au- (au̯e-), u̯e- 'herab, weg von'" = modern *h₂ew).
- Node verdicts: confirmed 5 (#1 ava/aorâ/avara, #6 OldRus u-/u-krai, #7 Ukraine, #9 Gmc westo, #10 west), plausible 2 (#4 ava-par, #8 We-spero), disputed 3.

Disputed items:
- **#2 avara-sad** — Nourai follows Mo'in's Borhān footnote (p.733), but MacKenzie (MP `hunsand` = hu- + sand, p.45) and Wiktionary give *hu-*, not *ava-ra-*; his own cited HRN:105 gives Av. \*hu-rasant- and so **contradicts** him. His ☞Sed pointer is also wrong: the second member is *sand-* 'to seem/please' (PIE *(s)ḱend-), not *sed-.
- **#3 xorsand** — same problem downstream (oftādan in the same node is fully confirmed by HRN:22 + Cheung + MacKenzie).
- **#5 obâsh** — Arabic loan أوباش, plural of وبش (Wiktionary; and Mo'in himself in the footnote on Borhān p.181 and in Farhang-e Fārsi [ع.]). The verb obârdan/اوباشتن in the same node is well supported (Horn 132, Hübschmann §68, Mo'in BQT:180 "*ava-pārayati … از par (پر کردن)").

Ref-check notes for the owner (no extraction errors found — the JSON is faithful to the printed page, which I checked as an image):
- **BQT:180 in node #3 is a mis-citation** by Nourai: p.180 is the اوبار page (cited correctly on node #4/#5); it has nothing on افتادن/خرسند. BQT:145 is the right page for افتاد (page number confirmed from the scan's running head).
- **HID:209** is one page short: the `ava]` entry is on p.210 (p.209 is the Glossar's opening remarks).
- The book prints the verb as **اُباردن** (no wāw), where all sources write اوباردن — Nourai's own orthography, not an extraction slip (recorded as `error_in: "book"` on node #5).

New audit files: `data/verification/sources/refs/ocr/BQT/{180,181,733}.{png,vision.txt}`, `.../HRN/105.{png,vision.txt}`, `.../BOOK/69.png`; 8 web pages archived via fetch_source.py (one, en.wiktionary اوباردن, 404'd and is not cited).
