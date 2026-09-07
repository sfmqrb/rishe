# Verification process log — verify-page-347


## [2026-09-07T17:36:20.816Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 347 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-347.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-347.json. Write /home/sfmqrb/git/rishe/data/verification/page-347.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 347` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:22.321Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:23.016Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:23.030Z] TOOL RESULT

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


## [2026-09-07T17:36:23.271Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-347.txt"
}
```


### [2026-09-07T17:36:23.284Z] TOOL RESULT

```
1	=== PDF page 347 (book page 317) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Nabatu : to shine  (refs AKD:60)
4	#1 (parent #0) [Akkadian] refs=AKD:60 | Nabtu, Naptu : light, lamp oil
5	#2 (parent #0) [Aramaic] refs=KLN:1027 | naftâ : oil
6	  #3 (parent #2) [Arabic] refs=KLN:1027 | naft «نفط» : oil
7	    #4 (parent #3) [Persian] refs=KLN:1027; BQT:2155; AKD:60; MON:4777 | naft «نفط ، نفت» : oil, kerosene | NOTE: POK:316 & HRN:232 derive "naft" from "Nebh:cloud".
8	  #5 (parent #2) [Greek] refs=FSD:1649; KLN:1027 | naphta : oil | NOTE: SKT:344 derives the Greek word from Persian "naft: oil".
9	    #6 (parent #5) [French] refs=PHN:283 | 
10	      #7 (parent #6) [Persian] refs=MON | naftâlîn «نفتالین» : Naphthalene
11	    #8 (parent #5) [Latin] refs=KLN:1027 | naphtha
12	      #9 (parent #8) [English] refs=None | naphthalene ; naphthol
13	--- entry 1 ---
14	ROOT [Indo-European] Nabja : beak  (refs AHD)
15	#1 (parent #0) [Persian] refs=ISS:143; MON:4857 | nok, nŭk «نوک» : tip, beak ; nŭl «نول» : beak
16	#2 (parent #0) [Sogdian] refs=MON | nwk : beak
17	#3 (parent #0) [Old English] refs=ISS:143 | nebb : nose, beak
18	  #4 (parent #3) [English] refs=AHD | neb ; nib ; nipple ; nibble
19	--- entry 2 ---
20	ROOT Nabtu -> redirect to Nabatu
21	--- entry 3 ---
22	ROOT [Avestan / Old Persian] Naěma : half  (refs HRN:239; SYN:936; BRT:1036)
23	#1 (parent #0) [Pahlavi] refs=BQT:2233; SNS:290 | něm : half
24	  #2 (parent #1) [Persian] refs=BQT:2233; BRT:1036 | nîm «نیم» : half | extra: نیمه، نیمروز، نیم رخ، نیمشب
25	
```


## [2026-09-07T17:36:27.628Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-347.json",
 "description": "Read source JSON for page 347"
}
```


### [2026-09-07T17:36:27.663Z] TOOL RESULT

```
{
  "pdf_page": 347,
  "book_page": 317,
  "entries": [
    {
      "root": {
        "name": "Nabatu",
        "lang": "Akkadian",
        "refs": "AKD:60",
        "gloss": "to shine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "AKD:60",
          "words": [
            {"translit": "Nabtu, Naptu", "gloss": "light, lamp oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "KLN:1027",
          "words": [
            {"translit": "naftâ", "gloss": "oil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "KLN:1027",
          "words": [
            {"translit": "naft", "gloss": "oil", "script": "نفط"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "KLN:1027; BQT:2155; AKD:60; MON:4777",
          "words": [
            {"translit": "naft", "gloss": "oil, kerosene", "script": "نفط ، نفت"}
          ],
          "note": "POK:316 & HRN:232 derive \"naft\" from \"Nebh:cloud\".",
          "quote": {"text": "هرکجا نفط و آب جمع شوند - نفط بالا وآب زیرتر است", "poet": "Khâqânî"}
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "Greek",
          "refs": "FSD:1649; KLN:1027",
          "words": [
            {"translit": "naphta", "gloss": "oil", "script": null}
          ],
          "note": "SKT:344 derives the Greek word from Persian \"naft: oil\".",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "PHN:283",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "naftâlîn", "gloss": "Naphthalene", "script": "نفتالین"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "Latin",
          "refs": "KLN:1027",
          "words": [
            {"translit": "naphtha", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "naphthalene", "gloss": null, "script": null},
            {"translit": "naphthol", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nabja",
        "lang": "Indo-European",
        "refs": "AHD",
        "gloss": "beak"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "ISS:143; MON:4857",
          "words": [
            {"translit": "nok, nŭk", "gloss": "tip, beak", "script": "نوک"},
            {"translit": "nŭl", "gloss": "beak", "script": "نول"}
          ],
          "note": null,
          "quote": {"text": "حرص بط آمد که نولش در زمین - در تر و در خشک میجوید دفین", "poet": "Molavî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "MON",
          "words": [
            {"translit": "nwk", "gloss": "beak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old English",
          "refs": "ISS:143",
          "words": [
            {"translit": "nebb", "gloss": "nose, beak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "neb", "gloss": null, "script": null},
            {"translit": "nib", "gloss": null, "script": null},
            {"translit": "nipple", "gloss": null, "script": null},
            {"translit": "nibble", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nabtu",
        "redirect": "Nabatu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Naěma",
        "lang": "Avestan / Old Persian",
        "refs": "HRN:239; SYN:936; BRT:1036",
        "gloss": "half",
        "note": "This word is cognate with Sanskrit word \"něma:half\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:2233; SNS:290",
          "words": [
            {"translit": "něm", "gloss": "half", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2233; BRT:1036",
          "words": [
            {"translit": "nîm", "gloss": "half", "script": "نیم"}
          ],
          "script_extra": "نیمه، نیمروز، نیم رخ، نیمشب",
          "note": null,
          "quote": {"text": "روندگان طریقت به نیم جو نخرند - قبای اطلس آنکس که از هنر عاریست", "poet": "Hâfez"}
        }
      ]
    }
  ]
}
```


## [2026-09-07T17:36:29.122Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AKD','KLN','FSD','SKT','PHN','MON','BQT','ISS','AHD','HRN','SYN','BRT','SNS','POK','WLD','PHD','NYB','HUB','ARY','SOD','IEC','WEB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T17:36:30.479Z] TOOL RESULT

```
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-07T17:36:40.981Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && ls | head -80; echo ---; ls | wc -l"
}
```


### [2026-09-07T17:36:41.041Z] TOOL RESULT

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
---
95
```


## [2026-09-07T17:36:41.196Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T17:36:41.240Z] TOOL RESULT

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


## [2026-09-07T17:36:49.136Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== AKD naptu/nabtu ===\"; grep -n -i -E 'na[bp]tu|naphtha|Naphta' AKD.txt | head -30\necho \"=== KLN 1966 naphtha ===\"; grep -n -i 'naphtha' KLN_1966.txt | head -20\necho \"=== KLN 1971 naphtha ===\"; grep -n -i 'naphtha' KLN_1971.txt | head -20\necho \"=== SKT naphtha ===\"; grep -n -i 'naphtha' SKT.txt | head -20"
}
```


### [2026-09-07T17:36:49.232Z] TOOL RESULT

```
=== AKD naptu/nabtu ===
975:alck.  naptu  Erdöl,  Naphtha  :  >  aram.  naptä,  neptä  O  arab.  naft, pers.  neft,  sowie  griech.  vätpfia^  usw.,  NapJdha).  akk.  etrdnu  wohl
=== KLN 1966 naphtha ===
24952:naphtha,  n.,  an  inflammable  liquid  distilled  from petroleum.  —  L.,  fr.  Gk.  vaiyffx,  fr.  Aram. naphta,  nephtd  (whence  also  Arab,  naft,  Pers. neft),  fr.  Akkad,  naptu,  ‘naphtha’.  See  Heinrich Zimmern,  Akkadische  Fremdworter  als  Beweis fiir  babylonischen  KultureinfluB,  2nd  edition, Leipzig,  1917,  p.  60.
24953:naphthalene,  n.,  a  white  crystalline  hydrocarbon, C10H8  ( chem .)  —  Orig.  naphthaline,  coined  by John  Kidd  fr.  naphtha  and  chem.  suff.  -ine.  The /  was  inserted  for  the  sake  of  euphony.  For  the ending  of  naphthalene  see  suff.  -ene.  Cp.  phtha- lein(e),  phthalin.
24955:naphthyl,  n.,  the  univalent  radical,  C10H.  (chem.) —  Formed  fr.  naphtha  with  suff.  -yl.
28664:Formed  fr.  prec.  word  with  suff.  -aceae. phthal-,  form  of  phthalo-  before  a  vowel, phthalate,  n.,  a  salt  of  phthalic  acid  (chem.)  — Formed  fr.  phthal-  and  chem.  suff.  -ate. phthalein,  phthaleine,  n.,  any  of  a  group  of  syn¬ thetic  dyes  (chem.)  —  Abbreviation  of  (na)ph- thalein,  (na)phthaleine.  See  naphtalene. phthalic,  adj.,  pertaining  to  any  of  three  isomeric acids  (chem.)  —  Abbreviation  of  (na)phthalic. See  naphthalene  and  adj.  suff.  -ic. phthalin,  n.,  any  of  a  series  of  compounds  obtain¬ ed  by  the  reduction  of  the  phtaleins  (chem.)  — - Abbreviation  of  (na)phthalin.  See  naphthalene, phthalo-,  before  a  vowel  phthal-,  related  to  phthal¬ ic  acid.  —  Back  formation  fr.  phthalic  (in phthalic  acid).
=== KLN 1971 naphtha ===
158558:naphtha, n., an inflammable liquid distilled from 
158561:neft), fr. Akkad, naptu, ‘naphtha’. See Heinrich 
158566:naphthalene, n., a white crystalline hydrocarbon, 
158567:C 10 H 8 ( chem .) — Orig. naphthaline, coined by 
158568:John Kidd fr. naphtha and chem. suff. -ine. The 
158570:ending of naphthalene see suff. -ene. Cp. phtha- 
158581:— Formed fr. naphtha with suff. -yl. 
181484:See naphthalene and adj. suff. -ic. 
181487:Abbreviation of ( na)phthalin . See naphthalene, 
=== SKT naphtha ===
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
```


