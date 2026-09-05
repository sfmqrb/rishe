# Verification process log — verify-page-67


## [2026-09-05T05:22:40.017Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 67 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-67.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-67.json. Write /home/sfmqrb/git/rishe/data/verification/page-67.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 67` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:22:42.022Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:22:42.772Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:22:42.791Z] TOOL RESULT

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


## [2026-09-05T05:22:42.872Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-67.txt"
}
```


### [2026-09-05T05:22:42.887Z] TOOL RESULT

```
1	=== PDF page 67 (book page 37) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ater, Atr : fire  (refs POK:69)
4	#1 (parent #0) [Avestan] refs=POK:69; KLN:123 | âtarš, âthra : fire
5	  #2 (parent #1) [Pahlavi] refs=BQT:13 | âtur : fire ; âtur-pât : fire guard, a hero after whom a province of Iran (Azerbaijan) was named ☞Pa
6	    #3 (parent #2) [Persian] refs=MON; FNI:12; ETM:59 | âtaš «آتش» : fire ; âzar «آذر» : fire, a name ; Âzarbâyejân «آذربایجان» : Azerbaijan | extra: آدر ، آدیش
7	#4 (parent #0) [Sogdian] refs=SOD:11 | âš`kw : ash ; ât`rh : fire
8	#5 (parent #0) [Latin] refs=AHD; KLN:27 | âter, âtrôx : black, darkened with fire, also cruelty ; âtrium : forecourt where fire smoke escapes through the roof ; Adriâticus, Hadriâticus : name of a town (now Atri) in Italy built on black soil
9	  #6 (parent #5) [English] refs=KLN:27, 123 | atrocity ; atrium ; Adrian : a name (from Atri) ; Adriatic
10	  #7 (parent #5) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=FNI:12; MON5:12 | Âdrîan «آدرین» : a Roman Emperor ; Âdrîâtîk «آدریاتیک» : a sea off the Mediterranean sea | extra: آدریان
12	--- entry 1 ---
13	ROOT Athal -> redirect to Âtos
14	--- entry 2 ---
15	ROOT Ato -> redirect to Âtos
16	
```


## [2026-09-05T05:22:46.028Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-67.json",
 "description": "Read source JSON for page 67"
}
```


### [2026-09-05T05:22:46.066Z] TOOL RESULT

