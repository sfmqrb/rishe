# Verification process log — verify-page-137


## [2026-09-05T20:07:21.185Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 137 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-137.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-137.json. Write /home/sfmqrb/git/rishe/data/verification/page-137.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 137` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:07:22.315Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:07:23.024Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:07:23.037Z] TOOL RESULT

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


## [2026-09-05T20:07:23.577Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-137.txt"
}
```


### [2026-09-05T20:07:23.599Z] TOOL RESULT

```
1	=== PDF page 137 (book page 107) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dinghw, Dnghu, Ghu 2, Ghuâ : tongue  (refs POK:223; PRT:335; KNT:211)
4	#1 (parent #0) [Avestan] refs=PRT:335; SYN:230; KNT:211,214 | zav 1, zbâ : call ; hizŭ, hizvâ : tongue
5	  #2 (parent #1) [Pahlavi] refs=None | uzvân
6	    #3 (parent #2) [Persian] refs=PRT:335; BQT:1003; BRT:1815; IEC:409,410; MON | zabân «زبان» : tongue, language ; hozvân «هزوان» : tongue
7	  #4 (parent #1) [Sogdian] refs=SOD:91 | `zb`k : tongue
8	#5 (parent #0) [Old Persian] refs=KNT:211,214 | zbâ : call ; hizana, hazana : tongue
9	  #6 (parent #5) [None] refs=None | 
10	#7 (parent #0) [Sanskrit] refs=KNT:211 | hŭ, hvâ : call ; jihva : tongue
11	#8 (parent #0) [Germanic] refs=AHD | tungôn : tongue
12	  #9 (parent #8) [English] refs=None | tongue
13	#10 (parent #0) [Latin] refs=AHD | dingua, lingua : tongue, language
14	  #11 (parent #10) [English] refs=None | language
15	
```


## [2026-09-05T20:07:26.862Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-137.json",
 "description": "Read source JSON for page 137"
}
```


### [2026-09-05T20:07:26.901Z] TOOL RESULT

```
{
  "pdf_page": 137,
  "book_page": 107,
  "entries": [
    {
      "root": {
        "name": "Dinghw, Dnghu, Ghu 2, Ghuâ",
        "lang": "Indo-European",
        "refs": "POK:223; PRT:335; KNT:211",
        "gloss": "tongue"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "PRT:335; SYN:230; KNT:211,214",
          "words": [
            {"translit": "zav 1, zbâ", "gloss": "call", "script": null},
            {"translit": "hizŭ, hizvâ", "gloss": "tongue", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "uzvân", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "PRT:335; BQT:1003; BRT:1815; IEC:409,410; MON",
          "words": [
            {"translit": "zabân", "gloss": "tongue, language", "script": "زبان"},
            {"translit": "hozvân", "gloss": "tongue", "script": "هزوان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:91",
          "words": [
            {"translit": "`zb`k", "gloss": "tongue", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:211,214",
          "words": [
            {"translit": "zbâ", "gloss": "call", "script": null},
            {"translit": "hizana, hazana", "gloss": "tongue", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": null,
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "KNT:211",
          "words": [
            {"translit": "hŭ, hvâ", "gloss": "call", "script": null},
            {"translit": "jihva", "gloss": "tongue", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tungôn", "gloss": "tongue", "script": null}
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
            {"translit": "tongue", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "dingua, lingua", "gloss": "tongue, language", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "language", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:07:27.582Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:07:27.616Z] TOOL RESULT

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


## [2026-09-05T20:07:31.252Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','PRT','KNT','SYN','SOD','BQT','BRT','IEC','MON','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700])\n    print('---')\n\""
}
```


## [2026-09-05T20:07:31.816Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-124.json"
}
```


### [2026-09-05T20:07:33.087Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
---
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.", "notes": "RE-SEARCH 2026-09: 8 lending
---
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
---
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
---
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
---
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
---
```


### [2026-09-05T20:07:33.144Z] TOOL RESULT

```
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
```


## [2026-09-05T20:07:39.007Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dn̥ǵhu\\|dṇg̑hū\\|dnghu\\|dn̥ghū\\|Zunge\" POK_full.txt | head -40\necho \"=== search lemma\"\ngrep -n \"Page(s): 223\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:07:39.078Z] TOOL RESULT

```
23309:Maybe alb. {*dnghua) g/uha^ tongue, language' not from Latin linguaior alb. has preserved 
23310:-/7-in contrast to Latin Hence alb. d- . I- mutation is genuine. Alb. {*dnghua) g/uha ^tongue' 
23331:metathesis from *tankwa, Indo Germanic *dnghua). 
75113:High German Bavarian Swiss Schachen ds., Old Icelandic s/reA/// 'Landzunge'. 
82614:starata-, stain's- v\. 'Streu, lair, bed'; urvard-straya-^H\e6er\\auev\irom Pflanzungen'; 
86224:thrum) in tunge-drum^Aas Zungenband', Middle Low German drum, o'/'o/77Trumm, 
=== search lemma
23335:Page(s): 223 
23553:Page(s): 223-226
```


## [2026-09-05T20:07:39.903Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hizan\\|hizv\\|hiz\\b\\|tongue\" KNT.txt | head -40"
}
```


### [2026-09-05T20:07:39.961Z] TOOL RESULT

```
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
536:$27. Тнк COMBINATION № was peculiar, since it could normally be used only for the value haz, not for hi. In representing hi, whether the 1 was an etymological vowel or only a part of hzy for hy ($25) or for final -hi (587), the ? was normally omitted in writing: опо = Атама, Av. Anā- hita-; d'hyau% = dahydus, Skt. ddsyu-; hey = hya, Skt. syds; рге ау" = part-barahy, Skt. bhdrdst; hzan"m* = Мгйлат DB 2.74, Av. hizvd-. Before an enclitic, the -y of -hy for -hi disappeared: paribarah’-dis DB 4.74, cf. pari- barahy 78; vikanals-di$ DB 4.77, cf. vikanahy 73. Rarely, the h? is omitted and the т is kept: a13?- а = амаа DB 1.85, cf. Av. pres. hiStaite. Both types of writing are exemplified іп maniyáhay DPe 20, maniyaity XPh 47, for maniydhaiy.
1198:OP Лапат for acc. hizénam ‘tongue’, Av. hizvà-, Skt. jthod-; see Lex. s.v. for details. $92. PIE ks became pAr. С and reverted in
2214:rate it is an extension of the stem seen in Ау. . hizvd- (see Lex. s.v. hazdna-). Neuters with suf- '*
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at my palace entrance, all the people saw him. Afterward I impaled him at Ecbatana; and the men who were his foremost followers, those at
3685:“Go forth; the hostile army which shall not call itself mine, that do ye smite!” Thereupon Takh- maspada with the army went off; he joined battle with Cigantakhma. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army and took Cicantakhma prisoner, (and) led him to me. Afterwards I cut off his ears and nose and tongue, and put out one eye; he he was kept bound at my palace entrance, all the people saw him. Afterwards I impaled him at Arbela.
5662:paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
```


## [2026-09-05T20:07:45.061Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23280,23345p' POK_full.txt"
}
```


### [2026-09-05T20:07:45.115Z] TOOL RESULT

```
Note: often reshaped through aniaut change and rearrangements 

Material: Old Indie y//7i/af., Avestan b/zva6s. (Proto Aryan * g/gbua kom * dagbua \N\t\r\ i 

from lib- "lick' orfromy//^ " turn down '; Iran. *s/zi/5 probably through sound dissimilation); 

Maybe Root/ lemma: dpghu, dpghua: tongue' derived from Root/ lemma: 6!^eregh- 

{6!^fgh-na^ : "to wind, turn'. 

besides J-stem in Old Indie yi//7jf. "tongue, spoon' (with u aiter Jubot/" pour into the fire ', 

different Wackernagel-Debrunner III 192), Avestan b/zum. ds.; with -on- for -a Old pers. 

bizbana-. Middle Persian buzvan6s., North Aryan b/sanm. "tongue, discourse ' {*vizhvan 

after E. Leumann North Aryan Spr. 127 f.); 

Armenian lezu. Gen. /ezi//places in ending -gbuas^a)/ from *dngbua, the first syllable 
probably influenced by leigh-^\\cV!\ 

Note: common Latin d- > l-\ also common Italic-Latin d- > /-shift. 

Old Latin dingua, Latin lingua {mVr\ A from lingere); Oscan fangvam {Wetter Serta 
Hoffilleriana 153; 



Maybe alb. {*dnghua) g/uha^ tongue, language' not from Latin linguaior alb. has preserved 
-/7-in contrast to Latin Hence alb. d- . I- mutation is genuine. Alb. {*dnghua) g/uha ^tongue' 
is similar to formation alb. {*dlagh-t-) glate, gjate, gJat^\ov\g\ 

Old Irish teng {a-siem) and tengae. Gen. tengadW\\h t- after tongid' swears '; but Old 
Irish //gi//'" tongue' to Latin ligurria, unclear is mcymr. tafawt, cymr. tafod, acorn, tauot. 
Middle Breton teaut, bret. teod, wherefore corn, tava. Middle Breton taffhaff, bret. tanva 
'taste' (Celtic *tamatol)\ 

Gothic tuggoi.. Old Norse Old Saxon tunga. Old English tunge. Old High German 
zunga, with -on- instead of -a, as ablaut neologism perhaps here Old Norse tangi^ clutch 
piece of the blade ', Middle Low German tange^sav\6 shift between two marshes'; 

Balto Slavic inzu-xw. in Old Prussian insuwis, Lithuanian //ezu v/s {aiter //iezZ/'lick'); Old 
Church Slavic yi^zy-/rb, Serbo-Croatian yiez/]^, po\n.j^zyk, russ.Jazy/c, to contraction of 
aniaut. d- s. J. Schmidt, Krit. 77; 

Note: 

Common lllyrian-Baltic d- > zero. 

Tocharian A kantu. Gen. kantwis, B kantwo. Obi. kantwa sa {*kantwa, reconverted with 
metathesis from *tankwa, Indo Germanic *dnghua). 

References: WP. I 1792, WH. I 806 f., Trautmann 104, Specht Dekl. 83, Havers 
Sprachtabu 123f. 
Page(s): 223 



Root / lemma: dous- 
Meaning: arm 

Note: 

Root/ lemma: dous-\ "arm' derived from an archaic root *^^e:/5'hand, arm' (see below).
```