## [2026-09-07T17:36:51.543Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== FSD naphtha ===\"; grep -rn -i 'naphtha' FSD_vol3.txt | head -20\necho \"=== PHN naphte ===\"; grep -n -i -E 'naphte|naphtha|nafta|naphthe' PHN.txt | head -20\necho \"=== LKT naphtha ===\"; grep -n -i -E 'naphtha|naft' LKT.txt | head -20\necho \"=== POK 316 nebh ===\"; grep -n -E 'nebh' POK_full.txt | head -20"
}
```


### [2026-09-07T17:36:51.632Z] TOOL RESULT

```
=== FSD naphtha ===
FSD_vol3.txt:34253:portion of light coal-naphtha
FSD_vol3.txt:35406:naphthalene, either of two loo-
FSD_vol3.txt:35408:oemethyl naphthalene Is a thick
FSD_vol3.txt:35411:ture of brom«naphthalene and
FSD_vol3.txt:65689:Originally naphtha was the more volatile constituent of
FSD_vol3.txt:65694:as naphtha vitriol! (sulfuric ether), and at present it Is
FSD_vol3.txt:65706:as crude naphtha, or again sepiiraied by distillation Into
FSD_vol3.txt:65707:gasoline, rehned naphtha, and benzene), shale«n. (dlsillled
FSD_vol3.txt:65713:liL* HayN wan ton liaht and inHaniinnhli* for niirh a umi* ( >1 naphtha,
FSD_vol3.txt:65716:fL , < Ur naphtha, v. Ar nafth 1
FSD_vol3.txt:65717:- Bathirate or Boghead naphtha* the naphtha cIIh-
FSD_vol3.txt:65719:— crude n.* unreiined iietroleum-naphtha — naph'tha*
FSD_vol3.txt:65721:vapor of naphtha n.-ship* n A vessel curry lug uuphlhu
FSD_vol3.txt:65728:salt of naphthalic acid
FSD_vol3.txt:65746:pounds Naphthalene Is (a»
FSD_vol3.txt:65747:used very generally as a dls- Naphthalene,
FSD_vol3.txt:65761:pertaining to, or derived from luiphthol. like naphthalene
FSD_vol3.txt:65793:A7ln derivative of naphthalene (CmlltN-C *i .Us) uapirtha*
FSD_vol3.txt:65821:rlv(*(l from coal-tar or synthetlcallv pr»*i»urecl from naphtha-
FSD_vol3.txt:65832:-MZ’iNO I To Hiituruto or mix with nuplithol or naphtha
=== PHN naphte ===
7899:NAPHTE,8. m.(A.)
9852:dant certaines propriétés du naphte et bonne à brûler, ce qui semble
10769:Naphte, s. m. (a) a83
=== LKT naphtha ===
2771:'Schmutz',  dazu  Adj.  kirli  'schmutzig' [vom  Stamme  kir  'schmieren,  Farbe, Schmutz'  Vämbery  TktEtWb  S.  89, Nr.  92];  hieraus  bulg.  kir  'Sehmutz  am Körper',  kirliiv  'schmutzig',  russ.  kir 'mit  Naphtha  getränkte  Erde'.  [Bern SlEtWb  505.
3547:'Erdpech,  Naplitha'  (Horn  NpEt  S.  23'2, Nr.  103Ö],  ar.  naft  [der  Wurzel  nafata 'sieden,  wallen'  anfrepaßl;  nachZAkkFW (iO  jedoch  ülier  aram.  napfä  aus  ass. naptu  'Erdöl'],  Ik.  na/t,  neft;  hieraus gr.  vctqpöa  [ngr.  tö  vd9Ti],  lat.  naphtha und  sp.  nafta,  frz.  naphte,  rum.  7iafta, naft;  luss.  neft';  dtsch.  Naphtha  'Erd- pech, Petroleum'.  [Gorjajew  228.  Löbel EITAP  68.  Eguilaz  462.
5852:3^a&ofe  1542 Nadir  1565 Nankint'gJ  1554 Naphtha  1538 J^a/-(/e  1548 Natron  1567 JV^afscfe  1530 Neschires  j.  127 iST/if/r/M  1569 Nirwana  1573 Nischan  1574
6629:j  naftai  1542
7440:naphtha  1538 wj^er  1568 nitrum  1567 nucha  1579 nuphar  1570
7628:naftoö  1542 w«/e  1536 nanking  1554 Mom"  1337
8728:nahdbßa)  1542 nacafa  1532 nacaradä  1546 nadir  1565 nafea  1531 naft(a)  1538 naliiea  1540 «aÄi  1544 waiöa  1289 naingiü  1541 waij<  1541 namas  1552 namea  1551 norghilea  1556 Jiar^  1557 naz(uri)  1563 nazar  1564 näfratnä  1361 wa/8M<  1577 nälban  1549 näran^ä  1555 nästräpa  1439 «awi  1577 Me/"er  1533 M«<M  1541 nene(acä)  1553 neiiei^or  1553 nenufär  1570 ni^ter  1576 no/ioi  1577 nufär  1570 nur(liÜ)  1580
=== POK 316 nebh ===
```


## [2026-09-07T17:36:59.307Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== POK nebh ===\"; grep -n -E 'nebh|nébh|nebli|nabh' POK_full.txt | head -30\necho \"=== POK files ===\"; for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"-- $f\"; grep -c '' $f; done"
}
```


### [2026-09-07T17:37:00.780Z] TOOL RESULT

```
=== POK nebh ===
26261:Material: Old Indie [nasalized * h2anmbhya] nabhya-u. "hub", nabhi-i. "navel, hub, kinship', 
26263:nabhTla-v\. (uncovered) " pubic region, navel dent'; Avestan naba-nazdista- " der 
26356:doubtful Old Indie nabbanu-m., nabhanu-i., probably "wellspring'; Avestan aiwi-naptJm 
62002:Material: Old Indie nabhate^ cracks'; Old Icelandic nsefr^ the outer birch bark ' as 
=== POK files ===
-- POK_01.txt
5152
-- POK_02.txt
6716
-- POK_03.txt
5975
```


## [2026-09-07T17:37:00.907Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== HRN naft ===\"; grep -n -i -E 'naft|neft' HRN.txt | head -20\necho \"=== HRN nim ===\"; grep -n -E 'n[iî]m\\b|naSma|naema|nae-ma' HRN.txt | head -30"
}
```


### [2026-09-07T17:37:00.975Z] TOOL RESULT

```
=== HRN naft ===
8977:1035. neft ^Naphta .
8980:LW. ar. naft; kurd. nefte; bei. n. napt 'Donnerkeil,
=== HRN nim ===
3758:büssen', tuganem, ttiganim (Hübschmann, No. 276).
4519:kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
5361:y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
5363:iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
5717:ein 'Geburt', cnanim 'erzeugen' (H. No. 136).
8126:LW. kurd. genim (vergl. g. gamim); af/. yanum;
8458:[/^mar-^ mriydte 'sterben ; arm. meranim 'sterben' (H.
8872:berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
9234:aw. naema- *halb* in naemo asm, na^me /saf^ti,
15225:Fnn/inim- 244 Anm.
21253:d. nimäyiin 1042.
22173:cnanim 645.
22464:tttrsatnim 388.
22477:tuyanim 402.
22531:zercanim 1097.
22762:ahd. mnimä 963.
```


## [2026-09-07T17:37:06.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== HRN 8965-9000 ===\"; sed -n '8965,9000p' HRN.txt\necho \"=== HRN 9225,9260 (naema) ===\"; sed -n '9225,9260p' HRN.txt"
}
```


### [2026-09-07T17:37:06.269Z] TOOL RESULT

```
=== HRN 8965-9000 ===
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.— 232 -
1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
Doch wohl auch zu np. nisesten (No. 1033), wenn-
schon die Erklärung der Formen schwierig ist. Ge-
hört dazu etwa auch äsyäne *Nest' (No. 35)?
skr. LW. niglmana" (PärasTpr. ed. Weber, No. 433).
1035. neft ^Naphta .
aw. napta- *feucht' ; ai. l/^nabh-, ndbhatB 'spalten,
platzen; hervorquellen*.
LW. ar. naft; kurd. nefte; bei. n. napt 'Donnerkeil,
Blitzstrahl, Kanone' (No. 177) gehört aber wohl nicht
hierher.
Arische Doppelformen naph- und nabh-, vergl.
Hörn, KZ. 32, 584 No. 16.
1036. fUgasten malen', Praes. nigär-em, nigarld^n^ nigär
*Bild*, nigdristdn (Häfiz 16, 5).
Causativum zu nigertdeny nigeristen (No. 1038),
wörtlich *ansehbar, sichtbar machen'; phlv. '^n(i)kar
etc., vergl. arm. LW, nkar 'Bild', nkaren, tikarem,
1037. nigäh 'Anblick, Aufmerksamkeit*.
aw. *nikasa- (vergl. ägäh, No. 40); phlv. n(i)käs.
LW. kurd. nekä; bei. nikäh (263).
Kä§. V. hat sogar als Verbum [/^kos- *sehen' noch
erhalten, nämlich in Praes. bitkesün, Impt. bikes, Inf.
bikasdn u. s. w. (s. v. nigäh kerden).
1038. nigertden 'betrachten', nigeristen.
Käs. Q. vergl. angastän^ batangastdn (s. v. nigc^
kerden),
Wohl zu derselben Wurzel wie aw. hankäray§mi,
siehe np. engärden (No. 123); phlv. n(i)karitan,
=== HRN 9225,9260 (naema) ===
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.- 239 —
ap. fiaiha- \schön, gut* ; phlv. neicah, nSwakih, new
(PPÖl.) 0.
1069. nem 'Hälfte, halb*.
aw. naema- *halb* in naemo asm, na^me /saf^ti,
vd. 4, 45, Geld n er, Studien I, 100 [na^mqm im
ZPGl. bedeutet nicht *halb*); skr. nvma- halb*; phlv.
mm, nSmak.
kurd. nTw *Hälfte, vergl. nlwrfiz 'Mittag*; afy. mmai;
bei. vergl. nl^röt^, nSnnöc, n. nermös 'Mittag', mmsap,
n. nSmSaf 'Mitternacht* (269) ; sar. L W. naim.
Vergl. D''i13X (Talmud) 'halb (sc. gar), nur zur
Hälfte (sc. gebraten)*, de Lagarde, Semitica I, 39.
1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
aw. *n? — \/gaos-, vergl. apa gaosay^iti; phlv.
n(i)yösJtany n(i)yö/sltan bezw. n(i)gösltan'') 'hören'; ai.
[/"ghöS'^ ghösati mit d 'hören, horchen auf.
bei. mgösag, niyösay (262).
>) Vergl. Fr. Müller, WZKM. 5, 265.
Die jüngere phlv. Form tiek liest Justi fZDMG. 46, 288) zwoi
Mal auf Gemmen (die letztere derselben, JRAS. XIII No. 45, die ich
ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
ZDMG. 11, 320 als semitisch (!) entziffert, worauf mich Herr Cler-
mont-Ganneau aufmerksam macht).
*) de Lagarde^s CBeitr. zur altb. Lex. 76) von Darmesteter
f6t. ir. I, 85 Note 2) wiederholte Erklärung aus aw. yao^nti' ist ver-
fehlt ; phlv. ftffJyö/Sitan^ das auch gelegentlich n(i)ybHltan geschrieben
sein kann (aber wo?), beruht auf einer im Pchlevl häufigen graphischen
Eigentümlichkeit.
Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
l/kar8', kasiian u. s. w.), vergl. auch bereits aw. pä^no" gegen ai.
```


## [2026-09-07T17:37:17.756Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== POK napta ===\"; grep -n -E 'napta|nébhos|nebhos|nebhelā|Nebel' POK_full.txt | head -30\necho \"=== POK_01/02/03 napta ===\"; grep -n 'napta' POK_0*.txt | head -20"
}
```


### [2026-09-07T17:37:17.816Z] TOOL RESULT

```
=== POK napta ===
26357:astrhe (befeuchtet =) besudelt with blood', napta- "humid, wet' {*nab-ta-), npers. neft^ 
62605:naptar-, ap. napat- (is.. Old Indie apam napat, Avestan apqm napa-u. name of a divinity (" 
=== POK_01/02/03 napta ===
POK_01.txt:4657:naptlm  asti  ,er  (befeuchtet  =)  besudelt  mit  Blut',  napta-  , feucht'  {*nah-ta-) npers.  neft  ,Najphtha' -^  ,^
```


## [2026-09-07T17:37:19.523Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== BRT naema ===\"; grep -n -E 'naēma|naema|nae-ma|naSma' BRT.txt | head -30\necho \"=== SYN 936 half ===\"; grep -n -E '^\\s*9\\.9[0-9]|half' SYN.txt | grep -n -i 'half' | head -20"
}
```


### [2026-09-07T17:37:19.604Z] TOOL RESULT

```
=== BRT naema ===
3251:•  j.  aüara-naema-  m.  'die  untere  Seite'; nur   Abi.   °mit  'von   unten   her,   unten':
3262:•  j.  aSairi.naema-  m.  'die  untere  Seite': "^wamca  drujitnca  niüamn  'ntpmca  Yt4-
4603:•  j.  antar«.naema-  m.  'Innenseite',  nur Abs,  'von  der  Innenseite,  von  innen  her, innerhalb' :  i^äraoxmam  (sd.)  "mät  V.  2. 30,38,  T. 57.2, ■>.  ■
7170:^fiti'"'Tir~  zL'^'"'  ""^  ""'  ^  '^'  ■"el"-|.  j.+ät9r»-tarö.naema-'>m. 'die  über  das
8336:•  j.  upara.naema-  m.  'die  obere  Seite', nui  AUS.  'mai  'von  oben  her,  oben':  urvatö
15728:väiam  (sd.j  vazaUi  YL  ü.  33;  —  mmsu  (sd.) *°f^fl">(ADm.)a:"ak/?V./p.42.  2)9)  der Reihenfolge  (und  dem  Rang)  nach,  'der erslere':  ttaola  (sd.)  yanya  .  ,  'va/^^  vä naemat  aparät  vä  N._37;  —  yai  ki  avßi •rum'>  ubjyäite  (sA.)  V.j-sa  PQZ.;  —  cva^ haca  'rvaiibya*^  (läxcA.  majaHfya)?  ya%a %rig3im  V.p.  9;  Ä  39; —  aiwUa  apanm (sd.)  apäla  'voHbyai'i  V.iß.^S; — 'rvä^^ äätä  dämqn  aiaonXsY.iÖ.^;  —  upa  vä mq%r?m  sp^niitn  maraSa..  'rutiüa'^  naime asne  apanmca  ".  ,  die  erste  Hälfte  und die  zweite"  V.4.4S;  45;  —  'ruin*>  vä na^m^m  ^yän  apanm  väü.44; — mitAbl.: näirivaite..afimäi  •rum''>  {SSx\.)/ramraomi ya%a  May avB^sd.)^. 4.47.  A)iSTLpcururva als  Adv.  'zuerst';  'rva  hl  tamS  baraiti •n>a  oTannä  Yt/4^36.  3)9)  der  Zeit nach  'der  frühere,  erstere':  Xtyaiy  'ruvä xsäyähiyä  Eh.  4. 9;  —  anuzvarstä^  (sd.) paiü  'rvät^  V.4.  ao;  —  yafärS  *rvS^ uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima&e  mä  Ä/  'rv5^''  büSiyaifa  nS Y.  p.  2 1 ;  a  I  \  F.  1 3»;  —  iaiärif  'rvö  (NPm.)J* amayäntei^)  V.7.36;37j  —  ava.jasnm (sd.)  -rvqm^  äpB  JaÜiyöt^  .  .  pasiaSa aiwyS  zaohrä  frabarOis  Y.  6^5. 1  o.  a)  Das Praesens  hat  dabei  den  Sinn  der  Ver- gangenheit"); j'?«  Toa^'f  (NPm.)  mihrwt druiinti  "die  zuvor  den  M.  belogen  haben" Yt  10. 45;  —  atibyS  .  .  ysi  vB  vanuhls  . . nHiJ  °rva^  (ASf.)")  äzärayente  "denen, die  euch,  ihr  guten, . .  nicht  zuvor  erzürnt haben"  YLy.30; — tä  sravä  ..yä'rva'^ al^rapalays  dnnjayan  (Sp.  773  o.)  V. 4.45;  —  ä  äim  aoxta..'rv3'*  asavapara.- iri^yB  (PPA.)  ". .  ein  früher  gestorbener Gläubiger"  H.  2.  16.  —  Aber:  ä  dim aoxta  .  .  'rv5''>  drvö  ava.mtrm  (PPfP.) ". .  ein   früher   gestorbener  Ungläubiger"
15745:«73  paurva.naema-
15747:•  j,  paurva-naema-"  m.  'die  vordere Seite';  nur  Abi.  'mal  'von  der  Vorderseite her,  an  der  Vorderseite'  sva,  1}  'vom,  vor- aus', a)  absolut:^«!  aM  °mät..ym paskät Yt.iS.2.  h)  mitG^a.: yeAAe  °m3t  vazaiU jvnihraynS  "welchem  voraus  fährt.."  Yt. 10,  Jo; —  ms^r)m..y5  tarU harqm  asnaoiii °tiist  amisahe  hü  ".  .  voraus  vor  der  ud- sterblichen  Sonne"  Vt./o.  13;  —  auirmja- yais  aom  srum  °mäl  ahe  gr-avaAe  "üa  soVisX befestigen  das  Blei(gefäss)  vom  an  dem Stock"  V.  §.  1 4.  a)  'kopfüber'  (?) :  'mät  '> paiai  dyaos^S^.  761  u.)  ..  artrö  mainyus Yt.,?.  13-
18490:•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;  —  paourwn  va  'm^m  yän apar?m  va  "das  erste  Halbjahr  oder  das zweite"  N.  44)  —  pimrumca  'me  asne (bz.  xia/ne)  aparvmca  "die  eiste  Hälfte  des Tags  (bz.  der  Nacht)  und  die  zweite"  V. 4. 45*>.  3)  m.  a)  'Hälfte,  latus  alterum': ya(  vS  'mim  yat  va  'hri^wi  .  .  V,  if ,  32, 16.  2,  Y.  Jp.  7;  V.Äioi;  — aWsr  'mat.. uparät  *mat  y.i4.T,  6'.  8,  N.5_j,  P.  23;  — haoyat  hol  +*mS/3' . .  dalinat  hat  *'mai^ N.  75;  —  '^fraoirilarai  'mat  N.fi?;  — *aevahmat  'mat  N.  7p;  —  paurvat  va 'mat  aparät  va  ^.Jj;  —  antarä^  (sd.) 'm^  V.5.43»,  51,  6.2,  3,  7.77,  8.^1,  42, 104,5.15,  16,  N.öo,  6p',  *7jT,  54,  104^; II';  —  *va  *'ma  N.pp*';  —  vaHbya 'maltiya  "von  beiden  Seiten"  V./_y.3 1—37 PüZ.*;  —  apaxtarat  haca  *mat  V.ig.i, H.2.25,  FrW,/o.43";  V.j^.s,  H.2.7,  A. 4.6.  b)  'Seite'  überhaupt:  vlspe  'mq (AP.)  F.jg;  —  vlspa^työ  'maübys  Yl /0.41;  —  ahmst  'mäi ..yahmäi  'tnanqm YtJO.  19;  y.  3,  V.Ä80;  —  usastaratibyö haca  'maiiiys  V./p.5;  1,  H.2.  35,  V.7.  2, *i6,  FrW.JO.42.
19263:•  j.  niitara-naema-  m.  'Aussenseite',  nur Abis,  'von  der  Aussenseite  her  sva.  aussen, ausserhalb';  'mäj  nmänahe  V,  f^.  7;  — , nmarum  :^sraoxs?um  (sd.)  *antar>jiaimä^ st?hrpals>m  'mal  "V.^y.zi,
22614:Vgl.  vaHä:  —  ai.  vanäm  GP.  —  Pü.:  van. }.  vana  N.p:  lies  ana;  —  l'.SO:  lies  vai'a. ]'.  vana/ma:  s.  ^van-; —  N.pp:  lies  va  naema. j.  T-anaf  F,  ^f. :  lies  vanf.
29683:i)  'sich  bemächtigen,  in  seinen  Besitz bringen,  gewinnen';  a)  mit  Akk.;  tri- %mttm  xia'hnm  zazaiti  (3SKPA.)''  Yt. 5.  i3o(?).  b)    mit    Lok.:    hanaema(3
=== SYN 936 half ===
1:2365:e Semantic source is most com ‘sort, kind? (this often from ee Tace’), but in part ‘section’, ‘side’ ‘half?
2:2393:6. ChSl. poli, SCr. spol, Russ. pol, same word as ChSl. polt, Pol. pol, etc. ‘half’ (18.24).
3:3257:But those containing words for ‘broth- er’ or ‘sister’ have arisen in two ways. Some denote the relationship through the brother or sister of one’s parent. Others reflect an early direct association between ‘brother, sister’, and ‘cousin’ as a ‘kind of brother or sister’. So Lat. pa- truélis started as frater patruélis (frater tuus erat frater patruelis meus, Plautus), Lith. pusbrolis is literally ‘half-brother’, SCr. brat od strica, not like OE federan sunu ‘son of father’s brother’, but liter- ally ‘brother from father’s brother’, Russ. dvojurodnyj brat lit. ‘second line brother’, etc. This extension of ‘broth- er’ and ‘sister’ is conspicuous in Balto-
4:3289:rolis, pusseseré lit. ‘half- ter�� and also used in that thalf’? and the words
5:3627:3. The Celtic series, Ir. lessathair, etc., NIr. leasathair, etc., W. llysdad, etc., Br. leztad, etc., cpds. of the words for ‘father’ etc., the first part, as in Ir. less-ainm, W. llys-enu ‘nickname’, cog- nate with Ir. leth, W. lled ‘side, half’. Pedersen 2.8.
6:4589:W. adfarch, epd. of march ‘horse, stal- lion’ and ad-, like adfwl ‘castrated bull’, with the depreciatory use of ad- as in adfyw ‘half alive’, adfyd ‘adversity’, etc.
7:4663:1. Grk, jpiovos, epd. of #yut- ‘half’? and dvos ‘ass’.
8:8228:ddall ‘half blind’), Goth. haths ‘one- eyed’, cf. Skt. kekara- ‘squinting’. Walde-P. 1.328. Ernout-M. 128. Walde-H. 1.129.
9:9051:5. Lith. pusryciat (pl.) ‘breakfast’, epd. of pusé ‘half’ (18.34) and rytas ‘morning’ (14.34), so lit. ‘midmorning’ (meal).
20:18890:maim, f Btagp, Clutch, ete . glac ‘half-open fist,
21:22039:Others are from such notions as ‘half’ or freq. ‘side’ (cf. accanto ‘beside’).
22:22048:Ir. leth, NIr. leath (both ‘side’, esp. 28 ‘direction’, and ‘half’, W. adv. led ‘0 part’), prob. : Ir. lethan, Grk. rAarts, ete.
23:22065:Lith. pusé, Lett. puse, lit. ‘half’ (13.24), but used commonly for ‘side’ of objects.
24:22070:Skt. paksa-, also ‘wing, shoulder, half’ : Lett. paksis ‘corner of the house’, aiz pakga iet ‘do one’s need’ (lit. ‘go aside’), Russ. pach ‘groin’, ete. Walde- P. 2.3f. Mithl.-Endz. 3.50.
25:22071:Skt. ardha-, Av. arada-, also ‘half’ (Av. ‘half’? adj. only in epds.), perh. : Lith. ardyti ‘split, divide’, etc. Walde- P. 1.143. Uhlenbeck 14. Barth. 193.
26:22314:Br. hanternoz, ‘midnight’ (lit. ‘half- night’, fr. hanter ‘half’, 13.24) and ‘north’, as opposed to kreisteiz ‘noon and ‘south’.
27:22326:Pol. péinoc ‘midnight’ of pil, pol ‘half’ and
28:23792:QUANTITY AND NUMBER 935 13.24 HALF (Adj. Except as Noted) ‘ Goth: halbs Lith. pusé (sb.), pus- ysos TH ON _ halfr Lett.  puse (sb.), pus- pias st? aémi- Dan. halv ChSl. polit (sb.) dina a (sb.) Sw. halv SCr. 70 (sb.) mea; ib (sb.) OE healf; sim- Boh. _ poloviént; pil (sb.) a mitad (sv-) ME half Pol. polowiczny; pot (sb.) a Wis (sb.) NE half Russ. pol-(polu-) th (sb.), leth- ae el rea ardha-; sami- | , 4 alp; sami- : é It. oath (sb.), leath A eas Vv. naéma- | hanner NHG  halb
29:23796:qlinumeral derivs.. those for ‘half’ (adj.) | the middle’, epd. of dis- ‘apart’ and
30:23797:or‘a half’ have no connection with a nu- | medius ‘middle’ (12.37). From the lat-
```


## [2026-09-07T17:37:28.860Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== SYN 23792-23840 ===\"; sed -n '23792,23840p' SYN.txt"
}
```


### [2026-09-07T17:37:28.904Z] TOOL RESULT

```
=== SYN 23792-23840 ===
QUANTITY AND NUMBER 935 13.24 HALF (Adj. Except as Noted) ‘ Goth: halbs Lith. pusé (sb.), pus- ysos TH ON _ halfr Lett.  puse (sb.), pus- pias st? aémi- Dan. halv ChSl. polit (sb.) dina a (sb.) Sw. halv SCr. 70 (sb.) mea; ib (sb.) OE healf; sim- Boh. _ poloviént; pil (sb.) a mitad (sv-) ME half Pol. polowiczny; pot (sb.) a Wis (sb.) NE half Russ. pol-(polu-) th (sb.), leth- ae el rea ardha-; sami- | , 4 alp; sami- : é It. oath (sb.), leath A eas Vv. naéma- | hanner NHG  halb
hanter
rast to the words for ‘a third’, 2. Lat. dimidius (VLat. dimedius >
ts fourth’, and other fractions, which are Fr. demi), orig. (with pars) ‘divided in
qlinumeral derivs.. those for ‘half’ (adj.) | the middle’, epd. of dis- ‘apart’ and
or‘a half’ have no connection with a nu- | medius ‘middle’ (12.37). From the lat-
meral, ‘There is an inherited group | ter, It. mezzo, Sp. medio, and through
hich probably rests on the notion of a | sb. Lat. medietés ‘middle, center’ and
single or even division, and in Latin ‘di- | ‘half’, It. meta, Fr. moitié, Sp. mitad.
vided in the middle’ was ‘half’. Other Ernout-M. 601. REW 2644, 5461.
ords, some of them used also for ‘side’ Rum. juméitate (sb.), fr. Lat. medietds
and some cognate with verbs for ‘cut, | or dimidietas, with peculiar phonetic de-
divide’, etc., must have gained the | velopment. Tiktin 879, Elementarbuch
meaning ‘half’ through specialization of | 208. Densusianu 295 f. (assuming blend
‘part, division’. with a loanword fr. Alb. gjysmé ‘half’, f
1, IE *sémi- in epds., prob. with ref- | this fr. Grk. Hous).
tence to a single or even division : TE | 3. Ir. leth (‘side’ and ‘half’), NIr.
a eee ete., io Cale duds, Skt. | leath (fem.: ‘side’, masc. ‘half’), orig.
reat an “at saute semel | ‘side’ : Lat. latus ‘side’ (12.36). Hence
Misa deus: of the Walde-P. | for adj. mostly epds. with leth-, leath.
with *sem-, ete . Er ° oe eine W. hanner, Br. hanter, see above, 1. Tk, mie in apie ae ‘ 921 f. i 4, Goth. halbs, etc., general Gmce.,
‘b. ‘a half’, then ee dj. (cf Gene ane: perh. (as orig. ‘divided’) : Lat. scalpere
aro), Att. fuious (a an re ‘ TS Ble ‘cut, carve, scrape, scratch’, Lith.
San dink ae dae tee | seernmlts how, of smooth, polish’, Grk.
#8), Cret. sutva, gb, oh inti (*hutt- | oxéroy ‘pointed stake’, ete. Walde-P.
cs ee > NG | 9.595. Falk-Torp 375. Feist 239.
B, O8 eam 0 ee a, sb. ; Lat. semt-,
tpds, ’ sami-, Skt. sami- in
In cont
5. Lith. pusé, Lett. puse sb. (with gen.), also freq. Lith., Lett. pus- in epds. : OPruss. possisawaite ‘mittwoch’, esse ... pausan ‘on the part of’, Toch. A posi Gk. en a and sb. (fr. *s7t-tero-) : ‘side, wall’. Mihl.-Endz. 3.426. Fraen- ; V aE repos ‘one or the other | eh IF 50.229.
(vith dierent lic. Pedersen 1.138 | 6. ChSI. polit, SCr. po (dial. pol), Pol. Toot connection). pot, Boh. pil sbs., Russ. pol- (in epds.
Of Sim} : hannep pula ultimate orig. prob. W.
Br, ie and sb. (in cpds. haner-),
Wo?
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
936 SELECTED INDO-EUROPEAN SYNONYMS
only in nom. and ace. with gen. of sec- ond member, in other cases polu- with second member regularly inflected), also adjs. Boh. polowiént, Pol. potowiczny; Slavic polti ‘half’ = poli ‘side, shore’ (cf. above Ir. leth ‘side, half’) : ChSl. ras- platiti, OHG spalian ‘split’, Skt. spdtaya-
‘split’, etc. Walde-P. 2.678. Miklosich 256 f. Briickner 429,
7. Skt. ardhd-, beside sb. drdha- ‘side part, half’ : Lith. ardyti ‘divide, split? ete. Walde-P. 1.143. Uhlenbeck 14.’
Av. naéma- (NPers. ném) : Skt, nema- ‘the one, the other’, also ‘half’, orig. dub. Barth. 1036. Uhlenbeck 151.
13.31. NOTE ON THE NUMERALS
No class of words, not even those de- noting family relationship, has been so persistent as the numerals in retaining the inherited words.
Except for some suffix-variation and actual substitution in the case of ‘one’ (13.32), the IE words for ‘one’ to ‘ten’ have persisted everywhere with only slight changes other than phonetic; like- wise the IE word for ‘hundred’, while for ‘thousand’ there are several different groups.
The ‘teens’ are expressed by cop. epds. of the digits with ‘ten’, with the ex- ception of the Gme. words for ‘eleven’ and ‘twelve’ (Goth. ain-lif, twa-lif) and the whole Lith. series (viento-lika, dvy- lika, try-lika, keturio-lika, etc. for 11-19), which are cpds. with a form of IB *leikv- ‘leave, remain’ (Grk. del, etc., Walde- P. 2.396 f.), hence orig. ‘one over’ (the ten), etc.
For 20-90 certain IE epds., the sec- ond part of which seems to be obscurely related to the numeral for ‘ten’, have been partly retained (for 20 Grk. etkoot, Dor. fikart, Lat. viginit, Skt. viricati-, etc.; for the others Grk. -xovra, Lat,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
— ee
-ginia, Skt. -gat-, etc.), and partly re- placed by more transparent phrases or epds. (as for 20 Goth. twaz tigjus, OB twen-tig, Lith. dvi-deSimt, Rum. doud- zect),
```


## [2026-09-07T17:37:29.684Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== POK_01 4620-4680 ===\"; sed -n '4620,4680p' POK_01.txt"
}
```


### [2026-09-07T17:37:29.735Z] TOOL RESULT

```
=== POK_01 4620-4680 ===
air.  eterj  etir,  etar  , zwischen',  adnom.  m.  Akk.,  corn.  ynter,  yntre,  bret. entre  (der  Endvokal  nach  tre-j  dre  =  cymr.  trvjy),  acymr.  ithr  ,inter';  gall. inter  ambes  ,inter  rlvös';
ahd.  untar  usw.  ,unter  =  zwischen'  ==  osk.  anter  (verschieden  von germ.  *under,  ahd.  usw.  untar  ,unterhalb'  aus  *7j,dher^  lat.  infrä)]  vgl. got.  undaürni-mats  ,Zwischen-mahl'  =  ,Frühstück',  anord.  nndorn  n. ^Vormittag  (um  9  Uhr)',  as.  undorn,  ags.  undern  ,Mittag',  ahd.  untorn ^Mittag,  Mittagessen'  (n-Suffix  wie  in  lat.  internus)]  hochstufig  wie  ^v. evrsQa  usw.  anord.  idrar  Fl.  , Eingeweide'  (aus  ^innrar,  *inperöz),  innre, idre  ,der  innere'  (wenn  diese  nicht  spez.  nord.  -?'o-Ableitungen  von  inn  = got.  inn  ,hinein',  s.  oben,  sind);
314
slav.  *^tro  in  aksl.  jqtro  ^Leber^,  ablaut.  gtroba  ,v.oilLa'j  gtrb  ^eiaw^ über  hitt.  antüinias  ,interior' ,  andurza  ^drinnen'  s.  Lohmann  I.  F.  51^  32Qf entös  /von)  innen^  (vgl.  ai.  i-tdh  ^von  hier^^  lat.  caelitus  usw.): gT.  h'zög  ^innen^;  wovon  evxoa-^ev^  -d-L  und  weiter  ivröad^ia,  ivroad^l^. , Eingeweide^  (oder  letztere  mit  aus  evroad-s  verschlepptem  -d"  für  *ivToancf vgl.  ai.  antastya-  n.  ^Eingeweide^,  Fick  I*  363^  Vendryes  Rev.  et.  gr.  23* 1910,  74);  '      '
lat.  intus  ,von  drinnen;  innen ^,  davon  mit  analoger  Umgestaltung  intestina' mnd.  nhd.  dial.  inser  ^eßbare  innere  Teile  von  Tieren',  anord.  istr  n tstra  Lj  ,das  die  Eingeweide  umgebende  Fett^  (*en-s-tro-);
apr.  instran  ,Fett^,  lett.  tstri  PL  _,Nieren^  (*en-s-<ro-) ;  lett.  leksa  ^Inneres'  pl  . ,Eingeweide^  (*'en-t-{a),  alit.  inscios  ,Herz^,  lit.  {scios  , Eingeweide^  {*en-s-t{o\ Über  die  Zusammenrückung  lat.  endo,  indu,  wozu  gr.  t«  evdiva,  air. inne  ^Eingeweide^,  s.  oben  S.  182  —  Über  gr.  bv-öov  ,*im  Haus^  (wozu evdo-d-av,  -i9-t,  lesb.  dor.  evdoL  nach  OL-KO-d-sv,  -&Ly  ö'iy.ol)  s.  dem-  ,bauen' WF.  I  125  ff.,  II  335  f.,  WH.  I  687  f.,  694,  708  f.,  711  f.,  870,  Traut^ mann  69  f.,  198  f.   W.  Schulze  Kl.  Sehr.  70  ff.  t^.^
2.  en-  jjahr'.
Gr.  evog  ,Jahr'  Hes.,  unsicher,  ob  m.  oder  n.,  dl-evog  , zweijährig*,  rer^a-  " Evrjg,  -sg  ,  vier  jährig*,  hom.  Akk.  Sg.  '^vlv,  Akk.  PI.  iv'ijg  ,  jährig*,  TtgrjT-rjy , einjähriges  Lamm*  (zu  dor.  nqäxog  aus  *p.r^os?);  h-LavTÖg  ,Jahr'  (zu laveiv:  ,wenn   das  Jahr  ruht,  Jahreswende*??).  ^»y-
Tiefstufe  -n-  in:  .1-,
got.  fram  fair-n-in  jera,  SiS^  fer-n-un  gere,  mhd.  verne  ,im  vorigen  Jahre'j
lit.  jper-n-ai  ,im  vorigen  Jahre*,  lett.  p§rns  , vorjährig* ;  '""5^
russ.  dial.,  cech.  lo-ni  (^ol-ni)  , letztjährig*.
Specht  Dekl.  16  stellt  dazu  das  Pron.  en  in  gr.  evrj  , jener  (Tag  oder jenes  Jahr*?).
Schwyzer  Gr.  Gr.  I  424  mit  Anm.  5,  Feist  140  f.,  Specht  Dekl.  15  f.
en  ,siehe  da!^  '
Gr.  ^V,  ijrjVj  lat.  en  ,siehe  da!^ WP.  I  127,  WH.  I  403  f.
I.  {enehh-),  emhh-,  ombh-,  nobh-  (nebh-?),  rpbh-  ,NabeP,  mehrfach  mit i-Formantien. Ai.  ndbhya-  n.  ,Nabe^,  nähhi-  f.  , Nabel,  Nabe,  Verwandtschaft^,  näbhlla- n.  (unhelegt)  ,Schamgegend,  Nabelvertiefung';  av.  nahä-nazdista-  ,der  ver-  ' wandtschaftlich  nächststehende',  daneben  mit  ar.  ph:  av.  näfö,  npers.  näf ,Nabel';
315
oT.  dficpalög  (Nom.  PL  auch  o^LcpaUg)  ,Nabel,  Schildbuckel',  wohl  auch }j^i(pa'Asg  ;die  unreifen  Weinbeeren  oder  Oliven  oder  andere  Früchte'  (als nabelartig  vorgestülpte  Knöpfchen),  d^cpa-ug  ,der  Kelch  der  Eichel;
lat.  umbillcus  ,Nabel',  umhö,  -önis  , Schildbuckel';
air.  imhliu  ,Nabel'  {*emUlön-),  mir.  imlecan  ds.  (ein  Versuch  zur  Suffix- erklärung bei  Pedersen  KG.  I  495);
ahd.  nahüj  ags.  nafu^  aisl.  nof  ,Radnabe'  (auch  in  ahd.  naba-ger,  ags. nafu-gär,  aisl.  nafarr  ,grober  Bohrer'),  ahd.  nahalo,  ags.  nafela,  aisl.  naß ^Nabel';  dazu  nach  Liden  KZ.  61,  17  ahd.  amban,  amhon,  m.  (o-St.) ^Wanst',  as.  dmhön  ,abdomina',  Nom.  Akk.  PI.  eines  m.  ow-St.  (germ. ^amhan-,  idg.   *omhhon-)]
apr.  nahis  ,Nabe,  Nabel',  lett.  naba  ,Nabel'.
Vielleicht  hierher  ags.  umbor  ,kleines  Kind',  auch  der  ital.  VN  Umbri (*mbh-),  anderer  Ablaut  im  germ.  VN  Ämbrones  {*ombh-)  anders  Kretschmer Gl.  21,  116  f.
WP.  I  130,  EM  1122,   Specht  Dekl.  100.
2.  (enebh-):  nebh-,  emhh',mhh-  (Kontaminationsform  nembh-);  z.T.  emb-, omb-  aus  embh-,  ombh-  , feucht,  Wasser',  daraus  ,Dampf,  Dunst, Nebel,  Wolke'.
nebhos- :  ai.  ndbhas-  n.  ,Nebel,  Dunst,  Gewölk,  Luftraum,  Himmel', daneben  Wurzelflexion  im  dehnstuf.  f.  Plur.  ndbha/i(?)]  av.  nabah-  n.  PI. ,Luf träum,  Himmel';
gr.  v€g)og,  -ovg  n.  ,Wolke,  Nebel'  (Denom.  primärer  Form  ^vvvecpSL  ,es  um- zieht sich',  ^vwivocpe  ,es  ist  wolkig');
auch  (s.  u.  nem-  ,biegen')  air.  nem  (n.  es-St.),  nir.  neamh^  cymr.  com. nef  , Himmel';
abg.  neboy  -ese  n.  , Himmel',  zum  i-St.  umgebildet  in  lit.  debesis  f.  und  m. , Wolke'  (aber  alter  konson.  PL,  z.  B.  Gen.  PL  debesy,\  d  für  n  durch  Ein- fluß von  dangüs  , Himmel');
hitt.  ne-pi-is  (nebis)  n.  , Himmel'  Gen.  nebisas;
mit  i-Formans  (nebhelä):
gr.  vE(pilv  ,Wolke,  Nebel',  =  lat.  nebula  ,Dunst,  Nebel',  Wolke';
aber  air.  nel  m..  Gen.  niuil  ,Wolke,  Nebel'  nicht  aus  *nebhlo-,  sondern Lehnwort  aus  cjmr.  niwl,  nificl,  ncorn.  niul  ds.  (die  wiederum  nach  Lotli RC  20,  346  f.  Lw.  aus  spätlat.  *nibulus  für  nübilus);
ahd.  nebul  m.  ^Nebel',  as.  nebal  ,Nebel,  Dunkel',  ags.  nifol  ds.,  aisl.  nifl- heimr  u.  dgl.,  njöl  ,Dunkelheit,  Nacht'  (germ.  *neila-  und  *nibula-  aus -elo-j  aisl.  nifl-  aus  *mSi7a-);
unsicher  ai.  nabhanü-  m.,  nabhanu-  f.,  wahrscheinlich  ,Quelle';  av.  aiiixi-
316  ^
naptlm  asti  ,er  (befeuchtet  =)  besudelt  mit  Blut',  napta-  , feucht'  {*nah-ta-) npers.  neft  ,Najphtha' -^  ,^
vielleicht  hierher  lat.  Neptünus  ,Gott  der  Quellen  und  Flüsse,  dann  des  "f
Meeres'  aus   *nebh-tu-s;    des  -p-  im   skyth.  FIN  Naparis,  apers.  Quell  ^  '' NdTtag  stammt  aus  iran.  apa-  ^Wasser,  Quelle'  (Brandenstein,  OLZ  1940 435  ff.).
inbb-(rO'):  g
ai.  abhrd-  m.  ,trübes  Wetter,  Gewölk',  n.  ,Wolke,  Luftraum'  {*7ribhros)  "
av.  avrra-  n.  ,Wolke';  fern  bleibt  wegen  der  Bedeutung  gr.  dq)QÖg  ,Schaum'  ■
(Meillet  BSL  31,  51);  k
in  die  i-Dekl.  übergetreten  lat.  imher,  imbris  ,Regenguß'  =  osk.  Anafnss  -•,''
wohl  ,imbribus'.  .:
Hierher  auch  die  Flußnamen  gall.  *Ämbräj  mcymr.  Amir,  Amyr  sowie  -l nhd.  Amper  und  Ammer  (kelt.  *  Ambra),  Emmer  (kelt.  *  Ambria)]  dazu  auch
engl.  Amber -^    frz.  Ambre,   Ambrole]    span.  Ambron,  Ambror-,    ital.  Ambi-a  '
Ambria,   Ambro,  Ambrio   usw.,  letztere  sind  bestimmt   ven. -illyrisch;   vgl.  ^
ohne   formantisches  r  gall.   inter   ambes    ,inter    rivos',    ambe    ,rivo',   abrit.  "^'
Amboglanna   ,Ufer  des  Stromes',   sowie   arm.  amb    und   (mit   idg.  b)  amp  .^j
,AYolke'.  X
emb{h)-  :  omb{h)- :
ai.  ämbhas-  n.  ,Regenwasser';  ambu  n.  ,Wasser',  gr.  ^iißqoq  m.  ,Regen'
(zum  b  vgl.  oben  arm.  amp  und  Schwyzer  Gr.  Gr.  I  333) ;  hierher  auch  lak.  J;
di.iq^ä  , Geruch,  Hauch',  arkad.  si)Oi.i(pog  ,wohlriechend',  usw.  jj
nembh-:  ^^
pehl.  namb,  nam,  npers.  nem  , feucht,  Feuchtigkeit',  pehl.  nambltan  ,be-  W^
feuchten' ;  ■^^■_
lat.  nimbus  , Sturzregen,  Platzregen;  Sturmwolke,  Regenwolke'.  '5-
WP.  I  131,  WH.  I  681,    II  151  f.,   Specht  Dekl.  16f.  %
```


## [2026-09-07T17:37:42.208Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== PHD nem ===\"; grep -n -E '\\bnēm\\b|nemag|nēmag|nem ' PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB nem ===\"; grep -n -E 'nēm|nem\\b' NYB_vol2_glossary.txt | head -20\necho \"=== SNS nem ===\"; grep -n -E 'nēm|nem' SNS_pages.txt | head -20"
}
```


### [2026-09-07T17:37:42.286Z] TOOL RESULT

```
=== PHD nem ===
PHD.txt:510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
PHD.txt:3516:satisfaction hupassandagih, sahišn, šnēmag.
PHD.txt:5212:wigrad wigridan nerang n��rógómand nerog nilopal nirmadomand nirmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
PHD_mackenzie.txt:3704:nem [PRG < A plg; nym I = M, N --] half.
PHD_mackenzie.txt:6408:direction kust(ag), nemag, ron, sog;    doer kardar, kunisngar.
PHD_mackenzie.txt:7569:sesame kunJid.                          . side alag, karan, kust(ag), nemag,
PHD_mackenzie.txt:8797:nem    I                       ... leu    pcskar, pesyar       '\... !"U-'V
PHD_mackenzie.txt:10181:zanihT                ~~,              nemag                     l.w,
=== NYB nem ===
672:= Dūrēsrav bé 6 Zartušt guft ku: cigēn-at fratom ham (cf 209 ete.) bahr u rocik be apakand hom, an tč an (v. lan and ?an) har 2 aš apar barom api-t bē marnjēnēm "D. said to Z.: because thou hast deprived me, as the first, of both munistry and food, we both, thou and I, shall be enraptured in an ecstatic vision, and then I shall annihilate thee’.
1097:~ drang $ ..., ~ ... drang for as lang a time as 54?-6.10-11; as big, as tall as 568; and ~, hàn and ~~, v. and. — 3. indefinite: some, with the sg. just as the numerals: ~ rūc some days 219; 505. 5418; ~ 4 nem rēc about half a day 31"; ~ tài, ~... tak; v. tak; ham ~ hàn sāk just as much tribute 1218 (= NP candän). — Av. (600) c(a)vant-; MPrth cwnd, Bal. cunt; MPrs cnd; Paz. NP cand. — V. also écand.
1184:danistan [YD‘YTN-stn'] dan-, Ist p. sg. danem [YD‘YTN-ym] 21? or danam [~- m] 2819-20, 2nd p. sg. dane [YD*YTN-yh, -y, -yd; d’nyh 41]; cond. 3d p. sg. dänist häh 321: to know, with kū ‘that’ or in- troducing direct speech 2% etc. passim; with indirect interrogative clause in- troduced by ki: ki cand how many 213-4, ku katäm who 21°, ki cé what 218. 305, ku ... atvāp whether ... or 2022-23;
1763:hāciš [hes], Ps. aei$ [Pcšy] adv. of hac 1. used instead of hac to refer back to an encl. pron. in the beginning of the sentence: -§ mà sax%van ~ pursét do not ask him any questions 74%7. 765-§; han gu ke-š Gayomart ~ the clay of which G. was (made) 9516; hamäk cis ké-§ martömän rämisn ... ~ all things in which men take pleasure 10029-21; api-§ purr aciš and full of it 12815-16; — referring directly to a preceding rel. pron.: ctš-ē ke ziyan nem šāyist butan something from which no harm
2338:amäh-ic bē danem ku sap hast aivāp rēc that we know whether it is night or day 2022-28; rast gob ku to hac fradandān i ke hah tell frankly of whose children thou art 1517-18; 2120; 2518-19 etc. passim. — MPrthPrs kw; Paz. ku; Av. (472) ku, cf (473) kuta.
2401:pret. pass.: ~ en dam dāt 10312313 (on 3%: ~ kart AWH-wm v. s. v. k- and -m); — my: a) izdfat + ~: kanicak i ~ 7!; b) placed before its headw.: cif i ~ fradandčin the conditions of my children 559; Hamāk i ~ duxt 261; ē (lo) ~ pit u € ~ brat 10018; c) definite rel. attr.: ēt i ~ zan 3215; õi 4 ~ mart i ahlav 3914-15, Ot i ~ pus 5118-19; elliptically: han i ~ my house (family) 3717-18; én i ~ my religious duty 535; — after prepositions: apük, apar, hac, 6, pat ~; ~ rād. — 2. the form normally used as the cas. rect. ‘I’: man Šāhpuhr hom 1514; ~ dānēm 21? etc. — 98° STHn-yt' (imp.) L: if an imp. has
2674:peš ~ i before 3616, 4118, cf Av. (132) antarāt naēmāt + gen. of a temporal w. ‘within’. — V. nem.
2675:nem-röc [nymlwe'; PRG YWM] midday 718.28, 675, 9611; — south 11521. 12011, — MPruhPrs nymrwz; NP nimrüz.
2816:the Man. texts). The pres. forms "wnyt', ’wnym = nët, onem are only found in some MSS, and wanting in most; they
3131:pēš [pyš; L'YN!, inser. and Ps. L'YNY] l. adv. before, earlier 97°; first, opp. pas, in a sequence 5718; ~ hac before: 912, 1274, 382, 392, 493, 652°, with a v. n. or an inf. instead of a temporal clause 4618, 5423; ~ ki 81. 1317, ~ hac han-tčit [ZK *D] ka 98% conj. before; dvārtšn 6 ~ to run forwards, opp. dvarišn 6 pas to run backwards 6811; 6 ~ + dar, matan, Sutan, z"àstan, v. these ws.; 6 ~ raft, tacit went, ran ahead, to the front 4918.19; ēn 4 6 — góbam what I am going to say presently 517-8. 541%, — 2. prep. before, regularly followed by the izafat: 7 sül peš <i>» hàn 7 years earlier 40°; þe- fore, in the presence of 23-15, 521, 7021, 9876; for the protection of 49%; without "the izafat HajB:5; 269; referring back to an encl. pron.: api-š Tos — ēstēt and T. will stand before him 1004; — with vbs. of motion, addressing etc., often 6 m: 619, 1015, 1] 15-19, 1316.23, 1510-11, ete, — ~ n&mak, hac ~ némak, v. nēmak; as first element of compounds, v. below. — OP prep. c. acc. patšiyā ‘before’ Beh. IV, 91, according to the last revision of the
3326:rče [YWM; lwc] day, pl. cas. obl. —-än [Iwe?n'] 2720; contrasting with gap ‘night’ 45, 2023; ka ~ būt when day was dawning 635; im ~ to-day 10, ete.; fratük ~ to- morrow, v. fratāk; nem ~ half a day 317, v. also nem-röc; hac im = tāt 3 — within three days counting from to-day 519; — m šapān 329. 728, 7417 [all lwc]. 989-109, 1203 (YWM šp'n'], röcak šapān 742°. 1011: the astronomical day of 24 hours (Swed dygn, Russ sutkt). — The names of the days of the month are in BP: 1. Ohurmazd. 2. Vahuman. 3. Art-(Urt-)
3434:are illustrative of the difficulty of writing the phonem sih phonetically.
3689:tacitan [teytn'] to run: api-m cand 4 nem roc pat pušt hamé tacit hom (for tacit-om) almost half a day (he was run after by me =) I ran after him 311? (cf s. v. kar- tan); be tacit pat oš han mat *cautiously (v. s. v. 68) his mother ran to him 48?9, 217.49 5019; pčš tacit ran before, got ahead (of the others) 494-19, — Av. (624) tak-; M Prth tc-; MPrs čz- (S); Paz. 0ajü for tazak (tajäk; Aog. 77); Verbum 169; Ghilain 50. Cf täxtan.
3818:tuvän [twb?n'] 1. adj. mighty, powerful, energetic 559. 6619; subst. what one is able to do, v. s. v. sämänihä. — 2. impers. vb.: it is possible, one can, is able to; the subj. is an encl. pron., or a subst. in the cas. obl., or a form felt as a cas. obl.; construed with an inf., which is generally placed before, less often after ~; pret. ~ būt; a) without a subj.: 6 x¥és kartan nem 9?" ; griftan ne" (ef s. v. Säyistan) ete.; — b) with a logical subj.: man zatan nē ~ I cannot slay him 99%; man zivistan ne ~ 1035-5; api-tan griftan ne ~ 7%; ete.; ka-tan ~ when it will be possible for you 911; šmah xvēš rād ne ~ x"astan 452-3, v. axtäyisneh; aš pād i man... apar daštan ne ~ büt he was not able to „.. 3318-19. 48-8 2-5 vicārtan nē ~ 11912; cand-šan ~ dätan as much as they pos- sibly can 79%; apäc daštan ke ~? 247; martömän ... ayaftan u dānistan ne ~ mankind cannot ... 804-5; 10926-??; duš- man pat dušman hin nē ~ kartani... 414-15, 619-20. Pēc kas vicārtan ne ~ būt 11921. — From Av. (638 sg.) tav-; MPrs twn; Ps. twb?n-; Paz. tuq, tva; NP tuvān, tavān; cf tāyītan and tahé-kar.
3847:ulēh [L’L’-yh], wë [+ -c: D’L’y-c] up- wards, above: pat uléh emphasizing the prev. ul in pat uleh ul nikérit 51%*-*%; pat uleh ul vāzēnēm 60°; — ule-c on high 42). - Cf Av. (351) loc. orodvaya ‘in upright, standing position’; cf also nıküneh.
4059:vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
4081:[vēcak [wyck'] lot, share, portion ; combat (as if it were a casting of lots between the combatants): rasnik ~ pitched battle FrP 14; v. nem-vecak. — From !vertan; Arm. lw. vičak ‘lot (e. g. in casting of lots), portion; position; fate, possession, dio- cese’; Ps. wyc ‘priest’, wycyhy ���clergy’].
4106:iyöxtan [*NDYHWN-tn'] vēc- (vinj-, v. below) to detach, to separate, to sift, to remove: di véxt šusr his sperm was de- tached from him, with the gl. kū-š Suhr pat post ul Gmat that is: his sperm broke through his skin 5419-29; ātaxš haciš nē šāyet véxtan the fire (hidden in the plant) cannot break forth (from it) 95! (gl.); api-š hösak vest u hošet and its ears having been torn off (by the wind) it withers 12814-15 (uncertain, v. note below); v. also vecisn. — Av. (1312 sq.) vaék-, pres. vaéca-; Skr vic-, pres. vinakti ‘to sift, to winnow, to separate; to inquire, to con- sider’; Arm. lw. wié-em ‘to dispute, to debate’, več ‘discussion’, vičak, v. večak; Bal gécag ‘to sift? < vēc-, gécin, gēšin ‘sieve’ (Makrani, v. Geiger); NP béxtan bez- ‘to sift’. The pres. vinj- is only attest- ed by Cod. K in FrP 18: wync-, but read vij- = the other MSS; as this vb. is al- ways written ideographically in the texts the existence of vinj- in BP is not fully ascertained. However, Psht has winjal ‘to wash, to cleanse’; traces of vinj- in NP are perhaps bunjak ‘carded cotton’ (« *binjak < *vinjak); banjidan (for *binj-) ‘to cut to pieces’ (Steingass); possibly banj ‘one of two women who share a common husband’ < *vincä-, cf vēcak and nēm-vēcak. — [Note: — The Phl translation of 12814-15 is based on a Syriac text which is guite as obscure as the Hebr. original: 'grass on the roof which, as soon as the wind blows upon it, šālef and it withers’. The vb. ŠLP means ‘to extract, to pull, to draw a sword’, so the senses ‘to dry up, to languish’ and ‘to shoot up, to form blades and ears’ seem to be simply conjectured from our Ps. verse. Evidently the Prs. translator took Syr SLP in its ordinary sense ‘to extract, to pull’, and tried to make sense of its Phl. equivalent včatan to the best of his ability. He needed an obj. for it,
4790:Schwarz, Iran = Paul Schwarz, Iran im Mittelalter nach den arabischen Geographen. 9 Bde, 1896-1969. In einem Band Hildesheim-New York 1969 + Ergánzungsband 1970. 4
4966:Airyanem vaščjo: Eran- včj
=== SNS nem ===
11527:                                                                                                                                                        —J- «^x*i f*i:nem:
16350:Sand-is 195/11            cisan 158/3                   danem 78/19               dahend 294/13
```


## [2026-09-07T17:37:43.738Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== ISS_alt_DKS nok/nul ===\"; grep -n -E 'nokh|nuk|nūk|beak' ISS_alt_DKS.txt | head -30\necho \"=== AHD watkins neb ===\"; grep -n -E 'neb-|nebb|nib\\b|nipple|nibble' AHD_watkins1985.txt | head -30"
}
```


### [2026-09-07T17:37:43.826Z] TOOL RESULT

```
<persisted-output>
Output too large (38.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/by486py8i.txt

Preview (first 2KB):
=== ISS_alt_DKS nok/nul ===
854:агг-, later ár-, participle árrda-, later arda- 'to grind’, Sid. 150v5 йсі jsa ārrāñä ' it is to be ground in water’, BS jala- pista-, Tib. čhu dags-su byas-pa (hthag-ba ‘о grind"); п 71:6, 2 plur. imperative, ganam và bisa bisai arryará 'grind the corn in the house’; participle ш 93:264 árrdá hauska ysálva ' ground dry barberry’; 1 145, 53v5 nauká araña, BS dapaya; 1 175, 93r2 hà nauka атаа. See also āda- ‘flour’, and ñada- ‘small’. Base ar- ' to grind’, pres. *ат-пй-  ürr-, *arnata- ürrda-, to Av. -arana- in yao- arana- ' grinding tool, pestle for grain', Zor.P. gloss yav- artük-arak ('lg), N.Pers. yávar, уйт; M.Parth.T. yw'rd'so ‘grain’, Zor.P. yav-artak ‘all grains’, from yava- ‘grain, barley’ and artā-ka- ‘ground’, Zor.P. artan (THNTWN), Baxtiüri ardan, Yazdi ōrotvūn, Gazi йтйе ‘һе grinds’, Pašto anal, participle Av. afa-, anaša-; Orm, ё1-, hal-, hinl- (*rnya-}, Iškāšmī yunuk, Sanglēčīi yūn-, Šuynt yān-:yūd, participle упуј, Yidya yan-, уйп-:уйруі-, yir-, yür-, Bartangt yex-: yét£, Yazg. yawn-:yug. Second com- ponent in the words for 'water-mill'! *Avata-üraka- 'self-grinding', Waxi xaBürg, Suyni xedárj Yazg. xwayérg, Yidya xirgoh, Yayn. xutanna, Parati xëra ‘mill’, xēra-gir ' mill-stone', and Caucasian lw Сеќеп heri. For ‘small’, Zor.P. xv-artak, Armen. lw xortak, N.Pers. хита, xurdah, Pašto wur, wür (*rta-, IIFL 2:273), see also below ñada- ‘small’ from *ni-arta- or *ui-rta-. From *àrüra- or *arÜra- ‘mill’ derives Maima'i är ‘mill’, N.Pers. às, asya, ахуйо, üsyüb, Zor.P. asyük, asyap ‘mill’, with N.Pers. asyd-sang ' mill-stone', Kurd. ai ‘п’. IE Pok. 28-9 al- ‘to grind’, O.Ind. atta- ‘flour’, no verbal forms (*alió-, see T. Burrow, ВЗОАЗ 35, 1972, 539), Greek Абэ Чо grind’, dAerov ‘mill’, &Acap ‘four’, Armen. alam ' to grind’, aliur, aleur ‘four’, alauri ' mill’,
...
</persisted-output>
```


## [2026-09-07T17:37:50.739Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== AHD neb ===\"; grep -n -E 'nipple|nibble|\\bnib\\b|\\bneb\\b' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T17:37:50.788Z] TOOL RESULT

```
=== AHD neb ===
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
517:ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan in: a. Old English gnagan, to gnaw: GNAW; b. Old Norse gnaga, to bite, akin to the probable Scandinavian source of NAG!. 2. Suffixed Ger- manic form “gnag-sk- in *(g)naskon in Old High German nascon, to nibble: NOSH. 3. Perhaps related is Germanic *gnatt-, “biting insect,” in Old English gnzt, gnat: GNAT. [Pok. ghen- 436.]
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
768:[nabja-. Bird’s beak. Germanic root. Old English neb(b), beak: NEB, (NIB), (NIPPLE).]
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
976:sneudh-. Mist, cloud. Latin nibés, cloud: NUANCE. [Pok. 2. sneudh- 978.]
```


## [2026-09-07T17:37:52.079Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== KLN neb/nib/nipple ===\"; grep -n -E '^neb,|^nib,|^nipple,|^nibble,|nebb' KLN_1966.txt | head -20\necho \"=== SKT neb ===\"; grep -n -E 'nebb|\\bneb\\b|nib\\b|nipple' SKT.txt | head -20"
}
```


### [2026-09-07T17:37:52.202Z] TOOL RESULT

```
=== KLN neb/nib/nipple ===
25084:neb,  n.  1)  the  beak  or  bill  of  a  bird;  2)  nose;  3) point,  tip.  —  ME.  nebbe,  fr.  OE.  nebb,  ‘beak, nose,  face’,  rel.  to  MLG.,  MDu,  nebbe,  ‘beak’, ON.  nef,  ‘beak,  nose’,  Du.  sneb,  snavel,  OHG. snabul,  MHG.  snabel,  G.  Schnabel ,  ‘beak’, OFris,  snavel,  ‘mouth’.  Cp.  nib,  nipple,  snaffle, snap,  snipe,  snow,  ‘a  kind  of  vessel’.
25085:Derivative:  nebb-ed,  adj.
25374:nib,  n.,  a  gentleman.  —  Probably  a  gradational var.  of  nob,  ‘a  person  of  high  position’, nibble,  tr.  v.,  to  bite  gently;  intr.  v.,  to  take  bites gently.  —  Prob.  of  LG.  origin.  Cp.  MLG.  nib- belen,  NLG.  nibbeln,  knibbeln,  gnibbeln,  MDu. knibbelen,  ‘to  gnaw’,  Du.  knibbelen,  ‘to  cavil, squabble’.
35695:snack,  n.,  1)  a  share;  2)  a  light  meal.  —  ME. snake,  fr.  snaken.  See  snack,  v. snaffle,  n.,  a  kind  of  bridle  bit.  —  Prob.  fr.  Du. snavel,  ‘beak;  horse’s  muzzle’,  which  is  rel.  to OFris.  snavel,  ‘mouth’,  OHG.  snabul,  MHG. snavel,  G.  Schnabel,  ‘beak;  face’,  MLG.,  MDu. nebbe,  ‘beak’,  OE.  nebb.  ON.  nef,  ‘beak,  nose’, Du.  sneb,  ‘beak’,  ON.  snipa,  ‘snipe’,  fr.  I.-E. base  *snab-,  ‘beak;  to  snatch  with  the  beak,  to snap’,  whence  also  Lith.  srtdpas,  ‘beak,  bill’.  Cp. neb  and  words  there  referred  to.
=== SKT neb ===
2335:broccoli.  (Ital.  -  L.)  Ital.  br^ctpHy sprouts ;  pi.  of  broccolc.  a  sprout.  Dlnib ofbroivo,  A  skewer,  a  shoot,  stalk.  — L.  fm* (Hs,  a  i»oint.
2512:Buah  (X),  a  thicket.  (Scand.)  M.  £, buvrM,  busk.  —  'D:iXi,  busk,  Swed.  buske,  a bush.shnib.  4>  Du  ^M  (whence  F.  bois)\ O.  II.G.^'/*jf ;  G.  btisch.
4005:Contiguous ;  see  Tangenib
5564:Dump,  an  ill  shapcn  [>iece. E.  dump,  a  clunib)'  lump,  a  L short  and  Ihick.  I^wl.  Sc  diimt,  to  tkca^ btiikc  with  the  feet:  Swcd.  dial.  str.  vt dimpa  |,siipiiic  durtipiH^,  to  lall  itow plump.  Ct.  I)u.  dompntu»»  a  gicAl  noK Ici-I.  dumpa,  to  thump ;  and  cf.  Thi dumpling,  a  kind  of  pudding A  small  aolid  ball  of  pudding;  du is  a  double  dimin.  of  dump  ^above).
9674:^diiey.  (Scand.)  Corruption  of  M.  E. kidnere,  kidneer;  nert  ia  also  used  alone. 1.  Here  kid  is  a  corruption  of  qtiid  or quitk  ;  cf.  prov.  E.  kite,  the  belly,  which  is the  same  word. « Icel.  kvi^r,  womb,  Swed. ^(d  {\.  S  rw'i'iNl,  the  wonib  ;  this  word  is cognate  with  Skt/ai/d/n.  the  belly,  womb, Gk.  yaar-iip,  2.  M.  E.  nere  is  also  a  Scand. word.  — Icel.  nyra,  Dan.  nyrc,  Swcd.  njure, a  kidney;  cognate  with  Da.  ni>r,  Q.niere^ and  allied  to  Gk.  vtfpp^,%.  kidney.
10887:Maggot,  a  gnib.  (W.)  M  E.  magpi ma^t.  —  W.  moi-fiad,  matai,  a  mi^i^ cf.  magiaid,  grubs.  Allied  to  W.  mapai breeding,  ma<^d,  a  brood  ;  from  magu^  (I breed,     Cf.  Bret,  and  Com.  m^fit,  to  feed
13186:pope,  the  father  of  a  church,  bishop  of Rome.   (.L.  —  Gk.)      M.  E.  poptx    formed from  A,  S.  fkifa,  pope,  by  the  usual  change from  d  to  long  0.-L. /a/a,  pope,  father: sec  papal  (above). Paper ;  see  Fapjma. Fapllionaceoufi ;  see  Parllion. Pupillary,  belonging  to  or  resembling nipples  or   teats,   warty.    (L.)      From   L. papilla,    a    small    postule,    nipple,    teat; dimin.   of  papula,   a    pustule. -t*  Lithuan. pdpas,  a  teat,  pampti,  to  swell  out ;  Gk. woM0(^,  bobble,  blister.    (VPAP.  to  swell ont )    Sec  Pintple.
16209:Rose,  (L.-Gk.-Anib.)  A.  S.  Mr^.- L.  tosa ;  borrowed  from  Gk.  ^^ov,  a  rose (whence  a  form  ^/a*  —  rosa)\  ./EoUc ^/mSJ$o»'.— Arab.  UHirJ,  a  ro*e.  Der.  rhodo- dendron (Gk.  iivZpov,  a  Irec).  •*
17216:brig,  to  nib  with  r  brojidi  of  a m  A.  S.  /<•«*,  a  shrub.  Cf.  E. the  shnib  so  called;  Lowl n^r,  *o  liandful  of  heath  tied
17602:neb.  beak,  nose.  (E.)  M.  E.  neb,  face. A  S.  neMi,  face.^Du  R<^,bill,  nib,  mouth ; Icel.  ntf,  nose ;  Dan  nab ;  Swed.  nahb. p.  Put  for  smb  • ;  cf.  Da  /«/i5.  bill,  beak  ; G.  schneppi,  nozzle;  G.  srhnaUL  bill. M.  H.  G.  tftabil,  from  M.  H.  C.  sftabtn,  to «p.  Y*  Ilcncc  sm^  is  for  m€p*\  from the  vetb  u  snaf.
17604:nib.  point  of  a  pen.  <E,)  Aootbcrlba of  neb ;  see  above.
17605:nipple,  a  teat.  (£.)  Formerly  «< (PaUgravc) ;  dimin.  of  nib  or  iw;  s above.     Dor.  nippU-wort.
17763:make  glasses:'  Florio,     Fern  of  Ital.  rnib,
18975:Swerve,  to  tuni  aside.  (E.)  M.  E. Tweruen  (^swervtn').  A.  S.  sweorfan,  pi.  t. nc^arf,  pp.  ntfof/en^  to  nib,  hie,  polish (hence  to  move  swiftly  lo  aiid  fro,  to  turn aside  in  movingV^-Ou.  sntftrvtH,  to  swerve, waiulcr,  not.  rove :  O.Sax.  swcrifun,  to  wipe; O.  I'ries.  rojerva,  to  creep;  \ctLsvtrfa  ^pt, t  svarf),  lo  file ;  Golh.  btxwairUan.  lo  wipe. p.  The  particular  sense  appears  in  Dan. dial,  wirre,  to  move  to  and  fro,  lo  swcr\'e, lo  tuni  aside;  cf.  Dan.  svirre^  to  whirl round,  svire,  to  revel,  svarre,  rvarbe,  lo  turn in  n  lathe.  Swed.  svirra,  to  murmur,  svarjva, to  turn  in  a  lalhc.  From  ^SU  AK,  to bum  (see  Swarm):  whence  the  senses  to whirl,  tu  work  to  and  fro,  wipe,  rub,  file,
19188:Tardy.  (F.-L.)  F.  tardif  tardy.  (CC ItaL  tardivo,  tardy.)  From  L.  tardmTt slow ;  with  suffis  intts.  Allied  to  iererf, to  nib,  also  to  wa^te  time.     Sec  Trite,
19262:Teat,  nipple  of  the  female  breast  (E) Also  tit.  M.  E.  tet€ ;  also  tette^  tittt.  K.%. tit,  a  teat ;  pi.  tiftat.  -|-  0,  Du,  tittt  x  G. zitu.  Cf  also  F.  tettt.  Span.  <r/*i.  lul tetta,  all  of  Tcau  origin.  Also  W.  MM, did,  a  teat.  tAs  if  from  on  Aryan  l>4«( DI.)  %  Distinct  from  W.  teth.  G.  tiiUi, Gk.  Th9Tf,  TiT^j,  a  tcMit,  which  appear  lo be  allied  to  Skt.  dht,  to  ^uck.  Goth.  daddjM^ to  suckle.
20197:Trite.  (L)  L.  tritus,  worn,  pp.  of  tir- tre,  to  nib,  wear  away.  +  Kius.  ttrtU, Uth.  triti,  to  nib.     (V  TAR.)
20198:attrition.  (F.  -  L)  F.  attrition.  - L.  ace.  attritiatifm,  a  robbing  or  wearing away.  •-  L.  attritus^  pp.  oi  aitereri,  to  nib away.  —  L.  d/-  <aJ)  \  tertre,  to  nib.
20199:contrite.  (L)    L.  r<7n/ri/ur.  thoroughly bniiscd;    hence,   penitent;    pp.  of  L.  ivm- ttrere,  to  nib  together,  bnii«e. detriment  (F.-L.)     O.V.  detriment.
20203:try,  to  iclectt  test  examine,  &c.  (F  — L.)  M.  E.  trien,  to  select,  pick  out,  choose. The  same  as  Prov.  trior,  to  separate  com from  the  straw.  aUo  to  choose.  —  Low  L. tri/are,  to  thredi.  —  L.  tritus,  pp.  oi  term, to  nib.  It  meant  to  thresh,  separate,  purify, GuII,  piok,  &C.     Der.  tri-al.
```


## [2026-09-07T17:38:09.527Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/\nfor f in BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"== $f\"; head -c 600 $f; echo; grep -c 'pdf page' $f; done"
}
```


### [2026-09-07T17:38:10.791Z] TOOL RESULT

```
== BQT_v3_pages.txt
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|

چاپ افست ر شدیه
[pdf page 3]
اداره ‎“oes‏
‏ساره و6۷ ۲۰۹

pe ۰ ay sf s ‏ار بخ‎
‏سرام ودارت‌شسات‎

د انشمند محتر ,آقای‌د
721
== BQT_v4_pages.txt
[pdf page 1]
[pdf page 2]
ه
و سم
۰ و
الب
اس ی 9 ۱
عه ر جر ن‌خلف بربری لیر رها
ّف‌بال ۱۰۶۲ #کک .
ناس مد ی «چا لد ولوح ا!
۰ ً ّ ۰ ,7 اس ۸۰
و مین ۰ شور بر رود نات سا رراصاو رصم
ی
تم و3 رو
اد دش نوت
طلرجارم : م-ی
ی اس -
چاپ دوم فروردین ۹۳۴۳
با تجدید نظر کامل
بسرمایه کتابفروشی اين سینا- تهران
۲
چاپ افست رشدیه
[pdf page 3]
اداره کل نکا زشن"
ساره ۰۱/۹/) ‎٩۰9‏ ی
ثاریم موم 
553
== BQT_v5_pages.txt
[pdf page 1]
5
[pdf page 2]
,۶ +مه
مان ها
۰
بل
هم هم ه
اعلیات
8
کم
ول ری
« داژن »
موسسة انتشار ات امی رکیهر
تهران» ۱۳۷۹
[pdf page 3]
تعلیقات بران اطع

دکترمحمد معین

چاپ چهارم : ۱۳۶۲

چاپ پنجم : ۱۳۷۶

چاپ و صحافی: چاپخانةٌ سپهر » تهرانت

تیراژ: ۳۰۰۰ نسخه

حق چاپ محفوظ است.

شایک ۰۳۰۷-۷- ۹۹۴-۰۰ 964-00-007-7 ۱38
موسسه انتشارات امیرکبیر تهران» میدان استقلال
[pdf page 4]
دو�
293
```


## [2026-09-07T17:38:11.257Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== ISS DKS beak ===\"; grep -n -i \"'beak\" ISS_alt_DKS.txt | head -20\necho \"=== MON نوک ===\"; grep -n 'نوک' MON_part1.txt MON_part2.txt | head -10\necho \"=== MON نفت ===\"; grep -n 'نفتالین' MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-07T17:38:11.350Z] TOOL RESULT

```
=== ISS DKS beak ===
3730:also naukya, nauca ‘acme’, With Yidya nzeyo 'beak', N.Pers. nauk, nol, Waxi nüčk ‘beak’, Sarikoli misk, Since -ahva- is kept in older ahva-, later aha- ‘noose’, BS раїа-; paha- 'cooked, ripe' < *paxva-, Pašto póx plur. pëxə, a connexion with West Iraniannaxva- ' before, in front, first’, Zor.P. naxvist, N.Pers. nuxust ‘first’, Armen. hw zaxa-, naha- 'frsv, naxa-bžišk 'chief physician’, nahatak ‘running in front, first in combat, champion’; M.Parth.T. пех, nxwit, nxwyn, M.Pers.T. nix, ‘beginning’, zxust, nxwstyn, nwxwyr ‘primal man’, adjective nxwryg, from *naxva-, "nox-, seems excluded for Khotan Saka niü/ta-. Yidya navyo may indicate a base *паба-.
4063:*panáha- 'beak', only loc. sing. JS 24vi pura pemegsti aysgam rraijsai pneha ‘the vulture seized the young ones in his sharp beak’. From nāh-'nose’ with pa- ‘associated with’ (see pa- above) Av. ndshaya, ndmha, O.Pers. uaham; Sogd. Bud. nns, Man. ns; Parüft лёй, See also neste (JS 3or1). IE Рок, 755 nas-, O.Ind. nas-, inst. sing. nasd, dual пй; fem. sing. ndsa-; Lat. nàris ‘nostril’, näsum ‘nose’, O.Engl. nëse ‘promontory’, nasu ‘nose’, Lit. nósis ' nose', O.Slav. позй. With other suffixes uyni nedz, Yayn. nes, бапр1ёёї nic (c= ts).
4720:pneha 'beak', see *zaha-, *panāha-.
=== MON نوک ===
MON_part1.txt:1810:نوک پستان. آبله از هم گسستن: : بیرون زدن 
MON_part1.txt:5368:تقایل بیضوی و نوکث نیز به درازی یکث 
MON_part1.txt:8311:نو آوردن» نوکاری کردن» چیزی نو 
MON_part1.txt:9374:دارنده. آقا (مق. نوکر). ارباب انواع: ج. ۱ رت 
MON_part1.txt:9782:آب) و نوکش دارای تیغه‌دای عرضی برای 
MON_part1.txt:9798:نوک پا بر کفل کسی بزنند تیپاء زهکونی» 
MON_part1.txt:10339:طرفین آن یکث سلسله دندان‌های نوکل‌تیز 
MON_part1.txt:11020:جفت جفت و دراز و نوک‌تيزند. گل‌هایش 
MON_part1.txt:11300:و يا از نوک مخروط‌های استالاکتیت در 
MON_part1.txt:11841:درخت استر کث» قره‌بوخوره قره کونوک 
=== MON نفت ===
MON_part2.txt:77612:نفتالین فرهنگ فارسی معین 
MON_part2.txt:77639:نفتالین: 0( (.) (بز.) هبدرو کربوری 
MON_part2.txt:77647:نفتالین را از قطران و زغال سنک استخراج
```


## [2026-09-07T17:38:19.372Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== DKS 3722-3735 ===\"; sed -n '3722,3734p' ISS_alt_DKS.txt"
}
```


### [2026-09-07T17:38:19.415Z] TOOL RESULT

```
=== DKS 3722-3735 ===
nuvaát- ‘examine, test, survey’, SuvO. 4r4 nvastemáte jsa “with examination’, BS parihsama-; vyupapariksana- ; v 130, таз nvaśstāmate; SuvO. s3r2 и kümo dio naastát(i) (not nvāttä) 'and in what direction he looks down', BS yam уйт diam avalokayati; Y 295, 435v5 (sam)tsariya hira пі nvastá паї ru (nar)tya ysitha|]| ‘ће examines not the things of migration nor in the maraka-underworld birth', Z 7:32 nuvastu, Z 1:51 nuvastüre, Z 20:20 пшаййте,
190 nuváta- — nai
K rog228 tta baida dasta поайаге 'so on the hands they examine’; Z 4-83 tti nijsadu hapur nuvastafiu 'so it mustbe examined by the wiseman'; rm 128, 2gvs bis hära ahámáta nvastaia (not noa-) 'by him all non-produced things are to be tested'; Z 12:11 nvastand sd satvd 'this being is to be examined’; adjective, v 130, таз ata nvastanai ‘very critical’; with suffix -aka-, У 131, 52b3 nvastükd 'testing'; -Inaa-, її 11710 nvastavina hvaihva- (ra) baridd hira 'let the Uigurs carry out the work of investigation’. Uncertain; see the fuller text s.v. vīnā. From anu-à-stai- to base stai- ‘stand’. See also алтайа ‘hostile’, and nvasta- 'easy', anvaita- ‘difficult’. Cog- nates s.v. s?a-. Note that nva- could also be traced to *nui-pa-.
nuvüta- 'sunken, slow, weak’, for BS manda-, Z 14775 aysmüna и indriyo nuvüta 'weak in mind and senses'; Z 274 idryau jsa nvata ‘weak in senses’; Sid. 107v2 nvàvai amga hámüre 'his limbs become weak’, BS mündya-kri, Tib. sgyid lug-pa ('the knee-joints give way"); of a slow fire, 1 185, 105v3 nvāva dim (= dai тайа jimdà ‘stops slow fire in the belly’, BS mandagni-. From ni-pāta-, see pāta- 'fallen in', base pat- ‘ќо fall’, See nvátta.
nuvaindá ‘еу make noise’, Z 2446 birgga rrüvüsa nuva- пай "wolves, jackals howl’; Z 20:30 rrüvdsa nvaindd pharu, Z 241420 birgga rrüvüsa hüysa sana nuveindi ‘wolves, jackals howl though far off’. Base nau-:nu- ‘to sound’, enlarged nuvā- (or nvad-?, N.Pers. navidan 'complain'!, navistan ' groan', navidan ' weep, complain’, nàyah ‘plaint’, naytdan ‘cry aloud', navünidan ' cause to cry’, navastah, nàstah ' noise of crying in throat'; Yidya yavo anuvë, yawa anuuo 'cow bellows’; Sogd. Bud. (with -b- increment) лш ‘noise’. To IE Рок. 767 neu- ‘call’, O.Ind. navate, nauti ' sound, praise’, Celtic O.Ir, Tall ‘cry’, possibly Lat. nuntium ' message! (*zouention); Tokhara AB nu- 'to roar’. With suffix -icd, sce nvicá ' ery’.
nü&- see nvāśś-, basa- ‘noise’.
nüśta 'easy', 1 1092942, 8 пайа ttr jsüm бетаїйа ' easy, also fortunate’, See zvasta- ‘easy’.
nüha- ‘top, point’, for BS agra-, Z 4:18 aysmya sau-nühä ‘concentrated in mind’; Z 23, 172 зати hho pruha ggisai nühya ‘like dew on tip of grass'; rt 20, 42b1 sam khu praha gisai nauhya, BS comparison of avaíyáya- ‘dew’; V 314, 4b3 sumjsiiia nihana ‘оп point of needle’, Tib. khab-kyi rée-mos; Sid. 18c3 ysba hoi nauhd ' point of reed', BS wetragra-, Tib. spahi to-rto; Sid. 142v3 nauhád point’, Tib. rée; Bed уоут агаи nauhya ‘оп tip of hair’, BS vala-pathegu; Z 2:113 druai nühána; 111 99:36 Хаи-паића 'concentrated on опе point’, parallel to BS ehagra-; Bcd 44vi 4e paramünavá паићуа ‘оп the point of one atom’, BS eka-rajagri (BS paramagu- 'atom"); v 68-16 (#упи-паиййпа aysmüna 'with intent mind'; SuvP. yor2 drrau nauhnd mahüsamudrrá, BS jalam ca valagram; L 95:2 аи nauhá; L 93:15 заи nauhi; K 145, 312 nàmha, námhd; K то, 4r2 nāmhai, =K 67:149 nàhim (for *namhi) ‘beginning’. Adjective, Bed 4s5vr hasta- туйу nauhauysyam baysam ‘of the best highest Buddhas’, BS sarva-jinanüm; UI 1275 hajü namhauysa nasagaista ‘wise, highest, evolved’. From nau- with suffix -ha- < *nauxa- (like -һа- in khāha 'fountain', Yazg. хах), see
also naukya, nauca ‘acme’, With Yidya nzeyo 'beak', N.Pers. nauk, nol, Waxi nüčk ‘beak’, Sarikoli misk, Since -ahva- is kept in older ahva-, later aha- ‘noose’, BS раїа-; paha- 'cooked, ripe' < *paxva-, Pašto póx plur. pëxə, a connexion with West Iraniannaxva- ' before, in front, first’, Zor.P. naxvist, N.Pers. nuxust ‘first’, Armen. hw zaxa-, naha- 'frsv, naxa-bžišk 'chief physician’, nahatak ‘running in front, first in combat, champion’; M.Parth.T. пех, nxwit, nxwyn, M.Pers.T. nix, ‘beginning’, zxust, nxwstyn, nwxwyr ‘primal man’, adjective nxwryg, from *naxva-, "nox-, seems excluded for Khotan Saka niü/ta-. Yidya navyo may indicate a base *паба-.
nubamjindá ‘еу open', v 125, 604 kvi ttd vàjáre пићат- пай "when they hold it, they open it'; Z 22-169 tceimani vasute пићїуе samu kho milütpalà parrá ‘his eyes pure, open like the blue-lotus petal' (parallel Rāmäyaņa n 4'2 rüfiva-patra-aksa- "having eyes like rajiva- lotus petal’, see A. Кози, JA. 1969, 37-9); V 124, бат cui nuhiyündá Мапататӣ selll| "what of his they opened, such, even...'. From ni-pank- > ni-fank- to a base (s)p(/t)en-k- in O.Ind. pra-panca-, -na- ' expanding, expanse’, Armen. lw nahang ' province, region’, N.Pers. nihang ('monster'—) ‘crocodile’, Armen. lw nhang ‘water beast’ (shape of horse, woman, dog), Syriac nàng-' ‘crocodile’ or ‘hippopotamus’ (if from *zifanka-). Here belongs Lat. panda, passus, -pansus ' to expand’, (*pen-d-) not from pant-, base pet- (IE Рок. 824). Connexion of Av. fánku- ‘реак’, Oss. D. хийпх, I. xox ‘mountain’ is possible, if both are from *phanku-. For O.Ind. pra- pancaya-, pra-bancana-, pra-panca-, J. Wackernagel, Altind. Gram. rr 354, connexion with panca 'five' dubious.
nühvarrde, nülrvarüre, nühvarame, see nühvarr-.
nrhiya- ' restrained, nrhisi- 'to check’, see nihalj-.
ne 'not', v 329, 13г1-2 nai ји ne. . ne ju ne.. .ne ne. . ., BS G 37, rob4-5 ла himcit...na ca. . na jütu... Z 22:211 nenne, Z 19:19 nernne; with yi, nai, nei, with u, mau, no, nyau, nyo, ño; ne ra (Sid. 129r1); o ne ‘ог not' K 2, 136г5. See na with ni.
```


## [2026-09-07T17:38:20.047Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== MON نفت context ===\"; sed -n '77590,77660p' MON_part2.txt"
}
```


### [2026-09-07T17:38:20.127Z] TOOL RESULT

```
=== MON نفت context ===
گرم‌کن‌های نفتی استفاده می‌کنند و مخلو طی 
است از درو کرورهای سین مستادکان 
رای تا هیر آدعان روا تبسن 
۰ درجه تا ۴۰۰ درجه روغن‌های 
سنگینی بدست می‌آید که برای چرب کردن 
محور اتومیل‌ها و ماشین‌ها بکار می‌رود و به 
عنوان سوخت بنام مازوت در موتورهای 
دیزل به مصرف می‌رسد. اين روغن‌ها بیشتر 
از ثیدروکربورهای پنتادکان (,,1آو,) و 
هک فان میم نانوی در 
حرارت‌های بین ۰ درحجه تا ۲۰ ۴ درجه 
پارافین مایع تا ییا اوه سر 
حرارت‌های ۴۰۰ تا ۴۵۰ درجه روغن‌های 
سنگینی حاصل می‌شود که با سرد کردن 
نا گهانی آنها پارافین جامد بدست می‌آید که 
از ان در ساختن شمم و مشمع استفاده 
می‌کنند. ۷ - پس از خروج تمام بخارات 
حاصل از نتیجه تصفیه در حرارت‌های 
معادل ۴۵۰ درجه ماده‌ای خمبری شکل در 
ظرف باقی می‌ماند موسوم به وازلین که 


نفتالین فرهنگ فارسی معین 


ی 
مرهم‌های جلدی و همچنین به منظور حفظ 
ابزار فلزی از زنگ زدن مصرف می‌شود. 
بالاخره در ته ظرف تصفیه ماده‌ای ۳۷۳9 
جامد و سیاه رنگ بنام قیر به جدار ظرف 
می‌چسبد که از آن جهت آسفالت خیابان‌ها 
و عایق کردن دیوارها در مقابل رطوبت 
اسستفاده می‌کنند و قسمت اعظم ان 
ثیدروکربورهای با تعداد کرین زیاد یعنی 
(ي ۲۷ 0) می‌باشد؛ نفت طبیعی؛ نفت خام. 
نفت چراع: (زم. شم.) مایعی است 
بی‌رنگ که در حرارت‌های بین ۱۲۰ تا 
۰ درجه از تصفیةً نفت طبیعی بدست 
مسی‌آید و از آن جسهت روشنایی در 
چراغ‌های نفتی و بخارها و آب گرم کن‌ها 
استفاده می‌کنند. نفت چراغ برخلاف نئر ین 
سریع الاشتعال نیست یعنی کبریت افروخته 
اگر در داخل ظرفی از نفت چراغ بیفتد 
خاموش می‌شود ولی در صورتی که حرارت 
زیادتر به آن برسد مشتمل می‌شود و تا 
آخرین ذره می‌سوزد» نفت معمولی. نفت 
خام: (زم. شیم.) نفت. نفت طیعی: (زم. 
شیم.) نفت. نفت معمولی: (زم. شیم.) نفت 
چراع. 
نفتالین: 0( (.) (بز.) هبدرو کربوری 
است حلقوی مرکب از دو حلقه بنزنی که 
فرمول آن را می‌توان بصورت ما۱., 
شت. این جسم در شرابط معمولی جامد 
است و بصورت ورقه‌های سفیدی متبلور 
شت گراود: در ۹ درجه حرارت دوب 
می‌شود و در ۸ درجه سمی‌جوشد. در 
بنزین و الکل جوش حل می‌شود. در صنعت 
نفتالین را از قطران و زغال سنک استخراج 
می‌کنند. نفتلین در شرایط معمولی تصعید 
می‌شود و چون ذرات تصعید شده سمی 
اس ات رکفت و از رفن ون 


۷ ۱ 
بلورهایش دارای بوی خاصی هستند که 
حشرات از آن گریزانند: برای محافظت 
لیسة پشمی از خطر بیدخوردگی از آن 
استفاده می‌کنند؛ نفتالن. 
نفت خیز: آد." (.) جایی که از آن نفت 
بیرون آبد. 
نفت‌سور: ۱-7 (۱.) انجه با نفت سورد؛
```


## [2026-09-07T17:38:28.666Z] TOOL CALL #24: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2155 --image 2>&1 | tail -40",
 "description": "Fetch BQT page 2155"
}
```


## [2026-09-07T17:38:28.690Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n 'نفت' MON_part2.txt | sed -n '1,40p'"
}
```


### [2026-09-07T17:38:35.975Z] TOOL RESULT

```
REF: BQT:2155  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 238  OCR-lang: fas

<وو۱و-< نت
فام است که تیره رنگه و سیاه فام باشد - ودر ففت ۱ « بروزن هفت » روغنی باش د که
عریی سیم قلب ناسره را کوبند . درولایت عپروان پیدا میشود وآن سیاه وسفیدعن
۹ - دراوستا -88068 ( تره نمناك )., هندی باستان -82010 , 28080216 (شکاتن,
تر کیدن ) « اسشق ۱۰۳۵ *. هوبشمان کوید : اسم مفعول ازريشة 82018 در اوستا -088008
آمده , که نظایر متعدد دارد . اسم مفمول مشتوم به 12- :338012 است . قن : - 02812 >
ساسکریت -۳20412 وغیره . دلیلی فیست کهآ نرا از ربشهٌ 8203 بدانیم . آیا این کل ه هند
و ژُرمانی ( هندواروپایی ) است ؟ ارمنی *32۷1 ( قیر » لفت ) , بونانی 240121172 « هوبشمان
۵ , دراوراق مانوی ( پهلوی ) 810 ( قیر ۰ افت ) ۸۸14416 0۲ 191] ۸ ,17688108)
۰( .0 را ,12 ,8505 و...86۲9188! لانینی 31801018 . از وی دیگرمژلف معجمیات
عريية - سامیه نوسد ( ص۹-۲۰۸) : « لفط : اصل‌آن کدی است بسورت فملی « نباو» ( بفتح
اول و دوم وضم چهارم ) بمعنی : درخشید . روشن کرد » نابید » طلوع کرد » آغا ز کرد » و ازآن
«بطو » ( بکسراول وضم سوم )آمده بمعنی نوره و « لمبطو» ( بفتح اول وسوم وضم‌چهارم) بممنی
روشنایی » درخشند کی و « نباطش * ( بفتح اول وکسر چهارم ) بمعنی با درخشند کی » آشکارا :
و ازآنست كلمهٌ « تبطو» ( بفتح اول و ضم سوم ) بمعنی لفط » وشکی لبست که سبب اطلاق این
اسم برآن آست که یکی از خواس « لفط » نبوط آست بعنی خروج ازجوف زمین وچون آلرا
بوزانند درخشد کی گیرد » پس آلرا بمعنی « تابط , خارج , لامع . مشرق »گرفتند . بنابررین
سربانی . لفت اصلی این کلمه بیست بلکه اکدی اصل آنت و ازین بنمام ژبانهای دیگر رفته »
وغرابتی هم ندارد؛ زبرا عراق - با بلاد اآکد. بابل ؛آشور - از قدیمترین ازمنه هنبع لفط بود ۰
چنانکه اکنون‌هم است؛ ونقط فقط درعصر ماکشف شده بلکه وجود آن همواره درعراق شناخته
بوده است » زیر| بصورت درباچه هابی برمطح زمین نبعان دارد و درشب میدرخشد وئورآن از دور
پیداست؛ وفعل « لفط » درعربی بمعنی پراگنده شد وخارج شده آمده ومبدل آن « لبط > است
بمعنی بیرون‌آمد آب وخارج شد .» :
باسپ و بنفت آش آندر زدنهت همه هندیان دست برسر زدند.
فردوسی‌طوسی « شاهنامةٌ بخ ج۷اص۱۸۶۲ ۰
از هلیله قبضش شد اطلاق رفت آب آتشرع را مدد شد همچو لفت.
مولوی بلخی‌رومی « مثنوی چاپ لیکلسن دفتر اوّل ص ۵ ).
بقیه ازحاشيهٌ صفحهٌ ۷۱۵۶
آورد للی بجوال و به‌بایه از ساحل دربا چو حمالان بکتّف بار(سار.دهخدا) .
3 منوچهری دامقانی ص ۱۶۸۶ » و رك : جپالگیری .
اما این کلمه عربی است « فاة بالفتح» چیز بلایه وردی و بقیه و رانده و دور کرده, فوة بالفتح,
ولفاه کسحاب , ولفاية كسحابة ویضم ولفاوة كثشمامة مثله .» « منتهی‌الارب » - بمعنی‌لبهره وناسره :
این که زحمت کم کنم نوعی ز تشوبر است از آ نك .|
شدهای بی نفایه اسست این و ناقد بی یر .
انوری اییوردی ۶ جهانگیری ».
میاد دين هدی را چئو تایه آمام ته نیز صدر زمالرا چئو لبهره ندریم.
سوزلی سمرقندی «چهانگیری».
```


### [2026-09-07T17:38:36.020Z] TOOL RESULT

```
4921:منفتح شود بر بنده از مقام قلب و ظهور 
5431:که با کاز (نفت) کار کند. (ف.) چین و شک 
13782:انفته ال ادن ۲۱۳۳۴ کر فرع تاه 
16402:امااکن نفتی قدیمی یافت می‌شود. ترکیب قیر 
16403:همان ترکیبات هیدرو کربورهای نفت است 
16425:نفت در نه دیگ‌های تصفبه مقادیری زبادی 
16432:طبیعی؛ حجر قیر اشنت» قطران نفت. مانند 
19612:کانفت؛: ۱ [- کامفت ِ قامیت ِِ قانفت 
23319:نفت کش: کشتبی که خاص حمل نفت است. 
25116:و به همین جهت آن را در نفت یا روغن 
29246:بدست آورند و در معادن نفت هم موجود 
29311:برای موتورهای دیزیل که از نفت استخراج 
29314:گازولین: ی ۰) اتر نفت. 
30868:نوعی چراغ نفتی که فتیله‌اش مدور و از 
36543:مسختلف است. ترکسات تفت گنفت 
38264:مخزنی است جهت مایع قابل احتراق (نفت» 
41157:نفت از مبداً آن به نقاط دیگری جاری شود. 
42373:هیدروکر بورهای نفتی که در تصفیهٌ خام پس 
42374:از اتر و بنزین و نفت چراغ بدست می‌آید و 
42375:چون سیاه رنگ است بنام نفت سیاه نیز 
42378:نانوایی‌ها و موتورهای دیزل می‌باشد؛ نفت 
45291:نفتی جزو کٌازهای بالای چاه‌های نفت 
48441:فو انفت ان ]. اجرا کننده» انجام دهند ه. 
50101:خالی. رطب اند ک رشیتاه. گنفت ی 
55709:قتس‌تانفت: ۱0۵۱۵0۵1 [ع.] (افا.) آغاز 
61534:کل نون نفت ان تاه 
63670:معانفت: (-21)06] ۱۱۵6۵۱۵ [ع. مکانفة | 
66832:منفتل: ۱001۵16 [ع.] (افا.) فتبله شونده» 
68720:رنگند. بعلاوه در اطراف تشکیلات نفتی 
68753:هیدروکریورهای نفتی در شکاف‌ها و 
68755:دخایر نفتی زیرزمینی هستند بیدا می‌شود. 
68797:مونتاز: ۱۹۸ ۱( ار طنفت عکس و و فیلم و 
77466:قاروره‌های مشتعل نز فط (نفت) را سوی 
77467:دشمن پرتاب می‌کر د؛ نفت‌انداز. آنکه نفت 
77468:را مشتعل سازد. آنکه نفط (نفت) از معدن 
77506:نقت: ۸0 [+ نفط» تر. نمنا کل قبر) نفت: 
77516:نفت طیعی وجود دارند به سه حالت گاز و 
77520:می‌باشند. نفتی که از اعماق زمین بدست 
77534:ترکیب نفت‌ها غیر از ثیدرو کربورهای 
77536:(خصوصا در نفت‌های ایبران) وجود دارد؛
```


## [2026-09-07T17:38:56.452Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2233 --image 2>&1 | tail -35",
 "description": "Fetch BQT page 2233"
}
```


## [2026-09-07T17:38:58.343Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '77500,77515p' MON_part2.txt; echo \"=== نوک MON ===\"; grep -n 'نوک:' MON_part1.txt MON_part2.txt | head; echo \"=== نول ===\"; grep -n 'نول:' MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-07T17:39:02.873Z] TOOL RESULT

```
لیم - بروزن میم» معروف است که صف کلاهی باشد از آهن که در روزهای جنگه برس
باشد ۱ - ونام درختی است درهندوستان که‌ب رکه | هند٩‏ .

(۱) چك : دوائر. (۲) چش : باشد .

- اوستا 326808 ( اضف ) در 1 88606 ۰ 81 3866 ( وندبداد
4 6 )» ماسکریت -36۸ ( صف ) » پپلوی 3۵۲۳ ۰ 67۳۵۸۴ » کردی 17۷ (صف) »
قی: 819۷۳۵2 (نیمروز) . افغابی81138 ۰ قس: بلوچی 2810۳۵0 ۰ ع886۲1۵5]0.8۲۲۳۵
( نیمروز) ۰ 8600818 ۰ 3613932 ( لمعب ) » سریکلی 2 0 رل : اسشق ۰۱۳۹۹
هوبشمان (۱۰۹۹) گوید : درتلفظ 8150 , قس : پازند 8100 , افغانی ع 8183 :

یم تالی گر خورد مرد ندای بذل درویشان کند لیمی دگر.

« کلتان ص ۰۲۱

۲ - هندی * 87601۳80۳18 و2زاه 2 (0.542. اع[1 0۲8۸06۵1 ۵2ا 110 )

۴ -ظ . برساختهٌ فرقهٌ آذرکیوان. ۴ - رك : نیم شکری .

* - رك : ترك . ۹ - در تاررخ بیهقی مصحح دکترفیاض (صس۸؟۲) آهده :دودیگر
رو چون بار بگست واعیان ری بجمله آمده بودند بخدمت (مسمود) با این مقدمان » و افزون
از ده هزار زن ومرد بنظازه ایستاده » واعیان را به نیم تراك بنشاردند .» محشی درذبل همان‌مفحه
کوید : نیم ترك نوعی بوده است ازخیمه » وبنا بحاشيهٌ یب (ادیب پیشاوری) لوعی ازخيمهٌ كوچك
بوده » و درهرحال بفتح تا وسکون راست , وکافآن تازی يا فارسی هردو محتمل است » چه‌اگر
کلمه مستعار از نیم ترکك بمعنی کلاه خود باشد چنانکه در برهان قاطم است ةاعدة باکاف فارمی
است ( چون تگه با م رکه قافیه شده است ) و اگراز ترك بمعنی قطعه‌های کلاء و خیمه آمده
باشد با کاف تازی است بنا بتلفظ جاری.

8 لولی - بکسر اول , از: بیل (ء.م.) ی (سبت) قن : لیله ؛ هرچیز منسوب‌به‌لیل
(«.م.) - رفگه کبود - هرچیز برنگه کبود :

در جبههٌ کمبه کعبه آرا بیلی‌زده دفم چشم بد را
نیلی کلفی برا و کشیدی از چشم بدان بیارمیدی .
دروش واله هرری بر تمریف حجرالاسود « فرهنگه نظام >.
```


### [2026-09-07T17:39:02.950Z] TOOL RESULT

```
آمده اگر ضبط غین در این نسخه صحیح‎ 
باشد رنفام» مصحف ان است.‎ 

نفایه: (۵-)-۱۸ ,غز3ا۱۵ [ع. نقابه | (۱.) هر جبز 
که به سبب فساد و پستی و بی‌قیمتی به دور 
انداخته شود. نبهر ه» ناسر 4۰ ج. تقابات. 
نقت: ۸0 [+ نفط» تر. نمنا کل قبر) نفت: 
از سوی دیگر در اکدی به صولت فعلی 
«نباطو» به معنی درخشید؛ روشن کرد تابید. 
طلوع کرد؛ «نبطو» به معنتی نفط آمده| )1( 
(زم. شیم.) مایعی روغنی شکل و معدنی که 
با بوی خاص (شبیه بوی قیر) مشخص است 
اکتا افستیلن ۱ات تاوطین از 
ثبدروکربورهای گونا گون است و در مراحل 
مختلف تصفبه مواد مختلفی از آن بدست 
می آورند. ثبدروکربورهایی که در ترکیب 
=== نوک MON ===
MON_part2.txt:81037:نوک: (قد. ۱۲)5۲ [- نک ] (.) منقار 
=== نول ===
MON_part2.txt:81070:نول: [ا: (۱.) منقار برنده. گرداگرد دهان. 
MON_part2.txt:81073:نول: ات« [فر. صفر ] (ص) (بازی شطر نج)
```


## [2026-09-07T17:39:21.142Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb && sed -n '1,60p' tools/fetch_source.py"
}
```


## [2026-09-07T17:39:21.967Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '81030,81080p' MON_part2.txt"
}
```


### [2026-09-07T17:39:22.016Z] TOOL RESULT

```
نوف: (۱۵۳۷۲0۷۷۵ [ع.] (.) کوهان بلند 
(شتر)؛ ج. انواف. 

نوف: ۲ ( نوفه ] (ا.) انعکاس صوت (در 
کو ه» حمام» چاه و غیره)؛ صدا. بر نوف: بر 
از انعکاس صوت. شور و غوغا که از کثرت 
مردم و جانوران خیزد. فریاد سکث. 
نوک: (قد. ۱۲)5۲ [- نک ] (.) منقار 
پرندگان. سر تیز چیزی مانند سر قلم. خار 
آهنی که بر بینی و موزه محکم کنند. نوک 
پا: (عم.) رأس انگشتان پا. نوکث دل: سر 
دل؛ راس القلب. یکك نوکت با: پا: (عم.) اند کک 
مدتی. نوکك کسی را قیچی کردن: (عم.) او 
ر وادار به سکوت کردن. 

نوکار: ۲-(۵) ۱2۷ (ص‌مر.) کس ی که تازه 
به شغلی با هنری برداخته» تازه کار مبتدی. 
اکسترن در بیمارستان (فره.) 

نوک تیز: 2« (ص‌مر.) آنجه که زاسشن 
تا 

نو کد خدا: تلم م2۲ (ص‌مر.) 
کسی که تازه صاحب خانه شده. تازه داماد. 
نوکر: )۱2۳۲۵۲ [- نوکار» مف. تر.] 
(ص. ۱.) چاکر» خدمتکار» گماشته. ضح. به 
خدمتکار مرد اطلاق شود؛ مق. کلفت. رفیق؛ 
دوست. مشاور. (ف.) عضو اداره (دولتی). 
نوکرباب: (۱۵۷۵۲)۱۵۷۰ [مف. تر . ۳6 
امر.) (عم.) کسی که از طبقةٌ نوکران و 
خدمتگزاران باشد. تس عضو اداره 


(دولتی). 
نو کیسه: (92)00۷-0[-72۷ (ص‌مر.) آنکه 


تازه به مال و دارایی رسیده؛ مق. کهن کیسه. 
تازه به دوران رسیده. 

نول: [ا: (۱.) منقار برنده. گرداگرد دهان. 
لول صراحی» ناژ مشربه. 

نول: ات« [فر. صفر ] (ص) (بازی شطر نج) 
هیچ به هیچ. 

نوع: (00۷۵) 0227۷۵۱ [ع.] (مص‌ل.) خواسدن. 
(ا.) خوات. 

نود: « (.) ن) ج. نونات. (ص.) ( کن.) 
خمیده قامت؛ منحنی» کمانی. ( کد.) ایرو»
```


### [2026-09-07T17:39:22.340Z] TOOL RESULT

```
Exit code 2
sed: can't read tools/fetch_source.py: No such file or directory
```


## [2026-09-07T17:39:26.947Z] TOOL CALL #30: Bash

```json
{
 "command": "ls tools/ && sed -n '1,40p' tools/fetch_source.py 2>/dev/null"
}
```


### [2026-09-07T17:39:27.006Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
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


## [2026-09-07T17:39:32.623Z] TOOL CALL #31: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/naphtha\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%88%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%85\" \\\n \"https://www.etymonline.com/word/naphtha\" ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 347 verification (naft/nok/nim)\"; done"
}
```


### [2026-09-07T17:39:38.174Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/naphtha
/home/sfmqrb/git/rishe/data/verification/sources/web/a0bdfbb3bd1cf04f.txt
### https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7
/home/sfmqrb/git/rishe/data/verification/sources/web/0b49945e713fcf7b.txt
### https://en.wiktionary.org/wiki/%D9%86%D9%88%DA%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/8aee135452d0fc74.txt
### https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/eff59a0ce44b9717.txt
### https://www.etymonline.com/word/naphtha
/home/sfmqrb/git/rishe/data/verification/sources/web/b9c82fce9c896780.txt
```


## [2026-09-07T17:39:41.037Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### naphtha wikt\"; grep -n -A3 -i 'Etymology' a0bdfbb3bd1cf04f.txt | head -60"
}
```


### [2026-09-07T17:39:41.082Z] TOOL RESULT

```
##### naphtha wikt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
88: Etymology 
89-
90- 2.3 
91- Pronunciation 
--
192: Etymology
193- [ edit ] 
194-
195: Etymology tree
196-
197- Akkadian napṭum bor. ? 
198- Old Persian *naftah bor. 
--
335: Etymology
336- [ edit ] 
337-
338- From Ancient Greek νάφθα ( náphtha ) .
--
494: Pages with etymology trees 
495: English entries with etymology trees 
496- Pages with entries 
497- Pages with 2 entries 
498- Quotation templates to be cleaned
```


## [2026-09-07T17:39:42.165Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### نفت wikt\"; sed -n '1,400p' 0b49945e713fcf7b.txt | grep -n -i -B2 -A8 'Etymology' | head -120"
}
```


### [2026-09-07T17:39:42.220Z] TOOL RESULT

```
##### نفت wikt
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
170- 2 terms 
171-
172: Etymology
173- [ edit ] 
174-
175- From Aramaic נִיפְטָא ( nip̄ṭā ) / נַפְטָא ( nap̄ṭā ) / ܢܷܦܛܳܐ ( nep̄ṭā ) / ܢܱܦܛܳܐ ( nap̄ṭā ) , from Akkadian 𒉌𒆳𒊏 ( napṭu , “ naphtha ” ) .
176-
177- Pronunciation
178- [ edit ] 
179-
180- IPA ( key ) : /naftˤ/ , /niftˤ/
```


## [2026-09-07T17:39:47.221Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### naphtha tree 190-260\"; sed -n '190,265p' a0bdfbb3bd1cf04f.txt"
}
```


### [2026-09-07T17:39:47.261Z] TOOL RESULT

```
##### naphtha tree 190-260
 Wikipedia 

 Etymology
 [ edit ] 

 Etymology tree

 Akkadian napṭum bor. ? 
 Old Persian *naftah bor. 
 Ancient Greek νάφθα ( náphtha ) bor. 
 Latin naphtha bor. 
 English naphtha 

 From Latin naphtha , from Ancient Greek νάφθα ( náphtha , “ naphtha ” ) , from Old Persian *naftah , probably borrowed or assimilated from Akkadian 𒉌𒆳𒊏 ( napṭu , “ naphtha ” ) . The Greek mediation is reflected in the spelling – ‘ph’ and ‘th’ (from ‘φ’ and ‘θ’).

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈnæfθə/ , /ˈnæpθə/ 

 Audio ( Southern England ) : ( file ) 

 Noun
 [ edit ] 

 naphtha ( countable and uncountable , plural naphthas ) 

 ( dated ) Naturally occurring liquid petroleum .

 ( petrochemistry ) Any of a wide variety of aliphatic or aromatic liquid hydrocarbon mixtures distilled from petroleum or coal tar , especially as used in solvents or petrol .
 1918 , W[illiam] B[abington] Maxwell , chapter VII, in The Mirror and the Lamp , Indianapolis, Ind.: The Bobbs-Merrill Company , →OCLC : The turmoil went on—no rest, no peace. [ … ] It was nearly eleven o'clock now, and he strolled out again. In the little fair created by the costers' barrows the evening only seemed beginning; and the naphtha flares made one's eyes ache, the men's voices grated harshly, and the girls' faces saddened one. 

 1973 , Thomas Pynchon , Gravity's Rainbow : No, this is not a disentanglement from, but a progressive knotting into — they go in under archways, secret entrances of rotted concrete that only looked like loops of an underpass... certain trestles of blackened wood have moved slowly by overhead, and the smells begun of coal from days far to the past, smells of naphtha winters, of Sundays when no traffic came through... 

 1995 , Philip Pullman, Northern Lights : The Common Room and the Library were lit by anbaric light, but the Scholars preferred the older, softer naphtha lamps in the Retiring Room. 

 Derived terms
 [ edit ] 

 napalm 
 naphthacene 
 naphtha lamp 
 naphthalene 
 naphthalenide 
 naphthalide 
 naphthalimide 
 naphthene 
 naphthenic 

 Descendants
 [ edit ] 

 → Japanese: ナフサ ( nafusa ) 

 → Korean: 나프타 ( napeuta ) 

 Translations
 [ edit ] 

 naturally occurring liquid petroleum

 Akkadian: napṭum   m 

 Arabic: نَفْط   m ( nafṭ ) 

 Armenian:
 Old Armenian: նաւթ ( nawtʻ ) 

 Czech: ropa   (cs)   f , nafta   (cs)   f 

 Finnish: nafta   (fi) 

 French: naphte   (fr)   m 

 German: Naphtha   (de)   f or n
```


## [2026-09-07T17:39:48.029Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### نفت persian section\"; sed -n '100,170p' 0b49945e713fcf7b.txt; echo \"-----\"; sed -n '185,260p' 0b49945e713fcf7b.txt"
}
```


### [2026-09-07T17:39:48.087Z] TOOL RESULT

```
##### نفت persian section
 Kurdî 
 ລາວ 
 ဘာသာမန် 
 Polski 
 Português 
 Русский 
 Türkçe 
 اردو 

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

 See also: نقط 

 Arabic
 [ edit ] 

 Root 

 ن ف ط ( n f ṭ ) 

 2 terms 
-----
 نِفْط or نَفْط • ( nifṭ or nafṭ )  m ( plural نُفُوط ( nufūṭ ) or أَنْفَاط ( ʔanfāṭ ) ) 

 ( uncountable ) oil , petroleum , naphtha 

 ( uncountable , dated ) turpentine 

 ( uncountable and countable , obsolete ) a flammable mix used in war such as Greek fire 

 ( countable , obsolete ) a kind of cannon that projects such substance, lombard 

 Declension
 [ edit ] 

 Declension of noun نِفْط ( nifṭ )‎; نَفْط ( nafṭ )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نِفْط ‎; نَفْط 
 nifṭ ‎; nafṭ 

 النِّفْط ‎; النَّفْط 
 an-nifṭ ‎; an-nafṭ 

 نِفْط ‎; نَفْط 
 nifṭ ‎; nafṭ 

 nominative

 نِفْطٌ ‎; نَفْطٌ 
 nifṭun ‎; nafṭun 

 النِّفْطُ ‎; النَّفْطُ 
 an-nifṭu ‎; an-nafṭu 

 نِفْطُ ‎; نَفْطُ 
 nifṭu ‎; nafṭu 

 accusative

 نِفْطًا ‎; نَفْطًا 
 nifṭan ‎; nafṭan 

 النِّفْطَ ‎; النَّفْطَ 
 an-nifṭa ‎; an-nafṭa 

 نِفْطَ ‎; نَفْطَ 
 nifṭa ‎; nafṭa 

 genitive

 نِفْطٍ ‎; نَفْطٍ 
 nifṭin ‎; nafṭin 

 النِّفْطِ ‎; النَّفْطِ 
 an-nifṭi ‎; an-nafṭi 

 نِفْطِ ‎; نَفْطِ 
 nifṭi ‎; nafṭi 

 dual

 indefinite

 definite

 construct
```


## [2026-09-07T17:39:55.555Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### نفت persian\"; grep -n 'Persian' 0b49945e713fcf7b.txt | head -20"
}
```


### [2026-09-07T17:39:55.607Z] TOOL RESULT

```
##### نفت persian
```


## [2026-09-07T17:39:56.588Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"##### نوک\"; grep -n -i -A6 'Etymology' 8aee135452d0fc74.txt | sed -n '1,60p'\necho \"##### نیم\"; grep -n -i -A6 'Etymology' eff59a0ce44b9717.txt | sed -n '1,60p'"
}
```


### [2026-09-07T17:39:56.650Z] TOOL RESULT

```
##### نوک
70: Etymology 1 
71-
72- 2.1.1 
73- Alternative forms 
74-
75- 2.1.2 
76- Pronunciation 
--
88: Etymology 2 
89-
90- 2.2.1 
91- Pronunciation 
92-
93- 2.2.2 
94- Noun 
--
185: Etymology 1
186- [ edit ] 
187-
188- Alternative forms
189- [ edit ] 
190-
191- نوگ ( nōg ) , نک ( nuk ) 
--
259: Etymology 2
260- [ edit ] 
261-
262- A user has added this entry to requests for verification ( + ) with the reason: “Persian does not have initial consonant clusters and this word is not present in dictionaries.”
263-
264- If it cannot be verified that this term meets our attestation criteria , it will be deleted. Feel free to edit this entry as normal, but do not remove {{ rfv }} until the request has been resolved.
265-
##### نیم
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.3 
68- Adjective 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Adjective 
--
102: Etymology 1 
103-
104- 3.1.1 
105- Pronunciation 
106-
107- 3.1.2 
108- Noun 
--
114: Etymology 2 
115-
116- 3.2.1 
117- Pronunciation 
118-
119- 3.2.2 
120- Noun 
--
196: Etymology
197- [ edit ] 
198-
199- From Classical Persian نیم ( nīm ) .
200-
201- Noun
202- [ edit ] 
--
226: Etymology
227- [ edit ] 
228-
229- From Middle Persian 𐭯𐭥𐭢, 𐭭𐭩𐭬 ( nēm , “ half ” ) (logogram PRG from Aramaic), from Proto-Iranian *náymah , from Proto-Indo-Iranian *náymas ( “ half ” ) . Cognate with Avestan 𐬥𐬀𐬉𐬨𐬀 ( naēma ) , Sanskrit नेम ( néma ) .
230-
231- Pronunciation
232- [ edit ] 
--
306: Etymology 1
307- [ edit ] 
308-
309- Inherited from Sanskrit नियम ( niyamá ) .
310-
311- Pronunciation
312- [ edit ] 
--
353: Etymology 2
354- [ edit ] 
355-
356- Inherited from Sanskrit निम्ब ( nimba ) .
```


## [2026-09-07T17:40:01.456Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/ && sed -n '185,262p' 8aee135452d0fc74.txt"
}
```


### [2026-09-07T17:40:01.513Z] TOOL RESULT

```
 Etymology 1
 [ edit ] 

 Alternative forms
 [ edit ] 

 نوگ ( nōg ) , نک ( nuk ) 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈnoːk/ 

 ( Dari, formal ) IPA ( key ) : [nóːk] 

 ( Dari, formal ) IPA ( key ) : [nóːk] 
 ( Kabuli ) IPA ( key ) : [nóːk] 

 ( Hazaragi ) IPA ( key ) : [nʊ́ːk] 

 ( Iran, formal ) IPA ( key ) : [núːkʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [nɵ́k] 

 Rhymes: -oːk 

 Readings

 Classical reading ? 

 nōk

 Dari reading ? 

 nōk

 Iranian reading ? 

 nuk

 Tajik reading ? 

 nük

 Noun
 [ edit ] 

 نوک • ( nōk / nuk ) ( Tajik spelling нӯк ) 

 beak , bill (of bird)
 Synonym: مِنْقَار ( minqār ) 

 nib , tip , point 

 spout 

 Derived terms
 [ edit ] 

 نوکدار ( nōkdār , “ beaked, pointed, nibbed ” ) 

 نوک پستان ( nōk-i pistān , “ nipple ” ) 

 Descendants
 [ edit ] 

 → Hindustani: 
 Hindi: नोक ( nok ) 
 Urdu: نوک ( nok ) 

 → Punjabi: 
 Gurmukhi script: ਨੋਕ ( nok ) 
 Shahmukhi script: نوک ( nok ) 

 Etymology 2
 [ edit ] 

 A user has added this entry to requests for verification ( + ) with the reason: “Persian does not have initial consonant clusters and this word is not present in dictionaries.”
```


## [2026-09-07T17:40:14.736Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== SOD nwk ===\"; grep -n -E \"nwk|n'wk|nōk|beak|منقار\" SOD.txt | head -20\necho \"=== HUB naft/neft ===\"; grep -n -E 'neft|naft|napta' HUB.txt | head -20\necho \"=== HUB nim ===\"; grep -n -E '\\bnim\\b|nīm|naema' HUB.txt | head -20"
}
```


### [2026-09-07T17:40:14.806Z] TOOL RESULT

```
=== SOD nwk ===
8889:214  "pm'nwk    M 
12026:697  'yr'nwkCw)   S  fU. 
13088:pw  nwkr,  TSP  2.871,  "absolutely" 
15717:1238  'nz'nwk03   B 
18334:having  an  iron  beak 
19397:'tSrmnwkw'nch 
19539:1811  'tSrmnkw'ch  =»  'tSrmnwkw'nch 
19552:1813  'tfirmnwkw'nch   B,  S  v-tj** 
19553:Gramanu-kwanc   OtSrmnkw'ch)  ^smnwk'nc 
26250:long-beaked 
38147:znuk   (z'nwk^,  jnwq)  ©Av.  znu;  Pahl.  snwk 
39695:having  a  red  beak 
40778:mouth,  beak 
42184:manuk   =*myn-3,  nVnkw,  nVnwk 
42290:5208  m'nwk  B,  M  ji,  ^U 
42297:38.2;  STii  1.94;  BSTi  81.51;  C2;  m>nwkw,  Frag. 
42302:manukya   ^nVnwk 
48975:6133  nwk   B 
48976:nuk   (nwq)  ©Khwar.  nwk 
48977:tip,  point,  beak 
=== HUB naft/neft ===
1661:naftafig *Mitte des Leibes' (beim Pferd, eigentl. *Nabel-
3579:Analogic der zahlreichen Ptcp. auf -ta zu napta- um-
3624:(vgl. zd. naptarem) zuriick. Daneben nahasa 'Enkel*
6601:afs, afs: tauf Ritze\ np. taft; »at?f *Erdharz\ np. naft; Khav-
9056:vgl. zd. napta- 'feucht*. Siehe w6 = m § 153.
=== HUB nim ===
```


## [2026-09-07T17:40:16.108Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/\necho \"=== ARY نفت ===\"; grep -n 'نفت' ARY_pages.txt | head -10\necho \"=== ARY نوک ===\"; grep -n 'نوک' ARY_pages.txt | head -10\necho \"=== ARY نیم ===\"; grep -n 'نیم' ARY_pages.txt | head -10"
}
```


### [2026-09-07T17:40:16.195Z] TOOL RESULT

```
=== ARY نفت ===
11253:ارمنی (474481142): ۷01 بلغاری (#نفتگممالناهق, اون نماد ۵:۱
11634:ایسلندی کهن (/(0104۵/نفت5 صا0): هنبت. (7177175): 71۳
14533:۲ ا ‎٩1۸۵۷۸7‏ گنفت بات۸ان۸۸ ۸11
14849:۱ ۲- واژه‌ی فارسی آنفت" نیز از همین واجریثه است(سانسکریت: ۷۸873۸۷۲ اوستابی: ۹8۷۸۳7۸ پهلوی:
16127:01770۵۸ ببفتفاز۵ ۲ کته‌نه ,تکتمه 00 بنفتتکاد. ,2/380
=== ARY نوک ===
997:می‌کند که زنده بودن و نوکری کردن را به سلطنت در جهان مردگان ترجیح می‌دهد.
1714:معنی این واژه در زبان پونانی؛ نوکك.
5412:پیئو» پینوک (به چم / ۱۸۵
=== ARY نیم ===
338:اصلاً از کجا میدانیم که هند و اروپائیان بومی محل‌های فعلی خود نبودند واز.
371:«صحبت از «خاستگاه اولیه» مستلزم این است که فرض کنیم که تا ۰یا ۵۰۰۰ سال قبل از
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
1032:عم سازمان ایل و امت: همانطور که در بالاگفنیم 1084 واژه‌یع «خانه» بود و واژه‌ی ریس
1053:فرزندان و دوردازی دشمنان و پیماری‌ها هم بود. نیمه خدایی بودن شاه (معمولاً با مادرش الهه بود یا
1165:امروزه حدود نیمی از واژگان زبان فارسی عربی با ترکی است. در چند دهای اغیر نفوذ فرهنگی
3551:887 بسپار شبیه به نظر می‌رسد. در دوران پیش از اسلام عرب‌های عربستان دارای برج و بارو نبودند و می‌دانیم که
6979:انگیی کهن اهب نیم #تهلا فرهنگ معین : ۱۳ ۱
7545:چم این واژه در زبان انگلیسی امروز: آهسته جاری شدن» (خون) آمدن؛ گل و لای» خون نیمه لخته.
9991:چم این واژه در بان ژرمنی: نیم‌گرم» ولرم» ملایم.
```


## [2026-09-07T17:40:26.817Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== HUB 3570-3590 ===\"; sed -n '3570,3590p' HUB.txt\necho \"=== HUB 6595-6612 ===\"; sed -n '6595,6612p' HUB.txt\necho \"=== HUB 9048,9060 ===\"; sed -n '9048,9060p' HUB.txt"
}
```


### [2026-09-07T17:40:26.880Z] TOOL RESULT

```
=== HUB 3570-3590 ===
textes du Mainyo-i-Khard p. 11, Mann, ZDMG. 47,
705). Kurd. LW. sdr neStw umgekehrt' (*Kopf unten)
Socin, kurd. Samml. II, 340.
1034»>*»- Np. ndSftn 'Nest' (mit %l) = *nisfdman'? Vgl.
Fr. Miiller, WZKM. 6, 190; Mann, ZDMG. 47, 706.
Horn stollt das Wort jetzt (KZ. 33, 435) zu skr.
ksBma- 'Aufenthalt, Rast'.
1035. Das ptc. pass, einer Wrzl. nabh wiirde im Avesta
urspr. *nabda^ lauten, kQnnte aber auch nach der
Analogic der zahlreichen Ptcp. auf -ta zu napta- um-
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
=== HUB 6595-6612 ===
als die Armenier die Worter entlehnten.
') Vgl. zd. fsebls *mit Fesseln' zu skr. pag,
2) Wie aber verhalt sich np pistan 'Brust' zu zd. fstana-? Vgl.
oben p. 41. Etwa pistan (aus ^pdatdna-?) zu. fstana' (aus *pstana-)
wie zd. pitar- zu zd. ptar- ?— 187 -
b) durch v = u in den Verbindungen pers. aft^ ifU
afs, afs: tauf Ritze\ np. taft; »at?f *Erdharz\ np. naft; Khav-
far ein Orbelier (bei Vardan), np. kaftar *Hyane'; ^iwf 'Pech',
arab. pers. zift; drauS Tahne, Banner = np. dirafs, zd.
drafsa-) karatis, karos *Eppich', np. karafs; kausik, kdsik
'Schuh', np. kafsy bal. LW. kaus *Schuh'; ausarak (osarak)
ausgepresster Saft, Most' (Hohelied) = np. afsara,
c) durch X vielleicht in :
Vaxrid ein Armenier (Thorn. 78) = Ovatpgl^rig einPerser
(Agath.) = syr. Gofrlz (4. Jhd.), s. NSldeke, Tab. 223,
'also = pers. Vafric (zu unterscheiden von Vahrid Faust us
V. Byz. 147, 148 ■■= p. Vahriz, gcOiagCQ-rig, ein Titel, Tab.
223—224); Hazaravuxt ein Titel (Faustus v. Byz. etc.),
=== HUB 9048,9060 ===
c) Idg. rfw, dAw — ap. np. n: sikanam zerbreche aus
arisch *8kadnami, Wrzl. idg. slcend; vgl. zd. 6wna- JGrund,
Boden ^) np. 6mw 'Fundament , Grund' = skr. budhna-.
Dagegen bleibt nd, ndh, vgl. handa == ap. bandaka-
*Diener.
d) Idg. bhn = ap. mw = np. m im Auslaut : kam wenig
= ap. kamna- aus *kabna', idg. *A:i^6Awa-, vgl. zd. sup.
kambistem; nam *feucht' = ap. *namna' = idg. *nabhna-y
vgl. zd. napta- 'feucht*. Siehe w6 = m § 153.
e) Idg. pn = iran. fn = np. / oder m oder 6 ? im
Auslaut: ^a/ *Hitze' = zd. tafnu-, tafnah-; sdm^) *Nacht-
essen', phi. iflw, zd. xsdfnlm (ace, ys. 62, 7 der Neuaus-
gabe), vgl. zd. xsafni; x^ab^) *Schlaf' = zd. x^afna- (oder
```


## [2026-09-07T17:40:27.824Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ && sed -n '14840,14860p' ARY_pages.txt; echo ===; grep -n 'pdf page' ARY_pages.txt | awk -F'[ \\\\]]' '$0 ~ /page/' | sed -n '1,1p'; awk 'NR>=14700 && NR<=14860 && /pdf page/' ARY_pages.txt"
}
```


### [2026-09-07T17:40:29.110Z] TOOL RESULT

```
Exit code 1
ایرلندی کهن رترعنط منم با ,۸8۵4 4 (25ت0101571) هن ما
هبیت (۰#1777775 ۱8۴۸۶۵ ,۸8815 12105 عاظ
5 (هاتآ۸82) :0/5
7 ر(شاآتاظ۷5) +57
76 للملا
برهان قاطع + ۳۱۸۷
فرهنگ معین : ۴۰۹
ٍ ۰ بادداشت:
8 ۱- چم این واژه در زبان‌های غیرایرانی: ابر» سحابی» آسمان,
۱ ۲- واژه‌ی فارسی آنفت" نیز از همین واجریثه است(سانسکریت: ۷۸873۸۷۲ اوستابی: ۹8۷۸۳7۸ پهلوی:
ا ۳ ضناً واژه‌ی انگلیسی ۸۸13773۸ از همین واژه‌ی فارسی گرفته شده است.
س جک _ت-
۱
اوستایی (4/537400): ]۱۷831۸71 ,۱۷8۸/۸3 اپرلندی کهن (بلونقا /۵1): ادا ادن
پارسی باستان (۳8۴۹4۸۷ ۰:۵۵ ۸۸۸۲۰ 1110۸5
۱ پهلری (۲تتت: ۰ ,۱۷۸۵۸2۲۲ ,3۸۸136 گالی (تاکلنمه): نی
وت 0 اند ولزی (5/7): یرای
۱ کر دی (0008۶: ب ۱۷۹/۲ ,۲12
بلوچی (/1613ل8): ترقا ,تاعتاجم :۲ پسگشت‌ها کت ی
افغانی (پشتی) (/۸8091): زلاتا ری ی
ا سانسکریت (54/88017): ,قشالفلا ,28 ((۳۵۹78۸710) ۰ هلانق ۸
(eval):1: == not found
```


## [2026-09-07T17:40:48.670Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== AKD context 960-990 ===\"; sed -n '963,985p' AKD.txt\necho \"=== AKD nabatu ===\"; grep -n -E 'nab[aā][tṭ]u|nabatu' AKD.txt | head"
}
```


### [2026-09-07T17:40:48.727Z] TOOL RESULT

```
=== AKD context 960-990 ===
akk.   siibil   ein   Edelstein    :  >   wohl   hebr.   .idbö.  akk.  sämtu,
sändii,  ein  Edelstein  (eig.  der  rotbraune)  :  dazu  wolü  hebr.  suham. [akk.  barraqtu  ein  Edelstein,   auch  im  Akk.  Fremdw.,  spät  und  vereinzelt
1)  Daß  die  eine  Pariser  Sargontafel  aus  Magnesit  besteht,  ist  m.  E.  kein  zwingender Beweis  für  abäru  =  Magnesit;  denn  vgl.  neben  der  Aufzählung  in  dieser,  der  Silber- und Goldtafel  auch  diejenige  in  Khors.  159  f.  und  Ann.  420  f.  Es  könnte  daher  z.  B. auch  aspü  =  Magnesit  sein.
      60      
belegt  :  zunächst  viell.  >  späthebr.  iäräqet,  bänjat,  angeblich  Smaragd. Fraglich,  ob  das  Wort  semit.  Ursprungs  (dann  zu  St.  brq  blitzen);  idg. entspricht  skr.  maralcata,  griech.  fiÜQuySog,  of^dgaySog  usw.,  Smaragd.]
[akk.  aJpü,  auch  jasupü  und  jos^m  eine  Steinart,  viell.  Magnesit  (s. S.  59  Anm.  1)  :  dazu  wohl  späthebr.  jclspe  ein  Steinname,  und  doch  wohl auch  griech.  Xaam?  usw.,  Jaspis^  [akk.  algnmisu  eine  Steinart,  auch  im
Akk.  wohl  Fremdw.  :  dazu  wohl  späthebr.  'älgahts,  schwerlich  „Eisstücke", bei  Ez.  u.  vieU.  Sir.  46,  5  und  ägypt.  "rqhS  eine  besonders  harte  Steiuart.
[akk.  burallu^  eine  Steinart,  vieU.  Berj^ll,  dann  zu  :  griech.  ß^Qvlloe, deutsch  auch  noch  in  Brille,  sanskr.  vrlidüriya,  praki\  verulia,  Pali  velu- riya  (syr.  hellüra  und  heridlä,  arab.  ballftr,  äth.  hereile  und  hellnr).
[akk.  sassu  wohl  weißer  Marmor  bezw.  Alabaster  :  dazu  späthebr. sajis,  ses,  syr.  slsä,  ägypt.  ss.]  akk.  p%lu,  pidu  Kalkstein  :  dazu
wohl  armen,  hur  Kalk,  sowie  griech.  nüQog  eine  Kalksteinart.
akk.  gassu  Gips  s.  oben  S.  31  f.  akk.  hipru  Erdpech,   As-
phalt^ :  >  hebr.  Icöper  Gen.  6,14,  aram.  hiprä  O  arab.  kufr,  sowie armen.  fe«pr,  falls  nicht  direkt  <[  akk.).  Ygl.  noch  unten  zu  hipr7hi. Da  akk.  Mm  Ofen  (s.  oben  S.  32)  speziell  gerade  vom  Asphalt-,  Pechofen des  Schiffers  gebraucht  wird,  wäre  es  nicht  unmöglich  daß  :  >  syr.  und jüd.-aram.  qträ^  Asphalt,  Pech  (>>  arab.  qlr  und  qär);  desgl.  dann  aber wohl  auch  aram.  gir,  gträ  Kalk  O  wohl  späthebr.  gtr,  sowie  arab.  gajjär, aber  auch  glr,  auch  südarab.  gjr  und  äth.  in  gajjara  tünchen).
alck.  naptu  Erdöl,  Naphtha  :  >  aram.  naptä,  neptä  O  arab.  naft, pers.  neft,  sowie  griech.  vätpfia^  usw.,  NapJdha).  akk.  etrdnu  wohl
Teer  od.  ä.  :  >  wohl  aram.,  trotz  des  ',  'atränä,  'etrcinä  Teer*  O,  mit auffälligem  q,  arab.  qaträn,  qitran).  akk.  wahrsch.  Jcuprrtu^  Schwefel,
dann  :  >  hebr.  goprtt,  aram.  guprlta,  kuhritä,  Jcebritä  O  arab.  kibrit).
akk.  uhtdu  eine  Alkalienart  :  ;>  syr.  'aJjla,  'vhlä  Lauge.  [akk.
1)  K.  996,  Rev.  10  ff.  (Harper  VI  570).  Es  ist  hier  anscheinend  vom  Erhitzen  des 6u?'a?ZM-Steines  die  Rede.  Daraus  darf  man  vielleicht  schließen,  daß  die  Babylonier  die eigenartige  Krystallhildung  des  Berylls  gekannt  und  verwertet  haben.
2)  Wörtl.  wohl  Schmiere,  von  kapärti  bestreichen,  beschmieren;  vgl.  dazu  unten  S.66.
3)  Jedenfalls  zu  trennen  von  jüd.-aram.  qerd  Wachs  <;^  griech.  xTj^öq.
4)  Die  Stelle  2  Maik.  1,  36  ist  natürlich  für  die  Etymologie  des  "Wortes  väip»a vollständig  belanglos.  5)  Wohl  ganz  zu  trennen  von  PI.  'etrSne  Räuoherwerk.
6)  Bab.  Exp.  Univ.  Penns.  XIV  Nr.  148,  52.  kupritu  könnte  einfach  WeiterbUdimg von  kupru  Erdpeoh,  sein.
      61      
nitiru  wohl   Natron,   nur  vereinzelt   zu   belogen,   wohl,   wie   liebr.  näter, arani.  nitro,  netrö,  griech.  vItqov,  Utqov  usw.,  Natron,  <C  ägypt.  ntrj.] akk.  si];l;ii  und  sHihttu  eine  Art  Alaun  :  >>  s^^r.  SekM}  [akk.  tß-
=== AKD nabatu ===
```


## [2026-09-07T17:40:49.653Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== FSD3 65700-65725 ===\"; sed -n '65705,65722p' FSD_vol3.txt\necho \"=== awk page count AKD ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' AKD.txt"
}
```


### [2026-09-07T17:40:50.927Z] TOOL RESULT

```
=== FSD3 65700-65725 ===
which Is collected separately during the diHtlllatlon and sold
as crude naphtha, or again sepiiraied by distillation Into
gasoline, rehned naphtha, and benzene), shale«n. (dlsillled
from bituminous sluUas or schists), wood*u. (same os
MBTUTL ALfOllUL)
I’liny mnntions tho oil of a sprinc at ARriKcntum, Hinly and
atuUw that it waa collootod and UHcd fur buniiiiK in larnim ns a
HulMtitiiti* for nil 11«* diHtiiiiruiMhn*i tliiM oil frinn naphttui, win. Ii
liL* HayN wan ton liaht and inHaniinnhli* for niirh a umi* ( >1 naphtha,
henitinlionNaloraiityin ‘I’arthia (ahniit ihgaounuiiof lli«<Induril
E H 1>ana i^cjicriptiBr AfiruruZ pt viii.9*l.UlU [was 18UU ]
fL , < Ur naphtha, v. Ar nafth 1
- Bathirate or Boghead naphtha* the naphtha cIIh-
tlllod from the Boglieurl shale of 'rorlmri Hill, Hcotluiiil.
— crude n.* unreiined iietroleum-naphtha — naph'tha*
gas"* n lllumluatliig-gaH charged with the dociiuiposeil
vapor of naphtha n.-ship* n A vessel curry lug uuphlhu
aaph'thn-cene, l nurthe-sln, 2 ii&rtiiu-cf!n. n f htm A
=== awk page count AKD ===
111
```


## [2026-09-07T17:41:05.927Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\nawk 'NR>=65600 && NR<=65760' FSD_vol3.txt | grep -n -E '^[0-9]{3,4}$|1649|1648|1650' | head\necho \"--- formfeeds vol3:\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' FSD_vol3.txt\necho \"--- search 1649 marker context\"; grep -n -E '^\\s*164[0-9]\\s' FSD_vol3.txt | head"
}
```


## [2026-09-07T17:41:07.164Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== SKT 344 naphtha context ===\"; grep -n -B4 -A4 'naphtha' SKT.txt | head -40\necho \"=== PHN naphte entry ===\"; sed -n '7890,7915p' PHN.txt"
}
```


### [2026-09-07T17:41:07.223Z] TOOL RESULT

```
--- formfeeds vol3:
697
--- search 1649 marker context
```


### [2026-09-07T17:41:07.274Z] TOOL RESULT

```
=== SKT 344 naphtha context ===
23686-Mantnatha. from  Greek  from  Syrieu  :  abbot,
23687-BlftintQOD.
23688-\  frmm  Latin  fr»m    Greek  from abbey,  damson.
23689-Italian    from    Sjrriae :
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
23691-BvM    Latin  from    Creek  from JMper,  myrrh,  nitre. from  Italian  from  Latin  from ^Arakie:  diaper.
23692-Greek  from  Arabic  \  dra-
23693-French  from  Latin  from  Arakie;  amulet, chtroise,  sarcenet  ^sarsnet).
23694-Low  lAtin  from  Ar&he:  Algebra, aaraccn.
=== PHN naphte entry ===
savoir : 1^ à l'aube du jour, ou quarante-cinq minutes avant
le lever du soleil ; a"* à midi ; mais on ne commence cette prière
que quarante minutes après le passage du soleil au méridien ;
3** au moment qui sépare en deux parties égales l'intervalle de
midi au coucher du soleil ; &^ vingt minutes après le coucher
du soleil; 5** la dernière prière se fait environ deux heures
après la précédente. (Voyez le Dictionnaire turc-français de
M. Bianchi, au mot jW nam4z.) Chez les Arabes, on se sert
du mot iijXtf ou 5^^ [«'a/a<] dans le même sens.
NAPHTE,8. m.(A.)
ki> [f'o/i'] Nom d'un bitume liquide, très-subtil et Irès-inflam-
mable, dont on faisait autrefois certaine sorte de feux d'arti-
fice, appelés yeux grégeois, et que l'on ne pouvait éteindre avec
l'eau. — Quelques dictionnaires donnent naphtiie, calqué sur
le grec vd(pOa ; mais ce dernier mot n'est lui-même qu'une trans-
cription de l'arabe nnft\ également employé pour désigner284 NAR
V huile de pétrole. — Suivant le géographe arabe Edrisi,*le
naplïte existait jadis en abondance près de la ville de Hit en
Ghaldée; Ebn Hawkal, de son côté, dit que Ton en trouve
aussi beaucoup dans les montagnes de Ferganah, qui font
partie du Turkestan.
NARCISSE, s. m. (p.)
(j««5^ [nergtiîs] en persan, et (y^^j^ [nardjù] en arabe. Nom
d'une plante bulbeuse dont il existe un grand nombre d'espèces
qui servent à Tornement des jardins. Les poètes orientaux
aiment à comparer la beauté de l'œil d'une mattresse avec la
```


## [2026-09-07T17:41:16.934Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\ngrep -n -i 'napht' SKT.txt | head -20\necho \"=== around Naphtha entry ===\"; grep -n -i -E 'Nap[hti]' SKT.txt | head -30"
}
```


### [2026-09-07T17:41:16.996Z] TOOL RESULT

```
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
=== around Naphtha entry ===
667:AnapiBst.  Anapest,  a  foot  in  prosody. (Gk.)  L.  ana/irs/us.  ■•  Gk.  ufawaiarct, struck  back,  rebounding ;  because  it  is  th^ ret'erse  ufa  ilaclyl.  — Gk.  Avaxtdttv,  lo  strike back.  —  QV.ilva,  back ;  and  maiuv,  to  stnkb
842:inopt,  foolish.  (F.-L.)  XVII  cent.- O.  V. ineptt,  —  h.iniptus^  improper,  foolish. —  L.  (>/•,  oot ;  and  aptus,  fit.  (Aliio  inapt^ from  m-.  notj  and  apt.)  And  see  Option. Aquatio.  (L.)  L.  aquaticui,  pertaiuiug to  water.— L.  otjua,  water.
2872:prooept.  (F.-L.)  O  ¥.  prtcrpte.'^'U /ntiffifum,  a  prescn bed  rule.  —  L..prtectpfHtt pp.  of  praci/rre.  to  take  beforehand,  |^ve rules.— L«  /rt«,  before;  captrt,  to  tahr* Der.  pnapt-ar.
9740:knave,  a  boy.  ^ivont,  sl\  fellow.  (£. ; ptrhafs  C.)  M.  E.  huiui  \knavt\  a  boy, servant.  A.  S.  cnafa^  older  form  cnafa^ a  boy.  (So  also  Do.  knaaf,  a  lad,  ser- i-ant ;  Icel.  knapi,  scr\*anl-lioy ;  G.  knabe^ boy.)  All  of  Celtic  origin  (the  Celtic  boys being  servants  to  the  Teutons);  cf.  Gnel. enaf^chf  a  yomigster,  a  stout  smart  boy, orig.  an  adj.  signifying  knobby,  lumpy, stout  \  from  the  sb.  rna/,  a  knob.  We may  therefore  regard  it  ns  ultimately  a dcri>'ative  of  knop ;  see  Ijelow.
10734:iUuminate,  to  enlighten.  (L.)  From pp.  of  L.  illuminapt,  to  throw  light  upon.
11093:Map.  (F.-L.)  The  oldest  mam  r sented  the  world,  and  were  calleii  m mounttt.  This  is  a  F.  form  of  aw mutuii,  map  of  the  world.  L.  an meant  a  napkin,  hence  a  painted  clolh.: apron.  (F.  -  L.*)  Formerly  tutf^ O.  F.  naptrmtj  a  large  cloth ;  angmcfln form  of  O.  F.  napt,  a  cloth  (F.  m^fi Low  L.  napa,  corraptioD  of  L.  m^ napkin,  cloth.
11094:napery.  linen  for  the  table  (F.  m O.  F  naptrit.^ljoMt  L.  naparia,  the  fl in  a  household  for  keening  toble-liai Low  L.  napa,  a  cloth  (aoove^.
12152:(U-Gk.-Arnb  )     X^Mfk- li^.""Arab.  naftt  nifi,  naph-
20048:TranapiououB ;  mtc  Sp«oiei.
20049:Tranapire  ;  s.cc  Spirit.
23690:ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  attar J  aximutb,  carob-tree,  elixir,  emir, iC^ra,  hookah  t.hooka),  noudah I,  jerboa,  koran,  Mahometan  (Mo- \n\  moonshte,  moslem,  muezzin, idir,  otto,  rack  (5),  rayah,  T>'Ot. ulam),  sheik^  sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner). fam  Creek  from  Arabic :  naphtha,
```


## [2026-09-07T17:41:24.293Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '12145,12160p' SKT.txt"
}
```


### [2026-09-07T17:41:24.383Z] TOOL RESULT

```
(F.-U;  owrfE)     F.  /«r. tvc.  over  ;  and  E.  nami. K&nkln,  a   kind  of  cotton .)     £>o  called  from  Nankin^
%  ahort  »lcep.    (E,)      ME.
rb,   to   dote.     A.S.  hn^tf-piant
Allied    to   A.  S.  kmpian,
f,  droop,   Icel.   knipn^i,   to
surface  of  cloth.    (C.) Knap.
tftblC'linen  i  see  Map.
(U-Gk.-Arnb  )     X^Mfk- li^.""Arab.  naftt  nifi,  naph-
Map.
Narootlo.
Fucing  stnpor.   (F. •■Gk.)
r.  —  Gk.  mpifvriuM,  l>enumbiug.
I  brnorob:  ra^inUr,  I  grow
\t  Dumbness,  orig.  coo-
traction;  put  for  avAp*nj,  i.e.  contraction. Sec  8 Dare.
narcissuo.  a  flower.    (L.  —  Ck.)    L. narcissus.  —  Gk.  yaptnocm ;   named  from it«  narxotic  properties. Ward,  an  unguent.  (F.  — L.  — Gk.  — Pen.
```


## [2026-09-07T17:41:52.442Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/nabb\" \\\n \"https://www.etymonline.com/word/neb\" \\\n \"https://www.etymonline.com/word/nipple\" \\\n \"https://www.etymonline.com/word/nibble\" ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 347 Nabja entry (neb/nib/nipple/nibble)\"; done"
}
```


## [2026-09-07T17:41:53.801Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== SNS page tags near 290 ===\"; grep -n '\\[pdf page 29[0-9]\\]' SNS_pages.txt | head\necho \"=== SNS نیم ===\"; grep -n 'نیم' SNS_pages.txt | head -20"
}
```


### [2026-09-07T17:41:55.548Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/nabb
/home/sfmqrb/git/rishe/data/verification/sources/web/50c1ce8943c8b454.txt
### https://www.etymonline.com/word/neb
/home/sfmqrb/git/rishe/data/verification/sources/web/a0eb5f992ca9a002.txt
### https://www.etymonline.com/word/nipple
/home/sfmqrb/git/rishe/data/verification/sources/web/c8812b11c0ea7aac.txt
### https://www.etymonline.com/word/nibble
/home/sfmqrb/git/rishe/data/verification/sources/web/54d0e2be153a948a.txt
```


### [2026-09-07T17:41:55.607Z] TOOL RESULT

```
=== SNS page tags near 290 ===
=== SNS نیم ===
```


## [2026-09-07T17:41:59.804Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/\necho \"### nabb\"; grep -n -i -A8 'Etymology' 50c1ce8943c8b454.txt | head -30\necho \"### neb\"; grep -n -A8 'neb (n' a0eb5f992ca9a002.txt | head -25\necho \"### nipple\"; grep -n -A6 'nipple (n' c8812b11c0ea7aac.txt | head -20\necho \"### nibble\"; grep -n -A6 'nibble (v' 54d0e2be153a948a.txt | head -20"
}
```


### [2026-09-07T17:41:59.882Z] TOOL RESULT

```
### nabb
### neb
23: neb (n.) 
24-
25- "beak or bill of a bird," Old English nebb "beak, nose; human face, countenance; beak-shaped thing," from Proto-Germanic nabja "beak, nose" (source also of Old Norse nef "beak, nose," Middle Dutch nebbe "beak," Old High German snabul , German Schnabel "beak," Old Frisian snavel "mouth"), which is of uncertain origin.
26-
27- Entries linking to neb 
28-
29- nib (n.) 
30-
31- 1580s, "beak or bill of a bird," Scottish variant of neb "beak or bill of a bird." Perhaps influenced by nibble (v.). Meaning "point" (of a pen or quill) is recorded by 1610s ( neb in this sense is from 1590s).
### nipple
23: nipple (n.) 
24-
25- 1530s, nyppell , "protuberance of a mammalian breast," in a female the extremity where the milk-ducts discharge, alteration of neble (1520s), probably diminutive of neb "bill, beak, snout" (see neb ), hence, literally "a small projection." Used from 1713 of any thing or mechanical part that projects like a nipple. From 1875 in reference to the mouthpiece of an infant's nursing-bottle. Earlier words were pap (n.2), teat . A 16c.-17c. slang term for a woman's nipples was cherrilets .
26- also from 1530s 
27-
28- Entries linking to nipple 
29-
### nibble
23: nibble (v.) 
24-
25- "to bite gently; eat by gnawing off small bits," c. 1500, not found in Middle English; perhaps from Low German nibbeln "to nibble, gnaw," related to Middle Low German nibbelen , Middle Dutch knibbelen "to gnaw," source of Dutch knibbelen "to cavil, squabble." Related: Nibbled ; nibbling .
26- also from c. 1500 
27-
28- nibble (n.) 
29-
30: 1650s, "act of nibbling," from nibble (v.). As "a small bite, a morsel" from 1838.
31- also from 1650s 
32-
33- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
34-
35- More to explore
36-
```


## [2026-09-07T17:42:00.457Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\nhead -5 SNS_pages.txt; echo ---; grep -c 'pdf page' SNS_pages.txt; echo ---; grep -n 'nem\\|nēm\\|nim' SNS.txt | head -20"
}
```


### [2026-09-07T17:42:00.530Z] TOOL RESULT

```
    A
>l»>'i



---
0
---
12374:A»A^)^^ :sa * nim5 * iSn: w~<»^ 3 
12378:(*U *U^ : *) **ri ^- : sag nimfldan: Nfftfl ->3 
16009:— J- «^x*i . f*i:nem: ■*» 
31866:nimayisn 281/20-282/1 
31867:nimud 282/8 
33404:danem 78/19
```


## [2026-09-07T17:42:09.041Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '16000,16015p' SNS.txt\necho \"=== nabb page ===\"; head -40 /home/sfmqrb/git/rishe/data/verification/sources/web/50c1ce8943c8b454.txt"
}
```


### [2026-09-07T17:42:09.085Z] TOOL RESULT

```
, U.i "U^l, (^ ^tfU^T.^4 v bT) x^ mirang: ^*l 

: a«j<3m : T c-j j jbi^ , ^Sw^tp :Neryosang: a*?o^s| 

. l^-I **# iftaj ^ ij^ } \ J, .^u f b . ^1 Neryosang: 

•\X/A^ 

— J- «^x*i . f*i:nem: ■*» 
nym : A{AiWb. 1036') nfena-wSj^na&na- : t- 
• A-M*^^ lAjt/tH* -6/lf*5 LMiff.Man,!!!, 59) 



• T/TV<* (u-y^r) <^*— *i :n5masp: e>«-*»^» 
=== nabb page ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/nabb
FETCHED: 2026-09-07T17:41:54Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-07T17:42:17.229Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C7%AD\" --note \"page 347 Nabja root: Proto-Germanic *nabjǭ 'beak'\"; echo ---; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/nebb\" --note \"page 347 Old English nebb\""
}
```


## [2026-09-07T17:42:18.399Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && awk 'NR>=18470 && NR<=18500' BRT.txt | grep -o -E '10[23][0-9]' | head -20; echo \"--- lines\"; sed -n '18485,18492p' BRT.txt | cut -c1-200"
}
```


### [2026-09-07T17:42:19.512Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2e0ab965efebc167.txt
---
/home/sfmqrb/git/rishe/data/verification/sources/web/33ef22f314eb1b6d.txt
```


### [2026-09-07T17:42:20.787Z] TOOL RESULT

```
1035
1036
1037
1038
--- lines
np.  tKv  'vrscker*,  tük  'schön*,  air.  mä  'heilig'; vgl.  Ln>£N  Stnd,  60.
•  j.  naenaestar-  m.  'der  eifrig  strebt nach  — ,  sich  bemüht  um  —'  (Gen.)'*:  kuma- tanqm  hüxtanam  kvar^lanqm  ..tnahl  aibi.- antärö  'tsrö  ya^ariä  voAunam  mahl  "wir
I  preisen,  was  (von  andern)  wohl  gedacht . . ist,  wie  wir  (auch  selber)  uns  eifrig  um das  Gute  bemühen"  Y.J5. 2.
Nom.  ag.  mnt  eineni  Fnes.  7  (Int.)  ar.  *ttai- n^.i).  _  Vgl.  goL  >ui^  -Neid',  »hd.  «fJ 'Eifer,  Neid'  niw.*).  —  Pü.:  iamalän  ..  em apar  gri/lär  -  ia  ö  ^S  gtrem  -  ä
j.  naem  H.44:  lies  naem^m;  —  ntüin/a  N. //:  lies  Hoeca.
•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;
KompA.,  E.  —  aL  ntina-  Adj.  'der  eine  —  der andere;  hilb'i  np.  nfm  'halb;  Hälfte'.  —VgL iBed.  ai.  flW*a-  i)  Adj.,  a)  m.  und  got  Aifii '^lucvf',  ia&a  'iiipa^.  ■ — 
•  j.  haarvS^^pass  fraSa^shH  naemö.- "piÖTwa  tara%ustrS  N.  64.
```


## [2026-09-07T17:42:25.793Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T17:42:25.828Z] TOOL RESULT

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


## [2026-09-07T17:42:26.802Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/ && grep -n -i -A6 'Etymology' 2e0ab965efebc167.txt | head -25; echo \"=== nebb ===\"; grep -n -i -A5 'Old English' 33ef22f314eb1b6d.txt | head -20"
}
```


### [2026-09-07T17:42:26.864Z] TOOL RESULT

```
=== nebb ===
99: Old English 
100-
101: Toggle Old English subsection 
102-
103- 4.1 
104- Alternative forms 
105-
106- 4.2 
--
273: Old English
274- [ edit ] 
275-
276- Alternative forms
277- [ edit ] 
278-
--
364: Old English terms inherited from Proto-West Germanic 
365: Old English terms derived from Proto-West Germanic 
366: Old English terms inherited from Proto-Germanic 
367: Old English terms derived from Proto-Germanic
```


## [2026-09-07T17:42:29.728Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-07T17:42:29.768Z] TOOL RESULT

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


## [2026-09-07T17:42:31.216Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/ && sed -n '273,300p' 33ef22f314eb1b6d.txt; echo \"=== pgmc file ===\"; head -12 2e0ab965efebc167.txt"
}
```


### [2026-09-07T17:42:31.263Z] TOOL RESULT

```
 Old English
 [ edit ] 

 Alternative forms
 [ edit ] 

 neb 

 Etymology
 [ edit ] 

 From Proto-West Germanic *nabi , from Proto-Germanic *nabją . Akin to Old Norse nef , Middle Low German nebbe and Middle Dutch nebbe .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /nebb/ , [neb] 

 Rhymes: -ebb 

 Noun
 [ edit ] 

 nebb   n 

 face 
 late 10th century , Ælfric , "Saint Agnes, Virgin" 
 He gesette his tacn on minum nebbe þæt ic nænne oðerne ofer hine ne lufige. He hath set His token upon my face that I should love none other beside Him. 
=== pgmc file ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C7%AD
FETCHED: 2026-09-07T17:42:19Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-07T17:42:41.906Z] TOOL CALL #60: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C4%85\" --note \"page 347 Nabja root: Proto-Germanic *nabją 'beak'\" ; echo ---; cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== AFA نفط ===\"; grep -n -E 'نفط|naft|Naphta' AFA.txt | head -10\necho \"=== AFM نفط ===\"; grep -n 'نفط' AFM.txt | head -10\necho \"=== TAD نفط ===\"; grep -n 'نفط' TAD.txt | head -10\necho \"=== PLA naft ===\"; grep -n -i -E 'naft|نفط' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10"
}
```


### [2026-09-07T17:42:43.650Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/469f4ec1dec2d292.txt
---
=== AFA نفط ===
=== AFM نفط ===
3466:اي اتح كل اليا حتت مكل ܢ تشبه.رائحة النفط» , 
=== TAD نفط ===
368:مول 0 ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه 
=== PLA naft ===
19020:us naft: "Naphtha" aus pers. us naft mp. Yo' naft 1 aw. naphtha 2, 
19022:pers. näft: "Naphtha, Erdpech'"' ar. naft, aram.s0»), tk. naft, neft 
19023:Hieraus griech. va va ,„ lat. naphtha, sp. nafta, frz. Nephtha, russ, 
19038:As- naft = naft a. v. 
19042:ana - naftiyya: "Feuerwerk" s. naft.
```


## [2026-09-07T17:42:50.112Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '19012,19045p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== page tag ===\"; awk 'NR<=19020 && /pdf page/' incoming/PLA/PLA_pages.txt | tail -1"
}
```


### [2026-09-07T17:42:51.443Z] TOOL RESULT

```
ei - na°nä® = naCna’ q. u. 


Fa -na°na® = na°nä° a. v. 
bb) - naffät: "derjenige, der Naphtha bereitet". 


us naft: "Naphtha" aus pers. us naft mp. Yo' naft 1 aw. naphtha 2, 
syr. N\a3 , mand. napt °. 
pers. näft: "Naphtha, Erdpech'"' ar. naft, aram.s0»), tk. naft, neft 
Hieraus griech. va va ,„ lat. naphtha, sp. nafta, frz. Nephtha, russ, 
neft, dtsch. Naphtha a 
Naphtha <Tassyr. >>) pers. > griech 5, 


e>- nufugß: Pl. v. ass nuffa q. v. 
ana - nufßa = näffa q. v. 


zer - nafrinag: "eine Süßigkeit'" pers. 6, wahrscheinlich aus pers. 


ferini "Reisbrei" 


As- naft = naft a. v. 


ti. 
ana - naftiyya: "Feuerwerk" s. naft. 


ee - nafif = nufga a. v. 
=== page tag ===
```


## [2026-09-07T17:43:03.226Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web/ && grep -n -i -A6 'Etymology' 469f4ec1dec2d292.txt | head -20; echo \"=== descendants ===\"; grep -n -A15 'Descendants' 469f4ec1dec2d292.txt | head -25"
}
```


### [2026-09-07T17:43:03.280Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
143: Etymology
144- [ edit ] 
145-
146: Uncertain. Has been taken as a derivative from *nabō ( “ nave ” ) , with sense development "nave" > "protuberance, knob" > "nose, beak", [ 1 ] as well as to Gaulish nebba ( “ bill ” ) . [ 2 ] Compare also Proto-Germanic *snabulaz ( “ snout ” ) , Lithuanian snãpas ( “ snout ” ) . ( Can this ( + ) etymology be sourced ?) 
147-
148- Pronunciation
149- [ edit ] 
150-
151- IPA ( key ) : /ˈnɑβ.jɑ̃/ 
152-
--
284: ^ Vladimir Orel ( 2003 ), “*naƀjan”, in A Handbook of Germanic Etymology ‎ [1] , Leiden, Boston: Brill , →ISBN , page 279 
=== descendants ===
77: Descendants 
78-
79- 1.4 
80- References 
81-
82- Toggle the table of contents 
83-
84- Reconstruction:Proto-Germanic/ nabją 
85-
86- Add languages 
87-
88- Reconstruction 
89-
90- Discussion 
91-
92- English 
--
217: Descendants
218- [ edit ] 
219-
220- Proto-West Germanic: *nabi 
221- Old English: nebb , neb ; nypel 
222- Middle English: neb ; *neble , *nypil , *neple 
223- Scots: neb ; nebbie ; nebbock 
224-
```


## [2026-09-07T17:44:09.648Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== KNT naima ===\"; grep -n -E 'naima|nai-ma|half' KNT.txt | head -15\necho \"=== IEC nema ===\"; grep -n -E '^n[eē]ma|nēmo-|naima' IEC.txt | head -10\necho \"=== WLD Bd2 naema/nebh ===\"; grep -n -i -E 'nebh|napta' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-07T17:44:09.729Z] TOOL RESULT

```
=== KNT naima ===
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1978:! Cf, the names of the states of the United States of America; about half of them are derived from aboriginal American languages, and the rest come directly or ulti- mately from English, German, Celtic, French, Spanish, Latin, Greek, Hebrew, and Indo-Jranian. For the OP place-names which can with certainty or with some prob- ability be interpreted etymologically, see Lex. s.vv. ? This section attempts only to list and classify the nouns and ethnic adjectives used as geographical terms in the OP texts; a complete list of the provinces of the Persian Empire, as given in the OP/texts, will befound in JNES 2.302-6, with discussion of the variations: The classifica- tion of Yadà DB 3.26, apparently the OP name for
4126:10 : naima : ava : kàma : tya : tunuvā : skaudais : r 11 афу : mia : kariyai$ : tya : rástam : ауа : mam : 12 kama : martiyam : draujanam : naiy : dausté : 4m 18 iy : naiy : manauviS : ату : (yàmaiy : dartana 14 ya : bavatiy : darsam : dárayàmiy : manaha : 15 uvaipasiyahyà : darsam : xSayamna : amy : 16 martiya : hya : hataxSataiy : anudim : hakarta? 17 hyà : ауадай : paribaráàmiy : hya : 0° 18 máfayatiy : anudim : vinastahyd : ava
5582:from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
=== IEC nema ===
=== WLD Bd2 naema/nebh ===
21435:..Enkel, Kachkomme'', av. napdt-, naptar-, ap. napfit- ds., ai. aparn napaf, 
21453:nebh- — nem- 
21478:nebh- „bersten“. 
21491:Bohrer“ (s. vielmehr u. enebh- „l^aheV'); nabhate ist auch nicht als „platzen : 
21492:,,heryorquellen‘‘ mit enebh- „feucht, Wasser, Dunst, Kebel** gleichzusetzen. 
33111:s. u. ak- „spitz'‘; gegen Anreihung von ofjopa^ s. u. enebh- „Nabel“). 
45061:DaB zur^-Erw. sn-ep- yon ai. sndp-ayati^ -ana- auch av. napta- ,,feucht^‘, 
45064:dann nach ar. nabQt)- „feucht“, s. nebh- ..feucht *) ist weniger wahrscheinlich, als
```


## [2026-09-07T17:44:19.564Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '45055,45070p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"===\"; sed -n '21486,21496p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== WLD naema half ===\"; grep -n -E 'naema|nēma-|nema-' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5"
}
```


### [2026-09-07T17:44:19.674Z] TOOL RESULT

```
693 


„iia6“ (s. Brugmann IF. 20, 222 m. Lit.; vdto^ nicht besser zu got. natjan 
„iietzen% ahd. na^ „na6‘‘ unter idg. Fick III^ 291). 

DaB zur^-Erw. sn-ep- yon ai. sndp-ayati^ -ana- auch av. napta- ,,feucht^‘, 
apers. Ndnag ' fj xgi^vt] im rcbv OQoyv rrjg HeQoidog loTOQeXxai, fj q)eQOVGa rd 
€L(poda [i. e. to vd(p^a] Hes., np. neft Naphtha * gehore (der Mangel des anl. s- 
dann nach ar. nabQt)- „feucht“, s. nebh- ..feucht *) ist weniger wahrscheinlich, als 
da6 diese Worte anfanglich zu nehh- gehoren {Ndmag^ wenn zuverlassig, dann 
mit p nach *snap-) ; ebenso zweideutig lat. NejMmus „der Gott der springen- 
den Quellen, der fliefienden Gewasser und der Briicken, sowie (erst als 
Vertreter des gr. Poseidon? s. Gl. 3, 364) des Meeres“ als Ableitung eines 
^‘sneptu-s Oder "^nehQiytu-s „Nasse“ (s. uber diese Formen Wilhelm BB. 
12, 104, Kretschmer Einl. 133, Horn KZ. 32, 584, Johansson IF. 4, 143, 
===
«chalend‘' anreihen ; dies ist fur ncefr ansprechender als fiir das wegen 
«eines anl. s- und der doch wesentlich andern Bed. eher fernzuhaltende S 7 iob, 

Zu ai. nabJiate nicht nach Fick I^ 97, 502 ai. dhliri- „Haue, Hacke, 
Bpater* (Bed. I) und aisl. nafarr = ags. nafugclr, ahd. nabager „grober 
Bohrer“ (s. vielmehr u. enebh- „l^aheV'); nabhate ist auch nicht als „platzen : 
,,heryorquellen‘‘ mit enebh- „feucht, Wasser, Dunst, Kebel** gleichzusetzen. 

1* nem- „zuteilen, nehmen‘' (aus ,,sich zuteilen“ oder von der gemeinsamen 
Vorstellung der hingestreckten Hand); von „zuteilen“ aus z. T. „rechnen, 
zahlen (Geldwesen)“. 
=== WLD naema half ===
```


## [2026-09-07T17:45:12.693Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/\necho \"=== HRN nok ===\"; grep -n -E \"\\bn[oū]k\\b|nūl|\\bnol\\b\" HRN.txt | head -5\necho \"=== HUB nok ===\"; grep -n -E \"\\bnuk\\b|\\bnok\\b\" HUB.txt | head -5\necho \"=== CHEUNG nok ===\"; grep -n -E 'nauka|nōk' CHEUNG.txt | head -5\necho \"=== IEC nabja ===\"; grep -n -E 'nabja|nebb' IEC.txt | head -5\necho \"=== POK nabja/snab ===\"; grep -n -E 'snab|nabja' POK_full.txt | head -5"
}
```


### [2026-09-07T17:45:12.807Z] TOOL RESULT

```
=== HRN nok ===
=== HUB nok ===
=== CHEUNG nok ===
=== IEC nabja ===
=== POK nabja/snab ===
78877:f. are Germanic snub-, snup-, snud-, snut-, snug-, snuk- lautmalend (as also snab-, snap-,
```


## [2026-09-07T17:45:17.943Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '78870,78880p' POK_full.txt | cut -c1-300"
}
```


### [2026-09-07T17:45:18.006Z] TOOL RESULT

```
as o^extension from sneu- one understands Middle Irish 5/7i7ao'(also FIN) 'river'; 
'caesaries' ('*herabflieftend'). Middle High German s/7^z 'catarrh', Norwegian snott. Old 
English gesnottu. 'Katarrh', Old Icelandic snyta. Old High German snuzen. Modern High 
German schneuzen, Norwegian snutm. 'snout'. Modern High German Schnauze' snout '; 

with yo; Middle High German snupfe. Old Icelandic 5/70/0/7© 'catarrh'. Middle High 
German snu fen ^wheeze', snuben^pant, sniff, snort' ; after Wissmann, Nom. postverb. 178 
f. are Germanic snub-, snup-, snud-, snut-, snug-, snuk- lautmalend (as also snab-, snap-, 
snad-, snat-, snak-, ebda. 187 f.), after Johannesson 223 f. belong sie to snu- 'pant, sniff, 
snort, pusten', also to the above *sneu-\
```


## [2026-09-07T17:45:23.381Z] AGENT

Now I'll write the verification file.


## [2026-09-07T17:53:18.455Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-347.json",
 "content": "{\n  \"pdf_page\": 347,\n  \"book_page\": 317,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nabatu\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Akkadian nabāṭu 'to shine, flare brightly' (G-stem, root n-b-ṭ), whence the noun napṭu / nabṭu 'naphtha, petroleum'\",\n      \"note\": \"The Akkadian verb nabāṭu 'to shine brightly' is real and the language label and gloss are correct; the connection of the noun napṭu 'naphtha' with it (the 'flaring' substance) is the standard Assyriological view and is exactly what Mo'in's footnote to Borhān-e Qāṭeʿ p. 2155 reports from an Arabic-Semitic etymological dictionary ('نفط: اصل آن اکدی است بصورت فعلی نباطو بمعنی درخشید، روشن کرد، تابید'). It is marked 'plausible' rather than 'confirmed' only because Nourai's own cited page (Zimmern, AKD p. 60) documents only the NOUN napṭu and says nothing about the verb; the verb-to-noun step comes from elsewhere. The chart's downstream shape (Akkadian → Aramaic → Arabic → Persian, and Aramaic → Greek → Latin/French) is the Semitist route of Zimmern and Klein; the Iranist tradition (Horn, Hübschmann, Pokorny, Walde-Pokorny, Asbaghi, Aryanpur) instead makes New Persian naft an inherited Iranian word from Avestan napta- 'moist' (PIE *nebh- 'damp, cloud'), and Nourai's own NOTE on node #4 records this. The two views cross at exactly one arrow — Arabic → Persian — which is the weakest link on the page (see node #4).\",\n      \"note_fa\": \"ریشهٔ اکدی nabāṭu «درخشید، شعله زد» واقعی است و برچسب زبانی و معنای آن درست است؛ نامِ napṭu/nabṭu «نفت» را نیز اکدی‌شناسان از همین ستاک می‌گیرند و معین در حاشیهٔ برهان قاطع (ص ۲۱۵۵) همین را از یک فرهنگ ریشه‌شناسی عربی-سامی نقل می‌کند: «نفط: اصل آن اکدی است بصورت فعلی نباطو بمعنی درخشید، روشن کرد، تابید». تنها از آن رو «با احتیاط پذیرفتنی» شمرده شد که خودِ مرجعِ نورایی (زیمرن، ص ۶۰) فقط نامِ napṭu را آورده و از فعل سخنی نگفته است. نکتهٔ اصلی این مدخل آن است که سنّت سامی‌شناسی (زیمرن، کلاین) نفتِ فارسی را وام‌واژهٔ آرامی/اکدی می‌داند، اما سنّت ایران‌شناسی (هرن، هوبشمان، پوکورنی، والده-پوکورنی، اصباغی، آریان‌پور) آن را واژه‌ای ایرانی از اوستایی napta- «نمناک» (ریشهٔ هندواروپایی *nebh- «نم، ابر») می‌شمارد؛ اختلاف دو سنّت درست در همان یک پیکان «عربی → فارسی» است (بند ۴).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/naphtha\",\n        \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AKD:60\", \"status\": \"partial\", \"note\": \"Zimmern, Akkadische Fremdwörter, p. 60 (AKD.txt line 975, immediately after the printed page-number '60'): 'akk. naptu Erdöl, Naphtha : > aram. naptā, neptā (> arab. naft, pers. neft, sowie griech. νάφθα usw., Naphtha)'. The page gives the noun and the whole loan-chain, but not the verb nabāṭu 'to shine' that Nourai puts in the root box.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. naphtha (KLN_1966.txt line 24952)\", \"stance\": \"supports\", \"note\": \"'— L., fr. Gk. νάφθα, fr. Aram. naphta, nephtā (whence also Arab. naft, Pers. neft), fr. Akkad. naptu, \\\"naphtha\\\". See Heinrich Zimmern … 1917, p. 60.' Klein makes Akkadian the ultimate source, exactly as the root box does.\"},\n        {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2155, Mo'in's footnote to نفت (ref_page.py BQT:2155 = pdf p. 238 of BQT_v4)\", \"stance\": \"supports\", \"note\": \"'... نفط: اصل آن اکدی است بصورت فعلی «نباطو» ... بمعنی: درخشید، روشن کرد، تابید، طلوع کرد ... و ازآنست کلمهٔ «نبطو» بمعنی نفط ... بنابراین سریانی، لغت اصلی این کلمه نیست بلکه اکدی اصل آن است و ازین بتمام زبانهای دیگر رفته' — the verb 'to shine' as the root, precisely Nourai's root box.\"},\n        {\"src\": \"MON\", \"where\": \"vol. 4 s.v. نفت (MON_part2.txt line 77506)\", \"stance\": \"supports\", \"note\": \"'نفت: [+ نفط، تر. نمناک، قیر] … از سوی دیگر در اکدی به صورت فعلی «نباطو» به معنی درخشید، روشن کرد، تابید، طلوع کرد؛ «نبطو» به معنی نفط آمده' — Mo'in repeats the Akkadian verb-etymology in his own dictionary.\"},\n        {\"src\": \"LKT\", \"where\": \"no. 1538 (LKT.txt line 3547)\", \"stance\": \"partial\", \"note\": \"Lokotsch prints both routes: 'pers. naft \\\"Erdpech, Naphtha\\\" [Horn NpEt S. 232, Nr. 1036], ar. naft [der Wurzel nafata \\\"sieden, wallen\\\" angepaßt; nach ZAkkFW 60 jedoch über aram. naptā aus ass. naptu \\\"Erdöl\\\"]' — i.e. Zimmern's Akkadian route is offered as the alternative to Horn's Iranian one.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Akkadian\",\n          \"words\": \"Nabtu, Naptu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Akkadian napṭu (also written nabṭu, Neo-Assyrian/Neo-Babylonian; cuneiform 𒉌𒆳𒊏) is the ordinary word for the naturally seeping bitumen-oil of Mesopotamia, used as lamp fuel and as an incendiary. Formally it is a *napṭ-u noun to the verbal root n-b-ṭ (nabāṭu 'to shine, flare'), with the regular Akkadian devoicing b > p before the voiceless ṭ, which is why both spellings nabṭu and napṭu occur — Nourai's double form 'Nabtu, Naptu' is therefore right, not a doublet of two words. Zimmern glosses it 'Erdöl, Naphtha'; Nourai's 'light, lamp oil' is a use-gloss rather than a lexical one.\",\n          \"derivation_fa\": \"واژهٔ اکدی napṭu (که nabṭu هم نوشته می‌شود، خط میخی 𒉌𒆳𒊏) نامِ همان قیر و روغن معدنیِ روان بین‌النهرین است که سوختِ چراغ و مادهٔ آتش‌افروزی بود. ساختِ آن *napṭ-u از ستاک n-b-ṭ (فعل nabāṭu «درخشیدن») است و «ب» در کنارِ «ط» بی‌واک شده و به «پ» بدل گشته؛ از همین رو هر دو صورت nabṭu و napṭu در متون آمده و آوردنِ هر دو در نمودار درست است، نه دو واژهٔ جدا. زیمرن آن را «نفت، روغن زمینی» معنی کرده است؛ «روشنایی، روغن چراغ» در کتاب معنایِ کاربردی است نه معنای واژگانی.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\"],\n          \"ref_check\": [\n            {\"ref\": \"AKD:60\", \"status\": \"supports\", \"note\": \"AKD.txt line 975, page 60: 'akk. naptu Erdöl, Naphtha' — the headword and gloss of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AKD\", \"where\": \"p. 60\", \"stance\": \"supports\", \"note\": \"'akk. naptu Erdöl, Naphtha : > aram. naptā, neptā …'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. naphtha\", \"stance\": \"supports\", \"note\": \"'… fr. Akkad. naptu, \\\"naphtha\\\"'.\"},\n            {\"src\": \"PLA\", \"where\": \"s.v. naft (PLA_asbaghi_1988_ia_djvu.txt line 19012ff.)\", \"stance\": \"partial\", \"note\": \"Asbaghi's closing formula 'Naphtha < assyr. > pers. > griech.' acknowledges the Assyrian/Akkadian starting point, though his own entry starts the chain in Persian.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Aramaic\",\n          \"words\": \"naftâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The word passed from Akkadian into Aramaic in the Achaemenid/Seleucid period as נַפְטָא / נִיפְטָא napṭā, nipṭā (Jewish Babylonian Aramaic) and ܢܰܦܛܳܐ / ܢܶܦܛܳܐ napṭā, nepṭā (Syriac), with the Aramaic determined-state ending -ā added to the borrowed stem napṭ-; the i-vowel of nipṭā/nepṭā is the usual Aramaic reduction of a in a closed unstressed syllable. Mesopotamia was Aramaic-speaking exactly where the naphtha seeps were (Hīt on the Euphrates, Babylonia), so the borrowing is a local, technical one; Zimmern lists it as one of his standard Akkadian culture-words in Aramaic.\",\n          \"derivation_fa\": \"این واژه در دورهٔ هخامنشی/سلوکی از اکدی به آرامی رفت: در آرامیِ بابلیِ یهودی נַפְטָא / נִיפְטָא napṭā، nipṭā و در سریانی ܢܰܦܛܳܐ / ܢܶܦܛܳܐ napṭā، nepṭā، با پسوندِ حالتِ معرفهٔ آرامی -ā بر ستاکِ وام‌گرفتهٔ napṭ-؛ واکهٔ i در nipṭā/nepṭā همان کاهشِ معمولِ a در هجای بستهٔ بی‌تکیه در آرامی است. چون چشمه‌های نفتِ بین‌النهرین (هیت بر فرات، بابل) درست در قلمروِ آرامی‌زبان بود، این وام‌گیری وام‌گیری‌ای بومی و فنّی است؛ زیمرن آن را در شمار وام‌واژه‌های فرهنگیِ اکدی در آرامی آورده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"supports\", \"note\": \"Klein p. 1027 s.v. naphtha: 'fr. Aram. naphta, nephtā … fr. Akkad. naptu' — the Aramaic node with both vocalisations, from Akkadian, exactly as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AKD\", \"where\": \"p. 60\", \"stance\": \"supports\", \"note\": \"'akk. naptu … : > aram. naptā, neptā' — the arrow Akkadian → Aramaic is Zimmern's own.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1027\", \"stance\": \"supports\", \"note\": \"'fr. Aram. naphta, nephtā … fr. Akkad. naptu'.\"},\n            {\"src\": \"AFA\", \"where\": \"grep 'نفط|naft|Naphta' in AFA.txt\", \"stance\": \"silent\", \"note\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, has no entry for this word under any of the spellings searched — he does not treat naft as an Aramaism.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"naft «نفط»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic نِفْط / نَفْط nifṭ, nafṭ 'petroleum, naphtha' (also 'Greek fire' and, later, a naphtha-throwing engine) is on the Semitist account a pre-Islamic borrowing of Aramaic napṭā from the Aramaic-speaking Iraqi oilfields, the -ā dropped as a foreign ending; once in Arabic it was reanalysed as a fiʿl-pattern noun of a native triliteral root n-f-ṭ and attached to the verb نَفَطَ nafaṭa 'to boil up, bubble out' (folk-etymology, as Lokotsch notes: 'der Wurzel nafata \\\"sieden, wallen\\\" angepaßt'). Klein, Zimmern and Wiktionary all draw exactly Nourai's arrow. Verdict 'plausible' because Asbaghi's specialist monograph on Persian loanwords in Arabic instead lists نفط among the Persian loans (ar. naft ← pers. naft), so the immediate donor — Aramaic or Persian — is disputed even though every party puts Akkadian at the head of the chain.\",\n          \"derivation_fa\": \"عربی نِفْط/نَفْط «نفت» (و در معنای دیرتر «آتش یونانی» و «نفت‌انداز») بر پایهٔ دیدگاه سامی‌شناسان وام‌واژه‌ای پیش از اسلام از آرامی napṭā است، از همان میدان‌های نفتیِ عراقِ آرامی‌زبان، با افتادنِ پایانهٔ بیگانهٔ -ā؛ سپس در عربی بر وزنِ فِعْل تحلیل شد و به ریشهٔ سه‌حرفیِ ن-ف-ط و فعلِ نَفَطَ «جوشید، برآمد» پیوند خورد — ریشه‌شناسی عامیانه‌ای که لوکوچ نیز به آن اشاره می‌کند. کلاین، زیمرن و ویکی‌واژه همین پیکانِ نورایی را می‌کشند. «با احتیاط پذیرفتنی» از آن رو که اصباغی در پژوهش ویژهٔ خود «وام‌واژه‌های فارسی در عربی» نفط را در شمار وام‌واژه‌های فارسی آورده است (ar. naft از pers. naft)؛ پس دهندهٔ بی‌واسطه — آرامی یا فارسی — مورد اختلاف است، هرچند همه سرِ زنجیره را اکدی می‌دانند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\",\n            \"https://en.wiktionary.org/wiki/naphtha\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"supports\", \"note\": \"Klein p. 1027: '… fr. Aram. naphta, nephtā (whence also Arab. naft, Pers. neft), fr. Akkad. naptu' — Arabic from Aramaic, as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. naphtha\", \"stance\": \"supports\", \"note\": \"'whence also Arab. naft'.\"},\n            {\"src\": \"PLA\", \"where\": \"s.v. naft (Asbaghi 1988; PLA_asbaghi_1988_ia_djvu.txt line 19016ff.)\", \"stance\": \"contradicts\", \"note\": \"'naft: \\\"Naphtha\\\" aus pers. naft, mp. naft ← aw. napta …; pers. nāft: \\\"Naphtha, Erdpech\\\" → ar. naft, aram. …, tk. naft, neft' — Asbaghi makes Arabic naft a Persian loan, the opposite arrow.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1538 (LKT.txt line 3547)\", \"stance\": \"partial\", \"note\": \"'ar. naft [der Wurzel nafata \\\"sieden, wallen\\\" angepaßt; nach ZAkkFW 60 jedoch über aram. naptā aus ass. naptu \\\"Erdöl\\\"]' — Lokotsch gives Nourai's route only as the alternative to a Persian one.\"},\n            {\"src\": \"AFM\", \"where\": \"grep 'نفط' in AFM.txt (only line 3466, a passing simile 'رائحة النفط')\", \"stance\": \"silent\", \"note\": \"Addi Shir's dictionary of Persian Arabisms has no headword نفط — he does not claim it as a Persian loan in Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"naft «نفط ، نفت»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both Persian spellings are right — the Arabicised نفط beside the naturalised نفت — but the arrow is wrong in the sources on both sides of the question. (a) Klein, whom Nourai cites here, does NOT derive Persian from Arabic: 'fr. Aram. naphta, nephtā (whence also Arab. naft, Pers. neft)' makes Arabic naft and Persian neft sister outcomes of Aramaic, not parent and child; Zimmern p. 60 likewise writes '> aram. naptā, neptā (> arab. naft, pers. neft)'. Wiktionary's tree goes Akkadian napṭum → Old Persian *naftah, i.e. Persian took it straight from Mesopotamia, centuries before Arabic existed as a donor. (b) The Iranist line rejects any borrowing at this point at all: Horn (Grundriss no. 1035, p. 232) derives neft from Avestan napta- 'feucht' beside Skt. √nabh- 'to burst, well up'; Pokorny puts 'npers. neft \\\"Naphtha\\\"' on p. 316 under *nebh- 'damp, water; vapour, mist, cloud' beside Av. napta- (*nab-ta-); Walde-Pokorny II 693 says the whole group Av. napta-, OP Νάπας (Hesychius), np. neft 'gehören anfänglich zu nebh-'; Aryanpur repeats it for a modern Persian readership. Hübschmann (Persische Studien no. 1035) is the honest sceptic: a *nabh- participle should be Avestan *nab-da-, napta- can only be an analogical remodelling, 'also liegt kein Grund zur Annahme einer Wrzl. naph vor. Ist das Wort überhaupt indogermanisch?', and he adds Armenian nawtʻ 'bitumen' (5th c.) and Gk. νάφθα. Decisively for the chart, the word is already Middle Persian: Manichaean Pahlavi nbt 'bitumen, naphtha' (cited in Mo'in's footnote after Hübschmann), so Persian had naft before any Arabic could give it. Nourai's own NOTE flags POK:316 and HRN:232; modern scholarship sides with them against the Arabic → Persian arrow, while keeping Akkadian as the ultimate source of the whole family.\",\n          \"derivation_fa\": \"هر دو املا درست است — نفطِ معرّب در کنارِ نفتِ فارسی‌شده — اما پیکان نادرست است و هیچ‌یک از دو اردوگاهِ منابع آن را تأیید نمی‌کند. یک: کلاین، که خودِ نورایی به او ارجاع می‌دهد، فارسی را از عربی نمی‌گیرد؛ او می‌نویسد «از آرامی naphta, nephtā (که عربی naft و فارسی neft نیز از آن‌اند)» یعنی عربی و فارسی هر دو خواهرِ یکدیگر و فرزندِ آرامی‌اند؛ زیمرن نیز در ص ۶۰ همین را می‌آورد. ویکی‌واژه راهِ اکدی napṭum → پارسی باستان *naftah را می‌کشد، یعنی فارسی آن را یکسر از بین‌النهرین گرفته است، قرن‌ها پیش از آنکه عربی دهنده‌ای در میان باشد. دو: ایران‌شناسان اساساً منکر وام‌گیری‌اند: هرن (ش ۱۰۳۵، ص ۲۳۲) نفت را از اوستایی napta- «نمناک» و در پیوند با √nabh- سنسکریت «ترکیدن، فوران کردن» می‌گیرد؛ پوکورنی در ص ۳۱۶ زیر *nebh- «نم، آب؛ بخار، مه، ابر» می‌آورد: «npers. neft \\\"Naphtha\\\"» در کنار اوستایی napta- (*nab-ta-)؛ والده-پوکورنی (ج ۲ ص ۶۹۳) می‌گوید این واژه‌ها «در اصل به nebh- تعلق دارند»؛ آریان‌پور همین را برای خوانندهٔ فارسی تکرار می‌کند. هوبشمان (ش ۱۰۳۵) شکّاکِ منصف است: اسم مفعولِ nabh- در اوستایی باید *nab-da- می‌شد و napta- جز بازساختِ قیاسی نیست، «پس دلیلی برای فرضِ ریشهٔ naph نیست. آیا این واژه اصلاً هندواروپایی است؟» و ارمنی nawtʻ (قرن پنجم) و یونانی νάφθα را نیز می‌افزاید. نکتهٔ سرنوشت‌ساز برای نمودار این است که واژه در فارسی میانه هم هست: پهلویِ مانوی nbt «قیر، نفت» (به نقلِ حاشیهٔ معین از هوبشمان)؛ پس فارسی نفت را پیش از هر تماسی با عربی داشته است. خودِ نورایی در یادداشت به POK:316 و HRN:232 اشاره کرده؛ پژوهش امروزی جانبِ آنان را می‌گیرد و پیکانِ «عربی → فارسی» را رد می‌کند، هرچند سرچشمهٔ نهاییِ همهٔ این خانواده را اکدی می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/naphtha\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%B7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"contradicts\", \"note\": \"Klein p. 1027 makes Persian neft a sibling of Arabic naft, both 'fr. Aram. naphta, nephtā' — not Persian from Arabic as the chart draws.\"},\n            {\"ref\": \"BQT:2155\", \"status\": \"partial\", \"note\": \"Mo'in's footnote 9 to نفت (BQT vol. 4 p. 2155) leads with the Iranian etymology — 'در اوستا napta (تر، نمناک)، هندی باستان nabh-, nabhate (شکافتن، ترکیدن) … اشتقاق ۱۰۳۵ [Horn]. هوبشمان گوید … دلیلی نیست که آن را از ریشهٔ nabh بدانیم. آیا این کلمه هندواروپایی است؟ ارمنی nawtʻ (قیر، نفت)، یونانی naphtha … در اوراق مانوی (پهلوی) nbt (قیر، نفت) … لاتینی naphtha' — and only then quotes the Akkadian view. It supports the ultimate Akkadian origin but not an Arabic → Persian step.\"},\n            {\"ref\": \"AKD:60\", \"status\": \"contradicts\", \"note\": \"Zimmern p. 60: '> aram. naptā, neptā (> arab. naft, pers. neft …)' — Arabic and Persian are parallel offspring of Aramaic in his notation, not a chain.\"},\n            {\"ref\": \"MON:4777\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang, s.v. نفت (MON_part2.txt line 77506): '[+ نفط، تر. نمناک، قیر] … در اکدی به صورت فعلی «نباطو» به معنی درخشید … «نبطو» به معنی نفط آمده' — gives the Akkadian etymon and the Iranian gloss 'نمناک', with no Arabic intermediary.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 1035, p. 232 (HRN.txt line 8977)\", \"stance\": \"contradicts\", \"note\": \"'1035. neft \\\"Naphta\\\". aw. napta- \\\"feucht\\\"; ai. √nabh-, nábhate \\\"spalten, platzen; hervorquellen\\\". LW. ar. naft' — Horn derives Persian from Avestan and treats Arabic naft as the loan FROM Persian.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 1035 (HUB.txt line 3579)\", \"stance\": \"contradicts\", \"note\": \"'Also liegt kein Grund zur Annahme einer Wrzl. naph vor. Ist das Wort überhaupt indogermanisch? — Hierzu arm. nawtʻ \\\"Erdharz, Erdpech, Erdöl\\\" (5. Jhd.), gr. νάφθα' — sceptical of the IE root but with no Arabic step; cf. also HUB.txt line 9056 'vgl. zd. napta- \\\"feucht\\\"'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 316, root 2. (enebh-): nebh- (POK_01.txt line 4657)\", \"stance\": \"contradicts\", \"note\": \"'napta- \\\"feucht\\\" (*nab-ta-) npers. neft \\\"Naphtha\\\"' listed under '*nebh- … \\\"feucht, Wasser\\\", daraus \\\"Dampf, Dunst, Nebel, Wolke\\\"' — Nourai's own NOTE cites this page correctly.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 693 (WLD_Bd2_1927_dli_106624_djvu.txt line 45061)\", \"stance\": \"contradicts\", \"note\": \"'… av. napta- \\\"feucht\\\", apers. Νάπας … np. neft Naphtha … als daß diese Worte anfänglich zu nebh- gehören' — Walde-Pokorny put the Persian word in the inherited IE group.\"},\n            {\"src\": \"ARY\", \"where\": \"s.v. the *nebh- root (ARY_pages.txt line 14849)\", \"stance\": \"contradicts\", \"note\": \"'واژه‌ی فارسی «نفت» نیز از همین واج‌ریشه است (سانسکریت NABHATE، اوستایی NAPTA، پهلوی …)' and note 3 'واژه‌ی انگلیسی NAPHTHA از همین واژه‌ی فارسی گرفته شده است' — Aryanpur reverses the direction entirely.\"},\n            {\"src\": \"PLA\", \"where\": \"s.v. naft (Asbaghi 1988)\", \"stance\": \"contradicts\", \"note\": \"'naft … aus pers. naft, mp. naft ← aw. napta' — Middle Persian naft posited, hence no Arabic donor.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2155, Mo'in's footnote\", \"stance\": \"partial\", \"note\": \"Reports both traditions side by side, including Manichaean Pahlavi nbt 'قیر، نفت'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"naphta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek νάφθα (náphtha, also νάφθας) is first found in the Hellenistic scientific literature about Mesopotamia — the incendiary 'naphtha' of Babylonia in Dioscorides, Strabo and 2 Maccabees 1:36 — and the aspirates φ, θ are the normal Greek rendering of a foreign p/f + ṭ cluster that Greek had no letters for. Klein derives it from Aramaic naphta/nephtā, which is Nourai's arrow and is geographically apt (the Seleucid Greeks met the substance and its name in Aramaic-speaking Babylonia). Wiktionary instead makes Greek νάφθα a borrowing of Old Persian *naftah. Both are live options; what is certainly wrong is the derivation Nourai attributes in his NOTE to Skeat — Skeat's concise dictionary in fact marks naphtha '(L. — Gk. — Arab.) L. naphtha. — Gk. νάφθα. — Arab. naft, nift', i.e. FROM ARABIC, not from Persian, and Arabic is chronologically impossible for a word already in Hellenistic Greek. So Nourai has misreported his own reference, and the modern view rejects Skeat's Arabic source in either version.\",\n          \"derivation_fa\": \"یونانی باستان νάφθα (و νάφθας) نخست در ادبیات علمیِ دورهٔ هلنیستی دربارهٔ بین‌النهرین دیده می‌شود — «نفتِ» آتش‌زای بابل در دیوسکوریدس، استرابون و مکابیان دوم ۱:۳۶ — و دمیده‌های φ و θ همان شیوهٔ معمولِ یونانی برای نشان دادنِ خوشهٔ بیگانهٔ p/f + ṭ است که یونانی حرفی برایش نداشت. کلاین آن را از آرامی naphta/nephtā می‌گیرد که همان پیکانِ نورایی است و از نظر جغرافیایی هم درست می‌نماید (یونانیانِ سلوکی این ماده و نامش را در بابلِ آرامی‌زبان شناختند). ویکی‌واژه در عوض νάφθα را وام‌گرفته از پارسی باستان *naftah می‌داند. هر دو پذیرفتنی‌اند؛ اما آنچه بی‌گمان نادرست است همان است که نورایی در یادداشت به اسکیت نسبت می‌دهد: فرهنگ فشردهٔ اسکیت naphtha را «(لاتینی ← یونانی ← عربی) از عربی naft, nift» می‌داند، نه از فارسی؛ و عربی برای واژه‌ای که پیش‌تر در یونانیِ هلنیستی هست، از نظر تاریخی ناممکن است. پس نورایی مرجعِ خود را نادرست نقل کرده و پژوهشِ امروزی سرچشمهٔ عربیِ اسکیت را در هر دو صورت رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/naphtha\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"supports\", \"note\": \"Klein p. 1027: 'naphtha … — L., fr. Gk. νάφθα, fr. Aram. naphta, nephtā' — Greek from Aramaic, as drawn.\"},\n            {\"ref\": \"FSD:1649\", \"status\": \"partial\", \"note\": \"The Funk & Wagnalls naphtha entry is in FSD_vol3.txt (lines 65689-65721) and its etymology reads (OCR-damaged) '[< L. naphtha, < Gk. …, < Ar. nafṭ]' — F&W route the Greek through Arabic, not Aramaic. The scan of vol. 3 carries no printed page numbers, so page 1649 itself could not be confirmed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027\", \"stance\": \"supports\", \"note\": \"'fr. Gk. νάφθα, fr. Aram. naphta, nephtā'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. naphtha (SKT.txt line 12152) and the appendix list of words 'from Greek from Arabic' (line 23690)\", \"stance\": \"contradicts\", \"note\": \"'(L. — Gk. — Arab.) … Arab. naft, nift, naph[tha]' — Skeat's source is Arabic, not the Persian that Nourai's NOTE attributes to SKT:344.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1538\", \"stance\": \"partial\", \"note\": \"'hieraus gr. νάφθα [ngr. τὸ νάφτι], lat. naphtha und sp. nafta, frz. naphte …' — Lokotsch feeds Greek from the Persian/Arabic word rather than from Aramaic.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 3 s.v. naphtha\", \"stance\": \"partial\", \"note\": \"Quotes Pliny on the naphtha of Agrigentum and of Parthia; etymology '< L. naphtha, … < Ar. nafṭ'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The empty pass-through node stands for French naphte (m.) 'naphtha', the form from which the chemical derivative naphtaline was coined in Paris in 1821 and which is what node #7 needs. Standard French lexicography takes naphte from Latin naphtha (attested in French from the 16th c. as a learned borrowing, with the Greek-Latin -phth- simplified in pronunciation), which makes the Greek → French arrow of the chart correct as an ultimate route but not a direct one. Nourai's own reference disagrees on the immediate donor: Pihan p. 283 s.v. NAPHTE marks it '(A.)' = Arabic, from نفط nafṭ, and argues that the spelling naphthe found in some dictionaries is 'calqué sur le grec νάφθα; mais ce dernier mot n'est lui-même qu'une transcription de l'arabe naft'.\",\n          \"derivation_fa\": \"این گرهِ تهی نمایندهٔ فرانسویِ naphte «نفت» است، همان صورتی که مشتقِ شیمیاییِ naphtaline در ۱۸۲۱ در پاریس از آن ساخته شد و گرهِ ۷ به آن نیاز دارد. فرهنگ‌های معیارِ فرانسوی naphte را از لاتینیِ naphtha می‌گیرند (وام‌واژه‌ای کتابی از سدهٔ شانزدهم، با ساده شدنِ تلفظِ خوشهٔ یونانی-لاتینیِ -phth-)؛ پس پیکانِ «یونانی → فرانسوی» در نمودار به عنوان مسیرِ نهایی درست است اما بی‌واسطه نیست. خودِ مرجعِ نورایی در دهندهٔ بی‌واسطه هم‌نظر نیست: پیان در ص ۲۸۳ ذیل NAPHTE آن را با نشانِ (A.) یعنی عربی می‌آورد، از «نفط»، و می‌گوید املای naphthe در برخی فرهنگ‌ها «به قیاسِ یونانیِ νάφθα» است، «حال آنکه خودِ آن واژهٔ یونانی چیزی جز آوانگاریِ عربیِ naft نیست».\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/naphtha\"],\n          \"ref_check\": [\n            {\"ref\": \"PHN:283\", \"status\": \"partial\", \"note\": \"Pihan p. 283 (PHN.txt line 7899): 'NAPHTE, s. m. (A.) نفط [naft] Nom d'un bitume liquide, très-subtil et très-inflammable … Quelques dictionnaires donnent naphthe, calqué sur le grec νάφθα; mais ce dernier mot n'est lui-même qu'une transcription de l'arabe naft'. The French word and page are right; Pihan's donor is Arabic, not Greek.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"p. 283 s.v. NAPHTE\", \"stance\": \"partial\", \"note\": \"French naphte from Arabic نفط; Pihan adds Idrīsī on the naphtha of Hīt in Chaldaea and Ibn Ḥawqal on Farghāna.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1538\", \"stance\": \"supports\", \"note\": \"'lat. naphtha und sp. nafta, frz. naphte, rum. nafta, naft; russ. neft'; dtsch. Naphtha' — the Romance forms including French naphte belong to this family.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"naftâlîn «نفتالین»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian نفتالین naftālīn is a 20th-century learned loan of French naphtaline (the name John Kidd's 'naphthaline' took in French chemistry from 1821, from naphte + -aline), taken over with the -īn that Persian regularly uses for French chemical -ine (cf. آسپیرین, گلیسیرین, ژلاتین). It is a re-entry, not an inheritance: the Persian word has the French compound's shape and its 19th-century chemical meaning 'naphthalene, mothballs', which the native نفت never had, and it is written with ت not ط, the mark of a modern European loan rather than an Arabised one. Mo'in lists it (with the doublet نفتالن) and defines it as the two-ring aromatic hydrocarbon distilled from coal-tar and used against clothes-moths.\",\n          \"derivation_fa\": \"«نفتالین» وام‌واژه‌ای کتابی از سدهٔ بیستم است از فرانسویِ naphtaline (نامی که «naphthaline»ِ جان کید در شیمیِ فرانسوی از ۱۸۲۱ گرفت، از naphte + -aline)، با همان پسوندِ -ین که فارسی برای -ine فرانسوی به کار می‌برد (قس آسپیرین، گلیسیرین، ژلاتین). این بازگشتِ واژه است نه میراثِ آن: صورتِ ترکیبیِ فرانسوی و معنای شیمیاییِ سدهٔ نوزدهمیِ «نفتالین، ضدِّ بید» را دارد که نفتِ بومی هرگز نداشت، و با «ت» نوشته می‌شود نه «ط» — نشانهٔ وام‌واژهٔ نوِ اروپایی در برابر معرّب. معین آن را (با گونهٔ «نفتالن») آورده و همان هیدروکربورِ حلقویِ دوحلقه‌ای می‌داند که از قطران و زغال‌سنگ می‌گیرند و برای نگه‌داشتِ لباسِ پشمی از بیدخوردگی به کار می‌رود.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/naphtha\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang, s.v. نفتالین (MON_part2.txt lines 77639-77650): 'نفتالین … (بز.) هیدروکربوری است حلقوی مرکب از دو حلقه بنزنی … در صنعت نفتالین را از قطران و زغال سنگ استخراج می‌کنند … برای محافظت لباس پشمی از خطر بیدخوردگی از آن استفاده می‌کنند؛ نفتالن.' The headword and gloss are Mo'in's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. نفتالین\", \"stance\": \"supports\", \"note\": \"Entry and chemical definition as quoted; the Latin-script gloss printed beside the headword is the European source-form.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. naphthalene\", \"stance\": \"supports\", \"note\": \"'Orig. naphthaline, coined by John Kidd fr. naphtha and chem. suff. -ine' — dates and derives the European word that Persian borrowed.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'نفتالین' in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no entry for the modern chemical term.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"naphtha\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin naphtha is a straight transliteration of Greek νάφθα, taken over in the technical prose of the early Empire: Pliny, Naturalis Historia 2.235 and 35.178 uses naphtha of the bitumen-oil of Babylonia and of Agrigentum, keeping the Greek ph and th letter for letter. Latin thus fixed the graphic shape -phth- that all the European descendants (French naphte, Spanish nafta, English naphtha, German Naphtha) inherit, even where the pronunciation simplified.\",\n          \"derivation_fa\": \"لاتینیِ naphtha آوانگاریِ مستقیمِ یونانیِ νάφθα است که در نوشتارِ فنیِ سده‌های نخستِ امپراتوری وام گرفته شد: پلینی در «تاریخ طبیعی» (۲.۲۳۵ و ۳۵.۱۷۸) naphtha را برای روغن-قیرِ بابل و آگریجنتوم به کار می‌برد و ph و th یونانی را حرف‌به‌حرف نگه می‌دارد. از همین رو صورتِ نوشتاریِ -phth- که همهٔ بازماندگانِ اروپایی (فرانسوی naphte، اسپانیایی nafta، انگلیسی naphtha، آلمانی Naphtha) به ارث برده‌اند در لاتینی تثبیت شد، حتی آنجا که تلفظ ساده گشت.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/naphtha\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1027\", \"status\": \"supports\", \"note\": \"Klein p. 1027: 'naphtha … — L., fr. Gk. νάφθα' — the Latin node is Klein's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027\", \"stance\": \"supports\", \"note\": \"'— L., fr. Gk. νάφθα'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1538\", \"stance\": \"supports\", \"note\": \"'hieraus gr. νάφθα …, lat. naphtha' — the Greek → Latin step.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 3 s.v. naphtha\", \"stance\": \"supports\", \"note\": \"The entry quotes Pliny distinguishing the oil of the Agrigentum spring from naphtha, 'as it burned at Ecbatana in Parthia', and etymologises '< L. naphtha'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"naphthalene ; naphthol\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are real English chemical terms but neither descends from Latin naphtha as the arrow suggests: they are 19th-century laboratory coinages on the English/scientific stem naphth-. Naphthalene was named naphthaline in 1821 by John Kidd, who first isolated it from coal-tar (naphtha + -ine); the l was inserted for euphony and the ending was later regularised to -ene on the pattern of benzene, whence also the clipped forms phthalic, phthalein (Klein). Naphthol (1860s) is naphth- + -ol, the suffix for hydroxyl compounds, and denotes the two hydroxynaphthalenes α- and β-naphthol used in dyestuffs. So the language and the words are right, and English naphtha itself does come from Latin — but the two words actually printed in this node are modern derivatives, not inherited forms.\",\n          \"derivation_fa\": \"هر دو واژه اصطلاحِ شیمیاییِ واقعیِ انگلیسی‌اند، اما هیچ‌یک — چنان که پیکان می‌نماید — از لاتینیِ naphtha به ارث نرسیده است: هر دو برساخته‌های آزمایشگاهیِ سدهٔ نوزدهم بر ستاکِ انگلیسی/علمیِ naphth-اند. naphthalene را جان کید در ۱۸۲۱، هنگام جدا کردنش از قطرانِ زغال‌سنگ، naphthaline نامید (naphtha + پسوندِ -ine)؛ «l» برای خوش‌آهنگی افزوده شد و پایانه بعدها به قیاسِ benzene به -ene قاعده‌مند گشت (کلاین). naphthol (دههٔ ۱۸۶۰) از naphth- + پسوندِ -ol برای ترکیب‌های هیدروکسیل‌دار است و آلفا- و بتا-نفتول را می‌رساند که در رنگ‌سازی به کار می‌روند. پس زبان و واژه‌ها درست‌اند و انگلیسیِ naphtha هم واقعاً از لاتینی آمده، ولی همین دو واژهٔ چاپ‌شده در این گره مشتق‌های نوین‌اند نه صورت‌های میراثی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/naphtha\",\n            \"https://www.etymonline.com/word/naphtha\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the claims were checked against Klein p. 1027 and Funk & Wagnalls instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. naphthalene, naphthyl; p. 1157 s.v. phthalein (KLN_1966.txt lines 24953, 28664)\", \"stance\": \"partial\", \"note\": \"'naphthalene … Orig. naphthaline, coined by John Kidd fr. naphtha and chem. suff. -ine. The l was inserted for the sake of euphony. For the ending of naphthalene see suff. -ene' — a coinage from English naphtha, not a Latin inheritance.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 3 s.v. naphthalene, naphthol (FSD_vol3.txt lines 65728-65761)\", \"stance\": \"supports\", \"note\": \"Both headwords present: 'naphthalene …' with the ring formula, and 'pertaining to, or derived from naphthol, like naphthalene'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Nabja\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Germanic *nabją 'beak, nose' (> Proto-West Germanic *nabi > OE nebb); of uncertain further origin, not a securely reconstructible PIE root\",\n      \"note\": \"The form and gloss are right, but the language label is not: Nourai's own source prints it in square brackets — '[nabja-. Bird's beak. Germanic root. Old English neb(b), beak: NEB, (NIB), (NIPPLE).]' (Watkins, AHD IE Roots) — and in Watkins's conventions square brackets mark precisely an entry that is NOT an inherited Indo-European root. Wiktionary calls *nabją 'uncertain', either a derivative of *nabō 'nave (of a wheel)' via 'protuberance, knob' or comparable to Gaulish nebba 'bill'; Pokorny treats the whole Germanic snab-/snap-/nab- 'snout, beak' group as onomatopoeic ('Germanic snab-, snap-, snad-, snat-, snak- lautmalend'). Klein alone posits an IE base *snab- 'beak; to snatch with the beak', but his witnesses are Germanic plus Lithuanian snãpas only. The Germanic branch of the chart (#3, #4) is sound; the Iranian branch (#1, #2) is not supported by any source and is the substantive problem of this entry.\",\n      \"note_fa\": \"صورت و معنای ریشه درست است، اما برچسبِ زبانی درست نیست: خودِ مرجعِ نورایی آن را در قلاب می‌آورد — «[nabja-. منقارِ پرنده. ریشهٔ ژرمنی. انگلیسی کهن neb(b) «منقار»: NEB، (NIB)، (NIPPLE).]» (واتکینز، ریشه‌های هندواروپاییِ AHD) — و در شیوهٔ واتکینز قلاب درست نشانهٔ آن است که مدخل ریشهٔ هندواروپاییِ به‌ارث‌رسیده نیست. ویکی‌واژه *nabją را «نامعلوم» می‌داند: یا مشتقی از *nabō «توپیِ چرخ» با تحولِ معنایی «برآمدگی، گره» ← «بینی، منقار»، یا سنجیدنی با گالیِ nebba «منقار». پوکورنی همهٔ خانوادهٔ ژرمنیِ snab-/snap-/nab- «پوزه، منقار» را نام‌آوا (lautmalend) می‌شمارد. تنها کلاین ریشهٔ هندواروپاییِ *snab- «منقار؛ با منقار قاپیدن» را فرض می‌کند، اما گواهانش جز ژرمنی و لیتوانیِ snãpas نیست. شاخهٔ ژرمنیِ نمودار (بندهای ۳ و ۴) استوار است؛ شاخهٔ ایرانی (بندهای ۱ و ۲) هیچ منبعی آن را تأیید نمی‌کند و اشکالِ اصلیِ این مدخل همان است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C4%85\",\n        \"https://en.wiktionary.org/wiki/nebb\",\n        \"https://www.etymonline.com/word/neb\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 768: '[nabja-. Bird's beak. Germanic root. Old English neb(b), beak: NEB, (NIB), (NIPPLE).]' — the form 'nabja-' and the gloss 'beak' are Watkins's, but he labels it a GERMANIC root and brackets it as non-IE, and he lists no Iranian and no 'nibble'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. [nabja-]\", \"stance\": \"partial\", \"note\": \"As quoted: Germanic root, bracketed, three English descendants only.\"},\n        {\"src\": \"POK\", \"where\": \"s.v. *sneu- (POK_full.txt line 78877)\", \"stance\": \"contradicts\", \"note\": \"'… are Germanic snub-, snup-, snud-, snut-, snug-, snuk- lautmalend (as also snab-, snap-, snad-, snat-, snak-)' — Pokorny has no PIE root *nabja-; he treats the group as onomatopoeic Germanic.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1467 s.v. snaffle, and p. 1027 s.v. neb (KLN_1966.txt lines 35695, 25084)\", \"stance\": \"partial\", \"note\": \"'… MLG., MDu. nebbe, \\\"beak\\\", OE. nebb … fr. I.-E. base *snab-, \\\"beak; to snatch with the beak, to snap\\\", whence also Lith. snãpas, \\\"beak, bill\\\"' — an IE base is posited, but as *snab- and on Germanic + Baltic evidence only.\"},\n        {\"src\": \"IEC\", \"where\": \"grep 'nabja|nebb' in IEC.txt\", \"stance\": \"silent\", \"note\": \"Mann's Indo-European Comparative Dictionary has no such root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"nok, nŭk «نوک»; nŭl «نول»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The words are real: نوک nōk (Classical), nuk (Iranian reading) 'beak, bill; nib, tip, point; spout', with the variants نوگ nōg and نک nuk, and نول nūl 'cutting beak; rim of a mouth, spout of a jug' (Mo'in). The derivation is not. Nothing connects them to Germanic *nabją, and the sound history forbids it: an Old Iranian *nabya- would have given Middle Persian *naw-/nab- and New Persian *nav-, never nōk with its final -k and its long ō from *au. Bailey — the very author Nourai cites — puts them elsewhere: under Khotanese nūha- 'top, point' (< *nauxa-, from the base nau- with suffix -ha-, beside naukya, nauca 'acme') he writes 'With Yidya nzeyo \\\"beak\\\", N.Pers. nauk, nol, Waxi nüčk \\\"beak\\\", Sarikoli misk', i.e. an inner-Iranian family *nau-ka- 'point, tip' shared with Sogdian nwk (node #2) and Khwarezmian nwk. Wiktionary gives نوک no etymology at all; Horn, Hübschmann and Cheung have no entry for it. So the word is Iranian, but the parent drawn here is wrong; نول is in addition probably a secondary l-variant of the same stem rather than an independent inheritance.\",\n          \"derivation_fa\": \"واژه‌ها واقعی‌اند: «نوک» nōk (فارسی کلاسیک)، nuk (خوانشِ ایرانی) «منقار؛ سرِ قلم، نوک، سرِ تیز؛ لولهٔ آبریز»، با گونه‌های «نوگ» nōg و «نک» nuk، و «نول» nūl «منقارِ برنده؛ گرداگردِ دهان، لولهٔ صراحی» (معین). اما ریشه‌شناسی نادرست است. هیچ منبعی این‌ها را به ژرمنیِ *nabją نمی‌پیوندد و تاریخِ آوایی نیز مانع است: ایرانیِ باستانِ *nabya- در فارسی میانه *naw-/nab- و در فارسی نو *nav- می‌داد، نه nōk با «ک» پایانی و «ō»ِ کشیده از *au. بیلی — همان نویسنده‌ای که نورایی به او ارجاع می‌دهد — این واژه‌ها را جای دیگری می‌نشاند: ذیل ختنیِ nūha- «قله، نوک» (از *nauxa-، از ستاکِ nau- با پسوندِ -ha-، در کنارِ naukya و nauca «اوج») می‌نویسد: «با یدغهٔ nzeyo «منقار»، فارسی نوِ nauk، nol، وخیِ nüčk «منقار»، سریکلیِ misk»؛ یعنی خانواده‌ای درون‌ایرانی از *nau-ka- «نوک، سر» که سغدیِ nwk (بند ۲) و خوارزمیِ nwk نیز از آن‌اند. ویکی‌واژه برای «نوک» هیچ ریشه‌شناسی‌ای نمی‌آورد؛ هرن، هوبشمان و چونگ مدخلی برایش ندارند. پس واژه ایرانی است اما پدرِ ترسیم‌شده نادرست؛ «نول» نیز به احتمال گونهٔ ثانویِ همان ستاک با «ل» است نه میراثی مستقل.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%DA%A9\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C4%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:143\", \"status\": \"partial\", \"note\": \"Indo-Scythian Studies VI p. 143 itself is not available; Bailey's own later Dictionary of Khotan Saka (the substitute on disk) s.v. nūha- 'top, point' (ISS_alt_DKS.txt line 3730) does contain the comparison Nourai must be citing — 'With Yidya nzeyo \\\"beak\\\", N.Pers. nauk, nol, Waxi nüčk \\\"beak\\\", Sarikoli misk' — but Bailey derives it 'From nau- with suffix -ha- < *nauxa-', an Iranian etymon, not from a Germanic *nabja-.\"},\n            {\"ref\": \"MON:4857\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang, s.v. نوک (MON_part2.txt line 81037): 'نوک: (قد. nūk) [- نک] (ا.) منقار پرندگان. سر تیز چیزی مانند سر قلم …' and s.v. نول (line 81070) 'نول: (ا.) منقار برنده. گرداگرد دهان. لول صراحی' — the words and glosses are confirmed, and 'قد. nūk' is the source of Nourai's second reading, but Mo'in offers no etymology at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS p. 190 s.v. nūha- 'top, point'\", \"stance\": \"contradicts\", \"note\": \"Groups N.Pers. nauk, nol with Khotanese nūha- < *nauxa-, Waxi nüčk, Yidgha nzeyo — an Iranian *nau- family; no Germanic or IE 'beak' root.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. نوک, نول\", \"stance\": \"partial\", \"note\": \"Words and glosses as quoted; no etymology.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 6133 (SOD.txt lines 48975-48977)\", \"stance\": \"partial\", \"note\": \"'6133 nwk B / nuk (nwq) ⊙Khwar. nwk / tip, point, beak' — the Sogdian and Khwarezmian cognates of the Persian word, again inner-Iranian.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'nok|nuk|nul|nol' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for نوک/نول.\"},\n            {\"src\": \"HUB\", \"where\": \"grep 'nuk|nok' in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien likewise has nothing.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"grep 'nauka|nōk' in CHEUNG.txt\", \"stance\": \"silent\", \"note\": \"Not a verb, so absent from Cheung's etymological dictionary of Iranian verbs.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"nwk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Sogdian word is genuine and Gharib's dictionary has it exactly as printed: entry 6133 'nwk (Buddhist Sogdian), nuk (nwq) — tip, point, beak', with the Khwarezmian cognate nwk noted. But drawing it straight from an Indo-European (in fact Germanic) *nabja- 'beak' is not supportable: Sogdian nwk is the East Iranian member of the same *nau-ka- 'point, tip' group as New Persian nōk (node #1), Khotanese nūha-/naukya 'acme', Wakhi nüčk and Yidgha nzeyo, per Bailey. Phonetically a *nabya- would have surfaced in Sogdian as *nβy-/*nby-, not nwk. The right picture is Proto-Iranian *nauka- > Sogd. nwk, Khwar. nwk, NP nōk — a horizontal set of Iranian cognates, not four independent descents from a Germanic root.\",\n          \"derivation_fa\": \"واژهٔ سغدی اصیل است و فرهنگِ قریب آن را درست همان‌گونه که چاپ شده دارد: مدخلِ ۶۱۳۳ «nwk (سغدیِ بودایی)، nuk (nwq) — نوک، سر، منقار»، با اشاره به هم‌ریشهٔ خوارزمیِ nwk. اما گرفتنِ آن یکسر از ریشه‌ای هندواروپایی (در واقع ژرمنی) به معنای «منقار» پذیرفتنی نیست: سغدیِ nwk عضوِ ایرانیِ شرقیِ همان خانوادهٔ *nau-ka- «نوک، سر» است که فارسی نوِ nōk (بند ۱)، ختنیِ nūha-/naukya «اوج»، وخیِ nüčk و یدغهٔ nzeyo نیز از آن‌اند (بیلی). از نظر آوایی *nabya- در سغدی *nβy-/*nby- می‌شد نه nwk. تصویرِ درست این است: ایرانیِ آغازین *nauka- ← سغدیِ nwk، خوارزمیِ nwk، فارسیِ نوک — مجموعه‌ای افقی از هم‌ریشه‌های ایرانی، نه چهار نسبِ جداگانه از ریشه‌ای ژرمنی.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D9%88%DA%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"not_found\", \"note\": \"Mo'in's entry نوک (MON_part2.txt line 81037) gives only '(قد. nūk) [- نک]' with no Sogdian comparison; the Sogdian form Nourai attributes to MON was not found in the lexicon volumes on disk. Gharib's Sogdian dictionary supplies it instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, no. 6133 (SOD.txt lines 48975-48977)\", \"stance\": \"supports\", \"note\": \"'6133 nwk B / nuk (nwq) ⊙Khwar. nwk / tip, point, beak' — the word, the reading and the gloss are confirmed.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. nūha-\", \"stance\": \"contradicts\", \"note\": \"Places the whole set (Khotanese nūha-, naukya 'acme', NP nauk/nol, Waxi nüčk) in an Iranian *nau- family, not in a Germanic 'beak' root.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. نوک\", \"stance\": \"silent\", \"note\": \"No Sogdian etymology given.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old English\",\n          \"words\": \"nebb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English nebb 'beak, bill; nose; face, countenance' (neuter, also spelt neb) is inherited from Proto-West Germanic *nabi, from Proto-Germanic *nabją, and stands beside Old Norse nef 'beak, nose', Middle Low German and Middle Dutch nebbe 'beak' and — with the s-mobile forms — Old High German snabul, German Schnabel 'beak', Old Frisian snavel 'mouth'. The West Germanic geminate -bb is the regular outcome of *-bj- (West Germanic gemination before *j), which is exactly why Old English has nebb where Old Norse, without that gemination, has nef. The word is well attested in the 'face' sense by the late 10th century (Ælfric, Life of St Agnes: 'He gesette his tacn on minum nebbe').\",\n          \"derivation_fa\": \"انگلیسی کهنِ nebb «منقار، نوک؛ بینی؛ چهره» (خنثی، با املای neb نیز) میراثِ ژرمنیِ غربیِ آغازینِ *nabi و آن از ژرمنیِ آغازینِ *nabją است و در کنارِ نورس کهنِ nef «منقار، بینی»، آلمانیِ میانهٔ سفلی و هلندیِ میانهٔ nebbe «منقار» و — با «s»ِ آغازیِ متحرک — آلمانیِ علیای کهنِ snabul، آلمانیِ Schnabel «منقار» و فریزیِ کهنِ snavel «دهان» می‌نشیند. مشدّدشدگیِ -bb در ژرمنیِ غربی برآمدِ قاعده‌مندِ *-bj- است (همگونیِ ژرمنیِ غربی پیش از *j)، و درست همین است که انگلیسی کهن nebb دارد و نورس کهن، که این مشدّدشدگی را ندارد، nef. واژه در معنای «چهره» از پایانِ سدهٔ دهم گواه دارد (الفریک، «قدیسه اَگنس»: He gesette his tacn on minum nebbe). ادعای نورایی در این بند درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nebb\",\n            \"https://www.etymonline.com/word/neb\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C4%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:143\", \"status\": \"not_checked\", \"note\": \"Bailey's Indo-Scythian Studies VI p. 143 is not available online or on disk (only his Dictionary of Khotan Saka), and a Khotanese Prolexis is in any case an unexpected authority for Old English nebb; the claim was checked against Klein, Skeat, Watkins and Wiktionary instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. neb (KLN_1966.txt line 25084)\", \"stance\": \"supports\", \"note\": \"'ME. nebbe, fr. OE. nebb, \\\"beak, nose, face\\\", rel. to MLG., MDu. nebbe, \\\"beak\\\", ON. nef, \\\"beak, nose\\\", Du. sneb, snavel, OHG. snabul … G. Schnabel, \\\"beak\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. neb (SKT.txt line 17602)\", \"stance\": \"supports\", \"note\": \"'neb, beak, nose. (E.) M. E. neb, face. A. S. nebb, face. + Du. neb, bill, nib, mouth; Icel. nef, nose; Dan. næb; Swed. näbb.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. [nabja-]\", \"stance\": \"supports\", \"note\": \"'Germanic root. Old English neb(b), beak.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"neb ; nib ; nipple ; nibble\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three of the four are right and the fourth is not, so the node takes the worse verdict. neb: Middle English neb(be) directly continues OE nebb, surviving in Scots and northern English for 'beak, nose, tip' — confirmed. nib: first recorded in the 1580s as a Scottish variant of neb, 'beak or bill of a bird', the sense 'point of a pen' from the 1610s; the final -b for -bb is a Scots by-form, not a separate word — confirmed. nipple: 1530s nyppell, an alteration of neble (1520s), a diminutive of neb 'bill, beak, snout', literally 'a small projection'; Wiktionary's descendant chain for *nabją has exactly OE nypel > ME *neble, *nypil, *neple, and Watkins lists (NIPPLE) under his nabja- entry — confirmed. nibble, however, is not from nebb at all: it appears only c. 1500 and is a Low German borrowing, 'perhaps from Low German nibbeln \\\"to nibble, gnaw\\\", related to MLG nibbelen, MDu. knibbelen \\\"to gnaw\\\"' (Etymonline; Klein 'Prob. of LG. origin'), and Nourai's own reference, Watkins, puts NIBBLE under a quite different entry, ken-2 'Low German nibbeln, to nibble' [Pok. 2. ken- 559] — not under nabja-, where the English descendants are only NEB, (NIB), (NIPPLE).\",\n          \"derivation_fa\": \"سه واژه از چهار واژه درست است و چهارمی نادرست، پس این گره حکمِ بدترین را می‌گیرد. neb: انگلیسیِ میانهٔ neb(be) دنبالهٔ بی‌واسطهٔ nebbِ انگلیسی کهن است و در اسکاتلندی و انگلیسیِ شمالی به معنای «منقار، بینی، نوک» مانده است — درست. nib: نخست در دههٔ ۱۵۸۰ به عنوان گونهٔ اسکاتلندیِ neb «منقارِ پرنده» ثبت شده و معنای «نوکِ قلم» از دههٔ ۱۶۱۰؛ «b»ِ ساده در برابر «bb» گونه‌ای اسکاتلندی است نه واژه‌ای جدا — درست. nipple: در دههٔ ۱۵۳۰ nyppell، دگرگون‌شدهٔ neble (دههٔ ۱۵۲۰)، مصغّرِ neb «منقار، پوزه»، لفظاً «برآمدگیِ کوچک»؛ زنجیرهٔ بازماندگانِ *nabją در ویکی‌واژه درست همین است: انگلیسی کهنِ nypel ← انگلیسیِ میانهٔ *neble، *nypil، *neple، و واتکینز نیز (NIPPLE) را ذیل nabja- می‌آورد — درست. اما nibble هرگز از nebb نیست: نخست حدودِ ۱۵۰۰ پیدا می‌شود و وام‌واژه‌ای از آلمانیِ سفلی است، «شاید از آلمانیِ سفلیِ nibbeln «جویدن»، هم‌خانوادهٔ nibbelenِ آلمانیِ میانهٔ سفلی و knibbelenِ هلندیِ میانه «جویدن»» (اتیمونلاین؛ کلاین: «احتمالاً از تبارِ آلمانیِ سفلی»)، و خودِ مرجعِ نورایی، واتکینز، NIBBLE را ذیل مدخلِ دیگری می‌گذارد: ken-2 «آلمانیِ سفلیِ nibbeln» [پوکورنی ۲. ken- ص ۵۵۹] — نه ذیل nabja- که بازماندگانِ انگلیسی‌اش تنها NEB، (NIB) و (NIPPLE)اند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/neb\",\n            \"https://www.etymonline.com/word/nipple\",\n            \"https://www.etymonline.com/word/nibble\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/nabj%C4%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 768 lists under [nabja-] only 'NEB, (NIB), (NIPPLE)'; NIBBLE appears at line 608 under a different root, 'ken-2 … 6. Low German nibbeln, to nibble: NIBBLE. [Pok. 2. ken- 559]'. So Nourai's own reference supports three of his four words and contradicts the fourth.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1027 s.v. neb, p. 1035 s.v. nib, nibble (KLN_1966.txt lines 25084, 25374)\", \"stance\": \"partial\", \"note\": \"neb 'fr. OE. nebb … Cp. nib, nipple'; but 'nibble … Prob. of LG. origin. Cp. MLG. nibbelen, NLG. nibbeln, knibbeln, gnibbeln, MDu. knibbelen, \\\"to gnaw\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. neb, nib, nipple (SKT.txt lines 17602-17605)\", \"stance\": \"supports\", \"note\": \"'nib, point of a pen. (E.) Another form of neb; see above.' — 'nipple, a teat. (E.) Formerly neble (Palsgrave); dimin. of nib or neb; see above.'\"},\n            {\"src\": \"WEB\", \"where\": \"grep in WEB_vol1.txt (A- volume only)\", \"stance\": \"silent\", \"note\": \"Webster's 2nd ed. vol. 2 (M-Z) is not available on disk, so the N words could not be checked there.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Naěma\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Avestan naēma- 'half; side' (Bartholomae, AiW col. 1036); Proto-Iranian *naymah, Proto-Indo-Iranian *naymas, cognate with Sanskrit néma- 'the one, the other; half'\",\n      \"note\": \"The Avestan half of the label, the form and the gloss are all correct — Bartholomae col. 1036 has 'j. naema- 1) Adj. \\\"halb\\\" … 2) m. a) \\\"Hälfte, latus alterum\\\", b) \\\"Seite\\\"', with 'ai. nēma- … np. nīm \\\"halb; Hälfte\\\"'. The 'Old Persian' half of the label is not: naēma- 'half' is unattested in Old Persian, and the only OP form that looks like it is a different thing entirely — Kent's lexicon lists nai-mā (DNb 8, 10, 19) as the negative naiy plus the enclitic pronoun -mā 'not … me' (KNT.txt line 5582). Buck adds the caution that the Indo-Iranian word's further origin is 'orig. dub.' — there is no accepted PIE root behind it, so this root box is correctly labelled Iranian rather than Indo-European, unlike entry 1. The root's own added note that the word is cognate with Sanskrit nēma- 'half' is right and is exactly Bartholomae's and Buck's comparison.\",\n      \"note_fa\": \"نیمهٔ اوستاییِ برچسب، صورت و معنا هر سه درست است: بارتولومه در ستونِ ۱۰۳۶ می‌آورد «naema- ۱) صفت «نیم» … ۲) اسم الف) «نیمه، لنگهٔ دیگر»، ب) «سو، طرف»» و «سنسکریت nēma- … فارسی نوِ nīm «نیم، نیمه»». اما نیمهٔ «پارسی باستان» درست نیست: naēma- «نیم» در پارسی باستان گواهی ندارد و تنها صورتِ همانندِ آن چیزِ دیگری است — کنت در واژه‌نامهٔ خود nai-mā (DNb ۸، ۱۰، ۱۹) را ترکیبِ نفیِ naiy با ضمیرِ پیوستهٔ -mā «نه … مرا» می‌داند. باک نیز هشدار می‌دهد که خاستگاهِ دورترِ این واژهٔ هندوایرانی «در اصل مشکوک» است؛ پس هیچ ریشهٔ هندواروپاییِ پذیرفته‌شده‌ای در پسِ آن نیست و همین است که این جعبه‌ریشه — برخلافِ مدخلِ ۱ — به‌درستی ایرانی برچسب خورده و نه هندواروپایی. یادداشتِ خودِ ریشه دربارهٔ هم‌ریشگی با سنسکریتِ nēma- «نیم» نیز درست و همان سنجشِ بارتولومه و باک است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%85\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"HRN:239\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 1069, p. 239 (HRN.txt line 9234): 'nēm \\\"Hälfte, halb\\\". aw. naema- \\\"halb\\\" in naemō asn, naēme xšafni, Vd. 4, 45 … skr. nēma- \\\"halb\\\"; phlv. nēm, nēmak.' Exactly the root and the chain of this entry.\"},\n        {\"ref\": \"SYN:936\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms §13.24 'HALF', p. 936 (SYN.txt line 23830): 'Av. naéma- (NPers. ném) : Skt. nema- \\\"the one, the other\\\", also \\\"half\\\", orig. dub. Barth. 1036. Uhlenbeck 151.' — and the §13.24 table on p. 935 lists 'Av. naēma-' as the Avestan word for 'half'.\"},\n        {\"ref\": \"BRT:1036\", \"status\": \"supports\", \"note\": \"Bartholomae, AiW col. 1036 (BRT.txt line 18490, between the printed column numbers 1035 and 1037): 'j. naema- 1) Adj. \\\"halb\\\" … 2) m. a) \\\"Hälfte, latus alterum\\\" … b) \\\"Seite\\\" überhaupt', with the comparison 'ai. nēma- Adj. \\\"der eine — der andere; halb\\\"; np. nīm \\\"halb; Hälfte\\\"'. Buck cites the same column, which independently confirms Nourai's page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"AiW col. 1036\", \"stance\": \"supports\", \"note\": \"As quoted; also the many compounds aŋtara-naēma-, upara-naēma-, paurva-naēma- 'inner/upper/front side' at cols. 3251-15747, which show the 'side' sense.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §13.24, pp. 935-936\", \"stance\": \"supports\", \"note\": \"'Av. naéma- (NPers. ném) : Skt. nema- … orig. dub.'\"},\n        {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. naiy (KNT.txt lines 5582, 1654)\", \"stance\": \"contradicts\", \"note\": \"'nai-maiy (§36) DB 4.64. nai-mā DNb 8, 10, 19. nai-patimā (§133) …' — the only Old Persian naima is the negative naiy + enclitic -mā; there is no OP word naēma- 'half'.\"},\n        {\"src\": \"HRN\", \"where\": \"no. 1069, p. 239\", \"stance\": \"supports\", \"note\": \"As quoted, plus the Iranian dialect cognates 'kurd. nīw \\\"Hälfte\\\", vergl. nīwrōž \\\"Mittag\\\"; afγ. nīmāī; bal. nēmrōč, nēmšap \\\"Mitternacht\\\"'.\"},\n        {\"src\": \"IEC\", \"where\": \"grep 'nema|naima' in IEC.txt\", \"stance\": \"silent\", \"note\": \"Mann's comparative dictionary has no PIE entry for this word, consistent with Buck's 'orig. dub.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"něm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian nēm 'half' continues Avestan naēma- / Proto-Iranian *naymah with the regular Middle Iranian monophthongisation of *ai > ē (as in Av. daēza- > MP dēz, Av. baēšaza- > MP bēšaz). MacKenzie prints it 'nēm [PRG < A plg; nym | = M, N ~] half', i.e. the word is normally written with the Aramaic logogram PRG (Aramaic plg 'half') but also spelt phonetically nym, and it is the same in Manichaean and New Persian; the derivatives nēmag 'half, side, direction', nēm-rōz 'midday, south', nēm-tan 'middle of the body', nēm-asp 'centaur' are all Pahlavi already. Nyberg's glossary has nēm-rōč [nymlwc'; PRG YWM] 'midday; south' and cand ī nēm rōč 'about half a day', and the Šāyast nē Šāyast glossary entry 'nem / nym' cites AiW 1036 naēma- and Nyberg's Manual II 59 for it.\",\n          \"derivation_fa\": \"فارسی میانهٔ nēm «نیم» دنبالهٔ اوستاییِ naēma- / ایرانیِ آغازینِ *naymah است با تک‌واکه‌شدنِ قاعده‌مندِ *ai به ē در ایرانیِ میانه (چنان‌که اوستاییِ daēza- ← دِژ و baēšaza- ← bēšaz). مکنزی آن را چنین می‌آورد: «nēm [PRG < A plg؛ nym | = M, N ~] نیم»، یعنی واژه معمولاً با لوگوگرامِ آرامیِ PRG (آرامیِ plg «نیم») نوشته می‌شود اما املای آواییِ nym هم دارد و در مانوی و فارسی نو نیز همان است؛ مشتق‌هایِ nēmag «نیمه، سو، جهت»، nēm-rōz «نیم‌روز، جنوب»، nēm-tan «میانِ تن» و nēm-asp «کنتاور» همه پهلوی‌اند. در واژه‌نامهٔ نیبرگ nēm-rōč [nymlwc'; PRG YWM] «نیم‌روز؛ جنوب» و cand ī nēm rōč «نزدیک نیم‌روز» آمده، و مدخلِ «nem / nym» در واژه‌نامهٔ شایست نشایست برای آن به AiW ۱۰۳۶ (naēma-) و «راهنمای پهلوی»ِ نیبرگ ج ۲ ص ۵۹ ارجاع می‌دهد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2233\", \"status\": \"supports\", \"note\": \"Mo'in's footnote to نیم (BQT vol. 4 p. 2233 = ref_page.py BQT:2233, pdf p. 316 of BQT_v4): 'اوستا naēma- (نصف) در naēmāt, naēme (وندیداد …)، سانسکریت nēma- (نصف)، پهلوی nēm، nēmak، کردی nīw (نصف)، قس nīwrōž (نیمروز)، افغانی nīmāī، قس بلوچی nēmrōč … رک: اشتقاق ۱۰۶۹ [= Horn]' — the Pahlavi forms nēm, nēmak are named explicitly.\"},\n            {\"ref\": \"SNS:290\", \"status\": \"partial\", \"note\": \"The Šāyast nē Šāyast glossary does have the entry (SNS.txt line 16009): 'nem: … nym : (AiWb. 1036) nēma- ~ naēma- … (Nyberg, Man. II, 59)'. The scan carries no recoverable page tags, so page 290 itself could not be confirmed, but the entry and its authorities are there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 58 s.v. nēm (PHD.txt line 510; PHD_mackenzie.txt line 3704)\", \"stance\": \"supports\", \"note\": \"'nēm [PRG < A plg; nym | = M, N ~] half. ~ag [nymk! | N ~a] half, side, direction. ~-asp [-sp] centaur; astr. Sagittarius. ~-rōz [-lwc | M -rwc, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.vv. nēm-rōč and rōč (NYB_vol2_glossary.txt lines 2674-2675, 3326)\", \"stance\": \"supports\", \"note\": \"'nēm-rōč [nymlwc'; PRG YWM] midday 7¹⁸ … — south … MPrthPrs nymrwz; NP nīmrūz' and 'nēm rōč half a day 31⁷'; at line 2674 'pēš ~ ī before …, cf Av. antarāt naēmāt + gen.' — the Avestan ablative that Bartholomae's column also cites.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2233, Mo'in's footnote to نیم\", \"stance\": \"supports\", \"note\": \"'پهلوی nēm، nēmak' as quoted.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nîm «نیم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian نیم nīm 'half' is the direct continuation of Middle Persian nēm, with the regular New Persian raising of Middle Persian majhūl ē to maʿrūf ī (the same change that gives MP šēr > NP šīr, MP tēr > NP tīr), so that the spelling نیم now reads nīm in Iran while Dari and the classical tradition keep nēm. Wiktionary states the chain in full: 'From Middle Persian nēm \\\"half\\\" (logogram PRG from Aramaic), from Proto-Iranian *náymah, from Proto-Indo-Iranian *náymas; cognate with Avestan naēma-, Sanskrit néma-.' The four extra forms printed in the entry are all transparent Persian compounds of it, and two are inherited rather than new: نیمه nīmeh is MP nēmag with the regular loss of final -g/-ak, and نیمروز nīmrūz 'midday; the south; Sistan' is already Pahlavi nēm-rōz (MacKenzie, Nyberg); نیم‌رخ 'half-face, profile' and نیم‌شب 'midnight' are New Persian formations on the same pattern (cf. Baluchi nēmšap in Horn).\",\n          \"derivation_fa\": \"فارسی نوِ «نیم» دنبالهٔ بی‌واسطهٔ فارسی میانهٔ nēm است، با تحولِ قاعده‌مندِ «ای»ِ مجهولِ فارسی میانه به «ای»ِ معروف در فارسی نو (همان دگرگونی که šēr را شیر و tēr را تیر کرده)، چنان‌که املای «نیم» امروز در ایران nīm خوانده می‌شود و دری و سنّتِ کلاسیک nēm را نگه داشته‌اند. ویکی‌واژه زنجیره را کامل می‌آورد: «از فارسی میانهٔ nēm «نیم» (لوگوگرامِ PRG از آرامی)، از ایرانیِ آغازینِ *náymah، از هندوایرانیِ آغازینِ *náymas؛ هم‌ریشه با اوستاییِ naēma- و سنسکریتِ néma-». چهار صورتِ افزودهٔ مدخل همه ترکیب‌های روشنِ فارسیِ همین واژه‌اند و دو تای آن‌ها میراثی‌اند نه نوساخته: «نیمه» همان nēmagِ فارسی میانه است با افتادنِ قاعده‌مندِ -g/-ak پایانی، و «نیمروز» «نیم‌روز؛ جنوب؛ سیستان» در پهلوی هم nēm-rōz بوده است (مکنزی، نیبرگ)؛ «نیم‌رخ» و «نیم‌شب» ساخته‌های فارسی نو بر همان الگواند (قس بلوچیِ nēmšap در هرن). ادعای نورایی در این بند درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2233\", \"status\": \"supports\", \"note\": \"Mo'in's footnote to نیم (BQT vol. 4 p. 2233) gives the whole chain 'اوستا naēma- … سانسکریت nēma- … پهلوی nēm، nēmak' for the Persian headword and adds 'هوبشمان (۱۰۹۹) گوید: در تلفظ nīm، قس پازند nīm، افغانی nīma' — i.e. the NP reading nīm beside Pazand nīm.\"},\n            {\"ref\": \"BRT:1036\", \"status\": \"supports\", \"note\": \"Bartholomae, AiW col. 1036 s.v. naema-, closing comparison: 'np. nīm \\\"halb; Hälfte\\\"' — the New Persian word is named in the Avestan entry itself.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2233, Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"As quoted, with the Kurdish, Afghan, Baluchi and Sarikoli cognates and the reference 'اشتقاق ۱۰۶۹' = Horn no. 1069.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1069, p. 239\", \"stance\": \"supports\", \"note\": \"'nēm \\\"Hälfte, halb\\\" … phlv. nēm, nēmak' with 'bal. nēmšap, n. nēmšaf \\\"Mitternacht\\\"' — the ancestor of نیم‌شب in a sister language.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 58 s.v. nēm\", \"stance\": \"supports\", \"note\": \"'= M, N ~' marks the New Persian form as identical, and nēm-rōz is glossed '[M -rwc, N ~] midday, south' — the Pahlavi ancestor of نیمروز.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §13.24, p. 936\", \"stance\": \"supports\", \"note\": \"'Av. naéma- (NPers. ném)' — Buck cites the New Persian reflex directly under the Avestan word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T17:53:18.490Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-347.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T17:53:24.468Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-347.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 347"
}
```


### [2026-09-07T17:53:26.007Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 7, 'plausible': 4, 'disputed': 4}
root verdicts: {'plausible': 3}
ref checks: {'supports': 9, 'contradicts': 2, 'partial': 8, 'not_checked': 2, 'not_found': 1}
books consulted: {'supports': 25, 'partial': 10, 'silent': 8, 'contradicts': 10} | by book: {'KLN': 9, 'LKT': 4, 'PLA': 3, 'HRN': 3, 'BQT': 3, 'SKT': 3, 'FSD': 3, 'MON': 3, 'AKD': 2, 'HUB': 2, 'ARY': 2, 'ISS_alt_DKS': 2, 'SOD': 2, 'PHD': 2, 'AFA': 1, 'AFM': 1, 'POK': 1, 'WLD': 1, 'PHN': 1, 'CHEUNG': 1, 'AHD': 1, 'WEB': 1, 'NYB': 1, 'SYN': 1}
```


## [2026-09-07T17:53:32.502Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i '347' | head -20; echo \"exit=$?\""
}
```


### [2026-09-07T17:53:35.619Z] TOOL RESULT

```
exit=0
```


## [2026-09-07T17:53:37.428Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20"
}
```


### [2026-09-07T17:53:39.741Z] TOOL RESULT

```
3158 cited URLs, 8 not yet archived
archived 8, failed 0
```


## [2026-09-07T17:54:02.963Z] AGENT

Done. `verify_check.py 347` reports 0 PROBLEM lines.

**Page 347 (book p. 317) — 3 entries (1 redirect skipped), 15 nodes**

- Node verdicts: 7 confirmed, 4 plausible, 4 disputed, 0 unverified, 0 transcription_suspect
- Root verdicts: 3 plausible
- Ref checks: 9 supports, 8 partial, 2 contradicts, 1 not_found, 2 not_checked; 24 books consulted at node level

Disputed items:
- **Nabatu #4 — Persian naft «نفط، نفت»**: the arrow Arabic → Persian is rejected by every side. Klein (Nourai's own ref, p. 1027) and Zimmern p. 60 make Arabic naft and Persian neft *sibling* offspring of Aramaic; Horn 1035/p. 232, Hübschmann 1035, Pokorny 316, Walde-Pokorny II 693, Asbaghi and Aryanpur derive NP naft from Av. napta- 'moist' (*nebh-); Manichaean Pahlavi nbt shows the word in Persian before Arabic contact.
- **Nabja #1 — Persian nok/nūk, nūl**: words real, parent wrong. Bailey (DKS s.v. nūha- < *nauxa-) groups NP nauk, nol with Khotanese naukya, Wakhi nüčk, Yidgha nzeyo — an Iranian *nau-ka- 'point/tip' family. Old Iranian *nabya- could not give nōk.
- **Nabja #2 — Sogdian nwk**: word confirmed by Gharib no. 6133 ('tip, point, beak', cf. Khwar. nwk), but it is the East Iranian cognate of NP nōk, not a descendant of Germanic *nabją.
- **Nabja #4 — English neb, nib, nipple, nibble**: three correct, but *nibble* is a Low German loan (nibbeln, c. 1500) — Watkins himself files NIBBLE under **ken-²** [Pok. 559], and his [nabja-] entry lists only NEB, (NIB), (NIPPLE).

Reference problems the owner may want flagged (not extraction errors):
- Root of entry 1 is labelled **[Indo-European] Nabja**, but AHD/Watkins prints "[nabja-. Bird's beak. **Germanic root**.]" — the square brackets in Watkins mean explicitly *not* a PIE root.
- Root of entry 3 is labelled **[Avestan / Old Persian] Naěma**: Avestan naēma- is right (Bartholomae col. 1036, confirmed independently by Buck p. 936 citing the same column), but there is no Old Persian naēma- 'half' — Kent's only naimā is negative naiy + enclitic -mā.
- Node #5's NOTE says "SKT:344 derives the Greek word from Persian naft"; Skeat actually marks naphtha "(L. — Gk. — **Arab.**) … Arab. naft, nift", which is chronologically impossible for a Hellenistic Greek word.
- Node #6's PHN:283 is the right page (Pihan s.v. NAPHTE) but Pihan derives French naphte straight from Arabic نفط, not from Greek as drawn.

No extraction errors found: the JSON matches the chart throughout (no node was flagged transcription_suspect, so no page image was needed).