```
{
  "pdf_page": 67,
  "book_page": 37,
  "entries": [
    {
      "root": {
        "name": "Ater, Atr",
        "lang": "Indo-European",
        "refs": "POK:69",
        "gloss": "fire"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:69; KLN:123",
          "words": [
            {"translit": "âtarš, âthra", "gloss": "fire", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:13",
          "words": [
            {"translit": "âtur", "gloss": "fire", "script": null},
            {"translit": "âtur-pât", "gloss": "fire guard, a hero after whom a province of Iran (Azerbaijan) was named", "script": null, "see": ["Pa"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON; FNI:12; ETM:59",
          "words": [
            {"translit": "âtaš", "gloss": "fire", "script": "آتش"},
            {"translit": "âzar", "gloss": "fire, a name", "script": "آذر"},
            {"translit": "Âzarbâyejân", "gloss": "Azerbaijan", "script": "آذربایجان"}
          ],
          "script_extra": "آدر ، آدیش",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:11",
          "words": [
            {"translit": "âš`kw", "gloss": "ash", "script": null},
            {"translit": "ât`rh", "gloss": "fire", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:27",
          "words": [
            {"translit": "âter, âtrôx", "gloss": "black, darkened with fire, also cruelty", "script": null},
            {"translit": "âtrium", "gloss": "forecourt where fire smoke escapes through the roof", "script": null},
            {"translit": "Adriâticus, Hadriâticus", "gloss": "name of a town (now Atri) in Italy built on black soil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:27, 123",
          "words": [
            {"translit": "atrocity", "gloss": null, "script": null},
            {"translit": "atrium", "gloss": null, "script": null},
            {"translit": "Adrian", "gloss": "a name (from Atri)", "script": null},
            {"translit": "Adriatic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "FNI:12; MON5:12",
          "words": [
            {"translit": "Âdrîan", "gloss": "a Roman Emperor", "script": "آدرین"},
            {"translit": "Âdrîâtîk", "gloss": "a sea off the Mediterranean sea", "script": "آدریاتیک"}
          ],
          "script_extra": "آدریان",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Athal",
        "redirect": "Âtos"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ato",
        "redirect": "Âtos"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:22:48.485Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','FNI','ETM','SOD','AHD','WLD','BRT','PHD','NYB','HRN','HUB','ARY','SKT','WEB','IEC','SYN','KNT','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online.json entries"
}
```


### [2026-09-05T05:22:50.886Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FNI {"title": "F. Danayi, Farhang-e Namha-ye Irani, Negah 1370/1991", "kind": "purchase", "url": "in print (Negah)", "lookup_hint": "Not found (archive has an unrelated 'کامل ترین فرهنگ نام های ایرانی' by Flora Jahandar).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; free PDFs with the same generic title online are unrelated name list
ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_ety
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
CHEUNG null
```


## [2026-09-05T05:22:54.156Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local reference files and read matrix"
}
```


### [2026-09-05T05:22:54.234Z] TOOL RESULT

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
```


## [2026-09-05T05:22:55.107Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-66.json && echo && echo ==== && sed -n 1,60p tools/verify_check.py",
 "description": "Look at prior page output and checker"
}
```


### [2026-09-05T05:22:55.168Z] TOOL RESULT

```
Exit code 1
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
  
(eval):1: === not found
```


## [2026-09-05T05:22:57.274Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T05:22:57.560Z] TOOL RESULT

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


## [2026-09-05T05:23:09.616Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full grep āter ===\"; grep -n -i -E \"^\\s*ā?ter-|āter|a-ter-|ā̆ter\" POK_full.txt | head -40\necho \"=== POK pages around 69 ===\"; grep -n \"69\" POK_full.txt | head -5",
 "description": "Grep Pokorny for ater"
}
```


### [2026-09-05T05:23:09.699Z] TOOL RESULT

```
=== POK_full grep āter ===
15102:Root / lemma: b^ra-ter-{*sue-lou6'^a-ter- ' member of clan, brother ') 
15106:Root/ lemma: b^ra-ter-{*sue-/ou6'"a-ter- ' member of clan, brother '): brother, derived 
15108:from Root / lemma: b^ra-ter- ( *sue-lotA^a-ter- " member of clan, brother '): brother [Root / 
35164:gena-ter-\r\ Old Indie ya/?//^/'- 'progenitor, father' , janitrf begetter, mother', gr. yEverrip, - 
=== POK pages around 69 ===
1684:Material: Phrygian a5-5aK£T " he does '; maked. a5-5ai pupoi (Schwyzer Gr. Gr. I 69); Latin 
2035:from an 7ending root form; cf Schwyzer Gr. Gr. I 694, 696). about nyspcbv see Schwyzer 
2598:KaK-ien(; Hes. 'ravenously' (W. Schuize KZ. 29, 269 = Kl. Schr. 329). common gr.- lllyrian 
3075:References: WP. I 2, Hirt Indo Germanic Gr. II, 82 f. Schwyzer Gr. Gr. 1 4213, 6969, 7957. 
3094:References: WP. I 3, Berneker 269.
```


## [2026-09-05T05:23:11.010Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD Watkins ater ===\"; grep -n -i -B3 -A12 \"^āter\" AHD_watkins1985.txt | head -60\necho \"=== AHD ater alt ===\"; grep -n -i \"ater-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for ater"
}
```


### [2026-09-05T05:23:11.094Z] TOOL RESULT

```
<persisted-output>
Output too large (31KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/buu2vha0a.txt

Preview (first 2KB):
=== AHD Watkins ater ===
=== AHD ater alt ===
112:The second element of the name of the chief god, *dyeu-pater-, is the general Indo- European word for FATHER, used not in the sense of father as parent, but with the mean- ing of the adult male who is head of the household, the sense of Latin pater familias. For the Indo-Europeans, the society of the gods was conceived in the image of their own society as patriarchal. The reconstructed words *deiw-os and *dyeu-pater- alone tell us more about the conceptual world of the Indo- Europeans than a roomful of graven images.
154:A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
155:Male blood relations were designated as bhrater- (BROTHER), which doubtless ex- tended beyond those with a common father or mother; the Greek cognate means “fellow member of a clan-like group.” The female counterpart was swesor- (SISTER), probably literally “the female member of the kin group,” with a feminine suffix *-sor- and the root s(w)e-, designating the self, one’s own group.
...
</persisted-output>
```


## [2026-09-05T05:23:17.243Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i -E \"Root ?/ ?lemma: *[āaA][ -]?te?r\" POK_full.txt | head -20\necho \"---- search atarS / athr ----\"\ngrep -n -i -E \"atar[sš]|āthr|ā\\^tar|Atar\" POK_full.txt | head -30",
 "description": "Find Pokorny ater root"
}
```


### [2026-09-05T05:23:17.316Z] TOOL RESULT

```
---- search atarS / athr ----
3934:S. 16 ff. from turko-tatar. etc a/t'a 'barley'. 
6093:Old Indie apataram Mn . " farther away ', ap. apataram Mn . ' apart, somewhere else 
8132:name Vattern; Old High German wazzar. Old Saxon watar. Old English waeter {* uodor) 
8162:Hittite wa-a-tar {* watar) "water'. Gen. ue-te-na-as {e-grade as Phrygian p£5u, a of Nom. 
8175:na-a^ which became the zero grade wa-a-tar {* hwatar) 'water'. 
8184:Truncated Tocharian (^hwatar) A war, B M/a/'"water'; 
10142:pos^ catarrh, waterfall ', engl. pose^ a cold in the head, catarrh ', mndd. pusten^pant, 
12379:Hittite: parku- ' high ', parganu- (I) 'make high', pargatarr\. (r/n) 'height ', parkija-, park- (I) 
12679:uncertain suppositions about the origin of cymr. breuddwyd' dream', Middle Irish bruatar 
12870:"priestess' : Avestan fra-bsratar-' earner of things, secondary priest' (compare Latin fertor- 
15112:Material: Old Indie bhratar-, Avestan Old pers. bratar-^broiber'; osset. a/'i/ao'" brother, 
15337:bebarnatarZ PI. preterit, with to-ess-: do-n-eprinn^ gushes forth ', Middle Irish to-oss-: 
16533:portion', datar-m. (= Sairpoc;) 'reaper, mower', datram^ allotted share ', datramu. 'sickle', 
16548:(as "serving the meal'), 5aiTp6(; " colter, plough coulter, pre-pruner. ' (: Old Indie datar-), 
18954:Old Indie dara-, darr\\o\e in the earth'); causative is trod to ga-taurnan (\terat\ye) gatarnjan 
19341:darkness ', Avestan daosatara-, daosastara-^ situated towards evening, to the west ', 
19663:participle dita- " bound ' (= gr. 5£t6(;), daman-u. "band, strap' (= gr. -5r|MC(), ni-datar- 
22420:Old Indie dhatar-xw. " instigator, founder', dhafar-^ creator, god' (compare also Old 
23009:Maybe Luvian tuwatar-: Lycian cbatru, kbatra: Tocharian A ckacar, B //race/' "daughter'. 
23481:nominal formation: Old Indie datar-, datar- "giver', gr. Swrcop, Swrrip ds., zero grade 
24870:hardly accessible ', pratar-ftvan-^ fruh ausgehend oderauskommend ', itvara- "going', vTta- 
25829:comparative Old Indie yatara-, Avestan yatara-, gr. (Cretan gort.) oTspoc; ' one or the 
25867:To e-also the comparative formation Avestan atara-^ this, the one from the two, the 
29547:Material: Old High German atar{*etr6-) "keen-scented; acute, sharp, perceptive, swift, 
29557:vocalism of Tocharian A atar, B etar'hero', whether correct, is unclear; compare Van 
32453:High German vergattern ds.\ in addition presumably also Old High German gataro. Modern 
35032:Material: Old Indie yaAa-/?' suitor, lover' {*gm-r6-s?)\ Old \r\(X\c jamatar-, Avestan zamatar- 
35036:second syllable after matar-; the basic root has been abbreviated *Jama-, compare 
35339:gno-ter- in Old \r\(ii\c jnatar-, Avestan znatar-^ connoisseur, expert ', compare gr. 
36037:prayer', hava-vn. n., havas-, havana-n. 6s., homann. " caller of the price ', hvatar-^ caller
```


## [2026-09-05T05:23:18.220Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls POK_0*.txt; for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f ==\"; grep -n -i -E \"ater-|atarš|Feuer\" $f | head -20; done",
 "description": "Grep POK parts"
}
```


### [2026-09-05T05:23:20.716Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
== POK_01.txt ==
82:ai.  in  ghase-ajra-  .zum  Verzehren  antreibend.  Eßlust  erregend',  av. (yehr-kam)  azrö-daiölm  .die  Jagd  machende,  auf  Beute  ausgehende  (Wölfin)': gr.  äyga,  ion.  Hygr]  .Jagd.  Fang',  nävayqoo,  .alles  fangend,  fassend',  x^sa/^a .Fleischzange'.  rcvQdyoa  .Feuerzange'.  TtoSdyga  .Fußfalle'.  MeXiocygog  ur- sprüngl.  Bezeichnung  eines  .Dämons,  der  als  hitziges  Fieber  die  Glieder ergreift' ('?).  äygsvg  .Jäger',  dygsvu)  .erjage,  fange';  aber  dygew  .nehme' nach  Schwyzer  Gr.  Gr.  I  727^  aus  "^ä-ygo-]  ir.  är  n.  .Niederlage'  {*agron), cjmr.  aer  .Schlacht.  Kampf  {*agra),  eigentlich  .Hetze',  acorn.  hair  .clades'. abret.  airou  Fl.  .strages'.  gall.  VN  Veragri  .die  ge wältigen  Kämpfer'.
169:o-St.:  gr.  ald-og  m.  , Brand'  (ald-ög  ,verbrannt')  =  ai.  idha-h  m.  , Brenn- holz' =  ags.  ädj  ahd.  mhd.  elt  m.  ,Glut,  Scheiterhaufen':  schwundstufig wohl  norw.  schwed.  id.  .leuciscus  idus'  (eine  helle  Karpfenart),  vgl.  nhd. dial.  aitel  , leuciscus  cephalus'  als  ,der  Glänzende';  daneben  w-St.  *aidhu- im  gall.  VN  Aedui^  air.  ded  , Feuer',  auch  als  MN;  lat.  aedes  , Tempel',  ur- sprüngl.  ,der  häusliche  Herd',  auch  aedis  =  maked.  äöig'  soxccoa  Hes. Vom  Verbaladjektiv  auf  -to-  stammt  wohl  lat.  aestäs,  -ätü  , warme Jahreszeit,  Sommer'  (aus  *aisto-tät-,  idg.  *aidh-to-)]  aestiis,  -üs  (aus  *aidh- tu-)   , Hitze,   Glut,   Brandung',   aestuare    , kochen,   wallen,   brausen';   agerm.
174:Auf  idg.  *aidh-lo-  beruht  germ.  ail-  in  ags.  '^lan  , brennen'  zu  al  n. , Flamme',  und  in  ags.  celed  m.,  aisl.  eldr  (Gen.  elds)  , Feuer,  Brand'.  Aus verschiedenen  Entwicklungsstufen  des  ags.  celed  sind  cymr.  aelwyd^  bret. oaled  , Feuer,  Herd'  entlehnt  (M.Förster  Themse  487 2).  Mir.  äel  ,Kalk' könnte  aus  *aidh-lo-  entstanden  sein.  Doch  könnten  die  germ.  und  kelt. Worte  auch  direkt  von  der  Wurzel  4.  äi-  mit  -Zo-Suffix  gebildet  sein.
176:Weiterbildungen:  aisl.  eisa  f.  [* aidh-s-ön-)  , Feuer',  norw.  , Feuerstätte', mnd.  ese  f.  ,Esse,  Feuerherd^  (aber  ahd.  essa  ,Esse'  s.  unter  äs-  , brennen'); av.  aesma-  m.  , Brennholz'  (*aidh-s-mo-,  vgl.  ohne  s  ai.  idhmd-li  m.  ds.); dazu  halt.  *ais7niä  in  lit.  iesme  , Brennholz';  lit.  aisträ  f.  , Leidenschaft'; acech.  niesteje  (fem.  PL)  ,Ofen',  später  nistej  (mit  7i-Vorsclilag  durch  falsche Zerlegung  der  Verbindungen  *v^n-esteje,  v^n'estejach^^  Berneker  275)  aus *aidh-s-to-]  dazu  schwundstufiges  *idh-s-to-  in  slov.  isteje,  steje  PL  ,Ofea- loch';  nach  Johansson  IF.  19,  J36  auch  ai.  isiakä  .gebrannter  Ziegel',  av. istya-  n.  , Ziegel,  Backstein'.
365:Ai.    an-ala-    ,Feuer^    (,das   Unersättliche^,  W.    Schulze   KZ.   45,  306   =   | Kl.  Sehr.  216);
392:Ai.  alätam  n.  , Feuerbrand,  Kohle^  (auch  lUmuJcam  ,Brand'^) ;  lat.  adoleö ,verbrenne  (bes.  Opfer)',  adolescö,  -ere  ,auflodern  (von  Altären)^  (0  aus a,  wie  im  etymologisch  verschiedenen  adolescere  ,heranwachsen^  zu  alö, s.  unter  2.  *al-  , wachsen*^),  altäre  ,Brandaltar^  (mit  schwierigem  o-Ablaut umbr.  uretii  ,ad  adolendum^) ;  nschwed.  ala  ,lodern,  flammen^  (Johannsson ZfdtPh.  31,  285  ff.  m.  Lit.);  aber  zweifelhaft  gr.  dXdßrj'  ävd-Qay.eg  Hes.; Auffassung  auch  von  lat.  alacer^  got.  aljari  n.  ,Eifer'^  usw.  als  , feurig, hitzig^  (Johansson  aaO.)  wäre  möglich;  über  ags.  xlan  ,brennen'^  s.  *aidh-.
562:Mir.  (linder,  aindir  .jung-e  Frau';  cymr.  anner  junge  Kuh*;  PI.  anneirod, neviiir-  enderic  ,vitulus%  cymr.  enderig  ,Stier;  Ochse^^  bret.  ounner  (Treg-. tinnoncir.  Yaiines  afinoer)  junge  Kuli'^;  hierzu  frz.  (T)andier  m.  ^Feuerbock, Widder'  auch  ^Mohn'  [=  junges  Mädchen'^  vgl.  ital.  madona,  fantina Mohir),  weiter  zu  bask,  andere  ,Frau',  iber.  FN  Andere,  Anderca,  MN Anderiis]  vielleicht  kelt.  Herkunft?  {^'andero-  ^blühend,  jung^?).
915:Ai.  äsa-h  , Asche,  Staub'  (über  dsita-h  , schwarz'  s.  *nsi-  ,schmutzfarben'); lat.  ära  , Altar'  (=  osk.  aasai  ,in  ära',  umbr.  are  ,arae'  usw.),  äreö,  -ere ,bin  trocken,  ausgedörrt',  äridus  ,trocken'  (davon  ardeö  , brenne',  Partiz. Pass.  assus  , trocken  gebraten'),  ärea  , freier  Platz,  Tenne  usw.'  (eigentl. , ausgebrannte,  trockene  Stelle');  ahd.  essa  f.,  nhd.  Esse  (*asiön)^  urnord. aRinaj  aisl.  arinn  ,Erhöhung,  Feuerstätte',  ahd.  erin  ,Diele,  Boden'  {*azena)] toch.  AB  as-  Präs.,  äs-  Perf.  und  Kausat.  , austrocknen',  A  äsar  ,trocken'; hett.  ha-as-si-i  (hasi)  Lok.  ,auf  dem  Herde'  (hasas).
929:ät{e)r-  ,Feuer'.
930:Av.  ätars  (Gen.  ädrö)  m.  , Feuer',  wozu  ai.  dtharvan-  ,Feuerpriester', Lw.  aus  av.  ad-aurvan-,  ad-aurun  (das  ^  aus  äd-rö)  ds.;
931:arm.  airem  ,verbrenne,  zünde  an'  (auf  Grund  von  *azV  aus  *äter)]  serb. vätra  , Feuer',  klr.  vdtra  , Feuer,  Herd',  poln.  vatra  , Strohasche'  sind  nach Jokl  WZKM.  34,  37  ff.  aus  rum.  vaträ  ,Herd'  entlehnt,  dies  wieder  aus dem  Alb.  {^Qg.  votre^  voter  mit  v-Vorschlag  vor  alb.  ot-  aus  *ä^-,  viell. iran.  Lw.).  Vielleicht  als  , verbrannt'  auch  lat.  ätey-  , schwarz,  dunkel'  == umbr.  atru,  adro  ,atra';  aber  lat.  Atella  =  osk.  Aderllßl  {^Atrolä,  z.  B.  v. Planta  I  551),  lat.  Atrius  =  osk.  Aadiriis  (v.  Planta  II  768,  Thurneysen lA.  4,  38,  Schulze  Lat.  Eig.  269,  578)  sind   etr.  Herkunft  verdächtig.
956:Ein  ähnliches  *äto-s  in  germ.  *apala,  '^öpela  scheint  auch  die  Grundlage von  ahd.  adal  , Geschlecht',  nhd.  Adelj  as.  athali,  ags.  zdelu  N.  PL  ,edle Abkunft',  aisl.  adal  , Anlage,  Geschlecht'^  Adj.  ahd.  edili,  as.  ethili,  ags. xdele  ,adelig,  edel',  dehnstufig  ahd.  nodal,  as.  öthil,  ags.  edel,  anord.  ödal , (väterliches)  Erbgut'  (vgl.  auch  ahd.  fater-uodal,  as.  fader-ödil  ,patrimo- nium');  hierher  got.  halmöpli  n.  , Erbgut',  vgl.  mit  derselben  Vokallänge ahd.  Vota  (eigentlich  , Urgroßmutter'),  afries.  edila  , Urgroßvater';  toch.  A ätäl  ,Mann';  hierher  auch  av.  ä-^icya-  ,Name  des  Vaters  QraEtaona's^  als ,von  adeliger  Abkunft'?
1119:e.  aa-et'    in   gr.  S:st(.iöv'   tö  7tvBvi.ia    Hes.,    ix£T(.ia '    cplo^    Et.  M.,   ärf-iög  ■ (kontrahiert  aus  dsT(j,ög)  , Dampf,  Dunst,  Rauch',   mit  Tief  stufe,   aber  ana- logischer Übernahme  des  d-:    dvTi.irj  ,Atem,    Luftzug    des  Blasebalgs,   des Windes,  Duft,  heißer  Anhauch  des  Feuers',  dviiiiqv  ds.
1134:Über  ai.  upa-väjayati  ,facht  das  Feuer  an'  (von  Pänini  als  Kaus.  zu vä-  gefaßt)  s.  Wackernagel  KZ.  43,  292.  ^
1217:Ai.  bahabä-karöti   vom   Knistern   des   Feuers;    gr.  ßaßaX,   TcaTcai    ,potz-
1414:Ist  germ.  *baukna-,  in  afries.  bähen  , Wahrzeichen,  Feuersignal',  as.  bökan , Zeichen,  Wahrzeichen',  ags.  beacen  , Zeichen,  Fahne',  ahd.  bouhhan  , Zei- chen' von  solchem  germ.  *bau-  nach  "^taikna-  , Zeichen'  gebildet?
1651:kelt.  helo-  ,leuchtend,  weiß^  in  cymr.  heleu  (*bheleuo-)  ,Marder^,  air. oibell  m.  ,Glut,  Hitze^  (f.  ,Funke,  glühende  Kohle^)  =  cymr.  ufel  m. ,Funke,  Feuer^  (^opi-bhelo-),  mir.  Bel-tene  ,Fest  des  1.  Mai^  (=  Leuchtfeuer), aall.  GN  {Apollo)  Belenos,  (^Minerva)  Belisama  (Superlat.),  FIN  Belenä  > frz.  Bienne,  Schweiz.  Biel]  afrz.  haille  ,Blässe^  (daraus  mbret.  baill  ds.) könnte  auf  ablaut.  gall.  *halio-  zurückgehen,  vgl.  frz.  ON  Bailleuil  < *BaUo-ialon-  gall.  heisa  ,Feld^  aus  *belisä',
1743:bhelg-:  ai.  bhdrgas-  n.  , strahlender  Glanz'  {*bhelgos)',  Bhfgavah'FL ,mythische  Priester  des  Blitzfeuers';  lett.  balgans  , weißlich';  vielleicht hierher  aksl.  blag^  ,gut',  russ.  (alt  und  mtdarl.)  bölogo  Adv.  ,gut',  eig. ,licht'  (Gegensatz  , dunkel':  ,böse');  toch.  AB  pälk-  , brennen,  leuchten, sich  erhitzen',  A  pälk,  B  pilko  ,Blick',  A  polkämts  , Gestirn'  (:  lit.  balgans), B  empalkaitte  ,nachlässig'  (Negation  -f  *palk-  _,leuchten'  neben  pälk-) ;
1860:2.  bher'  etwa  , auf  wallen',  von  quellendem  oder  siedendem  Wasser  (auch  vom Aufbrausen  beim  Gähren,  Kochen,  sowie  vom  Feuer)  »sich  heftig  be- ,     wegen';    oft  mit  in-Formans;    auch  als  schwere  Basis  bbers-  :  bhr-^ bb{e)rei-,  bb(e)rf-.    Vgl.  6.  bher-.
1861:Ai.  bhurdti  (Hhf-e-ti)  , bewegt  sich,  zuckt,  zappelt.  Intens. ^*ar-&Äwn^i  ds.; auch:  ,züngelt,  vom  Feuer';  bhuranydti  ,zuckt,  ist  unruhig;  setzt  in  heftige Bewegung,  rührt  um,  rührt  auf;  mit  m-Formans  ai.  bhramati,  bhrämyati jirrt  umher,  dreht  sich  herum',  bhramd-h  , wirbelnde  Flamme,  Strudel', bhfmi-h  ,beweglich;  Wirbelwind'  (s.  unten  aisl.  brimi  usw.);  bh'ärni-]^ ,heftig,  zornig,  wild,  eifrig',  dürfte  als  *bhfni-  ebenfalls  auf  der  schweren' Basis  beruhen;
== POK_02.txt ==
770:Dazu  mit  r-Suffix  (oder  erst  aus  *gulo-  nach  arm.  hur  , Feuer'  um,- gebildet) :
771:arm.  krak  ,Feuer,  glühende  Kohlen'  (<  "^giiro-,  *gurä-),  krak-aran  ,Herd, Feuerbecken,  Glutpfanne'.
1010:got.  gazds  m.  ,StacheF;  aisl.  gaddr  ,Stacliel_,  Spitze^,  as.  ßurgard  ^Feuer- crabel^,  ahd.  gart  m.  ^stimulus^;  dazu  mit  zä- Ableitung  ags.  gierd  f.  ,Rute^; afr.  ierde  , Gerte,  Meßrute*^,  as.  gerdia  ,Gerte,  Rute,  Stab,  StrahP,  ahd. gartia^  gertia  ,Rute,  Zepter^.
1569:Ai.  juhöti,  juhuti  , gießt  ins  Feuer,  opfert',  Passiv  hüydte^  huid-h  , ge- opfert', höman-  n.  , Opferguß,  Opfer'  (=  gr.  x^v^a),  höma-h  m.  ds.,  hötar- , Opferer,  Priester',  hötra  f.  , Opfergabe',  havis-  n.  ds.,  hdvanam  n.  ,Opfer';
2048:jji.  , Feuer',  n.  ,das  Brennen,  Lodern',  jvala-h  m.  ,Licht,  Flamme,  Fackel',
2207:Uimmel,    Feuersbrunst;    Zorn^,    gaXzdras    m.    , Lichtschein    am    Himmel'; ■tvohl  auch  apr.  gaylis  ,weiß*. WP.  I  665,  Trautmann  75.
2292:auch  Germ-  in  illyr.  PN,  wie  auch  wohl  im  ursprüngl.  nordillyr.  VK^ Germani  (Pokorny  ZceltPh.  21,  103 ff.);  alb.  tosk.  2/arr  , Feuer,  Hitze' {rr  aus  rm),  gheg.  zjarm  ( :  dsQi^ög),  ngroJi  ,wärme'  (*g^hre-  wie  in  aksl gr^ti  , wärmen',  lett.  gremens  , Sodbrennen');  alb.  gatse  , brennende  Kohle*. (*g^hortiä  ?) ;
2294:air.  fo-geir  ,erwärmt,  erhitzt'  usw.,  bret.  gred  m.  _, Wärme,  Hitze;  Mut* =  mir.  grith  , Sonne,  Hitze'  (*g}ihrtu-s),  mir.  gorim,  guirim  ,erhitze,  er- wärme, brenne',  nir.  gor  , Hitze;  Brüten;  Geschwür';  cymr.  gori  ,brüten', gor  ,Brut,  Eiter',  bret.  gor  ,{iQ\i)  ardent,  furoncle';  air.  gorn  ,Feuer* (==  lat.  fornus) ;  dagegen  ist  ir.  gorm  ,blau'  Lw.  aus  cymr.  gwrm  , dunkel- (blau)'  und  dieses  samt  abr.  uurm  in  Uurm-haelon  MN  ,aux  sourcils  bruns' aus  ags.  wurma  ,Purpurfarbe'  entlehnt  (Gwynn  Hermathena  20,  63 ff.);  air. goirt  jbitter'  (,*brennend  vom  Geschmack'),  wozu  air.  gorte  {*g^hortia) ,Hunger';
2304:ai.  ghramsd-h  m.  , Sonnenglut,  Sonnenschein,  Helle'  =  bret.  groez,  grouez (*guhrenso-)  , Sonnenhitze',  cymr.  gtvres  , Hitze'  (zum  w  s.  Pedersen  KG.  I 108,  das  e  durch  Einfluß  von  tes  ds.);  das  i  von  air.  gris  , Feuer',  grlsaid , feuert  an,  reizt  an'  wohl  aus  *ghTenso-,  trotz  Thurneysen  Gr.  130.
2674:Mit -t-Erw. :  lit.  kaistü,  kaitau,  kaisti  ,heiß  werden',  kaiträ  , Feuerglut', kaitrüs  , Hitze  gebend',  präkaitas  m.  , Schweiß',  lett.  käistu,  käitu,  käist ,heiß  werden,  brennen'  u.  dgl.,  übertragen  lett.  kaiiinät  , ärgern,  reizen' (kalte  , Schaden,  Leid,  Gebrechen,  Plage',  vgl.  Mühlenbach-Endzelin  II  135), apr.  ankaitltai  , Angefochtene' ;
3520:anord.  hrökr,  ags.  hröc,  ahd.  hruoh  , Krähe*;  ndd.  harken,  dän.  harke ,sich  räuspern*,  Schweiz,  harchlen  , röcheln*,  anord.  hark,  skark  ,Lärm*, herkir,  skerkir  , Feuer*  (,*knisternd'),  anord.  harka  ,lärmen*,  ndd.  harken , scharren,  kratzen*,  harke  , Rechen*,  nhd.  Lw.  Harke  ^  zu  ai.  kharju-  m. (unbelegt)  ,das  Jucken,  Kratzen',  khj-gala-  m.  ,Krücke'(?);
3570:got.  Jiaürin.  .Kohle',  aisl.  hyrr  m,  ,Feuer'  {*}iürja',  idg.  *Kr-io-)]
3572:lit.  kuriü,  kürii  ,heizen',  kürenti  , fortgesetzt  heizen',  kürstyti  ,schüren' lett.  kuru  (kurstu),   kurt,   frequent.   ktirstU,   kurindt  ,heizen',   aksl.    kurjq kuriti  s^  ,rauchen',    kureubje   ,Kohlenfeuer'    usw.;    halt,    kür-,    slav.  kur- müßten  hei  dieser  Deutung  Ahlautsneuhildungen   zu  *kür  aus   einer  idg.  J Red.-Stufe  o  sein;  eine  andere  Deutung  unter  {s)ker-  .schneiden';
3573:lett.  c^ri  ,Glutsteine',  ce^ras  .Inbrunst',  ceret  ,liehen,  sehnen,  hoffen*»^ russ.  ceren  , Salzpfanne  der  Salzsiedereien',  klr.  ceren  ,Boden  des  Back- 1 und  Kochofens,  Feuerherd',  poln.  trzon  ,Herd';
3574:lit.  kdrstas  ,heiß',  karstis  , Hitze',  lett.  kar^sts  ,heiß',  ka'rset  ,erhitzenV1 (*Ä;or-s-);  wozu  als  ,hitzig'  auch  lit.  kerHas  ,Zorn',  kerüs,  keringas  ,zorn- voll',  kiHti  zornig  ,werden' ;  wohl  zu  ai.  kusäku-  ,brennend ;  Feuer,  Sonne' und  kasäku-  ,Feuer,  Sonne'  (beide  mind.  aus  *kTsäku-]  vgl.  arm.  xarSem ,koche,  brenne'  aus  intensivem  *ä:Ä2's-);  vgl.  Mühlenbach-Endzelin  Lett.-D. Wb.  I  375,  II  164.
3575:Eine  verwandte  Wurzelf.  krä-s-  als  , Feuerglanz,  Glut',  woraus  teils  ,rotV teils  ,leuchtend,  hell,  schön',  in  aksl.  krasa  ,venustas,  pulchritudo',  russ. krasd  , Schönheit,  Zierde,  Schmuck',  aksl.  krashn^  ,schön,  angenehm,  weiß gekleidet',  russ.  krdsnyj  ,rot,  schön',  cech.  krdsny  , schön',  alt  auch  ,licht, glänzend'  und  ,rötlich'  (usw.);  lett.  kräsus  , schön'  ist  russ.  Lw.
4013:av.  saoSint-  , brennend',  sao^ayeiti  ,inflammat  =  incitat',  npers.  söxtan , anzünden,  verbrennen',  av.  upa-suxta-  , angezündet',  ätrd-saoka-  m.  ,Feuer- brand',  np.  sog  , Trauer,  Kummer'  (arm.  sug  , Trauer'  ist  iran.  Lw.);  av. suxra-  ,leuchtend  (vom  Feuer)',  np.  surx  ,rot';
4384:wenn  das  lett.  Wort  sein  zweites  k  durch  westidg.  Einfluß  empfangen hat,  kann  auch  folgende  slav.  Sippe  angereiht  werden:  russ.  kresü,  kresdth ^mit  dem  Feuerstahl  Feuer  schlagen',  klr.  kresdty^  kresnüty  ,Feuer  schlagen*, dial.  ,hauen,  schlagen  überhaupt',  skr.  kreserrij  kresati  , Feuer  schlagen; Steine  behauen;  Äste  abschlagen'  (usw.,  s.  Berneker  611).
4447:mit  -t-  ags.  hrldig  »schneebedeckt',  aisl.  hrodi  ,Abfair,  hrydr  ,es  bricht  ^ hervor'  (von  Dampf,  Feuer  u.  dgl.),  hrydja  ,naßkaltes  Wetter,  Regen  und  % Schnee'.  ^
4685:Aisl.  hvatr   ,schnell,    mutig,    scharf,    hvgt    f.    ,Anreizung',    hvata,    -ada     '^ ,antreiben,   beschleunigen',   ags.    hwcat  , schnell,   mutig',   as.   hwat   ds.,  ahd. [h)waz    ,scharf,    heftig',    got.    gahatjan    ,antreiben,    wetzen',    aisl.    hvetja , schärfen,  anreizen',  ags.  hwettan  ds.,  mnd.  wetten  ,wetzen*,  ahd.  (Ji)wezzeny mhd.    wetzen    ,reizen,    anfeuern,    wetzen';    <o-Partiz.    got.    hassaha    Adv.     2= ,scharf,   streng'   (Jvassei  ,Heftigkeit,   Strenge'),   aisl.    hvass  ,scharf,    rasch',    4 ags.    hwcess   ,scharf',   ahd.    {K)was^   mhd.   was{ser)   , scharf,    spitzig,   heftig,    ""'^• streng*;  ablaut.  aisl.  hväta  , durchstoßen';  aschwed.  Keta  , Löcher  bohren';    '"^' mit  einer  übertragenen  Bed.  as.  for-hwätan,  ahd.  far-hwäzan  ,verfluchen*  und got.  höta  f.  ,Drohung',  Ivötjan  , drohen',  aisl.  höt  n.  , Drohung',  höta  , drohen';      -
== POK_03.txt ==
127:Ai.  diigära-  m.  , Kohle*,  npers.  angist  ds. ;  gael.  nir.  aingeal  ,Licht,  Feuer* ;
774:peuÖTf  p^r,    Gen.  pu-n-es,  Lok.  puueni  ,Feuer',  mit   mannigfacher  Aus-  -^- gleichung  der  r-  und  i2-Formen  und  des  Vokalismus.
775:Arm.  hur  (Gen.  hroy)  ,Feuer'  (*pur-)y  hn-oc  ,Ofen'  (*pün-)]  gr.  tzvq^ nvQÖg  , Feuer',  wozu  Ttvgd  ,Feuerstätte,  Herd,  Scheiterhaufen',  TtVQSTog  m. , Fieber',  nvqaog  m.  »Brandfackel',  korinth.  IIvQfog  ,Pferdename'  (*,feuer- rot'),  TtvQQÖgy  poet.  itvqaog  ,feuerrot'  (*7ivQaJ^6g)]
776:umbr.  pir  ,Feuer'  (^pür)^  Akk.  purom-e  ,ins  Feuer'  (*pwr-),  osk.  aasai purasiai  ,in  ara  igniaria' ;
777:aisl.  fürr  m.  , Feuer'  {^pür-)  undfyrrjfyri]  ahd.  as.  airies. ßur  (*peuri)'^ ahd.  älter  fuir  (zweisilbig,  vgl.  Musp.  vugir),  ags.  fyr  (aus  dem  Lok. *puiieri) ;
778:got.  fön  jFeuer'  (*puö7i)j  Gen.  Dat.  funins,  funin  (letzterer  aus  *puneniy einer  Kreuzung  von  *puueni :  *pun-es),  aisl.  funi  m.  ,Feuer' ;  ahd.  funko, mengl.  fonke  ,Funke';  mit  Ablaut  (""puon-)  mnd.  vaw/be, Funke';
779:apr.  panno  ,Feuer',  panu-staclan  ,Feuerstrahl'  {*puon-u\  Lw.  finn. panu  , Feuer';
781:hitt.  pahhur,  pahhuwar,  Dat.  pahhu{e)ni  ,Feuer';  toch.  A  por,  B  puwaVy pivar  ds.
1032:p{h)u-k-'.  arm.  p^'uH  ,Hauch,  Wind,  Furz',  PL  , Blasebalg',  p^^äem ,hauche',  p'"Jham  ,blase  mich  auf;  npers.  pük  ,das  Blasen  (um  Feuer  an- zufachen) ,Blasebalg',  afgh.  pü,  püh  ,a  puff,  a  blast,  the  act  of  blowing';
1338:d.  ein  verwandtes  reus-  sucht  man  in: nhd.  rösten  (aach  dem  knisternden  Ton?),  ahd.  rös^  ,Röstpfanne,  Scheiter- häufen',  ahd.  rose,  mhd.  rosch,  rösch  ,knisternd,  spröde,  re^-cA',  ag-s.  ge-roscian ,beim  Feuer  trocknen'?;  dazu  wohl   lit.  rüzgiu  , brause,  schnurre,  murre*.
1539:slav.  *sulmka-  n.  in  aksl.  shmce  , Sonne'  (das  -ni-  von  *ogni  , Feuer');
1814:Gr.  df.ido(j,ai  ,sammle*,  ic^rj  f.  ,Wassereimer*  (daraus  lat.  ama  ,Feuereimer*, woraus  mhd.  ame,  ome^  nhd.  Ohm  , Flüssigkeitsmaß'),  d^iLg  f.  , Nachttopf*, ä^vLov  n.  ,Opf erschale*,  ä(.iaXXa  f.  , Garbe*  {äiuXXa),  aber  ävxXog^  -ov  , Haufen, Schiffsraum,  Kielwasser*  nach  Benveniste  ßSL.  50,  39  zu  hitt.  han-  ,giessen';
1989:dazu  germ.  *saup-  in  aisl.  sjöda  , sieden,  kochen*,  ags.  seodan  (engl,  seethe) ds.,  ahd.  siodan^  mhd.  nhd.  sieden,  aisl.  seyd  ,brausendes  Wasser*,  seydir ,Kochfeuer*;  got.  saups  , Opfertier*,  aisl.  saudr  ,Schaf,  auch  anderes  Klein- vieh*; aschwed.  saupn  ,Sprudelquelle* ;  germ.  *supa-  in  sod  n.  ,Fleisch- Suppe,  Brühe*;  •— »
2130:alb.  hale  ,Schuppe,  Gräte,  Splitter,  Bart  der  Ähren'  {*skoliä,  =  got. skalja)]  hole  ,dünn,  fein,  zart*;  f.  , Zartheit'  (*skel-)',  hei  ,Pfrieme,  Ahle', hele  ,Bratspieß,  Spieß,  Lanze'  (==  aTi&Xog) ;  vielleicht  shtel'  ,ö£fne,  mache glänzend,  scharf,  stecke  Feuer  an,  entzünde'  (lit.  skilti  ebenfalls  , Feuer  -^ anschlagen') ;
2150:lit.  skeliitj  skelti  , spalten'  (der  Akzent  nach  sküti?),  skilü,  skilti  ,sich spalten';  , Feuer  schlagen'  (Intonation  der  schweren  Basis,  wie  keines))  skalä ,Holzspan,  Lichtspan',  Iterat.  skeldeti  ,platzen,  bersten' ;  lett.  §kelt  ,spalten', Ekelet  ds.,  skele  ,abgeschnittenes  Stück',  usw.;  über  lit.  kelmas  s.  oben  S.  546;
2323:Aisl.  lireife  m.  ^Handwurzel',  hreifa  ,schwii)gen' ;  lit.  kreipiü,  kreipti , drehen,  wenden',  kraipaü,  -yti,  Iter.,  krypstil,  krypti  ,sich  drehen' ;  aksl. skrmja  jStiTQaneXia,  scurrilitas'  {^*skroipnia)]  slav.  '^kre{p)s^  {^^kroip-so-) in  aksl.  v^z-kr^sQ,  -iti  auferstehen  lassen  (von  den  Toten)^,  ksl.  kres-b  m. ,TQOTtrj,  temporum  mutatio',  serb.  krijes  ,Johannisfeuer';  ablaut.  aksl.  v%s- krhsnqti  , auferstehend
2393:ao-s.  sceorpan  , kratzen,  nagen'  (wohl  auch  ,*schneiden*;  vgl.  sceorp  , Kleid'); aisl.  sJcarpr  ,eingeschrumpft,  mager,  stark,  scharf,  ags.  scearp,  as.  skarjp ccharf;  rauh,  bitter^,  ahd.  scarf,  scaiyh,  mhd.  scharf ,  -p/,rauh,  schneidend'; ahd.  skurfen,  scurphen,  mhd.  schür{jp)fen  ,aufschneiden,  ausweiden,  (Feuer) anschlagen',  nhd.  schürfen]
2424:vermutlich  aksl.  kremy,  kremenh  , Feuerstein';  lett.  krems  ds.,  ablaut.  krams.
2572:aschwed.  sk'Ur  (aus  *sköyrr)  ,gebreclilich',  schwed.  norw.  skyr  ds. ;  got. sltaurö  , Schaufel'  (in  ivinpi-skaürö  ,Worfschaufel'),  ahd.  scora,   mhd.  schor , Schaufel,   Haue',   schorn   ,zusammenscharren,   kehren,   fortstoßen',  schüm  '  ' ,einen   Anstoß    geben,    reizen,    das    Feuer   anfachen,   schüren^ -^    aisl.   slcora »schneiden,  zählen',  ags.  scorian  ,abschlagen'  (eig.  , wegstoßen');  mit  rj^rg*    '* ahd.   shurgan,    mhd.   schürgen   , schieben,   treiben,   stoßen';   vgl.   mhd.  md.  ^-i schiuren,  schüren  , scheuern,  reinigen,  fegen' =  dän.  skure,  schwed.  skura  ds.j  \
2578:skeu-  ,werfen,  schießen,  stoßen';  intr.  ,dahinschießen';  nur  balto-slav. Lit.  sdujuj  Sduti  ,schießen  (mit  einer  Feuerwaffe »mehrfach  schießen,  herumschießen,  herumfliegen
```


## [2026-09-05T05:23:26.806Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '915,960p' POK_01.txt",
 "description": "Print Pokorny context around ater"
}
```


### [2026-09-05T05:23:26.850Z] TOOL RESULT

```
Ai.  äsa-h  , Asche,  Staub'  (über  dsita-h  , schwarz'  s.  *nsi-  ,schmutzfarben'); lat.  ära  , Altar'  (=  osk.  aasai  ,in  ära',  umbr.  are  ,arae'  usw.),  äreö,  -ere ,bin  trocken,  ausgedörrt',  äridus  ,trocken'  (davon  ardeö  , brenne',  Partiz. Pass.  assus  , trocken  gebraten'),  ärea  , freier  Platz,  Tenne  usw.'  (eigentl. , ausgebrannte,  trockene  Stelle');  ahd.  essa  f.,  nhd.  Esse  (*asiön)^  urnord. aRinaj  aisl.  arinn  ,Erhöhung,  Feuerstätte',  ahd.  erin  ,Diele,  Boden'  {*azena)] toch.  AB  as-  Präs.,  äs-  Perf.  und  Kausat.  , austrocknen',  A  äsar  ,trocken'; hett.  ha-as-si-i  (hasi)  Lok.  ,auf  dem  Herde'  (hasas).
Vielleicht  hierher  mir.  an  , feurig,  leuchtend,  edel'  (*äs-no-).  Über  gr. ÖLipdci},  TtsLvdo)  s.  Schwyzer  Gr.  Gr.  1,  724.
Da  das  r  in  hett.  a-a-ri  (äri)  ,wird  heiß'  nicht  zum  Stamm  gehört, ist  lat.  äreö  nicht  von  ära  zu  trennen.
69
Forinaiitische  Erweiterungen:
azd'  in  ^^-  ^'^^  (*az-d-iö)  ^ dorre,  trockne^,  ^'^a  f.  ,trockner  Schmutz^, A^aXioQ  dürr;  entflammend^,  äööavov  ^rjoov.  Aä-Awvag  Hes.  {-öö  aus  -zd-)] '•ecli    apoln.  ozd  ^Malzdarre^,  cech.  slov.  ozditi  ,Malz  dörrend
azo'-  arm.  ac'iun  ^Asclie^  (Meillet  Esquisse  29),  gr.  ^aßoXog  {*Uay-ßoloq) Ruß*  (  Aschen-wurf  j;  germ.  '^askö7i  in  aisl.  aska^  ags.  asce,  cESce,  ahd.  asca, 11  hd.  xl5c7ie.
az<^h-?  in  arm.  azazim  ,dörre^  (Meillet  Esquisse  33,  EM.  70),  got.  azgo Asche^  (*azgön).  Über  das  schwierige  Verhältnis  von  germ.  *askön  :  *az- ftön  s.  Feist  72  b;  wieder  anders  Specht  Dekl.  201,  219.  Auch  ist  die Beweiskraft  der  arm.  Beispiele  nicht  ganz  einwandfrei.
WH.  I  61,  65,  818,  Feist  72,  Trautmann  22,  Pedersen  Hittitisch  27,  164.
ast{by  ,Knochen^,  s.  ost{h)-.
at'  »gehen,   Jahr^
Ai.  dtati  ,geht,  wanderte  Hierzu  lat.  annus , Jahr' aus  *atnos  =  got.  Dat.  PL itpnam  ,Jahr^  Vgl.  Fick  I^  338,  W.  Meyer  KZ.  28,  164,  Froehde  BB.  16, 196  f.  (Bedeutungsentwicklung  wie  hei  germ.  '^jeram  ,Jahr^  zu  ie-  ,gehen'').
Osk.-umhr.  entspricht  akno-  ,Jahr,  Festzeit,  Opferzeit'  (mit  -tn-  zu  -kn-, Brugmann  IF.  17,  492).  Erhalten  ist  das  "Wort  in  den  Kompositis  lat. perennis  ,das  ganze  Jahr  dauernd;  beständig',  sollennis  , alljährlich  wieder- kehrend oder  gefeiert,  feierlich;  üblich'  (Nebenform  sollemnis  sicherlich analogisch  entstanden;  Thurneysen  AflL.  13,  23 ff.,  nach  omnis?)]  umbr. sev-acni-,  'per-acni-  , sollennis',  Subst.  ,hostia'.
WP.  I  42  f.,  WH.  I  öl,  847.
ät{e)r-  ,Feuer'.
Av.  ätars  (Gen.  ädrö)  m.  , Feuer',  wozu  ai.  dtharvan-  ,Feuerpriester', Lw.  aus  av.  ad-aurvan-,  ad-aurun  (das  ^  aus  äd-rö)  ds.;
arm.  airem  ,verbrenne,  zünde  an'  (auf  Grund  von  *azV  aus  *äter)]  serb. vätra  , Feuer',  klr.  vdtra  , Feuer,  Herd',  poln.  vatra  , Strohasche'  sind  nach Jokl  WZKM.  34,  37  ff.  aus  rum.  vaträ  ,Herd'  entlehnt,  dies  wieder  aus dem  Alb.  {^Qg.  votre^  voter  mit  v-Vorschlag  vor  alb.  ot-  aus  *ä^-,  viell. iran.  Lw.).  Vielleicht  als  , verbrannt'  auch  lat.  ätey-  , schwarz,  dunkel'  == umbr.  atru,  adro  ,atra';  aber  lat.  Atella  =  osk.  Aderllßl  {^Atrolä,  z.  B.  v. Planta  I  551),  lat.  Atrius  =  osk.  Aadiriis  (v.  Planta  II  768,  Thurneysen lA.  4,  38,  Schulze  Lat.  Eig.  269,  578)  sind   etr.  Herkunft  verdächtig.
Möglich  wäre  Zugehörigkeit  von  ir.  dith  (Gen.  dtho)  f.,  cymr.  odyn  f. ;Ofen',  s.  Fick  IP  9.
WP.  I  42,  WH.  I  75  f.,  849  f.
70  •
*ati-,  ateli-,  -o-  Fischname?  ^l
Gr.  heXig  ,Goldbrassen^  (kann  aus  ^dTslig  assimiliert  sein);  lat.  ai<i7|j|
,ein   störähnliclier   großer   Fisch   im    Fo^  (wohl   gall.   oder  ligur.:    Holderl
Altcelt.    Sprachsch.  s.  v.,  M.-L.  766;    anders    Hirt   IF.  37,  222);   alit.  aiis^
lit.  Ötas,  lett.  äte  ^Steinbutten
WP.  I  44  WH.  I  78.
ati,  ato-  ,über  etwas  hinaus^,  daher  bei  einer  dem  Sprecher  zugewendeteij Bewegung-  ^(über  den  Standort  des  Sprechenden)  zurück^,  endlich  ein fach  ,her^  unter  Verblassen  der  Vorstellung  eines  überrannten  Zieles oder  Ortes.  Vgl.  zur  Bedeutungsfrage  bes.  Brugmann  Grdr.  IP  2,  844 f. Die  Färbung  des  anlautenden  Vokals  steht  durchs  Lat.-Kelt.  (Griech.V als  idg.  a-  fest,  und  es  liegt  kein  triftiger  Grund  vor,  den  balt.-slav.| germ.  (und  ar.)  Formen  idg.  *o-  zuzuschreiben,  bloß  weil  dies  einen schulgerechten  Ablaut  zum  e-  von  *e^i  bildete.  Mit  eti  (s.  dort)  be^ stand  mindestens  Gleichheit  der  Bedeutung  und  Austausch  im  Ge-:- brauche.    Ist  ati  Reduktionsstufe  zu  eti?  '•
Ai.  ati  , über— hinaus  (adnominal  m.  Akk.),  überaus,  sehr^  (Adv.  und Präverb),  av.  aiti-^  apers.  atiy-  ds.  Adv.  (als  1.  Kompos. -Glied  und  Präverb (vor  i-  ,gehen^  als  ,vorübergehen,  vorüberziehen^  und  hai^-  , tragen'  als , wieder  hinüberbringen,  tragen  zu');  ar.  ati  kann  auch  idg.  *eti  mit  ver- treten.
Gr.  vermutlich  in  dc-aQ  ,aber'  (vgl.  avTäg  aus  a-öv^  äg]  Brugmann-Thumb 623,  KVG.  616;  bei  Verbindung  mit  äusg,  got.  sundrö,  bliebe  der  att.  Lenis' unerklärt).     Lat.  at  ,aber'  aus   steigernd-entgegensetzendem  , darüber  hin- aus',   welch    letztere    Bed.  in    at-avus,    at-nepos    (nicht   in   a'pprwiE  u.  dgl.,* s.  Skutsch  AflL.   12,  213).     Gall.  ate-  (aus  "^ati-)    in  Aiegnätus  (=  mbret.^ {h)aznat,    nbret.    anat  ,bekannt')    u.  dgl,    abrit.  Ate-cotti  ,die    sehr    Alten',! air.  aith-,  vortonig  ad-  , wieder,  ent-',  mcjmr.  at-,  ncymr.  ad-,  ed-  (Belege* z.  B.  bei  Fick  IP  8,  Pedersen  KG.  II  292);  hierher  als  *ate-ko-n  wohl  mir4 athach   n.   ,eine   gewisse  Zeit',    cjmr.  adeg  m.  ds.,    vgl.   gall.  ATENOVX (Bezeichnung  der  2.  Monatshälfte),  Thurneysen  ZcP.  20,  358?
Got.  ap-Pan  ,aber,  doch'  (sehr  fraglich  ist  dagegen   Herleitung  von  got.  ^ as.  ak,    ags.   ac   ,aber',    ahd.    oh   ,sondern,   aber'    aus    *ap- -{-  ke  =  gr.  ys] anders,  aber  kaum  zutreffend  Holthausen  IF.  17,  458:  =  gr.  itys,  lat.  age ,geh!  wohlan!').
Lit.  at-,  ata-,  jünger  auch  ati-,  in  Nominalkompos.  atö-  ,zurück-,  ab-, her-'  (s.  Brugmann  Grundr.  II  ^  2,  844  f.),  apr.  et-,  at-  (wohl  nur  aus  halt. at-,    Trautmann  46);
^  aksl.   ot-,    ot^  ,weg,   ab,    aus',   adnominal  m.  d.  Gen.-Abl.,   führt   Meillet Et.  155  f.  auf  gen.-ablativisches  "^atos  zurück  (ob  =  ai.  atah  ,von  da'?  eher
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
```


## [2026-09-05T05:23:29.417Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"ät{e)r-\")\nif i<0: i=t.find(\"ät(e)r-\")\nprint(\"idx\",i)\n# find form feeds count before\nprint(\"page(ff count)\", t[:i].count('\\f')+1)\n# look for nearby page-number-like markers\nprint(repr(t[max(0,i-3000):i][-1500:]))\nEOF",
 "description": "Locate Pokorny page for ater"
}
```


### [2026-09-05T05:23:31.089Z] TOOL RESULT

```
idx 192253
page(ff count) 78
's.  {-öö  aus  -zd-)] \'•ecli    apoln.  ozd  ^Malzdarre^,  cech.  slov.  ozditi  ,Malz  dörrend\nazo\'-  arm.  ac\'iun  ^Asclie^  (Meillet  Esquisse  29),  gr.  ^aßoXog  {*Uay-ßoloq) Ruß*  (  Aschen-wurf  j;  germ.  \'^askö7i  in  aisl.  aska^  ags.  asce,  cESce,  ahd.  asca, 11  hd.  xl5c7ie.\naz<^h-?  in  arm.  azazim  ,dörre^  (Meillet  Esquisse  33,  EM.  70),  got.  azgo Asche^  (*azgön).  Über  das  schwierige  Verhältnis  von  germ.  *askön  :  *az- ftön  s.  Feist  72  b;  wieder  anders  Specht  Dekl.  201,  219.  Auch  ist  die Beweiskraft  der  arm.  Beispiele  nicht  ganz  einwandfrei.\nWH.  I  61,  65,  818,  Feist  72,  Trautmann  22,  Pedersen  Hittitisch  27,  164.\nast{by  ,Knochen^,  s.  ost{h)-.\nat\'  »gehen,   Jahr^\nAi.  dtati  ,geht,  wanderte  Hierzu  lat.  annus , Jahr\' aus  *atnos  =  got.  Dat.  PL itpnam  ,Jahr^  Vgl.  Fick  I^  338,  W.  Meyer  KZ.  28,  164,  Froehde  BB.  16, 196  f.  (Bedeutungsentwicklung  wie  hei  germ.  \'^jeram  ,Jahr^  zu  ie-  ,gehen\'\').\nOsk.-umhr.  entspricht  akno-  ,Jahr,  Festzeit,  Opferzeit\'  (mit  -tn-  zu  -kn-, Brugmann  IF.  17,  492).  Erhalten  ist  das  "Wort  in  den  Kompositis  lat. perennis  ,das  ganze  Jahr  dauernd;  beständig\',  sollennis  , alljährlich  wieder- kehrend oder  gefeiert,  feierlich;  üblich\'  (Nebenform  sollemnis  sicherlich analogisch  entstanden;  Thurneysen  AflL.  13,  23 ff.,  nach  omnis?)]  umbr. sev-acni-,  \'per-acni-  , sollennis\',  Subst.  ,hostia\'.\nWP.  I  42  f.,  WH.  I  öl,  847.\n'
```


## [2026-09-05T05:23:40.436Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Watkins: atrocious/atrium ===\"; grep -n -i \"atrocious\\|atrium\\|ater\\b\\|āter\" AHD_watkins1985.txt | head -20\necho \"=== Watkins: fire root list ===\"; grep -n -i \"^at\\b\\|^āter\\|ā̆ter\" AHD_watkins1985.txt | head",
 "description": "Grep Watkins"
}
```


### [2026-09-05T05:23:40.516Z] TOOL RESULT

```
=== Watkins: atrocious/atrium ===
82:The other vowels of Indo-European were e, o, and a. These, as well as i and u, occurred both long and short. Since we can distinguish chronological layers in Proto-Indo-European, it can be said that a number of the long vowels of later Indo-European resulted from
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
102:The comparative study of Indo-European poetics has shown that such compounds were considered particularly apt for elevated, for- mal styles of discourse; they are a salient characteristic especially of Indo-European poetic language. In addition, it is amply clear that in Indo-European society the names of individual persons—at least in the priestly and ruling (or warrior) classes—were formed by such two-member compounds. Greek names like Sophocles, “famed for wisdom,” Celtic names like Vercingetorix, “warrior- king,” Slavic names like Wenceslas, “having greater gory,” Old Persian names like Xerxes, “ruling men,” Germanic names like Bertram, “bright raven,” are all compounds. The type goes as far back as Proto-Indo-Huropean, even if the individual names do not. English family names continue the same tradition with such types as Cartwright and Shake- speare, as do those of other languages, like Irish (O’)Toole, “‘people’s valor.”
112:The second element of the name of the chief god, *dyeu-pater-, is the general Indo- European word for FATHER, used not in the sense of father as parent, but with the mean- ing of the adult male who is head of the household, the sense of Latin pater familias. For the Indo-Europeans, the society of the gods was conceived in the image of their own society as patriarchal. The reconstructed words *deiw-os and *dyeu-pater- alone tell us more about the conceptual world of the Indo- Europeans than a roomful of graven images.
113:The comparative method enables us to construct a basic vocabulary for the society of speakers of Proto-Indo-European that ex- tends to virtually all aspects of their culture. This basic vocabulary is, to be sure, not uni- form in its attestation. Most Indo-European words are found only in certain of the at- tested languages, not in all, which suggests that they may well have been formed only at a period later than the oldest common Indo- European we can reconstruct. There exist certain dialectal words that are limited in the area of their extension, as in the case of such an important sociological term as the word for tribe, teuta-, which is confined to the western branches Italic, Celtic, and Ger- manic. (It is the base of German Deutsch and of DUTCH and TEUTONIC.) In cases such as
116:We may examine the contents of this Indo- European lexicon, which aside from its inher- ent interest permits us to ascertain many characteristics of Indo-European society. It is remarkable that by far the greater part of this reconstructed vocabulary is preserved in native or borrowed derivatives in Modern English.
138:On the other hand, from the absence of a general word for “sea” we may deduce that the Indo-Europeans were originally an inland people. A root mori- is attested dialectally (MERE), but it may well have referred to a lake or other smaller body of water. Trans- portation by or across water was, however, known to the Indo-Europeans, since most of the languages attest an old word for boat or ship, nau-?, probably propelled by oars or a pole (ere-', “to row”).
142:Of fruit trees in the usual sense, only the apple (abel-) and the cherry (ker-®) were known. Wine was made in the Mediterranean basin before the arrival of the Indo- Europeans, and the pear and the olive, as well as the grape, were cultivated. As immi- grants into Greece and Italy the Indo- Europeans adopted the names along with the fruits, and both were later widely diffused.
143:Indo-European had a generic term for “wild animal,” ghwer- (FERAL). The wolf was known and evidently feared; its name is subject to taboo deformation (conscious al- teration of the form of a tabooed word, as in English gol-derned, dad-burned). The vari- ant forms wlk’o-, *lupo-, and wlp- (also “fox”), are all found. The name of the bear was likewise subject to a hunter’s taboo: the animal could not be mentioned by its real name on the hunt. The southern Indo- European languages have the original form, rtko- (Latin ursus, Greek arktos), but all the northern languages have a substitute term. In Slavic the bear is the “honey-eater,” in Germanic the “brown one” (BEAR, and note also BRUIN).
154:A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
155:Male blood relations were designated as bhrater- (BROTHER), which doubtless ex- tended beyond those with a common father or mother; the Greek cognate means “fellow member of a clan-like group.” The female counterpart was swesor- (SISTER), probably literally “the female member of the kin group,” with a feminine suffix *-sor- and the root s(w)e-, designating the self, one’s own group.
157:The root deme-' denoted both the house (Latin domus) and the household as a social unit. The father of the family (Latin pater familias) was the “master of the house” (Greek despotes) or simply “he of the house” (Latin dominus). A larger unit was the vil- lage, designated by the word weik-'. The
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
194:Archaeologists have not in fact succeeded in locating the Indo-Europeans. An artifact other than a written record is silent on the language of its user, and prehistoric Eurasia offers an abundant choice of culture areas. Archaeologists are generally agreed that the so-called Kurgan peoples, named after the Russian word for their characteristic “bar- row” or “tumulus” grave structure, spoke an Indo-European language. Some time around the middle of the fifth millennium B.c., these people expanded from the steppe zone north of the Black Sea and beyond the Volga into the Balkans and adjacent areas. These Kur- gan peoples bore a new mobile and aggressive culture into Neolithic Europe, and it is not unreasonable to associate them with the coming of the Indo-Europeans. But the Kur- gan peoples’ movement into Europe took place in distinct waves from the fifth to the third millennium B.c. The earliest so far discovered might be compatible with a rea- sonable date for Proto-Indo-European, that is, a date sufficiently long ago for a single language to develop into forms as divergent as Mycenean Greek and Hittite as they are historically attested by the middle of the second millennium B.c. But the later Kurgan immigrations after 4,000 B.c. are too late to be regarded as incursions of speakers of un- differentiated Proto-Indo-European. The archaeological evidence for the later waves of Kurgan migrations points to their having had an Indo-European culture, but the lan- guages spoken by the later Kurgan peoples must have been already differentiated Indo- European dialects, some of which would doubtless evolve into some of the historical branches of the family tree. We must be content to recognize the Kurgan peoples as speakers of certain Indo-European languages and as sharing a common Indo-European cultural patrimony. The ultimate “cradle” of the Indo-Europeans may well never be known, and language remains the best and fullest evidence for prehistoric Indo- European society.
210:Much more commonly, however, intermedi- ate developments require explanation. These intermediate stages are reconstructions rep- resenting a word stem in Indo-European that is necessary to explain the lemma following it (see the section “Grammar and Syntax” in the preceding essay). The reconstructed forms are not historically attested; they are preceded by an asterisk (*) to note this fact. Sometimes earlier or later developments of the intermediate forms are given in parenthe- ses, as in the example of sta- below. In these cases the symbol < is used to mean “derived from” and the symbol > is used to mean “developed into.” The systematic presenta- tion of these reconstructed forms is a feature unique to The American Heritage Dictionary of Indo-European Roots. The following terms are used to describe typical morpho- logical processes of Indo-European:
277:akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
279:igland, iegland (land, land; see lendh-2), island: ISLAND. 2. Latin aqua, water: AQUA, AQUARELLE, AQUARIUM, AQUATIC, AQUI-, EWER, GOUACHE; SEWER!. [Pok. akva 23.
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
299:ater-. Fire. 1. Suffixed zero-grade form *dér-o- in Latin ater (feminine dtra), black (< “blackened by fire’): ATRABILIOUS. 2. Suffixed zero-grade form *dér-yo- in Latin dtrium, forecourt, hall, atrium (perhaps originally the place where the smoke from the hearth escaped through a hole in the roof): ATRIUM. 3. Compound shortened zero-grade form “atro-akv- (*ok¥-, “-looking”; see ok"-) in Latin dtréx, “black-looking,” frightful: aTRocIOUvS. [Pok. die)r- 69.]
=== Watkins: fire root list ===
298:at-. To go; with Germanic and Latin derivatives meaning a year (conceived as “the period gone through, the revolving year”). Suffixed form *at-no- in Latin annus, year: ANNALS, ANNUAL, ANNUITY; ANNIVERSARY, BIEN- NIUM, DECENNIUM, MILLENNIUM, OCTENNIAL, PEREN- NIAL, QUADRENNIUM, QUINDECENNIAL, QUINQUENNIUM, SEPTENNIAL, SEXENNIAL, SUPERANNUATED, TRIENNIUM, VICENNIAL. [Pok. at- 69.]
```


## [2026-09-05T05:23:42.398Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 ater ===\"; grep -n -i \"ät(e)r\\|äter-\\|ater-, *Feuer\\|Feuer\" incoming/WLD/WLD_Bd1_pages.txt | head -20\necho; echo \"=== WLD band3 ===\"; grep -n -i \"ater\\b\" WLD_band3.txt | head -20",
 "description": "Grep Walde-Pokorny"
}
```


### [2026-09-05T05:23:42.513Z] TOOL RESULT

```
=== WLD Bd1 ater ===
445:dem Grin, stammenden)                                  esca ..Feuerschwamm, Zunder“ (wenn nicht als
650:„Feuer“, cymr. aidd „Hitze, Eifer", bret. oaz „Eifersueht‘'                                    ;
690:olere )„Brand, Feuer“ (Johansson ZfdtPh. 31, 2S5ff.) beruht auch germ, ail-
696:und in ags. celed, aisl. eldr (g. elds), as. eld „Feuer, Brand“ [akorn. oilet,
699:Zupitza hatte (KZ. 35, 265) an. eldr, ags. celed „Feuer“ als genaue Ent-
709:bildungen:         aisl.   eisa       f.    „Feuer“, norw. „Feuerstatte“, mnd.
712:ese     f.   „Esse, Feuerherd" (aber nicht ahd. essa „Esse“ als *idh-tu, s. viel-
724:eista „Feuerfunke“, aisl. gneiste „Funke“ (wenn die Trennung gan-eista zu-
729:gehoriges, ursprgl. „Reibfeuer“. Fur Jcnaistis ist iibrigens dt. Ursprung zu
743:spater nistej „Ofen, Feuerstatte, Backofen" (mit w-Yorschlag durch falsche
2558:  Gr. e$av(o „scliopfe, entnohme“ (Simplex aco> Od. 5, 490 „(das Feuer)
2893: zweifelnd an Einflufa von Jcrems „Feuerstein’.
3446: dyga ,,Fleischzange“, sivodyga „Feuerzange“, noddy ga „Fu8falle“, Mf Xeaygog
3898:at- „Feuer“.
3899:   Av. atars m., np. adar „Feuer“, wozu trotz des auffalligen th wohl auch
3900:ai. atharvan- „Feuerpriester“, av. a&ravft, dat. a(}a u nme ds.
3903:*dter)\ mifc »-Vorschlag serb. vatra „Feuer“, klr. vatra „Feuer, Herd poln.                                              ,
5930:dyyagog „pers. Bote“, ayyagov rr vo „Signalfeuer“ (Aesch. Agam. 273).
7988:Feuer wachsen lassen“ s. Vf. LEWb. 2 12, Hartmann Glotta 6, 332.          Lidens                                   —
8062:„adoleto?“);        alatam „Feuerbrand, Kohle“ (auch uhnukam „Brand“?);

=== WLD band3 ===
833:220, neater a sit.
880:m 208". Petrucoriua 462, 512, Ferree mpic abrit. 612. rater
1571:Arid \kurze Zeit 585°, hund-(djarfr) 307. i eohwed. 430. Avid ,,Sturm §71*, Auman or hee »Holunder“ meohw. Avifa O56", lwnadr 4606. 441. Aviflin hundrod 73, 736 hylr 332. Anthea 416, Aunger 401. tyra opp schwed, GHp hrikta 416. hitnn 387. hire. dreundlich™ Arim 478. hupp norw. 373, 375, 655°. py hel (359). hring ,.schreion’ 416. hurd 42). 41s. Arias, berihren’ Se) STE Aurkl norw, dial. bog. de inn 126, Ariada, Aratl 484. Aurpa oorw. dial. 559°, id norw. zchw. 4 hringfa 414, Aurraka sschw. 362*. id, idtka i. luingr S70" Ais G61*, ifrar 127, Arip S72", (588*) Atize norw. dial, 551". idraak (100), Arie 572%. fuga Aas a78. ifnrmeanlir (100) Arista 407, 572*. hoalf 474. igea (113). Arita awchw. run. 585%. (ie wpull 116. Arjida ,ubschailen 586". a { igfa dlin. porw. G4 hrjlen, Araue 479, , $67; 515 ikorne 11. drjoate a50), hwaty 54 if (154), 1a3 Arjote 4 pansy (376, 398). ike Le. hrjitfr 481. Avasenjali 25, ill 136, 159, hrof: |S Boeishel” 447, heap S80. tare 161. hrodi , Abfall 480. hoor 621, ink schw. dial. 133 kradinn 477. Arar, Aer nechw, 520) tanre, tfre 127, fridr 353. Awarf 473. intr nisl. 3, hrof 477. hvarene GM. iss 108. Arogn 183. kecdrr 521. isfy 127. hrdl 416, heaaa schwed. dial. 474. af 200. hrisa 353. heasfe alt. din. 474. inidgjarn 225. Arostt 477. hearse GIF. fd falta 208: Art 485. heaetma achweil, dial, 474. jafn 102, Aronn 485 Amidta 614. joki 206. ArPkivra S60*. heater 613. jaleny 163, Argre 410. ewe ached. dial, d6s. jora 138. Av gaeene pl. 477. Avdim subwed. dial. 387. Jorknasteinn 83
1655:af anl®. ater 470", @agge nore, din], 474%,
1672:ake, So u 592" ake Heater. abel do0*.
2011:Ewirnen wial, 665. erinan age. O68. kite ‘nd. oon, CUNrCTis Ape. iis. bufef mbel. U7). quira, quirmd ahd. G85, kuteln mhd. S60, iapel mond. 45. cult ahd. @72, ein fries. 669, kutle mnd. 560, quiat abd. Sat ea hull abd. BGO. bafen a cis. kdize mill. 635. kuistern fries, 669, hits mui. 650, gquifhean as. 6046. kuzsildén ahd. 553, quill ahi, 660, O71, quibs ,,Bebemons” mond. quoden ahd. 500, 671 G74. | ew jem ue, Of nd. Gil. caf ops. 561, quidderen nil. O73 cocgel ope. SOS. quarer engl. 74 eyry aps. (7 cuarin ages. 671 cyrme! ages. (i) quack, quacken 458 cyepan og. (45 quackalm nll, 671 cyt age qualia all. (1M), cula aga. Go ualhit as, OD. cvlwer age, wale nlul. B91. la mbhd, 350" qual . 690, la gualater mn. “01. fam mci. 156, quiln as. G81. labe-schwete. 402". nminion ages. (4k. labhe nhd. cial. S54* and. 874, labém oli, 442* see Ehe: 710. fade, foden mh. 352%. quartar abil. Si), dén ahi. 4" quers mbhd. 747. “lien ahd. 405* HG. ldunen. bair. 430 mbhd. 44. laffa ahd. 428". qua? ahd. 605, laffated hell, 432%, en nh, God. Iaffan abd. 354". cuted age. G00. -uffea mihi, 432*, <quchben mid, O74, Laffe nhd. 432". a ee mind. 660. rob. 42)". quik, quik ahd. 669 tee SOR reer SBF, ' : wea" ° owen . 71, loka sa 436". Quecke nhd. 6g, IchAa, laocha oll. 423* an abd. G9), lohian ,,Tnoh” ahd. 718*, quellan abil. G91. lahhéa, K ' queman ahd. 675. lake oli. 331" quena abd. 851. lak mnd. 712* cocods, clwjudw aga. G60. fake mnd. 422* queran ahd. 687. lach ml, querdar ahd. 653. liche ..Kerbe“ mud. 713* eee ee ahd. 644. lallen nha. 376°. queisen ea pics 48 aba, 434". =! Tr | = cuidu ngs. 672. lam aha. 154. ewtd, cteida age. 56D lompen mhd. 407". quicken nbd. 455. der mh. 382%, (437%),
2460:mélin, mifii lit. 200". min nm: 263" sutra TO". mémuri, meinuri lett, 242%, mind, mind, mands ii, 209 Nn inti Ut, cate th 12 eae nee ati natglinu, -inti lit, 699%. mefikas lit. 207%, mig 1H ti par soil aaatadaa sae pra vrenke lit. 267%. : bt - t. 274", nireds, narsiae lit. 339%. Bt Sage mir mirkti lit, 282°, nartas lit. 334°. ts a ane ici, mira lit. 279". parva lit. 334°. nentiris, tore lik, 260%, madd Lett SAN ee see menu, minfli lit. 266°. mischiss 6 unlit. rene sigh ik ee cay Uke 286°. it rater eee alit “oad nuiarat lit, 318*. minu lit. 271*. migrié Li Sane. ociyepae r+ meéenza lett. 267". mit lett “38 “ a7 Tote, 60° merdét lett. 279°. maida lett. $40" ware Inte. ee Hk oai® eat a 240". adire. ndlre lett. 329°. , marge lett. 273%. itt ‘lott. “248°. epacrlg gpt uf lett, 280%. ats at a ess ae “His A, west Whe eaet:. wate Noth ono me ed eh mérkin, flit, 374". oy eo I 7”, naucedd, celta ‘fit. 260. mea lott, 262%. slater lit, A Ba : nie, ned lett ge yn ener, m baie 6%. adwilés lett, 314 aes oe kaa: poy as i it. 210". ne lit, 319*. mdalwtds Nig ean : u, -fi lit. (228%). siegale lit. 530. maedius mails lit, 245°. = mse Ree ties Sous: mean, midi lic, 246%, rtebiv Fi. li nyiue iit, 32% reek ga ett. B01". dnat ¥F- ii? 219°, nrkos lit, 320°. we rche lett. 261%. ‘a nekiiGta lit. 403. rndfnns, svelte leit 240°. pee per it. 219°. nikéti lit. 321°. milas tit. 237°. it. 3308, néml lett. 231°. toa lit, ad : sath . neil lett. 134, mets let. BgT®, aie he. mete iinet 9RO*). . alit. 229". re "at ey ped ee pl. lett: 251". neriti, nérti wuntertanchen™ owt ae mublcinv lett. 253". lit. 334 meta =on*. mut! lett. 253", 254°. infideln" i mégafi it, 301", ake vee lett. 201", oe wert’ 700" vat a a if meat ™ ott. BS6. ba lett. 690" mint dys lit. 246%. mouth’ ie lekt. 2o*. secsngtt 1 tie midis ae mulens lit. 248°. mesh, nedti lit. 120, miga. lott. 248", ae tg Sr it sok Ut, 322°. migla, +n guild it. 247°. m t.a7y*, wide, nidét lett. 322%. mig, A ete. Friel muni, emikti lit, 254°- mild lit. S21". lit. ‘Boge mndu, mua lett, 271". nifgubti£s leit. G0". oniduts, gneve lett, 268*, ayuaet lie, 251". batioratgadecrt Pega nao iit. oad must lit. S11*. 8 nirti Li. TOO". ped tg fry 157°), musindl lett. 310°. ‘chu, wi ft lett. S2S*. mildus tit. 289°. abate lit... 250%. mia i” 605°. ik onie mule lett. 310". niikin, niwkti Ht. 32492. wiht, mgt lit, 244°. tet hes Wael =. ee feos imiina lett. 280%, 300". imareientt Lit ee re misiaa teeta 4 on78, raed h lit. Loe niwrksas, -Gti Lit. ao", ssiot tatt. 200°. 280", sitrniu, niurndti lit. G05". ma milage mir(k ind lit. 280°. nitevit lett. 336°. mebldte "tt. nll cect Ee at nizing! lett. 321". * mila let soe. mbrealinds tit, "00". nogna Lit. (340"). miles lit (248°), mia Wit, 130 saris, sori 7 ty north lit. 3 miltinaa tit, a . B00", aoe lit, 161. ndsis lit. 318". il beg rd it (267%), gaa lit. BAT. nol(éyré Hit. a20*. | Sb pa mot role ant wep eae Ht, 329*. = lg n tt, a " viyti lit. ole. eee cee | Ft . rat wage” iw lit, 338", mit, nina Tt, oo. niku, nald lett, 129. nuoldfti lit, BO, 163.
2470:Rt * lit, 219 ana lit. 998. ; lit. 200. atastis lit. O41, pazfalu, Zinfi, lit, 679. kart lott. 576* st: Mteiltt -au 1it. O43 toskunde. lit. 554° pa » 21". pve egy eater ght whee pipas lit. LOT*. peda lett. 25°, hud Lott. O04, vatae lit, 80", pidas lit. 22%. muoivelnia lit. O43...  {pdanibat) pipets Tk. (8°). Pedinas init It. 28°. ee ae papijuet Barve lit. 74°. pidiija, ~ati lit. 23°.
2963:ay al agi BOR. = Arm 2: deus- — Bauch grnf- Arm 2. dews- T82. | anf ate: | pea. 202. raha) (aieu G14" | 106 er 278", . (achabend) U ssanpay erg Hoo. mi 180. iufreiBers 12. aad ay ao as » 251°, 47" Lae 2. See 351. L, bd L airiohier req Sranteaheeaatecies 3 78. —— anfachSumen(d) ghoilos 634. &. 106, anfechichten 2. qvei- G00. ?. 7 210, roofer rah wer 280. auarupden plens- 00", sasfaokinteaie aii a0. rtd | me a. aufschwollen 3. bu- 114°, wunechlagen oie 4. bhal- 77*, ts pel bien 6 665°. : , vip Sons f)- | wusschneiden 1. bel- 110,* ‘ sibcciaren i cn ee z, ae 52 “4 . cr, wor nes | Tmarhon md dG neu Si" thee O*. | suBer(halb) bjhje 137" ebha aufeprodeln Ed. 2108. aumeondern |. yeiq- 252 dea te | eufstaren aleh- a8, | Lave = eae ee opl, pr 122 | nnfstellen ——-at(Ajel- 843. tena) 2. tog 715, ; hi?) olka, | anfatittcon neil. 2. rem- 371". 2, sdi- 50", ie tn anfimohen Late. 12, nusstrenen 6. ater- dys*,  Bcry eae. | entealion (Sither 157, |eceeahie see ie ei ibd. | wufwithlen 3. perk’. 46%, a ocbeeieaan sone A red- 340). - bhlege- 215". 2. Feu- oe autoritativ ibaa laces Lome _ f ; ee , Ajeubrnue 1. Bra. 206, Ast wan ao. »bheb 17°. | ‘atvarboiten een. 405%, =| Bach 7 tae ‘Als al : fils an -7 ie : > austreiten L, ier) is*, | » Fe et Li aur |e ea Aufenthalifort) {me aTT. plel- on, bald mots 203°, Anfenthalt(sert) Ps hate: el : hhe “138 ree | oe anc = 215. autfahren (chou) t tere 3 746. | aneadehnen rel. 2. epett)- | <7 eh 202, pares .perq- 4 vclobie Hab), aay Gases. | Aiedubnang’-» i) 56%. ohrenudh- B57, ben regk- 367". | aumdriicken (Saft) J. seu- 7. Bae ist". ‘ Poirot t. (hete- 553. hes. 2. hhrd- 207". legend. 554". | anuadiinsten dhen- 835. | ®. rip- 370%. anigeriumt ecin 2, wer 307. | auscinander va- 212, 2. aef- TOS". a Ph ka, Fact wi- 312. Ss | 2. fa\fag- 422°, aL winierner nat steteandergei $22 | Cromnpetanatie ae sufgerieben aces, nualegen > Sheath) ptm ‘tet Magen, uftanto 2. qeei- 50%. autihren 4b. tbe ‘H46", | Ballen bine od rt aufheben ica ate ausgelassen — ghoilos G34. | hallen 1. ger- 612, aufkratzen: 3. perk*- 46", lns- 396%. reil. ap ripen I. feds T38. aosgelansen sein j an 666. | Band guhei- 670, anflesen lea. 440°. p 567 (out Reisern) mand- 234". fash | | | be Dt Tag jee Phy sik ‘oa linen hi wa a anfnohmen A | _ lek’ 782. pte sale telteion ; a mck a | “147*, | - auehili ler presser | me vent rt
3057:Grofvater ayons 30),
3063:baachen spes- — hochkommen- fensth— 935 hen saps O90", | hell ecin Meuy- 378. been 2, syeud- 554". ie jiu- B20). hemmen glen. 402 402. | heucheln — feud- 415*. 3, gel- 438, web 22%, | heulon ul- piu- 12%, om- G25" hilfreich sein 4. ay-, ayé-, mai- 222%, | Henkel keg- 382, | ai. 10. Haute panies ae pie af 42. A hin, hinan 4. an, amd, nd = H- aU. ern Z , Be~ LL = inflen- 1 | herabfallen Arews 872, | hinnuf. pad err LL = Le hern hiingen 43 a = ol emaiinemancene ec lonliheneend iat die nie es fd 189. : Puro 147 falleup 7108 hinbreiten (fluch) 2. ater. Li: pel- GB". hera 2, adi~ 450". nile i gett (abgespaltenc) (*em- | herabtraufein 2, gue G00, | Hinderu — 1. qom- viet ng, | Restate ar, | Mn a &e fraube) 1.(@)g6r~ 305%. | eee e ener ee eee, |, hineinschiipien weag. 253° Hautbentel HET 205* arb athhuro- @ hinfahren Aber Bred a. ei a 308 pl _ (von Geschimack) .'| ‘oye Reig TNB | ptm SBR | flggabe User 88, Gbh- 177. : Fea [are Pa | eae es ghovor 834. | Herr arjo 80, breit) wla- 48%:
3115:quetechen ak 492. {undectlich) mil- 00", eat) (gut) ayek- 521", treud- 755, | Reflexivypronomen s- 454°. b'iq- 451, dklga- STT j 4 . eh 465", mig- 224* Tgsiatiz) Aewdh- 147"  rieeeln meregh- meng- 268", | rege sein weg Rind qou- 606 or coon Soma Regen 2. rede S65" | (junges) « men a9%..| Le ae Rinde Bat. 180" regnerisches Wetter agAl(u a 563". Reh ork eh Shen Ba ‘ ae - 1 oto fork. : 1 ° pi ene pitt retben ps oe. L, dhon- Boz. Ranke gel. 447. 2. gou- BO. peled- 6°. rafien 2. reu- 351". ger- S99, pleu- 24", rid. 200°. 2. gher- 608. 4, ai{i)- 464", ragen lL. gel- 453; u. der- G28. acik- 466°. _/- regh> 367".  £ mer: 270". _ aeip~ 467°. Rahm reugh-mieju. | (@chuef) 2. ghréu- 648 | 1. seu- 408°, 357". L.ghrem- 655 epee 1. feg- 422°. Rand Bid 183, (aber) amd G55". lnise) #ag- O12*. leizd- 409°, | Teichen ened’ 125, Rippe(agegend) I. perk’-44" (acharfar)  bArtu- 196". 2. teg- 716. rigiki 2. prr- 28". ranzig L. dher- 854. be de 1. | ritmen =. yer- 286, (a)tég- 622%, aik- 465° 2 hg ranzig werden none Hh reichlich men(e}gh- i va : 25" peim(i} 11", | Keichtum 1 175. Fagen derbi. 08. | Reif 3. ker. 409 Rock (aus Ziogertel) bait rassel py fresh , Nears reif werden i cdnioh. Rabre aes bx Ratechlud (weber) 1. deve | _ | | ts gtr ruuben 8. uel Bo. ie 7 mea. Me | Pakconkinohen quel 399. ater GG". machen 2 495. ar Raubtier nlp 317. relnigen 1. 13*. rhaten 10. bher- 165%. Raubyogel, bidao- 135°. | Rela utr.  Lég(s)- 421° bhdg- 187°. (grofer) fino 605. | Reisen aent- 496". | Totlich g.ser- 490°. | Them: S61:; | Reisighaniol For. 462. IRS. m- 451. Bead | or- 452 is”. smeugh- 688" | reifien 8, wel. 30 Rogen raghio- 374". rauchen in- 37D. i. TRS. roh emu 179, = 84. : « PF, sire-a O15" 451. 219%. | Rohr Lolrma-s 40 smugh- 635" j.rei- B43". reth- 368%. rault sein 1. E’er{a)- 427. Pico a74*, | rot reudh- 358° Raum iro- 70. 4. aper- 668", 3. aer- 400", reyoe 356°, (an thy i. Rack machen 2. sew- 323%, Raum haben tulp- 741. | Ruderblatt ip. 428°. upe gep(, jad 346. reizen g er- oe 186. | ern l.eré- 143. rauschen =. go". | . STi. | Ribe rip- S41*. 1 *, Ralativum om 510, fickon niz- 740", areth- TO4". | religifes dhéze- 867. | Riicksicht nehmen ghow- (dompf)  mormor- reno lL. dhen- 852. 635. | a07*. | pleu- 94° rihmen 2. gar- 353. ‘hea Hee sachets tgraitoy te) 5 gage inepien (die Ne Nan) Boi Ge eeshnem Lede! 808, | Richtung’= Lorep- 908%, | Aes : tung nnhmen od. Wei- Chetan reuse. ad rechizeitiy 2ima- 290", | 28, mentor X reckon (reig-) 347* -eont- 406%. | rlitteln (sbgilt- B01", « Frys Fs /. hen L. ond - LT4. rofen ™ 1k a = i - guyAri- ' he 217. 2 gil. 672. dhew- 345 - 443, tod. 7a. i dhewes- S43. gai). 52
3168:atébnen eng-,ong- 133 i. ater. B2u*,
3174:etottern atem- §25*. Strihne 4. ater- 636", atrafen l.gar- 353. L.qg@ed- 35. rae 340", etrall 2. gireig- O40" caer 4. ater- O36" | ork- 147. a. pher- O02: | St #irenk- 650". atrauch sqhel- 590°, | steauichsae Pilanze “anh i atre ben 7 err: deja- 77d. ied fl ken 395, (heftic) 4. md- 238%. atrecken 4 rep aia". sieiohen mag- 226°. ber) 2 ol ja i = a rat ce . hiren-g- 107? malk- 207", Btreifen a 155. trolf * tok. ee. atrulfen Hgh- LD. es ara: (aber etw.) gret- 478. (achari ber et aw) ghren- | Streit tat~ 839. atrviten AP 130*. etrenen ep- 254}, 2. en Ajer- 670". ipl Ajer(e}-g- B72". api hjeredih)- 76", Strioh 4. ater. OB", Strick J. der PAB.
3480:5B. 44, Aele Iiov.u. Liew Ajal stant "Apal S444. Zeile id ¥. u. tater Rlucmor 8, 444, Zeile 3 vou, Les ahd. (A Minn 5.445, Zeile IT v. uw. ew skelbiu, i 445, Zoile 4 v. io. Hew owdl £ 445, Zeile 2 von. lies lb Aa sd sag shy pM achlieRe Klantuer ar “eilonencde . 447, Sele 2 vy. o. lee dh-barra- 447, Zeilo P ¥, o, echliete Klammer am Zeibende . 5, Setle 16 v. o. lies Adren siatt Aare - 449, Zeile 20 vy. u. lies Aaddr aitntt Aaeddr- 440, Zeile 14 -v. a. lee ml, Aerde - 453, Zeile 23 vy. u. lies afries. Aim-diga 453, Zelle [4 ¢. uo. les ald. Avalange 455, Aeila 6 vo o. offoe Kiammer vor: A, uch, ~—. » 20ile 16 vr. uw. bee Tas. apt 457, Zeile 15 7, uw. ties ai. en 457. Zelle 7 7 ¥. up lies Ammpa mig oe ae ek, lies cole, dire
3608:. 108, Zeile 19 veo. Liew "“ShaemhA atate Haile 2 vs 0. ie fi a atatt fubs "y eae. u: lies ater statt a tteckne 8.83, Zolle 13 ¥.u. schtinge Klammer
3690:mao A Hikel ‘pir, §. 5. Ye Zeile | +. o, lies ginl. bi ite) 5, 186, Zeile 3 -y. 0. lies apr. statt aj B. 185, Zeile 22 ¥, 0, lies abel. bfl-fi S. 186, Zeile Wi -v.u. lies fia atate ome S188, Zeile 17 eh tt. lies biltem statt, bates S. 187, Zolle 6 vy. o. lies ai; bhanga 8. aby, Zeile Fy, ie lies Jase wlatt bere S. 187, Zeilo 6 vi u. lies bose siett bare B. is int fulpender Artikel cinrusshieben: bhédilojs ,,linhlioh, sift Air. fai wlisblich, sia"; gr. Perec * ee Hes,, wenn. pe Haushvemetrung fir “mb(vor, w le paden: radtrn (a. hArriA-). Fick IT* 161 (mit fauttioh ebrulehnender Alternative bajd: vot. wifeis ,,2i0, angenelm'). 5. 160, Zeile 17 v. o. line: Zipoun. 8.101, Zeile 7 v, 0, adde vel. 3, 12, 8.101, Zeile 10 v. un. lies hirdots 8.104, Zeile 23 v.00. sater The statt Ponkt hinter: ion ‘oh 5.195, Helle 11 v.0. eg Stich siatt stiek* s. 1f5, #elle 13 ¥. 0. lier ,.Knowpe, be- laubter Zweig: Zeitpunkt", (H.) 5. 100, Zeile § v. 0. . Hes ,,gebrochlich'* statt »zerbrochlich*
```


## [2026-09-05T05:23:54.518Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 page tag near 3898 ===\"; awk 'NR>=3870 && NR<=3910' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"pdf page\" ; sed -n '3890,3912p' incoming/WLD/WLD_Bd1_pages.txt\necho \"=== preceding page tags ===\"; awk 'NR<3900 && /\\[pdf page/ {l=$0; n=NR} END{}' incoming/WLD/WLD_Bd1_pages.txt\ngrep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<3900' | tail -3",
 "description": "Find WLD page for at- Feuer"
}
```


### [2026-09-05T05:23:56.318Z] TOOL RESULT

```
=== WLD Bd1 page tag near 3898 ===
form sollemnis siclierlich analogiscb entstanden Thurneysen AflL. 13, 23ff.,     ;



nach omnisi) umbr. sev-acni-, per- ami- „sollennis, subst. hostia“.
  tJber andere Zusammenstellungen vgl. LEWb. 2 45 unter annus.


at- „Feuer“.
   Av. atars m., np. adar „Feuer“, wozu trotz des auffalligen th wohl auch
ai. atharvan- „Feuerpriester“, av. a&ravft, dat. a(}a u nme ds.
   arm. airem ,,verbrenne, ziinde an“ (auf Grund von *air aus *ater oder
                                                                                                                    11
*dter)\ mifc »-Vorschlag serb. vatra „Feuer“, klr. vatra „Feuer, Herd poln.                                              ,


vatra „Strohasche“.    Yielleieht als „verbrannt“ auch lat. ater „schwarz,
dunkel“ = u. atm, adro „atra“ vgl. lat. Atella — o. Aderl\a\                                    (z.       B.   v.   Planta I
551),       lat.    Atrius   =   o.   Aadiriis         (v.   Planta II 768, Thurneysen IA. IY 38)
Schulze Eigennamen 269, 578).
   Ganz fraglieb ist Zugehorigkeit von ir. aitli (gen. atho), cymr. odyn