## [2026-09-05T20:07:46.218Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1190,1205p;2205,2225p' KNT.txt\necho \"=== lexicon entries\"\ngrep -n \"hizana\\|hazana\\|hizān\\|hazān\\|zbā\\|zba\" KNT.txt | head -40"
}
```


### [2026-09-05T20:07:46.281Z] TOOL RESULT

```
Lex. s.vv.). $90. PIE fu became pár. Sy, and then Av. sp,
Med. sp, OP s, Skt. gv:
pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; OP nspa- (with Med. sp) in vispaeana-; Av. vispa-, Skt. visva-.
pIE *kyd- in Av. spá- ‘throw, set down’, OP sä- ‘erect, build’, in s-aor. pass. früsah[ya] DSf 27 (etymology not certain!). $91. PIE ghu became pAr. Zhu, and then Med.
and Av. zb, Skt. he, but OP z; the OP texts
have one example of the Median value and one of the OP value:
pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
OP Лапат for acc. hizénam ‘tongue’, Av. hizvà-, Skt. jthod-; see Lex. s.v. for details. $92. PIE ks became pAr. С and reverted in
Indie (Skt.) to kş,! but became plr. £$, shortened
to š:
pIE aor. *e-peik-s-m, OP niy-apaisam; cf. other forms in Lex. s.v. paib-.
i For the phonetic value of -b- in -zb-, sce discussion by Debrunner, IF 56.176-7.
692.1 If pIE Ё in ks had become the usual pAr. sibilant $, it is difficult to see how the $ could have yielded the stop in Skt. kg. Some other development of Ё in pAr. before s must therefore be assumed.
593. PIE $t (from Ё or ў + f) became pAr. &, and then plran. š, OP and Av. š, and Skt. st; these clusters are seen in derivatives with a t-sufhx: pIE *pik-to-, OP ni-pista- ‘engraved’; *peik-t- in
inf. ni-paistanaty; for cognates, see Lex. s.v.
groups.
I. Agency nouns with suffixes pIE -tor- and E! -ler-, showing ablaut variation in the declension; à E the nom. sg. has the long vowel, which is com- 24 monly extended to some or all of the other case- $ forms: Lt. dator, gen. daiór-is (6 throughout); 4 Gk. дотор ботор-оѕ (0 only in nom. sg.) jerjp d Sornp-os, дотћр dwrnpos (ë throughout except in voc, 4 | sg. дате); Skt. data, acc. dülirum, dat. datré, 4 loc. dätári, etc. OP has nom. sg. ja^tà ‘slayer’, 4 Av. Janta, Skt. hantå; dauštā ‘friend’. ОР асе, 4 framatüram ‘lord’, with extension of the long $ vowel of the nom., and the antevocalic value of 3
the ace. ending ($67.10).
II. Words of relationship had suffix -ter-, пот, -tē or restored -tér, other cases -ler- or -ir-. OP has nom. pita ‘father’, Skt. pita, Gk. татр, Lt. pater; also in cpd. hama-pità ‘having the same father’,
OP nom. mätä ‘mother’ in hamaté ‘having the 4
same mother’, Skt: mata, Gk. (Dor.) ратар, Lt. mater. OP nom. brátà ‘brother’, Skt. bhraid, Gk. ¢parno ‘clan-brother’, Lt. frater! OP gen. pica’, Gk. татр, Lt. patris, from *potr-os or -es, unlike Skt. pitis from *potrs.
v M8T. Tux -n- Srems тч OP: these also fall into Г |
several groups.
Those with suffixes (Aryan) -man- -van- -an- (pIE vowel -e- or -o-) had nom. in -mā -vā -à: OP {ашта ‘power’, stem tauman-; artàvà ‘blessed’, GAv. ašavā, LAv. aSava, Skt. stand, ef. GAv. acc. a$avanom; азб ‘stone’, cf. LAv. asanga- in epds,, OP aéa*ga- ‘stone’; zsacapava ‘kingdom-protect- ing, satrap’, with stem -pdvan- as in Skt. (Ved.) lanü-pàvan- ‘person-protecting’. Acc. with exten- sion of the long vowel, in OP asmdnam ‘sky’, ef. aec. Lith. dkmen; ‘stone’ and Gk. ёкиора ‘anvil’ with -mén- and -món- respectively. It is uncertain whether ace. h*zünam (for hizdnam) is an -an- stem with the long vowel, or an -dna- stem; at any
rate it is an extension of the stem seen in Ау. . hizvd- (see Lex. s.v. hazdna-). Neuters with suf- '*
fix -men- have nom.-ace, in the zero-grade -mx;' асс. OP nama, Skt. пата, 14. ndmen, from *nomn.
LOP hamapité and hamátà do not distinguish, and
cannot distinguish, between the two vocalisms seen in Gk. ддохаттр and ӧротётор; but the -ör forms are those proper in original compounds.
§187.! ОР c#8*m* із notyto be read cama as а neut. -n- | {
REPE
DECLENSION OF NOUNS 65
The stem XSayarSan-? has the regular nom. Xšayäršā, but the other cases are remodeled to the type of Auramazda, acc. -dam, gen. -düha (§185.1V): ace. XSayarSdm, gen. [XSaydr|8aha, with late genitives X SaydrSahyd (§57) and XSayar- Муй (А?Не), with the medial -d- of the other cases. On forms of ArtaxSaca-, see $172.
Of the other forms, OP baršnā is inst. sg. to stem barSan-, cf. Av. inst. barasna to barazan-, Skt. rüjfi to rajan- ‘king’. OP пата is probably а suf- fixless loe. пата". Inst. pl. taumants and arasani$ are analogical for -abis, since the paradigm would have been nom. -ana?, gen. -andm, inst. -abi& (from -n-bhis) 3
OP nom. manauvis is probably for *manas-vi, nom. to -vin- (ef. Skt. nom. bali to stem balin- ‘strong’), with added nom. -s.t
"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
І. Nom. парӣ = пара’, Skt. ndpat, from pIE *nepot-s with Aryan loss of last consonant of the final cluster; or = парӣ? from a remade Iranian *napäs seen їп Av. napa.
=== lexicon entries
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
408:$11. Diaugcr MIXTURE IN THE OP VocaBU- LARY: it is difficult at times to decide what is genuinely OP and what is borrowed. Of the two words for ‘good’, nazba- is a religious term, and vatu- is found only in proper names. Of the two for ‘earth’, zam- (which would have Med. 2) appears only in the form zm-, which is phoneti- cally OP as well as Median, and occurs m one proper name and in an official term for execution with torture; būmi- occurs chiefly in phrases of official character, but is used also in DSf to de- note the earth which was excavated for the palace of Darius. On some other points, the usages of Pahlavi seem to inform us: nom. hau» ‘he’, «yam ‘this’, prep. hadd ‘with’ belong to Pahlavi of the Northwest and not to that of the Southwest, and thus are shown to be borrowings from Median.!
1197:pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
1496:pIE ghy: patiyazbayam, Мейтат.
2468:Also, with strong-grade roots: OP kana- m imf. avakanam; gauba- in mid. gaubalaty, imf. agau- бий, pl. адамба'{@; tazša- m mid. ha”tarSatary, imf. hamataxsaiy hamataxíatà hamatazsa"td, yauda- (Av. yaozai), in imf. ayauda! ayauda’, pte. yau[da"tim]; apparently vaja- in avajam, татда- in imv. razbatuv; perhaps máva- in 3d pl. imf. mid. [am]ávatà.
2484:pIE *óhuà- (vowel quality indeterminate) and *Ghya-: pAr. Zhya-ya- ‘call’ in Skt. hváyati, OP imf, patij-azbayam.
3014:(d) Clauses of directly quoted statement as ob- ject or subject, normally without introductory conjunction: quotations of fact, with past parti- ciple or imf. ind., depending on xindsdhy and агай basdtiy, DNa 42-7; of volition, expressed by the subjunctive, depending upon amaniyaiy, DSI 3f; of wish, with the subjunctive or injunctive, de- pending upon maniyahaty, DB 4.39, DPe 20f, XPh 47; of negative command, with mà and the opt., depending upon patiyazbayam, XPh 38f; of direct question, with the imf. ind., introduced by ciya- karam ‘how many’ which is preceded by a superflu- ous tya ‘that’, and depending on тапталат, DNa 38f.
4593:38 m : viyakanam : uta : patiyazbayam : daivā :
```


## [2026-09-05T20:08:04.036Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 413\" POK_full.txt | head\necho \"=== ghau\"\ngrep -n \"lemma: ghau\\|lemma: g/jau\\|g/jau-\\|ghau-, ghaua\\|rufen, anrufen\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:08:04.100Z] TOOL RESULT

```
36085:Page(s): 413-414 
=== ghau
32325:Root / lemma: ghauo- 
36023:Root / lemma: ghau- ghaua- 
36027:Alb. shows that Root/ lemma: ghuen-: "to sound' derived from Root/ lemma: ghau-, 
38157:Alb. shows that Root/ lemma: ghuen-\ "to sound' derived from Root/ lemma: ghau-, 
39846:Root/ lemma: gh^ena^ woman, wife, *goddess' could be a truncated Root/ lemma: ghau-
```


## [2026-09-05T20:08:05.106Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT hizva col 1815\"\ngrep -n \"hizv\\|hizu\\|1815\" BRT.txt | head -40"
}
```


### [2026-09-05T20:08:05.163Z] TOOL RESULT

```
=== BRT hizva col 1815
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
6072:^aoi^anäil  hizvascä  (sd.)  'sahyä  nqsvä  i  vaahJus  'sähe  b/njä  dalnayä  vaahuya /a^tf  Y.5/.  13*'.  p)  Abl.mitÄa<5i 'demJY. ,35.  i;  f5. 1,  6'2,  lo,  A.J.4;  —  'sähe heiligen,  göttlichen  Recht  gemäss,  ent-  { vahistahe  *6fn)ja  F.  48.  y)  GS.  mit sprechend'  (s.Iabe):  nnii  alr>a  ahB(s&.)  ratav  (sd-, auchfdSt):  aäbyB  rattifys ySt vistö  'sältU  hacä  Y.  25.  6;  27.  13,  38.  i ; !  h^titi  'sähe  ratavS  %rayatea  %risqsca  ysi
10635:•  j.,  g.  xrafstra-  n.  i)  im  gAw.  'wildes Tier,  Raubtier":  atibyS  mas  äsä  syasdat (sd.)  yentat  ahmat  aurunä  'rH  (AP.)  Y. $4.  9.  a)  im  Plur.  als  Bezeichnung  für die  nicht  sesshaften  Religionsfeinde  und deren  Gölter,  sva.  'Raubgesindel':  anä mq'ira  maxist?in  väurüimaidl  (sd.)  Tä (A'P.)  hizvä  Y.  28.5;  —  pari  *vä  vJspäis pars  vaox?mä  dalviliscil  °räis  maSyäis^ä "losgesagt  haben  wir.  uns  von  allen  Xraf- stra^ (allem  Raubgesindel),  den  Daivas wie  den  Menschen"  "  Y.34. 5 ;  verwendet  Y. ig.  2.  2)  im  jAw,  Bezeichnung  fUr  alle schädlichen  ((/iZÄischen)  Tiere,  bes.  der niederen";  paitUtätie  a/astaca  zBüdiftaca apayantamaheca  a?prahe  mainyius  °ra Yt  21.1;  —  duye  Saite  kahyäcit  ar>rö.- mainyavanqm  "ranqm  ava.janyäl  V.  16. 12;  —  ähva  vyar?hähva  (sd.)  e^mB  'ra ham.bavainti  yim  tnasyäka  spis(sd.  tiqma aojaitt  V.  z/. 3;  —  *maxSiMhrpa  ..*akara- tum-driwyi  (sd.)  ya%a  taehdistäiS  'räis V.  7.  2;  —  Y.  ig.  2:  s.  unter  1.
11955:—  "nvS  vlspayä  drvatätim  °nvS  vTspayä vazdvar)  Yt/4.39;  —  imfm  'hwqm  ..yänim haema  Jailyemi  drvatätim  atiiAas)  'nvS.. darrjB.jltlm  ustänahe  Y.p.19;  K.i.Z;  — 'nuyäsca  paiti  druaiats  Yt.  13. 134;  —  aha r0  tarn  sraos'a  . .  zävar»  daya  AitaHbyB drvatätitn  °nubyu  ".  ,  Kraft  unsem  Ge- spannen, Gesundheit  unsern  Leibern"  Y. j7,  i6;  —  däl»m  te  'nuye  ^annd  'Yt.iy. 12;  15;  — ya>a  tW . .  ifä'^ravaiils  'nvö +,iwi/J  (Sp.  274  IL)  Y.  60.  11;  —  vohü uxsyä  (sd.)  manan&ä  .  .  ui'tä  'nUm  Y. ^.10;  —  haomü.artharstahe  (sd.)  hizvS mq%rS.hitahe  (sd.)  °nvd  A.4-5i  —  im Gegensatz  zu  gaihä-  (Sp.  477  in.),  urvan- usw,:  akmäi  nfmaahl  ävaldayamaidi  gal- %^slä  'nvascä  nipätayaicä  , .  Y.  56".  2  j  —  yö nS  . .  iririx/äite  gaghanqm  .  .  °nunqm  Y. 65, 7 ;  —  frähatiia  asake  gaghä  .  ,  asahe °nuy!  Yt,  6.1;  —  forasayäi  (sd.)  aibi %waha  gai'iäAa  -nuHcä  Y.  43.  T,  — 'nvagca  * kaosravar3h»m  untnaija  dan^tm havanium  F.^h;  —  cim  ,  .  qst>m  isaiti 'rwa  cim  uruna  Aog,  4^;  —  vJspS  gai- %isca  -nvasia  azdsbisca  .  .  iistänqs^a urvätamca  . .  pairica   dad>mahl  Y.  55.
22204:Rede:  at  J  (Sp.  11  m.)  vaocat  ahurS  .  ..■ nüif  .  .  Y.  2(J.  6;  —  yezica  vaocät  alsa  yä kaine:  faä:r»m  isd.)  alm  ..varsta  V.75. 13; 13.  a)  mit  Dat.  der  Person:  sat  vao- iät  ratul . .  mazJayasnagibyS:  maadayaina (Vok.)  ..  V.tf.  II.  3)  mit  Objektsakk.: ya'hä  iü  T  *ahuramazää  mSnghaca  vaocasifl däscä  varfscä  ya  vohu  aha  .  .  V.  J^.  4; —  /a(  0/  vainmaidi . .  hyat  I  mainimadicä vaocdimäcS  vsnzimäiä  yä  .  .  vakisiä  Y. JJ.  3;  —  tarahuslrahe  .  .  paoiryai  vohu mamnanai  .  .  vaokuSe  .  .  vävinzuh  Yl 13. 87  f. ;  —  ySi  nsii  ih3  mqhnm  vanssnti (sd.)  ya%S  Tm  mSnai^a  vai>ea(K.onj.)£ä Y.45.  3i  —  ai  sl  i"Ä(ADn.)  vaxs'ya  (iS.) mazdä,  vidull  zT  na  mruyai  (Sp.  1193  u.) Y.5/.8.  a)  zugleich  mit  o)  Akk.  der Person:  at  tä  vaxsya  üints  (Sp.  29  o.)  . . mazda^a  Y.  ?o.  t.  ß)  Dat  der  Person: y7  mlH  viäva  vaocäl  haihim  mähnm  .  , ampnitaias{sd.)ca  Y.^1.6;  —  *>'?*'  '''^' vTdvä  mazdä  vaocat  Y.  1^5. 3;  —  masda at  mSi  vahilta  sraväslä  .  .  vaocä  (Imp.) tä  .  .  asacä  iiudfm  (sd.)  Y,  j4. 15;  —  mit finalem  Inf. :  tat  nS  mazdä  vldvanöi  (sd.) vaola  hizvä  %'waAya  araks  Y.31. 3 ;  5 ;  —  in pass.  Wendung  :_)'as'4vö  mazdä  %wSi  va^äl daena  Y,  44. 11;  —  »n/  mdi  tneBcam  ^  vata- hJuI  va/u/(sd.)  manarahs  Y.  48. 9.  3)  mit wie?-Adv.slattObj.:  (is  mainyü  mamanäiti , .  vaocätari . .  vävjnzätarS  Y.  ly.  4 ;  —  *yal neit  yava  mihS  mamne  .  .  vavaü  .  .  va- variza  P.  iS;  —  tat  hwä  pinsa  (sd.)  fnS
22748:kaus.  BedeuL  'überzeugen,  ■aitisiv',  Med.  I J  MäfyJ' .  .paruv  *%aäayä* . .  nailim  vama- 1 vätaiy  duruxtain  (sd.)  *maniyätaiy  Bh.  4- S;  —  tya^  manu  kartam  varnavatam  1 "^uvam  mJ/yJ*  *draujTyähy  {^A.)  Bh.  4.  6; — . .  nüram  %uväm  vamavaiSm  ty<^  mann  \ kartam  ai'a3ij(sd.)..Bh.4. 10.'!  a)gAw.  | insbes.  vom  Überzeugen  auf  religiösem  1 Gebiet,  sva.  'zum  Glauben  bringen,  be- kehren'; nur  Int.,  Med:  tat  nS  ..  vaolä^ kisvS .  .y3  jvantd  vispSng  väuraya  ( 1 SOM.) ". .  auf  dass  ich  alle  Lebenden  überzeugen  , kann"  Y.jr.  3;  —  >43  (näml,  viääitis)  zT- pourül  ispnts  väuraitl  "sie  wird  ja  noch ' viele,  die  hören  wollen,  veranlassen  sich zu  bekehren"  Y.  47-  6.  ")  'bekehren zu  — '  (Akk.) :  ana  mahrH  matist>m  väitröi- maidl  xrafsträ  hizvä  "mittelst  dieses  (Ver- heissungs)  Wortes  wollen  wir  die  Xr.  (das Raubgesindel)  mit  unsrer  Zunge  zu  dem bekehren,  was  das  grösste  ist"  Y.  28. S-  {varänJ  Y.j^j.  4:    lies  livarünT,    s.
25489:•  j.  iristay-  f.  'Sterben':  nsit  ki  anyU urva  haom  urvämm  paiti  'ta  (LS.)  bqzaiti "keine  andere  Seele  wird  seiner  Seele  Hilfe leisten,  wenn  er  stirbt"  V.  jj.  g;  g;  — yezUa  hi  narU  °ta  hva  hizva  uxtam  väüm nizdasca  narS  dai>hr»m  paiti  dyaiti  Vd. 2'>;  2.
28735:dädansa  .  .  äat  .  .  pattyaoxta  'mö  .  .: aztm  ahmt  ..  'mS  a/ava  darao^ö  Y.g.  1  f.; 3,  19,  70.9".  77.3,  10.  57-'9.  VtÄ33, g.  17,  10.  88,  77.37;  —  imat  nmän^m  . . yat  'mahl  alavazanhB  Y.  70,  i ;  Ä  9,  Yt 20.0,  3;  —  uHa  te  yS  iflt  aojataha  vasB.- xsa%rS  ahi  'ma  Y.g.xy,  27,30,  70.14, 77.10;  —  US  mW  pita  'mai  drao>W  frSr»- naot  ahurS  maidä  .  .  hanuharme  *mal *hizvS  hSyümca  dai^tvm  Y.  77.4;  —  %w!t- /gm  (7  gfuf  fr^wpnsS  tanciUäi  'mäi draonü  mä  'iwS  'mS  bandayäi  ya%a  .  . bandayat  .  .  /raaraiyurum  Y.  7J.  7;  70. 15;  —  -mö  timcil  yim  kinsaalm  apa.- xsahrtm  nisäoayat  ys  .  .  Y.g.  34;  —  'mB täscit yä  haininS  änhaire{%6..)  darrfpm  ., *pai%lm  räh3m(iA^ca  baxiaiH  Y.g.  23; 33I;  —  uyräi  d/tmöii  upamanäi  'maheca ma^raheat  asaonaica  zara%uitrahe  Y.8. 1.  [Y.  70,  63:  lies  haoma.'.]
30062:•  j.  hitö.hizvah'  Adj.  'dem  die  Ztmge
30093:•  j.  hizuxda-  Adj.  'beredt''':  yvänS  . . yS  .  ,  danrS  .  .  'os  Yt.  15. 40.
30095:•  j.  hizu.dräjah-  Adj.  (auch  fem.)  i)  'die Zunge  herausstreckend':  "/?(NStn,",  näml. asti  spa)  ya^a  ap3r)näyus"ei  (der  Hund) streckt  die  Zunge  heraus  wie  das  Kind"
30100:•  j.  hizu'ma-  m.  'Mund'":  upa  vH  nastts ralhwät  narahanat  .  .  easmanat  .  .  'mai haca  V._j.  14.
30102:•  j,  hizvah-  n.  'Zunge':  vaim  ava.mivä- maM  (sd.)  'vas^a  pivasca  V.1S.55.
30104:•  j.  hizvä-  f,  'Zunge' :  'va  F._J  e;  — vihrkai  °vqm  daläiti  yS  azrasdäi  (sd.) *mq^r?m  caste  N.  ly;  —  'vam  akurake mazdä  yazamaide  fravaksi  ma%rahe  sp>n- tahe  Yl  /.  aS;  —  daya  mi  .  .  inastim spänS  xhfiwTjm  (sd.)  'vqm  urune  un Y.  62.  4;  —  yat  .  .  astt  ganrna  ä^an^a (sd.)  siamarum  v3  'mm  (näml.  des  Hundes) v3  apa.äaiat  V.15.  ^'t  —  'vam  frSnnagt Sl./i-.6Z.
30106:•  j.  hizvirana-  n.  —  ?  — :  ar^dvlm .  .yqm aztm  yö  a/iurS  tnazdä  'na  uebaire  /ra- ddhäi  nmSnaheca  .  .  "A.,  die  ich,  AhAf., . .  hervorgebracht  habe,  um  gedeihen  zu lassen  Haus  und  . ."  Yt.  5. 6,  Ny.  4.  7.
30712:•  j.  "^hvarStay-'^  f.  'gutes  Tun,  Handeln': mananhasca  ^humaiti  hizvasca  *hBxti tastayascä  'ti  *ra^wyg.varJN  (sd.)  Y.28.
```


## [2026-09-05T20:08:16.406Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=30090 && NR<=30110' BRT.txt | grep -o \"18[0-9][0-9]\" | head\necho \"--- context lines with col numbers\"\nsed -n '30085,30092p' BRT.txt\necho \"=== zbā\"\ngrep -n \"zbä-\\|zbā-\\|'zav\\|zav-\" BRT.txt | head -20"
}
```


## [2026-09-05T20:08:17.356Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN tongue 4.27\"\ngrep -n \"4\\.27\" SYN.txt | head -20"
}
```


### [2026-09-05T20:08:18.779Z] TOOL RESULT

```
1816
--- context lines with col numbers
PPM.:
dby  Google
1 8i  s  hizü-  -
•  h  8t  P-  hizü-  m."  'Zunge':  I  uta  näham Uta gausä  Uta  'zuvam'^ fraJanam'BA\.2.iy,
—  hariuhanne  *mai  *=3i;j3>  "die  beiden Backen  sammt  der  Zunge"  Y.  J/.4;  — /taomB.anhar^toAe  i^A.)  'evS^^  A.4.5;  — •zvffii  danhanha  "mit  Zungenfertigkeit"  Ny. 1. 1 6 ;  —  'sva  mrsSii  hüxttm  . ,  zastalibya vansa  hvarstint  Aog.söf.;  —  tai  ttS  .  . vldvanni  vao'a  'zvä  ^wahya  anhS  ". .  mit der  Zunge  deines  Mundes"  Y._J/.  3;  — mananhasca  *humaiti  'vaüa^  *hüxti  zasta- yasca  ''hvarsti'S.28; — kva  'w«  V.3,sPüZ., VdsjP.^j;  — ■  na^a.cit  mihs.aojSn!^ (sd.)   alSqm   a^aipai'iya  •sjiS''''   Yt  Z^.  95;
—  'gvSi>  raiiiSm  {sA.)  stfft  maAyä  Y.^0.6;
—  irpiuxhai  vacanhqm  xsayamnB  (sd.) •w?i>  vass  Y.31, 19.  a)  gAw.  IS.  und IP.  sva.  'durch,  im  Reden,  Sprechen'*'; ySi . .  aiiitnim  varyäm  (sd.) . .  o^ilt/  'tubls Y.  49-  4i  —  urvä  .  ,  x^äii  ^aohanäil 'zvascä"'  asahyä  nqsvä  pa%S  "die  Seele  , ., da  sie  in  ihrem  Tun  und  Reden  vom  Weg des  Ai^a  abgegangen  ist"  Y. 51.15; '"'zvä'f>  av?r>ts{si.)  Y.^lj.  i;  —  anä  mq^rä mazist>m  vüurSimaidc  (sd.)  xrafstra Y.  atV.  5,  a)  in  Verbindung  mit  »jcob-: ydi  rJ  fyao%anäis  särffitf  (sA.)  ..  *'zv3^^ uxlaii  vaivhJus  manavAs  Y.  5/.  3;  — vahUtfm  'svä  ux%äis  , .  }>änü  . .  tastsibyä syadkatiiJ  v?r3zyat  (sd.)  Y.  47.  2.
KompA.  1  Ableit.  —  S.  auch  Aitvä-  l.  —  Vgl. np.  labäH,  3.1.  jiMia-  f.«.  —  Pü. :  Ausvän.  — ')  Das  muk.  Geschlecht  ist  i.uf^lig,  wiid »ber  durch  alle  entscheidenden  Sielleo  ver- bürgt;  IF,  lO.  20z.  —  »)  Unsicher,  da  der Anfang  des  Wort»  lersiört  ist;  BB.  14.  245.  — i)  GS.  —  4)  LS.  statt  IS. ;  S  409  mit  No.  3.  — S>  S.  tasUiiyä;  Sp,  1685  m.  —  *)  Der  LS. dient  als  IS.  {s.  No.  5)  und  wird  im  Sandhih nach  dem  Muster  des  gleichlautenden  GS. (».  N'o.  4)  behandelt;  Bthl.  IF.  10.  102.  — 7)  So  K4;  NA.  :fenJ.  —  S)  NA,  aJä.M!vi; s.  aber  Pt  4  usw.  —  9)  Worüber  luletit  Colutz OrStudies  of  iheOr.Cluh  of  Philadelphia  167, BLoouFtSLD  AJPh.  f6.  426,  Wn.  AiGr.  r.  161, 163,  Fay  JAOS.  i6-  ccxxvm,  Pederson  KZ. jÄ  201  und  -  mit  treffender  Kritik  -  Uhlem- BECK  WAiSpr.  101.
=== zbā
5388:auniäa.bäzav-
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
7662:■»«zav-
7692:•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
7697:"arazav-
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
8118:•  j.  Ujra.bäzav-  Adj.  'starkarmig':  {iiit^r?) ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]
8660:•  j.  uzbäta-  Adj.  (fem.  'ta-),  PPf  P. :  s,  zav-. w+^-.  S  ja*  n.  36.
8661:•  j.  uz-bäzav-  Adj.  (auch  masfc.)  'die Ajme  emporhebend';  °zäus  (NS.)  fiaiii attunxllm  (sd.) /ravazai/e  mi^rS  Yt,/o.ia4.
9367:Igibt,  Gesetze  vorschreibt':  mi^tTm  .  . 'zavAsm  tylxamm  Yt.  /o.  6 1 ;  —  *frazain-' tlm  °sqm  (ASf.)"'  vyäxanam  Y.  ^s.s,  F.5,
11601:•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
12894:')  Ein  Schönheitsieichen;  vgl.  Artaxerxts  L Beiwort  Longimaiios,     S.  in  dar>-fö,bäzav-.
12906:darttgö.bazav-
12909:•  g.  darsgö.bäzav-,  j.  dar^ö.bäzav- Adj.  (auch  fem.)  langannig':  hukmlB  ahi
17125:•  j,  bäzav-  m.  i)  'Ann'  der  Menschen  und       '  5'  '*     ..  ..r,    _  .   i-n^    ,  *j:  -.^  « i-M^         i-,   -r  ,/TL'      .    Tc-v.i   j   <■      ■         Komp.  mit  ND.  im  l,  Glied;  s.  ituan-  A. Gotter:  ÄJtJv« '«i'jfLb.  als  IS.)'' j(jn«aiv)        .     /_      ■      v  ^      .  j-     (^    .     -       j ./aÄ«.-«.ä*te.«,*5,"milde,»li,JimAnn  •   !■   bs^-s-aolah-   Ad,.    Oak    m    den «.d  dem  «cht«,  mit  de«,  rechten  Ar»  m,d  '^f  "»  *^'  "^'  '""• '  -»ß-»«. . . deoh»kei."V.j.>5i-j...,yü!j»,,;7™i,  V»«"!'"  '?*''/'/?;  \t.,o.,y,-«-a^,aAr
17130:^««fcr)  Anne"  Yt5.7;  *F.^g;  — jwM^  .  j.  /r,!^^^«.^  biSe  buya,te  in%baoye  gräfa d^^aat'zava  fragTTW^i  ,m>rö.aüja»hö  tuy^,  y^iS.%^:  -?-. (sd.)  \t/0.  104;  — V«   *'zava'^\X.lO.       Angebt  ■Gefingniswirter' (Sp.)  od«  'GeßoE- 4a;  —   Ät»   hl  'sava  gmn-ayat  Ytj.Ös;       nis'  Jl-sti). —  havalibya  'tuiya  Yt.  JJ.  107 ;— i?mcii . .   ,  g.  »,b^  b5»dtlä""  Y.5J.4. hangrifhmtw  *fairi^paya (^A.)  'suu'e(JD.)        KettungsIosTerderbt— Pa.imiuötü'ür imH*«, Yt/0.105;  IJ.46;    —   yal    hl   äa>at  .  .        «rl.;  a'JnJ«.*  .  w>>.  —   •)  Pl4.  K5:  i}fi  ii; •iuwe  (DD.)  aejo  Yt  16.  7;  —  «/«  a^fV«       »■  ^  —  "  S-  No.  i. '«'rf  (GD.)    ao/j   .  .   öaraM   Yt  Jo.  23;  •   g.   bsndva-  m.  EN.   eines   der  tara- 14. 29.         a)  bildl.  sva.  'Stütze':  viStäspahe  l^a-^nschen  Religion  feindlichen  Fürsten":
20163:•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
20395:•  j.  'msrszav-  n.  'Wirbel'  des  Halses  und Rückens:  yavata  . .  tii/ainti  °tu/a  ttünB gayehe  'sula  x&  uimnahe  "bis  er  entzwei
```


### [2026-09-05T20:08:18.828Z] TOOL RESULT

```
=== SYN tongue 4.27
866:NHG dunst ‘vapor’), ME, NE dust, all fr. extensions of the root *dheu- seen in Skt. dhi-, dhu- ‘shake’, Grk. dtw ‘Tage, seethe’, Skt. dhiima-, Lat. fimus, etc. ‘smoke’. Walde-P. 1.840, 846. Falk- Torp 163, 168. NED s.v. dust. Prob. fr. the same root Toch. A for, B taur ‘dust’ (G. 8. Lane, Language 14.27).
5266:‘hear’, ‘smell’, ‘speak’ (or ‘eat’), ‘walk’, and so far as some cognates of the for- mer are applied to function this is prob- ably, and in most cases certainly, sec- ondary. On the other hand, the deriva- tion of the IE word for ‘tooth’ from the participle of the IE root for ‘eat’ seems too obvious on the formal side to be dis- carded, though even this situation may possibly be the result of a secondary as- sociation (see 4.27). The application of words for ‘tongue’ to ‘speech, language’ is almost universal, but the latter use is always secondary.
5490:3. Ir. adarc, NIr. adharc, an old con- tinental loanword with Celtic suffix (cf. Gallo-Lat. adarca ‘spongy growth on sedge’) fr. Basque adar ‘horn’. Walde- H. 1.12. Pokorny, Z. celt. Ph. 14.273, 16.112.
5996:ODY; BODILY FUNCTIONS AND CONDITIONS 231 Pas 4.27 TOOTH . tunpus Lith. dantis Sous Both ee Lett. zuobs Gtk Sayre Dan. tand ChSl. zabit NG dens Sw. tand SCr. zub Lot. aente OE tap Boh. zub "4 dent ME tothe Pol. zaqb gp. dient NE tooth Russ. zub Rum. dinte Fy Du. tand Skt. dant- Ke det, far ad) OHG zan(d) Av.  datd- dantan- Nir. fiacal (a? MHG zan(t) W. oer NHG zahn la im F - + of the words for ‘tooth’ belong 2. Ir. fiacail, NIr. fiacal, deriv. of a Pe eeiiarited group. rare fec ‘tooth’ (Windisch 538), NIr.
6878:Br. danta, fr. dant ‘tooth’ (4.27).
8424:‘move, glide’). Cf. also Toch. A tsuk- ‘drink’ : Lat. dicere ‘draw, lead’, etc. Walde-P. 1.874. Feist 125. G.S. Lane, Language 14.27.
10098:6. ON pofi: pefa ‘press’, cf. pof ‘crowd, throng’: Skt. vi-, sam-tap- ‘press’. Hence, or at least fr. some Gmc. form of this group, Lith., Lett. taba, OPruss. tubo. Falk-Torp 1250. Miuhl.- Endz. 4.277.
15132:as something ‘cut off’ or ‘trimmed’. H. Petersson, IF 24.277.
15344:3. Ir. indéin, indeoin, NIr. inneoin, W. ein(g)ion, Br. anneo, fr. a epd., first part Ir. ind-, etc., second part dub. Thurneysen, IF’ 4.274 f. Pedersen 1.114.
18780:6. Lith. turéti = Lett. turét ‘hold, keep’ (also ‘have’, dial. ‘possess’, cf. Miihl.-Endz. 4.270), OPruss. turit ‘have’ : Lith. twertt ‘fence, inclose’, nutvertz ‘seize’, Lett. tvert ‘grasp, seize’, ChSI. za-tvoritti ‘close, inclose’, Walde-P. 1.751.
22191:Lett. twou, fr. adj. tuvs ‘near’ : Lith. tuvt ‘at once’, OPruss. tawischan (ace. sg.) ‘the nearest’, etym. dub. Miuhl.,- Endz. 4.276 f.
22420:Skt. rudh-, ruh-, Av. rud- (pres. 3pl. Skt. rodhanti, Av. raodanti) : Goth. liu- dan ‘grow up’ (of seed, Mk. 4.27), OK léodan, OHG ar-liotan ‘spring, grow’ (of plants), ON lodinn ‘grown over, hairy’. Walde-P. 2.416.
24259:1, With preposition. Grk. ava pets or xara tpets; It. a tre, Fr. a trois, etc. (but more commonly with repetition, below, 8); Goth. bi twans ‘by twos’ (I Cor. 14.27; but Mk. 6.7, Lk. 10.1 lwans hwanzuh, as if distrib.), ME by thes, NE by threes, in threes, NHG zu ee Du. bij drieén; Lith. po tris, ii “A rim; ChSl. po trim, SCr. po
24261:. tae with or without ‘and’. ‘Ma ula ‘one by one’ (Soph ph.), but a only in late times, e.g. in NT “_ 6.7 (= ava 860 Lk. 10.1, 2, Cor, 14.27), rpia rpta POxy. tu, als ae Tpets; late Lat. duo et 2399). a uo duo (cf. Arch. f. lat. Lex. an a rt ha tri; OF brim and prim # Gram, for Lat. terni), NE Th ne ee, NHG drei und drei, ON
24304:14.27 Finis (vb.) 14.28 CEASE 14.29 Reapy 1431 Anways 1432 Orren 14.33 Sonetmmes 1434 Never 1435 Acarn 1441 Day M42 Nicur Xpbvos Katpbs Bom: Osa? em pus Dan * "tempo 5 : . lemps OE Rim, jemno ME » limp, vreme 7, mm, aims am, Brat i aa ome Prud OHG amzer, pred MHG NHG “ord fo e
25001:Grk,  7édos, reAcvTHT Goth. andeis Lith. galas, (pa)baiga NG rédos ON endi, lok Lett. gals, beigas Ist, _finis Dan.  ende, slutning ChSl. kontéina, konict . fine Sw. dnde, slut SCr. _konac, svrSetak Ir, _ fin, bout OE ende Boh. _konec Sp. fin ME ende Pol. = koniec Rum. sfirgit NE end Russ. konec ,  cend, dered, deod Du. einde, slot Skt.  anta-, pranta- Nir. detreadh, crioch OHG enti Av. Graosli-, dwarasah-, W.  diwedd MHG ende karana- Br diwez NHG  ende, schluss Nouns for ‘end’ in the temporal sense, | Walde-P. 1.832. Ernout-M. 363. the opposite of ‘beginning’, are in large | Walde-H. 1.503. measure the same as those used for ‘end’ Rum. sfirgit: vb. sfirgi_ ‘finish’ Ma spatial sense, for which see 12.35. (14.27).
25004:4, ON lok (pl. or sg., also epd. enda- lok, endilok), also ‘lid, cover’ : ON luka ‘shut, finish’ (14.27).
25012:14.27 FINISH (vb.)
25013:SCr. sursetak : sursiti ‘finish’ (14.27)
27709:W. syndod : syn ‘dazed, astonished, astonishing’, synnu ‘look, stare at’, perh. fr. *stunno-, *studno-, fr. *std- in words for ‘fixed, stiff? (ef. NHG staunen, be- low). Loth, RC 44.271 f. '
```


## [2026-09-05T20:08:41.069Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD\"; grep -n \"uzwān\\|uzwan\\|huzwān\\|huzwan\\|zuwān\\|zabān\\|zaban\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB\"; grep -n \"uzvān\\|uzwān\\|huzvān\\|huzwān\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:08:41.135Z] TOOL RESULT

```
=== PHD
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:684:zuwān [zwb’n'] = uzwān.
PHD.txt:836:arm-guard bazabanag.
PHD.txt:2561:language uzwàn, (zuwān).
PHD.txt:3420:reticence paduzwanih.
PHD.txt:3421:reticent pāduzwān.
PHD.txt:4030:tongue uzwān, (zuwān).
PHD.txt:4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
PHD.txt:4738:pāduzwānīh ^O v 19 "tero pāduzwān ir Sr pādixšā(y) (Ou v» оу
PHD_mackenzie.txt:3952:pad-uzwan [p)t)wzw)n            ] reticent.
PHD_mackenzie.txt:5100: uzwan [SN A < A lIn'; 'wzw'n l I M <zw'n, (N zaban)] tongue, language ~1~~ ~
PHD_mackenzie.txt:5867:zuwan [zwb)n l ] = uzwan.
PHD_mackenzie.txt:6113:brassard bazabanag.                    burn (vt.) dazidan, soxtan, taftan,
PHD_mackenzie.txt:7424:reliable awestwar, ostigan.              reticence paduzwanih.
PHD_mackenzie.txt:7425:religion den; v. Mazdaism, heresy;       reticent paduzwan.
PHD_mackenzie.txt:7807:tongue uzwan, (zuwan).                   troop gund.
PHD_mackenzie.txt:8801:padim                        -<'JCU            paduzwanih           ~t""~"..tUQ)
PHD_mackenzie.txt:8802:payidag                 ""VUlt)                paduzwan              tt" ~ l"-'~Q)
PHD_mackenzie.txt:11193:"bimgen                       ,~              bazabanag           \ ~ ~ CU-'ty \
=== NYB
3896:uzvaneh [’wew’nyh], v. pāt-uzvānēh.
4121:vie&hitan [wcyhytn'] to teach: anakéh vicēhīt he announced ill fate 482; han i visp vicēhīt uzvānēh the universal know- ledge of languages 54*7. — Av. (428) kaēd-, pres. cač0- or cinad-; MPrth weyh-; Ghilain 62, v. also cthēnītan.
```


## [2026-09-05T20:08:42.159Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 4.26 TONGUE\"; grep -n \"4\\.26 TONGUE\\|4\\.26  TONGUE\\|TONGUE\" SYN.txt | head -20"
}
```


### [2026-09-05T20:08:42.214Z] TOOL RESULT

```
=== SYN 4.26 TONGUE
5971:4.26 TONGUE
```


## [2026-09-05T20:08:48.377Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5960,5996p' SYN.txt"
}
```


### [2026-09-05T20:08:48.430Z] TOOL RESULT

```
W. guwefl ‘lip of animals’ = MBr. guefl ‘mouth of animals’, etym.? Stokes 335 (vs. 175).
Ir. bus ‘lip’ (rare), NIr. pus ‘lips, mouth’ (derogatory term), whence regu- lar word puisin, W. gwefus (fr. *gwe-bus; or *gwef-us : gwefl?), Br. gweuz : Alb. buzé, Rum. buzd ‘lip’, NE buss, NHG bus ‘a kiss’, etc., of imitative orig. Walde-P. 2.113 ff. Thurneysen, Kelto- Rom. 86.
Br. muzell, fr. Prov. muzel (Fr. museau) ‘snout, muzzle’, dim. of *misus, It. muso, etc. Henry 208. REW 5784.
4. OE lippa, etc., above, 2.
Goth. wairilém (dat. pl.), ON verr, OFris. were, OE weler (fr. *werel) : OPruss. warsus ‘lip’, and perh. through notion of ‘protuberance’: OE wearr ‘callous skin’, Lat. verrica ‘height’ and
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
230 SELECTED INDO-EUROPEAN SYNONYMS
‘wart’, Skt. varsman- ‘height’, etc. Walde-P. 1.266 ff. Feist 545.
5. Lith., Lett. lpa : LG lobbe ‘hang- ing lip’, Fris. lobbe ‘hanging lump of flesh’, NE lob (NED lob, sb.?), etc., with common notion of ‘loosely hanging’. Walde-P. 2.710.
6. ChSI. ustina, SCr. usne, deriv. of usta ‘mouth’ : Skt. ostha-, Av. aosta- ‘lip’, Lat. ostium ‘door, entrance, river- mouth’, etc., all derivs. of word for ‘mouth’ (4.24). Walde-P. 1.168 ff.
4.26 TONGUE
Grk.  -yAdooa Goth. tuggd NG yAGooa ON tunga Lat. lingua Dan. - tunge It. lingua Sw. tunga Fr. langue OE lunge Sp. lengua ME tounge Rum. limbd NE longue Ir. lenge Du. tong Nir. teanga OHG zunga W. tafod ; MHG zunge Br. teod NHG zunge
The majority of the words for ‘tongue’ belong to an inherited group, of un- known root connection, Secondary as- sociation with words for ‘lick’ is shown bysome. Most of the words for ‘tongue’ are also used for ‘language’ (see 18.24).
1. TH *dyghwa- or the like, but vari- ous phonetic difficulties involved. Walde-P. 1.792. Ernout-M. 553. Walde-H. 1.806 f.
Lat. lingua (> the Romance words), with dial. 7 (supported by association with lingere ‘lick’) fr. old dingua (quot- ed by grammarians); Ir. tenge, NIr. teanga, W. tafod, Br. teod (all with un- explained init. ¢; Pedersen 1.88 assumes init. zd); Goth. tuggd, OF tunge, OHG zunga, etc., general Gmc.; OPruss. in- zuwis, Lith. liezuvis (re-formed by asso- ciation with leZiu ‘lick’), ChSI. jezyki,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Boh, reé : ChSl. rittz ‘peak’, SCy. rt ‘promontory’, Russ. rot ‘mouth’ (4.24),
Boh. pysk = Pol. pysk ‘snout? - Boh. puchnouti, Pol. puchnaé ‘swell’, Grk. gucaw ‘blow’, etc. Walde-P. 2.81. Briickner 449 f.
Pol. warga, perh. : OPruss. warsus ‘lip’, etc. (above, 4). Briickner 609,
Russ. guba : Pol. geba ‘mouth’, ete, (4.24), with shift to ‘lips’ in pl. guby, whence sg. in same sense.
7. Skt. ostha-, Av. aosta-, see above, 6,
Lith. lLesuvis
Lett. méle
Chl.  jezykit
SCr. jezik
Boh. jazyk
Pol. jezyk
Russ. jazyk
Skt. jihua-
Ay. hizva-, hizi-
ete., general Slavic (all with unexplained loss of init. d, as in Lith. <lgas ‘long’ for *dilgas); here also (with metathesis) Toch. A kdntu, B. kdntwa (Pisani, KZ 64.100 f.; Benveniste, Hirt Festschrift 2.235).
2. Grk. yAdéooa, Att. ydAarra, Ion. yAaooa : yhwxts ‘point’, yhdxes ‘beard of corn’, outside connection dub. Walde-P. 1.662.
3. Lett. méle, etym.? Mithl.-Endz. 2.614. Berneker 2.72, 74.
4. Skt. jihva-, Av. hizva-, hizi-, OPers. acc. sg. h(i)zbanam (for reading, cf. Kent, Language 19.226 f.), NPers. zaban, all as if fr. an IE *sighwa- (init. s > Iran. h; Skt. 7 by assim. to follow- ing palatal), and so possibly a blend of TE *dnghwa- (above, 1) with some other word. Barth. 1815 with references.
Digitized by Arya Samaj Foundation Chennai and eGangotri
ODY; BODILY FUNCTIONS AND CONDITIONS 231 Pas 4.27 TOOTH . tunpus Lith. dantis Sous Both ee Lett. zuobs Gtk Sayre Dan. tand ChSl. zabit NG dens Sw. tand SCr. zub Lot. aente OE tap Boh. zub "4 dent ME tothe Pol. zaqb gp. dient NE tooth Russ. zub Rum. dinte Fy Du. tand Skt. dant- Ke det, far ad) OHG zan(d) Av.  datd- dantan- Nir. fiacal (a? MHG zan(t) W. oer NHG zahn la im F - + of the words for ‘tooth’ belong 2. Ir. fiacail, NIr. fiacal, deriv. of a Pe eeiiarited group. rare fec ‘tooth’ (Windisch 538), NIr.
```