„Ofen“ s. Fick II* 9.
   Weitere Zusammenstellungen unwahrscheinlich. Ygl. Yf. Lat. Wb. 2 67.
=== preceding page tags ===
```


## [2026-09-05T05:23:57.072Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT atar ===\"; grep -n -i \"ātar-\\|atar-\\b\\|āθr\\|a\\^thr\" BRT.txt | head -20\necho \"=== PHD adur ===\"; grep -n -i \"ādur\\|adur\\|ʾtwr\\|ādurbād\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Bartholomae and MacKenzie"
}
```


### [2026-09-05T05:23:57.260Z] TOOL RESULT

```
=== BRT atar ===
=== PHD adur ===
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:241:balādur [bPtwr | N ~] marking nut.
PHD.txt:296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
PHD.txt:578:šādurwān [P?wlw’n! | N ~] dais, platform; basin, pond, fountain.
PHD.txt:862:ashen ādurestarēn.
PHD.txt:863:ashes ādurestar. .
PHD.txt:934:basin šādurwān; v. bowl.
PHD.txt:1480:dais šādurwān.
PHD.txt:1948:fire adur, ātaxš; form of ~ āsrēkerpa; sacred ~ ádarog, Burzénmihr, Farrobág, Gušnasp, ātaxš i Wah- ram.
PHD.txt:1949:fire altar ādurgāh.
PHD.txt:2026:fountain šādurwān.
PHD.txt:2735:marking-nut balādur.
PHD.txt:3152:platform šadurwan.
PHD.txt:3176:pond šādurwān.
PHD.txt:3625:sheet čādur.
PHD.txt:4198:veil čādur, pardag.
PHD.txt:4385:Ādur
PHD.txt:4411:VIII Abin IX Adur X Day XI Wahman XII Spandarmad + Frawardīgān
PHD.txt:4568:šādurwān
PHD.txt:4590:1%čāštag čādur
```


## [2026-09-05T05:24:05.514Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ataxs ===\"; grep -n -o -i \"ātaxš[^.]\\{0,120\\}\" PHD.txt | head -10\necho \"=== PHD adurbad ===\"; grep -n -i \"ādurbād\\|adurbad\\|Ādurbādagān\\|Adurbadagan\\|bādagān\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== BRT sanity ===\"; wc -l BRT.txt; grep -c \"Feuer\" BRT.txt; grep -n -o \"ätar[^,;]\\{0,80\\}\" BRT.txt | head -20",
 "description": "More PHD and BRT checks"
}
```


### [2026-09-05T05:24:07.775Z] TOOL RESULT

```
=== PHD ataxs ===
172:ātaxš 1 ~ : the simplest kind of sacred fire
221:ātaxš Pths = Av
605:ātaxš 1~: a major sacred fire
1948:ātaxš; form of ~ āsrēkerpa; sacred ~ ádarog, Burzénmihr, Farrobág, Gušnasp, ātaxš i Wah- ram
=== PHD adurbad ===
=== BRT sanity ===
30724 BRT.txt
91
2461:ätarasca  
2873:ätar! . . uiti  vacibii  aojanö  Yt.  19. 49
3934:ätar*  m.  'Eigner
3964:ätar-
3968:ätarasca  .  .  Ytig.18.
5831:ätary  gafianqm 'vailinqm  asäum  V.  2.  39
6461:ätara    i^asura Yl  10. 116.
6602:ätari  
6860:ätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14
6863:ätars  (Stverz.)  'rahe  mazda  puira  Y.6$}mazdä  "Y.g.^it
6863:ätari  (Stverz.)  mazdä  'rahe]8.5J
6871:ätari  vSi (sd.)  mazdä  'rahyä ahi  Y.J6.3
6981:ätar^ni
7023:ätari  . .  ".  .  wenn  er  ihm  drauf Brennholz  bringt
7101:ätar-  1  312
7112:ätar- :  3/^r
7114:ätar^{m.  A)  VrA'.So
7160:ätara'Dra  Adv.  'auf  dieser
7163:ätara'^iSra-
7184:ätarä-äSra-  Adj.  'dem  Feuer  {Älar)  \  Träger  sva.  'zu  Ätar  m  Beziehung  ge
```


## [2026-09-05T05:24:07.976Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD_pages head ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | head -5\necho \"=== SOD ash/fire ===\"; grep -n -i \"'t'rh\\|ʾtʾrh\\|at'rh\\|atrh\\|'s'kw\\|ʾsʾkw\\|as.kw\" SOD.txt | head -20\necho \"=== SOD fire gloss ===\"; grep -n -i \"fire\" SOD.txt | head -20",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-05T05:24:08.148Z] TOOL RESULT

```
=== SOD_pages head ===
=== SOD ash/fire ===
9375:292  »tr  =»  't'rh 
=== SOD fire gloss ===
9364:fire 
9380:(rc)extinguish,  (fo)lay  a  fire 
9418:(o/)fire 
9423:GcOburn  with  fire 
9428:fire 
9433:fire  chariot 
9438:swallowing  fire 
9445:glowing  fire(Af  ani's  teaching) 
10734:GcOlight,  (ro)sct  in  fire 
10880:(o)fsa  ©<*frusdi  Khwar.  /rw/;  Sughn.  fireTj; 
19626:fire 
19631:fire,  conflagration 
19661:fiery,  (d?/)fire 
19668:fiery,  (c/)fire 
82887:fire-flaring 
84959:fuel,  firewood 
87994:(to)bum  with  fire    296 
89588:fire    290,  295,  297,  1825,  1826, 
89591:fire  chariot    298 
89593:fire-flaring     11042
```


## [2026-09-05T05:24:13.151Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9340,9460p' SOD.txt",
 "description": "Print Sogdian dictionary context"
}
```


### [2026-09-05T05:24:13.337Z] TOOL RESULT

```
ninth  day  of  the  month 
Hen.  JRAS  1945,  149.4;  GMS  299;  Hen. 
Oricntalia.  8,  1939,91  n  2 

287  "sync-  M  (oj±^)JJ^<(^)j**ij 
asenc   ©Shaih  Av.  hack   ©impf.  mysync 

^*sych  *ph 

(fo)pour 

GMS  600,  634;  Bailey.  Prolcxis.  417;  AVS  123 

288  »t  jiiU 
at  ©<ahat  ©3sg.  prcs.  subj.  of  ah-  ^Wt,  'sty1 
may  be 

SCE  186;  GMS  767 

289  »t*r  =>  n»rh 

290  »t*rh  (J>>>^jj)j^<>-7 
atar   (Hr,  "t'r,  Mrh)  ©ob.  -y   =^tr 

fire 

GMS  4,  943;  TSP;  SCE  78,  168;  BSTBL;  BBB; 
MSP;  STii  4.27 

291  »tp>k   B  u/ 
atpak   ©<*a-tdpaka-,  Av.  a-tapaite   =»>ntp 
heat  ? 

S  W,  IIJ  1976,  69,  Frag.  24.1;  C2  pl77.18 

292  »tr  =»  't'rh 

293  »tr  »wst-  M  (o*U  j^  h  Jz1)qjXx  jS\ 
atar  ost 

(rc)extinguish,  (fo)lay  a  fire 
Sund.  Man.  Lett.  305.23,  313 

294  »trh  **  nJrh 


"trn'y 


>v 


12 


Oijj(  'tr-'" 


'  a-" 


I  I 


ei-r"  ^J3-trJ  ' 


U^"'   L?^^. 


/ 


u^1 


295  »trn»y   M 
atarne 
(o/)fire 
S  W,  BSOAS  1981,236 

296  wtr  swyt-   B 
atar-suyd 
GcOburn  with  fire 
Bcnv.  TSP  7.138  n  p2l3 

297  Htr  swk   B 
atar-sok   -^trswcy,  }tr  swq 
fire 
TSP  9.29 

298  "tnvrtn    B  * 
atar-wartan   Ontrwrtn) 
fire  chariot 
SCE  243 

299  »tr  xwrndy(y)   M 
atar-xurande   ©Parth.  ddur  xwarendag 
swallowing  fire 

BBB  bl5,  b94 

300  »try  swc»y  8ynh   S  (^U  ^  Oiy*)oijsJ  J^ 
atarc-socc-Scn   =>6ynh 

glowing  fire(Af  ani's  teaching) 

Karab.  Insc.  17.11,  25;  Bcnv.  Notcsiii  223 

301  »ty(y)    M  j 
at   =>>rty\  't1 

and 
GMS  76 

302  »w'YS    B  Voyri^^-c^r 
awaxs   (*w>xs,  Wys) 

side,  now  ? 

BSTBL,  Dhy.  223;  Dhu.  229  n  p47.229;  TSP  3.298;
```


## [2026-09-05T05:24:22.925Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i -B6 \"^ash\\b\\|^ashes\\b\\|(o/)ash\\|ashes\" SOD.txt | head -60",
 "description": "Grep Sogdian for ash"
}
```


### [2026-09-05T05:24:23.014Z] TOOL RESULT

```
9290-
9291-277  "swr'n  =»  "s'wr 
9292-
9293-278  »S»k(w)   B  j^S^ 
9294-ase   ('s'y)   ©Av.  atrya  <*a0raka 
9295-
9296:ashes 
--
19436-
19437-1794  'swkc  =$  swkc} 
19438-
19439-1795  >sy   C  ^S^ 
19440-
19441-ase   ^"s'kCw) 
19442:ashes 
--
87345-
87346-9833,  10094,  10101 
87347-ascension    8847 
87348-ascetic    4112,8505 
87349-as  far  as    6873,  7152 
87350-ashamed    9186, 9199 
87351:ashes    278,  1795
```


## [2026-09-05T05:24:29.513Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7095,7200p' BRT.txt",
 "description": "Print Bartholomae ātar entry"
}
```


### [2026-09-05T05:24:29.567Z] TOOL RESULT