## [2026-09-05T20:08:48.852Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD\"; grep -n \"zb'k\\|zbʾk\\|zb\\`k\\|zbak\\|tongue\" SOD_pages.txt | head -30"
}
```


### [2026-09-05T20:08:50.543Z] TOOL RESULT

```
=== SOD
2773:refuge, followed his capture and death. -He had                 and Uzbakestan have brought to light documents of
10438:     tongue
10446:     root of the tongue
14363:     8wiste se-wist-mik                                                  two-tongued, hypocrite
29933:        498; swntk ^ftk firy "with deceitful tongue",
36363:       zay-xeze ?                                                                (c/)tongue, oral
36383:        tongue
36421:      tongue, language                                                            n p60
38186:evil-tongued     4152                       7041, 7045, 7050, 10323, 10346,     falsehood    11265
39320:root of the tongue   2297                sain   11481                            2877, 10270, 11392
39701:     tongue   2296,11235,11239,11241,               (to transfer     4531                     truth    164, 174, 176, 910, 8515,
39785:two-tongued     3728                     united   1671                            useful 6686
```


## [2026-09-05T20:09:00.122Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10425,10455p' SOD_pages.txt\necho \"=== pdf page tag near\"\nawk 'NR<=10438 && /\\[pdf page/ {l=$0; n=NR} END{print n\": \"l}' SOD_pages.txt"
}
```


### [2026-09-05T20:09:02.064Z] TOOL RESULT

```
        0o)tastc
        TSP 2.711                                                                messenger, envoy
                                                                                 MDii; MDiii; Frag. Len. 117 R2; Ladakh. Insc.;
2295 >zp}p(h) B, M,S                           •yj*?**
     (o)zPaP =*zp>p                                                               Hen. Mittelir. 54; "zVnty* GMS 342 n 1
        flavour, taste                                                     2306 'zyV S                                   j^j^j
        GMS     1505; BSTBL, Vaj. 14; Frag. Len. 35 bl;
                                                                                 humidity ?
                                                                                 (3)zyar ^zy'r
          KG 367; MSP b61, e26; ob. -y, bl6, 60
                                                                                 KG 478
2296 »2p»k(»} B, M, S                                        jlj
     (o)zPak (>zP5k) ©<Av.hizva          =*zP>k                            2307 >zy,rt B, S                               JU^Jj>
     tongue
                                                                                (9)zyart ©<*zgar ^zy'rt, zyrt, jyrt, >zyrt
        VJ 880; TSP 5.32; Sogdica. 5; GMS 93; KG 383;                           at once, immediately
          MDii A-14.6; MSP cl4; Frag. Len. 29.9 >zfl>kh,                        TSP 8.124; BSTBL; KG 358
          KG 399; ob. -y/x, TSP 2.393; pi. -ty MSP b51                     2308 >zy,w => »zYw(h)
2297 >zp>kwyY>k S                               utij^Jc-                   2309 }zY'yr-    S                            0-^O-^>-
     Dzpak-wexe
                                                                                (3)zyer Ozyyr-) =*JYyr-, zy'yr-
     root of the tongue
                                                                                GeOcall, (r<?)name
        Sogdica. 5; Frag. 4.12; Gersh. Sogd. Cpds. 1945,                        Hen. Tales. 486.13; BSOAS 11.69; KG 2053, pp.
          140
                                                                                  "zVyrfy, pi. -f, KG 560
2298 >zp>nt     B ^ >np>nt                                             2310 *zYd—         C      .         j^jC^-^ <o-l&>~ ij^ *r
2299 >zp>r- ? S                    ^Uoy^l^                                  azyaS         (zyd-) ©*ham-zgad ©impf. mzYd
     ozPar ? <DAv. uzban Parth. 'wzbry                                            ^'nzyynt-, 'nzyst-
     provisions                                                                 Go)leap up
        MDii pl46n7; Hen. Mittelir. 113.7                                       BSTii 888.56; Benv. J A 1955, 315; C2, 60V23 n
=== pdf page tag near
:
```


## [2026-09-05T20:09:10.641Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '2296' in p and 'zp}k' in p.replace('>','').replace('»',''):\n        pass\nfor i,p in enumerate(pages):\n    if 'root of the tongue' in p:\n        print('leaf idx',i,'-> printed approx',i-66)\nEOF"
}
```


### [2026-09-05T20:09:12.976Z] TOOL RESULT

```
leaf idx 156 -> printed approx 90
leaf idx 572 -> printed approx 506
```


## [2026-09-05T20:09:17.797Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find page containing 1003\nfor i,p in enumerate(pages):\n    if re.search(r'\\b1003\\b',p):\n        print(i, p[:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T20:09:19.706Z] TOOL RESULT

```
684
```


## [2026-09-05T20:09:22.841Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nhits=[i for i,p in enumerate(pages) if 'زبان' in p]\nprint(len(hits), hits[:40])\nEOF"
}
```


### [2026-09-05T20:09:24.513Z] TOOL RESULT

```
165 [5, 6, 19, 25, 36, 42, 45, 50, 51, 52, 57, 62, 65, 66, 67, 71, 72, 77, 79, 81, 87, 107, 117, 119, 120, 126, 127, 136, 137, 143, 152, 154, 159, 164, 170, 174, 179, 181, 186, 190]
```


## [2026-09-05T20:09:27.678Z] TOOL CALL #23: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1003 2>&1 | head -60"
}
```


### [2026-09-05T20:09:29.330Z] TOOL RESULT

```
no scan of BQT covers printed page 1003 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:09:31.518Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:09:33.339Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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


## [2026-09-05T20:09:36.736Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (462,463,464):\n    print('==== leaf',i,'printed',i+540)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-05T20:09:38.556Z] TOOL RESULT

```
==== leaf 462 printed 1002
 ‫—‬           ‫‪۵ ۵ 6‬‬




     ‫مخفف زدآوتر امت که انزاطرف ترباشد‪#*.‬‬                              ‫نام روز ست‬         ‫کشده و بدال ایرد زده )‪۰ (۱‬‬

‫زانو رصد اه کردن = کنابه‬                                              ‫و دامفرشتها‪.‬ست که‬      ‫وهشتم‌است ازماهپای شمسی‪-‬‬

                                                                      ‫صالح وتدییرآموراین روزباو علق دارد ویمحافظت‬
‫ازمراقبه کردن ومتفکرواندوهگین شتن باشد ؛‬
‫وزانو کرصرددن‌هم هت که بی کلمة گاهباشد‪.‬‬                               ‫حوران بپشتی لیزمامور است‪ .‬کوبند در این روز‬
                                                                      ‫درخت شاندن (‪ )۲‬و تخم‌کاشتن و عمارت کردن‬
‫سياه‬         ‫جااورىت‬       ‫»‬   ‫بروزن خانه‬    ‫=‬    ‫رانه‬
                                                                                                      ‫بغامت خوب امت ‪.‬‬
‫ریگ بوردار که بیشتر در حمامها متکون شود‬
                                                                      ‫ویمیم‬   ‫رامیم ‏‪ ۳ am‬تال ستحتالی رده‬
‫وبانگ طولالی کند ‪ ۰‬و بعضی گوبند زانه ختفا‬
                                                                                 ‫بزر که‬     ‫بيار‬   ‫نام رودخانه‌است‬   ‫‪4‬‬   ‫زده‬

                          ‫باشد ‪.‬‬      ‫نك‬
                                       ‫این‬
                                         ‫درک‬
                                           ‫ره س‬
                                              ‫گت ک‬
                                                 ‫اس‬
                                                                       ‫دان = بروزن جانِ‪ .‬مخفف ازآن امت‬
‫با نون بتحتالی رسیده(‪)4‬‬                   ‫رالیج" =‬                    ‫چنانکه گویند زناطرف وز آ نو ممنی ازا تطرف‬
                      ‫وبچیم زده * وطن مالوف رگاویند ‪.‬‬
                                                                      ‫ولزآشو‪ -‬و نام درختی هم هتا باربك ودراز‬
 ‫راو = ‪,‬کون واو ‪١‬‏ قوی و زیردمت‬                                        ‫شام بار‬     ‫که ازآن لىر ونىزە ساز ند و در ملك‬

‫و استاد بنا و کلکار را تدر‬                ‫و پرزور راکویند ‪-‬‬
‫‪-‬ودرة‬          ‫®‬     ‫ورخنه‌هرچیزباشد‬      ‫وشکاف‬        ‫‪۴‬‬   ‫کفتە‌اںد‬    ‫نقطه (‪.)۳‬‬    ‫بن سین بی‬        ‫ر ]فستر ‪= ۲‬‬


         ‫‪۰‬‬   ‫لقطه‬     ‫‪ :‬بی‬     ‫چك‬   ‫(‪)۳‬‬           ‫(‪ )۲‬چش ‪ :‬بنشاندن ‪.‬‬                 ‫(‪ )۱‬چك ‪ :‬ودال زده ‪۰‬‬
                                                                 ‫‪۰‬‬
                                                        
==== leaf 463 printed 1003
‫زاولایه‬                                                                                     ‫ات‬   ‫او‬




‫زاور فتراش * ‪ -‬بنتح ف واسکون‬                             ‫بارچه و لیم‬   ‫وهبمعتی خشت‬   ‫کوه را نیز گوبند ‪-‬‬

‫رای بی‌نقطه وفوقالی بالف کشیده وبشین قطمدار‬                                      ‫تن‬      ‫هم آمده‬      ‫خشت‬

‫زده » ءمتنم الوجود را کونند چه زاو بمعنی‬                  ‫راود = بر وزن باور ‪ ۰‬بمعنی خادم‬
               ‫باشف ‪۰‬‬    ‫بمعئی وجود‬    ‫همتتم وفرتاش‬      ‫و خدمتکار باشد وستارة زهره را نگیوزبند ‪٩‬‏‬
‫زاوش ‪ = ۱‬بشم واو پروزن خامش »‬                                                ‫ویمعنی قدرت رقوت؟ و‬
                                                          ‫‪-‬ژلده بود بعنی برزگه‬
                                                         ‫به از‬   ‫ناکه‬‫کره‬
                                                                       ‫وقوی هکل وتوانا ‪ -‬ویمعنی ز‬
 ‫میمننی بر وزن‬
             ‫نامکو کب مشتری ‪,‬اشد ؛ و با‬
                                                          ‫دلبری وبارا باشد ‪ - ۳‬و یمعنی چاروای سواری‬
‫خموش وخاموش هآمده است ؛ وبروزن‌خاموش‬
                   ‫کو کب عطارد را نبز گفته‌اند ‪5‬‬          ‫هم آمده‌است که بعربی‌راحله خوانند ‪ - ۴‬وزنده‬
                                                         ‫و سلامت را نگیفزته‌اند و‪-‬بمعنی آب سياه حم‬
                                                          ‫وان علتی باشد مشهور رسنی هر‬         ‫دة هن‬
‫زابل است که ولابت سیتان باشد ‪ -‬و لام فومی‬                 ‫وی راکه ات تاه آورده‪ :‬باشد گونند فزاوز‬
                                                          ‫شده است» بعنی آب سیاه آورده است‪ -‬ویمعنی‬
‫لزهٌ نت زبان فارسی باشد که آنرا‬
                              ‫جیکمی ا‬
                                    ‫و‬
       ‫زارلی مىگفته‌اد وکانون متروك است ‪. ۸‬‬               ‫رنگه ولون‌سیاء نآیمزده است‪ -‬وممك وبخیل‬
                                                          ‫را لیزگوبند ‪ -‬و بمعنی ممتنع هم هت که در‬
 ‫راو لاه * ‪-‬بروزنکاوخانه‪.‬بندآهنی‬                                              ‫برابر ممکن باشد ® ‪.‬‬
  ‫ظ ‪۰‬‬      ‫‪۴‬‬             ‫رك‪ :‬زور ‪.‬‬      ‫‪۴‬‬          ‫‪,‬هره باشد» «لفت فرس ‪۹۲۱‬؟‪.‬‬
                                                                           ‫ز‬         ‫«ور‬
                                                                                       ‫‪ ۱‬زا‬

  ‫‪ ۵ - ۴‬زاور‪...‬‬                ‫ممنی زهره ( بضم اول ) را زهره ( بقتح اول ) خوانده‌اند ! رك ‪ :‬ح ‪4‬‬
                          
==== leaf 464 printed 1004
   ‫و ‪ ۵‬ات‬
                                                                                                      ‫زاووش‬

  ‫راهد حخك د کنابه از زاهدی‬                           ‫است که‌برپای‌ستوران و بکزپرابان گذارند وآنرا‬
  ‫است که لهات اهتمام درزهد وپرهیز کاری داشته‬           ‫‌موی مجعد وییچیده‬       ‫ید‪-‬‬
                                                                                 ‫نوین‬‫عوک‬
                                                                                       ‫ییمبخا‬‫ورک‬‫بت‬
  ‫واهد جاهل را یز‬
                ‫باشد ‪ -‬وزاهد بی درد ز‬                                                        ‫همآمده اضنته‪..:‬‬
                                          ‫گونند ‪.‬‬      ‫و‬          ‫هبروزن هه‬
                                                      ‫خاموش » بمعنی‬                      ‫راو وس‬
                                                     ‫زاوش است که ستارة مشتری باشد ‪ -‬و عطارد را‬
                      ‫باشد ‪۰‬‬   ‫حهان آرا‬    ‫خورشد‬
                                                                                                 ‫زتماید ‪.‬‬
                                                                                                        ‫فن‬‫ک‬
  ‫با ها بروزن خاطری » بوی‬      ‫راهری۔‬
  ‫خوش‌را گوینده وبجای رای می‌نقطه زای نقطه‌دار‬
                                                      ‫داووق ‪ - ۴‬بر وزن فروق ‪ .‬نم‬
                                                      ‫باصطلاح ‪ ۱‬کیریان و عریی زببق‬                   ‫جنوه است‬




                                   ‫چن ادد‬                                           ‫وکل‌کار راکوبند ‪. ۴‬‬


                                              ‫يان دوم‬


  ‫زبراد بنتح اول بر وزن سواد » عرقی‬                    ‫می‬         ‫= بنتح اول و سکون ان‬               ‫رب‬

‫وچرکی باشد نکرهاآاز میان پای جانوری گیرند‬             ‫رایگان‌است‪ ,‬وآن هرچیزباشد که بیابند بابمفت‬
                         ‫و آن جانور بگربه‬            ‫پدست کی آید که در عوش آن چیزی لناید‬

                          ‫مانند باشد لیکن سر‬          ‫داد وییمتی آسان هم هت که درمقابل دشوار‬
                                                                                                          ‫است ‪.‬‬
                            ‫اوازس رگرب کوچکس‬
        ‫زباد‬              ‫است‪ .‬وآن‌عرق بغايت‬          ‫اول وثالی‌مشدد بالف کشده»‬         ‫ص‬         ‫ربا‬

  ‫عطربات مشهور‬       ‫هزٌ‬
                       ‫وا‬‫مل‬
                          ‫جاشد‬
                             ‫مپ‬
```


## [2026-09-05T20:09:48.168Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (465,466):\n    print('==== leaf',i,'printed',i+540)\n    print(pages[i][:3000])\nEOF"
}
```


### [2026-09-05T20:09:50.148Z] TOOL RESULT

```
==== leaf 465 printed 1005
   ‫زنباکنسكت‬                                                                            ‫و و ات‬    ‫تم‬




                                                   ‫زان ‪ ۱‬ب»فتم اول معروف است ‪۴‬‬
‫و سخن گوی باشد ‪ -‬و شخصی را لز کوبن که‬               ‫ی لان کواند ‪ ۰‬وضم اول هم درست اد‬                ‫وس‬

 ‫را کیفزته‌اند ‪- ۴‬‬     ‫رد‬
                        ‫گاند‬
                           ‫ارابد‬
                               ‫شنها‬
                                  ‫و زبا‬
                                      ‫همه‬          ‫ربان بر = بطم بای ایجد » کنابه از‬
 ‫ربان ران = با رای فرشت بر وزن‬                     ‫خاموش کردن صدعی است بدلابل و جوابیکه‬
 ‫زبان دان » صاحب قیل و قال و پرکوی و هرد‬            ‫دیگر حرف تمیتوالد زودبنمعنی عطا وبخشش‬
                                                   ‫نزآمده است چنانکه در زمان بیغمبر شاعربرا‬
 ‫ربان ردن ‪ -‬کنایه از حرف زدن‬                        ‫را سر‬    ‫بسمرکه زبانش‬   ‫فر مودند‬   ‫رسالت‬      ‫رت‬


                            ‫وسخن گفتن باشد ‪.‬‬       ‫عمر خواست که بکاارد ببرده حضرت امیرفرمود‬
 ‫تندن ‪ -‬کنابه از خاموش‬
                     ‫سبا‬
                       ‫ر‬                                                        ‫که باوچیزی بده ‪.‬‬
                                                   ‫ربان بر ‪۵‬ت بکر نون» گیاهی است‬
                     ‫کردالیدن باشد ‪.‬‬
                                                    ‫وبعربی لسان‌الحمل‬       ‫ند‬
                                                                             ‫نوشك‬
                                                                                ‫ورااخرک‬
                                                                                      ‫خآن‬
                                                                                        ‫که‬
 ‫زبان طوطی «بکرون‪ ,‬نامکیاهی‬                                 ‫و آذان‌الجدی گونند ‪ .‬علاج اسهال کند ‪۰‬‬
                                 ‫دواعی ‪5‬‬   ‫است‬

                                                    ‫ربان لست = کنابه از خاموش شدن‬
‫زان گاو ‪ -‬بکس ون نام وعی از‬                                                                      ‫باشد ‪.‬‬
 ‫اناهمی است که کاو‬
                 ‫پیکان تیرشکاری باکشدی‪-‬و‬
                             ‫زباش کوبند ‪. ۴‬‬        ‫زان یی سر = بکس ون »کنابه از‬
                                                                              ‫ب‬
                                                                      ‫سخن بیهوده باشد ‪.‬‬
‫ر بان گنحشات‪ -‬درختی را کوندکه‬
 ‫بارش بزبان کنجتك ماند وبعضی بارآن حرخت‌را‬         ‫ربان تر کردن ‏ کنابه از سخن‬
                                                              ‫گفتن ‪ -‬ولقمه در دهن گذاشتن باشد ‪.‬‬
 ‫کفته اند و بعربی لسان‌الصافیر و النةالسافر‬
 ‫خوانند و حب‌الوز هم کوبند بتشدید زای‬               ‫ریان دادن (‪ )۱‬س کنابه از عهد‬
                             ‫نقطه‌دار (>) © ‪.‬‬                      ‫وشرط کردن‪ -‬ورخصت‌دادن باشد‪.‬‬


                             ‫(‪ )۷‬چك ‪ :‬بتشدد زا ‪.‬‬    
==== leaf 466 printed 1006
    ‫ات‬                                                                                                            ‫ِ‬
‫ر بر جد ‪ - ۴‬لوعی اززمرد باشد‪ .‬وآن‬
‫از جملهٌ جواهراست وطسمش سرد وخشك است‬
                                                                              ‫‪4‬‬            ‫زبانه‪ma ۱‬‏ بفتح اول‬
                                                     ‫‪۰‬‬   ‫در دوم‬
                                                                                           ‫بر وزن بپانه » آنجه در ميان‬
‫را گویند‬      ‫صدر مجلی ‪۵‬‬          ‫=‬       ‫ر بر دست‬
                                                                                           ‫شاهین ترازو باشد ‪ -‬و زبالة‬
‫فوت و فدرت‬          ‫صاحب‬    ‫و‬    ‫توانا‬     ‫از مردم‬       ‫و کنابه‬
                                                                                          ‫هر چیز را نز گوند ؛ و هم‬
                                      ‫‪۷‬‬    ‫دن‌هروزو ‪‎‬دشاب ‪۹‬‬          ‫‪۲‬‬                ‫‪٣‬‬
                                                                                                       ‫آول‌هم دردت است‬
‫‪ -‬بغای مضموم بواو وفا زده؛‬                 ‫وف‬
                                            ‫قبر‬
                                              ‫ر‬                          ‫زان یاقتی ‪-‬کنابه ترازو و زبالآن‬
                                                                                                       ‫ب‬
                        ‫بمعنی دشنام ولفرین باشد ‪.‬‬
                                                                                                 ‫از وت بافتن باش ‪۸‬‬
  ‫بواوی‬
      ‫ز بر کلو بد = باکاف ولام و وا‬
                                                                           ‫ون‬‫کلی‬
                                                                               ‫سا‬‫وتح‬
                                                                                   ‫زربر ‪ -‬بکر اول وف‬
‫نمعنی دیگه‬      ‫‪۰‬‬    ‫و حرکت مجپول‬              ‫و دال‬        ‫حطی‬
                                                                         ‫‪ ۰‬بمعنی از بر باشد که حفظ کردن‬         ‫رای قرشت‬
                           ‫باشد که درآن طعام بر لد ‪۰‬‬
                                                                         ‫وبیادگرفتن وبخاطرنگاه داشتن است‪ -. ۴‬وبفتح‬
 ‫رر‪SE . 6‬‏ وفتح‌الی وسکون‬
                        ‫ب‬                                                ‫اول بمعنی بالا باشد ‪ ۴‬که در مقابل پابین است‬
‫سستت که حفط وبیادداشتن‬
                     ‫بمه‌نی ازبرا‬                 ‫ثالث وعم‬
                                                                         ‫است وبعربی فوق گوبند‪ -‬وحر کت فتحه را نیز‬
                                   ‫وبخاطرنگاه داشتن ‪,‬‬                                                           ‫گفته‌اند ‪.‬‬
‫و شم‬     ‫|‬                                                               ‫بنتحاول و ثانی » لحاف‬     ‫‪-‬‬   ‫ر بر پوش‬

 ‫غین نقطه دار(‪ )۱‬ورای بیلقطه سا کن ء آن‌است‬
```


## [2026-09-05T20:10:07.113Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\nfor i in range(450,480):\n    nums=re.findall(r'[۰-۹]{4}',pages[i])\n    print(i, i+540, nums[:6])\nEOF"
}
```


### [2026-09-05T20:10:08.879Z] TOOL RESULT

```
450 990 ['۷۱۱۲']
451 991 []
452 992 []
453 993 []
454 994 ['۵۸۲۷']
455 995 []
456 996 []
457 997 ['۷۵۹۱']
458 998 []
459 999 ['۵۲۵۵', '۰۱۸۸']
460 1000 []
461 1001 []
462 1002 ['۷۱۷۱', '۵۳۵۲']
463 1003 []
464 1004 ['۸۹۱۰']
465 1005 ['۰۵۲۰']
466 1006 ['۱۹۰۰']
467 1007 ['۵۵۹۱']
468 1008 []
469 1009 ['۳۹۰۰']
470 1010 ['۰۳۴۱', '۶۵۱۰']
471 1011 []
472 1012 []
473 1013 ['۱۰۲۱']
474 1014 ['۵۲۹۱', '۹۲۳۱', '۱۱۰۱', '۲۵۳۸']
475 1015 ['۱۰۱۳']
476 1016 []
477 1017 []
478 1018 ['۵۱۰۱']
479 1019 []
```


## [2026-09-05T20:10:22.620Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(462,468):\n    lat=[l for l in pages[i].split('\\n') if re.search(r'[A-Za-z]{3}',l)]\n    print(i,i+540,lat)\nEOF\necho \"=== BQT v5 ta'liqat referencing زبان / page 1005\"\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'زبان' in p and re.search(r'۱۰۰[0-9۰-۹]',p):\n        print('leaf',i,'printed',i-5)\n        print(p[:1500]); break\nEOF"
}
```


### [2026-09-05T20:10:24.405Z] TOOL RESULT

```
Exit code 1
462 1002 ['         \u202b\u202a( 67800 = ۱\u202cفر) « لك \u202a ۲\u202cس \u202a -. 4۹۱\u202cزان = رال = \u202aacitavlys\u202c\u200f \u202asugaF\u202c\u202c', '  \u202bدر بعض نخ خطی پهلوی \u202akW\u202c\u200f \u202a kûnhs = hs\u202cآمده\u202a ,\u202cاز اوستا _ \u202aunhs , ۷05\u202c\u200f ( (\u202ajy\u202c\u202c']
463 1003 ['  \u202b\u202a) Olmstead , The History of the Persian Empire,p .24 ( 2605 liu\u202c\u202c']
464 1004 []
465 1005 []
466 1006 []
467 1007 ['                    \u202b\u202a( raisin\u202cفر) «لك \u202a ۲\u202cص \u202a: ۵۵۹۱\u202c\u202c             \u202b\u202a065\u202c\u202c']
=== BQT v5 ta'liqat referencing زبان / page 1005
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'
```


## [2026-09-05T20:10:34.513Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (219,220,221):\n    print('==== leaf',i,'~pp',(i-15)*2,(i-15)*2+1)\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-05T20:10:36.398Z] TOOL RESULT

```
858
==== leaf 219 ~pp 408 409
 gs Zrünüve beside Zrünü- vü, m.; Li. girna; Latv. dzirnas, f. pl. beside dzirnus & dzirnavas ‘handmill, millstone’. E- grade in Go. -qairnus; OHG quirn, quirna; MHG quirn-, kurne-stein; OS quern, u-st.; OFris. quern; OE cweorn; G Querne 'quern'; ON kvern, pl.-ir. f. WP I, 685
guró (1) 'gulp down, devour’. Cf. guer-, guor- Ved., Skt. gire, gilami, gírami, grnami, id.; Av. gar-, xwar-; Lat. voro, åre; OCS (i-basis) Zr, Zréti; Li. cf. girà “small beer" girtas, adj. ‘drunk; tipsy’; girtüs ‘heady — of wine’; Latv. dzira “drink”
gurð (2), (euro, gureio) “load, weigh down, burden'. Cf. gurus Skt. gure ‘raise, lift; cf. garvami "be proud"; Oss. ärgavín, àr$uvun “cock — a gun’; ärgävag trigger; Arm. krem ‘carry, bear, suffer; kruim, krvim "am borne’; Gk. baréo ‘load’; báros, gs -eos ‘weight’; Go. kaúrjan ‘burden’; Lat. cf. gravō, āre; Li. gurnùs ‘portly, digni- fied’; Latv. cf. gurstu, gurt “flag, be tired’. Cf. also Gk. brabeús (?) umpire’, fr. *gurgueu-)
guroghos (?), see guroghos
gurquis ‘neck, throat”. Cf. WP I, 593 and gurgat-. (Cf. grquis)
gurksio (gurkskó, gursKo) — gurüsn-
15
20
25
30
35
40
45
376
Arm: kir, gs krči, i-st. ‘gorge’; Alb. grykë ‘neck, throat; goitre’; Olr. cf. brágae, id.; Blg. Srb. cf. grák-lan, grkljan, id.; Cz. cf. vyhrknout ‘gush out’; Li. cf. gurklys ‘craw, larynx. (In the sense of ‘goitre’, Alb. grykë equates with Cz. hrča, hrče, Srb. grča “lump, tumour’)
gurquið (gurquàið) ‘gulp; choke’. Cf. gurquis Gk. brápto (2) ‘gulp’; Slovene grčiti ‘strangle’; Cz. hrčet, hrknout (1) ‘gurgle’; OCS cf. grù- kajo, ati ‘croak’; grükavü ‘stammering’; Li. gurkiù, ti ‘gulp’
gurqutos, à (?) ‘gulp, throat’. Cf. gurgət-, gurð (1) & WP I, 683 Per. cf. gardan ‘throat, neck’; Oss. qùrtt ‘gulp’; Lat. guttus ‘decanter’; gutta ‘drop’; guttur, gs -uris ‘throat’; Lusat. hort, m.
==== leaf 220 ~pp 410 411
ignified’; gúroti ‘be heavy, lumber along’. Cf. WP I, 685 and guruos
guruos, ios ‘strong’. Cf. gurus, etc. Arm. kar, i-st. (2) ‘power’; karem, karenam "am able’; karık, pl. “means, supplies, rein- forcements'; kari ‘excessive; very’; Gk. cf.
guruidh- — guhaueió
15
378
brierós, briarós ((strong', fr. *gur + *isoros, q.V); W bryw ‘vigorous’; Li. cf. gurbti, v. ‘thrive’; gurbüs "luxuriant? -gus, suffix in Gk. prés-bus, Cret. preis-gus; Li. Zmo-gus (earth-dweller' hence: *man?); cf. Li. guvüs lively’ (gutā, cf. guetu. Z-gde only in OE cwudu *chewing-gun, cud’: Icel. kvoóa ‘gum, resin’) guüd- (guoud-, güd-) “a hooting bird’. Cf. güd- and next Gk. büza 'eagle-owl; W cf. buddai ‘bittern’; MHG kūz, kütze, s & wm. 'screech-owl; OE cyta ‘bittern’; E kite; Norw. cf. kyte, v. ‘bray’ guüt- (guout-), variant of guüd-, guoud-, q. v. Gk. cf. boütalis ‘nightjar or sim? ; Lat. büteo, bütio ‘buzzard’
Guh
(N. B. Much of the evidence for IE initial *guh- is ambiguous)
guhaidros, à “bright, clear; brightness’. Var- iant: £uhaidros (?) Gk. phaidrós; Thrac. cf. Gaidreas (a name: Gk. Phaidros. Krahe); Li. gaidrüs, giédras, id.; giedra, giedrà “bright weather”. Z-gde in Latv. dzidrs “bright, clear”. A possible variant is sug- gested in R zvézda ‘star’; Li. ZvaigZdé, Latv. zvaigzne, id. as against Cz. hvézda, id. (See Supt. gaidros and cf. SEM:AIE: § 53: kajtar)
guhak- (or guhak-?) Alb. gacé ‘ember’; Lat. fax, gs facis ‘torch; sun’; variant (?) in Li. Zvake “candle; sparking plug’. Cf. guhak-
guhäl-? ‘crooked, awry, amiss, wrong’. Cf. squhal-. Evidence ambiguous Skt. hváre, mp. “am crooked'; Gk. cf. phëlos (if Doric *phàlos) ‘deceitful’; Lat. fallo, Gre (if for *falno. EM & WP uncertain); W gal (?) ‘enemy’; Ir. galann, id. (Cf. EM: DELL: p. 381; WH:LEW p. 447-8; and Hes. spheló- ‘askew’, if s- is
==== leaf 221 ~pp 412 413
ice’ beside qäzäl ‘charred matter’; Alb. cf. zegël, zegth ‘gadfly’; OCS Zego, Zeët ‘kindle, burn’; Zegü, žega “heat; Cz. cf. Zehadlo ‘sting’; Pol. zegadto ‘red-hot iron’; Cz. Zehlice ‘flatiron’; Slovene žežel ‘poker’. (An R-gde w. i-basis seems to be present in Gk. thibrós ‘roasted, hot, ten- der”, cf. OCz. Zhu, Zéci ‘kindle’ and OCS Z1Ze- nije ‘burning, inflammation’. Gk. type *guhï- gu-)
guheguhon-, redup. theme of guhen-, q.v. Vedic. 3s pres. subj. jaghánat; MIr. geoguin, aor. 3s; Hom. cf. épephnon, aor. isg.
guheldhos ‘requital, debt? etc. Cf. gheldh- Gk. Myc. télthos, -es-, n. “debt, loan'. Other forms ambig. (Hes. téltho ‘cheer’ or ‘enjoy’ suggests a radical of type dhel- (1) & (2) w. an extn. Cf. MHG teizen ‘stroke, fondle’. However, both notions are present in Ir. gell, Mod. geall ‘pledge; favour; iove’. See next)
guhelo (-àio, -ëið) ‘wish, desire’. WP I, 692 Skt. haryāmi ‘desire’ is ambig. cf. gherið; Gk. thélo, Hom. ethélo (e- unexplained); Lat. (am- big.) felix (but cf. bhelos, dhél-); OHG OE will (ambig. cf. uel-); OCS Zelajo, -&jo “desire: Slovene cf. želja, f. ‘will
guhemər (guhemen-) ‘swell, bulge’ Lat. femur, gs feminis (variants: femen, -inis & femur, feminoris, n. 'thigh"); MHG wimer, wimmer ‘tumour, growth, burl on tree’; cf. Fris. wan, wanne; OE wenn 'tumour'; Du. wen 'goitre' qua *guhomn- (?). A further var- iant may be present (*guhembh-: *guhombh-) in Li. gémbe ‘burl on tree’; Go. wamba ‘belly’, etc. Gk. pompho$ ‘bubble’ is ambig.
guhen- radical of general sense: “drive, beat, kil. WP I, 679. Cf. guhn- Verbal forms: Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. $Énem (thematic: ‘beat: gin ‘whip, rod); fanam ‘strive’: athematic; beside ğan, Let, ‘effort’; Hitt. kwemi (for *kwenmi, 3pl. kunanci: Skt. ghnanti);; Gk. (thematic) th
```


## [2026-09-05T20:10:45.066Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dnghu\\|dngh\\|jihvà\\|jihva\\|hizvā\\|hizva\\|zabān\\|zaban\" IEC.txt | head -30"
}
```


### [2026-09-05T20:10:45.116Z] TOOL RESULT

```
5739:Skt. jihva; Av. hizu, hizva, hizvá-; OPer. izāva, hazvàn; Pehi. huzvan, hizvan: Per. zabàn; Oss. àvzag, dim. type
5910:voice’. WP I, 642. Cf. 8uhen- Skt. cf. jbanàmi “sound”, v.; Av. hizu, gs hiz- vð & hizva, f., hizvo, gs hizváh-, n. ‘tongue’; Ober, hazána-, m., id.; Pers. hazvàn, zabàn, id. (and speech: Arm. dzajn, i-st. ‘voice’ be- side dzoni, vo, eav, adj. ‘consecrated’; s. ‘idol; Alb. zâ, gs zàni “voice, sound"; (T zë, gs zëri); Lat. honos & honor ‘honour’; OCS and com. Sl. zvonü ‘sound, bell": Pol. dzwon, Ukr. dzvin, id.; Latv. zvans, id. Cf. ĝuhuð
5918:ĉuhuos (£houos) “shout, call, appeal, impre- cation’. Cf. &uhuo, guhon- Skt. hū, adj. ‘calling’; juhū, jihva ‘tongue’; ` havah 'invocation' in Vedic; ‘sacrifice’ in Skt.; Av. zavō ‘call’; hizu, -áh-, n. and hizva, f. ‘tongue’; Ober, (alleged) izáva, id.; Oss. äv- zag, dim. type, id.; Per. cf. hazvan, zaban, id.; Arm. cf. n-zovK, gp. n-zovic (curse: Skt. ni- havah ‘invocation’; ni-hvaye invoke); Gk. Hes. cf. oló-phus or ol-óphus ‘mourning’; olo- phudnós, adj.; Mir cf. guth, pl. gothanna (“+ voice”. See next); Go. gaunópus ‘plaint’; OE géanobp, id.; MHG cf. guft ‘shout’; OCS züvü (cal, and com. Sl.); Cz. cf. ná-zev 'appella- tion’; Li. Zavai (charms, spells’; Zavüs *be- witching’
```


## [2026-09-05T20:10:50.330Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line no -> leaf\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in (5739,5910,5918):\n    print(ln,'leaf',m[ln])\npages=t.split('\\f')\nfor i in (m[5739],m[5910]):\n    nums=re.findall(r'\\n\\s*(\\d{3})\\s*\\n',pages[i])\n    print('leaf',i,'numbers',re.findall(r'\\b\\d{3}\\b',pages[i])[:12])\n    print(pages[i][:900])\n    print('...')\nEOF"
}
```


### [2026-09-05T20:10:52.441Z] TOOL RESULT

```
5739 leaf 231
5910 leaf 237
5918 leaf 237
leaf 231 numbers ['527', '398', '576', '577', '527', '399']
d-? Cf. WP I, 527) Gk. cf. ai-gíthalos (orn. *tit'. Cf. auis (1)); Alb. (ambig.) dhí, def. dhija (goat, but cf. gid-); ME kid; Du. kid, kidde ‘pony’; ON kið, gp -a, ja, n. "d: Sw. kid, beside kidling, killing, id. (Eng. kid is prob. of Norse origin, note initial k-)
$ig- ^speck, jot Per cf. jtye, jiqqe ‘tuft, crest’; Gk. cf. gíg-arton “small grain, grapestone'; gigídion ('earthnut or sim.); R zga (jot, tittle’, in phr. ni zgi xléba ‘not a scrap of bread"); melju-zga ‘small fry’; G Kick-beere ‘gall on plants’; Srb. cf. zgeba ‘gnome’. (Isophonic: Li. Zigas 'goldbeetle")
2ig- (gigr-) ‘convulsion, sob; sob, hiccup, gasp' Arm. cf. ckram ‘sob’; Ir. gíogaim ‘squeak’; MHG kiche ‘asthma’; Sw. kikna ‘gasp’; kik- hosta *whooping-cough'
gig- (1) “look, peep’ NGer. kieken; Du. kijken; Icel. kíkja; Sw. kika, id.; Pol. cf. zez, zyz ‘squint’; zezem, adv. ‘asquint’
ĝibos, à — $leibh-
10
15
20
25
30
35
40
...
leaf 237 numbers ['664', '409', '642', '529', '410', '527', '540', '411', '548']
 beast’; Gk. thereu:ós *huntable'; type *guheriios in Gk. theríon “wild animal and thérios, théreios "of wild ammal'; OCS zvérij, adj. id.; Li. cf. žvērijà ‘wildlife’
ĝuhis, ĝuhus ‘fish’. WP I, 664 Arm. dzukn, gs dzkan; Gk. cf. ikh-thüs, gs
409 | -thúos; Li. Zuvis, -iés, f.; Latv. zivs, gp zivju, f. id. (Source of Gk. ikh- unknown)
(8uhlg- “shine? isa possible formula for both Lat. fulgeo, fulgo and Li. Zvilgu, éti, id. but cf. a preferable *bholg- for Lat. WH & EM confused)
$uhnos, see &uhen-, £uhon-
$uho-, see 8uhuo-
&uhon- (guhonos, -es-, à, is) “sound, noise,
voice’. WP I, 642. Cf. 8uhen- Skt. cf. jbanàmi “sound”, v.; Av. hizu, gs hiz- vð & hizva, f., hizvo, gs hizváh-, n. ‘tongue’; Ober, hazána-, m., id.; Pers. hazvàn, zabàn, id. (and speech: Arm. dzajn, i-st. ‘voice’ be- side dzoni, vo, eav, adj. ‘consecrated’; s. ‘idol; Alb. zâ, gs zàni “voice, sound"; (T zë, gs zëri); Lat. honos 
...
```


## [2026-09-05T20:11:03.477Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5730,5745p' IEC.txt"
}
```


### [2026-09-05T20:11:03.547Z] TOOL RESULT

```
45
398
$18- (2) ‘teat Oss. dzidzi; Arm. cic, gs cci, i-st., id.; Slovene zizek, dim. id.; zízati (v. ‘suck’)
êg- (3) ‘spark, fire’. (Variant: ĝeig-)
Arm. cf. ccumb, gs ccmbo, o-st. ‘sulphur’, lit. (?) ‘cloud of sparks’, cf. Arm. amb ‘cloud’; Alb. cf. xixé ‘spark’; Li. Zize Celow heat. Lalis. Infantine wd. for ‘fire’. Cf. variant ZíeZ- iba ‘spark’, fr. *&e18-)
$í&éno (redup.) “bear”; mp. "become WP I,
576. Radical: 8en-, q.v. Av. zizan- ‘give birth’; cf. Skt. jajflih *germi- nating’; Arm. cf. cnim Cam born”, fr. *8enio); Gk. gígnomai, aor. egéneto; Lat. gigno, Gre, pf. genui ‘beget’; W cf. geni, inf. ‘be bofn’; MIr. gignid, 3s fut. ‘will be born": gainiur “am born?
2í2nosko (X2nos-) (intens.) ‘know’. Cf. ong- mi, ?nosKo. WP I, 577-80 Skt. cf. desid. jijfiase; Ober cf. xsnàs-, id.; Gk. gignósko, Epirote gnósko; Lat. a-, co-gnoscó, ére; Arm. cf. canucanem (^warn', fr. *$nosKno)
eiguha ‘tongue’. (Redup. of type guhuo, &u- huos, 2uhón-, etc.)
Skt. jihva; Av. hizu, hizva, hizvá-; OPer. izāva, hazvàn; Pehi. huzvan, hizvan: Per. zabàn; Oss. àvzag, dim. type
ilos, a, is “growth, stem, sprout’
Arm. ciy 'stem, blade of plant’; cil “bud, shoot panicle’; Thracian zila- “vine? beside Dacian -zila, -dila (in plant-names: a-zila, beside a- dila, proce-dila, tani-dila, doc-tila (sic), and dio-dela (sic) of uncertain composition, cf. porKos, tn-, tāk-, diu-); Ir. giol (2) “early grass”; MHG kil (2) ‘leek’; cf. Rum. (? substrate) zir- nå, f. ‘woody nightshade’. (Per. zire ‘caraway, aniseed' is ambig.)
gislos, is (gisol-) ‘pebble, shingle’
Per. cf. Zale “hail; dew" (?); Alb. zallé ‘pebble, shingle’; OHG kisil, MHG kisel, OE ceosel, ceosol, id.; G Kiesel "flint, silica, hail; kisseln, v. ‘hail’; Icel. kísill ‘silica’; OCS žali “shore? Srb. žal, id.
(&it-, variant of ĝid-, gidh-, q.v. WP I, 527. Cf. W gid, giten ‘kid’. Isophonic are MHG kit, gs kides; kide ‘sprout’; OE cip *mote")
£ieua, see Seu
```


## [2026-09-05T20:11:13.894Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN\"; grep -n \"zabân\\|zabān\\|zubân\\|Zunge\" HRN.txt | head -20\necho \"=== HUB\"; grep -n \"zabân\\|zabān\\|hizvā\\|huzvān\\|Zunge\" HUB.txt | head -20"
}
```


### [2026-09-05T20:11:13.965Z] TOOL RESULT

```
=== HRN
5441:KZ. 28, 34 *Lenker der Zunge*, siehe aber Geldncr, KZ 28, 259.
5758:i)i}0, ^ehän, zuhän (AM.) 'Zunge*, zefan-),
5760:ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
5762:kurd. azmän 'Zunge'; af/. ziha\ oss. t. äuzdg (4);
=== HUB
5883:Ap. v ist zu b geworden in zaban^ zubdn *Zunge' =-
```


## [2026-09-05T20:11:15.309Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== RCH hozvan\"; grep -n \"هزوان\\|huzwán\\|huzwan\\|hazwán\" RCH.txt | head\necho \"=== MON\"; grep -n \"هزوان\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head"
}
```


### [2026-09-05T20:11:15.417Z] TOOL RESULT

```
=== RCH hozvan
=== MON
MON_part2.txt:90114:هزوان: ۱0-۵ (۰) زبان لسان. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:90114:هزوان: ۱0-۵ (۰) زبان لسان.
```


## [2026-09-05T20:11:22.184Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 5750-5775\"; sed -n '5750,5775p' HRN.txt\necho \"=== HUB 5875-5895\"; sed -n '5875,5895p' HUB.txt\necho \"=== MON hozvan ctx\"; sed -n '90110,90118p' MON_part2.txt"
}
```


### [2026-09-05T20:11:22.250Z] TOOL RESULT

```
=== HRN 5750-5775
(skr. prajUn-) ^) ; phlv. zünük, jfänäk (letzteres entweder
dialektisch oder auch zänük zu lesen); 2l\, jdnu- 'Knick-
arm, cunr 'Knie* (H. No. 138).
kurd. zCLna; af/. zangün^ cangün; bei. zän (421);
wa;^. zatij sar. zm^ sangl. zong.
649. t^äiv 'Spalt, Riss'.
Zu [/"gap" {Jap-) 'klaifen, tief sein , vergl. aw. Ja/ra-
jqfnH' (Nöldeke, mündliche Mitteihmg).
i)i}0, ^ehän, zuhän (AM.) 'Zunge*, zefan-),
g. izvFin (Käs. Q. ilzün ist natürlich arab. lisän).
ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
bezw. huzDän, ziivän bezw. zavän ; ai. jikvä-,
kurd. azmän 'Zunge'; af/. ziha\ oss. t. äuzdg (4);
hol. LW. ztivan^ n. zavan (311); siyn. zev, sar. ziv,
wa/. zik.
Über die indogerm. Grundform hat zuletzt Johans-
son Indog. Forsch. II, 1 folg. gehandelt.
051. lieber 'über, darüber, auf, zewer, vergl. zehet'dest 'die
Oberhand besitzend'.
') Über znii' wird hoffentlich die neue Ausgabe Klarheit bringen.
2j z/f/. X^'ärezm. Fol. 656 r (Berliner Handschrift); jedenfalls
dialektisch, vielleicht ;^^'ärezmisch.
'j Vordflchti<»o Form; Bartholoniao, BB. XIV, 245 vermutet
hiznrani.— 145 —
phlv. aj war, vergl. nniS': 11 TN in (Is. 1, 7).
LW. kurd. zhrl 'Heftigkeit, heftig' : af/. zahar ober-
=== HUB 5875-5895
= zd. xsvaepclf-; mar i seba * Viper, zd. xsva^wa-; seva *be-
redt*, zd. xsva^wa- (oben p. 82 — 83). Man beaehte, dass s
fiir sv hier im Anlaut steht. Im Inlaut bleibt §v in kisvar
'Erdtheil' = zd. karSvare und du^ar schwierig' (s. § 108).
V ist abgef alien nach r in har jeder* = ap. haruva-,
zd. haurva-.
Aus ap. *duva *zwer (= zd. dva, ved. dvau und duau)
ist np. dOy dt4 geworden.
Ap. v ist zu b geworden in zaban^ zubdn *Zunge' =-
phi. zuvan (geschrieben zuban) 61. and Ind. 150, zd. hizva-]
arabisch QubaJ = phi. Kavdt^ zd. kavata- noben np. Kavad
(bei Hamza etc. Noldeke, Tab. 135), syr. Qavad, arm.
Kavat Einmal raban (oder ruban) fiir ravdn 'Seele* (JRAS.
1894, 430) = phi. ruvan^ zd. urvan-.
*) Die Nebenform np. bar, arm. LW. bar in bdrapan u. 8. w?
ist wohl dialektisoh, ygl. H. 545 und oben p. 116 Anm. 2. — Zu hinin
siehe oben p. 33. Bleibt phi. bBs 'Leid' H. p. 270, Nr. 49 mit b fiir dv ,— 167
Kapitel 10: Kontraktion.
Die Lautgruppen : Vokal -f y oder v + Vokal bleiben
im Persischen entweder bestehen (vgl. § 40: -dya-^ -*y^-,
-aya- und § 56) oder werden kontrahirt.
=== MON hozvan ctx
موقع قرائت ترجمة پهلوی آن خوانده 


ین شنگه 
هزوان: ۱0-۵ (۰) زبان لسان. 

هزه: (ع-)متتدط [ع. هزة] یک بار جناندن» 
تحریک.
```


## [2026-09-05T20:11:37.845Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dnghu\\|dṇghū\\|tongue. Various\\|tungon\\|dingua\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:11:37.884Z] TOOL RESULT

```
403:dnghi. Tongue. 1. Germanic *tungon- in: a. Old English tunge, tongue: TONGUE; b. Middle Dutch tonghe, tongue: BILTONG. 2. Latin lingua (< Old Latin dingua), tongue, language: LANGUAGE, LANGUET, LIGULE, LINGO, LINGUA, LINGUIST; (BILINGUAL). [Pok. dnghii 223.]
```


## [2026-09-05T20:11:38.553Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN tongue\"; grep -n \"^tongue\\|tongue, n\\.\" KLN_1966.txt KLN_1971.txt | head\necho \"=== SKT\"; grep -n \"tongue,\" SKT.txt | head"
}
```


### [2026-09-05T20:11:38.617Z] TOOL RESULT

```
=== KLN tongue
KLN_1971.txt:62902:tongue’, which is compounded of xutov, gen. 
KLN_1971.txt:87337:tongue of a balance; a weighing examination*, 
KLN_1971.txt:116223:hounds-tongue, n., name of a plant. — OE. hundes 
KLN_1971.txt:118015:tongue (anat. and zool.) — F. hyolde , fr. Gk. 
KLN_1971.txt:118425:tongue (med.) — Medical L., formed fr. next 
KLN_1971.txt:138366:tongue’, fr. L. lingua, ‘tongue, speech, language’, 
KLN_1971.txt:138398:tongue’. See prec. word and adj. suff. -ate and 
KLN_1971.txt:167611:tongue. — ModL., compounded of Gk. 69K;, 
KLN_1971.txt:199986:tongue (anat.) — ML. rdninus , ‘pertaining to 
KLN_1971.txt:246550:tongued’), L. tenuis, ‘thin, slender’, tenus , ‘cord, 
=== SKT
```


## [2026-09-05T20:11:45.655Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN language\"; grep -n \"language, n\\.\" KLN_1971.txt | head\necho \"=== KLN tongue entry\"; grep -n \"OE\\. tunge\\|tunge, rel\\|Goth\\. tuggo\" KLN_1971.txt | head\necho \"=== SKT tongue\"; grep -n -i \"TONGUE\\.\" SKT.txt | head\necho \"=== SKT language\"; grep -n -i \"LANGUAGE\" SKT.txt | head"
}
```


### [2026-09-05T20:11:45.752Z] TOOL RESULT