```
Komp.:  •■i-\-lmrya.,  aus  ar.  \l-ilii,{r)i„m  D";  S  ■*!?. 1.  —  Pü.:  4  bar. —  ■>  Zur  Art  der  Komp.  s. ai.  ä-,l!'jdaiäm  'bis  ?.um  zwölften'  sva.  'zwölf- fach',  RV.  IQ.  114.  6;  Wir.  Gr.«  S  '3'3  b- [Falsch  lu  all'  Franke  ZDMG.  ./.*.  485;  be- achte n%rilJi«,  das  zu  V.  S.  16  iT.  keine  andre Bcdeulunj;  hat  als  x!-;-irzay,ii\
•  j.  ä'xrüra-  m.  EN.  eines  Gläubigen: "rahe  haosravanhalte  asifOHü  "des  A.,  Nach- kommens des  //.  .  ."  Vt.7y.137".
Eig.  Bed.?    Vgl.  ai.  ah-.ha-  als  EN.  —  ')  S. dazu  SEE.  iS.  375. g.  äxiJ:  s.  x;,i-.
•  j.  äxä-''  V.,  niur  mit  ami  'i<f>opäv\ I  Praes.  30  (Iter.)  amyJxsaya-.  Inf. I  aiwyäxstriii.
j  i)  'die  Aufsicht  fuhren',  ohne  Obj,: l^sraOMvarizff  (jid.)   aiwyffxiayit  N,  77;  —
lOogle
jii  sx$ta-  —  'ätar-  1  312
Wa  na  ßama  niSanharata  hs  aiwyifxh-\  ('^«  Y.  57.  3,  6S.  9):  an  ia.   —   <)  Von  ä-ia
yata  Y.5&4-  a)  'wachen  über  -,  be-j  ("''  '^^'  nicht  immer  sicher  lu  trenn«;  vel.
■',..,•'■,,.'  ,       '  I  Yt.  /o.  s.  77f-    und    s.    Pu.    —    ')    Wo   die
hüten,     mit    Akk.:     manay^n     ahe   yaia  ,  Teilung  in  Pü.  verfehlt  ist;  s.  lu  ,1  No.  8.
haxanrim  naram  Syum  nanm   aiwyäxsa~\  .     ,  ,    __v.,    ._.,v   „  ,
,iil  Yt;.  19;'-  /™™,V  ••  y''  «''  '';,v"°r,"'m  ''''"'
sfrJus  aiwyüxsayänti  yam  haptSir'wgS  Yt
y.6o;  59,  61,  62.  '       ,  \        J"  ''/"V"'""'"  ^-Sr-  li«  •T>uf.-«%  s.  '^rai..
Vgl.  ahByäxilar:  —  Vgl.  Hl.  uijoMÄ  'ansehen'^  1  j.  älat  Vr.  lg.  1;  lies  J  /a;.     Vyl.  V.  3.  2o,
femer   lit.  akh  'Auge'  usw.    bei   Bgm.  Grdr.= ,  wo"  NA,  ü./a/ bietet     S.  ä  No.  i8.
kJn"auTh''«i-"'t^."S^'ir^s^zen';!^  •  j-.  g-  G  P-)  'ätar- :  3/^r;..,  Oir-,  ,T//-'> aiwyäxi'  nach  S  ^ö*  3  a  erklären;  das  gilt  m.  'Feuer',  I)  im  jAw.  'Feuer'  im  AIl- auch  für  aa.'yäxU<xr-,  vgl.  Bgm.  BSächsGW.  gemeinen  und  spez.  vom  Herd-  und  vom '°97-  35-  sakralen  Feuer,  oft  persönUch  gedacht  und
*  j.  äxsta-  Adj.  'gefriedet',  nur  Plur.  ntr.  götthch*'  verehrt":  °tars  narim  jaitUi 'friedliche  Zustände,  Friede':  *a>a  »ä  'Ia  vilf  . . 'iars  {ÜS.)^  nanm  nsit  jainH  astö buyqpi  *yaia  iiä  .  .  "so  mögen  friedliche  vidsiuS  dim  i/andayeiti  ..  'tars  handazaili Zustande  uns  (beiden)  werden,  dass  .  ." '*asia  ultan?mca  V.  5.  9;  —  infrr/S  y,'> Yt.16.3;  —  *°/a')  is)mn3  datihave  am?m  '.parsJars  .  .  '"kro  vääm  surunaoili  FrW. ,.  tanuye  Yt.l6.19.  l'o.4i;  — yahmat . .  nalmanqm  vätö  '"^rö
KompE.  —  Et.?  Vgl.  äxSiay—  ')  So  J  lo,  ba0mm{%^)  vTbaraitl ahmät'..hazam-ayna Ei;  na.  mit  Fi  "//.  paiH-jasaiti  ätar^{m.  A)  VrA'.So;  Vyt 5i;
•  j.  äxätay-  f.  i)  'Fnede.  Friedensver-  —  »/«/-/(Gen.?)  ^«ö/of«  N./o^;  —  ya^a trag':  vaiiut  ahmi  nmäne  Uis  anäxsnm  Y.  -.fars  kulkim  agstn?m  aiJnJhrmiaiti  hrwa- fjo.y,  —  tarn  'tdis  a».7xsm's7a  mi^ra  yäü  (sd.)  daiaiii  Y.7J.8;  —  *:bripi>'Wö xsayehe  daüyunam  Yt.  70.29;  —  sraos?m  (sd.)  .  .  astt  'tari .  .  kama  bipOtwS  ahvi.- ,  .  yS  'tlsca  (AP.)  urvaiHsca  dmjo  spasx5  ^.tme  F.  25b;  —  '%re  aEsman  isaiü  (sd.) (sd.)  spJnihahe  YL  7/.  14;  —  *'ti  'P-Y. 5.2;  14.T,—  baR'an  va^aiiam  aisim- 26'\  a)  mit  hqm.vainli-  Adj.  'sieg- 1  w^«,  , .  .^^  . .  „isirlnuyat  Y.i4-i\  3;  — reicher  Fneden':  Ulm  hqm.vaintim  Yx.-j.\j,Jspaäl>yS  sastm  baraiü  Hari  .  .  yaHbyS 1,  \tn.15,  is.i'\  5.2.1;—  '/äis  Aqm.-^aem  "ham.paMti  *xsajnmca  *säirmca vaintyä  S./.2;—  auch  Flur.:  *'tibyaseai'>  ^(^^:^  ^_.;.jspanam  para.car>ntatn  UarS  zasta *kqm.vaitttibyS  Vr.7/.i6.  2)  •■XPottim- \  adioaya  (sd.)'.  .  äat  yni  sr  asm  baraiti Stimmung,  Einklang  mit  -'  (Inatr.):  Hag'M  '  aSsrntm  va  . .  ä  kl'pas^am  frinaiH  atari dalnaya  V.j.i.  [Ytj6.i9:  hes  äxlta;  {z\x  A)  .  .  imat  .ikrö  (zu  A)  Sfnvaimn s.  axita-^  i(sd.)  v^  ahmSi  aismim  baraiti  V,6"2.7  — 10;
—  Pu.:  ailih.   —  ')  Hds,  ahiili,  aber  Pu.:  /«',-'..  *       ,  ,    ,  .',         ,
mik.  —  '>  Wo  'ffm  hqoivamllmM,  in  Folge '  ^'"'"'j'  ■  ■  ^^'"••'  '^'"^  (^U  A)  S/rüUii missver^tändlicher  Auffassung  von  4' ;  s.  "      ^'   •''-'^           '-  ---.._--.
-  J)  So  K  7  a,  b.     Der   Dual    der   KA.
nicht  am  FUlz. •  j.  ä-xsnav-'>  Adj.  'bis  zum  Knie  reichend, so  gross  dass  es  bis  zum  Knie  reicht'
V. /.V,  26;  —  baivan  va^anqm ,  .  urvSsnayii  vii  voku^aonahe  vä  .  .  ' . .  nisirinuyat  V,  14. 3;  2 ;  —  ant .  .  ' sac^ra  frabaröil  xrUzdranam  assmai '>re  frabarBis  voku^aot
yöpaoiryö  barpsma /rasürmala  >ryaxäTs7a  |  '%re/rabaröis"V.  ig.  24;  Vr.  j.  14  PüZ.  (wo
(sd.)  . .  'ttBs'ca  ". ,  bis  zum  Knie  reichende '  -tanm  ä);  —  haeaipr^m  anumayanatn  .  .
(Zweige)''  Y.57.6.  '  aitaisam  pasi'am   asmanivri  (sd.)   tao>ra
Pü.^ .;,«,/  =:v,M.  -  .>  Oder  J/„%  PI4;   vgL    ,;j^,  /_  ^^^,^  ^^^.^  ^  .f.abaröit  V.  J,y.7o;
■    -X   .>  -       i  c  -^  All    .L-    I —   aetasp    t!  *'/fl;-**'    sag>ra  N.65;   -^
.  j.  aea'>  sva.  a;  1)  Praen.  mit  Akk.  hin  I  ^.^.  ^  ,.^^^  ^^^^        „isirinuy.lt  V.
zu  -  .  neben  ,.:   uv.  t?m_  spayat  ..  t'fnö  ,^_f,.^_      i  a,,hal ^r^'ara  antar,!  nahfnat a.a   vaels  am  acst^  „ca    ahum  .,  V.3. ;  ^^^     ^^'^  .,^^^  ..^^^^^  yraoirisyäH  V.  ,V. ^^S.  au.^^^l\.^Serl■;  tt;S,sS,.    -ö,"  -  ni^y^U  (sd.)  Har.' . .  Ä^a ya^H- —  mp.  vgl.  ik;    Bthi..  IF.  13.  114,  137.  -    h^  (sd.)    amy3   .  .  ya>a    .  .    P.  ;/;   — Pü.  (lu  V.  j)j):  o  . .  ,U\  sonst  weggelassen, '  raox^mm  bavähi  ya'ha  ■''hmn  (statt  Nom.)
dby  Google
313  'atar-  I  a
^yt.4;  Az.6  (wo  Uanm);  —  äat .  .  Im sä  iat-at  p3r»ne  .  .  ''hrqmta  suxrqm  (sd.) iaocintam  V.  2.8;  Vd.V;  —  asaocaniat paiti  '%räiS>  No*;  A.4.S,  V.g.$6  (wo °^rai);  —  Aaoa  'traii&yö''^  sao^ayantaäliyö Vd.p;  —  nixiata  ahinat  vazata  'tars  yS upa.suxtd  YL  to.  127;  —  hfya  .  .  '/rv//i aiti.barqn  avi  . .  nmätum  yaf  . .  na  fara.- ; iri^ytlJV.^.4i;  42f.; — yexi  nsit  mirika' (näml.  (i^ravaiti)  'trtm  atwi-valftai  (sd.)  | .  .'%re  (für  Gen.)  *raoxsnqm  paiti. dHyät  (sd,)  \ y.i0'.2i  —  avi  t/im  (n'iatL  vanqm)  aiwi.- rM/ayaü  (s±)  °^rffV.^.2; — ' '"kra  fra- vaiim^a  (sd.)  N.  65;  V.5.37;  —  von  Un- gläubigen mit  verpöntem  Material  genährt: yal  . .  dam)ayäzQ  avi  -irsm  äbarsiiti  .  . aO^m  aämitn  yS  vaoce  ^lumatka  nqma Yt  74. 5  5 ;  —  durch  Missbrauch  geschändet : yal  .  .  matdayasna  ,  .  'tnm  noiupäkfm (sd.)  /ra/atqn  .  .  '^raj  haca  . .  aismq frasaöcayähi  (sd.)  .  ,  yat  va  a?t»fn  "inm u%äarpza  (sd.)  .  .  vlca  barSil  vlca  sävaySit\ ya^a  äsiit-m  frävaySit'^ .S.T^-ty,  76,81';
—  y5  "tr^iii  uruzdipäk»tn  däitlm  gätUm avi  avaiaraiti  V.S.Sz;  83—96'*;  —  näi/ faahö  ahmst  ^ad^mm  vtr^nyäti  yaaöit Ptti:rahe  .  .  nasQm  pacät  paiti  '^re  üAfm baräiY.iO.iT; — yd  naiäum  matgü^qm ..'tr^m  ,'l../rabarinH\.y.2^.  a)neben| Wasser,  Rind,  Pflanzen,  Barssman  usw.:' para  asmgm  .  .  äpim  .  .  zqm  .  .  gqm  .  . urrarq/n  . . 'trwi  Y.ig.2;  —  iulia  "tnm , .  .  äpfm  .  .  zqm  .  .  gqm  .  ,  urvarqm  . . yaaidainni  V.ii.j;  3,  $,  9,  10,^.33,  42;
—  äat . .  ahe  nmänake  frapi'^ws  gäu/  .  . 'lars  ,  .   *vlspqm^ujyäiiii  V.J. 3;  —  "'^rS
fraiatimea  .  .  g}us  *vTmitim  N.  tf5(?);  — hat  drajo  haca  ''iirat . .  apat  . ,  baraimn /rast jiryiltV. 3.1(1;  17,  16.^,  l-J.a,;-^  aal tum  nisAioOis  apasca  .  .  yazimnö  'tarimca H.  2. 1 3 ;  —  (7/;»«  ä  va  °trpm  ä  vä  V.  7. *S;  5-37.  *.i04-io6,  Y.7.12,  2.12;  — '^/r  .  ,  aiwyö  V, /<S'.  70;  —  yoi  nmaiia hamiaräntaki  'trimca  bansmaca  tastaca haomaca  hävanaca  V.5,39;  40;-—  'trsm yaxaita  bansma  st}r>na3a  V.  12. 2 ;  J.  1 5, Vt.;2.3,  A.4.5,  Y.f?.s6.  b)  von  dem beim  Gottesdienst  (im  atas  dan  'Feuerbe- liäiter')**'  dämmenden  Feuer:  Hat  ätra- vaxsake  (sd.;  nämL  kairim  atthat)  yat '■tr>mca  aiwi.vaxsayät  ''^rasca  Hlr5  iiraxtis yaoida'^al  N.  Jj;  ffi;  —  aal  frahratarS Isd.)  yat    'Tirasca    alfqm    %raxlim  yaoz-
'atar-  I  A
3'4
[  da^at  . .  '"krasca  . .  paitHarat  N.  ■j4;  — j  iävanänS  (sd.)  dilityS  gätus  fralarqn  barts- ,  mqn  aparqm  ''i<ri)  N.79;  79 ; — '"ai^a  yff  dim *frähincin  (sd.)  *antarp  'tartmca  barsmaca \  ". .  zwischen  dem  Feuer  und  dem  B.  (an ■  der  Opferstätte)"  N.  08''\  c)  GS.  mit I  ta/nav-  m.  Flur.  'Feuergluten'  sva.  'Fieber- lanfälle':  kö pagiryS..'%rS  tafnus  därayat tanaot  haca    masyehe  V.  20.  i.  d)    Es
werden  in  der  Theologie  fünf  Arten  von Feuer  geschieden;  s.  unter  den  einzelnen Adj.:  °tr>m  b3r3zisavat3h3m..vohu.fryämm . .  urvOzist^m  (s.  A  und  2)  . .  väzist^m  (s.  A und  2)..  j/7«/i"ö/n  V. /7.11;  V.  75.40,  Yt 7J.85.  A)  als  Gottheit  (Vazata;  s.  aber Y.7.2)"':  tumas}  ti  °tars  .  ..huiiH  mazi^ta ^a;o/flNy.5.4;  V.51V.  7; — '7ire..yaltusl)mäi aiiinsanqm  spmtanqm  Y. /.  2;  —  a  html 'hnm  gärayemi  .  .  zaohraSyS  Any.  2^;  — hwqm  'tnm  akurahe  inazda  pu^rpm  asa- vamm  asahe  ratam  .  .  vtspe  "tarS  (AP.) yazamaidey.ss.T,  J'-io,  S. 2. 9,  Vyt, 26(?) ;
—  'tar/  (als  Vok.)  spitüa  ra%a?i'tara yazaia  pouruj^ar»nat?ha'^y.^.6;  — fryehe väziltake  astBil  (sd.)  ratüm  ämrvye  'trlm ahurahe  mazdä  Y.  13.2;—  "trim  vTspanqm nmänanqm  nmilnS.paitlm  Y.  77.  11;  — ttiva^ayemi  . .  tara  "'hrö  . .  mal  vispasibys 'l^nbyS  Y.7.11;  2.12,  77.11,  22.26,  Ny. 5. 6 ;  —  'tnm  väziitfm  (s.  I  d)  yazalla '' dalum.janim  sptfijayrlm  (sd.)  V.  z^.  40;
—  raziltqm  pantqm  dd^aiti  'tarsW.io.y,
—  yat  titarat  (sd.)  attrö  tnaittyus  duhjm alahe  . .  antar)  pairi.avsilim  vohula  tnanö "tarsca  ta  hc  taurvayattm  tba!sa  Yt.  13. 7 7 f.*';  —  asim  vahütim  'tnmca  Y.2.4; 7.4,  A.  4.2,  S.  7. 7,  2.7;  —  xmümaine  ahu- rahe mazdä  am»sanqm  spintaiiqm  sraosahe afyehe  °^riJ  Y.  22. 4;  —  mana/a  yastum yat  ahurahe  mazdä  'hrascd  "S.^ff;  — haurvata  anitrstätä  ,  .  gjui  tarne  gfus itrwie  ..    "'hre  Y.JO.2;    7.2,  Vr.p-S;  —
fravasayS . . yqmca  °'^ra  urvitzistahe  (s.  1  d) Hp>ntake  lyäxanahe  yqmca  sraelyeke  .  . yqmca  nairyS.sar?hahe  (sd.) . .  Yt.  7j.  8  5 ;  — °tar^  äfrJnämi  . .  tax'a  ahuräne  iifrinämi  Y. ÖÄ14;  — s.nochV.A:8o,7<V.26,Y.fo.7-io (oben  Sp.312);  —  als  besondrer  Gegner des  AiayDahäka*'':  sp?nlö  mainyus  aUym (sd)  frarf/tancayat  vohuca  manö  ahmca vahistfm  °trjmca . .  a»rS  maiiiyu^ , ,  akimca mano  alsimimca  .  .  a'sTmca  dakäk}m  Yt. 75.46;  —  dlilt  frasa  hqm.razayata  'tars..
dby  Google
3IS
atar-  I  Anhang
ataradrs
316
aat  ,  ,  /radvarai  aii7  dahäkö  , .  daernnS: .  .fra  '^wijm  paiti  a/iifia  (sd.)  nait  apaya uzmoeayäi  .  .  'i^rilibrai  asahe  gaSiianqm Yt.  ig.  48;  49f.  A  a)  airö  (näinl.  ayar?) heisst  der  9.  Monatstag:  -'^rB  akurafu mazda  pii^ra  (statt  Gen.)  S. /.g;  vgl.  2.9, J6.4,  Anhang  zu  1.  Das  Feuer  (J5?a^J  °>
wird  als  a)  der  des  oder  als  ß)  der  Sohn des  ÄkM.  {MAA.)  bezeichnet  (vgl,  zu  2 und  i);  a)  mil  zi  ahme  nmäne  ..frXm vaocata  mam  yim  ahurMii  mazdqm  ydia me  >i5il  °tars  (Nom.)  ahurahe  mazda  fry3 anhat  P.  17;  ar,  V. /Är8,  20,  32,  F.  25b;
—  -trim  ah'  m'  Y.  13.2;  —  'tr?mca  a/r nf  V.J.  15;  —  'tamiua  ah°  m°  H.  2. 13, Vyt.^;  —  '2)r^  ah'  m-  Y.7.2,  70.2,  V. 14.2,  7,  18,  26;  —  '"iraeca  ah'  m°  ¥.4.2;
—  "^rö  ah'  m-  Y.  22.4;  —  ->rasca  ah' m'  Y.  i. 4,  Vr.  IS. 3,  S.  1.  7,  F. 39'  —  ''^räca ah'  m'  Y.  5Ä4;  —  'iar^  (Vok.)  ah'  m'  ■ Y.5Ä7;  —  'iar/  (Nom.)  mazda  'rahti Y.62.7,  9,  Yt. /0.3,  19.47-49^  V.<?,8o, Ny.5.4;  s.  noch  2.  ß)  'lan  (Vok.j ahurahe  mazda  pu^ra  Y. 65. 12;  —  düyA ms  'tars  (dXsVok.)  pü>ra  ah'  m'  Y.62.4;! 2;  ��  afrinlmi  tava  °tars  puitra  ah'  m° Y.O'-J.ii  4.23,  22.26,  Ny,  j.4;  —  xsha-\ maine  tava  '"^rö  ah'  m°  pu^ra  Y.3.Z;. /.  12,    22.3,    26,  Ny.5.4-6^   S.  i.9;  — |
ah'  m'  puhrsm  (statt  Gen.)  V.5.  2,  15.  | 45;  —  'trun'a  ioa  ah'  m'  pu^inm  yazo- maide  Vr.  lO.  i ;  Yt.  I().  46,  S.  2.  7,  9S,  Y. 2.4,  12,  /Ö.4,  /7,ii',  ifj.2,  25.7',  V.fV. 14,15,75.48.  2)imYHapt.:  ö:5_)'<7  SjcjI 'Uro  vpr?iinil  paouruyS  pairTjasSmatdi mazdä  ahurä  '^wä  ~iivä  mainya  spSniitä , yi  ä  axlis  (sd.)  .  ,  "mittelst  der  Tätigkeit  j dieses  Feuers  hier  nahen  wir  uns  dir  zuerst,  I o  MAh.,  mittelst  deines  heiligsten  Geistes  I dir,  der  .  ,"__  Y.j6".i;  —  «/rf/-/ (NS.)  Ti>i: (sd.)  mazdii  ahurahya  ahi  mainyus  v!ii- ahyä  spsnisis  ahl  Y.  36. 3 ;  —  urz-iizist? (s.  I  d)  hvö  ria  . .  paili.jamya  'tan  mazdä ahurahya  (s.  I  Anhang  o)  Y.  3O.  2 ;  — hyat  i'ä  töi  namanqm  väzist^m  fs.  I  d)  'tar» mazda  ahurahya  (s.  I  Anhang  a)  Y.  3!}. 3-  3)  im  gAw.,  persönlich  und  gött- lich gedacht,  meist  als  dem  MasdähAh. angehörig  —  '^wa-  'tuus'  —  bezeichnet (vgl.  Anhang  zu  I ) :  him  nä  mazda  mavaiti päyütn  (sd.)  dadät  .  .  anyim  ^wahmat '^irasüi  mananhasai yaya  syao'iamüi  ahm
"^raoitS  (sd.)  V,  46. 7  •'.  a)  vom  Opfer- feuer: at  a  ^wahmäi  '%r!  ratam  iiima- t>hs  .,  asahyä  mä  ..  manyäi  (sd.)  Y.  47- 9.  b)   vom   eschatologischen   Ordal-
feuer***':  yqm  xsnBtftn  ränsibyä  (sd.)  da "^wä  ''ira  suxrä  mazdä  ayanhä  xiustä Y.5/.9;  31.3;  —  (a  da  spmta  mainyü ,  ■  '"^ra  vaahäu  vldäitim  (sd.)  ränStiyä  V. 47-  6j  3^-  '9;  —  ahurä  . .  yä  da  airs  (sd.) .  .  %wahya  garima  '%rS  asa.aojaah3  Y. 4J.4;  —  aitSi  'irSm  ahurä  aojSnhvanttm (sd.)  asä  usSmahl  .  .  siöi  rapantl  ci%ra.- avaahim  al  .  .  daibisyant!  .  .  dir^stä.- agnanh)m  Y.34'4-
Undeutlich:  'tar»  V.  7. 52  PuZ.'>;  —  'tars N.  70J;  —  °>rS  N.  75.
+1  Vgl.  JN.  GIrPh.  z.  641.  Clier  das  feuer im  Kult  s.  N.  /^  ff. ;  ferner  Sp.  Av.  2.  LXv,  DsT. ZA.  7.  LX^  In  dei  Mythologie  tritt  Alur  her- vor 1)  durch  seinen  Kampf  mit  AiayDaliJka um  das  i^'tirjiiah,  s.  Vi.  Ig-  \6f(. ;  2)  dmch  seinen Sieg  in  Gemeinschaft  mit  VehuManah  über  den angreifenden  AuraMainyat;  s.  Yt.  13.  77  f.,  Y. 46.  7.  —  ")  Der  TeuerbebSlter'  (d/«i  liia)  hat seinen  riati  auf  dem  'Feuersland'  {iitusi  od« äHU)7\  an  der  'Feuerslätte'  iftia's  i^ä6),  d.  i.  in der  Südhälfte  des  'OpferhauEes'  {j-azisH  xJn,ii); vom  Za^/ar  (Oberpriester)  aus  gesehen,  der  an der  Nordwand  der  'Opferstälte'  {ya::Jii  gilli),  d.  i. der  Nordhälfte  des  'Opferhaoses'  silit,  jenseits ■  des  Gerilctisches  (s.  araiiar-'),  auf  dem  auch I  das  Bai/iman  sich  befindet.  S.  oben  1  b.  — I  •")  Vgl.  dazu  oyah-  A  und  inlay-*') ;  ferner  lu
KompA.  1  Ableit.  —  mp.  Sliir',  np.  jW; arm.  vgl.  (i;>7'/'verbrennen';  weiteres  bei  Hbm.  . AGr.  7.  418.  S.  noch  No.  3.  —  iFlex.  Srf«'. jEi.  (unsicher)  IF.  5.  220,  BB.  23.  68.  —  Pü. : fl/fl/;  S.N0.3.—  ■)  Nur  im  AS.  älrim.  (%8)^\ woneben  seltener  ä%i->m  und  iilatun.  S.  auch ä/ryo'.  —  ")  Eine  strenge  Scheidung  der  ein- zelnen Bedeutungen  von  ä'm-  ist  nicht  durch- lufiihren.  —  3)  Als  gelW.  in  mp.,  np.  älits, sbal.  äc,  arm.  LW.  .ifas.—  4)  Hds.  <iDr).— i)  Them-,  s.  No.  8.  —  *)  Vgl.**).  —  7  <  BeideWöner aus  ir.  *.J//--//o/-.  J//i/  steht  Dd.  jiS".  15.  <Vi/si kann  ich  nicht  belegen ;  aber  Päi.  .i./.'fV  ist nur  eine  ungeschickte  Wiedergabe  des  Worts. Pars,  adik  in  SWien.\W.  67.  S37.  22  —  mil derErl.;  älas  ti  bar  ü  sü:anJ — ist  aus  adät, mit  dem  «-Zeichen  darüber?,  verlesen,  also ädusl.  —  S)  ältaahyö  in  Vd.  (s.  No.  5)  ist  werllos.
•  j.  'ä-tar-  m.  'Bedränger,  Angreifer'  (von i/oÄischenWesen):  iitse  *vatiAanhqm  paiti-
ität^e  'ranqiii'-'i  Y.H0.4;  —  vT  d'aiväil .  . sarjm  mruyi  .  .  vT  kahyäclt  hätqm  'räii^^ Y,72.4;  —  "iwä  paiti  'rS  VyL  26"(?).
Zum  V.  !,„..  —  ai.  vgl.  ^r"a-<"'-  Adj.  - Pü.:  -..■.ai„r.  valtam.  —  ')  Them.
•  j.  ätara'Dra  Adv.  'auf  dieser,  nach  dieser
dby  Google
317  ataradar-  —  ätrsvaxS-  318
der   beiden  Seiten':  yatara  (sd.)  ,,   °'^ra  •  j.   ätara'^iSra-,   'ät^9.6il^^a-   m.   EN.
fraoirisyeiti  YtJO.g;  iy.47.  1)  eines  Gläubigen:    'rahe  asaonS  '^i.13-
Adv.  m  aiära-').  —  ")  Wonach  man  *ai>ira-    102.  a)  unter  den  Namen,  die  fiir  den
%raodet  *^/ara%ra  (s  294.  3)  verlangte.  imSchlaf  ergossenenSamen  vorgeschrieben
•  j.  atar«-dar-  Adj.   (auch  fem.)   'ignem   ^^t^^Ti-.  aat hi mma  fradai>ya  Str^JäUm effundens,  Feuer  ausströmend,  aus  sich  ent- ;  (sd,)  ya  -rgm  vä  ..  V.ijf.52. wickelnd':  aaaya  urvarayh  •'i-af»/(GSfO'*|     Eig,  vll.  'dem  Feuer  {Äuir)  entstammt'.  —
V.Ä75.  Vgl.    ^il,-?.h%ra-    und    älarU>%ra~.    -    ')    So
Zum  V.  Ikar:  —   ai.  »gl.   'iir-  Adj.  —   l'ii.;       V.  rS.
^fiti'"'Tir~  zL'^'"'  ""^  ""'  ^  '^'  ■"el"-|.  j.+ät9r»-tarö.naema-'>m. 'die  über  das
/'  /■Rh       r  ■  1"      /   /"  I  Feuer  hinaus,  jenseits  des  Feuers  gelegene"
p^aara      .4.    4.   les  j  ar  j.  j  Seite  (der  Opferstätte)':  "«,7/ "von  jenseits
•  j.  atar«.fri»ita-  Adj.  'vom  Feuer  ge-  [  ^^^  Feuers"  F.  7.
liebt,    Liebling  des   Ätar':    "t^mca   F.7.  ,       Pq  .  ruai  *lar' nimal-   —  ■>  Hds    •/ararn-    —
•/ri5//fl-Adi.,PPfP.!U*AAai'rt-,den.Praes.3l        ,)  <iom  Plati  des  Z.wl.,fs.  aus. aus  /rt%a-;    vgl.  iBüd.  (ü.  mei;kilä-,  Wn.Gr.»  1  _  ,  _
S  j'otf^a.»  —  Vä-:  ätai  framifi,  erL:  .!/(  1 1  •  j.  atflM'daiahav-,  atrs.daliyav- m.EN. raiiHm  "der  am  meisten  A'.  ist".  —  ')  Dabei  j  i)  eines  Gläubigen:  "daiähSus  asaonS  YL Ut    die    richtiße    Oberlieferung    des   Worls!,^  ,03.  2)  unter  den  Namen,  die  fiir
T  rausgese    .  ,.,     .  ,         |  den  im  Schlaf  ergossenen  Samen  vorge-
•  j.  atar3.mar»zana-'>  m.  'Vorrichtung,  ^^hrieben  werden:  aat  hlnama /radai-:iyä das  Feuer  (von  der  Asche)  zu  re.nigen' :  j, j^_^^,^„  (,d.)  ya  .'.  -d^hyäm  v.l  .  .  V. ■«^  F.  7.  ^  /.Vgz
^^^Im^"'"'   "■  "^'^  """'■"'"'"  "■  -  ^"■=!      Kg.  'lum  Z).  des  Feuers  (^Wr)  gehörig'. -  H-  -i  ..    _     .  .,        '  »i.  ''''ätt»r»-5äta-'','ätr«.däta-Adi.  i)  'von
-i  „    •*       _  -1.       A      'j  -1         -*'"'  gegeben,  geschenkt':  *°0(J/a ''  va^-wa
atar9.vitar9.matDyascit    vitar».maiiyas- \  ''■,•,,    ^  11  r.   '  i.
at"  Yl  •>  17  '.yazammde  \x.ig.i.  2)    von  Atar  her,
-  "■   ^'  I  aus  gegeben',  von  Namen  und  von  dessen
•  j.  ätarä-äSra-  Adj.  'dem  Feuer  {Älar)  \  Träger  sva.  'zu  Ätar  m  Beziehung  gesetzt, entstammt':  'rJtca  yazati ..'rSsca  V<w-«k/|  stehend':  aat  As  (näml.  naire)'^  nama yaxamaide  Yt-iO.!.  Wradai%yä    StrsMüm    vä  ätrg.ci>nm  va
Komp.  mit  GS.  im  i.^GUed.  -  Vgl.  'Siri^\ atnjiaiiiam  v3  älf?.daßyüm  vä  iqmätva m/nii  JämJ'\-^^jTi''rX')\fk'äfJ'äi.  I  ''''^'  "?'""  """•^  als  Namen  sollst  du  ihm'' rJJ  iir  i  vih  itaän  iari.  —  0  DsT.  ZA.  /.  1  beilegen:  Ä.  oder  .  .  oder  sonst  irgend 480  will  röSii,  I  ein  Wort  als  Namen,  das  mit  Ä.  in  Be-
•  j.  'kvail  5tSe  yaza  afi^s  . ."  FrD.  7.   I  ^ie^ung  gesetzt  ist"  V.  ^^52.
I  a/as  ä.if,    [zu  V,);    fehlt    —    ■»  So  K.  7.    —
•  j.  ätrv.karst-  Adj.  'der  sich  mit  dem  j  ')  Nämt.  dem  Mann,  der  seinerieit  {»/•"  süram Feuer  zu  tun  macht,  dabei  tätig  ist':  'tä,  /raB.i-^y^nm)  aus  dem  im  Schlaf  ergossenen p  _                                                                             !  Samen  erstehen  soll;  rgl.  v.  iS.  40,  51.
Vä.:  ü/ai  iariäf.  |«   j.  'ät«r«'däta-,  'ätra.däta- ">  m.   EN.
.   -^      ,  .—  ...  ,     I  i)   eines   Gläubieen;    'lafie  aSaonü  Yt.  I?.
•  ].  atM.Öarana-  n.  'Feuergerat,  zur  In-  '  ^'  ^  ,  ,  ^  ,  ,.  ,.  „,  ,-' standhaltung  des  Feuers  dienendes  Gerät':  .^°|- „  ^)  ^nter  den  Namen,  d,e  fiir  den '«  (AP.)  pairisMnäna  V.  14. 7-                   ""^^'"^^  ergossenen  Samen  vorgeschrieben
Wana- nf'Gerit'  lumV  ikaZ  lii.cärana-n.  'werden:  Hat  h?  nqma  fradaiiiyä  'tum  vä Tgl.  iararia-  n.  ~  Vgl.' Slr.fJpr/t-.  —  Pü.!|.  ■  iamcU  vä  ätrs.dätalie  (sd.)  nama  V, älni  *iariär  (s.  ölrfJ^til-).  l8.%2.
•  j.  ■ätr«.ä«Ta-  Adj.  (fem.  =rJ-)  'ignis '  "^s'-  '"""»''"•'  "'"^■''«'■■'-  -  ■>  So  V.  r8. seraen  continens,  worin  das  Feuer  seine,«  J-  ätt.r»'p5ta-  m.  EN.  eines  Gläubigen: Nahrung  findet",   von  Pflanzen:   aSsma  .  ..'i>'^'  '^^'"""'^  Yt.7?.io2.
M^a  asta.ka,n  un-aranan,  yat  'ränan, ;     ^^  ^^^_  ''^^:l  ^^'^:^,:  '
'vg".ifr,.Ä5«.  EN.  und  5iari.c^r>i:-  Pü.J*  J"  ätra-vaxä-'>,  ätra-vaxä-"  m.  Name Hai  lätmai.  '■  des   zweiten,    mit   der  Unterhaltung   des
dby  Google
299
ahyäsa-
•  j.  ahyasa-"  fem.  Adj.  'die  Worte  ahyä yäsä  enthaltend,  damit  beginnend':  "sa Aaitir  {sd.)'<  y.  2A'  Überschr.;  —  's^m Aainm  yazamaide  Y.  2iV.  1 2.
')  Durch  Haploloffie  (lu  S^o6)  —  oder  eher vll.  Haplographie  —  für  ahyayäs",  —  J)  D.  i. Y.  2S.
```


## [2026-09-05T05:24:51.990Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 atrocious ===\"; grep -n -o \"atrocious[^|]\\{0,400\\}\" KLN_1966.txt | head -5\necho; echo \"=== KLN atrium ===\"; grep -n -o \"atrium[^|]\\{0,300\\}\" KLN_1966.txt | head -5\necho; echo \"=== KLN Adriatic ===\"; grep -n -o -i \"adriatic[^|]\\{0,300\\}\" KLN_1966.txt | head -5\necho; echo \"=== KLN azure/Avestan atar ===\"; grep -n -o -i \"atar[sšv][^|]\\{0,200\\}\" KLN_1966.txt | head -10",
 "description": "Grep Klein 1966"
}
```


### [2026-09-05T05:24:53.708Z] TOOL RESULT

```
=== KLN 1966 atrocious ===
3869:atrocious. Cp.  also  Atharvan.  For  the  etymology  of  L.  bilis see  bile.  For  the  ending  of  atrabiliary  see  adj. suff.  -ary.
3875:atrocious,  adj.,  extremely  cruel  or  wicked.  — Formed  with  suff.  -ous  fr.  L.  atrox,  gen.  atrdcis, ‘cruel,  fierce’,  prop,  ‘dark-looking,  gloomy’, and  compounded  of  ater,  ‘black,  dark’,  and -ox,  gen.  dcis,  ‘looking’.  For  the  first  element  see atrabilious.  The  second  element  is  cogn.  with Gk.  1,  gen.  cot to?,  ‘eye,  sight’.  See  -ops  and  cp. the  second  element  in
3875:atrocious-ly,  adv.,  atrocious-ness. atrocity,  n.,  atrociousness.  —  F.  atrocite,  fr.  L. atrocitdtem,  acc.  of  atrocitas,  ‘cruelty’,  fr.  atrox. See  prec.  word  and  -ity.
14244:atrocious,  ferocious, velocity.  Derivatives:  eye,  tr.  v.,  ey-ed,  adj.
14277:atrocious’,  fr.  facinus, gen.  facinoris,  ‘deed’,  esp.  ‘wicked  deed,  crime, villainy’,  fr.  facere,  ‘to  make,  do’.  See  fact.  For E.  -ous,  as  equivalent  to  L.  -us,  see  -ous. facio-,  combining  form  meaning  ‘pertaining  to the  face,  facial’.  —  Fr.  L.  facies,  ‘face’.  See  face, facsimile,  n.,  an  exact  copy.  —  L.  fac  simile, ‘make  like’,  fr.  fac,  imper.  of  facere,

=== KLN atrium ===
3513:atrium,  ferrum, sodium,  etc.  —  Named  after  the  Brazilian  geo¬ logist  Dr.  Miguel  Arrojado  of  Lisbon.  For  the ending  see  subst.  suff.  -ite. arrondissement,  n.,  an  administrative  district  of
3875:atrium,  n.,  1)  the  central,  courtlike  room  of  the ancient  Roman  house;  2)  ( anat .)  cavity  in  the heart  or  in  the  ear.  —  L.  atrium;  according  to Varro,  De  Lingua  Latina  5,  §  161,  a  word  of Etruscan  origin  and  rel.  to  the  Etruscan  town Atria,  as  the  place  of  ori
3875:atrium  with  ater, ‘black,  dark’,  is  folk  etymology, atrocious,  adj.,  extremely  cruel  or  wicked.  — Formed  with  suff.  -ous  fr.  L.  atrox,  gen.  atrdcis, ‘cruel,  fierce’,  prop,  ‘dark-looking,  gloomy’, and  compounded  of  ater,  ‘black,  dark’,  and -ox,  gen.  dcis,  ‘looking’.  For  t
8486:atrium of  a  Roman  house  through  which  the  rain  flew into  the  impluvium  ( Roman  antiq.)  —  L.,  fr. compluere,  ‘to  flow  together’,  fr.  com-  and pluere, ‘to  rain’.  See  pluvial  and  cp.  impluvium. comply,  intr.  v.  —  It.  complire,  fr.  VL.  *complire, which  corresponds  to  L.  
18920:atrium  of  the ancient  Roman  house.  —  L.,  fr.  impluere,  ‘to rain  into’,  fr.  in-,  ‘in’,  and  pluere,  ‘to  rain’.  See pluvial  and  cp.  compluvium. imply,  tr.  v.  —  OF.  emptier,  fr.  L.  implicare,  ‘to infold,  involve,  intangle’,  fr.  in-,  ‘in’,  and  pli-

=== KLN Adriatic ===
1657:Adriatic
1710:Adriatic.  —  See  Adriatic  and  -an. Adrian,  masc.  PN.  — •  L.  Adrianus,  Hadrianus, lit.  ‘of  the  Adriatic’.  See  next  word.
1711:Adriatic,  adj.  —  L.  Adriaticus,  Hadriaticus,  fr. Atria,  also  called  Adria,  Hadria  (now  Atri), a  town  in  Picenum,  fr.  dter,  fem.  atra,  neut. atrum,  ‘black’,  hence  lit.  ’the  black  city’  (see atrabilious  and  -atic);  the  town  was  so  called because  it  was  built  on  black  mu
10254:Adriatic.  Cp.  dal¬ matic.
18750:Adriatic.  —  Formed  with  suff.  -an  fr.  L.  Illyria, fr.  Gk.  ’ITXupla,  which  is  short  for  7)  ycopa  yj ’IXXupla,  ‘the  Illyrian  country’,  TXXupta  being the  fern,  of  ‘IXXupto?,  ‘Illyrian’.

=== KLN azure/Avestan atar ===
3812:atarsh,  ‘fire’,  atrya-,  ‘ashes’,  and  cogn.  with  L. ater,  ‘black,  dark’.  See  atrabiliary.
6804:atars).  Cp.
23694:atarsal,  1)  pertaining  to  the  metatarsus;  n., matatarsal  bone.  —  See  next  word  and  adj.  suff. -al.
23695:atarsus,  n.,  part  of  the  foot  between  the  tarsus and  the  toes  (anat.  and  zool.)  —  ModL.,  formed fr.  meta-  and  tarsus.
```


## [2026-09-05T05:25:08.155Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3805,3820p' KLN_1966.txt\necho \"=== 3860-3880 ===\"; sed -n '3860,3878p' KLN_1966.txt\necho \"=== 6800-6810 ===\"; sed -n '6800,6808p' KLN_1966.txt",
 "description": "Print Klein context"
}
```


### [2026-09-05T05:25:08.253Z] TOOL RESULT