```
=== KLN language
133697:language, n. — ME. langage, language, fr. OF. 
=== KLN tongue entry
138367:fr. OL. dingua , which is cogn. with OE. tunge, 
249581:tongue, n. — ME. tunge, tonge, fr. OE. tunge, rel. 
=== SKT tongue
7677:of  the  windpipe.— Gk.  7^£^ra,  Attic  form of  >Xwa<ja,  the  tongue.     Der.  epi-gUttU.
9944:Iiap  (i)j  to  lick  up  with  the  lonmie. tE.)  M.  E.  lapptn.  A.  S.  lapian,  to  lap. +Icel.  hpja,  Dan.  labt,  O.  H.  G.  /afan.  to Upup.+  W. //(t/w,  hJamberr,  GV.X&wrtiv, tolap  with  the  tongue.  (Base  LAP.)  Allied to  lamhient,  labial,  and  hp.
19862:Tongue.  (E.)    M.  £./«/. funj^.  +  Icel.   Swc*l.  /««:- Du.  Ai«;',  G.  zungt,  Gf't +  O.  Lat.  Jin^ta  (L. (for  i/tnga*\  a  longu&.     iwji    umi.* Allied  to  Lingual.
23850:Bugloss.  a  nlnnt.      ^  F  —  L.  —  Gk. '  ox-tongue.'— V.     bu^asse-^U-    .•'«* A\»obu^/i}Ssur.^Gk.Povy\a>ao- from  the  slmpe  of  the  leaves.  - ox  ;  yXoMia-a,  tongne.
=== SKT language
20:ENGLISH    LANGUAGE
25:ENGLISH    LANGUAGE
54:TttK  present  work  is  not  a  mere  abridgement  of  my  larger  Etymo- lopcal  Dictionary,  such  as  might  have  been  compiled  by  a  diligent book-maker,  but  has  been  entirely  rewritten  by  myself;  and  1  have Coand  that  the  experience  gained  by  writing  the  larger  work  has  been of  considerable  assistance  to  me  in  making  occasional  slight  improve- ments. My  object  has  been  to  produce  a  convenient  hand-book  for tbe  o«e  of  thai  increasing  number  of  students  who  wish  to  learn the  bistoTT  of  the  English  language,  and  who  naturally  desire  to  have Anglo-Saion  and  Icelandic  forms  presented  to  iliem  rightly  spelt  and ftOOcnniAted,  a  point  which  seldom  receives  sufficient  attention.
66:There  is  one  point  to  which  I  wish  to  draw  especial  attention.  Bf the  advice  of  a  friend,  I  procured  a  copy  of  a  Dictionary  of  English Etymology  by  the  Rev.  J.  Oswald,  written  on  an  unusual  but  excellent plan.  The  author  airanges  all  the  derivatives  of  the  Latin  cedtn under  the  heading  of  the  Latin  cedOy  so  that  words  such  as  acctdt^ concede^  recede^  succeed,  are  all  presented  to  the  eye  at  a  glance.  The advantage  of  such  an  arrangement  is  obvious,  and  I  at  once  de- termined to  adopt  it,  merely  substituting  the  representative  English word  cede  for  the  Latin  cedo,  and  so  in  other  cases.  At  the  same time,  I  adopted  two  very  considerable  improvements :  (i)  the  retention of  the  alphabetical  order  for  the  derived  words  accedcy  concede^  ftc^ with  a  cross-reference;  and  (a)  the  extension  of  the  principle  to words  of  English  and  Scandinavian  origin.  Mr.  Oswald  gives  the words  only  under  the  primary  form,  which  is  a  great  inconvenience, seeing  that  this  is  often  precisely  what  one  does  not  know ;  and,  yoA for  want  of  the  cross-reference,  he  omits  the  derivative  anctsler altogether.  At  the  same  time  I  have  found  his  book  very  useful,  as far  as  relates  to  that  part  of  our  language  which  is  of  classical  origin. With  respect  to  words  of  Teutonic  origin  it  is  practically  valueless; thus  the  only  word  given  under  W  is  the  word  wonder.
68:The  last  remark  leads  to  a  principle  of  the  first  importance  in etymology,  viz.  that  no  et3miologies  can  be  trusted  for  a  moment unless  they  can  fairly  be  shewn  to  be  consistent  with  the  ordinary phonetic  kws  which  regulate  the  various  Aryan  languages.  It  is impossible  to  piu^ue  this  matter  further  in  the  present  brief  intro- duction ;  it  must  suffice  to  lay  down  the  one  great  principle  whidi will  regulate  all  future  researches,  viz.  that  the  right  understanding  of the  vowel-sounds  lies  altogether  at  the  root  of  the  matter.
76:ICELANDIC.    Thia  language  abounds  in  somewhat  similar  vowel- tfciiigcs,  but  very  few  of  these  appear  in  English.     But  we  must  not )U9  ow  the  frequent  formation  of  derivatives  from  the  past  tenses or  plural)  and  tiie  past  participles  of  stronpf  verbs.     Thus btUa,  lit  *  to  cause  to  bite,'  is  the  causal  of  6ffay  to  bite ;  its 17  be  explained  by  the  fact  that  the  pt.  L  of  bUa  is  beii, \,  as  regards  the  Romance  languages,  especially  French,  it borne  in  mind  that  they  also  are  subject  10  phonetic  laws, is  bctUT  known  since  these  laws  have  been  sufficiently  illus- ?**«!  iu  Mr.  Kitchin's   translation  of   Brachet's   Historical    French >oimar.   In  particular,  I  may  note  that  most  French  substantives  are from  Latin  aausativfs ;  and  that  to  derive  bounly  from  botiitas \  or  honour  from  Lat.  honor  (nom.),  is  simply  impossible. Dot  a  litdc  surprising  that  many  etymological  dictionaries ignore  thti^e  most  significant,  elementary,  and  essential  facts. and  very  worthy  exception  is  £.  ^Killer's  Etymologisctics icli  der  Knglischen  Sprache. )in  a  key  to  the  plan  of  the  work,  and  a  list  of  abbrcviatioiiB.
100:§  4.  Language.     The  language  to  which  each  word  belongs distinctly  marked,  in  every  case,  by  means  of  leiters  within  marks  of parenthesis.      Here  the  symlxil  —  is  to  be  read  as  '  derived  froi Thus  Abbey  is  (F.-L.-Syriac) ;   i.e.  a  French  word  derived Latin ;  the  Latin  word  being,  in  its  turn,  of  Syrtac  origin.
105:5  5.  Symbols  of  Languages.    The  symbols,  such  as  F.  =  f  ren* are  not  used  in  their  usual  vague  sense,  so  as  to  baffle  the  enquirer who  wishes  10  find  the  words  referred  to.     Every  symbol  has  a unse^  and  has  reference  to  certain  books,  in  one  at  least  of  which word  cited  may  be  found,  as  I  have  ascertained  for  myself  by  lool ibein  all  out.     I  have  purposely  used,  as  far  as  was  practicable,  cl and  easily  accessible  authorities.     The  exact  sense  of  each  symbol  j given  in  ihc  list  btlow.
209:;ONCISE    ETYMOLOGICAL   DICTIONARY OF  THE   ENGLISH    LANGUAGE.
1408:btirbot,  a  fish.  (F.-L.)     F.  barl'ctt,^. burbot ;   named  from  its  small  beards  00 the  nose  and  chin.  —  F.  barbe,  a  beaid. Barb  (2),  a  horse.   ^F.-Barbary.)     F, barbt,  a  Barbary  hoise:  named  from  the country. Borbaroofl.  (L.-Gk.)    L.  barbants.^ Gk.  0Apl3apof.  foreign,  lit.  stammering;   a name    given   by   Greeks    to    express    the strange  sound  of  foreign  languages.    Cf.  L. baJbus,  stammering. BarbedL    as   applied    to    horses ;    see Beard. Barbel,  Barber;  sec  Barb  d). Barberry.  Berberry,  a  shrub.  (T.» Arab.)     Y*  berbcris;  Cot.  — Arab.  A*r-Wr»V, the  larbcrry-lrce.     %   The  spelling  should be  birbtry  or  batbary ;  no  coonecLion  wilb bttry. Barbic&a.  (F.  —  Arab.  7)  M.  F«  batbkan* —  F.  bsirliuant,  a  barbican  or  outwork  of  a castle;  also,  a  loop-hole;  also,  an  outlet foe   water.     Perh.ips  from  Arab.  borboAA, an  aquedncL  a  sewer  TDevic). Bard.  (C.)    W.  baniJ,  Iri^h  and  Gael. *Ani,  a  poel.
```


## [2026-09-05T20:11:49.578Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '249581,249590p' KLN_1971.txt\necho \"---\"\nsed -n '133697,133706p' KLN_1971.txt\necho \"--- lingua\"\nsed -n '138360,138372p' KLN_1971.txt"
}
```


### [2026-09-05T20:11:49.709Z] TOOL RESULT

```
tongue, n. — ME. tunge, tonge, fr. OE. tunge, rel. 
to OS., ON., Swed. tunga, Dan., OFris. tunge, 
MDu. tonghe, Du. tong, OHG. zunga , MHG., 
G. zunge, Goth, tuggo, and cogn. with OL. din- 
gua, Toch. A kantu, B kantwa (both metathes- 
ized fr. orig. *tank~), ‘tongue’. For the change 
of OL. dingua to L. lingua see lingual. The -u- in 
tongue is due to the influence of F. langue , 
‘tongue’ (fr. L. lingua ). Cp. tang, ‘spike’, and 
the second element in biltong 
---
language, n. — ME. langage, language, fr. OF. 
(= F.) langage, fr. VL. *lingudticum, fr. L. lin- 
gua, ‘tongue; speech, language’. See tongue and 
-age and cp. lingual. The spelling language 
(with u) is due to the influence of F. langue , 
‘tongue; language’. Cp. next word and languet. 
langued, adj., having the tongue of a tincture dif- 
ferent from the rest (her.) — Formed with 3rd 
suff. -ed fr. L. langue, ‘tongue’. See prec. word, 
langue d’oc, the Romance language of Southern 
--- lingua
of Italian, Spanish, French and Greek elements. 

— It., prop, ‘the language of the Franks’. See 
lingual and Frank. 

lingual, adj. — ML. lingualis, ‘pertaining to the 
tongue’, fr. L. lingua, ‘tongue, speech, language’, 
fr. OL. dingua , which is cogn. with OE. tunge, 
Goth, tuggo, ‘tongue’. See tongue and cp. lan- 
guage, langued, languet, langue d’oc, langue d’oil, 
lingo, lingula, dentilingual, bilingual, trilingual. 
The change of d (in OL. dingua) to / (in L. lingua) 
was prob. due to dialectal influence (the so-
```


## [2026-09-05T20:11:56.340Z] TOOL CALL #40: Bash

```json
{
 "command": "ls site/pages/137.jpg 2>/dev/null; pdftoppm -f 137 -l 137 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg137 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:12:01.018Z] TOOL RESULT

```
site/pages/137.jpg
total 4328
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:12 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb 746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb  60631 Sep  5 16:11 pg147.png
```


## [2026-09-05T20:12:39.866Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg137.png"
}
```


### [2026-09-05T20:12:40.256Z] TOOL RESULT

```

```


## [2026-09-05T20:12:40.240Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:12:54.054Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (225,226,227,228,229,230):\n    p=pages[i]\n    print('==== leaf',i,'-> printed?',i-15)\n    print(p[:600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:12:55.973Z] TOOL RESULT

```
232
==== leaf 225 -> printed? 210
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11. brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f. brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. d
==== leaf 226 -> printed? 211
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32. Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado. (1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23. (2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. 
==== leaf 227 -> printed? 212
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36. EU: ET TORR ON | INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne - LEXICON 203 ‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5242.11), ef. ~o- extension in Av. masya-, Skt. mártya- ($144.IV). See also wmartiya-, *Martiya-. martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ
==== leaf 228 -> printed? 213
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V). (1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà npm. DSf 50f, 52, 55. (2) ‘Egyptians’, as province: Mudräyā npm. DPe 11f. (3) ‘Egypt’: Mudráya nsm. DB 1.15, 27°; DNa 27; DSe 26°; DSm 7^; XPh 28. Mudrüyam asm. DB 1.32, 33; DZe 8. Mudrayé absm. DSf 41; DZe 11. Mudrüyaty lsm. DZe 9. ya- rel. pron. ‘who, which’, generalized by enel. -ciy (ef. Hz. ApI 355-6): Av. Skt. ya-, Gk. ds, pIE %0-. See also уйй, уада, yada-, yadry, yaniy, уйй.  ya-ciý nan~ ($105, $130, $197) РМ 57
==== leaf 229 -> printed? 214
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39. lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8). *Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an
==== leaf 230 -> printed? 215
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2. гада- sb. ‘wagon’ (570.11, $148.11), see urata-. Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192. ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60. ?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-. rādi
```


## [2026-09-05T20:13:04.802Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hazana-\\|hazàna-\\|hazána-\\|Аапат\\|Лапат\\|zbá-\\|zbà-\\|zbā-\\|zba- vb\" KNT.txt | head -20\necho \"=== search 'tongue’:'\"\ngrep -n \"‘tongue’:\" KNT.txt | head"
}
```


### [2026-09-05T20:13:04.858Z] TOOL RESULT

```
1198:OP Лапат for acc. hizénam ‘tongue’, Av. hizvà-, Skt. jthod-; see Lex. s.v. for details. $92. PIE ks became pAr. С and reverted in
=== search 'tongue’:'
```


## [2026-09-05T20:13:09.742Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hizva\\|hizvà\\|jihvā\\|jthod\\|zbay\\|azbaya\" KNT.txt | head -20\necho \"=== which leaf are the h- lexicon entries\"\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'hizv' in p or 'haz' in p and 'nam' in p:\n        pass\nfor i,p in enumerate(pages):\n    if 'LEXICON' in p:\n        import re\n        print(i, re.findall(r'LEXICON \\d+|\\d+ LEXICON',p))\nEOF"
}
```


### [2026-09-05T20:13:11.846Z] TOOL RESULT

```
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
1197:pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
1198:OP Лапат for acc. hizénam ‘tongue’, Av. hizvà-, Skt. jthod-; see Lex. s.v. for details. $92. PIE ks became pAr. С and reverted in
1496:pIE ghy: patiyazbayam, Мейтат.
2484:pIE *óhuà- (vowel quality indeterminate) and *Ghya-: pAr. Zhya-ya- ‘call’ in Skt. hváyati, OP imf, patij-azbayam.
3014:(d) Clauses of directly quoted statement as ob- ject or subject, normally without introductory conjunction: quotations of fact, with past parti- ciple or imf. ind., depending on xindsdhy and агай basdtiy, DNa 42-7; of volition, expressed by the subjunctive, depending upon amaniyaiy, DSI 3f; of wish, with the subjunctive or injunctive, de- pending upon maniyahaty, DB 4.39, DPe 20f, XPh 47; of negative command, with mà and the opt., depending upon patiyazbayam, XPh 38f; of direct question, with the imf. ind., introduced by ciya- karam ‘how many’ which is preceded by a superflu- ous tya ‘that’, and depending on тапталат, DNa 38f.
4593:38 m : viyakanam : uta : patiyazbayam : daivā :
=== which leaf are the h- lexicon entries
2 []
12 []
185 []
186 []
188 []
190 []
193 []
195 []
197 []
199 []
201 []
203 []
205 []
207 []
209 []
212 []
214 []
216 []
218 ['LEXICON 195']
220 []
222 ['LEXICON 199']
224 []
227 ['LEXICON 203']
229 []
```


## [2026-09-05T20:13:23.977Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nprint(pages[231][:1200])\nEOF"
}
```


### [2026-09-05T20:13:25.609Z] TOOL RESULT

```
232
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Wa
```


## [2026-09-05T20:13:33.110Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s \"https://archive.org/metadata/oldpers\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'),d.get('dir'))\nfor f in d['files']:\n    if 'djvu' in f['name'] or f['name'].endswith('.txt'): print(f['name'], f.get('size'))\n\" 2>&1 | head -20"
}
```


### [2026-09-05T20:13:36.609Z] TOOL RESULT

```
ia600101.us.archive.org /20/items/oldpers
oldpers_djvu.txt 944060
oldpers_djvu.xml 12640802
```


## [2026-09-05T20:13:40.526Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s -o oldpers_djvu.txt \"https://ia600101.us.archive.org/20/items/oldpers/oldpers_djvu.txt\" && wc -c oldpers_djvu.txt && grep -n \"hazana\\|hazāna\\|hizāna\\|hizana\\|zba- vb\\|zbä-\\|LEXICON 211\\|LEXICON 214\" oldpers_djvu.txt | head -20"
}
```


### [2026-09-05T20:13:43.436Z] TOOL RESULT

```
944060 oldpers_djvu.txt
```


## [2026-09-05T20:13:46.274Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ngrep -n \"LEXICON\" oldpers_djvu.txt | tail -20\necho \"=== tongue\"\ngrep -n \"tongue\" oldpers_djvu.txt | tail -10"
}
```


### [2026-09-05T20:13:46.336Z] TOOL RESULT

```
24661:LEXICON 
24936:LEXICON 
25228:LEXICON 
25509:LEXICON 
25795:LEXICON 
26071:LEXICON 
26371:LEXICON 
26641:LEXICON 
26917:LEXICON 
27196:LEXICON 195 
27468:LEXICON 
27729:LEXICON 199 
27980:LEXICON 
28249:LEXICON 203 
28527:LEXICON | 205 
28806:LEXICON 
29065:LEXICON 200 
29337:LEXICON 
29617:LEXICON 213 
29877:LEXICON 
=== tongue
1892:h*zdnam (acc.) ‘tongue’ with OP -z-, both from 
5458:OP Лапат for acc. hizénam ‘tongue’, Av. 
17509:and tongue, and put out one eye; he was kept 
17538:and nose and tongue, and put out one eye; he 
27373:kinds of men’ (‘having men of all tongues’, Wb. 
29809:hazüna- sb. ‘tongue’, graphic for hizdna- 
29820:‘tongue’, from a dialect with zb, has anaptyctic d).
```


## [2026-09-05T20:13:48.855Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nsed -n '29790,29900p' oldpers_djvu.txt"
}
```


### [2026-09-05T20:13:48.898Z] TOOL RESULT

```
harbünam, see hazdna-. 


Haldita- sb. ‘Haldita’, an Armenian, father 
of Arkha: Elam. hal-ti-da ($6, $107).  Halditahya 
(836.IVb) gsm. DB 3.79. 


һаўуа- adj. ‘true’: Ау. haifya-, Skt. satyd- 
(880, 5118.1): deriv. ($144.1V) of (Skt.) sat-, weak 
grade of pres. pte. (Skt.) sant- (8240) to root pIE 
*es- ‘be’ (Skt. as-, OP ah-), pIE *syt-yo-. Possibly 
in A6iyübauána- (Hz. Api 191-3). Cf. Lt. ab- 
sent-em, prae-sent-em, in-sont-em. — hasijam asn. 
DB 4.44. 


hazüna- sb. ‘tongue’, graphic for hizdna- 
(827), with OP z = Med. zb from ТЕ ghy ($91, 
$120): Av. hizeü- varying with hizü-, Skt. jihvå- 
perhaps to pIE root *ghyd- (see OP zbā- with 
Med. zb), with 4-reduplieation, and then, in 


OLD PERSIAN 


Iranian, dissimilation of the initial (NPers. zaban 
‘tongue’, from a dialect with zb, has anaptyctic d). 
OP stem identical with Av. hizva- (-zv- for -2b- by 
influence of collateral hizü-) extended by a suffix 
which perhaps spread from the gen. pl. ($143.IV, 
$147.11; cf. Lommel, KZ 50.261).  h*zinam 
(reading established by Cameron) asm. ($124. VT, 
$187) DB 2.74; previous reading and emendations: 
harbünam with 1° b* n° damaged, KT; h*zbénam 
Mt. MSLP 19.58-9; uzbánam Wb. ZDMG 61.726; 
hadbénam Lommel KZ 50.260-2 accepted by Bv. 
Gr. $129, cf. Kent Lg. 19.226-7. 


Hi"du- sb. ‘Sind’, a province of the Persian 
Empire, on the upper Indus River; Elam. hi-in- 
du-iš; Ау. hindu-, Skt. sindhu- ‘stream, the Indus, 
country around the Indus’ (§27, §111, §118.V, 
$158.I). See also Hiduya-. Hidus nsm. DPe 
171; DNa 25; DSe 24°; DSm 10°; XPh 25. 
Hidaw lsm. as abl. ($251D), DPh 7; DSf 44 
(йш; not hidat = Hiddva as taken by Scheil 
21.18, Konig Burgbau 34, Bv. Gr. §318); DH 5f. 


Hi”duya- adj. ‘(man) of Sind’: deriv. to pre- 
ceding ($27, §144.1II). Hiduya пзш. А?Р 13. 


hya nsm., hyd nsf., rel. pron. and def. art.; cf. 
similar forms in Skt. (Vedic) syd-s sya ‘this’: con- 
tamination of demonst. Av. Һб hà, Skt. sa-s sd, 
Gk. 64, pIE *so *sá, with relative stem pIE %о-, 
see under Yya-; cf. also hauv, hyd, hydparam. 
Decl., $198; syntax $261, §262. 

(1) rel. ‘who, which’: hya nsm. DB 1.21, 22, 49, 
51, 84, 98; 2.13 (hya-Xim), 18, 21, 23, 31, 51, 66, 
84, 95 (hya-Saty); 3.15, 30, 35, 54, 58, 70, 86, 
89°; 4.37, 38°, 41, 48°, 65, 66, 68, 68°, 68 (hya-va), 
70, 82, 87; 5.18, 34^; DPa 5f; DNa 1, 2, 3,31, 5; 
DNb 1, 2, 3, 16, 17; DSe 1, 2, 3°, 4°, 5°; DSF 1, 
2°, 2,3°, 3, 38, 40, 43, 58°; DSJ 5; DSs 1°, 2, 4°, 5°; 
DSt 1°, 2°, 3°, 4, 5°, 10°; DZe 1 bis, 2 bis, 3 bis; 
DE 2, 3, 4, 5, 7; XPa 1,2 bis, 3 bis; XPb 2, 3, 4, 5, 
7; XPe 1, 2 bis, 3, 4; XPd 1, 2, 3, 4, 5; XPf 1, 2, 
3, 4, 5, 23; XPh 1, 2 bis, 3, 4, 46, 51; XE 3, 4, 5, 
6, 7; XV 2, 3, 4 bis, 6; А:Ра 1°, 2°, 3°, 4°, 
5°; А (for gsm., §56.V); A*He 2, 3 bis, 4, 5; 
A?Pa 1, 2, 8, 4, 5. hyd nsf. DPd 8; hya as nsf. 
($5211) AmH 6. 

(2) def. art. ‘the’: hya пзш. AsH 6; DB 1.39, 
44, 46, 58, 64, 65, 70, 79 bis, 85; 2.16, 25°, 27, 
30, 40, 46, 55, 60, 87; 3.17, 25, 26, 32, 38, 45, 62, 
67, 81; 49°, 14, 27, 30^;-DBb.2, 5; рва 5; DBh 


LEXICON 


6; DBi 7; DBk 2; DPd 1; DPh 9; DSe 39; DSf 9, 
12, 18, 29, 30, 32, 37, 39; DSp 1°; DH 7; XPe 11; 
XPf 30; XPg 7; XSa 2; ХЕ 2; XV 1, 18; A!Pa 
20°; D'Sb 4^; A?Hb; A?He 1. hyd nsf. DB 1.8; 
DBa 12; DNa 56 (on hyà DPe 22, see hyà, below). 

hyd absn. of preceding as adv., ‘from this 
time on’ ($191.НІ, $198; ВЕШ. IF 12.127n, AiW 


1844); not nsf. making an attributive adj. of the 
following adv. (Foy, KZ 37.561; Mt. MSLP 19.- 


215 


55), nor 3d sg. opt of ah- ‘be’ (Thumb ap. Tm. 
Lex. 70; Hz. Арі 64). DPe 22.
```


## [2026-09-05T20:14:03.609Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ngrep -n \"zbā-\\|zba- vb\\|zbä- vb\\|zbà-\\|proclaim\" oldpers_djvu.txt | tail -20\necho \"--- around 29617 (LEXICON 213) back to 29060 (200)\"\nsed -n '29380,29420p' oldpers_djvu.txt"
}
```


### [2026-09-05T20:14:03.670Z] TOOL RESULT

```
1891:patiyazbayam ‘I proclaimed’, with Med. -zb-, but 
5455:pli ghu- in ОР patiy-azbayam Ч proclaimed’, 
29405:pati- + zbaya- ‘proclaim’ (used of prohibitions 
29812:perhaps to pIE root *ghyd- (see OP zbā- with 
--- around 29617 (LEXICON 213) back to 29060 (200)
za-za-an-nu (S120). Zazana nsm. DB 1.92. 


zürakara- sb. ‘evil-doer’ (§143.V, $160.Ia): 
zūrah- ‘evil’? (5105, $119, $120) + kara- ‘doer’ 
(899, 8122), to vb. kar-.  zürakara пэт. DB 
4.64, 68. 


zürah- sb. ‘deceit, wrong’: Av. zürah-, NPers. 
zür ‘lie’, cf. Skt. hváras- ‘crookedness, deceit, trap’ 
($9.1V, §88, $120, $156.11); see also zürakara-. 
züra asn. DB 4.65. 


Ziizahya- sb. 'Zuzahys', а town in Armenia: 
Elam. su-iz-za, АКК. zu-ú-zu (8120). Zūzahya (all 
characters visible acc. to Cameron) DB 2.33. 


2bà- vb. ‘call’ (Lg. 19.226-7; Hz. AMI 8.67, 
Apl 367): Av. zav- and zbä, pres. zbaya-, Skt. hū- 
and hed-, pres. hvaya-, plE *ghya- (Med. 2b-, 
89.V], $91, $120); see also hazdna-. 

pati- + zbaya- ‘proclaim’ (used of prohibitions 


211 


only, Ву. BSLP 42.2.70): patiyazbayam lst sg. 
imf. (§214) XPh 38. 


Zra"ka- adj. ‘Drangian’; masc. as sb., 
‘Drangiana’, a province of the Persian Empire: 
Elam. sir-ra-an-ga, АКК. za-ra-an-ga, Gk. (Hdt.) 
Lapayyat, (Polybius) Лрауүрт (Strabo) 
Apayyavh, (Arrian) Zapayya: (§9.1, $33, $88, 
$120, §128; cf. MB Gr. $119).
```


## [2026-09-05T20:14:15.077Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s \"https://archive.org/metadata/originsshortetym00part\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'),d.get('dir'))\nprint([f['name'] for f in d.get('files',[]) if f['name'].endswith(('.txt','.xml','.gz'))][:20])\n\""
}
```


### [2026-09-05T20:14:18.392Z] TOOL RESULT

```
ia600104.us.archive.org /5/items/originsshortetym00part
['originsshortetym00part_abbyy.gz', 'originsshortetym00part_chocr.html.gz', 'originsshortetym00part_dc.xml', 'originsshortetym00part_djvu.txt', 'originsshortetym00part_djvu.xml', 'originsshortetym00part_files.xml', 'originsshortetym00part_hocr_pageindex.json.gz', 'originsshortetym00part_hocr_searchtext.txt.gz', 'originsshortetym00part_marc.xml', 'originsshortetym00part_meta.xml', 'originsshortetym00part_metasource.xml', 'originsshortetym00part_scandata.xml']
```


## [2026-09-05T20:14:21.350Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s -o prt.txt \"https://ia600104.us.archive.org/5/items/originsshortetym00part/originsshortetym00part_djvu.txt\"; wc -c prt.txt; head -c 300 prt.txt"
}
```


### [2026-09-05T20:14:23.545Z] TOOL RESULT

```
4868 prt.txt
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1"
```


## [2026-09-05T20:14:27.257Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -sG 'https://ia600104.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=originsshortetym00part' --data-urlencode 'doc=originsshortetym00part' --data-urlencode 'path=/5/items/originsshortetym00part' --data-urlencode 'q=hizva' | head -c 2000"
}
```


### [2026-09-05T20:14:29.440Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Books" class="navia-link books"  href="https://archive.org/details/books" target="_top"><span class="iconochive-books" aria-hidden="true"></span><span>Books</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Video" class="navia-link movies"  href="https://archive.org/details/movies" target="_top"><span class="iconochive-movies" aria-hidden="true"></span><span>Video</span></a>
              </li>
              <li class="d
```


## [2026-09-05T20:14:40.882Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nfor id in originsetymologi0000part_j9t3 originsetymologi0000part originsshortetym0000unse; do\necho \"### $id\"\ncurl -s \"https://ia-fts.archive.org/api/v1/search/hits_inside?item_id=$id&q=hizva&size=5\" | head -c 800\necho\ndone"
}
```


### [2026-09-05T20:14:43.686Z] TOOL RESULT

```
### originsetymologi0000part_j9t3

### originsetymologi0000part

### originsshortetym0000unse
```


## [2026-09-05T20:14:49.476Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nfor id in originsetymologi0000part_j9t3 originsetymologi0000part; do\nmeta=$(curl -s \"https://archive.org/metadata/$id\")\nsrv=$(echo \"$meta\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('server',''))\")\ndir=$(echo \"$meta\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('dir',''))\")\necho \"### $id $srv $dir\"\ncurl -sG \"https://$srv/fulltext/inside.php\" --data-urlencode \"item_id=$id\" --data-urlencode \"doc=$id\" --data-urlencode \"path=$dir\" --data-urlencode \"q=hizva\" | head -c 600\necho\ndone"
}
```


### [2026-09-05T20:14:55.665Z] TOOL RESULT

```
### originsetymologi0000part_j9t3 ia902902.us.archive.org /13/items/originsetymologi0000part_j9t3
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id
### originsetymologi0000part ia801804.us.archive.org /30/items/originsetymologi0000part
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id
```


## [2026-09-05T20:15:01.783Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:15:01.788Z] TOOL RESULT

```


```


## [2026-09-05T20:15:06.490Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86",
 "prompt": "Give the full Persian etymology section for زبان (zabân): Middle Persian form, Proto-Iranian, Old Persian, Avestan, Proto-Indo-Iranian and PIE reconstructions, and any cited sources (Hasandust, MacKenzie, Cheung). Quote verbatim."
}
```


## [2026-09-05T20:15:08.424Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B9%86%C7%B5%CA%B0w%C3%A9h%E2%82%82s",
 "prompt": "Give the reconstruction, gloss, and the descendants list (Latin, Germanic, Indo-Iranian) verbatim, and any note about the Indo-Iranian forms being contaminated/influenced by another root."
}
```


### [2026-09-05T20:15:10.640Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:15:14.657Z] TOOL RESULT

```
# Persian Etymology for زبان (zabân)

Based on the Wiktionary article, here is the Persian etymology section:

**Middle Persian Forms:**
The article references Middle Persian ŠNA / ʾwzwʾn (uzwān) and 𐫙𐫉𐫇𐫀𐫗 (ʿzwʾn /izwān/).

**Proto-Iranian:**
"From Proto-Iranian *hijwáH" with comparisons to Northern Kurdish ziman, Pashto ژبه (žəba), and Avestan 𐬵𐬍𐬰𐬎𐬎𐬁 (hīzuuā).

**Proto-Indo-Iranian:**
"from Proto-Indo-Iranian *ȷ́iȷ́ʰwáH" with comparisons to Sanskrit जिह्वा (jihvā), Hindi जीभ (jībh), and Urdu جِیبھ (jībh).

**Proto-Indo-European:**
"from Proto-Indo-European *dn̥ǵʰwéh₂s" with comparisons to Old Prussian insuwis, Russian язы́к (jazýk), French langue, and English tongue.

**Cited Sources:**
MacKenzie, D. N. (1971), "uzwān", in *A concise Pahlavi dictionary*, page 85.
```


## [2026-09-05T20:15:20.822Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B8%B1%E1%B9%87%C7%B5%CA%B0w%C3%A9h%E2%82%82s",
 "prompt": "Reconstruction page for the PIE word for tongue. Give the headword, gloss, descendants (Latin dingua/lingua, Proto-Germanic *tungǭ, Proto-Indo-Iranian), and any note that the Indo-Iranian forms were remodelled/contaminated."
}
```


## [2026-09-05T20:15:21.531Z] TOOL CALL #60: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-Iranian *ȷ́iȷ́ʰwáH tongue dn̥ǵʰwéh₂s contamination"
}
```


### [2026-09-05T20:15:22.581Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:15:30.760Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-Iranian *ȷ́iȷ́ʰwáH tongue dn̥ǵʰwéh₂s contamination"

Links: [{"title":"Reconstruction:Proto-Indo-European/dn̥ǵʰwéh₂s - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s"},{"title":"Reconstruction talk:Proto-Indo-European/dn̥ǵʰwéh₂s - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction_talk:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s"},{"title":"Reconstruction:Proto-Indo-European/éǵh₂ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9%C7%B5(h%E2%82%82)"},{"title":"𐏃𐏀𐎠𐎴𐎶 - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%F0%90%8F%83%F0%90%8F%80%F0%90%8E%A0%F0%90%8E%B4%F0%90%8E%B6"},{"title":"جیب - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AC%DB%8C%D8%A8"},{"title":"زبان - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86"},{"title":"Proto-Indo-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language"},{"title":"Proto-Indo-European desiderative","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_desiderative"},{"title":"Proto-Indo-Aryan language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Aryan_language"},{"title":"Proto-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Iranian_language"}]

I found the information you were searching for. The search results show that *dn̥ǵʰwéh₂s is reconstructed as Proto-Indo-European for "tongue," with Proto-Indo-Iranian *ȷ́iȷ́ʰwáH as a descendant (though disputed, with Nuristani evidence pointing to *diȷ́ʰwáH).

The results also show multiple language examples tracing back to these reconstructions. For instance, Sanskrit जिह्वा (jihvā, "tongue") derives from Proto-Indo-Iranian *ȷ́iȷ́ʰwáH, which comes from Proto-Indo-European *dn̥ǵʰwéh₂s. Similarly, Persian زبان (zabān) derives from Proto-Iranian *hijwáH, which comes from Proto-Indo-Iranian *ȷ́iȷ́ʰwáH, ultimately from Proto-Indo-European *dn̥ǵʰwéh₂s.

These entries can be found on Wiktionary's reconstruction pages documenting the etymological connections between these proto-languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:15:35.211Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s",
 "prompt": "Give the headword, gloss, etymology notes (any mention of taboo deformation, contamination with a root meaning 'to call/invoke', or the Nuristani evidence), and the descendants for Latin, Proto-Germanic, and Proto-Indo-Iranian. Quote verbatim."
}
```


## [2026-09-05T20:15:36.300Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8F%83%F0%90%8F%80%F0%90%8E%A0%F0%90%8E%B4%F0%90%8E%B6",
 "prompt": "This is the Old Persian word hazānam/hizānam 'tongue'. Give the full entry: transliteration, meaning, etymology, and descendants."
}
```


### [2026-09-05T20:15:42.115Z] TOOL RESULT

```
# Proto-Indo-European *dn̥ǵʰwéh₂s

**Headword & Gloss:**
The entry reconstructs "*dn̥ǵʰwéh₂s" meaning "tongue," a feminine noun with oblique stem "*dn̥ǵʰuh₂-".

**Etymology Notes:**
The document states: "The root is unknown." It notes that Tocharian descendants suggest a metathetical variant "*ǵʰn̥dwéh₂-", though the timing of this metathesis is uncertain. Additionally, "Proto-Germanic *tungǭ could point to a different formation from the same root" rather than direct descent. The reconstruction notes indicate contamination with "*leyǵʰ-" ("to lick") and onomatopoetic effects help explain irregularities in descendant forms.

**Key Descendants:**

- **Latin:** Old Latin "dinguā" (closest regular reflex, lacking nominative -s)
- **Proto-Germanic:** "*tungǭ"
- **Proto-Indo-Iranian:** "*ȷ́iȷ́ʰwáH"

The entry also lists descendants in Proto-Celtic, Proto-Italic, Proto-Tocharian, Proto-Armenian, and Proto-Balto-Slavic, though Nuristani evidence is not mentioned in this document.
```


### [2026-09-05T20:15:43.159Z] TOOL RESULT

```
# Old Persian Entry: 𐏃𐏀𐎠𐎴𐎶

**Transliteration:** h-z-a-n-m (h^i zānam)

**Part of Speech:** Noun (accusative singular)

**Meanings:**
1. Tongue
2. Language

**Etymology:** This term derives from Proto-Iranian *hijwáH.

**Descendants:** The word evolved into multiple forms across Iranian languages:
- Middle Persian: izwān (Manichaean); uzwān (Book Pahlavi)
- Classical Persian: zufān, zuβān, zobân
- Modern Persian variants: Dari, Iranian Persian (zabān/zobân)
- Other branches: Tajik (zabon), Luri dialects (zun, zabu, zevö, zö)
- Judeo-Tat (zuhun)

**Historical Example:** The word appears in inscription DB 2.74, where it's used in the phrase describing: "I cut off his nose, ears, and **tongue**."
```


## [2026-09-05T20:15:49.488Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hij%C5%B5aH",
 "prompt": "Proto-Iranian reconstruction for 'tongue'. Give headword, gloss, etymology (mention of dissimilation of initial *ǰ- to h-, or contamination with a root 'to call'), and descendants (Avestan, Old Persian, Sogdian, Middle Persian)."
}
```


## [2026-09-05T20:15:50.713Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tongue",
 "prompt": "Give the full etymology of 'tongue' verbatim, including the PIE root, the Old Latin dingua note, and any remark about the Germanic/Latin irregularity."
}
```


### [2026-09-05T20:15:51.482Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:15:57.650Z] TOOL RESULT

```
# Etymology of "Tongue"

The word "tongue" derives from Old English *tunge*, tracing back through Proto-Germanic *\*tungō* to the PIE root *\*dnghu-*, meaning "tongue."

## Key Historical Points

**Origin Chain:** The term appears across Germanic languages—Old Saxon and Old Norse *tunga*, Dutch *tong*, German *Zunge*—all stemming from the same Proto-Germanic ancestor.

**Spelling Evolution:** Interestingly, "By normal evolution in Modern English it would be *\*tung*." The modern *-ue* ending represents a 14th-century attempt to indicate proper pronunciation of the *-g-*, though scholars note this result is "neither etymological nor phonetic, and is only in a very small degree historical."

**Note on Latin:** The document does not mention Old Latin *dingua* or any specific Germanic/Latin irregularity regarding the word's development. It focuses primarily on the Germanic lineage and the PIE root connection.

The verbal form (meaning "to touch with the tongue") emerged later, around 1680, derived from the noun.
```


## [2026-09-05T20:16:05.613Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG zbā\"; grep -n \"zbaH\\|zbā\\|\\*zau\\|zav-\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:16:05.653Z] TOOL RESULT

```
=== CHEUNG zbā
11948:‘dry’. © Kurd. ziha, zuhä is not from *zu-ta- (i.e. *zau, e.g. Pth. wyz’w- ‘to exude, 
30392:*zau 471 
30460:472 *zauH 
30494:*zauH ‘to call’ 
30527:gall’ < *a-zausa- ‘dis-pleasure’, *zau8. 
30541:*zauš ‘to take pleasure, rejoice in’ 
55139:*sam, *sand (s.v.), *zaus 
55368:*yarHz (s.v.), *zars', *zaus 
55891:*uab/f! , *xraus, *zauH 
56007:*uaic (s.v.), *uar(H)', *zaus 
56019:*uab/f! , *xraus, *zau H 
56345:*xsai (s.v.), *zauH (s.v.) 
56470:*yarHz (s.v.), *zars', *zaus 
57091:(s.v.), *raub (s.v.), *zaus 
57382:*haic, *Hraic, *Hmaij , *zau 
57481:*zauH (s.v.) 
57535:*yarHz (s.v.), *zars', *zaus 
58120:*kaH!, *kanH’, *naz, *zaus
```


## [2026-09-05T20:16:06.794Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index zaban\"; grep -n -i \"zaban\\|ZABAN\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"=== ARY persian\"; grep -n \"زبان\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T20:16:06.896Z] TOOL RESULT

```
=== ARY latin index zaban
4:Zabant Fats
=== ARY persian
25:نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
27:۴- برای نشان دادن خویشی زبان‌های هند و اروپایی و ریشه گیری آنها از یک سرچشمه‌ی
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
36:امیدوارم که این کتاب دوست‌داران زبان پارسی و زبانشناسی را خوش آید.
47:«هند و اروپایی» نامی است که به خانواده‌ی بزرگی از زبانها داده می‌شود. این خانواده شامل
```


## [2026-09-05T20:16:09.208Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30494,30530p' CHEUNG.txt"
}
```


### [2026-09-05T20:16:09.253Z] TOOL RESULT

```
*zauH ‘to call’ 

*AVESTAN: Zu- ‘to call’ || (+ *abi-) ‘to call upon’ || (+ *ä-) ‘to call to’ || (+ *upa-) ‘to 
call upon, invoke’ || (+ *uz-) ‘to call out’ || (+ *ni-) ‘to call off, herabrufen’ = Liste: 
69 

Pres. {1} (a)ia-: IND. 15р. YAv. äzbaiia (Y 15.1, Vr 6.1), YAv. nizbaiia (Vd 20), YAv. zbaiiemi (Y 
17.18, Y 26.1, Y 59.18, etc.), 2sg. YAv. zbaiiehi (Yt 17.17), 3sg. Y Av. zbaiieiti (Yt 10.83 f., Yt 10.86, Yt 
13.24, Yt 13.35), ҮАУ. upa.zbaiieiti (Yt 13.69), 3du. Y Av. zbaiiato (Yt 13.35), 1р1. YAv. zbaiiamahi (Yt 
12.3, Yt 12.10, Yt 12.11 ff, etc.), INJ. 3sg. YAv. zbaiiat (Yt 13.28), SUBJ.(/IND.) Isg. OAv. zbaiiä (Y 
35.5, Y 46.14, Y 51.10), Y Av. à zbaiiai (Yt 10.77 Ё), OPT. med. 2sg. Y Av. zbaiiaesa (Yt 15.49 ff.), 3sg. 
Y Av. zbaiidit (Yt 4.2), IMPV. med. Zeg YAv. nizbaiian‘ha (V 19.13 f., V 19.34); Pres. {2} them.: IND. 
3sg. YAv. zauuaiti (Y 11.1 f£), 3pl. YAv. zauuainti (Y 11.1); Partic.: pres. {1} YAv. zbaiiant-, perf. med. 
YAv. aißi.züzuiiana- (Y 8.4, N 71), perf. pass. YAv. uzbata- (Yt 13.42); Intens.: IND. lsg. OAv. 
zaozaomi (Y 43.10), med. Isg. YAv. "zaozuiie (G 1.6) 

*OLD PERSIAN: (+ pati-) zu- ‘to proclaim’ (LW) © Kent: 211a f. 

Pres. (a)ia-: impf. IND. 1sg. patiyazbayam <p-t-i-y-z-b-y-m> (XPh 38) 

*PARTHIAN: (+ *apa-) ’bzwysn ‘malediction, curse’ = DMMPP: 18b 

*SOGDIAN: SSogd. ’zw- ‘to call’, ? MSogd. zBnd ‘quarrel’ 

Pres.: IND. 15р. SSogd. ’zw’m, 35р. SSogd. ’zwtt 

*CHORESMIAN: ZD- “о curse’ = Samadi: 262 


*zgad 473 


*NEIR: Pash. zwag (m.) “noise, clamour, din’. 0 But zwag (m.) ‘bitterness, distress; 
gall’ < *a-zausa- ‘dis-pleasure’, *zau8. 

*SANSKRIT: hav’ ‘to call upon, invoke (ritually, at a sacrifice)’ (RV+) > EWAia II: 
809
```


## [2026-09-05T20:16:17.122Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30530,30545p' CHEUNG.txt"
}
```


### [2026-09-05T20:16:17.163Z] TOOL RESULT

```
809 

© This root has a good IE etymology. 

«PIE *g"euH- ‘to call upon’ — LIV: 180 f. | Pok.: 413 f. 


*IE COGNATES: OCS zsvati, Slov. zváti, Toch. B kwa- ‘to call out to, invite’ 
*REFERENCES: Werba 1997: 332; Adams 1999: 235; NEVP: 103 


*zauš ‘to take pleasure, rejoice in’ 
*AVESTAN: YAv. zus- ‘to take pleasure, rejoice in’ || (+ *a-) ‘to be joyful about 


something’ — Liste: 69
```


## [2026-09-05T20:16:22.759Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36023,36090p' POK_full.txt"
}
```


### [2026-09-05T20:16:22.826Z] TOOL RESULT

```
Root / lemma: ghau- ghaua- 

Meaning: to call, *priestess, *goddess 

Alb. shows that Root/ lemma: ghuen-: "to sound' derived from Root/ lemma: ghau-, 

ghaua-: "to call' 

Material: Old Indie havate^ call, shout, send for, call out to, summon ' (other phrase 

formations in hvayati, huve, homa, juhumasi). Pass. hOyate, participle hOta- " loaded, 

charged, filled with emotion, called', havftave \ni\n., havlman-n. "appeal, request, plea; 

prayer', hava-vn. n., havas-, havana-n. 6s., homann. " caller of the price ', hvatar-^ caller 



Avestan zavaitr calls, shouts, curses' (besides the present zbayeiti, zaozaomi), 
participle zuta- " call ', zavana-u. "shout, call, appeal, request, plea; prayer', zavan^shovX, 
call', zbafar-m. " shouter, caller'; [common alb. Romanian Iranian -v- > -b-]. 

Maybe Albanian zana^ nymph ', alb. geg {*gha-) za, zan/\o\ce, call' 

Lithuanian Z5i/e//" conjure, perform magic', Latvian zavetds., actually " somebody to 
curse something ' (compare Avestan zava/t/" enchanted, spellbound, bewitched '); 

Old Church Slavic zovg, zbvaf/^caW, shout, cry', Serbo-Croatian zovem, zvat/'caW, 
shout, cry'. Old Czech zovu, zvati, russ. zovu, zvatb ds.; in addition sloven, zovm. "shout, 
call (whether not noun post-verbal, = Old Indie hava-h, m. "shout, call'). 

Am\er\\an Jaunem ' consecrate, sanctify, bless; ordain', n-zovk" curse '; 

gr. KQuxaopai " praise, oneself, boast, brag' ( *ghaughau-, compare Avestan zaozaomi), 
from which back formation Kauxn f. " boastfulness '; 

maybe gemination alb. {*ghaughau-) ^e^e "northern alb. people. 

Old Irish guth m. "voice' ( *gutu-s); in addition gall, gutuatername a class of priests, 
probably from *ghufu-pdter lather (that is to say master) of calls (a god)'. Loth, RC 15, 224 
ff., 28, 1 1 9 ff.. Rev. Archeol. 1 925, 221 ; 



Here probably (as *ghu-t6-m "angerufenes creature '): 

Germanic *guda-n. "god' (compare Old Indie yC»^m-/7j/a-/7 "loud call', ved. epithet of 
Indras) in Gothic guf^m. "god' (the originally neutral form still in PI. ^^o'aand in galiuga- 
gul=>^ idol '), Old Icelandic god, gudu. " heathenish god'; gudm. "( Christian) god', Old 
English engl. Old Frisian asachs . godds., Old High German gotds.; 

therefrom derived Old High German gutin{na), mnl. godinne. Old English gyden 
"goddess'; Gothic ^^q^am. "(originally heathenish) priest'. Old Icelandic ^od/m. " 
heathenish priest' (Proto Norse gudija), gydjai. "priestess'; Middle High German gating 
"priest'; 

previous Christian formations are Old High German *gotfater, gotmuoter. Old English 
godfaeder. Old Norse gudfader, gudmoder' godfather, godmother ', in addition of the 
name indicating fondness also Swedish gubbe^ graybeard', gumma^ hag ', Old High 
German *goto, gota. Middle High German gd1{t)e, goi{t)e^ godfather, godmother'. 

References: WP. I 529 f., Trautmann 367; ausfiJhrl. Lithuanian by Feist 227 f. 
Page(s): 413-414 

Root / lemma: ghag^'h- 

Meaning: young of an animal or bird
```


## [2026-09-05T20:16:31.634Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"dṇg̑hū\\|dnghu\\|dngh\\|Zunge'\\|jihvā\\|hizvā\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T20:16:31.678Z] TOOL RESULT

```
45350:— s. dazu unter *dnghii ,,Zunge" — allerdings mit corn, tar a, mbret. taf fluff, 
49880:(*dngh - ; mit dh- anlautende Formen wie aor. dhak sind Neubildungen 
49925:dengh- — dngiiu, dnghua 
49953:dnghu, dnghua „Zunge“.
```