```
-ate,  verbal  suff.  —  L.  pp.  suff.  -dtus,  hence  deriv¬ atively  identical  with  adj.  suff.  -ate  (q.v.)  Its original  use  consisted  in  the  formation  of  verbs from  participial  adjectives  in  -ate.  So  e.g.  from the  participial  adj.  separate  arose  the  verb  to separate.
-ate,  subst.  suff.  expressing  office,  dignity,  rank, honor.  —  L.  -dtus  (gen.  -atus),  a  suff.  formed from  the  participial  suff.  -dtus.  Cp.  e.g.  consulate and  see  adj.  suff.  -ate.
-ate,  subst.  suff.  forming  names  of  salts  from acids  whose  names  end  in  -ic,  as  nitr ate,  fr. nitric  acid  (chem.)  —  L.  -arum,  neut.  of  pp.  suff. -dtus.  See  adj.  suff.  -ate. atelectasis,  n.,  incomplete  expansion  of  the  lungs (med.)  —  Medical  L.,  compounded  of  Gk. a-tdkTfi,  ‘incomplete’,  and  £xxa ait;,  ‘extension, expansion'.  The  first  element  is  formed  fr.  d- (see  priv.  pref.  a-)  and  x£Xo 9,  ‘end’;  see  teleo-. For  the  second  element  see  ectasis. atelier,  n.,  workshop,  studio.  —  F.,  fr.  OF.  aste- /  lier,  fr.  astelle,  ‘shiver  of  wood’,  fr.  Late  L.  as- tella,  fr.  L.  astula,  which  is  prob.  a  blend  of assula,  ‘shiver  of  wood’  and  hastula,  ‘a  little spear’.  Assula  is  a  dimin.  of  assis,  ‘board,  plank’ ; see  ashlar.  Hastula  is  a  dimin.  of  hasta,  ‘spear’; see  hastate.*
Athanasius,  masc.  PN.  —  L.,  fr.  Gk.  ’Afixvdaioc, fr.  dffdvaxoi;,  ‘immortal’.  See  next  word, athanasy,  n.,  immortality.  —  Gk.  dthxvaota,  fr. affdvaxo:,  ‘immortal’,  fr.  a-  (see  priv.  pref.  a-)
■5
and  ffdvaxo?,  ‘death’.  See  thanato-  and  cp. euthanasia.  For  the  ending  see  -y  (representing Gk.  -la).
athanor,  n.,  the  self  feeding  furnace  of  the  al¬ chemists.  —  F.,  fr.  Arab,  at-tanniir,  ‘the  oven’, fr.  at-,  assimilated  form  of  al-,  ‘the’,  and  tannfir ‘oven’,  borrowed  fr.  Heb.  tanndr,  which  is  rel. to  Akkad,  tinnuru,  ‘oven’.
Atharvan,  n.,  name  of  a  fire  priest,  the  eldest  son of  Brahma  (Vedic  mythol.)  —  OI.  atharvan, ‘fire  priest’,  rel.  to  Avestic  d&ravan-,  ‘fire  priest’, atarsh,  ‘fire’,  atrya-,  ‘ashes’,  and  cogn.  with  L. ater,  ‘black,  dark’.  See  atrabiliary.
atheism,  n.  —  F.  atheisme,  formed  with  suff. -ism  fr.  Gk.  fiS-eo?,  ‘without  god’,  fr.  d-  (see priv.  pref.  a-)  and  B-eo?,  ‘god’.  See  theism.
atheist,  n.  —  F.  atheiste.  See  prec.  word  and  -1st. Derivatives:  atheist-ic,  athest-ic-al,  adjs.,  athe- ist-ic-al-ly,  adv.
atheling,  n.,  a  noble,  a  prince.  - —  OE.  aedeling, ‘a  noble’,  fr.  tedele,  ‘noble’,  which  is  rel.  to OFris.  ethele,  OS.  edili,  OHG.  edili,  MHG. edele,  G.  edel,  ‘noble’.  The  orig.  meaning  of these  adjectives  was  ‘noble  by  birth’.  Cp.  odal and  the  first  element  in  Albert,  allerion,  Alphon- so,  Athelstan,  Audrey,  edelweiss,  Ethelbert, Etheldred,  Ethelinda,  Ulrica.
Athelstan,  masc.  PN.  —  OE.  Mdelstane,  lit. ‘noble  stone’,  fr.  sedele,  ‘noble’,  and  stan,  ‘stone’. For  the  first  element  see  atheling  and  cp.  words there  referred  to.  For  the  second  element  see stone.
Athena,  Athene,  fern.  PN.,  the  goddess  of  wis¬ dom  in  Greek  mythology,  identified  by  the Romans  with  Minerva.  —  Gk.  ’  A&rjvrj ,  a  pre- Hellenic  name  of  uncertain  origin.
Athenaeum,  n.,  the  temple  of  Athena  at  Athens; whence  athenaeum  1)  a  Roman  school  of  law; 2)  a  literary  club.  —  L.,  fr.  Gk.  ’AOrpiatov,  the temple  of  the  goddess  Athene  fr.  ’A&tjvt).  See prec.  word.
atherine,  n.,  any  of  the  fishes  of  the  family  Ather- inidae  ( ichthyol .)  —  ModL.  atherina,  fr.  Gk. xffEpfvr;,  ‘smelt’,  fr.  ‘gruel,  porridge’,
which  is  rel.  to  afif)p,  ‘awn,  chaff,  barb  of  a weapon’,  dvffsptxo?,  ‘the  asphodel’.  See  An- thericum  and  cp.  atheroma.
=== 3860-3880 ===
123
atom,  n.  —  F.  atome,  fr.  L.  atomus,  fr.  Gk.  axop.04, ‘atom’,  prop,  ‘uncut,  indivisible’,  fr.  4-  (see priv.  pref.  a-),  and  -xopop,  fr.  xspvetv,  ‘to  cut’. See  tome  and  cp.  anatomy.  The  word  axop.09 was  first  used  by  the  Greek  philosopher Leucippus.
Derivatives:  atom-ic,  adj.,  atom-ic-ity,  n.,  atom¬ ism,  n.,  atom-ist,  n.,  atom-ize,  tr.  v.,  atom-iz- ation,  n.,  atom-iz-er,  n.
atomy,  n.,  skeleton.  —  From  misdivision  of  ana¬ tomy  into  an  atomy.  See  anatomy, atomy,  n.,  pygmy.  —  L.  atomi  (pi.  of  atomus, ‘atom’),  mistaken  for  a  singular.  See  atom, atone,  intr.  v.  —  Short  for  ‘to  be  at  one’.
Derivatives:  atone-ment,  n.,  aton-ing-ly,  adv. atonic,  adj.  —  Formed  with  suff.  -ic  fr.  Gk. 4xovo5,  ‘not  stretched,  slack;  without  tone’, fr.  4-  (see  priv.  pref.  a-)  and  xovop,  ‘tone’.  See tonic  and  cp.  diatonic.
atony,  n.,  want  of  tone.  —  ML.  atonia,  fr.  Gk. 4xovia,  ‘slackness,  debility’,  fr.  axovop.  See  prec. word  and  -y  (representing  Gk.  -ia). atopic,  adj.,  pertaining  to  atopy  (med.)  —  Formed with  suff.  -ic  fr.  Gk.  6x07104,  ‘out  of  place;  un¬ usual’,  fr.  4-  (see  priv.  pref.  a-)  and  xoirop, ‘place’.  See  topic.
atopite,  n.,  calcium  antimonate  (mineral.)  — Formed  with  subst.  suff.  -ite  fr.  Gk.  axojtop. See  atopic.
atopy,  n.,  allergy.  —  See  atopic  and  -y  (represent¬ ing  Gk.  -(a).
-ator,  subst.  suff.  —  L.  -ator,  forming  masculine agential  nouns  from  verbs  of  the  first  conjuga¬ tion.  Accordingly  the  suff.  -ator  consists  of  -a-, the  characteristic  vowel  of  the  first  conjugation, and  suff.  -tor  (q.v.)
atrabiliary,  adj.,  melancholy,  hypochondriac.  — Medical  L.  atrabiliarius,  ‘suffering  from  black bile’,  fr.  L.  atra  bilis,  ‘black  bile,  melancholy’, loan  translation  of  Gk.  piXctivoc  yoXf)  (see  me¬ lancholy).  Atra  is  fem.  of  ater,  ‘black,  dark’,  rel. to  Umbr.  atru,  adro  (neut.  pi.),  ‘black’,  and prob.  cogn.  with  OI.  atharvan-,  Avestic  a&ra- van-,  ‘fire  priest',  dtarsh,  ‘fire’,  atrya-,  ‘ashes’. Arm.  airem,  ‘I  light  up,  kindle’.  Cp.  atrocious. Cp.  also  Atharvan.  For  the  etymology  of  L.  bilis see  bile.  For  the  ending  of  atrabiliary  see  adj. suff.  -ary.
Derivative:  atrabiliari-ous,  adj. atrabilious,  adj.  —  Formed  with  suff.  -ous  fr.  L. atra  bilis.  See  prec.  word.
Derivatives  :atribilious-ly,adv.  ,atrabilious-ness,n . Atractaspis,  n.,  a  genus  of  African  burrowing vipers  (zool.)  —  ModL.,  lit.  ‘arrow  snake’,  fr. Gk.  Sxpaxxop,  ‘spindle,  arrow’,  and  4<rmq, ‘serpent,  snake’,  The  first  element  is  cogn.  with L.  torquere,  ‘to  twist,  bend’ ;  see  torque.  For  the second  element  see  asp,  ‘snake’.
Atragene,  n.,  a  genus  of  trees  of  the  buttercup family  (bot.)  —  ModL.,  fr.  Gk.  d-SpayF/ir),  ‘tra¬ veler’s  joy’,  compounded  of  S&pap,  ‘chariot’, and  -yevr],  ‘of  a  certain  kind’.  The  first  ele-
menivSrands  for  *f4(v)ftpae  and  is  cogn.  with OI.  vandhurah,  ‘a  hamper  (made  of  wicker¬ work)’,  fr.  I.-E.  base  *wendh-,  *wtxdh-,  ‘to  turn, twist’,  whence  also  ON.  vinda ,  OE.  windan, ‘to  wind,  twist’;  see  wind,  ‘to  turn’.  The second  element  is  rel.  to  Gk.  ysvop,  ‘race, descent,  gender,  kind’;  see  genus  and  cp.  -gen. atresia,  n.,  occlusion  of  a  natural  passage  of  the body  (pathol.)  —  Medical  L.,  fr.  Gk.  axpvjxo 5, ‘not  perforated’,  fr.  4-  (see  priv.  pref.  a-)  and xp-pxop,  verbal  adj.  of  xexpatveiv,  ‘to  pierce, perforate’,  which  is  rel.  to  xeipciv  (for  *x!pjeiv), ‘to  rub,  rub  away,  wear  away’,  fr.  I.-E.  base *ter-,  ‘to  bore,  pierce,  rub’.  See  throw  and  cp. words  there  referred  to.  For  the  ending  see suff.  -ia.
Atreus,  n.,  a  son  of  Pelops  and  father  of  Aga¬ memnon  and  Menelaus  (Greek  mythol.)  — -  L., fr.  Gk.  ’Axpeu4,  a  word  of  uncertain  origin, atrip,  adv.  (nautl)  —  Formed  fr.  a-  ‘on’,  and  trip. Atriplex,  n.,  a  genus  of  plants  of  the  goosefoot family  (bot.)  —  L.  atriplex ,  ‘orach’,  fr.  Gk. axpatpaipup,  which  is  of  unknown  origin.  Cp. orach.
atrium,  n.,  1)  the  central,  courtlike  room  of  the ancient  Roman  house;  2)  ( anat .)  cavity  in  the heart  or  in  the  ear.  —  L.  atrium;  according  to Varro,  De  Lingua  Latina  5,  §  161,  a  word  of Etruscan  origin  and  rel.  to  the  Etruscan  town Atria,  as  the  place  of  origin  of  this  kind  of  ar¬ chitecture.  The  connection  of  atrium  with  ater, ‘black,  dark’,  is  folk  etymology, atrocious,  adj.,  extremely  cruel  or  wicked.  — Formed  with  suff.  -ous  fr.  L.  atrox,  gen.  atrdcis, ‘cruel,  fierce’,  prop,  ‘dark-looking,  gloomy’, and  compounded  of  ater,  ‘black,  dark’,  and -ox,  gen.  dcis,  ‘looking’.  For  the  first  element  see atrabilious.  The  second  element  is  cogn.  with Gk.  1,  gen.  cot to?,  ‘eye,  sight’.  See  -ops  and  cp. the  second  element  in  ferocious,  velocity. Derivatives:  atrocious-ly,  adv.,  atrocious-ness. atrocity,  n.,  atrociousness.  —  F.  atrocite,  fr.  L. atrocitdtem,  acc.  of  atrocitas,  ‘cruelty’,  fr.  atrox. See  prec.  word  and  -ity.
Atropa,  n.,  a  genus  of  plants  of  the  potato  family (bot.)  —  ModL.,  fr.  Gk.  4xpo7ia,  ‘the  deadly nightshade’,  which  is  rel.  to  ’'Axpotrop,  name of  one  of  the  Fates.  See  Atropos. atrophy,  n.,  a  wasting  away  through  lack  of nourishment  (med.)  —  F.  atrophie,  fr.  L.  atro¬ phia,  fr.  Gk.  4xpo<p(a,  ‘want  of  food’,  fr.  dcxpo- 904,  ‘not  nourished,  ill-fed’,  fr.  4-  (see  priv. pref.  a-)  and  -xpotpop,  fr.  xpocpf),  ‘food,  nourish¬ ment’.  See  trophic  and  cp.  athrepsia.  Cp.  also dystrophy,  hypertrophy.
Derivatives:  atrophy,  intr.  and  tr.  v.,  atropli-ic, atrophi-ed,  adjs.
atropine,  also  atropin,  n.,  an  alkaloid  poison extracted  from  belladonna.  —  Formed  with chem.  suff.  -ine,  resp.  -in,  fr.  Gk.  axpona,  ‘the deadly  nightshade’.  See  Atropa.
=== 6800-6810 ===
Catharist,  n.,  a  member  of  any  of  various  sects aiming  at  purity  ( Eccles .  hist.)  —  ML.  Catha- rista,  fr.  Eccles.  Gk.  xaf>apumf)<;,  fr.  Gk.  xaffa- poc ,  ‘pure,  clean’;  cp.  Gk.  xaffapiaTYip,  ‘tree pruner’,  and  see  next  word.  For  the  ending  see suff.  -ist.
catharsis,  n.,  i)  purgation  ( med.)\  2)  purification of  the  emotions  by  art.  —  ModL.,  fr.  Gk.  xaffxp- csi.q,  ‘cleansing,  purification’,  from  the  stem  of xaffalpeLv,  ‘to  cleanse,  purify;  to  prune  (a  tree)’, fr.  xaffap6p,  ‘clean,  pure’,  which  is  of  uncertain origin.  Cp.  cathartic,  Catherine,  acatharsia.
cathartic,  cathartical,  adj.,  cleansing,  purifying. —  Gk.  xoefrap-uxo?,  ‘fit  for  cleansing’,  from  the stem  of  xaffalpstv.  See  prec.  word.
Derivatives:  cathartical-ly,  adv.,  cathartical- ness,  n.
Cathay,  n.,  poetic  name  of  China.  —  ML.  Ca- taya,  fr.  Khitai,  the  name  of  a  Tatar  kingdom (the  kingdom  of  the  Khitan  Tatars).  Cp.
Khitan.
cathedra,  n.,  the  seat  of  a  bishop.  —  L.,  fr.  Gk. xaffcSpa.  See  chair  and  cp.  ex  cathedra.
cathedral,  n.  —  ML.  cathedralis,  short  for  ecclesia cathedralis,  ‘church  pertaining  to  the  seat  of  a bishop’,  fr.  cathedra.  See  prec.  word  and  adj. suff.  -al.
Catherine,  Catharine,  also  Katherine,  Katharine,
```


## [2026-09-05T05:25:22.967Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T05:25:22.974Z] TOOL RESULT

```


```


## [2026-09-05T05:25:26.475Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AA%D8%B4",
 "prompt": "Give the full Persian etymology section for آتش (ātaš) 'fire': the Middle Persian form, Old/Proto-Iranian reconstruction, Avestan form, and any cited sources. Also list any related terms like آذر."
}
```


## [2026-09-05T05:25:28.020Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1",
 "prompt": "Give the full Persian etymology for آذر (āzar) 'fire, the month Āzar': Middle Persian form, Avestan, Proto-Iranian reconstruction, and cited sources."
}
```


### [2026-09-05T05:25:33.479Z] TOOL RESULT

```
# Persian Etymology of آتش (ātaš) - 'Fire'

## Middle Persian Form
The word derives from Middle Persian *ʾthš* /ātaxš/, meaning "fire."

## Proto-Iranian & Avestan Origins
The etymology traces back through Proto-Iranian *HáHtr̥š to Avestan *𐬁𐬙𐬀𐬭𐬱* (ātarš), also meaning "fire." The Avestan form was borrowed into Middle Persian specifically for its specialized significance in Zoroastrian religious contexts.

## Key Etymology Details
According to the source: "borrowed from Avestan 𐬁𐬙𐬀𐬭𐬱 (ātarš, 'fire') for its special meaning in Zoroastrianism and well preserved unlike the other word آذر (âzar, 'fire')." The word ultimately derives from Proto-Indo-European *h₂eh₁ter-.

## Related Terms
- **آذر** (âzar) - an alternate Persian word for "fire," listed as a synonym and doublet of آتش. This related term is less well-preserved than آتش in modern Persian.

## Cited Source
Nişanyan, Sevan (2015-05-11), in *Nişanyan Sözlük* dictionary.
```


### [2026-09-05T05:25:33.666Z] TOOL RESULT

```
# Persian Etymology of آذر (āzar)

**Middle Persian Form:**
The word descends from Middle Persian 𐭭𐭥𐭥𐭠 (NWRA /⁠ādur⁠/).

**Avestan Cognate:**
It is cognate with Avestan 𐬁𐬙𐬀𐬭 (ātar), sharing the same ancient root.

**Proto-Iranian Reconstruction:**
The reconstructed Proto-Iranian form is *HáHtr̥š, representing the ancestor of these related terms across Iranian languages.

**Proto-Indo-European Origin:**
The etymology may ultimately derive from Proto-Indo-European *h₂eh₁-tr-, suggesting a deep historical connection across Indo-European language families.

**Related Form:**
آذر functions as a doublet of آتش (ātiš) in Persian, both descending from this shared etymological lineage and meaning "fire" in archaic contexts.
```


## [2026-09-05T05:25:39.081Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ater",
 "prompt": "Give the Latin etymology section for 'ater' (black): the Proto-Italic and PIE reconstruction, cognates (Avestan, Umbrian, Albanian), any mention of de Vaan or dispute, and derived terms such as atrox and atrium."
}
```


## [2026-09-05T05:25:40.105Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/atrium",
 "prompt": "Give the Latin etymology section for 'atrium': all proposed origins (Etruscan, from ater, from a town Atria), which is preferred, and any cited scholars (de Vaan, Varro)."
}
```


### [2026-09-05T05:25:45.674Z] TOOL RESULT

```
# Latin Etymology of "Ater" (Black)

## Proto-Italic and PIE Reconstruction

The article states that Latin *āter* derives "From [Proto-Italic](https://en.wikipedia.org/wiki/Proto-Italic_language "w:Proto-Italic language") _[\*ātros](/wiki/Reconstruction:Proto-Italic/%C4%81tros)_, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*h₂eh₁ter-](/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81ter-)_ ("fire")."

## Cognates

The entry lists several related forms across Indo-European languages:
- Proto-Iranian *HáHtr̥š* ("fire")
- Umbrian *𐌀𐌕𐌓𐌖* (atru)
- Oscan *𐌀𐌀𐌃𐌝𐌓𐌉𐌉𐌔* (aadíriis)
- Old Irish *áith* ("kiln")

The page does not mention de Vaan, provide dispute information, or include etymological details for related terms like *atrox* and *atrium* in the etymology section itself.
```


### [2026-09-05T05:25:46.313Z] TOOL RESULT

```
# Latin Etymology of "Atrium"

Based on the Wiktionary entry, the Latin section presents three proposed origins:

1. **From Ancient Greek**: "αἴθριον" (aíthrion, "under the sky, open"), derived from "αἰθήρ" (aithḗr, "clear sky, heaven")

2. **From Proto-Indo-European via related Latin/Italic words**: Connected to Latin "āter," Umbrian "𐌀𐌕𐌓𐌖" (atru), and Oscan forms, tracing back to "*h₂eh₁tr-yom"

3. **From Etruscan**: "𐌀𐌈𐌓𐌄" (aθre, meaning "atrium, temple, house, domus")

The entry does not explicitly state which origin is preferred, nor does it cite specific scholars like de Vaan or Varro. It presents the possibilities as alternatives using "or" without ranking them hierarchically.
```


## [2026-09-05T05:25:53.163Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86",
 "prompt": "Give the etymology of آذربایجان (Āzarbāyjān): the Middle Persian Ādurbādagān, Old Persian/Greek Atropatene, the personal name Atropates / *Ātṛpāta-, and its meaning ('protected by fire' or similar)."
}
```


## [2026-09-05T05:25:54.441Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/atrocity",
 "prompt": "Give the full etymology of 'atrocity' and 'atrocious', including Latin atrox, ater, and the PIE root cited. Also anything on atrium and Adriatic if present on the page."
}
```


### [2026-09-05T05:25:59.186Z] TOOL RESULT

```
# Etymology of آذربایجان (Āzarbāyjān)

The term derives from Old Persian *Ātr̥pātah* (Āturpat), meaning "protected by fire." This personal name refers to Atropates, a historical figure associated with the ancient region of Atropatene in northwestern Iran.

The name evolved through several linguistic stages:

- **Old Persian**: *Ātr̥pātah* 
- **Middle Persian**: ʾtwrpʾtkʾn (ādurbādagān)
- **Early New Persian**: آذربایگان/آذربادگان (āḏarbāygān/āḏarbādgān)
- **Classical Persian**: آذربایجان (āzarbāyjān)

The etymology tree traces the components back to Proto-Indo-European roots: *h₂eh₁ter-* ("fire") combined with *peh₂-tó-s* ("protected"), literally describing a place or person "protected by fire." The suffix *-gān* functions as a relational marker in Persian, transforming the personal name into a geographic designation for the region historically ruled by Atropates.
```


### [2026-09-05T05:26:01.653Z] TOOL RESULT

```
# Etymology of Atrocity and Atrocious

## Atrocity
The word emerged in the 1530s meaning "enormous wickedness," deriving from French *atrocité* or Latin *atrocitatem*. The term originates from Latin *atrox* ("fierce, cruel, frightful"), which combines two Proto-Indo-European roots: *\*ater-* meaning "fire" and *\*okw-* meaning "to see." This combination yields the sense of "of fiery or threatening appearance." The meaning shifted to "atrocious deed" by 1793.

## Atrocious
Appearing in the 1660s, this adjective means "heinous, extremely criminal, enormously cruel." It derives from the Latin stem *atrox* combined with the suffix *-ous*. A weakened colloquial sense denoting "very bad" developed by the late 19th century.

## Latin atrox
This Latin adjective meaning "fierce, savage, cruel" provides the etymological foundation for both terms above.

## Latin ater
Related to *atrox*, this Latin word means "black," literally "blackened by fire," connecting to the fire-related root.

## PIE Roots
The *\*ater-* root ("fire") and *\*okw-* root ("to see") combine to form the original concept.

**Note:** The page contains no information about atrium or Adriatic.
```


## [2026-09-05T05:26:14.165Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT_v1_pages page tags near start ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -20\necho \"=== grep آتش in BQT_v1 head ===\"; grep -n \"آتش\" BQT_v1_pages.txt | head -5",
 "description": "Inspect Borhan vol1 OCR"
}
```


### [2026-09-05T05:26:14.295Z] TOOL RESULT

```
=== BQT_v1_pages page tags near start ===
=== grep آتش in BQT_v1 head ===
1154:دیدمر | گر فته‌لب» آتش‌بارسی‌زتب ‏ نطق‌من آب تازیان‌برده بنکته دری.
2967:صباخی درجواب فصیدث حالف دذ کر آتشکده: صباحی».مقدمه نود ودو
3068:وایشان دوحکیم بودند دریونان» واو کتابی دردین آتش‌برستی بنام‌بدرخود
3073:کرده‌است دراحکام آتش‌پرستی و آن‌را قسطای لوقا گو بند.»
4155:۱ آتش برزین ؛ آتش باره " آنشکده ۰ آنشگاه »
```


## [2026-09-05T05:26:15.756Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/atrium",
 "prompt": "Give the full etymology of 'atrium' as stated: Latin atrium, the proposed derivations (from ater 'black' / smoke-blackened room, or Etruscan), and the PIE root cited."
}
```


### [2026-09-05T05:26:22.474Z] TOOL RESULT

```
# Etymology of Atrium

**Latin Origin:**
From Latin *atrium*, meaning "central court or first main room of a house, room which contains the hearth," derived from Proto-Italic *\*atro-*, possibly Etruscan in origin.

**Proposed Derivations:**

The primary theory connects the word to a PIE root related to fire. Watkins proposes the root *\*ater-* "fire," suggesting the atrium was a "place where smoke from the hearth escapes" through a roof opening. However, de Vaan finds this unconvincing since "soot is black, but not the fire itself."

De Vaan instead favors the PIE root *\*hert-r-* "fireplace," with cognates in Old Irish *aith*, Welsh *odyn* "furnace, oven," and Avestan *atarš* "fire."

**Scholarly Consensus:**
As noted in the source, "The appurtenance of atrium depends on the interpretation that this room originally contained the fireplace. This etymology was already current in ancient times, but there is no independent evidence for it. Still, there is no good alternative."

The anatomical sense (heart chambers) appeared by 1870, while the architectural meaning of "sky-lit central court in a public building" emerged by 1967.
```


## [2026-09-05T05:26:27.950Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('MON'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('SOD'),ensure_ascii=False,indent=1))\n\"",
 "description": "BQT/MON/SOD details"
}
```


### [2026-09-05T05:26:29.911Z] TOOL RESULT

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
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
```


## [2026-09-05T05:26:36.691Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '278' in p and 'ashes' in p:\n        print(\"leaf\",i,\"printed~\",i-66)\n        print(p[:1500]); break\nEOF",
 "description": "Find SOD leaf for entry 278"
}
```


## [2026-09-05T05:26:38.429Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"leaves\",len(t))\nfor i in range(218,232):\n    print(\"==== leaf\",i,\"====\")\n    print(t[i][:900])\nEOF",
 "description": "Print Borhan vol1 leaves near p.13"
}
```


### [2026-09-05T05:26:38.573Z] TOOL RESULT

```
leaf 76 printed~ 10
                                                                                                                                   »trh




     11


      264 "st'nyh *± 'st'n'yh                                      282 »s8scyy => »58yscyy

      265 »stnly B                                       ^*a       283 "sSyscyy M                                   *U ^a jjj
          astanc ? ('stny(y))                                          as-5isci (*s5scyy) =>5scy(y)
           permanent                                                    eighth day of the month
           GMS 969; "surely", VJ 231; TSP 6.155; S W,                   Hen. JRAS 1945, 151.15 n pl52

             BSOAS     1983, 42, "original"                        284 "sych »ph S                               JjJ^J^Ji
     266 "stn'yh =» »st»n>yh                                            asaxc-ap ? ©f. adj. ^'sync-, *>syt-
                                                                        waterfalls, flowing water
     267 "stn'yk     B                        oU^,;,.rtl^;ijL:L
         astanik                                                        TSP 3.126 n p!96; Hen. Texts. 726; GMS 600,
                                                                          634
          permanent
          TSP 2.1184,6.93, 155                                     285 *Msyt-                                             jjlSV

     268 "stny'kCh) S                           piar^jUUoU              asayd   ©pt. st. =»*sync-,
```


### [2026-09-05T05:26:40.231Z] TOOL RESULT

```
leaves 777
==== leaf 218 ====
آب صفت بودن - کنابه از یار
بفم و فایده رسانیدن باشد - و بالقواضم بودن‌را
نیز گویند.
آب طبرستان - بکسر ثاك »
چشمه‌است روان در کوهی که اکر بانگه , برآن
ود ند و چون فربادکنند پنهان خودوچون
طلب نمایند روان گزدد ؛ و این حنال هر هر
سای از آن چشمه مکرد بفعل میآید .
چشمه‌ایت که مدت هفت سال بیوستهروان‌باشد
و هفت سال دیگر خشك نود .
شراب انگوری باشد .
۲ ب‌عشر ت - بکس الك و عبن می
شمه » بىمنی آب طربست که شراب انگوری
باشد
! شت س بفتح ثالث بر وزن وارفت »
حخفف آبافت است که بارچه گنده و سطبر
باشد ۷ .-
آب سر ۵۵ - بکس تاك , کنایه‌از
-شنشی ی وخنجر باشد و شیشه و پلور و آبگینه
را نیز کویند .
] ها هد بت تالث بر وزن اوك ۰ مکی
از نلبهای سیماب است و آنرا آب و آیق
سس ۰ ۷..--
و ابوالارواح و اصل و االاجاد و پرنده و ده
و تیر وناقة (۱) وجوهر وجیوه و حل‌النهب(۷)
وحی‌الماء و روح و روحانی و رجراج و زارق(۳)
و ژموم (4) و ژبوه و ستاره و سحاب و نور (۵)
و سیماپ و طبار و عبد و عطارد و عین الحیوان
و غبیط وغیان وفرار و گریزنده 
==== leaf 219 ====
ات
آآب کبوث- بکس ات ؛ دربای‌چین
را کوید.و آن را جریی محر اخضر خوانشد .
گویند هو شب زنان خوب صورت از آن دربا
برمی‌آیند و پر دامن کوهی که کنار آن درب
واقع است بازی میکنند و چون روز میشود باز
بدربا فرو میروند ٩‏ .
تب گر ك فاه ه بکس ثالث » کنابه
آسمان است .
]یب .گشاده « یکی ثالث ۰ کنابه از
شراب زبون. و کم کیف باشد .
آب هه » پنکون ثالك و ضم کاف
و قتح میم ۰ کویند آبی است خاکستری ردکه
و بغایت کنده و بدبوی و آنرا از شکم نوعی
از ماهی گیرند که در بحو چین ی باشد . هر
عنوی که بشکند مقدار حو متقال از آن‌بخورند
چنانکه (۱) بدندانها نرسد آن عضو شکسته را
درست کند ودر دربای هرموز(۲) نیز هم حیرسد
و سربی ماوالسه خوانند .
۲ بکند بفتح رایع و سکون خونبودالٍ
ابجد , زمینی را کویند. که آب آترا کنده
و آب انبلر را نیز گویند - وتلم شهری ومدینه‌ای
_ ۱
! بگون ؟. بر وزن وا کون » » نام
رودخانة نمی أست ت که از خوارزم عی آید
۲ بدربای گیلان قرو حی رود - و یمی نشاسته
هم هست و آن چیزی باشد که ار گندم سازند,
ارو 0 کاغذ از آن 
==== leaf 220 ====
نواحی باشند از دنبال شخصي که آب میبرد روان
شوند تا بهرجا که ملخم آمده باشد آن سارها
تام آن ملخها را بکشند و پراکنده سازندوآن
چشمه را چشمةٌ سار هم میگوشد .
آب مر وار یف «- کنایه از روشنی
و روتق مروارید باشد - و نام علتی جم‌هست که
در چشم آدمی )۱( بیدا میشود .
آب هریم - بکس ثالك » جایوسلاح
حترت (۲) مریم مادر عنمی علیهاللام (۳) را
کوه شدب وکنابه آزشیر #ادگوروشرا اب‌انگوری(4)
ی
] ب‌هنجهد » پکتر تاكث , کنابه از
تیخ و شمشبر و خنجر وامثال آن باشد س و کتابه
از شيثه و آبگینه و بلور هم حست - و بخ
و تگرك را یز کویند .
آب هنال - یک ؟الث » بیعنی آب
منجمد است که کنابه از شيشه و آبگینه وبلور-
و یخ و نگ رکه - و نی و خنجر باشد .
آآب ام ه یکس #الت و نون بالف
کشیده و برای قرشت زده » کنابه از شراب
باشد ٩‏ .
آب نافع - بکسر الث وفا » کنابه
از شراب انگوری باشد .
اب ثتخوردن « کنابه از درنگه با
کردن و توقف تمودق پلشد ۰ _ ۱
آ نوس - بس وزن خاکبوی درختی
باشد سیاه ۴ و مشهور است و آنرا سربی نیز
آبنوی خوانند . اکر بر آ
==== leaf 221 ====
0
آش
تلم رودخانه ایست که آنرا رودخانة آهو ٩‏ فیز
میگویشد .
آي - کیش کون ما
آنچه در آب ممیشت کند - و آنچه موب
باب باشد - و نام رنگی است حشهور - و للم
هیوه ای است که آنرابهی (۱) سفرجل
خوانند؟ گویندا گرزن‌خامله
بخورد فرزندش خوشخوی )۱(
کردد - و نومی از انکوز حم
هت .
آ لیااد - بر وزن بادگار ۰ خی را
گوند که زراعت را آب میدهد .
(۱) چش : به .
هه ساب
مه ترديك دربا رسید
بوسئا درون نام او آبهی
آ لك » پروژن هید ء خراره وسرشاه
آش ( ۳ ) را گوبند - و در دژبد القنلا بجای
حرف آخر رای قرخث ودرجای دنگی زای فلوسی
و۳ بودند ز بجای(4) حرف ثالث وه ۴
رام اعلم .
آ ین - مرن ین ره ات ۴
۳ ۳
ابجد پس وزن پاکدنن : ضی عامل و نیکوکار
و صاحب گفتار و کرذار دب تيك ز اسخدالسمدا رائیز ۰
گونند ۷ وم پر فرینون هم هت .
آ شش « بکس ات (ه) و سکون‌شین
تقطمدار )٩(‏ ممروفت و عربی نار خوانند #-
(۳) خم ۳ : شرار؛ آش و سرشلك وا .
(٩)خم‏ ۲ : قرشت .
۹
پر جیحون را ابرانیان در قرون وسطی ۶ به رود *مینامیدند و این اسم » صفت اوستالی ونگوهی
نت۷۵8 
==== leaf 222 ====
۱ آخن آب پرود ۱ ۱ اه
کیره راگونند ؛ یمنی حرچی ز که بدان آش
افروزند همچو خس و خاشالك-و مانند آن - و
چتماق را نز کفتداند . #
]آتش پادسی (۲)- ه پکس رایع »
مرضی است غبر آنفك مشهور آنرا بعربی تلر
فارسی خوانند ا بسن کوند آتك فرنگ (۳)
ات و بسض ( 4 ) دیگر گویند جوششی است
بیار سوزان و حردنالك » و رنگه آن بزردی ماپل
انت و صاحب این مرض بیشتر اوقات با حرارت
و تب میباشد و علاج آنرا بچیزهای سرد بایدکرد
و آنرأ باد فرنگگ میگویند ۴ 3
نش بحان - و ده موزل
و شوق و مت باشد . *
[ ش هر ] هب - بکس رابع . کنابه از
شراب لعلی انگوری باشد - واشك چشم غمزد گانرا
نیز گویند - و یال طلا - و پیالٌ لعل و باقوت
پر از شراب را هم میگویند .
آ تش. بر گه «بنتح با و سکون را
و بمسی فوز و رواج و بونق - و فطب - وسبك
رونعی - و قدر و حرابه - و گرانن درخ حم
کتداد - وکتابه از شیطان است ٩‏ - وکتابه
از مردم شجاع از دلیر بلشد - و شخص عاشق -
و گرمی و حبت عدق را یز گویند - و اهل
مت و ( ۱) کیمیا کوکرد احمر را آش
خوانند - و قوت حاضه. و اشتها 
==== leaf 223 ====
وا ثِ آ دامن
وکاف ۰ بمننی آش زده اس ت که چنساق‌باشد . * ] نش آر « بفتح ی فرشت »کنابه از
آ آش پر ود بتح بای ظرسی و راو | شراب لعلی باشد - و لب ممشوق را نیز گویشد .
و سکون رای فرشت » کنامه از تسغ و شمشیر آتشی تو به سود کنابه از شراب.
آبدار است انگوری ماشد . **
آتش بسته کنابه از زر سرخ و طلای ] شش <حر ‏ بنتسمای بی‌شطه, کنابه
احمی باشد . - از لمل و با قوت باشد .
آ تش بهاد - یکس رایع ,کنانه از . ] تش خاطر - بسکون رابب ۱
کل مرخ و لاله باشد - و رواج و رونق بهار را کنابه از مردم عاشق ییشه باشد - وک یکه
نیز کوبند . * سنغنان عاشقانهٌ پر سوز از اوسرزند + ومردم تیز
آتش نی باك کنابه زشراب‌انگوری فهم و روشن رای را تیز
اش - وغل دی را یز گید . قش خواد - نم رات چم رنه
۲ نش لی دود - کنابه ازآ فقاب‌است_ | از مردم بدفی و ظالم باشد ‏ ومدم حرام‌خوار(۱)
وکتابه از قهر و نتب هم حسث - وشراب لملی و رشوت‌خوار (۲) را لیز گویند .
را لیز گویند . ۲ تش خواده - بنمنی آتشخوار است
آ قش ی ز با 4 -کناب از شراب | که نام مرغی 
==== leaf 224 ====
آش محقان
۰ ۲ تش ذهقان ه بکر رابم » آنثی
را کوبند که دهفان بد از دروکردن و پرداشتن
غله بر بغية آن زشد * زمین قوته‌گیرد و نود
م‌ رسائد .
۱ آتش‌رد بکر رایع د شتح رای
فرشت: » کنابه از شراب انگوری ,اشد .
"تشد وذ -کنایه از آقاب عالمناب
است. - و گرما و روشنی روز را (۱) کونند . *
از یز و ند بان باشد نی شخصی که ند وجلد
عری و 2 "
4 7 زر
تعلقات نمودن باشد - و کی را برسر غضبآوردن
- و بمعنی. بیقرار و گرم ساختن (۷) هم هست .
] نش ده « بکر رابم و فتح زای
. هوز و.سکون رای فرشت ؛ کنابه از رواح د رولق
پاشل . ,
۱ آتش هزم -کنب تباب
به.۰
تخاق پاشد و پبری زه کرین ۰
آ شش ستن « بسکون رابع . کنابه
از طمنه زننده و عتاب کننده باشد .
آ تش سر د بفتح مین بی‌هطه .کنابه
دوائی وآنرا بتازی بنضج‌الکلاب خوانند .
(۱) مك : + نز .
0
و فکر و خیال باشد . ۱ مه 0
" آتش سیال ِ ناب ری
۳ 9 وی ۳ 2
۷ ی
آش زر است که کنابه انگوری! باشد .
.]وی صبح من صاد بی‌هطه ء کتانه
از آغّاب عالمتاب باشد . *
آنش 9 اد » هبو ازء است»
آکش فروذ -ب بسن آش ا
==== leaf 225 ====
و مطیخی و آهنگر و امثال آنرایز کوند . *
۲ تشکدة بهر ام - کنایه از برج
حمل باشد بواسطةٌ آنکه حمل خانة صویخ
است ٩‏ #۶
] تشگیره - هرچیز که بدان آتش توان
بر‌داشت - و آنچه بدان آتش افروزند.
اش اس تبگه ۳ ۰ کتابه از
سرخ پوش باشد .
آ آش‌هچم -کابه از یغ سیر
آبدار و سایر اسلحد جتگه باشد .
] شش تشاد - یک نون . کنامه آزمردم
گربان و غمزده باشد .
۲ نش فشا ندن کنابه از فرونانیدن
آ تش و آب ‌ کنابه از نیغ و شمشیر
و امثال آن باشد - و یال بلوری پر از شراب
انگوری را فبز گوبند .
۲ نی هفت محمره » کنابه از
سبعهٌ ساره است که زحل ومشتری ومربخ و آ فتاب
و زهره و عطارد و ماه باشد . ۶
پا ی و ات ی
باشد . 3
] تشیز ۲۵ بازای هوزیی‌وزن‌با کشنده.
کرم « شب تاب را گونند و آن جانورست هر نده
و روشن . *#
۲ تشهن ارٌْذها - کنابه از حريك از
٩ب‏ از من اک هام1 است . راك
( ابسمك )علامت صفیر .
۰ ۲ تشکده ‏ مرکب از
هقی او
مر‌کب‌ا زکد ۲ هاء نسست‌است
که از رشة کته 6842 اوستائی -
و آن نیز از عصدرکن 120 1 ۷
بمعن ی کندن مشتق است ؛ وآن
ی زرت
==== leaf 226 ====
کویند . ۱ 1
| تین پنجه - بتح بای فارسی »
کاریکر (۱) و لستاد جلدکار وتند وئیز را گویند.
و آن را آاش دست یز کوبند .
] قشان دواج - بنتم.دال ابجد.
کتایه از آفتاب است - و شفق را نیز کوبند - و
کنابه از شراب لملی هم هست .
شین دبا - بت زای له دار,
و تتف و ئیز حرف زند .
ان بح ی سار و ی
قله . کنابه از خورشد عالم آراست
! تفن شون یت تم سار بر نقطه ,
بکرم ,کتابه از آفتاب تابااست .
است - و کسی را نیز کوبند که لبای سرخ پوشینه
علشث -
] قشین‌هاد « با میم با الف کنیده و
لفت کارگی .
یی کی 3 دبع باشد . و زمالةً
ش را ی
است که تبر حوائی باشد .
آ قل هکس تالث بر ون ساحل » تام
رودخانه‌ایست بسار بز رکه . ابتدای آن از بلاد
روی و بلفار است و امهای آن بحر خز رکه دربای
کیان باشد .کوبند ریب بهتا نهر ان جدا
میشو که از هی چکدام آن اسب بآسانی قواند
گذشت ۱ .
]تون - بر وزن خاتون , زنی باشد که
دخثرانرا تعلیم چیزی خواندن وتعلیم نوشتن ونقش
دوختن دهد ۴ - ویجه دان وزهدان را نیز کوبند
و بعربی هشیمه خوانند -
]ین - بر وزن لاچین . 
==== leaf 227 ====
عمل کردن ویبروی تىودن ناحکام شرمعت باشد .
] چالك - با جیم فارسی بر وزن ابا .
بمعنی خال باشد و بعربی ترآب خوانند .
] چاه - بفتح‌جیم بروژن آعده , بعطی
کرد اد وی شید دز و
و یر سوزن هم هست ِ#
آجل -: سوت 6۳ + ارم
آمد- و قتح تالث عم کفته اند - و بکسر تال
۳
آ چنگان - با کاف فارسی بر وزن آدم
خوان . نلم فربه ات از قرای سرخس که
ست ,۲ *
آ خ -بر وزن شاخ ,کلم نصین است
بمعنی آفرین و جاركايهٌ -
[ ال - بروزن‌پامال . چیززهای افکندنی
و بکار و -سقط باشد مانند پوست یره ها وتراشة
چوب و خس و خاشاك و خاکروبه و امنال آن .
و آن را بعربی حش و گوبند . و باين معنی بجای
حرف تال قاف هم آمده است - و نام شهری
و مدیته‌ای هم هت . ۱
آختن ۴- بروزن‌ساختن؛ بمعتی‌بی کشیدن .
آخر سشگین
باشد - و پرآوزدن تیغ را یز گویند لز غلاف -
کشینه باشد خواه تبغ خواء غبر یخ » و باین
معنی با همه مفتوح نیز آمده است .
آ خر - ۴ بنم ثالك وسکون رای ی
قطد . جای علف خوردن اسبان را گوشد و
استخوان (۲) را نیز گفته‌اندکسه در زمر کردن
وبالای سینه میباشد و
==== leaf 228 ====
که در آن حاسلی ونفعی لبوده باشد ٩‏ .
۲ خر لك » بر وزن ناخنك » استخوانی
را گونند که در زب کردن و بالای سینه میباشد
و اترا بمربی ترفوه خوانند ۴ .
خر بان - بسکون الك و تحتالی‌بالف
کنبده بروزن شاه ندان . ی
نم سین بی‌هطه و فتح هیم
بروزن صاف شده » بوزه را.گوشد و 0
باشد که ازآرد برفج با آرد جو یا آرزن و امتال
آن سازند. وبفتح سین هم آهده ق
] خش » بنتم الث بروزن آش
قیمت و بهای چیز ها را کویند ۴ - و بسکون
ی 4
تاث نام موبدیاست پارسی‌نژاد که او ماه عناص
دا پرورد کار شناسد ۵ .
هه ه بروزن و معنی آخسمه است
که بوزه باشد . چه در فارسی بین بی نقطه
و تقطفدار بهم تشدیل مي‌بابند .
آ خشیج « بکس رابع وسکون تعتانی
و جیم . بمعنی نقیض و ضد و مخالف باشد -
و حريك از عناصی اربعه (۲) را نیز گوشد باعتبار
ضدیت . و بعضی کوبند آخشیج معرب آخشگه
با کاف فارسی است
] خشیحجان - با الف و دون . جمیع
آخشیج است بعني ضدان و نقیضان و مخالفان -
و عنامی اریعه (۷) را نیز گویند که خاله و آب
و .هوا و آتش باشد بهمی اعتبار .
(۱) چپ ۷ , چش 
==== leaf 229 ====
] خشیگه ه با کان فارسی » بی وزن
ومعنی آخشیج است ت ۱ که نفض ومخالف - وطر
ءكث از عناصر ار بعه باشف» جح آن آخشیگان
ود .
| حمسه - با میم و سین بی لفطه » بر
وتان ام ]تیه ست که بوزه باشد .
ورای فرشت . جای علف خوردن دواب را گویند
ومربی معلف خوانند » وبی واو نیز درست است
چثانکه (۱) گذشت ۲ .
| خو دسا لاد ع می رآخورء(۲) وسلار
و دش سفید طویله را گویند .
۲ خو دك - با واو معدوله بی وزن
وبالای‌سینه واقماست » وبمربی ترفو‌خوانند ۴ . #۶
]داش - بروزن پاداش » در شخ صکه
يك نام داشته باشند هر يكك مر دمگریرا آداش
۳ و گویند این لفط هر کوع لسنت ت سکن در
آ دا لگ بروزن خاشاك , خشکیوجز برة
میان دریا را گویشد .
(۱) چك » چب ۲ : چنانجه .
۱ _ رك : آخشیج .
سمی ۶ قاموس اللغة العتمانه » .
7 ۵خ « بفتحتاك وسکون خای نقطهدار,
خوب و نیکو و نفز را گویند - و بععتی بلندی
ح‌ ۹۳ امنت اه
]ده ختح ثالث بر وزن عادر » بمهئی
آثر است که آتش باشد ۵ -وبکسرثالث نشتر فصاد
و رک زن راگونند .
و صاعقه و رعد و برق ماشد .
]۵۵ بروزن چارخم » نمدزین 
==== leaf 230 ====
آده
| ده » بر وزن جاده » دو چوب بلندی
اس ت که در زمین فرو برند و چوب دیگر بعرض
برلای آن دوچوب بندند نا کبوتران و جانوران
فان حتف
| دیش ۱ ۰ بکس نات وسکون تحتانی
و شین نقطمدار ء آش راکوند : ببابددانت که
با برآن تای آتش را بدال ابجد بدلکرده آدش
کفته‌اند و اینکه قح تای قرشت اشنهار دارد
غلط حشهور است چه این لفت در همه فرهشگها
کر تای فرشت آمده است وبا داش فافه شده
است و چون بکسر تا موضوع است ت بنابراین جد
از دال بای حطی در آورده‌اند تا دلالت بر کسره
ما قبل کند و آدیش خوانده شود ؛ و بسنی بکسر
ذال قطمدار آورده‌اند و اين نا غلط است چه
اکر دال اسلی مي‌بود بنا بر قاعدءكلة ایشا که
حردال که ما قبل آن الف و با واو ساکن باشد
نال ممجم است درست بود و چون این دال اصلی
تبت بلکه مدل از ای قسرشت است یس ذال
قطمدار نباشد .
] دینله » بتتح تحانی و دال بجد و
سکون ات و نون : فوی و قزح را کوند .
آ دا عا نان خظهدال پروون زار
در برج حوت ۰
وسکون فا و واو و نون » نوعی از زیدالبحراست
آذ ار عطوس - ایکون
7 بودیه ۴ .
]اد *
==== leaf 231 ====
رنه
حهای نی وآن بودن آفتاب‌است در برج فوی
- و نام روز نهم باشد از هر ماه شسی و بموجب
رسم یکه میان فارسیان مقرر است که چون نام
روز با نام ماه موافق آید آنروز را عید گیرند
و آش خانها را بروبند و مزین کردانند » و در
این روز نيك است ناخن چیدن و موی ستردن »
بش خانه رن ٩‏ - وکنابه از عشق هرت .
آذر ] با۵ س نام آتشکده تبربز است
و معنی ت رکیبی آن معمور؛ آش باشد چه آند
اک است و آباد حمموره را گوبند - و دام شهر
ریز چم مت ۰۲
] ذم ) باد گان» با کاف فارسی بالف
کشیده و بنون زده ۰ لام شهر تبریز ۴ - و نام
آتفکده فبریز است ؟. کونند چوت در برچ
آتشکده بسیار بوده است ت بنابر آن بدین نام حوسوم
شفه است
) دّد | بات گون ‏ بسکون وار رنون,
آش گاه ۵ و کلشن حمام - وکور؛ آهنگری
۰ وامثال ]را گویند ۸ -
آذربلد
1 نو ع بکربای حطی و سکون
تحثالی ولون » نام آتشکدء چهارم ۷ است. گویند
که عجماترا حفت آتشکد2 نامی بوده بمدد حفت
کوکب و آنها اين است
نوش ۳ - آنر بهرام ؛ - آنرآین ه ‏ آنرخرین
آتر زردهشت ؛ و هر يك
از آن آتشکده هارا متس
```


## [2026-09-05T05:27:02.495Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(215,240):\n    lat=[l for l in t[i].split('\\n') if re.search(r'[A-Za-z]{3,}',l)]\n    if lat:\n        print(\"=== leaf\",i,\"(printed ~\",i-210,\") ===\")\n        for l in lat: print(\"   \",l.strip()[:300])\nEOF",
 "description": "Find Latin-script footnotes in Borhan leaves"
}
```


### [2026-09-05T05:27:04.098Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:27:11.271Z] TOOL CALL #38: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:13 --image 2>&1 | head -60",
 "description": "Render Borhan page 13"
}
```


### [2026-09-05T05:27:12.766Z] TOOL RESULT

```
no scan of BQT covers printed page 13 (see 'scans' in refs_online.json)
```


## [2026-09-05T05:27:25.390Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (221,222,223):\n    print(\"############ leaf\",i,\"printed~\",i-210)\n    print(t[i][850:])\nEOF",
 "description": "Print tails of Borhan leaves 221-223"
}
```


### [2026-09-05T05:27:27.858Z] TOOL RESULT

```
############ leaf 221 printed~ 11
د *مینامیدند و این اسم » صفت اوستالی ونگوهی
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
هه درصفحه 4 ۱2 دب
############ leaf 222 printed~ 12
میا کوکرد احمر را آش
خوانند - و قوت حاضه. و اشتها را گویند.
آ تش آب پرود - بکس رابع .
کنابه لز شمغیر و تیغ ۲ آپدار باشد . .
آتش افر اه - ری بود از آیی
که برهوا رود و آن را ثبر هواگی نیز گویند .
آ آنش افر وف ظرفیباند هیأت کة
آدمی و سوراخ تنگی دارد . چون آن را کرم
کلند. و میان آب فرویرند آبرا بخو دکشد » و
چون بکنارآش‌نا افروخته گذارند چون کرم شود
بخاری ازآن سوراخب رآش‌وزد وا ش‌برافروزند ۰
و اين ا مخترعات جالینوی‌است - وسوخته وهر
چیزی که بدان آش افروزند - و نام ماه بازدهم
است از سالهای ملکی ۴ بزدجردی - وتلم مرغی
هم هست که آنرا برومی ققنی ۴ خوانند .
(۱) چك: - و. تفن ۱ (۳) چش : فرنگی . (4) چش : بسنی.
۱ - اثاره بخلقت ابلیس از آنتن-ب< سوره ۷ ( اعراف ) یه ۰.0۱۱ ۴ - مراد سال
جلالی است ت که بامی ملکشاه سلجوقی در سنة 4۷۱ قمری ترتیب دادن «گاه شماری ۱۸۷ *.
۴ - ره : قفنس . .۴ یز آتشکده فاری با آذر فرلبغ + مزدسنا ۲۲۲ - 6۲۷۳ - تبخال .
< لفت‌نامه > . ۱
۵ آتشان - پهلوی طألاأکقاك بمعنی آتشکده - آنشکد؛ بهرام « تاوادبا ۱۵۹ >.
۵ آقشیبرزیی - رك: آندبرزین  .‏ 5 آلش پاره - اخگرکرم شب‌تاب - مجازاً مخت جانی
و متمکار . < لفت للبه *. .
خه از صفحهٌ ۱۳
۶ منای۲۹۸ ». در پارسی‌آذر » آدر ۰ آتش » آدش, ش,آتیش ( عامیانه) ازهمین ربشه است .
دمزدیسنا ۱۷۷ ۰۴ درکیلکی قفا . فریزندی و بیریی. و طنزی طفقناة « . اس 4د۷»
سمنانی ۰80851 مبنکری 2400 رنافقاة . سرخة 58اه . لاسکردی «اعقا2 . شهمیرزادی
40 < ۵ .۲ س ۱۸۰ و ۱۷۹۰ * » اشکاشکمی و وخی 116 ( برق ) «کربرسن ۷۳ ۰
رگ : آذر .
############ leaf 223 printed~ 13
وار است
آ قش ی ز با 4 -کناب از شراب | که نام مرغی ۴ - ومردم بدشی وظالم و رشوت
انگوری باشد - وکنابه از لط و باقوت و عقیق | خواره باشد .
هت . * [ دادن -کنابه ازتراد دادن وتراد
آ نش لیکر - بننم بای فارسی . کنابه
از فتاب عالمتاب است - و شیاطین و جن را یز
گومته .
کردن باشد مطلقا - وکی را پرسر فهر وغنب
آوردن - و بمسنی شخصی را یقوار حاختن هم
سصت . 4
۱ کش خاطر . اضافةٌ تشبیهی (مشبه‌بهبمشبه) است بعنی فرمعت آتش‌مانند ونندوئیز :
چون آتش خاطر مرا شاه بدید از خا مرا برزبر ماه کشید.. «معزی۸۱۱*
؟ - شترمرغ ۰ ممامه , < لغت‌نامه * . 3
آنش پرست . کسیکه آتنرا نقدی سکند - مسلمانان زونفتیان را مظ بتفدییس آش»
آش پرمت و آئرپرست گفته اید :
بيك هفته بر پیش بزدان بدلد مپندار کاش پرستان بدند
که آت بدانگاه محراب بود پرستنده را دیده پر آب بود .
فردوسی « مزدیسنا ۱۸4 - 6۱۸۷
4 آتش بهرام - باآنرهرام , آشکد‌های بزرکه را پارسیان آش‌بهرام نامند ودربرابر
آن « آذران » با « آدران » با < آ گیاری » با نشکده ها یکوچك اطلاق میشود - دو بمبئی سه
آت‌بهرام و درحدود سد ٩‏ گیاری است . «مزدسنا ۲۳۳* .۰ آتش بهرام لباهش - یکی ازدماز
های‌پنجگانةٌ خرده اوستا . ۵ آقش‌پا - مجازاً نندری. روان. ۵ آقش‌چرخان - رك :آت شگردان.
‌ 7 تشخها ه - معا یکه درآن آش افروزند . آتشکنه , آنشگاء .
‌ آلش دان - در پیلوی 40 - عها۵ ؛ کانون » منقل ‏
```


## [2026-09-05T05:28:10.805Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (231,232,233):\n    print(\"############ leaf\",i,\"printed~\",i-210)\n    print(t[i])\nEOF",
 "description": "Print Borhan leaves 231-233 for Azerbaijan"
}
```


### [2026-09-05T05:28:12.360Z] TOOL RESULT

```
############ leaf 231 printed~ 21
رنه
حهای نی وآن بودن آفتاب‌است در برج فوی
- و نام روز نهم باشد از هر ماه شسی و بموجب
رسم یکه میان فارسیان مقرر است که چون نام
روز با نام ماه موافق آید آنروز را عید گیرند
و آش خانها را بروبند و مزین کردانند » و در
این روز نيك است ناخن چیدن و موی ستردن »
بش خانه رن ٩‏ - وکنابه از عشق هرت .
آذر ] با۵ س نام آتشکده تبربز است
و معنی ت رکیبی آن معمور؛ آش باشد چه آند
اک است و آباد حمموره را گوبند - و دام شهر
ریز چم مت ۰۲
] ذم ) باد گان» با کاف فارسی بالف
کشیده و بنون زده ۰ لام شهر تبریز ۴ - و نام
آتفکده فبریز است ؟. کونند چوت در برچ
آتشکده بسیار بوده است ت بنابر آن بدین نام حوسوم
شفه است
) دّد | بات گون ‏ بسکون وار رنون,
آش گاه ۵ و کلشن حمام - وکور؛ آهنگری
۰ وامثال ]را گویند ۸ -
آذربلد
1 نو ع بکربای حطی و سکون
تحثالی ولون » نام آتشکدء چهارم ۷ است. گویند
که عجماترا حفت آتشکد2 نامی بوده بمدد حفت
کوکب و آنها اين است
نوش ۳ - آنر بهرام ؛ - آنرآین ه ‏ آنرخرین
آتر زردهشت ؛ و هر يك
از آن آتشکده هارا متسوب ببکی ا زکواک (۱)
سیعه میداشته‌اند و بخوری که متعلق بان کو کب
بوده می‌سوخته‌اند ۵ .
[ذر افر ور بمعئی رد است
و آن ظرفی بائد میان خالی بهیأت کل آدمی
وسوراخ‌تنگی دارد ؛ چون آنرا کرم کنند ومیان
آب فرو برند آبرا بخودکشد و چون بر کار
آچه تش نهند بخاری از آن‌برآیدکه آتس افروخته
کت 0
نف 2
۲ ذد از ) ه بازای ششمدار بالف کشید
بمعنی آند افروز است که آتش افروز باشد وآن
از مخترمات جالینوی است اف
] 3 بأث » بابایابجیالفکشیده وسال
زده ء نامییکی از موبدان‌وداشمندانوده‌است *۷ -
۳-۱ ۱
(۱) - چك » چش : ک وکب .
٩‏ - رك : روز شماری ص۷۸ ۴
از «آنرویات» نام سردار و خشثرپاون (شهربان) آنربایجان است (رله : آنربایگان) و بدیهی لست
آشکدهحائ یکه در آن حوزه‌بوده بدین تلم تخصص‌نداشته است‌بلکه من‌بلب تمه حال باسم محل
مدا شده ت۱9 ۳ ز بست » بلکه للم فلحیتی است که
۵ موجرن خی *م فام تبریز یست ۰ ؛ وسیم
بیکماه در نا باد ان بودلد شاهان وآزادکان . فردوسی
۴ اشتباه است . وگ : آنرآماد ۰ یج رك : آذرآبادکان ۹ شاهدی مرای این
معانی نیست 00۱9۵ ۱ ۱ 900
راب منسوب پدر فربدون نوشته‌اند «مزدبنا ۷۳۷ . . ۸ رگ : حردی‌نا ۲۳۷-۷۳۱
٩‏ رك : آش اقروز . ۰ ٩‏ - اوسنا ۸۱۵۲608/۵ ( بممتی پابنده و نکیبان آش ) عم
یکی از پاکدینان ابران باستان « قروردین پشت بند ۱۰۲ > : پپلوی * ( و چیأت حلی
دیگر ). آتوریات مارسپندان ( آ نریاد مهرسیندان ) یکی از فوبدان بز رکه عصر علسالی است که
وک و ی مج اند که 2 ( آزمایش ریخن روی کداخته پربدن وی ) »
داد رك > زدیا ۱۰۷ - ۱5۹ .
۵ آذران با آدران معععفق. معابد و آتشکده ها یکوچك زرشتیان. «مزدیسنا ۰۷۳۳-۲۳۲
############ leaf 232 printed~ 22
] تربلدگان وت
که تیربز شهر آنولابت است . کوبند وقتشکه
آغور ۵ آنولایت کرفت صحرا و مرغزار اوجان
که یکی از محاژولات آذربایجاست اورا خوش
آمد و فرمود که عر بك از عردم او بك دامن
خاله ماورند و آنجا بریز تف » و خود شفی خود
بك دامن خاك آورد و بربخت . تمامت لشکو
ومردم هریك دامنی خاله ماوردند وبربختند ؛ مشتهُ
عظیمی یت نام آن پشته را آذربایگان کرد
چه آذر بلفت ترکی بمعنی بلند است و بایسگان
۷۳ وهحتعمان ؛ وآ یا را با ان حشهور
آ در باد گان - با کف فارسی باف
کشیده وبنون زده. تام تشکده‌ای بوده کهدرتبریز
بناکرده بودند ٩‏ ومعنی ت رکیبی آن نگهدارنده
و حافظ و خازن آتش بود چه آنر بمنی آتش
و بلدکان بیمتی نگهدارنده و خزانه دار و حفظ
کننده ؟ باشد وهعئی مجازی‌آن آتشخانه است
و حربی بیت‌النار خوانند - و نام شهر تبریز ۴
نو عبت 0۷
] ذر بایگان - با بای حی » بر وزن
و معنی آذربادکان است که آتشکد تبریز -
و نلم شهر تبریز باشد ۵ - و نام ولایتی هم هست ۱ کرداید ۷ و عمرب آن آذوبابجانت ۷.
4-۱ : آذرآبادکان و آذرآمد. ۴ - چنادکهکنته شد *آذرآباد» بمعنی نگهبان
آع است و ه گان » مساوند تست است . ۴- هل اماتی است کة فرط کرسی آفست..
۴ - افوز « کروی . مقالات ج اص ۱۱۹ *- آندبایگان وآذربایجان و آذربادگان؛
عرمه شکل در کتاب های فارسی محروف است . فردوسی آذدآ بادکان حم آورده :
بيك ماه در آنرآبادگان سودند شاهان و آزاد گان
عرب *آذریجان» و «اذرییجان» گومد . در کتابهای ارمني *1نریاباقان» و « آدرباداقان »
هردو آمده . در کتابپای پهلوی ۶ آ نوریانکان » ۸0۳۳212180 است . بقول استرابو 507200
حخرافی نوس بونانی» چون اسکندر مقدوتی برابران دست‌دافت. سرداری‌نام ۶ توریات» (آ خرباد .
رك : همن‌کلمه ) در آذربایگان برخاست و نگذاشت آن سرزم ن که بخشی از ماد و بنام * ماد
کوچك» معروف بود . بدست بونانیان افتد » از آن‌یس سرزمین مزبور تم 1 < توریاتکان»‌خوانده
شد . مردم آ تورپات دا بیادشاهی بر گزبدند و او سرزمین خود را مستفل ساخت . استراب و که کتاب
خود را در زمان پادشاهی اشکانیان (تزديك بتاریخ‌ولادت‌سیح) تألیف کرده ۳ : و هنوزجانشینان
آنوریات هنند و استفلال دارند » وگاعی نیز با بادشاهان ارهنستان و با اشکانیان و با حکمرانان
سوربه خویتی کرده‌اند . » علت‌هاب ی که منفان دور# مفول (از رشیدالدین وزبر و دیگران) برای
یداش این نام ذ کر کرده و بهانه بدست نومند کان ترك داده . جز بك رشته اساته هی بی
سر و بن نمیبانند (رلك : متن برهان) وهمچنین عمنیی که فرهنگه نوسان ابران برای کلم مزبور
بنداشته و علت پیدایش آترا بودن آتشکده ها در آنربایگان توشثه اند ممنی درستی فیست , اما
آخوریانکان م کب است از سه‌کلمه : ۱ - آنور با آذر » - یات با بای (پد) ۳ - کان يا گان .
آتور و آذر بمعنیآتش است و پات ازمسدر پابیدن بمعنی نگهبالی کردن وکان پسوند مکان‌است .
پی معنی‌کلمه بعنی سرزمین با شهر آذرباد . * کسروی . مقالات ج ۱ص ۱۲۲-۱۱۷ و دجوعبه
شه در صفحهً ۷۵
ه آذر ای _ اومتا خن , بهلوی 210۳۳8۳ » نگهبانآ تشه مزدسنا ۰۱۷۷
۶ و ۱*: » ات ۰.1۱ ۱۵۷*.
برهان فاطع ۸)
############ leaf 233 printed~ 23
آآذد بردفی - نام آنشکده ششم
است که در فاری برزین نام , شخصی از خلفای
ابراهيم زردشت ٩‏ ساخته بود » و بحضی کویند
روزی کیخرو سواره می َفت ناگاه صدای
رعدی بهم رسید چنان مهیپ که کیخرو خود را
از اسب انداخت ؛ درآن ائنا صاعقه افتاد وبرزین
اسب او خورد و زین افروخته کردید دیگر
نگذاشتند که آن آش فرو شیند و همانجا
آتشکده ای ساختند و آذربرزین نام کردند ۴ .
]فافع ی دزن تازف خر . کل
اشنان است و آن زرد رنگ میباشد و بونهُ آن
پرخار است و بیخ آن را + کلیم شوی » گونند
رحربی «فلام» خوانند ؛ وبسنی کویندآنربوه بخ
(۱) چب ۲ : سیم
خاری است وگل زردی دارد و شبرازیان فچويكث
ائنان» کوبند ۴ .
] ذد و 4 - ختح بای‌حطی: کل‌اشنان
است ؛ و بعض ی کونند بیخ زعفران است ؛ وبعضی
دیگرگویند بیخ خاری است که شیرازبان چوبك
اثنان خوانند و « بخور مرم » نوعی از آست .
کویند ا کر زنی آبستن نشود فدری ازآن بضود
بر‌گیرد آبستن کردد ۴ .
] در بر ام - تلم آ تشک سوم (۱)
است از جملهٌ هفت آنشکده فارسیان و مجموع
دور ۰آذرآین» کفته شد ۵ . 3
) ذد لیر | » بکر بای فارسی و سکون
ت«تانی و رای بی قطه بالف کشنه , خادم
. ۹۸-۵
بضواه جام و برافروز آند برزین
بکشور نگر تا چه آئبن نهاد . دقیفی
که پرشماعة کافورشدکه‌وبرزن . عمسق
«مزدسنا 4۲۱۹۲۱۵
۵رد : آش هرام .
چو ببروزی شاهتان مشنوید
شه از صفحهٌ ۲۶
کزیتی بانرپرستان دهید . دقیقی
۶ مزدسنا ۱۸۷-۱۸4
«مار کوارت . شهرستانپا ص۲۲و۵۲* و شهرستانهای ابران ترجمهُ ص. هدابت در مجلة مپرسال ۷
۱۷۳ شود . ۴ "- آذربایجان بخشی‌ازماد قدیم است که ازشمال به اران وازجئوب غربی به‌آئود
واز مغرب بارمنستان وازمشرق بدو ابالت مغانو گیلان محدود حیشده, ولی‌ابالت آنربایجان کنونی
محدود است از شمال برود اری و از عفرب بارمنستان و کردستان نرکیه و از جنوب بکردستان
و خسه واز مشرق بکوههای طالش و مغان . ساحت آن ۱۰2۰۶۰ کیلومتر مربم و جمعیت آن
قریب ۰۰۰ ۲۰۰۰ است. * جفرافبای سیاسی . کیهان ۱۵۰یبمد» - در تشکیلات کنونی آنربایجان
بدو قسمت شرقی »کرسی آن تبربز و غرمی .کرسی آن رضائیه (ارمیه) تقسیم شده است . برای
اطلاع ازاوضام فلاحتی واقتصادی, ره : فرهشگه روستاگی ۱۳ بعد
```


## [2026-09-05T05:28:48.540Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN atas/adar ===\"; grep -n -o -i \"âta[sš][^|]\\{0,250\\}\\|ätaš[^|]\\{0,250\\}\\|âdar[^|]\\{0,200\\}\\|ādar[^|]\\{0,200\\}\" HRN.txt | head -10\necho; echo \"=== HRN Feuer ===\"; grep -n -i \"Feuer'\" HRN.txt | head -10\necho; echo \"=== HUB atas ===\"; grep -n -o -i \"ata[sš][^|]\\{0,200\\}\" HUB.txt | head -10\necho; echo \"=== NYB adur ===\"; grep -n -o -i \"[āa]dur[^|]\\{0,150\\}\\|[āa]t[aū][xr][sš][^|]\\{0,150\\}\" NYB_vol2_glossary.txt | head -15",
 "description": "Grep Horn, Hübschmann, Nyberg"
}
```


### [2026-09-05T05:28:50.753Z] TOOL RESULT

```
=== HRN atas/adar ===

=== HRN Feuer ===
559:9. ä(fer *Feuer', ader,
9617:1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',

=== HUB atas ===
838:atasti' wiirde ich *ddast, tnr *abitasti- : *awdast,
1208:atasxani 'Antwort').
1861:atas 4- ayu- Von selbst
1862:atas + adi- Von selbst anfangend,
1883:ataS, sp&ter phi. x^atai, paz. x^adai.- 55 —
4319:atastan, arm. da-
4462:atas (vgl. Horn Nr. 7), afgh. LW. atas, paz.
4463:ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
4672:atasxani *Antwort', ap. *pati8a(h)uvan- ; np. pasaxt
4718:atas;