## [2026-09-05T20:16:34.704Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '49950,50010p' WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== page number nearby\"\nawk 'NR>=49900 && NR<=49960' WLD_Bd1_1930_dli_70244_djvu.txt | grep -n \"79[0-9]\""
}
```


### [2026-09-05T20:16:36.323Z] TOOL RESULT

```
leuchtens entspringen konnten (Prellwitzens, BB. 22, 129, Deutung *dhim 
*gat *moi „es kam mir in den Sinn“ iiberzeugt freilich nicht!. 

dnghu, dnghua „Zunge“. 

Altlat. d ingun , cl. lingua (mit sog. sabinischem /, das nach lingere fest 
wurde) „Zunge", germ. *timgdn-, got. tuggc >, anord. as. iunga , ags. timge, 
ahd. zunga ,,Zunge“ (als Ablautneubildung dazu vielleicht anord. tangi m. 
„in den Griff zuriickgehendes Stuck der Klinge“, mnd. tange „Sandriicken 
zwischen zwei Siimpfen“? Pick III 4 168, Falk-Torp u. tange); 

abg. (usw.) jczylcz, „Zunge; Sprache, Yolk“ (mit unerklartem rf-Abfall, 
woriiber bes. J. Schmidt Krit. 77 ; iihnlich lit. ilgas : slav. dhgz unter 
del- „lang“), apr. inzuwis „Zunge“, lit. lieziivis ds. (fiir *jziiuis nach lieziii 
„lecke“). 

Unklar ist der Anlaut von air. tenge, cymr. tafod , mcymr. tafawt , acorn. 
tauot, mcorn. tares , tavas , mbret. teaut , nbret. teod „Zunge“ (Zupitza KZ. 37, 
390 nimmt idg. Wechsel t- : d- an, Johansson IP. 2, 1 ff. idg. Anlaut zrl -, 
wie auch Pedersen KG. I S8; wenn corn, tava, mbret. taffhaff \ nbret. tanva 
,.kosten“, Loth Re. 18, 95, Henry Lex. bret. 260, 263, nicht etwa erst vom 
Worte fiir Zunge ausgegangen sind, konnten allenfalls sie das t- statt d- 
hervorgerufen haben). Noch hoffnungsloser scheint Yermittlung mit ai. 
jihvft, juhu , av. him: a, hizii „Zunge“ aus ar. sizhun , sizhu (s. Bartholomae 
KZ. 27, 207 ff., Grdr. d. iran. Phil. I 104, IA. 12, 23, Altiran. Wb. 1815 mit 
neuerer Lit.; Johanssons aaO. Ansatz *zdnglma , woraus ar. *zizhua geworden 
sei, befriedigt nicht i. Ebenso mit alb. ghihe , geg. g'ghe „Zunge“ (Peder- 
sen KZ. 38, 301, Pron. dem. 341: fiir einen Ansatz *dl- ist trotz Collitz 
BB. 29, 105, Schrijnen KZ. 46, 380 lat. lingua kaum als Stiitze verwert- 
bari. — Ir. ligiir „Zunge“(?) und arm. lezu ds. (Hiibschmann Arm. St. I 32, 
Arm. Gr. I 452) sind wohl urspriingliche Bildungen von Wz. *leigh- „lecken“ 
aus, lassen wenigstens keinen Rest von idg. mehr durchblicken. 



dens-, dent- 


793 


1. dens- „hohe Geisteskraft, weiser RatschluB; verbal: lehren, lernen". 

*densos n. : ai. damsas n. „Wunderkraft, kluge Tat“ = av. danhah- „Ge- 

schicklichkeit, Gewandtheit" (dazu ai. datiisu- „wunderkraftig“, damsistha- 
„sehr wunderkraftig" = av. dqhista- „sehr weise, der weiseste"); im Griech. 
nach tiefstufigen Formen mit *<5a[c]- = *dns- zu *davoo? umvokalisiert 
(Brugmann BSGW. 1897, 187): hom. df/vea n. pi. „Ratschlage, Anschlage", 
sg. dfjvog bei Hesych, (dor.) adaveg (-a) * dngovor/zov Hes. = (jon.) adrjvrjg ' 
ay.axog, Adv. adr/vecog Chios (SGDJ. 5653b 12); ai. purudamsas- „reich an 
Wundertaten", gr. nolvdf/vea ' noAvfiovlov Hes.; ai. damsana-m, dams&nd 
„Wunderkraft“. 

*dns-ro-s „verstandig, hochweise“ : ai. dasrd- „wundertatig“ = av. dtmra- 
„geschickt, kundig"; vgl. auch gr. ddeiga Beiname der Persephone, etwa 
„die wissende oder wunderkraftige“. daicpgcov , klugen Sinn habend" ver- 
hielte sich als *da[a\i-(pgcov zu ai. das-rd-, wie y.vdt-dveiQa zu y.vd-go-g 
(Brugmann Grdr. II 2 * 1, 78), wenn es nicht urspriinglich allein ,.den Sinn 
auf den Kampf gerichtet" bedeutet hat (vgl. dai-y.zapEvog „in der Schlacht 
getotet", ev dai „in der Schlacht'; s. zuletzt Bechtel Lexil. 92) und erst, 
=== page number nearby
23:792
```


## [2026-09-05T20:17:25.523Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86' --note 'pdf page 137, root Dinghw/Ghua, node 3: Persian زبان etymology (MP uzwān, PIr *hijwáH, PII *ȷ́iȷ́ʰwáH, PIE *dn̥ǵʰwéh₂s; cites MacKenzie 1971 p.85)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s' --note 'pdf page 137, root box: PIE *dn̥ǵʰwéh₂s tongue, descendants OLat dinguā, PGmc *tungǭ, PII *ȷ́iȷ́ʰwáH; note on contamination' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%F0%90%8F%83%F0%90%8F%80%F0%90%8E%A0%F0%90%8E%B4%F0%90%8E%B6' --note 'pdf page 137, node 5: Old Persian h(i)zānam tongue (DB 2.74), from PIr *hijwáH; descendants MP uzwān/izwān, NP zabān' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/tongue' --note 'pdf page 137, nodes 8-9: English tongue < OE tunge < PGmc *tungo < PIE *dnghu-' 2>&1 | tail -3"
}
```


### [2026-09-05T20:17:28.606Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9c5fe0ede6782890.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7cdd0fd140ebdc4d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0cc46cd13e1ad7b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2cf81f501a4c6030.txt
```


## [2026-09-05T20:17:32.655Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/language",
 "prompt": "Full etymology of 'language': Old French langage, Vulgar Latin *linguaticum, Latin lingua, Old Latin dingua, PIE root. Quote verbatim."
}
```


### [2026-09-05T20:17:38.649Z] TOOL RESULT

```
# Etymology of "Language"

The word "language" traces back through several linguistic layers:

**Medieval Origins:** The term entered English in the late 13th century from Old French *langage*, meaning "words, what is said, conversation, talk."

**Latin Foundation:** Old French *langage* derived from Vulgar Latin *linguaticum*, which came from Latin *lingua* meaning "tongue," also used for "speech, language."

**Ancient Roots:** According to the source, the Latin *lingua* is "reconstructed to be from PIE root *dnghu- 'tongue'." The *-u-* found in the English word represents "an Anglo-French insertion" that "was not originally pronounced."

**Semantic Evolution:** Early meanings focused on "words" and "conversation," but by around 1300, the sense expanded to encompass "manner of expression" and "a language" as a distinct system (like English, French, or Arabic).

The Century Dictionary definition captures this fully developed meaning: "The whole body of uttered signs employed and understood by a given community as expressions of its thoughts."
```


## [2026-09-05T20:17:41.690Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/language' --note 'pdf page 137, nodes 10-11: English language < OF langage < VL *linguaticum < L lingua (OL dingua) < PIE *dnghu-' 2>&1 | tail -2"
}
```


### [2026-09-05T20:17:43.879Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cc245cf9097c9111.txt
```


## [2026-09-05T20:17:46.427Z] TOOL CALL #75: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:17:46.465Z] TOOL RESULT

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


## [2026-09-05T20:23:40.286Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-137.json <<'JSONEOF'\n{\n  \"pdf_page\": 137,\n  \"book_page\": 107,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Dinghw, Dnghu, Ghu 2, Ghuâ\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *dn̥ǵʰwéh₂s / *dn̥ǵʰuh₂- 'tongue' (Pokorny 223 dn̥ǵhū, dn̥ǵhwā) — merged in this box with the separate root *ǵʰewH- / *ǵʰau-, *ǵʰawə- 'to call, invoke' (Pokorny 413-414)\",\n      \"note\": \"The box is really TWO Pokorny lemmas printed as one. 'Dinghw, Dnghu' is Pokorny p.223 exactly — POK_full.txt line 23335 has 'Root/ lemma: dn̥ghu, dn̥ghwā: tongue ... Page(s): 223', and Walde-Pokorny I 792 heads the same article 'dn̥ghu, dn̥ghwā „Zunge“'; Watkins/AHD likewise 'dn̥ghū. Tongue. ... [Pok. dn̥ghū 223.]'. 'Ghu 2, Ghuâ' is a DIFFERENT root, Pokorny pp.413-414 'ǵhau-, ǵhawə- : to call' (Skt. havate, hvayati, juhumasi; Av. zavaiti, zbayeiti, zaozaomi) = Cheung's *zauH 'to call' (< PIE *ǵʰewH-, 'LIV: 180 f. | Pok.: 413 f.'), and Nourai gives it no reference of its own. Putting the two in one box is not a fantasy: it is precisely the old explanation of the Indo-Iranian tongue-word that Nourai's own reference KNT states — Kent, Old Persian p.214 s.v. hazāna-: 'Av. hizvā- varying with hizū-, Skt. jihvā- perhaps to pIE root *ǵhwā- (see OP zbā- with Med. zb), with i-reduplication, and then, in Iranian, dissimilation of the initial' — and that Buck (SYN p.230, the very page cited) formulates as 'all as if fr. an IE *ǰighwā- ... and so possibly a blend of IE *dn̥ghwā- with some other word'. Walde-Pokorny I 792 is more sceptical still ('Noch hoffnungsloser scheint Vermittlung mit ai. jihvā, juhū, av. hizva, hizū „Zunge“ aus ar. *ǰizhwā, *ǰizhū'). Modern handbooks (Wiktionary after Mayrhofer EWAia) keep Skt. jihvā́- / Av. hizuuā- / OP h(i)zāna- / NPers. zabān INSIDE *dn̥ǵʰwéh₂s (via Proto-Indo-Iranian *ȷ́iȷ́ʰwáH, Proto-Iranian *hijwáH), explaining the odd initial as irregular remodelling/taboo deformation with contamination from the 'call' root rather than as descent from it. So the material of the box is right and the two roots really do meet in the Indo-Iranian tongue-word, but the box overstates a contamination as a single root, and its single gloss 'tongue' does not cover the 'call' half. Hence plausible rather than confirmed.\",\n      \"note_fa\": \"این خانه در حقیقت دو مادّهٔ جداگانهٔ پوکورنی را در یک قاب گذاشته است. «Dinghw, Dnghu» همان مادّهٔ صفحهٔ ۲۲۳ پوکورنی است: dn̥ghu, dn̥ghwā «زبان» (والده‌ـ‌پوکورنی ج۱ ص ۷۹۲ و واتکینز در پیوست American Heritage نیز همین را دارند). امّا «Ghu 2, Ghuâ» مادّهٔ دیگری است، صفحهٔ ۴۱۳–۴۱۴ پوکورنی: *ǵʰau-/ǵʰawə- «خواندن، فراخواندن» (سنسکریت havate، اوستایی zavaiti/zbayeiti)، که چونگ آن را *zauH بازسازی می‌کند و نورایی هیچ ارجاعی برای آن نمی‌آورد. آمیختن این دو بی‌پایه نیست: کنت در همان صفحهٔ ۲۱۴ که نورایی ارجاع داده می‌گوید صورت‌های hizuuā-/jihvā- «شاید» از ریشهٔ *ǵʰwā- با تکرار هجای آغازین و سپس ناهمگونی (dissimilation) در ایرانی پدید آمده‌اند، و باک (ص ۲۳۰) آن را «آمیزه‌ای از *dn̥ghwā- با واژه‌ای دیگر» می‌خواند. ولی زبان‌شناسی امروز (مایرهوفر، ویکی‌واژه) واژه‌های jihvā́-، hizuuā-، h(i)zāna- و «زبان» را همچنان زیر *dn̥ǵʰwéh₂s نگاه می‌دارد (ایرانی آغازین *hijwáH، هندوایرانی آغازین *ȷ́iȷ́ʰwáH) و بی‌قاعدگی آغاز واژه را دگرگونی نامنظّم یا تابو با اثرپذیری از ریشهٔ «خواندن» می‌داند. پس مواد نمودار درست است، امّا ادعای نورایی که این دو یک ریشه‌اند با احتیاط پذیرفتنی است، و معنای واحد «tongue» نیمهٔ «خواندن» را پوشش نمی‌دهد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s\",\n        \"https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:223\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 23335: 'Page(s): 223' closing the article whose head is 'Root/ lemma: dn̥ghu, dn̥ghwā: tongue' (OCR 'dpghu, dpghua'); material includes 'Old Latin dingua, Latin lingua', 'Gothic tuggo ... Old High German zunga', 'Old Indic jihú f. „tongue, spoon“ ... Avestan hizu m.', 'with -an- for -ā Old pers. hizbāna-, Middle Persian huzvān'. Exactly Nourai's tongue-half, including the Pahlavi form.\"\n        },\n        {\n          \"ref\": \"KNT:211\",\n          \"status\": \"supports\",\n          \"note\": \"Kent, Old Persian, Lexicon p.211 (archive.org oldpers djvu text, line 29405, page numeral '211' printed two lines below): 'zbā- vb. „call“ (Lg. 19.226-7; Hz. AMI 8.67, ApI 367): Av. zav- and zbā-, pres. zbaya-, Skt. hū- and hvā-, pres. hvaya-, pIE *ghwā- (Med. zb-, §9.VI, §91, §120); see also hazāna-.' This is the source of Nourai's 'Ghuâ' and of the 'call' words in nodes #1, #5, #7.\"\n        },\n        {\n          \"ref\": \"PRT:335\",\n          \"status\": \"not_checked\",\n          \"note\": \"Partridge, Origins, is lending-only on archive.org; the djvu text and the fulltext 'inside.php' endpoint both return 'Item not available' for originsshortetym00part, originsetymologi0000part and originsetymologi0000part_j9t3, and refs_online.json records no local copy.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"p.223, dn̥ghu / dn̥ghwā; pp.413-414, ǵhau-, ǵhawə-\",\n          \"stance\": \"partial\",\n          \"note\": \"p.223 gives the tongue root and every western form of the chart, but keeps the 'call' root apart at pp.413-414 ('Root / lemma: ghau- ghaua- / Meaning: to call ... Avestan zavaiti „calls, shouts“ (besides the present zbayeiti, zaozaomi) ... Page(s): 413-414'). Pokorny does list Skt. jihú and Av. hizu under 223, so he does put the Indo-Iranian tongue-words with *dn̥ghwā, not with *ǵhau-.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p.792, 'dn̥ghu, dn̥ghwā „Zunge“'\",\n          \"stance\": \"partial\",\n          \"note\": \"'Altlat. dingua, cl. lingua ... germ. *tungōn-, got. tuggo ... abg. językъ' — the western material as drawn. But on the Indo-Iranian side Walde-Pokorny is openly doubtful: 'Noch hoffnungsloser scheint Vermittlung mit ai. jihvā, juhū, av. hizva, hizū „Zunge“ aus ar. *ǰizhwā, *ǰizhū (s. Bartholomae ... Altiran. Wb. 1815 mit neuerer Lit.)'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 (AHD_watkins1985.txt line 403), s.v. dn̥ghū\",\n          \"stance\": \"supports\",\n          \"note\": \"'dn̥ghū. Tongue. 1. Germanic *tungōn- in: a. Old English tunge, tongue: TONGUE ... 2. Latin lingua (< Old Latin dingua), tongue, language: LANGUAGE ... [Pok. dn̥ghū 223.]' — the two AHD-tagged boxes (#8, #10) are lifted from this single entry.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck p.230, §4.26 TONGUE\",\n          \"stance\": \"supports\",\n          \"note\": \"'Skt. jihva-, Av. hizva-, hizū-, OPers. acc. sg. h(i)zbanam ..., NPers. zaban, all as if fr. an IE *ǰighwā- (init. ǰ > Iran. h; Skt. j by assim. to following palatal), and so possibly a blend of IE *dn̥ghwā- (above, 1) with some other word. Barth. 1815 with references.' Buck's 'blend' is Nourai's double-headed box, and Buck's cross-reference to Bartholomae col. 1815 is where Nourai's BRT:1815 comes from.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann pp.398-399 s.v. ǵiǵʰuā, and pp.409-410 s.v. ǵʰuhon- / ǵʰuhuos\",\n          \"stance\": \"supports\",\n          \"note\": \"p.398f: 'ǵiǵhuā „tongue“. (Redup. of type ǵhuo, ǵhuos, ǵhuōn-, etc.) Skt. jihva; Av. hizu, hizva, hizvá-; OPer. izāva, hazvàn; Pehl. huzvan, hizvan; Per. zabàn; Oss. ævzag'. Mann thus states the reduplication-of-the-'call'-root analysis as a lemma of its own, which is exactly the chart.\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"p.472, *zauH 'to call'\",\n          \"stance\": \"supports\",\n          \"note\": \"'*zauH „to call“ ... AVESTAN: zu- „to call“ ... OLD PERSIAN: (+ pati-) zu- „to proclaim“ (LW) © Kent: 211a f. ... SOGDIAN: SSogd. ʾzw- „to call“ ... SANSKRIT: hav „to call upon, invoke“ ... © This root has a good IE etymology. PIE *ǵʷeuH-/*ǵʰewH- „to call upon“ — LIV: 180 f. | Pok.: 413 f.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zav 1, zbâ : call; hizŭ, hizvâ : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Avestan lemmas are real and correctly glossed. (a) zav- / zbā- 'to call': Bartholomae's root zav- appears in the finite forms Y Av. zauuaiti (Y 11.1) beside the thematic present zbaiieiti / zbaiiemi and the Gathic intensive zaozaomi (Y 43.10); Cheung's Etymological Dictionary of the Iranian Verb p.472 lemmatises it *zauH 'to call' < PIE *ǵʰewH-, i.e. Nourai's 'Ghuâ'. The variation zav- ~ zb- is the regular Iranian treatment of PIE *ǵʰw: *ǵʰw > proto-Aryan *ȷ́ʰw > Avestan/Median zb, with a by-form zav- from the full grade *ǵʰew-. (b) hizū- m. / hizvā- f. 'tongue': Bartholomae, Altiranisches Wörterbuch col. 1815-1816 s.v. hizū- 'Zunge', with the derivatives hizu-xda- 'eloquent', hizu-drājah- 'putting out the tongue', hizū-ma- 'mouth' and the neuter hizvah-, and with the cross-references 'S. auch hizvā-. — Vgl. np. zabān, ai. jihvā- f. — Pahl.: huzvān'. The form is the Iranian reflex of Proto-Indo-Iranian *ȷ́iȷ́ʰwáH (Skt. jihvā́-), whose initial *ȷ́i- was dissimilated to hi- in Iranian (Kent §27, §91); the -zv- of hizvā- stands for older -zb- under the influence of the collateral u-stem hizū- (Kent p.214). Nourai's 'hizŭ' is Bartholomae's hizū-, 'hizvâ' his hizvā-.\",\n          \"derivation_fa\": \"هر دو مدخل اوستایی درست‌اند. یکم، ستاک zav-/zbā- «خواندن، فراخواندن»: صورت‌های zauuaiti در کنار zbaiieiti و zaozaomi گواه آن است؛ چونگ (ص ۴۷۲) آن را *zauH از هندواروپایی *ǵʰewH- می‌گیرد، یعنی همان «Ghuâ» نورایی. دگرگونی آوایی روشن است: *ǵʰw هندواروپایی در ایرانی به zb بدل می‌شود و صورت درجهٔ کامل *ǵʰew- به zav-. دوم، hizū- (مذکر) و hizvā- (مؤنث) «زبان»: بارتولومه در ستون ۱۸۱۵ فرهنگ ایرانی باستان آن را با ترکیب‌های hizu-xda- «سخنور» و hizū-ma- «دهان» آورده و خود می‌افزاید «قس. فارسی نو زبان، سنسکریت jihvā-؛ پهلوی huzvān». این صورت بازماندهٔ هندوایرانی آغازین *ȷ́iȷ́ʰwáH است که آغاز آن در ایرانی به hi- ناهمگون شده و zv در آن به جای zb کهن‌تر، به اثرپذیری از hizū-، نشسته است. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:211,214\",\n              \"status\": \"supports\",\n              \"note\": \"p.211 s.v. zbā-: 'Av. zav- and zbā-, pres. zbaya-, Skt. hū- and hvā-, pres. hvaya-, pIE *ghwā- (Med. zb-)'; p.214 s.v. hazāna-: 'Av. hizvā- varying with hizū-, Skt. jihvā-'. Both Avestan words of the box, with both glosses, come straight from these two Kent entries (archive.org oldpers djvu text lines 29405 and 29809).\"\n            },\n            {\n              \"ref\": \"SYN:230\",\n              \"status\": \"supports\",\n              \"note\": \"Buck §4.26 TONGUE, p.230 (SYN.txt line 5971 ff.): 'Av. hizva-, hizī-' in the table and, in §4, 'Skt. jihva-, Av. hizva-, hizū-'.\"\n            },\n            {\n              \"ref\": \"PRT:335\",\n              \"status\": \"not_checked\",\n              \"note\": \"Partridge, Origins — lending-only on archive.org, no local copy (see root ref_check).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1815-1816, s.v. hizū-\",\n              \"stance\": \"supports\",\n              \"note\": \"'hizū- m. „Zunge“ ... uta nāham uta gaušā uta hizuvam frājanam Bh. 2.73' [the Old Persian quotation Bartholomae adds], with 'Kompp. u. Ableit. — S. auch hizvā-. — Vgl. np. zabān, ai. jihvā- f. — Pahl.: huzvān.' Nearby: 'hizvah- n. „Zunge“', 'hizvā- f. „Zunge“', 'hizu-xda- Adj. „beredt“', 'hizū-ma- m. „Mund“'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p.472, *zauH\",\n              \"stance\": \"supports\",\n              \"note\": \"'*AVESTAN: zu- „to call“ ... Pres. {1} (a)ia-: ... YAv. zbaiiemi ..., Pres. {2} them.: IND. 3sg. YAv. zauuaiti (Y 11.1 f.) ... Intens.: IND. 1sg. OAv. zaozaomi (Y 43.10)' — Nourai's 'zav 1, zbâ' are Cheung's two present stems of one root.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.413-414, ǵhau-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Avestan zavaiti „calls, shouts, curses“ (besides the present zbayeiti, zaozaomi), participle zuta- „call“, zavana- n. „shout, call, appeal“ ... zbātar- m. „shouter, caller“'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"uzvân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi uzwān [written ʾwzwʾn], Manichaean Middle Persian ʿzwʾn (izwān), 'tongue, language'. MacKenzie, A Concise Pahlavi Dictionary p.85: 'uzwān [ŠNʾ < A liššān; ʾwzwʾn | M ʿzwʾn, (N zabān)] tongue, language', with the by-form 'zuwān [zwbʾn] = uzwān' and the compound pād-uzwān 'reticent'. The word continues Old Iranian *hizwān- (the -ān- stem also seen in OP hizāna-/hazāna-, Kent p.214): initial *hi- was reduced to u-/i- in Middle Persian (whence the prothetic spelling ʾwzwʾn and the Manichaean ʿzwʾn), the medial -zw- being retained. Nourai's 'uzvân' is MacKenzie's uzwān letter for letter; the aspirated variant huzvān that Pokorny (p.223, 'Middle Persian huzvān') and Horn (no. 650, 'phlv. uzvān bezw. huzvān, zuvān bezw. zavān') print is the same word. The chart's arrow Avestan → Pahlavi is a chart convention: Middle Persian does not descend from Avestan but from the South-West Old Iranian dialect represented by OP hizāna-, of which Avestan hizvā- is the sister form.\",\n          \"derivation_fa\": \"پهلوی کتابی uzwān (نوشتهٔ ʾwzwʾn) و پهلوی مانوی ʿzwʾn (izwān) به معنی «زبان». مکنزی در فرهنگ کوچک پهلوی ص ۸۵ می‌نویسد: «uzwān [ŠNʾ؛ ʾwzwʾn | M ʿzwʾn، (N زبان)] tongue, language» و صورت دیگر «zuwān [zwbʾn] = uzwān» را هم می‌آورد. این واژه دنبالهٔ ایرانی باستان *hizwān- است — همان ستاک ـان که در پارسی باستان hizāna-/hazāna- دیده می‌شود — و در فارسی میانه هجای آغازین hi- سست و به u-/i- بدل شده است؛ پوکورنی (ص ۲۲۳) و هرن (شمارهٔ ۶۵۰) صورت huzvān را هم ثبت کرده‌اند. پیکان «اوستایی ← پهلوی» در نمودار قراردادی است: فارسی میانه از اوستایی نمی‌آید، بلکه از گویش جنوب‌باختری ایرانی باستان که پارسی باستان نمایندهٔ آن است، و hizvā- اوستایی خواهرِ آن است نه مادرش. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The Pahlavi box carries no reference of its own in the printed chart (p.107); the surrounding boxes carry PRT:335 / BRT:1815 / IEC:409,410, which do cover the Pahlavi form (Bartholomae col. 1815 'Pahl.: huzvān'; Mann p.398 'Pehl. huzvan, hizvan').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p.85 s.v. uzwān (PHD_mackenzie.txt line 5100; PHD.txt lines 684, 2561, 4030)\",\n              \"stance\": \"supports\",\n              \"note\": \"'uzwan [ŠNʾ < A lšnʾ; ʾwzwʾn | M ʿzwʾn, (N zaban)] tongue, language'; also 'zuwan [zwbʾn] = uzwan' and the English index 'tongue uzwān, (zuwān)', 'language uzwān, (zuwān)'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 3896, 4121)\",\n              \"stance\": \"partial\",\n              \"note\": \"the simplex is not lemmatised, but the derivative is: 'uzvaneh [ʾwzwʾnyh], v. pāt-uzvānēh' and, in the entry vicēhītan, 'han i visp vicēhīt uzvānēh — the universal knowledge of languages'. Nyberg's transcription uzvān(ēh) matches Nourai's 'uzvân'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 650 (HRN.txt lines 5758-5762)\",\n              \"stance\": \"supports\",\n              \"note\": \"'zabān, zubān „Zunge“ ... ap. hizavan(?) „die Zunge“; aw. hizū; phlv. uzvān bezw. huzvān, zuvān bezw. zavān; ai. jihvā-.' Both Pahlavi variants of the box.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann p.398 s.v. ǵiǵʰuā\",\n              \"stance\": \"supports\",\n              \"note\": \"'Pehl. huzvan, hizvan: Per. zabàn'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"zabân «زبان» : tongue, language; hozvân «هزوان» : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"(a) NP زبان zabān 'tongue, language' < MP uzwān / zuwān (spelt zwbʾn). Hübschmann, Persische Studien (chapter on Old Persian v), states the sound law: 'Ap. v ist zu b geworden in zabān, zubān „Zunge“ = phl. zuvān (geschrieben zubān) ..., zd. hizva-' — i.e. intervocalic Old/Middle Persian -w- was written and then pronounced -b- in New Persian, and the initial syllable hi-/u- was lost by aphaeresis, giving hizwān- > (u)zwān > zubān/zabān; the a of the first syllable is anaptyctic (Kent p.214: 'NPers. zabān „tongue“, from a dialect with zb, has anaptyctic a'). Classical Persian still shows zufān/zuβān beside zabān. (b) NP هزوان hozvān 'tongue' is the same word preserved without the aphaeresis, i.e. a doublet of zabān going back directly to Pahlavi huzvān; Mo'in's Farhang-e Fārsi lemmatises it 'هزوان: (اِ) زبان، لسان', and Mann prints 'Per. hazvān, zabān' side by side. Both words are therefore genuine and the arrow Pahlavi → Persian is right for both. The chart's gloss 'tongue, language' for zabān is correct: the sense 'language' is the usual secondary extension of 'tongue' (Buck §4.26: 'Most of the words for „tongue“ are also used for „language“').\",\n          \"derivation_fa\": \"الف) «زبان» فارسی نو از فارسی میانهٔ uzwān/zuwān (نوشتهٔ zwbʾn) می‌آید. هوبشمان در «مطالعات فارسی» قاعدهٔ آوایی را روشن می‌گوید: «و در پارسی باستان در زبان، زُبان به ب بدل شده است = پهلوی zuvān (نوشتهٔ zubān)، اوستایی hizva-»؛ یعنی هجای آغازین hi-/u- افتاده (aphaeresis) و w میان‌واکه‌ای به b بدل شده است، و کنت می‌افزاید که «الف» نخست، واکهٔ میانجی (anaptyctic) است. در فارسی کلاسیک هنوز zufān/zuβān در کنار zabān دیده می‌شود. ب) «هزوان» همان واژه است بی افتادن هجای آغازین، یعنی دوگانهٔ (doublet) «زبان» که یکسر از پهلوی huzvān می‌آید؛ معین در فرهنگ فارسی آن را «هزوان: (اِ) زبان، لسان» آورده و مان هم «Per. hazvān, zabān» را کنار هم می‌گذارد. پس هر دو واژه اصیل‌اند و پیکان «پهلوی ← فارسی» برای هر دو درست است. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%A8%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/%F0%90%8F%83%F0%90%8F%80%F0%90%8E%A0%F0%90%8E%B4%F0%90%8E%B6\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BRT:1815\",\n              \"status\": \"supports\",\n              \"note\": \"Bartholomae col. 1815 s.v. hizū- closes with 'Vgl. np. zabān, ai. jihvā- f. — Pahl.: huzvān' — the New Persian word is named there, exactly as Nourai's arrow requires. (The column number is Buck's own cross-reference on SYN p.230, 'Barth. 1815 with references', which is presumably where Nourai took it from.)\"\n            },\n            {\n              \"ref\": \"IEC:409,410\",\n              \"status\": \"supports\",\n              \"note\": \"Mann, IEC pp.409-410 (leaf 237 of the archive scan, margin numerals 409/410/411): s.v. ǵʰuhon- 'Av. hizu, gs hizvō & hizva, f. ... n. „tongue“; OPer. hazāna-, m., id.; Pers. hazvān, zabān, id.'; s.v. ǵʰuhuos '„shout, call, appeal“ ... Skt. hū, adj. „calling“; juhū, jihva „tongue“ ... Av. zavō „call“; hizu ... Per. cf. hazvān, zabān'. Mann's 'hazvān' is Nourai's 'hozvân'.\"\n            },\n            {\n              \"ref\": \"BQT:1003\",\n              \"status\": \"partial\",\n              \"note\": \"Borhān-e Qāṭeʿ in Moʿin's edition: the ز-ب chapter opens on printed p.1004 (BQT_v2_pages.txt leaf 464, 'باب دوم') and the headword 'زبان ۱: بفتح اول معروف است ... را لسان گویند، وضم اول هم درست است' stands at the top of p.1005 (leaf 465) — i.e. within one or two pages of the cited 1003, the residual uncertainty being the ±2 drift of the leaf→page offset for vol. 2. Borhān/Moʿin thus confirm the word and both readings zabān/zobān, but there is no etymological footnote on that page (no Latin-script Pahlavi/Avestan form appears on leaves 464-466), so the reference supports the word, not the Avestan→Pahlavi→Persian route.\"\n            },\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin, Farhang-e Fārsi (MON_part2.txt line 90114): 'هزوان: [...] (اِ) زبان، لسان' — the rarer of Nourai's two Persian words is a real Moʿin headword with exactly the chart's gloss.\"\n            },\n            {\n              \"ref\": \"PRT:335\",\n              \"status\": \"not_checked\",\n              \"note\": \"Partridge, Origins — lending-only, no accessible copy.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien, §on Old Persian v (HUB.txt line 5883)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ap. v ist zu b geworden in zabān, zubān „Zunge“ = phl. zuvān (geschrieben zubān) Bd. and Ind. 150, zd. hizva-.'\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 650 (HRN.txt lines 5758-5763)\",\n              \"stance\": \"supports\",\n              \"note\": \"'zabān, zubān (AM.) „Zunge“, zefān ...; ap. hizavan(?) „die Zunge“; aw. hizū; phlv. uzvān bezw. huzvān, zuvān bezw. zavān; ai. jihvā-. kurd. azmān „Zunge“; afgh. zibā; oss. t. ævzāg', with the footnote 'Vorsichtige Form; Bartholomae, BB. XIV, 245 vermutet hizvani'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part2.txt line 90114, s.v. هزوان\",\n              \"stance\": \"supports\",\n              \"note\": \"'هزوان: (اِ) زبان، لسان.'\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2, printed p.1005 (leaf 465), s.v. زبان\",\n              \"stance\": \"partial\",\n              \"note\": \"'زبان ۱: بفتح اول معروف است ... را لسان گویند، وضم اول هم درست است' — word and both vocalisations, but no etymological note.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. زبان (Persian)\",\n              \"stance\": \"supports\",\n              \"note\": \"'From Middle Persian ʾwzwʾn (uzwān) ... from Proto-Iranian *hijwáH ... from Proto-Indo-Iranian *ȷ́iȷ́ʰwáH ... from Proto-Indo-European *dn̥ǵʰwéh₂s', citing MacKenzie 1971 p.85.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for زبان returns only running prose in Aryanpur's preface (lines 25-47) and the Latin index yields no 'ZABAN' headword; the word has no entry of its own in the copy on disk.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`zb`k : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian ʾzβʾk(h) (Buddhist, Manichaean and Christian scripts), read (ə)zβāk 'tongue'. Gharib's Sogdian Dictionary, entry 2296 on printed p.91, prints exactly 'ʾzβʾk(h) B, M, S — (ə)zβāk — tongue' and adds the etymological tag '< Av. hizva', with the derivative 2297 ʾzβʾkwyδʾk (ə)zβāk-wēδē 'root of the tongue'. The form is Old Iranian *hizwā- enlarged by the very common Sogdian nominal suffix -ak (< *-aka-): *hizwā-ka- > *(h)izβāk > ʾzβʾk, with loss of the initial h- and prothetic aleph (the same reduction of the first syllable that gives MP uzwān). Nourai's transliteration '`zb`k' is the usual ASCII rendering of ʾzβʾk (aleph = `, β = b). The arrow from the Avestan box is again a convention for 'Old Iranian': Sogdian is an Eastern Iranian language and does not descend from Avestan, but Gharib herself states the Avestan comparison.\",\n          \"derivation_fa\": \"سغدی ʾzβʾk(h) (در هر سه خطّ بودایی، مانوی و مسیحی)، خوانده (ə)zβāk «زبان». قریب در فرهنگ سغدی، مدخل ۲۲۹۶ در صفحهٔ ۹۱، همین صورت را با معنی tongue می‌آورد و خود می‌افزاید «< اوستایی hizva»، و مدخل ۲۲۹۷ ʾzβʾkwyδʾk «بُنِ زبان» را در پی آن می‌گذارد. صورت سغدی از ایرانی باستان *hizwā- با پسوند پرکاربرد ـak (< *-aka-) ساخته شده است: *hizwā-ka- > *(h)izβāk، با افتادن h آغازین و افزودن الف پیشین — همان فرسایش هجای آغازین که در uzwān پهلوی هم دیده می‌شود. آوانویسی نورایی «`zb`k» همان ʾzβʾk است. پیکان از خانهٔ اوستایی، مانند دیگر جاها، به جای «ایرانی باستان» است؛ سغدی زبانی ایرانی خاوری است و از اوستایی نمی‌آید. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:91\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, entry 2296 (SOD_pages.txt leaf 156 ≈ printed p.90-91, per the documented 'printed page ≈ leaf − 66'): 'ʾzβʾk(ʾ) B, M, S | (ə)zβak (ʾzβāk) ⓔ<Av. hizva = *zβʾk | tongue | VJ 880; TSP 5.32; Sogdica. 5; GMS 93; KG 383; MDii A-14.6; MSP c14; Frag. Len. 29.9 ʾzβʾkh ...'. Both the word and the Avestan derivation Nourai draws are on the cited page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"entries 2296-2297, p.91\",\n              \"stance\": \"supports\",\n              \"note\": \"2296 'ʾzβʾk(ʾ) ... tongue ... ⓔ<Av. hizva'; 2297 'ʾzβʾkwyδʾk S — (ə)zβak-wēδē — root of the tongue'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p.472, *zauH\",\n              \"stance\": \"partial\",\n              \"note\": \"'*SOGDIAN: SSogd. ʾzw- „to call“ ... Pres.: IND. 1sg. SSogd. ʾzwʾm, 3sg. SSogd. ʾzwtt' — Sogdian preserves the verb of the 'call' half of Nourai's root box as well as the noun; Cheung does not treat the noun.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.223\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny's article on dn̥ghwā lists Avestan, Old Persian, Middle Persian and 'North Aryan' (Khotanese) but no Sogdian form.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Old Persian\",\n          \"words\": \"zbâ : call; hizana, hazana : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are Kent's own Old Persian lemmas. (a) zbā- 'to call', attested only in the compound pati-zbaya-, imperfect 1 sg. patiyazbayam 'I proclaimed' (Xerxes, XPh 38, the 'daiva inscription'); Kent p.211: 'zbā- vb. „call“ ... Av. zav- and zbā-, pres. zbaya-, Skt. hū- and hvā-, pres. hvaya-, pIE *ǵhwā- (Med. zb-)'. The -zb- is a Median (north-west Iranian) feature: genuine Old Persian would show -z-, so patiyazbayam is a loan from the chancery language, as Kent §11 and §91 note and Cheung marks with '(LW)'. (b) hazāna- 'tongue', written h-z-a-n-m and read h(i)zānam (acc. sg.) in DB 2.74, Darius' account of mutilating Fravartiš: 'I cut off his nose and ears and tongue'. Kent p.214: 'hazāna- sb. „tongue“, graphic for hizāna- (§27), with OP z = Med. zb from IE ǵhw'. Nourai's doublet 'hizana, hazana' reproduces Kent's own pair (graphic hazāna- vs. phonetic hizāna-); the reading was established by Cameron against the older harbānam / hizbānam / uzbānam conjectures Kent lists.\",\n          \"derivation_fa\": \"هر دو واژه از مدخل‌های خودِ کنت در فرهنگ پارسی باستان است. الف) zbā- «خواندن، ندا دادن»، تنها در ترکیب pati-zbaya- و صورت ماضی نقلی patiyazbayam «اعلام کردم» در کتیبهٔ دیوهای خشایارشا (XPh ۳۸) به کار رفته است؛ کنت (ص ۲۱۱): «zbā- فعل „خواندن“ ... اوستایی zav- و zbā-، سنسکریت hū- و hvā-، هندواروپایی *ǵʰwā- (مادی zb-)». خوشهٔ -zb- ویژگی گویش مادی است و در پارسی باستانِ اصیل باید -z- می‌بود؛ پس این فعل وام‌واژهٔ دیوانی از مادی است (چونگ آن را با نشانهٔ LW آورده). ب) hazāna- «زبان»، نوشتهٔ h-z-a-n-m و خواندهٔ h(i)zānam (رایی مفرد) در بیستون ۲/۷۴، آنجا که داریوش می‌گوید بینی و گوش و زبان فرورتیش را برید. کنت (ص ۲۱۴): «hazāna- „زبان“، نوشتاری برای hizāna-، با z پارسی باستان = zb مادی از *ǵʰw هندواروپایی». دوگانهٔ «hizana, hazana» در نمودار همان جفت کنت است. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%F0%90%8F%83%F0%90%8F%80%F0%90%8E%A0%F0%90%8E%B4%F0%90%8E%B6\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:211,214\",\n              \"status\": \"supports\",\n              \"note\": \"p.211: 'zbā- vb. „call“ (Lg. 19.226-7; Hz. AMI 8.67, ApI 367): Av. zav- and zbā-, pres. zbaya-, Skt. hū- and hvā-, pres. hvaya-, pIE *ghwā- (Med. zb-, §9.VI, §91, §120); see also hazāna-. pati- + zbaya- „proclaim“ ... patiyazbayam 1st sg. imf. (§214) XPh 38.' p.214: 'hazāna- sb. „tongue“, graphic for hizāna- (§27), with OP z = Med. zb from IE ghw (§91, §120): Av. hizvā- varying with hizū-, Skt. jihvā- perhaps to pIE root *ghwā- ... h(i)zānam (reading established by Cameron) asm. DB 2.74'. Both of Nourai's Old Persian lines, both glosses and both spellings are on the two cited pages.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"§27, §91, §187 (KNT.txt lines 401, 1197-1198, 2214)\",\n              \"stance\": \"supports\",\n              \"note\": \"'PIE ghw became pAr. ȷ́ʰw, and then Med. and Av. zb, Skt. hv, but OP z; the OP texts have one example of the Median value and one of the OP value: ... OP patiy-azbayam „I proclaimed“, Av. root zbā-, Skt. pres. hvayati. OP h(i)zānam for acc. hizānam „tongue“, Av. hizvā-, Skt. jihvā-'; and §187 'it is an extension of the stem seen in Av. hizvā- (see Lex. s.v. hazāna-)'.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1815 s.v. hizū-\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae quotes the Bisotun passage under the Avestan lemma: 'uta nāham uta gaušā uta hizuvam frājanam Bh. 2.73' — his reading (hizuvam) of the same accusative Kent reads h(i)zānam.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann pp.398, 409\",\n              \"stance\": \"partial\",\n              \"note\": \"'OPer. izāva, hazvàn' (p.398) and 'OPer. hazāna-, m., id.' (p.409); Mann's 'izāva' is one of the discarded older readings, his hazāna- is Kent's.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck p.230 §4.26\",\n              \"stance\": \"partial\",\n              \"note\": \"'OPers. acc. sg. h(i)zbanam (for reading, cf. Kent, Language 19.226 f.)' — Buck still prints the -zb- reading that Kent later replaced by h(i)zānam.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language label, no reference, no word, no gloss. It mirrors the position of the filled Persian box that hangs to the right of the Pahlavi box above it, so it is almost certainly an unfinished or accidentally blanked frame left in the author's drawing (the same kind of stray empty frame occurs elsewhere in the book). The extraction is faithful: the JSON's node #6 with lang null and an empty word list is exactly what the page shows.\",\n          \"derivation_fa\": \"چیزی برای بررسی نیست: در صفحهٔ چاپی ۱۰۷ (برگ ۱۳۷ پی‌دی‌اف) قابی که در سمت راستِ خانهٔ «پارسی باستان» آویخته است کاملاً خالی است — نه نام زبانی دارد، نه ارجاعی، نه واژه‌ای و نه معنایی. جای آن درست قرینهٔ خانهٔ «فارسی» است که در بالا از «پهلوی» آویخته؛ پس به احتمال بسیار قابِ ناتمام یا سهواً خالی‌مانده‌ای در نقشهٔ خودِ مؤلف است. خوانش اسکن درست است و داده‌ها همان چیزی را نشان می‌دهند که در کتاب چاپ شده: خانه‌ای تهی.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the box carries no reference (and no content) on the printed page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"Nourai (printed page)\",\n              \"where\": \"EtymologicalDictionary-persian-english.pdf p.137 = book p.107, rendered with pdftoppm -r 200\",\n              \"stance\": \"silent\",\n              \"note\": \"the frame to the right of 'Old Persian | zbâ : call / hizana, hazana : tongue' is drawn but empty; the JSON matches the page, so this is a defect of the book, not of the extraction.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"hŭ, hvâ : call; jihva : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"(a) Sanskrit hū- / hvā- 'to call, invoke', present hváyati, middle huvé, reduplicated juhūmasi, agent hótar- 'invoker, priest': Kent p.211 pairs 'Skt. hū- and hvā-, pres. hvaya-' with Av. zav-/zbā- under pIE *ǵʰwā-, and Pokorny pp.413-414 lists 'Old Indic havate „call, shout, send for, summon“ (other phrase formations in hvayati, huve, homa, juhumasi)'. Skt. h- is the regular Indic outcome of PIE *ǵʰ before w (PIE *ǵʰw > Indo-Iranian *ȷ́ʰw > Skt. hv, Iranian zb). (b) Sanskrit jihvā́- f. 'tongue' (RV+), beside the u-stem juhū́- 'tongue, sacrificial ladle': the initial ji- is a reduplication of the same *ǵʰw- syllable on the older analysis (Kent, Mann), or an irregular remodelling of PIE *dn̥ǵʰwéh₂- under the influence of juhóti 'pours the offering' on the standard modern analysis (Mayrhofer, followed by Wiktionary's Proto-Indo-Iranian *ȷ́iȷ́ʰwáH). Either way the word and gloss of the box are right, and Skt. jihvā́- is the exact counterpart of Av. hizvā-, differing only in the palatal assimilation of the first consonant (Buck: 'Skt. j by assim. to following palatal').\",\n          \"derivation_fa\": \"الف) سنسکریت hū-/hvā- «خواندن، فراخواندن»، حال hváyati، وجه میانی huvé، صورت مضاعف juhūmasi و اسم فاعل hótar- «زمزمه‌گر، موبد»: کنت (ص ۲۱۱) آن را در کنار zav-/zbā- اوستایی زیر *ǵʰwā- هندواروپایی می‌گذارد و پوکورنی (ص ۴۱۳) صورت‌های havate، hvayati، huve و juhumasi را می‌آورد. h سنسکریت بازتاب قانونمند *ǵʰ هندواروپایی پیش از w است (*ǵʰw > هندوایرانی *ȷ́ʰw > سنسکریت hv، ایرانی zb). ب) سنسکریت jihvā́- «زبان» (از ریگ‌ودا به بعد) در کنار ستاک u‑دار juhū́- «زبان؛ ملاقهٔ قربانی». هجای آغازین ji- را بر پایهٔ تحلیل کهن‌تر (کنت، مان) تکرار همان هجای *ǵʰw- می‌دانند و بر پایهٔ تحلیل امروزی (مایرهوفر، و به پیروی او ویکی‌واژه با هندوایرانی آغازین *ȷ́iȷ́ʰwáH) دگرگونی نامنظّم *dn̥ǵʰwéh₂- زیر اثر juhóti «می‌ریزد (قربانی)». به هر روی واژه و معنای این خانه درست است و jihvā́- برابر دقیق hizvā- اوستایی است؛ تفاوت تنها در همگونی نخستین همخوان با کامی پس از آن است (باک). ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:211\",\n              \"status\": \"supports\",\n              \"note\": \"s.v. zbā-: 'Skt. hū- and hvā-, pres. hvaya-, pIE *ghwā-'; and s.v. hazāna- (p.214) 'Skt. jihvā- perhaps to pIE root *ghwā- ... with i-reduplication'. Nourai's two Sanskrit lines with their two glosses are Kent's.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.223 and pp.413-414\",\n              \"stance\": \"partial\",\n              \"note\": \"p.223 puts the noun with the tongue root — 'Old Indic jihú f. „tongue, spoon“ (with u after juhoti „pour into the fire“ ...), Avestan hizu m. ds.'; pp.413-414 put the verb with the call root — 'Old Indic havate „call, shout ...“ (other phrase formations in hvayati, huve, homa, juhumasi)'. So Pokorny splits what Nourai's box joins, but names the same juhoti influence.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann p.398 s.v. ǵiǵʰuā and p.410 s.v. ǵʰuhuos\",\n              \"stance\": \"supports\",\n              \"note\": \"'ǵiǵhuā „tongue“. (Redup. of type ǵhuo ...) Skt. jihva ...'; 'Skt. hū, adj. „calling“; juhū, jihva „tongue“; havah „invocation“ in Vedic'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck p.230 §4.26\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. jihva-, Av. hizva-, hizū-, OPers. acc. sg. h(i)zbanam ..., NPers. zaban, all as if fr. an IE *ǰighwā- (init. ǰ > Iran. h; Skt. j by assim. to following palatal)'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p.472, *zauH\",\n              \"stance\": \"supports\",\n              \"note\": \"'*SANSKRIT: hav „to call upon, invoke (ritually, at a sacrifice)“ (RV+) > EWAia II: 809'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"tungôn : tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *tungōn- f. 'tongue', an n-stem: Gothic tuggō, Old Norse/Old Saxon tunga, Old English tunge, Old High German zunga, Middle Dutch tonghe. It continues PIE *dn̥ǵʰwéh₂- with two well-known irregularities: the initial *d- appears as Germanic t- instead of the expected þ- (by Grimm's law *d > t, which is regular; it is Latin that is irregular in turning d- into l-), and the ā-stem was recharacterised as an n-stem (*-ōn-), Pokorny p.223 'Gothic tuggō ... with -on- instead of -ā'. Watkins/AHD gives the node verbatim: 'dn̥ghū. Tongue. 1. Germanic *tungōn- in: a. Old English tunge, tongue: TONGUE; b. Middle Dutch tonghe: BILTONG.' Nourai's 'tungôn' is that starred form with the asterisk dropped.\",\n          \"derivation_fa\": \"ژرمنی آغازین *tungōn- (مؤنث، ستاک n‑دار) «زبان»: گوتی tuggō، نورس باستان و ساکسون باستان tunga، انگلیسی باستان tunge، آلمانی علیای باستان zunga. این صورت دنبالهٔ *dn̥ǵʰwéh₂- هندواروپایی است با دو بی‌قاعدگی شناخته‌شده: نخست، *d آغازین بنا بر قانون گریم به t بدل شده (که قاعده‌مند است؛ بی‌قاعده لاتینی است که d را به l بدل کرده)، و دوم، ستاک ā‑دار به ستاک n‑دار بازساخته شده است (پوکورنی ص ۲۲۳: «گوتی tuggō ... با ـon به جای ـā»). واتکینز در پیوست فرهنگ American Heritage همین خانه را عیناً می‌آورد. آنچه نورایی «tungôn» نوشته همان صورت بازسازی‌شدهٔ ستاره‌دار است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tongue\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 403: 'dn̥ghū. Tongue. 1. Germanic *tungōn- in: a. Old English tunge, tongue: TONGUE; b. Middle Dutch tonghe, tongue: BILTONG. ... [Pok. dn̥ghū 223.]' Nourai's reference is just 'AHD' without a page; the 1975 New College appendix ran pp.1505-1550 alphabetically, so 'dn̥ghū' falls in the expected place there.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.223\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic tuggō f., Old Norse Old Saxon tunga, Old English tunge, Old High German zunga, with -on- instead of -ā'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.792\",\n              \"stance\": \"supports\",\n              \"note\": \"'germ. *tungōn-, got. tuggō, anord. as. tunga, ags. tunge, ahd. zunga „Zunge“'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. tongue (KLN_1971.txt line 249581)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. tunge, tonge, fr. OE. tunge, rel. to OS., ON., Swed. tunga ... OHG. zunga, MHG., G. zunge, Goth. tuggo, and cogn. with OL. dingua, Toch. A kantu, B kantwa'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"tongue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English tunge f. > Middle English tunge, tonge > Modern English tongue. The word is inherited, not borrowed: OE tunge is the direct continuation of Proto-Germanic *tungōn-. The spelling is the only oddity — Klein: 'The -u- in tongue is due to the influence of F. langue „tongue“ (fr. L. lingua)'; Etymonline agrees that 'by normal evolution in Modern English it would be *tung', the -ue being a 14th-c. device to keep the -g- hard, 'neither etymological nor phonetic'. The semantic range 'organ of speech' → 'language' (mother tongue, the tongues of men) matches the same shift in Latin lingua and Persian zabān.\",\n          \"derivation_fa\": \"انگلیسی باستان tunge (مؤنث) ← انگلیسی میانه tunge/tonge ← انگلیسی نو tongue. این واژه میراثی است نه وام‌واژه: tunge دنبالهٔ مستقیم *tungōn- ژرمنی آغازین است. تنها نکتهٔ ناهنجار، املا است؛ کلاین می‌گوید «u در tongue از اثر langue فرانسوی است»، و اتیمآنلاین می‌افزاید که سیر طبیعی واژه در انگلیسی نو *tung می‌شد و ـue را در سدهٔ چهاردهم برای سخت نگاه‌داشتن g افزوده‌اند، که «نه ریشه‌شناختی است نه آوایی». گسترش معنایی «اندام گفتار» به «زبان (لسان)» همان است که در lingua لاتینی و «زبان» فارسی هم رخ داده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tongue\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the English box carries no reference of its own; the parent Germanic box's 'AHD' covers it ('Old English tunge, tongue: TONGUE').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. tongue\",\n              \"stance\": \"supports\",\n              \"note\": \"'tongue, n. — ME. tunge, tonge, fr. OE. tunge ... The -u- in tongue is due to the influence of F. langue, „tongue“ (fr. L. lingua).'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Tongue (SKT.txt line 19862)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Tongue. (E.) M.E. tunge. + Icel., Swed. tunga, Du. tong, G. zunge, Goth. tuggo + O. Lat. dingua (L. lingua) ... Allied to Lingual.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. dn̥ghū\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old English tunge, tongue: TONGUE'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"dingua, lingua : tongue, language\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Latin dingua (quoted as such by the Roman grammarians, e.g. Marius Victorinus) > Classical Latin lingua 'tongue; speech, language'. dingua is the phonologically closest reflex of PIE *dn̥ǵʰwéh₂- anywhere in the family (Wiktionary: 'the closest regular reflex, lacking nominative -s'); the change d- > l- is not a regular Latin sound law but is usually explained either as a Sabine/dialectal feature (Latin has other d/l doublets: dacruma/lacrima, dautia/lautia) or as contamination with lingere 'to lick' — Pokorny p.223 'Latin lingua (with l from lingere)', Walde-Pokorny I 792 'cl. lingua (mit sog. sabinischem l, das nach lingere fest wurde)', Klein 'The change of d (in OL. dingua) to l (in L. lingua) was prob. due to dialectal influence'. Both of Nourai's glosses are Latin senses: lingua is 'tongue' and, from Plautus and Cicero on, 'language, dialect'.\",\n          \"derivation_fa\": \"لاتینی باستان dingua (که دستورنویسان رومی خود آن را نقل کرده‌اند) ← لاتینی کلاسیک lingua «زبان؛ گفتار، زبانِ قومی». صورت dingua نزدیک‌ترین بازتاب قاعده‌مند *dn̥ǵʰwéh₂- در سراسر خانوادهٔ هندواروپایی است. بدل شدن d آغازین به l قانون آوایی لاتینی نیست؛ آن را یا ویژگی گویشی سابینی می‌دانند (قس. dacruma/lacrima و dautia/lautia) و یا اثرپذیری از lingere «لیسیدن»: پوکورنی (ص ۲۲۳) «lingua با l از lingere»، والده‌ـ‌پوکورنی (ج۱ ص ۷۹۲) «lingua کلاسیک با لامِ به‌اصطلاح سابینی که پس از lingere استوار شد»، و کلاین «تبدیل d به l احتمالاً اثر گویشی است». هر دو معنایی که نورایی آورده معنای واقعی lingua است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/language\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dn%CC%A5%C7%B5%CA%B0w%C3%A9h%E2%82%82s\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 403: '2. Latin lingua (< Old Latin dingua), tongue, language: LANGUAGE, LANGUET, LIGULE, LINGO, LINGUA, LINGUIST; (BILINGUAL). [Pok. dn̥ghū 223.]' — Nourai's Latin box and its two glosses are this clause verbatim.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p.223\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old Latin dingua, Latin lingua (with l from lingere); Oscan fangvam'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.792\",\n              \"stance\": \"supports\",\n              \"note\": \"'Altlat. dingua, cl. lingua (mit sog. sabinischem l, das nach lingere fest wurde) „Zunge“'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. lingual (KLN_1971.txt line 138366)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ML. lingualis ... fr. L. lingua, „tongue, speech, language“, fr. OL. dingua, which is cogn. with OE. tunge, Goth. tuggo, „tongue“ ... The change of d (in OL. dingua) to l (in L. lingua) was prob. due to dialectal influence'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"language\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin lingua 'tongue, speech' → Vulgar Latin *linguāticum (an -āticum abstract, the same suffix as in viāticum > voyage) → Old French langage 'words, what is said, conversation' → Middle English langage (late 13th c., 'words, conversation'; by c.1300 also 'a language, a tongue such as English or French') → language. Klein: 'language, n. — ME. langage, language, fr. OF. (= F.) langage, fr. VL. *linguāticum, fr. L. lingua, „tongue; speech, language“ ... The spelling language (with u) is due to the influence of F. langue.' Etymonline concurs, adding that the -u- 'is an Anglo-French insertion' that 'was not originally pronounced'. Watkins lists LANGUAGE among the English descendants of Latin lingua under the same root, so Nourai's arrow Latin → English is right, with Old French as the (unshown) intermediary.\",\n          \"derivation_fa\": \"لاتینی lingua «زبان، گفتار» ← لاتینی عامیانه *linguāticum (اسم معنا با پسوند ـāticum، همان که در viāticum ← voyage دیده می‌شود) ← فرانسوی باستان langage «سخن، گفت‌وگو» ← انگلیسی میانه langage (اواخر سدهٔ سیزدهم؛ از حدود ۱۳۰۰ به معنی «زبانِ قومی») ← language. کلاین می‌نویسد: «language از انگلیسی میانه langage، از فرانسوی باستان langage، از لاتینی عامیانه *linguāticum، از lingua لاتینی»؛ و می‌افزاید که املای u‑دار از اثر langue فرانسوی است، و اتیمآنلاین آن را «افزودهٔ انگلوـ‌نورمانی» می‌خواند که در آغاز تلفّظ نمی‌شده است. واتکینز نیز LANGUAGE را در شمار بازماندگان lingua زیر همین ریشه می‌آورد. پس پیکان «لاتینی ← انگلیسی» درست است و تنها حلقهٔ فرانسوی باستان در نمودار نیامده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/language\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the English box carries no reference of its own; the parent Latin box's 'AHD' covers it ('Latin lingua ... : LANGUAGE').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. language (KLN_1971.txt line 133697)\",\n              \"stance\": \"supports\",\n              \"note\": \"'language, n. — ME. langage, language, fr. OF. (= F.) langage, fr. VL. *linguāticum, fr. L. lingua, „tongue; speech, language“. See tongue and -age and cp. lingual.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. dn̥ghū\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin lingua (< Old Latin dingua), tongue, language: LANGUAGE, LANGUET, LIGULE, LINGO, LINGUA, LINGUIST'.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"s.v. language\",\n              \"stance\": \"supports\",\n              \"note\": \"'late 13c., from Old French langage „words, what is said, conversation, talk“, from Vulgar Latin *linguaticum, from Latin lingua „tongue“, also „speech, language“ ... reconstructed to be from PIE root *dnghu- „tongue“.'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-137.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 137"
}
```


### [2026-09-05T20:23:42.351Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 10, 'unverified': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 10, 'not_checked': 6, 'partial': 1}
books consulted: {'supports': 28, 'partial': 6, 'silent': 3} | by book: {'POK': 5, 'KLN': 4, 'CHEUNG': 3, 'IEC': 3, 'BRT': 2, 'HRN': 2, 'SYN': 2, 'WLD': 2, 'AHD': 2, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'MON': 1, 'BQT': 1, 'Wiktionary': 1, 'ARY': 1, 'SOD': 1, 'KNT': 1, 'Nourai (printed page)': 1, 'SKT': 1, 'Etymonline': 1}
```


## [2026-09-05T20:24:04.220Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-137.json` written; `verify_check.py 137` reports **11/11 nodes, 0 PROBLEM lines**.

**Page 137 (book p.107), one entry: root "Dinghw, Dnghu, Ghu 2, Ghuâ : tongue"**

- Root: **plausible** (1). Node verdicts: **confirmed 10, unverified 1**.
- Ref checks: supports 10, partial 1 (BQT:1003), not_checked 6 (PRT:335 ×3 + three boxes that print no refs). Books consulted: 37 entries across POK, WLD, AHD, SYN, IEC, KNT, BRT, PHD, NYB, HRN, HUB, CHEUNG, SOD, BQT, MON, ARY, KLN, SKT, Etymonline, Wiktionary.

Key findings:
- The root box merges **two** Pokorny lemmas: *dn̥ǵʰū/dn̥ǵʰwā* "tongue" (POK 223 — cited) and *ǵʰau-/ǵʰawə-* "to call" (POK 413-414 — **not** cited by Nourai). That merger is not invented: Kent p.214 and Buck p.230 both explain the Indo-Iranian tongue-word as a reduplication/"blend" involving the 'call' root, and Mann even lemmatises it (IEC p.398 *ǵiǵʰuā*). Modern handbooks instead keep jihvā́-/hizuuā-/zabān inside *dn̥ǵʰwéh₂s with contamination from the 'call' root. Hence root = plausible, not confirmed; the single gloss "tongue" also fails to cover the 'call' half.
- Every word on the page checks out against the cited pages. Kent pp.211 and 214 are exact (`zbā- vb. 'call' … pIE *ǵʰwā-`; `hazāna- sb. 'tongue', graphic for hizāna-`), Bartholomae col. 1815 is exact (hizū- with "Vgl. np. zabān … Pahl.: huzvān"), Buck p.230 is exact (and is where BRT:1815 came from), Gharib entry 2296 on p.91 is exact and even carries the "< Av. hizva" tag, Mann pp.409-410 are exact. MacKenzie p.85 `uzwān … (N zabān)` and Hübschmann's `Ap. v ist zu b geworden in zabān` back the Pahlavi→Persian link; Mo'in has هزوان "زبان، لسان".
- No `disputed` and no `transcription_suspect` items. **No extraction errors** — the JSON matches the printed page exactly.

Two things worth the owner's attention (neither is a data bug):
- **Node #6 is an empty box in the printed book** (a blank double-ruled frame hanging off the Old Persian box, mirroring the Persian box above). Marked `unverified`; the extraction is faithful.
- **BQT:1003** is off by ~2 pages: the زبان headword sits at the top of printed p.1005 (BQT_v2 leaf 465) and the ز-ب chapter opens on p.1004; also there is no Mo'in etymological footnote on those leaves, so the reference supports the word but not the route. Marked `partial`.
- **PRT:335** (Partridge, Origins) could not be checked — all three archive.org identifiers return "Item not available" for both the djvu text and the fulltext search endpoint, and there is no local copy.

The file is written but not committed.