=== NYB adur ===
690:ātaxš apar ~ 4816; the house pat äsepisn äsift estet is all ablaze 4429-22, _ The sense is clear, and the reading fairly certain; I have no evident etymolo
761:ātaxš [^th$] fire, in the ordinary sense 20? and passim; — in the Zoroastrian creed and cult: personified as the son of Ohur- mazd 311-235, passim; 589.29,
761:ātarš; Paz. NP ātaš (-x- in ātaxš inorganic as in Zartuxšt; an attempt to explain it as purely graphical v. de Menasce, Feux p.43).
1706:ātaxš andar urvar apar grat the fire did not reach, and catch hold of, the plants (the fuel) 4819, with the gl. kit bē nē ūyēt. — MPrth pres. gr’y- (MHC; L
1750:ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is ve
2242:ātaxš ~ generator of fire (i.e. letting loose the fire hidden
2842:ātaxš mänäk aparociónik hesme m hàn i xét like a fire which has to be kindled but is thrown into wet fuel, ibid. 411°]. As it stands, this form can only be
3109:ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand w
3627:ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, mig
3690:ātaxš ~ to roast, to grill 445. — 2. intrans. to shine 1%, 372, — Av. (631sg.) tap-, pres. tāpa-, caus. täpaya-; MPrth t’b’dn tb- ‘to burn, to shine’, Ghil
3912:ātaxš i ~ 203-4, v. Varhrän ; the planet Mars 511, 77. — 2. n. pr. the Sassanid king V. V, son of Yazdékirt I (420—438), 114*. 115?. 11712-18 with the surn
3963:ātaxš Varhran 1139-21; of ātaxš i Karköi 1164; — subst. a man endowed with supernatural power, of Zartuxšt 36%; mart i vazurg x"arrah 4 Yam u an-ic ~ 44°; 
4050:ātaxš paitak rošneh. — V. *vax- šitan.
4106:ātaxš haciš nē šāyet véxtan the fire (hidden in the plant) cannot break forth (from it) 95! (gl.); api-š hösak vest u hošet and its ears having been torn o
4326:ātaxš 92°, with the same ending -é as in menöye, v. meno. — < *xvarka-, cf vastarg, vistarg, vitarg, vazurg, etc. Cf MPrth xwryndg or waryndg.
```


## [2026-09-05T05:28:58.295Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 550-575 ===\"; sed -n '552,572p' HRN.txt\necho; echo \"=== HUB 4455-4470 ===\"; sed -n '4455,4470p' HUB.txt\necho; echo \"=== NYB adur entry ===\"; grep -n -o \"ādur[^0-9]\\{0,300\\}\" NYB_vol2_glossary.txt | head -8",
 "description": "Print Horn/Hübschmann/Nyberg contexts"
}
```


### [2026-09-05T05:28:59.946Z] TOOL RESULT

```
=== HRN 550-575 ===
1*— 4 -
8. üj^xir *Stair.
aw. avöx^'arena- *Stall, Futterplatz' ; phlv. av;(ur oder
avx^'ar (Darmesteter, Et. ir. II, 136), arm. LW. ayor,
vergl. Talmud LW. •imnx (de Lagard e, Semitica
I 42) 'Stallmeister' (arm. LW. axorapet, a/orapan), —
Anders Geldner KZ. 28, 186.
9. ä(fer *Feuer', ader,
ap. vergl. Äd^rina-, Ä&riyädiya- ; aw. äfar- 'Feuer ;
phlv. ätiir (häufig auch auf Gemmen), schon ad^o' ge-
sprochen, vergl. Hörn, Mittigen Heft IV, 32 (daneben
arm. LW. atr-).
kurd. aür, a7\ er; af/. ör; oss. arf (36); bei. äs (16);
minj. yür; arm. vergl. airem verbrennen, anzünden*
(H. No. 18).
10. ärazis 'Guttat' (unbelegt).
vgl. aw. rä-^ayfm^/ 'sie ordnen', rä^a-, räzar- 'Richt-
schnur; schon im Pehlevl verloren gegangen^). Also
zu {/reg- 'richten, aufrichten. Vergl. Hübsch mann
zu oss. ardzin 'richten' (28). Die Bedeutung des neu-
persischen Wortes lässt sich nicht weiter zurück ver-

=== HUB 4455-4470 ===
gegeben: arm. Xosroc -= pers. Xusrav; arm. xortakem *schlage
in Stiicke', np. xurdj xurda *klein, kleines Stiick*. Vgl. gr.
XoHQOTjg = pers. Xusrav ; XfO()aaiLua = ap. {h)uvarazmis, np.
x^'arazm; ^AguyMaia = ap. hara(h)uvatis etc.
§ 6. Ap. a wird zu i:
a) einigemal vor Zischlauten (s, z, s, z) und y sowie
nach den Palatalen 6 und /: atis Teuer (so immer bei Vullers)
fiir alteres atas (vgl. Horn Nr. 7), afgh. LW. atas, paz.
ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
jfidan = pasanjldan 'besprengt werden, aus "^pal-sinc-Uan
(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
pieman (pazmdn^ puzmdn) *bereuend* aus paseman; hizisk
*Arzt*, arm. hzisk (aus^hizisk iuv ^bisizk), skr. bhisdj- 'Arzt'
(unter Mitwii^kung des i der ersten Silbe); hiayar Viel* =
ap. ^vasi-ddra- zu bas Viel' = ap. vasiy (unter Mitwirkung
des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;

=== NYB adur entry ===
```


## [2026-09-05T05:29:09.920Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY آتش ===\"; grep -n \"آتش\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY آذر ===\"; grep -n \"آذر\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY latin index ATER ===\"; grep -n -i \"ATER\\b\\|ATAR\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T05:29:10.000Z] TOOL RESULT

```
=== ARY آتش ===
551:دادند که مثلاً واژه‌ی سانسکریت "۸018" (به معنی «آذر» يا «آتش») و واژه‌ی لاتین 10727157" نه
1441:ممین(در پانوشت برهان قاطع) این واژه را با آتش" همريشه می‌داند.
7147:۱ چم این واژه در زبان یونانی و ایسلندی کهن و ایرلندی کهن: شمله؛ لو آتش,.
15938:۲- چم این واژه در زبان‌های یونانی و ایسلندی کهن و ایرلندی کهن و گالی: آتش» سوختن.
16086:8 ,آتشآ7ل ها( ۷۵۸۳ 8۷ 0107704
=== ARY آذر ===
50:جنوبی و مرکزی و همچنین در استرالیاگبترش داده است. ضمناً در گذشته زبان مردم آذرپایجان و
182:شدند. مردمان این نواحی (مثلا ساکنان آذربایجان و ترکیه) همه به زبانهای هند و اروپایی تکلم
187:اسلامبولی و ترکی ترکمنی و آذری و غیره).
189:می‌دهد که مردم ترکیه (و شاید مردم آذربایجان) از نظر زادشناختی (0138287109) فقط دارای سی.
551:دادند که مثلاً واژه‌ی سانسکریت "۸018" (به معنی «آذر» يا «آتش») و واژه‌ی لاتین 10727157" نه
699:زبانهای قفقاز و گورهای سبکك کورگان (1180۸) در شمال آذربایجان مسیر کوچ این اقوام
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
832:ِ زبانهای ایرانی آذربایجان و آسیای صغیر و آسیای مرکزی) جای خود را به زبان ترکی دادند. ۱۲
=== ARY latin index ATER ===
224:INATARA io. ill (NADRE 653 £ NAEDDRE: 34S .,Sil (NATHIR 45°
528:Bay yma) (Ki2 dle se dale jl yy cel BROTHER ,,IKiI 3 y PHRATER
941:J Mater Thay Bae pls (ARES) cysts esl oy co lie y oblast
1361:MACKENZIE: (WATER) 139 APIA GREEK) gli
1362:BUCK: (WATER) 34-35 AMNIS LATIN) 3
1366:_ ATER ATARSH —(AVESTAN) gus)
1373:Ir-tF iebG oly ATER _— ALATINY a3 “a
1379:wth A ws (ARDENT ¢ ARID <) ARDERE 2 oj} VATER ys isojly lt -¥
1384:AGNIS _ ABITTITE) cox ATER {OLD PERSIAN) jheuly
1633:US-+MATAR-
```


## [2026-09-05T05:29:13.628Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT ater ===\"; grep -n -o -i \"ater,\\? *-tra\\|ater[^|]\\{0,300\\}\" LAT.txt | head -6\necho \"=== LAT atrium ===\"; grep -n -o \"atrium[^|]\\{0,300\\}\" LAT.txt | head -4\necho \"=== LEW ater ===\"; grep -n -o \"ater[^|]\\{0,250\\}\" LEW_1910.txt | head -6\necho \"=== SYN fire ===\"; grep -n -i \"atarš\\|ātar-\\|atar-\" SYN.txt | head -6\necho \"=== IEC ater ===\"; grep -n -i \"āter-\\|ater- *(\\|atr̥\\|ātr\" IEC.txt | head -8",
 "description": "Grep Latin dictionaries, Buck, Mann"
}
```


### [2026-09-05T05:29:15.360Z] TOOL RESULT

```
=== LAT ater ===
147:aternus ne
148:ater, il n'y a pas de mot du
173:ater, mater, frater, les principaux animaux do-
462:aternelle, contribuent A cette transforraation.
774:ateris ex auratis
846:atertera, abamita, abpatruus, abnepos,
=== LAT atrium ===
4909:atrium (P.F. 13,17 ), ete.; cf. Flor., Dig .50,16,311,arina
5755:atrium; et ■v.atrdx. - Le mot le plus sem-
5769:atrium, -i n.: pikce principale de la maison romaine, salle com¬
5780:atrium dictum est; atrum enim erat
=== LEW ater ===
225:aternum I 26 allo I 28, 30 altinim, altiram IY am- I 686 amfret I 36, 37, 407 amiricatud I 686, IT 78 amiricum I 687, I78
252:ater II 459 oaxooo II 459 Saipinaz, Lawes II 461 odhayé I 761 oahafc, salavs ITI 472 scriftas II 499
313:aterafust I 361 atero I 33, 845 atru I 75 avie, aviekla, aviekate I 84 avif, avef I 84 berva, berus II 766 bio II $09 bum, bue, buf I 112 cabriner, kabru LI 157 kalefuf I 139 kanetu I 154 capif, kapire I 160 kaprum I 157 karne I 170 kartu I 170, 198 karu
313:ateramu, catera- hamo I 181
362:ater I 542 frehtef, frehtu I 548 frif, fri I 552 frite I 505, II 4387 frosetom I 543 futa I 504, 505, 558 fuzest I 504, 505 Fulonie I 561 fons, foner I 464 Funtlere, fondlire I 525 furent I 557, II 629 furfant I 473 furo, furu I 537 fust I 557, 558, II 
365:ater, Juvepatre UG os LIP 263 aust I 406, 408 Joute, Juvie, Juve LEWES, WS) maletu II 104, 106 mandraclo, mantra- (h)klu II 32, 670 mani, manf IT 35 maronatet II 43 Marte, Marties, Martier, Martie II 43 Matrer II 50 mefa, mefe II 58, 70 mehe II 84 menzne
=== SYN fire ===
2082:8. Av. atar-, NPers. ddar ‘fire’, Av. abravan-, abaurvan-, Skt. atharvan- ‘fire- priest’, root connection? Walde-P. 1.42.
2558:In the inherited group the suffix -ter- or in some cases -er-, -or-, is conspicuous (cf. Skt. pitar-, matar-, bhratar-, duhitar-, jamatar-, yatar-; devar-, svasar-). Owing to the well-known use of this suffix in agent-nouns, these words of relationship were also formerly interpreted as agent- nouns from certain roots, e.g. ‘father’ as ‘protector’, ‘mother’ as ‘measurer, thoughtful one’, or the like, ‘brother’ as ‘supporter’, ‘daughter’ as ‘milker’, either the ‘suckling’ or the ‘milkmaid’, etc. Most of these derivations now seem fan- ciful and pointless and are generally given up. The use of the suffix is not to be connected directly with its use in agent-nouns, but rather with the use of -tero- (-ero) in words of contrasted rela- tionship, like Lat. dexter vs. sinister, nos- ter vs. vester, etc., that is, it was used in words for ‘father’ and ‘mother’, etc. as contrasted terms. Cf. Streitberg, IF 35.196.
2685:1. Grk. yapéw (a), yapéouar (b, but yanéw also for either party, N'T; in pop. NG ‘coire’), beside yauos ‘marriage, wed- ding’ : Grk. yayBpds, Skt. jamatar- ‘son- in-law’, etc. (2.63). Walde-P. 1.574.
2811:Skt. —_ pitar- méatar- pitarau, malarau
2812:Av. pitar- matar- pitara
2908:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 2.44 2.45 BROTHER SISTER Grk. 4ded¢ds abehon NG abeAdeds, pop. Abephés 4deAH7, POP- d5epon s Lat. frdter soror It. fratello sorella Fr. frére se@ur Sp. hermano hermana Rum. frate sora Ir. brathir siur Nir.  dearbrathatr deirbhshiur W. brawd chwaer Br. breur c’hoar Goth. brépar swistar ON brddir systir Dan. _broder sdster Sw. broder syster (0) 0) brddor sweostor ME brother sister, suster NE brother sister Du. broeder zuster OHG  bruodar swestar MHG_bruoder swester NHG _ bruder schwester Lith.  brdlis sesuo Lett. bralis masa ChSl.  bratrii, brati sestra SCr. brat sesira Boh.  brair sestra Pol. brat siostra Russ. brat sestra Skt. bhratar- svasar- Av. bratar- x’ anhar-
=== IEC ater ===
686:arədhlom ‘plough, ploughshare’. WP I, 78. Cf. arātrom, aro, io (1) MHG arl; Austro-Ger. Arl; OCS oralo, ralo; Cz. rádlo *ploughshare'; Slovene orálo ‘plough’; ralo *ploughshare'; oral ‘acre’, ral 'arable field"; Li. arklas; Latv. arkls
786:átos (-is, -us) “keen, swift Mir. áith ‘sharp, keen Li. otüs (beside otruüs), id.; Latv. cf. ātrs, id.
1612:bhrater- (bhratr-, bhrate) ‘brother’. WP II, 193 Skt. bhràtr; Av. brátà, acc.sg. bràtarom, braürom; Ober, bràtar, Per. biràdar; Tokh. A pracar, pl. pracre; B procer; Oss. árvad; Arm. eybajr, pl. eybarK; Phryg. brater-; Gk. phráter, adj. “of same tribe’; Ven. vhraterei, ds.; Hes. phréter; Lat. frāter; Osc. Umb. fra- ter, Osc. gp fratrüm; Mir & Ir. bráthair, pl. bráithre; W brawd, pl. brodyr, cf. also brodor (*club-member': Gk. phrátor, id.); Br. broer, pl. broedoer; Cor. broder, pl. breder; OHG bruoder; Go. bropar; OE broóor; ON broóir; OCS bratü, bratrá (and comm. Sl.); Li. cf. broter-élis, dim. beside brótis
3534:-elis, ios (noun and adj. extrí.) Arm. cf. eyk-eli ‘miserable’; Lat. mātru-ēlis; crud-elis; Li. broter-elis; numir-elis, etc.
5632:$enotér- (-tor-, -tór-) “parent, kinsman’. Cf. ênmātr- and WP I, 574-7 Skt. jánitr ‘father’; janitríh ‘mother’; janiítra ‘parents, bloodrelations'; Gk. genetér, genétor ‘parent’; Lat. genitor, genitrix; W geneth ‘girl, daughter'; cf. Venetic (queried) porah egetora (?) “for a kinsman’; variant in Arm. cnawy (parent, fr. *&enotlo-)
9504:las- — lātros, is, om
10369:mātēr (màter-, mātr) (1) ‘mother’. Cf. maté and mati. WP II, 229 Skt. matt; Ober matar; Per. madar; Oss. cf. mad, madà; Tokh. macar, B macer; Arm. majr, gs mawr, ab. s. marb; Myc. matere(i), ds; Gk. méter, gs métrós; Doric mater; Phryg. māte- res, pl.; Alb. motër 'sister'!; Lat. mater, gs matris; Osc. maatreís, gs; Umb. matrer, gs; (?) Faliscan materei, ds; Olr. máthir, Ir. má- thair, gs máithre; Gaul. matre-bo, dpl.; W cf. modr-yb (“aunt', fr. *màtriqua); OHG muoter; OE moóor, ds meóer; ON móðir, gs móður & moeór; OCS materi beside mati, gs matere; Slovak mat, mati & mater; R mat, gs materi; Li. móte, gs móters & móteris, f. ‘woman’; cf. móčia ‘mother; Latv. (isophone) materes, pl. Cmotherwort', bot.)
10382:māter- (3) (?) ‘pad, coating MHG muoder, müeder, m. n. ‘corselet (mod. Mieder); OFris. mother, n. id.; if related to mäter (1), cf. Lat. måtrix, Gk. métrà and G Perl-mutter, E mother-of-pearl. (In sense of “lees, dregs’ cf. E mother, Du. moer (2) and Fr. mère de vinaigre, Moravian z-matetely *mouldy'. The semantic link is obscure)
```


## [2026-09-05T05:29:25.210Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT 5750-5790 ===\"; sed -n '5750,5790p' LAT.txt",
 "description": "Print Ernout-Meillet atrium/ater"
}
```


### [2026-09-05T05:29:25.269Z] TOOL RESULT

```
=== LAT 5750-5790 ===
sorte de vigne (cf .asinusca); compose tardif: atribux (Ans. gloss.)
= atra bucca. Cf. atrox.
Adjectif italique: ombr. atru, adro "atra", etc. Cf. peut-etre iri.
aith ( g 4 n.dtho ) f. "fourneau", gall.odyn f. "id. ", s. vatra "feu", arn.
ayren "je brule" et a x.dtars "feu". Le sens serait "noirci par le
feu". Cf. une remarque sous atrium; et ■v.atrdx. - Le mot le plus sem-
blable serait lette atris "rapide"; mais le sens en est autre.
athanuulu»: r.atalla.
atinia, -ae f.: sorte d'orme (o.cille), gaulois (cf. Colum.5,6,a,
Plin.16,73,etc. ). Sans doute mot etranger, sans rapport avec le nom
propre Atinius, malgre le Thesaurus qui le range parmi les derives de
Attus, II 1175,lasqq.
atque: v. at.
atriplex ( atriplexun Fest. ) m.: arroche. - Sans doute emprunt au
gr. axpacpa^uC et av6pacpa!|t,S, atteste depuis Columelle. - Les formes
romanes remontent peut-etre a une forne plus voisine de 1'original
grec *atrapex, *atripex (on a adricipis CGL III 616,15, adrafax Ili
550,30), cf. M.L.759 et Festchr. Louis Gauchat, p.40, n.3. Le mot apparait
deforme de plusieurs manieres dans les Gloses.
atrium, -i n.: pikce principale de la maison romaine, salle com¬
mune situee imm 4 diatement aprfes 1'entree et le vestibule, et caracte-
risee par sa forme carr 4 e, et par son toit perc6 d'une ouverture au
centre ( conpluuiun) , a laquelle correspondait un bassin (impluuium)
dans le plancher. Le nom d ] dtrium a et 4 egalement donne a certains
monuments publica: 5 . Libertatis, atria Licinia, etc.; dans la 1 . de
l' 4 glise, traduit ccuAt) la "cour" du roi, ou designe les abords de la
basilique, et parfois la basilique elle-meme. - Ancien, usuel. Conserve
dans le port. adro, M.L.760. Ddrives: atriolum; atriensis (dtrensis,
etc.), le plus 3 ouvent substantive: (esclave), concierge, intendant.
Les anciens en donnent differentes 6tymologies: ab citer; cf. Serv.,
Ae.1,736, ibi et culina erat, unde atrium dictum est; atrum enim erat
ex fumo (mais la cuisine ne figurait pas dans 1 'atrium); ab Atria,
ville d'itrurie (Varr. L.L.5,161, atrium ab Atriatibus fuscis; illinc
enim exemplum sumptum). On a rapproche aussi gr. ouGpoov. II est probable
que le mot est d'origine etrusque.
Si 1 'atrium n'est pas etrusque, ce serait un souvenir de 1 ’ancienne
maison ou la fumee du foyer s'echappait par une ouverture raenagee dans
le toit (v. aedes) ; il y aurait ici soit un derive d'un ancien nom du
"feu", soit un derive de ater.
atrox, -ocis adj . : a 1 'aspect noir, c.-a-d. "affreux", e.g. Naeu.,
Carm.fr. 41, simul atrocia proicerent exta ministratores; d'ou "ter-
```


## [2026-09-05T05:29:27.439Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY around 1441 ===\"; sed -n '1425,1450p' incoming/ARY/ARY_pages.txt\necho \"=== nearest pdf page tag ===\"; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<1441' | tail -2\necho \"=== ARY latin index 1360-1390 ===\"; sed -n '1360,1390p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Print Aryanpur contexts"
}
```


### [2026-09-05T05:29:28.893Z] TOOL RESULT

```
=== ARY around 1441 ===
فقل ی
[pdf page 51]
اوستایی (/4۲8574۸): ب20۸7 ,۸71138۸۷۸1 لنونی (لتی) (7۳۵۸۷ا): 108 ر
۸738۸ ,۸78 آلبانی ((714ل۵قا)م): 7
پارسی باستان (۶8۴۶/۸۸ 010): ۱3 هیت (77/78/): .. . ۸5
پهلوی (۷هاتل۸ط): ۸1 پسگشت‌ها لامش اد ادن
کردی (020184): ۸ 9 ق۸۶00
سانسکریت (84(/5۴۸/7): ۰ ۸6818 ,۸۴ 6 (167153015) وی ان
لاین (712ل): 105 2 (781 86) :ما05
اسلاوی‌کهن (ع۲1بها5 #6لاتل ا0): 4 (5188) رگ :8ل2آلقق ما۸
: 0 72 عل‌ا8
روسی (/(۷8514): 0 1 (1075015) :0/05
چکه (2560)): 0 6 (6(185015]) :7
اسلواکی (8101۸4): 0 11 :47
لیترانی (40714ل 7 7/): 1018 برهان قاطع :(خاکستر) ۲۲و ۷۰۲ و(اگر)۵۳
یادداشت:
ممین(در پانوشت برهان قاطع) این واژه را با آتش" همريشه می‌داند.
اوستابی (/4۲897۸): ۰ ۰8۸01 ,011هعم ۸
پهلوی (۷7هالل۲۸): ۸ آلمانی (057/۸0): نراد با
سانسکریت (54(/86(7): ۰ ,8۸0177:07 انگلیسی کهن (8۸0/34 00): رال۸ ۸
مور موز 8۵08 ات۸ للقط ,50۸
لانین 1470 اد دی انگلیسی (0ل5ل6۸0): راد
گویک (077/0): 1360۸۷ ,ال۸ 0۸50 دانمارکی (0۸/۷18]7): 0)
ایسلند یکهن (010۸14۸/(ع5 صا0): هلندی (27ع0076): لد(
8۸0۸ اسلاوی کهن (ع4۷7ا5 804ات 0):
آلمانی کهن (/(688۵/۸ 0ات صا0): 371
=== nearest pdf page tag ===
1397:[pdf page 50]
1426:[pdf page 51]
=== ARY latin index 1360-1390 ===
POKORNY: . 51-52 Ae, APA (SANSKRIT) 2 Sie
MACKENZIE: (WATER) 139 APIA GREEK) gli
BUCK: (WATER) 34-35 AMNIS LATIN) 3
MALLORY 129 EAV APRENCH) si
1 igbG ob, UPE A(LITHUANIAN) gigs
ro sfaseos al cai UPE ALATVIAN) (3) is)
_ ATER ATARSH —(AVESTAN) gus)
‘REFERENCES breathy ATUR, ATAXSH (PAHLAVI) by
POKORNY, ar) AGIR (KURDISH) 52,5
DELAMARRE: (BEU) 179 ATHARVAN, — (SANSKRIT) © Site
MACKENZIE: (FIRE) 114 EDHOS, HUTASH u<o5
BUCK: n AIREM ARMENIAN) gs,\
AMINDAROV: (BIRE) 247 AITHOS GREEK) li
Ir-tF iebG oly ATER _— ALATINY a3 “a
FO-PF Mes eal cid EIT HOLD FRISIAN) (75 523
AITH OLD IRISH) S43 p
detlooy
oF AS SHA Oly al ee
a tole tad 3 dle ool ee
wth A ws (ARDENT ¢ ARID <) ARDERE 2 oj} VATER ys isojly lt -¥
re |
[pdf page 51]
» UGNUS * (LATVIAN) (33) 93) ATHRAVAN, ADAR, :(AVESTAN) gl!
ZJARR ALBANIAN) gidT ATUR, ATHRA-
AGNIS _ ABITTITE) cox ATER {OLD PERSIAN) jheuly
REFERENCES beh ADUR PAHLAVI) 5 shy
0) a) Acar (KURDISH) «52,5
BARNHART: (IGNEOUS) 506 AGNI, AGNIS (SANSKRIT) cy Suite
DELAMARRE: (LE FEU) 182 IGNIS LATIN) ys
MACKENZIE: 5, (FIRE) 114 HOLD CHURCH SLAVIC) 45g sl
BUCK: n OGNT ,
```


## [2026-09-05T05:29:47.407Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest standalone number before line 1710 (0-based idx 1709)\nfor i in range(1709,1650,-1):\n    if re.fullmatch(r'\\s*\\d{1,4}\\s*', t[i]):\n        print(\"page marker at line\",i+1,\":\",t[i].strip()); break\nprint(t[1705:1713])\nEOF\necho \"=== SKT atrocious ===\"; grep -n -o -i \"atrocious[^|]\\{0,250\\}\\|Atri[^|]\\{0,150\\}\" SKT.txt | head -6",
 "description": "Klein page marker and Skeat"
}
```


### [2026-09-05T05:29:49.249Z] TOOL RESULT

```
page marker at line 1684 : 27
['adown,  adv.,  downward.  —  ME.  adoune,  adoun, fr.  OE.  of-dune,  ‘from  (the)  hill’,  fr.  of,  ‘off’, and  diin,  ‘hill’.  See  of  and  down,  adv.', "Adoxa,  n.  a  genus  of  plants,  the  moschatel  (hot.) —  ModL.,  fr.  Gk.  &8oi;o<;,  ‘inglorious,  obscure, insignificant’,  fr.  a-  (see  priv.  pref.  a-)  and  So'a, ‘glory’,  which  is  rel.  to  Soxsiv,  ‘to  think,  be¬ lieve’,  86y|xa,  ‘opinion’,  and  cogn.  with  L.  do- cere,  ‘to  teach’,  decus,  ‘honor,  ornament’.  See decent  and  cp.  dogma,  doxology.", 'Adrastea,  Adrastia,  n.,  Nemesis.  —  L.  Adrdstea, Adrastia,  fr.  Gk.  ’ASpSoxsta,  lit.  ‘she  from whom  there  is  no  escape’,  fr.  SSpaoxop,  ‘not running  away,  not  inclined  to  run  away’,  fr.  a- (see  priv.  pref.  a-)  and  the  stem  of  SpoiapA;,  ‘a running  away’,  and  of  -8t8p4oxetv  (used  only in  compounds,  esp.  in  aTro-SiSp&cntEiv,  ‘to run  away’),  fr.  l.-E.  base  *dra-,  ‘to  move  quick¬ ly’,  whence  also  OI.  drSti,  ‘he  runs’.  From *drem-,  a  collateral  form  of  base  *dra-,  derive Gk.  Spapeiv,  ‘to  run’,  8p6|2.o;,  ‘course’.  See dromedary.', 'adrenal,  adj.,  near  the  kidneys;  n.,  one  of  the  two ductless  glands  above  the  kidneys  ( anat .)  — Formed  fr.  ad-  and  L.  renalis,  ‘pertaining  to  the kidneys’,  fr.  ren,  ‘kidney’.  See  renal, adrenaline,  adrenalin,  n.,  a  substance  secreted  by the  suprarenal  glands  (chem.)  —  Coined  by  the Japanese  chemist  Jokichi  Takamine  (1854-1922) in  1901  fr.  ad-,  L.  renalis,  and  chem.  suff.  -ine, -in.  See  prec.  word.', 'Adrian,  adj.,  Adriatic.  —  See  Adriatic  and  -an. Adrian,  masc.  PN.  — •  L.  Adrianus,  Hadrianus, lit.  ‘of  the  Adriatic’.  See  next  word.', 'Adriatic,  adj.  —  L.  Adriaticus,  Hadriaticus,  fr. Atria,  also  called  Adria,  Hadria  (now  Atri), a  town  in  Picenum,  fr.  dter,  fem.  atra,  neut. atrum,  ‘black’,  hence  lit.  ’the  black  city’  (see atrabilious  and  -atic);  the  town  was  so  called because  it  was  built  on  black  mud.  See  Momm¬ sen,  Inhabitants  of  Italy,  p.  76.', 'adrift', 'advocate']
=== SKT atrocious ===
30:atriarch- pupil  woald  be  learainf;  still.*
1218:atrich.abird.(F.-L.tf«^Gk,)  M.E. ^triie,  oysttycJu.^O.V.  osttiue;  mod.  F. autruiht,  Cf.  Span,  aveiinu^  Port,  a&es- truz,  an  ostrich.  —  L.  a
1285:atriflc-ItaLi«^
2968:atrixeio,  a  chariot,  augmentative of  c^nff  a  car.
3445:atrix.  a  icar .-•L.)    ItAl.  or^nm/.  a ao.«>L.  ace  Ciarpnciu,
4390:atriet^
```


## [2026-09-05T05:30:17.424Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON آذر ===\"; grep -n -o \"آذر[^ ]\\{0,3\\} *\\[[^]]\\{0,40\\}\\]\" MON_part1.txt | head -10\necho \"=== MON آتش ===\"; grep -n -o \"آتش *\\[[^]]\\{0,40\\}\\]\" MON_part1.txt | head -6\necho \"=== MON آدریاتیک ===\"; grep -n \"آدریاتیک\\|آدرین\" MON_part1.txt | head -5\necho \"=== FSD atrium ===\"; grep -n -o \"atrium[^|]\\{0,200\\}\" FSD_vol1.txt | head -4",
 "description": "Grep Mo'in 2-vol and Funk&Wagnalls"
}
```


### [2026-09-05T05:30:19.503Z] TOOL RESULT

```
=== MON آذر ===
=== MON آتش ===
=== MON آدریاتیک ===
=== FSD atrium ===
4336:atrium  (sodium).  [sign.
23635:atrium
28181:atrium  (cavity  or  sac);  as,  the  atrial  membrane,  etc.
28182:atrium;  as,
```


## [2026-09-05T05:30:27.733Z] TOOL CALL #49: Bash

```json
{
 "command": "ls site/pages/67.jpg 2>/dev/null; pdftoppm -f 67 -l 67 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg67 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 67"
}
```


### [2026-09-05T05:30:29.842Z] TOOL RESULT

```
site/pages/67.jpg
total 1144
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 01:30 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71145 Sep  5 01:29 pg71.png
```


## [2026-09-05T05:30:31.265Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%AF%D8%B1%DB%8C%D8%A7%D8%AA%DB%8C%DA%A9/",
 "prompt": "What do the Persian dictionaries say about آدریاتیک — is it defined as a sea (دریای آدریاتیک), and is any origin (French/Latin) given? Quote the Persian entry text."
}
```


### [2026-09-05T05:30:35.239Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T05:30:38.312Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg67.png"
}
```


### [2026-09-05T05:30:38.847Z] TOOL RESULT

```

```


## [2026-09-05T05:30:38.842Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T05:31:06.725Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://fr.wiktionary.org/wiki/Adriatique",
 "prompt": "Give the French etymology of Adriatique (mer Adriatique) and, if present, of the given name Adrien / Hadrien — their Latin sources."
}
```


### [2026-09-05T05:31:11.654Z] TOOL RESULT

```
# Etymology of Adriatique

**Adriatique (Mer Adriatique):**

The French term derives from Latin *Adriaticus*, which came from *Adria*, "the principal port of the Etruscans on the eastern coast of the Italian peninsula." The Latin root likely traces to Illyrian *adur*, cognate with Indo-European words for water, including English "water," Polish *woda*, and Welsh *dŵr*.

**Adrien/Hadrien:**

The web page provided does not contain etymological information for the given names Adrien or Hadrien. Only the geographical term *Adriatique* is documented in this Wiktionary entry.
```


## [2026-09-05T05:31:30.252Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/آتش\" \"https://en.wiktionary.org/wiki/آذر\" \"https://en.wiktionary.org/wiki/ater\" \"https://en.wiktionary.org/wiki/atrium\" \"https://en.wiktionary.org/wiki/آذربایجان\" \"https://www.etymonline.com/word/atrocity\" \"https://www.etymonline.com/word/atrium\" \"https://fr.wiktionary.org/wiki/Adriatique\"; do\npython3 tools/fetch_source.py \"$u\" --note \"pdf page 67, root Ater/Atr (PIE *h2eh1ter- fire): checking Persian atas/azar/Azarbayjan, Latin ater/atrium/Adriaticus, English atrocity/atrium/Adriatic and the French->Persian Adriatik link\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T05:31:33.568Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2b0ad0133a327d9a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbd3f0ee98ff0cb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51106cb7bcbd7065.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a1aca379903ce30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc207ccbe9e0d85c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0c0a96cfc4abaae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c6d0245554dfc54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb814390915449d2.txt
```


## [2026-09-05T05:40:47.491Z] TOOL CALL #54: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk67.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_ATASH=\"https://en.wiktionary.org/wiki/%D8%A2%D8%AA%D8%B4\"\nW_AZAR=\"https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1\"\nW_ATER=\"https://en.wiktionary.org/wiki/ater\"\nW_ATRIUM=\"https://en.wiktionary.org/wiki/atrium\"\nW_AZB=\"https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86\"\nE_ATROC=\"https://www.etymonline.com/word/atrocity\"\nE_ATRIUM=\"https://www.etymonline.com/word/atrium\"\nF_ADR=\"https://fr.wiktionary.org/wiki/Adriatique\"\n\ndoc = {\n \"pdf_page\": 67,\n \"book_page\": 37,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ater, Atr\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂eh₁ter- 'fire' (Pokorny's āt(e)r-, IEW 69; Watkins/AHD āter-)\",\n   \"note\": \"The root box is right on all three counts. Pokorny IEW p.69 has the lemma verbatim: 'āt(e)r- ,Feuer‘' (POK_01.txt, the entry stands between the printed page numbers 69 and 70), with Av. ātarš (gen. āθrō), Skt. atharvan- 'fire priest', Arm. ayrem 'I burn' and, hedged with 'vielleicht', Lat. āter. Nourai's two-shape headword 'Ater, Atr' simply reproduces Pokorny's ablauting stem ātar- / āθr-, which is also the Avestan strong/weak stem pair. Watkins (AHD Appendix, 1985 ed. p. 3 s.v.) heads the entry 'āter-. Fire.' and closes it '[Pok. ā(e)r- 69]'. Two refinements, neither an error: (a) the label 'Indo-European' is generous — the root is securely attested only in Indo-Iranian, Armenian and Italic (plus possible Celtic áith / odyn and Albanian vatër), so it is a dialectal rather than a common-IE word, and Buck (Selected Synonyms 1.81) files it with a sceptical 'root connection?'; (b) the modern laryngeal notation is *h₂eh₁ter-, Pokorny's ā- being the outcome of *h₂e-h₁. The gloss 'fire' is exactly Pokorny's 'Feuer'.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂eh₁ter- «آتش» درست است و پوکورنی در صفحهٔ ۶۹ فرهنگ ریشه‌شناختی خود دقیقاً همین مدخل را به صورت āt(e)r- «Feuer» آورده است؛ پس ارجاع نورایی (POK:69) عیناً درست است. دوگانگی «Ater / Atr» همان دو ستاک قوی و ضعیف اوستایی ātar- / āθr- است. دو نکتهٔ ویرایشی: نخست آنکه این ریشه تنها در هندوایرانی، ارمنی و ایتالیک (و شاید کلتی و آلبانیایی) گواه دارد و بنابراین واژه‌ای ناحیه‌ای است نه همه‌هندواروپایی (باک در فرهنگ مترادف‌ها با پرسش «root connection?» از آن یاد می‌کند)؛ دوم آنکه در بازسازی امروزین این ریشه با حنجره‌ای‌ها به صورت *h₂eh₁ter- نوشته می‌شود. در مجموع ادعای نورایی دربارهٔ خود ریشه درست است.\",\n   \"sources\": [W_ATER, W_ATASH],\n   \"ref_check\": [\n    {\"ref\": \"POK:69\", \"status\": \"supports\", \"note\": \"POK_01.txt, entry printed between the page numerals '69' and '70': 'āt(e)r- ,Feuer‘. Av. ātarš (Gen. āθrō) m. ,Feuer‘, wozu ai. atharvan- ,Feuerpriester‘, Lw. aus av. āθraxan-…; arm. airem ,verbrenne, zünde an‘… Vielleicht als ,verbrannt‘ auch lat. āter ,schwarz, dunkel‘ = umbr. atru, adro ,atra‘. … WP. I 42, WH. I 75 f.' (found with a python search for 'ät{e)r-' in POK_01.txt).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 42 (WLD_Bd1_pages.txt l.3898)\", \"stance\": \"supports\", \"note\": \"'at- „Feuer“. Av. atars m., np. adar „Feuer“, wozu trotz des auffälligen th wohl auch ai. atharvan- „Feuerpriester“ … Vielleicht als „verbrannt“ auch lat. ater „schwarz, dunkel“' — the same material Pokorny later condensed; the page reference WP. I 42 given by Pokorny is confirmed.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, Appendix s.v. āter- (AHD_watkins1985.txt l.299)\", \"stance\": \"supports\", \"note\": \"'āter-. Fire. 1. Suffixed zero-grade form *ātr-o- in Latin ater (feminine ātra), black (< “blackened by fire”): ATRABILIOUS. 2. … Latin ātrium … 3. … Latin ātrōx … [Pok. āt(e)r- 69.]' — identical root, gloss and Pokorny page.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1.81 'fire' (SYN.txt l.2082)\", \"stance\": \"partial\", \"note\": \"'8. Av. atar-, NPers. ādar “fire”, Av. aθravan-, aθaurvan-, Skt. atharvan- “fire-priest”, root connection? Walde-P. 1.42.' — Buck accepts the Iranian family but leaves the deeper IE etymology (and hence the Latin link) an open question.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, searched for āter-/ātr- (IEC.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'āter-', 'ater- (', 'ātr' returns only ātos 'keen, swift', bhrāter-, mātēr- etc.; Mann has no fire-root *āter- entry, so he offers no support either way.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ater (LAT.txt ll.5750-5757)\", \"stance\": \"supports\", \"note\": \"'Adjectif italique: ombr. atru, adro „atra“. Cf. peut-être irl. áith … gall. odyn … s. vatra „feu“, arm. ayrem „je brûle“ et av. ātarš „feu“. Le sens serait „noirci par le feu“.'\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nnodes = doc[\"entries\"][0][\"nodes\"]\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"âtarš, âthra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan ātar- m. 'fire' is an r/n-less heteroclitic-looking stem with a strong shape ātar- and a weak shape āθr-: nominative singular ātarš (< *ātar-s), genitive āθrō, accusative ātrəm; in composition the weak stem appears as āθrə- / āθra-, e.g. āθravan- 'fire-priest', āθrō.saoka- 'firebrand'. Nourai's two forms are therefore exactly this nominative and this compositional stem, and both are real. In the Younger Avesta ātar- is both the physical element and the divinity Ātar, 'son of Ahura Mazdā' (Y. 62, Ny. 5); the ninth day of the month is called Ātar. The word inherits PIE *h₂eh₁ter-, the *-r of the root showing directly in the strong stem, while the weak stem āθr- shows the regular Iranian shift of *-tr- to -θr-. Sanskrit atharvan- 'fire priest' is generally taken (Pokorny, Klein) as a loan from Iranian āθravan-, which is why Indic has no *ātar-.\",\n \"derivation_fa\": \"اوستایی ātar- «آتش» ستاکی دوگانه دارد: ستاک قوی ātar- که در نهادی (فاعلی) مفرد به صورت ātarš درمی‌آید و ستاک ضعیف āθr- که در اضافی (āθrō) و در ترکیب‌ها (āθravan- «آذربان، موبد») دیده می‌شود؛ پس هر دو صورتی که نورایی آورده واقعی‌اند. دگرگونی آوایی *-tr- به -θr- در ایرانی باستان قاعده‌مند است. در اوستای نو Ātar هم عنصر آتش است و هم ایزدی که «پسر اهورامزدا» خوانده شده و روز نهم ماه به نام اوست. بارتولومه (فرهنگ ایرانی باستان، ستون‌های ۳۱۲–۳۱۶) همین مدخل را با همین صورت‌ها دارد. ادعای نورایی در این گره درست است.\",\n \"sources\": [W_ATASH, W_ATER],\n \"ref_check\": [\n  {\"ref\": \"POK:69\", \"status\": \"supports\", \"note\": \"Pokorny p.69 s.v. āt(e)r-: 'Av. ātarš (Gen. āθrō) m. ,Feuer‘' — both of Nourai's forms, with the same gloss.\"},\n  {\"ref\": \"KLN:123\", \"status\": \"supports\", \"note\": \"Klein 1966 p.123 (page numeral '123' printed at KLN_1966.txt l.3860) s.v. atrabiliary: 'prob. cogn. with OI. atharvan-, Avestic aθravan-, „fire priest“, ātarsh, „fire“, atrya-, „ashes“, Arm. airem, „I light up, kindle“'; the same forms recur on the same page s.v. Atharvan.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 312-316 s.v. ātar- (BRT.txt ll.7101-7200)\", \"stance\": \"supports\", \"note\": \"Headword printed \\\"'ātar-: āθr-, aθr-, ātr-’ m. ,Feuer‘, 1) im jAw. ,Feuer‘ im Allgemeinen und spez. vom Herd- und vom sakralen Feuer, oft persönlich gedacht und göttlich verehrt\\\"; the closing note gives the descendants 'mp. ātūr, np. āδar' and 'Als gel[ehrtes]W[ort] in mp., np. ātaš, bal. āč, arm. LW. atas'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. āter- (AHD_watkins1985.txt l.299)\", \"stance\": \"silent\", \"note\": \"Watkins lists only the Latin descendants of the root and cites Pokorny 69; he gives no Avestan form, so he neither confirms nor contradicts ātarš / āθra- individually.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. ātaxš (NYB_vol2_glossary.txt l.761)\", \"stance\": \"supports\", \"note\": \"'ātaxš [ʾthš] fire, in the ordinary sense … — Av. ātarš; Paz. NP ātaš' — the Avestan nominative ātarš is the recognised source of the Middle Persian word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"âtur; âtur-pât\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book-Pahlavi ʾTWR / ʾtwr is conventionally transliterated ĀTUR and read ādur (MacKenzie, CPD p.5: 'ādur [ʾtwr | M ʾdwr, N ādar] fire; the god “Fire”; cal. 9th month; 9th day'); Nourai's 'âtur' is simply the older transliteration of the same word. It continues the Avestan weak stem āθr- / oblique āθur-, with intervocalic *-θr- > MP -dur- and, later, -ð- > NP -z- (Horn, Grundriss no.9: 'phlv. ātūr … schon aδōʹ gesprochen'). Beside it Middle Persian has ātaxš, an Avestanising loan of the nominative ātarš (Nyberg: 'the -x- in ātaxš [is] inorganic as in Zartuxšt'), which is what actually gives NP ātaš — see node #3. Ātur-pāt = MP Ādurbād, from Old Iranian *Ātr̥-pāta-, Av. Ātərəpāta- (Frawardin Yasht 102), the name both of the Sasanian high priest Ādurbād ī Mahraspandān and, earlier, of the Median satrap whom the Greeks called Atropates (4th c. BCE); with the relational suffix -akān it yielded MP Ādurbādagān > NP Āðarbāyagān > Āzarbāyjān, Greek Atropatēnē. Nourai's rendering 'fire guard' follows the Persian tradition (Kasravi, quoted by Mo'in in the Borhan footnote: 'pāt az masdar-e pāyidan be ma'nā-ye negahbāni kardan', i.e. 'guardian of the fire'); Western Iranists usually take pāta- as the past participle 'protected', hence 'protected by (the god) Fire'. Both readings are current and the morphology is the same, so this is a difference of interpretation, not an error; 'a hero' is a loose label for a historical Median satrap.\",\n \"derivation_fa\": \"در فارسی میانه این واژه به خط پهلوی ʾTWR نوشته و به قرارداد کهن ĀTUR آوانگاری می‌شود، ولی خوانش درست آن ādur است (مکنزی، فرهنگ کوچک پهلوی، صفحهٔ ۵). این صورت دنبالهٔ ستاک ضعیف اوستایی āθr- است؛ هرن می‌گوید که همان پهلوی ātūr در عمل aδō تلفّظ می‌شده و همین دال نرم در فارسی نو به ذال/ز بدل شده است (آذر). در کنار آن، فارسی میانه صورت دیگری هم دارد: ātaxš، که وام‌گیری دینی از صورت فاعلی اوستایی ātarš است و منشأ واقعی «آتش» است (نگاه کنید به گرهٔ ۳). Ātur-pāt همان آذرباد است، از ایرانی باستان *Ātr̥-pāta- و اوستایی Ātərəpāta- (فروردین‌یشت بند ۱۰۲)؛ با پسوند -اکان آذربادگان و سپس آذربایگان/آذربایجان شده است. معنیی که نورایی می‌دهد («نگهبان آتش») همان برداشت کسروی است که معین در حاشیهٔ برهان قاطع نقل کرده («پات از مصدر پاییدن به معنی نگهبانی کردن»)؛ ایران‌شناسان غربی معمولاً pāta- را صفت مفعولی «پاس‌داشته‌شده» می‌گیرند، یعنی «پاس‌داشتهٔ آتش». هر دو خوانش رایج است و این اختلاف تفسیر است نه خطا.\",\n \"sources\": [W_AZAR, W_AZB],\n \"ref_check\": [\n  {\"ref\": \"BQT:13\", \"status\": \"supports\", \"note\": \"Mo'in's etymological footnote to the headword آتش in Borhan-e Qate' runs across the foot of two facing pages (BQT_v1_pages.txt leaves 221-222, printed pp. ~11-12 by the file's leaf-210 offset, so Nourai's '13' is within the OCR/offset margin of error): '… اوستا ātar- و āθr-، پهلوی ātūr …' continuing 'در پارسی آذر، آدر، آتش، آدش، آتیش (عامیانه) از همین ریشه است'. The Pahlavi ātūr of Nourai's box is precisely Mo'in's form.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.5 (PHD.txt l.172)\", \"stance\": \"supports\", \"note\": \"'ādur [ʾtwr | M ʾdwr, N ādar] fire; the god “Fire”; cal. 9th month; 9th day'; the same page has 'ādišt [ʾtyst] fire-stand' and 'ādurgāh [ʾtwrgʾh] fire altar', all built on ādur.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. ātaxš (NYB_vol2_glossary.txt l.761)\", \"stance\": \"partial\", \"note\": \"Nyberg's headword for the ordinary word 'fire' in Pahlavi is ātaxš, not ādur ('— Av. ātarš; Paz. NP ātaš'); ādur is the sacral/calendrical form. So Nourai's Pahlavi box is right but incomplete: it omits the very form that actually feeds NP ātaš.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 9, p. 4 (HRN.txt ll.559-563)\", \"stance\": \"supports\", \"note\": \"'9. āδer „Feuer“, āder — ap. vergl. Āδrina-, Āθriyādiya-; aw. ātar- „Feuer“; phlv. ātūr (häufig auch auf Gemmen), schon aδōʹ gesprochen … arm. LW. atr-.'\"},\n  {\"src\": \"BQT\", \"where\": \"Mo'in's footnotes to آذربایگان / آذرباد (BQT_v1_pages.txt leaves 231-232, printed pp. ~21-22)\", \"stance\": \"supports\", \"note\": \"'در کتابهای پهلوی «آتورپاتکان» Ādurbādagān است … آتورپاتکان مرکب است از سه کلمه: ۱- آتور یا آذر، ۲- پات یا پای، ۳- کان یا گان … پس معنی کلمه یعنی سرزمین یا شهر آذرباد' (quoting Kasravi, Maqālāt I 117-122), and in the preceding note 'اوستا Ātərəpāta (بمعنی پاینده و نگهبان آتش) نام یکی از پاکدینان ایران باستان «فروردین یشت بند ۱۰۲»'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"âtaš «آتش»; âzar «آذر»; Âzarbâyejân «آذربایجان» (extra آدر، آدیش)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three words hang exactly where Nourai puts them, the third does not. (a) آذر āðar/āzar is the regular continuation of MP ādur: intervocalic -d- was already a fricative -ð- in late Sasanian Pahlavi (Horn no.9: 'phlv. ātūr … schon aδōʹ gesprochen'), and NP writes it ذ, pronounced z in modern Persian; it survives as the name of the ninth month and ninth day and as a personal name. The variant آدر of the chart's 'extra' field is the same word with plain d, a Borhan headword ('آدر … بمعنی آذر است که آتش باشد'), and آدیش likewise ('آدیش … آتش را گویند'); Mo'in's footnote lists all of them as one family. (b) آذربایجان < آذربایگان < MP Ādurbādagān < *Ātr̥-pāta-kāna-, 'the land of Ādurbād (Atropates)', is standard. (c) آتش ātaš, however, is NOT the descendant of ādur. It continues MP ātaxš, which is itself an Avestanising borrowing of the Avestan nominative ātarš taken over for its Zoroastrian cult sense (Nyberg: '-x- in ātaxš inorganic as in Zartuxšt'; Hübschmann, Persische Studien §6: 'atiš „Feuer“ … für älteres ataš … phl. ātaxš, zd. ātarš'; Wiktionary, following Nisanyan). آتش and آذر are therefore doublets — siblings, not parent and child — and Nourai's single arrow Pahlavi ātur → Persian ātaš collapses two separate Middle Persian words into one. The root and the general route are right, the internal link is wrong, hence 'plausible'.\",\n \"derivation_fa\": \"از سه واژهٔ این گره، دو تا دقیقاً همانجا که نورایی گذاشته می‌نشینند و یکی نه. «آذر» دنبالهٔ قاعده‌مند فارسی میانهٔ ādur است؛ دال میان‌دوواکه در اواخر دورهٔ ساسانی سایشی شده بود (هرن: ātūr در عمل aδō) و در فارسی نو ذال نوشته و ز خوانده می‌شود. گونه‌های «آدر» و «آدیش» که در کنار مدخل آمده هر دو سرمدخل برهان قاطع‌اند و معین همه را هم‌ریشه دانسته است. «آذربایجان» نیز از آذربایگان و آن از Ādurbādagān فارسی میانه است. امّا «آتش» فرزند ādur نیست؛ این واژه از فارسی میانهٔ ātaxš می‌آید که خود وام‌گیری دینی از صورت اوستایی ātarš است (نیبرگ: خ در ātaxš غیراصلی است، مانند زرتخشت؛ هوبشمان، پژوهش‌های فارسی بند ۶). پس «آتش» و «آذر» دوگانه (doublet) اند، نه پدر و فرزند؛ پیکان نورایی در این جا دو واژهٔ جداگانهٔ فارسی میانه را یکی گرفته است. ریشه و مسیر کلی درست است، پس این ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W_ATASH, W_AZAR, W_AZB],\n \"ref_check\": [\n  {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Nourai cites Mo'in's Farhang-e Farsi without a page; the six-volume Amir Kabir edition is not online (see refs_online.json MON notes) and the two-volume Adena condensation on disk (MON_part1/2.txt) is OCR'd so poorly that greps for آتش / آذر return nothing. Mo'in's own etymological opinion is however available at second hand through his Borhan footnotes (see BQT below) and through Aryanpur, who cites it.\"},\n  {\"ref\": \"FNI:12\", \"status\": \"not_checked\", \"note\": \"F. Danayi, Farhang-e Namha-ye Irani: purchase only, no copy online (refs_online.json marks it 'purchase').\"},\n  {\"ref\": \"ETM:59\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi: catalogue-only, no scan found (refs_online.json 'catalog').\"}\n ],\n \"consulted\": [\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §6 (HUB.txt ll.4461-4464)\", \"stance\": \"contradicts\", \"note\": \"'atiš „Feuer“ (so immer bei Vullers) für älteres ataš (vgl. Horn Nr. 7), afgh. LW. ataš, paz. ataš, arm. LW. atas (Sebeos), phl. ātaxš, zd. ātarš' — NP ātaš goes back to Pahlavi ātaxš and Avestan ātarš, not to Pahlavi ādur.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 9 p.4 (HRN.txt ll.559-563)\", \"stance\": \"supports\", \"note\": \"Horn's headword for the ādur line is exactly NP 'āδer „Feuer“, āder', from 'phlv. ātūr' — confirming آذر/آدر (and the chart's 'extra' آدر) but treating it separately from ātaš (his no. 7).\"},\n  {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to آتش (BQT_v1_pages.txt leaf 222) and the headwords آدر / آدیش (leaves 229-230)\", \"stance\": \"supports\", \"note\": \"'در پارسی آذر، آدر، آتش، آدش، آتیش (عامیانه) از همین ریشه است'; and the Borhan headwords 'آدر … بمعنی آذر است که آتش باشد' and 'آدیش … آتش را گویند' justify the chart's 'extra' field. Mo'in groups them as one root but does not derive آتش from ādur specifically.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi, pdf p.51 = printed p.52 (ARY_pages.txt / ARY_latin_index_pages.txt)\", \"stance\": \"supports\", \"note\": \"Independent modern Persian cross-check: the entry آتش lists 'ATER, ATARSH (AVESTAN) / ATUR, ATAXSH (PAHLAVI) / ATER (LATIN) / AIREM (ARMENIAN) / AITH (OLD IRISH) / ATHARVAN (SANSKRIT)', and the entry آذر lists 'ATHRAVAN, ADAR, ATUR, ATHRA- (AVESTAN) / ADUR (PAHLAVI)' — i.e. Aryanpur too puts آتش with ātaxš and آذر with ādur, as two branches of one root, and links both to Latin ater.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. ātaxš (NYB_vol2_glossary.txt l.761)\", \"stance\": \"contradicts\", \"note\": \"'— Av. ātarš; Paz. NP ātaš (-x- in ātaxš inorganic as in Zartuxšt…)' — explicit that NP ātaš comes from ātaxš.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Sogdian\",\n \"words\": \"âš`kw; ât`rh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both words are in Gharib's Sogdian dictionary on the page Nourai cites. No. 290 'ʾtʾrh, ātar (ʾtr, ʾtʾr, ʾtrh) — fire' is the Sogdian cognate of Avestan ātar-, inherited directly from Proto-Iranian *Hātr̥š with the usual Sogdian feminine/stem-extension -h; it appears in Manichaean, Buddhist and Christian Sogdian and in compounds such as ʾtr-xwrndē 'fire-swallowing' (no. 299, glossed by Gharib against Parthian ādur xwarendag). No. 278 'ʾsʾk(w) (āse) — ashes' carries Gharib's own etymology '©Av. āθrya < *āθraka', i.e. a -ka- derivative of the weak stem āθr- 'fire' → 'what the fire leaves'. So Nourai's semantic pairing 'ash / fire' in one box reproduces Gharib exactly. Two small points: Gharib romanises the first word with s (ʾsʾkw, read āse) where Nourai prints š, a difference of transliteration system rather than of substance; and hanging the Sogdian box on the root rather than on the Avestan box is the correct choice, since Sogdian ātar is a sister of Avestan ātar-, not a loan from it.\",\n \"derivation_fa\": \"هر دو واژه در فرهنگ سغدی بدرالزمان قریب در همان صفحه‌ای که نورایی ارجاع داده موجودند. مدخل ۲۹۰ ʾtʾrh به معنی «آتش» هم‌ریشهٔ مستقیم اوستایی ātar- است و از ایرانی آغازین *Hātr̥š به ارث رسیده، نه آنکه از اوستایی وام گرفته باشد؛ پس وصل کردن این جعبه به خود ریشه (و نه به اوستایی) روشمندانه است. مدخل ۲۷۸ ʾsʾk(w) «خاکستر» را خود قریب از اوستایی āθrya < *āθraka می‌گیرد، یعنی مشتقی از همان ستاک ضعیف āθr- با پسوند -ka-؛ پس جفت کردن «خاکستر» و «آتش» در یک جعبه دقیقاً برگرفته از قریب است. تنها اختلاف جزئی آن است که قریب حرف نخست را s آوانگاری کرده و نورایی š؛ این تفاوت نظام آوانگاری است نه خطا. ادعای نورایی درست است.\",\n \"sources\": [W_ATASH],\n \"ref_check\": [\n  {\"ref\": \"SOD:11\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p.11 (SOD_pages.txt leaf 76, the page numeral '11' is printed on the leaf; printed ≈ leaf − 66 per refs_online.json). That page carries no. 278 'ʾsʾk(w) B … āse (ʾsʾy) ©Av. āθrya < *āθraka — ashes' and, at its foot, the running entry 'ʾtʾrh'; nos. 289-294 'ʾtʾr => ʾtʾrh / ʾtʾrh … ātar (ʾtr, ʾtʾr, ʾtrh) — fire' straddle pp.11-12. Both of Nourai's words and both glosses are Gharib's.\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib nos. 278, 290, 293, 295-300 (SOD.txt ll.9290-9400)\", \"stance\": \"supports\", \"note\": \"Besides the two headwords, the surrounding entries confirm the vitality of the stem in Sogdian: 293 'ʾtr ʾwst- — (to) extinguish, (to) lay a fire', 296 'ʾtr swyt- — burn with fire', 298 'ʾtrwrtn — fire chariot', 299 'ʾtr xwrndy ©Parth. ādur xwarendag'.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 316 s.v. ātarya- / āθrya- and the ātar- article\", \"stance\": \"supports\", \"note\": \"Bartholomae's article for ātar- lists the derivatives in āθr-/ātr- from which Gharib's *āθraka 'ashes' is formed, e.g. 'ātarə-āθra- Adj. ‚dem Feuer (Ātar) entstammt‘'.\"},\n  {\"src\": \"POK\", \"where\": \"IEW p.69 (POK_01.txt)\", \"stance\": \"silent\", \"note\": \"Pokorny's article for āt(e)r- cites Avestan, Sanskrit, Armenian, Slavic and Latin but no Sogdian; he is silent on this node.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Latin\",\n \"words\": \"âter, âtrôx; âtrium; Adriâticus, Hadriâticus\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Āter, ātra, ātrum 'black, dark' < Proto-Italic *ātros < zero-grade *h₂eh₁t-ro-, literally 'blackened by fire' — this much is standard and is Nourai's own gloss: Umbrian atru/adro 'atra' is the direct Italic cognate, and Ernout-Meillet say plainly 'Le sens serait „noirci par le feu“'. Ātrōx 'fierce, frightful' is ātro- + the reduced *h₃ekʷ-s 'looking', i.e. 'black-looking' (Watkins: 'Compound shortened zero-grade form *ātro-okʷ- … „black-looking“, frightful: ATROCIOUS'; Klein p.123 s.v. atrocious identical) — so Nourai's combined gloss 'black, darkened with fire, also cruelty' is accurate for the pair. The other two items are less secure. Ātrium: Watkins/AHD does give exactly Nourai's explanation ('Latin ātrium, forecourt, hall, atrium (perhaps originally the place where the smoke from the hearth escaped through a hole in the roof)'), but Klein — Nourai's own second reference — rejects it: 'according to Varro … a word of Etruscan origin and rel. to the Etruscan town Atria … The connection of atrium with ater, „black, dark“, is folk etymology'; Ernout-Meillet call an Etruscan origin 'probable'; de Vaan finds Watkins' soot argument unconvincing but still prefers a fire word (*h₁eh₁t-r- 'fireplace'). Adriāticus: Klein p.27 supports Nourai word for word ('L. Adriāticus, Hadriāticus, fr. Atria, also called Adria, Hadria (now Atri), a town in Picenum, fr. āter … the town was so called because it was built on black mud'), but the sea is normally named from the other Adria, the Etruscan port in the Veneto, whose name is widely traced instead to an Illyrian *adur 'water'. Verdict 'plausible': āter/ātrōx confirmed, ātrium and Adriāticus contested.\",\n \"derivation_fa\": \"لاتین āter «سیاه، تیره» از ایتالیک آغازین *ātros و آن از صورت صفرمرتبهٔ *h₂eh₁t-ro- است، یعنی در اصل «آنچه آتش سیاهش کرده»؛ امبریایی atru/adro هم‌ریشهٔ مستقیم آن است و ارنو-میه هم همین معنی («سیاه‌شده از آتش») را می‌پذیرد. ātrōx «سهمگین، بی‌رحم» ترکیب ātro- با ستاک «دیدن» است، یعنی «سیاه‌روی، هول‌نما»؛ تا اینجا ادعای نورایی درست است. ولی دو واژهٔ دیگر مورد اختلاف‌اند: دربارهٔ ātrium واتکینز دقیقاً همان توضیح نورایی (جای خروج دود از سقف) را می‌دهد، امّا کلاین — که خود نورایی به او ارجاع داده — آن را ریشه‌شناسی عامیانه می‌خواند و آن را اتروسکی می‌داند؛ دووان نیز استدلال دود و دوده را نمی‌پذیرد هرچند همچنان آن را به واژه‌ای به معنی «اجاق» مربوط می‌کند. دربارهٔ Adriāticus نیز کلاین (صفحهٔ ۲۷) عیناً همان چیزی را می‌گوید که نورایی آورده، ولی نام دریا را معمولاً از آدریای دیگر (بندر اتروسکی در ونتو) می‌گیرند که خود را به ایلیریایی *adur «آب» بازمی‌گردانند. پس این گره در کلیّت پذیرفتنی است ولی با احتیاط.\",\n \"sources\": [W_ATER, W_ATRIUM, E_ATRIUM, E_ATROC, F_ADR],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. āter- (AHD_watkins1985.txt l.299) gives all three of Nourai's Latin items with his glosses: 'Latin ater (feminine ātra), black (< “blackened by fire”)'; 'Latin ātrium, forecourt, hall, atrium (perhaps originally the place where the smoke from the hearth escaped through a hole in the roof)'; 'Latin ātrōx, “black-looking”, frightful'.\"},\n  {\"ref\": \"KLN:27\", \"status\": \"supports\", \"note\": \"Klein p.27 (page numeral at KLN_1966.txt l.1684) s.v. Adriatic: 'L. Adriāticus, Hadriāticus, fr. Atria, also called Adria, Hadria (now Atri), a town in Picenum, fr. āter, fem. atra, neut. atrum, „black“, hence lit. ‚the black city‘ … the town was so called because it was built on black mud. See Mommsen, Inhabitants of Italy, p.76.' This is verbatim Nourai's 'name of a town (now Atri) in Italy built on black soil'. NOTE: the same Klein, on p.123 s.v. atrium, contradicts the other half of the box — 'The connection of atrium with ater, „black, dark“, is folk etymology' — so Nourai has taken the part of Klein that suited him and the atrium item from AHD instead.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.69-70 (POK_01.txt)\", \"stance\": \"partial\", \"note\": \"'Vielleicht als „verbrannt“ auch lat. āter „schwarz, dunkel“ = umbr. atru, adro „atra“' — Pokorny admits the Latin adjective only with 'vielleicht', and he lists neither ātrium nor Adriāticus.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein p.123 s.v. atrium (KLN_1966.txt l.3875)\", \"stance\": \"contradicts\", \"note\": \"'L. atrium; according to Varro, De Lingua Latina 5, §161, a word of Etruscan origin and rel. to the Etruscan town Atria, as the place of origin of this kind of architecture. The connection of atrium with ater, „black, dark“, is folk etymology.'\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ater and s.v. atrium (LAT.txt ll.5750-5790)\", \"stance\": \"partial\", \"note\": \"For ater: 'Le sens serait „noirci par le feu“' (supports). For atrium: 'Les anciens en donnent différentes étymologies: ab ater; cf. Serv. … atrium dictum est; atrum enim erat ex fumo … ab Atria, ville d’Étrurie (Varr. L.L. 5,161) … Il est probable que le mot est d’origine étrusque. Si l’atrium n’est pas étrusque … il y aurait ici soit un dérivé d’un ancien nom du „feu“, soit un dérivé de ater.'\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 42 (WLD_Bd1_pages.txt l.3898-3906)\", \"stance\": \"partial\", \"note\": \"'Vielleicht als „verbrannt“ auch lat. ater „schwarz, dunkel“ = u. atru, adro „atra“' — same hedged verdict as Pokorny, and again no atrium.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"atrocity; atrium; Adrian; Adriatic\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are straightforward Latin-to-English items, and Klein's two cited pages cover them exactly. Atrocity is first attested in the 1530s, from French atrocité, from Latin atrōcitātem (acc. of atrōcitās 'cruelty'), from atrōx (Klein p.123: 'F. atrocite, fr. L. atrocitātem … fr. atrox'; Etymonline dates it 1530s and glosses the Latin as 'of fiery or threatening appearance'); the adjective atrocious was formed on the same stem in the 1660s. Atrium is a learned direct borrowing of the Latin noun, used first of the Roman house and, from about 1870, of the chambers of the heart. Adrian is Latin Adriānus/Hadriānus, literally 'of Adria' — the emperor Hadrian's family came from Hadria/Atri in Picenum — and Adriatic is Latin Adriāticus; the English forms keep the Latin ones essentially unchanged. The Latin → English edge as drawn is therefore correct; whatever doubt attaches to these words attaches upstream, to the Latin box (node #5), not here.\",\n \"derivation_fa\": \"هر چهار واژه وام‌واژه‌های مستقیم یا باواسطهٔ لاتین‌اند و هر دو صفحه‌ای که نورایی از کلاین ارجاع داده دقیقاً همین‌ها را دارند. atrocity از دههٔ ۱۵۳۰ میلادی از فرانسوی atrocité و آن از لاتین atrōcitātem (از atrōx) وارد انگلیسی شده است. atrium وام‌گیری عالمانهٔ مستقیم از لاتین است که از حدود ۱۸۷۰ معنی تشریحی (دهلیز قلب) هم یافته. Adrian همان Hadriānus لاتین است به معنی «اهل آدریا» و Adriatic همان Adriāticus. پس پیوند لاتین به انگلیسی در این گره قطعی است و هر تردیدی که هست به جعبهٔ لاتین (گرهٔ ۵) بازمی‌گردد نه به اینجا. ادعای نورایی درست است.\",\n \"sources\": [E_ATROC, E_ATRIUM],\n \"ref_check\": [\n  {\"ref\": \"KLN:27\", \"status\": \"supports\", \"note\": \"Klein p.27 (KLN_1966.txt ll.1710-1711): 'Adrian, adj., Adriatic. — See Adriatic and -an. Adrian, masc. PN. — L. Adriānus, Hadriānus, lit. ‚of the Adriatic‘.' and 'Adriatic, adj. — L. Adriāticus, Hadriāticus, fr. Atria … (now Atri)'.\"},\n  {\"ref\": \"KLN:123\", \"status\": \"supports\", \"note\": \"Klein p.123 (KLN_1966.txt l.3875): 'atrocity, n., atrociousness. — F. atrocite, fr. L. atrocitātem, acc. of atrocitas, „cruelty“, fr. atrox'; and 'atrium, n., 1) the central, courtlike room of the ancient Roman house; 2) (anat.) cavity in the heart or in the ear. — L. atrium'. Both English words are on the cited page.\"}\n ],\n \"consulted\": [\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol.1 s.v. atrium (FSD_vol1.txt ll.23635, 28181-28182)\", \"stance\": \"supports\", \"note\": \"carries English 'atrium' in both the architectural and the anatomical sense ('atrium (cavity or sac); as, the atrial membrane'), confirming the word and the semantic range Nourai's box implies.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. āter- (AHD_watkins1985.txt l.299)\", \"stance\": \"supports\", \"note\": \"The English words Watkins hangs on this root are precisely ATRABILIOUS, ATRIUM and ATROCIOUS — three of Nourai's four; Adrian/Adriatic are proper names and outside Watkins' scope.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"An empty pass-through box with no forms and no reference: its only function in the chart is to route the Latin words onward to the Persian loans of node #8, i.e. to say that Persian took these words from French rather than from Latin or English directly. The forms Nourai leaves unwritten are French atroce/atrocité, atrium, Adrien (learned Hadrien) and Adriatique, all learned borrowings from Latin made in the later Middle Ages and the Renaissance rather than inherited popular forms — the retention of -tr- and of the Latin suffix shape shows this. French Adriatique is fr.wiktionary's headword, 'du latin Adriaticus, de Adria', which is exactly the link the box needs. The claim is reasonable but unevidenced in the book, hence 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"این جعبه تهی است و نه واژه‌ای دارد و نه مأخذی؛ کارکردش در نمودار فقط آن است که بگوید وام‌واژه‌های فارسی گرهٔ ۸ از راه فرانسه آمده‌اند و نه مستقیماً از لاتین یا انگلیسی. صورت‌هایی که نورایی ننوشته عبارتند از atroce/atrocité، atrium، Adrien (و صورت عالمانهٔ Hadrien) و Adriatique؛ همه وام‌گیری عالمانه از لاتین‌اند (نگاه‌داشتن خوشهٔ -tr- و شکل پسوند لاتینی گواه آن است) و نه میراث مستقیم مردمی. ویکی‌واژهٔ فرانسه ذیل Adriatique می‌نویسد «du latin Adriaticus, de Adria» که دقیقاً همان حلقه‌ای است که این جعبه لازم دارد. ادعا معقول است ولی در کتاب بی‌سند مانده، پس با احتیاط پذیرفتنی است.\",\n \"sources\": [F_ADR, E_ATROC],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference at all in the book (refs=None), so there is nothing of Nourai's to verify; the box is a silent conduit between the Latin and the modern Persian boxes.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein p.123 s.v. atrocity (KLN_1966.txt l.3875)\", \"stance\": \"supports\", \"note\": \"Klein routes the word through French — 'atrocity … F. atrocite, fr. L. atrocitātem' — which shows the French stage of this family is real, even though Nourai leaves the box empty.\"},\n  {\"src\": \"WEB\", \"where\": \"fr.wiktionary s.v. Adriatique (archived, see sources)\", \"stance\": \"supports\", \"note\": \"'Du latin Adriaticus, de Adria, principal port des Étrusques sur la côte est de la péninsule italienne' — confirms the existence and the Latin source of the French form that must underlie Persian آدریاتیک; it also offers a rival etymology of Adria itself (Illyrian *adur 'water'), which does not affect this node.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"Persian\",\n \"words\": \"Âdrîan «آدرین»; Âdrâtîk «آدریاتیک» (extra آدریان)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both are modern European loanwords in Persian, not inherited Iranian words, and their shape points to French as Nourai says. آدریاتیک ādriātīk 'the Adriatic (sea)' renders French Adriatique: the final -یک is the standard Persian rendering of French -ique (compare کلاسیک, آتلانتیک), whereas English 'Adriatic' would have given *آدریاتیک with a different stress-and-vowel profile and Latin Adriāticus would have given *آدریاتیکوس. آدرین / آدریان for the emperor Hadrian likewise reflects French Adrien (آدرین) beside the Latin-based آدریان/هادریانوس used in Persian histories — the chart's main form and its 'extra' variant are exactly this pair. The chain is thus a long round trip: a word that Persian already owned as آذر (from the same PIE *h₂eh₁ter-) returns to Persian in the twentieth century through Latin and French, as a doublet its speakers do not recognise. Verdict 'plausible' rather than 'confirmed' only because neither of Nourai's two references for the box could be consulted, and no dictionary on disk or online was found that states the French route explicitly; the reasoning above is phonological, not documentary.\",\n \"derivation_fa\": \"هر دو واژه وام‌واژهٔ اروپایی نو‌اند و میراث ایرانی نیستند، و ریخت آوایی‌شان — چنانکه نورایی می‌گوید — به فرانسه اشاره دارد. «آدریاتیک» برگردان Adriatique فرانسوی است؛ پسوند -یک در فارسی برابر معمول -ique فرانسوی است (مانند کلاسیک، آتلانتیک)، در حالی که از لاتین Adriāticus باید «آدریاتیکوس» می‌داشتیم. «آدرین» نیز برابر Adrien فرانسوی است در کنار گونهٔ لاتینی‌تر «آدریان/هادریانوس» که در تواریخ فارسی به کار می‌رود — و همان دوگانه‌ای است که در نمودار یکی مدخل و دیگری در پرانتز آمده است. نکتهٔ جالب آنکه این وام‌گیری یک رفت و برگشت کامل است: واژه‌ای از همان ریشهٔ *h₂eh₁ter- که فارسی از دیرباز به صورت «آذر» داشت، این بار از راه لاتین و فرانسه بازمی‌گردد. چون هیچ‌یک از دو مأخذ نورایی در دسترس نبود، این ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [F_ADR],\n \"ref_check\": [\n  {\"ref\": \"FNI:12\", \"status\": \"not_checked\", \"note\": \"Danayi, Farhang-e Namha-ye Irani — purchase-only, no copy online (refs_online.json).\"},\n  {\"ref\": \"MON5:12\", \"status\": \"not_checked\", \"note\": \"Mo'in, Farhang-e Farsi vol.5 (a'lam / proper names), p.12. refs_online.json records that the six-volume Amir Kabir edition is not online at all and that vajehyab's Mo'in has no proper-name entries; the two-volume Adena condensation on disk does not include the a'lam volumes. Not verifiable with the material available.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"vajehyab / abadis (Mo'in online) and MON_part1.txt\", \"stance\": \"silent\", \"note\": \"The online Mo'in carries no proper-name entries and greps for آدریاتیک / آدرین in MON_part1.txt return nothing; abadis.ir returned HTTP 400 for the query آدریاتیک. No confirmation either way.\"},\n  {\"src\": \"WEB\", \"where\": \"fr.wiktionary s.v. Adriatique (archived, see sources)\", \"stance\": \"supports\", \"note\": \"Establishes the French form Adriatique < Latin Adriaticus, the only stage that can explain Persian آدریاتیک with its -یک ending; it is indirect support for the arrow French → Persian that Nourai draws.\"}\n ]\n})\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-67.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk67.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-67.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 67",
 "description": "Write and validate page-67.json"
}
```


### [2026-09-05T05:40:49.470Z] TOOL RESULT

```
ok 8
JSON OK
nodes verified: 8/8
node verdicts: {'confirmed': 4, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_checked': 6}
books consulted: {'supports': 15, 'silent': 3, 'partial': 4, 'contradicts': 3} | by book: {'NYB': 3, 'BRT': 2, 'AHD': 2, 'HRN': 2, 'BQT': 2, 'POK': 2, 'KLN': 2, 'WEB': 2, 'PHD': 1, 'HUB': 1, 'ARY': 1, 'SOD': 1, 'LAT': 1, 'WLD': 1, 'FSD': 1, 'MON': 1}
```


## [2026-09-05T05:40:58.739Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-67.json'\nd=json.load(open(p,encoding='utf-8'))\nn=d['entries'][0]['nodes']\nn[7]['words']=\"Âdrîan «آدرین»; Âdrîâtîk «آدریاتیک» (extra آدریان)\"\nfor nd in n:\n    for c in nd.get('consulted',[]):\n        if c['src']=='WEB' and 'fr.wiktionary' in c['where']:\n            c['src']='WKT-fr'\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(n[7]['words'])\nEOF\npython3 tools/verify_check.py 67",
 "description": "Patch node 8 words and source labels"
}
```


### [2026-09-05T05:41:00.647Z] TOOL RESULT

```
Âdrîan «آدرین»; Âdrîâtîk «آدریاتیک» (extra آدریان)
nodes verified: 8/8
node verdicts: {'confirmed': 4, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_checked': 6}
books consulted: {'supports': 15, 'silent': 3, 'partial': 4, 'contradicts': 3} | by book: {'NYB': 3, 'BRT': 2, 'AHD': 2, 'HRN': 2, 'BQT': 2, 'POK': 2, 'KLN': 2, 'WKT-fr': 2, 'PHD': 1, 'HUB': 1, 'ARY': 1, 'SOD': 1, 'LAT': 1, 'WLD': 1, 'FSD': 1, 'MON': 1}
```


## [2026-09-05T05:41:18.810Z] AGENT

Page 67 (book p. 37), root **Ater, Atr** "fire" — verification written to `/home/sfmqrb/git/rishe/data/verification/page-67.json`. `verify_check.py 67`: 8/8 nodes, **0 PROBLEM lines**.

Counts: root confirmed; nodes 4 confirmed (#1 Avestan, #2 Pahlavi, #4 Sogdian, #6 English), 4 plausible (#3 Persian, #5 Latin, #7 French, #8 Persian loans). Ref checks: 8 supports, 6 not_checked (FNI, ETM, MON — all purchase/offline). 16 books consulted (POK, WLD, AHD/Watkins, SYN, IEC, LAT, BRT, PHD, NYB, HRN, HUB, BQT, MON, ARY, SOD, KLN, FSD).

No `disputed` or `transcription_suspect` items, and **no extraction errors** — I read the printed page (200 dpi render) and the JSON is faithful throughout, including the Sogdian `âš`kw`, the `extra` fields (آدر ، آدیش / آدریان) and the `☞Pa` see-reference.

Notable findings the owner may want:
- **#3 Persian آتش is not a child of Pahlavi ātur.** Nyberg, Hübschmann §6 and Wiktionary all derive آتش from MP *ātaxš*, an Avestanising loan of the nominative *ātarš*; آذر is the one that continues *ādur*. They are doublets, so Nourai's single arrow collapses two distinct Middle Persian words. Hence `plausible`.
- **#5 Latin: Nourai's own reference contradicts half the box.** Klein p.123 s.v. *atrium*: "The connection of atrium with ater … is folk etymology" (Ernout-Meillet: probably Etruscan; de Vaan rejects Watkins' soot argument). Nourai took *atrium* from AHD instead. Klein p.27 does support *Adriāticus* < Atri verbatim, but the sea is usually named from the Veneto Adria (Illyrian *\*adur* "water").
- **BQT:13 page offset**: Mo'in's آتش footnote ("اوستا ātar- و āθr-، پهلوی ātūr … در پارسی آذر، آدر، آتش، آدش، آتیش از همین ریشه است") sits at leaves 221–222 = printed pp. ~11–12 by the file's leaf−210 offset, not 13; within OCR/offset error, recorded as `supports` with the caveat.
- POK:69, KLN:27, KLN:123, SOD:11 and AHD all check out exactly as cited; Pokorny's lemma "āt(e)r- ,Feuer'" is literally on p. 69.
- "ātur-pāt = fire guard" follows Kasravi/Mo'in (*pāt* < *pāyidan*); Western Iranists read *pāta-* as "protected by fire". Both current — noted, not flagged.

8 web pages archived via `fetch_source.py` (Wiktionary آتش/آذر/ater/atrium/آذربایجان, Etymonline atrocity/atrium, fr.wiktionary Adriatique).
